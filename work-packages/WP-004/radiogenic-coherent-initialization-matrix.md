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
