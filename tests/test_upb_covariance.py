import math
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'research' / 'upb-validation'))
from upb_baseline import conventional
from upb_covariance import RatioObservation, mahalanobis2, log_likelihood, fit_age

class CovarianceTests(unittest.TestCase):
    def test_zero_residual(self):
        o = RatioObservation(.2, .4, .01, .02, .7)
        self.assertAlmostEqual(mahalanobis2(o, (.2,.4)), 0)
    def test_independent_errors(self):
        o = RatioObservation(.2,.4,.01,.02,0)
        self.assertAlmostEqual(mahalanobis2(o, (.21,.44)), 5)
    def test_correlated_errors(self):
        o = RatioObservation(.2,.4,.01,.02,.5)
        self.assertAlmostEqual(mahalanobis2(o, (.21,.42)), 4/3)
    def test_symmetric_covariance(self):
        o = RatioObservation(.2,.4,.01,.02,-.3)
        self.assertTrue(math.isfinite(log_likelihood(o, (.21,.42))))
    def test_reject_invalid(self):
        for o in (RatioObservation(.2,.4,0,.02,0), RatioObservation(.2,.4,.01,.02,1), RatioObservation(.2,.4,.01,.02,float('nan')), RatioObservation(-.2,.4,.01,.02,0)):
            with self.assertRaises(ValueError):
                mahalanobis2(o, (.2,.4))
    def test_fit_conventional_synthetic(self):
        for age in (1e6, 100e6, 1000e6, 4500e6):
            a,b = conventional(age)
            o=RatioObservation(a,b,max(a*.01,1e-6),max(b*.01,1e-6),.2)
            f=fit_age(o)
            self.assertAlmostEqual(f['age_years']/1e6,age/1e6,places=4)
            self.assertLess(f['chi2'],1e-9)
    def test_fixed_initialized_synthetic(self):
        from upb_baseline import initialized
        age=800e6
        a,b=initialized(age,.03,.07)
        f=fit_age(RatioObservation(a,b,.001,.002,.1),initial68=.03,initial75=.07)
        self.assertAlmostEqual(f['age_years']/1e6,800,places=4)
    def test_bad_age_bound(self):
        with self.assertRaises(ValueError):
            fit_age(RatioObservation(.1,.2,.01,.02,0),max_age_years=0)

if __name__=='__main__': unittest.main()
