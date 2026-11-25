# 收割批 15：逻辑与论证方法族（2026-11-25）

按「逻辑基础／论证谬误／模型论」三块抽查 100 个常见名，缺 24；语料或池频次支持者登记 19 条、并入 4 条。

## 一、登记 19 条

| 英文 | 主形 | 依据要点 |
| ---- | ---- | ---- |
| axiom | 公理 | 语料 986 次 |
| proof | 证明（逻辑与数学义；与 burhān 证明按原文分列） | 语料高频 |
| lemma | 引理 | 语料 39 次 |
| paradox | 悖论 | 语料 455 次，与 antinomy 二律背反分列 |
| quantifier | 量词 | 语料 272 次 |
| biconditional | 双条件 | ↔ |
| logical connective | 逻辑联结词 | 语料 10 次 |
| truth table | 真值表 | |
| compactness theorem | 紧致性定理 | 语料 20 次 |
| hypothetical syllogism | 假言三段论 | 语料 24 次 |
| circular reasoning | 循环论证 | 语料 21 次 |
| begging the question | 丐题（亦作“预设问题”） | 与循环论证分列，勿混 |
| straw man | 稻草人谬误（亦作“稻草人”） | |
| false dilemma | 假两难（亦作“虚假两难”） | |
| burden of proof | 举证责任 | 与 presumption 推定对举 |
| necessary and sufficient conditions | 充分必要条件（亦作“充要条件”） | |
| lambda calculus | λ 演算 | 丘奇；池 freq 54 |
| combinatory logic | 组合子逻辑 | 池 freq 48 |
| axiomatic set theory | 公理集合论 | 与 naive set theory 朴素集合论对举 |

## 二、并入 4 条

* `material implication / material conditional`（同概念两形，原只有前者）
* `propositional logic / propositional calculus`（同概念，原只有前者）
* `inference rule / rule of inference`（同概念，原只有前者）
* `Löwenheim-Skolem theorem / Löwenheim–Skolem theorem`（连字符与一字线连接号两形；另有一行 `Löwenheim–Skolem–Tarski theorem` 是三名定理，保留）
* `Gödel encoding / Gödel numbering`（同概念；原文列补 `Gödel-Encoding`，避免非英语键缺原文告警）

## 三、教训：本批初版造了一行重复

`Löwenheim–Skolem theorem` 初版当成缺口新登，落册后告警暴露既有 `Löwenheim-Skolem theorem`（连字符）行——**强归一（去连字符）在两形之间本应判为同键，但本批建清单时跳过了这一步**（批 9 之后我已把强归一写进方法，却在这一批直接按「键精确缺」列表动手）。处置：删除新行、旧行加异形并入、保留一字线形作别名。**今后任何批次开工前先跑一次强归一判缺，不得只信 term_flow 的键精确查重。**

## 四、门禁

* 清单 `tasks/manifests/2026-11-25-058-batch66-terms.json`（19 行）；池 published=12
* 数据行 8,829→8,848；`registry_azsort` 守恒；`check_terms` 硬错误 0（自洽 0）
* 缺原文告警 148（初版一度 150，因 Gödel／Löwenheim 两非 ASCII 键未填原文，已修回）

## 五、未登

* `corollary 推论`（语料 457 次，但绝大多数是一般义“推论”，非定理序列义，登记会污染）／`syntactic consequence`（0 次）／`Kripke semantics`（0 次）／`paradox of material implication`（4 次，先留池）。
* `induction 归纳`／`deduction 演绎`／`definition 定义` 早已在册。
