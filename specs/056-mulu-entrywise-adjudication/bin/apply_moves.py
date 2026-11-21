#!/usr/bin/env python3
"""specs/056 应用器：按台账 MOVE 修正 mu-lu-s.md 归类。

读 results/adjudication-b*.tsv（seq 1..1883 全覆盖校验），收集 MOVE 行，
逐条"删除→重解析标题树→按（档，英文字题）定位插入目标节"，
保持节内排序惯例与簇结构。

卡钉：链接集合守恒 1883 进=出、零重复零丢失；目标节必须存在于现行树；
嵌套成员与带子条目的簇行不在本批 MOVE 内（断言拦截）。
"""
import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
RES = ROOT / "specs/056-mulu-entrywise-adjudication/results"
MULUS = ROOT / "mu-lu-s.md"

HEADING = re.compile(r"^(#{1,6}) (.+?)\s*$")
ENTRY = re.compile(r"^(\s*)\* \[(.+?)\]\(([^)]+\.md)\)\s*$")

def unesc(t):
    return t.replace("\\*", "*").replace("\\[", "[").replace("\\]", "]")

def slug_of(href):
    return href.rsplit("/", 1)[-1][:-3]

# ---- en_key（与 specs/055 build_mapping 同规则） ----
def en_key(text):
    s, i, n = text, 0, len(text)
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
    depth, start = 0, None
    for idx in range(len(s) - 1, -1, -1):
        c = s[idx]
        if c == ")":
            depth += 1
        elif c == "(":
            depth -= 1
            if depth == 0 and start is None:
                start = idx
    if start is not None and start >= 1 and s[start - 1] == " ":
        s = s[:start]
    return re.sub(r"\\\[|\\\]|\[|\]", "", s.replace("’", "'").replace("‘", "'")).strip().lower()

TIER_S = {"metaphysics", "epistemology", "philosophy-mathematics", "biology-philosophy",
          "linguistics", "cognitive-science", "metaethics", "philosophy-religion",
          "game-theory", "decision-theory", "chemistry", "medicine", "computer-science",
          "consciousness", "truth", "action", "freewill", "evil", "value-theory",
          "justice", "democracy", "scientific-method", "scientific-realism", "qm",
          "logic-classical", "logic-modal", "set-theory", "feminist-philosophy"}
TIER_A = {
    "abstract-objects", "object", "properties", "events", "substance", "existence", "facts",
    "mereology", "natural-kinds", "states-of-affairs", "ontological-commitment",
    "material-constitution", "supervenience", "causation-metaphysics",
    "causation-counterfactual", "identity", "identity-personal", "identity-time", "time",
    "temporal-parts", "possible-worlds", "modality-varieties", "knowledge-analysis",
    "knowledge-how", "knowledge-acquaindescrip", "induction-problem", "epistemology-social",
    "disagreement", "reliabilism", "propositions", "logical-form", "analysis", "meaning",
    "reference", "compositionality", "pragmatics", "speech-acts", "implicature",
    "intentionality", "concepts", "mental-representation", "memory", "physicalism",
    "functionalism", "qualia", "color", "emotion", "compatibilism", "ontological-arguments",
    "cosmological-argument", "teleological-arguments", "free-will-foreknowledge",
    "consequentialism", "ethics-deontological", "ethics-virtue", "death", "life-meaning",
    "well-being", "hedonism", "value-intrinsic-extrinsic", "rights", "justice-distributive",
    "equality", "liberalism", "liberty-positive-negative", "authority",
    "political-obligation", "justice-global", "race", "lawphil-nature", "legal-positivism",
    "natural-law-theories", "beauty", "art-definition", "music", "feminism-ethics",
    "feminism-epistemology", "feminism-gender", "confirmation", "thomas-kuhn", "popper",
    "laws-of-nature", "quantum-field-theory", "evolution", "natural-selection", "species",
    "platonism-mathematics", "neuroscience", "artificial-intelligence", "information",
    "turing", "tarski", "goedel", "model-theory", "proof-theory", "type-theory",
    "logic-intuitionistic", "quantification"}
RANK = {"S": 0, "A": 1, "B": 2}

def tier_of(slug):
    return "S" if slug in TIER_S else "A" if slug in TIER_A else "B"

# ---- 台账 ----
moves = {}
seen = set()
n_move_rows = 0
for f in sorted(RES.glob("adjudication-b*.tsv")):
    if f.name == "adjudication-b12.tsv":
        continue  # b12 为簇化批次（CLUS/MOVECLUS），由 apply_clusters.py 处理
    with f.open(encoding="utf-8", newline="") as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            seq = int(row["seq"])
            assert seq not in seen, f"seq 重复 {seq}（{f.name}）"
            seen.add(seq)
            if row["裁定"] == "MOVE":
                assert row["新节"].strip(), f"seq {seq} MOVE 缺新节"
                n_move_rows += 1
                moves[row["slug"]] = row["新节"].strip()
missing = set(range(1, 1884)) - seen
extra = seen - set(range(1, 1884))
assert not missing and not extra, f"台账覆盖缺口 {sorted(missing)[:5]}／越界 {sorted(extra)[:5]}"
assert len(moves) == n_move_rows, "slug 跨批重复"

# ---- 解析与搬运原语 ----
def parse_heads(lines):
    heads, stack = [], []
    for i, l in enumerate(lines):
        m = HEADING.match(l)
        if m:
            lv, t = len(m.group(1)), unesc(m.group(2).strip())
            stack = stack[: lv - 1] + [t]
            heads.append((i, tuple(stack)))
    return heads

def find_entry(lines, slug):
    hits = []
    for i, l in enumerate(lines):
        m = ENTRY.match(l)
        if m and slug_of(m.group(3)) == slug:
            hits.append((i, m))
    assert len(hits) == 1, f"{slug} 条目行数 {len(hits)}"
    return hits[0]

def section_bounds(heads, total, tpath):
    for idx, (li, path) in enumerate(heads):
        if path == tpath:
            end = heads[idx + 1][0] if idx + 1 < len(heads) else total
            return li, end
    raise AssertionError(f"目标节不存在：{'／'.join(tpath)}")

def blocks(lines, lo, hi):
    """节内条目块：母行＋其后连续嵌套行。"""
    out, cur = [], None
    for i in range(lo + 1, hi):
        m = ENTRY.match(lines[i])
        if m:
            if len(m.group(1)) == 0:
                if cur:
                    out.append(cur)
                cur = [i]
            else:
                assert cur is not None, f"嵌套行无母行：{lines[i].strip()}"
                cur.append(i)
        elif cur:
            out.append(cur)
            cur = None
    if cur:
        out.append(cur)
    return out

def insert_pos(lines, lo, hi, key, slug):
    for b in blocks(lines, lo, hi):
        m = ENTRY.match(lines[b[0]])
        bslug = slug_of(m.group(3))
        assert bslug != slug, f"{slug} 删除后仍在目标节"
        bkey = (RANK[tier_of(bslug)], en_key(unesc(m.group(2))))
        if bkey > key:
            return b[0]
    if blocks(lines, lo, hi):
        return blocks(lines, lo, hi)[-1][-1] + 1
    # 空节：跳过节注行后插入
    p = lo + 1
    while p < hi and lines[p].lstrip().startswith(">"):
        p += 1
    return p

lines = MULUS.read_text(encoding="utf-8").splitlines()
n0 = len([l for l in lines if ENTRY.match(l)])
report = []
skipped = []
def path_of(heads, i):
    cur = None
    for li, path in heads:
        if li < i:
            cur = path
        else:
            break
    return cur

for slug, target in sorted(moves.items()):
    heads = parse_heads(lines)
    i, m = find_entry(lines, slug)
    cur_path = path_of(heads, i)
    tpath = tuple(target.split("／"))
    if len(m.group(1)) > 0:
        # 嵌套成员：若母簇已搬至目标节，随簇达成
        if tuple(cur_path) == tpath:
            skipped.append((slug, "随簇"))
            continue
        raise AssertionError(f"{slug} 是嵌套成员且未随簇到位，需单独搬运")
    if tuple(cur_path) == tpath:
        skipped.append((slug, "已到位"))   # 幂等：重放时跳过
        continue
    j = i + 1
    while j < len(lines):
        mm = ENTRY.match(lines[j])
        if mm and len(mm.group(1)) > 0:
            j += 1
        else:
            break
    assert tuple(cur_path) != tpath, f"{slug} 新节与现节相同"
    block = lines[i:j]          # 母行＋嵌套子行整簇
    text, href = m.group(2), m.group(3)
    del lines[i:j]
    heads = parse_heads(lines)
    lo, hi = section_bounds(heads, len(lines), tpath)
    pos = insert_pos(lines, lo, hi, (RANK[tier_of(slug)], en_key(unesc(text))), slug)
    lines[pos:pos] = block
    report.append((slug, "／".join(cur_path), target))

n1 = len([l for l in lines if ENTRY.match(l)])
assert n0 == n1 == 1883, f"守恒破坏：{n0} → {n1}"

MULUS.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")

# 空节判定交权威门禁 check_mulu_s.py 第 [6] 项（整子树语义），此处不重复实现
print(f"应用 {len(report)} 条 MOVE（另有 {len(skipped)} 条随簇达成），条目守恒 {n0}={n1}")
if empty:
    print("空节预警：", "；".join(empty))
for slug, cur, tgt in report:
    print(f"  {slug}: {cur} → {tgt}")
