# -*- coding: utf-8 -*-
"""progress.py 的 W4 切读面单元测试：验证 load_journal 折叠与核心段完成判定。

不碰真实 journal/，用临时目录注入。核心断言：进度读数只认 journal 的 pass
事件，与 tasks 的 state 游标无关（ADR-0068 W4）。
"""
import json
import os
import tempfile
import unittest

from tools import progress


def _write_ndjson(dirpath, slug, events):
    letter = slug[0] if slug and slug[0].isalnum() else "0"
    sub = os.path.join(dirpath, letter)
    os.makedirs(sub, exist_ok=True)
    path = os.path.join(sub, slug + ".ndjson")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        for e in events:
            f.write(json.dumps(e, ensure_ascii=False) + "\n")


class TestLoadJournal(unittest.TestCase):
    def setUp(self):
        self._dir = tempfile.TemporaryDirectory()

    def tearDown(self):
        self._dir.cleanup()

    def test_core_done_folds_pass_set(self):
        # 一个走完全核心段、一个只到 s1
        _write_ndjson(self._dir.name, "a-full", [
            {"type": "lock", "sha256": "0" * 64},
            {"type": "pass", "node": "draft"},
            {"type": "pass", "node": "s1"},
            {"type": "pass", "node": "s2"},
            {"type": "pass", "node": "S3"},
            {"type": "pass", "node": "R1"},
            {"type": "pass", "node": "R2"},
            {"type": "pass", "node": "R3"},
        ])
        _write_ndjson(self._dir.name, "b-part", [
            {"type": "pass", "node": "draft"},
            {"type": "pass", "node": "s1"},
        ])
        _write_ndjson(self._dir.name, "c-idle", [
            {"type": "import", "synthetic": True, "basis": "state:pending"},
        ])

        passed, node_count = progress.load_journal(self._dir.name)

        self.assertEqual(set(passed), {"a-full", "b-part", "c-idle"})
        # a-full 核心段完成，b-part 在途，c-idle 未开工
        core_done = [s for s, d in passed.items() if progress.CORE <= d]
        self.assertEqual(core_done, ["a-full"])
        self.assertEqual(node_count.get("s1"), 2)
        self.assertEqual(node_count.get("R3"), 1)

    def test_empty_journal_returns_empty(self):
        passed, node_count = progress.load_journal(self._dir.name)
        self.assertEqual(passed, {})
        self.assertEqual(node_count, {})

    def test_ignore_non_pass_events(self):
        _write_ndjson(self._dir.name, "x-mixed", [
            {"type": "rework", "from_node": "s2.4"},
            {"type": "pass", "node": "draft"},
            {"type": "lock", "sha256": "1" * 64},
        ])
        passed, _ = progress.load_journal(self._dir.name)
        self.assertEqual(passed["x-mixed"], {"draft"})


if __name__ == "__main__":
    unittest.main()
