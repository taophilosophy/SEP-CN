# -*- coding: utf-8 -*-
"""en_source_audit 公式定界符单测（064 T193/T194）：`\\[1em]` 行距不计 display。"""
import os
import sys
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, REPO)

from tools import en_source_audit  # noqa: E402


class CheckMathTest(unittest.TestCase):
    def _out(self):
        return {"counts": {}, "hard": []}

    def test_line_break_not_display(self):
        raw = r"\[x\] \begin{align} a \\[1em] b \end{align}"
        out = self._out()
        en_source_audit._check_math(raw, out)
        self.assertEqual(out["counts"]["math_display"], 1)
        self.assertEqual(out["hard"], [])

    def test_unbalanced_display_still_hard(self):
        raw = r"\[x"
        out = self._out()
        en_source_audit._check_math(raw, out)
        self.assertTrue(any(h.get("class") == "math_delim" for h in out["hard"]))


if __name__ == "__main__":
    unittest.main()
