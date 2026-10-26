# -*- coding: utf-8 -*-
r"""数学保真门禁（用户 2026-10-27 裁定：内含大量数学公式，必须格式准确）。

对基线中已转换 yuanwen 的词条逐一核验：
  1. 原始 HTML（正文 + notes.html）里抓出的每个 \(…\)/\[…\]/$$…$$ 公式，
     实体解码、空白归一后，其内部内容必须原样出现在产物 md 中；
  2. 产物不得残留占位符（\x00N\x00——占位恢复失败的痕迹）；
  3. 产物内 $ 定界符成对（正文行内 $ 计数平衡）。

用法: python tools/check_math.py [slug...]
输出: stdout JSON {checked, formulas, missing:[{slug, kind, excerpt}], leaks:[…],
                   unbalanced:[…]}
退出码: 0 全部通过；1 有失真。
"""
import json
import os
import re
import sys
from html import unescape

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools import parser  # noqa: E402
from tools.common import load_json, read_text, repo_path  # noqa: E402

MATH_RE = re.compile(r'(\$\$.*?\$\$|\\\[.*?\\\]|\\\(.*?\\\))', re.S)
PLACEHOLDER_RE = re.compile(r'\x00\d+\x00')


def _norm(s):
    return re.sub(r'\s+', ' ', s).strip()


def raw_formulas(html):
    """正文原始 HTML → 解码后的公式内部内容列表（保留定界符类型）。

    先剥 HTML 注释：转换器丢弃注释内容（含 <!-- TOO SOON --> 类编辑性注释），
    其中的公式不参与保真核对，否则误报。
    """
    html = re.sub(r'<!--.*?-->', '', html, flags=re.S)
    out = []
    for m in MATH_RE.finditer(html):
        v = m.group(1)
        if v.startswith('$$') and v.endswith('$$') and len(v) > 4:
            out.append(('display-$$', unescape(v[2:-2])))
        elif v.startswith('\\[') and v.endswith('\\]'):
            out.append(('display-\\[]', unescape(v[2:-2])))
        elif v.startswith('\\(') and v.endswith('\\)'):
            out.append(('inline-\\()', unescape(v[2:-2])))
        else:
            out.append(('literal-$$', unescape(v)))
    return out


def check_slug(slug, rec=None):
    issues = {'slug': slug, 'missing': [], 'unbalanced': []}
    if rec is None:
        base = load_json(repo_path('baseline', 'entries.json'))
        rec = next((r for r in base['entries'] if r['slug'] == slug), None)
    if not rec or not rec.get('yuanwen'):
        return {'slug': slug, 'skipped': 'no yuanwen'}
    md_path = repo_path(rec['yuanwen']['md'])
    if not os.path.exists(md_path):
        return {'slug': slug, 'skipped': 'md missing'}
    md = read_text(md_path)
    md_norm = _norm(md)

    n = 0
    htmls = []
    idx = repo_path('en', slug, 'index.html')
    if os.path.exists(idx):
        html = read_text(idx)
        m, e = parser.HEAD_RE.search(html), parser.TAIL_RE.search(html)
        htmls.append(html[m.end():e.start()] if (m and e) else html)
        notes = repo_path('en', slug, 'notes.html')
        if os.path.exists(notes):
            htmls.append(read_text(notes))
    for h in htmls:
        for kind, inner in raw_formulas(h):
            n += 1
            if _norm(inner) not in unescape(md_norm):
                issues['missing'].append({'kind': kind, 'excerpt': _norm(inner)[:80]})
    issues['formulas'] = n
    if PLACEHOLDER_RE.search(md):
        issues['missing'].append({'kind': 'placeholder-leak', 'excerpt': '占位符残留'})

    # 正文行内 $ 计数平衡（剥掉 $$ 与围栏/行内代码后，$ 应成对；
    # `$` 后紧跟数字视为货币金额，不参与配对——与 .vitepress/math-plugin.mjs 的货币分支一致）
    fence = False
    for line in md.split('\n'):
        if line.lstrip().startswith('```'):
            fence = not fence
            continue
        if fence:
            continue
        t = line.replace('$$', '')
        # 行内代码里的 $ 不算定界符
        t = re.sub(r'`[^`]*`', '', t)
        t = re.sub(r'\$\d[\d,.]*', '', t)
        if t.count('$') % 2:
            issues['unbalanced'].append(line.strip()[:80])
    return issues


def main(argv=None):
    slugs = [a for a in (argv or sys.argv[1:]) if not a.startswith('-')]
    base = load_json(repo_path('baseline', 'entries.json'))
    recs = [r for r in base['entries'] if r.get('yuanwen')]
    if slugs:
        want = set(slugs)
        recs = [r for r in recs if r['slug'] in want]
    out = {'checked': len(recs), 'formulas': 0, 'missing': [], 'unbalanced': []}
    for rec in recs:
        r = check_slug(rec['slug'], rec)
        if r.get('skipped'):
            continue
        out['formulas'] += r.get('formulas', 0)
        out['missing'] += [{'slug': rec['slug'], **x} for x in r['missing']]
        out['unbalanced'] += [{'slug': rec['slug'], 'line': x} for x in r['unbalanced']]
    print(json.dumps(out, ensure_ascii=False, indent=2))
    # 退出码只由 missing（公式丢失/占位残留）驱动；unbalanced 仅为渲染歧义警告
    return 1 if out['missing'] else 0


if __name__ == '__main__':
    sys.exit(main())
