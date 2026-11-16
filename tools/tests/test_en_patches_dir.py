# -*- coding: utf-8 -*-
"""补丁池目录正本单测（ADR-0062/0063，2026-11-16 目录化裁定）。

覆盖：正本解析、字段校验、准入谓词、行锚定应用与硬失败、INDEX 一致性、
目录体检端到端。

跑法: python -m unittest tools.tests.test_en_patches_dir -v
"""
import contextlib
import hashlib
import io
import json
import os
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "tools"))

import yuanwen  # noqa: E402
from tools import en_patch_lib  # noqa: E402
from tools import check_en_patches  # noqa: E402


def patch_text(pid="P-900", slug="demo", file_rel="en/demo/index.html", expect=1,
               old="b Einstein1949b c", new="b Einstein 1949b c",
               before="a line", after="d line"):
    head = [
        "# id: %s" % pid,
        "# slug: %s" % slug,
        "# file: %s" % file_rel,
        "# expect: %d" % expect,
        "# category: 格式层（空格）",
        "# source: en-errata.md §九",
        "--- a/%s" % file_rel,
        "+++ b/%s" % file_rel,
        "@@ -1,3 +1,3 @@",
    ]
    return "\n".join(head + [" " + before, "-" + old, "+" + new, " " + after]) + "\n"


class TestParse(unittest.TestCase):
    def test_fields(self):
        p = en_patch_lib.parse_patch_text(patch_text())
        self.assertEqual(p["id"], "P-900")
        self.assertEqual(p["slug"], "demo")
        self.assertEqual(p["expect"], 1)
        self.assertEqual(p["find"], "b Einstein1949b c")
        self.assertEqual(p["replace"], "b Einstein 1949b c")
        self.assertEqual(p["context"], ["a line", "d line"])

    def test_multi_minus_rejected(self):
        text = patch_text() + "-second removed line\n"
        with self.assertRaises(ValueError):
            en_patch_lib.parse_patch_text(text)

    def test_missing_field_rejected(self):
        text = patch_text().replace("# source: en-errata.md §九\n", "")
        with self.assertRaises(ValueError):
            en_patch_lib.parse_patch_text(text)


class TestAdmission(unittest.TestCase):
    def test_blank(self):
        self.assertEqual(en_patch_lib.admission("a1949b", "a 1949b"), "blank")

    def test_tag(self):
        self.assertEqual(en_patch_lib.admission("<p>x", "</p>\n<p>x"), "tag")

    def test_text_layer(self):
        self.assertIsNone(en_patch_lib.admission("Teubener", "Teubner"))


class TestApply(unittest.TestCase):
    def setUp(self):
        self.p = en_patch_lib.parse_patch_text(patch_text())

    def tearDown(self):
        yuanwen._EN_PATCH_CACHE = None

    def test_applies_and_replaces(self):
        yuanwen._EN_PATCH_CACHE = {"demo": [self.p]}
        html = "x\na line\nb Einstein1949b c\nd line\nz"
        out = yuanwen.apply_en_patches("demo", html)
        self.assertIn("Einstein 1949b", out)
        self.assertNotIn("Einstein1949b", out)

    def test_mismatch_raises(self):
        yuanwen._EN_PATCH_CACHE = {"demo": [self.p]}
        with self.assertRaises(yuanwen.PatchMismatch):
            yuanwen.apply_en_patches("demo", "no such line here")

    def test_context_missing_raises(self):
        yuanwen._EN_PATCH_CACHE = {"demo": [self.p]}
        with self.assertRaises(yuanwen.PatchMismatch):
            yuanwen.apply_en_patches("demo", "b Einstein1949b c")


class TestRealPool(unittest.TestCase):
    def test_load_real_dir(self):
        patches = en_patch_lib.load_patches()
        self.assertGreaterEqual(len(patches), 3)
        seen = set()
        for slug, items in patches.items():
            for p in items:
                seen.add(p["id"])
                self.assertTrue(p["patch_file"].startswith("baseline/en-patches/"))
                self.assertEqual(p["slug"], slug)
                self.assertIsNotNone(en_patch_lib.admission(p["find"], p["replace"]),
                                     "池内补丁 %s 应过准入谓词" % p["id"])
        self.assertIn("P-001", seen)
        self.assertIn("P-003", seen)

    def test_checker_strict_green(self):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = check_en_patches.main(["--strict", "--no-git-check"])
        self.assertEqual(rc, 0, buf.getvalue())
        self.assertIn('"mismatch": 0', buf.getvalue())


class TestIndex(unittest.TestCase):
    def test_consistency_and_tamper(self):
        with tempfile.TemporaryDirectory() as d:
            body = patch_text()
            path = os.path.join(d, "P-900.patch")
            with open(path, "w", encoding="utf-8", newline="\n") as f:
                f.write(body)
            idx = {"schema": "sep-cn-en-patches-dir/1", "count": 1, "patches": [
                {"id": "P-900", "slug": "demo", "file": "en/demo/index.html",
                 "expect": 1, "category": "格式层（空格）", "source": "x",
                 "patch": "baseline/en-patches/P-900.patch",
                 "sha256": hashlib.sha256(body.encode("utf-8")).hexdigest()}]}
            with open(os.path.join(d, "INDEX.json"), "w", encoding="utf-8", newline="\n") as f:
                f.write(json.dumps(idx, ensure_ascii=False))
            self.assertEqual(check_en_patches._index_issues(d), [])
            with open(path, "a", encoding="utf-8", newline="\n") as f:
                f.write("\n")
            issues = check_en_patches._index_issues(d)
            self.assertTrue(any("sha256" in m for m in issues), issues)

    def test_index_missing(self):
        with tempfile.TemporaryDirectory() as d:
            self.assertTrue(check_en_patches._index_issues(d))


if __name__ == "__main__":
    unittest.main()
