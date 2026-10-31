# -*- coding: utf-8 -*-
"""specs/010 第四轮增量补丁：基于 HEAD（f703461d，并行会话已拆 19/20 世纪节）：
A. 同步 mu-lu-s 链接文本至 SUMMARY 契约（修复 [4] 66 处——并行会话改 SUMMARY 未同步 mu-lu-s）
B. 拆 austin-jl 下误挂嵌套块（hare…alexander-crummell 18 条，缩进减 2 平铺）
C. 特殊归位：alexander-aphrodisias→中期希腊哲学节；james-viterbo→经院哲学节；
   james-ward/james-mill/alexander-humboldt/alexander-crummell→19 世纪节（均平铺缩进重置）
对账门禁：li 总数守恒 1888=1888、slug 进=出零重复；任一不过拒绝写回。
"""
import io
import re
import sys
from collections import Counter

def unesc(t):
    out, i = [], 0
    while i < len(t):
        if t[i] == '\\' and i + 1 < len(t) and t[i + 1] in '*[]':
            out.append(t[i + 1]); i += 2
        else:
            out.append(t[i]); i += 1
    return ''.join(out)

# ---------- 读 ----------
src = io.open('mu-lu-s.md', encoding='utf-8').read()
summ = {}
for line in io.open('SUMMARY.md', encoding='utf-8'):
    m = re.match(r'^\s*\* \[(.*)\]\(([^)]*)\)\s*$', line.rstrip('\n'))
    if m:
        # ADR-0007：别名行（— see）setdefault，不覆盖正式行标题（与 check_mulu_s 同款）
        if '— see' in m.group(1) or '——见' in m.group(1):
            summ.setdefault(m.group(2), m.group(1))
        else:
            summ[m.group(2)] = m.group(1)

class Li:
    __slots__ = ('indent', 'text', 'target', 'tail')
    def __init__(self, indent, text, target, tail):
        self.indent, self.text, self.target, self.tail = indent, text, target, tail
    @property
    def slug(self):
        return self.target.split('/')[-1][:-3]
    def render(self, indent=None):
        ind = self.indent if indent is None else indent
        return '%s* [%s](%s)%s' % (ind, self.text, self.target, self.tail)

items = []
for ln in src.split('\n'):
    m = re.match(r'^(#{1,6}) (.+?)\s*$', ln)
    if m:
        items.append(('h', len(m.group(1)), m.group(2))); continue
    m = re.match(r'^( *)\* \[(.+?)\]\(([a-zA-Z0-9._/\-]+\.md)\)(.*)$', ln)
    if m:
        items.append(('li', Li(m.group(1), m.group(2), m.group(3), m.group(4)))); continue
    items.append(('raw', ln))

n_li0 = sum(1 for it in items if it[0] == 'li')

# ---------- A 同步标题契约 ----------
a = 0
for i, it in enumerate(items):
    if it[0] != 'li':
        continue
    p = it[1].target
    if p in summ and unesc(it[1].text).strip() != unesc(summ[p]).strip():
        items[i] = ('li', Li(it[1].indent, summ[p], it[1].target, it[1].tail))
        a += 1

# ---------- take ----------
def take(slugs, seq):
    got, rest, i = [], [], 0
    while i < len(seq):
        it = seq[i]
        if it[0] == 'li' and it[1].slug in slugs:
            base = len(it[1].indent); got.append(it); j = i + 1
            while j < len(seq) and seq[j][0] == 'li' and len(seq[j][1].indent) > base:
                got.append(seq[j]); j += 1
            i = j
        else:
            rest.append(it); i += 1
    return rest, got

# ---------- B 拆 austin-jl 下误挂块 ----------
out, in_ab = [], False
for it in items:
    if it[0] == 'li':
        ind = len(it[1].indent)
        if ind == 0:
            in_ab = (it[1].slug == 'austin-jl'); out.append(it)
        elif in_ab and ind >= 2:
            out.append(('li', Li(it[1].indent[2:], it[1].text, it[1].target, it[1].tail)))
        else:
            out.append(it)
    else:
        out.append(it)
items = out

# ---------- C 特殊归位 ----------
def find_h(items, level, prefix):
    return next(i for i, it in enumerate(items) if it[0] == 'h' and it[1] == level and it[2].startswith(prefix))

items, move_anc = take({'alexander-aphrodisias'}, items)
items, move_vit = take({'james-viterbo'}, items)
items, move_19 = take({'james-ward', 'james-mill', 'alexander-humboldt', 'alexander-crummell'}, items)
# 摘出块平铺缩进重置（插入新节为顶层条目）
def flatten(seq):
    first = None
    out = []
    for it in seq:
        if it[0] == 'li':
            if first is None:
                first = len(it[1].indent)
            out.append(('li', Li(it[1].indent[first:], it[1].text, it[1].target, it[1].tail)))
        else:
            out.append(it)
    return out
move_anc = flatten(move_anc)
move_vit = flatten(move_vit)
move_19 = flatten(move_19)
i_anc = find_h(items, 2, '中期希腊哲学')
i_nxt = next(i for i in range(i_anc + 1, len(items)) if items[i][0] == 'h' and items[i][1] <= 2)
items[i_nxt:i_nxt] = move_anc
i_vit = find_h(items, 2, '经院哲学')
i_nxt = next(i for i in range(i_vit + 1, len(items)) if items[i][0] == 'h' and items[i][1] <= 2)
items[i_nxt:i_nxt] = move_vit
i_19 = find_h(items, 2, '19 世纪西方哲学')
items[i_19 + 1:i_19 + 1] = move_19

# ---------- 对账 ----------
n_li1 = sum(1 for it in items if it[0] == 'li')
slugs = Counter(it[1].slug for it in items if it[0] == 'li')
assert n_li0 == n_li1 == 1888, (n_li0, n_li1)
dups = [s for s, c in slugs.items() if c > 1]
assert not dups, dups
# 人物/结构完整性：三条特殊不再嵌套
for row in items:
    if row[0] == 'li' and row[1].slug in ('alexander-aphrodisias', 'james-viterbo', 'james-ward', 'james-mill', 'alexander-humboldt', 'alexander-crummell'):
        assert row[1].indent == '', row[1].slug

# ---------- 写 ----------
out = []
for it in items:
    if it[0] == 'h':
        out.append('#' * it[1] + ' ' + it[2])
    elif it[0] == 'li':
        out.append(it[1].render())
    else:
        out.append(it[1])
text = re.sub(r'\n{3,}', '\n\n', '\n'.join(out))
io.open('mu-lu-s.md', 'w', encoding='utf-8', newline='\n').write(text + '\n')
print('A 标题同步 %d 处；B austin 误挂块拆平铺；C 特殊归位 %d+%d+%d' % (
    a, len(move_anc), len(move_vit), len(move_19)))
print('对账 PASS %d=%d，零重复' % (n_li0, n_li1))
