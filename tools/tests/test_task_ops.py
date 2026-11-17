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
        self.old_audit = task_ops._audit_gate
        self.old_term = task_ops._term_gate
        self.old_src = task_ops._source_gate
        task_ops.TASKS_DIR = self._dir.name
        # 测试打桩：版本钉与基线 gate 注入，生产 gate 不变
        task_ops._version_pin = lambda slug: {"pubinfo_date": "Aug 9, 2026",
                                              "archive_edition": "Fall 2026",
                                              "sha256": "0" * 64}
        task_ops._clear_gate = lambda slug: None
        task_ops._audit_gate = lambda zh_doc: None
        task_ops._term_gate = lambda zh_doc: None
        task_ops._source_gate = lambda slug: None

    def tearDown(self):
        task_ops.TASKS_DIR = self.old
        task_ops._version_pin = self.old_pin
        task_ops._clear_gate = self.old_gate
        task_ops._audit_gate = self.old_audit
        task_ops._term_gate = self.old_term
        task_ops._source_gate = self.old_src
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
        t = task_ops.advance("test-b", "s0", actor="t", evidence="源审计记录")
        self.assertEqual(t["state"], "s0_source_checked")
        task_ops.advance("test-b", "draft", actor="t", evidence="e")
        t = task_ops.advance("test-b", "s1", actor="t", evidence="对照记录")
        self.assertEqual(t["state"], "s1_checked")

    def test_draft_requires_s0(self):
        # 源审计前置（ADR-0052）：cleared → draft 跳过 s0 即拒
        task_ops.create("test-s0a", "retranslate", zh_doc=self._md("s0a.md"))
        task_ops.clear("test-s0a")
        with self.assertRaises(task_ops.PreconditionError):
            task_ops.advance("test-s0a", "draft", actor="t", evidence="e")
        t = task_ops.advance("test-s0a", "s0", actor="t", evidence="源审计记录")
        self.assertEqual(t["state"], "s0_source_checked")

    def test_s3_requires_s0_history(self):
        # 进三校前必须有 s0 记录（ADR-0052 决策 5）：在途件补课后才放行。
        # 直接构造 ADR-0052 之前的 legacy 任务 JSON（state=s2.5_checked、无 s0 步），
        # 新状态机下已无法经 advance 走出这种流程。
        task_ops.create("test-s0b", "retranslate", zh_doc=self._md("s0b.md"))
        t = task_ops.load_task("test-s0b")
        t["state"] = "s2.5_checked"
        t["steps"] = [{"step": st, "status": "ok", "actor": "t", "at": "2026-11-01T00:00:00Z",
                       "evidence": "e"} for st in ("clear", "draft", "s1", "s2", "s24", "s25")]
        task_ops.save_task(t)
        with self.assertRaises(task_ops.PreconditionError):
            task_ops.advance("test-s0b", "s3", actor="t", evidence="e")
        t = task_ops.source_audit("test-s0b", actor="t", evidence="specs/036 补课凭证")
        self.assertEqual(t["state"], "s2.5_checked")  # 补课不迁移状态
        self.assertEqual(sum(1 for s in t["steps"] if s["step"] == "s0"), 1)
        t = task_ops.advance("test-s0b", "s3", actor="t", evidence="e")
        self.assertEqual(t["state"], "s3_checked")

    def test_source_audit_makeup_rules(self):
        # 补课子命令边界：pending/cleared 走正常 advance；重复补课拒
        task_ops.create("test-s0c", "retranslate", zh_doc=self._md("s0c.md"))
        with self.assertRaises(task_ops.PreconditionError):
            task_ops.source_audit("test-s0c", actor="t", evidence="e")  # pending
        task_ops.clear("test-s0c")
        with self.assertRaises(task_ops.PreconditionError):
            task_ops.source_audit("test-s0c", actor="t", evidence="e")  # cleared
        task_ops.advance("test-s0c", "s0", actor="t", evidence="源审计记录")
        task_ops.advance("test-s0c", "draft", actor="t", evidence="e")
        with self.assertRaises(task_ops.PreconditionError):
            task_ops.source_audit("test-s0c", actor="t", evidence="e")  # 已有 s0

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
        for step in ("s0", "draft", "s1", "s2"):
            task_ops.advance("test-r", step, actor="t", evidence="e")
        task_ops.advance("test-r", "s24", actor="t", evidence="e")
        task_ops.advance("test-r", "audit", actor="t", evidence="e；冷置回读＋密度统计")
        for step in ("s3", "r1", "r2"):
            task_ops.advance("test-r", step, actor="t", evidence="e")
        task_ops.advance("test-r", "r3", actor="t", evidence="冷置重读",
                         mandate="用户 2026-11-15 指定本会话终审（ADR-0054）")  # 单会话形态留痕
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
            task_ops.advance("test-c", "s0", actor="t", evidence="changes:#item3")
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
        for step in ("s0", "draft", "s1", "s2"):
            task_ops.advance("test-e", step, actor="t", evidence="e")
        task_ops.advance("test-e", "s24", actor="t", evidence="e")
        task_ops.advance("test-e", "audit", actor="t", evidence="e；冷置回读＋密度统计")
        task_ops.advance("test-e", "s3", actor="t", evidence="e")
        with self.assertRaises(task_ops.PreconditionError):
            task_ops.advance("test-e", "done", actor="t", evidence="跳步收口")
        for step in ("r1", "r2"):
            task_ops.advance("test-e", step, actor="t", evidence="e")
        t = task_ops.advance("test-e", "r3", actor="t", evidence="冷置重读",
                             mandate="用户 2026-11-15 指定本会话终审（ADR-0054）")
        t = task_ops.advance("test-e", "done", actor="t", evidence="e")
        self.assertEqual(t["state"], "done")
        with self.assertRaises(task_ops.PreconditionError):
            task_ops.advance("test-e", "done", actor="t", evidence="重复收口")

    def test_r3_requires_user_mandate(self):
        # 终审会话用户指定硬门（ADR-0054）：无 --mandate 拒绝，条目停 r2_reviewed
        task_ops.create("test-m", "retranslate", zh_doc=self._md("m.md"))
        task_ops.clear("test-m")
        for step in ("s0", "draft", "s1", "s2"):
            task_ops.advance("test-m", step, actor="t", evidence="e")
        task_ops.advance("test-m", "s24", actor="t", evidence="e")
        task_ops.advance("test-m", "audit", actor="t", evidence="e；冷置回读＋密度统计")
        for step in ("s3", "r1", "r2"):
            task_ops.advance("test-m", step, actor="t", evidence="e")
        with self.assertRaises(task_ops.PreconditionError):
            task_ops.advance("test-m", "r3", actor="t", evidence="自作主张终审")
        self.assertEqual(task_ops.load_task("test-m")["state"], "r2_reviewed")
        t = task_ops.advance("test-m", "r3", actor="t", evidence="冷置重读",
                             mandate="用户 2026-11-15 指定本会话终审（ADR-0054）")
        self.assertEqual(t["state"], "r3_reviewed")
        self.assertEqual(t["steps"][-1].get("mandate"),
                         "用户 2026-11-15 指定本会话终审（ADR-0054）")

    def test_r3_independence_same_actor_requires_cold_note(self):
        # 复核独立性机检（rules/04、ADR-0020 裁定②）：单会话形态 r3 必须记明冷置
        task_ops.create("test-i1", "retranslate", zh_doc=self._md("i1.md"))
        task_ops.clear("test-i1")
        for step in ("s0", "draft", "s1", "s2"):
            task_ops.advance("test-i1", step, actor="t", evidence="e")
        task_ops.advance("test-i1", "s24", actor="t", evidence="e")
        task_ops.advance("test-i1", "audit", actor="t", evidence="e；冷置回读＋密度统计")
        for step in ("s3", "r1", "r2"):
            task_ops.advance("test-i1", step, actor="t", evidence="e")
        with self.assertRaises(task_ops.PreconditionError):
            task_ops.advance("test-i1", "r3", actor="t", evidence="看过了",
                             mandate="用户 2026-11-15 指定本会话终审（ADR-0054）")
        t = task_ops.advance("test-i1", "r3", actor="t", evidence="冷置：先做其他任务后回读",
                             mandate="用户 2026-11-15 指定本会话终审（ADR-0054）")
        self.assertEqual(t["state"], "r3_reviewed")

    def test_r3_independence_cross_actor_passes(self):
        # 评审线交叉（specs/005 §6）：r3 由初译以外 actor 执行即满足，无需冷置记明
        task_ops.create("test-i2", "retranslate", zh_doc=self._md("i2.md"))
        task_ops.clear("test-i2")
        for step in ("s0", "draft", "s1", "s2"):
            task_ops.advance("test-i2", step, actor="w", evidence="e")
        task_ops.advance("test-i2", "s24", actor="w", evidence="e")
        task_ops.advance("test-i2", "audit", actor="w", evidence="e；冷置回读＋密度统计")
        for step in ("s3", "r1", "r2"):
            task_ops.advance("test-i2", step, actor="w", evidence="e")
        t = task_ops.advance("test-i2", "r3", actor="rev", evidence="e",
                             mandate="用户 2026-11-15 指定本会话终审（ADR-0054）")
        self.assertEqual(t["state"], "r3_reviewed")

    def test_r3_independence_update_keys_on_s1(self):
        # update 任务首写步是 s1：独立性相对变更写者判定
        with tempfile.TemporaryDirectory() as d:
            cf = os.path.join(d, "change.json")
            write_text(cf, '{"items": []}')
            task_ops.create("test-i3", "update", change_file=cf)
            task_ops.advance("test-i3", "s0", actor="w", evidence="changes:#item3")
            task_ops.advance("test-i3", "s1", actor="w", evidence="changes:#item3")
            task_ops.advance("test-i3", "s2", actor="w", evidence="changes:#item3")
            task_ops.advance("test-i3", "s24", actor="w", evidence="changes:#item3")
            task_ops.advance("test-i3", "audit", actor="w",
                             evidence="changes:#item3；冷置回读＋密度统计")
            for step in ("s3", "r1", "r2"):
                task_ops.advance("test-i3", step, actor="w", evidence="changes:#item3")
            with self.assertRaises(task_ops.PreconditionError):
                task_ops.advance("test-i3", "r3", actor="w", evidence="changes:#item3",
                                 mandate="用户 2026-11-15 指定本会话终审（ADR-0054）")
            t = task_ops.advance("test-i3", "r3", actor="rev", evidence="changes:#item3",
                                 mandate="用户 2026-11-15 指定本会话终审（ADR-0054）")
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
        task_ops.advance("test-d", "s0", actor="t", evidence="e")
        t2 = task_ops.advance("test-d", "draft", actor="t", evidence="e")
        self.assertEqual(t2["state"], "drafted")


    def test_audit_step_required_before_s3(self):
        # 审计已译环节（ADR-0040）：s2_checked → s3 跳过 audited 即拒
        task_ops.create("test-a1", "retranslate", zh_doc=self._md("a1.md"))
        task_ops.clear("test-a1")
        for step in ("s0", "draft", "s1", "s2"):
            task_ops.advance("test-a1", step, actor="t", evidence="e")
        task_ops.advance("test-a1", "s24", actor="t", evidence="e")
        with self.assertRaises(task_ops.PreconditionError):
            task_ops.advance("test-a1", "s3", actor="t", evidence="跳过审计")
        t = task_ops.advance("test-a1", "audit", actor="t",
                             evidence="三向比对记录；单会话冷置回读＋密度统计")
        self.assertEqual(t["state"], "s2.5_checked")
        t = task_ops.advance("test-a1", "s3", actor="t", evidence="e")
        self.assertEqual(t["state"], "s3_checked")

    def test_audit_gate_blocks_bare_dollar(self):
        # audited 挂钩：check_math_zh 默认档硬错误（裸 $）拦下审计（ADR-0040）
        task_ops._audit_gate = self.old_audit  # 还原真 gate
        bad_body = "# 测试标题\n\n值 $x 未配对。\n"
        bad = self._md("g-bad.md", bad_body)
        task_ops.create("test-g1", "retranslate", zh_doc=bad)
        task_ops.clear("test-g1")
        write_text(bad, bad_body)  # clear 置空后写回，模拟 draft 成稿含裸 $
        for step in ("s0", "draft", "s1", "s2"):
            task_ops.advance("test-g1", step, actor="t", evidence="e")
        task_ops.advance("test-g1", "s24", actor="t", evidence="e")
        with self.assertRaises(task_ops.PreconditionError):
            task_ops.advance("test-g1", "audit", actor="t", evidence="三向比对记录")
        good_body = "# 测试标题\n\n值 $x$ 配对完好。\n"
        good = self._md("g-good.md", good_body)
        task_ops.create("test-g2", "retranslate", zh_doc=good)
        task_ops.clear("test-g2")
        write_text(good, good_body)
        for step in ("s0", "draft", "s1", "s2"):
            task_ops.advance("test-g2", step, actor="t", evidence="e")
        task_ops.advance("test-g2", "s24", actor="t", evidence="e")
        t = task_ops.advance("test-g2", "audit", actor="t",
                             evidence="三向比对记录；冷置回读＋密度统计")
        self.assertEqual(t["state"], "s2.5_checked")

    def test_update_audit_requires_change_evidence(self):
        # update 任务 audit 与 s1/s2 同款：证据必须引用变更清单
        with tempfile.TemporaryDirectory() as d:
            cf = os.path.join(d, "change.json")
            write_text(cf, '{"items": []}')
            task_ops.create("test-u1", "update", change_file=cf)
            task_ops.advance("test-u1", "s0", actor="t", evidence="changes:#item3")
            task_ops.advance("test-u1", "s1", actor="t", evidence="changes:#item3")
            task_ops.advance("test-u1", "s2", actor="t", evidence="changes:#item3")
            task_ops.advance("test-u1", "s24", actor="t", evidence="changes:#item3")
            with self.assertRaises(task_ops.PreconditionError):
                task_ops.advance("test-u1", "audit", actor="t", evidence="口说无凭")
            t = task_ops.advance("test-u1", "audit", actor="t",
                                 evidence="changes:#item3；冷置回读＋密度统计")
            self.assertEqual(t["state"], "s2.5_checked")

    def test_audit_independence_same_actor_requires_compensation(self):
        # 审计独立性机检（rules/04 同源盲区对冲、specs/027 FR-001）：
        # audit 与初译 actor 全同时，evidence 须记明冷置或密度统计补偿
        task_ops.create("test-n1", "retranslate", zh_doc=self._md("n1.md"))
        task_ops.clear("test-n1")
        for step in ("s0", "draft", "s1", "s2"):
            task_ops.advance("test-n1", step, actor="t", evidence="e")
        task_ops.advance("test-n1", "s24", actor="t", evidence="e")
        with self.assertRaises(task_ops.PreconditionError):
            task_ops.advance("test-n1", "audit", actor="t", evidence="三向比对记录")
        t = task_ops.advance("test-n1", "audit", actor="rev", evidence="三向比对记录")
        self.assertEqual(t["state"], "s2.5_checked")

    def test_reopen_upstream_sync_from_s25(self):
        # R3（ADR-0051）：在途 s2.5_checked 遇上游实质修订——无 flag 拒绝（禁跳步），
        # --upstream-sync 显式绕过打回 pending，step 留 bypass 标记
        md = self._md("u.md", "# 测试标题\n\n旧译文。\n")
        task_ops.create("test-u2", "retranslate", zh_doc=md)
        task_ops.clear("test-u2")
        for step in ("s0", "draft", "s1", "s2"):
            task_ops.advance("test-u2", step, actor="t", evidence="e")
        task_ops.advance("test-u2", "s24", actor="t", evidence="e")
        t = task_ops.advance("test-u2", "audit", actor="rev", evidence="e")
        self.assertEqual(t["state"], "s2.5_checked")
        with self.assertRaises(task_ops.PreconditionError):
            task_ops.reopen("test-u2", "上游修订", actor="t")
        t = task_ops.reopen("test-u2", "上游实质修订，compare/u.json 在案", actor="t",
                            upstream_sync=True)
        self.assertEqual(t["state"], "pending")
        self.assertTrue(any(st.get("bypass", "").startswith("upstream-sync")
                            for st in t["steps"]))

    def test_reopen_upstream_sync_rejects_done_and_blocked(self):
        # blocked 即使带 flag 也拒（先 --unblock）；done 走默认 R1/R2 语义（flag 不适用）
        md = self._md("u3.md", "# 测试标题\n\n旧译文。\n")
        task_ops.create("test-u3", "retranslate", zh_doc=md)
        task_ops.clear("test-u3")
        task_ops.advance("test-u3", "s0", actor="t", evidence="e")
        task_ops.advance("test-u3", "draft", actor="t", evidence="e")
        task_ops.block("test-u3", "挂起核查")
        with self.assertRaises(task_ops.PreconditionError):
            task_ops.reopen("test-u3", "上游修订", actor="t", upstream_sync=True)
        # done 件：flag 不适用（done 走默认 R1/R2），默认 reopen 照常
        md2 = self._md("u4.md", "# 测试标题\n\n旧译文。\n")
        task_ops.create("test-u4", "retranslate", zh_doc=md2)
        task_ops.clear("test-u4")
        for step in ("s0", "draft", "s1", "s2"):
            task_ops.advance("test-u4", step, actor="t", evidence="e")
        task_ops.advance("test-u4", "s24", actor="t", evidence="e")
        task_ops.advance("test-u4", "audit", actor="rev", evidence="e")
        for step in ("s3", "r1", "r2"):
            task_ops.advance("test-u4", step, actor="rev", evidence="e")
        task_ops.advance("test-u4", "r3", actor="rev", evidence="e",
                         mandate="用户 2026-11-15 指定本会话终审（ADR-0054）")
        task_ops.advance("test-u4", "done", actor="t", evidence="e")
        with self.assertRaises(task_ops.PreconditionError):
            task_ops.reopen("test-u4", "上游修订", actor="t", upstream_sync=True)
        t = task_ops.reopen("test-u4", "上游实质修订", actor="t")
        self.assertEqual(t["state"], "pending")


class TestS25ThreeAxes(unittest.TestCase):
    """s2.5 三轴并挂（ADR-0063 2026-11-17 补记）。

    背景：受控回退目标态为 s2.4_termchecked（该 checkpoint 视为已完成），
    随后正常推进即 s25——advance s24 对回退件不可达。若不把术语/体例/勘误
    三轴并挂到 s25，P8 的 416 件回退重走会整体绕过体例硬门。
    """

    def setUp(self):
        self._dir = tempfile.TemporaryDirectory()
        self.old = task_ops.TASKS_DIR
        task_ops.TASKS_DIR = self._dir.name
        self.calls = []
        self._old = {n: getattr(task_ops, n) for n in
                     ("_version_pin", "_clear_gate", "_audit_gate", "_term_gate",
                      "_source_gate", "_style_gate", "_audit_independence_gate")}
        task_ops._version_pin = lambda slug: {"pubinfo_date": "Aug 9, 2026",
                                              "archive_edition": "Fall 2026",
                                              "sha256": "0" * 64}
        task_ops._clear_gate = lambda slug: None
        task_ops._source_gate = lambda slug: None
        task_ops._audit_independence_gate = lambda task, actor, ev: None
        task_ops._term_gate = lambda zh: self.calls.append("term")
        task_ops._style_gate = lambda zh: self.calls.append("style")
        task_ops._audit_gate = lambda zh: self.calls.append("audit")

    def tearDown(self):
        task_ops.TASKS_DIR = self.old
        for n, f in self._old.items():
            setattr(task_ops, n, f)
        self._dir.cleanup()

    def _md(self, name):
        p = os.path.join(self._dir.name, name)
        write_text(p, "# 测试标题\n\n旧正文。\n")
        return p

    def _walk_s24(self, slug):
        task_ops.create(slug, "retranslate", zh_doc=self._md(slug + ".md"))
        task_ops.clear(slug)
        for step in ("s0", "draft", "s1", "s2", "s24"):
            task_ops.advance(slug, step, actor="t", evidence="e")

    def test_normal_path_s25_refires_three_axes(self):
        self._walk_s24("t-s25a")
        self.calls.clear()
        t = task_ops.advance("t-s25a", "s25", actor="t", evidence="两轴比对记录")
        self.assertEqual(t["state"], "s2.5_checked")
        self.assertEqual(sorted(self.calls), ["audit", "style", "term"])

    def test_revert_then_s25_refires_three_axes(self):
        self._walk_s24("t-s25b")
        task_ops.advance("t-s25b", "s25", actor="t", evidence="e")
        t = task_ops.revert_state("t-s25b", "s2.4_termchecked",
                                  "体例归一全量回退（specs/039 P8）", actor="t")
        self.assertEqual(t["state"], "s2.4_termchecked")
        self.calls.clear()
        t = task_ops.advance("t-s25b", "s25", actor="t", evidence="体例轴增项并入 s25")
        self.assertEqual(t["state"], "s2.5_checked")
        self.assertEqual(sorted(self.calls), ["audit", "style", "term"])

    def test_style_gate_failure_blocks_s25(self):
        self._walk_s24("t-s25c")

        def boom(zh):
            raise task_ops.PreconditionError("体例轴未通过：tail-order")
        task_ops._style_gate = boom
        with self.assertRaises(task_ops.PreconditionError):
            task_ops.advance("t-s25c", "s25", actor="t", evidence="e")
        self.assertEqual(task_ops.load_task("t-s25c")["state"], "s2.4_termchecked")


if __name__ == "__main__":
    unittest.main()
