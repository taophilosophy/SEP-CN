# -*- coding: utf-8 -*-
r"""019 探针：抓 MathJax v2 TeX input jax，确认 \amp 等宏是否在 v2 内建。"""
import os
import sys

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))))
sys.path.insert(0, REPO)
from tools import fetch as tf  # noqa: E402

DEST = os.path.join(REPO, 'state', 'mathval', 'js')
for path in ['MathJax/jax/input/TeX/jax.js']:
    url = 'https://plato.stanford.edu/' + path
    name = path.replace('/', '__')
    try:
        st, data = tf.get(url, dest=os.path.join(DEST, name))
        print(st, len(data or b''), name)
    except tf.FetchError as exc:
        print('ERR', getattr(exc, 'status', None), name)
