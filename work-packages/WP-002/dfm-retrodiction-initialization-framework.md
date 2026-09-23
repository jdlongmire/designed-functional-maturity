# DFM Retrodiction and Initialization Framework

**Artifact:** WP-002 / WS-1 + WS-2  
**Status:** Working baseline  
**Date:** 23 September 2026

## 1. Scope

This framework defines the epistemic boundary between present observation, model-conditioned reconstruction, and actual history within Designed Functional Maturity (DFM). It also constrains what DFM may legitimately place in an initialized state.

The framework is intentionally prior to particular radiometric, geological, astronomical, or biological applications.

## 2. Primitive terms

Let:

```text
O_t = observational state available at time t
M   = model or dynamical law-set
A   = auxiliary assumptions required to apply M
B   = boundary conditions supplied to the reconstruction
R   = reconstructed antecedent trajectory
H   = actual historical trajectory
S_0 = initialized physical state
F   = immediately functional component of S_0
I_s = state-consistent initialization information in S_0
```

### 2.1 Observation

An **observation** is a measured or otherwise directly detected state/property of the system at the observational boundary.

Examples include isotope ratios, concentrations, spectra, spatial relationships, heat flow, retained gases, mineral structure, sequence relationships, and present rates.

An age, causal history, or antecedent trajectory inferred from those observations is not itself an observation.

### 2.2 Model

A **model** is a formal or conceptual representation specifying lawful relationships or state transitions.

A model may be empirically well-supported prospectively while its retrodictive use still depends on boundary and auxiliary assumptions.

### 2.3 Auxiliary assumption

An **auxiliary assumption** is a proposition required to connect a model to a particular inference but not contained in the observation itself.

Examples may include system closure, initial daughter inventory, equilibrium, constancy of relevant conditions, calibration relationships, or assumptions about unobserved state history.

### 2.4 Boundary condition

A **boundary condition** specifies a state or constraint from which model evolution or reconstruction is evaluated.

Boundary conditions are inputs to an inference. Their justification must not be obtained solely by assuming the historical reconstruction they are used to generate.

### 2.5 Retrodiction

A **retrodiction** is a model-conditioned reconstruction of antecedent state or elapsed duration from a later observational state.

Formally:

```text
R = R(O_t | M, A, B)
```

### 2.6 Provenance

**Historical provenance** is the warranted identification of an observed state with the actual causal trajectory by which that state came to exist.

A model showing that trajectory R could produce O_t establishes compatibility. Establishing that R actually produced O_t requires provenance warrant.

### 2.7 Historical trajectory

```text
H = the sequence of states/events that actually occurred
```

The central distinction is:

```text
R is a reconstruction.
H is an ontological fact about what occurred.
```

A valid R does not by logical necessity entail R = H.

## 3. Retrodictive and historical age

Define:

```text
T_R = T(O_t | M, A, B)
T_H = actual elapsed duration in H
```

**Retrodictive age (T_R)** is the duration returned by a specified reconstruction.

**Historical age (T_H)** is the duration that actually elapsed.

Therefore:

```text
T_R = T_H
```

is a substantive historical claim. It may be strongly warranted, weakly warranted, or underdetermined depending on the independence and quality of the provenance evidence.

The framework does not presume T_R != T_H. It denies only that T_R = T_H follows analytically from the existence of a successful retrodiction.

## 4. Reconstruction conditions

A retrodiction gains historical force as the following increase:

1. independent constraint on B;
2. independent constraint on A;
3. prospective validation of M in the relevant regime;
4. uniqueness or near-uniqueness of the reconstructed trajectory;
5. agreement across genuinely independent observables;
6. external historical or event constraints;
7. successful novel predictions or risky consequences of the reconstruction.

A retrodiction loses historical force when multiple materially different antecedent states or trajectories produce the same observed state under comparably warranted models.

## 5. Reconstruction underdetermination

Define the admissible antecedent set:

```text
P(O_t) = { S_i : F_M,A(S_i, Delta t) is compatible with O_t }
```

If:

```text
|P(O_t)| > 1
```

then O_t alone does not uniquely identify its antecedent state.

This is an epistemic result. It does not imply that no unique history occurred. Exactly one actual history may have occurred while present evidence underdetermines which admissible reconstruction is that history.

## 6. DFM initialization

DFM proposes an initialized physical boundary:

```text
S_0 = F + I_s
```

where:

- **F** contains structures required for immediate intended function.
- **I_s** contains information/state variables that accompany a physically coherent initialized state.

This is not equivalent to placing an arbitrary fictive history in S_0.

### 6.1 Class I: functional initialization

A feature qualifies provisionally as functional initialization when removing it would prevent or materially defeat the immediate intended operation of the initialized system.

### 6.2 Class II: state-consistent initialization information

A feature qualifies provisionally as state-consistent initialization information when it is physically coupled to, entailed by, or independently motivated as part of the coherent initialized state, even if it can also be mapped by a retrodictive model onto an antecedent trajectory.

### 6.3 Class III: historical trace

A feature qualifies as a historical trace when independent evidence warrants that it was generated by an event occurring after S_0.

The burden rises with specificity. A feature that purports to encode a particular event, actor, date, sequence, or contingent occurrence requires stronger justification as initialization information than a generic state variable required for immediate physical coherence.

## 7. Operational no-smuggling rule

**NS-1.** Observations must be stated first in non-historical measurement language where practicable.

**NS-2.** Derived ages and trajectories must identify M, A, and B sufficiently to expose the inferential bridge.

**NS-3.** A retrodictive output may not be used as independent evidence for an auxiliary assumption already required to produce that output.

**NS-4.** DFM may not relabel a historical trace as initialization merely because its conventional T_R conflicts with DFM chronology.

**NS-5.** Competing programmes may not relabel model-conditioned reconstruction as direct observation merely because the model is conventional.

Violation of NS-3 is circular support. Violations of NS-4 or NS-5 are programme-protective smuggling.

## 8. Operational no-free-lunch rule

A proposed initialization parameter I_i is admissible only if at least one independent constraint C_j bears on it:

```text
Admissible(I_i) only if exists C_j independent of desired chronology
such that C_j constrains I_i
```

Relevant constraint classes include:

- immediate functionality;
- physical coupling/coherence;
- conservation constraints;
- canonical boundary conditions;
- independently measured state relationships;
- cross-system concordance;
- consequences testable outside the chronology being protected.

An initialization parameter introduced solely because it yields the preferred T_H is ad hoc and counts against DFM.

## 9. No chronology rescue rule

The following inference is invalid:

```text
T_R conflicts with preferred T_H
therefore alter B until T_R is compatible with preferred T_H
```

Likewise:

```text
T_R conflicts with preferred T_H
therefore alter a measured physical rate
```

is invalid absent independent evidence for rate variation.

DFM must absorb unresolved discrepancies as unresolved rather than purchasing agreement through unconstrained auxiliaries.

## 10. Concordance rule

Concordance is evidentially strong to the degree that converging reconstructions are genuinely independent.

For reconstructions R_1 ... R_n, the evidential question is not merely:

```text
T_R1 ~= T_R2 ~= ... ~= T_Rn
```

but whether the systems share calibration assumptions, boundary conditions, samples, correction models, or common causal dependencies.

Where independence is established, concordance increases the burden on alternative initialization models.

DFM must seek a common cause or common initialized constraint capable of explaining the concordance without assigning arbitrary independent initial values to each system.

## 11. Provenance warrant test

Before identifying T_R with T_H, ask:

1. What exactly was measured?
2. What model transforms the measurement into elapsed time?
3. Which auxiliaries are required?
4. Which boundary conditions are assumed?
5. Which of those are independently constrained?
6. Are materially different antecedent states compatible with the observation?
7. Do independent systems converge?
8. Are those systems genuinely independent?
9. Is there an external known-age or historical calibration?
10. What observation would discriminate the proposed provenance from a rival initialization/history?

The purpose is symmetric scrutiny. The test applies to DFM and competing programmes.

## 12. Falsification conditions for the initialization auxiliary

The DFM initialization auxiliary is weakened if:

- required initial values proliferate independently across datasets;
- initial values are selected primarily to preserve chronology;
- cross-system concordance has no common explanation;
- initialized features encode specific contingent histories without functional, physical, or canonical warrant;
- proposed initialization violates conservation or other well-tested physical constraints;
- a rival historical trajectory predicts discriminating observations that DFM does not;
- DFM repeatedly adds new initialization clauses after contrary observations.

The auxiliary is strengthened if one constrained S_0 generates multiple independent observed relationships and novel consequences without dataset-specific adjustment.

## 13. Relationship to radiogenic inference

The framework does not decide radiometric chronology in advance.

For radiogenic systems the initial decomposition is:

```text
O_iso + M_decay + B_initial + G_history -> T_R
```

The next workstream must identify which terms are measured, which are experimentally constrained, which are inferred, and which can be independently calibrated.

Measured ordinary decay behavior remains the prospective default. Accelerated decay is not implied by a short historical chronology and receives no privileged place in the framework.

## 14. Governing propositions

**P1.** Observation and historical reconstruction are categorically distinct epistemic products.

**P2.** A successful retrodiction establishes model-conditioned compatibility before it establishes provenance.

**P3.** Historical identification R = H requires warrant beyond the bare existence of R.

**P4.** DFM initialization is constrained initialization, not arbitrary assignment of antecedent-looking state.

**P5.** Initialization freedom cannot be purchased by chronology conflict.

**P6.** Genuine independent concordance is evidence that DFM must explain rather than dismiss.

**P7.** Physical rates are not altered to rescue chronology without independent empirical warrant.

**P8.** Unresolved accounting remains unresolved. It is not evidence for whichever programme currently lacks an explanation.

## 15. Next gate

WS-1 and WS-2 are provisionally complete when this framework survives adversarial application to a concrete inference system.

The first gate is radiogenic inference:

```text
measurement -> isotope model -> initial-state assumptions
-> geochemical history -> retrodictive age -> provenance claim
```

WS-3 must now construct the evidence ledger and known-age calibration dataset from primary technical sources before the flagship DFM paper is revised.
