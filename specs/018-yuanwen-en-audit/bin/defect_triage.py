# -*- coding: utf-8 -*-
"""018 转换器缺陷分诊（020 移交清单四类 + \\( 残留分类）。

对给定 slug 的 en/<slug>/index.html 做深度感知扫描：
  表格：每个 <table> 按栈深度与最近容器归类（body 流 / td 嵌套 / li / dd /
        blockquote / figure / div 包装），并与镜像 md 表块数对照，定位丢失面。
  图片：en <img src> 与镜像 ../assets/<slug>/<src> 引用差集，附上文取样。
  \\(  ：镜像 md 里 \\( 出现处是否落在 $$…$$ 内（忠实嵌套）或独立泄漏。

用法: python specs/018-yuanwen-en-audit/bin/defect_triage.py <slug>...
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from tools.common import read_text, repo_path  # noqa: E402

TAG_RE = re.compile(r'<(/?)([a-zA-Z][a-zA-Z0-9]*)\b[^>]*?(/?)>', re.I)
BLOCK_CONTAINERS = ('blockquote', 'figure', 'li', 'dd', 'dt', 'td')
DIV_WRAP_RE = re.compile(r'class="[^"]*"|id="[^"]*"', re.I)


def table_contexts(html):
    """栈式扫描 → [(depth, ctx, pos)]。ctx = td|li|dd|dt|blockquote|figure|body。"""
    stack = []
    out = []
    for m in TAG_RE.finditer(html):
        close, name, selfclose = m.group(1), m.group(2).lower(), m.group(3)
        if name == 'table':
            if close:
                if stack and stack[-1][0] == 'table':
                    depth, ctx = stack.pop()[1:]
                    out.append((depth, ctx, m.start()))
            elif not selfclose:
                ctx = 'body'
                for nm, d, _ in reversed(stack):
                    if nm == 'table':
                        ctx = 'td'
                        break
                    if nm in ('li', 'dd', 'dt', 'blockquote', 'figure'):
                        ctx = nm
                        break
                    if nm == 'div':
                        # div 包装类（preamble/figure/wrapper）不拦；bibliography 记 div
                        ctx = 'div'
                        break
                stack.append(('table', len([1 for n, _, _ in stack if n == 'table']) + 1, ctx))
    return out


def md_table_blocks(md):
    return len(re.findall(r'(?:^\|.*\|$\n\|+ *---\|.*$)', md, re.M))


def main(argv):
    report = {}
    for slug in argv:
        rec = {}
        html = read_text(repo_path('en', slug, 'index.html'))
        md_path = repo_path('yuanwen', slug[0], slug + '.md')
        md = read_text(md_path) if os.path.exists(md_path) else ''
        ctxs = table_contexts(html)
        rec['en_tables'] = len(ctxs)
        rec['by_depth1_ctx'] = {}
        rec['nested_in_table'] = 0
        for depth, ctx, _ in ctxs:
            if depth == 1:
                rec['by_depth1_ctx'][ctx] = rec['by_depth1_ctx'].get(ctx, 0) + 1
            else:
                rec['nested_in_table'] += 1
        rec['md_tables'] = md_table_blocks(md)
        rec['md_nested_marks'] = md.count('（嵌套表：')

        # 图片差集
        en_imgs = [m.group(1) for m in re.finditer(r'<img[^>]*\ssrc="([^"]*)"', html, re.I)]
        en_imgs = [i.strip() for i in en_imgs]
        missing = []
        for src in en_imgs:
            base = os.path.basename(src)
            if not re.search(r'(?:^|[/\\])' + re.escape(base), md.replace('\\', '/')):
                missing.append(src)
        rec['en_imgs'] = len(en_imgs)
        rec['imgs_missing_from_md'] = missing[:6]
        rec['imgs_missing_n'] = len(missing)

        # \( 分类
        out_of_math = 0
        in_math = 0
        stripped = re.sub(r'\$\$.*?\$\$', lambda m: m.group(0).replace('\\(', '\x01').replace('\\)', '\x02'), md, flags=re.S)
        for m in re.finditer(re.escape('\\('), stripped):
            in_math += 1
        for m in re.finditer(re.escape('\\('), re.sub(r'\x01.*?\x02', '', stripped)):
            out_of_math += 1
        rec['backslash_paren'] = {'in_display_math': in_math, 'outside_math': out_of_math}
        report[slug] = rec
    print(json.dumps(report, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main(sys.argv[1:])
