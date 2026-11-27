# 选择公理 The Axiom of Choice (John L. Bell)

> *首次发表于 2008 年 1 月 8 日；实质修订于 2021 年 12 月 10 日。*

集合论中称为 **选择公理** 的原则，素有“也许是最有趣、而且尽管出现较晚，却是数学中被讨论得最多的公理，仅次于两千多年前引入的欧几里得平行公理”之称（Fraenkel, Bar-Hillel & Levy 1973, §II.4）[^fraenkel-1973]。这番溢美之词或许会使不熟悉该公理的读者以为它像光速不变原理或海森堡不确定性原理那样惊世骇俗。但实际上，通常表述的选择公理看上去平淡无奇，甚至自明。因为它只不过断言：给定任意一族两两不交的非空集合，就可以组装出一个新集合——一个 **横截集** 或 **选择集**——它恰好从该族的每个成员中取一个元素。然而，这个看似无害的原则却有深远的数学后果——许多不可或缺，有些令人惊讶——并已在数学基础讨论中占据显著位置。它（或其等价形式）已被用于无数数学论文，还有若干专著专门讨论它。

## 1. 选择公理的起源与年表

1904 年，Ernst Zermelo 以一种他称为 **覆盖**（coverings）的方式表述了选择公理（本文通篇简称 *AC*）（Zermelo 1904）[^zermelo-1904]。他先从任意集合 $M$ 出发，用符号 $M'$ 表示 $M$ 的任意非空子集，并把它们的汇集记作 M。他接着写道：

> 设想每个子集 $M'$ 都配定一个出现在 $M'$ 自身之中的任意元素 $m_{1}'$；称 $m_{1}'$ 为 $M'$ 的“特异”（distinguished）元素。这就得到由集合 $M$ 的某些元素对集合 $M$ 所作的一个“覆盖” $g$。这些覆盖的数目等于［所有子集 $M'$ 的基数之］积，并且肯定不为 0。

这段引文的最后一句——它实际上断言，对任何（非空）集合的非空子集汇集，覆盖总是存在——是 Zermelo 对选择公理的第一个表述[^note-1]。这一表述如今通常用 **选择函数** 来陈述：由非空集合构成的族 $\mathcal{H}$ 上的选择函数，是一个定义域为 $\mathcal{H}$ 的映射 $f$，使得对每个 $X \in \mathcal{H}$ 都有 $f(X) \in X$。

举一个很简单的例子：令 $\mathcal{H}$ 为 $\{0, 1\}$ 的非空子集构成的汇集，即 $\mathcal{H} = \{\{0\}, \{1\}, \{0,1\}\}$。于是 $\mathcal{H}$ 有两个不同的选择函数 $f_{1}$ 与 $f_{2}$，由下式给出：

$$\begin{align} f_{1}(\{0\}) &= 0 \\ f_{1}(\{1\}) &= 1 \\ f_{1}(\{0, 1\}) &= 0 \\ f_{2}(\{0\}) &= 0 \\ f_{2}(\{1\}) &= 1 \\ f_{2}(\{0, 1\}) &= 1 \end{align}$$

另一个更有意思的选择函数例子是：取 $\mathcal{H}$ 为实数无序对的集合，取那个为每一对指定其最小元素的函数。若为每一对指定其最大元素，就得到另一个不同的选择函数。显然，$\mathcal{H}$ 上还能定义多得多的选择函数。

用选择函数来陈述，Zermelo 对 *AC* 的第一个表述是：

**AC1**：任何由非空集合构成的族都有一个选择函数。

**AC1** 也可以用 **索引集族** 或 **变元集** 来重新表述。集合的索引集族 $\mathcal{A} = \{A_{i}: i \in I\}$ 可以设想为一个 **变元集**，即一个在索引集 $I$ 上 **变动** 的集合。此时每个 $A_{i}$ 都是变元集 $\mathcal{A}$ 在 **阶段** $i$ 的“值”。$\mathcal{A}$ 上的 **选择函数** 是一个映射 $f: I \rightarrow \bigcup_{i\in I} A_{i}$，使得对所有 $i\in I$ 都有 $f(i) \in A_{i}$。于是 $\mathcal{A}$ 上的选择函数就是在每一阶段对变元集 $\mathcal{A}$ 的某个元素作出的“选择”；换言之，$\mathcal{A}$ 上的选择函数是 $\mathcal{A}$ 的一个 **变元元素**。**AC1** 于是等价于下述断言：

**AC2**：任何集合的索引集族都有一个选择函数。

非正式地说，**AC2** 相当于断言：一个在每一阶段都有元素的变元集有一个变元元素。

**AC1** 也可以用关系来重新表述，即：

**AC3**：对集合 $A$ 与 $B$ 之间的任何关系 $R$，

$$ {\forall x\in A}\ \exists y\in B[R(x,y)] \Rightarrow \exists f[f: A \rightarrow B \mathbin{\&} {\forall x\in A}[R(x,fx)]]. $$

换言之，每个关系都包含一个具有相同定义域的函数。

最后，**AC3** 很容易被证明（在通常的集合论中）等价于：[^note-2]

**AC4**：任何满射函数都有右逆。

在 1908 年的一篇论文中，Zermelo 引入了 *AC* 的一种修正形式。我们称任一子集 $T \subseteq \bigcup \mathcal{H}$ 为集合族 $\mathcal{H}$ 的一个 **横截集**（或 **选择集**），只要对每个 $X \in \mathcal{H}$，交集 $T \cap X$ 恰有一个元素。举一个很简单的例子：令 $\mathcal{H} = \{\{0\}, \{1\}, \{2, 3\}\}$，则 $\mathcal{H}$ 有两个横截集 $\{0, 1, 2\}$ 与 $\{0, 1, 3\}$。一个更实在的例子是：令 $\mathcal{H}$ 为欧几里得平面中所有平行于 $x$ 轴的直线构成的汇集。此时 $y$ 轴上的点集 $T$ 就是 $\mathcal{H}$ 的一个横截集。

那么，用横截集来陈述，Zermelo 的第二个（1908 年）表述就相当于断言：任何两两不交的非空集合族都有一个横截集。[^note-3]

Zermelo 断言，这一原则“纯客观的特性”“是显而易见的”。作此断言时，Zermelo 意在强调：在这一形式下，该原则并未诉诸“选择”的可能性。也可能 Zermelo 心中想的是下面这个对该原则的“组合”辩护。给定一个两两不交的非空集合族 $\mathcal{H}$，称子集 $S \subseteq \bigcup \mathcal{H}$ 为 $\mathcal{H}$ 的 **选择子**，如果对所有 $X \in \mathcal{H}$ 都有 $S\cap X \ne \varnothing$。显然 $\mathcal{H}$ 的选择子是存在的；$\bigcup \mathcal{H}$ 本身就是一例。现在可以设想取 $\mathcal{H}$ 的一个选择子 $S$，并“削薄”每个交集 $S \cap X$（其中 $X\in \mathcal{H}$），直到它只含一个元素。结果便是 $\mathcal{H}$ 的一个横截集。这一论证经适当精化，就从称为 **佐恩引理** 的集合论原则（见下文）给出了这一形式下 *AC* 的精确推导。

我们称 Zermelo 1908 年的表述为 **组合** 形式的选择公理：

**CAC**：任何两两不交的非空集合族都有一个横截集。

应当注意，对于 **有限** 的集合族，**AC1** 与 **CAC** 在通常的集合论中都是可证的（用归纳法）。但对于 **无限** 族，即便其每个成员都是有限的，选择函数或横截集是否存在，也是成问题的[^note-4]。例如，如前所述，为实数无序对构成的族找一个选择函数很容易（只需选出每一对中较小的元素）。但是，要为任意实数集合组成的无序对构成的族给出一个选择函数，却绝非显然。

Zermelo 引入 *AC* 的初衷，是要确立 Cantor 集合论的一条核心原则，即每个集合都容许一个良序，因而也可以被指派一个基数。Zermelo 于 1904 年引入这一公理并使用它，招致了当时数学家的相当多批评。主要反对意见针对该公理高度非构造性、甚至唯心主义的特征。它断言可以任意选择若干——甚至可能不可数多个——对象，却丝毫没有说明这些选择实际上如何实现，也丝毫没有说明如何 **定义** 选择函数。这一点对具有“构造”倾向的数学家尤其难以接受，例如所谓的法国经验论者 Baire、Borel 与 Lebesgue；在他们看来，一个数学对象只有能如此定义以致唯一地刻画它，才能被断言存在。Zermelo 对批评者的回应见于 1908 年的两篇论文。在第一篇中，如上所述，他用横截集重新表述了 *AC*；在第二篇（1908a）中，他明确给出了完成其良序定理证明所需的进一步假设。这些假设构成了对集合论公理系统的首次明确陈述。

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
| 1935—38 | Gödel 确立了 *AC* 与集合论公理的相对相容性（Gödel 1938a, 1938b, 1939, 1940）[^gödel-1938a][^gödel-1938b][^gödel-1940]。 |
| 1950s | Mendelson、Shoenfield 与 Specker 各自独立地运用置换法，确立了 *AC* 各种形式相对于不含原子、但也缺少基础公理的集合论系统的独立性（Mendelson 1956, 1958, Shoenfield 1955, Specker 1957）[^mendelson-1956][^mendelson-1958][^shoenfield-1955][^specker-1957]。 |
| 1963 | Paul Cohen 证明 *AC* 相对于集合论标准公理的独立性（Cohen 1963, 1964）[^cohen-1963][^cohen-1964]。 |

## 2. 选择公理的独立性与相容性

如前所述，1922 年 Fraenkel 证明了 *AC* 相对于一个含有“原子”的集合论系统的独立性。这里所谓 **原子**（atom），指的是一个纯粹的个体，即一个没有成员、却又区别于空集的实体（因此 *a fortiori* 原子不可能是集合）。在带原子的集合论系统中，假定给定了一个由原子构成的无限集 $A$。人们可以从 $A$ 出发，先加入 $A$ 的一切子集，再加入所得结果的一切子集，如此等等，并超限地迭代下去，从而在 $A$ 之上构造出一个集合的宇宙 $V(A)$。于是 $V(A)$ 就是带原子的集合论的一个模型。Fraenkel 证明 *AC* 独立性之方法的核心在于这样一个观察：既然原子无法在集合论上被区分，那么原子集 $A$ 的任一置换都会诱导出由 $A$ 构造的集合宇宙 $V(A)$ 的一个保结构置换——一个 **自同构**。这一想法可用来构造集合论的另一个模型 $Sym(V)$：一个 **置换模型** 或 **对称模型**；在其中，由 $A$ 的元素组成彼此不交的对，再由这些对组成集合，该集合没有选择函数。

现在假定给定 $A$ 的一个自同构群 $G$。我们说 $A$ 的一个自同构 *π* **固定** $V(A)$ 的一个元素 $x$，如果 $\pi(x) = x$。显然，若 $\pi \in G$ 固定 $A$ 的每个元素，则它也固定 $V(A)$ 的每个元素。现在可能出现这样的情况：对某些元素 $x \in V(A)$，只要任一 $\pi\in G$ 固定 $A$ 的某个 **子集** 的元素，就足以固定 $x$。于是我们不妨把 $x$ 的一个 **支撑** 定义为 $A$ 的一个子集 $X$，使得只要 $\pi\in G$ 固定 $X$ 的每个成员，它也就固定 $x$。$V(A)$ 中具有 **有限** 支撑的成员称为 **对称的**。

我们接下来把宇宙 $Sym(V)$ 定义为由 $V(A)$ 中 **遗传对称的** 成员组成，即那些 $x\in V(A)$，使得 $x$、$x$ 的元素、$x$ 的元素的元素等等全都是对称的。$Sym(V)$ 也是以 $A$ 为原子集的集合论的一个模型，而 *π* 诱导出 $Sym(V)$ 的一个自同构。

现在设 $A$ 被划分成一个（必然无限的）由彼此不交的对组成的族 $P$。取 $G$ 为 $A$ 的、固定 $P$ 中所有对的一切置换所构成的群。于是 $P\in Sym(V)$；此时可以证明，$Sym(V)$ 中不含 $P$ 上的任何选择函数。因为，假定 $f$ 是 $P$ 上的一个选择函数且 $f \in Sym(V)$。那么 $f$ 有一个有限支撑，不妨取为形如 $\{a_{1}, \ldots, a_{n}, b_{1},\ldots,b_{n}\}$ 的集合，其中每一对 $\{a_{i}, b_{i}\} \in P$。既然 $P$ 是无限的，我们可以从 $P$ 中选出一对 $\{c, d\} = U$，它不同于所有的 $\{a_{i}, b_{i}\}$。现在我们定义 $\pi \in G$，使 *π* 固定每个 $a_{i}$ 与 $b_{i}$，并互换 $c$ 与 $d$。于是 *π* 也固定 $f$。既然假定 $f$ 是 $P$ 上的选择函数，而 $U \in P$，就必须有 $f(U) \in U$，即 $f(U) = c$ 或 $f(U) = d$。既然 *π* 互换 $c$ 与 $d$，就有 $\pi(f(U)) \ne f(U)$。但 *π* 是自同构，因而也保持函数应用，故 $\pi(f(U)) = \pi f(\pi(U))$。然而 $\pi(U) = U$ 且 $\pi f = f$，于是 $\pi(f(U)) = f(U)$。我们就这样得出了一个矛盾，这表明宇宙 $Sym(V)$ 不含 $P$ 上的任何选择函数。

这里的要点在于：对定义在 $P$ 上的对称函数 $f$，存在一个有限的、由 $P$ 中的对组成的表 $L$，固定这些对中的所有元素就足以固定 $f$，从而也固定 $f$ 的一切值。现在，对 $P$ 中任一不在 $L$ 中的对 $U$，总能找到一个置换 *π*，它固定 $L$ 中各对的所有元素，却不固定 $U$ 的成员。既然 *π* 必须固定 $f$ 在 $U$ 处的值，该值就不可能落在 $U$ 中。因此 $f$ 无法“选择” $U$ 的一个元素，于是 *a fortiori* $f$ 不可能是 $P$ 上的选择函数。

这一论证表明，**由原子构成的集合** 所组成的族未必都有选择函数；但它未能对数学中“通常的”集合，例如实数集，建立同样的事实。这要等到 1963 年，Paul Cohen 才证明：与集合论的标准公理（它们排除了原子的存在）相容的是，可数多个由实数集合构成的对所组成的汇集没有选择函数。Cohen 证明方法的核心——著名的 **力迫** 方法——其普适性远超以往的任何技巧；尽管如此，他的独立性证明也本质地使用了置换与对称，其形式与 Fraenkel 最初所用的大致相同。

Gödel 关于 *AC* 相对于集合论公理之相对相容性的证明（见“Kurt Gödel”词条），依据的是一个全然不同的想法：**可定义性**。他仿照累积类型分层，引入了一个新的集合分层——**可构造** 分层。我们记得，后者的定义是如下关于序数的递归，其中 $\mathcal{P}(X)$ 表示 $X$ 的幂集，*α* 是序数，*λ* 是极限序数：

$$\begin{align} V_0 &= \varnothing \\ V_{\alpha+1} &= \mathcal{P}(V_{\alpha}) \\ V_{\lambda} &= {\bigcup}_{\alpha \lt \lambda} V_{\alpha} \end{align}$$

可构造分层由关于序数的类似递归定义，其中 $\mathrm{Def}(X)$ 是在结构 $(X, \in, (x)_{x\in X})$ 中一阶可定义的一切 $X$ 子集构成的集合：[^note-7]

$$\begin{align} L_0 &= \varnothing \\ L_{\alpha+1} &= \mathrm{Def}(L_{\alpha}) \\ L_{\lambda} &= {\bigcup}_{\alpha\lt \lambda} L_{\alpha} \end{align}$$

**可构造宇宙** 是类 $L = \bigcup_{\alpha\in \mathrm{Ord}} L_{\alpha}$；$L$ 的成员就是 **可构造集**。Gödel 表明，（在假定 Zermelo–Fraenkel 集合论 **ZF** 的公理的情况下）结构 $(L, \in)$ 是 **ZF** 的模型，也是 *AC* 以及广义连续统假设的模型。由此可得 *AC* 相对于 **ZF** 的相对相容性。

Gödel（1964）[^gödel-1964] 也注意到（Myhill 与 Scott 1971、Takeuti 1963 与 Post 1951 亦各自独立地注意到）[^myhill-1971]：*AC* 的相对相容性可以借助 **序数可定义性** 给出一个更简单的证明。若我们用 $\mathrm{D}(X)$ 表示在结构 $(X, \in)$ 中一阶可定义的一切 $X$ 的子集所构成的集合，则 **序数可定义集** 的类 OD 就定义为并 $\bigcup_{\alpha\in \mathrm{Ord}} D(V_{\alpha})$。**遗传序数可定义集** 的类 HOD 由一切这样的集合 $a$ 组成：$a$、$a$ 的成员、$a$ 的成员的成员……等等，全都是序数可定义的。于是可以证明，结构 (HOD, $\in$) 是 **ZF** + *AC* 的模型，由此再次得出 *AC* 相对于 **ZF** 的相对相容性。[^note-8]

## 3. 极大原理与佐恩引理

选择公理与一组统称为 **极大原理** 的数学命题密切相关。宽泛地说，这些命题断言：某些条件足以保证一个偏序集至少含有一个 **极大元**，即这样一个元素：相对于给定的偏序，没有元素严格超过它。

要看出极大元概念与 *AC* 之间的联系，让我们回到后者用索引集表述的形式 **AC2**。据此，假定给定一个由非空集构成的索引集族 $\mathcal{A} = \{A_{i}:i \in I\}.$ 我们称这样一个函数 $f$ 为 $\mathcal{A}$ 上的一个 **潜在选择函数**：其定义域是 $I$ 的子集，且对所有 $i\in \operatorname{dom}(f)$ 都有 $f(i) \in A_{i}$。（这里使用 **潜在** 这一限定语，是因为定义域是 $I$ 的子集；回想一下，$\mathcal{A}$ 上的选择函数 $f$ 其性质与我们现在所称的潜在选择函数相同，只不过要求 $f$ 的定义域是整个 $I$，而不只是一个子集。）$\mathcal{A}$ 上潜在选择函数的集合 $P$ 可按包含关系偏序化。我们约定，对潜在选择函数 $f, g \in P$，关系 $f \le g$ 成立，当且仅当 $f$ 的定义域包含于 $g$ 的定义域，且 $f$ 在其定义域某个元素处的值与 $g$ 在该处的值一致。现在容易看出，$P$ 关于偏序 $\le$ 的极大元恰恰就是 $\mathcal{A}$ 上的选择函数。

**佐恩引理** 是确保这类极大元存在的最著名原则。要陈述它，我们需要一些定义。给定偏序集 $(P, \le)$，$P$ 的子集 $X$ 的 **上界** 是这样一个元素 $a\in P$：对每个 $x\in X$ 都有 $x\le a$；于是 $P$ 的 **极大元** 可以定义为这样一个元素 $a$：$\{a\}$ 的上界集与 $\{a\}$ 重合，这实质上意味着 $P$ 中没有元素严格大于 $a$。$(P,\le)$ 中的 **链** 指 $P$ 的子集 $C$，使得对任意的 $x$、$y\in C$，或者 $x\le y$，或者 $y\le x$。若 $P$ 中每条链都有上界，则称 $P$ 是 **归纳的**。现在，佐恩引理断言：

**佐恩引理**（**ZL**）：每个非空归纳偏序集都有极大元。

佐恩引理为何可信？这里给出一个非正式的论证。给定非空归纳偏序集 $(P,\le)$，任取 $P$ 的一个元素 $p_{0}$。若 $p_{0}$ 是极大元，就此打住。否则取一个元素 $p_{1} \gt p_{0}$；若 $p_{1}$ 是极大元，就此打住。否则取一个元素 $p_{2} \gt p_{1}$，并重复这一过程。若元素 $p_{0} \lt p_{1} \lt p_{2} \lt \ldots \lt p_{n} \lt \ldots$ 中没有一个是极大元，则这些 $p_{i}$ 构成一条链，而由于 $P$ 是归纳的，这条链有上界 $q_{0}$。若 $q_{0}$ 是极大元，就此打住。否则可对 $q_{0} \lt q_{1}$、……重复上述程序，然后再迭代下去。这一过程必定最终停止，否则如此生成的各条链之并将构成一个真类，从而使 $P$ 本身也成为真类，与假设矛盾。过程停止之处就给出 $P$ 的一个极大元。

这一论证经适当严格化，就在 Zermelo–Fraenkel 集合论中给出了由 **AC1** 推出 **ZL** 的一个证明[^note-9]：在这一证明中，**AC1** 被用来“挑选”非正式论证所提到的那些元素。

佐恩引理还有另一种用集合汇集的表述。给定集合族 $\mathcal{H}$，我们称 $\mathcal{H}$ 的一个子族 $\mathcal{N}$ 为 $\mathcal{H}$ 中的一个 **巢**，如果对 $\mathcal{N}$ 的任意两个成员，其中一个包含于另一个。[^note-10] 若 $\mathcal{H}$ 中任一巢的并仍是 $\mathcal{H}$ 的成员，则称 $\mathcal{H}$ 是 **强归纳的**。于是佐恩引理可以等价地重述为：任何非空强归纳的集合族 $\mathcal{H}$ 都有一个极大成员，即一个不真包含于 $\mathcal{H}$ 的任何成员之中的成员。这又可以表述为一种对偶形式。若一族集合对巢的交封闭，则称之为 **强归约的**。于是任何非空强归约的集合族都有一个 **极小** 元，即一个不真包含族中任何成员的成员。

现在很容易从这种替代形式的佐恩引理推出 **AC2**。因为索引集族 $\mathcal{A}$ 上潜在选择函数的集合 $P$ 显然非空，且不难证明它是强归纳的；于是佐恩引理给出 $\mathcal{A}$ 上一个选择函数的存在性。

**CAC** 可以从 **ZL** 推出，其方式与上文勾勒的 **CAC** 的“组合”辩护相呼应。据此，假定给定一个由两两不交的非空集构成的族 $\mathcal{H}$；称子集 $S \subseteq \bigcup \mathcal{H}$ 为 $\mathcal{H}$ 的一个 **采样**，如果对任一 $X\in \mathcal{H}$，或者 $X \subseteq S$，或者 $S \cap X$ 非空且有限。极小采样恰恰就是 $\mathcal{H}$ 的横截集；[^note-11] 而采样构成的族 $\mathcal{T}$ 显然非空，因为它包含 $\bigcup \mathcal{H}$。因此，若能证明 $\mathcal{T}$ 是强归约的，[^note-12] 佐恩引理就将给出 $\mathcal{T}$ 的一个极小元，从而是 $\mathcal{H}$ 的一个横截集。$\mathcal{T}$ 的强归约性可以这样看出：设 $\{S_{i}: i\in I\}$ 是一个由采样构成的巢；令 $S = {\bigcap}_{i\in I} S_{i}$。我们需要证明 $S$ 本身是一个采样；为此设 $X \in \mathcal{H}$，并假定 $\neg(X \subseteq S)$。则存在 $i \in I$ 使 $\neg(X \subseteq S_{i})$；既然 $S_{i}$ 是采样，$S_{i}\cap X$ 有限且非空，比如 $S_{i}\cap X = \{x_{1}, \ldots, x_{n}\}$。显然此时 $S\cap X$ 是有限的；为导出矛盾，假定 $S\cap X = \varnothing$。那么对每个 $k = 1,\ldots,n$，存在 $i_k \in I$ 使 $\neg(x_k \in S_{i_k})$。由此可知 $\neg(S_{i} \subseteq S_{i_k})$，对 $k = 1, \ldots, n$。因此，既然这些 $S_{i}$ 构成链，每个 $S_{i_k}$ 都是 $S_{i}$ 的子集。令 $S_{j}$ 为 $S_{i_1},\ldots, S_{i_n}$ 中最小的一个；则 $S_{j}\subseteq S_{i}$。但既然 $\neg(x_{k} \in S_{j})$ 对 $k = 1, \ldots, n$ 成立，此时就推出 $S_{j} \cap X = \varnothing$，这与 $S_{j}$ 是采样这一事实矛盾。因此 $S \cap X\ne \varnothing$；故 $S$ 如所断言是一个采样。

我们注意到，虽然佐恩引理与选择公理在集合论上等价，但从后者推出前者要比从前者推出后者困难得多。

下面是极大原理的一份简略年表。

| 1909 | Hausdorff 首次明确表述了一种极大原理，并由 *AC* 推出它（Hausdorff 1909）[^hausdorff-1909] |
| --- | --- |
| 1914 | Hausdorff 的 *Grundzüge der Mengenlehre*（最早的集合论与一般拓扑学著作之一）包含若干极大原理。 |
| 1922 | Kuratowski 在避免使用超限序数时表述并运用了若干极大原理（Kuratowski 1922）[^kuratowski-1922]。 |
| 1926—28 | Bochner 等人各自独立地引入极大原理（Bochner 1928, Moore 1932）[^bochner-1928][^moore-1932]。 |
| 1935 | Max Zorn 显然并不熟悉此前关于极大原理的各种表述，他发表了（Zorn 1935）[^zorn-1935] 自己关于该原理的定稿版本，此版本后来以他的引理（**ZL**）之名广为人知。**ZL** 最早于 1933 年在汉堡被表述出来，Chevalley 与 Artin 很快“采纳”了它。似乎正是 Artin 最先认识到 **ZL** 能够推出 *AC*，从而在集合论其余公理之上两者等价。Zorn 本人更多地把他的原理视为一条 **公理** 而非一条定理——他希望它能取代代数中超限归纳与良序的那些笨重应用，而 Noether 学派的代数学家当时已开始把这些应用视为“超越性的”手段。 |
| 1939—40 | Teichmüller、Bourbaki 与 Tukey 各自独立地用“有限特征的性质”重新表述了 **ZL**（Bourbaki 1939, Teichmuller 1939, Tukey 1940）[^bourbaki-1939][^teichmuller-1939]。 |

## 4. 选择公理的数学应用

选择公理在数学中有众多应用，其中若干已被证明在形式上与它等价[^note-13]。历史上最重要的应用是第一个，即：

**良序定理**（Zermelo 1904, 1908）[^zermelo-1904][^zermelo-1908]。每个集合都能被良序化。

Zermelo 发表 1904 年从 *AC* 出发对良序定理的证明之后，人们很快便看出两者等价。

另一个早期的 *AC* 等价形式是

**乘法公理**（Russell 1906）[^russell-1906]。任何由非零基数构成的集合之积非零。

*AC* 的早期应用包括：

- 每个无限集都有一个可数子集。这一原理同样弱于 *AC*，在集合论其余公理的语境中，没有 *AC* 便无法证明这一原理。
- 每个无限基数都等于其平方。这一点在 Tarski 1924 中被证明等价于 *AC*。
- 每个向量空间都有基（由 Hamel 1905 首倡）[^hamel-1905]。这一点在 Blass 1984 中被证明等价于 *AC*。
- 每个域都有代数闭包（Steinitz 1910）[^steinitz-1910]。这一断言弱于 *AC*，实际上是（更弱的）一阶逻辑紧致性定理的推论（见下文）。
- 存在勒贝格不可测的实数集（Vitali 1905）[^vitali-1905]。很久以后人们才表明，它是 **BPI**（见下文）的推论，因而弱于 *AC*。Solovay（1970）[^solovay-1970] 确立了它相对于集合论其余公理的独立性。

一个重要的“民间”*AC* 等价形式是

**集合论分配律**。对任意的双重索引集族 $\{M_{i,j}: i \in I,j \in J\}$，其中 $J^I$ 是以 $I$ 为定义域、取值于 $J$ 的一切函数所构成的集合：

$$ \bigcap_{i\in I} \bigcup_{j\in J} M_{i,j} = \bigcup_{f\in J^I} \bigcap_{i\in I} M_{i,f(i)} $$

*AC* 的一个被广泛研究的特例是

**依赖性选择原理**（Bernays 1942, Tarski 1948）[^bernays-1942][^tarski-1948]。对集合 $A$ 上任一满足 $\mathrm{range}(R) \subseteq \mathrm{domain}(R)$ 的非空关系 $R$，存在函数 $f: \omega \rightarrow A$，使得对所有的 $n\in \omega, R(f(n),f(n+1))$ 都成立。这一原理尽管（远）弱于 *AC*，在集合论其余公理的语境中，没有 *AC* 便无法证明它。

*AC* 的数学等价形式包括：

- **吉洪诺夫定理**（1930）：紧致拓扑空间的积是紧致的。这一点在 Kelley 1950 中被证明等价于 *AC*。但对紧致豪斯多夫空间，它等价于 **BPI**（见下文），因而弱于 *AC*。
- **勒文海姆—斯科伦—塔斯基定理**（Löwenheim 1915, Skolem 1920, Tarski and Vaught 1957）[^tarski-1957]：具有无限基数 *κ* 之模型的一阶语句，也具有任一满足 $\mu \le \kappa$ 的无限基数 *μ* 之模型。Tarski 证明了它等价于 *AC*。
- **克莱因—米尔曼定理**：实赋范线性空间的对偶空间的单位球 $B$ 有一个极点，即一个不是 $B$ 中任何线段内点的点。这一点在 Bell and Fremlin 1972a 中被证明等价于 *AC*。该文表明，给定任一非空集构成的索引族 $\mathcal{A}$，$\mathcal{A}$ 上的选择函数与由 $\mathcal{A}$ 构造出的某个实赋范线性空间之对偶的单位球的极点之间存在自然的双射。
- 每个分配格都有极大理想。这一点在 Klimovsky 1958 中被证明等价于 *AC*；对由集合构成的格的情形则在 Bell and Fremlin 1972 中得到证明。
- 每个含单位元的交换环都有极大理想。Hodges 1979 证明了它等价于 *AC*。

*AC* 还有若干已知弱于[^note-14]它的数学推论，特别是：

- **布尔素理想定理**（**BPI**）：每个布尔代数都有极大（或素）理想。Halpern and Levy 1971 表明它弱于 *AC*。
- **布尔代数的斯通表示定理**（Stone 1936）[^stone-1936]：每个布尔代数都同构于一个集合域。它等价于 **BPI**，因而弱于 *AC*。
- **一阶逻辑紧致性定理**（Gödel 1930, Malcev 1937 等）：若一阶语句集的每个有限子集都有模型，则该集合有模型。Henkin 1954 表明它等价于 **BPI**，因而弱于 *AC*。
- **一阶逻辑完全性定理**（Gödel 1930, Henkin 1954）：每个一致的一阶语句集都有模型。Henkin 于 1954 年表明它等价于 **BPI**，因而弱于 *AC*。若以恰当方式指定模型的基数，该断言便等价于 *AC*。

最后还有

- **布尔代数的西科尔斯基扩张定理**（Sikorski 1949）①：每个完备布尔代数都是内射的，即对任一布尔代数 $A$ 与任一完备布尔代数 $B$，从 $A$ 的子代数到 $B$ 的任一同态都可扩张到整个 $A$ 上。

这一原理是否等价于 *AC*，是该领域中少数几个尚存的有趣未决问题之一；它显然蕴涵 **BPI**，但 Bell 1983 证明了它独立于 **BPI**。

这些定理中有许多在 Bell and Machover（1977）中得到讨论。

## 5. 选择公理与逻辑

*AC* 与逻辑之间最初的联系，可以通过回到它用关系表述的形式 **AC3** 而显现出来，即：任何二元关系都包含一个具有相同定义域的函数。**AC** 的这一版本可以自然地在一个二阶语言 $L$ 中表达，该语言有个体变元 $x$、$y$、$z$、……以及函数变元 $f$、$g$、$h$、……。在 $L$ 中，二元关系由带有两个自由个体变元 $x$、$y$ 的公式 $\phi(x, y)$ 表示。于是断言 **AC3** 在 $L$ 中的对应物是

> **ACL**：
> $\forall x \exists y \phi(x, y) \rightarrow \exists f \forall x \phi(x, fx).$

这一语句模式是 *AC* 的标准逻辑形式。

Zermelo 对选择公理的原始表述 **AC1**，可以在 $L$ 的一个适当加强版本中表达为一个语句模式。据此，我们现在假定 $L$ 还包含谓词变元 $X$、$Y$、$Z$、……以及二阶函数变元 $F$、$G$、$H$、……。这里，二阶函数变元 $F$ 可以施用于谓词变元 $X$，从而得到个体项 $FX$。语句模式

> **AC1L**：
> $\forall X [\Phi(X) \rightarrow \exists x X(x)] \rightarrow \exists F \forall X[\Phi(X) \rightarrow X(FX)]$

它就是 **AC1** 在这一加强的二阶语言中的直接对应物。用文字来说，**AC1L** 断言：若每个具有某种性质 *Φ* 的谓词都有实例，则存在一个定义在谓词上的函数 $F$，使得对任一满足 *Φ* 的谓词 $X$，$FX$ 都是 $X$ 的一个实例。这里谓词扮演着集合的角色。

迄今为止，我们一直默契地假定背景逻辑是通常的经典逻辑。但 **AC** 与逻辑之间联系的真正深度，只有在把 **直觉主义** 或 **构造性** 逻辑引入视野之后才会显现。一个值得注意的事实是：仅假定直觉主义逻辑的框架，再加上某些温和的进一步预设，就可以表明选择公理蕴涵经典逻辑的根本规则——排中律，即对任一命题 $A$ 都有 $A \vee \neg A$ 的断言。确切地说，我们在加强语言 $L$ 中使用直觉主义逻辑的规则，将从 **AC1L** 连同下述附加原理一起，推导出[^note-15]排中律：

**直谓概括**：$\exists X \forall x[X(x) \leftrightarrow \phi(x)]$，其中 *φ* 不含受约束的函数变元或谓词变元。

**函数的外延性**：$\forall X \forall Y \forall F[X \approx Y \rightarrow FX = FY]$，其中 $X \approx Y$ 是 $\forall x[X(x) \leftrightarrow Y(x)]$ 的缩写，也就是说，$X$ 与 $Y$ 是 **外延等价** 的。

**两个不同的个体**：$\underline{0} \ne \underline{1}$，其中 $\underline{0}$ 与 $\underline{1}$ 是个体常项。

现在设 $A$ 为给定命题。根据直谓概括，我们可以引入谓词常项 $U$、$V$，连同以下断言：

$$\begin{align} \tag{1} &\forall x[U(x) \leftrightarrow (A \vee x = 0)] \\ \notag &\forall x[V(x) \leftrightarrow (A \vee x = 1)] \end{align}$$

令 $\Phi(X)$ 为公式 $X \approx U \vee X \approx V$。于是显然可以断言 $\forall X[\Phi(X) \rightarrow \exists xX(x)]$，因此可以援引 **AC1L** 来断言 $\exists F \forall X[\Phi(X) \rightarrow X(FX)]$。现在我们可以引入函数常项 $K$，连同断言

$$ \tag{2} \forall X[\Phi(X) \rightarrow X(KX)]. $$

既然显然可以断言 $\Phi(U)$ 与 $\Phi(V)$，由 (2) 即知可以断言 $U(KU)$ 与 $V(KV)$，于是再利用 (1)，

$$ [A \vee KU = 0] \wedge [A \vee KV = 1]. $$

利用分配律（它在直觉主义逻辑中成立），即知可以断言

$$ A \vee [KU = 0 \wedge KV = 1]. $$

由 $0 \ne 1$ 这一预设即知

$$ \tag{3} A \vee KU \ne KV $$

是可断言的。但由 (1) 可知可以断言 $A \rightarrow U ≈ V$，因而利用函数的外延性，也可以断言 $A \rightarrow KU = KV$。这就给出 $KU \ne KV \rightarrow \neg A$ 的可断言性，而它连同 (3) 又给出

$$ A \vee \neg A $$

即排中律。

选择公理蕴涵排中律这一事实，初看似乎与下述事实相左。在受直觉主义逻辑支配的构造性数学系统——例如比肖普的《构造性分析》[^note-16] 与马丁-洛夫的构造性类型论[^note-17]——中，前者常被视为一条 **有效** 原理，而这些系统并不肯定排中律。用比肖普的话说：“在构造性数学中，选择函数存在，因为选择 **正是由存在的意义本身所蕴涵的**。”因此，举例来说，**ACL** 的前件 $\forall x \exists y \phi(x,y)$，在作构造性解读时，恰恰 **意味着** 我们有一个程序，把它施用于每个 $x$，就产生一个使 $\phi(x, y)$ 成立的 $y$。而这正是 **ACL** 的后件 $\exists f \forall x \phi(x,fx)$ 所表达的东西。

为化解这一困难，我们注意到，从 **AC1L** 推导排中律时，本质地使用了直谓概括原理与函数的外延性原理[^note-18]。由此可知，在肯定 **AC**（但不肯定排中律）的构造性数学系统中，**要么直谓概括原理失效，要么函数的外延性原理失效**。直谓概括原理尚可得到构造性证成，函数的外延性原理却无法如此。谓词上的函数按内涵给出，只满足相应的内涵性原理 $\forall X \forall Y \forall F[X = Y \rightarrow FX = FY]$。很容易构造出使外延性原理失效的实例：例如考虑谓词 $P$：**有理性的、无羽毛的两足动物** 与 $Q$：**人**，以及定义在谓词上的函数 $K$，它给每个谓词指派其描述中的词数。于是我们可以同意 $P \approx Q$，但 $KP = 3$ 而 $KQ = 2$。

在直觉主义集合论（以直觉主义逻辑而非经典逻辑为基础，缩写为 **IST**）与拓扑斯理论中，直谓概括原理与函数的外延性原理（两者都作适当解读）成立，因此在其中 **AC** 蕴涵排中律。[^note-19][^note-20]

Diaconescu（1975）[^diaconescu-1975] 最早在范畴论框架中给出了从 *AC* 推导排中律的论证。他的证明的基本想法与上文不同；特别是，它不使用外延性原理，而是采用以等价关系对对象（或集合）作商的想法。在 **IST** 中表述 Diaconescu 的论证是有教益的。为此，我们称集合 $A$ 的子集 $U$ 是 **可分离的**（detachable），如果存在 $A$ 的子集 $V$，使得 $U \cap V = \varnothing$ 且 $U \cup V = A$。Diaconescu 的论证相当于从 **AC4**（见上文）推出如下断言：集合的每个子集都是可分离的；由此即可容易地得出排中律。论证如下。

首先，给定 $U \subseteq A$，$U$（在 $A$ 中）的一个 **指示映射** 是一个满足下式的映射 $g: A \times 2 \rightarrow 2$：

$$ U = \{ x \in A: g(x,0) = g(x,1) \} $$

于是不难证明：一个子集可分离，当且仅当它有指示映射。

现在我们来证明：若 **AC4** 成立，则集合的任何子集都有指示映射，因而都是可分离的。

对 $U \subseteq A$，令 $R$ 为 $A + A = A \times \{0\} \cup A \times \{1\}$ 上的二元关系，由下式给出：

$$ R = \{ ((x,0),(x,0)) : x \in A \} \cup \{ ((x,1),(x,1)) : x \in A \} \cup \{ ((x,0),(x,1) : x \in A \} \cup \{ ((x,1),(x,0) \} : x \in A $$

可以验证 $R$ 是一个等价关系。用 $r$ 表示从 $A + A$ 到 $(A + A)$ 模 $R$ 的商[^note-21] $Q$ 的自然映射，它把 $A + A$ 的每个成员送到其 $R-$等价类。

现在施用 **AC4**，得到映射 $f: Q \rightarrow A + A$，使得对所有 $X \in Q$ 都有 $f(X) \in X$。于是不难证明：若用 $\pi_{1}$ 表示向第一坐标的投影，则

$$ \tag{*} \mbox{对 } n=0,1 \mbox{ 且 } x \in A, \pi_1(f(r(x,n))) = x; $$

并且

$$ \tag{**} x \in U \leftrightarrow f(r(x,0)) = f(r(x,1)). $$

现在由 $g = \pi_{2} \circ f \circ r$ 定义 $g: A \times 2 \rightarrow 2$，其中 $\pi_2$ 是向第二坐标的投影。于是 $g$ 是 $U$ 的一个指示映射，正如以下等价关系所示：

$$\begin{align} x \in U &\leftrightarrow f(r(x,0))=f(r(x,1)) \ldots \mbox{由 (**)} \\ &\leftrightarrow \pi_{1}(f(r(x,0))) = \pi_{1}(f(r(x,1))) \wedge \pi_{2}(f(r(x,0))) = \pi_{2}(f(r(x,1))) \\ &\leftrightarrow \pi_{2}(f(r(x,0))) = \pi_{2}(f(r(x,1))) \ldots \mbox{利用 (*)} \\ &\leftrightarrow g(x,0) = g(x,1). \end{align}$$

证毕。

可以证明（Bell 2006）[^bell-2006]：若干在直觉主义下无效的逻辑原理——包括排中律在内——各自都（在直觉主义集合论中）**等价** 于选择公理的某个适当弱化版本。据此，这些逻辑原理可以被视为选择原理。

以下是所涉及的逻辑原理：

| **SLEM** | $\alpha \vee \neg \alpha$（*α* 为任意语句） |
| --- | --- |
| **Lin** | $(\alpha \rightarrow \beta) \vee (\beta \rightarrow \alpha)$（*α*、*β* 为任意语句） |
| **Stone** | $\neg \alpha \vee \neg\neg \alpha$（*α* 为任意语句） |
| **Ex** | $\exists x[ \exists x \alpha(x) \rightarrow \alpha(x)]$（$\alpha(x)$ 为至多以 $x$ 为自由变元的任意公式） |
| **Un** | $\exists x[\alpha(x) \rightarrow \forall x\alpha(x)]$（$\alpha(x)$ 为至多以 $x$ 为自由变元的任意公式） |
| **Dis** | $\forall x[\alpha \vee \beta(x)] \rightarrow \alpha\vee\forall x\beta(x)$（*α* 为任意语句，$\beta(x)$ 为至多以 $x$ 为自由变元的任意公式） |

在直觉主义逻辑之上，**Lin**、**Stone** 与 **Ex** 都是 **SLEM** 的推论；而 **Un** 蕴涵 **Dis**。当然，所有这些模式都可由完整的排中律——即对任意公式的 **SLEM**——推出。

下文用 0 表示空集，用 1 表示 $\{0\}$，用 2 表示 $\{0, 1\}$。

我们表述以下选择原理——这里 $X$ 是任意集合，$\mathrm{Fun}(X)$ 是以 $X$ 为定义域的函数所构成的类，$\phi(x,y)$ 是集合论语言中至多以 $x$、$y$ 为自由变元的任意公式：

| **AC** $_X$ | $\forall x\in X\ \exists y \phi(x,y) \rightarrow \exists f \in \mathrm{Fun}(X)\ \forall x \in X\ \phi(x,fx)$ |
| --- | --- |
| **AC** $^*_X$ | ${\exists f \in \mathrm{Fun}(X)} [{\forall x\in X}\ \exists y \phi(x,y) \rightarrow {\forall x \in X}\ \phi(x,fx)]$ |
| **DAC** $_X$ | $\forall f \in Fun(X)\ {\exists x \in X}\ \phi(x,fx) \rightarrow {\exists x \in X}\ \forall y \phi(x,y)$ |
| **DAC** $^*_X$ | ${\exists f \in \mathrm{Fun}(X)}\ [{\exists x\in X}\ \phi(x,fx) \rightarrow {\exists x\in X}\ \forall y \phi(x,y)]$ |

其中前两个是 *AC* 对 $X$ 的形式；它们在经典逻辑下等价，但在 **IST** 中 **AC** $^*_X$ 蕴涵 **AC** $_X$，反之则不然。原理 **DAC** $_X$ 与 **DAC** $^*_X$ 是选择公理对 $X$ 的 **对偶** 形式：在经典逻辑下它们都等价于 **AC** $_X$ 与 **AC** $^*_X$，但在直觉主义下 **DAC** $^*_X$ 蕴涵 **DAC** $_X$，反之则不然。

我们还表述 **弱外延选择原理**，其中 $\alpha(x)$ 与 $\beta(x)$ 是至多以变元 $x$ 为自由变元的任意公式：

**WESP**：${\exists x\in 2}\ \alpha(x) \wedge {\exists x \in 2}\ \beta(x) \rightarrow {\exists x \in 2}\ {\exists y \in 2}\ [\alpha(x) \wedge \beta(y) \wedge [{\forall x \in 2}\ [\alpha(x) \leftrightarrow \beta(x)] \rightarrow x = y]].$

这一原理是选择公理的直接推论，它断言：对 2 的成员之任意一对有实例的性质，都可以按照仅取决于其外延的方式为这些性质指派实例。

上表所列的每个逻辑原理都（在 **IST** 中）等价于某个选择原理。事实上：

- **WESP** 与 **SLEM** 在 **IST** 上等价。
- **AC** $^*_1$ 与 **Ex** 在 **IST** 上等价。

此外，虽然容易看出 **DAC** $_1$ 在 **IST** 中可证，我们却有

- **DAC** $^*_1$ 与 **Un** 在 **IST** 上等价。

其次，虽然 **AC** $_2$ 在 **IST** 中容易证明，与之相对，我们却有

- **DAC** $_2$ 与 **Dis** 在 **IST** 上等价。
- 在 **IST** 上，**DAC** $^*_2$ 等价于 **Un**，因而也等价于 **DAC** $^*_1$。

为了给出与 **Lin** 和 **Stone** 等价的选择模式，我们引入

**ac** $^*_X$：${\exists f \in 2^X} [{\forall x\in X}\ {\exists y \in 2}\ \phi(x,y) \rightarrow {\exists x \in X}\ \phi(x,fx)]$

**wac** $^*_X$：${\exists f \in 2^X} [{\forall x \in X}\ {\exists y \in 2}\ \phi(x,y) \rightarrow {\forall x \in X}\ \phi(x,fx)]$，前提是 **IST** 中可证 $\forall x[\phi(x,0) \rightarrow \neg\phi(x,1)]$

显然 **ac** $^*_X$ 等价于

${\exists f \in 2^X}[{\forall x \in X}[\phi(x,0) \vee \phi(x,1)] \rightarrow {\forall x \in X}\ \phi(x,fx)]$

**dac** $^*_X$ 类似。

于是，在 **IST** 上，**ac** $^*_1$ 与 **dac** $^*_1$ 分别等价于 **Lin** 与 **Stone**。

这些结果恰好表明，当背景逻辑被假定为直觉主义逻辑时，选择原理与逻辑的相互作用有多么深刻。而在假定排中律的经典框架中，这些联系则荡然无存。

对选择公理与类型论这一主题感兴趣的读者，可参阅以下补充文档：

> [选择公理与类型论](https://plato.stanford.edu/entries/axiom-choice/choice-and-type-theory.html)

## 参考文献

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## 学术工具

* [如何引用本词条](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=axiom-choice)。
* [预览本词条的 PDF 版本](https://leibniz.stanford.edu/friends/preview/axiom-choice/)，见 [SEP 学会之友](https://leibniz.stanford.edu/friends/)。
* 在 [InPhO](https://www.inphoproject.org/entity?sep=axiom-choice&redirect=True) 查找与本词条相关的话题与思想家。
* 在 [PhilPapers](http://philpapers.org/sep/axiom-choice/) 查看本词条的增强文献目录及其数据库链接。

## 其他网络资源

- [选择公理主页](http://www.math.vanderbilt.edu/~schectex/ccc/choice.html)，由 Eric Schecter（范德堡大学）维护。

## 相关词条

范畴论 | 哥德尔，库尔特 | 逻辑史：直觉主义逻辑 | 逻辑：直觉主义 | 数学：构造性的 | 集合论：构造性与直觉主义 ZF | 集合论：策梅洛公理化 | 类型论：直觉主义

### 致谢

作者与编者感谢 Jesse Alama 仔细阅读本文并提出许多有价值的改进建议。

## 脚注

[^note-1]: Zermelo does not, however, actually give the principle an explicit name at this point. ( He does so only in 1908, where he uses the term “postulate of choice”. We note that Zermelo here uses the term “product” , which is the reason why a number of mathematicians (in particular Russell and Ramsey) referred to the axiom as the “multiplicative axiom” (see §4 below).

[^note-2]: A function $f$: $A \rightarrow B$ is *surjective* if for any element $b \in B$ there is $a \in A$ such that $f(a) = b$. A *right inverse* to $f$ is a function $g: B \rightarrow A$ such that, for any $x\in B$, $f(g(x) = x$.

[^note-3]: Zermelo’s formulation reads literally:

> A set $S$ that can be decomposed into a set of disjoint parts $A$, $B$, $C$, … , each containing at least one element, possess at least one subset $S_{1}$ having exactly one element with each of the parts $A$, $B$, $C$, … , considered.

[^note-4]: The difficulty here is amusingly illustrated by an anecdote due to Bertrand Russell. A millionaire possesses an infinite number of pairs of shoes, and an infinite number of pairs of socks. One day, in a fit of eccentricity, the millionaire summons his valet and asks him to select one shoe from each pair. When the valet, accustomed to receiving precise instructions, asks for details as to how to perform the selection, the millionaire suggests that the left shoe be chosen from each pair. Next day the millionaire proposes to the valet that he select one *sock* from each pair. When asked as to how *this* operation is to be carried out, the millionaire is at a loss for a reply, since, unlike shoes, there is no intrinsic way of distinguishing one sock of a pair from the other. In other words, the selection of the socks must be truly arbitrary.

[^note-5]: In 1923 Hilbert asserted:

> The essential idea on which the axiom of choice is based constitutes a general logical principle which, even for the first elements of mathematical inference, is indispensable.

(Quoted in section 4.8 of Moore 1982.)[^moore-1982]

[^note-6]: For a detailed history of the Axiom of Choice, see Moore 1982.

[^note-7]: Here ($x)_{x\in X}$ indicates that all the members of $X$ are taken as designated elements of the structure, i.e. as being named by constant symbols in the associated first-order language.

[^note-8]: For a detailed account of the proof of the independence of the Axiom of Choice, see Bell 2005 or Jech 1973.

[^note-9]: For the proof of *ZL* from *AC* in **ZF**, see Mendelson 1987 (Ch. 4, sect. 5). For a proof not using ordinals, and so formulable in Zermelo set theory, see Bourbaki 1950 or Lawvere and Rosebrugh 2003 (Appendix B).

[^note-10]: Thus a nest in $S$ is a chain in $S$ partially ordered by set inclusion.

[^note-11]: That minimal samplings are transversals requires demonstration. Suppose $S$ is a minimal sampling; then, given $X\in \mathcal{I}$ either (1) $S\cap X$ is finite nonempty or (2) $X \subseteq S$. In case (1) $S\cap X$ cannot contain two distinct elements because the removal of one of them from $S$ would yield a sampling smaller than $S$, violating its minimality. So in this case $S\cap X$ must be a singleton. In case (2) $S$ cannot contain two distinct elements $a$, $b$ since, if it did, $S' = [(S - X) \cup \{a\}]$ would be a sampling smaller than $S$ (notice that $S' \cap X = \{a\}$ and the relations of $S'$ with the members of $\mathcal{I} - \{X\}$ are the same as those of $S$), again violating the minimality of $S$. So in this case $X$, and *a fortiori* $S\cap X$ must be a singleton.

[^note-12]: Had we elected to follow more closely the intuitive combinatorial derivation of *AC* as sketched above by using selectors instead of samplings we would have encountered the obstacle that—unlike the set of samplings—the set of selectors is not necessarily reductive.

[^note-13]: For equivalents of the Axiom of Choice, see Rubin and Rubin 1985; for consequences, see Howard and Rubin 1998.

[^note-14]: “Weaker” here means that, within the context of the axioms of set theory (minus, of course, *AC*), the proposition in question is entailed by *AC*, but not vice-versa.

[^note-15]: The idea of the proof goes back to Goodman and Myhill 1978, which was itself built on a result of Diaconescu 1975. See below.

[^note-16]: See Bishop and Bridges 1985.

[^note-17]: See Supplementary Document. For an analysis of various versions of *AC* within constructive type theory, see Martin-Löf 2006.

[^note-18]: Also, of course, use was made of $0 \ne 1$, but this assumption is so weak that it may be consistently added to virtually any axiomatic system.

[^note-19]: But in weak set theories lacking the axiom of extensionality the derivation of Excluded Middle from *AC* does not go through: some form of extensionality, or the existence of quotient sets for equivalence relations, needs to be assumed. See Bell 2008.

[^note-20]: With Zorn’s Lemma the situation is otherwise. For despite its equivalence to *AC* in classical set theory, in intuitionistic set theory Zorn’s Lemma *does not imply* **LEM:** in fact, it has no “non-constructive” logical consequences whatsoever (Grayson 1975, Bell 1997)[^bell-1997][^grayson-1975]. Thus Zorn’s Lemma is considerably weaker than *AC* in intuitionistic set theory. Intuitionistic equivalents of Zorn’s Lemma are scarce; a few have been formulated in Bell 2003.

[^note-21]: That is, the set of all $R$-equivalence classes of members of $A$.

[^aczel-1978]: Aczel, P., 1978. “The type-theoretic interpretation of constructive set theory,” in A. ManIntyre, L. Pacholski, and J. Paris (eds.), *Logic Colloquium 77*, Amsterdam: North-Holland, pp. 55–66.

[^aczel-1982]: –––, 1982. “The type-theoretic interpretation of constructive set theory: choice principles,” in A. S. Troelstra and D. van Dalen (eds.), *The L.E.J. Brouwer Centenary Symposium*, Amsterdam: North-Holland, pp. 1–40.

[^aczel-2002]: Aczel, P. and N. Gambino, 2002. “Collection principles in dependent type theory,” in P. Callaghan, Z. Luo, J. McKinna and R. Pollack (eds.), *Types for Proofs and Programs* (Lecture Notes on Computer Science, Volume 2277), Berlin: Springer, pp. 1–23.

[^aczel-2005]: –––, 2005. “The generalized type-theoretic interpretation of constructive set theory,” *Journal of Symbolic Logic*, 71/1: 67–103. [[Preprint available online in compressed Postscript](http://www.cs.man.ac.uk/~petera/gambino-aczel.ps.gz)]

[^aczel-2013]: Aczel, P., Berg, B. and J. Granstrom, 2013. “Are there enough injective sets?,” *Studia Logica*, 101(3): 467–482.

[^aczel-2001]: Aczel, P. and M. Rathjen, 2001. *Notes on Constructive Set Theory*. Technical Report 40, Mittag-Leffler Institute, The Swedish Royal Academy of Sciences. [[Preprint available online](http://www.mittag-leffler.se/sites/default/files/IML-0001-40.pdf)]

[^banach-1924]: Banach, S. and Tarski, A., 1924. “Sur la décomposition des ensembles de points en parties respectivement congruentes,” *Fundamenta Mathematicae*, 6: 244–277.

[^bell-1983]: Bell, J.L., 1983. “On the strength of the Sikorski extension theorem for Boolean algebras,” *Journal of Symbolic Logic*, 48: 841–846.

[^bell-1988]: –––, 1988. *Toposes and Local Set Theories: An Introduction*, Oxford: Clarendon Press.

[^bell-1997]: –––, 1997. “Zorn’s lemma and complete Boolean algebras in intuitionistic type theories,” *Journal of Symbolic Logic*, 62: 1265–1279.

[^bell-2003]: –––, 2003. “Some new intuitionistic equivalents of Zorn’s Lemma,” *Archive for Mathematical Logic*, 42: 811–814.

[^bell-2005]: –––, 2005. *Set Theory: Boolean-valued Models and Independence Proofs*, Oxford: Clarendon Press.

[^bell-2006]: –––, 2006. “Choice principles in intuitionistic set theory,” in *A Logical Approach to Philosophy*, Devidi, D. and Kenyon, T.(eds.), Berlin: Springer, 36–44.

[^bell-2008]: –––, 2008. “The axiom of choice and the law of excluded middle in weak set theories,” *Mathematical Logic Quarterly*, 48: 841–846.

[^bell-2009]: –––, 2009. *The Axiom of Choice*, London: College Publications.

[^bell-2011]: –––, 2011. “The axiom of choice in an elementary theory of operations and sets” in *Analysis and Interpretation in the Exact Sciences*, Devidi, D. and Kenyon, T.(eds.), Berlin: Springer, 163–175.

[^bell-1972]: Bell, J.L. and Fremlin, D., 1972. “The maximal ideal theorem for lattices of sets,” *Bulletin of the London Mathematical Society*, 4: 1–2.

[^bell-1972a]: –––, 1972a. “A geometric form of the axiom of choice,” *Fundamenta Mathematicae*, 77: 167–170.

[^bell-1977]: Bell, J.L. and Machover, M. , 1977. *A Course in Mathematical Logic*. Amsterdam: North-Holland.

[^bernays-1942]: Bernays, P., 1942. “A system of axiomatic set theory, Part III,” *Journal of Symbolic Logic*, 7: 65–89.

[^bishop-1985]: Bishop, E. and Bridges, D., 1985. *Constructive Analysis*, Berlin: Springer.

[^blass-1984]: Blass, A., 1984. “Existence of bases implies the axiom of choice,” in *Axiomatic Set Theory*, Baumgartner, Martin and Shelah (eds.) (Contemporary Mathematics Series, Volume 31), American Mathematical Society, pp. 31–33.

[^bochner-1928]: Bochner, S., 1928. “Fortsetzung Riemannscher Flachen,” *Mathematische Annalen*, 98: 406–421.

[^bourbaki-1939]: Bourbaki, N., 1939. *Elements de Mathematique, Livre I: Theorie des Ensembles*, Paris: Hermann.

[^bourbaki-1950]: –––, 1950.“Sur le theoreme de Zorn,” *Archiv dem Mathematik*, 2: 434–437.

[^cohen-1963]: Cohen, P.J., 1963. “The independence of the continuum hypothesis I,” *Proceedings of the U.S. National Academy of Sciemces*, 50: 1143–48. [The independence of the Axiom of Choice from the standard axioms of set theory, ZF, is part of Theorem 1 of this paper.]

[^cohen-1964]: –––, 1964. “The independence of the continuum hypothesis II,” *Proceedings of the U.S. National Academy of Sciemces*, 51: 105–110.

[^cohen-1966]: –––, 1966. *Set Theory and the Continuum Hypotheis*, New York: Benjamin.

[^curry-1958]: Curry, H.B. and R. Feys, 1958. *Combinatory Logic*, Amsterdam: North Holland.

[^devidi-2004]: Devidi, D., 2004. “Choice principles and constructive logics,” *Philosophia Mathematica*, 12(3): 222–243.

[^diaconescu-1975]: Diaconescu, R., 1975. “Axiom of choice and complementation,” *Proceedings of the American Mathematical Society*, 51: 176–8.

[^fraenkel-1922]: Fraenkel, A., 1922. “Zu den Grundlagen der Cantor-Zermeloschen Mengenlehre”, *Mathematische Annalen*, 86: 230–237.

[^fraenkel-1922a]: Fraenkel, A., 1922a.“Über den Begriff ‘definit’ und die Unabhängigkeit des Auswahlsaxioms,” *Sitzungsberichte der Preussischen Akademie der Wissenschaften, Physik-math. Klasse*, 253–257. Translated in van Heijenoort, From Frege to Gödel: A Source Book in Mathematical Logic 1879–1931, Harvard University Press, 1967, pp. 284–289.

[^fraenkel-1973]: Fraenkel, A., Y. Bar-Hillel and A. Levy, 1973. *Foundations of Set Theory*, Amsterdam: North-Holland, 2ⁿᵈ edition.

[^gödel-1938a]: Gödel, K., 1938a. “The consistency of the axiom of choice and of the generalized continuum-hypothesis,” *Proceedings of the U.S. National Academy of Sciences*, 24: 556–7.

[^gödel-1938b]: Gödel, K., 1938b. “Consistency-proof for the generalized continuum-hypothesis,” *Proceedings of the U.S. National Academy of Sciemces*, 25: 220–4.

[^gödel-1940]: Gödel, K., 1940. *The Consistency of the Axiom of Choice and of the Generalized Continuum-Hypothesis with the Axioms of Set Theory*, Annals of Mathematics Studies, No. 3, Princeton: Princeton University Press.

[^gödel-1964]: Gödel, K., 1964. “Remarks before the Princeton Bicentennial Conference,” in *The Undecidable*, Martin Davis (ed.), CITY: Raven Press, pp. 84–88.

[^goodman-1978]: Goodman, N. and Myhill, J., 1978. “Choice implies excluded middle,” *Zeitschrift fur Mathematische Logik und Grundlagen der Mathematik* , 24(25–30): 461.

[^grattan-guinness-2012]: Grattan-Guinness, I., 2012. “Jourdain, Russell and the axiom of choice: a new document,” *Russell: The Journal of the Bertrand Russell Archives*, 32(1): 69–74.

[^grayson-1975]: Grayson, R.J., 1975. “A sheaf approach to models of set theory,” M.Sc. Thesis, Mathematics Department, Oxford University.

[^halpern-1971]: Halpern, , J.D. and Levy, A., 1971. “The Boolean prime ideal theorem does not imply the axiom of choice,” *Axiomatic Set Theory*, Proceedings of Symposia in Pure Mathematics, Vol. XIII, Part I. American Mathematical Society, pp. 83–134.

[^hamel-1905]: Hamel, G., 1905. “Eine Basis aller Zahlen und die unstetigen Lösungen der Funktionalgleichung: *f(x* + *y*) = *f(x*) + *f(y*),” *Mathematische Annalen*, 60: 459–62.

[^hausdorff-1909]: Hausdorff, F., 1909. “Die Graduierung nach dem Endverlauf,” *Königlich Sächsichsen Gesellschaft der Wissenschaften zu Leipzig, Math.—Phys. Klasse, Sitzungberichte*, 61: 297–334.

[^hausdorff-1914]: –––, 1914. *Grundzüge der Mengenlehre*, Leipzig: de Gruyter. Reprinted, New York: Chelsea, 1965.

[^hausdorff-1914a]: –––, 1914a. “Bemerkung über den Inhalt von Punktmengen,” *Mathematische Annalen*, 75: 428–433.

[^hilbert-1926]: Hilbert D., 1926. “Über das Unendliche,” *Mathematische Annalen*, 95. Translated in J. van Heijenoort (ed.) *From Frege to Gödel: A Source Book in Mathematical Logic, 1879–1931*, Cambridge, MA: Harvard University Press, 1967, pp. 367–392.

[^hodges-1979]: Hodges, W., 1979. “Krull implies Zorn,” *Journal of the London Mathematical Society*, 19: 285–7.

[^howard-1998]: Howard, P. and Rubin, J. E., 1998. *Consequences of the Axiom of Choice*, American Mathematical Society Surveys and Monographs, Vol. 59.

[^howard-1980]: Howard, W. A., 1980. “The formulae-as-types notion of construction,” in J. R. Hindley and J. P. Seldin (eds.), *To H. B. Curry: Essays on Combinatorial Logic. Lambda Calculus and Formalism*, New York and London: Academic Press, pp. 479–490.

[^jacobs-1999]: Jacobs, B., 1999. *Categorical Logic and Type Theory*, Amsterdam: Elsevier.

[^jech-1973]: Jech, T., 1973. *The Axiom of Choice*, Amsterdam: North-Holland.

[^kelley-1950]: Kelley, J.L., 1950. “The Tychonoff product theorem implies the axiom of choice,” *Fundamenta Mathematicae*, 37: 75–76.

[^klimovsky-1958]: Klimovsky, G., 1958. “El teorema de Zorn y la existencia de filtros a ideales maximales en los reticulados distributivos,” *Revista de la Union Matematica Argentina* , 18: 160–64.

[^kuratowski-1922]: Kuratowski, K., 1922. “Une méthode d’élimination des nombres transfinis des raissonements mathématiques,” *Fundamenta Mathematicae*, 3: 76–108.

[^lawvere-2003]: Lawvere, F. W. and Rosebrugh, R., 2003. *Sets for Mathematics*, Cambridge: Cambridge University Press.

[^lindenbaum-1938]: Lindenbaum, A., and Mostowski, A., 1938. “Über die Unabhängigkeit des Auswahlsaxioms und einiger seiner Folgerungen,” *Comptes Rendus des Séances de la Société des Sciences et des Lettres de Varsovie*, 31: 27–32.

[^maietti-2005]: Maietti, M.E., 2005. “Modular correspondence between dependent type theories and categories including pretopoi and topoi,” *Mathematical Structures in Computer Science*, 15/6: 1089–1145.

[^martin-löf-1975]: Martin-Löf, P., 1975. “An Intuitionistic theory of types; predicative part,” in H. E. Rose and J. C. Shepherdson (eds.), *Logic Colloquium 73*, Amsterdam: North-Holland, pp. 73–118.

[^martin-löf-1982]: –––, 1982. “Constructive mathematics and computer programming,” in L. C. Cohen, J. Los, H. Pfeiffer, and K.P. Podewski (eds.), *Logic, Methodology and Philosophy of Science VI*, Amsterdam: North-Holland, pp. 153–179.

[^martin-löf-1984]: –––, 1984. *Intuitionistic Type Theory*, Naples: Bibliopolis.

[^martin-löf-2006]: –––, 2006. “100 years of Zermelo’s axiom of choice: what was the problem with it?,” *The Computer Journal*, 49(3): 345–350.

[^mendelson-1956]: Mendelson, E., 1956. “The independence of a weak axiom of choice,” *Journal of Symbolic Logic*, 21: 350–366.

[^mendelson-1958]: –––, 1958. “The axiom of fundierung and the axiom of choice,” *Arkiv fur Mathematische Logik und Grundlagenforschung*, 4: 67–70.

[^mendelson-1987]: –––, 1987. *Introduction to Mathematical Logic*, CITY: Wadsworth & Brooks, 3rd edition.

[^moore-1982]: Moore, G.H., 1982. *Zermelo’s Axiom of Choice*, Berlin: Springer-Verlag.

[^moore-1932]: Moore, R.L., 1932. *Foundations of Point Set Theory*, Anerican Mathematical Society Colloquium Publications, vol. 13.

[^myhill-1971]: Myhill, J. and Scott, D.S., 1971. “Ordinal definability,” *Axiomatic Set Theory*. Proceedings of Symposia in Pure Mathematics, Vol. XIII, Part I. American Mathematical Society, pp. 271–8.

[^post-1953]: Post, E.L., 1953. “A necessary condition for definability for transfinite von Neumann-Gödel set theory sets, with an application to the problem of the existence of a definable well-ordering of the continuum.” Preliminary Report, *Bulletin of the American Mathematical Society*, 59: 246.

[^ramsey-1926]: Ramsey, F. P., 1926. “The foundations of mathematics,” *Proceedings of the London Mathematical Society*, 25: 338–84. Reprinted in *The Foundations of Mathematics and Other Essays*, D.H. Mellor, ed. London: Routledge, 2001.

[^rubin-1985]: Rubin, H. and Rubin, J. E., 1985. *Equivalents of the Axiom of Choice II*, Amsterdam: North-Holland.

[^rubin-1954]: Rubin, H. and Scott, D.S., 1954. “Some topological theorems equivalent to the prime ideal theorem,” *Bulletin of the American Mathematical Society*, 60: 389.

[^russell-1906]: Russell, B., 1906. “On some difficulties in the theory of transfinite numbers and order types,” *Proceedings of the London Mathematical Society*, 4(2): 29–53.

[^shoenfield-1955]: Shoenfield, J. R., 1955. “The independence of the axiom of choice,” *Journal of Symbolic Logic*, 20: 202.

[^sikorski-1948]: Sikorski, R., 1948. “A theorem on extensions of homomorphisms,” *Annales de la Societé Polonaise de Mathématiques*, 21: 332–35.

[^solovay-1970]: Solovay, R., 1970. “A model of set theory in which every set of reals is Lebesgue measurable,” *Annals of Mathematics*, 92: 1–56.

[^specker-1957]: Specker, E., 1957. “Zur Axiomatik der Mengenlehre (Fundierungs- und Auswahlaxiom),” *Zeit. Math. Logik und Grund.*, 3: 173–210.

[^steinitz-1910]: Steinitz, E., 1910. “Algebraische Theorie der Körper,” *Journal für die Reine und angewandte Mathematik (Crelle)*, 137: 167–309.

[^stone-1936]: Stone, M.H., 1936. “The theory of representations for Boolean algebras,” *Transactions of the American Mathematical Society*, 40: 37–111.

[^tait-1994]: Tait, W. W., 1994. “The law of excluded middle and the axiom of choice,” in *Mathematics and Mind*, A. George (ed.), New York: Oxford University Press, pp. 45–70.

[^takeuti-1961]: Takeuti, G., 1961. “Remarks on Cantor’s Absolute,” *Journal of the Mathematical Society of Japan*, 13: 197–206.

[^tarski-1948]: Tarski, A., 1948. “Axiomatic and algebraic aspects of two theorems on sums of cardinals,” *Fundamenta Mathematicae*, 35: 79–104.

[^tarski-1957]: Tarski, A., and Robert L. Vaught, 1957. “Arithmetical extensions of relational systems,” *Compositio Mathematica*, 13: 81–102. [[Tarski & Vaught 1957 available online](http://www.numdam.org/article/CM_1956-1958__13__81_0.pdf)]

[^teichmuller-1939]: Teichmuller, O., 1939. “Brauch der Algebraiker das Auswahlaxiom?” *Deutsches Mathematik*, 4: 567–577.

[^vitali-1905]: Vitali, G., 1905. *Sul problema della misura dei gruppi di punti di una retta*, Bologna: Tip. Gamberini e Parmeggiani.

[^wagon-1993]: Wagon, S., 1993.*The Banach-Tarski Paradox*, Cambridge University Press.

[^zermelo-1904]: Zermelo, E., 1904. “Neuer Beweis, dass jede Menge Wohlordnung werden kann (Aus einem an Herrn Hilbert gerichteten Briefe)”, *Mathematische Annalen*, 59: 514–16. Translated in J. van Heijenoort (ed.), *From Frege to Gödel: A Source Book in Mathematical Logic, 1879–1931*, Cambridge, MA: Harvard University Press, 1967, pp. 139–141.

[^zermelo-1908]: –––, 1908. Neuer Beweis für die Möglichkeit einer Wohlordnung, *Mathematische Annalen*, 65: 107–128. Translated in J. van Heijenoort (ed.), *From Frege to Gödel: A Source Book in Mathematical Logic, 1879–1931*, Cambridge, MA: Harvard University Press, 1967, pp. 183–198.

[^zermelo-1908a]: –––, 1908a.“Untersuchungen uber die Grundlagen der Mengenlehre,” *Mathematische Annalen*, 65: 107–128. Translated in J. van Heijenoort (ed.), *From Frege to Gödel: A Source Book in Mathematical Logic, 1879–1931*, Cambridge, MA: Harvard University Press, 1967, pp. 199–215.

[^zorn-1935]: Zorn, M., 1935. A remark on method in transfinite algebra, *Bulletin of the American Mathematical Society*, 41: 667–70.

### 补充文档注记：选择公理与类型论

1. 依赖类型实际上最早由 de Bruijn 及其埃因霍温大学同事于 20 世纪 60 年代末在 AUTOMATH 项目中研究。**CDTT** 已被用作多种计算装置的基础，这些装置用于验证数学理论以及计算机科学中的软件和硬件系统。

2. Peter Aczel 发展了类似的、包含选择原理的构造性集合论版本。参见 Aczel 1978、1982、2005 与 Aczel & Rathjen 2001。

3. 这一想法由 Curry 与 Feys 1958 提出，后由 Howard 1980 推进。作为“柯里-霍华德对应”（Curry–Howard correspondence），它在理论计算机科学中已发挥重要作用。

4. 关于 DCTT 的运算与规则的完整规定，参见 Jacobs 1999 第 10 章或 Gambino & Aczel 2005。

5. 参见 §4。

6. 有趣的是，Ramsey 1926 也断言 *AC* 的重言式特征，但理由颇为不同。与 Zermelo 一样，Ramsey 把 *AC* 理解为断言选择函数的客观存在，并接受其为真；这种存在是外延地给出的，因而独立于描述它们的方式。但构造性数学、尤其是 **CDTT** 的内涵性质决定：没有任何东西可以完全独立于其描述而被给出。这导致对量词的强读法；正如我们已经看到的，这种读法实质上使 *AC* 成为琐屑的，因为它使构成该蕴涵的前件本质上等价于后件。值得注意的是，无论从外延观点还是从内涵观点看，*AC* 都可被视为重言式。

7. 在经典集合论中，这种意义上的每个单元素集要么是空的，要么是一元集；而在直觉主义集合论中，有许多额外的“中间”集合也符合单元素集的资格。


## 译者注释

① 正文作“Sikorski 1949”，书目条目作 `sikorski-1948`（1948）；上游两处年份不一致，译文照录，未改。
