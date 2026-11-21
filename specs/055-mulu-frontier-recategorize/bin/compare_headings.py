#!/usr/bin/env python3
"""specs/055 标题树对照：旧版（00ee29e44^，四区）vs 新版（HEAD，六区）mu-lu-s.md。

匹配规则：同一父节内同名 → 保留（递归）；仅旧有 → 撤离；仅新有 → 新设；
跨父同名 → 迁移/随父改名（按题名配对，多名冲突时按父题名配对）。
只读分析，输出人读清单。"""
import json
import re
import subprocess
from pathlib import Path
from collections import OrderedDict, defaultdict

OLD_REV = "00ee29e44^"
# 新侧默认读工作树 mu-lu-s.md（提交后与 HEAD 一致）；argv[1] 可覆盖旧 rev，argv[2] 覆盖新文件
NEW_FILE = None

def get_text(rev):
    r = subprocess.run(["git", "show", rev + ":mu-lu-s.md"],
                       capture_output=True, check=True)
    return r.stdout.decode("utf-8")

def tree(text):
    root = OrderedDict()
    stack = [("", root)]
    for line in text.splitlines():
        m = re.match(r"^(#{1,6}) (.+?)\s*$", line)
        if not m:
            continue
        lv, t = len(m.group(1)), m.group(2)
        node = stack[lv - 1][1]
        child = OrderedDict()
        node[t] = child
        stack = stack[:lv]
        stack.append((t, child))
    return root

def walk(node, path, out):
    for t, ch in node.items():
        p = path + [t]
        out.append(tuple(p))
        walk(ch, p, out)

def collect_paths(t):
    ps = []
    walk(t, [], ps)
    return ps

old_ps = collect_paths(tree(get_text(OLD_REV)))
new_text = Path(__file__).resolve().parents[3].joinpath("mu-lu-s.md").read_text(encoding="utf-8")
new_ps = collect_paths(tree(new_text))

# 递归 diff：同父同名保留；仅一方有 → 该子树全枚举（2026-11-22 修正：此前只枚举
# 顶层，新增/撤离节点的后代全部漏计）
def subtree(node, path, out):
    for t, ch in node.items():
        p = path + [t]
        out.append(tuple(p))
        subtree(ch, p, out)

def diff(old, new, path, rem, add):
    for t in old:
        if t in new:
            diff(old[t], new[t], path + [t], rem, add)
        else:
            rem.append(tuple(path + [t]))
            subtree(old[t], path + [t], rem)
    for t in new:
        if t not in old:
            add.append(tuple(path + [t]))
            subtree(new[t], path + [t], add)

rem, add = [], []
diff(tree(get_text(OLD_REV)), tree(new_text), [], rem, add)

# 配对：题名单一 → 直接配；多冲突 → 按父题名配
def group(paths):
    g = defaultdict(list)
    for p in paths:
        g[p[-1]].append(p)
    return g

grem, gadd = group(rem), group(add)
moved, removed_only, added_only = [], [], []
for t in sorted(set(grem) | set(gadd)):
    rs, as_ = grem.get(t, []), gadd.get(t, [])
    if rs and as_:
        if len(rs) == 1 and len(as_) == 1:
            moved.append((rs[0], as_[0]))
        else:
            used = set()
            for r in rs:
                match = next((a for a in as_ if a not in used
                              and (len(r) > 1 and len(a) > 1 and r[-2] == a[-2])), None)
                if match:
                    used.add(match)
                    moved.append((r, match))
            for r in rs[len([m for m in moved if m[0] == r]):]:
                if all(m[0] != r for m in moved):
                    removed_only.append(r)
            for a in as_:
                if all(m[1] != a for m in moved):
                    added_only.append(a)
    else:
        removed_only.extend(rs)
        added_only.extend(as_)

def fmt(p):
    return "／".join(p)

print("== 旧 %d 节点 → 新 %d 节点；保留 %d、迁移 %d、撤销 %d、新设 %d ==" % (
    len(old_ps), len(new_ps),
    len(old_ps) - len(rem), len(moved), len(removed_only), len(added_only)))
print()
print("── 迁移／随父改名（旧父 → 新父，同题名）──")
for r, a in moved:
    lv = len(a)
    print("H%d %s：%s → %s" % (lv, r[-1], fmt(r[:-1]) or "（根）", fmt(a[:-1]) or "（根）"))
print()
print("── 撤销（旧有新无）──")
for p in removed_only:
    print("H%d %s（原属 %s）" % (len(p), p[-1], fmt(p[:-1]) or "（根）"))
print()
print("── 新设（新有旧无）──")
for p in added_only:
    print("H%d %s（现属 %s）" % (len(p), p[-1], fmt(p[:-1]) or "（根）"))
