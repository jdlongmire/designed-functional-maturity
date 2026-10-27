# DFM-PAM-015: Intermediate-Chain Activity Trajectories

**Status:** Reduced U-238 chain time-series diagnostics implemented; complete-chain heat modeling remains open.

## Method
`research/rcim/track_a_u238_chain_timeseries.py` reports activities normalized to surviving U-238 parent activity at 0, 100, 1,000, and 6,000 years for depleted and secular-equilibrium initialization. It also supports a third class: **user-specified initial activity ratios** for U-234, Th-230 and Ra-226. All values are explicit model parameters, not inferred historical boundary conditions.

## Why it matters
A stable Pb-206 inventory can be initialized independently of radioactive U-series intermediate populations. The depleted and equilibrium cases imply different short-time daughter activity trajectories. The equilibrium case is a separately testable auxiliary, not a logical consequence of initialized stable daughters.

## Interpretive limits
This four-stage reduction collapses the short-lived intermediates, including Th-234/Pa-234 and downstream Ra-226 products. It is appropriate only for the slow-chain population sensitivity it explicitly represents. It **cannot** determine complete-chain deposited energy, spatial heat generation, U-Pb mineral concordance, or terrestrial thermal plausibility. A fully specified physical model must use evaluated branching and energy data and independently constrained initial intermediate inventories.

## Next gate
Obtain complete evaluated chain data; implement a conservation-checked Bateman solver with branch-specific deposited energies; compare time-integrated heat and present power for explicit initialization scenarios; then propagate those constraints through the independently sourced Earth inventory without assuming secular equilibrium by default.
