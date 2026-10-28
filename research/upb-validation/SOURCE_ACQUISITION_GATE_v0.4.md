# Original observation acquisition gate v0.4 (2026-10-28)

**State: BLOCKED ON ORIGINAL SOURCE BYTES.** No empirical zircon ratios have been retrieved or admitted. No observational model comparison has been conducted.

## Verified discovery

- Jones, USGS Manzano Mountains zircon release: https://doi.org/10.5066/P9U0P2ZY. USGS explicitly identifies `geochronology_SHRIMP-RG_manzanoMtns_jones.csv`, `geochronology_sampleSummary_manzanoMtns_jones.csv`, and `geochronology_dataDictionary_manzanoMtns_jones.csv`. These are *candidate* files, not yet obtained.
- USGS Geochron v4: https://doi.org/10.5066/P9RZNPIF. Large standardized alternative; may not expose paired covariance for every analysis.
- USGS technical documentation: https://doi.org/10.3133/dr1227 (2026).

## Retrieval and admission contract

1. Retrieve source files directly from the DOI-linked USGS release using a network-enabled environment; retain original bytes unchanged.
2. Record for each original file `doi`, exact `source_url`, local `filename`, computed SHA-256, actual `retrieved_utc`, `license`, and `source_type` in a JSON list. Do **not** use the example test timestamp as an actual retrieval timestamp.
3. Run `python research/upb-validation/source_provenance.py manifest.json raw_dir/`. Only `VERIFIED` files advance.
4. Inspect original data dictionary; establish actual column semantics, ratio coordinate system, uncertainty level and units, common-Pb correction, and analytical covariance. Do not derive missing rho from unrelated reported ages.
5. Write a versioned, auditable transformation to normalized admission CSV. Run `audit_cohort.py` with checksum guard; preserve all rejected records and reasons.
6. Freeze calibration and holdout groups by geological unit and lab *before* fitting. If no usable paired-ratio covariance exists, select another published dataset or explicitly downgrade the study to a limited univariate demonstration; do not assert a full two-ratio validation.

## Scientific discriminator

Initial daughter parameters must be constrained across independent samples, with predeclared complexity penalties. If a free daughter ratio is fitted separately per grain, the RCI fit is non-identifying and must not count as evidence for explanatory parity.

## Integration gate

Merge/cleanup handoff remains **NOT READY** until original measurements are acquired and admitted, or the principal explicitly authorizes a scoped infrastructure-only integration with the observational gate left open.
