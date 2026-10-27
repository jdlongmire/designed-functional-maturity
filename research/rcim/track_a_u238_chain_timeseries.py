"""Time-series diagnostics for reduced U-238 intermediate-chain model.

Not a complete physical U-238 decay chain or heat calculation.
"""
from math import isclose
from track_a_u238_chain_sensitivity import (
    LAM, NAMES, initial_populations, evolve, activity_ratios
)

def custom_initial(activity_ratios_to_parent):
    """Set arbitrary nonnegative initial activities relative to U-238 activity."""
    if set(activity_ratios_to_parent) != set(NAMES[1:]):
        raise ValueError("Supply U234, Th230, Ra226 activity ratios")
    if any(v < 0 for v in activity_ratios_to_parent.values()):
        raise ValueError("Negative activity ratio")
    return [1.0] + [activity_ratios_to_parent[name] * LAM[0] / LAM[i]
                    for i, name in enumerate(NAMES[1:], start=1)]

def diagnostics(mode, years=(0, 100, 1000, 6000), custom=None):
    if mode == "custom":
        if custom is None:
            raise ValueError("Custom mode needs activity ratios")
        initial = custom_initial(custom)
    else:
        initial = initial_populations(mode)
    return [{"years": t, "activity_ratios": activity_ratios(evolve(initial, t))}
            for t in years]

def self_test():
    depleted = diagnostics("depleted")
    eq = diagnostics("secular_equilibrium")
    assert all(isclose(v, 0, abs_tol=1e-15)
               for k,v in depleted[0]["activity_ratios"].items() if k != "U238")
    assert all(isclose(v, 1, rel_tol=1e-12)
               for v in eq[0]["activity_ratios"].values())
    assert all(0 <= row["activity_ratios"]["Ra226"] < 1 for row in depleted)
    custom = diagnostics("custom", custom={"U234": 0.5, "Th230": 0.5, "Ra226": 0.5})
    assert isclose(custom[0]["activity_ratios"]["Ra226"], .5)
    for bad in ({"U234": -.1, "Th230": 1, "Ra226": 1},
                {"U234": 1, "Th230": 1}):
        try:
            custom_initial(bad)
            raise AssertionError("Invalid custom ratios accepted")
        except ValueError:
            pass

if __name__ == "__main__":
    self_test()
    print("Reduced U-238 activity ratios to surviving parent activity")
    for mode in ("depleted", "secular_equilibrium"):
        print(mode)
        for row in diagnostics(mode):
            print(row["years"], *(f"{n}={row['activity_ratios'][n]:.7g}" for n in NAMES))
    print("Custom boundary ratios supported; none are empirically calibrated.")
