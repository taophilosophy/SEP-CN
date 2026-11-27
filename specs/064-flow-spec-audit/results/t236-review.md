# T236 tr-02 样章：logic-dynamic（导论＋§1＋§2.1）

- 日期：2026-11-27（执行跨 2026-11-28）
- 对象：`zh/l/logic-dynamic.md`（H1＋pubinfo＋导论＋§1＋§2＋§2.1）
- 源样章：`en/l/logic-dynamic.md` 导论（L6）至 §2.1（L32–119），16,153 字符
- 账本：`tasks/l/logic-dynamic.ledger.yaml`（44 段）
- 子代理：2 个（用户当轮批准至多 5 个）：A 译导论＋§1，B 译 §2＋§2.1；主代理合并、核验、PE

## 一、入库范围与结构

| 项 | 源 | 译 | 判定 |
| ---- | ---- | ---- | ---- |
| 块数 | 44（导论 1＋H2 2＋H3 1＋段落／列表／图） | 44 | 一致 |
| 行内公式 | 259（导论 3＋§1 40＋§2.1 216） | 259 | 一致 |
| 图片 | 2（model1／model2） | 2 | 路径 `../../assets/logic-dynamic/modelN.png` |
| 列表块 | 7（10／2／1／8／8／3／2 项） | 7 | 一致 |
| display 公式 | 0（§3.1 起） | 0 | — |
| 脚注引用 | 0（样章） | 0 | — |
| 标题 | `## 2. Definitions…`／`### 2.1 Syntax…` | `## 2. 定义与基本结果`／`### 2.1 句法与语义` | 一致 |
| pubinfo | 首次 2007-02-01；修订 2023-02-16 | 同 | 一致 |

- 块 25 的 `\ldquo M, x`／`A\rdquo` 按宏展开为中文引号，公式序列因此拆为 `$M, x$`＋`$A$`；源 6 个数学跨度、译 6 个，无数学内容损失。

## 二、术语与人名

- 登记 22 条：program、formula、atomic formula、transition、iteration、test、converse (program)、intersection (program)、bisimilar、satisfiable、Kripke frame、Hoare calculus、regular program、regular expression、finite automaton、sequence (program)、composition、deterministic、non-deterministic、state (PDL)、world (modal logic)、program construct。
- 撞形处置：`atomic formula` 并入既有 `atomic formulas`；`test` 并入既有 `test (dynamic semantics)`；`state`／`world` 加域括注，与 `state (action ontology)`／《世界》分列（撞形豁免 2026-11-27）。
- 复用：propositional dynamic logic、dynamic logic、atomic program、labeled transition system、Kripke model、valuation、binary relation、non-deterministic choice、converse、bisimulation、satisfiability、validity、modality、axiom schema、completeness、decidability、complexity、partial／total correctness。
- 人名：Engeler／Yanov／Salwicki／Fischer／Ladner／Burstall／Pratt 保留英文原名（登记册无通行汉名）；Hoare 作“托尼·霍尔／霍尔”；van Benthem 作“约翰·范本特姆”。

## 三、译后编辑（PE）

- 两个片段合并后逐块核对：44/44 块、块类型序列一致；259/259 公式多重集一致（唯一差异为块 25 的宏展开）。
- 术语统一：LTS 统一“标记转移系统”；`sat` 在公式与记法中保留，叙述作“满足／可满足”；`iff` 记法行照源保留。
- 风格：中文强调改**加粗**（程序逻辑、一阶、命题动态逻辑、原子、命题、顺序、互模拟、对互模拟安全）；`*α*`／`*β*`／`*π*` 等拉丁变量斜体保留。
- 图片 alt 与图注按原文译；图注保留 `$M = (W,R,V)$` 等数学。

## 四、机检

| 检查 | 结果 |
| ---- | ---- |
| `check_style --docs` | 0 issue |
| `check_quotes --docs` | 0 处违例 |
| `check_math_zh --docs` | 0 个文件有问题、硬错误 0 |
| `check_terms --docs` | 硬错误 0（告警为后续节术语与“可满足”形态变体） |
| `check_academic --docs --strict` | 学术规范无硬错误（在途豁免 1） |
| `check_pairs --gate` | hard 0；out_of_scope 1（样章缺尾节／脚注，符合预期） |

## 五、结论与移交

1. 样章 44 块、259 公式、7 个列表块、2 图与源一一对应。
2. 术语 22 条先登记后用；人名按登记册。
3. 可进入 T237（§2.2–§2.3，123 公式）。
4. 移交：T237 注意公理图式与推演表；T238 的 4 个 display 公式与 15 行规则表；后续“可满足的”形态告警留 rv-01 处置。
