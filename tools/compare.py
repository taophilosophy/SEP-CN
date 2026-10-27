# -*- coding: utf-8 -*-
"""段落级变更比较（spec 001 US-3，用户 2026-10-27 指令实现）。

对任一词条：抓取英文源最新快照（不覆盖 en/ 不可变原始物），与基线快照
en/<slug>/index.html 比较，产出段落级变更清单（新增/删除/修改/移动），
每条变更标注英文节号（锚 id + 标题）并映射到中文仓库对应 md 文档与节。

流程（FR-007/US-3）：
  1. 读 baseline 记录（zh_doc 映射与 source_sha256）；
  2. 抓取最新 HTML 到 script/tmp/compare-<slug>.html（礼貌 5 秒，不覆盖基线）；
  3. 节级拆分（h2 锚 id + 标题；首 h2 前为"导言"伪节）→ 段落规范化文本；
  4. 节集合 diff：added / removed / moved（同标题异锚）→ modified（同锚内容变）；
     modified 节内做段落级 diff（difflib，附原文摘录）；
  5. 每条变更映射中文文档：baseline.zh_doc + md 内 `## 节标题` 行号定位；
     无 zh_doc 者标注"待建任务/待译名登记"。

用法:
  python tools/compare.py <slug>...            # 抓取最新快照并与基线比较
  python tools/compare.py <slug> --html PATH   # 用指定快照比较（跳过抓取）
输出: stdout JSON {slug, changed, sections:{added,removed,moved,modified},
                   changes:[{type, anchor, title, excerpt, zh_doc, zh_section, zh_line}]}
退出码: 0 无变更/成功；1 有变更（供管线感知）；2 用法/抓取失败。
"""
import argparse
import difflib
import io
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools import fetch
from tools.common import load_json, repo_path, sha256_file, utcnow_iso

# stdout 重包守卫：CI/unittest 下可能已是被别的模块重包过的流，重复包会关闭底层 buffer
if (sys.stdout.encoding or "").lower().replace("-", "") != "utf8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

SECTION_RE = re.compile(r'<h2[^>]*>\s*<a[^>]*\bid="([^"]*)"[^>]*>(.*?)</a>\s*</h2>', re.S | re.I)
TAG_RE = re.compile(r"<[^>]+>")
HEAD_RE = re.compile(r"<!--\s*BEGIN ARTICLE HTML\s*-->", re.I)
TAIL_RE = re.compile(r"<!--\s*END ARTICLE HTML\s*-->", re.I)
SPECIAL = {"References": "References", "Academic Tools": "Academic Tools",
           "Other Internet Resources": "Other Internet Resources",
           "Related Entries": "Related Entries"}


def strip_tags(html):
    return re.sub(r"\s+", " ", TAG_RE.sub(" ", html)).strip()


def parse_sections(html):
    """词条 HTML → [(anchor, title, [段落规范化文本])…]；首 h2 前为导言伪节。"""
    m = HEAD_RE.search(html)
    e = TAIL_RE.search(html)
    article = html[m.end():e.start()] if (m and e) else html
    marks = [(mm.group(1), strip_tags(mm.group(2)), mm.start(), mm.end())
             for mm in SECTION_RE.finditer(article)]
    if not marks:
        return [("(intro)", "导言", [strip_tags(article)] if strip_tags(article) else [])]
    secs = []
    intro = strip_tags(article[:marks[0][2]])
    if intro:
        secs.append(("(intro)", "导言", [intro]))
    for i, (anchor, title, s, ee) in enumerate(marks):
        end = marks[i + 1][2] if i + 1 < len(marks) else len(article)
        body = article[ee:end]
        paras = [strip_tags(p) for p in re.findall(r"<p[^>]*>(.*?)</p>", body, re.S | re.I)]
        # 表格/列表内容整块作为一段（规范化后参与 diff）
        rest = TAG_RE.sub(" ", re.sub(r"<p[^>]*>.*?</p>", " ", body, flags=re.S | re.I))
        rest = re.sub(r"\s+", " ", rest).strip()
        if rest:
            paras.append(rest)
        paras = [p for p in paras if p]
        secs.append((anchor, title, paras))
    return secs


def diff_sections(old, new):
    """节级与段落级 diff → changes 列表。"""
    old_by = {a: (t, ps) for a, t, ps in old}
    new_by = {a: (t, ps) for a, t, ps in new}
    changes = []
    for a, t, ps in new:
        if a not in old_by:
            changes.append({"type": "added", "anchor": a, "title": t,
                            "excerpt": (ps[0][:120] if ps else "")})
    for a, t, ps in old:
        if a not in new_by:
            changes.append({"type": "removed", "anchor": a, "title": t,
                            "excerpt": (ps[0][:120] if ps else "")})
    # moved：同标题异锚
    old_titles = {t: a for a, t, _ in old}
    for a, t, ps in new:
        if a in old_by or a == "(intro)":
            continue
        if t in old_titles and old_titles[t] not in new_by:
            changes.append({"type": "moved", "anchor": a, "title": t,
                            "excerpt": "自锚 %s 移入" % old_titles[t]})
    # modified：同锚（或同标题同锚）段落文本变化
    for a, (t, ps_new) in new_by.items():
        if a not in old_by or a == "(intro)":
            continue
        ps_old = old_by[a][1]
        sm = difflib.SequenceMatcher(None, ps_old, ps_new, autojunk=False)
        for tag, i1, i2, j1, j2 in sm.get_opcodes():
            if tag == "equal":
                continue
            for k in range(i1, i2):
                changes.append({"type": "removed", "anchor": a, "title": t,
                                "excerpt": ps_old[k][:160]})
            for k in range(j1, j2):
                changes.append({"type": "added", "anchor": a, "title": t,
                                "excerpt": ps_new[k][:160]})
            if tag == "replace" and i1 == i2 and j1 == j2:
                changes.append({"type": "modified", "anchor": a, "title": t, "excerpt": ""})
    return changes


def map_zh(changes, zh_doc):
    """变更映射中文文档：md 内 `## 节标题` 行定位；无 zh_doc 标注待建任务。"""
    if not zh_doc:
        for c in changes:
            c["zh_doc"] = None
            c["zh_section"] = "待建任务/待译名登记（无对应中文文档）"
            c["zh_line"] = None
        return changes
    zh_path = repo_path(*zh_doc.split("/"))
    heads = []
    if os.path.isfile(zh_path):
        for i, line in enumerate(open(zh_path, encoding="utf-8").read().splitlines(), 1):
            hm = re.match(r"^##\s+(.*)$", line)
            if hm:
                heads.append((i, hm.group(1)))
    for c in changes:
        c["zh_doc"] = zh_doc
        hit = None
        for i, h in heads:
            hn = re.sub(r"[\s（）()]+", "", h).lower()
            tn = re.sub(r"[\s（）()]+", "", c["title"]).lower()
            if tn and (tn in hn or hn in tn):
                hit = (i, h)
                break
        if hit is None:
            for i, h in heads:
                if h.startswith(tuple(SPECIAL)) and c["title"].startswith(tuple(SPECIAL)):
                    hit = (i, h)
                    break
        c["zh_section"] = hit[1] if hit else "节未找到（标题待人工对照）"
        c["zh_line"] = hit[0] if hit else None
    return changes


def compare_slug(slug, new_html_path=None):
    base = load_json(repo_path("baseline", "entries.json"))
    rec = next((r for r in base["entries"] if r["slug"] == slug), None)
    if rec is None:
        return {"slug": slug, "error": "词条不在 baseline，先 fetch_entry.py %s" % slug}, 2
    zh_doc = rec.get("zh_doc")
    old_path = repo_path("en", slug, "index.html")
    if not os.path.isfile(old_path):
        return {"slug": slug, "error": "基线快照缺失 en/%s/index.html" % slug}, 2
    if new_html_path:
        tmp = new_html_path
    else:
        os.makedirs(repo_path("script", "tmp"), exist_ok=True)
        tmp = repo_path("script", "tmp", "compare-%s.html" % slug)
        url = fetch.BASE + "/entries/%s/" % slug
        status, data = fetch.get(url, dest=tmp, delay=fetch.MIN_DELAY)
        if status != 200:
            return {"slug": slug, "error": "抓取 HTTP %s" % status}, 2
    if sha256_file(tmp) == rec.get("yuanwen", {}).get("source_sha256"):
        return {"slug": slug, "changed": False,
                "note": "英文源与基线一致（source_sha256 相同），无变更"}, 0
    old_secs = parse_sections(open(old_path, encoding="utf-8", errors="replace").read())
    new_secs = parse_sections(open(tmp, encoding="utf-8", errors="replace").read())
    changes = map_zh(diff_sections(old_secs, new_secs), zh_doc)
    sys.stderr.write("[compare] %s: %d 处变更\n" % (slug, len(changes)))
    return {"slug": slug, "changed": bool(changes), "compared_at": utcnow_iso(),
            "new_snapshot": os.path.relpath(tmp, repo_path(".")),
            "sections_changed": len({c["anchor"] for c in changes}),
            "changes": changes}, (1 if changes else 0)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("slugs", nargs="+")
    ap.add_argument("--html", help="指定新快照 HTML（跳过抓取，仅对单 slug 有效）")
    args = ap.parse_args(argv)
    results, code = [], 0
    for slug in args.slugs:
        res, rc = compare_slug(slug, args.html if len(args.slugs) == 1 else None)
        results.append(res)
        code = max(code, rc)
    print(json.dumps({"results": results}, ensure_ascii=False, indent=2))
    return code


if __name__ == "__main__":
    sys.exit(main())
