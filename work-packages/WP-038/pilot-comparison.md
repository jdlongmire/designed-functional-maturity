# WP-038 Pilot Comparison: Event Accounting at Presence/Absence Level

Run date: 2026-11-15. Data: pilot evidence matrices (see data/data-manifest.md). Level of analysis: presence/absence patterns only. This is a calibration exercise for the accounting machinery, not a model verdict; the benchmark's discriminating evidence (boundaries, TSD, LTR divergence, shared mutations) is not present in the pilot data.

## Method
For each locus, the presence pattern across the taxon panel was scored under two event accountings on the accepted primate phylogeny:
- **Single-gain accounting (C0-style):** one integration at the most recent common ancestor of the taxa carrying the locus, plus one loss per maximal absent subclade inside that ancestral range.
- **Independent-gain accounting (coincidence-style):** one integration per maximal present subclade, no losses.
Both accountings charge one AHPP unit per event, symmetrically, per the formalization.

## Results

| Dataset | Loci | Single-gain events | Independent-gain events | Loci needing a 2nd event |
|---|---|---|---|---|
| RV15 training (human-chimp pairs) | 206 | 206 gains + 30 losses = 236 | 236 gains | 30 (14.6%) |
| RV15 held-out (census only, not scored) | 136 | 136 + 14 = 150 | 149 | 13 |
| RV15 full matrix (all anchor pairs) | 862 | 862 + 349 = 1211 | 1200 | 297 |
| Grandi HERV-W (6 taxa, reconciled matrix) | 211 | 211 + 17 = 228 | 237 | 15 |

## Reading
1. On the training set the two accountings tie exactly at 236 events. At presence/absence granularity, a loss and an independent gain cost the same unit, so pattern data alone cannot separate common ancestry from coincidence; the accounting trades them one for one. This is a property of the evidence level, not of either model, and it confirms the benchmark design decision that scoring must use joint sequence-level patterns per locus, where the models' predictions actually diverge.
2. The discriminating minority is identifiable: 30 of 206 training loci (14.6%) have non-nested patterns (for example present in human, chimpanzee and orangutan but absent in gorilla) that cost a second event under any accounting. These loci are where boundary, TSD and shared-mutation extraction matters most, and they should be prioritized in the full slice 5 re-extraction.
3. HERV-W leans the other way: single-gain accounting is cheaper (228 vs 237), driven by 121 of 211 loci present in all six taxa. One family behaving differently from the pooled set is expected and is why the benchmark scores functional and family strata separately. (Grandi figures recomputed on the reconciled matrix; see grandi-reconciliation.md. The first-filed values were computed on a defective parse and are superseded.)
4. Held-out figures are reported as census only, per the unblinding rule: no model was fitted to the training numbers above, so nothing has been scored against held-out data, and the split remains unspent.
5. D1, D2 and D4 are not scored at this level: their differences from C0 live at and below the creation boundary and in sequence evolution, which presence/absence cannot express. Any presence-level claim for or against them would be an artifact of the accounting, and none is made.

## Next data step
Full slice 5 re-extraction of the priority subset (the 30 non-nested training loci first) against current assemblies, populating both flanks, TSD, LTR divergence and shared derived marks. That is the first dataset on which the formalized models can actually be compared.

Human-Curated, AI-Enabled (HCAE)
