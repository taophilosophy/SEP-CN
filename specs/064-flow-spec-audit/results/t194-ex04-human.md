# T194 评审记录：ex-04 人工定性（logic-preference）

- 任务：T194（T142 拆分项二）；日期：2026-11-27；actor：trae-main
- 输入：T193 三份凭证（`t193-en-integrity.json`、`t193-en-source-audit.json`、`t193-check-math.json`）与 T193 评审记录
- 范围：候选逐条定性；**本轮不改 en／yuanwen，不建勘误或补丁**；任务状态仍 `cleared`

## 1 候选逐条定性

| 编号 | 来源 | 内容 | 定性 | 处置 |
| ---- | ---- | ---- | ---- | ---- |
| H1 | `en_source_audit` hard `math_delim` | `\[` 45／`\]` 43 不配对 | **false-positive** | 真实 display 定界符 43／43（`(?<!\\)\\\[`）；多出的 2 个是 `align` 内 `\\[1em]` 行距，非定界符。无需补丁 |
| W1 | `heading_skip` | h2→h4 | **false-positive** | 内容标题序列为 h2→h3→h4→h5；h2→h4 仅出现在页脚站点导航（Browse／About／Support SEP／Mirror Sites）。非正文结构问题 |
| W2 | `typo_candidate` | `win2022` | **false-positive** | SEP 归档 URL 年份，非错字 |
| W3–W5 | `typo_candidate` | `(2013a,b)` 三处逗号无空格 | **false-positive** | 作者-年份引用键习惯写法，非标点差错 |
| U1 | `check_math` unbalanced | 含 `$C_m(x)$`／`$1 \leq m \leq n$` 的行 | **false-positive** | 该行 8 个 `$`，成对；`$1` 被 `check_math` 的货币启发式误当金额剥掉，造成奇偶误判。公式内容 missing 0 |
| D1 | 任务书 362 vs 实测 417 | 行内公式数差 55 | **口径差异** | `en_source_audit` 实测 `math_inline=417`，`\(` 417／`\)` 417 全配对；362 为旧口径。T143 验收改按 417 执行 |

## 2 结构与书目

- 正文 H2 8 节＋References／Academic Tools／Other Internet Resources／Related Entries，共 12 个 H2；H3 16 个；内容层级无跳档。
- 表 1、图 2（与 T193 一致）。
- 脚注定义 67 条，逐条抽查均为文献条目（含 3 条“–––”同作者续列，年份为 2011a／2011b／2013b）；书目完整。
- 无漏抓：`en_integrity` clean，`default_absent_total=0`。

## 3 结论

- 源侧**无 Critical／Major 实质缺陷**；H1、W1–W5、U1 全部定性为工具启发式误报或引用习惯，**不建勘误条、不建补丁**。
- 唯一需回写的是口径：T143 的行内公式验收从“362 处”改为“417 处（实测）”。
- T194 可勾选；T195（G13 清单，按需）为 ex-04 最后一项；完成后再 `advance --step ex-04`。
