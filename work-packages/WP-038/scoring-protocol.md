# WP-038 Scoring Protocol v1 (frozen 2026-11-15)

Frozen under the G1 disposition (g1-disposition.md). Any change after freezing is a new protocol version, recorded as a programme revision with its reason. No held-out extraction or unblinding occurs under this protocol until JD authorizes the scoring phase.

## Sampling frame and datasets

- Frame: the 342 human-chimpanzee paired loci of the Retrovirology 2015 supplement (MOESM2), as listed in data/pilot-split.csv with family assignments.
- Split: group-aware by ERV family, data/pilot-split-v2.csv (seed 20261116; rule in g1-disposition.md F1). Training side: 212 loci. Held-out side: 130 loci in 12 families, of which 78 are quarantined as previously examined and 52 are the clean held-out scoring set.
- Canonical training dataset: data/training206-verdicts-final.csv (the v1 training 206, all inside training-side families or quarantined; fitting uses resolved training-side loci only). Resolved status at freeze: 144 of 206 resolved; unresolved loci are excluded from fitting and reported.
- Canonical held-out dataset: the 52 clean loci, extracted at scoring time under the benchmark design's graded orthology rule, with the same manifest provenance requirements as the training extraction.

## Predictive metric

- Primary: mean per-locus log predictive density of the joint evidence under each model, computed on held-out loci. Joint evidence per locus: presence and absence pattern across the taxon panel, flank and boundary agreement, orientation, TSD where recoverable, shared derived substitutions, deletions and disabling mutations with positions, and LTR divergence where an LTR pair is measurable.
- Model parameters are fitted on training loci only. The D3 targeting distribution is estimated from experimental integration datasets only, never from orthology patterns.
- Secondary: locus-weighted and family-cluster-weighted versions of the primary metric; event-count accounting reported as descriptive only, never as a parity measure.

## Decision rule for parity

Parity for a D model against the comparator on this evidence class requires all of the following, evaluated on held-out loci:

1. **Predictive noninferiority.** The family-cluster bootstrap 95 percent confidence interval for the difference in mean log predictive density (D model minus comparator) lies entirely above the noninferiority margin of minus 0.1 nats per locus. The margin is declared here, before any held-out result: 0.1 nats per locus corresponds to roughly a 10 percent per-locus predictive odds disadvantage, the largest disadvantage the programme will still call comparable. Sensitivity is reported at margins of 0.05 and 0.2 nats. Equivalence is never inferred from overlapping intervals or from a nonsignificant difference.
2. **Burden of the same order.** The model's burden ledger vector (scoring-protocol burden section) shows no dimension exceeding the comparator's corresponding dimension by an order of magnitude, and the coding-length sensitivity analysis does not reverse the ordering under any declared weighting.
3. **No hard-core violation.** No fabricated event trace, no unregistered auxiliary, no post-hoc modification counted as a prediction.

Gate outcomes use the WP-038 labels: supported (all three conditions met), unresolved (the interval crosses the margin, or scored held-out loci fall below the benchmark minimum of 50 and the result is labelled preliminary), failed (the interval lies entirely below the margin, or parity is reachable only through a hard-core violation or a degenerative modification).

## Uncertainty

Family-cluster bootstrap, 1,000 resamples over families, loci resampled within families as clusters. Both locus-weighted and cluster-weighted estimates are reported. Where the two disagree materially, the cluster-weighted estimate governs the headline, because family is the dependence unit.

## Missingness

Unresolved loci (assembly gaps, segmental duplications, pericentromeric regions, failed controls) are excluded from the headline score and reported with their causes. A bounds analysis accompanies every headline result: unresolved held-out loci are scored once under the assignment most favourable to the D model and once under the assignment most favourable to the comparator; if the gate outcome differs between the bounds, the outcome is reported as unresolved with the bounds stated.

## Burden ledger

Per model, reported as a vector, never collapsed to a single count in the headline:

- integration events and loss events invoked;
- boundary placements (D models) or ancestral nodes and branch parameters (comparator);
- initialized families or elements (D models), each with its preregistered warrant;
- rate, population and ascertainment parameters, each marked estimated, assumed, or externally fixed with rationale;
- auxiliary invocations from the declared catalogues, counted per invocation.

A coding-length sensitivity analysis accompanies the ledger: each dimension is converted to an approximate description length under a declared encoding, and the parity burden condition is re-evaluated under at least two alternative encodings.

## Unblinding and versioning

Held-out extraction and scoring run once per preregistered model version, after JD authorizes the scoring phase. Any model modified after held-out exposure is a new version and requires a genuinely new held-out cohort for any subsequent parity claim; results obtained after exposure are reported as training performance only. Negative results and unresolved loci are preserved and reported, per the Historical Integrity Constraint.

Human-Curated, AI-Enabled (HCAE)
