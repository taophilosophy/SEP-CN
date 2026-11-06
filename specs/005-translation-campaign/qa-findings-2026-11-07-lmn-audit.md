# L–N 批进度对账与纠正记录（2026-11-07）

**会话**：LMN-main-20261106　**范围**：`l/` `m/` `n/` 三批共 333 条正式词条（L 144 / M 139 / N 50）
**方法**：五方对账——SUMMARY 词条 × 成稿（行数/汉字/节/尾节）× 任务 JSON（状态机）× 段落账本（段数与 step2 填充）× git 最后改动。工具：`script/lmn_audit3.py`、`script/tmp/*`（`script/` 为草稿区，结论以本文件为准）。

## 1. 对账结论（2026-11-07 00:0x UTC 基线）

| 字母 | 正式词条 | 已成稿 | done | s3_checked（待复审） | 在途 | pending 任务 | 未建任务 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| L | 144 | 18（12.5%） | 2 | 16 | 0 | 1 | 125 |
| M | 139 | 5（3.6%） | 3 | 2（原 cleared） | 0 | 9 | 125 |
| N | 50 | 0 | 0 | 0 | 0 | 2 | 48 |
| 合计 | 333 | 23（6.9%） | 5 | 18 | 0 | 12 | 298 |

* 结构零偏差：有稿 23 条与有稿任务 23 条一一对应，无“有稿无任务/任务超前于成稿”。
* M 计数：SUMMARY 中 m/ 有 190 行（139 正式 + 51 别名行），progress.py 口径为 139，正确。
* 批次注记污染已修：`ledger.json` 的 m/n 注记原混入“l 批任务 19 已建”句（复制粘贴），已按实核重写；l/m/n 认领转交 `LMN-main-20261106`。

## 2. 偏差与处置

1. **在途状态滞后（M 2 条）**：`modesty-humility`（账本 91/91）、`montesquieu`（57/57）已 compose 成稿但状态停在 `cleared`。处置：核验守恒门与 compose 一致性后推进 `draft → s1 → s2 → s3`，见 §3。
2. **`lq.py map_related` 子节名歧义（新发现）**：源文相关词条 `Chinese Philosophy: ethics` 走“父: 子”分支时，子节名 `ethics` 与 `a/african-ethics` 的英文名同为 `ethics`，候选消解失败后落回通用循环取首个同名命中，误映射为“非洲伦理学”。处置：本批手工改为“中国哲学中的伦理学”；**工具未改**，列债务 §4。
3. **标题/别名术语错位**：`modesty-humility` 原题“谦虚与谦逊”把 modesty/humility 混作同义词对，正文却严格区分（谦逊 59 处 / 谦卑 39 处），别名行又把 humility 标成“谦逊”。处置：H1+SUMMARY+mu-lu-s 统一为“谦逊与谦卑”，别名行改“谦卑——见谦逊与谦卑”，术语表登记 modesty/humility/intellectual humility 三行。
4. **OIR 链接全角右括号**：`montesquieu` 两条其他网络资源链接用 `）` 收尾，Markdown 链接不闭合。处置：改 ASCII `)`。
5. **老批次参考文献形态**：`lady-masham` 用 `## 参考文献` 且缺 `### Sources/### Studies`，与 done 标准（`## References（引用注释）`+注记+源子标题照录）不符。处置：归正。
6. **prose 实修**：`montesquieu` 第 80 行 de-chain 1 处拆句；其余条目待逐条复审。

## 3. 已完成（2026-11-07）

* `m/modesty-humility` → s3_checked：91 段零数字差、defs 73=73、相关词条 10 项（修 1 项误映射）、标题与别名纠正、术语 3 行、人名 12 行；四检全绿。提交 48fb6052。
* `m/montesquieu` → s3_checked：57 段、defs 23=23、引文 9 封信 + SL 36 处逐句核销、OIR 链接修复、de-chain 实修 1 处、人名 8 行；四检全绿。提交 a4af969d。
* `l/lady-masham` → done：参考文献形态归正（含 2 子标题）、模板 marker 归位、人名 12 行补登；四检全绿。提交 575a72a9。

## 4. 债务登记

* **map_related 歧义未修**：凡是源文相关词条形如 `X: y` 且子节名 `y` 与其他词条英文名同形（如 `ethics`、`mind`、`language`），都可能误映射。建议修法：`父: 子` 候选消解失败时，先按父名 token 匹配 slug 片段（`chinese`→`ethics-chinese`），再回退；不得直接落回全局首个同名。修复前各批 s1 必须人工复核“相关词条”整行。
* **L 批 15 条 s3_checked 待 r1–r3**：lambert-auxerre、landmann-kalischer、law-ideology、lawphil-theory、legrand、leibniz-ethics、leibniz-evil、leibniz-logic-influence、leibniz-mind、leibniz-modal、leucippus、locke-on-medicine、logic-preference、lorenzo-valla、luxemburg。机检已出队列：marker 差 1 项/条为模板占位行缺失（同 lady-masham），节数差异集中在 References 子标题。
