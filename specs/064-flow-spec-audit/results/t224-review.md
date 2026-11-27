# T224 证据：axiom-choice tr-02 批 2（§4–§5）

- 日期：2026-11-27
- 任务：T224（T156 拆站第 4 项）；范围 en 第 136–340 行
- 产出：`zh/a/axiom-choice.md` §4–§5；账本 146 段（§1 30＋§2–§3 26＋§4–§5 90）

## 一、结构守恒

| 项 | en §4–§5 | zh | 结论 |
| ---- | ---- | ---- | ---- |
| 非空块 | 90 | 90 | 类型序列一致（2 标题＋64 段＋12 display＋2 表＋7 列表＋3 引块） |
| 脚注标记 | 22 | 22 | 等序 |
| 行内公式 | 179 | 178 | 差 1 为孤立 `$\mu$` 按 ADR-0049 转文字 `*μ*` |
| display | 12 | 12 | 全部保留 |
| 表格 | 2 块 12 行 | 2 块 12 行 | 逐行对应 |

## 二、数学与勘误

- `check_math_zh` 硬错误 0；宏已展开（`\Fun`→`\mathrm{Fun}`、`\sH`→`\mathcal{H}`、`\inn`→`\in` 等）。
- en L86 公式定界符错位：译文拆为两个公式（勘误第十八节第 1 行）。
- en L243 末尾游离 `^{,}`：译文略去，已入勘误第十八节第 2 行（纯排版）。
- 孤立 `$\mu$` 按 ADR-0049 转文字 `*μ*`；其余希腊字母公式保留。

## 三、术语

新增 16 条：field of sets 集合域、injective (Boolean algebra) 内射的、compact 紧致的、Hausdorff space 豪斯多夫空间、normed linear space 赋范线性空间、dual space 对偶空间、extreme point 极点、distributive lattice 分配格、maximal ideal 极大理想、commutative ring 交换环、algebraically closed 代数闭的、basis 基、countable 可数的、Lebesgue measurable 勒贝格可测的、prime ideal 素理想、vector space (mathematics) 向量空间。

`vector space` 与 qm 语境“矢量空间”同形异义，已按撞形豁免分域，不合并。

## 四、机检

| 检查器 | 结果 |
| ---- | ---- |
| `check_style.py` | 0 issue |
| `check_quotes.py` | 0 处 |
| `check_math_zh.py` | 硬错误 0 |
| `check_terms.py --docs` | 硬错误 0；36 条缺译法为尾节／注记尚未入文 |
| `check_academic.py --strict` | 硬错误 0 |
| `check_pairs.py` | 样章缺口：标题 5 vs 10、公式 491 vs 532、尾节缺失；归 T225 |

## 五、结论

T224 通过：§4–§5 入库，90 块／22 标记／12 display／12 行表守恒；行内 179→178 为 ADR-0049 文字化，已留痕；账本扩至 146 段。下一步 T225（尾节＋111 脚注＋补充注记）。
