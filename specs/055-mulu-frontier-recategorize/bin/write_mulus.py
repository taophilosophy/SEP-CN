#!/usr/bin/env python3
"""specs/055 写回器：plan.json → mu-lu-s.md（对账式生成）。

用法：
  --dry    试写 specs/055-mulu-frontier-recategorize/results/mulus-new.md（不写回）
  --apply  写回 mu-lu-s.md（写回前做集合守恒自检，破坏即拒写）

守恒自检：新旧文件链接行集合逐项相等、计数相等、零重复。
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PLAN = ROOT / "specs/055-mulu-frontier-recategorize/results/plan.json"
MULUS = ROOT / "mu-lu-s.md"
DRY = ROOT / "specs/055-mulu-frontier-recategorize/results/mulus-new.md"

LINK = re.compile(r"^\s*\* \[(.+?)\]\(([^)]+\.md)\)\s*$")

# 案一重排导致的节注旧路径引用修订（specs/055 §Assumptions）
ANNO_FIX = [
    ("哲学通论／女性主义哲学／女性主义理论", "价值理论／性别、种族与性哲学／女性主义理论"),
    ("政治哲学／政治理论", "政治与社会哲学／政治理论"),
    ("伦理学／应用伦理学", "价值理论／应用伦理学"),
]

def fix_anno(line):
    for old, new in ANNO_FIX:
        if old in line:
            line = line.replace(old, new)
    return line

def render(plan):
    lines = ["---", "outline: [1, 6]", "---"]
    lines += plan["foreword_lines"]
    for sec in plan["sections"]:
        p = sec["path"]
        lines.append("")
        lines.append("#" * len(p) + " " + p[-1])
        if sec["anno"]:
            lines.append("")
            for a in sec["anno"]:
                lines.append(fix_anno(a))
        if sec["entries"]:
            lines.append("")
            for e in sec["entries"]:
                ind = " " * e["indent"]
                lines.append(f"{ind}* [{e['raw_text']}]({e['href']})")
    return lines

def link_set(lines):
    out = []
    for l in lines:
        m = LINK.match(l)
        if m:
            out.append((m.group(2), len(l) - len(l.lstrip())))
    return out

def main():
    plan = json.loads(PLAN.read_text(encoding="utf-8"))
    new_lines = render(plan)
    old_lines = MULUS.read_text(encoding="utf-8").splitlines()

    old_links = link_set(old_lines)
    new_links = link_set(new_lines)
    old_paths = sorted(p for p, _ in old_links)
    new_paths = sorted(p for p, _ in new_links)
    ok = old_paths == new_paths
    dup = len(new_paths) != len(set(new_paths))
    report = {
        "old_links": len(old_links), "new_links": len(new_links),
        "conserved": ok and not dup and len(new_links) == len(new_paths),
        "dup": dup,
        "missing": sorted(set(old_paths) - set(new_paths))[:10],
        "extra": sorted(set(new_paths) - set(old_paths))[:10],
    }
    print(json.dumps(report, ensure_ascii=False, indent=1))
    if not report["conserved"]:
        print("!! 守恒破坏，拒写")
        return 1

    if "--apply" in sys.argv:
        MULUS.write_text("\n".join(new_lines) + "\n", encoding="utf-8", newline="\n")
        print("written:", MULUS)
    else:
        DRY.write_text("\n".join(new_lines) + "\n", encoding="utf-8", newline="\n")
        print("dry:", DRY, "lines:", len(new_lines))
    return 0

if __name__ == "__main__":
    sys.exit(main())
