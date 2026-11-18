# WP-038 Slice 5 Re-extraction: Sequence-Level Pass on the Priority Loci

Date: 2026-11-15. Inputs: human GRCh38 and gorilla gorGor6 interval sequences for the 30 priority loci (UCSC genome API; see the methods note in section 4). Data files: data/sequence-verdicts.csv, data/ltr-divergence.csv, data/reextraction-results.csv.

## 1. Gorilla verdicts at sequence level
Windowed 31-mer homology profiles of each human interval against its gorilla counterpart (flank windows score 0.44 to 0.72 at these loci, the expected human-gorilla range):

- **23 loci: full homologous provirus in gorilla.** Internal-region homology 0.44 to 0.64, indistinguishable in kind from the flanks, across the whole interval. Includes RV15-0130 (one divergent internal segment) and RV15-0405 (scaffold locus), both unresolved after the coordinate pass and resolved as present here.
- **1 locus: solo LTR in gorilla** (RV15-0342; section 2).
- **6 loci: unresolved.** Four (0059, 0168, 0348, 0591) have only one mappable flank anchor, so the fetched gorilla piece covers one flank only; two (0441, 0544) have no gorilla chain span. None of the six shows any positive evidence of absence.

**Net result: none of the 30 priority loci is a verified gorilla empty site.** The class of 'non-nested patterns requiring a second event' in the source data was, for gorilla, an artifact of the 2012 assembly plus one recombinational deletion misread as absence (section 2).

## 2. RV15-0342: a solo LTR, not an empty site
The one locus whose gorilla absence survived the coordinate pass (collapsed 3,600 bp flank gap) resolves at sequence level as a solo LTR:
- Human carries a direct-repeat LTR pair at offset 7,387 bp (52 independent 31-mers at a single consistent offset; copies at human interval positions about 3,595 and 10,981), giving a provirus of about 7.9 kb.
- The gorilla junction segment (700 bp spanning the join) matches the human 5' LTR zone (169 of 670 31-mers) and the human 3' LTR zone (187 of 670), and matches the human internal region **0 of 670**. One LTR copy sits between the gorilla flanks; the internal region is gone.
- Reading: the provirus was present in the gorilla lineage and its internal region was deleted by LTR-LTR recombination, the standard solo-LTR formation mechanism. Under single-gain accounting this locus costs one integration (shared, at the human-chimp-gorilla ancestor or deeper) plus one documented-mechanism deletion in gorilla. Under any never-present-in-gorilla reading, the solo LTR itself requires an integration in the gorilla lineage plus the same deletion, so the locus cannot be used as evidence that gorilla never had the element. It is evidence of presence followed by deletion.

## 3. LTR pairs and divergence (first estimates)
A direct-repeat detector (31-mers recurring at one consistent offset) found LTR pairs in the human interval at 26 of 30 loci and in gorilla at 22 of the 24 full-length gorilla intervals. At most loci the human and gorilla offsets agree within a few dozen bp (for example 4,184/4,184; 7,329/7,313; 8,327/8,333; 7,984/7,986), the same provirus architecture at the same spacing in both species. Pairwise identity between the 5' and 3' LTR copies, computed base-by-base over the detected span, ranges from about 0.60 to 1.00 in human and 0.42 to 1.00 in gorilla (full table in data/ltr-divergence.csv). Method limits, stated for the record: detected spans are partial (76 to 939 bp of LTRs that run longer), so identities are estimates over the detected region only; two loci (0130, 0490) show human-gorilla offset disagreement and are flagged for alignment-based re-measurement; the lowest identities (for example gorilla 0.42 at RV15-0318) mark degraded copies or imperfect span detection and are not to be quoted as divergence measurements without the alignment pass. These estimates size the LTR-divergence dataset that the D4 severe test and any clock-based argument will need; they are not yet that dataset.

## 4. Methods note: a retrieval error caught and corrected
Gorilla intervals were first fetched from the Ensembl REST API using UCSC gorGor6 coordinates. Ensembl's gorilla assembly coordinates are not UCSC gorGor6 coordinates, and the returned sequences (right length, wrong DNA) produced zero 31-mer sharing even in flanks. The error was caught because flank homology is a built-in control: it cannot be zero at genuinely orthologous loci. All gorilla sequences were refetched from the UCSC genome API on gorGor6 coordinates, after which flank profiles fell in the expected range at every locus. Lesson recorded for the full extraction: sequence retrieval must always run a flank-homology control before any interval is analyzed, and assembly provenance (UCSC vs Ensembl coordinate systems) must be logged per sequence, as the manifest now requires.

## 5. Consequences for scoring
- The training-set pattern census must be rebuilt from re-extracted verdicts before any burden comparison is rerun; the pilot table remains superseded for appraisal (see its addendum).
- The gorilla 'losses' that the source data implied for HERV-K(HML2) largely evaporate; what remains is one documented recombinational deletion (0342) and six unresolved loci. Re-extracting the remaining training loci, and then the held-out set under the unblinding rule only at scoring time, is the path to a scoreable matrix.
- Nothing in this pass bears directly on D1 or D2 (their claims sit at the creation boundary, below these divergences) or on D4's timeline test, which awaits the alignment-grade LTR divergence dataset. It bears on C0 versus coincidence readings of shared loci, and it moves that reading toward C0 on the loci examined.

Human-Curated, AI-Enabled (HCAE)
