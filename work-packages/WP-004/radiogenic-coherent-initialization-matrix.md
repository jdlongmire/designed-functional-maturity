# Radiogenic Coherent Initialization Matrix (RCIM)

**WP:** WP-004  
**Status:** Baseline v0.1  
**Rule:** No conventional radiometric target age may be used as an initialization input.

| System | Functional / heat relation | Principal physical coupling | Initialization freedom | Concordance target | Post-initialization history | DFM status / pressure |
|---|---|---|---|---|---|---|
| U-238 -> Pb-206 | U contributes materially to long-lived radiogenic heat | U geochemistry, zircon/mineral partition, decay chain, Pb mobility | Bulk U constrained by thermal architecture; exact mineral daughter state not derived by heat alone | U-Pb concordia, terrestrial zircon and meteoritic relationships | decay, crystallization, closure, Pb loss/gain, inheritance, metamorphism | **High-pressure test.** Must derive or independently constrain pristine concordance without target-age fitting. |
| U-235 -> Pb-207 | Same U inventory; distinct decay constant provides internal cross-check | Shared U chemistry with U-238, distinct nuclear decay chain | Coupled to U-238 abundance and nuclear law; daughter state remains constrained target | dual U-Pb concordance | same mineral history with isotope-specific decay | **High-pressure test.** Particularly valuable because two clocks occupy the same mineral system. |
| Th-232 -> Pb-208 | Th is a major heat-producing element | Th geochemistry, mineral partition, decay chain | Bulk Th constrained by thermal/geochemical architecture; Pb state not automatically entailed | U-Th-Pb coherence | decay, closure, alteration, Pb mobility | **High-pressure test.** Heat relevance gives independent motivation for parent inventory, not exact daughter structure. |
| K-40 -> Ar-40 / Ca-40 | K contributes to radiogenic heat and geochemistry | volatile Ar behavior, mineral closure, K partitioning | Bulk K constrained in part by thermal/geochemical state; retained Ar highly history-sensitive | K-Ar / Ar-Ar structure where appropriate | degassing, closure, diffusion, excess/inherited Ar, reheating | **Mixed marker/chronometer domain.** Strong candidate for known-age post-initialization calibration. |
| Rb-87 -> Sr-87 | Limited direct heat-budget leverage relative to U/Th/K | Rb/Sr geochemistry, mineral partition, isochron relationships | Greater initialization burden; common-state constraints must be independently specified | Rb-Sr isochron and meteorite concordance | crystallization, mixing, metamorphism, open-system behavior | **Critical discriminator.** Concordance cannot be explained merely by terrestrial heat requirement. |
| Sm-147 -> Nd-143 | Limited direct thermal motivation | REE geochemistry, Sm/Nd fractionation, robust mineral behavior | Greater initialization burden; must emerge from common geochemical architecture | Sm-Nd isochron and meteoritic relationships | differentiation, crystallization, metamorphism | **Critical discriminator.** Tests whether coherent initialization extends beyond heat-producing architecture. |
| Lu-176 -> Hf-176 | No primary terrestrial heat-budget motivation | Lu/Hf fractionation, zircon Hf systematics | Must be constrained through geochemical/mineral architecture, not heat | Lu-Hf correlations and cross-system agreement | differentiation, crystallization, inheritance | **Severe test.** Useful against an overly heat-centric explanation. |
| Re-187 -> Os-187 | No primary heat-budget motivation | siderophile/chalcophile geochemistry, mantle/meteorite reservoirs | Requires independent compositional constraints | Re-Os systematics and meteoritic/terrestrial relationships | differentiation, melting, reservoir evolution | **Severe test.** Common concordance must have a generative account beyond heat. |
| Extinct radionuclide systems | Not generally required by present heat budget | initial abundance, daughter excesses, nucleosynthetic/geochemical context | Cannot be licensed merely as mature-state decoration | correlated extinct-nuclide signatures across primitive materials | early/post-initialization differentiation depending model placement | **Open high-pressure problem.** Requires dedicated treatment. |

## Interpretation classes

### Class A: thermally motivated parents

U, Th and K have independent functional relevance through long-lived radiogenic heat. Their existence and approximate inventory can therefore be constrained without using radiometric ages as inputs. This does **not** entail their exact daughter distributions.

### Class B: coupled geochemical markers

Rb-Sr, Sm-Nd, Lu-Hf, Re-Os and similar systems test whether a coherent initialization model can generate broad isotopic order through common compositional, mineralogical and geochemical constraints. These systems prevent DFM from reducing the concordance problem to heat production alone.

### Class C: historical-event candidates

Closure, resetting, alteration and crystallization events occurring after initialization can generate genuine chronometric records. DFM must preserve such event records when provenance is independently established.

## Baseline inference

The radiogenic heat budget supplies a principled anchor for the existence and broad architecture of long-lived heat-producing nuclides. It is therefore a physical entry point into coherent radiogenic initialization.

The full concordance claim is stronger. A successful DFM model must propagate from independently constrained global initialization through nuclear, geochemical and mineralogical coupling to the observed pattern of concordance and discordance across both heat-producing and non-heat-producing isotope systems.

Accordingly:

```text
Radiogenic heat constraint
    -> partial constraint on S_0^rad
    != complete derivation of C_rad
```

The research objective is:

```text
independently constrained S_0
    -> coupled physical/geochemical state family
    -> predicted concordance/discordance structure
```

without:

```text
conventional target age -> tuned isotope initialization
```

## Priority execution order

1. U-Pb dual-decay concordance in zircon.
2. U-Th-Pb coupling and heat-budget consistency.
3. Rb-Sr and Sm-Nd meteoritic concordance as non-heat-centric discriminators.
4. K-Ar/Ar-Ar known-age calibration and post-initialization event chronometry.
5. Lu-Hf and Re-Os severe tests.
6. Extinct radionuclide systems as a dedicated follow-on work package.


## PEP appraisal overlay (v0.2; 2026-10-27)

**Target:** plausible explanatory parity (PEP), not explanatory superiority. **AHPP** requires symmetrical scrutiny of initialized states, conventional initial conditions, closure assumptions, disturbance histories, calibration, and post-hoc tuning. A parity determination is scoped to a named dataset and specified comparator, not to all geochronology at once.

| Evidence domain | Demonstrated Track A accommodation | Remaining constraint for PEP | Track B / parity status |
|---|---|---|---|
| U-238 / Pb-206 | Ordinary post-boundary decay and heat-accounting equations; initialized stable Pb does not itself imply past decay heat | Independently constrain initial Pb-206 and intermediate-chain populations, mineral partition, concordia and discordance without using target ages | Not established |
| U-235 / Pb-207 | Same conceptual boundary and coupled U inventory | Joint U-235/U-238 initial-state generator reproducing two-clock zircon relationships | Not established |
| Th-232 / Pb-208 | Th contribution to present radiogenic power modeled under explicit chain assumptions | Initial Th/Pb and intermediates plus cross-system U-Th-Pb concordance | Not established |
| K-40 / Ar-40 / Ca-40 | Heat contribution and ordinary branching can be represented | Quantitative gas retention, degassing, closure, isotope partition and known-event calibrations | Not established |
| Rb-87 / Sr-87 | Coherent initialization is mathematically possible | Non-thermal initial-state constraints; isochron slope/intercept structure and held-out reservoirs | Not established |
| Sm-147 / Nd-143 | Coherent initialization is mathematically possible | Independent REE partition constraints and multi-reservoir isotope correlations | Not established |
| Lu-176 / Hf-176 | Candidate coupling through zircon and geochemical partition | Quantitative isotope generator linked to U-Pb without age-derived tuning | Not established |
| Re-187 / Os-187 | Candidate reservoir-composition coupling | Mantle/meteorite mass balance and independently constrained correlations | Not established |
| Extinct radionuclides | No quantitative initialization accommodation established | Parent/daughter excesses and correlated extinct-nuclide signatures in primitive material | Not established |

**Evidence grade:** Current heat-accounting work supports limited physical compatibility and model consistency for specified assumptions, not independent derivation of observed daughter inventories. The entries above are not claims of empirical equivalence. Successful CI tests establish software behavior within tested regimes, not historical provenance.

### Minimum scoped PEP demonstration protocol

1. Register a specific dataset, its uncertainty, provenance, sample selection, and a concrete conventional comparator with disclosed auxiliaries.
2. Specify one common initial-state generator and a bounded parameter budget *before* examining held-out isotope ratios; list parameters informed by training data.
3. Propagate both models with ordinary post-boundary decay, relevant intermediate nuclides, partitioning, closure, and documented disturbances. Check mass/energy conservation.
4. Report fit residuals, uncertainty calibration, sensitivity to auxiliaries, number and scope of adjustable parameters, and performance on held-out data for each model.
5. Record outcomes as **compatible**, **adequate in scope**, **parity supported in scope**, **parity not established**, or **disfavored in scope**. Do not infer global parity from a single system.
6. Preserve failed or indeterminate cases. A comparator's shortcomings do not automatically count as positive evidence for DFM.

**Current disposition:** Conceptual coherence and preliminary Track A physical-accounting support. No scoped radiometric PEP determination has yet been earned. The strongest near-term candidate is a preregistered U-Th-Pb mineral-level test, followed by non-thermal Rb-Sr or Sm-Nd cross-checks.

## Preregistered pilot

The first scoped PEP protocol is [RCIM-004: U-Th-Pb parity pilot](RCIM-004-pep-u-th-pb-pilot.md). It defines comparator symmetry, dataset gates, a constrained parameter budget, held-out testing, and explicit blockers. It is a proposed protocol, not an executed empirical result.
