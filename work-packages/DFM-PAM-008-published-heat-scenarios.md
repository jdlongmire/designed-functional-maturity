# DFM-PAM-008: Published Heat-Power Scenarios and Calibration Boundaries

**Date:** 2026-10-27. **Status:** Literature-grounded benchmark comparison, not a validated Earth-reservoir isotope-mass fit. **Parent:** DFM-PAM-007.

## Source-grounded benchmark scenarios
| Scenario | Radiogenic power (TW) | Surface flux (TW) | What it represents |
|---|---:|---:|---|
| Geochemical low/mid/high range | 10 / 20 / 30 | 47 ± 2 | Range of published radiogenic model predictions; NOT one confidence interval |
| Combined KamLAND + Borexino inference | 20.8 (+7.3/-7.9) | 47 ± 2 | Geoneutrino-derived radiogenic power using lithosphere and mantle assumptions |
| Borexino-only inference | 38.2 (+13.6/-12.7) | 47 ± 2 | Alternative experimental inference with differing assumptions and substantial uncertainty |

**References:** Davies and Davies (2010), https://doi.org/10.5194/se-1-5-2010; Strati, Mantovani and Bellini (2023/2026 proceedings), https://doi.org/10.1393/gdf/i2023-10525-4; Borexino Collaboration (2020), https://borex.lngs.infn.it/papers/articles/comprehensive-geoneutrino-analysis-with-borexino/; McDonough (TAUP2025), https://indico-cdex.ep.tsinghua.edu.cn/event/175/contributions/2543/.

## Independent compositional anchors
The published Geoneutrinos.org model interface displays a BSE preset U = 20 ng/g, Th = 80 ng/g, K = 240 microgram/g, with model total radiogenic power 19.5 TW; it also displays mantle preset U = 11 ng/g, Th = 40 ng/g, K = 230 microgram/g. These are **model presets, not direct measurements**. Source: https://geoneutrinos.org/model/.

A geoneutrino review compiles continental-crust models: one bulk continental crust estimate U = 1.3 microgram/g, Th = 5.6 microgram/g, K = 15,000 microgram/g, with modeled crust radiogenic power 7.2 TW. These are inferred reservoir averages, not directly measured whole-crust compositions. Source: https://indico.phys.hawaii.edu/event/2411/attachments/3950/4990/McDonough_Watanabe_AGU_book2023.pdf.

**Do not** mix BSE bulk concentrations with mantle-only mass, or double-count crust. To run the repository reservoir model quantitatively, independently document reservoir mass, geometry, elemental compositions, correlations, and exclusion of the core. BSE encompasses silicate mantle plus crust.

## Heat-flow arithmetic, not secular cooling inference
At 47 TW surface flux, model scenarios 10, 20, 30, and 38.2 TW yield differences of 37, 27, 17, and 8.8 TW respectively. These are **net residuals in a simplified instantaneous energy balance**, not direct measurements of Earth's secular cooling, and not a historical temperature trajectory. Sources and uncertainties are correlated and are not combined here into a statistical posterior.

## Nuclear constant validation status
- The repository's isotope heat-per-decay coefficients have **not** been verified against an evaluated, branch-complete decay dataset. Do not present reservoir-model TW outputs as calibrated.
- K-40's approximate 0.65 MeV effective heat-per-decay is particularly sensitive to branching and neutrino-energy accounting. The model's value remains provisional.
- A published 2025 crust study gives *elemental* present-day specific heat-production coefficients U 98.29, Th 26.18 and K 0.00339 microW/kg of element; this supports an independent implementation route after unit reconciliation. Source: https://www.nature.com/articles/s41561-025-01820-2.

## Track A implications
1. Present-day radioactive power is a physical constraint on any DFM initialized-state model. Initialization of stable daughter inventories does not remove ongoing parent decay.
2. These published ranges do not discriminate DFM from a conventional deep-time history by themselves: both must account for present-day source power and transport.
3. Thermal-history plausibility requires initial thermal energy, crust/mantle heat exchange, surface loss, spatial gradients, and geological thermal observations, not only source accounting.
4. Source-model variation must not be mislabeled as measurement error or used to manufacture evidential parity.
5. **Status:** Literature benchmark comparison established; Earth-specific reservoir fit and nuclear-data verification remain open.

## Next acceptance gate
Implement a second, *elemental specific-power* calculation with traceable units, then compare against the decay-chain method after resolving nuclear constants. Enter mass/abundance inputs from one internally consistent published Earth model, not a patchwork of incompatible reservoirs.
