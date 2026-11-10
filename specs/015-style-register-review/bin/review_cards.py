# -*- coding: utf-8 -*-
"""specs/015 复核卡生成：为排序靠前的词条打印「文言最密的 3 句 + 所在段上下文」。

只作定位与阅读辅助，判定由复核人在卡片上逐条作出（specs/015 判定口径）。
用法: python -B specs/015-style-register-review/bin/review_cards.py [N] > script/tmp/cards.md
"""
import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from register_metrics import REPO, CLASSICAL, FINAL, CJK, prose, metrics  # noqa: E402

SENT_RE = re.compile(r"[^。；！？]*[。；！？]?")


def dense_sents(text, k=3):
    scored = []
    for p in prose(text):
        for s in SENT_RE.findall(p):
            if len(CJK.findall(s)) < 12:
                continue
            c = sum(s.count(w) for w in CLASSICAL) + len(FINAL.findall(s))
            zhi = len(re.findall(r"[一-龥]之[一-龥]", s))
            if c or zhi >= 2:
                scored.append((c + 0.5 * zhi, c, zhi, s.strip(), p))
    scored.sort(key=lambda t: -t[0])
    return scored[:k]


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 60
    rows = []
    import glob
    for d in sorted(glob.glob(os.path.join(REPO, "[a-z]"))):
        if not os.path.isdir(d):
            continue
        for f in sorted(glob.glob(os.path.join(d, "*.md"))):
            t = open(f, encoding="utf-8").read()
            if len([l for l in t.split("\n") if l.strip()]) <= 1:
                continue
            m = metrics(t)
            m["slug"] = os.path.basename(f)[:-3]
            m["path"] = f
            m["file"] = os.path.relpath(f, REPO).replace("\\", "/")
            rows.append(m)
    rows.sort(key=lambda r: -(r["zhi_ratio"] * 100 + r["score_per_k"]))
    out = io.open(sys.stdout.fileno(), "w", encoding="utf-8", closefd=False)
    for r in rows[:n]:
        out.write("=" * 78 + "\n")
        out.write("%s | %s | CJK=%d 真之/的=%.3f 文言成分=%d 句末/千=%.1f | %s\n" % (
            r["slug"], r["file"], r["cjk"], r["zhi_ratio"], r["score"],
            r["final_per_k"],
            ",".join("%s:%d" % kv for kv in sorted(r["hits"].items(),
                                                   key=lambda kv: -kv[1])[:8])))
        for i, (sc, c, z, s, p) in enumerate(dense_sents(open(r["path"], encoding="utf-8").read()), 1):
            out.write("  [%d] (文言%s/之%s) %s\n" % (i, c, z, s[:170]))
    out.write("TOTAL files=%d shown=%d\n" % (len(rows), min(n, len(rows))))


if __name__ == "__main__":
    main()
