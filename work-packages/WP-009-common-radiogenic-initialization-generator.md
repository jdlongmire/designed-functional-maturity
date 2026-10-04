# WP-009: Common Radiogenic Initialization Generator

**Status:** Executed baseline  
**Parent:** DFM Research Programme  
**Depends on:** WP-004, WP-007, WP-008

## Purpose

Test whether DFM can replace sample-by-sample radiometric initialization with a common physical generator that produces the observed U-Pb concordia relationship without using conventional radiometric age as an input.

The target is not merely to show that an initialized state *can* contain concordant isotope ratios. The target is to identify independent constraints that reduce the relevant degrees of freedom and predict concordant structure.

## 1. Problem inherited from WP-008

For a concordant zircon domain:

```text
x = Pb206*/U238 = exp(lambda238 T_R) - 1
y = Pb207*/U235 = exp(lambda235 T_R) - 1
```

The pair `(x,y)` occupies a one-dimensional curve because the same parameter `T_R` controls both decay systems.

Under a short-history DFM initialization:

```text
x0 ~= x
y0 ~= y
```

unless substantial post-initialization decay occurred.

Therefore a DFM generator must explain why the two initialized daughter-parent ratios are not independent.

## 2. Candidate generator architecture

Define a common generator:

```text
S0_rad = G(R, Uiso, P, X, F, L)
```

where:

- `R` = source-reservoir elemental and isotopic composition;
- `Uiso` = uranium isotopic abundance relationship;
- `P` = mineral partition/crystal-chemistry constraints;
- `X` = common-Pb and daughter-hosting constraints;
- `F` = commissioned functional constraints, including thermal architecture;
- `L` = ordinary nuclear and chemical law.

For zircon domain `j`:

```text
Z_j = P_j(S0_rad)
```

and its initialized U-Pb state is:

```text
(x0_j, y0_j) = Q(Z_j)
```

A successful generator must yield a population-level relation:

```text
y0 = g(x0)
```

without defining `g` by the conventional target age of each grain.

## 3. Constraint decomposition

### C1. Thermal constraint

Radiogenic heat constrains the bulk abundance and distribution of long-lived heat-producing parents, especially U, Th, and K.

**Result:** constrains parent inventory, but does not determine daughter ratios.

### C2. Uranium-isotope constraint

The two U decay systems share the same element and therefore are coupled by the uranium isotope abundance of the source and mineral.

**Result:** removes some independent parent freedom, but does not by itself determine Pb206*/U238 and Pb207*/U235.

### C3. Zircon partition constraint

Zircon strongly accepts U relative to Pb during crystallization. Conventional U-Pb practice exploits this because low initial Pb makes subsequent radiogenic Pb accumulation interpretable.

**Result:** this constraint works against a simple DFM proposal that mature zircon merely begins with arbitrary large daughter Pb dissolved uniformly in the lattice.

### C4. Common-Pb constraint

Non-radiogenic/common Pb can be measured or modeled separately in high-quality U-Pb work, and total-Pb/U methods can incorporate common-Pb uncertainty.

**Result:** common Pb cannot generically supply the required radiogenic daughter relation.

### C5. Post-initialization decay

Ordinary decay after `S0` moves an initialized point forward according to the same decay laws.

**Result:** for a short post-initialization interval, it produces only a small displacement relative to multi-Ga concordia positions and therefore cannot generate the missing deep concordia structure.

### C6. Reservoir mass-balance constraint

A common source reservoir can couple elemental and isotopic inventories across many mineral domains.

**Result:** promising as a population-level constraint, but no currently specified mass-balance law forces the exact concordia relation.

## 4. Dimensionality test

The central test is dimensional.

Observed ideal concordia occupies approximately a one-dimensional locus in the two-dimensional `(x,y)` space.

A DFM generator succeeds only if independent physics reduces the admissible initialized state family to approximately the same one-dimensional locus, or to a narrow family that predicts the observed data.

If the generator leaves `x0` and `y0` independently adjustable, it has not explained concordance.

If it imposes:

```text
y0 = [1 + x0]^(lambda235/lambda238) - 1
```

merely because that is the algebraic elimination of `T` from the conventional decay equations, then it has renamed concordia rather than explained it.

## 5. Age-equivalence test

Any proposed common parameter `q` must be tested for age equivalence.

Suppose:

```text
x0 = f238(q)
y0 = f235(q)
```

If:

```text
q = h(T_R)
```

or if `q` has no independent measurement or physical derivation apart from fitting the concordia position, then `q` is an age surrogate.

**Rule:** an initialization parameter is not independent merely because it is given a different name.

## 6. Candidate hypotheses assessed

### H1. Heat-budget generator

```text
Phi_thermal -> U inventory -> concordia
```

**Assessment:** insufficient. The bridge from U inventory to paired daughter ratios is missing.

### H2. Fixed global isotopic-state generator

All created reservoirs receive one globally coherent U-Pb isotopic state.

**Assessment:** insufficient for the observed range of zircon concordia positions and geological populations unless subsequent history generates that range. A single state does not explain a family of apparent formation ages.

### H3. Reservoir-class generator

Different functional reservoirs receive distinct but physically derived U-Pb states based on reservoir role and chemistry.

**Assessment:** potentially testable but presently underconstrained. If each reservoir receives whatever state matches its conventional age, this degenerates into target-age fitting.

### H4. Mineral-formation-state generator

Each mineral is initialized with daughter products corresponding to its mature structural/chemical state.

**Assessment:** weak in current form. Zircon's Pb exclusion means large radiogenic daughter inventories require an additional physical account, and grain-specific states risk encoding fictional event histories.

### H5. Global lawful-order generator

The initialized universe is specified by a deeper common state relation that constrains multiple isotope systems simultaneously.

**Assessment:** conceptually closest to DFM's orderly-marker claim, but not yet a physical model. It becomes scientifically useful only when the relation is derived independently and predicts more than concordia.

## 7. Baseline result

**No currently specified DFM constraint set derives the U-Pb concordia relation independently of age.**

This is a negative result for the strongest current radiogenic-concordance claim.

It does not show that designed initialization is impossible. It shows that the present DFM programme has not yet earned the claim that coherent initialization *explains* U-Pb concordance.

The canonical wording should therefore remain:

> DFM expects a globally coherent initialized radiogenic state and treats concordance as a candidate orderly marker. The radiogenic heat budget supplies an independent constraint on parent radionuclide architecture, but no age-independent physical generator has yet been demonstrated that derives the observed dual U-Pb concordia relation.

## 8. Productive consequence

The negative result narrows the research programme.

Future work should not search for arbitrary initial daughter assignments. It should ask whether a deeper common generator has independent consequences outside U-Pb.

A viable generator should simultaneously constrain at least:

- U isotope abundance;
- U/Th/K heat architecture;
- Pb isotopic inventory;
- zircon partition behavior;
- source-reservoir mass balance;
- non-heat-centric isotope systems;
- meteorite/terrestrial/lunar relationships.

If it explains only U-Pb, it is likely an age surrogate.

## 9. Severe falsification pressure

The orderly-marker auxiliary should be downgraded if:

1. no independent generator can reduce U-Pb initialization freedom;
2. candidate generators require conventional ages as hidden parameters;
3. zircon chemistry contradicts the required daughter-hosting state;
4. extending the generator to other isotope systems requires unrelated tuning;
5. conventional provenance models continue to predict concordance/discordance patterns with materially fewer unconstrained parameters.

## 10. Next gate

WP-010 should move one level deeper and test whether **source-reservoir isotopic architecture plus mass balance** can generate any nontrivial cross-system predictions before mineral-level age fitting.

The target should be a falsifiable reservoir model, not another conceptual restatement.
