# -*- coding: utf-8 -*-
"""原文 Markdown 镜像生成器（yuanwen/）——用户 2026-10-27 裁定。

把 en/<slug>/index.html（不可变原始抓取物）确定性转换为 yuanwen/<字母>/<slug>.md：
- 结构镜像中文仓库：字母目录 + yuanwen/SUMMARY.md（--summary 生成，已转换条目改链 yuanwen 路径）
- 脚注：正文 <sup>[<a href="notes.html#n">n</a>]</sup> → [^note-n]；notes.html → 文末脚注定义
- 补充材料：en/<slug>/<x>.html → yuanwen/<字母>/<slug>.<x>.md，正文内相对互链
- 图片：![](../../en/<slug>/imageN.jpg) 相对引用本地原始抓取物，不复制不外链
- 参考文献转引用注释：文内 (Author year, page) 引用组后追加 [^key]；文献节改为脚注定义；
  数学定界符、DK 编号、古代作品行号原样保留；<sub>/<sup> 标签保留（工作底稿不受
  发布体例"禁止 HTML"约束，登记 demo-log）
- 确定性：同源 HTML 必得同 md；审计链登记于 baseline/entries.json（md 哈希 + 源哈希）

用法: python tools/yuanwen.py <slug>... | --all-baselined [--summary] [--force]
输出: stdout JSON {converted: [...], failures: [...], summary_links_rewritten}
"""
import json
import os
import re
import sys
from html import unescape

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools import parser  # noqa: E402
from tools.common import (  # noqa: E402
    find_zh_doc, load_json, read_text, repo_path, sha256_file, utcnow_iso,
    write_json_verified, write_text_verified)

BLOCK_OPEN_RE = re.compile(
    r'<(?P<tag>h1|h2|h3|h4|p|blockquote|table|ul|ol|dl|pre|div)\b(?P<attrs>[^>]*)>', re.I)
MATH_RE = re.compile(r'(\$\$.*?\$\$|\\\[.*?\\\]|\\\(.*?\\\))', re.S)
SUP_KEEP_RE = re.compile(r'<(su[bp])>.*?</\1>', re.S | re.I)
NOTE_REF_RE = re.compile(
    r'<sup>\s*\[?\s*<a\s+href="notes\.html#(\d+)"[^>]*>\s*\d*\s*</a>\s*\]?\s*</sup>', re.I)
SPECIAL_DIV_RE = re.compile(r'pubinfo|preamble|figure|bibliography', re.I)
SKIP_DIV_RE = re.compile(r'\btoc\b', re.I)


# ---------------------------------------------------------------- blocks ----

def _div_kind(attrs):
    idm = re.search(r'id="([^"]*)"', attrs)
    clm = re.search(r'class="([^"]*)"', attrs)
    ident = (idm.group(1) if idm else '') + ' ' + (clm.group(1) if clm else '')
    if SKIP_DIV_RE.search(ident):
        return 'skip'
    if re.search(r'\bpubinfo\b', ident, re.I):
        return 'pubinfo'
    if re.search(r'\bpreamble\b', ident, re.I):
        return 'preamble'
    if re.search(r'\bbibliography\b', ident, re.I):
        return 'bib-container'
    if re.search(r'\bfigure\b', ident, re.I):
        return 'figure'
    return 'wrapper'


def _find_close(html, tag, start):
    """返回与 start 处开标签配对的闭标签结束位置；找不到返回 len(html)。"""
    depth = 1
    for cm in re.finditer(r'<(/?)%s\b[^>]*>' % tag, html[start:], re.I):
        depth += -1 if cm.group(1) else 1
        if depth == 0:
            return start + cm.end()
    return len(html)


def extract_blocks_raw(html):
    """按块级标签切分 HTML → [{type, attrs, inner}]，inner 为原始 HTML 片段。"""
    blocks = []
    i = 0
    n = len(html)
    while i < n:
        m = BLOCK_OPEN_RE.search(html, i)
        if not m:
            break
        tag = m.group('tag').lower()
        attrs = m.group('attrs') or ''
        if tag == 'div':
            kind = _div_kind(attrs)
            if kind == 'wrapper':
                i = m.end()          # 透明包装：递归处理其内容
                continue
            end = _find_close(html, 'div', m.end())
            inner = html[m.end():end]
            inner = re.sub(r'</div>\s*$', '', inner)  # 去掉自身闭标签残余
            if kind == 'skip':
                i = end
                continue
            blocks.append({'type': kind, 'attrs': attrs, 'inner': inner})
            i = end
            continue
        end = _find_close(html, tag, m.end())
        inner = html[m.end():end]
        inner = re.sub(r'</%s>\s*$' % tag, '', inner, flags=re.I)
        blocks.append({'type': tag, 'attrs': attrs, 'inner': inner})
        i = end
    return blocks


# ---------------------------------------------------------------- inline ----

def inline_to_md(html, slug=None):
    """行内 HTML → Markdown 文本。数学与 sub/sup 占位保护后原样还原。"""
    if not html:
        return ''
    s = re.sub(r'<!--.*?-->', '', html, flags=re.S)
    s = NOTE_REF_RE.sub(lambda m: '[^note-%s]' % m.group(1), s)
    # 用户 2026-10-27 指令：禁止 HTML 标签，保持洁净——sub/sup 一律转纯文本记法
    # （下标 _{x}、上标 ^{x}），不再保留 <sub>/<sup> 标签
    s = re.sub(r'<sub>(.*?)</sub>', lambda m: '_{%s}' % m.group(1), s, flags=re.S | re.I)
    s = re.sub(r'<sup>(.*?)</sup>', lambda m: '^{%s}' % m.group(1), s, flags=re.S | re.I)
    store = []

    def _stash(m):
        store.append(m.group(0))
        return '\x00%d\x00' % (len(store) - 1)

    s = MATH_RE.sub(_stash, s)

    def _link(m):
        href = (m.group('href') or '').strip()
        text = m.group('t')
        if href.startswith('#') or href.startswith('index.html#'):
            return text
        if href.startswith('notes.html#'):
            return '[^note-%s]' % href.split('#')[1].split('&')[0]
        if re.fullmatch(r'[a-zA-Z0-9][a-zA-Z0-9._-]*\.html', href) and slug:
            base = href[:-5]
            return '[%s](%s.%s.md)' % (text, slug, base)
        if href.startswith(('http:', 'https:')):
            return '[%s](%s)' % (text, href)
        return text

    s = re.sub(r'<a\b[^>]*href="(?P<href>[^"]*)"[^>]*>(?P<t>.*?)</a>',
               _link, s, flags=re.S | re.I)
    s = re.sub(r'<(?:em|i)>(.*?)</(?:em|i)>', r'*\1*', s, flags=re.S | re.I)
    s = re.sub(r'<(?:strong|b)>(.*?)</(?:strong|b)>', r'**\1**', s, flags=re.S | re.I)
    s = re.sub(r'<code>(.*?)</code>', r'`\1`', s, flags=re.S | re.I)
    s = re.sub(r'<br\s*/?>', ' ', s, flags=re.I)
    s = re.sub(r'</?span[^>]*>', '', s, flags=re.I)
    s = re.sub(r'<img[^>]*>', '', s, flags=re.I)
    s = re.sub(r'<[^>]+>', '', s)
    s = unescape(s)
    s = re.sub(r'[ \t\r\n\f\v]+', ' ', s).strip()
    for idx, val in enumerate(store):
        # 恢复的数学/sub/sup 内容也要 unescape：源里 \(x &lt; y\) 的实体
        # 在占位保护期躲过了正文 unescape（演示轮 2 复核发现）
        s = s.replace('\x00%d\x00' % idx, unescape(val))
    return s


def table_to_md(inner, slug):
    rows = []
    for rm in re.finditer(r'<tr[^>]*>(.*?)</tr>', inner, re.S | re.I):
        cells = [_cell(c, slug)
                 for c in re.findall(r'<t[dh][^>]*>(.*?)</t[dh]>', rm.group(1), re.S | re.I)]
        if cells:
            rows.append(cells)
    if not rows:
        return ''
    width = max(len(r) for r in rows)
    rows = [r + [' '] * (width - len(r)) for r in rows]
    out = ['| ' + ' | '.join(r) + ' |' for r in rows]
    out.insert(1, '|' + ' --- |' * width)
    return '\n'.join(out)


def _cell(cell_html, slug):
    t = inline_to_md(cell_html, slug)
    return t.replace('|', '\\|') or ' '


def list_to_md(inner, ordered, slug, indent=0):
    out = []
    pad = ' ' * indent
    items = re.split(r'<li[^>]*>', inner, flags=re.I)[1:]
    for idx, it in enumerate(items, 1):
        it = re.sub(r'</li>\s*$', '', it.strip(), flags=re.I)
        sub = ''
        sm = re.search(r'(<ul[^>]*>.*</ul>|<ol[^>]*>.*</ol>)\s*$', it, re.S | re.I)
        if sm:
            sub_html = sm.group(1)
            it = it[:sm.start()]
            sub_o = sub_html.lower().startswith('<ol')
            sub = '\n' + list_to_md(re.sub(r'^<(ul|ol)[^>]*>|</(ul|ol)>\s*$', '', sub_html,
                                           count=1, flags=re.I),
                                    sub_o, slug, indent + 2)
        marker = ('%d. ' % idx) if ordered else '- '
        out.append(('%s%s%s' % (pad, marker, inline_to_md(it, slug))) + sub)
    return '\n'.join(out)


def figure_to_md(inner, slug):
    out = []
    im = re.search(r'<img[^>]*\ssrc="([^"]+)"[^>]*>', inner, re.I)
    if im:
        src = im.group(1)
        if not src.startswith(('http', '/', '../')):
            alt = re.search(r'alt="([^"]*)"', im.group(0))
            out.append('![%s](../../en/%s/%s)' % ((alt.group(1) if alt else ''), slug, src))
    fl = re.search(r'<span class="figlabel">(.*?)</span>', inner, re.S | re.I)
    if fl:
        cap = inline_to_md(fl.group(1), slug)
        if cap:
            out.append('*%s*' % cap)
    return '\n\n'.join(out)


# ------------------------------------------------------------ block loop ----

class Ctx:
    def __init__(self, slug):
        self.slug = slug
        self.out = []
        self.in_bib = False
        self.bib_lvl = 0
        self.bib_entries = []

    def emit(self, *lines):
        self.out.extend(lines)


def render_blocks(blocks, ctx):
    for b in blocks:
        t, inner = b['type'], b['inner']
        if t == 'h1':
            ctx.emit('# ' + inline_to_md(inner, ctx.slug))
        elif t in ('h2', 'h3', 'h4'):
            text = inline_to_md(inner, ctx.slug)
            hashes = '#' * {'h2': 2, 'h3': 3, 'h4': 4}[t]
            if re.fullmatch(r'(?:references|bibliography)', text, re.I):
                ctx.in_bib = True
                ctx.bib_lvl = {'h2': 2, 'h3': 3, 'h4': 4}[t]
                ctx.emit('', '%s References（引用注释）' % hashes, '',
                         '> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，'
                         '完整条目见本文末脚注定义。')
            else:
                # 文献节后的任何同级/更高级标题都终止文献节
                # （演示轮 2 复核：in_bib 永不复位曾吞掉致谢/相关词条等尾段）
                if not (ctx.in_bib and {'h2': 2, 'h3': 3, 'h4': 4}[t] > ctx.bib_lvl):
                    ctx.in_bib = False
                ctx.emit('', '%s %s' % (hashes, text))
        elif t == 'pubinfo':
            text = inline_to_md(inner, ctx.slug)
            if text:
                ctx.emit('*%s*' % text)
        elif t == 'preamble':
            # div#preamble 内是正文引言段落（演示轮 2 复核：v2 曾整段丢弃）
            render_blocks(extract_blocks_raw(inner), ctx)
        elif t == 'p':
            text = inline_to_md(inner, ctx.slug)
            if not text:
                continue
            if ctx.in_bib:
                ctx.bib_entries.append(text)
            else:
                ctx.emit('', text)
        elif t == 'blockquote':
            ctx.emit('')
            tm = re.search(r'<table[^>]*>.*?</table>', inner, re.S | re.I)
            rest = inner
            if tm:
                for ln in table_to_md(tm.group(0), ctx.slug).split('\n'):
                    ctx.emit('> ' + ln)
                rest = inner[:tm.start()] + inner[tm.end():]
            chunks = re.findall(r'<p[^>]*>(.*?)</p>', rest, re.S | re.I) or [rest]
            for ch in chunks:
                txt = inline_to_md(ch, ctx.slug)
                if txt:
                    ctx.emit('> ' + txt)
        elif t == 'table':
            ctx.emit('', table_to_md(inner, ctx.slug))
        elif t == 'figure':
            ctx.emit('', figure_to_md(inner, ctx.slug))
        elif t in ('ul', 'ol'):
            items = re.split(r'<li[^>]*>', inner, flags=re.I)[1:]
            texts = []
            for it in items:
                it = re.sub(r'</li>\s*$', '', it.strip(), flags=re.I)
                it = re.sub(r'<ul[^>]*>.*</ul>|<ol[^>]*>.*</ol>', '', it, flags=re.S | re.I)
                texts.append(inline_to_md(it, ctx.slug))
            if ctx.in_bib:
                ctx.bib_entries.extend(t for t in texts if t)
            else:
                ctx.emit('', list_to_md(re.sub(r'^<(ul|ol)[^>]*>|</(ul|ol)>\s*$', '', inner,
                                               count=1, flags=re.I),
                                        t == 'ol', ctx.slug))
        elif t == 'dl':
            for dm in re.finditer(r'<dt[^>]*>(.*?)</dt>|<dd[^>]*>(.*?)</dd>',
                                  inner, re.S | re.I):
                if dm.group(1) is not None:
                    ctx.emit('', '**%s**' % inline_to_md(dm.group(1), ctx.slug))
                else:
                    ctx.emit('', inline_to_md(dm.group(2), ctx.slug))
        elif t == 'pre':
            code = unescape(re.sub(r'<[^>]+>', '', inner))
            ctx.emit('', '```\n%s\n```' % code.strip('\n'))
        elif t == 'bib-container':
            # 容器内的 h2 Bibliography 自行置位 in_bib；无需强制
            render_blocks(extract_blocks_raw(inner), ctx)


# ------------------------------------------------------------ citations -----

def build_cite_keys(entry_texts):
    """文献条目 → [{key, pats, text}]。key 取 首作者姓-年份[后缀]，冲突加序号。"""
    keys = []
    prev_surnames = []
    seen = {}
    for raw in entry_texts:
        text = re.sub(r'\s+', ' ', raw or '').strip()
        if not text:
            continue
        continued = text.startswith('–––') or text.startswith('———')
        ym = re.search(r'\b(1[6-9]\d\d|20\d\d)([a-e]?)\b', text)
        if not ym:
            continue
        year, suffix = ym.group(1), ym.group(2)
        if continued:
            surnames = list(prev_surnames)
        else:
            toks = re.findall(r"[A-ZÀ-ÿ][\wÀ-ÿ'’\-]*\.?", text[:ym.start()])
            surnames = [t.rstrip('.') for t in toks
                        if not re.fullmatch(r"[A-ZÀ-ÿ]\.?", t)
                        and t.rstrip('.').lower() not in ('and', 'the', 'in', 'on', 'eds',
                                                          'ed', 'review', 'of')]
            if not surnames:
                surnames = list(prev_surnames)
            if not surnames:
                continue
        prev_surnames = surnames
        first = surnames[0]
        joined = ' '.join(surnames)
        acronym = ''.join(s[0] for s in surnames) if len(surnames) >= 2 else ''
        base = ('%s-%s%s' % (first, year, suffix)).lower()
        seen[base] = seen.get(base, 0) + 1
        key = base if seen[base] == 1 else '%s-%d' % (base, seen[base])
        pats = []
        for name in (joined, first, acronym):
            if name and len(name) >= 3:
                pats.append(re.compile(
                    re.escape(name) + r'[^,;()\[\]]{0,60}?\b' +
                    re.escape(year) + re.escape(suffix) + r'\b'))
        keys.append({'key': key, 'pats': pats, 'text': text})
    return keys


GROUP_RE = re.compile(r'\([^()]{0,300}?\)|(?<!\])\[[^()\[\]]{0,300}?\](?!\()')


def link_citations(md_text, keys):
    """文内引用组后追加 [^key]；返回 (新文本, 追加数, 命中 key 集)。"""
    used = set()
    count = [0]

    def _sub(m):
        group = m.group(0)
        hits = []
        for k in keys:
            if any(p.search(group) for p in k['pats']):
                hits.append(k['key'])
        if hits:
            count[0] += len(hits)
            used.update(hits)
            return group + ''.join('[^%s]' % h for h in hits)
        return group

    return GROUP_RE.sub(_sub, md_text), count[0], used


# ------------------------------------------------------------ notes/supp ----

def convert_notes(html, slug):
    """notes.html → [^note-n]: 文本 列表（顺带保留无编号说明段）。"""
    m, e = parser.HEAD_RE.search(html), parser.TAIL_RE.search(html)
    article = html[m.end():e.start()] if (m and e) else html
    defs = []
    for b in extract_blocks_raw(article):
        if b['type'] != 'p':
            continue
        inner = b['inner']
        nm = re.match(r'\s*<a href="index\.html#note-(\d+)"[^>]*>\s*\d+\.\s*</a>',
                      inner, re.I)
        if nm:
            defs.append('[^note-%s]: %s' % (nm.group(1), inline_to_md(inner[nm.end():], slug)))
        else:
            txt = inline_to_md(inner, slug)
            if txt:
                defs.append(txt)
    return defs


def convert_supplement(html, slug, base):
    ctx = Ctx(slug)
    render_blocks(extract_blocks_raw(html), ctx)
    text = '\n'.join(ctx.out).strip() + '\n'
    header = '# %s — %s（supplement）\n\n> （《%s》词条补充材料，源：plato.stanford.edu/entries/%s/%s.html）\n\n' % (
        slug, base, slug, slug, base)
    return header + text


# --------------------------------------------------------------- convert ----

def update_baseline(slug, patch):
    path = repo_path('baseline', 'entries.json')
    base = load_json(path)
    for rec in base['entries']:
        if rec['slug'] == slug:
            rec.update(patch)
            break
    base['updated_at'] = utcnow_iso()
    write_json_verified(path, base)


def convert_entry(slug):
    src_dir = repo_path('en', slug)
    idx_path = os.path.join(src_dir, 'index.html')
    if not os.path.exists(idx_path):
        return {'slug': slug, 'error': 'no local snapshot（先 fetch_entry）'}
    html = read_text(idx_path)
    m, e = parser.HEAD_RE.search(html), parser.TAIL_RE.search(html)
    article = html[m.end():e.start()] if (m and e) else html
    tm = re.search(r'<meta name="citation_title" content="([^"]*)"', html)
    authors = [unescape(a) for a in
               re.findall(r'<meta name="citation_author" content="([^"]*)"', html)]

    letter = slug[0]
    ydir = repo_path('yuanwen', letter)
    os.makedirs(ydir, exist_ok=True)

    ctx = Ctx(slug)
    render_blocks(extract_blocks_raw(article), ctx)
    md = '\n'.join(ctx.out).strip()
    if not md.startswith('# '):
        title = unescape(tm.group(1)) if tm else slug
        md = '# %s\n\n%s' % (title, md)
    if authors:
        md = md.replace('\n\n', '\n\n*%s*\n\n' % ', '.join(authors), 1)

    # 脚注（notes.html）
    note_defs = []
    notes_path = os.path.join(src_dir, 'notes.html')
    if os.path.exists(notes_path):
        note_defs = [d for d in convert_notes(read_text(notes_path), slug)
                     if d.startswith('[^note-')]
        if note_defs:
            md += '\n\n## Notes（原文脚注）\n\n' + '\n\n'.join(note_defs)

    # 补充材料
    supp_files = []
    for f in sorted(os.listdir(src_dir)):
        if f.endswith('.html') and f not in ('index.html', 'notes.html'):
            base = f[:-5]
            sp = convert_supplement(read_text(os.path.join(src_dir, f)), slug, base)
            sp_path = os.path.join(ydir, '%s.%s.md' % (slug, base))
            write_text_verified(sp_path, sp)
            supp_files.append('%s.%s.md' % (slug, base))

    # 引用注释（文献 → 脚注）
    keys = build_cite_keys(ctx.bib_entries)
    cite_markers, cite_defs = 0, 0
    if keys:
        md, cite_markers, _used = link_citations(md, keys)
        md += '\n\n' + '\n\n'.join('[^%s]: %s' % (k['key'], k['text']) for k in keys)
        cite_defs = len(keys)

    md_path = os.path.join(ydir, slug + '.md')
    write_text_verified(md_path, md + '\n')
    if not os.path.exists(md_path):
        raise OSError('yuanwen write failed: %s' % md_path)

    update_baseline(slug, {'yuanwen': {
        'md': 'yuanwen/%s/%s.md' % (letter, slug),
        'sha256': sha256_file(md_path),
        'source_sha256': sha256_file(idx_path),
        'converted_at': utcnow_iso(),
        'cite_markers': cite_markers,
        'cite_defs': cite_defs,
        'supplements': supp_files,
        'notes': len(note_defs),
    }})
    return {'slug': slug, 'md': 'yuanwen/%s/%s.md' % (letter, slug),
            'cite_markers': cite_markers, 'cite_defs': cite_defs,
            'supplements': supp_files, 'notes': len(note_defs)}


def write_summary():
    """镜像根 SUMMARY.md → yuanwen/SUMMARY.md：已转换条目改链 yuanwen 路径。"""
    base = load_json(repo_path('baseline', 'entries.json'))
    zh2yuan = {}
    for rec in base['entries']:
        y = rec.get('yuanwen')
        zh = rec.get('zh_doc') or (find_zh_doc(rec['slug'], rec.get('title'))
                                   if y else None)
        if y and zh:
            zh2yuan[zh] = y['md']
    src = read_text(repo_path('SUMMARY.md'))
    n = [0]

    def repl(m):
        target = m.group(1)
        if target in zh2yuan:
            n[0] += 1
            return '](%s)' % zh2yuan[target]
        return m.group(0)

    out = re.sub(r'\]\(([^)]+\.md)\)', repl, src)
    write_text_verified(repo_path('yuanwen', 'SUMMARY.md'), out)
    return n[0]


# ------------------------------------------------------------------ main ----

def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    do_summary = '--summary' in argv
    argv = [a for a in argv if not a.startswith('--')]
    if '--all-baselined' in sys.argv[1:]:
        base = load_json(repo_path('baseline', 'entries.json'))
        argv = [r['slug'] for r in base['entries']]
    if not argv and not do_summary:
        print(json.dumps({'error': '用法: python tools/yuanwen.py <slug>... | '
                                   '--all-baselined [--summary]'}, ensure_ascii=False))
        return 2
    converted, failures = [], []
    for slug in argv:
        sys.stderr.write('[yuanwen] %s ...\n' % slug)
        try:
            converted.append(convert_entry(slug))
        except Exception as exc:
            failures.append({'slug': slug, 'error': repr(exc)})
    summary_n = write_summary() if do_summary else None
    print(json.dumps({'converted': converted, 'failures': failures,
                      'summary_links_rewritten': summary_n},
                     ensure_ascii=False, indent=2))
    return 1 if failures else 0


if __name__ == '__main__':
    sys.exit(main())
