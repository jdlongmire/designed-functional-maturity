# DFM-PAM-014: U-238 Intermediate-Chain Initialization Sensitivity

**Status:** Reduced-chain prototype, not a calibrated nuclear heating model.

## Question
Does initializing stable Pb-206 daughter products by itself justify treating all U-238 parent transformations as immediate full-chain heat? **No.** The time distribution of daughter decay depends on initial intermediate radioactive populations.

## Implemented comparison
`research/rcim/track_a_u238_chain_sensitivity.py` solves a reduced four-stage U-238 -> U-234 -> Th-230 -> Ra-226 -> sink model using fourth-order Runge–Kutta integration. Short-lived intermediate steps are collapsed, and no complete-chain heat is assigned. Two explicit initialization cases are compared over an illustrative 6,000-year interval:

1. **Depleted chain:** U-238 present, modeled intermediates initially absent.
2. **Secular-equilibrium chain:** initial intermediate populations selected so each stage has the same activity as U-238.

The resulting activities are expressed as ratios to the surviving U-238 activity. The depleted-chain case cannot be assumed to have the same downstream heat release as an initialized equilibrium chain. Neither initial case is asserted as a historical fact.

## Physical and methodological constraints
- The reduced chain is **not** the complete U-238 chain. U-238 actually passes through Th-234 and Pa-234 before U-234, and through short-lived descendants after Ra-226. These omissions prevent calculation of physically complete energy release.
- Full-chain yield multiplied by U-238 decay rate is an equilibrium **approximation**, not an exact short-history result for arbitrary initialized populations.
- A secular-equilibrium boundary is a substantive DFM auxiliary hypothesis. It must be declared, physically evaluated and tested against U-series disequilibrium data, mineral chemistry and geological context.
- Stable initialized Pb-206 inventory is conceptually separate from initial radioactive intermediate inventory. Neither directly proves the other.
- A six-millennia scenario is a sensitivity example, not a date inferred from these calculations.

## Next acceptance gate
Implement complete Bateman decay chains for U-238, U-235 and Th-232, including branches and decay energy deposited locally rather than escaping as neutrinos. Validate against evaluated ENSDF/IAEA nuclear data and known U-series activity ratios. Only then compare integrated post-boundary heat for alternative initial-chain populations. Preserve the independent U-Pb mineral and geoneutrino constraints.

**Track A judgment:** A previously implicit equilibrium dependency has been exposed and parameterized; global thermal plausibility is not established.
