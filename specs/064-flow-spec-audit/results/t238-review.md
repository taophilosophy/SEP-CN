# T238 tr-02 批 2：logic-dynamic（§3）

- 日期：2026-11-28
- 对象：`zh/l/logic-dynamic.md` 追加 §3
- 源范围：`en/l/logic-dynamic.md` L243–348，12,761 字符
- 账本：`tasks/l/logic-dynamic.ledger.yaml` 100→141 段
- 子代理：1 个（累计 4/5）

## 一、结构与公式

| 项 | 源 | 译 | 判定 |
| ---- | ---- | ---- | ---- |
| 块数 | 41 | 41 | 一致 |
| 行内公式 | 106 | 106 | 逐块多重集一致（块 30 仅定界符空白规范化） |
| display 公式 | 4（8 个 `$$`） | 4 | 一致；第 263 行两个 display 保持同块同线 |
| 表格块 | 2（7 行／14 行，各含分隔行与末行 `—`） | 2 | 一致 |
| 标题 | `## 3.`／`### 3.1`–`3.3` | `## 3. 结构化程序设计与程序正确性`／`### 3.1 霍尔演算`／`### 3.2 霍尔演算与 PDL`／`### 3.3 完全正确性` | 一致 |
| 列表 | 5 个程序构造定义 | 5 | 一致 |

- 块 30 源 `$V(\Delta\alpha) = \{x: $` 的行内定界符内侧空白按公式体例去除（`\{x:$`），入勘误第二十节；数学内容不变。

## 二、术语与人名

- 复用／新用：structured programming 结构化程序设计、correctness 正确性、flowchart 流程图、Hoare logic 霍尔逻辑、Floyd-Hoare logic 弗洛伊德—霍尔逻辑、Hoare calculus 霍尔演算、Hoare triple 霍尔三元组、precondition 前提条件、post-condition 后条件、partial／total correctness 部分／完全正确性、termination 终止、rule of composition **合成规则**（按登记册 L7131）、rule of iteration 迭代规则、rule of consequence 后承规则、axiom schema 公理图式、monotony 单调性、propositional tautology 命题重言式、deterministic 确定的、non-termination 不终止、diverge 发散、infinite looping 无限循环、expressiveness 表达力、RPDL 带重复的 PDL（RPDL）、combinatory PDL 组合式 PDL。
- 人名：Floyd、Apt、Streett、Sakalauskaite、Valiev、Gargov、Passy、Yanov、Engeler、Pratt 保留英文原名；Hoare 首现已于导论作“托尼·霍尔”，§3 起作“霍尔”。

## 三、机检

| 检查 | 结果 |
| ---- | ---- |
| `check_style` | 0 issue |
| `check_quotes` | 0 处违例 |
| `check_math_zh` | 0 个文件有问题、硬错误 0（修正 C2 1 处） |
| `check_terms` | 硬错误 0（50 条告警为后续节术语与形态变体） |
| `check_academic --strict` | 无硬错误（在途豁免 1） |
| `check_pairs --gate` | hard 0；out_of_scope 1（中途阶段） |

## 四、结论

§3 入库：41 块、106 公式、4 display、2 张推演表与源逐项一致。可进入 T239（§4，116 公式）。
