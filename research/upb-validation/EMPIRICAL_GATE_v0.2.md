# U-Pb observational gate v0.2

**State: NOT FROZEN.** No observed ratios have been retrieved, ingested, fitted or compared. All executable tests currently use synthetic inputs.

## Input schema (one analysis per record)
`source_doi,source_sha256,analysis_id,rock_unit,laboratory,method,r68,r75,sigma68_abs_1s,sigma75_abs_1s,rho_wetherill,common_pb_method,correction_status,measurement_basis`.
`r68` and `r75` mean corrected radiogenic 206Pb*/238U and 207Pb*/235U ratios. Uncertainty must be absolute 1-sigma; percentages and 2-sigma reported by sources must be converted with recorded provenance. Correlation is for the *same two ratios*, not Tera-Wasserburg correlation. Do not silently assume rho=0. Source-specific analytical covariance and shared systematic uncertainties require separate handling.

## Admission gates
1. Retrieve original public dataset bytes, record SHA-256, license and DOI/version.
2. Verify original column meanings, correction algorithms, 1-sigma vs 2-sigma, and covariance orientation. Reject ambiguous rows *before* looking at model residuals.
3. Retain exclusions and counts; no concordance-based cherry-picking in the primary cohort.
4. Split by geological unit and analytical laboratory, not random grains. Freeze source checksums, train/holdout group IDs, initialization parameter bounds and evaluation code commit before fitting.
5. Independent comparator: standard Wetherill concordia age and correlated-residual likelihood; later common-Pb/disequilibrium/Pb-loss treatments must be modeled symmetrically.
6. RCI parameters must be shared across predeclared geological/mineralogical groups, constrained independently of held-out ratios; no per-grain initial Pb free parameters.
7. Report predictive log-likelihood, calibration, coverage, parameter count, sensitivity and failed cases. Failure to distinguish RCI from conventional chronology is **not** evidence of empirical parity.

## Current implementation boundary
`upb_covariance.py` evaluates a *single* corrected two-ratio observation and finds its bounded best-fitting age for **fixed** initial ratios. This is a computational building block, not a geological chronology fit or a test of initial provenance. Shared systematic errors, common Pb, chain disequilibrium, Pb loss and multi-grain hierarchy are not yet modeled. The next step is to obtain source data and perform the admission audit.
