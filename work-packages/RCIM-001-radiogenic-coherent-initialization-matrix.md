# RCIM-001: Radiogenic Coherent Initialization Matrix

**Status:** Proposed research baseline, not empirical validation. **Parent:** WP-004, WP-005, WP-002. **Date:** 2026-10-27.

## Governing distinctions
- **Sufficiency:** the observed isotopic state supports an independently defined function.
- **Constraint:** the function restricts a family of admissible states.
- **Uniqueness:** only one state works; not presumed.
- **Provenance:** how the state originated; not inferred from present utility.
- Isotope substitution is a *sensitivity analysis*, not a general discriminator for DFM.
- Standard geochronology does not universally assume zero initial daughter products. Address common daughters, inheritance, mixing, closure and disturbance explicitly.
- Ordinary observed decay remains in force after the initialization boundary. Avoid unconstrained sample-specific daughter inventories.

## Candidate systems

| System | Established physical context | Proposed functional constraint (unverified) | Observed structure requiring explanation | Principal confounders | Independent severe test |
|---|---|---|---|---|---|
| U-238/Pb-206 and U-235/Pb-207 | U contributes radiogenic heat; U and Pb partition differently into minerals | Initial mineralogical and thermal constraints restrict parent/daughter distributions | Dual-chain U-Pb concordia and discordia in zircon | Common Pb, inheritance, Pb loss, metamorphism | One generative initial-state rule predicts both chains in held-out zircon data without fitting target ages |
| Th-232/Pb-208 | Th contributes radiogenic heat | Thermal/mineral requirements restrict Th/Pb inventories | Th-Pb and coupled U-Th-Pb mineral signatures | Open-system alteration, common Pb | Joint cross-mineral predictions using shared initialization parameters |
| K-40/Ar-40 | K contributes heat; argon is an atmospheric gas; Ar-40 dominates present atmospheric Ar | Atmospheric/thermal requirements restrict admissible Ar and K distributions | K-Ar and Ar-Ar mineral patterns; atmospheric Ar inventory | Degassing, escape, trapped/excess Ar, heating | Time-dependent mass balance with independent atmospheric and known-age sample controls |
| K-40/Ca-40 | Calcium is important to mineral and biological systems | Calcium isotope inventory is functionally constrained | K-Ca isotopic relationships | Large nonradiogenic Ca reservoir, mixing | Predict measurable restrictions beyond total elemental calcium |
| Rb-87/Sr-87 | Rb/Sr partitioning in minerals | Mineral chemistry restricts Sr inventory and distribution | Rb-Sr isochrons | Initial Sr, mixing, resetting | Jointly predict slopes/intercepts without post hoc initial-ratio assignment |
| Sm-147/Nd-143 | Rare-earth mineral partitioning | Mineral/source constraints restrict Nd isotopic states | Sm-Nd isochrons and source signatures | Source heterogeneity, mixing | Predict held-out mineral/source isotope patterns |
| Lu-176/Hf-176 | Hf is incorporated into zircon | Mineral/source constraints restrict Hf isotopic states | Lu-Hf patterns alongside U-Pb | Inheritance, source mixing | Joint zircon U-Pb/Hf predictions |
| U/Th chains/He-4 | Alpha production, diffusion and mineral retention | Fluid/thermal constraints restrict He inventory | U-Th-He retention signatures | Diffusion, thermal history, escape | Predict independently constrained retention and heating events |

## Test architecture

**Gate A: Independent functional constraints.** Define measurable atmospheric, mineralogical, thermal or geochemical performance criteria before examining target isotopic ratios. Record uncertainties and alternatives. A demonstrated elemental function does not imply isotope-specific necessity.

**Gate B: Constrained initialization generator.** Express initial state as R0 = G(Phi, L, B), with common rules and limited parameters. Specify which parameters are shared globally, regionally, and by mineral class. No arbitrary independent initial daughter assignment per sample.

**Gate C: Forward evolution.** Apply measured decay constants, decay branching, heat generation, transport, mineral partitioning and independently justified disturbance processes after initialization.

**Gate D: Held-out prediction.** Derive quantitative isotope-ratio and spatial-pattern predictions, including U-Pb dual-clock concordance, without fitting the target ratios or reconstructed ages. Separate training and held-out samples.

**Gate E: Comparative appraisal.** Evaluate the same measurements against conventional geochronological accounts with appropriate initial-daughter corrections, closure models, geological controls and uncertainties. Compare predictive accuracy and parameter complexity, not mere mathematical fit.

## First executable analyses

1. **K-Ar:** Build an atmospheric and mineral mass-balance model with time-dependent K-40 decay, branching, argon degassing, transport and escape. Treat equal-mole isotope substitution only as an optional sensitivity control. The previous ~0.930% pressure benchmark demonstrates a gas-inventory effect under declared assumptions, not Ar-40 necessity or provenance.
2. **U-Pb:** Define a low-dimensional mineral initialization generator from independently measured chemistry. Propagate U-238 and U-235 decay chains; model common Pb, inheritance and Pb loss explicitly. Preregister predictions for held-out zircon datasets. The previous short-interval decay calculation is only a mathematical benchmark, not a geochronological explanation.

## Claim and failure ledger

| Claim | Status | What would count against it |
|---|---|---|
| Ordinary post-initialization decay and heat production | Established physics | Contradiction of reproducible measurements |
| Daughter elements participate in Earth systems | Established in selected cases | Case-specific evidence |
| Specific isotopic inventories are functionally constrained | Unproven auxiliary | No independently specified constraint or failed functional prediction |
| Observed isotopic configuration is uniquely necessary | Not asserted | A viable alternative under the same functional criteria |
| A coherent initialized inventory predicts cross-system isotope structure | Central research conjecture | Held-out failure or unconstrained sample-by-sample tuning |
| Functional participation establishes special-creation provenance | Invalid inference | Not a permissible conclusion |

**Research integrity rule:** Failure of an auxiliary does not logically disprove special creation, but it counts against that auxiliary's scientific explanatory adequacy. A model that can reproduce any result by freely selecting initial daughter inventories has not passed the severe test.

## Evidence acquisition requirements
Before numerical validation: archive exact datasets, sample identifiers, measured ratios and uncertainties, calibration standards, mineralogical covariates, disturbance evidence, primary-source citations, and frozen model parameters. Record observations separately from conventional age interpretations and DFM predictions.
