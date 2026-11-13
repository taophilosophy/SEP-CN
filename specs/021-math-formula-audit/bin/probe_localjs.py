# -*- coding: utf-8 -*-
r"""019 探针：抓取 SEP 词条级 local.js 与 MathJax 配置，定位全站宏表。

SEP 页头 <script src="local.js"> 为词条专属，MathJax 宏（\amp、\osim 等）
通常在其中的 TeX 扩展配置或 /MathJax/config/ 里。
"""
import os
import sys

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))))
sys.path.insert(0, REPO)
from tools import fetch as tf  # noqa: E402

DEST = os.path.join(REPO, 'state', 'mathval', 'js')
os.makedirs(DEST, exist_ok=True)
pacer = tf.Pacer(5.0)
targets = [
    'https://plato.stanford.edu/entries/actualism-possibilism-ethics/local.js',
    'https://plato.stanford.edu/MathJax/config/TeX-MML-AM_CHTML.js',
    'https://plato.stanford.edu/MathJax/config/TeX-MML-AM_CHTML-full.js',
]
for url in targets:
    name = url.replace('https://plato.stanford.edu/', '').replace('/', '__')
    try:
        st, data = tf.get(url, dest=os.path.join(DEST, name), pacer=pacer)
        print(st, len(data or b''), name)
    except tf.FetchError as exc:
        print('ERR', getattr(exc, 'status', None), name)
