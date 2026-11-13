# -*- coding: utf-8 -*-
"""图片丢弃上下文诊断：en <img> 在镜像无引用者，打印其上文与 src 形态。"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from tools.common import read_text, repo_path  # noqa: E402

for slug in sys.argv[1:]:
    html = read_text(repo_path('en', slug, 'index.html'))
    md = read_text(repo_path('yuanwen', slug[0], slug + '.md'))
    miss = []
    for m in re.finditer(r'<img[^>]*\ssrc="([^"]*)"[^>]*>', html, re.I):
        src = m.group(1).strip()
        if src.startswith(('http', '../')):
            continue
        base = os.path.basename(src)
        if not re.search(r'(?:^|[/\\])' + re.escape(base), md.replace('\\', '/')):
            ctx = html[max(0, m.start() - 200):m.start()].replace('\n', ' ')[-140:]
            miss.append((src, ctx))
    print(f'== {slug}: 丢失 {len(miss)}')
    for src, ctx in miss[:4]:
        print(f'   src={src}')
        print(f'   前文: …{ctx}')
