# DFM U-Pb research baseline: infrastructure-only integration candidate

**Status:** synthetic verification and provenance/admission tooling; **no observational data admitted** and **no empirical PEP demonstrated**.

## Included

- Hypothesis and validation protocol, reference register, observational source and acquisition decisions.
- Closed-system synthetic forward/inverse benchmark and covariance-aware fitting.
- Strict admission audit (`audit_cohort.py`) requiring measured Wetherill ratios, positive-definite covariance, confirmed radiogenic corrections, and traceable source references.
- Immutable original-data SHA-256 verifier (`source_provenance.py`).
- Original-file inventory (`acquisition_inventory.py`), which does **not** treat locally supplied files or matching checksums as independent source authentication.
- Automated tests in `tests/`.

## Verification

From repository root: `python -m pytest -q`.

## Data acquisition gate

The official USGS Manzano release DOI is `10.5066/P9U0P2ZY`. Its three original CSV names are listed in `acquisition_inventory.py`. Acquire them from the official DOI-linked data release in a network-enabled environment; record URL, UTC retrieval time, license, and source bytes. Run `python research/upb-validation/acquisition_inventory.py /path/to/originals`, then create a source provenance manifest and verify with `source_provenance.py`. Review the original data dictionary before any column mapping. Never substitute fabricated isotope ratios, inferred correlation, or publication ages for missing measurements.

Sierra Nevada DOI `10.5066/P13LKC5C` is a candidate **independent geological holdout**, pending review of its original data and uncertainty structure.

## Limitations

- Synthetic tests establish code behavior, not historical inference.
- No common-Pb correction, disequilibrium or Pb-loss process model is implemented.
- A freely tuned initial daughter ratio for each sample is disallowed; shared parameters must be independently constrained and frozen before held-out evaluation.
- The local development repository was created separately from the canonical DFM `master`; integration must apply this directory and tests onto a fresh branch based on `master`, review collisions, and run canonical CI.

## Merge handoff

**Ready for an infrastructure-only integration review**, provided the scope explicitly excludes empirical validation. Authorized execution lane must stage the package onto canonical `master` ancestry, create PR, verify checks and diff, merge and delete only the new integration branch, and report receipt. Existing unrelated branches must remain untouched.
