# -*- coding: utf-8 -*-
r"""021 en 失败归类：区分「v2 扩展/包依赖」与「上游真语法错」。

SEP 用 MathJax v2 + 每词条 local.js；v2 的扩展（sc.js、xypic、bussproofs 等）
在 v3 无对应，故 v3 下的 Undefined 不等于上游坏。判据：
  * local.js 含 extensions/packages 声明，且缺失宏名属该扩展的已知符号表
    → ext-dependency（上游可渲染，本库 v3 不可）
  * 其余编译错（Misplaced &、Missing close brace、实体残留等）→ upstream-defect
输出 results/en-fail-classified.jsonl 与汇总。
"""
import collections
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RESULTS = os.path.join(HERE, '..', 'results')
MACRO_DIR = os.path.join(REPO, 'state', 'mathval', 'macros')

# v2 扩展/包及其提供的主要符号（保守表）
EXT_SYMBOLS = {
    'sc': {'sc'},
    'xypic': {'xymatrix', 'ar', 'entry', 'ar@'},
    'bussproofs': {'AxiomC', 'UnaryInfC', 'BinaryInfC', 'TrinaryInfC', 'noLine',
                   'prooftree', 'LeftLabel', 'RightLabel', 'DisplayProof'},
    'infer': {'infer'},
    'squarear': {'squarear'},
    'extpfeil': {'xlongequal', 'xtwoheadrightarrow', 'xhookrightarrow'},
    'centernot': {'centernot'},
    'color': {'color', 'textcolor'},
    'unicode': {'unicode'},
    'mathrsfs': {'mathscr'},
    'autoload': set(),
}
UNDEF_RE = re.compile(r'Undefined control sequence \\?([A-Za-z]+)')


def ext_names(slug):
    path = os.path.join(MACRO_DIR, slug + '.js')
    if not os.path.exists(path):
        return set()
    text = open(path, encoding='utf-8', errors='replace').read()
    names = set()
    for m in re.finditer(r'extensions\s*:\s*\[([^\]]*)\]', text):
        for part in re.findall(r'"([^"]+)"', m.group(1)):
            names.add(part.replace('.js', ''))
    for m in re.finditer(r'packages[^:]*:\s*\{[^}]*\}\s*,\s*|\'\[\+\]\'\s*:\s*\[([^\]]*)\]',
                         text):
        if m.group(1):
            for part in re.findall(r"'([^']+)'", m.group(1)):
                names.add(part)
    for m in re.finditer(r"load\s*:\s*\[([^\]]*)\]", text):
        for part in re.findall(r"'\[tex\]/([^']+)'", m.group(1)):
            names.add(part)
    return names


def main():
    rows = [json.loads(l) for l in open(os.path.join(RESULTS, 'en-render-fail.jsonl'),
                                        encoding='utf-8')]
    ext_cache = {}
    summary = collections.Counter()
    out = open(os.path.join(RESULTS, 'en-fail-classified.jsonl'), 'w',
               encoding='utf-8')
    for r in rows:
        slug = r['f'].split('/')[0]
        if slug not in ext_cache:
            ext_cache[slug] = ext_names(slug)
        exts = ext_cache[slug]
        m = UNDEF_RE.search(r['err'])
        cls = 'upstream-defect'
        why = r['err'][:80]
        if m:
            sym = m.group(1)
            hit = [e for e in exts if sym in EXT_SYMBOLS.get(e, set())]
            if hit:
                cls = 'ext-dependency'
                why = f'{sym} ← {hit[0]}'
            elif exts:
                cls = 'ext-dependency?'
                why = f'{sym}（词条声明 {"/".join(sorted(exts))}，符号未在已知表）'
        elif 'Cannot read properties of null' in r['err']:
            cls = 'control-char-or-unicode'
            why = 'v3 内部异常（多为不可见字符/整数实体）'
        summary[cls] += 1
        out.write(json.dumps({'f': r['f'], 'i': r['i'], 'cls': cls, 'why': why,
                              'x': r['x'][:200]}, ensure_ascii=False) + '\n')
    out.close()
    print(json.dumps(summary, ensure_ascii=False, indent=1))
    # 逐词条
    per = collections.Counter()
    for line in open(os.path.join(RESULTS, 'en-fail-classified.jsonl'), encoding='utf-8'):
        r = json.loads(line)
        per[(r['f'], r['cls'])] += 1
    for (f, c), n in per.most_common(12):
        print(f'{n:4d} {c:22s} {f}')


if __name__ == '__main__':
    main()
