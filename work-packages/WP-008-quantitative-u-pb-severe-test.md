# WP-008: Quantitative U-Pb Severe-Test Model

**Status:** Executed — baseline model  
**Parent:** DFM Research Programme  
**Depends on:** WP-002, WP-004, WP-007

## Purpose

Turn the U-Pb concordance burden into an explicit mathematical severe test of the DFM coherent-initialization hypothesis.

## Model

For a zircon domain with present parent inventories `N238` and `N235`, ordinary closed-system decay from a boundary state gives radiogenic daughters:

```text
D206(t) = D206_0 + N238_0 (1 - exp(-lambda238 t))
D207(t) = D207_0 + N235_0 (1 - exp(-lambda235 t))
```

Here `D206(t)` and `D207(t)` are daughter inventories at time `t`; `D206_0` and `D207_0` are initial daughter inventories; `N238_0` and `N235_0` are initial parent inventories; `lambda238` and `lambda235` are the measured decay constants; and `t` is elapsed time.

Equivalently in present-parent form:

```text
D206_rad / U238_now = exp(lambda238 t) - 1
D207_rad / U235_now = exp(lambda235 t) - 1
```

Here `D206_rad` and `D207_rad` are radiogenic daughter inventories, while `U238_now` and `U235_now` are present parent inventories.

Concordia arises because one value of `t` simultaneously satisfies both decay systems.

## DFM boundary problem

At DFM initialization time `t=0`, a mature zircon state may contain U and state-consistent daughter Pb. But the initial daughter state is not free merely because DFM permits initialization.

The severe test is whether an independently constrained initialization rule `G` can produce:

```text
(D206_0/U238_0, D207_0/U235_0)
```

that lies on, or generates after short prospective evolution, the observed concordia structure **without using the target conventional age as an input**.

## Key result of baseline execution

For a perfectly concordant point corresponding to a conventional age `T_R`, the required initialized daughter ratios under negligible DFM elapsed time are approximately:

```text
r206_0 ~= exp(lambda238 T_R) - 1
r207_0 ~= exp(lambda235 T_R) - 1
```

Here `r206_0` and `r207_0` are initialized radiogenic daughter-to-parent ratios, and `T_R` is the retrodictive duration.

Therefore the two initial daughter ratios must satisfy the same nonlinear relationship that defines conventional concordia.

This is not automatically explained by the bulk heat budget.

The heat budget constrains U inventory. It does not by itself select the paired Pb-206 and Pb-207 daughter abundances required to place zircon domains on the dual-decay concordia curve.

## Consequence

The orderly-marker hypothesis remains logically possible but acquires a sharp quantitative burden:

> DFM must identify an independent physical, chemical, mineralogical, nucleosynthetic, or functional generator that produces the dual daughter-parent relationship corresponding to concordia without encoding the conventional age parameter.

Merely initializing “appropriate Pb” is target-age smuggling.

## Zircon constraint

Zircon generally incorporates U while excluding most Pb during crystallization. Therefore a DFM model in which mature zircons are initialized with large radiogenic-Pb inventories must explain how that state relates to zircon crystal chemistry.

Candidate hypotheses must distinguish:

1. Pb incorporated during initialized crystal specification;
2. Pb generated as state-consistent radiogenic daughter information;
3. Pb hosted in nanoscale phases or damage domains;
4. common Pb;
5. actual post-initialization radiogenic Pb.

These are physically different claims.

## Severe-test criteria

### ST-1: Dual-decay independence

A single initialization rule must account for both U-238/Pb-206 and U-235/Pb-207.

### ST-2: No target age

No parameter may be set by first calculating the conventional U-Pb age of the sample.

### ST-3: Zircon chemistry

The initialized daughter state must be compatible with observed zircon chemistry and microstructure.

### ST-4: Population structure

The rule must account for populations of concordant zircons, not one hand-selected grain.

### ST-5: Discordance

The model must generate or permit observed discordia behavior under independently warranted post-initialization disturbance.

### ST-6: Cross-system extension

A successful U-Pb rule must not make Rb-Sr, Sm-Nd, Pb-Pb, Lu-Hf, or extinct-radionuclide concordance less plausible.

## Baseline appraisal

**Result: unresolved, high-pressure.**

The current DFM radiogenic heat constraint is insufficient by itself to derive U-Pb concordance.

This does **not** establish that concordia uniquely proves traversed pre-initialization time. It establishes that DFM has not yet supplied a quantitative alternative generator for the dual-isotope structure.

Accordingly the flagship claim must remain:

- concordance is compatible with an orderly initialized state in principle;
- DFM expects global order rather than arbitrary isotope states;
- but quantitative explanation of U-Pb concordance remains an unresolved severe test.

## Next hypothesis-development gate

Investigate whether a common initialization generator can be derived from constraints stronger than the heat budget alone, including:

- bulk nucleosynthetic isotope inventory;
- U isotopic abundance relationship;
- mineral lattice and partition constraints;
- coupled elemental/isotopic mass balance;
- planetary differentiation constraints;
- functional thermal requirements;
- common initialization of source reservoirs rather than sample-level tuning.

Any candidate generator must be specified before fitting zircon ages.
