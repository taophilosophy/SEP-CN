# -*- coding: utf-8 -*-
"""原文 Markdown 镜像生成器（yuanwen/）——用户 2026-10-27 裁定。

把 en/<slug>/index.html（不可变原始抓取物）确定性转换为 yuanwen/<letter>/<slug>.md：
- 结构与中文仓库逐字符镜像（ADR-0009 A–Z 字母目录）：yuanwen/<letter>/<slug>.md，letter=slug 首字符
- 抓取的原始 HTML 一律存 en/<slug>/（不可变原始物，不入库）；yuanwen/ 只存转换后的 md 镜像
- 脚注：正文 <sup>[<a href="notes.html#n">n</a>]</sup> → [^note-n]；notes.html → 文末脚注定义
  （定义名取注段自身锚点 id，即 <div id="note-N"> 的 N——旧实现取回链目标
  index.html#ref-N，与正文引用 notes.html#note-N 错位，D14）
- 补充材料：en/<slug>/<x>.html → yuanwen/<letter>/<slug>.<x>.md（点号命名），正文内相对互链
- 图片：本地化为 yuanwen/assets/<slug>/（上游同名 imageN.jpg，用户 2026-10-27 裁定复制而非外链），
  正文 <img> 一律接线为 ![](../assets/<slug>/<文件名>)——md 位于 <letter>/ 子目录，
  相对引用须跨一级（ADR-0010 修正根级时代的 assets/ 写法，D15）
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
    r'<sup>\s*\[?\s*<a\s+href="notes\.html#(?P<ref>[A-Za-z0-9_-]+)"[^>]*>\s*\d*\s*</a>\s*\]?\s*</sup>', re.I)
SPECIAL_DIV_RE = re.compile(r'pubinfo|preamble|figure|bibliography', re.I)
SKIP_DIV_RE = re.compile(r'\btoc\b', re.I)
CROSS_MATH_RE = re.compile(r'(\\\[.*?\\\]|\\\(.*?\\\))', re.S)
CROSS_BLOCK_TAG_RE = re.compile(
    r'</?(?:p|div|table|ul|ol|blockquote|h[1-6]|dl|pre)\b', re.I)
# p 的隐式闭合边界（D16）：闭标签 / 列表与引用容器边界 / 下一块级开标签
IMPLIED_END_RE = re.compile(
    r'</p\s*>|</li\s*>|</blockquote\s*>|<(?:p|div|ul|ol|dl|table|blockquote|pre|h[1-6])\b',
    re.I)
# HTML 标签形态（浏览器一致语义）：<name 后随空白/></；<y 是数学比较不是标签
TAGLIKE_RE = re.compile(r'</?[a-zA-Z][a-zA-Z0-9]*(?:[\s/>]|$)')
# SEP 用 <!--pdf include <table>…--> / <!--pdf exclude begin--> 注释开关
# 切换 PDF/HTML 两版内容；正确闭合的注释须在切块前剥除，否则切分器会把
# 注释里的标签当真块（编辑性注释政策一贯为丢弃）
COMMENT_RE = re.compile(r'<!--.*?-->', re.S)


def strip_closed_comments(region):
    return COMMENT_RE.sub('', region)


def protect_cross_block_math(region):
    r"""区域级跨块公式保护（2026-10-27 数学保真裁定）。

    横跨块级标签的 \(…\)/\[…\] 公式在按块切分时被腰斩，两侧都无法配对。
    含块级标签的公式整体换成占位标记（切块、行内转换对标记透明），
    最终在 md 层还原为 $$/…$ 定界形式。返回 (region', {标记: 内部内容})。

    护栏（2026-10-28 D16）：仅当跨度像公式——无标题标签、块级开标签 ≤2、
    长度 ≤4000——才保护；typelogical-grammar 存在上游未配对的 \(，非贪婪
    匹配曾把 40KB 正文整段当公式吞进占位符，标题/列表全部失联。
    """
    stash = {}

    def _repl(m):
        inner = m.group(1)
        if not CROSS_BLOCK_TAG_RE.search(inner):
            return m.group(0)
        if (re.search(r'<h[1-6]\b', inner, re.I)
                or len(re.findall(r'<(?:p|div|ul|ol|li|table|blockquote|dl|pre)\b',
                                  inner, re.I)) > 2
                or len(inner) > 4000):
            return m.group(0)  # 跨度过大/含标题：是未配对定界符，不保护
        key = '\x00M%d\x00' % len(stash)
        stash[key] = inner
        return key

    return CROSS_MATH_RE.sub(_repl, region), stash


def restore_cross_block_math(text, stash):
    for key, inner in stash.items():
        v = re.sub(r'[ \t\r\n\f\v]+', ' ', unescape(inner)).strip()
        if v.startswith('\\(') and v.endswith('\\)'):
            v = '$' + v[2:-2] + '$'
        elif v.startswith('\\[') and v.endswith('\\]'):
            v = '$$' + v[2:-2] + '$$'
        text = text.replace(key, v)
    return text


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
    """返回与 start 处开标签配对的闭标签结束位置；找不到返回 len(html)。

    p 是非嵌套标签（HTML 隐式闭合语义）：遇到 </p>、</li>、</blockquote>
    或下一个块级开标签即视为闭合。上游源 html 常漏写 </p>，深度配对永不归零
    会把余下全文吞成一个块（aquinas §2–13、set-theory §4 等 19 件吞章，
    2026-10-28 全量复核 D16）。
    """
    if tag.lower() == 'p':
        m = IMPLIED_END_RE.search(html, start)
        return m.start() if m else len(html)
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
            # 无更多块标签：剩余纯文本（无 <p> 包装的引文、块尾残余）不得丢弃
            if html[i:].strip():
                blocks.append({'type': 'p', 'attrs': '', 'inner': html[i:]})
            break
        gap = html[i:m.start()]
        if gap.strip():
            # 块间裸文本：SEP 的展示公式 \[…\] 常不带 <p> 标签（演示轮 2 复核发现）
            blocks.append({'type': 'p', 'attrs': '', 'inner': gap})
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
        cm = re.match(r'</%s[^>]*>\s*' % tag, html[end:], re.I)
        if cm:
            end = end + cm.end()   # p 走隐式闭合时 end 停在闭标签起点，此处消费掉
        inner = re.sub(r'</%s>\s*$' % tag, '', inner, flags=re.I)
        blocks.append({'type': tag, 'attrs': attrs, 'inner': inner})
        i = end
    return blocks


# ---------------------------------------------------------------- inline ----

# 用户 2026-10-28 裁定：上下标优先用 Unicode 原生字符（数字、常见小写字母、
# ±=() 与希腊部分有原生字形），整体不可映射时保持 _{…}/^{…} 纯文本记号。
# 大写仅上标有原生字形；q 无任何形态；全角负号 − 与半角 - 同映射。
SUP_MAP = {
    '0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴', '5': '⁵', '6': '⁶',
    '7': '⁷', '8': '⁸', '9': '⁹', '+': '⁺', '-': '⁻', '−': '⁻', '=': '⁼',
    '(': '⁽', ')': '⁾', 'n': 'ⁿ', 'i': 'ⁱ',
    'a': 'ᵃ', 'b': 'ᵇ', 'c': 'ᶜ', 'd': 'ᵈ', 'e': 'ᵉ', 'f': 'ᶠ', 'g': 'ᵍ',
    'h': 'ʰ', 'j': 'ʲ', 'k': 'ᵏ', 'l': 'ˡ', 'm': 'ᵐ', 'o': 'ᵒ', 'p': 'ᵖ',
    'r': 'ʳ', 's': 'ˢ', 't': 'ᵗ', 'u': 'ᵘ', 'v': 'ᵛ', 'w': 'ʷ', 'x': 'ˣ',
    'y': 'ʸ', 'z': 'ᶻ',
    'A': 'ᴬ', 'B': 'ᴮ', 'D': 'ᴰ', 'E': 'ᴱ', 'G': 'ᴳ', 'H': 'ᴴ', 'I': 'ᴵ',
    'J': 'ᴶ', 'K': 'ᴷ', 'L': 'ᴸ', 'M': 'ᴹ', 'N': 'ᴺ', 'O': 'ᴼ', 'P': 'ᴾ',
    'R': 'ᴿ', 'T': 'ᵀ', 'U': 'ᵁ', 'V': 'ⱽ', 'W': 'ᵂ',
    'α': 'ᵅ', 'β': 'ᵝ', 'γ': 'ᵞ', 'δ': 'ᵟ', 'ε': 'ᵋ', 'θ': 'ᶿ',
    'ι': 'ᶥ', 'φ': 'ᶲ', 'π': 'ᵠ',
}
SUB_MAP = {
    '0': '₀', '1': '₁', '2': '₂', '3': '₃', '4': '₄', '5': '₅', '6': '₆',
    '7': '₇', '8': '₈', '9': '₉', '+': '₊', '-': '₋', '−': '₋', '=': '₌',
    '(': '₍', ')': '₎',
    'a': 'ₐ', 'e': 'ₑ', 'h': 'ₕ', 'i': 'ᵢ', 'j': 'ⱼ', 'k': 'ₖ', 'l': 'ₗ',
    'm': 'ₘ', 'n': 'ₙ', 'o': 'ₒ', 'p': 'ₚ', 'r': 'ᵣ', 's': 'ₛ', 't': 'ₜ',
    'u': 'ᵤ', 'v': 'ᵥ', 'x': 'ₓ',
    'β': 'ᵦ', 'γ': 'ᵧ', 'ρ': 'ᵨ', 'φ': 'ᵩ', 'χ': 'ᵪ',
}


def _subsup_md(inner, mapping, marker):
    """<sub>/<sup> 内容整体可映射 → Unicode 原生字符；否则保持纯文本记号。

    内容含标签/强调（如 <sub><i>x</i></sub>）或无原生字形的字符时不可映射，
    维持 _{…}/^{…} 交由站点渲染层处理（2026-10-28 裁定）。"""
    if inner and all(ch in mapping for ch in inner):
        return ''.join(mapping[ch] for ch in inner)
    return marker % inner


def inline_to_md(html, slug=None):
    """行内 HTML → Markdown 文本。数学与 sub/sup 占位保护后原样还原。"""
    if not html:
        return ''
    s = re.sub(r'<!--.*?-->', '', html, flags=re.S)
    def _noteref(m):
        ref = re.sub('^note-', '', m.group('ref'))
        return '[^note-%s]' % ref
    s = NOTE_REF_RE.sub(_noteref, s)
    # 用户 2026-10-27 指令：禁止 HTML 标签，保持洁净——sub/sup 一律转纯文本；
    # 2026-10-28 裁定升级：有原生 Unicode 字形直接用原生字符，否则保持
    # 下标 _{x}、上标 ^{x} 记号（站点渲染层兜底），不再保留 <sub>/<sup> 标签
    s = re.sub(r'<sub>(.*?)</sub>', lambda m: _subsup_md(m.group(1), SUB_MAP, '_{%s}'), s, flags=re.S | re.I)
    s = re.sub(r'<sup>(.*?)</sup>', lambda m: _subsup_md(m.group(1), SUP_MAP, '^{%s}'), s, flags=re.S | re.I)
    store = []

    def _stash(m):
        # 护栏（D16）：真实公式不含原始 HTML 标签（源中真 < 一律写作 &lt;，
        # 裸 < 按浏览器语义即标签）。含标签的 \(…\) 是未配对定界符
        # （如 typelogical-grammar 的 40KB 吞段），按普通文本走标签管线。
        if TAGLIKE_RE.search(m.group(0)):
            return m.group(0)
        store.append(m.group(0))
        return '\x00%d\x00' % (len(store) - 1)

    s = MATH_RE.sub(_stash, s)

    def _link(m):
        href = (m.group('href') or '').strip()
        text = m.group('t')
        if href.startswith('#') or href == 'index.html' or href.startswith('index.html#'):
            return text
        if href.startswith('notes.html#'):
            ref = re.sub('^note-', '', href.split('#')[1].split('&')[0])
            return '[^note-%s]' % ref
        if slug and re.fullmatch(r'[A-Za-z0-9._%+-]+\.(?:png|jpe?g|gif|svg|webp|pdf)', href):
            # 点图放大链（<a href="X-large.gif"> 包 <img src="X.gif">）：本地化引用，
            # 否则大图资产成为无引用孤儿（2026-10-28 复核）
            return '[%s](../assets/%s/%s)' % (text, slug, href)
        if re.fullmatch(r'[a-zA-Z0-9][a-zA-Z0-9._-]*\.html', href) and slug:
            base = href[:-5]
            return '[%s](%s.%s.md)' % (text, slug, base)
        if href.startswith(('http:', 'https:')):
            return '[%s](%s)' % (text, href)
        return text

    s = re.sub(r'<a\b[^>]*href="(?P<href>[^"]*)"[^>]*>(?P<t>.*?)</a>',
               _link, s, flags=re.S | re.I)
    # 2026-10-30：三处 (.*?) re.S 会在 strong/b 交错时跨标签吞段、且 em 先行
    # 转出的内层星与外层 ** 组成三连星边界错乱（149 镜像文件 667 对星内空格
    # 的根因，实测）——改 [^<]* 限单层；粗体内容含星（内层 em 转出）时降级
    # <b> 保结构稳定。<b>（数学记号粗体，如 <b>P</b>(<em>H</em>)）保留 raw
    # HTML 不转 md 星：与 <em>/字面星交错会产生星流奇偶错位并连锁整段
    def _md_bold(m):
        inner = m.group(1)
        return ('<b>%s</b>' % inner) if '*' in inner else ('**%s**' % inner)

    s = re.sub(r'<(?:em|i)>([^<]*)</(?:em|i)>', r'*\1*', s, flags=re.I)
    s = re.sub(r'<strong>([^<]*)</strong>', _md_bold, s, flags=re.I)
    s = re.sub(r'<code>([^<]*)</code>', r'`\1`', s, flags=re.S | re.I)
    s = re.sub(r'<br\s*/?>', ' ', s, flags=re.I)
    s = re.sub(r'</?span[^>]*>', '', s, flags=re.I)

    def _img(m):
        tag = m.group(0)
        sm = re.search(r'\ssrc="([^"]*)"', tag)
        if not sm:
            return ''
        src = unescape(sm.group(1)).strip()
        am = re.search(r'\salt="([^"]*)"', tag)
        alt = unescape(am.group(1)) if am else ''
        # ADR-0008 上游同名本地化 + ADR-0010 相对引用 ../assets/<slug>/（md 在
        # <letter>/ 子目录）；旧实现一律剥除 <img>，正文图片全部失联（D15）
        if slug and re.fullmatch(r'[A-Za-z0-9._%+-]+', src):
            return '![%s](../assets/%s/%s)' % (alt, slug, src)
        if src.startswith(('http://', 'https://')):
            return '![%s](%s)' % (alt, src)
        return ''

    s = re.sub(r'<img[^>]*>', _img, s, flags=re.I)
    s = re.sub(r'<[^>]+>', '', s)
    s = unescape(s)
    s = re.sub(r'[ \t\r\n\f\v]+', ' ', s).strip()
    for idx, val in enumerate(store):
        # 恢复的数学内容：实体解码 + 定界符统一为 LaTeX（$…$ / $$…$$）；
        # sub/sup 已在占位前转纯文本。内部空白折叠为单空格（LaTeX 语义
        # 不依赖空白；保留源换行会让 md 行内 $ 计数失衡），其余字符原样
        v = re.sub(r'[ \t\r\n\f\v]+', ' ', unescape(val)).strip()
        if v.startswith('\\(') and v.endswith('\\)'):
            v = '$' + v[2:-2] + '$'
        elif v.startswith('\\[') and v.endswith('\\]'):
            v = '$$' + v[2:-2] + '$$'
        s = s.replace('\x00%d\x00' % idx, v)
    return s


NESTED_TABLE_RE = re.compile(r'<table[^>]*>.*?</table>', re.S | re.I)


def _flatten_nested_tables(html, slug, depth=0):
    """最内层优先，把嵌套表展平为单元格内文本（markdown 不支持嵌套表；
    非贪婪的 td 匹配会被内层 </td> 截断导致外层单元格内容丢失）。"""
    if depth > 4:
        return html
    while True:
        best = None
        for m in NESTED_TABLE_RE.finditer(html):
            if '<table' not in m.group(0)[6:]:
                best = m
                break
        if best is None:
            return html
        flat = table_to_md(best.group(0), slug, depth + 1).replace('\n', ' ')
        html = html[:best.start()] + '（嵌套表：' + flat + '）' + html[best.end():]


def table_to_md(inner, slug, depth=0):
    if depth == 0:
        inner = _flatten_nested_tables(inner, slug)
    cap = ''
    cm = re.search(r'<caption[^>]*>(.*?)</caption>', inner, re.S | re.I)
    if cm:
        # 表题（caption）是表格语义的一部分，丢弃即丢其中的公式/文字
        # （epistemic-game 表题 \(\lambda_A(a_1)\)，2026-10-28 复核）
        cap = inline_to_md(cm.group(1), slug)
        inner = inner[:cm.start()] + inner[cm.end():]
    rows = []
    for rm in re.finditer(r'<tr[^>]*>(.*?)</tr>', inner, re.S | re.I):
        cells = [_cell(c, slug)
                 for c in re.findall(r'<t[dh][^>]*>(.*?)</t[dh]>', rm.group(1), re.S | re.I)]
        if cells:
            rows.append(cells)
    if not rows:
        return cap
    width = max(len(r) for r in rows)
    rows = [r + [' '] * (width - len(r)) for r in rows]
    out = ['| ' + ' | '.join(r) + ' |' for r in rows]
    out.insert(1, '|' + ' --- |' * width)
    table = '\n'.join(out)
    return ('*%s*\n\n' % cap + table) if cap else table


def _cell(cell_html, slug):
    t = inline_to_md(cell_html, slug)
    # 表格竖线转义只作用于数学之外；数学内容里的 | 若被转成 \| 会改语义
    # （LaTeX \| = ‖），故数学段内的 | 用 &#124; 实体保真（渲染时还原为 |）
    parts = re.split(r'(\$\$.*?\$\$|\$[^$\n]*\$)', t, flags=re.S)
    out = []
    for i, p in enumerate(parts):
        if i % 2:  # 数学段
            out.append(p.replace('|', '&#124;'))
        else:
            out.append(p.replace('|', '\\|'))
    t = ''.join(out)
    return t or ' '


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
    fl = re.search(r'<span class="figlabel">(.*?)</span>', inner, re.S | re.I)
    if fl:
        cap = inline_to_md(fl.group(1), slug)
        if cap:
            out.append('*%s*' % cap)
    # 图注与其余内容不再丢弃（2026-10-27 数学保真裁定：SEP 常把表格、公式
    # 段落整个包进 <div class="figure">）；图片统一由 inline_to_md 接线
    # （2026-10-28 D15：不再单独挑首图、不再剥除其余 <img>）
    sub = Ctx(slug)
    render_blocks(extract_blocks_raw(inner), sub)
    body = '\n'.join(sub.out).strip()
    if body:
        out.append(body)
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
            # 引文块内完整渲染（2026-10-27 数学保真裁定）：旧实现只挑 <p>，
            # 会丢引文中的裸展示公式（p 间 gap）与无 <p> 包装的列表项
            sub = Ctx(ctx.slug)
            render_blocks(extract_blocks_raw(inner), sub)
            body = '\n'.join(sub.out).strip()
            if body:
                ctx.emit('')
                for ln in body.split('\n'):
                    ctx.emit('> ' + ln if ln.strip() else '>')
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
                    # 2026-10-30：dt 内容首尾常带空格/内含星号，无条件 `**%s**`
                    # 会产生星内空格（永不渲染）或跨距配对——strip 后仅对无星内容加粗
                    dtext = inline_to_md(dm.group(1), ctx.slug).strip()
                    ctx.emit('', '**%s**' % dtext if dtext and '*' not in dtext else dtext)
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
        year, suffix = (ym.group(1), ym.group(2)) if ym else (None, '')
        if continued:
            surnames = list(prev_surnames)
            if not surnames:
                # 文献表以续行（———）开头且无前条可继承：跳过该条
                continue
        else:
            # 无年份条目（如版本卷次引用）：作者名在条目头部，
            # 取前 120 字符做姓氏扫描——此类条目不得整条丢弃
            scan_to = ym.start() if ym else min(len(text), 120)
            toks = re.findall(r"[A-ZÀ-ÿ][\wÀ-ÿ'’\-]*\.?", text[:scan_to])
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
        # 无年份条目用 -nd 键；不生成文内标记 pats，但定义行必须保留，
        # 否则整条文献（含其中公式）从产物消失
        base = ('%s-%s%s' % (first, year or 'nd', suffix)).lower()
        seen[base] = seen.get(base, 0) + 1
        key = base if seen[base] == 1 else '%s-%d' % (base, seen[base])
        pats = []
        if ym:
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

NOTE_ANCHOR_RE = re.compile(
    r'<(?:a|div|p|li|dt|dd)\b[^>]*\bid="(note-[A-Za-z0-9_-]+)"[^>]*>', re.I)
BACKLINK_RE = re.compile(
    r'<a\b[^>]*\bhref="index\.html#[^"]*"[^>]*>\s*(?:\d+\.?|\^)?\s*</a>', re.I | re.S)


def _render_note_inner(inner, slug):
    """注段 div 内块 → md 文本；去掉段首回链标记（^ / 1.，旧实现同样不保留）。"""
    inner = BACKLINK_RE.sub('', inner, count=1)
    sub = Ctx(slug)
    render_blocks(extract_blocks_raw(inner), sub)
    return '\n'.join(sub.out).strip()


def _notes_gap_defs(gap, slug):
    """注段间隙的裸内容（无 div 包裹的公式段、dl 公理列表等）原样转出。"""
    out = []
    for b in extract_blocks_raw(gap):
        if b['type'] == 'p':
            txt = inline_to_md(b['inner'], slug)
            if txt:
                out.append(txt)
        else:
            sub = Ctx(slug)
            render_blocks([b], sub)
            body = '\n'.join(sub.out).strip()
            if body:
                out.append(body)
    return out


def convert_notes(html, slug):
    """notes.html → [^note-n]: 文本 列表。

    注段按 id="note-N" 锚点切段（锚点可能在包裹 div 上，如 tarski，也可能
    直接钉在回链 <a> 上，如 common-knowledge）——定义名一律取锚点 id。旧实现
    取回链目标 index.html#ref-N，与正文引用 notes.html#note-N 错位，646 文件
    3931 引用悬空（2026-10-28 全量复核 D14）。锚点间隙的裸内容（<dl> 公理
    列表、表格、无 <p> 包装的展示公式等）一律完整保留（2026-10-27 数学保真
    裁定，不得过滤）。
    """
    m, e = parser.HEAD_RE.search(html), parser.TAIL_RE.search(html)
    article = html[m.end():e.start()] if (m and e) else html
    article = strip_closed_comments(article)
    article, stash = protect_cross_block_math(article)
    defs = []
    marks = [(mm.start(), mm.group(1)) for mm in NOTE_ANCHOR_RE.finditer(article)]
    if marks:
        pos = 0
        for j, (start, key) in enumerate(marks):
            end = marks[j + 1][0] if j + 1 < len(marks) else len(article)
            if start < pos:
                continue  # 异常嵌套防串段
            gap = article[pos:start]
            if gap.strip():
                defs.extend(_notes_gap_defs(gap, slug))
            body = _render_note_inner(article[start:end], slug)
            if body:
                defs.append('[^note-%s]: %s' % (re.sub('^note-', '', key), body))
            pos = end
        if article[pos:].strip():
            defs.extend(_notes_gap_defs(article[pos:], slug))
    else:
        # 无 div 包裹的旧版式：p 内锚点 id 优先，回链目标兜底
        for b in extract_blocks_raw(article):
            if b['type'] == 'p':
                inner = b['inner']
                idm = re.search(r'\bid="(note-[A-Za-z0-9_-]+)"', inner, re.I)
                nm = re.match(r'\s*<a href="index\.html#(?:note-)?([A-Za-z0-9_-]+)"[^>]*>\s*\d*\.?\s*</a>',
                              inner, re.I)
                if idm:
                    body = inline_to_md(BACKLINK_RE.sub('', inner, count=1), slug)
                    if body:
                        defs.append('[^note-%s]: %s'
                                    % (re.sub('^note-', '', idm.group(1)), body))
                elif nm:
                    defs.append('[^note-%s]: %s'
                                % (re.sub('^note-', '', nm.group(1)),
                                   inline_to_md(inner[nm.end():], slug)))
                else:
                    txt = inline_to_md(inner, slug)
                    if txt:
                        defs.append(txt)
            else:
                sub = Ctx(slug)
                render_blocks([b], sub)
                body = '\n'.join(sub.out).strip()
                if body:
                    defs.append(body)
    return [restore_cross_block_math(d, stash) for d in defs]


def convert_supplement(html, slug, base):
    m, e = parser.HEAD_RE.search(html), parser.TAIL_RE.search(html)
    article = html[m.end():e.start()] if (m and e) else html
    ctx = Ctx(slug)
    article = strip_closed_comments(article)
    article, stash = protect_cross_block_math(article)
    render_blocks(extract_blocks_raw(article), ctx)
    text = restore_cross_block_math('\n'.join(ctx.out).strip() + '\n', stash)
    header = '# %s — %s（supplement）\n\n> （《%s》词条补充材料，源：plato.stanford.edu/entries/%s/%s.html）\n\n' % (
        slug, base, slug, slug, base)
    return header + text


# --------------------------------------------------------------- convert ----

def update_baseline(slug, patch):
    from tools.common import BASELINE_LOCK
    path = repo_path('baseline', 'entries.json')
    with BASELINE_LOCK:
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
    article = strip_closed_comments(article)
    article, stash = protect_cross_block_math(article)
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
        # 不得过滤非 [^note- 行：notes.html 里裸公式段与"where…"接续段
        # 是原文内容（2026-10-27 数学保真裁定），过滤即丢公式
        note_defs = convert_notes(read_text(notes_path), slug)
        if note_defs:
            md += '\n\n## Notes（原文脚注）\n\n' + '\n\n'.join(note_defs)

    # 图片本地化（用户 2026-10-27 裁定复制而非外链；ADR-0008 上游同名，存
    # yuanwen/assets/<slug>/）。仅复制图片类资产：local.js 等站点脚本不被
    # md 引用（2026-10-28 D15 复核），历史误复制的一并清除。
    adir = repo_path('yuanwen', 'assets', slug)
    image_exts = ('.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp', '.pdf')
    image_files = []
    for f in sorted(os.listdir(src_dir)):
        src_f = os.path.join(src_dir, f)
        if f.endswith('.html') or os.path.isdir(src_f):
            continue
        os.makedirs(adir, exist_ok=True)
        dst_f = os.path.join(adir, f)
        if not f.lower().endswith(image_exts):
            if os.path.exists(dst_f):
                os.remove(dst_f)
            continue
        data = open(src_f, 'rb').read()
        with open(dst_f, 'wb') as fh:
            fh.write(data)
        image_files.append('yuanwen/assets/%s/%s' % (slug, f))

    # 补充材料
    supp_files = []
    for f in sorted(os.listdir(src_dir)):
        if f.endswith('.html') and f not in ('index.html', 'notes.html'):
            base = f[:-5]
            sp = convert_supplement(read_text(os.path.join(src_dir, f)), slug, base)
            if note_defs and '[^note-' in sp:
                # 补充材料引用主文脚注：定义随被引条目附于文末，页内自洽
                # （2026-10-28 复核：46 文件引用悬空，D14 伴生缺陷）
                need = list(dict.fromkeys(
                    re.findall(r'\[\^(note-[^\]\s]+)\](?!:)', sp)))
                defmap = {}
                for d in note_defs:
                    dm = re.match(r'\[\^(note-[^\]]+)\]:', d)
                    if dm:
                        defmap.setdefault(dm.group(1), d)
                extra = [defmap[n] for n in need if n in defmap]
                if extra:
                    sp += ('\n\n## Notes（原文脚注，引自主文）\n\n'
                           + '\n\n'.join(extra))
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

    md = restore_cross_block_math(md, stash)

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
        'images': image_files,
        'notes': len(note_defs),
    }})
    return {'slug': slug, 'md': 'yuanwen/%s/%s.md' % (letter, slug),
            'cite_markers': cite_markers, 'cite_defs': cite_defs,
            'supplements': supp_files, 'notes': len(note_defs)}


def write_summary():
    """镜像根 SUMMARY.md → yuanwen/SUMMARY.md。

    条目链接（<letter>/<slug>.md）两侧相对路径逐字符一致，原样拷贝；
    zh 侧导航行（README.md、mu-lu-s.md、qian-yan/*、guan-yu/*）在 yuanwen/
    下无镜像对应文件，改写为 ../ 前缀使其自 yuanwen/ 可解析
    （specs/007-review-campaign 审阅实证 167 处断链，2026-10-28）。
    """
    src = read_text(repo_path('SUMMARY.md'))
    out = []
    for line in src.split('\n'):
        if '](../' in line:
            out.append(line)
            continue

        def _rw(m):
            target, frag = m.group(1), m.group(2) or ''
            if re.match(r'^(https?:|mailto:)', target):
                return m.group(0)
            yuanwen_side = repo_path('yuanwen', target)
            root_side = repo_path(target)
            if not os.path.exists(yuanwen_side) and os.path.exists(root_side):
                return '](../%s%s)' % (target, frag)
            return m.group(0)

        out.append(re.sub(r'\]\(([^)#\s]+)(#[^)]*)?\)', _rw, line))
    write_text_verified(repo_path('yuanwen', 'SUMMARY.md'), '\n'.join(out))
    return 0


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
