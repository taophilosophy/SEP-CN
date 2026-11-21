#!/usr/bin/env python3
"""specs/055 两案骨架生成器（预览阶段，不填充条目）。

数据源：
  mu-lu-s.md                              现行分类树（1881 链接行）
  specs/010 .../philpapers-mapping.tsv    PP 全量映射（2026-11-01）

产出（results/）：
  skeleton-scheme1-pp.md        案一：PP 骨架＋本地细分（树＋计数）
  skeleton-scheme2-calibrate.md 案二：现行四区＋校准标记（树＋计数＋增并疑位标记）
  skeleton-stats.json           机检对账数据（守恒、diff、增补候选、疑位统计）

只读分析，不写回任何源文件。
"""
import csv
import json
import re
from collections import OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
MULUS = ROOT / "mu-lu-s.md"
TSV = ROOT / "specs/010-mulu-recategorize/results/philpapers-mapping.tsv"
OUT = ROOT / "specs/055-mulu-frontier-recategorize/results"
OUT.mkdir(parents=True, exist_ok=True)

HEADING = re.compile(r"^(#{1,6}) (.+?)\s*$")
ENTRY = re.compile(r"^(\s*)\* \[(.+?)\]\(([^)]+\.md)\)\s*$")

def unescape(t):
    return t.replace("\\*", "*").replace("\\[", "[").replace("\\]", "]")

def slug_of(href):
    return href.rsplit("/", 1)[-1][:-3]

# ---------- 解析现行树 ----------
nodes = []      # {level,title,path}
entries = []    # {slug,text,indent,path(node_path),lineno}
stack = []
for lineno, line in enumerate(MULUS.read_text(encoding="utf-8").splitlines(), 1):
    m = HEADING.match(line)
    if m:
        level, title = len(m.group(1)), unescape(m.group(2).strip())
        stack = stack[: level - 1]
        stack.append(title)
        nodes.append({"level": level, "title": title, "path": tuple(stack), "lineno": lineno})
        continue
    m = ENTRY.match(line)
    if m:
        href = m.group(3)
        entries.append({
            "slug": slug_of(href), "text": unescape(m.group(2)),
            "indent": len(m.group(1)), "path": tuple(stack), "lineno": lineno,
        })

# ---------- 010 TSV ----------
PP = {}
with TSV.open(encoding="utf-8-sig", newline="") as fh:
    for row in csv.DictReader(fh, delimiter="\t"):
        PP[row["slug"]] = (row.get("PP大类", "").strip(), row.get("PP子类", "").strip())

unmapped = [e["slug"] for e in entries if e["slug"] not in PP]
# 注：TSV（2026-11-01）之后接入的词条（inquiry、bioethics-moral-reasoning、
# bessarion、gianfrancesco-pico、cardano、shaftesbury、novalis、lukacs、
# ibn-gabirol、privacy-health、shu-yu-biao、ren-ming-biao）无 PP 行；
# 案一映射改为区域优先＋确定性锚定表，不依赖 PP 行，unmapped 仅作信息项。

# ---------- 案一：PP 骨架＋本地细分（确定性锚定表，PP 挂载点经联网核实） ----------
H1_ME, H1_VT, H1_SLM = "形而上学与认识论", "价值理论", "科学、逻辑与数学"
H1_HIST, H1_TRAD = "西方哲学史", "哲学传统"

# 哲学通论 cur2 → (H1, H2, 是否携带原节名为 ###)
S1_TONG2 = {
    "形而上学": (H1_ME, "形而上学", False), "认识论": (H1_ME, "认识论", False),
    "心灵哲学": (H1_ME, "心灵哲学", False), "宗教哲学": (H1_ME, "宗教哲学", False),
    "政治哲学": (H1_VT, "政治与社会哲学", False), "法哲学": (H1_VT, "法哲学", False),
    "环境哲学": (H1_VT, "应用伦理学", True), "美学": (H1_VT, "美学", False),
    "女性主义哲学": (H1_VT, "性别、种族与性哲学", False),
    "教育哲学": (H1_SLM, "社会科学哲学", True), "经济哲学": (H1_VT, "政治与社会哲学", True),
    "决策与博弈论": (H1_ME, "行动哲学", False), "文化哲学": (H1_VT, "政治与社会哲学", True),
    "出生与死亡哲学": (H1_VT, "应用伦理学", True),
}
# 语言哲学与逻辑学 cur3 → (H1, H2, carry)
S1_LANG3 = {
    "语言哲学": (H1_ME, "语言哲学", False), "语义学": (H1_ME, "语言哲学", True),
    "语用学": (H1_ME, "语言哲学", True),
    "逻辑史与逻辑学家": (H1_SLM, "逻辑学与逻辑哲学", True),
    "经典逻辑与传统逻辑": (H1_SLM, "逻辑学与逻辑哲学", True),
    "非经典逻辑": (H1_SLM, "逻辑学与逻辑哲学", True),
    "数理逻辑与数学基础": (H1_SLM, "逻辑学与逻辑哲学", True),
    "悖论与非形式逻辑": (H1_SLM, "逻辑学与逻辑哲学", True),
}
# 伦理学 cur3 → (H1, H2, carry)
S1_ETH3 = {
    "元伦理学": (H1_VT, "元伦理学", False), "规范伦理学": (H1_VT, "规范伦理学", False),
    "价值论": (H1_VT, "价值论", False),
    "道德心理学": (H1_ME, "行动哲学", True), "行动哲学与理由论": (H1_ME, "行动哲学", True),
    "社会伦理学": (H1_VT, "应用伦理学", True), "应用伦理学": (H1_VT, "应用伦理学", False),
}
# 科学哲学 cur2 → (H1, H2, carry)
S1_SCI2 = {
    "科学哲学史与学派": (H1_SLM, "一般科学哲学", True), "一般科学哲学": (H1_SLM, "一般科学哲学", False),
    "物理学哲学": (H1_SLM, "物理科学哲学", False), "化学哲学": (H1_SLM, "物理科学哲学", True),
    "数学哲学": (H1_SLM, "数学哲学", False), "生物学哲学": (H1_SLM, "生物哲学", False),
    "医学哲学": (H1_SLM, "医学哲学", False), "认知科学与神经科学哲学": (H1_SLM, "认知科学哲学", False),
    "信息与计算科学哲学": (H1_SLM, "计算与信息哲学", False), "社会科学哲学": (H1_SLM, "社会科学哲学", False),
    "技术哲学": (H1_SLM, "计算与信息哲学", True),
}

def _dest_path(dest, cur2, cur3, path):
    """装配方：carry=True 且源节为 ## 直挂时，原节名作为 ### 随行。"""
    h1n, h2n, carry = dest
    if cur3:
        mid = (cur3,) if cur3 != h2n else ()
        return (h1n, h2n) + mid + path[3:]
    if carry and cur2 and cur2 != h2n:
        return (h1n, h2n, cur2) + path[2:]
    return (h1n, h2n) + path[2:]

def s1_assign(e):
    path = e["path"]
    h1 = path[0] if path else ""
    cur2 = path[1] if len(path) > 1 else None
    cur3 = path[2] if len(path) > 2 else None
    if h1 in ("前言", "关于"):
        return path
    if h1 == "西方哲学史":
        if cur2 == "犹太哲学":  # PP：犹太哲学归哲学传统
            return (H1_TRAD, "犹太哲学") + path[2:]
        return path
    if h1 == "世界哲学（欧洲以外）":
        return (H1_TRAD,) + path[1:]
    if h1 == "科学哲学":
        dest = S1_SCI2.get(cur2, (H1_SLM, cur2, False))
        return _dest_path(dest, cur2, cur3, path)
    if h1 == "哲学通论":
        if cur2 == "形而上学" and cur3 == "自由意志":  # PP：自由意志归行动哲学
            return (H1_ME, "行动哲学", "自由意志") + path[3:]
        if cur2 == "语言哲学与逻辑学":
            d = S1_LANG3.get(cur3, (H1_ME, "语言哲学", False))
            return _dest_path(d, cur2, cur3, path)
        if cur2 == "伦理学":
            d = S1_ETH3.get(cur3, (H1_VT, "规范伦理学", False))
            return _dest_path(d, cur2, cur3, path)
        d = S1_TONG2.get(cur2)
        if d:
            return _dest_path(d, cur2, cur3, path)
        return ("归类待裁",) + path[1:]
    return ("归类待裁",) + path[1:]

s1_tree = OrderedDict()
for e in entries:
    p = s1_assign(e)
    s1_tree.setdefault(p, 0)
    s1_tree[p] += 1

# ---------- 案二：现行四区＋校准标记 ----------
s2_tree = OrderedDict()
for e in entries:
    s2_tree.setdefault(e["path"], 0)
    s2_tree[e["path"]] += 1

# 【小】节点（主题区 ###/#### 且 <3 条；史区/传统区人物节不计）
small = [p for p, c in s2_tree.items()
         if len(p) >= 3 and c < 3 and p[0] in ("哲学通论", "科学哲学")]
# 错位疑位：通论/科学哲学区 ### 节内 PP 大类与节点学科域不符（集合用 TSV 英文类名）
ME_E, VT_E, SLM_E = "Metaphysics and Epistemology", "Value Theory", "Science, Logic, and Mathematics"
CANON = {  # 现行 ## → 允许的 PP 大类集
    "形而上学": {ME_E}, "认识论": {ME_E},
    "语言哲学与逻辑学": {ME_E, SLM_E}, "心灵哲学": {ME_E}, "宗教哲学": {ME_E},
    "伦理学": {VT_E, ME_E}, "政治哲学": {VT_E}, "法哲学": {VT_E},
    "环境哲学": {VT_E}, "美学": {VT_E}, "女性主义哲学": {VT_E},
    "教育哲学": {SLM_E, "Philosophy, Misc"}, "经济哲学": {VT_E},
    "决策与博弈论": {ME_E, SLM_E},
    "文化哲学": {VT_E}, "出生与死亡哲学": {VT_E},
    "科学哲学史与学派": {SLM_E}, "一般科学哲学": {SLM_E}, "物理学哲学": {SLM_E},
    "化学哲学": {SLM_E}, "数学哲学": {SLM_E}, "生物学哲学": {SLM_E},
    "医学哲学": {SLM_E}, "认知科学与神经科学哲学": {SLM_E},
    "信息与计算科学哲学": {SLM_E}, "社会科学哲学": {SLM_E}, "技术哲学": {SLM_E},
}
misplaced_by_node = {}
for e in entries:
    path = e["path"]
    if len(path) < 2 or path[0] not in ("哲学通论", "科学哲学"):
        continue
    canon = CANON.get(path[1])
    if canon is None:
        continue
    cat = PP.get(e["slug"], ("", ""))[0]
    if cat and cat not in canon:
        misplaced_by_node.setdefault(path, []).append(e["slug"])

# 增补候选：学科类 PP 子类 ≥6 条且散布 ≥3 个现行 ##（断代/传统类除外）
PERIODISH = {"20th Century Philosophy", "17th/18th Century Philosophy",
             "19th Century Philosophy", "19th/20th Century Philosophy",
             "Medieval and Renaissance Philosophy", "Ancient Greek and Roman Philosophy",
             "Asian Philosophy", "Philosophical Traditions, Miscellaneous",
             "African/Africana Philosophy", "Philosophy of the Americas",
             "Continental Philosophy", "站点导航", "nav"}
scattered = {}
for e in entries:
    cat, sub = PP.get(e["slug"], ("", ""))
    if not sub or sub in PERIODISH:
        continue
    cur2 = e["path"][1] if len(e["path"]) > 1 else None
    scattered.setdefault(sub, {}).setdefault(cur2, 0)
    scattered[sub][cur2] += 1
add_cands = []
for sub, by2 in scattered.items():
    total = sum(by2.values())
    if total >= 6 and len(by2) >= 3:
        add_cands.append((sub, total, len(by2)))
add_cands.sort(key=lambda x: -x[1])

# ---------- 渲染（祖先合成＋累计计数） ----------
def build_full_tree(counts, seed_paths=()):
    """counts: {path: direct_count}；seed_paths: 仅有标题无直接条目的路径（direct=0）。"""
    root = {"children": OrderedDict(), "direct": 0}
    def insert(path, c):
        node = root
        for t in path:
            node = node["children"].setdefault(t, {"children": OrderedDict(), "direct": 0})
        node["direct"] += c
    for p, c in counts.items():
        insert(p, c)
    for p in seed_paths:
        insert(p, 0)
    def cum(node):
        total = node["direct"]
        for ch in node["children"].values():
            total += cum(ch)
        node["cum"] = total
        return total
    cum(root)
    return root

def render_tree(root, marks=None):
    lines = []
    def walk(node, path):
        for title, ch in node["children"].items():
            p = path + [title]
            level = len(p)
            label = "#" * level + f" {title}（{ch['cum']}）"
            if marks and tuple(p) in marks:
                label += "　" + "、".join(marks[tuple(p)])
            lines.append(label)
            walk(ch, p)
    walk(root, [])
    return lines

# 空标题节（标题下直到下一标题无任何条目）——两案都需要知晓
entry_linenos = {e["lineno"] for e in entries}
empty_headings = []
last_head = None
for n in nodes:
    if last_head is not None:
        # 上一个标题与当前标题之间无条目行 → 上一个标题为空节
        if not any(last_head["lineno"] < ln < n["lineno"] for ln in entry_linenos):
            empty_headings.append(last_head)
    last_head = n
# 最后一个标题到文件尾
if last_head is not None and not any(ln > last_head["lineno"] for ln in entry_linenos):
    empty_headings.append(last_head)
empty_paths = [tuple(n["path"]) for n in empty_headings if len(n["path"]) >= 1]

# 案一 H1 规范排序
H1_ORDER = ["前言", "关于", H1_HIST, H1_TRAD, H1_ME, H1_VT, H1_SLM, "归类待裁"]
root1 = build_full_tree(s1_tree)
root1["children"] = OrderedDict(
    sorted(root1["children"].items(), key=lambda kv: H1_ORDER.index(kv[0]) if kv[0] in H1_ORDER else 99))
scheme1_lines = render_tree(root1)

marks2 = {}
for p in small:
    marks2.setdefault(p, []).append(f"【小 {s2_tree[p]} 条】")
for p, slugs in misplaced_by_node.items():
    if len(slugs) >= 3:
        marks2.setdefault(p, []).append(f"【疑位 {len(slugs)} 条·待终审】")
# 案二以现行标题树为真值种子（含空节）
head_paths2 = [tuple(n["path"]) for n in nodes]
root2 = build_full_tree(s2_tree, seed_paths=head_paths2)
scheme2_lines = render_tree(root2, marks2)

def subtree_sum(source_path):
    return sum(c for p, c in s2_tree.items() if tuple(p)[: len(source_path)] == tuple(source_path))

MOVED = [
    ("犹太哲学（自西史）", subtree_sum(("西方哲学史", "犹太哲学")), "哲学传统＞犹太哲学"),
    ("语言哲学＋语义学＋语用学", subtree_sum(("哲学通论", "语言哲学与逻辑学", "语言哲学"))
     + subtree_sum(("哲学通论", "语言哲学与逻辑学", "语义学"))
     + subtree_sum(("哲学通论", "语言哲学与逻辑学", "语用学")), "形而上学与认识论＞语言哲学"),
    ("逻辑学五节", subtree_sum(("哲学通论", "语言哲学与逻辑学")) - subtree_sum(("哲学通论", "语言哲学与逻辑学", "语言哲学"))
     - subtree_sum(("哲学通论", "语言哲学与逻辑学", "语义学"))
     - subtree_sum(("哲学通论", "语言哲学与逻辑学", "语用学")), "科学、逻辑与数学＞逻辑学与逻辑哲学"),
    ("自由意志", subtree_sum(("哲学通论", "形而上学", "自由意志")), "形而上学与认识论＞行动哲学"),
    ("决策与博弈论", subtree_sum(("哲学通论", "决策与博弈论")), "形而上学与认识论＞行动哲学"),
    ("道德心理学＋行动哲学与理由论", subtree_sum(("哲学通论", "伦理学", "道德心理学"))
     + subtree_sum(("哲学通论", "伦理学", "行动哲学与理由论")), "形而上学与认识论＞行动哲学"),
    ("教育哲学", subtree_sum(("哲学通论", "教育哲学")), "科学、逻辑与数学＞社会科学哲学（PP：教育挂社科）"),
    ("技术哲学", subtree_sum(("科学哲学", "技术哲学")), "科学、逻辑与数学＞计算与信息哲学"),
    ("化学哲学", subtree_sum(("科学哲学", "化学哲学")), "科学、逻辑与数学＞物理科学哲学"),
    ("科学哲学史与学派", subtree_sum(("科学哲学", "科学哲学史与学派")), "科学、逻辑与数学＞一般科学哲学"),
    ("环境哲学", subtree_sum(("哲学通论", "环境哲学")), "价值理论＞应用伦理学"),
    ("经济哲学", subtree_sum(("哲学通论", "经济哲学")), "价值理论＞政治与社会哲学"),
    ("文化哲学", subtree_sum(("哲学通论", "文化哲学")), "价值理论＞政治与社会哲学"),
    ("出生与死亡哲学", subtree_sum(("哲学通论", "出生与死亡哲学")), "价值理论＞应用伦理学"),
]
moved_lines = ["", "## 相对现行的整建制变动（簇计数）", ""] + [
    f"- {name}（{cnt}）→ {dest}" for name, cnt, dest in MOVED] + [""]

hdr1 = [
    "# 案一骨架：PhilPapers 骨架＋本地细分（specs/055 预览，不填充条目）",
    "",
    "- 数据：mu-lu-s.md 全部 1883 链接行；H1/H2 按 PP 六大类锚定（挂载点逐页核实：决策博弈/道德心理→行动哲学、技术→计算与信息、化学→物理科学、教育→社会科学哲学、医学 PP 有类保留、环境/生死→应用伦理、经济/文化→政治与社会、犹太→哲学传统）。",
    "- 映射为区域优先＋确定性锚定表：史区/传统区整建制搬运；学科区（通论＋科学哲学）按表归位，### 及以下现行细分整建制随行。010 TSV 仅作校准审计不驱动归类。",
    "- 排序（选型后执行）：主题节内按语义聚簇，簇内按重要性/影响力（人工裁定，映射表留依据列）；史区人物簇内默认保留生年序（016 惯例）。",
    "- 单一归类；嵌套人物簇结构保留。",
    "",
] + moved_lines
hdr2 = [
    "# 案二骨架：现行四区＋逐条校准（specs/055 预览，不填充条目）",
    "",
    "- 树＝现行 mu-lu-s.md 原样（H1–H4）；标记为校准候选：【小】=少于 3 条待并入；【疑位】=节点内 PP 映射指向他域的条数（执行时逐条终审）。",
    "- 排序（选型后执行）：同案一（聚簇＋重要性/影响力）。",
    "- 增补候选见文末（PP 子类 ≥6 条且散布 ≥3 个 ## 节者）。",
    "",
]

(OUT / "skeleton-scheme1-pp.md").write_text("\n".join(hdr1 + scheme1_lines) + "\n", encoding="utf-8")
(OUT / "skeleton-scheme2-calibrate.md").write_text(
    "\n".join(hdr2 + scheme2_lines)
    + "\n\n## 增补候选（案二视角）\n\n"
    + "\n".join(f"- {sub}：共 {t} 条，散布 {n} 个 ## 节" for sub, t, n in add_cands)
    + "\n", encoding="utf-8")

stats = {
    "entries_total": len(entries),
    "conserved_ok": sum(s2_tree.values()) == len(entries) == sum(s1_tree.values()),
    "empty_headings": ["/".join(p) for p in empty_paths],
    "unmapped_after_manual": unmapped,
    "s1_h1_counts": {h1: sum(c for p, c in s1_tree.items() if p[0] == h1) for h1 in sorted({p[0] for p in s1_tree})},
    "s2_h1_counts": {h1: sum(c for p, c in s2_tree.items() if p[0] == h1) for h1 in sorted({p[0] for p in s2_tree})},
    "small_nodes": [list(p) for p in small],
    "misplaced_top": {"/".join(k): len(v) for k, v in sorted(misplaced_by_node.items(), key=lambda kv: -len(kv[1]))[:20]},
    "add_candidates": [{"sub": s, "total": t, "spread": n} for s, t, n in add_cands],
    "me_misc_entries": [e["slug"] for e in entries if PP.get(e["slug"], ("", "")) == ("Metaphysics and Epistemology", "M&E Misc")],
}
(OUT / "skeleton-stats.json").write_text(
    json.dumps(stats, ensure_ascii=False, indent=2), encoding="utf-8")

print("entries:", len(entries))
print("conserved:", stats["conserved_ok"])
print("unmapped_after_manual:", unmapped)
print("s1 H1:", stats["s1_h1_counts"])
print("s2 H1:", stats["s2_h1_counts"])
print("small nodes:", len(small))
print("add candidates:", stats["add_candidates"][:12])
print("misplaced top:", dict(list(stats["misplaced_top"].items())[:10]))
