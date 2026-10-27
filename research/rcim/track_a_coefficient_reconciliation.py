"""Compare isotope-decay heat power with independent elemental coefficients.

This diagnostic does NOT adjust constants to force agreement.
Uses present-day natural isotope fractions as approximate mass fractions.
"""
from track_a_global_heat import ISOTOPES, AVOGADRO, LN2, SECONDS_PER_YEAR, MEV_J
from track_a_elemental_power import SPECIFIC_MICROWATT_PER_KG_ELEMENT

FRACTIONS = {"U238": .992745, "U235": .007200, "Th232": 1.0, "K40": .000117}

def isotope_elemental_specific_w_per_kg():
    p = {}
    for isotope, fraction in FRACTIONS.items():
        n = 1000 / ISOTOPES[isotope]["molar_g"] * AVOGADRO * fraction
        lam = LN2 / (ISOTOPES[isotope]["half_y"] * SECONDS_PER_YEAR)
        p[isotope] = n * lam * ISOTOPES[isotope]["heat_mev"] * MEV_J
    return {"U": p["U238"] + p["U235"], "Th": p["Th232"], "K": p["K40"]}

def compare():
    isotope = isotope_elemental_specific_w_per_kg()
    return {e: {"decay_w_per_kg": isotope[e],
                "published_w_per_kg": SPECIFIC_MICROWATT_PER_KG_ELEMENT[e] * 1e-6,
                "ratio": isotope[e] / (SPECIFIC_MICROWATT_PER_KG_ELEMENT[e] * 1e-6)}
            for e in ("U", "Th", "K")}

def self_test():
    r = compare()
    assert all(x["ratio"] > 0 for x in r.values())
    # These are intentionally broad plausibility checks, NOT coefficient validation.
    assert all(0.5 < x["ratio"] < 2.0 for x in r.values())

if __name__ == "__main__":
    self_test()
    print("Isotope / elemental coefficient diagnostic")
    for k, v in compare().items():
        print(k, f"decay={v['decay_w_per_kg']:.9g} W/kg",
              f"published={v['published_w_per_kg']:.9g} W/kg",
              f"ratio={v['ratio']:.6f}")
    print("Differences must be investigated, not calibrated away.")
