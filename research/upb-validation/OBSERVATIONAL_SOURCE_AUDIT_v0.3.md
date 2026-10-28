# Observational source audit v0.3 (2026-10-28)

**No source data ingested. Cohort NOT FROZEN.** This is a documented admission workflow, not an observational comparison.

## Preferred source
USGS Geochron v4.0, DOI 10.5066/P9RZNPIF. USGS documents a complete downloadable CSV release with metadata and a data dictionary; the technical documentation DOI 10.3133/dr1227 covers the relational schema. A database of published dates does **not** guarantee every row contains both corrected Wetherill ratios and covariance. Inspect the actual column completeness before committing to this source.

## Independent cross-check candidate
USGS Jones (2021), *U-Pb Isotopic Data and Ages of Zircon from the Manzano Mountains, New Mexico*, DOI 10.5066/P9U0P2ZY. The USGS describes a SHRIMP-RG grain-level CSV, a sample summary CSV and a data dictionary CSV. Assess the original table for paired ratios, analytical uncertainties, correction status and ratio correlation; do not infer them from reported ages.

## Source retrieval status
The public USGS catalog pages were inspected, but direct dataset-byte retrieval was unavailable in the execution environment. Therefore no SHA-256 of original raw data, row count, column audit or admission result can be reported. Do not fabricate or approximate these.

## Executable admission check
`python research/upb-validation/audit_cohort.py <normalized_admission.csv> --expected-sha256 <admission_table_sha256>`

The normalized admission table is *derived* from original data; retain original raw bytes, source URL/DOI, source SHA-256, transformation script, and immutable field mapping separately. In the normalized CSV, `source_sha256` must refer to original raw data, not the normalized table. Only explicitly corrected radiogenic Wetherill ratios with absolute 1-sigma uncertainty and same-coordinate correlation can pass. Missing rho is not silently set to zero. Every rejected row retains its reason.

## Freeze rule
Do not freeze or split the cohort until source bytes and original measurement conventions are independently verified. Group by geological unit and laboratory, then predeclare holdout group IDs, code commit and metric definitions. Cross-source or within-group repeated analyses must not leak across train and holdout.

## Next gate
Acquire original source tables using a network-enabled retrieval path, preserve bytes and checksums, map native columns to the admission schema, run the admission audit, inspect rejection counts and select a defensible cohort. No merge/cleanup handoff is warranted until this gate is completed or explicitly deferred.
