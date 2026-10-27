"""Independent present-day elemental specific-power accounting.

Coefficients from Smye & Kelemen (2025), Nature Geoscience,
https://www.nature.com/articles/s41561-025-01820-2
U 98.29, Th 26.18, K 0.00339 microW/kg ELEMENT (not isotope).
This is an independent unit-consistent cross-check, not a full Earth fit.
"""
from math import isclose

MICROWATT_TO_WATT = 1e-6
SPECIFIC_MICROWATT_PER_KG_ELEMENT = {"U": 98.29, "Th": 26.18, "K": 0.00339}

def present_elemental_power_w(element_masses_kg):
    if set(element_masses_kg) - set(SPECIFIC_MICROWATT_PER_KG_ELEMENT):
        raise ValueError("Unknown element")
    if any(m < 0 for m in element_masses_kg.values()):
        raise ValueError("Negative mass")
    return sum(m * SPECIFIC_MICROWATT_PER_KG_ELEMENT[e] * MICROWATT_TO_WATT
               for e, m in element_masses_kg.items())

def reservoir_elemental_power_tw(mass_kg, u_ppb, th_ppb, k_ppm):
    if min(mass_kg, u_ppb, th_ppb, k_ppm) < 0:
        raise ValueError("Negative input")
    masses = {"U": mass_kg * u_ppb * 1e-9,
              "Th": mass_kg * th_ppb * 1e-9,
              "K": mass_kg * k_ppm * 1e-6}
    return present_elemental_power_w(masses) / 1e12

def self_test():
    assert isclose(present_elemental_power_w({"U": 1}), 98.29e-6)
    assert isclose(present_elemental_power_w({"Th": 1}), 26.18e-6)
    assert isclose(present_elemental_power_w({"K": 1}), 0.00339e-6)
    assert isclose(reservoir_elemental_power_tw(0, 20, 80, 240), 0)
    assert isclose(reservoir_elemental_power_tw(1e20, 20, 80, 240),
                   present_elemental_power_w({"U": 2e12, "Th": 8e12, "K": 2.4e16}) / 1e12)
    try:
        present_elemental_power_w({"K": -1})
        raise AssertionError("Negative mass accepted")
    except ValueError:
        pass

if __name__ == "__main__":
    self_test()
    print("Elemental power unit tests passed; no calibrated Earth inventory asserted")
