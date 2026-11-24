# -*- coding: utf-8 -*-
"""按批次 TSV 自动给 ALIGNED_SAME 行补审定凭证（选优：学科相关优先、非海峡两岸对照库优先）。
用法：python term_evidence_cite.py <queue.json> <out_dir> <batch_tsv_name>
"""
import io, json, os, re, sys, glob, unicodedata
sys.path.insert(0, '.')
from tools.register_lib import norm_key_quote, term_path

def fold(s):
    s = unicodedata.normalize('NFKD', s or '')
    s = ''.join(c for c in s if not unicodedata.combining(c))
    return re.sub(r'[^a-z0-9]+', '_', s.lower()).strip('_')

PRI = [('自然辩证法', 6), ('哲学', 6), ('逻辑', 5), ('伦理', 4), ('美学', 4), ('数学', 4),
       ('计算机', 4), ('语言学', 3), ('心理学', 3), ('物理学', 3), ('马克思主义', 3)]
q = json.load(io.open(sys.argv[1], encoding='utf-8'))
outdir, tsv = sys.argv[2], sys.argv[3]
files = {os.path.basename(f): f for f in glob.glob(os.path.join(outdir, '*.json'))}

def score(h):
    s = 0
    src = h.get('source') or ''
    sub = h.get('subjectFullName') or ''
    if '海峡两岸' in src: s -= 4
    for k, v in PRI:
        if k in src or k in sub: s += v
    y = str(h.get('publishYear') or '')
    if y.isdigit(): s += (int(y) - 1990) / 50.0
    return s

p = term_path()
lines = io.open(p, encoding='utf-8', newline='').read().split('\n')
idx = {}
for i, l in enumerate(lines):
    if l.startswith('| '):
        c = [x.strip() for x in l.strip().strip('|').split('|')]
        if len(c) == 6 and c[0]:
            idx.setdefault(norm_key_quote(c[0]), i)

def cn_norm(s): return re.sub(r'[\[\]［］\s]', '', s or '')
n = 0; skipped = []
for it in q:
    en, cn = it['en'], it.get('cn') or ''
    if not cn: continue
    fn = files.get(fold(en) + '.json')
    if not fn: continue
    d = json.load(io.open(fn, encoding='utf-8'))
    parts = [p2.strip().lower() for p2 in re.split(r'/', en)]
    al = []
    for h in d.get('hits', []):
        he = (h.get('en') or '').lower().strip()
        if any(p2 and (p2 == he or he.startswith(p2 + ' ') or p2 + 's' == he or p2 == he.split(';')[0].strip()) for p2 in parts):
            if cn_norm(h.get('cn')) == cn_norm(cn):
                al.append(h)
    if not al:
        skipped.append(en); continue
    h = max(al, key=score)
    num = '' if not h.get('wordNumber') else ' ' + str(h['wordNumber'])
    year = '' if str(h.get('publishYear')) in ('None', '', '暂无年份') else '，' + str(h['publishYear'])
    note = '审定名词库（termonline-all·%s%s%s）作“%s”，与本行一致（2026-11-24 JWT 直连，凭证 %s）' % (
        h.get('source'), num, year, h.get('cn'), tsv)
    i = idx.get(norm_key_quote(en))
    if i is None: continue
    c = [x.strip() for x in lines[i].strip().strip('|').split('|')]
    if note not in c[4]:
        c[4] = c[4].rstrip('；') + '；' + note
    lines[i] = '| ' + ' | '.join(c) + ' |'
    n += 1
io.open(p, 'w', encoding='utf-8', newline='').write('\n'.join(lines))
print('cited=%d skipped_same_check=%d' % (n, len(skipped)))
for k in skipped[:10]: print('  no-same-hit:', k)
