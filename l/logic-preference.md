# 偏好逻辑 Preference Logic (Fenrong Liu and Leon van der Torre)

*首次发表于 2025 年 7 月 28 日。*

偏好的概念横跨众多研究领域，对这一主题产生了多样的视角。偏好逻辑专门关注在比较对象、情形、行动等时的偏好推理，途径是考察其形式性质。本词条综述偏好逻辑迄今的主要发展。第 2 节给出历史概览，始于 Halldén 与 von Wright 的奠基工作——他们强调偏好的语法面向。第 3 节引入 Rescher 与 Van Dalen 的早期语义学贡献。对可能世界的偏好关系自然引出模态偏好逻辑，其中偏好提升（preference lifting）使跨可能世界集合的比较成为可能。第 4 节引入 von Wright 对内在偏好与外在偏好之分，并呈现外在（即基于理由的）偏好的双层结构——这是过去二十年的主要发展方向。本词条评述该领域的主要框架。第 5 节讨论偏好改变——它可以因多种原因发生——并探究这些动态的不同逻辑进路。第 6 节讨论其余条件相同（ceteris paribus）偏好的多种解释，评述其底层逻辑，并考察与之密切相关的条件偏好网络（CP 网）。第 7 节简要考察偏好逻辑与其他研究领域的关联。第 8 节收束本词条。

## 1 引言

偏好逻辑天然是跨学科的：对偏好的表示与分析因领域而异。但有一个独特的共同特征——偏好关乎比较情形、对象或行动。这类比较所涉的二元关系是：“*A* 优于 *B*”($>$)、“*A* 与 *B* 一样好”($\equiv$)，以及“*A* 不劣于 *B*”($\geq$)。

偏好逻辑始于语法进路，其聚焦支配偏好关系的形式原理。与之相对，语义进路旨在为这些关系提供解释，从而得以识别这些原理在何种条件下成立。尤其是，可能世界语义提供了一个系统框架，可从语义视角探究偏好逻辑。本词条的展开正反映了从语法进路到语义进路的这一过渡。

行动者作比较时，产生的偏好或者只反映其自身趣味、无需外部证成，或者源自得到外部证成的特定理由。纯粹基于行动者自身趣味而形成的偏好称为内在偏好；反之，能由外部理由解释或证成的偏好称为外在偏好。本词条以 von Wright（1963）的这一著名区分为中心主题，引介偏好逻辑中的经典与当代工作。

外在偏好要求模型中有额外要素，以同时表示偏好与证成它们的理由。这类理由可以是优先性、对象属性或价值。逻辑与理性选择理论中已提出若干主要框架——在这两个学科中，偏好传统上被当作固定的。“双层结构”一词将用来描述这些框架。这一更丰富的建模方式，使推理不仅针对偏好本身，也针对其底层理由。有趣的是，道义逻辑中可见一种平行发展：基于规范的语义为道义概念引入附加结构，与外在偏好模型背后的想法高度契合。

偏好逻辑的另一关键主题是偏好改变研究，这与纳入新信息的更宽潮流一致。正如知识、信念与意图等态度可能需要更新，偏好也会随新信息、行动者状态的改变或其他因素而演化。本词条假定读者熟悉信念修正理论（参见 SEP 偏好词条）与动态认知逻辑（DEL；参见动态认知逻辑词条），并专门聚焦偏好改变的独特方面。

在必须作决策的 AI 系统中，偏好往往需要简明地表示。此语境的一个核心概念是其余条件相同的偏好——它使诸如“*A* 优于 *B*，其余条件相同”的偏好推理成为可能。这一概念在逻辑中已被广泛研究，也是计算机科学文献中 CP 网（条件偏好网络）等框架的基础。CP 网是一种著名的可视化语言，兼顾表达力与计算效率。因此，本词条对其余条件相同的偏好给予大量关注。

## 2 偏好逻辑的语法进路

开创性的逻辑学家如 Halldén（1957）与 von Wright（1963）提出了聚焦情形间比较的偏好逻辑。这些逻辑以二元联结词 $>$ 扩充命题语言，表示偏好或“较优”概念。

### 2.1 Halldén：理论 A 与理论 B

Halldén（1957）的著作《论“更好”的逻辑》常被视为偏好逻辑分析的起点，是所有其他偏好逻辑的参照点。Halldén 以两个新联结词扩充命题逻辑——他称之为“伦理联结词”：“更好”($>$)与“一样好”($\equiv$)。他区分 $\equiv$ 的肯定义与否定义，由此得出理论 A 与理论 B。理论 A 基于肯定义，形式上由 $p\equiv q$ 当且仅当对一切 r，$r>p$ 当且仅当 $r>q$，且 $p>r$ 当且仅当 $q>r$ 给出。理论 B 基于否定义，其中 $p\equiv q$ 即 $\neg(p>q)\land \neg(q>p)$。

由命题变元、普通真值函项联结词以及两个新联结词构造起来的句子称为“A 公式”。它们遵循惯常的省略括号约定，读法基于递减的结合次序：$\neg$、$>$、$\equiv$、$\land$、$\lor$、$\rightarrow$、$\leftrightarrow$。

**理论 A.** 理论 A 如图 1 所示，是命题演算的扩充。公设 $A_1–A_5$ 表明 Halldén 把 $>$ 当作非对称且传递的关系，即偏序；而“$\equiv$”被当作自反、对称且传递的关系，即等价关系。Halldén 早在 1939 年就把这些假定追溯到 Menger（参 Menger 1939）[^menger-1939]。$A_6$ 关乎“更好”与“等值”两概念的相互关系。扩充原理 $A_7$ 与 $A_8$ 使用否定；它们在后来 von Wright 的偏好逻辑中也居于中心地位。

图 1.

**理论 A**

命题演算的一切定理都是理论 A 的公设。

**$R_1$**

若 $\varphi$ 与 $\varphi\rightarrow\psi$ 是 A 的定理，则 $\psi$ 是 A 的定理（分离规则）。

**$R_2$**

设 $\varphi$ 是 A 的定理，且 $\psi$ 除一处外处处与 $\varphi$ 相似：凡 $\varphi$ 中出现某变元之处，$\psi$ 中出现一个 A 公式。则 $\psi$ 是 A 的定理（代入）。

**$R_3$**

设 $\varphi$ 与 $\tau_1\equiv\tau_2$ 是 A 的定理，$\psi$ 是 A 公式，且 $\psi$ 除一处外处处与 $\psi$ 相似：$\tau_1$ 在 $\psi$ 的一处或多处出现，而 $\tau_2$ 在 $\varphi$ 中出现。则 $\psi$ 是 A 的定理（替换）。

$$\begin{align*} \tag*{\(A_1\)} p> q\rightarrow\neg (q > p)&& \textrm{(\(>\)-asymmetry)}\\ \tag*{\(A_2\)} p>q \land q >r\rightarrow p>r&& \textrm{(\(>\)-transitivity)}\\ \tag*{\(A_3\)} p\equiv p&& \textrm{(\(\equiv\)-reflexivity)}\\ \tag*{\(A_4\)} p\equiv q \rightarrow q\equiv p&& \textrm{(\(\equiv\)-symmetry)}\\ \tag*{\(A_5\)} p\equiv q \land q\equiv r \rightarrow p\equiv r&& \textrm{(\(\equiv\)-transitivity)}\\ \tag*{\(A_6\)} p>q\land q\equiv r \rightarrow p>r&& \textrm{(\(>\equiv\)-transitivity)}\\ \tag*{\(A_7\)} p>q\leftrightarrow(p\land \neg q)> (q\land \neg p)&& \textrm{(\(>\)-expansion)}\\ \tag*{\(A_8\)} p\equiv q\leftrightarrow(p\land \neg q)\equiv(q\land \neg p)&& \textrm{(\(\equiv\)-expansion)} \end{align*} $$

图 1。

Halldén 证明理论 A 一致。他给出理论 A 的若干定理，如逆否：$p>q \rightarrow\neg q>\neg p$。他还考虑了可加到理论 A 上的十四条可选公设。例如分配公设 $p>(q\land r)\rightarrow p>q \land p>r$，以及连通性公设 $p>q \lor p\equiv q \lor q>p$。

**理论 B.** 理论 B 的语言是理论 A 语言的一个片段，只含不含 $>$ 与 $\equiv$ 嵌套出现的句子。此外，若 $\varphi>\psi$ 或 $\varphi\equiv\psi$ 出现于一个 B 公式中，则 $\varphi$ 与 $\psi$ 不含合取或析取符号。

理论 B 由图 2 中的规则与公设构成。公设 $B_1–B_5$ 与 $A_1–A_5$ 相同；$B6$ 可由理论 A 导出；$B_7$ 表示连通性。

图 2。

**理论 B**

* 命题演算的一切定理都是 B 的公设。
* 理论 A 的推理规则 $R_1, R_2$ 与 $R_3$ 也适用于理论 B。

$$\begin{align*} \tag*{\(B_6\)} p>q \rightarrow\neg q>\neg p&& \textrm{(contraposition)}\\ \tag*{\(B_7\)} p>q \lor p\equiv q \lor q>p && \textrm{ (connected)} \end{align*}$$

图 2。

理论 B 已被证明一致。有趣的是，书中给出一个程序，可判定给定公式是否为 B 的定理。它由两步构成，称为单义展开与多义展开。

第一阶段把逻辑原理应用于展开公式。例如 $p\equiv q$ 换为 $p\equiv q \land q \equiv p$，$p> q\land q>r$ 换作 $p> q\land q>r\land p>r$。考虑 Halldén（1957）给出的如下替换序列，用以判定是否

$$p\equiv \neg p\land q\equiv \neg q \rightarrow \neg (p>q)$$

是一个定理：

$$\begin{gather*} p\equiv \neg p\land q\equiv \neg q \land p>q\\ p\equiv \neg p\land \neg p\equiv p\land q\equiv \neg q \land p>q\\ p\equiv \neg p\land \neg p\equiv p\land q\equiv \neg q \land \neg q\equiv q \land p>q\\ p\equiv \neg p\land \neg p\equiv p\land q\equiv \neg q \land \neg q\equiv q \land p>q\land \neg q>\neg p\\ p\equiv \neg p\land \neg p\equiv p\land q\equiv \neg q \land \neg q\equiv q \land p>q\land \neg q>\neg p\land \neg q>p\\ p\equiv \neg p\land \neg p\equiv p\land q\equiv \neg q \land \neg q\equiv q \land p>q\land \neg q>\neg p\land \neg q>p\land q>\neg p\\ p\equiv \neg p\land \neg p\equiv p\land q\equiv \neg q \land \neg q\equiv q \land p>q\land \neg q>\neg p\land \neg q>p\land q>\neg p\land p>\neg q \end{gather*}$$

最后一个公式是矛盾的，因此我们可以断定 $p\equiv \neg p\land q\equiv \neg q \rightarrow \neg (p>q)$ 是定理。

若第一阶段无法判定，则第二步把每个公式展开为一组更复杂的公式。例如 $p>q\land \neg q> \neg p$ 无法再用单义展开推进，但可展开为如下公式集：

$$\begin{align} &p>q\land \neg q> \neg p\land p>\neg p, \\ &p>q\land \neg q> \neg p\land p\equiv \neg p, \\ &p>q\land \neg q> \neg p\land \neg p>p, \\ &p>q\land \neg q> \neg p\land \neg p\equiv p, \end{align}$$

反映出 p 与 $\neg p$ 之间所有可能的关系。有兴趣的读者可在 Halldén（1957）的书中找到其运作的更多细节。

### 2.2 Von Wright 的偏好逻辑

第二个参照点是 von Wright（1963）的《偏好逻辑》。在此书中，von Wright 区分了与偏好相关的三组概念，同时指出它们之间没有截然分界。相关概念组是：道义论概念（正当、义务、命令、禁止）、价值论概念（善、恶、较优）与人类学概念（需要、意愿、决定、选择）。这些概念在道义逻辑与决策论中得到探讨，并与偏好逻辑相交。这一关联将在第 7 节讨论。von Wright 还提出几个对偏好逻辑后续发展至关重要的区分：

* 事态之间的偏好 对 手段或方法的偏好
* 内在偏好（内在较优） 对 外在偏好（有理由的偏好）
* 定性偏好 对 可测量的价值（如效用）
* 无风险的偏好 对 不确定性下的偏好

更具体地说，von Wright 采纳的形式语言仍是 Halldén A 公式的一个片段，只含不含 $>$ 与 $\equiv$ 嵌套出现的句子。但与理论 B 的语言不同：若 $\varphi>\psi$ 或 $\varphi\equiv\psi$ 出现于一个公式中，$\varphi$ 与 $\psi$ 可以含合取或析取符号。

与 Halldén 的两个理论不同，偏好逻辑并非作为公理演算给出。相反，它是一种判定技术：判定给定的偏好表达式（P 表达式）是否表示一个逻辑上为真的命题。

偏好逻辑基于五条关键原理，见图 3。前两条——非对称与传递——描述偏好间的关系，源自 Halldén 的系统。其余三条——扩充、析取分配与放大——使任何 P 表达式都能变换为标准形，从而可应用判定技术。此技术以一例说明。考虑 P 表达式

$$(p>\neg p)\land (\neg q>q)\rightarrow(p>q).$$

使用扩充我们得到

$$(p>\neg p)\land (\neg q>q)\rightarrow(p\land \neg q>\neg p \land q).$$

由于原子偏好中没有析取，分配是空洞的。第三步放大给出标准形

$$ \begin{align} (p\land q>\neg p\land q) &\land (p\land \neg q>\neg p\land \neg q)\\ &\land (p\land \neg q>p\land q)\\ &\land (\neg p\land \neg q>\neg p\land q) \rightarrow(p\land \neg q>\neg p \land q). \end{align} $$

这个公式是重言式，可以如下解释。该公式为假，当且仅当头四个成分

$$\begin{align} &(p\land q>\neg p\land q), \\ &(p\land \neg q>\neg p\land \neg q), \\ &(p\land \neg q>p\land q) \textrm{ and} \\ &(\neg p\land \neg q>\neg p\land q) \end{align}$$

都为真而 $(p\land \neg q>\neg p \land q)$ 为假。但这与传递性相冲突。

考察这五条关于偏好的原理时须加小心，因为它们在代入下不封闭。这一限制背后的推理在下文说明。

*Figure 3.*

**Von Wright’s 5 preference principles**

$$\begin{align} &\tag*{\(V_1\)} (p>q) \rightarrow\neg (q>p)&& \textrm{(\(>\)-asymmetry)}\\[1em] & \tag*{\(V_2\)} (p>q) \land (q >r)\rightarrow q>r&& \textrm{(\(>\)-transitivity)}\\[1em] & \tag*{\(V_3\)} (p>q)\leftrightarrow(p\land \neg q)> (\neg p\land q)&& \textrm{(\(>\)-expansion)}\\ \end{align}$$ $$ \begin{align}\tag*{\(V_4\)}\quad (p&\lor q)>(r \lor s) \leftrightarrow \\ &(p \land \neg r \land \neg s) > (\neg p\land \neg q \land r) \\ &\land\ (p\land \neg r \land \neg s)> (\neg p\land \neg q \land s)\\ &\land\ (q\land \neg r \land \neg s)> (\neg p\land \neg q \land r)\\ &\land\ (q\land \neg r \land \neg s)> (\neg p\land \neg q \land s) \ \text{(disjunctive distribution)} \end{align} $$ $$ \begin{align}\tag*{\(V_5\)} (p&>q) \leftrightarrow \\ &((p\land r)> (q\land r)) \\ &\land\ ((p\land \neg r)>(q\land \neg r)) \qquad {\textrm{(amplification)}} \end{align} $$

图 3。

von Wright 的另一项贡献，是他试图以“改变”来理解偏好的含义。他的分析揭示了一种看待偏好的独特方式。何时能说一种事态优于另一种？为回答此问题，考虑两个一般的偏好状态 p 与 q。有四种可能情形：$p \land q$、$p \land \neg q$、$\neg p \land q$ 与 $\neg p \land \neg q$。任何世界必然落入这四种可能之一。这不仅解释了 Halldén 已采纳的前三条原理，也解释了上表 $V_4$ 所示例示的析取分配原理。

在 $p\land q$ 的情形中，“行动者偏好 p 胜过 q”意味着：行动者宁可失去 q（而保留 p），也不愿失去 p（而保留 q）。

在 $p\land \neg q$ 的情形中，“行动者偏好 p 胜过 q”意味着：行动者宁可维持当前状态，也不愿看到它变为 $\neg p\land q$。

在 $\neg p\land q$ 的情形中，“行动者偏好 p 胜过 q”意味着：行动者宁可看到世界从 $\neg p$ 变为 p、q 变为 $\neg q$，也不愿看到毫无变化。

在 $\neg p \land \neg q$ 的情形中，“行动者偏好 p 胜过 q”意味着：行动者宁可得到没有 q 的 p，也不愿得到没有 p 的 q。

原理 $V_5$ 是所谓偏好的整体性性质。设 $\varphi$ 为一公式，$PL(\varphi)$ 为 $\varphi$ 中出现的命题字母之集——von Wright 称之为论域。设 $r \not\in PL(\varphi>\psi)$，则把每个公式 $\varphi> \psi$ 替换为合取

$$((\varphi\land r)> (\psi\land r)) \land ((\varphi\land \neg r)>(\psi\land \neg r)).$$

这一原理也称为放大，应用于命题字母集中 $PL(\varphi > \psi)$ 的补集中的每一个 r。放大保证：论域中每个与偏好子公式之评估没有直接关联的 r 都保持恒定。

虽然 $V_1$、$V_2$、$V_3$ 与 $V_4$ 出现于许多公理化偏好逻辑中，$V_5$ 却不然。原因是 $V_5$ 不能与代入相结合。

自 Halldén 以来，文献中已探索了大量原理。全面的综述见 S. O. Hansson（2001）关于该主题的章节，其中包含如下例子：

*Figure 4:*

$$\begin{align*} \tag{H1} \textrm{There is no series } p_1,\ldots, p_n \\ \textrm{such that } p_1>\ldots>p_n>p_1 && \textrm{(\(>\)-acyclic)}\\ \tag{H2} p\equiv q \land q >r \rightarrow p>r &&\textrm{(\(\equiv\)\(>\)-trans)}\\ \tag{H3} p> q \land q >r \rightarrow p>s \lor s>r && \textrm{(semi-trans)}\\ \tag{H4} p>q \land r >s \rightarrow p>s \lor r>q && \textrm{(interval order)} \end{align*} $$

图 4：更多偏好原理

Halldén 与 von Wright 都通过采纳语法或算法进路来强调偏好原理的普遍性。后来的研究者常用例子来支持或挑战这些原理，而许多偏好性质至今悬而未决。

## 3 偏好逻辑的语义进路

本节通过引入 Rescher（1967）与 Van Dalen（1974）的早期方案以及可能世界语义，给出偏好的语义视角；后者一直是这一领域后续研究的核心。

### 3.1 Rescher-Van Dalen 语义学

Rescher（1966, 1967）引入了偏好逻辑的第一个语义学，其模型是公式上的实值函数。Van Dalen（1974）把它推广到偏序，并证明 Rescher 的偏好逻辑是一个特例。语义结构直接反映语言所表达的偏好。我们在此给出 Van Dalen 的语义学与公理化。

该语言与 von Wright 的语言一致，即以二元联结词 $>$ 扩充命题逻辑——只是此处不含嵌套的偏好陈述。无差异由偏好定义：$\varphi\equiv \psi = \neg (\varphi>\psi)\land \neg (\psi>\varphi)$。

为了给形如 $\varphi>\psi$ 的公式赋真值，Van Dalen 规定命题之间的一个序关系。他同时考虑真值赋值 v 与善的测度 m。在此框架中，m 是从命题集到偏序集 A 的映射；v 是从命题符号（原子）到 $\{0,1\}$ 的映射，并由如下归纳定义扩充到所有公式：

1. $v(\neg \varphi) = 1-v(\varphi)$
2. $v(\varphi\lor\psi) = \textrm{max}\{v(\varphi),v(\psi)\}$
3. $v(\varphi P\psi) = 1$ if $m(\varphi) \lt m(\psi)$ on A, or 0 otherwise

For a set $\Gamma$ of formulas, the satisfaction relation is defined by:

$$\begin{align*} A, m, v \models p &\quad \textrm{ iff}\quad v(p) = 1 \textrm{ for atomic } p\\ A, m \models \varphi &\quad \textrm{ iff}\quad A, m, v \models \varphi \textrm{ for all } v\\ A, v \models \varphi &\quad \textrm{ iff}\quad A, m, v \models \varphi \textrm{ for all } m\\ A \models \varphi &\quad \textrm{ iff}\quad A, m, v\models \varphi \textrm{ for all } m \textrm{ and } v\\ \models \varphi &\quad \textrm{ iff}\quad A \models \varphi \textrm{ for all } A (\varphi \textrm{ is true})\\ A, m, v \models \Gamma &\quad \textrm{ iff}\quad A, m, v \models \Gamma \textrm{ for all } \varphi\in\Gamma\\ \Gamma\models \varphi &\quad \textrm{ iff}\quad A, m,v\models\Gamma \Rightarrow A, m,v\models \varphi\\ \end{align*}$$

Van Dalen 把上述语义称为非理性语义，主要是因为逻辑等价的命题可以导致不同的偏好。因此他考虑对测度 m 或偏序集 A 添加三个额外条件，以得到更具受限性的语义：

1. If $\varphi\equiv \psi$ is a tautology, then $m (\varphi) = m(\psi)$.
2. A is linearly ordered.
3. A is the set of reals and $m(\neg \varphi)=-m(\varphi)$.

Van Dalen 给出多个理论——**PREFIR**、**PREF**、**PREFL** 与 **PREFR**——概述于图 5。他证明：**PREFIR** 对非理性语义完全，**PREF** 对带条件 (i) 的语义完全，**PREFL** 对线性语义完全，**PREFR** 对 Rescher 语义完全。

*Figure 5.*

Van Dalen 的偏好理论 **PREFIR**、**PREF**、**PREFL** 与 **PREFR**

* 古典命题逻辑的一切重言式都是公理。
* 分离规则与替换（见 Halldén 的理论 A）

$$\begin{align*} \tag*{P1} \neg (\varphi> \varphi) \\ \tag*{P2} \varphi>\psi \land \psi >\chi \rightarrow \varphi> \chi\\ \tag*{P3} \varphi>\psi \land \psi \equiv\chi \rightarrow \varphi> \chi\\ \tag*{P4} \varphi>\psi \rightarrow \neg \psi > \neg \varphi\\ \end{align*}$$

我们将考虑若干公理系统：它们都以重言式为公理、以分离规则为推理规则；除第一个外，都以替换规则为推理规则。

**PREFIR**

公理 P1, P2（只应用分离规则）

**PREF**

公理 P1, P2

**PREFL**

公理 P1, P2, P3

**PREFR**

公理 P1, P2, P3, P4

图 5。

此外，Van Dalen 证明所有系统都有有穷模型性质且可判定。他还以“善”“恶”“中立”的一元算子扩充该语言，并考虑嵌套的偏好陈述。Chisholm 与 Sosa（1966）等其他作者则考虑这类偏好逻辑的一阶扩充。

### 3.2 可能世界上的偏好

在模态逻辑迅速发展的时代（参见模态逻辑词条），二元偏好关系被自然地纳入可能世界语义，以便在不同语境中比较不同的情形或世界。本小节与下一小节评述模态偏好逻辑，并讨论提升偏好以比较可能世界集合的多种方法。

自 1960 年代末以来，二元模态逻辑被发展为条件义务的模型（B. Hansson 1969）[^hansson-1969]，并伴随条件句的相关形式理论（Lewis 1973; Makinson 1993）[^lewis-1973][^makinson-1993]。在这些框架中，可能世界语义下的偏好结构得到使用，尤其是在道义逻辑与条件句的研究中。

从 1980 年代末开始，一种被广泛采纳的一元模态进路兴起，它在非单调逻辑与信念修正（Boutilier 1990; Lamarre 1991）[^boutilier-1990][^lamarre-1991]以及道义逻辑（Tan & Van der Torre 1996）[^tan-1996]中探索偏好。这些工作的动机各异，但一元模态进路在某些情形下为偏好逻辑的公理化提供了更直接的路径。

偏好逻辑研究常与理解动态环境中的行动者选择相关联。一个核心焦点是：行动者如何为可能世界排序以表达其偏好。这使决策制定与规范性推理的模型更加细致。受条件逻辑与信念修正早期发展的启发，把偏好序整合进模态逻辑，通过纳入可能世界上的偏好结构而扩展了逻辑系统的表达力。

模态偏好模型 $\mathcal{M}$ 是三元组 $(W, \succeq, V)$：W 是可能世界集合，$\succeq$ 是这些世界上的二元偏好关系，V 是为这些世界中的命题字母赋真值的赋值。依语境不同，我们假定偏好关系 $\succeq$ 具有某些性质：例如可以是（全）预序，或偏序等。若选（全）预序，则严格偏好关系“$w\succ v$”可定义为“$w\succeq v\land v \nsucceq w$”，无差异关系“$w\approx v$”可定义为“$w\succeq v\land v\succeq w$”。

在语法方面，给出一套模态偏好语言以表达基本的偏好关系及其性质。该语言是命题逻辑的扩充，带有两个新算子 $\lozenge^{\geq}\varphi$ 与 $\lozenge^{>}\varphi$（Van Benthem, Girard, & Roy 2009）。其真值条件定义如下：

$\mathcal{M}$, $w \models \lozenge^{\geq} \varphi$    iff    for some v   with $v\succeq w$, $\mathcal{M}$, $v \models \varphi$.

$\mathcal{M}$, $w \models \lozenge^{>} \varphi$    iff    for some v   with $v \succ w$, $\mathcal{M}$, $v \models \varphi.$

下图 6 所示的理论是 Van Benthem、Girard 与 Roy（2009）给出的模态偏好逻辑公理化，其中 $\succeq$ 是传递且自反的关系，E 是存在模态词，解释如下：

$\mathcal{M}, w \models E\varphi$    iff    for some $v, \mathcal{M}, v \models \varphi$.

*Figure 6.*

**模态偏好逻辑**

* S4 for $\lozenge^{\geq}$, S5 for E, K for $\lozenge^{>}$.
* Inclusion axioms:
* $\lozenge^{>} \varphi\rightarrow\lozenge^{\geq} \varphi$
* $\lozenge^{\geq} \varphi\rightarrow\lozenge E\varphi$
* Interaction axioms between $\lozenge^{\geq}\varphi$ and $\lozenge^{>} \varphi$:
* $\lozenge^{>}\lozenge^{\geq} \varphi\rightarrow\lozenge^{>} \varphi$
* $\lozenge^{\geq}\lozenge^{>} \varphi\rightarrow\lozenge^{>} \varphi$
* $\psi\land \lozenge^{\geq}\varphi\rightarrow\lozenge^{>}\varphi\lor \lozenge^{\geq}(\varphi\land \lozenge^{\geq}\psi)$

图 6。

### 3.3 偏好提升

上述模态偏好语言可以表达可能世界之间偏好关系的性质。但要处理可能世界集合之间的关系，会遇到一个提升问题（Thomason & Horty 1996）[^thomason-1996]：它涉及把适用于个别世界的性质扩展到世界集合。实现方式有多种。下面三个例子只使用两个量词。

$$\begin{align*} p\geq^{\forall\forall}q & := \forall w \models q\, \forall v\models p: v\succeq w \\ p>^{\forall\forall}q & := \forall w \models q\, \forall v\models p: v\succ w \\ \end{align*}$$ $$\begin{align*} p\geq^{\forall\exists}q & := \forall w \models q\, \exists v\models p: v\succeq w \\ p>^{\forall\exists}q & := \forall w \models q\, \exists v\models p: v\succ w \\ \end{align*}$$ $$\begin{align*} p\unrhd^{\overline{\forall\forall}}q & := \forall w \models p\, \forall v\models q: v\not\succ w \\ p\rhd^{\overline{\forall\forall}}q & := \forall w \models p\, \forall v\models q: v\not\succeq w\\ \end{align*}$$

在语法方面，为表达提升，基本模态偏好语言以全称模态词 $U\varphi$（及其对偶 $E\varphi$）扩充（Boutilier 1992）[^boutilier-1992]。这一新模态词的真值定义是：

$\mathcal{M}$, $w \models U \varphi$    iff    for all v  , $\mathcal{M}$, $v \models \varphi$.

有了这一模态词，语言获得更大的表达力，可以定义与提升问题相关的一般偏好概念。我们给出一个例子：

$$\varphi\geq^{\forall\exists}\psi \coloneq U(\varphi\rightarrow\lozenge^{\geq}\psi).$$

我们可以把 $\varphi\geq^{\forall\exists}\psi$ 读作“对每个 $\varphi$-世界，都存在一个与该 $\varphi$-世界同样好的 $\psi$-世界”。我们可以类似方式定义其他一般偏好概念。例如 $\forall\exists$-偏好与 $\exists\exists$-偏好可在语言中定义如下：

1. $\varphi\geq^{\forall\exists}\psi \coloneq U(\varphi\rightarrow\langle\geq\rangle\psi)$
2. $\varphi\geq^{\exists\exists}\psi \coloneq E(\varphi\land\langle\geq\rangle\psi)$

Van Benthem、Girard 与 Roy（2009）论证：其余条件相同下的 $\geq^{\forall\forall}$ 表示 von Wright（1963）在其偏好逻辑开创性著作中所意指的“偏好”概念，并为其提供公理化。其余条件相同的偏好逻辑将在第 6 节讨论。

为可能世界集合上的偏好关系公理化逻辑的其他尝试，出现在各个研究领域。值得注意的贡献包括 Van Fraassen（1973）、Lewis（1973）、Spohn（1988）、Boutilier（1990）与 Halpern（1997）等人的工作。下面给出一个示例。

Halpern（1997）为“相对似然”逻辑提出一个完全公理化。它在结构上类似于偏好逻辑——或如他所称的“偏好”。与早期公理化不同，他同时处理全预序与偏序。所用语言与 von Wright 相同——排除嵌套偏好公式——只是原子偏好公式 $\varphi>\psi$ 可以包含合取与析取。

给定偏好模型 $\mathcal{M}=(W, \succeq, V)$，偏好公式解释如下：

> $\mathcal{M} \models \varphi > \psi$ iff $\llbracket \varphi \rrbracket _{\mathcal{M}}$ is nonempty, $\forall v \in \llbracket \psi \rrbracket _{\mathcal{M}}\exists u \in \llbracket \varphi \rrbracket _{\mathcal{M}}$ such that $u\succ v$ and u dominates $\llbracket \psi \rrbracket _{\mathcal{M}}$

and u dominates V if there is no $v' \in V$ such that $v'\succ u$.

当 $\succeq$ 是偏序时，Halpern（1997）的完全公理化由图 7 所列的公理与规则构成。公理 2 对应 $\succeq$ 的自反性，公理 3 对应 $\succeq$ 的传递性。在全预序情形，还须添加公理 $\varphi_1>\varphi_2\rightarrow (\varphi_1>\varphi_3)\lor(\varphi_3>\varphi_2)$。

*Figure 7.*

**系统 AX**

1. All substitution instances of tautologies of propositional calculus.
2. $\neg (\varphi> \varphi)$
3. $((\varphi_1 \lor \varphi_2)> \varphi_3) \land ((\varphi_1\lor \varphi_3)> \varphi_2)\rightarrow(\varphi_1>(\varphi_2\lor \varphi_3))$
4. $U (\varphi_1\rightarrow\varphi_2) \land U(\varphi_3\rightarrow\varphi_4)\land(\varphi_1>\varphi_4) \rightarrow(\varphi_2>\varphi_3)$
5. Gen. $U\varphi,$ for all propositional tautologies.
6. MP. From $\varphi$ and $\varphi\rightarrow\psi$ infer $\psi$.

图 7。

Shi 与 Sun（2021）的一篇近期论文探索了偏好提升的另一种方法，即 Egli-Milner 序。这一双向进路（形式定义见下）同时考虑集合中的最好与最坏元素，与趋利避害地平衡最坏结果的最大最小原则相呼应：

$$\mathcal{M}, w \models \varphi \geq \psi \text{ iff } \begin{cases} (1) \ \forall x \in \llbracket\varphi\rrbracket_w \ \exists y \in \llbracket\psi\rrbracket_w : x \succeq_w y; \\ (2) \ \forall x \in \llbracket\psi\rrbracket_w \ \exists y \in \llbracket\varphi\rrbracket_w : y \succeq_w x \end{cases}$$

where $\llbracket\varphi\rrbracket_w$ denotes the set of w-accessible worlds that satisfy $\varphi$. Traditionally applied in fields like denotational semantics, Shi and Sun (2021) extend the Egli-Milner order to preference logic by developing a complete axiomatic system for the “convex order” derived from a total pre-order.

## 4 基于理由的偏好

过去二十年，基于理由的偏好逻辑研究是本节综述之诸工作的主要焦点。

### 4.1 内在偏好与外在偏好

基于理由的偏好概念源自 von Wright（1963）提出的内在偏好与外在偏好的著名区分。这一区分的关键在于：偏好是否植根于一个明确的理由或证成。

外在偏好产生于如下情形：一个选项之所以优于另一个，是因为它在某个特定方面被认为更好。例如在 von Wright 的例子中，某人偏好波尔多红酒胜过莱茵白葡萄酒，因为红酒有益其健康。这里对红酒的偏好是外在的，因为它基于一个关于健康益处的客观判断。因此，外在偏好系于某种底层理据——常涉及健康、实际考量或专家建议等外部因素。

相比之下，内在偏好是纯粹基于个人喜好的偏好，无需明确的理由或证成。例如，某人可能偏好红酒胜过白酒，仅仅因为喜欢其口味。这一偏好是内在的，因为它完全由主观享受驱动，不涉及任何外部理据。

在外在偏好的形式模型中，通常采用双层结构来兼顾理由基与偏好。

### 4.2 双层结构

#### 4.2.1 优先性与偏好

在选项间作决定的语境中，（Liu 2008, 2010; De Jongh & Liu 2009）[^liu-2008]引入了优先性概念。优先性表示按个人考量排序的重要属性，它们又决定选项间的偏好。

双层结构由一个优先基与偏好构成。优先基是按行动者的考量排序的一组属性。考虑爱丽丝决定买哪套房的例子。她依三条标准评估每套房——成本、质量与社区，并按此重要次序。对爱丽丝而言，若房价符合预算则其成本是好的，否则是坏的。她的决定便由房子是否满足其优先标准、以及这些标准的相对重要性所引导。

为形式化这一点，使用一带常元 $d_0,$ $d_1,$…、变元 $x_0,$ $x_1,$… 与谓词 $P,$ $Q,$ $P_0,$ $P_1,$… 的一阶逻辑。为简明起见，这一设定假定有穷论域、一元谓词与简单的（通常无量词的）公式。

形式上，优先基是一个有序的公式序列，写作

$$C_1(x) \gg C_2(x) \gg \dots \gg C_n(x) \quad (n \in \mathbb{N}),$$

其中每个 $C_m(x)$（$1 \leq m \leq n$）是恰有一个自由变元 x 的公式。靠前的优先性按词典序被视为比靠后者更重要，由此产生偏好序。例如，$C_1 \land \neg C_2 \land \dots \land \neg C_m$ 优于 $\neg C_1 \land C_2 \land \dots \land C_m$。

为说明这一点，爱丽丝的优先基可能是

$$C(x) \gg Q(x) \gg N(x),$$

其中 $C(x)$、$Q(x)$ 与 $N(x)$ 分别表示 x 价格低（成本）、质量高与社区好。给定两套房 $d_1$ 与 $d_2$，其性质为 $C(d_1),$ $C(d_2),$ $\neg Q(d_1),$ $\neg Q(d_2),$ $N(d_1)$ 与 $\neg N(d_2)$，则按这一优先基爱丽丝会偏好 $d_1$ 胜过 $d_2$。

双层结构中的线性序优先性，也可以推广到偏序的优先图（允许某些优先性不可比），甚至推广到无序的属性集合（Kratzer 1981; Liu 2011b）[^kratzer-1981][^liu-2011b]。

在道义逻辑中，双层结构（其中优先性建立偏好或义务序）也已广受承认，尤其是在优先处理命令的系统中（见 Hansen 2008 与 Van Benthem, Grossi, & Liu 2010 的工作）[^hansen-2008][^liu-2010]——这将在第 7 节讨论。

信念作为理由

上述从优先基定义偏好的方法，预设了关于备选物是否具备基中属性的完备信息。在信息不完备的情形中，信念扮演关键角色，行动者的偏好依赖于它们。这种情形需要引入诸如 $BC(x),$ $\neg BC(x)$ 或 $B\neg C(x)$ 的公式，其中 $C_m$ 表示优先性。这一进路使复杂面向得以纳入考量：例如判定优先基中的某些属性是否适用，或者更根本地，基于信念构造优先基。处理这类不确定性需要道信逻辑与偏好语言的结合；关于不确定性下定义偏好的多种程序，见 Liu（2011b）。在这一设定中，关于某备选物是否具备某优先性的信念，充当偏好的理由。

#### 4.2.2 显著属性与偏好

理性选择理论通常假定行动者有固定的偏好，但不解释这些偏好从何而来。Dietrich 与 List（2013a,b）开始填补这一空缺。他们提出一个建模偏好形成与改变的框架：偏好基于备选物那些“动机上显著”的属性，而非备选物本身。这一进路使偏好可以是基于理由的——随着不同属性变得显著而演化。

为形式化：行动者对备选物的偏好序，取决于这些备选物在给定状态中动机上显著的属性。

设 X 为备选物集合。设 P 为备选物可能具有的所有属性的集合。动机状态 $M \subseteq P$ 包括行动者在给定语境中认为显著的所有属性。

偏好由 X 上的二元关系 $\succeq_M$ 定义：$x \succeq_M y$ 意味着在状态 M 中备选物 x 弱优于 y。

为照顾动机状态之间的偏好差异，Dietrich 与 List（2013a,b）引入了属性组合上的权衡关系 $\geq$：

* 每个备选物 x 可以由它所具有的属性集合刻画，记作 $S_x$。
* 对任意两个属性集合，$S_x \geq S_y$ 表示 $S_x$ 中的属性优于 $S_y$ 中的属性。
* 权衡关系因此充当一个稳定的底层结构，支撑行动者在不同动机状态下的偏好排序。

形式上，若 x 与 y 是备选物，则行动者在状态 M 中的偏好 $x \succeq_M y$ 可表示如下：

$$x \succeq_M y \iff S_x \geq S_y,$$

where $S_x = \{ P \in M : x \text{ has } P \}$ and $S_y = \{ P \in M : y \text{ has } P \}$. This relation ensures that the agent’s preferences in any motivational state M reflect the agent’s stable evaluation of property combinations across contexts.

Dietrich 与 List（2013a,b）的工作通过对比两种理性来探讨理性问题：结构理性——聚焦偏好中的内在一致性（如传统经济学）——与实质理性——评估偏好内容的正当与否。形式理性要求逻辑融贯，例如若 A 优于 B 且 B 优于 C 则 A 优于 C。实质理性则认为：即便偏好一致，若其自我毁灭或有害，也应视作“非理性的”——它评估偏好自身的价值，而不只是其融贯性。对这些哲学问题的更早讨论见 Pettit（2002）。

#### 4.2.3 理由与偏好

Osherson 与 Weinstein（2012）提出一种偏好逻辑：偏好并非任意、也不仅求一致，而是基于可辨识的理由。这一框架引入模态联结词，使渴望某一结果的理由得以形式表达，从而提供一种建模方式：各种理由如何结合起来塑造行动者的偏好。

在决定是否安装火灾报警器时，一个人可能把安全与成本视为支持或反对该行动的不同理由。在此例中，安装报警器的偏好高度重视提升安全，因此这一偏好基于“安全理由”。若手头拮据，成本可能构成反对安装报警器的理由。

每条理由（如安全或成本）都可以用效用尺度来量化——它们表示依据特定标准，各选择好多少或差多少。形式上，“效用函数” u 定义为一个映射

$$u: W \times S \rightarrow \mathbb{R}$$

where W is the set of possible worlds and S indexes utility scales such as safety or cost.

为评估诸如是否安装火灾报警器的选择，模型使用“选择函数” s 来辨识与现实世界最接近的备选世界以供比较。例如它比较

* 世界 $w_1$：安装了火灾报警器（更安全的世界）；
* 世界 $w_2$：未安装火灾报警器（当前的、较不安全的世界）。

形式上，“选择函数” $s(w, A)$ 依据与当前世界 w 的相似性，从集合 A 中选出一个代表世界：

$$s(w, A) = \text{closest world in } A \text{ to } w.$$

最后，偏好关系可以用模态表达式形式定义。例如 $p \succ_1 \neg p$ 成立，当且仅当就安全理由而言，安装报警器（以 p 表示）优于不安装——以安全效用尺度 $u_1$ 表示。若还考虑 $u_2$（成本），偏好关系可以结合 $u_1$ 与 $u_2$，从而刻画兼顾安全与成本的综合视角。

这一逻辑框架支持把偏好背后的具体理由纳入结构化推理，从而对植根于现实决策语境的选择给出细致的表示。

Osherson 与 Weinstein 还探讨可判定性问题以及模型子类的各种条件。

双层结构已成为为带理由的偏好建模的标准进路，在多个领域都有潜在应用。一个晚近的例子是源自底层因果考量的偏好——见 Xie 与 Yan（2024）关于这一主题的工作。类似地，Chen、Shi 与 Wang（2024）把偏好与依赖整合进合作博弈，为纳什均衡、帕累托最优与 Shapley 核等概念提供统一视角。

## 5 偏好改变的动态学

偏好可以因各种触发因素而改变，这使偏好改变成为值得考虑的自然现象。逻辑建模因此被提议为研究这些动态之推理的方式。本节部分遵循 Lang 与 Van der Torre（2008）对偏好改变的分类——以驱动改变的输入类型为据。此外，本节着重双层结构中可能发生的动态改变。Grüne-Yanoff 与 Hansson（2009）讨论了偏好改变为何在社会科学（尤其是经济学）中遭到忽视；其文集给出研究偏好改变的多种进路（另见偏好词条中关于偏好改变的一节）。本节考察逻辑传统中的主要思想与形式框架。

### 5.1 内在偏好修正

第一类偏好改变类似于信念改变：正如信念修正在既有信念状态中纳入新获信念，内在偏好修正在既有偏好状态中纳入新偏好。这里，偏好被其他偏好修正而形成新偏好，信念不介入。

建模偏好改变主要有两种方法：Alchourrón、Gärdenfors 与 Makinson（AGM）的公设化框架（见信念修正逻辑词条中对 AGM 信念修正理论的描述）与基于动态逻辑的系统（见动态认知逻辑词条）。研究者广泛采用二者来探索偏好改变的各种形式。

Sven Ove Hansson（1995）对偏好改变作了细致分析，在 AGM 框架内辨识出四种类型：

* **修正**：获得对 $\varphi$ 优于 $\psi$ 的偏好，伴随修正陈述“$\varphi$ 优于 $\psi$”。
* **收缩**：移除“$\varphi$ 优于 $\psi$”这一偏好。
* **添加**：向所考虑的选项集添加一个新备选物。
* **删除**：从所考虑的选项集中移除一个选项。

信念修正通过分配优先性来最小化对先前信念的改变；Hansson 则论证优先性不适合偏好修正。在偏好修正中，接纳像 $\varphi\succeq \psi$ 这样的新陈述，可能涉及调整 $\varphi$ 或 $\psi$ 任意一方的位置。他还提出一个相似性测度，使修正后的偏好模型尽可能接近原模型，并为这些算子给出 AGM 式公设。

Van Benthem 与 Liu（2007）发展了动态认知逻辑的一个扩充，用以推理偏好改变。文中引入一个“建议”算子，记作 $\sharp\varphi$。公式 $[\sharp\varphi]\psi$ 意为“在 $\varphi$ 被公开建议之后，$\psi$ 成立”，定义为：

$$(\mathcal{M}, s) \models [\sharp \varphi]\psi \quad\textrm{ iff }\quad \mathcal{M}_{\sharp \varphi}, s \models \psi$$

where $\mathcal{M}_{\sharp \varphi}$ is defined with the same domain, valuation, and actual world as $(\mathcal{M}, s)$ but with the preference relations updated by subtracting the preference links from $\varphi$-worlds to $\neg \varphi$-worlds:

$$\leq^{*} = \leq - \{(s, t) \mid \mathfrak{M}, s \models \varphi \textrm{ and } \mathfrak{M}, t \models \neg \varphi\}.$$

更一般地，在此框架中，建议 $\sharp(\varphi)$ 可以理解为命题动态逻辑（PDL）中的一个关系程序（参 Harel, Kozen, & Tiuryn 2000），即

$$(?\neg \varphi ; R) \cup (R ; ?\varphi)$$

indicating that all existing R links are retained with the exception of those links from $\varphi$-worlds to $\neg \varphi$-worlds. This setup allows for different types of preference change. For example, adding preference links (making every $\varphi$-world preferable to every $\neg \varphi$-world) can be represented as

$$R := R \cup (?\neg \varphi ; \top; ?\varphi)$$

where $\top$ denotes the universal relation. *Radical preference upgrade* is defined as

$$\Uparrow \varphi(R) := (?\varphi;R;?\varphi)\cup(?\neg \varphi; R;?\neg \varphi) \cup (?\neg \varphi;\top;?\varphi)$$

它使所有 $\varphi$-世界优于所有 $\neg \varphi$-世界，同时保留每组内部的原有序。

这一动态偏好逻辑通过支持多种关系改变算子而扩充 DEL；Van Benthem 与 Liu（2007）为这些算子给出完全性定理。其结果借助 PDL 格式——它使动态模态词的归约与归约公理的递归计算成为可能。

### 5.2 由信念更新驱动的偏好改变

第二类偏好改变应答于信念的改变，反映行动者所信与所评之间的动态互动。这一话题已获相当关注（见 Bradley 2007、Lang & Van der Torre 2008 与 Liu 2011b 的工作）[^bradley-2007][^lang-2008][^liu-2011b]。例如，遵循 Savage（1954）确立的决策论传统，Bradley 论证偏好改变可以源于信念改变——“偏好改变由信念在可能性空间某个划分上的重新分布所引发”。他以贝叶斯进路形式化这一原则。考虑 Lang 与 Van der Torre（2008）的如下例子：

> 起初，我想吃这盘里的寿司。随后我得知这寿司是用不新鲜的鱼做的。现在我不想吃这寿司了。（2008: 351）

得知寿司以不新鲜的鱼做成，这一消息改变了我的信念，进而反转初始偏好。这里，偏好改变是信念改变的结果，信念改变因此成为建模的关键要素。

AGM 框架通过建立公设处理信念修正：规定信念集应如何适应新的、可能冲突的信息。Lang 与 Van der Torre（2008）把类似进路应用于由信念更新导致的偏好改变。其提出的形式语言包括：信念的二元模态算子 $N(\alpha\mid\beta)$，意为“给定 $\beta$，$\alpha$ 是正常的（或被相信的）”；偏好算子 $P(\alpha\mid\beta)$，意为“给定 $\beta$，$\alpha$ 是更偏好的”；以及动态算子 $[*\alpha]\beta$，读作“在习得 $\alpha$ 后，$\beta$ 成立”。为刻画偏好改变的性质，他们提出八条公设。两条例子如下：

$$\tag{P1} P\alpha \rightarrow [*\alpha]P\alpha $$

（P1）意味着：习得某物已是所偏好的，并不改变初始偏好。例如，若我渴望财富，那么在变得富有时，这一偏好仍保持。这种持续性通常显得自然，但也有争议：例如在 Jeffrey 的决策论中，一旦你变得富有，变富的欲望可能就不再适用。

$$\tag{P5} P\alpha \land N\beta \rightarrow [*\beta]P\alpha$$

(P5) implies that learning that something that was expected is actually the case should not alter existing preferences. This principle, equivalently stated as $P\alpha \land \neg[*\beta]P\alpha \rightarrow \neg N\beta$, expresses that unexpected information is necessary for preference change to occur.

总之，信念更新驱动偏好改变，这表明二者的紧密关系。AGM 理论与动态逻辑系统等框架为建模这一演化提供了工具。

### 5.3 偏好改变的双层模型

在双层结构中，优先基可以随诸因素相对重要性的变化而移动，自然导致相应的偏好改变。De Jongh 与 Liu（2009）考察线性优先基与偏好之间的互动，展示优先性移动如何影响偏好关系。在相关语境中，Andréka、Ryan 与 Schobbens（2002）在更一般的非线性图结构中探索从各种优先序导出偏好的方法。沿这些思路，Girard（2008）与 Liu（2011a）引入基本的图更新操作，为分析优先结构的改变提供形式框架。Christoff、Gratzl 与 Roy（2021）研究标记相继演算中优先合并的证明论。

#### 5.3.1 图更新：基本操作

设有一个优先基，记作 $\mathscr{B}$，它是一组带优先性的命题。当新命题 A 加入时，有几种直接的纳入方式：

* 给 A 最高优先性：可把 A 放在优先基顶部，使之成为最重要的命题。
* 给 A 最低优先性：可把 A 加在底部，使之优先性最低。
* **并列**：可把 A 与 $\mathscr{B}$ 并置，不在 A 与其他优先性之间建立次序。

The set $\alpha(\mathscr{B}, A)$ of basic graph updates is defined in a way that allows these possible changes to be captured:

$$\alpha(\mathscr{B}, A) := A \mid \mathscr{B}_1 ; \mathscr{B}_2 \mid \mathscr{B}_1 \parallel \mathscr{B}_2.$$

Here, $\mathscr{B}_1 ; \mathscr{B}_2$ represents the sequential composition of adding $\mathscr{B}_1$ on top of $\mathscr{B}_2$ so that every element in $\mathscr{B}_1$ has a higher priority than every element in $\mathscr{B}_2$. Parallel composition, ($\mathscr{B}_1 \parallel \mathscr{B}_2$), combines $\mathscr{B}_1$ and $\mathscr{B}_2$ as disjoint sets with no priority ordering between them.

优先基不仅可通过插入新命题来修改，还可通过删除操作移除优先性。例如，顶部删除会把优先基中不被其他项“支配”的项移除，即具有最高优先级的项。

这些基本图更新为重构给定优先基提供了简便方式——添加或删除命题。

#### 5.3.2 追踪动态学

为追踪不同层面——世界层与优先层——的变化，我们定义一个专门的技术性概念。给定优先更新 $\alpha: (\mathscr{B}, A) \rightarrow \mathscr{B'}$ 与世界层映射 $\sigma: (\preceq, A) \rightarrow \preceq'$，则称 $\alpha$ 诱导 $\sigma$，若：

$$\sigma(\preceq_{\mathscr{B}}, A) = \preceq_{\alpha(\mathscr{B}, A).}$$

若一个操作 $\alpha$ 借助语言中公式的测试、弱与强基本偏好关系 R、以及全称关系，并允许任意并集与顺序复合，而诱导出一个 *PDL*-可定义的关系变换器 $\sigma$，则称 $\alpha$ 为 *PDL*-可定义操作：

\pi:=?\varphi \mid R\mid R^{<} \mid \top\mid ;\mid \cup.$$

它们被解释为标准的 *PDL* 程序操作：测试 $?\varphi$、顺序复合 $“;”$ 与选择 $“\cup”$。

在双层框架中，有趣的是看优先动态如何映射偏好动态。例如，可以通过改变世界层的偏好关系，也可以通过修改优先基，来实现由“建议”算子引起的偏好改变。若新命题 A 以并列方式加入既有基 $\mathscr{B}$，偏好关系便被更新——如下面的交换图所示：

图 A：

![a commuting diagram: link to extended description below](../assets/logic-preference/figxy1.svg)

图 A：交换图，其中新命题 A 以并列方式加入既有基［图 A 的扩展描述见补充材料。]

同样，把新命题 A 置于优先图 $(\mathscr{B}, <)$ 顶部，与世界层的激进更新相呼应：

图 B

![a diagram: link to extended description below](../assets/logic-preference/figxy2.svg)

图 B：交换图，其中新命题 A 被置于优先图顶部［图 B 的扩展描述见补充材料。]

这些例子展示了优先层变换与世界层关系更新无缝对应的情况。

虽然优先动态与偏好动态常常一致，但也有界限。例如，删除操作 $\textit{del}(\mathscr{B})$ 不是 *PDL*-可定义的（Liu 2011a）[^liu-2011a]。某些自然的优先层修改无法在世界层完全表示。

#### 5.3.3 双层结构中信念驱动的偏好改变

在双层结构中，考虑由信念更新驱动的偏好改变也有意义。在 De Jongh 与 Liu（2009）的框架中，人们采用多种策略从优先性与信念导出偏好，如下例所示：

> 爱丽丝正在找公寓。她认为价格比社区更重要。她相信公寓 $d_1$ 价格低但社区不好。她对公寓 $d_2$ 的价格没有任何信息，但相信它社区好。

在涉及不确定性的情形中，“决策策略”通过比较各选项（据信）满足的最重要标准来比较两个选项。在此语境中，基于其信念，爱丽丝会偏好 $d_1$ 胜过 $d_2$。

然而，如果她的信念改变（例如她得知 $d_2$ 价格低），她的偏好可能随之移动，转而偏好 $d_2$ 胜过 $d_1$。这凸显了两种偏好改变之间的区别：其一是信念更新所引发，其二是优先性移动所引发——如前面的例子所示。

总之，优先动态与偏好动态虽密切相关，却各有独特之处；总之，优先动态与偏好动态虽密切相关，却各有独特之处；这表明：为全面理解行动者如何决策，宜同时建模内在偏好与基于理由的偏好。

## 6 其余条件相同的偏好与 CP 网

其余条件相同的偏好（*ceteris paribus* preference）是在“其余一切相同”的条件下表达偏好的方式。它使行动者得以宣称一个选项优于另一个，同时假定所有其他相关因素保持不变。在作决策的 AI 系统中，CP 网是一种表示条件偏好的图形模型。它依赖如下原则：各选项间的比较，以其他因素不变为假定——与其余条件相同的概念紧密契合。

本节介绍其余条件相同偏好逻辑的结果，以及 CP 网的基础。

### 6.1 在逻辑中形式化其余条件相同的偏好

其余条件相同偏好的核心问题，是如何解释“其余一切相同”。例如，某人一般偏好红酒胜过白酒——其余条件相同——但若红酒有毒而白酒无毒则不然。因此，形式化其余条件相同限制条件的挑战在于：如何判定除了酒的颜色之外各项条件相同。Halldén（1957）与 von Wright（1963）在偏好逻辑的最早研究中就讨论过这一问题。其余条件相同的等同解读与正常性解读（“其余一切正常”）之别，Van Benthem、Girard 与 Roy（2009）也有讨论。

解释“其余一切相同”这一短语时，一个自然的做法是使用世界的等价类。该领域的许多研究者都采取了这一进路。例如，Doyle 与 Wellman（1994）为个体定义了依赖语境的等价关系，称为语境等价。由此，等价类可以随所考虑的语境而变化。

Formally, let $\Omega$ be a set of states, and let $\mathcal{E}(\Omega)$ denote the set of all equivalence relations on $\Omega$. The contextual equivalence is defined on a set $\Omega$ as a function $\eta$: $\mathcal{P}(\mathcal{P}(\Omega))\rightarrow\mathcal{E} (\Omega)$ assigning to each set of proposition $\{p, q, \ldots\}$ an equivalence relation $\eta(p, q, \ldots)$. For $w\,\eta(p,q,\ldots)\, w^{\prime}$ , we write $w\approx_{ mod\, p,q,\ldots} w^{\prime}$, meaning that with regard to $p, q, \ldots$, it is the case that w and $w^{\prime}$ are the same. Doyle and Wellman (1994) thus proposed dividing the space of possibilities into equivalence classes and ignoring comparison links that go across these classes.

Van Benthem、Girard 与 Roy（2009）把这一想法应用于可能世界之间的等价关系：对某个特定集合中所有相关模态公式的真值等价。此外，他们展示这一概念如何与 von Wright 的工作相衔接，以及它如何应用于博弈论解概念。他们向语言引入形如 $\langle \Gamma \rangle\varphi$ 的新模态词，形式定义如下：

$$p\mid \neg \varphi\mid \varphi\land \psi \mid\langle \Gamma \rangle^{>}\varphi\mid \langle \Gamma \rangle^{\geq}\varphi\mid \langle \Gamma \rangle\varphi,$$

where $\Gamma$ is an arbitrary set of formulas. This way, “being equal” is part of the formal language itself. Semantically, $\Gamma$ defines an equivalence class of possible worlds. For instance, $w \approx_{\Gamma} v$ indicates that w and v are equal w.r.t. $\Gamma$—they satisfy the same formulas in $\Gamma$.

其余条件相同的偏好模型是四元组 $\mathcal{M}$= $(W, \succeq, \trianglerighteq_{\Gamma}, V)$，其中：

* W 是状态集合，$\succeq$ 是二元偏好关系，V 是赋值
* $\trianglerighteq_{\Gamma}$ 是由 $w\trianglerighteq_{\Gamma}v$ 当且仅当 $w\succeq v$ 且 $w \approx_{\Gamma} v$ 给出的二元关系
* 严格子关系 $\trianglerighteq_{\Gamma}$ 由 $w\succ v$ 且 $w \approx_{\Gamma} v$ 定义

关系 $\trianglerighteq_{\Gamma}$ 实质上是两个世界间关系的交：基本偏好关系，与对 $\Gamma$ 中公式的真值等价。涉及等价类的新公式的真值条件是：

* $\mathcal{M}, w \models \langle \Gamma \rangle^{\geq}\varphi$  iff   $\exists v$ s.t. $v \trianglerighteq_{\Gamma} w$ and $\mathcal{M}, v\models \varphi$
* $\mathcal{M}, w \models \langle \Gamma \rangle^{>}\varphi$  iff   $\exists v$ s.t. $v \vartriangleright_{\Gamma} w$ and $\mathcal{M}, v\models \varphi$
* $\mathcal{M}, w \models \langle \Gamma \rangle\varphi$  iff   $\exists v$ s.t. $v \approx_{\Gamma} w$ and $\mathcal{M}, v\models \varphi$

对 $\Gamma$ 有穷的情形，Van Benthem、Girard 与 Roy（2009）给出完全公理化。针对其余条件相同的特征，新公理集见图 8。

*Figure 8:*

Reflexivity axioms for ceteris paribus sets where $\varphi\in\Gamma$:

1. $\langle \Gamma \rangle\varphi\rightarrow\varphi$
2. $\langle \Gamma \rangle\neg \varphi\rightarrow\neg\varphi$

Monotonicity axioms for ceteris paribus sets where $\Gamma \subseteq\Gamma^{\prime}$

1. $\langle \Gamma^{\prime} \rangle\varphi\rightarrow\langle \Gamma \rangle\varphi$
2. $\langle \Gamma^{\prime} \rangle^{\geq}\varphi\rightarrow\langle \Gamma \rangle\varphi$
3. $\langle \Gamma^{\prime} \rangle^{>}\varphi\rightarrow\langle \Gamma \rangle\varphi$

Axioms characterizing the changes to the ceteris paribus sets:

1. $\pm\varphi\land \langle \Gamma \rangle(\alpha\land \pm \varphi)\rightarrow\langle \Gamma \cup\{\varphi\} \rangle\alpha$
2. $\pm\varphi\land \langle \Gamma \rangle^{\geq}(\alpha\land \pm \varphi)\rightarrow\langle \Gamma \cup\{\varphi\} \rangle^{\geq}\alpha$
3. $\pm\varphi\land \langle \Gamma \rangle^{>}(\alpha\land \pm \varphi)\rightarrow\langle \Gamma \cup\{\varphi\} \rangle^{>}\alpha$

图 8：Van Benthem、Girard 与 Roy（2009）对其余条件相同偏好的公理化

在完全语言中，模态词 $\langle\Gamma\rangle\varphi$ 中的 $\Gamma$ 可以任意大。Seligman 与 Girard（2011）的后续工作给出了完全逻辑一部分——即所谓“灵活”有效式之集——的公理化，并提供另一种语义：其中所有有效式都是灵活的，因而得到完全公理化。无限任意集的公理化仍是未决问题。

### 6.2 其余条件相同的偏好的计算模型

CP 网（“条件偏好网络”的缩写）实质上体现其余条件相同的概念——它是这些网络表示偏好的核心原则。本节介绍 CP 网的基础，突出其在其余条件相同假定（其余一切相同）下表示行动者偏好的紧凑、直观且结构化的方式。

条件偏好网络（CP 网）是一个图形模型，定义如下。

设 $V = \{X_1, X_2, \ldots, X_n\}$ 为变量集合，每个 $X_i$ 有一个可能值的有穷域 $\text{Dom}(X_i)$。有一个有向图 G，其中：

* 每个变量 $X_i$ 对应一个节点。
* $X_i$ 的父节点记作 $\text{Pa}(X_i)$，即有边指向 $X_i$ 的节点。这些父节点表示影响 $X_i$ 之偏好的变量。从 $X_i$ 到 $X_j$ 的边意味着：对 $X_j$ 的偏好依赖于 $X_i$ 的值。

CP 网不列举所有可能结果的偏好（其数量随变量数指数增长），而使用条件偏好表（CPT）只捕捉相关依赖（即偏好所依赖的要素）。每个节点 $X_i$ 配有一张 CPT：对 $\text{Pa}(X_i)$ 的每个可能实例化 u，它规定 $\text{Dom}(X_i)$ 上的一个全序 $\succ_{u}$。例如：

> 若 $\text{Pa}(X_i) = \{A, B\},$ 则 $X_i$ 的 CPT 规定 A 与 B 的所有组合下的偏好。

CP 网的语义描述：如何基于各网络的结构与条件偏好表导出结果上的偏好。

结果（outcome）是对 CP 网中所有变量的一个完全赋值。例如，若 $V = \{X_1, X_2, X_3\}$ 且各域为

$$\text{Dom}(X_1) = \{a_1, a_2\}, \quad \text{Dom}(X_2) = \{b_1, b_2\}, \quad \text{Dom}(X_3) = \{c_1, c_2\},$$

then one outcome would be $o = \{X_1 = a_1, X_2 = b_2, X_3 = c_1\}$.

遵循其余条件相同的假定——即在保持所有其他变量不变的情况下比较结果——如果我们尊重每个变量的 CPT 中规定的条件偏好，就可以得到结果上的偏好。

例如，若 $X_2$ 的 CPT 规定在 $X_1 = a_1$ 时 $b_1 \succ b_2$，则：

$$\begin{align*} \text{if } &o_1 = \{X_1 = a_1, X_2 = b_1, X_3 = c_1\} \text{ and }\\ &o_2 = \{X_1 = a_1, X_2 = b_2, X_3 = c_1\}, \text{then } o_1 \succ o_2.\\ \end{align*}$$

可以设计算法在 CP 网中高效地找到最优结果——见 Boutilier、Brafman 等人（2004）、Wilson（2004）与 Goldsmith、Lang 等人（2008）的工作。

通过只捕捉相关的条件偏好，CP 网避免了枚举所有可能结果之偏好所导致的组合爆炸。CP 网在 AI 驱动的决策中已显示重要价值，应用于推荐系统与产品配置等领域。它在计算机科学与人工智能领域吸引了大量关注，如 Allen（2015）与 Cai、Zhan、Jiang（2023）等较近期的工作所示。

## 7 各研究领域中的偏好

### 7.1 偏好与条件逻辑

众所周知，自 1960 年代末与 1970 年代初以来，偏好逻辑 $p\geq^{\forall\exists}q$ 与条件逻辑之间存在紧密关系（Lewis 1973）[^lewis-1973]：其中一些可以相互定义。

例如，若我偏好鱼胜过肉，偏好肉胜过素食，而我在一家只供应牛排或沙拉的牛排馆，那么在此语境中，我偏好牛排。这类关于偏好与事实的推理，把偏好推理与条件推理联系起来。

在可能世界语义中，可以这样解释：条件逻辑的模型也是偏好结构。然而，这些偏好逻辑是 1960 年代末与 1970 年代初作为条件逻辑与道义逻辑的对应物发展起来的，与 Halldén 和 von Wright 在此前十年发展的偏好逻辑相当不同。

若以 $\varphi\Rightarrow \psi$ 表示条件句“若 $\varphi$ 则 $\psi$”，则在适当条件下可定义：$\varphi$ 优于 $\psi$，当 $\varphi\lor \psi$ 蕴涵 $\varphi$ 而不蕴涵 $\psi$：

$$\varphi\geq^{\forall\exists} \psi :=\neg ((\varphi\lor \psi)\Rightarrow \neg \varphi).$$

于是我们也有：条件句“若 $\varphi$ 则 $\psi$”定义为 $\varphi\land \psi$ 优于 $\varphi\land \neg \psi$：

$$\varphi\Rightarrow \psi := (\psi\land \varphi)>^{\forall\exists}(\neg \psi\land \varphi).$$

条件逻辑更为流行，因为条件句在自然语言中频繁出现。可以说，某些偏好逻辑在文献中以条件逻辑之名为人所知，另一些则以道义逻辑之名。但由此结果不能推出偏好逻辑与条件逻辑是同一回事。一般而言，条件句与比较级之间的关系只有部分被理解（Makinson 1993）[^makinson-1993]。

### 7.2 偏好与道义逻辑

传统道义逻辑常用可能世界语义解释义务与许可等概念：世界由一个偏好关系排序，按理想程度分级。道义公式在当前世界的语境中评估，依据其对理想世界的可及性：一个行动是义务性的，如果它出现在从当前世界可及的所有最受偏好世界中。较好世界与最好世界之间的复杂关系，Parent（2014）与 Grossi、Van der Hoek、Kuijer（2022）作了大量考察。这一排序反映直观的道义原理，但难以处理冲突与两难，因为单一排序可能无法完全刻画多个可能不相容的命令。

Makinson（1999）强调两类东西的区分：规范（无真值的命令）与道义命题（关于义务或许可、可真可假的陈述）。他指出这一区分在当代道义逻辑中被忽视，并呼吁把道义逻辑“重构”为一个以明确命令而非抽象真值条件为基础的系统。在其 2012 年的书中，Horty 贡献显著：他提出一个理解行动背后理由的框架，以缺省逻辑为基本结构。他阐明多种理由如何互动——支持、压倒或相互冲突——以决定个体应当做什么。

这些对理由的关注，促成道义逻辑中以命令为本的语义：它相对于明确的命令集合定义道义算子。标准道义系统（如一元与二元系统）被改造以适配这一模型，并扩展以处理命令间的优先性冲突与两难。道义逻辑也采纳了双层结构。值得注意的工作包括 Hansen（2008, 2014）；Van Benthem、Grossi 与 Liu（2014）；以及 Benzmüller、Parent 与 Van der Torre（2020）。

### 7.3 决策论与博弈论中的偏好

在决策论与博弈论中，“偏好”与“偏好关系”被用来建模选择，常带行为解释。偏好关系的形式性质及其经由效用函数的表示，已在文献中得到广泛研究，其中一些甚至早于偏好逻辑。本词条主要强调偏好的定性进路——聚焦偏好关系的形式性质。与之相对，定量进路通常依赖效用函数以数值方式表示偏好。不确定性下的决策常用期望值框架建模：它把行动者的信念（表示为概率）与效用结合以刻画偏好。批判性研究重新审视了偏好理论的基础。例如，Hausman（2012）区分了作为选择、福祉与价值的偏好概念，提出效用函数能否充分刻画福祉的问题——尤其当定性因素塑造个体偏好时。Fu（2020）提出一种融合定性与定量方法的新进路，以更准确地反映现实决策的复杂性。要把本词条与决策论连接起来，关键在于：为第 4 节那种更丰富的双层结构所导出的基于理由偏好，给出数值化定量表示。

### 7.4 社会选择理论中的偏好

在社会选择理论中，核心问题是如何把个体偏好聚合成一个融贯的群体偏好。这一领域的一个著名结果是 Arrow（1951）的不可能性定理：它表明构造一个满足某些合意条件的公平聚合规则有其限度。后续研究探索替代假定，得出新结果。例如，Andréka、Ryan 与 Schobbens（2002）用图表示选项的替代排序，作为聚合个体偏好的一种方法。List（2022）（社会选择理论词条）对这一主题给出有用综述。在社会环境中，个体偏好常常并非完全独立，而是受同伴看法的影响。作为共同体，值得思考的是：社会偏好如何随时间演化，以及能否出现稳定的偏好。Seligman、Liu 与 Girard（2011）以及 Liang 与 Seligman（2011）讨论了这一主题的逻辑研究。这一领域需要探索共同体结构、更新个体偏好的机制，以及定义社会偏好的方法。相关洞见也可得自社会信念方面的工作，如 Shi（2021）。演化博弈论中也研究类似问题，尤其是社会偏好的所谓“间接演化进路”。例如，Bowles 与 Gintis（2011）探讨利他、公平与合作等亲社会偏好如何演化并达到稳定。

## 8 结论

偏好逻辑为理解行动者如何比较情形并作决策提供了一个多用途框架。本词条评述了这一领域的关键发展，追溯其从语法与算法进路到语义框架的演化。它还突出双层结构的近期研究——后者源自内在偏好与外在偏好的区分，强调理由在塑造偏好中的作用。

偏好改变的研究与其余条件相同之偏好概念，凸显了偏好逻辑的动态性与实用性，尤其在决策语境中。这些框架仍将是应对未来挑战、推进该领域研究的基础。

## References（引用注释）

**以下文献从原文照录，不作翻译；中国文献译为中文。**

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

[^allen-2015]: Allen, Thomas E., 2015, “CP-Nets: From Theory to Practice”, in *Algorithmic Decision Theory* (Lecture Notes in Computer Science 9346), Toby Walsh (ed.), Cham: Springer, 555–560.
[^andréka-2002]: Andréka, Hajnal, Michael Ryan, and Philippe-Yves Schobbens, 2002, “Operators and Laws for Combining Preferential Relations”, *Journal of Logic and Computation*, 12(1): 13–53. doi:10.1093/logcom/12.1.13
[^arrow-1951]: Arrow, Kenneth J., 1951, *Social Choice and Individual Values* (Yale University. Cowles Foundation for Research in Economics 12), New York: John Wiley & Sons.
[^benzmüller-2020]: Benzmüller, Christoph, Xavier Parent, and Leendert W. N. van der Torre, 2020, “Designing Normative Theories for Ethical and Legal Reasoning: LogiKEy Framework, Methodology, and Tool Support”, *Artificial Intelligence*, 287: 103348. doi:10.1016/J.ARTINT.2020.103348
[^boutilier-1990]: Boutilier, Craig, 1990, “Conditional Logics of Normality as Modal Systems”, in *Proceedings of the Eighth National Conference on Artificial Intelligence (AAAI’90)*, volume 1, Menlo Park, CA: AAAI Press, 594–599.
[^boutilier-1992]: –––, 1992, *Toward a Logic for Qualitative Decision Theory*, Ph.D. thesis, University of Toronto.
[^boutilier-2004]: Boutilier, Craig, Ronen I. Brafman, Carmel Domshlak, Holger H. Hoos, and David Poole, 2004, “CP-Nets: A Tool for Representing and Reasoning with Conditional Ceteris Paribus Preference Statements”, *Journal of Artificial Intelligence Research*, 21: 135–191. doi:10.1613/jair.1234
[^bowles-2011]: Bowles, Samuel and Herbert Gintis, 2011, *A Cooperative Species: Human Reciprocity and Its Evolution*, Princeton/Oxford: Princeton University Press.
[^bradley-2007]: Bradley, Richard, 2007, “The Kinematics of Belief and Desire”, *Synthese*, 156(3): 513–535. doi:10.1007/s11229-006-9136-7
[^cai-2023]: Cai, Jianlong, Jieyu Zhan, and Yuncheng Jiang, 2023, “CP-Nets-Based User Preference Learning in Automated Negotiation through Completion and Correction”, *Knowledge and Information Systems*, 65(9): 3567–3590. doi:10.1007/s10115-023-01872-z
[^chen-2024]: Chen, Qian, Chenwei Shi, and Yiyan Wang, 2024, “Reasoning about Dependence, Preference and Coalitional Power”, *Journal of Philosophical Logic*, 53(1): 99–130. doi:10.1007/s10992-023-09727-2
[^chisholm-1966]: Chisholm, Roderick M. and Ernest Sosa, 1966, “On the Logic of ‘Intrinsically Better’”, *American Philosophical Quarterly*, 3(3): 244–249.
[^christoff-2022]: Christoff, Zoé, Norbert Gratzl, and Olivier Roy, 2022, “Priority Merge and Intersection Modalities”, *The Review of Symbolic Logic*, 15(1): 165–196. doi:10.1017/s1755020321000058
[^de-2009]: De Jongh, Dick and Fenrong Liu, 2009, “Preference, Priorities and Belief”, in Grüne-Yanoff and Hansson 2009: 85–107. doi:10.1007/978-90-481-2593-7_4
[^dietrich-2013a]: Dietrich, Franz and Christian List, 2013a, “A Reason-Based Theory of Rational Choice”, *Noûs*, 47(1): 104–134. doi:10.1111/j.1468-0068.2011.00840.x [[Dietrich and List 2013a preprint available online](https://eprints.lse.ac.uk/46930/)]
[^dietrich-2013b]: –––, 2013b, “Where Do Preferences Come From?”, *International Journal of Game Theory*, 42(3): 613–637. doi:10.1007/s00182-012-0333-y
[^doyle-1994]: Doyle, Jon and Michael P. Wellman, 1994, “Representing Preferences as *Ceteris Paribus* Comparatives”, in *Papers from the 1994 AAAI Spring Symposium: Decision-Theoretic Planning* (AAAI Technical Report, SS-94-06), Association for the Advancement of Artificial Intelligence, 69–75.
[^fu-2020]: Fu, Xiaoxuan, 2020, “Preference Lifting under Uncertainty”, Ph.D. thesis, Department of Philosophy, Tsinghua University.
[^girard-2008]: Girard, Patrick, 2008, *Modal Logics for Belief and Preference Change*, Ph.D. thesis, Stanford University.
[^goldsmith-2008]: Goldsmith, Judy, Jérôme Lang, Miroslaw Truszczynski, and Nic Wilson, 2008, “The Computational Complexity of Dominance and Consistency in CP-Nets”, *Journal of Artificial Intelligence Research*, 33: 403–432. doi:10.1613/JAIR.2627
[^grossi-2022]: Grossi, Davide, Wiebe van der Hoek, and Louwe B. Kuijer, 2022, “Reasoning about General Preference Relations”, *Artificial Intelligence*, 313: 103793. doi:10.1016/j.artint.2022.103793
[^grüne-yanoff-2009]: Grüne-Yanoff, Till and Sven Ove Hansson (eds), 2009, *Preference Change: Approaches from Philosophy, Economics and Psychology* (Theory and Decision Library. Series A, Philosophy and Methodology of the Social Sciences, 42), Dordrecht/London: Springer. doi:10.1007/978-90-481-2593-7
[^halldén-1957]: Halldén, Sören, 1957, *On the Logic of “Better”* (Library of Theoria 2), Lund: C.W.K. Gleerup.
[^halpern-1997]: Halpern, Joseph Y., 1997, “Defining Relative Likelihood in Partially-Ordered Preferential Structures”, *Journal of Artificial Intelligence Research*, 7: 1–24. doi:10.1613/jair.391
[^hansen-2008]: Hansen, Jörg, 2008, *Imperatives and Deontic Logic*, Ph.D. dissertation, Konstanz, Germany: University of Konstanz.
[^hansen-2014]: –––, 2014, “Reasoning about Permission and Obligation”, in *David Makinson on Classical Methods for Non-Classical Problems* (Outstanding Contributions to Logic 5), Sven Ove Hansson and David Makinson (eds), Dordrecht: Springer, 255–280. doi:10.1007/978-94-007-7759-0_14
[^hansson-1969]: Hansson, Bengt, 1969, “An Analysis of Some Deontic Logics”, *Noûs*, 3(4): 373–398. doi:10.2307/2214372
[^hansson-1995]: Hansson, Sven Ove, 1995, “Changes in Preference”, *Theory and Decision*, 38(1): 1–28. doi:10.1007/bf01083166
[^hansson-2001]: –––, 2001, “Preference Logic”, in *Handbook of Philosophical Logic*, Dov M. Gabbay and Franz Guenthner (eds), second edition, Dordrecht: Kluwer, 319–393. doi:10.1007/978-94-017-0456-4_4
[^harel-2000]: Harel, David, Dexter Kozen, and Jerzy Tiuryn, 2000, *Dynamic Logic*, Cambridge, MA: MIT Press. doi:10.7551/mitpress/2516.001.0001
[^hausman-2012]: Hausman, Daniel M., 2012, *Preference, Value, Choice, and Welfare*, Cambridge/New York: Cambridge University Press. doi:10.1017/cbo9781139058537
[^horty-2012]: Horty, John Francis, 2012, *Reasons as Defaults*, Oxford/New York: Oxford University Press. doi:10.1093/acprof:oso/9780199744077.001.0001
[^kratzer-1981]: Kratzer, Angelika, 1981, “Partition and Revision: The Semantics of Counterfactuals”, *Journal of Philosophical Logic*, 10(2): 201–216. doi:10.1007/bf00248849
[^lamarre-1991]: Lamarre, Philippe, 1991, “S4 as the Conditional Logic of Nonmonotonicity”, in *Proceedings of the Second International Conference on Principles of Knowledge Representation and Reasoning (KR’91)*, James F. Allen, Richard Fikes, and Erik Sandewall (eds), San Francisco, CA: Morgan Kaufmann, 357–367.
[^lang-2008]: Lang, Jérôme and Leendert van der Torre, 2008, “From Belief Change to Preference Change”, in *Proceedings of the 18th European Conference on Artificial Intelligence (ECAI-2008)* (Frontiers in Artificial Intelligence and Applications 178), Malik Ghallab, Constantine D. Spyropoulos, Nikos Fakotakis, Nikos Avouris (eds), IOS Press, 351–355. doi:10.3233/978-1-58603-891-5-351
[^lewis-1973]: Lewis, David, 1973, *Counterfactuals*, Oxford: Basil Blackwell.
[^liang-2011]: Liang Zhen and Jeremy Seligman, 2011, “A Logical Model of the Dynamics of Peer Pressure”, *Electronic Notes in Theoretical Computer Science*, 278: 275–288. doi:10.1016/j.entcs.2011.10.021
[^list-2022]: List, Christian, 2022, “Social Choice Theory”, in *The Stanford Encyclopedia of Philosophy* (Winter 2022), Edward N. Zalta and Uri Nodelman (eds), URL = <[https://plato.stanford.edu/archives/win2022/entries/social-choice/](https://plato.stanford.edu/archives/win2022/entries/social-choice/)>. First published 2013.
[^liu-2008]: Liu, Fenrong, 2008, *Changing for the Better: Preference Dynamics and Agent Diversity*, Ph.D. thesis, ILLC, University of Amsterdam.
[^liu-2010]: –––, 2010, “Von Wright’s ‘The Logic of Preference’ Revisited”, *Synthese*, 175(1): 69–88. doi:10.1007/s11229-009-9530-z
[^liu-2011a]: –––, 2011a, “A Two-Level Perspective on Preference”, *Journal of Philosophical Logic*, 40(3): 421–439. doi:10.1007/s10992-010-9168-9
[^liu-2011b]: –––, 2011b, *Reasoning about Preference Dynamics* (Synthese Library 354), Berlin: Springerd. doi:10.1007/978-94-007-1344-4
[^makinson-1993]: Makinson David, 1993, “Five Faces of Minimality”, *Studia Logica*, 52(3): 339–379, doi:10.1007/bf01057652
[^makinson-1999]: –––, 1999, “On a Fundamental Problem of Deontic Logic”, in *Norms, Logics and Information Systems. New Studies on Deontic Logic and Computer Science*, Paul McNamara and Henry Prakken (eds), Amsterdam: IOS Press, 29–53.
[^menger-1939]: Menger, Karl, 1939, “A Logic of the Doubtful. On Optative and Imperative Logic”, *Reports of a Mathematical Colloquium*, Notre Dame, IN, series 2, 1: 53–64.
[^osherson-2012]: Osherson, Daniel and Scott Weinstein, 2012, “Preference Based on Reasons”, *The Review of Symbolic Logic*, 5(1): 122–147. doi:10.1017/s1755020311000244
[^parent-2014]: Parent, Xavier, 2014, “Maximality vs. Optimality in Dyadic Deontic Logic”, *Journal of Philosophical Logic*, 43(6): 1101–1128. doi:10.1007/s10992-013-9308-0
[^pettit-2002]: Pettit, Philip, 2002, *Rules, Reasons, and Norms: Selected Essays*, Oxford/New York: Oxford University Press. doi:10.1093/0199251878.001.0001
[^rescher-1966]: Rescher, Nicholas, 1966, *The Logic of Commands* (Monographs in Modern Logic), London: Routledge & K. Paul.
[^rescher-1967]: –––, 1967, “Semantic Foundations for the Logic of Preference”, in *The Logic of Decision and Action*, Nicholas Rescher (ed.), Pittsburgh: University of Pittsburgh Press, 37–62.
[^savage-1954]: Savage, Leonard J., 1954, *The Foundations of Statistics* (Wiley Publications in Statistics), New York: Wiley.
[^seligman-2011]: Seligman, Jeremy and Patrick Girard, 2011, “Flexibility in Ceteris Paribus Reasoning”, *The Australasian Journal of Logic*, 10: 67–99. doi:10.26686/ajl.v10i0.1826
[^seligman-2011-2]: Seligman, Jeremy, Fenrong Liu, and Patrick Girard, 2011, “Logic in the Community”, in *Logic and Its Applications: Fourth Indian Conference (ICLA 2011)* (Lecture Notes in Computer Science 6521), Mohua Banerjee and Anil Seth (eds.), Berlin/Heidelberg: Springer, 178–188. doi:10.1007/978-3-642-18026-2_15
[^shi-2021]: Shi, Chenwei, 2021, “Collective Opinion as Tendency Towards Consensus”, *Journal of Philosophical Logic*, 50(3): 593–613. doi:10.1007/s10992-020-09579-0
[^shi-2021-2]: Shi, Chenwei and Yang Sun, 2021, “Logic of Convex Order”, *Studia Logica*, 109(5): 1019–1047. doi:10.1007/s11225-020-09940-z
[^spohn-1988]: Spohn, Wolfgang, 1988, “Ordinal Conditional Functions: A Dynamic Theory of Epistemic States”, in *Causation in Decision, Belief Change, and Statistics*, William L. Harper and Brian Skyrms (eds), Dordrecht: Kluwer, 105–134. doi:10.1007/978-94-009-2865-7_6
[^tan-1996]: Tan, Yao-Hua and Leendert W. N. van der Torre, 1996, “How to Combine Ordering and Minimizing in a Deontic Logic Based on Preferences”, in *Deontic Logic, Agency and Normative Systems: Third International Workshop on Deontic Logic in Computer Science (DEON ’96)*, Mark A. Brown and José Carmo (eds), London: Springer London, 216–232. doi:10.1007/978-1-4471-1488-8_12
[^thomason-1996]: Thomason, Richmond H. and John F. Horty, 1996, “Nondeterministic Action and Dominance: Foundations for Planning and Qualitative Decision”, in *Proceedings of the 6th Conference on Theoretical Aspects of Rationality and Knowledge (TARK ’96)*, Yoav Shoham (ed.), San Francisco, CA: Morgan Kaufmann, 229–250.
[^van-2009]: Van Benthem, Johan, Patrick Girard, and Olivier Roy, 2009, “Everything Else Being Equal: A Modal Logic for *Ceteris Paribus* Preferences”, *Journal of Philosophical Logic*, 38(1): 83–125. doi:10.1007/s10992-008-9085-3
[^van-2010]: Van Benthem, Johan, Davide Grossi, and Fenrong Liu, 2010, “Deontics = Betterness + Priority”, in *Deontic Logic in Computer Science: 10th International Conference (DEON 2010)* (Lecture Notes in Computer Science 6181), Guido Governatori and Giovanni Sartor (eds), Berlin/Heidelberg: Springer, 50–65. doi:10.1007/978-3-642-14183-6_6
[^van-2014]: –––, 2014, “Priority Structures in Deontic Logic”, *Theoria*, 80(2): 116–152. doi:10.1111/theo.12028
[^van-2007]: Van Benthem, Johan and Fenrong Liu, 2007, “Dynamic Logic of Preference Upgrade”, *Journal of Applied Non-Classical Logics*, 17(2): 157–182. doi:10.3166/jancl.17.157-182
[^van-1974]: Van Dalen, Dirk, 1974, “Variants of Rescher’s Semantics for Preference Logic and Some Completeness Theorems”, *Studia Logica*, 33(2): 163–181. doi:10.1007/BF02120492
[^van-1973]: Van Fraassen, Bas C., 1973, “Values and the Heart’s Command”, *The Journal of Philosophy*, 70(1): 5–19. doi:10.2307/2024762
[^wright-1963]: von Wright, Georg Henrik, 1963, *The Logic of Preference*, Edinburgh: Edinburgh University Press.
[^wilson-2004]: Wilson, Nic, 2004, “Extending CP-Nets with Stronger Conditional Preference Statements”, in *Proceedings of the 19th National Conference on Artificial Intelligence (AAAI’04)*, Deborah L. McGuinness and George Ferguson (eds), San Jose, CA: AAAI Press, 735–741. [[Wilson 2004 available online](https://aaai.org/papers/00735-AAAI04-116-extending-cp-nets-with-stronger-conditional-preference-statements/)]
[^xie-2024]: Xie, Kaibo and Jialiang Yan, 2024, “A Logic for Desire Based on Causal Inference”, *Journal of Logic and Computation*, 34(2): 352–371. doi:10.1093/logcom/exac060

## 学术工具

* [如何引用本词条](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=logic-preference)。
* [预览本词条的 PDF 版本](https://leibniz.stanford.edu/friends/preview/logic-preference/)，见 [SEP 学会之友](https://leibniz.stanford.edu/friends/)。
* 在 [InPhO](https://www.inphoproject.org/entity?sep=logic-preference&redirect=True) 查找与本词条相关的话题与思想家。
* 在 [PhilPapers](https://philpapers.org/sep/logic-preference/) 查看本词条的增强文献目录及其数据库链接。

## 其他网络资源

[请与作者联系提供建议。]

## 相关词条

logic: dynamic epistemic | \*模态逻辑——见逻辑学：模态逻辑 | logic: of belief revision | 偏好 | 社会选择理论

**（译注：相关词条的中文站内链接将由管线在对应词条重译完成后统一挂接。）**
