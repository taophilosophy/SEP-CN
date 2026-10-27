# -*- coding: utf-8 -*-
"""词条 HTML 结构解析器（契约来源：specs/001-sep-sync-pipeline/spec.md
"网站结构事实基础"，2026-10-26 九词条完整抽样固化）。

标记契约：
- 正文范围：``<!-- BEGIN ARTICLE HTML -->`` … ``<!-- END ARTICLE HTML -->``
- 版本元数据：``<div id="pubinfo"><em>First published …; substantive revision …</em></div>``
- 分节：``<h2><a id="锚">N. 标题</a></h2>``（h3/h4 同理，节号 N[.M[.K]]）
- 图：``<div class="figure">`` 内 ``<img src="相对路径">`` + ``<span class="figlabel">Figure N</span>``
- 脚注引用：``<sup>[<a href="notes.html#N">N</a>]</sup>``
- 引用元数据：``<meta name="citation_title|citation_author" …>``
- 补充材料：正文内指向同目录 ``*.html`` 的相对链接
"""
import re
from html import unescape
from html.parser import HTMLParser

HEAD_RE = re.compile(r"<!--\s*BEGIN ARTICLE HTML\s*-->", re.I)
TAIL_RE = re.compile(r"<!--\s*END ARTICLE HTML\s*-->", re.I)
PUBINFO_RE = re.compile(
    r"First published\s+(?:\w{3},?\s+)?(\w{3} \d{1,2}, \d{4})"
    r"(?:;\s*substantive revision\s+(?:\w{3},?\s+)?(\w{3} \d{1,2}, \d{4}))?", re.I)
SECNO_RE = re.compile(r"^(\d+(?:\.\d+)*)\.?\s+")
META_RE = re.compile(r'<meta name="(citation_title|citation_author)" content="([^"]*)"')
FIG_RE = re.compile(r'<span class="figlabel">(Figure [^<]*)</span>', re.I)
NOTE_REF_RE = re.compile(r'<a href="notes\.html#([A-Za-z0-9_-]+)"', re.I)
SUPP_HREF_RE = re.compile(r'<a href="([a-z0-9][a-z0-9._-]*\.html)"', re.I)
IMG_RE = re.compile(r'<img[^>]*\ssrc="([^"]+)"[^>]*>', re.I)
ALT_RE = re.compile(r'\salt="([^"]*)"')
TAG_RE = re.compile(r"<[^>]+>")

_OPEN_BLOCK = {"h1", "h2", "h3", "h4", "p", "blockquote", "table", "li", "dt", "dd", "pre"}


class _BlockParser(HTMLParser):
    """把正文切成块序列。自闭合策略：块由其自身结束标签关闭；
    div#pubinfo 由配对 div 关闭；figure 容器内的 img/figlabel 单独成块。"""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.blocks = []
        self.cur = None          # dict(type, attrs, parts, div_depth, anchor)
        self.in_figure = False
        self.in_figlabel = False
        self._figlabel_parts = []

    # -- helpers ----------------------------------------------------------
    def _open(self, btype, attrs):
        self.cur = {"type": btype, "attrs": attrs, "parts": [], "div_depth": 0,
                    "anchor": attrs.get("id")}

    def _close(self):
        cur, self.cur = self.cur, None
        text = re.sub(r"\s+", " ", "".join(cur["parts"])).strip()
        if cur["type"] in ("h2", "h3", "h4"):
            m = SECNO_RE.match(text)
            self.blocks.append({"type": cur["type"],
                                "section": m.group(1) if m else None,
                                "anchor": cur["anchor"], "text": text})
        elif cur["type"] == "pubinfo":
            m = PUBINFO_RE.search(text)
            if m:
                self.blocks.append({"type": "pubinfo", "first_published": m.group(1),
                                    "substantive_revision": m.group(2)})
        elif cur["type"] == "table":
            self.blocks.append({"type": "table", "text": text, "anchor": cur["anchor"]})
        elif text:
            self.blocks.append({"type": cur["type"], "text": text,
                                "anchor": cur["anchor"]})

    # -- parser hooks ------------------------------------------------------
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if self.cur is not None:
            if tag == "div":
                self.cur["div_depth"] += 1
            elif tag == "a" and "id" in a and self.cur["anchor"] is None:
                self.cur["anchor"] = a["id"]
            elif tag == "img":
                self.cur["parts"].append(" ")
        elif tag in _OPEN_BLOCK:
            self._open(tag, a)
        elif tag == "div":
            ident = a.get("id") or ""
            cls = a.get("class") or ""
            if ident == "pubinfo":
                self._open("pubinfo", a)
            elif "figure" in cls:
                self.in_figure = True
        elif tag == "span" and "figlabel" in (a.get("class") or ""):
            self.in_figlabel = True
            self._figlabel_parts = []

    def handle_startendtag(self, tag, attrs):
        if tag == "img":
            a = dict(attrs)
            if self.cur is not None:
                self.cur["parts"].append(" ")
            elif self.in_figure:
                self.blocks.append({"type": "img", "src": a.get("src", ""),
                                    "alt": a.get("alt", "")})

    def handle_endtag(self, tag):
        if self.cur is not None:
            if tag == "div":
                self.cur["div_depth"] -= 1
                if self.cur["div_depth"] < 0:
                    self._close()
            elif tag == self.cur["type"] and self.cur["type"] != "pubinfo":
                self._close()
            elif tag == "table" and self.cur["type"] == "table":
                self._close()
        elif self.in_figure and tag == "div":
            self.in_figure = False

    def handle_data(self, data):
        if self.cur is not None:
            self.cur["parts"].append(data)
        elif self.in_figlabel:
            self._figlabel_parts.append(data)


def parse_entry(html_text):
    """解析词条页 → 结构化字典（不落盘，供 fetch_entry/extract_text 使用）。"""
    m = HEAD_RE.search(html_text)
    end = TAIL_RE.search(html_text)
    article = html_text[m.end():end.start()] if (m and end) else html_text
    in_article = bool(m and end)

    bp = _BlockParser()
    bp.feed(article)
    bp.close()
    blocks = bp.blocks

    # figlabel 归并：FIG_RE 依序匹配，逐个挂到尚未有 figlabel 的 img 块上
    fig_iter = iter(FIG_RE.findall(article))
    for b in blocks:
        if b["type"] == "img":
            try:
                b["figlabel"] = next(fig_iter).strip()
            except StopIteration:
                break

    notes_refs = sorted(set(NOTE_REF_RE.findall(article)))
    supplements = sorted({h for h in SUPP_HREF_RE.findall(article)
                          if h not in ("index.html", "notes.html")})
    images = []
    for im in IMG_RE.finditer(article):
        src = im.group(1)
        if src.startswith(("../", "http:", "https:", "/")):
            continue  # 站点框架图（symbols/*）与外链不算词条资产
        images.append({"src": src, "alt": (ALT_RE.search(im.group(0)) or [None, ""])[1]})

    title_m = META_RE.search(html_text)
    authors = re.findall(r'<meta name="citation_author" content="([^"]*)"', html_text)

    return {
        "in_article_markers": in_article,
        "title": unescape(title_m.group(2)) if title_m else None,
        "authors": [unescape(a) for a in authors],
        "blocks": blocks,
        "notes_refs": notes_refs,
        "supplements": supplements,
        "images": images,
    }


def parse_archinfo(html_text):
    """解析 archinfo.cgi 输出 → {latest_edition, latest_change_type, history[]}。"""
    text = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html_text))
    out = {"latest_edition": None, "latest_change_type": None, "history": []}
    m = re.search(r"following archive edition:\s*((Spring|Summer|Fall|Winter) \d{4})"
                  r"\s*\(([^)]*)\)", text)
    if m:
        out["latest_edition"] = m.group(1)
        out["latest_change_type"] = m.group(3).strip()
    for hm in re.finditer(r"((Spring|Summer|Fall|Winter) \d{4})\s*\(([^)]*)\)", text):
        if hm.group(1) != out["latest_edition"]:
            out["history"].append({"edition": hm.group(1), "change_type": hm.group(3).strip()})
    return out


class _CatalogHTMLParser(HTMLParser):
    """contents.html 结构化解析：按 <li> 栈捕获，父条目遇嵌套 <ul> 即冻结自身文本。

    修复 2026-10-27 发现的嵌套吞没缺陷：旧正则 ``<li[^>]*>(.*?)</li>`` 的非贪婪
    匹配跨越嵌套边界，把每个集群的第一个子词条吞进父条目匹配（64 条丢失，
    如 altruism-biological、kant-reason、shared-agency）。
    """
    SEE_RE = re.compile(r"(?:\u2014|&mdash;|\u2013)\s*see\b", re.I)

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.items = []
        self.depth = 0
        self.stack = []

    def handle_starttag(self, tag, attrs):
        if tag == "ul":
            self.depth += 1
            if self.stack:
                self.stack[-1]["frozen"] = True
        elif tag == "li":
            self.stack.append({"frozen": False, "slug": None, "strong": [],
                               "linktext": [], "post": [], "raw": [],
                               "in_a": False, "in_strong": False})
        elif tag == "a" and self.stack and not self.stack[-1]["frozen"]:
            fr = self.stack[-1]
            if fr["slug"] is None:
                m = re.search(r"entries/([^/\"]+)/?$", dict(attrs).get("href") or "")
                if m:
                    fr["slug"] = m.group(1)
                    fr["in_a"] = True
        elif tag == "strong" and self.stack and self.stack[-1]["in_a"]:
            self.stack[-1]["in_strong"] = True

    def handle_endtag(self, tag):
        if tag == "a" and self.stack:
            fr = self.stack[-1]
            if fr["in_a"]:
                fr["in_a"] = False
                fr["in_strong"] = False
        elif tag == "strong" and self.stack:
            self.stack[-1]["in_strong"] = False
        elif tag == "ul":
            self.depth = max(0, self.depth - 1)
        elif tag == "li" and self.stack:
            self._finish(self.stack.pop())

    def handle_data(self, data):
        for fr in self.stack:
            if fr["frozen"]:
                continue
            fr["raw"].append(data)
            if fr["in_a"]:
                fr["linktext"].append(data)
                if fr["in_strong"]:
                    fr["strong"].append(data)
            elif fr["slug"] is not None:
                fr["post"].append(data)

    def close(self):
        super().close()
        while self.stack:
            self._finish(self.stack.pop())

    def _finish(self, fr):
        if fr["slug"] is None:
            return
        raw = "".join(fr["raw"])
        title = "".join(fr["strong"]).strip() or "".join(fr["linktext"]).strip()
        if self.SEE_RE.search(raw):
            low = raw.lower()
            i = low.find("see")
            before = raw[:i].strip().rstrip("—–- ") if i >= 0 else title
            self.items.append({"slug": fr["slug"], "title": before or title,
                               "authors": [], "alias_of": fr["slug"],
                               "level": self.depth})
        else:
            authors = "".join(fr["post"]).strip().strip("() ").strip()
            self.items.append({"slug": fr["slug"], "title": title,
                               "authors": authors or [], "alias_of": None,
                               "level": self.depth})


def parse_catalog(html_text):
    """解析 contents.html → [{slug,title,authors,alias_of,level}]。

    实测格式（2026-10-26 快照）：
      正常词条: <li> <a href="entries/slug/"><strong>title</strong></a> (Author) </li>
      别名词条: <li> 别名 &mdash; see <a href="entries/target/"><strong>目标</strong></a> </li>
      子词条:   集群母词条下嵌套 <ul>（子词条 level = 父 level + 1）

    两遍归并：正常词条按 slug 占键；别名词并入目标记录的 aliases；
    无正常词条对应的别名独立成条（如 recursion — see recursion 的梗词条）。
    """
    p = _CatalogHTMLParser()
    p.feed(html_text)
    p.close()
    by_slug = {}
    for it in p.items:
        if not it["alias_of"]:
            by_slug[it["slug"]] = it
    standalone = {}
    for it in p.items:
        if it["alias_of"]:
            tgt = it["alias_of"]
            rec = by_slug.get(tgt)
            if rec is not None:
                rec.setdefault("aliases", []).append(it["title"])
            else:
                standalone.setdefault(tgt, it)
    out = list(by_slug.values()) + list(standalone.values())
    out.sort(key=lambda x: x["slug"])
    return out
