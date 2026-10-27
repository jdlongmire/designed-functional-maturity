"""Constrained synthetic U-Pb initialization and identifiability benchmark.

Synthetic only: two parent nuclides and stable daughters, no evaluated full
decay chains, heat calculation, measured isotope data, or empirical parity.
"""
from math import exp, log, isclose

HALF_LIVES_Y = (4.468e9, 7.038e8)  # illustrative reference values
DURATION_Y = 6000.0

def forward(shared_daughters, parent_pair, partition, duration_y=DURATION_Y):
    """Shared reservoir daughter/parent ratios; mineral partition scales both
    initial daughter inventories identically, never independently per isotope."""
    if len(shared_daughters)!=2 or len(parent_pair)!=2:
        raise ValueError("Two parent and daughter species required")
    if min(*shared_daughters,*parent_pair,partition,duration_y)<0:
        raise ValueError("Negative input")
    result=[]
    for ratio, parent, half_life in zip(shared_daughters,parent_pair,HALF_LIVES_Y):
        surviving=parent*exp(-log(2)*duration_y/half_life)
        daughter=partition*ratio*parent+(parent-surviving)
        result.append((surviving,daughter))
        assert isclose(surviving+daughter, parent*(1+partition*ratio),
                       rel_tol=1e-12,abs_tol=1e-12)
    return tuple(result)

def observables(shared_daughters, parent_pair, partition, duration_y=DURATION_Y):
    return tuple(d/p for p,d in forward(shared_daughters,parent_pair,partition,duration_y))

def fit_shared_parameters(training):
    """Two common daughter ratios estimated from two or more known mineral
    partition coefficients; reject a rank-deficient dataset."""
    if len(training)<2:
        raise ValueError("Need at least two training specimens")
    estimates=[[],[]]
    for parent_pair,partition,observed in training:
        if partition<=0 or min(parent_pair)<=0:
            raise ValueError("Positive parent populations and partition required")
        for i,half in enumerate(HALF_LIVES_Y):
            growth=exp(log(2)*DURATION_Y/half)-1
            estimates[i].append((observed[i]-growth)*exp(-log(2)*DURATION_Y/half)/partition)
    return tuple(sum(vals)/len(vals) for vals in estimates)

def self_test():
    truth=(0.11,0.27)
    parents=((1.0,0.2),(1.3,0.3),(0.8,0.15))
    partitions=(0.8,1.2,1.6)
    data=[(p,k,observables(truth,p,k)) for p,k in zip(parents,partitions)]
    recovered=fit_shared_parameters(data[:2])
    # Fit uses known synthetic 6000-y duration and fixed partition coefficients;
    # this is an inverse-consistency check, NOT independent age-free derivation.
    for actual,expected in zip(recovered,truth):
        assert isclose(actual,expected,rel_tol=1e-8,abs_tol=1e-8)
    held_out=observables(recovered,parents[2],partitions[2])
    for actual,expected in zip(held_out,data[2][2]):
        assert isclose(actual,expected,rel_tol=1e-8,abs_tol=1e-8)
    # Identifiability counterexample: unknown partition and initial ratio
    # enter only as a product; scaling one and inversely scaling the other
    # leaves all observed ratios unchanged.
    for scale in (0.5,2.0,10.0):
        assert all(isclose(a,b,rel_tol=1e-12) for a,b in zip(
            observables(truth,parents[0],partitions[0]),
            observables(tuple(x*scale for x in truth),parents[0],partitions[0]/scale)))
    print("Synthetic U-Pb constrained-generator checks passed")
    print("Identifiability caveat: daughter ratio and partition require independent constraints.")
    print("No observed data, evaluated full-chain energy, or empirical PEP established.")

if __name__=="__main__":
    self_test()
