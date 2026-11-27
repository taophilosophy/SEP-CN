# T223 证据：axiom-choice tr-02 批 1（§2–§3）

- 日期：2026-11-27
- 任务：T223（T156 拆站第 3 项）；范围 en 第 78–135 行
- 产出：`zh/a/axiom-choice.md` §2–§3；账本 56 段（§1 30＋§2–§3 26）

## 一、结构守恒

| 项 | en §2–§3 | zh | 结论 |
| ---- | ---- | ---- | ---- |
| 非空块 | 26 | 26 | 类型序列一致（2 标题＋22 段＋2 display） |
| 脚注标记 | 15 | 15 | 等序 |
| 行内公式 | 226 | 227 | ＋1 为 en L86 定界符错位的正确拆读（见下） |
| display | 2 | 2 | 累积分层与可构造分层递归式 |
| 表格 | 1 块 7 行 | 1 块 7 行 | 极大原理年表；畸形表头照录 |

## 二、数学与勘误

- `check_math_zh` 硬错误 0；`\sI` 在脚注 note-11 中残留 2 处，已按 local.js 展开为 `\mathcal{I}`。
- en L86 `$\{a_1,\ldots,b_n\} with each pair \{a_i,b_i\} \in P$` 的公式定界符错位：英文短语被包入数学。译文按正确读法拆为两个公式；已入 `baseline/en-errata/en-errata.md` 第十八节（纯排版，无需译注）。
- 其余 SEP 宏（`\sH`／`\sA`／`\sP`／`\rD`／`\Def`／`\Ord`／`\inn`／`\amp`）均已展开。

## 三、术语

新增 13 条：atom 原子、universe 宇宙、support 支撑、hereditarily symmetric 遗传对称的、ordinal definability 序数可定义性、maximal principle 极大原理、partially ordered set 偏序集、upper bound 上界、chain 链、inductive 归纳的、generalized continuum hypothesis 广义连续统假设、finite character 有限特征、transcendental (mathematics) 超越性的。

沿用：automorphism 自同构、permutation model 置换模型、symmetric model 对称模型、forcing 力迫、constructible hierarchy 可构造分层、constructible universe 可构造宇宙、ordinal definable sets 序数可定义集、hereditarily ordinal definable sets 遗传序数可定义集、maximal element 极大元、nest 巢、strongly inductive 强归纳的、strongly reductive 强归约的、sampling 采样、potential choice function 潜在选择函数、transfinite induction 超限归纳。

## 四、机检

| 检查器 | 结果 |
| ---- | ---- |
| `check_style.py` | 0 issue |
| `check_quotes.py` | 0 处 |
| `check_math_zh.py` | 硬错误 0 |
| `check_terms.py --docs` | 硬错误 0；48 条缺译法为后续节尚未入文，属批范围 |
| `check_academic.py --strict` | 硬错误 0 |
| `check_pairs.py` | 样章缺口：标题 3 vs 10、公式 313 vs 532、尾节缺失；归 T224–T225 |

## 五、结论

T223 通过：§2–§3 入库，26 块／15 标记／2 display／7 行表守恒；226→227 行内公式的＋1 为已登记勘误的正确拆读；账本扩至 56 段。下一步 T224（§4–§5）。
