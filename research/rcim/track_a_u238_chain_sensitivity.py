"""Track A U-238 slow-chain population sensitivity, NOT a complete heat model.

Reduced chain: U-238 -> U-234 -> Th-230 -> Ra-226 -> sink.
Fast intermediates are collapsed. The sink does not represent a complete
Pb-206 chain and this module does NOT assign complete-chain heat yields.
All populations are atoms normalized to one initial U-238 atom.
"""
from math import exp, log, isclose

HALF_Y = (4.468e9, 245500.0, 75380.0, 1600.0)
LAM = tuple(log(2.0) / h for h in HALF_Y)
NAMES = ("U238", "U234", "Th230", "Ra226")

def initial_populations(mode):
    if mode == "depleted":
        return [1.0, 0.0, 0.0, 0.0]
    if mode == "secular_equilibrium":
        return [1.0] + [LAM[0] / LAM[i] for i in range(1, 4)]
    raise ValueError("Choose depleted or secular_equilibrium")

def derivative(n):
    return [-LAM[0] * n[0]] + [
        LAM[i-1] * n[i-1] - LAM[i] * n[i] for i in range(1, 4)]

def evolve(initial, years=6000.0, step_y=1.0):
    if len(initial) != 4 or any(x < 0 for x in initial):
        raise ValueError("Nonnegative four-isotope populations required")
    if years < 0 or step_y <= 0 or step_y > 50:
        raise ValueError("Invalid duration or step")
    n = list(initial)
    t = 0.0
    while t < years:
        h = min(step_y, years-t)
        k1 = derivative(n)
        k2 = derivative([x + h*y/2 for x,y in zip(n,k1)])
        k3 = derivative([x + h*y/2 for x,y in zip(n,k2)])
        k4 = derivative([x + h*y for x,y in zip(n,k3)])
        n = [x + h*(a+2*b+2*c+d)/6
             for x,a,b,c,d in zip(n,k1,k2,k3,k4)]
        t += h
    return n

def activity_ratios(n):
    parent = LAM[0] * n[0]
    return {NAMES[i]: (LAM[i] * n[i]) / parent for i in range(4)}

def self_test():
    assert evolve(initial_populations("depleted"), 0) == initial_populations("depleted")
    for mode in ("depleted", "secular_equilibrium"):
        n = evolve(initial_populations(mode))
        assert all(x >= 0 for x in n)
        assert isclose(n[0], exp(-LAM[0]*6000), rel_tol=1e-10)
    depleted = activity_ratios(evolve(initial_populations("depleted")))
    equilibrium = activity_ratios(evolve(initial_populations("secular_equilibrium")))
    assert depleted["Ra226"] < equilibrium["Ra226"]
    assert abs(equilibrium["Ra226"] - 1) < 0.001

if __name__ == "__main__":
    self_test()
    for mode in ("depleted", "secular_equilibrium"):
        print(mode, {k: round(v, 8) for k,v in
                     activity_ratios(evolve(initial_populations(mode))).items()})
    print("Reduced-chain activity sensitivity only; no complete-chain heat claims.")
