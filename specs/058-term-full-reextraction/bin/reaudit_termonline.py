# -*- coding: utf-8 -*-
"""审计首批 102 条：找出审定库中对口但此前未采的命中（变体形/学科对口）。"""
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
from tools.cnki_query import safe_key  # noqa: E402
from tools.register_lib import norm_key_quote  # noqa: E402

RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')
QD = os.path.join(ROOT, 'specs', '008-terminology-campaign', 'results',
                  'queries', 'termonline-all')
PHIL = ('哲学', '自然辩证法', '逻辑', '伦理', '美学', '宗教', '心理', '语言',
        '科学哲学', '技术哲学', '认知科学', '马克思主义', '外国哲学', '思维',
        '方法论', '辩证法')


def variants(en):
    base = en.casefold().strip()
    out = {base}
    if base.endswith('ies'):
        out.add(base[:-3] + 'y')
    if base.endswith('es'):
        out.add(base[:-2])
    if base.endswith('s'):
        out.add(base[:-1])
    out.add(base + 's')
    out.add('law of ' + base)
    out.add('the ' + base)
    out.add(base.replace(' ', '-'))
    out.add(base.replace('-', ' '))
    return out


rows = []
for line in open(os.path.join(RES, 'curated-translations.tsv'),
                 encoding='utf-8'):
    if not line.strip():
        continue
    en, zh = line.rstrip('\n').split('\t')
    path = os.path.join(QD, safe_key(norm_key_quote(en)) + '.json')
    if not os.path.exists(path):
        continue
    doc = json.load(open(path, encoding='utf-8'))
    vs = variants(en)
    cand = []
    for h in doc.get('hits') or []:
        hen = (h.get('en') or '').strip().casefold()
        subj = (h.get('subjectFullName') or '') + (h.get('subjectName') or '')
        if hen in vs and any(p in subj + (h.get('source') or '') for p in PHIL):
            cand.append(h)
    if cand:
        for h in cand[:3]:
            rows.append((en, zh, h['cn'], h.get('en') or '',
                         h.get('source') or '', (h.get('subjectName') or '')[:24],
                         h.get('publishYear') or '', (h.get('definition') or '')[:40]))
out = ['en\tours\tcn\thit_en\tsource\tsubject\tyear\tdefinition']
for r in rows:
    out.append('\t'.join(str(x).replace('\t', ' ') for x in r))
open(os.path.join(RES, 'termonline-reaudit.tsv'), 'w', encoding='utf-8',
     newline='\n').write('\n'.join(out) + '\n')
print('对口候选行 %d，覆盖词条 %d' % (len(rows), len({r[0] for r in rows})))
for r in rows[:40]:
    print('%s | 我方 %s | 审定 %s | %s | %s' % (r[0], r[1], r[2], r[4], r[5]))
