#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""B3.2 正文段装配：R 平铺块 → SEP 文章区段脚手架。

分工纪律：
  · 散文文字只来自 md（经 specs/053 bin/reassemble.py 的 R）
  · 结构（区段、标题 id 形态、文献分节切分、相关条目链接、学术工具行）
    只来自装配补集（baseline/en-template/article-ledger/），补集禁含散文
  · 本模块不读 H0；只受 md＋补集的驱动（判官另行比对 H0）

产出：文章内层 HTML（含 `#aueditable` 包装与 BEGIN/END 标记之外的部分）。
"""
import os
import re
import sys

# `-I` 模式不带脚本目录：显式补上，供同目录模块互引
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

# 表块扫描／嵌套表暂存与账侧同一实现（「账与 R 必须同语料」）
from article_ledger import stash_nested, table_spans  # noqa: E402

PREFIX = '\n\n\n<div id="aueditable"><!--DO NOT MODIFY THIS LINE AND ABOVE-->\n\n'
SUFFIX = ('</div><!-- #aueditable --><!--DO NOT MODIFY THIS LINE AND BELOW-->\n\n')

TOC_FIXED = (("Bib", "Bibliography"), ("Aca", "Academic Tools"),
             ("Oth", "Other Internet Resources"), ("Rel", "Related Entries"))
ACAD_ROWS = (("sepman-icon.jpg", "sep man icon"),
             ("sepman-icon.jpg", "sep man icon"),
             ("inpho.png", "inpho icon"),
             ("pp.gif", "phil papers icon"))
REGION_HEADS = {"Bibliography": "bibliography", "Academic Tools": "academic-tools",
                "Other Internet Resources": "other-internet-resources",
                "Related Entries": "related-entries"}
# 致谢区题：Acknowledgment(s)／Acknowledgement(s) 四种拼写，级别 h2/h3 都有
ACK_HEAD_RE = re.compile(r"^Acknowl")


def split_blocks(art):
    """R 的平铺输出 → 块列表（按顶层标签配平切分）。

    行首出现新块的开标签（`<h2>`/`<p>`/`<ul>` 等）时先收上一块——
    词条 HTML 的块边界恒在行首，而深度计数法会因跨行标签把相邻块并成
    一块（meinong 判例：`</p>\n<h2>Bibliography</h2>\n<p>…` 三块并一，
    区域路由只见 h2、首段被当标题附件吞掉）。"""
    lines = art.split("\n")
    blocks, cur, depth = [], [], 0
    for ln in lines:
        s = ln.lstrip()
        opens = re.match(r"<(?:p|ul|ol|blockquote|table|div|figure|dl|pre|"
                         r"h[1-6])\b", s)
        if cur and opens and depth <= 0:
            blocks.append("\n".join(cur))
            cur = []
        if not cur and not ln.strip():
            continue
        cur.append(ln)
        depth += sum(ln.count("<" + t) - ln.count("</" + t)
                     for t in ("p", "ul", "ol", "blockquote", "table",
                               "div", "figure", "dl", "pre"))
        if depth <= 0 and cur:
            depth = 0
            blocks.append("\n".join(cur))
            cur = []
    if cur:
        blocks.append("\n".join(cur))
    return blocks


def head_of(block):
    m = re.match(r"<h([1-6])(?:\s[^>]*)?>(.*?)</h\1>", block, re.S)
    return m


def _ids_for(headings, ledger):
    """标题 id 形态：补集按文档序给（hids）；序数不齐时逐位回退 None。"""
    ids = (ledger or {}).get("hids") or []
    out = []
    for i, (lv, txt) in enumerate(headings):
        out.append(ids[i].get("id") if i < len(ids) else None)
    return out


def _enc(text, ledger):
    """账内文字按件位实体策略编码（rel 链接题等不经 _inline_md_to_html 的路径）。"""
    em = (ledger or {}).get("entities") or {}
    if not em:
        return text
    return "".join(em.get(c, c) for c in text)


def toc_href(hid):
    """TOC 目标：id 形态去前缀（name:/aid: 两种旧式锚）。"""
    if not hid:
        return ""
    for p in ("name:", "aid:"):
        if hid.startswith(p):
            return hid[len(p):]
    return hid


def wrap_html(s, width):
    """源字符宽度贪心折行（标签计入宽度，标签内不折）。

    断行时：闭合标签与自闭合标签（`</em>`、`<br />`）留在前行，开标签随下一词
    下行——与上游书写习惯一致（`worlds or\\n<em>kosmoi</em> are` 与
    `…</em>\\nphilosophy` 两型并存实证）。"""
    if not width or width <= 0:
        return s

    def left_tags(p):
        i = 0
        while i < len(p):
            m = re.match(r"</[^>]*>|<[^>]*?/>", p[i:])
            if not m:
                break
            i += len(m.group(0))
        return p[:i], p[i:]

    toks = re.findall(r"<a\b[^>]*>.*?</a>|<[^>]*>|[^<]+", s, re.S)
    lines, cur, pend = [], "", ""
    for tk in toks:
        if tk.startswith("<") and not tk.startswith("<a "):
            pend += tk
            continue
        # 整锚作一个不可折单元：H0 正文 129,369 条锚里仅 54 条锚文内含换行
        # （0.04%），折行只发生在锚之前。若让锚文参与词级折行，右逆新插入的
        # 锚会被从中间折断，而 H0 是整行不折 → 文字层错位（original-position
        # 判例：`Constructivism,\nObjectivity…`）。
        _anchor = tk.startswith("<a ")
        words = [tk] if _anchor else tk.split(" ")
        for idx, word in enumerate(words):
            brk = idx > 0 or (_anchor and idx == 0)
            if not word:
                if brk:
                    cur += pend + " "
                    pend = ""
                continue
            if brk and cur and not cur.endswith(" "):
                left, right = left_tags(pend)
                trial = cur + left
                if len(trial) + 1 + len(right) + len(word) > width:
                    lines.append(trial)
                    cur, pend = right + word, ""
                    continue
                cur, pend = trial + " " + right + word, ""
                continue
            if brk and cur.endswith(" "):
                # 连续空格串：`split(" ")` 的 n−1 个空 token 已各记一空格，
                # 词前再补一个分隔符才等于原串长度（H0 正文 439 件有词间双空格）
                cur += pend + " " + word
                pend = ""
                continue
            cur += pend + word
            pend = ""
    lines.append(cur + pend)
    return "\n".join(lines)


def wrap_article(html, width):
    """只折 <p>/<li> 文本层（表格、标题、列表结构不动）；相关条目区不折
    （该区一件一条链接，上游从不折行）；导航区 toc 不折——账里 toc_block
    本就逐字（article_ledger 注），而 wrap_html 把标签计入宽度且折叠连续
    空格，会把短项误折（alain-locke 判例：`2.1\nValue-Feelings` 与
    `2.  Axiology` 双空格坍缩，整页文字流错位）。"""
    if not width:
        return html
    cut = html.find('<div id="related-entries">')
    if cut > 0:
        return wrap_article(html[:cut], width) + html[cut:]
    t = html.find('<div id="toc">')
    if t >= 0:
        e = html.find("</div>", t)
        if e > 0 and "<div" not in html[t + len("<div"):e]:
            e += len("</div>")
            return (wrap_article(html[:t], width) + html[t:e]
                    + wrap_article(html[e:], width))
    html = re.sub(r"<p>\n?(.*?)</p>",
                  lambda m: "<p>\n%s</p>" % wrap_html(m.group(1), width),
                  html, flags=re.S)
    html = re.sub(r"<li>(.*?)</li>",
                  lambda m: "<li>%s</li>" % wrap_html(m.group(1), width),
                  html, flags=re.S)
    return html


def heading_tag(lv, hid, inner):
    if not hid:
        return "<h%d>%s</h%d>" % (lv, inner, lv)
    if hid.startswith("name:"):
        return '<h%d><a name="%s">%s</a></h%d>' % (lv, hid[5:], inner, lv)
    if hid.startswith("aid:"):
        return '<h%d><a id="%s">%s</a></h%d>' % (lv, hid[4:], inner, lv)
    return '<h%d id="%s">%s</h%d>' % (lv, hid, inner, lv)


def render_tables(html, ledger):
    """按表格结构账重建 <table> 位形（th/td/空位/colspan、thead/tbody）。

    按**行**分配 R 侧格内容：账的非空格依序取本行 R 的非空单元、空格留白。
    不按列位置对应——C 把 H0 的 colspan 展开成逻辑列时，文字落点不可靠
    （aristotle-logic 判例：`| | Affirmations | Denials | | |` 五列，
    H0 是 `[空, colspan2 Affirmations, colspan2 Denials]` 三格）。"""
    tbls = (ledger or {}).get("tables")
    if not tbls:
        return html
    idx = [0]

    def render_block(block):
        """一个**顶层**表块 → 按账重建；内层表原样还原（账只记顶层）。"""
        m = re.match(r"<table([^>]*)>", block, re.I)
        if not m or idx[0] >= len(tbls):
            return block
        spec = tbls[idx[0]]
        idx[0] += 1
        # 内层表先占位：行/格解析只看本层（非贪婪 `</td>` 不会在内层收口处截断）
        inner, tstore = stash_nested(block[m.end():])
        inner = re.sub(r"</table\s*>\s*$", "", inner, flags=re.I)
        # 题注：账只记位形，题注文字在 R 侧块里（md `***Table 1***` 紧贴表格
        # → R 发 <caption>）——重建时原样带回，否则表题整块丢失
        # （bayes-theorem 判例：A 侧表从 Ratio/Difference 起，无 Table 1）
        cap = ""
        cm = re.search(r"<caption[^>]*>.*?</caption>", inner, re.S)
        if cm:
            cap = cm.group(0)
        rrows = [[c.group(1) for c in re.finditer(
            "<t[hd][^>]*>(.*?)</t[hd]>", r.group(1), re.S)]
            for r in re.finditer(r"<tr[^>]*>(.*?)</tr>", inner, re.S)]
        out = ["<table%s>\n" % spec.get("attrs", "")]
        if cap:
            out.append(cap + "\n")
        th_rows = spec.get("thead_rows", 0)
        for ri, row in enumerate(spec.get("rows", [])):
            if ri == 0 and spec.get("thead"):
                out.append("<thead>\n")
            if th_rows and ri == th_rows:
                out.append("</thead>\n")
            if th_rows and ri == th_rows and spec.get("tbody"):
                out.append("<tbody>\n")
            rcells = rrows[ri] if ri < len(rrows) else []
            pool = [c for c in rcells if c.strip()]
            n_nonx = sum(1 for c in row
                         if (c if isinstance(c, str) else c[0]) != "x")
            if len(pool) != n_nonx:
                # 分配不成立（rowspan 缩并等）：原样交回，让池判 gap
                return block
            pi = 0
            cs = []
            for cell in row:
                if isinstance(cell, str):
                    kind, span = cell, 1
                else:
                    kind, span = cell[0], int(cell[1] or 1)
                if kind == "x":
                    content, tag = "", "td"
                else:
                    content = pool[pi]
                    pi += 1
                    tag = "th" if kind == "h" else "td"
                attr = ' colspan="%d"' % span if span > 1 else ""
                cs.append("<%s%s>%s</%s>" % (tag, attr, content, tag))
            out.append("<tr>%s</tr>\n" % "".join(cs))
        if th_rows and th_rows >= len(spec.get("rows", [])):
            out.append("</thead>\n")
        if spec.get("tbody"):
            out.append("</tbody>\n")
        out.append("</table>")
        res = "".join(out)
        for k, blk in enumerate(tstore):
            res = res.replace("\x06T%d\x06" % k, blk)
        return res

    spans = table_spans(html)
    if not spans:
        return html
    pieces, prev = [], 0
    for st, en in spans:
        pieces.append(html[prev:st])
        pieces.append(render_block(html[st:en]))
        prev = en
    pieces.append(html[prev:])
    return "".join(pieces)


def build(md_article_html, ledger):
    """R 平铺 HTML → (article_inner_html)。ledger 缺省时按最小规则装配。"""
    ledger = ledger or {}
    md_article_html = render_tables(md_article_html, ledger)
    blocks = split_blocks(md_article_html)
    if not blocks:
        return None
    # ① 取 h1 与 pubinfo（合成层）；h1 **之前**的块（H0 头部图段等）按原位
    # 发在 h1 前——C 的 md 把 h1 提到首行，R 平铺序与 H0 相同，build 不得
    # 把这些块卷进 preamble（whitehead 判例：H0 序＝照片段→h1→pubinfo）
    title_inner = None
    pubinfo = None
    rest = []
    pre = []
    for b in blocks:
        if title_inner is None and b.startswith("<h1>"):
            title_inner = b[len("<h1>"):-len("</h1>")]
            continue
        if title_inner is None:
            pre.append(b)
            continue
        if pubinfo is None and b.startswith('<div id="pubinfo">'):
            pubinfo = b[len('<div id="pubinfo"><em>'):-len("</em></div>")]
            continue
        rest.append(b)
    if title_inner is None:
        return None
    # ② 粗分区
    preamble, main, bib, acad, oth, rel, ack = [], [], [], [], [], [], []
    cur = preamble
    # 书目 div 内的同行级分节（H0 的 Bibliography 之后仍有 h2 分节，全库 4 件：
    # baudrillard／aristotle-ethics／epistemology-latin-america／marxism-analytical）。
    # 账里的 bib_heads 是容器内标题的唯一事实源：名字在册即归书目区，
    # 否则会被当成正文新主节、抢到书目区之前（baudrillard 判例）。
    _bib_names = {re.sub(r"<[^>]*>", "", (h[1] or "")).strip()
                  for h in ((ledger or {}).get("bib_heads") or [])}
    for b in rest:
        m = head_of(b)
        if m:
            lv, txt = int(m.group(1)), m.group(2).strip()
            if lv == 2 and txt in REGION_HEADS:
                cur = {"bibliography": bib, "academic-tools": acad,
                       "other-internet-resources": oth,
                       "related-entries": rel}[REGION_HEADS[txt]]
                cur.append(b)
                continue
            if cur is bib and lv >= 2 and txt in _bib_names:
                cur.append(b)      # 书目容器内的分节标题，留在书目区
                continue
            if lv in (2, 3) and ACK_HEAD_RE.match(
                    re.sub(r"</?(?:strong|em|b)>", "", txt)):
                # 致谢题允许行内强调包裹（suhrawardi 判例：md
                # `### **Acknowledgement**` → R 发 <strong>；不剥则匹配
                # 失败、整节被并进 related-entries 区丢弃）
                cur = ack
                cur.append(b)
                continue
            if lv == 2:
                cur = main
                cur.append(b)
                continue
            if lv == 3 and cur is preamble:
                # 全 h3 体例的词条（logic-connexive 判例：H0 主节即 h3、
                # 通体无 h2）：首个 h3 即入 main——否则正文全部卷进
                # preamble、TOC 块被挤到正文之后（unaligned text units）
                cur = main
                cur.append(b)
                continue
            if lv == 3 and cur is bib:
                cur.append(b)
                continue
        cur.append(b)
    # ③ 标题 id 形态
    heads = []
    for b in rest:
        m = head_of(b)
        if m:
            heads.append((int(m.group(1)), m.group(2).strip()))
    ids = _ids_for(heads, ledger)
    hid_map = {}
    it = iter(ids)
    for b in rest:
        m = head_of(b)
        if m:
            hid_map[id(b)] = next(it, None)
    # ④ 装配
    out = [PREFIX]
    if pre:
        out.append("\n".join(pre))
    out.append("<h1>%s</h1>" % title_inner)
    if pubinfo is not None:
        out.append('<div id="pubinfo"><em>%s</em></div>\n' % pubinfo)
    else:
        out.append("\n")
    # TOC 逐字块与「toc 后悬置的正文首段」先算：preamble 过滤要用 _skip_norms
    _toc_block = (ledger or {}).get("toc_block")
    _skip_norms = []
    if _toc_block:
        # H0 的 toc div 与 main-text div 之间可能悬着正文首块（domination 判例：
        # main-text div 晚开；consciousness-intentionality 判例：main-text 首段
        # 在首个 h2 之前）——toc_block 已按 H0 原样带上这一截，正文与前言两侧
        # 须跳过同文块，否则双发。
        _mtail = re.search(r"</div>\s*(.*)$", _toc_block, re.S)
        if _mtail and _mtail.group(1).strip():
            _skip_norms = [_norm_txt(x) for x in re.findall(
                r"<(?:h[1-6]|p|blockquote|ul|ol|table|dl)[^>]*>.*?"
                r"</(?:h[1-6]|p|blockquote|ul|ol|table|dl)>",
                _mtail.group(1), re.S)]
    if preamble:
        if _skip_norms:
            preamble = [b for b in preamble
                        if _norm_txt(b) not in _skip_norms]
        body = "\n".join(preamble)
        body = re.sub(r"^<p>", "<p>\n", body)
        out.append('\n<div id="preamble">\n\n%s\n</div> \n' % body)
    # TOC
    toc = []
    for b in rest:
        m = head_of(b)
        if not m:
            continue
        lv, txt = int(m.group(1)), m.group(2).strip()
        if lv == 2 and txt in REGION_HEADS:
            break
        if lv == 2:
            hid = hid_map.get(id(b)) or ""
            toc.append('\t<li><a href="#%s">%s</a></li>' % (toc_href(hid), txt))
    for hid, txt in TOC_FIXED:
        toc.append('\t<li><a href="#%s">%s</a></li>' % (toc_href(hid), txt))
    if _toc_block:
        # 导航区逐字（题与锚由正文派生；另设一致性核对，见 article_ledger 注释）
        out.append("\n" + _toc_block)
    else:
        out.append('\n<div id="toc"><!--Entry Contents-->\n<ul>\n%s\n</ul>\n'
                   '<!--Entry Contents-->\n\n<hr /></div>\n' % "\n".join(toc))
    # main-text
    mt = _render_main(main, hid_map, _skip_norms)
    out.append('<div id="main-text">\n\n%s\n</div>\n' % (mt or ""))
    # 尾部区按 md 标题次序发（md 序＝H0 序，C 按文档序落块）：常序 bib→acad→oth→rel；
    # civil-disobedience 的致谢在书目之后、学术工具之前（H0 实测），固定次序会错位。
    _pos = {}
    for _i, _b in enumerate(rest):
        _pos[id(_b)] = _i
    _regions = [("bib", bib), ("acad", acad), ("oth", oth), ("rel", rel),
                ("ack", ack)]
    for _name, _lst in sorted(_regions,
                              key=lambda x: _pos.get(id(x[1][0]), 10 ** 9)
                              if x[1] else 10 ** 9):
        if not _lst:
            continue
        if _name == "bib":
            out.append(_render_bib(bib, hid_map, ledger))
        elif _name == "acad":
            out.append(_render_acad(acad, hid_map, ledger))
        elif _name == "oth":
            out.append(_render_other(oth, hid_map))
        elif _name == "rel":
            out.append(_render_rel(rel, hid_map, ledger))
        else:
            head = ack[0]
            inner = "\n".join(ack[1:])
            inner = re.sub(r"^<p>", "<p>\n", inner)
            hd = heading_tag(int(head_of(head).group(1)), hid_map.get(id(head)),
                             head_of(head).group(2).strip())
            if (ledger or {}).get("ack_div", 1) == 0:
                # H0 无独立包层：致谢题与段直接跟在 related-entries div 之后
                out.append("\n%s\n\n%s\n" % (hd, inner))
            else:
                out.append('\n<div id="acknowledgments">\n\n%s\n\n%s\n</div> \n'
                           % (hd, inner))
    out.append(SUFFIX)
    return wrap_article("".join(out), (ledger or {}).get("wrap_width"))


def _norm_txt(s):
    """块 → 归一化可见文（剥标签折空白），跨侧同文块比对用。"""
    return re.sub(r"\s+", "", re.sub(r"<[^>]*>", "", s))


def _render_main(main, hid_map, skip_norms=None):
    skip = list(skip_norms or [])
    skipping = bool(skip)   # 只允许吃头部：同文块出现在中段不跳
    chunks = []
    for b in main:
        if skipping and skip and _norm_txt(b) == skip[0]:
            skip.pop(0)
            continue
        skipping = False
        m = head_of(b)
        if m:
            lv = int(m.group(1))
            chunks.append(heading_tag(lv, hid_map.get(id(b)), m.group(2).strip()))
            continue
        if b.startswith("<p>"):
            chunks.append("<p>\n%s" % b[len("<p>"):])
            continue
        chunks.append(b)
    return "\n\n".join(chunks)


def _match_close(s, start, open_pat, close_pat):
    """括号配平：找 start 之后首个开标签对应的闭标签（depth 自 1 起算，
    已由调用方消费开标签本身）。"""
    depth = 1
    j = None
    # 大小写不敏感同账侧：H0 偶见大写 `<LI>`／`</LI>`（time 判例）
    for t in re.finditer(open_pat + "|" + close_pat, s, re.I):
        if t.start() < start:
            continue
        depth += 1 if re.match(open_pat, t.group(0), re.I) else -1
        if depth == 0:
            j = t
            break
    return j


def _flat_li(html):
    """嵌套 ul → 文档序平铺条目表（父项剥掉子 ul 后的剩余，父先子后）。

    与账 _tree_nodes 的 i 序一致。旧实现用非贪婪 `<li>(.*?)</li>` 提取，
    遇嵌套 subhang 会在子项首个 </li> 处错切（abelard：父项被截断、
    随后 English 分节条目混进 Latin ul）。"""
    out = []

    def walk(inner):
        pos = 0
        for m in re.finditer(r"<li([^>]*)>", inner, re.I):
            if m.start() < pos:
                continue
            t = _match_close(inner, m.end(), r"<li[^>]*>", r"</li>")
            if t:
                sub, nxt = inner[m.end():t.start()], t.end()
            else:
                sub, nxt = inner[m.end():], len(inner)
            kids, rest, p = [], [], 0
            for mu in re.finditer(r"<ul([^>]*)>", sub, re.I):
                if mu.start() < p:
                    # 已随外层 ul 平衡跨度入 kids 的内层 ul 不重扫：三层嵌套
                    # （li→ul→ul）时旧实现把同一子表挂两遍，条目双计、后续
                    # 索引整体错位（habermas 判例：Works 节 125 条 vs H0 124）
                    continue
                tu = _match_close(sub, mu.end(), r"<ul[^>]*>", r"</ul>")
                if not tu:
                    continue
                kids.append(sub[mu.end():tu.start()])
                rest.append(sub[p:mu.start()])
                p = tu.end()
            rest.append(sub[p:])
            out.append("".join(rest))
            for k in kids:
                walk(k)
            pos = nxt

    walk(html)
    return out


def _p_inner(s):
    """`<p>…</p>` 块剥壳（dl 的 dt/dd 内容取整块内文）；空串原样。"""
    if s.startswith("<p>"):
        s = s[len("<p>"):]
    if s.endswith("</p>"):
        s = s[:-len("</p>")]
    return s


def _render_bib(bib, hid_map, ledger):
    if not bib:
        return ""
    ledger = ledger or {}
    # 书目区标题：R 侧恒发“Bibliography”（源自 `## References（引用注释）`），
    # H0 的 bibliograph div 首题未必是它（aristotle-ethics：div 首题 Further
    # Reading，其后才是 h2 Bibliography）。故取 bib_heads 中**与 R 侧同名**的
    # 那一项作区标题（找不到退回首项），并在 seq 中跳过同一项，避免重复。
    _rname = head_of(bib[0]).group(2).strip()
    _bh = ledger.get("bib_heads") or []
    _skip_h = None
    _bh_sel = None
    for _k, _h in enumerate(_bh):
        if (_h[1] or "").strip() == _rname:
            _skip_h, _bh_sel = _k, _h
            break
    if _bh_sel is None and _bh:
        _skip_h, _bh_sel = 0, _bh[0]
    if _bh_sel and _bh_sel[1]:
        _hlv = _bh_sel[0] or 2
        _hname = _bh_sel[1]
        _hhid = _bh_sel[2] if len(_bh_sel) > 2 else None
    else:
        _hlv = 2
        _hname = _rname
        _hhid = hid_map.get(id(bib[0])) or "Bib"
    parts = ['\n<div id="bibliography">\n\n%s\n\n'
             % heading_tag(_hlv, _hhid, _enc(_hname, ledger))]
    body = bib[1:]
    items = []
    for b in body:
        if b.startswith("<ul"):
            items.extend(_flat_li(b))
    subs = [(int(head_of(b).group(1)), head_of(b).group(2).strip(),
             hid_map.get(id(b)))
            for b in body if head_of(b)]
    ps = [b for b in body if b.startswith("<p>")]
    counts = ledger.get("bib_groups") or ([len(items)] if items else [])
    k = 0

    def ul(chunk):
        ids = ledger.get("bib_ids") or {}
        lis = []
        prev = -1
        for j, c in chunk:
            if j is None:
                # 账内定位失败的条目按顺序兜底（H0 顺序＝md 定义序）
                j = prev + 1
            prev = j
            lid = ids.get(str(j))
            lis.append('<li id="%s">%s</li>' % (lid, c) if lid
                       else "<li>%s</li>" % c)
        return '<ul class="hanging">\n\n%s\n</ul>\n\n' % "\n\n".join(lis)

    cursor = [-1]
    used_i = set()

    def _next_free(start):
        j = max(start, 0)
        while j in used_i and j < len(items):
            j += 1
        return j

    def nodes_html(nodes):
        """按嵌套结构账渲染条目树（子 ul 属性、缩进与 li 包裹按账）。

        账内 i 缺失时取「下一个未用索引」兜底——只用 cursor+1 会让多条
        缺失节点指向同一/已用条目而重复、错位（abelard 104 li vs H0 96
        判例：8 个节点缺 i）。"""
        ids = ledger.get("bib_ids") or {}
        out = []
        for nd in nodes:
            j = nd.get("i")
            if not isinstance(j, int) or j in used_i:
                if nd.get("c") and not nd.get("t"):
                    # 有子表、且本层无文字的空壳 li（H0 双层 ul 包装，
                    # confucian-gender 判例）：本无条目内容，禁兜底占位——
                    # 占位会把整条 ul 的条目顶后一位、尾段条目溢进下一节。
                    # 父条目带引子行（`t`=1，pomponazzi `Aristotle,`）不在此列，
                    # 仍须兜底占位，否则引子文字丢失
                    content = ""
                    lid = None
                    head = "<li>"
                    head += ("\n\n<ul %s>\n\n%s\n</ul>\n\n</li>"
                             % (nd.get("u") or "", nodes_html(nd["c"])))
                    out.append(head)
                    continue
                if nd.get("e"):
                    # 账记 `e`=1：H0 的 `<li> </li>` 空条目（全库 12 件）。原样
                    # 发空条目，禁兜底占位——占位会把本节尾条顶进下一节、下一
                    # 节首条错位一位（scottus-eriugena「Other Early Works」尾
                    # 混进 Allard，2026-11-25）。须由账标记而非渲染侧猜测：
                    # 匹配失败但 H0 有文字的节点仍须兜底（habermas 判例）
                    out.append("<li></li>")
                    continue
                j = _next_free(cursor[0] + 1)
            if j >= len(items) or j in used_i:
                # 无可用条目：跳过空节点（不再输出空 li，abelard 多 8 条判例）
                continue
            cursor[0] = j
            used_i.add(j)
            content = items[j] if j < len(items) else ""
            lid = ids.get(str(j))
            head = ('<li id="%s">%s' % (lid, content) if lid
                    else "<li>%s" % content)
            if nd.get("c"):
                head += ("\n\n<ul %s>\n\n%s\n</ul>\n\n</li>"
                         % (nd.get("u") or "", nodes_html(nd["c"])))
            else:
                head += "</li>"
            out.append(head)
        return "\n\n".join(out)

    tree = ledger.get("bib_tree")
    ul_i = [0]

    seq = ledger.get("bib_seq")
    if seq:
        bids = ledger.get("bib_ids") or {}
        bh = ledger.get("bib_heads") or []
        bhi = [0]
        tables = [b for b in body if b.startswith("<table")]
        bqs = [b for b in body if b.startswith("<blockquote")]
        tb_i = [0]
        for kind, idx in seq:
            if kind == "h":
                lv = name = hid = None
                _pos = bhi[0]
                if isinstance(idx, int) and idx < len(subs):
                    lv, name, hid = subs[idx]
                if bhi[0] < len(bh):
                    b = bh[bhi[0]]
                    l2, t2 = b[0], b[1]
                    i2 = b[2] if len(b) > 2 else None
                    if l2:
                        lv = l2
                    if t2:
                        name = t2
                    if not hid and i2:
                        hid = i2
                bhi[0] += 1
                # 区标题已由本函数开头预发（按 bib_heads 中与 R 同名项即
                # “Bibliography”），该项及其之前的 H0 标题一律跳过：H0 的
                # bibliograph div 可能包含 md 已排进正文的前置节
                # （aristotle-ethics：div 首题 Further Reading 在 md 正文里），
                # 再发一遍就成了重复标题；其文字已在正文出现，div 边界差交池
                if (bh and _skip_h is not None and _pos <= _skip_h) or (
                        not bh and lv == 2 and name == "Bibliography"):
                    continue
                if name and re.sub(r"<[^>]*>", "", name).strip() in REGION_HEADS:
                    # 后续独立区题被 H0 的 bibliograph div 裹进来
                    # （marxism-analytical 判例：div 内 `Academic Tools`）：
                    # 该区由自己的分区渲染（含表），此处跳过，免双重
                    continue
                if lv and name:
                    # 题后散字（账第 4 位，H0 原文片段）原样接在题后，替代
                    # 常规空行分隔——该片段自带尾随空白（hobbes-science 判例）
                    _bt = bh[bhi[0] - 1][3] if (bhi[0] - 1 < len(bh)
                                                and len(bh[bhi[0] - 1]) > 3) else ""
                    _hname_enc = _enc(name, ledger)
                    if _bt:
                        parts.append(heading_tag(lv, hid, _hname_enc) + _bt)
                    else:
                        parts.append("%s\n\n" % heading_tag(lv, hid, _hname_enc))
            elif kind == "table":
                if tb_i[0] < len(tables):
                    parts.append("%s\n\n" % tables[tb_i[0]])
                    tb_i[0] += 1
            elif kind == "p":
                if isinstance(idx, int) and idx < len(ps):
                    parts.append("%s\n\n" % re.sub(r"^<p>", "<p>\n", ps[idx]))
            elif kind == "pd":
                # 散文被 C 折成定义行（`[^following-nd]:` 判例）：原位发 <p>
                if isinstance(idx, int) and idx < len(items):
                    parts.append("<p>\n%s</p>\n\n" % items[idx])
            elif kind == "bq":
                # 书目区引块（berkeley 的 `[W]` 版本条目）：R 侧 body 内对应位次
                # 的 blockquote 块原样发（文本取自 md `>` 块，账只记位次）
                if isinstance(idx, int) and idx < len(bqs):
                    parts.append("%s\n\n" % bqs[idx])
            elif kind == "dl":
                # 定义表（缩写键块）：dt/dd 文字从 md 段取，属性由账记
                # （alain-locke 判例：旧实现整块漏发，23 件书目区 dl 全 gap）
                dls = ledger.get("bib_dl") or []
                if isinstance(idx, int) and idx < len(dls):
                    rec = dls[idx]
                    rows = []
                    for pair in rec.get("pairs") or []:
                        dt_i, dd_i = pair[0], pair[1]
                        dt_a = pair[2] if len(pair) > 2 else ""
                        dd_a = pair[3] if len(pair) > 3 else ""
                        dt_in = (_p_inner(ps[dt_i])
                                 if isinstance(dt_i, int) and dt_i < len(ps)
                                 else "")
                        dd_in = (_p_inner(ps[dd_i])
                                 if isinstance(dd_i, int) and dd_i < len(ps)
                                 else "")
                        if (not dd_in and len(pair) > 4
                                and isinstance(pair[4], int)
                                and 0 <= pair[4] < len(items)):
                            # specs/053 第五十八批：书目 dd 入定义流后 md 无散文段，
                            # 文字从定义行（装配 items 与 md 定义行同序）取
                            dd_in = items[pair[4]]
                        rows.append("<dt%s>%s</dt>\n<dd%s>%s</dd>"
                                    % (dt_a, dt_in, dd_a, dd_in))
                    if rows:
                        parts.append("<dl%s>\n%s\n</dl>\n\n"
                                     % (rec.get("attrs") or "",
                                        "\n".join(rows)))
            elif kind in ("ul", "ol"):
                if kind == "ul" and tree and ul_i[0] < len(tree):
                    nodes = tree[ul_i[0]].get("nodes") or []
                    ul_i[0] += 1
                    if nodes:
                        parts.append('<ul class="hanging">\n\n%s\n</ul>\n\n'
                                     % nodes_html(nodes))
                        continue
                chunk = [(j, items[j]) for j in idx
                         if isinstance(j, int) and j < len(items)]
                if chunk:
                    if kind == "ol":
                        lis = "\n\n".join(
                            '<li id="%s">%s</li>'
                            % (bids.get(str(j)), c) if bids.get(str(j))
                            else "<li>%s</li>" % c for j, c in chunk)
                        parts.append("<ol>\n\n%s\n</ol>\n\n" % lis)
                    else:
                        parts.append(ul(chunk))
        parts.append("</div> \n")
        return "".join(parts)
    if not subs and items:
        parts.append(ul(list(enumerate(items))))
        k = len(items)
    for i, (lv, name, hid) in enumerate(subs):
        n = counts[i] if i < len(counts) else 0
        chunk = list(enumerate(items[k:k + n], start=k))
        k += n
        parts.append("%s\n\n" % heading_tag(lv, hid, name))
        if chunk:
            parts.append(ul(chunk))
    if k < len(items):
        parts.append(ul(list(enumerate(items[k:], start=k))))
    parts.append("</div> \n")
    return "".join(parts)


def _render_acad(acad, hid_map, ledger):
    if not acad:
        return ""
    head = acad[0]
    rows = []
    for b in acad[1:]:
        for r in re.finditer(r"<tr><td[^>]*>(.*?)</td><td[^>]*>(.*?)</td></tr>", b, re.S) or []:
            rows.append((r.group(1), r.group(2)))
        for r in re.finditer(r"<tr>\s*<td>(.*?)</td>\s*<td>(.*?)</td>\s*</tr>", b, re.S):
            if (r.group(1), r.group(2)) not in rows:
                rows.append((r.group(1), r.group(2)))
    out = ['\n<div id="academic-tools">\n%s\n\n<blockquote>\n<table class="vert-top">\n'
           % heading_tag(2, hid_map.get(id(head)) or "Aca",
                         head_of(head).group(2).strip())]
    icons = (ledger or {}).get("acad_icons") or [list(x) for x in ACAD_ROWS]
    for i, (cell1, cell2) in enumerate(rows):
        # 行数按实有行发，**不设 4 行上限**：新版模板的学术工具表多一行
        # 「The PhilPapers Surveys…」（truth-correspondence 判例，全库 1 件）。
        # 图标按位取；超出默认表的行沿用末项（pp.gif）——该行在 H0 恒为
        # PhilPapers 图标行。
        if i < len(icons):
            icon, alt = icons[i]
        elif i < len(ACAD_ROWS):
            icon, alt = ACAD_ROWS[i]
        else:
            icon, alt = ACAD_ROWS[-1]
        # 学术工具外链一律带 target="other"（站点固定式；md 表里只有 href）
        cell2 = re.sub(r'<a href="(https?://[^"]*)"', r'<a href="\1" target="other"',
                       cell2)
        if icon:
            out.append('<tr>\n<td><img src="../../symbols/%s" alt="%s" /></td>\n'
                       '<td>%s</td>\n</tr>\n' % (icon, alt, cell2))
        else:
            out.append('<tr>\n<td></td>\n<td>%s</td>\n</tr>\n' % cell2)
    out.append("</table>\n</blockquote>\n</div>\n")
    # acad 区余块原样跟随（levinas 判例：H0 书目 A./B. 分节被 C 按文档序排在
    # 学术工具表之后，H0 里位于 acad div 之外、OIR 之前；旧实现整块丢弃）。
    # 标题 id 形态交补集池（'m' 段）补。
    _tb = next((b for b in acad[1:] if "<tr" in b), None)
    _head_name = head_of(head).group(2).strip()
    for b in acad[1:]:
        if b is _tb or "<tr" in b:
            continue
        m = head_of(b)
        if m and re.sub(r"<[^>]*>", "", m.group(2)).strip() == re.sub(
                r"<[^>]*>", "", _head_name).strip():
            # 区内重复的区标题块（marxism-analytical 判例：H0 的 bibliograph
            # 尾部另有一段 `Academic Tools` 题，路由已由 acad[0] 发过一次；
            # H0 的题常带 `<a name=…>` 包裹，比对须剥标签）
            continue
        out.append("\n%s\n" % b)
    return "".join(out)


def _render_other(oth, hid_map):
    if not oth:
        return ""
    head = oth[0]
    body = "\n".join(oth[1:])
    body = re.sub(r"^<p>", "<p>\n", body)
    return '\n<div id="other-internet-resources">\n\n%s\n\n%s\n</div>\n' % (
        heading_tag(2, hid_map.get(id(head)) or "Oth",
                    head_of(head).group(2).strip()), body)


def _render_rel(rel, hid_map, ledger):
    if not rel:
        return ""
    head = rel[0]
    body = "\n".join(rel[1:])
    m = re.search(r"<p>(.*?)</p>", body, re.S)
    inner = m.group(1) if m else body
    items = (ledger or {}).get("rel_items")
    if items:
        trailing = bool((ledger or {}).get("rel_trailing"))
        # 新账逐项记 sep（该项前有无 `|`）；旧账无 sep 键时退回「项间全有|」
        has_sep = any("sep" in it for it in items)
        lines = []
        for i, it in enumerate(items):
            txt = _enc(it["text"], ledger)
            if has_sep:
                nxt = ((i + 1 < len(items) and bool(items[i + 1].get("sep")))
                       or (i == len(items) - 1 and trailing))
            else:
                nxt = (i < len(items) - 1 or trailing)
            sep = " |" if nxt else ""
            kind = it.get("kind")
            if kind == "dead":
                lines.append(' <!--<a href="%s">-->%s<!--</a>-->%s'
                             % (it["href"], txt, sep))
            elif kind == "a":
                lines.append(' <a href="%s">%s</a>%s'
                             % (it["href"], txt, sep))
            else:  # 纯文字项（上游未链接）——原样，无前导空格
                lines.append("%s%s" % (txt, sep))
        para = "\n".join(lines)
        if (ledger or {}).get("rel_lead"):
            # H0 的 related `<p>` 以 ` |` 起（md 同形保留）：首项前补回前导竖线
            para = " |\n" + (" " + para if not para.startswith(" ") else para)
    else:
        para = inner.strip()
    out = '\n<div id="related-entries">\n\n%s\n\n<p>\n%s\n\n</p>\n</div>\n' % (
        heading_tag(2, hid_map.get(id(head)) or "Rel",
                    head_of(head).group(2).strip()), para)
    # rel 区余块原样跟随（chinese-translate-interpret 判例：H0 在 rel div
    # 之后、acknowledgments div 之前悬一枚上游杂散反引号 `<p>`</p>`；旧实现
    # 丢弃）。位置随文档序落在 rel 与下一区之间。
    # 只发「不在已渲染条目文内」的块：H0 的 related 区可被拆成多段 `<p>`
    # （feminist-science 判例），逐块跟随会把条目文字重发一遍。
    def _rel_flat(x):
        # 注释（死链形 `<!--<a …>-->文字<!--</a>-->`）、分隔竖线、空白与实体
        # 形态不参与比对：H0 的 related 区可另有一份无竖线副本
        # （feminist-science 判例），账侧文字经实体编码、R 侧原文两侧形态
        # 不同（gregory-rimini／boethius-dacia 判例）
        x = re.sub(r"<!--.*?-->", "", x, flags=re.S)
        x = re.sub(r"&[A-Za-z]+;|&#\d+;", "", re.sub(r"<[^>]*>", "", x))
        return re.sub(r"[\s|]+", "", x)
    _para_flat = _rel_flat(para)
    for b in rel[1:]:
        if _rel_flat(b) and _rel_flat(b) in _para_flat:
            continue
        out += "\n%s\n" % b
    return out
