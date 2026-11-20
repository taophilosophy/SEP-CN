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
import re

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


def split_blocks(art):
    """R 的平铺输出 → 块列表（按顶层标签配平切分）。"""
    lines = art.split("\n")
    blocks, cur, depth = [], [], 0
    for ln in lines:
        if not cur and not ln.strip():
            continue
        cur.append(ln)
        depth += sum(ln.count("<" + t) - ln.count("</" + t)
                     for t in ("p", "ul", "ol", "blockquote", "table",
                               "div", "figure", "dl"))
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

    toks = re.findall(r"<[^>]*>|[^<]+", s)
    lines, cur, pend = [], "", ""
    for tk in toks:
        if tk.startswith("<"):
            pend += tk
            continue
        for idx, word in enumerate(tk.split(" ")):
            brk = idx > 0
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
            cur += pend + word
            pend = ""
    lines.append(cur + pend)
    return "\n".join(lines)


def wrap_article(html, width):
    """只折 <p>/<li> 文本层（表格、标题、列表结构不动）；相关条目区不折
    （该区一件一条链接，上游从不折行）。"""
    if not width:
        return html
    cut = html.find('<div id="related-entries">')
    if cut > 0:
        return wrap_article(html[:cut], width) + html[cut:]
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

    def rep(m):
        if idx[0] >= len(tbls):
            return m.group(0)
        spec = tbls[idx[0]]
        idx[0] += 1
        rrows = [[c.group(1) for c in re.finditer(
            "<t[hd][^>]*>(.*?)</t[hd]>", r.group(1), re.S)]
            for r in re.finditer(r"<tr[^>]*>(.*?)</tr>", m.group(1), re.S)]
        out = ["<table%s>\n" % spec.get("attrs", "")]
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
                return m.group(0)
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
        return "".join(out)

    return re.sub("<table[^>]*>(.*?)</table>", rep, html, flags=re.S)


def build(md_article_html, ledger):
    """R 平铺 HTML → (article_inner_html)。ledger 缺省时按最小规则装配。"""
    ledger = ledger or {}
    md_article_html = render_tables(md_article_html, ledger)
    blocks = split_blocks(md_article_html)
    if not blocks:
        return None
    # ① 取 h1 与 pubinfo（合成层）
    title_inner = None
    pubinfo = None
    rest = []
    for b in blocks:
        if title_inner is None and b.startswith("<h1>"):
            title_inner = b[len("<h1>"):-len("</h1>")]
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
            if lv == 3 and txt == "Acknowledgments":
                cur = ack
                cur.append(b)
                continue
            if lv == 2:
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
    out.append("<h1>%s</h1>" % title_inner)
    if pubinfo is not None:
        out.append('<div id="pubinfo"><em>%s</em></div>\n' % pubinfo)
    else:
        out.append("\n")
    if preamble:
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
    if (ledger or {}).get("toc_block"):
        # 导航区逐字（题与锚由正文派生；另设一致性核对，见 article_ledger 注释）
        out.append("\n" + ledger["toc_block"])
    else:
        out.append('\n<div id="toc"><!--Entry Contents-->\n<ul>\n%s\n</ul>\n'
                   '<!--Entry Contents-->\n\n<hr /></div>\n' % "\n".join(toc))
    # main-text
    mt = _render_main(main, hid_map)
    out.append('<div id="main-text">\n\n%s\n</div>\n' % (mt or ""))
    out.append(_render_bib(bib, hid_map, ledger))
    out.append(_render_acad(acad, hid_map, ledger))
    out.append(_render_other(oth, hid_map))
    out.append(_render_rel(rel, hid_map, ledger))
    if ack:
        head = ack[0]
        inner = "\n".join(ack[1:])
        inner = re.sub(r"^<p>", "<p>\n", inner)
        out.append('\n<div id="acknowledgments">\n\n%s\n\n%s\n</div> \n' % (
            heading_tag(3, hid_map.get(id(head)), head_of(head).group(2).strip()), inner))
    out.append(SUFFIX)
    return wrap_article("".join(out), (ledger or {}).get("wrap_width"))


def _render_main(main, hid_map):
    chunks = []
    for b in main:
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
    for t in re.finditer(open_pat + "|" + close_pat, s):
        if t.start() < start:
            continue
        depth += 1 if re.match(open_pat, t.group(0)) else -1
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
        for m in re.finditer(r"<li([^>]*)>", inner):
            if m.start() < pos:
                continue
            t = _match_close(inner, m.end(), r"<li[^>]*>", r"</li>")
            if t:
                sub, nxt = inner[m.end():t.start()], t.end()
            else:
                sub, nxt = inner[m.end():], len(inner)
            kids, rest, p = [], [], 0
            for mu in re.finditer(r"<ul([^>]*)>", sub):
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


def _render_bib(bib, hid_map, ledger):
    if not bib:
        return ""
    ledger = ledger or {}
    parts = ['\n<div id="bibliography">\n\n%s\n\n' % heading_tag(
        2, hid_map.get(id(bib[0])) or "Bib",
        head_of(bib[0]).group(2).strip())]
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
        tb_i = [0]
        for kind, idx in seq:
            if kind == "h":
                lv = name = hid = None
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
                # seq 首项即 H0 的 `<h2>Bibliography</h2>`（区标题已由本函数
                # 开头预发，勿重复；abstract-objects 判例）
                if lv == 2 and name == "Bibliography":
                    continue
                if lv and name:
                    parts.append("%s\n\n" % heading_tag(lv, hid, name))
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
    for i, (cell1, cell2) in enumerate(rows[:4]):
        icon, alt = (icons[i] if i < len(icons) else ACAD_ROWS[i])
        # 学术工具外链一律带 target="other"（站点固定式；md 表里只有 href）
        cell2 = re.sub(r'<a href="(https?://[^"]*)"', r'<a href="\1" target="other"',
                       cell2)
        if icon:
            out.append('<tr>\n<td><img src="../../symbols/%s" alt="%s" /></td>\n'
                       '<td>%s</td>\n</tr>\n' % (icon, alt, cell2))
        else:
            out.append('<tr>\n<td></td>\n<td>%s</td>\n</tr>\n' % cell2)
    out.append("</table>\n</blockquote>\n</div>\n")
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
    else:
        para = inner.strip()
    return '\n<div id="related-entries">\n\n%s\n\n<p>\n%s\n\n</p>\n</div>\n' % (
        heading_tag(2, hid_map.get(id(head)) or "Rel",
                    head_of(head).group(2).strip()), para)
