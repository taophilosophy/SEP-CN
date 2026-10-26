# -*- coding: utf-8 -*-
"""check_doc_size 阈值边界与扫描逻辑单测。"""
import os
import sys
import tempfile
import unittest
from pathlib import Path

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, REPO)

from tools.check_doc_size import EXEMPT, LIMIT_BYTES, LIMIT_LINES, over_limit, scan  # noqa: E402


class OverLimitTest(unittest.TestCase):
    def test_under_thresholds_pass(self):
        self.assertFalse(over_limit(LIMIT_LINES, LIMIT_BYTES))

    def test_lines_boundary_inclusive(self):
        self.assertFalse(over_limit(LIMIT_LINES, 0))
        self.assertTrue(over_limit(LIMIT_LINES + 1, 0))

    def test_bytes_boundary_inclusive(self):
        self.assertFalse(over_limit(0, LIMIT_BYTES))
        self.assertTrue(over_limit(0, LIMIT_BYTES + 1))


class ScanTest(unittest.TestCase):
    def test_scan_counts_lines_and_bytes(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / "a.md").write_bytes("一行\n两行\n".encode("utf-8"))
            (root / "rules").mkdir()
            (root / "rules" / "b.md").write_bytes(b"x\n")
            rows = {rel: (lines, size) for rel, lines, size in scan(root)}
            self.assertEqual(rows["a.md"], (2, 14))
            self.assertEqual(rows["rules/b.md"], (1, 2))

    def test_repo_gate_clean(self):
        rows = scan()
        violations = [r for r in rows if r[0] not in EXEMPT and over_limit(r[1], r[2])]
        self.assertEqual(violations, [])


if __name__ == "__main__":
    unittest.main()
