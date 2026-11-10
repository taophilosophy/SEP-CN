# 子结构逻辑 substructural (Greg Restall)

*首次发表于 2000 年 7 月 4 日；2024 年 8 月 15 日实质修订。*

**子结构逻辑** 是一类非经典逻辑，其特征在于缺少经典逻辑具备的一条或多条 **结构规则**。20 世纪下半叶，对子结构逻辑的兴趣最初从几条彼此独立的线索生长出来：哲学（相干逻辑）、语言学（Lambek 演算）与证明论的数学（线性逻辑）。1990 年代以来，这几条线索被理解为同一统一领域的不同侧面；子结构逻辑的技巧，对经典逻辑、直觉主义逻辑这类传统逻辑的研究也很有用。本文概览子结构逻辑领域；想要带定理、证明与例子的详细导论，可查阅参考文献中的书文。

## 1 结构规则

子结构逻辑是一族按 **结构规则** 刻画的逻辑系统。结构规则是不顾形式的逻辑规则——它毫不区分地施用于一切命题，不问其形式。熟悉的 **肯定前件**（由 $p\to q$ 与 $p$ 推出 $q$）不是结构规则：其第一前提必须是条件句，故它是关于条件句的规则，而非关于一切命题之推理行为的规则。三段论 *Barbara*（由 *所有 F 是 G* 与 *所有 G 是 H* 推出 *所有 F 是 H*）同样不是：它专管全称断言。肯定前件、Barbara、不矛盾律这类熟悉规则是 **运算规则**——支配或描述特定概念（条件句、全称概括、否定等）的逻辑特征。但并非一切规则都是运算规则：有些规则支配逻辑后承 **本身** 的环境行为，这就是结构规则。

**切** 规则可以这样说：若从某些前提（记作 $X$）可证结论 $A$，又从 $A$ 加另一些前提（记作 $Y$）可证 $B$，则从 $X$ 与 $Y$ 合起来可证结论 $B$。$$ \cfrac{X\vdash A\qquad Y,A\vdash B}{X,Y\vdash B} $$ 规则里出现的各判断，形式上不受任何限制：特定前提与结论完全一般，所以 **切** 是结构规则。

这里的结构规则按“能证什么”陈述；为这类规则提供动机，可以看证明怎样构成与结合。从 $X$ 加 $Y$ 到结论 $B$ 的证明，可以这样搭起来：先从 $X$ 证 $A$，再拿这个 $A$ 加 $Y$ 证 $B$。

结构规则也能借 **模型** 刻画有效性而获得动机。若论证 **有效** 是指：凡前提的模型同时也是结论的模型（不然就是 **反例**），则 **切** 规则同样得到动机。设 $X$ 每个成员的每个模型都是 $A$ 的模型，$Y$ 每个成员与 $A$ 的每个模型也是 $B$ 的模型。取一个同时满足 $X$ 与 $Y$ 全部成员的模型：既然它满足 $X$，就是 $A$ 的模型；既然又满足 $Y$，就是 $B$ 的模型。这推理全程不诉诸任何公式在模型中的真值条件：规则不受公式赋值方案的约束。只要有效性按“在模型中成立”的保持来定义，逻辑后承关系就满足 **切** 规则。

所以，无论把有效性想作关于证明还是关于模型，结构规则都是有效性的这样一类事实：与论证成分的逻辑形式无关。它们出自有效性的一般定义及其结构特征，而非支配特定联结词、量词或别的词项的规则。

尽管如此，不同逻辑系统在支配特定概念的规则上各不相同：直觉主义逻辑的否定处理与经典逻辑不同，这很有名。结构规则是解释单个概念行为不可或缺的一环——我们正是借逻辑后承的环境语境刻画概念的行为。例如条件句 $p\rightarrow q$（“若 $p$ 则 $q$”）的行为可以这样刻画：

$$ X, p \vdash q \text{ if and only if } X \vdash p \rightarrow q $$

这说：$q$ 从 $X$ 加 $p$ 可推出，当且仅当 $p \rightarrow q$ 仅从 $X$ 可推出。给定 $X$，从 $p$ 到 $q$ 的转移之有效，由 $p \rightarrow q$ 记录。刻画条件句相关有效性时，我们用的是涉及条件句 **组成部分** 的有效性陈述。

（条件句与后承的这一联系，类比数学情形，叫 **剩余化**。看加法与减法：$a + b = c$ 当且仅当 $a = c - b$。所得 $a$（即 $c - b$）是 **剩余**——从 $c$ 拿走 $b$ 剩下的东西。这条联系的另一名字是 **演绎定理**。）

$X,p\vdash q$ 与 $X\vdash p\to q$ 的剩余化等价，不是刻画条件句行为的唯一方式。有时换一种规则更有用：既描述“何时能推出含该联结词的句子”（这里从 $X,p\vdash q$ 到 $X\vdash p\to q$ 的左到右方向回答了这个问题），又描述“从含该联结词的句子能推出什么”。$p\to q$ 的剩余化条件只借诉诸 **切** 规则和假定 $p\to q\vdash p\to q$ 隐式回答后一个问题。于是可如下推理：$$ \cfrac{ \cfrac{ \begin{matrix} \\ {Y\vdash p} \end{matrix} \quad \cfrac{p\rightarrow q\vdash p\rightarrow q}{p\rightarrow q,p\vdash q} } {p\rightarrow q,Y\vdash q} \quad \begin{matrix} \\ {X,q\vdash C} \end{matrix} } {X,p\to q,Y\vdash C} $$ 所以，由两前提 $Y\vdash p$ 与 $X,q\vdash C$ 得结论 $X,p\to q,Y\vdash C$。这是条件句的一条 **左** 矢列规则：给出从作为前提的 $p\to q$ 推出结论 $C$ 的适当条件。它有时用来替代剩余化等价的右到左一半（从 $X\vdash p\to q$ 到 $X,p\vdash q$）——它同剩余化等价的左到右一半一样，用组成部分的推理行为刻画条件句的行为。

无论用剩余化规则还是条件句的左/右矢列规则，后承与条件句的联系都牵涉几个不同概念。其一是表示逻辑有效性的十字转门；其二是把后承编码进命题语言的条件句；其三是表示前提之 **结合** 的 **逗号**。我们把“$X, p \vdash q$”读作“$q$ 从 $X$ **连同** $p$ 可推出”。结合前提，就是有办法把它们 **凑到一起**。可怎么凑？结果发现凑法不止一种，各有不同的逻辑性质，于是有了带不同纯结构规则的不同子结构逻辑：前提结合的行为变了，条件句与其他联结词的行为也随之而变。本导论将看几个例子。

### 1.1 弱化

$p$ 为 **真** 是一回事，条件句 $q \rightarrow p$ 为真是另一回事。可若“$\rightarrow$”是实质条件句，$q \rightarrow p$ 便从 $p$ 推出。出于种种原因，我们可能想了解条件句在 **没有** 这种推理时如何运作；这与前提结合的行为相关，如下面的演示所示。

$$ \cfrac{p \vdash p} { \cfrac{p, q \vdash p} {p \vdash q \rightarrow p} } $$

从公理 $p \vdash p$（任何东西从 **自身** 可推出）我们推出 $p$ 从 $p$ 加 $q$ 可证，再由剩余化得 $p \vdash q \rightarrow p$。要拒斥从 $p$ 到 $q \rightarrow p$ 的推理，要么拒斥剩余化，要么拒斥证明开头的同一性公理，要么拒斥证明第一步。看最后一个选项牵涉什么，颇有启发：这里要否认 $p$ 从 $p, q$ 推出。一般地，要拒斥形如

$$ \frac{X \vdash A} {X, Y \vdash A} $$
的规则。

这就是 **弱化** 规则：从较强的陈述——$A$ 从 $X$ 可推出——走到可能较弱的一个：$A$ 从 $X$ 加 $Y$ 可推出。规则中 $X$ 的成员、$Y$、结论 $A$ 都是任意的，故它是纯 **结构** 规则。

拒斥弱化的理由随对后承与前提结合的解释而异。早期的动机之一来自对相干性的关切：若逻辑 **相干**（说 $p$ 蕴涵 $q$ 为真，至少是说 $q$ 真 **依赖** $p$），弱化就不必成立。我们确实可能有 $A$ 从 $X$ 推出，而 $A$ 不从 $X, Y$ 推出——$A$ 不必依赖 $X$ 与 $Y$ 合起来。

相干逻辑里，弱化在逗号 **另一侧** 也失效：我们也希望 **这个** 论证无效。

$$ \cfrac{q \vdash q} { \cfrac{p, q \vdash q} {p \vdash q \rightarrow q} } $$

同样，$q$ 可以从 $q$ 推出，却不意味着它从 $p$ **连同** $q$ 推出——只要“连同”取足够强的意义。所以在相干逻辑里，从任意前提到 $q \rightarrow q$ 这类逻辑真的推理多半会失效。

### 1.2 交换性

若前提结合可交换（凡从 $X, Y$ 可推出者，亦从 $Y, X$ 可推出），只用同一性公理与剩余化即可如下推理：

$$ \cfrac{p \rightarrow q \vdash p \rightarrow q} { \cfrac{p \rightarrow q, p \vdash q} { \cfrac{p, p \rightarrow q \vdash q} {p \vdash(p \rightarrow q) \rightarrow q} } } $$

前提结合不可交换时，这个证明行不通。这是前提结合行为与涉及条件句的演绎行为之间联系的又一简单例子。

许多种条件句上，这推理会失效。若条件句带 **模态** 力（表达一种蕴涵：只要在相关情形中 $p$ 成立，$q$ 便成立，$p \rightarrow q$ 就真），且“$\vdash$”表达局部后承（$p\vdash q$ 当且仅当任何模型在 $p$ 成立的任何情形中 $q$ 也成立），它就失效。Greg 是逻辑学家（$p$）可为真，Greg 是逻辑学家蕴涵 Greg 是哲学家（$p \rightarrow q$——相关情形中 Greg 是逻辑学家时他是哲学家）也可为真，但这并不 **蕴涵** Greg 是哲学家（许多情形里蕴涵式 $(p \rightarrow q)$ 真而 $q$ 不真）。所以有 $p$ 真而 $(p \rightarrow q) \rightarrow q$ 不真的情形，论证无效。

这个反例也能按前提结合的行为来理解。说 $X,A \vdash B$ 为真，并非只说 $B$ 在 $X$ 与 $A$ 都成立的任何情形中成立。要的是真正的 **蕴涵** *A $\rightarrow$ B*：$B$ 在 $A$ 为真的任何（相关）情形中为真。于是 $X,A \vdash B$ 说，在 $A$ 为真的 **任何** 可能性中 $B$ 亦真；这些可能性未必满足 $X$ 的全部（经典蕴涵理论中，可能性是 $X$ 中一切被当作 **必然** 者为真的那些）。

前提结合不可交换时，剩余化可走 **两条** 路。除给出 $\rightarrow$ 行为的剩余化条件外，还可定义新箭头 $\leftarrow$：

$$ p, q \vdash r \text{ if and only if } q \vdash r \leftarrow p $$

对左到右箭头，这个方向的肯定前件成立：

$$ p \rightarrow q, p \vdash q $$

对右到左箭头，肯定前件在前提次序相反时可证：

$$ p, q \leftarrow p \vdash q $$

这是子结构逻辑的特色：一旦注意缺少全套结构规则时会怎样，新的可能性就打开了。原先只有一个条件句（直觉主义或经典逻辑）的地方，露出了 **两个** 条件句。

下一节再举一例，说明非交换前提结合与这两个条件句的动机。

### 1.3 结合性

证明里还有一类结构假定。迄今你也许假定矢列的前提排成一个列表，且 $p,q,r$ 既可读作 $p,q$ 右侧添 $r$，也可读作 $q,r$ 左侧添 $p$。若如此，你就认为前提结构 $(p,q),r$ 与 $p,(q,r)$ 同一——前提结合（此处以逗号表示）是 **可结合的**。前提结合的结合性又是一条结构规则，同样影响推理的有效性。

为看清来由，回到 **切** 规则的表述：怎样在不对前提结合是否可结合作预判的情况下清楚陈述它？更一般的形式是：

$$ \cfrac{X\vdash A \qquad Y(A)\vdash B}{Y(X)\vdash B} $$

凡能从 $X$ 证 $A$，又能从某处含 $A$ 的假定证 $B$，则能从这些假定证 $B$——只要在那些地方把诉诸 $A$ 就地换成诉诸 $X$。这里没有对前提结合作任何隐含重排。我们外科手术般地把“诉诸 $A$”换成“诉诸当初证成 $A$ 的东西”。

类似地，条件句规则也可不靠结合性来理解：$X,p\vdash q$ 与 $X\vdash p\rightarrow q$ 等价，标志着逗号可读作 **施用**——假定 $X$ 给出条件句，当且仅当把这些假定施于前件即得后件。施用概念 **本身** 不含结合性假定。

这样理解，条件句的 **左** 规则如下：

$$ \cfrac{X(q)\vdash C\qquad Y\vdash p}{X(p\to q,Y)\vdash C} $$

这说：若在 $C$ 的某个证成中诉诸 $q$，而另有对 $p$ 的证成 $Y$，则在 $C$ 的该证成中可不直接诉诸 $q$，改诉诸施于 $Y$ 的 $p\to q$。这一表述同样小心尊重施用次序，没有隐含重排。

明白这些，就能读懂下述证明：左规则施用两次，引入 $r\to p$ 与 $p\to q$，表明 $p\to q,(r\to p,r)$ 合起来证成 $q$。要用它得出关于 $r\to q$ 的结论，得消去假定 $r$；可为此必须重排前提结合的次序。

$$ \cfrac{ \begin{matrix} \\ q\vdash q \end{matrix} \qquad \begin{matrix} p\vdash p\quad r\vdash r \\ \hline r \rightarrow p, r \vdash p \end{matrix}} { \cfrac{p \rightarrow q, (r \rightarrow p, r) \vdash q} { \cfrac{(p \rightarrow q, r \rightarrow p), r \vdash q} { \cfrac{ p \rightarrow q, r \rightarrow p \vdash r \rightarrow q } {p \rightarrow q \vdash(r \rightarrow p) \rightarrow(r \rightarrow q)} } } } $$

可见这证明诉诸前提结合的结合性，却没用到收缩与弱化。没有结合性，就别指望从 $p\to q$ 推出 $(r\to p)\to(r\to q)$ 有效。

### 1.4 收缩

最后一个重要例子是 **收缩** 规则，它规定前提怎样重复使用。从 $p \rightarrow (p \rightarrow q)$ 推出 $p \rightarrow q$ 时，收缩不可少：

$$ \cfrac{ \matrix{ \cfrac{p \rightarrow(p \rightarrow q) \vdash p \rightarrow(p \rightarrow q)} {p \rightarrow(p \rightarrow q), p \vdash p \rightarrow q} & \cfrac{p \rightarrow q \vdash p \rightarrow q} {p \rightarrow q, p \vdash q} } } { \cfrac{(p \rightarrow(p \rightarrow q), p), p \vdash q} { \cfrac{p \rightarrow(p \rightarrow q), p \vdash q} {p \rightarrow(p \rightarrow q) \vdash p \rightarrow q} } } $$

证明倒数第二步用到一条原则：某结论若靠 **两次** 施用某假定（此处 $p$）得出，则只施用 **一次** 该假定时也可证成。（注意：第三行给假定加了括号——该证明不诉诸前提结合的结合性，故可区分 $(A,B),C$ 与 $A,(B,C$。）

这些例子让人体会结构规则如何决定条件性这类概念的行为。结构规则不只影响条件句，也影响合取、析取（下文将见）与否定（Dunn 1993; Restall 2000）[^restall-2000][^dunn-1993]。

### 1.5 十字转门右侧的结构

Gentzen 的矢列演算开创性工作（Gentzen 1935）[^gentzen-1935] 表明：**经典** 与 **直觉主义** 逻辑之别，未必在于某个联结词（否定、析取、条件句）的行为。它也可以在于定义这些联结词的矢列环境结构，以及该环境满足的结构规则。Gentzen 的直觉主义矢列演算 *LJ* 用形如 $X \vdash A$ 的矢列：一簇前件、单个后件——正是我们迄今关注的矢列。其经典演算 *LK* 则用更一般的形式：

$$ X \vdash Y $$

这里矢列右侧也允许若干公式，$X$、$Y$ 都是公式汇集。预期解释：从 $X$ 的 **全部** 可推出 $Y$ 中某些；换言之，不会出现 $X$ 全成立而 $Y$ **一个不** 成立。（更多见“证明论”第 2 节、“命题逻辑”第 2.3.2 节。）

允许多后件矢列，把熟悉的联结词规则译入这一更宽语境，就能推出经典重言式。例如：

$$ \cfrac{p \vdash p} { \cfrac{p \vdash q, p} {\vdash p \rightarrow q, p} } $$

表明 $p \rightarrow q$ 与 $p$ 至少有一成立。经典逻辑中有效（$p$ 不成立则 $p$ 为 **假**，前件假的条件句为真），直觉主义逻辑中无效。类似地，直觉主义者对不矛盾律的推导可自然“对偶化”为排中律的经典证明。如下所示：$$ \cfrac{p\vdash p}{\cfrac{p,\neg p\vdash} {p\amp\neg p\vdash}} \qquad\qquad \cfrac{p\vdash p}{\cfrac{\vdash p,\neg p}{\vdash p\lor\neg p}} $$ 这样，经典与直觉主义之别，在于允许何种结构规则、分析后承时宜用何种结构，而不在某个逻辑常项的行为。

### 1.6 切与同一性

这里每条结构规则（弱化、交换、结合、收缩）本质上都涉及前提结合；就经典矢列而言，则涉及前提与 **结论** 的结合。最先见到的 **切** 规则，最简形式与前提结合无关：$$ \cfrac{A\vdash B\qquad B\vdash C}{A\vdash C} $$ 完全不涉及两侧公式的凑合。它的核心不在前提或结论怎样结合，而在两点之间：“证出某公式”（即 **切** 公式 $B$）在矢列 **右侧** 所需之物，以及拿该公式在 **左侧** 能 **做** 什么。用经济学比喻：能“付”$A$ 换 $B$、又付 $B$ 换 $C$，最初付 $A$ 就应足以得到 $C$。更抽象地说：矢列右侧的 $B$ 至少与左侧的 $B$ 同样有力——凡能从 **左** 侧的 $B$ 证出者（此处即 $C$），凡蕴涵 **右** 侧之 $B$ 者也都能证出。

还有一条结构规则值得说：**同一性** 以相反方式匹配两侧公式 $$ B\vdash B $$ 它告诉我们，左侧的 $B$ 强到足以给出右侧的 $B$。于是 **切** 与 **同一性** 涉及矢列左右两侧公式出现之间的关系，其他结构规则则支配公式在左侧或右侧 **内部** 被操作的方式。

## 2 不同的逻辑

20 世纪下半叶以至 21 世纪，一系列子结构逻辑被各自独立地发展出来，动机各不相同。

### 2.1 相干逻辑

人们自然会想，逻辑后承与相干性之间有某种联系：$X \vdash A$ 若成立，演绎的前提 $X$ 总该与结论 $A$ 有某种 **相干**。照此理解，限制前提结合就很自然：可以有 $X \vdash A$ 而没有 $X,Y \vdash A$，因为新材料 $Y$ 可能与 $A$ 的演绎不相干。这样理解的相干逻辑是 **子结构的**：相干性属于逻辑后承本身与支配后承的结构规则，而不属于任何联结词。

1950 年代，Moh（1950）、Church（1951）、Ackermann（1956）都给出过“相干”逻辑可以是什么的说明。这些想法由以 Anderson、Belnap 及其学生 Dunn、Meyer 为中心的一批研究者及众多同道发展起来。标准文献是 Anderson、Belnap、Dunn 两卷本 *Entailment*（1975、1992）；其他导论见 Read *Relevant Logic*（1988）、Dunn 与 Restall *Relevance Logic*（2000）、Mares *Relevant Logic*：*a philosophical interpretation*（2004）。

### 2.2 线性逻辑与其他无收缩逻辑

限制前提结合不止这一条路。Girard（1987）引入 **线性逻辑**，作为过程与资源使用的模型。其演绎观的想法是：资源必须被使用（前提结合满足相干性判据），且不会 **无限** 延伸，前提不可 **重复** 使用。于是可以有 $X,X \vdash A$（用 $X$ 两次得 $A$），却未必有 $X \vdash A$（单用 $X$ 一次得 $A$）。有益导论见 Troelstra *Lectures on Linear Logic*（1992）。

还有别的形式逻辑缺 **收缩规则**（从 $X,X \vdash A$ 到 $X \vdash A$），最著名的是 Łukasiewicz 多值逻辑。无收缩逻辑一直有人关注，因为收缩规则出现在说谎者悖论、Curry 悖论等语义悖论的推导里（Curry 1977, Geach 1955；另见 Field 2008、Restall 1994、Zardini 2021）[^zardini-2021][^curry-1977][^field-2008][^geach-1955]。

### 2.3 Lambek 演算

独立于上述两个传统，Joachim Lambek 考察了语言与句法的数学模型（Lambek 1958, 1961）[^lambek-1958]：前提结合对应于字符串或其他语言单位的组合。这里 $X,X$ 的内容不同于 $X$，$X,Y$ 也不同于 $Y,X$——不但所用前提的 **数目** 要紧，**次序** 也要紧。Lambek 演算（也称 **范畴语法**）的良好导论见 Moortgat（1988）、Morrill（1994）、Moot 与 Retoré（2012）。

### 2.4 ST 与 TS

迄今每条子结构逻辑都以某种方式限制前提结合，禁掉弱化、收缩或交换。另一族则保留这些，转而限制某条跨矢列规则：**切** 与 **同一性**。它们与经典逻辑的差别或极小或极大，全看拒斥哪一条。不带 **切** 的经典逻辑，在某个层面上与经典逻辑无从分别：Gentzen（1935）表明 **切** 可消除——能用切证的矢列，不用切也能证。所以就有效矢列而言，去掉切的经典逻辑子结构变体就是经典逻辑本身。

反之，若从经典逻辑的标准表述中去掉 **同一性**，结果大不相同：无同一性的经典逻辑 **没有** 任何有效矢列。推导无处开始，什么都证不出。

2000 年代以来，为处理模糊性、语义悖论等语义现象而舍弃切或同一性的逻辑，持续受到关注。Zardini（2008）《一个容忍的模型》与 van Rooij（2011）《模糊性、容忍与非传递蕴涵》，都用无切（非传递）后承关系建模满足自然容忍条件的模糊谓词——凡与某个 $F$ 足够 $F$-接近者也是 $F$。表达该容忍的条件句（及其底层后承关系）若不传递，堆垛悖论便在某意义上被避开。Cobreros 等（2012）表明该逻辑有基于严格/宽容语义评价的简单模型（第 6 节讨论），Ripley（2012）表明它可建模真谓词 $T$：$T\langle A\rangle$ 等价于 $A$，而说谎句 $\lambda$（$\lambda=\neg T\lambda$）引起不一致却不致平凡化。按标准说谎者推理可推出 $\vdash T\lambda$ 与 $\vdash\neg T\lambda$（从而 $T\lambda \vdash \bot$），但 $T$-句的切失效，故不能从 $\vdash T\lambda$ 与 $T\lambda\vdash \bot$ 走到预期后果 $\vdash\bot$。（Alan Weir（2005）早先也用过无切逻辑分析素朴真谓词引起的悖论，但所得逻辑不是 ST：条件句与否定的通常规则被改动，且拒斥 **切**。）

出于第 6 节将显明的原因，这叫 **ST**（严格/宽容后承）；其表亲 **TS**（宽容/严格后承），则是不带 **同一性** 规则的经典矢列演算的逻辑。

## 3 证明论

前面已见过用证明呈现子结构逻辑的一个片段：剩余条件，可理解为条件句的两条规则，一条 **引入** 条件句

$$ \cfrac{X, A \vdash B} {X \vdash A \rightarrow B} $$

另一条 **消除** 它：

$$ \cfrac{X \vdash A \rightarrow B \ \ \ Y \vdash A} {X, Y \vdash B} $$

这类规则是自然演绎系统的基石，适用于广大范围的子结构逻辑。但证明论也能另做：*Gentzen* 系统不靠引入与消除运作，而是在后承十字转门左右两侧都作引入。保留上面的引入规则，把消除规则换成左侧引入条件句：

$$ \cfrac{X \vdash A \ \ \ Y(B) \vdash C} {Y(A \rightarrow B, X) \vdash C} $$

规则更复杂，效果却同箭头消除：若 $X$ 足以给出 $A$，且你（在语境 $Y$ 中）用 $B$ 证 $C$，那么（在同一语境 $Y$ 中）用 $A \rightarrow B$ 连同 $X$ 同样能证 $C$——$A \rightarrow B$ 加 $X$ 就给出 $B$。

Gentzen 系统左右两侧都有引入规则，性质特殊，很适合研究逻辑。联结词在证明里总是被 **引入**（自上而下读），证明因此从不 **丢** 结构：某联结词若不在结论中，就根本不会出现在证明里——联结词消除不得。

在线性逻辑、Lambek 演算这类子结构逻辑中，以及在相干逻辑 $\mathbf{R}$ 的无析取片段中，Gentzen 系统可证该逻辑 **可判定**：能找到算法判定 $X \vdash A$ 是否有效。办法是在 Gentzen 系统中搜索 $X \vdash A$ 的证明。结论的前提不得含结论中没有的语词，复杂度又不更大，可能的前提便只有有穷多个；算法检查它们是否合规则，再为其找前提，撞上公理就停。如此，某些子结构逻辑的可判定性得到保证。

但并非所有子结构逻辑都可判定：最著名的是 $\mathbf{R}$ 不可判定，部分因为其证明论比其他子结构逻辑复杂。$\mathbf{R}$ 与线性逻辑、Lambek 演算不同，对合取与析取有直接处理：合取、析取满足 **分配** 规则

$$ p \amp(q \vee r) \vdash (p \amp q) \vee (p \amp r) $$

分配律的自然证明在任何系统里都要用弱化和收缩，$\mathbf{R}$ 不含弱化，自然用不上。于是 $\mathbf{R}$ 的证明论要么把分配当原始规则，要么添第二种前提结合（**外延** 结合，与前述 **内涵** 结合相对），它满足弱化与收缩。

近年受子结构逻辑研究启发，围绕 **经典逻辑** 证明论的工作大量涌现。经典逻辑有全套结构规则，历史上先于子结构逻辑。但要理解 **经典** 证明系统的深层结构，不妨把经典逻辑想成一个基本子结构逻辑，再外加额外结构规则；如此看颇有启发。特别是，两种仅在表层句法上不同的推导，可能实为同一底层“证明”的两种表示。已清楚的是：经典证明之所以区别于同族，正在于收缩与弱化以其完全一般性在场（例如见 Bellin *et al.* 2006 及其文献）[^bellin-2006]。

## 4 模型论

$\mathbf{R}$ 的证明系统比线性逻辑这类缺（外延）合取对析取分配的子结构逻辑复杂，**模型论** 却简单得多。$\mathbf{R}$ 的 Routley–Meyer **模型** 由 **点** 集 $P$ 与 $P$ 上的三元关系 $R$ 组成，条件句 $A \rightarrow B$ 的求值是：

$A \rightarrow B$ 在 $x$ 为真，当且仅当对每个满足 $Rxyz$ 的 $y,z$：$A$ 在 $y$ 真则 $B$ 在 $z$ 真。

论证在模型中 **有效**，当且仅当前提为真的每一点上结论也真。$A \vdash B \rightarrow B$ 无效：可以有 $x$ 使 $A$ 真而 $B \rightarrow B$ 不真。取 $Rxyz$ 使 $B$ 在 $y$ 真、在 $z$ 不真，$B \rightarrow B$ 便不真于 $x$。

三元关系 $R$ 紧跟证明论中前提结合的行为。不同逻辑可给 $R$ 不同条件：前提结合可交换，就给 $R$ 加 **对称性**——$Rxyz$ 当且仅当 $Ryxz$。三元语义为 **建模** 子结构逻辑的行为提供了极大便利。（证明论、代数与语义的对应范围，见 Dunn 论 *Gaggle 理论*（1991），概述于 Restall *Introduction to Substructural Logics*（2000）。

另外，合取、析取若满足上节的分配公理，也能直接建模：合取在一点真，当且仅当两支都真；析取在一点真，当且仅当至少一支真。对 **没有** 分配公理的逻辑（如线性逻辑），语义得更复杂，析取需另立子句，好让分配推理失效。

把语义当建模逻辑的形式装置是一回事，当 **应用** 逻辑的 **解释** 装置是另一回事。子结构逻辑文献提供了若干路子，用三元关系语义描述那些传统结构规则不适用的现象的逻辑结构。

对 Lambek 演算这类逻辑，解释很直接：点取语言单位，三元关系取连接（$Rxyz$ 当且仅当 $x$ 与 $y$ 连接得 $z$）。这些模型里收缩、弱化、置换都失效，前提结合却可结合。

当代语言分类文献把基本 Lambek 演算扩展出更丰富的组合形式，以建模更多句法特征（见 Moortgat 1995）[^moortgat-1995]。

另一应用是 **函数施用** 的语义：把模型中的点同时看作 **函数** 与 **数据**，并主张 $Rxyz$ 当且仅当把 $x$（作函数）施于 $y$（作数据）得 $z$。传统函数说明不鼓励这种双用：函数被视为比输入输出“更高”（按传统集合论模型，函数 $=$ 其 **输入—输出** 对之集，故永不能以 **自身** 为输入——集合不能以自身为成员）。但无类型 $\lambda$-演算建模的函数系统允许自我施用。按此读法，一点具有类型 $A \rightarrow B$，当且仅当凡接受 $A$ 型输入，便给出 $B$ 型输出。其推理规则便是支配函数类型的原理：矢列

$$ (A \rightarrow B) \amp(A \rightarrow C) \vdash A \rightarrow (B \amp C) $$

告诉我们：函数若把 $A$ 映为 $B$、又把 $A$ 映为 $C$，它就把 $A$ 映为既是 $B$ 又是 $C$ 的东西。

这个例子的模型给出一套极弱的子结构逻辑：惯常结构规则——连结合性也不例外——**一条** 都不满足。该例见（Restall 2000 第 11 章）[^restall-2000]。

对 $\mathbf{R}$ 及其自然语言条件句解释，还得弄清楚形式语义究竟建模了现实的哪些特征。这颇有争议：熟悉可能世界间较简单 **二元** 可达关系的模态逻辑的人不惯三元关系；相干逻辑模型中 **否定** 的处理也别开生面。此处不暇详论。部分工作见本百科全书相干逻辑条目；按此视角写的专著是 Mares *Relevant Logic*：*a philosophical interpretation*（2004）。

## 5 量词

子结构逻辑模型中量词处理相当困难，2000 年代初方有进展。难在量词的证明论与模型论似乎对不上号，而量词的公理或规则本身倒直接。全称消除公理 $$ \forall xA \rightarrow A[t/x] $$ 说实例从全称概括推出（在相干意义上）；引入规则 $$ \cfrac{\vdash A\rightarrow B} {\vdash A\rightarrow \forall xB} $$（附条件：$x$ 在 $A$ 中不自由）说：若能作为逻辑之事，从对该实例无所断言的某假定证出概括 $\forall xB$ 的实例，则也能从此假定证出概括。这两条似乎与一系列子结构逻辑（从最弱系统到 $\mathbf{R}$ 这类强系统）对一阶量词的任何解释都相合。

量词的证明论看来规矩，推广到模型论却困难。Richard Routley（1980）表明，把量词规则加到很弱的子结构逻辑 $\mathbf{B}$ 上，与三元关系语义恰相配合：量词在对象域上取值，该域在模型所有点上恒定。但这 **不** 适用于更强的逻辑，尤其 $\mathbf{R}$。Kit Fine（1989）表明，有个复杂公式在 $\mathbf{R}$ 的所有常域框架模型中成立，却不可从公理推出。细节不重要，根由却好说：常域语义中，$\forall x Fx$ 在每点的真值条件与实例族 $Fx_1$、$Fx_2$、$Fx_3,\ldots$、$Fx_\lambda,\ldots$（域中对象由 $x_i$ 的值枚举）完全相同；于是 $\forall x Fx$ 在语义上与（可能无穷的）合取 $Fx_1\land Fx_2\land Fx_3\land\cdots $ 无从区分。可任何实例合取（哪怕无穷）都不可能 **相干地** 等价于全称量化主张 $\forall x Fx$：这些实例可能在某情形中为真而概括不为真——若事物比那些更多的话。常域模型似乎不适合相干量化理论。

Robert Goldblatt 与 Edwin Mares（2006）表明，相干量化有自然的替代语义，优雅而相对直接。关键是把三元关系语义稍改：并非每个点集都算“命题”，即并非每个点集都是句子的可能语义值。于是，尽管 $\forall xFx$ 各实例的无穷合取 $Fx_1\land Fx_2\land Fx_3\land\cdots $ 确定了一个世界集，那个集合并未必要算作命题。（也许无法把那些特定对象单独挑出，在一个判断里收拢。）我们 **能说** 的是概括 $\forall xFx$：它是蕴涵每个实例的命题（全称消除公理）；而命题若蕴涵每个实例，就蕴涵概括（引入规则）。所以 $\forall xFx$ 表达的命题，是蕴涵每个实例 *Fa* 的 **语义上最弱** 的命题。这正是 Goldblatt–Mares 模型中全称量词的建模条件，与公理精确吻合。

## 6 无切或同一性的逻辑

如第 1 节所见，结构规则分两类：一类约束矢列某一侧前提或结论的结合（交换、收缩、弱化），另一类本质上涉及两侧之间的联系（同一性、切）。前面处理证明与模型，聚焦于对第一类规则作特殊选择的子结构逻辑；最后一节，转向拒斥 **切** 或 **同一性** 的较新工作。

无 **切** 的逻辑，后承关系不传递。哲学文献举了几条理由。其一，把焦点放在 **实质** 后承（见 Brandom 2000）[^brandom-2000] 或 **缺省** 后承（见 Reiter 1980 及 **非单调逻辑** 条目）[^reiter-1980]，而非必然的、形式的后承。（Tweety 是鸟，缺省推断它会飞是恰当的；它若是企鹅，可推断它是鸟。但切掉中间一步、径直推断它会飞并不恰当。）

另一理由基于 **相干性**：Neil Tennant 因相干之故倡一种拒斥无限制 **切** 的相干逻辑（2017）。其 **核心逻辑** 中，$\neg p\vdash \neg p\lor q$ 与 $p,\neg p\lor q\vdash q$ 都成立，却不能用 **切** 推出 $p,\neg p\vdash q$——这里 $q$ 不相干，是逻辑上的搭便车者。核心逻辑中 $p,\neg p\vdash $ 成立（$p$ 与其否定联合不一致），但不能用弱化得 $p,\neg p\vdash q$。切规则在此不普遍成立，但有一个限制版 **成立**：若 $X\vdash A,Y$ 且 $X',A\vdash Y'$，则有 **子集** $X^*\subseteq X\cup X'$、$Y^*\subseteq Y\cup Y'$ 使 $X^*\vdash Y^*$。可是，出于核心逻辑理由限制 **切**，对想承认 $\vdash T\lambda$ 与 $\vdash T\lambda\vdash\bot$、同时拒斥 $\vdash\bot$ 以回应语义悖论的逻辑学家毫无帮助。

前述严格/宽容有效性的无切逻辑 **ST**，与实质推理、缺省推理或 Tennant 核心逻辑都大不相同。首先，就有效矢列而言，它 **就是** 经典逻辑：由不带 **切** 的 Gentzen 矢列演算给出，而 **切** 可消除（Gentzen 1935）。

**ST** 的模型论异常简单：按 **三分** 评价求值。（可理解为给每个公式指派 $0$、$i$、$1$ 之一的函数，或等价地，指派 $0$ 或 $1$、某些情形下可不指派的 **部分** 函数。）复杂公式用标准经典真值条件求值，自然修改以容纳部分赋值：$v(\neg A)=1$ 当且仅当 $v(A)=0$，$v(\neg A)=0$ 当且仅当 $v(A)=1$；$v(A\amp B)=1$ 当且仅当 $v(A)=1$ 且 $v(B)=1$，$v(A\amp B)=0$ 当且仅当 $v(A)=0$ 或 $v(B)=0$，余类推。（这是 Kleene 强三值逻辑赋值的一种定义。）赋值是 $X\vdash Y$ 的 **ST** 反例，当且仅当它给 $X$ 中每式指派 $1$、给 $Y$ 中每式指派 $0$。把得到 $1$ 者看作 **严格** 真（或以严格标准可断言），把未得 $0$ 者看作 **宽容** 真（或以宽容标准可断言），则有效论证就是前提 **严格** 真时结论至少 **宽容** 真的论证。故名 **ST**。有效性并非固定值的保持（后件标准低于前件），**切** 因此一般可能失效。

不难看出，这个子结构逻辑是考察语义悖论的好去处。给定说谎句 $\lambda$，$\vdash T\lambda$ 的推导说明说谎者至少宽容为真；$T\lambda\vdash\bot$ 的推导说明它不可能 **严格** 为真。它被钉在中间：它与它的否定都宽容为真，都不严格为真。

类似地，堆垛悖论中形如 $p_n\rightarrow p_{n+1}$ 的每个条件句主张，都至少可看作 **宽容** 为真：相邻情形变化足够慢，就不会出现 $p_n$ 严格真而 $p_{n+1}$ 严格假的情形。

**ST** 对悖论的回应一旦提出，拒斥 **剩下** 那条结构规则 **同一性** 也就顺理成章。Fjellstand（2015）与 French（2016）考察了不带 **同一性** 的矢列演算的逻辑，它在部分赋值中同样有自然语义。保留 **切**、丢弃同一性，自然逻辑是 **TS**：$X\vdash Y$ 有 **TS** 反例，当且仅当存在赋值把 $X$ 的每个成员送 **离 $0$**（至少宽容为真），把 $Y$ 的每个成员送 **离 $1$**（不严格为真）。把 $p$ 既不指 $0$ 也不指 $1$ 的赋值，便是 $p\vdash p$ 的反例——于是有手段让同一性失效。

这两族逻辑——无切与无同一性者——以第一代子结构逻辑没有的方式追问：它们算何种 **逻辑**？**ST** 的可证矢列在逻辑词汇上与经典逻辑完全相同，**TS** 则一条也没有。**ST** 等于经典逻辑吗？**TS** 等于某个无可导出矢列的逻辑吗？径直答“是”就错过了它们的独特行为：**ST** 与经典逻辑的差别不在 **矢列** 层面，而在矢列间关系层面。**切** 可看作关联矢列的推理规则，在任何二值赋值类下有效，在 **ST** 中却无效。**TS** 在矢列层面虽空，在矢列间关系层面却丰富。由此生出晚近的 **元推理** 研究（见 Barrio *et al* 2014、2019）[^barrio-2014][^barrio-2019]。反思 **ST**、**TS** 这类用两个特出值的逻辑中矢列间元推理的自然理解，引出一个问题：单个公式层面既已有严格与宽容两种有效性等级，到矢列层面何必只给一个裁决？其实（第 2 层）元推理也有两种自然等级：**ST** 有效性比 **TS** 宽容得多。可说矢列对矢列的元推理 **TS/ST** 有效，当且仅当前提矢列 **TS** 有效时结论矢列 **ST** 有效。于是 **切** 这条元推理确实 **TS/ST** 元有效；**TS/ST** 有效的元推理恰是经典逻辑传统上有效的那族元推理，且此结果自然推广到一切 *n* 的 *n*-层元推理（Barrio *et al* 2019）[^barrio-2019]。

无切矢列演算与三值逻辑的联系由来已久，早于晚近子结构逻辑工作。Schütte（1960）为无切经典矢列演算用了非确定三值语义，Girard（1987b 第 3 章）分析无切演算语义时大量取用；Hösli 与 Jäger（1994）也考察了三值方法在缺 **同一性** 的经典矢列演算上的应用，并用于理解逻辑编程中的现象（Jäger, 1993）。

## References（引用注释）

**以下文献从原文照录，不作翻译；中国文献译为中文。**

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

### Books on Substructural Logic and Introductions to the Field

### Other Works Cited

[^robert-1992]: A comprehensive bibliography on relevant logic was put together by Robert Wolff and can be found in Anderson, Belnap and Dunn 1992. The bibliography in Restall 2000 is not as comprehensive as Wolff’s, but it does include material up to the end of the 20th Century.
[^anderson-1975]: Anderson, A.R., and Belnap, N.D., 1975, *Entailment: The Logic of Relevance and Necessity*, Princeton, Princeton University Press, Volume I.
[^anderson-1992]: Anderson, A.R., Belnap, N.D. Jr., and Dunn, J.M., 1992, *Entailment*, Volume II, Princeton, Princeton University Press. [This book and the previous one summarise the work in relevant logic in the Anderson–Belnap tradition. Some chapters in these books have other authors, such as Robert K. Meyer and Alasdair Urquhart.]
[^barrio-2022]: Barrio, E. and Égré (2022) “Substructural Logics and Metainferences” *Journal of Philosophical Logic*, 51: 1215–1231. [A summary of recent work on reflexivity and the *Cut* rule and characterising different logics in terms of the metainferences they admit.]
[^bimbó-2008]: Bimbó, K. and Dunn, J. M., 2008, *Generalised Galois Logics: Relational Semantics of Nonclassical Logical Calculi*, CSLI Lecture Notes, v. 188, CSLI, Stanford. [A systematic treatment of the ternary relational semantics and its generalisations for substructural logics.]
[^dunn-2000]: Dunn, J. M. and Restall, G., 2000, “Relevance Logic” in F. Guenthner and D. Gabbay (eds.), *Handbook of Philosophical Logic* second edition; Volume 6, Kluwer, pp 1–136. [A summary of work in relevant logic in the Anderson–Belnap tradition.]
[^galatos-2007]: Galatos, N., P. Jipsen, T. Kowalski, and H. Ono, 2007, *Residuated Lattices: An Algebraic Glimpse at Substructural Logics* (Studies in Logic: Volume 151), Amsterdam: Elsevier, 2007.
[^mares-2004]: Mares, Edwin D., 2004, *Relevant Logic*: *a philosophical interpretation* Cambridge University Press. [An introduction to relevant logic, proposing an information theoretic understanding of the ternary relational semantics.]
[^moortgat-1988]: Moortgat, Michael, 1988, *Categorial Investigations: Logical Aspects of the Lambek Calculus* Foris, Dordrecht. [An introduction to the Lambek calculus.]
[^moot-2012]: Moot, Richard and Retoré Christian (2012) *The Logic of Categorical Grammars*, Springer, Berlin. [An introduction to the Lambek calculus, including its non-associative variant, multimodal calculi, linear logic and proof nets.]
[^morrill-1994]: Morrill, Glyn, 1994, *Type Logical Grammar: Categorial Logic of Signs* Kluwer, Dordrecht [An introduction to the Lambek calculus.]
[^ono-2019]: Ono, Hiroakira, 2019, *Proof Theory and Algebra in Logic* Springer, Singapore [Not exclusively on substructural logics, this treatment of the relationship between proof theory and algebra treats logical systems quite generally, and includes substructural logics in its remit.]
[^paoli-2002]: Paoli, Francesco, 2002, *Substructural Logics*: *A Primer* Kluwer, Dordrecht [A general introduction to substructural logics.]
[^read-1988]: Read, S., 1988, *Relevant Logic*, Oxford: Blackwell. [An introduction to relevant logic motivated by considerations in the theory of meaning. Develops a Lemmon-style proof theory for the relevant logic $\mathbf{R}$.]
[^restall-2000]: Restall, Greg, 2000, *An Introduction to Substructural Logics*, Routledge. ([online précis](http://consequently.org/isl/)) [A general introduction to the field of substructural logics.]
[^routley-1983]: Routley, R., Meyer, R.K., Plumwood, V., and Brady, R., 1983, *Relevant Logics and their Rivals*, Volume I, Atascardero, CA: Ridgeview. [Another distinctive account of relevant logic, this time from an Australian philosophical perspective.]
[^schroeder-heister-1993]: Schroeder-Heister, Peter, and Došen, Kosta, (eds), 1993, *Substructural Logics*, Oxford University Press. [An edited collection of essays on different topics in substructural logics, from different traditions in the field.]
[^troestra-1992]: Troestra, Anne, 1992, *Lectures on Linear Logic*, CSLI Publications [A quick, easy-to-read introduction to Girard’s linear logic.]
[^zardini-2021]: Zardini, Elia, 2021, “Substructural Approaches to Paradox,” *Synthese*, 199: 493–525. [A summary of recent work on substructural approaches to paradox.]
[^ackermann-1956]: Ackermann, Wilhelm, 1956, “Begründung Einer Strengen Implikation,” *Journal of Symbolic Logic*, 21: 113–128.
[^avron-1988]: Avron, Arnon, 1988, “The Semantics and Proof Theory of Linear Logic,” *Theoretical Computer Science*, 57(2–3): 161–184.
[^barrio-2014]: Barrio, Eduardo; Lucas Rosenblatt, and Diego Tajer, 2014, “The Logics of Strict-Tolerant Logic,” *Journal of Philosophical Logic*, 44:5, 551–571.
[^barrio-2019]: Barrio, Eduardo; Federico Pailos, and Damian Szmuc, 2019, “A Hierarchy of Classical and Paraconsistent Logics,” *Journal of Philosophical Logic*, 49:1, 93–120.
[^bellin-2006]: Bellin, Gianluigi; Martin Hyland, Edmund Robinson, and Christian Urban, 2006, “Categorical Proof Theory of Classical Propositional Calculus,” *Theoretical Computer Science*, 364: 146–165.
[^brandom-2000]: Brandom, Robert, 2000 *Articulating Reasons*, Harvard University Press.
[^church-1951]: Church, Alonzo, 1951, “The Weak Theory of Implication,” in *Kontrolliertes Denken: Untersuchungen zum Logikkalkül und zur Logik der Einzelwissenschaften*, A. Menne, A. Wilhelmy and H. Angsil (eds.), Kommissions-Verlag Karl Alber, 22–37.
[^cobreros-2012]: Cobreros, Pablo; Paul Égré, David Ripley and Robert van Rooij, 2012, ‘Tolerant, Classical, Strict’ *Journal of Philosophical Logic*, 21:347–385.
[^curry-1977]: Curry, Haskell B., 1977, *Foundations of Mathematical Logic*, New York: Dover (originally published in 1963).
[^dunn-1991]: Dunn, J.M., 1991, “Gaggle Theory: An Abstraction of Galois Connections and Residuation with Applications to Negation and Various Logical Operations,” in *Logics in AI, Proceedings European Workshop JELIA 1990* (Lecture notes in Computer Science, Volume 476), Berlin: Springer-Verlag.
[^dunn-1993]: –––, 1993, “Star and Perp,” *Philosophical Perspectives*, 7: 331–357.
[^field-2008]: Field, H., 2008, *Saving Truth from Paradox*, Oxford: Oxford University Press.
[^fine-1989]: Fine, K., 1989, “Incompleteness for Quantified Relevance Logics,” in J. Norman and R. Sylvan (eds.), *Directions in Relevant Logic*, Dordrecht: Kluwer, pp. 205–225.
[^fjellstand-2015]: Fjellstand, Andreas, 2015. “How a Semantics for Tonk Should Be,” *Review of Symbolic Logic*, 8:488–505.
[^french-2016]: French, Rohan, 2016. “Structural Reflexivity and the Paradoxes of Self-Reference,”, *Ergo*, 3 No. 05. doi:10.3998/ergo.12405314.0003.005
[^geach-1955]: Geach, P. T., 1955, “On Insolubilia,” *Analysis*, 15: 71–72.
[^gentzen-1935]: Gentzen, Gerhard, 1935, “Untersuchungen über das logische Schließen,” *Mathematische Zeitschrift*, 39: 176–210 and 405–431. [An English translation is found in Gentzen 1969.]
[^gentzen-1969]: –––, 1969, *The Collected Papers of Gerhard Gentzen*, M. E. Szabo (ed.), Amsterdam: North Holland, 1969.
[^girard-1987]: Girard, Jean-Yves, 1987, “Linear Logic,” *Theoretical Computer Science*, 50: 1–101.
[^girard-1987b]: –––, 1987b, *Proof Theory and Logical Complexity*, Volume 1, Bibliopolis, Naples.
[^goldblatt-2006]: Goldblatt, R., and E. Mares, 2006, “An Alternative Semantics for Quantified Relevant Logic,” *Journal of Symbolic Logic*, 71(1): 163–187.
[^hösli-1994]: Hösli, Brigitte and Gerhard Jäger, 1994. “About Some Symmetries of Negation,” *Journal of Symbolic Logic* 59(2):473–485.
[^jäger-1993]: Jäger, Gerhard, 1993, “Some proof-theoretic aspects of logic programming,” p. 113–142 in *Logic and Algebra of Specification*, F. Bauer, W. Brauer and H. Schwichtenberg (ed.), Springer.
[^lambek-1958]: Lambek, Joachim, 1958, “The Mathematics of Sentence Structure,” *American Mathematical Monthly*, 65: 154–170.
[^lambek-1961]: –––, 1961, “On the Calculus of Syntactic Types, ” in *Structure of Language and its Mathematical Aspects* (Proceedings of Symposia in Applied Mathematics, XII), R. Jakobson (ed.), Providence, RI: American Mathematical Society.
[^moh-1950]: Moh Shaw-Kwei, 1950, “The Deduction Theorems and Two New Logical Systems,” *Methodos*, 2: 56–75.
[^moortgat-1995]: Moortgat, Michael, 1995, “Multimodal Linguistic Inference,” *Logic Journal of the IGPL*, 3: 371–401.
[^ono-2003]: Ono, Hiroakira, 2003, “Substructural Logics and Residuated Lattices – an Introduction,” in V. Hendricks and J. Malinowski (eds.), *Trends in Logic: 50 Years of Studia Logica*, Dordrecht: Kluwer, 2003, pp. 193–228.
[^reiter-1980]: Reiter, Raymond, 1980. “A Logic for Default Reasoning,” *Artificial Intelligence*, 13:81–132.
[^ripley-2012]: Ripley, David, 2012, “Conservatively Extending Classical Logic with Transparent Truth’ *The Review of Symbolic Logic*, 5:354–378.
[^rooij-2011]: Rooij, Robert van, 2011, “Vagueness, tolerance and non-transitive entailment,’ in P. Cintula, C. Fermüller, L. Godo, and P. Hajek (eds.), *Reasoning Under Vagueness: Logical, Philosophical and Linguistic Perspectives*, College Publications, pp. 205–222.
[^routley-1980]: Routley, R., 1980. “Problems and Solutions in Semantics in Quantified Relevant Logics,” in A. Arruda, R. Chuaqui, and N.C.A. Da Costa (eds.), *Mathematical Logic in Latin America*, Amsterdam: North Holland, 1980, pp. 305–340.
[^schütte-1960]: Schütte, Kurt, 1960. “Syntactical and Semantical Properties of Simple Type Theory,” *Journal of Symbolic Logic*, 25:305–326.
[^tennant-2017]: Tennant, Neil, 2017. *Core Logic*, Oxford University Press.
[^troelstra-1992]: Troelstra, A.S., 1992, “Lectures on Linear Logic”, *CSLI Lecture Notes* (Number 29), Stanford: CSLI Publications.
[^weir-2005]: Weir, Alan, 2005. “Naive Truth and Sophisticated Logic” in Jc Beall and B. Armour-Garb (eds.), *Deflationism and Paradox*, pages 218–249.
[^zardini-2008]: Zardini, Elia, 2008. “A Model of Tolerance,” *Studia Logica* 90(3), 337–368.

## 学术工具

* [如何引用本词条](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=logic-substructural)。
* [预览本词条的 PDF 版本](https://leibniz.stanford.edu/friends/preview/logic-substructural/)，见 [SEP 学会之友](https://leibniz.stanford.edu/friends/)。
* 在 [InPhO](https://www.inphoproject.org/entity?sep=logic-substructural&redirect=True) 查找与本词条相关的话题与思想家。
* 在 [PhilPapers](https://philpapers.org/sep/logic-substructural/) 查看本词条的增强文献目录及其数据库链接。

## 其他网络资源

- Restall, Greg, 1994, [*On Logics Without Contraction*](http://consequently.org/writing/onlogics)，昆士兰大学博士论文。
- Slaney, John, 1995, [MaGIC：蕴涵联结词的矩阵生成器](http://users.cecs.anu.edu.au/~jks/magic.html)，为子结构逻辑生成有穷模型的软件包。

## 相关词条

形式逻辑中的句子连接词 | 线性逻辑 | 模态逻辑 | 次协调逻辑 | 命题逻辑 | 相干逻辑 | 证明论

**（译注：相关词条的中文站内链接将由管线在对应词条重译完成后统一挂接。）**
