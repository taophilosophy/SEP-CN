# -*- coding: utf-8 -*-
"""specs/011：mu-lu-s 四行标题对齐 SUMMARY 正式词条行（排除别名链行）。"""
import io
import re

mt = io.open("mu-lu-s.md", encoding="utf-8").read()
sm = {}
for m in re.finditer(r"^\s*\* \[(.+?)\]\((\S+?)\)", io.open("SUMMARY.md", encoding="utf-8").read(), re.M):
    title, path = m.group(1), m.group(2)
    if title.startswith("\\") or "\u2014\u2014\u89c1" in title:  # 别名链行「——见」
        continue
    sm.setdefault(path, title)
n = 0
for path in ("i/incommensurability.md", "i/incompatibilism-theories.md",
             "i/intellectual-property.md", "i/it-privacy.md"):
    m = re.search(r"^(\s*)\* \[([^\]]*)\]\(%s\)" % re.escape(path), mt, re.M)
    if m and path in sm and m.group(2) != sm[path]:
        mt = mt[:m.start()] + "%s* [%s](%s)" % (m.group(1), sm[path], path) + mt[m.end():]
        n += 1
        print("修", path, "->", sm[path][:56])
io.open("mu-lu-s.md", "w", encoding="utf-8", newline="").write(mt)
print("共修", n)
