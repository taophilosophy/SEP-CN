# -*- coding: utf-8 -*-
"""divergence.py 分歧账核验核心单元测试（CI: unittest discover）。"""
import hashlib
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from tools.divergence import check_consistency

PIN = hashlib.sha256(b"upstream-bytes").hexdigest()
LOCAL = hashlib.sha256(b"upstream-bytes + errata").hexdigest()
OTHER = hashlib.sha256(b"something-else").hexdigest()

IDX = {"en/x/index.html": {"slug": "x", "sha256": PIN, "bytes": 14}}
DIV_OK = {"slug": "x", "path": "en/x/index.html", "upstream_sha256": PIN,
          "local_sha256": LOCAL, "base_commit": "abc123", "commit": "def456"}


def sha_of_factory(files):
    def sha_of(p):
        b = files.get(p)
        return hashlib.sha256(b).hexdigest() if b is not None else None
    return sha_of


class TestCheckConsistency(unittest.TestCase):
    def test_pristine_ok(self):
        s, f = check_consistency(IDX, [], sha_of_factory({"en/x/index.html": b"upstream-bytes"}))
        self.assertEqual((s["pristine"], s["divergent"]), (1, 0))
        self.assertEqual(f, [])

    def test_unregistered_divergence_fails(self):
        s, f = check_consistency(IDX, [], sha_of_factory({"en/x/index.html": b"upstream-bytes + errata"}))
        self.assertEqual(s["divergent"], 0)
        self.assertTrue(any("未登记分歧" in x["reason"] for x in f))

    def test_registered_divergence_ok(self):
        s, f = check_consistency(IDX, [DIV_OK],
                                 sha_of_factory({"en/x/index.html": b"upstream-bytes + errata"}))
        self.assertEqual((s["pristine"], s["divergent"]), (0, 1))
        self.assertEqual(f, [])

    def test_stale_upstream_pin(self):
        d = dict(DIV_OK, upstream_sha256=OTHER)
        s, f = check_consistency(IDX, [d],
                                 sha_of_factory({"en/x/index.html": b"upstream-bytes + errata"}))
        self.assertTrue(any("upstream_sha256 与台账钉不符" in x["reason"] for x in f))

    def test_stale_local_sha(self):
        d = dict(DIV_OK, local_sha256=OTHER)
        s, f = check_consistency(IDX, [d],
                                 sha_of_factory({"en/x/index.html": b"upstream-bytes + errata"}))
        self.assertTrue(any("local_sha256 与现文件不符" in x["reason"] for x in f))

    def test_divergence_obsolete_after_restore(self):
        s, f = check_consistency(IDX, [DIV_OK], sha_of_factory({"en/x/index.html": b"upstream-bytes"}))
        self.assertTrue(any("账已过时" in x["reason"] for x in f))

    def test_missing_file(self):
        s, f = check_consistency(IDX, [], sha_of_factory({}))
        self.assertTrue(any("文件缺失" in x["reason"] for x in f))

    def test_duplicate_registration(self):
        s, f = check_consistency(IDX, [DIV_OK, dict(DIV_OK)],
                                 sha_of_factory({"en/x/index.html": b"upstream-bytes + errata"}))
        self.assertTrue(any("重复登记" in x["reason"] for x in f))

    def test_missing_base_commit(self):
        d = dict(DIV_OK, base_commit=None)
        s, f = check_consistency(IDX, [d],
                                 sha_of_factory({"en/x/index.html": b"upstream-bytes + errata"}))
        self.assertTrue(any("缺 base_commit" in x["reason"] for x in f))

    def test_deep_blob_mismatch(self):
        s, f = check_consistency(IDX, [DIV_OK],
                                 sha_of_factory({"en/x/index.html": b"upstream-bytes + errata"}),
                                 deep=True, blob_sha=lambda c, p: OTHER)
        self.assertTrue(any("blob ≠ 原始钉" in x["reason"] for x in f))

    def test_deep_blob_unavailable(self):
        s, f = check_consistency(IDX, [DIV_OK],
                                 sha_of_factory({"en/x/index.html": b"upstream-bytes + errata"}),
                                 deep=True, blob_sha=lambda c, p: None)
        self.assertTrue(any("不可核" in x["reason"] for x in f))

    def test_unknown_divergence_path(self):
        d = dict(DIV_OK, path="en/ghost/index.html")
        s, f = check_consistency(IDX, [d], sha_of_factory({"en/x/index.html": b"upstream-bytes"}))
        self.assertTrue(any("不在 baseline" in x["reason"] for x in f))

    def test_missing_ledger(self):
        s, f = check_consistency(None, [], sha_of_factory({}))
        self.assertTrue(any("台账缺失" in x["reason"] for x in f))


if __name__ == "__main__":
    unittest.main()
