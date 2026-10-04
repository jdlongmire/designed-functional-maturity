# Rb-Sr Isochron Decomposition

## Core equation

```text
87Sr/86Sr_now
  = 87Sr/86Sr_initial
  + (87Rb/86Sr)_now [exp(lambda87 t) - 1]
```

or:

```text
y = b + mx
```

## DFM decomposition

| Component | Conventional role | Reservoir-level DFM status |
|---|---|---|
| `b` | common initial 87Sr/86Sr | Can be constrained by common source reservoir |
| `x` spread | different 87Rb/86Sr among phases | Can arise from chemical/mineral partitioning |
| linearity | common source + closed evolution | Partly testable through reservoir/process model |
| `m` | radiogenic growth | Not independently derived by current DFM |
| `t = ln(1+m)/lambda` | elapsed age | Retrodictive age unless provenance warrants historical identity |

## Initialization burden

For short actual elapsed time `tau` and conventional retrodictive time `T_R`:

```text
m_required_at_initialization
  ~= exp(lambda87 T_R) - exp(lambda87 tau)
```

For `tau << T_R`:

```text
m_initialization ~= exp(lambda87 T_R) - 1
```

Thus a mature initialized suite must contain a population-level daughter-parent covariance approximating the conventional isochron slope.

## Key discriminator

The physically motivated reservoir model already predicts variation in `x`.

Therefore the unresolved question is unusually narrow:

> Why should initialized `y-b` be proportional to `x` by a coefficient indexed to the Rb-87 decay constant?

No current DFM mechanism answers that question independently.

## Mixing caveat

Two-component or multi-component mixing can produce linear or near-linear isotope arrays. Therefore observed linearity is not sufficient by itself to prove radiogenic age.

But this does not rescue DFM generically:

- mixing must be independently demonstrated;
- high-quality isochron practice tests for mixing and alteration;
- cross-system concordance remains after many such controls;
- a universal “mixing” response would violate the no-free-lunch rule.

## Research verdict

**Parent/reference structure: partly derived.**

**Radiogenic slope: underived.**

**Cross-system slope concordance: high-pressure unresolved test.**
