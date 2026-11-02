# -*- coding: utf-8 -*-
"""组装最终译文 c/concept-emotion-india.md：
- step2 作为正文
- 插入节标题与引用块（引用块用 step2 内容 + 原文前缀 >）
- 尾部照录（References/Primary sources 表格/脚注定义原文不译）
"""
import json, re, os

here = r"D:\SEP-CN"
# 读取账本 step2
lines = open(os.path.join(here, "tasks", "c", "concept-emotion-india.ledger.yaml"), encoding="utf-8").read().split("\n")
entries = []; cur = None
for l in lines:
    if l.startswith("- id:"):
        if cur: entries.append(cur)
        cur = {"id": l.split(":",1)[1].strip()}
    elif cur is not None and l.startswith("  step2:"):
        cur["step2"] = json.loads(l.split(":",1)[1].strip())
if cur: entries.append(cur)
S = {e["id"]: e["step2"] for e in entries}

# 读取英文源
src = open(os.path.join(here, "yuanwen", "c", "concept-emotion-india.md"), encoding="utf-8").read()
blocks = src.split("\n\n")

def is_quote(blk):
    return blk.strip().startswith(">")

# 构造正文：遍历段落，遇节标题输出中文节标题，遇引用块加 > 前缀
zh_headings = {
 "## 1. The Nyāya-Vaiśeṣika account of the emotions": "## 1. 正理—胜论论情感",
 "## 2. The Advaita Vedānta account of the emotions": "## 2. 不二吠檀多论情感",
 "## 3. The Sāṃkhya-Yoga account of the emotions": "## 3. 数论—瑜伽论情感",
 "## 4. The Buddhist account of the emotions": "## 4. 佛教论情感",
 "### 4.1 Buddhist cognition": "### 4.1 佛教的认知",
 "### 4.2 Śāntarakṣita on love and hatred": "### 4.2 寂护论爱与憎",
 "### 4.3 Cognitions, emotions and kleśas": "### 4.3 认知、情感与烦恼",
 "### 4.4 Buddhist emotions": "### 4.4 佛教的情感",
 "## 5. Conclusion": "## 5. 结论",
}

# pid -> 对应块索引（引用块映射）
pid_block = {
 "p1":2,"p2":3,"p3":4,
 "p4":6,"p5":7,"p6":8,"p7":9,"p8":10,"p9":11,"p10":12,"p11":13,"p12":14,"p13":15,
 "p14":17,"p15":18,"p16":19,
 "p17":21,"p18":22,"p19":23,"p20":24,"p21":25,"p22":26,"p23":27,"p24":28,"p25":29,"p26":30,"p27":31,"p28":32,
 "p29":34,"p30":36,"p31":37,"p32":38,"p33":39,"p34":40,"p35":41,
 "p36":43,"p37":44,"p38":45,"p39":46,"p40":47,"p41":48,"p42":49,"p43":50,"p44":51,"p45":52,
 "p46":54,"p47":55,"p48":56,"p49":57,"p50":58,"p51":59,"p52":60,
 "p53":62,"p54":64,
}

# 构建输出
out = []
out.append("# 古典印度哲学中的情感概念 concept of emotion (Joerg Tuske)")
out.append("")
out.append("**首次发表于 2011 年 3 月 1 日；2025 年 10 月 30 日实质修订。**")
out.append("")

# 正文段落，插入节标题
# 节标题出现的块号（在段落之前）
sec_before = {}
for pid, blk_i in pid_block.items():
    # 找前一块是否标题
    pass

# 顺序遍历所有块号 2..64，按需输出标题或段落
# 标题块号集合
head_block = {5:"## 1. The Nyāya-Vaiśeṣika account of the emotions",
              16:"## 2. The Advaita Vedānta account of the emotions",
              20:"## 3. The Sāṃkhya-Yoga account of the emotions",
              33:"## 4. The Buddhist account of the emotions",
              35:"### 4.1 Buddhist cognition",
              42:"### 4.2 Śāntarakṣita on love and hatred",
              53:"### 4.3 Cognitions, emotions and kleśas",
              61:"### 4.4 Buddhist emotions",
              63:"## 5. Conclusion"}
inv_block = {v:k for k,v in pid_block.items()}

for bi in range(2, 65):
    if bi in head_block:
        en = head_block[bi]
        out.append(zh_headings[en])
        out.append("")
        continue
    if bi in inv_block:
        pid = inv_block[bi]
        blk = blocks[bi].strip()
        if is_quote(blk):
            # 引用块：加 > 前缀
            for ln in S[pid].split("\n"):
                out.append("> " + ln if ln else ">")
        else:
            out.append(S[pid])
        out.append("")

# 尾部照录：References 到文件末尾
i = src.index("## References")
tail = src[i:]
# 节标题与说明按体例译中文（参考文献条目照录原文不译）
tail = tail.replace("### Primary sources", "### 原始文献")
tail = tail.replace("### Secondary sources", "### 第二手文献")
tail = tail.replace("## Academic Tools", "## 学术工具")
tail = tail.replace("## Other Internet Resources", "## 其他网络资源")
tail = tail.replace("## Related Entries", "## 相关词条")
# 学术工具链接文本译中文
tail = tail.replace("[How to cite this entry]", "[如何引用本词条]")
tail = tail.replace("[Preview the PDF version of this entry]", "[预览本词条的 PDF 版本]")
tail = tail.replace(" at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/).",
                    "（[SEP 之友协会](https://leibniz.stanford.edu/friends/)）。")
tail = tail.replace("[Look up topics and thinkers related to this entry]", "[查找与本词条相关的话题与思想家]")
tail = tail.replace(" at the Internet Philosophy Ontology Project (InPhO).",
                    "（互联网哲学本体论项目，InPhO）。")
tail = tail.replace("[Enhanced bibliography for this entry]", "[本词条的增强文献目录]")
tail = tail.replace(" at [PhilPapers](https://philpapers.org/), with links to its database.",
                    "（[PhilPapers](https://philpapers.org/)），含其数据库链接。")
# 相关词条译中文名（保留原词条名对照；站内链接由管线统一挂接，不造死链）
rel_zh = ("早期中国哲学中的情 | 法称 | 早期现代印度的分析哲学 | 情感 | "
          "情感：17 世纪和 18 世纪的情感理论 | 情感：中世纪情感理论 | 爱 | "
          "印度佛教哲学中的心灵 | 快乐 | 寂护")
tail = re.sub(r"Chinese Philosophy: emotions in early Chinese Philosophy \| Dharmakīrti \| "
              r"Early Modern India, analytic philosophy in \| emotion \| "
              r"emotion: 17th and 18th century theories of \| emotion: medieval theories of \| "
              r"love \| mind: in Indian Buddhist Philosophy \| pleasure \| Śāntarakṣita",
              rel_zh, tail)
out.append(tail.rstrip("\n"))

final = "\n".join(out).rstrip("\n") + "\n"
open(os.path.join(here, "c", "concept-emotion-india.md"), "w", encoding="utf-8").write(final)
print("written", len(final), "chars")
