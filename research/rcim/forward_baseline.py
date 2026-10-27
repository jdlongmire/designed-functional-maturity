"""RCIM analytical baseline. Standard library only. No empirical inference.

Run: python3 research/rcim/forward_baseline.py
All parameter values below are illustrative and must be sourced before publication.
"""
from dataclasses import dataclass
from math import exp, log, isclose

SECONDS_PER_YEAR = 365.25 * 24 * 3600

@dataclass(frozen=True)
class Nuclide:
    name: str
    half_life_years: float

    @property
    def decay_constant(self):
        if self.half_life_years <= 0:
            raise ValueError("Half-life must be positive")
        return log(2) / self.half_life_years

U238 = Nuclide("U-238", 4.468e9)
U235 = Nuclide("U-235", 7.038e8)
K40 = Nuclide("K-40", 1.248e9)
# Approximate K-40 electron-capture / positron branch to Ar-40.
# Source, precision, and uncertainty must be verified before use in inference.
K40_TO_AR40_BRANCH = 0.1072

def closed_system(parent0, daughter0, years, nuclide, daughter_branch=1.0):
    """Return (parent, daughter) after ordinary decay, preserving branch accounting."""
    if min(parent0, daughter0, years) < 0 or not 0 <= daughter_branch <= 1:
        raise ValueError("Nonnegative inventories/time and 0<=branch<=1 required")
    parent = parent0 * exp(-nuclide.decay_constant * years)
    daughter = daughter0 + daughter_branch * (parent0 - parent)
    return parent, daughter

def ratio_at_time(initial_daughter_per_parent, years, nuclide):
    """Closed-system stable-daughter/current-parent ratio, unit branching."""
    if initial_daughter_per_parent < 0 or years < 0:
        raise ValueError("Invalid inputs")
    e = exp(nuclide.decay_constant * years)
    return initial_daughter_per_parent * e + e - 1

def ideal_gas_ar40_pressure_pa(total_pressure_pa=101325.0,
                                ar_mole_fraction=0.00934,
                                ar40_fraction=0.996):
    if total_pressure_pa < 0 or not (0 <= ar_mole_fraction <= 1
                                    and 0 <= ar40_fraction <= 1):
        raise ValueError("Invalid pressure or fractions")
    return total_pressure_pa * ar_mole_fraction * ar40_fraction

def run_tests():
    for nuclide in (U238, U235, K40):
        p, d = closed_system(100.0, 5.0, 0, nuclide)
        assert p == 100.0 and d == 5.0
        p, d = closed_system(100.0, 5.0, nuclide.half_life_years, nuclide)
        assert isclose(p, 50.0, rel_tol=1e-12)
        assert isclose(d, 55.0, rel_tol=1e-12)
    p, d = closed_system(100, 0, K40.half_life_years, K40,
                         K40_TO_AR40_BRANCH)
    assert isclose(d, 50 * K40_TO_AR40_BRANCH, rel_tol=1e-12)
    assert isclose(ratio_at_time(0, 6000, U238),
                   exp(U238.decay_constant * 6000)-1, rel_tol=1e-12)
    assert isclose(ideal_gas_ar40_pressure_pa(), 943.0, rel_tol=0.005)
    try:
        closed_system(-1, 0, 1, U238)
        raise AssertionError("Negative input accepted")
    except ValueError:
        pass

if __name__ == "__main__":
    run_tests()
    print("RCIM baseline self-tests passed")
    print("Illustrative 6000-year U-238 daughter/current-parent increment:",
          f"{ratio_at_time(0, 6000, U238):.9g}")
    print("Illustrative 6000-year U-235 daughter/current-parent increment:",
          f"{ratio_at_time(0, 6000, U235):.9g}")
    print("Illustrative Ar-40 partial pressure (Pa):",
          f"{ideal_gas_ar40_pressure_pa():.3f}")
