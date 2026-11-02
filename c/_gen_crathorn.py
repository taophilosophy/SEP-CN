# -*- coding: utf-8 -*-
import io, re, os

root = r"D:\SEP-CN"
ledger_path = os.path.join(root, "tasks", "c", "crathorn.ledger.yaml")
src_path = os.path.join(root, "yuanwen", "c", "crathorn.md")
out_path = os.path.join(root, "c", "crathorn.md")

# --- parse ledger step2 by segment id ---
step2 = {}
cur_id = None
cur_key = None
buf = []
for line in io.open(ledger_path, encoding="utf-8").read().split("\n"):
    m = re.match(r"\s*-\s*id:\s*(\d+)\s*$", line)
    if m:
        if cur_id is not None and cur_key == "step2":
            step2[cur_id] = "\n".join(buf)
        cur_id = int(m.group(1)); cur_key = None; buf = []
        continue
    if cur_id is None:
        continue
    m = re.match(r"\s*(source|step1|step2):\s*\|-?\s*$", line)
    if m:
        if cur_key == "step2":
            step2[cur_id] = "\n".join(buf)
        cur_key = m.group(1); buf = []
        continue
    if cur_key == "step2":
        buf.append(line.rstrip("\n"))
if cur_id is not None and cur_key == "step2":
    step2[cur_id] = "\n".join(buf)

def s(i):
    t = step2.get(i, "")
    t = t.strip("\n")
    # strip common indentation of a block scalar (6 spaces from original)
    lines = t.split("\n")
    out = []
    for ln in lines:
        out.append(re.sub(r"^      ", "", ln))
    return "\n".join(out).strip()

# --- sections mapping: heading -> segment ids ---
sections = [
    ("1 生平与著作", [2, 3]),
    ("2 与其他学者的关系", [4, 5]),
    ("3 认识论", [6, 7, 8, 9, 10, 11]),
    ("4 语言哲学", [12, 13]),
    ("5 本体论与范畴", [14, 15, 16, 17]),
    ("6 原子论", [18, 19, 20, 21]),
]

# --- footnotes transcribed verbatim from source (lines after "## Related Entries") ---
src = io.open(src_path, encoding="utf-8").read().split("\n")
fn = []
grab = False
for line in src:
    if line.strip().startswith("[^"):
        grab = True
    if grab:
        fn.append(line)

H1 = "# 威廉·克雷索恩 Crathorn, William (Aurélien Robert)"
VER = "**首次发表于 2005 年 8 月 12 日；2022 年 2 月 24 日实质修订。**"

parts = [H1, "", VER, "", s(1), ""]
for heading, ids in sections:
    parts.append("## " + heading)
    parts.append("")
    for i in ids:
        parts.append(s(i))
        parts.append("")

parts.append("## 参考文献")
parts.append("")
parts.append("> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。")
parts.append("")
parts.append("### 原始文献")
parts.append("")
parts.append("#### 译本")
parts.append("")
parts.append("### 第二手文献")
parts.append("")
parts.append("## 学术工具")
parts.append("")
parts.append("> |   | [如何引用本词条](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=crathorn). |")
parts.append("> | --- | --- |")
parts.append("> |   | [预览本词条的 PDF 版本](https://leibniz.stanford.edu/friends/preview/crathorn/)（[SEP 之友协会](https://leibniz.stanford.edu/friends/)）。 |")
parts.append("> |   | [查找与本词条相关的话题与思想家](https://www.inphoproject.org/entity?sep=crathorn&redirect=True)（互联网哲学本体论项目，InPhO）。 |")
parts.append("> |   | [本词条的增强文献目录](https://philpapers.org/sep/crathorn/)（[PhilPapers](https://philpapers.org/)），含其数据库链接。 |")
parts.append("")
parts.append("## 其他网络资源")
parts.append("")
parts.append("[请与作者联系以提出建议。]")
parts.append("")
parts.append("## 相关词条")
parts.append("")
parts.append("亚里士多德 | 古代原子论 | 罗吉尔·培根 | 约翰·布里丹 | 沃尔特·查顿 | 罗伯特·霍尔柯特 | 威廉·奥卡姆")
parts.append("")
parts.extend(fn)
parts.append("")

out = "\n".join(parts)
io.open(out_path, "w", encoding="utf-8", newline="\n").write(out)
print("WROTE", out_path)
print("n_step2_used:", len(step2))
print("n_footnotes:", len(fn))
print("footnote_keys_first:", fn[0][:40] if fn else None)
print("footnote_keys_last:", fn[-1][:40] if fn else None)
