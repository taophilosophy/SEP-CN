# -*- coding: utf-8 -*-
"""check_terms 单元测试（specs/002 T003）：自洽、规范化、告警分级。

ADR-0036（2026-11-13）：发布词汇表并网删除，原「登记册↔词汇表冲突/滞后/交集」
三表比对逻辑整体移除，测试收敛为两登记册自洽口径。
"""
import io
import json
import os
import sys
import unittest
from contextlib import redirect_stdout

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools import check_terms

FIX = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   'fixtures', 'check_terms')
REG = os.path.join(FIX, 'registry.md')
REG5 = os.path.join(FIX, 'registry5.md')
PERSONS = os.path.join(FIX, 'persons.md')
SLUG = os.path.join(FIX, 'registry_slug.md')
PERSONS_ORIG = os.path.join(FIX, 'persons_orig.md')


def run(*extra):
    buf = io.StringIO()
    argv = ['--registry', REG] + list(extra)
    with redirect_stdout(buf):
        code = check_terms.main(argv)
    return code, buf.getvalue()


class CheckTermsTests(unittest.TestCase):

    def setUp(self):
        self.code, self.out = run()

    def test_exit_code_reflects_hard_errors(self):
        self.assertEqual(self.code, 1)

    def test_broken_deprecated_chain(self):
        self.assertIn('废弃链断裂：brokenchain', self.out)

    def test_duplicate_rows(self):
        self.assertIn('重复行：dupterms|重复译法', self.out)

    def test_missing_date_is_warning_not_error(self):
        self.assertIn('缺裁定日期（告警）：nodate', self.out)

    def test_no_glossary_leg_in_output(self):
        # ADR-0036：词汇表比对腿移除后，输出不再含词汇表字样
        self.assertNotIn('词汇表', self.out)

    def test_single_injection_skips_person_table(self):
        code, out = run()
        self.assertIn('人名表 (跳过) 行 0', out)

    def test_five_column_date_and_basis_parse(self):
        code, out = run('--registry', REG5)
        # 五列行：日期与依据齐全，无告警
        self.assertNotIn('缺裁定日期（告警）：dialetheism', out)
        self.assertNotIn('缺依据列（告警）：dialetheism', out)
        # 旧四列行：缺依据 = 告警，日期仍在第 4 列可读
        self.assertIn('缺依据列（告警）：oldcol', out)
        self.assertNotIn('缺裁定日期（告警）：oldcol', out)
        # 少于四列：列数告警，不误报废弃链
        self.assertIn('仅 3 列', out)

    def test_missing_basis_is_warning_not_error(self):
        code, out = run()
        self.assertIn('缺依据列（告警）：abductive reasoning', out)
        self.assertEqual(code, 1)  # 告警不计硬错误，退出码仍由自洽决定

    def test_person_table_exempt_from_orig_warning(self):
        # ADR-0030（2026-11-10）：人名表原文列留「—」不计入「非英语术语缺原文」告警
        code, out = run('--registry2', PERSONS_ORIG)
        self.assertNotIn('非英语术语缺原文: 人名表 al-Fārābī', out)
        self.assertNotIn('非英语术语缺原文: 人名表 Ibn Sīnā', out)

    def test_editorial_paren_whitelist_ignores_paren_width(self):
        # 2026-11-25：白名单按全角括注登记，登记册里半角写法曾继续告警（7 条）
        from tools import check_terms as ct
        rows = [('anarchy(国际关系)', '—', '无政府状态', 'x', 'b', '2026-01-01', 1),
                ('anarchy（国际关系）', '—', '无政府状态', 'x', 'b', '2026-01-01', 2)]
        self.assertEqual(ct.orig_missing(rows), [])

    def test_slug_in_translation_column_is_hard_error(self):
        # 2026-11-10 补遗：合并脚本曾把来源 slug 写进译法列，slug 被当译法变体比对，
        # 造成滞后伪欠账（lvov-warsaw / cancer / logical-consequence 三例）。
        code, out = run('--registry', SLUG)
        self.assertIn('译法列混入词条 slug：deductive system', out)
        self.assertNotIn('译法列混入词条 slug：modus ponens', out)
        self.assertEqual(code, 1)


LEDGER_REG = os.path.join(FIX, 'ledger_registry.md')


class LedgerTests(unittest.TestCase):
    """判读台账（specs/031 FR-1/FR-2，ADR-0048 决策 6）。

    夹具：ledger_registry.md 三行均「首现=demo」；临时目录写 demo.md（只含「平均」）。
    预期：modus ponens 与 nohit-term 报缺译法（missing），isonomia 只命中变体（ripple）。
    """

    def setUp(self):
        import tempfile
        self.tmp = tempfile.mkdtemp(prefix='term_ledger_')
        self.doc = os.path.join(self.tmp, 'demo.md')
        with io.open(self.doc, 'w', encoding='utf-8') as f:
            f.write('# 演示\n\n本段只写平均二字，不含其他登记译法。\n')
        self.ledger = os.path.join(self.tmp, 'ledger.json')

    def _run_ledger(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = check_terms.main(['--registry', LEDGER_REG, '--ledger',
                                     self.ledger, '--docs', self.doc])
        return code, buf.getvalue()

    def _load(self):
        with io.open(self.ledger, encoding='utf-8') as f:
            return json.load(f)

    def test_ledger_written_with_facts_and_blank_judgement(self):
        code, out = self._run_ledger()
        self.assertEqual(code, 0)  # --docs 恒 0（告警级）
        data = self._load()
        self.assertEqual(data['schema'], 'sep-cn-term-ledger/1')
        self.assertEqual(len(data['rows']), 3)
        by_term = {r['term']: r for r in data['rows']}
        self.assertEqual(by_term['modus ponens']['status'], 'missing')
        self.assertEqual(by_term['nohit-term']['status'], 'missing')
        self.assertEqual(by_term['isonomia']['status'], 'ripple')
        for r in data['rows']:
            self.assertEqual(r['d_class'], '')
            self.assertEqual(r['exit'], '')
            self.assertEqual(r['evidence'], '')
            self.assertEqual(r['source'], '')
            self.assertEqual(r['reviewer'], '')
        self.assertIn('判读台账骨架', out)

    def test_ledger_requires_docs_mode(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = check_terms.main(['--registry', LEDGER_REG, '--ledger', self.ledger])
        self.assertEqual(code, 2)
        self.assertIn('仅在 --docs 模式可用', buf.getvalue())

    def test_check_ledger_rejects_unfilled_rows(self):
        self._run_ledger()
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = check_terms.main(['--check-ledger', self.ledger])
        out = buf.getvalue()
        self.assertEqual(code, 1)
        self.assertIn('d_class 须为', out)
        self.assertIn('exit 须为', out)
        self.assertIn('缺 evidence', out)

    def test_check_ledger_accepts_closed_ledger(self):
        self._run_ledger()
        data = self._load()
        for r in data['rows']:
            r.update(d_class='D2', exit='fix',
                     evidence='回源核对：该概念未出现，按 D2 记不适用')
        with io.open(self.ledger, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False)
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = check_terms.main(['--check-ledger', self.ledger])
        self.assertEqual(code, 0)
        self.assertIn('0 处违例', buf.getvalue())

    def test_check_ledger_requires_source_for_d3_to_d5_and_reviewer_for_exempt(self):
        self._run_ledger()
        data = self._load()
        rows = data['rows']
        rows[0].update(d_class='D4', exit='register', evidence='新分行登记')
        rows[1].update(d_class='D1', exit='exempt', evidence='登记错，保留英文')
        with io.open(self.ledger, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False)
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = check_terms.main(['--check-ledger', self.ledger])
        out = buf.getvalue()
        self.assertEqual(code, 1)
        self.assertIn('D3–D5 须填 source', out)
        self.assertIn('豁免须填 reviewer', out)

    def test_check_ledger_unreadable_file(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = check_terms.main(['--check-ledger', os.path.join(self.tmp, 'nope.json')])
        self.assertEqual(code, 1)
        self.assertIn('台账不可读', buf.getvalue())

    def test_letter_prefix_firstseen_not_matched_by_suffix(self):
        # 「s/scholem 首译」型的单字母碎片是字头目录前缀，不是 slug：
        # 不得以 endswith('s.md') 误配 s 结尾文档（zombies 先例，
        # 119 条噪点淹没真告警；specs/036 裁定表）
        import tempfile
        tmp = tempfile.mkdtemp(prefix='term_prefix_')
        reg = os.path.join(tmp, 'reg.md')
        with io.open(reg, 'w', encoding='utf-8') as f:
            f.write('# 测试登记册\n\n## 术语\n\n| 原文 | 译法 | 首现 | 裁定日期 |\n'
                    '| ---- | ---- | ---- | -------- |\n'
                    '| scholemterm | 绝不会出现的译法 | s/scholem 首译 | 2026-11-15 |\n')
        doc = os.path.join(tmp, 'as.md')
        with io.open(doc, 'w', encoding='utf-8') as f:
            f.write('# 任意\n\n正文不含该译法。\n')
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = check_terms.main(['--registry', reg, '--docs', doc])
        self.assertEqual(code, 0)  # --docs 恒 0（告警级）
        self.assertNotIn('正文缺登记译法', buf.getvalue())


class LibHonestyGateTests(unittest.TestCase):
    """ADR-0090 引证库名如实：检查器对「称审定、实为对照库」的行亮告警。"""

    REG_TEXT = (
        '# 测试登记册\n\n'
        '| 键 | 原文 | 译法 | 首现 | 依据 | 裁定日期 |\n'
        '| --- | --- | --- | --- | --- | --- |\n'
        '| abnormality | — | 异常 | test | 审定作“畸形”（解剖与组织胚胎学名词） | 2026-11-26 |\n'
        '| hermeneutics | — | 诠释学 | test | 审定作“诠释学”（自然辩证法名词） | 2026-11-26 |\n'
    )

    def setUp(self):
        import tempfile
        from tools import term_pairing as tp
        self.tmp = tempfile.mkdtemp(prefix='libgate-')
        reg = os.path.join(self.tmp, 'registry.md')
        with io.open(reg, 'w', encoding='utf-8', newline='\n') as f:
            f.write(self.REG_TEXT)
        idx = {'records': [['畸形', 'malformation', '海峡两岸解剖与组织胚胎学名词', '', 'tw'],
                           ['诠释学', 'hermeneutics', '自然辩证法名词', '03.001', 'audit']],
               'by_key': {}, 'en': {}, 'cn': {}}
        for i, r in enumerate(idx['records']):
            for e in tp.en_stems(r[1]):
                idx['en'].setdefault(e, []).append(i)
            for ck in tp.cn_keys(r[0]):
                idx['cn'].setdefault(ck, []).append(i)
        self.path = os.path.join(self.tmp, 'index.json.gz')
        tp.save_index(idx, self.path)
        buf = io.StringIO()
        with redirect_stdout(buf):
            self.code = check_terms.main(['--registry', reg, '--pair-index', self.path])
        self.out = buf.getvalue()

    def tearDown(self):
        import shutil
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_mislabel_warns(self):
        self.assertIn('引证库名失实（告警）: abnormality', self.out)

    def test_correct_lib_silent(self):
        self.assertNotIn('hermeneutics：', self.out)

    def test_exit_code_zero(self):
        self.assertEqual(self.code, 0)


if __name__ == '__main__':
    unittest.main()


class AtomicWriteTest(unittest.TestCase):
    """报告写出不得因并发而崩（specs/052：8 路并行回补暴露的判官假阳性）。"""

    def test_writes_and_leaves_no_tmp(self):
        import tempfile
        with tempfile.TemporaryDirectory() as d:
            p = os.path.join(d, 'sub', 'report.txt')
            check_terms._atomic_write(p, 'a\nb\n')
            self.assertEqual(open(p, encoding='utf-8').read(), 'a\nb\n')
            leftovers = [f for f in os.listdir(os.path.dirname(p)) if f.endswith('.tmp')]
            self.assertEqual(leftovers, [])

    def test_overwrites_existing_report(self):
        import tempfile
        with tempfile.TemporaryDirectory() as d:
            p = os.path.join(d, 'report.txt')
            check_terms._atomic_write(p, 'old\n')
            check_terms._atomic_write(p, 'new\n')
            self.assertEqual(open(p, encoding='utf-8').read(), 'new\n')

class PairingGateTests(unittest.TestCase):
    """ADR-0088 审定引用配对的集成测试：检查器真会亮告警（不只是判据单测）。"""

    REG_TEXT = (
        '# 测试登记册\n\n'
        '| 键 | 原文 | 译法 | 首现 | 依据 | 裁定日期 |\n'
        '| --- | --- | --- | --- | --- | --- |\n'
        '| halting problem | — | 停机问题 | test | 审定名词库（termonline-all，凭证 2026-11-23） | 2026-11-23 |\n'
        '| knowing how | — | 知道如何 | test | 审定名词库（termonline-all，凭证 2026-11-23） | 2026-11-23 |\n'
        '| negative case | — | 反证形 | test | 审定库无对口条目（2026-11-26 界面复核：未审定） | 2026-11-26 |\n'
    )

    def setUp(self):
        import tempfile
        from tools import term_pairing as tp
        self.tmp = tempfile.mkdtemp(prefix='pairgate-')
        reg = os.path.join(self.tmp, 'registry.md')
        with io.open(reg, 'w', encoding='utf-8', newline='\n') as f:
            f.write(self.REG_TEXT)
        idx = {'records': [['停机问题', 'halting problem', '自然辩证法名词', '03.662', 'audit']],
               'by_key': {}, 'en': {}, 'cn': {}}
        for i, r in enumerate(idx['records']):
            for e in tp.en_stems(r[1]):
                idx['en'].setdefault(e, []).append(i)
            for ck in tp.cn_keys(r[0]):
                idx['cn'].setdefault(ck, []).append(i)
        self.idx_path = os.path.join(self.tmp, 'index.json.gz')
        tp.save_index(idx, self.idx_path)
        buf = io.StringIO()
        with redirect_stdout(buf):
            self.code = check_terms.main(['--registry', reg, '--pair-index', self.idx_path])
        self.out = buf.getvalue()

    def tearDown(self):
        import shutil
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_matched_row_passes_silently(self):
        self.assertNotIn('halting problem', self.out)

    def test_unmatched_claim_warns(self):
        self.assertIn('审定引用无配对（告警）: knowing how', self.out)

    def test_negative_claim_exempt(self):
        self.assertNotIn('negative case', self.out)

    def test_warning_does_not_raise_hard_error(self):
        # 配对告警是告警级：本夹具无自洽错误，退出码应为 0
        self.assertEqual(self.code, 0)

class StdPairingGateTests(unittest.TestCase):
    """GB 标准库配对门（ADR-0088 同判据）：claim 无配对即告警，负证豁免。"""

    REG_TEXT = (
        '# 测试登记册\n\n'
        '| 键 | 原文 | 译法 | 首现 | 依据 | 裁定日期 |\n'
        '| --- | --- | --- | --- | --- | --- |\n'
        '| scada system | — | 数据采集系统 | test | 知网系查证在案（termonline-standard GB 标准库凭证 2026-10-28） | 2026-10-28 |\n'
        '| noise term | — | 噪声项 | test | 知网系查证在案（termonline-standard GB 标准库凭证 2026-10-28） | 2026-10-28 |\n'
        '| negative std | — | 反证标 | test | 知网系查证无收录（GB 标准库凭证在案 2026-10-28） | 2026-10-28 |\n'
    )

    def setUp(self):
        import tempfile
        from tools import term_pairing as tp
        self.tmp = tempfile.mkdtemp(prefix='stdgate-')
        reg = os.path.join(self.tmp, 'registry.md')
        with io.open(reg, 'w', encoding='utf-8', newline='\n') as f:
            f.write(self.REG_TEXT)
        idx = {'records': [['数据采集系统', 'SCADA system', '工业自动化 术语', 'GB/T 1', 'std']],
               'by_key': {}, 'en': {}, 'cn': {}}
        for i, r in enumerate(idx['records']):
            for e in tp.en_stems(r[1]):
                idx['en'].setdefault(e, []).append(i)
            for ck in tp.cn_keys(r[0]):
                idx['cn'].setdefault(ck, []).append(i)
        self.path = os.path.join(self.tmp, 'std.json.gz')
        tp.save_index(idx, self.path)
        buf = io.StringIO()
        with redirect_stdout(buf):
            self.code = check_terms.main(['--registry', reg, '--std-index', self.path])
        self.out = buf.getvalue()

    def tearDown(self):
        import shutil
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_matched_std_row_passes(self):
        self.assertNotIn('scada system', self.out)

    def test_unmatched_std_claim_warns(self):
        self.assertIn('标准库引用无配对（告警）: noise term', self.out)

    def test_negative_std_claim_exempt(self):
        self.assertNotIn('negative std', self.out)

