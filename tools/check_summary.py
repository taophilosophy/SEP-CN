import os, re, sys, io, json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 2026-11-07 裁定（ADR-0024）：H1 与 SUMMARY 条目文字必须一致；CI 只校验不写回，
# 本地用 --sync-headers 同步。默认全量结构审计；--headers 只查标题一致性（CI 用）。
ARGS = set(sys.argv[1:])
HEADERS_ONLY = '--headers' in ARGS
SYNC = '--sync-headers' in ARGS

entries = []  # (title, path, raw_line)
unparsed = 0
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
            unparsed += 1
            continue
        entries.append((mt.group(1), mp.group(1), s))


def unescape_title(t):
    return re.sub(r'\\([\[\]*])', r'\1', t).strip()


def is_alias(t):
    return '— see' in t or '——见' in t or t.lstrip().startswith('*')


def header_lines():
    """SUMMARY 正式条目行 → (title, path)。

    标题用贪婪捕获到最后一个 `](`，兼容标题里的转义方括号 `\\[Abailard\\]`；
    上面结构审计用的 `\\[([^]]*)\\]` 会在第一个 `]` 处截断，**不得**用于 H1 同步
    （2026-11-07 实例：误用后 31 个 H1 被截断，已回退）。
    """
    out = []
    with open(os.path.join(root, 'SUMMARY.md'), encoding='utf-8') as f:
        for line in f:
            m = re.match(r'^\s*\* \[(.*)\]\(([^)]*)\)\s*$', line.rstrip('\n'))
            if not m:
                continue
            out.append((m.group(1), m.group(2)))
    return out


def load_baseline_titles():
    """slug → SEP 完整标题（baseline/entries.json，入库件；缺失时返回空表并跳过别名门）。"""
    path = os.path.join(root, 'baseline', 'entries.json')
    if not os.path.isfile(path):
        return {}
    with open(path, encoding='utf-8') as f:
        d = json.load(f)
    ents = d['entries'] if isinstance(d, dict) and 'entries' in d else d
    if isinstance(ents, dict):
        ents = list(ents.values())
    return {e['slug']: (e.get('title') or '') for e in ents}


CJK = re.compile(r'[\u4e00-\u9fff\u3000-\u303f\uff00-\uffef]')
SLUGPATH = re.compile(r'[a-z0-9]/[A-Za-z0-9][A-Za-z0-9.\-]*\.md')
FUNC_START = re.compile(r'^(and|of|in|on|to|for|with|is|are)\b', re.I)
FUNC_END = re.compile(r'\b(and|or|of|in|on|to|for|with)$', re.I)


def norm_title(s):
    return re.sub(r'[^a-z0-9]+', ' ', s).strip().lower()


def alias_fragments():
    """别名行左侧英文片段为半截/悬空的清单（2026-11-07 裁定：必须是完整标题）。

    口径：取最后一个汉字之后的英文片段；与目标 baseline 完整标题或右侧索引名等价即放行，
    否则以功能词开头/结尾（and/of/in/on/to/for/with/is/are）即判残缺。
    """
    titles = load_baseline_titles()
    if not titles:
        return []
    rows = []
    for t, p in header_lines():
        if ' — see' not in t or not SLUGPATH.fullmatch(p):
            continue
        left, right = t.split(' — see', 1)
        idx = max((k for k, ch in enumerate(left) if CJK.match(ch)), default=-1)
        frag = left[idx + 1:].strip().replace('\\*', '').strip()
        slug = os.path.basename(p)[:-3]
        full = titles.get(slug) or ''
        if not full:
            continue
        nf, nt, nr = norm_title(frag), norm_title(full), norm_title(right)
        if not frag:
            rows.append((p, frag, full))
        elif nf == nt or nf == nr:
            continue
        elif FUNC_START.match(frag) or FUNC_END.search(frag):
            rows.append((p, frag, full))
    return rows


def header_mismatches():
    """SUMMARY 正式条目文字（还原转义后）与文件 H1 不一致的清单。

    跳过别名行（共用目标路径）、`*` 占位母词条、README（多行共指）、frontmatter 文件，
    口径与改写前的 sync-headers.yml 一致（ADR-0007/0009/0024）。
    """
    rows = []
    for t, p in header_lines():
        if p == 'README.md' or is_alias(t):
            continue
        full = os.path.join(root, p)
        if not os.path.isfile(full):
            continue
        with open(full, encoding='utf-8-sig') as f:
            first = f.read().split('\n')[0]
        if first.strip() == '---':
            continue
        want = unescape_title(t)
        have = re.sub(r'^#*\s*', '', first).strip()
        if not want:
            raise SystemExit('SUMMARY 条目文字为空，拒绝比对：%s' % p)
        if want != have:
            rows.append((p, want, have))
    return rows


def rewrite_h1(path, want):
    full = os.path.join(root, path)
    with open(full, 'rb') as f:
        raw = f.read()
    bom = raw.startswith(b'\xef\xbb\xbf')
    text = raw.decode('utf-8-sig')
    nl = '\r\n' if '\r\n' in text else '\n'
    parts = text.split(nl)
    parts[0] = '# ' + want
    out = (b'\xef\xbb\xbf' if bom else b'') + nl.join(parts).encode('utf-8')
    with open(full, 'wb') as f:
        f.write(out)


mismatch = header_mismatches()
if SYNC:
    for p, want, have in mismatch:
        print('SYNC %s: %r -> %r' % (p, have, want))
        rewrite_h1(p, want)
    # 写回后置门：残差必须归零（rules/05「生成器与批量改写脚本」）
    resid = header_mismatches()
    print('H1 同步 %d 处，残差 %d' % (len(mismatch), len(resid)))
    for p, want, have in resid:
        print('  RESIDUAL %s\n    SUMMARY: %s\n    H1     : %s' % (p, want, have))
    sys.exit(1 if resid else 0)

print('total entries: %d' % len(entries))

if HEADERS_ONLY:
    print('H1 mismatch: %d' % len(mismatch))
    for p, want, have in mismatch:
        print('  MISMATCH %s\n    SUMMARY: %s\n    H1     : %s' % (p, want, have))
    sys.exit(1 if mismatch else 0)

alias_bad = alias_fragments()

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
    dirnames[:] = [d for d in dirnames if d not in ('.git', '.gitbook', 'node_modules', 'script', 'yuanwen', 'en')]
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

# duplicate paths（ADR-0007：别名行链目标词条路径、导航节点链 README 属预期共享，不计入硬错误）
from collections import Counter
c = Counter(p for t, p, _ in entries
            if '— see' not in t and '——见' not in t and p != 'README.md')
dups = [(p, n) for p, n in c.items() if n > 1]
print('duplicate path entries: %d' % len(dups))
for p, n in dups[:20]:
    print('  DUP: %s x%d' % (p, n))

# frontmatter / near-empty stats
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

print('H1 mismatch: %d' % len(mismatch))
for p, want, have in mismatch:
    print('  MISMATCH %s\n    SUMMARY: %s\n    H1     : %s' % (p, want, have))

print('alias fragment (需完整标题): %d' % len(alias_bad))
for p, frag, full in alias_bad[:30]:
    print('  ALIAS %s: %r，应为 %r' % (p, frag, full))

# 门禁：硬错误非零退出（孤儿文件/近空文件为统计信息，不计入；H1 不一致与别名残缺为硬错误，ADR-0024）
hard = unparsed + len(missing) + len(bad) + len(dups) + len(mismatch) + len(alias_bad)
print('HARD ERRORS: %d' % hard)
sys.exit(1 if hard else 0)
