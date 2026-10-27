# DFM-PAM-011: BSE Crust/Mantle Partition Conservation Gate

**Status:** Parameterized partition model added; empirical fractions not selected.

## Method
`research/rcim/track_a_bse_partition.py` takes published BSE U/Th/K element masses from one named scenario and a separately specified crust fraction for each element. It assigns the remainder to mantle. It verifies element-by-element mass conservation and equality of combined radiogenic power to the original BSE scenario.

## Essential epistemic boundary
The partition is algebraic. A mathematically conserved split does not identify the actual crust or mantle composition. Fractions must be derived from independently sourced lithosphere/crust inventories and the selected BSE model, with their correlations and uncertainties. BSE includes crust and mantle, so adding independent crust power to BSE total would double-count.

## Acceptance
- Specify crust reservoir geometry, mass, and sampled versus inferred U/Th/K abundances.
- Preserve the selected BSE scenario's totals and uncertainty covariance.
- Document mantle as residual inference rather than directly measured concentration.
- Compare geoneutrino source-location constraints and terrestrial heat flow separately.
- Do not interpret a source-power partition as a full thermal transport solution or as evidence of initialized daughter inventories.

**Current status:** Conservation logic implemented; Earth-reservoir calibration and DFM Track A thermal plausibility remain open.
