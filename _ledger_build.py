# -*- coding: utf-8 -*-
"""从 translations dict 生成 ledger YAML（block scalar 手工写出，不依赖 pyyaml）。"""
import json, io, sys

def esc_block(text):
    lines = text.rstrip('\n').split('\n')
    return '|-\n' + '\n'.join('      ' + (ln if ln else '') for ln in lines)

def get_segments():
    """返回 [(seg_id, source_text)]；块 0+1（标题+版本+作者）合并为段 1。"""
    text = open('yuanwen/e/epistemology-language-tibetan.md', encoding='utf-8').read()
    blocks = [b.strip() for b in text.split('\n\n')]
    # 合并块0(H1+版本) 与 块1(作者)
    merged = [blocks[0] + '\n' + blocks[1]] + blocks[2:117]
    segs = []
    n = 0
    for b in merged:
        if not b:
            continue
        n += 1
        segs.append((n, b))
    return segs

def build(translations):
    out = []
    out.append('version: 1')
    out.append('slug: epistemology-language-tibetan')
    out.append('segments:')
    for sid, src in get_segments():
        t = translations.get(str(sid), {})
        out.append('  - id: %d' % sid)
        out.append('    source: ' + esc_block(src))
        out.append('    step1: ' + esc_block(t.get('step1', '')))
        out.append('    step2: ' + esc_block(t.get('step2', '')))
    return '\n'.join(out) + '\n'

if __name__ == '__main__':
    tf = sys.argv[1]
    trans = json.load(open(tf, encoding='utf-8'))
    out = build(trans)
    open('tasks/e/epistemology-language-tibetan.ledger.yaml', 'w', encoding='utf-8').write(out)
    segs = get_segments()
    filled = sum(1 for k, v in trans.items() if v.get('step1') and v.get('step2'))
    print('segments total: %d, filled: %d' % (len(segs), filled))
