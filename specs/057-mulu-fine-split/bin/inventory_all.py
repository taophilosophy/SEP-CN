#!/usr/bin/env python3
"""specs/057 s3 盘点：全库列出"仍可再细分"的节点。

归属口径：条目行归属于**其上方最近的标题**（mu-lu-s.md 条目一律缩进 0，
层级靠标题表达；缩进 2 的 `* [...]` 是簇成员，随母条不单独计）。
候选条件：节点直属条目≥2 且节点自身无下一层子节。
输出 Markdown，按 H1 分区。
"""
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
    nodes = {}          # 行号 -> dict
    stack = []          # [(层级, 行号)]
    cur = None
    for i, l in enumerate(lines):
        m = HEADING.match(l)
        if m:
            lv, t = len(m.group(1)), m.group(2).strip()
            while stack and stack[-1][0] >= lv:
                stack.pop()
            path = tuple(nodes[li]["title"] for _, li in stack) + (t,)
            nodes[i] = dict(line=i, level=lv, title=t, path=path,
                            direct=[], sub=0)
            if stack:
                nodes[stack[-1][1]]["sub"] += 1
            stack.append((lv, i))
            cur = i
            continue
        em = ENTRY.match(l)
        if em and len(em.group(1)) == 0 and cur is not None:
            nodes[cur]["direct"].append(i)
    out = []
    for i in sorted(nodes):
        n = nodes[i]
        rows = []
        for k in n["direct"]:
            em = ENTRY.match(lines[k])
            kids = []
            j = k + 1
            while j < len(lines):
                mm = ENTRY.match(lines[j])
                if mm:
                    if len(mm.group(1)) == 0:
                        break
                    kids.append(slug_of(mm.group(3)))
                    j += 1
                    continue
                if lines[j].strip() == "":
                    j += 1
                    continue
                break
            rows.append((slug_of(em.group(3)), em.group(2), kids))
        n["direct"] = rows
        out.append(n)
    return out


def main():
    text = (ROOT / "mu-lu-s.md").read_text(encoding="utf-8")
    nodes = scan(text)
    total_link = sum(1 for l in text.splitlines() if ENTRY.match(l))
    direct_total = sum(len(n["direct"]) for n in nodes)
    zones = {}
    for n in nodes:
        zones.setdefault(n["path"][0], []).append(n)
    cand = [n for n in nodes if len(n["direct"]) >= 2 and n["sub"] == 0
            and n["level"] <= 5 and n["path"][0] not in ("前言", "关于")]
    print(f"节点 {len(nodes)}；链接行 {total_link}；直属条目 {direct_total}；"
          f"候选节点 {len(cand)}；候选条目 {sum(len(n['direct']) for n in cand)}")
    for z, ns in zones.items():
        cz = [n for n in ns if len(n["direct"]) >= 2 and n["sub"] == 0
              and n["level"] <= 5 and n["path"][0] not in ("前言", "关于")]
        print(f"  {z}：候选 {len(cz)} 节 / 条目 {sum(len(n['direct']) for n in cz)}")
    # ADR-0004 单体规模：按区分档输出（合出一文件超 1000 行／100 KB 门禁）
    outdir = ROOT / "specs/057-mulu-fine-split/results/s3-inventory"
    outdir.mkdir(parents=True, exist_ok=True)
    for old in outdir.glob("s3-inv-*.md"):      # 文件名按区固定，先清旧档防残留错位
        old.unlink()
    index = ["# s3 全库细分盘点索引（直属条目≥2 且无子节、层级≤H5 的节点，按区分档）", ""]
    for z, ns in zones.items():
        cz = [n for n in ns if len(n["direct"]) >= 2 and n["sub"] == 0
              and n["level"] <= 5 and n["path"][0] not in ("前言", "关于")]
        if not cz:
            continue
        lines = [f"# s3 盘点 · {z}（候选 {len(cz)} 节 / 条目 "
                 f"{sum(len(n['direct']) for n in cz)}）", ""]
        for n in cz:
            lines.append(f"## {'／'.join(n['path'])}　[H{n['level']}，{len(n['direct'])} 条]")
            for slug, title, kids in n["direct"]:
                extra = f"　［簇：{'、'.join(kids)}］" if kids else ""
                lines.append(f"- `{slug}`｜{title}{extra}")
            lines.append("")
        fn = "s3-inv-" + re.sub(r"[、，\s]", "", z) + ".md"
        (outdir / fn).write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
        index.append(f"- `s3-inventory/{fn}`｜{z}：候选 {len(cz)} 节 / "
                     f"条目 {sum(len(n['direct']) for n in cz)}")
    p = ROOT / "specs/057-mulu-fine-split/results/s3-inventory-INDEX.md"
    p.write_text("\n".join(index) + "\n", encoding="utf-8", newline="\n")
    print("写出", p, "与", outdir)


if __name__ == "__main__":
    sys.exit(main())
