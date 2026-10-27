# DFM-PAM-010: Isotope-to-Elemental Coefficient Reconciliation

**Status:** Analytical comparison code added; evaluated nuclear-data validation and CI execution not confirmed.

## Objective
Compare two independent present-day heat-production calculations:
1. Parent-isotope decay constants, approximate heat per decay, molar mass and present natural isotope fractions.
2. Published elemental U, Th and K heat-production coefficients.

The executable `research/rcim/track_a_coefficient_reconciliation.py` prints each element's W/kg by both routes and their ratio. It does not tune inputs to force a match.

## Required technical corrections before certification
- Verify decay energy **deposited as heat**, subtracting escaping neutrino energy and including all relevant daughter-chain radiation and branching.
- Verify K-40 beta-minus and electron-capture branches separately.
- Replace approximate atomic fractions used as mass fractions with abundance-weighted molar-mass conversion.
- Reconcile U-234 and decay-chain equilibrium assumptions.
- Confirm reference year, source convention and uncertainty for elemental heat coefficients.
- Execute the CI suite and inspect results, rather than treating workflow configuration as validation.

## BSE partition protocol
The BSE scenario totals in DFM-PAM-009 cover crust plus mantle. A crust/mantle model must partition each parent-element mass with nonnegative fractions that sum to one, preserve the scenario's total element mass and correlated uncertainties, and use independently supported crust estimates. It must not treat inferred mantle abundances as direct measurements. Thermal transport remains a separate model.

## Acceptance criteria
Coefficient agreement within independently justified uncertainty and convention differences is a V1 milestone; simple numerical proximity is not sufficient. A reservoir partition preserving mass and published compositional bounds is V2. Comparison to measured heat flow and geoneutrinos, including nonradiogenic contributions, is V3. None of these milestones alone validates DFM's historical initialization hypothesis.
