# DFM Framework

## Core model

Let:

```text
O_t = observed state at time t
M   = model or dynamical structure
A   = auxiliary assumptions
B   = boundary conditions
R   = retrodictively reconstructed trajectory
H   = actual historical trajectory
```

Then:

```text
R = R(O_t | M, A, B)
```

A successful reconstruction establishes model-conditioned compatibility. It does not establish by logical necessity `R = H`. Historical identification requires additional provenance warrant.

## Age terminology

- **Historical age (T_H):** actual elapsed duration.
- **Retrodictive age (T_R):** duration reconstructed under observations, model, auxiliaries, and boundary conditions.
- **Extrapolated age:** acceptable public-facing term subordinate to retrodictive age.

## Initialization

```text
S_0 = F + I_s
```

`F` denotes structures required for immediate intended function. `I_s` denotes state-consistent initialization information. Proposed initialized parameters require independent constraint.

## Programme-wide rules

**No smuggling.** Neither DFM nor competing programmes may present model-conditioned reconstruction as direct observation. DFM may not relabel inconvenient historical traces as initialization merely to protect chronology.

**No free lunch.** Initialization parameters require constraint independent of the chronology they are invoked to protect.

**Symmetric burden.** Auxiliaries and model revision are normal research tools. DFM is neither exempt from their explanatory cost nor categorically forbidden from using them. Competing models receive the same treatment.

**Concordance.** Genuine independent convergence increases evidential force and must be explained.

**Physical-rate discipline.** Chronology conflict alone does not warrant changing an experimentally measured physical rate.

**Unresolved accounting.** Where no warranted account is available, record the matter as unresolved.

## Provenance

Detailed formal development currently resides in `work-packages/WP-002/dfm-retrodiction-initialization-framework.md`. WP-004 promotes that material without erasing its originating record.
