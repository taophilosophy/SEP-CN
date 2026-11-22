#!/usr/bin/env python3
"""specs/057 s3 映射生成器：设计 JSON → TSV，并在生成前做守恒比对。

设计文件格式（UTF-8 JSON）：
  {"节路径／子节路径": [["子节名", "slug1,slug2"], ...], ...}

校验（任一不成立即退出，不写文件）：
- 节路径在当前 mu-lu-s.md 中唯一命中；
- 设计 slug 集合 == 该节点现有直属母条集合（簇子条随母、不列）；
- 子节名非空、slug 无重复、每节 slug 全在现状中；
- 同一 slug 不跨父节重复设计。

用法：python build_map.py <design.json> <out.tsv>
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HEADING = re.compile(r"^(#{1,6}) (.+?)\s*$")
ENTRY = re.compile(r"^(\s*)\* \[(.+?)\]\(([^)]+\.md)\)\s*$")


def slug_of(h):
    return h.rsplit("/", 1)[-1][:-3]


def scan(text):
    lines = text.splitlines()
    nodes = {}
    stack = []
    cur = None
    for i, l in enumerate(lines):
        m = HEADING.match(l)
        if m:
            lv, t = len(m.group(1)), m.group(2).strip()
            while stack and stack[-1][0] >= lv:
                stack.pop()
            path = tuple(nodes[li]["title"] for _, li in stack) + (t,)
            nodes[i] = {"line": i, "level": lv, "title": t,
                        "path": path, "direct": []}
            stack.append((lv, i))
            cur = i
            continue
        em = ENTRY.match(l)
        if em and len(em.group(1)) == 0 and cur is not None:
            nodes[cur]["direct"].append(slug_of(em.group(3)))
    return nodes


def main():
    design_path, out_path = Path(sys.argv[1]), Path(sys.argv[2])
    design = json.loads(design_path.read_text(encoding="utf-8"))
    by_path = {}
    for n in scan((ROOT / "mu-lu-s.md").read_text(encoding="utf-8")).values():
        by_path.setdefault("／".join(n["path"]), []).append(n)

    lines = ["# s3 映射（build_map.py 生成，勿手改）：节路径\t子节名\tslug 列表"]
    seen = {}
    errs = []
    for path, groups in design.items():
        hits = by_path.get(path, [])
        if len(hits) != 1:
            errs.append(f"路径命中 {len(hits)} 处：{path}")
            continue
        cur = set(hits[0]["direct"])
        want = []
        for name, slugs in groups:
            if not name.strip():
                errs.append(f"{path}：空子节名")
            ss = [s for s in slugs.split(",") if s.strip()]
            for s in ss:
                if s in seen:
                    errs.append(f"slug 跨节重复 {s}：{seen[s]} ↔ {path}")
                seen[s] = path
            want += ss
        if len(want) != len(set(want)):
            errs.append(f"{path}：设计内 slug 重复")
        if set(want) != cur:
            errs.append(f"{path}：设计 {len(set(want))} vs 现状 {len(cur)}；"
                        f"缺 {sorted(cur - set(want))} 多 {sorted(set(want) - cur)}")
            continue
        for name, slugs in groups:
            lines.append(f"{path}\t{name}\t{slugs}")
    if errs:
        print("校验失败，未写文件：")
        for e in errs:
            print("  -", e)
        return 1
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    print(f"写出 {out_path}：{len(design)} 节 / {sum(len(g) for g in design.values())} 子节")
    return 0


if __name__ == "__main__":
    sys.exit(main())
