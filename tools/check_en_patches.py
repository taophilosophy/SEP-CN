#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""补丁池离线校验（ADR-0062）

用法: python tools/check_en_patches.py [--slug X] [--pool 路径]

逐条校验 baseline/en-patches.json 中每条格式层补丁在当前 en/ 上的命中计数
是否等于 expect（补丁池只承载格式层修正；文字层缺陷登记全局勘误表并以中文
译注承载，不入池）。失配即报——上游漂移或补丁失效时，转换层（yuanwen.py）
会硬失败，本工具供不转换时快速体检。

退出码: 0 全通过；1 有失配或无补丁池以外的异常；2 池文件缺失。
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import repo_path  # noqa: E402


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    only = None
    pool_path = repo_path('baseline', 'en-patches.json')
    i = 0
    while i < len(argv):
        if argv[i] == '--slug' and i + 1 < len(argv):
            only = argv[i + 1]
            i += 2
        elif argv[i] == '--pool' and i + 1 < len(argv):
            pool_path = argv[i + 1]
            i += 2
        else:
            sys.stderr.write(__doc__)
            return 2
    if not os.path.exists(pool_path):
        sys.stderr.write('[en-patches] 补丁池缺失: %s\n' % pool_path)
        return 2
    pool = json.load(open(pool_path, encoding='utf-8'))
    patches = pool.get('patches', [])
    bad = 0
    checked = 0
    for p in patches:
        if only and p['slug'] != only:
            continue
        full = repo_path(p['file'])
        if not os.path.exists(full):
            print('MISSING FILE %s（补丁 %s）' % (p['file'], p.get('id', '?')))
            bad += 1
            continue
        html = open(full, encoding='utf-8', newline='').read()
        n = html.count(p['find'])
        checked += 1
        if n != p['expect']:
            print('MISMATCH %s 补丁 %s 命中 %d 次 expect %d（上游漂移？）'
                  % (p['slug'], p.get('id', '?'), n, p['expect']))
            bad += 1
    print(json.dumps({'schema': pool.get('schema'), 'patches': len(patches),
                      'checked': checked, 'mismatch': bad},
                     ensure_ascii=False))
    return 0 if bad == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
