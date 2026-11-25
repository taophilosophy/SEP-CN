# -*- coding: utf-8 -*-
"""fetch_all 驱动器回归测试（2026-11-25 修复：线程数取法、unchanged 覆盖钉账）。"""
import os
import sys
import unittest
from queue import Queue
from unittest import mock

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from tools import fetch_all
from tools.fetch_entry import upsert_baseline


class TestConfigShape(unittest.TestCase):
    def test_configs_are_channel_counts(self):
        for k, v in fetch_all.CONFIGS.items():
            self.assertIsInstance(v, int, "CONFIGS[%s] 应为线程数（int）" % k)
            self.assertGreater(v, 0)


class TestUpsertGuard(unittest.TestCase):
    def test_unchanged_record_rejected(self):
        # fetch_one 的 unchanged 结果无 files；误交 upsert 会清空钉账字段。
        with self.assertRaises(ValueError):
            upsert_baseline({"slug": "x", "result": "unchanged"})


class TestWorkerUnchanged(unittest.TestCase):
    def test_unchanged_no_upsert(self):
        q = Queue()
        q.put("x")
        stats = {"done": 0, "failed": 0, "fetched": 0, "unchanged": 0,
                 "converted": 0, "fail": [], "conv_fail": [], "total": 1}
        with mock.patch.object(fetch_all, "fetch_one",
                               return_value={"slug": "x", "result": "unchanged"}), \
             mock.patch.object(fetch_all, "upsert_baseline") as up, \
             mock.patch.object(fetch_all, "_flog"), \
             mock.patch.object(fetch_all, "_checkpoint"):
            fetch_all.worker(q, 1, {"convert": False}, stats)
        up.assert_not_called()
        self.assertEqual(stats["unchanged"], 1)
        self.assertEqual(stats["done"], 1)
        self.assertEqual(stats["fetched"], 1)
        self.assertEqual(stats["failed"], 0)

    def test_changed_goes_through_upsert(self):
        q = Queue()
        q.put("y")
        stats = {"done": 0, "failed": 0, "fetched": 0, "unchanged": 0,
                 "converted": 0, "fail": [], "conv_fail": [], "total": 1}
        rec = {"slug": "y", "files": [{"path": "en/y/index.html", "sha256": "0" * 64}],
               "missing": []}
        with mock.patch.object(fetch_all, "fetch_one", return_value=rec), \
             mock.patch.object(fetch_all, "upsert_baseline") as up, \
             mock.patch.object(fetch_all, "_flog"), \
             mock.patch.object(fetch_all, "_checkpoint"):
            fetch_all.worker(q, 1, {"convert": False}, stats)
        up.assert_called_once_with(rec)
        self.assertEqual(stats["unchanged"], 0)
        self.assertEqual(stats["done"], 1)


if __name__ == "__main__":
    unittest.main()
