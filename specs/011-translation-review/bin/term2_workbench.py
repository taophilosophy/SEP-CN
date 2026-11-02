# -*- coding: utf-8 -*-
"""specs/011：双词术语裁定卡生成器。

对 term2-verdict.tsv 的每对 (slug, en, zh_reg)：
  EN 句（yuanwen 正文首个含该术语的句子）→ 提取锚点（年份/大写专名/数字）→
  zh 正文中找锚点同现段 → 输出裁定卡（EN 句 | zh 对应段）。
人工逐对裁定后走 apply 决策表。
"""
import io
import os
import re
import sys
import collections

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
os.chdir(ROOT)


def body(p):
    t = io.open(p, encoding="utf-8").read()
    m = re.search(r"^#{1,3}\s*(?:参考文献|Bibliography|References|学术工具|如何引用|Related Entries|延伸阅读)", t, re.M)
    return t[:m.start()] if m else t


def main():
    rows = [l.rstrip("\n").split("\t") for l in
            io.open("specs/011-translation-review/results/term2-verdict.tsv", encoding="utf-8")]
    out = io.open("specs/011-translation-review/results/term2-workbench.txt", "w", encoding="utf-8")
    cache = {}
    for slug, en, zhreg, enflag, ctx in rows:
        if slug not in cache:
            cache[slug] = (body("yuanwen/%s.md" % slug), body(slug + ".md"))
        yw, zh = cache[slug]
        m = re.search(r"([^.!?\n]{0,110}%s[^.!?\n]{0,110}[.!?" "\"" "])" % re.escape(en), yw, re.I)
        en_sent = m.group(1).replace("\n", " ") if m else ctx
        # 锚点：年份、专名、数字
        anchors = re.findall(r"\b(?:1[0-9]{3}|20[0-9]{2})\b", en_sent) or \
                  re.findall(r"\b[A-Z][a-z]{2,}\b", en_sent) or \
                  re.findall(r"\b\d+\b", en_sent)
        zh_seg = ""
        for a in anchors:
            am = re.search(r"[^\n。]{0,60}%s[^\n。]{0,90}" % re.escape(a), zh)
            if am:
                zh_seg = am.group(0)
                break
        out.write("### %s | %s | %s\nEN: %s\nZH: %s\n\n" % (
            slug, en, zhreg, en_sent[:200], zh_seg[:180]))
    out.close()
    print("裁定卡已写 term2-workbench.txt")


if __name__ == "__main__":
    main()
