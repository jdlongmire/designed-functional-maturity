# DFM-PAM-013: Nuclear Heat-Coefficient Reconciliation

**Date:** 2026-10-27. **Status:** Numerical reconciliation of approximate published full-chain heat yields; initial-chain populations remain unmodeled.

## Independent coefficient comparison

Source full-chain heat yields are entered as joules per decay from Dye (2012), *Reviews of Geophysics*, https://doi.org/10.1029/2012RG000400. Prototype isotope fractions and half-lives remain approximate. Elemental benchmark coefficients are those recorded in `track_a_elemental_power.py`.

| Element | Decay-derived (W/kg element) | Elemental benchmark (W/kg element) | Relative difference |
|---|---:|---:|---:|
| U | 9.85146e-5 | 9.829e-5 | +0.23% |
| Th | 2.62710e-5 | 2.618e-5 | +0.35% |
| K | 3.41324e-9 | 3.390e-9 | +0.69% |

These are calculations from the **same physical decay process** using different parameterizations, not statistically independent empirical observations. Numerical proximity checks unit and convention consistency; it does not prove the nuclear inputs or an Earth chronology.

## Critical initial-chain-population gate
The U-238, U-235 and Th-232 coefficients incorporate energy released by their *complete decay chains*, not necessarily energy deposited immediately when a parent decays. In a short elapsed history, intermediate half-lives (notably U-234, Th-230 and Ra-226 in the U-238 chain) can affect the temporal distribution of heat. Thus a model with initialized stable lead daughters must also specify intermediate radioactive inventories, or explicitly establish secular equilibrium, to use the full-chain instantaneous power formula. Such an initial equilibrium state is a substantive auxiliary hypothesis and must be evaluated for physical coherence, independent mineral constraints and natural isotopic signatures.

## Limitations and next test
- Replace approximate natural isotope atom fractions used as mass fractions with precise mass-based conversion.
- Audit published heat yields and K-40 branching against current evaluated ENSDF/IAEA nuclear data.
- Implement a Bateman-chain or equivalent numerical time evolution for initialized intermediate radionuclides.
- Test at least three cases: depleted intermediate chains, secular equilibrium, and independently constrained initial intermediates.
- Report time-resolved power and cumulative heat under each case, separately from stable initialized daughter products.
- Recompute published BSE reservoir powers with reconciled coefficients and uncertainty propagation.

**Track A judgment:** coefficient conventions numerically reconciled; short-history chain heat and geologic thermal plausibility remain open.
