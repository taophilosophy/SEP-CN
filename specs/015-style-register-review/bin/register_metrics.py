# -*- coding: utf-8 -*-
"""语体复核指标（specs/015 辅佐）：只产排序与证据定位，不产生判定。

口径（specs/015「判定口径」）：
  * 排除 `>` 引块、标题、表格、列表、脚注定义、参考文献/学术工具区；
  * 真·之/的比 = 结构助词「之」/(结构助词「之」+「的」)，剔除之一/之后/之外/之间/之前/
    之中/之上/之下/之所以 等现代固定搭配；
  * 文言专有成分只作证据定位，不作判定：吾人、者也、然则、何则、之伦、之属、未尝、
    遑论、无由、非徒、不特、此其、所憾、要者、是已、云尔、余以为、窃谓、且夫、今夫、
    庶几、毋宁、焉/矣/哉/欤 + 句末标点；
  * 逐条给出「证据句」候选：含文言成分最多的正文句（供 015 verdicts.jsonl 抄录）。

用法: python -B specs/015-style-register-review/bin/register_metrics.py [--json]
输出: stdout 表格；--json 输出 script/tmp/register_metrics.json
"""
import glob
import json
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))))
CJK = re.compile(r"[\u4e00-\u9fff]")

# 文言专有成分（只作证据定位）
CLASSICAL = ["吾人", "者也", "然则", "何则", "之伦", "之属", "之辈", "未尝", "遑论",
             "无由", "非徒", "不特", "此其", "所憾", "要者", "是已", "云尔", "余以为",
             "窃谓", "且夫", "今夫", "庶几", "毋宁", "莫能", "无以", "不亦", "得无",
             "无乃", "既已", "诸般", "可尔", "者流", "莫不", "罔不", "曷", "盍"]
FINAL = re.compile(r"[也矣焉耳哉乎欤](?=[。；？！，、]|$)")
# 之 的现代固定搭配（不计入结构助词）
ZHI_FIXED = ["之一", "之后", "之外", "之间", "之前", "之中", "之上", "之下", "之所以",
             "之类", "之余", "之故", "之至", "之极"]
ZHI_RE = re.compile(r"[一-龥]之[一-龥]")
DE_RE = re.compile(r"[一-龥]的[一-龥]")
SENT_RE = re.compile(r"[^。；！？]*[。；！？]?")

BIB_HEAD = re.compile(r"^#{1,6}\s*(?:参考文献|Bibliography|学术工具|注释|Notes)\s*$")
SKIP_LINE = re.compile(r"^(?:\||>\s?|\s*[-*+]\s|\[\^)")


def prose(text):
    paras, cur, bib = [], [], False
    for ln in text.split("\n")[1:]:
        s = ln.strip()
        if s.startswith("#"):
            if BIB_HEAD.match(s):
                bib = True
            continue
        if bib or SKIP_LINE.match(s):
            continue
        if not s:
            if cur:
                paras.append("".join(cur))
                cur = []
            continue
        cur.append(s)
    if cur:
        paras.append("".join(cur))
    return [p for p in paras if len(CJK.findall(p)) >= 40]


def metrics(text):
    paras = prose(text)
    j = "\n".join(paras)
    n = len(CJK.findall(j)) or 1
    zhi = 0
    for m in ZHI_RE.finditer(j):
        s = m.group(0)
        if s[1:] in ZHI_FIXED:
            continue
        zhi += 1
    de = len(DE_RE.findall(j))
    final = len(FINAL.findall(j))
    hits = {w: j.count(w) for w in CLASSICAL if w in j}
    score = sum(hits.values())
    # 证据句：文言成分最密的句子
    best, best_c = "", 0
    for s in SENT_RE.findall(j):
        if len(CJK.findall(s)) < 15:
            continue
        c = sum(s.count(w) for w in CLASSICAL) + len(FINAL.findall(s))
        if c > best_c:
            best, best_c = s.strip(), c
    return {
        "cjk": n, "paras": len(paras),
        "zhi": zhi, "de": de,
        "zhi_ratio": round(zhi / (zhi + de), 3) if (zhi + de) else 0.0,
        "final": final,
        "final_per_k": round(final * 1000 / n, 1),
        "hits": hits, "score": score,
        "score_per_k": round(score * 1000 / n, 1),
        "evidence": best[:80],
    }


def main():
    rows = []
    for d in sorted(glob.glob(os.path.join(REPO, "[a-z]"))):
        if not os.path.isdir(d):
            continue
        for f in sorted(glob.glob(os.path.join(d, "*.md"))):
            t = open(f, encoding="utf-8").read()
            if len([l for l in t.split("\n") if l.strip()]) <= 1:
                continue
            m = metrics(t)
            m["slug"] = os.path.basename(f)[:-3]
            m["file"] = os.path.relpath(f, REPO).replace("\\", "/")
            rows.append(m)
    rows.sort(key=lambda r: -(r["zhi_ratio"] * 100 + r["score_per_k"]))
    if "--json" in sys.argv:
        os.makedirs(os.path.join(REPO, "script", "tmp"), exist_ok=True)
        json.dump(rows, open(os.path.join(REPO, "script", "tmp", "register_metrics.json"),
                             "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("files=%d" % len(rows))
    print("%-34s %6s %6s %7s %6s  %s" % ("slug", "zhi/的", "zhi", "文言成分", "句末/千", "hits"))
    for r in rows[:45]:
        print("%-34s %6.3f %6d %7d %6.1f  %s" % (
            r["slug"], r["zhi_ratio"], r["zhi"], r["score"], r["final_per_k"],
            ",".join("%s:%d" % kv for kv in sorted(r["hits"].items(), key=lambda kv: -kv[1])[:6])))


if __name__ == "__main__":
    main()
