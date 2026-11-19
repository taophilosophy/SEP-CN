#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""B3.2 正文段装配补集：结构账抽取器。

只抽结构，不抽散文：
  hids        每个 h2/h3 的 id 形态（`X` 为 id 属性 / `name:X` / `aid:X` / 空串）
  bib_groups  文献分节各自的条目数（切分文献 ul）
  rel_links   相关条目链接（href＋显示文本＋死链注释标记）
  acad_icons  学术工具四行的图标与 alt
  wrap/entities 视觉层（空白位图与实体策略）由后续批次补入

产出 baseline/en-template/article-ledger.json（冻结派生件，重跑须复核）。
"""
import argparse
import html as htmllib
import io
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))), "tools"))
from tools.common import repo_path  # noqa: E402

B1 = "<!-- BEGIN ARTICLE HTML -->"
E1 = "<!-- END ARTICLE HTML -->"
LEDGER_PATH = ("baseline", "en-template", "article-ledger.json")
HEAD_RE = re.compile(r"<h([2-6])((?:\s[^>]*)?)>(.*?)</h\1>", re.S)


def read(p):
    return io.open(p, encoding="utf-8", newline="").read()


def inner_article(t):
    i1 = t.index(B1) + len(B1)
    i2 = t.index(E1)
    return t[i1:i2]


def hid_form(attrs, inner):
    m = re.search(r'\bid="([^"]*)"', attrs)
    if m:
        return m.group(1)
    m = re.search(r'<a\s+name="([^"]*)"', inner)
    if m:
        return "name:" + m.group(1)
    m = re.search(r'<a\s+id="([^"]*)"', inner)
    if m:
        return "aid:" + m.group(1)
    return ""


ENT_RE = re.compile(r"&(#[0-9]+|#[xX][0-9A-Fa-f]+|[A-Za-z][A-Za-z0-9]*);")


def extract_entities(art_inner):
    """实体策略：件内以实体形态出现的非 ASCII 字符 → 该实体串。

    同一字符若在本文中既以实体出现又以字面出现，视为非一致策略（不入账，
    交装配补集吸收）；`&amp;`/`&lt;`/`&gt;` 等 ASCII 实体不入账（R 自带转义）。
    """
    forms = {}
    ambig = set()
    for m in ENT_RE.finditer(art_inner):
        dec = htmllib.unescape(m.group(0))
        if len(dec) != 1 or ord(dec) < 128:
            continue
        forms.setdefault(dec, set()).add(m.group(0))
    # 字面出现统计：剥掉全部实体后计字面次数
    stripped = ENT_RE.sub("", art_inner)
    out = {}
    for ch, fs in forms.items():
        if len(fs) > 1 or ch in stripped:
            ambig.add(ch)
            continue
        out[ch] = next(iter(fs))
    return out


def wrap_width(art_inner):
    """折行宽度：源字符宽度（标签计入）贪心折行，取使 <p>/<li> 命中最多的一档。"""
    def wrap_src(flat, width):
        toks = flat.split(" ")
        lines, cur = [], toks[0]
        for tk in toks[1:]:
            if len(cur) + 1 + len(tk) > width:
                lines.append(cur)
                cur = tk
            else:
                cur += " " + tk
        lines.append(cur)
        return "\n".join(lines)

    samples = []
    for m in re.finditer(r"<p>\n(.*?)</p>", art_inner, re.S):
        if "<p>" in m.group(1):
            continue
        samples.append(m.group(1))
    for m in re.finditer(r"<li>(.*?)</li>", art_inner, re.S):
        if "<li>" in m.group(1):
            continue
        samples.append(m.group(1))
    if not samples:
        return None
    flows = [re.sub(r"\n", " ", s) for s in samples]
    best = (0, None)
    for w in range(60, 85):
        n = sum(1 for s, fl in zip(samples, flows) if wrap_src(fl, w) == s)
        if n > best[0]:
            best = (n, w)
    return best[1]


def _cut_region(s, start_pat, end_pat):
    m1 = re.search(start_pat, s)
    if not m1:
        return s
    m2 = re.search(end_pat, s[m1.end():])
    return s[:m1.start()] + s[m1.end() + (m2.end() if m2 else 0):]


def _count_word(text, needle):
    """同 R 侧一致的出现计数（词界判定），用于定义“第 n 次出现”。"""
    if not needle:
        return 0
    pat = "(?<![A-Za-z0-9])" + re.escape(needle) + "(?![A-Za-z0-9])"
    return len(re.findall(pat, text))


def extract_links(art_inner):
    """C 丢弃的内部链接（跨词条 ../slug/、页内 #anchor），文档序＋出现序。

    扫描域＝正文区（剔 TOC／学术工具／相关条目三块——它们各有专用账）。
    nth＝该锚文在本文可见文字流中的第几次出现（0 基），R 按此定位，
    避免同文多处时把链接挂错位置（advance-directives 判例）。"""
    s = art_inner
    s = _cut_region(s, '<div id="toc"', '</div>' + chr(92) + 's*(?=<div id="main-text">)')
    s = _cut_region(s, '<div id="academic-tools"', '</div>')
    s = _cut_region(s, '<div id="related-entries"', '</div>')
    out = []
    for m in re.finditer('<a href="([^"]*)">(.*?)</a>', s, re.S):
        href, inner = m.group(1), m.group(2)
        if href.startswith(("http://", "https://", "notes.html#")):
            continue
        if not (href.startswith("../") or href.startswith("#")):
            continue
        text = htmllib.unescape(re.sub("<[^>]*>", "", inner)).strip()
        if not text:
            continue
        prefix = htmllib.unescape(re.sub("<[^>]*>", "", s[:m.start()]))
        out.append({"text": text, "href": href, "nth": _count_word(prefix, text)})
    return out


def extract_italics(art_inner):
    """按件斜体标签形：H0 全用 <i> 时记 "i"（C 把 <em>/<i> 同归一为 *…*）。"""
    BS = chr(92)
    n_i = len(re.findall("<i[" + BS + "s>]", art_inner))
    n_em = len(re.findall("<em[" + BS + "s>]", art_inner))
    return "i" if n_i and not n_em else None


def extract_greek_form(art_inner):
    """按件希腊字形态：H0 用 <em>&alpha;</em> 而非宏时记 "em"。"""
    BS = chr(92)
    rng = "[" + chr(0x370) + "-" + chr(0x3ff) + "]"
    n_ent = len(re.findall("<em>" + BS + "s*&[A-Za-z]+;" + BS + "s*</em>", art_inner))
    n_uni = len(re.findall("<em>" + BS + "s*" + rng + BS + "s*</em>", art_inner))
    n_macro = len(re.findall("[(]" + BS + BS + "[A-Za-z]+[)]", art_inner))
    return "em" if (n_ent or n_uni) and not n_macro else None


def extract_note_forms(art_inner):
    """脚注引用形账：H0 全部 `notes.html#note-N` 引用按**文档序**记列表。

    同一 note 键可既有规范脚注又有散文原形（agent-modeling 判例），且 md
    的 `[^note-N]` 出现序＝H0 引用序（C 保序），故全量记账、R 侧游标逐个
    消费：规范形记 form=None（R 出默认 sup 形），散文原形记原片段。
    规范形判据：前缀 `<sup>[` 且锚文＝N（带 id 属性亦算规范，属性差由
    标记层补丁吸收）。"""
    out = []
    for m in re.finditer(
            r'<a href="notes\.html#note-([^"]+)"[^>]*>(.*?)</a>', art_inner,
            re.S):
        n, inner = m.group(1), m.group(2)
        pre = art_inner[max(0, m.start() - 40):m.start()]
        if re.search(r"<sup>\[$", pre) and inner.strip() == n:
            out.append({"n": n, "form": None})
        else:
            out.append({"n": n, "form": m.group(0)})
    return out


def extract_toc(art_inner):
    """TOC 块逐字（导航区：题与锚皆由正文派生，另设一致性核对）。"""
    m = re.search(r'<div id="toc".*?(?=<div id="main-text">)', art_inner, re.S)
    return m.group(0) if m else None


MD_DEF_RE = re.compile(r"^\[\^([^\]\s]+)\]:(.*)$", re.M)
SUP_MAP = getattr(__import__("yuanwen"), "SUP_MAP", {})
SUB_MAP = getattr(__import__("yuanwen"), "SUB_MAP", {})


def norm_md(s):
    """md 定义行 → 可见文（去链接包裹/星号/上下标字形）。

    URL 可含一级圆括号（`ERInt.2013(1(2)).pdf` 实证，al-farabi-logic 文献
    条目匹配失败判例），故 URL 组允许括号对。"""
    t = re.sub(r"\[((?:[^\[\]]|\[[^\[\]]*\])*)\]"
               r"\(((?:[^()\s]|\([^()]*\))*)\)", r"\1", s)
    t = t.replace("*", "")
    rev = {v: k for k, v in list(SUP_MAP.items()) + list(SUB_MAP.items())}
    if rev:
        cls = "".join(__import__("re").escape(c) for c in rev)

        def rep(m):
            return "".join(rev[c] for c in m.group(0))

        t = re.sub("[%s]+" % cls, rep, t)
    return re.sub(r"\s+", " ", htmllib.unescape(t)).strip()


def norm_html(s):
    """H0 li → 可见文（剥标签）。"""
    return re.sub(r"\s+", " ", htmllib.unescape(
        re.sub(r"<[^>]*>", "", s))).strip()


BI_START = re.compile(r"<h([2-6])[^>]*>|<ul[^>]*>|<p>", re.S)


def _match_close(region, start, open_pat, close_pat):
    """从 start 起按深度扫描，返回 [(内容起, 内容止, 标签止)] 的顶层块。"""
    depth = 1
    j = None
    for t in re.finditer(open_pat + "|" + close_pat, region):
        if t.start() < start:
            continue
        depth += 1 if re.match(open_pat, t.group(0)) else -1
        if depth == 0:
            j = t
            break
    return j


def split_items(inner):
    """顶层 <li> 内容表（支持条目内嵌套列表）。"""
    out = []
    for m in re.finditer(r"<li([^>]*)>", inner):
        t = _match_close(inner, m.end(), r"<li[^>]*>", r"</li>")
        end = t.start() if t else len(inner)
        out.append((m.group(1), inner[m.end():end]))
    return out


def scan_bib(region):
    """文献区按文档序解析 → [("h", level, inner) | ("ul", [(attrs, inner)]) | ("p", inner)]"""
    out = []
    i = 0
    while i < len(region):
        m = BI_START.search(region, i)
        if not m:
            break
        if m.group(1) is not None:
            close = "</h%s>" % m.group(1)
            e = region.find(close, m.end())
            out.append(("h", int(m.group(1)), region[m.end():e]))
            i = e + len(close)
        elif m.group(0).startswith("<ul"):
            t = _match_close(region, m.end(), r"<ul[^>]*>", r"</ul>")
            if not t:
                break
            out.append(("ul", split_items(region[m.end():t.start()])))
            i = t.end()
        else:
            e = region.find("</p>", m.end())
            out.append(("p", region[m.end():e]))
            i = e + 4
    return out


def _tree_nodes(inner, md_plain, used):
    """ul 内层 → [{i, u, c}] 节点表（i＝md 定义序，u＝子 ul 属性，c＝子节点）。

    父项匹配用“剥净嵌套 ul 后的本层文字”——否则子项文字混入父项可见文。"""
    nodes = []
    for attrs, sub in split_items(inner):
        kids = []
        rest = ""
        pos = 0
        for m in re.finditer("<ul([^>]*)>", sub):
            t = _match_close(sub, m.end(), "<ul[^>]*>", "</ul>")
            if not t:
                continue
            kids.append((m.group(1), sub[m.end():t.start()]))
            rest += sub[pos:m.start()]
            pos = t.end()
        rest += sub[pos:]
        vis = norm_html(rest)
        idx = next((k for k, t in enumerate(md_plain)
                    if k not in used and t == vis), None)
        if idx is None:
            vis2 = norm_html(sub)
            idx = next((k for k, t in enumerate(md_plain)
                        if k not in used and t == vis2), None)
        if idx is not None:
            used.add(idx)
        node = {"i": idx}
        for attrs2, inner2 in kids:
            node.setdefault("u", (attrs2 or "").strip())
            node.setdefault("c", []).extend(_tree_nodes(inner2, md_plain, used))
        nodes.append(node)
    return nodes


def extract_bib_tree(art_inner, md_defs):
    """文献区嵌套结构账：每 ul 的节点树（纯整数＋ul 属性）。"""
    bib = re.search('<div id="bibliography">(.*?)' + chr(10) + '</div> ',
                    art_inner, re.S)
    if not bib:
        return None
    md_plain = [norm_md(t) for t in md_defs]
    used = set()
    uls = []
    for blk in scan_bib(bib.group(1)):
        if blk[0] != "ul":
            continue
        inner = "<li>".join("")  # 占位，不会用到
        # 从扫描块重建原始 inner：把 (attrs, inner) 拼回
        raw = "".join("<li%s>%s</li>" % (a or "", b) for a, b in blk[1])
        uls.append({"nodes": _tree_nodes(raw, md_plain, used)})
    return uls or None


def extract_bib_indices(art_inner, md_defs):
    """文献条目在 md 定义序中的位置账（分节序，纯整数）＋ li id 属性表。

    条目匹配用可见文等值（norm_md ↔ norm_html）；li 的 id 只记属性、不记散文。"""
    bib = re.search('<div id="bibliography">(.*?)' + chr(10) + '</div> ',
                    art_inner, re.S)
    if not bib:
        return None
    plain = [norm_md(t) for t in md_defs]
    used, ids = set(), {}
    sections, cur = [], None
    for blk in scan_bib(bib.group(1)):
        if blk[0] == "h":
            if cur is not None:
                sections.append(cur)
            cur = []
            continue
        if blk[0] != "ul":
            continue
        if cur is None:
            cur = []
        for attrs, inner in blk[1]:
            vis = norm_html(inner)
            idx = next((i for i, t in enumerate(plain)
                        if i not in used and t == vis), None)
            cur.append(idx)
            if idx is not None:
                used.add(idx)
                m = re.search('id="([^"]*)"', attrs or "")
                if m:
                    ids[idx] = m.group(1)
    if cur is not None:
        sections.append(cur)
    return sections, ids


def extract_bib_seq(art_inner, md):
    """文献区块序账：[[kind, idx], …]，kind ∈ h/p/pd/ul（纯整数＋结构位）。"""
    if not md:
        return None
    bib = re.search('<div id="bibliography">(.*?)' + chr(10) + '</div> ',
                    art_inner, re.S)
    if not bib:
        return None
    NL = chr(10)
    reg = re.search("^## References[^" + NL + "]*" + NL + "(.*?)(?=^## )",
                    md, re.S | re.M)
    if not reg:
        return None
    md_heads, md_prose = [], []
    for ln in reg.group(1).split(NL):
        s2 = ln.strip()
        if not s2 or s2.startswith(">") or MD_DEF_RE.match(ln):
            continue
        m = re.match(r"^(#{3,6})\s+(.*)$", s2)
        if m:
            md_heads.append(norm_md(m.group(2)))
            continue
        md_prose.append(norm_md(s2))
    defs = [m.group(2).strip() for m in MD_DEF_RE.finditer(md)
            if not m.group(1).startswith("note-")]
    defs_plain = [norm_md(t) for t in defs]
    used, seq = set(), []
    hi = pi = 0
    for blk in scan_bib(bib.group(1)):
        if blk[0] == "h":
            vis = norm_html(blk[2])
            idx = next((i for i in range(hi, len(md_heads))
                        if md_heads[i] == vis), None)
            if idx is not None:
                hi = idx + 1
            seq.append(["h", idx])
        elif blk[0] == "ul":
            ids = []
            for attrs, inner in blk[1]:
                vis = norm_html(inner)
                idx = next((i for i, t in enumerate(defs_plain)
                            if i not in used and t == vis), None)
                ids.append(idx)
                if idx is not None:
                    used.add(idx)
            seq.append(["ul", ids])
        else:
            vis = norm_html(blk[1])
            idx = next((i for i in range(pi, len(md_prose))
                        if md_prose[i] == vis), None)
            if idx is not None:
                pi = idx + 1
                seq.append(["p", idx])
                continue
            di = next((i for i, t in enumerate(defs_plain)
                       if i not in used and t == vis), None)
            if di is not None:
                used.add(di)
            seq.append(["pd", di])
    return seq


def extract_tables(art_inner):
    """表格结构账：每表的开标签属性、thead/tbody 有无、逐行逐格标签形。

    单元格文字不入账（只记 th/td/空位三类位形）；行数与格数与 H0 一致才可用。"""
    out = []
    for m in re.finditer(r"<table([^>]*)>", art_inner):
        open_tag = m.group(1)
        end = art_inner.find("</table>", m.end())
        if end < 0:
            continue
        seg = art_inner[m.end():end]
        thead = "<thead>" in seg
        tbody = "<tbody>" in seg
        rows = []
        for r in re.finditer(r"<tr[^>]*>(.*?)</tr>", seg, re.S):
            cells = []
            for c in re.finditer("<t([hd])[^>]*>(.*?)</t[hd]>", r.group(1), re.S):
                if not c.group(2).strip():
                    cells.append("x")
                else:
                    cells.append(c.group(1))
            rows.append(cells)
        th_rows = 0
        tm = re.search("<thead>(.*?)</thead>", seg, re.S)
        if tm:
            th_rows = len(re.findall("<tr", tm.group(1)))
        out.append({"attrs": open_tag, "thead": thead, "tbody": tbody,
                    "thead_rows": th_rows, "rows": rows})
    return out


def extract_greek(art_inner):
    """按件希腊宏账：同形不同名（phi/varphi 等）者按出现序记宏名表。

    单一名与 GREEK_UNI 默认相同的字形不入账（默认规则已覆盖）。"""
    GREEK_UNI = getattr(__import__("yuanwen"), "GREEK_UNI", {})
    rev = {}
    for k, v in GREEK_UNI.items():
        rev.setdefault(v, []).append(k)
    seq = {}
    pat = chr(92) * 2 + "(" + "([A-Za-z]+)" + ")"
    matcher = re.compile(pat)
    for m in matcher.finditer(art_inner):
        name = m.group(1)
        for cp, names in rev.items():
            if name in names:
                seq.setdefault(cp, []).append(name)
                break
    out = {}
    for cp, names in seq.items():
        canon = (rev.get(cp) or [None])[0]
        if len(rev.get(cp, [])) > 1 or names[0] != canon:
            out[cp] = names
    return out


def extract(art_inner, md=None):
    led = {}
    heads = []
    for m in HEAD_RE.finditer(art_inner):
        txt = re.sub(r"<[^>]*>", "", m.group(3)).strip()
        heads.append({"level": int(m.group(1)), "text": htmllib.unescape(txt),
                      "id": hid_form(m.group(2), m.group(3))})
    led["hids"] = heads
    # 文献分节账：标题级别＋该节条目数（文献区题可为 h3/h4，条目与题交错）
    bib = re.search(r'<div id="bibliography">(.*?)\n</div> ', art_inner, re.S)
    if bib:
        secs, pend, n = [], None, 0
        for m in re.finditer(r'<h([2-6])[^>]*>(.*?)</h\1>|<ul[^>]*>(.*?)</ul>',
                             bib.group(1), re.S):
            if m.group(1) is not None:
                if pend is not None:
                    secs.append([pend, n])
                pend, n = int(m.group(1)), 0
            else:
                n += len(re.findall(r"<li>", m.group(3)))
        if pend is not None:
            secs.append([pend, n])
        led["bib_sections"] = secs
        led["bib_groups"] = [x[1] for x in secs]
        if md:
            defs = [m.group(2).strip() for m in MD_DEF_RE.finditer(md)
                    if not m.group(1).startswith("note-")]
            got = extract_bib_indices(art_inner, defs)
            if got:
                idx, ids = got
                if idx is not None:
                    led["bib_indices"] = idx
                if ids:
                    led["bib_ids"] = {str(k): v for k, v in ids.items()}
            seq = extract_bib_seq(art_inner, md)
            if seq is not None:
                led["bib_seq"] = seq
            tree = extract_bib_tree(art_inner, defs)
            if tree:
                led["bib_tree"] = tree
    # 相关条目
    rel = re.search(r'<div id="related-entries">.*?<p>(.*?)</p>', art_inner, re.S)
    if rel:
        items = []
        for part in re.split(r"\s*\|\s*", rel.group(1)):
            part = part.strip()
            if not part:
                continue
            m = re.match(r'<!--<a href="([^"]*)">-->(.*?)<!--</a>-->',
                         part, re.S)
            if m:
                items.append({"kind": "dead", "href": m.group(1),
                              "text": htmllib.unescape(
                                  re.sub(r"<[^>]*>", "", m.group(2)))})
                continue
            m = re.match(r'<a href="([^"]*)"[^>]*>(.*?)</a>', part, re.S)
            if m:
                items.append({"kind": "a", "href": m.group(1),
                              "text": htmllib.unescape(
                                  re.sub(r"<[^>]*>", "", m.group(2)))})
                continue
            # 无链接项（上游本就未链接的关注条目，aesthetics-race 实证七处）
            items.append({"kind": "text",
                          "text": htmllib.unescape(
                              re.sub(r"<[^>]*>", "", part))})
        led["rel_items"] = items
        # 尾随竖线（aesthetics-race 判例：H0 末项后仍有 ` |`）
        led["rel_trailing"] = bool(re.search(r"\|\s*$", rel.group(1)))
    # 学术工具图标
    acad = re.search(r'<table class="vert-top">(.*?)</table>', art_inner, re.S)
    if acad:
        icons = []
        for m in re.finditer(r'<tr>\s*<td>(.*?)</td>\s*<td>', acad.group(1), re.S):
            cell = m.group(1)
            im = re.search(r'src="\.\./\.\./symbols/([^"]*)"\s+alt="([^"]*)"', cell)
            icons.append([im.group(1), im.group(2)] if im else ["", ""])
        led["acad_icons"] = icons
    tb = extract_tables(art_inner)
    if tb:
        led["tables"] = tb
    gk = extract_greek(art_inner)
    if gk:
        led["greek"] = gk
    led["entities"] = extract_entities(art_inner)
    led["links"] = extract_links(art_inner)
    it = extract_italics(art_inner)
    if it:
        led["italics"] = it
    gf = extract_greek_form(art_inner)
    if gf:
        led["greek_form"] = gf
    nf = extract_note_forms(art_inner)
    if nf:
        led["note_forms"] = nf
    toc = extract_toc(art_inner)
    if toc:
        led["toc_block"] = toc
    w = wrap_width(art_inner)
    if w:
        led["wrap_width"] = w
    return led


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args(argv)
    entries = {}
    n_no = 0
    base = {}
    bpath = repo_path("baseline", "entries.json")
    if os.path.exists(bpath):
        base = {r["slug"]: r for r in json.load(
            io.open(bpath, encoding="utf-8"))["entries"] if r.get("slug")}
    for d in sorted(os.listdir(repo_path("en"))):
        p = repo_path("en", d, "index.html")
        if not os.path.exists(p):
            continue
        t = read(p)
        if B1 not in t or E1 not in t:
            continue
        md = None
        zhip = (base.get(d) or {}).get("zh_doc")
        if zhip:
            mp = repo_path("yuanwen", zhip)
            if os.path.exists(mp):
                md = io.open(mp, encoding="utf-8").read()
        led = extract(inner_article(t), md)
        if not led.get("bib_groups") and not led.get("rel_items"):
            n_no += 1
        entries[d] = led
    sys.stderr.write("[ledger] %d 件；缺区段 %d\n" % (len(entries), n_no))
    if args.check:
        return 0
    payload = {"schema": "sep-cn-article-ledger/1",
               "generated_by": "specs/053 bin/article_ledger.py",
               "note": "正文段结构补集：只承载结构（标题 id 形态/文献切分/链接目标/图标），禁含散文",
               "entries": entries}
    with io.open(repo_path(*LEDGER_PATH), "w", encoding="utf-8", newline="\n") as f:
        json.dump(payload, f, ensure_ascii=False, indent=1)
        f.write("\n")
    sys.stderr.write("[ledger] 写出 %s\n" % repo_path(*LEDGER_PATH))
    return 0


if __name__ == "__main__":
    sys.exit(main())
