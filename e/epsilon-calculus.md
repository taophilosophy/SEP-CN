# ε 演算 The Epsilon Calculus (Jeremy Avigad and Richard Zach)

**首次发表于 2002 年 5 月 3 日；2024 年 7 月 18 日实质修订。**

**首次发表于 2002 年 5 月 3 日；2024 年 7 月 18 日实质修订。**

epsilon 演算是大卫·希尔伯特为其数学基础纲领而发展的一种逻辑形式体系。epsilon 算子是一个构词算子，它在通常的谓词逻辑中取代量词。具体而言，在此演算中，项 $\varepsilon x A$ 表示某个满足 $A(x)$ 的 $x$（如果存在的话）。在希尔伯特纲领中，epsilon 项扮演理想元素的角色；希尔伯特的有穷主义一致性证明的目标，是给出一个从形式证明中移除这些项的程序。实现这一点的程序基于希尔伯特的 epsilon 替换方法。然而，epsilon 演算在其他语境中也有应用。epsilon 演算的首次一般应用是希尔伯特的 epsilon 定理，而后者又为 Herbrand 定理的第一个正确证明奠定了基础。epsilon 算子的变体已被应用于语言学、计算机科学以及语言哲学、数学哲学与科学哲学。

## 1 概述

世纪之交，大卫·希尔伯特与亨利·庞加莱被公认为同代人中最重要的两位数学家。希尔伯特的数学兴趣广泛，其中包括对数学基础的关注：其《几何基础》出版于 1899 年，而在 1900 年向国际数学家大会提出的问题清单中，有三条明确涉及基础问题。

罗素悖论发表后，希尔伯特在 1904 年第三次国际数学家大会上发表演讲，首次勾勒了他通过语法一致性证明为数学提供严格基础的计划。但他没有认真地回到这一主题，直到 1917 年，在保罗·贝奈斯的协助下开始关于数学基础的系列讲座。虽然希尔伯特对罗素与怀特海在《数学原理》中的工作印象深刻，但他确信逻辑主义把数学还原为逻辑的尝试不可能成功，尤其是因为其可还原性公理的非逻辑性质。与此同时，他认为直觉主义对排中律的拒斥是数学所不能接受的。因此，逻辑悖论与集合论悖论的发现引发了忧虑，于是需要一种新的进路为现代数学方法辩护。

到 1920 年夏，希尔伯特已经形成了这样一种进路。第一，现代数学方法要在形式演绎系统中得到表示。第二，这些形式系统要在语法上证明为一致——既不靠展示一个模型，也不把一致性还原到另一个系统，而是依靠一种明确的、具有“有穷”性质的直接元数学论证。这一进路后来被称为希尔伯特纲领。epsilon 演算为该纲领提供第一个组成部分，而其 epsilon 替换方法为第二个组成部分提供支持。

就其最基本的形式而言，epsilon 演算是一阶谓词逻辑的扩充，增有一个“epsilon 运算”；该运算为任何为真的存在公式挑选存在量词的一个见证。这一扩充是保守的，因为它不增加任何新的一阶后承。但反过来，量词可以用 epsilon 来定义，因此一阶逻辑可以被理解为涉及 epsilon 运算的无量词推理。正是这后一特性使得该演算便于证明一致性。适当扩充 epsilon 演算，便可把更强的、量词性的数论与集合论嵌入无量词演算。希尔伯特期望能够证明这种扩充的一致性。

## 2 Epsilon 演算

在 1921 年的汉堡讲演（1922）中，希尔伯特首次提出了在算术形式系统中用这种运算处理排中律的想法。这些想法在 1921 至 1923 年间的一系列讲义课程以及希尔伯特（1923）中发展为 epsilon 演算与 epsilon 替换方法。epsilon 演算的最终表述可见于威廉·阿克曼的博士论文（1924）。

本节将描述对应于一种一阶逻辑的演算版本，而对一阶与二阶算术的扩充将在下文描述。

设 $L$ 为一种一阶语言，即一个具有指定元数的常项、函数与关系符号的清单。$L$ 的 epsilon 项集合与公式集合被同时归纳地定义如下：

* $L$ 的每个常项是一个项。
* 每个变项是一个项。
* 若 $s$ 与 $t$ 是项，则 $s = t$ 是一个公式。
* 若 $s_1, \ldots, s_k$ 是项且 $F$ 是 $L$ 的一个 $k$ 元函数符号，则 $F(s_1, \ldots, s_k)$ 是一个项。
* 若 $s_1, \ldots, s_k$ 是项且 $R$ 是 $L$ 的一个 $k$ 元关系符号，则 $R(s_1, \ldots, s_k)$ 是一个公式。
* 若 $A$ 与 $B$ 是公式，则 $(A \wedge B)$、$(A \vee B)$、$(A \rightarrow B)$ 与 $\neg A$ 也是公式。
* 若 $A$ 是公式且 $x$ 是变项，则 $\varepsilon x A$ 是一个项。

在无歧义时可省略括号。代入与自由变项、约束变项的概念按通常方式定义；特别地，变项 $x$ 在项 $\varepsilon x A$ 中被约束。预期解释是：$\varepsilon x A$ 表示 **某个** 满足 $A$ 的 $x$（如果存在的话）。因此，epsilon 项受以下公理支配（希尔伯特的“超限公理”）：$$ A(x) \rightarrow A(\varepsilon x A) $$ 此外，epsilon 演算还包括支配经典命题联结词的完备公理组，以及支配等词符号的公理。演算的仅有规则如下：

* 肯定前件式
* 代入：从 $A(x)$ 推出 $A(t)$，$t$ 为任意项。

早期形式的 epsilon 演算（如希尔伯特 1923 中所呈现的）[^hilbert-1923]使用 epsilon 算子的一种对偶形式，其中 $\varepsilon x A$ 返回一个 **证伪** $A(x)$ 的值。上文的版本用于阿克曼的博士论文（1924），并已成为标准。

注意，刚描述的演算是无量词的。量词可以按如下方式 **定义**：$$ \begin{align} \exists x A(x) &\equiv A(\varepsilon x A) \\ \forall x A(x) &\equiv A(\varepsilon x (\neg A)) \end{align} $$ 通常的量词公理与规则可以从这些定义导出，因此上述定义起到把一阶逻辑嵌入 epsilon 演算的作用。但逆命题不成立：在该嵌入下，并非 epsilon 演算中的每个公式都对应某个通常的量化公式。因此，epsilon 演算比谓词演算更具表达力，原因很简单：epsilon 项能以比量词更复杂的方式组合。

值得指出的是，epsilon 项是非决定性的。例如，在带有常项符号 $a$ 与 $b$ 的语言中，$\varepsilon x (x = a \vee x = b)$ 要么是 $a$ 要么是 $b$，但演算对究竟是哪个完全不做规定。人们可以在演算中增加一个 **外延性** 图式，$$ \forall x (A(x) \leftrightarrow B(x)) \rightarrow \varepsilon x A = \varepsilon x B $$ 该图式断言 epsilon 算子给等价的公式 $A$ 与 $B$ 指派相同的见证。但对许多应用而言，这一附加图式并非必要。

## 3 Epsilon 定理

希尔伯特与贝奈斯《数学基础》第二卷（1939）总结了当时已证的关于 epsilon 演算的结果。其中包括：第一与第二 epsilon 定理及其在一阶逻辑中的应用；带开放归纳之算术的 epsilon 替换方法；以及用 epsilon 演算发展分析（即二阶算术）。

第一与第二 epsilon 定理如下：

**第一 epsilon 定理。** 设 $\Gamma \cup \{A\}$ 是一组不涉及 epsilon 符号的无量词公式。若 $A$ 可在 epsilon 演算中从 $\Gamma$ 导出，则 $A$ 可在无量词谓词逻辑中从 $\Gamma$ 导出。

**第二 epsilon 定理。** 设 $\Gamma \cup \{A\}$ 是一组不涉及 epsilon 符号的公式。若 $A$ 可在 epsilon 演算中从 $\Gamma$ 导出，则 $A$ 可在谓词逻辑中从 $\Gamma$ 导出。

在第一 epsilon 定理中，“无量词谓词逻辑”意指包含上述代入规则，因此无量词公理的行为如同其全称封闭。由于 epsilon 演算包含一阶逻辑，第一 epsilon 定理蕴含：从无量词公理导出无量词定理时，任何经过一阶谓词逻辑的迂回最终都可避免。第二 epsilon 定理表明：从谓词演算语言的公理导出该语言中的定理时，任何经过 epsilon 演算的迂回也可避免。

更一般地，第一 epsilon 定理确立：在从其他无量词公式导出无量词公式的证明中，量词与 epsilon 总可以被消去。这对希尔伯特纲领尤为重要，因为 epsilon 扮演数学中理想元素的角色。如果无量词公式对应数学理论的“实在”部分，那么第一 epsilon 定理表明：理想元素可以从实在命题的证明中被消去——前提是公理也是实在命题。

这一想法在希尔伯特与贝奈斯从第一 epsilon 定理导出的某个一般一致性定理中得到精确化。该定理说：设 $F$ 为由谓词逻辑加上常项、函数与谓词符号以及无量词且无 epsilon 的真公理而得到的任何形式系统，并设新语言中原子公式的真值是可判定的。则 $F$ 在强意义上是一致的：每个可导的无量词且无 epsilon 的公式都是真的。希尔伯特与贝奈斯用这一定理给出了初等几何的有穷主义一致性证明（1939，第 1.4 节）。

为算术与分析给出一致性证明的困难在于：把这一结果扩展到公理也包含理想元素——即 epsilon 项——的情形。

**延伸阅读。** 关于 epsilon 演算与 epsilon 定理的原始文献（Ackermann 1924, Hilbert & Bernays 1939）[^ackermann-1924][^hilbert-1939]仅有德文版。Leisenring 1969 是一部关于 epsilon 演算的较为现代的英文导论性专著。第一与第二 epsilon 定理在 Zach 2017 中有详细描述。Moser 与 Zach 2006 对不带等词的情形给出了详细分析，Miyamoto 与 Moser 2024 则处理带等词的情形。原始证明是针对 epsilon 演算的公理化表述给出的。Maehara 1955 首次考虑了带 epsilon 项的矢列演算。他展示了如何利用切割消去证明第二 epsilon 定理，然后把该定理加强到包含外延性图式（Maehara 1957）[^maehara-1957]。Baaz 等 2018 给出了第一 epsilon 定理的改进版本。文献中的错误（包括 Leisenring 的书）的更正见 Flannagan 1975；Ferrari 1987；以及 Yasuhara 1982。一种基于 Skolem 函数的、因此与一阶逻辑兼容的 epsilon 演算变体在 Davis 与 Fechter 1991 中得到讨论。

## 4 Herbrand 定理

希尔伯特与贝奈斯使用 epsilon 演算的方法来建立关于一阶逻辑而不涉及 epsilon 演算本身的定理。一个例子是 **Herbrand 定理**（Herbrand 1930；见 Buss 1995, Girard 1982，以及 Buss 1998 的第 2.5 节）[^buss-1995][^buss-1998][^girard-1982][^herbrand-1930]。它常被表述为：如果一个存在公式 $$ \exists x_1 \ldots \exists x_k A(x_1, \ldots, x_k) $$ 在（不带等词的）一阶谓词逻辑中可导，其中 $A$ 是无量词的，那么存在项序列 $t_{1}^1, \ldots, t_{k}^1, \ldots, t_{1}^n, \ldots, t_k ^n$，使得 $$ A(t_{1}^1, \ldots, t_k ^1) \vee \ldots \vee A(t_{1}^n, \ldots, t_k^n) $$ 是重言式。如果处理的是带等词的一阶逻辑，则须把“重言式”替换为“等词公式的代入实例的重言后承”；我们将用“准重言式”来称谓这种公式。

刚才所述的 Herbrand 定理版本，可从希尔伯特与贝奈斯的 **扩展第一 epsilon 定理** 立即导出。然而，利用与第二 epsilon 定理之证明相关的方法，希尔伯特与贝奈斯导出了一个更强的结果，该结果如同 Herbrand 原来的表述一样提供了更多信息。为理解下述定理的两个部分，考虑一个具体例子会有帮助。设 $A$ 为公式

$$ \exists x_1 \forall x_2 \exists x_3 \forall x_4 B(x_1, x_2, x_3, x_4) $$ 其中 $B$ 是无量词的。$A$ 的否定等价于 $$ \forall x_1 \exists x_2 \forall x_3 \exists x_4 \neg B(x_1, x_2, x _3, x_4). $$ 通过 Skolem 化——即用函数符号见证存在量词——我们得到 $$ \exists f_2, f_4 \forall x_1, x_3 \neg B(x_1, f_2 (x_1), x_3, f_4 (x_1, x_3)). $$ 取其否定，我们看到原公式“等价”于 $$ \forall f_2, f_4 \exists x_1, x_3 B(x_1, f_2 (x_1), x_3, f_4 (x_1, x_3)). $$

下述定理的第一款，在此具体情形中，是说上面的公式 $A$ 在一阶逻辑中可导，当且仅当在带有 $f_2$ 与 $f_4$ 的扩张语言中存在项序列 $t_{1}^1, t_{3}^1, \ldots, t_{1}^n, t_{3}^n$，使得 $$ B(t_{1}^1, f_2 (t_{1}^1), t_{3}^1, f_4 (t_{1}^1,t_{3}^1)) \vee \ldots \vee B(t_{1}^n, f_2 (t_{1}^n), t_{3}^n, f_4 (t_{1}^n,t_{3}^n)) $$ 是准重言式。

下述定理的第二款，在此具体情形中，是说公式 $A$ 在一阶逻辑中可导，当且仅当在 **原语言** 中存在变项序列 $x_{2}^1, x_{4}^1, \ldots, x_2^n, x_4 ^n$ 与项序列 $s_{1}^1, s_{3}^1, \ldots, s_1^n, s_3 ^n$，使得 $$ B(s_{1}^1, x_{2}^1, s_{3}^1, x_4 ^1 ) \vee \ldots \vee B(s_1^n, x_2^n, s_3^n, x_4^n ) $$ 是准重言式，且 $A$ 可从该公式出发仅用下述量词规则与幂等规则导出。

更一般地，设 $A$ 为任何前束公式，形如 $$ \mathbf{Q}_1 x_1 \ldots \mathbf{Q}_n x_n B(x_1, \ldots, x_n), $$ 其中 $B$ 是无量词的。则 $B$ 被称为 $A$ 的 **母式**，$B$ 的一个 **实例** 通过在该语言的项替换 $B$ 的某些变项而得到。$A$ 的 **Herbrand 范式** $A^H$ 通过以下步骤获得：

* 删去每个全称量词；
* 把每个全称量化的变项 $x_i$ 替换为 $f_i (x_{i}^1,\ldots, x_{i}^{k(i)})$，其中 $x_{i}^1,\ldots, x_{i}^{k(i)}$ 是 $A$ 中前于 $\mathbf{Q}_i$ 的（按序排列的）对应存在量词的变项，$f_i$ 是为此目的指定的一个新函数符号。

所谓 $A^H$ 母式的一个 **实例**，指在 $A^H$ 的母式中代入扩张语言的项而得到的公式。现在我们可以陈述希尔伯特与贝奈斯对

**Herbrand 定理。**（1）一个前束公式 $A$ 在谓词演算中可导，当且仅当 $A^H$ 的母式的实例的某个析取是准重言式。

（2）一个前束公式 $A$ 在谓词演算中可导，当且仅当 $A$ 的母式的实例的某个析取 $\bigvee_j B_j$ 是准重言式，且 $A$ 可从 $\bigvee_j B_j$ 出发、仅用以下规则导出：

* 从 $C_1 \vee \ldots \vee C_i (t) \vee \ldots \vee C_m$ 推出 $C_1 \vee \ldots \vee \exists x C_i (x) \vee \ldots \vee C_m$；以及
* 从 $C_1 \vee \ldots \vee C_i (x) \vee \ldots \vee C_m$ 推出 $C_1 \vee \ldots \vee \forall xC_i (x) \vee \ldots \vee C_m$（若 $x$ 不在 $C_j$ 中，$j \ne i$）；

以及 $\vee$ 的幂等性（从 $C \vee C \vee D$ 推出 $C \vee D$）。

Herbrand 定理也可以通过切割消去——经由根岑的“中后续定理”——得到。然而，使用第二 epsilon 定理的证明具有作为 Herbrand 定理第一个完整且正确的证明的殊荣。此外——这一点很少被认识到——基于切割消去的证明只给出一个界：Herbrand 析取的长度是证明中切割秩与切割公式复杂性的函数。而基于 epsilon 演算的证明给出的界，则是超限公理应用次数及其中出现的 epsilon 项之秩与次数的函数。换言之，Herbrand 析取的长度，仅取决于所代入项的量词复杂性，与所证明命题的结构或长度完全无关。

本节开头所述的 Herbrand 定理版本，实质上是（2）中公式 $A$ 为存在公式的特殊情形。鉴于这一特殊情形，（1）等价于如下断言：公式 $A$ 在一阶谓词逻辑中可导，当且仅当 $A^H$ 亦可导。这一等价的前向方向容易证明得多；事实上，对任何公式 $A$，$A \rightarrow A^H$ 在谓词逻辑中可导。证明逆向方向涉及消去 $A^H$ 中的附加函数符号，要困难得多，尤其在有等词时。正是在这里，epsilon 方法发挥了核心作用。

给定一个前束公式，**Skolem 范式** $A^S$ 的定义与 $A^H$ 对偶，即通过用见证函数替换存在量化的变项。若 $\Gamma$ 是一组前束语句，令 $\Gamma^S$ 表示其 Skolem 范式的集合。利用演绎定理与 Herbrand 定理，不难证明以下各项两两等价：$$ \begin{align} \Gamma &\text{ 证明 } A \\ \Gamma &\text{ 证明 } A^H \\ \Gamma^S &\text{ 证明 }A \\ \Gamma^S &\text{ 证明 } A^H \end{align} $$

Herbrand 定理及相关方法的一个引人注目的应用，见于 Luckhardt（1989）对 Roth 定理的分析。关于 Herbrand 方法的有用扩展的讨论，见 Sieg 1991。其模型论版本在 Avigad 2002a 中得到讨论。

## 5 Epsilon 替换方法与算术

如上所述，从历史上看，对 epsilon 演算的首要兴趣在于获得一致性证明。希尔伯特 1917–1918 年的讲义已经指出，可以轻松证明命题逻辑的一致性：取命题变项与公式在真值 0 与 1 上取值，把逻辑联结词解释为相应的算术运算。类似地，可以证明谓词逻辑（或纯 epsilon 演算）的一致性，方法是把解释特殊化为论域只有一个元素的情形。这些考量提示了如下更一般的一致性证明纲领：

* 扩充 epsilon 演算，使之表示数学的更大范围。
* 用有穷方法表明，扩充系统中的每个证明都有一个一致的解释。

例如，考虑算术的语言，带有符号 $0$、$1$、$+$、$\times$、$\lt$。除了定义基本符号的无量词公理之外，还可以规定 epsilon 项 $\varepsilon x A(x)$ 挑出满足 $A$ 的最小值（如果存在），用以下公理：$$ \tag{*} A(x) \rightarrow A(\varepsilon x A(x)) \wedge \varepsilon x A(x) \le x $$ 由此得到的系统足以解释一阶（Peano）算术。另一种选择是取 epsilon 符号满足以下公理：$$ A(y) \rightarrow A(\varepsilon x A(x)) \wedge \varepsilon x A(x) \ne y + 1. $$

换言之，如果存在任何满足 $A(y)$ 的见证 $y$，epsilon 项返回一个其前驱不具有同一性质的值。显然，星标公式所描述的 epsilon 项满足备选公理；反之，可以验证：给定 $A$，满足备选公理的 $\varepsilon x (\exists z \le x A(x))$ 的一个值可用来解释 (**) 中的 $\varepsilon x A(x)$。还可以用公理 $$ \varepsilon x A(x) \ne 0 \rightarrow A(\varepsilon x A(x)) $$ 进一步固定 epsilon 项的含义，该公式要求：若 $A$ 没有见证，则 epsilon 项返回 0。但为了下文的讨论，最方便的做法是仅聚焦于 (*)。

假设我们想证明上述系统是一致的；换言之，我们想证明不存在公式 $0 = 1$ 的证明。通过把所有代入推到公理上、并把自由变项替换为常项 0，只需证明：从公理的有限多个闭实例出发，不存在 $0 = 1$ 的命题证明。为此，只需证明：给定任何有限多个公理的闭实例，可以给项指派数值使得所有公理在该解释下为真。由于算术运算 $+$ 与 $\times$ 可以按通常方式解释，唯一的困难在于找到适当的值来指派给 epsilon 项。

希尔伯特的 **epsilon 替换方法** 大致可以描述如下：

* 给定一组有限的公理，先把所有 epsilon 项解释为 0。
* 找一个在该解释下为假的上述公理 (*) 的实例。这只会发生在：有一个项 $t$ 使得 $A(t)$ 在该解释中为真，但 $A(\varepsilon x A(x))$ 为假，或 $t$ 的值小于 $\varepsilon x A(x)$ 的值。
* 通过把 $\varepsilon x A(x)$ 的值改为 $t$ 的值来“修复”该指派，并重复此过程。

一旦以有穷上可接受的方式表明这一逐次“修复”的过程终止，就得到了有穷主义一致性证明。如果确实终止，所有关键公式都是不含 epsilon 项的真公式。

这一基本想法（“希尔伯特式设准”）由希尔伯特在其 1922 年讲演（1923）中首次提出，并在 1922–23 年的讲义中得到 elaboration。不过，那里给出的例子仅处理所有超限公理实例对应于单一 epsilon 项 $\varepsilon x A(x)$ 的证明。挑战在于把这一进路扩展到多个 epsilon 项、嵌套 epsilon 项，并最终扩展到二阶 epsilon（以便获得不仅算术而且分析的一致性证明）。

处理嵌套 epsilon 项的困难可以描述如下。假设证明中的某条公理是超限公理 $$ B(y) \rightarrow B(\varepsilon y B(y)) $$ 当然，$\varepsilon y B(y)$ 可能出现在证明的其他公式中，尤其是其他超限公理中，例如 $$ A(x, \varepsilon y B(y)) \rightarrow A(\varepsilon x A(x, \varepsilon y B(y)), \varepsilon y B(y)) $$ 那么，看来首先需要为 $\varepsilon y B(y)$ 找到正确的解释，然后才尝试为 $\varepsilon x A(x, \varepsilon y B(y))$ 找一个。但是，epsilon 项在证明中的出现还有更复杂的模式。在为 $\varepsilon y B(y)$ 确定正确解释时起作用的一个公理实例可能是 $$ B(\varepsilon x A(x, \varepsilon y B(y))) \rightarrow B(\varepsilon y B(y)) $$ 如果 $B$(0) 为假，则在第一轮中 $\varepsilon y B(y)$ 将被解释为 0。后续把 $\varepsilon x A(x, 0)$ 的解释从 0 改为比如 $n$，将导致该实例被解释为 $B(n) \rightarrow B$(0)，若 $B(n)$ 为真则此式为假。因此 $\varepsilon y B(y)$ 的解释将不得不被修正为 $n$，而这又可能导致 $\varepsilon x A(x, \varepsilon y B(y))$ 的解释不再是真公式。

这只是概略：要把希尔伯特的想法扩展到一般情形，涉及的困难远不止于此。阿克曼（1924）提供了一个这样的推广，使用了一个在给定阶段的新解释需要修正先前阶段已找到的解释时“回溯”的程序。

阿克曼的程序应用于一个二阶算术系统，但二阶项受到限制以排除二阶 epsilon 的交叉约束。这大致相当于把可用的集合形成原理限制为算术概括（参见本节末尾的讨论）。二阶 epsilon 项又显露更多困难，人们很快发现该证明本身站不住脚。然而，在希尔伯特学派的圈子里，直到 1930 年哥德尔宣布其不完备性结果之前，无人意识到困难的程度。在那之前，人们相信该证明（至少经过阿克曼引入的一些修改——其中一些涉及冯·诺依曼（1927）版本的 epsilon 替换方法中的思想）至少会顺利通过一阶部分。希尔伯特与贝奈斯（1939）提出：所用方法只能提供带开放归纳之一阶算术的一致性证明。1936 年，格哈德·根岑成功地在基于不带 epsilon 符号的谓词逻辑的表述中给出了一阶算术一致性的证明。该证明使用了直到 $\varepsilon_0$ 的超限归纳。阿克曼（1940）后来能够改造根岑的想法，用 epsilon 替换方法给出了一阶算术的正确一致性证明。

尽管阿克曼为二阶算术一致性证明所做的尝试没有成功，但这些尝试使人们更清楚地理解了二阶 epsilon 项在数学形式化中的使用。阿克曼使用了二阶 epsilon 项 $\varepsilon f\ A(f)$，其中 $f$ 是函数变项。类比一阶情形，$\varepsilon f\ A(f)$ 是一个使 $A(f)$ 为真的函数，例如 $\varepsilon f (x + f(x) = 2x)$ 是恒等函数 $f(x) = x$。再次类比一阶情形，可以使用二阶 epsilon 来解释二阶量词。特别地，对任何二阶公式 $A(x)$，可以找到项 $t(x)$ 使得 $$ A(x) \leftrightarrow t(x) = 1 $$ 在演算中可导（公式 $A$ 可以有其他自由变项，此时这些变项也出现在项 $t$ 中）。然后可以利用这一事实来解释 **概括** 原理。在带函数符号的语言中，这些采取如下形式 $$ \exists f \forall x (A(x) \leftrightarrow f(x) = 1) $$ 其中 $A(x)$ 为任意公式。概括更常用集合变项来表达，此时它采取如下形式 $$ \exists Y \forall x (A(x) \leftrightarrow x \in Y), $$ 断言每个带参数的二阶公式定义一个集合。

**分析**，即 **二阶算术**，是一阶算术加上任意二阶公式的概括图式的扩充。该理论是 **非直谓的**（impredicative），因为它允许用遍及整个集合宇宙的量词来定义自然数的集合——隐含地包括正在被定义的那个集合。通过限制概括公理中允许的公式类型，可以得到该理论的 **直谓** 片段。例如，上文联系阿克曼讨论的限制对应于 **算术概括图式**，其中公式不涉及二阶量词。有多种方式可以获得分析学的更强片段，但它们仍是直谓地可辩护的。例如，通过给集合变项关联一个序数秩，可以获得 **分层的分析**：大致地说，在定义一个给定秩的集合时，量词只遍及较低秩的集合，即那些定义在逻辑上居先的集合。

**延伸阅读。** 希尔伯特与阿克曼的早期证明在 Zach 2003; 2004 中得到讨论。冯·诺依曼的证明是 Bellotti 2016 的主题。阿克曼 1940 年的证明在 Hilbert & Bernays 1970 与 Wang 1963 中得到讨论。Moser 2006 给出了现代表述。epsilon 替换的一个早期应用是无反例解释（Kreisel 1951）[^kreisel-1951]。

## 6 更晚近的发展

在本节中我们讨论为强系统获得一致性结果的 epsilon 替换方法的发展；这些结果具有数学性质。遗憾的是我们无法在此讨论证明的细节，但想表明 epsilon 替换方法并未随希尔伯特纲领而消亡，而且在 epsilon 形式体系中仍有大量当前研究在进行。

根岑的算术一致性证明开辟了一个被称为 **序数分析** 的研究领域，用序数记号来度量数学理论之强度的纲领至今仍在推进。这对 **扩展的希尔伯特纲领** 尤为相关——其目标是相对于构造性或准构造性系统来为经典数学辩护。根岑的切割消去方法（以及由 Paul Lorentzen、Petr Novikov 和 Kurt Schütte 发展的非直谓逻辑扩展）在很大程度上取代了这些追求中的 epsilon 替换方法。但 epsilon 演算方法提供了另一种进路，而且关于把希尔伯特—阿克曼方法扩展到更强理论的研究仍然活跃。一般模式保持不变：

1. 把所研究的理论嵌入一个适当的 epsilon 演算。
2. 描述一个更新 epsilon 项指派的过程。
3. 证明该程序是规范化的，即给定任何项的集合，存在一列更新，其结果是一个满足公理的指派。

最后一步保证了原理论的一致性。在基础研究看来，人们关心的正是证明规范化所用的方法。例如，通过给程序中的步骤指派序数记号——使得记号的值随每一步递减——可以获得一个 **序数分析**。

在 1960 年代，Tait（1960, 1965, 2010）扩展了阿克曼的方法，获得了带超限归纳原理的算术扩充的序数分析。这一进路的更精炼的现代版本可在 Mints 2001 与 Avigad 2002b 中找到。更近时，Mints、Tupailo 与 Buchholz 考虑了更强的但仍直谓地可辩护的分析学片段，包括算术概括的理论与一个 $\Delta^{1}_1$-概括规则（Mints, Tupailo & Buchholz 1996; Mints & Tupailo 1999；另见 Mints 2016）[^mints-1999]。Arai 2002 已把 epsilon 替换方法扩展到允许沿原始递归良序迭代算术概括的理论。特别地，其工作给出了涉及超限层级与超限归纳的分析学直谓片段的序数分析。

在用 epsilon 替换方法分析 **非直谓** 理论方面已有一些初步步骤（见 Arai 2003, 2006 与 Mints 2015）[^arai-2003][^mints-2015]。

上文步骤 3 的一个变体涉及证明规范化程序对更新的选择不敏感，即 **任何** 更新序列都终止。这被称为 **强规范化。** Mints 1996 已证明所考虑的许多程序具有这种更强的性质。

除证明理论的传统分支及其基础性研究之外，如今人们对 **结构证明理论** 也有很大兴趣——该分支专注于逻辑演绎演算及其性质。这一研究与计算机科学中的相关问题密切相关，涉及自动演绎、函数式编程与计算机辅助验证。在这里，根岑式方法也趋于占主导（再次参见证明理论词条）。但 epsilon 演算也能提供有价值的洞见；参见例如 Aguilera 与 Baaz 2019，或上文对 Herbrand 定理的讨论。

除了证明理论中对 epsilon 演算的探究之外，还应提及两个应用。一是 epsilon 记号在布尔巴基《集合论》（1958）中的使用。二是——也许具有更大的当前意义——epsilon 算子在定理证明系统 [HOL](https://www.cl.cam.ac.uk/Research/HVG/HOL/) 与 [Isabelle](https://www.cl.cam.ac.uk/Research/HVG/Isabelle/) 中的使用，其中 epsilon 项的表达力带来了显著的实践优势。

## 7 语言学、哲学与非经典逻辑中的 Epsilon 算子

把 epsilon 算子读作一个不定选择算子（“一个使得 $A(x)$ 的 $x$”）提示它可能是形式语义学中分析不定与定冠名词短语的有用工具。epsilon 记号事实上已被如此使用，而且这一应用在处理回指语方面证明特别有用。

考虑熟悉的例子

1. 每个拥有驴子的农夫都打它。

这一句子的普遍接受的解释由全称语句给出

1. $\forall x \forall y (\mathrm{Farmer}(x) \wedge \mathrm{Donkey}(y) \wedge \mathrm{Owns}(x, y)) \rightarrow \mathrm{Beats}(x, y))$

缺点在于“一头驴子”暗示一个存在量词，因而该分析应当在形式上与语句 3 被语句 4 给出的分析相平行：

1. 每个拥有驴子的农夫都是快乐的，
2. $\forall x (\mathrm{Farmer}(x) \wedge \exists y (\mathrm{Donkey}(y) \wedge \mathrm{Owns}(x, y)) \rightarrow \mathrm{Happy}(x))$，

但最接近的可能形式化

1. $\forall x ((\mathrm{Farmer}(x) \wedge \exists y (\mathrm{Donkey}(y) \wedge \mathrm{Owns}(x, y)) \rightarrow \mathrm{Beats}(x, y))$

包含 $y$ 的一个自由出现。Evans 1980 建议，由于代词是指称表达，应当把它们分析为确定摹状词；如果代词出现在条件句的后件中，则描述性条件由前件决定。这导向了（1）的如下 E-型分析：$$ \begin{align*} & &\forall x ((\mathrm{Farmer}(x) \wedge \exists y (\mathrm{Donkey}(y) \wedge \mathrm{Owns}(x, y)) \rightarrow\\ & &(\mathrm{Beats}(x, \iota y (\mathrm{Donkey}(y) \wedge \mathrm{Owns}(x, y))) \end{align*} $$ 此处，$\iota x$ 是确定摹状词算子，$\iota y (\mathrm{Donkey}(y) \wedge \mathrm{Owns}(x, y))$ 是“$x$ 所拥有的那头驴子”。麻烦在于，按标准分析，确定摹状词带有唯一性条件，因此（5）在有一个农夫拥有多于一头驴子时将为假。一条出路是引入一个新算子 whe（whoever, whatever），它充当一个广义量词（Neale, 1990）：

$$ \begin{align*} & &\forall x ((\mathrm{Farmer}(x) \wedge \exists y (\mathrm{Donkey}(y) \wedge \mathrm{Owns}(x, y)) \rightarrow\\ & & (\mathrm{Beats}(x, \mathrm{whe}\, y (\mathrm{Donkey}(y) \wedge \mathrm{Owns}(x, y))) \end{align*} $$

正如 von Heusinger（1994）指出的，这暗示 Neale 承诺了代词在确定摹状词（$\iota$-表达式）与 whe-表达式之间是歧义的。Heusinger 建议改用由选择函数（取决于语境）索引的 epsilon 算子。按照这一进路，（1）的分析为

> 对每个选择函数 $i$：$$\begin{align*} & &\forall x ((\mathrm{Farmer}(x) \wedge \mathrm{Owns}(x, \varepsilon_i y \mathrm{Donkey} (y)) \rightarrow \\ & &\mathrm{Beats} (x, \varepsilon_{a^*}y \mathrm{Donkey} (y)) \end{align*} $$

此处 $a^**$ 是一个选择函数，它依赖于 $i$ 与条件句的前件：如果 $i$ 是从所有驴子的集合中选出 $\varepsilon_i y \mathrm{Donkey}(y)$ 的选择函数，则 $\varepsilon_{a^**}y \mathrm{Donkey} (y)$ 从 $x$ 所拥有的驴子的集合中选出。

这种使用由选择函数索引的 epsilon 算子来处理代词的进路，使 von Heusinger 得以处理各种各样的情形（见 Egli 与 von Heusinger 1995; von Heusinger 2000）[^egli-1995][^heusinger-2000][^heusinger-2000-2]。

形式语义学中 epsilon 算子的应用，以及广义的选择函数，已经受到语言学家的重大关注。Von Heusinger 与 Egli 2000a 列举了以下几种：问题的表示（Reinhart 1992）[^reinhart-1992]、特称不定词（Reinhart 1992; 1997; Winter 1997）[^reinhart-1992][^winter-1997]、E-型代词（Hintikka 与 Kulas 1985; Slater 1986; Chierchia 1992, Egli 与 von Heusinger 1995）[^chierchia-1992][^egli-1995][^hintikka-1985][^slater-1986]以及确定名词短语（von Heusinger 1997, 2004）[^heusinger-1997]。Gratzl 与 Schiemer 2017 提供了罗素与希尔伯特处理不定词方式的比较。

关于 epsilon 算子在语言学与语言哲学中的议题与应用的讨论，见 B. H. Slater 的 epsilon 演算文章（在下文其他网络资源节中引用），以及文集 von Heusinger 与 Egli 2000 和 von Heusinger 与 Kempson 2004。

epsilon 演算的另一应用是作为关于任意对象的推理的一般逻辑。Meyer Viol 1995a 提供了 epsilon 演算与 Fine 1985 任意对象理论的比较。事实上，这一联系不难看到。给定等价 $\forall x A(x) \equiv$ A$(\varepsilon x (\neg A))$，项 $\varepsilon x (\neg A)$ 是一个任意对象，其意义在于它是一个使 $A$ 为真当且仅当 $A$ 一般地为真的对象。$\varepsilon$-项与 Fine 任意对象理论之间的联系被 Bonatti 2022（数学中的抽象）和 Sandu 2020（不定词）用于哲学目的。

在其 1961 年的著作中，卡尔纳普建议使用 $\varepsilon$-算子来重构科学理论的理论部分（一个类似于拉姆齐化的提议；参见科学中的理论词条及[卡尔纳普词条的补充 E](https://plato.stanford.edu/entries/carnap/reconstruct-sci-theories.html#TheoTermSentLogiStruTheo)）。这一提议由 Schiemer 与 Gratzl 2016 讨论。Leitgeb 2023 在不确定性语义学的语境中考虑了拉姆齐语句的 $\varepsilon$-版本。

Meyer Viol 的论文 1995a, 1995b 包含 epsilon 演算的进一步的证明论与模型论研究，特别是直觉主义 epsilon 演算。在这种演算中，epsilon 定理不再成立，即 epsilon 项的引入产生直觉主义逻辑的非保守扩充。对直觉主义逻辑中 epsilon 算子的其他研究可见 Shirai 1971, Bell 1993a, 1993b, DeVidi 1995 以及 Baaz 与 Zach 2022。多值逻辑中的 epsilon 算子见 Mostowski 1963；模态 epsilon 演算见 Fitting 1975。

## 参考文献

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## 学术工具

> | | [如何引用本词条](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=epsilon-calculus). |
> | --- | ----------------------------------------------------------------------------------------------------------------------------------- |
> | | [预览本词条的 PDF 版本](https://leibniz.stanford.edu/friends/preview/epsilon-calculus/)（[SEP 之友学会](https://leibniz.stanford.edu/friends/)）. |
> | | [查找与本词条相关的话题与思想家](https://www.inphoproject.org/entity?sep=epsilon-calculus&redirect=True)（互联网哲学本体论项目，InPhO）. |
> | | [本词条的增强文献目录](https://philpapers.org/sep/epsilon-calculus/)（[PhilPapers](https://philpapers.org/)），含其数据库链接. |

## 其他网络资源

* [Epsilon Calculi](http://www.utm.edu/research/iep/e/ep-calc.htm) by B. Hartley Slater (Internet Encyclopedia of Philosophy).

Please contact the authors with further suggestions.

## 相关词条

anaphora | finitism | Hilbert, David | Hilbert, David: program in the foundations of mathematics | logic: classical | mathematics, philosophy of | proof theory | quantifiers and quantification | theoretical terms in science

[^aguilera-2019]: Aguilera, J.P., and M. Baaz, 2019, ‘Unsound inferences make proofs shorter’. *Journal of Symbolic Logic*, 84: 102–122.

[^ackermann-1924]: Ackermann, W., 1924, ‘Begründung des ’’tertium non datur’’ mittels der Hilbertschen Theorie der Widerspruchsfreiheit’, *Mathematische Annalen*, 93: 1–36.

[^ackermann-1937]: –––, 1937–38, ‘Mengentheoretische Begründung der Logik’, *Mathematische Annalen*, 115: 1–22.

[^ackermann-1940]: –––, 1940, ‘Zur Widerspruchsfreiheit der Zahlentheorie’, *Mathematische Annalen*, 117: 162–194.

[^arai-2002]: Arai, T., 2002, ‘Epsilon substitution method for theories of jump hierarchies’, *Archive for Mathematical Logic*, 2: 123–153.

[^arai-2003]: –––, 2003, ‘Epsilon substitution method for ID$_1 (\Pi^{0}_1 \vee \Sigma^{0}_1)$’, *Annals of Pure and Applied Logic*, 121: 163–208.

[^arai-2006]: –––, 2006, ‘Epsilon substitution method for $\Pi^{0}_2$-FIX. *Journal of Symbolic Logic*, 71: 1155–1188

[^avigad-2002a]: Avigad, J., 2002a, ‘Saturated models of universal theories’, *Annals of Pure and Applied Logic*, 118: 219–234.

[^avigad-2002b]: –––, 2002b, ‘Update procedures and the 1-consistency of arithmetic’, *Mathematical Logic Quarterly*, 48: 3–13.

[^baaz-2018]: Baaz, M., A. Leitsch, and A. Lolic, 2018, ‘A sequent-calculus based formulation of the extended first epsilon theorem’, in: Artemov, S., Nerode, A. (eds.), *Logical Foundations of Computer Science*, Berlin: Springer, 55–71.

[^baaz-2022]: Baaz, M., and R. Zach, 2022, ‘Epsilon theorems in intermediate logics’, *The Journal of Symbolic Logic*, 87(2): 682–720.

[^bell-1993a]: Bell, J. L., 1993a. ‘Hilbert’s epsilon-operator and classical logic’, *Journal of Philosophical Logic*, 22: 1–18.

[^bell-1993b]: –––, 1993b. ‘Hilbert’s epsilon operator in intuitionistic type theories’, *Mathematical Logic Quarterly*, 39: 323–337.

[^bellotti-2016]: Bellotti, L., 2016, ‘Von Neumann’s consistency proof’, *Review of Symbolic Logic*, 9: 429–455.

[^bonatti-2022]: Bonatti, N., 2022, ‘A reassessment of cantorian abstraction based on the ε-operator’, *Synthese*, 200(5): 396.

[^bourbaki-1958]: Bourbaki, N., 1958, *Theorie des ensembles*, Paris: Hermann.

[^buss-1995]: Buss, S., 1995, ‘On Herbrand’s theorem’, *Logic and Computational Complexity* (Lecture Notes in Computer Science 960), Berlin: Springer, 195–209.

[^buss-1998]: ––– 1998, ‘Introduction to proof theory’, in: Buss (ed.), *The Handbook of Proof Theory*, Amsterdam: North-Holland, 1–78.

[^chierchia-1992]: Chierchia, G., 1992, ‘Anaphora and dynamic logic’. *Linguistics and Philosophy*, 15: 111–183.

[^davis-1991]: Davis, M., and R. Fechter, 1991, ‘A free variable version of the first-order predicate calculus’, *Journal of Logic and Computation*, 1: 431–451.

[^devidi-1995]: DeVidi, D., 1995, ‘Intuitionistic $\varepsilon$- and $\tau$-calculi’, *Mathematical Logic Quarterly*, 41: 523–546.

[^egli-1995]: Egli, U., and K. von Heusinger, 1995, ‘The epsilon operator and E-type pronouns’, in U. Egli *et al*. (eds.), *Lexical Knowledge in the Organization of Language*, Amsterdam: Benjamins, 121–141 (Current Issues in Linguistic Theory 114).

[^evans-1980]: Evans, G., 1980, ‘Pronouns’, *Linguistic Inquiry*, 11: 337–362.

[^ewald-1996]: Ewald, W. B. (ed.), 1996, *From Kant to Hilbert. A Source Book in the Foundations of Mathematics*, Vol. 2, Oxford: Oxford University Press.

[^ferrari-1987]: Ferrari, P. L., 1987, ‘A note on a proof of Hilbert’s second $\varepsilon$-theorem’, *Journal of Symbolic Logic*, 52: 214–215.

[^fine-1985]: Fine, K., 1985, *Reasoning with Arbitrary Objects*, Oxford: Blackwell.

[^fitting-1975]: Fitting, M., 1975, ‘A modal logic epsilon-calculus’, *Notre Dame Journal of Formal Logic*, 16: 1–16.

[^flannagan-1975]: Flannagan, T. B., 1975, ‘On an extension of Hilbert’s second $\varepsilon$-theorem’, *Journal of Symbolic Logic*, 40: 393–397.

[^genco-2021]: Genco, F. A., F. Poggiolesi, and L. Rossi, 2021, ‘Grounding, quantifiers, and paradoxes’, *Journal of Philosophical Logic*, 50(6): 1417–1448.

[^girard-1982]: Girard, J.-Y., 1982, ‘Herbrand’s theorem and proof theory’, *Proceedings of the Herbrand Symposium*, Amsterdam: North-Holland, 29-38.

[^gratzl-2017]: Gratzl, N., and G. Schiemer, 2017, ‘Two types of indefinites: Hilbert & Russell’, *IfCoLog Journal of Logics and Their Applications*, 4(2): 333–348.

[^herbrand-1930]: Herbrand, J., 1930, *Recherches sur la thèorie de la dèmonstration*, *Dissertation*, University of Paris. English translation in Herbrand 1971, pp. 44–202.

[^herbrand-1971]: –––, 1971, *Logical Writings*, W. Goldfarb (ed.), Cambridge, Mass.: Harvard University Press.

[^hilbert-1922]: Hilbert, D., 1922, ‘Neubegründung der Mathematik: Erste Mitteilung’, *Abhandlungen aus dem Seminar der Hamburgischen Universität*, 1: 157–177, English translation in Mancosu, 1998, 198–214 and Ewald, 1996, 1115–1134.

[^hilbert-1923]: –––, 1923, ‘Die logischen Grundlagen der Mathematik’, *Mathematische Annalen*, 88: 151–165; English translation in Ewald, 1996, 1134–1148.

[^hilbert-1934]: Hilbert, D., and P. Bernays, 1934, *Grundlagen der Mathematik* (Volume 1), Berlin: Springer.

[^hilbert-1939]: –––, 1939, *Grundlagen der Mathematik* (Volume 2), Berlin: Springer.

[^hilbert-1970]: –––, 1970, ‘Grundlagen der Mathematik’ (Volume 2), 2nd, edition, Berlin: Springer, Supplement V.

[^hintikka-1985]: Hintikka, J., and J. Kulas, 1985, *Anaphora and Definite Descriptions: Two Applications of Game-Theoretical Semantics*, Dordrecht: Reidel.

[^kempson-2001]: Kempson, R., W. Meyer Viol, and D. Gabbay, 2001, *Dynamic Syntax: The Flow of Language Understanding*, Oxford: Blackwell.

[^kreisel-1951]: Kreisel, G, 1951, ‘On the interpretation of non-finitist proofs – part I’, *Journal of Symbolic Logic*, 16: 241–267.

[^leisenring-1969]: Leisenring, A. C., 1969, *Mathematical Logic and Hilbert’s Epsilon-Symbol*, London: Macdonald.

[^leitgeb-2023]: Leitgeb, H., 2023, ‘Ramsification and semantic indeterminacy’, *The Review of Symbolic Logic*, 16(3): 900–950.

[^luckhardt-1989]: Luckhardt, H., 1989, ‘Herbrand-Analysen zweier Beweise des Satzes von Roth: Polynomiale Anzahlschranken’, *Journal of Symbolic Logic*, 54: 234–263.

[^maehara-1955]: Maehara, S., 1955, ‘The predicate calculus with $\varepsilon$-symbol’, *Journal of the Mathematical Society of Japan*, 7: 323–344.

[^maehara-1957]: –––, 1957, ‘Equality axiom on Hilbert’s $\varepsilon$-symbol’, *Journal of the Faculty of Science*, University of Tokyo, Section 1, 7: 419–435.

[^mancosu-1998]: Mancosu, P. (ed.), 1998, *From Brouwer to Hilbert. The Debate on the Foundations of Mathematics in the 1920s*, Oxford: Oxford University Press.

[^meyer-1995a]: Meyer Viol, W. P. M., 1995a, *Instantial Logic. An Investigation into Reasoning with Instances*, Ph.D. thesis, University of Utrecht. ILLC Dissertation Series 1995–11.

[^meyer-1995b]: –––, 1995b. ‘A proof-theoretic treatment of assignments’, *Bulletin of the IGPL*, 3: 223–243.

[^mints-1994]: Mints, G., 1994, ‘Gentzen-type systems and Hilbert’s epsilon substitution method. I’, *Logic, Methodology and Philosophy of Science, IX* (Uppsala, 1991), Amsterdam: North-Holland, 91-122.

[^mints-1996]: –––, 1996, ‘Strong termination for the epsilon substitution method’, *Journal of Symbolic Logic*, 61: 1193–1205.

[^mints-2001]: –––, 2001, ‘The epsilon substitution method and continuity’, in W. Sieg *et al*. (eds.), *Reflections on the Foundations of Mathematics: Essays in Honor of Solomon Feferman*, Lecture Notes in Logic 15, Association for Symbolic Logic.

[^mints-2008]: –––, 2008, ‘Cut Elimination for a simple formulation of epsilon calculus’, *Annals of Pure and Applied Logic*,152 (1–3): 148–160.

[^mints-2013]: –––, 2013, ‘Epsilon substitution for first- and second-order predicate logic’, *Annals of Pure and Applied Logic*, 164: 733–739.

[^mints-2015]: –––, 2015, ‘Non-deterministic epsilon substitution method for PA and ID$_1$’, in: Kahle, R., Rathjen, M. (Eds.), *Gentzen’s Centenary: The Quest for Consistency*, Berlin: Springer, pp. 479–500.

[^mints-1999]: Mints, G., and S. Tupailo, 1999, ‘Epsilon-substitution method for the ramified language and $\Delta^{1}_1$-comprehension rule’, in A. Cantini *et al*. (eds.), *Logic and Foundations of Mathematics* (Florence, 1995), Dordrecht: Kluwer, 107–130.

[^mints-1996-2]: Mints, G., S. Tupailo, and W. Buchholz, 1996, ‘Epsilon substitution method for elementary analysis’, *Archive for Mathematical Logic*, 35: 103–130.

[^miyamoto-2024]: Miyamoto, K., and G. Moser, 2024, ‘Herbrand complexity and the epsilon calculus with equality’, *Archive for Mathematical Logic*, 63(1): 89–118.

[^moser-2006]: Moser, G., 2006, ‘Ackermann’s substitution method (remixed)’, *Annals of Pure and Applied Logic*, 142(1–3): 1–18.

[^moser-2006-2]: Moser, G., and R. Zach, 2006, ‘The epsilon calculus and Herbrand complexity’, *Studia Logica*, 82(1): 133–155.

[^mostowski-1963]: Mostowski, A., 1963, ‘The Hilbert epsilon function in many-valued logics’, *Acta Philosophica Fennica*, 16: 169–188.

[^neale-1990]: Neale, S., 1990, *Descriptions*, Cambridge, MA: MIT Press.

[^reinhart-1992]: Reinhart, T., 1992, ‘Wh-in-situ: An apparent paradox’, in P. Dekker and M. Stokhof (eds.). *Proceedings of the Eighth Amsterdam Colloquium*, December 17–20, 1991, ILLC, University of Amsterdam, 483–491.

[^reinhart-1997]: –––, 1997, ‘Quantifier scope: How labor is divided between QR and choice functions’. *Linguistics and Philosophy*, 20: 335–397.

[^sandu-2020]: Sandu, G., 2020, ‘Indefinites, Skolem functions, and arbitrary objects’, in M. Dumitru (ed.), *Metaphysics, Meaning, and Modality: Themes from Kit Fine*, Oxford: Oxford University Press, 98–112.

[^schiemer-2016]: Schiemer, G., and N. Gratzl, 2016, ‘The epsilon-reconstruction of theories and scientific structuralism’, *Erkenntnis*, 81(2): 407–432.

[^shirai-1971]: Shirai, K., 1971, ‘Intuitionistic predicate calculus with $\varepsilon$-symbol’, *Annals of the Japan Association for Philosophy of Science*, 4: 49–67.

[^sieg-1991]: Sieg, W., 1991, ‘Herbrand analyses’, *Archive for Mathematical Logic*, 30: 409–441.

[^slater-1986]: Slater, B. H., 1986, ‘E-type pronouns and $\varepsilon$-terms’, *Canadian Journal of Philosophy*, 16: 27–38.

[^slater-1988]: –––, 1988, ‘Hilbertian reference’, *Noûs*, 22: 283–97.

[^slater-1994]: –––, 1994, ‘The epsilon calculus’ problematic’, *Philosophical Papers*, 23: 217–42.

[^slater-2000]: –––, 2000, ‘Quantifier/variable-binding’, *Linguistics and Philosophy*, 23: 309–21.

[^tait-1960]: Tait, W. W., 1960, ‘The substitution method.’ *Journal of Symbolic Logic*, 30: 175–192.

[^tait-1965]: –––, 1965, ‘Functionals defined by transfinite recursion,’ *Journal of Symbolic Logic*, 30: 155–174.

[^tait-2010]: –––, 2010, ‘The substitution method revisited.’ in: S. Feferman and W. Sieg (eds.), *Proofs, Categories and Computations: Essays in Honor of Grigori Mints*, London: College Publications, pp. 131–14.

[^heusinger-1994]: von Heusinger, K., 1994, Review of Neale (1990). *Linguistics*, 32: 378–385.

[^heusinger-1997]: –––, 1997, ‘Definite descriptions and choice functions’, in S. Akama (ed.). *Logic, Language and Computation*, Dordrecht: Kluwer, 61–91.

[^heusinger-2000]: –––, 2000, ‘The Reference of Indefinites’, in von Heusinger and Egli, (2000), 265–284.

[^heusinger-2004]: –––, 2004, ‘Choice functions and the anaphoric semantics of definite NPs’, *Research in Language and Computation*, 2: 309–329.

[^heusinger-2000-2]: von Heusinger, K., and U. Egli (eds.), 2000, *Reference and Anaphoric Relations*, Dordrecht: Kluwer.

[^heusinger-2000a]: –––, 2000a. ‘Introduction: Reference and the Semantics of Anaphora’, in von Heusinger and Egli (2000), 1–13.

[^heusinger-2004-2]: von Heusinger, K., and R. Kempson (eds.), 2004, *Choice Functions in Semantics*, Special Issue of *Research on Language and Computation*, 2(3).

[^neumann-1927]: von Neumann, J., 1927, ‘Zur Hilbertschen Beweistheorie’, *Mathematische Zeitschrift*, 26: 1–46.

[^wang-1963]: Wang, H., 1963, *A Survey of Mathematical Logic*, Peking: Science Press.

[^winter-1997]: Winter, Y., 1997, ‘Choice functions and the scopal semantics of indefinites’. *Linguistics and Philosophy*, 20: 399–467.

[^yasuhara-1982]: Yasuhara, M., 1982, ‘Cut elimination in $\varepsilon$-calculi’, *Zeitschrift für mathematische Logik und Grundlagen der Mathematik*, 28: 311–316.

[^zach-2003]: Zach, R., 2003, ‘The practice of finitism. Epsilon calculus and consistency proofs in Hilbert’s Program’, *Synthese*, 137: 211–259.

[^zach-2004]: –––, 2004, ‘Hilbert’s “*Verunglückter Beweis*”, the first epsilon theorem, and consistency proofs’. *History and Philosophy of Logic*, 25: 79–94.

[^zach-2017]: –––, 2017, ‘Semantics and proof theory of the epsilon calculus’, in: Ghosh, S., Prasad, S. (Eds.), *Logic and Its Applications. ICLA 2017*, LNCS. Springer, Berlin, Heidelberg, pp. 27–47.
