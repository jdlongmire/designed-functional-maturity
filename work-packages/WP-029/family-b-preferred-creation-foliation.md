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
