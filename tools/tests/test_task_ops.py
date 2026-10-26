# -*- coding: utf-8 -*-
"""task_ops 状态机：禁止跳步、update 证据约束、clear gate 拒绝。"""
import os
import sys
import tempfile
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, REPO)

from tools import task_ops  # noqa: E402
from tools.common import read_text, write_text  # noqa: E402


class TestTaskOps(unittest.TestCase):
    def setUp(self):
        self._dir = tempfile.TemporaryDirectory()
        self.old = task_ops.TASKS_DIR
        self.old_pin = task_ops._version_pin
        self.old_gate = task_ops._clear_gate
        task_ops.TASKS_DIR = self._dir.name
        # 测试打桩：版本钉与基线 gate 注入，生产 gate 不变
        task_ops._version_pin = lambda slug: {"pubinfo_date": "Aug 9, 2026",
                                              "archive_edition": "Fall 2026",
                                              "sha256": "0" * 64}
        task_ops._clear_gate = lambda slug: None

    def tearDown(self):
        task_ops.TASKS_DIR = self.old
        task_ops._version_pin = self.old_pin
        task_ops._clear_gate = self.old_gate
        self._dir.cleanup()

    def _md(self, name, body="# 测试标题\n\n旧正文。\n"):
        p = os.path.join(self._dir.name, name)
        write_text(p, body)
        return p

    def test_skip_step_rejected(self):
        task_ops.create("test-a", "retranslate", zh_doc=self._md("a.md"))
        with self.assertRaises(task_ops.PreconditionError):
            task_ops.advance("test-a", "s2", actor="t", evidence="e")  # 未 clear/draft/s1

    def test_advance_happy_path(self):
        task_ops.create("test-b", "retranslate", zh_doc=self._md("b.md"))
        task_ops.clear("test-b")
        task_ops.advance("test-b", "draft", actor="t", evidence="e")
        t = task_ops.advance("test-b", "s1", actor="t", evidence="对照记录")
        self.assertEqual(t["state"], "s1_checked")

    def test_clear_keeps_h1_only(self):
        md = self._md("c.md")
        task_ops.create("test-c", "retranslate", zh_doc=md)
        task_ops.clear("test-c")
        self.assertEqual(read_text(md), "# 测试标题\n")
        t = task_ops.load_task("test-c")
        self.assertEqual(t["state"], "cleared")

    def test_update_requires_change_evidence(self):
        with tempfile.TemporaryDirectory() as d:
            cf = os.path.join(d, "change.json")
            write_text(cf, '{"items": []}')
            task_ops.create("test-c", "update", change_file=cf)
            with self.assertRaises(task_ops.PreconditionError):
                task_ops.advance("test-c", "s1", actor="t", evidence="口说无凭")
            t = task_ops.advance("test-c", "s1", actor="t", evidence="changes:#item3")
            self.assertEqual(t["state"], "s1_checked")

    def test_clear_gate_rejected_without_baseline(self):
        # 还原真 gate：仓库基线无此词条 → 必须拒绝（宪法附加约束）
        task_ops._clear_gate = self.old_gate
        task_ops.create("test-no-baseline-xyz", "retranslate", zh_doc=self._md("x.md"))
        with self.assertRaises(task_ops.PreconditionError):
            task_ops.clear("test-no-baseline-xyz")

    def test_block_unblock(self):
        task_ops.create("test-d", "retranslate", zh_doc=self._md("d.md"))
        task_ops.block("test-d", "等待术语裁定")
        with self.assertRaises(task_ops.PreconditionError):
            task_ops.clear("test-d")
        t = task_ops.advance("test-d", None, actor="t", evidence="裁定完成", unblock=True)
        self.assertEqual(t["blockers"], [])
        task_ops.clear("test-d")
        t2 = task_ops.advance("test-d", "draft", actor="t", evidence="e")
        self.assertEqual(t2["state"], "drafted")


if __name__ == "__main__":
    unittest.main()
