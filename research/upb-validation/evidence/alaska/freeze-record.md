# Alaska holdout freeze record

Date: 2026-10-28
Cohort: Jones et al. (2020) western Alaska Range U-Pb release (admission cohort)
Companion evidence: this directory (audit-report.md, inventory-record.json, source-provenance-manifest.json, provenance-output.json, alaska-admission-cohort.csv, audit-output.json, cohort-mapping-log.json, originals/)
Authorization: Principal Operator, 2026-10-28: "File the Alaska evidence and freeze it as the designated holdout"

Human-Curated, AI-Enabled (HCAE)

## Cohort identification

- Source release: Jones et al. (2020), U-Pb Isotopic Data and Ages of Zircon and Titanite from the Western Alaska Range, Northern Aleutian Range, Taylor Mountains, and Tikchik Mountains Regions, Alaska, USGS.
- DOI: 10.5066/P9K5NFKN (ScienceBase item 5f163a1282cef313ed81a191). Publication date: 2020-07-21.
- Scope as admitted: SHRIMP-RG zircon analyses of bedrock igneous and metamorphic samples from the western Alaska Range and related regions (65 samples; section "Subset rule and admission result").
- Laboratory: Stanford-USGS SHRIMP-RG. Method: SHRIMP U-Pb.
- Ratios admitted: 204Pb-corrected 206Pb/238U and 207Pb/235U (Wetherill pair), uncertainties published as percent 1-sigma and converted to absolute 1-sigma with the conversion recorded in cohort-mapping-log.json. Paired-ratio error correlation is published in the source as Error_Correlation (in-scope range 0.0 to 0.99, none missing); no correlation was inferred, set to zero, or derived from ages.

## Designation

DESIGNATED HOLDOUT. This cohort is the program's held-out evaluation cohort, and it is frozen with this filing.

It fills the holdout seat left open by the Sierra Nevada holdout determination (evidence/sierra-nevada/holdout-determination.md, filed by PR #46), which found the Sierra Nevada release (Langenheim et al. 2025, DOI 10.5066/P13LKC5C) ineligible under EMPIRICAL_GATE_v0.2 as written and superseded the earlier Sierra designation in OBSERVATIONAL_ACQUISITION_DECISION_v0.5.md. The holdout designation sentence in the Manzano freeze record (evidence/manzano/freeze-record.md) is superseded accordingly: it named Sierra Nevada as the designated holdout pending its audit; that audit found it ineligible, and this record now designates the Alaska cohort.

## Role restriction

HELD-OUT EVALUATION ONLY. This cohort must never be used to fit, tune, or select calibration parameters, models, or bounds. Shared RCI parameters are fitted on calibration material only (currently the Manzano cohort), frozen, and only then scored against this cohort. Nothing from this cohort has informed any calibration quantity, and that separation was preserved throughout acquisition and audit.

## Subset rule and admission result

The subset rule was declared from sample-summary metadata before any ratio was examined, and applied mechanically: a SHRIMP-RG table row is in scope if and only if the summary row for its (sample, mineral-mapped analysis type) pair states Analysis_Type "U-Pb zircon" for a zircon row, Analysis_Method "SHRIMP U-Pb", Rock_Class igneous or metamorphic, and UPb_Age_Interpretation "crystallization". Titanite rows are out: the gate program is a zircon U-Pb program, declared by mineral in advance. No concordance, age, or publication-inclusion criterion was used.

Counts (full record in audit-report.md and cohort-mapping-log.json):

- Analytical table rows: 1344 (1036 zircon, 308 titanite).
- Excluded by the rule: 493 (35 no matching summary row for the (sample, mineral type) pair; 293 titanite; 156 summary interpretation "metamorphism"; 9 summary interpretation blank).
- In scope and mapped: 851 analyses from 65 bedrock samples.
- Admission audit (audit_cohort.py): 846 accepted, 5 rejected. Rejection reasons: nonpositive_uncertainty on 5 records and negative_ratio on 1 of them. Three analyses have r75 exactly 0 and one has r68 exactly 0 (a zero ratio converts to a zero absolute sigma under the percent conversion); the fifth has negative background-subtracted ratios (r68 -0.006, r75 -1.491) and carries both reasons. All 5 samples containing a rejected analysis retain other admitted analyses; no sample was lost. Full output in audit-output.json.
- Status transition: with this filing, the Alaska cohort moves from AUDITED_NOT_FROZEN to FROZEN at the cohort level. The checksums below, the cohort file, the designation, and the role restriction are fixed as of this record.
- The overall empirical gate status remains NOT FROZEN. This record freezes the Alaska holdout cohort only; it does not freeze the evaluation, any parameter bounds, or the calibration side.

## Frozen checksums (SHA-256)

Originals (byte-pristine, in originals/):
- geochronology_SHRIMP-RG_swAlaskaMts_jones.csv: c891fff4a4454c40377de2288e6e1d47b970e6ee6ac08e8712a42e746d4b186d
- geochronology_sampleSummary_swAlaskaMts_jones.csv: 189e32c39a9ab8b87c9c9e027f3547aed425320a28744142d7228e6bd2a2a7f0
- geochronology_dataDictionary_swAlaskaMts_jones.csv: 93716a490f6cde071957814e6771d51c2f65e3cfcbf0e3d0ae22b2f4c9a8aa6b

Normalized admission cohort:
- alaska-admission-cohort.csv: 9c9bef2d48af043a339e37bf86d211796f2269df637461462c7bc346555f74ef

## Retrieval and provenance record

Acquired 2026-10-28 between 08:06 and 08:11 UTC (data dictionary and sample summary) and between 08:11 and 08:12 UTC (analytical table) via a live browser session from the official ScienceBase item page (https://www.sciencebase.gov/catalog/item/5f163a1282cef313ed81a191), after direct API access from the acquisition environment returned HTTP 403; the browser route was used for that reason. No sign-in, payment, or terms click-through was required. The release is a USGS public data release. Provenance verification (source_provenance.py against source-provenance-manifest.json): VERIFIED, 3 of 3 files. Five of the release's eight attached files were not downloaded, with reasons recorded in inventory-record.json (the LA-ICP-MS detrital zircon table is out of cohort scope; the FGDC metadata renderings and the two supplemental methods PDFs were not required for the admission audit).

## Grouping structure of the admitted cohort

- 65 bedrock samples, all retained after audit rejections. The cohort's unit key is the field sample (the sample summary carries no formation or pluton-name field).
- By Rock_Class: 55 igneous samples (668 analyses) and 10 metamorphic samples (178 analyses).
- Analyses per sample: 3 to 32. No single sample dominates; the largest contributes 32 of 846 analyses (under 4 percent).
- By Rock_Type: granite 21 samples / 253 analyses; granodiorite 14 / 167; monzonite 5 / 79; amphibolite 6 / 111; diorite 3 / 39; andesite 3 / 33; orthogneiss 3 / 50; rhyolite 3 / 30; gabbro 2 / 27; mafic gneiss 2 / 33; dacite 1 / 11; mafic dike 1 / 8; trondhjemite 1 / 5.
- The summary carries latitude and longitude for every sample, so a geographic grouping is possible at the evaluation predeclare step, but the files carry no per-sample region field and no region assignment is made by this record.

## Independence basis

- Geological units: fully disjoint from the Manzano calibration cohort. The 65 admitted samples are Alaskan bedrock samples from a different release; the Manzano cohort is one sample (Blue Springs metarhyolite, New Mexico). No sample, unit, or analysis overlaps.
- Source: independent. Different publication, different DOI, different field program, separately provenance-verified bytes.
- Laboratory and method: NOT independent. Every admitted analysis was produced by the Stanford-USGS SHRIMP-RG laboratory, the same laboratory as the Manzano calibration cohort, using the same method (SHRIMP U-Pb) and the same reporting template. This holdout therefore tests geological generalization, not laboratory generalization. It satisfies the locked split decision ("split by geological unit or independent source") through unit and source independence; any shared laboratory systematic would be common to both cohorts, a known and bounded limitation.

## Evaluation code reference

The evaluation and admission tooling referenced by this record is the upb-validation package as it stands on master at this filing: integrated at master commit 85e779b374efb6449c7e5b60065fc407dfe617ad (research/upb-validation/: acquisition_inventory.py, source_provenance.py, audit_cohort.py, upb_baseline.py, upb_covariance.py, DFM_UPb_Validation_Protocol_v0.1.md, EMPIRICAL_GATE_v0.2.md) and unchanged since; master HEAD at filing is 0929da4dced6f1eccfe72281b10d40d36bc8c27b. Any change to that code after this record requires the evaluation predeclare step to re-pin the code commit before fitting.

## Parameter bounds statement

Initialization parameter bounds are NOT yet frozen. Neither DFM_UPb_Validation_Protocol_v0.1.md nor EMPIRICAL_GATE_v0.2.md declares numeric initialization parameter bounds. Both documents require bounds to be frozen before fitting (protocol, Preregistration and splits: freeze "model parameter priors/bounds and primary metrics before examining test outcomes"; gate item 4: freeze "initialization parameter bounds and evaluation code commit before fitting"). No numeric bounds are recorded here because none exist to record. No fitting is authorized anywhere in this program until bounds are declared and frozen in the evaluation predeclare step.

## Caveats carried with this freeze

1. Laboratory non-independence (see "Independence basis"). The holdout tests geological generalization, not laboratory generalization.
2. Twelve in-scope rows carry a published Error_Correlation of exactly 0.0; 9 of them are in admitted rows. An exactly zero published correlation is admissible under the auditor as written. Whether a published 0.0 is a measured near-zero correlation or a placeholder is not stated by the source. The values are frozen as published; whether those rows stand as admitted must be decided explicitly at the evaluation predeclare step, not silently in either direction.
3. Two sample identifiers are unreconciled: 20 zircon rows from samples 12AJJ039A and 13ATE310 cannot be matched to any summary row under the join rule (the nearest summary codes, 12AJJ39E and 13ATE310A, differ in suffix, and suffixes distinguish distinct samples elsewhere in this release). They are excluded as unmatchable, not reconciled by guess. Both candidate summary rows describe igneous crystallization zircon samples, so reconciliation against the FGDC metadata or the authors' records could add 2 samples to a future cohort version; that is a source-data decision for the Principal Operator. Related source inconsistency: sample 12SB112Z has only a zircon summary row but only titanite table rows (15, excluded as unmatchable for their pair).
4. Rock-type concentration: granite and granodiorite together contribute 420 of 846 admitted analyses (about 50 percent). A unit-level split can be stratified by rock type at the predeclare step if type balance is wanted.
5. One published correlation in the release is out of range (4.01, analysis 15AJJ017C-1.1_AJJ27). It sits in a sample the subset rule excludes on interpretation grounds, so it never reached the auditor; it was excluded, not repaired. If the cohort definition ever widens to metamorphism interpretations, that value needs a source-data decision first.

## Standing caveats

- No empirical PEP is claimed. Admission and freezing of a holdout cohort is not an empirical result.
- Nothing from this cohort has informed any calibration quantity, parameter, model, or bound.
- Synthetic benchmarks in this program are software checks, not measured isotope evidence.
- Failure to distinguish the RCI model from conventional chronology is not evidence of empirical parity (EMPIRICAL_GATE_v0.2.md item 7).
- Partition coefficients and other illustrative parameters elsewhere in this program remain illustrative, not calibrated.

Human-Curated, AI-Enabled (HCAE)
