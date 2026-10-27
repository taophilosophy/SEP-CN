# -*- coding: utf-8 -*-
"""check_doc_size 阈值边界与扫描逻辑单测（含 2026-10-27 规则文本专用阈值）。"""
import os
import sys
import tempfile
import unittest
from pathlib import Path

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, REPO)

from tools.check_doc_size import (  # noqa: E402
    EXEMPT, LIMIT_BYTES, LIMIT_LINES, RULE_LIMIT_BYTES, RULE_LIMIT_LINES,
    limits_for, over_limit, scan,
)


class OverLimitTest(unittest.TestCase):
    def test_under_thresholds_pass(self):
        self.assertFalse(over_limit(LIMIT_LINES, LIMIT_BYTES, (LIMIT_LINES, LIMIT_BYTES)))

    def test_lines_boundary_inclusive(self):
        self.assertFalse(over_limit(LIMIT_LINES, 0, (LIMIT_LINES, LIMIT_BYTES)))
        self.assertTrue(over_limit(LIMIT_LINES + 1, 0, (LIMIT_LINES, LIMIT_BYTES)))

    def test_bytes_boundary_inclusive(self):
        self.assertFalse(over_limit(0, LIMIT_BYTES, (LIMIT_LINES, LIMIT_BYTES)))
        self.assertTrue(over_limit(0, LIMIT_BYTES + 1, (LIMIT_LINES, LIMIT_BYTES)))

    def test_rule_threshold_tighter(self):
        # 约束性规则专用阈值：300 行 / 30KB——通用阈值内但规则阈值外应超限
        limits = (RULE_LIMIT_LINES, RULE_LIMIT_BYTES)
        self.assertTrue(over_limit(RULE_LIMIT_LINES + 1, 0, limits))
        self.assertTrue(over_limit(0, RULE_LIMIT_BYTES + 1, limits))
        self.assertFalse(over_limit(RULE_LIMIT_LINES, RULE_LIMIT_BYTES, limits))

    def test_limits_for_paths(self):
        self.assertEqual(limits_for("rules/05-ci-and-tools.md"),
                         (RULE_LIMIT_LINES, RULE_LIMIT_BYTES))
        self.assertEqual(limits_for("rules/adr/0005-目录重建.md"),
                         (LIMIT_LINES, LIMIT_BYTES))
        self.assertEqual(limits_for("specs/001-x/spec.md"),
                         (LIMIT_LINES, LIMIT_BYTES))


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
        violations = [r for r in rows if r[0] not in EXEMPT
                      and over_limit(r[1], r[2], limits_for(r[0]))]
        self.assertEqual(violations, [])


if __name__ == "__main__":
    unittest.main()
