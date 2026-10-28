# Sierra Nevada acquisition and admission audit report

Date: 2026-10-28
Authorization: Principal Operator, main chat, 2026-10-28 02:38 CDT: "Do both" (selecting "Acquire and audit the Sierra Nevada holdout release")
Scope executed: provenance verification, inventory record, data-dictionary inspection, cohort construction attempt, and admission audit only. No fitting, no tuning, no model comparison, no repository commits, and no bridge filings. This release is the designated geological holdout. Nothing in it was used to tune, calibrate, or otherwise inform the Manzano calibration cohort, and this audit preserves that separation.
Release: Langenheim et al. (2025), Tabular uranium-lead and trace-element compositional data of zircons and whole-rock geochemistry of plutonic rocks in the Sierra Nevada, California, USGS, DOI 10.5066/P13LKC5C, ScienceBase item 67d5cd7ed34e1acf3979e1a3, publication date 2025-04-23.

Human-Curated, AI-Enabled (HCAE)

## Outcome summary

| Gate or product | Verdict |
|---|---|
| Acquisition | COMPLETE: 3 of 3 in-scope originals present under canonical names |
| Inventory record (equivalent JSON) | AWAITING_PROVENANCE: all 3 downloaded files PRESENT_UNVERIFIED; 3 attached files NOT_DOWNLOADED with reasons |
| source_provenance.py | VERIFIED: 3 of 3 files |
| Dictionary inspection | DECISIVE AND ADVERSE: the release does not publish the Wetherill pair, any error correlation, or corrected radiogenic ratios |
| Cohort construction | 706 spot analyses carried into the admission table with source values copied and source-silent gate fields left blank; 0 fields fabricated |
| audit_cohort.py | AUDITED_NOT_FROZEN: 0 accepted, 706 rejected |
| Holdout suitability under EMPIRICAL_GATE_v0.2 | INELIGIBLE as delivered; see section 8 for the exact failing fields and the decisions that could change this |
| Empirical freeze or model test | NOT PERFORMED and not authorized by this task |

The one-sentence finding: the Sierra Nevada release is a 207Pb/206Pb and 206Pb/238U dataset with a 207Pb-corrected age product; it contains no 207Pb/235U ratio, no 204Pb measurement, and no published error correlation of any kind, so it cannot populate the gate's Wetherill admission schema, and the missing quantities cannot be derived or inferred under the locked methodological decisions.

Zero admitted is the audit's result, not an audit failure. Every rejection reason below was produced by the admission authority (`audit_cohort.py`) from an admission table in which each source-published value was copied verbatim and each source-silent field was left blank rather than filled by assumption.

## 1. Acquisition and retrieval record

The three in-scope originals were acquired on 2026-10-28 between 07:38 and 07:40 UTC via a live browser session from the official ScienceBase item page:

https://www.sciencebase.gov/catalog/item/67d5cd7ed34e1acf3979e1a3

The item's bot block cleared in a fresh browser environment. No sign-in, payment, or terms click-through was required. The release is a USGS public data release. Direct API access from this VM returns HTTP 403; that access limitation is why the browser route was used.

| File | Size (bytes) | SHA-256 |
|---|---:|---|
| UPb_dates_zircon_trace_elements_final.csv | 206916 | 74f5cd1c65f15cefc6b18ab3a28a01e952c865dbbf3ac8ac3ce94a66dd7fb310 |
| DataDictionary_final.csv | 5047 | 317d6b57c550c609352e5d00c51ceec00c9921c91afc5970ae5a02b03c6f16a5 |
| sierra_igneous_sample_localities_into_review.csv | 8817 | 858e49cb3a8d0342dbfefd22719772012f8e2139db628d68c522015d1772b4b5 |

The originals remain in `originals/` under their canonical names. Their hashes were rechecked after all processing and were unchanged.

### 1.1 File-structure facts established during inspection

- The analytical CSV is not plain UTF-8. It contains 87 non-ASCII bytes, overwhelmingly 0xCA, the Mac OS Roman non-breaking space, used as trailing padding in some column names (for example `Sample_ID`, `Analysis_ID`, `Pb206U238`, `AnalysisType`) and in some Sample_ID values. The dictionary contains the same padding in some attribute names. Inspection and mapping decoded the files as Mac OS Roman and normalized the padding. The original bytes were never modified.
- The analytical file's final line is unterminated, so line counts and CSV record counts differ by one. CSV parsing yields 742 records: 1 header, 706 spot analyses, and 35 per-sample summary records (section 4.6). Any earlier description of this file as "740 analyses" counts lines, not analyses; the table's own structure is 706 spot analyses across 35 samples.
- The locality CSV parses to 94 data rows covering 94 samples; 35 of them are flagged in the locality table itself as zircon U-Pb samples of this study, matching the 35 samples in the analytical table.

### 1.2 Attached files not downloaded

The item's complete attached-file list has six entries. Three were not downloaded:

- `sierra_nevada_geochron_geochem_final.xml`: FGDC metadata record; not required for the admission audit.
- `sndesa-zircons-chemistry.jpg`: map image; not tabular data.
- `sierra_chemistry_2024_final.csv`: whole-rock geochemistry for 93 samples; deliberately out of scope for the zircon U-Pb admission audit.

## 2. Inventory record

`acquisition_inventory.py` was NOT run on this release. It is Manzano-specific: it hardcodes DOI 10.5066/P9U0P2ZY and the three Manzano filenames, so forcing it onto this release would produce a false record. An equivalent inventory record was produced instead at `inventory-record.json`, listing all six attached files with per-file status (PRESENT_UNVERIFIED for the three downloaded files, with sizes and SHA-256 hashes; NOT_DOWNLOADED with reasons for the other three) and the retrieval record. Its overall status uses the same vocabulary as the Manzano tool: AWAITING_PROVENANCE, with the retained note that hashes describe local bytes and do not independently authenticate source provenance.

## 3. Provenance manifest and verification

Manifest: `source-provenance-manifest.json`

`source_provenance.py` is release-agnostic (it verifies a manifest list of doi, source_url, filename, sha256, retrieved_utc, license, source_type entries against a raw directory), so it was used directly, unchanged. Each manifest entry records:

- DOI: 10.5066/P13LKC5C
- Source URL: https://www.sciencebase.gov/catalog/item/67d5cd7ed34e1acf3979e1a3
- Canonical filename
- SHA-256 of the original local bytes
- Retrieved UTC: 2026-10-28 07:38-07:40 UTC
- License/release characterization: USGS public data release
- Source type: Original USGS ScienceBase data file acquired via live browser session

Command interface:

`python source_provenance.py source-provenance-manifest.json originals/`

Verifier verdict:

- Overall status: VERIFIED
- UPb_dates_zircon_trace_elements_final.csv: VERIFIED
- DataDictionary_final.csv: VERIFIED
- sierra_igneous_sample_localities_into_review.csv: VERIFIED

Full output: `provenance-output.json`.

As with the Manzano run, the license/release field is recorded as "USGS public data release" from the retrieval record; no separate formal license identifier was present in the downloaded files. The verifier confirms the manifest field is present and the recorded hashes match the local original bytes; it does not independently validate a formal license identifier.

## 4. Data-dictionary findings (pivotal section)

The dictionary was read in full before the analytical table was mapped. It has 41 lines: a header and 40 field descriptions, all attributed to a table named `UPb_dates_zircon_trace_elements_into_review` (the delivered file is the `_final` variant of the same table; the field inventory matches the delivered header).

### 4.1 Ratios the release actually publishes

The dictionary defines exactly four isotope ratio fields:

- `Pb207Pb206`: "Ratio of 207Pb to 206Pb", range 0.034 to 0.165.
- `Pb208Pb206`: "Ratio of 208Pb to 206Pb", range -0.0746 to 0.5063.
- `Pb206U238`: "Ratio of 206Pb to 238U", range 0.0124 to 0.3672.
- `Pb208Th232`: "Ratio of 208Pb to 232Th", range -0.0016 to 0.1044.

Plus two age products: `Pb207corr_Pb206U238Age`, "207Pb corrected age calculated using ratio of 206Pb to 238U", and `Age`, "Preferred age estimate", a per-sample interpreted age.

No field in the dictionary, and no column in the delivered table, reports a 207Pb/235U ratio, a 238U/206Pb ratio, a 204Pb ratio, or any 235U quantity at all. The string "235" does not occur in either file.

### 4.2 The missing Wetherill coordinate: r75 cannot be populated, and derivation is not justified

The gate schema requires `r75`, the corrected radiogenic 207Pb*/235U ratio, with an absolute 1-sigma uncertainty `sigma75_abs_1s` and the paired-ratio correlation `rho_wetherill` between r68 and r75.

The algebra that might appear to rescue r75 is:

r75 = (207Pb/206Pb) x (206Pb/238U) x (238U/235U)

with 238U/235U a measured physical constant (about 137.818). That identity holds for ratios taken on a common basis. It does not make the derivation admissible here, for three independent reasons, each sufficient:

1. **Basis.** The gate requires corrected radiogenic ratios. The dictionary defines the two published ratios only as "Ratio of 207Pb to 206Pb" and "Ratio of 206Pb to 238U" (the uncertainty field for 207Pb/206Pb calls it the "final ratio"). Neither definition states that the tabulated ratio is common-Pb corrected or radiogenic-only, and the release contains no 204Pb measurement with which a 204Pb correction could be verified or reproduced. Locked decision 5 applies: where corrections are absent or unverified, reject rather than treat corrected ratios as known. A product of two unverified-basis ratios is an unverified-basis ratio.
2. **Uncertainty.** sigma75 by propagation requires the covariance between the 207Pb/206Pb and 206Pb/238U measurements. That covariance is not published (section 4.4). Propagating under an independence assumption is the rho-equals-zero fabrication in another form and is barred by locked decision 1 and by EMPIRICAL_GATE_v0.2 ("Do not silently assume rho=0").
3. **Correlation.** rho_wetherill is a correlation between r68 and r75. Because r75 would itself be a product involving the same 206Pb/238U measurement as r68, its correlation with r68 is structurally dominated by the unpublished covariance in point 2. It cannot be computed from anything the release publishes.

Determination: `r75`, `sigma75_abs_1s`, and `rho_wetherill` are not populatable from this release. No Tera-Wasserburg substitution was made: the gate specifies the Wetherill pair and states that correlation is for the same two ratios, not Tera-Wasserburg correlation, and the release's native pairing (207Pb/206Pb against 206Pb/238U, with a 207Pb-corrected age) is a different formulation that this audit has no authority to substitute.

### 4.3 Uncertainty basis

The dictionary is explicit for the ratios that exist:

- `Pb207Pb206UncPct1s`: "One sigma uncertainty (percent) for final ratio of 207Pb to 206Pb", Units "percent", range 0.5 to 218.
- `Pb206U238UncPct1S`: "One sigma (percent) error for ratio of 206Pb to 238U", Units "percent", range 0.9 to 59.6.
- `Pb208Pb206UncPct1s` and `Pb208Th232UncPct1s`: likewise one sigma, percent.

So the ratio uncertainty basis is relative percent at 1 sigma, and for r68 the conversion used was the same one the Manzano audit used:

- `sigma68_abs_1s = r68 * Pb206U238UncPct1S / 100`

Observed ranges across the 706 spot analyses: r68 0.0124 to 0.3672; percent uncertainty 0.9 to 59.6 percent; converted absolute 1-sigma 0.000131 to 0.009547. This is the one numeric conversion the dictionary justifies. It does not cure the basis problem in section 4.2 point 1: an uncertainty can be converted for a ratio whose radiogenic status is still unverified, which is why `measurement_basis` was left blank rather than asserted as `wetherill_absolute_1sigma`.

Two age uncertainties exist and neither was used: `Pb207corr_Pb206U238AgeUnc1S` (one sigma, Ma, on the 207Pb-corrected age) and `AgeUnc` (two sigma, absolute, on the preferred age). No age or age uncertainty is an admission field.

### 4.4 No error correlation is published

There is no error-correlation, covariance, or rho field in the dictionary or in the delivered table. The only dictionary entries containing "correction" or "correlation"-adjacent language are the 207Pb-corrected age fields. This is the direct contrast with the Manzano release, which publishes `Error_Correlation` for exactly the Wetherill pair.

Consequence under locked decision 1: rho must not be fabricated, inferred, set to zero, or derived from ages. Records from this release therefore cannot enter a two-ratio Wetherill cohort. This single absence, on its own, is sufficient for the audit outcome in section 6.

### 4.5 Common-Pb correction: documented for an age, not for the ratios

The only common-Pb treatment the dictionary documents is embedded in one field name and definition: `Pb207corr_Pb206U238Age`, the "207Pb corrected age calculated using ratio of 206Pb to 238U". A 207Pb correction is a common-Pb correction strategy that estimates and removes common Pb using the measured 207Pb/206Pb under a concordance assumption, applied here to produce an age. The dictionary does not state that the tabulated `Pb206U238` or `Pb207Pb206` ratios are themselves corrected, gives no assumed common-Pb composition, and publishes no 204Pb data. Accordingly:

- `common_pb_method` was left blank in the admission table. Writing "207Pb correction" there would assert that the ratios were so corrected, which the source does not establish.
- `correction_status` was left blank. Asserting `corrected_radiogenic` (the only value the auditor accepts) would misrepresent the ratios.

### 4.6 Analysis IDs, table structure, and grouping

Analytical-table structure (CSV-parsed):

- 741 data records: 706 spot analyses and 35 per-sample summary records.
- Each summary record carries the sample's preferred `Age`, `AgeUnc` (2 sigma), `NofAnalyses`, and `MSWD`, with Analysis_ID and all isotope fields blank. These are interpreted-age summaries, not analyses, and were not carried into the admission table.
- The 706 spot analyses span 35 samples, 13 to 38 spots per sample.
- All 706 spot analyses are zircon, AnalysisType "Spot", one laboratory, one method: Lab_ID "Stanford University-USGS SHRIMP-RG Lab" (705 rows; 1 blank) and InstrumentMethod "SIMS (Ion Microprobe)" (705 rows; 1 blank). The single row blank in Lab_ID, InstrumentMethod, AnalysisType, and SampleMaterial is analysis 19POB046-5.1 (sample 19pob046).
- `AnalysisInc` ("Was the analyses included in the interpreted age?") among spots: Yes 647, No 58, blank 1 (the same 19POB046-5.1 row). As in the Manzano audit, AnalysisInc was NOT used as an admission filter; importing the publication's age-inclusion choice into an admission cohort would be selection.
- Published Analysis_IDs are not unique. There are 693 unique Analysis_IDs among 706 spots. All 13 duplicated IDs occur in sample 20-R-61 (for example 20R61-5.1 appears twice with different ratio values, once AnalysisInc Yes and once No): they are distinct repeat measurements sharing a spot name, not duplicate rows. The auditor flags the 13 later occurrences as `duplicate_analysis_id`. A future use of this table would need a disambiguated analysis key (for example Sample_ID plus Analysis_ID plus occurrence); this audit used the published IDs verbatim so the defect is visible in the auditor's own output rather than silently repaired.

Grouping and the locality table:

- The gate splits by geological unit. This release's unit structure is 35 individual pluton samples across the Sierra Nevada batholith; the locality table gives each sample a lithology (for the 32 cleanly joinable zircon samples: granodiorite 17, diorite 5, monzonite 3, gabbroic diorite 2, quartz monzonite 2, monzogabbro 1, granite 1, granitoid 1) and, for many, a pluton name in the Comment field (for example Coloma pluton, Haypress Creek pluton, Lake Combie Complex, Sugar Pine Mountain pluton). A sample-level split is therefore structurally meaningful: these are independent rock units, not grains of one rock.
- The join is imperfect. Matching Sample_IDs to the locality table's Sample column after whitespace normalization and case folding joins 32 of 35 zircon samples. Three do not join: 18pob55a, 22rcb011b, and 19pl104 (the locality table carries 19pl104a, a suffix variant). Any unit-level freeze using this release must first reconcile those three identifiers against the FGDC metadata or the authors' records.
- Laboratory independence does not hold. The holdout laboratory (Stanford University-USGS SHRIMP-RG Lab) is the same laboratory, and SHRIMP-RG the same instrument family, as the Manzano calibration cohort. A Sierra Nevada holdout would satisfy locked decision 2 through its "independent source / geological unit" clause, not through laboratory independence. Gate 4's "geological unit and analytical laboratory" phrasing should be read with that fact on the record.

The admission table uses the whitespace-normalized Sample_ID as `rock_unit`, `Lab_ID` verbatim as `laboratory`, and `InstrumentMethod` verbatim as `method`.

### 4.7 Dictionary-to-table discrepancies that do not affect the determination

1. The dictionary attributes its fields to a table named `UPb_dates_zircon_trace_elements_into_review`; the delivered analytical file is `UPb_dates_zircon_trace_elements_final.csv`. The field inventory matches the delivered header, so this is a naming-stage artifact of the release, recorded for completeness.
2. Several column and attribute names carry trailing non-breaking-space padding in both files (section 1.1). It affects machine matching only and was normalized in mapping, never in the originals.
3. The dictionary presents `Age`, `AgeUnc`, `NofAnalyses`, and `MSWD` as ordinary columns of the analytical table without noting that in the delivered table they are populated only on the 35 per-sample summary records, not on spot rows.

None of these change any admission field determination.

## 5. Cohort construction

Transformation script: `build_admission_cohort.py` (run locally during the audit; not filed with this evidence)
Mapping and per-field populatability log: `cohort-mapping-log.json`
Admission table: `sierra-nevada-admission-cohort.csv`
Admission table SHA-256: 83532a6793b1c16631bb44846e0f0277f0ad9af6f75ebfecec2e3b0b02f8653d

Construction rule: source values copied verbatim; the single dictionary-justified conversion applied (sigma68); every gate field the source is silent on left blank so the admission authority, not this audit's prose, enumerates the failures. Nothing was derived, inferred, or filled by assumption.

| Admission field | Disposition |
|---|---|
| source_doi | 10.5066/P13LKC5C |
| source_sha256 | SHA-256 of original analytical CSV, 74f5cd1c65f15cefc6b18ab3a28a01e952c865dbbf3ac8ac3ce94a66dd7fb310 |
| analysis_id | Analysis_ID verbatim (whitespace-normalized); published duplicates retained and flagged by the auditor |
| rock_unit | Sample_ID (whitespace-normalized) |
| laboratory | Lab_ID verbatim (1 blank retained) |
| method | InstrumentMethod verbatim (1 blank retained) |
| r68 | Pb206U238 verbatim; radiogenic basis NOT confirmed by the dictionary |
| r75 | BLANK: not published; derivation rejected (section 4.2) |
| sigma68_abs_1s | r68 * Pb206U238UncPct1S / 100 |
| sigma75_abs_1s | BLANK: no r75 and no published covariance |
| rho_wetherill | BLANK: no error correlation published anywhere in the release |
| common_pb_method | BLANK: no correction of the tabulated ratios is documented |
| correction_status | BLANK: corrected_radiogenic cannot be honestly asserted |
| measurement_basis | BLANK: wetherill_absolute_1sigma cannot be asserted without the Wetherill pair |

Counts:

- Records in analytical file: 741 (706 spot analyses, 35 sample-summary records)
- Spot analyses carried into the admission table: 706
- Spot analyses excluded before audit: 0
- Sample-summary records excluded as non-analyses: 35

No concordance-based selection was used. No row was excluded for discordance, age, or AnalysisInc status.

## 6. Admission audit

Command interface, including the checksum guard for the normalized admission table:

`python audit_cohort.py sierra-nevada-admission-cohort.csv --expected-sha256 83532a6793b1c16631bb44846e0f0277f0ad9af6f75ebfecec2e3b0b02f8653d`

Audit output:

- Admission table SHA-256: 83532a6793b1c16631bb44846e0f0277f0ad9af6f75ebfecec2e3b0b02f8653d
- Total: 706
- Accepted: 0
- Rejected: 706
- Status: AUDITED_NOT_FROZEN

Rejection reasons (auditor-produced; a record carries every reason that applies to it):

| Reason | Records |
|---|---:|
| invalid_r75 | 706 |
| invalid_sigma75_abs_1s | 706 |
| invalid_rho_wetherill | 706 |
| missing_common_pb_method | 706 |
| missing_correction_status | 706 |
| not_confirmed_radiogenic_ratios | 706 |
| missing_measurement_basis | 706 |
| unverified_uncertainty_or_ratio_basis | 706 |
| duplicate_analysis_id | 13 |
| missing_laboratory | 1 |
| missing_method | 1 |

Full output: `audit-output.json`.

The eight universal reasons are the schema-level ineligibility of section 4 expressed per record: the Wetherill pair, its correlation, and the confirmed radiogenic basis do not exist in this release. The remaining three reasons are record-level defects in the source itself (13 repeated spot names in sample 20-R-61; one analysis row with blank laboratory and method). Even a schema amendment would have to reckon with those.

## 7. EMPIRICAL_GATE_v0.2 gate-by-gate disposition

1. **Retrieve original bytes and record SHA-256, license, and DOI/version:** Evaluated. Bytes present, DOI and hashes recorded, provenance verification passed. License/release field recorded as "USGS public data release"; no separate formal license identifier was supplied in the files.
2. **Verify column meanings, correction algorithms, sigma level, and covariance orientation:** Evaluated, with an adverse result. Column meanings and the 1-sigma percent basis are verified for the ratios that exist. The correction algorithm for the tabulated ratios is not documented (only a 207Pb-corrected age is), and covariance orientation cannot be verified because no covariance is published. Ambiguity was resolved by rejection at the mapping stage, before any residual analysis (none was performed).
3. **Retain exclusions and counts; no concordance-based cherry-picking:** Evaluated. Counts retained throughout: 741 file records, 35 non-analysis summary records identified, 706 spot analyses carried forward, 0 pre-audit exclusions, 706 audit rejections. AnalysisInc was not used as a filter.
4. **Split by geological unit and laboratory and freeze before fitting:** Not performed (no freeze is meaningful for an ineligible cohort), but the structural facts are established: 35 independent pluton samples support a unit-level split in principle; the laboratory is the same as the calibration cohort's, so independence rests on source and unit, not laboratory; 3 of 35 sample identifiers do not join the locality table and would need reconciliation first.
5. **Independent conventional comparator and symmetric process models:** Not evaluated. Fitting and model comparison are outside this task, and there is no admitted cohort to compare on.
6. **Shared RCI parameters constrained independently of held-out ratios:** Not evaluated. No fitting was performed. The holdout separation was preserved: nothing in this release informed any calibration quantity.
7. **Predictive log-likelihood, calibration, coverage, parameter count, sensitivity, and failed cases:** Not evaluated for model performance. The failed-case counts available at this stage are the admission results: 0 pre-audit exclusions and 706 audit rejections, of which 706 are schema-level and 14 record-level (13 duplicate IDs, 1 blank laboratory/method record).

## 8. Holdout-suitability conclusion and what could change it

**Conclusion: as delivered, the Sierra Nevada release is ineligible as the DFM holdout under EMPIRICAL_GATE_v0.2.** It fails the schema on exactly these fields, for exactly these reasons:

- `r75`: not published; no 207Pb/235U quantity exists in the release.
- `sigma75_abs_1s`: not computable; requires the unpublished 207Pb/206Pb to 206Pb/238U covariance.
- `rho_wetherill`: not published; no error correlation of any kind exists in the release.
- `correction_status` / `common_pb_method`: the tabulated ratios are not documented as common-Pb corrected; the documented 207Pb correction produces an age, not corrected ratios; no 204Pb data exists to verify a correction.
- `measurement_basis`: cannot be `wetherill_absolute_1sigma` without the Wetherill pair.

The following are findings for the Principal Operator to decide. This audit makes none of these changes itself.

1. **Author-level reduced data.** The decisive cure is the underlying SHRIMP-RG reduced data for these same 35 samples from the Stanford-USGS SHRIMP-RG laboratory or the data authors, if it reports 207Pb/235U ratios and the paired-ratio error correlations (the Manzano release proves this laboratory's reporting pipeline can publish exactly that correlation). With those fields, this release's unit structure (35 independent plutons) would make it a strong holdout, subject to identifier reconciliation (section 4.6) and a disambiguated analysis key.
2. **A different holdout release.** A release that, like Manzano, publishes corrected Wetherill ratios with percent 1-sigma uncertainties and a paired-ratio error correlation, from geological units independent of Blue Springs metarhyolite, would satisfy the schema as written. Laboratory independence from Stanford-USGS SHRIMP-RG would additionally satisfy gate 4 on both dimensions.
3. **A schema amendment to a lower-dimensional demonstration.** Locked decision 1 already contemplates treating a covariance-less source "as a lower-dimensional demonstration". A gate amendment admitting a 206Pb/238U-only cohort (r68 with converted absolute 1-sigma) could use this release for ingestion and single-ratio checks. It would still have to resolve the radiogenic-basis question for Pb206U238 (the dictionary does not confirm the ratio is common-Pb corrected) and it could not, by construction, test two-ratio concordia behavior or held-out parity.
4. **A schema amendment to a Tera-Wasserburg formulation.** This release's native coordinates (207Pb/206Pb and 206Pb/238U) are the Tera-Wasserburg pair, so an amendment is conceivable. It would not cure the covariance absence: Tera-Wasserburg fitting with correlated errors needs the error correlation between its two coordinates, which is likewise unpublished here, and the radiogenic-basis question in point 3 remains. An amendment alone does not make this release admissible; it changes which missing quantity is decisive.

What this release CAN support today, without any amendment: byte-level provenance and repeatable ingestion of an official USGS release; a documented, auditor-verified demonstration of the admission gate rejecting a real, high-quality dataset that does not meet the Wetherill schema; and a precisely scoped data request (option 1) whose required fields are now enumerated rather than guessed.

What it cannot support: admission to the empirical cohort, any train/holdout split, any held-out scoring, and any statement about explanatory parity.

## 9. Work products

- `inventory-record.json` (equivalent inventory; acquisition_inventory.py not run, Manzano-specific)
- `source-provenance-manifest.json`
- `provenance-output.json`
- `build_admission_cohort.py` (local only; not filed)
- `cohort-mapping-log.json`
- `sierra-nevada-admission-cohort.csv`
- `audit-output.json`

Originals in `originals/` were rehashed after all processing: unchanged (74f5cd1c..., 317d6b57..., 858e49cb...).

Human-Curated, AI-Enabled (HCAE)
