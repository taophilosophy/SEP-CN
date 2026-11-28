# -*- coding: utf-8 -*-
"""TBX Core 导出单测（ADR-0086 §10.6）。"""
import os
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, REPO)

from tools import term_tbx  # noqa: E402

REG = """| 键 | 原文 | 译法 | 首现 | 依据 | 裁定日期 |
| --- | --- | --- | --- | --- | --- |
| 此在 | Dasein | 此在 | a/x | ADR | 2026-12-01 |
| 旧词 | old | 旧词 | a/y | ADR | 2026-11-01 |
| 专名 | — | 专名 | a/z | ADR | 2026-11-01 |
"""

CON = """| 键 | 定义 | 学科域 | 概念关系 | 依据 | 裁定日期 |
| --- | --- | --- | --- | --- | --- |
| 此在 | 存在的方式 | 本体论 | 相关：存在 | ADR | 2026-12-01 |
"""


class TestTermTbx(unittest.TestCase):
    def _write(self, text):
        f = tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8")
        f.write(text)
        f.close()
        self.addCleanup(os.unlink, f.name)
        return f.name

    def _items(self, reg=REG, con=CON):
        return term_tbx.concepts(term_tbx.rows(self._write(reg)),
                                 term_tbx.rows(self._write(con)))

    def test_terms_and_descrips(self):
        root = ET.fromstring(term_tbx.render(self._items()))
        ns = {"t": term_tbx.NS}
        entries = root.findall(".//t:conceptEntry", ns)
        self.assertEqual(len(entries), 3)
        terms = [t.text for t in root.findall(".//t:term", ns)]
        self.assertIn("Dasein", terms)
        self.assertIn("此在", terms)
        self.assertIn("存在的方式", [d.text for d in root.findall(".//t:descrip", ns)])
        self.assertIn("本体论", [d.text for d in root.findall(".//t:descrip", ns)])

    def test_sorted_and_deterministic(self):
        a = term_tbx.render(self._items())
        self.assertEqual(a, term_tbx.render(self._items()))
        zh = [t.text for t in ET.fromstring(a).iter("{urn:iso:std:iso:30042:ed-2}term")
              if t.text in ("此在", "旧词", "专名")]
        self.assertEqual(zh, sorted(zh))  # 码点序：专名 < 旧词 < 此在

    def test_dash_source_omits_en_term(self):
        root = ET.fromstring(term_tbx.render(self._items()))
        ns = {"t": term_tbx.NS}
        entry = [e for e in root.findall(".//t:conceptEntry", ns)
                 if "专名" in [x.text for x in e.findall(".//t:term", ns)]][0]
        langs = [s.get("{http://www.w3.org/XML/1998/namespace}lang")
                 for s in entry.findall("t:langSec", ns)]
        self.assertEqual(langs, ["zh-Hans"])

    def test_escaping(self):
        reg = REG.replace("Dasein", "Dasein & <sein>")
        text = term_tbx.render(self._items(reg=reg))
        ET.fromstring(text)  # 良构
        self.assertIn("&amp;", text)

    def test_repeated_section_header_skipped(self):
        reg = REG + """| 键 | 原文 | 译法 | 首现 | 依据 | 裁定日期 |
| --- | --- | --- | --- | --- | --- |
| 新键 | neu | 新 | a/n | ADR | 2026-12-02 |
"""
        items = self._items(reg=reg)
        self.assertEqual([r["key"] for r in items], sorted(["此在", "旧词", "专名", "新键"]))

    def test_duplicate_key_rejected(self):
        reg = REG + "| 此在 | again | 再 | a/w | ADR | 2026-12-02 |\n"
        with self.assertRaises(ValueError):
            self._items(reg=reg)

    def test_id_unique_after_sanitize(self):
        reg = """| 键 | 原文 | 译法 | 首现 | 依据 | 裁定日期 |
| --- | --- | --- | --- | --- | --- |
| a b | x | X | a | ADR | 2026-12-01 |
| a/b | y | Y | a | ADR | 2026-12-01 |
"""
        items = self._items(reg=reg, con="")
        root = ET.fromstring(term_tbx.render(items))
        ids = [e.get("id") for e in root.iter("{urn:iso:std:iso:30042:ed-2}conceptEntry")]
        self.assertEqual(len(ids), len(set(ids)))

    def test_schema_fields_and_roundtrip(self):
        reg = """| 键 | 原文 | 译法 | 首现 | 依据 | 裁定日期 |
| --- | --- | --- | --- | --- | --- |
| 此在 | Dasein | 此在 | a/x | ADR | 2026-12-01 |
"""
        name = """| 原文 | 别名 | 译法 | 籍属 | 生卒 | 首现 | 依据 | 裁定日期 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Ayer | — | 艾耶尔 | 英国 | 1910–1989 | a/y | ADR | 2026-12-01 |
"""
        items = term_tbx.migrate_items(term_tbx.layout_rows(self._write(reg)), [],
                                      term_tbx.layout_rows(self._write(name)), limit=1)
        text = term_tbx.render(items)
        for token in ("subjectField", "definition", "status", "date", "owner", "view"):
            self.assertIn('type="%s"' % token, text)
        path = self._write("")
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
        parsed = term_tbx.parse_tbx(path)
        self.assertEqual(len(parsed), 2)
        self.assertEqual(term_tbx.validate(parsed)["errors"], [])
        self.assertIn("| 此在 | Dasein | 此在 |", term_tbx.render_view(parsed, "shu-yu"))
        self.assertIn("| Ayer | — | 艾耶尔 |", term_tbx.render_view(parsed, "ren-ming"))

    def test_validate_rejects_structural_errors(self):
        good = term_tbx._base("k", "en", "zh", status="current",
                              date="2026-12-01", owner="术语员", view="shu-yu")
        good["id"] = "k"
        self.assertEqual(term_tbx.validate([good])["errors"], [])
        bad_status = dict(good, status="obsolete")
        self.assertTrue(term_tbx.validate([bad_status])["errors"])
        bad_date = dict(good, date="2026/12/01")
        self.assertTrue(term_tbx.validate([bad_date])["errors"])
        no_term = dict(good, source="", target="")
        self.assertTrue(term_tbx.validate([no_term])["errors"])
        dup = [dict(good), dict(good)]
        self.assertTrue(term_tbx.validate(dup)["errors"])

    def test_repo_sample_validates(self):
        path = os.path.join(term_tbx.ROOT, "baseline", "termbase-sample.tbx")
        self.assertTrue(os.path.exists(path))
        result = term_tbx.validate(term_tbx.parse_tbx(path))
        self.assertEqual(result["errors"], [])
        self.assertGreaterEqual(result["count"], 10)


if __name__ == "__main__":
    unittest.main()
