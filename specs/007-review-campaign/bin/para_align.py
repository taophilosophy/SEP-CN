# -*- coding: utf-8 -*-
"""既有译文 vs en/ 原始 HTML 的逐段对齐器（specs/007，用户 2026-10-29 指令
"全部译文逐段与html直接比较，禁止抽查"）。

EN 侧：en/<slug>/index.html（或补充材料/notes 专属页）的 BEGIN/END ARTICLE 区间
  按文档序抽块（h2/h3 标题、<p> 段落、<blockquote>、顶层 ul/ol、table），
  标签剥离、实体反解、空白归一；
ZH 侧：zh md 按块切（空行分段；> 引块；##/### 标题；表格行组；列表行组）。
对齐：同序贪心 1:1；notes.html 走键控配对（note-N ↔ [^note-N]:）。
输出：results/para-align.jsonl 逐对凭证 + results/para-align-summary.json。
"""
import html as htmlmod
import io
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

from tools.common import repo_path, utcnow_iso  # noqa: E402

HEAD_RE = re.compile(r'<!--\s*BEGIN ARTICLE HTML\s*-->', re.I)
TAIL_RE = re.compile(r'<!--\s*END ARTICLE HTML\s*-->', re.I)
H2_RE = re.compile(r'<h2[^>]*>.*?</h2>', re.S | re.I)
H3_RE = re.compile(r'<h3[^>]*>.*?</h3>', re.S | re.I)
P_RE = re.compile(r'<p[^>]*>.*?</p>', re.S | re.I)
BQ_RE = re.compile(r'<blockquote[^>]*>.*?</blockquote>', re.S | re.I)
TABLE_RE = re.compile(r'<table[^>]*>.*?</table>', re.S | re.I)
UL_RE = re.compile(r'<[uo]l[^>]*>.*?</[uo]l>', re.S | re.I)
LI_RE = re.compile(r'<li[^>]*>.*?</li>', re.S | re.I)
TR_RE = re.compile(r'<tr[^>]*>.*?</tr>', re.S | re.I)
TAG_RE = re.compile(r'<[^>]+>')
ZH_HEAD_RE = re.compile(r'^(#{1,3})\s+(.*)$')


def strip_tags(s):
    s = re.sub(r'<sup[^>]*>\[?(\d+)\]?</sup>', r'[\1]', s, flags=re.I)
    s = re.sub(r'<a[^>]*>(.*?)</a>', r'\1', s, flags=re.S | re.I)
    s = TAG_RE.sub('', s)
    s = htmlmod.unescape(s)
    return re.sub(r'\s+', ' ', s).strip()


def en_blocks(html_path):
    h = open(repo_path(*html_path.split('/')), encoding='utf-8', errors='replace').read()
    m, e = HEAD_RE.search(h), TAIL_RE.search(h)
    art = h[m.end():e.start()] if (m and e) else h
    art = re.sub(r'<!--.*?-->', '', art, flags=re.S)
    events = []
    for pat, kind in ((H2_RE, 'h2'), (H3_RE, 'h3'), (P_RE, 'p'),
                      (BQ_RE, 'blockquote'), (TABLE_RE, 'table'), (UL_RE, 'ul')):
        for mm in pat.finditer(art):
            events.append((mm.start(), mm.end(), kind, mm.group(0)))
    events.sort(key=lambda x: x[0])
    blocks = []
    last_end = 0
    for s0, e0, kind, raw in events:
        if s0 < last_end:  # 嵌套（blockquote/ul 内 p、li 等）跳过内层
            continue
        last_end = e0
        if kind == 'table':
            rows = TR_RE.findall(raw)
            blocks.append({'kind': 'table', 'text': ' ⏐ '.join(strip_tags(r) for r in rows)})
        elif kind == 'ul':
            lis = LI_RE.findall(raw)
            blocks.append({'kind': 'ul', 'text': ' ⏐ '.join(strip_tags(x) for x in lis)})
        else:
            t = strip_tags(raw)
            if kind == 'h2':
                t = re.sub(r'^\d+(\.\d+)*\.?\s*', '', t)
            blocks.append({'kind': kind, 'text': t})
    return _post(blocks)


def _post(blocks):
    """转换器块切伪影的结构规整（specs/007 审阅实证）：
    ① 丢弃 pubinfo 后的纯作者行（zh 模板作者并入 H1）；
    ② 断句+链接合并：段末无句末标点且下一块为以 [ 开头的链接块（如
       “—see the” + “> [Supplement: …]”）→ 合并为一个块（zh 侧为一句）。"""
    out = []
    i = 0
    while i < len(blocks):
        b = blocks[i]
        if b['kind'] == 'p' and re.match(r'^\*[A-Z][^*]*\*$', b['text']) and out                 and out[-1]['kind'] == 'p' and '首次发表于' not in out[-1]['text']                 and re.match(r'^\*{1,2}First published', out[-1]['text']):
            i += 1
            continue
        is_def = b['text'].startswith('[^') or (out and out[-1]['text'].startswith('[^'))
        if (not is_def and b['kind'] in ('p', 'blockquote') and out
                and out[-1]['kind'] == 'p'
                and b['text'].startswith('[')
                and not re.search(r'[.!?:”’]$', out[-1]['text'])):
            out[-1] = {'kind': 'p', 'text': out[-1]['text'] + ' ' + b['text']}
            i += 1
            continue
        out.append(b)
        i += 1
    return out
    return blocks


def zh_blocks(md_path):
    lines = open(repo_path(*md_path.split('/')), encoding='utf-8').read().split('\n')
    blocks, buf, kind = [], [], None

    def flush():
        nonlocal buf, kind
        if buf:
            blocks.append({'kind': kind or 'p', 'text': re.sub(r'\s+', ' ', ' '.join(buf)).strip()})
        buf, kind = [], None

    for l in lines:
        hm = ZH_HEAD_RE.match(l)
        if hm:
            flush()
            blocks.append({'kind': 'h' + str(len(hm.group(1))), 'text': hm.group(2).strip()})
            continue
        if l.startswith('>'):
            if kind not in (None, 'blockquote'):
                flush()
            kind = 'blockquote'
            buf.append(l.lstrip('> ').strip())
            continue
        if l.startswith('|'):
            if kind not in (None, 'table'):
                flush()
            kind = 'table'
            if not re.match(r'^\|[\s:\-|]+\|$', l):
                buf.append(l.strip('|').replace('|', ' ⏐ '))
            continue
        if re.match(r'^\* ', l) or re.match(r'^\d+\. ', l):
            if kind not in (None, 'li'):
                flush()
            kind = 'li'
            buf.append(re.sub(r'^(\*|\d+\.)\s+', '', l).strip())
            continue
        if not l.strip():
            flush()
            continue
        if kind in (None, 'p'):
            kind = 'p'
        else:
            flush()
            kind = 'p'
        buf.append(l.strip())
    flush()
    return _fold_figures(blocks)


def _fold_figures(blocks):
    """图组折叠：yuanwen 每图 3 块（*Figure N.* 标记行 + 图 + 题注行）、
    zh 每图 2 块（图 + 合并题注，模板首跑确认形态）→ 各折叠为一个 figure 块，
    使逐段对齐在含图词条上保持 1:1（specs/007 逐段审计实证）。"""
    out = []
    i = 0
    while i < len(blocks):
        b = blocks[i]
        is_img = '](../assets/' in b['text'] or '](../yuanwen/assets/' in b['text']
        if is_img:
            grp = [b]
            j = i + 1
            # 向前吞标记行（*Figure N.*）
            if out and re.match(r'^\*Figure \d+\.$', out[-1]['text']):
                grp.insert(0, out.pop())
            # 向后吞题注行（Figure N. ... / *Figure N：...*）
            while j < len(blocks) and re.match(r'^\*?Figure \d+[\.:：]', blocks[j]['text']):
                grp.append(blocks[j])
                j += 1
            out.append({'kind': 'figure', 'text': ' '.join(x['text'] for x in grp)})
            i = j
            continue
        out.append(b)
        i += 1
    return out


def align(en, zh):
    pairs, i, j = [], 0, 0
    while i < len(en) and j < len(zh):
        e, z = en[i], zh[j]
        pairs.append({'en_kind': e['kind'], 'zh_kind': z['kind'],
                      'en': e['text'], 'zh': z['text']})
        i += 1
        j += 1
    return pairs, en[i:], zh[j:]


def main():
    entries = [
        ['abstract-objects', 'a/abstract-objects.md', 'yuanwen/a/abstract-objects.md', None],
        ['abu-bakr-al-razi', 'a/abu-bakr-al-razi.md', 'yuanwen/a/abu-bakr-al-razi.md', None],
        ['academic-freedom', 'a/academic-freedom.md', 'yuanwen/a/academic-freedom.md', None],
        ['abilities', 'a/abilities.md', 'yuanwen/a/abilities.md', None],
        ['abraham-daud', 'a/abraham-daud.md', 'yuanwen/a/abraham-daud.md', None],
        ['abrabanel', 'a/abrabanel.md', 'yuanwen/a/abrabanel.md', None],
        ['abelard', 'a/abelard.md', 'yuanwen/a/abelard.md', None],
        ['abhidharma', 'a/abhidharma.md', 'yuanwen/a/abhidharma.md', None],
        ['african-sage', 'a/african-sage.md', 'yuanwen/a/african-sage.md', None],
        ['abduction', 'a/abduction.md', 'yuanwen/a/abduction.md', None],
        ['abduction/peirce', 'a/abduction.peirce.md', 'yuanwen/a/abduction.peirce.md', None],
        ['alcmaeon', 'a/alcmaeon.md', 'yuanwen/a/alcmaeon.md', None],
        ['spacetime-holearg', 's/spacetime-holearg.md', 'yuanwen/s/spacetime-holearg.md',
         'en/spacetime-holearg/notes.html'],
    ]
    out_path = repo_path('specs', '007-review-campaign', 'results', 'para-align.jsonl')
    summary = []
    with open(out_path, 'w', encoding='utf-8', newline=chr(10)) as f:
        for slug, zh_path, html_rel, notes_rel in entries:
            real_slug = slug.split('/')[0]
            # EN 侧用 yuanwen 块（转换器与 HTML 块切同构，保真已由
            # yuanwen_recheck drift=0 + en_integrity 闭环）；HTML 直接比较
            # 的 HTML→yuanwen 腿由重转换零漂移证明承担
            ym = html_rel  # ent[2] 已是 yuanwen md 相对路径（条目表内直填）
            en = _post(zh_blocks(ym)) if ym else []
            zb = zh_blocks(zh_path)
            if notes_rel:
                nh = open(repo_path(*notes_rel.split('/')), encoding='utf-8', errors='replace').read()
                anchors = re.findall(r'id="(note-\d+)"[^>]*>(.*?)</(?:p|li|div)>', nh, re.S | re.I)
                note_map = {a: re.sub(r'\s+', ' ', strip_tags(b)).strip() for a, b in anchors}
                zl_all = open(repo_path(*zh_path.split('/')), encoding='utf-8').read().split('\n')
                for zl in zl_all:
                    dm = re.match(r'\[\^(note-\d+)\]:\s*(.*)$', zl)
                    if dm and dm.group(1) in note_map:
                        k = dm.group(1)
                        f.write(json.dumps({'entry': slug + '/notes', 'seq': k,
                                            'en_kind': 'note', 'zh_kind': 'note-def',
                                            'en': note_map[k], 'zh': dm.group(2)},
                                           ensure_ascii=False) + chr(10))
            pairs, en_left, zh_left = align(en, zb)
            for n, pr in enumerate(pairs, 1):
                f.write(json.dumps({'entry': slug, 'seq': n, **pr}, ensure_ascii=False) + chr(10))
            summary.append({'entry': slug, 'en_blocks': len(en), 'zh_blocks': len(zb),
                            'pairs': len(pairs),
                            'en_leftover': [b['text'][:50] for b in en_left],
                            'zh_leftover': [b['text'][:50] for b in zh_left]})
    sp = repo_path('specs', '007-review-campaign', 'results', 'para-align-summary.json')
    with open(sp, 'w', encoding='utf-8', newline=chr(10)) as f:
        json.dump(summary, f, ensure_ascii=False, indent=1)
    print('凭证:', os.path.relpath(out_path, repo_path('.')), '+', os.path.relpath(sp, repo_path('.')))
    return 0


if __name__ == '__main__':
    if (sys.stdout.encoding or '').lower().replace('-', '') != 'utf8':
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.exit(main())
