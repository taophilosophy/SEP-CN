# T209 证据：imprecise-probabilities ex-04 源审计

- 日期：2026-11-27
- 任务：T209（T154 拆站第 1 项）；状态推进目标 `ex-04_checked`
- 条目：`i/imprecise-probabilities`；版本钉 `pubinfo Feb 19, 2019／Spring 2019／sha256 ae9016a1…0767`
- 源文：`en/i/imprecise-probabilities.md`（119,763 字节／759 行）；原始 HTML 冻结，不改
- 方案：`results/t154-decomposition.md`

## 一、机检面

| 检查器 | 结果 | 说明 |
| ---- | ---- | ---- |
| `en_integrity.py imprecise-probabilities` | clean 1/1，hard 0，errors 0 | 镜像与 `html/` 一致；图片／资产引用闭包无缺件 |
| `en_source_audit.py imprecise-probabilities` | hard 0；warn 10；info 0 | `entry_links 7／external_links 15／math_inline 366／math_display 4／tables 2／headings 31` |
| `check_math.py imprecise-probabilities` | formulas 370；missing 0；unbalanced 6 | 370＝display 4＋行内 366；6 条 unbalanced 均见 §三 |

`en_source_audit` 的 `tables: 2` 含 Table 1 与其后的说明行判定差异；人工复核确认正文表格块为 **1 块**（Table 1，5 行×4 列），见 §四。

## 二、三段式汇总

### 1. 候选总数

- `en_source_audit` warn：**10 条**（`typo_candidate` 类）。
- `check_math` unbalanced：**6 条**（行内 `$` 奇偶启发式）。
- 合计候选 **16 条**；hard／Critical 候选 **0**。

### 2. 豁免类计数

| 豁免类 | 条数 | 依据 |
| ---- | ---- | ---- |
| 存档 URL 年份串（`fall2014`／`win2012`／`spr2014`／`win2011`／`win2013`／`fall2013`／`isipta15`） | 7 | URL 路径中的年份／会议名，非错字 |
| 公式占位剥除后的重复词（`and   and`） | 1 | 原文 `between $A$ and $B$`；数学被剥离后相邻 |
| 标题与正文相邻（`evidence`／`Evidence`） | 1 | 2.3 节标题＋正文首词，非重复 |
| 引用年份后缀列表（`2008a,b`） | 1 | Norton 2007, 2008a,b 的规范写法 |
| `$` 后接数字的货币启发式（`$0`／`$1`） | 6 | 数学以数字起首（`$0$`、`$1$`、`$1/2$`、`$1-\alpha$`），被 `check_math` 当货币剥除后误判 |
| **合计** | **16** | 全部 false-positive，无文字缺陷、无格式补丁需求 |

### 3. 逐条定性结论

| # | 候选 | 位置 | 定性 | 处置 |
| ---- | ---- | ---- | ---- | ---- |
| 1 | `isipta15` | L403 文献 URL | false-positive | 不建勘误／补丁 |
| 2 | `fall2014` | 文献 URL（存档版） | false-positive | 同上 |
| 3 | `win2012` | 文献 URL（存档版） | false-positive | 同上 |
| 4 | `spr2014` | 文献 URL（存档版） | false-positive | 同上 |
| 5 | `win2011` | 文献 URL（存档版） | false-positive | 同上 |
| 6 | `win2013` | 文献 URL（存档版） | false-positive | 同上 |
| 7 | `fall2013` | 文献 URL（存档版） | false-positive | 同上 |
| 8 | `and   and` | L116 引块 | false-positive（数学剥离） | 同上 |
| 9 | `evidence`／`Evidence` | §2.3 标题＋正文 | false-positive（跨块相邻） | 同上 |
| 10 | `2008a,b` | L210 正文 | false-positive（年份后缀） | 同上 |
| 11 | `- $0 = p(\emptyset)…=1$` | L40 列表 | false-positive（`$0` 被当货币） | 同上 |
| 12 | `$p(X \cap Y)$…` 行 | L194 | false-positive（行内 `$0$`） | 同上 |
| 13 | `$p(X \cup Y)$…` 行 | L198 | false-positive（行内 `$1$`） | 同上 |
| 14 | `learning $Y$…` 行 | L246 | false-positive（`$1/2$`） | 同上 |
| 15 | `- Win $1-\alpha$…` | L317 | false-positive（`$1` 起首） | 同上 |
| 16 | `- Lose $1- \alpha $…` | L318 | false-positive（同上） | 同上 |

**结论**：无 Critical／Major／Minor；不建全局勘误条，不建格式补丁。

## 三、14 类构件复核（验收口径）

| # | 构件类 | 命中 | 计数 | 备注 |
| ---- | ---- | ---- | ---- | ---- |
| 1 | H2 | 有 | 8 | §1–§4＋References／Academic Tools／OIR／Related Entries |
| 2 | H3+ | 有 | 18 | H3 16＋H4 2 |
| 3 | 脚注定义 | 有 | 189 | 唯一键 189，无重复定义 |
| 4 | 链接 | 有 | 21 | 文献／工具／OIR 链接 |
| 5 | 图片 | 有 | 2 | `two-by-two.png`、`joyces-diagram.png` 均在 `assets/imprecise-probabilities/` |
| 6 | 表格块 | 有 | 1 | Table 1：5 行（含表头）×4 列 |
| 7 | 引块 | 有 | 15 块／19 行 | 含 Keynes、Sturgeon、Walley、Kaplan 等 |
| 8 | 列表项 | 有 | 21 | 全部一级 |
| 9 | 嵌套列表 | 无 | 0 | 译文不得自行制造 |
| 10 | 行内公式 | 有 | 366 | `en_source_audit` 与 `check_math` 一致 |
| 11 | display 公式 | 有 | 4 | L59／L196／L200／L276 |
| 12 | LaTeX 环境 | 有 | 1 | L276 `\begin{align}`，与 `\end{align}` 配对 |
| 13 | 代码块 | 无 | 0 | 译文不得新增 |
| 14 | 加粗 | 有 | 1 | 1 处 `**First published…**` |

**命中 12／14**，与 060 spec “14 类格式构件占 12 类”一致。

## 四、脚注与资产核验

- 脚注定义 189 条，唯一键 189，重复定义 0。
- 正文引用 179 处，唯一键 137（多次引用为正常）。
- 无悬空引用；唯一例外 `[^key]` 出现在 L358 的转换说明引块（`原文参考文献已转为脚注引用…`），为转换层固定说明，非正文引用，判 false-positive。
- 未在正文引用的定义 52 条，属参考文献节“只列不引”条目，符合 SEP 体例。
- 图片 2 幅路径均可解析；`assets/imprecise-probabilities/` 下文件存在。
- Table 1 结构完整（表头 `R/B/Y`＋I–IV 四行）。

## 五、G13 判定

warn 10 条全部为 URL／引用写法／数学占位误报，无 A–E 类源侧缺陷候选；**无需建 G13 豁免清单**。

## 六、结论与下一步

- ex-04 源审计通过：hard 0，16 条候选全部定性为 false-positive，构件 12/14、脚注 189、图 2、表 1 均已核实。
- 不建勘误、不建补丁；译文阶段按 `results/t154-decomposition.md` §二 的 14 类清单验“构件无丢失”。
- 下一步 T210：tr-02 样章 §1–§1.2（14,244 源字符、76 行内＋1 display、35 脚注引用、1 引块、13 列表项）。
