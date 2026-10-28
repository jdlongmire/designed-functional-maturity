# Observational acquisition decision v0.5 — 2026-10-28

## Verified primary record

Jones (2020/2021), *U-Pb Isotopic Data and Ages of Zircon from the Manzano Mountains, New Mexico*, USGS, DOI https://doi.org/10.5066/P9U0P2ZY. Official landing page: https://www.usgs.gov/data/u-pb-isotopic-data-and-ages-zircon-manzano-mountains-new-mexico . It names the raw SHRIMP-RG analytical table, sample summary, and data dictionary:

- `geochronology_SHRIMP-RG_manzanoMtns_jones.csv`
- `geochronology_sampleSummary_manzanoMtns_jones.csv`
- `geochronology_dataDictionary_manzanoMtns_jones.csv`

The DOI resolves to ScienceBase item `5f99b6c9d34e198cb786e76d`, but the available web retrieval fails at the ScienceBase redirect. A direct network request from the local execution container also fails DNS resolution. **No source CSV bytes were acquired, no checksums computed, and no measurements admitted.**

## Independent fallback cohort

Langenheim et al. (2025), USGS Sierra Nevada zircon and whole-rock release, DOI https://doi.org/10.5066/P13LKC5C . Official catalog: https://data.usgs.gov/datacatalog/data/USGS%3A67d5cd7ed34e1acf3979e1a3 . This describes zircon U-Pb analyses from 35 samples, with a separate whole-rock geochemistry table. Prefer as a **distinct geological holdout**, not a second source for tuning Manzano initialization parameters. Admission requires actual ratios, uncertainties, analytical correlation, common-Pb provenance and sample grouping to be inspected; public catalog metadata alone do not establish their presence.

## Locked methodological decisions (before data acquisition)

1. **No inferred covariance.** If the published measurements lack Wetherill paired-ratio correlation, do not fabricate rho=0 or infer it from ages. Treat as a lower-dimensional demonstration or seek an alternative source.
2. **No random grain-level leakage.** Split by geological unit or independent source, not individual spots within one rock. The single-rock Manzano release is suitable for ingestion/calibration checks but cannot alone establish cross-unit held-out parity.
3. **No circular fitting.** Fit shared initialization parameters only to calibration material; freeze before scoring a distinct geological holdout. A freely chosen daughter intercept per grain is inadmissible.
4. **Preserve raw data.** Original bytes and data dictionary must be stored with source URL, retrieval time, SHA-256, and license before normalization.
5. **Common-Pb and disequilibrium are not optional scientific assumptions.** Where corrections or uncertainties are absent, downgrade or reject rather than treat corrected ratios as known.
6. **Independent comparator.** Run conventional concordia and appropriate Pb-loss/common-Pb alternatives with the same accepted measurements and error model; penalize additional parameters in RCI.

## Next operational action

Acquire the three named Manzano CSVs from the DOI-linked ScienceBase release in a network-enabled environment. Then run `source_provenance.py` and `audit_cohort.py`, record rejection reasons, and assess the Sierra Nevada release for a held-out unit. If acquisition remains blocked, a scoped **infrastructure-only** integration may be requested, explicitly excluding empirical-validation claims.

**Integration handoff: NOT READY** under the existing research-completion criterion.
