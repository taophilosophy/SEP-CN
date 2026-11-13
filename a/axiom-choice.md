# 选择公理 The Axiom of Choice (John L. Bell)

*首次发表于 2008 年 1 月 8 日；2021 年 12 月 10 日实质修订。*

集合论中称为**选择公理**的原理，曾被誉为“也许是数学中最有趣、并且尽管出现较晚，却是讨论得最多的公理，仅次于两千多年前引入的欧几里得平行公理”（Fraenkel, Bar-Hillel & Levy 1973, §II.4）。这番溢美之辞，或许会让不熟悉该公理的人期待它与光速不变原理或海森堡不确定性原理一样惊人。但事实上，选择公理按通常陈述方式看显得平淡无奇，甚至自明。因为它无非是断言：给定任意一族互不相交的非空集合，可以把它们合并成一个新集合——一个**横截**（*transversal*）或**选择集**——其中恰好含有该族每个成员中的一个元素。然而，这个看似无害的原理有着深远的数学后果——许多不可或缺，有些令人震惊——并且已在数学基础讨论中占据显著位置。它（或它的等价形式）已被用于无数数学论文，还有若干专著专门讨论它。

## 1 选择公理的起源与年表

1904 年，恩斯特·策梅洛以他所谓的**覆盖**（*coverings*）表述了选择公理（本文以下简记为 *AC*）（Zermelo 1904）[^zermelo-1904]。他从任意集合 $M$ 出发，用符号 $M'$ 表示 $M$ 的任意非空子集，并用 M 表示这些子集的汇集。他接着写道：

> 设想对每个子集 $M'$ 都联系着一个出现于 $M'$ 本身的任意元素 $m_{1}'$；称 $m_{1}'$ 为 $M'$ 的“特异”元素。这就产生了集合 $M$ 由集合 $M$ 的某些元素构成的一个“覆盖” $g$。这些覆盖的数目等于[所有子集 $M'$ 的基数]之积，并且肯定不等于 0。

这段引文的最后一句实际上断言：对任意（非空）集合的非空子集族，覆盖总是存在——是策梅洛对选择公理的最初表述[^note-1]。如今这通常用**选择函数**来陈述：集合族 ${\mathcal{H}}$ 上的一个选择函数是一个映射 $f$，其定义域为 ${\mathcal{H}}$，且对每个 $X \in {\mathcal{H}}$ 都有 $f(X) \in X$。

作为一个很简单的例子，令 ${\mathcal{H}}$ 为 $\{0, 1\}$ 的非空子集组成的族，即 ${\mathcal{H}} = \{\{0\}, \{1\}, \{0,1\}\}$。那么 ${\mathcal{H}}$ 有两个不同的选择函数 $f_{1}$ 与 $f_{2}$，由下式给出：

\begin{align} f_{1}(\{0\}) &= 0 \\ f_{1}(\{1\}) &= 1 \\ f_{1}(\{0, 1\}) &= 0 \\ f_{2}(\{0\}) &= 0 \\ f_{2}(\{1\}) &= 1 \\ f_{2}(\{0, 1\}) &= 1 \end{align}

一个更有趣的选择函数例子是：取 ${\mathcal{H}}$ 为实数（无序）对的集合，取函数为给每一对指派其最小元素。若给每一对指派其最大元素，则得到另一个选择函数。显然，还可以在 ${\mathcal{H}}$ 上定义更多选择函数。

用选择函数来陈述，策梅洛对 *AC* 的最初表述是：

**AC1**：任意非空集合族都有一个选择函数。

**AC1** 可以用**索引集**或**变元集**重新表述。索引集族 ${\mathcal{A}} = \{A_{i}: i \in I\}$ 可以设想为一个**变元集**，即在索引集 $I$ 上**变化**的集合。每个 $A_{i}$ 于是就是变元集 ${\mathcal{A}}$ 在**阶段** $i$ 的“值”。${\mathcal{A}}$ 上的一个**选择函数**是一个映射 $f: I \rightarrow \bigcup_{i\in I} A_{i}$，使得对所有 $i\in I$ 都有 $f(i) \in A_{i}$。因此，${\mathcal{A}}$ 上的选择函数就是在每个阶段对变元集 ${\mathcal{A}}$ 的一个元素作出的“选择”；换言之，${\mathcal{A}}$ 上的选择函数是 ${\mathcal{A}}$ 的一个**变元元素**。于是 **AC1** 等价于如下断言：

**AC2**：任意索引集族都有一个选择函数。

非正式地说，**AC2** 相当于断言：在每个阶段都有元素的变元集，有一个变元元素。

**AC1** 也可以用关系来重新表述，即：

**AC3**：对集合 $A$、$B$ 之间的任意关系 $R$，

$$ {\forall x\,{\in}\, A}\ \exists y\,{\in}\, B[R(x,y)] \Rightarrow \exists f[f: A \rightarrow B \mathbin{\&} {\forall x\,{\in}\, A}[R(x,fx)]]. $$

换言之，每个关系都包含一个具有相同定义域的函数。

最后，**AC3** 容易证明（在通常的集合论中）等价于：[^note-2]

**AC4**：任意满射函数都有右逆。

在 1908 年的一篇论文中，策梅洛引入了 *AC* 的一个修改形式。对于集合族 ${\mathcal{H}}$，我们把任一子集 $T \subseteq \bigcup {\mathcal{H}}$ 称为其**横截**（或**选择集**），只要对每个 $X \in {\mathcal{H}}$，交集 $T \cap X$ 恰好含有一个元素。作为一个很简单的例子，令 ${\mathcal{H}} = \{\{0\}, \{1\}, \{2, 3\}\}$。那么 ${\mathcal{H}}$ 有两个横截 $\{0, 1, 2\}$ 与 $\{0, 1, 3\}$。一个更实质的例子是：令 ${\mathcal{H}}$ 为欧几里得平面中所有平行于 $x$ 轴的直线组成的族。那么 $y$ 轴上所有点构成的集合 $T$ 就是 ${\mathcal{H}}$ 的一个横截。

用横截来陈述，策梅洛 1908 年的第二个表述相当于断言：任意一族互不相交的非空集合都有一个横截。[^note-3]

策梅洛断言，这一原理“纯客观的性质”“是直接显明的”。作出这一断言时，策梅洛意在强调：在这一形式中，该原理并未诉诸作出“选择”的可能性。策梅洛心中也可能对该原理有如下“组合”辩护。给定一族互不相交的非空集合 ${\mathcal{H}}$，称子集 $S \subseteq \bigcup {\mathcal{H}}$ 为 ${\mathcal{H}}$ 的**选择子**，如果对所有 $X \in {\mathcal{H}}$ 都有 $S\cap X \ne \varnothing$。显然 ${\mathcal{H}}$ 的选择子存在；$\bigcup {\mathcal{H}}$ 本身就是一例。现在可以设想取 ${\mathcal{H}}$ 的一个选择子 $S$，并把每个交集 $S \cap X$（$X\in {\mathcal{H}}$）“削薄”，直到它只含一个元素。结果就是 ${\mathcal{H}}$ 的一个横截。这一论证经过适当精细化，就从称为**佐恩引理**的集合论原理（见下文）给出了此形式下 *AC* 的精确推导。

我们把策梅洛 1908 年的表述称为**组合**选择公理：

**CAC**：任意一族互不相交的非空集合都有一个横截。

应当注意，对**有限**集合族，**AC1** 与 **CAC** 在通常的集合论中都可（用归纳法）证明。但对**无限**族，即便其每个成员都是有限的，选择函数或横截的存在性问题也是麻烦的[^note-4]。例如，如前所述，很容易为实数对的族给出一个选择函数（只需选每对中较小的元素）。但如何为**任意实数集**所成对的族给出选择函数，则远非显然。

策梅洛引入 *AC* 的最初目的，是确立康托集合论的一个核心原理，即每个集合都容许一个良序，因而也可以被指派一个基数。策梅洛 1904 年对该公理的引入，以及他对它的运用，招致了当时数学家的相当多批评。主要反对意见针对的是它那种在某些人看来高度非构造性、甚至唯心主义的特征：该公理断言可以作出若干——甚至不可数多个——任意的“选择”，却丝毫没有说明这些选择实际上如何实现，换言之，选择函数如何被**定义**。这对“构造性”倾向的数学家尤其难以接受，例如所谓法国经验主义者贝尔、博雷尔与勒贝格，对他们来说，一个数学对象只有能以唯一刻画它的方式被定义时，才能断言其存在。策梅洛在 1908 年的两篇论文中回应了批评者。在第一篇中，如上所述，他用横截重新表述了 *AC*；在第二篇（1908a）中，他明确陈述了完成良序定理证明所需的进一步假定。这些假定构成了集合论公理系统的首次明确呈现。

随着关于选择公理的争论持续发酵，人们逐渐看清：若干重要数学定理的证明都本质地使用了它，从而使许多数学家把它视为本行不可或缺的工具。例如，希尔伯特把 *AC* 视为数学的一项本质原理[^note-5]，并用它来为经典数学推理辩护，以回应直觉主义者的攻击。事实上，他的 ε-算子本质上就是选择函数（见 epsilon 演算词条）。

尽管 *AC* 的用处很快变得清楚，对其可靠性的怀疑仍然存在。这些怀疑因该公理有一些引人注目的反直觉后果而得到加强。其中最壮观的是巴拿赫与塔斯基的**球体悖论分解**（Banach and Tarski 1924）[^banach-1924]：任意实心球都可以分成有限多块，这些块可以重新拼合成两个同样大小的实心球；并且任意实心球都可以分成有限多块，使它们能重新拼合成一个任意大小的实心球。（见 Wagon 1993。）[^wagon-1993]

直到 1930 年代中期，库尔特·哥德尔证明了 *AC* 相对于集合论其他公理的一致性，关于 *AC* 可靠性的问题才最终平息。

以下是 *AC* 的简要年表：[^note-6]

| 1904/1908 | 策梅洛引入集合论公理，明确表述 *AC* 并用它证明良序定理，由此激起轩然大波。 |
| --- | --- |
| 1904 | 罗素认识到 *AC* 即**乘法公理**：任意非零基数的积非零。 |
| 1914 | 豪斯多夫从 *AC* 推出不可测集的存在，其“悖论式”形式是：球的 ${^{1}\unicode{x2044}_{2}}$ 与它的 ${^{1}\unicode{x2044}_{3}}$ 全等（Hausdorff 1914）[^hausdorff-1914]。 |
| 1922 | 弗兰克尔引入“置换方法”，以确立 *AC* 相对于带原子的集合论系统的独立性（Fraenkel 1922）[^fraenkel-1922]。 |
| 1924 | 巴拿赫与塔斯基在豪斯多夫工作的基础上，从 *AC* 推出他们的球体悖论分解。 |
| 1926 | 希尔伯特在其证明论中引入“超限”或“epsilon”公理，作为 *AC* 的一个版本。（Hilbert 1926）[^hilbert-1926]。 |
| 1936 | 林登鲍姆与莫斯托夫斯基扩展并改进了弗兰克尔的置换方法，并证明了若干弱于 *AC* 的集合论陈述的独立性。（Lindenbaum and Tarski 1938）[^lindenbaum-1938] |
| 1935–38 | 哥德尔确立 *AC* 相对于集合论公理的一致性（Gödel 1938a, 1938b, 1939, 1940）[^gödel-1938a]。 |
| 1950s | 门德尔松、舍恩菲尔德与施佩克各自独立地使用置换方法，确立 *AC* 的各种形式相对于一个既无原子、又缺少基础公理的集合论系统的独立性（Mendelson 1956, 1958, Shoenfield 1955, Specker 1957）[^mendelson-1956][^shoenfield-1955][^specker-1957]。 |
| 1963 | 保罗·科恩证明 *AC* 相对于集合论标准公理的独立性（Cohen 1963, 1964）[^cohen-1963]。 |

## 2 选择公理的独立性与一致性

如上所述，1922 年弗兰克尔证明了 *AC* 相对于一个含“原子”的集合论系统的独立性。这里**原子**指纯粹个体，即没有成员却又不同于空集的实体（因此**原子**绝不可能是集合）。在带原子的集合论系统中，假定给出了一个无限原子集 $A$。可以从 $A$ 出发，加上 $A$ 的所有子集，再加上所得结果的所有子集，如此超限迭代，在 $A$ 上构造一个集合的宇宙 $V(A)$。$V(A)$ 于是就是带原子集合论的一个模型。弗兰克尔证明 *AC* 独立性方法的核心，是这样一种观察：既然原子不能在集合论上被区分，原子集 $A$ 的任一置换都诱导出由 $A$ 构造的集合宇宙 $V(A)$ 的一个保结构置换——一个**自同构**。这一想法可用来构造集合论的另一个模型 $Sym(V)$——一个**置换模型**或**对称模型**——在其中，由 $A$ 的元素组成的某个互不相交的对之集合没有选择函数。

现在假定给出了 $A$ 的一个自同构群 $G$。我们说 $A$ 的一个自同构 $\pi$ **固定** $V(A)$ 的元素 $x$，如果 $\pi(x) = x$。显然，若 $\pi \in G$ 固定 $A$ 的每个元素，它也就固定 $V(A)$ 的每个元素。现在可能出现这样的情况：对某些 $x \in V(A)$，任一 $\pi\in G$ 对 $A$ 的某个**子集**之元素的固定，就足以固定 $x$。于是我们被引向把 $x$ 的**支撑**定义为 $A$ 的子集 $X$，使得只要 $\pi\in G$ 固定 $X$ 的每个成员，它也就固定 $x$。$V(A)$ 中拥有**有限**支撑的成员称为**对称的**。

我们接着把宇宙 $Sym(V)$ 定义为 $V(A)$ 中**遗传对称**的成员，即这样的 $x\in V(A)$：$x$、$x$ 的元素、$x$ 的元素的元素等等全部是对称的。$Sym(V)$ 也是以 $A$ 为原子集的集合论的一个模型，且 $\pi$ 诱导出 $Sym(V)$ 的一个自同构。

现在假定 $A$ 被划分成一个（必然无限的）互不相交的对之集合 $P$。取 $G$ 为 $A$ 的固定 $P$ 中所有对的置换群。那么 $P\in Sym(V)$；现在可以证明 $Sym(V)$ 中不含 $P$ 上的选择函数。因为假定 $f$ 是 $P$ 上的选择函数且 $f \in Sym(V)$。那么 $f$ 有一个有限支撑，可以取形式 $\{a_{1}, \ldots, a_{n}, b_{1},\ldots,b_{n}\}$，其中每个对都属于 P。由于 $P$ 无限，我们可以从 $P$ 中选取一个不同于所有 $\{a_{i}, b_{i}\}$ 的对 $\{c, d\} = U$。现在定义 $\pi \in G$，使 $\pi$ 固定每个 $a_{i}$ 与 $b_{i}$，并交换 $c$ 与 $d$。那么 $\pi$ 也固定 $f$。既然 $f$ 被假定为 $P$ 上的选择函数，且 $U \in P$，我们必须有 $f(U) \in U$，即 $f(U) = c$ 或 $f(U) = d$。由于 $\pi$ 交换 $c$ 与 $d$，可知 $\pi(f(U)) \ne f(U)$。但既然 $\pi$ 是自同构，它也保持函数应用，于是 $\pi(f(U)) = \pi f(\pi(U))$。但 $\pi(U) = U$ 且 $\pi f = f$，所以 $\pi(f(U)) = f(U)$。我们由此得到矛盾，表明宇宙 $Sym(V)$ 不含 $P$ 上的选择函数。

这里的要点是：对定义在 $P$ 上的对称函数 $f$，存在 $P$ 中对的有限列表 $L$，固定其中所有元素就足以固定 $f$，因而也足以固定 $f$ 的所有值。现在，对 $P$ 中任一不在 $L$ 中的对 $U$，总能找到一个置换 $\pi$，它固定 $L$ 中所有对的元素，却不固定 $U$ 的成员。既然 $\pi$ 必须固定 $f$ 在 $U$ 处的值，该值就不能落在 $U$ 中。因此 $f$ 不能“选择” $U$ 的一个元素，所以 $f$ 绝不可能是 $P$ 上的选择函数。

这一论证表明，**原子集之集**的族不必都有选择函数；但它未能对数学中“通常”的集合确立同样的事实，例如实数集。直到 1963 年，保罗·科恩才表明：与集合论标准公理（它们排除原子的存在）相容的是，存在一个可数的实数集对之族没有选择函数。科恩证明方法的核心——著名的**力迫**方法——比以往任何技术都远为普遍；不过他的独立性证明也本质地使用了置换与对称，其形式与弗兰克尔最初采用的实质相同。

哥德尔关于 *AC* 相对于集合论公理的一致性的证明（见库尔特·哥德尔词条）依据的是一个完全不同的想法：**可定义性**。他类比累积类型分层，引入了一个新的集合分层——**可构造**分层。我们记得，后者由如下超限递归定义，其中 ${\mathcal{P}}(X)$ 是 $X$ 的幂集，$\alpha$ 是序数，$\lambda$ 是极限序数：

\begin{align} V_0 &= \varnothing \\ V_{\alpha+1} &= \sP(V_{\alpha}) \\ V_{\lambda} &= {\bigcup}_{\alpha \lt \lambda} V_{\alpha} \end{align}

可构造分层由对序数的类似递归定义，其中 ${\mathrm{Def}}(X)$ 是 $X$ 的所有在结构 $(X, \in, (x)_{x\in X})$ 中一阶可定义的子集之集：[^note-7]

\begin{align} L_0 &= \varnothing \\ L_{\alpha+1} &= \Def(L_{\alpha}) \\ L_{\lambda} &= {\bigcup}_{\alpha\lt \lambda} L_{\alpha} \end{align}

**可构造宇宙**是类 $L = \bigcup_{\alpha\in {\mathrm{Ord}}} L_{\alpha}$；$L$ 的成员是**可构造集**。哥德尔表明（假定策梅洛—弗兰克尔集合论 **ZF** 的公理），结构 $(L, \in)$ 是 **ZF** 的模型，同时也是 *AC* 以及广义连续统假设的模型。由此可得 *AC* 相对于 **ZF** 的一致性。

哥德尔（1964）还注意到（迈希尔与斯科特 1971、竹内外史 1963 与波斯特 1951 也独立注意到）[^myhill-1971]，*AC* 相对一致性的一个更简单证明可以用**序数可定义性**表述。若用 ${\mathrm{D}}(X)$ 表示 $X$ 的所有在结构 $(X, \in)$ 中一阶可定义的子集之集，则**序数可定义集**的类 OD 定义为并 $\bigcup_{\alpha\in {\mathrm{Ord}}} D(V_{\alpha})$。**遗传序数可定义集**的类 HOD 由所有这样的集合 $a$ 组成：$a$、$a$ 的成员、$a$ 的成员的成员……等等全是序数可定义的。于是可以证明结构 (HOD, $\in$) 是 **ZF** + *AC* 的模型，由此再次得到 *AC* 相对于 **ZF** 的一致性。[^note-8]

## 3 极大原理与佐恩引理

选择公理与一组统称为**极大原理**的数学命题密切相关。宽泛地说，这些命题断言：某些条件足以保证偏序集至少含有一个**极大元**，即相对于给定偏序没有元素严格超过它的元素。

为了看清极大元概念与 *AC* 的联系，让我们回到后者用索引集作出的表述 **AC2**。据此假定给出了非空集的索引族 ${\mathcal{A}} = \{A_{i}:i \in I\}.$ 我们把 ${\mathcal{A}}$ 上的**潜在选择函数**定义为一个函数 $f$，其定义域是 $I$ 的子集，且对所有 $i\in J$ 都有 $f(i) \in A_{i}$。（这里使用**潜在**这一限定语，是因为定义域是 $I$ 的子集；回想 ${\mathcal{A}}$ 上的选择函数 $f$ 与我们如今称为潜在选择函数的东西性质相同，只是要求 $f$ 的定义域是整个 $I$，而不只是子集。）${\mathcal{A}}$ 上潜在选择函数的集合 $P$ 可以按包含关系偏序化：我们约定，对潜在选择函数 $f, g \in P$，关系 $f \le g$ 成立，只要 $f$ 的定义域包含于 $g$ 的定义域，且 $f$ 在任一元素处的值与 $g$ 在该处的值相同。现在容易看出，$P$ 关于偏序 $\le$ 的极大元恰恰就是 ${\mathcal{A}}$ 上的选择函数。

**佐恩引理**是确保此类极大元存在的最著名原理。为陈述它，我们需要几个定义。给定偏序集 $(P, \le)$，$P$ 的子集 $X$ 的**上界**是元素 $a\in P$，使得对每个 $x\in X$ 都有 $x\le a$；于是 $P$ 的**极大元**可以定义为这样的元素 $a$：$\{a\}$ 的上界之集与 $\{a\}$ 重合，这实质上意味着 $P$ 中没有元素严格大于 $a$。$(P,\le)$ 中的**链**是 $P$ 的子集 $C$，使得对任意 $x$，$y\in P$，或者 $x\le y$，或者 $y\le x$。若 $P$ 中每条链都有上界，就说 $P$ 是**归纳的**。现在佐恩引理断言：

**佐恩引理**（**ZL**）：每个非空归纳偏序集都有极大元。

佐恩引理为何可信？这里有一个非正式的论证。给定非空归纳偏序集 $(P,\le)$，任取 $P$ 的一个元素 $p_{0}$。若 $p_{0}$ 极大，就停在那里。否则取元素 $p_{1} \gt p_{0}$；若 $p_{1}$ 极大，就停在那里。否则取元素 $p_{2} \gt p_{1}$，并重复此过程。若元素 $p_{0} \lt p_{1} \lt p_{2} \lt \ldots \lt p_{n} \lt \ldots$ 中没有极大的，则这些 $p_{i}$ 构成一条链；由于 $P$ 归纳，该链有上界 $q_{0}$。若 $q_{0}$ 极大，就停在那里。否则可以对 $q_{0} \lt q_{1}$，……重复程序，然后再迭代。这一过程必定最终终止，否则如此生成的各条链之并会构成真类，使 $P$ 本身成为真类，与假定矛盾。过程终止之处就给出 $P$ 的一个极大元。

这一论证经过适当精细化，就在策梅洛—弗兰克尔集合论中从 **AC1** 给出了 **ZL** 的证明[^note-9]：在该证明中，**AC1** 被用来“挑选”非正式论证中提到的元素。

佐恩引理的另一个版本可以用集合族来表述。给定集合族 ${\mathcal{H}}$，我们把 ${\mathcal{H}}$ 中的**巢**定义为 ${\mathcal{H}}$ 的子族 ${\mathcal{N}}$，使得对 ${\mathcal{N}}$ 的任意两个成员，一个包含于另一个。[^note-10]若 ${\mathcal{H}}$ 中任一巢之并都是 ${\mathcal{H}}$ 的成员，就称 ${\mathcal{H}}$ 是**强归纳的**。佐恩引理于是可以等价地重述为：任意非空强归纳集合族 ${\mathcal{H}}$ 都有极大成员，即不被 ${\mathcal{H}}$ 中任何成员真包含的成员。这又可以表述为一个对偶形式。若一个集合族对巢的交封闭，就称它是**强归约的**。那么任意非空强归约集合族都有**极小**元，即不真包含该族中任何成员的成员。

**AC2** 现在容易从这个替代形式的佐恩引理推出。因为索引集族 ${\mathcal{A}}$ 上潜在选择函数的集合 $P$ 显然非空，且容易证明是强归纳的；于是佐恩引理给出 ${\mathcal{A}}$ 上选择函数的存在性。

**CAC** 可以从 **ZL** 推出，其方式呼应上文勾勒的 **CAC** 的“组合”辩护。据此假定给出了互不相交的非空集合族 ${\mathcal{H}}$；称子集 $S \subseteq \bigcup {\mathcal{H}}$ 为 ${\mathcal{H}}$ 的**采样**，如果对任意 $X\in {\mathcal{H}}$，或者 $X \subseteq S$，或者 $S \cap X$ 非空且有限。极小采样恰恰就是 ${\mathcal{H}}$ 的横截；[^note-11]而采样之集 ${\mathcal{T}}$ 显然非空，因为它包含 $\bigcup {\mathcal{H}}$。因此，若能证明 ${\mathcal{T}}$ 是强归约的，[^note-12]佐恩引理就会给出 ${\mathcal{T}}$ 的极小元，从而是 ${\mathcal{H}}$ 的一个横截。${\mathcal{T}}$ 的强归约性可以这样看出：假定 $\{S_{i}: i\in I\}$ 是一个采样巢；令 $S = {\bigcap}_{i\in I} S_{i}$。我们需要证明 $S$ 本身是采样；为此令 $X \in {\mathcal{H}}$ 并假定 $\neg(X \subseteq S)$。那么存在 $i \in I$ 使 $\neg(X \subseteq S_{i})$；既然 $S_{i}$ 是采样，$S_{i}\cap X$ 有限且非空，比如说 $S_{i}\cap X = \{x_{1}, \ldots, x_{n}\}$。显然 $S\cap X$ 于是有限；为导出矛盾，假定 $S\cap X = \varnothing$。那么对每个 $k = 1,\ldots,n$，存在 $i_k \in I$ 使 $\neg(x_k \in S_{i_k})$。由此可知 $\neg(S_{i} \subseteq S_{i_k})$，对 $k = 1, \ldots, n$。所以，由于这些 $S_{i}$ 构成链，每个 $S_{i_k}$ 都是 $S_{i}$ 的子集。令 $S_{j}$ 为 $S_{i_1},\ldots, S_{i_k}$ 中最小的；那么 $S_{j}\subseteq S_{i}$。但既然对 $k = 1, \ldots, n$ 有 $\neg(x_{k} \in S_{j})$，现在可知 $S_{j} \cap X = \varnothing$，这与 $S_{j}$ 是采样的事实相矛盾。因此 $S \cap X\ne \varnothing$；如所断言，$S$ 是采样。

我们注意到，虽然佐恩引理与选择公理在集合论上等价，但从后者推出前者要比相反方向困难得多。

以下是极大原理的简要年表。

| 1909 | 豪斯多夫首次明确表述一个极大原理，并从 *AC* 推出它（Hausdorff 1909）[^hausdorff-1909] |
| --- | --- |
| 1914 | 豪斯多夫的《集合论基础》（最早的集合论与一般拓扑学著作之一）包含若干极大原理。 |
| 1922 | 库拉托夫斯基表述并使用若干极大原理，以避免使用超限序数（Kuratowski 1922）[^kuratowski-1922]。 |
| 1926–28 | 博赫纳等人独立引入极大原理（Bochner 1928, Moore 1932）[^bochner-1928][^moore-1932]。 |
| 1935 | 马克斯·佐恩显然不了解此前对极大原理的表述，发表（Zorn 1935）[^zorn-1935]其定本，后来以他的名字闻名（**ZL**）。**ZL** 最早于 1933 年在汉堡被表述，舍瓦莱与阿廷很快“采纳”了它。似乎正是阿廷最先认识到 **ZL** 会推出 *AC*，从而使两者（在集合论其余公理之上）等价。佐恩更多把他的原理视为**公理**而非定理——他希望它能取代代数中超限归纳与良序的繁琐应用，而诺特学派的代数学家已开始把这些应用视为“超验”手段。 |
| 1939–40 | 泰希米勒、布尔巴基与图基各自独立地用“有限特征的属性”重新表述 **ZL**（Bourbaki 1939, Teichmuller 1939, Tukey 1940）[^bourbaki-1939][^teichmuller-1939]。 |

## 4 选择公理的数学应用

选择公理在数学中有大量应用，其中若干已被证明与它形式等价[^note-13]。历史上最重要的应用是第一个，即：

**良序定理**（Zermelo 1904, 1908）[^zermelo-1904]：每个集合都可以良序化。

策梅洛发表其 1904 年从 *AC* 对良序定理的证明后，人们很快看出两者等价。

另一个早期的 *AC* 等价形式是

**乘法公理**（Russell 1906）[^russell-1906]：任意非零基数之集之积非零。

*AC* 的早期应用包括：

- 每个无限集都有可数子集。这一原理又弱于 *AC*，在集合论其余公理的语境中不用它无法证明。
- 每个无限基数都等于其平方。这在 Tarski 1924 中被证明等价于 *AC*。
- 每个向量空间都有基（由 Hamel 1905 开创）[^hamel-1905]。这在 Blass 1984 中被证明等价于 *AC*。
- 每个域都有代数闭包（Steinitz 1910）[^steinitz-1910]。这一断言弱于 *AC*，其实是（更弱的）一阶逻辑紧致性定理的推论（见下文）。
- 存在勒贝格不可测的实数集（Vitali 1905）[^vitali-1905]。很久以后才表明这是 **BPI**（见下文）的推论，因而弱于 *AC*。索洛维（1970）确立了它相对于集合论其余公理的独立性。

一个重要的“民间” *AC* 等价形式是

**集合论分配律**。对任意双重索引的集合族 $\{M_{i,j}: i \in I,j \in J\}$，且其中 $J^I$ 是定义域为 $I$、取值于 $J$ 的所有函数之集：

$$ \bigcap_{i\in I} \bigcup_{j\in J} M_{i,j} = \bigcup_{f\in J^I} \bigcap_{i\in I} M_{i,f(i)} $$

一个被大量研究的 *AC* 特例是

**依赖性选择原理**（Bernays 1942, Tarski 1948）[^bernays-1942][^tarski-1948]：对集合 $A$ 上任意非空关系 $R$，若 ${\mathrm{range}}(R) \subseteq {\mathrm{domain}}(R)$，则存在函数 $f: \omega \rightarrow A$，使得对所有 $n\in \omega, R(f(n),f(n+1))$。这一原理虽然（远）弱于 *AC*，但在集合论其余公理的语境中不用它无法证明。

*AC* 的数学等价形式包括：

- **吉洪诺夫定理**（1930）：紧拓扑空间之积是紧的。这在 Kelley 1950 中被证明等价于 *AC*。但对紧豪斯多夫空间，它等价于 **BPI**（见下文），因而弱于 *AC*。
- **勒文海姆—斯科伦—塔斯基定理**（Löwenheim 1915, Skolem 1920, Tarski and Vaught 1957）[^tarski-1957]：具有无限基数 $\kappa$ 的模型的一阶语句，也具有任意无限基数 $\mu$ 的模型，只要 $\mu \le \kappa$。塔斯基证明它等价于 *AC*。
- **克莱因—米尔曼定理**：实赋范线性空间的对偶空间中的单位球 $B$ 有端点，即不是 $B$ 中任何线段的内部点的点。这在 Bell and Fremlin 1972a 中被证明等价于 *AC*。该文表明：给定任意非空集的索引族 ${\mathcal{A}}$，${\mathcal{A}}$ 上的选择函数与由 ${\mathcal{A}}$ 构造的某个实赋范线性空间对偶单位球的端点之间存在自然双射。
- 每个分配格都有极大理想。这在 Klimovsky 1958 中被证明等价于 *AC*，对集合格则在 Bell and Fremlin 1972 中证明。
- 每个含单位元的交换环都有极大理想。这被 Hodges 1979 证明等价于 *AC*。

*AC* 还有许多已知弱于它[^note-14]的数学推论，特别是：

- **布尔素理想定理**（**BPI**）：每个布尔代数都有极大（或素）理想。这在 Halpern and Levy 1971 中被表明弱于 *AC*。
- **布尔代数的斯通表示定理**（Stone 1936）[^stone-1936]：每个布尔代数都同构于一个集合域。这等价于 **BPI**，因而弱于 *AC*。
- **一阶逻辑紧致性定理**（Gödel 1930, Malcev 1937 等）：若一阶语句集的每个有限子集都有模型，则该集合有模型。这在 Henkin 1954 中被表明等价于 **BPI**，因而弱于 *AC*。
- **一阶逻辑完全性定理**（Gödel 1930, Henkin 1954）：每个一致的一阶语句集都有模型。这在 1954 年被亨金表明等价于 **BPI**，因而弱于 *AC*。若以恰当方式指定模型的基数，该断言就变得等价于 *AC*。

最后，还有

- **布尔代数的西科尔斯基扩张定理**（Sikorski 1949）：每个完备布尔代数都是内射的，即对任意布尔代数 $A$ 与任意完备布尔代数 $B$，$A$ 的任一子代数到 $B$ 的任一同态都可以扩张到整个 $A$。

它是否等价于 *AC*，是该领域少数尚存的有趣未决问题之一；虽然它明显蕴含 **BPI**，但在 Bell 1983 中被证明独立于 **BPI**。

这些定理中有许多在 Bell and Machover（1977）中得到了讨论。

## 5 选择公理与逻辑

*AC* 与逻辑的最初联系，可以通过回到它用关系表述的形式 **AC3** 来引出，即：任意二元关系都包含一个具有相同定义域的函数。**AC** 的这一版本可以自然地在二阶语言 $L$ 中表达，该语言有个体变元 $x$、$y$、$z$、……与函数变元 $f$、$g$、$h$、……。在 $L$ 中，二元关系由含两个自由个体变元 $x$、$y$ 的公式 $\phi(x, y)$ 表示。断言 **AC3** 在 $L$ 中的对应物于是是

> **ACL**：$\forall x \exists y \phi(x, y) \rightarrow \exists f \forall x \phi(x, fx).$

这一语句模式就是 *AC* 的标准逻辑形式。

策梅洛对选择公理的最初表述 **AC1**，可以在 $L$ 的一个适当加强版本中表达为语句模式。据此我们现在假定 $L$ 还含有谓词变元 $X$、$Y$、$Z$、……与二阶函数变元 $F$、$G$、$H$、……。这里二阶函数变元 $F$ 可以应用于谓词变元 $X$，产生个体词项 $FX$。语句模式

> **AC1L**：$\forall X [\Phi(X) \rightarrow \exists x X(x)] \rightarrow \exists F \forall X[\Phi(X) \rightarrow X(FX)]$

就是 **AC1** 在这个加强的二阶语言中的直接对应物。用文字说，**AC1L** 断言：若每个具有某种属性 $\Phi$ 的谓词都有实例，则存在谓词上的函数 $F$，使得对任一满足 $\Phi$ 的谓词 $X$，$FX$ 是 $X$ 的一个实例。这里谓词扮演集合的角色。

到此为止，我们一直默认背景逻辑是通常的经典逻辑。但 **AC** 与逻辑联系的真深度，只有在把**直觉主义**或**构造性**逻辑引入图景时才显现出来。一个显著的事实是：仅假定直觉主义逻辑的框架加上某些温和的进一步预设，就可以表明选择公理蕴含经典逻辑的枢要规则——排中律，即对任意命题 $A$ 断言 $A \vee \neg A$。确切地说，在我们加强的语言 $L$ 中使用直觉主义逻辑的规则，我们将从 **AC1L** 连同下列附加原理推出[^note-15]排中律：

**谓词性概括**：$\exists X \forall x[X(x) \leftrightarrow \phi(x)]$，其中 $\phi$ 不含约束函数变元或谓词变元。

**函数的外延性**：$\forall X \forall Y \forall F[X \approx Y \rightarrow FX = FY]$，其中 $X \approx Y$ 是 $\forall x[X(x) \leftrightarrow Y(x)]$ 的缩写，即 $X$ 与 $Y$ *外延等价*。

**两个不同个体**：${\underline{0}} \ne {\underline{1}}$，其中 ${\underline{0}}$ 与 ${\underline{1}}$ 是个体常元。

现在令 $A$ 为给定命题。由谓词性概括，我们可以引入谓词常元 $U$、$V$ 以及断言

\begin{align} \tag{1} &\forall x[U(x) \leftrightarrow (A \vee x = 0)] \\ \notag &\forall x[V(x) \leftrightarrow (A \vee x = 1)] \end{align}

令 $\Phi(X)$ 为公式 $X \approx U \vee X \approx V$。那么显然我们可以断言 $\forall X[\Phi(X) \rightarrow \exists xX(x)]$，于是可以援引 **AC1L** 断言 $\exists F \forall X[\Phi(X) \rightarrow X(FX)]$。现在我们可以引入函数常元 $K$ 以及断言

$$ \tag{2} \forall X[\Phi(X) \rightarrow X(KX)]. $$

既然显然可以断言 $\Phi(U)$ 与 $\Phi(V)$，由 (2) 可知我们可以断言 $U(KU)$ 与 $V(KV)$，从而利用 (1) 也有

$$ [A \vee KU = 0] \wedge [A \vee KV = 1]. $$

利用分配律（它在直觉主义逻辑中成立），可知我们可以断言

$$ A \vee [KU = 0 \wedge KV = 1]. $$

由 $0 \ne 1$ 这一预设可知

$$ \tag{3} A \vee KU \ne KV $$

是可断言的。但由 (1) 可知我们可以断言 $A \rightarrow U ≈ V$，从而利用函数的外延性也有 $A \rightarrow KU = KV$。这给出 $KU \ne KV \rightarrow \neg A$ 的可断言性，再结合 (3) 就得出

$$ A \vee \neg A $$

的可断言性，即排中律。

选择公理蕴含排中律这一事实，初看似乎与另一事实相悖：前者常被视为构造性数学系统中的**有效**原理，而这些系统由直觉主义逻辑支配，例如比肖普的构造分析[^note-16]与马丁-洛夫构造类型论[^note-17]，其中排中律并未被肯定。用比肖普的话说，“选择函数在构造性数学中存在，因为选择**由存在本身的含义所蕴含**”。因此，例如 **ACL** 的前件 $\forall x \exists y \phi(x,y)$，在构造性解释下就**意味着**我们有一个程序，把它应用于每个 $x$ 就产生一个使 $\phi(x, y)$ 成立的 $y$。但这恰恰就是 **ACL** 的后件 $\exists f \forall x \phi(x,fx)$ 所表达的。

为化解这一困难，我们注意到，从 **ACL1** 推出排中律时，本质地使用了谓词性概括与函数的外延性原理[^note-18]。由此可知，在肯定 **AC**（但不肯定排中律）的构造性数学系统中，**或者谓词性概括原理，或者函数的外延性原理必定失效**。谓词性概括原理可以获得构造性辩护，函数的外延性原理却得不到这样的辩护。谓词上的函数是内涵地给出的，只满足相应的内涵性原理 $\forall X \forall Y \forall F[X = Y \rightarrow FX = FY]$。很容易使外延性原理失效，例如考虑谓词 $P$：**理性无羽两足动物**与 $Q$：**人**，以及谓词上的函数 $K$，它给每个谓词指派其描述中的词数。那么我们可以同意 $P \approx Q$，但 $KP = 3$ 而 $KQ = 2$。

在直觉主义集合论（即以直觉主义逻辑而非经典逻辑为基础的集合论——我们简记为 **IST**）与拓扑斯理论中，谓词性概括与函数的外延性原理（两者都经过适当解释）成立，因此其中 **AC** 蕴含排中律。[^note-19] ^{,} [^note-20]

从 *AC* 推出排中律，最早由迪亚科内斯库（1975）在范畴论背景中给出。他的证明使用了与上述证明实质上不同的想法；特别是，它没有使用外延性原理，而是使用了对象（或集合）对一个等价关系的商这一想法。在 **IST** 内表述迪亚科内斯库的论证是有启发性的。为此，我们把集合 $A$ 的子集 $U$ 称为**可分离的**，如果存在 $A$ 的子集 $V$，使得 $U \cap V = \varnothing$ 且 $U \cup V = A$。迪亚科内斯库的论证相当于从 **AC4**（见上文）推出如下断言：集合的每个子集都是可分离的；由此容易推出排中律。论证如下。

首先，给定 $U \subseteq A$，$U$（在 $A$ 中）的**指示函数**是满足

$$ U = \{ x \in A: g(x,0) = g(x,1) \} $$

的一个映射 $g: A \times 2 \rightarrow 2$。

于是容易证明：一个子集可分离，当且仅当它有指示函数。

现在我们证明：若 **AC4** 成立，则集合的任意子集都有指示函数，从而是可分离的。

对 $U \subseteq A$，令 $R$ 为 $A + A = A \times \{0\} \cup A \times \{1\}$ 上的二元关系，由下式给出

$$ R = \{ ((x,0),(x,0)) : x \in A \} \cup \{ ((x,1),(x,1)) : x \in A \} \cup \{ ((x,0),(x,1) : x \in A \} \cup \{ ((x,1),(x,0) \} : x \in A $$

可以验证 $R$ 是一个等价关系。用 $r$ 表示从 $A + A$ 到 $(A + A)$ 对 $R$ 的商[^note-21] $Q$ 的自然映射，它把 $A + A$ 的每个成员送到其 $R$-等价类。

现在应用 **AC4** 得到映射 $f: Q \rightarrow A + A$，满足对所有 $X \in Q$ 都有 $f(X) \in X$。于是容易证明：若用 $\pi_{1}$ 表示第一坐标投影，则

$$ \tag{*} \mbox{对于 } n=0,1 \mbox{ 且 } x \in A, \pi_1(f(r(x,n))) = x; $$

并且

$$ \tag{**} x \in U \leftrightarrow f(r(x,0)) = f(r(x,1)). $$

现在定义 $g: A \times 2 \rightarrow 2$ 为 $g = \pi_{2} \circ f \circ r$，其中 $\pi_2$ 是第二坐标投影。那么 $g$ 是 $U$ 的指示函数，如下列等价式所示：

\begin{align} x \in U &\leftrightarrow f(r(x,0))=f(r(x,1)) \ldots \mbox{by (**)} \\ &\leftrightarrow \pi_{1}(f(r(x,0))) = \pi_{1}(f(r(x,1))) \wedge \pi_{2}(f(r(x,0))) = \pi_{2}(f(r(x,1))) \\ &\leftrightarrow \pi_{2}(f(r(x,0))) = \pi_{2}(f(r(x,1))) \ldots \mbox{using (*)} \\ &\leftrightarrow g(x,0) = g(x,1). \end{align}

证明完毕。

可以表明（Bell 2006）[^bell-2006]，若干在直觉主义下无效的逻辑原理（包括排中律）各自都**等价**（在直觉主义集合论中）于选择公理的一个适当弱化版本。因此，这些逻辑原理可以被视为选择原理。

这里涉及的是以下逻辑原理：

| **SLEM** | $\alpha \vee \neg \alpha$（$\alpha$ 为任意语句） |
| --- | --- |
| **Lin** | $(\alpha \rightarrow \beta) \vee (\beta \rightarrow \alpha)$（$\alpha$、$\beta$ 为任意语句） |
| **Stone** | $\neg \alpha \vee \neg\neg \alpha$（$\alpha$ 为任意语句） |
| **Ex** | $\exists x[ \exists x \alpha(x) \rightarrow \alpha(x)]$（$\alpha(x)$ 为至多以 $x$ 为自由变元的任意公式） |
| **Un** | $\exists x[\alpha(x) \rightarrow \forall x\alpha(x)]$（$\alpha(x)$ 为至多以 $x$ 为自由变元的任意公式） |
| **Dis** | $\forall x[\alpha \vee \beta(x)] \rightarrow \alpha\vee\forall x\beta(x)$（$\alpha$ 为任意语句，$\beta(x)$ 为至多以 $x$ 为自由变元的任意公式） |

在直觉主义逻辑之上，**Lin**、**Stone** 与 **Ex** 是 **SLEM** 的推论；而 **Un** 蕴含 **Dis**。当然，这些模式全都从完整的排中律推出，即对任意公式成立的 **SLEM**。

以下用 0 表示空集，用 1 表示 $\{0\}$，用 2 表示 $\{0, 1\}$。

我们表述以下选择原理——这里 $X$ 是任意集合，${\mathrm{Fun}}(X)$ 是定义域为 $X$ 的函数之类，$\phi(x,y)$ 是集合论语言中至多以自由变元 $x$、$y$ 为自由变元的任意公式：

| **AC**$_X$ | $\forall x\in X\ \exists y \phi(x,y) \rightarrow \exists f \in {\mathrm{Fun}}(X)\ \forall x \in X\ \phi(x,fx)$ |
| --- | --- |
| **AC**$^*_X$ | ${\exists f \,{\in}\, {\mathrm{Fun}}(X)} [{\forall x\,{\in}\, X}\ \exists y \phi(x,y) \rightarrow {\forall x \,{\in}\, X}\ \phi(x,fx)]$ |
| **DAC**$_X$ | $\forall f \,{\in}\, Fun(X)\ {\exists x \,{\in}\, X}\ \phi(x,fx) \rightarrow {\exists x \,{\in}\, X}\ \forall y \phi(x,y)$ |
| **DAC**$^*_X$ | ${\exists f \,{\in}\, {\mathrm{Fun}}(X)}\ [{\exists x\,{\in}\, X}\ \phi(x,fx) \rightarrow {\exists x \,{\in}\, X}\ \forall y \phi(x,y)]$ |

其中前两个是 $X$ 上 *AC* 的形式；它们在经典语境中等价，但在 **IST** 中 **AC**$^*_X$ 蕴含 **AC**$_X$，反之不成立。原理 **DAC**$_X$ 与 **DAC**$^*_X$ 是 $X$ 上选择公理的**对偶**形式：在经典语境中它们都等价于 **AC**$_X$ 与 **AC**$^*_X$，但在直觉主义下 **DAC**$^*_X$ 蕴含 **DAC**$_X$，反之不成立。

我们还表述**弱外延选择原理**，其中 $\alpha(x)$ 与 $\beta(x)$ 是至多以变元 $x$ 为自由变元的任意公式：

**WESP**：${\exists x\,{\in}\, 2}\ \alpha(x) \wedge {\exists x \,{\in}\, 2}\ \beta(x) \rightarrow {\exists x \,{\in}\, 2}\ {\exists y \,{\in}\, 2}\ [\alpha(x) \wedge \beta(y) \wedge [{\forall x \,{\in}\, 2}\ [\alpha(x) \leftrightarrow \beta(x)] \rightarrow x = y]].$

这一原理是选择公理的直接推论，它断言：对 2 的成员任意两个已实例化的属性，可以按只依赖其外延的方式给这些属性指派实例。

上表列出的每个逻辑原理都（在 **IST** 中）等价于一个选择原理。事实上：

- **WESP** 与 **SLEM** 在 **IST** 上等价。
- **AC**$^*_1$ 与 **Ex** 在 **IST** 上等价。

此外，虽然 **DAC**$_1$ 容易看出在 **IST** 中可证，但我们有

- **DAC**$^*_1$ 与 **Un** 在 **IST** 上等价。

其次，虽然 **AC**$_2$ 在 **IST** 中容易证明，但与之相对，我们有

- **DAC**$_2$ 与 **Dis** 在 **IST** 上等价。
- 在 **IST** 上，**DAC**$^*_2$ 等价于 **Un**，因而也等价于 **DAC**$^*_1$。

为了给出等价于 **Lin** 与 **Stone** 的选择模式，我们引入

**ac**$^*_X$：${\exists f \,{\in}\, 2^X} [{\forall x\,{\in}\, X}\ {\exists y \,{\in}\, 2}\ \phi(x,y) \rightarrow {\exists x \,{\in}\, X}\ \phi(x,fx)]$

**wac**$^*_X$：${\exists f \,{\in}\, 2^X} [{\forall x \,{\in}\, X}\ {\exists y \,{\in}\, 2}\ \phi(x,y) \rightarrow {\forall x \,{\in}\, X}\ \phi(x,fx)]$，前提是 $\forall x[\phi(x,0) \rightarrow \neg\phi(x,1)]$ 在 **IST** 中可证

显然 **ac**$^*_X$ 等价于

${\exists f \,{\in}\, 2^X}[{\forall x \,{\in}\, X}[\phi(x,0) \vee \phi(x,1)] \rightarrow {\forall x \,{\in}\, X}\ \phi(x,fx)]$

**dac**$^*_X$ 类似。

于是，在 **IST** 上，**ac**$^*_1$ 与 **dac**$^*_1$ 分别等价于 **Lin** 与 **Stone**。

这些结果表明，当背景逻辑被假定为直觉主义逻辑时，选择原理与逻辑的相互作用有多么深。在假定排中律的经典环境中，这些联系被抹去了。

对选择公理与类型论主题感兴趣的读者，可以参阅以下补充文档：

> [选择公理与类型论](axiom-choice.choice-and-type-theory.md)

## 脚注

[^note-1]: 不过，策梅洛此时实际上并未给该原理一个明确名称。（他只在 1908 年这样做，那里他使用“选择公设”一词。我们注意到，策梅洛这里使用“积”一词，这正是若干数学家（尤其是罗素与拉姆齐）把该公理称为“乘法公理”的原因（见下文 §4）。

[^note-2]: 函数 $f$: $A \rightarrow B$ 是**满射**，如果对任意元素 $b \in B$ 都存在 $a \in A$ 使 $f(a) = b$。$f$ 的**右逆**是函数 $g: B \rightarrow A$，使得对任意 $x\in B$ 都有 $f(g(x) = x$。

[^note-3]: 策梅洛的表述字面上是：

> 一个集合 $S$，若能分解为若干互不相交的部分 $A$、$B$、$C$、……，每个部分至少含一个元素，则它至少有一个子集 $S_{1}$，就所考虑的每个部分 $A$、$B$、$C$、……而言，恰好含有一个元素。

[^note-4]: 这里的困难可以用罗素的一则轶事有趣地说明。一位百万富翁拥有无限多双鞋与无限多双袜子。一天，他突发奇想，召来男仆，要他从每双鞋中选出一只。男仆习惯于接受精确指示，便问如何执行选择；百万富翁建议从每双中选左脚那只。第二天，百万富翁又提议男仆从每双中选出一只**袜子**。当被问到**这一**操作如何进行时，百万富翁无言以对，因为与鞋不同，一双袜子中的两只没有内在方式可以区分。换言之，袜子的选择必须是真正任意的。

[^note-5]: 1923 年希尔伯特断言：

> 选择公理所依据的本质想法构成一条普遍逻辑原理，即便对数学推理的最初要素而言，它也是不可或缺的。

（转引自 Moore 1982 第 4.8 节。）[^moore-1982]

[^note-6]: 关于选择公理的详细历史，见 Moore 1982。

[^note-7]: 这里 $(x)_{x\in X}$ 表示 $X$ 的所有成员都被取作该结构的指定元素，即在相关一阶语言中由常元符号命名。

[^note-8]: 关于选择公理独立性证明的详细说明，见 Bell 2005 或 Jech 1973。

[^note-9]: 关于在 **ZF** 中从 *AC* 推出 *ZL* 的证明，见 Mendelson 1987（第 4 章第 5 节）。关于不使用序数、因而可在策梅洛集合论中表述的证明，见 Bourbaki 1950 或 Lawvere and Rosebrugh 2003（附录 B）。

[^note-10]: 因此 $S$ 中的巢就是 $S$ 中按集合包含偏序化的链。

[^note-11]: 极小采样是横截，这需要证明。假定 $S$ 是极小采样；那么给定 $X\in {\mathcal{I}}$，或者 (1) $S\cap X$ 有限非空，或者 (2) $X \subseteq S$。在情形 (1) 中，$S\cap X$ 不能含有两个不同元素，因为从 $S$ 中移除其中一个会得到一个比 $S$ 更小的采样，违反其极小性。所以在此情形中 $S\cap X$ 必须是单元集。在情形 (2) 中，$S$ 不能含有两个不同元素 $a$、$b$，因为若含有，则 $S' = [(S - X) \cup \{a\}]$ 会是一个比 $S$ 更小的采样（注意 $S' \cap X = \{a\}$，且 $S'$ 与 ${\mathcal{I}} - \{X\}$ 的成员的关系与 $S$ 相同），这再次违反 $S$ 的极小性。所以在此情形中 $X$，因而**更不必说** $S\cap X$，必须是单元集。

[^note-12]: 假如我们选择更贴近上文勾勒的 *AC* 的直观组合推导，使用选择子而非采样，就会遇到这样的障碍：与采样之集不同，选择子之集不一定是归约的。

[^note-13]: 关于选择公理的等价形式，见 Rubin and Rubin 1985；关于其推论，见 Howard and Rubin 1998。

[^note-14]: 这里的“更弱”意味着：在集合论公理（当然除去 *AC*）的语境中，所讨论的命题由 *AC* 蕴含，但反之不然。

[^note-15]: 该证明的想法可追溯到 Goodman and Myhill 1978，而后者本身建立在迪亚科内斯库 1975 年的一个结果之上。见下文。

[^note-16]: 见 Bishop and Bridges 1985。

[^note-17]: 见补充文档。关于构造类型论中各种 *AC* 版本的分析，见 Martin-Löf 2006。

[^note-18]: 当然，还用到了 $0 \ne 1$，但这一假定如此之弱，以至于它可以一致地加到几乎任何公理系统上。

[^note-19]: 但在缺少外延公理的弱集合论中，从 *AC* 推出排中律的推导不成立：需要假定某种形式的外延性，或者等价关系的商集的存在。见 Bell 2008。

[^note-20]: 佐恩引理的情况则不同。因为尽管它在经典集合论中与 *AC* 等价，在直觉主义集合论中佐恩引理**并不蕴含** **LEM**：事实上，它根本没有任何“非构造性”逻辑后果（Grayson 1975, Bell 1997）[^bell-1997][^grayson-1975]。因此，在直觉主义集合论中，佐恩引理远比 *AC* 弱。佐恩引理的直觉主义等价形式很少；Bell 2003 中表述了几个。

[^note-21]: 即 $A$ 的成员的所有 $R$-等价类之集。

## References（引用注释）

**以下文献从原文照录，不作翻译；中国文献条目（古今）一律译为中文。**

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

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

## 学术工具

* [如何引用本词条](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=axiom-choice)。
* [预览本词条的 PDF 版本](https://leibniz.stanford.edu/friends/preview/axiom-choice/)，见 [SEP 学会之友](https://leibniz.stanford.edu/friends/)。
* 在 [InPhO](https://www.inphoproject.org/entity?sep=axiom-choice&redirect=True) 查找与本词条相关的话题与思想家。
* 在 [PhilPapers](https://philpapers.org/sep/axiom-choice/) 查看本词条的增强文献目录及其数据库链接。

## 其他网络资源

- [选择公理主页](http://www.math.vanderbilt.edu/~schectex/ccc/choice.html)，由埃里克·谢克特（范德堡大学）维护。

## 相关词条

范畴论 | 库尔特·哥德尔 | 直觉主义逻辑的发展 | 直觉主义逻辑 | 构造数学 | 集合论：构造主义和直觉主义 | 策梅洛的公理化集合论 | 直觉主义类型论

**（译注：相关词条的中文站内链接将由管线在对应词条重译完成后统一挂接。）**

## 致谢

作者与编辑感谢杰西·阿拉马仔细阅读本文并提出许多有价值的改进建议。
