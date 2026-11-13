# -*- coding: utf-8 -*-
"""pdf 开关语境下的图片归属判定：
对每个 en <img>，判定它落在注释内（PDF 专版）还是注释外（浏览器可见），
再核对镜像是否引用了浏览器可见版本；BNfiles 类无扩展名/路径形 src 单列。
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from tools.common import read_text, repo_path  # noqa: E402

# 全文按浏览器语义划区：注释区 / 可见区
def visible_segments(html):
    out, last = [], 0
    for m in re.finditer(r'<!--.*?-->', html, re.S):
        out.append((last, m.start()))
        last = m.end()
    out.append((last, len(html)))
    return out

def in_visible(pos, segs):
    return any(a <= pos < b for a, b in segs)

for slug in sys.argv[1:]:
    html = read_text(repo_path('en', slug, 'index.html'))
    md_path = repo_path('yuanwen', slug[0], slug + '.md')
    md = read_text(md_path).replace('\\', '/') if os.path.exists(md_path) else ''
    segs = visible_segments(html)
    vis, hidden, missing_vis = [], [], []
    for m in re.finditer(r'<img[^>]*\ssrc="([^"]*)"[^>]*>', html, re.I):
        src = m.group(1).strip()
        (vis if in_visible(m.start(), segs) else hidden).append(src)
        if in_visible(m.start(), segs):
            base = os.path.basename(src)
            if not re.search(r'(?:^|[/\\])' + re.escape(base), md):
                missing_vis.append(src)
    print(f'== {slug}: 浏览器可见 img={len(vis)} 注释内 img={len(hidden)} 可见但镜像缺引={len(missing_vis)}')
    if missing_vis:
        for s in missing_vis[:6]:
            print('   缺引:', s)
    if hidden:
        print('   注释内(PDF专版,应丢):', sorted(set(os.path.basename(s) for s in hidden)))
