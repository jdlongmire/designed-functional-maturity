"""Track A radiogenic source budget and minimal thermal-box sensitivity model.

Illustrative assumptions, NOT an empirical Earth fit. Standard library only.
Run: python3 research/rcim/track_a_global_heat.py
"""
from math import exp, expm1, log, isclose

SECONDS_PER_YEAR = 365.25 * 86400
AVOGADRO = 6.02214076e23
MEV_J = 1.602176634e-13
LN2 = log(2)
# Approximate net heat per parent transformation, excluding neutrino losses.
# K-40 includes branching-averaged heat; all values require independent
# source validation before quantitative geological interpretation.
ISOTOPES = {
    "U238": {"half_y": 4.468e9, "heat_mev": 47.7, "molar_g": 238.0508},
    "U235": {"half_y": 7.038e8, "heat_mev": 44.4, "molar_g": 235.0439},
    "Th232": {"half_y": 1.405e10, "heat_mev": 40.4, "molar_g": 232.0381},
    "K40": {"half_y": 1.248e9, "heat_mev": 0.65, "molar_g": 39.9640},
}

def parent_atoms(mass_kg, isotope):
    if mass_kg < 0:
        raise ValueError("Negative isotope mass")
    return mass_kg * 1000 / ISOTOPES[isotope]["molar_g"] * AVOGADRO

def decay_fraction(years, isotope):
    if years < 0:
        raise ValueError("Negative duration")
    return -expm1(-LN2 * years / ISOTOPES[isotope]["half_y"])

def source_budget(mass_kg, isotope, years=0):
    """mass_kg is the INITIAL isotope mass at the boundary, not current mass."""
    p = ISOTOPES[isotope]
    n0 = parent_atoms(mass_kg, isotope)
    lam_s = LN2 / (p["half_y"] * SECONDS_PER_YEAR)
    remaining = n0 * exp(-lam_s * years * SECONDS_PER_YEAR)
    power_w = remaining * lam_s * p["heat_mev"] * MEV_J
    released_j = (n0 - remaining) * p["heat_mev"] * MEV_J
    return {"power_w": power_w, "post_boundary_heat_j": released_j,
            "remaining_parent_atoms": remaining}

def combined_budget(initial_masses_kg, years):
    missing = set(initial_masses_kg) - set(ISOTOPES)
    if missing:
        raise ValueError(f"Unknown isotope keys: {missing}")
    parts = {k: source_budget(m, k, years) for k, m in initial_masses_kg.items()}
    return {"power_w": sum(x["power_w"] for x in parts.values()),
            "post_boundary_heat_j": sum(x["post_boundary_heat_j"] for x in parts.values()),
            "by_isotope": parts}

def thermal_box_step(temperature_k, heat_capacity_j_per_k,
                     source_w, outward_heat_w, duration_years):
    """One-box energy balance, not a spatial conduction/convection solution.
    T1 = T0 + (P_source - P_out)*dt/C. User supplies all thermal parameters."""
    if heat_capacity_j_per_k <= 0 or duration_years < 0 or temperature_k < 0:
        raise ValueError("Invalid thermal-box parameters")
    return temperature_k + (source_w - outward_heat_w) * duration_years * SECONDS_PER_YEAR / heat_capacity_j_per_k

def self_test():
    for key in ISOTOPES:
        assert isclose(decay_fraction(ISOTOPES[key]["half_y"], key), 0.5, rel_tol=1e-12)
        initial = source_budget(1.0, key, 0)
        later = source_budget(1.0, key, 6000)
        assert initial["post_boundary_heat_j"] == 0
        assert later["post_boundary_heat_j"] > 0
        assert later["power_w"] < initial["power_w"]
    assert isclose(thermal_box_step(300, 1e12, 10, 10, 100), 300)
    assert combined_budget({}, 6000)["power_w"] == 0
    try:
        source_budget(-1, "U238")
        raise AssertionError("Negative mass was accepted")
    except ValueError:
        pass

if __name__ == "__main__":
    self_test()
    # Normalized demonstration: 1 kg of each parent isotope, not Earth inventory.
    example = combined_budget({k: 1.0 for k in ISOTOPES}, 6000)
    print("Track A global heat accounting self-tests passed")
    print("Normalized example (1 kg of each isotope; not Earth inventory)")
    for k, value in example["by_isotope"].items():
        print(k, f"power={value['power_w']:.6g} W",
              f"post-boundary heat={value['post_boundary_heat_j']:.6g} J")
    print("total power W", f"{example['power_w']:.6g}")
