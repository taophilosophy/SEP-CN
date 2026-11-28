# -*- coding: utf-8 -*-
"""标记分叉定性：对 zh/yw 标记集的差键，抓 en 正文中的引证组语境。"""
import re
import sys

slug = sys.argv[1]
keys = sys.argv[2:]
t = open('en/%s/index.html' % slug, encoding='utf-8', errors='replace').read()
m = re.search(r'BEGIN ARTICLE HTML', t)
e = re.search(r'END ARTICLE HTML', t)
art = t[m.end():e.start()] if m and e else t
art = re.sub(r'<!--.*?-->', '', art, flags=re.S)
# 剥标签留文本
text = re.sub(r'</?[^>]+>', '', art)
text = re.sub(r'\s+', ' ', text)
import html as H
text = H.unescape(text)

SUR = {'clarke': 'Clarke', 'frankfurt': 'Frankfurt', 'lavin': 'Lavin',
       'setiya': 'Setiya', 'smith': 'Smith', 'brass': 'Brass',
       'grünbaum': 'Gr[üu]nbaum', 'hornsby': 'Hornsby', 'horschler': 'Horschler',
       'thompson': 'Thompson', 'vekony': 'Vekony'}
for k in keys:
    base = k.rsplit('-', 1)[0]
    year = k.rsplit('-', 1)[-1]
    sur = SUR.get(base.lower(), base.replace('-', ' ').title())
    pat = re.compile(r'\(?[^().]{0,140}?\b%s[^().]{0,80}?\b%s\b[^().]{0,40}?\)?' % (re.escape(sur), re.escape(year)))
    ms = list(pat.finditer(text))[:3]
    print('==', k)
    if not ms:
        print('   en 正文未找到该姓氏-年份组')
    for m in ms:
        print('   …' + text[max(0, m.start() - 60):m.end()][:230] + '…')
