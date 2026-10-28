# Manzano acquisition and admission audit report

Date: 2026-10-28
Authorization: Principal Operator, main chat, 2026-10-28 02:27 CDT: "Acquire the Manzano CSVs and run the admission audit"
Scope executed: acquisition record, inventory, provenance verification, data-dictionary inspection, cohort construction, and admission audit only. No fitting, no model comparison, no repository commits, and no bridge filings.
Release: Jones (2020/2021), U-Pb Isotopic Data and Ages of Zircon from the Manzano Mountains, New Mexico, USGS, DOI 10.5066/P9U0P2ZY, ScienceBase item 5f99b6c9d34e198cb786e76d.

Human-Curated, AI-Enabled (HCAE)

## Outcome summary

| Gate or product | Verdict |
|---|---|
| Acquisition | COMPLETE: 3 of 3 originals present under canonical names |
| acquisition_inventory.py | AWAITING_PROVENANCE: all 3 files PRESENT_UNVERIFIED |
| source_provenance.py | VERIFIED: 3 of 3 files |
| Cohort construction | 24 source analyses mapped; 0 excluded before audit |
| audit_cohort.py | AUDITED_NOT_FROZEN: 24 accepted, 0 rejected |
| Empirical freeze or model test | NOT PERFORMED and not authorized by this task |

The pivotal dictionary finding is favorable on covariance: paired-ratio error correlation is published in the source table as `Error_Correlation`. It was not inferred, set to zero, or derived from ages. All 24 values are present and range from 0.40 to 0.97.

Admission is not an empirical result. This is a single-sample, single-rock-unit, single-laboratory cohort. It supports ingestion and calibration work only and cannot by itself support cross-unit held-out parity.

## 1. Acquisition and retrieval record

The three originals were acquired on 2026-10-28 between 07:31 and 07:32 UTC via a live browser session from the official ScienceBase item page:

https://www.sciencebase.gov/catalog/item/5f99b6c9d34e198cb786e76d

The item's bot block cleared in a fresh browser environment. No sign-in, payment, or terms click-through was required. The release is a USGS public data release. Direct API access from this VM remains HTTP 403; that access limitation is why the browser route was used. This acquisition record supersedes the earlier failed-acquisition report where they conflict.

| File | Size (bytes) | SHA-256 |
|---|---:|---|
| geochronology_SHRIMP-RG_manzanoMtns_jones.csv | 8608 | 5fff6ae27388471313004c97d8894dbfd98045699f68fe63461e6a73f7eea4ce |
| geochronology_sampleSummary_manzanoMtns_jones.csv | 416 | 89b04e95b5db51e615b3c521f6252ed02c9c8f973bc0d13b82523086661b6fc0 |
| geochronology_dataDictionary_manzanoMtns_jones.csv | 8749 | 0a22434070f4ab30f69afe957b6ae8b65d7e71ff156d55b1a5c294f474a6cb03 |

The originals remain in `originals/` under their canonical names. Their hashes were rechecked after all processing and were unchanged.

The provenance manifest records the license/release characterization supplied with the retrieval record as "USGS public data release." No separate formal license identifier was present in the three CSVs or supplied in the retrieval record. The provenance tool verifies that the manifest license field is present and that the recorded hashes match the local original bytes; it does not independently validate a formal license identifier.

## 2. Acquisition inventory verdict

Command interface:

`python acquisition_inventory.py originals/`

The script returned:

- Release: manzano
- DOI: 10.5066/P9U0P2ZY
- Overall status: AWAITING_PROVENANCE
- geochronology_SHRIMP-RG_manzanoMtns_jones.csv: PRESENT_UNVERIFIED, 8608 bytes, SHA-256 5fff6ae27388471313004c97d8894dbfd98045699f68fe63461e6a73f7eea4ce
- geochronology_sampleSummary_manzanoMtns_jones.csv: PRESENT_UNVERIFIED, 416 bytes, SHA-256 89b04e95b5db51e615b3c521f6252ed02c9c8f973bc0d13b82523086661b6fc0
- geochronology_dataDictionary_manzanoMtns_jones.csv: PRESENT_UNVERIFIED, 8749 bytes, SHA-256 0a22434070f4ab30f69afe957b6ae8b65d7e71ff156d55b1a5c294f474a6cb03

Full output: `inventory-output.json`.

The script's own note is retained: "Hashes describe local bytes; they do not independently authenticate source provenance."

### Inventory interface difference

The all-present state in `acquisition_inventory.py` is `AWAITING_PROVENANCE`, not `COMPLETE`. The script has no COMPLETE status. It checks canonical file presence and computes local hashes; provenance comparison is the separate job of `source_provenance.py`.

## 3. Provenance manifest and verification

Manifest: `source-provenance-manifest.json`

Each manifest entry records:

- DOI: 10.5066/P9U0P2ZY
- Source URL: https://www.sciencebase.gov/catalog/item/5f99b6c9d34e198cb786e76d
- Canonical filename
- SHA-256 of the original local bytes
- Retrieved UTC: 2026-10-28 07:31-07:32 UTC
- License/release characterization: USGS public data release
- Source type: Original USGS ScienceBase data file acquired via live browser session

Command interface:

`python source_provenance.py source-provenance-manifest.json originals/`

Verifier verdict:

- Overall status: VERIFIED
- geochronology_SHRIMP-RG_manzanoMtns_jones.csv: VERIFIED
- geochronology_sampleSummary_manzanoMtns_jones.csv: VERIFIED
- geochronology_dataDictionary_manzanoMtns_jones.csv: VERIFIED

Full output: `provenance-output.json`.

## 4. Data-dictionary findings

The dictionary was read before mapping. It has 69 lines: a header and 68 field descriptions. The analytical table has 24 data rows. The sample-summary table has one data row.

### 4.1 Ratio columns

The decisive dictionary entries are:

- `204Pbcorr_206Pb_238U_Ratio`: "204Pb-corrected ratio of 206Pb to 238U."
- `204Pbcorr_207Pb_235U_Ratio`: "204Pb-corrected ratio of 207Pb to 235U."

Accordingly:

- `r68` maps to `204Pbcorr_206Pb_238U_Ratio`.
- `r75` maps to `204Pbcorr_207Pb_235U_Ratio`.

Observed source ranges:

- r68: 0.2351 to 0.2990
- r75: 3.14 to 3.97

No total, uncorrected ratio was substituted for either target ratio.

### 4.2 Uncertainty basis

The decisive dictionary entries are:

- `204Pbcorr_206Pb_238U_Ratio_Unc_1sig_perc`: "Uncertainty (1-sigma) on 204Pb-corrected ratio of 206Pb to 238U, in percent", Units "%".
- `204Pbcorr_207Pb_235U_Ratio_Unc_1sig_perc`: "Uncertainty (1-sigma) on 204Pb-corrected ratio of 207Pb to 235U, in percent", Units "%".

Therefore the analytical ratio uncertainties are relative percent uncertainties at 1 sigma. They are not absolute uncertainties and not 2-sigma uncertainties. The only conversion used was:

- `sigma68_abs_1s = r68 * 204Pbcorr_206Pb_238U_Ratio_Unc_1sig_perc / 100`
- `sigma75_abs_1s = r75 * 204Pbcorr_207Pb_235U_Ratio_Unc_1sig_perc / 100`

Observed ranges:

- Source percent uncertainty for r68: 1.45 to 2.78 percent
- Converted absolute 1-sigma for r68: 0.0037816 to 0.00788686
- Source percent uncertainty for r75: 1.55 to 4.08 percent
- Converted absolute 1-sigma for r75: 0.0527 to 0.151776

The sample summary's separate `UPb_Age_Unc_Ma` is described in the dictionary as a 2-sigma age uncertainty. No age or age uncertainty was mapped into the cohort, so that 2-sigma field has no effect on this audit.

### 4.3 Wetherill paired-ratio correlation

The dictionary entry for `Error_Correlation` is decisive and is quoted verbatim:

"Error correlation of the 207Pb/235U and 206Pb/238U ratios."

This is the paired-ratio correlation for the two target Wetherill coordinates, not a Tera-Wasserburg correlation and not a quantity derived from ages. In the analytical table, the field follows the two 204Pb-corrected ratio and uncertainty field pairs. All 24 analyses have a nonblank numeric value. The observed range is 0.40 to 0.97.

Consequence: the anticipated no-covariance blocker does not occur for admission of this release. `rho_wetherill` maps directly to the published `Error_Correlation`. No rho was fabricated, inferred, set to zero, or reconstructed from reported ages.

### 4.4 Common-Pb correction and correction status

The selected ratio fields are explicitly named with the `204Pbcorr_` prefix, and their dictionary descriptions call them "204Pb-corrected" ratios. The cohort therefore records:

- `common_pb_method`: "204Pb correction"
- `correction_status`: "corrected_radiogenic"

There is no separate per-row source column named correction status. That status is encoded from the selected 204Pb-corrected ratio fields, not copied from a status field. This distinction is retained here so the transformation is auditable.

The source also contains `comm_206Pb_perc`, described as "207Pb corrected common 206Pb, in percent". That field was not used as the correction method for the two selected Wetherill ratios and was not used in the cohort.

### 4.5 Analysis IDs and grouping

Analytical-table findings:

- All 24 rows have Sample `K05ABO1R`.
- All 24 rows are zircon.
- All 24 rows use Mount `AJJ46`.
- `Analysis_Spot` has 24 unique values.
- `AnalysisSpot_Mount` has 24 unique values.
- The dictionary defines `AnalysisSpot_Mount` as "Concatenation of Analysis_Spot and Mount."
- `analysis_id` maps to `AnalysisSpot_Mount`.

Sample-summary findings:

- Sample: K05-ABO-1r
- Rock_Class: metamorphic
- Rock_Type: metarhyolite
- Rock_Comment: Blue Springs metarhyolite
- Analysis_Type: U-Pb zircon
- Analysis_Lab: Stanford-USGS SHRIMP-RG
- Analysis_Method: SHRIMP U-Pb
- Total grains analyzed: 24

The analytical sample code `K05ABO1R` and summary sample code `K05-ABO-1r` match after removing punctuation and normalizing case. The cohort uses the summary's `Rock_Comment` as `rock_unit`, `Analysis_Lab` as `laboratory`, and `Analysis_Method` as `method`.

### 4.6 Dictionary-to-table discrepancies that do not affect mapping

Two descriptive discrepancies were found:

1. The dictionary describes a sample-summary field `Lab_Sample`, but the actual sample-summary CSV header does not contain `Lab_Sample`.
2. The dictionary describes analytical fields `Nb_ppm` and `Pr_ppm`, but the actual analytical CSV header does not contain either field.

Neither discrepancy affects a mapped admission field. They are recorded because the dictionary is not a perfectly exact header inventory for the delivered tables.

## 5. Cohort construction

Transformation script: `build_admission_cohort.py` (run locally during the audit; not filed with this evidence)
Mapping and per-record log: `cohort-mapping-log.json`
Cohort: `manzano-admission-cohort.csv`
Cohort SHA-256: 8bf4ebbea63ea2c99f9304bc66e0f54b5912a029438b3dbe50de4cae259f9b65

### 5.1 Field mapping

| Admission field | Source or rule |
|---|---|
| source_doi | 10.5066/P9U0P2ZY |
| source_sha256 | SHA-256 of original analytical CSV, 5fff6ae27388471313004c97d8894dbfd98045699f68fe63461e6a73f7eea4ce |
| analysis_id | AnalysisSpot_Mount |
| rock_unit | Sample-summary Rock_Comment |
| laboratory | Sample-summary Analysis_Lab |
| method | Sample-summary Analysis_Method |
| r68 | 204Pbcorr_206Pb_238U_Ratio |
| r75 | 204Pbcorr_207Pb_235U_Ratio |
| sigma68_abs_1s | r68 * source percent uncertainty / 100 |
| sigma75_abs_1s | r75 * source percent uncertainty / 100 |
| rho_wetherill | Error_Correlation, copied directly |
| common_pb_method | 204Pb correction |
| correction_status | corrected_radiogenic |
| measurement_basis | wetherill_absolute_1sigma after conversion |

### 5.2 Counts and selection discipline

- Source analytical rows: 24
- Rows mapped to cohort: 24
- Rows excluded before audit: 0
- Unique analysis IDs in cohort: 24

All relevant ratio, uncertainty, correlation, and ID fields were nonblank for all 24 rows.

No concordance-based selection was used. `Percent_Discordant` was not used to include or exclude any row. The source column `Interpreted_Age_Included` also was not used as an admission criterion: 23 rows have value Y and one row, K05ABO1R-5.1_AJJ46, has value N. That N row was retained and admitted. This preserves the source's full analytical set rather than importing the publication's sample-age inclusion choice into the admission cohort.

## 6. Admission audit

Command interface, including the checksum guard for the normalized cohort:

`python audit_cohort.py manzano-admission-cohort.csv --expected-sha256 8bf4ebbea63ea2c99f9304bc66e0f54b5912a029438b3dbe50de4cae259f9b65`

Audit output:

- Admission table SHA-256: 8bf4ebbea63ea2c99f9304bc66e0f54b5912a029438b3dbe50de4cae259f9b65
- Total: 24
- Accepted: 24
- Rejected: 0
- Rejection reasons: none; the returned `rejection_reasons` object is empty
- Rejections: none; the returned `rejections` list is empty
- Status: AUDITED_NOT_FROZEN

Full output: `audit-output.json`.

Accepted analysis IDs:

K05ABO1R-5.1_AJJ46, K05ABO1R-7.1_AJJ46, K05ABO1R-2.1_AJJ46, K05ABO1R-17.1_AJJ46, K05ABO1R-9.1_AJJ46, K05ABO1R-24.1_AJJ46, K05ABO1R-11.1_AJJ46, K05ABO1R-15.1_AJJ46, K05ABO1R-10.1_AJJ46, K05ABO1R-6.1_AJJ46, K05ABO1R-22.1_AJJ46, K05ABO1R-21.1_AJJ46, K05ABO1R-16.1_AJJ46, K05ABO1R-1.1_AJJ46, K05ABO1R-18.1_AJJ46, K05ABO1R-4.1_AJJ46, K05ABO1R-3.1_AJJ46, K05ABO1R-14.1_AJJ46, K05ABO1R-13.1_AJJ46, K05ABO1R-19.1_AJJ46, K05ABO1R-8.1_AJJ46, K05ABO1R-12.1_AJJ46, K05ABO1R-20.1_AJJ46, K05ABO1R-23.1_AJJ46.

### Audit interface and enforcement limits

The `--expected-sha256` value for `audit_cohort.py` is the SHA-256 of the normalized admission table, not the SHA-256 of the original analytical CSV. The cohort's separate `source_sha256` field correctly carries the original analytical-file hash.

The audit script checks that required text fields are nonempty, numeric fields are finite, ratios are nonnegative, uncertainties are positive, rho is strictly between -1 and 1, `correction_status` is exactly `corrected_radiogenic`, and `measurement_basis` is exactly `wetherill_absolute_1sigma`. It does not independently verify that the DOI is the Manzano DOI, that `source_sha256` equals the provenance-verified analytical-file hash, that the laboratory and rock-unit strings came from the summary, or that rho was actually published. Those links were established by the provenance and dictionary steps in this run.

## 7. EMPIRICAL_GATE_v0.2 gate-by-gate disposition

1. **Retrieve original bytes and record SHA-256, license, and DOI/version:** Evaluated for admission. The original bytes are present, the DOI and hashes are recorded, and provenance verification passed. The license/release field is recorded as "USGS public data release" from the retrieval record; no separate formal license identifier was supplied.
2. **Verify column meanings, correction algorithms, sigma level, and covariance orientation:** Evaluated. The dictionary establishes 204Pb-corrected Wetherill ratios, percent 1-sigma uncertainties, and published paired-ratio error correlation.
3. **Retain exclusions and counts; no concordance-based cherry-picking:** Evaluated. There were no pre-audit exclusions and no audit rejections. All 24 source analyses were retained.
4. **Split by geological unit and laboratory and freeze before fitting:** Not evaluated and not satisfiable as a cross-unit split from this cohort alone. There is one sample, one rock unit, and one laboratory. No split or freeze was performed.
5. **Independent conventional comparator and symmetric process models:** Not evaluated. Fitting and model comparison are outside this task.
6. **Shared RCI parameters constrained independently of held-out ratios:** Not evaluated. No fitting was performed, and this cohort has no independent geological holdout.
7. **Predictive log-likelihood, calibration, coverage, parameter count, sensitivity, and failed cases:** Not evaluated for model performance. The only failed-case count available at this stage is the admission result: 0 pre-audit exclusions and 0 audit rejections.

## 8. Standing conclusion

The Manzano cohort is admitted but not frozen. Its correct status is the audit script's status, `AUDITED_NOT_FROZEN`.

What it can support:

- Byte-level provenance and repeatable ingestion of the official Manzano release.
- Admission-schema validation using measured corrected Wetherill ratios, absolute 1-sigma uncertainties converted from published percent values, and published paired-ratio error correlations.
- Calibration-oriented work that is explicitly confined to this sample and laboratory.

What it cannot support:

- Cross-unit held-out parity.
- A train/holdout split based on independent geological units or laboratories.
- Any empirical claim that radiogenic initialization has achieved explanatory parity.

All 24 analyses come from one sample, Blue Springs metarhyolite, one mount, and one laboratory and method: Stanford-USGS SHRIMP-RG, SHRIMP U-Pb. Splitting individual grains from this one rock into training and holdout sets would leak the same geological and analytical group across both sides and would violate the locked grouping decision.

The published `Error_Correlation` removes the expected covariance obstacle for a two-ratio Manzano admission cohort. It does not remove the independent-holdout obstacle. A defensible empirical phase still requires at least one independently sourced geological unit, preferably from a distinct release and laboratory where available, followed by provenance verification, dictionary inspection, admission audit, group freeze, parameter freeze, and only then fitting and comparator evaluation. Those later steps are outside this report's executed scope.

## 9. Work products

- `inventory-output.json`
- `source-provenance-manifest.json`
- `provenance-output.json`
- `build_admission_cohort.py` (local only; not filed)
- `cohort-mapping-log.json`
- `manzano-admission-cohort.csv`
- `audit-output.json`

`sciencebase-item.json` is retained from the earlier failed direct-API attempt and contains the 25-byte HTTP 403 response body. It is not source data and was not used in provenance, mapping, or audit.

Human-Curated, AI-Enabled (HCAE)
