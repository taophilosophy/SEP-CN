# -*- coding: utf-8 -*-
"""yuanwen 保真工具单测：strip_math_ex 跨度统计（specs/039 I3 标定，2026-11-17）。"""
import os
import sys
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, REPO)

from tools.check_yuanwen_fidelity import (  # noqa: E402
    SENTINEL, strip_math, strip_math_ex)


class TestStripMathEx(unittest.TestCase):
    def test_inline_pair(self):
        t, s = strip_math_ex(r"a \(x+y\) b")
        self.assertEqual(s, {"spans": 1, "oversize": 0, "unclosed": 0})
        self.assertEqual(t, "a " + SENTINEL + " b")

    def test_display_pair_multiline(self):
        t, s = strip_math_ex("a $$x\n+y$$ b")
        self.assertEqual(s["spans"], 1)
        self.assertEqual(t, "a " + SENTINEL + " b")

    def test_left_paren_no_truncate(self):
        # \right) 内部括号不再提前截断（2026-11-16 formal-belief 判例）
        t, s = strip_math_ex(r"\(f(\left(x\right))\)")
        self.assertEqual(s["spans"], 1)
        self.assertEqual(t, SENTINEL)

    def test_escaped_opener_literal(self):
        t, s = strip_math_ex(r"价格 \$5 与 \$7")
        self.assertEqual(s, {"spans": 0, "oversize": 0, "unclosed": 0})
        self.assertIn("5", t)

    def test_unclosed_opener(self):
        t, s = strip_math_ex("a $x b")
        self.assertEqual(s["unclosed"], 1)
        self.assertEqual(s["spans"], 0)

    def test_oversize_span_flagged(self):
        body = "q" * 7000
        t, s = strip_math_ex("$" + body + "$ tail")
        self.assertEqual(s["spans"], 1)
        self.assertEqual(s["oversize"], 1)

    def test_span_count_symmetry_signal(self):
        # 合并跨度判例：html 两个公式夹正文 vs md 一个大跨度 → 计数不等
        _, sa = strip_math_ex(r"\(x\) and \(y\)")
        _, sb = strip_math_ex("$x and y$")
        self.assertEqual(sa["spans"], 2)
        self.assertEqual(sb["spans"], 1)
        self.assertNotEqual(sa["spans"], sb["spans"])  # 深比对据此判 math-asymmetric

    def test_strip_math_wrapper(self):
        self.assertEqual(strip_math(r"\(x\)"), SENTINEL)

    def test_closer_escaped_not_matched(self):
        # closer 前带反斜杠不闭合（v1 既有语义保留）
        t, s = strip_math_ex(r"\(a\) b \(c\)")
        self.assertEqual(s["spans"], 2)


class TestMdSideSymmetry(unittest.TestCase):
    """md 面侧向对称三修（specs/039 I3 定性，2026-11-17）：逐字搬运的 HTML 片段、
    链接目标、图 alt 阈值与围栏体分流——四者都只为消假阳性，不放松判据。"""

    def _text(self, body):
        import tempfile
        from tools.check_yuanwen_fidelity import md_text
        fd, path = tempfile.mkstemp(suffix=".md")
        os.close(fd)
        try:
            with open(path, "w", encoding="utf-8", newline="\n") as f:
                f.write(body)
            t, _stats = md_text(path)
            return t
        finally:
            os.unlink(path)

    def test_url_target_stripped_with_nested_sigla(self):
        # jefferson 判例：[[[F] available online](https://…)] 三层方括号
        t = self._text("[[[F] available online](https://founders.archives.gov/doc-1)]\n")
        self.assertNotIn("https", t)
        self.assertNotIn("founders", t)
        self.assertIn("available online", t)

    def test_url_target_with_balanced_parens(self):
        # philosophy-religion 判例：维基类 URL 自带圆括号
        t = self._text("[x](https://en.wikipedia.org/wiki/Foo_(bar))\n")
        self.assertNotIn("wikipedia", t)
        self.assertNotIn("bar", t)

    def test_relative_asset_target_stripped(self):
        t = self._text("![long enough description text for the figure here](assets/a/b1.png)\n")
        self.assertNotIn("assets", t)
        self.assertNotIn("b1", t)

    def test_raw_html_fragment_tags_dropped_text_kept(self):
        # nonwellfounded 判例：复杂表格原样搬运，标签名不得计入
        t = self._text("<table><tr><td>alpha</td><td>beta</td></tr></table>\n")
        self.assertIn("alpha", t)
        self.assertIn("beta", t)
        for tag in ("table", "tr", "td"):
            self.assertNotIn(tag, t)

    def test_html_entity_decoded(self):
        t = self._text("a&nbsp;b\n")
        self.assertNotIn("nbsp", t)

    def test_short_alt_dropped_long_alt_kept(self):
        t = self._text("![icon](a.png) ![a figure description that is long enough to count](b.png)\n")
        self.assertNotIn("icon", t)
        self.assertIn("figure description", t)

    def test_fence_body_kept_for_plain_text(self):
        # linguistics 判例：围栏里是 XML 句法样例（正文内容），不得整段剔除
        t = self._text("```\n<clause>\n<noun>freeway</noun>\n```\n")
        self.assertIn("freeway", t)

    def test_fence_body_dropped_for_tex(self):
        t = self._text("```\n\\begin{array}{c} x \\end{array}\n```\n")
        self.assertNotIn("begin", t)


if __name__ == "__main__":
    unittest.main()
