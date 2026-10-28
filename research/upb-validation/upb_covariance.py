"""Two-ratio covariance-aware U-Pb pilot likelihood, closed-system only.

Input: corrected radiogenic 206Pb*/238U, 207Pb*/235U ratios, absolute 1-sigma
uncertainties and their correlation. Common Pb, disequilibrium, systematic
uncertainty and between-grain covariance must be handled upstream or later.
"""
import math
from dataclasses import dataclass
from upb_baseline import conventional, initialized

@dataclass(frozen=True)
class RatioObservation:
    r68: float
    r75: float
    sigma68: float
    sigma75: float
    rho: float

    def validate(self):
        values = (self.r68, self.r75, self.sigma68, self.sigma75, self.rho)
        if not all(math.isfinite(x) for x in values):
            raise ValueError('non-finite measurement')
        if self.sigma68 <= 0 or self.sigma75 <= 0 or not -1 < self.rho < 1:
            raise ValueError('invalid covariance (must be positive definite)')
        if self.r68 < 0 or self.r75 < 0:
            raise ValueError('negative corrected radiogenic ratio')

def mahalanobis2(obs, prediction):
    """Squared Mahalanobis residual; valid for within-analysis correlation."""
    obs.validate()
    z1 = (obs.r68 - prediction[0]) / obs.sigma68
    z2 = (obs.r75 - prediction[1]) / obs.sigma75
    return (z1*z1 - 2*obs.rho*z1*z2 + z2*z2) / (1 - obs.rho*obs.rho)

def log_likelihood(obs, prediction):
    obs.validate()
    det = (obs.sigma68*obs.sigma75)**2 * (1 - obs.rho**2)
    return -0.5 * (mahalanobis2(obs, prediction) + math.log(det) + 2*math.log(2*math.pi))

def fit_age(obs, *, initial68=0.0, initial75=0.0, max_age_years=4.6e9):
    """Bounded 1D minimization; initialization terms are fixed, never fitted here."""
    obs.validate()
    if not all(math.isfinite(v) and v >= 0 for v in (initial68, initial75, max_age_years)) or max_age_years <= 0:
        raise ValueError('invalid model bounds')
    def score(t):
        return mahalanobis2(obs, initialized(t, initial68, initial75))
    # Coarse scan prevents assuming convexity across the full age domain.
    n = 256
    step = max_age_years/n
    j = min(range(n+1), key=lambda i: score(i*step))
    a, b = max(0, (j-1)*step), min(max_age_years, (j+1)*step)
    phi = (math.sqrt(5)-1)/2
    c, d = b-phi*(b-a), a+phi*(b-a)
    for _ in range(100):
        if score(c) < score(d):
            b, d = d, c
            c = b-phi*(b-a)
        else:
            a, c = c, d
            d = a+phi*(b-a)
    t = (a+b)/2
    return {'age_years': t, 'chi2': score(t), 'prediction': initialized(t, initial68, initial75)}
