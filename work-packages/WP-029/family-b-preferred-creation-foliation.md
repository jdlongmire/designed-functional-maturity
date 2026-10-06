# WP-029C: Family B - Preferred Creation Foliation with Covariant Local Physics

**Parent:** WP-029
**Status:** Active candidate architecture
**Predecessor/control:** WP-029B Family A

## Objective

Test whether an explicit preferred foliation during the extraordinary creation-deployment regime provides a cleaner architecture than encoding the same privileged structure indirectly in a single highly specialized metric.

Family B does not begin by asserting a preferred frame in ordinary runtime. It asks whether the finite creation/deployment interval may possess additional boundary structure that coordinates the Genesis terrestrial chronology while local physical processes remain governed by covariant laws.

## Core structure

Let spacetime during deployment admit a foliation by spacelike hypersurfaces

    Sigma_s

indexed by a deployment parameter s.

The terrestrial creation chronology is represented by a monotonic reference relation

    tau_E = T_E(s),

with the Day 4 interval satisfying

    Delta tau_E ~= 24 h.

For each local physical worldline gamma_i, proper time remains metric-defined:

    d tau_i^2 = -(1/c^2) g_mu_nu dx^mu dx^nu.

The foliation parameter s is therefore not automatically identical to local proper time.

## Deployment-rate field

Introduce one auxiliary field or law

    alpha_i(s) = d tau_i / ds

or, more generally,

    alpha(x,s) = d tau_local / ds

for observers/processes associated with the foliation.

Then

    Delta tau_i = integral alpha_i(s) ds.

The strong asynchronous auxiliary becomes

    integral alpha_C(s) ds >> integral alpha_E(s) ds.

This makes the privileged structure explicit rather than hiding it in a coordinate lapse.

## Critical distinction

Family B must not merely rename the Family A lapse N as alpha.

To earn explanatory value, the foliation must have an independent physical role, such as:

- specifying the creation/deployment boundary-value problem;
- defining the ordering of commissioned states;
- constraining which local solutions are admissible on each Sigma_s;
- governing coupling/synchronization among domains;
- producing derived relationships among alpha, local metric evolution, and observables.

If alpha(x,s) is freely assignable point by point, Family B fails immediately as an unconstrained clock field.

## Local covariance requirement

Within local domains, ordinary field equations should retain covariant form unless a separately registered auxiliary modifies them.

The preferred foliation is a global/boundary structure, not permission to assign different local laws observation by observation.

This permits the conceptual combination:

    preferred deployment ordering
    + covariant local physics.

The existence of a preferred creation foliation need not imply a detectable preferred frame after commissioning.

## ADM-style representation

Use the standard 3+1 decomposition as the mathematical language:

    ds^2 = -N^2 c^2 ds^2
           + h_ij (dx^i + beta^i ds)(dx^j + beta^j ds).

Here:

- s labels the preferred deployment slices;
- N is the lapse relating slice parameter to local proper time;
- beta^i is the shift;
- h_ij is the induced spatial metric.

Family B differs from failed Family A only if N, beta^i, and h_ij are constrained by the preferred deployment architecture rather than chosen solely to generate desired clock ratios.

## Boundary-value interpretation

Treat creation as a constrained boundary/deployment problem:

    B_initial
      -> {Sigma_s, admissible local states}
      -> Sigma_sync
      -> ordinary runtime.

The hypothesis to test is that the creation boundary supplies information not recoverable from ordinary runtime evolution alone.

That is already consonant with DFM's reconstruction argument. Family B asks whether temporal coordination is one component of that boundary information.

## Synchronization

The final slice Sigma_sync is the commissioning boundary.

Required:

1. local physical state on Sigma_sync is well-defined;
2. constraints on h_ij and extrinsic curvature are satisfied;
3. no observation-specific reset occurs;
4. post-commissioning evolution follows ordinary runtime law L_R;
5. the preferred deployment structure either disappears, becomes dynamically irrelevant, or reduces to an empirically acceptable ordinary foliation.

## SN 1987A test

The foliation may permit substantial local process time for the SN 1987A causal domain while only one terrestrial Day 4 elapses, but the complete causal family must remain coupled:

    progenitor
      -> collapse
      -> neutrinos
      -> photons
      -> nucleosynthesis
      -> ejecta/remnant
      -> propagation
      -> later observed interaction.

The model may not independently assign alpha values to each node.

The first admissible version should therefore define alpha by broad physical domain or geometry, not by observational target.

## Family B hypotheses

### B1 Boundary-determined lapse

The creation boundary conditions determine N(x,s), with no independent observation-specific clock factors.

### B2 Foliation-coupled metric evolution

h_ij(s) and K_ij(s) evolve under constrained equations tied to the deployment foliation.

### B3 Local-covariance preservation

Matter and signal propagation obey common local covariant equations on the deployment geometry.

### B4 Smooth foliation retirement

At Sigma_sync the preferred deployment structure becomes observationally irrelevant without discontinuously resetting physical state.

## Advantages over Family A

Potential advantages:

- privileged creation ordering is explicit rather than hidden;
- boundary information has a defined mathematical home;
- multiple local proper-time accumulations can be coordinated against one deployment sequence;
- synchronization is built into the architecture;
- local covariance can be preserved.

These are potential advantages only. Each is an additional structural commitment that must earn its cost.

## Principal risks

1. alpha/N becomes an arbitrary clock field.
2. the foliation is merely coordinate gauge with no explanatory content.
3. the foliation is physical but predicts unacceptable preferred-frame effects.
4. local covariance is asserted but not maintained at coupling boundaries.
5. the model reproduces Family A's spectral/propagation problems under different notation.
6. retirement at Sigma_sync requires an ad hoc phase change.

## Severe-test criteria

Family B advances only if it can produce a constrained relation among:

    deployment ordering
    local proper-time accumulation
    metric evolution
    messenger propagation
    synchronization.

It must do this with fewer effective degrees of freedom or greater independent explanatory reach than the demoted Family A.

## First mathematical target

Construct the minimal boundary-determined-lapse model:

    N(x,s) = F[C_initial, h_ij, K_ij, matter state; s]

rather than

    N(x,s) = arbitrary function.

The first question is whether a physically meaningful constraint or variational principle can determine N or alpha from deployment boundary data while preserving local covariance.

Candidate mathematical analogues may include constant-mean-curvature slicing, York-time formulations, preferred-foliation gravity frameworks, or other constrained 3+1 constructions. These are analogues/research resources, not adopted DFM mechanisms.

## Stop rule

Demote Family B if its explanatory success requires freely specifying N(x,s), alpha(x,s), or slice geometry after seeing each target observation.

Promote it only if one constrained foliation architecture explains multiple independent domains and yields at least one discriminator not built into its construction.


## Boundary-determined lapse test: CMC/York-style screen

The first Family B screen uses standard 3+1 constraint structure rather than inventing a new clock law.

On each deployment slice Sigma_s, let h_ij be the spatial metric, K_ij its extrinsic curvature, n^mu the unit normal, rho the normal-frame energy density, and S the trace of spatial stress.

The ADM constraints include, schematically,

    R^(3) + K^2 - K_ij K^ij = 16 pi G rho / c^4

and

    D_j(K^ij - h^ij K) = 8 pi G j^i / c^4.

These constrain admissible initial/slice data but do not by themselves determine the lapse N, because lapse is ordinarily part of the slicing/gauge freedom.

### Add a physical deployment slicing condition

Test constant-mean-curvature slicing:

    K(x,s) = K(s).

Demanding preservation of this condition under evolution yields an elliptic lapse equation of the general form

    -D^2 N
    + N [K_ij K^ij + 4 pi G (rho + S)/c^4]
    = source[K_dot(s), shift, conventions].

The exact coefficients/signs depend on convention, but the structural result is what matters:

> Once the slice geometry, matter data, prescribed K(s), shift treatment, and boundary conditions are fixed, the lapse is constrained by an elliptic equation rather than freely assigned point by point.

This is the first Family B result that materially differs from an arbitrary alpha(x,s) clock field.

## What is and is not determined

CMC does not remove all freedom.

The programme still must justify:

- why CMC, or another slicing principle, is physically privileged during creation deployment;
- the function K(s) or an equivalent global temporal condition;
- spatial boundary/asymptotic conditions for N;
- shift beta^i or a rule fixing it;
- initial h_ij, K_ij, and matter/boundary data.

Therefore Family B has not derived the terrestrial/cosmic time ratio from first principles. It has reduced local lapse freedom to a smaller set of global geometric/boundary choices.

That reduction is genuine methodological progress if those choices are independently constrained.

## York-time interpretation

The mean curvature K can serve as a global temporal parameter in suitable formulations. Define a York-like deployment parameter schematically by

    T_Y proportional to -K.

Then the creation foliation can be expressed as ordered constant-K slices rather than an arbitrary coordinate-time stack.

This has an architectural attraction for DFM:

    boundary geometry
      -> ordered deployment slices
      -> locally covariant evolution
      -> commissioning slice.

But DFM must not infer from mathematical usefulness that York time is the actual creation clock. It is a candidate organizing variable only.

## Lapse-ratio consequence

For observers normal to the slices,

    d tau = N ds.

Hence the local process-depth ratio between a cosmic domain C and terrestrial domain E is

    Delta tau_C / Delta tau_E
      = [integral N_C(s) ds] / [integral N_E(s) ds].

Under the CMC screen, N_C and N_E are solutions of the same lapse equation on the same slice geometry. Their ratio is therefore not independently selectable if h_ij, K_ij, matter content, K(s), and boundary conditions are fixed.

This is exactly the kind of constraint Family B needs.

## SN 1987A implication

A successful CMC-like deployment geometry would determine the lapse throughout the source-to-observer geometry at once. SN 1987A photons, neutrinos, stellar processes, ejecta, and ring interaction would therefore inherit one geometric temporal architecture rather than independent clock assignments.

This does not yet show that the required large differential exists. It shows that the hypothesis can be made non-arbitrary enough to test.

## First Family B discriminator

The central quantitative question becomes:

> Can admissible slice data and a physically motivated K(s) produce a large N_C/N_E or integrated proper-time differential while maintaining regular geometry, acceptable matter/source behavior, and ordinary post-commissioning physics?

If the answer is no across reasonable CMC/boundary data, this version of Family B fails.

If yes, the lapse equation supplies a derived clock relation rather than a stipulated one.

## Commissioning condition

Choose Sigma_sync as a final slice satisfying ordinary-runtime constraint data and require the preferred deployment slicing to match onto an ordinary solution.

A particularly economical target is

    K(s) -> K_R
    N(x,s) -> N_R(x)
    beta^i -> beta_R^i
    h_ij -> h_ij^R
    K_ij -> K_ij^R

smoothly as s approaches s_sync.

No state reset is permitted.

## CMC screen verdict

**Family B passes its first structural screen.**

Reason: a preferred slicing condition such as CMC can convert lapse from an arbitrary pointwise function into the solution of a constrained elliptic boundary-value problem.

This does not establish CMC as the correct creation foliation and does not establish a large cosmic/terrestrial proper-time ratio. It establishes that Family B need not collapse immediately into arbitrary clock assignment.

## New burden ledger

B1. **Foliation-selection burden:** independently motivate CMC/York or another slicing principle.

B2. **Global-time burden:** constrain K(s) rather than choosing it to manufacture the desired ratio.

B3. **Boundary-data burden:** specify lapse boundary/asymptotic conditions without source-specific tuning.

B4. **Existence burden:** show regular solutions with the required differential proper time actually exist.

B5. **Propagation burden:** evolve photons/neutrinos/fields on the same geometry.

B6. **Commissioning burden:** recover ordinary runtime smoothly.

B7. **Discriminator burden:** derive a consequence not used to construct the foliation.

## Next severe test

Construct a simplified spherically symmetric CMC boundary-value model with:

    terrestrial normalization N_E = 1,
    one source-domain geometry,
    one global K(s),
    no messenger-specific functions.

Solve or bound the elliptic lapse equation sufficiently to determine whether large N_C/N_E can arise without singular geometry or exotic source terms chosen solely for that purpose.

If CMC cannot generate the required hierarchy under constrained data, test one alternative slicing principle before increasing the ontology further.


## Spherical CMC lapse bound: first quantitative screen

Take a simplified spherical slice with vanishing shift and a conformally simple spatial geometry sufficient for a sign/bound analysis. Write the CMC lapse equation as

    -D^2 N + V(r) N = C(s),

where

    V(r) = K_ij K^ij + 4 pi G (rho + S)/c^4

up to convention-dependent factors, and C(s) is spatially constant on a CMC slice when K_dot is prescribed globally.

Impose terrestrial normalization at the reference boundary

    N(r_E) = 1

and regularity at a symmetry center or appropriate regular inner boundary.

The immediate question is whether a large positive lapse maximum N_C >> 1 can arise in the interior when V(r) is nonnegative and the source C is not specially tuned.

### Maximum-principle screen

At an interior positive maximum of N,

    D^2 N <= 0.

Therefore

    -D^2 N >= 0.

The lapse equation then gives

    C = -D^2 N + V N >= V N.

If V > 0,

    N_max <= C / V

at that maximum.

This is not a global numerical bound unless V has a positive lower bound, but it reveals the sign structure: with V >= 0, the elliptic operator resists arbitrarily large interior lapse maxima unless the global source C is itself large, V becomes small, or the assumptions are changed.

If V(r) >= V_min > 0 throughout the relevant region, then any interior maximum obeys schematically

    N_max <= C / V_min.

Thus a large N_C/N_E hierarchy is not generated for free by ordinary positive-potential CMC data.

### Homogeneous control

If V is approximately constant and N is spatially constant, then

    V N = C,

so

    N = C/V.

With terrestrial normalization N_E=1 on the same homogeneous slice, there is no cosmic/terrestrial lapse hierarchy at all.

Spatial differentiation is therefore essential.

### What can generate a hierarchy?

Within this simplified CMC equation, large N_C relative to N_E requires at least one of:

1. strong spatial variation in V(r);
2. regions where V becomes very small;
3. a large global C(s);
4. boundary conditions that drive a large interior solution;
5. sign-changing/effectively negative contributions to the lapse potential under a more complete matter/geometry model;
6. nontrivial spatial curvature/conformal geometry omitted by the simplified screen.

Each possibility is testable and carries a physical interpretation.

### Source-sign implication

Because

    V ~ K_ij K^ij + 4 pi G (rho + S)/c^4,

the geometric K_ij K^ij term is nonnegative. For ordinary matter satisfying sufficiently standard stress/energy behavior, rho+S is often nonnegative as well.

Accordingly, the simplest ordinary-sign source content tends to make V nonnegative.

A very large lapse hierarchy may therefore require unusual stress/pressure structure, a near-zero-potential domain, strongly inhomogeneous geometry, or a different slicing law.

This is an important result because Family B cannot simply invoke CMC and assume that the required differential follows.

## Toy two-domain bound

Represent Earth and cosmic domains by effective potentials V_E and V_C under one common C(s). In a slowly varying/quasi-homogeneous approximation,

    N_E ~ C/V_E
    N_C ~ C/V_C.

Hence

    N_C/N_E ~ V_E/V_C.

With N_E normalized to 1, a target ratio R requires approximately

    V_C ~ V_E/R.

For R >> 1, the cosmic deployment region must therefore sit in an effective lapse-potential environment parametrically smaller than the terrestrial reference region.

This converts the desired clock hierarchy into a geometric/source hierarchy that can be investigated rather than stipulated.

### Interpretation

The toy result does not establish that such a hierarchy exists. It identifies what a CMC realization would have to explain:

> Why does the creation-deployment geometry generate a large, globally coherent contrast in the effective lapse potential between the Earth-local reference domain and cosmic process domains?

That question is preferable to simply asking for a clock multiplier because V is built from geometric and matter quantities.

## SN 1987A consequence

The SN 1987A source domain, intervening propagation geometry, and Earth reference domain cannot be assigned independent lapse factors. They must occupy one solution N(r) generated by one V(r), one C(s), and common boundary conditions.

Any large source-domain proper-time gain therefore predicts a spatial lapse profile between source and observer. That profile will affect propagation/frequency calculations and becomes an observational discriminator.

## Quantitative-screen verdict

**CMC Family B remains viable but does not naturally generate a large lapse hierarchy under homogeneous ordinary-sign data.**

The first bound converts the problem from arbitrary temporal scaling to a required hierarchy in constrained geometric/source quantities.

This is progress, but it raises the evidential burden.

### No-go direction

If more realistic CMC slice models with physically admissible V(r) and untuned boundary data obey maximum-principle bounds that keep N_C/N_E near unity, the CMC realization should be demoted.

Do not evade such a result by choosing source-specific lapse boundary conditions.

## Next computation

Test whether a physically interpretable radial V(r) can generate a large but smooth lapse hierarchy.

Use a minimal two-scale profile

    V(r) = V_C + (V_E - V_C) W(r),

where W(r) is one smooth transition function fixed by broad domain geometry, not by individual observations.

Solve

    -[1/r^2] d/dr [r^2 dN/dr] + V(r) N = C

with regularity and N_E=1.

Then evaluate:

    achievable N_C/N_E,
    gradient scale,
    curvature/source interpretation,
    photon frequency implications,
    sensitivity to V_C/V_E.

If the required ratio tracks an equally extreme unexplained V_E/V_C hierarchy, Family B has relocated rather than explained the temporal problem.


## Convergent proposal: Synchronized-Lapse Cosmology

The October 2026 working preprint *A Synchronized-Lapse Cosmology: Real Thermal History inside a Temporary Metric Lapse* provides an independently stated target architecture closely aligned with the DFM asynchronous-deployment programme.

Its core construction is:

    terrestrial proper-time day
    + temporary cosmic/terrestrial lapse differential
    + genuine execution of the standard cosmic thermal history
    + populated inbound light cone
    + synchronization
    + ordinary post-barrier runtime.

The proposal is explicitly a model definition rather than a solved Einstein initial-value problem. DFM therefore treats it as a convergent phenomenological proposal, not as a completed physical realization.

### Stipulated lapse versus boundary-derived lapse

The preprint postulates, over Day 4,

    integral alpha_E dt = 1 day

and

    integral alpha_C dt = tau_thermal,

with tau_thermal of order the conventional 13.8 Gyr when the cosmic thread executes the standard history.

Its open obligation is to construct an alpha(x,t) satisfying that hierarchy while preserving acceptable geometry, energy/source behavior, terrestrial integrity, and post-synchronization observations.

Family B strengthens the research question:

    designed boundary data
      + constrained foliation principle
      + 3+1 constraint/evolution equations
      -> derived N(x,s)
      -> derived Delta tau_C / Delta tau_E.

Accordingly:

**Synchronized-Lapse Cosmology:** stipulates the required lapse behavior and asks whether a physical realization exists.

**DFM Family B:** asks whether the lapse behavior follows from independently constrained creation-boundary and foliation data.

This distinction is methodologically important and should be preserved.

## Real-History Allocation Principle

The preprint supplies a strong allocation heuristic for DFM.

> **Where multiple independently observed consequences are naturally generated by one tightly coupled causal history, DFM should prefer genuine execution of that history during creation deployment over independent initialization of each consequence, unless Scripture, physical coherence, or severe testing supplies reason for a different allocation.**

This is not a prohibition on initialization. It is an anti-fragmentation rule within Initialization-Deployment Complementarity.

For the cosmic thread, candidate genuinely executed processes include:

    nucleosynthesis
    recombination
    structure growth
    stellar evolution
    supernovae/remnants
    intervening absorption
    photon/neutrino propagation.

The initial data remain designed; products of the run need not each be separately instantiated.

## Single-History / No-Frequency-Layer Constraint

Adopt as a severe-test rule:

> **A successful Day-4 deployment architecture must derive clock accumulation, signal propagation, frequency shift, time dilation, path delays, and thermal-history observables from one coherent geometry/history. It may not repair these observables with an independent post-hoc frequency translation layer.**

This directly strengthens the WP-029 anti-overfitting rule.

## Expanded cross-observable invariant matrix

A candidate deployment geometry must jointly preserve or explain:

| Domain | Coupled observable/relationship | Required common source |
| --- | --- | --- |
| Redshift | redshift-distance relation | one a(tau)/deployment geometry |
| SN Ia | light-curve stretch ~ 1+z | emitter clock + same expansion history |
| Intervening gas | Lyman-alpha forest | real intermediate causal history |
| Lensing | path/time delays | same metric/geodesic structure |
| CMB monopole | blackbody temperature | recombination + expansion |
| CMB acoustic scale | sound horizon/angular distance | same thermal/metric history |
| Light elements | abundance yields | genuine nucleosynthesis history |
| Structure | clustering/lensing/dynamics | component active during growth |
| Late acceleration | magnitude-redshift relation | same stress-energy history |
| SN 1987A neutrinos | collapse-time messenger relation | same source event/geometry |
| SN 1987A radioactive lines | nucleosynthesis + decay sequence | same explosion history |
| SN 1987A ejecta/rings | expansion/shock interaction | same causal event network |
| SN 1987A dust/remnant | post-explosion evolution | same executed history |

Failure in one coupled domain cannot be repaired by assigning it a separate temporal transform without registering and independently motivating a new auxiliary.

## Strengthened synchronization surface

At Sigma_sync require jointly:

S1. The terrestrial/cosmic deployment-rate differential has reduced to the ordinary-runtime relation.

S2. Every past-directed null geodesic required for the inherited observable sky terminates on a genuine event in the executed deployment history rather than an initialized image or frequency translation.

S3. Macroscopic boundary data satisfy the ordinary-runtime constraints.

S4. No future event is declared actual merely by synchronization; the architecture does not require a block-universe ontology.

S5. No observation-specific state reset occurs at commissioning.

S6. The same causal histories that produced photons also produced their coupled material/remnant consequences.

## Imported failure conditions

Family B inherits and strengthens the convergent preprint's failure conditions:

**FB-1 Start/stop failure.** No constrained solution generates the required differential during deployment and removes it after synchronization without unacceptable residuals.

**FB-2 Geodesic/spectral shear.** The deployment geometry breaks the common relation among redshift, clock stretch, lens delays, spectra, or messenger propagation.

**FB-3 Truncated history.** The architecture cannot contain the genuinely executed thermal/stellar histories required by the inherited-observable matrix.

**FB-4 Present-day residual.** A large lapse, preferred-direction residual, CMB anisotropy, or other deployment signature survives where the model requires ordinary runtime.

**FB-5 Arbitrary lapse.** The target hierarchy is inserted through freely chosen N(x,s), alpha(x,s), or observation-specific boundary data rather than derived from the registered architecture.

**FB-6 Synchronization reset.** The final state requires discontinuous rewriting of photons, matter, remnants, spectra, or causal relations.

## Quantified target ratio

Using the preprint's explicit phenomenological target,

    tau_thermal ~= 13.8 Gyr
    Delta tau_E = 1 day,

the integrated proper-time ratio is approximately

    R_target
      = (13.8 x 10^9 yr)(365.2425 day/yr)/(1 day)
      ~= 5.04 x 10^12.

Thus a standard-history realization requires roughly five trillion units of cosmic proper time per unit of terrestrial proper time integrated across the Day-4 deployment interval.

This number is a target for the candidate realization, not a DFM hard-core commitment. A different physically adequate cosmic execution history could imply a different required ratio.

## CMC two-domain consequence at the target ratio

The previous quasi-homogeneous CMC approximation gave

    N_C/N_E ~ V_E/V_C.

If the integrated hierarchy is represented approximately by a comparable lapse hierarchy, then

    V_E/V_C ~ 5.04 x 10^12,

or

    V_C/V_E ~ 1.98 x 10^-13.

This is severe.

A CMC realization cannot claim explanatory success merely by inserting an effective cosmic lapse potential about thirteen orders of magnitude below the terrestrial reference potential. It must derive that hierarchy from independently motivated slice geometry, stress-energy, boundary data, or a common dynamical principle.

### Interpretation

The synchronized-lapse preprint clarifies the observational target; the CMC screen clarifies its physical cost.

The research question is now:

> Can one constrained creation-deployment boundary problem naturally generate an integrated proper-time hierarchy of order 10^12-10^13 while preserving the entire coupled observable matrix and smoothly retiring the differential at commissioning?

If yes, Family B would provide a physical realization stronger than the phenomenological synchronized-lapse model.

If no, the stipulated lapse remains a useful conceptual reconciliation but not a derived physical mechanism.

## Updated next computation

Do not immediately tune a radial V(r) profile to 1.98 x 10^-13.

Instead perform a source-of-hierarchy analysis:

1. decompose V into extrinsic-curvature and matter/stress contributions;
2. determine which terms can vary coherently by many orders of magnitude under one CMC boundary problem;
3. test whether a near-zero V_C is stable or structurally fine-tuned;
4. determine whether the same geometry predicts unacceptable lapse gradients/redshifts;
5. only then solve a radial profile.

This prevents the numerical target from becoming an input disguised as a result.


## Source-of-hierarchy analysis for the CMC potential

The simplified CMC lapse potential is

    V = K_ij K^ij + 4 pi G (rho + S)/c^4,

up to convention-dependent factors.

Decompose extrinsic curvature into trace and trace-free parts:

    K_ij = A_ij + (1/3) h_ij K,

so

    K_ij K^ij = A_ij A^ij + K^2/3.

Hence

    V = A_ij A^ij + K^2/3 + 4 pi G (rho + S)/c^4.

Under CMC,

    K = K(s)

is spatially constant on each slice. Therefore the trace contribution K^2/3 is a common positive floor across terrestrial and cosmic regions on the same slice.

This is a major constraint on the proposed hierarchy.

### Consequence of the common K floor

Let

    V_E = K^2/3 + X_E
    V_C = K^2/3 + X_C,

where

    X = A_ij A^ij + 4 pi G (rho + S)/c^4.

The synchronized-lapse target requires approximately

    V_C/V_E ~ 1.98 x 10^-13

in the quasi-homogeneous approximation.

If K^2/3 is appreciable relative to V_E, then V_C cannot become thirteen orders of magnitude smaller than V_E merely by reducing positive cosmic contributions: both regions retain the same K^2/3 floor.

Thus a large CMC lapse hierarchy requires at least one of the following:

1. K^2/3 is itself negligible compared with V_E;
2. V_E is made enormous by terrestrial-local X_E while V_C remains near the common floor;
3. the matter/stress term in X_C becomes negative enough to cancel the common positive floor;
4. the quasi-homogeneous approximation fails and derivative/boundary structure dominates the lapse solution.

These are now distinct candidate routes rather than one undifferentiated lapse assumption.

## Route H1: negligible common mean-curvature floor

Suppose

    K^2/3 << V_C << V_E.

Then the hierarchy must arise almost entirely from X_E/X_C.

Because A_ij A^ij is nonnegative, ordinary positive-sign matter/stress terms do not naturally drive V_C toward zero. They can instead make V_E large.

This changes the interpretation of the model: the hierarchy may be generated by a strongly elevated terrestrial effective potential rather than a specially suppressed cosmic clock potential.

But that route must explain why the Earth reference domain possesses an enormous localized geometric/stress contribution during Day 4 while remaining intact and leaving no forbidden post-synchronization residual.

**Disposition:** open, high localization/source burden.

## Route H2: cosmic cancellation

Suppose the common K floor is not negligible. Then achieving

    V_C/V_E ~ 10^-13

may require

    4 pi G (rho_C + S_C)/c^4

to cancel

    A_C^2 + K^2/3

to very high precision.

Unless a field equation, symmetry, constraint, or boundary principle enforces this relation, it is fine-tuning of the lapse potential.

A cancellation inserted solely to recover the desired Day-4 ratio fails FB-5.

**Disposition:** disfavored unless independently enforced.

## Route H3: terrestrial enhancement

Let the cosmic region possess an ordinary-scale V_C while the terrestrial region has

    V_E ~ R_target V_C.

This avoids making V_C anomalously tiny but requires a transient terrestrial enhancement of order the target hierarchy.

Because N_E is normalized to the terrestrial clock, the physical question becomes whether a creation-boundary structure around the terrestrial contour can generate this enhancement without:

- catastrophic local curvature;
- unacceptable stresses;
- extreme gravitational frequency shifts;
- horizon/pathology formation;
- residual preferred-frame signatures.

This route has a conceptual attraction: Genesis supplies an Earth-referenced creation chronology, so an Earth-local boundary structure is independently motivated at the theological/model level. That does not establish the required physics.

**Disposition:** active candidate route; requires geometric feasibility test.

## Route H4: elliptic/boundary amplification

The local approximation

    N ~ C/V

may be misleading when spatial derivatives dominate.

The full equation

    -D^2 N + V(r)N = C

can support profiles controlled by boundary conditions and length scales rather than the local ratio C/V alone.

This is the most important remaining mathematical opportunity.

A large lapse contrast might arise from a constrained global elliptic solution even when V_E/V_C is far smaller than R_target.

If so, Family B would gain explanatory leverage from the boundary-value structure itself rather than hiding the hierarchy in local source terms.

**Disposition:** highest-priority mathematical test.

## Dimensionless scaling

Let L be the characteristic transition length and write

    r = L x.

Then

    -D_x^2 N + [L^2 V(x)] N = L^2 C.

The relevant control parameter is not V alone but

    U(x) = L^2 V(x).

Therefore large spatial scales can materially change the balance between the derivative term and local potential term.

This means the previous two-domain estimate

    N_C/N_E ~ V_E/V_C

is only the slowly varying/local-potential limit. It must not be promoted to a general no-go theorem.

## New opportunity: hierarchy from geometry times scale

The dimensionless combination L^2 V suggests a potentially less tuned route:

    moderate geometric/source contrast
    x enormous creation-domain length scale
    -> strong elliptic lapse structure.

Whether this actually yields N_C/N_E ~ 5 x 10^12 under regular boundary conditions must be solved, not asserted.

Crucially, L is not an observation-specific free parameter if it is fixed by the global creation-domain geometry.

## Stability criterion

Any near-zero effective V_C or cancellation route must be tested for structural stability.

Define a sensitivity measure schematically:

    S_p = | d ln R / d ln p |,

where p is a boundary/source parameter.

If obtaining R ~ 10^12-10^13 requires S_p >> 1 for ordinary perturbations, the hierarchy is structurally fine-tuned unless a symmetry or constraint fixes p.

This supplies a quantitative anti-tuning discriminator.

## Source-of-hierarchy verdict

The decomposition rules out one easy story:

> CMC does not naturally provide a nearly zero cosmic lapse potential merely because the cosmic region is large or old.

The spatially constant K^2/3 term supplies a common floor, and A_ij A^ij is nonnegative.

The best remaining CMC opportunity is therefore **not** a thirteen-order local V contrast. It is a globally constrained elliptic solution in which derivative terms, domain scale, and independently motivated boundary data generate substantial lapse structure.

This route is both more interesting and more falsifiable.

## Revised next computation

Solve the dimensionless spherical equation

    -(1/x^2) d/dx [x^2 dN/dx] + U(x) N = J

under:

    regularity at the cosmic-domain center or inner boundary,
    N_E = 1 at the terrestrial reference boundary,
    one smooth U(x),
    no target-ratio fitting in the first pass.

Sweep physically generic U amplitude and transition-width classes and determine whether the elliptic operator can generate very large N contrasts without near-singular parameter choices.

Only after mapping that response should the 5.04 x 10^12 target be overlaid.

This preserves the distinction between prediction and fitting.
