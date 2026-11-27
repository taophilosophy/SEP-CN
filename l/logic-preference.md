# 偏好逻辑 Preference Logic (Fenrong Liu、Leon van der Torre)

> *首次发表于 2025 年 7 月 28 日。*

偏好的概念横跨众多研究领域，因而对它的理解也呈现出多种视角。偏好逻辑专门研究在比较对象、情境、行动等时如何推理偏好，考察其形式性质。本词条综述偏好逻辑迄今的主要发展。第 2 节作历史概述，从哈勒登与冯·赖特的奠基工作开始，他们强调偏好的句法面向。第 3 节介绍雷舍尔与范达伦早期的语义贡献。对可能世界之间偏好关系的考察自然引出模态偏好逻辑，其中偏好提升使跨可能世界集合的比较成为可能。第 4 节介绍冯·赖特对内在偏好与外在偏好的区分，并呈现外在（或基于理由的）偏好的双层结构——这是过去二十年发展的主要焦点；本词条综述该领域的主要框架。第 5 节讨论偏好改变：偏好改变可能出于多种原因，该节考察处理这些动态的不同逻辑进路。第 6 节讨论其他条件不变（*ceteris paribus*）偏好的各种解释，综述其底层逻辑，并考察与这一概念密切相关的条件偏好网络（CP-nets）。第 7 节简要考察偏好逻辑与其他研究领域的联系。第 8 节总结本词条。

## 1. 引言

偏好逻辑本质上是跨学科的：不同领域对偏好的表征与分析各不相同。但有一个明显的共同特征——偏好关涉对情境、对象或行动的比较。此类比较涉及的二元关系有：“*A* 优于 *B*”（$>$）、“*A* 与 *B* 同样好”（$\equiv$），以及“*A* 至少与 *B* 一样好”（$\geq$）。

偏好逻辑始于句法进路，后者关注支配偏好关系的形式原则。与之相对，语义进路旨在为这些关系提供解释，从而能够识别这些原则在何种条件下成立。特别是，可能世界语义学为从语义角度研究偏好逻辑提供了系统框架。本词条也体现从句法进路到语义进路的转变。

行动者作比较时，所得的偏好可能只反映自身的品味，无需任何外在证成；也可能来自可由外部证成的特定理由。纯粹基于行动者自身品味形成的偏好称为 **内在** 偏好。与之相对，可由外在理由解释或证成的偏好称为 **外在** 偏好。冯·赖特（1963）[^wright-1963] 的这一著名区分，是本词条贯穿经典与当代偏好逻辑文献的中心主题。

外在偏好要求模型加入额外要素，以便既表征偏好，又表征证成偏好的理由。此类理由可以包括优先性、对象属性或价值。逻辑学与理性选择理论提出了若干主要框架；在这两个学科中，偏好传统上都被视为固定的。本词条用“双层结构”一词描述这些框架。这种更丰富的建模方式不仅能够推理偏好本身，也能推理其底层理由。有趣的是，道义逻辑中可以看到一种平行发展：基于规范的语义学为道义概念引入额外结构，从而与外在偏好模型背后的观念高度契合。

偏好逻辑的另一关键主题是偏好改变，这与纳入新信息的更广泛趋势相一致。正如知识、信念与意图等态度可能需要更新，偏好也可能随新信息、行动者状态的变化或其他因素而演变。本词条假定读者熟悉信念修正理论（见 SEP 偏好词条）与动态认知逻辑（DEL；见动态认知逻辑词条），并专门聚焦偏好改变的独特面向。

在必须作出决策的 AI 系统中，偏好往往需要被简洁地表征。此语境下的一个核心概念是 **其他条件不变** 偏好，它使如下推理成为可能：“*A* 比 *B* 更可取，其余条件相同”。这一概念已在逻辑学中得到广泛研究，也构成计算机科学文献中 CP-nets（条件偏好网络）等框架的基础。CP-nets 是一种著名的可视化语言，在表达力与计算效率之间取得平衡。因此，本词条对 **其他条件不变** 偏好给予相当多的关注。

## 2. 偏好逻辑的句法进路

哈勒登（1957）[^halldén-1957] 与冯·赖特（1963）[^wright-1963] 等先驱逻辑学家提出了偏好逻辑，聚焦情境之间的比较。这些逻辑用二元联结词 $>$ 扩展命题语言，以表示偏好或“更好”概念。

### 2.1 哈勒登：理论 A 与理论 B

哈勒登（1957）[^halldén-1957] 的《论“更好”的逻辑》常被视为偏好逻辑分析的起点，也是所有其他偏好逻辑的参照点。哈勒登用两个新联结词扩展命题逻辑，他称之为“伦理联结词”：“更好”（$>$）与“同样好”（$\equiv$）。他区分 $\equiv$ 的肯定意义与否定意义，由此得出理论 A 与理论 B。理论 A 基于 **肯定** 意义，其形式表述为：$p\equiv q$ 当且仅当对所有 *r*，$r>p$ 当且仅当 $r>q$，且 $p>r$ 当且仅当 $q>r$。理论 B 基于 **否定** 意义，其中 $p\equiv q$ 仅表示 $\neg(p>q)\land \neg(q>p)$。

由命题变项、普通真值函项联结词以及两个新联结词构成的句子称为“A-公式”。它们遵循通常的省略括号约定，读法依据 $\neg$、$>$、$\equiv$、$\land$、$\lor$、$\rightarrow$、$\leftrightarrow$ 的结合力递减顺序确定。

**理论 A。** 理论 A 见图 1，是命题演算的扩展。公设 $A_1–A_5$ 表明，哈勒登把 $>$ 视为不对称且传递的关系，即偏序；把“$\equiv$”视为自反、对称且传递的关系，即等价关系。哈勒登早在 1939 年就把这些假定追溯到门格尔（参看 Menger 1939）[^menger-1939]。$A_6$ 涉及“更好”与“同等价值”两个概念之间的相互关系。扩展原则 $A_7$ 与 $A_8$ 利用了否定；它们在冯·赖特后来的偏好逻辑中也起核心作用。

**理论 A**

命题演算的所有定理都是理论 A 的公设。

**$R_1$**

若 *φ* 与 $\varphi\rightarrow\psi$ 是 A 的定理，则 *ψ* 是 A 的定理（肯定前件）。

**$R_2$**

设 *φ* 是 A 的定理，*ψ* 除一点外与 *φ* 完全相同：凡 *φ* 中某变项出现之处，*ψ* 中相应出现一个 A-公式。则 *ψ* 是 A 的定理（代换）。

**$R_3$**

设 *φ* 与 $\tau_1\equiv\tau_2$ 是 A 的定理，*ψ* 是 A-公式，且 *ψ* 除一点外与 *ψ* 完全相同：$\tau_1$ 在 *ψ* 中出现于一处或多处，而相应位置在 *φ* 中出现的是 $\tau_2$。则 *ψ* 是 A 的定理（替换）。

$$\begin{align*} \tag*{\(A_1\)} p> q\rightarrow\neg (q > p)&& \textrm{(\(>\)-asymmetry)}\\ \tag*{\(A_2\)} p>q \land q >r\rightarrow p>r&& \textrm{(\(>\)-transitivity)}\\ \tag*{\(A_3\)} p\equiv p&& \textrm{(\(\equiv\)-reflexivity)}\\ \tag*{\(A_4\)} p\equiv q \rightarrow q\equiv p&& \textrm{(\(\equiv\)-symmetry)}\\ \tag*{\(A_5\)} p\equiv q \land q\equiv r \rightarrow p\equiv r&& \textrm{(\(\equiv\)-transitivity)}\\ \tag*{\(A_6\)} p>q\land q\equiv r \rightarrow p>r&& \textrm{(\(>\equiv\)-transitivity)}\\ \tag*{\(A_7\)} p>q\leftrightarrow(p\land \neg q)> (q\land \neg p)&& \textrm{(\(>\)-expansion)}\\ \tag*{\(A_8\)} p\equiv q\leftrightarrow(p\land \neg q)\equiv(q\land \neg p)&& \textrm{(\(\equiv\)-expansion)} \end{align*} $$

*图 1.*

哈勒登证明理论 A 是一致的。他给出理论 A 的若干定理，例如换质位：$p>q \rightarrow\neg q>\neg p$。他还考察了十四条可加入理论 A 的任意公设。例如分配公设 $p>(q\land r)\rightarrow p>q \land p>r$，以及连通性公设 $p>q \lor p\equiv q \lor q>p$。

**理论 B。** 理论 B 的语言是理论 A 语言的一个片段，只包含那些不含 $>$ 与 $\equiv$ 嵌套出现的句子。此外，若 $\varphi>\psi$ 或 $\varphi\equiv\psi$ 出现在 B-公式中，则 *φ* 与 *ψ* 不含合取或析取符号。

理论 B 由公设与规则组成，见图 2。公设 $B_1–B_5$ 与 $A_1–A_5$ 相同，$B6$ 可由理论 A 推出，$B_7$ 表示连通性。

**理论 B**

- 命题演算的所有定理都是 B 的公设。
- 理论 A 的推理规则 $R_1, R_2$ 与 $R_3$ 也适用于理论 B。

$$\begin{align*} \tag*{\(B_6\)} p>q \rightarrow\neg q>\neg p&& \textrm{(contraposition)}\\ \tag*{\(B_7\)} p>q \lor p\equiv q \lor q>p && \textrm{ (connected)} \end{align*}$$

*图 2.*

理论 B 已被证明是一致的。有趣的是，还存在一种判定给定公式是否为 B 的定理的程序。该程序分两步，称为 **单义** 扩展与 **多义** 扩展。

第一阶段运用逻辑原则扩展公式。例如，把 $p\equiv q$ 替换为 $p\equiv q \land q \equiv p$，把 $p> q\land q>r$ 替换为 $p> q\land q>r\land p>r$。考虑哈勒登（1957）[^halldén-1957] 的如下替换序列，以判定

$$p\equiv \neg p\land q\equiv \neg q \rightarrow \neg (p>q)$$

是否为定理：

$$\begin{gather*} p\equiv \neg p\land q\equiv \neg q \land p>q\\ p\equiv \neg p\land \neg p\equiv p\land q\equiv \neg q \land p>q\\ p\equiv \neg p\land \neg p\equiv p\land q\equiv \neg q \land \neg q\equiv q \land p>q\\ p\equiv \neg p\land \neg p\equiv p\land q\equiv \neg q \land \neg q\equiv q \land p>q\land \neg q>\neg p\\ p\equiv \neg p\land \neg p\equiv p\land q\equiv \neg q \land \neg q\equiv q \land p>q\land \neg q>\neg p\land \neg q>p\\ p\equiv \neg p\land \neg p\equiv p\land q\equiv \neg q \land \neg q\equiv q \land p>q\land \neg q>\neg p\land \neg q>p\land q>\neg p\\ p\equiv \neg p\land \neg p\equiv p\land q\equiv \neg q \land \neg q\equiv q \land p>q\land \neg q>\neg p\land \neg q>p\land q>\neg p\land p>\neg q \end{gather*}$$

最后一个公式是矛盾的，因此可以断定 $p\equiv \neg p\land q\equiv \neg q \rightarrow \neg (p>q)$ 是定理。

若第一阶段不能定论，第二阶段把每个公式扩展为一组更复杂的公式。例如，$p>q\land \neg q> \neg p$ 不能用单义扩展进一步展开，但可以扩展为如下公式集：

$$\begin{align} &p>q\land \neg q> \neg p\land p>\neg p, \\ &p>q\land \neg q> \neg p\land p\equiv \neg p, \\ &p>q\land \neg q> \neg p\land \neg p>p, \\ &p>q\land \neg q> \neg p\land \neg p\equiv p, \end{align}$$

这反映了 *p* 与 $\neg p$ 之间一切可能的关系。有兴趣的读者可在哈勒登（1957）[^halldén-1957] 的书中找到更详细的说明。

### 2.2 冯·赖特的偏好逻辑

第二个参照点是冯·赖特（1963）[^wright-1963] 的《偏好逻辑》。在该书中，冯·赖特区分了三组与偏好相关的概念，同时指出它们之间并无截然分界。相关的概念分组是：道义概念（正当、义务、命令、禁令）、价值论概念（善、恶、更好），以及人类学概念（需要、想要、决定、选择）。这些概念在道义逻辑与决策理论中得到探讨，并与偏好逻辑相交；其联系将在第 7 节讨论。冯·赖特还作出若干对偏好逻辑后续发展至关重要的区分：

- 事态之间的偏好 vs. 对手段或方法的偏好；
- 内在偏好（内在更好）vs. 外在偏好（有理由的偏好）；
- 定性偏好 vs. 可测量的价值（如效用）；
- 无风险偏好 vs. 不确定性下的偏好。

更具体地说，冯·赖特采用的形式语言同样是哈勒登 A-公式的片段，只包含那些不含 $>$ 与 $\equiv$ 嵌套出现的句子。然而，与理论 B 的语言不同，若 $\varphi>\psi$ 或 $\varphi\equiv\psi$ 出现在公式中，则 *φ* 与 *ψ* 可以含有合取或析取符号。

与哈勒登的两个理论不同，偏好逻辑不是作为公理化演算提出的，而是作为一种判定给定偏好表达式（P-表达式）是否表示逻辑真命题的技术。

偏好逻辑基于五项关键原则，见图 3。前两项——不对称性与传递性——描述偏好之间的关系，来自哈勒登的系统。其余三项——扩展、析取分配与放大——使任何 P-表达式都能转化为标准形，从而可以应用判定技术。下面用一个例子说明该技术。考虑 P-表达式

$$(p>\neg p)\land (\neg q>q)\rightarrow(p>q).$$

使用扩展，得到

$$(p>\neg p)\land (\neg q>q)\rightarrow(p\land \neg q>\neg p \land q).$$

由于原子偏好中没有析取，分配是空泛的。第三步“放大”给出范式

$$ \begin{align} (p\land q>\neg p\land q) &\land (p\land \neg q>\neg p\land \neg q)\\ &\land (p\land \neg q>p\land q)\\ &\land (\neg p\land \neg q>\neg p\land q) \rightarrow(p\land \neg q>\neg p \land q). \end{align} $$

该公式是重言式，可以这样解释：该公式为假，当且仅当前四个构成项

$$\begin{align} &(p\land q>\neg p\land q), \\ &(p\land \neg q>\neg p\land \neg q), \\ &(p\land \neg q>p\land q) \textrm{ 与} \\ &(\neg p\land \neg q>\neg p\land q) \end{align}$$

全部为真，而 $(p\land \neg q>\neg p \land q)$ 为假。但这与传递性冲突。

考察关于偏好的五项原则时必须小心，因为它们在代换下并不封闭。下文解释这一限制的理由。

**冯·赖特的五项偏好原则**

$$\begin{align} &\tag*{\(V_1\)} (p>q) \rightarrow\neg (q>p)&& \textrm{(\(>\)-asymmetry)}\\[1em] & \tag*{\(V_2\)} (p>q) \land (q >r)\rightarrow q>r&& \textrm{(\(>\)-transitivity)}\\[1em] & \tag*{\(V_3\)} (p>q)\leftrightarrow(p\land \neg q)> (\neg p\land q)&& \textrm{(\(>\)-expansion)}\\ \end{align}$$ $$ \begin{align}\tag*{\(V_4\)}\quad (p&\lor q)>(r \lor s) \leftrightarrow \\ &(p \land \neg r \land \neg s) > (\neg p\land \neg q \land r) \\ &\land\ (p\land \neg r \land \neg s)> (\neg p\land \neg q \land s)\\ &\land\ (q\land \neg r \land \neg s)> (\neg p\land \neg q \land r)\\ &\land\ (q\land \neg r \land \neg s)> (\neg p\land \neg q \land s) \ \text{(disjunctive distribution)} \end{align} $$ $$ \begin{align}\tag*{\(V_5\)} (p&>q) \leftrightarrow \\ &((p\land r)> (q\land r)) \\ &\land\ ((p\land \neg r)>(q\land \neg r)) \qquad {\textrm{(amplification)}} \end{align} $$

*图 3.*

冯·赖特的另一贡献是尝试用“变化”来理解偏好的意义。他的分析揭示了一种独特的偏好观。人们何时可以说一个事态比另一个事态更可取？为回答这一问题，考虑两个一般偏好状态 *p* 与 *q*。共有四种可能情形：$p \land q$、$p \land \neg q$、$\neg p \land q$ 与 $\neg p \land \neg q$。任何世界都必然落入这四种可能之一。这不仅解释了哈勒登已经采纳的前三项原则，也解释了析取分配原则，即上表中的 $V_4$。

在 $p\land q$ 情形下，“行动者偏好 *p* 胜过 *q*”意味着：行动者宁可失去 *q*（并保留 *p*），也不愿失去 *p*（并保留 *q*）。

在 $p\land \neg q$ 情形下，“行动者偏好 *p* 胜过 *q*”意味着：行动者宁可维持当前状态，也不愿看到它变为 $\neg p\land q$。

在 $\neg p\land q$ 情形下，“行动者偏好 *p* 胜过 *q*”意味着：行动者宁可看到世界从 $\neg p$ 变为 *p*、从 *q* 变为 $\neg q$，也不愿看到毫无变化。

在 $\neg p \land \neg q$ 情形下，“行动者偏好 *p* 胜过 *q*”意味着：行动者宁可得到不带 *q* 的 *p*，也不愿得到不带 *p* 的 *q*。

原则 $V_5$ 是偏好所谓的 **整体论** 性质。设 *φ* 是公式，$PL(\varphi)$ 是出现在 *φ* 中的命题字母集合，冯·赖特称之为论域。设 $r \not\in PL(\varphi>\psi)$，则把每个公式 $\varphi> \psi$ 替换为合取

$$((\varphi\land r)> (\psi\land r)) \land ((\varphi\land \neg r)>(\psi\land \neg r)).$$

这一原则也称为 **放大**，对 $PL(\varphi > \psi)$ 相对于命题字母集合的补集中的每个 *r* 施用。放大确保论域中与偏好子公式评价没有直接关系的每个 *r* 都保持不变。

$V_1$、$V_2$、$V_3$ 与 $V_4$ 出现在许多公理化偏好逻辑中，$V_5$ 则不然。原因是 $V_5$ 不能与代换结合。

自哈勒登以来，文献中探讨了大量原则。全面的综述可参见 S. O. 汉松（2001）[^hansson-2001] 的相关章节，其中包括以下例子：

$$\begin{align*} \tag{H1} \textrm{不存在序列 } p_1,\ldots, p_n \\ \textrm{使得 } p_1>\ldots>p_n>p_1 && \textrm{(\(>\)-acyclic)}\\ \tag{H2} p\equiv q \land q >r \rightarrow p>r &&\textrm{(\(\equiv\)\(>\)-trans)}\\ \tag{H3} p> q \land q >r \rightarrow p>s \lor s>r && \textrm{(semi-trans)}\\ \tag{H4} p>q \land r >s \rightarrow p>s \lor r>q && \textrm{(interval order)} \end{align*} $$

*图 4：* 更多偏好原则

哈勒登与冯·赖特都通过句法或算法进路强调偏好原则的普遍性。后来的研究者常用例子支持或挑战这些原则，许多偏好性质至今仍无定论。

## 脚注

[^halldén-1957]: Halldén, Sören, 1957, *On the Logic of “Better”* (Library of Theoria 2), Lund: C.W.K. Gleerup.

[^hansson-2001]: –––, 2001, “Preference Logic”, in *Handbook of Philosophical Logic*, Dov M. Gabbay and Franz Guenthner (eds), second edition, Dordrecht: Kluwer, 319–393. doi:10.1007/978-94-017-0456-4_4

[^menger-1939]: Menger, Karl, 1939, “A Logic of the Doubtful. On Optative and Imperative Logic”, *Reports of a Mathematical Colloquium*, Notre Dame, IN, series 2, 1: 53–64.

[^wright-1963]: von Wright, Georg Henrik, 1963, *The Logic of Preference*, Edinburgh: Edinburgh University Press.
