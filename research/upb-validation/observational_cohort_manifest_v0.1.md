# DFM U-Pb observational cohort manifest v0.1

Status: Candidate sources only. No sample-level data ingested, no cohort frozen, no observed-data results.

## Preferred primary source
USGS Geochron v4.0, DOI 10.5066/P9RZNPIF, public domain. USGS technical documentation DOI 10.3133/dr1227 specifies U-Pb isotope-ratio and uncertainty fields, including rhowetherill. Filter for zircon, paired 206Pb/238U and 207Pb/235U, explicit uncertainty and covariance, common-Pb treatment, method and sample provenance. Verify actual non-null coverage before selection.

## Independent external candidates
USGS Puerto Rico zircon release DOI 10.5066/P1ZN39XQ, public domain, LA-ICP-MS. Verify availability of paired ratios, uncertainty, correction metadata.
Foley 2021 Mendeley Data DOI 10.17632/98m2db62tk.1, CC BY 4.0, detrital zircon ratios and ages; check covariance and instrument metadata.
Cruz 2025 Zenodo DOI 10.5281/zenodo.16936985, CC BY 4.0, sample DA-07B, only concordant analyses selected by age criterion: use for secondary sensitivity only, not unbiased primary evaluation.
OneDZ 2026 DOI 10.5281/zenodo.19690702, large detrital compilation; inspect raw ratio, covariance and source-provenance completeness before considering.

## Freeze gate
Before fitting, create machine-readable per-sample manifest with DOI, record IDs, instrument, rock unit, lab, original and reduced ratios, 1-sigma uncertainties, correlation, common Pb, exclusion reasons and SHA-256 of exact source bytes. Group by geological unit and lab. Set pilot/train/holdout split and freeze code commit, parameter bounds and metrics. Exclude no observations based on agreement with either hypothesis.

## Immediate blockers
Source data bytes not yet retrieved; no real measurement or model comparison performed. Conventional comparator needs independently checked covariance and common-Pb handling.
