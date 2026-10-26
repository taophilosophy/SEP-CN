import os, re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def unescape(t):
    out = []
    i = 0
    while i < len(t):
        if t[i] == '\\' and i + 1 < len(t) and t[i + 1] in '*[]':
            out.append(t[i + 1])
            i += 2
        else:
            out.append(t[i])
            i += 1
    return ''.join(out)

def is_fake(title):
    # 递归引用的假条目：— see 前后的英文部分相同（如 recursion — see recursion）
    m = re.search(r'\s+—\s*see\s+(.*)$', title)
    if not m:
        return False
    left = title[:m.start()].strip()
    right = m.group(1).strip()
    return left == right

# SUMMARY.md 条目
summary = {}  # path -> title(已解转义)
with open(os.path.join(root, 'SUMMARY.md'), encoding='utf-8') as f:
    for line in f:
        m = re.match(r'^\s*\* \[(.*)\]\(([^)]*)\)\s*$', line.rstrip('\n'))
        if m:
            summary[m.group(2)] = unescape(m.group(1))

# mu-lu-s.md 链接
mulu = {}  # path -> list of titles
broken = []  # 文件不存在的链接
with open(os.path.join(root, 'mu-lu-s.md'), encoding='utf-8') as f:
    for i, line in enumerate(f, 1):
        for m in re.finditer(r'\[((?:\\.|[^\]])*)\]\(([^)]*)\)', line):
            title, path = m.group(1), m.group(2)
            if not path.endswith('.md'):
                continue
            mulu.setdefault(path, []).append(unescape(title))
            if not os.path.isfile(os.path.join(root, path)):
                broken.append((i, path))

print('SUMMARY 条目: %d | mu-lu-s 链接路径: %d' % (len(summary), len(mulu)))

# 1. mu-lu-s 链接的文件是否存在
print('\n[1] mu-lu-s 链接指向不存在的文件: %d' % len(broken))
for i, p in broken[:20]:
    print('    行 %d: %s' % (i, p))

# 2. mu-lu-s 的路径不在 SUMMARY 中（对应失败）
not_in_summary = sorted(p for p in mulu if p not in summary)
print('\n[2] mu-lu-s 路径不在 SUMMARY 中: %d' % len(not_in_summary))
for p in not_in_summary[:30]:
    print('    %s' % p)

# 3. SUMMARY 路径未出现在 mu-lu-s（覆盖缺口），按类型分组
missing = [p for p in summary if p not in mulu]
fake = sorted(p for p in missing if is_fake(summary[p]))
alias = sorted(p for p in missing if p not in set(fake) and '— see' in summary[p])
placeholder = sorted(p for p in missing
                     if p not in set(fake) | set(alias) and summary[p].lstrip().startswith('*'))
real = sorted(p for p in missing if p not in set(fake) | set(alias) | set(placeholder)
              and p != 'README.md')
print('\n[3] SUMMARY 有而 mu-lu-s 无: %d' % len(missing))
print('    其中递归引用假条目（— see 自指，预期不收录）: %d' % len(fake))
for p in fake[:20]:
    print('      %s  <-  %s' % (p, summary[p][:50]))
print('    其中一般别名词条（— see 型，预期不收录）: %d' % len(alias))
print('    其中 * 前缀占位母词条（无正文，预期不收录）: %d' % len(placeholder))
print('    其中正式条目（如非刻意应为覆盖缺口）: %d' % len(real))
for p in real:
    print('      %s  <-  %s' % (p, summary[p][:60]))

# 4. 共有路径的标题差异（解转义后比对）
diff = []
for p in sorted(set(mulu) & set(summary)):
    for t in mulu[p]:
        if t.strip() != summary[p].strip():
            diff.append((p, t, summary[p]))
print('\n[4] 共有路径标题不一致: %d' % len(diff))
for p, a, b in diff[:20]:
    print('    %s\n      mu-lu-s: %s\n      SUMMARY: %s' % (p, a[:60], b[:60]))

# 5. mu-lu-s 内重复收录同一路径
dup = sorted((p, len(ts)) for p, ts in mulu.items() if len(ts) > 1)
print('\n[5] mu-lu-s 重复收录路径: %d' % len(dup))
for p, n in dup[:20]:
    print('    %s x%d' % (p, n))
