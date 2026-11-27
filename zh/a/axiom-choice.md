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
