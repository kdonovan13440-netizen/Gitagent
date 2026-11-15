import tempfile
import unittest
from pathlib import Path

import gitagent


class GitagentTests(unittest.TestCase):
    def test_organize_previews_then_applies_without_overwrite(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "report.pdf").write_text("one")
            preview = gitagent.organize(root)
            self.assertEqual(len(preview), 1)
            self.assertTrue((root / "report.pdf").exists())
            gitagent.organize(root, apply=True)
            self.assertEqual((root / "Documents" / "report.pdf").read_text(), "one")

    def test_cleanup_only_reports_candidates(self):
        with tempfile.TemporaryDirectory() as tmp:
            file = Path(tmp) / "cache.tmp"
            file.write_text("keep")
            self.assertEqual(gitagent.cleanup_report(Path(tmp)), [file])
            self.assertTrue(file.exists())

    def test_calendar_requires_timezone_and_valid_order(self):
        with self.assertRaises(ValueError):
            gitagent.make_event("Test", "2026-06-05T14:00:00", "2026-06-05T15:00:00")
        with self.assertRaises(ValueError):
            gitagent.make_event("Test", "2026-06-05T15:00:00+00:00", "2026-06-05T14:00:00+00:00")

    def test_calendar_escapes_text(self):
        event = gitagent.make_event("A, B", "2026-06-05T14:00:00+00:00", "2026-06-05T15:00:00+00:00")
        self.assertIn("SUMMARY:A\\, B", event)


if __name__ == "__main__":
    unittest.main()
