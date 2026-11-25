# -*- coding: utf-8 -*-
"""mandatory_backfill 单测：回补记账的三条硬约束。

三条都是踩过的坑：①已有 pass 不得重记（幂等）；②某节点 fail 后下游不得记 pass
（schema 的 fail 不变量）；③局部运行不得写主账（specs/051 §1.5 凭证覆写）。
"""
import unittest
from unittest import mock

from tools import mandatory_backfill as mb


class LedgerNameTest(unittest.TestCase):

    def test_full_ledger_has_no_suffix(self):
        self.assertTrue(mb._ledger_name(True).endswith(".json"))
        self.assertNotIn("-partial", mb._ledger_name(True))

    def test_partial_ledger_is_separate_file(self):
        self.assertIn("-partial", mb._ledger_name(False))

    def test_partial_never_equals_full(self):
        self.assertNotEqual(mb._ledger_name(True), mb._ledger_name(False))


class ProcessTest(unittest.TestCase):

    TASK = {"slug": "x-entry", "state": "rv-01_checked", "zh_doc": "x/x-entry.md"}

    def _run(self, events, eval_result, apply=True):
        written = []
        with mock.patch.object(mb, "_load_task", return_value=self.TASK), \
                mock.patch.object(mb, "read_events", return_value=events), \
                mock.patch.object(mb, "eval_node", side_effect=eval_result), \
                mock.patch.object(mb, "append_event", side_effect=lambda s, e: written.append(e)):
            rec = mb.process("x-entry", apply=apply, gate_version="gv", ledger_name="led.json")
        return rec, written

    def test_existing_pass_is_not_rewritten(self):
        rec, written = self._run([{"type": "pass", "node": "s0"}],  # 历史旧名须经别名归一（ADR-0080）
                                 lambda s, z, n: (True, ["x"], ""))
        self.assertEqual(rec["nodes"]["ex-04"]["status"], "already-pass")
        self.assertEqual([e["node"] for e in written], ["rv-01", "rv-02"])

    def test_fail_stops_downstream_and_records_reason(self):
        rec, written = self._run(
            [], lambda s, z, n: (n != "rv-01", ["g:%s" % n], "boom" if n == "rv-01" else ""))
        self.assertEqual(rec["nodes"]["ex-04"]["status"], "pass")
        self.assertEqual(rec["nodes"]["rv-01"]["status"], "fail")
        self.assertEqual(rec["nodes"]["rv-02"]["status"], "skipped-after-fail")
        fails = [e for e in written if e["type"] == "fail"]
        self.assertEqual(len(fails), 1)
        self.assertEqual(fails[0]["node"], "rv-01")
        self.assertTrue(fails[0]["reason"])

    def test_pass_event_carries_nonempty_gate_and_witness(self):
        rec, written = self._run([], lambda s, z, n: (True, ["g:%s" % n], ""))
        self.assertEqual(len(written), 3)
        for ev in written:
            self.assertEqual(ev["type"], "pass")
            self.assertTrue(ev["gate"], "schema 要求 gate 非空")
            self.assertEqual(ev["gate_version"], "gv")
            self.assertIn("led.json#x-entry:%s" % ev["node"], ev["witness"])
            self.assertTrue(ev["note"].startswith("backfill:"))

    def test_dry_run_writes_nothing(self):
        rec, written = self._run([], lambda s, z, n: (True, ["g:%s" % n], ""), apply=False)
        self.assertEqual(written, [])
        self.assertEqual(rec["nodes"]["rv-02"]["status"], "pass")

    def test_missing_zh_doc_fails_loudly(self):
        task = {"slug": "y-entry", "state": "rv-01_checked", "zh_doc": ""}
        written = []
        with mock.patch.object(mb, "_load_task", return_value=task), \
                mock.patch.object(mb, "read_events", return_value=[]), \
                mock.patch.object(mb, "eval_node") as ev, \
                mock.patch.object(mb, "append_event", side_effect=lambda s, e: written.append(e)):
            rec = mb.process("y-entry", apply=True, gate_version="gv", ledger_name="led.json")
        ev.assert_not_called()
        self.assertEqual(rec["nodes"]["ex-04"]["status"], "fail")


if __name__ == "__main__":
    unittest.main()
