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
               before="a line", after="d line", origin="upstream-typo"):
    head = [
        "# id: %s" % pid,
        "# slug: %s" % slug,
        "# file: %s" % file_rel,
        "# expect: %d" % expect,
        "# category: 格式层（空格）",
        "# origin: %s" % origin,
        "# source: en-errata.md §九",
        "--- a/%s" % file_rel,
        "+++ b/%s" % file_rel,
        "@@ -1,3 +1,3 @@",
    ]
    return "\n".join(head + [" " + before, "-" + old, "+" + new, " " + after]) + "\n"


class TestOrigin(unittest.TestCase):
    """ADR-0085：补丁出处二分类必填且值域受限。"""

    def test_origin_parsed(self):
        p = en_patch_lib.parse_patch_text(patch_text(origin="converter-gap"))
        self.assertEqual(p["origin"], "converter-gap")

    def test_origin_missing_rejected(self):
        txt = patch_text().replace("# origin: upstream-typo\n", "")
        with self.assertRaises(ValueError):
            en_patch_lib.parse_patch_text(txt)

    def test_origin_bad_value_rejected(self):
        with self.assertRaises(ValueError):
            en_patch_lib.parse_patch_text(patch_text(origin="whatever"))


class TestPublicProbe(unittest.TestCase):
    """公共性探针：变更核心 token 的跨件命中（候选升档信号）。"""

    def test_probe_key_extracts_glued_token(self):
        self.assertEqual(
            check_en_patches.probe_key("b Einstein1949b c", "b Einstein 1949b c"),
            "Einstein1949b")

    def test_probe_key_markup_diff_returns_none(self):
        self.assertIsNone(
            check_en_patches.probe_key("x <div>", "x </div>"))

    def test_public_hits_counts_files(self):
        with tempfile.TemporaryDirectory() as td:
            for slug, body in (("a", "x Einstein1949b y"), ("b", "no hit"),
                               ("c", "x Einstein1949b y")):
                os.makedirs(os.path.join(td, slug))
                with open(os.path.join(td, slug, "index.html"), "w", encoding="utf-8") as f:
                    f.write(body)
            hits = check_en_patches.public_hits(["Einstein1949b"], en_root=td)
            self.assertEqual(hits["Einstein1949b"], {"a", "c"})


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
