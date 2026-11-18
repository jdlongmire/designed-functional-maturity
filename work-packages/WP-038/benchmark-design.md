# WP-038 Benchmark Design (Slice 4)

Status: reviewed (thinx-gpt G1, 2026-11-15; disposition in g1-disposition.md). Superseded in part by the G1 disposition and scoring-protocol.md v1, which govern where they differ. Chronology, recorded for preregistration honesty: the design and formalization were drafted 2026-11-15; pilot extraction on v1 training assignments followed the same day under JD's go-ahead, before the G1 review returned; the group-aware split v2 and this scoring freeze postdate that extraction. Pilot extraction results are development results, not prospective predictions. Canonical datasets: training side, data/training206-verdicts-final.csv (206 loci, 144 resolved, 62 declared unresolved); held-out side, the 52 clean loci of data/pilot-split-v2.csv, unextracted at freeze. Earlier census snapshots are retained as historical evidence and are not scored.

## Purpose
Construct a reproducible orthologous-locus evidence matrix on which C0, D1, D2 and D3 can be compared under the scoring rules of the model formalization, with a held-out set reserved before any fitting.

## Taxon and assembly panel
- Human: GRCh38 (primary), T2T-CHM13 (cross-check for repeat-rich loci).
- Chimpanzee, gorilla, orangutan: current reference assemblies at design freeze; exact accessions recorded in the data manifest at extraction time, not from memory.
- Outgroup: rhesus macaque (Old World monkey) as the primary outgroup; a second outgroup may be added if orthology calls require it.
- Every locus carries an assembly-confidence grade per taxon: A (both flanks uniquely placed, gap-free), B (placed, minor uncertainty), C (ambiguous or gapped; locus excluded from headline scoring, retained in an appendix set).

## Locus classes
1. **Shared-orthologous candidate loci:** provirus present at the orthologous site in at least human and chimpanzee, with gorilla/orangutan/outgroup presence-absence recorded. Primary discriminator class.
2. **Lineage-specific loci:** present in exactly one taxon with an empty orthologous site confirmed in at least one other taxon (the PTERV1 pattern). Calibrates independent-integration base rates for D3 and post-boundary infection counts for D1.
3. **Solo-LTR loci:** recorded separately; solo LTRs evidence a past full provirus plus recombination deletion, and are scored as event traces with reduced information, never pooled with full loci.
4. **Polymorphic loci:** insertion polymorphisms within a species, where population data exists. Reserved for ILS and recent-activity analysis.

## Per-locus record (evidence matrix schema)
Locus ID; taxon panel presence/absence with confidence grade; left and right flank coordinates per assembly; TSD sequence; orientation; 5-prime and 3-prime LTR sequences and pairwise divergence; internal shared substitutions, deletions and disabling mutations with positions; functional annotation; source accession and extraction script version for every field.

Orthology rule (graded, per G1 disposition F4): Grade A requires two-flank synteny with boundary and TSD evidence where recoverable. Grade B requires two-flank synteny plus internal homology where the TSD is not recoverable. Internal homology alone never establishes a shared locus. Absence requires a verified empty-site sequence at the orthologous position; a chain-lift or mapping failure is recorded as missing, never as absence. Scoring runs sensitivity analyses under a strict rule (Grade A only, TSD required) and the graded rule (Grades A and B).

## Training and held-out protocol
- Superseded by the group-aware split v2 (G1 disposition F1): the ERV family is the clustering unit and whole families are assigned to one side only, so family, segment and shared-history dependence cannot leak across the split. Assignments, seed and rule: data/pilot-split-v2.csv and g1-disposition.md. The v1 stratified random split is retained in data/pilot-split.csv as a historical record.
- The held-out side carries a quarantine class: loci examined during v1 training extraction that fall in held-out families are excluded from all scoring. The clean held-out set is 52 never-examined loci.
- Minimum viable benchmark: 50 scored loci in class 1; if extraction yield falls below that, the comparison is labelled preliminary, per the stop conditions.
- No parameter of any model, including the D3 targeting distribution, may be estimated from held-out loci. The D3 targeting distribution is estimated from experimental integration datasets only.
- Unblinding rule: held-out scoring runs once per preregistered model version, after JD authorizes the scoring phase. Any post-unblinding modification creates a new model version requiring a genuinely new held-out cohort, or the result is reported as training-set performance only.
- The full frozen decision procedure is scoring-protocol.md v1.

## Data sources and manifest
Candidate sources, to be validated at extraction: published comparative ERV catalogues with accession-level locus tables (beginning with the validated register entries), genome-browser ERV annotations (RepeatMasker-based) used only as discovery leads, and author-supplied supplementary tables preferred over scraped summaries. The '205' and '336' counts circulating in secondary debate material are not data and enter only as claims to be traced to a primary table or discarded.

The data manifest records, per locus: source publication or accession, assembly build, extraction date, script commit, and any filtering applied. The manifest is part of the deliverable; a locus without manifest provenance is excluded.

## Scoring outputs
Per the formalization: per-locus joint-pattern scores or qualitative discriminators, auxiliary burden table per model, held-out predictive comparison as the headline, posterior predictive checks for the fitted event counts, and a negative-results register (loci no model explains, loci excluded and why).

## Stop conditions (carried from the test plan)
No parity claim without held-out performance. No independent-explanation claim for any D model if its fit requires fabricated event traces. No conflation of the ancestry question with the separate innovation-sufficiency question. If grade A/B locus yield is too low for quantitative scoring, the programme reports qualitative discriminators and marks the quantitative gate unmet rather than lowering the standard.

Human-Curated, AI-Enabled (HCAE)
