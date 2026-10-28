"""Synthetic-only tests for the independent conventional comparator."""
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'research' / 'upb-validation'))
from upb_baseline import conventional
from concordia_comparator import (ConcordiaAnalysis, fit_concordia_age,
                                  mahalanobis2, parameter_count,
                                  sample_chi2)


def on_curve_sample(age, n=5, rho=0.3):
    r68, r75 = conventional(age)
    return [ConcordiaAnalysis(r68, r75, max(r68 * .01, 1e-6),
                               max(r75 * .01, 1e-6), rho)
            for _ in range(n)]


class ComparatorTests(unittest.TestCase):
    def test_zero_residual_on_curve(self):
        sample = on_curve_sample(1000e6)
        self.assertAlmostEqual(sample_chi2(sample, 1000e6), 0.0)

    def test_recovers_noise_free_ages(self):
        for age in (100e6, 1000e6, 2500e6):
            fit = fit_concordia_age(on_curve_sample(age))
            self.assertAlmostEqual(fit['age_years'] / 1e6, age / 1e6, places=2)
            self.assertLess(fit['chi2'], 1e-9)

    def test_parameter_count_is_one_for_any_sample_size(self):
        for n in (1, 3, 12):
            self.assertEqual(parameter_count(n), 1)
            fit = fit_concordia_age(on_curve_sample(500e6, n=n))
            self.assertEqual(fit['parameter_count'], 1)
            self.assertEqual(fit['degrees_of_freedom'], 2 * n - 1)

    def test_rho_direction_along_and_cross_axis(self):
        # Displacement along the correlation axis is cheaper with
        # positive rho; against it, dearer. Exact values: for z1 = z2
        # = z, chi2 = 2 z^2 / (1 + rho); for z1 = -z2, 2 z^2 / (1 - rho).
        base = conventional(1000e6)
        s68, s75 = base[0] * .01, base[1] * .01
        along = ConcordiaAnalysis(base[0] + s68, base[1] + s75, s68, s75, 0.9)
        cross = ConcordiaAnalysis(base[0] + s68, base[1] - s75, s68, s75, 0.9)
        self.assertAlmostEqual(mahalanobis2(along, base), 2 / 1.9)
        self.assertAlmostEqual(mahalanobis2(cross, base), 2 / 0.1)

    def test_rho_changes_fit_in_expected_direction(self):
        # Coherent along-axis displacements: with the true rho the fit
        # is not dragged as far from the true age as with rho forced
        # to zero (which is never an admissible substitution under the
        # gate; it is used here only to prove rho is actually used).
        age = 1000e6
        r68, r75 = conventional(age)
        s68, s75 = r68 * .01, r75 * .01
        sample = [ConcordiaAnalysis(r68 + k * s68, r75 + k * s75,
                                     s68, s75, 0.9)
                  for k in (-2, -1, 0, 1, 2, 3)]
        fit_rho = fit_concordia_age(sample)
        relabeled = [ConcordiaAnalysis(o.r68, o.r75, o.sigma68,
                                       o.sigma75, 0.0) for o in sample]
        fit_zero = fit_concordia_age(relabeled)
        self.assertLess(abs(fit_rho['age_years'] - age),
                        abs(fit_zero['age_years'] - age))
        self.assertGreater(abs(fit_rho['age_years'] - fit_zero['age_years']),
                           1e6)

    def test_rejects_invalid(self):
        with self.assertRaises(ValueError):
            fit_concordia_age([])
        with self.assertRaises(ValueError):
            fit_concordia_age([ConcordiaAnalysis(.2, .4, .01, .02, 1.0)])
        with self.assertRaises(ValueError):
            fit_concordia_age([ConcordiaAnalysis(.2, .4, 0.0, .02, 0.0)])
        with self.assertRaises(ValueError):
            fit_concordia_age(on_curve_sample(1e8), max_age_years=0)


if __name__ == '__main__':
    unittest.main()
