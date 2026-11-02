# -*- coding: utf-8 -*-
"""specs/011 机械层全跑：对全部有实质译文的词条跑 check_style/check_math/check_academic，落 results/mechanical-scan.jsonl。

用法：python specs/011-translation-review/bin/mechanical_scan.py [--write]
只读被审文件，不改写；发现的处置由人工逐条裁定。
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "tools"))

OUT = os.path.join(ROOT, "specs", "011-translation-review", "results")
PLACEHOLDER_HINT = "占位"


def translated_entries():
    """有实质译文的词条：正文非占位（>=10 个非空行）。"""
    out = []
    for letter in "abcdefghijklmnopqrstuvwxyz":
        d = os.path.join(ROOT, letter)
        if not os.path.isdir(d):
            continue
        for fn in sorted(os.listdir(d)):
            if not fn.endswith(".md"):
                continue
            path = os.path.join(d, fn)
            slug = "%s/%s" % (letter, fn[:-3])
            try:
                txt = io.open(path, encoding="utf-8").read()
            except Exception:
                continue
            lines = [l for l in txt.splitlines() if l.strip()]
            if len(lines) < 10 or PLACEHOLDER_HINT in txt[:300]:
                continue
            out.append(slug)
    return out


def main():
    os.makedirs(OUT, exist_ok=True)
    entries = translated_entries()
    print("有实质译文词条 %d 条" % len(entries))

    # ---- check_style（导入调用，全量一次） ----
    import check_style
    style_hits = {}
    for slug in entries:
        path = os.path.join(ROOT, slug + ".md")
        try:
            issues = check_style.check_file(path) or []
        except Exception as e:
            issues = ["check_style EXC: %s" % e]
        if issues:
            style_hits[slug] = issues

    # ---- check_math（逐 slug；只在 missing/unbalanced 非空时记问题） ----
    import check_math
    math_hits = {}
    for slug in entries:
        try:
            r = check_math.check_slug(slug.split("/", 1)[1])
            problems = (r.get("missing") or []) + (r.get("unbalanced") or [])
        except Exception as e:
            problems = ["check_math EXC: %s" % e]
        if problems:
            math_hits[slug] = problems

    # ---- check_academic（子进程 --docs 传全部路径一次） ----
    paths = [os.path.join(ROOT, s + ".md") for s in entries]
    r = subprocess.run([sys.executable, os.path.join(ROOT, "tools", "check_academic.py"),
                        "--docs"] + paths, capture_output=True, text=True)
    acad_hits = {}
    for line in (r.stdout + r.stderr).splitlines():
        m = re.match(r"\s*\[([\w-]+)\]\s+(\S+\.md)\s+(.*)", line)
        if m:
            acad_hits.setdefault(m.group(2).replace("\\", "/"), []).append(
                {"code": m.group(1), "msg": m.group(3)})

    # ---- 汇总 ----
    recs = []
    for slug in entries:
        rel = slug + ".md"
        style_issues = [
            {"line": x.get("line"), "rule": x.get("rule"), "detail": x.get("detail")}
            for x in style_hits.get(slug, [])]
        recs.append({
            "slug": slug,
            "style": style_issues,
            "math": [str(x) for x in math_hits.get(slug, [])],
            "academic": acad_hits.get(rel, []),
        })
    outp = os.path.join(OUT, "mechanical-scan.jsonl")
    with io.open(outp, "w", encoding="utf-8") as f:
        for rec in recs:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")

    n_style = sum(1 for r in recs if r["style"])
    n_math = sum(1 for r in recs if r["math"])
    n_acad = sum(1 for r in recs if r["academic"])
    print("style 有问题 %d | math 有问题 %d | academic 有问题 %d（含在途尾节缺失）" % (n_style, n_math, n_acad))
    print("已写 %s" % outp)


if __name__ == "__main__":
    main()
