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

## Verified schema reconnaissance (2026-10-27)

USGS Data Report 1227 (https://doi.org/10.3133/dr1227), published September 2026, documents the Geochron relational schema, CSV exports, QA procedures and data dictionaries. Its Appendix 2 explicitly documents the following candidate analytical fields, **but the appendix says its descriptions are accurate to release 3.0**; the release 4.0 CSV headers and actual non-null coverage must still be checked.

| Field | Meaning / audit implication |
|---|---|
| `pb206u238unc1s`, `pb207u235unc1s` | One-sigma percentage uncertainties; do not treat as absolute or two-sigma |
| `pb206u238unc2s`, `pb207u235unc2s` | Two-sigma percentage uncertainties; harmonize before fitting |
| `rhowetherill` | Correlation coefficient for 206Pb/238U and 207Pb/235U; necessary for joint error ellipse where populated |
| `pb208th232`, `pb208th232unc` | Candidate Th-Pb ratio and two-sigma absolute uncertainty |
| `pb204corrpb206u238` | 204Pb-corrected ratio; correction provenance must be retained |
| `pb206u238corrspikeblankfraction`, `pb207u235corrspikeblankfraction` | Processed ratios with spike/blank/fractionation corrections; **not raw detector signals** |
| `pb206u238corrspikeblankfractiondisequil`, `pb207u235corrspikeblankfractiondisequil` | Also corrected for initial disequilibrium; correction assumptions must be audited |
| `analysis_id` | Laboratory run identifier, potentially useful for grouped dependence and deduplication |

**Caution:** The USGS technical report explicitly notes that its database does not account for uncertainties in decay constants, spike calibrations, or age-value uncertainties in some direct comparisons. These are potential systematic components to address separately, not grounds to dismiss the observations.

**Updated gate:** Prefer the published *analytical ratio* columns with declared correction states, sigma levels, and correlation. Reject an age-only dataset for the forward isotope-ratio comparison. Check field coverage by geological unit and laboratory method before selecting a freeze subset. No unit or sample has been selected and no dataset downloaded, hashed, or frozen.

**Sources:** USGS Geochron v4.0 release (https://doi.org/10.5066/P9RZNPIF); Thomson et al., USGS Data Report 1227 (https://doi.org/10.3133/dr1227).
