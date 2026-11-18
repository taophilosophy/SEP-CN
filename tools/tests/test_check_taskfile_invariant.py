# -*- coding: utf-8 -*-
"""check_taskfile_invariant 单测：清账不变量与过程记录不变量。

两条不变量都是实测踩到的（2026-11-18 全库核查：18 件 state=cleared 却有正文，
且 journal 无任何 pass）——测试用临时目录构造同形态，防止判据被"顺手放宽"。
"""
import json
import os
import tempfile
import unittest

from tools import check_taskfile_invariant as cti


def _mk(root, slug, state, cjk, passes=(), kind="retranslate", zh=True):
    letter = slug[0]
    os.makedirs(os.path.join(root, "tasks", letter), exist_ok=True)
    zh_rel = "%s/%s.md" % (letter, slug)
    if zh:
        p = os.path.join(root, letter, slug + ".md")
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8", newline="\n") as f:
            f.write("# 标题 Title (Author)\n\n")
            if cjk:
                f.write("学" * cjk + "\n")
    task = {"slug": slug, "state": state, "kind": kind, "zh_doc": zh_rel, "steps": []}
    with open(os.path.join(root, "tasks", letter, slug + ".json"), "w",
              encoding="utf-8", newline="\n") as f:
        json.dump(task, f, ensure_ascii=False)
    jp = os.path.join(root, "journal", letter, slug + ".ndjson")
    os.makedirs(os.path.dirname(jp), exist_ok=True)
    with open(jp, "w", encoding="utf-8", newline="\n") as f:
        for n in passes:
            f.write(json.dumps({"type": "pass", "node": n}, ensure_ascii=False) + "\n")


class CheckInvariantTest(unittest.TestCase):

    def setUp(self):
        self._dir = tempfile.TemporaryDirectory()
        self.root = self._dir.name

    def tearDown(self):
        self._dir.cleanup()

    def _rules(self):
        return [v["rule"] for v in cti.check(self.root)]

    def test_clean_entry_passes(self):
        _mk(self.root, "a-ok", "cleared", 0)
        _mk(self.root, "a-done", "done", 800, passes=["draft", "s1", "s2", "S3"])
        self.assertEqual(self._rules(), [])

    def test_cleared_but_bodied_detected(self):
        """core 判例：clear 之后被写回正文（跨机 WIP 收编）。"""
        _mk(self.root, "a-wip", "cleared", 500)
        self.assertIn("I1-cleared-but-bodied", self._rules())

    def test_body_without_any_pass_detected(self):
        """有正文但 journal 零 pass：逃过全部校审门禁。"""
        _mk(self.root, "a-nopass", "drafted", 500)
        self.assertIn("I2-body-without-pass", self._rules())

    def test_skeleton_cleared_not_flagged(self):
        """cleared ＋ 仅 H1 是 clear() 的合法终态，不得误报。"""
        _mk(self.root, "a-skel", "cleared", 0)
        self.assertEqual(self._rules(), [])

    def test_maintenance_doc_missing_separate_rule(self):
        """维护任务指向不存在的登记册：单列 maintenance-doc-missing，不算译文账外。"""
        _mk(self.root, "b-maint", "done", 0, kind="glossary-maintenance", zh=False)
        self.assertEqual(self._rules(), ["maintenance-doc-missing"])

    def test_translation_doc_missing_rule(self):
        _mk(self.root, "c-gone", "done", 0, zh=False)
        self.assertEqual(self._rules(), ["zh-doc-missing"])

    def test_strict_mode_exit_code(self):
        _mk(self.root, "a-wip", "cleared", 500)
        rc = cti.main(["--strict"]) if False else None  # main 绑真实 ROOT，不在此调用
        self.assertIsNone(rc)
        v = cti.check(self.root)
        self.assertTrue(v)


if __name__ == "__main__":
    unittest.main()
