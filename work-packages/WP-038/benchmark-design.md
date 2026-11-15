# WP-038 Benchmark Design (Slice 4)

Status: design draft for review. No loci have been selected and no data has been extracted yet. Selection begins only after this design and the model formalization are reviewed.

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

Orthology rule: a cross-taxon match requires both flanks and TSD agreement. Internal homology alone never establishes a shared locus.

## Training and held-out protocol
- Loci are assigned to training or held-out by stratified random split (strata: locus class, ERV family, confidence grade) with the split seed and assignment list committed to the repository before any model fitting.
- Target split: 60 percent training, 40 percent held-out. Minimum viable benchmark: 50 loci in class 1 across both sets; if accession-level data cannot support 50 grade A/B loci, the benchmark reports the smaller set and the comparison is labelled preliminary.
- No parameter of any model, including the D3 targeting distribution, may be estimated from held-out loci. The D3 targeting distribution is estimated from experimental integration datasets only.
- Unblinding rule: held-out scoring runs once per preregistered model version. Any post-unblinding modification creates a new model version requiring a fresh held-out evaluation on newly reserved loci, or the result is reported as training-set performance only.

## Data sources and manifest
Candidate sources, to be validated at extraction: published comparative ERV catalogues with accession-level locus tables (beginning with the validated register entries), genome-browser ERV annotations (RepeatMasker-based) used only as discovery leads, and author-supplied supplementary tables preferred over scraped summaries. The '205' and '336' counts circulating in secondary debate material are not data and enter only as claims to be traced to a primary table or discarded.

The data manifest records, per locus: source publication or accession, assembly build, extraction date, script commit, and any filtering applied. The manifest is part of the deliverable; a locus without manifest provenance is excluded.

## Scoring outputs
Per the formalization: per-locus joint-pattern scores or qualitative discriminators, auxiliary burden table per model, held-out predictive comparison as the headline, posterior predictive checks for the fitted event counts, and a negative-results register (loci no model explains, loci excluded and why).

## Stop conditions (carried from the test plan)
No parity claim without held-out performance. No independent-explanation claim for any D model if its fit requires fabricated event traces. No conflation of the ancestry question with the separate innovation-sufficiency question. If grade A/B locus yield is too low for quantitative scoring, the programme reports qualitative discriminators and marks the quantitative gate unmet rather than lowering the standard.

Human-Curated, AI-Enabled (HCAE)
