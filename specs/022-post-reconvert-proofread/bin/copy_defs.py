# -*- coding: utf-8 -*-
r"""022 defs 缺件补齐：把 yw 有而 zh 缺的 [^key]: 照录 def 行按 yw 序插入 zh 文献区。

用法:
  python -I specs/022/bin/copy_defs.py <slug>... [--apply]

语义与防线:
  - 只插缺键，不动 zh 既有 defs（中国文献译条、已照录条目原样保留）。
  - 插入位＝yw defs 序中前一个「zh 已有」键之后（保持文献区与 yw 同序）。
  - 前身为条目式列表（零 defs）的整节改形属大改形，另行处置，本工具跳过并登记。
  - 幂等：键已在 zh 则跳过。
  - 2026-11-14 重写（原稿被并行 clean 扫走）。
"""
import io
import json
import os
import re
import sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))
DEF = re.compile(r'^\[\^([^\]\s]+)\]:(.*)$', re.M)


def read(p):
    with io.open(p, encoding='utf-8', newline='') as f:
        return f.read()


def write(p, t):
    with io.open(p, 'w', encoding='utf-8', newline='') as f:
        f.write(t)


def yw_def_blocks(yw):
    """yw 的 def 行（含续行）块列表 [(key, block_text)]，按文档序。"""
    lines = yw.split('\n')
    blocks, cur_key, cur = [], None, []
    for ln in lines:
        m = re.match(r'^\[\^([^\]\s]+)\]:(.*)$', ln)
        if m:
            if cur_key:
                blocks.append((cur_key, '\n'.join(cur)))
            cur_key, cur = m.group(1), [ln]
        elif cur_key is not None:
            if ln.startswith((' ', '\t')) or (ln.strip() and not re.match(r'^(#|\[\^|[*+\-] |\$|>)', ln)):
                cur.append(ln)          # 续行
            else:
                blocks.append((cur_key, '\n'.join(cur)))
                cur_key, cur = None, []
    if cur_key:
        blocks.append((cur_key, '\n'.join(cur)))
    return blocks


def letter_of(slug):
    for d in os.listdir(ROOT):
        if len(d) == 1 and d.isalpha() and os.path.exists(os.path.join(ROOT, d, slug + '.md')):
            return d
    return None


def plan(slug, apply=False):
    letter = letter_of(slug)
    if not letter:
        return None
    zh_p = os.path.join(ROOT, letter, slug + '.md')
    yw_p = os.path.join(ROOT, 'yuanwen', letter, slug + '.md')
    zh, yw = read(zh_p), read(yw_p)
    zh_keys = set(k for k, _ in DEF.findall(zh))
    yw_blocks = yw_def_blocks(yw)
    yw_order = [k for k, _ in yw_blocks]
    missing = [k for k in yw_order if k not in zh_keys]
    if not missing:
        return {'slug': slug, 'missing': 0}
    zh_def_seq = [k for k, _ in DEF.findall(zh)]
    block_map = dict(yw_blocks)
    zh_set = set(zh_def_seq)
    if not zh_def_seq:
        return {'slug': slug, 'missing': len(missing),
                'skip': 'zh-no-defs(大改形另案)', 'missing_keys': missing[:20]}
    ins = []
    for k in missing:
        idx = yw_order.index(k)
        prev_present = next((yw_order[j] for j in range(idx - 1, -1, -1)
                             if yw_order[j] in zh_set), None)
        if prev_present is not None:
            ins.append(('after:' + prev_present, k))
            continue
        nxt = next((yw_order[j] for j in range(idx + 1, len(yw_order))
                    if yw_order[j] in zh_set), None)
        if nxt is not None:
            ins.append(('before:' + nxt, k))
        else:
            ins.append((None, k))       # zh 无任何参照键：尾插
    if not apply:
        return {'slug': slug, 'missing': len(missing), 'n_plan': len(ins),
                'plan': ins[:10]}
    after_map, before_map, tail = {}, {}, []
    for ref, k in ins:
        if ref is None:
            tail.append(k)
        elif ref.startswith('after:'):
            after_map.setdefault(ref[6:], []).append(k)
        else:
            before_map.setdefault(ref[7:], []).append(k)
    lines = zh.split('\n')
    out = []
    for ln in lines:
        m = re.match(r'^\[\^([^\]\s]+)\]:', ln)
        if m and m.group(1) in after_map:
            out.append(ln)
            for k in after_map[m.group(1)]:
                out.append(block_map[k])
            continue
        if m and m.group(1) in before_map:
            for k in before_map[m.group(1)]:
                out.append(block_map[k])
            out.append(ln)
            continue
        out.append(ln)
    if tail:
        idxs = [i for i, ln in enumerate(out) if re.match(r'^\[\^[^\]\s]+\]:', ln)]
        if idxs:
            last = idxs[-1]
            out = out[:last + 1] + [block_map[k] for k in tail] + out[last + 1:]
        else:
            out.extend(block_map[k] for k in tail)
    write(zh_p, '\n'.join(out))
    return {'slug': slug, 'missing': len(missing), 'applied': len(missing)}


def main(argv):
    apply = '--apply' in argv
    slugs = [a for a in argv if not a.startswith('--')]
    res = []
    for s in slugs:
        r = plan(s, apply=apply)
        if r:
            res.append(r)
            print('%-30s missing=%-3d %s' % (s, r['missing'],
                  r.get('skip') or ('applied=%d' % r.get('applied', 0) if apply
                                    else 'plan=%d %s' % (r.get('n_plan', 0), r.get('plan', [])[:3]))))
    with io.open(os.path.join(ROOT, 'specs', '022-post-reconvert-proofread', 'results',
                              'copydefs-log.jsonl'), 'a', encoding='utf-8') as f:
        for r in res:
            f.write(json.dumps(r, ensure_ascii=False) + '\n')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
