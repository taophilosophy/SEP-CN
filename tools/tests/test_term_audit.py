# -*- coding: utf-8 -*-
"""term_audit 单元测试（specs/008 US-3）：四态判定、维基排查、只报告不修改。"""
import io
import json
import os
import shutil
import sys
import tempfile
import unittest
from contextlib import redirect_stdout

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools import term_audit

REG = '''# 测试登记册

| 原文 | 译法 | 首现 | 依据 | 裁定日期 |
| ---- | ---- | ---- | ---- | -------- |
| quuxological realism | 虚构实在论 | test | 待复核 | 2026-10-28 |
| florbian transfer | 奇异迁移 | test | 待复核 | 2026-10-28 |
| zorpian dogma | 佐尔比教义 | test | 维基百科某条目 | 2026-10-28 |
| nocred term | 无凭证译法 | test | 待复核 | 2026-10-28 |
| empty term | 空库译法 | test | 待复核 | 2026-10-28 |
'''


def write_cred(queries, term, status, hits):
    d = os.path.join(queries, 'fakeprov')
    os.makedirs(d, exist_ok=True)
    rec = {'key': term, 'term': term, 'provider': 'fakeprov',
           'status': status, 'hits': hits, 'error': None}
    with open(os.path.join(d, term + '.json'), 'w', encoding='utf-8') as f:
        json.dump(rec, f, ensure_ascii=False)


class TermAuditTests(unittest.TestCase):

    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix='audit_test_')
        self.reg = os.path.join(self.tmp, 'reg.md')
        open(self.reg, 'w', encoding='utf-8').write(REG)
        self.queries = os.path.join(self.tmp, 'queries')
        write_cred(self.queries, 'quuxological_realism', 'ok',
                   [{'cn': '虚构实在论', 'en': 'quuxological realism'}])
        write_cred(self.queries, 'florbian_transfer', 'ok',
                   [{'cn': '花袍迁移', 'en': 'florbian transfer'}])
        write_cred(self.queries, 'zorpian_dogma', 'ok',
                   [{'cn': '佐尔比教义', 'en': 'zorpian dogma'}])
        write_cred(self.queries, 'empty_term', 'empty', [])
        # nocred_term 故意无凭证

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def run_audit(self):
        out = os.path.join(self.tmp, 'out')
        buf = io.StringIO()
        argv = ['--registry', self.reg, '--registry2', '',
                '--queries', self.queries, '--out', out]
        with redirect_stdout(buf):
            code = term_audit.main(argv)
        return code, out, buf.getvalue()

    def test_four_states(self):
        code, out, _ = self.run_audit()
        self.assertEqual(code, 0)
        data = json.load(open(os.path.join(out, 'audit-'
                                           + term_audit.date.today().isoformat()
                                           + '.json'), encoding='utf-8'))
        by_term = {r['term']: r for r in data['results']}
        self.assertEqual(by_term['quuxological realism']['status'], '一致')
        self.assertEqual(by_term['florbian transfer']['status'], '不一致')
        self.assertEqual(by_term['empty term']['status'], '查无')
        self.assertEqual(by_term['nocred term']['status'], '未查证')

    def test_wiki_basis_flagged(self):
        code, out, _ = self.run_audit()
        md = open(os.path.join(out, 'audit-'
                               + term_audit.date.today().isoformat()
                               + '.md'), encoding='utf-8').read()
        self.assertIn('zorpian dogma', md)
        self.assertIn('维基来源排查', md)

    def test_mismatch_detail_lists_suggestion(self):
        code, out, _ = self.run_audit()
        md = open(os.path.join(out, 'audit-'
                               + term_audit.date.today().isoformat()
                               + '.md'), encoding='utf-8').read()
        self.assertIn('花袍迁移', md)  # 源译名进建议列
        self.assertIn('不一致明细', md)

    def test_report_only_no_registry_write(self):
        before = open(self.reg, encoding='utf-8').read()
        self.run_audit()
        self.assertEqual(open(self.reg, encoding='utf-8').read(), before)


if __name__ == '__main__':
    unittest.main()
