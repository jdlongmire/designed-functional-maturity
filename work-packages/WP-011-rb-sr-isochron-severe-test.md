# WP-011: Rb-Sr Isochron Severe Test

**Status:** Executed baseline  
**Parent:** DFM Research Programme  
**Depends on:** WP-007 through WP-010

## Purpose

Use the Rb-Sr isochron method as a severe discriminator between:

1. structure that follows naturally from source-reservoir chemistry and mass balance; and
2. structure that still requires a common radiogenic-history parameter or an independently derived DFM alternative.

Rb-Sr is especially useful because its conventional formulation explicitly separates a common initial daughter ratio from the radiogenic slope.

## 1. Conventional isochron equation

For co-genetic samples or mineral phases:

```text
(87Sr/86Sr)_now
  = (87Sr/86Sr)_0
  + (87Rb/86Sr)_now [exp(lambda87 t) - 1]
```

Define:

```text
y = 87Sr/86Sr
x = 87Rb/86Sr
b = (87Sr/86Sr)_0
m = exp(lambda87 t) - 1
```

Then:

```text
y = b + m x
```

The intercept represents the common initial Sr isotopic ratio under the conventional co-genetic model. The slope represents radiogenic growth and is converted to a retrodictive age.

## 2. What DFM reservoir initialization can derive

WP-010 established that a common initialized reservoir can constrain:

- total Rb inventory;
- total Sr inventory;
- bulk Sr isotopic composition;
- reservoir mass balance;
- Rb/Sr differentiation;
- mineral-specific Rb/Sr partitioning;
- covariance among co-genetic phases.

This provides a principled route to variation in:

```text
x_j = (87Rb/86Sr)_j
```

across samples `j`.

A common source reservoir can also motivate a common or narrowly distributed initial:

```text
b = (87Sr/86Sr)_0
```

subject to mixing and source heterogeneity.

Thus DFM can independently motivate two important ingredients of an isochron:

1. horizontal spread in `x`;
2. a shared initial daughter/reference baseline `b`.

## 3. The slope problem

Neither mass balance nor Rb/Sr partitioning by itself forces:

```text
y_j - b = m x_j
```

with one common nonzero `m`.

Partitioning generates variation in `x_j`. To produce an isochron, the excess radiogenic daughter component must scale linearly with that parent/reference ratio.

Under ordinary traversed decay this follows directly because every co-genetic phase experiences the same elapsed time:

```text
m = exp(lambda87 t) - 1
```

Under short-history DFM, most of a large conventional slope would have to be present at initialization.

The initialization generator must therefore produce:

```text
(87Sr/86Sr)_0,j
  = b + m* (87Rb/86Sr)_0,j
```

or an equivalent state relationship, where `m*` is derived independently of the target conventional age.

## 4. Why this is a severe test

Unlike U-Pb zircon, Rb-Sr does not obtain its principal DFM motivation from Earth's radiogenic heat budget.

Rb-87 contributes negligibly to terrestrial heat compared with U, Th and K. Therefore the argument:

```text
functional heat requirement -> radiogenic inventory
```

does little explanatory work here.

Rb-Sr asks more directly whether **global coherent initialization itself** predicts a radiogenic-looking population relation.

## 5. Intercept versus slope

This WP establishes a critical decomposition:

### Intercept

A common source reservoir can independently motivate a common initial Sr isotopic composition.

**DFM status:** physically plausible reservoir constraint.

### Horizontal spread

Chemical differentiation and mineral partitioning can independently generate a range of Rb/Sr ratios.

**DFM status:** physically plausible and expected.

### Slope

A common nonzero relationship between radiogenic 87Sr excess and Rb/Sr ratio requires an additional generator.

**DFM status:** unresolved.

Therefore:

```text
reservoir initialization
    -> common intercept + x-spread

reservoir initialization alone
    !=> radiogenic slope
```

## 6. Initialization inversion

Suppose a co-genetic suite has conventional retrodictive age `T_R`, but only short actual post-initialization time `tau` has elapsed.

The observed slope is:

```text
m_R = exp(lambda87 T_R) - 1
```

Ordinary post-initialization decay contributes:

```text
m_tau = exp(lambda87 tau) - 1
```

The initialization boundary must supply approximately:

```text
m_0 = m_R - m_tau
```

for short `tau`, approximately:

```text
m_0 ~= m_R
```

Thus the initialized daughter state must already covary with the parent/reference ratio across the mineral population.

## 7. Age-surrogate test

Any proposed initialization parameter `q` satisfying:

```text
m_0 = f(q)
```

must have independent physical meaning and measurement.

If:

```text
q = h(T_R)
```

or is chosen solely to fit the observed slope, it is an age surrogate and fails WP-009.

## 8. Candidate explanations

### H1. Common reservoir chemistry

Can explain intercept and Rb/Sr spread.

**Slope:** not generated.

### H2. Equilibrium isotope fractionation

Heavy-isotope fractionation may modify Sr isotope ratios slightly under some conditions.

**Slope:** no demonstrated reason it should generate the parent-proportional radiogenic relation over large conventional age ranges.

### H3. Mixing

Mixing can generate linear arrays in isotope diagrams.

**Status:** important conventional and DFM confounder. A line alone is not sufficient evidence of an isochron. However, invoking mixing must be independently supported and cannot explain all high-quality isochrons by default.

### H4. Designed population-level covariance

The initialized suite is specified so that daughter excess covaries with parent abundance.

**Status:** mathematically sufficient but physically unexplained. Unless derived from an independent common constraint, this simply installs the isochron slope at initialization.

### H5. Global lawful-order generator

A deeper creation-state law simultaneously relates parent abundance and daughter isotope state across reservoirs.

**Status:** research hypothesis only. It becomes explanatory only if derived independently and if it predicts multiple isotope systems without clock-by-clock fitting.

## 9. Cross-system pressure

A DFM explanation cannot stop at Rb-Sr.

If a rock or meteorite population yields mutually consistent Rb-Sr, Sm-Nd, U-Pb, Pb-Pb, or other chronometer outputs, then a common initialization generator must account for several distinct slope relations:

```text
m_i = exp(lambda_i T_R) - 1
```

Each system has a different decay constant.

If the generator independently assigns `m_i` to reproduce one common `T_R`, it has encoded the age.

This is a stronger form of the concordance burden.

## 10. Severe-test criteria

### ST-1: Common-intercept prediction

DFM should derive or constrain the initial Sr isotope baseline from source-reservoir architecture.

### ST-2: Parent-ratio spread

DFM should derive Rb/Sr variation from chemical/mineral partitioning rather than arbitrary sample assignment.

### ST-3: Slope independence

The nonzero slope must be derived without conventional target age.

### ST-4: Mixing discrimination

Any claim that a linear array is mixing rather than radiogenic must be supported by independent geochemical evidence.

### ST-5: Cross-system consistency

A proposed slope generator must extend to at least one other isotope system with a different decay constant.

### ST-6: Complexity reduction

Adding Rb-Sr must reduce or preserve the programme complexity ratio `rho`, not require a new unconstrained slope parameter for each suite.

## 11. Baseline result

**Rb-Sr sharpens the negative result from WP-008 through WP-010.**

DFM reservoir initialization can plausibly explain:

- common-source initial Sr composition;
- Rb/Sr differentiation;
- mineral-population structure.

It does not presently explain:

- the common radiogenic slope;
- the mapping of that slope through the measured Rb-87 decay constant to the same retrodictive ages obtained by independent systems.

Therefore the current orderly-marker hypothesis remains **underived at the chronometric-slope level**.

## 12. Canonical programme statement

> DFM reservoir architecture provides an independent physical basis for common initial isotopic composition and parent/daughter differentiation. It has not yet supplied an age-independent generator for the radiogenic slopes of isochrons. Cross-system agreement among slopes therefore remains a principal severe test of the orderly-marker hypothesis.

## 13. Implication for programme direction

The repeated structure across U-Pb and Rb-Sr is now clear:

```text
physical initialization constraints
    -> parent architecture
    -> source/reservoir structure
    -> mineral differentiation

but not yet:

physical initialization constraints
    -> decay-constant-indexed daughter relation
```

The unresolved object is no longer generic “radiometric dating.” It is specifically the family of **decay-constant-indexed covariance relations**.

## 14. Next gate

WP-012 should formalize this object across multiple systems.

Proposed target:

**Decay-Constant-Indexed Concordance Theorem/Challenge**

For isotope systems `i` with distinct `lambda_i`, conventional common-age concordance satisfies:

```text
m_i = exp(lambda_i T) - 1
```

The next WP should ask whether any non-temporal common generator can produce this family of relations without containing a parameter mathematically equivalent to `T`.

This is now the central formal problem for the DFM orderly-marker hypothesis.
