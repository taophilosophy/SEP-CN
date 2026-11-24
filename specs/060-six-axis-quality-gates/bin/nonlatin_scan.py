#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""非英文引文摸底扫描（只读，specs/060 T0 凭证）。

用法: python specs/060-six-axis-quality-gates/bin/nonlatin_scan.py [--top N]
输出: stdout 摘要＋ specs/060-six-axis-quality-gates/results/nonlatin-scan.json

对象: yuanwen/<letter>/<slug>.md（忠实转换的英文镜像，弯引号形态）
口径: 启发式产候选，不作裁判（ADR-0070）。语种按字符域优先，拉丁系按变音符
      ＋特征词判类；命中不足记 unclassified-latin。

统计三项:
  1. 按语种: 条数、涉及词条数、引文后是否紧跟英文对译（gloss）
  2. 按词条: 非英文引文数 Top N
  3. 斜体外语片段（术语级，不入引文清单，另计）

豁免: 参考文献/Bibliography/References 节内条目（照录对象）、围栏代码块、
      数学定界符、URL。
退出码: 0（分析工具，不做门禁）。
"""
import argparse
import collections
import glob
import json
import os
import re
import sys

if (getattr(sys.stdout, "encoding", "") or "").lower().replace("-", "") != "utf8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))

QUOTE_RE = re.compile(r"[“]([^”\n]{3,500})[”]")
EMPH_RE = re.compile(r"(?<![*\w])\*([^*\n]{2,120})\*(?![*\w])")
FENCE_RE = re.compile(r"^\s*```.*?^\s*```", re.S | re.M)
MATH_RE = re.compile(r"\$\$.*?\$\$|\$[^$\n]{1,400}\$")
BIB_HEAD_RE = re.compile(
    r"^#{1,3}\s*(References|Bibliography|Works Cited|参考文献)", re.I | re.M)
PAREN_RE = re.compile(r"\(([^)[]{5,400})\)")
URL_RE = re.compile(r"https?://\S+")

SCRIPT_RANGES = [
    ("greek", r"\u0370-\u03ff"),
    ("cyrillic", r"\u0400-\u04ff"),
    ("hebrew", r"\u0590-\u05ff"),
    ("arabic", r"\u0600-\u06ff"),
    ("devanagari", r"\u0900-\u097f"),
    ("tibetan", r"\u0f00-\u0fff"),
    ("kana", r"\u3040-\u30ff"),
    ("cjk", r"\u4e00-\u9fff\u3400-\u4dbf"),
]
DIACITRIC_RE = re.compile(r"[àáâãäåæçèéêëìíîïðñòóôõöøùúûüýþÿ]"
                          r"[̄̆́]?"
                          r"|[ĀāĂăĄąĆćĈĉĊċČčĎđĘęĚěĞğİıŁłŃŅņŌōŐőŘřŚŜśŠšŢţŤůŮŰũỸźŻżž]")

LATIN_HINTS = {
    "german": ["der", "die", "das", "und", "ist", "nicht", "von", "als", "ein",
              "eine", "sich", "auch", "werden", "wurde", "dass", "was", "mit"],
    "french": ["le", "la", "les", "des", "est", "que", "pour", "dans", "ne",
               "pas", "qui", "sur", "avec", "cela", "être", "l'esprit"],
    "italian": ["il", "lo", "gli", "della", "che", "non", "sono", "questa",
                "questo", "per", "come", "anche", "del", "delle"],
    "latin": ["est", "non", "et", "in", "ad", "quod", "quae", "esse", "cum",
              "sed", "per", "sunt", "qui", "quid", "vel", "nec", "ita", "res",
              "anima", "Deus", "ens", "ratio", "naturae", "sciencia"],
    "spanish": ["el", "los", "las", "del", "que", "por", "una", "sono", "está"],
}


ENGLISH_STOP = frozenset(
    "the of and to a in that is are was were be been being it its as for with on by not this "
    "these those which or from at an has have had he she they we you i his her their our your "
    "there here what when who whom whose why how then so if but no yes all any some each every "
    "into over under between through during before after above below can could may might must "
    "shall should will would do does did done also only very just more most other another such "
    "than one two three first second third new other same own s t don now".split())


def lang_of(text):
    """字符域优先判语种；拉丁系按变音符＋特征词细分。"""
    low = text.lower()
    for name, rng in SCRIPT_RANGES:
        n = len(re.findall("[" + rng + "]", text))
        if n >= 2:
            # 数学语境残留（^、\\、= 伴随希腊字母）不计
            if name in ("greek",) and re.search(r"[\^\\=₂³]|\d\s*[\^]", text):
                return "none"
            # 假名与汉字并存时归日语
            if name == "cjk" and re.search(r"[\u3040-\u30ff]", text):
                return "japanese"
            return name
    words = re.findall(r"[A-Za-zÀ-ÿĀ-ſ]+", low)
    if not words:
        return "none"
    # 英文占比高且无特征词命中 → 归英文（防带变音符的英文句误入）
    en_ratio = sum(1 for w in words if w in ENGLISH_STOP) / max(len(words), 1)
    scored = []
    for lang, hints in LATIN_HINTS.items():
        hit = sum(words.count(h.lower()) for h in hints)
        if hit:
            scored.append((hit, lang))
    if scored:
        scored.sort(reverse=True)
        if scored[0][0] >= 2:
            return scored[0][1]
    if en_ratio >= 0.45:
        return "none"
    scored = []
    for lang, hints in LATIN_HINTS.items():
        hit = sum(words.count(h.lower()) for h in hints)
        if hit:
            scored.append((hit, lang))
    if scored:
        scored.sort(reverse=True)
        if scored[0][0] >= 2:
            return scored[0][1]
    if DIACITRIC_RE.search(text):
        return "latin-diacritic"
    return "unclassified-latin" if len(words) > 2 else "none"


def has_gloss(buf, end):
    """引文后 250 字符内是否紧跟英文对译（括注形或明示 trans. 标记）。"""
    tail = buf[end:end + 250]
    if re.search(r"(my translation|translation mine|trans\.|translated by)",
                 tail, re.I):
        return "explicit"
    for m in PAREN_RE.finditer(tail[:250]):
        inner = m.group(1)
        if lang_of(inner) in ("none", "unclassified-latin"):
            if re.search(r"[a-z]{3,}", inner.lower()) and not DIACITRIC_RE.search(inner):
                ascii_ratio = sum(c.isascii() for c in inner) / max(len(inner), 1)
                if ascii_ratio > 0.95:
                    return "parenthetical"
    return None


def scan_entry(path):
    txt = open(path, encoding="utf-8", errors="replace").read()
    slug = os.path.splitext(os.path.basename(path))[0]
    txt = FENCE_RE.sub(" ", txt)
    txt = MATH_RE.sub(" ", txt)
    # 参考文献节及其后内容整段豁免（书目条目不是引文）
    m = BIB_HEAD_RE.search(txt)
    body = txt[:m.start()] if m else txt
    found, emph = [], []
    stats = {"quotes": 0, "sent": 0, "sent_confident_non": 0}
    for mt in QUOTE_RE.finditer(body):
        s = URL_RE.sub(" ", mt.group(1)).strip()
        if len(s) < 4:
            continue
        stats["quotes"] += 1
        is_sent = len(s) >= 40 and len(s.split()) >= 6
        if is_sent:
            stats["sent"] += 1
        lg = lang_of(s)
        if is_sent and lg not in ("none", "unclassified-latin", "latin-diacritic"):
            stats["sent_confident_non"] += 1
        if lg in ("none",):
            continue
        if lg == "unclassified-latin" and not DIACITRIC_RE.search(s):
            continue  # 纯英文引号片段不计
        found.append({"slug": slug, "lang": lg,
                      "gloss": has_gloss(body, mt.end()),
                      "len": len(s), "words": len(s.split()), "sample": s[:90]})
    for mt in EMPH_RE.finditer(body):
        s = URL_RE.sub(" ", mt.group(1)).strip()
        lg = lang_of(s)
        if lg not in ("none", "unclassified-latin") or DIACITRIC_RE.search(s):
            if len(s.split()) <= 6:
                emph.append({"slug": slug, "lang": lg, "text": s[:60]})
    return found, emph, stats


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--top", type=int, default=20)
    ap.add_argument("--out", default=os.path.join(
        ROOT, "specs", "060-six-axis-quality-gates", "results",
        "nonlatin-scan.json"))
    args = ap.parse_args()

    files = [p for p in sorted(glob.glob(os.path.join(ROOT, "yuanwen", "*", "*.md")))
             if len(os.path.basename(os.path.dirname(p))) == 1
             and os.path.basename(os.path.dirname(p)).isalpha()]

    all_q, all_e = [], []
    agg = {"quotes": 0, "sent": 0, "sent_confident_non": 0}
    for p in files:
        q, e, st = scan_entry(p)
        all_q.extend(q)
        all_e.extend(e)
        for k in agg:
            agg[k] += st[k]

    by_lang = collections.defaultdict(lambda: {"quotes": 0, "entries": set(),
                                               "gloss_explicit": 0,
                                               "gloss_paren": 0, "no_gloss": 0})
    for r in all_q:
        d = by_lang[r["lang"]]
        d["quotes"] += 1
        d["entries"].add(r["slug"])
        if r["gloss"] == "explicit":
            d["gloss_explicit"] += 1
        elif r["gloss"] == "parenthetical":
            d["gloss_paren"] += 1
        else:
            d["no_gloss"] += 1

    per_entry = collections.Counter(r["slug"] for r in all_q)

    # 成句门槛（>=40 字符且 >=6 词）下的确定非英文占比：回答“SEP 引文是否以英文为主”
    sent_by = collections.Counter(
        r["lang"] for r in all_q
        if r["len"] >= 40 and r.get("words", 0) >= 6
        and r["lang"] not in ("unclassified-latin", "latin-diacritic"))

    out = {
        "schema": "nonlatin-scan/v1",
        "scope": "yuanwen/<letter>/*.md（引文候选，参考文献节与代码数学豁免）",
        "note": "启发式产候选不作裁判；unclassified-latin 仅在有变音符时计入",
        "files_scanned": len(files),
        "quote_candidates": len(all_q),
        "emph_foreign_candidates": len(all_e),
        "by_lang": {k: {"quotes": v["quotes"], "entries": len(v["entries"]),
                        "gloss_explicit": v["gloss_explicit"],
                        "gloss_parenthetical": v["gloss_paren"],
                        "no_gloss": v["no_gloss"]}
                    for k, v in sorted(by_lang.items(),
                                       key=lambda kv: -kv[1]["quotes"])},
        "sentence_level": {
            "rule": "quote spans >=4 chars for totals; sentence = >=40 chars and >=6 words; unclassified-latin/latin-diacritic excluded from non-English",
            "all_quote_spans": agg["quotes"],
            "sentence_quote_spans": agg["sent"],
            "confident_nonenglish": agg["sent_confident_non"],
            "ratio_pct": round(100.0 * agg["sent_confident_non"] / max(agg["sent"], 1), 2),
            "by_lang": dict(sent_by.most_common())},
        "top_entries": per_entry.most_common(args.top),
        "samples": {k: [r["sample"] for r in all_q if r["lang"] == k][:3]
                    for k in sorted({r["lang"] for r in all_q})},
    }
    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w", encoding="utf-8", newline="\n") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)

    print("扫描文件 %d；非英文引文候选 %d 条；斜体外语片段 %d 条"
          % (len(files), len(all_q), len(all_e)))
    print("%-18s %8s %8s %8s %10s %8s" % ("lang", "条数", "词条", "明示译",
                                           "括注译", "无译"))
    for k, v in out["by_lang"].items():
        print("%-18s %8d %8d %8d %10d %8d"
              % (k, v["quotes"], v["entries"], v["gloss_explicit"],
                 v["gloss_parenthetical"], v["no_gloss"]))
    print("\n非英文引文最多的词条：")
    for slug, n in out["top_entries"][:args.top]:
        print("  %-34s %d" % (slug, n))
    print("\n结果：%s" % os.path.relpath(args.out, ROOT))


if __name__ == "__main__":
    main()
