# -*- coding: utf-8 -*-
"""specs/054 运营化：四方漂移报告与队列构造（离线夹具，不联网）。"""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.catalog_drift import _slugs_from_md, drift_report, render_md  # noqa: E402
from tools.detect_updates import build_queue, filter_window, parse_new_html  # noqa: E402


def full(items, alias=None, mothers=None):
    return {"items": items, "alias_rows": alias or [], "cluster_mothers": mothers or []}


class TestSlugsFromMd(unittest.TestCase):
    def test_paths_and_see(self):
        text = ("* [甲 Alpha (A)](a/alpha.md)\n"
                "  * [乙 Beta (B)](b/beta.md)\n"
                "* [丙_alias — see gamma](g/gamma-see-gamma.md)\n"
                "* [导航](qian-yan/x.md)\n"
                "* 无链接分组行\n")
        got = _slugs_from_md(text)
        self.assertEqual(got, {"alpha", "beta"})


class TestDriftReport(unittest.TestCase):
    def setUp(self):
        self.base = full([
            {"slug": "alpha", "title": "alpha", "authors": "A"},
            {"slug": "beta", "title": "beta", "authors": "B"},
            {"slug": "gone", "title": "gone", "authors": "G"},
        ], alias=[{"slug": "alpha"}])
        self.up = full([
            {"slug": "alpha", "title": "alpha", "authors": "A"},
            {"slug": "beta", "title": "beta", "authors": "B2"},
            {"slug": "newone", "title": "new one", "authors": "N"},
        ], alias=[{"slug": "alpha"}, {"slug": "newone"}])

    def test_changed_axes(self):
        rep = drift_report(self.up, self.base, {"alpha", "beta"}, {"alpha", "beta"})
        self.assertTrue(rep["changed"])
        self.assertEqual(rep["catalog"]["added"], ["newone"])
        self.assertEqual(rep["catalog"]["removed"], ["gone"])
        self.assertEqual([r["slug"] for r in rep["catalog"]["authors_changed"]], ["beta"])
        self.assertEqual(rep["catalog"]["alias_added"], ["newone"])
        self.assertEqual(rep["local"]["upstream_missing_in_summary"], ["newone"])

    def test_suspended_not_counted(self):
        rep = drift_report(self.up, self.base, {"alpha", "beta"}, {"alpha", "beta"},
                           suspended={"gone"})
        self.assertEqual(rep["catalog"]["removed"], ["gone"])       # 账层仍如实报告
        self.assertEqual(rep["local"]["summary_only_upstream"], [])  # 本地覆盖层不生噪

    def test_clean(self):
        rep = drift_report(self.base, self.base, {"alpha", "beta", "gone"},
                           {"alpha", "beta", "gone"})
        self.assertFalse(rep["changed"])
        self.assertIn("上游目录漂移巡检", render_md(rep))

    def test_rename_detected(self):
        up = full([{"slug": "alpha", "title": "alpha renamed", "authors": "A"},
                   {"slug": "beta", "title": "beta", "authors": "B"},
                   {"slug": "gone", "title": "gone", "authors": "G"}])
        rep = drift_report(up, self.base, {"alpha", "beta", "gone"},
                           {"alpha", "beta", "gone"})
        self.assertEqual(rep["catalog"]["renamed"],
                         [{"slug": "alpha", "old": "alpha", "new": "alpha renamed"}])


NEW_FIXTURE = (
    '<ul>\n'
    '<li> <a href="entries/hamann/"><strong>Johann Georg Hamann</strong></a> '
    '(Gwen Griffith-Dickson) [REVISED: <em>September 23, 2026</em>]'
    '<div class="small">Changes to: Main text, Bibliography</div></li>\n'
    '<li> <a href="entries/aesthetics-race/"><strong>Aesthetics and Race</strong></a> '
    '(Monique Roelofs) [NEW: <em>September 22, 2026</em>]</li>\n'
    '<li> <a href="entries/old-entry/"><strong>Old Entry</strong></a> '
    '(Someone) [REVISED: <em>January 02, 2020</em>]</li>\n'
    '</ul>\n')


class TestFilterSynced(unittest.TestCase):
    def test_pin_newer_than_event(self):
        """baseline.fetched_at ≥ 事件日期 → 已同步，剔出队列。"""
        from tools.detect_updates import filter_synced
        base = {"entries": [
            {"slug": "done-one", "fetched_at": "2026-11-19T00:00:00Z"},
            {"slug": "stale-one", "fetched_at": "2026-10-26T00:00:00Z"},
        ]}
        web = [{"slug": "done-one", "event": "revised", "when": "2026-11-17"},
               {"slug": "stale-one", "event": "revised", "when": "2026-11-17"},
               {"slug": "brand-new", "event": "new", "when": "2026-11-17"}]
        kept, skipped = filter_synced(web, base)
        self.assertEqual(skipped, 1)
        self.assertEqual([w["slug"] for w in kept], ["stale-one", "brand-new"])


class TestArchinfoPending(unittest.TestCase):
    def test_pending_archive_text(self):
        """冻结后修订：archinfo 只说「is not yet archived」，无 archive edition 行。"""
        from tools import parser
        html = ('<p>The latest version of the entry "<i>Johann Georg Hamann</i>" '
                '(substantive content change) is not yet archived and may change before '
                'it is archived</p>')
        ai = parser.parse_archinfo(html)
        self.assertIsNone(ai["latest_edition"])
        self.assertEqual(ai["pending_change_type"], "substantive content change")

    def test_archived_text(self):
        from tools import parser
        html = ('<p>This is a file in the archives of the Stanford Encyclopedia of '
                'Philosophy. Please note that the following archive edition: '
                'Summer 2025 (substantive content change) is the most recent.</p>')
        ai = parser.parse_archinfo(html)
        self.assertEqual(ai["latest_edition"], "Summer 2025")
        self.assertEqual(ai["latest_change_type"], "substantive content change")
        self.assertIsNone(ai["pending_change_type"])


class TestDetectUpdates(unittest.TestCase):
    def test_parse_new_html(self):
        items = parse_new_html(NEW_FIXTURE)
        self.assertEqual([i["slug"] for i in items], ["hamann", "aesthetics-race", "old-entry"])
        self.assertEqual(items[0]["event"], "revised")
        self.assertIn("Main text", items[0]["changes"])
        self.assertEqual(items[1]["event"], "new")
        self.assertEqual(items[1]["title"], "Aesthetics and Race")

    def test_window_filter(self):
        picked, undated = filter_window(parse_new_html(NEW_FIXTURE), 90)
        self.assertEqual(undated, [])
        slugs = [i["slug"] for i in picked]
        self.assertIn("hamann", slugs)
        self.assertNotIn("old-entry", slugs)

    def test_queue_merge(self):
        web = [{"slug": "aesthetics-race", "event": "new", "date": "September 22, 2026",
                "when": "2026-09-22", "title": "x", "changes": ""},
               {"slug": "hamann", "event": "revised", "date": "September 23, 2026",
                "when": "2026-09-23", "title": "y", "changes": "Main text"}]
        arch = [{"slug": "hamann", "baseline_edition": "Summer 2025",
                 "latest_edition": "Fall 2026", "change_type": "substantive content change"}]
        q = build_queue(web, arch)
        actions = {(r["slug"], r["action"]) for r in q}
        self.assertIn(("aesthetics-race", "retranslate"), actions)
        self.assertIn(("hamann", "update"), actions)
        ham = [r for r in q if r["slug"] == "hamann"][0]
        self.assertGreaterEqual(len(ham["sources"]), 2)


if __name__ == "__main__":
    unittest.main()
