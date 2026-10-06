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


## Minimal two-phase spherical screen: hierarchy mechanism before target fitting

The homogeneous screen requires genuine spatial/domain structure. Test the smallest such extension without solving the full cosmic history.

Take one scalar phase field Phi with action

    S_Phi = integral sqrt(-g)
            [-1/2 (grad Phi)^2 - V(Phi)],

and let the dynamical æther/khronon sector carry a phase-dependent coefficient

    F(Phi) L_u.

Choose a generic two-minimum potential only as a structural control,

    V(Phi) = (lambda_Phi/4)(Phi^2-v^2)^2,

so the two phases lie near Phi = +/-v and a regular interpolating wall is possible.

No parameter is selected from R_target.

### What a scalar wall can and cannot do

A scalar wall can dynamically define:

    Earth/reference phase,
    cosmic phase,
    finite transition region.

Its characteristic flat-space thickness scales schematically as

    ell_wall ~ 1/(v sqrt(lambda_Phi)).

This gives a derived transition scale from field parameters rather than an arbitrary radial interpolation function.

However, if the two minima are exactly degenerate and F(Phi) merely takes two order-unity values, no enormous clock hierarchy follows automatically. Domain existence is not clock amplification.

### Moderate-parameter exponential opportunity

A hierarchy could arise without a 10^12 input if an invariant metric/æther response depends exponentially on an order-tens field excursion or integrated coupling, schematically

    R_tau ~ exp[I(Phi,u,g)].

This would be analogous to other physical hierarchy mechanisms where a moderate dimensionless action/field distance generates a large ratio.

For R_target ~= 5.04 x 10^12,

    ln R_target ~= 29.25.

Thus an exponential mechanism would need an invariant exponent of order 30, not 10^12.

This is a legitimate opportunity, but only if the exponential relation is derived from the field equations or matching conditions. Writing

    N = exp[k Phi]

by hand and choosing k Delta Phi ~= 29

does not count as a derivation.

### Static-wall limitation

A static spherical domain wall in an otherwise stationary geometry primarily supplies localized stress-energy and gravitational potential.

Standard gravitational redshift generated by a regular static potential is tied to the same metric lapse that affects photon frequencies. Attempting to obtain a 10^12 proper-time contrast by a static gravitational potential therefore risks:

    extreme compactness,
    horizon formation,
    enormous redshift,
    unacceptable transition stress.

This is structurally similar to the Family A lapse burden.

Therefore the promising B2 mechanism, if any, is unlikely to be a permanent static wall.

### Dynamical phase-transition route

The more distinctive opportunity is a finite deployment phase transition:

    initial boundary
      -> Phi/u deployment phase
      -> large differential process accumulation
      -> relaxation
      -> ordinary-runtime phase.

Scalar-æther couplings are known mathematical structures: coupling a scalar to æther expansion can modify scalar dynamics while retaining a dynamical end to an inflationary phase. This does not validate DFM, but it demonstrates that scalar/æther interactions can generate nontrivial finite cosmological phases rather than requiring a hand-switched coefficient.

For DFM the required version is harder: the phase must be spatially differentiated enough to preserve the terrestrial reference day while the cosmic domain executes substantial history.

### First two-phase no-free-lunch result

With a canonical scalar, a regular two-minimum potential, order-unity phase-dependent æther couplings, and one common metric:

**No large Earth/cosmos proper-time hierarchy follows merely from having two phases.**

To produce the hierarchy, the model still requires a derived mechanism in one of these classes:

B2-M1. **Dynamical critical/attractor hierarchy:** evolution near a critical solution produces exponentially separated accumulated proper times.

B2-M2. **Integrated æther-expansion hierarchy:** a moderate coupling integrated over a dynamical phase yields an exponential invariant effect.

B2-M3. **Geometric throat/horizon-adjacent hierarchy:** geometry generates large lapse separation. High risk because of redshift/horizon/pathology burdens.

B2-M4. **Phase-dependent effective gravitational coupling:** one phase changes metric response strongly. Must satisfy stability and synchronization constraints.

B2-M5. **Topological/boundary protected hierarchy:** global boundary structure fixes a large ratio without continuous fine-tuning. No concrete realization yet.

### Stability burden

Preferred-frame/vector theories cannot be assumed stable merely because the action is covariant. Candidate kinetic sectors can exhibit ghosts, tachyons, runaway anisotropy, or singular evolution for portions of parameter space.

Accordingly, any B2-M candidate must pass:

    positive-energy/ghost screen,
    gradient/tachyon screen,
    regular wall/transition evolution,
    no runaway æther tilt,
    ordinary-runtime preferred-frame bounds.

These are mechanism-level tests, not objections to the broader asynchronous deployment auxiliary.

## B2 two-phase disposition

**Retain B2, but reject “two phases alone” as an explanation.**

The phase field earns one thing: a dynamical way to define the Earth/cosmic/transition architecture and potentially a dynamical retirement mechanism.

It has not yet earned the proper-time hierarchy.

The most promising next target is B2-M1/B2-M2: determine whether a scalar-æther dynamical system possesses a critical, attractor, or integrated-expansion regime in which an invariant proper-time ratio grows exponentially from moderate dimensionless parameters.

The benchmark is now

    ln R_target ~= 29.25.

This is a much more discriminating target than fitting R_target directly.

## Next computation

Build the minimal reduced dynamical system for a scalar Phi coupled to æther expansion theta = nabla_a u^a, using a bilinear or lowest-order symmetry-allowed coupling.

Determine whether the equations contain:

1. a finite deployment phase;
2. an attractor or near-critical trajectory;
3. an invariant accumulated quantity with exponential sensitivity;
4. a natural exit/relaxation;
5. parameter values of order unity to tens rather than 10^12;
6. a route to spatial differentiation without species-specific propagation.

If the reduced dynamics only changes a common expansion rate and never generates a relative Earth/cosmic proper-time hierarchy, demote B2-M1/M2 before adding spatial complexity.


## Reduced scalar-aether dynamical-system screen: B2-M1/M2

Use the lowest-order expansion-coupled scalar structure studied in Einstein-aether cosmology,

    V(phi,theta) = U(phi) + Y(phi) theta,

where

    theta = nabla_a u^a.

In a homogeneous/isotropic background theta is proportional to the Hubble expansion rate. The reduced equations can be written schematically as

    (1/3) theta^2
      = (1/2) phi_dot^2 + U(phi),

    (2/3) theta_dot + (1/3) theta^2
      = -(1/2) phi_dot^2 + U(phi)
        - phi_dot Y_,phi,

    phi_ddot + theta phi_dot
      + U_,phi + Y_,phi theta = 0.

The coupling therefore enters the scalar force/pressure sector and can change critical points, attractors, slow-roll behavior, and exit dynamics.

### B2-M1 test: critical/attractor dynamics

The literature establishes that Einstein-aether scalar systems can possess multiple critical points, including power-law and de Sitter-like solutions, and can admit stable/unstable attractor structure.

That is enough to establish the mathematical availability of critical dynamics.

It is not enough to establish the DFM hierarchy.

In the homogeneous reduced system there remains one comoving proper-time congruence. Critical behavior can make

    a(tau)

grow exponentially or make a scalar trajectory linger near an attractor, but it does not create a second invariant clock accumulation against which the Earth contour remains at one day.

Thus an attractor-generated large number such as

    exp(N_e-fold)

is not yet

    Delta tau_C / Delta tau_E.

**Disposition B2-M1 homogeneous:** demote as a direct clock-hierarchy mechanism; retain as a possible engine inside a spatially differentiated phase model.

### B2-M2 test: integrated aether-expansion hierarchy

The natural invariant accumulator supplied by the reduced homogeneous dynamics is

    integral theta d tau.

For FLRW,

    theta = 3H,

so

    integral theta d tau
      = 3 ln(a_f/a_i).

Exponentiating this integral yields

    exp[(1/3) integral theta d tau]
      = a_f/a_i.

Therefore the apparent exponential opportunity is real mathematically, but in the homogeneous system it is the ordinary expansion factor.

It does not independently generate a ratio of local proper times.

This sharply distinguishes:

    exponential scale-factor hierarchy

from

    exponential proper-time hierarchy.

Conflating them would reproduce the Family A mistake in a different variable.

**Disposition B2-M2 homogeneous:** reject as a standalone explanation of synchronized lapse.

### What survives from the e^29 observation

The numerical observation

    ln R_target ~= 29.25

remains useful only if a future spatial/domain solution derives an invariant relation of the form

    ln(Delta tau_C/Delta tau_E)
      = integral_D Q[g,u,Phi] d(lambda)

for a physically defined scalar Q along the solved deployment geometry.

The integral must not merely equal ln a or a coordinate duration.

This becomes a formal requirement for any claimed exponential hierarchy.

## Natural exit result

Expansion-coupled scalar-aether systems can alter slow-roll dynamics while retaining a dynamical end to the modified phase.

This is relevant to the DFM synchronization problem because it demonstrates a class of dynamical systems in which a preferred-frame/scalar interaction need not be permanently active.

But a graceful exit from modified scalar dynamics is not yet a solution of

    alpha_C/alpha_E -> 1

across a spatial Earth/cosmic domain structure.

The latter remains to be derived.

## Reduced-system verdict

The reduced homogeneous scalar-aether system gives a mixed result:

**Pass:**
- dynamical preferred structure exists;
- critical points/attractors are available;
- expansion-coupled scalar dynamics can possess a natural exit;
- moderate parameters can generate exponentially large scale-factor changes.

**Fail for the central DFM target:**
- there is only one homogeneous proper-time congruence;
- the exponential accumulator is expansion, not relative proper time;
- no Earth/cosmos clock hierarchy is generated.

Therefore neither B2-M1 nor B2-M2 should be promoted on homogeneous dynamics.

## Consequence for Family B2

The research programme has now isolated the missing ingredient more precisely:

> A viable Family B2 realization requires a spatially differentiated dynamical solution in which the same scalar-aether field equations produce two physically distinct proper-time histories and a regular transition between them.

The next model must not infer this from homogeneous e-folding.

## Next severe test: two-domain invariant accumulator

Before solving full PDEs, construct a reduced two-domain model with a common scalar-aether action but domain-dependent solved states:

    E: (Phi_E, u_E, g_E)
    C: (Phi_C, u_C, g_C)
    B: dynamical transition.

Define

    R_tau = Delta tau_C / Delta tau_E

directly from metric proper-time integrals.

Then determine whether the field equations imply a relation

    d ln R_tau / d lambda = Q(Phi_E,Phi_C,u,g)

whose integral can become order 29 with moderate couplings.

If no such invariant evolution equation emerges, the exponential-hierarchy opportunity should be closed rather than retained as suggestive numerology.


## Reduced two-domain invariant-accumulator test

Represent the terrestrial and cosmic domains by two timelike congruences in one common solved spacetime:

    E: x_E^mu(lambda)
    C: x_C^mu(lambda).

Their accumulated proper times are

    tau_E = integral sqrt[-g_mu_nu dx_E^mu dx_E^nu]/c
    tau_C = integral sqrt[-g_mu_nu dx_C^mu dx_C^nu]/c.

Define the invariant ratio

    R_tau = tau_C/tau_E.

This definition contains no khronon label, coordinate lapse, or scale-factor proxy.

### Differential identity

For any common evolution label lambda,

    d ln R_tau/d lambda
      = (1/tau_C) d tau_C/d lambda
        - (1/tau_E) d tau_E/d lambda.

This identity is exact but not yet explanatory. To generate an exponential hierarchy, the field equations must make the right-hand side a derived invariant functional of the domain states rather than an assigned clock-rate difference.

Call that derived quantity

    Q_EC[g,u,Phi] .

Then a genuine hierarchy mechanism would require

    ln R_tau(lambda_f)
      - ln R_tau(lambda_i)
      = integral Q_EC d lambda.

The synchronized-lapse target corresponds to an accumulated invariant of order 29.25.

### Two homogeneous patches do not derive Q_EC

Suppose E and C are approximated as separate homogeneous patches, each with its own locally FLRW metric, joined by a transition region.

Within each patch the khronon aligns with the local cosmological congruence. The scalar-aether equations determine each patch's expansion and matter evolution.

But unless the junction/boundary equations determine the relative normalization of the two timelike geometries, the reduced patch equations do not determine Q_EC.

One may write

    d tau_E = N_E d lambda,
    d tau_C = N_C d lambda,

but the ratio N_C/N_E is then precisely the quantity that must be derived from the common global solution.

Thus merely solving two different homogeneous attractors does not generate the synchronized lapse.

### Junction is the mechanism candidate

The only place a relative clock normalization can become physical in the reduced two-domain picture is the common transition geometry.

A valid mechanism must therefore derive the relation among

    induced metric,
    extrinsic curvature,
    scalar profile and normal derivative,
    aether orientation/derivatives,
    domain proper times

across B.

This converts the search from "find a fast cosmic attractor" to:

> Can one regular junction solution force a large invariant relative normalization between two domain proper-time histories?

### Thin-wall control

In a thin-wall idealization, standard junction conditions tie discontinuities in extrinsic curvature to surface stress-energy.

A huge static relative lapse generally corresponds to strong gravitational potential/compactness and therefore reintroduces the redshift/horizon burden already identified.

So a static thin wall is retained only as a control.

### Dynamical-wall opportunity

A dynamical transition can, in principle, accumulate different proper times on its two sides even if the final geometry later becomes common.

This is closer to the synchronized-lapse requirement:

    temporary domain differentiation
      -> differential accumulated tau
      -> smooth relaxation
      -> shared ordinary runtime.

But the accumulated ratio must be solved from wall/domain dynamics. A prescribed wall trajectory or prescribed relative lapse would fail the stop rule.

## Exponential-hierarchy verdict

The reduced two-domain analysis does **not** produce a field-derived Q_EC from homogeneous scalar-aether dynamics alone.

Therefore the generic "e^29" opportunity is closed as a standalone mechanism.

Retain only the more specific hypothesis:

**B2-M6: junction-generated differential aging.**

Proposition: a regular dynamical scalar-aether transition solution may force large differential accumulated proper time between E and C before relaxing to a common runtime geometry.

Status: candidate, high burden.

### Promotion criterion

B2-M6 advances only if a solved or analytically constrained junction produces R_tau from moderate boundary/coupling data without:

- inserting the ratio into initial lapse normalization;
- near-horizon tuning solely to obtain redshift/time dilation;
- messenger-specific matching;
- singular wall stress;
- hand-prescribed wall trajectory;
- discontinuous synchronization.

## Next computation

Before full PDE integration, derive the spherical junction bookkeeping for a moving boundary R(lambda):

    interior metric g_E,
    exterior/cosmic metric g_C,
    wall proper time tau_B.

Use continuity of the induced metric to relate

    dtau_B,
    dtau_E,
    dtau_C

along the wall, then use the extrinsic-curvature jump condition to identify what surface stress-energy is required for a large transient differential.

This will determine whether junction-generated differential aging is a genuine new route or merely the static gravitational-lapse problem in dynamical form.
