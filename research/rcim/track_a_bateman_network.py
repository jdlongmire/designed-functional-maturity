"""Conservation-checked Bateman network engine for branch-resolved decay chains.

This is a generic solver. It does NOT contain an evaluated U/Th nuclear-data
table and does NOT assert physically calibrated heat. Energy per transformation
must be supplied explicitly in joules, net of neutrino losses.
"""
from dataclasses import dataclass
from math import log, isclose

@dataclass(frozen=True)
class Nuclide:
    name: str
    half_life_y: float | None
    branches: tuple  # (daughter name, probability, deposited joules)

def validate(nodes):
    if not nodes:
        raise ValueError("Empty network")
    names = set(nodes)
    for name, node in nodes.items():
        if name != node.name:
            raise ValueError("Mismatched nuclide name")
        if node.half_life_y is None:
            if node.branches:
                raise ValueError("Stable node cannot decay")
            continue
        if node.half_life_y <= 0 or not node.branches:
            raise ValueError("Invalid unstable nuclide")
        if not isclose(sum(b for _, b, _ in node.branches), 1, abs_tol=1e-12):
            raise ValueError("Branches must sum to unity")
        for daughter, probability, heat_j in node.branches:
            if daughter not in names or not (0 <= probability <= 1) or heat_j < 0:
                raise ValueError("Invalid branch")

def derivative(nodes, populations):
    dn = {n: 0.0 for n in nodes}
    heat_rate_j_per_y = 0.0
    for name, node in nodes.items():
        if node.half_life_y is None:
            continue
        activity_y = populations[name] * log(2) / node.half_life_y
        dn[name] -= activity_y
        for daughter, probability, heat_j in node.branches:
            dn[daughter] += activity_y * probability
            heat_rate_j_per_y += activity_y * probability * heat_j
    return dn, heat_rate_j_per_y

def evolve(nodes, initial, duration_y, step_y):
    validate(nodes)
    if set(initial) != set(nodes) or any(x < 0 for x in initial.values()):
        raise ValueError("Supply nonnegative populations for all nodes")
    if duration_y < 0 or step_y <= 0:
        raise ValueError("Invalid time")
    n = dict(initial)
    heat_j = 0.0
    t = 0.0
    # RK4 integrates populations and cumulative energy together.
    while t < duration_y:
        h = min(step_y, duration_y - t)
        k1, q1 = derivative(nodes, n)
        k2, q2 = derivative(nodes, {k: n[k] + h*k1[k]/2 for k in n})
        k3, q3 = derivative(nodes, {k: n[k] + h*k2[k]/2 for k in n})
        k4, q4 = derivative(nodes, {k: n[k] + h*k3[k] for k in n})
        n = {k: n[k] + h*(k1[k]+2*k2[k]+2*k3[k]+k4[k])/6 for k in n}
        heat_j += h*(q1+2*q2+2*q3+q4)/6
        if min(n.values()) < -1e-10:
            raise ArithmeticError("Negative population: decrease integration step")
        n = {k: max(0.0, v) for k, v in n.items()}
        t += h
    initial_total = sum(initial.values())
    if not isclose(sum(n.values()), initial_total, rel_tol=1e-9, abs_tol=1e-12):
        raise ArithmeticError("Atom conservation failure")
    return {"populations": n, "deposited_heat_j": heat_j,
            "heat_rate_j_per_y": derivative(nodes, n)[1]}

def self_test():
    # Artificial branched network: NOT physical isotope data.
    nodes = {"A": Nuclide("A", 10, (("B", .7, 2), ("C", .3, 3))),
             "B": Nuclide("B", 5, (("C", 1.0, 4),)),
             "C": Nuclide("C", None, ())}
    x = evolve(nodes, {"A": 1, "B": 0, "C": 0}, 250, .01)
    assert isclose(sum(x["populations"].values()), 1, abs_tol=1e-10)
    assert isclose(x["populations"]["C"], 1, abs_tol=1e-7)
    assert isclose(x["deposited_heat_j"], 5.1, abs_tol=1e-6)  # .7*(2+4)+.3*3 = 5.1
    z = evolve(nodes, {"A": 1, "B": 0, "C": 0}, 0, 1)
    assert z["deposited_heat_j"] == 0
    try:
        validate({"A": Nuclide("A", 1, (("A", .8, 1),))})
        raise AssertionError("Invalid branching accepted")
    except ValueError:
        pass

if __name__ == "__main__":
    self_test()
    print("Generic branched Bateman network conservation and energy tests passed")
    print("No evaluated isotope network loaded; no Earth heat estimate.")
