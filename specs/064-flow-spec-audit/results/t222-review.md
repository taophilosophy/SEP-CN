# T222 证据：axiom-choice tr-02 样章（§1）

- 日期：2026-11-27
- 任务：T222（T156 拆站第 2 项）；范围 `en/a/axiom-choice.md` 第 8–77 行（§1）
- 条目：`a/axiom-choice`；版本钉 `Dec 10, 2021／Winter 2021／4a723bef…e9c8f`
- 产出：`zh/a/axiom-choice.md`（H1＋pubinfo＋§1＋脚注）；`tasks/a/axiom-choice.ledger.yaml`（30 段）

## 一、结构守恒

| 项 | en §1 | zh 样章 | 结论 |
| ---- | ---- | ---- | ---- |
| 非空块 | 30 | 30 | 类型序列一致（`HPQ`＋27 段） |
| 标题 | 1 | 1 | `## 1. 选择公理的起源与年表` |
| 引块 | 1 | 1 | Zermelo 引块 |
| display | 2 | 2 | 选择函数对照式 |
| 表格 | 1 块 11 行 | 1 块 11 行 | 两列逐行对应 |
| 行内公式 | 68 | 68 | 全部 `$…$` 保留 |
| 脚注标记 | 22 | 22 | 等序 |
| 脚注定义 | 22 直接引用＋1 嵌套 | 23 | 逐条与 en 定义一致 |

源表首行后接分隔行的“畸形”表头按 en 原样保留，未擅改为规范表头（结构保真优先；全量 T223–T225 仍按此口径）。

## 二、数学保真

- 68 行内＋2 display 全部保留；`check_math_zh` 硬错误 0。
- SEP 宏已按 `html/axiom-choice/local.js` 展开：`\sH`→`\mathcal{H}`、`\sA`→`\mathcal{A}`、`\inn`→`\in`、`\amp`→`\mathbin{\&}`、`\bfrac{1}{2}`→`{^{1}\unicode{x2044}_{2}}` 等；扫描无 `\sH`／`\inn`／`\amp`／`\bfrac` 残留。
- 源文 “the collection of which he denotes by M” 的 M 在 HTML 中为正文而非公式，译文照录为正文 M。
- 术语候选：`collection` 统一“族”、`indexed collection` 统一“索引集族”；避免“汇集／索引汇”混用。

## 三、术语登记（本批新增 14 条）

transversal＝横截集（亦作选择集）、well-ordering＝良序、cardinal number＝基数、covering＝覆盖、indexed collection＝索引集族、permutation method＝置换法、multiplicative axiom＝乘法公理、paradoxical decomposition＝悖论分解、epsilon axiom＝ε 公理、non-constructive＝非构造性的、French Empiricists＝法国经验论者、surjective＝满射的、unordered pair＝无序对、variable element＝可变元素。

`right inverse` 本已登记（右逆，2026-11-25），本批误加重行已删除，避免自洽违例。

## 四、机检

| 检查器 | 结果 |
| ---- | ---- |
| `check_style.py` | 0 issue |
| `check_quotes.py` | 0 处 |
| `check_math_zh.py` | 硬错误 0 |
| `check_terms.py --docs` | 硬错误 0；60 条“缺登记译法”为全量条目尚未入样章，属样章范围 |
| `check_academic.py --strict` | 硬错误 0 |
| `check_pairs.py` | 3 条样章缺口：标题 2 vs 10、公式 87 vs 532、尾节缺失；归 T223–T225 |

## 五、结论

T222 满足验收：§1 入库、30 块与 68 行内／2 display／11 行表守恒、脚注 22 标记闭合、术语先登记后用、定点机检无硬错误。下一步 T223（§2–§3）。
