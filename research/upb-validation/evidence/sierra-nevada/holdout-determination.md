# Sierra Nevada holdout determination

Date: 2026-10-28
Subject release: Langenheim et al. (2025), Tabular uranium-lead and trace-element compositional data of zircons and whole-rock geochemistry of plutonic rocks in the Sierra Nevada, California, USGS, DOI 10.5066/P13LKC5C (ScienceBase item 67d5cd7ed34e1acf3979e1a3)
Companion evidence: this directory (audit-report.md, source-provenance-manifest.json, provenance-output.json, inventory-record.json, sierra-nevada-admission-cohort.csv, audit-output.json, cohort-mapping-log.json, originals/)

Human-Curated, AI-Enabled (HCAE)

## Designation history

- OBSERVATIONAL_ACQUISITION_DECISION_v0.5.md designated this release the independent geological holdout: "Prefer as a distinct geological holdout, not a second source for tuning Manzano initialization parameters."
- The Manzano cohort freeze record (research/upb-validation/evidence/manzano/freeze-record.md) repeated that designation, pending this release's own acquisition and admission audit.
- Acquisition and admission audit were executed on 2026-10-28 under the Principal Operator's authorization for that task ("Do both", 2026-10-28 02:38 CDT). This filing is made under the Principal Operator's direction "Both" (2026-10-28 03:05 CDT), selecting "File the Sierra finding to the DFM repo and notify GPT".

## Admission result

- Provenance verification (source_provenance.py against source-provenance-manifest.json): VERIFIED, 3 of 3 files.
- Originals filed byte-pristine in originals/ (SHA-256):
  - UPb_dates_zircon_trace_elements_final.csv: 74f5cd1c65f15cefc6b18ab3a28a01e952c865dbbf3ac8ac3ce94a66dd7fb310
  - DataDictionary_final.csv: 317d6b57c550c609352e5d00c51ceec00c9921c91afc5970ae5a02b03c6f16a5
  - sierra_igneous_sample_localities_into_review.csv: 858e49cb3a8d0342dbfefd22719772012f8e2139db628d68c522015d1772b4b5
- Admission audit (audit_cohort.py): 706 spot analyses carried into the admission table, 0 admitted, 706 rejected. Status AUDITED_NOT_FROZEN. Normalized admission table (sierra-nevada-admission-cohort.csv) SHA-256: 83532a6793b1c16631bb44846e0f0277f0ad9af6f75ebfecec2e3b0b02f8653d. Full output in audit-output.json; full reasoning in audit-report.md.
- Universal rejection reasons (706 records each): invalid_r75, invalid_sigma75_abs_1s, invalid_rho_wetherill, missing_common_pb_method, missing_correction_status, not_confirmed_radiogenic_ratios, missing_measurement_basis, unverified_uncertainty_or_ratio_basis. Record-level defects in the source itself: duplicate_analysis_id on 13 records (repeated spot names in sample 20-R-61, distinct repeat measurements) and 1 record with blank laboratory and method (analysis 19POB046-5.1).
- No concordance-based selection was used at any stage: 0 pre-audit exclusions, and the publication's AnalysisInc flag was not used as a filter.

## Failing schema fields

- r75: not published. The dictionary defines exactly four ratio fields (207Pb/206Pb, 208Pb/206Pb, 206Pb/238U, 208Pb/232Th); no 207Pb/235U quantity exists anywhere in the release.
- sigma75_abs_1s: not computable. Propagating it from the published ratios requires their covariance, which is not published; assuming independence is the barred rho-equals-zero fabrication in another form.
- rho_wetherill: not published. No error-correlation or covariance field of any kind exists in the dictionary or the delivered table, and the locked decisions bar inferring, zero-filling, or deriving it from ages.
- correction_status / common_pb_method: the only common-Pb treatment the source documents is a 207Pb correction applied to produce an age (Pb207corr_Pb206U238Age). The tabulated ratios are not documented as corrected, no assumed common-Pb composition is given, and the release contains no 204Pb measurement; corrected_radiogenic therefore cannot honestly be asserted.
- measurement_basis: cannot be wetherill_absolute_1sigma, because the Wetherill pair the basis names does not exist in this release.

## Determination

- The Sierra Nevada release is INELIGIBLE as the DFM holdout under EMPIRICAL_GATE_v0.2 as written.
- The holdout designation in OBSERVATIONAL_ACQUISITION_DECISION_v0.5.md is superseded by this record. The Manzano freeze record's holdout pointer stands as the historically accurate record of the designation as made; this determination is the current record.
- Holdout seat: OPEN. No admitted holdout currently exists.
- This filing makes no schema amendment. Any amendment to EMPIRICAL_GATE_v0.2 or to the admission schema is a Principal Operator decision.

## Options recorded for the Principal Operator

The following options are recorded from audit-report.md section 8, without recommendation. None is actioned by this filing.

1. Author-level reduced data: obtain the underlying SHRIMP-RG reduced data for these same 35 samples from the Stanford-USGS SHRIMP-RG laboratory or the data authors, if it reports 207Pb/235U ratios and paired-ratio error correlations (the Manzano release proves this laboratory's reporting pipeline can publish that correlation). Subject to identifier reconciliation and a disambiguated analysis key.
2. A different holdout release: a release that, like Manzano, publishes corrected Wetherill ratios with percent 1-sigma uncertainties and a paired-ratio error correlation, from geological units independent of Blue Springs metarhyolite. Laboratory independence from Stanford-USGS SHRIMP-RG would additionally satisfy the gate's split rule on both dimensions.
3. A schema amendment to a lower-dimensional demonstration: admit a 206Pb/238U-only cohort for ingestion and single-ratio checks. It would still have to resolve the radiogenic-basis question for Pb206U238, and it could not test two-ratio concordia behavior or held-out parity.
4. A schema amendment to a Tera-Wasserburg formulation: this release's native coordinates are the Tera-Wasserburg pair, but the amendment would not cure the covariance absence (Tera-Wasserburg fitting with correlated errors needs the unpublished correlation between its coordinates) and the radiogenic-basis question remains.

## Standing caveats

- No empirical PEP is claimed. An admission audit of an ineligible holdout candidate is not an empirical result.
- Nothing from this release informed any calibration quantity. The holdout separation was preserved throughout the audit; no fitting, tuning, or model comparison was performed.
- Synthetic benchmarks in this program are software checks, not measured isotope evidence.
- Failure to distinguish the RCI model from conventional chronology is not evidence of empirical parity (EMPIRICAL_GATE_v0.2.md item 7).

Human-Curated, AI-Enabled (HCAE)
