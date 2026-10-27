"""Track A crust/mantle radiogenic source inventory with bounded scenarios.

Inputs are explicitly illustrative unless sourced and audited separately.
No claim of empirical Earth calibration. Standard library only.
Run: python research/rcim/track_a_reservoir_inventory.py
"""
from dataclasses import dataclass
from math import isclose
from track_a_global_heat import combined_budget

@dataclass(frozen=True)
class Reservoir:
    name: str
    mass_kg: float
    u_ppb: float
    th_ppb: float
    k_ppm: float

# Approximate natural fractions; verify against evaluated isotope abundance data
U238_FRACTION = 0.992745
U235_FRACTION = 0.007200
K40_FRACTION = 0.000117

def initial_parent_masses(reservoir, elapsed_y):
    """Concentrations refer to present-day elemental abundance, not initial.
    Back-propagate ordinary decay to boundary; isotope fractions approximated
    by present-day atom fractions, with molar-mass differences neglected."""
    from math import exp, log
    from track_a_global_heat import ISOTOPES
    if min(reservoir.mass_kg, reservoir.u_ppb, reservoir.th_ppb, reservoir.k_ppm, elapsed_y) < 0:
        raise ValueError("Negative reservoir input")
    u = reservoir.mass_kg * reservoir.u_ppb * 1e-9
    th = reservoir.mass_kg * reservoir.th_ppb * 1e-9
    k = reservoir.mass_kg * reservoir.k_ppm * 1e-6
    present = {"U238": u * U238_FRACTION, "U235": u * U235_FRACTION,
               "Th232": th, "K40": k * K40_FRACTION}
    return {key: mass * exp(log(2) * elapsed_y / ISOTOPES[key]["half_y"])
            for key, mass in present.items()}

def inventory(reservoirs, elapsed_y):
    parts = {}
    for r in reservoirs:
        if r.name in parts:
            raise ValueError("Duplicate reservoir")
        parts[r.name] = combined_budget(initial_parent_masses(r, elapsed_y), elapsed_y)
    return {"reservoirs": parts,
            "radiogenic_power_tw": sum(v["power_w"] for v in parts.values()) / 1e12,
            "post_boundary_heat_j": sum(v["post_boundary_heat_j"] for v in parts.values())}

def bounds(scenarios, elapsed_y):
    if not scenarios:
        raise ValueError("Empty scenarios")
    values = {name: inventory(reservoirs, elapsed_y)["radiogenic_power_tw"]
              for name, reservoirs in scenarios.items()}
    return {"scenario_tw": values, "min_tw": min(values.values()),
            "max_tw": max(values.values())}

def self_test():
    r = Reservoir("test", 1e20, 20, 80, 100)
    x = inventory([r], 6000)
    assert x["radiogenic_power_tw"] > 0
    assert x["post_boundary_heat_j"] > 0
    assert isclose(inventory([r], 0)["post_boundary_heat_j"], 0)
    assert isclose(inventory([r, Reservoir("empty", 0, 0, 0, 0)], 6000)["radiogenic_power_tw"],
                   x["radiogenic_power_tw"])
    try:
        inventory([r, r], 6000)
        raise AssertionError("Duplicate reservoir accepted")
    except ValueError:
        pass

if __name__ == "__main__":
    self_test()
    print("Reservoir accounting self-tests passed")
    print("No Earth-specific estimate printed: empirical reservoir inputs not calibrated.")
