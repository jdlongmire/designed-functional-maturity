# WP-038 Pilot Data Manifest

Extraction date: 2026-11-15. Extractor: programme operator, script-driven (xlrd parse of the published supplement; generation script retained in the working record).

## Source 1 (extracted): Retrovirology 2015 orthologous ERV dataset
- Publication: *Orthologous endogenous retroviruses exhibit directional selection since the chimp-human split*, Retrovirology 2015, DOI 10.1186/s12977-015-0172-6, PMC4477479.
- File used: Additional file 2 (12977_2015_172_MOESM2_ESM.xls), retrieved from the publisher's static content server after the PMC bin link returned a download interstitial. Sheets: data (862 paired loci), description (field definitions), Belshaw et al. 2007 cross-reference.
- Genome builds: Ensembl release 69 (September 2012), as stated in the supplement's description sheet: human GRCh37, chimpanzee CHIMP2.1.4, gorilla gorGor3.1, orangutan PPYG2, rhesus macaque MMUL_1 (build names per Ensembl 69; to be re-confirmed at full extraction).
- Method of the source study: tBLASTn with 771 retroviral pol probes against five primate genomes; paired orthologues by two-stage pairwise alignment of 15 kb excerpts around pol hits; paralogous regions excluded.

## Pilot evidence matrix (pilot-evidence-matrix.csv)
862 paired loci. Per pair: family (BLAST probe assignment), ERV class, both species' chromosome and 15 kb excerpt coordinates, orientation, gag/env HMM detection on both sides, and the study's orthologue presence flags for human, chimpanzee, gorilla, orangutan and macaque. Presence-flag totals across the matrix: human 843, chimpanzee 709, gorilla 502, orangutan 358, macaque 12.

## Preregistered split (pilot-split.csv)
Benchmark pilot set: the 342 human-chimpanzee pairs. Stratified by ERV family, 60/40 training/held-out, random seed 20261115, assignment committed with this manifest before any model fitting: 206 training, 136 held-out. The paper's headline 336 pairs are this set after the authors' alignment-quality exclusions; the pilot retains all 342 and records the difference.

## Limitations (binding on any use of this pilot)
1. Coordinates are 15 kb excerpt windows around pol hits, not proviral boundaries. TSD, exact boundary, LTR-pair and shared-mutation fields of the benchmark schema are NOT populated by this source and require re-extraction against current assemblies (GRCh38/T2T and current ape assemblies) in the full slice 5 pass. No boundary-level claim may be made from the pilot matrix.
2. Assemblies are 2012-era (Ensembl 69). Presence/absence flags inherit those assemblies' gaps; confidence grades per the benchmark design cannot be assigned from this source alone, so all pilot loci carry provisional grade B/C pending re-extraction.
3. The source study selected for full-length, alignable proviruses; the pilot is therefore a class 1 (shared-orthologous candidate) sample biased toward intact elements. It does not sample solo LTRs or degraded loci, and rates estimated from it do not generalize to the full ERV complement.
4. Orthology in the source is alignment-based on excerpts; the benchmark's both-flanks-plus-TSD rule is stricter and will reclassify some pairs at full extraction.

## Source 2 (extracted): Grandi et al. HERV-W dataset
- Publication: Grandi et al., *Identification and characterization of ERV-W sequences in Catarrhini primate genomes*, BMC Evolutionary Biology 2018, DOI 10.1186/s12862-018-1125-1, PMC5775608.
- File used: Additional file 1 (12862_2018_1125_MOESM1_ESM.xlsx), Table S1, retrieved from the publisher's static content server.
- Extracted matrix (grandi-herw-matrix.csv): 214 human HERV-W locus rows with ortholog coordinates or absence calls for chimpanzee, gorilla, orangutan, gibbon and rhesus. Coordinate-present counts: chimpanzee 207, gorilla 208, orangutan 207, gibbon 192, rhesus 131.
- Reconciliation note (open): the paper's categorized summary counts (211 loci after excluding 2 chromosome Y loci; categorized as canonical ortholog, solitary-LTR correspondence, or HERV-W-like element in its Table 2) do not map one-to-one onto a raw coordinate-present count of Table S1 (214 rows, 207 chimpanzee-present). The difference is definitional (category boundaries and the Y loci), not a data error, but the exact category reconciliation, including Tables S2 (solitary-LTR correspondences) and S3 (HERV-W-like elements), is required before HERV-W numbers are quoted at category level. The '205 shared' figure in circulation corresponds to the paper's categorized counting, not to the raw S1 presence count.
- Genome builds: human GRCh38/hg38 and contemporary ape assemblies as reported in the paper (to be re-confirmed field-by-field at full extraction).

Human-Curated, AI-Enabled (HCAE)
