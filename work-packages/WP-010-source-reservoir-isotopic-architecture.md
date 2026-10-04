# WP-010: Source-Reservoir Isotopic Architecture and Mass-Balance Model

**Status:** Executed baseline  
**Parent:** DFM Research Programme  
**Depends on:** WP-004, WP-007, WP-008, WP-009

## Purpose

Test whether DFM can obtain nontrivial isotope-system structure from a common initialized source-reservoir architecture before any mineral-level radiometric age fitting.

This WP moves the problem upstream. Instead of assigning mature isotope states to individual zircons or rocks, it asks what follows if the initialized world contains a finite set of chemically and physically constrained reservoirs whose elemental and isotopic inventories must satisfy global mass balance.

## 1. State architecture

Let the initialized radiogenic state be partitioned among reservoirs:

```text
S0_rad = {R_1, R_2, ..., R_n}
```

For isotope or element species `k`:

```text
M_k,total = Sum_r M_k,r
```

where `M_k,total` is the total inventory of species `k`, `M_k,r` is its inventory in reservoir `r`, and the sum runs over all reservoirs `r`.

No reservoir can be assigned an isotope inventory independently of the global inventory.

For a parent-daughter system `p -> d`:

```text
M_p,total = Sum_r M_p,r
M_d,total = Sum_r M_d,r
```

and partition coefficients constrain redistribution into phases and minerals.

## 2. Initialization generator

Define:

```text
S0_rad = G(M_bulk, I_bulk, Phi_thermal, C_chem, C_phase, C_mass, L)
```

where:

- `M_bulk` = bulk elemental inventory;
- `I_bulk` = bulk isotopic inventory;
- `Phi_thermal` = thermal functional requirements;
- `C_chem` = chemical affinity and partition constraints;
- `C_phase` = phase/mineral stability constraints;
- `C_mass` = mass-conservation constraints;
- `L` = ordinary physical/nuclear law.

The generator is valid only if these inputs are independently specified or measured rather than derived from target radiometric ages.

## 3. Reservoir partition

For element `E` distributed between reservoirs `a` and `b`:

```text
K_E^(a/b) = C_E,a / C_E,b
```

For mineral `m` crystallizing from reservoir `r`:

```text
D_E^(m/r) = C_E,m / C_E,r
```

Here `K_E^(a/b)` is the partition coefficient for element `E` between phases `a` and `b`; `C_E,a` and `C_E,b` are the corresponding concentrations. Likewise, `D_E^(m/r)` is the mineral/reservoir partition coefficient, with `C_E,m` and `C_E,r` the element concentrations in mineral `m` and reservoir `r`.

These relationships can strongly alter parent/daughter elemental ratios across reservoirs and minerals.

However, chemical partitioning ordinarily acts primarily on elements and may produce only limited isotope fractionation for heavy radiogenic systems.

This distinction is central.

## 4. Mass-balance prediction

Mass balance plus partitioning can predict correlated elemental parent/daughter ratios across reservoir families if:

1. bulk inventory is constrained;
2. partition coefficients are constrained;
3. phase proportions are constrained.

This is genuine predictive structure.

For example, a reservoir process can create variation in `Rb/Sr`, `Sm/Nd`, `U/Pb`, or `Lu/Hf` across co-genetic phases without assigning each phase independently.

Thus a common reservoir generator can reduce degrees of freedom at the **elemental-ratio level**.

## 5. Isochron problem

A conventional isochron relation has the form:

```text
D_now / D_ref
  = (D_initial / D_ref)
  + (P_now / D_ref) * (exp(lambda T) - 1)
```

Across co-genetic samples, variation in parent/reference ratio creates a line whose slope is:

```text
m = exp(lambda T) - 1
```

A reservoir model can naturally generate the horizontal spread in parent/reference ratios through chemical partitioning.

It does **not**, by mass balance alone, generate the age-like slope `m`.

This is a second form of the WP-008/WP-009 result.

### Result

```text
reservoir partitioning
    -> parent/reference variation

reservoir partitioning alone
    !=> radiogenic isochron slope
```

## 6. U-Pb application

A source reservoir can constrain:

- total U inventory;
- U-238/U-235 abundance;
- total Pb inventory;
- Pb isotopic composition;
- U/Pb differentiation;
- zircon U uptake;
- zircon Pb exclusion;
- reservoir-to-mineral mass balance.

These constraints substantially reduce arbitrary state freedom.

But they still do not force:

```text
Pb206*/U238 = exp(lambda238 q) - 1
Pb207*/U235 = exp(lambda235 q) - 1
```

for one independently derived common `q`.

If `q` is introduced only to match concordia, it fails the WP-009 age-surrogate test.

## 7. Cross-system consequence

The reservoir framework nevertheless produces an important DFM research advance.

A valid initialization generator cannot be isotope-system specific. The same reservoir architecture must propagate into:

- U-Pb;
- Pb-Pb;
- Rb-Sr;
- Sm-Nd;
- Lu-Hf;
- Re-Os;
- K-Ar/Ar-Ar where applicable;
- extinct-radionuclide daughter systems.

Therefore the initialized state can be represented as a coupled vector:

```text
V_r = {
  U/Pb,
  Rb/Sr,
  Sm/Nd,
  Lu/Hf,
  Re/Os,
  K/Ar,
  isotopic compositions,
  phase fractions,
  thermal contribution
}
```

The same `G` must generate all components subject to common mass balance.

This converts “global coherence” from rhetoric into a model requirement.

## 8. First cross-system prediction

The first genuine prediction from the reservoir framework is qualitative but nontrivial:

> Isotope-system initialization parameters must covary according to shared reservoir chemistry and mass balance rather than behaving as independently tunable age markers.

Accordingly, a DFM reservoir model predicts structured covariance among elemental parent/daughter ratios tied to differentiation and mineral partitioning.

It does **not yet** predict the radiogenic daughter slopes conventionally interpreted as elapsed time.

This distinction must be preserved.

## 9. Degrees-of-freedom accounting

Let `N` isotope systems be modeled over `R` reservoirs.

An unconstrained mature-state model could assign independent parent and daughter values to every system and reservoir, producing parameter growth approximately proportional to `N x R`.

A common reservoir generator should instead derive many states from:

- one bulk inventory vector;
- a finite reservoir architecture;
- constrained partition coefficients;
- phase fractions;
- ordinary laws.

A successful DFM programme should therefore show **sublinear growth of free initialization parameters relative to observations explained**.

This is now a programme metric.

### Complexity criterion

Define:

```text
rho = N_free_initialization_parameters / N_independent_observational_constraints
```

Here `rho` is the parameter-to-constraint ratio, `N_free_initialization_parameters` counts freely adjustable initialization parameters, and `N_independent_observational_constraints` counts independent observational constraints.

A developing DFM generator should drive `rho` downward as cross-system evidence is added.

If `rho` remains constant or increases because each isotope system needs new unconstrained initialization values, the programme is degenerating.

## 10. Baseline result

### Positive result

Reservoir-level modeling is materially stronger than grain-level mature-state assignment because:

- it enforces global conservation;
- it couples mineral populations;
- it provides independent chemical reasons for parent/daughter elemental variation;
- it naturally extends across isotope systems;
- it supplies a quantitative degrees-of-freedom framework.

### Negative result

Mass balance and chemical partitioning alone do not generate the radiogenic daughter relationships that define concordia or isochron slopes.

Therefore no current DFM reservoir model explains the central chronometric convergence.

### Canonical conclusion

> Source-reservoir architecture is a necessary constraint on any viable DFM radiogenic initialization model, but it is not sufficient to derive radiometric concordance. Its immediate predictive content concerns coupled elemental and isotopic inventories and their covariance across reservoirs. The radiogenic daughter relationships conventionally associated with elapsed time remain an unresolved explanatory burden.

## 11. Implications for the orderly-marker hypothesis

The phrase **orderly marker** remains admissible only at two levels:

1. **Established DFM expectation:** initialized reservoirs should exhibit globally coherent, mass-balanced physical order.
2. **Research hypothesis:** radiometric concordance may be one manifestation of that order.

The second must not be promoted to an explanation until a generator derives it.

## 12. Next severe test

WP-011 should test a system where reservoir partitioning is central to the conventional method: **Rb-Sr isochrons**.

Why Rb-Sr:

- Rb and Sr partition differently during igneous differentiation;
- multiple co-genetic phases can acquire different Rb/Sr ratios;
- the isochron method explicitly separates a common initial daughter ratio from the radiogenic slope;
- heat-budget motivation is weak, removing the strongest DFM functional anchor;
- the method therefore directly tests whether reservoir architecture can explain horizontal structure while leaving the age-like slope unexplained.

WP-011 should quantify exactly which portion of an Rb-Sr isochron DFM reservoir initialization can derive independently and which portion still requires a historical or alternative common generator.
