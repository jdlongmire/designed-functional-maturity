# DFM-PAM-018: Stiff-Safe Bateman Solver

**Status:** Matrix-exponential solver committed, synthetic and analytic tests configured; evaluated U-238 network not yet loaded.

## Numerical approach
`research/rcim/track_a_stiff_bateman.py` constructs a linear decay generator for arbitrary branch-resolved heavy-nuclide networks and propagates populations with `scipy.linalg.expm`. An augmented state integrates deposited heat in joules over the interval without a uniform RK4 time step. This is suitable for widely separated decay rates, subject to conditioning and physical-data verification.

## Verification
- Synthetic A -> B -> C with a 10^15-fold contrast in half-lives; checks atom conservation and limiting integrated energy.
- Exact two-stage Bateman comparison with nonzero initialized intermediate population.
- Zero-duration and negative-input checks.
- GitHub Actions installs NumPy and SciPy and runs the new fixture; workflow success must be inspected.

## Required physical data
The solver is deliberately generic. It does **not** yet contain a complete evaluated U-238 chain. Before physical claims, version-pin ENSDF/NNDC/IAEA half-lives, branch probabilities, metastable transitions, decay energies net of neutrino losses, and initial daughter inventories. Confirm that collapsed alpha and beta products are counted consistently and no branch energy is duplicated.

## DFM inference
This removes the principal *numerical-method* barrier to modeling explicit intermediate populations over a short post-boundary history. It does not resolve the *empirical* question of which intermediate populations were initialized or whether U-Pb mineral evidence, geoneutrino flux, and thermal history are jointly accommodated.

**Next gate:** Implement a complete source-audited U-238 network and independently compare depleted, equilibrium and constrained intermediate-boundary scenarios for time-dependent power and integrated heat.
