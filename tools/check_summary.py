import os, re, sys, io, json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

entries = []  # (title, path, raw_line)
with open(os.path.join(root, 'SUMMARY.md'), encoding='utf-8') as f:
    for i, line in enumerate(f, 1):
        s = line.rstrip('\n')
        m = re.match(r'^\s*\*\s+(.*)$', s)
        if not m:
            continue
        content = m.group(1)
        # replicate sync-headers.yml sed extraction
        mt = re.search(r'\[([^]]*)\]', content)
        mp = re.search(r'\]\(([^)]*)\)', content)
        if not mt or not mp:
            print('UNPARSED LINE %d: %s' % (i, s))
            continue
        entries.append((mt.group(1), mp.group(1), s))

print('total entries: %d' % len(entries))

top_dirs = {}
for t, p, _ in entries:
    d = p.split('/')[0]
    top_dirs[d] = top_dirs.get(d, 0) + 1
print('paths by top dir:', json.dumps(top_dirs, ensure_ascii=False))

# indent levels
lv = {}
for t, p, s in entries:
    ind = len(s) - len(s.lstrip())
    lv[ind] = lv.get(ind, 0) + 1
print('indent levels:', lv)

missing = [(t, p) for t, p, _ in entries if not os.path.isfile(os.path.join(root, p))]
print('missing files: %d' % len(missing))
for t, p in missing[:30]:
    print('  MISSING: %s -> %s' % (t, p))

# orphan md files (on disk, not referenced by SUMMARY.md)
ref = set(p for _, p, _ in entries)
orphans = []
for dirpath, dirnames, filenames in os.walk(root):
    dirnames[:] = [d for d in dirnames if d not in ('.git', '.gitbook', 'node_modules', 'script')]
    for fn in filenames:
        if fn.endswith('.md'):
            full = os.path.join(dirpath, fn)
            rel = os.path.relpath(full, root)
            rel = rel.replace(os.sep, '/')
            if rel not in ref:
                orphans.append(rel)
print('orphan md files: %d' % len(orphans))
for o in sorted(orphans)[:40]:
    print('  ORPHAN: %s' % o)

# filename violations: whitespace, CJK, colon, other windows-illegal chars
bad = []
for _, p, _ in entries:
    name = p.split('/')[-1]
    if re.search(r'[\s:]|[\u4e00-\u9fff]|[<>|?*"]', name):
        bad.append(p)
print('filename violations: %d' % len(bad))
for b in bad[:20]:
    print('  BADNAME: %s' % b)

# duplicate paths
from collections import Counter
c = Counter(p for _, p, _ in entries)
dups = [(p, n) for p, n in c.items() if n > 1]
print('duplicate path entries: %d' % len(dups))
for p, n in dups[:20]:
    print('  DUP: %s x%d' % (p, n))

# frontmatter / near-empty stats (H1 mismatch is expected; rewrite will normalize)
fm = []
near_empty = 0
for t, p, _ in entries:
    full = os.path.join(root, p)
    if not os.path.isfile(full):
        continue
    with open(full, encoding='utf-8-sig') as f:
        lines = f.read().split('\n')
    if lines and lines[0].strip() == '---':
        fm.append(p)
    if len([l for l in lines if l.strip()]) <= 1:
        near_empty += 1
print('files with frontmatter: %d' % len(fm))
for p in fm[:10]:
    print('  FM: %s' % p)
print('files with <=1 nonempty lines: %d' % near_empty)
