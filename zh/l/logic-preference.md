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

## 5. 偏好改变

偏好会因多种触发因素而改变，因此偏好改变是一个自然会纳入考虑的现象。逻辑建模因而被提出来研究关于这些动态的推理。本节部分遵循 Lang 与 Van der Torre（2008）对偏好改变的分类，该分类以驱动改变的信息输入类型为依据。此外，本节强调双层结构中可能发生的动态变化。Grüne-Yanoff 与 Hansson（2009）讨论了偏好改变为何在社会科学、尤其是经济学中被忽视，该文集呈现了研究偏好改变的各种进路（另见“偏好”词条中关于偏好改变的一节）。本节考察逻辑传统中的主要观念与形式框架。

### 5.1 内在偏好修正

第一类偏好改变类似于信念改变：正如信念修正把新获得的信念纳入既有信念状态，内在偏好修正把新偏好纳入既有偏好状态。在这里，偏好由其他偏好修正以形成新偏好，信念并不介入。

建模偏好改变主要有两种方法：Alchourrón、Gärdenfors 与 Makinson（AGM）的公设框架（见“信念修正逻辑”词条中对 AGM 信念修正理论的描述），以及基于动态逻辑的系统（见“动态认知逻辑”词条）。两者都已被研究者广泛采用，以探讨各种形式的偏好改变。

Sven Ove Hansson（1995）[^hansson-1995] 对偏好改变作了细致分析，在 AGM 框架内区分出四种不同类型：

- **修正**：以修正语句“*φ* 优于 *ψ*”获得对 *φ* 而非 *ψ* 的偏好。
- **收缩**：移除“*φ* 优于 *ψ*”这一偏好。
- **增加**：向所考虑选项集中加入一个新选项。
- **删减**：从所考虑选项集中移除一个选项。

信念修正会分配优先级以尽量减少对先前信念的改动，而 Hansson 主张优先级并不适用于偏好修正。在偏好修正中，接纳诸如 $\varphi\succeq \psi$ 的新语句，可能涉及调整 *φ* 或 *ψ* 的位置。他还提出一种相似性度量，使修正后的偏好模型尽可能接近原模型，并为这些算子给出 AGM 式公设。

Van Benthem 与 Liu（2007）发展了一种动态认知逻辑的扩展，用以推理偏好改变。他们引入一个“建议”算子，记作 $\sharp\varphi$。公式 $[\sharp\varphi]\psi$ 意为“在 *φ* 被公开建议之后，*ψ* 成立”，其定义为：

$$(\mathcal{M}, s) \models [\sharp \varphi]\psi \quad\textrm{ 当且仅当 }\quad \mathcal{M}_{\sharp \varphi}, s \models \psi$$

其中 $\mathcal{M}_{\sharp \varphi}$ 与 $(\mathcal{M}, s)$ 具有相同的论域、赋值和现实世界，但偏好关系通过删去从 *φ* 世界到 $\neg \varphi$ 世界的偏好链接而更新：

$$\leq^{*} = \leq - \{(s, t) \mid \mathfrak{M}, s \models \varphi \textrm{ 与 } \mathfrak{M}, t \models \neg \varphi\}.$$

更一般地，在此框架中，建议 $\sharp(\varphi)$ 可理解为命题动态逻辑（PDL）中的一个关系程序（参 Harel、Kozen 与 Tiuryn 2000）[^harel-2000]，即

$$(?\neg \varphi ; R) \cup (R ; ?\varphi)$$

它表示保留所有既有 *R* 链接，唯独去掉从 *φ* 世界到 $\neg \varphi$ 世界的链接。这一设置允许不同类型的偏好改变。例如，添加偏好链接（使每个 *φ* 世界都优于每个 $\neg \varphi$ 世界）可表示为

$$R := R \cup (?\neg \varphi ; \top; ?\varphi)$$

其中 $\top$ 表示全关系。**激进偏好升级** 定义为

$$\Uparrow \varphi(R) := (?\varphi;R;?\varphi)\cup(?\neg \varphi; R;?\neg \varphi) \cup (?\neg \varphi;\top;?\varphi)$$

它使所有 *φ* 世界都优于所有 $\neg \varphi$ 世界，同时保留各组内部的原有排序。

这一动态偏好逻辑通过支持多种改变关系的算子而扩展了 DEL，Van Benthem 与 Liu（2007）为这些算子给出了完全性定理。他们的结果利用 PDL 形式，使得动态模态可归约，并可递归计算归约公理。

### 5.2 信念更新驱动的偏好改变

第二类偏好改变源于信念的改变，反映了行动者所信与其评价选项方式之间的动态互动。这一主题已获得相当关注（见 Bradley 2007、Lang 与 Van der Torre 2008、Liu 2011b 的工作）[^bradley-2007][^lang-2008][^liu-2011b]。例如，沿袭 Savage（1954）[^savage-1954] 所奠定的决策论传统，Bradley 主张偏好改变可源于信念改变，即“偏好改变是由信念在可能性空间某一划分上的重新分配所引发的”。他用贝叶斯进路形式化这一原则。考虑 Lang 与 Van der Torre（2008）的如下例子：

> 起初，我想吃这盘里的寿司。随后我得知这寿司是用不新鲜的鱼做的。现在我不想吃这寿司了。（2008：351）

得知寿司用不新鲜的鱼制作改变了我的信念，进而逆转了我最初的偏好。在这里，偏好改变是信念改变的结果，因此信念改变成为建模的关键要素。

AGM 框架通过为信念集应如何适应新的、可能冲突的信息建立公设来处理信念修正。Lang 与 Van der Torre（2008）把类似进路用于由信念更新引起的偏好改变。他们提出的形式语言包括：一个信念二元模态算子 $N(\alpha\mid\beta)$，意为“给定 *β*，*α* 是正常的（或被相信的）”；一个偏好算子 $P(\alpha\mid\beta)$，意为“给定 *β*，*α* 更受偏好”；以及一个动态算子 $[*\alpha]\beta$，读作“在学习 *α* 之后，*β* 成立”。为刻画偏好改变的性质，他们提出八条公设。下面给出两例：

$$\tag{P1} P\alpha \rightarrow [*\alpha]P\alpha $$

（P1）意为：得知某事已被偏好，并不会改变最初的偏好。例如，如果我渴望财富，那么在我变得富有之后，这一偏好仍然保留。这种持续性通常显得自然，但有争议；例如在 Jeffrey 的决策论中，一旦你变得富有，想变得富有的欲望可能不再适用。

$$\tag{P5} P\alpha \land N\beta \rightarrow [*\beta]P\alpha$$

（P5）蕴含：得知原本预期之事确实如此，不应改变既有偏好。该原则等价地表述为 $P\alpha \land \neg[*\beta]P\alpha \rightarrow \neg N\beta$，它表达的是：意外信息是偏好改变得以发生的必要条件。

总之，信念更新驱动偏好改变，这表明两者关系密切。AGM 理论与动态逻辑系统等框架为建模这一演化提供了工具。

### 5.3 偏好改变的双层模型

在双层结构中，优先基可因各因素相对重要性的变化而移动，从而自然导致偏好的相应改变。De Jongh 与 Liu（2009）考察了线性优先基与偏好之间的互动，并展示了优先性移动如何影响偏好关系。在相关语境中，Andréka、Ryan 与 Schobbens（2002）在更一般的非线性图结构中探讨了从各种优先排序导出偏好的方法。在这些观念的基础上，Girard（2008）[^girard-2008] 与 Liu（2011a）[^liu-2011a] 引入基本图更新操作，为分析优先结构的变化提供形式框架。Christoff、Gratzl 与 Roy（2021）研究了标签相继式中的优先合并证明论。

#### 5.3.1 图更新：基本操作

假设有一个优先基，记作 $\mathscr{B}$，它是一组带优先级的命题。当加入新命题 *A* 时，有几种直接的纳入方式：

- **赋予 *A* 最高优先级**：可将 *A* 置于优先基顶端，使其成为最重要的命题。
- **赋予 *A* 最低优先级**：可将 *A* 加到底部，使其优先级最低。
- **并置**：可将 *A* 与 $\mathscr{B}$ 并排放置，而不在 *A* 与其他优先项之间建立次序。

基本图更新的集合 $\alpha(\mathscr{B}, A)$ 以能够刻画这些可能变化的方式定义：

$$\alpha(\mathscr{B}, A) := A \mid \mathscr{B}_1 ; \mathscr{B}_2 \mid \mathscr{B}_1 \parallel \mathscr{B}_2.$$

这里，$\mathscr{B}_1 ; \mathscr{B}_2$ 表示把 $\mathscr{B}_1$ 加到 $\mathscr{B}_2$ 之上的顺序组合，使得 $\mathscr{B}_1$ 中每个元素都优先于 $\mathscr{B}_2$ 中每个元素。并行组合（$\mathscr{B}_1 \parallel \mathscr{B}_2$）把 $\mathscr{B}_1$ 与 $\mathscr{B}_2$ 作为彼此无优先次序的不相交集合组合起来。

优先基不仅可通过插入新命题来修改，也可通过删除操作移除优先关系。例如，顶部删除会移除优先基中那些不被其他项“支配”的项，即处于最高优先级层次的项。

这些基本图更新为通过增删命题来重构给定优先基提供了简单方式。

#### 5.3.2 追踪动态

为追踪不同层次——世界层与优先层——之间的变化，我们定义一个特定的技术概念。给定优先更新 $\alpha: (\mathscr{B}, A) \rightarrow \mathscr{B'}$ 与世界层映射 $\sigma: (\preceq, A) \rightarrow \preceq'$，称 *α* **诱导** *σ*，当且仅当：

$$\sigma(\preceq_{\mathscr{B}}, A) = \preceq_{\alpha(\mathscr{B}, A).}$$

一个操作 *α* 是 *PDL 可定义操作*，如果它通过使用语言中公式的测试、弱与严格基本偏好关系 *R* 以及全关系，并允许任意并集与顺序组合，诱导出一个 *PDL* 可定义的关系变换器 *σ*：

$$\pi:=?\varphi \mid R\mid R^{<} \mid \top\mid ;\mid \cup.$$

这些被解释为 *PDL* 的标准程序操作：**测试** $?\varphi$、**顺序组合** “;”与 **选择** “∪”。

在双层框架中，考察优先动态如何映照偏好动态是很有意思的。例如，既可通过改变世界层偏好关系，也可通过修改优先基，来实现由“建议”算子引起的偏好改变。若把新命题 *A* 并行加入既有基 $\mathscr{B}$，偏好关系会按下图更新：

![交换图：扩展说明见下](../../assets/logic-preference/figxy1.svg)

*图 A*：把新命题 A 并行加入既有基的交换图 [图 A 的扩展说明见补充材料。]

类似地，把新命题 *A* 置于优先图 $(\mathscr{B}, <)$ 顶端，对应于世界层的一次激进升级：

![图：扩展说明见下](../../assets/logic-preference/figxy2.svg)

*图 B*：把新命题 A 置于优先图顶端的交换图 [图 B 的扩展说明见补充材料。]

这些例子表明，优先层变换与世界层关系更新可以无缝对应。

尽管优先动态与偏好动态常常一致，但也存在限制。例如，删除操作 $\textit{del}(\mathscr{B})$ 不是 *PDL* 可定义的（Liu 2011a）[^liu-2011a]。某些自然的优先层修改无法在世界层完全表示。

#### 5.3.3 双层结构中的信念驱动偏好改变

在双层结构中，考虑由信念更新驱动的偏好改变同样合理。在 De Jongh 与 Liu（2009）的框架中，采用多种策略从优先基与信念导出偏好，如下例所示：

> Alice 正在找公寓。她认为价格比邻里环境更重要。她相信公寓 $d_1$ 价格低但邻里环境差。她对公寓 $d_2$ 的价格 **没有信息**，但相信其邻里环境好。

在涉及不确定性的情形中，“决策策略”通过优先考虑每个选项被相信满足的最重要标准来比较两个选项。在此语境中，Alice 会基于其信念偏好 $d_1$ 而非 $d_2$。

然而，如果她的信念改变（例如得知 $d_2$ 价格低），她的偏好可能转向偏好 $d_2$ 而非 $d_1$。这突显了由信念更新引起的偏好改变与由优先性移动引起的偏好改变之间的区别，如前面例子所示。

总之，优先动态与偏好动态虽然密切相关，却各自保留独特特征，这凸显了同时建模内在偏好与基于理由的偏好在全面理解行动者决策方面的价值。

## 6. 其他条件不变偏好与 CP 网

**其他条件不变** 偏好指在“其余条件相同”的条件下表达偏好的一种方式。它使行动者能够断言某一选项优于另一选项，同时假定其他所有相关因素保持不变。在用于决策的 AI 系统中，CP 网是一种用于表征条件偏好的图模型。它依赖如下原则：选项之间的比较是在其他因素不变的假定下作出的，这与 **其他条件不变** 概念高度契合。

本节介绍 **其他条件不变** 偏好的逻辑研究结果，以及 CP 网的基础知识。

### 6.1 在逻辑中形式化 **其他条件不变** 偏好

**其他条件不变** 偏好的核心问题是如何解释“其余条件相同”。例如，一个人通常可能偏好红葡萄酒胜过白葡萄酒（**其他条件不变**），但如果红葡萄酒有毒而白葡萄酒无毒，则不然。因此，形式化 **其他条件不变** 限定的挑战在于：如何确定除葡萄酒颜色之外的条件是否相同。哈勒登（1957）[^halldén-1957] 与冯·赖特（1963）[^wright-1963] 在偏好逻辑的最初研究中已讨论过这一问题。**其他条件不变** 的“相等”读法与“其余条件正常”的正常性读法之间的区别，也由 Van Benthem、Girard 与 Roy（2009）讨论过。

在解释“其余条件相同”一语时，一种自然的进路是使用世界的等价类。该领域许多研究者采取了这一进路。例如，Doyle 与 Wellman（1994）定义了个体之间依赖语境的等价关系，称为语境等价。因此，这意味着等价类可能随所考虑的语境而变化。

形式上，设 $\Omega$ 为状态集，$\mathcal{E}(\Omega)$ 表示 $\Omega$ 上所有等价关系的集合。语境等价定义在集合 $\Omega$ 上，是一个函数 *η*：$\mathcal{P}(\mathcal{P}(\Omega))\rightarrow\mathcal{E} (\Omega)$，为每个命题集合 $\{p, q, \ldots\}$ 指派一个等价关系 $\eta(p, q, \ldots)$。对于 $w\,\eta(p,q,\ldots)\, w^{\prime}$，我们写作 $w\approx_{ mod\, p,q,\ldots} w^{\prime}$，意为就 $p, q, \ldots$ 而言，*w* 与 $w^{\prime}$ 相同。Doyle 与 Wellman（1994）由此提出把可能性空间划分为等价类，并忽略跨越这些类的比较链接。

Van Benthem、Girard 与 Roy（2009）把这一观念应用于可能世界之间的等价关系：在某个指定集合中所有相关模态公式上的真值等价。此外，他们展示了这一概念如何与冯·赖特的工作相联系，以及它如何应用于博弈论解概念。他们在语言中引入形式为 $\langle \Gamma \rangle\varphi$ 的新模态，形式定义为

$$p\mid \neg \varphi\mid \varphi\land \psi \mid\langle \Gamma \rangle^{>}\varphi\mid \langle \Gamma \rangle^{\geq}\varphi\mid \langle \Gamma \rangle\varphi,$$

其中 *Γ* 是任意公式集。这样，“相等”成为形式语言本身的一部分。在语义上，*Γ* 定义可能世界的一个等价类。例如，$w \approx_{\Gamma} v$ 表示 *w* 与 *v* 在 *Γ* 上相等——它们满足 *Γ* 中相同的公式。

一个 **其他条件不变** 偏好模型是四元组 $\mathcal{M}$= $(W, \succeq, \trianglerighteq_{\Gamma}, V)$，其中：

- *W* 是状态集，$\succeq$ 是二元偏好关系，*V* 是赋值
- $\trianglerighteq_{\Gamma}$ 是由 $w\trianglerighteq_{\Gamma}v$ 当且仅当 $w\succeq v$ 且 $w \approx_{\Gamma} v$ 给出的二元关系
- 严格子关系 $\trianglerighteq_{\Gamma}$ 由 $w\succ v$ 且 $w \approx_{\Gamma} v$ 定义

关系 $\trianglerighteq_{\Gamma}$ 本质上是两个世界间关系的交集：基本偏好关系，以及相对于 *Γ* 中公式的真值等价。涉及等价类的新公式的真值条件为：

- $\mathcal{M}, w \models \langle \Gamma \rangle^{\geq}\varphi$ 当且仅当 $\exists v$ 使得 $v \trianglerighteq_{\Gamma} w$ 且 $\mathcal{M}, v\models \varphi$
- $\mathcal{M}, w \models \langle \Gamma \rangle^{>}\varphi$ 当且仅当 $\exists v$ 使得 $v \vartriangleright_{\Gamma} w$ 且 $\mathcal{M}, v\models \varphi$
- $\mathcal{M}, w \models \langle \Gamma \rangle\varphi$ 当且仅当 $\exists v$ 使得 $v \approx_{\Gamma} w$ 且 $\mathcal{M}, v\models \varphi$

对于 *Γ* 有限的情形，Van Benthem、Girard 与 Roy（2009）给出了完全公理化。就 **其他条件不变** 的特征而言，新的公理集见图 8。

当 $\varphi\in\Gamma$ 时 **其他条件不变** 集合的自反性公理：

1. $\langle \Gamma \rangle\varphi\rightarrow\varphi$
2. $\langle \Gamma \rangle\neg \varphi\rightarrow\neg\varphi$

当 $\Gamma \subseteq\Gamma^{\prime}$ 时 **其他条件不变** 集合的单调性公理：

1. $\langle \Gamma^{\prime} \rangle\varphi\rightarrow\langle \Gamma \rangle\varphi$
2. $\langle \Gamma^{\prime} \rangle^{\geq}\varphi\rightarrow\langle \Gamma \rangle\varphi$
3. $\langle \Gamma^{\prime} \rangle^{>}\varphi\rightarrow\langle \Gamma \rangle\varphi$

刻画 **其他条件不变** 集合变化的公理：

1. $\pm\varphi\land \langle \Gamma \rangle(\alpha\land \pm \varphi)\rightarrow\langle \Gamma \cup\{\varphi\} \rangle\alpha$
2. $\pm\varphi\land \langle \Gamma \rangle^{\geq}(\alpha\land \pm \varphi)\rightarrow\langle \Gamma \cup\{\varphi\} \rangle^{\geq}\alpha$
3. $\pm\varphi\land \langle \Gamma \rangle^{>}(\alpha\land \pm \varphi)\rightarrow\langle \Gamma \cup\{\varphi\} \rangle^{>}\alpha$

*图 8：* Van Benthem、Girard 与 Roy（2009）对 **其他条件不变** 偏好的公理化

在完整语言中，模态 $\langle\Gamma\rangle\varphi$ 中的 *Γ* 可以具有任意大小。Seligman 与 Girard（2011）的后续工作给出了完整逻辑一部分——即所谓“灵活”有效式集合——的公理化，并提供了一种替代语义，其中所有有效式都是灵活的，因而得到完全公理化。任意无限集合的公理化仍是一个开放问题。

### 6.2 其他条件不变偏好的计算模型

CP 网（CP-net）是“条件偏好网络”的简称，它本质上体现了 **其他条件不变** 概念，而后者正是这些网络表征偏好方式的核心原则。本节介绍 CP 网的基础知识，突出其在 **其他条件不变**（其余条件相同）假定下表征行动者偏好的紧凑、直观且有结构的方式。

条件偏好网络（CP 网）是定义如下的图模型。

设 $V = \{X_1, X_2, \ldots, X_n\}$ 是变量集，其中每个 $X_i$ 都有可能取值的有限域 $\text{Dom}(X_i)$。有一个有向图 *G*，其中：

- 每个变量 $X_i$ 对应一个节点。
- $X_i$ 的父节点记作 $\text{Pa}(X_i)$，是那些有边指向 $X_i$ 的节点。这些父节点表示影响对 $X_i$ 偏好的变量。从 $X_i$ 到 $X_j$ 的边意味着对 $X_j$ 的偏好取决于 $X_i$ 的取值。

CP 网不列出所有可能结果的偏好（那会随变量数目指数增长），而是使用条件偏好表（CPT）只刻画相关依赖（即偏好所依赖的要素）。每个节点 $X_i$ 标注一个 CPT，为 $\text{Pa}(X_i)$ 的每一种可能实例化 *u* 指定 $\text{Dom}(X_i)$ 上的全序 $\succ_{u}$。例如：

> 若 $\text{Pa}(X_i) = \{A, B\},$ 则 $X_i$ 的 CPT 指定 *A* 与 *B* 的所有组合上的偏好。

CP 网的语义描述如何根据每个网络的结构与条件偏好表导出结果上的偏好。

**结果** 是对 CP 网中所有变量取值的完整指派。例如，若 $V = \{X_1, X_2, X_3\}$，且各域为

$$\text{Dom}(X_1) = \{a_1, a_2\}, \quad \text{Dom}(X_2) = \{b_1, b_2\}, \quad \text{Dom}(X_3) = \{c_1, c_2\},$$

则一个结果会是 $o = \{X_1 = a_1, X_2 = b_2, X_3 = c_1\}$。

按照 **其他条件不变** 假定（即比较结果时保持其他所有变量不变），若我们遵循每个变量 CPT 中指定的条件偏好，便可得到结果上的偏好。

例如，若 $X_2$ 的 CPT 指定在 $X_1 = a_1$ 时 $b_1 \succ b_2$，则：

$$\begin{align*} \text{若 } &o_1 = \{X_1 = a_1, X_2 = b_1, X_3 = c_1\} \text{ 且 }\\ &o_2 = \{X_1 = a_1, X_2 = b_2, X_3 = c_1\}, \text{ 则 } o_1 \succ o_2.\\ \end{align*}$$

可以设计算法来高效地找出 CP 网中的最优结果——见 Boutilier、Brafman 等（2004）、Wilson（2004）[^wilson-2004] 以及 Goldsmith、Lang 等（2008）的工作。

通过只刻画相关的条件偏好，CP 网避免了枚举所有可能结果之偏好所带来的组合爆炸。CP 网在 AI 驱动的决策中已展现出重要价值，应用于推荐系统与产品配置等领域。它们在计算机科学与人工智能领域引起了相当多的关注，Allen（2015）[^allen-2015] 以及 Cai、Zhan 与 Jiang（2023）等较新工作即体现了这一点。

## 7. 跨研究领域的偏好

### 7.1 偏好与条件逻辑

众所周知，自 1960 年代末与 1970 年代初以来，偏好逻辑 $p\geq^{\forall\exists}q$ 与条件逻辑之间一直存在紧密关系（Lewis 1973）[^lewis-1973]，因为其中一些系统可以相互定义。

例如，如果我偏好鱼胜过肉，偏好肉胜过素食，而我在一家只供应牛排或沙拉的牛排馆，那么在该语境中，我偏好牛排。此类关于偏好与事实的推理把偏好推理与条件推理联系起来。

在可能世界语义学中，这可以从条件逻辑的模型同时也是偏好结构这一事实得到解释。然而，这些偏好逻辑是作为 1960 年代末与 1970 年代初条件逻辑与道义逻辑的对应物发展起来的，与哈勒登和冯·赖特在此前十年发展的偏好逻辑颇为不同。

若我们用 $\varphi\Rightarrow \psi$ 表示条件句“如果 *φ* 那么 *ψ*”，则在适当条件下，我们可以定义：*φ* 优于 *ψ*，当且仅当 $\varphi\lor \psi$ 蕴含 *φ* 而非 *ψ*：

$$\varphi\geq^{\forall\exists} \psi :=\neg ((\varphi\lor \psi)\Rightarrow \neg \varphi).$$

于是我们也有：条件句“如果 *φ* 那么 *ψ*”定义为 $\varphi\land \psi$ 优于 $\varphi\land \neg \psi$：

$$\varphi\Rightarrow \psi := (\psi\land \varphi)>^{\forall\exists}(\neg \psi\land \varphi).$$

由于自然语言中条件句的频繁使用，条件逻辑更受欢迎。我们可以说，一些偏好逻辑在文献中以条件逻辑之名流传，另一些则以道义逻辑之名流传。然而，这一结果并不推出偏好逻辑与条件逻辑是同一回事。一般而言，条件句与比较句之间的关系只得到部分理解（Makinson 1993）[^makinson-1993]。

### 7.2 偏好与道义逻辑

传统道义逻辑常用可能世界语义学解释义务与允许等概念，其中世界按理想性由偏好关系排序。道义公式在当前世界的语境中根据其与这些理想世界的可达性来评价：一个行动是义务性的，当且仅当它出现在从当前世界可达的所有最受偏好的世界中。较佳世界与最佳世界之间的复杂关系已由 Parent（2014）[^parent-2014] 以及 Grossi、Van der Hoek 与 Kuijer（2022）广泛考察。这种排序反映了直观的道义原则，但难以处理冲突与困境，因为单一排序可能无法充分刻画多重且可能不相容的命令。

Makinson（1999）[^makinson-1999] 强调规范（无真值的命令）与道义命题（关于义务或允许、可为真或为假的陈述）之间的区分。他认为这一区分在当代道义逻辑中被忽视，并呼吁把道义逻辑“重构”为以明确命令而非抽象真值条件为基础的系统。在其 2012 年的著作中，Horty 作出了显著贡献：他提出一个理解行动背后理由的框架，以缺省逻辑作为基础结构。他阐明多重理由如何相互作用——相互支持、压倒或冲突——从而决定个体应当做什么。

这些对理由的关注促成了道义逻辑中基于命令的语义学的发展，它相对于明确的命令集来定义道义算子。标准道义系统（例如一元系统与二元系统）已被调整以适应这一模型，并扩展出处理命令之间优先冲突与困境的机制。道义逻辑也采用了双层结构。值得注意的工作包括 Hansen（2008, 2014）[^hansen-2008][^hansen-2014]、Van Benthem、Grossi 与 Liu（2014）以及 Benzmüller、Parent 与 Van der Torre（2020）。

### 7.3 决策论与博弈论中的偏好

在决策论与博弈论中，“偏好”与“偏好关系”概念被用来建模选择，通常带有行为解释。偏好关系的形式性质及其通过效用函数的表征已在文献中得到广泛研究，其中一些甚至早于偏好逻辑。本词条主要强调对偏好的定性进路，后者关注偏好关系的形式性质。相比之下，定量进路通常依赖效用函数以数值方式表征偏好。不确定性下的决策通常用期望值框架建模，该框架把行动者的信念（表示为概率）与效用结合起来以刻画偏好。批判性研究重新审视了偏好理论的基础。例如，Hausman（2012）[^hausman-2012] 区分了作为选择、福利与价值的偏好概念，并提出效用函数能否充分刻画福祉的问题——尤其当定性因素塑造个体偏好时。Fu（2020）提出一种新进路，整合定性与定量方法，以更准确地反映现实决策的复杂性。为把本词条与决策论联系起来，考虑第 4 节所呈现的更丰富双层结构所产生的基于理由偏好的数值化、定量化表征至关重要。

### 7.4 社会选择理论中的偏好

在社会选择理论中，核心问题是如何把个体偏好聚合为连贯的群体偏好。该领域一个著名结果是 Arrow（1951）[^arrow-1951] 的不可能性定理，它表明在满足某些合意条件的前提下构造公平聚合规则的局限。后续研究探索了替代假定，产生了新结果。例如，Andréka、Ryan 与 Schobbens（2002）用图表示选项的替代排序，作为聚合个体偏好的一种方法。List（2022）[^list-2022]（在社会选择理论词条中）对该主题提供了有用综述。在社会环境中，个体偏好往往并不完全独立，而受同伴观点影响。作为一个共同体，思考社会偏好如何随时间演变、稳定偏好能否出现，是颇有意思的问题。Seligman、Liu 与 Girard（2011）以及 Liang 与 Seligman（2011）[^seligman-2011][^seligman-2011-2] 讨论了该主题的逻辑研究。这一研究领域需要探索共同体结构、个体偏好的更新机制以及定义社会偏好的方法。相关洞见可借鉴社会信念方面的研究，如 Shi（2021）[^shi-2021][^shi-2021-2]。演化博弈论也研究了类似问题，特别是所谓社会偏好的“间接演化进路”。例如，Bowles 与 Gintis（2011）考察利他、公平与合作等亲社会偏好如何演化并达到稳定。

## 8. 结论

偏好逻辑为理解行动者如何比较情境并作出决策提供了一个多用途框架。本词条综述了该领域的关键发展，追溯其从句法与算法进路到语义框架的演变。它还着重介绍了关于双层结构的最新研究——这些结构源于内在偏好与外在偏好的区分，强调理由在塑造偏好中的作用。

对偏好改变的研究以及 **其他条件不变** 偏好的概念，突显了偏好逻辑的动态与实践面向，尤其是在决策语境中。这些框架将继续作为应对未来挑战、推进该领域研究的基础。

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

[^hansson-1995]: Hansson, Sven Ove, 1995, “Changes in Preference”, *Theory and Decision*, 38(1): 1–28. doi:10.1007/bf01083166

[^harel-2000]: Harel, David, Dexter Kozen, and Jerzy Tiuryn, 2000, *Dynamic Logic*, Cambridge, MA: MIT Press. doi:10.7551/mitpress/2516.001.0001

[^bradley-2007]: Bradley, Richard, 2007, “The Kinematics of Belief and Desire”, *Synthese*, 156(3): 513–535. doi:10.1007/s11229-006-9136-7

[^lang-2008]: Lang, Jérôme and Leendert van der Torre, 2008, “From Belief Change to Preference Change”, in *Proceedings of the 18th European Conference on Artificial Intelligence (ECAI-2008)* (Frontiers in Artificial Intelligence and Applications 178), Malik Ghallab, Constantine D. Spyropoulos, Nikos Fakotakis, Nikos Avouris (eds), IOS Press, 351–355. doi:10.3233/978-1-58603-891-5-351

[^savage-1954]: Savage, Leonard J., 1954, *The Foundations of Statistics* (Wiley Publications in Statistics), New York: Wiley.

[^girard-2008]: Girard, Patrick, 2008, *Modal Logics for Belief and Preference Change*, Ph.D. thesis, Stanford University.

[^liu-2011a]: –––, 2011a, “A Two-Level Perspective on Preference”, *Journal of Philosophical Logic*, 40(3): 421–439. doi:10.1007/s10992-010-9168-9

[^wilson-2004]: Wilson, Nic, 2004, “Extending CP-Nets with Stronger Conditional Preference Statements”, in *Proceedings of the 19th National Conference on Artificial Intelligence (AAAI’04)*, Deborah L. McGuinness and George Ferguson (eds), San Jose, CA: AAAI Press, 735–741. [[Wilson 2004 available online](https://aaai.org/papers/00735-AAAI04-116-extending-cp-nets-with-stronger-conditional-preference-statements/)]

[^allen-2015]: Allen, Thomas E., 2015, “CP-Nets: From Theory to Practice”, in *Algorithmic Decision Theory* (Lecture Notes in Computer Science 9346), Toby Walsh (ed.), Cham: Springer, 555–560.

[^parent-2014]: Parent, Xavier, 2014, “Maximality vs. Optimality in Dyadic Deontic Logic”, *Journal of Philosophical Logic*, 43(6): 1101–1128. doi:10.1007/s10992-013-9308-0

[^makinson-1999]: –––, 1999, “On a Fundamental Problem of Deontic Logic”, in *Norms, Logics and Information Systems. New Studies on Deontic Logic and Computer Science*, Paul McNamara and Henry Prakken (eds), Amsterdam: IOS Press, 29–53.

[^hansen-2014]: –––, 2014, “Reasoning about Permission and Obligation”, in *David Makinson on Classical Methods for Non-Classical Problems* (Outstanding Contributions to Logic 5), Sven Ove Hansson and David Makinson (eds), Dordrecht: Springer, 255–280. doi:10.1007/978-94-007-7759-0_14

[^hausman-2012]: Hausman, Daniel M., 2012, *Preference, Value, Choice, and Welfare*, Cambridge/New York: Cambridge University Press. doi:10.1017/cbo9781139058537

[^arrow-1951]: Arrow, Kenneth J., 1951, *Social Choice and Individual Values* (Yale University. Cowles Foundation for Research in Economics 12), New York: John Wiley & Sons.

[^list-2022]: List, Christian, 2022, “Social Choice Theory”, in *The Stanford Encyclopedia of Philosophy* (Winter 2022), Edward N. Zalta and Uri Nodelman (eds), URL = <[https://plato.stanford.edu/archives/win2022/entries/social-choice/](https://plato.stanford.edu/archives/win2022/entries/social-choice/)>. First published 2013.

[^seligman-2011]: Seligman, Jeremy and Patrick Girard, 2011, “Flexibility in Ceteris Paribus Reasoning”, *The Australasian Journal of Logic*, 10: 67–99. doi:10.26686/ajl.v10i0.1826

[^seligman-2011-2]: Seligman, Jeremy, Fenrong Liu, and Patrick Girard, 2011, “Logic in the Community”, in *Logic and Its Applications: Fourth Indian Conference (ICLA 2011)* (Lecture Notes in Computer Science 6521), Mohua Banerjee and Anil Seth (eds.), Berlin/Heidelberg: Springer, 178–188. doi:10.1007/978-3-642-18026-2_15

[^shi-2021]: Shi, Chenwei, 2021, “Collective Opinion as Tendency Towards Consensus”, *Journal of Philosophical Logic*, 50(3): 593–613. doi:10.1007/s10992-020-09579-0

[^shi-2021-2]: Shi, Chenwei and Yang Sun, 2021, “Logic of Convex Order”, *Studia Logica*, 109(5): 1019–1047. doi:10.1007/s11225-020-09940-z
