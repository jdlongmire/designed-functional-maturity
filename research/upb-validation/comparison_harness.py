"""Side-by-side comparison harness over synthetic cases (no real data).

Runs the independent conventional comparator (concordia_comparator.py)
and the shared-parameter RCI fitter (rci_fitter.py) over the SAME
synthetic samples and reports the raw statistics the gate names
(EMPIRICAL_GATE_v0.2 item 7; protocol "Predictive outputs and metrics"):
joint log-likelihood, chi-square, parameter count, degrees of freedom.

The protocol states that a material improvement margin is to be
predefined only after a pilot on non-test data and then locked. No such
margin exists in the current documents, so this harness reports raw
statistics only and encodes NO comparison verdict of any kind.

All cases are synthetic, generated from known ground truth with a
seeded generator. This module never reads the evidence cohorts.
"""
import math
import random
from upb_baseline import conventional, initialized
from upb_covariance import RatioObservation
from concordia_comparator import ConcordiaAnalysis, fit_concordia_age
import rci_fitter


def _correlated_errors(rng, sigma68, sigma75, rho):
    """One correlated Gaussian error draw (Box-Muller via Random.gauss)."""
    z1 = rng.gauss(0.0, 1.0)
    z2 = rng.gauss(0.0, 1.0)
    e68 = sigma68 * z1
    e75 = sigma75 * (rho * z1 + math.sqrt(1 - rho * rho) * z2)
    return e68, e75


def synthetic_sample(age_years, n, *, rel_sigma=0.01, rho=0.5, seed=1234,
                     initial68=0.0, initial75=0.0):
    """A synthetic sample of n analyses from known ground truth.

    Truth is the initialized curve at (age_years, initial68, initial75);
    with zero initials this is the conventional concordia curve.
    Uncertainties are rel_sigma of the true ratios (with a floor, as in
    the existing covariance tests). Errors are correlated with the
    stated rho, which is also the published rho carried by each record:
    nothing is hidden from either fitter.
    """
    if n < 1:
        raise ValueError('empty sample')
    rng = random.Random(seed)
    r68_true, r75_true = initialized(age_years, initial68, initial75)
    s68 = max(r68_true * rel_sigma, 1e-9)
    s75 = max(r75_true * rel_sigma, 1e-9)
    out = []
    for _ in range(n):
        e68, e75 = _correlated_errors(rng, s68, s75, rho)
        out.append(RatioObservation(
            max(r68_true + e68, 0.0), max(r75_true + e75, 0.0),
            s68, s75, rho))
    return out


def synthetic_discordant_sample(age_years, loss_fractions, *,
                                rel_sigma=0.005, rho=0.5, seed=99):
    """Synthetic recent-Pb-loss discordia: each analysis sits on the
    chord from the concordia point at age_years toward the origin, at
    its stated loss fraction. No single-age closed-system model fits
    such a sample well; both fitters should report large chi-square.
    """
    if not loss_fractions:
        raise ValueError('empty sample')
    rng = random.Random(seed)
    r68_true, r75_true = conventional(age_years)
    s68 = max(r68_true * rel_sigma, 1e-9)
    s75 = max(r75_true * rel_sigma, 1e-9)
    out = []
    for f in loss_fractions:
        if not 0.0 <= f < 1.0:
            raise ValueError('loss fraction out of range')
        e68, e75 = _correlated_errors(rng, s68, s75, rho)
        out.append(RatioObservation(
            max((1 - f) * r68_true + e68, 0.0),
            max((1 - f) * r75_true + e75, 0.0),
            s68, s75, rho))
    return out


def _to_comparator(observations):
    return [ConcordiaAnalysis(o.r68, o.r75, o.sigma68, o.sigma75, o.rho)
            for o in observations]


def run_comparison(name, observations):
    """Run both implementations over one synthetic sample.

    Returns raw statistics only: no verdict, no margin, no winner.
    """
    observations = list(observations)
    conventional_fit = fit_concordia_age(_to_comparator(observations))
    rci_fit = rci_fitter.fit_unit(observations)
    return {
        'case': name,
        'n_analyses': len(observations),
        'conventional': {
            'age_years': conventional_fit['age_years'],
            'chi2': conventional_fit['chi2'],
            'log_likelihood': conventional_fit['log_likelihood'],
            'parameter_count': conventional_fit['parameter_count'],
            'degrees_of_freedom': conventional_fit['degrees_of_freedom'],
        },
        'rci': {
            'age_years': rci_fit['age_years'],
            'initial68': rci_fit['initial68'],
            'initial75': rci_fit['initial75'],
            'chi2': rci_fit['chi2'],
            'log_likelihood': rci_fit['log_likelihood'],
            'parameter_count': rci_fit['parameter_count'],
            'degrees_of_freedom': rci_fit['degrees_of_freedom'],
            'identifiability': rci_fit['identifiability'],
        },
    }


def standard_cases():
    """The fixed synthetic case set used by the demo and the tests."""
    return [
        ('concordant_100Ma', synthetic_sample(100e6, 8, seed=11)),
        ('concordant_1000Ma', synthetic_sample(1000e6, 8, seed=12)),
        ('concordant_2500Ma', synthetic_sample(2500e6, 8, seed=13)),
        ('initialized_800Ma', synthetic_sample(
            800e6, 8, seed=14, initial68=0.03, initial75=0.07)),
        ('discordant_1500Ma', synthetic_discordant_sample(
            1500e6, [0.0, 0.1, 0.25, 0.4, 0.55, 0.7])),
    ]


def main():
    for name, observations in standard_cases():
        report = run_comparison(name, observations)
        c, r = report['conventional'], report['rci']
        print(f"{name}: n={report['n_analyses']}")
        print(f"  conventional: age={c['age_years']/1e6:.3f} Ma "
              f"chi2={c['chi2']:.3f} loglik={c['log_likelihood']:.3f} "
              f"k={c['parameter_count']} dof={c['degrees_of_freedom']}")
        print(f"  rci:          age={r['age_years']/1e6:.3f} Ma "
              f"a68={r['initial68']:.4f} a75={r['initial75']:.4f} "
              f"chi2={r['chi2']:.3f} loglik={r['log_likelihood']:.3f} "
              f"k={r['parameter_count']} dof={r['degrees_of_freedom']}")
    print('Raw statistics only: no comparison margin is defined in the '
          'current gate or protocol, so no verdict is computed.')


if __name__ == '__main__':
    main()
