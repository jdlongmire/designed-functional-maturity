# WP-038 Scoring Report: Held-Out Pattern Comparison (Scoring Phase, 2026-11-15)

Executed under scoring-protocol.md v1 as frozen in the G1 disposition, on JD's authorization of the scoring phase (2026-11-15). This report is the one-shot unblinding result for model version 1. Gate outcome first, method and numbers after.

## Gate outcome: UNRESOLVED (preliminary)

The plausible-abductive-model claim is **neither established nor failed** on this run. Three independent reasons, each sufficient under the protocol:

1. **Bounds.** The marginalized point estimate favours the independence-class models (below), but the protocol's bounds analysis, which assigns unresolved held-out cells their extreme completions, spans [-0.72, +1.02] nats per locus. It crosses both zero and the noninferiority margin. Per the protocol, when the bounds change the outcome, the outcome is unresolved.
2. **Yield.** 47 of the 52 clean held-out loci carried at least one resolved non-frame cell and were scored; only 8 are fully resolved across gorilla, orangutan and macaque. The benchmark minimum for a non-preliminary label is 50 scored loci. This result is preliminary by the programme's own rule.
3. **Evidence class.** The protocol's joint evidence includes exact boundaries, TSD and shared derived marks. The held-out extraction delivered verified presence patterns (including solo-LTR and empty-site verification), not boundary, TSD or shared-mark fields. The comparison below therefore covers the pattern component of the joint evidence only, and pattern presence within this frame is not the discriminating evidence class for these models (see the ascertainment note).

## What was extracted

The 52 clean held-out loci (data/pilot-split-v2.csv) were extracted with the training census pipeline (anchor liftOver cascade at decreasing stringency) and then verified at sequence level. Two method corrections were required and are recorded here rather than silently absorbed:

- The exact 31-mer k-mer homology control used in the training sequence pass proved invalid as a pass/fail control at these loci: direct local alignment showed orthologous chimpanzee flanks whose exact 31-mer fraction was about 0.1. Verdicts in this run therefore rest on alignment-based criteria per the graded orthology rule: both flanks aligning to the target interval (normalized score at least 0.5), the internal segment aligning (at least 0.35) for presence, and absence called only on a verified empty site (flanks align, internal segment does not, short inter-flank gap), with an LTR-junction test for intermediate gaps (solo-LTR class).
- A first scoring pass fitted the models on the 50 training loci that are resolved in all three non-frame taxa. That subset is presence-biased (gorilla presence 100 percent) and is not the canonical training set. It was discarded before any result was reported; the reported run fits on the 123 training loci with gorilla and orangutan called, marginalizing uncalled cells, the same missing-data treatment as the held-out side. The discarded pass is disclosed here for the record; its headline difference was +0.34 nats on the biased subset.

Held-out resolution (52 loci): chimpanzee 51 present, 1 unresolved (RV15-0555, frame membership itself unverified there); gorilla 43 present, 9 unresolved, 0 absent; orangutan 20 present, 5 solo-LTR, 1 verified absent, 26 unresolved; macaque 4 present, 5 solo-LTR, 3 verified absent, 40 unresolved. Macaque resolution is the binding constraint, as it was in training.

## Fitted models (training only)

Patterns are the (gorilla, orangutan, macaque) presence bits; human and chimpanzee presence is fixed by the sampling frame.

- **C0** (ancestral integration and inheritance): integration placed on one of four stem branches (uniform prior in the primary run), per-segment loss probability q fitted, background independent-gain probability g fixed at 0.01. Fit: q = 0.0 (no losses required by the in-frame training patterns).
- **D3 machinery** (independent integration with locus propensity): per-locus propensity drawn from a fitted Beta distribution (alpha 55, beta 0.5, propensity concentrated high), taxon scales set from training marginal presence (gorilla 0.992, orangutan 0.951, macaque 0.60 on called cells). D1's pattern-level form is this same machinery (initialization per kind plus subsequent infection is pattern-equivalent to it); D1 is separated by its burden ledger and hard-core screen, not by a different pattern likelihood.

## Held-out results (47 scored loci)

Mean per-locus log predictive density: **C0 -0.724, independence class -0.255; difference +0.469 nats per locus in favour of the independence class**, family-cluster bootstrap 95 percent CI [+0.343, +0.538], locus-weighted. Per-locus scores are in data/scoring-results.csv; fitted parameters and the summary statistics are in the run record reproduced in the data manifest addendum in this report's repository files (data/heldout-verdicts.csv).

Sensitivity to the comparator's placement prior (the dominant assumption): stem-heavy prior (0.55 on the deepest placement) narrows the difference to +0.139 [+0.086, +0.188]; recent-heavy widens it to +0.907. The sign does not change across priors, g = 0, or g = 0.05, but the magnitude is prior-sensitive by a factor of six, which is itself reported as a finding: within this frame, the pattern comparison measures placement-prior assumptions as much as it measures history.

**Ascertainment note (material).** The 342-locus frame consists of human-chimpanzee orthologous pairs, a class selected for sharing. Presence is near-universal wherever cells resolve, in training and held-out alike. A model that assigns high probability to presence everywhere therefore scores well almost regardless of the historical claim it encodes, and the independence machinery's shared per-locus propensity is a latent common cause carried by homologous flanking sequence. This comparison does not test the origin of sharing; it tests loss rates and placement distributions inside an already-shared frame. The discriminating evidence for origin remains exact boundaries, TSD identity and shared derived marks, which is where the formalization located the severe tests from the start.

## Model-by-model gate assessment

- **C0:** not vindicated and not refuted. Its fitted loss rate is zero in-frame; its held-out score is placement-prior-sensitive. Its ledger is the lightest of the historical models (one integration per locus; phylogeny externally fixed).
- **D3:** best pattern-level predictive score, but the win is within a non-discriminating evidence class and under a propensity structure that presupposes homologous context. Parity is not established (bounds, yield, evidence class). Its ledger is parameter-light; its coincidence costs sit inside its likelihood.
- **D1:** pattern score inherits the independence machinery's. Its separate burden is heavy: an initialization per shared locus per created kind, with no preregistered independent functional warrants in this package. Its deciding test, the Historical Integrity screen on shared derived marks, was not run at held-out level because marks were not extracted. Unresolved, with the heaviest ledger of the set.
- **D2:** predictively identical to C0 below its boundary, by its own formalization, and carries C0's full ledger plus one boundary-placement choice. It earns no ERV-specific credit in this run, as designed.
- **D4:** not separately scored at pattern level (no defensible pattern likelihood exists without its designed-targeting distribution, which has not been supplied). Its severe test stands on the training-side LTR dataset (ltr-dataset-note.md): fitting the observed LTR divergence inside compressed timelines requires per-lineage substitution rates of about 33 times the standard rate at a 1,000,000-year timeline, about 3,300 times at 10,000 years, and about 5,400 times (median divergence) to 10,300 times (maximum divergence) at 6,000 years. At timelines of thousands of years that is a failed severe test by orders of magnitude; at a million years it is a large declared cost. The rooted phylogenetic direction test required by its admission conditions has not been run.

## Burden ledgers (summary; dimensions per scoring protocol)

- **C0:** integrations 1 per locus; losses fitted at 0 in-frame; parameters q plus declared placement weights; phylogeny and frame externally fixed; no catalogue auxiliaries invoked in the fit.
- **D3:** parameters alpha, beta and three taxon scales; expected independent integrations per locus equal to its expected presence count (about 2.6 in-frame); no boundary choices.
- **D1:** D3's parameters plus initialized elements per kind per shared locus (the dominant term; on the scored held-out set alone this is dozens of initializations, each requiring a warrant) plus post-creation infection events.
- **D2:** C0's ledger plus one boundary placement.
- **D4:** initialized element families (closed list not yet supplied), escape events per exogenous lineage claimed, and the rate-regime multiples recorded above.

Coding-length sensitivity: under any encoding in which an initialized locus state costs at least as much as an inherited one, D1's ledger exceeds C0's by a wide margin on shared loci; D3's advantage is predictive rather than ledger-based; D2 is C0 plus a constant. No reweighting of the ledger reverses the gate outcome, which is decided by the bounds, yield and evidence-class findings.

## What would resolve the question

1. Boundary, TSD and shared-derived-mark extraction on the held-out loci (the discriminating evidence class), under the same graded orthology and verification discipline.
2. Higher orangutan and macaque resolution, most plausibly from newer assemblies than the rheMac10 and ponAbe3 builds used here.
3. Any revised model version requires a genuinely new held-out cohort under the protocol; version 1's held-out set is spent for fitting purposes and is now a reported result.

Nothing in this report is a public claim. PR #53 remains draft; nothing is merged.

Human-Curated, AI-Enabled (HCAE)
