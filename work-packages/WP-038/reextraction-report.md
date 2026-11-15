# WP-038 Slice 5 Re-extraction: Priority Loci, First Pass (Coordinate Level)

Date: 2026-11-15. Input: data/priority-loci.csv (30 training loci whose 2012-era presence patterns required a second event under any accounting). Method per reextraction-protocol.md, first pass: flank-anchor geometry plus an internal-anchor homology test. Data: data/reextraction-results.csv.

## Method in brief
Each locus's human 15 kb excerpt (GRCh37) was split into a 5' flank anchor (first 2 kb), a 3' flank anchor (last 2 kb) and an internal anchor (central 2 kb, proviral). Anchors were carried GRCh37 to GRCh38 and then to gorGor6, ponAbe3 and panTro6 with UCSC liftOver chains. The inter-anchor gap in each target genome measures what sits between the flanks: about 11,000 bp when an element-length interval is present (the human value at all 30 loci, which validates the geometry), about 2,000 to 4,500 bp at a clean empty site. For gorilla, the internal anchor was then checked: if the human proviral core maps inside the gorilla interval, the interval carries homologous ERV sequence, not filler.

## Results for the 29 gorilla-absent (11010) loci
- **22 loci: absence call not supported.** Gorilla flank gap is element-length (9,603 to 11,765 bp) and the human internal anchor maps inside the gorilla interval. On the current gorilla assembly these loci carry homologous ERV sequence at the orthologous position. The Retrovirology 2015 gorilla absence, derived from the 2012 gorGor3-era assembly and pol-probe search, does not survive re-extraction.
- **1 locus (RV15-0130): unresolved.** Flank gap element-length (9,603 bp) but the internal anchor does not map in gorilla; the interval is filled with sequence not homologous at the proviral core, or too divergent for the chain. Needs sequence-level examination.
- **1 locus (RV15-0342, ERV-9): absence supported at coordinate level.** Gorilla flank gap collapsed to 3,600 bp and the internal anchor is unmapped in gorilla: consistent with a genuine empty site (or a clean deletion) in gorilla. This is the only one of the 29 whose non-nested pattern currently survives.
- **5 loci: unresolved.** One or both gorilla flank anchors fail to map (0059, 0168, 0441, 0544 fully; 0348 and 0591 have internal anchors mapped in gorilla despite flank failure, suggesting presence with chain breaks at the flanks).

## The orangutan-absent locus (RV15-0805, pattern 11101)
Orangutan flank gap is element-length (10,975 bp), so its 2012 orangutan absence is likewise doubtful at coordinate level; the internal-anchor test for orangutan is queued with the sequence-level pass.

## Chimpanzee and orangutan flank geometry (context)
Chimpanzee gaps are element-length at 28 of 30 loci (2 unmapped), orangutan at 25 (5 unmapped), as expected where the source called presence. The flank method behaves sanely where presence is not in dispute.

## Programme implications, stated plainly
1. The pilot comparison's event accounting was computed on the source study's presence calls. For gorilla, most of those calls in the discriminating subset were assembly-era artifacts. Corrected to current assemblies, at most 1 of the 30 priority patterns is currently verified non-nested, with 6 to 7 unresolved. Any burden table built on legacy presence calls, ours included, is not scoreable evidence; the pilot-comparison.md file now carries an addendum saying so.
2. The direction of the correction favors the single-gain (C0-style) reading of these loci: patterns that looked like losses or coincidences mostly become ordinary nested presences. We record that without trimming; it is what the re-extraction shows at this level.
3. Coordinate-level presence is not orthology proof. The 22 corrected loci still require the sequence-level pass (boundaries, TSD, LTR divergence, shared derived marks) before they can be scored for any model, and RV15-0342's empty site requires the gorilla junction sequence to distinguish a true pre-integration allele from a precise deletion, which the models price differently.
4. The benchmark design's confidence grading and its refusal to score legacy-assembly calls are vindicated by this pass and are now binding precedent for the full extraction: no locus enters headline scoring on a pre-2020 assembly call.

## Next
Sequence-level pass on the priority set: gorilla interval sequences for the 22 corrected loci plus 0130 and 0342 (junction sequence first), LTR-pair extraction and divergence, shared-mark alignment across human, chimpanzee, gorilla and orangutan; resolution attempts for the 6 flank-unmapped loci using Compara alignments where chains break.

Human-Curated, AI-Enabled (HCAE)
