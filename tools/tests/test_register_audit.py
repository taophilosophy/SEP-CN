# -*- coding: utf-8 -*-
"""register_audit 行号单测（064 T188 q4）：节内句子定位须回指全文绝对行号。"""
import os
import sys
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, REPO)

from tools import register_audit  # noqa: E402


class ScanTextTest(unittest.TestCase):
    def test_absolute_line_numbers(self):
        text = (
            "## 1. Alpha\n\n"
            "这是第一段，长度足够进入扫描范围。\n\n"
            "## 2. Beta\n\n"
            "这里出现“您”这个称谓，句子也足够长。\n"
        )
        data = register_audit.scan_text(text, "demo")
        hits = [i for i in data["issues"] if i["rule"] == "R-f"]
        self.assertEqual(len(hits), 1)
        self.assertEqual(hits[0]["line"], 7)
        self.assertEqual(len(data["sections"]), 2)


if __name__ == "__main__":
    unittest.main()
