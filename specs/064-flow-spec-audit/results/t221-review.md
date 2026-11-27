# T221 证据：axiom-choice ex-04 源审计

- 日期：2026-11-27
- 任务：T221（T156 拆站第 1 项）；状态推进目标 `ex-04_checked`
- 条目：`a/axiom-choice`；版本钉 `Dec 10, 2021／Winter 2021／4a723bef…e9c8f`
- 源文：`en/a/axiom-choice.md`（70,819 字节／610 行）
- 方案：`results/t156-decomposition.md`

## 一、机检面

| 检查器 | 结果 | 说明 |
| ---- | ---- | ---- |
| `en_integrity.py axiom-choice` | clean 1/1，hard 0，errors 0 | 镜像与 `html/` 一致，资产引用闭包无缺件 |
| `en_source_audit.py axiom-choice` | hard 0；warn 3；info 0 | `math_inline 492／math_display 11／tables 5（工具口径）／headings 15` |
| `check_math.py axiom-choice` | formulas 547；missing 0；unbalanced 2 | 2 条均为 `$0 \ne 1$`（见下） |

## 二、三段式汇总

### 1. 候选总数

`en_source_audit` warn **3 条**；`check_math` unbalanced **2 条**。合计 **5 条**；hard／Critical 候选 **0**。

### 2. 豁免类计数

| 候选 | 条数 | 定性 |
| ---- | ---- | ---- |
| `orphan_note`：note-1–note-21 无引用 | 1（聚合） | false-positive：正文实有 21 处 `[^note-*]` 引用（逐键核对），工具未计入 |
| `doubled_word`：`and   and` | 1 | false-positive：公式被剥离后留下的连接词并列，非重复笔误 |
| `doubled_word`：`DAC … DAC` | 1 | false-positive：表格/公式内 `**DAC**$_X$` 与 `**DAC**$^*_X$` 被剥离后并置 |
| `check_math` unbalanced：`$0 \ne 1$`（L229、L407） | 2 | false-positive：工具把 LaTeX `\ne` 误当换行，`$` 实际成对（各 2 个） |

**真候选 0**；G13 无需建清单。

### 3. 逐条结论

- `orphan_note`：回源正文，`note-1`–`note-21` 均有引用；为工具口径差，不改 `en/`。
- 两个 `doubled_word`：均出现在公式/表格语境，剥离公式后形成假重复；不改。
- 两个 `unbalanced`：`$0 \ne 1$` 定界符成对；`check_math` 的 `\n` 转义误判。记录为工具缺陷候选，不影响译文。

## 三、脚注与构件

| 项 | 实测 |
| ---- | ---- |
| 脚注定义 | 111（含 `note-1`–`note-21`、7 条补充文档注记后的文献定义） |
| 正文引用 | 64 处／63 个唯一键；唯一“缺失”为 References 说明中的字面 `[^key]` |
| 未被正文引用的定义 | 49（书目条目，按 en 全量照录） |
| H2／H3 | 10／2（`Acknowledgments`、`Notes to Supplementary Document`） |
| 表格块 | 4（11／7／7／5 行） |
| 引块 | 14 行 |
| 列表 | 21 项 |
| 行内／display 公式 | 517／16（人工口径；工具 492／11） |
| 链接 | 11（§5 补充文档 1／尾节 7／补充注记 3） |
| 图片／代码块／LaTeX 环境 | 0／0／0 |

14 类构件命中 12／14；无图、无嵌套列表、无 LaTeX 环境与代码块。译文不得新增。

## 四、特殊结构

1. §5 末链接补充文档 `axiom-choice.choice-and-type-theory.md`；该文件不在本仓库 `en/` 内，译文保留链接与题名。
2. `### Notes to Supplementary Document: The Axiom of Choice and Type Theory` 下 7 条编号注记（非脚注）；T225 单列处理，不混入 111 条脚注定义。
3. 4 个表格块均须逐行保留；表格内公式与 `**DAC**` 等粗体记号不得改写。

## 五、结论

T221 满足验收：en 完整性 clean，源审计 hard 0，5 条候选全部定性为 false-positive／工具口径差，111 脚注闭合、14 类构件复核完成，无静默跳过。下一步 T222 样章（§1）。
