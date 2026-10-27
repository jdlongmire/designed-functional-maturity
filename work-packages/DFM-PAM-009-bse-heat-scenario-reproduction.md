# DFM-PAM-009: BSE Heat-Inventory Scenario Reproduction

**Status:** Published-model arithmetic reproduced in code; automated checks configured but CI results not inspected. **Parent:** DFM-PAM-008.

## Published model family
Borexino Collaboration, *Phys. Rev. D* **101**, 012009 (2020), Table II, https://arxiv.org/abs/1909.02257, reports BSE (crust **plus** mantle) isotope-element masses and model radiogenic powers. Its representative cosmochemical, geochemical, geodynamical and fully radiogenic scenarios give **11.3 ± 1.6**, **20.2 ± 3.8**, **33.5 ± 3.6**, and **47 ± 2 TW**. These are model scenarios, not four independent measurements. The fully radiogenic model is a comparison extreme, not an observationally established Earth composition.

The code `research/rcim/track_a_bse_scenarios.py` recomputes each model's present-day heat from its published U, Th and K masses using separately published elemental coefficients. The code uses the masses in **10^16 kg for U and Th, 10^19 kg for K**. Its test accepts a rounding-level difference (<2 TW), not a precision validation. The independent-error diagnostic is *not* the original model's uncertainty estimate: the cited study assumes fully correlated abundance errors.

## What this establishes
- A consistent mass and coefficient convention can reproduce published model-power orders of magnitude.
- BSE already includes crust; crust power must not be added a second time.
- Observed global surface flux (~47 ± 2 TW) must not be equated with radioactive power.
- Present radiogenic power depends on existing parent inventories, not on whether stable radiogenic daughters were initialized.

## What remains open
1. Verify nuclear decay energies, particularly branch-weighted K-40 deposited heat.
2. Reconcile elemental coefficients with isotope-specific decay calculations quantitatively, including abundance, atomic mass, neutrino losses and uncertainties.
3. Select an internally consistent lithosphere/crust/mantle partition of **one** BSE scenario, preserving correlations.
4. Incorporate independent geoneutrino evidence: Abe et al. (2022), https://doi.org/10.1029/2022GL099566, report data that disfavor high-radiogenic and fully radiogenic scenarios under specified mantle-distribution assumptions.
5. Model thermal transport and geological history. Matching a present-day BSE source inventory alone does not establish DFM's historical thermal plausibility.

## Interpretation
The new result is **literature-model reproduction**, not an independent empirical fit or a test discriminating DFM from conventional deep time. The Auxiliary Hypothesis Parity Principle requires preserving both independently observed geoneutrino evidence and explicit compositional-model assumptions.

**Source references:**
- Borexino Collaboration (2020), *Comprehensive geoneutrino analysis with Borexino*, https://arxiv.org/abs/1909.02257.
- Abe et al. (2022), *Geophysical Research Letters*, https://doi.org/10.1029/2022GL099566.
- Geoneutrinos.org model presets, https://geoneutrinos.org/model/.
