# 完备性证明：联网查证记录

**日期**：2026-11-18｜**性质**：查证（联网，逐条附源）｜**被查对象**：`specs/043-pipeline-axioms/spec.md` §六「6.4 要求登记册 R 自身的完备性（不可自证）」
**结论**：原表述**错误**，已修正。错在用 Gödel 不完备定理类比工程语境的要求集完备性。正确框架是 **相对完备（relative completeness）**——与 Cook 1978 对 Hoare 逻辑的处理同构。

---

## 一、被查的原表述

> 「任何公理系统都不能证明自己的要求集完整——这是系统内的盲点。」
> 「系统不能证明自己的要求集完整」被归入「不可证」四类之一，并与 Gödel 的语境并置。

两处需要分别核证：
1. Gödel 定理到底说了什么，能否这样用；
2. 「要求集完整」在标准与文献中是什么性质，可不可形式证明。

---

## 二、Gödel：准确表述与常见误用

**源**：Raatikainen, Panu. "Gödel's Incompleteness Theorems." *The Stanford Encyclopedia of Philosophy*, Winter 2016 Edition, Edward N. Zalta (ed.).
`https://plato.stanford.edu/archives/win2016/entries/goedel-incompleteness/`（查证日 2026-11-18）

### 2.1 两条定理的原文

> **First incompleteness theorem**: Any consistent formal system F within which a certain amount of elementary arithmetic can be carried out is incomplete; i.e., there are statements of the language of F which can neither be proved nor disproved in F.

> **Second incompleteness theorem**: such a formal system cannot prove that the system itself is consistent (assuming it is indeed consistent).

### 2.2 SEP 明确点出的两处误用

> A common misunderstanding is to interpret Gödel's first theorem as showing that there are truths that cannot be proved. This is, however, incorrect, for the incompleteness theorem **does not deal with provability in any absolute sense**, but only concerns derivability in some particular formal system or another.

> There have been attempts to apply the results also in other areas of philosophy such as the philosophy of mind, but **these attempted applications are more controversial**.

### 2.3 对原表述的判定

| 检查项 | 事实 | 原表述是否成立 |
|---|---|---|
| 第二定理讲的是「不能证明**一致性**」 | 是 | **否**——原表述写成「不能证明完备性」 |
| 第一定理讲「存在不可判定命题」 | 是 | 部分相关，但结论是「系统不完全」，不是「不能自证完备」 |
| 适用前提：能表达一定量算术 ＋ 可递归公理化 | 是 | **不满足**——`pipeline-17` 是有限数据结构，不含算术 |
| SEP 对跨领域应用的评价 | "more controversial" | **否**——原表述属此类 |

**判定：原表述不成立。** 这是把逻辑定理当作通用修辞使用，而 SEP 对该用法有明确保留。

---

## 三、要求集完备性：标准的定义与文献的定性

### 3.1 ISO/IEC/IEEE 29148:2018 把「完备」定义为语法判据

**源**：ISO/IEC/IEEE 29148:2018, Clause 5.2.6（Characteristics of a set of requirements）。标准正文付费，条款内容经两个独立二手源交叉：
* TU München 学位论文引 ISO11b p.11：complete 意为 "the set of requirements **needs no further amplification** because it contains everything pertinent to the definition of the system or system element being specified"，并要求 "the set does not contain any TBx's, such as to be defined (TBD)"。`http://mediatum.ub.tum.de/doc/1346242/445192.pdf`
* 条款汇编站：complete = "stands alone and contains **no To Be Defined, To Be Specified or To Be Resolved clauses**"。`https://iso-29148-revision-checker.theartofservice.com/clauses/5-2-6`

同一标准把「能否满足需要」列为**另一个特性**：

> It can be **validated** when satisfying the set would actually meet the need within cost, schedule, technical, legal and regulatory limits.

Clause 5.2.5 对单条要求给九特性：necessary, appropriate, unambiguous, complete, singular, feasible, verifiable, correct, conforming。

**关键结论**：标准的 `complete` 是**无占位符、无需外部补充**——**可机检**；`validatable`（能否满足真实需要）是另一维度。原表述把两者混为一谈。

### 3.2 Zave & Jackson：要求集的完整性属「非形式验证」

**源**：Zave, P. & Jackson, M. "Four Dark Corners of Requirements Engineering." *Annals of Software Engineering* 4 (1997)。原文引文经两个独立转载核对：`https://arxiv.org/html/1507.06260`、`https://arxiv.org/pdf/2104.14110`

ZJ 框架给出的「需求工程完成」五条件中，只有两条是形式的：

> 4. A proof shows that K, S ⊢ R.
> 5. There is a proof that S and K are consistent.

而第一条关于 R 本身的完整性，明确标注为**非形式**：

> There is a set R of requirements. Each member of R has been validated (**checked informally**) as acceptable to the customer, and **R as a whole has been validated as expressing all the customer's desires** with respect to the software development project.

**关键结论**：在这个被广泛接受的框架里，「R 表达客户全部愿望」从始至今就是 `checked informally`。不是「暂时没证出来」，而是**归入非形式验证**。

### 3.3 Glinz：开放环境下不可能穷举

**源**：Glinz, M. "How much Requirements Engineering do we need?" University of Zurich open repository, 2016. `https://www.zora.uzh.ch/135589/1/Glinz_2016.pdf`

> for any real world software (the type E in Lehman's classification), we are confronted with the problem of mapping phenomena of the real world on constructs of our specification language. This is a modeling process which, **by its very nature, is not formalizable**.

> is it possible there to describe all inputs, including everything that could ever happen even in the most improbable case? **The answer is no.** As our perception of the world is limited, we will never be able to describe all inputs in terms of everything that could ever happen in the real world.

**关键结论**：不可穷尽的理由是**建模过程本身不可形式化**（Lehman type E），不是「系统内的自指盲点」。

### 3.4 标准自身的版本状态（引用纪律）

**源**：ISO 官方页面 `https://www.iso.org/fr/standard/72089.html`、`https://www.iso.org/standard/94091.html`（查证日 2026-11-18）

| 项 | 记录 |
|---|---|
| 现行版 | ISO/IEC/IEEE 29148:2018，Edition 2，2018-11-28 发布 |
| 系统审查 | 90.20 起 2023-10-15，90.60 结束 2024-03-04，90.93 确认 2024-05-10 |
| **进入修订** | **90.92，2026-02-16** |
| 下一代 | ISO/IEC/IEEE DIS 29148 Edition 3，101 页 |
| DIS 阶段 | 40.00 注册 2026-07-13；40.20 投票启动 2026-09-14（12 周）；40.60 投票结束 **2026-12-07**（依 12 周推算，ISO 未记录该日期） |
| 可引用性 | 2018 版现行有效；DIS 未发布，**不得作为适用标准引用** |

引用 29148 时必须同时标注「2018 现行、2026-02-16 进入修订」，否则读者会以为引用的是最新版。

---

## 四、Hoare 逻辑：完备性的正确范式是「相对完备」

**源**：Cook, S. A. "Soundness and Completeness of an Axiom System for Program Verification." *SIAM Journal on Computing* 7(1), 1978, pp. 70–90。结论经两个独立二手源核对：ScienceDirect 论文摘要 `https://www.sciencedirect.com/science/article/pii/S0020025501001645`、知识库条目 `https://lingenic.com/en/Knowledge_Base/Logic/Formal_Logical_Systems/Applications/Verification/Hoare_Logic`

### 4.1 为什么不能绝对完备

> It is not complete in the absolute sense and cannot be, since `{P} C {false}` is valid exactly when C diverges from every P-state, and **non-termination is not recursively enumerable**, so the valid triples are not r.e. and no effective proof system enumerates them.

### 4.2 正确表述

> Cook (1978) supplied the correct statement: Hoare logic is **complete relative to an oracle for validity in the assertion language**, provided that language is **expressive** — that is, provided the strongest postcondition of each command is definable in it.

> The proof system itself contributes no incompleteness; **all missing power, if any, lives in the arithmetic**.

### 4.3 边界条件（诚实标注）

* Wand (1978)：存在不表达的模型，此时系统**真不完备**；
* Clarke (1979)：对含递归过程＋过程参数＋静态作用域＋全局变量的语言，**不存在**既可靠又相对完备的 Hoare 系统。

---

## 五、结论：原表述改为相对完备

### 5.1 三种「完备性」不可混用

| 类型 | 含义 | 是否可证 | 本项目的对应 |
|---|---|---|---|
| **语法完备** | 无占位符、无悬空引用、无需外部补充 | 可机检 | D1–D6（35 项中 D 组 6 项）**已证** |
| **相对完备** | 相对于外部输入 R，系统内无遗漏 | 可证（条件性） | 本项目**成立**：给定 R，35/35 |
| **经验完备** | R 是否穷尽所有应有关切 | **不可形式证**，属非形式验证 | ZJ 的 `checked informally`；Glinz 的 type E 不可穷举 |

### 5.2 修正后的表述

> 本验证证明的是**相对于要求登记册 R 的完备性**（complete relative to R）：给定 R 的 18 条，pipeline-17 无遗漏、无空挂、无冗余。
>
> 这不保证 R 本身的经验完备性——即「R 是否穷尽了所有应有关切」。该问题**不属于形式系统的能力范围**，理由是双重的：
> ① Zave & Jackson 框架把「R 表达客户全部愿望」归入 `checked informally`，形式部分只覆盖 `K,S ⊢ R` 与 `K,S ⊬ ⊥`；
> ② Glinz 指出面向真实世界（Lehman type E）的需求建模过程 `by its very nature is not formalizable`，不存在「描述所有可能输入」的终点。
>
> 因此本体系的完备性结构与 Cook 的 Hoare 逻辑同构：**验证器本身不贡献遗漏，缺失的力量全部位于外部输入 R**。系统性保障只能是登记纪律——新增 ADR 时同步登记新要求。

### 5.3 与原表述的差异

| 项 | 原表述 | 修正后 |
|---|---|---|
| 依据 | Gödel 不完备定理（隐含） | Zave & Jackson ＋ Glinz ＋ Cook 相对完备 |
| 定性 | 「系统不能自证」 | 「R 是外部输入，其有效性属非形式验证」 |
| 适用范围 | 暗示一切公理系统 | 仅限「要求集」这一类外部输入 |
| 可操作性 | 无（只是承认盲区） | 有（ADR 模板增加要求登记项） |
| 准确性风险 | 高（SEP 明示此类应用 controversial） | 低（三源交叉，均为该领域标准引用） |

---

## 六、诚实标注的三处不确定

1. **29148 条款原文未见**。标准付费，Clause 5.2.5／5.2.6 的具体措辞经两个二手源交叉，二者一致但非官方原文。若要写入正式条文，需购买标准核对原句。
2. **ZJ 原文未见**。1997 年 *Annals of Software Engineering* 原文经两篇 arXiv 论文转引，两处引文逐字一致，可信度高，但仍属转引。
3. **DIS 29148 Ed.3 的 40.60 日期为推算**。ISO 只记录 40.20 启动日与 12 周投票期，2026-12-07 是依此推算，非 ISO 记录值。

---

## 七、源清单

| # | 源 | 类型 | 用途 | 查证日 |
|---|---|---|---|---|
| 1 | SEP, "Gödel's Incompleteness Theorems", Winter 2016 ed., Raatikainen | 权威百科 | 两条定理原文与误用警示 | 2026-11-18 |
| 2 | ISO/IEC/IEEE 29148:2018, Clause 5.2.5／5.2.6（经 TUM 论文与条款汇编站交叉） | 标准（二手） | complete 与 validatable 的区分 | 2026-11-18 |
| 3 | ISO 官方页 72089／94091 | 标准状态 | 2018 现行、2026-02-16 进入修订、DIS Ed.3 阶段 | 2026-11-18 |
| 4 | Zave & Jackson, "Four Dark Corners of RE", 1997（经 arXiv 1507.06260／2104.14110 交叉） | 经典论文（转引） | R 的完整性属 checked informally | 2026-11-18 |
| 5 | Glinz, "How much RE do we need?", UZH 2016 | 学术论文 | type E 建模不可形式化 | 2026-11-18 |
| 6 | Cook, SIAM J. Comput. 7(1) 1978（经 ScienceDirect 摘要与知识库交叉） | 经典论文（转引） | 相对完备性；绝对不完备的理由 | 2026-11-18 |
| 7 | Clarke 1979（经同上二手源） | 经典论文（转引） | 相对完备亦可能失败的语言特征 | 2026-11-18 |
