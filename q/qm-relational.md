# 关系性量子力学 relational (Carlo Rovelli)

*首次发表于 2002 年 2 月 4 日；2025 年 2 月 4 日实质修订。*

关系性量子力学（RQM）是当今讨论最广的量子力学解释中最晚出的一种。它于 1996 年提出，最初动因在量子引力（Rovelli 1996）[^rovelli-1996]；此后关注渐增，起初极慢，却稳步上升，近些年达到高峰（参见 Calosi and Riedel 2024，该文对这一解释的历史演变亦有很好的梳理）[^calosi-2024][^riedel-2024]。

关于量子理论的种种困惑，RQM 并不视为这样的征兆：仿佛为使理论可理解，非得引入某个新方程（如德布罗意-玻姆理论），或某些尚未观测到的现象（如物理坍缩假说）。它也不认为，非得预设一个不可企及的实在域（如多世界的普遍量子态）。它把这些现象看作一场邀请：彻底更新我们思考实在所用的概念框架。

RQM 精化了教科书解释：哥本哈根“观察者”所扮角色中的某些方面（并非全部）并不限于经典世界，而可由任何物理系统承担。这一解释拒绝对量子态作本体论解读：量子态只起辅助作用，类似经典力学中的哈密顿-雅可比函数；其立足点反而是与经典力学相同的本体论，即物理系统与物理变量。与经典力学的差别有二：其一，**变量只在离散的相互作用中取值**；其二，变量所取的值只 **相对于** 受该相互作用影响的另一系统。此处“相对”一语，取经典力学中速度乃系统 **相对于** 另一系统之性质的意思。这些相对事件发生在离散时刻：物理变量取得精确的相对值；至于中间时刻，这些变量可能全无取值。至少在某些读法下（详见下文），这会导向一种激进的角度主义反基础主义。RQM 的技术基础如下：

**主要假设**：相对于某系统 $S$ 的（未来）变量取值，其概率分布取决于同一系统 $S$ 的（过去）变量取值，而与另一系统 $S'$ 的（过去）变量取值无关。

这一解释的表述无需预设经典世界。测量不具基础地位，也不要求把某些特殊系统算作“观察者”；它假定任何物理系统都可承担哥本哈根观察者的角色——在给定时刻促成变量取值。由于主要假设，这样做不改变量子理论的一切预言：系统 $S$ 所观察到的干涉，不会因另一系统 $S'$ 上变量取值的实现而消失（退相干当然仍可抑制它）。在维格纳-朋友情境中，维格纳观察到的干涉与朋友所确定的观察相容。RQM 由此说明了一个完全量子的世界，而不诉诸隐变量、多世界、物理坍缩机制，也不给心智、能动者之类留特殊位置。

这份简约的代价，是削弱经典力学所持的惯常“强”实在论——它假定物理变量具有非关系的值，且在每一时刻都存在。变量只在相互作用中取值，于是有了稀疏的事件本体论（或“闪光”本体论）；变量又以其所指涉的系统作标示，这给世界的表示添了一层索引性，也引出哲学难题。

就其自身而言，RQM 在形而上学上是中立的；但它持一种强烈的关系主义立场，因而质疑强实在论（Laudisa 2019）[^laudisa-2019]，其含义见下文。正因这番对实在论的改造，RQM 先后被安放在多种哲学视角之中：建构经验论（van Fraassen 2009）[^fraassen-2009]、新康德主义（Bitbol 2007 [Other Internet Resources], Bitbol 2010）[^bitbol-2010]、反一元论（Dorato 2016）[^dorato-2016]、结构实在论（Candiotto 2017）[^candiotto-2017]、视角实在论（Massimi 2022）[^massimi-2022]、形而上学融贯论（Dorato and Morganti 2022）[^dorato-2022]，以及反基础主义的融贯论。（另见 Brown 2009、Wood 2010 [Other Internet Resources]，尤以 Calosi and Riedel 2024 的讨论最为详尽。）[^brown-2009][^calosi-2024][^riedel-2024] 它与 Dennis Dieks 的视角量子实在论（Dieks 2022, Bene and Dieks 2002）[^bene-2002][^dieks-2022]、与 QBism（Fuchs 2001, 2002 [Other Internet Resources]）[^fuchs-2001]、与 Healey 的实用主义进路（Healey 1989, 2023）[^healey-1989]，以及与 Zeilinger、Bruckner 所主张的量子理论观点（Zeilinger 1999, Brukner & Zeilinger 2003）[^brukner-2003][^zeilinger-1999]，多有相通。

## 1 主要观念

### 1.1 物理变量的取值

RQM 的出发点是：量子力学并不关乎波函数或量子态 $\psi$，而关乎物理变量的取值。相应地，RQM 预设的基本本体论只含物理系统与取值的变量，与经典力学无异。例如，粒子在时刻 $t$ 位于 $x$，就是一个真实事实。这类事实（“粒子在时刻 $t$ 位于 $x$”）称为“事件”或“量子事件”；量子理论讲的就是这类事件。不过，量子力学中的事实与经典力学中的事实有两点不同。经典力学有两个一般假定，RQM 都放弃了：

(a) 经典力学假定，系统的所有变量在每一时刻都有值。RQM 反其道而行：它假定自然界一般并不如此（Heisenberg 1925; Kochen & Specker 1967）[^heisenberg-1925][^kochen-1967]。物理变量只在某些时刻有值，其余时刻则无值。换句话说，事件是离散的。变量取值，恰在系统作用于另一系统之时。更确切地说：系统 $S$ 的变量 $A$ 取某个值，**就是** 与第二个系统 $S'$ 发生相互作用；变量 $A$ 刻画某一作用对 $S'$ 的影响。在 RQM 中，这就是“变量有值”的全部含义。换言之，一个系统可由取值的变量来描述，**就是** 以某种方式影响另一系统，别无其他。正是这一基本直觉，让海森堡在 1925 年找到了量子力学的钥匙：有些问题在经典力学中讲得通，在自然界却没有意义。比如，“当电子自旋的 $z$ 分量为 $\frac{1}{2} \hslash$ 时，其 $y$ 分量为何？”便毫无意义：它既无操作定义，也不是对自然的实在论理解所必需。

(b) RQM 放弃的第二个经典假定是：变量取绝对值，即不依赖于任何其他系统的值。RQM 反其道而行：**所有**（偶然）物理变量都是关系性的。所谓偶然变量，即经典理论中由相空间函数表示的那些变量。这类变量无论取什么值，都（隐含或明确地）由一个第二个物理系统作标示。若系统 $S$ 的变量 $A$ 在与第二个系统 $S'$ 的相互作用中取值，则所取之值 **相对于** $S'$；事件本身的实现也相对于某个系统。其具体含义就是上述假设：系统 $S$ 未来以何种方式影响 $S'$，以概率方式取决于 $S$ 的变量相对于 $S'$ 所取的值，而不取决于 $S$ 未来以何种方式影响第三个系统 $S''$。相对于任给系统 $S'$ 的全部事件所成之集，连同由此产生的概率预言，称为 $S'$ 的“视角”。

放弃这两个假定，便离开了一个由来已久的概念框架——它长期支撑着物理学，或许也支撑着我们的世界观。这一框架设想：世界由若干系统构成，而这些系统在任何时刻都凭自身（独立于任何别的系统）具有可变性质；这些性质可由该系统所固有的变量之取值来刻画。

RQM 的立论是：“不同的观察者可以对同一组事件给出不同的描述”（Rovelli 1996: 1643）[^rovelli-1996]。教科书量子力学完备地描述单个系统的视角，却无视该系统对其他系统视角的影响。RQM 强调：任何观察者作用于其他系统时，自身就是一个量子系统。Vincenzo Fano（2024 [Other Internet Resources]）举了一个浅例，说明 RQM 如何处理量子力学中常见而看似悖谬的情形。视角之间的关系见下文。

### 1.2 相对变量：“不同的观察者可以对同一组事件给出不同的描述”

相对变量，指取值不取决于单一系统、而取决于两个系统的变量。经典力学中物体的速度即一著例：速度总是（隐含或明确地）相对于第二个物体而言；在经典力学里，孤立的“单个物体的速度”并不存在。其他著例还有电势（只有一导体相对于另一导体的电势才有物理意义）与位置（只有相对于某个其他物体的位置才有物理意义）。关系性量子力学朝此方向又迈出一大步：它假定，只要承认 **所有** 物理变量都在此意义上是关系性的，量子力学便可理解。

“相对”并不等于主观。主体或能动者在 RQM 中并无特殊地位。我们说自身相对于太阳的速度是每秒 11 公里，并没有把主观性强加给太阳；我们说路标到路口的距离是 100 米，也没有把路口当成能动者。在自然主义视角下，人、能动者、主体都是物理系统；他们所关联的世界，由变量 **相对于** 他们所取的值来描述。住在地球上的人见宇宙旋转，只因地球在自转；而宇宙相对于地球所定义的参照系旋转，与地球上有没有人毫不相干。说 RQM 需要主体或能动者，与说解释日月星辰每日绕地旋转需要引入能动性或主体性一样，是同一种谬误：无稽之谈。RQM 不带任何主观、唯心论或心理主义色彩。

### 1.3 观察者与测量

按教科书的讲法，量子力学讲的是“观察者”对量子系统作“测量”所得的测量结果。这类测量不是两个系统间的一般相互作用，而是特殊的一类：它们要求信息被登记、储存。要做到这一点，必须有退相干与耗散，因之必须有一个经典域。RQM 把理论的解释推广到退相干与耗散不足以支撑“观察者-测量”解释的范围。退相干足够时，变量取值变得“稳定”（Di Biagio and Rovelli 2021）[^rovelli-2021]：其标示不再相干，测量在该退相干域内也有所确定的结果。

因此，在 RQM 看来，量子力学并非关于某一实体 $\psi$ 之动力学的理论，仿佛我们经验的世界由它生发而出。它讲的正是我们经验里那个标准世界：惯常物理变量在相互作用中取什么值，转移概率又如何说明这些取值在已有取值之下能否实现。只要顾到变量的相对性质，这与量子现象便相容。

### 1.4 波函数

在 RQM 中，量子态是一个指涉两个系统（而非一个系统）的数学装置。它编码第一个系统的变量在与第二个系统相互作用中已然实现的值（Groenewold 1957）[^groenewold-1957]；因此也编码了关于这些变量相对于第二个系统的未来取值，我们所可能预言的一切。换言之，态 $\psi$ 可视为一份可供第二个系统获取的信息汇编，由一段特定的相互作用史所决定。如此理解，量子态始终且仅是 **相对态**，即埃弗雷特（1957）意义上的相对态。就此而言，RQM 是强烈的“埃弗雷特式的”理论；但它与多世界解释不同：后者假定一个普遍波函数，各种相对态 $\psi$ 只是它的分支，而这一普遍波函数在 RQM 中毫无作用（在量子理论的任何物理应用中也一样）。

量子理论的许多表述，把系统的波函数或量子态 $\psi$ 当作该系统自身的性质。在 RQM 看来，关于量子理论的种种混乱正由此而生（Rovelli 2018）[^rovelli-2018]。RQM 对量子态持一种弱实在论：量子态表示某种物理上真实的东西。例如，在经历我们称为“态制备”的程序之后，“那次制备是什么”确有其事实；制备出不同的纯量子态，对应着不同的物理事态。然而这些“事态”**相对于制备装置**，并不单单属于系统本身。正因如此，RQM 才与 ψ-本体论一类的定理相容，例如论波函数实在性的 PBR 定理（Pusey, Barrett, & Rudolph 2012; Leifer 2014）[^leifer-2014]：把 PBR 定理读作关于相对态的定理，它便适用于 RQM。RQM 与这类定理的和平共处，已在（Calosi and Oldofredi 2021）[^calosi-2021][^oldofredi-2021] 中讨论。

另一方面，RQM 不用系统的 **绝对** 态这一概念，也不取其他解释中的常见想法——量子态可表示关于该系统的“全部所是”。这种对态的“强实在论”解读，RQM 放弃之。在此意义上，RQM 对波函数的解释近似于经典力学对哈密顿-雅可比泛函的解释：一种理论工具，用以依据关于某个事态的已知信息，便利地算出未来事件的概率。波函数 $\psi$ 与哈密顿-雅可比泛函 $S$ 之间不止是类比：在半经典近似下，后者逼近前者（$\psi \sim \exp iS/\hslash$）。这一数学关系可作反对 $\psi$ 强实在论解读的论据，理由如下：对物理理论数学装置中量 A 的解释，必须与该量在近似下所归约为的东西的解释相容。举例说，经典粒子的哈密顿-雅可比函数并无强实在论解释；我们在计算中明确使用的哈密顿-雅可比函数，会随我们对系统的了解而坍缩、跳跃——量子波函数亦然。

剥去量子态的强实在论解释，量子跃迁与坍缩之谜也随之消散。RQM 的态相对于某一系统，这正解释了它为何会随两系统相互作用而跳跃。

经典力学里，哈密顿-雅可比泛函可以不用——这正说明它没有直接的本体论分量。量子理论中的 $\psi$ 同样可以不用。证据是：量子力学形式体系的整个早期发展（Heisenberg 1925; Born & Jordan 1925; Dirac 1925; Born, Heisenberg, & Jordan 1926）[^born-1925][^dirac-1925][^heisenberg-1925] 早于引入 $\psi$ 的工作（Schrödinger 1926）[^schrödinger-1926]。量子力学可以不提量子态，而表述为关于事件序列之概率的理论：态 $\psi$ 是称手的工具，却非必需之物。

Heilbron 与 Rovelli（2023）认为，薛定谔的波动力学尽管用途极广，在概念上却有误导之嫌：它助长了对 $\psi$ 本体论作用的错误强调。

### 1.5 量子叠加：猫能否半死半活？

若 $\psi'$ 与 $\psi''$ 是系统两个正交的量子态，量子力学便假定系统也可处于态 $\psi = (\psi' +\psi'')/\sqrt{2}$：这就是叠加原理，理论的基石（Dirac 1930）[^dirac-1930]。若 $\psi'$ 是活猫之态、$\psi''$ 是死猫之态，则 $\psi$ 便是猫处于死活叠加的态；理论预言，这是猫的一个可能（相对）态。RQM 对此类情形怎么说？猫在某种意义上半死半活吗？

像 $\psi =(\psi' +\psi'')/\sqrt{2}$ 这类态的存在，并不意味着我们“看见叠加”（此说时有所闻，实属误解）：按教科书量子理论，我们“看见”即测量到的，是自伴算符的本征值，而非量子态；被测的本征值总是单义的，从不“叠加”。说某态是叠加，其实只意味着两件事。其一，若某可观测量在 $\psi'$ 中取 $a'$、在 $\psi''$ 中取 $a''$，则对该系统的任何观察都给出 $a'$ 或 $a''$，各以概率 1/2。其二，对任何在 $(\psi'$, $\psi''$) 基下非对角的可观测量，其测量结果的概率分布都会受干涉影响：它不会是该可观测量在 $\psi'$ 与 $\psi''$ 中取值的平均之平均。在 RQM 中，“处于量子叠加”的含义不过如此。

我们从未见过半死半活的猫，因为量子理论预言我们永远不会见到这类东西：它预言我们看到的猫非活即死。它也预言，原则上我们应当能观察到两个态之间的干涉效应。在猫这类宏观系统上，退相干会强烈抑制这些干涉效应，因此理论实际上预言它们极难观察到——这与经验相符。另一方面，若问猫自身在被量子叠加地描述时会感知到什么，谜题就出现了。设猫的大脑测量自己的心脏是否跳动。理论预言：大脑会发现它在跳，或不在跳。按教科书量子力学，这意味着 $\psi$ 坍缩为 $\psi'$ 或 $\psi''$。这又意味着两态之间不再有任何干涉效应。然而 **这一** 结论与量子理论所预言的干涉效应（尽管因退相干而微弱）相矛盾。**这个问题** 由 RQM 化解：靠的是主要假设——猫作为量子系统影响外部系统的方式，并不受猫的心脏影响其大脑这一特定方式的影响。

也就是说，猫的某一部分与另一部分相互作用时，猫相对于外部世界的态并不坍缩。

## 2 相关问题

### 2.1 信息

RQM 的早期表述以信息论语言写成，后来的“用信息论阐明量子理论”之风正发源于此（Calosi and Riedel 2024）[^calosi-2024][^riedel-2024]。量子态是一种编码方式：它把观察系统 $S'$ 可能拥有的、关于量子系统 $S$ 的信息编码起来，而这些信息关乎预言 $S$ 未来如何影响 $S'$。此类信息由 $S$ 过去影响 $S'$ 的方式决定。此外，（Rovelli 1996）[^rovelli-1996]还提出一个希望：凭几条简单的信息公设，即可完整重构量子形式体系。当时提出两条主要公设：

- (i) 相空间紧致的系统，相关信息有限；
- (ii) 新信息总可获取。

两条公设并不冲突：收集到新信息时，某些原先相关的信息便不再相关。此处“相关”意为影响未来的概率。稍一思量便知，第一条公设蕴涵量子理论特有的离散性，第二条则由海森堡不确定性原理蕴涵。类似想法曾由 Zeilinger 与 Bruckner 独立提出（Zeilinger 1999; Brukner & Zeilinger 2003）[^brukner-2003][^zeilinger-1999]。

诚如 Dorato（2017）所强调，信息最好别当作初始概念；它必须借别的东西在物理上得到定义，正因如此，它才能在爱因斯坦（1919）意义上的“原理理论”中担当要角。在 RQM 中，信息以关系方式定义：即一个物理系统关于另一系统所拥有的相对信息（香农意义）。相对信息是两系统间的物理关联，即因存在物理约束，复合系统的可能状态数与两系统状态数之积之间差额的一种度量。于是，若系统变量 $O_A$ 与另一系统变量 $A$ 的取值彼此关联，我们就说 $O_A$ 拥有关于 $A$ 的信息；此时测量 $O_A$ 的结果可预言测量 $A$ 的结果——在这个意义上，“$O_A$ 拥有关于 $A$ 的信息”。

依香农的精神，这是一种很弱的信息定义，不涉心理主义、语义或认知层面。RQM 早期工作的信息视角，影响了后来大量以信息论研究量子理论基础的进路，也影响了随后若干试图从物理上透明的公设推出量子形式体系的尝试。关于这一纲领的现状，有一份风格独特、略显散漫而时见洞见的叙述，见（Stacey 2021 [Other Internet Resources]）。

### 2.2 离散性

离散性并非量子理论可有可无的方面，而是其最本质的特征（理论之名即由此而来）。离散性在量子理论中以两种相关的方式出现。

其一，系统若处于相空间有限区域 R 内，能收集到的有关其态的信息量有限：每个自由度上，信息量等于 R 的刘维尔测度除以普朗克常数。离散谱正由此而生。连续谱则需要无限相空间，可视为理想化的产物。因此，量子力学的离散性体现在第一条信息公设中。

其二，量子力学以变量在特定离散时刻的取值来描述世界。离散性的这一面，正由 RQM 的稀疏本体论直接说明。例如，量子粒子的历史，既非时空中的一条连续线（如经典力学），也非时空上的连续波函数；相对于任何别的系统，它是一组离散的相互作用，每一次都定域于时空之中。

RQM 的离散本体论似乎带来一个难题：事件发生的 **时机** 由什么决定？难处在于，要确定比如说一次测量发生在哪一特定时刻，并不容易。Rovelli（1998）处理了这个问题，指出量子力学本身确实对测量何时发生给出（概率性的）预言。因为“测量是否已经发生”这一问题的含义，就是查明观察系统 $S$ 中的指针变量 $O_A$ 是否已与系统 $A$ 的变量 $A$ 恰当关联（即“拥有关于它的信息”）；而这又是个物理问题，其意义在于可以经验地提出：测量 $A$ 与 $O_A$，看二者是否一致。由此产生的无穷倒退，见下文 §3.3。

### 2.3 与其他解释的比较

**教科书** “**哥本哈根**”：在很大程度上，RQM 是标准教科书解释的完成。差别在于：后者假定存在一个经典世界或经典观察者，并描述量子系统在相互作用中如何影响它；关系性解释则假定，对这类相互作用的说明对任何物理系统都成立。因此，RQM 可说是哥本哈根解释的“民主化”版本：单一观察者的某些（并非全部）角色，可由任何物理系统承担。这些已足以定义一个自洽的解释，无须惯常量子测量所要求的退相干与耗散。在 RQM 看来，退相干足够时，教科书解释便浮现出来。

**多世界**：RQM 与多世界解释（见 Vaidman 2018）[^vaidman-2018]皆植根于埃弗雷特（1957）的工作。二者都试图靠增设一层索引性来解开量子理论之谜：在 RQM 中，变量相对于其他物理系统而有值；在多世界中，变量相对于普遍波函数的分支而有值。两种解释都不给测量或观察者任何先天的特殊角色。主要差别在本体论承诺：多世界解释假定，所有相对态都是唯一普遍波函数的分支，而该波函数被当作一个真实实体，服从单一的确定性演化律。于是它必须费力地从这一唯一、确定、连续的普遍波函数中，重新得到海森堡不确定性（借分支索引性）、概率（借概率的主观解释）与离散性；RQM 却把这些直接置于基础之中。反过来，多世界解释建立在一种（有人说膨胀，却）干脆利落的实在论形而上学之上，而这恰为 RQM 的视角主义所不容。若把模态按 Lewis（1986）的方式转换为多世界实在论，以索引性换现实性，二者或许可以靠得更近。

**隐变量**（玻姆）：隐变量理论以玻姆理论（Bohm 1952）[^bohm-1952]为现有最佳范例，为量子力学提供了一种实在论、确定性的解释。RQM 与玻姆理论的相似处，在于对某些变量（如粒子位置）作实在论解释。差别有二。其一，玻姆理论中总是位置具有确定值；RQM 中哪个变量在相互作用中取值，取决于相互作用的性质。其二，玻姆理论中位置始终有确定值，且连续变化；RQM 的本体论则具前文所说的稀疏性。玻姆理论所假定的额外方程，在 RQM 中没有对应物。Drezet（2024）讨论了玻姆理论与 RQM 的关系。

**物理坍缩**：Ghirardi、Rimini 与 Weber（1986）以及 Penrose（1996）式的物理坍缩理论，在物理上可与标准量子力学相区别；RQM 则假定标准量子力学正确，除非出现相反的经验迹象。

另有一些量子力学解释与关系性解释相近：

Zeilinger-Bruckner：关系性解释与 Zeilinger、Bruckner 所发展的量子理论观点相近：（Zeilinger 1999, Brukner & Zeilinger 2003）[^brukner-2003][^zeilinger-1999]独立提出了与 RQM 原初公设类似的公设。这些想法催生了一批有趣的数学工作，意在精确地从信息论公设导出量子理论的形式体系。该纲领中与 RQM 相关的版本，见（Grinbaum 2005; Höhn 2017; Höhn & Wever 2017）[^grinbaum-2005][^höhn-2017][^höhn-2017-2]。

QBism：Rovelli（1996）对信息的强调，影响了 QBism 的诞生（见 Fuchs 1998: 3, 2001, 2002 [Other Internet Resources]）[^fuchs-1998]。RQM 与 QBism 颇有相似（Pienaar 2021b）[^pienaar-2021b]：其一，都强调放弃被认为无意义的问题；其二，都使用信息论语言（Spekkens 2014）[^spekkens-2014]。差别主要在如何对待持有信息的主体。QBism 以 **能动者** 与 **经验** 为基本观念（DeBrota 2018 [Other Internet Resources]），二者在 RQM 中却不起作用：RQM 把主体彻底自然化，主体本身就是一个可由量子理论描述的物理系统。这导向一种强于 QBism 的实在论，也导向对所有变量关系性一面的强调。QBism 的重点，是单一主体所持有的关于世界的信息，并以此为本原；RQM 的信息则是一物理系统关于另一系统所拥有的相对信息（香农意义），并非本原（见 Dorato 2017）[^dorato-2017]：它可以被简单地物理理解为两系统间的关联，且可由第三个系统观察到。Steven French（2024, 2024b）借 Michela Massimi 视角实在论（Massimi 2022）[^massimi-2022]所论的两种视角主义（“perspectival₁”“perspectival₂”），梳理了 QBism 与 RQM 的关系。

Richard Healey：Healey 的实用主义进路（Healey 1989）[^healey-1989]与 RQM 共有如下看法：量子态不是对物理实在的描述，连不完备的描述也不是；其主要功能是充当计算概率的（可弃置的）工具。二者的主要差别，在于强调量子态相对于什么。在 Healey 的实用主义看来，量子态归属 **仅** 相对于某个现实或潜在能动者的视角（Healey 2012）[^healey-2012]；在 RQM 中，值相对于任何物理系统。把量子理论限于能动者的使用，对 Healey 的实用主义哲学并不构成问题；但在自然主义视角下就较为要紧——这种视角寻求对自然的理解，且要求这理解在没有能动者时也依然有意义。这与 RQM 同 QBism 的差别相同，不过 Healey 的立场比 QBism 更近 RQM：QBism 的量子态归属取决于能动者的认知状态，Healey 则只取决于界定该能动者视角的物理环境。

**现象学**：Steven French 从现象学视角讨论了 RQM（2024b, 9.8），指出：倘若 RQM 放弃“观察者不能给自己指派量子态”这一坚持，并能容纳有意识的观察者，则“RQM 与现象学之间有可能达成一种有趣的调和”（2024b, 226 页）。

Cavalcanti 的“**实验形而上学**”：Cavalcanti 把量子预言与关于世界的一般假定相联系的论证加以形式化（Cavalcanti 2008 [Other Internet Resources]），由此导向一种与 RQM 极为接近的观点。

### 2.4 表征

量子力学的解释问题，与能否提供一种 **表征** 有关——即能否对世上发生的事给出直观说明。把不同解释背后的直觉画成简图，或许有用。设想时刻 $t_1$，一个放射性原子被若干盖革计数器环绕；时刻 $t_2$，其中一个计数器的咔嗒响了一声，探测到衰变产物。在 $t_1$ 到 $t_2$ 之间，发生了什么？

- 按 **教科书量子理论**，一个被经典地困于核内的粒子，其波函数会对称地漏出核外，充满核周围的空间；探测发生的那一刻，这波函数在除了咔嗒作响的那台探测器之外的一切地方都魔法般地消失了。
- 按 **多世界** 解释，所有探测器都会响。事实上，每台探测器在每一时刻都在响；只是宇宙的波函数持续分支为无数分支，而我们自己恰处于某一特定分支，其中某台特定探测器在某一特定时刻响了一声。
- 按 **玻姆解释**，波函数同样均匀地漏入空间，但与此同时，与之相伴的粒子受此波函数导引，四处曲折穿行，直到击中某台特定探测器。
- 按 **物理坍缩** 解释，波函数也均匀漏出；然而当它对沉重的盖革探测器的作用开始使过多物质发生位移时，波函数便如教科书解释那样坍缩——只是由一个尚未被明确观测到的假想动力学过程所驱动（Ghirardi 2018）[^ghirardi-2018]。
- RQM 又如何？依海森堡的精神，自然界中并没有实际存在的波函数；在 $t_1$ 与 $t_2$ 之间的任何时刻，也不存在“粒子相对于盖革计数器的位置”这一事实。量子理论中（尤其在 RQM 中）变量未获确定的问题，已在（Calosi and Mariani 2020）[^calosi-2020] 中讨论。不过，其他事实可能存在。例如“粒子相对于途中某个空气分子的位置”。但这些对粒子相对于盖革计数器的位置并无影响；后者要到时刻 $t_2$ 才实现。这一位置的概率分布，并不取决于粒子相对于空气分子的位置。

### 2.5 Frauchiger-Renner 实验与定域性

Frauchiger-Renner 思想实验（Frauchiger & Renner 2018）[^frauchiger-2018]可视为对 RQM 的间接支持：它把“不同的观察者可以对同一组事件给出不同的描述”这句 RQM 的原初口号落实为具体情形。Waaijer 与 van Neerven（2019 [Other Internet Resources]）在 RQM 的概念框架中讨论了这一实验。当然，一切解释都能说明它。

RQM 应用于 EPR 情境与量子非定域问题，最早见于 Smerlak 与 Rovelli（2007）及（Laudisa 2001）[^laudisa-2001]。早期讨论里“RQM 是定域的”这类说法已受质疑：有人指出，RQM 无论如何都“被迫接受量子现象中 **某种** 形式的非定域性”（Laudisa 2019: 227）[^laudisa-2019]。另见 Pienaar 的批评（2019），以及 Martin-Dussaud、Rovelli 与 Zalamea（2019）和（Martin-Dussaud 2021）[^martin-dussaud-2021] 的讨论——其中澄清了从 RQM 视角看量子理论非定域的一个具体含义。

### 2.6 唯我论？

初看之下，RQM 似乎隐含某种视角性唯我论（Rovelli 2024 [Other Internet Resources]）：某系统 $S$ 视角中实现的变量取值，未必等于相对于另一系统 $S'$ 实现的取值。然而情况往往并非如此——这直接来自量子理论本身。关键在于：任何物理比较本身就是一次量子相互作用。设 $S$ 的变量 $A$ 被 $S'$ 测量并存入 $S'$ 的变量 $A'$；这一相互作用便在 $A$ 与 $A'$ 之间建立了关联。于是，第三个系统若测量 $A$ 与 $A'$，将发现二值一致。换言之，$S'$ 与 $S''$ 的视角在这点上彼此一致，且可在物理相互作用中检验。

例如：实验者 $S'$ 测量电子 $S$ 的自旋，并把该自旋值写在一张纸上。原则上，实验者 $S''$ 可以设计一个实验，去探测两个分支（其中电子自旋与纸上文字分别取此值或彼值）之间的干涉效应。但若 $S''$ 测量自旋并读那张纸，她会发现 $S'$ 所见的与自己所见的相同。

  为什么？因为量子理论预言了这一点，可见下文：相对于 $S''$，第一次相互作用产生如下形式的量子态

$$ \begin{align} & \ket{\text{spin up}} \times \ket{\text{paper with text } \lsq\text{spin up}\rsq} \\ & + \ket{\text{spin down}} \times \ket{\text{paper with text } \lsq\text{spin down}\rsq} \end{align} $$

测量自旋，就把态投影到两分支之一；两个分支都通向一致。因此，只要不去追索藏在退相干背后的细微干涉现象，RQM 就意味着我们都“看见同一个世界”。

## 3 一般评论

### 3.1 反应、批评与发展

Bas van Fraassen（2009）细察“RQM 笔下的量子力学世界”（2010: 390），澄清了何者相对观察者、何者不相对。他聚焦于 RQM 显得悖谬的方面。观察者能拥有的信息只能经物理相互作用获得，这一限制在复杂情形下后果惊人。比如：一个观察者作测量，第二个观察者对第一人及其测量对象再作测量，甚至第三个观察者进来，观察涉及前两人的过程。Van Fraassen 的结论是：只要恰当理解 RQM 中对该情形的表征，一切一致性问题都可平息。但另一方面他也指出：在 RQM 中，一个系统相对于某观察者的态本身若不相对于任何东西，便有一个问题。同一个纠缠系统或其组成部分相对于不同观察者的态之间，关系如何？于是他提议增设一条公设，把不同观察者对同一系统的描述弱式地联系起来，禁止视角增殖所容许的破坏性不一致。这一增设公设的想法，后来在 Adlam & Rovelli（2023）中得到发展。

Laura Candiotto（2017）认为，最适合 RQM 的哲学框架是存在结构实在论（OSR）（Ladyman& Ross 2007; French & Ladyman 2011）[^french-2011][^ladyman-2007]。存在结构实在论旨在成为科学实在论的一种可辩护形态（Ladyman 2019）[^ladyman-2019]，主张关系优先于实体——而非自足的个别对象（Morganti 2011）[^morganti-2011]。在 Candiotto 看来，RQM 是一种实在论理论：它把关系（系统与仪器间的物理相互作用）当作初始概念；对象则以关系性“节点”（French 2006）[^french-2006]、或诸过程的交叠处的形式涌现。缺乏观察者独立性，并不等于无力说明物质结构：既然不存在可独立于相互作用而赋予系统的内在性质，这一结构本身就是关系性的，因而尤其依赖观察者。经信息交换的动力学过程形成的关系，可以被当作宇宙的构件。

RQM 与存在结构实在论的关系，Mauro Dorato（2016）亦有强调。Dorato 对 RQM 作了全面评估，指出其主要特征，并强调两点刻画。第一，RQM 对量子理论作修正主义的形而上学说明：凡与当代物理理论相抵触的常识性中心假定，都必须放弃。这里放弃的预设是：量子系统具有非关系、内在的本性。RQM 的形而上学之所以是修正主义的，还有第二重原因。与多世界解释相仿，RQM 并不建议改换量子理论的形式体系（替代性的理论表述才这样做），而是修改我们用以解释形式体系的概念图式，随之修改我们的形而上学。Dorato 指出，取值的相对化会带来对象或实体概念本身的相对化——倘若 (i) 具有某些内在的、非纯然倾向性的性质乃对象同一性所必需，且 (ii) 无内在同一性者不成其为实体（见 Nāgārjuna 1995）[^nāgārjuna-1995]。RQM 中的唯一实在由事件给出：事件是不同量子系统相互作用的结果，但即便是这些事件，也可被不同物理系统以不同方式描述。这种相互作用无法由爱因斯坦意义上的构造性理论（Einstein 1919）[^einstein-1919]更精确地描述——构造性理论能在不把确定结果的出现径直当作基本事实的前提下解释之。Dorato 的结论是：RQM 没有测量问题，因为它隐式地被表述为一条原理理论。他还考虑了 Schaffer（2010）所定义的优先一元论：Shaffer 主张，量子力学的纠缠证明整个宇宙对其部分具有本体论优先性。Dorato 指出，RQM 坚定捍卫关系主义，其后果反而是激进的反对整体论。

Dorato 指出 RQM 的第二个特征：既然如此，把握尚未相互作用之量子系统的本性，最好的办法是诉诸倾向主义。赋予量子系统依赖态的性质以内在性，唯一途径是赋予它们依所受相互作用而以某种方式显现的倾向。倾向主义见于许多其他量子力学观点（Dorato 2006）[^dorato-2006]，在 RQM 语境中却尤为契合。与以能动者为中心的 QBism 式解释不同，RQM 中“$S$ 相对于 $S'$ 显现 $q$”的关系是对称的；这是“量子系统与‘观察者’处于同一层面”这一假设的简单推论。由于其关系性与倾向性，Dorato 强调：RQM 中不可能有普遍生成之流，只可能有局域、依赖世界线的关系性生成。这仍是一种关系性生成：没有普遍涌现之潮，只有纵横交错的涟漪。既然物理系统只有相对于另一系统、而非绝对地，才能例示给定的事件序列，RQM 中便不可能有宇宙时间；于是与广义相对论一样，事件的时间先后也不被视作全序。某种意义上，RQM 中没有宇宙的量子态，也没有上帝之眼的视角——宇宙只能“从某个给定的视角之内”来描述。

Richard Healey 曾在两篇文章中讨论 RQM。第一篇（2021）质疑：在量子引力的语境下，测量结果的观察者相对性能否与科学客观性的基本规范相调和。第二篇（2022）则对 RQM 的主要论题转为更同情的态度——量子测量结果应被视为相对而非绝对的事实——，并将 RQM 与其实用主义量子理论观相较。他论证：Adlam & Rovelli 2023 的 RQM 版本化解了他此前的主要反对（其相对事实的本体论与科学客观性不相容，并削弱量子理论的证据基础），使 RQM 与其实用主义观点更为贴近。

Steven French（2024）讨论了 RQM 与 Fritz London、Edmund Bauer 1939 年给出的量子测量“大陆哲学”说明之间的关系。Andrea Oldofredi（2021）论证 RQM 易与科学实在论相容，其语境是一种性质本体论（Oldofredi 2021）[^oldofredi-2021]；他还讨论了 RQM 解决测量问题的确切方式（Oldofredi 2022）[^oldofredi-2022]。Juan Sebastian Ardenghi 与 Olimpia Lombardi（2022）讨论了 RQM 与模态-哈密顿解释的关系，认为两种解释互补。（Martin-Dussaud, 2023）提出了相对事实概念的数学形式化。

### 3.2 关系性与实在论

RQM 的中心一步，是把所有物理变量解释为关系性的：指涉两个系统而非一个，且只在相互作用中实现。随着我们自然知识的增长，关系性一直扮演着愈来愈主导的角色。例子有：经典力学中速度的关系本性、广义相对论中定域性的关系本性、电磁学中势的关系本性、非阿贝尔规范理论中规范不变可观测量的关系本性，等等。RQM 是此方向上的又一大步。认真对待的话，这种无所不及的关系性，哲学后果可能很重。最要紧的一条：强实在论版本的削弱。

RQM 中没有任何东西与世界“在那里”、独立于我们的心理状态或感知这一假定相抵触。在这个弱的意义上，RQM 与实在论相容。但 RQM 质疑另一个假定：世界的每个子系统、每个变量在每一时刻都有单一的值。在这个更强的意义上，实在论被 RQM 质疑。RQM 的本体论是关系性量子事件的稀疏本体论，不从任何唯一的“底层”表示导出。这种实在论的削弱，与伽利略或爱因斯坦相对性带来的情形方向相似：二者表明，单个物体的速度、或两个类空分离事件的同时性，单独而言并无事实可言。

然而，朝这个方向迈的是激进的一步。Laudisa（2019）指出，RQM 没有就主要过程——量子事件在相互作用中的实现——给出更深层的说明或底层动力学表示；这正是在教科书量子理论中称为测量、并伴随态约化的过程。量子力学给出量子事件发生的概率，却没有一个叙述说明它们如何发生。量子理论的这一核心方面，RQM 并未解决，而是当作世界的一个事实。RQM 解决的是“何时”：每当一个系统影响另一个系统，它便相对于后者发生。RQM 所做的，是表明这一点与干涉效应的存在并不矛盾。但量子事件实现的根本离散性，在 RQM 中并未得到“解释”，而是径直被读作量子理论所刻画的自然运作图景。这在精神上可类比牛顿的著名断言：“凡不是从现象推得的，都必须称为假说；而假说，无论形而上学的还是物理学的，无论基于隐秘性质还是力学性质，在实验哲学中都没有位置。在这门哲学中，特殊命题从现象推得，再经归纳而推广。”（Newton 1713）[^newton-1713]

Timotheus Riedel（2024）强调了 RQM 这一步的激进。Riedel 指出：RQM 必然承诺一个“不受限制的迭代原则”——关于“从某特定视角看事实为何”的事实本身又依赖视角，如此以至于无穷。这一原则对保证事件跨视角的可传达性与一致性至关重要，却与以关系性读相对性的正统读法不相容，于是必须采纳一种视角性事实的概念。其根据在于：在 RQM 中，“系统 $S'$ 拥有关于系统 $S$ 的信息”本身就是耦合系统 $(S, S')$ 的一个偶然性质，因而只能相对于某个系统（可能正是 $S'$ 自己）而言。具体地，只有当某个量子结果实现时，测量才发生——即处在“测量已发生”与“测量未发生”两种情形的叠加之中。因此 RQM 假定，“事实 E 已发生”这类命题没有绝对意义。这种激进视角主义（含其 RQM 版本）的可行性，Peter Evans（2020）近期有讨论，标题为 *Perspectival objectivity Or: how I learned to stop worrying and love observer-dependent reality*。

实在论的这种削弱，是量子力学关系性解释的“代价”。它可与其他解释的“代价”相提并论：多世界解释的本体论膨胀及其本体论与我们所见世界之间的距离，玻姆理论原则上不可观测的变量、以及洛伦兹不变性的丧失，等等。

对这种激进视角主义的一个替代，是把它还原为相对主义（Riedel 2024）[^riedel-2024]：假定变量的值是相对的，但“变量相对于某系统”这一事实是绝对事实，其本身不相对于任何东西——亦即假定每个独一无二的量子事件之实现，本身就是一个基本的绝对物理事件。这种驯化版的 RQM 常被评论者隐含地预设并加以批评。Jacques Pienaar（2021）以五个不可行定理给出这些批评的尖锐版本：相对取值与量子事件的绝对实现之间的平衡难以维持。相关批评另见（Muciño 2022）[^muciño-2022]与（Lawrence 2023）[^lawrence-2023]；回应指出这些论文含有 RQM 所拒绝的隐含假定，见（Rovelli 2021b [Other Internet Resources], Di Biagio & Rovelli 2022 与 Cavalcanti 2023）[^cavalcanti-2023]。

每个“代价”的另一面，是我们或许能从量子理论的经验成功中收获的教训：对多世界解释，教训是其他分支真实存在；对玻姆理论，是挑选特定参照系的不可观测变量真实存在；如此等等。对 RQM，量子理论的教训是：描述不同物理系统相互作用时彼此如何影响（而非物理系统“是”什么），就已穷尽关于物理世界所能说的一切。物理世界必须被描述为一张相互作用组件之网；在这张网里，“孤立系统的态”或孤立系统变量的取值没有意义。物理系统的态，就是它与周围系统保持的关系之网；世界的物理结构，即被确认为这张关系之网。在西方哲学中举足轻重的实体概念，或许不适于说明这门科学；也许“相互依存”（Nāgārjuna 1995）[^nāgārjuna-1995]的观念能提供一个相关的哲学框架（Rovelli 2021）[^rovelli-2021]。

### 3.3 关于跨视角链接的争论

Emily Adlam（2022）论证：否认观察者独立性的量子力学解释，会挑战我们关于测量结果主体间性的预设，而这可能动摇科学事业本身的可能性——科学事业正以这种一致的可能为基础。她说，这类观察者无法跳出自己的视角去了解他人的视角，因而无法确证理论。这一挑战促使她与 Rovelli 为 RQM 增设一条关于视角间关系的特定公设（Adlam & Rovelli 2023）[^adlam-2023]。他们提出一条“跨视角链接”公设：对一个系统的指针的测量，会准确揭示该系统在较早相互作用中记录的结果（除非指针被篡改）。这条公理规定了跨视角交流的可能。

这条公设有两种读法。强读法：把它当作关于视角间关系的绝对陈述。弱读法：把它当作关于某个（可能是更进一步的）观察者所能查明之事的陈述。在弱读法下，公设只导致上文 §2.6 所论的量子形式体系所隐含的物理交流之一致性。

强解释假定，可以实在论地对待全部视角之整体：“把点状量子事件或‘闪光’当作绝对的、观察者独立的关于实在的事实”［Adlam & Rovelli 2023, Adlam 2024］[^adlam-2024][^adlam-2023]——即便这个整体在原则上不对任何人可及。这条路线在 RQM 中是否可行，仍是开放问题：Riedel（2024）的“不受限制的迭代原则”挑战它，若干不可行定理（Pienaar 2021）[^pienaar-2021]亦然。Blake Stacey（2022 [Other Internet Resources]）论证：强解释是从该解释的视角主义向后退了一步，是“投影公设的伪装形式，导致相互作用对的态发生‘全局坍缩’”（Lahti and Pelonpää 2023）[^lahti-2023]。

弱解释下，该公设足以保证享有共同退相干域的能动者之间的主体间性。他们可以积累足够多的、在（DiBiagio 与 Rovelli 2021）[^rovelli-2021]意义上稳定的事实，靠注意概率性规律与归纳发展出理性科学，从而提出并检验物理定律。因此，就研究对象为何达成一致的科学感知共同体，与 RQM 的完全视角主义版本相容。但这仍不足以排除一种可能：相对于该共同体之外的一个进一步观察者，当前科学所具体描述的整个偶然世界，不过是量子叠加中的一项。按这种解释，RQM 不挑战科学事业的理性，却 **确实** 削弱了把事实查明为绝对真实的可能。在这个意义上，RQM 把量子现象解释为对激进视角主义的邀请：相对于某个观察者，我们总可能像朋友之于维格纳。这些方案的近期详尽讨论，见 *Foundation of Physics* RQM 特刊，尤其 Calosi 与 Riedel（2024）的导言。

## References（引用注释）

**以下文献从原文照录，不作翻译；中国文献译为中文。**

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

[^adlam-2022]: Adlam, Emily, 2022, “Does science need intersubjectivity? The problem of confirmation in orthodox interpretations of quantum mechanics”, *Synthese*, 200: 522.
[^adlam-2024]: –––, 2024, “What Does ‘(Non)-Absoluteness of Observed Events’ Mean?” *Foundations of Physics*, 54: 1–43. doi:10.1007/s10701-023-00747-1
[^adlam-2023]: Adlam, Emily and Rovelli, Carlo, 2023, “Information is Physical: Cross-Perspective Links in Relational Quantum Mechanics”, *Philosophy of Physics*, 1(1): 4, 1–19. doi:10.31389/ pop.8
[^ardengi-2022]: Ardengi, Juan Sebastian and Lombardi, Olimpia, 2022, “How Different Interpretations of Quantum Mechanics can Enrich Each Other: The Case of the Relational Quantum Mechanics and the Modal‑Hamiltonian Interpretation”, *Foundation of Physics*, 52: 1–21.
[^bene-2002]: Bene, G., Dieks, D., 2002, “A perspectival version of the modal interpretation of quantum mechanics and the origin of macroscopic behavior”, *Foundation of Physics*, 32: 645–671.
[^bitbol-2010]: Bitbol, Michel, 2010, *De l’intérieur du monde*, Paris: Flammarion. (Relational Quantum Mechanics is extensively discussed in Chapter 2.)
[^bohm-1952]: Bohm, David, 1952, “A Suggested Interpretation of the Quantum Theory in Terms of ‘Hidden’ Variables. I”, *Physical Review*, 85(2): 166–179. doi:10.1103/PhysRev.85.166
[^born-1925]: Born, M. and P. Jordan, 1925, “Zur Quantenmechanik”, *Zeitschrift für Physik*, 34(1): 858–888. doi:10.1007/BF01328531
[^born-1926]: Born, M., W. Heisenberg, and P. Jordan, 1926, “Zur Quantenmechanik. II.”, *Zeitschrift für Physik*, 35(8–9): 557–615. doi:10.1007/BF01379806
[^brown-2009]: Brown, Matthew J., 2009, “Relational Quantum Mechanics and the Determinacy Problem”, *The British Journal for the Philosophy of Science*, 60(4): 679–695. doi:10.1093/bjps/axp017
[^brukner-2003]: Brukner, Časlav and Anton Zeilinger, 2003, “Information and Fundamental Elements of the Structure of Quantum Theory”, in *Time, Quantum and Information*, Lutz Castell and Otfried Ischebeck (eds.), Berlin, Heidelberg: Springer Berlin Heidelberg, 323–354. doi:10.1007/978-3-662-10557-3_21
[^calosi-2020]: Calosi, Claudio and Mariani, Cristian, 2020, “Quantum relational indeterminacy”, *Studies in History and Philosophy of Science Part B* (Studies in History and Philosophy of Modern Physics), 71(C): 158–169.
[^calosi-2021]: Calosi, Claudio and Oldofredi, Andrea, 2021, “Relational Quantum Mechanics and the PBR Theorem: A Peaceful Coexistence”, *Foundations of Physics*, 51: 82.
[^calosi-2024]: Calosi, Claudio and Riedel, Timotheus, 2024, “Relational Quantum Mechanics at the Crossroads”, *Foundations of Physics* 54(74). doi:10.1007/s10701-024-00810-5
[^candiotto-2017]: Candiotto, Laura, 2017, “The Reality of Relations”, *Giornale di Metafisica*, 2017(2): 537–551. [[Candiotto 2017 preprint available online](http://philsci-archive.pitt.edu/14165/)]
[^cavalcanti-2023]: Cavalcanti, E., Di Biagio, A. and Rovelli, C., 2023, “On the consistency of relative facts”, *Foundations of Physics*, 13: 55.
[^di-2021]: Di Biagio, Andrea and Rovelli, Carlo, 2021, “Stable Facts, Relative Facts”, *Foundations of Physics*, 51: 30. doi:10.1007/s10701-021-00429-w
[^di-2022]: –––, 2022, “Relational Quantum Mechanics is About Facts, Not States: A Reply to Pienaar and Brukner”, *Foundations of Physics*, 52: 62.
[^dieks-2022]: Dieks, Dennis, 2022, “Perspectival Quantum Realism”, *Foundations of Physics*, 52: 95.
[^dieks-2019]: –––, 2019, “Quantum reality, perspectivalism and covariance”, *Foundations of Physics*, 49: 629–646.
[^dirac-1925]: Dirac, Paul Adrien Maurice, 1925, “The Fundamental Equations of Quantum Mechanics”, *Proceedings of the Royal Society A: Mathematical, Physical and Engineering Sciences*, 109(752): 642–653. doi:10.1098/rspa.1925.0150
[^dirac-1930]: –––, 1930, *Principles of Quantum Mechanics*, Oxford: Oxford University Press.
[^dorato-2006]: Dorato, Mauro, 2006, “Properties and Dispositions: Some Metaphysical Remarks on Quantum Ontology”, in *Quantum Mechanics*, Angelo Bassi, Detlef Dürr, Tullio Weber and Nino Zanghi (eds), (AIP Conference Proceedings, 844), 139–157. doi:10.1063/1.2219359
[^dorato-2016]: –––, 2016, “Rovelli’s Relational Quantum Mechanics, Anti-Monism, and Quantum Becoming”, in *The Metaphysics of Relations*, Anna Marmodoro and David Yates (eds.), Oxford: Oxford University Press, 235–262. doi:10.1093/acprof:oso/9780198735878.003.0014 [[Dorato 2006 preprint available online](http://arxiv.org/abs/1309.0132)]
[^dorato-2017]: –––, 2017, “Dynamical versus Structural Explanations in Scientific Revolutions”, *Synthese*, 194(7): 2307–2327. doi:10.1007/s11229-014-0546-7 [[Dorato 2017 preprint available online](http://philsci-archive.pitt.edu/10982/.)]
[^dorato-2022]: Dorato, Mauro and Morganti, Matteo, 2022, “What Ontology for Relational Quantum Mechanics?”, *Foundation of Physics*, 52: 66.
[^drezet-2024]: Drezet, Aurélien, 2024, “Can a Bohmian be a Rovellian for all practical purposes?”, *Foundation of Physics*, 53: 30.
[^einstein-1919]: Einstein, Albert, 1919 [1920] “Time, Space, and Gravitation”, Times (London), 28 November 1919, 13–14. Reprinted 1920, *Science*, 51(1305): 8–10. doi:10.1126/science.51.1305.8
[^evans-2020]: Evans, Peter W., 2020, “Perspectival objectivity Or: how I learned to stop worrying and love observer-dependent reality”, *European Journal for Philosophy of Scienc*, 10: 19.
[^everett-1957]: Everett, Hugh, 1957, “‘Relative State’ Formulation of Quantum Mechanics”, *Reviews of Modern Physics*, 29(3): 454–462. doi:10.1103/RevModPhys.29.454
[^frauchiger-2018]: Frauchiger, Daniela and Renato Renner, 2018, “Quantum Theory Cannot Consistently Describe the Use of Itself”, *Nature Communications*, 9: article number 3711. doi:10.1038/s41467-018-05739-8
[^french-2006]: French, Steven, 2006, “Structure as a Weapon of the Realist”, *Proceedings of the Aristotelian Society*, 106(1): 170–187. doi:10.1111/j.1467-9264.2006.00143.x
[^french-2024]: –––, 2024, “Phenomenology, Perspectivalism and (Quantum) Physics”, *Foundations of Physics*, 54: 34.
[^french-2024b]: –––, 2024b, *A Phenomenological Approach to Quantum Mechanics, Cutting the Chain of Correlations*, Oxford: Oxford University Press.
[^french-2011]: French, Steven and James Ladyman, 2011, “In Defence of Ontic Structural Realism”, in *Scientific Structuralism*, Alisa Bokulich and Peter Bokulich (eds.), Dordrecht: Springer Netherlands, 25–42. doi:10.1007/978-90-481-9597-8_2
[^fuchs-1998]: Fuchs, Christopher A., 1998, “Information Gain vs. State Disturbance in Quantum Theory”, *Fortschritte Der Physik*, 46(4–5): 535–565. Reprinted in *Quantum Computation: Where Do We Want to Go Tomorrow?*, Samuel L. Braunstein (ed.), Weinheim: Wiley-VCH Verlag, pp. 229–259.
[^fuchs-2001]: –––, 2001, “Quantum Foundations in the Light of Quantum Information”, in *Decoherence and Its Implications in Quantum Computation and Information Transfer: Proceedings of the NATO Advanced Research Workshop*, Antonios Gonis and P. E. A. Turchi (eds.) Amsterdam: ios press. [[Fuchs 2001 early version available online](https://arxiv.org/abs/quant-ph/0106166)]
[^fuchs-2014]: Fuchs, Christopher A., N. David Mermin, and Rüdiger Schack, 2014, “An Introduction to QBism with an Application to the Locality of Quantum Mechanics”, *American Journal of Physics*, 82(8): 749–754. doi:10.1119/1.4874855
[^ghirardi-2018]: Ghirardi, Giancarlo, 2018, “Collapse Theories”, *The Stanford Encyclopedia of Philosophy* (Fall 2018 Edition), Edward N. Zalta (ed.), [[Ghirardi 2018 available online](https://plato.stanford.edu/archives/fall2018/entries/qm-collapse)].
[^ghirardi-1986]: Ghirardi, G. C., A. Rimini, and T. Weber, 1986, “Unified Dynamics for Microscopic and Macroscopic Systems”, *Physical Review D*, 34(2): 470–491. doi:10.1103/PhysRevD.34.470
[^grinbaum-2005]: Grinbaum, Alexei, 2005, “Information-Theoretic Principle Entails Orthomodularity of a Lattice”, *Foundations of Physics Letters*, 18(6): 563–572. doi:10.1007/s10702-005-1129-0
[^groenewold-1957]: Groenewold, H.J., 1957, “Objective and Subjective Aspects of Statistics in Quantum Description,” in *Observation and Interpretation in the Philosophy of Physics. Proceedings of the Ninth Symposium of the Colston Research Society*, S. Körner (ed.), New York: Dover, pp. 197–203.
[^healey-1989]: Healey, Richard A., 1989, *The Philosophy of Quantum Mechanics: An Interactive Interpretation*, Cambridge: Cambridge University Press. doi:10.1017/CBO9780511624902
[^healey-2012]: –––, 2012, “Quantum Theory: A Pragmatist Approach”, *The British Journal for the Philosophy of Science*, 63(4): 729–771. doi:10.1093/bjps/axr054
[^healey-2021]: –––, 2021, “The Measurement Problem for Emergent Spacetime in Loop Quantum Gravity”, in *Philosophy Beyond Spacetime*, Christian Wüthrich, Baptiste Le Bihan, and Nick Huggett (eds.), Oxford: Oxford University Press.
[^healey-2023]: –––, 2023, “Securing the Objectivity of Relative Facts”, *Foundations of Physics*, 52(4): 1–20.
[^heilbron-2023]: Heilbron, John L. and Rovelli, Carlo, 2023, “Matrix Mechanics Mis-Prized: Max Born’s Belated Nobelization”, *The European Physical Journal* H, 48: 11. doi:10.1140/epjh/s13129-023-00056-1
[^heisenberg-1925]: Heisenberg, W., 1925, “Über quantentheoretische Umdeutung kinematischer und mechanischer Beziehungen.”, *Zeitschrift für Physik*, 33(1): 879–893. doi:10.1007/BF01328377
[^höhn-2017]: Höhn, Philipp Andres, 2017, “Toolbox for Reconstructing Quantum Theory from Rules on Information Acquisition”, *Quantum*, 1(December): article 38. doi:10.22331/q-2017-12-14-38
[^höhn-2017-2]: Höhn, Philipp Andres and Christopher S. P. Wever, 2017, “Quantum Theory from Questions”, *Physical Review A*, 95(1): 012102. doi:10.1103/PhysRevA.95.012102
[^kochen-1967]: Kochen, Simon and E. P. Specker, 1967, “The Problem of Hidden Variables in Quantum Mechanics”, *Journal of Mathematics and Mechanics*, 17(1): 59–87.
[^lahti-2023]: Lahti, P., and Pelonpää. J.-P., 2023, “An Attempt to Understand Relational Quantum Mechanics”, *International Journal of Theoretical Physics*, 62(170). doi:10.1007/s10773-023-05416-7
[^ladyman-2019]: Ladyman, James, 2019, “Structural Realism”, in *The Stanford Encyclopedia of Philosophy* (Fall 2019 edition), Edward N. Zalta (ed.), [[Layman 2007 available online](https://plato.stanford.edu/archives/fall2019/entries/structural-realism/)].
[^ladyman-2007]: Ladyman, James and Don Ross, 2007, *Every Thing Must Go: Metaphysics Naturalized*, Oxford: Oxford University Press. doi:10.1093/acprof:oso/9780199276196.001.0001
[^laudisa-2001]: Laudisa, Federico, 2001, “The EPR Argument in a Relational Interpretation of Quantum Mechanics”, *Foundations of Physics Letters*, 14(2): 119–132. doi:10.1023/A:1012325503383
[^laudisa-2019]: –––, 2019, “Open Problems in Relational Quantum Mechanics”, *Journal for General Philosophy of Science*, 50(2): 215–230. doi:10.1007/s10838-019-09450-0
[^lawrence-2023]: Lawrence, J., Markiewicz, M., Żukowski, M., 2023, “Relative facts of relational quantum mechanics are incompatible with quantum mechanics”. *Quantum*, 7: 1015.
[^leifer-2014]: Leifer, Matthew Saul, 2014, “Is the Quantum State Real? An Extended Review of ψ-Ontology Theorems”, *Quanta*, 3(1): 67. doi:10.12743/quanta.v3i1.22
[^lewis-1986]: Lewis, David K., 1986, *On the Plurality of Worlds*, New York: Blackwell.
[^london-1939]: London, Fritz and Bauer, Edmund, 1939, “La Théorie de L’Observation en Mécanique Quantique”, in *Quantum Theory and Measurement*, J.A. Wheeler and W.H. Zurek (eds.), Princeton: Princeton University Press, 1983. [[London and Bauer 1939 available online](https://www3.nd.edu/~dhoward1/The%20Theory%20of%20Observation%20in%20Quantum%20Mechanics.pdf)].
[^martin-dussaud-2021]: Martin-Dussaud, Pierre, 2021, “Relational Structures of Fundamental Theories”, *Foundations of Physics*, 51: 24.
[^martin-dussaud-2019]: Martin-Dussaud, P., Rovelli, C. and Zalamea, F., 2019, “The Notion of Locality in Relational Quantum Mechanics”, *Foundations of Physics*, 49(2): 96–106.
[^martin-dussaud-2023]: Martin-Dussaud, P., Carette, T., Głowacki, J., Zatloukal, V. and Zalamea, Federico, 2023, “Fact-nets: Towards a Mathematical Framework for Relational Quantum Mechanics”, *Foundations of Physics*, 53: 26.
[^massimi-2022]: Massimi, Michela, 2022, *Perspectival Realism*, Oxford: Oxford University Press.
[^morganti-2011]: Morganti, Matteo, 2011, “Is There a Compelling Argument for Ontic Structural Realism?”, *Philosophy of Science*, 78(5): 1165–1176. doi:10.1086/662258.
[^muciño-2022]: Muciño, R., Okon, E., Sudarsky, D., 2022, “Assessing relational quantum mechanics”, *Synthese*, 200(5): 1–26.
[^newton-1713]: Newton, Isaac, 1713, General Scholium (added to the second edition of *Philosophiae Naturalis Principia Mathematica*), Cambridge, 1713. [[Newton’s *General Scholium* available online](https://isaacnewton.ca/newtons-general-scholium/)
[^nāgārjuna-1995]: Nāgārjuna, c. 2nd century CE [1995], “Mūlamadhyamakakārikā”, Translated in *The Fundamental Wisdom of the Middle Way: Nagarjuna’s “Mulamadhyamakakarika”*, Jay L. Garfield (trans.), Oxford: Oxford University Press, 1995.
[^oldofredi-2021]: Oldofredi, Andrea, 2021, “The Bundle Theory Approach to Relational Quantum Mechanics”, *Foundations of Physics*, 51(1): 1–22.
[^oldofredi-2022]: –––, 2022, “The Relational Dissolution of the Quantum Measurement Problems”, *Foundations of Physics*, 53: 10.
[^penrose-1996]: Penrose, Roger, 1996, “On Gravity’s Role in Quantum State Reduction”, *General Relativity and Gravitation*, 28(5): 581–600. doi:10.1007/BF02105068
[^pienaar-2019]: Pienaar, Jacques, 2019, “Comment on ‘The Notion of Locality in Relational Quantum Mechanics’,” *Foundations of Physics*, 49: 1404–1414.
[^pienaar-2021]: –––, 2021, “A Quintet of Quandaries: Five No-Go Theorems for Relational Quantum Mechanics”, *Foundations of Physics*, 51: 97.
[^pienaar-2021b]: –––, 2021b, “QBism and Relational Quantum Mechanics compared”, *Foundations of Physics*, 51: 1–18.
[^pusey-2012]: Pusey, Matthew F., Jonathan Barrett, and Terry Rudolph, 2012, “On the Reality of the Quantum State”, *Nature Physics*, 8(6): 475–478. doi:10.1038/nphys2309
[^riedel-2024]: Riedel, Timotheus, 2024, “Relational Quantum Mechanics, quantum relativism, and the iteration of relativity”*, Studies in History and Philosophy of Science*, 104: 109–118.
[^rovelli-1996]: Rovelli, Carlo, 1996, “Relational Quantum Mechanics”, *International Journal of Theoretical Physics*, 35(8): 1637–1678. doi:10.1007/BF02302261
[^rovelli-1998]: –––, 1998, “‘Incerto Tempore, Incertisque Loci’: Can We Compute the Exact Time at Which a Quantum Measurement Happens?”, *Foundations of Physics*, 28(7): 1031–1043. doi:10.1023/A:1018889802170
[^rovelli-2018]: –––, 2018, “‘Space Is Blue and Birds Fly through It’”, *Philosophical Transactions of the Royal Society A: Mathematical, Physical and Engineering Sciences*, 376(2123): 20170312. doi:10.1098/rsta.2017.0312
[^rovelli-2021]: –––, 2021, *Helgoland* (Chapter V), London: Penguin.
[^schaffer-2010]: Schaffer, Jonathan, 2010, “Monism: The Priority of the Whole”, *Philosophical Review*, 119(1): 31–76. doi:10.1215/00318108-2009-025
[^schrödinger-1926]: Schrödinger, Erwin, 1926, “Quantisierung als Eigenwertproblem (Zweite Mitteilung)”, *Annalen der Physik*, 384(6): 489–527. doi:10.1002/andp.19263840602
[^smerlak-2007]: Smerlak, Matteo and Carlo Rovelli, 2007, “Relational EPR”, *Foundations of Physics*, 37(3): 427–445. doi:10.1007/s10701-007-9105-0 [[Smerlak and Rovelli 2007 preprint available online](https://arxiv.org/abs/quant-ph/0604064)].
[^spekkens-2014]: Spekkens, Robert, 2014, “The Invasion of Physics by Information Theory”, talk at Perimeter Institute, 26 March 2014, [[Spekkens 2014 available online](http://pirsa.org/14030085/)].
[^strawson-1959]: Strawson, P. F., 1959, *Individuals: An Essay in Descriptive Metaphysics*, London: Methuen.
[^vaidman-2018]: Vaidman, Lev, 2018, “Many-Worlds Interpretation of Quantum Mechanics”, *The Stanford Encyclopedia of Philosophy* (Fall 2018 Edition), Edward N. Zalta (ed.), URL = <[Vaidman 2018 available online](https://plato.stanford.edu/archives/fall2018/entries/qm-manyworlds/)>.
[^fraassen-2009]: van Fraassen, Bas C., 2009, “Rovelli’s World”, *Foundations of Physics*, 40(4): 390–417. doi:10.1007/s10701-009-9326-5 [[van Fraassen 2009 preprint available online](https://www.princeton.edu/~fraassen/articles/pdfs/Rovelli%20publ.pdf)].
[^wigner-1967]: Wigner, Eugene P., 1967, “Remarks on the Mind-Body Question”, in his *Symmetries and Reflections: Scientific Essays of Eugene P. Wigner*, Bloomington, IN: Indiana University Press, pp. 171–184. Reprinted in his *Philosophical Reflections and Syntheses*, Jagdish Mehra (ed.), (The Collected Works of Eugene Paul Wigner 6), Berlin, Heidelberg: Springer Berlin Heidelberg, 247–260. doi:10.1007/978-3-642-78374-6_20
[^zeilinger-1999]: Zeilinger, Anton, 1999, “A Foundational Principle for Quantum Mechanics”, *Foundations of Physics*, 29(4): 631–643. doi:10.1023/A:1018820410908

## 学术工具

* [如何引用本词条](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=qm-relational)。
* [预览本词条的 PDF 版本](https://leibniz.stanford.edu/friends/preview/qm-relational/)，见 [SEP 学会之友](https://leibniz.stanford.edu/friends/)。
* 在 [InPhO](https://www.inphoproject.org/entity?sep=qm-relational&redirect=True) 查找与本词条相关的话题与思想家。
* 在 [PhilPapers](https://philpapers.org/sep/qm-relational/) 查看本词条的增强文献目录及其数据库链接。

## 其他网络资源

- [物理关系还是函数关系？对罗韦利关系性量子力学的一种非形而上学解读](http://philsci-archive.pitt.edu/3506/)，Bitbol, M.，2007，PhilSci Archive 手稿。
- [来自维格纳气泡的视角](https://arxiv.org/abs/2008.05100)，Cavalcanti, Eric G.，2008，arXiv.org 手稿。
- [FAQBism](https://arxiv.org/abs/1810.13401)，DeBrota, J.B. 与 Stacey, B.C.，2018，arXiv.org 手稿。
- [关系性量子力学对简单物理情境的应用](https://philsci-archive.pitt.edu/23375/)，Fano, Vincenzo，2024，PhilSci Archive 手稿。
- [量子力学即量子信息（且仅此而已）](http://arxiv.org/abs/quant-ph/0205039)，Fuchs, Christopher A.，2002，arXiv.org 手稿。
- [关系性量子力学：视角与发展](https://link.springer.com/collections/jbfadjdbae)，Claudio Calosi 客座编辑，*Foundation of Physics* 专刊。
- [对 Mucino-Okon-Sudarsky 关于关系性量子力学之评估的回应](https://arxiv.org/abs/2106.03205)，Rovelli, Carlo，2021b，arXiv.org 手稿。
- [在关系性量子世界中，爱丽丝能否做科学并拥有朋友？唯我论与关系性量子力学](https://arxiv.org/abs/2410.20012)，Rovelli, Carlo，2024，arXiv.org 手稿。
- [关系性量子力学的去关系化](https://arxiv.org/abs/2211.03230)，Rovelli, Carlo，2022，arXiv.org 手稿。
- [Frauchiger—Renner 悖论的关系性分析与过去记录的存在](http://arxiv.org/abs/1902.07139)，Waaijer, Marijn 与 Jan van Neerven，2019，arXiv.org 手稿。
- [一切皆相对：罗韦利找到出路了吗？](http://dwolf.eu/uploads/2/7/1/3/27138059/rqm_essay_dwood.pdf)，Wood, Daniel，2010，未刊手稿。

## 相关词条

龙树 | 属性 | 量子力学 | 坍缩理论 | 埃弗雷特量子力学 | 量子力学的模态解释 | 量子理论的哲学问题 | 量子纠缠与信息 | 量子逻辑和概率论

**（译注：相关词条的中文站内链接将由管线在对应词条重译完成后统一挂接。）**
