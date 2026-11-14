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

    def test_reopen_then_clear(self):
        # done → reopen（旧 steps 保留）→ clear 置空，回重译队列（ADR-0033）
        md = self._md("r.md", "# 测试标题\n\n旧译文。\n")
        task_ops.create("test-r", "retranslate", zh_doc=md)
        task_ops.clear("test-r")
        for step in ("draft", "s1", "s2", "s3", "r1", "r2"):
            task_ops.advance("test-r", step, actor="t", evidence="e")
        task_ops.advance("test-r", "r3", actor="t", evidence="冷置重读")  # 单会话形态留痕
        task_ops.advance("test-r", "done", actor="t", evidence="e")
        with self.assertRaises(task_ops.UsageError):
            task_ops.reopen("test-r", "", "t")  # 原因必填
        t = task_ops.reopen("test-r", "语体不合规：正文文言", "t")
        self.assertEqual(t["state"], "pending")
        self.assertEqual(t["steps"][-1]["step"], "reopen")
        self.assertEqual(sum(1 for s in t["steps"] if s["step"] == "done"), 1)  # 旧步骤留史
        t = task_ops.clear("test-r")
        self.assertEqual(t["state"], "cleared")
        self.assertEqual(read_text(md), "# 测试标题\n")

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

    def test_done_requires_r3(self):
        # done 不得绕过 r3（2026-11-10 修 done 分支缺前置校验，实测重复 done 由并发撞出）
        task_ops.create("test-e", "retranslate", zh_doc=self._md("e.md"))
        task_ops.clear("test-e")
        for step in ("draft", "s1", "s2", "s3"):
            task_ops.advance("test-e", step, actor="t", evidence="e")
        with self.assertRaises(task_ops.PreconditionError):
            task_ops.advance("test-e", "done", actor="t", evidence="跳步收口")
        for step in ("r1", "r2"):
            task_ops.advance("test-e", step, actor="t", evidence="e")
        t = task_ops.advance("test-e", "r3", actor="t", evidence="冷置重读")
        t = task_ops.advance("test-e", "done", actor="t", evidence="e")
        self.assertEqual(t["state"], "done")
        with self.assertRaises(task_ops.PreconditionError):
            task_ops.advance("test-e", "done", actor="t", evidence="重复收口")

    def test_r3_independence_same_actor_requires_cold_note(self):
        # 复核独立性机检（rules/04、ADR-0020 裁定②）：单会话形态 r3 必须记明冷置
        task_ops.create("test-i1", "retranslate", zh_doc=self._md("i1.md"))
        task_ops.clear("test-i1")
        for step in ("draft", "s1", "s2", "s3", "r1", "r2"):
            task_ops.advance("test-i1", step, actor="t", evidence="e")
        with self.assertRaises(task_ops.PreconditionError):
            task_ops.advance("test-i1", "r3", actor="t", evidence="看过了")
        t = task_ops.advance("test-i1", "r3", actor="t", evidence="冷置：先做其他任务后回读")
        self.assertEqual(t["state"], "r3_reviewed")

    def test_r3_independence_cross_actor_passes(self):
        # 评审线交叉（specs/005 §6）：r3 由初译以外 actor 执行即满足，无需冷置记明
        task_ops.create("test-i2", "retranslate", zh_doc=self._md("i2.md"))
        task_ops.clear("test-i2")
        for step in ("draft", "s1", "s2", "s3", "r1", "r2"):
            task_ops.advance("test-i2", step, actor="w", evidence="e")
        t = task_ops.advance("test-i2", "r3", actor="rev", evidence="e")
        self.assertEqual(t["state"], "r3_reviewed")

    def test_r3_independence_update_keys_on_s1(self):
        # update 任务首写步是 s1：独立性相对变更写者判定
        with tempfile.TemporaryDirectory() as d:
            cf = os.path.join(d, "change.json")
            write_text(cf, '{"items": []}')
            task_ops.create("test-i3", "update", change_file=cf)
            task_ops.advance("test-i3", "s1", actor="w", evidence="changes:#item3")
            for step in ("s2", "s3", "r1", "r2"):
                task_ops.advance("test-i3", step, actor="w", evidence="changes:#item3")
            with self.assertRaises(task_ops.PreconditionError):
                task_ops.advance("test-i3", "r3", actor="w", evidence="changes:#item3")
            t = task_ops.advance("test-i3", "r3", actor="rev", evidence="changes:#item3")
            self.assertEqual(t["state"], "r3_reviewed")

    def test_advance_requires_actor_and_evidence(self):
        # actor/evidence 非空机检（FR-017；brouwer draft actor='?' 同类缺口防再犯）
        task_ops.create("test-f", "retranslate", zh_doc=self._md("f.md"))
        task_ops.clear("test-f")
        with self.assertRaises(task_ops.UsageError):
            task_ops.advance("test-f", "draft", actor="", evidence="e")
        with self.assertRaises(task_ops.UsageError):
            task_ops.advance("test-f", "draft", actor="t", evidence="")

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
