# Historical Reconstruction Identifiability: Radiometric Inverse-Problem Research Protocol

**DFM | 2026-10-25 | Proposed research protocol, not validated result.**  
**Companion work packages:** radiometric provenance classification; geological disturbance audit; daughter-product adjudication.

## Question
Under what independently justified conditions do present isotope measurements and geological relationships identify a unique or tightly bounded actual history, rather than one of several observationally equivalent histories? In particular, can DFM specify an alternative history with coherent initialization, genuine generative deployment, and actual later geological events that reproduces *joint* observations without freely tuning specimen-specific initial states?

## Scientific framing
Radiometric dating is an inverse problem: present isotope abundances constrain past conditions and processes through a forward physical model. Inversion can be identifiable under restrictive, well-supported assumptions and underdetermined when initial conditions, open-system transfer, mixing, or event assignments are insufficiently constrained. **Non-uniqueness in a permissive model does not demonstrate non-uniqueness after independent geological constraints are imposed.** Nor does it establish a young chronology.

For a simple closed parent-daughter system, P(t)=P0 exp(-lambda t), D(t)=D0+P0[1-exp(-lambda t)]. Given measured P and D alone, t is not determined without information about D0 and/or initial state. A multi-aliquot isochron constrains initial daughter composition and elapsed time if aliquots are cogenetic, initially homogeneous in the daughter ratio, and sufficiently closed. Multiple clocks, concordia, textures, field relations, and calibration further reduce admissible histories.

An illustrative generalized forward model is y=F(theta,h,B)+epsilon, where y includes isotope ratios, covariance, zoning, diffusion profiles, textures and geological relations; theta includes physical parameters; h specifies actual event order and duration; B is a possible initialization/deployment boundary. Disturbance and mixing are explicit processes, not a universal error term.

## Three model families to compare
- **M0 Conventional history:** ordinary formation, crystallization, alteration, cooling and radioactive decay; inherited reservoirs and open-system events are independently constrained.
- **M1 DFM coherent initialization:** a shared, physically derived initial-state generator, followed by ordinary decay and genuine subsequent geological processes. No per-specimen age-target tuning.
- **M2 DFM generative deployment:** genuine extraordinary processes during deployment, followed by ordinary evolution. Explicit nuclear energy, heat removal, transport, conservation, and temporal mapping.
- **M3 Constrained hybrid:** M1+M2, with a predeclared finite parameter set and model-complexity penalty.

## Identifiability ladder
1. **Algebraic:** Can distinct parameter sets yield the same isotope ratios?
2. **Structural:** Can distinct full histories yield identical multi-isotope observations under the governing physical model?
3. **Practical:** Do uncertainty, sparse samples, and analytical covariance prevent discrimination even if structural uniqueness exists?
4. **Geological:** Do independent textures, closure constraints, stratigraphy and field relationships eliminate alternatives?
5. **Cross-system:** Do terrestrial, lunar, meteoritic and multiple mineral clocks jointly eliminate alternatives?
6. **Historical Integrity:** Do proposed event traces correspond to actual events in each candidate history?

A model is not competitive merely because it passes level 1.

## Pre-registered-style protocol (not yet formally registered)
**Stage A: Data acquisition.** Select published raw or machine-readable data with uncertainties and covariance, mineral/rock metadata, and independent field relations. Include at least one terrestrial igneous isochron suite, a concordant and discordant U-Pb zircon dataset, a metamorphic reset case, a stratigraphically constrained volcanic ash, a known-age calibration case, and Earth–meteorite Pb constraints.

**Stage B: Baseline reproduction.** Recompute conventional results with established open-source geochronology methods such as IsoplotR, including uncertainties, correlations, and goodness of fit. Report cases where published interpretation is contested.

**Stage C: Disturbance reconstruction.** Fit physically bounded Pb loss, mixing, diffusion, metamorphism and closure models where supported by independent textures and thermal history. Distinguish recognizable resetting from irretrievable information loss.

**Stage D: DFM forward model.** Before examining withheld data, specify the initialized-state generator or real deployment processes, parameter count, physical constraints, and which specimens could qualify as primordial. No appeal to 'maturity' without a predicted isotope distribution.

**Stage E: Holdout evaluation.** Compare M0–M3 on withheld isotope ratios, concordance/discordance, zoning, field order, and thermal constraints. Use posterior predictive checks or another explicitly justified common metric; report complexity, sensitivity and failures.

**Stage F: Adjudication.** Identify whether DFM is (i) merely algebraically possible, (ii) physically admissible, (iii) observationally equivalent under present data, (iv) empirically distinguishable, or (v) contradicted by specified observations. Register only genuinely prospective predictions through programme governance.

## Proposed measures
- Fit residuals standardized by full analytical covariance, not independent-error shortcuts.
- Profile likelihood / posterior distributions for elapsed time, initial daughter ratios, closure ages, transfer coefficients and event count.
- Sensitivity to priors and allowed boundary conditions.
- Effective degrees of freedom, parameter count, and out-of-sample predictive error.
- Cross-chronometer agreement and geological event-order consistency.
- Energy/mass balance for extraordinary generative models.
- Count of specimen-specific exceptions and unregistered auxiliary adjustments.

## Critical adversarial tests
**I-01:** Can M1 explain *multiple* mineral isotope systems with a single shared initialization rule? Failure: free initial daughter ratios are required for each sample to reproduce desired dates.

**I-02:** Can M2 explain genuine isotope-production histories without catastrophic unaccounted energy? Failure: hidden accelerated-decay assumption or unconstrained heat sink.

**I-03:** Do zircon growth zoning, discordia and independently dated overprints constrain multiple actual episodes? Failure: DFM classifies traces as initialized without a physical generation mechanism.

**I-04:** Does adding field order and stratigraphic bracketing break an apparent algebraic degeneracy? If yes, report identifiability improvement, not generic underdetermination.

**I-05:** Can Earth–Moon–meteorite concordance be predicted rather than fitted? Failure: the target conventional age is an input to initial-state specification.

**I-06:** Does the provenance classifier select primordial specimens without looking at their conventional numerical age? Failure: circular selection.

**I-07:** Are conventional M0 results reproduced accurately before critique? Failure: comparison based on caricature or incorrect regressions.

## Known scientific constraints
- Isochron assumptions include cogenetic material, shared initial daughter isotope ratio, and sufficient closure. Real datasets can be complicated by mixing and open-system behavior.
- U-Pb concordance and discordance can constrain Pb loss, inherited cores, common Pb and disequilibrium, although ambiguity remains in some cases.
- Analytical error covariance and choice of regression model can materially affect uncertainty and even age estimates in imprecise datasets.
- An inverse problem with too few observations can have infinitely many solutions, but independent observations and physics may identify a much narrower family.

## Initial literature
- Schoene (2014), *U–Th–Pb Geochronology*, Treatise on Geochemistry: https://timslab.princeton.edu/sites/g/files/toruqf2276/files/schoene-treatisegeochemistry-2014.pdf
- Powell et al. (2020), *Robust isochron calculation*, Geochronology 2, 325–342: https://doi.org/10.5194/gchron-2-325-2020
- Li and Vermeesch (2021), *Inverse isochron regression for Re–Os, K–Ca and other chronometers*, Geochronology 3, 415–420: https://doi.org/10.5194/gchron-3-415-2021
- Vermeesch (2021), *On the treatment of discordant detrital zircon U–Pb data*, Geochronology 3, 247–257: https://doi.org/10.5194/gchron-3-247-2021
- Vermeesch (2024), *Errorchrons and anchored isochrons in IsoplotR*, Geochronology 6, 397–412: https://doi.org/10.5194/gchron-6-397-2024
- Davies et al. (2018), *Investigating Complex Isochron Data Using Mixture Models*: https://doi.org/10.1029/2018GC007548

## Governance
This protocol is a proposed test design. It does not claim any demonstrated non-identifiability for a specific geological dataset, alter the adopted Christian Designism A-001 auxiliary, resolve I-0006 or I-0008, or assert that terrestrial radiometric chronology has been invalidated. Those questions require actual data and forward-model computation.
