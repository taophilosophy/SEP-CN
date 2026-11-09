# 混合逻辑 hybrid (Torben Braüner)

*首次发表于 2006 年 6 月 13 日；2021 年 12 月 22 日实质修订。*

混合逻辑是在普通模态逻辑之上增添表达力而形成的逻辑。最基础的混合逻辑引入所谓“名项”：这是一种新的命题符号，每个名项恰在一个可能世界上为真。其历史可上溯至 Arthur N. Prior 于 20 世纪 60 年代的工作。

## 1 混合逻辑的动机

在标准 Kripke 语义中，模态逻辑的真相对于某个点集里的点而定。同一命题符号相对于不同点，真值可能不同。这些点通常用以表示可能世界、时间、认知状态、计算机状态等。借此，我们可以形式化真值相对于时间等要素的自然语言语句，例如：

> 正在下雨。

这句话在不同时间显然有不同真值。另有一些自然语言语句，则恰在一个时间、可能世界或其他对象上为真。例如：

> 现在是 2021 年 11 月 15 日五点整。

该语句在 2021 年 11 月 15 日五点整为真，在其余一切时间上则假。第一类语句可在普通模态逻辑中形式化，第二类则不能。

混合逻辑的一大动机，是增强普通模态逻辑的表达力，以形式化上述第二类语句。其做法是引入第二类命题符号——**名项**，并规定在 Kripke 语义中每个名项恰相对于一个点为真。于是，第二类自然语言语句（如以 2021 年 11 月 15 日五点整为时间的那句）便以名项而非普通命题符号来形式化；普通命题符号则用于“正在下雨”一类例句。名项恰相对于一个点为真，这意味着名项可以看作指称某一点的词项：设 $\mathtt{a}$ 为代表“现在是 2021 年 11 月 15 日五点整”的名项，则它可视为指称该时刻的词项。由此可见，混合逻辑中的词项是一类特殊的命题符号，而在一阶逻辑中词项是谓词的论元。

多数混合逻辑还设有名项之外的其他机制，可供选择者不止一种；这里只考察所谓 **满足算子**。引入满足算子，是为了能形式化“某陈述在特定时间、可能世界或其他对象上为真”。例如，我们希望形式化“正在下雨”在 2021 年 11 月 15 日五点整为真，亦即：

> 在 2021 年 11 月 15 日五点整，正在下雨。

这由公式 $\mathtt{@_a p}$ 形式化：其中名项 $\mathtt{a}$ 如上代表“现在是 2021 年 11 月 15 日五点整”，$\mathtt{p}$ 则是代表“正在下雨”的普通命题符号。公式 $\mathtt{@_a p}$ 中的 $\mathtt{@_a}$ 部分即所谓满足算子。一般地，给定名项 $\mathtt{a}$ 与任意公式 $\mathtt{\phi}$，即可构造新公式 $\mathtt{@_a\phi}$，称为 **满足陈述**。满足陈述 $\mathtt{@_a\phi}$ 表达：公式 $\mathtt{\phi}$ 相对于某一特定点——即名项 $\mathtt{a}$ 所指称之点——为真。

综上，我们借助名项与满足算子为普通模态逻辑增添了表达力。非正式地说，名项 $\mathtt{a}$ 的真值条件为：

> $\mathtt{a}$ 相对于点 $w$ 为真，当且仅当 $\mathtt{a}$ 的指称就是 $w$。

满足陈述 $\mathtt{@_a\phi}$ 的真值条件则为：

> $\mathtt{@_a\phi}$ 相对于点 $w$ 为真，当且仅当 $\mathtt{\phi}$ 相对于 $\mathtt{a}$ 的指称为真。

须注意，$\mathtt{@_a\phi}$ 的真值条件其实与点 $w$ 无关：无论 $w$ 为何，满足算子 $\mathtt{@_a}$ 都会把求值点移至 $\mathtt{a}$ 的指称。

值得注意的是，名项与满足算子合用，竟可表达两点相同：若名项 $\mathtt{a}$、$\mathtt{b}$ 分别指称点 $w$、$v$，则公式 $\mathtt{@_a b}$ 即表达 $w$ 与 $v$ 相同。理由见下：

> $\mathtt{@_a b}$ 相对于点 $w$ 为真，当且仅当 $\mathtt{b}$ 相对于 $\mathtt{a}$ 的指称为真，当且仅当 $\mathtt{b}$ 相对于 $w$ 为真，当且仅当 $\mathtt{b}$ 的指称为 $w$，当且仅当 $v$ 就是 $w$。

集合上的同一关系素以自反、对称、传递著称，这正体现在下列公式均为混合逻辑的有效公式：

$$\begin{align*} & \mathtt{@_a a} \\ & \mathtt{@_a b \rightarrow @_b a} \\ &(\mathtt{@_a b \amp @_b c) \rightarrow @_a c} \end{align*}$$

此外，公式

$$ (\mathtt{@_ab \amp @_a\phi) \rightarrow @_b\phi} $$

同样有效。

此即替换规则。它与带等词一阶逻辑中的公式 $\mathtt{(a=b \amp \phi(a)) \rightarrow \phi(b)}$ 颇为相似（该式通常称为莱布尼茨律）。

除名项与满足算子，下文还考察所谓 **约束子** $\mathtt{\forall}$、$\mathtt{\downarrow}$，用以构造公式 $\mathtt{\forall a \phi}$ 与 $\mathtt{{\downarrow} a \phi}$。二者约束名项的方式不同：$\mathtt{\forall}$ 约束子仿照标准一阶全称量词对点作量化，即 $\mathtt{\forall a \phi}$ 相对于 $w$ 为真，当且仅当无论名项 $\mathtt{a}$ 指称何点，$\mathtt{\phi}$ 都相对于 $w$ 为真；$\mathtt{\downarrow}$ 约束子则把名项约束到求值点，即 $\mathtt{{\downarrow} a \phi}$ 相对于 $w$ 为真，当且仅当令 $\mathtt{a}$ 指称 $w$ 时，$\mathtt{\phi}$ 相对于 $w$ 为真。结果表明，$\mathtt{\downarrow}$ 约束子可用 $\mathtt{\forall}$ 定义（见下文）。

## 2 形式语义

本词条考察的语言，是在普通命题符号 $\mathtt{p}, \mathtt{q}, \mathtt{r}, …$ 与名项 $\mathtt{a}, \mathtt{b}, \mathtt{c}, …$ 之上建立的普通模态逻辑语言，再加入满足算子与约束子。命题联结词以 $\mathtt{\wedge}$、$\mathtt{\neg}$ 为初始符号，其余按通常方式定义；模态算子以 $\mathtt{\Box}$ 为初始符号，$\mathtt{\Diamond}$ 则定义为 $\mathtt{\neg \Box \neg}$。约束子约束名项；名项何谓自由出现、何谓约束出现，仿照一阶逻辑界定。满足算子不约束名项：$\mathtt{@_a \phi}$ 中自由出现的名项，等于 $\mathtt{\phi}$ 中自由出现的名项再加上 $\mathtt{a}$。记 $\mathtt{\phi[c/a]}$ 为如下结果：把名项 $\mathtt{c}$ 代入 $\mathtt{\phi}$，替换 $\mathtt{a}$ 的全部自由出现。若 $\mathtt{a}$ 在 $\mathtt{\phi}$ 中于 $\mathtt{\forall c}$ 或 $\mathtt{{\downarrow} c}$ 辖域内自由出现，则相应改名 $\mathtt{\phi}$ 里的约束名项 $\mathtt{c}$。

现在定义模型与框架。混合逻辑的 **模型** 为三元组 $(W, R, V)$：$W$ 是非空集，$R$ 是 $W$ 上的二元关系，$V$ 是函数：给每一对“$W$ 中元素与普通命题符号”指派 $\{0,1\}$ 中一个元素。对 $(W, R)$ 称为 **框架**。可见模型、框架与普通模态逻辑无异。$W$ 的元素称 **世界**，$R$ 称 **可及关系**；模型 $(W, R, V)$ 称 **基于** 框架 $(W, R)$。

模型 $M = (W, R, V)$ 的 **指派** 是给每个名项指派 $W$ 中元素的函数 $g$。若 $g'$ 与 $g$ 在除 $\mathtt{a}$ 外的所有名项上一致，则称 $g'$ 为 $g$ 的 $\mathtt{a}$ **变体**。关系 $M, g, w \vDash \phi$ 按归纳定义，其中 $g$ 为指派、$w$ 为 $W$ 的元素、$\mathtt{\phi}$ 为公式。

> $M, g, w \vDash \mathtt{p}$ 当且仅当 $V(w, \mathtt{p})=1$；$M, g, w \vDash \mathtt{a}$ 当且仅当 $w = g(\mathtt{a})$；$M, g, w \vDash \mathtt{\phi \wedge \psi}$ 当且仅当 $M, g, w \vDash \mathtt{\phi}$ 且 $M, g, w \vDash \mathtt{\psi}$；$M, g, w \vDash \mathtt{\neg \phi}$ 当且仅当并非 $M, g, w \vDash \mathtt{\phi}$；$M, g, w \vDash \mathtt{\Box} \phi$ 当且仅当对 $W$ 中一切满足 $wRv$ 的 $v$，均有 $M, g, v \vDash \mathtt{\phi}$；$M, g, w \vDash \mathtt{@_a \phi}$ 当且仅当 $M, g, g(\mathtt{a}) \vDash \mathtt{\phi}$；$M, g, w \vDash \mathtt{\forall a\phi}$ 当且仅当对 $g$ 的任一 $\mathtt{a}$-变体 $g'$，均有 $M, g', w \vDash \mathtt{\phi}$；$M, g, w \vDash \mathtt{{\downarrow} a\phi}$ 当且仅当 $M, g', w \vDash \mathtt{\phi}$，其中 $g'$ 是 $g$ 的满足 $g'(\mathtt{a}) = w$ 的 $\mathtt{a}$-变体。

若 $M, g, w \vDash \mathtt{\phi}$，称 $\mathtt{\phi}$ 在 $w$ 处 **真**，否则称在 $w$ 处 **假**。约定 $M, g \vDash \mathtt{\phi}$ 指对 $W$ 中一切 $w$ 均有 $M, g, w \vDash \mathtt{\phi}$；$M \vDash \mathtt{\phi}$ 指对一切指派 $g$ 均有 $M, g \vDash \mathtt{\phi}$。$\mathtt{\phi}$ 在某框架中 **有效**，当且仅当一切基于该框架的模型 $M$ 都满足 $M \vDash \mathtt{\phi}$；$\mathtt{\phi}$ 在框架类 $F$ 中 **有效**，当且仅当 $\mathtt{\phi}$ 在 $F$ 的每个框架中都有效；$\mathtt{\phi}$ **有效**，当且仅当 $\mathtt{\phi}$ 在一切框架的类中有效。可满足性的定义从略。

须注意，$\mathtt{\downarrow}$ 约束子可用 $\mathtt{\forall}$ 定义：公式 $\mathtt{{\downarrow} a\phi \leftrightarrow \forall a(a \rightarrow \phi)}$ 在任何框架中皆有效。

混合化普通模态逻辑确能增强表达力，公式 $\mathtt{{\downarrow} c\Box \neg c}$ 即为一例：不难验证，它在某框架中有效，当且仅当该框架非自反。可见非自反性可由混合逻辑公式表达；而众所周知，普通模态逻辑的任何公式都无从表达它。其实只消给普通模态逻辑加入名项，便可用 $\mathtt{c\rightarrow \Box \neg c}$ 表达非自反性。其他可为混合逻辑表达、却不能为普通模态逻辑表达的性质还有：不对称性（$\mathtt{c \rightarrow \Box \neg \Diamond c }$）、反对称性（$\mathtt{c\rightarrow \Box(\Diamond c \rightarrow c)}$）与普遍性（$\mathtt{\Diamond c}$）。

混合逻辑的语法、语义及许多基本定义，详见手册章节 Areces and ten Cate (2006)。上述语法与语义可有多种扩展，尤其可加入一阶量化；当然，给一阶模态逻辑加入混合逻辑机制，亦可得等价的一阶混合逻辑。一阶混合逻辑的概览见 Braüner (2014)，详论见 Braüner (2011a) 第 6 章，内涵一阶混合逻辑则见同书第 7 章。

## 3 翻译

混合逻辑可译为带等词的一阶逻辑，而带等词一阶逻辑的（一部分）亦可回译为混合逻辑的（一部分）。所论一阶语言对模态逻辑的每个普通命题符号 $\mathtt{p}$ 设一个 1 元谓词符号 $\mathtt{p^*}$，另设 2 元谓词符号 $\mathtt{R}$ 与 2 元谓词符号 $\mathtt{=}$。谓词符号 $\mathtt{p^*}$ 的解释，使相应模态命题符号 $\mathtt{p}$ 的解释相对于世界而定；$\mathtt{R}$ 以可及关系解释；$\mathtt{=}$ 以世界间的同一关系解释。以 $\mathtt{a}, \mathtt{b}, \mathtt{c},\ldots$ 取遍一阶变元。该语言不含常元与函数符号。一阶变元与混合逻辑的名项视为同一。

先译混合逻辑为带等词的一阶逻辑。给定两个新一阶变元 $\mathtt{a}$、$\mathtt{b}$，翻译 $\mathrm{ST}_\mathtt{a}$ 与 $\mathrm{ST}_\mathtt{b}$ 相互递归定义；此处仅列 $\mathrm{ST}_\mathtt{a}$。

$$\begin{align*} \mathrm{ST}_\mathtt{a} (\mathtt{p}) &= \mathtt{p^*(a)} \\ \mathrm{ST}_\mathtt{a} (\mathtt{c}) &= \mathtt{a=c} \\ \mathrm{ST}_\mathtt{a} (\mathtt{\phi \wedge \psi}) &= \mathrm{ST}_\mathtt{a} (\mathtt{\phi}) \mathtt{\wedge} \mathrm{ST}_\mathtt{a} (\mathtt{\psi}) \\ \mathrm{ST}_\mathtt{a} (\mathtt{\neg \phi}) &= \mathtt{\neg} \mathrm{ST}_\mathtt{a}(\phi) \\ \mathrm{ST}_\mathtt{a} (\mathtt{\Box \phi}) &= \mathtt{\forall b(R(a, b) \rightarrow} \mathrm{ST}_\mathtt{b} (\mathtt{\phi})\mathtt{)} \\ \mathrm{ST}_\mathtt{a} (\mathtt{@_c \phi}) &= \mathrm{ST}_\mathtt{a} (\mathtt{\phi})[\mathtt{c}/\mathtt{a}] \\ \mathrm{ST}_\mathtt{a} (\mathtt{{\downarrow} c\phi}) &= \mathrm{ST}_\mathtt{a} (\mathtt{\phi})[\mathtt{a}/\mathtt{c}] \\ \mathrm{ST}_\mathtt{a} (\mathtt{\forall c\phi}) &= \mathtt{\forall c }\mathrm{ST}_\mathtt{a} (\mathtt{\phi}) \end{align*}$$

$\mathrm{ST}_\mathtt{b}$ 的定义只需互换 $\mathtt{a}$、$\mathtt{b}$。此翻译是模态逻辑到一阶逻辑的著名 **标准翻译** 之扩展。下面逐步演示混合逻辑公式 $\mathtt{{\downarrow} c\Box \neg c}$ 如何译成一阶公式：

$$\begin{align*} \mathrm{ST}_\mathtt{a} (\mathtt{{\downarrow} c\Box \neg c}) &= \mathrm{ST}_\mathtt{a} (\mathtt{\Box \neg c})[\mathtt{a}/\mathtt{c}] \\ &= \mathtt{\forall b(R(a, b) \rightarrow } \mathrm{ST}_\mathtt{b} (\mathtt{\neg c})\mathtt{)}[\mathtt{a}/\mathtt{c}] \\ &= \mathtt{\forall b(R(a, b) \rightarrow \neg } \mathrm{ST}_\mathtt{b} (\mathtt{c})\mathtt{)}[\mathtt{a}/\mathtt{c}] \\ &= \mathtt{\forall b(R(a, b) \rightarrow \neg b=c)}[\mathtt{a}/\mathtt{c}] \\ &= \mathtt{\forall b(R(a, b) \rightarrow \neg b=a)}. \end{align*}$$

所得一阶公式等价于 $\mathtt{\neg R(a, a)}$，可见 $\mathtt{{\downarrow} c\Box \neg c}$ 确实对应可及关系的非自反性（参上文）。

带等词的一阶逻辑可经下述翻译 HT 回译入混合逻辑。

$$\begin{align*} \mathrm{HT}(\mathtt{p^*(a)}) &= \mathtt{@_a p} \\ \mathrm{HT}(\mathtt{R(a, c)}) &= \mathtt{@_a \Diamond c} \\ \mathrm{HT}(\mathtt{a=c}) &= \mathtt{@_a c} \\ \mathrm{HT}(\mathtt{\phi \wedge \psi}) &= \mathrm{HT}(\mathtt{\phi}) \mathtt{\wedge} \mathrm{HT}(\mathtt{\psi}) \\ \mathrm{HT}(\mathtt{\neg \phi}) &= \mathtt{\neg} \mathrm{HT}(\mathtt{\phi}) \\ \mathrm{HT}(\mathtt{\forall a\phi}) &= \mathtt{\forall a} \mathrm{HT}(\mathtt{\phi}) \end{align*}$$

请注意，此处须借助混合逻辑的 $\mathtt{\forall}$ 约束子。上述观察的历史可上溯至 Arthur N. Prior 的工作，后文将再作讨论。

同理，一阶逻辑的所谓 **有界片段** 亦可译入混合逻辑，但此时仅需 $\mathtt{\downarrow}$ 约束子——Areces, Blackburn, and Marx (2001) 已指出此点。有界片段是一阶逻辑的一个片段，其中量词只以 $\mathtt{\forall c(R(a, c) \rightarrow \phi)}$ 的形式出现，且要求变元 $\mathtt{a}$ 与 $\mathtt{c}$ 相异。将有界片段译入不含 $\mathtt{\forall}$ 约束子的混合逻辑，只须把翻译 HT 的最后一款改为

$$ \mathrm{HT}(\mathtt{\forall c(R(a, c) \rightarrow \phi)}) = \mathtt{@_a \Box {\downarrow} c}\mathrm{HT}(\mathtt{\phi}). $$

Areces, Blackburn, and Marx (2001) 给出了有界片段的多种独立语义刻画。

上述翻译保持真值。为形式陈述此点，可用一个公认观察：混合逻辑模型与指派，可视为一阶逻辑模型与指派，反之亦然。真值保持结果，表述颇为直接，细节从略。由此，凡含 $\mathtt{\forall}$ 约束子之混合逻辑，与带等词一阶逻辑表达力相当；不含 $\mathtt{\forall}$ 约束子而含 $\mathtt{\downarrow}$ 约束子之混合逻辑，则与一阶逻辑有界片段相当。（注意：凡不含 $\mathtt{\forall}$ 约束子之公式 $\mathtt{\phi}$，其翻译 $\mathrm{ST}_\mathtt{a} (\mathtt{\phi})$ 均属有界片段。）

上述翻译可推广到一阶混合逻辑，此时目标逻辑为带等词的二类一阶逻辑：一类是世界，一类是个体（见 Braüner (2011a) 第 6 章）。若是内涵一阶混合逻辑，则用三类，第三类为内涵（见同书第 7 章）。

## 4 Arthur N. Prior 与混合逻辑

混合逻辑的历史可上溯至 Arthur N. Prior 的混合时态逻辑，即普通时态逻辑的混合化版本。为深入考察，先给出混合时态逻辑的形式定义。其语言同上述混合逻辑，只是以两个模态算子 $\mathtt{G}$、$\mathtt{H}$ 取代单一模态算子 $\mathtt{\Box}$；这两个新算子称 **时态算子**。语义沿用混合逻辑（见前），只将 $\mathtt{\Box}$ 的条款换成 $\mathtt{G}$、$\mathtt{H}$ 的条款。

> $M, g, w \vDash \mathtt{G \phi}$ 当且仅当对 $W$ 中一切满足 $wRv$ 的 $v$，均有 $M, g, v \vDash \mathtt{\phi}$；$M, g, w \vDash \mathtt{H \phi}$ 当且仅当对 $W$ 中一切满足 $vRw$ 的 $v$，均有 $M, g, v \vDash \mathtt{\phi}$

于是有了两个模态算子：一沿可及关系“向前看”，一“向后看”。在时态逻辑中，$W$ 的元素称 **时刻** 或 **瞬间**，关系 $R$ 称 **先后关系**。

当然，只需稍改上述 $\mathrm{ST}_a$ 与 $\mathrm{HT}$，便可得混合时态逻辑（含 $\mathtt{\forall}$ 约束子）与带等词一阶逻辑间的翻译。所论一阶逻辑，即 Prior 所称 **一阶先后逻辑**。据这些翻译，Prior 的一阶先后逻辑与混合时态逻辑表达力相当。

Prior 引入混合时态逻辑，是与他所谓时态逻辑卷入的四个等级相联系的；四等级的动机是哲学性的。四等级见 Prior (1968) 第十一章（新版 Prior (2003) 亦为第十一章），另见 Prior (1967) 第五章第 6 节与附录 B.3-4；更一般的讨论见遗著 Prior and Fine (1977)。诸阶段由可视为纯粹一阶先后逻辑者，推进到可视为纯粹时态逻辑者，目标在于使第四阶段的时态逻辑涵盖第一阶段的先后逻辑。换言之，目标是把先后关系的一阶逻辑译为时态逻辑。正为此，Prior 引入所谓瞬间命题：

> 我所谓的时态逻辑卷入第三等级，在于把瞬间变元 $a, b, c$ 等也视为代表命题。（Prior 2003, p. 124）[^prior-2003]

在模态逻辑语境中，Prior 称这类命题为可能世界命题——这正是我们所说的名项。Prior 还引入 $\mathtt{\forall}$ 约束子及我们所说的满足算子（满足算子他记作 $\mathtt{T(a, \phi)}$，而非 $\mathtt{@_a \phi}$）。其实，Prior 的第三等级时态逻辑与上述混合时态逻辑并无二致；$\mathtt{\downarrow}$ 约束子则是很久以后才出现的。可见 Prior 通过给普通时态逻辑添入名项、满足算子与 $\mathtt{\forall}$ 约束子，取得了他的一阶先后逻辑的表达力；从技术上说，他显然已达标。

然而从哲学上看，第三等级时态逻辑的本体论意涵是否同于一阶先后逻辑的本体论意涵，历来有争议。例如，有些作者视 $\mathtt{\forall}$ 约束子为直接类比一阶 $\mathtt{\forall}$ 量词，因而心存疑虑；参见 Copeland (1996) 文集中 Sylvan (1996)。Prior 第四等级时态逻辑的讨论见 Braüner (2002)；另见 Øhrstrøm and Hasle (1993)、Øhrstrøm and Hasle (2006)、Müller (2007)、Blackburn (2006)。四等级的讨论则见 Braüner (2011a) 第 1 章。

Hasle (2020) 指出，在 Prior (1967)、Prior (1968)（新版 Prior (2003)）问世之前，Prior 著作中已见混合逻辑观念的痕迹。前述 Øhrstrøm and Hasle (2006) 详述 Prior 的逻辑工作；其生平与著述的全面论述见 Øhrstrøm and Hasle (1995)。Hasle and Øhrstrøm (2016) 则描述 Prior 的方法论进路，尤其是他对形式化及符号逻辑在概念研究中作用的看法。

## 5 Prior 以来混合逻辑的发展

混合逻辑的第一个完全严格定义出自 Bull (1970)，刊于纪念 Prior 的《Theoria》专号。Bull 引入第三类命题符号：它被假定恰在分支时间模型的某一分支（“事件进程”）上为真。这种依解释限制为命题符号分类的想法，后经多位作者发展，见 Blackburn and Tzakova (1999) 第 5 节及 Blackburn and Goranko (2001)。

Prior 于 20 世纪 60 年代末首创的混合逻辑进路，80 年代由保加利亚的 Solomon Passy 与 Tinko Tinchev 重新发明，见 Passy and Tinchev (1985)、(1991)。这项工作并非依托普通模态逻辑，而是依托表达力强得多的命题动态逻辑。

90 年代的一大贡献，是 $\mathtt{\downarrow}$ 约束子的引入。下箭头约束子的早期版本见于 Valentin Goranko 的 Goranko (1994)、(1996)；本文所用版本则由 Blackburn and Seligman (1995) 引入。此后，带 $\mathtt{\downarrow}$ 约束子的混合逻辑研究蔚然成风，例如 Areces, Blackburn, and Marx (2001) 论其模型论。混合逻辑模型论的全面研究，见 ten Cate (2004) 的博士论文。Areces, Fervari, Hoffmann, and Martel (2018) 则考察带 $\mathtt{\downarrow}$ 约束子的强混合逻辑与所谓变关系模态逻辑的关系。

同时省去 $\mathtt{\downarrow}$、$\mathtt{\forall}$ 两个约束子所得的较弱混合逻辑，也得到广泛探究。结果表明，此无约束子逻辑及其若干变体皆可判定。Areces, Blackburn, and Marx (1999) 就混合模态逻辑与时态逻辑在各种框架类（任意、传递、线性、分支等）上给出若干复杂性结果。值得注意的是，无约束子混合逻辑在任意框架上的可满足性问题可在 PSPACE 内判定，与普通模态逻辑可满足性判定的复杂性相同。可见混合化虽增强了表达力，复杂性却不变。在模态逻辑内部模拟名项的工作，可见 Kracht and Wolter (1997)。

任何普通模态公式都在框架上表达一个一元二阶性质；众所周知，对某些模态公式（含所谓 Sahlqvist 公式），该二阶性质等价于某个一阶性质。Goranko and Vakarelov (2006) 表明，这对包括名项在内的一类混合逻辑公式同样成立。计算普通模态公式一阶等价式的算法已有数种，其一为 SQEMA，Conradie, Goranko, and Vakarelov (2006) 将其扩展至 Goranko and Vakarelov (2006) 所论混合逻辑公式。

如上一节所述，Prior 引入混合时态逻辑，本为处理时间哲学中的一个特定问题；但 Prior (1968) 第十四章（新版 Prior (2003) 亦为第十四章）又表明，混合时态逻辑可取代 Hans Kamp 于 1967 年未刊稿中提出、后收入 Kamp (1971) 的二维时态逻辑。所谓维度，即公式求值所相对的时刻数目；加入混合逻辑机制，便可使二维化为一维。此线工作近由 Blackburn 与 Jørgensen 在一系列论文中推进，概述见 Blackburn and Jørgensen (2016a)。今按本词条术语略述其要。所论混合逻辑版本设一个指派名项 $\mathtt{now}$，每个模型各带一指派时间 $ t_0 $，使得 i) 任何独立公式皆相对于 $ t_0 $ 求值，ii) 名项 $\mathtt{now}$ 指称 $ t_0 $。更形式地说，约定 $(M,t_0), g \vDash \mathtt{\phi}$ 意即 $M, g, t_0 \vDash \mathtt{\phi}$，且只考虑 $g(\mathtt{now})=t_0$ 的指派 $g$。注意，名项 $\mathtt{now}$ 作为独立公式在此语义中有效，其他名项则不然。Blackburn 与 Jørgensen 称此新的有效性概念为 **语境有效性**；Blackburn and Jørgensen (2013) 给出关于该概念完全的公理系统，Blackburn and Jørgensen (2012) 则给出完全的表列系统，唯其语义与 Kamp 原初二维语义一致。两文还论及 $\mathtt{yesterday}$、$\mathtt{today}$、$\mathtt{tomorrow}$ 等索引词。

Blackburn and Jørgensen (2016b) 以混合时态逻辑糅合 Prior 与 Hans Reichenbach 关于自然语言时态表示的想法。Prior 偏爱上述时态算子，Reichenbach 则偏爱时间指称，即对特定时间的指称（Reichenbach 1947）。两种进路原来可以结合，唯 Prior 本人未取此途——详见 Blackburn and Jørgensen (2016b) 的论述，

混合逻辑概念应用甚广。例如，Areces and Fervari (2021) 把混合算子加入 XPath——这是广泛用于 XML 的查询语言，而 XML 是描述数字文本的标记语言。混合逻辑也被用来增强规约逻辑的表达力，以刻画计算系统的某些性质，见 Neves, Madeira, Martins, Barbosa (2016)。此外，类似混合逻辑的逻辑在描述逻辑中居核心地位；描述逻辑是人工智能中用于知识表示的一族逻辑，见 Blackburn and Tzakova (1998) 及 Carlos Areces 的博士论文 (2000)。

## 6 混合逻辑的公理

混合逻辑的公理系统，已有不少论文讨论，如 Gargov and Goranko (1993)、Blackburn (1993)、Blackburn and Tzakova (1999)。Gargov and Goranko (1993) 给出一个混合逻辑公理系统，并证明：若增补一组 **纯** 公式（即所有命题符号均为名项的公式）作为附加公理，则扩展后的系统相对于使这些公理有效的框架类完全。纯公式对应可及关系上的一阶条件（参前述翻译 $\mathrm{ST}_\mathtt{a}$），故凡以可及关系一阶条件刻画的新混合逻辑，其公理系统皆可按需增补公理而统一获得。例如加入公理 $\mathtt{c\rightarrow \Box \neg c}$，所得系统即相对于非自反框架完全（如前所述）。此类规则的讨论见 Blackburn (2000) 第 4 节。

Gargov and Goranko (1993) 的证明系统用一条复杂规则（COV），其含活动部分的公式模式可任意大——活动部分实嵌套于任意深度的模态算子之下。Blackburn and Tzakova (1999) 表明，借满足算子可以更标准的格式表述公理系统，只需一条更简单的规则 PASTE；系统增补纯公理后仍完全。

Blackburn and ten Cate (2006) 考察 **正统** 证明规则（即无附条件的规则），并表明：若欲借纯公式获得扩展完全性，则无约束子混合逻辑的公理系统离不开非正统规则。但在含 $\mathtt{\downarrow}$ 约束子的更强混合逻辑中，可以给出仅用正统规则的公理系统。另见 Braüner (2011a)：其中既有混合逻辑的另一公理系统，也有直觉主义混合逻辑及纳尔逊悖论逻辑 N4 之混合化的公理系统（比较 Costa and Martins (2017) 所论另一悖论混合逻辑）。直觉主义混合逻辑的综述见 Braüner (2011b)。

## 7 混合逻辑的分析性证明方法

较之普通模态逻辑，混合逻辑的表列、Gentzen 与自然演绎证明论运作得颇为顺畅。通常，模态表列、Gentzen 或自然演绎系统皆针对某一特定模态逻辑；事实证明，若不引入元语言机制，便很难统一地为模态逻辑表述此类系统。混合化恰可补救：模态逻辑一经混合化，便能为广泛的逻辑类统一表述表列、Gentzen 与自然演绎系统。Blackburn (2000) 给出的混合逻辑表列系统即具此优点：与 Blackburn and Tzakova (1999) 的公理系统相仿，给表列系统增补一组纯公理（即允许在表列构造中添入表列的纯公式），完全性仍得保持。该表列系统是 Bolander and Braüner (2006) 无约束子混合逻辑判定程序的基础；此线研究由 Bolander and Blackburn (2007)、(2009) 续之。Cerrito and Cialdea (2010) 另提出一种基于表列的混合逻辑判定程序；其他基于证明论的判定程序见 Kaminski and Smolka (2009)，其程序基于涉及简单类型 lambda 演算的高阶混合逻辑表述。

Hansen, Bolander, and Braüner (2018) 给出多值混合逻辑的基于表列的判定程序。所谓多值混合逻辑，即把二值经典逻辑基础推广为多值逻辑基础，其真值空间具有有限 Heyting 代数结构。Hansen (2010) 则给出公共宣告逻辑（一种动态认知逻辑）混合化版本的基于表列的判定程序，这也是 Hansen (2011) 博士论文的一大主题。

Braüner (2011a) 探讨了混合逻辑的自然演绎证明论，并给出无切 Gentzen 序列系统。无切性经规范化自然演绎系统证得，但亦可直接证明，见 Indrzejczak (2016)。Braüner (2011a) 的自然演绎与 Gentzen 系统可增补证明规则，以对应所谓 **几何理论** 所表达的可及关系一阶条件（这自然类似于以纯公理扩展表列与公理系统）。另见 Braüner and de Paiva (2006) 所给直觉主义混合逻辑的自然演绎系统（Braüner (2011a) 第 8 章）。

与混合逻辑类似的逻辑，其 Gentzen 与自然演绎系统早在 20 世纪 90 年代即由 Jerry Seligman 探究，概述见 Seligman (2001)。Seligman 尤其发展了处理任意公式、而非仅处理满足陈述的证明系统；多数混合逻辑证明系统则只处理满足陈述，借满足算子获取隐于模态之后的信息。此种风格的自然演绎系统由 Seligman (1997) 引入，并在 Braüner (2011a) 第 4 章进一步发展。Seligman 式表列系统见 Blackburn, Bolander, Braüner, and Jørgensen (2017)，文中给出句法完全性证明；其语义完全性证明则见 Jørgensen, Blackburn, Bolander, Braüner (2016)。此类系统中的推理并不直接依赖满足算子所提供的全局编码，故更契合模态逻辑标准 Kripke 语义的局部特性。事实上，这种更局部的推理风格，使这些系统适于形式化某些心理学推理任务中的视角性推理，见 Braüner (2014b) 及 Braüner, Blackburn, and Polyanskaya (2016)。

如前所述，Blackburn, Bolander, Braüner, and Jørgensen (2017) 与 Jørgensen, Blackburn, Bolander, Braüner (2016) 给出了混合逻辑 Seligman 式表列系统的完全性证明。本此，From (2021) 与 From, Blackburn, and Villadsen (2020) 借证明助手 Isabelle/HOL 将这些系统的完全性完全形式化。

消解演算与模型检验方面亦已有若干成果：消解演算见 Areces, de Rijke, and de Nivelle (2001) 与 Areces and Gorin (2011)；模型检验结果见 Franceschet and de Rijke (2006) 与 Lange (2009)。

## 8 量化混合逻辑

量化混合逻辑另作处理。一阶模态逻辑版本繁多，一阶混合逻辑亦然。一阶混合逻辑的表列系统见 Blackburn and Marx (2002)；自然演绎与公理系统见 Braüner (2011a) 第 6 章，该书第 7 章则论内涵一阶混合逻辑的自然演绎。Indrzejczak (2020) 给出带 lambda 算子以及存在与有定义谓词的一阶混合逻辑 Gentzen 式序列演算。Barbosa, Martins, and Carreteiro (2014) 则公理化了称为等式一阶混合逻辑的一阶混合逻辑片段。

值得注意的是，一阶混合逻辑恰具备证明插值定理所需之特征：插值在许多著名一阶模态逻辑中失效，其混合化对应物却保有该性质，见 Areces, Blackburn, and Marx (2003) 与 Blackburn and Marx (2003)。前文给出插值的模型论证明，后文给出基于表列系统计算插值项的算法。

Areces, Blackburn, Huertas, and Manzano (2014) 讨论高阶模态逻辑（即建于 Church 简单类型论之上的模态逻辑）的混合逻辑版本，给出公理系统并相对于 Henkin 型语义证明完全性。Blackburn, Huertas, Manzano, and Jørgensen (2014) 将这些结果推及下箭头约束子，并给出与一阶逻辑有界片段间的双向翻译（见上文）。

有时 Prior 不把名项当作第二类命题符号引入，而以命题量词配合如下定义的 $\mathtt{Q}$ 算子造出它们：

> $\mathtt{ Qp = \Diamond p \wedge \forall q (\Box (p \rightarrow q) \vee \Box (p \rightarrow \neg q)) }$

此处 $\mathtt{\Box}$、$\mathtt{\Diamond}$ 为全称模态的方框与菱形形式。在普通命题符号 $\mathtt{p}$ 前冠以 $\mathtt{Q}$ 算子，即把 $\mathtt{p}$ 化为名项。更准确地说，若命题量词 $\mathtt{\forall q}$ 的范围取一切世界集合，则 $\mathtt{Qp}$ 表示 $\mathtt{p}$ 指称单元素集，即 $\mathtt{p}$ 是标准名项。但命题量词另有一种解释方式，称为一般（或 Henkin）方式，其范围是 **预先选定** 的世界子集。两种解释之下，$\mathtt{Q}$ 算子生出两种不同的名项“物种”；结果表明，二者在全称例示规则上表现各异。Blackburn, Braüner, and Kofod (2020) 对此作了研究，给出带 Henkin 式命题量词、兼含两种名项的混合逻辑表列系统，并说明这种形式定义的“物种划分”与 Prior 著作中可辨识的两种名项直觉颇为契合。

20 世纪 90 年代中期以来，混合逻辑研究蔚然成风。更多文献请参书目所列。另见下文网络资源。

## References（引用注释）

**以下文献从原文照录，不作翻译；中国文献译为中文。**

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

[^areces-2000]: Areces, C., 2000. *Logic Engineering. The Case of Description and Hybrid Logics*, Ph.D. thesis, Institute for Logic, Language and Computation, University of Amsterdam.
[^areces-1999]: Areces, C., Blackburn, P., and Marx, M., 1999. “The Computational Complexity of Hybrid Temporal Logics”, *The Logic Journal of the IGPL*, 8: 653–679.
[^areces-2001]: –––, 2001. “Hybrid Logics: Characterization, Interpolation and Complexity”, *Journal of Symbolic Logic*, 66: 977–1010.
[^areces-2003]: –––, 2003. “Repairing the Interpolation Theorem in Quantified Modal Logic”, *Annals of Pure and Applied Logic*, 124: 287–299.
[^areces-2014]: Areces, C., Blackburn, P., Huertas, A., and Manzano, M., 2014. “Completeness in Hybrid Type Theory”, *Journal of Philosophical Logic*, 43: 209–238.
[^areces-2001-2]: Areces, C., de Rijke, M., and de Nivelle, H., 2001. “Resolution in Modal, Description and Hybrid Logic”, *Journal of Logic and Computation*, 11: 717–736.
[^areces-2021]: Areces, C. and Fervari, R., 2021. “Axiomatizing Hybrid XPath with Data”, *Logical Methods in Computer Science*, 17:5:1–5:37.
[^areces-2018]: Areces, C., Fervari, R., Hoffmann, G., and Martel, M., 2018. “Satisfiability for Relation-Changing Logics”, *Journal of Logic and Computation*, 28: 1443–1470.
[^areces-2011]: Areces, C. and Gorin, D., 2011. “Resolution with Order and Selection for Hybrid Logics”, *Journal of Automated Reasoning*, 46: 1–42.
[^areces-2006]: Areces, C. and ten Cate, B., 2006. “Hybrid Logics”, in Blackburn, van Benthem, and Wolter (eds.) (2006): 821–868.
[^barbosa-2014]: Barbosa, L.S., Martins, M.A., and Carreteiro, M., 2014. “A Hilbert-Style Axiomatisation for Equational Hybrid Logic”, *Journal of Logic, Language and Information*, 23: 31–52.
[^blackburn-1993]: Blackburn, P., 1993. “Nominal Tense Logic”, *Notre Dame Journal of Formal Logic*, 14: 56–83.
[^blackburn-2000]: –––, 2000. “Internalizing Labelled Deduction”, *Journal of Logic and Computation*, 10: 137–168.
[^blackburn-2006]: –––, 2006. “Arthur Prior and Hybrid Logic”, *Synthese*, 150: 329–372.
[^blackburn-2017]: Blackburn, P., Bolander, T., Braüner, T., and Jørgensen, K.F., 2017. “Completeness and Termination for a Seligman-style Tableau System”, *Journal of Logic and Computation*, 27: 81–107.
[^blackburn-2020]: Blackburn, P., Braüner, T., and Kofod, J.L., 2020. “Remarks on Hybrid Modal Logic with Propositional Quantfiers”, in *The Metaphysics of Time: Themes from Prior* (*Logic and Philosophy of Time*, No. 4), pp. 401–426, Aalborg Universitetsforlag.
[^blackburn-2001]: Blackburn, P. and Goranko, V., 2001. “Hybrid Ockhamist Temporal Logic”, in *Proc. of the Eighth International Symposium on Temporal Representation and Reasoning (TIME-01)*, pp. 183–188, IEEE Computer Society Press.
[^blackburn-2014]: Blackburn, P., Huertas, A., Manzano, M., and Jørgensen, K.F., 2014. “Henkin and Hybrid Logic”, in *The Life and Work of Leon Henkin: Essays on His Contributions* (Studies in Universal Logic), pp. 279–306, Birkhäuser.
[^blackburn-2012]: Blackburn, P. and Jørgensen, K.F., 2012. “Indexical hybrid tense logic”, in *Advances in Modal Logic* (Volume 9), pp. 144–160, London: College Publications.
[^blackburn-2013]: –––, 2013. “Contextual validity in hybrid logic”, in *Modeling Using Context* (Lecture Notes in Computer Science: Volume 8177), pp. 185–198, Heidelberg: Springer.
[^blackburn-2016a]: –––, 2016a. “Arthur Prior and ‘now’”, *Synthese*, 193: 3665–3676.
[^blackburn-2016b]: –––, 2016b. “Reichenbach, Prior and hybrid tense logic”, *Synthese*, 193: 3677–3689.
[^blackburn-2002]: Blackburn, P. and Marx, M., 2002. “Tableaux for Quantified Hybrid Logic”, in *Automated Reasoning with Analytic Tableaux and Related Methods, TABLEAUX* (Lecture Notes in Artificial Intelligence: Volume 2381), pp. 38–52, Heidelberg: Springer.
[^blackburn-2003]: –––, 2003. “Constructive Interpolation in Hybrid Logic”, *Journal of Symbolic Logic*, 68: 463–480.
[^blackburn-1995]: Blackburn, P. and Seligman, J., 1995. “Hybrid Languages”, *Journal of Logic, Language and Information*, 4: 251–271.
[^blackburn-2006-2]: Blackburn, P. and ten Cate, B., 2006. “Pure Extensions, Proof Rules, and Hybrid Axiomatics”, *Studia Logica*, 84: 277–322.
[^blackburn-1998]: Blackburn, P. and Tzakova, M., 1998. “Hybridizing Concept Languages”, *Annals of Mathematics and Artificial Intelligence*, 24: 23–49.
[^blackburn-1999]: –––, 1999. “Hybrid Languages and Temporal Logic”, *Logic Journal of the IGPL*, 7: 27–54.
[^blackburn-2006-3]: Blackburn, P., van Benthem, J., and Wolter, F. (eds.), 2006. *Handbook of Modal logic*, Amsterdam: Elsevier.
[^bolander-2007]: Bolander, T. and Blackburn, P., 2007. “Termination for Hybrid Tableaus”, *Journal of Logic and Computation*, 17: 517–554.
[^bolander-2009]: –––, 2009. “Terminating Tableau Calculi for Hybrid Logics Extending K”, in *Proceedings of Methods for Modalities 5* (Electronic Notes in Theoretical Computer Science: Volume 231), pp. 21–39, Amsterdam: Elsevier.
[^bolander-2006]: Bolander, T. and Braüner, T., 2006. “Tableau-Based Decision procedures for Hybrid Logic”, *Journal of Logic and Computation*, 16: 737–763.
[^braüner-2002]: Braüner, T., 2002. “Modal logic, Truth, and the Master Modality”, *Journal of Philosophical Logic*, 31: 359–386.
[^braüner-2011a]: –––, 2011a. *Hybrid Logic and its Proof-Theory* (Applied Logic Series: Volume 37), Dordrecht-Heidelberg-Berlin-New York: Springer.
[^braüner-2011b]: –––, 2011b. “Intuitionistic Hybrid Logic: Introduction and Survey”, *Information and Computation*, 209: 1437–1446.
[^braüner-2014a]: –––, 2014a. “First-order Hybrid Logic: Introduction and Survey”, *Logic Journal of the IGPL*, 22: 155–165.
[^braüner-2014b]: –––, 2014b. “Hybrid-Logical Reasoning in the Smarties and Sally-Anne Tasks”, *Journal of Logic, Language and Information*, 23: 415–439.
[^braüner-2016]: Braüner, T., Blackburn, P., and Polyanskaya, I., 2016. “Second-order false-belief tasks: Analysis and formalization”, in *Logic, Language, Information, and Computation : 23rd International Workshop, WoLLIC* (Lecture Notes in Computer Science: Volume 9803), pp. 125–144, Heidelberg: Springer.
[^braüner-2006]: Braüner, T. and de Paiva, V., 2006. “Intuitionistic Hybrid Logic”, *Journal of Applied Logic*, 4: 231–255.
[^bull-1970]: Bull, R., 1970. “An Approach to Tense Logic”, *Theoria*, 36: 282–300.
[^cerrito-2010]: Cerrito, S. and Cialdea, M., 2010. “Nominal Substitution at Work with the Global and Converse Modalities”, in *Advances in Modal Logic* (Volume 8), pp. 57–74, London: College Publications.
[^conradie-2006]: Conradie, W., Goranko, V., and Vakarelov, D., 2006. “Algorithmic Correspondence and Completeness in Modal Logic II. Polyadic and Hybrid Extensions of the Algorithm SQEMA”, *Journal of Logic and Computation*, 16: 579–612.
[^copeland-1996]: Copeland, J. (ed.), 1996. *Logic and Reality: Essays in the Legacy of Arthur Prior*, Oxford: Clarendon Press.
[^costa-2017]: Costa, D. and Martins, M.A., 2017. “Paraconsistency in Hybrid Logic”, *Journal of Logic and Computation*, 27: 1825–1852
[^franceschet-2006]: Franceschet, M. and de Rijke, M., 2006. “Model Checking Hybrid Logics (With An Application to Semistructured Data)”, *Journal of Applied Logic*, 4: 279–304.
[^from-2021]: From, A.H., 2021. “Completeness for a Terminating Seligman-Style Tableau System”, in *26th International Conference on Types for Proofs and Programs* (TYPES 2020), Leibniz International Proceedings in Informatics (LIPIcs): Volume 188, Schloss Dagstuhl–Leibniz-Zentrum für Informatik, pp. 5:1–5:17.
[^from-2020]: From, A.H., Blackburn, P., and Villadsen, J., 2020. “Formalizing a Seligman-Style Tableau System for Hybrid Logic”, in: *Proceedings of 10th International Joint Conference on Automated Reasoning* (IJCAR), Lecture Notes in Computer Science (Voume 12166), pp. 474–482, Cham: Springer-Verlag.
[^gabbay-2006]: Gabbay, D. and Woods, J. (eds.), 2006. *Logic and the Modalities in the Twentieth Century. The Handbook of the History of Logic* (Volume 7), Amsterdam: Elsevier.
[^gargov-1993]: Gargov, G. and Goranko, V., 1993. “Modal Logic with Names”, *Journal of Philosophical Logic*, 22: 607–636.
[^goranko-1994]: Goranko, V., 1994. “Temporal Logic with Reference Pointers”, in *Proceedings of the 1st International Conference on Temporal Logic* (Lecture Notes in Artificial Intelligence: Volume 827), pp. 133–148, Berlin: Springer.
[^goranko-1996]: –––, 1996. “Hierarchies of Modal and Temporal Logics with Reference Pointers”, *Journal of Logic, Language, and Information*, 5: 1–24.
[^goranko-2001]: Goranko, V. and Vakarelov, D., 2001. “Sahlqvist Formulas in Hybrid Polyadic Modal Logics”, *Journal of Logic and Computation*, 11: 737–754.
[^hansen-2010]: Hansen, J.U., 2010. “Terminating Tableaux for Dynamic Epistemic Logics”, in *Proceedings of the 6th Workshop on Methods for Modalities (M4M-6 2009)* (Electronic Notes in Theoretical Computer Science: Volume 262), pp. 141–156.
[^hansen-2011]: –––, 2011. *A Logic Toolbox for Modeling Knowledge and Information in Multi-Agent Systems and Social Epistemology*, Ph.D. thesis, Roskilde University.
[^hansen-2018]: Hansen, J.U., Bolander, T., and Braüner, T., 2018. “Many-Valued Hybrid Logic”, *Journal of Logic and Computation*, 28: 883–908.
[^hasle-2020]: Hasle, P., 2020. “The Beginnings of Hybrid Logic: Meredith, Prior and the Contingent Constant n”, in *The Metaphysics of Time: Themes from Prior* (Logic and Philosophy of Time No. 4), pp. 145–163, Aalborg Universitetsforlag.
[^hasle-2016]: Hasle, P. and Øhrstrøm, P., 2016. “Prior’s Paradigm for the Study of Time and its Methodological Motivation”, *Synthese*, 193: 3401–3416.
[^indrzejczak-2016]: Indrzejczak, A., 2016. “Simple cut elimination proof for hybrid logic”, *Logic and Logical Philosophy*, 25: 129–141.
[^indrzejczak-2020]: Indrzejczak, A., 2020. “Existence, Definedness and Definite Descriptions in Hybrid Modal Logic”, in *Advances in Modal Logic* (Volume 13), pp. 349–368, London: College Publications.
[^jørgensen-2016]: Jørgensen, K.F., Blackburn, P., Bolander, B., and Braüner, T., 2016. “Synthetic Completeness Proofs for Seligman-style Tableau Systems”, in *Advances in Modal Logic* (Volume 11), pp. 302–321, London: College Publications.
[^kaminski-2009]: Kaminski, M. and Smolka, G., 2009. “Terminating Tableau Systems for Hybrid Logic with Difference and Converse”, *Journal of Logic, Language and Information*, 18: 437–464.
[^kamp-1971]: Kamp, H., 1971. “Formal properties of ‘now’”, *Theoria*, 37: 237–273.
[^kracht-1997]: Kracht, M. and Wolter, F., 1997. “Simulation and Transfer Results in Modal Logic — A Survey”, *Studia Logica*, 59: 149–177.
[^lange-2009]: Lange, M., 2009. “Model Checking for Hybrid Logic”, *Journal of Logic, Language and Information*, 18: 465–491.
[^müller-2007]: Müller, T., 2007. “Prior’s Tense-Logical Universalism”, *Logique et Analyse*, 50: 223–252.
[^neves-2016]: Neves, R., Madeira, A., Martins, M.A., Barbosa, L.S., 2016. “Proof theory for hybrid(ised) logics”, *Science of Computer Programming*, 126: 73–93.
[^øhrstrøm-1993]: Øhrstrøm, P. and Hasle, P., 1993. “A.N. Prior’s Rediscovery of Tense Logic”, *Erkenntnis*, 39: 23–50.
[^øhrstrøm-1995]: –––, 1995. *Temporal Logic. From Ancient Ideas to Artificial Intelligence*, Dordrecht: Kluwer.
[^øhrstrøm-2006]: –––, 2006. “A.N. Prior’s Logic”, in Gabbay and Woods (2006), pp. 399–446.
[^passy-1985]: Passy, S. and Tinchev, T., 1985. “Quantifiers in Combinatory PDL: Completeness, Definability, Incompleteness”, in *Fundamentals of Computation Theory FCT 85* (Lecture Notes in Computer Science: Volume 199), pp. 512–519, Berlin: Springer.
[^passy-1991]: Passy, S. and Tinchev, T., 1991. “An Essay in Combinatory Dynamic Logic”, *Information and Computation*, 93: 263–332.
[^prior-1967]: Prior, A.N., 1967. *Past, Present and Future*, Oxford: Clarendon Press.
[^prior-1968]: –––, 1968. *Papers on Time and Tense*, Oxford: Clarendon Press.
[^prior-2003]: –––, 2003. *Papers on Time and Tense*, second revised and expanded edition of Prior 1968, edited by P. Hasle, P. Øhrstrøm, T. Braüner, and J. Copeland, Oxford: Oxford University Press.
[^prior-1977]: Prior, A.N. and Fine, K., 1977. *Worlds, Times and Selves*, London: Duckworth; based on manuscripts by Prior with a preface and a postscript by K. Fine.
[^reichenbach-1947]: Reichenbach, H., 1947. *Elements of Symbolic Logic*, New York: Free Press.
[^seligman-1997]: Seligman, J., 1997. “The logic of correct description”, in *Advances in Intensional Logic* (Applied Logic Series: Volume 7), pp. 107–135, Dordrecht: Kluwer.
[^seligman-2001]: Seligman, J., 2001. “Internalisation: The Case of Hybrid Logics”, *Journal of Logic and Computation*, 11: 671–689.
[^sylvan-1996]: Sylvan, R., 1996. “Other Withered Stumps of Time”, in Copeland (1996), pp. 111–130.
[^cate-2004]: ten Cate, B., 2004. *Model Theory for Extended Modal Languages*, PhD thesis, Institute for Logic, Language and Computation, University of Amsterdam.

## 学术工具

* [如何引用本词条](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=logic-hybrid)。
* [预览本词条的 PDF 版本](https://leibniz.stanford.edu/friends/preview/logic-hybrid/)，见 [SEP 学会之友](https://leibniz.stanford.edu/friends/)。
* 在 [InPhO](https://www.inphoproject.org/entity?sep=logic-hybrid&redirect=True) 查找与本词条相关的话题与思想家。
* 在 [PhilPapers](https://philpapers.org/sep/logic-hybrid/) 查看本词条的增强文献目录及其数据库链接。

## 其他网络资源

* [A.N. Prior——时态逻辑之父](http://www.priorstudies.org/)

## 相关词条

未来偶然性 | 模态逻辑 | 时间逻辑 | 可能性主义与实在主义辩论 | 阿瑟·普赖尔

**（译注：相关词条的中文站内链接将由管线在对应词条重译完成后统一挂接。）**
