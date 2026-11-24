# -*- coding: utf-8 -*-
"""人名第二十五批（2026-11-24，中文源补证）：蒋庆生年、Hansen 汉名，新增 Goldin、Elga。"""
import io
import json
import os
import sys

sys.path.insert(0, '.')
from tools.register_lib import norm_key_quote, person_path

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')
EV = 'people-cnweb-2026-11-24-b25.md'

# 定点改写：(键, 新籍属 или None, 新生卒 или None, 新译法 или None, 追加依据)
FIX = [
    ('Jiang Qing', '中国（贵州贵阳）', '1953–', None,
     '中文源补证：中国孔子网人物页（chinakongzi.org，2012-12-25）“1953 年 10 月生，'
     '祖籍江苏徐州，出生、成长于贵州贵阳”；儒家网访谈（rujiazg.com/article/1235）'
     '记“一九五三年十月一日生”（2026-11-24 查，见 %s）' % EV),
    ('Chad Hansen', None, None, '陈汉生',
     '中文定名补证：中译本《中国古代的语言和逻辑》（周云之、张清宇、崔清田等译，'
     '社会科学文献出版社 1998）作者署名“陈汉生”（2026-11-24 查，见 %s）' % EV),
]

p = person_path()
lines = io.open(p, encoding='utf-8', newline='').read().split('\n')
idx = {}
for i, l in enumerate(lines):
    if l.startswith('| '):
        cells = [c.strip() for c in l.strip().strip('|').split('|')]
        if len(cells) == 8 and cells[0]:
            idx.setdefault(norm_key_quote(cells[0]), i)
n = 0
for key, aff, dates, zh, note in FIX:
    i = idx.get(norm_key_quote(key))
    if i is None:
        print('未找到', key)
        continue
    cells = [c.strip() for c in lines[i].strip().strip('|').split('|')]
    if zh:
        cells[2] = zh
    if aff:
        cells[3] = aff
    if dates:
        cells[4] = dates
    if note not in cells[6]:
        cells[6] = cells[6].rstrip('；') + '；' + note
    lines[i] = '| ' + ' | '.join(cells) + ' |'
    print('改行', key, '|', cells[2][:20], '|', cells[3], '|', cells[4])
    n += 1
io.open(p, 'w', encoding='utf-8', newline='').write('\n'.join(lines))

NEW = [
    ('Paul R. Goldin', '金鹏程', '美国', '—',
     '中文定名补证：中国人民大学国学院与古代文本研究中心页面均作“金鹏程（Paul R. '
     'Goldin）”，宾大 EALAC 教授、哈佛博士（2026-11-24 查，见 %s）；生年未见著录' % EV),
    ('Adam Elga', '亚当·埃尔加', '美国', '—',
     '中文通行译名（睡美人问题译介均作“亚当·埃尔加”）；生年未见权威著录，留白'
     '（2026-11-24 查，见 %s）' % EV),
]
rows = []
ev = ['en\tzh\taff\tdates']
for en, zh, aff, dates, note in NEW:
    rows.append({'en': en, 'zh': zh, 'table': 'person', 'affiliation': aff,
                 'dates': dates,
                 'basis': '学界通行译名；籍属/生卒联网查证（2026-11-24 查，凭证 %s）；%s'
                          % (EV, note),
                 'date': '2026-11-24'})
    ev.append('%s\t%s\t%s\t%s' % (en, zh, aff, dates))
out = os.path.join(RES, 'rowspec-batch57-people.json')
json.dump({'batch': '058-batch57-people', 'date': '2026-11-24',
           'scope': '人名第二十五批（中文源补证 2 改 2 增）', 'rows': rows},
          io.open(out, 'w', encoding='utf-8', newline='\n'),
          ensure_ascii=False, indent=1)
print('patch=%d rows=%d -> %s' % (n, len(rows), out))
