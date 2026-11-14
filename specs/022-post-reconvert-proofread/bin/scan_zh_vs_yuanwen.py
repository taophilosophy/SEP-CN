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
H2 = re.compile(r'^## .*$', re.M)

TAIL_MISSING_CANDIDATES = ('参考文献', '学术工具', '其他网络资源', '相关词条')
# 尾节/注释节识别（两侧同名异语；命中即跳过段配对，键集已全文比对）
TAIL_PAT = re.compile(
    r'^(参考文献|References|Bibliography|Notes and References|学术工具|Academic Tools?|'
    r'其他网络资源|Other Internet Resources|相关词条|Related Entries|脚注|Notes|'
    r'Primary Literature|Secondary Literature|Acknowledg)', re.I)
TAIL_PATTERNS = (
    re.compile(r'^##\s*(参考文献|References|Bibliography)', re.I),
    re.compile(r'^##\s*(学术工具|Academic Tools?)', re.I),
    re.compile(r'^##\s*(其他网络资源|Other Internet Resources)', re.I),
    re.compile(r'^##\s*(相关词条|Related Entries)', re.I),
)
TAIL_TITLE_PAT = re.compile(
    r'(参考文献|References|Bibliography|学术工具|Academic Tools|其他网络资源|'
    r'Other Internet Resources|相关词条|Related Entries|脚注|Notes|Literature|'
    r'Acknowledg|致谢|Supplementary|延伸阅读|Further reading)', re.I)


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
    if rec['kind'] == 'stub':
        return rec
    if not os.path.exists(yw_p):
        rec['skip'] = 'no-yuanwen'
        return rec
    yw = read(yw_p)

    # ---- 全文标记与 defs 键集 ----
    mk_zh = Counter(norm_key(m.group(1)) for m in MARKER.finditer(zh))
    mk_yw = Counter(norm_key(m.group(1)) for m in MARKER.finditer(yw))
    mk_zh.pop('key', None)  # 照录说明行的字面 [^key] 非真键
    mk_yw.pop('key', None)
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

    # ---- 尾节四件套（双形态标题） ----
    if not slug.endswith('.supplement'):
        h2s = [m.group(0) for m in re.finditer(r'^## .*$', zh, re.M)]
        rec['tail_missing'] = [
            t for t, pat in zip(TAIL_MISSING_CANDIDATES, TAIL_PATTERNS)
            if not any(pat.search(h) for h in h2s)]
    else:
        rec['tail_missing'] = []

    # ---- 节序列与段落配对 ----
    sz, sy = sections_of(zh), sections_of(yw)
    rec['sections_zh'] = len(sz)
    rec['sections_yw'] = len(sy)
    # 节差只对正文节计（尾节形态差异合法：原生脚注型 zh 多 ## 脚注；引用注释型双语同构）
    body_z = [t for t, _ in sz if not TAIL_TITLE_PAT.search(t or '')]
    body_y = [t for t, _ in sy if not TAIL_TITLE_PAT.search(t or '')]
    rec['body_sections'] = {'zh': len(body_z), 'yw': len(body_y)}
    if len(body_z) != len(body_y):
        rec['section_count_diff'] = {'zh': body_z, 'yw': body_y}
    mm, untranslated, ratio_flags = [], [], []
    unpaired_yw, unpaired_zh = [], []
    import difflib
    for si, ((zt, zb), (yt, yb)) in enumerate(zip(sz, sy)):
        # 尾节/注释节（双形态标题）：只比键集（全文已比），段落不配对
        if TAIL_TITLE_PAT.search(zt or '') or TAIL_TITLE_PAT.search(yt or ''):
            continue
        bz, by = blocks_of(zb), blocks_of(yb)
        # 导言节（## 前）：剥 H1/pubinfo/byline 元块，其余按位配对
        if zt == '' and yt == '':
            def is_meta(ty, bt):
                if ty == '#' or bt.startswith('#'):
                    return True
                if '首次发表于' in bt or 'First published' in bt:
                    return True
                if re.fullmatch(r'\*[^*]+\*', bt.strip()):
                    return True  # byline（斜体作者行）
                return False
            while bz and is_meta(*bz[0]):
                bz = bz[1:]
            while by and is_meta(*by[0]):
                by = by[1:]
        # 节内 difflib 块型序列对齐（容插删），只对齐对做比率探针
        tz_seq = [t for t, _ in bz]
        ty_seq = [t for t, _ in by]
        sm = difflib.SequenceMatcher(None, ty_seq, tz_seq, autojunk=False)
        for tag, i1, i2, j1, j2 in sm.get_opcodes():
            if tag == 'equal':
                for k in range(i2 - i1):
                    ty_, yt_ = by[i1 + k]
                    tz_, zt_ = bz[j1 + k]
                    if ty_ != 'plain':
                        continue
                    if not CJK.search(zt_):
                        untranslated.append({'sec': si, 'yw': yt_[:70]})
                        continue
                    words = len(WORD.findall(yt_))
                    if words >= 15:
                        ratio = len(zt_) / float(words)
                        if not (0.7 <= ratio <= 4.5):
                            ratio_flags.append({'sec': si, 'ratio': round(ratio, 2),
                                                'zh_head': zt_[:60], 'yw_head': yt_[:60]})
            elif tag == 'replace':
                for k in range(max(i2 - i1, j2 - j1)):
                    ty_ = by[i1 + k][0] if i1 + k < i2 else None
                    tz_ = bz[j1 + k][0] if j1 + k < j2 else None
                    yt_ = by[i1 + k][1] if i1 + k < i2 else ''
                    zt_ = bz[j1 + k][1] if j1 + k < j2 else ''
                    if ty_ == 'plain' and tz_ == 'plain':
                        if not CJK.search(zt_):
                            untranslated.append({'sec': si, 'yw': yt_[:70]})
                        else:
                            words = len(WORD.findall(yt_))
                            if words >= 15:
                                ratio = len(zt_) / float(words)
                                if not (0.7 <= ratio <= 4.5):
                                    ratio_flags.append({'sec': si, 'ratio': round(ratio, 2),
                                                        'zh_head': zt_[:60], 'yw_head': yt_[:60]})
                    elif ty_ == 'plain' and tz_ is None:
                        mm.append({'sec': si, 'kind': 'yw_only', 'type': ty_, 'head': yt_[:60]})
                    elif tz_ == 'plain' and ty_ is None:
                        mm.append({'sec': si, 'kind': 'zh_only', 'type': tz_, 'head': zt_[:60]})
                    else:
                        mm.append({'sec': si, 'kind': 'type', 'type_yw': ty_, 'type_zh': tz_,
                                   'yw_head': yt_[:50], 'zh_head': zt_[:50]})
            elif tag == 'delete':
                for k in range(i1, i2):
                    mm.append({'sec': si, 'kind': 'yw_only', 'type': by[k][0],
                               'head': by[k][1][:60]})
            elif tag == 'insert':
                for k in range(j1, j2):
                    mm.append({'sec': si, 'kind': 'zh_only', 'type': bz[k][0],
                               'head': bz[k][1][:60]})
    rec['para_mismatch'] = mm[:24]
    rec['n_para_mismatch'] = len(mm)
    rec['untranslated'] = [u['yw'] for u in untranslated[:8]]
    rec['n_untranslated'] = len(untranslated)
    rec['ratio_flags'] = ratio_flags[:20]
    rec['n_ratio_flags'] = len(ratio_flags)
    return rec


def main(argv):
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
    skip_vals = {v for v in (out,) if v}
    args = [a for a in argv if not a.startswith("-") and a not in skip_vals]

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
        for o in recs:
            flags = []
            for k in ('n_para_mismatch', 'n_untranslated', 'n_ratio_flags'):
                if o.get(k):
                    flags.append('%s=%d' % (k[2:], o[k]))
            m = o.get('markers') or {}
            if m.get('n_only_yw') or m.get('n_only_zh'):
                flags.append('mk(+%d/-%d)' % (m.get('n_only_yw', 0), m.get('n_only_zh', 0)))
            d = o.get('defs') or {}
            if d.get('n_only_yw') or d.get('n_only_zh'):
                flags.append('defs(+%d/-%d)' % (d.get('n_only_yw', 0), d.get('n_only_zh', 0)))
            if o.get('tail_missing'):
                flags.append('tail:%s' % '|'.join(o['tail_missing']))
            if o.get('section_count_diff'):
                flags.append('SECS:%d/%d' % (o['sections_zh'], o['sections_yw']))
            if o.get('skip'):
                flags.append('SKIP:%s' % o['skip'])
            print('%-22s %s' % (o.get('slug', '?'), ' '.join(flags) or 'CLEAN'))
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
