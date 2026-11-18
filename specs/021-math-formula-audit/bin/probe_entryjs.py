# -*- coding: utf-8 -*-
r"""019 探针：抓 SEP 全站 js/entry.js（可能含 MathJax 宏配置）。"""
import os
import sys

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))))
sys.path.insert(0, REPO)
from tools import fetch as tf  # noqa: E402

DEST = os.path.join(REPO, 'state', 'mathval', 'js')
for path in ['js/entry.js']:
    url = 'https://plato.stanford.edu/' + path
    name = 'site__' + path.replace('/', '__')
    try:
        st, data = tf.get(url, dest=os.path.join(DEST, name))
        print(st, len(data or b''), name)
    except tf.FetchError as exc:
        print('ERR', getattr(exc, 'status', None), name)
