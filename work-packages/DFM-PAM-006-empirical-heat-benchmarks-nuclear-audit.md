# DFM-PAM-006: Initial Empirical Heat-Budget Benchmarks and Nuclear-Data Audit

**Date:** 2026-10-27. **Status:** Source-linked calibration intake; not a fitted Earth model. **Parent:** DFM-PAM-005.

## Observational and inferred benchmarks

| Quantity | Published estimate | Epistemic status | Source |
|---|---|---|---|
| Global surface heat flux | 47 ± 2 TW | Spatial synthesis of heat-flow measurements plus oceanic thermal corrections, not a raw single instrument measurement | Davies & Davies (2010), https://doi.org/10.5194/se-1-5-2010 |
| Alternative global surface heat flux | 46 ± 3 TW | Independent synthesis, partly overlapping data | Jaupart et al. (2007), cited by Dye (2012), https://doi.org/10.1029/2012RG000400 |
| Radiogenic terrestrial power | Often ~20 ± 10 TW; published estimates roughly 10–30 TW | Model-dependent geochemical/geophysical estimate, **not** a direct whole-Earth measurement | Dye, conference contribution (2025), https://indico-cdex.ep.tsinghua.edu.cn/event/175/contributions/contributions.pdf |
| Continental crust radiogenic power | 7.1 (+2.1 / -1.6) TW | Geochemical model estimate | Dye, conference contribution (2025), same URL |
| K-40 decay branches | Approximately 89.1% to Ca-40, 10.9% to Ar-40 | Evaluated nuclear data, precision/source version to reconcile | ICRP-107-derived MIRDspecs https://mirdsoft.org/products/MIRDspecs/MIRDspecs_HTMLs/K-40.htm |

**Critical separation:** 47 ± 2 TW surface flux and 20 ± 10 TW radiogenic production are **different quantities**. Their difference cannot be declared a directly measured cooling rate; it also depends on the models and uncertainty used to infer radiogenic power and the Earth's nonradiogenic sources.

## Source parameter audit

| Parameter | Prototype | Cross-check | Decision |
|---|---|---|---|
| U-238 half-life | 4.468 Ga | IAEA LiveChart example and ICRP-derived MIRDspecs U-238: 4.468 Ga | Consistent at stated precision |
| U-235 half-life | 0.7038 Ga | Published geochemistry table, DOI 10.1016/j.pce.2024.103602 | Consistent at stated precision |
| Th-232 half-life | 14.05 Ga | Published geochemistry table, DOI 10.1016/j.pce.2024.103602 | Consistent at stated precision |
| K-40 half-life | 1.248 Ga | ICRP-derived MIRDspecs: 1.251 Ga | Approximate; reconcile evaluation and uncertainty |
| U-238 heat/chain | 47.7 MeV | Not independently established by current retrieval | UNVERIFIED |
| U-235 heat/chain | 44.4 MeV | Not independently established by current retrieval | UNVERIFIED |
| Th-232 heat/chain | 40.4 MeV | Not independently established by current retrieval | UNVERIFIED |
| K-40 effective heat/decay | 0.65 MeV | ICRP-derived radiation summaries indicate electron/photon energy, but full heat calculation must integrate decay branches and neutrino losses | UNVERIFIED; do not use as validated coefficient |

**Unit warning:** The 2024 heat-production table reports K-40 heat production as 3.4737e-9 W/kg while also reporting isotope-specific values for U/Th. Its K value may correspond to **natural elemental potassium rather than pure K-40**, despite its label. Do not use it as a pure K-40 coefficient without verifying the table's original convention and isotope abundance. An order-of-magnitude/unit error here would invalidate global heat calculations.

## Conditional illustrative comparison (not a fit)
If surface heat loss is represented by 47 TW and radiogenic generation by an illustrative 20 TW, the simple arithmetic difference is 27 TW. It is **not** a validated secular-cooling power, nor does it establish any particular Earth chronology. Initial thermal energy and transport mechanisms must be modeled separately. The ~10–30 TW radiogenic range reflects substantive model uncertainty; it is not a uniform statistical confidence interval.

## Source traceability
- Davies, J. H. and Davies, D. R. (2010). Earth's surface heat flux. *Solid Earth* 1, 5–24. https://doi.org/10.5194/se-1-5-2010
- Dye, S. T. (2012). Geoneutrinos and the radioactive power of the Earth. *Reviews of Geophysics* 50, RG3007. https://doi.org/10.1029/2012RG000400
- Dye (2025). Interpreting Earth's geoneutrino flux, conference contribution. https://indico-cdex.ep.tsinghua.edu.cn/event/175/contributions/contributions.pdf
- IAEA Nuclear Data Section. LiveChart API documentation and ENSDF-derived data. https://iaea-nds.github.io/lc_api_notebook/
- MIRDspecs (ICRP Publication 107 derived). K-40 radionuclide data. https://mirdsoft.org/products/MIRDspecs/MIRDspecs_HTMLs/K-40.htm
- Radiogenic heat production in North Sea sediments (2024), isotope coefficient compilation. https://doi.org/10.1016/j.pce.2024.103602

## Acceptance gates
1. Resolve K-40 coefficient conventions and verify all heat energies against evaluated decay data before any Earth-wide numerical claim.
2. Record actual CI execution results; configuration alone is not a passed test.
3. Import independently sourced present-day U/Th/K crust and mantle inventories, explicitly tracking concentration uncertainties.
4. Distinguish total surface flux, radiogenic source power, and internal thermal storage/transport.
5. Compare U-Pb daughter initialization against mineral observations independently of thermal-budget fitting.

**Current Track A judgment:** Observational target and some decay constants identified; thermal calibration and whole-Earth plausibility **not established**.
