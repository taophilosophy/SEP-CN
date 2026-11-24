# -*- coding: utf-8 -*-
"""术语依据补证批次：termonline 抓取结果 → 对齐判定 TSV。
用法：python term_evidence_batch.py <queue.json> <out_dir> <out.tsv> <批次标签>
"""
import io, json, os, re, sys, glob, unicodedata

def fold(s):
    s = unicodedata.normalize('NFKD', s or '')
    s = ''.join(c for c in s if not unicodedata.combining(c))
    return re.sub(r'[^a-z0-9]+', '_', s.lower()).strip('_')

def cn_norm(s):
    s = re.sub(r'[\[\]［］]', '', s or '')
    return re.sub(r'\s+', '', s)

q = json.load(io.open(sys.argv[1], encoding='utf-8'))
outdir, outtsv, tag = sys.argv[2], sys.argv[3], sys.argv[4]
files = {os.path.basename(f): f for f in glob.glob(os.path.join(outdir, '*.json'))}

rows = []
for it in q:
    en, cn = it['en'], it['cn']
    fn = files.get(fold(en) + '.json')
    if not fn:
        for base, f in files.items():
            if base.startswith(fold(en)[:18]):
                fn = f; break
    st, aligned = ('NOFILE', []) if not fn else (None, [])
    if fn:
        d = json.load(io.open(fn, encoding='utf-8'))
        st = d.get('status')
        parts = [p.strip().lower() for p in re.split(r'/', en)]
        for h in d.get('hits', []):
            he = (h.get('en') or '').lower().strip()
            if any(p and (p == he or he.startswith(p + ' ') or p + 's' == he or p == he.split(';')[0].strip()) for p in parts):
                aligned.append(h)
    same = [h for h in aligned if cn_norm(h.get('cn')) == cn_norm(cn)]
    if same:
        verdict = 'ALIGNED_SAME'
    elif aligned:
        verdict = 'ALIGNED_DIFF'
    elif st == 'empty':
        verdict = 'EMPTY'
    else:
        verdict = 'NO_ALIGNED'
    top = (same or aligned)[:3]
    hits = ' ; '.join('%s<=%s|%s|%s|%s' % (h.get('cn'), (h.get('en') or ''), h.get('source'),
                                            h.get('wordNumber'), h.get('publishYear')) for h in top)
    rows.append((en, cn, st, verdict, hits))

with io.open(outtsv, 'w', encoding='utf-8', newline='\n') as f:
    f.write('en\tcurrent_cn\tstatus\tverdict\taligned_hits\n')
    for r in rows:
        f.write('\t'.join(x or '' for x in r) + '\n')

from collections import Counter
print(tag, Counter(r[3] for r in rows))
for r in rows:
    if r[3] in ('ALIGNED_DIFF', 'ALIGNED_SAME'):
        print(' ', r[3], r[0], '|', r[1], '|', r[4][:150])
