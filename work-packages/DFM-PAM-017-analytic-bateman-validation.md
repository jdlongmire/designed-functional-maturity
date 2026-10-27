# DFM-PAM-017: Analytic Bateman Verification and Stiffness Gate

**Status:** Mathematical verification fixture committed. Complete evaluated U-238 decay chain **not** implemented.

The executable `research/rcim/track_a_bateman_analytic_validation.py` compares the numerical RK4 solver with the analytic two-stage Bateman solution for A -> B -> C, including nonzero initial B populations, equal and nearly equal half-lives, and integrated deposited energy. The analytic solution uses exact exponential propagation and conservation to compute the stable sink. Synthetic heat yields of 2 J and 3 J per transformation are deliberate test fixtures, not physical decay energies.

## Why this gate precedes a complete U-238 chain

The U-238 chain spans extremely short and extremely long half-lives. Explicitly integrating every nuclide with a uniform RK4 step over thousands of years is computationally impractical and can be unstable. A correct implementation must use a stiff integrator, matrix exponential, or rigorously validated elimination of short-lived intermediates. The current RK4 network is a useful verification prototype but must **not** be used as a complete U-238 solver merely by entering isotope data.

## Acceptance criteria for physical chain integration

1. Pin evaluated nuclear-data versions and source records for each isotope, half-life, branch, and energy deposition (ENSDF/NNDC/IAEA).
2. Confirm every branch terminates at a tracked daughter or stable sink; include alpha, beta and electron-capture pathways as applicable.
3. Validate a stiff/analytic solver against this two-stage reference, atom conservation and integrated energy for both depleted and nonzero intermediate initial populations.
4. Compare step refinement and convergence across timescales before reporting post-boundary heat.
5. Preserve distinct initial conditions for stable Pb-206 and radioactive intermediates; quantify secular-equilibrium assumptions rather than imposing them.
6. Only after these gates, propagate results to the sourced crust/mantle inventory and evaluate independent geochemical constraints.

**Track A conclusion:** Numerical population/energy verification is improved, but the physical U-238 heat-history question remains open. A full-chain model is not established by a generic solver.
