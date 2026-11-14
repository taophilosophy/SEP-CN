# -*- coding: utf-8 -*-
r"""022 建文献节：zh 无 ## 参考文献节时，按模板节头＋yw defs 照录整节建入（追加在正文后/学术工具前）。

用法: python -I specs/022/bin/build_refs.py <slug>... [--apply]
防线：yw defs 含汉字条目时拒绝（中国文献须人工翻译，不在此列）；幂等（已有节跳过）。
"""
import io
import os
import re
import sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from copy_defs import yw_def_blocks, read, write  # noqa

CJK = re.compile(r'[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]')
NOTE = '**以下非中文文献条目从原文照录，不作翻译；中国文献条目一律译为中文（本条无中国文献）。**'


def build(slug, apply=False):
    letter = slug[0]
    zh_p = os.path.join(ROOT, letter, slug + '.md')
    yw_p = os.path.join(ROOT, 'yuanwen', letter, slug + '.md')
    zh, yw = read(zh_p), read(yw_p)
    if re.search(r'^##\s*(参考文献|References)', zh, re.M):
        return 'exists'
    blocks = yw_def_blocks(yw)
    if not blocks:
        return 'no-defs-in-yw'
    cjk = [k for k, b in blocks if CJK.search(b)]
    if cjk:
        return 'reject-cjk(%d)' % len(cjk)
    sec = '## 参考文献\n\n' + NOTE + '\n\n' + '\n\n'.join(b for _, b in blocks) + '\n\n'
    if not apply:
        return 'plan: %d defs' % len(blocks)
    # 插入位：## 学术工具/Academic 之前；否则文末
    m = re.search(r'^##\s*(学术工具|Academic Tools?)', zh, re.M)
    if m:
        zh2 = zh[:m.start()] + sec + zh[m.start():]
    else:
        zh2 = zh.rstrip('\n') + '\n\n' + sec
    write(zh_p, zh2)
    return 'built: %d defs' % len(blocks)


if __name__ == '__main__':
    apply = '--apply' in sys.argv
    for slug in [a for a in sys.argv[1:] if not a.startswith('--')]:
        print('%-24s %s' % (slug, build(slug, apply=apply)))
