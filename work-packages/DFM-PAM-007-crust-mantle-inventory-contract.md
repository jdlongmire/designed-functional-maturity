# DFM-PAM-007: Crust/Mantle Inventory Calibration Contract

**Status:** Reservoir modeling implemented; empirical calibration not complete. **Parent:** DFM-PAM-006.

## Executable scope
`research/rcim/track_a_reservoir_inventory.py` accepts separate named reservoirs, their masses, present-day elemental U/Th concentrations in ppb, and K in ppm. It converts to approximate parent isotope masses, reverses ordinary decay over a stipulated elapsed interval, and computes present radiogenic power plus integrated post-boundary energy. Named low/base/high scenarios can be supplied; no scenario values are silently invented or asserted as measured.

## Required source evidence for each reservoir
- Mass and geometry (continental crust, oceanic crust, lithospheric mantle, convecting mantle); cite source and uncertainty.
- U, Th, K abundance and covariance; distinguish sampled crust from indirectly inferred mantle.
- Natural isotope abundance and atomic-mass conversion, including K-40's small natural fraction.
- Nuclear decay constants, branching fractions, deposited heat and neutrino losses.
- Geoneutrino constraints and the extent of model dependence.
- Surface heat flow and nonradiogenic contributions; thermal response requires an independent transport model.

## Current cautions
The code uses approximate present-day atom fractions as mass fractions, neglecting small isotope mass differences. U-234 is omitted. U/Th secular-equilibrium assumptions and K-40 effective heat coefficient remain unvalidated. These approximations must be revised before interpreting TW estimates as empirical. The code's back-propagation of *present-day* isotope inventories is a boundary arithmetic operation, not an empirical proof of initial inventories.

## Acceptance gates
1. Validate heat per decay chain and K-40 branch accounting with evaluated nuclear data.
2. Introduce a cited dataset for each reservoir with uncertainty bounds and correlations.
3. Run sensitivity analyses with all major reservoirs and report a TW range.
4. Compare that range against published radiogenic estimates and global surface heat flow **without equating the two**.
5. Document what independent thermal history and U-Pb constraints remain unmet.

**Current appraisal:** Reusable reservoir accounting is now specified; Earth-wide radiogenic heat and DFM thermal plausibility remain uncalibrated.
