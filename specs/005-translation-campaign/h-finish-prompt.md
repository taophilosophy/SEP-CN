# H 批完成指令 v2（账本体段齐备，拼合 + 尾部 + 推进）

> 本指令用于**账本已覆盖全部正文段**（step1+step2 双版齐备）但文档未完整或未推进的词条。**不要再翻译正文**——只需拼合正文 + 从源复制尾部 + 检查 + 推进。工作目录 D:\SEP-CN。

## 你的任务
处理词条 **SLUG**，从当前状态推进到 **s3_checked**。不执行 r1/r2/r3/done。

## 第 1 步：拼合正文
读 `tasks/h/SLUG.ledger.yaml`，把每段 `step2` 按 `id` 顺序拼合成正文，写入 `h/SLUG.md`：
- H1 = SUMMARY 条目文字（`# 中文名 English-name (Authors)`）
- 版本行：`*首次发表于 YYYY 年 M 月 D 日；YYYY 年 M 月 D 日实质修订。*`（与 baseline pubinfo 一致）
- 段间空行；元素映射（图/表/数学/引块/行内引用）已在账本中，照抄。
- 若 `h/SLUG.md` 已有完整正文，直接进入第 2 步。

## 第 2 步：尾部节（从源复制/翻译，不逐段入账本）
对照 `yuanwen/h/SLUG.md` 尾部，按固定节序补全（账本只覆盖正文段，脚注/文献等尾部**不经账本**）：
- 脚注定义 `[^note-N]: ...`：键名逐字符一致，非中文照录、中国文献译中文（ADR-0011）。
- `## 参考文献`：非中文条目照录不译；中国文献译为中文；文首斜体说明行 `*非中文文献从原文照录，不作翻译；中国文献译为中文。*`。
- `## 学术工具`（archinfo/InPhO/PhilPapers 三行原样）、`## 其他网络资源`、`## 相关词条`（中文站内链接占位或照译）、`## 致谢`（有则）。
- 若源有正文段未入账本（对照空行分块，账本未覆盖的正文段）：**补译入账本**（step1+step2），不要跳过。

## 第 3 步：逐级推进到 s3（不跳步）
当前状态决定起级：
```
python tools/task_ops.py advance SLUG s1 --actor sub-SLUG --evidence "..."
python tools/task_ops.py advance SLUG s2 --actor sub-SLUG --evidence "..."
python tools/task_ops.py advance SLUG s3 --actor sub-SLUG --evidence "check_style 0; academic 0; math 0"
```
每级前跑对应检查：s1 对照源核销幻觉/漏译/增译/术语漂移/事实；s2 跑 `check_prose.py` 反欧化；s3 前 `check_style.py`+`check_academic.py --docs h/SLUG.md --strict`+`check_math.py` 全 0。**s3 学术门禁自动挂钩**，未过先修再推。

## 纪律
- 不 git 提交、不 push；不改其他词条/SUMMARY/登记册/baseline/en/yuanwen；不造备份。
- 若检查发现漏译/错译：报告，不要伪造。
- 完成后报告：最终状态、账本段数、s1/s2/s3 问题数、需人工复查项。
