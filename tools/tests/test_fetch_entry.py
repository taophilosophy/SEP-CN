# -*- coding: utf-8 -*-
"""fetch_entry 软 404 防护与归档版 URL 单元测试（2026-10-28 撤稿词条教训）。"""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from tools.fetch_entry import entry_base, is_soft404


class TestSoft404(unittest.TestCase):
    def test_error_pages_detected(self):
        self.assertTrue(is_soft404('<html><head><title>Document Not Found</title></head>'))
        self.assertTrue(is_soft404('<title> Update Your Link (Stanford Encyclopedia of Philosophy)</title>'))
        self.assertTrue(is_soft404('<TITLE>document not found</TITLE>'))

    def test_real_entry_not_flagged(self):
        page = ('<!DOCTYPE html><html lang="en"><head>'
                '<title>Abduction (Stanford Encyclopedia of Philosophy)</title>'
                '<meta name="citation_title" content="Abduction"/></head>')
        self.assertFalse(is_soft404(page))
        self.assertFalse(is_soft404('<title>Alcmaeon [Internet Encyclopedia]</title>'))


class TestEntryBase(unittest.TestCase):
    def test_live_url_default(self):
        self.assertEqual(entry_base("abduction"),
                         "https://plato.stanford.edu/entries/abduction/")

    def test_archive_edition_url(self):
        self.assertEqual(
            entry_base("pineal-gland", "spr2017"),
            "https://plato.stanford.edu/archives/spr2017/entries/pineal-gland/")


if __name__ == "__main__":
    unittest.main()
