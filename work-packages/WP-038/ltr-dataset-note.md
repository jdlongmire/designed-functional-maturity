# WP-038 Alignment-Grade LTR Divergence Dataset (Priority Loci)

Date: 2026-11-15. Data: data/ltr-divergence-aligned.csv (supersedes the k-mer-span estimates in data/ltr-divergence.csv, which are retained for provenance). Intervals: human GRCh38, chimpanzee panTro6, gorilla gorGor6, orangutan ponAbe3, retrieved from the UCSC genome API on chain-derived spans, flank-control passed.

## Method
LTR pairs were located by the consistent-offset direct-repeat detector, extracted with 350 bp of margin, and aligned pairwise (local alignment, match 2, mismatch -3, gap open -5, extend -2). Divergence is 1 minus identity over aligned columns (substitutions only; gap columns excluded from the denominator). 90 of 116 species-intervals yielded an aligned pair; failures are short intervals (solo-LTR and single-anchor loci), degraded copies, and two loci with no detectable pair in any species.

## Results
- Divergence range across all species: **0.025 to 0.124**. Medians by species: human 0.067 (n=26), chimpanzee 0.068 (n=23), gorilla 0.060 (n=20), orangutan 0.062 (n=21).
- Cross-species consistency: at the 22 loci with estimates in at least 3 species, the median spread between species is 0.016 and the maximum 0.035. The four species' LTR pairs at the same locus report near-equal divergences, as expected if each pair started identical at one integration and aged in place. This consistency is itself a dataset quality check: independent assemblies and independent extractions converge on the same per-locus values.

## The measuring instrument for the D4 severe test
D4 (exogenization within a compressed post-creation timeline) must fit these divergences at stated rates. The arithmetic, stated neutrally:
- At the standard primate neutral rate (mu about 1e-9 per site per year per lineage; the two LTR copies diverge at 2 mu), the median divergence of 0.065 implies about 32 Myr since integration, and the maximum 0.124 implies about 62 Myr. Rate uncertainty of a factor of two moves these proportionally.
- Under a compressed timeline of T years for all post-creation divergence, the required per-lineage rate is mu = d / 2T:

| Timeline T | Required mu at median d=0.065 | Multiple of standard | Required mu at max d=0.124 | Multiple |
|---|---|---|---|---|
| 6,000 yr | 5.4e-6 | about 5,400x | 1.0e-5 | about 10,300x |
| 10,000 yr | 3.3e-6 | about 3,300x | 6.2e-6 | about 6,200x |
| 100,000 yr | 3.3e-7 | about 325x | 6.2e-7 | about 620x |
| 1,000,000 yr | 3.3e-8 | about 33x | 6.2e-8 | about 62x |

This table is the instrument, not a verdict. Under the auxiliary-symmetry section, D4 may invoke accelerated rates, but it must state them numerically, hold them consistently across loci (a single rate regime must fit the whole distribution, including the 0.025 minimum and the cross-species concordance), and carry the AHPP charge for the invocation. A rate regime fitted per-locus would be a degenerative modification under the programme's rules. The same instrument, read the other way, is what any mainstream reading uses to date the integrations; the numbers are common property.

## Limits
Priority-locus subset only (30 loci, HERV-K(HML2)-heavy); extension to the resolved training set is mechanical now that the pipeline exists. Divergence estimates assume the detected repeat pair is the provirus's own LTR pair; at loci where human and gorilla offsets disagreed in the first pass (0130, 0490), treat values as provisional pending manual inspection. Gene conversion between LTR copies, which homogenizes pairs and biases ages downward, is not modeled in this pass and is a declared refinement.

Human-Curated, AI-Enabled (HCAE)
