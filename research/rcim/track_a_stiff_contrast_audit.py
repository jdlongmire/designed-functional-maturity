"""Diagnostic sweep for stiff Bateman solver against analytic two-stage solution.

Extreme cases are measured and reported, not silently certified.
A failed extreme case does not make this diagnostic a passing validation.
"""
from math import isclose
from track_a_bateman_network import Nuclide
from track_a_stiff_bateman import propagate
from track_a_bateman_analytic_validation import analytic

CASES = (
    ("ordinary", 10.0, 2.0, 25.0),
    ("contrast_1e7", 1e4, 1e-3, 1e5),
    ("contrast_1e10", 1e6, 1e-4, 1e7),
    ("contrast_1e15", 1e9, 1e-6, 1e10),
)

def check(label, ha, hb, duration):
    nodes = {"A": Nuclide("A", ha, (("B", 1.0, 2.0),)),
             "B": Nuclide("B", hb, (("C", 1.0, 3.0),)),
             "C": Nuclide("C", None, ())}
    expected = analytic(1.0, 0.0, ha, hb, duration)
    expected_heat = 2*(1-expected["A"]) + 3*(1-expected["A"]-expected["B"])
    try:
        actual = propagate(nodes, {"A":1.0,"B":0.0,"C":0.0}, duration)
        errors = [abs(actual["populations"][n] - expected[n]) for n in expected]
        errors.append(abs(actual["deposited_heat_j"] - expected_heat))
        return {"case":label, "passed":max(errors)<1e-7, "max_abs_error":max(errors)}
    except (ArithmeticError, ValueError, OverflowError) as error:
        return {"case":label, "passed":False, "error":str(error)}

def main():
    results = [check(*case) for case in CASES]
    for r in results:
        print(r)
    assert results[0]["passed"], "Ordinary analytical baseline failed"
    assert results[1]["passed"], "Validated 1e7 contrast baseline failed"
    # The 1e10 and 1e15 cases remain diagnostic until they pass in CI
    # on a pinned, reproducible environment. Their status is printed.

if __name__=="__main__":
    main()
