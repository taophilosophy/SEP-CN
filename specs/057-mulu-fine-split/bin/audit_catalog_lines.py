#!/usr/bin/env python3
"""specs/057 s3u：目录行逐条审计（翻译／分类／格式），输出报告供人工判读。

口径：
- mu-lu-s.md 链接行文字 = SUMMARY 同路径文字（G3 文字跟随，此处仅复核）；
- 上游权威＝baseline/catalog.json（slug→title/authors）；
- 分类参照＝条目所在标题路径（节点标题不与上游对齐，属编辑判断）。

输出 results/s3u-audit.md：
A. 格式形态异常（缺英文段、作者段缺括号、逗号分隔作者、多余空格、路径异常等）
B. 翻译对照异常（英文段与上游 title 规范化后低重合；作者集合与上游不一致）
C. 分类弱信号（条目英文题名与节点标题词零交集，供人工判读，噪声大仅作线索）
D. 全量清单（条目→节点路径，供逐条通读）
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
H = re.compile(r"^(#{1,6}) (.+?)\s*$")
E = re.compile(r"^(\s*)\* \[(.+?)\]\(([^)]+\.md)\)\s*$")
LINK_TXT = re.compile(r"^([^\[\]]*)\s([A-ZÀ-ÞĀĀ-Ŷ][^\(\)]*?)\s*\(([^()]*)\)\s*$")


def unesc(t):
    return t.replace("\\[", "[").replace("\\]", "]").replace("\\*", "*")


def norm_en(s):
    s = s.lower()
    s = re.sub(r"[^a-z0-9 ]", " ", s)
    toks = [t for t in s.split() if t not in ("the", "a", "an", "of", "in", "and", "vs")]
    return set(toks)


def parse_line(txt):
    """链接文字 → (中文段, 英文段, 作者段)；形态异常返回标记。"""
    t = unesc(txt)
    m = re.match(r"^(.*?)\s*\(([^()]*)\)\s*$", t)
    if not m:
        return t, "", "", "no-author-paren"
    head, authors = m.group(1).strip(), m.group(2).strip()
    # 英文段 = head 尾部的连续拉丁串（含隔音符、连字符、撇号、空格）
    m2 = re.search(r"([A-Za-zÀ-ÿĀ-ſ'’\-\.:\[\]/ ]*[A-Za-zÀ-ÿ])\s*$", head)
    if not m2:
        return head, "", authors, "no-english"
    en = m2.group(1).strip()
    zh = head[: m2.start()].strip()
    return zh, en, authors, ""


def main():
    catalog = json.loads((ROOT / "baseline" / "catalog.json").read_text(encoding="utf-8"))
    up = {it["slug"]: it for it in catalog["items"] if not it.get("alias_of")}

    lines = (ROOT / "mu-lu-s.md").read_text(encoding="utf-8").split("\n")
    stack, entries = [], []
    for ln, l in enumerate(lines, 1):
        m = H.match(l)
        if m:
            lv, t = len(m.group(1)), m.group(2).strip()
            while stack and stack[-1][0] >= lv:
                stack.pop()
            stack.append((lv, t))
            continue
        e = E.match(l)
        if e and len(e.group(1)) == 0:
            slug = e.group(3).rsplit("/", 1)[-1][:-3]
            entries.append(dict(ln=ln, slug=slug, txt=e.group(2),
                                path="／".join(x[1] for x in stack)))

    A, B_name, B_author, C, D = [], [], [], [], []
    for ent in entries:
        zh, en, authors, flag = parse_line(ent["txt"])
        where = f"{ent['path']}｜`{ent['slug']}`｜{ent['txt'][:60]}"
        if flag:
            A.append(f"{where} → {flag}")
        if "," in authors and "、" not in authors:
            A.append(f"{where} → 作者用逗号分隔")
        if "  " in ent["txt"] or ent["txt"] != ent["txt"].strip():
            A.append(f"{where} → 多余空格")
        it = up.get(ent["slug"])
        if it:
            a1src = authors.replace("、", "; ")
            a1src = re.sub(r"\s+and\s+", "; ", a1src)
            a2src = re.sub(r",\s*Jr\.?$", " Jr.", it.get("authors", "").strip())
            a2src = a2src.replace("; and ", "; ").replace(", ", "; ")
            a2src = re.sub(r"\s+and\s+", "; ", a2src)
            a1 = set(t.strip() for t in a1src.split(";") if t.strip())
            a2 = set(t.strip() for t in a2src.split(";") if t.strip())
            drop = {"Jr.", "Jr", "et al.", "III", "II"}
            a1 = {x.strip() for x in a1 if x.strip() and x.strip() not in drop}
            a2 = {x.strip() for x in a2 if x.strip() and x.strip() not in drop}
            a1 = {re.sub(r"^\.\s*", "", x) for x in a1}
            a2 = {re.sub(r"^\.\s*", "", x) for x in a2}
            if a1 != a2 and not (a1 <= a2 or a2 <= a1):
                B_author.append(f"{where}\n     mu-lu-s: {'、'.join(sorted(a1))}\n     上游: {'; '.join(sorted(a2))}")
            ov = norm_en(en) & norm_en(it["title"])
            if en and len(norm_en(en)) >= 2 and len(ov) / max(1, len(norm_en(en))) < 0.4:
                B_name.append(f"{where}\n     译文英文段: {en}\n     上游题名: {it['title']}")
        path_toks = norm_en(ent["path"])
        etoks = norm_en(en)
        if en and len(etoks) >= 2 and not (etoks & path_toks):
            C.append(f"{where}｜en: {en[:40]}")

    D.append("| 条目 | 节点路径 |")
    D.append("| ---- | ---- |")
    for ent in entries:
        D.append(f"| `{ent['slug']}` | {ent['path']} |")

    out = ["# s3u 目录行审计（翻译／分类／格式）", "",
           f"条目 {len(entries)}；格式异常 {len(A)}；作者不一致 {len(B_author)}；"
           f"英文题名低重合 {len(B_name)}；分类弱信号 {len(C)}（失效信号，节点标题为中文，仅留档）；",
           "全量清单按区分档至 s3u-review/", "",
           "## A. 格式形态异常", ""] + [f"- {x}" for x in A] + ["",
           "## B1. 作者集合与上游不一致", ""] + [f"- {x}" for x in B_author] + ["",
           "## B2. 英文题名与上游低重合（人工判读是否合理改写）", ""] + [f"- {x}" for x in B_name] + ["",
           "## C. 分类弱信号", "", "（信号失效：节点标题为中文，无英文词元可比；分类判读改走 s3u-review/ 全量清单人工通读，见复核记录）"]
    p = ROOT / "specs/057-mulu-fine-split/results/s3u-audit.md"
    p.write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")
    # D 全量清单按区分档（ADR-0004）
    import collections
    rd = ROOT / "specs/057-mulu-fine-split/results/s3u-review"
    rd.mkdir(parents=True, exist_ok=True)
    for old in rd.glob("*.md"):
        old.unlink()
    byz = collections.OrderedDict()
    for ent in entries:
        byz.setdefault(ent["path"].split("／")[0], []).append(ent)
    for z, es in byz.items():
        fn = rd / ("s3u-list-" + re.sub(r"[、，\s]", "", z) + ".md")
        rows = ["# 全量清单·" + z, "", "| 条目 | 节点路径 |", "| ---- | ---- |"]
        rows += [f"| `{x['slug']}` | {x['path']} |" for x in es]
        fn.write_text("\n".join(rows) + "\n", encoding="utf-8", newline="\n")
    print(f"条目 {len(entries)}；格式异常 {len(A)}；作者不一致 {len(B_author)}；"
          f"英文低重合 {len(B_name)}；分类弱信号 {len(C)}")
    print("写出", p)


if __name__ == "__main__":
    sys.exit(main())
