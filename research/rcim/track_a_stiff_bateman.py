"""Stiff-safe decay network via augmented matrix exponential (SciPy).

Exact for the specified constant decay generator to floating-point precision.
Heat is integrated as an additional state; inputs are branch-deposited joules.
This is a numerical engine, NOT evaluated U-238 chain data.
"""
from math import log, isclose
import numpy as np
from scipy.linalg import expm
from track_a_bateman_network import Nuclide, validate

SECONDS_PER_YEAR = 365.25 * 86400

def propagate(nodes, initial, duration_y):
    validate(nodes)
    if set(initial) != set(nodes) or any(x < 0 for x in initial.values()):
        raise ValueError("Supply nonnegative populations for every nuclide")
    if duration_y < 0:
        raise ValueError("Negative duration")
    names = list(nodes)
    idx = {name: i for i, name in enumerate(names)}
    count = len(names)
    # The last state is cumulative locally deposited heat in joules.
    generator = np.zeros((count + 1, count + 1), dtype=float)
    for name, node in nodes.items():
        if node.half_life_y is None:
            continue
        j = idx[name]
        rate = log(2) / node.half_life_y
        generator[j, j] -= rate
        for daughter, probability, deposited_j in node.branches:
            generator[idx[daughter], j] += rate * probability
            generator[count, j] += rate * probability * deposited_j
    state0 = np.array([initial[n] for n in names] + [0.0])
    state = expm(generator * duration_y) @ state0
    populations = {name: float(state[idx[name]]) for name in names}
    if min(populations.values()) < -1e-9:
        raise ArithmeticError("Negative populations")
    if not isclose(sum(populations.values()), sum(initial.values()),
                   rel_tol=1e-9, abs_tol=1e-9):
        raise ArithmeticError("Tracked-chain population conservation failure")
    deposited = float(state[count])
    if deposited < -1e-9:
        raise ArithmeticError("Negative deposited heat")
    instantaneous_j_per_y = float(generator[count, :count] @ state[:count])
    return {"populations": populations, "deposited_heat_j": deposited,
            "heat_rate_w": instantaneous_j_per_y / SECONDS_PER_YEAR}

def self_test():
    # Artificial A -> B -> C with 10^7 half-life contrast and known
    # limiting total energy 2 + 3 J per initial A atom.
    nodes = {"A": Nuclide("A", 1e4, (("B", 1., 2.),)),
             "B": Nuclide("B", 1e-3, (("C", 1., 3.),)),
             "C": Nuclide("C", None, ())}
    initial = {"A": 1., "B": 0., "C": 0.}
    at_zero = propagate(nodes, initial, 0.)
    assert at_zero["deposited_heat_j"] == 0.
    result = propagate(nodes, initial, 1e5)
    assert isclose(result["populations"]["A"], 2**-10, rel_tol=1e-7)
    assert isclose(result["deposited_heat_j"], 5*(1-2**-10), rel_tol=1e-7)
    # This fixture does not certify numerical stability at 10^15 contrast.\n    # Compare against analytic two-stage solution on ordinary time scales.
    from track_a_bateman_analytic_validation import analytic
    ordinary = {"A": Nuclide("A", 10., (("B", 1., 2.),)),
                "B": Nuclide("B", 2., (("C", 1., 3.),)),
                "C": Nuclide("C", None, ())}
    r = propagate(ordinary, {"A": 1., "B": .2, "C": 0.}, 25.)
    exact = analytic(1., .2, 10., 2., 25.)
    for name in exact:
        assert isclose(r["populations"][name], exact[name], rel_tol=1e-10, abs_tol=1e-10)
    exact_heat = 2*(1-exact["A"]) + 3*(1.2-exact["A"]-exact["B"])
    assert isclose(r["deposited_heat_j"], exact_heat, rel_tol=1e-10)

if __name__ == "__main__":
    self_test()
    print("Stiff matrix-exponential decay-network tests passed")
    print("No evaluated U-238 nuclear dataset has been loaded.")
