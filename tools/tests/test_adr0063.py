# -*- coding: utf-8 -*-
"""ADR-0063 工具单测：体例轴四则、补丁准入谓词、保真字符流。

跑法: python -m unittest tools.tests.test_adr0063 -v
"""
import json
import os
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "tools"))

from check_en_patches import admission  # noqa: E402
from check_pairs import (check_tail_order, check_heading_number, check_h1_form,  # noqa: E402
                         HARD_RULES)
from check_yuanwen_fidelity import multiset_diff, chars, digit_count  # noqa: E402


class TestPatchAdmission(unittest.TestCase):
    """C2 准入谓词（ADR-0063 决策 6）：空白差/标记差可入池，词符差禁入。"""

    def test_blank_diff_allowed(self):
        self.assertEqual(admission("Einstein1949b", "Einstein 1949b"), "blank")

    def test_tag_diff_allowed(self):
        self.assertEqual(admission('<div class="x">a', '</div>\n<div class="x">a'), "tag")

    def test_text_layer_rejected(self):
        self.assertIsNone(admission("Renthe-Fink", "von Renthe-Fink"))
        self.assertIsNone(admission("Teubener", "Teubner"))

    def test_real_pool_patches_pass(self):
        path = os.path.join(ROOT, "baseline", "en-patches.json")
        if not os.path.exists(path):
            # 池目录化（baseline/en-patches/）在途由并行会话改造，正本格式未定；
            # 谓词逻辑已由上三条合成用例覆盖，此处不依赖池文件布局。
            self.skipTest("补丁池正处目录化改造（baseline/en-patches/），本用例跳过")
        with open(path, encoding="utf-8") as f:
            pool = json.load(f)
        for p in pool["patches"]:
            self.assertIsNotNone(admission(p["find"], p["replace"]),
                                 "池内补丁 %s 应过准入谓词" % p["id"])


class TestTailOrder(unittest.TestCase):
    """尾节齐备与顺序 + 脚注末位（ADR-0063 判定表第一行）。"""

    def _run(self, text):
        issues = []
        check_tail_order("t.md", text, issues)
        return issues

    def test_canonical_ok(self):
        text = ("# 题\n\n正文\n\n## 1. 一\n\n## 参考文献\n\n## 学术工具\n\n"
                "## 其他网络资源\n\n## 相关词条\n")
        self.assertEqual(self._run(text), [])

    def test_missing_section(self):
        text = "# 题\n\n## 1. 一\n\n## 参考文献\n\n## 学术工具\n"
        issues = self._run(text)
        self.assertEqual(issues[0]["rule"], "tail-order")
        self.assertIn("相关词条", issues[0]["detail"])

    def test_footnote_must_be_last(self):
        text = ("# 题\n\n## 脚注\n\n## 参考文献\n\n## 学术工具\n\n"
                "## 其他网络资源\n\n## 相关词条\n")
        issues = self._run(text)
        self.assertTrue(any("末位" in i["detail"] for i in issues))


class TestHeadingNumber(unittest.TestCase):
    """编号点号式与跳号（ADR-0063 判定表第二行，用户裁定与原文一致）。"""

    def _run(self, text):
        issues = []
        check_heading_number("t.md", text, issues)
        return issues

    def test_dotted_ok(self):
        text = "## 1. 一\n\n### 1.1 子\n\n## 2. 二\n"
        self.assertEqual(self._run(text), [])

    def test_bare_number_rejected(self):
        issues = self._run("## 1 一\n")
        self.assertEqual(issues[0]["rule"], "heading-number")

    def test_skip_rejected(self):
        issues = self._run("## 1. 一\n\n## 3. 三\n")
        self.assertTrue(any("跳号" in i["detail"] for i in issues))

    def test_tail_sections_untouched(self):
        self.assertEqual(self._run("## 参考文献\n"), [])


class TestH1Form(unittest.TestCase):
    """H1 作者括号与英文题一致（ADR-0063 判定表第三行）。"""

    def test_with_author_ok(self):
        check_h1_form("t.md", "# 溯因 Abduction (Igor Douven)\n", [])  # 不新增

    def test_missing_author(self):
        issues = []
        check_h1_form("t.md", "# 溯因 Abduction\n", issues)
        self.assertEqual(issues[0]["rule"], "h1-form")

    def test_en_title_must_match_yuanwen(self):
        issues = []
        check_h1_form("t.md", "# 溯因 (Igor Douven)\n", issues,
                      yw_text="# Abduction\n")
        self.assertTrue(any("英文题" in i["detail"] for i in issues))


class TestHardRules(unittest.TestCase):
    def test_hard_rules_membership(self):
        for r in ("tail-order", "heading-number", "h1-form", "errata-apply", "pubinfo-form"):
            self.assertIn(r, HARD_RULES)


class TestFidelity(unittest.TestCase):
    """I3 字母多重集判据：移位合法、丢字叠字必现。"""

    def test_equal_after_reorder(self):
        a = "alpha beta gamma"
        b = "gamma beta alpha"
        self.assertIsNone(multiset_diff(a, b))

    def test_duplicate_title_detected(self):
        # 缺陷形态＝md 比源多出一份文字（30 件重复 H1 即此面）
        d = multiset_diff("Bertrand Russell preamble text",
                          "Bertrand Russell Bertrand Russell preamble text")
        self.assertIsNotNone(d)
        self.assertEqual(d["n_missing"], 0)
        self.assertGreater(d["n_extra"], 0)
        self.assertIn("Bertrand", d["words"])

    def test_dropped_word_detected(self):
        d = multiset_diff("the mean of the nature", "the mean of nature")
        self.assertIsNotNone(d)
        self.assertEqual(d["n_missing"], 3)  # 丢了 "the" 的三字母

    def test_superscript_forms_equivalent(self):
        # 数字化入软信号不入主判据：G₁ 与 G1 的字母流同为 ['G']
        self.assertEqual(chars("G₁"), chars("G1"))
        self.assertEqual(digit_count("G1"), 1)
        self.assertIsNone(multiset_diff("G1 model", "G₁ model"))

    def test_digit_count_soft_signal(self):
        self.assertEqual(digit_count("a1b22"), 3)

    def test_greek_letters_counted(self):
        self.assertEqual(len(chars("φψ")), 2)


if __name__ == "__main__":
    unittest.main()
