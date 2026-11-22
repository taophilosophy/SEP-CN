#!/usr/bin/env python3
"""specs/057 s2 应用器：按映射表给节点加子节（H4/H5）。

映射表格式（TSV，tab 分隔）：节路径（／分隔）｜子节名｜slug 列表（逗号分隔；簇子条随母，不单列）
用法：python apply_map.py results/s2-map-history.tsv [...]

规则：
- 节点可为任意层级 L；新子节为 L+1 级标题；
- 区间内现有条目（含簇子条）与映射 slugs 必须集合相等（不丢不增）；
- 区间内已有的子标题（此前细分的 H4/H5）在重建时以映射为准整体替换；
- 节注（> 开头行）保留在节点标题下；
- 全局链接行守恒断言 1883。
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
MULUS = ROOT / "mu-lu-s.md"
ENTRY = re.compile(r"^(\s*)\* \[(.+?)\]\(([^)]+\.md)\)\s*$")
HEADING = re.compile(r"^(#{1,6}) (.+?)\s*$")

def slug_of(h):
    return h.rsplit("/", 1)[-1][:-3]

# ---- 读映射 ----
plans = {}   # path tuple -> [(subname, [slugs...])]
order = []
for arg in sys.argv[1:]:
    p = Path(arg)
    if not p.is_absolute():
        p = ROOT / p
    for ln, raw in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
        if not raw.strip() or raw.startswith("#"):
            continue
        parts = raw.split("\t")
        assert len(parts) == 3, f"{p.name}:{ln} 列数 {len(parts)}"
        path, sub, slugs = parts[0].strip(), parts[1].strip(), parts[2].strip()
        tpath = tuple(path.split("／"))
        if tpath not in plans:
            plans[tpath] = []
            order.append(tpath)
        plans[tpath].append((sub, slugs.split(",")))

lines = MULUS.read_text(encoding="utf-8").splitlines()

def head_index(tpath):
    stack = []
    hits = []
    for i, l in enumerate(lines):
        m = HEADING.match(l)
        if m:
            lv, t = len(m.group(1)), m.group(2).strip()
            stack = stack[: lv - 1] + [t]
            if tuple(stack) == tpath:
                hits.append((i, lv))
    assert len(hits) == 1, f"{'／'.join(tpath)} 匹配 {len(hits)} 处"
    return hits[0]

# 按文档逆序处理，避免行号漂移
targets = []
for tpath in order:
    li, lv = head_index(tpath)
    targets.append((li, lv, tpath))
for li, lv, tpath in sorted(targets, reverse=True):
    end = len(lines)
    for j in range(li + 1, len(lines)):
        m = HEADING.match(lines[j])
        if m and len(m.group(1)) <= lv:
            end = j
            break
    body = lines[li + 1:end]
    notes = [l for l in body if l.lstrip().startswith(">")]
    # 收集条目块（母 + 连续子条），忽略现有子标题
    blocks = {}
    i = 0
    while i < len(body):
        m = ENTRY.match(body[i])
        if m and len(m.group(1)) == 0:
            blk = [body[i]]
            j = i + 1
            while j < len(body) and (mm := ENTRY.match(body[j])) and len(mm.group(1)) > 0:
                blk.append(body[j])
                j += 1
            blocks[slug_of(m.group(3))] = blk
            i = j
        else:
            i += 1
    # 现有全部 slug（含子条）
    cur = set()
    for l in body:
        m = ENTRY.match(l)
        if m:
            cur.add(slug_of(m.group(3)))
    plan = plans[tpath]
    want = set()
    for sub, slugs in plan:
        for s in slugs:
            assert s not in want, f"{'／'.join(tpath)}：slug 重复 {s}"
            want.add(s)
            assert s in blocks, f"{'／'.join(tpath)}：缺块 {s}"
    have_subs = {slug_of(ENTRY.match(l).group(3)) for b in blocks.values() for l in b[1:]}
    assert not (set(x for _, ss in plan for x in ss) & have_subs), \
        f"{'／'.join(tpath)}：映射把簇子条当母条列出"
    assert cur == want | have_subs, \
        f"{'／'.join(tpath)}：条目集合不符 缺 {sorted((want | have_subs) - cur)} 多 {sorted(cur - (want | have_subs))}"
    # 重建
    out = [lines[li]]
    if notes:
        out.append("")
        out.extend(notes)
    for sub, slugs in plan:
        out.append("")
        out.append("#" * (lv + 1) + " " + sub)
        out.append("")
        for s in slugs:
            out.extend(blocks[s])
    out.append("")
    # 保持与下一节之间一个空行：替换区间 [li+1, end)
    lines[li + 1:end] = out[1:]

n = sum(1 for l in lines if ENTRY.match(l))
assert n == 1883, f"守恒破坏：{n}"

MULUS.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
print(f"s2 应用 {len(targets)} 节，新增子节 {sum(len(plans[t]) for _, _, t in targets)} 个，条目守恒 {n}")
