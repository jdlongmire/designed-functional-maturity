# WP-024: DFM Media Library and Visual Asset Publication Architecture

**Status:** Executed / infrastructure established
**Type:** Publication infrastructure
**Depends on:** WP-016, WP-017, WP-020, WP-023

## Objective
Create a durable public Media Library for approved DFM graphics and define the asset lifecycle from development through canonical publication.

## Publication workflow

```text
Develop -> Review -> Approve -> Canonize -> Store Master -> Create Thumbnail -> Index -> Contextual Placement
```

A generated image is not canonical until explicitly approved.

## Asset architecture

- `image-assets/` remains the canonical source/master asset area.
- `docs/media/` contains the public Media Library page and web-ready publication derivatives.
- `docs/media/full/` is reserved for full-size approved public graphics.
- `docs/media/thumbs/` is reserved for thumbnail derivatives.

Recommended stable filename convention:

```text
dfm-<topic-slug>-v<major>.<ext>
dfm-<topic-slug>-v<major>-thumb.<ext>
```

Once a graphic is canonical and publicly referenced, avoid changing its URL casually. Material conceptual revisions should increment the major version.

## Library card metadata
Each indexed visual should expose:
- title;
- thumbnail;
- one-line explanatory purpose;
- category;
- status;
- link to full-size graphic;
- optional link to explanatory context.

Statuses:
- **Canonical**: approved representation of a DFM concept.
- **Supporting**: approved explanatory visual that is not the canonical representation.
- Draft/development graphics are not published in the public library.

Initial categories:
- Core Concepts
- Genesis 1
- Epistemology & Provenance
- Technical Framework
- Evidence & Severe Tests

## Interaction
- Thumbnail selection opens the full-resolution graphic.
- The visual title or context link may lead to explanatory material when available.
- The library uses a responsive grid suitable for desktop and mobile.
- Filtering is intentionally deferred until collection size justifies it.

## Visual governance
WP-023 remains authoritative for infographic design and approval. The preferred public/social format is a square 2 x 2 grid unless the explanatory topology warrants an exception.

## Initial state
The Media Library launches as an intentional empty-state catalogue. Visual 1, **Deployment vs. Operation**, is planned as the first canonical entry after individual review and approval.

## Success criterion
The public library provides a stable, low-friction way to scan DFM visual assets as thumbnails and open approved graphics at full size without making the homepage carry the full visual corpus.
