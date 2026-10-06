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


## Homogeneous/isotropic severe test

Take a spatially homogeneous and isotropic background

    ds^2 = -N(t)^2 c^2 dt^2 + a(t)^2 gamma_ij dx^i dx^j.

FLRW symmetry forbids a homogeneous preferred vector with a nonzero spatial component: such a component would select a spatial direction and break isotropy.

Therefore the homogeneous æther/khronon must align with the cosmological normal congruence,

    u^mu = n^mu = (1/N, 0, 0, 0)

in adapted coordinates.

For a homogeneous khronon T=T(t), normalization removes the magnitude of T_dot:

    u_mu = -partial_mu T /
           sqrt[-g^ab partial_a T partial_b T]

so monotonic changes in T(t) leave the physical u^mu aligned with the same normal direction.

### Result B2-H1: no second physical clock from a homogeneous khronon

A comoving cosmic observer has

    d tau = N dt.

The aligned homogeneous khronon does not supply an independent invariant proper-time accumulation. It defines the same timelike congruence already selected by FLRW symmetry.

Consequently a homogeneous/isotropic khronon cannot by itself produce

    Delta tau_C >> Delta tau_E

between two comoving domains of one homogeneous FLRW solution.

Changing T_dot cannot solve this because normalization and T-reparameterization remove that quantity from the physical timelike direction.

### Result B2-H2: background effect is dynamical renormalization, not clock bifurcation

The æther sector can contribute to the cosmological field equations through expansion/derivative terms and thereby modify the relation among matter density, Hubble expansion, and gravitational couplings.

That is a genuine physical effect.

But in a homogeneous isotropic background it modifies the common cosmological evolution; it does not create an Earth-local clock and a separate cosmic clock with a 10^12-10^13 integrated hierarchy.

Thus changing æther couplings to alter the Friedmann equation is not equivalent to deriving the synchronized-lapse target.

### Result B2-H3: the synchronized-lapse architecture requires broken homogeneity during deployment

To obtain distinct invariant accumulations, Family B2 must contain genuine domain structure, for example:

    Earth/reference domain E,
    cosmic fast domain C,
    transition region B,

with the solved fields satisfying different invariant geometry in E and C.

The preferred field may help define and dynamically support that structure, but it cannot remain exactly homogeneous.

This is a useful constraint rather than a defect: the synchronized-lapse proposal itself already distinguishes a terrestrial contour from an extraterrestrial fast region.

### Domain-wall / phase-boundary opportunity

The minimal next architecture is therefore not arbitrary radial lapse assignment but a dynamical phase profile.

Introduce a scalar deployment phase Phi(r,t) with two regimes:

    Phi_E : terrestrial/reference phase
    Phi_C : cosmic/deployment phase.

The khronon/æther sector couples through one function F(Phi), while Phi obeys its own field equation derived from a potential and kinetic term.

Schematic action:

    S = S_EH
        + S_Phi[g,Phi]
        + F(Phi) S_u[g,u]
        + S_m[g,psi].

A regular interpolating solution could then define E, C, and the transition region dynamically.

The important distinction from a hand-drawn lapse is:

    Phi profile + u field + metric

must be a joint solution of one boundary-value problem.

### New danger: moving the hierarchy into the phase potential

A two-phase model is explanatory only if the large proper-time contrast follows from a structurally motivated difference between phases.

If the potential V(Phi), coupling F(Phi), or vacuum values are chosen so that their ratio is 5.04 x 10^12 solely to reproduce the target, the model fails KB-2.

The hierarchy must emerge from equations, critical behavior, exponential dependence with moderate parameters, topological/boundary structure, or another independently motivated mechanism.

### Common-history requirement

The cosmic phase must contain the genuine thermal/stellar history.

The transition region must transmit photons, neutrinos, and gravitational effects through one solved geometry.

No messenger-specific matching rule is allowed at the phase boundary.

### Homogeneous-screen verdict

**The homogeneous/isotropic khronon realization fails as a synchronized-lapse mechanism but passes as a useful control.**

It confirms that a dynamical preferred foliation is not enough. The required clock hierarchy demands physical spatial/domain structure.

This result strengthens rather than weakens the methodological distinction from CMC: the khronon remains a dynamical field, but symmetry shows exactly what it cannot accomplish.

## Family B2 next test

Test a minimal two-phase spherical configuration before introducing full cosmology.

Requirements:

1. one scalar Phi with a simple two-regime potential;
2. one hypersurface-orthogonal u^a;
3. one common metric;
4. regular Earth/cosmic/transition domains;
5. no target-ratio parameter inserted initially;
6. derive whether invariant lapse/proper-time contrast can become parametrically large;
7. determine transition stress-energy and stability;
8. only then overlay R_target ~= 5.04 x 10^12.

A particularly valuable outcome would be a hierarchy generated exponentially from order-unity or moderately separated field parameters. A merely linear transfer of a 10^12 input into a 10^12 clock ratio would not improve on the stipulated-lapse model.
