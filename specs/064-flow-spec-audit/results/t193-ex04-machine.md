# T193 评审记录：ex-04 机检面（logic-preference）

- 任务：T193（T142 拆分项一）；日期：2026-11-27；actor：trae-main
- 条目：`l/logic-preference`（当前 `cleared` 存根；源文 91 KB）
- 依据：`rules/04` ex-04、ADR-0052；T130 口径
- 范围：只做机检面；人工定性归 T194，G13 清单归 T195；本轮**不推进任务状态**

## 1 机检凭证

| 检查 | 命令 | 结果 |
| ---- | ---- | ---- |
| en 包完整性 | `python tools/en_integrity.py logic-preference --out ... --quiet` | audited 1、clean 1、hard 0、errors 0；mathjax 1、math_inline_entries 2、math_asset 0、default_absent 0 |
| HTML 本体审计 | `python tools/en_source_audit.py logic-preference --out ...` | **hard 0**（修 `\\[` 误计后；原误报 1）、warn 5、info 0；counts：entry_links 12、external_links 11、math_inline 417、math_display 43、tables 1、headings 40 |
| 公式保真 | `python tools/check_math.py logic-preference` | formulas 429、missing 0、unbalanced 1（见 §3） |

凭证：`results/t193-en-integrity.json`、`results/t193-en-source-audit.json`、`results/t193-check-math.json`。

## 2 四项计数

| 项 | 实测 | 备注 |
| ---- | ---- | ---- |
| 行内公式 | 417（`en_source_audit` math_inline）；43 处 display | 任务书 362 为旧口径；T194 已定 417 |
| 节集合 | H2 12（正文 8＋References／Academic Tools／Other Internet Resources／Related Entries）；H3 16 | 无缺节 |
| 表格／图片 | 表 1、图 2 | 表在源文 HTML，`tables: 1`；图 2 处 |
| 文献条目 | 脚注定义 67 条 | References 节为“转脚注引用”说明行，完整条目在文末脚注定义区 |

## 3 候选登记（交 T194 定性）

| 编号 | 类型 | 内容 | 初判 |
| ---- | ---- | ---- | ---- |
| H1 | hard `math_delim` | `\[` 45 处与 `\]` 43 处不配对 | 已修扫描器误报：真实 display 43/43，`\\[1em]` 不计；修复后 hard 0 |
| W1 | warn `heading_skip` | 标题层级 h2→h4 | 源 HTML 结构；非译文问题 |
| W2 | warn `typo_candidate` | `win2022`（archive URL） | 归档年份，非错字 |
| W3–W5 | warn `typo_candidate` | `(2013a,b)` 三处逗号无空格 | 引用键写法，非错字 |
| U1 | check_math unbalanced | 含 `$C_m(x)$`／`$1 \leq m \leq n$` 的行 | 行内 `$` 计数告警，missing 0；待 T194 判是否真失衡 |

## 4 结论

ex-04 机检面完成：en 包完整性 clean；源审计 hard 0（修复 `\\[` 误计后；原误报 1）＋warn 5（W1–W5，均疑非缺陷）；公式 missing 0；四项计数齐全。**T193 可勾选**；状态仍为 `cleared`，待 T194 逐条定性、T195 按需建 G13 清单后再 `advance --step ex-04`。

下一步：T194（人工定性）。
