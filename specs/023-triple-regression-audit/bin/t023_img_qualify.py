# -*- coding: utf-8 -*-
"""023 图片缺图定性：对 t020-img-rerun.txt 的每条「镜像缺图」，
检查 en 中该 <img> 是否在注释内（PDF 版专用，转换器剥注释属正确），
以及该文件名在 yw 中是否以任何形态在场。输出逐件判定。"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

# 从 rerun 报告取 slug → 缺图清单
slug = None
missing = {}
for ln in open(os.path.join(ROOT, 'specs', '023-triple-regression-audit', 'results', 't020-img-rerun.txt'), encoding='utf-8'):
    m = re.match(r'=====\s+(\S+)\s+=====', ln)
    if m:
        slug = m.group(1)
        missing.setdefault(slug, [])
    elif slug and '镜像缺图' in ln:
        missing[slug].append(ln.strip().split()[-1])

for slug, imgs in missing.items():
    letter = slug[0]
    p_en = os.path.join(ROOT, 'en', slug, 'index.html')
    p_yw = os.path.join(ROOT, 'yuanwen', letter, slug + '.md')
    en = open(p_en, encoding='utf-8', errors='replace').read()
    yw = open(p_yw, encoding='utf-8', errors='replace').read()
    print('=====', slug)
    for img in imgs:
        # en 中该文件名的所有 <img 出现位置，判注释包裹
        in_comment = False
        out_comment = False
        for m in re.finditer(r'<img\b[^>]*\bsrc="[^"]*' + re.escape(img), en, re.I):
            before = en[:m.start()]
            n_open = len(re.findall(r'<!--', before))
            n_close = len(re.findall(r'--!?>', before))  # HTML 注释尾可为 --> 或 --!>
            if n_open > n_close:
                in_comment = True
            else:
                out_comment = True
        present = img in yw
        status = []
        if out_comment:
            status.append('注释外有 img（应为真图）')
        if in_comment:
            status.append('PDF 注释内（豁免）')
        status.append('yw 在场' if present else 'yw 缺')
        print('  %-22s %s' % (img, '；'.join(status)))
