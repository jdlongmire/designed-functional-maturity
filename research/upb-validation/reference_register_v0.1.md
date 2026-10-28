# DFM U-Pb reference-data and calibration register v0.1
Date: 2026-10-28. Status: candidate sources verified by source pages; no observational cohort frozen.

| ID | Source | Role | Verified facts | Limitations / next action |
|---|---|---|---|---|
| NUC-01 | Jaffey et al. (1971), DOI 10.1103/PhysRevC.4.1889 | Original U half-life measurements | U-238: (4.4683 ± 0.0024) Ga; U-235: (0.70381 ± 0.00048) Ga; stated errors statistical | Distinguish statistical from systematic uncertainties; do not use quoted precision as total budget |
| NUC-02 | IUPAC-IUGS TGIG, DOI 10.1515/pac-2021-1202 | Recommended U-238 uncertainty | U-238: (4.4683 ± 0.0096) Ga, k=2; lambda238 (1.55125 ± 0.00333)e-10 yr^-1, k=2 | Paper does not endorse unambiguous consensus for U-235; define sensitivity cases |
| DATA-01 | Geochron, https://www.geochron.org/gettingdata | Candidate measured aliquot data | Public HTML/XLS/XML export and REST API; public data generally CC BY 4.0 | Identify individual downloadable zircon records with raw isotope ratios, uncertainties, covariance, metadata and corrections |
| DATA-02 | USGS Geochron, https://www.usgs.gov/centers/geosciences-and-environmental-change-science-center/science/usgs-geochron-database-usgs | Alternate measured data cohort | Public standardized geochronological database | Check per-record raw ratios, uncertainty covariance, common Pb, tracer/calibration and closure history |
| DATA-03 | Global zircon U-Th-Pb dataset, DOI 10.5281/zenodo.7387567 | Screening/reference catalog | Includes age fields, uncertainties, lithology and publication links | Files currently restricted; ages alone insufficient for primary ratio-space validation; not primary cohort |
| CAL-01 | IsoplotR, https://github.com/pvermees/IsoplotR | Independent comparator | Implements U-Pb concordia and several common-Pb correction methods | Pin version and correction mode; validate independent calculations before comparison |
| METH-01 | GSA Bulletin, Recommendations for reporting and interpretation of isotope dilution U-Pb geochronological information | Reporting and uncertainty practice | Highlights decay-constant uncertainty and isotope-dilution conventions | Obtain DOI/full methods; record interlaboratory systematic uncertainties |

## Data eligibility and leakage controls
- Unit of holdout: geological sample / analytical session / publication, not random individual spots from one zircon.
- Require measured 206Pb/238U and 207Pb/235U ratios or losslessly reconstructible isotope quantities, with 1σ errors and covariance/correlation or a documented conservative sensitivity analysis.
- Retain common-Pb correction method, measured 204Pb where available, U isotope ratio assumption, tracer, instrument, standard, and evidence of open-system behavior.
- Exclude or flag metamict, inherited, discordant, or Pb-loss grains by preregistered criteria; report exclusion counts and a sensitivity analysis retaining flagged data.
- Freeze source version, sample IDs, extraction time, license, file SHA-256, transform script and calibration/held-out assignment before fitting.
- Do not use a dataset containing only derived ages as if it were independent isotope ratio measurements.

## Cohort selection decision
No cohort is frozen. Preferred first cohort: Geochron zircon U-Pb with analyte-level isotope ratios and covariance, selected by published quality/metadata completeness criteria, then a held-out cohort from distinct publication(s). If unavailable, pivot to a published supplementary raw-ratio dataset. Do not fabricate observations.

## Model-identifiability gate
For a single closed sample, x206=a206+exp(lambda238*t)-1 and x207=a207+exp(lambda235*t)-1. Two observed ratios cannot uniquely identify t,a206,a207. Shared initial-state parameters, independent mineralogical constraints and held-out predictions are necessary; report parameter-count and prior sensitivity.

## Sources
https://doi.org/10.1103/PhysRevC.4.1889
https://doi.org/10.1515/pac-2021-1202
https://www.geochron.org/policies
https://www.geochron.org/gettingdata
https://www.usgs.gov/centers/geosciences-and-environmental-change-science-center/science/usgs-geochron-database-usgs
https://zenodo.org/records/7387567
https://github.com/pvermees/IsoplotR

## 2026-10-28 candidate update
- USGS Geochron v4.0, DOI 10.5066/P9RZNPIF, and schema report DOI 10.3133/dr1227 are preferred primary source and dictionary; inspect record-level ratio/covariance completeness before admission.
- USGS Puerto Rico zircon release DOI 10.5066/P1ZN39XQ is an independent candidate.
- Foley (2021), DOI 10.17632/98m2db62tk.1, is a CC BY 4.0 independent candidate.
- Cruz (2025), DOI 10.5281/zenodo.16936985, prefilters for concordance and is therefore only a secondary sensitivity cohort.
- OneDZ (2026), DOI 10.5281/zenodo.19690702, is a candidate broad catalogue; verify underlying ratio/covariance fields and source provenance.
