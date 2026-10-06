# WP-016: DFM Public Pages Site

**Status:** Executed — baseline  
**Type:** Public communication / GitHub Pages
**Depends on:** WP-013, WP-014, WP-015

## Objective
Create an accessible public presentation layer for DFM while keeping the repository research corpus canonical.

## Architecture
- Mobile-first static site under `docs/`.
- Accessible landing page with progressive disclosure.
- Accessible track: programme thesis, Genesis phased deployment, functional maturity, pre-seeded-world analogy, retrodiction/provenance, objections.
- Technical track: formalism, hard core, evidential ladder, severe-test posture, current burdens.
- Direct links back to canonical repo artifacts.
- No attempt to hide unresolved burdens.
- GitHub Pages source target: `master:/docs`.

## Public framing
The site leads with the deployment/operation distinction rather than radiometric controversy.

Canonical public sequence:
1. The rules that govern a running system need not be the process by which the system was deployed.
2. Consilience establishes coherence; provenance establishes history.
3. Measurement establishes state. Retrodiction reconstructs trajectory. Provenance warrants history.

## Guardrails
- Scripture remains authoritative over systems-engineering analogies.
- Virtual-world language is explicitly analogy, not simulation ontology.
- Consensus reconstructions are represented as models subject to the same evidential standards, not caricatured.
- DFM burdens are publicly visible.
- Technical claims link back to canonical programme artifacts.

## Deployment
The repository contains a Pages-ready `docs/` tree. GitHub Pages should publish from the `master` branch `/docs` directory.