# -*- coding: utf-8 -*-
"""著作名第三十批补行（2026-11-24）：Cosmogony 概念行已被 peirce-benjamin 占用，书另立键。"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')

rows = [{
    'en': 'Cosmogony (Ehrenfels)', 'zh': '《宇宙发生论》', 'table': 'term',
    'first_seen': '语料回收（specs/058 全库提取）',
    'basis': '本库译名（厄棱费尔著；在册 cosmogony 为概念行“宇宙生成论”，书加人物括注分键；'
             '语料 6 处一致；2026-11-24 核对，凭证 works-batch30-2026-11-24.md）',
    'date': '2026-11-24'}]
out = os.path.join(RES, 'rowspec-batch58-works30b.json')
json.dump({'batch': '058-batch58-works30b', 'date': '2026-11-24',
           'scope': '著作名第三十批补行（Ehrenfels Cosmogony）', 'rows': rows},
          io.open(out, 'w', encoding='utf-8', newline='\n'),
          ensure_ascii=False, indent=1)
print('rows=1 -> %s' % out)
