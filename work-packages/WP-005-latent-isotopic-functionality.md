# WP-005: Latent Isotopic Functionality and Daughter-Product Necessity

**Status:** Proposed ancillary hypothesis; initial research baseline (2026-10-27)  
**Parent:** DFM radiogenic track, WP-004; dependent on WP-002  
**Epistemic status:** Empirical contributions established in selected systems; isotope-specific and initialization-specific necessity unverified.

## Research question
Could the initial inventory of selected radiogenic daughter isotopes be functionally constrained by Earth's immediate and continuing habitability, including coupled functions not yet identified?

## Three claims, kept separate
- **H1, present participation:** Selected daughter products participate in present terrestrial atmospheric, mineralogical, geochemical, and physical systems. This is demonstrable in particular cases.
- **H2, functional necessity:** At least one daughter isotope's abundance, ratio, or spatial distribution is required to satisfy an independently specified terrestrial functional constraint. This is unproven.
- **H3, initialization necessity:** That required inventory had to be present at functional commissioning rather than accumulated by ordinary post-initialization decay. This is unproven and requires an explicit time-dependent model.

**LIFH:** An initialized, life-friendly terrestrial state may require coordinated parent and daughter inventories whose functional effects include presently unknown isotope-specific or coupled-system relationships. Unknown functions are candidates for discovery, not evidence by themselves.

## Model
Let R0 = (P0, D0, X0, T0, A0), representing initial parent and daughter nuclide inventories, spatial/mineral distribution, thermal state, and atmosphere. After initialization, ordinary measured decay and geochemical transport govern evolution. Define independently measured functional constraints C_j(R(t)) >= threshold_j over specified time intervals. An isotope is *initially necessary* only if admissible alternatives with D0,i = 0 (or an isotope-substituted control) cannot satisfy the constraints while holding all other independently justified assumptions fixed. Account for mass balance, decay branching, isotope effects, toxicity, and transport.

## Candidate evidence matrix
| Daughter isotope/system | Established present contribution | Unproven necessity claim | Primary test |
|---|---|---|---|
| K-40 -> Ar-40 | Dominant atmospheric argon isotope; atmospheric gas contributes to pressure and transport properties | Particular initial Ar-40 fraction necessary for habitability | Atmospheric model: removal versus equal-mole isotope substitution; include degassing and escape |
| K-40 -> Ca-40 | Calcium participates in minerals and living systems | Radiogenic Ca-40 specifically required at initialization | Hold calcium concentration fixed, vary isotopic fractions; quantify fractionation effects |
| U/Th -> Pb-206/207/208 | Lead-bearing minerals and isotope inventories | Specific lead isotope mix functionally necessary | Mineral stability and partitioning simulations with isotope substitution |
| Rb-87 -> Sr-87 | Strontium-bearing minerals; biological substitution for calcium in some systems | Sr-87 rather than other stable Sr isotopes necessary | Isotope-substitution and mineral fractionation tests |
| Sm-147 -> Nd-143 | Rare-earth-bearing minerals | Nd-143 specific functional requirement | Mineral partitioning and isotope-sensitive transport |
| Lu-176 -> Hf-176 | Hafnium-bearing minerals including zircon | Hf-176-specific structural requirement | Crystal chemistry/isotope substitution |
| U/Th chains -> He-4 | Groundwater/geothermal tracer; fluid gas inventory | Initial helium inventory required | Degassing, retention, and transport model |

An isotope's *measurement usefulness* as a tracer is not evidence of necessity for life or geophysical operation. Likewise, a present contribution does not establish an indispensable initial inventory. Intermediate decay-chain products include hazardous radionuclides and must be evaluated for adverse as well as beneficial effects.

## Experiments and discriminators
1. **Deletion:** Remove a selected daughter isotope; explicitly track changes to elemental abundance, total mass, pressure, and charge balance.
2. **Substitution:** Replace it with a stable isotope of the same element at constant atom count; isolate isotope-specific effects.
3. **Redistribution:** Preserve total daughter inventory but vary mineralogical/geographic placement.
4. **Timing:** Compare zero initial daughter inventory plus ordinary decay against nonzero initialized inventory with the same post-boundary physics.
5. **Coupled effects:** Evaluate atmospheric-geochemical-thermal interactions rather than inferring system-level necessity from one element.
6. **Adversarial cross-system test:** Derive predicted isotopic correlations from functional constraints *before* fitting measured ratios, including U-Pb concordia, Rb-Sr isochrons, Sm-Nd, and independently dated post-initialization events.

## Failure criteria
- The claimed function is preserved by isotope substitution, defeating isotope-specific necessity.
- The function is preserved by post-initialization accumulation, defeating initialization necessity.
- Claimed constraints are chosen only after observing target isotope ratios.
- Each sample requires an unconstrained, separately tuned D0.
- Predicted isotopic distributions or concordance patterns fail independently held-out tests.

## Research status and next gate
This is a hypothesis specification and candidate inventory, not a completed quantitative model or validation. The next deliverable is the WP-004 Radiogenic Coherent Initialization Matrix (RCIM), extended with functional category, isotope-substitution controls, timing controls, uncertainty, and sources. Prioritize K-Ar atmospheric mass-balance and U-Pb mineral-scale cross-system tests. Record independently specified functional thresholds before simulation.

## Source starting points
- DFM canonical WP-002 and WP-004 in this repository (primary programme documents).
- Abe et al. (2022), *Geoneutrinos and Earth's interior*, for radiogenic thermal constraints (verify full bibliographic metadata before scholarly citation).
- Dauphas, N. and Schauble, E.A. (2016), *Mass Fractionation Laws, Mass-Independent Effects, and Isotopic Anomalies*, Annual Review of Earth and Planetary Sciences 44, 709-783 (verify exact pages and DOI before publication).
- ICR/CRS RATE technical volumes as primary documents for RATE's own claims; independently assess interpretations and heat-budget objections.

## Governance
Ancillary/protective-belt hypothesis only. No changes to hard core, chronology, decay constants, or accepted observations. Preserve the WP-002 no-smuggling rule and WP-004 quantitative concordance obligations.
