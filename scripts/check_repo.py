#!/usr/bin/env python3
"""Repository checks: work-package index, status vocabulary, relative links.

Run from the repository root: python scripts/check_repo.py
"""
import re
import sys
from pathlib import Path

STATUSES = ("Proposed", "Active", "Executed", "Deferred", "Superseded", "Closed")
WP_FILE = re.compile(r"^WP-(\d{3})-[^/]+\.md$")
WP_DIR = re.compile(r"^WP-(\d{3})$")
STATUS_LINE = re.compile(r"^\*\*Status:\*\*\s+(\S+)")
INDEX_ID = re.compile(r"^\[?(WP-\d{3})\]?(?:\(([^)]*)\))?$")
LINK = re.compile(r"\[[^\]]*\]\(<?([^)\s>]+)>?(?:\s+\"[^\"]*\")?\)")
FENCE = re.compile(r"^\s*(`{3,}|~{3,})")
CODE_SPAN = re.compile(r"`[^`\n]*`")


def wp_files(wp_dir):
    return sorted(p for p in wp_dir.iterdir() if p.is_file() and WP_FILE.match(p.name))


def file_status(path):
    """Return the first word of the Status line, or None."""
    for line in path.read_text(encoding="utf-8").splitlines():
        m = STATUS_LINE.match(line)
        if m:
            return m.group(1)
    return None


def check_numbers_unique(files):
    seen = {}
    for p in files:
        seen.setdefault(WP_FILE.match(p.name).group(1), []).append(p)
    return [f"{p.as_posix()}: duplicate WP number WP-{n}"
            for n, ps in seen.items() if len(ps) > 1 for p in ps]


def check_subdirs(wp_dir, files):
    nums = {WP_FILE.match(p.name).group(1) for p in files}
    out = []
    for d in sorted(p for p in wp_dir.iterdir() if p.is_dir()):
        m = WP_DIR.match(d.name)
        if m and m.group(1) not in nums:
            out.append(f"{d.as_posix()}: orphan directory, no WP-{m.group(1)}-*.md file")
    return out


def check_statuses(files):
    out = []
    for p in files:
        word = file_status(p)
        if word is None:
            out.append(f"{p.as_posix()}: missing '**Status:** <word>' line")
        elif word not in STATUSES:
            out.append(f"{p.as_posix()}: status '{word}' not in {', '.join(STATUSES)}")
    return out


def index_rows(readme):
    """Yield (id, link_target_or_None, last_cell) for each WP table row."""
    for line in readme.read_text(encoding="utf-8").splitlines():
        if not line.lstrip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        m = INDEX_ID.match(cells[0])
        if m:
            yield m.group(1), m.group(2), cells[-1]


def check_index(wp_dir, files):
    readme = wp_dir / "README.md"
    if not readme.is_file():
        return [f"{readme.as_posix()}: missing work-package index"]
    out, indexed = [], set()
    by_name = {p.name: p for p in files}
    for wp_id, target, last in index_rows(readme):
        where = f"{readme.as_posix()}: {wp_id}"
        if not target:
            out.append(f"{where} row has no link to its file")
            continue
        path = by_name.get(target)
        if path is None:
            out.append(f"{where} row links to missing file '{target}'")
            continue
        indexed.add(path.name)
        word = file_status(path)
        row_word = re.match(r"\W*(\w+)", last)
        if word and (not row_word or row_word.group(1) != word):
            out.append(f"{where} status '{last}' does not match file status '{word}'")
    for p in files:
        if p.name not in indexed:
            out.append(f"{readme.as_posix()}: no index row for {p.name}")
    return out


def check_links(root):
    out = []
    for md in sorted(root.rglob("*.md")):
        if ".git" in md.relative_to(root).parts:
            continue
        in_fence = None
        for n, line in enumerate(md.read_text(encoding="utf-8").splitlines(), 1):
            f = FENCE.match(line)
            if f:
                marker = f.group(1)[0]
                in_fence = None if in_fence == marker else (in_fence or marker)
                continue
            if in_fence:
                continue
            for target in LINK.findall(CODE_SPAN.sub("", line)):
                if re.match(r"^(https?:|mailto:|#)", target):
                    continue
                path = target.split("#", 1)[0]
                if not path:
                    continue
                base = root if path.startswith("/") else md.parent
                if not (base / path.lstrip("/")).exists():
                    out.append(f"{md.relative_to(root).as_posix()}:{n}: broken link '{target}'")
    return out


def run_checks(root):
    root = Path(root)
    wp_dir = root / "work-packages"
    out = []
    if wp_dir.is_dir():
        files = wp_files(wp_dir)
        out += check_numbers_unique(files)
        out += check_subdirs(wp_dir, files)
        out += check_statuses(files)
        out += check_index(wp_dir, files)
    out += check_links(root)
    return out


def main():
    violations = run_checks(Path("."))
    for v in violations:
        print(v)
    print(f"{len(violations)} violation(s)" if violations else "OK: no violations")
    return 1 if violations else 0


if __name__ == "__main__":
    sys.exit(main())
