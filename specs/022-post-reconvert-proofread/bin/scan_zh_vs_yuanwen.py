# -*- coding: utf-8 -*-
r"""022 扫描器：zh 译文 ↔ yuanwen（b20ab51b8 重转基准）机器预检。只读，不抓取。

用法:
  python -I specs/022/bin/scan_zh_vs_yuanwen.py [--out PATH] [--limit N] [--letters a,b,c] [slug ...]
  python -I specs/022/bin/scan_zh_vs_yuanwen.py --calib slug1,slug2   # 校准模式（打印段落比率明细）

输出: specs/022/results/scan-<时间戳>.jsonl，每词条一行：
  {slug, kind, sections_zh, sections_yw, blocks: {plain, quote, table, list, formula, code, other},
   para_mismatch: [{sec, yw_i, zh_i, type_yw, type_zh}],
   untranslated: [yw 块头样例],
   ratio_flags: [{sec, i, ratio, zh_head, yw_head}],
   markers: {zh, yw, only_zh, only_yw},
   defs: {zh, yw, only_zh, only_yw},
   tail_missing: [...],
   skip: 存根/缺镜像等原因}

判读提示（真伪鉴别）:
  - para_mismatch 高发于引块两行体、byline、表尾注——type 错位≠缺陷，人工定性。
  - markers 落差＝ADR-0038「中文未挂、原文已挂」预期态，偿还时按新基准补齐。
  - defs only_zh/only_yw 差额须回源核对（K 批教训：defs 差额≠缺件，先查形态）。
"""
import io
import json
import os
import re
import sys
from collections import Counter

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))
CJK = re.compile(r'[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]')
WORD = re.compile(r"[A-Za-z][A-Za-z'\u2019\-\u02BC]*")
MARKER = re.compile(r'\[\^([^\]\s]+)\](?!:)')
DEF = re.compile(r'^\[\^([^\]\s]+)\]:', re.M)
H2 = re.compile(r'^## ', re.M)

TAIL_MISSING_CANDIDATES = ('参考文献', '学术工具', '其他网络资源', '相关词条')


def read(p):
    with io.open(p, encoding='utf-8') as f:
        return f.read()


def classify(block):
    b = block.lstrip()
    if b.startswith('>'):
        return 'quote'
    if b.startswith('|'):
        return 'table'
    if b.startswith('```'):
        return 'code'
    if b.startswith('$$') or b.startswith('\\['):
        return 'formula'
    if re.match(r'^(\d+\.|[-*+] )', b):
        return 'list'
    if b.startswith('\\begin') or b.startswith('\\('):
        return 'formula'
    return 'plain'


def blocks_of(text):
    """按空行切块；标题行单独成块标 '#'。返回 [(type, text)]。"""
    out = []
    for raw in re.split(r'\n\s*\n', text):
        raw = raw.strip()
        if not raw:
            continue
        lines = raw.split('\n')
        # 标题混进块首（### 子节标题与段落连排）：拆出标题行
        while lines and re.match(r'^#{2,6} ', lines[0]):
            out.append(('#', lines[0]))
            lines = lines[1:]
        body = '\n'.join(lines).strip()
        if body:
            out.append((classify(body), body))
    return out


def sections_of(text):
    """按 '## ' 切节。返回 [(title, [blocks])]；首节 title=''。"""
    idx = [(m.start(), m.group(0).strip()) for m in H2.finditer(text)]
    if not idx:
        return [('', text)]
    secs = []
    pre = text[:idx[0][0]]
    if pre.strip():
        secs.append(('', pre))
    for k, (st, title) in enumerate(idx):
        end = idx[k + 1][0] if k + 1 < len(idx) else len(text)
        secs.append((title[3:].strip(), text[st:end]))
    return secs


def is_stub(zh):
    return len([ln for ln in zh.split('\n') if ln.strip()]) <= 10


def norm_key(k):
    return k.replace('\u2019', "'").replace('\u02BC', "'").lower()


def scan_entry(letter, slug, calib=False):
    zh_p = os.path.join(ROOT, letter, slug + '.md')
    yw_p = os.path.join(ROOT, 'yuanwen', letter, slug + '.md')
    rec = {'slug': slug, 'letter': letter}
    if not os.path.exists(zh_p):
        rec['skip'] = 'no-zh'
        return rec
    zh = read(zh_p)
    rec['kind'] = 'supplement' if '.supplement' in slug else ('stub' if is_stub(zh) else 'entry')
    if rec['kind'] in ('stub',) or slug.endswith('.supplement') is False and False:
        pass
    if rec['kind'] == 'stub':
        return rec
    if not os.path.exists(yw_p):
        rec['skip'] = 'no-yuanwen'
        return rec
    yw = read(yw_p)

    # ---- 全文标记与 defs 键集 ----
    mk_zh = Counter(norm_key(m.group(1)) for m in MARKER.finditer(zh))
    mk_yw = Counter(norm_key(m.group(1)) for m in MARKER.finditer(yw))
    only_zh = sorted((mk_zh - mk_yw).elements())
    only_yw = sorted((mk_yw - mk_zh).elements())
    rec['markers'] = {'zh': sum(mk_zh.values()), 'yw': sum(mk_yw.values()),
                      'only_zh': only_zh[:12], 'only_yw': only_yw[:12],
                      'n_only_zh': len(only_zh), 'n_only_yw': len(only_yw)}
    d_zh = set(norm_key(k) for k in DEF.findall(zh))
    d_yw = set(norm_key(k) for k in DEF.findall(yw))
    rec['defs'] = {'zh': len(d_zh), 'yw': len(d_yw),
                   'only_zh': sorted(d_zh - d_yw)[:12], 'only_yw': sorted(d_yw - d_zh)[:12],
                   'n_only_zh': len(d_zh - d_yw), 'n_only_yw': len(d_yw - d_zh)}

    # ---- 尾节四件套 ----
    if not slug.endswith('.supplement'):
        rec['tail_missing'] = [t for t in TAIL_MISSING_CANDIDATES
                               if ('## ' + t) not in zh]
    else:
        rec['tail_missing'] = []

    # ---- 节序列与段落配对 ----
    sz, sy = sections_of(zh), sections_of(yw)
    rec['sections_zh'] = len(sz)
    rec['sections_yw'] = len(sy)
    if len(sz) != len(sy):
        rec['section_count_diff'] = {'zh': [t for t, _ in sz], 'yw': [t for t, _ in sy]}
    pairs = list(zip(sz, sy)) if not calib else list(zip(sz, sy))
    mm, untranslated, ratio_flags = [], [], []
    for si, ((zt, zb), (yt, yb)) in enumerate(pairs):
        # 脚注/Notes 与参考文献类节：只比键集（上面全文已比），段落不配对
        tl = zt or ''
        if any(k in tl for k in ('脚注', '参考文献', '学术工具', '其他网络资源', '相关词条')) \
                or any(k in (yt or '') for k in ('Notes', 'Literature', 'Academic', 'Internet', 'Related')):
            continue
        bz, by = blocks_of(zb), blocks_of(yb)
        # 首节（导言）：剥 H1 与 pubinfo（前两块），yw 的 byline 短拉丁块跳过
        if si == 0 or (zt == '' and yt == ''):
            if bz and bz[0][0] == '#':
                bz = bz[1:]
            if by and by[0][0] == '#':
                by = by[1:]
            if bz and bz[0][0] == 'plain' and '首次发表于' in bz[0][1]:
                bz = bz[1:]
            if by and by[0][0] == 'plain' and 'First published' in by[0][1]:
                by = by[1:]
            if by and by[0][0] == 'plain' and len(WORD.findall(by[0][1])) <= 12 \
                    and not CJK.search(by[0][1]) and '*' in by[0][1]:
                by = by[1:]  # byline 省略豁免
        n = max(len(bz), len(by))
        for i in range(n):
            tz = bz[i][0] if i < len(bz) else None
            ty = by[i][0] if i < len(by) else None
            zt_ = bz[i][1] if i < len(bz) else ''
            yt_ = by[i][1] if i < len(by) else ''
            if tz != ty:
                mm.append({'sec': si, 'yw_i': i, 'type_yw': ty, 'type_zh': tz,
                           'yw_head': yt_[:50], 'zh_head': zt_[:50]})
                continue
            if ty == 'plain':
                if not CJK.search(zt_):
                    untranslated.append(yt_[:60])
                    continue
                words = len(WORD.findall(yt_))
                if words >= 15:
                    ratio = len(zt_) / float(words)
                    if not (1.1 <= ratio <= 3.4):
                        ratio_flags.append({'sec': si, 'i': i, 'ratio': round(ratio, 2),
                                            'zh_head': zt_[:60], 'yw_head': yt_[:60]})
    rec['para_mismatch'] = mm[:20]
    rec['n_para_mismatch'] = len(mm)
    rec['untranslated'] = untranslated[:10]
    rec['n_untranslated'] = len(untranslated)
    rec['ratio_flags'] = ratio_flags[:20]
    rec['n_ratio_flags'] = len(ratio_flags)
    return rec


def main(argv):
    args = [a for a in argv if not a.startswith('--')]
    calib = '--calib' in argv
    limit = None
    letters = None
    if '--limit' in argv:
        limit = int(argv[argv.index('--limit') + 1])
    if '--letters' in argv:
        letters = argv[argv.index('--letters') + 1].split(',')
    out = None
    if '--out' in argv:
        out = argv[argv.index('--out') + 1]

    targets = []
    if calib:
        slugs = argv[argv.index('--calib') + 1].split(',')
        for s in slugs:
            targets.append((s[0], s))
    else:
        for letter in sorted(os.listdir(ROOT)):
            if len(letter) == 1 and letter.isalpha() and os.path.isdir(os.path.join(ROOT, letter)) \
                    and (letters is None or letter in letters):
                for fn in sorted(os.listdir(os.path.join(ROOT, letter))):
                    if fn.endswith('.md'):
                        slug = fn[:-3]
                        if args and slug not in args:
                            continue
                        targets.append((letter, slug))
        if args:
            targets = [t for t in targets if t[1] in args]
    if limit:
        targets = targets[:limit]

    recs = []
    for letter, slug in targets:
        try:
            rec = scan_entry(letter, slug, calib=calib)
        except Exception as e:  # noqa
            rec = {'slug': slug, 'letter': letter, 'skip': 'error: %s' % e}
        recs.append(rec)
        if calib:
            print(json.dumps(rec, ensure_ascii=False, indent=1)[:3000])
    if not calib:
        out = out or os.path.join(ROOT, 'specs', '022-post-reconvert-proofread', 'results',
                                  'scan-latest.jsonl')
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with io.open(out, 'w', encoding='utf-8') as f:
            for r in recs:
                f.write(json.dumps(r, ensure_ascii=False) + '\n')
        n = len([r for r in recs if r.get('kind') == 'entry'])
        flagged = len([r for r in recs if r.get('kind') == 'entry'
                       and (r.get('n_ratio_flags') or r.get('n_para_mismatch')
                            or r.get('n_only_yw') or r.get('n_only_zh')
                            or r.get('tail_missing') or r.get('section_count_diff'))])
        clean = n - flagged
        print('entries=%d flagged=%d clean=%d -> %s' % (n, flagged, clean, out))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
