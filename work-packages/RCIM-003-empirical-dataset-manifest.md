# RCIM-003: Empirical Dataset Acquisition Manifest

**Status:** Candidate sources identified; no source data imported or analyzed. **Date:** 2026-10-27.
**Parent:** RCIM-002.

## Primary acquisition target
**USGS Manzano Mountains zircon U-Pb release**
- DOI: https://doi.org/10.5066/P9U0P2ZY
- Landing page: https://www.usgs.gov/data/u-pb-isotopic-data-and-ages-zircon-manzano-mountains-new-mexico
- Reported files: `geochronology_SHRIMP-RG_manzanoMtns_jones.csv` (grain-level isotopic measurements), `geochronology_sampleSummary_manzanoMtns_jones.csv` (sample context), `geochronology_dataDictionary_manzanoMtns_jones.csv` (field definitions).
- Selection rationale: grain-level U/Pb ratios, Th/U and trace-element context, documented analytical technique, public-domain USGS release.
- **Verification outstanding:** download and inspect the actual files; confirm raw vs corrected ratios, units, uncertainties, covariance, common-Pb treatment, spot-to-grain mapping, and any publication-specific corrections.
- **Use:** initial ingestion/schema exercise and physics benchmark. A single geological body is insufficient for a credible generalizable held-out test.

## Independent candidate
**USGS Graphite Creek, Alaska, U-Pb and supporting measurements**
- Landing page: https://catalog.data.gov/dataset/data-for-uranium-lead-geochronology-carbon-and-sulfur-stable-isotopes-and-raman-spectrosco
- Includes zircon numerical tables, sample descriptions and plots. Confirm direct dataset landing URL and file access before importing.
- **Use:** candidate out-of-source validation after method compatibility and geological-context review.

## Additional cross-system candidate
**EarthChem, Dou and Wang (2026), Zhongchuan composite pluton**
- DOI: https://doi.org/10.60520/IEDA/114380
- Landing page: https://ecl.earthchem.org/view.php?id=4380
- Lists downloadable zircon U-Pb, Hf isotope, trace-element, Raman and bulk-rock datasets.
- **Use:** candidate U-Pb/Hf coupled-system challenge, subject to schema, uncertainty and provenance checks.

## Explicitly deferred
**EarthChem Botero et al. Zimbabwe craton datasets** DOI 10.60520/IEDA/114246 and methods DOI 10.60520/IEDA/114268. The repository pages state data availability begins 2026-12-31; do not claim the data have been acquired as of 2026-10-27.

## Acquisition acceptance criteria
1. Download original files and record immutable checksums, retrieval date, licensing, DOI, publication and measurement method.
2. Preserve unmodified source files separately from derived tables. No inferred ages used as input predictors.
3. Map each observation to sample ID, spot/grain ID, mineral, isotopic ratios, uncertainty definition, corrections, and source row.
4. Explicitly distinguish raw instrument ratios, corrected ratios, and calculated radiogenic ratios; preserve all available variants.
5. Mark absent common-Pb corrections, covariance or sample metadata as missing; do not synthesize them.
6. Validate decay model using known published standards and independently documented post-initialization events.
7. Define train/holdout splits by independent geological groups. Do not claim a holdout if only one group is available.
8. Freeze DFM generator and functional constraints *before* using target isotopic observations for model selection.

## Gate status
- Public candidate source discovery: **complete**.
- Source-file acquisition and checksum: **not completed**.
- Data dictionary inspection: **not completed**.
- Raw measurement normalization: **not completed**.
- Reproducible forward-code execution: **not completed**.
- Constrained DFM generator: **not yet specified quantitatively**.
- Empirical validation: **not started**.

**Research integrity:** Candidate identification is not data ingestion, and ordinary-decay reproduction is not evidence of functional initialization.
