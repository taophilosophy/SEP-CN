# -*- coding: utf-8 -*-
"""yuanwen 镜像 \\( 残留全量分类：$$…$$ 内（忠实嵌套）vs 外（泄漏）。

另对每文件统计 \\[ 同类情况。输出汇总 + 泄漏样本行。
"""
import os
import re
import sys

BACKSLASH_PAREN = re.compile(r'\\\(')
BACKSLASH_BRACKET = re.compile(r'\\\[')
DISPLAY_RE = re.compile(r'\$\$.*?\$\$', re.S)

files = []
for root, dirs, fns in os.walk('yuanwen'):
    for fn in fns:
        if fn.endswith('.md'):
            p = os.path.join(root, fn)
            with open(p, encoding='utf-8', errors='replace') as f:
                t = f.read()
            if '\\(' in t or '\\[' in t:
                files.append((p, t))

print('含 \\(/\\[ 的镜像文件数:', len(files))
tot_pin = tot_pout = tot_bin_ = tot_bout = 0
leak_samples = []
for p, t in files:
    stash = []

    def _stash(m):
        stash.append(m.group(0))
        return '\x00D%d\x00' % (len(stash) - 1)

    t2 = DISPLAY_RE.sub(_stash, t)
    t3 = re.sub(r'\x00D\d+\x00', '', t2)
    pin = sum(s.count('\\(') for s in stash)
    pout = len(BACKSLASH_PAREN.findall(t3))
    bin_ = sum(s.count('\\[') for s in stash)
    bout = len(BACKSLASH_BRACKET.findall(t3))
    tot_pin += pin
    tot_pout += pout
    tot_bin_ += bin_
    tot_bout += bout
    if pout or bout:
        m2 = re.search(r'^.*\\(?:\(|\[).*$', t3, re.M)
        leak_samples.append((p, pout, bout, m2.group(0)[:150] if m2 else ''))

print('\\( 总计: $$内', tot_pin, '/ $$外', tot_pout)
print('\\[ 总计: $$内', tot_bin_, '/ $$外', tot_bout)
print('--- 泄漏文件明细（前 25）---')
for p, po, bo, s in leak_samples[:25]:
    kind = ('\\(×%d ' % po if po else '') + ('\\[×%d' % bo if bo else '')
    print(f'  {p}: {kind}')
    print(f'    样本: {s!r}')
