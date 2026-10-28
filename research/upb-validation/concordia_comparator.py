"""Independent conventional Wetherill concordia comparator.

Implements gate item 5 of EMPIRICAL_GATE_v0.2: a standard Wetherill
concordia age and a correlated-residual (Mahalanobis) likelihood for a
sample of corrected radiogenic ratio analyses.

Independence: this module deliberately shares no fitting internals with
the RCI-side building block (upb_covariance.py). It has its own
observation type, its own Mahalanobis / log-likelihood evaluation and its
own bounded minimizer. The only shared code is upb_baseline.py (decay
constants and the closed-system forward curve), which is generic math,
plus the standard library.

Scope boundary (per the gate): closed-system conventional model only.
Common Pb, U-series disequilibrium and Pb loss are not modeled here;
the gate requires any later such treatments to be modeled symmetrically
on both sides of the comparison.
"""
import math
from dataclasses import dataclass
from upb_baseline import conventional

# Decay constants are those of upb_baseline.py: Jaffey et al. (1971)
# central values (half-lives 4.4683 Ga for U-238, 0.70381 Ga for U-235).


@dataclass(frozen=True)
class ConcordiaAnalysis:
    """One corrected radiogenic two-ratio analysis with published rho."""
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


def _validate_sample(analyses):
    analyses = list(analyses)
    if not analyses:
        raise ValueError('empty sample: at least one analysis is required')
    for a in analyses:
        a.validate()
    return analyses


def mahalanobis2(analysis, prediction):
    """Squared Mahalanobis residual for one analysis (own implementation)."""
    analysis.validate()
    z1 = (analysis.r68 - prediction[0]) / analysis.sigma68
    z2 = (analysis.r75 - prediction[1]) / analysis.sigma75
    return (z1 * z1 - 2 * analysis.rho * z1 * z2 + z2 * z2) / (1 - analysis.rho * analysis.rho)


def log_likelihood(analysis, prediction):
    analysis.validate()
    det = (analysis.sigma68 * analysis.sigma75) ** 2 * (1 - analysis.rho ** 2)
    return -0.5 * (mahalanobis2(analysis, prediction)
                   + math.log(det) + 2 * math.log(2 * math.pi))


def sample_chi2(analyses, age_years):
    """Joint chi-square of a sample at one conventional concordia age."""
    analyses = _validate_sample(analyses)
    prediction = conventional(age_years)
    return sum(mahalanobis2(a, prediction) for a in analyses)


def sample_log_likelihood(analyses, age_years):
    """Joint predictive log-likelihood of a sample at one age."""
    analyses = _validate_sample(analyses)
    prediction = conventional(age_years)
    return sum(log_likelihood(a, prediction) for a in analyses)


def parameter_count(n_analyses):
    """The conventional comparator fits exactly one parameter: the age."""
    if n_analyses < 1:
        raise ValueError('empty sample')
    return 1


def fit_concordia_age(analyses, *, max_age_years=4.6e9):
    """Fit the conventional concordia age of a sample by minimizing the
    joint correlated-residual chi-square over the sample's analyses.

    Deterministic: a fixed coarse scan brackets the minimum, then a
    golden-section search refines it (same strategy class as the
    existing single-observation pilot, independently implemented).
    """
    analyses = _validate_sample(analyses)
    if not math.isfinite(max_age_years) or max_age_years <= 0:
        raise ValueError('invalid model bounds')

    def score(t):
        return sample_chi2(analyses, t)

    n = 256
    step = max_age_years / n
    j = min(range(n + 1), key=lambda i: score(i * step))
    a, b = max(0.0, (j - 1) * step), min(max_age_years, (j + 1) * step)
    phi = (math.sqrt(5) - 1) / 2
    c, d = b - phi * (b - a), a + phi * (b - a)
    for _ in range(100):
        if score(c) < score(d):
            b, d = d, c
            c = b - phi * (b - a)
        else:
            a, c = c, d
            d = a + phi * (b - a)
    t = (a + b) / 2
    k = parameter_count(len(analyses))
    return {
        'age_years': t,
        'chi2': score(t),
        'log_likelihood': sample_log_likelihood(analyses, t),
        'n_analyses': len(analyses),
        'parameter_count': k,
        'degrees_of_freedom': 2 * len(analyses) - k,
        'per_analysis_chi2': [mahalanobis2(x, conventional(t)) for x in analyses],
    }
