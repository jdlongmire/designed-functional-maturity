# DFM-PAM-016: Branch-Resolved Decay Network Foundation

**Status:** Generic Bateman-type numerical solver committed. Nuclear-data ingestion and full-chain physical validation are **not complete**.

## Implemented
`research/rcim/track_a_bateman_network.py` accepts nuclides with half-lives, daughter branches, branching probabilities and **deposited heat per branch** (J/decay). Stable sinks retain daughter atoms. It validates branch probabilities, integrates populations and deposited heat with fourth-order Runge–Kutta, and checks atom conservation. Its self-test uses a **synthetic** branched chain, not U/Th isotope data.

## Scope and physical limits
- A complete U-238, U-235 or Th-232 model requires evaluated half-lives, every relevant alpha/beta branch, intermediate populations, and branch-specific locally deposited energy accounting for neutrinos.
- The current generic solver treats each branch as yielding one daughter nuclide; alpha particles and beta leptons are not separately counted as nuclei, and its atom-conservation assertion therefore means **one tracked heavy-chain nucleus per initial tracked nucleus**, not full baryon conservation.
- Explicit fast daughters may impose numerical stiffness: the current fixed-step RK4 method is not suitable for spanning nanosecond-to-billion-year half-lives without adaptive stiff integration or analytic/aggregated fast-chain handling.
- Branch-specific deposited heat must include decay-energy accounting without double counting daughter transitions; assigning full-chain heat to every parent branch is invalid.
- The initial radioactive intermediate populations and stable daughter inventories remain independent boundary inputs.

## Validation gates
1. Ingest an evaluated, versioned ENSDF/IAEA/NNDC nuclear dataset with provenance.
2. Verify branch completeness, stable endpoints, energy deposition and unit conversions.
3. Introduce a stiff solver or validated fast-chain reduction; compare against analytic two-stage Bateman solutions.
4. Verify energy conservation and convergence under step refinement.
5. Compute depleted, equilibrium and constrained-boundary scenarios and compare activity trajectories and heat production.
6. Only then propagate into Earth reservoir inventories and thermal transport.

**Track A appraisal:** The computational architecture for branch-resolved post-boundary heat now exists. It does **not** yet establish a physically complete U/Th decay-chain solution or global thermal plausibility.
