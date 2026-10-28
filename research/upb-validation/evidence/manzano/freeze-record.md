# Manzano cohort freeze record

Date: 2026-10-28
Cohort: Jones Manzano Mountains U-Pb release (admission cohort v0.1)
Companion evidence: this directory (audit-report.md, source-provenance-manifest.json, provenance-output.json, inventory-output.json, manzano-admission-cohort.csv, audit-output.json, cohort-mapping-log.json, originals/)

Human-Curated, AI-Enabled (HCAE)

## Cohort identification

- Source release: Jones (2020/2021), U-Pb Isotopic Data and Ages of Zircon from the Manzano Mountains, New Mexico, USGS.
- DOI: 10.5066/P9U0P2ZY (ScienceBase item 5f99b6c9d34e198cb786e76d).
- Sample: K05-ABO-1r, Blue Springs metarhyolite (one sample, 24 zircon analyses).
- Laboratory: Stanford-USGS SHRIMP-RG. Method: SHRIMP U-Pb.
- Ratios admitted: 204Pb-corrected 206Pb/238U and 207Pb/235U (Wetherill pair), uncertainties published as percent 1-sigma and converted to absolute 1-sigma with the conversion recorded in cohort-mapping-log.json. Paired-ratio error correlation is published in the source as Error_Correlation (range 0.40 to 0.97); no correlation was inferred, set to zero, or derived from ages.

## Declared role

CALIBRATION AND INGESTION ONLY. This cohort is not a held-out parity test and no result from it, alone, can support a plausible explanatory parity (PEP) claim.

## Admission result and freeze status

- Admission audit (audit_cohort.py): 24 of 24 analyses admitted, 0 rejected. Full output in audit-output.json.
- Status transition: with this filing, the Manzano cohort moves from AUDITED_NOT_FROZEN to FROZEN at the cohort level. The checksums below, the cohort file, and the declared role are fixed as of this record.
- The overall empirical gate status remains NOT FROZEN. This record freezes the Manzano cohort only; it does not freeze the evaluation, any parameter bounds, or any holdout.

## Frozen checksums (SHA-256)

Originals (byte-pristine, in originals/):
- geochronology_SHRIMP-RG_manzanoMtns_jones.csv: 5fff6ae27388471313004c97d8894dbfd98045699f68fe63461e6a73f7eea4ce
- geochronology_sampleSummary_manzanoMtns_jones.csv: 89b04e95b5db51e615b3c521f6252ed02c9c8f973bc0d13b82523086661b6fc0
- geochronology_dataDictionary_manzanoMtns_jones.csv: 0a22434070f4ab30f69afe957b6ae8b65d7e71ff156d55b1a5c294f474a6cb03

Normalized admission cohort:
- manzano-admission-cohort.csv: 8bf4ebbea63ea2c99f9304bc66e0f54b5912a029438b3dbe50de4cae259f9b65

## Retrieval and provenance record

Acquired 2026-10-28 between 07:31 and 07:32 UTC via a live browser session from the official ScienceBase item page (https://www.sciencebase.gov/catalog/item/5f99b6c9d34e198cb786e76d), after direct API access from the acquisition environment returned HTTP 403; the browser route was used for that reason. No sign-in, payment, or terms click-through was required. The release is a USGS public data release. Provenance verification (source_provenance.py against source-provenance-manifest.json): VERIFIED, 3 of 3 files. Full record in audit-report.md sections 1 and 2.

## Group structure

One geological unit (Blue Springs metarhyolite), one sample, one laboratory, one method. No internal train/holdout split is permitted on this cohort; splitting single-rock, single-laboratory analyses into train and test partitions would violate the grouped-split rule in DFM_UPb_Validation_Protocol_v0.1.md and EMPIRICAL_GATE_v0.2.md (split by geological unit and laboratory, not random grains).

## Holdout designation

The designated independent holdout is the Sierra Nevada zircon release (Langenheim et al. 2025, USGS, DOI 10.5066/P13LKC5C). It is pending its own acquisition and admission audit. It must never be used to tune this cohort's calibration parameters; parameters are fit on calibration material, frozen, and only then scored against the holdout.

## Evaluation code reference

The evaluation and admission tooling referenced by this record is the upb-validation package as integrated into this repository at master commit 85e779b374efb6449c7e5b60065fc407dfe617ad (research/upb-validation/: acquisition_inventory.py, source_provenance.py, audit_cohort.py, upb_baseline.py, upb_covariance.py, DFM_UPb_Validation_Protocol_v0.1.md, EMPIRICAL_GATE_v0.2.md). Any change to that code after this record requires the evaluation predeclare step to re-pin the code commit before fitting.

## Parameter bounds statement

Initialization parameter bounds are NOT yet frozen. Neither DFM_UPb_Validation_Protocol_v0.1.md nor EMPIRICAL_GATE_v0.2.md declares numeric initialization parameter bounds. Both documents require bounds to be frozen before fitting (protocol, Preregistration and splits: freeze "model parameter priors/bounds and primary metrics before examining test outcomes"; gate item 4: freeze "initialization parameter bounds and evaluation code commit before fitting"). No numeric bounds are recorded here because none exist to record. No fitting is authorized until bounds are declared and frozen in the evaluation predeclare step.

## Standing caveats

- No empirical PEP is claimed. Admission of a calibration cohort is not an empirical result.
- Synthetic benchmarks in this program are software checks, not measured isotope evidence.
- Failure to distinguish the RCI model from conventional chronology is not evidence of empirical parity (EMPIRICAL_GATE_v0.2.md item 7).
- Partition coefficients and other illustrative parameters elsewhere in this program remain illustrative, not calibrated.

Human-Curated, AI-Enabled (HCAE)
