# WP-038 Grandi HERV-W Category Reconciliation

Date: 2026-11-15. Source: Grandi et al. 2018, Additional file 1 (Tables S1 to S4), parsed directly.

## The discrepancy as first filed
The pilot manifest recorded 214 human HERV-W rows in Table S1 with a chimpanzee coordinate-present count of 207, against the paper's headline 211 loci and the widely circulated figure of 205 shared with chimpanzee. The manifest flagged the mismatch as definitional and open. Direct re-parsing resolves it completely; the first parse had three defects.

## Defects in the first parse
1. **A footnote counted as a locus.** Table S1 ends with a long footnote row whose first cell is text. It was ingested as a 214th locus with all-absent flags.
2. **Chromosome Y rows miscounted.** Table S1 lists 213 locus rows, including two chromosome Y loci (Yp11.2, Yq11.222) whose non-human cells carry '-' (not applicable; the authors state in the footnote and main text that these two loci were excluded from the analysis). The first parse treated '-' as coordinate-present, adding two false presences for every species.
3. **Column mislabel.** Table S1's first column is the cytogenetic band, not the human coordinate. Human coordinates (GRCh37/hg19) are given in the companion paper, Grandi et al. 2016, as the Table S1 footnote states. The matrix's first column is now correctly named cytogenetic_band.

## Reconciled counts
- Table S1 locus rows: 213. Excluding the 2 chromosome Y loci: **211**, the paper's denominator.
- Coordinate-present at the orthologous position, of 211: chimpanzee **205**, gorilla 206, orangutan 205, gibbon 190, rhesus 129.
- The chimpanzee figure of **205 of 211 is reproduced exactly** from the supplement. The '205' attribution in claims-verification.md stands verified at source.
- Table S2 lists 19 human solitary-LTR loci with orthologous-region coordinates in the other species (a separate category, not part of the 211). Table S3 lists 39 HERV-W-like element rows (the paper's non-canonical category). Table S4 lists ERV-W loci found in non-human genomes without a human ortholog, by species.

## Remaining caveat
Within Table S1, proviral completeness per species (full provirus vs lacking one or both LTRs) is encoded in the workbook's character formatting (bold and italics, per the table footnotes), which a values-only parse does not capture. The paper's Table 2 category counts (for example 138 canonical chimpanzee orthologs) are completeness-graded from the non-human side and cannot be reproduced from presence values alone. Category-level quotation beyond presence/absence requires a formatting-aware parse or the 2016 companion data. Presence-level numbers above are safe to quote as stated.

## Corrections propagated
- data/grandi-herw-matrix.csv rebuilt: 211 rows, band column corrected, Y loci and footnote removed.
- data/data-manifest.md Source 2 section rewritten with the reconciled counts and the GRCh37/hg19 build correction.
- pilot-comparison.md Grandi row recomputed on the corrected matrix: 211 loci, single-gain 211 + 17 = 228 events, independent-gain 237, 15 loci needing a second event, 121 loci present in all six taxa. (First-filed values 214/231/240/123 were computed on the defective parse and are superseded.)

Human-Curated, AI-Enabled (HCAE)
