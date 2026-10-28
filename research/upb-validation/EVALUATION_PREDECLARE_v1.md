# DFM U-Pb evaluation predeclare v1 (RATIFIED)

Version: v1 (filed, RATIFIED). Ratified by the Principal Operator on
2026-10-28: "Ratify v2 with the rubric-vocabulary fix". This is the
ratified text of the predeclare draft v2 (amended 2026-10-28 per the
program's drift audit and the Principal Operator's goal statement of the
same date), with one change applied at ratification: the
rubric-vocabulary fix, under which outcome labels follow the RCIM-004
rubric's own vocabulary ("adequate in scope" for a positive outcome,
"disfavored in scope" for a negative outcome, INDETERMINATE for
indistinguishability; sections 1 and 5.4). The v2 amendments are scope
and language amendments: the evaluation sequence and the D1 to D13
decision mechanics are unchanged in substance from draft v1. Working
drafts v1 and v2 are preserved in the program's local record.
Date: 2026-10-28 (draft v1); amended 2026-10-28 (draft v2); ratified and filed 2026-10-28
Program: designed-functional-maturity, radiogenic / U-Pb validation track
Parent documents: DFM_UPb_Validation_Protocol_v0.1.md; EMPIRICAL_GATE_v0.2.md;
OBSERVATIONAL_ACQUISITION_DECISION_v0.5.md (locked methodological decisions)
Cohorts: evidence/manzano/freeze-record.md; evidence/alaska/freeze-record.md
Machinery: research/upb-validation/{upb_baseline.py, upb_covariance.py,
concordia_comparator.py, rci_fitter.py, comparison_harness.py}, merged by PR #48
Authorization for this draft: Principal Operator, 2026-10-28: "Draft the
evaluation predeclare". Authorization for the v2 amendment: Principal
Operator, 2026-10-28, "Proceed", confirming the proposal to fold his goal
statement into the purpose section, apply the re-scope edits from the drift
audit, and return the amended draft for ratification as one package. This
draft was prepared without fitting any real data. Ratification: Principal
Operator, 2026-10-28: "Ratify v2 with the rubric-vocabulary fix".

Human-Curated, AI-Enabled (HCAE)

## 1. Purpose and status

Governing framing. The Principal Operator stated the goal of this program
on 2026-10-28, in his own words, and this predeclare is written under that
statement:

"a plausible framing (radiometric parent-daughter pre-seeded components
that enable an intelligent life-friendly ecosystem) with viable empirical
substantiation"

Assessment track. Under that framing, this program sits on Track A,
plausibility, in the assessment hierarchy of RCIM-002 (Track A governed by
DFM-PAM-001). This evaluation does not seek Track B superiority over the
conventional model, and no result it can produce establishes provenance:
functional participation and predictive consistency do not, separately or
together, show how the inventoried state originated (RCIM-001, claim and
failure ledger). The question this evaluation answers is narrower: whether
the shared-initials radiogenic model, with its parameters fitted only on
the calibration cohort and frozen, remains predictively consistent with
held-out U-Pb measurements, at plausibility grade.

What this evaluation is. This document is the predeclare for a preliminary
predictive-consistency evaluation. It sits between the protocol's G1 gate
(diagnostics, identifiability, negative controls, baseline cross-check) and
its G3 gate (the preregistered held-out evaluation). It is not the G3
evaluation, because G2 as the protocol specifies it, externally constrained
RCI parameters frozen before held-out evaluation, has NOT occurred: no
independent constraint set for the initial ratios exists in the record, and
the initials used here are fitted to the calibration cohort's ratios
(section 1A, narrowing record). The preregistered PEP evaluation remains
contingent on an independent-constraint work package whose constraints are
to be derived from the ecosystem-requirement side of the framing, that is,
from radiogenic heat and mass budgets and the conditions the life-friendly
ecosystem requires, rather than from the isotope ratios under test. The
named starting point for that work package is the repository's Track A heat
line and work packages DFM-PAM-003, DFM-PAM-004, and DFM-PAM-005.

Outcome ceiling. Outcome labels follow the vocabulary of the RCIM-004
outcome rubric. The maximum outcome this evaluation can return is the
rubric's positive tier, "adequate in scope", expressed at plausibility
grade as CONSISTENT with the framing. A result in which the two models
are not distinguished on this data is reported as INDETERMINATE
(indistinguishability, not parity). A negative outcome carries the
rubric's own negative label, "disfavored in scope", expressed at
plausibility grade as INCONSISTENT with the framing. No outcome of this
evaluation may be reported as "PEP supported", as a parity verdict on the
full hypothesis, or as substantiation of any specific initial inventory.
Decision D1's deferral of inventory claims is a direct consequence of the
governing framing: the framing is substantiated, if at all, by the
portfolio below, and this evaluation tests none of its inventory specifics.

Substantiation portfolio. Viable empirical substantiation of the framing
is a portfolio, and no single leg of it is sufficient alone: (i) the
functional side, radiogenic heat and mass budgets and their consistency
with the ecosystem the framing invokes; (ii) cross-system consistency
checks beyond U-Pb; and (iii) this U-Pb predictive-consistency evaluation.
This predeclare governs leg (iii) only. A favorable result here leaves the
framing's substantiation incomplete until the other legs are assessed; an
unfavorable result counts against the shared-initials family specifically,
at the grade stated above.

Status. This document is RATIFIED. It was ratified by the Principal
Operator on 2026-10-28 and took effect on ratification of the decision
list in section 9, as amended in v2 and with the rubric-vocabulary fix
(section 9 preamble).

On ratification, this predeclare freezes, for this evaluation only:

- the evaluation sequence (section 2), with no deviations permitted;
- the anchoring treatment for the RCI identifiability problem (section 3);
- the numeric parameter bounds (section 4);
- the comparison statistics, penalty, aggregation, and decision rule
  (section 5), including the margin-locking rule;
- the data rulings (section 6);
- the evaluation code pin: master commit
  12906ecfdc4965032a56bd9b860ec733b7a26197 of jdlongmire/designed-functional-maturity.
  Both freeze records pinned the admission tooling at 85e779b3 and require the
  predeclare step to re-pin the code commit before fitting; ratification of
  this predeclare performs that re-pin. Any later change to the evaluation
  code requires a ratified amendment and a new pin before use.

Before this ratification, no fitting of any real cohort data was authorized
anywhere in this program; fitting is now authorized only in the sequence
and under the rulings this predeclare freezes. Both cohorts are already frozen at the cohort level by their
own freeze records; the overall empirical gate (EMPIRICAL_GATE_v0.2) remains
NOT FROZEN. Ratification of this predeclare freezes the bounds, metrics, and
anchoring treatment for this narrowed evaluation only. It does not complete
gate G2, does not freeze the empirical gate for the preregistered PEP
evaluation, and does not advance this evaluation to G3.

Standing caveats, carried from the protocol, the gate, and both freeze
records, and binding on every report produced under this predeclare:

- No empirical plausible explanatory parity (PEP) is claimed by anything in
  this program to date, and this evaluation cannot by itself establish PEP:
  the protocol requires nuclear, thermal, mineralogical, and cross-system
  obligations to be assessed as well (protocol, Failure and interpretation
  rules; gates G4). Under the v2 re-scope, the stronger statement also
  holds: no outcome of this evaluation may be reported as "PEP supported"
  at all; the outcome ceiling of this section governs every report.
- Failure to distinguish the RCI model from conventional chronology is NOT
  evidence of empirical parity (EMPIRICAL_GATE_v0.2, item 7). Equal predictive
  performance must be reported as observational equivalence /
  indistinguishability, nothing more (protocol, Failure and interpretation
  rules).
- Synthetic benchmarks in this program are software checks, not measured
  isotope evidence.

## 1A. Narrowing record (v2 amendment)

This section is the on-the-record account of how this evaluation is
narrower than the founding documents specify. It answers the drift audit of
2026-10-28 (drift-audit-2026-10-28.md). Each item names the founding
requirement, what this evaluation does instead, and the consequence for
what its results may be taken to mean. Ratifying this predeclare ratifies
this record as a versioned amendment to RCIM-002, RCIM-004, and the
Validation Protocol (section 9); the narrowing is adopted openly, not
absorbed silently.

N1. The generator is absent. The founding documents define the DFM model
as a generative initial-state rule, R0 = G(Phi, L, B), a shared reservoir
state with geochemical partition rules (RCIM-001, Gate B; RCIM-002, model
M2). No reservoir state, partition rule, or functional input exists in the
current pipeline. The machinery under test (rci_fitter.py) is a
concordia-family parameterization with shared initial ratios. Consequence:
this evaluation tests a generic shared-initials model, not the distinctive
DFM claim that function constrains inventory.

N2. The initials are fitted to ratios, not externally constrained. The
founding documents fix RCI parameters from independent, non-target
functional, mineralogical, and thermal observations before isotope
outcomes are revealed (RCIM-001, Gates A and B; protocol, hypothesis H2
and gate G2). This evaluation fits the shared initials to the Manzano
calibration cohort's ratios and freezes the fitted values. The gate's
literal requirement, parameters constrained independently of held-out
ratios, is satisfied for the holdout; the calibration-side independence
the protocol intends is absent. Consequence: hypothesis H1 is addressed
only in weakened form, and H2 is not addressed at all.

N3. The comparator is narrower than specified. RCIM-004 requires the
conventional comparator to carry common-Pb treatment, closure, and
Pb-loss or mixing events where independently warranted, and forbids
comparison against an idealized straw model. The built comparator is a
per-sample concordia age fit. Neither side models common Pb beyond the
source's correction of the admitted ratios, U-series disequilibrium, or
Pb loss. The absence is symmetric, and discordant holdout analyses
therefore have no modeled home on either side. Consequence: the
comparison is valid only at the level of the corrected-ratio likelihood
both sides consume.

N4. The Th-Pb chain is out of scope. RCIM-004 is a U-Th-Pb pilot whose
test T3 is Th-232/Pb-208 joint consistency. The frozen admission schema
carries only the Wetherill pair (r68, r75), so the third chain left the
design during acquisition gating, before this predeclare existed and
without a ratified scope change. Consequence: no cross-chain consistency
claim of any kind may be drawn from this evaluation.

N5. The holdout is from the same laboratory. The protocol's split design
separates by geological unit and by analytical laboratory, and asks for an
external laboratory dataset where eligible data exist. The Alaska holdout
is disjoint from the calibration cohort in release, region, geological
units, and samples, but it comes from the same laboratory and method
(Stanford-USGS SHRIMP-RG) as the Manzano calibration cohort.
Consequence: this evaluation tests geological generalization only, not
laboratory generalization, and any shared laboratory systematic is common
to both sides.

N6. Calibration rests on a single sample. The protocol contemplates
multiple geological contexts before fitting. The calibration cohort is one
sample (K05-ABO-1r) from one unit from one laboratory; with one unit, the
shared initials are shared across 24 analyses of a single rock, and their
transport to other units is the untested assumption the holdout scoring
examines (section 7). Consequence: the calibration fit establishes
ingestion and parameter estimation at sample level, and nothing more.

N7. Gate position. Protocol gates run G1 (diagnostics), G2 (externally
constrained parameters frozen), G3 (preregistered held-out evaluation),
G4 (cross-system tests). This evaluation performs G1-grade diagnostics and
a held-out predictive scoring, but G2 as specified has not occurred (item
N2) and G4 is untouched. It therefore sits between G1 and G3, and its
outcome ceiling (section 1) follows from that position.

## 2. Evaluation sequence

The evaluation runs in exactly this order. No step may be reordered, repeated
with altered settings, or supplemented with undeclared runs on the holdout.

Step (i) - Calibration fit. Fit the Manzano calibration cohort with the
shared-parameter RCI fitter (rci_fitter.fit_unit): sample K05-ABO-1r, Blue
Springs metarhyolite, 24 admitted analyses, frozen cohort SHA-256
8bf4ebbea63ea2c99f9304bc66e0f54b5912a029438b3dbe50de4cae259f9b65. The single
sample is the fitting unit; the initial ratios (a206, a207) are shared across
all 24 analyses of the sample, never per analysis and never per grain (gate
item 6; decision document, locked decision 3). The fit uses the anchoring
treatment ratified under D1 and the bounds ratified under D2 and D3.

Step (ii) - Freeze of fitted parameters. Record the fitted shared parameters
(the canonical representative under D1, together with its identifiability
flag), the fitted calibration age, chi-square, log-likelihood, parameter
count, degrees of freedom, and the full fitter output. From this moment the
shared parameters are frozen for this evaluation. The margin M is also locked
at this point, by the rule in section 5.4, using only calibration-side
(Manzano) quantities. No Alaska data of any kind has been accessed for fitting
purposes before this point; the Alaska cohort file is first opened by the
scoring code in step (iii).

Step (iii) - Holdout scoring, exactly once. Score the Alaska holdout with the
frozen shared parameters: 65 samples, 846 admitted analyses, frozen cohort
SHA-256 9c9bef2d48af043a339e37bf86d211796f2269df637461462c7bc346555f74ef.
Each sample is scored with rci_fitter.fit_unit with fixed_initials set to the
frozen pair, so the only fitted quantity per sample is its closure age
(parameter count 1 per sample on the RCI side at scoring). The comparator is
run on the same samples in step (iv). The RCI scoring pass over the holdout
runs exactly once, end to end, under the ratified settings. A scoring run
that fails partway for computational reasons (crash, I/O error) before
producing any per-sample result may be restarted unchanged; a run that has
produced per-sample results may not be rerun with altered settings.

Step (iv) - Conventional comparator. Run the independent conventional
comparator (concordia_comparator.fit_concordia_age) on the Manzano sample and
on all 65 Alaska samples, under its own parameter accounting (1 parameter per
sample: the concordia age; section 5.3). The comparator is independent of the
RCI implementation (it shares no fitting internals with upb_covariance.py or
rci_fitter.py) and consumes exactly the same admitted, corrected ratios,
published uncertainties, and published correlations as the RCI side (gate
item 5: same accepted measurements and error model).

Step (v) - Report. Produce the evaluation report required by section 8 and
gate item 7.

Amendment rule. Any change to the sequence, bounds, statistics, data rulings,
or code after step (iii) has begun voids the run: the holdout is considered
spent for that configuration, and a further scoring attempt requires a
ratified amendment that states what was seen and why a new run is justified.
Changes before step (iii) begins require a ratified amendment recorded the
same way as this predeclare. There are no silent amendments.

Bound-contact check (part of steps (i) and (iii)). If any fitted age or
initial ratio lands exactly on a ratified bound, that fact is reported for
the affected unit, because bound contact changes the meaning of the fit (and,
at scoring, can break the translation-invariance the anchoring treatment
relies on; see section 3.2).

## 3. The anchoring decision

### 3.1 The problem, exactly as the machinery states it

The RCI model, in the form the protocol states it and rci_fitter.py
implements it, predicts for a unit of closure age t with shared initial
ratios a206 = D206*(0)/P238(0) and a207 = D207*(0)/P235(0):

  R68(t) = (a206 + 1) exp(lambda238 t) - 1
  R75(t) = (a207 + 1) exp(lambda235 t) - 1

The fitter's module docstring records, and its test suite verifies
(test_translation_identity), the exact identity: for any shift dt, replacing
every age t by t + dt and each initial a by (a + 1) exp(-lambda dt) - 1
leaves every prediction unchanged. With the initials free and every unit's
age free, the likelihood is therefore exactly invariant under a uniform
translation of all ages. Age and shared initials are not separately
identifiable, at unit level or at group level. This is the protocol's own
warning in exact form: "If a206 and a207 are free for each sample, time and
initial inventory are not identifiable" (protocol, Models and
identifiability). Sharing the initials across units (gate item 6) removes
per-sample tuning, which the protocol declares a failure mode, but it does
not remove the single global translation direction.

What is and is not affected:

- Invariant along the family: chi-square and log-likelihood of any fitted
  unit or group, and therefore every comparison statistic built only from
  them (subject to the bound-contact caveat in section 2).
- Not invariant: the reported age of every unit, the reported values of
  a206 and a207 themselves, any comparison of RCI ages against comparator
  ages or published ages, and any physical interpretation of the initials as
  a measured initial daughter inventory.

The fitter, unconstrained, already handles this honestly: it returns the fit
statistics plus a deterministic representative of the equivalence family
(the minimum-initial-inventory member, obtained by translating the optimum
until the first initial ratio reaches zero), flagged
"unanchored_translation_degenerate". That convention is a reporting rule,
not identification, and the fitter says so.

### 3.2 Option (a): fix the initials from an independent common-Pb evolution model

The conventional candidate is the Stacey and Kramers (1975) two-stage
terrestrial Pb evolution model, which gives common-Pb isotope composition as
a function of time. Assessment:

- Wrong quantity without further machinery. Stacey-Kramers models common-Pb
  composition (ratios to 204Pb). The RCI initials are initial radiogenic
  daughter-to-parent ratios at closure. Converting one to the other requires
  a full reservoir history: primordial composition, stage boundary, and
  reservoir 238U/204Pb and 235U/204Pb evolution from Earth formation to the
  unit's closure. None of that is in the admitted data or the repo documents.
- Circularity, two layers. First, a Stacey-Kramers model age takes a
  candidate age as an input; here age is a fitted unknown, so the anchor
  would have to be solved jointly with the quantity it is meant to pin.
  Second, the model's stage parameters were calibrated against conventionally
  dated material: anchoring RCI initials to it imports the conventional
  framework into the RCI side of a comparison whose purpose is to test RCI
  against that framework. Agreement would be partly built in.
- Freeze breach. The admitted cohort schema (gate input schema) carries no
  per-analysis 204Pb measurement or common-Pb composition fields; the
  admitted ratios are already 204Pb-corrected by the source. Computing
  per-sample evolution-model initials would require stepping outside the
  frozen admitted cohorts to unadmitted source fields and correction
  internals.
- Effect on identifiability if it were done: it would identify age and
  initials, at the cost of making both conditional on the evolution model.

Verdict: not usable as the primary anchor for this evaluation.

### 3.3 Option (b): constrain the initials to a stated numeric prior box, with sensitivity analysis

Assessment:

- A box truncates the equivalence family; it does not identify anything
  inside it. The likelihood is exactly flat along the family segment inside
  the box, so fitted ages and initials remain non-identified; only the
  segment endpoints move. Anyone reporting a point estimate of age or
  initials under a box alone is reporting a convention.
- Combined with a predeclared representative rule (the fitter's canonical
  minimum-inventory representative) and a predeclared sensitivity analysis
  that re-expresses every non-invariant reported quantity across the
  feasible family segment inside the box, option (b) supports fully honest
  reporting: invariant statistics as results, non-invariant quantities as
  ranges.
- Information imported from outside the data: only the two box endpoints,
  which are judgments. Section 4 states what justification exists for the
  proposed endpoints and where it runs out.
- Effect on the comparison: none on fit statistics (invariant); the
  sensitivity ranges attach to RCI ages wherever they are reported next to
  comparator ages.

### 3.4 Option (c): reparametrize so the degenerate direction is removed by construction

The fitter's structure permits this. Define per-ratio apparent-age offsets
u = ln(1 + a206)/lambda238 and v = ln(1 + a207)/lambda235. A unit's
predictions are then exp(lambda238 (t + u)) - 1 and exp(lambda235 (t + v)) - 1:
the data identify the two combinations (t + u) and (t + v) per unit, never t,
u, v separately. Sharing initials across units is the statement that u and v
are common, which is exactly what makes relative ages between units
identifiable in a group fit.

- Reparametrization creates no information. It does not identify age or
  initials; it makes the null direction impossible to overlook and defines
  the evaluation's estimands as the identifiable quantities: fit statistics,
  relative age differences, and the offset difference (v - u).
- Cost: none to any fit statistic. The physical reading of the initials as
  an initial inventory is deferred, not denied: it becomes available only
  when an independent constraint set exists (option (d)).
- Effect on the comparison: the primary comparison (predictive
  log-likelihood with parameter penalty) is untouched. Age-level comparison
  is reported in identifiable terms or as representative-plus-range under
  option (b)'s sensitivity rule.

### 3.5 Option (d): the anchor the documents themselves imply

The documents consistently require the RCI parameters to be constrained
independently of the ratios being fitted: gate item 6 ("constrained
independently of held-out ratios"), the protocol's calibration section
("Record zircon U/Pb partitioning and common-Pb behavior with independently
measured bounds"), hypothesis H2 (independent functional/mineralogical
constraints narrowing admissible initial inventories), and gate G2
("externally constrained RCI parameters frozen before held-out evaluation").
The protocol also requires a null unconstrained initial-inventory model to be
run as a demonstration of nonidentifiability (protocol, Predictive outputs
and metrics, comparator (b)); the fitter's unanchored mode is that
demonstration.

However: no numeric independent constraint set exists anywhere in the current
record. Both freeze records state explicitly that initialization parameter
bounds are not frozen and that no document declares them. Option (d) is the
program's intended long-term resolution, but it supplies no numbers today,
and this predeclare may not invent them.

### 3.6 Recommendation (advice; the decision is the Principal Operator's)

RECOMMENDED (decision D1): adopt the identifiable-estimand evaluation, which
is option (c) as the frame with option (b) as its numerical enclosure:

1. The evaluation's primary results are the family-invariant statistics of
   section 5 (predictive log-likelihoods, chi-squares, and their penalized
   difference). These need no anchor and are unaffected by the degeneracy.
2. For holdout scoring, the shared initials are frozen at the value fitted
   on the calibration cohort and expressed as the fitter's canonical
   minimum-inventory representative, labeled in every output as a
   representative of an equivalence family, not an estimate of an initial
   inventory. (Scoring statistics per sample are family-invariant provided
   no fitted age contacts a bound; the section 2 bound-contact check
   verifies this.)
3. Every non-invariant quantity that is reported (per-sample RCI ages, the
   initials themselves) carries the family sensitivity range computed over
   the feasible segment inside the ratified initials box (D2).
4. No claim in this evaluation concerns the absolute value of the initial
   inventory or the absolute RCI age scale. Such claims are deferred until
   an independent constraint set of the kind option (d) describes exists and
   is frozen by a later predeclare. This deferral is required by the
   governing framing itself (section 1): the framing claims pre-seeded
   inventories, so an evaluation that cannot identify any inventory cannot
   substantiate that part of the framing, and must not be read as doing so.
5. Option (a) is rejected for this evaluation (circularity and freeze
   breach, section 3.2).

Reasons: this is the only treatment that (i) respects the protocol's and
gate's requirement that parameters not be tuned to the data they are scored
on, (ii) imports no unexamined external model into either side, (iii) keeps
the holdout genuinely out-of-sample, and (iv) reports exactly what the data
identify, no more.

### 3.7 Commensurability with the conventional comparator

Where the two sides are commensurate, by construction: identical admitted
corrected ratios, identical published uncertainties and correlations,
identical decay constants (section 4.4), identical age bound (D3), and a
likelihood of the same form (correlated-residual / Mahalanobis; gate item 5).
The comparator's common-Pb handling is inherited from the source's 204Pb
correction of the input ratios, which is the same input the RCI side
consumes, so the treatment is symmetric at the level of the data.

The models are nested at a boundary: the conventional model is exactly the
RCI model with both initials fixed at zero. Two consequences are stated
plainly. First, on any data both sides fit, the RCI chi-square can only match
or beat the conventional chi-square; that is why the only comparison that
carries weight is out-of-sample (frozen initials on the holdout) with a
parameter penalty
(section 5), and why no fitted-data comparison is evidence of anything.
Second, the comparator's initials are not "measured zero"; they are a
structural assumption of the conventional model, just as the RCI initials
are the RCI model's substantive free quantities. The parameter accounting
in section 5.3
charges each side for exactly the freedom it uses.

Where commensurability fails, stated plainly: absolute ages. Comparator ages
are absolute within the conventional model. RCI ages under the recommended
anchoring treatment are representative-relative (section 3.6). Any table
that places them side by side must carry the RCI family sensitivity range
and the identifiability flag; a bare numerical age difference between the
two sides is not a meaningful statistic in this evaluation and must not be
reported as one.

## 4. Parameter bounds

Every bound below is PROPOSED, not frozen. Ratification of the corresponding
decision in section 9 freezes it for this evaluation. Sources of justification
are limited to: the protocol, the gate, the decision document, the freeze
records, the machinery's actual parameter definitions and defaults, and the
parameter ranges the PR #48 synthetic tests actually exercised.

### 4.1 RCI side: shared initial ratios a206 and a207

- PROPOSED bound, each of a206 and a207: [0, 1.0] (decision D2).
- Lower bound 0: structural. The fitter requires the lower bound to be
  nonnegative (initial_bounds validation in rci_fitter.py), and a negative
  initial daughter-to-parent ratio has no physical reading in this
  parameterization.
- Upper bound 1.0: judgment, with the following support and no more. The
  synthetic validation exercised true initials of 0.02, 0.03, 0.04, 0.07, and
  0.09 (test_rci_fitter.py; comparison_harness.py standard cases), and
  optimizer starting values up to 0.3. An initial ratio of 1.0 (initial
  radiogenic daughter equal in amount to present parent) is about 11 times
  the largest exercised true value and is already extreme for the quantity.
  No repo document declares any numeric bound; the machinery's placeholder
  default (DEFAULT_INITIAL_UPPER = 10.0 in rci_fitter.py) is explicitly
  marked there as not a frozen program value.
- What this bound does and does not do: it encloses the family segment used
  for the section 3.6 sensitivity reporting and prevents the optimizer from
  wandering to implausible inventories. It does not identify the initials
  (section 3.3).
- Alternative the principal may choose instead: [0, 10.0] (the machinery
  placeholder). Trade-off: a wider box lengthens the reported family
  sensitivity ranges and admits inventories with no support anywhere in the
  exercised range; a narrower box (for example [0, 0.3], the largest
  exercised starting value) risks truncating a genuinely large inventory
  without evidence for doing so. If the principal declines both, the upper
  bound is a value he must set; the trade-off is the one just stated.

### 4.2 RCI side and comparator side: closure ages

- PROPOSED bound, every fitted age on both sides: [0, 4.6e9] years
  (decision D3).
- Justification: 4.6e9 years is the machinery default max_age_years in both
  rci_fitter.py and concordia_comparator.py. The synthetic tests exercised
  ages from 1.0e8 to 4.0e9 years (recovery at 100, 500, 800, 1000, 1200,
  1500, 2000, and 2500 Ma; the translation-identity test at 4000 Ma). The
  bound is a code default, not a value declared by the protocol or the gate;
  it is ratified here as a program value if D3 passes.

### 4.3 Comparator side: remaining parameters

- The conventional comparator fits exactly one parameter per sample, the
  concordia age (concordia_comparator.parameter_count). Its initial ratios
  are fixed at exactly zero by the model's definition; that is a structural
  assumption, not a bound, and it is charged for in the parameter accounting
  (section 5.3) by the contrast with the RCI side's two additional shared
  parameters.
- There are no other fitted parameters on the comparator side.

### 4.4 Held fixed, not fitted (both sides)

- Decay constants: Jaffey et al. (1971) central values as coded in
  upb_baseline.py (half-lives 4.4683 Ga for U-238 and 0.70381 Ga for U-235),
  shared by both sides. PROPOSED treatment (decision D4): proceed with these
  fixed central values and declare the limitation. The protocol's calibration
  section asks for decay constants with stated uncertainty and provenance
  and points to IUGS-IUPAC uncertainty budgets; the machinery propagates no
  decay-constant uncertainty. Because both sides use identical constants, the
  comparison between them is internally consistent; absolute age accuracy
  (where reported, on the comparator side) carries this limitation. The
  alternative is to halt the evaluation until uncertainty propagation is
  implemented.
- Per-analysis uncertainties and correlations: as published and as converted
  at admission (absolute 1-sigma; conversion recorded in each cohort's
  cohort-mapping-log.json). No covariance is inferred, fabricated, or
  adjusted anywhere in this evaluation (locked decision 1; gate input
  schema).
- Shared systematic uncertainties between analyses (for example a
  laboratory-wide component) are not modeled by either side's likelihood;
  both likelihoods treat analyses as independent given the parameters. This
  limitation is symmetric and is declared in the report (section 8). The
  gate's input schema already warns that source-specific analytical
  covariance and shared systematic uncertainties require separate handling;
  no such handling exists in the current machinery.

### 4.5 Bounds summary

| Parameter | Side | PROPOSED bound | Status |
|---|---|---|---|
| a206 (shared initial 206 ratio) | RCI | [0, 1.0] | D2 |
| a207 (shared initial 207 ratio) | RCI | [0, 1.0] | D2 |
| Closure age, calibration sample | RCI | [0, 4.6e9] yr | D3 |
| Closure age, each holdout sample (scoring) | RCI | [0, 4.6e9] yr | D3 |
| Concordia age, each sample | Comparator | [0, 4.6e9] yr | D3 |
| Initial ratios | Comparator | fixed at 0 (structural) | n/a |
| Decay constants | Both | fixed, Jaffey 1971 central | D4 |

## 5. Comparison statistics, penalty, aggregation, and decision rule

### 5.1 What the documents define

- Primary metric (protocol, Predictive outputs and metrics): joint
  predictive log-likelihood of the measured isotope ratios, with covariance
  and uncertainty, on held-out groups. The gate (item 7) requires reporting
  predictive log-likelihood, calibration, coverage, parameter count,
  sensitivity, and failed cases.
- Secondary metrics (protocol): calibrated posterior predictive coverage;
  standardized residuals; concordia distance / discordance distribution;
  cross-sample correlation structure; common-Pb and Pb-loss sensitivity;
  parameter count / effective complexity; robustness to alternative
  defensible data reductions.
- Hypotheses (protocol): H0, once independently constrained processes and
  parameter complexity are accounted for, RCI does not improve held-out
  predictive performance over the conventional comparator. H1, a globally or
  hierarchically constrained RCI initialization produces competitive
  held-out predictions without sample-specific initial-daughter tuning. H2
  is separately tested and is out of scope for this evaluation (no
  independent functional/mineralogical constraint set exists yet; section
  3.5). Scope note (v2): the H1 this evaluation can address is H1 in
  weakened form only, because the constraint on the initials here is
  sharing plus a calibration fit, not the independent constraint the
  protocol intends (section 1A, item N2). Results are reported against that
  weakened form and under the outcome ceiling of section 1, never as a
  verdict on H1 as written.

### 5.2 Gaps in the documents (named, not silently filled)

The gate and protocol do NOT define:

- G1: any numeric material-improvement margin or decision threshold. The
  protocol says a margin is to be predefined only after a pilot on non-test
  data and then locked. No pilot has been run and no margin exists.
- G2: the form of the parameter penalty. The gate (decision document, locked
  decision 6) says to penalize additional RCI parameters; neither document
  gives a penalty formula.
- G3: any aggregation rule across the 65 holdout samples (sum over analyses,
  mean over samples, or otherwise).
- G4: a computational definition of coverage. The protocol names calibrated
  posterior predictive coverage, but the machinery produces point estimates
  by deterministic minimization; there is no posterior anywhere in the
  current implementation.
- G5: whether parameter counts under a degeneracy are nominal or effective
  (the calibration fit has 3 nominal parameters and a 1-dimensional null
  direction; section 3.1).

Sections 5.3 to 5.5 propose completions for G2, G3, G5, G4, and G1 in that
order. Each is a PROPOSAL; it takes effect only through the corresponding
decision in section 9.

### 5.3 Parameter accounting and penalty (proposal for G2 and G5; decision D5)

Parameter counts, using the machinery's own counting functions:

- Calibration fit (RCI): k = 3 (one closure age plus the two shared initials;
  rci_fitter.unit_parameter_count). Nominal count 3; identifiable dimension
  2 because of the translation null direction. Both numbers are reported.
- Holdout scoring (RCI): each sample fits 1 parameter (its age, initials
  frozen), so 65 across the holdout, plus the 2 shared initials counted once
  as model complexity: K_RCI = 67.
- Comparator: 1 parameter per sample on both cohorts: K_conv = 65 on the
  holdout, 1 on the calibration sample.

PROPOSED penalty: Akaike form. The penalized log-likelihood of a side is
LL_pen = LL - K (the Akaike criterion rescaled so that larger is better), so
the penalized difference on the holdout carries a penalty of
(K_RCI - K_conv) = 2 log-likelihood units. The nominal counts are used
(charging RCI for the degenerate direction as well), which is conservative
against RCI. Two sensitivities are reported alongside: a
Bayesian-information form, LL - (ln N / 2) K with N the number of scored
analyses; and an identifiable-dimension form that charges one fewer
parameter (difference of 1 instead of 2), reflecting the calibration fit's
single null direction. The headline rule uses the nominal Akaike form.

### 5.4 Aggregation and decision rule (proposals for G3 and G1; decisions D6, D7)

PROPOSED primary statistic: the total predictive log-likelihood difference
over the scored holdout samples,

  Delta = sum over samples s of (LL_RCI,s - LL_conv,s),

where LL_RCI,s is sample s's joint log-likelihood under the frozen initials
at its fitted age, and LL_conv,s is the same sample's joint log-likelihood
at its fitted conventional concordia age. The penalized form is
Delta_pen = Delta - (K_RCI - K_conv) = Delta - 2. The per-analysis form
is Delta_pen / N, with N the number of scored analyses (846 if all samples
are scored).

PROPOSED secondary reporting: the full per-sample table (section 8); the
unit-weighted mean of per-sample differences (each sample weighted equally,
so the granite and granodiorite concentration of the holdout, 420 of 846
analyses in two rock types, cannot dominate unnoticed); and strata summaries
by Rock_Class (igneous / metamorphic) and by granite-plus-granodiorite
versus all other rock types. Strata are reporting only; the headline rule
uses the primary statistic.

PROPOSED decision rule, with margin M in log-likelihood units per analysis,
locked under D7 before any holdout access:

- Delta_pen / N greater than M: RCI predicted the holdout better than the
  conventional comparator by more than the material margin, after penalty.
  Report exactly that, as a predictive result on this holdout. It is not a
  PEP claim (section 1).
- Delta_pen / N between -M and M inclusive: the two models are not
  distinguished on this holdout at the material margin. Report as
  indistinguishability / observational equivalence on this data, per gate
  item 7: explicitly NOT parity.
- Delta_pen / N less than -M: the conventional comparator predicted the
  holdout better by more than the material margin. Report as a negative
  result for H1 on this holdout.

Outcome labels (v2, with the rubric-vocabulary fix applied at
ratification). Whichever branch obtains, the evaluation's outcome is
reported at plausibility grade, under the ceiling of section 1, in the
RCIM-004 rubric's own vocabulary: first branch, "adequate in scope" with
the framing verdict CONSISTENT; second branch, INDETERMINATE
(indistinguishability, not parity), which carries neither the rubric's
positive nor its negative tier label; third branch, "disfavored in scope"
with the framing verdict INCONSISTENT. These labels describe the standing
of the shared-initials model family on this holdout. They are not a PEP
verdict, not a verdict on the full hypothesis, and not substantiation of
any initial inventory.

PROPOSED margin-locking rule (for G1): after step (ii) and before step
(iii), compute on the Manzano calibration sample the per-analysis penalized
log-likelihood difference between the two sides and its jackknife standard
error s over the 24 calibration analyses (within-sample only; the sample is
one unit and the jackknife measures analysis-level noise, nothing more).
Lock M = max(0.5, 2s). The floor 0.5 corresponds to a per-analysis
likelihood ratio of about 1.65, a weak-evidence scale; the 2s term prevents
the margin from being set below the noise scale visible on calibration data.
If the pilot computation fails, M = 0.5. The locked value of M, the pilot
quantities, and s are recorded in the evaluation report before the holdout
results are presented.

### 5.5 Calibration and coverage (proposal for G4; decision D13)

PROPOSED operationalization, in place of the posterior predictive coverage
the machinery cannot produce: for each sample on each side, report chi2
against its degrees of freedom (2n - k), the count of samples whose chi2
exceeds the 0.99 quantile of the chi-square distribution at their degrees of
freedom, and the distribution of per-analysis standardized residuals
(Mahalanobis components). This is a calibration report, labeled as the
point-estimate analogue of coverage, not as posterior coverage. If the
principal prefers, the evaluation can be halted until a posterior-producing
implementation exists; the trade-off is that no current machinery can run
the evaluation at all in that case.

## 6. Data rulings to ratify

### 6.1 Alaska rows with published error correlation exactly 0.0 (decision D8)

The Alaska freeze record (caveat 2) records 12 in-scope rows with a published
Error_Correlation of exactly 0.0, of which 9 are in admitted rows, and notes
that whether a published 0.0 is a measured near-zero correlation or a
placeholder is not stated by the source. The Manzano cohort is unaffected
(its published correlations run 0.40 to 0.97, none zero).

RECOMMENDED ruling: the primary analysis uses those rows exactly as
published, with rho = 0.0. Grounds: the gate forbids fabricating covariance
and forbids silently assuming rho = 0 where it is not published; here 0.0 IS
the published value, and replacing it with anything else would be an
inference of exactly the kind locked decision 1 prohibits. A secondary
sensitivity run that excludes the affected rows (whole analyses, on both
sides identically) is predeclared here as the only permitted variant; its
results are reported as sensitivity, never as the headline. (The sensitivity
run is a reporting variant computed in the same scoring pass outputs; it does
not constitute a second scoring of the holdout under different primary
settings, and it may not be promoted to primary after the fact.)

### 6.2 Suffix-discrepant Alaska samples (decision D9)

RECOMMENDED ruling: samples 12AJJ039A and 13ATE310 (20 zircon rows) remain
excluded, as the Alaska freeze record left them. Their rows cannot be matched
to any sample-summary row under the declared join rule; the nearest summary
codes differ in suffix, and suffixes distinguish distinct samples elsewhere
in the release. They may enter a future cohort version only if the Principal
Operator reconciles the identifiers against the FGDC metadata or the authors'
records, as a source-data decision, and any such change is a cohort revision
requiring its own freeze record, not an amendment to this evaluation.
(The related source inconsistency, sample 12SB112Z, concerns titanite rows
already out of scope and needs no ruling here.)

### 6.3 Minimum-information rule for scoring a sample (decision D10)

Alaska samples carry 3 to 32 admitted analyses. PROPOSED rule: a sample is
scored in the primary aggregate if and only if it has at least 3 admitted
analyses. At scoring, each side fits 1 parameter per sample, so a 3-analysis
sample has 2 x 3 - 1 = 5 degrees of freedom on each side; below 3 analyses
the per-sample calibration statistics of section 5.5 carry almost no
information. All 65 Alaska samples satisfy the rule, so on this cohort the
rule excludes nothing. A sample below the threshold, if one ever appeared in
a scored cohort, would be listed in the report as not scored, with its
admitted data shown and the reason stated, and excluded from every aggregate;
it is never silently dropped. Per-sample diagnostics for samples with fewer
than 5 analyses are flagged low-information in the report but are still
reported.

## 7. Calibration honesty

The Manzano calibration cohort is one sample (K05-ABO-1r) from one geological
unit (Blue Springs metarhyolite) from one laboratory (Stanford-USGS
SHRIMP-RG) by one method. The decision document (locked decision 2) already
states what follows from that; this section binds the evaluation's language
to it.

Fitting the Manzano sample can establish:

- that the ingestion and admission pipeline runs end to end on real,
  provenance-verified data, and the machinery executes on it;
- a fitted representative of the shared-initial family for this one sample
  under the ratified anchoring treatment, with its fit statistics;
- the calibration-side comparison against the conventional comparator on the
  same sample (a fitted-data comparison, reported for completeness and
  explicitly not evidence about generalization; section 3.7);
- the pilot quantities used to lock the margin M (section 5.4).

Fitting the Manzano sample cannot establish:

- that the fitted initials describe any other sample, unit, or laboratory;
  with one unit, "shared" initials are shared across 24 analyses of a single
  rock, and their transport to the holdout is precisely the untested
  assumption the holdout scoring examines;
- any cross-laboratory claim (the holdout is from the same laboratory; the
  Alaska freeze record states that the holdout tests geological
  generalization, not laboratory generalization, and any shared laboratory
  systematic is common to both cohorts);
- any separation of age from initial inventory (section 3.1);
- any PEP claim, in either direction.

Every generalization statement in the evaluation report must rest on the
holdout alone and must carry the laboratory non-independence limitation with
it.

## 8. Reporting obligations

The evaluation report (protocol deliverable D4; gate item 7) must contain:

1. The frozen inputs: cohort hashes, the code pin, the ratified bounds, the
   anchoring treatment, the locked margin M with its pilot quantities, and
   this predeclare's ratification record.
2. The calibration fit in full: fitted representative and identifiability
   flag, age, chi-square, log-likelihood, parameter count (nominal and
   identifiable dimension), degrees of freedom, optimizer outcome.
3. A per-sample table for all 65 holdout samples, no exceptions: analyses
   count; each side's fitted age, chi-square, log-likelihood, parameter
   count, degrees of freedom; the per-sample log-likelihood difference; the
   RCI identifiability flag and family sensitivity range for the age;
   bound-contact flags; convergence or failure status. Non-converged,
   rejected, and failed fits are reported in place, with the optimizer's
   outcome, never omitted and never replaced by a rerun under altered
   settings.
4. The aggregate statistics of section 5.4 (primary, penalized, per-analysis,
   unit-weighted, and strata forms) and the decision-rule outcome stated in
   the language of section 5.4.
5. The calibration and residual reporting of section 5.5, including failed
   cases.
6. The rho = 0.0 sensitivity results (section 6.1) and a statement of which
   samples, if any, fell under section 6.3 (none expected on this cohort).
7. Negative results reported as negative, in the headline, not only in an
   appendix. If the conventional comparator wins by more than the margin,
   the report says so in its first paragraph.
8. Declared / observed / inferred separation throughout: DECLARED quantities
   are the frozen inputs and rules of item 1; OBSERVED quantities are the
   published ratios, uncertainties, and correlations as frozen in the
   admission cohorts; INFERRED quantities are fitted ages, fitted initial
   representatives, and all statistics computed from them. No inferred
   quantity may be presented as observed, and the initial-ratio
   representative may not be presented as a measured inventory.
9. Limitations, stated in the report itself: laboratory non-independence of
   the holdout; fixed decay constants without uncertainty propagation
   (section 4.4); unmodeled shared systematics (section 4.4); no common-Pb,
   disequilibrium, or Pb-loss modeling on either side (symmetric absence;
   the gate requires any later such treatment to be modeled symmetrically);
   the age/initials non-identifiability and its treatment.
10. The standing caveats of section 1, verbatim in substance: no PEP claim;
    indistinguishability is not parity.

## 9. Ratification block

Ratifying this predeclare (v2) means ratifying three things together:

(a) the re-scoped evaluation: a preliminary predictive-consistency
    evaluation between the protocol's G1 and G3 gates, at plausibility
    grade, under the outcome ceiling of section 1, run under the sequence
    of section 2;
(b) the narrowing record of section 1A as a versioned amendment to
    RCIM-002, RCIM-004, and the DFM U-Pb Validation Protocol, to be filed
    with those documents when this predeclare is filed, so that the
    narrowing stands on the record of the program and not only in this
    draft; and
(c) each decision below as stated (recommended option first in each case),
    as amended in v2.

Any decision the Principal Operator changes must be recorded with its
changed value before the evaluation runs; the evaluation may not start
with a decision left open.

Ratification record. Ratified by the Principal Operator on 2026-10-28, in
his own words: "Ratify v2 with the rubric-vocabulary fix". Parts (a), (b),
and (c) above are ratified together. Decisions D1 to D13 below are
RATIFIED AS A WHOLE, each in its recommended form as stated. The
rubric-vocabulary fix is applied in this filed text (sections 1 and 5.4).

- D1 Anchoring treatment. RECOMMENDED: the identifiable-estimand evaluation
  of section 3.6 (family-invariant primary statistics; initials frozen at
  the canonical minimum-inventory representative for scoring; family
  sensitivity ranges on all non-invariant reported quantities; option (a)
  rejected; inventory-level and absolute-RCI-age claims deferred until an
  independent constraint set exists). Alternatives: (a) Stacey-Kramers fixed
  initials (not recommended; section 3.2); (b) box only, no estimand
  restriction (not recommended; section 3.3).
- D2 Initial-ratio bounds. RECOMMENDED: a206 and a207 each in [0, 1.0].
  Alternative: [0, 10.0] (machinery placeholder). Or a value set by the
  principal (section 4.1 trade-off).
- D3 Age bound. RECOMMENDED: [0, 4.6e9] years for every fitted age on both
  sides (machinery default).
- D4 Decay constants. RECOMMENDED: proceed with Jaffey et al. (1971) central
  values fixed on both sides, limitation declared. Alternative: halt until
  decay-constant uncertainty propagation is implemented.
- D5 Parameter counting and penalty. RECOMMENDED: nominal counts (calibration
  RCI k = 3; holdout K_RCI = 67, K_conv = 65), Akaike-form penalty as
  primary (penalized difference Delta - 2), Bayesian-information and
  identifiable-dimension forms as reported sensitivities.
- D6 Aggregation. RECOMMENDED: primary statistic = total predictive
  log-likelihood difference summed over scored samples (analysis-weighted),
  with per-analysis normalization for the decision rule; unit-weighted mean
  and rock-type strata as secondary reporting.
- D7 Margin. RECOMMENDED: lock M by the section 5.4 pilot rule,
  M = max(0.5, 2s), computed from the Manzano calibration fit after step
  (ii) and before any holdout access; fallback M = 0.5 if the pilot
  computation fails. Alternative: a fixed numeric margin set by the
  principal now.
- D8 Rho = 0.0 rows. RECOMMENDED: primary analysis uses the 9 admitted
  Alaska rows exactly as published (rho = 0.0); exclusion of those analyses
  (both sides identically) as a predeclared secondary sensitivity only.
- D9 Suffix-discrepant samples. RECOMMENDED: 12AJJ039A and 13ATE310 remain
  excluded (20 rows); reconciliation is a separate source-data decision by
  the principal and would be a cohort revision, not part of this evaluation.
- D10 Minimum-information rule. RECOMMENDED: primary scoring requires at
  least 3 admitted analyses per sample; below-threshold samples are reported
  as not scored, never silently dropped (no Alaska sample is below the
  threshold).
- D11 Grouping and sharing structure. RECOMMENDED: calibration fit at sample
  level (fit_unit on K05-ABO-1r; the calibration cohort contains exactly one
  sample, so the gate's group-level sharing has no second unit on the
  calibration side); holdout scoring per sample with the frozen initials
  (fit_unit with fixed_initials); no re-grouping of holdout samples (by rock
  type, geography, or otherwise) for the primary score; strata are reporting
  only. This resolves, for this evaluation, the grouping-granularity gap the
  fitter records (the gate names unit versus group sharing but predeclares
  no concrete grouping).
- D12 Evaluation code pin. RECOMMENDED: pin the evaluation code at master
  commit 12906ecfdc4965032a56bd9b860ec733b7a26197 (the PR #48 machinery state);
  any later code change requires a ratified amendment and a new pin before
  use.
- D13 Coverage operationalization. RECOMMENDED: report the chi-square
  calibration analogue of section 5.5, labeled as such. Alternative: halt
  until a posterior-producing implementation exists.

## Appendix: traceability and document gaps found

Traceability. Cohort counts, hashes, and caveats: the two freeze records.
Model form, degeneracy identity, parameter counts, defaults, and the
fitter's recorded gaps: rci_fitter.py and its tests. Comparator structure
and counting: concordia_comparator.py and its tests. Exercised synthetic
ranges: tests/test_rci_fitter.py, tests/test_concordia_comparator.py,
tests/test_comparison_harness.py, and comparison_harness.standard_cases().
Metrics and hypotheses: protocol (Predictive outputs and metrics; Hypotheses)
and gate item 7. Locked methodological decisions: OBSERVATIONAL_ACQUISITION_
DECISION_v0.5.md.

Gaps found in the gate and protocol documents, beyond the anchoring
degeneracy (each is handled above by a named proposal or a declared
limitation; none is silently filled):

- Margin: none defined (gap G1; the protocol defers it to a pilot that had
  not been run).
- Penalty form: none defined (gap G2).
- Aggregation across holdout samples: none defined (gap G3).
- Coverage: named but not computable with the current point-estimate
  machinery (gap G4).
- Nominal versus effective parameter count under degeneracy: undefined
  (gap G5).
- Grouping granularity for shared initials (unit versus geological /
  mineralogical group): named by the gate, never concretely predeclared
  (resolved for this evaluation by D11).
- No numeric initialization parameter bounds anywhere in the documents
  (both freeze records state this; section 4 proposes values from the
  machinery's defaults and the exercised synthetic ranges only).
- Decay-constant uncertainty: the protocol asks for uncertainty budgets;
  the machinery fixes central values (section 4.4, decision D4).
- Shared systematic uncertainties between analyses: flagged by the gate's
  input schema as requiring separate handling; not modeled by either
  likelihood (section 4.4).
- Documentation drift: the gate's state header ("No observed ratios have
  been retrieved, ingested, fitted or compared") predates the acquisition
  and freezing of both cohorts. The gate's NOT FROZEN state remains accurate
  for bounds and metrics, but the header's factual sentence is stale and
  should be corrected when the gate is next revised.
- Scope drift (v2): v1 of this predeclare was drafted as the protocol's G3
  preregistered evaluation although G2 as specified had not occurred, and
  the founding documents' generator, independent-constraint, comparator,
  and cross-chain requirements had narrowed without a ratified scope
  change. The drift audit of 2026-10-28 named the items; section 1A of
  this version is the corrective record, and ratification under section 9
  carries it into RCIM-002, RCIM-004, and the protocol as a versioned
  amendment.

Human-Curated, AI-Enabled (HCAE)
