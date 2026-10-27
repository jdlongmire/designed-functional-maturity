# RCIM-002: Pre-registered Radiogenic Test Protocol

**Status:** Draft protocol; no empirical result claimed. **Date:** 2026-10-27.  
**Depends on:** WP-002, WP-004, WP-005, RCIM-001.

## Objective
Determine whether a low-dimensional, independently constrained initialization generator predicts observed radiogenic isotope structure across held-out samples more successfully than unconstrained initialization and competitively with conventional geological models. This is a comparative test of explanatory auxiliaries, not a direct experiment on creation.

## Model classes
- **M0, conventional geological history:** Ordinary decay plus independently evidenced mineral formation, common daughters, inheritance, transport, mixing, and resetting. Use current published reference analyses as benchmarks, not caricatures.
- **M1, unconstrained initialization:** Arbitrary initial daughters per sample, with ordinary subsequent decay. Deliberate flexibility ceiling; excellent in-sample fit does not count as predictive success.
- **M2, constrained functional initialization:** Shared initial-state generator G(Phi,L,B;theta) whose parameters are fixed from non-target mineralogical/thermal/geochemical observations before isotope test outcomes are revealed. Ordinary subsequent decay and explicitly modeled disturbance.
- **M3, null functional sensitivity:** Keep elemental inventories fixed while perturbing isotope fractions where physically admissible. Optional sensitivity probe; does not adjudicate provenance.

## Mathematical forward model
For each parent isotope i and stable daughter j in a closed compartment:
P_i(t) = P_i(0) exp(-lambda_i t)
D_j(t) = D_j(0) + b_ij P_i(0) [1-exp(-lambda_i t)]
where b_ij is the appropriate daughter branching fraction; for open systems, add explicitly defined transfer/retention terms. Correctly handle K-40 branching to Ar-40 and Ca-40, and chain-to-stable-daughter accounting for U/Th. Keep daughter and common-isotope inventories distinct.

**U-Pb paired-chain ratio test:**
r68(t) = [D206*(0)/P238(0)] exp(lambda238 t) + exp(lambda238 t)-1
r75(t) = [D207*(0)/P235(0)] exp(lambda235 t) + exp(lambda235 t)-1
Use measured present ratios with uncertainty and common-Pb correction. Do not assume initial radiogenic daughters zero in M2; do not use target apparent ages to set them.

**K-Ar reservoir model:** Couple atmospheric, mantle, crustal and mineral Ar-40 with K-40 decay branching, source/sink transport, degassing, escape, and retention. Conserve atoms through reservoir transfers. Atmospheric pressure is a diagnostic, not a proxy for habitability or proof of isotope-specific necessity.

## Data acquisition and provenance
1. Select publicly accessible zircon U-Pb measured-isotope datasets with sample IDs, uncertainties, common-Pb handling, and documented mineral context. Prefer datasets with independent Lu-Hf/Th-Pb measurements for linked tests.
2. Select documented K-Ar/Ar-Ar datasets including standards, known-age lava controls where available, and atmospheric Ar baseline measurements.
3. Capture DOI/URL, version/date, instrument methods, correction scheme, analytical covariance, and original reported ratios. Preserve raw ratios independently of interpreted ages.
4. Freeze inclusion/exclusion criteria before fitting. Exclude only on independently documented analytical or geological grounds, not discordance unfavorable to a model.
5. Record unknown or inaccessible parameters as missing, not invented.

## Holdout and leakage prevention
- Split by geological body or source group, not randomly by spot from the same zircon. Avoid train/test leakage from shared inheritance, lab calibration or mineral origin.
- Fit nuisance parameters only on training samples. Declare shared/global, lithology-level and sample-level parameters with explicit counts.
- Pre-register predicted ranges, uncertainty intervals, concordance/discordance geometry and any spatial correlations.
- Do not tune functional thresholds or initial daughter inventories using held-out isotope ratios, conventional inferred ages or known outcomes.
- Include negative controls and report all failed predictions.

## Scoring
Primary: held-out predictive log likelihood or uncertainty-normalized residuals, with calibration diagnostics. Secondary: parameter complexity, cross-system consistency, physical mass/heat balance, and independent functional evidence. Compare M2 against M0 and M1. A model with sample-specific free daughter parameters cannot earn a positive result simply by fitting every measurement.

## Decision outcomes
- **Pass (narrow):** M2 produces independently constrained, reproducible, quantitatively accurate held-out predictions and adds explanatory restriction beyond M1. This does not alone establish historical provenance or divine design.
- **Partial:** Some physically plausible functional constraints are identified, but no predictive advantage is demonstrated.
- **Fail:** The specified M2 generator cannot predict held-out ratios, relies on hidden target-age fitting, violates measured physics, or requires unconstrained per-sample adjustments.
- **Undetermined:** Available data or uncertainties cannot discriminate models. Report as such.

## First execution order
A. Freeze data schema and literature-backed constants, including half-lives, branching fractions, reservoir parameters and uncertainty.
B. Reproduce ordinary-decay closed-system analytical benchmarks with unit tests and mass-balance checks.
C. Implement K-Ar four-reservoir forward model with explicit uncertainty and sensitivity analysis.
D. Implement U-Pb dual-chain forward model with common-Pb and disturbance alternatives.
E. Acquire datasets, preregister group holdouts and initial-state generator before scoring.
F. Publish reproducible code, machine-readable inputs, negative results and a gate report.

## Open scientific obligations
No independently validated function has yet been shown to determine specific daughter-isotope inventories. A proposed functional constraint cannot be inferred from its ability to fit target isotope ratios. Any short-history initialized-daughter account must also explain multi-system concordance, cross-cutting geological relationships, and independent known-age calibration rather than simply labeling radiometric ages retrodictive.
