"""Mass-conserving BSE crust/mantle partition; illustrative fractions only.

BSE model totals are imported from track_a_bse_scenarios. Fractions are
explicit user inputs; they are NOT observational estimates.
"""
from math import isclose
from track_a_bse_scenarios import BSE, calculate
from track_a_elemental_power import present_elemental_power_w

ELEMENTS = ("U", "Th", "K")

def partition_bse(scenario, crust_fractions):
    if scenario not in BSE:
        raise ValueError("Unknown BSE scenario")
    if set(crust_fractions) != set(ELEMENTS):
        raise ValueError("Specify crust fraction for U, Th, K")
    if any(not 0 <= crust_fractions[e] <= 1 for e in ELEMENTS):
        raise ValueError("Fractions must be within [0,1]")
    masses = {e: BSE[scenario][e][0] * BSE[scenario][e][2] for e in ELEMENTS}
    crust = {e: masses[e] * crust_fractions[e] for e in ELEMENTS}
    mantle = {e: masses[e] - crust[e] for e in ELEMENTS}
    for e in ELEMENTS:
        assert isclose(crust[e] + mantle[e], masses[e], rel_tol=1e-12)
    crust_w = present_elemental_power_w(crust)
    mantle_w = present_elemental_power_w(mantle)
    total_w = present_elemental_power_w(masses)
    assert isclose(crust_w + mantle_w, total_w, rel_tol=1e-12)
    return {"crust_masses_kg": crust, "mantle_masses_kg": mantle,
            "crust_tw": crust_w / 1e12, "mantle_tw": mantle_w / 1e12,
            "total_tw": total_w / 1e12}

def self_test():
    for scenario in BSE:
        for fractions in ({"U": 0, "Th": 0, "K": 0},
                          {"U": 1, "Th": 1, "K": 1},
                          {"U": .4, "Th": .5, "K": .2}):
            result = partition_bse(scenario, fractions)
            assert isclose(result["total_tw"], calculate(BSE[scenario])[0], rel_tol=1e-12)
            assert isclose(result["crust_tw"] + result["mantle_tw"],
                           result["total_tw"], rel_tol=1e-12)
    for invalid in ({"U": -0.1, "Th": .5, "K": .5},
                    {"U": 1.1, "Th": .5, "K": .5}):
        try:
            partition_bse("geochemical", invalid)
            raise AssertionError("Invalid fraction accepted")
        except ValueError:
            pass

if __name__ == "__main__":
    self_test()
    print("BSE crust/mantle partition conservation checks passed")
    print("No observational crust fraction is assumed.")
