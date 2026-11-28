# -*- coding: utf-8 -*-
"""T273（G4）：check_tables_images 规则正反例。"""
import os
import sys
import tempfile
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, REPO)

from tools import check_tables_images as cti  # noqa: E402


def scan(text, name="slug.md"):
    d = tempfile.mkdtemp()
    p = os.path.join(d, name)
    with open(p, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    return p, cti.check_file(p)


def rules(text):
    _p, issues = scan(text)
    return [r for _ln, r, _d in issues]


class TableShapeTest(unittest.TestCase):
    def test_aligned_ok(self):
        text = "| 甲 | 乙 |\n| --- | --- |\n| 一 | 二 |\n"
        self.assertNotIn("table-cols", rules(text))
        self.assertNotIn("table-no-sep", rules(text))

    def test_col_mismatch_rejected(self):
        text = "| 甲 | 乙 |\n| --- | --- |\n| 一 | 二 | 三 |\n"
        self.assertIn("table-cols", rules(text))

    def test_missing_separator_rejected(self):
        text = "| 甲 | 乙 |\n| 一 | 二 |\n"
        self.assertIn("table-no-sep", rules(text))


class TableStyleTest(unittest.TestCase):
    def test_fullwidth_space_rejected(self):
        text = "| 甲 | 乙 |\n| --- | --- |\n| 一\u3000 | 二 |\n"
        self.assertIn("table-fullwidth", rules(text))

    def test_compact_padding_rejected(self):
        text = "| 甲 | 乙 |\n| --- | --- |\n| 一  | 二 |\n"
        self.assertIn("table-compact", rules(text))

    def test_single_space_ok(self):
        text = "| 甲 | 乙 |\n| --- | --- |\n| 一 | 二 |\n"
        self.assertNotIn("table-compact", rules(text))

    def test_academic_tools_table_rejected(self):
        text = "## 学术工具\n\n| 甲 | 乙 |\n| --- | --- |\n| 一 | 二 |\n"
        self.assertIn("academic-table", rules(text))

    def test_academic_tools_list_ok(self):
        text = "## 学术工具\n\n* [如何引用](https://example.org)。\n"
        self.assertNotIn("academic-table", rules(text))

    def test_english_cell_candidate(self):
        text = ("| Term | Definition |\n| --- | --- |\n"
                "| one two three four | five six seven eight |\n")
        self.assertIn("table-en-prose", rules(text))

    def test_chinese_cell_ok(self):
        text = "| 甲 | 乙 |\n| --- | --- |\n| 一二三四 | 二 |\n"
        self.assertNotIn("table-en-prose", rules(text))


class ImageTest(unittest.TestCase):
    def _scan(self, text, make_asset=False):
        d = tempfile.mkdtemp()
        p = os.path.join(d, "slug.md")
        if make_asset:
            rel = "../assets/x.png"
            ap = os.path.normpath(os.path.join(d, rel))
            os.makedirs(os.path.dirname(ap), exist_ok=True)
            open(ap, "wb").close()
        with open(p, "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
        return cti.check_file(p)

    def test_alt_chinese_ok(self):
        issues = self._scan("![图](../assets/x.png)\n", make_asset=True)
        self.assertNotIn("alt-lang", [r for _l, r, _d in issues])

    def test_alt_english_rejected(self):
        issues = self._scan("![cat](../assets/x.png)\n", make_asset=True)
        self.assertIn("alt-lang", [r for _l, r, _d in issues])

    def test_img_base_rejected(self):
        issues = self._scan("![图](x.png)\n")
        self.assertIn("img-base", [r for _l, r, _d in issues])

    def test_img_resolve_rejected(self):
        issues = self._scan("![图](../assets/missing.png)\n")
        self.assertIn("img-resolve", [r for _l, r, _d in issues])

    def test_img_resolve_ok(self):
        issues = self._scan("![图](../assets/x.png)\n", make_asset=True)
        self.assertNotIn("img-resolve", [r for _l, r, _d in issues])


if __name__ == "__main__":
    unittest.main()
