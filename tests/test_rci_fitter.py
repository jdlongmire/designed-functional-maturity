"""Synthetic-only tests for the shared-parameter RCI fitter."""
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'research' / 'upb-validation'))
from upb_baseline import conventional, initialized
from upb_covariance import RatioObservation
import rci_fitter
from concordia_comparator import ConcordiaAnalysis, fit_concordia_age
import comparison_harness as harness


def exact_sample(age, a68=0.0, a75=0.0, n=5, rho=0.3):
    r68, r75 = initialized(age, a68, a75)
    return [RatioObservation(r68, r75, max(r68 * .01, 1e-6),
                             max(r75 * .01, 1e-6), rho)
            for _ in range(n)]


class RCIFitterTests(unittest.TestCase):
    def test_zero_initial_sample_recovers_conventional_age(self):
        fit = rci_fitter.fit_unit(exact_sample(1000e6))
        self.assertLess(fit['chi2'], 1e-9)
        self.assertAlmostEqual(fit['age_years'] / 1e6, 1000, delta=1.0)
        self.assertLess(fit['initial68'], 0.01)
        self.assertLess(fit['initial75'], 0.01)

    def test_unanchored_flag_and_exact_fit_on_initialized_points(self):
        # Free initials + free age are not separately identifiable for
        # one unit (module docstring); the fit must still find an exact
        # representative (chi2 ~ 0) and must carry the flag.
        fit = rci_fitter.fit_unit(exact_sample(800e6, .03, .07))
        self.assertLess(fit['chi2'], 1e-6)
        self.assertEqual(fit['identifiability'],
                         'unanchored_translation_degenerate')
        prediction = initialized(fit['age_years'], fit['initial68'],
                                 fit['initial75'])
        truth = initialized(800e6, .03, .07)
        self.assertAlmostEqual(prediction[0], truth[0], places=9)
        self.assertAlmostEqual(prediction[1], truth[1], places=7)

    def test_translation_identity(self):
        a68t, a75t = rci_fitter.translated_initials(50e6, .04, .09)
        for age in (100e6, 500e6, 2000e6, 4000e6):
            p1 = initialized(age, .04, .09)
            p2 = initialized(age + 50e6, a68t, a75t)
            self.assertAlmostEqual(p1[0], p2[0], delta=1e-9 * max(1, p1[0]))
            self.assertAlmostEqual(p1[1], p2[1], delta=1e-9 * max(1, p1[1]))

    def test_fixed_initials_recover_age_and_count_one_parameter(self):
        fit = rci_fitter.fit_unit(exact_sample(800e6, .03, .07),
                                  fixed_initials=(.03, .07))
        self.assertAlmostEqual(fit['age_years'] / 1e6, 800, delta=0.5)
        self.assertEqual(fit['parameter_count'], 1)
        self.assertEqual(fit['identifiability'],
                         'initials_fixed_independently')

    def test_parameter_sharing_counts_do_not_scale_with_grains(self):
        self.assertEqual(rci_fitter.unit_parameter_count(3), 3)
        self.assertEqual(rci_fitter.unit_parameter_count(12), 3)
        self.assertEqual(rci_fitter.group_parameter_count(2, 10), 4)
        self.assertEqual(rci_fitter.group_parameter_count(2, 200), 4)
        fit_small = rci_fitter.fit_unit(exact_sample(500e6, n=3))
        fit_large = rci_fitter.fit_unit(exact_sample(500e6, n=12))
        self.assertEqual(fit_small['parameter_count'],
                         fit_large['parameter_count'])

    def test_anchored_group_recovers_shared_initials_and_ages(self):
        ages = {'U0': 500e6, 'U1': 1200e6, 'U2': 2000e6}
        units = {u: exact_sample(a, .04, .09, n=4) for u, a in ages.items()}
        fit = rci_fitter.fit_group(units, anchor_ages={'U0': 500e6})
        self.assertEqual(fit['identifiability'],
                         'anchored_by_independent_age')
        self.assertEqual(fit['parameter_count'], 4)
        self.assertAlmostEqual(fit['initial68'], .04, delta=0.002)
        self.assertAlmostEqual(fit['initial75'], .09, delta=0.002)
        for uid, age in ages.items():
            self.assertAlmostEqual(fit['units'][uid]['age_years'], age,
                                   delta=5e5)

    def test_group_fixed_initials_recover_all_ages(self):
        ages = {'U0': 500e6, 'U1': 1200e6, 'U2': 2000e6}
        units = {u: exact_sample(a, .04, .09, n=4) for u, a in ages.items()}
        fit = rci_fitter.fit_group(units, fixed_initials=(.04, .09))
        self.assertEqual(fit['parameter_count'], 3)
        for uid, age in ages.items():
            self.assertAlmostEqual(fit['units'][uid]['age_years'], age,
                                   delta=5e5)

    def test_noisy_initialized_sample_beats_conventional_chi2(self):
        # Machinery signal only: shared initials absorb the initialized
        # offset that the conventional model cannot. No parity claim.
        sample = harness.synthetic_sample(800e6, 8, seed=14,
                                          initial68=.03, initial75=.07)
        rci = rci_fitter.fit_unit(sample)
        conv = fit_concordia_age([ConcordiaAnalysis(
            o.r68, o.r75, o.sigma68, o.sigma75, o.rho) for o in sample])
        self.assertLess(rci['chi2'], 0.05 * conv['chi2'])
        self.assertGreater(rci['log_likelihood'], conv['log_likelihood'])

    def test_bounds_and_validation(self):
        fit = rci_fitter.fit_unit(exact_sample(300e6, .02, .02))
        self.assertGreaterEqual(fit['initial68'], 0.0)
        self.assertLessEqual(fit['initial68'], fit['initial_bounds'][1])
        with self.assertRaises(ValueError):
            rci_fitter.fit_unit([])
        with self.assertRaises(ValueError):
            rci_fitter.fit_unit(exact_sample(1e8), initial_bounds=(2.0, 1.0))
        with self.assertRaises(ValueError):
            rci_fitter.fit_group({'U': exact_sample(1e8)},
                                 anchor_ages={'ZZ': 1e8})
        with self.assertRaises(TypeError):
            rci_fitter.fit_unit([ConcordiaAnalysis(.2, .4, .01, .02, .3)])


if __name__ == '__main__':
    unittest.main()
