"""Synthetic-only tests for the side-by-side comparison harness."""
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'research' / 'upb-validation'))
from upb_covariance import RatioObservation
import comparison_harness as harness


class HarnessTests(unittest.TestCase):
    def test_concordant_cases_both_recover_age(self):
        truths = {'concordant_100Ma': 100e6, 'concordant_1000Ma': 1000e6,
                  'concordant_2500Ma': 2500e6}
        for name, observations in harness.standard_cases():
            if name not in truths:
                continue
            report = harness.run_comparison(name, observations)
            for side in ('conventional', 'rci'):
                self.assertAlmostEqual(
                    report[side]['age_years'] / truths[name], 1.0,
                    delta=0.02, msg=f'{name} {side}')

    def test_initialized_case_statistics(self):
        observations = dict(harness.standard_cases())['initialized_800Ma']
        report = harness.run_comparison('initialized_800Ma', observations)
        self.assertLess(report['rci']['chi2'],
                        0.05 * report['conventional']['chi2'])
        self.assertGreater(report['rci']['log_likelihood'],
                           report['conventional']['log_likelihood'])

    def test_discordant_case_fits_poorly_on_both_sides(self):
        observations = dict(harness.standard_cases())['discordant_1500Ma']
        report = harness.run_comparison('discordant_1500Ma', observations)
        for side in ('conventional', 'rci'):
            reduced = (report[side]['chi2'] /
                       report[side]['degrees_of_freedom'])
            self.assertGreater(reduced, 50, msg=side)

    def test_report_shape_and_parameter_counts(self):
        report = harness.run_comparison(
            'shape', harness.synthetic_sample(500e6, 6, seed=7))
        self.assertEqual(report['conventional']['parameter_count'], 1)
        self.assertEqual(report['rci']['parameter_count'], 3)
        self.assertEqual(report['rci']['identifiability'],
                         'unanchored_translation_degenerate')
        # The gate defines no comparison margin yet: the report must
        # carry raw statistics only, with no verdict machinery.
        self.assertNotIn('verdict', report)
        for side in ('conventional', 'rci'):
            for key in report[side]:
                self.assertNotIn('parity', key)
                self.assertNotIn('winner', key)
                self.assertNotIn('margin', key)

    def test_relabeled_rho_changes_harness_result(self):
        sample = harness.synthetic_sample(1000e6, 10, rel_sigma=0.02,
                                          rho=0.9, seed=2)
        as_published = harness.run_comparison('rho_as_published', sample)
        relabeled = [RatioObservation(o.r68, o.r75, o.sigma68, o.sigma75,
                                      0.0) for o in sample]
        as_zero = harness.run_comparison('rho_relabeled_zero', relabeled)
        self.assertGreater(
            abs(as_published['conventional']['age_years']
                - as_zero['conventional']['age_years']), 1e6)


if __name__ == '__main__':
    unittest.main()
