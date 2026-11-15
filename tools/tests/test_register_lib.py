# -*- coding: utf-8 -*-
"""register_lib 单元测试（specs/033 FR-4）：三口径差异类、分节桶、双 schema 解析、
库出口与消费工具旧名一致性。"""
import io
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools import check_terms, cnki_query, registry_azsort, register_lib  # noqa: E402
from tools.register_lib import (bucket_of, fold_nfd, norm_key,  # noqa: E402
                                norm_key_quote, parse_registry2_full,
                                split_row)


class TestFolds(unittest.TestCase):
    def test_b_vs_a_quote_class(self):
        """A 口径折叠引号类字符，B 口径保留：两口径必须可区分。"""
        for ch in ('ʾ', 'ʿ', '’', '‘', 'ʼ', '′', '`'):
            k = 'al-Ṣafā' + ch
            self.assertEqual(norm_key(k), 'al-safa' + ch)
            self.assertEqual(norm_key_quote(k), "al-safa'")

    def test_b_strips_asterisk_c_keeps(self):
        """B 剥斜体星号；C 无星号处理：*Nō* 在 B/C 下折叠态不同。"""
        self.assertEqual(norm_key('*Nō*'), 'no')
        self.assertEqual(fold_nfd('*Nō*'), '*no*')

    def test_variants_agree_on_plain_ascii(self):
        """纯 ASCII 无星无引号时三口径同键。"""
        for s in ('A Priori', '  Ibn  SINA  ', 'modus ponens'):
            self.assertEqual(norm_key(s), norm_key_quote(s))
            self.assertEqual(norm_key(s), fold_nfd(s.strip()))

    def test_whitespace_and_casefold(self):
        """空白归一＋casefold＋NFD 剥变音符（B 保 hamza，A 折直引号）。"""
        self.assertEqual(norm_key('Ikhwān  al-ṢAFĀʾ'), 'ikhwan al-safaʾ')
        self.assertEqual(norm_key_quote('Ikhwān  al-ṢAFĀʾ'), "ikhwan al-safa'")


class TestBucket(unittest.TestCase):
    def test_decor_strip(self):
        """书名号/引号/ʿʾ 等前置装饰符剥离后取首个拉丁字母；中文起首归 #。"""
        self.assertEqual(bucket_of('《Logic》'), 'L')
        self.assertEqual(bucket_of('《逻辑学》'), '#')
        self.assertEqual(bucket_of('ʿilm'), 'I')

    def test_transliteration_folds(self):
        self.assertEqual(bucket_of('Łukasiewicz'), 'L')
        self.assertEqual(bucket_of('Øhrstrøm'), 'O')
        self.assertEqual(bucket_of('Æthelstan'), 'A')
        self.assertEqual(bucket_of('ß'), 'S')

    def test_greek_transliteration(self):
        self.assertEqual(bucket_of('ω-consistency'), 'O')
        self.assertEqual(bucket_of('φ'), 'F')

    def test_non_latin_to_hash(self):
        self.assertEqual(bucket_of('阿字观'), '#')
        self.assertEqual(bucket_of('أبو بكر'), '#')
        self.assertEqual(bucket_of('1/18thGerman-preKant'), '#')
        self.assertEqual(bucket_of(''), '#')


class TestParse(unittest.TestCase):
    def _write(self, text):
        fd, path = tempfile.mkstemp(suffix='.md')
        with os.fdopen(fd, 'w', encoding='utf-8', newline='\n') as f:
            f.write(text)
        self.addCleanup(os.unlink, path)
        return path

    def test_six_column_term_row(self):
        path = self._write(
            '| a priori | a priori | 先天 | x | 学界惯例 | 2026-11-01 |\n')
        rows, warns = parse_registry2_full(path)
        self.assertEqual(len(rows), 1)
        t, orig, trans, nation, years, fs, basis, date, ln = rows[0]
        self.assertEqual((t, orig, trans, nation, years, fs, basis, date),
                         ('a priori', 'a priori', '先天', None, None,
                          'x', '学界惯例', '2026-11-01'))
        self.assertEqual(warns, [])

    def test_eight_column_person_row(self):
        path = self._write(
            '| Abelard Peter | — | 阿伯拉尔 | 法国 | 1079–1142 | y | 依据 | 2026-11-02 |\n')
        rows, warns = parse_registry2_full(path)
        t, orig, trans, nation, years, fs, basis, date, ln = rows[0]
        self.assertEqual((t, trans, nation, years, basis), ('Abelard Peter', '阿伯拉尔',
                                                            '法国', '1079–1142', '依据'))
        self.assertEqual(warns, [])

    def test_missing_basis_warns(self):
        path = self._write('| k | — | 译 | x |  | 2026-11-03 |\n')
        _rows, warns = parse_registry2_full(path)
        self.assertEqual(len(warns), 1)
        self.assertIn('缺依据列', warns[0])

    def test_header_row_not_data(self):
        path = self._write('| 键 | 原文 | 译法 | 首现 | 依据 | 裁定日期 |\n')
        rows, _warns = parse_registry2_full(path)
        self.assertEqual(rows, [])


class TestConsumerAliases(unittest.TestCase):
    """库出口与消费工具旧名一致（specs/033 FR-2 再出口纪律）。"""

    def test_check_terms_norm_key_is_a(self):
        self.assertIs(check_terms.norm_key, register_lib.norm_key_quote)

    def test_azsort_norm_key_is_c(self):
        self.assertIs(registry_azsort.norm_key, register_lib.fold_nfd)
        self.assertIs(registry_azsort.bucket_of, register_lib.bucket_of)

    def test_cnki_norm_key_is_b(self):
        self.assertIs(cnki_query.norm_key, register_lib.norm_key)

    def test_parse_roundtrip_via_check_terms(self):
        src = ('# 术语表\n\n| k1 | — | 译一 | s1 | 依据 | 2026-11-04 |\n'
               '| k2 | — | 译二 | s2 | 依据 | 2026-11-05 |\n')
        fd, path = tempfile.mkstemp(suffix='.md')
        with os.fdopen(fd, 'w', encoding='utf-8', newline='\n') as f:
            f.write(src)
        self.addCleanup(os.unlink, path)
        rows, _w = check_terms.parse_registry(path)
        self.assertEqual([r[0] for r in rows], ['k1', 'k2'])

    def test_paths_match_lib_constants(self):
        self.assertEqual(check_terms.REGISTRY, register_lib.term_path())
        self.assertEqual(check_terms.REGISTRY2, register_lib.person_path())
        self.assertEqual(os.path.basename(register_lib.term_path()), 'shu-yu-biao.md')
        self.assertEqual(os.path.basename(register_lib.person_path()), 'ren-ming-biao.md')


if __name__ == '__main__':
    unittest.main()
