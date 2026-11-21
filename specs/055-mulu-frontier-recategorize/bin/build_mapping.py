#!/usr/bin/env python3
"""specs/055 执行阶段：全量映射表＋排序计划生成器（案一 PP 骨架＋本地细分）。

产出（results/）：
  mapping.tsv          slug／题名／现节／新节／档／en_key／母条slug／依据规则
  plan.json            新树计划（标题节点＋节注＋逐节条目序列，write_mulus.py 的输入）
  write-preview.md     新树预览（标题＋计数，条目不入）
  review-clusters.txt  叶节条目清单（≥5 条的节，供人工调整档位）

卡钉：链接集合守恒 1883 进=出、零重复、零丢失；映射逐行含依据。
只读分析，不写回任何源文件。
"""
import csv
import json
import re
from collections import OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
MULUS = ROOT / "mu-lu-s.md"
OUT = ROOT / "specs/055-mulu-frontier-recategorize/results"
OUT.mkdir(parents=True, exist_ok=True)

HEADING = re.compile(r"^(#{1,6}) (.+?)\s*$")
ENTRY = re.compile(r"^(\s*)\* \[(.+?)\]\(([^)]+\.md)\)\s*$")

def unescape(t):
    return t.replace("\\*", "*").replace("\\[", "[").replace("\\]", "]")

def slug_of(href):
    return href.rsplit("/", 1)[-1][:-3]

# ---------- 解析 ----------
nodes = []
entries = []
stack = []
anno_pending = []
raw_lines = MULUS.read_text(encoding="utf-8").splitlines()
for lineno, line in enumerate(raw_lines, 1):
    if line.startswith(">"):
        anno_pending.append(line)
        continue
    # 悬注规则：节注归属于其上方最近的标题（节首悬注与节尾悬注同源），遇任何非注行即落账
    if anno_pending and nodes:
        nodes[-1]["anno"].extend(anno_pending)
        anno_pending = []
    m = HEADING.match(line)
    if m:
        level, title = len(m.group(1)), unescape(m.group(2).strip())
        stack = stack[: level - 1]
        stack.append(title)
        nodes.append({"level": level, "title": title, "path": tuple(stack),
                      "anno": [], "lineno": lineno})
        continue
    m = ENTRY.match(line)
    if m:
        indent, text, href = len(m.group(1)), m.group(2), m.group(3)
        entries.append({"slug": slug_of(href), "href": href, "text": unescape(text),
                        "raw_text": text, "indent": indent, "path": tuple(stack),
                        "lineno": lineno})
if anno_pending and nodes:  # EOF 悬注
    nodes[-1]["anno"].extend(anno_pending)
    anno_pending = []

# 父条（嵌套簇）：同一标题内最近的前驱更小缩进条目
by_node = OrderedDict()
for e in entries:
    by_node.setdefault(e["path"], []).append(e)
for plist in by_node.values():
    st = []
    for e in plist:
        while st and st[-1]["indent"] >= e["indent"]:
            st.pop()
        e["parent_slug"] = st[-1]["slug"] if st else None
        st.append(e)

def en_key(text):
    """英文题排序键：①跳过中文字题与全角括号注记段（如“科亨-施佩克尔定理（KS 定理）”）
    从真正的英文题起算；②作者段＝串尾最外层尾部括号组（反向扫描最后一次 depth 由 1→0
    的“ (”，兼容作者名内嵌括号，如 Rineke (L.C.) Verbrugge）。
    2026-11-22 修正：旧 rfind(" (") 在作者名含内嵌括号时截断、在全角注记段内 ASCII 字母
    处误起算（specs/055 误报归因更正，见 execution-log.md）。"""
    s = text
    i = 0
    n = len(s)
    while i < n:
        ch = s[i]
        if ch == "（":
            j = s.find("）", i)
            if j == -1:
                break
            i = j + 1
        elif ord(ch) > 127 or ch in " -—–·":
            i += 1
        else:
            break
    s = s[i:]
    m = re.search(r"[A-Za-z]", s)
    if not m:
        return text.strip()
    s = s[m.start():]
    depth = 0
    author_start = None
    for idx in range(len(s) - 1, -1, -1):
        c = s[idx]
        if c == ")":
            depth += 1
        elif c == "(":
            depth -= 1
            if depth == 0 and author_start is None:
                author_start = idx
    if author_start is not None and author_start >= 1 and s[author_start - 1] == " ":
        s = s[:author_start]
    s = s.replace("’", "'").replace("‘", "'")
    s = re.sub(r"\\\[|\\\]|\[|\]", "", s)
    return s.strip().lower()
for e in entries:
    e["en_key"] = en_key(e["text"])

# ---------- 案一模型（与骨架预览同表；本文件为执行正典） ----------
H1_ME, H1_VT, H1_SLM = "形而上学与认识论", "价值理论", "科学、逻辑与数学"
H1_HIST, H1_TRAD = "西方哲学史", "哲学传统"

S1_TONG2 = {
    "形而上学": (H1_ME, "形而上学", False), "认识论": (H1_ME, "认识论", False),
    "心灵哲学": (H1_ME, "心灵哲学", False), "宗教哲学": (H1_ME, "宗教哲学", False),
    "政治哲学": (H1_VT, "政治与社会哲学", False), "法哲学": (H1_VT, "法哲学", False),
    "环境哲学": (H1_VT, "应用伦理学", True), "美学": (H1_VT, "美学", False),
    "女性主义哲学": (H1_VT, "性别、种族与性哲学", False),
    "教育哲学": (H1_SLM, "社会科学哲学", True), "经济哲学": (H1_VT, "政治与社会哲学", True),
    "决策与博弈论": (H1_ME, "行动哲学", True), "文化哲学": (H1_VT, "政治与社会哲学", True),
    "出生与死亡哲学": (H1_VT, "应用伦理学", True),
}
S1_LANG3 = {
    "语言哲学": (H1_ME, "语言哲学", False), "语义学": (H1_ME, "语言哲学", True),
    "语用学": (H1_ME, "语言哲学", True),
    "逻辑史与逻辑学家": (H1_SLM, "逻辑学与逻辑哲学", True),
    "经典逻辑与传统逻辑": (H1_SLM, "逻辑学与逻辑哲学", True),
    "非经典逻辑": (H1_SLM, "逻辑学与逻辑哲学", True),
    "数理逻辑与数学基础": (H1_SLM, "逻辑学与逻辑哲学", True),
    "悖论与非形式逻辑": (H1_SLM, "逻辑学与逻辑哲学", True),
}
S1_ETH3 = {
    "元伦理学": (H1_VT, "元伦理学", False), "规范伦理学": (H1_VT, "规范伦理学", False),
    "价值论": (H1_VT, "价值论", False),
    "道德心理学": (H1_ME, "行动哲学", True), "行动哲学与理由论": (H1_ME, "行动哲学", True),
    "社会伦理学": (H1_VT, "应用伦理学", True), "应用伦理学": (H1_VT, "应用伦理学", False),
}
S1_SCI2 = {
    "科学哲学史与学派": (H1_SLM, "一般科学哲学", True), "一般科学哲学": (H1_SLM, "一般科学哲学", False),
    "物理学哲学": (H1_SLM, "物理科学哲学", False), "化学哲学": (H1_SLM, "物理科学哲学", True),
    "数学哲学": (H1_SLM, "数学哲学", False), "生物学哲学": (H1_SLM, "生物哲学", False),
    "医学哲学": (H1_SLM, "医学哲学", False), "认知科学与神经科学哲学": (H1_SLM, "认知科学哲学", False),
    "信息与计算科学哲学": (H1_SLM, "计算与信息哲学", False), "社会科学哲学": (H1_SLM, "社会科学哲学", False),
    "技术哲学": (H1_SLM, "计算与信息哲学", True),
}

def _dest_path(dest, cur2, cur3, path, rule):
    h1n, h2n, carry = dest
    if cur3:
        mid = (cur3,) if cur3 != h2n else ()
        return (h1n, h2n) + mid + path[3:], rule
    if carry and cur2 and cur2 != h2n:
        return (h1n, h2n, cur2) + path[2:], rule + "+节名随行"
    return (h1n, h2n) + path[2:], rule

def s1_assign(e):
    path = e["path"]
    h1 = path[0] if path else ""
    cur2 = path[1] if len(path) > 1 else None
    cur3 = path[2] if len(path) > 2 else None
    if h1 in ("前言", "关于"):
        return path, "R0 导航保留"
    if h1 == "西方哲学史":
        if cur2 == "犹太哲学":
            return (H1_TRAD, "犹太哲学") + path[2:], "R1 犹太→哲学传统（PP 核实）"
        return path, "R2 西方哲学史整建制"
    if h1 == "世界哲学（欧洲以外）":
        return (H1_TRAD,) + path[1:], "R3 世界哲学→哲学传统整建制"
    if h1 == "科学哲学":
        dest = S1_SCI2.get(cur2, (H1_SLM, cur2, False))
        return _dest_path(dest, cur2, cur3, path, f"R4 科学哲学表:{cur2}")
    if h1 == "哲学通论":
        if cur2 == "形而上学" and cur3 == "自由意志":
            return (H1_ME, "行动哲学", "自由意志") + path[3:], "R5 自由意志→行动哲学（PP 核实）"
        if cur2 == "语言哲学与逻辑学":
            d = S1_LANG3.get(cur3, (H1_ME, "语言哲学", False))
            return _dest_path(d, cur2, cur3, path, f"R6 语言逻辑拆分:{cur3}")
        if cur2 == "伦理学":
            d = S1_ETH3.get(cur3, (H1_VT, "规范伦理学", False))
            return _dest_path(d, cur2, cur3, path, f"R7 伦理学表:{cur3}")
        d = S1_TONG2.get(cur2)
        if d:
            return _dest_path(d, cur2, cur3, path, f"R8 通论表:{cur2}")
        return ("归类待裁",) + path[1:], "R9 待裁"
    return ("归类待裁",) + path[1:], "R9 待裁"

for e in entries:
    e["new_path"], e["rule"] = s1_assign(e)

# ---------- 排序模型 ----------
TIER_RANK = {"S": 0, "A": 1, "B": 2}
# S＝学科枢纽主条目（SEP 总览条），人工核定；A＝经典专题（复审逐节补充）；其余 B
TIER_S = {
    "metaphysics", "epistemology", "philosophy-mathematics", "biology-philosophy",
    "linguistics", "cognitive-science", "metaethics", "philosophy-religion",
    "game-theory", "decision-theory", "chemistry", "medicine", "computer-science",
    "consciousness", "truth", "action", "freewill", "evil", "value-theory",
    "justice", "democracy", "scientific-method", "scientific-realism", "qm",
    "logic-classical", "logic-modal", "set-theory", "feminist-philosophy",
}
TIER_A = {
    # 本体论
    "abstract-objects", "object", "properties", "events", "substance", "existence",
    "facts", "mereology", "natural-kinds", "states-of-affairs",
    "ontological-commitment", "material-constitution", "supervenience",
    # 因果／同一性／时空／模态
    "causation-metaphysics", "causation-counterfactual",
    "identity", "identity-personal", "identity-time", "time", "temporal-parts",
    "possible-worlds", "modality-varieties",
    # 认识论
    "knowledge-analysis", "knowledge-how", "knowledge-acquaindescrip",
    "induction-problem", "epistemology-social", "disagreement", "reliabilism",
    # 语言哲学
    "propositions", "logical-form", "analysis",
    "meaning", "reference", "compositionality",
    "pragmatics", "speech-acts", "implicature",
    # 心灵
    "intentionality", "concepts", "mental-representation", "memory",
    "physicalism", "functionalism", "qualia", "color", "emotion",
    # 行动
    "compatibilism",
    # 宗教
    "ontological-arguments", "cosmological-argument", "teleological-arguments",
    "free-will-foreknowledge",
    # 伦理
    "consequentialism", "ethics-deontological", "ethics-virtue",
    "death", "life-meaning", "well-being", "hedonism", "value-intrinsic-extrinsic",
    # 政治
    "rights", "justice-distributive", "equality", "liberalism",
    "liberty-positive-negative", "authority", "political-obligation",
    "justice-global", "race",
    # 法
    "lawphil-nature", "legal-positivism", "natural-law-theories",
    # 美学／性别
    "beauty", "art-definition", "music", "feminism-ethics", "feminism-epistemology",
    "feminism-gender",
    # 科学哲学
    "confirmation", "thomas-kuhn", "popper", "laws-of-nature",
    # 物理／生物／数学／认知
    "quantum-field-theory", "evolution", "natural-selection", "species",
    "platonism-mathematics", "neuroscience",
    # 计算
    "artificial-intelligence", "information", "turing",
    # 逻辑
    "tarski", "goedel", "model-theory", "proof-theory", "type-theory",
    "logic-intuitionistic", "quantification",
}
# 校验：S/A 档 slug 必须实存于条目集
_known = {e["slug"] for e in entries}
_unknown = sorted((TIER_S | TIER_A) - _known)
if _unknown:
    print("!! TIER 表含未知 slug（已自动忽略）:", _unknown)
TIER_S &= _known
TIER_A &= _known

def tier_of(e):
    if e["parent_slug"] is not None:
        return "C"
    if e["slug"] in TIER_S:
        return "S"
    if e["slug"] in TIER_A:
        return "A"
    return "B"
for e in entries:
    e["tier"] = tier_of(e)

# ---------- 标题节点重要性排序（显式子序表；未列出的父节保持现行次序） ----------
NODE_ORDER = {
    ("西方哲学史", "古代哲学"): ["古典希腊哲学", "早期希腊自然哲学", "希腊化与罗马哲学", "古代哲学专题"],
    ("西方哲学史", "古代哲学", "古典希腊哲学"): ["柏拉图与学园", "亚里士多德与逍遥学派", "苏格拉底", "智者运动", "小苏格拉底学派"],
    ("西方哲学史", "近代哲学", "唯理论"): ["唯理论总论", "笛卡尔与笛卡尔学派", "莱布尼茨-沃尔夫学派", "斯宾诺莎", "剑桥柏拉图学派"],
    ("西方哲学史", "近代哲学", "经验论"): ["洛克", "休谟", "培根与霍布斯", "贝克莱", "苏格兰常识学派", "英国道德哲学与宗教哲学"],
    ("西方哲学史", "近代哲学", "德国古典哲学"): ["康德", "黑格尔", "费希特", "谢林"],
    ("西方哲学史", "现代哲学"): ["分析哲学", "现象学运动", "存在主义与诠释学", "实用主义与过程哲学",
        "后黑格尔与马克思主义", "非理性主义与生存哲学", "实证主义与科学主义", "功利主义与古典自由主义",
        "新康德主义", "英国观念论与实在论", "法兰克福学派", "现代政治哲学", "结构主义与符号学", "后结构主义", "解构哲学"],
    ("西方哲学史", "现代哲学", "分析哲学"): ["早期分析哲学", "分析形而上学", "分析语言哲学", "分析伦理学与政治哲学", "日常语言哲学"],
    ("西方哲学史", "现代哲学", "后黑格尔与马克思主义"): ["马克思与恩格斯", "青年黑格尔派", "西方马克思主义"],
    ("西方哲学史", "现代哲学", "非理性主义与生存哲学"): ["尼采", "叔本华", "克尔凯郭尔"],
    ("形而上学与认识论",): ["形而上学", "认识论", "语言哲学", "心灵哲学", "行动哲学", "宗教哲学"],
    ("形而上学与认识论", "形而上学"): ["本体论", "因果关系", "同一性与变化", "时间与空间哲学", "模态与可能世界", "哲学中的神秘传统"],
    ("形而上学与认识论", "行动哲学"): ["自由意志", "决策与博弈论", "道德心理学", "行动哲学与理由论"],
    ("形而上学与认识论", "心灵哲学"): ["心灵哲学总论", "意识", "知觉", "心理现象与认知科学", "心灵因果性",
        "物理主义与二元论", "延展心灵与外在主义", "他心问题", "情感"],
    ("形而上学与认识论", "宗教哲学"): ["宗教哲学总论", "上帝存在的论证", "神学与教义", "基督教神学", "宗教与科学"],
    ("价值理论",): ["规范伦理学", "元伦理学", "应用伦理学", "价值论", "政治与社会哲学", "法哲学", "美学", "性别、种族与性哲学"],
    ("价值理论", "应用伦理学"): ["社会伦理学", "环境哲学", "出生与死亡哲学"],
    ("价值理论", "政治与社会哲学"): ["政治理论", "正义理论", "民主理论", "自由主义与共和主义", "政治义务与合法性",
        "全球正义与移民", "种族哲学", "社会理论与公共哲学", "经济哲学", "文化哲学"],
    ("科学、逻辑与数学",): ["逻辑学与逻辑哲学", "一般科学哲学", "物理科学哲学", "生物哲学", "数学哲学",
        "认知科学哲学", "计算与信息哲学", "医学哲学", "社会科学哲学"],
}

def order_children(parent_path, child_nodes):
    """child_nodes: [{path,...}]（首次出现序）→ NODE_ORDER 显式序在前，其余保持原序。"""
    explicit = NODE_ORDER.get(tuple(parent_path), [])
    seen_order = {n["path"][-1]: i for i, n in enumerate(child_nodes)}
    def keyf(n):
        t = n["path"][-1]
        return (explicit.index(t) if t in explicit else len(explicit), seen_order[t])
    return sorted(child_nodes, key=keyf)

# ---------- 计划树装配 ----------
# 新树节点集合：全部条目 new_path 前缀 + 现行标题树中仍存在的节点（以 new_path 前缀形式出现）
new_tree = OrderedDict()  # path -> {"anno": [...], "entries": [...], "order": int}
order_counter = 0
for n in nodes:
    p = n["path"]
    if p and p[0] in ("前言", "关于"):
        continue  # 前言/关于整段原样保留
    if p not in new_tree:
        new_tree[p] = {"anno": [], "entries": [], "order": order_counter}
        order_counter += 1
for e in entries:
    p = e["new_path"]
    if p[0] in ("前言", "关于"):
        continue
    if p not in new_tree:
        new_tree[p] = {"anno": [], "entries": [], "order": order_counter}
        order_counter += 1
    new_tree[p]["entries"].append(e)
# 节注迁移：现行标题的节注随其对应新树节点（映射：现行 path → 找第一条以它为前缀的 new_path 条目所在新节点；
# 对整建制搬运区，现行 path 直接映射到 new_path 前缀重写后的节点）
def anno_target(n):
    p = n["path"]
    # 构造该标题对应的新路径：对每个以 p 为前缀的条目取 new_path[:len(p)]，众数即目标
    candidates = {}
    for e in entries:
        if len(e["path"]) >= len(p) and e["path"][: len(p)] == p:
            tgt = e["new_path"][: len(p)]
            candidates[tgt] = candidates.get(tgt, 0) + 1
    if not candidates:
        return None
    return max(candidates, key=candidates.get)

for n in nodes:
    if n["anno"] and n["path"][0] not in ("前言", "关于"):
        tgt = anno_target(n)
        if tgt is None:
            print("!! 节注无目标:", "/".join(n["path"]))
        elif tgt in new_tree:
            new_tree[tgt]["anno"].extend(n["anno"])
        else:
            new_tree.setdefault(tgt, {"anno": n["anno"], "entries": [], "order": order_counter})
            order_counter += 1

# 前言/关于 原样行
fw_start = None
for i, line in enumerate(raw_lines):
    if line == "# 前言":
        fw_start = i
        break
# 前言/关于 覆盖从 "# 前言" 行到 "# 西方哲学史" 行前
hist_line = next(i for i, line in enumerate(raw_lines) if line == "# 西方哲学史")
FOREWORD_LINES = raw_lines[fw_start:hist_line]

def ordered_nodes():
    """返回深度优先排序后的节点列表（含合成父节点）。"""
    # 合成缺失的中间节点（含四个新设 H1）
    all_paths = set(new_tree)
    for p in list(new_tree):
        for i in range(1, len(p)):
            all_paths.add(p[:i])
    synth = []
    for p in sorted(all_paths):
        if p not in new_tree:
            new_tree[p] = {"anno": [], "entries": [], "order": 10_000 + len(synth), "synth": True}
            synth.append(p)
    for p, nd in new_tree.items():
        nd["path"] = p
    # 子节点索引在合成之后构建，保证新设 H1 子树可达
    children_map = {}
    for p, nd in new_tree.items():
        children_map.setdefault(p[:-1], []).append(nd)
    root_key = ()
    def walk(parent):
        ch = children_map.get(parent, [])
        ch = order_children(parent, ch)
        out = []
        for c in ch:
            out.append(c)
            out.extend(walk(c["path"]))
        return out
    return walk(root_key)

seq_nodes = ordered_nodes()

# 逐节条目排序：master（parent_slug=None）按 (tier, en_key) 稳定排序；嵌套成员随母条原序
def sort_entries(elist):
    masters = [e for e in elist if e["parent_slug"] is None]
    members = [e for e in elist if e["parent_slug"] is not None]
    masters.sort(key=lambda e: (TIER_RANK[e["tier"]], e["en_key"]))
    by_parent = OrderedDict()
    for m in members:
        by_parent.setdefault(m["parent_slug"], []).append(m)
    out = []
    for m in masters:
        out.append(m)
        out.extend(by_parent.get(m["slug"], []))
    # 极端情形：母条不在本节（悬挂成员）——按原序追加并告警
    hung = [m for m in members if m["parent_slug"] not in {x["slug"] for x in masters}]
    if hung:
        print("!! 悬挂嵌套成员:", [(m["slug"], m["parent_slug"]) for m in hung])
        out.extend(hung)
    return out

for nd in seq_nodes:
    if nd.get("entries"):
        nd["entries"] = sort_entries(nd["entries"])

# ---------- 卡钉对账 ----------
slugs = [e["slug"] for e in entries]
assert len(slugs) == 1883, f"条目数 {len(slugs)} ≠ 1883"
assert len(set(slugs)) == len(slugs), "重复 slug"
plan_total = sum(len(nd.get("entries", [])) for nd in seq_nodes)
fw_total = sum(1 for e in entries if e["path"][0] in ("前言", "关于"))
assert plan_total + fw_total == len(entries), \
    f"计划 {plan_total}＋前言关于 {fw_total} ≠ 解析 {len(entries)}"
bad = [e for e in entries if e["new_path"][0] == "归类待裁"]
assert not bad, f"归类待裁 {len(bad)}"

# ---------- 输出 ----------
with (OUT / "mapping.tsv").open("w", encoding="utf-8", newline="") as fh:
    w = csv.writer(fh, delimiter="\t", lineterminator="\n")
    w.writerow(["slug", "题名", "现节", "新节", "档", "en_key", "母条slug", "依据"])
    for e in entries:
        w.writerow([e["slug"], e["text"], "／".join(e["path"]), "／".join(e["new_path"]),
                    e["tier"], e["en_key"], e["parent_slug"] or "", e["rule"]])

plan = {
    "foreword_lines": FOREWORD_LINES,
    "sections": [
        {"path": list(nd["path"]), "anno": nd.get("anno", []),
         "entries": [{"slug": e["slug"], "href": e["href"], "text": e["text"],
                      "raw_text": e["raw_text"], "indent": e["indent"],
                      "tier": e["tier"]} for e in nd.get("entries", [])]}
        for nd in seq_nodes
    ],
    "stats": {"entries": len(entries), "nodes": len(seq_nodes)},
}
(OUT / "plan.json").write_text(json.dumps(plan, ensure_ascii=False, indent=1) + "\n",
                               encoding="utf-8", newline="\n")

prev = []
for nd in seq_nodes:
    p = nd["path"]
    prev.append("#" * len(p) + f" {p[-1]}（{len(nd.get('entries', []))}）")
    for a in nd.get("anno", []):
        prev.append(a)
(OUT / "write-preview.md").write_text("\n".join(prev) + "\n", encoding="utf-8", newline="\n")

with (OUT / "review-clusters.txt").open("w", encoding="utf-8", newline="\n") as fh:
    for nd in seq_nodes:
        el = nd.get("entries", [])
        if len(el) >= 5:
            fh.write(f"== {'／'.join(nd['path'])}（{len(el)}）\n")
            for e in el:
                ind = "  " if e["parent_slug"] else ""
                fh.write(f"{ind}[{e['tier']}] {e['en_key']}  ({e['slug']})\n")
            fh.write("\n")

print("entries:", len(entries), "nodes:", len(seq_nodes), "plan_total:", plan_total)
from collections import Counter
print("H1:", Counter(e["new_path"][0] for e in entries))
print("tier:", Counter(e["tier"] for e in entries))
