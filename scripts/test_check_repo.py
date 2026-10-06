import tempfile
import unittest
from pathlib import Path

import check_repo


class Fixture(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.root = Path(self._tmp.name)
        (self.root / "work-packages").mkdir()
        self.wp("001", "alpha", "Executed")
        self.wp("002", "beta", "Active")
        self.index([("001", "alpha", "Executed"), ("002", "beta", "Active")])

    def write(self, rel, text):
        p = self.root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")

    def wp(self, num, slug, status, body=None):
        line = body if body is not None else f"**Status:** {status}\n"
        self.write(f"work-packages/WP-{num}-{slug}.md", f"# WP-{num}\n\n{line}")

    def index(self, rows):
        lines = ["# WPs", "", "| ID | Title | Status |", "|---|---|---|"]
        for num, slug, status in rows:
            lines.append(f"| [WP-{num}](WP-{num}-{slug}.md) | t | {status} |")
        self.write("work-packages/README.md", "\n".join(lines) + "\n")

    def violations(self):
        return check_repo.run_checks(self.root)

    def assertViolation(self, text):
        v = self.violations()
        self.assertTrue(any(text in x for x in v), v)


class CheckRepoTests(Fixture):
    def test_clean_fixture_passes(self):
        self.assertEqual(self.violations(), [])

    def test_status_qualifier_allowed(self):
        self.wp("002", "beta", "Active — investigating")
        self.assertEqual(self.violations(), [])

    def test_duplicate_wp_number(self):
        self.wp("001", "other", "Executed")
        self.assertViolation("duplicate WP number WP-001")

    def test_bad_status_word(self):
        self.wp("002", "beta", "In progress")
        self.assertViolation("status 'In' not in")

    def test_missing_status(self):
        self.wp("002", "beta", "", body="no status here\n")
        self.assertViolation("missing '**Status:")

    def test_wp_missing_from_index(self):
        self.wp("003", "gamma", "Proposed")
        self.assertViolation("no index row for WP-003-gamma.md")

    def test_index_row_points_to_missing_file(self):
        self.index([("001", "alpha", "Executed"), ("002", "beta", "Active"),
                    ("009", "ghost", "Closed")])
        self.assertViolation("links to missing file 'WP-009-ghost.md'")

    def test_unlinked_index_row(self):
        self.write("work-packages/README.md",
                   "| ID | T | Status |\n|---|---|---|\n| WP-001 | t | Executed |\n"
                   "| [WP-002](WP-002-beta.md) | t | Active |\n")
        self.assertViolation("WP-001 row has no link")

    def test_status_mismatch_index_vs_file(self):
        self.index([("001", "alpha", "Closed"), ("002", "beta", "Active")])
        self.assertViolation("does not match file status 'Executed'")

    def test_orphan_subdir(self):
        (self.root / "work-packages" / "WP-007").mkdir()
        self.assertViolation("WP-007: orphan directory")

    def test_subdir_with_matching_wp_ok(self):
        (self.root / "work-packages" / "WP-001").mkdir()
        self.assertEqual(self.violations(), [])

    def test_broken_relative_link(self):
        self.write("docs/a.md", "see [x](missing.md#frag)\n")
        self.assertViolation("docs/a.md:1: broken link 'missing.md#frag'")

    def test_valid_and_external_links_ok(self):
        self.write("docs/b.md", "[a](../README.md) [w](https://x.org/y) [t](#top)\n")
        self.write("README.md", "# r\n")
        self.assertEqual(self.violations(), [])

    def test_link_in_fenced_code_ignored(self):
        self.write("docs/c.md", "```\n[x](nope.md)\n```\n")
        self.assertEqual(self.violations(), [])

    def test_link_after_fence_still_checked(self):
        self.write("docs/d.md", "```\n[x](nope.md)\n```\n[y](nope2.md)\n")
        self.assertViolation("nope2.md")


if __name__ == "__main__":
    unittest.main()
