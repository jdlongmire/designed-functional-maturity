# DFM-PAM-012: Published BSE–Continental-Crust Residual Inventory

**Status:** Empirical literature-input mass balance implemented; coefficients and statistical uncertainty treatment remain provisional.

## Source and units
Lyubetskaya and Korenaga (2007), *Chemical composition of Earth's primitive mantle and its variance: 2. Implications for global geodynamics*, **Table 2**, https://doi.org/10.1029/2005JB004224. Published elemental inventories are in **grams**; the code converts to kilograms. The paper presents two alternative BSE models alongside a common continental-crust inventory.

| Element | Continental crust (kg) | McDonough–Sun BSE (kg) | Lyubetskaya–Korenaga BSE (kg) |
|---|---:|---:|---:|
| U | (3.1 ± 0.9) × 10^16 | (8.2 ± 1.7) × 10^16 | (7.0 ± 1.2) × 10^16 |
| Th | (1.32 ± 0.40) × 10^17 | (3.23 ± 0.48) × 10^17 | (2.54 ± 0.43) × 10^17 |
| K | (3.5 ± 1.1) × 10^20 | (9.8 ± 1.9) × 10^20 | (7.7 ± 1.6) × 10^20 |

## Implementation
`research/rcim/track_a_published_reservoir_balance.py` calculates BSE power, continental-crust power, and residual power, all from the same published inventory table and a common elemental coefficient set. It enforces mass and power conservation. It reports interval-arithmetic envelopes by subtracting marginal uncertainty bounds. **These are conservative mathematical envelopes, not confidence intervals**: the original uncertainties have correlations, and the two BSE models are alternative hypotheses rather than independent samples.

The residual **must not be labeled mantle-only**: it includes oceanic crust and any other unmodeled silicate reservoir. Independent oceanic crust inventories are required before deriving a strict mantle residual.

## Interpretation and limitations
The underlying paper discusses continental crust radiogenic power of approximately 5–10 TW and model-dependent mantle power; this calculation is a consistency check, not an independent measurement of those quantities. It does not certify the independently imported elemental heat coefficients or the prototype full-chain nuclear constants. It does not demonstrate historical duration, initialized daughter inventories, or thermal transport adequacy.

## Next gates
1. Execute code and inspect numerical results/CI.
2. Reconcile isotope-decay and elemental heat coefficients against evaluated nuclear decay data.
3. Separate oceanic crust from mantle using sourced, consistent inventories.
4. Carry covariance or explicitly bounded correlated scenarios through source power.
5. Test heat-flow, geoneutrino and mineral-system constraints independently.
