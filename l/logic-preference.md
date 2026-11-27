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

## 3. 偏好逻辑的语义进路

本节从语义角度讨论偏好，介绍雷舍尔（1967）[^rescher-1967] 与范达伦（1974）早期的方案，以及可能世界语义学——后者一直是该领域后续研究的核心。

### 3.1 雷舍尔-范达伦语义

雷舍尔（1966, 1967）[^rescher-1966][^rescher-1967] 提出了偏好逻辑的第一个语义学，其中模型是公式上的实值函数。范达伦（1974）将其推广到偏序，并证明雷舍尔的偏好逻辑是其特例。这些语义结构直接反映语言所表达的偏好。这里介绍范达伦的语义与公理化。

语言与冯·赖特的语言相同，即用二元联结词 $>$ 扩展命题逻辑，但这里没有嵌套偏好陈述。无差异按偏好定义：$\varphi\equiv \psi = \neg (\varphi>\psi)\land \neg (\psi>\varphi)$。

为了给 $\varphi>\psi$ 形式的公式赋值，范达伦规定命题之间的序关系。他同时考虑真值赋值 *v* 与善性度量 *m*。在此框架中，*m* 把命题集合映射到偏序集 *A*，*v* 把命题符号（原子）映射到 $\{0,1\}$，并按如下归纳定义扩展到所有公式：

1. $v(\neg \varphi) = 1-v(\varphi)$
2. $v(\varphi\lor\psi) = \textrm{max}\{v(\varphi),v(\psi)\}$
3. 若在 *A* 上 $m(\varphi) \lt m(\psi)$，则 $v(\varphi P\psi) = 1$；否则为 0

对公式集 *Γ*，满足关系定义如下：

$$\begin{align*} A, m, v \models p &\quad \textrm{ 当且仅当}\quad v(p) = 1 \textrm{ 对原子 } p\\ A, m \models \varphi &\quad \textrm{ 当且仅当}\quad A, m, v \models \varphi \textrm{ 对所有 } v\\ A, v \models \varphi &\quad \textrm{ 当且仅当}\quad A, m, v \models \varphi \textrm{ 对所有 } m\\ A \models \varphi &\quad \textrm{ 当且仅当}\quad A, m, v\models \varphi \textrm{ 对所有 } m \textrm{ 与 } v\\ \models \varphi &\quad \textrm{ 当且仅当}\quad A \models \varphi \textrm{ 对所有 } A (\varphi \textrm{ 为真})\\ A, m, v \models \Gamma &\quad \textrm{ 当且仅当}\quad A, m, v \models \Gamma \textrm{ 对所有 } \varphi\in\Gamma\\ \Gamma\models \varphi &\quad \textrm{ 当且仅当}\quad A, m,v\models\Gamma \Rightarrow A, m,v\models \varphi\\ \end{align*}$$

范达伦称上述语义为 **非理性语义**，主要因为逻辑等价的命题可能导致不同偏好。因此，他给度量 *m* 或偏序集 *A* 附加三个条件，以获得更受限的语义：

1. 若 $\varphi\equiv \psi$ 是重言式，则 $m (\varphi) = m(\psi)$。
2. *A* 是线性序。
3. *A* 是实数集，且 $m(\neg \varphi)=-m(\varphi)$。

范达伦提出若干理论——**PREFIR**、**PREF**、**PREFL**、**PREFR**——见图 5。他证明 **PREFIR** 对非理性语义完全，**PREF** 对满足条件 (i) 的语义完全，**PREFL** 对线性语义完全，**PREFR** 对雷舍尔语义完全。

范达伦的偏好理论 **PREFIR**、**PREF**、**PREFL** 与 **PREFR**

- 经典命题逻辑的所有重言式都是公理。
- 肯定前件与替换（见哈勒登的理论 A）。

$$\begin{align*} \tag*{P1} \neg (\varphi> \varphi) \\ \tag*{P2} \varphi>\psi \land \psi >\chi \rightarrow \varphi> \chi\\ \tag*{P3} \varphi>\psi \land \psi \equiv\chi \rightarrow \varphi> \chi\\ \tag*{P4} \varphi>\psi \rightarrow \neg \psi > \neg \varphi\\ \end{align*}$$

我们将考察若干公理系统；它们都以重言式为公理、以肯定前件为推理规则。除第一个系统外，其余系统都以替换为推理规则。

**PREFIR**

公理 P1、P2（只施用肯定前件规则）

**PREF**

公理 P1、P2

**PREFL**

公理 P1、P2、P3

**PREFR**

公理 P1、P2、P3、P4

*图 5.*

此外，范达伦证明所有系统都具有有限模型性质并且可判定。他还把语言扩展为带有“好”“坏”“中性”一元算子，并考察嵌套偏好陈述。奇泽姆与索萨（1966）等其他作者则考察此类偏好逻辑的一阶扩展。

### 3.2 可能世界上的偏好

在模态逻辑迅速发展的时代（见模态逻辑词条），二元偏好关系被自然地纳入可能世界语义学，以便在各种语境中比较不同情境或世界。本小节与下一小节综述模态偏好逻辑，并讨论为比较可能世界集合而提升偏好的各种方法。

自 20 世纪 60 年代末起，二元模态逻辑被发展出来，以建模条件义务（B. 汉松 1969）[^hansson-1969]，以及相关的条件句形式（Lewis 1973; Makinson 1993）[^lewis-1973][^makinson-1993]。在这些框架中，可能世界语义学背后的偏好结构得到运用，尤其是在道义逻辑与条件句研究中。

自 20 世纪 80 年代末起，一种被广泛采用的一元模态进路出现，它在非单调逻辑与信念修正（Boutilier 1990; Lamarre 1991）[^boutilier-1990][^lamarre-1991] 以及道义逻辑（Tan & Van der Torre 1996）[^tan-1996] 中探讨偏好。尽管这些工作的动机各不相同，一元模态进路在某些情形下为偏好逻辑的公理化提供了更直接的路径。

偏好逻辑研究常与理解动态环境中的行动者选择相联系。一个核心关注点是行动者如何排列可能世界以表达偏好。这使决策与规范推理的模型更为细致。受条件逻辑与信念修正早期发展的启发，把偏好序整合进模态逻辑，通过引入可能世界上的偏好结构扩展了逻辑系统的表达力。

一个模态偏好模型 $\mathcal{M}$ 是三元组 $(W, \succeq, V)$，其中 *W* 是可能世界集合，$\succeq$ 是这些世界上的二元偏好关系，*V* 是为这些世界中的命题字母赋真值的赋值。视语境而定，我们假定偏好关系 $\succeq$ 具有某些性质。例如，它可以是（全）预序、偏序等。若选择（全）预序，则严格偏好关系“$w\succ v$”可定义为“$w\succeq v\land v \nsucceq w$”，无差异关系“$w\approx v$”可定义为“$w\succeq v\land v\succeq w$”。

在句法侧，给出一种模态偏好语言以表达基本偏好关系及其性质。该语言是命题逻辑的扩展，新增两个算子 $\lozenge^{\geq}\varphi$ 与 $\lozenge^{>}\varphi$（Van Benthem, Girard, & Roy 2009）[^van-2009]。其真值条件定义如下：

$\mathcal{M}$，$w \models \lozenge^{\geq} \varphi$ 当且仅当 存在 *v*，$v\succeq w$，且 $\mathcal{M}$，$v \models \varphi$。

$\mathcal{M}$，$w \models \lozenge^{>} \varphi$ 当且仅当 存在 *v*，$v \succ w$，且 $\mathcal{M}$，$v \models \varphi.$

下图 6 中的理论是 Van Benthem、Girard 与 Roy（2009）给出的模态偏好逻辑公理化，其中 $\succeq$ 是传递且自反的关系，E 是存在模态，解释如下：

$\mathcal{M}, w \models E\varphi$ 当且仅当 存在 $v, \mathcal{M}, v \models \varphi$。

**模态偏好逻辑**

- 对 $\lozenge^{\geq}$ 取 S4，对 *E* 取 S5，对 $\lozenge^{>}$ 取 K。
- 包含公理：
- $\lozenge^{>} \varphi\rightarrow\lozenge^{\geq} \varphi$
- $\lozenge^{\geq} \varphi\rightarrow\lozenge E\varphi$
- $\lozenge^{\geq}\varphi$ 与 $\lozenge^{>} \varphi$ 之间的交互公理：
- $\lozenge^{>}\lozenge^{\geq} \varphi\rightarrow\lozenge^{>} \varphi$
- $\lozenge^{\geq}\lozenge^{>} \varphi\rightarrow\lozenge^{>} \varphi$
- $\psi\land \lozenge^{\geq}\varphi\rightarrow\lozenge^{>}\varphi\lor \lozenge^{\geq}(\varphi\land \lozenge^{\geq}\psi)$

*图 6.*

### 3.3 偏好提升

上述模态偏好语言可以表达可能世界之间偏好关系的性质。但处理可能世界集合之间的关系会带来提升问题（Thomason & Horty 1996）[^thomason-1996]，因为它涉及把适用于单个世界的性质扩展到世界集合。实现这一点有多种方式。下面三个例子只使用两个量词。

$$\begin{align*} p\geq^{\forall\forall}q & := \forall w \models q\, \forall v\models p: v\succeq w \\ p>^{\forall\forall}q & := \forall w \models q\, \forall v\models p: v\succ w \\ \end{align*}$$ $$\begin{align*} p\geq^{\forall\exists}q & := \forall w \models q\, \exists v\models p: v\succeq w \\ p>^{\forall\exists}q & := \forall w \models q\, \exists v\models p: v\succ w \\ \end{align*}$$ $$\begin{align*} p\unrhd^{\overline{\forall\forall}}q & := \forall w \models p\, \forall v\models q: v\not\succ w \\ p\rhd^{\overline{\forall\forall}}q & := \forall w \models p\, \forall v\models q: v\not\succeq w\\ \end{align*}$$

在句法侧，为表达提升，基本模态偏好语言被扩展出全称模态 $U\varphi$（及其对偶 $E\varphi$）（Boutilier 1992）[^boutilier-1992]。这一新模态的真值定义是：

$\mathcal{M}$，$w \models U \varphi$ 当且仅当 对所有 *v*，$\mathcal{M}$，$v \models \varphi$。

有了这一模态，语言获得更强的表达力，可以定义与提升问题相关的一般偏好概念。下面给出一个例子：

$$\varphi\geq^{\forall\exists}\psi := U(\varphi\rightarrow\lozenge^{\geq}\psi).$$

我们可以把 $\varphi\geq^{\forall\exists}\psi$ 读作“对每个 *φ*-世界，都存在一个与该 *φ*-世界同样好的 *ψ*-世界”。其他一般偏好概念可类似定义。例如，$\forall\exists$-偏好与 $\exists\exists$-偏好可在该语言中定义如下：

1. $\varphi\geq^{\forall\exists}\psi := U(\varphi\rightarrow\langle\geq\rangle\psi)$
2. $\varphi\geq^{\exists\exists}\psi := E(\varphi\land\langle\geq\rangle\psi)$

Van Benthem、Girard 与 Roy（2009）主张，在其他条件不变的情况下，$\geq^{\forall\forall}$ 表示冯·赖特（1963）[^wright-1963] 在其偏好逻辑奠基之作中所意图的“偏好”概念，并给出其公理化。其他条件不变偏好的逻辑将在第 6 节讨论。

其他试图为可能世界集合上的偏好关系公理化的努力，也出现在各个研究领域。重要贡献包括 Van Fraassen（1973）、Lewis（1973）[^lewis-1973]、Spohn（1988）[^spohn-1988]、Boutilier（1990）[^boutilier-1990] 与 Halpern（1997）[^halpern-1997] 等。下面给出一个示例。

Halpern（1997）[^halpern-1997] 为“相对似然”逻辑提出了一个完全公理化。它在结构上类似于偏好逻辑，或他所谓的“偏好”。与早期公理化不同，他同时处理全预序与偏预序。所用语言与冯·赖特相同——排除嵌套偏好公式——但原子偏好公式 $\varphi>\psi$ 可以包含合取与析取。

给定偏好模型 $\mathcal{M}=(W, \succeq, V)$，偏好公式的解释如下：

> $\mathcal{M} \models \varphi > \psi$ 当且仅当 $⟦ \varphi ⟧ _{\mathcal{M}}$ 非空，且 $\forall v \in ⟦ \psi ⟧ _{\mathcal{M}}\exists u \in ⟦ \varphi ⟧ _{\mathcal{M}}$，使得 $u\succ v$，并且 *u* 支配 $⟦ \psi ⟧ _{\mathcal{M}}$

而 *u* 支配 *V*，当且仅当不存在 $v' \in V$ 使得 $v'\succ u$。

当 $\succeq$ 是偏序时，Halpern（1997）[^halpern-1997] 的完全公理化由图 7 所列公理与规则组成。公理 2 对应 $\succeq$ 的自反性，公理 3 对应 $\succeq$ 的传递性。在全预序情形下，还须加入公理 $\varphi_1>\varphi_2\rightarrow (\varphi_1>\varphi_3)\lor(\varphi_3>\varphi_2)$。

**系统 AX**

1. 命题演算重言式的一切代换实例。
2. $\neg (\varphi> \varphi)$
3. $((\varphi_1 \lor \varphi_2)> \varphi_3) \land ((\varphi_1\lor \varphi_3)> \varphi_2)\rightarrow(\varphi_1>(\varphi_2\lor \varphi_3))$
4. $U (\varphi_1\rightarrow\varphi_2) \land U(\varphi_3\rightarrow\varphi_4)\land(\varphi_1>\varphi_4) \rightarrow(\varphi_2>\varphi_3)$
5. 概括规则：对所有命题重言式 $\varphi$，有 $U\varphi,$。
6. 肯定前件：由 *φ* 与 $\varphi\rightarrow\psi$ 推出 *ψ*。

*图 7.*

Shi 与 Sun（2021）的近期论文探讨了另一种偏好提升方法，称为 Egli-Milner 序。这种双向方法形式定义如下，它同时考虑集合中的最好与最坏元素，与“有利地平衡最坏结果”的 maximin 原则相一致：

$$\mathcal{M}, w \models \varphi \geq \psi \text{ 当且仅当 } \begin{cases} (1) \ \forall x \in ⟦\varphi⟧_w \ \exists y \in ⟦\psi⟧_w : x \succeq_w y; \\ (2) \ \forall x \in ⟦\psi⟧_w \ \exists y \in ⟦\varphi⟧_w : y \succeq_w x \end{cases}$$

其中 $⟦\varphi⟧_w$ 表示满足 *φ* 的 *w*-可达世界集合。Egli-Milner 序传统上用于指称语义等领域；Shi 与 Sun（2021）把它扩展到偏好逻辑，为全预序导出的“凸序”建立了完全公理系统。

## 4. 基于理由的偏好

过去二十年，基于理由的偏好逻辑研究一直是本节综述的若干研究工作的主要焦点。

### 4.1 内在偏好与外在偏好

基于理由的偏好概念源于冯·赖特（1963）[^wright-1963] 提出的著名区分：内在偏好与外在偏好。这一区分取决于偏好是否有明确的理由或证成作为基础。

**外在偏好** 出现在一个选项因在特定方面被认为更好而胜过另一选项之时。例如，在冯·赖特的例子中，某人偏好红葡萄酒胜过白葡萄酒，因为前者有益于她的健康。这里对红葡萄酒的偏好是外在的，因为它基于关于健康益处的客观判断。外在偏好因此与某种底层理据相联系，往往涉及健康、实际考虑或专家建议等外部因素。

相反，**内在偏好** 是纯粹基于个人喜好的偏好，不需要任何明确的理由或证成。例如，某人可能偏好红葡萄酒胜过白葡萄酒，仅仅因为她喜欢那种味道。这种偏好是内在的，因为它完全由主观享受驱动，不涉及任何外部理据。

在外在偏好的形式模型中，通常采用 **双层结构** 来同时处理理由基础与偏好。

### 4.2 双层结构

#### 4.2.1 优先性与偏好

在选项之间作决定的语境中，优先性概念被引入（Liu 2008, 2010; De Jongh & Liu 2009）[^liu-2008][^liu-2010]。优先性表示按个人考量排序的重要属性，这些属性反过来决定选择之间的偏好。

双层结构由优先基与偏好组成。**优先基** 是一组按行动者考量排序的属性。考虑爱丽丝决定买哪栋房子的例子。她按成本、质量、邻里环境这一重要性顺序，用三项标准评价每栋房子。对爱丽丝来说，一栋房子的成本若符合她的预算就是好的，否则就是坏的。因此，她的决定由房子是否满足其优先标准以及这些标准的相对重要性引导。

为形式化这一点，使用一阶逻辑，常量 $d_0,$ $d_1,$…，变量 $x_0,$ $x_1,$…，以及谓词 $P,$ $Q,$ $P_0,$ $P_1,$…。为简便起见，这一设置假定有限域、一元谓词以及简单的、通常无量词的公式。

形式上，优先基是一个有序公式序列，写作

$$C_1(x) \gg C_2(x) \gg \dots \gg C_n(x) \quad (n \in \mathbb{N}),$$

其中每个 $C_m(x)$ ($1 \leq m \leq n$) 是恰好含一个自由变项 *x* 的公式。较早的优先性被认为按词典序比较晚的优先性更重要，从而形成偏好序。例如，$C_1 \land \neg C_2 \land \dots \land \neg C_m$ 偏好于 $\neg C_1 \land C_2 \land \dots \land C_m$。

为说明这一点，爱丽丝的优先基可能形如

$$C(x) \gg Q(x) \gg N(x),$$

其中 $C(x)$、$Q(x)$、$N(x)$ 分别表示 *x* 价格低（成本）、质量高、邻里环境好。给定两栋房子 $d_1$ 与 $d_2$，其属性为 $C(d_1),$ $C(d_2),$ $\neg Q(d_1),$ $\neg Q(d_2),$ $N(d_1)$ 与 $\neg N(d_2)$，按照这一优先基，爱丽丝会偏好 $d_1$ 胜过 $d_2$。

双层结构中的线性序优先性也可推广到偏序优先图（允许某些优先性不可比较），甚至推广到无序属性集（Kratzer 1981; Liu 2011b）[^kratzer-1981][^liu-2011b]。

在道义逻辑中，双层结构（优先性建立偏好或义务序）也得到广泛承认，尤其是在优先处理命令的系统中（见 Hansen 2008 与 Van Benthem, Grossi, & Liu 2010 的工作）[^hansen-2008][^liu-2010][^van-2010]；第 7 节将讨论。

##### 信念作为理由

上述从优先基定义偏好的方法，预设了关于一个备选项是否具有基中属性的完全信息。在信息不完全的情形下，信念起关键作用，行动者的偏好依赖于信念。这种情形需要引入 $BC(x),$ $\neg BC(x),$ 或 $B\neg C(x),$ 等公式，其中 $C_m$ 表示优先性。这一进路使复杂方面得以考虑，例如判定优先基中的某些属性是否适用，或更根本地，基于信念形成优先基。处理此类不确定性需要把信念语言与偏好语言结合起来；关于不确定性下定义偏好的各种程序，见 Liu（2011b）[^liu-2011b] 的工作。在此设置中，关于备选项是否具有某项优先性的信念，充当偏好的理由。

#### 4.2.2 显著属性与偏好

理性选择理论通常假定行动者具有固定偏好，却不解释这些偏好的起源。Dietrich 与 List（2013a,b）开始填补这一空白。他们提出一个建模偏好形成与变化的框架，主张偏好基于备选项的“动机显著”属性，而不是备选项本身。这一进路使偏好可以是基于理由的，并随不同属性变得显著而演变。

为形式化这一点：行动者对备选项的偏好序取决于这些备选项在给定状态中具有动机显著性的属性。

设 *X* 是备选项集合。设 *P* 是所有可能属性的集合，一个备选项可能具有其中某些属性。动机状态 $M \subseteq P$ 包含行动者在给定语境中认为显著的一切属性。

偏好由 *X* 上的二元关系 $\succeq_M$ 定义，其中 $x \succeq_M y$ 表示在状态 *M* 中备选项 *x* 弱偏好于 *y*。

为处理不同动机状态下的偏好变化，Dietrich 与 List（2013a,b）在 **属性组合** 上引入 **权衡关系** $\geq$：

- 每个备选项 *x* 都可由其具有的属性集 $S_x$ 描述。
- 对任意两个属性集，$S_x \geq S_y$ 表示 $S_x$ 中的属性偏好于 $S_y$ 中的属性。
- 因此，权衡关系充当稳定的底层结构，支撑行动者在不同动机状态下的偏好序。

形式上，若 *x* 与 *y* 是备选项，则行动者在状态 *M* 中的偏好 $x \succeq_M y$ 可表示如下：

$$x \succeq_M y \iff S_x \geq S_y,$$

其中 $S_x = \{ P \in M : x \text{ has } P \}$，$S_y = \{ P \in M : y \text{ has } P \}$。这一关系确保行动者在任何动机状态 *M* 中的偏好都反映其对跨语境属性组合的稳定评价。

Dietrich 与 List（2013a,b）的工作通过对照 **结构合理性** 与 **实质合理性** 来探讨合理性：结构合理性关注偏好的内部一致性（如传统经济学），实质合理性评价偏好的内容或价值。形式合理性要求逻辑连贯，例如若 *A* 偏好于 *B*、*B* 偏好于 *C*，则 *A* 偏好于 *C*。实质合理性则把自毁或有害的偏好视为“非理性”，即使它们前后一致，因为它评价偏好的价值，而不只是其连贯性。关于这些哲学问题的早期讨论见 Pettit（2002）[^pettit-2002]。

#### 4.2.3 理由与偏好

Osherson 与 Weinstein（2012）提出一种偏好逻辑，其中偏好不是任意或仅仅一致的，而是基于可识别的理由。该框架引入模态联结词，使支持某一结果的理由得以形式表达，从而为建模各种理由如何结合并塑造行动者偏好提供途径。

在决定是否安装火灾报警器时，一个人可能把安全与成本视为支持或反对该行动的不同理由。在此例中，偏好安装火灾报警器高度重视提高安全性，因此这一偏好基于“安全理由”。若经济拮据，成本可能成为反对安装报警器的理由。

每一理由（如安全或成本）都可用 **效用尺度** 量化，表示基于特定标准每个选择好多少或差多少。形式上，“效用函数” *u* 定义为映射

$$u: W \times S \rightarrow \mathbb{R}$$

其中 *W* 是可能世界集合，*S* 是安全、成本等效用尺度的索引集。

为评价是否安装火灾报警器之类的选择，模型使用 **选取函数** *s* 找出与真实世界最接近的备选世界，以供比较。例如，它比较：

- 世界 $w_1$：安装了火灾报警器（更安全的世界）；
- 世界 $w_2$：未安装火灾报警器（当前、较不安全的世界）。

形式上，**选取函数** $s(w, A)$ 根据与当前世界 *w* 的相似性，从集合 *A* 中选出一个代表世界：

$$s(w, A) = \text{closest world in } A \text{ to } w.$$

最后，偏好关系可用模态表达式形式定义。例如，$p \succ_1 \neg p$ 成立，当且仅当出于安全理由，安装报警器（由 *p* 表示）胜过不安装，记作安全效用尺度 $u_1$。若同时考虑 $u_2$（成本），偏好关系可结合 $u_1$ 与 $u_2$，从而把握平衡安全与成本的整体观点。

这一逻辑框架使结构化推理得以纳入偏好背后的具体理由，从而在现实决策语境中对选择作出细致表征。

Osherson 与 Weinstein 探讨可判定性问题以及模型子类的各种条件。

双层结构已成为建模有理由偏好的标准进路，并在各领域有潜在应用。近期一例是源于底层因果考量的偏好——见 Xie 与 Yan（2024）的相关工作。类似地，Chen、Shi 与 Wang（2024）把偏好与依赖整合进合作博弈，为纳什均衡、帕累托最优与沙普利核心等概念提供统一视角。

## 脚注

[^halldén-1957]: Halldén, Sören, 1957, *On the Logic of “Better”* (Library of Theoria 2), Lund: C.W.K. Gleerup.

[^hansson-2001]: –––, 2001, “Preference Logic”, in *Handbook of Philosophical Logic*, Dov M. Gabbay and Franz Guenthner (eds), second edition, Dordrecht: Kluwer, 319–393. doi:10.1007/978-94-017-0456-4_4

[^menger-1939]: Menger, Karl, 1939, “A Logic of the Doubtful. On Optative and Imperative Logic”, *Reports of a Mathematical Colloquium*, Notre Dame, IN, series 2, 1: 53–64.

[^wright-1963]: von Wright, Georg Henrik, 1963, *The Logic of Preference*, Edinburgh: Edinburgh University Press.

[^rescher-1966]: Rescher, Nicholas, 1966, *The Logic of Commands* (Monographs in Modern Logic), London: Routledge & K. Paul.

[^rescher-1967]: –––, 1967, “Semantic Foundations for the Logic of Preference”, in *The Logic of Decision and Action*, Nicholas Rescher (ed.), Pittsburgh: University of Pittsburgh Press, 37–62.

[^hansson-1969]: Hansson, Bengt, 1969, “An Analysis of Some Deontic Logics”, *Noûs*, 3(4): 373–398. doi:10.2307/2214372

[^lewis-1973]: Lewis, David, 1973, *Counterfactuals*, Oxford: Basil Blackwell.

[^makinson-1993]: Makinson David, 1993, “Five Faces of Minimality”, *Studia Logica*, 52(3): 339–379, doi:10.1007/bf01057652

[^boutilier-1990]: Boutilier, Craig, 1990, “Conditional Logics of Normality as Modal Systems”, in *Proceedings of the Eighth National Conference on Artificial Intelligence (AAAI’90)*, volume 1, Menlo Park, CA: AAAI Press, 594–599.

[^lamarre-1991]: Lamarre, Philippe, 1991, “S4 as the Conditional Logic of Nonmonotonicity”, in *Proceedings of the Second International Conference on Principles of Knowledge Representation and Reasoning (KR’91)*, James F. Allen, Richard Fikes, and Erik Sandewall (eds), San Francisco, CA: Morgan Kaufmann, 357–367.

[^tan-1996]: Tan, Yao-Hua and Leendert W. N. van der Torre, 1996, “How to Combine Ordering and Minimizing in a Deontic Logic Based on Preferences”, in *Deontic Logic, Agency and Normative Systems: Third International Workshop on Deontic Logic in Computer Science (DEON ’96)*, Mark A. Brown and José Carmo (eds), London: Springer London, 216–232. doi:10.1007/978-1-4471-1488-8_12

[^van-2009]: Van Benthem, Johan, Patrick Girard, and Olivier Roy, 2009, “Everything Else Being Equal: A Modal Logic for *Ceteris Paribus* Preferences”, *Journal of Philosophical Logic*, 38(1): 83–125. doi:10.1007/s10992-008-9085-3

[^thomason-1996]: Thomason, Richmond H. and John F. Horty, 1996, “Nondeterministic Action and Dominance: Foundations for Planning and Qualitative Decision”, in *Proceedings of the 6th Conference on Theoretical Aspects of Rationality and Knowledge (TARK ’96)*, Yoav Shoham (ed.), San Francisco, CA: Morgan Kaufmann, 229–250.

[^boutilier-1992]: –––, 1992, *Toward a Logic for Qualitative Decision Theory*, Ph.D. thesis, University of Toronto.

[^spohn-1988]: Spohn, Wolfgang, 1988, “Ordinal Conditional Functions: A Dynamic Theory of Epistemic States”, in *Causation in Decision, Belief Change, and Statistics*, William L. Harper and Brian Skyrms (eds), Dordrecht: Kluwer, 105–134. doi:10.1007/978-94-009-2865-7_6

[^halpern-1997]: Halpern, Joseph Y., 1997, “Defining Relative Likelihood in Partially-Ordered Preferential Structures”, *Journal of Artificial Intelligence Research*, 7: 1–24. doi:10.1613/jair.391

[^liu-2008]: Liu, Fenrong, 2008, *Changing for the Better: Preference Dynamics and Agent Diversity*, Ph.D. thesis, ILLC, University of Amsterdam.

[^liu-2010]: –––, 2010, “Von Wright’s ‘The Logic of Preference’ Revisited”, *Synthese*, 175(1): 69–88. doi:10.1007/s11229-009-9530-z

[^kratzer-1981]: Kratzer, Angelika, 1981, “Partition and Revision: The Semantics of Counterfactuals”, *Journal of Philosophical Logic*, 10(2): 201–216. doi:10.1007/bf00248849

[^liu-2011b]: –––, 2011b, *Reasoning about Preference Dynamics* (Synthese Library 354), Berlin: Springerd. doi:10.1007/978-94-007-1344-4

[^hansen-2008]: Hansen, Jörg, 2008, *Imperatives and Deontic Logic*, Ph.D. dissertation, Konstanz, Germany: University of Konstanz.

[^van-2010]: Van Benthem, Johan, Davide Grossi, and Fenrong Liu, 2010, “Deontics = Betterness + Priority”, in *Deontic Logic in Computer Science: 10th International Conference (DEON 2010)* (Lecture Notes in Computer Science 6181), Guido Governatori and Giovanni Sartor (eds), Berlin/Heidelberg: Springer, 50–65. doi:10.1007/978-3-642-14183-6_6

[^pettit-2002]: Pettit, Philip, 2002, *Rules, Reasons, and Norms: Selected Essays*, Oxford/New York: Oxford University Press. doi:10.1093/0199251878.001.0001
