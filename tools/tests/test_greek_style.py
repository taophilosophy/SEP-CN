# -*- coding: utf-8 -*-
"""ADR-0049 孤立希腊字母文字化：check_math_zh C10 与 check_pairs 归一口径单测。"""
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from tools.check_math_zh import check_file  # noqa: E402
from tools.check_pairs import GREEK_LONE_RE, check_counts  # noqa: E402


class LoneGreekC10(unittest.TestCase):
    def _codes(self, content):
        fd, path = tempfile.mkstemp(suffix=".md")
        try:
            with os.fdopen(fd, "w", encoding="utf-8") as f:
                f.write(content)
            issues = check_file(path, "tmp.md")
            return {code for code, _, _ in issues}
        finally:
            os.remove(path)

    def test_lone_greek_flagged(self):
        self.assertIn("C10", self._codes("解释 $\\omega$ 与 *K* 之间。\n"))

    def test_primed_not_flagged(self):
        self.assertNotIn("C10", self._codes("则 $\\omega'$ 取距 *ω* 最近的那个。\n"))

    def test_composite_not_flagged(self):
        self.assertNotIn("C10", self._codes("即若 $\\varphi \\in A$，则 $\\neg\\varphi$ 亦在。\n"))

    def test_subscripted_not_flagged(self):
        self.assertNotIn("C10", self._codes("第一条把 $\\alpha_1$ 换成 $\\alpha$。\n"))

    def test_upright_delta_not_flagged(self):
        self.assertNotIn("C10", self._codes("Δ 是 *IC* 融合算子。\n"))

    def test_c10_is_warn_level(self):
        from tools.check_math_zh import main
        fd, path = tempfile.mkstemp(suffix=".md")
        try:
            with os.fdopen(fd, "w", encoding="utf-8") as f:
                f.write("解释 $\\omega$ 与 *K* 之间。\n")
            rc = main([path])
            self.assertEqual(rc, 0, "C10 是告警级，不得影响退出码")
        finally:
            os.remove(path)


class PairsNormalization(unittest.TestCase):
    def _run(self, zh, yw):
        tmp = tempfile.mkdtemp()
        try:
            letter = os.path.join(tmp, "x")
            os.makedirs(os.path.join(tmp, "yuanwen", "x"))
            os.makedirs(letter)
            slug = "a-foo"
            zh_p = os.path.join(letter, slug + ".md")
            with open(zh_p, "w", encoding="utf-8") as f:
                f.write(zh)
            with open(os.path.join(tmp, "yuanwen", "x", slug + ".md"), "w",
                      encoding="utf-8") as f:
                f.write(yw)
            issues = []
            check_counts(zh_p, slug, zh, issues)
            return [i for i in issues if i["rule"] == "count-vs-source"]
        finally:
            import shutil
            shutil.rmtree(tmp)

    SPANS = " ".join("$x_{%d}$" % i for i in range(30))
    LONE = " ".join(["$\\omega$", "$\\varphi$", "$\\alpha$", "$\\beta$", "$\\pi$"])

    def test_unconverted_parity(self):
        # 两侧同形（回改前）：30 段（含 5 孤立）对 30 段，对称剔除后仍平
        self.assertEqual(self._run(self.SPANS, self.SPANS), [])

    def test_converted_no_alarm(self):
        # 回改后：zh 孤立归零，yuanwen 源形态仍在 → 归一后 25 对 25，不告警
        zh_converted = self.SPANS + " 首现。" + " 又见。"
        self.assertEqual(self._run(zh_converted, self.SPANS + " " + self.LONE), [])

    def test_lone_regex_scope(self):
        self.assertEqual(len(GREEK_LONE_RE.findall("$\\omega$ $\\omega'$ $\\omega_1$ $\\le$")),
                         1, "只剔纯孤立希腊字母，撇号/下标/非希腊不在列")


if __name__ == "__main__":
    unittest.main()
