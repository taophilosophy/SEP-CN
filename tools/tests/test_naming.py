# -*- coding: utf-8 -*-
"""命名登记表单测（ADR-0080：identifier／name／state 三层分离）。

断言的都是这次迁移真正依赖的性质：别名可解析（历史 journal 与旧命令行不改写也能读）、
状态由 identifier 派生（改名不再牵动状态）、词表与管线一一对应（新增节点漏登记即红）。
"""
import copy
import json
import os
import sys
import tempfile
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, REPO)

from tools import naming_lib  # noqa: E402
from tools.check_stages import check, load_pipeline  # noqa: E402


class RegistryTest(unittest.TestCase):

    def test_registry_self_consistent(self):
        self.assertEqual(naming_lib.validate(), [])

    def test_count_and_segments(self):
        ids = naming_lib.identifiers()
        self.assertEqual(len(ids), 22)
        self.assertEqual(sum(1 for i in ids if i.startswith("ex-")), 5)
        self.assertEqual(sum(1 for i in ids if i.startswith("tr-")), 5)
        self.assertEqual(sum(1 for i in ids if i.startswith("rv-")), 9)
        self.assertEqual(sum(1 for i in ids if i.startswith("sg-")), 3)

    def test_state_derived_from_identifier(self):
        for n in naming_lib.load().get("nodes", []):
            if n.get("state"):
                self.assertEqual(n["state"], n["identifier"] + "_checked")


class AliasTest(unittest.TestCase):

    def test_historical_names_resolve(self):
        cases = {"P1": "ex-01", "s0": "ex-04", "draft": "tr-02", "s2.4": "rv-01",
                 "s24": "rv-01", "global": "rv-02", "s25": "rv-02", "audit": "rv-02",
                 "q1": "rv-03", "q6": "rv-08", "S3": "rv-09", "s3": "rv-09",
                 "R1": "sg-01", "r3": "sg-03"}
        for old, new in cases.items():
            self.assertEqual(naming_lib.identifier(old), new, old)

    def test_identifier_and_name_roundtrip(self):
        self.assertEqual(naming_lib.identifier("rv-03"), "rv-03")
        self.assertEqual(naming_lib.identifier("review.cite"), "rv-03")
        self.assertEqual(naming_lib.name_of("rv-03"), "review.cite")
        self.assertIsNone(naming_lib.try_identifier("no-such-node"))

    def test_state_aliases_cover_legacy_states(self):
        legacy = ["drafted", "s0_source_checked", "s1_checked", "s2_checked",
                  "s2.4_termchecked", "s2.5_checked", "q1_cite_checked",
                  "q6_punct_checked", "s3_checked", "r1_reviewed", "r3_reviewed"]
        for st in legacy:
            self.assertTrue(naming_lib.normalize_state(st).endswith("_checked"), st)
        self.assertEqual(naming_lib.normalize_state("pending"), "pending")
        self.assertEqual(naming_lib.normalize_state(None), None)

    def test_steps_table_accepts_every_spelling(self):
        tbl = naming_lib.steps_table()
        for spelling in ("s0", "rv-04", "review.punctuation", "R3", "q1"):
            self.assertIn(spelling, tbl, spelling)


class S7PredicateTest(unittest.TestCase):

    def test_pipeline_matches_registry(self):
        hits = check(load_pipeline())
        bad = [h for h in hits if h["code"] == "S7" and not h["ok"]]
        self.assertEqual(bad, [])

    def test_new_node_without_registry_entry_is_red(self):
        """新增节点不在登记表里 → S7 必须红（单一事实源不得绕过）。"""
        pipe = load_pipeline()
        pipe["nodes"].append({"id": "rv-20", "prev": "sg-03", "type": "stage",
                              "seg": "seg3", "criteria": [], "mandatory": False})
        hits = check(pipe, journal_nodes=set(), task_states=set())
        self.assertTrue(any(h["code"] == "S7" and h["name"] == "登记表与管线一一对应"
                            and not h["ok"] for h in hits))

    def test_unresolved_historical_node_is_red(self):
        pipe = load_pipeline()
        hits = check(pipe, journal_nodes={"s0", "q3", "phantom-node"}, task_states=set())
        self.assertTrue(any(h["name"] == "历史节点名可归一" and not h["ok"] for h in hits))

    def test_stray_task_state_is_red(self):
        pipe = load_pipeline()
        hits = check(pipe, journal_nodes=set(), task_states={"rv-01_checked", "halfway"})
        self.assertTrue(any(h["name"] == "任务状态名在词表内" and not h["ok"] for h in hits))

    def test_registry_reusing_reserved_number_is_red(self):
        reg = copy.deepcopy(naming_lib.load())
        reg["nodes"][0]["identifier"] = "ex-07"   # 落在预留号段
        reg["nodes"][0]["state"] = None
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False,
                                         encoding="utf-8") as f:
            json.dump({k: v for k, v in reg.items() if not k.startswith("_")}, f)
            path = f.name
        try:
            errs = naming_lib.validate(path)
            self.assertTrue(any("预留" in e or "一一对应" in e for e in errs), errs)
        finally:
            os.unlink(path)


if __name__ == "__main__":
    unittest.main()
