# -*- coding: utf-8 -*-
"""specs/011：按词条主题解析词汇（用户建议 2026-11-03）。

每词条三层主题词汇场：
  L1 标题词：SUMMARY 英文题名（去作者括注）↔ 中文题名译名，对照登记册/词汇表；
  L2 正文斜体术语：yuanwen 正文（剔 References/学术工具）中的 *term* 拉丁/外语斜体，
     词频排序取前 N，对照登记册；
  L3 登记落实：登记侧变体在 zh 正文的出现与否。
输出 results/topic-vocab/entries.jsonl（每词条一记录），并汇总体量统计。
只读不写登记册；裁定登记走后续批次。
"""
import io
import json
import os
import re
import sys
import unicodedata
import collections

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
os.chdir(ROOT)
sys.path.insert(0, os.path.join(ROOT, "specs", "011-translation-review", "bin"))
from mechanical_scan import translated_entries  # noqa: E402

OUT_DIR = os.path.join(ROOT, "specs", "011-translation-review", "results", "topic-vocab")


def fold(s):
    s = unicodedata.normalize("NFD", s)
    s = "".join(ch for ch in s if not unicodedata.combining(ch))
    return re.sub(r"\s+", " ", s).strip().casefold()


def load_registry():
    """en_key(lower/fold) -> {zh 全串, lines}。"""
    reg = {}
    for path in ("yi-zhe-shuo-ming.md", "ren-ming-biao.md"):
        for line in io.open(path, encoding="utf-8"):
            if not line.startswith("|"):
                continue
            c = [x.strip() for x in line.split("|")]
            if len(c) > 2 and c[1] and c[2]:
                key = fold(c[1])
                reg.setdefault(key, {"zh": set(), "src": c[1]})
                reg[key]["zh"].add(c[2])
    return reg


def glossary():
    g = {}
    for line in io.open("qian-yan/ci-hui-biao.md", encoding="utf-8"):
        if line.startswith("|"):
            c = [x.strip() for x in line.split("|")]
            if len(c) >= 2 and c[1]:
                g.setdefault(fold(c[1]), c[2])
    return g


def strip_tail(t):
    m = re.search(r"^#{1,3}\s*(?:参考文献|Bibliography|References|学术工具|如何引用|Related Entries|延伸阅读|脚注)",
                  t, re.M)
    return t[:m.start()] if m else t


def title_pair(zh_text):
    """从 zh H1 取 (中文题名, 英文题名去作者括注)，保留完整题名短语。"""
    m = re.match(r"#\s*(.+)", zh_text)
    if not m:
        return "", ""
    full = m.group(1).strip()
    # 作者括注在行尾：[(姓名, 姓名)] 或 (姓名…)——剥行尾括注
    m2 = re.search(r"\s*\((?:[A-ZÀ-ÿ][^()]*)\)\s*$", full)
    body = full[: m2.start()].strip() if m2 else full
    # body = 中文题名 + 英文题名；英文题名 = body 中最后一个拉丁字母起始的位置起
    m3 = re.search(r"([A-Za-z\u00C0-\u024F][A-Za-z\u00C0-\u024F0-9'’\-\s\.\,\:\?！]*[A-Za-z\?\!]|\w)$", body)
    # 逐字符找最后一个 CJK 与拉丁的分界
    split_at = None
    for idx, ch in enumerate(body):
        if "\u4e00" <= ch <= "\u9fff" or ch in "，。、；：（）":
            split_at = idx + 1
    en = body[split_at:].strip() if split_at else body
    zh = body[:split_at].strip() if split_at else ""
    # 英文题名再剥行尾作者括注（一些标题作者括注在英文题名内）
    en = re.sub(r"\s*\((?:[A-ZÀ-ÿ][^()]*|\.\.\.)\)\s*$", "", en).strip()
    return zh, en


def italic_terms(yw_body, cap=12):
    """yuanwen 正文的 *term* 斜体拉丁术语，按词频排序。"""
    terms = collections.Counter()
    for m in re.finditer(r"(?<![\*\w])\*([A-Za-zÀ-ÿĀ-žĀ-ɏ][A-Za-zÀ-ÿĀ-žā-ž'\- ]{1,60}?)\*(?!\*)", yw_body):
        t = m.group(1).strip()
        if 2 <= len(t.split()) <= 6 or 3 <= len(t) <= 40:
            if re.search(r"[A-Za-z]", t):
                terms[t] += 1
    # 归并大小写
    merged = collections.Counter()
    for t, n in terms.items():
        merged[t if t[0].isupper() else t] += n
    return [t for t, _ in merged.most_common(cap)]


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    reg, gl = load_registry(), glossary()
    entries = translated_entries()
    out = io.open(os.path.join(OUT_DIR, "entries.jsonl"), "w", encoding="utf-8")
    stats = collections.Counter()
    for slug in entries:
        zh_text = io.open(slug + ".md", encoding="utf-8").read()
        zh, en = title_pair(zh_text)
        ywp = os.path.join("yuanwen", slug + ".md")
        it_terms = []
        if os.path.exists(ywp):
            it_terms = italic_terms(strip_tail(io.open(ywp, encoding="utf-8").read()))
        # L1 标题词登记状态
        en_fold = fold(en)
        title_reg = reg.get(en_fold) or reg.get(fold(en.replace("The ", "", 1)))
        title_state = "registered" if title_reg else ("gloss" if en_fold in gl else "UNREGISTERED")
        if title_state == "UNREGISTERED":
            stats["title-unreg"] += 1
        else:
            stats["title-ok"] += 1
        # L2 斜体术语登记状态
        it_rows = []
        for t in it_terms:
            r = reg.get(fold(t))
            it_rows.append({"en": t, "reg": bool(r), "zh": sorted(r["zh"])[0] if r else ""})
        unreg_it = sum(1 for x in it_rows if not x["reg"])
        stats["it-total"] += len(it_rows)
        stats["it-unreg"] += unreg_it
        out.write(json.dumps({"slug": slug, "title_zh": zh, "title_en": en,
                              "title_state": title_state,
                              "title_reg_zh": sorted(title_reg["zh"])[0] if title_reg else "",
                              "italic_terms": it_rows}, ensure_ascii=False) + "\n")
    out.close()
    print("词条 %d | 标题词已登记 %d 未登记 %d | 斜体术语 %d 条其中未登记 %d" % (
        len(entries), stats["title-ok"], stats["title-unreg"], stats["it-total"], stats["it-unreg"]))


if __name__ == "__main__":
    main()
