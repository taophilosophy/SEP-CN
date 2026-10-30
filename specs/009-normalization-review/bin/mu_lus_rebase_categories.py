# -*- coding: utf-8 -*-
"""mu-lu-s.md 分类模式 rebase 生成器（one-shot；重跑 fail-closed）。

基线还原：以 68be4fac^（抹头前最后一版，23 H1 + 102 H2）为分类骨架，
将现行 mu-lu-s.md（1874 条目、现行链接与标题、手编分类序）逐行注入骨架；
现行行 byte-identical 保留，仅插入头部行与必要空行。
门禁：slug 全量对账 + 行不变 + 表头计数 + 残余归零前置门。
用法：python mu_lus_rebase_categories.py [--write]
"""
import io, re, difflib, sys, subprocess

DRY = '--write' not in sys.argv

OLD = subprocess.run(['git', 'show', '68be4fac^:mu-lu-s.md'], capture_output=True,
                     check=True).stdout.decode('utf-8')
CUR = io.open('mu-lu-s.md', encoding='utf-8').read()

E_RE = re.compile(r'^(\s*)\* \[.*?\]\(((?:[a-z]|qian-yan|guan-yu)/[a-z0-9][a-z0-9\-]*\.md)\)\s*$')

def parse(text):
    toks = []
    for ln in text.split('\n'):
        if ln.startswith('# '):
            toks.append(('H1', ln[2:].strip(), ln))
        elif ln.startswith('## '):
            toks.append(('H2', ln[3:].strip(), ln))
        else:
            m = E_RE.match(ln)
            if m:
                toks.append(('E', m.group(2).split('/', 1)[1][:-3], ln))
    return toks

ot = parse(OLD)
cur_lines = CUR.split('\n')
old_e = [(i, t[1]) for i, t in enumerate(ot) if t[0] == 'E']
cur_e = [(i, E_RE.match(ln).group(2).split('/', 1)[1][:-3]) for i, ln in enumerate(cur_lines) if E_RE.match(ln)]

# --- 门 1：现行行身份对账 ---
assert len(cur_e) == 1883, 'cur entry rows = %d' % len(cur_e)
assert len(set(t[1] for t in cur_e)) == 1883, 'cur slugs not unique'
old_slugs = [t[1] for t in old_e]
cur_slugs = [t[1] for t in cur_e]

# --- 门 2：LCS 保序对齐（slug 精确匹配） ---
sm = difflib.SequenceMatcher(None, old_slugs, cur_slugs, autojunk=False)
blocks = [b for b in sm.get_matching_blocks() if b.size > 0]
o2c = {}
for b in blocks:
    for k in range(b.size):
        o2c[old_e[b.a + k][0]] = cur_e[b.b + k][0]
lcs = sum(b.size for b in blocks)
print('align: old %d rows, cur %d rows, exact-pair %d, LCS %d' % (len(old_e), len(cur_e), len(o2c), lcs))

# --- 门 3：表头落位（节首成批落位；空节停靠下一有锚节边界） ---
# old token 序走查：表头入 pending，遇已对齐 old 行则成批落位到其现行行号
placed = []   # (level, text, anchor_line_idx)
pending = []
for oi, tok in enumerate(ot):
    if tok[0] in ('H1', 'H2'):
        pending.append((tok[0], tok[1]))
    else:
        ci = o2c.get(oi)
        if ci is not None and pending:
            for lv, tx in pending:
                placed.append([lv, tx, ci])
            pending = []
for lv, tx in pending:
    placed.append([lv, tx, None])   # 空节：无任何对齐行
anchored = [p for p in placed if p[2] is not None]
unanchored = [p for p in placed if p[2] is None]
# 空节表头停靠：下一个有锚表头的锚行（保持 old 相对顺序），否则文件尾
last_ci = max((p[2] for p in anchored), default=len(cur_lines) - 1)
for p in reversed(unanchored):   # reversed：后面的空节先拿到后续锚；无后续则尾部
    nxt = next((q[2] for q in placed if q[0] is not None and placed.index(q) > placed.index(p) and q[2] is not None), None)
    p[2] = nxt if nxt is not None else last_ci
assert len(placed) == 125, 'headers = %d' % len(placed)
h1n = sum(1 for p in placed if p[0] == 'H1')
h2n = sum(1 for p in placed if p[0] == 'H2')
assert (h1n, h2n) == (23, 102), 'header counts (%d,%d)' % (h1n, h2n)

# --- 组装：现行行 byte-identical；表头按锚点行前插入（old 相对顺序），前后补空行 ---
ins_at = {}
for p in placed:
    ins_at.setdefault(p[2], []).append(p)

out = []
out.append('---')
out.append('outline: [1, 6]')
out.append('---')
out.append('')
out.append('<!-- markdownlint-disable MD025 -->')
out.append('')
for idx, ln in enumerate(cur_lines):
    for p in ins_at.get(idx, []):
        if out and out[-1].strip() != '':
            out.append('')
        out.append('# ' + p[1] if p[0] == 'H1' else '## ' + p[1])
        out.append('')
    if ln.strip() == '# 分类目录':
        continue  # 旧模式以 # 前言 起头；抹头期补的单标题行移除
    out.append(ln)

result = '\n'.join(out)

# --- 门 4：残余归零前置门 ---
cur_rows = [ln for ln in cur_lines if E_RE.match(ln)]
out_rows = [ln for ln in result.split('\n') if E_RE.match(ln)]
assert cur_rows == out_rows, 'entry lines altered!'
assert len(out_rows) == 1883, 'out rows = %d' % len(out_rows)
h1 = sum(1 for ln in result.split('\n') if ln.startswith('# '))
h2 = sum(1 for ln in result.split('\n') if ln.startswith('## '))
assert (h1, h2) == (23, 102), 'final header counts (%d,%d)' % (h1, h2)
for s in set(cur_slugs):
    key = '](%s/%s.md)' % (s[0], s)
    assert result.count(key) == CUR.count(key), 'link count drift: %s' % s
diff_added = sum(1 for ln in result.split('\n') if ln not in set(cur_lines))
print('gates: rows byte-identical %d | headers H1=%d H2=%d | added lines %d' % (len(out_rows), h1, h2, diff_added))
print('unanchored headers parked: %d' % len(unanchored))
for p in unanchored:
    print('  park:', p[0], p[1])

if DRY:
    print('DRY RUN — no write. Rerun with --write to apply.')
    sys.exit(0)

io.open('mu-lu-s.md', 'w', encoding='utf-8', newline='\n').write(result)
print('WROTE mu-lu-s.md')
