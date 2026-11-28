# -*- coding: utf-8 -*-
"""T272（G4）：check_pairs 全规则正反例。"""
import os
import sys
import tempfile
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, REPO)

from tools import check_pairs as cp  # noqa: E402


def _issues(fn, *args):
    out = []
    fn(*args, out)
    return out


class PubinfoFormTest(unittest.TestCase):
    def test_canonical_ok(self):
        self.assertEqual(_issues(cp.check_pubinfo, "x.md", 3,
                                 "> *首次发表于 2020 年 1 月 1 日。*"), [])

    def test_plain_text_rejected(self):
        out = _issues(cp.check_pubinfo, "x.md", 3, "首次发表于 2020 年 1 月 1 日。")
        self.assertTrue(any(i["rule"] == "pubinfo-form" for i in out))


class BracketPairTest(unittest.TestCase):
    def test_balanced_ok(self):
        self.assertEqual(_issues(cp.check_brackets, "x.md", 1, "文本（含括号）与《书名》。"), [])

    def test_right_before_left_rejected(self):
        out = _issues(cp.check_brackets, "x.md", 1, "文本）含括号（。")
        self.assertTrue(any(i["rule"] == "bracket-pair" for i in out))


class EllipsisFormTest(unittest.TestCase):
    def test_six_dots_ok(self):
        self.assertEqual(_issues(cp.check_ellipsis, "x.md", 1, "中文省略……完。"), [])

    def test_three_dots_rejected(self):
        out = _issues(cp.check_ellipsis, "x.md", 1, "中文省略...完。")
        self.assertTrue(any(i["rule"] == "ellipsis-form" for i in out))


class DanglingLinkTest(unittest.TestCase):
    def test_existing_target_ok(self):
        with tempfile.TemporaryDirectory() as d:
            open(os.path.join(d, "ok.md"), "w", encoding="utf-8").close()
            out = []
            cp.check_links("x.md", 1, "[链接](ok.md)", out, d)
            self.assertEqual(out, [])

    def test_missing_target_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            out = []
            cp.check_links("x.md", 1, "[链接](missing.md)", out, d)
            self.assertTrue(any(i["rule"] == "dangling-link" for i in out))


class AuthoryearTest(unittest.TestCase):
    def test_hit_ok(self):
        defs = [("k", "Smith, John, 2000, *Book*.")]
        out = []
        cp.check_authoryear("x.md", 1, "文本（Smith 2000）。", out, defs)
        self.assertEqual(out, [])

    def test_miss_rejected(self):
        defs = [("k", "Smith, John, 2000, *Book*.")]
        en = ("<h2>Bibliography</h2><ul><li>Jones, Ann, 1999, *Book*.</li></ul>")
        out = []
        cp.check_authoryear("x.md", 1, "文本（Jones 1999）。", out, defs, en)
        self.assertTrue(any(i["rule"] == "cite-authoryear" for i in out))


class BibDuplicateTest(unittest.TestCase):
    def test_unique_ok(self):
        ordered, dups = cp.extract_bib_defs(
            "[^a]: Smith 2000.\n[^b]: Jones 2001.\n")
        self.assertEqual(len(ordered), 2)
        self.assertEqual(dups, [])

    def test_duplicate_detected(self):
        ordered, dups = cp.extract_bib_defs(
            "[^a]: Smith 2000.\n[^a]: Smith 2000.\n")
        self.assertEqual(len(ordered), 2)
        self.assertEqual(dups, ["a"])


class CountVsSourceTest(unittest.TestCase):
    def _tree(self, d, zh_heads, en_heads):
        os.makedirs(os.path.join(d, "zh", "d"), exist_ok=True)
        os.makedirs(os.path.join(d, "en", "d"), exist_ok=True)
        os.makedirs(os.path.join(d, "html", "slug"), exist_ok=True)
        zh = "# 题\n\n" + "\n\n".join("## %d. 节" % n for n in range(1, zh_heads + 1)) + "\n"
        en = "# Title\n\n" + "\n".join("## %d. Sec" % n for n in range(1, en_heads + 1)) + "\n"
        hp = os.path.join(d, "html", "slug", "index.html")
        with open(hp, "w", encoding="utf-8") as f:
            f.write("<html>" + "".join("<h2>%d</h2>" % n for n in range(1, en_heads + 1)) + "</html>")
        p = os.path.join(d, "zh", "d", "slug.md")
        with open(p, "w", encoding="utf-8") as f:
            f.write(zh)
        with open(os.path.join(d, "en", "d", "slug.md"), "w", encoding="utf-8") as f:
            f.write(en)
        return p, zh

    def test_aligned_ok(self):
        with tempfile.TemporaryDirectory() as d:
            p, zh = self._tree(d, 3, 3)
            out = []
            cp.check_counts(p, "slug", zh, out)
            self.assertEqual(out, [])

    def test_mismatch_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            p, zh = self._tree(d, 2, 8)
            out = []
            cp.check_counts(p, "slug", zh, out)
            self.assertTrue(any(i["rule"] == "count-vs-source" for i in out))


class H1FormTest(unittest.TestCase):
    def test_author_ok(self):
        out = []
        cp.check_h1_form("x.md", "# 题 Title (A. Author)\n", out)
        self.assertEqual(out, [])

    def test_missing_author_rejected(self):
        out = []
        cp.check_h1_form("x.md", "# 题 Title\n", out)
        self.assertTrue(any(i["rule"] == "h1-form" for i in out))


if __name__ == "__main__":
    unittest.main()
