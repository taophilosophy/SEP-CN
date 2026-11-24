# -*- coding: utf-8 -*-
"""check_stages 判据登记表核对单测（ADR-0068：pipeline.json 判据唯一事实源）。"""
import json
import os
import sys
import tempfile
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, REPO)

from tools.check_stages import check, load_pipeline  # noqa: E402


class CheckStagesTest(unittest.TestCase):

    def test_pipeline_valid(self):
        """rules/pipeline.json 应全绿（S1 链闭合／S2 判据唯一／S3 强制集／S4 类型／S5 承载体）。"""
        pipe = load_pipeline()
        hits = check(pipe)
        self.assertTrue(all(h["ok"] for h in hits), [h for h in hits if not h["ok"]])

    def test_carrier_axis_resolves(self):
        """axis 型判据（errata_check → check_pairs#errata-apply）应被解析为真实承载体。"""
        pipe = load_pipeline()
        self.assertIn("errata_check", pipe["criteria_carrier"])
        c = pipe["criteria_carrier"]["errata_check"]
        self.assertEqual(c["kind"], "axis")
        host = os.path.join(REPO, "tools", "%s.py" % c["of"])
        self.assertTrue(os.path.exists(host))
        with open(host, encoding="utf-8") as fh:
            self.assertIn(c["rule"], fh.read())

    def test_negative_dual_gate(self):
        """构造判据双硬拦，S2 应失败。"""
        pipe = load_pipeline()
        for n in pipe["nodes"]:
            if n["id"] == "s1":
                n["criteria"] = ["check_pairs", "check_style"]
        hits = check(pipe)
        self.assertTrue(any(not h["ok"] and h["code"] == "S2" for h in hits))

    def test_negative_break_chain(self):
        """构造断链（双链首），S1 应失败。"""
        pipe = load_pipeline()
        for n in pipe["nodes"]:
            if n["id"] == "P3":
                n["prev"] = None
        hits = check(pipe)
        self.assertTrue(any(not h["ok"] and h["code"] == "S1" for h in hits))

    def test_negative_dangling_carrier(self):
        """登记一个无同名工具、无承载体声明的判据，S5 应失败。

        动机：`errata_check`／`markdownlint`／`ci_all` 曾长期是这种形态——S2 只查
        "登记双向一致"，判据悬空也能全绿，故补 S5。
        """
        pipe = load_pipeline()
        target = next(n for n in pipe["nodes"] if n["id"] == "s1")
        target["criteria"] = ["nonexistent_tool"]
        pipe["criteria_owner"].pop("check_pairs", None)
        pipe["criteria_owner"]["nonexistent_tool"] = ["s1"]
        hits = check(pipe)
        self.assertTrue(any(not h["ok"] and h["name"] == "判据承载体可解析" for h in hits))

    def test_negative_warn_carrier_on_hard_gate(self):
        """硬拦位判据若由告警级承载体承担，S5 应失败（声明硬拦、实际不拦）。"""
        pipe = load_pipeline()
        pipe["criteria_carrier"]["check_style"] = {
            "kind": "external", "config": ".nonexistent.jsonc", "level": "warn"}
        hits = check(pipe)
        self.assertTrue(any(not h["ok"] and h["name"] == "硬拦判据不由告警级承载"
                            for h in hits))

    def test_negative_axis_rule_missing(self):
        """axis 指向宿主内不存在的规则名，S5 应失败。"""
        pipe = load_pipeline()
        pipe["criteria_carrier"]["errata_check"] = {
            "kind": "axis", "of": "check_pairs", "rule": "no-such-rule", "level": "hard"}
        hits = check(pipe)
        self.assertTrue(any(not h["ok"] and h["name"] == "判据承载体可解析" for h in hits))


    def test_object_class_declared_for_multi_criteria(self):
        """S6：多判据节点必须声明 object_class（ADR-0079 补记）。"""
        pipe = load_pipeline()
        for n in pipe["nodes"]:
            crit = [g for g in n.get("criteria", []) if g]
            if len(crit) > 1:
                self.assertTrue(n.get("object_class"), n["id"])

    def test_negative_merge_detected_by_s6(self):
        """把六轴判据塞进 S3 而不改 object_class，S6 应失败（防静默归并）。"""
        pipe = load_pipeline()
        for n in pipe["nodes"]:
            if n["id"] == "S3":
                n["criteria"] = n["criteria"] + ["cite_audit", "logic_audit"]
        hits = check(pipe)
        bad = [h for h in hits if h["code"] == "S6" and not h["ok"]]
        self.assertTrue(bad, hits)

if __name__ == "__main__":
    unittest.main()
