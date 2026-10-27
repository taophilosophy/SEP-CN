# -*- coding: utf-8 -*-
"""biblio_audit 中文文献探针单元测试（CI: unittest discover）。"""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from tools.biblio_audit import likely_chinese, probe_text


class TestProbeText(unittest.TestCase):
    def test_cjk_and_kana(self):
        p = probe_text("Yan Buke 阎步克, 2001, 《乐师与史官》")
        self.assertTrue(p["cjk"])
        self.assertFalse(p["kana"])
        self.assertTrue(likely_chinese(p))
        self.assertTrue(probe_text("Kasulis 2002, ほとけ")["kana"])

    def test_classic_terms(self):
        p = probe_text("Analects 2.3; Zhuangzi, ch. 2; Daodejing")
        self.assertIn("Analects", p["classic_hits"])
        self.assertIn("Zhuangzi", p["classic_hits"])
        self.assertTrue(likely_chinese(p))

    def test_authorpos_threshold(self):
        one = probe_text("Long, A. A., 1986, ...")
        self.assertEqual(one["authorpos_hits"], 1)
        self.assertFalse(likely_chinese(one))  # 单个作者位姓氏不判中（噪声）
        two = probe_text("Long, A. A., 1986. Wang, K., 1999.")
        self.assertGreaterEqual(two["authorpos_hits"], 2)
        self.assertTrue(likely_chinese(two))

    def test_english_biblio_clean(self):
        p = probe_text("Achinstein, P., 2001. The Book of Evidence, Oxford.")
        self.assertFalse(likely_chinese(p))


if __name__ == "__main__":
    unittest.main()
