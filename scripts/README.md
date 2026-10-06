# Repository checks

`check_repo.py` is a stdlib-only Python 3 script that enforces the work-package contract and link integrity. Run it from the repository root:

```
python -m unittest discover -s scripts -p "test_*.py"
python scripts/check_repo.py
```

It prints one `path: message` line per violation and exits 1 if any exist.

Enforced:

- Work packages are top-level `work-packages/WP-NNN-<slug>.md` files with unique three-digit numbers.
- Each `work-packages/WP-NNN/` subdirectory corresponds to an existing WP-NNN file.
- Each WP file has a `**Status:** <word>` line, where the word is one of Proposed, Active, Executed, Deferred, Superseded, Closed (an optional qualifier may follow).
- `work-packages/README.md` has one table row per WP file, with the ID as a resolving relative link and a Status cell beginning with the same word as the file.
- Relative markdown links in every `*.md` file resolve to an existing path (external links, `mailto:`, pure anchors, and fenced code blocks are skipped).

The GitHub Actions job `repo-checks` runs both commands on pull requests and pushes to `master`.
