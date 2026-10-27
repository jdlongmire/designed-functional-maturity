"""Published internally paired BSE / continental crust elemental mass balance.

Lyubetskaya & Korenaga (2007), JGR, Table 2:
https://doi.org/10.1029/2005JB004224
All masses converted from grams to kg. 'Residual' includes mantle and any
silicate reservoirs not separately accounted for, including oceanic crust.
Uncertainties are reported marginal ranges, NOT independent Gaussian errors.
"""
from math import isclose
from track_a_elemental_power import present_elemental_power_w

# kg of element, central and stated +/- uncertainty; same Table 2 source.
MODELS = {
    "mc_donough_sun_1995_bse": {
        "U": (8.2e16, 1.7e16), "Th": (3.23e17, 4.8e16),
        "K": (9.8e20, 1.9e20)},
    "lyubetskaya_korenaga_2007_bse": {
        "U": (7.0e16, 1.2e16), "Th": (2.54e17, 4.3e16),
        "K": (7.7e20, 1.6e20)},
}
CONTINENTAL_CRUST = {
    "U": (3.1e16, .9e16), "Th": (1.32e17, .40e17),
    "K": (3.5e20, 1.1e20),
}
ELEMENTS = ("U", "Th", "K")

def split(model_name):
    if model_name not in MODELS:
        raise ValueError("Unknown model")
    bse = MODELS[model_name]
    central_bse = {e: bse[e][0] for e in ELEMENTS}
    crust = {e: CONTINENTAL_CRUST[e][0] for e in ELEMENTS}
    residual = {e: central_bse[e] - crust[e] for e in ELEMENTS}
    if any(v < 0 for v in residual.values()):
        raise ValueError("Negative central residual")
    # Conservative interval arithmetic, ignoring correlation. These are
    # mathematical envelopes, NOT statistical confidence intervals.
    envelopes = {}
    for e in ELEMENTS:
        b, db = bse[e]
        c, dc = CONTINENTAL_CRUST[e]
        envelopes[e] = (b - db - (c + dc), b + db - (c - dc))
    def tw(masses):
        return present_elemental_power_w(masses) / 1e12
    result = {
        "bse_tw": tw(central_bse), "continental_crust_tw": tw(crust),
        "residual_tw": tw(residual),
        "crust_fractions": {e: crust[e] / central_bse[e] for e in ELEMENTS},
        "residual_masses_kg": residual,
        "residual_element_interval_kg": envelopes,
        "residual_power_envelope_tw": (
            tw({e: max(0, envelopes[e][0]) for e in ELEMENTS}),
            tw({e: envelopes[e][1] for e in ELEMENTS})),
    }
    assert isclose(result["bse_tw"], result["continental_crust_tw"] + result["residual_tw"], rel_tol=1e-12)
    return result

def self_test():
    for name in MODELS:
        r = split(name)
        assert all(0 < f < 1 for f in r["crust_fractions"].values())
        assert r["residual_power_envelope_tw"][0] <= r["residual_tw"] <= r["residual_power_envelope_tw"][1]
    assert split("mc_donough_sun_1995_bse")["bse_tw"] > split("lyubetskaya_korenaga_2007_bse")["bse_tw"]

if __name__ == "__main__":
    self_test()
    print("Published BSE minus continental crust mass balance")
    for name in MODELS:
        r = split(name)
        print(name, "BSE", round(r["bse_tw"], 3),
              "continental crust", round(r["continental_crust_tw"], 3),
              "residual", round(r["residual_tw"], 3),
              "envelope", tuple(round(x, 3) for x in r["residual_power_envelope_tw"]),
              "TW")
    print("Envelope is not a confidence interval; residual is not mantle-only.")
