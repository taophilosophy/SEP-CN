# -*- coding: utf-8 -*-
"""check_layout 四谓词单测（ADR-0067）。"""
import json
import os
import sys
import tempfile
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, REPO)

from tools.check_layout import (  # noqa: E402
    check_l2, check_l4, declared_paths, load_layout, normalize_table_cell,
)

LAYOUT = load_layout(os.path.join(REPO, "rules", "layout.json"))


class NormalizeCellTest(unittest.TestCase):
    def test_single_path(self):
        self.assertEqual(normalize_table_cell("| `rules/` | x |"), {"rules"})

    def test_multi_path_cell(self):
        self.assertEqual(normalize_table_cell("| `script/`、`state/` | x |"), {"script", "state"})

    def test_letter_placeholder(self):
        self.assertEqual(normalize_table_cell("| `<letter>/`（a…z） | x |"), {"<letter>"})

    def test_nested_path_takes_head(self):
        self.assertEqual(normalize_table_cell("| `yuanwen/assets/<slug>/` | x |"), {"yuanwen"})


class DeclaredPathsTest(unittest.TestCase):
    def test_zh_container(self):
        declared = declared_paths(LAYOUT)
        self.assertIn("zh", declared)
        for c in "abcdefghijklmnopqrstuvwxyz1":
            self.assertNotIn(c, declared)

    def test_known_entries(self):
        declared = declared_paths(LAYOUT)
        for p in ("rules", "specs", "en", "yuanwen", "zh", ".github", "AGENTS.md"):
            self.assertIn(p, declared)


class L2Test(unittest.TestCase):
    def test_identical_sets_pass(self):
        a = {"rules", "specs"}
        self.assertEqual(check_l2(a, a), ([], []))

    def test_missing_and_extra(self):
        missing, extra = check_l2({"rules", "specs"}, {"rules", "tools"})
        self.assertEqual(missing, ["specs"])
        self.assertEqual(extra, ["tools"])


class L4Test(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.base = self._tmp.name

    def tearDown(self):
        self._tmp.cleanup()

    def mk_spec(self, name="001-demo", children=("spec.md",)):
        d = os.path.join(self.base, name)
        os.makedirs(d, exist_ok=True)
        for c in children:
            p = os.path.join(d, c)
            if c.endswith("/"):
                os.makedirs(p, exist_ok=True)
            else:
                os.makedirs(os.path.dirname(p) or d, exist_ok=True)
                with open(p, "w", encoding="utf-8") as f:
                    f.write("")
        return d

    def test_canonical_passes(self):
        self.mk_spec(children=("spec.md", "bin/", "results/", "notes.md"))
        hard, warn = check_l4(LAYOUT, self.base)
        self.assertEqual(hard, [])
        self.assertEqual(warn, [])

    def test_missing_spec_flagged(self):
        self.mk_spec(children=("report.md",))
        hard, _ = check_l4(LAYOUT, self.base)
        self.assertTrue(any("缺 spec.md" in w for _, w in hard))

    def test_forbidden_tmp_flagged(self):
        self.mk_spec(children=("spec.md", "tmp/"))
        hard, _ = check_l4(LAYOUT, self.base)
        self.assertTrue(any("禁止子目录" in w for _, w in hard))

    def test_root_json_flagged(self):
        self.mk_spec(children=("spec.md", "ledger.json"))
        hard, _ = check_l4(LAYOUT, self.base)
        self.assertTrue(any("规格根不得放 JSON" in w for _, w in hard))

    def test_root_json_allowed_by_file_exception(self):
        self.mk_spec(name="005-translation-campaign", children=("spec.md", "ledger.json"))
        hard, _ = check_l4(LAYOUT, self.base)
        self.assertEqual([h for h in hard if "ledger.json" in h[0]], [])

    def test_execution_log_pair_flagged(self):
        self.mk_spec(children=("spec.md", "execution-log.md", "execution-log/"))
        hard, _ = check_l4(LAYOUT, self.base)
        self.assertTrue(any("并存" in w for _, w in hard))

    def test_bad_dirname_flagged(self):
        self.mk_spec(name="script", children=("x.md",))
        hard, _ = check_l4(LAYOUT, self.base)
        self.assertTrue(any("目录名不符" in w for _, w in hard))

    def test_unknown_subdir_warns_only(self):
        self.mk_spec(children=("spec.md", "weird/"))
        hard, warn = check_l4(LAYOUT, self.base)
        self.assertEqual(hard, [])
        self.assertTrue(any("未知子目录" in w for _, w in warn))


if __name__ == "__main__":
    unittest.main()
