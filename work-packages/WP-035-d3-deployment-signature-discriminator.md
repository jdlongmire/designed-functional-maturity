# WP-035: D3 Deployment-Signature Discriminator

**Status:** Active — candidate generation; no candidate frozen  
**Parents:** WP-029 (frozen Day 4 hypothesis), WP-031 (D3 registration), WP-034 (Day 4 reconciliation)  
**Origin:** step 3 of the execution order agreed with thinx-gpt on ai-bridge (2026-10-06)

## Question

> **What observable consequence follows from an Earth-reference-domain Day 4 deployment/synchronization architecture that is not equally expected under standard FLRW cosmology plus terrestrial nonprivilege?**

Until such a consequence exists and survives a severe test, terrestrial isotropy and the other WP-031 observations remain constraints and research opportunities, not positive physical evidence (WP-031).

## Governing rules

1. **Architecture before anomalies.** Every candidate is derived from the WP-029 frozen architecture and preregistered (see [`WP-035/preregistration-template.md`](WP-035/preregistration-template.md)) before any anomaly literature is consulted. Existing *null bounds* (published constraints that something is absent) may be used to test implementations; existing *anomalies* may not be used to select or tune candidates.
2. **Null result is a debit.** If, after candidate generation, no candidate yields a consequence that discriminates from FLRW plus nonprivilege, the asynchronous Day 4 auxiliary is recorded in the Bayesian ledger as an empirically idle auxiliary: a debit, not a neutral result. This rule is fixed now, before any candidate is evaluated.
3. **Failure demotes the implementation first.** Per WP-029, a failed candidate demotes its mechanism family. Repeated failure across families, or a demonstration that all admissible families are observationally equivalent to FLRW, demotes the Layer 2 asynchronous auxiliary without automatically defeating Layer 1 DFM.
4. **No fitted parameters.** Any scale a candidate depends on (domain boundary, synchronization epoch) must be fixed from the programme's stated commitments before comparison, not fitted to data.
5. **Numerical values quoted below from the literature are placeholders** for orientation and must be verified against primary sources (WP-007 ledger) before any candidate is frozen.

## Architecture premises used

From WP-029: (P1) a stable, encapsulated terrestrial reference domain experiences ~1 ordinary day during Day 4; (P2) the external cosmos genuinely executes the standard expansion and thermal history, Δτ_C ≈ 13.8 Gyr; (P3) a synchronization/commissioning transition `A(τ_E, {τ_C,i}) → Sync → R(L_R)` brings both into ordinary common runtime; (P4) ordinary physics thereafter.

Two quantities the architecture leaves unspecified, and which every candidate below forces into the open:

- **B, the encapsulation boundary.** Which bodies share the terrestrial domain: Earth only, Earth-Moon, the Sun and planets, the whole Solar System?
- **T_s, the synchronization epoch** in present Earth-local time, fixed by the programme's biblical chronology rather than by data.

## Candidate signatures

### D3-A: Domain-boundary process-age discontinuity

*Derivation.* Bodies inside B share Earth's short deployment history (mature state by initialization); bodies outside B genuinely executed long histories (P2). Indicators that record **process exposure** rather than initialized composition should therefore change discontinuously at B.

*Candidate observables.* Cosmic-ray exposure ages and solar-wind implantation in lunar regolith and meteorites; helioseismic and stellar-evolution age of the Sun; meteorite and lunar chronometers that integrate irradiation history.

*FLRW plus nonprivilege expects* continuity: the Sun, Moon, meteorite parent bodies and Earth are coeval within a few Myr (orientation values to verify: CAI Pb-Pb ≈ 4.567 Gyr; helioseismic solar age ≈ 4.6 Gyr).

*DFM-Day4 expects* a discontinuity at B, or, if B is drawn wide enough to avoid one, an explanation of why initialized interior bodies match the genuinely aged exterior ones. That second branch is a concordance burden of the CCN-001 kind and must be preregistered as such.

*Why it matters.* It is the cheapest candidate to specify and it cannot be satisfied by an observationally transparent synchronization.

### D3-B: Synchronization shell

*Derivation.* Light from external sources that was in flight at the synchronization event crossed the Sync transition; light emitted after it did not. Any transformation Sync applies to propagating signals (frequency, phase, timing, intensity) therefore marks sources beyond an Earth-centered radius r_s ≈ c · T_s and spares sources within it.

*Scale.* For T_s ≈ 6,000 to 10,000 years, r_s ≈ 1.8 to 3.1 kpc. The value must be fixed from chronology before comparison.

*Candidate observables.* Concordance of independent distance and timing indicators straddling r_s: parallax against standard candles, pulsar spin-down and dispersion consistency, spectral-line ratios, eclipsing-binary and Cepheid timing.

*FLRW plus nonprivilege expects* no Earth-centered radial feature at r_s.

*DFM-Day4 expects* either a feature at r_s, or a proof that Sync transforms nothing observable. The latter does not rescue the candidate; it moves the architecture into D3-D.

### D3-C: Implementation constraint inheritance

*Derivation.* Each WP-029 mechanism family carries the observational constraints of the physics it borrows.

*Family B2 (dynamical khronon/aether)* inherits preferred-frame and Lorentz-violation bounds: gravitational-wave speed (orientation: GW170817), post-Newtonian preferred-frame parameters α1 and α2, and big-bang-nucleosynthesis bounds on the cosmological gravitational coupling.

*Family A (single deployment metric)* inherits its own recorded result: a large lapse enters null propagation and the frequency relation, so ordinary-looking spectra constrain it (WP-029 Family A minimal-subfamily verdict).

*Status.* These checks compare implementations against null bounds, not anomalies, so they are permitted before freeze. They are severe tests of implementations rather than discriminators of DFM against FLRW, and they should run first because they are cheap and can eliminate families outright.

### D3-D: Observational-equivalence analysis

*Derivation.* For each family, determine whether every observable accessible from the terrestrial domain after commissioning is invariant under the deployment architecture.

*Expectation.* A pure foliation choice (Family B without dynamics) is likely to be unobservable, as foliation choice is in general relativity.

*Consequence.* A family proven observationally equivalent to FLRW has no D3 signature by construction and falls under governing rule 2. This analysis protects the programme from treating the absence of a signature as compatibility.

### D3-E: Radial process-time gradient (remote-observer non-equivalence)

*Derivation.* If external process time τ_C depends on distance from the terrestrial domain, rather than being homogeneous across the external cosmos, then remote observers are not statistically equivalent to us. Structures at equal lookback time would carry different process ages depending on their distance from Earth.

*Candidate observables.* Copernican-principle tests that probe what remote observers see: kinematic Sunyaev-Zel'dovich and CMB spectral-distortion tests of the Caldwell-Stebbins type, and the age-lookback relation of stellar populations.

*FLRW plus nonprivilege expects* homogeneity.

*DFM-Day4 expects* either a measurable gradient, or homogeneity. Homogeneity makes this candidate null and must be declared in advance.

## Sequence

1. Fix B and T_s from the programme's stated commitments (Principal Investigator decision).
2. Run D3-C against verified null bounds, then D3-D, to eliminate or classify mechanism families.
3. Preregister D3-A and D3-B (and D3-E if the surviving families predict a gradient), freeze them by commit, then compare against data.
4. Record each outcome in the Bayesian ledger; apply governing rule 2 if no discriminating candidate survives.

## Success criterion

At least one preregistered candidate whose DFM-Day4 expectation differs from the FLRW-plus-nonprivilege expectation by more than current measurement uncertainty, tested against data not used in its construction.

Human-Curated, AI-Enabled (HCAE)
