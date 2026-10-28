# DFM U-Pb Empirical Validation Protocol v0.1
Date: 2026-10-28
Status: Draft for methodological review; no empirical validation claimed.
Parent: DFM WP-004 radiogenic track and WP-035 latent isotopic functionality.

## Objective
Test whether a constrained radiogenic coherent initialization (RCI) model predicts independently held-out U-Pb isotope measurements at least as well as a conventional geochronological model under comparable geochemical, nuclear, and uncertainty assumptions. Mathematical fit alone does not establish provenance or plausible explanatory parity (PEP).

## Hypotheses
H0: Once independently constrained physical processes and parameter complexity are accounted for, RCI does not improve held-out predictive performance over the conventional comparator.
H1: A globally or hierarchically constrained RCI initialization produces competitive held-out predictions without sample-specific initial-daughter tuning.
H2 (stronger, separately tested): Independent functional/mineralogical constraints narrow admissible initial daughter inventories enough to yield novel quantitative predictions.

## Models and identifiability
Conventional: parent-daughter accumulation since mineral closure, common Pb correction, optional independently justified initial disequilibrium and Pb loss.
RCI: initial parent/daughter vector and spatial distribution at commissioning, followed by the same measured decay and physical transport; mineral formation/closure events modeled explicitly. Do not conflate Earth initialization time with individual zircon closure times.

For ideal closed-system post-closure evolution, define a206 = D206*(0)/P238(0) and a207 = D207*(0)/P235(0). Then D206*(t)/P238(t) = (a206+1) exp(lambda238*t)-1, and D207*(t)/P235(t) = (a207+1) exp(lambda235*t)-1. Initial radiogenic daughters must be separated from common Pb. If a206 and a207 are free for each sample, time and initial inventory are not identifiable; such a model cannot count as successful validation.

## Data register requirements
Each candidate dataset: stable ID, original DOI/URL, instrument and analytical method, rock/mineral context, sampling geography, parent and daughter isotope ratios, uncertainty/covariance, common-Pb correction, standards, raw vs reduced status, Pb-loss/discordance flags, provenance, license, and any independent constraints. Preserve raw measurements and processing versions. Exclude samples only using preregistered, measurement-independent quality rules.

## Sources to investigate
- Jaffey et al. (1971), Physical Review C 4, 1889, DOI 10.1103/PhysRevC.4.1889: uranium half-lives and primary measurement basis.
- IUGS-IUPAC recommendations, DOI 10.1515/pac-2021-1202: half-life uncertainty budgets and status.
- Geochron/EarthChem https://www.geochron.org/gettingdata : public U-Pb data export, subject to per-record provenance and licenses.
- International Association of Geoanalysts https://www.geoanalyst.org/zircon-reference-materials-and-their-u-pb-ages/ : zircon reference materials, including caution about Pb loss.
- IsoplotR DOI 10.1016/j.gsf.2018.04.001 : independent conventional calculation and concordia methodology.
No datasets have yet been downloaded, vetted, frozen or analyzed under this protocol.

## Preregistration and splits
Select multiple geological contexts and laboratories before fitting. Use grouped splits by geological unit and laboratory, not random spots from the same grain or rock across train/test. Reserve at least one fully held-out geological unit and one external laboratory dataset if sufficient eligible data exist. Freeze selection rules, dataset hashes, analysis code commit, model parameter priors/bounds and primary metrics before examining test outcomes. Separate calibration standards from independent scientific test specimens.

## Calibration
Obtain decay constants with stated uncertainty and provenance. Validate uranium isotope ratios rather than universally fixing them. Record zircon U/Pb partitioning and common-Pb behavior with independently measured bounds. Identify zircon crystallization and closure events, metamorphism, Pb loss, radiation damage and U-series disequilibrium. Parameterize nuclear network explicitly if intermediate chains matter at the evaluated timescale. Treat provisional branching/energies as blockers to heat-budget conclusions.

## Predictive outputs and metrics
Primary: joint predictive log-likelihood of measured isotope ratios with covariance and uncertainty, on held-out groups; calibrated posterior predictive coverage; standardized residuals.
Secondary: concordia distance/discordance distribution, cross-sample correlation structure, common-Pb and Pb-loss sensitivity, parameter count/effective complexity, and robustness to alternative defensible data reductions.
Compare against (a) standard conventional model with appropriate geological flexibility, (b) a null unconstrained initial-inventory model as a demonstration of nonidentifiability, and (c) restricted RCI models. Report likelihood and predictive scores, not just fitted age differences. Predefine a material improvement margin only after a pilot on non-test data, then lock it.

## Failure and interpretation rules
- Failure if RCI needs an independent freely tuned initial daughter ratio for every sample.
- Failure if independent constraints make predicted observations incompatible with held-out data beyond declared uncertainty.
- Failure if claimed functional constraints are chosen after viewing target isotope ratios.
- Equal predictive performance does not by itself demonstrate historical RCI provenance; observational equivalence must be acknowledged.
- Negative evidence for unique isotope functionality does not by itself falsify coordinated initialization.
- Do not claim PEP unless nuclear, thermal, mineralogical and cross-system obligations have also been assessed.

## First computational gates
G0: independent reproduction of standard U-Pb concordia from accepted decay constants; uncertainty propagation; synthetic closed-system checks.
G1: fit and holdout leakage tests, identifiability diagnostics, negative controls and conventional baseline cross-check against independent software.
G2: externally constrained RCI parameters frozen before held-out evaluation.
G3: preregistered held-out U-Pb evaluation, blinded where feasible.
G4: independent K-Ar and Rb-Sr cross-system tests and radiogenic heat/mass balance, with no retroactive parameter tuning.

## Deliverables
D1 Reference-data register with sources, licensing, parameter uncertainty and gaps.
D2 Preregistration dossier and dataset manifest with frozen selection/split rules.
D3 Reproducible comparator and RCI implementation, tests and diagnostics.
D4 Held-out evaluation with residual plots, calibration and complexity comparison.
D5 Epistemic assessment: consistency, plausibility, PEP, discriminators, limitations.

## Immediate decisions
Select first geological/mineral cohort and define independent calibration sources. Avoid using published model-derived 'ages' as the only response variable; prioritize measured ratios and covariance. No repository mutations or cross-agent handoffs are implied by this draft.

## Amendment 2026-10-28: scope narrowing for the first U-Pb evaluation

The first U-Pb evaluation in this program proceeds in a narrowed form, as
recorded in section 1A (narrowing record) of the ratified evaluation
predeclare, research/upb-validation/EVALUATION_PREDECLARE_v1.md, filed
with this amendment. The narrowing items that touch this document are:

- Externally constrained parameters have not been frozen (item N2).
  Gate G2 of this protocol (externally constrained RCI parameters frozen
  before held-out evaluation) has not occurred as specified: no
  independent constraint set exists in the record, and the shared
  initials are fitted to the calibration cohort's ratios and frozen.
  Hypothesis H1 is addressed only in weakened form, and H2 is not
  addressed at all.
- The split and context design is narrowed (items N5, N6). This protocol
  calls for multiple geological contexts and laboratories, grouped splits
  by geological unit and laboratory, and an external laboratory dataset
  where eligible data exist. The narrowed evaluation calibrates on a
  single sample from one unit and one laboratory, and its holdout is
  from the same laboratory and method, so it tests geological
  generalization only.
- The comparator is run in closed-system concordia form only (item N3).
  The initial disequilibrium and Pb-loss treatments this protocol
  contemplates for the conventional model are not modeled on either
  side; the absence is symmetric.
- Gate position (item N7). The narrowed evaluation sits between gates G1
  and G3 of this protocol. It is not the G3 preregistered held-out
  evaluation, and G4 is untouched.

The original requirements of this document remain in force, unamended in
substance, for the full preregistered PEP evaluation; that evaluation
remains contingent on the independent-constraint work package named in
the predeclare. This amendment was ratified by the Principal Operator on
2026-10-28 ("Ratify v2 with the rubric-vocabulary fix") as part (b) of
the three-part ratification of the predeclare.

Human-Curated, AI-Enabled (HCAE)
