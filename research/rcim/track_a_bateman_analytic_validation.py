"""Analytic Bateman validation of the generic decay-network solver.

Two-stage A -> B -> C, with arbitrary initial A and B. This is a
mathematical verification fixture, not evaluated U-238 nuclear data.
"""
from math import exp, expm1, log, isclose
from track_a_bateman_network import Nuclide, evolve

def analytic(a0, b0, half_a_y, half_b_y, years):
    if min(a0, b0, years) < 0 or min(half_a_y, half_b_y) <= 0:
        raise ValueError("Invalid populations, half-lives, or duration")
    la, lb = log(2)/half_a_y, log(2)/half_b_y
    a = a0 * exp(-la*years)
    if isclose(la, lb, rel_tol=1e-10):
        b = (b0 + a0*la*years)*exp(-la*years)
    else:
        b = b0*exp(-lb*years) + a0*la*exp(-la*years)*(-expm1(-(lb-la)*years))/(lb-la)
    c = a0+b0-a-b
    return {"A": a, "B": b, "C": c}

def check_case(a0, b0, ha, hb, years, step):
    nodes = {"A": Nuclide("A", ha, (("B", 1.0, 2.0),)),
             "B": Nuclide("B", hb, (("C", 1.0, 3.0),)),
             "C": Nuclide("C", None, ())}
    result = evolve(nodes, {"A":a0, "B":b0, "C":0.0}, years, step)
    exact = analytic(a0,b0,ha,hb,years)
    for k in exact:
        assert isclose(result["populations"][k], exact[k], rel_tol=2e-7, abs_tol=1e-10), (k, result, exact)
    # Each A transformation deposits 2 J, each B transformation 3 J.
    exact_heat = 2*(a0-exact["A"]) + 3*(a0+b0-exact["A"]-exact["B"])
    assert isclose(result["deposited_heat_j"], exact_heat, rel_tol=2e-7, abs_tol=1e-10)
    return result

def self_test():
    for a0,b0,ha,hb,years,step in (
        (1.0,0.0,10.0,2.0,25.0,.01),
        (1.0,.2,10.0,2.0,25.0,.01),
        (1.0,.2,10.0,10.0,25.0,.01),
        (1.0,.2,10.0,10.00000000001,25.0,.01),
    ):
        check_case(a0,b0,ha,hb,years,step)
    # Stability boundary: short half-lives cannot use a long RK4 step.
    try:
        check_case(1.0,0.0,10.0,1e-6,1.0,.1)
        raise AssertionError("Expected stiffness-related failure")
    except (ArithmeticError, AssertionError):
        pass

if __name__ == "__main__":
    self_test()
    print("Analytic two-stage populations and integrated heat agree with RK4")
    print("Synthetic fixture only; complete U-238 nuclear data not loaded.")
