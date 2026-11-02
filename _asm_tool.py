# -*- coding: utf-8 -*-
"""Assemble ledger parse + source block match -> _asm_<slug>.json (dedent-aware)."""
import re, sys, json

def norm(s):
    s = re.sub(r'\[\^[^\]]+\]', '', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s

def parse_ledger(ltxt):
    """Line-based parse of segments: id / source / step2."""
    segs = []
    cur = None  # dict with id, source lines, in_step2 flag
    mode = None
    for ln in ltxt.split('\n'):
        m = re.match(r'^  - id: (\S+)', ln)
        if m:
            if cur: segs.append(cur)
            cur = {'id': m.group(1), 'source': [], 'step2': []}
            mode = None
            continue
        if cur is None: continue
        if re.match(r'^    source: \|', ln):
            mode = 'source'; continue
        if re.match(r'^    step1: \|', ln):
            mode = 'step1'; continue
        if re.match(r'^    step2: \|', ln):
            mode = 'step2'; continue
        if re.match(r'^    \w+:', ln):
            mode = None; continue
        if re.match(r'^  - id:', ln):
            if cur: segs.append(cur)
            cur = None; mode = None
            continue
        if mode in ('source', 'step2'):
            cur[mode].append(ln)
    if cur: segs.append(cur)
    out = []
    for s in segs:
        out.append((s['id'], '\n'.join(s['source']).strip(), '\n'.join(s['step2']).strip()))
    return out

def parse_source(src):
    lines = src.split('\n')
    blocks = []
    tail_i = None
    for i, ln in enumerate(lines):
        if i == 0:
            blocks.append(('h1', ln)); continue
        if ln.startswith('**First published') or ln.startswith('**First'):
            blocks.append(('date', ln)); continue
        if ln.startswith('*') and not ln.startswith('**') and ln.rstrip().endswith('*'):
            blocks.append(('author', ln)); continue
        if ln.startswith('## ') and 'References' in ln:
            tail_i = i
            break
        if re.match(r'^#{2,4} ', ln):
            blocks.append(('header', ln)); continue
        if ln.strip():
            blocks.append(('para', ln))
    if tail_i is not None:
        tail = '\n'.join(lines[tail_i:]).strip()
        blocks.append(('tail', tail))
    return blocks

def main(slug):
    src = open(f'yuanwen/c/{slug}.md', encoding='utf-8').read()
    ltxt = open(f'tasks/c/{slug}.ledger.yaml', encoding='utf-8').read()
    segs = parse_ledger(ltxt)
    lookup = {}
    for sid, s, st2 in segs:
        if s.strip() and st2.strip():
            lookup[norm(s)] = st2
    blocks = parse_source(src)
    out = []
    missing = []
    for typ, txt in blocks:
        if typ == 'para':
            n = norm(txt)
            if n in lookup:
                out.append(('para', lookup[n])); continue
            hit = None
            for k, v in lookup.items():
                if n[:60] and (k[:60] == n[:60] or n[:60] in k or k[:60] in n):
                    hit = v; break
            if hit:
                out.append(('para', hit))
            else:
                missing.append(txt[:70])
                out.append(('para', '<<<MISSING>>>' + txt))
        else:
            out.append((typ, txt))
    print(f'{slug}: src_blocks {len(blocks)}, ledger_segs {len(segs)}, missing {len(missing)}')
    for m in missing[:8]:
        print('  MISS:', m)
    json.dump(out, open(f'_asm_{slug}.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

for s in sys.argv[1:]:
    main(s)
