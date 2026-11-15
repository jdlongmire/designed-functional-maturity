# WP-038 Slice 5 Re-extraction Protocol: Priority Loci

Date: 2026-11-15. Input: data/priority-loci.csv (30 loci). Status: protocol and priority set filed; sequence-level execution is the next work block.

## Why these 30
From the pilot comparison: 30 of the 206 training loci have presence patterns that cost a second event under any accounting. Twenty-nine show pattern 11010 across (human, chimpanzee, gorilla, orangutan, macaque): present in human, chimpanzee and orangutan, absent in gorilla. One (RV15-0805) shows 11101: present everywhere except orangutan. Under a single-gain reading each requires a lineage loss (gorilla, resp. orangutan); under an independent-gain reading each requires coincident integrations. They are the cheapest place to buy discriminating evidence, and HERV-K(HML2) dominates the list (21 of 30), consistent with that family's recent activity.

## Per-locus target record
For each priority locus, extract against current assemblies (human GRCh38 with T2T-CHM13 cross-check; current chimpanzee, gorilla, orangutan and rhesus assemblies):
1. Orthologous-region sequence in all five taxa, located from the RV15 excerpt coordinates by assembly mapping (human GRCh37 to GRCh38) and whole-genome alignment chains, never by coordinate assumption.
2. Presence verdict per taxon at the benchmark standard: both flanks alignable, and the element classified as full provirus, truncated, solo LTR, or absent with an empty-site sequence (pre-integration allele) where the assembly supports it. The gorilla empty site is the single most valuable sequence in this set: a clean pre-integration allele in gorilla converts 'absent' from an alignment gap into evidence.
3. Where the element is present: exact boundaries, TSD sequence and length, 5' and 3' LTR sequences and their pairwise divergence, and the internal-region alignment across taxa for shared derived substitutions and shared disabling mutations, recorded per the evidence-matrix schema.
4. Assembly-confidence grade per taxon per the benchmark design (A/B/C), with C-grade taxa excluded from that locus's headline pattern.

## Route
Ensembl REST (GRCh37 archive for source coordinates; current REST for mapping and Compara genomic alignments) for region location and sequence retrieval; local alignment (pairwise flank alignment) for boundary and empty-site verification. Every retrieved region is logged with assembly name, coordinates and retrieval date in the data manifest before use. No locus is scored from the 2012 excerpts; they serve only as locators.

## Acceptance criteria for the priority batch
- At least 25 of 30 loci with grade A/B presence verdicts in all five taxa.
- Every gorilla absence in the 11010 set resolved to one of: empty-site sequence obtained, element found (pattern corrected), or grade C with the assembly gap identified.
- LTR divergence and shared-mark fields populated for every locus with two or more full/provirus-grade copies.
- Results written as a version increment of the evidence matrix, with the training/held-out split untouched: these 30 are all training loci, and no held-out locus is examined in this batch.

Human-Curated, AI-Enabled (HCAE)
