# WP-038 Model Formalization (Slice 3)

Status: formalization draft for review. No dataset has been fitted; nothing in this document is an empirical result.

## Shared notation and evidence units

The unit of evidence is the **locus**: a candidate integration site characterized by (a) left and right flanking host sequence, (b) target-site duplication (TSD) where recoverable, (c) proviral orientation, (d) 5-prime and 3-prime LTR sequences and their divergence, (e) internal shared substitutions, deletions and disabling mutations, (f) presence/absence calls in human, chimpanzee, gorilla, orangutan and at least one Old World monkey outgroup, each with an assembly-confidence grade, and (g) functional annotation, if any.

Orthology is asserted from flanking sequence identity, never from internal viral homology alone. A locus is **shared-orthologous** when the same integration, identified by both boundaries and TSD, is present in two or more taxa. A **derived mark** is a substitution, deletion or disabling mutation inside the provirus that is shared by exactly the taxa carrying the locus.

Each model below is stated as a generative process: a declared initial state, a set of event types with rates or counts to be estimated, and the observations the process is required to produce. Auxiliary burden is counted in declared units: independent integration events, loss events, initialization choices, and free parameters. AHPP applies symmetrically: an auxiliary is charged to whichever model invokes it, and an auxiliary that can absorb any observation without cost is prohibited for all models.

## C0: Common ancestral integration and vertical inheritance

**Generative process.** On a fixed primate phylogeny, retroviral integrations occur in ancestral and terminal lineages as a point process. An integration in an ancestral population is inherited by descendant taxa unless removed by deletion or obscured by assembly failure. After integration, the provirus accumulates substitutions and deletions at host-like rates; the two LTRs, identical at integration, diverge independently, giving a locus-internal clock. Lineage sorting of insertion polymorphisms is permitted where the population genetics supports it.

**Declared degrees of freedom.** Phylogeny (fixed externally, not fitted to ERV data), per-branch integration counts, per-locus loss indicators, substitution rates (shared across loci by default), ILS invocations (each charged and each requiring a polymorphism case).

**Historical Integrity.** Satisfied by construction: every event-diagnostic trace corresponds to a real integration event in the model's own history.

**Discriminating expectations.** Shared-orthologous loci carry derived marks distributed on the phylogeny exactly as inherited characters; LTR divergence at a shared locus is consistent with the speciation time of the taxa sharing it; presence/absence patterns are nested up to counted losses and ILS cases.

**Costs and failure modes.** C0 is charged for distributional anomalies it cannot produce: a locus whose LTR divergence is far younger than the speciation node it is mapped to, or presence/absence patterns requiring loss counts well above the fitted deletion rate. Anomalies charge C0; they do not transfer support to any D model automatically.

## D1: Constrained functional initialization plus actual subsequent infection

**Generative process.** An initialized genome state at a declared creation boundary contains only structures justified independently of ERV evidence: functional elements required for coherent operation, each named in advance with its functional warrant. After the boundary, ordinary processes operate, including real germline retroviral infections, which produce real integration events with real scars. Any ERV-like structure present at the boundary must be either (a) a functional element with a stated non-viral function, or (b) absent. Event-diagnostic traces (matched boundaries, TSD, LTR pairs with divergence, shared disabling mutations) may not be initialized, because they represent specific events.

**Declared degrees of freedom.** The initialization list is closed and preregistered: each initialized ERV-like structure costs one initialization choice and must carry an independent functional justification recorded before locus comparison begins. Post-boundary integration events are counted exactly as in C0. No per-locus initialization is permitted after seeing the data; adding one reopens preregistration and is recorded as a degenerative modification.

**Historical Integrity.** This is the binding constraint on D1. D1 fails at any locus where matching C0 requires an event-diagnostic trace at the boundary, because initializing that trace would fabricate an infection record.

**Discriminating expectations.** D1 predicts a sharp partition: loci explainable by post-boundary infection (lineage-restricted, young LTR divergence, no cross-boundary orthology of event-diagnostic traces) versus loci it cannot claim. In particular, D1 predicts that no shared-orthologous locus with shared derived marks spans the creation boundary, unless the boundary is placed before the relevant taxa diverge, in which case D1 collapses toward D2 and must be re-scored as D2.

**Costs and failure modes.** D1 fails per WP-038 downgrade criteria when matching event-specific scars require invented infections or locus-specific initial tuning. Its auxiliary burden is the size of its initialization list plus post-boundary event counts.

## D2: Shared ancestral biological history with a creation boundary

**Generative process.** As C0 for the period after a declared boundary point in the phylogeny, with genuine viral integrations in genuinely ancestral populations. The model's distinctive content is where the boundary is placed and what it severs.

**Declared degrees of freedom.** Boundary placement (one choice, stated in advance), plus the C0 event machinery below the boundary. The model must disclose, as a scored output and not a footnote, whether its boundary placement entails genealogical common ancestry of humans and other primates for the loci under study.

**Historical Integrity.** Satisfied for all post-boundary and pre-boundary real events; the boundary itself may not be used to convert an event trace into an initialized state (Non-Migration Principle).

**Discriminating expectations.** Identical to C0 for loci below the boundary. D2 therefore earns no ERV-specific credit over C0 for those loci; its ERV content is the claim that the shared history is real but bounded. Per WP-038 criteria, D2 must be explicitly rejected as a no-human-primate-common-ancestry explanation if its required boundary placement entails precisely that ancestry.

**Costs and failure modes.** D2's burden is the boundary assumption plus any theological or systematic cost its disclosure surfaces. ERV evidence alone cannot distinguish D2 from C0 below the boundary; claiming otherwise is a scoring error this programme will not make.

## D3: Targeted integration and hotspot convergence

**Generative process.** Independent integrations in separate lineages land at the same locus because integration is site-biased. The bias is not a free story: it is a probability distribution over sites estimated from experimental integration data (HIV/MLV target-site selection studies and endogenous retrovirus integration preferences), parameterized by measurable genomic context (chromatin state, gene density, sequence motifs, DNase hypersensitivity).

**Declared degrees of freedom.** The targeting distribution's parameters, estimated from experimental data only, never fitted to the orthology pattern it is asked to explain. Each claimed coincident locus costs the joint probability of independent insertion at the same site, in the same orientation, producing the same TSD, followed by independent accumulation of the same derived marks.

**Historical Integrity.** Satisfied: the events are real, merely independent.

**Discriminating expectations.** D3 predicts coincidence rates that decay steeply with the specificity of the match: same approximate region is cheap; same exact boundary plus orientation plus TSD is expensive; same boundary plus shared internal disabling mutations is, under any measured targeting distribution, the severe case, because targeting biases act on integration sites, not on post-integration mutation patterns. D3 also predicts that coincidence frequency correlates with measured hotspot strength across loci, a regression the benchmark can test directly.

**Costs and failure modes.** D3 fails when the measured targeting distribution, applied honestly, cannot produce the joint orthology pattern at rates compatible with the observed counts. Yohn et al. 2005 cuts both ways and is the calibration anchor: PTERV1 shows independent concurrent infection is real and common (about 95.8 percent of sites non-orthologous between chimpanzee and gorilla), which establishes the base rate of independent integration, and by the same token shows that genuinely independent integrations almost never land at orthologous loci, which is the rate D3 must beat for shared loci.

## D4: Exogenization, created mobile elements with post-Fall escape (candidate, added 2026-11-15)

**Provenance.** Added from the creationist-literature considerations supplied by JD on 2026-11-15 (see creationist-literature-map.md, section 2). Candidate status: it enters the comparison set only on JD/GPT review of this formalization.

**Generative process.** Genomes are initialized with beneficial mobile regulatory elements: created transposition-capable elements whose integration machinery, targeting and regulatory roles are designed. In a post-Fall degeneration phase, elements accumulate disabling mutations, and some escape cellular control to become exogenous infectious retroviruses, which then run ordinary infection and endogenization cycles. Direction of derivation is host-to-virus for the exogenous forms.

**Declared degrees of freedom.** The initialized element families and their designed functions (closed list, preregistered, charged per family as in D1); the degeneration timeline and the mutation and transposition rates it requires; escape events (counted per exogenous lineage claimed). Rates assumed to fit LTR divergence and shared-mark patterns inside a compressed timeline are scored quantities: D4 must state the per-generation rates it needs, and AHPP compares them against the rates C0 needs over its timeline.

**Historical Integrity.** Binding in full. Orthologous boundary structure, TSDs, LTR divergence and shared disabling mutations are event traces; D4 must supply real transposition or infection events for them within its own history. It may not initialize a shared disabling mutation as a design feature, because a shared inactivation is the trace of a mutational event or of common inheritance, and claiming it as initialized design is precisely the fabricated-chronicle move the constraint prohibits.

**Discriminating expectations.** Exogenous retrovirus phylogenies root within or beside endogenous element diversity; the least degraded endogenous copies are the oldest families rather than the youngest insertions; element families show design coherence (controlled targeting, regulatory integration) with infectious behaviour as the derived state. LTR divergence at shared loci must be fittable inside the declared degeneration timeline at stated rates.

**Costs and failure modes.** D4 fails if fitting observed LTR divergence and shared derived marks requires per-generation rates far outside measured ranges, if exogenous phylogenies nest inside endogenous diversity in the virus-to-host direction instead, or if its initialized-family list grows locus by locus after seeing the data. Its timeline compression is its most exposed quantity and the benchmark reports it explicitly.

## Comparative scoring rules

1. Score joint patterns per locus, never isolated similarities.
2. Fit on the training locus set only; report held-out predictive performance as the headline comparison.
3. Charge every auxiliary in the declared units of the model that invokes it; publish the burden table alongside any likelihood or predictive score.
4. A model that must be modified after seeing held-out results is recorded as degeneratively modified, and the modification is scored as a new preregistration.
5. Where quantitative scoring is not defensible for a locus class, report the qualitative discriminator and mark the locus class unresolved rather than forcing a number.
6. Burden is reported as a ledger vector with separated dimensions (events; boundary placements or ancestral parameters; initialized families or elements; rate, population and ascertainment parameters; catalogue auxiliary invocations), never as a single equal-weight count in any headline. A coding-length sensitivity analysis accompanies the ledger (G1 disposition F6). The frozen decision procedure is scoring-protocol.md v1.

## G1 review amendments (2026-11-15; see g1-disposition.md)

- **C0 ledger.** The comparator's protective belt (insertion polymorphism, incomplete lineage sorting, loss including recombinational deletion, recombination and gene conversion, orthology uncertainty, ascertainment) is entered as declared auxiliaries in its burden ledger. Discordance is not folded into a single charged deletion.
- **D1 warrant discipline.** Functional initialization warrants must be preregistered independently of the ERV patterns under test. A functional annotation alone does not warrant a specific initialized integration scar.
- **D3 transferability.** HIV and MLV integration preferences are analogues, not calibrations, for ancient germline ERV families. Any D3 likelihood must state its transferability assumptions with uncertainty and an effective target-space size per family. Shared derived mutations acquired after integration are priced independently of targeting: targeting acts on integration sites and cannot be charged for post-integration marks; an exact shared disabling mutation under D3 requires its own independently priced mechanism.
- **D4 provisional admission and correction.** D4 is provisionally admitted as a separate candidate (GPT G1 recommendation; JD approval recorded in g1-disposition.md), conditional on: a rooted phylogenetic direction test with outgroups and model uncertainty for the host-to-virus claim; predeclared chronology, generation-time and mutation and substitution rate distributions; LTR conversion and recombination effects modelled alongside divergence; and endogenous-to-exogenous emergence distinguished from later ordinary reintegration. Correction to the D4 text above: the expectation that the least degraded endogenous copies are the oldest families is not entailed without a specified degeneration process and is downgraded from a discriminating expectation to a hypothesis pending that specification. LTR divergence under a compressed timeline remains a severe test but is not sufficient alone; it is combined with boundary, TSD, shared-mark and direction-of-derivation evidence.

Human-Curated, AI-Enabled (HCAE)
