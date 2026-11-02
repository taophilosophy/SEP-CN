# -*- coding: utf-8 -*-
"""临时装配脚本：从 ledger 抽取 step2 组装 c/cordemoy.md。用完即删。"""
import re, io, os

ROOT = r"D:\SEP-CN"
LEDGER = os.path.join(ROOT, "tasks", "c", "cordemoy.ledger.yaml")
OUT = os.path.join(ROOT, "c", "cordemoy.md")

txt = io.open(LEDGER, encoding="utf-8").read()

# 按段拆分
chunks = re.split(r"^  - id: (\d+)\s*$", txt, flags=re.M)
# chunks[0] 是头部，之后 (id, body) 成对
segs = {}
for i in range(1, len(chunks), 2):
    seg_id = int(chunks[i])
    body = chunks[i + 1]
    m = re.search(r"^    step2: \|(.*?)(?=^  - id:|\Z)", body, re.M | re.S)
    assert m, "no step2 for seg %d" % seg_id
    block = m.group(1)
    lines = [ln[6:] for ln in block.split("\n") if ln.startswith("      ")]
    # 去除首尾空行
    while lines and lines[0].strip() == "":
        lines.pop(0)
    while lines and lines[-1].strip() == "":
        lines.pop()
    segs[seg_id] = "\n".join(lines)

for k in sorted(segs):
    print("seg", k, "chars", len(segs[k]))

HEAD = (
    "# 热罗·德·科尔德穆瓦 Cordemoy, Géraud de (Fred Ablondi)\n"
    "\n"
    "**首次发表于 2005 年 1 月 8 日；2026 年 5 月 7 日实质修订。**\n"
)

def para(seg_id):
    return segs[seg_id]

body_parts = []
body_parts.append(para(1))
body_parts.append("## 1. 生平与著作")
for s in (2, 3, 4, 5):
    body_parts.append(para(s))
body_parts.append("## 2. 原子论")
for s in range(6, 18):
    body_parts.append(para(s))
body_parts.append("## 3. 偶因论")
for s in range(18, 23):
    body_parts.append(para(s))
body_parts.append("## 4. 心灵与身体")
for s in range(23, 26):
    body_parts.append(para(s))
body_parts.append("## 5. 语言与言语")
for s in range(26, 28):
    body_parts.append(para(s))

BODY = "\n\n".join(body_parts)

# 尾部节
TAIL = r"""## 参考文献

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

### 原始文献

### 研究文献与批评性讨论

## 学术工具

> |   | [如何引用本词条](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=cordemoy). |
> | --- | --- |
> |   | [预览本词条的 PDF 版本](https://leibniz.stanford.edu/friends/preview/cordemoy/)（[SEP 之友协会](https://leibniz.stanford.edu/friends/)）。 |
> |   | [查找与本词条相关的话题与思想家](https://www.inphoproject.org/entity?sep=cordemoy&redirect=True)（互联网哲学本体论项目，InPhO）。 |
> |   | [本词条的增强文献目录](https://philpapers.org/sep/cordemoy/)（[PhilPapers](https://philpapers.org/)），含其数据库链接。 |

## 其他网络资源

[请向作者提出改进建议。]

## 相关词条

勒内·笛卡尔 | 罗伯特·戴加贝 | 路易·德·拉弗尔热 | 尼古拉·马勒伯朗士"""

# 脚注定义（照录）
src = io.open(os.path.join(ROOT, "yuanwen", "c", "cordemoy.md"), encoding="utf-8").read()
foot_lines = [ln for ln in src.split("\n") if ln.strip().startswith("[^") and ln.strip().endswith(":")]
FOOTNOTES = "\n".join(foot_lines)

doc = HEAD + "\n\n" + BODY + "\n\n" + TAIL + "\n\n" + FOOTNOTES + "\n"
io.open(OUT, "w", encoding="utf-8", newline="\n").write(doc)
print("WROTE", OUT, "lines", doc.count("\n"), "footnotes", len(foot_lines))
