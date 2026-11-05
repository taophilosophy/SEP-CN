# 可证性逻辑 Provability Logic (Verbrugge, Rineke (L.C.))

*首次发表于 2003 年 4 月 2 日；2024 年 3 月 4 日实质修订。*

可证性逻辑是一个模态逻辑，用于研究算术理论能以受限语言就其可证性谓词表达些什么。这一逻辑受元数学发展的启发，如哥德尔（Gödel）1931 年的不完备性定理与 Löb 1953 年的定理。作为模态逻辑，它自七十年代初以来被持续研究，并在数学基础中有重要应用。

从哲学的观点看，可证性逻辑之所以有趣，是因为在一个固定的算术理论中，可证性概念有独特而无争议的含义。这一点不同于模态逻辑与认知逻辑所研究的必然性与知识等概念。此外，可证性逻辑为研究自指概念提供了工具。

## 1 可证性逻辑的历史

两条研究脉络催生了可证性逻辑。第一条源自哥德尔（1933）的一篇论文：他在其中给出从直觉主义命题逻辑到模态逻辑（更准确地说，到今天所谓的 S4 系统）的翻译，并简短提及可证性可被视为一个模态算子。更早之前，C.I. Lewis 以严格蕴涵作为一种演绎性（deducibility）开启模态逻辑的现代研究——他心中的演绎或许指《数学原理》这类形式系统中的演绎，但其著作对此并不明确。

另一条脉络始于元数学研究：数学理论通过编码有趣的性质，能对自身说些什么？1952 年，亨金（L. Henkin）受哥德尔不完备性定理启发，提出一个看似简单的问题。为表述亨金的问题，需要一些背景。回顾一下：哥德尔第一不完备性定理说，对像皮亚诺算术这样足够强的形式理论而言，任何断言自身不可证的句子事实上不可证。另一方面，从形式理论“外部”可以看出：这样的句子在标准模型中为真——这指出了真与可证之间的一个重要区分。

更形式化地说，令 $\ulcorner A \urcorner$ 表示算术公式 $A$ 的哥德尔数，即给 $A$ 指派数值代码的结果。令 $\Prov$ 表示皮亚诺算术的形式化可证性谓词，其形式为 $\exists p \, \Proof(p,x)$。这里 $\Proof$ 是皮亚诺算术的形式化证明谓词，$\Proof(p,x)$ 表示“哥德尔数 $p$ 为以哥德尔数 $x$ 编码的公式编码了一个出自皮亚诺算术公理的正确证明”。（更精确的表述见 Smoryński (1985), Davis (1958)。）现在假设皮亚诺算术证明 $A \leftrightarrow \neg$ $\Prov (\ulcorner A \urcorner)$，那么由哥德尔的结果，$A$ 在皮亚诺算术中不可证，因而为真——因为自指句子 $A$ 说的正是“我不可证”。

亨金则想知道：对于断言自身可证性的句子能说些什么？假设皮亚诺算术证明 $B \leftrightarrow \Prov(\ulcorner B \urcorner)$，这对 $B$ 意味着什么？三年后，M. Löb 接下这一挑战，以令人惊讶的方式回答了亨金的问题。虽然在皮亚诺算术中可证的一切句子关于自然数确实为真，Löb 却证明：这一事实的形式化版本 $\Prov(\ulcorner B \urcorner) \rightarrow B$ 只有在皮亚诺算术本来就证明 $B$ 的平凡情形下才能在皮亚诺算术中得证。这一结果如今称为 Löb 定理，立即回答了亨金的问题。（Löb 定理的证明见第 4 节。）Löb 还给出其定理的形式化版本，即皮亚诺算术证明

$$ \Prov(\ulcorner \Prov(\ulcorner B\urcorner ) \rightarrow B\urcorner ) \rightarrow \Prov(\ulcorner B \urcorner ). $$

正是在同一篇论文中，Löb 为皮亚诺算术的可证性谓词表述了三个条件——相较于 Hilbert 与 Bernays 在 1939 年为证明哥德尔第二不完备性定理而引入的那组复杂条件，这是一处有用的修改。下文中，从皮亚诺算术推出 $A$ 记作 $\PA \vdash A$：

1. 若 $\PA \vdash A$，则 $\PA \vdash \Prov(\ulcorner A \urcorner )$；
2. $\PA \vdash \Prov(\ulcorner A\rightarrow B\urcorner) \rightarrow ( \Prov(\ulcorner A \urcorner ) \rightarrow \Prov(\ulcorner B \urcorner ));$
3. $\PA \vdash \Prov(\ulcorner A \urcorner ) \rightarrow \Prov(\ulcorner \Prov(\ulcorner A \urcorner ) \urcorner ).$

这些如今所谓的 Löb 条件，似乎呼唤一次模态逻辑式的考察，其中模态词 $\Box$ 表示 PA 中的可证性。讽刺的是，Löb 定理的形式化版本第一次作为模态原则

$$ \Box(\Box A \rightarrow A) \rightarrow \Box A $$

被表述出来，是在 Smiley 1963 年一篇关于伦理学之逻辑基础的论文中——它完全没有考虑算术。然而，更相关的研究直到 Löb 论文发表近二十年后才真正开始。七十年代早期见证了命题可证性逻辑的迅速发展：不同国家的若干研究者各自独立证明了最重要的结果，见第 2、3、4 节的讨论。命题可证性逻辑最终证明恰好捕捉许多形式算术理论能以命题手段就其自身可证性谓词所表达的内容。晚近，研究者考察这一进路的边界，并提出若干更有表达力的可证性逻辑扩充（见第 5 节）。

## 2 命题可证性逻辑的公理系统

命题可证性逻辑的语言，除命题原子、通常的真值函项算子以及矛盾符号 $\bot$ 外，还含有一个模态算子 $\Box$。这一算子的意向含义是“在 $T$ 中可证”，其中 $T$ 是足够强的形式理论——比如皮亚诺算术（见第 4 节）。$\Diamond A$ 是 $\neg\,\Box\neg\, A$ 的缩写。因此，该语言与模态逻辑词条中 K、S4 等系统的语言相同。

### 2.1 公理与规则

命题可证性逻辑常称为 GL，以纪念哥德尔与 Löb。（文献中见于等价系统的别名有 L、G、KW、K4W 与 PrL。）逻辑 GL 由在基本模态逻辑 K 上添加如下公理而得：

$$\tag{GL} \Box(\Box A \rightarrow A) \rightarrow \Box A. $$

回顾一下：由于 GL 扩充 K，它包含一切具有命题重言式形式的公式。同理，GL 包含

$$\tag{Distribution Axiom} \Box(A \rightarrow B) \rightarrow (\Box A \rightarrow \Box B). $$

此外，它在分离规则下封闭——该规则允许从 $A \rightarrow B$ 与 $A$ 导出 $B$；也在概括规则下封闭——后者说：若 $A$ 是 GL 的定理，则 $\Box A$ 亦然。

记号 $\GL \vdash A$ 表示模态公式 $A$ 在命题可证性逻辑中的可证性。不难看出，模态公理 $\Box A \rightarrow \Box\Box A$（即模态逻辑的公理 4）确实在 GL 中可证。为证此，可在公理 (GL) 中以 $A \wedge \Box A$ 代入 $A$。看到所得蕴涵式的前件可从 $\Box A$ 得出后，再应用分配公理与概括规则以及一些命题逻辑即可。

注意 GL 证明许多出乎意料的定理，它们并不为 K、S4 等其他著名模态逻辑所共享。例如，公理 GL 的一个实例是 $\Box(\Box\bot \rightarrow \bot) \rightarrow \Box\bot$，由其他公理与规则可从它推出：对任意公式 $A$ 与 $B$ 都有 $\Box\Diamond A \rightarrow \Box B$。[^note-1] 除非另有明确说明，下文中的“可证性逻辑”指命题可证性逻辑的系统 GL。

至于可证性逻辑的 **证明论**，Valentini（1983）证明 GL 的一个标准相继式演算表述服从 **切割消除**。粗略地说，这意味着每个在相继式演算中从 GL 可证的公式都有一个“无绕行”的 GL 相继式证明（切割消除的精确解释见证明论之发展词条）。近年，GL 的证明论重新受到关注，例如 Goré 与 Ramanayake（2008, 2012）以及 Goré、Ramanayake 与 Shillito（2021）。切割消除为 GL 带来理想的 **子公式性质**：无切割证明中出现的所有公式都是末端相继式公式的子公式。

关于基于不同无切割相继式演算的可证性逻辑的晚近证明论研究，见（Negri 2005, 2014; Poggiolesi 2009）[^negri-2005][^poggiolesi-2009]。Negri 给出 GL 的两个等价带标记相继式演算与切割消除的语法证明。尽管因标记的缘故，这些演算不满足完整的子公式性质，其惯常推论仍可确立：带标记的形式体系允许直接完全性证明，可用于确立可判定性与有穷模型性质；也就是说，任何不可证的公式都有一个 **有穷** 反模型。

一个引人入胜的证明论新进展是 Shamkanov 对相继式型证明系统的扩充——允许 **循环证明**（Shamkanov 2014）[^shamkanov-2014]。考虑 K4 的一个相继式系统：K4 是把 GL 的公理换成较弱的公理 $\Box A \rightarrow \Box\Box A$（公理 4）所得的模态系统。但设想允许开放假设，只要同一相继式在证明树中严格低于该假设处出现。更技术性地说：把普通推导树中每个非公理叶子与一个相同的内部节点相连，即可得到循环推导。Shamkanov（2014）证明所得系统一致，而且一般地，每个相继式有 GL 推导当且仅当它有循环 K4 推导。循环证明也提供一种方法，证明式地表明 Lyndon 插值定理对 GL 成立（Shamkanov 2011）[^shamkanov-2011]。GL 的标准插值此前已用不同方法证明（Boolos 1979; Smoryński 1978; Rautenberg 1983）[^boolos-1979][^rautenberg-1983][^smoryński-1978]，一致插值亦然（Shavrukov 1993b, Bílková 2016, Férée et al. [Other Internet Resources]）[^bílková-2016][^shavrukov-1993b]。（关于一阶逻辑的 Lyndon 插值定理的更多信息，另见一阶模型理论词条。）

### 2.2 不动点定理

关于可证性逻辑的主要“模态”结果是不动点定理，由 D. de Jongh 与 G. Sambin 于 1975 年独立证明（Sambin 1976, Smoryński 1985, de Jongh forthcoming）[^smoryński-1985][^sambin-1976]。尽管它以严格的模态方法表述并证明，不动点定理仍有重大的算术意义。其要旨是：在如下意义上，自指其实并不必要。假设给定公式 $A(p)$ 中命题变元 $p$ 的一切出现都在可证性算子的辖域内，例如 $A(p) = \neg\Box p$，或 $A(p) = \Box(p \rightarrow q)$。那么存在一个不含 $p$ 的公式 $B$，使得 $B$ 中出现的所有命题变量都已出现于 $A(p)$ 中，且

$$ \GL \vdash B \leftrightarrow A(B). $$

这个公式 $B$ 称为 $A(p)$ 的一个 **不动点**。而且不动点是唯一的，或更准确地说：若另有公式 $C$ 使得 $ \GL \vdash C \leftrightarrow A(C)$，则必有 $ \GL \vdash B \leftrightarrow C$。文献中的大多数证明都给出可计算不动点的算法（见 Smoryński 1985, Boolos 1993, Sambin and Valentini 1982, Lindström 2006）[^boolos-1993][^smoryński-1985][^sambin-1982][^lindström-2006][^sambin-1982-2][^lindström-2006-2]。Reidhaar-Olson（1990）中可找到一个特别简短清晰的证明，以及一个计算不动点的高效算法。

例如，设 $A(p) = \neg \, \Box p$。那么由这类算法产生的不动点是 $\neg \, \Box\bot$，而且确实可证

$$ \GL \vdash \neg\,\Box\bot \leftrightarrow \neg\,\Box(\neg\,\Box\bot). $$

若对此作算术解读，从左到右的方向正是哥德尔第二不完备性定理的形式化版本：若像皮亚诺算术这样足够强的形式理论 $T$ 不证明矛盾，则在 $T$ 中不可证“$T$ 不证明矛盾”。因此，足够强的一致算术理论无法证明自身的一致性。我们将在第 4 节更精确地考察可证性逻辑与算术的关系，但为此需先给出 GL 的另一个“模态”面向：语义学。

## 3 可能世界语义与拓扑语义

与许多其他模态逻辑一样，可证性逻辑有合适的可能世界语义。回顾一下：可能世界模型（或 Kripke 模型）是三元组 $M = \langle W,R,V \rangle$，其中 $W$ 是可能世界的非空集合，$R$ 是 $W$ 上的二元可及关系，$V$ 是为 $W$ 中每个世界的每个命题变元赋真值的赋值。偶对 $F = \langle W,R \rangle$ 称为该模型的框架。公式 $A$ 在模型 $M$ 中于世界 $W$ 处为真的概念，记作 $M,w \models A$，按归纳定义。这里只重复最有趣的一条——关于可证性算子 $\Box$ 的条款：

$$ M,w \models \Box A \text{ iff for every } w', \text{ if } wRw', \text{ then } M,w' \models A. $$

关于可能世界语义的一般信息，见模态逻辑词条。

### 3.1 刻画与模态可靠性

模态逻辑 K 在所有 Kripke 模型中有效。但其扩充 GL 却不然：我们需要把可能世界模型的类限制到一个更合适的类。设公式 $A$ 在框架 $F$ 中有效，记作 $F \models A$，当且仅当 $A$ 在基于 $F$ 的所有 Kripke 模型 $M$ 的所有世界中为真。结果表明，可证性逻辑的新公理 (GL) 对应于框架上的一个条件，如下：

对所有框架 $F = \langle W,R \rangle, F \models \Box(\Box p \rightarrow p) \rightarrow \Box p$ 当且仅当 $R$ 传递且逆良基。

这里 **传递性** 是众所周知的性质：对 $W$ 中所有世界 $w_1$、$w_2$、$w_3$，若 $w_1 Rw_2$ 且 $w_2 Rw_3$，则 $w_1 Rw_3$。一个关系是 **逆良基的**，当且仅当不存在无穷上升序列，即形如 $w_1 Rw_2 Rw_3 R \ldots$ 的序列。注意逆良基框架也非自反：因为若 $wRw$，就会产生无穷上升序列 $wRwRwR\ldots$。

上述对应结果立即表明：GL 相对于传递逆良基框架上那类可能世界模型是模态可靠的，因为 GL 的一切公理与规则在此类模型上有效。问题是完全性是否也成立：例如，公式 $\Box A \rightarrow \Box\Box A$ 在所有传递框架上有效，且如第 1 节所述确实在 GL 中可证。但 **每一个** 在所有传递逆良基框架上有效的公式也都在 GL 中可证吗？

### 3.2 模态完全性

GL 的算术意义尚无人知晓时，K. Segerberg 就于 1971 年证明 GL 相对于传递逆良基框架确实完全；D. de Jongh 与 S. Kripke 也独立证明了这一结果。Segerberg 甚至证明 GL 相对于更受限的类——有穷传递非自反树——也完全；这一事实后来证明对 Solovay 算术完全性定理的证明非常有用（见第 4 节）。

模态可靠性与完全性定理立即给出一个判定程序：通过在有界深度的非自反传递树中做深度优先搜索，即可对任意模态公式 $A$ 检查 $A$ 是否从 GL 得出。更细致地看这一程序，可以证明 GL 在计算复杂性类 PSPACE 中可判定，一如著名模态逻辑 K、T 与 S4。这意味着存在一台图灵机：给定公式 $A$ 为输入，回答 $A$ 是否从 GL 得出；该图灵机计算所需内存的大小只是 $A$ 长度的多项式。可以证明 GL 的判定问题（再次如同 K、T、S4 的判定问题）是 **PSPACE-完全的**：PSPACE 中所有其他问题都不比判定给定公式是否为 GL 的定理更难。（关于 GL 的自动定理证明器的描述，见 Goré and Kelly 2007 [Other Internet Resources]。）

为给复杂性一个参照系：P 类——可在输入长度的多项式时间内计算的函数之类——包含于 PSPACE，而 PSPACE 又包含于 EXPTIME 类——可在指数时间内计算的函数之类（见可计算性与复杂性词条）。这两个包含关系是否为真包含，仍是著名的未决问题，尽管许多复杂性理论家相信如此。另一些著名模态逻辑——如有共同知识的认知逻辑——在 EXPTIME 中可判定，因此它们可能比 GL 更复杂，取决于这些未决问题。

### 3.3 强完全性的失效

许多著名模态逻辑 $S$ 不仅相对于合适的框架类完全，甚至 **强完全**。为解释强完全性，需要 **从一组假设导出** 的概念。公式 $A$ 从假设集 $\Gamma$ 在模态逻辑 $S$ 中可导，写作 $\Gamma \vdash A$，如果 $A$ 在 $\Gamma$ 中，或 $A$ 可从 $\Gamma$ 中的公式与 $S$ 的公理经应用分离规则与概括规则得出。这里概括规则只能用于无假设的推导（见 Hakli and Negri 2010）。

一个模态逻辑 $S$ 是 **强完全的**，如果对所有（有穷或无穷）集合 $\Gamma$ 与所有公式 $A$：

若在合适的 $S$-框架上，$A$ 在 $\Gamma$ 的所有公式都为真的所有世界中为真，则 $\Gamma \vdash A$ 在逻辑 $S$ 中成立。

这一条件对 K、M、K4、S4 与 S5 等系统成立。若限于有穷集 $\Gamma$，上述条件对应于（普通）完全性。

然而强完全性对可证性逻辑不成立，因为 **语义紧致性** 失效。语义紧致性是这样一条性质：对每个无穷公式集 $\Gamma$，

若 $\Gamma$ 的每个有穷子集 $\Delta$ 都有一个合适 $S$-框架上的模型，则 $\Gamma$ 也有一个合适 $S$-框架上的模型。

作为反例，取无穷公式集

$$\begin{align} \Gamma &= \{\Diamond p_0, \Box(p_0 \rightarrow \Diamond p_1), \Box(p_1 \rightarrow \Diamond p_2), \Box(p_2 \rightarrow \Diamond p_3), \ldots, \\ &\qquad\ \Box(p_n \rightarrow \Diamond p_{n+1}), \ldots\} \end{align}$$

于是对 $\Gamma$ 的每个有穷子集 $\Delta$，都可以在传递逆良基框架上构造一个模型，以及模型中 $\Delta$ 的所有公式都为真的一个世界。因此由模态可靠性，对任何有穷 $\Delta \subseteq \Gamma$，GL 不能从 $\Delta$ 证明 $\bot$；**更不用说** 从 $\Gamma$ 证明 $\bot$——因为任何 GL 证明都是有穷的。另一方面，容易看出：不存在传递逆良基框架上的模型，使得在某个世界中 $\Gamma$ 的所有公式都成立。于是 $\bot$ 语义上由 $\Gamma$ 得出，却不能在 GL 中从它证明——这与强完全性的条件相矛盾。[^note-2]

### 3.4 可证性逻辑的拓扑语义

作为可能世界语义的替代，许多模态逻辑可以赋予拓扑语义。显然，命题可解释为拓扑空间的子集。同样容易看出：命题联结词 $\wedge$ 对应集合论运算 $\cap$，$\vee$ 对应 $\cup$，$\neg$ 对应集合论补，$\rightarrow$ 对应 $\subseteq$。包含反射公理 $\Box A \rightarrow A$ 的模态逻辑，其模态算子也有特别自然的解释：对这些逻辑，$\Diamond$ 对应拓扑空间中的闭包算子，而 $\Box$ 对应内部。为看出这些解释为何合适，注意反射公理对应于这样的事实：每个集合包含于其闭包，且每个集合包含其内部。

然而，可证性逻辑 **不** 证明反射，因为反射的实例 $\Box\bot \rightarrow \bot$ 会与公理 (GL) 导致矛盾。

因此可证性逻辑需要不同的进路。基于 J. McKinsey 与 A. Tarski（1944）的建议，L. Esakia（1981, 2003）考察了把 $\Diamond$ 解释为导集算子 $d$——它把集合 $B$ 映到其极限点之集 $d(B)$。为解释这一 $\Diamond$ 解释的推论，还需两个定义：概念 **自密的** 与 **散布的**。拓扑空间的子集 $B$ 称为 **自密的**，如果 $B \subseteq d(B)$。拓扑空间称为 **散布的**，如果它没有非空的自密子集。区间拓扑下的序数就是散布空间的例子。Esakia（1981）证明一个重要对应：他表明拓扑空间 **满足公理 GL** 当且仅当该空间 **散布**。这一对应很快引出 Abashidze（1985）与 Blass（1990）各自独立发现的结果：可证性逻辑相对于任何序数 $\ge \omega^\omega$ 完全。

过去几十年，可证性逻辑的拓扑语义经历真正的复兴，尤其在对 Japaridze 的双模可证性逻辑 GLB 的研究中——GLB 是 GL 的扩充（Japaridze 1986）[^japaridze-1986]。结果表明 GLB 相对于其可能世界语义是 **模态不完全的**：它不对应于任何框架类。[^note-3] 这一特点使双模 GLB 与单模 GL 形成鲜明对照——如上所述，后者对应于有穷传递非自反树的类。不过，Beklemishev 等人（2009）证明 GLB 相对于其 **拓扑** 语义完全（另见 Beklemishev 2009, Icard 2011）[^beklemishev-2009][^beklemishev-2009-2][^icard-2011]。Esakia 的 GL 与散布拓扑空间之间的对应，甚至可以在空间逻辑与认知逻辑的拓扑研究中找到引人入胜的回响（见 Aiello et al. 2007）[^aiello-2007]。（关于 GLB 的进一步讨论见第 5.4 节。）

## 4 可证性逻辑与皮亚诺算术

自 GL 被表述以来，研究者一直想知道：它对皮亚诺算术（PA）这类形式理论是否足够：GL 是否证明 **一切** 能以命题模态语言表达且能在皮亚诺算术中证明的关于可证性概念的内容？还是应向 GL 添加更多原理？为使这一“足够”概念更精确，我们把 **实现**（有时称翻译或解释）定义为函数 *f*：它为模态逻辑的每个命题原子指派一个算术句子，其中

* $f(\bot)=\bot;$
* $f$ 对逻辑联结词保持结构，例如 $f(B \rightarrow C) = (f(B) \rightarrow f(C));$ 且
* $\Box$ 翻译为可证性谓词 $\Prov$，因此 $f(\Box B) = \Prov(\ulcorner f(B)\urcorner ).$

### 4.1 算术可靠性

早在七十年代初就已清楚：GL 相对于 PA 是 **算术可靠的**，形式化地说：

$$ \text{If } \GL \vdash A, \text{then for all realizations } f, \PA \vdash f(A).$$

为略尝元数学滋味，让我们概述可靠性证明。

**算术可靠性证明概述**。PA 确实证明命题重言式的实现，而 GL 分配公理的可证性翻译为

$$ \PA \vdash \Prov(\ulcorner A \rightarrow B\urcorner ) \rightarrow (\Prov(\ulcorner A\urcorner ) \rightarrow \Prov(\ulcorner B\urcorner )) $$

对一切公式 *A* 与 *B*——这正是 Löb 的第二条可导出性条件（见第 1 节）。此外，PA 服从分离规则，以及概括规则的翻译：

$$ \text{If } \PA \vdash A, \text{then } \PA \vdash \Prov(\ulcorner A\urcorner ), $$

这正是 Löb 的第一条可导出性条件。最后，主公理 (GL) 的翻译确实在 PA 中可证：

$$ \PA \vdash \Prov(\ulcorner \Prov(\ulcorner A\urcorner ) \rightarrow A\urcorner ) \rightarrow \Prov(\ulcorner A\urcorner ). $$

这正是第 1 节提到的 Löb 定理的形式化版本。

让我们从 Löb 的可导出性条件概述 Löb 定理本身的证明（形式化版本的证明类似）。该证明基于哥德尔的对角化引理：对任意算术公式 $C(x)$，存在算术公式 $B$ 使得

$$ \PA \vdash B \leftrightarrow C(\ulcorner B\urcorner ). $$

用文字说，公式 $B$ 说的是“我具有性质 $C$。”

**Löb 定理的证明：** 设 $\PA \vdash \Prov(\ulcorner A\urcorner ) \rightarrow A$；须证 $\PA \vdash A$。由对角化引理，存在公式 $B$ 使得

$$ \PA \vdash B \leftrightarrow (\Prov(\ulcorner B\urcorner ) \rightarrow A). $$

由此经 Löb 的第一、第二条可导出性条件加上一些命题推理可得

$$ \PA \vdash \Prov(\ulcorner B\urcorner ) \leftrightarrow \Prov(\ulcorner \Prov(\ulcorner B\urcorner ) \rightarrow A\urcorner ). $$

于是再次由 Löb 的第二条件，

$$ \PA \vdash \Prov(\ulcorner B\urcorner ) \rightarrow (\Prov(\ulcorner \Prov(\ulcorner B\urcorner ) \urcorner ) \rightarrow \Prov(\ulcorner A\urcorner )). $$

另一方面，Löb 的第三条件给出

$$ \PA \vdash \Prov(\ulcorner B\urcorner ) \rightarrow \Prov(\ulcorner \Prov(\ulcorner B\urcorner )\urcorner ), $$

于是

$$ \PA \vdash \Prov(\ulcorner B\urcorner ) \rightarrow \Prov(\ulcorner A\urcorner ). $$

与假设 $PA \vdash \Prov(\ulcorner A\urcorner ) \rightarrow A$ 合起来，这给出

$$ \PA \vdash \Prov(\ulcorner B\urcorner ) \rightarrow A. $$

最后，对角化引理产生的等式蕴涵 $\PA \vdash B$，于是 $\PA \vdash \Prov(\ulcorner B\urcorner )$，从而

$$ \PA \vdash A, $$

如所愿。

注意在 Löb 定理中以 $\bot$ 代 $A$，我们导出：$\PA \vdash \neg\, \Prov(\ulcorner \bot\urcorner )$ 蕴涵 $\PA \vdash \bot$——这正是哥德尔第二不完备性定理的逆否。

### 4.2 算术完全性

可证性逻辑的里程碑式结果是 R. Solovay 1976 年的算术完全性定理：它表明 GL 对皮亚诺算术确实足够：

$$ \GL \vdash A \text{ if and only if for all realizations } f, \PA \vdash f(A). $$

这一定理的要旨是：模态逻辑 GL 捕捉了皮亚诺算术能以模态术语就其自身可证性谓词真实说出的一切。从左到右的方向——GL 的算术可靠性——已在上文讨论。Solovay 以逆否的方式着手证明另一个困难得多的方向。他的证明基于精巧的自指技术，这里只能窥豹一斑。

Segerberg 的模态完全性定理是 Solovay 证明 GL 相对于皮亚诺算术之算术完全性的重要第一步。假设 GL 不证明模态公式 $A$。那么由模态完全性，存在一棵有穷传递非自反树，使 $A$ 在该树的根处为假。Solovay 设计精巧的方式，在皮亚诺算术的语言中模拟这样一棵有穷树。于是他找到一个从模态公式到算术句子的实现 $f$，使得皮亚诺算术不证明 $f(A)$。

Solovay 的完全性定理提供一种构造许多皮亚诺算术不可证算术句子的替代方式。例如，容易构造可能世界模型表明 GL 不证明 $\Box p \vee \Box\neg\, p$；于是由 Solovay 定理，存在算术句子 $f(p)$ 使得皮亚诺算术不证明 $\Prov(\ulcorner f(p)\urcorner ) \vee \Prov(\ulcorner \neg\, f(p)\urcorner )$。特别地，这意味着 $f(p)$ 与 $\neg\, f(p)$ 在皮亚诺算术中都不可证：假设相反情形 $\PA \vdash f(p)$，则由 Löb 第一条件与命题逻辑得 $\PA \vdash \Prov(\ulcorner f(p)\urcorner ) \vee \Prov(\ulcorner \neg\, f(p)\urcorner )$，导致矛盾；假设 $\PA \vdash \neg\, f(p)$ 时同理。

Solovay 定理意义重大。它表明，一个不可判定形式理论（如皮亚诺算术）的有趣片段——即算术能以命题术语就其自身可证性谓词表达的那部分，可以借由一个可判定的模态逻辑来研究。GL 的可能世界语义清晰透彻。

## 5 可证性逻辑的范围

本节讨论可证性逻辑研究的一些趋势。一条重要线索关乎 GL 的范围界限：除皮亚诺算术外，GL 对哪些形式理论是合适的命题可证性逻辑？接下来我们讨论命题可证性逻辑在更有表达力的模态语言中的若干推广。

### 5.1 边界

自 1980 年代末以来，逻辑学家研究弱于皮亚诺算术的许多其他算术系统。这些逻辑学家常从可计算性问题获取灵感，例如多项式时间可计算函数的研究。他们对如下问题给出部分回答：“对哪些算术理论，Solovay 的算术完全性定理（相对于合适的可证性谓词）仍然成立？”为讨论这一问题，需要两个概念。$\Delta_0$-公式是所有量词都由一个项限定的算术公式，例如

$$ \forall y \le \bs\bs 0 \: \forall z \le y \: \forall x \le y + z \: (x + y \le (y+(y+z))), $$

其中 $\bs$ 是后继算子（“$+1$”）。算术理论 $I \Delta_0$（I 代表“归纳”）与皮亚诺算术类似，只是它允许较少的归纳：归纳模式

$$ A(0) \wedge \forall x\, (A(x) \rightarrow A(\bs x)) \rightarrow \forall x \, A(x) $$

限定于 $\Delta_0$-公式 $A$。

如 De Jongh 等人（1991）指出的，对满足以下两个条件的理论 $T$，算术完全性肯定成立：

1. $T$ 对 $\Delta_0$-公式证明归纳，并且 $T$ 证明 EXP，即表达对一切 $x$ 其幂 $2^x$ 存在的公式。用更标准的记号说：$T$ 扩充 $I \Delta_0$+EXP；
2. $T$ 不证明任何形如 $\exists x\, A(x)$ 的假句子，其中 $A(x)$ 为 $\Delta_0$-公式。

对这类理论，GL 的算术可靠性与完全性成立——只要 $\Box$ 翻译为 $\Prov_T$，即相对于 $T$ 的一个足够简单公理化的自然可证性谓词。于是对模态句子 $A$：

$$ \GL \vdash A \text{ if and only if for all realizations } f,T \vdash f(A). $$

尚不清楚条件 1 是否给出可证性逻辑范围的下界。例如，GL 是否是 $I \Delta_0+\Omega_1$ 的可证性逻辑仍是未决问题——该理论在某种意义上弱于 $I \Delta_0$+EXP：$\Omega_1$ 是断言对一切 $x$ 其幂 $x^{\log(x)}$ 存在的公理。可证性逻辑 GL 相对于 $I \Delta_0+\Omega_1$ 算术可靠，但除 Berarducci 与 Verbrugge（1993）的部分结果——为与 GL 一致的受限句子类提供与 $I \Delta_0+\Omega_1$ 一致的算术实现——之外，问题仍未决。其答案可能系于计算复杂性理论的未决问题。

上述由 De Jongh 等人给出的结果表明，可证性逻辑有一个强特征：对许多不同的算术理论，GL 恰好捕捉这些理论就其自身可证性谓词所说的一切。与此同时这也是一个弱点。例如，命题可证性逻辑无法区分哪些理论可有限公理化、哪些不能。

### 5.2 可解释性逻辑

为了能在模态语言中谈论理论间的重要区分，研究者以多种方式扩充可证性逻辑。略举几例。一种扩充是添加二元模态词 $\interprets$：对给定算术理论 $T$，模态句子 $A \interprets B$ 意为“$T+B$ 可解释于 $T+A$”（Švejdar, 1983）。De Jongh 与 Veltman（1990）考察若干可解释性逻辑的模态语义，De Jongh 与 Visser（1991）证明其中最重要几个的显式不动点性质。Visser 刻画最常见可有限公理化理论的可解释性逻辑；Berarducci 与 Shavrukov 各自独立刻画 PA 的——PA 不可有限公理化。看来确实如此：可有限公理化理论的可解释性逻辑不同于皮亚诺算术的可解释性逻辑（见 Montagna 1987; Visser 1990, 1998; Berarducci 1990, Shavrukov 1988; Joosten and Visser 2000）[^berarducci-1990][^joosten-2000][^montagna-1987][^shavrukov-1988][^visser-1990]。

### 5.3 命题量词

扩充命题可证性逻辑框架的另一种方式是添加命题量词，从而能表达诸如 Goldfarb 原理之类的东西：

$$ \forall p \,\forall q \,\exists r \: \Box((\Box p \vee \Box q) \leftrightarrow \Box r), $$

它说的是：对任意两个句子，存在第三个句子，其可证当且仅当前两句之一可证。这一原理在皮亚诺算术中可证（见例如 Artemov and Beklemishev 1993）[^artemov-1993]。带命题量词的 GL 句子中算术有效的那个集合，最终被证明不可判定（Shavrukov 1997）[^shavrukov-1997]。

### 5.4 Japaridze 的双模与多模可证性逻辑

Japaridze（1988）的双模逻辑 GLB 有两个类 $\Box$ 的可证性算子，记作 $[0]$ 与 $[1]$，其对偶的类 $\Diamond$ 算子分别为 $\langle 0\rangle$ 与 $\langle 1\rangle$。在 Japaridze 的解释中，可把 $[0]$ 看作皮亚诺算术的标准可证性谓词；而 $[1]$ 对应一个更强的可证性谓词，即 **$\omega$-可证性**。

让我们定义理解 GLB 这一意向解释所需的概念。算术理论 $T$ 定义为 **$\omega$-一致的**，当且仅当对所有带自由变元 $x$ 的公式 A：若 $T\vdash \neg\, A(I_n)$ 对所有 $n$ 成立，则 $T \not\vdash \exists x \, A(x)$；这里 $I_n$ 是 $n$ 的数字词，即带 $n$ 个后继算子 $\bs$ 出现的项 $\bs\bs\ldots\bs 0$。皮亚诺算术（PA）是 $\omega$-一致理论最著名的例子（另见哥德尔不完备性定理）。现在令 PA$^+$ 为这样的算术理论：其公理是 PA 的公理，加上所有形如 $\forall x \, \neg \, A(x)$ 的句子——只要对每个 $n$ 都有 PA$\vdash \neg \, A(I_n)$。于是 $\omega$-可证性就是在 PA$^+$ 中的可证性：它是 $\omega$-一致性的对偶。

Japaridze 的双模可证性逻辑 GLB 可由 GL 的公理与规则（见第 2 节）公理化，并分别为 [0] 与 [1] 表述。此外，GLB 还有两条混合公理： $$\tag{Monotonicity} [0] A \rightarrow [1] A $$ $$\tag{\(\Pi^0_1\)-completeness} \langle 0\rangle A \rightarrow [1]\langle 0\rangle A $$ 该逻辑可判定、有合理的 Kripke 语义，且相对于皮亚诺算术既算术可靠又完全（Japaridze 1988, Boolos 1993）[^boolos-1993][^japaridze-1988]。

Japaridze 的 GLB 的一个多模类比名为 GLP，近年受到大量关注。GLP 有无穷多个类 $\Box$ 的可证性算子，记作对每个自然数 $n$ 的盒 $[n]$，其对偶的类 $\Diamond$ 算子为 $\langle n\rangle$。同样，可把 $[0]$ 看作皮亚诺算术的标准可证性谓词，$\langle 1\rangle$ 为 $\omega$-可证性，等等。GLP 的公理化从 GL 的公理与规则出发（见第 2 节），为每个 $[n]$ 分别表述。此外 GLP 有三个混合公理模式，即如 Beklemishev（2010）所表述的： $$ [m] A \rightarrow [n] A, \mbox{ for } m \leq n $$ $$ \langle k\rangle A \rightarrow [n]\langle k\rangle A, \mbox{ for } k \lt n $$ $$ [m] A \rightarrow [n][m] A, \mbox{ for } m \leq n $$

GLP 被赋予一个 Kripke 语义并相对于它完全，也被证明相对于皮亚诺算术算术完全（见 Beklemishev 2010a, 2011a）[^beklemishev-2010a]。与 GL 一样，GLP 的判定问题是 PSPACE-完全的（Shapirovsky 2008）[^shapirovsky-2008]，而其闭片段多项式时间可判定（Pakhomov 2014）[^pakhomov-2014]。

过去三十年，关于强可证性谓词的多模逻辑 GLP，已有若干结果被证明。以下是一些特别多产的议题：

* GLP 的闭片段（见 Ignatiev 1993; Beklemishev, Joosten and Vervoort 2005）[^ignatiev-1993]；
* GLP 与证明论序数（Beklemishev 2004）[^beklemishev-2004]；
* GLP 的邻域语义（Shamkanov 2020）[^shamkanov-2020][^shamkanov-2020-2]；
* GLP 的插值定理（见 Beklemishev 2010b, Shamkanov 2011）[^shamkanov-2011][^beklemishev-2010b]；
* 拓扑语义与集合论的关系，其中包括特定的大基数公理与平稳反射（见 Beklemishev 2011b; Beklemishev and Gabelaia 2013, 2014; Fernández-Duque 2014; Aguilera and Fernández-Duque 2017）[^beklemishev-2011b][^beklemishev-2013][^fernández-duque-2014][^aguilera-2017][^fernández-duque-2014-2]。

### 5.5 谓词可证性逻辑

最后，当然可以研究谓词可证性逻辑。其语言是无函数符号的谓词逻辑语言，加上算子 $\Box$。这里的情形比命题可证性逻辑复杂得多。首先，GL 的直接量化版本不具有不动点性质、相对于任何 Kripke 框架类不完全，且相对于皮亚诺算术算术不完全（Montagna, 1984；晚近推广见 Rybakov 2023）[^rybakov-2023]。于是问题来了：是否存在某个公理化良好的谓词可证性逻辑，足以恰好证明可证性的有效原理？遗憾的是，答案响亮地是否定的。Vardanyan（1986）基于 Artemov（1985a）的思想证明：谓词可证性逻辑中一切实现都在 PA 中可证的句子，其集合不仅不是递归可枚举的；它更是 $\Pi^0_2$-完全的，因此没有任何合理的公理化。Visser 与 De Jonge（2006）通过证明一个推广表明无法逃脱 Vardanyan 定理：对广泛的算术理论 $T$，谓词可证性逻辑中一切实现在 $T$ 中可证的句子之集同样是 $\Pi^0_2$-完全的。不过晚近，Borges 与 Joosten（2020, 2022）证明：基于严格正面语言的谓词可证性逻辑的一个片段——含命题联结词 $\wedge$、模态算子 $\Diamond$ 与量词 $\forall$——算术完全且仍可判定。

### 5.6 其他推广

上文讨论未及可证性逻辑及其扩充研究中许多其他重要线索。有兴趣的读者可参看以下领域：

* 直觉主义算术的可证性逻辑（见 Troelstra 1973; Visser 1982, 1999, 2002, 2008; Iemhoff 2000, 2001, 2003; Ardeshir and Mojtahedi 2018; Litak and Visser 2018, forthcoming; Mojtahedi 2022 [Other Internet Resources]; Visser and Zoethout 2021; van der Giessen and Iemhoff 2021; van der Giessen 2023; Shillito 2023）[^shillito-2023][^ardeshir-2018][^giessen-2023][^giessen-2021][^iemhoff-2000][^litak-2018][^troelstra-1973][^visser-1982]；
* 可证性逻辑的分类（见 Visser 1980, Artemov 1985b, Beklemishev 1989, Beklemishev et al. 1999）[^artemov-1985b][^beklemishev-1989][^beklemishev-1999][^beklemishev-1999-2][^visser-1980]；
* Rosser 序与证明加速（见 Guaspari and Solovay 1979, Švejdar 1983, Montagna 1992）[^guaspari-1979][^montagna-1992]；
* 若干种双模可证性逻辑，带不同理论的可证性算子（见 Carlson 1986; Smoryński 1985; Beklemishev 1994, 1996; Visser 1995）[^smoryński-1985][^beklemishev-1994][^carlson-1986][^visser-1995]；
* 以标准可证性与外部枚举 PA 的异常可证性谓词相结合的可证性逻辑，如 Feferman 与 Parikh 的可证性谓词及慢可证性谓词（见 Feferman 1960; Parikh 1971; Montagna 1978; Visser 1989; Carbone and Montagna 1990; Shavrukov 1994; Lindström 1994, 2006; Henk and Pakhomov 2016 (Other Internet Resources)）；
* 用可证性逻辑与可解释性逻辑分析哥德尔第二不完备性定理（Visser 2016; 2020）[^visser-2016]；
* 显式证明的逻辑（见 Artemov 1994, 2001; Artemov and Montagna 1994; Yavorskaya 2001; Artemov and Iemhoff 2007; Kuznets and Studer 2019）[^artemov-1994][^artemov-2007][^artemov-1994-2][^kuznets-2019][^yavorskaya-2001]；
* 可证性逻辑与证成逻辑之间的对应（见 Artemov and Nogina 2005; Shamkanov 2016 (Other Internet Resources); Fitting 2020）；
* 基于相关逻辑 R 的相关可证性逻辑（见 Mares 2000）[^mares-2000]；
* 可证性逻辑在证明论中的应用（见 Beklemishev 1999, 2003, 2004, 2005, 2006）[^beklemishev-1999][^beklemishev-1999-2]；
* 与可证性逻辑 GL 密切相关的命题模态逻辑的证明论，即 Grzegorczyk 逻辑（Grz）与弱 Grzegorczyk 逻辑（wGrz）（见 Litak 2007; Maksimova 2014; Goré and Ramanayake 2014; Dyckhoff and Negri 2016; Savateev and Shamkanov 2019, 2021）[^dyckhoff-2016][^goré-2014][^litak-2007][^maksimova-2014][^savateev-2019]；
* 正可证性逻辑与反射演算（见 Beklemishev 2012, 2014, 2018a, 2018b; Dashkov 2012）[^beklemishev-2012][^dashkov-2012]；
* 多模可证性逻辑 GLP 的推广，即带超穷多个模态词的可证性逻辑（见 Beklemishev et al. 2014; Fernández-Duque and Joosten 2013a, 2013b, 2014, 2018; Joosten 2021; Beklemishev and Pakhomov 2022）[^beklemishev-2014][^beklemishev-2014-2][^beklemishev-2014-3][^beklemishev-2022][^fernández-duque-2013a][^joosten-2021]；
* 可证性逻辑与 $\mu$-演算的关系（见 van Benthem 2006, Visser 2005, Alberucci and Facchini 2009）[^alberucci-2009][^benthem-2006][^visser-2005]；以及
* 可证性代数——也称可对角化代数或 Magari 代数（见 Magari 1975a, 1975b; Montagna 1979, 1980a, 1980b; Bernardi and D’Aquino 1988; Shavrukov 1993a, 1993b, 1997; Zambella 1994；关于其初等理论的晚近结果，见 Pakhomov 2012, 2014a (Other Internet Resources), 2015）。

对于想在可证性逻辑及其推广领域有所贡献的读者，Beklemishev 与 Visser（2006）拟就了一份注解版的开问题清单。

## 6 哲学意义

尽管命题可证性逻辑是一个带某种“必然性”算子的模态逻辑，它顶住了蒯因（Quine，1976）对模态概念不可理解的争议性批评——这至少是因为它有清晰无歧义的算术解释。例如，与许多其他模态逻辑不同，带嵌套模态词的公式如 $\Box\Diamond p \rightarrow \Box\bot$ 并无问题，也不存在关于哪些应为重言式的争论。事实上，可证性逻辑体现了蒯因（1953）为模态的语法处理设定的一切期望。

蒯因的主要矛头指向模态谓词逻辑，尤其是构造在量词辖域内含模态算子的句子（“量化入内”）。然而在谓词可证性逻辑中，量词取值于自然数，无论 *de dicto* 还是 *de re* 模态词都有直截了当的解释——与其他模态逻辑的情形相反（见 *de dicto*／*de re* 区分之注）。例如，形如

$$ \forall x\, \Box\, \exists y \,(y=x) $$

的公式毫无问题。若把数 $n$ 赋给 $x$，则 $\Box \,\exists y\,(y = x)$ 就该赋值为真，当且仅当句子 $\exists y\,(y=I_n)$ 在皮亚诺算术中可证；这里 $I_n$ 是 $n$ 的数字词，即带 $n$ 个后继算子 $\bs$ 出现的项 $\bs\bs\ldots\bs 0$。这一句子对所有 $n$ 在自然数标准模型中为真，而 $\forall x \,\Box\, \exists y \,(y = x)$ 甚至在皮亚诺算术中可证。

顺带一提，Barcan 公式

$$ \forall x \,\Box\, A(x) \rightarrow \Box\, \forall x\, A(x) $$

对整数并不成立，更谈不上在皮亚诺算术中可证（例如取 $A(x)$ 为“$x$ 不编码对 $\bot$ 的证明”这一公式）。而它的逆

$$ \Box\, \forall x \, A(x) \rightarrow \forall x \, \Box\, A(x) $$

则对任意公式 $A$ 都在皮亚诺算术中可证。

可证性逻辑的原理与其他模态逻辑——哪怕貌似目的相近者——大不相同。例如，可证性逻辑捕捉形式算术理论中的可证性，而认知逻辑力图描述知识——后者可视为一种非形式可证性。在认知逻辑的许多版本中，最重要的原理之一是真公理（5）：

$$ \mbox{S5} \vdash \Box A \rightarrow A, (\text{if one knows } A, \text{ then } A \text{ is true}). $$

类似的原理显然对 GL 不成立：毕竟，

$$ \text{if } \GL \vdash \Box A \rightarrow A, \text{ then } \GL \vdash A. $$

因此，比较两种概念的强弱或把它们合并进一个模态系统，看来都是误入歧途。

自 1940 年代以来，数学哲学家对非形式可证性或 **绝对可证性** 的概念抱有浓厚兴趣（Gödel 1946, Kreisel 1967）[^gödel-1946][^kreisel-1967]，包括关于其恰当定义的争论（良好讨论见 Leach-Krouse 2013; Kennedy 2014; Crocco 2019）[^crocco-2019][^kennedy-2014][^leach-krouse-2013]。Williamson（2016）给出如下定义：“一个数学假设是 **绝对可证的**，当且仅当它原则上能经由正常的数学过程被知道。”无论如何，清楚的是：绝对可证性概念与给定形式系统中的 **形式可证性** 概念非常不同——后者是本文其余部分关于可证性逻辑的核心概念。

与绝对可证陈述相关的概念是 **绝对不可判定的陈述**：即那些 $A$ 与 $\neg A$ 都不绝对可证的陈述 $A$。一个有趣的问题是哥德尔析取式是否成立：是否要么“心灵无法被机械化”，要么“存在绝对不可判定的陈述”？对这一问题的精彩处理见（Koellner 2016, Leach-Krouse 2016, Williamson 2016）[^koellner-2016][^leach-krouse-2016][^williamson-2016]。

关于哥德尔不完备性定理之后果的讨论，有时围绕可证性概念产生混淆，引出人类能在“知道”定理一事上胜过形式系统的主张；对这些主张的良好批判性讨论见（Davis 1990, 1993; Franzén 1995; Lindström 2001）[^davis-1990][^lindström-2001]。

总而言之，形式可证性是一个精确定义的概念——比真与知识精确得多。因此，可证性辖域内的自指不会导致说谎者式的语义悖论。相反，它引出关于数学的一些最重要结果，如哥德尔不完备性定理。

## 脚注

[^note-1]: 下文我们将给出 GL $\vdash \Box\Diamond A \rightarrow \Box B$ 的更详细证明概述——这是一个简单却令人惊讶的定理，由 Nils Kurbis 向我们建议。先收集一些素材。注意在模态逻辑 K（当然也在 GL）中，对每个公式 $ C $，两个公式 $ C \rightarrow \bot$ 与 $\neg C$ 逻辑等价，可以互相替换。对两个公式 $\Diamond C$ 与 $\neg\Box\neg C$ 亦然。此外，由概括规则、分配公理与分离规则，对一切公式 $C, D$ 我们有如下导出规则：若 GL $\vdash C \rightarrow D$，则 GL $\vdash \Box C \rightarrow \Box D$。以下就是应许的证明概述。

1. GL $\vdash \bot \rightarrow \neg A$（命题逻辑重言式）
2. GL $\vdash \Box \bot \rightarrow \Box\neg A$（由第 1 行经上述导出规则）
3. GL $\vdash \bot \rightarrow B$（命题逻辑重言式）
4. GL $\vdash \Box\bot \rightarrow \Box B$（由第 3 行经上述导出规则）
5. GL $\vdash \Box(\Box \bot \rightarrow \bot) \rightarrow \Box\bot $（公理 GL）
6. GL $\vdash \Box(\Box \bot \rightarrow \bot) \rightarrow \Box B $（由第 4、5 行经假言三段论）
7. GL $\vdash \Diamond A \rightarrow (\Box \bot \rightarrow \bot) $（由第 2 行经逆否与上述等价）
8. GL $\vdash \Box\Diamond A \rightarrow \Box(\Box \bot \rightarrow \bot) $（由第 7 行经上述导出规则）
9. GL $\vdash \Box\Diamond A \rightarrow \Box B $（由第 6、8 行经假言三段论）。

注意从语义上看，容易看出公式 $\Box\Diamond A \rightarrow \Box B $ 在传递逆良基框架上有效（见第 3 节）。毕竟，形如 $\Box\Diamond A$ 的公式只能在传递逆良基框架的端点处成立；而在此类框架的所有端点处，我们也有 $\Box\bot$，从而对每个公式 $B$ 都有 $\Box B$。

[^note-2]: 事实上，几乎同一个反例对直觉主义可证性逻辑同样有效，甚至对不带 $\Diamond$ 的版本亦然——该结果由 Ian Shillito（2023，定理 13.2.1）证明。按 Rosalie Iemhoff 的建议，只需将上例中的每个 $\Diamond$ 换成 $\neg\Box\neg$。

[^note-3]: Holliday 与 Litak（2019）强化了这一结果：GLB 不仅相对 Kripke 框架不完全，甚至相对于 $\Diamond$ 算子*完全可加*的布尔代数也不完全——所谓完全可加，是说对任意元素集 $X$，只要 $\bigvee X$ 存在，$\bigvee\{\Diamond x \mid x \in X \}$ 便也存在，且 $\Diamond\bigvee X = \bigvee\{\Diamond x \mid x \in X \}$。这一结果有一个漂亮的侧面：双模可证性逻辑 GLB 是第一个在完全可加布尔代数上表现出这种不完全性的自然出现的模态逻辑。还应注意，Van Benthem（1979）最初用来证明存在模态不完全逻辑的那个逻辑，同样是可证性逻辑的一个（略显人工的）变体——即 $K$ 再加一条额外公理 $\Box\Diamond\top\rightarrow \Box(\Box(\Box p \rightarrow p) \rightarrow p)$，它是 GL 的一个弱化。

## References（引用注释）

**以下文献从原文照录，不作翻译；中国文献译为中文。**

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

### General references on provability logic

### History

### Cut-elimination for provability logic

### The fixed point theorem

### Possible worlds semantics and topological semantics

### Provability and Peano Arithmetic

### The scope of provability logic: boundaries

### Interpretability logic

### Propositional quantifiers

### Japaridze’s bimodal and polymodal provability logics

### Predicate provability logic

### Other generalizations

### Philosophical significance

[^artemov-2006]: Artemov, S.N., 2006, “Modal Logic in Mathematics,” in P. Blackburn, et al. (eds.), *Handbook of Modal Logic*, Amsterdam: Elsevier, pp. 927–970.
[^artemov-2004]: Artemov, S.N. and L.D. Beklemishev, 2004, “Provability Logic,” in *Handbook of Philosophical Logic*, Second Edition, D. Gabbay and F. Guenthner, eds., Volume 13, Dordrecht: Kluwer, pp. 229–403.
[^boolos-1979]: Boolos, G., 1979, *The Unprovability of Consistency: An Essay in Modal Logic*, Cambridge: Cambridge University Press.
[^boolos-1993]: –––, 1993, *The Logic of Provability*, New York and Cambridge: Cambridge University Press.
[^jongh-1998]: de Jongh, D.H.J. and G. Japaridze, 1998, “The Logic of Provability,” in *Handbook of Proof Theory*, Buss, S.R. (ed.), Amsterdam: North-Holland, pp. 475-546.
[^lindström-1996]: Lindström, P., 1996, “Provability Logic—A Short Introduction,” *Theoria*, 52(1–2): 19–61.
[^segerberg-1971]: Segerberg, K., 1971, *An Essay in Classical Modal Logic*, Uppsala: Filosofiska Föreningen och Filosofiska Institutionen vid Uppsala Universitet.
[^segerberg-2000]: Švejdar, V., 2000, “On Provability Logic,” *Nordic Journal of Philosophy*, 4: 95–116.
[^smoryński-1984]: Smoryński, C., 1984, “Modal Logic and Self-Reference,” in D.M. Gabbay and F. Guenthner (eds.), *Handbook of Philosophical Logic* (Volume II: Extensions of Classical Logic), Dordrecht: Springer, pp. 441–495.
[^smoryński-1985]: Smoryński, C., 1985, *Self-Reference and Modal Logic*, New York: Springer-Verlag.
[^verbrugge-1996]: Verbrugge, R. 1996, “Provability” in *The Encyclopedia of Philosophy* (Supplement), D.M. Borchert (ed.), New York: Simon and Schuster MacMillan, pp. 476–478.
[^visser-1998]: Visser, A., 1998, “Provability Logic,” in *Routledge Encyclopedia of Philosophy*, W. Craig (ed.), London: Routledge, pp. 793–797.
[^benthem-1978]: van Benthem, J.F.A.K., 1978, “Four Paradoxes,” *Journal of Philosophical Logic*, 7(1): 49–72.
[^boolos-1991]: Boolos, G. and G. Sambin, 1991, “Provability: The Emergence of a Mathematical Modality,” *Studia Logica*, 50(1): 1–23.
[^gödel-1933]: Gödel, K., 1933, “Eine Interpretation des intuitionistischen Aussagenkalküls,” *Ergebnisse eines Mathematischen Kolloquiums*, 4: 39–40; translation “An Interpretation of the Intuitionistic Propositional Calculus,” in K. Gödel, *Collected Works*, S. Feferman et al. (eds.), Oxford and New York: Oxford University Press, Volume 1, 1986, pp. 300–302.
[^gödel-1931]: –––, 1931, “Über Formal Unentscheidbare Sätze der Principia Mathematica und Verwandter Systeme I,” *Monatshefte für Mathematik und Physik*, 38: 173–198.
[^halbach-2014]: Halbach, V., and A. Visser, 2014, “The Henkin Sentence,” in M. Mazano, I. Sain, and E. Alonso (eds.), *The Life and Work of Leon Henkin: Essays on His Contributions*, Dordrecht: Springer International Publishing, pp. 249–263.
[^henkin-1952]: Henkin, L., 1952, “A Problem Concerning Provability,” *Journal of Symbolic Logic*, 17: 160.
[^henkin-1954]: –––, 1954, “Review of G. Kreisel: On a Problem of Leon Henkin’s,” *Journal of Symbolic Logic*, 19(3): 219–220.
[^hilbert-1939]: Hilbert, D. and P. Bernays, 1939, *Grundlagen der Mathematik*, volume 2, Berlin/Heidelberg/New York: Springer-Verlag.
[^jongh-nd]: de Jongh, D.H.J., forthcoming, “Notes on my Scientific Life,” in N. Bezhanishvili, R. Iemhoff and F. Yang (eds.), *Dick de Jongh on Intuitionistic and Provability Logic*, Cham: Springer.
[^kreisel-1953]: Kreisel, G., 1953, “On a Problem of Leon Henkin’s,” *Indagationes Mathematicae*, 15: 405–406.
[^lewis-1912]: Lewis, C.I., 1912, “Implication and the Algebra of Logic,” *Mind*, 21: 522–531.
[^löb-1955]: Löb, M.H., 1955, “Solution of a Problem of Leon Henkin,” *Journal of Symbolic Logic*, 20: 115–118.
[^macintyre-1973]: Macintyre, A.J. and H. Simmons, 1973, “Gödel’s Diagonalization Technique and Related Properties of Theories,” *Colloquium Mathematicum*, 28: 165–180.
[^magari-1975a]: Magari, R., 1975a, “The Diagonalizable Algebras,” *Bollettino della Unione Mathematica Italiana*, 12: 117–125.
[^magari-1975b]: –––, 1975b, “Representation and Duality Theory for Diagonalizable Algebras,” *Studia Logica*, 34(4): 305–313.
[^smiley-1963]: Smiley, T.J., 1963, “The Logical Basis of Ethics,” *Acta Philosophica Fennica*, 16: 237–246.
[^smoryński-1991]: Smoryński, C., 1991, “The Development of Self-reference: Löb’s Theorem,” in T. Drucker (ed.), *Perspectives on the History of Mathematical Logic*, Basel: Birkhäuser, pp. 110–133.
[^avron-1984]: Avron, A., 1984, “On Modal Systems Having Arithmetical Interpretations,” *The Journal of Symbolic Logic*, 49(3): 935–942.
[^bílková-2016]: Bílková, M., 2016, “Uniform Interpolation in Provability Logics,” in J. van Eijck, R. Iemhoff, and J.J. Joosten (eds.), *Liber Amicorum Alberti: A Tribute to Albert Visser*, London: College Publications, pp. 57–90.
[^goré-2008]: Goré, R. and R. Ramanayake, 2008, “Valentini’s Cut-Elimination for Provability Logic Resolved,” in *Advances in Modal Logic* (Volume 7), C. Areces and R. Goldblatt (eds.), London: College Publications, pp. 67–86.
[^goré-2012]: Goré, R. and R. Ramanayake, 2012, “Valentini’s Cut-Elimination for Provability Logic Resolved,” *Review of Symbolic Logic*, 5(2): 212–238.
[^goré-2021]: Goré, R., Ramanayake, R., and Shillito, I., 2021, “Cut-Elimination for Provability Logic by Terminating Proof-Search: Formalised and Deconstructed Using Coq,” in *Automated Reasoning with Analytic Tableaux and Related Methods: 30th International Conference, TABLEAUX 2021*, Cham: Springer International Publishing, pp. 299–313.
[^maksimova-1989a]: Maksimova, L.L., 1989a, “A Continuum of Normal Extensions of Modal Provability Logic with the Interpolation Property,” *Sibirskii Matematicheskii Zhurnal*, 30(6): 122–131.
[^maksimova-1989b]: Maksimova, L.L., 1989b, “Definability Theorems in Normal Extensions of the Probability Logic,” *Studia Logica*, 48(4): 495–507.
[^negri-2005]: Negri, S., 2005, “Proof Analysis in Modal Logic,” *Journal of Philosophical Logic*, 50: 507–544.
[^negri-2014]: Negri, S., 2014, “Proofs and Countermodels in Non-classical Logics,” *Logica Universalis*, 8(1): 25–60.
[^poggiolesi-2009]: Poggiolesi, F., 2009, “A Purely Syntactic and Cut-free Sequent Calculus for the Modal Logic of Provability,” *The Review of Symbolic Logic*, 2(4): 593–611.
[^rautenberg-1983]: Rautenberg, W., 1983, “Modal Tableau Calculi and Interpolation,” *Journal of Philosophical Logic*, 12(4): 403–423.
[^sambin-1982]: Sambin, G., and S. Valentini, 1982, “The Modal Logic of Provability. The Sequential Approach,” *Journal of Philosophical Logic*, 11(3): 311–342.
[^shamkanov-2011]: Shamkanov, D.S., 2011, “Interpolation Properties for Provability Logics GL and GLP,” *Proceedings of the Steklov Institute of Mathematics*, 274(1): 303–316.
[^shamkanov-2014]: –––, 2014, “Circular Proofs for the Gödel-Löb Provability Logic,” *Mathematical Notes*, 96(4): 575–585.
[^shamkanov-2020]: –––, 2020, “Non-well-founded Derivations in the Gödel-Löb Provability Logic,” *Review of Symbolic Logic*, 13(4): 776–796.
[^smoryński-1978]: Smoryński, C., 1978, “Beth’s Theorem and Self-referential Sentences,” *Studies in Logic and the Foundations of Mathematics*, 96: 253–261.
[^valentini-1983]: Valentini, S., 1983, “The Modal Logic of Provability: Cut-Elimination,” *Journal of Philosophical Logic*, 12: 471–476.
[^benthem-nd]: van Benthem, J., forthcoming, “An Abstract Look at the Fixed-Point Theorem for Provability Logic,” in N. Bezhanishvili, R. Iemhoff and F. Yang (eds.), *Dick de Jongh on Intuitionistic and Provability Logic*, Cham: Springer.
[^jongh-1988]: de Jongh, D.H.J., and F. Montagna, 1988, “Provable Fixed Points,” *Zeitschrift fur mathematische Logik und Grundlagen der Mathematik*, 34(3): 229–250.
[^lindström-2006]: Lindström, P., 2006, “Note on Some Fixed Point Constructions in Provability Logic,” *Journal of Philosophical Logic*, 35(3): 225–230.
[^reidhaar-olson-1990]: Reidhaar-Olson, L., 1990, “A New Proof of the Fixed-point Theorem of Provability Logic,” *Notre Dame Journal of Formal Logic*, 31(1): 37–43.
[^sambin-1976]: Sambin, G., 1976, “An Effective Fixed Point Theorem in Intuitionistic Diagonalizable Algebras (The Algebraization of the Theories Which Express Theor, IX),” *Studia Logica* 35: 345–361.
[^sambin-1982-2]: Sambin, G., and S. Valentini, 1982, “The Modal Logic of Provability. The Sequential Approach,” *Journal of Philosophical Logic*, 11(3): 311–342.
[^abashidze-1985]: Abashidze, M., 1985, “Ordinal Completeness of the Gödel-Löb Modal System,” (in Russian) in *Intensional Logics and the Logical Structure of Theories*, Tbilisi: Metsniereba, pp. 49–73.
[^aiello-2007]: Aiello, M., I. Pratt-Hartmann and J. van Benthem (eds.), 2007, *Handbook of Spatial Logics*, Berlin: Springer-Verlag.
[^beklemishev-2009]: Beklemishev, L.D. 2009, “Ordinal Completeness of Bimodal Provability Logic GLB,” In *International Tbilisi Symposium on Logic, Language, and Computation*, Berlin: Springer-Verlag, pp. 1–15.
[^beklemishev-2009-2]: Beklemishev, L.D., G. Bezhanishvili, and T. Icard, 2009, “On Topological Models of GLP,” in R. Schindler (ed.), *Ways of Proof Theory* (Ontos Mathematical Logic: Volume 2), Frankfurt: Ontos Verlag, pp. 133–153.
[^benthem-1979]: van Benthem, J.F.A.K., 1979, “Syntactic Aspects of Modal Incompleteness Theorems,” *Theoria*, 45(2): 63–77.
[^blass-1990]: Blass, A., 1990, “Infinitary Combinatorics and Modal Logic,” *Journal of Symbolic Logic*, 55(2): 761–778.
[^esakia-1981]: Esakia, L., 1981, “Diagonal Constructions, Löb’s Formula and Cantor’s Scattered Spaces,” (in Russian), in *Studies in Logic and Semantics*, Z. Mikeladze (ed.), Tbilisi: Metsniereba, pp. 128–143.
[^esakia-2003]: –––, 2003, “Intuitionistic Logic and Modality via Topology,” *Annals of Pure and Applied Logic*, 127: 155–170.
[^goré-2009]: Goré, R., 2009, “Machine Checking Proof Theory: An Application of Logic to Logic,” In *ICLA ’09: Proceedings of the 3rd Indian Conference on Logic and Its Applications*, Berlin: Springer-Verlag, pp. 23–35.
[^hakli-2012]: Hakli, R. and S. Negri, 2012, “Does the Deduction Theorem Fail for Modal Logic?,” *Synthese* 187(3): 849–867.
[^holliday-2019]: Holliday, W.H. and Litak, T., 2019, “Complete Additivity and Modal Incompleteness,” *The Review of Symbolic Logic*, 12(3): 487–535.
[^icard-2011]: Icard, T.F. III, 2011, “A Topological Study of the Closed Fragment of GLP,” *Journal of Logic and Computation*, 21(4): 683–696; first published online 2009, doi:10.1093/logcom/exp043
[^japaridze-1986]: Japaridze, G.K., 1986, *The Modal Logical Means of Investigation of Provability*, Thesis in Philosophy (in Russian), Moscow.
[^mckinsey-1944]: McKinsey, J.C.C. and A. Tarski, 1944, “The Algebra of Topology,” *Annals of Mathematics*, 45: 141–191.
[^shillito-2023]: Shillito, I., 2023, *New Foundations for the Proof Theory of Bi-Intuitionistic and Provability Logics Mechanized in Coq*, Ph.D. Thesis, Canberra: The Australian National University.
[^verbrugge-2021]: Verbrugge, R., 2021, “Zero-One Laws for Provability Logic: Axiomatizing Validity in Almost All Models and Almost All Frames,” in L. Libkin (ed.), *Proceedings of the 36th Annual ACM/IEEE Symposium on Logic in Computer Science (LICS)*, Rome: IEEE Press.
[^davis-1958]: Davis, M., 1958, *Computability and Unsolvability*, New York, McGraw-Hill; reprinted with an additional appendix, New York, Dover Publications 1983.
[^feferman-1960]: Feferman, S., 1960, “Arithmetization of Metamathematics in a General Setting,” *Fundamenta Mathematicae*, 49(1): 35–92.
[^hájek-1993]: Hájek, P. and P. Pudlák, 1993, *Metamathematics of First-Order Arithmetic*, Berlin: Springer-Verlag.
[^solovay-1976]: Solovay, R.M., 1976, “Provability Interpretations of Modal Logic,” *Israel Journal of Mathematics*, 25: 287–304.
[^berarducci-1993]: Berarducci, A. and R. Verbrugge, 1993, “On the Provability Logic of Bounded Arithmetic,” *Annals of Pure and Applied Logic*, 61: 75–93.
[^buss-1986]: Buss, S.R., 1986, *Bounded Arithmetic*, Naples: Bibliopolis.
[^jongh-1991]: de Jongh, D.H.J., M. Jumelet and F. Montagna, 1991, “On the Proof of Solovay’s Theorem,” *Studia Logica*, 50(1): 51–70.
[^parikh-1971]: Parikh, R., 1971, “Existence and Feasibility in Arithmetic“, *The Journal of Symbolic Logic*, 36(3): 494–508.
[^areces-2001]: Areces, C., Hoogland, E. and de Jongh, D.H.J., 2001, “Interpolation, Definability and Fixed-points in Interpretability Logics“, in M. Zakharyaschev, K. Segerberg, M. de Rijke and H. Wansing (eds.), *Advances in Modal Logic* (Volume 2), Stanford: CSLI Publications, pp. 35–58.
[^berarducci-1990]: Berarducci, A., 1990, “The Interpretability Logic of Peano Arithmetic,” *Journal of Symbolic Logic*, 55: 1059–1089.
[^bílková-2009]: Bílková, M., de Jongh, D. and Joosten, J.J., 2009, “Interpretability in PRA,” *Annals of Pure and Applied Logic*, 161(2): 128–138.
[^jongh-1990]: de Jongh, D.H.J., and F. Veltman, 1990, “Provability Logics for Relative Interpretability,” in P.P. Petkov (ed.), *Mathematical Logic: Proceedings of the Heyting 1988 Summer School in Varna, Bulgaria*, Boston: Plenum Press, pp. 31–42.
[^jongh-1991-2]: de Jongh, D.H.J., and A. Visser, 1991, “Explicit Fixed Points in Interpretability Logic,” *Studia Logica*, 50(1): 39–49.
[^joosten-2000]: Joosten, J.J., and Visser, A., 2000, “The Interpretability Logic of All Reasonable Arithmetical Theories,” *Erkenntnis*, 53(1-2): 3–26.
[^joosten-nd]: Joosten, J.J., Mas Rovira, J., Mikec, L., and Vuković, M., forthcoming, “An Overview of Verbrugge Semantics, a.k.a. Generalised Veltman Semantics,” in N. Bezhanishvili, R. Iemhoff and F. Yang (eds.), *Dick de Jongh on Intuitionistic and Provability Logic*, Cham: Springer.
[^mikec-2020]: Mikec, L. and Vuković, M., 2020, “Interpretability Logics and Generalised Veltman Semantics,” *The Journal of Symbolic Logic*, 85(2): 749–772.
[^montagna-1987]: Montagna, F., 1987, “Provability in Finite Subtheories of PA,” *Journal of Symbolic Logic*, 52(2): 494–511.
[^shavrukov-1988]: Shavrukov, V.Yu., 1988, “The Logic of Relative Interpretability over Peano Arithmetic,” Technical Report No. 5, Moscow: Steklov Mathematical Institute (in Russian).
[^shavrukov-1983]: Švejdar, V., 1983, “Modal Analysis of Generalized Rosser Sentences,” *Journal of Symbolic Logic*, 48: 986–999.
[^visser-1990]: Visser, A., 1990, “Interpretability Logic,” in P.P. Petkov (ed.), *Mathematical Logic: Proceedings of the Heyting 1988 Summer School in Varna, Bulgaria*, Boston: Plenum Press, pp. 175–209.
[^visser-1998-2]: –––, 1998, “An Overview of Interpretability Logic,” in M. Kracht et al. (eds.), *Advances in Modal Logic* (Volume 1), Stanford: CSLI Publications, pp. 307–359.
[^artemov-1993]: Artemov, S.N. and L.D. Beklemishev, 1993, “On Propositional Quantifiers in Provability Logic,” *Notre Dame Journal of Formal Logic*, 34: 401–419.
[^shavrukov-1997]: Shavrukov, V.Yu., 1997, “Undecidability in Diagonalizable Algebras,” *Journal of Symbolic Logic*, 62: 79–116.
[^beklemishev-2004]: Beklemishev, L.D., 2004, “Provability Algebras and Proof-Theoretic Ordinals, I,” *Annals of Pure and Applied Logic*, 128: 103–123.
[^beklemishev-2010a]: –––, 2010a, “Kripke Semantics for Provability Logic GLP,” *Annals of Pure and Applied Logic*, 161(6): 756–774.
[^beklemishev-2010b]: –––, 2010b, “On the Craig Interpolation and the Fixed Point Properties of GLP,” in S. Feferman et al. (eds.), *Proofs, Categories and Computations* (Tributes, 13), London: College Publications, pp. 49–60.
[^beklemishev-2011a]: –––, 2011a, “A Simplified Proof of Arithmetical Completeness Theorem for Provability Logic GLP,” *Proceedings Steklov Institute of Mathematics*, 274(1): 25–33.
[^beklemishev-2011b]: –––, 2011b, “Ordinal Completeness of Bimodal Provability Logic GLB,” in N. Bezhanishvili et al. (eds.), *Logic, Language, and Computation, 8th International Tbilisi Symposium TbiLLC 2009* (Lecture Notes in Computer Science: Volume 6618), Heidelberg: Springer, pp. 1–15.
[^beklemishev-2013]: Beklemishev, L.D., and D. Gabelaia, 2013, “Topological Completeness of the Provability Logic GLP,” *Annals of Pure and Applied Logic*, 164(12): 1201–1223.
[^beklemishev-2014]: –––, 2014, “Topological Interpretations of Provability Logic,“ in G. Bezhanishvili (ed.), *Leo Esakia on Duality in Modal and Intuitionistic Logics* (Outstanding Contributions to Logic: Volume 4), Heidelberg: Springer, pp. 257–290.
[^beklemishev-2005]: Beklemishev, L.D., J. Joosten and M. Vervoort, 2005, “A Finitary Treatment of the Closed Fragment of Japaridze’s Provability Logic,” *Journal of Logic and Computation*, 15(4): 447–463.
[^fernández-duque-2014]: Fernández-Duque, D. and J.J. Joosten, 2014, “Well-orders on the Transfinite Japaridze Algebra,” *Logic Journal of the IGPL*, 22 (6): 933–963.
[^fernández-duque-2018]: Fernández-Duque, D. and Joosten, J.J., 2018, “The Omega-Rule Interpretation of Transfinite Provability Logic,” *Annals of Pure and Applied Logic*, 169(4): 333–371.
[^ignatiev-1993]: Ignatiev, K.N., 1993, “On Strong Provability Predicates and the Associated Modal Logics,” *Journal of Symbolic Logic*, 58: 249–290.
[^japaridze-1988]: Japaridze, G., 1988, “The Polymodal Provability Logic,” In *Intensional Logics and the Logical Structure of Theories: Material from the Fourth Soviet-Finnish Symposium on Logic*, Telavi, pp. 16–48.
[^pakhomov-2014]: Pakhomov, F.N., 2014, “On the Complexity of the Closed Fragment of Japaridze’s Provability Logic,” *Archive for Mathematical Logic*, 53(7-8): 949–967.
[^shamkanov-2020-2]: Shamkanov, D., 2020, “Global Neighbourhood Completeness of the Provability Logic GLP,” in N. Olivetti, R. Verbrugge, S. Negri, and G. Sandu (eds.), *Proceedings Advances in Modal Logic* (Volume 13), London: College Publications, pp. 581–595.
[^artemov-1985a]: Artemov, S.N., 1985a, “Nonarithmeticity of Truth Predicate Logics of Provability,” *Doklady Akademii Nauk SSSR*, 284: 270–271 (in Russian); English translation in *Soviet Mathematics Doklady*, 32: 403–405.
[^borges-2020]: Borges, A.A. and Joosten, J.J., 2020, “Quantified Reflection Calculus with One Modality,” in N. Olivetti, R. Verbrugge, S. Negri, and G. Sandu (eds.), *Proceedings Advances in Modal Logic* (Volume 13), London: College Publications, pp. 13–32.
[^borges-2022]: –––, 2022, “An Escape from Vardanyan’s Theorem,” *The Journal of Symbolic Logic*, first online 13 May 2022. doi:10.1017/jsl.2022.38
[^borges-2022-2]: Borges, A.A., 2022, “Towards a Coq Formalization of a Quantified Modal Logic,” in C. Benzmüller and J. Otten (eds.), *Proceedings of the 4th Workshop on Automated Reasoning in Quantified Non-Classical Logics (ARQNL 2022)*, CEUR Workshop Proceedings, pp. 13–27.
[^mcgee-1987]: McGee, V. and G. Boolos, 1987, “The Degree of the Set of Sentences of Predicate Provability Logic that are True under Every Interpretation,” *Journal of Symbolic Logic*, 52: 165–171.
[^montagna-1984]: Montagna, F., 1984, “The Predicate Modal Logic of Provability,” *Notre Dame Journal of Formal Logic*, 25(2): 179–189.
[^rybakov-2023]: Rybakov, M., 2023, “Predicate Counterparts of Modal Logics of Provability: High Undecidability and Kripke Incompleteness,” *Logic Journal of the IGPL*, first online 28 February 2023. doi:10.1093/jigpal/jzad002
[^vardanyan-1986]: Vardanyan, V.A., 1986, “Arithmetic Complexiy of Predicate Logics of Provability and their Fragments,” *Doklady Akademii Nauk SSSR*, 288: 11–14 (in Russian); English translation in *Soviet Mathematics Doklady*, 33: 569–572.
[^visser-2006]: Visser, A. and M. de Jonge, 2006, “No Escape from Vardanyan’s Theorem,” *Archive of Mathematical Logic*, 45(5): 539–554.
[^aguilera-2017]: Aguilera, J.P. and Fernández-Duque, D., 2017, “Strong Completeness of Provability Logic for Ordinal Spaces,” *The Journal of Symbolic Logic*, 82(2): 608–628.
[^alberucci-2009]: Alberucci, L., and A. Facchini, 2009, “On Modal μ-Calculus and Gödel-Löb logic,” *Studia Logica*, 91: 145–169.
[^ardeshir-2018]: Ardeshir, M. and Mojtahedi, M., 2018, “The $Σ_1$-Provability Logic of HA,” *Annals of Pure and Applied Logic*, 169(10): 997–1043.
[^artemov-1985b]: Artemov, S.N., 1985b,“On Modal Logics Axiomatizing Provability,” *Izvestiya Akadademii Nauk SSSR, Seriya Matematicheskaya*, 49(6): 1123–1154 (in Russian); English translation in *Mathematics of the USSR–Izvestiya*, 27(3): 402–429.
[^artemov-1994]: –––, 1994, “Logic of Proofs,” *Annals of Pure and Applied Logic*, 67(2): 29–59.
[^artemov-2001]: –––, 2001, “Explicit Provability and Constructive Semantics,” *Bulletin of Symbolic Logic*, 7: 1–36.
[^artemov-2007]: Artemov, S.N. and R. Iemhoff, 2007, “The Basic Intuitionistic Logic of Proofs,” *Journal of Symbolic Logic*, 72(2): 439–451.
[^artemov-1994-2]: Artemov, S.N. and F. Montagna, 1994, “On First-order Theories with Provability Operator,” *Journal of Symbolic Logic*, 59(4): 1139–1153.
[^artemov-2005]: Artemov, S.N. and Nogina, E., 2005, “Introducing Justification into Epistemic Logic,” *Journal of Logic and Computation*, 15(6): 1059–1073.
[^beklemishev-1989]: Beklemishev, L.D., 1989, “On the Classification of Propositional Provability Logics,” *Izvestiya Akademii Nauk SSSR, Seriya Matematicheskaya.*, 53(5): 915–943 (in Russian); English translation in *Mathematics of the USSR–Izvestiya*, 35 (1990) 247–275.
[^beklemishev-1994]: –––, 1994, “On Bimodal Logics of Provability,” *Annals of Pure and Applied Logic*, 68: 115–160.
[^beklemishev-1996]: –––, 1996, “Bimodal Logics for Extensions of Arithmetical Theories,” *Journal of Symbolic Logic*, 61: 91–124.
[^beklemishev-1999]: –––, 1999, “Parameter-Free Induction and Provably Total Computable Functions,” *Theoretical Computer Science*, 224: 13–33.
[^beklemishev-2003]: –––, 2003, “Proof-theoretic Analysis by Iterated Reflection,” *Archive for Mathematical Logic*, 6(42): 515–552.
[^beklemishev-2005-2]: –––, 2005, “Reflection Principles and Provability Algebras in Formal Arithmetic,” *Uspekhi Matematicheskikh Nauk*, 60(2): 3–78. (in Russian); English translation in: *Russian Mathematical Surveys*, 60(2): 197–268.
[^beklemishev-2006]: –––, 2006, “The Worm Principle,” in *Lecture Notes in Logic 27. Logic Colloquium ’02*, Z. Chatzidakis, P. Koepke, and W. Pohlers (eds.), Natick (MA): AK Peters, pp. 75–95.
[^beklemishev-2012]: –––, 2012, “Calibrating Provability Logic: From Modal Logic to Reflection Calculus,” in T. Bolander, T. Braüner, S. Ghilardi, and L. Moss (eds.), *Advances in Modal Logic* (Volume 9), London: College Publications, pp. 89–94.
[^beklemishev-2014-2]: –––, 2014, “Positive Provability Logic for Uniform Reflection Principles,” *Annals of Pure and Applied Logic*, 165 (1): 82–105.
[^beklemishev-2018a]: –––, 2018a, “A Note on Strictly Positive Logics and Word Rewriting Systems,” in S. Odintsov (ed.), *Larisa Maksimova on Implication, Interpolation, and Definability* (Outstanding Contributions to Logic: Volume 15), Cham: Springer, pp.61–70.
[^beklemishev-2018b]: –––, 2018b, “Reflection Calculus and Conservativity Spectra “, *Russian Mathematical Surveys*, 73(4): 569–613.
[^beklemishev-2014-3]: Beklemishev, L.D., D. Fernández-Duque, and J.J. Joosten, 2014, “On Provability Logics with Linearly Ordered Modalities,” *Studia Logica*, 102(3): 541–566.
[^beklemishev-2022]: Beklemishev, L. D., and Pakhomov, F. N., 2022, “Reflection Algebras and Conservation Results for Theories of Iterated Truth,” *Annals of Pure and Applied Logic*, 173(5): 103093.
[^beklemishev-1999-2]: Beklemishev, L.D., M. Pentus and N. Vereshchagin, 1999, *Provability, Complexity, Grammars*, American Mathematical Society Translations (Series 2, Volume 192).
[^beklemishev-2006-2]: Beklemishev, L.D. and A. Visser, 2006, “Problems in the Logic of Provability,” in D.M. Gabbay, S.S. Goncharov and M. Zakharyashev (eds.), *Mathematical Problems from Applied Logic I: Logics for the XXIst Century* (International Mathematical Series, Volume 4), New York: Springer, pp. 77–136.
[^benthem-2006]: van Benthem, J., 2006, “Modal Frame Correspondences and Fixed-points,” *Studia Logica*, 83(1-3): 133–155.
[^bernardi-1988]: Bernardi, C. and D’Aquino, P., 1988, “Topological Duality for Diagonalizable Algebras“, *Notre Dame Journal of Formal Logic*, 29(3): 345–364.
[^carbone-1990]: Carbone, A. and Montagna, F., 1990, “Much Shorter Proofs: A Bimodal Investigation,” *Mathematical Logic Quarterly*, 36(1): 47–66.
[^carlson-1986]: Carlson, T., 1986, “Modal Logics with Several Operators and Provability Interpretations,” *Israel Journal of Mathematics*, 54(1): 14–24.
[^dashkov-2012]: Dashkov, E.V., 2012, “On the Positive Fragment of the Polymodal Provability Logic GLP,” *Mathematical Notes*, 91 (3): 318–333.
[^dyckhoff-2016]: Dyckhoff, R and Negri, S., 2016, A Cut-free Sequent System for Grzegorczyk Logic, with an Application to the Gödel–McKinsey–Tarski Embedding, *Journal of Logic and Computation*, 26: 169–187.
[^fernández-duque-2014-2]: Fernández-Duque, D., 2014, “The Polytopologies of Transfinite Provability Logic,“ *Archive for Mathematical Logic*, 53(3-4): 385–431.
[^fernández-duque-2013a]: Fernández-Duque, D. and J.J. Joosten, 2013a, “Hyperations, Veblen Progressions, and Transfinite Iteration of Ordinal Functions,” *Annals of Pure and Applied Logic* 164 (7-8): 785–801, [[available online](http://www.sciencedirect.com/science/article/pii/S0168007213000109)].
[^fernández-duque-2013b]: Fernández-Duque, D. and J.J. Joosten, 2013b, “Models of Transfinite Provability Logic,” *Journal of Symbolic Logic*, 78(2): 543–561, [[available online](http://projecteuclid.org/DPubS?service=UI&version=1.0&verb=Display&handle=euclid.jsl/1368627064)].
[^giessen-2023]: van der Giessen, I., 2023, “Admissible Rules for Six Intuitionistic Modal Logics,” *Annals of Pure and Applied Logic*, 174(4): 103233.
[^giessen-2021]: van der Giessen, I. and Iemhoff, R., 2021, “Sequent Calculi for Intuitionistic Gödel–Löb Logic,” *Notre Dame Journal of Formal Logic*, 62(2): 221–246.
[^goré-2014]: Goré, R and Ramanayake, R., 2014, “Cut-elimination for Weak Grzegorczyk Logic Go,” *Studia Logica*, 102(1): 1–27.
[^guaspari-1979]: Guaspari, D. and R.M. Solovay, 1979, “Rosser Sentences,” *Annals of Mathematical Logic*, 16: 81–99.
[^iemhoff-2000]: Iemhoff, R., 2000, “A Modal Analysis of some Principles of the Provability Logic of Heyting Arithmetic,” in *Advances in Modal Logic* (Volume 2), M. Zakharyashev et al. (eds.), Stanford: CSLI Publications, pp. 319–354.
[^iemhoff-2001]: –––, 2001, “On the Admissible Rules of Intuitionistic Propositional Logic,” *Journal of Symbolic Logic*, 66: 281–294.
[^iemhoff-2003]: –––, 2003, “Preservativity Logic: An Analogue of Interpretability Logic for Constructive Theories,” *Mathematical Logic Quarterly*, 49(3): 1–21.
[^iemhoff-2005]: Iemhoff, R., de Jongh, D. and Zhou, C., 2005, “Properties of Intuitionistic Provability and Preservativity Logics,” *Logic Journal of the IGPL*, 13(6): 615–636.
[^joosten-2021]: Joosten, J.J., 2021, “Münchhausen Provability,” *The Journal of Symbolic Logic*, 86(3): 1006–1034.
[^kuznets-2019]: Kuznets, R. and Studer, T., 2019, *Logics of Proofs and Justifications*, London: College Publications.
[^lindström-1994]: Lindström, P., 1994, “The Modal Logic of Parikh Provability,” *Filosofiska Meddelanden*, Gröna Serien, Gothenburg: Göteborgs Universitetet.
[^lindström-2006-2]: Lindström, P., 2006, “On Parikh Provability: An Exercise in Modal Logic,” in H. Lagerlund, S. Lindström, and R. Sliwinski (eds.), *Modality Matters: Twenty-Five Essays in Honour of Krister Segerberg*, Uppsala: Uppsala Philosophical Studies (Volume 53), pp. 53–287.
[^litak-2007]: Litak, L., 2007, “The Non-Reflexive Counterpart of Grz,” *Bulletin of the Section of Logic*, 36(3–4): 195–208.
[^litak-2018]: Litak, T. and Visser, A., 2018, “Lewis Meets Brouwer: Constructive Strict Implication,” *Indagationes Mathematicae*, 29(1): 36–90.
[^litak-nd]: –––, forthcoming, “Lewisian Fixed Points I: Two Incomparable Constructions,” in N. Bezhanishvili, R. Iemhoff and F. Yang (eds.), *Dick de Jongh on Intuitionistic and Provability Logic*, Cham: Springer.
[^maksimova-2014]: Maksimova, L.L., 2014, “The Lyndon Property and Uniform Interpolation over the Grzegorczyk Logic,” *Siberian Mathematical Journal*, 55(1): 118–124.
[^mares-2000]: Mares, E.D., 2000, “The Incompleteness of RGL,” *Studia Logica*, 65: 315–322.
[^mojtahedi-nd]: Mojtahedi, M., forthcoming, “The $Σ_1$-provability logic of HA revisited,” in N. Bezhanishvili, R. Iemhoff and F. Yang (eds.), *Dick de Jongh on Intuitionistic and Provability Logic*, Cham: Springer.
[^montagna-1978]: Montagna, F.,1978, “On the algebraization of a Feferman’s predicate,” *Studia Logica*, 37(3): 221–236.
[^montagna-1979]: –––, 1979, “On the Diagonalizable Algebra of Peano Arithmetic,” *Bollettino della Unione Matematica Italiana*, B(5), 16: 795–812.
[^montagna-1980a]: –––, 1980a, “Interpretations of the First-order Theory of Diagonalizable Algebras in Peano Arithmetic,” *Studia Logica*, 39: 347–354.
[^montagna-1980b]: –––, 1980b, “Undecidability of the First-order Theory of Diagonalizable Algebras, ” *Studia Logica*, 39: 355–359.
[^montagna-1992]: –––, 1992, “Polynomially and Superexponentially Shorter Proofs in Fragments of Arithmetic,” *Journal of Symbolic Logic*, 57: 844–863.
[^pakhomov-2012]: Pakhomov, F.N., 2012, “Undecidability of the Elementary Theory of the Semilattice of GLP-words,” *Sbornik: Mathematics*, 203(8): 1211.
[^pakhomov-2015]: Pakhomov, F.N., 2015, “On Elementary Theories of Ordinal Notation Systems Based on Reflection Principles,” *Proceedings of the Steklov Institute of Mathematics*, 289: 194–212.
[^savateev-2019]: Savateev, Y., and Shamkanov, D., 2019, “Cut Elimination for the Weak Modal Grzegorczyk Logic via Non-well-founded Proofs,” in R. Iemhoff, M. Moortgat, M. and R. de Queiroz (eds.), *Proceedings of WoLLIC 2019*, Heidelberg: Springer, pp. 569–583.
[^savateev-2021]: –––, 2021, “Non-well-founded Proofs for the Grzegorczyk Modal Logic,” *The Review of Symbolic Logic*, 14(1): 22–50.
[^shamkanov-2016]: Shamkanov, D.S., 2016, “A Realization Theorem for the Gödel–Löb Provability Logic,” *Sbornik: Mathematics*, 207(9): 1344–1360.
[^shapirovsky-2008]: Shapirovsky, I., 2008, “PSPACE-decidability of Japaridze’s Polymodal Logic,” *Advances in Modal Logic*, 7: 289–304.
[^shavrukov-1993a]: Shavrukov, V.Yu., 1993a, “A Note on the Diagonalizable Algebras of PA and ZF,” *Annals of Pure and Applied Logic*, 61: 161–173.
[^shavrukov-1993b]: –––, 1993b, “Subalgebras of Diagonalizable Algebras of Theories Containing Arithmetic,” *Dissertationes Mathematicae*, 323.
[^shavrukov-1994]: –––, 1994, “A Smart Child of Peano’s,” *Notre Dame Journal of Formal Logic*, 35(2): 161–185.
[^troelstra-1973]: Troelstra, A.S., 1973, *Metamathematical Investigation of Intuitionistic Arithmetic and Analysis*, Berlin: Springer-Verlag.
[^visser-1980]: Visser, A., 1980, *Aspects of Diagonalization and Provability*, Ph.D. Thesis, Utrecht: University of Utrecht.
[^visser-1982]: –––, 1982, “On the Completeness Principle: A Study of Provability in Heyting’s Arithmetic and Extensions,” *Annals of Mathematical Logic*, 22(3): 263–295.
[^visser-1989]: –––, 1989, “Peano’s Smart Children: A Provability Logical Study of Systems with Built-in Consistency,” *Notre Dame Journal of Formal Logic*, 30(2): 161–196.
[^visser-1995]: –––, 1995, “A Course on Bimodal Provability Logic,” *Annals of Pure and Applied Logic*, 73(1): 109–142.
[^visser-1999]: –––, 1999, “Rules and Arithmetics,” *Notre Dame Journal of Formal Logic*, 40(1): 116–140.
[^visser-2002]: –––, 2002, “Substitutions of $\Sigma_1$ Sentences: Explorations between Intuitionistic Propositional Logic and Intuitionistic Arithmetic,” *Annals of Pure and Applied Logic*, 114: 227–271.
[^visser-2005]: –––, 2005, “Löb’s Logic Meets the μ-Calculus,” in A. Middeldorp, V. van Oostrom, F. van Raamsdonk and R. de Vrijer (eds.), *Processes, Terms and Cycles: Steps on the Road to Infinity*, Berlin: Springer, pp. 14–25.
[^visser-2008]: –––, 2008, “Closed Fragments of Provability Logics of Constructive Theories,” *Journal of Symbolic Logic*, 73: 1081–1096.
[^visser-2016]: –––, 2016, “The Second Incompleteness Theorem: Reflections and Ruminations,” in L. Horsten and P. Welch (eds.), *Gödel’s Disjunction: The Scope and Limits of Mathematical Knowledge*, Oxford: Oxford University Press, pp. 67–91.
[^visser-2020]: –––, 2020, “Another Look at the Second Incompleteness Theorem,” *The Review of Symbolic Logic*, 13(2): 269–295.
[^visser-2019]: Visser, A. and Zoethout, J., 2019, “Provability Logic and the Completeness Principle,” *Annals of Pure and Applied Logic*, 170(6): 718–753.
[^yavorskaya-2001]: Yavorskaya, T., 2001, “Logic of Proofs and Provability,” *Annals of Pure and Applied Logic*, 113(1-3): 345–372.
[^zambella-1994]: Zambella, D., 1994, “Shavrukov’s Theorem on the Subalgebras of Diagonalizable Algebras for Theories Containing $I \Delta_0 + \exp$,” *Notre Dame Journal of Formal Logic*, 35: 147–157.
[^crocco-2019]: Crocco, G., 2019, “Informal and Absolute Proofs: Some Remarks from a Gödelian Perspective,” *Topoi*, 38: 561–575.
[^davis-1990]: Davis, M., 1990, “Is Mathematical Insight Algorithmic?,” Commentary on Roger Penrose, The Emperor’s New Mind, *Behavioral and Brain Sciences*, 13: 659–660.
[^davis-1993]: –––, 1993, “How Subtle is Gödel’s Theorem? More on Roger Penrose” (Commentary on Roger Penrose, The Emperor’s New Mind), *Behavioral and Brain Sciences*, 16: 611–612.
[^egré-2005]: Egré, P., 2005, “The Knower Paradox in the Light of Provability Interpretations of Modal Logics,” *Journal of Logic, Language, and Information*, 14(1): 13–48.
[^franzén-2005]: Franzén, T., 2005, *Gödel’s Theorem: An Incomplete Guide to its Use and Abuse*, Boca Raton, Florida: CRC Press.
[^gödel-1946]: Gödel, K., 1946, “Remarks Before the Princeton Bicentennial Conference on Problems in Mathematics,” reprinted in S. Feferman et al. (eds.), *Kurt Gödel Collected Works, Volume II: Publications 1938–1975*, New York, Oxford: Oxford University Press, 1990, pp. 150–153.
[^kaplan-1960]: Kaplan, D. and R. Montague, 1960, “A Paradox Regained,” *Notre Dame Journal of Formal Logic*, 1(3): 79–90.
[^kennedy-2014]: Kennedy, J., 2014, “Gödel’s 1946 Princeton Bicentennial Lecture: An Appreciation,” in J. Kennedy (ed.), *Interpreting Gödel: Critical Essays*, Cambridge: Cambridh=ge University Press, pp.109–130.
[^koellner-2016]: Koellner, P., 2016, “Gödel’s Disjunction,” in L. Horsten and P. Welch (eds.), *Gödel’s Disjunction: The Scope and Limits of Mathematical Knowledge*, Oxford: Oxford University Press, pp. 148–188.
[^kreisel-1967]: Kreisel, G., 1967, “Informal Rigour and Completeness Proofs,” in I. Lakatos (ed.), *Problems in the Philosophy of Mathematics*, Amsterdam: North-Holland, pp. 138–157.
[^leach-krouse-2013]: Leach-Krouse, G.E., 2013, “Conceptions of Absolute Provability,” Ph.D. Thesis, Note Dame: Notre Dame University.
[^leach-krouse-2016]: Leach-Krouse, G.E., 2016, “Provability, Mechanism, and the Diagonal Problem,” in L. Horsten and P. Welch (eds.), *Gödel’s Disjunction: The Scope and Limits of Mathematical Knowledge*, Oxford: Oxford University Press, pp. 211–242.
[^lindström-2001]: Lindström, P, 2001, “Penrose’s New Argument,” *Journal of Philosophical Logic*, 30: 241–250.
[^montague-1963]: Montague, R., 1963, “Syntactical Treatments of Modality, with Corollaries on Reflection Principles and Finite Axiomatizability,” *Acta Philosophica Fennica*, 16: 153–67.
[^quine-1966]: Quine, W.V., 1966, “Necessary Truth,” in Quine, W.V., *The Ways of Paradox and Other Essays*, New York: Random House, pp. 48–56.
[^quine-1953]: –––, 1953, “Three Grades of Modal Involvement,” in *Proceedings of the 11th International Congress of Philosophy*, Amsterdam: North-Holland, pp. 65-81; reprinted in W.V. Quine, *The Ways of Paradox and Other Essays*, New York: Random House, 1966, pp. 156–174.
[^vos-2023]: de Vos, M., Verbrugge, R., and Kooi, B., 2023, “Solutions to the Knower Paradox in the Light of Haack’s Criteria,” *Journal of Philosophical Logic*, 52: 1101–1132.
[^williamson-2016]: Williamson, T., 2016, “Absolute Provability and Safe Knowledge of Axioms,” in L. Horsten and P. Welch (eds.), *Gödel’s Disjunction: The Scope and Limits of Mathematical Knowledge*, pp. 243–253.

## 学术工具

* [如何引用本词条](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=logic-provability)。
* [预览本词条的 PDF 版本](https://leibniz.stanford.edu/friends/preview/logic-provability/)，见 [SEP 学会之友](https://leibniz.stanford.edu/friends/)。
* 在 [InPhO](https://www.inphoproject.org/entity?sep=logic-provability&redirect=True) 查找与本词条相关的话题与思想家。
* 在 [PhilPapers](https://philpapers.org/sep/logic-provability/) 查看本词条的增强文献目录及其数据库链接。

## 其他网络资源

### 论文与报告

* Férée, H., I. van der Giessen, S. van Gool, and I. Shillito, 2024, “[模态逻辑 K、GL 与 iSL 的机械化一致插值](https://arxiv.org/abs/2402.10494)”，arxiv.org 手稿。
* Fitting, M., 2020, “[第二个 GL 辩护逻辑](https://id144254.securedata.net/melvinfitting/bookspapers/pdf/papers/GLJustification.pdf)”，手稿见于作者网站。
* Goré, R. and J. Kelly, 2007, “[Gödel-Löb 可证性逻辑中的自动证明搜索](https://www.dcs.bbk.ac.uk/~roman/blc/gore-kelly-provability.pdf)”，2007 年在[英国逻辑讨论会](http://www.dcs.bbk.ac.uk/~roman/blc/)上宣读。
* Henk, P., and Pakhomov, F., 2016, “[皮亚诺算术的慢可证性与通常可证性](https://arxiv.org/pdf/1602.01822v2.pdf)”，arxiv.org 手稿。
* Mojtahedi, M., 2022, “[论 HA 的可证性逻辑](https://arxiv.org/abs/2206.00445)”，arxiv.org 手稿。
* Pakhomov, F., 2014a, “[论 GLP-代数的初等理论](http://arxiv.org/abs/1412.4439)”，arxiv.org 手稿。
* Verbrugge, Rineke, [可证性逻辑讲稿](https://rinekeverbrugge.nl/wp-content/uploads/2017/02/VerbruggeProvability-Logic-clc11-1.pdf)，讲义，格罗宁根大学。
* Visser, Albert, 1986, [论形式可证性与人类可证性](https://www.phil.uu.nl/onderwijs/cki/cki10/cki/slides/lucasac.pdf)（荷兰语），在线手稿，乌得勒支大学。

### 其他站点

* [可证性逻辑开问题清单](http://www.mi.ras.ru/~bekl/problems.html)，由 Lev Beklemishev 维护
* [“数学基础”邮件列表](http://www.cs.nyu.edu/mailman/listinfo/fom/)，纽约大学

## 相关词条

基于逻辑的人工智能 | 可计算性与复杂度 | 柯里悖论 | 菲奇的可知性悖论 | 库尔特·哥德尔 | 哥德尔不完备定理 | 希尔伯特计划 | 现代模态逻辑的起源 | 经典逻辑 | 认知逻辑 | 直觉主义逻辑 | 确证逻辑 | 模态逻辑 | 相干逻辑 | 数学哲学 | 构造数学 | 模型论 | 可能世界 | 《数学原理》 | 证明论的发展 | 威拉德·冯·奥曼·蒯因 | 自我指涉 | 大基数与独立性 | 艾伦·图灵

**（译注：相关词条的中文站内链接将由管线在对应词条重译完成后统一挂接。）**

## 致谢

我谨向 Lev Beklemishev 致以最诚挚的谢意：他于 2017 年惠赐一封长信，其中包含大量文献引证，从他自己的视角呈现了可证性逻辑的发展。同样感谢 Albert Visser、Sara Uckelman、Rajeev Goré、Giovanni Sambin、Vítězslav Švejdar、Sara Negri、Joost Joosten、Ian Shillito、Wesley Holliday、Revantha Ramanayake、Anupam Das、Shawn Standefer、Toby Meadows、Edson Bezerra、Nils Kürbis 与 Tadeusz Litak——感谢他们为本文 2017 年和/或 2024 年版本的改进与增补提出建议。

谨以本文 2024 年版纪念可证性逻辑与一阶算术元数学的三位元老：Franco Montagna（1948–2015）、Sol Feferman（1928–2016）与 Petr Hájek（1940–2016）。
