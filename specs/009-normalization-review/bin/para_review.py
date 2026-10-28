#!/usr/bin/env python3
"""009 全量逐段复核驱动器：en/ HTML ↔ yuanwen/ md 全段对齐 + 分歧标记 + 形状特征。

spec: specs/009-normalization-review/spec.md「全量逐段复核（长线战役）」「确保 SUMMARY 正确」。

用法（在仓库根执行）:
  python specs/009-normalization-review/bin/para_review.py --letters a,b   # 字母批
  python specs/009-normalization-review/bin/para_review.py --slugs a/abduction,p/pm-notation
  python specs/009-normalization-review/bin/para_review.py --limit 3       # 冒烟
  python specs/009-normalization-review/bin/para_review.py --summary       # 聚合进度

断点续跑: results/para-review/review-log.jsonl 已录入词条自动跳过（--force 重跑）。
产物: review-log.jsonl（一行一词）+ <slug>.json（对齐明细/分歧段/抽检段/标题链）。
分歧段人工裁定由审阅者另落 adjudication.jsonl，本工具只读被审文件（en/、yuanwen/、
SUMMARY.md、zh 词条），零写入。
"""
import argparse
import difflib
import html as htmllib
import json
import os
import re
import sys
from datetime import datetime, timezone

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.abspath(os.path.join(_HERE, '..', '..', '..'))
sys.path.insert(0, _ROOT)

from tools import parser                      # noqa: E402
from tools.common import repo_path, read_text  # noqa: E402
from tools.yuanwen import (extract_blocks_raw, strip_closed_comments,  # noqa: E402
                           SUB_MAP, SUP_MAP)

SUBCH = re.compile('[%s]' % re.escape(''.join(SUB_MAP.values())))
SUPCH = re.compile('[%s]' % re.escape(''.join(SUP_MAP.values())))

OUT_DIR = os.path.join(_HERE, '..', 'results', 'para-review')
LOG_PATH = os.path.join(OUT_DIR, 'review-log.jsonl')
RATIO_MIN = 0.95

MATH_TEX = re.compile(r'\\\[.*?\\\]|\\\(.*?\\\)', re.S)
MATH_MD = re.compile(r'\$\$.+?\$\$|\$[^$\n]+?\$', re.S)
CITE_MARK = re.compile(r'\[\d{1,3}\]')
FNREF = re.compile(r'\[\^[^\]\s]+\]')
IMG_MD = re.compile(r'!\[[^\]]*\]\([^)]*\)')
MDLINK = re.compile(r'\[([^\]]*)\]\([^)]*\)')
TAG = re.compile(r'<[^>]+>')
BACKLINK_TXT = re.compile(r'[↩↑]')


def _ws(t):
    return re.sub(r'\s+', ' ', t).strip()


def norm_html(inner):
    t = re.sub(r'<sub\b[^>]*>.*?</sub>', ' ⟦S⟧ ', inner, flags=re.S | re.I)
    t = re.sub(r'<sup\b[^>]*>.*?</sup>', ' ⟦P⟧ ', t, flags=re.S | re.I)
    t = MATH_TEX.sub(' ⟦M⟧ ', t)
    t = TAG.sub(' ', t)
    t = htmllib.unescape(t)
    t = CITE_MARK.sub(' ', t)
    t = BACKLINK_TXT.sub(' ', t)
    t = re.sub(r'\\\[|\\\]|\\\(|\\\)', ' ⟦M⟧ ', t)  # 跨块被腰斩的公式残余定界符
    return _ws(t)


def _strip_md_deco(t):
    lines = []
    for ln in t.split('\n'):
        hm = re.match(r'^(#{1,6})\s+(.*)$', ln)
        if hm:
            lines.append(hm.group(2))          # 标题只剥 #，编号是 SEP 原文不剥
            continue
        ln = re.sub(r'^\s*> ?', '', ln)
        ln = re.sub(r'^\s*[-*+]\s+', '', ln)
        ln = re.sub(r'^\s*\d+\.\s+', '', ln)
        lines.append(ln)
    t = '\n'.join(lines)
    t = re.sub(r'\*\*([^*]+)\*\*', r'\1', t)
    t = re.sub(r'\*([^*\n]+)\*', r'\1', t)
    t = re.sub(r'_([^_\n]+)_', r'\1', t)
    t = re.sub(r'`([^`]+)`', r'\1', t)
    return t


def norm_md(chunk):
    t = IMG_MD.sub(' ', chunk)
    t = re.sub(r'_\{[^}]*\}', ' ⟦S⟧ ', t)          # 上下标记号归一（T-02）
    t = re.sub(r'\^\{[^}]*\}', ' ⟦P⟧ ', t)
    t = SUBCH.sub(' ⟦S⟧ ', t)
    t = SUPCH.sub(' ⟦P⟧ ', t)
    t = re.sub(r'(⟦S⟧|⟦P⟧)+', lambda m: '⟦S⟧' if 'S' in m.group(0) else '⟦P⟧', t)
    t = MATH_MD.sub(' ⟦M⟧ ', t)
    t = MDLINK.sub(r'\1', t)
    t = FNREF.sub(' ', t)
    t = _strip_md_deco(t)
    lines = []
    for ln in t.split('\n'):
        if re.match(r'^\s*\|?[\s:|-]+\|?\s*$', ln):   # 表格分隔行
            continue
        if '|' in ln:
            ln = re.sub(r'\\\|', '\x01', ln)
            ln = ' '.join(p.strip() for p in ln.strip('|').split('|'))
            ln = ln.replace('\x01', '|')
        lines.append(ln)
    return _ws(' '.join(lines))


def md_shape(chunk):
    if re.match(r'^#{1,6}\s', chunk):
        return 'h%d' % len(re.match(r'^(#+)', chunk).group(1))
    if chunk.lstrip().startswith('|'):
        return 'table'
    if chunk.lstrip().startswith('$$'):
        return 'mathblock'
    if re.match(r'^\s*[-*+]\s', chunk):
        return 'ul'
    if re.match(r'^\s*\d+\.\s', chunk):
        return 'ol'
    if chunk.lstrip().startswith('>'):
        return 'blockquote'
    if IMG_MD.match(chunk.lstrip()):
        return 'image'
    return 'p'


def load_summary_titles():
    """SUMMARY.md → {slug: 条目文字}。链接文字可含嵌套方括号（如
    `Abelard [Abailard], Peter`），字母目录含数字开头词条（`1/xxx.md`）。"""
    titles, aliases = {}, {}
    for ln in read_text(repo_path('SUMMARY.md')).split('\n'):
        m = re.search(r'\]\(([a-z0-9])[/\\]([^/\\)]+\.md)\)', ln)
        if not m:
            continue
        end = m.start()                       # '](target)' 前的 ']'，回溯配对 '['
        depth, i = 1, end - 1
        while i >= 0:
            c = ln[i]
            if c == ']':
                depth += 1
            elif c == '[':
                depth -= 1
                if depth == 0:
                    break
            i -= 1
        if depth != 0:
            continue
        text = re.sub(r'\\([*\[\]])', r'\1', ln[i + 1:end]).strip()
        slug = m.group(2)[:-3]
        if '— see' in text or '—— see' in text:
            aliases[slug] = text
        else:
            titles[slug] = text
    return titles, aliases


def h1_of(md_text):
    m = re.match(r'^#\s+(.+)$', md_text.strip(), re.M)
    return _ws(re.sub(r'\\([*\[\]])', r'\1', m.group(1))) if m else None


def split_md_body(md_text):
    """去 H1；在前 3 个非空行内剥全斜体作者行；截 Notes/引用定义尾部；
    剔 References（引用注释）标题与体例说明块（T-07 设计：文献全量转脚注）。
    返回 (chunks, authors_found)。"""
    cut = len(md_text)
    mn = re.search(r'^## Notes（原文脚注', md_text, re.M)
    if mn:
        cut = min(cut, mn.start())
    mc = re.search(r'^\[\^[^\]]+\]:', md_text, re.M)
    if mc:
        cut = min(cut, mc.start())
    body = md_text[:cut].strip()
    lines = body.split('\n')
    rest = lines[1:]                        # H1
    seen, authors_found = 0, False
    out = []
    for ln in rest:
        if not ln.strip():
            out.append(ln)
            continue
        seen += 1
        if seen <= 3 and re.match(r'^\*[^*\n]+\*$', ln.strip()):
            authors_found = True
            continue                        # 作者行（meta 重组，html 侧作者块同样剔除）
        out.append(ln)
    body = '\n'.join(out)
    chunks = [c.strip() for c in re.split(r'\n\s*\n', body) if c.strip()]
    kept, in_refs = [], False
    for c in chunks:
        if re.match(r'^#{1,6}\s*References（引用注释）?\s*$', c):
            in_refs = True                    # T-07：文献节标题；其后 h3 小节与
            continue                          # 体例说明随节剔除，遇 h2 回到正文
        if in_refs:
            hm = re.match(r'^(#{1,6})\s', c)
            if hm and len(hm.group(1)) >= 3:
                continue
            if '原文参考文献已转为脚注引用' in c:
                continue
            in_refs = False
        kept.append(c)
    return kept, authors_found


def review_entry(rec, summary_titles):
    slug = rec['slug']
    letter = slug[0]
    idx_path = repo_path('en', slug, 'index.html')
    md_path = repo_path('yuanwen', letter, slug + '.md')
    out = {'slug': slug, 'letter': letter}
    if not os.path.exists(idx_path):
        out['state'] = 'error'
        out['error'] = 'no en/index.html'
        return out
    if not os.path.exists(md_path):
        out['state'] = 'error'
        out['error'] = 'no yuanwen md'
        return out
    html = read_text(idx_path)
    m, e = parser.HEAD_RE.search(html), parser.TAIL_RE.search(html)
    article = html[m.end():e.start()] if (m and e) else html
    article = strip_closed_comments(article)

    tm = re.search(r'<meta name="citation_title" content="([^"]*)"', html)
    authors = [htmllib.unescape(a) for a in
               re.findall(r'<meta name="citation_author" content="([^"]*)"', html)]
    supp = [f for f in os.listdir(repo_path('en', slug))
            if f.endswith('.html') and f not in ('index.html', 'notes.html')]

    hblocks = extract_blocks_raw(article)
    # 标题块（h1）、作者块、bib-container（T-07：md 侧对应段同样剔除）剔除；
    # pubinfo 保留（md 侧 **First published…** 与之配对）
    html_title = None
    n_bib = 0
    body_h = []
    for b in hblocks:
        t = norm_html(b['inner'])
        if b['type'] == 'h1' and html_title is None:
            html_title = t
            continue
        if b['type'] == 'bib-container':
            n_bib += 1
            continue
        if authors and t and len(t) < 300 and any(a in t for a in authors):
            continue  # 作者块（meta 重组，md 侧对应行已剥）
        if not t:
            continue
        body_h.append((b['type'], t))

    md_text = read_text(md_path)
    md_h1 = h1_of(md_text)
    chunks, _af = split_md_body(md_text)
    body_m = []
    for c in chunks:
        t = norm_md(c)
        if t:
            body_m.append((md_shape(c), t))

    # ---- 标题链：SUMMARY 条目文字 = zh H1（中文侧，硬）；
    #      yuanwen H1 = html 标题（英文侧，硬）；zh H1 含英文原题（参照）----
    zh_path = repo_path(letter, slug + '.md')
    zh_h1 = h1_of(read_text(zh_path)) if os.path.exists(zh_path) else None
    s_title = summary_titles.get(slug)
    html_title_eff = html_title or (htmllib.unescape(tm.group(1)) if tm else None)
    _deco = lambda s: re.sub(r'[*_]', '', s) if s else s   # 标题强调标记不参与比较
    chain = {
        'summary_title': s_title, 'zh_h1': zh_h1, 'yuanwen_h1': md_h1,
        'html_title': html_title_eff,
        'summary_eq_zh': bool(s_title and zh_h1 and s_title == zh_h1),
        'yuanwen_eq_html': bool(md_h1 and html_title_eff
                                and _deco(md_h1) == _deco(html_title_eff)),
        'zh_contains_en': bool(zh_h1 and html_title_eff and html_title_eff in zh_h1),
        'alias_row': slug not in summary_titles,
    }

    # ---- 序列对齐（区段级）：连续非 equal 区段先试整组合并比值
    #      （preamble/列表内拆块 1↔N 是转译形态，合上即不算分歧）----
    a = [t for _, t in body_h]
    b = [t for _, t in body_m]
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    pairs, flags, merged = [], [], []
    ops = sm.get_opcodes()
    k = 0
    while k < len(ops):
        tag, i1, i2, j1, j2 = ops[k]
        if tag == 'equal':
            for x in range(i2 - i1):
                pairs.append({'i': i1 + x, 'j': j1 + x, 'ratio': 1.0})
            k += 1
            continue
        grp = []
        while k < len(ops) and ops[k][0] != 'equal':
            grp.append(ops[k])
            k += 1
        htxt = ' '.join(a[x] for op in grp for x in range(op[1], op[2]))
        mtxt = ' '.join(b[x] for op in grp for x in range(op[3], op[4]))
        gr = difflib.SequenceMatcher(None, htxt, mtxt, autojunk=False).ratio()
        n_gh = sum(op[2] - op[1] for op in grp)
        n_gm = sum(op[4] - op[3] for op in grp)
        if gr >= RATIO_MIN:                     # 整组比值达标＝拆/合块转译形态（T-01 注记）
            merged.append({'ratio': gr, 'n_h': n_gh, 'n_m': n_gm,
                           'shape_h': [body_h[x][0] for op in grp
                                       for x in range(op[1], op[2])],
                           'shape_m': [body_m[x][0] for op in grp
                                       for x in range(op[3], op[4])]})
            continue
        for tag2, q1, q2, r1, r2 in grp:
            if tag2 == 'replace':
                for x in range(max(q2 - q1, r2 - r1)):
                    fi = q1 + x if x < q2 - q1 else None
                    fj = r1 + x if x < r2 - r1 else None
                    if fi is not None and fj is not None:
                        ratio = difflib.SequenceMatcher(
                            None, a[fi], b[fj], autojunk=False).ratio()
                        if ratio >= RATIO_MIN:
                            pairs.append({'i': fi, 'j': fj, 'ratio': ratio})
                            continue
                    flags.append({
                        'kind': 'replace', 'i': fi, 'j': fj,
                        'ratio': ratio if fi is not None and fj is not None else None,
                        'shape_h': body_h[fi][0] if fi is not None else None,
                        'shape_m': body_m[fj][0] if fj is not None else None,
                        'html_text': (a[fi][:800] if fi is not None else None),
                        'md_text': (b[fj][:800] if fj is not None else None)})
            elif tag2 == 'delete':
                for fi in range(q1, q2):
                    flags.append({'kind': 'delete', 'i': fi, 'j': None,
                                  'ratio': None, 'shape_h': body_h[fi][0],
                                  'shape_m': None, 'html_text': a[fi][:800],
                                  'md_text': None})
            else:
                for fj in range(r1, r2):
                    flags.append({'kind': 'insert', 'i': None, 'j': fj,
                                  'ratio': None, 'shape_h': None,
                                  'shape_m': body_m[fj][0], 'html_text': None,
                                  'md_text': b[fj][:800]})

    # ---- 形状特征对（T-rule 分布证据）----
    shape_pairs = {}
    pi = {p['i']: p['j'] for p in pairs}
    for i, (sh, _) in enumerate(body_h):
        j = pi.get(i)
        key = '%s→%s' % (sh, body_m[j][0] if j is not None else '∅')
        shape_pairs[key] = shape_pairs.get(key, 0) + 1
    for m in merged:
        key = 'merged×%d(%s→%s)' % (m['n_h'], '+'.join(m['shape_h']),
                                    '+'.join(m['shape_m']))
        shape_pairs[key] = shape_pairs.get(key, 0) + 1

    # ---- 抽检段（无分歧段 ≥3：最长段/含公式段/含表格或链接段）----
    clean = [(i, body_h[i][0], body_m[pi[i]][0], a[i], b[pi[i]])
             for i in sorted(pi) if a[i] and b[pi[i]]]
    spot = []
    if clean:
        picks = [max(clean, key=lambda x: len(x[3]))]
        mm = next((x for x in clean if '⟦M⟧' in x[3]), None)
        if mm:
            picks.append(mm)
        mt = next((x for x in clean if x[1] in ('table', 'ul', 'ol', 'figure')
                   or x[2] in ('table', 'ul', 'ol')), None)
        if mt and mt not in picks:
            picks.append(mt)
        for i, sh, sm2, ht, mdt in picks[:3]:
            spot.append({'i': i, 'shape_h': sh, 'shape_m': sm2,
                         'html_text': ht[:500], 'md_text': mdt[:500]})

    out.update({
        'state': 'flagged' if flags else 'ok',
        'n_html': len(body_h), 'n_md': len(body_m), 'n_pairs': len(pairs),
        'n_flags': len(flags), 'n_merged': len(merged), 'merged': merged,
        'n_bib_html': n_bib, 'title_chain': chain,
        'shape_pairs': shape_pairs, 'flags': flags, 'spot': spot,
        'supplements': supp, 'meta_title': htmllib.unescape(tm.group(1)) if tm else None,
        'authors': authors,
    })
    return out


def load_done():
    done = {}
    if os.path.exists(LOG_PATH):
        with open(LOG_PATH, encoding='utf-8') as fh:
            for ln in fh:
                try:
                    r = json.loads(ln)
                    done[r['slug']] = r['state']
                except Exception:
                    pass
    return done


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--letters')
    ap.add_argument('--slugs')
    ap.add_argument('--limit', type=int)
    ap.add_argument('--force', action='store_true')
    ap.add_argument('--summary', action='store_true')
    args = ap.parse_args()

    if args.summary:
        from collections import Counter
        st, letters = Counter(), Counter()
        if os.path.exists(LOG_PATH):
            with open(LOG_PATH, encoding='utf-8') as fh:
                for ln in fh:
                    r = json.loads(ln)
                    st[r['state']] += 1
                    letters[r['letter']] += 1
        print('states:', dict(st))
        print('letters:', dict(sorted(letters.items())))
        return

    entries = json.load(open(repo_path('baseline', 'entries.json'), encoding='utf-8'))['entries']
    slugs = sorted(e['slug'] for e in entries)
    if args.slugs:
        slugs = [s for s in args.slugs.split(',') if s]
    elif args.letters:
        keep = {s.strip() for s in args.letters.split(',')}
        slugs = [s for s in slugs if s[0] in keep]
    done = {} if args.force else load_done()
    summary_titles, _aliases = load_summary_titles()
    os.makedirs(OUT_DIR, exist_ok=True)

    n_done = 0
    for slug in slugs:
        if slug in done:
            continue
        if args.limit and n_done >= args.limit:
            break
        rec = {'slug': slug, 'letter': slug[0]}
        try:
            r = review_entry(rec, summary_titles)
        except Exception as exc:                       # 逐条隔离，不中断批次
            r = {'slug': slug, 'letter': slug[0], 'state': 'error', 'error': repr(exc)}
        with open(LOG_PATH, 'a', encoding='utf-8', newline='\n') as fh:
            tc = r.get('title_chain', {})
            fh.write(json.dumps({
                'slug': slug, 'letter': slug[0], 'state': r.get('state'),
                'n_pairs': r.get('n_pairs'), 'n_flags': r.get('n_flags'),
                'title_ok': bool(tc.get('summary_eq_zh') and tc.get('yuanwen_eq_html')),
                'summary_eq_zh': tc.get('summary_eq_zh'),
                'yuanwen_eq_html': tc.get('yuanwen_eq_html'),
                'at': datetime.now(timezone.utc).isoformat(timespec='seconds'),
            }, ensure_ascii=False) + '\n')
        if r.get('state') != 'error':
            with open(os.path.join(OUT_DIR, slug.replace('/', '_') + '.json'),
                      'w', encoding='utf-8', newline='\n') as fh:   # ok 词条也落盘（抽检凭证）
                json.dump(r, fh, ensure_ascii=False, indent=1)
        tc = r.get('title_chain', {})
        print('%-40s %-8s pairs=%-5s flags=%-4s title[s=zh:%s yw=html:%s zh含en:%s]' % (
            slug, r.get('state'), r.get('n_pairs'), r.get('n_flags'),
            tc.get('summary_eq_zh'), tc.get('yuanwen_eq_html'),
            tc.get('zh_contains_en')))
        n_done += 1
    print('本批处理:', n_done)


if __name__ == '__main__':
    main()
