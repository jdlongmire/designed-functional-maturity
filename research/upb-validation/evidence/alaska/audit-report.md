# Western Alaska Range acquisition and admission audit report

Date: 2026-10-28
Authorization: Principal Operator, 2026-10-28: "Both" (including the holdout search, under its stated rule that a candidate passing the dictionary screen receives the full admission audit)
Scope executed: inventory record, provenance verification, data-dictionary inspection, subset-rule declaration, cohort construction, admission audit, and holdout-suitability assessment only. No fitting, no tuning, no model comparison, no repository commits, and no bridge filings. This release is a designated-holdout candidate. Nothing in it was used to tune, calibrate, or otherwise inform the Manzano calibration cohort, and this audit preserves that separation.
Release: Jones et al. (2020), U-Pb Isotopic Data and Ages of Zircon and Titanite from the Western Alaska Range, Northern Aleutian Range, Taylor Mountains, and Tikchik Mountains Regions, Alaska, USGS, DOI 10.5066/P9K5NFKN, ScienceBase item 5f163a1282cef313ed81a191, publication date 2020-07-21.

Human-Curated, AI-Enabled (HCAE)

## Outcome summary

| Gate or product | Verdict |
|---|---|
| Acquisition | COMPLETE: 3 of 3 in-scope originals present under canonical names |
| Inventory record (equivalent JSON) | AWAITING_PROVENANCE: all 3 downloaded files PRESENT_UNVERIFIED; 5 attached files NOT_DOWNLOADED with reasons |
| source_provenance.py | VERIFIED: 3 of 3 files |
| Dictionary screen | PASSED: 204Pb-corrected Wetherill pair and published paired-ratio Error_Correlation, the Manzano template family |
| Subset rule (declared from summary metadata) | 851 of 1344 table rows in scope; 493 excluded by rule, grouped by reason |
| Cohort construction | 851 analyses mapped from 65 bedrock samples; 0 excluded after the rule |
| audit_cohort.py | AUDITED_NOT_FROZEN: 846 accepted, 5 rejected |
| Holdout suitability under EMPIRICAL_GATE_v0.2 | ELIGIBLE as the designated holdout, subject to the freeze decisions in section 8; independence rests on geological unit and source, not laboratory |
| Empirical freeze or model test | NOT PERFORMED and not authorized by this task |

The one-sentence finding: unlike the Sierra Nevada release, this release publishes the full corrected Wetherill pair with percent 1-sigma uncertainties and a populated paired-ratio error correlation, and after a methodological (non-concordance) subset to bedrock zircon crystallization analyses, 846 of 851 mapped analyses pass the admission audit across 65 independent bedrock samples.

Admission is not an empirical result and not a freeze. No train/holdout split was performed, no parameter was fitted, and no quantity in this release informed the Manzano calibration cohort.

## 1. Acquisition and retrieval record

The three in-scope originals were acquired via a live browser session from the official ScienceBase item page:

https://www.sciencebase.gov/catalog/item/5f163a1282cef313ed81a191

The data dictionary and sample summary were acquired on 2026-10-28 between 08:06 and 08:11 UTC, and the SHRIMP-RG analytical table between 08:11 and 08:12 UTC. The item's bot block cleared in a fresh browser environment. No sign-in, payment, or terms click-through was required. The release is a USGS public data release. Direct API access from this VM returns HTTP 403; that access limitation is why the browser route was used.

| File | Size (bytes) | SHA-256 |
|---|---:|---|
| geochronology_SHRIMP-RG_swAlaskaMts_jones.csv | 445772 | c891fff4a4454c40377de2288e6e1d47b970e6ee6ac08e8712a42e746d4b186d |
| geochronology_sampleSummary_swAlaskaMts_jones.csv | 32104 | 189e32c39a9ab8b87c9c9e027f3547aed425320a28744142d7228e6bd2a2a7f0 |
| geochronology_dataDictionary_swAlaskaMts_jones.csv | 12108 | 93716a490f6cde071957814e6771d51c2f65e3cfcbf0e3d0ae22b2f4c9a8aa6b |

The originals remain in `originals/` under their canonical names. Their hashes were rechecked after all processing and were unchanged.

### 1.1 Attached files not downloaded

The release has eight attached files. Five were not downloaded:

- `geochronology_detritalZircon_swAlaskaMts_jones.csv`: LA-ICP-MS detrital zircon table. Out of cohort scope: a different method and a detrital (sedimentary provenance) population, not SHRIMP-RG bedrock analyses. Its dictionary entries also show its ratios are total (uncorrected) ratios, so it would not populate the gate schema in any case.
- FGDC metadata XML and the HTML metadata rendering: not required for the admission audit.
- Two supplemental methods PDFs: not required for the admission audit; the data dictionary carries the field-level definitions the audit relies on.

## 2. Inventory record

`acquisition_inventory.py` was NOT run on this release. It is Manzano-specific: it hardcodes DOI 10.5066/P9U0P2ZY and the three Manzano filenames, so forcing it onto this release would produce a false record. An equivalent inventory record was produced instead at `inventory-record.json` (this directory), listing all eight attached files with per-file status (PRESENT_UNVERIFIED for the three downloaded files, with sizes and SHA-256 hashes; NOT_DOWNLOADED with reasons for the other five) and the retrieval record. Its overall status uses the same vocabulary as the Manzano tool: AWAITING_PROVENANCE, with the retained note that hashes describe local bytes and do not independently authenticate source provenance.

## 3. Provenance manifest and verification

Manifest: `source-provenance-manifest.json`

`source_provenance.py` is release-agnostic, so it was used directly, unchanged. Each manifest entry records:

- DOI: 10.5066/P9K5NFKN
- Source URL: https://www.sciencebase.gov/catalog/item/5f163a1282cef313ed81a191
- Canonical filename
- SHA-256 of the original local bytes
- Retrieved UTC: 2026-10-28 08:06-08:11 UTC (dictionary and sample summary); 2026-10-28 08:11-08:12 UTC (analytical table)
- License/release characterization: USGS public data release
- Source type: Original USGS ScienceBase data file acquired via live browser session

Command interface:

`python source_provenance.py source-provenance-manifest.json originals/`

Verifier verdict:

- Overall status: VERIFIED
- geochronology_SHRIMP-RG_swAlaskaMts_jones.csv: VERIFIED
- geochronology_sampleSummary_swAlaskaMts_jones.csv: VERIFIED
- geochronology_dataDictionary_swAlaskaMts_jones.csv: VERIFIED

Full output: `provenance-output.json`.

As with the Manzano and Sierra Nevada runs, the license/release field is recorded as "USGS public data release" from the retrieval record; no separate formal license identifier was present in the downloaded files. The verifier confirms the manifest field is present and the recorded hashes match the local original bytes; it does not independently validate a formal license identifier.

## 4. Data-dictionary findings

The dictionary was read in full before the analytical table was mapped. It has 94 lines and covers three tables: the SHRIMP-RG analytical table, the detrital zircon table (not downloaded), and the sample summary. The dictionary's field inventory matches both delivered headers exactly, in both directions: no dictionary-only fields and no table-only fields for either delivered table. (This is cleaner than the Manzano release, which had two such discrepancies.)

### 4.1 Ratio columns

The decisive dictionary entries are:

- `204Pbcorr_206Pb_238U_Ratio`: "204Pb-corrected ratio of 206Pb to 238U."
- `204Pbcorr_207Pb_235U_Ratio`: "204Pb-corrected ratio of 207Pb to 235U."

Accordingly:

- `r68` maps to `204Pbcorr_206Pb_238U_Ratio`.
- `r75` maps to `204Pbcorr_207Pb_235U_Ratio`.

The table also carries total (uncorrected) ratios and 204Pb-corrected 238U/206Pb and 207Pb/206Pb ratios. No total ratio was substituted for either target ratio.

### 4.2 Uncertainty basis

The decisive dictionary entries are:

- `204Pbcorr_206Pb_238U_Ratio_Unc_1sig_perc`: "Uncertainty (1-sigma) on 204Pb-corrected ratio of 206Pb to 238U, in percent", Units "%".
- `204Pbcorr_207Pb_235U_Ratio_Unc_1sig_perc`: "Uncertainty (1-sigma) on 204Pb-corrected ratio of 207Pb to 235U, in percent", Units "%".

The analytical ratio uncertainties are therefore relative percent uncertainties at 1 sigma. The only conversion used was:

- `sigma68_abs_1s = r68 * 204Pbcorr_206Pb_238U_Ratio_Unc_1sig_perc / 100`
- `sigma75_abs_1s = r75 * 204Pbcorr_207Pb_235U_Ratio_Unc_1sig_perc / 100`

Observed ranges across the 846 admitted analyses:

- r68: 0.003 to 0.341; source percent uncertainty 0.6 to 82.8 percent; converted absolute 1-sigma 0.000035 to 0.00546
- r75: 0.001 to 6.833; source percent uncertainty 1.5 to 2108.2 percent; converted absolute 1-sigma 0.000738 to 1.3338

The sample summary's `UPb_Age_Unc_Ma` is a 2-sigma age uncertainty. No age or age uncertainty was mapped into the cohort.

### 4.3 Wetherill paired-ratio correlation: present and populated

The dictionary entry for `Error_Correlation` is decisive and is quoted verbatim:

"Error correlation of the 207Pb/235U and 206Pb/238U ratios."

This is the paired-ratio correlation for the two target Wetherill coordinates, not a Tera-Wasserburg correlation and not a quantity derived from ages. Confirmation in the analytical table itself:

- The `Error_Correlation` column exists in the delivered table header (column 25).
- All 1344 table rows carry a nonblank numeric value; there are no missing values.
- Across the full table the values run from 0.0 to 4.01. The single value above 1 (4.01, analysis 15AJJ017C-1.1_AJJ27) sits in a sample the subset rule excludes on interpretation grounds (section 5), so it never reaches the auditor.
- Across the 851 in-scope rows: minimum 0.0, maximum 0.99, no missing values, and 12 rows with the value exactly 0.0. Of those 12, 9 were admitted and 3 were among the 5 audit rejections (on other grounds, section 6). An exactly zero published correlation is admissible under the auditor as written (it rejects only values not strictly between -1 and 1). Whether a published 0.0 is a measured near-zero correlation or a placeholder is not stated by the source; this audit copies the values verbatim and flags the question for the freeze step rather than resolving it by assumption.

Consequence: `rho_wetherill` maps directly to the published `Error_Correlation`. No rho was fabricated, inferred, set to zero, or reconstructed from reported ages.

### 4.4 Common-Pb correction and correction status

The selected ratio fields are explicitly named with the `204Pbcorr_` prefix, and their dictionary descriptions call them "204Pb-corrected" ratios. The cohort therefore records:

- `common_pb_method`: "204Pb correction"
- `correction_status`: "corrected_radiogenic"

As in the Manzano audit, there is no separate per-row source column named correction status. That status is encoded from the selected 204Pb-corrected ratio fields, not copied from a status field. This distinction is retained here so the transformation is auditable.

### 4.5 Table structure, sample join, and source inconsistencies

Analytical-table structure:

- 1344 data rows: 1036 zircon analyses and 308 titanite analyses (`Mineral` column).
- 84 distinct sample codes in the table.
- `AnalysisSpot_Mount` is unique across all 1344 rows (the dictionary defines it as "Concatenation of Analysis_Spot and Mount; unique identifier"), and `analysis_id` maps to it.
- The table bytes are UTF-8 except for six bytes of value 0x85, each inside an analysis spot name (for example `11AJJ008-10.1` followed by byte 0x85 and `dup1`). Read as Windows-1252, 0x85 is the ellipsis character, and the suffix marks a repeated spot. Inspection and mapping decoded the table as Windows-1252 so these identifiers are preserved; the original bytes were never modified. One such analysis (RAAK136-16, ellipsis, dup1) is in the admitted cohort.

Sample-summary structure:

- 190 summary rows covering three analysis populations: 95 SHRIMP-RG rows (79 U-Pb zircon, 16 U-Pb titanite) and 95 LA-ICP-MS detrital zircon rows (not part of this audit).
- 14 samples appear twice in the summary, once with a U-Pb titanite row and once with a U-Pb zircon row: the same bedrock sample analyzed for both minerals. The join is therefore keyed by (sample, mineral-mapped analysis type), not by sample alone.

Join rule and its limits:

- Table sample codes are matched to summary codes after removing non-alphanumerics, uppercasing, and stripping leading zeros inside digit runs, because the table zero-pads some codes the summary does not (for example table `12AJJ042D` against summary `12AJJ42D`).
- Two table samples cannot be matched to any summary row under this rule: `12AJJ039A` (10 zircon rows) and `13ATE310` (10 zircon rows). The nearest summary codes, `12AJJ39E` and `13ATE310A`, differ in their suffix letters, and suffix letters distinguish distinct samples elsewhere in this release (for example 12AJJ42C against 12AJJ42D). These pairs were NOT reconciled by guess. The 20 zircon rows are excluded as unmatchable (section 5). Both candidate summary rows describe igneous crystallization zircon samples, so if the Principal Operator reconciles the identifiers against the FGDC metadata or the authors' records, these rows would likely enter scope; that reconciliation is a source-data decision, not this audit's.
- Sample `12SB112Z` is internally inconsistent in the source: its only summary row describes a U-Pb zircon analysis, but the table contains no zircon rows for it, only 15 titanite rows, which have no titanite summary row. Those 15 rows are excluded as unmatchable for their (sample, type) pair.

### 4.6 Analysis IDs and grouping fields

- `analysis_id` maps to `AnalysisSpot_Mount`.
- `rock_unit` maps to the sample-summary `Sample` code. At this release's granularity each field sample is one bedrock unit occurrence; the summary carries no formation or pluton-name field (its Rock_Comment is free text and is blank for many samples), so the sample is the honest unit key. Grouping tallies by Rock_Class and Rock_Type are reported in section 8.
- `laboratory` maps to the sample-summary `Analysis_Lab`: Stanford-USGS SHRIMP-RG for every in-scope row.
- `method` maps to the sample-summary `Analysis_Method`: SHRIMP U-Pb for every in-scope row.

## 5. Subset rule and cohort construction

Transformation script: `build_admission_cohort.py` (run locally during the audit; not filed with this evidence)
Mapping and per-record log: `cohort-mapping-log.json`
Cohort: `alaska-admission-cohort.csv`
Cohort SHA-256: 9c9bef2d48af043a339e37bf86d211796f2269df637461462c7bc346555f74ef

### 5.1 The rule, as declared

The rule was fixed from sample-summary metadata before any ratio was examined, and applied mechanically:

A SHRIMP-RG table row is in scope if and only if the summary row for its (sample, mineral-mapped analysis type) pair states Analysis_Type "U-Pb zircon" for a zircon row, Analysis_Method "SHRIMP U-Pb", Rock_Class igneous or metamorphic, and UPb_Age_Interpretation "crystallization".

Titanite declaration: titanite rows are OUT. The gate program (EMPIRICAL_GATE_v0.2 and the validation protocol, with the Manzano cohort as precedent) is a zircon U-Pb program; titanite is a different mineral system whose summary interpretations in this release are dominated by metamorphism and cooling rather than crystallization, and mixing mineral systems into one Wetherill cohort would confound the shared-parameter structure the gate requires. This exclusion is by mineral, declared in advance, and is not based on any titanite row's ratios.

Selection discipline: no concordance-based criterion was used. `Percent_Discordant` was not consulted. `Interpreted_Age_Included` was not used as a filter: among the 846 admitted analyses, 700 carry Y and 146 carry N in that source column, and both were retained, exactly as in the Manzano audit.

### 5.2 Counts at each step

| Step | Rows |
|---|---:|
| Table rows total | 1344 |
| Excluded: no matching summary row for (sample, mineral type) | 35 |
| Excluded: titanite analysis (zircon program) | 293 |
| Excluded: summary interpretation "metamorphism" (zircon rows) | 156 |
| Excluded: summary interpretation blank (zircon rows) | 9 |
| In scope and mapped to cohort | 851 |

The 35 unmatchable rows decompose as: 20 zircon rows from the two suffix-discrepant samples (section 4.5) and 15 titanite rows from sample 12SB112Z, which has no titanite summary row. The 293 titanite exclusions are the titanite rows that did match a titanite summary row; total titanite rows are 308. No row was excluded for Rock_Class: every matched zircon row's sample is igneous or metamorphic (the sedimentary summary rows belong to the LA-ICP-MS detrital population, which has no rows in this table).

### 5.3 Field mapping

| Admission field | Source or rule |
|---|---|
| source_doi | 10.5066/P9K5NFKN |
| source_sha256 | SHA-256 of original analytical CSV, c891fff4a4454c40377de2288e6e1d47b970e6ee6ac08e8712a42e746d4b186d |
| analysis_id | AnalysisSpot_Mount |
| rock_unit | Sample-summary Sample code |
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

## 6. Admission audit

Command interface, including the checksum guard for the normalized cohort:

`python audit_cohort.py alaska-admission-cohort.csv --expected-sha256 9c9bef2d48af043a339e37bf86d211796f2269df637461462c7bc346555f74ef`

Audit output:

- Admission table SHA-256: 9c9bef2d48af043a339e37bf86d211796f2269df637461462c7bc346555f74ef
- Total: 851
- Accepted: 846
- Rejected: 5
- Status: AUDITED_NOT_FROZEN

Full output: `audit-output.json`.

Rejection reasons (auditor-produced):

| Reason | Records |
|---|---:|
| nonpositive_uncertainty | 5 |
| negative_ratio | 1 |

The 5 rejected analyses, characterized from their source rows:

| Analysis | Source values | Why the auditor rejects it |
|---|---|---|
| 12AJJ47B-1.1_AJJ01 | r75 = 0, percent uncertainty 6261.2 | A zero ratio converts to a zero absolute sigma |
| AJJ232A-12.1_AJJ06 | r75 = 0, percent uncertainty 3978.6 | A zero ratio converts to a zero absolute sigma |
| 16AJJ102A-43.1_AJJ31 | r75 = 0, percent uncertainty 18230.8 | A zero ratio converts to a zero absolute sigma |
| 12SB135A-4.1_AJJ07 | r68 = 0, r75 = 0.016 | A zero ratio converts to a zero absolute sigma |
| 15ALR138-3.1_AJJ25 | r68 = -0.006, r75 = -1.491 | Negative (background-subtracted) ratios, and a negative converted sigma |

These are source-data properties, not mapping defects: a measured ratio of exactly zero (or a negative background-subtracted value) cannot carry a positive absolute 1-sigma under the percent conversion, and the auditor's positivity requirements are doing exactly what they are designed to do. All 5 samples containing a rejected row retain other admitted analyses, so no sample is lost from the cohort by these rejections.

### Audit interface and enforcement limits

The `--expected-sha256` value for `audit_cohort.py` is the SHA-256 of the normalized admission table, not the SHA-256 of the original analytical CSV. The cohort's separate `source_sha256` field correctly carries the original analytical-file hash.

The audit script checks that required text fields are nonempty, numeric fields are finite, ratios are nonnegative, uncertainties are positive, rho is strictly between -1 and 1, `correction_status` is exactly `corrected_radiogenic`, and `measurement_basis` is exactly `wetherill_absolute_1sigma`. It does not independently verify that the DOI is this release's DOI, that `source_sha256` equals the provenance-verified analytical-file hash, that the subset rule was the declared one, or that rho was actually published. Those links were established by the provenance, dictionary, and subset-rule steps in this run.

## 7. EMPIRICAL_GATE_v0.2 gate-by-gate disposition

1. **Retrieve original bytes and record SHA-256, license, and DOI/version:** Evaluated for admission. The original bytes are present, the DOI and hashes are recorded, and provenance verification passed. The license/release field is recorded as "USGS public data release" from the retrieval record; no separate formal license identifier was supplied.
2. **Verify column meanings, correction algorithms, sigma level, and covariance orientation:** Evaluated. The dictionary establishes 204Pb-corrected Wetherill ratios, percent 1-sigma uncertainties, and the published paired-ratio error correlation for exactly those two ratios.
3. **Retain exclusions and counts; no concordance-based cherry-picking:** Evaluated. All counts are retained: 1344 table rows, 493 rule exclusions grouped by methodological reason, 851 mapped, 5 audit rejections. No concordance, age, or publication-inclusion criterion was used at any step.
4. **Split by geological unit and analytical laboratory and freeze before fitting:** Not performed. No freeze was made and no split was executed; the structural facts a freeze would need are established in section 8 (65 independent bedrock samples as units; one laboratory, the same as the calibration cohort's). Freezing group IDs, parameter bounds, and the evaluation code commit remains a separate, later decision.
5. **Independent conventional comparator and symmetric process models:** Not evaluated. Fitting and model comparison are outside this task.
6. **Shared RCI parameters constrained independently of held-out ratios:** Not evaluated. No fitting was performed. The holdout separation was preserved: nothing in this release informed any Manzano calibration quantity.
7. **Predictive log-likelihood, calibration, coverage, parameter count, sensitivity, and failed cases:** Not evaluated for model performance. The failed-case counts available at this stage are the admission results: 493 rule exclusions and 5 audit rejections.

## 8. Holdout-suitability assessment

### 8.1 Grouping structure of the admitted cohort

The admitted cohort spans all 65 in-scope samples; no sample was lost to audit rejections.

- Samples by Rock_Class: 55 igneous, 10 metamorphic.
- Analyses by Rock_Class: 668 igneous, 178 metamorphic.
- Analyses per sample: 3 to 32.
- Samples and analyses by Rock_Type: granite 21 samples / 253 analyses; granodiorite 14 / 167; monzonite 5 / 79; amphibolite 6 / 111; diorite 3 / 39; andesite 3 / 33; orthogneiss 3 / 50; rhyolite 3 / 30; gabbro 2 / 27; mafic gneiss 2 / 33; dacite 1 / 11; mafic dike 1 / 8; trondhjemite 1 / 5.

No single sample dominates (the largest contributes 32 of 846 analyses, under 4 percent). Concentration exists at the rock-type level: granite and granodiorite together contribute 420 of 846 analyses (about 50 percent). That is a composition fact a freeze should record, not an admission defect: the units are independent bedrock samples, and a unit-level split can be stratified by rock type if the Principal Operator wants type balance across the split.

The summary carries latitude and longitude (NAD83) for every sample, so a geographic grouping (the release spans the Western Alaska Range, Northern Aleutian Range, Taylor Mountains, and Tikchik Mountains regions) is possible at freeze time, but the files carry no per-sample region field, and this audit does not assign regions from coordinates by its own judgment.

### 8.2 Independence from the Manzano calibration cohort

- **Geological units: fully disjoint.** The 65 admitted samples are Alaskan bedrock samples from a different release; the Manzano cohort is one sample (Blue Springs metarhyolite, New Mexico). No sample, unit, or analysis overlaps.
- **Source: independent.** Different publication, different DOI, different field program, separately provenance-verified bytes.
- **Laboratory: NOT independent.** Every admitted analysis was produced by the Stanford-USGS SHRIMP-RG laboratory, the same laboratory as the Manzano calibration cohort, using the same method (SHRIMP U-Pb) and the same reporting template. Gate 4's phrasing ("geological unit and analytical laboratory") should be read with that fact on the record: this holdout satisfies the locked decision's "split by geological unit or independent source" clause through unit and source independence, not through laboratory independence. Any shared laboratory systematic would be common to both cohorts; that is a known, bounded limitation, and it is the same limitation recorded for the Sierra Nevada candidate.

### 8.3 Caveats a freeze must carry

1. **Laboratory non-independence** (section 8.2). The holdout tests geological generalization, not laboratory generalization.
2. **Twelve published correlations of exactly 0.0**, 9 of them in admitted rows (section 4.3). If the freeze judges them placeholders rather than measurements, those rows' status should be decided explicitly at freeze time, not silently in either direction.
3. **Two unreconciled sample identifiers** (section 4.5): 20 zircon rows from samples 12AJJ039A and 13ATE310 are currently unmatchable and excluded. Reconciliation against the FGDC metadata or the authors' records could add 2 igneous crystallization samples to a future cohort version; it cannot be done by assumption.
4. **Rock-type concentration**: granite plus granodiorite is about half the admitted analyses (section 8.1).
5. **The single out-of-range correlation in the release** (4.01) is excluded by the subset rule, not repaired; if the cohort definition ever widens to metamorphism interpretations, that value would need a source-data decision first.

### 8.4 Conclusion

The Western Alaska Range release is **eligible as the designated DFM holdout under EMPIRICAL_GATE_v0.2 as written**: it populates every schema field from published values, its provenance verifies, its admission audit passes 846 of 851 rule-scoped analyses, and its units are geologically disjoint from the calibration cohort. Its status is the audit script's status, `AUDITED_NOT_FROZEN`.

What it can support, once a freeze is separately decided and recorded:

- A unit-level held-out evaluation disjoint from the Manzano calibration cohort, split by bedrock sample (and stratifiable by rock class or rock type).
- Held-out scoring under gate 6, provided RCI parameters are fitted on the calibration side only and frozen before any ratio in this cohort is scored.

What it cannot support:

- Any claim of laboratory-independent replication (same laboratory and method as calibration).
- Any empirical statement yet: no split, freeze, fit, or comparator evaluation has been performed, and none was authorized by this task.

## 9. Work products

- `inventory-record.json` (equivalent inventory; acquisition_inventory.py not run, Manzano-specific)
- `source-provenance-manifest.json`
- `provenance-output.json`
- `build_admission_cohort.py` (local only; not filed)
- `cohort-mapping-log.json` (including the full per-record exclusion list)
- `alaska-admission-cohort.csv`
- `audit-output.json`

Originals in `originals/` were rehashed after all processing: unchanged (c891fff4..., 189e32c3..., 93716a49...).

Human-Curated, AI-Enabled (HCAE)
