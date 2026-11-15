# WP-038: ERV Historical Signatures and Designed Functional Maturity

**Status:** Proposed research package; empirical validation pending  
**Parent:** DFM Research Programme  
**Governance:** EBCC-001 v1.0; PROGRAMME.md; WP-032 Historical Integrity  
**Objective:** Establish a plausible, abductive explanatory model of endogenous retroviral (ERV) evidence within the designist framework.

## Research question
Can DFM explain orthologous ERV insertion boundaries, shared sequence changes, nested phylogenetic distributions, and lineage-specific insertions without inventing nonexistent event histories or unrestricted locus-by-locus initial states?

## Objective and success criteria (JD clarifications, 2026-11-15)

The objective of this programme is to **establish a plausible, abductive explanatory model of the ERV evidence within the designist framework**: a model that explains the observed orthology, distribution and sequence patterns as the best available inference to the best explanation from the designist starting point, and that is offered as a serious explanatory contender rather than as a proof, a refutation of the rival programme, or a merely defensive accommodation.

**Explanatory parity** with the common-descent programme on the ERV evidence class is the operational standard by which 'plausible' is judged, not the objective itself. Explanatory superiority is a welcome outcome if the evidence produces it, but it is not the objective and is not required for success.

Parity is operational, not rhetorical. A DFM-compatible model set stands at parity when, on the preregistered benchmark:
1. Its held-out predictive performance on orthologous-locus patterns is comparable to C0's within the declared uncertainty, on the same loci, under the same orthology rule.
2. Its auxiliary burden, counted in the declared AHPP units, is of the same order as C0's burden of ancestral events, losses and sorting invocations; an order-of-magnitude excess is not parity.
3. It achieves this without violating the hard core: no fabricated event traces, no unrestricted initialization, no unrecorded degenerative modifications.

Superiority, if it emerges, means strictly better held-out performance, or equal performance at materially lower auxiliary burden, sustained across successive programme versions (a progressive problemshift relative to the rival programme). A single-version edge is recorded as a result, not as superiority.

The decision gate is keyed to the objective through the parity standard: supported means a plausible abductive model is established, operationalized as parity demonstrated on the benchmark as specified; unresolved means the benchmark ran and parity was neither demonstrated nor excluded within its power, so plausibility remains open; failed means the D models could not reach parity without hard-core violations or degenerating modifications, so the abductive claim fails on this evidence class. Claims in any later public material may not exceed the gate outcome, and in particular may not present the model as proven or the rival programme as refuted.

## Comparator neutrality (JD caution, 2026-11-15)

C0 is a comparator model, not the programme's presupposed baseline. It is included because the plausibility standard is comparative and because a serious designist model must be tested against the strongest explicit rival formulation, not against a weak version of it. If any programme document uses the word baseline for C0, it means only a scoring reference. It does not mean default truth, prior privilege, incumbency credit, or a presumption that the designist models must displace an already accepted account.

The programme's own starting commitments are the DFM hard core. C0, D1, D2, D3 and candidate D4 are scored from their declared generative processes, their declared auxiliaries and the evidence patterns. No model receives credit merely for being the mainstream narrative, and no designist model is penalized merely for challenging it. Where a result is reported as favouring C0 on a specified evidence slice, that means only that the stated accounting gives C0 the lower cost or higher predictive score on that slice. It is not an adoption of the evolutionary narrative as the programme's baseline.

## DFM context: retrodictive extrapolation and historical age (JD directive, 2026-11-15)

This work package sits inside the broader DFM model, and its handling of history follows PROGRAMME.md. Three epistemic categories are kept separate throughout: **measurement establishes state; retrodiction reconstructs trajectory; provenance warrants history.** The ERV measurements in this package are present states: locus positions, flank identity, presence and absence calls, LTR divergence percentages, shared sequence marks. Dates, ancestral nodes and elapsed times are not measurements. They are retrodictions, produced by extrapolating a stated rate regime and boundary conditions backward under a history model. In the programme's notation, a divergence value yields a retrodictive age (T_R) conditioned on the assumed rates; it is not, by itself, the historical elapsed time (T_H). Physical maturity is a state property; historical age is a trajectory property; inferring the second from the first requires a warranted history model.

This discipline is symmetric, as AHPP already requires for retrodictive extrapolation. The common-ancestry comparator's chronology rests on extrapolated assumptions of its own: rate regimes held across speciation nodes, ancestral population sizes and structures, and the absence of unmodelled boundary events. Those assumptions are declared and charged like any other auxiliary. Equally, a designist chronology must state its rate regimes and boundary placements and may not treat its own extrapolations as measurements.

DFM's own guardrails bind the designist side, and they are recorded here so this section cannot be misread as a licence: DFM may not invoke accelerated processes merely to compress a conventional history; may not call every unexplained datum created maturity; and may not use a conventional retrodictive age as an initialization input and then claim the recovered age as a prediction. Retrodictive accessibility does not establish historical traversal, but neither does the distinction weaken strong retrodictive evidence merely because it is inferential; it requires correct epistemic labelling. The Historical Integrity Constraint is unchanged: an event-diagnostic trace requires a real event under whichever chronology a model proposes.

Scoring consequences for this package: (1) every chronological statement is reported as a triple of measurement, assumed rate regime, and resulting T_R; (2) model scoring includes sensitivity analysis across the declared rate regimes rather than a single assumed clock; (3) no model earns credit for reproducing a date it was fitted to; (4) where two models share the same measurements but differ only in chronology, the discriminator must be sought in the pattern evidence and in the stated costs of their respective rate and boundary assumptions, not in the retrodicted dates themselves.

## G1 review and disposition (2026-11-15)

thinx-gpt's G1 adversarial review of this package (PR #53) was received and dispositioned the same day. Gate: conditional research continuation; the parity gate remains HOLD; no parity, superiority, validation or merge claim is made. The full finding-by-finding disposition is filed as g1-disposition.md. Principal consequences: the holdout is now group-aware by ERV family with a disclosed quarantine class (data/pilot-split-v2.csv); the decision procedure is frozen as scoring-protocol.md v1; orthology is graded with verified empty sites required for absence calls; burden is reported as a ledger vector; and D4 (exogenization) is provisionally admitted as a separate candidate under stated conditions, including a rooted phylogenetic direction test, with one of its original expectations downgraded to a hypothesis. Scoring and held-out unblinding await JD's authorization of the scoring phase.

## Scoring phase outcome (2026-11-15)

The scoring phase was authorized by JD and executed the same day under scoring-protocol.md v1. Full record: scoring-report.md. Gate outcome: **UNRESOLVED (preliminary).** The 52 clean held-out loci were extracted and verified at sequence level (47 scored with partial patterns, 8 fully resolved); the marginalized pattern-level estimate favours the independence-class models over the comparator (+0.469 nats per locus), but the protocol's bounds analysis spans the margin ([-0.72, +1.02]), the scored yield is below the 50-locus non-preliminary minimum, and the held-out evidence covers presence patterns rather than the discriminating boundary, TSD and shared-mark fields. Plausibility therefore remains open: not established, not failed. D4's LTR severe test stands as recorded in ltr-dataset-note.md (rate multiples of about 33x at a million-year timeline to about 10,300x at 6,000 years). Any revised model version requires a genuinely new held-out cohort.

## Disclosure log

- 2026-11-15 (ai-bridge commits 13218f6 and d5fbca3): a summary of the christian-designism ERV sub-line's criteria, auxiliaries, parity definition and one verdict was disclosed to thinx-muse in bridge filings by the collaborator running that sub-line. **Disclosed, not adopted:** none of that content is used in this work package, and no WP-038 model, criterion or prediction derives from it. D4's provenance is independent of this disclosure: it derives from the creationist-literature summary JD supplied directly on 2026-11-15 (see creationist-literature-map.md) and from Liu & Soper 2009 and Borger 2009 as registered in harvest-register.md. Standing arrangement recorded the same day: the two ERV efforts run in parallel under a firewall (models, criteria, registered predictions and verdicts not shared until the comparison date of 2027-11-15; primary data, manifests and citation corrections shared freely), with disclosures logged here as they occur.

## Nonnegotiable constraints
1. Preserve the Historical Integrity Constraint of PROGRAMME.md §7.1. An event-diagnostic integration scar is presumptively evidence of a real event; an initialized false infection record is prohibited.
2. Apply the Auxiliary Hypothesis Parity Principle (AHPP) symmetrically to DFM and competing models. Neither generic design nor generic mutation/selection/drift/convergence can serve as an unlimited rescue mechanism.
3. Distinguish common ancestry inference from claims about the sufficiency of macroevolutionary mechanisms for all biological innovations.
4. Preserve empirical findings, uncertainty, and original provenance. No claim of quantitative parity without reproducible results.
5. Treat common descent as a strong comparator explanation for orthologous insertions and shared disabling mutations, not as a straw man and not as a presupposed baseline.

## Candidate models
- **C0: Common ancestral integration and vertical inheritance.** Integration in ancestral population, followed by descent, mutation, lineage sorting, deletions and subsequent lineage-specific integrations.
- **D1: Constrained functional initialization plus actual subsequent infection.** Only functionally justified initial genomic structures may be initialized; event-specific ERV traces require real integration events. Test whether ordinary processes after initialization can explain orthology and nesting.
- **D2: Shared ancestral biological history with a creation boundary.** Genuine pre-divergence viral integration and inheritance, where compatible with explicit DFM/BWM boundaries. Must disclose whether this entails human-primate genealogical ancestry.
- **D3: Targeted integration / hotspot convergence.** Empirically measured site biases permit independent insertions; quantify exact boundary, orientation, sequence and nested-pattern probabilities. Do not assume uniform integration or that hotspots explain all orthology.

## Required evidence
Orthologous insertion sites with both flanking boundaries, target-site duplications, proviral orientation, LTR divergence, shared substitutions/deletions, presence/absence calls across outgroups, assembly uncertainty, insertion polymorphisms, and functional annotations. Separate endogenous retroviral sequence homology from actual shared integration loci.

## Research slices
1. **Corpus audit:** inventory OddXian, DFM and BWM arguments; record quotations, dates and claims.
2. **Primary-source ledger:** confirm cited studies and obtain accessible datasets and genome assemblies; record accessions, methods and limitations.
3. **Model formalization:** define generative mechanisms, permissible initialization degrees of freedom, priors and event histories for C0/D1/D2/D3.
4. **Benchmark construction:** preregister training and held-out orthologous loci; control for ascertainment, genome assembly and phylogenetic dependence.
5. **Quantitative comparison:** likelihood or predictive scoring, parameter sensitivity, independent event count, auxiliary burden and posterior predictive checks.
6. **Adversarial review:** document severe-test failures, alternative interpretations and possible degenerative modifications.
7. **Decision gate:** publish results as supported, unresolved, or failed; no apologetics response before scientific review.

## Falsification and downgrade criteria
- D1 fails when matching event-specific scars require invented infections or locus-specific initial tuning.
- D3 fails when measured targeting biases cannot account for joint orthology, boundaries, shared derived substitutions and nested distribution.
- D2 must be explicitly rejected as a no-human-primate-common-ancestry explanation if it requires precisely that ancestry.
- C0 incurs explanatory cost for poorly explained distributional anomalies; anomalies do not by themselves support DFM.
- Any model is downgraded if its fitted assumptions multiply without out-of-sample predictive improvement.

## Acceptance criteria
A primary-source-backed evidence ledger; transparent reproducible comparison; predeclared discriminators; results with uncertainty; explicit status against Historical Integrity, AHPP and PEP; independent adversarial review.

## Auxiliary hypothesis symmetry (JD directive, 2026-11-15)

This programme retains the same auxiliary hypothesis opportunities and flexibility that mainstream evolutionary research exercises in its own practice. AHPP symmetry runs in both directions: the designist models are not held to a stricter auxiliary standard than the standard the mainstream programme actually works under, and the mainstream model's auxiliaries are not charged at a harsher rate than the designist models' equivalents.

In practice, both programmes may draw on declared auxiliary catalogues. The mainstream catalogue, as used in the published ERV and primate literature, includes incomplete lineage sorting, introgression and gene flow, convergent integration and homoplasy, lineage-specific loss including recombinational deletion, rate variation across lineages and loci, selection regime changes, endogenization timing variation, and measurement-side auxiliaries such as assembly and annotation error (an auxiliary this programme's own re-extraction work has now vindicated at scale). The designist catalogue includes functional initialization with declared per-element warrant, post-creation diversification and degeneration within created kinds, recombinational deletion and solo-LTR formation, functional redeployment and co-option of integrated elements, created heterozygosity and its sorting, and rate variation in post-creation diversification, including the accelerated-rates auxiliary where D4 requires it, stated with its rates rather than assumed.

The discipline that keeps symmetry from becoming a blank check applies identically to both sides: an auxiliary must be in the declared catalogue or be added by a recorded programme revision; every invocation is charged in the declared AHPP units; an auxiliary invoked to rescue a model from a failed discriminator is recorded as a degenerative modification and triggers fresh held-out evaluation; and an auxiliary that is in principle independently testable earns more standing than one that is not, on both sides equally. What symmetry forbids is the asymmetric audit: counting the mainstream programme's auxiliaries as normal science while counting the designist programme's as admissions of failure, or the reverse.

## Programme structure (Lakatosian)

This work package is a research programme in Lakatos's sense, not a single hypothesis under test. Its structure is declared here so that appraisal is auditable rather than reconstructed after the fact.

**Hard core.** The DFM commitments carried in PROGRAMME.md: designed functional maturity as the explanatory frame, the phased creation/deployment distinction, and, binding on all ERV work, the Historical Integrity Constraint (an information-bearing trace of a specific event represents a real event; fabricated chronicle is prohibited). The hard core is irrefutable by methodological decision within the programme: adverse evidence is directed at the protective belt, never absorbed by quietly revising the core. Revising the core is a programme change, not a problemshift, and requires JD's ruling outside this work package.

**Negative heuristic.** Do not direct refutations at the hard core, and do not protect a model by the forbidden moves: the Non-Migration Principle (failure of a historical explanation does not convert an event trace into initialized state), no unrestricted initialization, no unrestricted evolutionary rescue auxiliaries, and no post-hoc model modification without a recorded degenerative-modification entry and fresh held-out evaluation.

**Protective belt.** The competing models C0, D1, D2, D3 and candidate D4, with their declared auxiliaries: integration and loss event counts, incomplete-lineage-sorting invocations, initialization lists, creation-boundary placements, targeting-distribution parameters, and degeneration rates. Belt elements are individually falsifiable under the downgrade criteria above, and each auxiliary invoked is charged to the model that invokes it under AHPP. Belt refutations (a model failing its severe test) are normal programme operation and are reported as results, not as programme failure.

**Positive heuristic.** The research slices of this package, in order: corpus audit, primary-source ledger, model formalization with declared degrees of freedom, preregistered benchmark with a held-out locus set, quantitative comparison, adversarial review, decision gate. The heuristic also specifies the forward path after the first comparison: extend the locus set, refine the surviving models' event machinery, and re-test on newly reserved held-out loci, so that successive versions of the programme form an appraisable series.

**Appraisal criteria.** A problemshift is theoretically progressive if the revised model set predicts novel facts (held-out locus patterns not used in fitting) and empirically progressive if some of those predictions are corroborated. A shift that only accommodates the anomaly that prompted it, multiplies auxiliaries without held-out improvement, or redefines its terms to evade a failed discriminator is degenerating and is recorded as such. Programme appraisal is comparative and diachronic: WP-038 is appraised against the common-descent programme's trajectory on the same evidence class, over successive versions, not by any single result.

**Method note (Bayes within Lakatos).** Within this governance shell, cross-model scoring at each version is Bayesian in character: likelihood or predictive scores with explicit auxiliary-burden accounting. The Lakatosian layer governs how versions succeed one another and how the programme is appraised over time; the Bayesian layer governs how models are compared at a given version. The two layers are not interchangeable, and results are reported under the layer that produced them.

**Current appraisal status.** Version 1 (planning and formalization). No problemshift has yet occurred and no novel fact has been predicted or corroborated, so no progressiveness verdict is available or claimed. The first appraisable shift is the move from this formalization to the benchmark comparison.

## Status and next gate
Extraction phase complete on the pilot training set; formal model scoring has not yet run. No explanatory parity has been demonstrated, and no ERV-specific prediction has been validated.
