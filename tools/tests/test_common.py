# -*- coding: utf-8 -*-
"""金样本测试：common 写后自校验、parser 标记契约、extract 确定性。"""
import json
import os
import sys
import tempfile
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, REPO)

from tools.common import read_text, sha256_file, write_json_verified, write_text  # noqa: E402
from tools import parser  # noqa: E402

FIX = os.path.join(REPO, "tools", "tests", "fixtures")


def fix(name):
    with open(os.path.join(FIX, name), "rb") as f:
        return f.read().decode("utf-8", "replace")


class TestCommon(unittest.TestCase):
    def test_write_json_verified_roundtrip(self):
        with tempfile.TemporaryDirectory() as d:
            p = os.path.join(d, "x.json")
            sha = write_json_verified(p, {"a": "中文", "b": [1, 2]})
            self.assertEqual(sha, sha256_file(p))
            self.assertEqual(load(p)["a"], "中文")

    def test_write_text_lf_utf8(self):
        with tempfile.TemporaryDirectory() as d:
            p = os.path.join(d, "x.md")
            write_text(p, "中文\r\n英文\r\n")
            raw = open(p, "rb").read()
            self.assertFalse(raw.startswith(b"\xef\xbb\xbf"))
            self.assertNotIn(b"\r", raw)


def load(p):
    with open(p, "rb") as f:
        return json.loads(f.read().decode("utf-8"))


class TestParser(unittest.TestCase):
    def test_set_theory_supplement_and_pubinfo(self):
        e = parser.parse_entry(fix("entry-set-theory.html"))
        self.assertTrue(e["in_article_markers"])
        self.assertIn("basic-set-theory.html", e["supplements"])
        pub = [b for b in e["blocks"] if b["type"] == "pubinfo"]
        self.assertEqual(len(pub), 1)
        self.assertIsNotNone(pub[0]["first_published"])
        h2 = [b for b in e["blocks"] if b["type"] == "h2"]
        self.assertGreater(len(h2), 10)

    def test_bayes_notes_refs_and_tables(self):
        e = parser.parse_entry(fix("entry-bayes-theorem.html"))
        self.assertGreaterEqual(len(e["notes_refs"]), 16)
        tables = [b for b in e["blocks"] if b["type"] == "table"]
        self.assertGreaterEqual(len(tables), 3)  # 文内独立表格（侧栏表格不在正文范围内）

    def test_bell_figures(self):
        e = parser.parse_entry(fix("entry-bell-theorem.html"))
        imgs = [b for b in e["blocks"] if b["type"] == "img"]
        srcs = [i["src"] for i in imgs]
        self.assertIn("image1.jpg", srcs)
        labelled = [i for i in imgs if i.get("figlabel")]
        self.assertTrue(any("Figure 1" in i["figlabel"] for i in labelled),
                        "figlabel 未归并: %r" % [i.get("figlabel") for i in imgs])

    def test_anaxagoras_pubinfo_dates(self):
        e = parser.parse_entry(fix("arch-anaxagoras-fall2026.html"))
        pub = [b for b in e["blocks"] if b["type"] == "pubinfo"][0]
        self.assertEqual(pub["first_published"], "Aug 22, 2007")
        self.assertEqual(pub["substantive_revision"], "Aug 9, 2026")

    def test_logic_classical_math_density(self):
        e = parser.parse_entry(fix("entry-logic-classical.html"))
        text = " ".join(b.get("text", "") for b in e["blocks"])
        self.assertGreater(text.count("\\("), 1000)

    def test_archinfo_parse(self):
        ai = parser.parse_archinfo(fix("archinfo-anaxagoras.html"))
        self.assertEqual(ai["latest_edition"], "Fall 2026")
        self.assertTrue(any(h["edition"] == "Winter 2019" for h in ai["history"]))


class TestExtract(unittest.TestCase):
    def test_deterministic(self):
        from tools.extract_text import render_blocks
        e1 = parser.parse_entry(fix("entry-quine.html"))
        e2 = parser.parse_entry(fix("entry-quine.html"))
        self.assertEqual(render_blocks(e1), render_blocks(e2))

    def test_entities_decoded_math_preserved(self):
        from tools.extract_text import render_blocks
        e = parser.parse_entry(fix("entry-set-theory.html"))
        out = render_blocks(e)
        self.assertNotIn("&mdash;", out)
        self.assertIn("\\(", out)


if __name__ == "__main__":
    unittest.main()

class TestCatalog(unittest.TestCase):
    def test_catalog_parse(self):
        """目录解析：正常词条/别名/子词条三类都要识别（演示轮 1 教训：
        parse_catalog 曾无测试覆盖，<strong> 包裹导致 547 条全误判）。"""
        import glob
        cats = sorted(glob.glob(os.path.join(REPO, "en", "_catalog", "*-contents.html")))
        if not cats:
            self.skipTest("no catalog snapshot")
        with open(cats[-1], "rb") as f:
            html = f.read().decode("utf-8", "replace")
        items = parser.parse_catalog(html)
        normal = [i for i in items if not i["alias_of"]]
        # 别名总数 = 独立别名记录 + 并入正常记录的 aliases 词数（演示轮 1 修订后的归并模型）
        alias = sum(len(i.get("aliases", [])) for i in items)             + len([i for i in items if i["alias_of"]])
        self.assertGreater(len(normal), 1400, "正常词条数异常: %d" % len(normal))  # 实测 1460
        self.assertGreater(alias, 300, "别名词条数异常: %d" % alias)  # 实测 348（85 独立 + 263 并入）
        by = {i["slug"]: i for i in items}
        self.assertFalse(by["abduction"]["alias_of"])
        self.assertEqual(by["abduction"]["authors"], "Igor Douven")
        # akrasia 是别名词，应并入目标 weakness-will 的 aliases
        self.assertIn("akrasia", by["weakness-will"].get("aliases", []))
