# -*- coding: utf-8 -*-
r"""022 键改名：重转后 yw 改键，zh 的 marker+def 键随改。

取证：zh 独有键的 def 行文本 ↔ yw 独有键的 def 行文本，NFD 去音符+去标点归一后
按相似度配对，1:1 唯一匹配且出现次数一致才改。无 def 行可取文本时按键名归一匹配。

用法:
  python -I specs/022/bin/rename_keys.py <slug>... [--apply] [--queue FILE]
"""
import io
import json
import os
import re
import sys
import unicodedata
from collections import Counter

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))
MARKER = re.compile(r'\[\^([^\]\s]+)\](?!:)')
DEF = re.compile(r'^\[\^([^\]\s]+)\]:(.*)$', re.M)


def read(p):
    with io.open(p, encoding='utf-8', newline='') as f:
        return f.read()


def norm_text(s):
    s = unicodedata.normalize('NFD', s)
    s = ''.join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r'[^a-z0-9]+', '', s.lower())
    return s


def def_text(t, key):
    m = re.search(r'^\[\^' + re.escape(key) + r'\]:(.*)$', t, re.M)
    return m.group(1) if m else ''


def plan_entry(slug, letter):
    zh_p = os.path.join(ROOT, letter, slug + '.md')
    yw_p = os.path.join(ROOT, 'yuanwen', letter, slug + '.md')
    if not os.path.exists(zh_p):
        return None
    zh, yw = read(zh_p), read(yw_p)
    mk_zh = Counter(m.group(1) for m in MARKER.finditer(zh))
    mk_yw = Counter(m.group(1) for m in MARKER.finditer(yw))
    zh_only = list((mk_zh - mk_yw).elements())
    yw_only = list((mk_yw - mk_zh).elements())
    if not zh_only:
        return None
    zh_u, yw_u = sorted(set(zh_only)), sorted(set(yw_only))
    # 取证文本
    ztxt = {k: norm_text(def_text(zh, k)) for k in zh_u}
    ytxt = {k: norm_text(def_text(yw, k)) for k in yw_u}
    pairs = []
    for zk in zh_u:
        need = mk_zh[zk]
        # 文本匹配优先
        cand = [yk for yk in yw_u if ztxt[zk] and ztxt[zk] == ytxt[yk] and len(ztxt[zk]) > 8]
        if not cand:
            # 键名归一匹配
            zk_n = norm_text(zk)
            cand = [yk for yk in yw_u if norm_text(yk) == zk_n]
        if len(cand) == 1 and mk_yw[cand[0]] >= need:
            pairs.append((zk, cand[0], need))
        else:
            pairs.append((zk, None, need,
                          {'cands': cand, 'yw_cnt': {c: mk_yw[c] for c in cand}}))
    return {'slug': slug, 'letter': letter, 'pairs': pairs}


def apply_renames(pl):
    zh_p = os.path.join(ROOT, pl['letter'], pl['slug'] + '.md')
    zh = read(zh_p)
    n = 0
    for zk, yk, need in pl['pairs']:
        if yk is None:
            continue
        pat = re.compile(r'\[\^' + re.escape(zk) + r'\](?!:)|(\[\^' + re.escape(zk) + r'\]:)')
        zh, k = pat.subn(lambda m: '[^%s]' % yk if m.group(1) is None else '[^%s]:' % yk, zh)
        n += k
    write(zh_p, zh)
    return n


def main(argv):
    apply = '--apply' in argv
    slugs = [a for a in argv if not a.startswith('-')]
    if '--queue' in argv:
        qf = argv[argv.index('--queue') + 1]
        slugs = [x['slug'] for x in json.load(io.open(qf, encoding='utf-8'))]
    out_log = os.path.join(ROOT, 'specs', '022-post-reconvert-proofread', 'results',
                           'rename-log.jsonl')
    n_renamed = 0
    for slug in slugs:
        pl = plan_entry(slug, slug[0])
        if not pl:
            continue
        ok = [(a, b, c) for a, b, c, *_ in pl['pairs'] if b]
        bad = [p for p in pl['pairs'] if not p[1]]
        print('%-30s rename=%-3d manual=%d %s' % (
            slug, len(ok), len(bad),
            ('-> ' + ', '.join('%s→%s' % (a, b) for a, b, _ in ok[:5])) if ok else ''))
        if apply and ok:
            n = apply_renames(pl)
            n_renamed += n
        with io.open(out_log, 'a', encoding='utf-8') as f:
            f.write(json.dumps({'slug': slug, 'pairs': pl['pairs'], 'applied': apply},
                               ensure_ascii=False) + '\n')
    if apply:
        print('TOTAL subn=%d' % n_renamed)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
