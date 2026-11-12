# -*- coding: utf-8 -*-
"""017 审核器：按关键词规则检查条目是否落在语义相符的节。

只报告，不修改。命中即是“需人工判断”的线索，不是错误判决。
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SRC = ROOT / "mu-lu-s.md"

HEAD = re.compile(r"^(#{1,4})\s+(.*)$")
ITEM = re.compile(r"^(\s*)\*\s+\[(.*)\]\(([^)]+)\)\s*$")

RULES = [
    ("女性主义", r"女性主义|Feminist|Feminism|Gender|Queer|Trans Philosophy", ("女性主义哲学",)),
    ("逻辑", r"逻辑|Logic|Set Theory|Model Theory|Proof Theory|Computability", ("语言哲学与逻辑学", "数学哲学")),
    ("美学", r"美学|Aesthetic|Art\b|Music\b|Film\b|Dance|Theater|Architecture", ("美学",)),
    ("宗教", r"宗教|God\b|Theolog|Divine|Trinity|Atonement|Faith\b", ("宗教哲学",)),
    ("心灵", r"心灵|Mind\b|Consciousness|Perception|Qualia|Intentionality", ("心灵哲学", "认知科学与神经科学哲学")),
    ("医学", r"医学|Medical|Medicine|Health|Disability|Bioethics|Nursing", ("医学哲学",)),
    ("生物", r"生物学|Biology|Evolution|Species|Gene\b|Genetics|Ecology|Organism", ("生物学哲学",)),
    ("物理", r"物理学|Quantum|Spacetime|Relativity|Statistical Mechanics|Cosmolog", ("物理学哲学",)),
    ("数学", r"数学|Mathematics|Geometry|Arithmetic|Infinity|Probability", ("数学哲学", "语言哲学与逻辑学")),
    ("政治", r"政治哲学|Political Philosophy|Democracy|Justice|Rights\b|Liberty|Sovereignty", ("政治哲学", "现代政治哲学")),
    ("法", r"法律|Law\b|Legal|Punishment|Tort", ("法哲学",)),
    ("科学", r"科学哲学|Philosophy of Science|Scientific|Kuhn|Popper|Feyerabend|Lakatos", ("科学哲学",)),
    ("教育", r"教育|Education|Childhood|Children", ("教育哲学",)),
    ("经济", r"经济|Economic|Market|Utilitarian|Welfare Economics", ("经济哲学", "决策与博弈论")),
]


def main() -> int:
    lines = SRC.read_text(encoding="utf-8").splitlines()
    h1 = h2 = h3 = h4 = ""
    rows = []
    for ln in lines:
        m = HEAD.match(ln)
        if m:
            lvl, txt = len(m.group(1)), m.group(2).strip()
            if lvl == 1:
                h1, h2, h3, h4 = txt, "", "", ""
            elif lvl == 2:
                h2, h3, h4 = txt, "", ""
            elif lvl == 3:
                h3, h4 = txt, ""
            else:
                h4 = txt
            continue
        m = ITEM.match(ln)
        if m:
            rows.append((h1, h2, h3, h4, m.group(2), m.group(3)))

    hits = 0
    for name, pat, allowed in RULES:
        rx = re.compile(pat, re.I)
        bad = []
        for h1, h2, h3, h4, title, path in rows:
            if not rx.search(title):
                continue
            secs = (h1, h2, h3, h4)
            if any(a in secs for a in allowed):
                continue
            bad.append((title, path, " / ".join(x for x in secs if x)))
        if bad:
            hits += len(bad)
            print(f"\n## {name}：{len(bad)} 条不在预期节")
            for t, p, s in bad[:40]:
                print(f"  {t[:60]}  <{p}>  现属：{s}")
    print(f"\n合计线索 {hits} 条")
    return 0


if __name__ == "__main__":
    sys.exit(main())
