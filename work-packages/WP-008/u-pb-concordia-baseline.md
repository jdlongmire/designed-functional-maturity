# U-Pb Concordia Severe-Test Baseline

## 1. Constants

Using Jaffey et al. (1971):

```text
half-life U-238 = 4.4683e9 yr
half-life U-235 = 7.0381e8 yr

lambda238 = ln(2) / half-life238
lambda235 = ln(2) / half-life235
```

## 2. Concordia equations

For closed-system radiogenic accumulation with negligible initial radiogenic daughter Pb:

```text
x(T) = Pb206*/U238 = exp(lambda238 T) - 1
y(T) = Pb207*/U235 = exp(lambda235 T) - 1
```

Here `T` is elapsed or retrodictive time; `x(T)` is the radiogenic Pb-206/U-238 ratio; `y(T)` is the radiogenic Pb-207/U-235 ratio; and `lambda238` and `lambda235` are the corresponding measured decay constants.

The concordia curve is the parametric locus `(x(T), y(T))`.

## 3. Initialization inversion

If DFM historical elapsed time after initialization is `tau`, but a zircon plots at conventional retrodictive age `T_R`, the boundary-state daughter ratios required to evolve to that point under ordinary decay are:

```text
x0 = [x(T_R) + 1] exp(-lambda238 tau) - 1
y0 = [y(T_R) + 1] exp(-lambda235 tau) - 1
```

Here `x0` and `y0` are the ratios required at initialization, `T_R` is the retrodictive duration represented by the target concordia point, and `tau` is actual post-initialization elapsed time.

For `tau << T_R`:

```text
x0 ~= x(T_R)
y0 ~= y(T_R)
```

Thus a short-history DFM does not erase the concordia burden. It relocates most of the required radiogenic structure to the initialization boundary.

## 4. Numerical examples

Approximate concordia ratios implied by selected conventional retrodictive ages:

| T_R (Ga) | Pb206*/U238 | Pb207*/U235 |
|---:|---:|---:|
| 0.5 | 0.081 | 0.637 |
| 1.0 | 0.168 | 1.676 |
| 2.0 | 0.364 | 6.169 |
| 3.0 | 0.593 | 18.19 |
| 4.0 | 0.860 | 50.45 |
| 4.4 | 0.980 | 75.1 |
| 4.55 | 1.026 | 87.2 |

Values are rounded baseline calculations using the Jaffey half-lives. They are not fitted to a particular zircon dataset.

## 5. Why convergence is nontrivial

If initialization independently assigns `x0` and `y0`, the probability of repeatedly landing on the one-dimensional concordia relation inside a two-dimensional ratio space is not explained.

Therefore “orderly initialization” becomes scientifically useful only if the generator reduces the two apparent degrees of freedom by a common constraint.

In conventional U-Pb, elapsed time `T` supplies that common parameter.

DFM requires a different common generator if it denies that `T` was traversed.

## 6. Heat-budget result

The heat budget constrains U abundance and, through isotope abundance, the U-238/U-235 parent architecture. It does not directly impose:

```text
y0 = f(x0)
```

with `f` equal to the concordia relationship.

Therefore:

```text
radiogenic heat constraint
    -> parent inventory constraint

radiogenic heat constraint
    !=> dual daughter concordia
```

This is the central quantitative result of the baseline severe test.

## 7. DFM-safe interpretation

The result should not be overstated.

It does not prove that no coherent initialization generator exists. It shows that the generator cannot be merely “Earth needed radiogenic heat.”

A successful extension must produce the daughter-parent relationship from independent common constraints and must operate at reservoir/mineral-population scale rather than by assigning an age-like state to each grain.

## 8. Research decision

**Do not promote “radiogenic heat explains radiometric concordance” as a DFM result.**

Promote instead:

> Radiogenic heat independently constrains part of the initialized parent-isotope architecture. DFM hypothesizes that the complete initialized state is globally coherent, but the observed dual U-Pb concordia relationship remains an unresolved quantitative test of that hypothesis.

This formulation preserves the insight that radiogenic inventory is functional while preventing the programme from claiming more than has been derived.
