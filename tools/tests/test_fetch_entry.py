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


class TestJournalLock(unittest.TestCase):
    """钉前移须落 journal lock 事件（ADR-0068 W1 事件族；2026-11-21 形式化审视补缺）。"""

    def test_main_sha_of(self):
        from tools.fetch_entry import _main_sha_of
        self.assertIsNone(_main_sha_of([]))
        self.assertIsNone(_main_sha_of(None))
        self.assertIsNone(_main_sha_of([{"sha256": "a", "kind": "notes"}]))
        self.assertEqual(_main_sha_of([{"sha256": "a", "kind": "notes"},
                                       {"sha256": "b", "kind": "main"}]), "b")

    def test_lock_event_written_and_idempotent(self):
        import tempfile
        from tools import journal_lib
        from tools.fetch_entry import _journal_lock
        rec = {"fetched_at": "2026-11-21T00:00:00Z",
               "pubinfo": {"first_published": "Feb 8, 2006",
                           "substantive_revision": "Nov 20, 2026"},
               "source_url": "https://plato.stanford.edu/entries/x/"}
        with tempfile.TemporaryDirectory() as td:
            journal_lib.JOURNAL_DIR = td
            try:
                ev = _journal_lock("x", None, "shaA", rec)
                self.assertIsNotNone(ev)
                self.assertEqual(ev["type"], "lock")
                self.assertEqual(ev["sha256"], "shaA")
                self.assertEqual(ev["seq"], 1)
                self.assertEqual(ev["actor"], "fetch_entry")
                self.assertEqual(ev["pubinfo_date"], "Nov 20, 2026")
                # 幂等：sha 相同不落（重抓同内容零事件）
                self.assertIsNone(_journal_lock("x", "shaA", "shaA", rec))
                self.assertEqual(len(journal_lib.read_events("x")), 1)
                # sha 再变更 → 新事件，seq 递增
                _journal_lock("x", "shaA", "shaB", rec)
                events = journal_lib.read_events("x")
                self.assertEqual(len(events), 2)
                self.assertEqual(events[-1]["seq"], 2)
                self.assertEqual(events[-1]["sha256"], "shaB")
            finally:
                journal_lib.JOURNAL_DIR = None


if __name__ == "__main__":
    unittest.main()
