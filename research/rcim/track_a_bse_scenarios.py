"""Reproduce published BSE heat scenario estimates with elemental coefficients.

Inputs from Ludhova, Neutrino 2024 slide 11, BSE U/Th/K masses.
Coefficients from Smye & Kelemen (2025) as in track_a_elemental_power.py.
BSE includes crust + mantle: NEVER add crust heat again.
"""
from track_a_elemental_power import present_elemental_power_w
from math import sqrt

# masses in 10^16 kg U/Th, 10^19 kg K; quoted one-sigma-like
# source uncertainties as presented, not independently verified statistical errors.
BSE = {
    "cosmochemical": {"U": (5, 1, 1e16), "Th": (17, 2, 1e16),
                       "K": (59, 12, 1e19), "published_tw": 11.3},
    "geochemical": {"U": (8, 2, 1e16), "Th": (32, 5, 1e16),
                     "K": (113, 24, 1e19), "published_tw": 20.2},
    "geodynamical": {"U": (14, 2, 1e16), "Th": (57, 6, 1e16),
                      "K": (142, 14, 1e19), "published_tw": 33.5},
    "fully_radiogenic": {"U": (20, 1, 1e16), "Th": (77, 3, 1e16),
                          "K": (224, 10, 1e19), "published_tw": 47.0},
}
COEFFICIENT_W_PER_KG = {"U": 98.29e-6, "Th": 26.18e-6, "K": 0.00339e-6}

def calculate(entry):
    masses = {k: entry[k][0] * entry[k][2] for k in COEFFICIENT_W_PER_KG}
    power_tw = present_elemental_power_w(masses) / 1e12
    # Conditional independent-error propagation only; real source covariance unknown.
    conditional_sigma_tw = sqrt(sum(
        (entry[k][1] * entry[k][2] * COEFFICIENT_W_PER_KG[k])**2
        for k in COEFFICIENT_W_PER_KG)) / 1e12
    return power_tw, conditional_sigma_tw

def self_test():
    for name, entry in BSE.items():
        power, sigma = calculate(entry)
        assert power > 0 and sigma >= 0
        # Reproduces literature scenario to rounding/coefficient differences.
        assert abs(power - entry["published_tw"]) < 2, (name, power)
    assert len(BSE) == 4

if __name__ == "__main__":
    self_test()
    print("Published BSE scenario arithmetic checks passed")
    print("Model / recomputed TW / conditional uncorrelated sigma TW / published TW")
    for name, entry in BSE.items():
        p, s = calculate(entry)
        print(f"{name}: {p:.2f} / {s:.2f} / {entry['published_tw']:.1f}")
    print("No model-selection or DFM chronology inference follows from this match.")
