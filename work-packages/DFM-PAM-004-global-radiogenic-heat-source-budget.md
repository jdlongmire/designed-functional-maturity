# DFM-PAM-004: Four-Isotope Radiogenic Heat Source Budget

**Status:** Parameterized analytical prototype; not a calibrated global Earth model. **Parent:** DFM-PAM-003.

## Scope
`research/rcim/track_a_global_heat.py` models ordinary post-boundary decay heat from U-238, U-235, Th-232 and K-40. Inputs are initial isotope masses, not measured terrestrial abundances. It reports power at elapsed time and cumulative heat released since initialization. It includes a deliberately minimal one-box energy balance to expose the dependence on heat capacity and outward heat transport. No empirical crust/mantle inventory, surface heat-flow map, spatial transport solver or initial Earth temperature has been calibrated.

## Boundary interpretation
The model permits an initialized stable daughter inventory without charging its hypothetical pre-boundary radiogenic heat to the post-boundary budget. This is a stipulated creation-boundary condition, not a demonstrated geological event. Heat from *actual* post-boundary decay of radioactive parents remains mandatory. Present radiogenic power cannot by itself determine initial thermal state, surface heat flow or integrated cooling.

## Numerical limitations and next validation
- Half-lives and chain energies are approximate; validate against evaluated nuclear data.
- U/Th chain energy estimates assume approximate secular equilibrium and local energy deposition; daughter-chain disequilibrium and energy escape require refinement.
- K-40 heat uses a simplified branch-weighted average; explicit beta-minus, electron capture, neutrino and gamma contributions are needed for precision.
- Parent masses must distinguish initial from present, and K-40 from total potassium by isotope abundance.
- A lumped thermal box cannot resolve mantle convection, crustal heat production, hydrothermal circulation or geological metamorphic patterns.
- Source-budget self-tests are included but are not equivalent to empirical validation.

## Track A matrix

| Requirement | Implemented | Outstanding |
|---|---|---|
| Ordinary U/Th/K decay | Four-parent analytical expressions | Validated constants and decay-chain treatment |
| Post-boundary integrated heat | Yes, parameterized | Earth-specific initial parent masses |
| Initialized stable daughters | Conceptual separation | Independently constrained daughter distribution |
| Thermal response | One-box sensitivity equation | Crust/mantle spatial model and boundary conditions |
| Present terrestrial heat flow | Not calibrated | Measured regional and global heat-flow bounds |
| Geological thermal evidence | Not assessed | Mineral closure, metamorphic and magmatic history |
| U-Pb concordance coupling | Separate prototype | Shared mineral-scale isotope and heat model |

**Assessment:** An ordinary-decay heat source budget is mathematically tractable under the DFM boundary stipulation. Whole-Earth thermal plausibility is **not yet established**.

## Next gate
Validate constants, execute tests, introduce published crust/mantle heat-producing-element inventories and observed heat-flow constraints, then couple to mineral-scale U-Pb cases. Apply the Auxiliary Hypothesis Parity Principle to conventional thermal reconstructions and DFM initial-state alternatives.
