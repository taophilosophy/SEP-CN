# -*- coding: utf-8 -*-
"""临时装配：从 hare.ledger.yaml 抽 step2 组装 h/hare.md 完整稿（用完即删）。"""
import io, re, os

ROOT = r"D:\SEP-CN"
LEDGER = os.path.join(ROOT, "tasks", "h", "hare.ledger.yaml")
OUT = os.path.join(ROOT, "h", "hare.md")
SRC = os.path.join(ROOT, "yuanwen", "h", "hare.md")


def read(path):
    return io.open(path, encoding="utf-8").read()


def get_field(body, field):
    m = re.search(r'^    %s: \|(.*?)(?=^    (?:source|step1|step2): \||^  - id:|\Z)' % field,
                  body, re.M | re.S)
    if not m:
        return None
    lines = [ln[6:] for ln in m.group(1).split("\n") if ln.startswith("      ")]
    while lines and lines[0].strip() == "":
        lines.pop(0)
    while lines and lines[-1].strip() == "":
        lines.pop()
    return "\n".join(lines)


# 1) 解析账本 step2
txt = read(LEDGER)
chunks = re.split(r"^  - id: (\d+)\s*$", txt, flags=re.M)
segs = {}
for k in range(1, len(chunks), 2):
    sid = int(chunks[k])
    segs[sid] = {
        "source": get_field(chunks[k + 1], "source"),
        "step2": get_field(chunks[k + 1], "step2"),
    }
assert len(segs) == 110, len(segs)
for sid in range(1, 111):
    assert segs[sid]["step2"] is not None, sid

# 2) 源结构：正文段（块 2..119，含块 119 补充材料）+ 节标题
srclines = read(SRC).split("\n")
blocks = []
i = 0
while i < len(srclines):
    if srclines[i].strip() == "":
        i += 1
        continue
    buf = []
    while i < len(srclines) and srclines[i].strip() != "":
        buf.append(srclines[i])
        i += 1
    blocks.append("\n".join(buf))

# 标题译文（源 ## N. 标题 -> 中文）
HEADING_MAP = {
    "## 1. The Life and the Man": "## 1 生平与为人",
    "## 2. The Language of Morals": "## 2 道德的语言",
    "## 3. The Logic of Imperatives": "## 3 祈令的逻辑",
    "## 4. Decisions of Principle": "## 4 原则的决定",
    "## 5. Attending to Preferences": "## 5 关注偏好",
    "## 6. Possible People": "## 6 可能的人",
    "## 7. Levels of Moral Thinking": "## 7 道德思维的层次",
    "## 8. Traces of Positivism in Religion and Metaethics": "## 8 宗教与元伦理学中的实证主义痕迹",
    "## 9. Afterword": "## 9 后记",
}

# 3) 对位：账本 seg 1..109 == 源正文段 2..119；节标题插到对应 seg 前
# 源块 0=H1+版本,1=作者；正文段从块 2 起；块 119 是补充材料；块 120 起为参考文献等。
ref_idx = next(idx for idx, b in enumerate(blocks) if re.match(r"^## References", b))
body_blocks = [idx for idx in range(2, ref_idx)
               if not re.match(r"^#{1,6}\s", blocks[idx])]
assert len(body_blocks) == 109, len(body_blocks)

# 逐块走：正文段按序对应 seg；节标题记录插入点（在下一个 seg 前）
insert = {}  # seg_idx -> heading text
seg_counter = 0
for idx in range(2, ref_idx):
    b = blocks[idx]
    if re.match(r"^#{1,6}\s", b):
        assert b in HEADING_MAP, "未译标题: %s" % b
        # 标题在正文段 seg_counter 已消费之后、下一个 seg（seg_counter+1）之前
        insert[seg_counter + 1] = HEADING_MAP[b]
    else:
        seg_counter += 1
        assert blocks[idx] == segs[seg_counter]["source"], \
            "对位错 seg %d" % seg_counter
assert seg_counter == 109, seg_counter

# 4) 拼正文（seg 1..109，段间空行，标题按插入点）
body_parts = []
for sid in range(1, 110):
    if sid in insert:
        body_parts.append(insert[sid])
    body_parts.append(segs[sid]["step2"])
# 末段后若有标题（不应有）
assert 110 not in insert
BODY = "\n\n".join(body_parts)

# 5) 尾部（参考文献/学术工具/其他网络资源/相关词条/致谢）
TAIL = """## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

### 原始文献

### 研究文献与批评性讨论

## 学术工具

> |   | [如何引用本词条](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=hare). |
> | --- | --- |
> |   | [预览本词条的 PDF 版本](https://leibniz.stanford.edu/friends/preview/hare/)（[SEP 之友协会](https://leibniz.stanford.edu/friends/)）。 |
> |   | [查找与本词条相关的话题与思想家](https://www.inphoproject.org/entity?sep=hare&redirect=True)（互联网哲学本体论项目，InPhO）。 |
> |   | [本词条的增强文献目录](https://philpapers.org/sep/hare/)（[PhilPapers](https://philpapers.org/)），含其数据库链接。 |

## 其他网络资源

[请向作者提出改进建议。]

## 相关词条

道德认知主义与非认知主义 | 元伦理学 | 实践理性 | 意志薄弱

### 致谢

%s""" % segs[110]["step2"]

# 6) 脚注定义（照录源）
foot_lines = [ln for ln in read(SRC).split("\n")
              if ln.strip().startswith("[^") and re.match(r"^\[\^[^\]]+\]:", ln.strip())]
FOOTNOTES = "\n".join(foot_lines)

HEAD = "# 理查德·默尔文·黑尔 Hare, Richard Mervyn (Anthony Price)\n\n*首次发表于 2014 年 6 月 4 日；2019 年 5 月 10 日实质修订。*\n"

doc = HEAD + "\n\n" + BODY + "\n\n" + TAIL + "\n\n" + FOOTNOTES + "\n"
io.open(OUT, "w", encoding="utf-8", newline="\n").write(doc)
print("WROTE", OUT)
print("lines:", doc.count("\n"))
print("headings:", len(insert), "->", insert)
print("footnotes:", len(foot_lines))
