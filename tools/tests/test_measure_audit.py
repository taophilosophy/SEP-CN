# -*- coding: utf-8 -*-
"""measure_audit 量值识别单测（064 T189 q5）：引用键不计量值、白名单单位、复数与空格。"""
import os
import sys
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, REPO)

from tools import measure_audit  # noqa: E402


class ScanTextTest(unittest.TestCase):
    def test_citation_key_not_measure(self):
        data = measure_audit.scan_text("这里引用 1992a 与 1971c，均非量值。", "demo")
        self.assertEqual(data["items"], [])
        self.assertEqual(data["issues"], [])

    def test_units_and_spacing(self):
        data = measure_audit.scan_text("距离 5km，温度 25 °C，比例 25%。", "demo")
        units = [i["unit"] for i in data["items"]]
        self.assertEqual(units, ["km", "°C", "%"])
        rules = [(i["rule"], i["line"]) for i in data["issues"]]
        self.assertIn(("M-2", 1), rules)
        self.assertEqual(len([r for r in rules if r[0] == "M-2"]), 1)

    def test_plural_unit(self):
        data = measure_audit.scan_text("路程约 30 miles。", "demo")
        self.assertEqual(data["items"][0]["unit"], "mile")
        self.assertTrue(any(i["rule"] == "M-1" for i in data["issues"]))

    def test_non_unit_token_skipped(self):
        data = measure_audit.scan_text("5G 网络与 3D 打印都不是量值。", "demo")
        self.assertEqual(data["items"], [])


if __name__ == "__main__":
    unittest.main()
