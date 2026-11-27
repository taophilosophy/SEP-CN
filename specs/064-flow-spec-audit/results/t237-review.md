# T237 tr-02 批 1：logic-dynamic（§2.2–§2.3）

- 日期：2026-11-28
- 对象：`zh/l/logic-dynamic.md` 追加 §2.2–§2.3
- 源范围：`en/l/logic-dynamic.md` L121–241，10,518 字符
- 账本：`tasks/l/logic-dynamic.ledger.yaml` 44→100 段
- 子代理：1 个（累计 3/5）

## 一、结构与公式

| 项 | 源 | 译 | 判定 |
| ---- | ---- | ---- | ---- |
| 块数 | 56 | 56 | 一致 |
| 行内公式 | 123 | 123 | 逐块多重集一致 |
| 表格块 | 2（各 6 行：表头＋分隔＋4 步） | 2 | 一致 |
| 标题 | `### 2.2`／`### 2.3` | `### 2.2 公理化与完全性`／`### 2.3 可判定性与复杂度` | 一致 |
| 标签块 | (K)(N)(A1)–(A5)(I)(I′)(L-SAT)(PDL-SAT) | 同 | 一致 |
| display 公式 | 0（§3.1 起） | 0 | — |

- 两张推演表“序号／公式／理由”三列不变；理由列译“前提／由 1 用（N）／公理图式（A5）／由 3 用命题推理／由 2 与 4 用肯定前件式”等。
- 独立记法行 `$\vdash A$ iff $\models A$` 与 `$\vdash' A$ iff $\models A$` 照源保留 `iff`；正文 `iff` 译“当且仅当”。

## 二、术语与人名

- 复用：proof theory 证明论、validity 有效性、axiom 公理、rule of inference 推理规则、deducibility 可推演性、tautology 重言式、normal modal logic 正规模态逻辑、distribution axiom schema 分配公理图式、necessitation 必然化、distributivity 分配性、monotony 单调性、loop invariance 循环不变性、induction axiom schema 归纳公理图式、derived rule 派生规则、soundness 可靠性、completeness 完全性、infinitary rule of inference 无穷推理规则、finite model property 有穷模型性质、small model property 小模型性质、complexity theory 复杂性理论、decision problem 判定问题、satisfiability 可满足性、sub-procedure 子过程、semantic tableaux 语义表列法、alternating Turing machine 交替图灵机。
- 人名：Segerberg、Kozen、Nishimura、Vakarelov、Goldblatt、De Giacomo、Massacci 保留英文原名；Parikh 首现“罗希特·帕里克”，其后“帕里克”；Pratt、Fischer、Ladner 沿用样章。

## 三、机检

| 检查 | 结果 |
| ---- | ---- |
| `check_style` | 0 issue |
| `check_quotes` | 0 处违例 |
| `check_math_zh` | 0 个文件有问题、硬错误 0 |
| `check_terms` | 硬错误 0（55 条告警为后续节术语与形态变体） |
| `check_academic --strict` | 无硬错误（在途豁免 1） |
| `check_pairs --gate` | hard 0；out_of_scope 1（样章／中途阶段） |

## 四、结论

§2.2–§2.3 入库：56 块、123 公式、2 张推演表与源逐项一致。可进入 T238（§3，106 公式＋4 display＋4 表块）。
