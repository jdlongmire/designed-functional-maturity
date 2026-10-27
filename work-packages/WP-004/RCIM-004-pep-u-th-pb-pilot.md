# RCIM-004: Preregistered U-Th-Pb Plausible Explanatory Parity Pilot

**Status:** Proposed protocol; not executed. **Date:** 2026-10-27.
**Programme:** DFM / WP-004 / WP-035. **Objective:** scoped PEP, not superiority.
**No observational results, parameters, or parity verdict are asserted here.**

## Question and comparison
Can a single independently constrained initial-state generator plus ordinary post-boundary decay and documented mineral histories account for a defined U-238/Pb-206, U-235/Pb-207, Th-232/Pb-208 zircon dataset with residuals and auxiliary flexibility comparable to a specified conventional crystallization/closure model?

**Comparator C:** a conventional U-Th-Pb concordia/discordia model with measured decay constants, common-Pb treatment, mineral crystallization/closure, and explicit Pb-loss/mixing events where independently warranted. Freeze the comparator's actual parameterization before scoring; do not compare DFM with an idealized straw model.

**DFM D:** a shared initialized terrestrial reservoir state, geochemical partition into mineral populations, then ordinary decay, transport, and measured post-boundary events. Historical duration is not inferred from target conventional ages. D must specify the commissioning boundary, spatial reservoir structure, parent/intermediate/daughter inventories, and mineral partition rules before scoring.

## Dataset gate (not yet fulfilled)
1. Select a public zircon U-Th-Pb dataset with raw isotope ratios, uncertainties/covariances, common-Pb information, sample-level metadata, analytical method, and documented processing.
2. Record dataset identifier, URL/DOI, access date, version/hash, sampling criteria, exclusions, and calibration dependencies.
3. Partition by geological unit or specimen, not randomly by individual spot, to prevent leakage. Reserve at least one held-out unit and a separately justified post-initialization event control.
4. Record independent geological constraints without importing their conventional radiometric ages as DFM initial-state parameters.
5. No model fit or PEP verdict until dataset provenance and split are frozen.

## Model specification and parameter budget
| Category | DFM D | Conventional C | Required record |
|---|---|---|---|
| Shared initial reservoir | Global/regional parent and daughter vectors; U235/U238 coupling; Th/U | Initial common Pb and source reservoir composition | Bounds and independently justified priors |
| Mineral partition | One shared partition rule per declared mineral/reservoir class | Crystallization fractionation and mineral-specific common Pb | Parameter count and sample independence |
| Nuclear kinetics | Evaluated branches, half-lives, intermediates; ordinary decay | Same evaluated nuclear physics | Source/version and numerical error |
| Open-system events | Independently supported Pb loss/gain, mixing, metamorphism | Same documented event evidence | Event count, free parameters, rationale |
| Thermal accounting | Chain-resolved heat, daughter inventories, reservoir mass balance | Same physical constraints where relevant | Conservation and uncertainty |
| Fitting | Training units only | Same training units | Optimization method and parameter disclosure |

No independent initial Pb value per analytical spot. A parameter introduced after examining held-out results is a new auxiliary and invalidates that holdout; version the revision and select a fresh holdout.

## Tests and outcomes
**T1:** Conservation and kinetic verification, including the extreme U-238 chain stiffness; currently incomplete for the evaluated full chain.
**T2:** Within-unit dual U-Pb concordia and discordia structure, with uncertainty propagation.
**T3:** Th-Pb joint consistency on applicable material, avoiding unjustified assumption of identical closure behavior.
**T4:** Held-out unit predictive residuals and coverage, including systematic direction of errors.
**T5:** Non-thermal external check (Rb-Sr or Sm-Nd), preregistered separately rather than claimed from U-Th-Pb alone.
**T6:** Sensitivity to source reservoir priors, closure assumptions, common-Pb corrections, mixing, and disturbance auxiliaries for *both* models.

Report for each: dataset coverage, normalized residuals, uncertainty calibration, fitted parameter count, post-hoc revisions, independent constraints, and failures. Model-selection metrics are permitted only with defensible likelihood/error models; do not invent Bayes factors or probabilities.

**Outcome rubric:**
- *Compatible*: no demonstrated contradiction in a narrowly specified calculation.
- *Adequate in scope*: quantified observed relationships reproduced with disclosed residuals and physical constraints.
- *PEP supported in scope*: adequate DFM and comparator models with comparable constraint/auxiliary burden and held-out performance, after explicit uncertainty accounting.
- *PEP not established*: missing data, model, validation, or comparative evidence.
- *Disfavored in scope*: material unexplained failure under frozen constraints.

## Immediate blockers and ordered work
1. Complete evaluated branch/energy provenance for U-238, U-235, Th-232 and validate the stiff solver across required half-life contrasts.
2. Identify and freeze a suitable publicly reproducible zircon dataset and comparator specification.
3. Specify shared initial-state generator and finite parameter budget without using conventional ages as initialization targets.
4. Execute preregistered forward predictions, held-out scoring, and AHPP audit.

**Baseline verdict (2026-10-27): PEP not established.** Current heat models provide preliminary Track A consistency, not a demonstrated U-Th-Pb isotopic fit. No claim of superiority is required or made.
