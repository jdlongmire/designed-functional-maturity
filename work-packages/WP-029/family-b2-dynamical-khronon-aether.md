# WP-029D: Family B2 - Dynamical Khronon / Æther Foliation Screen

**Parent:** WP-029C Family B
**Status:** Active candidate screen
**Predecessor:** CMC/York realization (demoted)

## Objective

Test whether a dynamically determined timelike field can supply the preferred creation-deployment foliation without hiding the required proper-time hierarchy in a freely prescribed lapse or slice label.

This work package uses khronometric / hypersurface-orthogonal Einstein-æther structures as mathematical analogues. DFM does not adopt Hořava gravity, Einstein-æther theory, or Lorentz violation as part of its hard core.

## Why this candidate follows CMC

CMC demonstrated that a preferred slicing can constrain lapse, but its global temporal history K(s) remains slicing data unless another principle determines it.

The next candidate must therefore contain physical/dynamical temporal structure.

Introduce a scalar field T(x) whose level surfaces define the preferred foliation and a normalized timelike field

    u_mu = - partial_mu T /
           sqrt[-g^ab partial_a T partial_b T].

The normalization removes arbitrary monotonic relabeling of T from the physical timelike direction. The foliation can therefore be represented covariantly even though it selects a preferred temporal structure.

## Minimal action template

Use the hypersurface-orthogonal Einstein-æther/khronometric form schematically:

    S = S_EH[g]
        + S_u[g,u; c_i]
        + S_m[g,psi].

The æther sector is constructed from covariant derivatives of u and a finite set of dimensionless couplings c_i, subject to

    u^a u_a = -1.

Equivalent low-energy preferred-foliation parameterizations may be written in ADM variables using combinations of

    K_ij K^ij,
    K^2,
    R^(3),
    a_i a^i,

with fixed coupling constants.

The key methodological gain is that the foliation field is varied in the action. Its structure is therefore constrained by equations of motion rather than assigned observation by observation.

## Reparameterization test

The theory depends on the foliation rather than the numerical labels attached to its leaves. Under

    T -> Tbar(T),

the normalized u_mu is unchanged for monotonic relabeling.

This directly addresses the CMC/York failure mode:

> A large coordinate rate dT/ds is not itself a physical clock acceleration.

Any Day-4 hierarchy must instead appear in invariant relations among g_ab, u^a, matter worldlines, and accumulated proper times.

## DFM deployment interpretation

Candidate architecture:

    designed Day-4 boundary data
      + dynamical foliation field T
      + metric/æther field equations
      -> deployment geometry
      -> local proper-time histories
      -> Sigma_sync
      -> ordinary runtime.

Earth remains the reference chronology:

    Delta tau_E ~= 1 day.

The model succeeds only if the same solution yields

    Delta tau_C / Delta tau_E >> 1

for the relevant cosmic causal domains without inserting that ratio into T labels, source-specific couplings, or messenger-specific propagation rules.

## Local covariance and preferred structure

A preferred timelike field need not mean arbitrary local laws. The mathematical analogue is generally covariant while the solution contains a preferred timelike direction.

For DFM the desired distinction is:

    covariant equations
    + physically selected deployment foliation
    !=
    arbitrary coordinate preferred frame.

Whether Lorentz symmetry is modified during deployment, spontaneously broken, or fully recovered in ordinary runtime remains an open auxiliary question.

## Common-coupling requirement

First pass:

    photons,
    neutrinos,
    ordinary matter,
    gravitational disturbances

couple to one metric g_ab.

No species-dependent clock functions are permitted.

The preferred field influences observables only through the common solved geometry unless a separately motivated coupling is registered and severely tested.

## Synchronization / retirement problem

A permanent present-day æther with large effects would be observationally costly and contrary to the synchronized-lapse target.

Therefore DFM requires one of two outcomes:

A. **Deployment-only phase:** the foliation field has a nontrivial Day-4 phase and dynamically relaxes into a state whose stress-energy/effects are negligible after Sigma_sync.

B. **Persistent but inert phase:** the field remains defined after commissioning but approaches a configuration whose observable preferred-frame effects satisfy ordinary-runtime constraints.

A discontinuous deletion of u^a at Sigma_sync is not permitted.

## Immediate opportunity: phase-controlled coupling

A potentially economical DFM-specific extension is to let the *dynamical importance* of the foliation field depend on one scalar deployment phase Phi rather than switch the foliation itself on and off by hand.

Schematically:

    S = S_EH
        + F(Phi) S_u
        + S_Phi
        + S_m,

with

    F(Phi) substantial during deployment,
    F(Phi) -> small/ordinary-runtime value at commissioning.

This is not yet an adopted model. It is attractive only if Phi has its own boundary/dynamical rationale and the transition is solved rather than prescribed.

Otherwise F(Phi) merely becomes the old lapse switch under a new name.

## Severe tests

### KB-1 Dynamical hierarchy

Can field equations plus independently specified boundary data generate a large invariant proper-time hierarchy?

### KB-2 No hidden clock input

Does the hierarchy survive T reparameterization and remain absent from arbitrary initial field normalization?

### KB-3 Common messenger geometry

Do photons, neutrinos, matter, and gravity remain mutually coherent on one solution?

### KB-4 Source cost

What stress-energy and curvature are required from the foliation sector?

### KB-5 Stability

Are perturbations stable and free of pathological modes in the candidate deployment regime?

### KB-6 Retirement

Can the preferred structure become ordinary-runtime-inert smoothly?

### KB-7 Present-day constraints

If any foliation/æther effect remains, is it compatible with the required absence of a large present-day lapse/preferred-frame anomaly?

### KB-8 Novel discriminator

Does the architecture predict any deployment-related relationship not inserted into its construction?

## Comparison with Synchronized-Lapse Cosmology

Synchronized-Lapse Cosmology specifies the phenomenological requirement

    integral alpha_C dt / integral alpha_E dt
      ~ 5.04 x 10^12

for a conventional 13.8-Gyr cosmic thread.

The khronon/æther screen must not encode this ratio in the field label or a freely chosen lapse.

The research question is:

> Does a finite-coupling dynamical preferred-foliation theory possess a regular deployment solution whose invariant proper-time integrals naturally approach the synchronized-lapse target while preserving the common thermal/optical history?

## Stop rule

Demote this realization if obtaining the hierarchy requires:

- coupling constants selected solely to reproduce 5.04 x 10^12;
- a source-specific initial T profile encoding the desired clock ratio;
- species-dependent propagation repair;
- a hand-prescribed shutdown at Sigma_sync;
- unstable/pathological field behavior;
- present-day preferred-frame effects incompatible with the synchronization requirement.

## First computation

Do not solve the full cosmology first.

Construct the homogeneous/isotropic khronon/æther background and determine:

1. whether the normalized timelike field adds a genuinely physical clock relation or simply aligns with FLRW cosmic time;
2. how its stress-energy modifies the Friedmann equations;
3. whether any proper-time hierarchy between Earth and cosmic domains is possible without spatial inhomogeneity;
4. which coupling combination controls that result;
5. whether a deployment-to-runtime relaxation can occur dynamically.

If the homogeneous solution merely supplies one common cosmic clock, then spatial structure or a phase boundary is essential and must be justified before further elaboration.
