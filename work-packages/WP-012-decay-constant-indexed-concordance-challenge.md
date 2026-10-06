# WP-012: Decay-Constant-Indexed Concordance Challenge

**Status:** Captured / not executed  
**Parent:** DFM Research Programme  
**Depends on:** WP-008 through WP-011

## Purpose

Formalize the central mathematical problem exposed by the U-Pb and Rb-Sr severe tests:

> Can a genuinely non-temporal common initialization generator produce concordant radiogenic relationships across isotope systems with distinct measured decay constants without containing a latent parameter mathematically equivalent to elapsed time?

This WP records the challenge for later execution. It does not presume that such a generator exists.

## 1. Problem statement

For isotope system `i` with decay constant `lambda_i`, conventional closed-system radiogenic growth yields a slope or daughter-parent relation of the form:

```text
m_i = exp(lambda_i T) - 1
```

Here `i` indexes an isotope system, `m_i` is its radiogenic slope or daughter-parent growth relation, `lambda_i` is its measured decay constant, and `T` is elapsed/retrodictive time.

Cross-system concordance occurs when distinct isotope systems recover approximately the same `T`:

```text
T_i = ln(1 + m_i) / lambda_i ~= T
```

Here `T_i` is the duration inferred from isotope system `i`; `ln` is the natural logarithm. Approximate equality across `T_i` values is the cross-system concordance condition.

WP-008 through WP-011 established that DFM physical initialization constraints can motivate:

- parent radionuclide inventory;
- source-reservoir mass balance;
- common initial daughter/reference baselines;
- elemental parent/daughter differentiation;
- mineral partitioning;
- population structure.

They have not yet derived the family of decay-constant-indexed daughter relations represented by `m_i`.

## 2. Formal challenge

Let a proposed non-temporal initialization generator be:

```text
G(q, C) -> {m_1, m_2, ..., m_n}
```

where:

- `q` is a common initialization parameter or state variable;
- `C` is a set of independently motivated physical constraints;
- `m_i` is the generated radiogenic relation for isotope system `i`.

The generator succeeds only if:

1. `q` is independently defined and measurable or derivable;
2. `q` is not fitted from conventional radiometric ages;
3. `C` is independently motivated;
4. the generator predicts multiple `m_i` values for distinct `lambda_i`;
5. the resulting inferred values
   ```text
   ln(1 + m_i) / lambda_i
   ```
   converge without having that convergence inserted as a target.

## 3. Age-equivalence criterion

Define:

```text
T_i(G) = ln(1 + m_i(G)) / lambda_i
```

Here `G` is the proposed initialization generator and `m_i(G)` is the relation it generates for isotope system `i`.

If for all modeled systems:

```text
T_i(G) = h(q)
```

and `q` has no independent physical content apart from setting `h(q)`, then `q` is an age surrogate.

Renaming elapsed time does not constitute an alternative generator.

## 4. Candidate theorem direction

A possible formal result to investigate:

### Decay-Constant-Indexed Concordance Proposition

Given at least two independent isotope systems with distinct positive decay constants `lambda_1 != lambda_2`, exact common-age concordance requires generated relations satisfying:

```text
ln(1 + m_1)/lambda_1
  =
ln(1 + m_2)/lambda_2
```

or equivalently:

```text
1 + m_2
  =
(1 + m_1)^(lambda_2/lambda_1)
```

Any initialization generator reproducing exact concordance must therefore impose a cross-system relation isomorphic to the common-time relation.

The open question is whether such an isomorphic relation can arise from a physically independent non-temporal state variable rather than elapsed time.

## 5. Research questions

1. Is the common-time parameter mathematically identifiable from exact multi-system concordance?
2. Under what conditions is a non-temporal generator observationally equivalent to elapsed time?
3. Can a non-temporal state variable possess independent physical content while inducing the same exponential family?
4. Does adding three or more distinct decay constants overdetermine candidate non-temporal generators?
5. How do uncertainty, open-system behavior, mixing, inheritance, and resetting alter identifiability?
6. Can reservoir mass balance impose any portion of the cross-system exponential relation?
7. What novel prediction would distinguish an orderly-marker generator from traversed decay time?

## 6. Severe-test standard

A candidate DFM generator must not merely fit existing concordant systems.

It must predict at least one of:

- a previously unused isotope-system relation;
- a bounded deviation from conventional concordance;
- a reservoir-specific covariance;
- a mineralogical dependency;
- a discordance pattern;
- another observable not used to construct the generator.

Without such novelty, observational equivalence to elapsed time leaves the DFM auxiliary empirically underdetermined.

## 7. Potential outcomes

### Outcome A: independent non-temporal generator found

DFM gains a quantitative mechanism for orderly radiometric markers and must derive novel discriminators.

### Outcome B: mathematical observational equivalence

A non-temporal generator can reproduce concordance but is observationally equivalent to elapsed time over existing isotope data.

DFM retains logical possibility but gains little empirical preference.

### Outcome C: latent-time necessity

Any sufficiently general generator reproducing multi-system concordance is shown to contain a scalar parameter mathematically equivalent to elapsed time.

This would substantially weaken the present orderly-marker auxiliary and require DFM to reconsider the role of radiometric concordance in its initialization model.

### Outcome D: current formalism insufficient

The question cannot be resolved without a more complete physical model of reservoir initialization.

The programme records the dependency rather than adding unconstrained auxiliaries.

## 8. Guardrails

- Do not dispute measured decay constants merely to avoid the challenge.
- Do not use target ages as initialization inputs.
- Do not invoke design as a substitute for a physical generator.
- Do not classify all discordance as disturbance without independent evidence.
- Do not require DFM to preserve a radiogenic auxiliary if severe testing defeats it.
- Distinguish failure of an auxiliary from failure of the broader DFM research programme.

## 9. Deliverables when activated

1. Formal mathematical note on parameter identifiability.
2. Multi-system symbolic model for at least U-Pb, Rb-Sr, and Sm-Nd.
3. Numerical sensitivity analysis under measurement uncertainty.
4. Age-surrogate detection criteria.
5. Comparison of temporal and candidate non-temporal generators.
6. Explicit theorem/proposition status with proof, counterexample, or unresolved conditions.
7. Programme recommendation for the orderly-marker hypothesis.

## 10. Current disposition

**Captured for later execution.**

The radiometric workstream has reached a natural formal checkpoint. Further execution should occur only after programme-level reprioritization confirms that this is the highest-value next investment for DFM.

## Re-entry criterion (proposed, pending Principal Investigator decision)

**Status: DRAFT for JD's review. JD decides whether any of this is adopted, amended, or discarded. Nothing here changes WP-012's current disposition until he does.**

Proposed triggers. WP-012 moves from "captured" to "active" when the first of these occurs:

1. **Calendar backstop.** Twelve months after adoption of this criterion (date to be set by JD), unless the programme has recorded a dated decision to extend the deferral with a stated reason.
2. **Deliverable gate.** Completion of the WP-013 phased-deployment and provenance deliverables, or of any later named phased-deployment deliverable JD designates, whichever comes first. The identifiability result is then the next open burden on the radiogenic auxiliary.
3. **Public-claim gate.** Any new radiogenic claim in a public artifact (paper, page, video, or OBJECTIONS-AND-RESPONSES entry), including any statement that an orderly-marker or common-initialization generator accounts for concordance. Such a claim may not be published while CCN-001 or CCN-002 stands at "Severe Challenge / active" unless WP-012 has first been activated or the claim is explicitly labeled as an undefended auxiliary.

Rationale. Under the severe-test rule, an auxiliary that has met an adverse test is not retired from scrutiny by being reprioritized. CCN-001 and CCN-002 remain at "Severe Challenge / active" and WP-008 and WP-009 found no age-independent generator, so the negative heuristic protects the hard core while the protective belt carries an acknowledged open burden. The symmetric evidential standard forbids granting DFM a deferral that a competing programme would not receive on its own adverse results. A deferral with no stated exit condition is indistinguishable, to a Lakatosian critic, from a degenerating problem shift: the belt is held fixed while attention moves to areas where the positive heuristic is producing results. Pre-registering the exit conditions converts the pivot into an openly scheduled sequence, keeps the programme's progressive-versus-degenerative accounting auditable, and leaves the theological hard core untouched by the fate of this one auxiliary.

