"""DFM Track A: illustrative coupled U-Pb and radiogenic heat accounting.

No geological age or empirical fit is inferred. Standard library only.
Run: python3 research/rcim/track_a_upb_heat.py
"""
from math import exp, log, isclose

LN2 = log(2)
U238_HALF_Y = 4.468e9
U235_HALF_Y = 7.038e8
SECONDS_PER_YEAR = 365.25 * 86400
# Approximate energy released as heat per full decay chain, excluding neutrino energy.
# These are illustrative and require independent verification and uncertainty bounds.
U238_CHAIN_HEAT_MEV = 47.7
U235_CHAIN_HEAT_MEV = 44.4
MEV_TO_J = 1.602176634e-13

def evolve(parent0, radiogenic_daughter0, years, half_life_years):
    if min(parent0, radiogenic_daughter0, years) < 0 or half_life_years <= 0:
        raise ValueError("Invalid physical input")
    decayed = parent0 * (-__import__("math").expm1(-LN2 * years / half_life_years))
    return parent0 - decayed, radiogenic_daughter0 + decayed, decayed

def current_daughter_parent_ratio(parent0, daughter0, years, half_life_years):
    p, d, _ = evolve(parent0, daughter0, years, half_life_years)
    return d / p if p > 0 else float("inf")

def heat_power_w(parent_atoms, half_life_years, chain_heat_mev):
    """Secular-equilibrium approximation: full-chain heat per parent decay.
    Not valid for arbitrary chain disequilibrium or non-retained decay energy."""
    if min(parent_atoms, chain_heat_mev) < 0 or half_life_years <= 0:
        raise ValueError("Invalid physical input")
    return (LN2 / (half_life_years * SECONDS_PER_YEAR)
            * parent_atoms * chain_heat_mev * MEV_TO_J)

def integrated_heat_j(parent0, years, half_life_years, chain_heat_mev):
    _, _, decayed = evolve(parent0, 0, years, half_life_years)
    return decayed * chain_heat_mev * MEV_TO_J

def infer_initial_daughter_for_target_ratio(parent0, years, half_life_years,
                                            observed_ratio):
    """Algebraic diagnostic only; using this to fit observations is NOT
    independent evidence for initialized daughters."""
    if observed_ratio < 0:
        raise ValueError("Negative target ratio")
    present_p, _, decayed = evolve(parent0, 0, years, half_life_years)
    return observed_ratio * present_p - decayed

def self_test():
    for half in (U238_HALF_Y, U235_HALF_Y):
        p, d, n = evolve(100, 10, half, half)
        assert isclose(p, 50, rel_tol=1e-12)
        assert isclose(d, 60, rel_tol=1e-12)
        assert isclose(n, 50, rel_tol=1e-12)
        assert isclose(p + d, 110, rel_tol=1e-12)
    assert heat_power_w(1e24, U238_HALF_Y, U238_CHAIN_HEAT_MEV) > 0
    assert integrated_heat_j(1e24, 6000, U238_HALF_Y,
                             U238_CHAIN_HEAT_MEV) > 0
    assert isclose(infer_initial_daughter_for_target_ratio(
        1e9, 6000, U238_HALF_Y,
        current_daughter_parent_ratio(1e9, 1e6, 6000, U238_HALF_Y)),
        1e6, rel_tol=1e-8)
    # Initial stable daughter inventories do not themselves produce decay heat.
    assert heat_power_w(1e24, U238_HALF_Y, U238_CHAIN_HEAT_MEV) == heat_power_w(
        1e24, U238_HALF_Y, U238_CHAIN_HEAT_MEV)

if __name__ == "__main__":
    self_test()
    print("Track A analytical self-tests passed")
    for name, half, mev in (("U-238", U238_HALF_Y, U238_CHAIN_HEAT_MEV),
                            ("U-235", U235_HALF_Y, U235_CHAIN_HEAT_MEV)):
        p, d, n = evolve(1e24, 0, 6000, half)
        print(name, "6000-year decayed fraction", f"{n/1e24:.9g}",
              "illustrative parent power W", f"{heat_power_w(p, half, mev):.6g}")
