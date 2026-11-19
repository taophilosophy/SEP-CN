# -*- coding: utf-8 -*-
"""specs/054 装配器单测：往返全等（B3.1/B3.2 目录域夹具级）＋谓词组合枚举。"""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools import parser  # noqa: E402
from tools.rebuild_catalog import (  # noqa: E402
    align_events, rebuild, render_event, strip_variants, events_from_account)


FIXTURE = """<!DOCTYPE html>
<head><title>T</title></head>
<body>
<a id="a"></a>
<h2>A</h2>
<ul>
<li> <a href="entries/alpha/"><strong>alpha</strong></a> (A One) </li>
<li> alpha-old &mdash; see <a href="entries/alpha/">alpha</a> </li>
<li> group-label
   <ul>
   <li> <a href="entries/alpha-sub/"><strong>alpha sub</strong></a> </li>
   </ul></li>
<li> <a href="entries/beta/"><strong>beta</strong></a> (B Two)
</ul>
</body>"""

SNAP_NAME = "20261111T000000Z-contents.html"


def account_from_fixture():
    full = parser.parse_catalog_full(FIXTURE)
    return {"fetched_at": None, "source": "en/_catalog/" + SNAP_NAME,
            "items": sorted(full["items"], key=lambda x: x["slug"]),
            "alias_rows": sorted(full["alias_rows"], key=lambda x: x["doc_order"]),
            "cluster_mothers": sorted(full["cluster_mothers"], key=lambda x: x["doc_order"])}


class TestStripVariants(unittest.TestCase):
    def test_basename_any_cross_platform(self):
        """账内 source 曾写 Windows 绝对路径，Linux CI 上 os.path.basename 不切分 →
        误判“账与快照不同时点”（2026-11-19 CI 实红）。双分隔符归一须成立。"""
        from tools.rebuild_catalog import _basename_any
        win = "C:\\Users\\x\\SEP-CN\\en\\_catalog\\20261114T231750Z-contents.html"
        posix = "en/_catalog/20261114T231750Z-contents.html"
        want = "20261114T231750Z-contents.html"
        self.assertEqual(_basename_any(win), want)
        self.assertEqual(_basename_any(posix), want)

    def test_exact(self):
        self.assertEqual(strip_variants("<li> x </li>", "<li> x </li>"), ())

    def test_no_close(self):
        self.assertEqual(strip_variants("<li> x", "<li> x </li>"), ("no-close-li",))

    def test_inline(self):
        self.assertEqual(strip_variants("<li> <em>x</em>", "<li> x </li>"),
                         ("inline-markup", "no-close-li"))

    def test_entity(self):
        got = "<li> <strong>Grüne-Yanoff</strong></a>"
        want = "<li> <strong>Gr&uuml;ne-Yanoff</strong></a>"
        self.assertEqual(strip_variants(got, want), ("entity-encoding",))

    def test_combination(self):
        got = "<li> <a href=\"entries/x/\"><strong>x </strong></a> (A)"
        want = "<li> <a href=\"entries/x/\"><strong>x</strong></a> (A) </li>"
        self.assertEqual(strip_variants(got, want), ("trailing-space", "no-close-li"))

    def test_off_predicate(self):
        self.assertIsNone(strip_variants("<li> 完全不同", "<li> x </li>"))


class TestRoundtrip(unittest.TestCase):
    def test_fixture_roundtrip_sha(self):
        """夹具级 B3.2：账⊕骨架⊕池 → 装配 ≡ 原页（逐字节）。"""
        account = account_from_fixture()
        lines = FIXTURE.split("\n")
        events = events_from_account(account)
        resid, skeleton, tail, unmatched = align_events(lines, events)
        self.assertEqual(unmatched, [])
        skel_doc = {"source_snapshot": SNAP_NAME, "fixed_rows": skeleton, "tail": tail}
        resid_doc = {"source_snapshot": SNAP_NAME, "count": len(resid),
                     "entries": resid}
        rebuilt = rebuild(account, skel_doc, resid_doc)
        self.assertEqual(rebuilt, FIXTURE)

    def test_residual_kind_inventory(self):
        """夹具残差只落准入类；池条目键=doc_order 唯一。"""
        account = account_from_fixture()
        lines = FIXTURE.split("\n")
        resid, _, _, _ = align_events(lines, events_from_account(account))
        allowed = {"trailing-space", "inline-markup", "no-close-li", "entity-encoding"}
        for e in resid:
            self.assertTrue(set(e["kind"]) <= allowed, e)
        # 夹具里 beta 行是 no-close-li 形态（SEP 噪声仿真）
        self.assertTrue(any("no-close-li" in e["kind"] for e in resid))

    def test_render_forms(self):
        ev_canon = {"slug": "s", "title": "t", "authors": "A", "level": 1, "doc_order": 0}
        self.assertEqual(render_event(ev_canon),
                         '<li> <a href="entries/s/"><strong>t</strong></a> (A) </li>')
        ev_alias = {"slug": "s", "label": "old", "href_text": "t", "level": 2, "doc_order": 1}
        self.assertEqual(render_event(ev_alias),
                         '   <li> old &mdash; see <a href="entries/s/">t</a> </li>')
        ev_mother = {"label": "g", "level": 1, "doc_order": 2}
        self.assertEqual(render_event(ev_mother), "<li> g")


if __name__ == "__main__":
    unittest.main()
