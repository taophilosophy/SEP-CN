# -*- coding: utf-8 -*-
r"""019 战役普查：en/ HTML 与中文译文侧公式全量清点（禁抽样，逐个计数）。

用法:
  python census.py en    → 扫 en/<slug>/*.html，产 results/en-census.json
  python census.py zh    → 扫 <letter>/<slug>.md（含 $ 定界符的文件全扫），
                           产 results/zh-census.json
  python census.py yw    → 扫 yuanwen/<letter>/<slug>.md，产 results/yw-census.json

只统计与取证，不改任何文件。公式判定与 tools/check_math.py 同口径：
\(…\) 行内、\[…\] 展示、$$…$$ 展示；en/ 侧另探 <script type="math/tex">、
<math>、单 $；zh/ 侧单 $ 为行内公式正文口径（rules/02：真公式入 $…$）。
"""
import json
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))))

INLINE_RE = re.compile(r'\\\((.+?)\\\)', re.S)
DISPLAY_RE = re.compile(r'\\\[(.+?)\\\]', re.S)
DDOLLAR_RE = re.compile(r'\$\$(.+?)\$\$', re.S)
SDOLLAR_RE = re.compile(r'(?<!\$)\$(?!\$)([^$\n]+?)\$(?!\$)')
SCRIPT_TEX_RE = re.compile(r'<script[^>]*type="math/tex[^"]*"[^>]*>(.*?)</script>', re.S)
MATHML_RE = re.compile(r'<math[>\s]')
TEXT_IN_MATH_RE = re.compile(r'\\(?:text|mbox|operatorname\*?|mathrm)\s*\{([^{}]*)\}')

EN_KINDS = ('inline', 'display', 'ddollar', 'sdollar', 'script_tex', 'mathml')
ZH_KINDS = ('inline', 'display', 'ddollar', 'sdollar')


def scan_file(path, kinds):
    try:
        with open(path, encoding='utf-8') as fh:
            txt = fh.read()
    except UnicodeDecodeError:
        with open(path, encoding='utf-8', errors='replace') as fh:
            txt = fh.read()
    pats = {'inline': INLINE_RE, 'display': DISPLAY_RE, 'ddollar': DDOLLAR_RE,
            'sdollar': SDOLLAR_RE, 'script_tex': SCRIPT_TEX_RE, 'mathml': MATHML_RE}
    out = {}
    bodies = []
    for k in kinds:
        ms = pats[k].findall(txt)
        out[k] = len(ms)
        if k in ('inline', 'display', 'ddollar', 'sdollar', 'script_tex'):
            bodies.extend(ms if k != 'mathml' else [])
    text_hits = TEXT_IN_MATH_RE.findall('\n'.join(bodies))
    out['text_in_math'] = len(text_hits)
    out['text_samples'] = sorted({t.strip() for t in text_hits})[:12]
    return out


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else 'en'
    per_file = {}
    if mode == 'en':
        root = os.path.join(REPO, 'en')
        kinds = EN_KINDS
        for slug in sorted(os.listdir(root)):
            d = os.path.join(root, slug)
            if not os.path.isdir(d):
                continue
            for name in sorted(os.listdir(d)):
                if name.endswith('.html'):
                    rel = f'{slug}/{name}'
                    per_file[rel] = scan_file(os.path.join(d, name), kinds)
    else:
        root = os.path.join(REPO, 'yuanwen') if mode == 'yw' else REPO
        kinds = ZH_KINDS
        for letter in sorted(os.listdir(root)):
            d = os.path.join(root, letter)
            if not (os.path.isdir(d) and len(letter) == 1 and letter.isalpha()):
                continue
            for name in sorted(os.listdir(d)):
                if name.endswith('.md'):
                    rel = f'{letter}/{name}'
                    per_file[rel] = scan_file(os.path.join(d, name), kinds)

    totals = {k: sum(v[k] for v in per_file.values()) for k in kinds}
    totals['text_in_math'] = sum(v['text_in_math'] for v in per_file.values())
    n_with = sum(1 for v in per_file.values()
                 if any(v[k] for k in kinds))
    hot = sorted(per_file.items(),
                 key=lambda kv: -sum(kv[1][k] for k in kinds))[:25]
    report = {
        'files_scanned': len(per_file),
        'files_with_math': n_with,
        'totals': totals,
        'top25': {rel: {k: v[k] for k in kinds} for rel, v in hot},
        'text_samples_global': sorted(
            {s for v in per_file.values() for s in v['text_samples']})[:80],
    }
    dest = os.path.join(REPO, 'specs', '021-math-formula-audit', 'results',
                        f'{mode}-census.json')
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, 'w', encoding='utf-8') as fh:
        json.dump({'per_file': per_file, 'report': report}, fh,
                  ensure_ascii=False, indent=1)
    print(json.dumps(report, ensure_ascii=False, indent=1)[:2600])


if __name__ == '__main__':
    main()
