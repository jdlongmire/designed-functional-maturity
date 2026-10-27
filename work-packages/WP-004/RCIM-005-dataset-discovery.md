# RCIM-005: U-Th-Pb Data Source Discovery and Freeze Gate

**Date:** 2026-10-27. **Status:** Source candidates identified; dataset NOT frozen; no fit executed.
**Parent:** [RCIM-004](RCIM-004-pep-u-th-pb-pilot.md).

## Primary candidate: USGS Geochron v4.0
- Data release: https://www.usgs.gov/data/usgs-geochron-a-database-geochronological-and-thermochronological-dates-and-data-ver-40-may
- DOI: https://doi.org/10.5066/P9RZNPIF
- Technical dictionary: https://pubs.usgs.gov/publication/dr1227/full
- Rationale: published U-Th-Pb analytical information, sample identifiers, uncertainties, metadata, and source citations; versioned USGS release.
- Unverified for selected pilot subset: completeness of raw measured ratios, error covariance, common-Pb treatment, mineral identity, and availability of independent event controls.

## Secondary candidate: Global zircon U-Th-Pb compilation (Wu et al., 2023)
- Article: https://essd.copernicus.org/articles/15/5171/2023/essd-15-5171-2023.html
- Data: https://doi.org/10.5281/zenodo.7387566
- Rationale: approximately two million compiled records, useful for geographic and analytical-method robustness checks.
- Risks: literature aggregation, duplicated/overlapping samples, sampling bias, heterogeneous calibration and uncertainty conventions. Do not substitute published age fields for measured isotope ratios.

## Freeze checklist (all required before empirical scoring)
- [ ] Download a specific immutable version and record archive URL, date, checksum, license, and file names.
- [ ] Verify zircon identification, specimen/unit identifiers, measured 206Pb/238U and 207Pb/235U (or equivalent independent ratios), uncertainties, correlation where available, and common-Pb corrections.
- [ ] Verify Th-Pb measurements are actually present in the selected subset; otherwise label the first pilot **U-Pb only** and reserve Th-Pb as an extension.
- [ ] Document whether entries are raw signals, reduced ratios, or model-derived ages; preserve processing provenance.
- [ ] Select geological units without using apparent ages as DFM initial-state inputs.
- [ ] Freeze inclusion/exclusion criteria and grouped train/holdout units before model fitting.
- [ ] Specify the conventional comparator and its common-Pb/discordance auxiliaries using the same selected data.
- [ ] Publish a manifest and machine-readable dataset audit; record missing fields and exclusion counts.

## Epistemic safeguard
This discovery step establishes access to candidate evidence, **not** empirical adequacy or plausible explanatory parity. The first comparative score remains blocked pending data freeze, evaluated decay-chain inputs, and a common initial-state generator.
