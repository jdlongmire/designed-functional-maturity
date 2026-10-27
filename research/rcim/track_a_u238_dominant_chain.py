"""U-238 dominant-path nuclear topology for stiff Bateman solver.

Major-path half-lives are rounded provisional reference values, pending
line-by-line evaluated nuclear-data provenance. Minor branches and Pa-234m isomeric transition are NOT
fully represented. Every branch deposited energy is ZERO BY DESIGN.
This module may calculate populations but MUST NOT be used for heat budgets.
"""
from track_a_bateman_network import Nuclide
from track_a_stiff_bateman import propagate
from math import log, isclose

DAY=1/365.25
HOUR=DAY/24
MINUTE=HOUR/60
SECOND=MINUTE/60

# Name, half-life years, major daughter. Pa234m is the dominant pathway.
CHAIN = [
 ("U238",4.468e9,"Th234"),
 ("Th234",24.1*DAY,"Pa234m"),
 ("Pa234m",1.17*MINUTE,"U234"),
 ("U234",245500.,"Th230"),
 ("Th230",75380.,"Ra226"),
 ("Ra226",1600.,"Rn222"),
 ("Rn222",3.8235*DAY,"Po218"),
 ("Po218",3.10*MINUTE,"Pb214"),
 ("Pb214",26.8*MINUTE,"Bi214"),
 ("Bi214",19.9*MINUTE,"Po214"),
 ("Po214",164.3e-6*SECOND,"Pb210"),
 ("Pb210",22.3,"Bi210"),
 ("Bi210",5.01*DAY,"Po210"),
 ("Po210",138.4*DAY,"Pb206"),
]

def nodes():
    result={n:Nuclide(n,h,((daughter,1.0,0.0),))
            for n,h,daughter in CHAIN}
    result["Pb206"]=Nuclide("Pb206",None,())
    return result

def initial(mode):
    data={name:0.0 for name in nodes()}
    data["U238"]=1.0
    if mode=="depleted":
        return data
    if mode=="equilibrium":
        parent_rate=log(2)/CHAIN[0][1]
        for name,half,_ in CHAIN[1:]:
            data[name]=parent_rate/(log(2)/half)
        return data
    raise ValueError("Unknown initialization")

def self_test():
    model=nodes()
    assert len(model)==15
    for mode in ("depleted","equilibrium"):
        start=initial(mode)
        end=propagate(model,start,6000)
        assert isclose(sum(start.values()),sum(end["populations"].values()),
                       rel_tol=1e-9)
        assert end["deposited_heat_j"]==0.0
        assert isclose(end["populations"]["U238"],2**(-6000/4.468e9),
                       rel_tol=1e-9)
    depleted=propagate(model,initial("depleted"),6000)
    equilibrium=propagate(model,initial("equilibrium"),6000)
    assert depleted["populations"]["Ra226"] < equilibrium["populations"]["Ra226"]

if __name__=="__main__":
    self_test()
    print("U238 dominant-path 15-node population checks passed")
    for mode in ("depleted","equilibrium"):
        n=propagate(nodes(),initial(mode),6000)["populations"]
        parent_activity=log(2)/CHAIN[0][1]*n["U238"]
        print(mode,"Ra226/U238 activity",round((log(2)/1600*n["Ra226"])/parent_activity,8))
    print("Energy intentionally unset; minor branches and isomer details unvalidated.")
