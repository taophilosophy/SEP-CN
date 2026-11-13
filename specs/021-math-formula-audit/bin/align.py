# -*- coding: utf-8 -*-
r"""019 公式序列对齐器：en↔zh（译文复核）与 en↔upstream（联网比对）。

用法:
  python -I align.py zh
      en-formulas.jsonl(快照) ↔ render-zh.jsonl，逐词条 difflib 序列对齐。
      zh 文件 <letter>/<slug>.md ↔ en <slug>/index.html（补篇回退同名/尾段名）。
  python -I align.py upstream
      en-formulas.jsonl(快照) ↔ upstream-formulas.jsonl。
      index.html ↔ 上游 <slug>.html；子页 ↔ 上游 <slug>/<name>。

公式体剥定界符后：空白归一相等 → identical；剥 \text{…}/\mbox{…} 等文字壳
后相等 → text-diff（公式内文字差异，翻译体例作用面）；其余 → structural
（note 双侧留痕）。序列差异经 SequenceMatcher 消化插入/删除，不再逐位错位。
产: results/align-<mode>.jsonl + stdout 汇总。
"""
import difflib
import json
import os
import re
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, '..', 'results')

WS_RE = re.compile(r'\s+')
TEXTISH_RE = re.compile(
    r'\\(?:text|mbox|textnormal|mathrm|textrm|operatorname\*?)\s*\{[^{}]*\}')


def norm(s):
    return WS_RE.sub(' ', s).strip()


def skel(s):
    return norm(TEXTISH_RE.sub('', s))


def strip_delims(kind, x):
    r"""剥定界符：en 为 \(…\)/\[…\]/$$…$$，zh/yw 为 $…$/$$…$$。"""
    if kind == 'display':
        if x.startswith('$$') and x.endswith('$$'):
            return x[2:-2]
        if x.startswith('\\[') and x.endswith('\\]'):
            return x[2:-2]
    else:
        if x.startswith('\\(') and x.endswith('\\)'):
            return x[2:-2]
        if x.startswith('$') and x.endswith('$'):
            return x[1:-1]
    return x


def load(path):
    seq = {}
    with open(path, encoding='utf-8') as fh:
        for line in fh:
            r = json.loads(line)
            if r.get('k') == 'paren':
                continue
            seq.setdefault(r['f'], []).append(
                (r['k'], strip_delims(r['k'], r['x'])))
    return seq


def verdict(ex, zx):
    na, nb = norm(ex), norm(zx)
    if na == nb:
        return 'identical', ''
    if skel(ex) == skel(zx):
        return 'text-diff', f'EN: {na} || ZH: {nb}'
    return 'structural', f'EN: {na} || ZH: {nb}'


def align_pair(out, key, slug, eseq, zseq, summary):
    a = [norm(x) for _, x in eseq]
    b = [norm(x) for _, x in zseq]
    sm = difflib.SequenceMatcher(a=a, b=b, autojunk=False)
    idx = 0
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == 'equal':
            for k in range(i2 - i1):
                summary['identical'] += 1
                out.write(json.dumps({'key': key, 'slug': slug, 'i': idx,
                                      'v': 'identical', 'note': ''},
                                     ensure_ascii=False) + '\n')
                idx += 1
        elif tag == 'insert':
            for j in range(j1, j2):
                summary['extra-in-zh'] += 1
                out.write(json.dumps(
                    {'key': key, 'slug': slug, 'i': idx, 'v': 'extra-in-zh',
                     'note': f'ZH: {b[j]}'}, ensure_ascii=False) + '\n')
                idx += 1
        elif tag == 'delete':
            for i in range(i1, i2):
                summary['missing-in-zh'] += 1
                out.write(json.dumps(
                    {'key': key, 'slug': slug, 'i': idx, 'v': 'missing-in-zh',
                     'note': f'EN: {a[i]}'}, ensure_ascii=False) + '\n')
                idx += 1
        else:  # replace
            n = max(i2 - i1, j2 - j1)
            for k in range(n):
                if i1 + k >= i2:
                    summary['extra-in-zh'] += 1
                    out.write(json.dumps(
                        {'key': key, 'slug': slug, 'i': idx,
                         'v': 'extra-in-zh', 'note': f'ZH: {b[j1 + k]}'},
                        ensure_ascii=False) + '\n')
                elif j1 + k >= j2:
                    summary['missing-in-zh'] += 1
                    out.write(json.dumps(
                        {'key': key, 'slug': slug, 'i': idx,
                         'v': 'missing-in-zh', 'note': f'EN: {a[i1 + k]}'},
                        ensure_ascii=False) + '\n')
                else:
                    (ek, ex), (zk, zx) = eseq[i1 + k], zseq[j1 + k]
                    if ek != zk:
                        v = 'kind-mismatch'
                        note = f'{ek}↔{zk}: EN: {norm(ex)} || ZH: {norm(zx)}'
                    else:
                        v, note = verdict(ex, zx)
                    summary[v] += 1
                    out.write(json.dumps(
                        {'key': key, 'slug': slug, 'i': idx, 'v': v,
                         'note': note[:400]}, ensure_ascii=False) + '\n')
                idx += 1


def pair_files(en, zh):
    mapping = {}
    for f in zh:
        base = f[2:-3]  # <letter>/<slug>.md → <slug>
        slug = base.split('.')[0]
        parts = base.split('.')
        cand = [f'{slug}/index.html', f'{slug}/{base}.html']
        if len(parts) > 1:
            cand.append(f'{slug}/{parts[-1]}.html')
        hit = next((c for c in cand if c in en), None)
        mapping[f] = (slug, hit)
    return mapping


def run_zh():
    en = load(os.path.join(RESULTS, 'en-formulas.jsonl'))
    zh = load(os.path.join(RESULTS, 'render-zh.jsonl'))
    mapping = pair_files(en, zh)
    out = open(os.path.join(RESULTS, 'align-zh.jsonl'), 'w', encoding='utf-8')
    summary = Counter()
    no_en = []
    for f, zseq in sorted(zh.items()):
        slug, hit = mapping[f]
        if hit is None:
            summary['no-en-source'] += 1
            no_en.append(f)
            continue
        summary['files'] += 1
        align_pair(out, f, slug, en[hit], zseq, summary)
    out.close()
    print(json.dumps(summary, ensure_ascii=False, indent=1))
    if no_en:
        print('no-en-source files:', no_en[:20])


def run_upstream():
    en = load(os.path.join(RESULTS, 'en-formulas.jsonl'))
    up = load(os.path.join(RESULTS, 'upstream-formulas.jsonl'))
    up_by_rel = {}
    for f, seq in up.items():
        slug = f.split('/')[0]
        if f == f'{slug}/{slug}.html' or f == f'{slug}/index.html':
            rel = f'{slug}/index.html'
        else:
            rel = f
        up_by_rel[rel] = seq
    out = open(os.path.join(RESULTS, 'align-upstream.jsonl'), 'w',
               encoding='utf-8')
    summary = Counter()
    for f, eseq in sorted(en.items()):
        useq = up_by_rel.get(f)
        if useq is None:
            summary['upstream-missing'] += 1
            continue
        summary['files-compared'] += 1
        summary['en'] += len(eseq)
        summary['upstream'] += len(useq)
        align_pair(out, f, f.split('/')[0], eseq, useq, summary)
    out.close()
    print(json.dumps(summary, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else 'zh'
    (run_zh if mode == 'zh' else run_upstream)()
