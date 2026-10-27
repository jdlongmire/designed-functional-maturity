# RCIM-006: Alternative U-Th-Pb Dataset Candidates and Parallel Work

**Date:** 2026-10-27. **Status:** Source reconnaissance; no downloaded or frozen observational records.
**Parent:** RCIM-004 PEP pilot; RCIM-005 Geochron access gate.

## Ranked candidates

1. **USGS Western Alaska Range LASS zircon data**, Todd and Kylander-Clark (2023), DOI https://doi.org/10.5066/P9HE4U9N. Describes U, Th, 206/207/208Pb, 235/238U, 232Th ratios and Lu-Hf isotope data on related aliquots. Best initial *cross-system* candidate, subject to actual columns, uncertainty/correlation completeness, specimen grouping, and data retrieval.
2. **USGS Manzano Mountains zircon SHRIMP-RG**, Jones (2020/2021), DOI https://doi.org/10.5066/P9U0P2ZY. Identifies a specific analytical CSV (`geochronology_SHRIMP-RG_manzanoMtns_jones.csv`), sample-summary CSV and data dictionary. Small, tractable U-Pb methods pilot; may be unsuitable for geological-unit holdout because it describes a single metamorphic-rock sample.
3. **Wu, Fang and Ji (2023) global zircon compilation v2.1**, https://zenodo.org/records/8303076, DOI https://doi.org/10.5281/zenodo.8303076. Public archive lists three large XLSX partitions plus reference index and explicitly includes 206Pb/238U, 207Pb/235U, 207Pb/206Pb and 208Pb/232Th ratios with errors. Heterogeneous literature aggregation; use as external robustness corpus, not first controlled pilot.
4. **OneDZ (Li et al., 2026)**, https://doi.org/10.5281/zenodo.19690702, with expert-verified U-Pb subset and CSV exports. Candidate independent U-Pb holdout corpus; confirm actual uncertainty, covariance and overlap with training sources before use.

## Data selection rules

- Favor a **small primary-source study** with measured ratios, uncertainty/covariance, correction provenance, sample identifiers, and a meaningful geological-unit split over a massive aggregated age-only corpus.
- Keep source-derived **ages out of DFM initial-state parameterization**; use analytical ratios and their uncertainties.
- Do not mistake 208Pb measurements for proof that a usable 208Pb/232Th ratio and uncertainty are present. Verify both.
- Group train/holdout by geological unit or specimen, and keep overlapping publications/measurements together.
- Record source URLs, immutable versions, SHA-256, row counts, missingness and laboratory calibration before any freeze.
- If no source supplies required Th-Pb ratios, declare the initial pilot **U-Pb only**.

## Parallel, independently actionable work

**Synthetic Track A benchmark:** Construct a shared initial reservoir vector and explicit mineral partition operator, then propagate through ordinary decay with declared intermediate-chain states. Test conservation, identifiability and sensitivity using *synthetic* observations whose generating parameters are known. Never claim this establishes empirical parity.

**Nuclear validation:** Resolve extreme-stiffness numerical diagnostics, then populate U-238, U-235 and Th-232 branching/energy inputs from versioned evaluated nuclear sources. Do not assign unverified heat energies.

**Observational Track B:** Retrieve a primary-source CSV, audit field completeness, freeze a grouped holdout and specified conventional comparator, then score independently.

## Decision

**The Geochron bulk archive is not a hard blocker.** Any adequately documented primary-source dataset may satisfy the observational gate. The actual requirement is reproducible measured isotope evidence and a constrained comparative protocol. No parity verdict is currently supported.

## Source references

- https://www.usgs.gov/data/u-pb-ages-hafnium-isotope-ratios-and-trace-element-concentrations-laser-ablation-split-stream
- https://www.usgs.gov/data/u-pb-isotopic-data-and-ages-zircon-manzano-mountains-new-mexico
- https://zenodo.org/records/8303076
- https://essd.copernicus.org/articles/18/3671/2026/
