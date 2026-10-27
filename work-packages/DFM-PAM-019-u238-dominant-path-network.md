# DFM-PAM-019: U-238 Dominant-Path Population Network

**Status:** Provisional 15-node population topology committed; **not** a complete evaluated U-238 chain and **not** a heat-production model.

## Implemented
`research/rcim/track_a_u238_dominant_chain.py` specifies the major sequence U-238 -> Th-234 -> Pa-234m -> U-234 -> Th-230 -> Ra-226 -> Rn-222 -> Po-218 -> Pb-214 -> Bi-214 -> Po-214 -> Pb-210 -> Bi-210 -> Po-210 -> stable Pb-206. It uses the SciPy matrix-exponential solver to compare initially depleted versus nominal secular-equilibrium intermediate populations over 6,000 years.

The numerical model intentionally sets **all deposited-energy entries to zero**. It is a population-topology test and must not be used to infer cumulative heat. Rounded half-lives are provisional and must be checked isotope by isotope against a version-pinned evaluated nuclear dataset.

## Known omissions
- Minor alpha/beta branches, including alternate Bi-214, Bi-210 and Po-218 pathways, are not fully represented.
- Pa-234 / Pa-234m isomeric populations and transitions require evaluated branching treatment.
- Short-lived daughters require independent evaluation of radiation energy, neutrino losses, alpha recoil and spatial deposition.
- The equilibrium case uses idealized parent-matched activities, not observed mineral U-series compositions.
- Stable Pb-206 can be initialized independently of radioactive intermediate populations; the stable Pb inventory here is zero by default and not a geological assertion.

## Source audit targets
- IAEA LiveChart/ENSDF, https://www-nds.iaea.org/relnsd/vcharthtml/VChartHTML.html
- NNDC NuDat 3, https://www.nndc.bnl.gov/nudat3/
- IAEA decay data API documentation, https://iaea-nds.github.io/lc_api_notebook/

## Acceptance gate
Validate all isotope half-lives and branch probabilities against evaluated records; add branch-complete energy deposition with neutrino accounting; compare resulting activity ratios and integrated heat under explicit initial populations; and evaluate independent U-series mineral data. **Track A thermal plausibility is not established.**
