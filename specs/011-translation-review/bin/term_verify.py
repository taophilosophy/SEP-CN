# -*- coding: utf-8 -*-
"""specs/011 术语缺口二重验证。

term_coverage 的 EN 匹配扫全文（含 References），缺口有水分。
本脚本对每条缺口：
  1. EN 正文级确认（yuanwen 镜像剔除 References 节后仍含该术语，词边界）；
  2. zh 正文级缺口确认（词条正文剔除 References/学术工具节后无登记中文变体）；
  3. 输出 zh 正文上下文行（含 EN 原词是否以英文形态残留在 zh 中）。
只读，输出 results/term-verify.jsonl。
"""
import io
import json
import os
import re
import sys
import unicodedata

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
os.chdir(ROOT)
sys.path.insert(0, os.path.join(ROOT, "tools"))
import check_terms as ct  # noqa: E402

GAPS = os.path.join(ROOT, "specs", "011-translation-review", "results", "term-gaps.txt")
OUT = os.path.join(ROOT, "specs", "011-translation-review", "results", "term-verify.jsonl")
DONE_STATES = ("done", "s3_checked", "r1_reviewed")


def strip_tail(text):
    """剔除 References/参考文献/学术工具/Related Entries 节及其后内容。"""
    m = re.search(r"^#{1,3}\s*(?:参考文献|Bibliography|References|学术工具|如何引用|Related Entries|延伸阅读)",
                  text, re.M)
    return text[:m.start()] if m else text


def fold(s):
    return unicodedata.normalize("NFKD", s)


_REG_CACHE = {}


def registry_variants(kind, en):
    """从登记册取该 EN 名/术语的全部登记译名串（聚合所有匹配行，含亦作变体）。"""
    key = (kind, en.lower())
    if key in _REG_CACHE:
        return _REG_CACHE[key]
    path = "ren-ming-biao.md" if kind == "P" else "yi-zhe-shuo-ming.md"
    res = ""
    try:
        hits = []
        for line in io.open(path, encoding="utf-8"):
            if line.startswith("|"):
                parts = [p.strip() for p in line.split("|")]
                if len(parts) > 2 and parts[1].lower() == en.lower():
                    hits.append(parts[2])
        res = "、".join(hits)
    except Exception:
        pass
    _REG_CACHE[key] = res
    return res


def main():
    # 登记册变体表
    reg = ct.load_registry() if hasattr(ct, "load_registry") else None
    rows = [l.rstrip("\n").split("\t") for l in io.open(GAPS, encoding="utf-8") if l.strip()]
    tasks = {}
    out = io.open(OUT, "w", encoding="utf-8")

    def state(slug):
        if slug not in tasks:
            try:
                tasks[slug] = json.load(open("tasks/%s.json" % slug, encoding="utf-8")).get("state", "no-task")
            except Exception:
                tasks[slug] = "no-task"
        return tasks[slug]

    n = 0
    for r in rows:
        kind, zhname, en, slug = r[0], r[1], r[2], r[3]
        if state(slug) not in DONE_STATES:
            continue
        zh_path = slug + ".md"
        yw_path = os.path.join("yuanwen", slug + ".md")
        if not os.path.exists(zh_path):
            continue
        zh = strip_tail(io.open(zh_path, encoding="utf-8").read())
        # zh 中变体确认（登记册行全串按分隔符拆；登记 zh 与 EN 相同=保留英文体例豁免）
        full = registry_variants(kind, en) or zhname
        if not full or full.strip() == en.strip():
            continue
        variants = []
        for v in re.split(r"[／/、；]", full):
            v = v.strip()
            # 剥括注与引号：「亚伯拉罕·伊本·以斯拉（亦作“伊本·以斯拉”）」→ 两变体
            v = re.sub(r"（[^）]*）", "", v).strip(" “”\"")
            if v:
                variants.append(v)
        # 名字简形豁免：「哈贝马斯」⊂「于尔根·哈贝马斯」——zh 用任一段简形也算落实
        seg_variants = []
        for v in variants:
            if "·" in v:
                seg_variants += v.split("·")
        if any(v in zh for v in variants + seg_variants):
            continue  # zh 正文其实有（term_coverage 口径差异）
        # EN 正文级确认
        en_hit = None
        if os.path.exists(yw_path):
            yw = strip_tail(io.open(yw_path, encoding="utf-8").read()).lower()
            pat = re.compile(r"\b" + re.escape(en.lower()) + r"s?\b")
            en_hit = bool(pat.search(fold(yw).lower()))
        # zh 中 EN 残留位置（前 2 处）
        ctx = []
        pat = re.compile(r".{0,28}" + re.escape(en) + r".{0,28}", re.I)
        for m in list(pat.finditer(zh))[:2]:
            ctx.append(m.group(0).replace("\n", " "))
        out.write(json.dumps({"kind": kind, "en": en, "zh": zhname, "slug": slug,
                              "en_body": en_hit, "ctx": ctx}, ensure_ascii=False) + "\n")
        n += 1
    out.close()
    print("二重验证缺口 %d 条 → %s" % (n, OUT))


if __name__ == "__main__":
    main()
