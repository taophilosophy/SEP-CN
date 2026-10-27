# -*- coding: utf-8 -*-
"""check_math 公式内容判定单元测试（CI: unittest discover）。"""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from tools.check_math import _content_present, classify_formula, raw_formulas

MD = r"""行内 $\pi r^2$ 与显示：

$$
E = mc^2
$$

脚注保留上游笔误：\(\iota x\forall F^n(F^n x \equiv B^n \Rightarrow F^n).
"""


class TestContentPresent(unittest.TestCase):
    def test_exact(self):
        self.assertTrue(_content_present(r"\pi r^2", MD))

    def test_multiline_norm(self):
        self.assertTrue(_content_present("E = mc^2", MD))

    def test_swallowed_markup_forgiven(self):
        # 贪婪抽取跨块吞入标签：截断到首个 '<' 后仍在产物 → 视为忠实
        inner = r"\iota x\forall F^n(F^n x \equiv B^n \Rightarrow F^n)." \
                "</p>  <div id=\"note-33\">  <p>   <a href=\"index.html\">"
        self.assertTrue(_content_present(inner, MD))

    def test_real_loss_still_flagged(self):
        self.assertFalse(_content_present(r"E = mc^3", MD))
        # 内容中途被转换器丢失时，截断重试也救不回
        inner = r"a \Rightarrow F^n).</p> <div>"
        self.assertFalse(_content_present(inner, r"产物里只有 $a \Rightarrow F$。"))

    def test_empty_head_not_forgiven(self):
        # 以 '<' 开头的抽取结果没有可核对的内容，不豁免
        self.assertFalse(_content_present("<p>x</p>", MD))


class TestRawFormulas(unittest.TestCase):
    def test_kinds(self):
        got = raw_formulas(r"<p>\(a+b\)</p><p>\[c\]</p><p>$$d$$</p>")
        self.assertEqual([k for k, _ in got],
                         ["inline-\\()", "display-\\[]", "display-$$"])

    def test_comment_stripped(self):
        self.assertEqual(raw_formulas(r"<!-- \(ghost\) --><p>\(x\)</p>"),
                         [("inline-\\()", "x")])


class TestClassifyFormula(unittest.TestCase):
    def test_ok_when_content_present(self):
        self.assertEqual(classify_formula(r"\pi r^2", MD), "ok")

    def test_ok_when_swallowed_markup_head_present(self):
        inner = r"\iota x\forall F^n(F^n x \equiv B^n \Rightarrow F^n)." \
                "</p>  <div id=\"note-33\">"
        self.assertEqual(classify_formula(inner, MD), "ok")

    def test_warning_when_crossblock_and_unverifiable(self):
        # 期望串自身以标记开头且含块级闭合——上游未闭合定界符，期望串不可信
        inner = "<em>B</em> ⊗ <em>A</em>)</li> </ul> <li>lifting"
        self.assertEqual(classify_formula(inner, MD), "warning")

    def test_missing_on_real_loss(self):
        self.assertEqual(classify_formula(r"E = mc^3", MD), "missing")
        self.assertEqual(classify_formula(r"a \Rightarrow F^n).</p> <div>",
                                          r"产物只有 $a \Rightarrow F$。"),
                         "missing")


if __name__ == "__main__":
    unittest.main()
