# 逻辑后承 Logical Consequence (Jc Beall, Greg Restall, and Gil Sagi)

*首次发表于 2005 年 1 月 7 日；2024 年 5 月 17 日实质修订。*

好论证，就是结论能从前提得出的论证；结论是前提的 **后承**，或被前提所 **蕴涵**。可“从前提得出”到底是什么意思？说结论是前提的 **后承**、被前提 **蕴涵**，又是什么意思？这些问题在许多方面都是逻辑学（作为一门哲学学科）的核心。本词条主要用“结论 **从前提得出**”“是前提的 **后承**”来谈，因为 **蕴涵**（entailment）一词在哲学与逻辑的其他场合，有时另有含义或含义更强。

看下面这个论证：

1. 如果大学收费高昂，只有富人会入学。大学收费高昂。所以，只有富人会入学。

这个论证可说的很多，但多数人同意：只要不含混其词（前提和结论里词项意义相同），这个论证就 **有效**——结论演绎地从前提得出。这不等于说结论为真；前提可能不真。但只要前提为真，结论就也为真，这是凭逻辑保证的。本词条谈的，就是有效论证里前提与结论的关系。

当代对后承概念（“从……得出”这一关系）的分析，把它同时视为 **必然的** 和 **形式的**；相关回答常借 **证明** 或 **模型**（有时兼用二者）来阐明。本文的目的是简要刻画当代逻辑后承理论中的几个核心概念。

要说明的是，这里只挑逻辑后承的少数 **哲学** 问题来谈，技术细节几乎全部略去，哲学争论也只留了一角。理由是：技术细节及其背后的哲学动机，从考察 **具体逻辑**——具体的后承理论，比如相干逻辑、子结构逻辑、非单调逻辑、动态逻辑、模态逻辑、量化理论等——中能学得更透。（再说，凡涉及语言特征的争论——句子的结构与形式、命题、语境敏感性、意义，甚至真——都牵连逻辑后承的争论，想面面俱到实际做不到。）这里只打算碰到几个最基本的问题。

## 1 演绎后承与归纳后承

有些论证，前提（合在一起）为真就 **必然足以** 保证结论为真。按眼下传统里最核心的 **逻辑后承** 观念，“必然的充分性”正是演绎有效与归纳有效之分。归纳有效的论证，前提（合在一起）为真 **很可能（但并非必然）足以** 保证结论为真；用常说的话说，前提使结论更可能、更有理由成立（即使前提全真，结论仍可能不真）。比如论证

1. 迄今观察到的天鹅都是白的。Smoothy 是一只天鹅。所以，Smoothy 是白的。

这个论证演绎上不有效：前提对结论并非必然充分——Smoothy 完全可能是只黑天鹅。

归纳论证彼此有别：有的看着相当合理，有的差些。分析归纳后承的途径很多。可以看前提把结论弄得 **多可能**（概率式读法），也可以看让前提为真的最 **正常** 情境是否也使结论为真（这就通向某些默认推理或非单调推理）。归纳后承领域既难又重要，但这里放下不谈，专讲 **演绎** 有效性。

（更多内容见“归纳逻辑”与“非单调逻辑”词条。）

只有 **必然性** 这一约束，还定不下演绎有效性概念——**必然性** 本身可以充实出好几种讲法。说结论必然从前提得出，是说论证在某种意义上 **没有例外**；可把这个想法做精确的办法不止一种。

第一条路子，可以用今天所谓的形而上学必然性。也许可以这样说：若“前提真而结论不真” **（在形而上学上）不可能**，论证即有效——也就是说，固定前提与结论的解释之后，凡前提成立的可能世界，结论都成立。这条约束被合理地当作逻辑后承的必要条件（若 **可能** 前提真而结论不真，结论当然不从前提得出）；但按多数后承理论，它不是充分条件。许多人承认存在 **后验** 必然真理，如“水是 H$_2$O”。若这话必然，则论证：

1. $x$ 是水。所以，$x$ 是 H$_2$O。

它必然保真，却离演绎有效差得很远。“水是 H$_2$O”是真发现，靠大量经验研究得来。有效的论证也可能被我们真正“发现”（从前没认出来），但要说这类发现也得靠经验研究，就是另一码事了。

另一条路线转向 **概念必然性**。按此说，(3) 的结论不是前提的后承：“水是 H$_2$O”并非概念真理。概念 **水** 和概念 $H_2O$ 碰巧指称同一属性，但这种巧合部分取决于世界。

与之相近的一种逻辑观，把后承归结为 **分析地** 为真的东西；而“水是 H$_2$O”不是分析真理。“水”这个词和公式“H$_2$O”外延相同（且必然相同），但 **意义** 不同。

若嫌形而上学必然性太粗，定不下逻辑后承（它可能把太多论证都算成演绎有效），诉诸概念或分析必然性似乎更好。麻烦是，正如 Quine 所论：分析与综合（概念与非概念亦然）之分，并不像 20 世纪初人们以为的那么干脆。（见“分析/综合区分”词条。）何况许多论证单凭分析就保真：

1. Peter 是 Greg 的母亲的兄弟的儿子。所以，Peter 是 Greg 的表亲。

只要懂这些概念，就能看出结论从前提得出；无须知道 Peter 或 Greg 的表亲是谁。尽管如此，许多人还是不认 (4) 为演绎有效，哪怕它靠分析或概念理由保真。它的毛病是不够 **形式**、不够普遍：论证能成立，全靠“母亲”“兄弟”“儿子”“表亲”这些家族概念的具体细节。

还有一种刻画 **必然性** 的办法，是诉诸 **先验性**。演绎有效的论证，不管长什么样，都能不经经验而知其有效，也就是 **先验** 可知。这条约束当然能合理地把 (3) 挡在演绎有效之外——排得对。可它挡不住 (4)。若认为 (4) 这类论证涉及的并非演绎有效性，而是别的什么，比如 **先验** 可知的定义，那就得另找刻画逻辑后承的路子。

## 2 形式后承与实质后承

给逻辑后承找更窄判据的最强、最通行方案，是诉诸 **形式性**。(4) 里从“Peter 是 Greg 的母亲的兄弟的儿子”到“Peter 是我的表亲”那一步是 **实质** 后承，不是形式后承：光靠主张的 **结构** 或 **形式** 走不到结论，还得懂它们的 **内容**。

**形式** 与 **内容** 之分到底指什么？我们想说的是：后承若只取决于主张的 **形式** 而非 **实质**，便是形式的。可这又怎么理解？这里只能勾个轮廓，往深处充实同样有多种办法。

头一步显而易见：逻辑后承 **规则** 的各种表述都靠图式。亚里士多德的三段论就是现成的光荣例子。

F*e*r*io*：没有 $F$ 是 $G$。有的 $H$ 是 $G$。所以有的 $H$ 不是 $F$。

上面这样的推理图式，展示有效论证的结构。说论证形式有效，也许就是说：它落入某个一般图式，而这个图式的每个实例都有效——F*e*r*io* 就是一例。

但这样刻画形式性仍不完备。实质论证 (4) 其实是下面图式的实例：

1. $x$ 是 $y$ 的母亲的兄弟的儿子。所以，$x$ 是 $y$ 的表亲。

这个图式的每个实例都有效。但要说清为什么有的图式算真正形式的（从而足以支撑逻辑后承），有的不算，还得讲更多。一般的答案要阐明“逻辑形式”这个概念——它本身就是个大问题（牵涉逻辑常项等）。我们不去细抠逻辑形式的各家候选，而改谈这项工作的 **目的** 何在。

要求有效性由逻辑形式撑着，图的是什么？所需的形式性概念至少有三种不同提案，每种对此给出不同回答。

一种看法是：逻辑的形式规则对 **对象** 的具体特征完全 **中立**。按此说，逻辑规律必须从对象的具体特征中抽象出来；逻辑之所以是形式的，就因为它完全 **一般**。要刻画什么叫完全 **一般** 的概念，一个办法是借置换。Tarski（1986）提出：一个域上的运算或谓词，若在对象置换下不变，就算一般的（或逻辑的）。（集合中对象的置换，给每个对象指派该集合里唯一一个对象，且没有对象被指派两次。比如 $\{a, b, c, d\}$ 的一个置换，可以把 $b$ 指定给 $a, d$ 指定给 $b, c$ 指定给 $c$、把 $a$ 指定给 $d$。）$2$ 元谓词 $R$ 置换不变，是指对任何置换 $p$，凡 $Rxy$ 成立，$Rp(x)p(y)$ 也成立。看得出来，**同一** 关系置换不变——若 $x = y$，则 $p(x) = p(y)$——但 **……的母亲** 关系不是：可能存在置换 $p$，使 $x$ 是 $y$ 的母亲，$p(x)$ 却不是 $p(y)$ 的母亲。置换还能用来刻画谓词之外的逻辑性：说一元语句联结词“$\bullet$”置换不变，当且仅当对所有 $A$，$p(\bullet A)$ 为真当且仅当 $\bullet p(A)$ 为真。要严格定义这一点，得先说明置换如何作用于句子，这超出本文范围。只说一句：否定这类运算能通过不变性检验，“JC 相信”这类运算通不过。

另一种密切相关的形式性分析是：形式规则完全 **抽象**，从思想或主张的语义 **内容** 中抽走，只留下语义结构。“母亲”“表亲”这些词项是本质地进入论证 (5) 的。按此说，命题联结词、量词这类表达式不增添新的语义内容，只增添组合、组织语义内容的方式；“母亲”“表亲”这类表达式则增添新内容。

还有一种分法（也许分的是另一件事）：把逻辑形式规则看作思想的 **构成性规范**，不管思想关于什么。无论我们想的是什么，把思想合取、析取、否定，造出新思想，都说得通；量化大概也说得通。于是逻辑词汇的行为能用来组织和调节 **任何** 理论，支配逻辑词汇的规范普遍适用。按这幅图景，有效论证的规范，就是不管思想具体内容如何都管用的规范。[^note-1]

## 3 数学工具：模型与证明

20 世纪围绕逻辑后承的 **技术** 工作，集中在两件数学工具上：证明论与模型论。两者各自阐明后承概念的不同侧面，背后也各有哲学立场。

### 3.1 逻辑后承的模型论说明

我们把逻辑后承刻画为 **凭形式而必然保真**。这个想法可以形式地讲清楚：用数学结构来涵盖需要保真的种种可能性；再给逻辑词汇一个特殊地位，把它当作句子形式的构成成分，从而形式地说明后承的形式性。下面看模型论怎样同时应付这两件事。

逻辑后承的 **以模型为中心的进路**，把论证有效看作 **没有反例**。一般说，论证的 **反例** 就是显示前提 **推不出** 结论的某种方式。可以给出同形式、前提明显真而结论明显假的论证；也可以给出一种 **境况**，其中前提真、结论假。当代文献把反例这个直观想法发展成了 **模型** 理论。

模型的具体结构取决于语言的种类（外延/内涵、一阶/高阶等）。外延一阶语言的模型包括一个非空集合，即 **域**；还包括一个 **解释函数**。它给每个非逻辑词项指定域上的一个外延，只要与其语义类型相符即可（个体常项指派域中元素，函数符号指派域到自身的函数，一元一阶谓词指派域的子集，等等）。

当代模型论的后承定义可追溯到 Tarski（1936），它建立在 Tarski（1935）的 **模型中的真** 定义上。Tarski 给逻辑词汇规定真（或满足）条件，递归地定义 **模型中的真句子**：比如合取在模型中为真，当且仅当两个合取项在该模型中都真；全称量化句 $\forall xFx$ 在模型中为真，当且仅当其每个实例在模型中为真（按 Tarski 的满足说明，则是开公式 $Fx$ 被模型中域的所有对象满足；细节见“Tarski 真定义”词条）。于是，逻辑后承可定义为模型上的保真：在任何使前提为真的 **模型** 中（或按任何使前提为真的 **解释**），结论也为真，论证就有效。

模型论定义是迄今对哲学概念最成功的数学阐明之一。它似乎既能抓住后承的必然性（看所有模型中的真），又能抓住形式性（在各模型间改变非逻辑词汇的解释：非逻辑词汇无论什么意思，论证都有效）。可模型只是集合，只是数学对象，它们凭什么说明所需的那一范围可能性或境况？John Etchemendy（1990）提出两种理解模型的视角。按 **表象进路**，每个模型表象一个可能世界；论证若在模型上保真，就保证在可能世界上保真，再把必然性等同于在所有可能世界中为真，便得到后承的必然保真。问题是：这把逻辑后承等同于形而上学后承，也没说明形式性——按表象进路，逻辑词汇与非逻辑词汇无从区分，也解释不了为什么非逻辑词汇的解释要被尽量变化。另一视角是 **解释进路**：每个模型都从现实世界给非逻辑词汇指定外延，模型之间变的是词项意义，不是所描绘的世界。这里担心的是必然性没被抓住。比如按通常的逻辑/非逻辑词汇之分，同一性是逻辑词项，能构成关于域之基数的陈述（如“至少有两个东西”），这些陈述在每种重新解释下都真，却未必必然真。按这种进路，也没有根据去考虑域不同于实际存在总体的模型，尤其解释不了模型论为何使用不同大小的域。照上面的描述，两种进路在我们“必然且形式”的分析下各有缺陷：解释进路只盯现实世界，说明不了必然性；表象进路说明不了形式性（细节见 Etchemendy 1990、Sher 1996、Shapiro 1998；改进见 Etchemendy 2008）[^etchemendy-1990][^etchemendy-2008][^shapiro-1998][^sher-1996]。对 Etchemendy 的一种可能回应，是把两种视角融合：每个模型都在非逻辑词汇重新解释之下表象一个可能世界（Shapiro 1998；其他回应见 Sher 1996、Hanson 1997）[^hanson-1997][^shapiro-1998][^sher-1996]。

模型论定义的一大挑战，是区分逻辑词汇与非逻辑词汇。逻辑词汇在所有模型里由递归子句定义（如前文对合取、全称量词的处理），在这个意义上意义固定。选哪些逻辑词汇，就决定了评价有效性时考察哪一类模型，从而决定哪些论证逻辑有效。每种形式语言通常都带着某种逻辑词汇的选择，但人们仍可要求对逻辑词汇作更有原则的刻画。Tarski 1936 年把这问题搁下了，只给了相对主义立场的线索：逻辑词汇的不同选择都可允许。另一些人提出逻辑性判据，要求逻辑常项适当地形式、一般或中立于主题（文献与细节见“逻辑常项”词条）。要注意，选逻辑词汇只是给模型类加约束的特例；有人指出，只盯逻辑词汇判据会漏掉这一点，更一般的问题是采用哪些 **语义约束** 来限制语言的 **可容许模型**（Sagi 2014a, Zinke 2017）[^sagi-2014a]。

模型论说明还有一重困难：它的集合论基础有限。模型是集合，而模型上的保真未必保证必然保真，甚至未必保证实质保真（现实世界里的保真）。因为每个模型域都是集合，可现实世界大概包含所有集合；把所有集合收在一起的总体“太大”，不是集合（它是 **真类**），所以现实世界不被任何模型说明（见 Shapiro 1987）[^shapiro-1987]。

一种应对办法是借外部手段，比如证明论，来支撑模型论定义——Georg Kreisel 的“挤压论证”就是这么做的，见 3.3 节。该论证的关键，是所涉语言要有可靠且完全的证明系统。另一条路是用集合论反射原则：粗略说，凡对集合宇宙为真的，在它的某个初始段（总是一个集合）里已经为真。若接受反射原则，至少对相关语言可以论证：论证有效，当且仅当不存在反例集合模型（见 Kreisel 1967、Shapiro 1987、Kennedy & Väänänen 2017）[^kennedy-2017][^kreisel-1967][^shapiro-1987]。

最后，用模型中的真来解释后承，通常是“实在论者”的口味——他们认为句子真不真，与我们能知道什么无关。用模型中的真解释后承，离用 **真** 解释后承很近；而“模型中的真”有时被当作对符合论之真的阐明——符合论正是典型的实在论概念。但也有人认为，逻辑后承有不可或缺的认识成分，牵涉我们如何依据前提确立结论。“反实在论者”不肯把真（至少符合论的真）当作解释概念，通常更愿意用 **证明** 来解释后承——下面就说这个。

### 3.2 逻辑后承的证明论说明

按 **以证明为中心的进路**，论证有效，就在于存在从前提到结论的 **证明**。证明究竟 **是什么** 是大问题，但想法很朴素（只要你接触过某种证明系统）。证明由一小步一小步组成，即证明系统的原始推理原则。20 世纪涌现了名目繁多的证明系统：从规则简单、公理复杂的所谓希尔伯特证明，到公理很少（甚至没有）、规则一大堆的自然演绎系统。

以证明为中心的进路，突出后承的认识面。证明不只是在担保论证有效，它还给出我们据以确立有效性的步骤。所以，推理者若对前提有根据，又通过一串有效推理规则推出结论，就由此得到了结论的根据（见 Prawitz 2012）[^prawitz-2012]。还可以再进一层，接受 **推理主义**：表达式意义由其在推理中的角色决定。我们对语言表达式的使用受规则调节，掌握规则就足以理解表达式。这就先给语义值划了条线：凡规则未说明的区分，语义值都做不出来。再进一步，还可以拒斥一切超出规则的意义，采纳后期维特根斯坦的口号“意义即用法”。意义反实在论者偏爱这种看法，因为在这里意义完全由可知的东西解释。

在证明中心进路里，后承的必然性条件有了新读法：有效论证中，结论为真凭思想的必然性从前提为真得出（Prawitz 2005）[^prawitz-2005]。解析一下：**真** 作 **构造性** 理解——句子凭其 **潜在证据** 为真，真句子描述的事实也按潜在证据设想为构造出来的。（也可以完全绕开真，改谈句子的可断言性或可接受性。）论证借以有效的思想必然性，由所涉词项的意义解释：前提真，意义就逼着我们接受结论真。表达式的意义又靠其使用规则来理解：含该表达式的公式，通常的 **真值条件** 让位给 **证明条件**。

这样就能给语言配上 **证明论语义**（Schroeder-Heister 1991）[^schroeder-heister-1991]。Gentzen 呈现自然演绎系统时说过：逻辑表达式的引入规则代表其“定义”，消去规则是这些定义的后果（Gentzen 1933）。比如合取的引入规则规定，合取 $A \amp B$ 可从两个合取项 $A$、$B$ 推出，这条规则抓住了联结词的意义；消去规则反过来说，从 $A \amp B$ 可推出 $A$ 与 $B$。全称量词规则说：从 $\forall xFx$ 可推出任何实例 $Fa$；只要没有其他涉及名称 $a$ 的假定，也可从实例 $Fa$ 推出 $\forall xFx$。在一定条件下可以证明，消去规则得到引入规则的认可。

以证明为中心的进路，主要难题之一是分清哪些规则真正决定意义、哪些不。有些联结词规则一旦加入系统，系统就会平凡。Prior（1960）给联结词“$\tonk$”设了两条规则：引入规则说，从 $A$ 可推出 $A \tonk B$；消去规则说，从 $A \tonk B$ 可推出 $B$。加入这两条后，只要系统里至少能证一件事，就会平凡——因为从任何假定 $A$ 都能推出任何结论 $B$。所以必须给推理规则加约束，后来的文献很大一部分就在讨论这些约束（Belnap 1962, Dummett 1991, Prawitz 1974）[^dummett-1991][^belnap-1962][^prawitz-1974]。

为把证明与有效性讲得更系统，Prawitz 引入 **规范证明**。一个句子可以有多种证法，但直接证法即规范证明，才构成它的意义。规范证明的最后一步是引入规则的应用，且其直接子证明也规范（除非含自由变元或未解除的假定——细节见 Prawitz 2005）[^prawitz-2005]。规范证被视为给所证句子提供了直接证据：它凭构成联结词意义的规则确立句子为真。规范证明以及其他证明如何归约为它，见“证明论语义”词条。

上面说了必然性条件在证明中心进路里怎么解释，形式性条件也能交代。注意，这个视角下词汇照样分逻辑与非逻辑。用这个区分可以定义论证的 **代入**：把非逻辑词项统一换成同句法范畴的词项，所得论证就是原论证的代入。尊重形式性的有效性定义会蕴涵：论证有效，当且仅当其所有代入都有效；在这里，就是要求所有代入都有证明。只给逻辑词汇设规则的证明系统，都满足这一点。当然，证明中心进路同样要面对区分逻辑词汇的问题（见“逻辑常项”词条）。

最后要说，证明论语义不光能给经典逻辑，也能给各种非经典逻辑。不过，鉴于证明中心进路底下的认识论反实在论态度，其倡导者通常主张直觉主义逻辑（见 Dummett 1991）[^dummett-1991]。

证明中心视角与证明论语义的更多内容，见“证明论语义”词条。

### 3.3 模型与证明之间

过去人们把证明论视角与模型论视角看作关于后承的竞争对手。其实也可以把“逻辑后承”和“有效性”看作 **簇概念**：“若干不同而密切相关的概念共用这些名称；它们牵涉模态、意义、有效性、辩护、理性与形式”（Shapiro 2014）[^shapiro-2014]。还值得一提：模型论与证明论之分是现代的，得等元数学研究工具发展出来才可能有。比如 Frege 的 *Begriffsschrift* 早于这些工具，写成公理证明系统，可联结词的意义却用真值条件给。

有了后承关系的两种分析，就可以问它们如何互动——下面再说。也可以问：抛开证明论或模型论的分析，这种关系本身有什么一般特征？回答之一可追溯到 Tarski，他引入后承算子。这里只看这类算子的几个特征。设 $Cn(X)$ 为 $X$ 的后承。（可以把算子 $Cn$ 看成来自先在的后承关系：把 $X$ 作为“输入（或前提）”集，它告诉你从 $X$ 能推出什么。也可以倒过来看这个“过程”；一个关键洞见是，后承关系与相应算子实际上可相互定义。细节见“代数命题逻辑”词条。）对后承关系可以施加的最小条件，至少有下面两条（出自 Tarski）：

1. $X$ 是 $Cn(X)$ 的子集。
2. $Cn(Cn(X)) = Cn(X)$。

把 $X$ 想成一组主张，第一条就是说：一组主张的后承包含这些主张本身。第二条要求：$X$ 的后承就是 $X$ 的后承之后承。这两条都能从模型论、证明论进路的反思中找到理由，此外还有别的条件。（一般讨论见“代数命题逻辑”词条。）但和许多基础问题（如“后承关系一般有哪些本质特征”）一样，这些最小条件在哲学逻辑和逻辑哲学里也有争议。比如有人反对 (2)，理由是：由于模糊性（或别的缘故），自然语言（不管怎么形式化）上的重要后承关系一般并不以 (2) 反映的方式传递。（反对传递性后承的哲学动机，见 Tennant 1994、Cobreros et al 2012、Ripley 2013。）[^cobreros-2012][^ripley-2013][^tennant-1994] 这些就留待更深入的讨论了。

尽管实在论与反实在论的哲学鸿沟仍深，后承的证明中心说明与模型中心说明在许多情形下已经合流（至少外延上合流）。不同证明系统（换个角度说，不同模型论语义）的可靠性与完全性大定理表明：在重要意义上，两种进路常常重合，至少外延重合。证明系统相对于某种模型论语义 **可靠**，是指系统里能证明的论证都是模型论有效的；**完全**，是指所有模型论有效的论证在系统里都有证明。可靠性是任何像样的证明系统都得有的条件，完全性却不能总指望。这些定义当然偏向模型论：是模型论语义定了“可靠”“完全”的标准。撇开术语不谈，一个证明系统若相对于某种模型论语义既可靠又完全（一阶谓词逻辑就是显例），那么它与该语义在“哪些论证有效”上就一致。

完全性结果也能支持模型论说明的适当性，Kreisel 的“挤压论证”即是一例。前面说过模型论说明的弱点：模型都是集合，可能没有模型表象现实世界。Kreisel 表明：若有一个“直观可靠”且相对于模型论语义完全的证明系统，我们就不会漏掉任何模型——每个直观有效的论证都会有反模型。设 $L$ 为一阶语言，$Val$ 表示 $L$ 中直观有效论证的集合。Kreisel 把直观有效性理解为在所有结构（不论是不是集合）上保真；他的分析偏向后承的模态分析——但要注意，我们要处理的弱点正是：只看集合论结构可能不够。设 $V$ 表示 $L$ 中模型论有效性的集合，即在模型上保真的论证；$D$ 表示按某个公认一阶逻辑证明系统演绎有效的论证集合。任何这样的证明系统都“直观可靠”，即系统里演绎有效的论证直观上有效，于是 $D \subseteq Val$。而按定义显然 $Val \subseteq V$：对所有结构保真，自然对集合结构也保真。

由一阶逻辑的完全性结果，有 $V$ ⊆ $D$。把三个包含关系合起来（“挤压”），三个集合就必然相等，特别是 $V = Val$。这就证明了：若某个结构是一阶论证的反例，则存在一个集合论的反例。

证明论与模型论互动的另一处，是逻辑词汇的定义。比如可以持“温和”推理主义：用语义（即真值条件）定义逻辑联结词的意义，但要求联结词意义由推理规则决定。Carnap 有个著名结果：经典推理规则允许对逻辑表达式作非标准解释（Carnap 1943）[^carnap-1943]。晚近许多工作都在追究 Carnap 范畴性问题的性质与范围（Raatikainen 2008, Murzi and Hjortland 2009, Woods 2012, Garson 2013, Peregrin 2014, Bonnay and Westerståhl 2016；另见“形式逻辑中的句子联结词”词条）[^bonnay-2016][^garson-2013][^murzi-2009][^peregrin-2014][^raatikainen-2008][^woods-2012]。

最后要说，阐明逻辑后承最突出的候选虽然是模型论与证明论，但形式语义还有别的框架，比如代数语义、博弈论语义、动态语义（见 Wansig 2000）。

## 4 前提与结论

即便在亚里士多德时代，逻辑后承的“形状”也有异议。用几个前提、几个结论来“系住”后承关系才算合适，至今没有定论。

亚里士多德的三段论，把两个或更多前提与一个结论联在一起。他实际上关注恰好两个前提（大前提、小前提）的论证，但定义并不禁止三个以上前提。这类论证当然该允许：比如有从 $A$、$B$ 到 $C$ 的三段论，又有从 $C$、$D$ 到 $E$ 的三段论，那么从 $A, B$ 与 $D$ 到 $E$ 的更长的论证，某种意义上也是好论证——它是两个小论证串起来的。原来两个论证形式有效，从三个前提出发的长论证也形式有效。另一方面，按常见的解读，亚里士多德的三段论定义把 **单** 前提论证排除在外——这未免武断，因为连他自己的“换位”推理也会被排除。

因此，许多人把逻辑后承关系看作把任意（可能无限的）前提 **集合** 与单个结论配对。这样做还有个好处：把空前提集作为特例收进来。没有任何前提却推出结论的论证，就是结论仅凭逻辑为真。这样的“结论”是 **逻辑真理**（有时叫 **重言式**），按证明中心进路说明是 **定理**。

也许还有理由把后承概念用得更广。Gentzen 为经典逻辑建立的证明论，把后承定义在多个前提与多个结论之间：从前提集 $X$ 到结论集 $Y$ 的论证有效，如果 $X$ 里每个成员为真都保证（在相关意义上）$Y$ 里某个成员为真。这形式上无疑清晰，但多前提—多结论意义上的后承有没有哲学适用性，仍是悬案。尤其是那些用 **证明** 定义后承的反实在论者（如 Michael Dummett），拒斥多结论分析。对反实在论者来说，好推理的特征是 **辩护**（warrant）从前提传到结论；多结论分析似乎根本行不通。从 $A$ 到 $B, C$ 的多结论论证里，对 $A$ 的辩护未必传到 $B$ 或 $C$：我们有权得出的唯一结论是析取 $B$ **或** $C$。可见要用辩护分析后承，似乎得先懂某些逻辑词汇（这里是析取），才能懂后承关系。若想用后承来 **定义** 那些逻辑词汇，这不可接受。单结论设定似乎没这麻烦。（不过反实在论者也可为多结论后承辩护，见 Restall 2005；用某些次经典多结论逻辑服务悖论的非经典解，见 Beall 2011。）

拓宽后承概念的另一条线，与晚近的子结构逻辑有关。提议是：也许可以不要某些支配前提（或结论）如何组合的标准规则。结构规则管的是论证的 **形状** 或 **结构**——前提和结论怎么收在一起，而不是这些陈述怎么构造。比如 **弱化** 规则说：从前提集 $X$ 到结论 $C$ 的论证若有效，那么从 $X$ 再加一个前提 $A$ 到 $C$ 的论证也有效。有人觉得这条有问题，主要理由是：多出来的前提 $A$ 不必在推出 $C$ 时派上用场，所以 $C$ 并不在适当意义上 **从** 前提 $X,A$ 得出。**相干逻辑** 就是为尊重这个想法而设计的，去掉了弱化规则。（证明论方面的图景见 Negri and von Plato (2001)。）

其他结构规则也受到质疑。子结构逻辑还可能用在柯里悖论一类悖论的分析上。柯里悖论及类似推理有个关键步骤，似乎要把某个假定的两次使用并成一次（再解除该假定）。有人认为这步有问题，于是必须区分从 $A$ 到 $B$ 的论证与从 $A, A$ 到 $B$ 的论证，**收缩** 规则由此被拒斥。

还有些例子，前提的使用 **顺序** 要紧，从 $A, B$ 到 $C$ 的论证得和从 $B, A$ 到 $C$ 的论证分开。（细节见“子结构逻辑”词条。）子结构逻辑的形式系统无疑优雅有趣，但其哲学重要性与适用性的争论还没有定论。

## 5 一种还是多种？

这里只碰到后承概念的几个核心方面，其余问题、争论尤其是细节，留给各种具体说明（本百科里都有）。可只要看一眼下面的 **相关词条**，就会发现关于“什么从什么（逻辑地）得出”的理论多得惊人。由此引出收尾的问题：所有这些理论瞄准的是同一个逻辑后承概念，还是有许多个？

大家都同意：研究后承的形式技术很多，提出不同后承关系的形式系统也极多。可给定一个具体论证，它是否演绎有效，是不是全有或全无？正统观点叫逻辑 **一元论**，答“是”：只有一种演绎后承关系，不同形式系统对它的建模有好有坏。（例如 Priest 1999 为二元论辩护。）[^priest-1999] 逻辑 **语境论者** 或 **相对主义者** 说，论证有效与否取决于主题、参照框架或其他评价语境。（比如排中律的某次使用，在经典数学教科书里有效，在直觉主义数学教科书里就未必，在讨论虚构或模糊事项的语境里也未必。）逻辑 **多元论者** 则说，对同一个论证、同一个语境，关于有效性有时可以有不止一种恰当说法。例如，从矛盾前提集到不相干结论的论证，也许既该说它 **有效**——凭其形式，前提真而结论不真不会发生，所以按一种精确意义有效；又该说，按另一种意义，其形式并不保证前提的真 **引出** 结论的真。一元论者或语境论者认为，同一个论证的有效性必须有个单一答案；多元论者不认。多元论者认为，后承概念本身可以用不止一种方式精确化，正如“好论证”原初的想法分成了演绎有效与归纳有效（为多元论辩护见 Beall and Restall 2000）[^restall-2000][^beall-2000]。

## 脚注

[^note-1]: 上一节多得益于 John MacFarlane 的论文 MacFarlane 2000（其他网络资源）。他区分了我们这里只约略提及的三种形式性，并对这些概念详加讨论，作出许多我们一带而过的区分。

## References（引用注释）

**以下文献从原文照录，不作翻译；中国文献译为中文。**

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

### History of Logical Consequence

#### Expositions

#### Source Material

### 20th Century Developments

### Philosophy of Logical Consequence

[^coffa-1993]: Coffa, J. Alberto, 1993, *The Semantic Tradition from Kant to Carnap*, Linda Wessels (ed.), Cambridge: Cambridge University Press. An historical account of the Kantian origins of the rise of analytic philosophy and its development from Bolzano to Carnap.
[^kneale-1962]: Kneale, W. and Kneale, M., 1962, *The Development of Logic*, Oxford: Oxford University Press; reprinted, 1984. The classic text on the history of logic until the middle 20th Century.
[^ewald-1996]: Ewald, William, 1996, *From Kant to Hilbert: a source book in the foundations of mathematics* (Volumes I and II), Oxford: Oxford University Press. Reprints and translations of important Texts, including Bolzano on logical consequence.
[^heijenoort-1967]: van Heijenoort, Jean, 1967, *From Frege to Gödel: a sourcebook in mathematical logic 1879–1931*, Cambridge, MA: Harvard University Press. Reprints and translations of central texts in the development of logic.
[^husserl-1900]: Husserl, Edmund, 1900 [2001], *Logical Investigations* (Volumes 1 and 2), J. N. Findlay (trans.), Dermot Moran (intro.), London: Routledge.
[^mill-1872]: Mill, John Stuart, 1872 [1973], *A System of Logic* (8th edition), in J. M. Robson (ed.), *Collected works of John Stuart Mill* (Volumes 7 & 8), Toronto: University of Toronto Press.
[^anderson-1975]: Anderson, A.R., and Belnap, N.D., 1975, *Entailment: The Logic of Relevance and Necessity* (Volume I), Princeton: Princeton University Press.
[^anderson-1992]: Anderson, A.R., Belnap, N.D. Jr., and Dunn, J.M., 1992, *Entailment* (Volume II), Princeton: Princeton University Press. This book and the previous one summarise the work in relevant logic in the Anderson–Belnap tradition. Some chapters in these books have other authors, such as Robert K. Meyer and Alasdair Urquhart.
[^dummett-1991]: Dummett, Michael, 1991 *The Logical Basis of Metaphysics*, Cambridge, MA: Harvard University Press. Groundbreaking use of natural deduction proof to provide an anti-realist account of logical consequence as the central plank of a theory of meaning.
[^gentzen-1969]: Gentzen, Gerhard, 1969, *The Collected Papers of Gerhard Gentzen*, M. E. Szabo (ed.), Amsterdam: North Holland.
[^mancosu-1998]: Mancosu, Paolo, 1998, *From Brouwer to Hilbert*, Oxford: Oxford University Press. Reprints and translations of source material concerning the constructivist debates in the foundations of mathematics in the 1920s.
[^negri-2001]: Negri, Sara and von Plato, Jan, 2001, *Structural Proof Theory*, Cambridge: Cambridge University Press. A very accessible exposition of so-called structural proof theory (which involves a rejection of some of the standard structural rules at the heart of proof theory for classical logic).
[^shoesmith-1978]: Shoesmith D. J. and Smiley, T. J., 1978, *Multiple-Conclusion Logic*, Cambridge: Cambridge University Press. The first full-scale exposition and defence of the notion that logical consequence relates multiple premises and multiple conclusions.
[^restall-2000]: Restall, Greg, 2000, *An Introduction to Substructural Logics*, Lond: Routledge. ([Précis available online](http://consequently.org/isl/)) An introduction to the field of substructural logics.
[^tarski-1935]: Tarski, Alfred, 1935, “The Concept of Truth in Formalized Languages,” J.H. Woodger (trans.), in Tarski 1983, pp. 152–278.
[^tarski-1936]: –––, 1936, “On The Concept of Logical Consequence,” J.H. Woodger (trans.), in Tarski 1983, pp. 409–420.
[^tarski-1983]: –––, 1983, *Logic, Semantics, Metamathematics: papers from 1923 to 1938*, second edition, J. H. Woodger (trans.), J. Corcoran (ed.), Indianapolis, IN: Hackett.
[^there-nd]: There are many (many) other works on this topic, but the bibliographies of the following will serve as a suitable resource for exploring the field.
[^avron-1994]: Avron, Arnon, 1994, “What is a Logical System?” in *What is a Logical System?*, D.M. Gabbay (ed.), Oxford: Clarendon Press (Studies in Logic and Computation: Volume 4), pp. 217–238.
[^beall-2011]: Beall, Jc, 2011, “Multiple-conclusion LP and default classicality,” *Review of Symbolic Logic*, 4(2): 326–336.
[^beall-2000]: Beall, Jc and Restall, Greg, 2000, “Logical Pluralism,” *Australasian Journal of Philosophy*, 78: 457–493.
[^belnap-1962]: Belnap, Nuel D., 1962, “Tonk, Plonk and Plink,” *Analysis*, 22 (6): 130–134.
[^bonnay-2012]: Bonnay, Denis and Westerståhl, Dag, 2012, “Consequence Mining: Constants Versus Consequence Relations,” *Journal of Philosophical Logic*, 41(4): 671–709.
[^bonnay-2016]: –––, 2016, “ Compositionality Solves Carnap’s Problem,” *Erkenntnis*, 81 (4): 721–739.
[^brandom-1994]: Brandom, Robert, 1994, *Making It Explicit*, Cambridge, MA: Harvard University Press. [See especially Chapters 5 and 6 on the account of logical consequence according to which truth is not a fundamental explanatory notion.]
[^caret-2015]: Caret, Colin R. and Hjortland, Ole T. (eds.), 2015, *Foundations of Logical Consequence*, Oxford: Oxford University Press.
[^carnap-1943]: Carnap, Rudolf, 1943, *Formalization of Logic*, Cambridge, MA: Harvard University Press.
[^cobreros-2012]: Cobreros, Pablo; Égré, Paul; Ripley, David and van Rooij, Robert, 2012, “Tolerance and mixed consequence in the s’valuational setting,” *Studia Logica*, 100(4): 855–877.
[^etchemendy-1990]: Etchemendy, John, 1990, *The Concept of Logical Consequence*, Cambridge, MA: Harvard University Press.
[^etchemendy-2008]: –––, 2008, “Reflections on Consequence”, in D. Patterson (ed.), 2008.
[^garson-2013]: Garson, James W., 2013, *What Logics Mean: From Proof Theory to Model-Theoretic Semantics*, Cambridge: Cambridge University Press.
[^gomez-torrente-1996]: Gomez-Torrente, Mario, 1996, “Tarski on Logical Consequence,” *Notre Dame Journal of Formal Logic*, 37: 125–151.
[^griffiths-2022]: Griffiths, Owen, and Paseau, A.C., 2022, *One True Logic: A Monist Manifesto*, Oxford: Oxford University Press.
[^hanson-1997]: Hanson, William H., 1997, “The Concept of Logical Consequence,” *The Philosophical Review*, 106 (3): 365–409.
[^kennedy-2017]: Kennedy, Juliette and Väänänen, Jouko, 2017, “Squeezing arguments and strong logics,”, in Hannes Leitgeb, Ilkka Niiniluoto, Elliot Sober and P. Seppälä (eds.), *Logic, Methodology, and the Philosophy of Science: Proceedings of the Fifteenth International Congress* (CLMPS 2015), London: College Publications.
[^kreisel-1967]: Kreisel, Georg, 1967, “Informal Rigour and Completeness Proofs,” in I. Lakatos (ed.), *Problems in the Philosophy of Mathematics*, (Studies in Logic and the Foundations of Mathematics: Volume 47), Amsterdam: North Holland, pp. 138–186.
[^mcgee-1992]: McGee, Vann, 1992, “Two Problems with Tarski’s Theory of Consequence,” *Proceedings of the Aristotelian Society*, 92: 273–292.
[^murzi-2014]: Murzi, Julien and Carrara, Massimiliano, 2014, “More Reflections on Consequence,” *Logique et Analyse*, 57 (227): 223–258.
[^murzi-2009]: Murzi, Julien and Hjortland, Ole T., 2009, “Inferentialism and the Categoricity Problem: Reply to Raatikainen,” *Analysis*, 69 (3): 480–488.
[^patterson-2008]: Patterson, Douglas, (ed.), 2008, *New Essays on Tarski and Philosophy*, Oxford: Oxford University Press.
[^peregrin-2014]: Peregrin, Jaroslav, 2014, *Inferentialism: Why Rules Matter*, UK: Palgrave Macmillan.
[^prawitz-1974]: Prawitz, Dag, 1974, “On the Idea of a General Proof Theory,” *Synthese*, 27 (1–2): 63–77.
[^prawitz-1985]: –––, 1985, “Remarks on some approaches to the concept of logical consequence,” *Synthese*, 62: 153–171.
[^prawitz-2005]: –––, 2005, “Logical Consequence from a Constructivist Point of View,” in S. Shapiro (ed.), *The Oxford Handbook of the Philosophy of Mathematics and Logic*, Oxford: Oxford University Press, pp. 671–695.
[^prawitz-2012]: –––, 2012, “The Epistemic Significance of Valid Inference,” *Synthese*, 187: 887–898.
[^priest-1999]: Priest, Graham, 1999, “Validity,” *European Review of Philosophy*, 4: 183–205 (Special Issue: *The Nature of Logic*, Achillé C. Varzi (ed.), Stanford: CSLI Publications.
[^prior-1960]: Prior, Arthur N., 1960, “The Runabout Inference-Ticket,” *Analysis*, 21 (2): 38–39.
[^putnam-1971]: Putnam, Hilary, 1971, *Philosophy of Logic*, New York: Harper & Row.
[^quine-1986]: Quine, W.V.O., 1986 (2nd Ed.), *Philosophy of Logic*, Cambridge, MA: Harvard University Press.
[^raatikainen-2008]: Raatikainen, Panu, 2008, “On Rules of Inference and the Meanings of Logical Constants,” *Analysis*, 68 (300): 282–287.
[^ray-1996]: Ray, Greg, 1996, “Logical Consequence: A Defense of Tarski,” *The Journal of Philosophical Logic*, 25 (6): 617–677.
[^read-1994]: Read, Stephen, 1994, “Formal and Material Consequence,” *The Journal of Philosophical Logic*, 23 (3): 247–265.
[^restall-2005]: Restall, Greg, 2005, “Multiple Conclusions,” in P. Hájek, L. Valdés-Villanueva, and D. Westerståhl (eds.), *Logic, Methodology and Philosophy of Science: Proceedings of the Twelfth International Congress*, London: KCL Publications, pp. 189–205. [[Preprint available online in PDF](http://consequently.org/papers/multipleconclusions.pdf)].
[^ripley-2013]: Ripley, David, 2013, “Paradoxes and failures of cut,” *Australasian Journal of Philosophy*, 91(1): 139–164. doi: 10.1080/00048402.2011.630010.
[^sagi-2014a]: Sagi, Gil, 2014a, “Formality in Logic: From Logical Terms to Semantic Constraints,” *Logique et Analyse*, 57 (227): 259–276.
[^sagi-2014b]: –––, 2014b, “Models and Logical Consequence,” *Journal of Philosophical Logic*, 43 (5): 943–964.
[^shapiro-1987]: Shapiro, Stewart, 1987, “Principles of Reflection and Second Order Logic,” *Journal of Philosophical Logic* 16 (3): 309–333.
[^shapiro-1998]: –––, 1998, “Logical Consequence: Models and Modality,” in M. Schirn (ed.), *The Philosophy of Mathematics Today*, Oxford: Oxford University Press, pp. 131–156.
[^shapiro-2005]: –––, 2005, “Logical Consequence, Proof Theory, and Model Theory,” in S. Shapiro (ed.), *The Oxford Handbook of the Philosophy of Mathematics and Logic*, Oxford: Oxford University Press, pp. 651–670.
[^shapiro-2014]: –––, 2014, *Varieties of Logic*, Oxford: Oxford University Press.
[^sher-1991]: Sher, Gila, 1991, *The Bounds of Logic*, Cambridge, MA: MIT Press.
[^sher-1996]: –––, 1996, “Did Tarski Commit Tarski’s Fallacy?,” *Journal of Symbolic Logic*, 61 (2): 653–686.
[^sher-2022]: Sher, Gila, 2022, *Logical Consequence*, Cambridge: Cambridge University Press.
[^schroeder-heister-1991]: Schroeder-Heister, Peter, 1991, “Uniform Proof-Theoretic Semantics for Logical Constants (Abstract),” *Journal of Symbolic Logic*, 56: 1142.
[^tarski-1986]: Tarski, Alfred, 1986, “What are Logical Notions,” *History and Philosophy of Logic*, 7: 143–154.
[^tennant-1994]: Tennant, Neil, 1994, “The Transmission of Truth and the Transitivity of Deduction,” in *What is a Logical System?* (Studies in Logic and Computation: Volume 4), D.M. Gabbay (ed.), Oxford: Clarendon Press, pp. 161–177.
[^wansing-2000]: Wansing, Heinrich, 2000, “The Idea of a Proof-Theoretic Semantics and the Meaning of the Logical Operations,” *Studia Logica*, 64 (1): 3–20.
[^westerståhl-2012]: Westerståhl, Dag, 2012, “From constants to consequence, and back,” *Synthese*, 187 (3): 957–971.
[^woods-2012]: Woods, Jack, 2012, “Failures of Categoricity and Compositionality for Intuitionistic Disjunction,” *Thought: A Journal of Philosophy*, 1 (4): 281–291.
[^zinke-2018]: Zinke, Alexandra, 2018, *The Metaphysics of Logical Consequence* (Studies in Theoretical Philosophy: Volume 6), Frankfurt am Main: Vittorio Klostermann.

## 学术工具

* [如何引用本词条](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=logical-consequence)。
* [预览本词条的 PDF 版本](https://leibniz.stanford.edu/friends/preview/logical-consequence/)，见 [SEP 学会之友](https://leibniz.stanford.edu/friends/)。
* 在 [InPhO](https://www.inphoproject.org/entity?sep=logical-consequence&redirect=True) 查找与本词条相关的话题与思想家。
* 在 [PhilPapers](https://philpapers.org/sep/logical-consequence/) 查看本词条的增强文献目录及其数据库链接。

## 其他网络资源

- MacFarlane, John, 2000, [*What Does it Mean to Say that Logic is Formal?*](http://johnmacfarlane.net/dissertation.pdf), Ph. D. Dissertation, Philosophy Department, University of Pittsburgh.

## 相关词条

亚里士多德的逻辑学 | 伯恩哈德·波尔查诺 | 鲁道夫·卡尔纳普 | 弗雷格定理和算术基础 | 代数命题逻辑 | 经典逻辑 | 归纳逻辑 | 直觉主义逻辑 | 非单调逻辑 | 逻辑的规范地位 | 子结构逻辑 | 逻辑常项 | 逻辑形式 | 逻辑多元主义 | 逻辑真理 | 模型论 | 证明论 | 伯特兰·罗素 | 图式 | 证明论语义

**（译注：相关词条的中文站内链接将由管线在对应词条重译完成后统一挂接。）**
