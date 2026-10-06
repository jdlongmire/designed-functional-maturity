# WP-029B: Family A - Single Deployment Metric Feasibility

**Parent:** WP-029
**Status:** Feasibility model, not DFM conclusion

## Question

Can one spacetime metric generate a large difference between Earth-local elapsed time and non-terrestrial process proper time during Day 4 while preserving the causal invariants fixed by SN 1987A and transitioning coherently into ordinary runtime?

## Baseline

For a timelike worldline in a metric spacetime:

    d tau^2 = -(1/c^2) g_mu_nu dx^mu dx^nu

The deployment hypothesis seeks a metric g_D such that:

    Delta tau_E ~ 1 terrestrial day
    Delta tau_C >> Delta tau_E

for selected cosmic worldlines/process domains, while relevant fields and signals propagate consistently in the same geometry.

## Minimal ansatz

Begin with a spherically organized toy metric around the Earth-local reference domain:

    ds^2 = -N(r,t)^2 c^2 dt^2 + A(r,t)^2 dr^2 + R(r,t)^2 dOmega^2

For approximately comoving local observers:

    d tau(r) ~= N(r,t) dt

Choose Earth-local normalization N_E ~= 1 during Day 4. Large cosmic proper-time accumulation requires N_C/N_E >> 1 over relevant deployment regions.

This is a feasibility parameterization, not a solution of Einstein's equations.

## Immediate consequence

A large lapse contrast cannot be treated as an isolated clock effect. In a metric theory the same geometry affects photon null geodesics, neutrino trajectories, gravitational propagation, frequency/redshift relations, causal structure, and source/observer clock calibration. The metric must do the work coherently.

## SN 1987A constraint

SN 1987A is severe for Family A because photons and neutrinos associated with the event arrived close together. Relativity analyses use this coincidence to constrain differential propagation and gravitational delay.

Family A should therefore begin with common metric coupling for photons and neutrinos rather than separate propagation transformations.

## Candidate conditions

A1 Earth-local day:
    integral_Day4 d tau_E ~= 24 h

A2 Cosmic process depth:
    integral_Day4 d tau_C >> 24 h
if the strong LPI auxiliary is retained.

A3 Common causal structure:
Photons and ultrarelativistic neutrinos from one source event traverse a mutually consistent geometry.

A4 Local physics:
Along each local worldline, local microphysics remains internally coherent unless a separate auxiliary is explicitly introduced.

A5 Synchronization:
There exists a commissioning hypersurface Sigma_sync on which g_D -> g_R with induced geometry and relevant state variables joined without arbitrary resetting.

A6 Post-commissioning continuity:
The deployed SN 1987A state evolves continuously into the ordinary-runtime remnant later observed from Earth.

## First result: lapse alone is insufficient

The relation d tau ~= N dt demonstrates mathematical room for differential proper-time accumulation, but a large N_C/N_E is not a physical explanation. A candidate must derive or constrain N(r,t), A(r,t), and R(r,t) from stress-energy, creation-boundary conditions, a gravitational model, or another explicit physical structure. Otherwise Family A merely renames the desired acceleration factor as a metric coefficient.

## Redshift burden

Clock-rate differences and gravitational frequency shifts are generally coupled by the geometry. A large lapse contrast therefore creates a potentially severe spectral burden unless the full nonstationary deployment metric yields an acceptable derived frequency relation. Observed spectra are consequently a primary severe test.

## Synchronization burden

An abrupt assignment N_C >> 1 -> N = 1 at the end of Day 4 is not sufficient. The model must specify a transition geometry and matching conditions. At minimum, the induced geometry and causal state on Sigma_sync must be well-defined.

## Preliminary disposition

**Family A is mathematically conceivable at the level of differential proper time but not yet physically demonstrated.**

Three coupled burdens are exposed:

1. field-equation burden: derive a metric rather than stipulate a lapse;
2. spectral burden: obtain acceptable frequency/redshift behavior from that metric;
3. matching burden: transition to ordinary runtime without resetting the created state.

These burdens are strong enough that Family A can genuinely fail.

## No-go criteria

Demote or reject Family A if every candidate single metric requires observation-specific lapse functions, separate ad hoc metrics for different messengers/processes, spectral corrections not derived from the metric, a discontinuous commissioning reset, physically uninterpretable boundary/stress-energy content, or loss of SN 1987A cross-messenger causal relationships.

## Next derivation

Test the simplest subfamily in which lapse varies primarily with deployment time and radial domain, and calculate jointly:

    proper-time ratio
    + radial null propagation
    + frequency shift
    + Sigma_sync matching

before adding fields or temporal domains.

If the minimal subfamily fails, record that failure before increasing freedom.


## Minimal subfamily calculation: separable lapse screen

To expose the constraints before solving a full field equation, take the restricted ansatz

    ds^2 = -N(r,t)^2 c^2 dt^2 + a(t)^2 [dr^2 + r^2 dOmega^2]

with Earth-local normalization N(r_E,t)=1.

For a comoving timelike observer at fixed r:

    d tau(r) = N(r,t) dt

so over the Day 4 coordinate interval T_E:

    Delta tau_C(r) / Delta tau_E
      = [integral_0^T_E N(r,t) dt] / T_E
      = <N(r,t)>_Day4.

Thus a strong LPI requirement Delta tau_C >> Delta tau_E demands a correspondingly large mean lapse in the relevant cosmic domain.

### Radial null propagation

For ds^2=0 and dOmega=0:

    dr/dt = +/- c N(r,t) / a(t).

Therefore the same lapse that increases local cosmic proper-time accumulation also changes radial signal propagation in the common coordinate description. The proper-time effect and the travel-time effect are not independent knobs.

For a source r_s and observer r_E, a radial null ray must satisfy:

    integral_(r_E)^(r_s) dr
      = integral_(t_emit)^(t_obs) c N[r(t),t] / a(t) dt.

Any proposed N(r,t) must therefore satisfy both the process-depth requirement and the source-observer propagation constraint.

### Frequency constraint

For a photon with wave vector k^mu and an observer with four-velocity u^mu, the measured frequency is

    omega = -k_mu u^mu.

Hence the observable frequency ratio is

    omega_obs / omega_emit
      = (k_mu u^mu)_obs / (k_mu u^mu)_emit.

In a stationary lapse-dominated limit this reduces to the familiar gravitational clock/frequency linkage, schematically

    omega_obs / omega_emit ~ N_emit / N_obs,

subject to sign/convention and full-metric details.

The consequence is decisive for the toy model: if N_C/N_E is extremely large and the geometry is approximately stationary while the signal traverses it, an equally extreme frequency shift is generically expected. The observed spectrum therefore prevents treating N_C/N_E as a free acceleration factor.

A viable Family A solution must use a genuinely nonstationary deployment geometry, spatial structure, or derived cancellation that jointly produces the desired proper-time depth and acceptable observed spectra. Such a cancellation must emerge from the metric solution, not be imposed as a separate spectral correction.

## Commissioning surface as a junction problem

Let Sigma_sync separate deployment geometry g_D from ordinary-runtime geometry g_R.

For a smooth GR matching without an impulsive surface layer, require at minimum the Darmois-Israel conditions

    [h_ab]_Sigma = 0
    [K_ab]_Sigma = 0,

where h_ab is the induced metric and K_ab the extrinsic curvature of Sigma_sync.

If [K_ab] != 0, the jump corresponds to a surface stress-energy layer rather than a cost-free synchronization operation.

Accordingly, DFM Family A adopts the following default:

> **No-shell commissioning criterion:** prefer candidate deployment metrics that approach ordinary runtime with continuous induced geometry and extrinsic curvature at Sigma_sync. Any thin-shell or distributional transition must be explicitly modeled and counted as an additional physical auxiliary.

This turns "synchronization" into a genuine matching problem.

## Minimal-subfamily verdict

The separable/lapse-dominated screen yields a useful negative result.

A large N_C/N_E can trivially generate large differential proper time, but the same N enters null propagation and, in simple stationary limits, the frequency relation. Therefore:

    large proper-time gain
      + acceptable propagation
      + ordinary-looking spectra
      + smooth commissioning

cannot be obtained merely by choosing a large lapse.

The minimal lapse-only explanation is **insufficient**.

This does not reject Family A. It rejects the idea that Family A can be reduced to a scalar "cosmic clock multiplier."

## What remains viable inside Family A

A viable single-metric candidate now needs all of:

1. substantial nonstationarity and/or spatial structure;
2. a metric derived from explicit boundary/stress-energy assumptions;
3. common geodesic treatment of coupled messengers;
4. derived, observationally acceptable frequency/redshift behavior;
5. Darmois-Israel-compatible commissioning, or an explicitly modeled shell;
6. post-commissioning continuity of deployed causal state.

## Decision gate

**Do not yet move to Family B.**

Family A survives the first screen, but its simplest lapse-only form does not. The next test should attempt a structured nonstationary metric family and ask whether the needed proper-time differential can coexist with acceptable redshift and junction conditions without introducing an equivalent number of hidden free functions.

If that structured Family A attempt also collapses into unconstrained function choice, record the failure and advance to Family B.
