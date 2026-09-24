# WP-004: Longmire Template Normalization

**Status:** In progress  
**Parent:** Designed Functional Maturity (DFM) Research Programme  
**Target:** Repository normalization, canonical architecture, and content promotion

## 1. Purpose

Normalize the DFM repository to the Longmire repository pattern without erasing provenance or treating historical work packages as canonical doctrine.

DFM has matured from a paper-development workspace into a research programme. The repository structure must make that explicit.

## 2. Governing architecture

Separate governance, canonical foundations, canonical framework, research controls, domain investigations, historical work packages, papers/publications, references, and media.

Work packages remain execution and provenance records. Mature conclusions are promoted into canonical surfaces and referenced from the originating work package.

## 3. Canonical boundary

This repository is canonical for DFM as methodology and research programme. BWM remains the parent integration context. DFM shall not silently expand into a duplicate BWM repository.

## 4. Normalization principles

1. Preserve existing artifacts unless supersession is explicit.
2. Do not rewrite historical work packages merely to make them look current.
3. Promote stable conclusions into canonical documents.
4. Distinguish hard-core commitments from revisable protective-belt hypotheses.
5. Preserve unresolved accounting as unresolved.
6. Apply no-smuggling, no-free-lunch, concordance, provenance, and symmetric burden rules.
7. Do not impose a higher anti-auxiliary standard on DFM than on competing programmes.
8. Track canonical ownership to prevent proposition drift.

## 5. Target surfaces

```text
/
├── README.md
├── AGENTS.md
├── 00-governance/
├── 01-foundations/
├── 02-framework/
├── 03-research-programme/
├── 04-domains/
├── work-packages/
├── drafts/
├── published-papers/
├── references/
├── image-assets/
└── video-assets/
```

Empty directory shells are not required.

## 6. Promotion map

| Existing source | Destination | Treatment |
|---|---|---|
| `drafts/designed-functional-maturity.md` | foundations/framework | Extract stable commitments; paper remains a paper |
| WP-002 | framework/radiometrics | Promote mature inferential rules; retain provenance |
| WP-002 formal framework | framework | Primary promotion source |
| WP-003 | cosmology | Remains active hypothesis |
| publication/media READMEs | existing directories | Retain and cross-link |

## 7. Tranches

A. Repository shell and canonical navigation.  
B. Canonical promotion from WP-002.  
C. Research registers and terminology control.  
D. Domain normalization.  
E. Reconciliation of indexes, status fields, links, and terminology drift.

## 8. Acceptance criteria

A new reader can determine what DFM claims and does not claim, its hard core and revisable hypotheses, its inferential rules, active empirical research, revision conditions, BWM relationship, and authoritative content locations.

Human-Curated, AI-Enabled (HCAE)
