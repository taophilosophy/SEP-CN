# 相干逻辑 Relevance Logic (Edwin Mares)

*首次发表于 1998 年 6 月 17 日；2020 年 11 月 13 日实质修订。*

**相干逻辑** 属非经典逻辑。英国与澳大拉西亚学界把它叫做 “relevant logics”。这类系统之所以发展起来，就是为了避开实质蕴涵和严格蕴涵的悖论。所谓悖论，是指按实质蕴涵、严格蕴涵的定义推出来的有效结论，只是有些人觉得这些结论有问题。

比如，实质蕴涵 $(p \rightarrow q)$ 在 $p$ 假或 $q$ 真时为真，也就是 $(\neg p \vee q)$。因此，$p$ 为真时，只要 $q$ 真，实质蕴涵就真。实质蕴涵的悖论有：

$$\begin{align} & p \rightarrow(q \rightarrow p), \\ & \neg p \rightarrow(p \rightarrow q), \\ & (p \rightarrow q) \vee(q \rightarrow r). \end{align}$$

第一式说的是：每个命题都蕴涵一个真命题。第二式说：假命题蕴涵任何命题。第三式说：任取三个命题，要么第一个蕴涵第二个，要么第二个蕴涵第三个。

同理，严格蕴涵 $(p \rightarrow q)$ 在不可能“$p$ 真而 $q$ 假”时为真，也就是 $\neg \diamond(p \mathbin{\&} \neg q)$。严格蕴涵的悖论有：

$$\begin{align} & (p \mathbin{\&} \neg p) \rightarrow q, \\ & p \rightarrow(q \rightarrow q), \\ & p \rightarrow(q \vee \neg q). \end{align}$$

第一式说的是：矛盾严格蕴涵任何命题。第二式和第三式则意味着：每个命题都严格蕴涵某个重言式。

从 Hugh MacColl（1908）起，不少哲学家就认为这些论题反直觉。他们说：如果把 $\rightarrow$ 理解为我们在学经典逻辑之前就有的蕴涵概念，这些公式并不有效。相干逻辑学家则说，这些所谓悖论之所以叫人不安，是因为每一例里前件和后件看上去毫不相干。

另外，经典逻辑判定有效的某些推理，也让相干逻辑学家不放心。例如下面这个经典有效推理：

> 月亮是绿奶酪做的。所以，现在厄瓜多尔要么在下雨，要么没下雨。

这里同样像是相干性断了：结论与前提似乎毫无关系。相干逻辑学家想构造出一些逻辑，把犯“相干性谬误”的论题和论证排除掉。

相干逻辑学家指出，有些悖论（以及谬误）的毛病，在于前件和后件（或前提和结论）根本不在同一个话题上。可“话题”这种东西，似乎不该是逻辑学家操心的事——它关涉句子或推理的内容，不关涉形式。不过有一条形式原则，相干逻辑学家用它逼着定理和推理“留在话题上”，这就是 **变量共享原则**。该原则说：在相干逻辑里，若 $A$ 与 $B$ 连一个共同的命题变元（有时叫命题字母）都没有，任何形如 $A \rightarrow B$ 的公式都证不出来；若前提与结论不共享至少一个命题变元，任何推理都不能被证明有效。

讲到这里，人们对相干逻辑学家究竟想干什么感到困惑，也很自然。变量共享原则只是逻辑成为相干逻辑的必要条件，不是充分条件；它也没有给出一个能扫清所有悖论和谬误的标准——有些悖论或谬误照样满足变量共享，却仍是悖论或谬误。不过下文会看到，相干逻辑确实凭“前提的真正使用”给出了相干的证明概念（见下文“证明论”一节），但它本身并不告诉我们什么才算真（且相干）的蕴涵；只有把形式理论和哲学解释放在一起，它才能做到这一点（见下文“相干蕴涵的语义”一节）。

本文对相干逻辑这个领域作一个简短、相对不那么技术的概述。

## 1 相干蕴涵的语义

本文讲相干逻辑的顺序，和文献里大多数讲法相反：先讲语义，而不是把语义放在最后，因为如今多数哲学家都偏爱语义。

这里讲的语义，是 Richard Routley 与 Robert K. Meyer 的三元关系语义，由 Alasdair Urquhart 的“半格语义”发展而来（Urquhart 1972）[^urquhart-1972]。Kit Fine 另有一种类似的语义，与 Routley–Meyer 理论同时提出（Fine 1974）[^fine-1974]；J. Michael Dunn 则有代数语义。Urquhart、Fine、Dunn 的模型本身都很有意趣，可惜这里没有篇幅讨论。

三元关系语义的想法其实很简单。回想 C.I. Lewis 为避免实质蕴涵悖论所做的尝试：他给经典逻辑添了一个新联结词，即严格蕴涵。用 Kripke 之后的语义术语说，$A \mathbin{\unicode{x22b0}} B$ 在世界 $w$ 为真，当且仅当凡 $w'$ 可被 $w$ 通达，要么 $A$ 在 $w'$ 失败，要么 $B$ 在 $w'$ 成立。但在 Kripke 的模态逻辑语义里，可及关系是二元关系，只成立于世界对之间。遗憾的是，从相干的观点看，严格蕴涵理论仍不相干：我们照样使 $p \mathbin{\unicode{x22b0}} (q \mathbin{\unicode{x22b0}} q)$ 这类公式有效。稍加推演就能看出，Kripke 的真值条件逼出了这条公式。

相干逻辑的语义与模态逻辑一样，也把公式的真值相对于世界。但 Routley 与 Meyer 比模态逻辑更进一步，用的是世界间的三元关系。于是可以有使 $q \rightarrow q$ 失败的世界，进而也可以有使 $p \rightarrow(q \rightarrow q)$ 失败的世界。他们在这种语义下给 $\rightarrow$ 的真值条件是：

$A \rightarrow B$ 在世界 $a$ 为真，当且仅当凡满足 $Rabc$ 的世界 $b$、$c$（$R$ 即可及关系），要么 $A$ 在 $b$ 上为假，要么 $B$ 在 $c$ 上为真。

刚入门的人得花点时间才习惯这个真值条件。不过稍加推敲就能看出，它无非是 Kripke 严格蕴涵真值条件的推广——只要令 $b = c$ 就行。

三元关系语义稍作调整，就能给一大类逻辑当语义：对关系加不同约束，有效的公式和推理也随之不同。比如，若约束关系使 $Raaa$ 对一切世界 $a$ 成立，就能保证：只要 $(A \rightarrow B) \mathbin{\&} A$ 在某世界为真，$B$ 也在那里为真；再结合 Routley–Meyer 语义的其他特征，论题 $((A \rightarrow B) \mathbin{\&} A) \rightarrow B$ 便有效。若让三元关系的前两位对称，即凡世界 $a, b$ 与 $c$ 满足 $Rabc$ 就有 $Rbac$，那么论题 $A \rightarrow ((A \rightarrow B) \rightarrow B)$ 也有效。

要让相干蕴涵在这种语义上有真正的意义，三元可及关系就需要哲学解释。近年来已有几种基于信息理论的解释。

Jon Barwise（1993）提出一种解释，Restall（1996）进一步阐发。这种看法把世界当作信息论意义上的“站点”和“信道”：站点接收信息，信道传送信息。比如 BBC 新闻出现在我客厅的电视上时，客厅可算站点，连接电视与伦敦演播室的线缆、卫星等可算信道。用信道论解释 Routley–Meyer 语义，$Rabc$ 意为 $a$ 是站点 $b$、$c$ 之间的信息论信道；于是 $A \rightarrow B$ 在 $a$ 为真，当且仅当 $a$ 把 $A$ 在其中成立的站点 $b$ 连到站点 $c, B$ 在 $c$ 成立。

同样，Mares（1997）采用了 David Israel 与 John Perry（1990）提出的一种信息理论。一个世界除包含其他信息外，还包含信息联系，比如自然规律、约定等。例如，牛顿式的世界包含“一切物质都吸引其他一切物质”这一信息。用信息论的术语说，它包含的信息是：两物为物质，承载着它们相互吸引的信息。按这种看法，$Rabc$ 成立，当且仅当依 $a$ 中的联系，$b$ 中所发生之事承载的全部信息都包含在 $c$ 中。于是，若 $a$ 是牛顿式的世界，而“$x$ 与 $y$ 是物质”这一信息包含在 $b$ 中，那么“$x$ 与 $y$ 相互吸引”这一信息就包含在 $c$ 中。

Mares（2004）提出另一种解释，把 Routley–Meyer 语义看作“情境化蕴涵”概念的形式化，并把该语义中的“世界”看作 **情境**。情境是对宇宙的一种表象，可能只涉及部分。两个情境 $a$ 与 $b$ 所含的信息合在一起，也许能推出关于宇宙的进一步信息，而这是两个情境各自都不包含的。比如，假定当前情境中有广义相对论定律所含的信息（即爱因斯坦的引力理论），我们又设想一个能看到恒星沿椭圆运动的情境；那么根据手头的信息与所设想的情境，就能推出：存在一个情境，其中有个极重的天体在作用于这颗恒星。

用关系 $I$（“蕴涵”的缩写）可以给情境化推理建模：$IabP$ 成立（$P$ 是命题），当且仅当 $a$ 与 $b$ 的信息合起来许可推出“存在一个 $P$ 在其中成立的情境”。命题本身可视为一个情境集合。规定 $A \rightarrow B$ 在 $a$ 成立，当且仅当对所有使 $A$ 成立的情境 $b$，都有 $Iab|B|,$，这里 $|B$| 是使 $B$ 为真的情境集合。规定 $Rabc$ 成立，当且仅当 $c$ 属于每个满足 $IabP$ 的命题 $P$。再补一条公设：任取满足 $IabP$ 的命题集 $P$，其交集 $X$ 也满足 $IabX$。由此可知，借 $I$ 的真值条件在任何情境上判为真的蕴涵，与 Routley–Meyer 真值条件判为真的蕴涵一致。可见情境化推理为理解 Routley–Meyer 语义提供了一条途径。（以上只是 Mares（2004）第 2、3 章相关讨论的极简版。）

另一种信息论解释见 Dunn（2015）。它把相干逻辑的相干概念，同 Grice 会话准则与 Sperber、Wilson 语用理论中的语用相干概念挂上了钩。想法是：三个“状态” $a,b,c$ 之间有关系 $R$，意思是在语境 $a$ 中，$b$ 对 $c$ 相干；也就是说，合起来使用 $a$ 与 $b$ 的信息，可以推出 $c$ 的信息。这里的“推出”即 Sperber 与 Wilson 所说的“语境蕴涵”：结论可从 $a$ 与 $b$ 的信息推出，却不能从其中任一单独推出（Sperber and Wilson, 2002, p. 251）。$a$ 与 $b$ 的信息如何结合，可以有不同理解。Dunn 讨论的一种是：把 $a$、$b$ 比作计算机程序，两者的结合即其复合——先运行 $b$，把结果作为 $a$ 的输入，再运行 $a$。若这样产生的信息全在 $c$ 中，该结合便与 $c$ 相干。

Beall 等（2012）给出另一种解释，实际上提出了三元关系的三种解释，分别联系不同的“条件性”概念。这里只谈两种，第三种对百科词条来说过于繁复。第一种解释认为，条件句 $A\rightarrow B$ 在世界 $a$ 成立，当且仅当该条件句没有反例，即没有相对于 $a$ 而言显著的地点使 $A$ 成立而 $B$ 失败。这种“地点”不是单个世界，而是一对世界 $b,c$：若 $A$ 在这一对的第一个世界为真、$B$ 在第二个世界不为真，这对世界就是反例。

第二种解释认为，Routley–Meyer 模型的点既是（数学意义上的）算子，又是其作用对象。按这种理解，$Rabc$ 意为：把 $a$ 当作算子作用于 $b$，所产生的信息全部包含在 $c$ 中。这样，Routley–Meyer 语义在意图上就很接近 Fine 的算子语义，也与 Dunn 的解释（尤其是其状态信息结合的概念）关系密切。

光有三元关系还不够，避不开所有蕴涵悖论。按目前所述，还看不出这种语义怎样排除 $(p \mathbin{\&} \neg p) \rightarrow q$、$p \rightarrow (q \vee \neg q)$ 这类悖论。办法是在语义中放进不一致世界与非二值世界。因为若没有世界使 $p \mathbin{\&} \neg p$ 成立，按箭头的真值条件，$(p \mathbin{\&} \neg p) \rightarrow q$ 就会处处成立；同理，若 $q \vee \neg q$ 在每个世界都成立，$p \rightarrow(q \vee \neg q)$ 便普遍为真。

Routley、Loparic（1978）以及 Priest（1992、2008）提出了一种不用三元关系的相干性进路。它使用一个世界集合和一个二元关系 $S$，把世界分成正规世界与非正规世界。蕴涵 $A \rightarrow B$ 在正规世界 $a$ 为真，当且仅当凡世界 $b$ 使 $A$ 在 $b$ 为真，$B$ 也在 $b$ 为真；在非正规世界，蕴涵真值随机，或真或假。公式有效，当且仅当它在每个这类模型的 **正规** 世界都为真。如此划分世界，并让非正规世界的蕴涵取随机真值，就能为 $p \rightarrow (q \rightarrow q)$ 之类公式找到反模型。

Priest 把非正规世界解释为“逻辑虚构”所对应的世界。科幻小说里的自然规律可以与我们宇宙不同；同样，逻辑虚构里的逻辑规律也可以不同于我们的规律，比如 $A \rightarrow A$ 在某些逻辑虚构中就不为真。这类虚构描述的世界，就是非正规世界。

不用三元关系的语义有个毛病：它能刻画的逻辑系统范围，远不如三元关系语义那么广。而且，这种语义确定的逻辑相当弱，比如不把蕴涵传递性 $((A \rightarrow B) \mathbin{\&}(B \rightarrow C)) \rightarrow (A \rightarrow C)$ 当作定理。

这种语义和三元关系语义一样，也要求有些世界不一致、有些世界非二值。

## 2 否定语义

要让不一致世界与非二值世界派上用场，否定就得用非经典的真值条件。20 世纪 70 年代初，Richard 与 Val Routley 发明“星号算子”来处理否定（Routley & Routley 1972）。这是作用于非正规世界的算子：每个世界 $a$ 都有对应的世界 $a$*。并且

$\neg A$ 在 $a$ 上为真，当且仅当 $A$ 在 $a$* 上为假。

这里又碰上了解释形式语义某一部分的难题。Dunn（1993）对 Routley 星号给出一种解释：他在世界之间用一个二元关系 $C$，$Cab$ 表示 $b$ 与 $a. a$* 相容；这个星号世界就是与 $a$ 相容的极大世界，也就是信息最多的世界。

否定还有别的语义。一种是 Dunn 的四值语义：和经典逻辑的真值表一样，它从 T（真）、F（假）两个值出发，但给公式赋予这些真值的一个集合。于是公式 $A$ 可取 $\{\mathrm{T}\}$、$\{\mathrm{F}\}$、$\{\mathrm{T},\mathrm{F}\}$ 或 $\varnothing$。取 $\{\mathrm{T}\}$ 就是单纯为真，取 $\{\mathrm{F}\}$ 就是单纯为假；取 $\{\mathrm{T},\mathrm{F}\}$ 是既真又假，取 $\varnothing$ 则既不真也不假。

每个公式既有真条件，也有假条件。比如，T 属于 $\neg A$ 的值，当且仅当 F 属于 $A$ 的值；F 属于 $\neg A$ 的值，当且仅当 T 属于 $A$ 的值。合取方面，T 属于 $A \mathbin{\&} B$ 的值，当且仅当 T 同时属于 $A$ 与 $B$ 的值；F 属于 $A \mathbin{\&} B$ 的值，当且仅当 F 属于 $A$ 的值或属于 $B$ 的值。析取的真、假条件与此十分相似。

Dunn 提出这套语义，是为了刻画 FDE（First Degree Entailment）；它只处理不含蕴涵的公式之间的蕴涵。（关于 FDE 的性质与发展，见 Omori & Wansing 2017。）[^omori-2017] Richard Routley（1988）把该理论推广到某些弱相干逻辑，Restall（1995）又推广到仅比著名相干逻辑 E、R 稍弱的逻辑（见下文第 4、5 节）。Mares（2004a）用邻域语义加上四个真值，为 R 给出一种语义。四值语义在“次协调逻辑”词条中讲得更细；否定的其他处理（有些曾用于相干逻辑）见 Wansing（2001）与“否定”词条。

## 3 量化语义

Richard Routley（1980）猜想，模态逻辑中常见的那种常域语义足以刻画量化相干逻辑。按这种语义，全称量化公式 $\forall xA(x)$ 在某个世界为真，当且仅当 $A(x)$ 在 $x$ 的每种解释下都为真。

可惜，Kit Fine（1988a）证明：逻辑 RQ（相干蕴涵逻辑 R 加上若干标准量化公理）在常域语义下不完全。

Fine（1988b）又给出一种语义，RQ 相对于它完全，而且稍加修改就能容纳任何主流相干逻辑。Fine 的语义是“分层”的：一个模型由一组微型模型构成，每个微型模型各有自己的个体域；每个微型模型都与域更大的模型相连，一个模型中的每个世界也照此与那些更大域模型中的世界相连。Shay Logan（2019）对 Fine 语义的运作方式解释得很清楚。

Mares 与 Robert Goldblatt（2006）给出量化相干逻辑的另一种语义，Goldblatt（2011）又作了发展。除了世界与域，这种模型还包含一个命题集合，而命题就是指定的世界集合。公式 $\forall xA(x)$ 在世界 $w$ 为真，当且仅当存在一个在 $w$ 为真的命题 $\pi$，$\pi$ 蕴涵 $A(x)$ 的每个实例；也就是说，在 $\pi$ 所含的每个世界里，$A(x)$ 的每个实例都为真。

Mares–Goldblatt 语义又叫“可容许集合”语义：命题就是可容许集合。至少有些模型里，并非任意一组世界都算命题。理由之一来自对人类如何把不同境况归为相似的反思：并非每一组情境都让人觉得组内成员彼此相似、而与组外情境不相似。把命题看成“可以充当某人内容的世界集合”，似乎说得通。（若真造一种语言来谈论人们换种说法会想什么，也许可以把命题集索引到世界；不过那是后话。）

相干量化理论有一个有用的补充：用条件句来表示受限量化。这是 Jc Beall 等（2006）提出的。拿范畴图式“所有 $A$ 都是 $B$”来说，经典逻辑把它译为 $\forall x(A(x)\supset B(x))$；但在相干逻辑里，实质条件句 $\supset$ 太弱，干不了这活（相干逻辑把 $A\supset B$ 理解为 $\neg A\vee B$）。若照此使用实质蕴涵，相干逻辑的模型里就可能出现这样的世界：所有 $A$ 都是 $B$，某个 $i$ 是 $A$，可 $i$ 却不是 $B$。实质条件句太弱，相干蕴涵又太强。比如有人说“这屋里的每个人都养狗”，她并不是说“身处此屋”能推出“养狗”，只是碰巧这屋里的每个人都养狗罢了。受限量化条件句想捕捉的，正是这种介于实质蕴涵与相干蕴涵之间的联系。

不过，Beall 等（2006）的条件句是不是合适的联结词，至少对某些较弱相干逻辑来说，还不好说。有些较弱系统的长处，是能用来形式化朴素集合论（见第 6 节）。Zach Weber（2010）就用这个条件句定义子集关系，形式化了朴素集合论；可惜所得系统是平凡的——其中每个公式都可证。

## 4 证明论

最常被当作相干逻辑范式的，是逻辑 $\mathbf{R}$。$\mathbf{R}$ 的公理化见[逻辑 $\mathbf{R}$](logic-relevance.logicr.md)。

如今 $\mathbf{R}$ 的证明论有好几条进路：Gregory Mints（1972）与 J.M. Dunn（1973）为 $\mathbf{R}$ 的无否定片段给出了矢列演算；Nuel Belnap（1982）发展出“显示逻辑”，优雅而极为一般。这里只讲 Anderson 与 Belnap 为相干逻辑 $\mathbf{R}$ 建立的自然演绎系统。

Anderson 与 Belnap 的自然演绎系统，建立在 Fitch 为经典逻辑和直觉主义逻辑设计的自然演绎系统之上。要看懂这套技术，最省事的办法是看一个例子。

| 1. | $A_{\{1\}}$ | 假设 |
| --- | --- | --- |
| 2. | $(A \rightarrow B)_{\{2\}}$ | 假设 |
| 3. | $B_{\{1,2\}}$ | $1,2, \rightarrow$ E |

这是肯定前件的一个简单例子。花括号里的数字，是证明该公式所用到的假设，我们称之为“索引”。结论上的索引表明：推导结论时真正用到了哪些假设。下面这个“证明”里，第二个前提其实没派上用场：

| 1. | $A_{\{1\}}$ | 假设 |
| --- | --- | --- |
| 2. | $B_{\{2\}}$ | 假设 |
| 3. | $(A \rightarrow B)_{\{3\}}$ | 假设 |
| 4. | $B_{\{1,3\}}$ | $1,3, \rightarrow$ E |

这个“证明”其实只说明：从 $A$ 与 $A \rightarrow B$ 推出 $B$ 是相干有效的。结论下标里没有数字 2，可见第二个“前提”并不真的算前提。

同理，要相干地证明一个蕴涵，对前件的假定就必须真正用来证明结论。下面是一个证明蕴涵的例子：

| 1. | $A_{\{1\}}$ | 假设 |
| --- | --- | --- |
| 2. | $(A \rightarrow B)_{\{2\}}$ | 假设 |
| 3. | $B_{\{1,2\}}$ | $1,2, \rightarrow$ E |
| 4. | $((A \rightarrow B) \rightarrow B)_{\{1\}}$ | $2,3, \rightarrow$ I |
| 5. | $A \rightarrow((A \rightarrow B) \rightarrow B)$ | $1,4, \rightarrow$ I |

像证明第 4、5 行那样解除假设时，该假设的编号必须确实出现在那个将要充当蕴涵后件的公式的下标里。

乍看之下，索引系统似乎会让不相干的前提混进来。最可能被钻空子的地方，是合取引入规则：好像总能这样塞进一个不相干的前提：

| 1. | $A_{\{1\}}$ | 假设 |
| --- | --- | --- |
| 2. | $B_{\{2\}}$ | 假设 |
| 3. | $(A \mathbin{\&} B)_{\{1,2\}}$ | 1,2, &I |
| 4. | $B_{\{1,2\}}$ | 3, &E |
| 5. | $(B \rightarrow B)_{\{1\}}$ | $2,4, \rightarrow$ I |
| 6. | $A \rightarrow(B \rightarrow B)$ | $1,5, \rightarrow$ I |

在相干逻辑学家看来，第一个前提在这里完全多余。为堵住这类动作，Anderson 与 Belnap 把合取引入规则写成：

由 $A_i$ 与 $B_i$ 推出 $(A \mathbin{\&} B)_i$。

这条规则的意思是：两个公式要合取，必须先有相同的索引，才能用合取引入。

自然演绎系统当然远不止这些（见 Anderson and Belnap 1975；Anderson, Belnap, and Dunn 1992）[^anderson-1975]，但对我们来说已经够用。至少某些相干逻辑所刻画的相干理论，可以从相应自然演绎系统如何记录“前提的真正使用”来理解。

## 5 相干逻辑的若干系统

Anderson 与 Belnap 的工作里，相干逻辑的中心系统是相干衍推逻辑 $\mathbf{E}$ 和相干蕴涵系统 $\mathbf{R}$。两者的关系是：$\mathbf{E}$ 的衍推联结词被设想为严格（即必然化）的相干蕴涵。为作比较，Meyer 给 $\mathbf{R}$ 加了一个必然性算子，得到逻辑 $\mathbf{NR}$。但 Larisa Maksimova 发现，$\mathbf{NR}$ 与 $\mathbf{E}$ 有重要差别——有些 $\mathbf{NR}$ 的定理（按自然翻译）并不是 $\mathbf{E}$ 的定理。这让一些相干逻辑学家犯了难：究竟该把 $\mathbf{NR}$ 还是 $\mathbf{E}$ 当作相干衍推系统？若选 $\mathbf{E}$，那么“衍推就是相干蕴涵加逻辑必然性”的说法也许就不合理了；衍推与蕴涵的关系可能另有讲法。

另一方面，也有相干逻辑学家把 $\mathbf{R}$ 与 $\mathbf{E}$ 一并拒斥。Arnon Avron 等人接受比 $\mathbf{R}$ 更强的逻辑（Avron 1990）[^avron-1990]；Ross Brady、John Slaney、Steve Giambrone、Richard Sylvan、Graham Priest、Greg Restall 等人则主张接受比 $\mathbf{R}$ 或 $\mathbf{E}$ 更弱的系统。Robert Meyer 与 Errol Martin 的逻辑 $\mathbf{S}$ 极弱：据 Martin 证明，它没有任何形如 $A \rightarrow A$ 的定理。换句话说，按 $\mathbf{S}$ 的说法，没有命题蕴涵自身，“$A$，所以 $A$”这种论证也不有效。于是，这个逻辑不让任何循环论证成为有效。

关于这些逻辑的更多细节，见[逻辑 $\mathbf{E}$](logic-relevance.logice.md)、[逻辑 $\mathbf{R}$](logic-relevance.logicr.md)、[逻辑 $\mathbf{NR}$](logic-relevance.logicnr.md)、[逻辑 $\mathbf{S}$](logic-relevance.logics.md) 四份补充材料。

较弱系统的一个好处是：与 $\mathbf{R}$、$\mathbf{E}$ 不同，它们中有许多可判定。有些较弱逻辑还有一点很吸引人——能用来构造朴素集合论。朴素集合论把朴素概括公理当作定理，即对一切公式 $A(y)$，

$\exists x\forall y(y \in x \leftrightarrow A(y))$。

在基于 $\mathbf{E}$、$\mathbf{R}$ 这类强相干逻辑的集合论里，和经典集合论一样，一旦加入朴素概括公理，就能推出任何公式。所以，基于 $\mathbf{E}$、$\mathbf{R}$ 等系统的朴素集合论被称作“平凡的”。下面用逻辑 **R** 的推理原则，粗略说明朴素集合论为何平凡。设 $p$ 为任意命题：

| 1. | $\exists x\forall y(y \in x \leftrightarrow(y \in y \rightarrow p))$ | 朴素概括 |
| --- | --- | --- |
| 2. | $\forall y(y \in z \leftrightarrow (y \in y \rightarrow p))$ | 1，存在例化 |
| 3. | $z \in z \leftrightarrow(z \in z \rightarrow p)$ | 2，全称例化 |
| 4. | $z \in z \rightarrow(z \in z \rightarrow p)$ | 3，$\leftrightarrow$ 的定义、合取消去 |
| 5. | $(z \in z \rightarrow (z \in z \rightarrow p)) \rightarrow(z \in z \rightarrow p)$ | 收缩公理 |
| 6. | $z \in z \rightarrow p$ | 4,5，肯定前件 |
| 7. | $(z \in z \rightarrow p)) \rightarrow z \in z$ | 3，$\leftrightarrow$ 的定义、合取消去 |
| 8. | $z \in z$ | 6,7，肯定前件 |
| 9. | $p$ | 6,8，肯定前件 |

这样便表明，这个朴素集合论能推出任意命题——这就是臭名昭著的柯里悖论。正因如此，Grishen、Brady、Restall、Priest 等人放弃了收缩公理 $((A \rightarrow (A \rightarrow B)) \rightarrow(A \rightarrow B))$。Brady 证明，从 $\mathbf{R}$ 中去掉收缩公理以及另外几条关键论题，所得逻辑可以接受朴素概括而不致平凡（Brady 2005）[^brady-2005]。

用自然演绎系统的话说，有收缩就等于允许一个前提被用上不止一次。看下面这个证明：

| 1. | $A \rightarrow(A \rightarrow B)_{\{1\}}$ | 假设 |
| --- | --- | --- |
| 2. | $A_{\{2\}}$ | 假设 |
| 3. | $A \rightarrow B_{\{1,2\}}$ | $1,2, \rightarrow$ E |
| 4. | $B_{\{1,2\}}$ | $2,3, \rightarrow$ E |
| 5. | $A \rightarrow B_{\{1\}}$ | 2–$4, \rightarrow$ I |
| 6. | $(A \rightarrow(A \rightarrow B)) \rightarrow (A \rightarrow B)$ | 1–$5, \rightarrow$ I |

收缩之所以推得出来，是因为下标用的是集合：我们不记录一个假设在推导中用了几次（超过一次也算一次）。要拒斥收缩，就得数清假设用了几次。所以无收缩系统的自然演绎系统改用相干数字的“多重集”而非集合——在这种结构里，某个数字出现几次要算，出现顺序不算。还能构造更弱的系统，连假设的使用顺序也记录下来（见 Read 1986；Restall 2000）[^restall-2000]。

三个较知名、用得也较广的弱相干逻辑 $\mathbf{B}, \mathbf{DK}$ 与 $\mathbf{DJ}$，见相应补充材料：

[逻辑 $\mathbf{B}, \mathbf{DJ}$ 与 $\mathbf{DK}$](logic-relevance.logic-b-dj-dk.md)。

## 6 与主流相干逻辑密切相关的系统

有些系统称得上 **相干**，却不属于主流相干逻辑，Graham Priest 的逻辑 N$_4$ 就是一例。要介绍它，最方便的办法是讲它的语义。

N$_4$ 的模型由一个世界集合构成，集合分成正规世界与非正规世界。在每个世界，合取、析取、否定按上文第 2 节讲的 Dunn 语义赋予四个真值之一。蕴涵的处理则相当有意思：在正规世界，蕴涵 $A\rightarrow B$ 为真，当且仅当凡世界 w 使 $A$ 为真，$B$ 也为真；只要有一个世界使 $A$ 真而 $B$ 假，蕴涵即为假。在非正规世界，蕴涵的真假则是随机指定的。

N$_4$ 是相干逻辑，具备变量共享性质，语义也非常简单直观。但它很弱：没有任何蕴涵传递公理，只有一条传递规则；既没有逆否公理，也没有逆否的规则形式。

另一个很有意思的逻辑是 Neil Tennant 的核心逻辑。相干逻辑原本要避开的一个“谬误”是 ex falso quodlibet，也就是爆炸：从矛盾推出随便什么命题。C.I. Lewis 曾用一个小论证替爆炸辩护。他以 $p \mathbin{\&} \neg p$ 为前提，由合取消去得 $p$，再由析取引入得 $p\vee q$；又从前提经合取消去得 $\neg p$。于是有了 $p\vee q$ 和 $\neg p$，再经析取三段论推出 $q$。主流相干逻辑学家拒斥析取三段论，以此堵住这个论证；但拒斥析取三段论，也成了相干逻辑最受争议的一点。

但 Tennant 的核心逻辑接受析取三段论，也接受合取消去与析取引入。事实上，直觉主义逻辑证明论里的标准初始规则，核心逻辑全都支持；因此可以说，核心逻辑中联结词的意义就是它们在直觉主义逻辑中的意义。差别在于对一条结构规则的处理：它拒斥最一般形式的逻辑后承传递性。

还有一个与相干逻辑密切相关的系统，是 William Parry 的分析蕴涵逻辑。分析蕴涵要满足一种极强的变量共享：除非 $B$ 中的 $\mathbf{all}$（全部）变量都包含在 $A$ 中，任何蕴涵 $A\rightarrow B$ 都不可证。为满足这条强原则，析取引入得受限制：$A\rightarrow(A\vee B)$ 不再对所有公式 $A$、$B$ 都是定理，而只在 $B$ 的所有命题变元也都在 $A$ 中时才有效。逆否原则和某些蕴涵传递原则同样要受限制。

Kit Fine 为分析蕴涵给出了优雅的可能世界语义：他在可能世界模型上增加一个“题材”域。蕴涵在世界成立，当且仅当它在所有可及世界都保真，并且后件的每个题材也都属于前件的题材（Fine 1986）[^fine-1986]。

分析蕴涵与相干逻辑的比较，见 Routley 等（1982，第 96–101 页）；对分析蕴涵的详细考察与辩护，见 Ferguson（2017）。

## 7 相干逻辑的应用与扩展

相干逻辑的动机，本在于更好地形式化我们前形式的蕴涵、衍推概念，并为朴素集合论提供基础；除此之外，它在哲学与计算机科学中还有不少用途。这里只举几例。

Dunn 以相干逻辑为基础，提出了一种关于内在属性与本质属性的理论，即他的 **相干谓述** 理论。简单说，事物 $i$ 相干地具有属性 $F$，当且仅当 $\forall x(x{=}i \rightarrow F(x))$。用大白话说，一个对象相干地具有某属性，是指“是那个东西”相干地蕴涵“具有那个属性”。相干蕴涵后件为真，本身不足以保证整个蕴涵为真，所以事物既可以相干地具有属性，也可以不相干地具有属性。Dunn 的表述似乎至少抓住了“内在属性”的一种用法。若在语言中加入模态，还可把本质属性形式化为既必然又内在地具有的属性（见 Anderson, Belnap, and Dunn 1992, §74）。

相干逻辑也被用作集合论之外其他数学理论的基础。Meyer 以逻辑 $\mathbf{R}$ 为基础，造出皮亚诺算术的一个变体，并给出有穷性证明：他的相干算术不以 $0 = 1$ 为定理。这样，Meyer 就在相干算术的范围内解决了 Hilbert 的一个核心问题——用有穷手段表明相干算术绝对一致。相干皮亚诺算术因此成为一个极有意思的理论。可惜，正如 Meyer 与 Friedman 所示，相干算术并不包含经典皮亚诺算术的全部定理，所以不能由此推出经典皮亚诺算术绝对一致（见 Meyer and Friedman 1992）[^meyer-1992]。

Anderson（1967）以 $\mathbf{R}$ 为基础构造了一个道义逻辑系统；后来 Mares（1992）与 Lou Goble（1999）也以相干逻辑为基础建立道义逻辑。这些系统避开了传统道义逻辑的一些标准麻烦。麻烦之一，是标准道义逻辑会让“$A$ 是定理，所以 $OA$ 是定理”这条推理有效，其中“$OA$”表示“应当 $A$”。病根在于如今通常把道义逻辑当作正规模态逻辑：按模态逻辑的标准语义，$A$ 有效就在所有可能世界为真；而 $OA$ 在世界 $a$ 为真，当且仅当 $A$ 在一切可及于 $a$ 的世界为真。于是 $A$ 有效，$OA$ 也有效。但说每个有效公式都应当成立，未免荒唐——凭什么“现在厄瓜多尔在下雨或没下雨”应当成立呢？相干逻辑的语义里，并非每个世界都使有效公式为真，只有一类特殊世界（有时叫“基础世界”，有时叫“正规世界”）才使有效公式为真，任何有效公式都可以在某个世界失败。把这类“非正规世界”放进模型，这条有问题的规则便失效了。

相干逻辑还被加上了其他种类的模态算子。Fuhrmann（1990）把经典模态逻辑的常见公理改造成相干版本，得到一批相干模态逻辑，并证明了完全性。Heinrich Wansing（2002）、Marta Bilkova、Ondrej Majer、Michal Peliš、Greg Restall（2010）等人给相干逻辑加入了认识模态算子；Shawn Standefer（2019）造出辩护逻辑的相干版本，最近又给相干逻辑添了现实性算子。甚至还有关于问与答的相干逻辑（见 Punčochář 2020）[^punčochář-2020]。

Routley 与 Val Plumwood（1989）、Mares 与 André Fuhrmann（1995）提出了基于相干逻辑的反事实条件句理论。他们在标准 Routley–Meyer 语义上增加了一个可及关系，它成立于一个公式与两个世界之间。按 Routley 与 Plumwood 的语义，$A\gt B$ 在世界 $a$ 成立，当且仅当凡满足 $SAab$ 的世界 $b$，$B$ 都在 $b$ 成立。Mares 与 Fuhrmann 的语义稍复杂：$A\gt B$ 在世界 $a$ 成立，当且仅当凡满足 $SAab$ 的世界 $b$，$A \rightarrow B$ 都在 $b$ 成立（两种语义的细节见 Brady (ed.) 2002, §10）。Mares（2004）提出了一套更复杂的相干条件句理论，其中包含反事实条件句。这些理论都避开了标准反事实逻辑中蕴涵悖论的对应物。

相干逻辑不只用于哲学，也用于计算机科学。线性逻辑——Jean-Yves Girard 开创的一个逻辑分支——是计算资源的逻辑。线性逻辑学家把蕴涵 $A \rightarrow B$ 读作：拥有类型 $A$ 的资源，就能得到类型 $B$ 的东西。因此，若有 $A \rightarrow(A \rightarrow B)$，便知可以从两份类型 $A$ 的资源得到一个 $B$；但这并不意味着能从单份类型 $A$ 的资源得到 $B$，也就是说，不知道能否得到 $A \rightarrow B$。所以收缩在线性逻辑中失效。线性逻辑其实就是缺少收缩、也缺少合取对析取分配律 $((A \mathbin{\&}(B \vee C)) \rightarrow((A \mathbin{\&} B) \vee(A \mathbin{\&} C)))$ 的相干逻辑。它还有两个算子（! 与 ?），称为“指数”：把指数加在公式前面，就好像让该公式取得“经典”行事的资格。例如，在标准相干逻辑中，通常不能只给有效推理添一个前提还让它保持有效；但加上形如 $!A$ 的前提，就总能保持有效。线性逻辑对形如 $!A$ 的公式还有收缩，即 $(!A \rightarrow(!A \rightarrow B)) \rightarrow(!A \rightarrow B)$ 是这些逻辑的定理（见 Troelstra 1992）[^troelstra-1992]。! 的用处，是处理“可以随意复制或忽略”的资源（Restall 2000, p 56）[^restall-2000]。线性逻辑的更多内容，见“子结构逻辑”词条。

## References（引用注释）

**以下文献从原文照录，不作翻译；中国文献译为中文。**

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

### Books on Relevance Logic and Introductions to the Field:

### Other Works Cited:

[^an-1992]: An extremely good, although slightly out of date, bibliography on relevance logic was put together by Robert Wolff and is in Anderson, Belnap, and Dunn (1992). What follows is a brief list of introductions to and books about relevant logic and works that are referred to above.
[^anderson-1975]: Anderson, A.R. and N.D. Belnap, Jr., 1975, *Entailment: The Logic of Relevance and Necessity*, Princeton, Princeton University Press, Volume I. Anderson, A.R. N.D. Belnap, Jr. and J.M. Dunn (1992) *Entailment*, Volume II. These are both collections of slightly modified articles on relevance logic together with a lot of material unique to these volumes. Excellent work and still the standard books on the subject. But they are very technical and quite difficult.
[^avron-2014]: Avron, A., 2014, “What is Relevance Logic?” *Annals of Pure and Applied Logic* 165:26–48. This paper puts forward a rather different view of what makes a relevance logic relevant.
[^beall-2012]: Beall, Jc, Ross Brady, J. Michael Dunn, A. P. Hazen, Edwin Mares, Robert K. Meyer, Graham Priest, Greg Restall, David Ripley, John Slaney and Richard Sylvan, 2012, “On the ternary relation and conditionality,” *Journal of Philosophical Logic*, 41(3): 595–612.
[^beall-2006]: Beall, JC, R. Brady, A. Hazen, G. Priest, and G. Restall, 2006, “Relevant Restricted Quantification,” *Journal of Philosophical Logic*, 35(6): 587–598.
[^brady-2005]: Brady, R.T., 2005, *Universal Logic*, Stanford: CSLI Publications, 2005. A difficult, but extremely important book, which gives details of Brady’s semantics and his proofs that naïve set theory and higher order logic based on his weak relevant logic are consistent.
[^dunn-1986]: Dunn, J.M., 1986, “Relevance Logic and Entailment,” in F. Guenthner and D. Gabbay (eds.), *Handbook of Philosophical Logic* (Volume 3), Dordrecht: Reidel, pp. 117–24.
[^dunn-1986-2]: Dunn, J.M. and G. Restall, “Relevance Logic” in D. Gabbay & F. Guenthner (eds.), *Handbook of Philosophical Logic* (Volume 6), second edition, Dordrecht: Springer, pp. 1–128. An updated and greatly expanded version of Dunn (1986).
[^mares-2004]: Mares, E.D., 2004, *Relevant Logic: A Philosophical Interpretation*, Cambridge: Cambridge University Press.
[^mares-2001]: Mares, E.D. and R.K. Meyer, 2001, “Relevant Logics,” in L. Goble (ed.), *The Blackwell Guide to Philosophical Logic*, Oxford: Blackwell.
[^norman-1988]: Norman, J. and R. Sylvan, 1988, *Directions in Relevant Logic*, Dordrecht: Kluwer. A good, although somewhat dated, collection of essays on relevance logic together with some on related logics, such as analytic implication.
[^paoli-2002]: Paoli, F., 2002, *Substructural Logics: A Primer*, Dordrecht: Kluwer. Excellent and clear introduction to a field of logic that includes relevance logic.
[^priest-2008]: Priest, G., 2008, *An Introduction to Non-Classical Logic: From If to Is*, Cambridge: University of Cambridge Press. A very good and extremely clear presentation of relevant and other non-classical logics that uses a tableau approach to proof theory.
[^read-1988]: Read, S., 1988, *Relevant Logic*, Oxford: Blackwell. A very interesting and fun book. Idiosyncratic, but philosophically adept and excellent on the pre-history and early history of relevance logic.
[^restall-2000]: Restall, G., 2000, *An Introduction to Substructural Logics*, London: Routledge. Excellent and clear introduction to a field of logic that includes relevance logic.
[^rivenc-2005]: Rivenc, François, 2005, *Introduction à la logique pertinente*, Paris: Presses Universitaires de France. In French. Gives a “structural” interpretation of relevant logic, which is largely proof theoretic. The structures involved are structures of premises in a sequent calculus.
[^routley-1982]: Routley, R., R.K. Meyer, V. Plumwood and R. Brady, 1982, *Relevant Logics and its Rivals* (Volume I), Atascardero, CA: Ridgeview. A very useful book for formal results especially about the semantics of relevance logics. The introduction and philosophical remarks are full of “Richard Routleyisms”. They tend to be Routley’s views rather than the views of the other authors and are fairly radical even for relevant logicians. Volume II updates Volume I and includes other topics such as conditionals, quantification, and decision procedures: R.Brady (ed.), *Relevant Logics and their Rivals* (Volum II), Aldershot: Ashgate, 2003.
[^goldblatt-2011]: Goldblatt, R., 2011, *Quantifiers, Propositions and Identity: Admissible Semantics for Quantified Modal and Substructural Logics*, Cambridge: Cambridge University Press. A detailed account of the admissible semantics for quantified logic, applied to both modal and relevance logic, and provides a new type of semantics for quantified relevance logic called the “cover semantics”.
[^jago-2013]: Jago, M., 2013, “Recent Work in Relevant Logic,” *Analysis*, 73: 526–541. A very clear survey of recent technical and philosophical work in relevance logic.
[^anderson-1967]: Anderson, A.R., 1967, “Some Nasty Problems in the Formal Logic of Ethics,” *Noûs*, 1: 354–360.
[^avron-1990]: Avron, Arnon, 1990, “Relevance and Paraconsistency — A New Approach,” *The Journal of Symbolic Logic*, 55: 707–732.
[^bilková-2010]: Bilková, M., O. Majer, M. Peliš, and G. Restall, 2010, “Relevant Agents” in L. Beklemishev, V. Gorenko, and V. Shehtman (eds.), *Advances in Modal Logic* (Volume 8), London: College Publications, 22–38.
[^barwise-1993]: Barwise, J., 1993, “Constraints, Channels and the Flow of Information,” in P.Aczel, et al. (eds.), *Situation Theory and Its Applications* (Volume 3), Stanford: CSLI Publications, pp. 3–27.
[^belnap-1982]: Belnap, N.D., 1982, “Display Logic,” *Journal of Philosophical Logic*, 11: 375–417.
[^brady-1989]: Brady, R.T., 1989, “The Non-Triviality of Dialectical Set Theory,” in G. Priest, R. Routley and J. Norman (eds.), *Paraconsistent Logic*, Munich: Philosophia Verlag, pp. 437–470.
[^dunn-1973]: Dunn, J.M., 1973, (Abstract) “A ‘Gentzen System’ for Positive Relevant Implication,” *The Journal of Symbolic Logic*, 38: 356–357.
[^dunn-1993]: –––, 1993, “Star and Perp,” *Philosophical Perspectives*, 7: 331–357.
[^dunn-2015]: –––, 2015, “The Relevance of Relevance to Relevance Logic” in M. Banerjee and S.N. Krishna (eds.), *Logic and its Applications: 6th Indian Conference, ICLA 2015Mumbai, India, January 8–10, 2015Proceedings*, Basel: Springer, pp. 11–29.
[^ferguson-2017]: Ferguson, T.M., 2017, *Meaning and Proscription in Formal Logic*, Basel: Springer.
[^fine-1974]: Fine, K., 1974, “Models for Entailment,” *Journal of Philosophical Logic*, 3: 347–372.
[^fine-1986]: –––, 1986, “Analytic Implication” *Notre Dame Journal of Formal Logic*, 27: 169–179.
[^fine-1988a]: –––, 1988a, “Incompleteness for Quantified Relevance Logic” in Norman and Sylvan (eds.), 1988, pp. 205–225.
[^fine-1988b]: –––, 1988b, “Semantics for Quantified Relevance Logic” *Journal of Philosophical Logic*, 17: 27–59.
[^fuhrmann-1990]: Fuhrmann, A., 1990, “Models for Relevant Modal Logics,” *Studia Logica*, 49: 501–514.
[^goble-1999]: Goble, L., 1999, “Deontic Logic with Relevance” in P. McNamara and H. Prakken (eds.), *Norms, Logis and Information Systems*, Amsterdam: ISO Press, pp. 331–346.
[^grishin-1974]: Grishin, V.N., 1974, “A Non-Standard Logic and its Application to Set Theory,” *Studies in Formalized Languages and Non-Classical Logics* (Russian), Moscow: Nauka.
[^israel-1990]: Israel, D. and J. Perry, 1990, “What is Information?,” in P.P. Hanson (ed.), *Information, Language, and Cognition*, Vancouver: University of British Columbia Press, pp. 1–19.
[^logan-2019]: Logan, S.A., 2019, “Notes on Stratified Semantics” *Journal of Philosophical Logic*, 48: 479–486.
[^maccoll-1908]: MacColl, H., 1908, “‘If’ and ‘imply’,” *Mind*, 17: 151–152, 453–455.
[^mares-1992]: Mares, E.D., 1992, “Andersonian Deontic Logic,” *Theoria*, 58: 3–20.
[^mares-1997]: –––, 1997, “Relevant Logic and the Theory of Information,” *Synthese*, 109: 345–360.
[^mares-2004a]: –––, 2004a, ““Four-Valued” Semantics for the Relevant Logic R” *Journal of Philosophical Logic*, 33: 327–341.
[^mares-1995]: Mares, E.D. and A. Fuhrmann, 1995, “A Relevant Theory of Conditionals,” *Journal of Philosophical Logic*, 24: 645–665.
[^mares-2006]: Mares, E.D. and R. Goldblatt, 2006, “An Alternative Semantics for Quantified Relevant Logic” *The Journal of Symbolic Logic*, 71: 163–187.
[^meyer-1992]: Meyer, R.K. and H. Friedman, 1992, “Whither Relevant Arithmetic?,” *The Journal of Symbolic Logic*, 57: 824–831.
[^omori-2017]: Omori, H. and H. Wansing (eds.), 2017, “40 years of FDE: An Introductory Overview” *Studia Logica*, 105: 1021–1049.
[^punčochář-2020]: Punčochář, V., 2020, “A Relevant Logic of Questions” *Journal of Philosophical Logic*, 49: 905–939. doi:10.1007/s10992-019-09541-9
[^rantala-1982]: Rantala, V., 1982, “Quantified Modal Logic: Non-Normal Worlds and Propositional Attitudes,” *Studia Logica*, 41: 41–65.
[^restall-1995]: Restall, G., 1995, “Four-Valued Semantics for Relevant Logics (and Some of their Rivals)” *Journal of Philosophical Logic*, 24: 139–160.
[^restall-1996]: –––, 1996, “Information Flow and Relevant Logics,” in J. Seligman and D. Westerstahl (eds.), *Logic, Language and Computation* (Volume 1), Stanford: CSLI Publications, pp. 463–478.
[^routely-1972]: Routely, R., and V. Routley, 1972, “The Semantics of First Degree Entailment,” *Noûs*, 6(4): 335–369.
[^routely-1980]: Routely, R., 1980, “Problems and Solutions in the Semantics of Quantified Relevant Logics, I” in A.I. Arruda, R. Chuaqui, N.C.A. Da Costa (eds.), *Mathematical Logic in Latin America* Amsterdam: North Holland, 1980, pp. 309–340.
[^routley-1978]: Routley, R. and A. Loparic, 1978, “Semantical Analysis of Arruda-da Costa P Systems and Adjacent Non-Replacement Relevant Systems,” *Studia Logica*, 37: 301–322.
[^sperber-2002]: Sperber, D. and D. Wilson, 2002, “Relevance Theory” in L. Horn & G. Ward (eds.), *The Handbook of Pragmatics*, Oxford: Blackwell, pp. 607–632.
[^standefer-2019]: Standefer, S., 2019, “Tracking Reasons with Extensions of Relevant Logics” *Logic Journal of the IGPL*, 27: 543–569.
[^tennant-2017]: Tennant, Neil., 2017, *Core Logic*, Oxford: Oxford University Press.
[^troelstra-1992]: Troelstra, A.S., 1992, *Lectures on Linear Logic*, Stanford: CSLI Publications.
[^urquhart-1972]: Urquhart, A., 1972, “Semantics for Relevant Logics” *The Journal of Symbolic Logic*, 37: 159–169.
[^wansing-2001]: Wansing, H., 2001, “Negation,” in L. Goble (ed.), *The Blackwell Guide to Philosophical Logic*, Oxford: Blackwell, pp. 415–436.
[^wansing-2002]: –––, 2002, “Diamonds are a Philosopher’s Best Friends,” *Journal of Philosophical Logic*, 31: 591–612.
[^weber-2010]: Weber, Z., 2010, “Extensionality and Restriction in Naive Set Theory” *Studia Logica*, 94: 87–104.

## 学术工具

* [如何引用本词条](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=logic-relevance)。
* [预览本词条的 PDF 版本](https://leibniz.stanford.edu/friends/preview/logic-relevance/)，见 [SEP 学会之友](https://leibniz.stanford.edu/friends/)。
* 在 [InPhO](https://www.inphoproject.org/entity?sep=logic-relevance&redirect=True) 查找与本词条相关的话题与思想家。
* 在 [PhilPapers](https://philpapers.org/sep/logic-relevance/) 查看本词条的增强文献目录及其数据库链接。

## 其他网络资源

- Jago, M., forthcoming, “[相干逻辑的真值制造者语义](https://link.springer.com/article/10.1007/s10992-019-09533-9)”，*Journal of Philosophical Logic*，2020 年 1 月 7 日首次在线，doi:10.1007/s10992-019-09533-9。[本文以 Kit Fine 的真值制造者理论为基础，为相干逻辑建立一种语义。]

## 相关词条

双面真理论 | 直觉主义逻辑 | 模态逻辑 | 次协调逻辑 | 子结构逻辑 | 不一致数学 | 否定

**（译注：相关词条的中文站内链接将由管线在对应词条重译完成后统一挂接。）**

## 致谢

作者感谢匿名审稿人与 Shawn Standefer 提出修正和改进建议。
