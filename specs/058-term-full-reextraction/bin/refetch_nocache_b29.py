# -*- coding: utf-8 -*-
"""批 29 收尾：为 34 个无缓存键补抓 termonline-all 凭证（JWT 从 .secrets 内存读，不落盘不入日志）。"""
import io
import json
import os
import sys

sys.path.insert(0, '.')
sys.stdout.reconfigure(encoding='utf-8')

TSV = 'specs/058-term-full-reextraction/results/auto-basis-reaudit-2026-11-25.tsv'
keys = [l.split('\t')[0] for l in io.open(TSV, encoding='utf-8')
        if l.rstrip('\n').endswith('\tnocache')]
print('待抓', len(keys))
d = json.load(io.open('.secrets/termonline-session.json', encoding='utf-8'))
os.environ['TERMONLINE_TOKEN'] = d['jwt']
from tools import cnki_query  # noqa: E402

argv = ['--provider', 'termonline-all', '--terms'] + keys
print('退出码', cnki_query.main(argv))
