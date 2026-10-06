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


## Structured nonstationary test: one-profile Family A

To avoid solving the previous problems by independent tuning, constrain the deployment metric to one temporal deployment profile q(t) and one fixed spatial shape f(r):

    ds^2 = -exp[2 lambda q(t) f(r)] c^2 dt^2
           + a(t)^2 exp[2 mu q(t) f(r)] dr^2
           + R(r,t)^2 dOmega^2

with

    q(t_start) = 0
    q(t) > 0 during deployment
    q(t_sync) = 0.

The constants lambda and mu set temporal and radial response to one common deployment field. The spatial function f(r) is fixed before fitting individual observations. q(t) is global to the deployment episode.

This deliberately forbids a separate lapse function, propagation function, spectral correction function, and synchronization function.

### Proper-time condition

For approximately comoving observers:

    d tau(r) = exp[lambda q(t) f(r)] dt

and therefore

    Delta tau_C(r)
      = integral exp[lambda q(t) f(r)] dt.

A large process-depth ratio remains mathematically possible when lambda q f is sufficiently positive over the cosmic deployment region.

### Null propagation condition

For radial null curves in the reduced sector:

    dr/dt
      = +/- (c/a)
          exp[(lambda - mu) q(t) f(r)].

Thus the same q(t) controlling proper-time accumulation also controls radial propagation. The special relation

    lambda ~= mu

suppresses direct coordinate propagation enhancement while still allowing local proper-time differences.

This is not yet a solution. It identifies a potentially useful constrained subfamily.

### Important tradeoff

If lambda = mu exactly, the t-r sector receives a common conformal factor:

    ds^2_(t,r)
      = exp[2 lambda q f]
        [-c^2 dt^2 + a(t)^2 dr^2].

Null paths in that two-dimensional sector are conformally invariant as unparameterized curves. This helps avoid arbitrary messenger-specific path changes.

However, conformal structure does not make the model free:

- timelike proper times still change;
- photon frequency measurements still depend on emitter/observer four-velocities and the evolving geometry;
- curvature and stress-energy requirements remain;
- angular/areal geometry must be specified consistently;
- q(t) must return to zero without generating unacceptable junction behavior.

The same feature that makes this subfamily attractive therefore creates a sharp test: can one common deployment field alter timelike process depth substantially while leaving the observed null causal network and spectra acceptable?

### Smooth commissioning profile

Impose

    q(t_sync) = 0
    q_dot(t_sync) = 0

as a minimal smooth-exit condition.

These conditions make the metric coefficients and their first temporal derivatives approach the ordinary-runtime form at commissioning, improving the prospect of satisfying induced-metric and extrinsic-curvature matching without a thin shell.

A stronger implementation should also constrain higher derivatives if curvature scalars or stress-energy become singular.

### Parameter economy

The admissible freedom in this test is intentionally small:

    Theta_A1 = {lambda, mu, parameters of one q(t), parameters of one f(r), ordinary a(t)/R(r,t) specification}.

The model is not allowed to introduce separate q_photon, q_neutrino, q_decay, q_stellar, or q_sync functions.

### Field-equation burden

Given a candidate g_D, compute

    G_mu_nu[g_D] + Lambda g_mu_nu

and infer the effective source required by

    G_mu_nu + Lambda g_mu_nu = (8 pi G / c^4) T_mu_nu.

This reverses the usual construction initially: rather than guessing exotic matter first, determine what stress-energy or creation-boundary source the proposed geometry would require.

The resulting T_mu_nu becomes a discriminator. If it is singular, observation-specific, internally inconsistent, or requires an unexplained exotic source with no independent role, the metric is penalized.

### Spectral test

For every candidate q(t), calculate photon wave-vector transport

    k^nu nabla_nu k^mu = 0

and observer frequency

    omega = -k_mu u^mu

from emission through observation.

No post hoc spectral correction is permitted.

The same calculation must eventually be compared against redshift/spectral observations and SN 1987A line constraints.

### Cross-messenger test

At first pass, photons, neutrinos, and gravitational disturbances couple to the same g_D. Differences arise only from their physical equations/masses/interactions, not from separate temporal maps.

This is the preferred high-constraint implementation.

### Provisional result

The one-profile construction shows that Family A has a nontrivial constrained research path. In particular, the near-conformal lambda ~= mu subfamily offers a mathematically motivated way to separate large timelike proper-time accumulation from arbitrary changes to radial null paths.

But it has **not** solved the spectral, source, or full matching problem. Those become the decisive tests.

Accordingly:

**Family A remains active, but only in constrained one-profile form.**

The unconstrained statement "cosmic time ran faster" remains rejected as insufficient.

## Family A promotion/demotion gate

Promote Family A from feasibility to developed candidate only if a concrete q(t), f(r), lambda, mu choice can jointly:

1. generate the required process-depth ratio;
2. preserve the SN 1987A causal DAG;
3. derive acceptable photon/neutrino propagation;
4. derive acceptable spectral behavior;
5. produce a physically interpretable effective T_mu_nu or boundary source;
6. approach Sigma_sync smoothly;
7. generate at least one discriminator beyond the observations used to construct it.

Demote Family A if satisfying items 1-6 requires independent compensating functions or observation-by-observation tuning.

## Next computation

Use the near-conformal subfamily lambda = mu as the next severe test. Choose a simple compact-support or smooth pulse q(t) satisfying q=q_dot=0 at both deployment boundaries, then derive:

    Delta tau_C / Delta tau_E
    radial null relation
    photon frequency transport
    effective curvature / T_mu_nu scaling
    commissioning regularity.

This should determine whether the apparent economy of the conformal subfamily is genuine or merely moves the required complexity into q(t), f(r), and the effective source.


## Near-conformal severe test: smooth Day-4 pulse

Set lambda = mu and define

    Omega(r,t) = exp[lambda f(r) q(t)].

In the reduced time-radial sector:

    ds^2_(2) = Omega^2 [-c^2 dt^2 + a(t)^2 dr^2].

Choose the simplest finite pulse satisfying the first-order commissioning conditions:

    q(t) = Q sin^2(pi t / T),    0 <= t <= T
    q(t) = 0,                    outside deployment,

where T is the Earth-local Day-4 coordinate interval.

Then

    q(0) = q(T) = 0
    q_dot(0) = q_dot(T) = 0

and

    q_dot(t) = (pi Q/T) sin(2 pi t/T).

The metric and its first temporal derivative therefore return continuously to the ordinary-runtime values at both boundaries. The second derivative is finite but generally nonzero at the endpoints, so stronger smoothness may later motivate a higher-order bump function.

### Proper-time gain

For a comoving observer at fixed r with beta(r)=lambda f(r):

    Delta tau(r)
      = integral_0^T exp[beta q(t)] dt
      = T exp(beta Q/2) I_0(beta Q/2),

where I_0 is the modified Bessel function.

Therefore the process-depth ratio is

    R_tau(beta Q)
      = Delta tau(r)/T
      = exp(z) I_0(z),

with z = beta Q/2.

For large z,

    I_0(z) ~ exp(z)/sqrt(2 pi z),

so

    R_tau ~ exp(beta Q) / sqrt(pi beta Q).

This is important: enormous proper-time ratios do not require an enormous dimensionless exponent. The required beta Q grows only logarithmically with the target ratio.

For illustration only, a ratio of order 10^12-10^13 corresponds to beta Q of order several tens, not 10^12-10^13.

### Radial null paths

Because the reduced t-r sector is conformally related,

    ds^2_(2)=0
      => dr/dt = +/- c/a(t).

Thus Omega cancels from the radial null-path equation.

This is the strongest result yet for Family A: in the reduced conformal model, large timelike proper-time accumulation can coexist with unchanged unparameterized radial null paths.

However, this does **not** establish unchanged affine parameterization, photon energy, measured frequency, full four-dimensional propagation, or observational redshift.

### Frequency transport burden

For a conformal transformation g_tilde = Omega^2 g, null geodesic curves are preserved but their affine parameterization changes. Measured frequency remains

    omega = -k_mu u^mu.

For comoving emitter/observer worldlines, endpoint values of Omega and the evolution of the background enter the observed frequency relation.

Because the pulse is constructed with Omega=1 at commissioning, signals emitted and observed entirely after commissioning incur no residual endpoint conformal factor from the deployment pulse. Signals whose emission/propagation occurs during deployment require explicit wave-vector transport through the time-dependent Omega.

Therefore the model gains a possible route to avoiding a permanent gigantic redshift, but only if the full transport calculation confirms it. No cancellation is assumed.

### Curvature/source scaling

The economy in proper-time gain does not imply a free geometry.

For a conformal transformation in four dimensions, curvature receives terms schematically of the form

    R_tilde
      = Omega^-2 [R - 6 Box ln(Omega) - 6 (grad ln(Omega))^2].

Here

    ln(Omega) = beta(r) q(t).

Hence the effective curvature/source contains terms scaling approximately as

    beta q_ddot,
    beta^2 q_dot^2,
    spatial derivatives of beta,
    and cross terms.

For the pulse,

    |q_dot|_max = pi Q/T,

so increasing beta Q to obtain large process depth necessarily increases derivative-driven curvature unless spatial/temporal structure produces a derived compensation.

This identifies the next major cost center: the required effective stress-energy or creation-boundary source.

### Key tradeoff

The conformal subfamily has now passed one conceptual screen and exposed another:

**Gain:**
large timelike process depth with unchanged reduced radial null paths.

**Cost:**
time-dependent conformal curvature/source terms plus unresolved frequency transport.

This is a better research position than the lapse-only model because the propagation economy follows from one geometric structure rather than an independent correction.

### Commissioning regularity

The sin^2 pulse guarantees continuity of Omega and its first temporal derivative at t=T. That is favorable for first-order matching.

Because q_ddot does not vanish at the endpoints, curvature can change abruptly there even though the metric and extrinsic-curvature-relevant first derivatives are continuous.

Accordingly, the next refinement should replace sin^2 with a compact smooth bump whose derivatives vanish to the order required by the field equations. This should be done only if the source/frequency tests justify continuing Family A; smoothness must not become a way of hiding a failed physical source.

## Severe-test disposition after conformal screen

Family A is **not demoted**.

The near-conformal subfamily has earned continued investigation because it derives a nontrivial separation between timelike proper-time accumulation and radial null-path geometry using one deployment field.

It has not earned promotion to a physical DFM mechanism because:

1. the effective T_mu_nu has not been shown physically interpretable;
2. photon frequency transport has not been solved;
3. the full 3+1 geometry has not been specified;
4. no quantitative SN 1987A fit has been attempted;
5. no novel observational discriminator has yet been derived.

## Next decision experiment

Before increasing geometric complexity, compute the effective Einstein tensor for the simplest conformal 3+1 completion and classify its required source by:

    energy density,
    radial/tangential pressure,
    energy-condition behavior,
    singularity/regularity,
    spatial localization,
    boundary behavior.

In parallel, derive photon frequency transport through the same Omega(r,t).

If both require independent compensating structure, Family A should be demoted. If one common source geometry controls proper-time depth, propagation, frequency behavior, and smooth commissioning, Family A becomes a serious developed candidate.
