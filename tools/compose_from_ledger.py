#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Compose h/<slug>.md from tasks/h/<slug>.ledger.yaml (step2 join) + tail sections from yuanwen.

Usage: python tools/compose_from_ledger.py <slug> [--write]

Reads ledger segments in id order, joins step2 with blank lines into the body.
Prepends H1 (from SUMMARY.md entry line) + version line (from baseline/entries.json pubinfo).
Then copies the tail sections from yuanwen/h/<slug>.md that come AFTER the last ledger
segment's source (footnotes, references, tools, other resources, related entries, acknowledgments),
translating Chinese-literature references per ADR-0011 (best-effort: leaves them, flagged for human).

--write: write to h/<slug>.md. Without --write: print to stdout (dry run).
"""
import json, re, sys, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

def load_json(p):
    with open(p, encoding='utf-8') as f:
        return json.load(f)

def ledger_segments(slug):
    p = f'tasks/h/{slug}.ledger.yaml'
    if not os.path.exists(p):
        return None
    txt = open(p, encoding='utf-8').read()
    m = re.search(r'segments:\n(.*)$', txt, re.S)
    if not m:
        return None
    segs = []
    # split on every '- id: N' including the first
    body = m.group(1)
    for blk in re.split(r'(?m)^  - id: ', body):
        if not blk.strip():
            continue
        sid = re.match(r'(\d+)', blk)
        s2 = re.search(r'step2: \|-\n(.*?)(?=\n  - id:|\Z)', blk, re.S)
        if not sid or not s2:
            continue
        segs.append({'id': int(sid.group(1)), 'step2': s2.group(1).rstrip('\n')})
    segs.sort(key=lambda s: s['id'])
    return segs

def dedent_block(txt):
    """Strip the common leading whitespace from a YAML block-scalar content."""
    lines = txt.split('\n')
    # find min indent of non-empty lines
    inds = [len(l) - len(l.lstrip(' ')) for l in lines if l.strip()]
    if not inds:
        return txt
    mi = min(inds)
    return '\n'.join(l[mi:] if len(l) >= mi else l for l in lines)

def h1_from_summary(slug):
    txt = open('SUMMARY.md', encoding='utf-8').read()
    for line in txt.splitlines():
        if f'](h/{slug}.md)' in line:
            s = line.strip()
            # strip leading * and [ and trailing ](...)
            s = re.sub(r'^\*\s*\[', '', s)
            s = re.sub(r'\]\(.*\)$', '', s).strip()
            return s
    return None

def version_line(slug):
    try:
        e = load_json('baseline/entries.json')
    except Exception:
        return None
    ent = None
    if isinstance(e, dict) and 'entries' in e:
        ents = e['entries']
        if isinstance(ents, dict):
            ent = ents.get(slug)
        elif isinstance(ents, list):
            ent = next((x for x in ents if isinstance(x, dict) and x.get('slug') == slug), None)
    elif isinstance(e, list):
        ent = next((x for x in e if isinstance(x, dict) and x.get('slug') == slug), None)
    if not ent:
        return None
    pub = ent.get('pubinfo', {}).get('first_published')
    rev = ent.get('pubinfo', {}).get('substantive_revision') or ent.get('pubinfo', {}).get('revised_date')
    if pub:
        m = re.match(r'([A-Za-z]+)\s+(\d{1,2}),\s*(\d{4})', str(pub))
        if m:
            mo = {'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}.get(m.group(1))
            y, d = m.group(3), m.group(2)
            first = f'*首次发表于 {y} 年 {mo} 月 {int(d)} 日'
            if rev:
                m2 = re.match(r'([A-Za-z]+)\s+(\d{1,2}),\s*(\d{4})', str(rev))
                if m2:
                    mo2 = {'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}.get(m2.group(1))
                    y2, d2 = m2.group(3), m2.group(2)
                    return f'{first}；{y2} 年 {mo2} 月 {int(d2)} 日实质修订。*'
            return first + '。*'
        m = re.match(r'(\d{4})[-/](\d{1,2})[-/](\d{1,2})', str(pub))
        if m:
            y, mo, d = m.groups()
            first = f'*首次发表于 {y} 年 {int(mo)} 月 {int(d)} 日'
            if rev:
                m2 = re.match(r'(\d{4})[-/](\d{1,2})[-/](\d{1,2})', str(rev))
                if m2:
                    y2, mo2, d2 = m2.groups()
                    return f'{first}；{y2} 年 {int(mo2)} 月 {int(d2)} 日实质修订。*'
            return first + '。*'
    return None

def source_blocks(slug):
    txt = open(f'yuanwen/h/{slug}.md', encoding='utf-8').read()
    return [b for b in re.split(r'\n\s*\n', txt) if b.strip()]

def tail_after_last(slug, last_src):
    blocks = source_blocks(slug)
    # find index of block containing first 60 chars of last ledger source
    key = last_src.replace('\n', ' ')[:60]
    for i, b in enumerate(blocks):
        if key in b.replace('\n', ' '):
            return '\n\n'.join(blocks[i+1:])
    return None

def main():
    slug = sys.argv[1]
    write = '--write' in sys.argv
    segs = ledger_segments(slug)
    if segs is None:
        print('NO LEDGER', slug); return 1
    body = '\n\n'.join(dedent_block(s['step2']) for s in segs)
    h1 = h1_from_summary(slug)
    vl = version_line(slug)
    parts = []
    if h1: parts.append(f'# {h1}')
    if vl: parts.append(vl)
    parts.append(body)
    doc = '\n\n'.join(p for p in parts if p)
    if write:
        with open(f'h/{slug}.md', 'w', encoding='utf-8') as f:
            f.write(doc + '\n')
        print(f'WROTE h/{slug}.md ({len(doc)} bytes, {len(segs)} segs)')
    else:
        print(doc)
    return 0

if __name__ == '__main__':
    sys.exit(main())
