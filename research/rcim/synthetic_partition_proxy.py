"""Synthetic partition operator with independently supplied geochemical proxies.

A fixed shared rule maps measurable proxy composition to partition factors.
No isotope observations enter this rule. This is NOT an empirical calibration.
"""
from math import exp, isclose
from synthetic_upb_initialization import observables, fit_shared_parameters

def partition_from_proxy(proxy, *, baseline=1.0, sensitivity=0.4):
    """Dimensionless proxy is declared independently of isotope ratios."""
    if not -1 <= proxy <= 1 or baseline <= 0 or sensitivity < 0:
        raise ValueError("Proxy or fixed rule out of range")
    return baseline*exp(sensitivity*proxy)

def self_test():
    initial=(0.11,0.27)
    proxies=(-0.6,0.2,0.9)
    parents=((1.0,0.2),(1.3,0.3),(0.8,0.15))
    # Freeze this proxy->partition rule before generating any synthetic ratios.
    factors=tuple(partition_from_proxy(p) for p in proxies)
    training=[(p,k,observables(initial,p,k)) for p,k in zip(parents[:2],factors[:2])]
    recovered=fit_shared_parameters(training)
    predicted=observables(recovered,parents[2],partition_from_proxy(proxies[2]))
    actual=observables(initial,parents[2],factors[2])
    assert all(isclose(a,b,rel_tol=1e-8,abs_tol=1e-8) for a,b in zip(predicted,actual))
    # Proxy information breaks the arbitrary ratio/partition rescaling
    # only if baseline and sensitivity are externally fixed.
    assert not isclose(partition_from_proxy(-0.6),partition_from_proxy(0.9))
    print("Synthetic fixed-proxy partition and held-out checks passed")
    print("Rule coefficients are illustrative, not measured geochemical constraints.")
    print("No observed isotope data or empirical PEP established.")

if __name__=="__main__":
    self_test()
