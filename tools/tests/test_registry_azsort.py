# -*- coding: utf-8 -*-
"""registry_azsort 单元测试：节头去重（幂等）、显式路径参数只处理指定文件。"""
import io
import os
import sys
import tempfile
import unittest
from contextlib import redirect_stdout

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools import registry_azsort as az

TITLE = '# 译者说明：术语对照表\n'
ROWS_A = [
    '| Aardvark | — | 土豚 | entry-a | 说明；凭证 2026-11-01 | 2026-11-01 |\n',
    '| Abacus | — | 算盘 | entry-ab | 说明；凭证 2026-11-02 | 2026-11-02 |\n',
]
ROWS_B = [
    '| Bacon | — | 培根 | entry-b | 说明；凭证 2026-11-03 | 2026-11-03 |\n',
]


def render_text(lines):
    header, rows, docs = az.scan(lines)
    return az.render(header, rows, docs)[0]


class TestLetterHeader(unittest.TestCase):
    def test_first_letter_header_before_rows_not_duplicated(self):
        """首个字母节标题先于数据行出现时，不得被收进文件头而重复输出。"""
        src = [TITLE, '\n', '## A\n', '\n'] + ROWS_A + ['\n', '## B\n', '\n'] + ROWS_B
        out = render_text(src)
        self.assertEqual(out.count('\n## A\n'), 1, out)
        self.assertEqual(out.count('\n## B\n'), 1, out)

    def test_idempotent(self):
        """渲染结果再扫再渲染应逐字节一致（不动点）。"""
        src = [TITLE, '\n', '## A\n', '\n'] + ROWS_A + ['\n', '## B\n', '\n'] + ROWS_B
        once = render_text(src)
        twice = render_text(once.splitlines(True))
        self.assertEqual(once, twice)

    def test_rows_conserved(self):
        """重排不增删数据行。"""
        src = [TITLE, '\n', '## B\n', '\n'] + ROWS_B + ['\n', '## A\n', '\n'] + ROWS_A
        out = render_text(src)
        for row in ROWS_A + ROWS_B:
            self.assertIn(row, out)
        data = [l for l in out.splitlines()
                if l.startswith('|') and l.strip() not in az.TERM_HEADER
                and l.strip() not in az.PERSON_HEADER]
        self.assertEqual(len(data), 3)
        # 每节必带表头与分隔行（020：登记册原为裸管道网格，站点渲染成文字墙）
        self.assertEqual(out.count(az.TERM_HEADER[0]), 2, out)
        self.assertEqual(out.count(az.TERM_HEADER[1]), 2, out)


class TestMainPaths(unittest.TestCase):
    def test_explicit_path_only_one_file(self):
        """带路径参数时只处理该文件，不连带处理默认两册。"""
        with tempfile.NamedTemporaryFile('w', suffix='.md', delete=False,
                                         encoding='utf-8') as f:
            f.write(TITLE + '\n## A\n\n' + ''.join(ROWS_A))
            path = f.name
        try:
            buf = io.StringIO()
            with redirect_stdout(buf):
                rc = az.main([path, '--allow-dirty'])
            self.assertEqual(rc, 0)
            out = buf.getvalue()
            self.assertIn(os.path.basename(path), out)
            self.assertNotIn(az.TERM_FILE + '：', out)
            self.assertNotIn(az.PERSON_FILE + '：', out)
        finally:
            os.unlink(path)


if __name__ == '__main__':
    unittest.main()
