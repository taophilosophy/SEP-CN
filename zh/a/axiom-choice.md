# 选择公理 The Axiom of Choice (John L. Bell)

> *首次发表于 2008 年 1 月 8 日；实质修订于 2021 年 12 月 10 日。*

## 1. 选择公理的起源与年表

1904 年，Ernst Zermelo 以一种他称为 **覆盖**（coverings）的方式表述了选择公理（本文通篇简称 *AC*）（Zermelo 1904）[^zermelo-1904]。他先从任意集合 $M$ 出发，用符号 $M'$ 表示 $M$ 的任意非空子集，并把它们的汇集记作 M。他接着写道：

> 设想每个子集 $M'$ 都配定一个出现在 $M'$ 自身之中的任意元素 $m_{1}'$；称 $m_{1}'$ 为 $M'$ 的“特异”（distinguished）元素。这就得到由集合 $M$ 的某些元素对集合 $M$ 所作的一个“覆盖” $g$。这些覆盖的数目等于［所有子集 $M'$ 的基数之］积，并且肯定不为 0。

这段引文的最后一句——它实际上断言，对任何（非空）集合的非空子集汇集，覆盖总是存在——是 Zermelo 对选择公理的第一个表述[^note-1]。这一表述如今通常用 **选择函数** 来陈述：非空集合族 $\mathcal{H}$ 上的选择函数，是一个定义域为 $\mathcal{H}$ 的映射 $f$，使得对每个 $X \in \mathcal{H}$ 都有 $f(X) \in X$。

举一个很简单的例子：令 $\mathcal{H}$ 为 $\{0, 1\}$ 的非空子集构成的汇集，即 $\mathcal{H} = \{\{0\}, \{1\}, \{0,1\}\}$。于是 $\mathcal{H}$ 有两个不同的选择函数 $f_{1}$ 与 $f_{2}$，由下式给出：

$$\begin{align} f_{1}(\{0\}) &= 0 \\ f_{1}(\{1\}) &= 1 \\ f_{1}(\{0, 1\}) &= 0 \\ f_{2}(\{0\}) &= 0 \\ f_{2}(\{1\}) &= 1 \\ f_{2}(\{0, 1\}) &= 1 \end{align}$$

另一个更有意思的选择函数例子是：取 $\mathcal{H}$ 为实数无序对的集合，取那个为每一对指定其最小元素的函数。若为每一对指定其最大元素，就得到另一个不同的选择函数。显然，$\mathcal{H}$ 上还能定义多得多的选择函数。

用选择函数来陈述，Zermelo 对 *AC* 的第一个表述是：

**AC1**：任何非空集合族都有一个选择函数。

**AC1** 也可以用 **索引集族** 或 **变元集** 来重新表述。集合的索引集族 $\mathcal{A} = \{A_{i}: i \in I\}$ 可以设想为一个 **变元集**，即一个在索引集 $I$ 上 **变动** 的集合。此时每个 $A_{i}$ 都是变元集 $\mathcal{A}$ 在 **阶段** $i$ 的“值”。$\mathcal{A}$ 上的 **选择函数** 是一个映射 $f: I \rightarrow \bigcup_{i\in I} A_{i}$，使得对所有 $i\in I$ 都有 $f(i) \in A_{i}$。于是 $\mathcal{A}$ 上的选择函数就是在每一阶段对变元集 $\mathcal{A}$ 的某个元素作出的“选择”；换言之，$\mathcal{A}$ 上的选择函数是 $\mathcal{A}$ 的一个 **可变元素**。**AC1** 于是等价于下述断言：

**AC2**：任何集合的索引集族都有一个选择函数。

非正式地说，**AC2** 相当于断言：一个在每一阶段都有元素的变元集有一个可变元素。

**AC1** 也可以用关系来重新表述，即：

**AC3**：对集合 $A$ 与 $B$ 之间的任何关系 $R$，

$$ {\forall x\in A}\ \exists y\in B[R(x,y)] \Rightarrow \exists f[f: A \rightarrow B \mathbin{\&} {\forall x\in A}[R(x,fx)]]. $$

换言之，每个关系都包含一个具有相同定义域的函数。

最后，**AC3** 很容易被证明（在通常的集合论中）等价于：[^note-2]

**AC4**：任何满射函数都有右逆。

在 1908 年的一篇论文中，Zermelo 引入了 *AC* 的一种修正形式。我们称集合族 $\mathcal{H}$ 的一个 **横截集**（或 **选择集**）为任一子集 $T \subseteq \bigcup \mathcal{H}$，使得对每个 $X \in \mathcal{H}$，交集 $T \cap X$ 恰有一个元素。举一个很简单的例子：令 $\mathcal{H} = \{\{0\}, \{1\}, \{2, 3\}\}$，则 $\mathcal{H}$ 有两个横截集 $\{0, 1, 2\}$ 与 $\{0, 1, 3\}$。一个更实在的例子是：令 $\mathcal{H}$ 为欧几里得平面中所有平行于 $x$ 轴的直线构成的汇集。此时 $y$ 轴上的点集 $T$ 就是 $\mathcal{H}$ 的一个横截集。

那么，用横截集来陈述，Zermelo 的第二个（1908 年）表述就相当于断言：任何两两不交的非空集合族都有一个横截集。[^note-3]

Zermelo 断言，这一原则“纯客观的特性”“是显而易见的”。作出这一断言时，Zermelo 意在强调：在这一形式下，该原则并未诉诸作出“选择”的可能性。也可能 Zermelo 心中想的是下面这个对该原则的“组合”辩护。给定一个两两不交的非空集合族 $\mathcal{H}$，称子集 $S \subseteq \bigcup \mathcal{H}$ 为 $\mathcal{H}$ 的 **选择子**，如果对所有 $X \in \mathcal{H}$ 都有 $S\cap X \ne \varnothing$。显然 $\mathcal{H}$ 的选择子是存在的；$\bigcup \mathcal{H}$ 本身就是一例。现在可以设想取 $\mathcal{H}$ 的一个选择子 $S$，并“削薄”每个交集 $S \cap X$（其中 $X\in \mathcal{H}$），直到它只含一个元素。结果便是 $\mathcal{H}$ 的一个横截集。这一论证经适当精化，就从称为 **佐恩引理** 的集合论原则（见下文）给出了这一形式下 *AC* 的精确推导。

我们称 Zermelo 1908 年的表述为 **组合** 形式的选择公理：

**CAC**：任何两两不交的非空集合族都有一个横截集。

应当注意，对于 **有限** 的集合族，**AC1** 与 **CAC** 在通常的集合论中都是可证的（用归纳法）。但对于 **无限** 族，即便其每个成员都是有限的，选择函数或横截集的存在性问题也是成问题的[^note-4]。例如，如前所述，为实数对族找一个选择函数很容易（只需选出每一对中较小的元素）。但是，要为任意实数集合组成的无序对构成的族给出一个选择函数，却绝非显然。

Zermelo 引入 *AC* 的初衷，是要确立 Cantor 集合论的一条核心原则，即每个集合都容许一个良序，因而也可以被指派一个基数。Zermelo 1904 年对这一公理的引入，以及他对它的使用，招致了当时数学家的相当多批评。主要反对意见针对的是某些人眼中的该公理高度非构造性、甚至唯心主义的特征：该公理断言可以作出若干——甚至可能不可数多个——任意的“选择”，却丝毫没有说明这些选择实际上如何实现，换言之，丝毫没有说明选择函数如何被 **定义**。这一点对具有“构造”倾向的数学家尤其难以接受，例如所谓的法国经验论者 Baire、Borel 与 Lebesgue；在他们看来，一个数学对象只有能被如此定义以致唯一地刻画它时，才能被断言存在。Zermelo 对批评者的回应见于 1908 年的两篇论文。在第一篇中，如上所述，他用横截集重新表述了 *AC*；在第二篇（1908a）中，他明确给出了完成其良序定理证明所需的进一步假设。这些假设构成了对集合论公理系统的首次明确陈述。

随着关于选择公理的争论持续发酵，人们渐渐看清楚：若干重要数学定理的证明都本质地用到它，从而使许多数学家把它当作本行不可或缺的工具。例如 Hilbert 逐渐把 *AC* 视为数学的一条本质性原则[^note-5]，并在为经典数学推理辩护、反驳直觉主义者攻击时使用了它。事实上，他的 ε 算子本质上就是选择函数（见“ε 演算”词条）。

尽管 *AC* 的有用性很快就变得清楚，关于其可靠性的疑虑却依然存在。这些疑虑因它具有某些极其反直觉的推论而得到加强。其中最引人注目的是 Banach 与 Tarski 的 **球体悖论分解**（Banach and Tarski 1924）[^banach-1924]：任何实心球都可被分成有限多块，这些块可重新拼合成两个同样大小的实心球；并且任何实心球都可被分成有限多块，使得它们能重新拼合成一个任意大小的实心球。（见 Wagon 1993。）[^wagon-1993]

直到 1930 年代中期，*AC* 的可靠性问题才因 Kurt Gödel 证明它相对于集合论其余公理是相容的而最终尘埃落定。

下面是与 *AC* 有关的简略年表：[^note-6]

| 1904/1908 | Zermelo 引入集合论公理，明确表述 *AC* 并用它证明良序定理，由此掀起了一场争论风暴。 |
| --- | --- |
| 1904 | Russell 认识到 *AC* 即 **乘法公理**：任意非零基数的乘积非零。 |
| 1914 | Hausdorff 由 *AC* 推出不可测集的存在，其“悖论”形式为：球体的 ${^{1}\unicode{x2044}_{2}}$ 与它的 ${^{1}\unicode{x2044}_{3}}$ 全等（Hausdorff 1914）[^hausdorff-1914]。 |
| 1922 | Fraenkel 引入“置换法”，以证明 *AC* 相对于带原子的集合论系统的独立性（Fraenkel 1922）[^fraenkel-1922]。 |
| 1924 | 在 Hausdorff 工作的基础上，Banach 与 Tarski 由 *AC* 推出他们的球体悖论分解。 |
| 1926 | Hilbert 在其证明论中引入“超限”或“ε”公理，作为 *AC* 的一个版本。（Hilbert 1926）[^hilbert-1926]。 |
| 1936 | Lindenbaum 与 Mostowski 推广并精化了 Fraenkel 的置换法，证明了若干弱于 *AC* 的集合论陈述的独立性。（Lindenbaum and Tarski 1938）[^lindenbaum-1938] |
| 1935–38 | Gödel 确立了 *AC* 与集合论公理的相对相容性（Gödel 1938a, 1938b, 1939, 1940）[^gödel-1938a][^gödel-1938b][^gödel-1940]。 |
| 1950s | Mendelson、Shoenfield 与 Specker 各自独立地运用置换法，确立了 *AC* 各种形式相对于不含原子、但也缺少基础公理的集合论系统的独立性（Mendelson 1956, 1958, Shoenfield 1955, Specker 1957）[^mendelson-1956][^mendelson-1958][^shoenfield-1955][^specker-1957]。 |
| 1963 | Paul Cohen 证明 *AC* 相对于集合论标准公理的独立性（Cohen 1963, 1964）[^cohen-1963][^cohen-1964]。 |

## 2. 选择公理的独立性与相容性

如前所述，1922 年 Fraenkel 证明了 *AC* 相对于一个含有“原子”的集合论系统的独立性。这里所谓 **原子**（atom），指的是一个纯粹的个体，即一个没有成员、却又区别于空集的实体（因此 *a fortiori* 原子不可能是集合）。在带原子的集合论系统中，假定给定了一个由原子构成的无限集 $A$。人们可以从 $A$ 出发，先加入 $A$ 的一切子集，再加入所得结果的一切子集，如此等等，并超限地迭代下去，从而在 $A$ 之上构造出一个集合的宇宙 $V(A)$。于是 $V(A)$ 就是带原子的集合论的一个模型。Fraenkel 证明 *AC* 独立性之方法的核心在于这样一个观察：既然原子无法在集合论上被区分，那么原子集 $A$ 的任一置换都会诱导出由 $A$ 构造的集合宇宙 $V(A)$ 的一个保结构置换——一个 **自同构**。这一想法可用来构造集合论的另一个模型 $Sym(V)$——一个 **置换模型** 或 **对称模型**——在其中，由 $A$ 的元素构成的、彼此不交的对所组成的集合没有选择函数。

现在假定给定 $A$ 的一个自同构群 $G$。我们说 $A$ 的一个自同构 *π* **固定** $V(A)$ 的一个元素 $x$，如果 $\pi(x) = x$。显然，若 $\pi \in G$ 固定 $A$ 的每个元素，则它也固定 $V(A)$ 的每个元素。现在可能出现这样的情况：对某些元素 $x \in V(A)$，只要任一 $\pi\in G$ 固定 $A$ 的某个 **子集** 的元素，就足以固定 $x$。于是我们不妨把 $x$ 的一个 **支撑** 定义为 $A$ 的一个子集 $X$，使得只要 $\pi\in G$ 固定 $X$ 的每个成员，它也就固定 $x$。$V(A)$ 中具有 **有限** 支撑的成员称为 **对称的**。

我们接下来把宇宙 $Sym(V)$ 定义为由 $V(A)$ 中 **遗传对称的** 成员组成，即那些 $x\in V(A)$，使得 $x$、$x$ 的元素、$x$ 的元素的元素等等全都是对称的。$Sym(V)$ 也是以 $A$ 为原子集的集合论的一个模型，而 *π* 诱导出 $Sym(V)$ 的一个自同构。

现在设 $A$ 被划分成一个（必然无限的）由两两不交的对构成的族 $P$。取 $G$ 为 $A$ 的、固定 $P$ 中所有对的一切置换所构成的群。于是 $P\in Sym(V)$；此时可以证明，$Sym(V)$ 中不含 $P$ 上的任何选择函数。因为，假定 $f$ 是 $P$ 上的一个选择函数且 $f \in Sym(V)$。那么 $f$ 有一个有限支撑，不妨取为形如 $\{a_{1}, \ldots, a_{n}, b_{1},\ldots,b_{n}\}$ 的集合，其中每一对 $\{a_{i}, b_{i}\} \in P$。既然 $P$ 是无限的，我们可以从 $P$ 中选出一对 $\{c, d\} = U$，它不同于所有的 $\{a_{i}, b_{i}\}$。现在我们定义 $\pi \in G$，使 *π* 固定每个 $a_{i}$ 与 $b_{i}$，并互换 $c$ 与 $d$。于是 *π* 也固定 $f$。既然假定 $f$ 是 $P$ 上的选择函数，而 $U \in P$，就必须有 $f(U) \in U$，即 $f(U) = c$ 或 $f(U) = d$。既然 *π* 互换 $c$ 与 $d$，就有 $\pi(f(U)) \ne f(U)$。但 *π* 是自同构，因而也保持函数应用，故 $\pi(f(U)) = \pi f(\pi(U))$。然而 $\pi(U) = U$ 且 $\pi f = f$，于是 $\pi(f(U)) = f(U)$。我们就这样得出了一个矛盾，这表明宇宙 $Sym(V)$ 不含 $P$ 上的任何选择函数。

这里的要点在于：对定义在 $P$ 上的对称函数 $f$，存在一个有限的、由 $P$ 中的对组成的表 $L$，固定其中所有元素就足以固定 $f$，从而也固定 $f$ 的一切值。现在，对 $P$ 中任一不在 $L$ 中的对 $U$，总能找到一个置换 *π*，它固定 $L$ 中各对的所有元素，却不固定 $U$ 的成员。既然 *π* 必须固定 $f$ 在 $U$ 处的值，该值就不可能落在 $U$ 中。因此 $f$ 无法“选择” $U$ 的一个元素，于是 *a fortiori* $f$ 不可能是 $P$ 上的选择函数。

这一论证表明，**由原子构成的集合** 所组成的族未必都有选择函数；但它未能对数学中“通常的”集合，例如实数集，建立同样的事实。这要等到 1963 年，Paul Cohen 才证明：与集合论的标准公理（它们排除了原子的存在）相容的是，可数多个由实数集合构成的对所组成的汇集没有选择函数。Cohen 证明方法的核心——著名的 **力迫** 方法——其普适性远超以往的任何技巧；尽管如此，他的独立性证明也本质地使用了置换与对称，其形式与 Fraenkel 最初所用的大致相同。

Gödel 关于 *AC* 相对于集合论公理之相对相容性的证明（见“Kurt Gödel”词条），依据的是一个全然不同的想法：**可定义性**。他仿照累积类型分层，引入了一个新的集合分层——**可构造** 分层。我们记得，后者的定义是如下关于序数的递归，其中 $\mathcal{P}(X)$ 是 $X$ 的幂集，*α* 是序数，*λ* 是极限序数：

$$\begin{align} V_0 &= \varnothing \\ V_{\alpha+1} &= \mathcal{P}(V_{\alpha}) \\ V_{\lambda} &= {\bigcup}_{\alpha \lt \lambda} V_{\alpha} \end{align}$$

可构造分层由关于序数的类似递归定义，其中 $\mathrm{Def}(X)$ 是在结构 $(X, \in, (x)_{x\in X})$ 中一阶可定义的一切 $X$ 的子集所构成的集合：[^note-7]

$$\begin{align} L_0 &= \varnothing \\ L_{\alpha+1} &= \mathrm{Def}(L_{\alpha}) \\ L_{\lambda} &= {\bigcup}_{\alpha\lt \lambda} L_{\alpha} \end{align}$$

**可构造宇宙** 是类 $L = \bigcup_{\alpha\in \mathrm{Ord}} L_{\alpha}$；$L$ 的成员就是 **可构造集**。Gödel 表明，（在假定 Zermelo–Fraenkel 集合论 **ZF** 的公理的情况下）结构 $(L, \in)$ 是 **ZF** 的模型，也是 *AC* 以及广义连续统假设的模型。由此可得 *AC* 相对于 **ZF** 的相对相容性。

Gödel（1964）[^gödel-1964] 也注意到（Myhill 与 Scott 1971、Takeuti 1963 与 Post 1951 亦各自独立地注意到）[^myhill-1971]：*AC* 的相对相容性可以借助 **序数可定义性** 给出一个更简单的证明。若我们用 $\mathrm{D}(X)$ 表示在结构 $(X, \in)$ 中一阶可定义的一切 $X$ 的子集所构成的集合，则 **序数可定义集** 的类 OD 就定义为并 $\bigcup_{\alpha\in \mathrm{Ord}} D(V_{\alpha})$。**遗传序数可定义集** 的类 HOD 由一切这样的集合 $a$ 组成：$a$、$a$ 的成员、$a$ 的成员的成员……等等，全都是序数可定义的。于是可以证明，结构 (HOD, $\in$) 是 **ZF** + *AC* 的模型，由此再次得出 *AC* 相对于 **ZF** 的相对相容性。[^note-8]

## 3. 极大原理与佐恩引理

选择公理与一组统称为 **极大原理** 的数学命题密切相关。宽泛地说，这些命题断言：某些条件足以保证一个偏序集至少含有一个 **极大元**，即这样一个元素：相对于给定的偏序，没有元素严格超过它。

要看出极大元概念与 *AC* 之间的联系，让我们回到后者用索引集表述的形式 **AC2**。据此，假定给定一个由非空集构成的索引集族 $\mathcal{A} = \{A_{i}:i \in I\}.$ 我们称 $\mathcal{A}$ 上的一个 **潜在选择函数** 为这样一个函数 $f$：其定义域是 $I$ 的子集，且对所有 $i\in J$ 都有 $f(i) \in A_{i}$。（这里使用 **潜在** 这一限定语，是因为定义域是 $I$ 的子集；回想一下，$\mathcal{A}$ 上的选择函数 $f$ 具有与我们现在称为潜在选择函数的那些函数相同的性质，只不过要求 $f$ 的定义域是整个 $I$，而不只是一个子集。）$\mathcal{A}$ 上潜在选择函数的集合 $P$ 可按包含关系偏序化：我们约定，对潜在选择函数 $f, g \in P$，关系 $f \le g$ 成立，当且仅当 $f$ 的定义域包含于 $g$ 的定义域，且 $f$ 在其定义域某个元素处的值与 $g$ 在该处的值一致。现在容易看出，$P$ 关于偏序 $\le$ 的极大元恰恰就是 $\mathcal{A}$ 上的选择函数。

**佐恩引理** 是确保这类极大元存在的最著名原则。要陈述它，我们需要一些定义。给定偏序集 $(P, \le)$，$P$ 的子集 $X$ 的 **上界** 是这样一个元素 $a\in P$：对每个 $x\in X$ 都有 $x\le a$；于是 $P$ 的 **极大元** 可以定义为这样一个元素 $a$：$\{a\}$ 的上界集与 $\{a\}$ 重合，这实质上意味着 $P$ 中没有元素严格大于 $a$。$(P,\le)$ 中的 **链** 是 $P$ 的一个子集 $C$，使得对任意的 $x$、$y\in P$，或者 $x\le y$，或者 $y\le x$。若 $P$ 中每条链都有上界，则称 $P$ 是 **归纳的**。现在，佐恩引理断言：

**佐恩引理**（**ZL**）：每个非空归纳偏序集都有极大元。

佐恩引理为何可信？这里给出一个非正式的论证。给定非空归纳偏序集 $(P,\le)$，任取 $P$ 的一个元素 $p_{0}$。若 $p_{0}$ 是极大元，就此打住。否则取一个元素 $p_{1} \gt p_{0}$；若 $p_{1}$ 是极大元，就此打住。否则取一个元素 $p_{2} \gt p_{1}$，并重复这一过程。若元素 $p_{0} \lt p_{1} \lt p_{2} \lt \ldots \lt p_{n} \lt \ldots$ 中没有一个是极大元，则这些 $p_{i}$ 构成一条链，而由于 $P$ 是归纳的，这条链有上界 $q_{0}$。若 $q_{0}$ 是极大元，就此打住。否则可对 $q_{0} \lt q_{1}$、……重复上述程序，然后再迭代下去。这一过程必定最终停止，否则如此生成的各条链之并将构成一个真类，从而使 $P$ 本身也成为真类，与假设矛盾。过程停止之处就给出 $P$ 的一个极大元。

这一论证经适当严格化，就在 Zermelo–Fraenkel 集合论中给出了由 **AC1** 推出 **ZL** 的一个证明[^note-9]：在这一证明中，**AC1** 被用来“挑选”非正式论证所提到的那些元素。

佐恩引理还有另一种用集合汇集的表述。给定集合族 $\mathcal{H}$，我们称 $\mathcal{H}$ 的一个子族 $\mathcal{N}$ 为 $\mathcal{H}$ 中的一个 **巢**，如果对 $\mathcal{N}$ 的任意两个成员，其中一个包含于另一个。[^note-10] 若 $\mathcal{H}$ 中任一巢的并仍是 $\mathcal{H}$ 的成员，则称 $\mathcal{H}$ 是 **强归纳的**。于是佐恩引理可以等价地重述为：任何非空强归纳的集合族 $\mathcal{H}$ 都有一个极大成员，即一个不真包含于 $\mathcal{H}$ 的任何成员之中的成员。这又可以表述为一种对偶形式。若一族集合对巢的交封闭，则称之为 **强归约的**。于是任何非空强归约的集合族都有一个 **极小** 元，即一个不真包含族中任何成员的成员。

现在很容易从这种替代形式的佐恩引理推出 **AC2**。因为索引集族 $\mathcal{A}$ 上潜在选择函数的集合 $P$ 显然非空，且不难证明它是强归纳的；于是佐恩引理给出 $\mathcal{A}$ 上一个选择函数的存在性。

**CAC** 可以从 **ZL** 推出，其方式与上文勾勒的 **CAC** 的“组合”辩护相呼应。据此，假定给定一个由两两不交的非空集构成的族 $\mathcal{H}$；称子集 $S \subseteq \bigcup \mathcal{H}$ 为 $\mathcal{H}$ 的一个 **采样**，如果对任一 $X\in \mathcal{H}$，或者 $X \subseteq S$，或者 $S \cap X$ 非空且有限。极小采样恰恰就是 $\mathcal{H}$ 的横截集；[^note-11] 而采样构成的族 $\mathcal{T}$ 显然非空，因为它包含 $\bigcup \mathcal{H}$。因此，若能证明 $\mathcal{T}$ 是强归约的，[^note-12] 佐恩引理就将给出 $\mathcal{T}$ 的一个极小元，从而是 $\mathcal{H}$ 的一个横截集。$\mathcal{T}$ 的强归约性可以这样看出：设 $\{S_{i}: i\in I\}$ 是一个由采样构成的巢；令 $S = {\bigcap}_{i\in I} S_{i}$。我们需要证明 $S$ 本身是一个采样；为此设 $X \in \mathcal{H}$，并假定 $\neg(X \subseteq S)$。则存在 $i \in I$ 使 $\neg(X \subseteq S_{i})$；既然 $S_{i}$ 是采样，$S_{i}\cap X$ 有限且非空，比如 $S_{i}\cap X = \{x_{1}, \ldots, x_{n}\}$。显然此时 $S\cap X$ 是有限的；为导出矛盾，假定 $S\cap X = \varnothing$。那么对每个 $k = 1,\ldots,n$，存在 $i_k \in I$ 使 $\neg(x_k \in S_{i_k})$。由此可知 $\neg(S_{i} \subseteq S_{i_k})$，对 $k = 1, \ldots, n$。因此，既然这些 $S_{i}$ 构成链，每个 $S_{i_k}$ 都是 $S_{i}$ 的子集。令 $S_{j}$ 为 $S_{i_1},\ldots, S_{i_k}$ 中最小的一个；则 $S_{j}\subseteq S_{i}$。但既然 $\neg(x_{k} \in S_{j})$ 对 $k = 1, \ldots, n$ 成立，此时就推出 $S_{j} \cap X = \varnothing$，这与 $S_{j}$ 是采样这一事实矛盾。因此 $S \cap X\ne \varnothing$；故 $S$ 如所断言是一个采样。

我们注意到，虽然佐恩引理与选择公理在集合论上等价，但从后者推出前者要比从前者推出后者困难得多。

下面是极大原理的一份简略年表。

| 1909 | Hausdorff 首次明确表述了一种极大原理，并由 *AC* 推出它（Hausdorff 1909）[^hausdorff-1909] |
| --- | --- |
| 1914 | Hausdorff 的 *Grundzüge der Mengenlehre*（最早的集合论与一般拓扑学著作之一）包含若干极大原理。 |
| 1922 | Kuratowski 在避免使用超限序数时表述并运用了若干极大原理（Kuratowski 1922）[^kuratowski-1922]。 |
| 1926–28 | Bochner 等人各自独立地引入极大原理（Bochner 1928, Moore 1932）[^bochner-1928][^moore-1932]。 |
| 1935 | Max Zorn 显然并不熟悉此前关于极大原理的各种表述，他发表了（Zorn 1935）[^zorn-1935] 自己关于该原理的定稿版本，此版本后来以他的引理（**ZL**）之名广为人知。**ZL** 最早于 1933 年在汉堡被表述出来，Chevalley 与 Artin 很快“采纳”了它。似乎正是 Artin 最先认识到 **ZL** 能够推出 *AC*，从而在集合论其余公理之上两者等价。Zorn 本人更多地把他的原理视为一条 **公理** 而非一条定理——他希望它能取代代数中超限归纳与良序的那些笨重应用，而 Noether 学派的代数学家当时已开始把这些应用视为“超越性的”手段。 |
| 1939–40 | Teichmüller、Bourbaki 与 Tukey 各自独立地用“有限特征的性质”重新表述了 **ZL**（Bourbaki 1939, Teichmuller 1939, Tukey 1940）[^bourbaki-1939][^teichmuller-1939]。 |

## 脚注

[^zermelo-1904]: Zermelo, E., 1904. “Neuer Beweis, dass jede Menge Wohlordnung werden kann (Aus einem an Herrn Hilbert gerichteten Briefe)”, *Mathematische Annalen*, 59: 514–16. Translated in J. van Heijenoort (ed.), *From Frege to Gödel: A Source Book in Mathematical Logic, 1879–1931*, Cambridge, MA: Harvard University Press, 1967, pp. 139–141.

[^note-1]: Zermelo does not, however, actually give the principle an explicit name at this point. ( He does so only in 1908, where he uses the term “postulate of choice”. We note that Zermelo here uses the term “product” , which is the reason why a number of mathematicians (in particular Russell and Ramsey) referred to the axiom as the “multiplicative axiom” (see §4 below).

[^note-2]: A function $f$: $A \rightarrow B$ is *surjective* if for any element $b \in B$ there is $a \in A$ such that $f(a) = b$. A *right inverse* to $f$ is a function $g: B \rightarrow A$ such that, for any $x\in B$, $f(g(x) = x$.

[^note-3]: Zermelo’s formulation reads literally:  > A set $S$ that can be decomposed into a set of disjoint parts $A$, $B$, $C$, … , each containing at least one element, possess at least one subset $S_{1}$ having exactly one element with each of the parts $A$, $B$, $C$, … , considered.

[^note-4]: The difficulty here is amusingly illustrated by an anecdote due to Bertrand Russell. A millionaire possesses an infinite number of pairs of shoes, and an infinite number of pairs of socks. One day, in a fit of eccentricity, the millionaire summons his valet and asks him to select one shoe from each pair. When the valet, accustomed to receiving precise instructions, asks for details as to how to perform the selection, the millionaire suggests that the left shoe be chosen from each pair. Next day the millionaire proposes to the valet that he select one *sock* from each pair. When asked as to how *this* operation is to be carried out, the millionaire is at a loss for a reply, since, unlike shoes, there is no intrinsic way of distinguishing one sock of a pair from the other. In other words, the selection of the socks must be truly arbitrary.

[^note-5]: In 1923 Hilbert asserted:  > The essential idea on which the axiom of choice is based constitutes a general logical principle which, even for the first elements of mathematical inference, is indispensable.  (Quoted in section 4.8 of Moore 1982.)[^moore-1982]

[^moore-1982]: Moore, G.H., 1982. *Zermelo’s Axiom of Choice*, Berlin: Springer-Verlag.

[^banach-1924]: Banach, S. and Tarski, A., 1924. “Sur la décomposition des ensembles de points en parties respectivement congruentes,” *Fundamenta Mathematicae*, 6: 244–277.

[^wagon-1993]: Wagon, S., 1993.*The Banach-Tarski Paradox*, Cambridge University Press.

[^note-6]: For a detailed history of the Axiom of Choice, see Moore 1982.

[^hausdorff-1914]: –––, 1914. *Grundzüge der Mengenlehre*, Leipzig: de Gruyter. Reprinted, New York: Chelsea, 1965.

[^fraenkel-1922]: Fraenkel, A., 1922. “Zu den Grundlagen der Cantor-Zermeloschen Mengenlehre”, *Mathematische Annalen*, 86: 230–237.

[^hilbert-1926]: Hilbert D., 1926. “Über das Unendliche,” *Mathematische Annalen*, 95. Translated in J. van Heijenoort (ed.) *From Frege to Gödel: A Source Book in Mathematical Logic, 1879–1931*, Cambridge, MA: Harvard University Press, 1967, pp. 367–392.

[^lindenbaum-1938]: Lindenbaum, A., and Mostowski, A., 1938. “Über die Unabhängigkeit des Auswahlsaxioms und einiger seiner Folgerungen,” *Comptes Rendus des Séances de la Société des Sciences et des Lettres de Varsovie*, 31: 27–32.

[^gödel-1938a]: Gödel, K., 1938a. “The consistency of the axiom of choice and of the generalized continuum-hypothesis,” *Proceedings of the U.S. National Academy of Sciences*, 24: 556–7.

[^gödel-1938b]: Gödel, K., 1938b. “Consistency-proof for the generalized continuum-hypothesis,” *Proceedings of the U.S. National Academy of Sciemces*, 25: 220–4.

[^gödel-1940]: Gödel, K., 1940. *The Consistency of the Axiom of Choice and of the Generalized Continuum-Hypothesis with the Axioms of Set Theory*, Annals of Mathematics Studies, No. 3, Princeton: Princeton University Press.

[^mendelson-1956]: Mendelson, E., 1956. “The independence of a weak axiom of choice,” *Journal of Symbolic Logic*, 21: 350–366.

[^mendelson-1958]: –––, 1958. “The axiom of fundierung and the axiom of choice,” *Arkiv fur Mathematische Logik und Grundlagenforschung*, 4: 67–70.

[^shoenfield-1955]: Shoenfield, J. R., 1955. “The independence of the axiom of choice,” *Journal of Symbolic Logic*, 20: 202.

[^specker-1957]: Specker, E., 1957. “Zur Axiomatik der Mengenlehre (Fundierungs- und Auswahlaxiom),” *Zeit. Math. Logik und Grund.*, 3: 173–210.

[^cohen-1963]: Cohen, P.J., 1963. “The independence of the continuum hypothesis I,” *Proceedings of the U.S. National Academy of Sciemces*, 50: 1143–48. [The independence of the Axiom of Choice from the standard axioms of set theory, ZF, is part of Theorem 1 of this paper.]

[^cohen-1964]: –––, 1964. “The independence of the continuum hypothesis II,” *Proceedings of the U.S. National Academy of Sciemces*, 51: 105–110.

[^note-7]: Here ($x)_{x\in X}$ indicates that all the members of $X$ are taken as designated elements of the structure, i.e. as being named by constant symbols in the associated first-order language.

[^gödel-1964]: Gödel, K., 1964. “Remarks before the Princeton Bicentennial Conference,” in *The Undecidable*, Martin Davis (ed.), CITY: Raven Press, pp. 84–88.

[^myhill-1971]: Myhill, J. and Scott, D.S., 1971. “Ordinal definability,” *Axiomatic Set Theory*. Proceedings of Symposia in Pure Mathematics, Vol. XIII, Part I. American Mathematical Society, pp. 271–8.

[^note-8]: For a detailed account of the proof of the independence of the Axiom of Choice, see Bell 2005 or Jech 1973.

[^note-9]: For the proof of *ZL* from *AC* in **ZF**, see Mendelson 1987 (Ch. 4, sect. 5). For a proof not using ordinals, and so formulable in Zermelo set theory, see Bourbaki 1950 or Lawvere and Rosebrugh 2003 (Appendix B).

[^note-10]: Thus a nest in $S$ is a chain in $S$ partially ordered by set inclusion.

[^note-11]: That minimal samplings are transversals requires demonstration. Suppose $S$ is a minimal sampling; then, given $X\in \mathcal{I}$ either (1) $S\cap X$ is finite nonempty or (2) $X \subseteq S$. In case (1) $S\cap X$ cannot contain two distinct elements because the removal of one of them from $S$ would yield a sampling smaller than $S$, violating its minimality. So in this case $S\cap X$ must be a singleton. In case (2) $S$ cannot contain two distinct elements $a$, $b$ since, if it did, $S' = [(S - X) \cup \{a\}]$ would be a sampling smaller than $S$ (notice that $S' \cap X = \{a\}$ and the relations of $S'$ with the members of $\mathcal{I} - \{X\}$ are the same as those of $S$), again violating the minimality of $S$. So in this case $X$, and *a fortiori* $S\cap X$ must be a singleton.

[^note-12]: Had we elected to follow more closely the intuitive combinatorial derivation of *AC* as sketched above by using selectors instead of samplings we would have encountered the obstacle that—unlike the set of samplings—the set of selectors is not necessarily reductive.

[^hausdorff-1909]: Hausdorff, F., 1909. “Die Graduierung nach dem Endverlauf,” *Königlich Sächsichsen Gesellschaft der Wissenschaften zu Leipzig, Math.—Phys. Klasse, Sitzungberichte*, 61: 297–334.

[^kuratowski-1922]: Kuratowski, K., 1922. “Une méthode d’élimination des nombres transfinis des raissonements mathématiques,” *Fundamenta Mathematicae*, 3: 76–108.

[^bochner-1928]: Bochner, S., 1928. “Fortsetzung Riemannscher Flachen,” *Mathematische Annalen*, 98: 406–421.

[^moore-1932]: Moore, R.L., 1932. *Foundations of Point Set Theory*, Anerican Mathematical Society Colloquium Publications, vol. 13.

[^zorn-1935]: Zorn, M., 1935. A remark on method in transfinite algebra, *Bulletin of the American Mathematical Society*, 41: 667–70.

[^bourbaki-1939]: Bourbaki, N., 1939. *Elements de Mathematique, Livre I: Theorie des Ensembles*, Paris: Hermann.

[^teichmuller-1939]: Teichmuller, O., 1939. “Brauch der Algebraiker das Auswahlaxiom?” *Deutsches Mathematik*, 4: 567–577.
