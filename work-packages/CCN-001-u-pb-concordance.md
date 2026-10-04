# CCN-001 — U-Pb Concordance

**Status:** Active severe-test baseline  
**Region:** II — Historical Development  
**Track:** A and conventional comparator, scored separately  
**Linked work:** WP-008, WP-009, WP-012, OAR-006, OAR-008

## 1. Claim under test

Does concordant U-Pb isotope structure warrant the historical claim that the reconstructed radiogenic duration was actually traversed, and can DFM independently generate the same observed structure without using that duration as an initialization surrogate?

This CCN does not treat "U-Pb dating" as one observation. It decomposes the evidential network.

## 2. O -> L -> R -> H decomposition

### O — Observation

Measured quantities include, depending on analytical method and correction scheme:

- U-238, U-235, Pb-206, Pb-207 and relevant common-Pb isotope abundances/ratios;
- spatial and microstructural relationships within zircon domains;
- populations of concordant and discordant analyses;
- mineral chemistry and trace-element context.

The observed datum is the isotope/mineral state. "Age" is not itself the raw observation.

### L — Operational physics

The reconstruction uses experimentally constrained radioactive decay behavior:

```text
N(t) = N0 exp(-lambda t)
```

and radiogenic daughter growth. For ideal closed-system present-parent ratios:

```text
x = Pb206*/U238 = exp(lambda238 T_R) - 1
y = Pb207*/U235 = exp(lambda235 T_R) - 1
```

The two decay constants are physically distinct. DFM accepts ordinary measured prospective decay physics by default.

### R — Reconstruction

A common retrodictive duration is reconstructed when the two systems satisfy:

```text
T_R,238 = ln(1+x)/lambda238
T_R,235 = ln(1+y)/lambda235
T_R,238 ~= T_R,235
```

Eliminating `T_R` yields the concordia relation:

```text
1 + y = (1+x)^(lambda235/lambda238)
```

Concordance is therefore a highly structured relation, not generic "order."

### H — Historical interpretation

The historical claim is:

```text
T_R = T_H
```

for the relevant crystallization/closure event and subsequent history.

That identification may be strongly warranted when initial state, closure, disturbance, mineral behavior, and independent geological relationships are sufficiently constrained. It remains the historical/provenance step and is not identical to the measured isotope state or decay law.

## 3. Dependency graph

| Dependency | Role | Independence / coupling | Current appraisal |
|---|---|---|---|
| Isotope-ratio measurement | Establishes O | Analytical methods can differ; measurements share standards and corrections | Strong measurement layer |
| lambda238 | Maps U-238/Pb-206 state to R | Distinct decay system | Strong prospective physics |
| lambda235 | Maps U-235/Pb-207 state to R | Distinct decay system | Strong prospective physics |
| U isotopic abundance | Couples parent inventories | Shared elemental/isotopic architecture | Constrained, not independent of both systems |
| Zircon U/Pb partition behavior | Constrains initial Pb interpretation | Mineral-chemical dependency | Important |
| Common-Pb treatment | Separates non-radiogenic Pb | Method/model dependent but testable | Important auxiliary/calibration layer |
| Closure/retention | Connects daughter accumulation to event | Depends on thermal/diffusive history | Must be constrained case by case |
| Inheritance | Can preserve older domains | Geological/mineralogical history | Known failure mode with observable signatures |
| Pb loss | Produces discordance | Disturbance mechanism | Known failure mode; can be independently investigated |
| Mixing / alteration | Perturbs ratios | Geological/mineralogical history | Known failure mode |
| Concordant population structure | Cross-grain constraint | Partially independent analyses sharing decay model | Stronger than one grain |
| Stratigraphic/cross-cutting context | External ordering constraint | Different evidential stream, not wholly independent of geological interpretation | Potentially strong cross-check |
| Other isotope systems | Cross-system comparison | Distinct decay constants/chemistry, but may share geological event model | Potentially high-value dependency-aware consilience |

## 4. Failure modes

Known discordance does not automatically count against the conventional interpretation or for DFM.

A disturbance mechanism receives evidential credit when its predicted signature is independently constrained and subsequently observed.

Initial auxiliary grades:

- radioactive decay law: A1;
- zircon partition behavior: A1/A2;
- diffusion/retention behavior where experimentally constrained: A1/A2;
- independently demonstrated Pb loss/inheritance/alteration: A1-A4 depending on case;
- disturbance invoked only to restore a preferred age without independent signature: A5;
- unconstrained rescue mechanism: A6.

## 5. Conventional reconstruction

### Specify

Given measured isotope state, measured decay constants, appropriate treatment of common Pb, and a sufficiently constrained mineral history, reconstruct the duration associated with radiogenic daughter accumulation.

### Run

Apply the two U decay systems and test whether both recover the same `T_R`.

### Prediction / structural expectation

A closed system sharing one elapsed duration should occupy the decay-constant-indexed concordia relation. Disturbance mechanisms can produce structured departures whose form depends on the disturbance history.

### Evidential strength

U-Pb concordance earns substantially more weight than generic coherence because:

1. two decay systems with distinct decay constants participate;
2. one scalar duration constrains both relations;
3. zircon chemistry limits simple arbitrary initial-Pb explanations;
4. population structure and external geological relations can provide additional checks;
5. known disturbances can sometimes be diagnosed independently.

### Limitation

The strength of R does not erase the R -> H distinction. The historical identity depends on the provenance/closure/event model actually warranted for the sample or population.

**Current evidential level:** process-specific sequential consilience, reaching stronger levels in cases with independent event/provenance constraints.

## 6. DFM reconstruction

### DFM specification

```text
S0_rad = G(R, Uiso, P, X, F, L)
```

with source-reservoir composition, uranium isotopic architecture, mineral partition constraints, common/daughter Pb constraints, commissioned functional constraints, and ordinary physical law.

### Present DFM expectation

DFM expects an integrated rather than arbitrary initialized radiogenic state. This predicts generic coherence but does not yet predict the exact concordia locus.

### Current generator result

WP-008 and WP-009 found no presently specified age-independent DFM generator that derives:

```text
1 + y = (1+x)^(lambda235/lambda238)
```

across zircon populations without effectively importing `T_R`.

Radiogenic heat constrains parent architecture but does not generate the paired daughter ratios.

### Anti-circularity result

If initialized ratios are selected as:

```text
x0 = exp(lambda238 T_R) - 1
y0 = exp(lambda235 T_R) - 1
```

because the target sample has conventional retrodictive age `T_R`, the model has encoded the target and receives accommodation credit only.

Renaming `T_R` as another scalar parameter does not solve the problem if the new parameter has no independent physical content.

**Current evidential level:** generic coherence / accommodation for concordia; independent derivation not yet achieved.

## 7. Separate burden ledger

### Conventional burden

- establish that the relevant initial-state and closure assumptions are warranted for the specific application;
- demonstrate disturbance/inheritance/common-Pb corrections rather than merely assert them;
- establish the R -> H step with appropriate provenance and external constraints;
- avoid treating all concordant results as epistemically identical when dependency structures differ.

### DFM burden

- derive the dual-decay concordia relation from independently specified initialization constraints;
- respect zircon Pb partition/mineral chemistry;
- explain population structure rather than isolated grains;
- extend any generator beyond U-Pb without unrelated tuning;
- produce at least one discriminator not used to construct the generator.

Neither burden transfers to the other.

## 8. Bayesian appraisal

**Comparator:** conventional closed-system U-Pb radiogenic-growth model with sample-specific, independently evaluated geological/mineral-history auxiliaries.

**Region:** Historical Development.

**Dependency status:** partially dependent evidence network. The two decay chains are physically distinct but share sample history, mineral system, analytical/calibration context, and the common historical-duration hypothesis. External stratigraphic or cross-system checks must be evaluated for their own dependencies before multiplication.

**Numerical Bayes factor:** not assigned. Current programme models do not justify a defensible quantitative likelihood ratio.

**Ordinal likelihood appraisal:** U-Pb concordance presently favors the specified conventional historical model over the current DFM radiogenic-initialization auxiliary because the conventional model derives the decay-constant-indexed relation from elapsed time, while DFM has not independently derived that relation.

This is a Region II debit to current DFM, not a global posterior verdict on DFM's Region I initialization/provenance claims.

## 9. High-value discriminators

DFM gains material evidential standing here only if a generator specified independently of target ages predicts one or more of:

- a previously unused isotope-system relationship;
- a bounded systematic deviation from conventional concordia;
- a reservoir-specific covariance;
- a mineralogical dependency;
- a discordance pattern;
- another observable not used in constructing the generator.

A candidate non-temporal generator that merely reproduces existing concordia and remains observationally equivalent to elapsed time gains little comparative preference.

## 10. Falsification / progression pressure

### Against current DFM radiogenic auxiliary

Substantial negative pressure occurs if:

1. every viable concordance generator contains a latent age-equivalent scalar;
2. zircon chemistry excludes required initialized daughter states;
3. cross-system extension requires unrelated tuning;
4. conventional models continue to predict concordance and diagnostic discordance with materially lower parameter cost.

### Against a specified conventional application

A particular historical application is weakened if independently constrained initial/closure/disturbance conditions make its inferred history physically unreachable or if it predicts signatures that are not observed.

Such a failure debits that application. It is not automatically a positive DFM result.

## 11. Current disposition

**Severe Challenge / active.**

U-Pb is currently one of the strongest Region II nodes against the present DFM radiogenic auxiliary.

The correct programme response is neither to deny the measurements nor to grant `T_R = T_H` as an observation. It is to preserve the epistemic decomposition and attempt an independently specified generator under severe-test conditions.

## 12. Next actions

1. Activate WP-012 as the formal identifiability extension of CCN-001.
2. Add Rb-Sr and Sm-Nd to test whether three or more distinct decay constants overdetermine candidate non-temporal generators.
3. Separate exact mathematical concordance from real-data uncertainty and disturbance.
4. Identify external cross-checks and map their dependency structure before assigning additional Bayesian weight.
5. Enter CCN-001 into Bayesian Evidence Ledger v0.1 as a Region II datum favoring the specified conventional model, with no numerical Bayes factor.
