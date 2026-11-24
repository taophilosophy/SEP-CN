# -*- coding: utf-8 -*-
"""著作名第三十四批 rowspec（2026-11-24）：Kitāb al-burhān 立册（池 held 项收口）。"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')

rows = [{
    'en': 'Kitāb al-burhān', 'zh': '《证明书》', 'table': 'term',
    'first_seen': '语料回收（specs/058 全库提取）',
    'basis': '本库译名（法拉比《证明书》；阿维森纳同名著作在 khunaji 条目作《证明之书》；'
             '语料《证明书》5 处、《证明之书》1 处；2026-11-24 核对，凭证 works-batch34-2026-11-24.md）',
    'date': '2026-11-24'}]
out = os.path.join(RES, 'rowspec-batch58-works34.json')
json.dump({'batch': '058-batch58-works34', 'date': '2026-11-24',
           'scope': '著作名第三十四批（Kitāb al-burhān 立册，池 held 收口）', 'rows': rows},
          io.open(out, 'w', encoding='utf-8', newline='\n'),
          ensure_ascii=False, indent=1)
print('rows=1 -> %s' % out)
