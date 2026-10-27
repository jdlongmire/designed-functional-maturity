# DFM-PAM-003: Coupled U-Pb and Radiogenic Heat Plausibility Gate

**Status:** Analytical model specification; no empirical validation. **Parent:** DFM-PAM-002 and RCIM-002.

## Coupling principle
A coherent initialization may contain parent U-238/U-235 and stable daughter Pb-206/Pb-207 inventories. Subsequent ordinary decay increases daughter inventories and generates radiogenic heat from the parent chains. Stable lead daughter atoms do not themselves generate radiogenic heat. Therefore initial daughter inventories need not entail the heat that would have been released had those daughters formed through ordinary post-boundary decay. This is a conditional accounting distinction, not independent evidence that the inventories were initialized.

## Analytical baseline
The executable `research/rcim/track_a_upb_heat.py` includes:
- Closed-system evolution for each U parent and its corresponding stable daughter.
- Initial radiogenic daughter inventory as an explicit parameter.
- Parent-decay-based heat power and integrated heat under an approximate secular-equilibrium assumption.
- Algebraic inversion showing why arbitrary initial daughters can fit target isotope ratios, explicitly disallowed as evidential support.
- Self-tests for conservation and decay half-lives. Execution and source-parameter validation remain outstanding.

## Plausibility obligations
1. **Nuclide accounting:** Include parent isotope abundances, initial radiogenic Pb, common Pb, and mineral-specific partitioning; obey mass and atom conservation post-boundary.
2. **Thermal accounting:** Calculate U, Th, K heat sources, neutrino losses, chain disequilibrium, transport, conduction, convection, surface heat flow, and thermal boundary conditions. A per-nuclide heat calculation is not a global thermal model.
3. **Mineral consistency:** Explain U-Pb paired-chain concordance, discordance, mineral growth and Pb loss without sample-specific initial-state tuning.
4. **Time-dependent history:** Specify whether mineral grains were initialized mature, subsequently crystallized, inherited, or altered; test consistency with independent observations.
5. **Geological context:** Account for thermal metamorphism, mineral closure, geological ordering and known-age events.
6. **Auxiliary parity:** Compare against actual conventional common-Pb, inheritance and open-system reconstructions with the same documentation standards.

## Current conditional result
The mathematical distinction between pre-existing stable daughter inventories and post-boundary heat release is coherent under stipulated initialization. It does **not** establish a physically constrained Earth-wide initial state, observed U-Pb concordance, or a satisfactory global heat budget. Track A remains **not yet established quantitatively**.

## Next gate
Run the code and verify decay constants and heat-per-chain values against authoritative references. Then add Th/K parent heat, isotope abundance, crust/mantle inventories, heat transport and measured heat-flow bounds. Independently parameterize mineral Pb distributions before comparing measured zircon ratios.
