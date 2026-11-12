"""017 分析器：把 mu-lu-s.md 解析为“标题树 + 条目”清单，供逐条复核。

用法：
  python specs/017-mulu-completeness/bin/analyze.py stats
  python specs/017-mulu-completeness/bin/analyze.py dump  > results/entries-before.tsv
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SRC = ROOT / "mu-lu-s.md"

HEAD = re.compile(r"^(#{1,4})\s+(.*)$")
ITEM = re.compile(r"^(\s*)\*\s+\[(.*)\]\(([^)]+)\)\s*$")


def parse(path=SRC):
    heads = []      # 当前标题栈 [(level, text)]
    rows = []
    for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        m = HEAD.match(line)
        if m:
            level = len(m.group(1))
            text = m.group(2).strip()
            heads = [h for h in heads if h[0] < level] + [(level, text)]
            continue
        m = ITEM.match(line)
        if m:
            indent = len(m.group(1))
            rows.append({
                "lineno": lineno,
                "indent": indent,
                "title": m.group(2),
                "path": m.group(3),
                "h1": next((t for l, t in heads if l == 1), ""),
                "h2": next((t for l, t in heads if l == 2), ""),
                "h3": next((t for l, t in heads if l == 3), ""),
                "h4": next((t for l, t in heads if l == 4), ""),
            })
    return rows


def main():
    rows = parse()
    mode = sys.argv[1] if len(sys.argv) > 1 else "stats"
    if mode == "stats":
        from collections import Counter, OrderedDict
        groups = OrderedDict()
        for r in rows:
            key = (r["h1"], r["h2"], r["h3"], r["h4"])
            groups.setdefault(key, []).append(r)
        print(f"条目总数 {len(rows)}；唯一路径 {len({r['path'] for r in rows})}")
        for key, items in groups.items():
            label = " / ".join(x for x in key if x)
            print(f"{len(items):4d}  {label}")
    elif mode == "dump":
        print("lineno\th1\th2\th3\th4\tindent\ttitle\tpath")
        for r in rows:
            print("\t".join([str(r["lineno"]), r["h1"], r["h2"], r["h3"], r["h4"],
                             str(r["indent"]), r["title"], r["path"]]))
    elif mode == "sections":
        # 只打印非叶子节（无子标题的节）的条目数，便于找“超载节”
        pass


if __name__ == "__main__":
    main()
