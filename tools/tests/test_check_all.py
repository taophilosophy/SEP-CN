# -*- coding: utf-8 -*-
"""check_all 的 CI 矩阵数据源单测（ADR-0061）。

`--list-gates` 是 `.github/workflows/checks.yml` 门禁矩阵的唯一事实源：这里守住
「单行 JSON、键唯一、命令引用的脚本真实存在」三条，防止改门禁时 CI 静默跑空。
"""
import json
import os
import subprocess
import sys
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def list_gates():
    r = subprocess.run([sys.executable, os.path.join(REPO, 'tools', 'check_all.py'),
                        '--list-gates'], cwd=REPO, capture_output=True)
    return r


class GateMatrixTest(unittest.TestCase):
    def setUp(self):
        self.r = list_gates()

    def test_exit_ok(self):
        self.assertEqual(self.r.returncode, 0,
                         self.r.stderr.decode('utf-8', 'replace'))

    def test_single_line_json(self):
        # GITHUB_OUTPUT 只接受单行值；换行会截断矩阵
        out = self.r.stdout.decode('utf-8')
        self.assertNotIn('\n', out)
        self.assertTrue(out.strip().startswith('{'))

    def test_entries_shape(self):
        data = json.loads(self.r.stdout.decode('utf-8'))
        items = data['include']
        self.assertTrue(items)
        keys = [i['key'] for i in items]
        self.assertEqual(len(keys), len(set(keys)), keys)
        for it in items:
            self.assertEqual(set(it), {'key', 'name', 'run'})
            self.assertTrue(it['name'])
            self.assertTrue(it['run'].startswith('python '))
            self.assertEqual(it['key'], it['key'].lower())
            self.assertTrue(it['key'].replace('-', '').isalnum())

    def test_commands_point_to_existing_scripts(self):
        data = json.loads(self.r.stdout.decode('utf-8'))
        tool_cmds = [i['run'].split()[1] for i in data['include']
                     if i['run'].startswith('python tools/')]
        self.assertTrue(tool_cmds)
        for path in tool_cmds:
            self.assertTrue(os.path.isfile(os.path.join(REPO, path)), path)

    def test_unit_tests_entry_present(self):
        data = json.loads(self.r.stdout.decode('utf-8'))
        by_key = {i['key']: i for i in data['include']}
        self.assertIn('unittest', by_key)
        self.assertIn('unittest', by_key['unittest']['run'])


if __name__ == '__main__':
    unittest.main()
