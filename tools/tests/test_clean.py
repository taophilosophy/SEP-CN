# -*- coding: utf-8 -*-
"""clean.py 契约单测（T020/T021）：只读档、strict、垃圾目录识别与删除。"""
import os
import sys
import tempfile
import unittest
from unittest import mock

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, REPO)

from tools import clean  # noqa: E402


class JunkClassifyTest(unittest.TestCase):
    def test_junk_dirs(self):
        self.assertTrue(clean.is_junk_dir("target", "target"))
        self.assertTrue(clean.is_junk_dir("sep-core/target", "target"))
        self.assertTrue(clean.is_junk_dir(".vitepress/cache", "cache"))
        self.assertTrue(clean.is_junk_dir(".vitepress/dist", "dist"))
        self.assertTrue(clean.is_junk_dir("tools/__pycache__", "__pycache__"))
        self.assertTrue(clean.is_junk_dir(".pytest_cache", ".pytest_cache"))
        self.assertTrue(clean.is_junk_dir(".mypy_cache", ".mypy_cache"))
        self.assertTrue(clean.is_junk_dir(".ruff_cache", ".ruff_cache"))
        self.assertTrue(clean.is_junk_dir(".screenshots", ".screenshots"))
        self.assertFalse(clean.is_junk_dir("src/cache", "cache"))

    def test_junk_files(self):
        self.assertTrue(clean.is_junk_file("state/a.tmp", "a.tmp"))
        self.assertTrue(clean.is_junk_file("tools/x.pyc", "x.pyc"))
        self.assertTrue(clean.is_junk_file(".vitepress/cache/x", "x"))
        self.assertFalse(clean.is_junk_file("state/keep.txt", "keep.txt"))


class CollectTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = self.tmp.name
        os.makedirs(os.path.join(self.root, "en"))
        os.makedirs(os.path.join(self.root, "yuanwen"))
        os.makedirs(os.path.join(self.root, "baseline"))
        os.makedirs(os.path.join(self.root, "state"))
        os.makedirs(os.path.join(self.root, "tools", "__pycache__"))
        os.makedirs(os.path.join(self.root, "target"))
        os.makedirs(os.path.join(self.root, ".vitepress", "cache"))
        for rel in ("en/index.html", "yuanwen/x.md", "baseline/pin.json",
                    "SUMMARY.md", "keep.txt"):
            path = os.path.join(self.root, rel)
            os.makedirs(os.path.dirname(path), exist_ok=True)
            open(path, "w", encoding="utf-8").close()
        for rel in ("state/a.tmp", "tools/__pycache__/x.pyc",
                    "target/out.o", ".vitepress/cache/data"):
            open(os.path.join(self.root, rel), "w", encoding="utf-8").close()

    def tearDown(self):
        self.tmp.cleanup()

    def test_collect_prunes_junk_dirs_and_keeps_tracked(self):
        tracked = {"en/index.html", "yuanwen/x.md", "baseline/pin.json",
                   "SUMMARY.md", "keep.txt"}
        with mock.patch.object(clean, "ROOT", self.root):
            targets = clean.collect(tracked)
        rels = {rel for _, rel, _ in targets}
        self.assertIn("state/a.tmp", rels)
        self.assertIn("tools/__pycache__", rels)
        self.assertIn("target", rels)
        self.assertIn(".vitepress/cache", rels)
        self.assertNotIn("keep.txt", rels)
        self.assertNotIn("en/index.html", rels)
        kinds = {rel: kind for _, rel, kind in targets}
        self.assertEqual(kinds["target"], "dir")
        self.assertEqual(kinds["state/a.tmp"], "file")

    def test_delete_removes_only_targets(self):
        tracked = {"en/index.html", "yuanwen/x.md", "baseline/pin.json",
                   "SUMMARY.md", "keep.txt"}
        with mock.patch.object(clean, "ROOT", self.root):
            targets = clean.collect(tracked)
            failures = clean.delete(targets)
        self.assertEqual(failures, [])
        self.assertFalse(os.path.exists(os.path.join(self.root, "target")))
        self.assertFalse(os.path.exists(os.path.join(self.root, "state", "a.tmp")))
        self.assertTrue(os.path.exists(os.path.join(self.root, "keep.txt")))
        self.assertTrue(os.path.exists(os.path.join(self.root, "en", "index.html")))

    def test_protected_issues(self):
        with mock.patch.object(clean, "ROOT", self.root):
            self.assertEqual(clean.protected_issues([]), [])
        os.remove(os.path.join(self.root, "SUMMARY.md"))
        with mock.patch.object(clean, "ROOT", self.root):
            self.assertEqual(clean.protected_issues([]),
                             ["保护件缺失：SUMMARY.md"])


class MainContractTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = self.tmp.name
        for rel in ("en/x", "yuanwen/x", "baseline/x", "SUMMARY.md"):
            path = os.path.join(self.root, rel)
            os.makedirs(os.path.dirname(path), exist_ok=True)
            open(path, "w", encoding="utf-8").close()
        os.makedirs(os.path.join(self.root, "state"))
        open(os.path.join(self.root, "state", "a.tmp"), "w", encoding="utf-8").close()

    def tearDown(self):
        self.tmp.cleanup()

    def test_check_returns_zero_with_junk(self):
        with mock.patch.object(clean, "ROOT", self.root), \
                mock.patch.object(clean, "tracked_set", return_value=set()):
            self.assertEqual(clean.main(["--check"]), 0)

    def test_strict_missing_protected_returns_one(self):
        os.remove(os.path.join(self.root, "SUMMARY.md"))
        with mock.patch.object(clean, "ROOT", self.root), \
                mock.patch.object(clean, "tracked_set", return_value=set()):
            self.assertEqual(clean.main(["--check", "--strict"]), 1)

    def test_go_check_usage_error(self):
        with self.assertRaises(SystemExit) as ctx:
            clean.main(["--go", "--check"])
        self.assertEqual(ctx.exception.code, 2)


if __name__ == "__main__":
    unittest.main()
