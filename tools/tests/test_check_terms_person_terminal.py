# -*- coding: utf-8 -*-
"""check_terms 人名缺项终态豁免的单元测试（2026-11-26，specs/013 B 档收口）。

覆盖：
  * 缺项且依据列注明终态 → 不计入告警
  * 「留白待考」等含待办词 → 仍计入（终态与待办不可混）
  * 013 台账（per-line NOSOURCE／gnd none／decisions 驳回）→ 不计入
  * 终态来源统计与索引写入
"""
import json
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools import check_terms


def row(term, nation, years, basis, lineno):
    """parse_registry2_full 口径的 9 元组。"""
    return (term, '—', '译名', nation, years, '首现', basis, '2026-01-01', lineno)


ROWS = [
    row('Filled', '德国', '1900–1990', '凭证', 1),
    row('SoftTerminal', '—', '—', '查无权威源，留空并登记', 2),
    row('Pending', '—', '—', '留白待考', 3),
    row('HardTerminal', '—', '—', '终态：013 B 档', 4),
    row('HalfMissing', '法国', '—', '凭证', 5),
]


class PersonTerminalTests(unittest.TestCase):

    def setUp(self):
        self._ledgers = check_terms.PERSON_TERMINAL_LEDGERS
        check_terms.PERSON_TERMINAL_LEDGERS = ()
        check_terms._PERSON_TERMINAL_CACHE = None

    def tearDown(self):
        check_terms.PERSON_TERMINAL_LEDGERS = self._ledgers
        check_terms._PERSON_TERMINAL_CACHE = None

    def test_terminal_excluded_pending_kept(self):
        missing = check_terms.person_missing(ROWS)
        self.assertEqual([m[0] for m in missing], ['Pending', 'HalfMissing'])

    def test_stats_split_by_source(self):
        total, by = check_terms.person_terminal_stats(ROWS)
        self.assertEqual(total, 2)
        self.assertEqual(by, {'basis': 2})

    def test_nosource_ledger_exempts(self):
        with tempfile.TemporaryDirectory() as d:
            p = os.path.join(d, 'per-line.jsonl')
            with open(p, 'w', encoding='utf-8') as f:
                f.write(json.dumps({'key': 'Pending', 'v': 'NOSOURCE'},
                                   ensure_ascii=False) + '\n')
            check_terms.PERSON_TERMINAL_LEDGERS = ((p, 'per-line'),)
            check_terms._PERSON_TERMINAL_CACHE = None
            missing = check_terms.person_missing(ROWS)
            self.assertEqual([m[0] for m in missing], ['HalfMissing'])

    def test_gnd_none_and_reject_ledgers(self):
        with tempfile.TemporaryDirectory() as d:
            tri = os.path.join(d, 'triage.tsv')
            with open(tri, 'w', encoding='utf-8') as f:
                f.write('键\tverdict\t理由\t候选\n')
                f.write('Pending\tnone\t查无\t-\n')
            dec = os.path.join(d, 'decisions.tsv')
            with open(dec, 'w', encoding='utf-8') as f:
                f.write('键\t候选名\t生卒\t出生地\t职业\tGND\t判定\t理由\n')
                f.write('HalfMissing\t某某\t\t\t\t\t同名驳回\t同名异人\n')
            check_terms.PERSON_TERMINAL_LEDGERS = ((tri, 'triage'),
                                                   (dec, 'decisions'))
            check_terms._PERSON_TERMINAL_CACHE = None
            missing = check_terms.person_missing(ROWS)
            self.assertEqual(missing, [])

    def test_terminal_index_written(self):
        with tempfile.TemporaryDirectory() as d:
            p = os.path.join(d, 'terminal.tsv')
            n = check_terms.write_person_terminal_index(ROWS, p)
            self.assertEqual(n, 2)
            with open(p, encoding='utf-8') as f:
                text = f.read()
            self.assertIn('SoftTerminal', text)
            self.assertIn('basis', text)
            self.assertNotIn('Pending', text)


if __name__ == '__main__':
    unittest.main()
