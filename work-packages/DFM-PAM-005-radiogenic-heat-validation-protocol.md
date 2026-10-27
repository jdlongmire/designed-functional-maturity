# DFM-PAM-005: Radiogenic Heat Validation and Calibration Protocol

**Status:** Preregistered validation plan; numerical CI configured, results not yet inspected. **Parent:** DFM-PAM-004.

## Verification stages
**V0: Code correctness.** Run all three standard-library scripts under Python 3.12 in `.github/workflows/dfm-track-a-radiogenic.yml`. Verify decay half-life identities, conservation, nonnegative source power, parent decline and no heat from stable daughter inventories. CI passing demonstrates internal code checks only, not scientific validity.

**V1: Nuclear constants.** Compare half-lives, branching fractions, emitted energy, neutrino energy and secular-equilibrium assumptions with authoritative evaluated nuclear data (e.g., NNDC NuDat/ENSDF, IAEA LiveChart). Record version, access date, uncertainty, conversion and each citation. Current energy constants are preliminary; especially K-40's effective heat-per-decay must be branch-weighted and independently verified. Do not treat code defaults as accepted calibrated values.

**V2: Terrestrial source inventories.** Define independent crust, lithospheric mantle and convecting mantle masses and U, Th, K concentrations with uncertainties. Convert total elemental potassium to K-40 with an independently validated isotope fraction. Distinguish present-day inventories from initial masses by ordinary decay back-calculation over the stipulated post-boundary interval. Check against geochemical and geoneutrino constraints; avoid assuming all reservoir inventories are directly observed.

**V3: Heat balance.** Compare present-day radiogenic power to observed terrestrial surface heat flow while retaining nonradiogenic contributions (secular cooling, core heat, latent/gravitational terms, and possible local hydrothermal transport). Do not equate total surface heat flow with radiogenic production. A one-box thermal response is a sensitivity illustration, not a solution of spatial heat transport.

**V4: Geological consequences.** Evaluate temperature-time constraints, mineral closure, metamorphic grades, volcanism, and regional heat-flow patterns. Where the model stipulates mature initial minerals, document which later features it predicts or accommodates through ordinary dynamics.

**V5: Coupled U-Pb audit.** For each mineral population, specify parent isotope ratios, initial common/radiogenic Pb families, thermal history and alteration independently of the target isotope age. Assess paired U decay-chain concordance and discordance alongside heat source constraints. Record extra free parameters and unresolved observations.

## Calibration data register (unpopulated)
| Input | Units | Evidence source needed | Status |
|---|---|---|---|
| U-238 half-life and heat per chain | yr; MeV | Evaluated nuclear data | Preliminary code constants |
| U-235 half-life and heat per chain | yr; MeV | Evaluated nuclear data | Preliminary code constants |
| Th-232 half-life and heat per chain | yr; MeV | Evaluated nuclear data | Preliminary code constants |
| K-40 half-life, branches, heat | yr; fractions; MeV | Evaluated nuclear data | Preliminary effective constant |
| Crust U/Th/K concentrations and mass | kg/kg; kg | Published geochemistry | Not entered |
| Mantle U/Th/K concentrations and mass | kg/kg; kg | Published models and geoneutrinos | Not entered |
| Terrestrial surface heat flow | TW | Published heat-flow synthesis | Not entered |
| Reservoir heat exchange | W | Geophysical constraints | Not entered |
| Mineral U-Pb ratios and petrography | ratios; uncertainties | Measured zircon datasets | Not entered |

## Preregistration and interpretation rules
- Lock nuclear constants and selected reservoir parameter ranges before comparing against target heat-flow observations.
- Report uncertainties and sensitivity intervals, not only point estimates.
- Do not count initialized stable daughter inventories as post-boundary radiogenic heat.
- Do not infer that absence of accelerated-decay heat automatically establishes global thermal plausibility.
- Preserve independent published conventional accounts and assess auxiliaries under DFM-PAM-001's parity principle.
- A successful V0 is **code verified**; V1 is **nuclear parameters verified**; V2/V3 are **Earth-source calibrated**; V4/V5 are **geologically cross-checked**. These milestones must not be conflated.

## Decision gate
Track A global thermal plausibility remains **open** until at least V1 through V3 have been completed with bounded uncertainties and no unresolved physical contradiction. Coupled U-Pb explanatory adequacy remains open until V5.
