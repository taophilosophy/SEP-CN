# -*- coding: utf-8 -*-
"""Assemble tasks/h/hare.ledger.yaml from _hare_seg_NN.py part files."""
import io, sys, importlib.util, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ORDER = [3,4,5, 7,8,9,10,11,12,13,14,15,16,17,18,19, 21,22,23,24,
         26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,
         47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,
         68,69,70,71,72,73,74,75,76, 78,79,80,81,82, 84,85,
         87,88,89,90,91,92,93,94, 96,97,98,99,100,101,102,103,104,105,
         107,108,109,110,111,112,113,114,115,116,117,118,119,120, 132]

def load_part(path):
    spec = importlib.util.spec_from_file_location(os.path.basename(path)[:-3], path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m.SEGS

def collect(limit=None):
    segs = {}
    parts = sorted([f for f in os.listdir('.') if f.startswith('_hare_seg_') and f.endswith('.py')])
    for p in parts:
        segs.update(load_part(p))
    return segs

def emit(key, scalar, indent):
    pad = ' ' * indent
    lines = scalar.split('\n')
    out = [pad + key + ': |-']
    for ln in lines:
        out.append(pad + '  ' + ln if ln.strip() else pad)
    return '\n'.join(out)

def build(segs, only_ids=None):
    ids = [b for b in ORDER if str(b) in segs]
    if only_ids:
        ids = [b for b in ids if b in only_ids]
    chunks = ['version: 1', 'slug: hare', 'segments:']
    for n, b in enumerate(ids, 1):
        src, s1, s2 = segs[str(b)]
        chunks.append('  - id: %d' % n)
        chunks.append(emit('source', src, 4))
        chunks.append(emit('step1', s1, 4))
        chunks.append(emit('step2', s2, 4))
    return '\n'.join(chunks) + '\n'

if __name__ == '__main__':
    segs = collect()
    # default: all blocks present
    txt = build(segs)
    open('tasks/h/hare.ledger.yaml', 'w', encoding='utf-8').write(txt)
    print('ledger written: %d segments' % len([b for b in ORDER if str(b) in segs]))
