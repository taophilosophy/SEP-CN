#!/usr/bin/env python3
"""specs/057 s1：现象学／存在主义／诠释学拆分独立＋内部 H4。

用户指令（2026-11-22）："不要管规模能细分就细分。全盘复核所有条目。
现象学、存在主义、诠释学需要拆分独立，内部也需要再划分。"

PP 依据（联网取证）：PhilPapers 三类的子类均按人物/学派设
  Phenomenology: Husserl / Heidegger / Henry / Gurwitsch ...
  Existentialism: Beauvoir* / Camus / Jaspers / Sartre / Misc
  Hermeneutics: Gadamer / Ricoeur / Misc

本脚本只做结构手术：把现有"### 现象学运动"＋"### 存在主义与诠释学"两节
重组为三节（现象学运动／存在主义／诠释学），加 H4，条目整簇随行；
守恒断言 1883。
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
MULUS = ROOT / "mu-lu-s.md"
ENTRY = re.compile(r"^(\s*)\* \[(.+?)\]\(([^)]+\.md)\)\s*$")

def slug_of(h):
    return h.rsplit("/", 1)[-1][:-3]

# 新结构：H3 -> [(H4, [块...])]；块 = 母 slug（其连续子行随行）
PLAN = [
    ("### 现象学运动", [
        ("#### 现象学总论", [["phenomenology"]]),
        ("#### 慕尼黑与哥廷根学派", [["phenomenology-mg", "reinach"]]),
        ("#### 布伦塔诺学派与早期现象学",
         [["brentano", "brentano-judgement"], ["stumpf"], ["marty"], ["ehrenfels"], ["meinong"], ["twardowski"]]),
        ("#### 胡塞尔", [["husserl"]]),
        ("#### 经典现象学",
         [["scheler"], ["stein"], ["ingarden"], ["landmann-kalischer"], ["schutz"]]),
        ("#### 海德格尔", [["heidegger", "heidegger-aesthetics"]]),
        ("#### 法国现象学", [["merleau-ponty"], ["michel-henry"], ["levinas"]]),
    ]),
    ("### 存在主义", [
        ("#### 存在主义总论", [["existentialism"], ["authenticity"]]),
        ("#### 萨特", [["sartre"]]),
        ("#### 波伏娃", [["beauvoir"]]),
        ("#### 加缪", [["camus"]]),
        ("#### 雅斯贝尔斯", [["jaspers"]]),
        ("#### 生命哲学与宗教实存主义",
         [["bergson"], ["marcel"], ["simone-weil"], ["susman-margarete"],
          ["gasset"], ["rosenstock-huessy"]]),
    ]),
    ("### 诠释学", [
        ("#### 诠释学总论", [["hermeneutics"]]),
        ("#### 狄尔泰与历史诠释学", [["dilthey"], ["yorck"]]),
        ("#### 伽达默尔", [["gadamer", "gadamer-aesthetics"]]),
        ("#### 利科", [["ricoeur"]]),
    ]),
]

lines = MULUS.read_text(encoding="utf-8").splitlines()

# 定位范围：### 现象学运动 → ### 实用主义与过程哲学
start = next(i for i, l in enumerate(lines) if l.strip() == "### 现象学运动")
end = next(i for i, l in enumerate(lines) if l.strip() == "### 实用主义与过程哲学")

# 提取范围内条目块（母行 + 连续子行）
blocks = {}
i = start + 1
while i < end:
    m = ENTRY.match(lines[i])
    if m:
        assert len(m.group(1)) == 0, f"范围首行即子条：{lines[i]}"
        blk = [lines[i]]
        j = i + 1
        while j < end and (mm := ENTRY.match(lines[j])) and len(mm.group(1)) > 0:
            blk.append(lines[j])
            j += 1
        blocks[slug_of(m.group(3))] = blk
        i = j
    else:
        i += 1

n_old = sum(len(b) for b in blocks.values())
assert n_old == 39, f"范围内条目行 {n_old} ≠ 39（20＋19）"

# 组装新文本
out = []
used = set()
for h3, h4s in PLAN:
    out.append(h3)
    out.append("")
    for h4, groups in h4s:
        out.append(h4)
        out.append("")
        for g in groups:
            mother = g[0]
            assert mother in blocks, f"缺块 {mother}"
            blk = blocks[mother]
            # 块内子条归属校验
            subs = [slug_of(ENTRY.match(l).group(3)) for l in blk[1:]]
            assert subs == g[1:] if len(g) > 1 else subs == [], \
                f"{mother} 子条不符：{subs} vs {g[1:]}"
            out.extend(blk)
            used.add(mother)
        out.append("")          # H4 段间空行
    if h3 != PLAN[-1][0]:
        pass

assert used == set(blocks), f"未用块：{set(blocks) - used}"
n_new = sum(1 for l in out if ENTRY.match(l))
assert n_new == 39, f"新块条目行 {n_new} ≠ 39"

lines[start:end] = out
n_all = sum(1 for l in lines if ENTRY.match(l))
assert n_all == 1883, f"全库守恒破坏：{n_all}"

MULUS.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
print(f"s1 完成：2 节 → 3 节（17 个 H4），条目 39 行守恒，全库 {n_all}")
