# -*- coding: utf-8 -*-
"""T275–T280（G4）：六轴补正反例、边界与 Unicode。"""
import os
import sys
import tempfile
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, REPO)

from tools import (axis_lib as ax, cite_audit, grammar_audit, logic_audit,
                   measure_audit, punct_audit, register_audit)  # noqa: E402


def write(text, name="sample.md"):
    d = tempfile.mkdtemp()
    p = os.path.join(d, name)
    with open(p, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    return p


class CiteGapTest(unittest.TestCase):
    def test_clean_has_no_items(self):
        _slug, items = cite_audit.scan(write("# 样本\n\n正文没有引文。\n"))
        self.assertEqual(items, [])

    def test_inline_and_block(self):
        text = ("# 样本\n\n他说：“凡不可说的，应当沉默。”\n\n"
                "> 这是一段足够长的英文引文，用于引块候选测试。\n")
        _slug, items = cite_audit.scan(write(text))
        self.assertTrue(any(it["form"] == "inline" for it in items))
        self.assertTrue(any(it["form"] == "block" for it in items))

    def test_unicode_quotes(self):
        text = "# 样本\n\n“这是一段足够长的中文引文，用于 Unicode 引号测试。”\n"
        _slug, items = cite_audit.scan(write(text))
        self.assertTrue(items)


class LogicGapTest(unittest.TestCase):
    def test_operator_sentence(self):
        p = write("# 样本\n\n所有天鹅都是白的，但有些鸟不是。\n")
        rows = logic_audit.skeleton("logic", ax.read_doc(p))
        self.assertTrue(any(r["verdict"] == "pending" for r in rows))

    def test_trivial_sentence(self):
        p = write("# 样本\n\n他昨天去了图书馆。\n")
        rows = logic_audit.skeleton("triv", ax.read_doc(p))
        self.assertTrue(any(r["verdict"] == "trivial" for r in rows))

    def test_unicode_text(self):
        p = write("# 样本\n\n如果\u00a0下雨，那么地面会湿。\n")
        rows = logic_audit.skeleton("uni", ax.read_doc(p))
        self.assertTrue(rows)


class GrammarGapTest(unittest.TestCase):
    def test_mismatched_conjunction(self):
        p = write("# 样本\n\n无论天气如何，他也坚持出门。\n")
        _slug, issues = grammar_audit.scan(p)
        self.assertTrue(any(i["rule"] == "G-7" for i in issues))

    def test_clean_sentence(self):
        p = write("# 样本\n\n无论天气如何，他都坚持出门。\n")
        _slug, issues = grammar_audit.scan(p)
        self.assertFalse(any(i["rule"] == "G-7" for i in issues))

    def test_unicode_sentence(self):
        p = write("# 样本\n\n这次学习使我明白了“道理”二字。\n")
        _slug, issues = grammar_audit.scan(p)
        self.assertIsInstance(issues, list)


class RegisterGapTest(unittest.TestCase):
    def test_you_rejected(self):
        p = write("# 样本\n\n## 1. 节\n\n您认为此事可行。\n")
        _slug, data = register_audit.scan(p)
        self.assertTrue(any(i["rule"] == "R-f" for i in data["issues"]))

    def test_academic_ok(self):
        p = write("# 样本\n\n## 1. 节\n\n本文认为此说可行。\n")
        _slug, data = register_audit.scan(p)
        self.assertFalse(any(i["rule"] == "R-f" for i in data["issues"]))

    def test_unicode_ok(self):
        p = write("# 样本\n\n## 1. 节\n\n本文认为“此说”可行。\n")
        _slug, data = register_audit.scan(p)
        self.assertIsInstance(data["issues"], list)


class MeasureGapTest(unittest.TestCase):
    def test_missing_space(self):
        p = write("# 样本\n\n速度达到 5km。\n")
        _slug, data = measure_audit.scan(p)
        self.assertIn("M-2", {i["rule"] for i in data["issues"]})

    def test_with_space_ok(self):
        p = write("# 样本\n\n速度达到 5 km。\n")
        _slug, data = measure_audit.scan(p)
        self.assertNotIn("M-2", {i["rule"] for i in data["issues"]})

    def test_unicode_digits(self):
        p = write("# 样本\n\n速度达到 ５km。\n")
        _slug, data = measure_audit.scan(p)
        self.assertIsInstance(data["issues"], list)


class PunctGapTest(unittest.TestCase):
    def test_ascii_quote_and_ellipsis(self):
        p = write('# 样本\n\n他说"好"，然后走了...\n')
        _slug, data = punct_audit.scan(p)
        rules = {i["rule"] for i in data["issues"]}
        self.assertIn("P-8", rules)
        self.assertIn("P-11", rules)

    def test_apostrophe_ok(self):
        p = write("# 样本\n\ndon't 与 O'Brien 的撇号不是引号。\n")
        _slug, data = punct_audit.scan(p)
        self.assertNotIn("P-8", {i["rule"] for i in data["issues"]})

    def test_paragraph_break_quote_ok(self):
        p = write("# 样本\n\n“甲段。”\n\n“乙段。”\n")
        _slug, data = punct_audit.scan(p)
        self.assertNotIn("P-18", {i["rule"] for i in data["issues"]})


if __name__ == "__main__":
    unittest.main()
