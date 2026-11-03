# -*- coding: utf-8 -*-
"""specs/011 v2：16 条标题截断精确修复（白名单 slug 清单，yuanwen H1 重建英文题名）。"""
import io
import os
import re

os.chdir(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))

SLUGS = [
    "a/atomism-modern", "c/consciousness-17th", "e/epsilon-calculus",
    "f/femapproach-continental", "f/femapproach-prag-cont", "f/feminism-psychoanalysis",
    "f/free-will-foreknowledge", "g/genotype-phenotype", "1/18thGerman-preKant",
    "i/implicature-optimality-games", "i/innate-acquired", "k/kant-mind",
    "s/science-mechanisms", "m/moral-conventional", "s/scientific-reproducibility",
    "r/rule-of-law",
]


def authors_of(slug):
    hp = os.path.join("en", slug.split("/", 1)[1], "index.html")
    h = io.open(hp, encoding="utf-8", errors="replace").read()
    names = re.findall(r'citation_author" content="([^"]+)"', h)
    disp = []
    for n in names:
        n = n.strip()
        if "," in n:
            last, first = n.split(",", 1)
            disp.append(first.strip() + " " + last.strip())
        else:
            disp.append(n)
    if len(disp) == 1:
        return disp[0]
    return "%s and %s" % (disp[0], " and ".join(disp[1:]))


def main():
    st = io.open("SUMMARY.md", encoding="utf-8").read()
    ml = io.open("mu-lu-s.md", encoding="utf-8").read()
    n = 0
    for slug in SLUGS:
        path = slug + ".md"
        ywp = os.path.join("yuanwen", slug + ".md")
        en_main = io.open(ywp, encoding="utf-8").read().splitlines()[0].lstrip("# ").strip()
        auth = authors_of(slug)
        en_new = "%s (%s)" % (en_main, auth)
        # SUMMARY 行：zh 部分保留，英文段整体换为 en_new
        m = re.search(r"\* \[([^\]]+)\]\(%s\)" % re.escape(path), st)
        if not m:
            print("SUMMARY 未找到", slug)
            continue
        title = m.group(1)
        zh = re.match(r"^([^A-Za-z]*)", title).group(1).strip()
        new_title = (zh + " " if zh else "") + en_new
        old_line = m.group(0)
        new_line = "* [%s](%s)" % (new_title, path)
        st = st.replace(old_line, new_line, 1)
        # mu-lu-s
        m2 = re.search(r"^(\s*)\* \[([^\]]*)\]\(%s\)" % re.escape(path), ml, re.M)
        if m2 and m2.group(2) != new_title:
            ml = ml[:m2.start()] + "%s* [%s](%s)" % (m2.group(1), new_title, path) + ml[m2.end():]
        # 词条 H1
        zhp = slug + ".md"
        if os.path.exists(zhp):
            zt = io.open(zhp, encoding="utf-8").read()
            m1 = re.match(r"#\s*(.+)\n", zt)
            if m1:
                full = m1.group(1)
                # zh 段 = full 中第一个 ASCII 单词边界前
                zm = re.match(r"^([^A-Za-z]*)", full)
                zh_h = zm.group(1).strip()
                new_full = (zh_h + " " if zh_h else "") + en_new
                if full.strip() != new_full:
                    zt = zt.replace("# " + full, "# " + new_full, 1)
                    io.open(zhp, "w", encoding="utf-8", newline="").write(zt)
        n += 1
        print("修", slug, "→", new_title[:64])
    io.open("SUMMARY.md", "w", encoding="utf-8", newline="").write(st)
    io.open("mu-lu-s.md", "w", encoding="utf-8", newline="").write(ml)
    print("共修", n)


if __name__ == "__main__":
    main()
