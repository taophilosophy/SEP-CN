#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""B3.2 页面装配：版式账抽取器（chrome 骨架＋词条字段）。

从 en/<slug>/index.html（H0）提取页面骨架可变性：
  head → headA 常量 + title 块 + meta 块（字段驱动） + head-rest（时代模板）
  bodyPre → 时代模板（{{SLUG}} 槽）
  post → 版权块（字段驱动） + post-rest（时代模板，{{SLUG}}/{{SY}} 槽）
产出：
  baseline/en-template/skeleton/{headrest,pre,postrest}-<era>.html
  baseline/en-template/page-layout.json  词条 → 时代号＋字段账（单一事实源）

派生纪律：本脚本是版式账的唯一生产者；账一经提交即冻结，重跑须经人工复核
（--check 模式只比对不落盘，供门禁/CI 使用）。
"""
import argparse
import collections
import hashlib
import io
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
from tools.common import repo_path  # noqa: E402

B1 = "<!-- BEGIN ARTICLE HTML -->"
E1 = "<!-- END ARTICLE HTML -->"
SKEL_DIR = ("baseline", "en-template", "skeleton")
LAYOUT_PATH = ("baseline", "en-template", "page-layout.json")
META_RE = re.compile(r'<meta name="([^"]*)" content="([^"]*)"')
TITLE_RE = re.compile(r"<title>\n(.*?)\n</title>\n", re.S)
COPYRIGHT_RE = re.compile(
    r'<div id="article-copyright">\n    <p>\n'
    r' <a href="\.\./\.\./info\.html#c">Copyright &copy; (\d{4})</a> by\n\n'
    r'<br />\n(.*?)\n    </p>\n  </div>\n', re.S)
OBFUSC_PREFIX = 'm&#97;ilto:'


def read(p):
    return io.open(p, encoding="utf-8", newline="").read()


def slotify(text, slug):
    """骨架槽位化：slug 只经两处已知 URL 形态入模板，其余原样保留。"""
    if not slug:
        return text
    text = text.replace("friends/preview/%s/" % slug, "friends/preview/@S@/")
    text = text.replace("archinfo.cgi?entry=%s" % slug, "archinfo.cgi?entry=@S@")
    return text.replace(slug, "@S@") if slug in text else text


def deslotify(text, slug):
    return text.replace("@S@", slug)


def split_page(t):
    """→ dict(headA, title, headmid, meta_block, metas, headrest, pre, article, post)"""
    i1 = t.index(B1)
    i2 = t.index(E1)
    pre_all = t[:i1]
    h = pre_all.index("</head>") + len("</head>")
    head, bodypre = pre_all[:h], pre_all[h:]
    tm = TITLE_RE.search(head)
    metas = list(META_RE.finditer(head))
    first = min(m.start() for m in metas if m.group(1) in
                ("citation_title", "citation_author", "DC.title"))
    last = max(m.end() for m in metas if m.group(1).startswith("DCTERMS"))
    line_end = head.index("\n", last)
    return {"headA": head[:tm.start()],
            "title": head[tm.start():tm.end()],
            "title_text": tm.group(1),
            "headmid": head[tm.end():first],
            "meta_block": head[first:line_end + 1],
            "metas": [(m.group(1), m.group(2)) for m in metas],
            "headrest": head[line_end + 1:],
            "pre": bodypre,
            "article": t[i1:i2 + len(E1)],
            "post": t[i2 + len(E1):]}


def era_id(text):
    return hashlib.sha1(text.encode("utf-8")).hexdigest()[:8]


def render_email(addr):
    href = OBFUSC_PREFIX + addr.replace("@", "&#37;40").replace(".", "&#37;2e")
    vis = ("<em>" + addr.replace("@", '<abbr title=" at ">&#64;</abbr>')
           .replace(".", '<abbr title=" dot ">&#46;</abbr>') + "</em>")
    return '&lt;<a href="%s">%s</a>&gt;' % (href, vis)


def parse_copyright(block):
    """版权块 → (year, [{display,url,email}])；解析失败返回 None。"""
    m = COPYRIGHT_RE.search(block)
    if not m:
        return None
    year, body = m.group(1), m.group(2)
    authors = []
    for ch in body.split("<br />"):
        ch = ch.strip("\n")
        if not ch:
            return None
        email = None
        om = re.search(r'&lt;<a href="' + re.escape(OBFUSC_PREFIX)
                       + r'([^"]*)"><em>(.*?)</em></a>&gt;', ch)
        if om:
            ch = ch[:om.start()] + ch[om.end():]
            email = om.group(1).replace("&#37;40", "@").replace("&#37;2e", ".")
            if render_email(email) != om.group(0):
                return None
        ch = ch.strip()
        url = None
        um = re.fullmatch(r'<a href="([^"]*)" target="other">([^<]*)</a>', ch)
        if um:
            url, disp = um.group(1), um.group(2)
        else:
            if "<" in ch or ">" in ch:
                return None
            disp = ch
        authors.append({"display": disp, "url": url, "email": email})
    return year, authors


def render_copyright(year, authors):
    """作者块：有邮箱者邮箱紧随其名（同行收尾 `<br />`）；无邮箱者 `<br />` 自成一行。"""
    chunks = []
    for a in authors:
        disp = ('<a href="%s" target="other">%s</a>' % (a["url"], a["display"])
                if a.get("url") else a["display"])
        s = disp
        if a.get("email"):
            s += "\n" + render_email(a["email"]) + "<br />"
        else:
            s += "\n<br />"
        chunks.append(s)
    body = "\n".join(chunks)
    # 末位作者不带尾随 <br />
    last = authors[-1]
    tail_keep = "\n<br />" if not last.get("email") else "<br />"
    if body.endswith("\n" + tail_keep):
        body = body[: -len("\n" + tail_keep)]
    elif body.endswith(tail_keep):
        body = body[: -len(tail_keep)]
    tail = "\n" if not last.get("email") else ""
    return ('<div id="article-copyright">\n    <p>\n'
            ' <a href="../../info.html#c">Copyright &copy; %s</a> by\n\n'
            '<br />\n%s%s\n    </p>\n  </div>\n'
            % (year, body, tail))


def render_meta_block(fields):
    out = ['<meta name="citation_title" content="%s" />' % fields["title_meta"]]
    for a in fields["meta_authors"]:
        out.append('<meta name="citation_author" content="%s" />' % a)
    out.append('<meta name="citation_publication_date" content="%s" />'
               % fields["pub_date"])
    out.append('<meta name="DC.title" content="%s" />' % fields["title_meta"])
    for a in fields["meta_authors"]:
        out.append('<meta name="DC.creator" content="%s" />' % a)
    out.append('<meta name="DCTERMS.issued" content="%s" />' % fields["issued"])
    out.append('<meta name="DCTERMS.modified" content="%s" />' % fields["modified"])
    return "\n".join(out) + "\n"


def extract(paths):
    eras = {"headrest": {}, "pre": {}, "postrest": {}, "headmid": {}}
    headA = {}
    layout = {}
    anom = collections.Counter()
    for p in paths:
        slug = os.path.basename(os.path.dirname(p))
        t = read(p)
        if B1 not in t or E1 not in t:
            anom["no-marker"] += 1
            continue
        sp = split_page(t)
        metas = collections.OrderedDict()
        for k, v in sp["metas"]:
            metas.setdefault(k, []).append(v)
        fields = {"title_meta": (metas.get("citation_title") or [""])[0],
                  "meta_authors": metas.get("citation_author") or [],
                  "pub_date": (metas.get("citation_publication_date") or [""])[0],
                  "issued": (metas.get("DCTERMS.issued") or [""])[0],
                  "modified": (metas.get("DCTERMS.modified") or [""])[0]}
        if render_meta_block(fields) != sp["meta_block"]:
            anom["meta-shape"] += 1
        cr = parse_copyright(sp["post"])
        if not cr:
            anom["copyright-parse"] += 1
            year, cauth = None, None
        else:
            year, cauth = cr
            if render_copyright(year, cauth) not in sp["post"]:
                anom["copyright-render"] += 1
        sy = re.search(r'copyright &copy; (\d{4})</a> by <a href="https://mally',
                       sp["post"])
        siteyear = sy.group(1) if sy else ""
        e_head = era_id(sp["headrest"])
        e_pre = era_id(slotify(sp["pre"], slug))
        postrest = sp["post"]
        if cr:
            postrest = postrest.replace(render_copyright(year, cauth), "@CR@")
        postrest = slotify(postrest, slug).replace(
            '<a href="../../info.html#c">Copyright &copy; %s</a>' % siteyear,
            '<a href="../../info.html#c">Copyright &copy; @SY@</a>')
        e_post = era_id(postrest)
        e_mid = era_id(sp["headmid"])
        eras["headrest"].setdefault(e_head, sp["headrest"])
        eras["pre"].setdefault(e_pre, slotify(sp["pre"], slug))
        eras["postrest"].setdefault(e_post, postrest)
        eras["headmid"].setdefault(e_mid, sp["headmid"])
        headA.setdefault(era_id(sp["headA"]), sp["headA"])
        layout[slug] = {
            "slug": slug, "title_meta": fields["title_meta"],
            "title_html": sp["title"], "meta_authors": fields["meta_authors"],
            "pub_date": fields["pub_date"], "issued": fields["issued"],
            "modified": fields["modified"], "headA_id": era_id(sp["headA"]),
            "era": {"headrest": e_head, "pre": e_pre, "postrest": e_post,
                    "headmid": e_mid},
            "copyright_year": year, "copyright_authors": cauth,
            "site_year": siteyear,
        }
    return headA, eras, layout, anom


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--slugs", nargs="*")
    args = ap.parse_args(argv)
    if args.slugs:
        paths = [repo_path("en", s, "index.html") for s in args.slugs]
    else:
        paths = [repo_path("en", d, "index.html") for d in sorted(os.listdir(
            repo_path("en"))) if os.path.isdir(repo_path("en", d))]
    paths = [p for p in paths if os.path.exists(p)]
    headA, eras, layout, anom = extract(paths)
    sys.stderr.write("[layout] %d 件；异常计数 %s\n" % (len(layout), dict(anom)))
    sys.stderr.write("[layout] headA 常量 %d 种\n" % len(headA))
    for kind, d in eras.items():
        cnt = collections.Counter(e["era"][kind] for e in layout.values())
        for k, v in sorted(d.items(), key=lambda kv: -cnt[kv[0]]):
            sys.stderr.write("[layout] %-9s %s  %5d 件  %6d B\n"
                             % (kind, k, cnt[k], len(v)))
    if args.check:
        return 0
    os.makedirs(repo_path(*SKEL_DIR), exist_ok=True)
    for kind, d in eras.items():
        for k, v in d.items():
            with io.open(repo_path(*SKEL_DIR, "%s-%s.html" % (kind, k)),
                         "w", encoding="utf-8", newline="\n") as f:
                f.write(v)
    for k, v in headA.items():
        with io.open(repo_path(*SKEL_DIR, "headA-%s.html" % k),
                     "w", encoding="utf-8", newline="\n") as f:
            f.write(v)
    payload = {"schema": "sep-cn-page-layout/1",
               "generated_by": "specs/053 bin/page_layout.py",
               "note": "页面骨架版式账：chrome 时代号＋词条字段；正文区不在本账内",
               "entries": [layout[s] for s in sorted(layout)]}
    with io.open(repo_path(*LAYOUT_PATH), "w", encoding="utf-8", newline="\n") as f:
        json.dump(payload, f, ensure_ascii=False, indent=1)
        f.write("\n")
    sys.stderr.write("[layout] 写出 %s\n" % repo_path(*LAYOUT_PATH))
    return 0


if __name__ == "__main__":
    sys.exit(main())
