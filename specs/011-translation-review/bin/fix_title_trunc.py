# -*- coding: utf-8 -*-
"""specs/011：SUMMARY 标题作者括注截断批量修复（对照 html citation_author）。

截断形态：标题 "... and 第二作者)" 缺第一作者与开括号。
修复：en/<slug>/index.html 的 citation_author 列表 → "First Last and First Last" →
SUMMARY / mu-lu-s / 词条 H1 三链同步。zh 部分不动。
"""
import io
import os
import re

os.chdir(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))


def authors_of(slug):
    hp = os.path.join("en", slug.split("/", 1)[1], "index.html")
    if not os.path.exists(hp):
        return None
    h = io.open(hp, encoding="utf-8", errors="replace").read()
    names = re.findall(r'citation_author" content="([^"]+)"', h)
    if not names:
        return None
    # "Last, First" → "First Last"
    disp = []
    for n in names:
        n = n.strip()
        if "," in n:
            last, first = n.split(",", 1)
            disp.append("%s %s" % (first.strip(), last.strip()))
        else:
            disp.append(n)
    if len(disp) == 1:
        return disp[0]
    return "%s and %s" % (disp[0], " and ".join(disp[1:]))


def main():
    fixed = 0
    sum_new, mul_new = [], []
    for i, l in enumerate(io.open("SUMMARY.md", encoding="utf-8"), 1):
        m = re.search(r"\[([^\]]+)\]\((\S+?)\)", l)
        if not m:
            continue
        title, path = m.group(1), m.group(2)
        if title.count("(") == title.count(")"):
            continue
        slug = path[:-3]
        auth = authors_of(slug)
        if not auth:
            print("跳过（无作者源）:", slug)
            continue
        # 截断形态：尾段 " and X Y)" —— 去掉从最后一个 " and " 到 ")" 的残段，补全括注
        tail_m = re.search(r"\s([A-Za-z][A-Za-z\s\.]*?)\)$", title)
        if not tail_m:
            print("形态异常:", slug, title[-40:])
            continue
        # 截断的尾部作者名残段 → 用真实作者串替换整段括注
        # 新标题 = 去掉残段 + "(全作者)"
        new_title = title[: tail_m.start()].rstrip() + " (" + auth + ")"
        new_line = l.replace(title, new_title)
        fixed += 1
        print("修 %s: ...%s → ...%s" % (slug, title[-45:], new_title[-52:]))
        # SUMMARY / mu-lu-s：内存积累，最后单次写回
        sum_new.append((l, new_line))
        mul_new.append((title, new_title, path))
        # 词条 H1：# zh_title en_title (authors)
        zhp = slug + ".md"
        if os.path.exists(zhp):
            zt = io.open(zhp, encoding="utf-8").read()
            m1 = re.match(r"#\s*(.+)", zt)
            if m1:
                full = m1.group(1)
                # H1 尾部英文题名段——同样有截断括注
                new_h1_tail = new_title.split(" ", 1)
                # zh 前缀 = full 中非英文开头部分（取 full 里 en 截断前的 zh 段）
                # 简化：把 full 中的截断英文串换成 new_title 的英文串
                en_bad = new_title  # full new_title（zh+en）
                # full 的英文段 = full 里最后出现拉丁的位置起；直接替换 full 尾部与 new_title 尾部共同残段
                new_full = full
                # 用 new_title 反推：new_title = zh + " " + en_new；full = zh + " " + en_bad
                zh_part = new_title[: new_title.find(en_bad2)] if False else None
                # 直接：full 尾部残段 = title 中 "英文题名残段"；找 full 中同一残段替换
                tail_seg = tail_m.group(0)  # " and X Y)"
                if tail_seg in full:
                    # 新尾 = " (全作者)"；其前保留 full 的英文题名主体
                    # 英文题名主体 = new_title 的英文段去括注
                    en_main = re.search(r"([A-Za-z][^)*]*?)\s*\(" , new_title + "(")
                    new_full = full[: tail_m.start()] + " (" + auth + ")"
                    zt = zt.replace(m1.group(0), "# " + new_full, 1)
                    io.open(zhp, "w", encoding="utf-8", newline="").write(zt)
    st = io.open("SUMMARY.md", encoding="utf-8").read()
    for old, new in sum_new:
        st = st.replace(old, new, 1)
    io.open("SUMMARY.md", "w", encoding="utf-8", newline="").write(st)
    ml = io.open("mu-lu-s.md", encoding="utf-8").read()
    for title, new_title, path in mul_new:
        old_ml = re.search(r"^(\s*)\* \[%s\]\(%s\)" % (re.escape(title), re.escape(path)), ml, re.M)
        if old_ml:
            ml = ml[:old_ml.start()] + "%s* [%s](%s)" % (old_ml.group(1), new_title, path) + ml[old_ml.end():]
    io.open("mu-lu-s.md", "w", encoding="utf-8", newline="").write(ml)
    print("共修", fixed)


if __name__ == "__main__":
    main()
