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
