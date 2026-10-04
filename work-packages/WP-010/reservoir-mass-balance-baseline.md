# Reservoir Mass-Balance Baseline Model

## Objective

Define the minimum mathematical structure for a DFM radiogenic source-reservoir model and identify what it predicts without radiometric-age inputs.

## A. Conservation

For each species `k`:

```text
M_k,total = Sum_r M_k,r
```

For each reservoir:

```text
M_r = Sum_k M_k,r
```

The model must close both species and reservoir mass balances.

## B. Partitioning

For a mineral `m` and source reservoir `r`:

```text
C_E,m = D_E^(m/r) * C_E,r
```

This predicts elemental enrichment/depletion patterns when `D_E` and phase fractions are independently constrained.

## C. Isotopic composition

For isotope `i` of element `E`:

```text
M_E,r = Sum_i M_i,r
```

Absent a specified fractionation process, elemental partitioning must not be treated as freely assigning isotope ratios.

## D. Radiogenic evolution

After initialization:

```text
N_P(t) = N_P(0) exp(-lambda t)

N_D*(t) = N_D*(0) + N_P(0)[1 - exp(-lambda t)]
```

Ordinary decay is retained.

## E. What the reservoir model can derive

Without age fitting, the baseline model can in principle derive:

- bulk and reservoir parent abundance;
- parent/reference elemental ratios;
- covariance of elemental ratios across co-genetic phases;
- constraints on common daughter inventory;
- population relationships induced by common source and partition history;
- present-state change from the actual post-initialization interval.

## F. What it cannot yet derive

Without an additional generator, it does not derive:

- U-Pb concordia position;
- Rb-Sr isochron radiogenic slope;
- Sm-Nd isochron radiogenic slope;
- Pb-Pb age slope;
- extinct-radionuclide daughter excesses that mimic a specific decay interval.

## G. Cross-system constraint vector

For each reservoir `r`:

```text
V_r = [
 U238, U235, Pb204, Pb206, Pb207, Pb208,
 Rb87, Sr86, Sr87,
 Sm147, Nd143, Nd144,
 Lu176, Hf176, Hf177,
 Re187, Os186, Os187,
 K40, Ar40,
 Th232,
 phase fractions,
 heat contribution
]
```

A mature DFM model must generate the vector jointly, not one clock at a time.

## H. Complexity ledger

For every future model revision record:

```text
N_obs  = independent observational constraints
N_free = unconstrained initialization parameters
rho    = N_free / N_obs
```

Desired programme behavior:

```text
d(rho)/d(N_obs) < 0
```

That is, adding independent observations should increasingly constrain the model rather than require proportionate new freedom.

## I. Baseline verdict

**Reservoir mass balance is necessary and productive, but not sufficient for radiometric concordance.**

The next discriminator is an explicit Rb-Sr isochron decomposition.
