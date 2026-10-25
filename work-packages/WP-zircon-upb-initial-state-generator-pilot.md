# Zircon U-Pb Initial-State Generator: Preregistered Pilot Protocol

**DFM | 2026-10-25 | Study design only; no results or successful fit claimed**

## Research question
Can one independently constrained constitutive initialization model predict joint U-Pb isotope measurements across held-out zircon grains at least as well as a conventional geological-history model, without per-grain target-age tuning?

## Dataset shortlist (verified public metadata; files not yet ingested)
1. **Primary candidate:** Kirkland et al., *Full zircon U-Pb geochronology data*, Maniitsoq, Greenland, Figshare (2021), CC0, 1.52 MB, https://springernature.figshare.com/articles/dataset/Full_zircon_U-Pb_geochronology_data/14178392. A regional collection with full per-analysis data; verify columns, uncertainties, sample grouping, common-Pb correction, and raw versus reduced ratios after acquisition.
2. **Secondary:** Foley, *U-Pb Isotopic Ratios and Ages*, Mendeley Data (2021), CC BY 4.0, DOI 10.17632/98m2db62tk.1, https://data.mendeley.com/datasets/98m2db62tk.1. Workbook advertises raw-data sheet; verify what 'raw' means analytically.
3. **Replication:** USGS Sierra Nevada zircon U-Pb plus trace-element CSV dataset, https://catalog.data.gov/dataset/tabular-uranium-lead-and-trace-element-compositional-data-of-zircons-and-whole-rock-geoche ; and Geochron https://www.geochron.org/gettingdata (XLS/XML).
4. **External generalization only:** global zircon U-Th-Pb database https://zenodo.org/records/8303076; compilation-level ages may not supply sufficient raw ratios/covariances for the primary mechanistic test.

## Data audit gate
Before any fitting, inventory sample_id, grain_id, spot_id, lithology, analytical method, measured 206Pb/238U and 207Pb/235U or 207Pb/206Pb, 204Pb/common-Pb correction, 1-sigma uncertainties and error correlations, U concentration, discordance, images/zoning, provenance and analytical quality flags. Explicitly classify reported ages as derived, not independent observables. If raw/reduced ratios or covariance are missing, restrict claims accordingly; do not manufacture data.

## Mathematical baseline
Let x_i=(206Pb*/238U)_i, y_i=(207Pb*/235U)_i be corrected radiogenic ratios, and t_i conventional age:
x_i=exp(lambda238 t_i)-1; y_i=exp(lambda235 t_i)-1, with correlated measurement uncertainty.
Conventional geological model M0 allows geologically justified distinct crystallization events and documented common-Pb/open-system histories, not a strawman single-age fit.

A constitutive model M1 must specify **before holdout** a common generator G(theta, c_i), where theta are global parameters and c_i are independently measured sample covariates (e.g., U abundance, geochemical class, source reservoir). Predict observed ratios by physical mass balance and post-boundary actual processes. Do not feed measured apparent age or target daughter ratio back as c_i. Model initialized daughter fractions with nonnegative abundances and isotope mass balance. The mere assertion that G exists is not a prediction.

## Model families and identifiability
- M0: Conventional crystallization/closure ages, common Pb, and documented disturbances.
- M1a: One common initial Pb isotope reservoir plus actual subsequent decay and independently specified geological events.
- M1b: Small-number reservoir classes with class membership established from non-age covariates.
- M1c: Explicit physical generative mechanism with a priori parameter bounds and forward isotope predictions.
- M2: Real extraordinary transformations, separately energy-accounted and not silently conflated with M1.

**Important null:** A sufficiently flexible initial-state model can fit any dataset and therefore has no evidentiary value. Require finite-dimensional shared parameters and complexity penalties.

## Train/validation/holdout
- Group split by rock sample or locality, never randomly split analytical spots from the same grain between training and test.
- Lock a test set before model selection; choose an external dataset for replication.
- Reproduce published M0 dates and uncertainties first.
- Fit M1 global parameters on training only; evaluate predictive joint log likelihood, uncertainty calibration, isotope concordance, outlier sensitivity, and physical residuals on held-out groups.
- Report parameter counts, priors, identifiability and a negative-control shuffled-covariate test.
- Check whether the model predicts discordance, common-Pb signals, inherited cores and geological event ordering, not just a marginal histogram of apparent ages.

## Decision rules
- **Not viable:** requires separate initial daughter adjustments per zircon or fails mass balance/physical positivity.
- **Unresolved:** matches held-out ratios but cannot distinguish from ordinary initial-common-Pb treatment, or lacks event-level predictions.
- **Provisionally competitive:** predicts multiple held-out isotope systems and geological constraints with comparable uncertainty calibration and independent shared parameters.
- **Empirically progressive:** additionally predicts genuinely new data or anomalies not used to specify the generator, then survives independent replication.

No conclusion about Earth's absolute historical age follows from a dataset's fit alone. Strong performance against a weak baseline is insufficient.

## Immediate execution checklist
1. Download the small CC0 Maniitsoq data table; inspect actual columns and metadata.
2. Record SHA256, original citation, analytical method and transformations.
3. Determine whether paired raw ratios and their covariance exist.
4. Build reproducible M0 concordia reproduction with documented uncertainty treatment.
5. Draft one constrained G(theta,c) candidate *before* inspecting held-out measurements.
6. Run grouped holdout and independent dataset replication.

## Governance
Research-only pilot. PDAIH/Day One exegetical reconciliation remains paused. No edits to programme hard core, parent Christian Designism registry or formal position statement.
