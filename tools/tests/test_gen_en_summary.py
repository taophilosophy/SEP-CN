# -*- coding: utf-8 -*-
"""gen_en_summary.py 的标题切分与分组行口径单测（ADR-0056，接口约定见 ADR-0057 §6）。

锁定四件事：
  1. 英文标题切分：常规「中文 English (Authors)」、别名词条保留 `\\*` 标记、
     书名号/括号/破折号夹在中间时剥净、英文在前（`\\*Confucianism 儒学`）时取前段、
     SEP 作者并列顿号 `、` 归半角逗号；
  2. 母词条占位行两形态（链接式与无链接式）产出**同一**无链接分组行，且去掉 `\\*` 标记；
  3. 分组行绝不含链接语法，也不指向 README.md（GitBook 一文件一页，ADR-0057）；
  4. `groups=False` 退回纯词条形态（ADR-0057 回退方案）。
"""
import os
import sys
import tempfile
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, REPO)

from tools.gen_en_summary import build, english_title  # noqa: E402


class EnglishTitleTest(unittest.TestCase):
    def test_plain_entry(self):
        self.assertEqual(english_title('溯因 Abduction (Igor Douven)'), 'Abduction (Igor Douven)')

    def test_alias_keeps_mark(self):
        title = '\\*偶然属性——见本质属性与偶然属性 accidental properties — see essential vs. accidental properties'
        self.assertEqual(
            english_title(title),
            '\\*accidental properties — see essential vs. accidental properties')

    def test_bracket_title_untouched(self):
        title = '枢机主教贝萨里翁 Basil [Cardinal] Bessarion (Eva Del Soldato)'
        self.assertEqual(english_title(title), 'Basil [Cardinal] Bessarion (Eva Del Soldato)')

    def test_fullwidth_punctuation_stripped(self):
        title = '亚里士多德的《动物的运动》 Aristotle’s De Motu Animalium (Klaus Corcilius)'
        self.assertEqual(english_title(title), 'Aristotle’s De Motu Animalium (Klaus Corcilius)')

    def test_english_first(self):
        self.assertEqual(english_title('\\*Confucianism 儒学'), '\\*Confucianism')

    def test_ideographic_comma_normalized(self):
        self.assertEqual(
            english_title('能力 Abilities (John Maier、Sophie Kikkert)'),
            'Abilities (John Maier, Sophie Kikkert)')

    def test_chinese_only_returns_none(self):
        self.assertIsNone(english_title('术语表'))


class GroupRowTest(unittest.TestCase):
    """占位母行两形态必须产出同一无链接分组行。"""

    SOURCES = {
        'linked': '* [\\*美学 aesthetics](README.md)\n  * [审美体验 Aesthetic Experience (Antonia Peacocke)](a/aesthetic-experience.md)\n',
        'bare': '* \\*美学 aesthetics\n  * [审美体验 Aesthetic Experience (Antonia Peacocke)](a/aesthetic-experience.md)\n',
    }

    def setUp(self):
        self.base = tempfile.mkdtemp()
        os.makedirs(os.path.join(self.base, 'a'), exist_ok=True)
        with open(os.path.join(self.base, 'a', 'aesthetic-experience.md'), 'w', encoding='utf-8') as fh:
            fh.write('# stub\n')

    def tearDown(self):
        import shutil
        shutil.rmtree(self.base, ignore_errors=True)

    def _text(self, key, groups=True):
        with tempfile.NamedTemporaryFile('w', suffix='.md', delete=False, encoding='utf-8') as fh:
            fh.write(self.SOURCES[key])
            path = fh.name
        try:
            text, entries, groups_n, skipped = build(path, groups=groups, base=self.base)
        finally:
            os.unlink(path)
        return text, entries, groups_n, skipped

    def test_both_forms_agree(self):
        self.assertEqual(self._text('linked')[0], self._text('bare')[0])

    def test_group_row_is_linkless_and_unmarked(self):
        text = self._text('bare')[0]
        self.assertIn('\n* aesthetics\n', text)
        self.assertNotIn('](README.md)', text)
        self.assertNotIn('\\*aesthetics', text)

    def test_counts(self):
        text, entries, groups, skipped = self._text('bare')
        self.assertEqual(entries, 1)
        self.assertEqual(groups, 1)
        self.assertEqual(len(skipped), 0)

    def test_no_groups_fallback(self):
        text, entries, groups, _ = self._text('bare', groups=False)
        self.assertEqual(groups, 0)
        self.assertEqual(entries, 1)
        self.assertNotIn('aesthetics', text)


if __name__ == '__main__':
    unittest.main()
