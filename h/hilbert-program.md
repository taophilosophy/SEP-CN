# 希尔伯特纲领 Hilbert’s Program (Richard Zach)

*首次发表于 2003 年 7 月 31 日；2023 年 9 月 29 日实质修订。*

20 世纪 20 年代初，德国数学家大卫·希尔伯特（David Hilbert，1862–1943）提出了一项关于经典数学基础的新方案，后来被称为希尔伯特纲领。纲领要求把全部数学形式化为公理形式，并证明这一数学公理化是一致的；而一致性证明本身只许用希尔伯特所谓的“有穷”（finitary）方法来实施。有穷推理的特殊认识论品格，由此给出经典数学所需的辩护。希尔伯特虽然在 1921 年才以这一形式提出纲领，但纲领的各个侧面都植根于他大约自 1900 年以来的基础工作：那一年，他首次指出为分析学给出直接的一致性证明是必要的。20 世纪 20 年代，纲领工作在保罗·贝尔奈斯、Wilhelm Ackermann、冯·诺伊曼与雅克·埃尔布朗（Jacques Herbrand）等逻辑学家的贡献下取得显著进展。它对库尔特·哥德尔也影响巨大：哥德尔关于不完全性定理的工作正是受希尔伯特纲领的推动。人们一般认为，哥德尔的工作表明希尔伯特纲领无法实现。尽管如此，它仍是数学哲学中一个有影响的立场；而且自 20 世纪 30 年代 Gentzen 的工作开始，所谓相对化希尔伯特纲领的工作一直是证明论发展的核心。

## 1 希尔伯特纲领的历史发展

### 1.1 基础问题的早期工作

希尔伯特在数学基础方面的工作，植根于他 19 世纪 90 年代的几何研究，其顶点是影响深远的教科书《几何基础》（*Foundations of Geometry*，1899）（参见“19 世纪几何学”词条）。希尔伯特相信，要严格发展任何科学学科，正确的方式都是公理化进路。在给出公理化处理时，理论将独立于任何对直观的需要而发展；这也便于分析基本概念与公理之间的逻辑关系。对希尔伯特来说，公理的独立性、尤其是一致性的研究，在公理化处理中头等重要。就几何公理而言，只要在实平面上给系统一个解释，便能证明其一致性；几何的一致性由此被还原为分析学的一致性。而分析学的基础本身，又要求一个公理化与一个一致性证明。希尔伯特在（1900b）中给出了这样的公理化；但人们很快看清，分析学的一致性面临重大困难。原因之一，是戴德金为分析学奠基的通行做法依赖可疑的假设——它们与导致集合论悖论的假设相近，也与弗雷格算术基础中的罗素悖论相近。

希尔伯特由此认识到：需要的是分析学的 **直接** 一致性证明，即不以还原到另一理论为据的证明。1900 年国际数学家大会演讲（1900a）中，他把寻找这样一个证明列为 23 个数学问题中的第二个；海德堡演讲（1905）则给出这样一个证明的概要。若干因素推迟了希尔伯特基础纲领的进一步发展。其一也许是庞加莱（1906）的批评：在庞加莱看来，希尔伯特所概述的一致性证明对归纳的用法是恶性循环（见 Steiner 1975, Appendix）[^steiner-1975]。希尔伯特还认识到，公理化研究需要一个成熟的逻辑形式系统。他当时依赖基于代数传统的逻辑观念，特别是施罗德的工作；这种逻辑观念并不特别适合充当数学公理化的形式系统。（关于希尔伯特纲领的早期发展，见 Peckhaus 1990。）[^peckhaus-1990]

### 1.2 《数学原理》的影响

罗素与怀特海《数学原理》（*Principia Mathematica*）的出版，为重新进攻基础问题提供了所需的逻辑基础。自 1914 年起，希尔伯特的学生贝曼（Heinrich Behmann）等人着手研究《数学原理》系统（关于贝曼在希尔伯特学派中的角色，见 Mancosu 1999）[^mancosu-1999]。希尔伯特本人则在 1917 年回到基础问题。1917 年 9 月，他向瑞士数学会作题为“公理化思想”（Axiomatic Thought，1918a）的演讲；这是他自 1905 年以来第一个发表的数学基础贡献。演讲中，他再次强调对公理系统一致性证明的要求。他写道：“公理理论的首要要求必须更进一步［而不只是避开已知悖论］，即表明在每一个知识领域中，基于底层公理系统的矛盾 **绝对不可能** 出现。”他把算术（以及集合论）的一致性证明重新列为主要的未决问题。在这两种情形下，除逻辑本身之外，似乎再没有更基本的东西可供一致性还原；而希尔伯特当时认为，这一问题已被罗素在《数学原理》中的工作基本解决。尽管如此，公理化的其他基础问题仍未解决，其中包括“每一个数学问题的可判定性”问题——它同样可追溯到希尔伯特 1900 年的演讲。

这些公理化的未决问题，促使希尔伯特在随后几年投入大量精力研究逻辑。1917 年，贝尔奈斯作为助手来到哥廷根。在 1917–1921 年的一系列课程中，希尔伯特在贝尔奈斯与贝曼的协助下，对形式逻辑作出了显著的新贡献。1917 年的课程（Hilbert, 1918b）尤其包含对一阶逻辑的精巧发展，并构成希尔伯特与 Ackermann 教科书《理论逻辑原理》（*Principles of Theoretical Logic*，1928）的基础（见 Ewald and Sieg 2013、Sieg 1999、Zach 1999 与 2003）[^ewald-2013][^sieg-1999][^sieg-2013][^zach-1999]。

### 1.3 有穷主义与一致性证明的探求

然而在随后几年中，希尔伯特转而拒绝罗素对算术一致性问题的逻辑主义解决方案。与此同时，布劳威尔的直觉主义数学渐成风气；特别是，希尔伯特先前的学生赫尔曼·外尔皈依了直觉主义。外尔的论文“数学中的新基础危机”（1921）得到希尔伯特在 1921 年夏汉堡三次演讲（1922b）的回应。在那里，希尔伯特提出了自己解决数学基础问题的方案。这一方案吸收了他 1904 年关于直接一致性证明的想法与他对公理系统的观念，也吸收了罗素在数学公理化工作中的技术发展，以及他本人与其合作者的进一步发展。新颖之处在于：希尔伯特想以有穷观点（the finitary point of view）赋予其一致性纲领以回应布劳威尔与外尔批评所需的哲学意义。

希尔伯特认为，数学中有一个特权部分，即内容性的初等数论；它只依赖“具体符号的纯粹直观基础”。抽象概念的运算被视为“不充分且不可靠”；与之相对，却存在这样一个领域：

> 超逻辑的离散对象，它们作为直接经验先于一切思想而直观地在场。逻辑推理若要可靠，就必须能在一切部分上完全通览这些对象；它们的出现、彼此的差异、先后相继（或相连成串）则必须连同对象本身一起，直接而直观地被给予我们，成为既不能还原为他物、也不需要还原的东西。（Hilbert 1922b, 202；此段在 Hilbert 1926, 376、Hilbert 1928, 464 与 Hilbert 1931b, 267 中几乎逐字重复）[^hilbert-1922b][^hilbert-1926][^hilbert-1928][^hilbert-1931b][^hilbert-1928-2]

对希尔伯特而言，这些对象是 **符号**（signs）。内容性数论的领域由有穷数字构成，即笔画序列。它们没有意义——不代表任何抽象对象——但可以对它们作运算（如连接）与比较。关于其性质与关系的知识是直观的，不经逻辑推理中介。依希尔伯特之见，如此发展出来的内容性数论是安全的：矛盾不可能出现，因为内容性数论的命题中根本不存在逻辑结构。

对符号作直观—内容性的运算，构成希尔伯特元数学的基础。正如内容性数论对笔画序列作运算，元数学也对符号序列（公式、证明）作运算。公式与证明可以被句法地操作；公式与证明的性质与关系，同样基于一种无需逻辑的直观能力；这种能力保证：经由这类句法运算，我们能确定地认识公式与证明。而数学本身处理抽象概念，如量词、集合、函数，并使用基于数学归纳法或排中律等原则的逻辑推理。这些“概念构成”与推理方式受到布劳威尔等人的批评，理由是它们预设无穷总体为给定的，或涉及非直谓定义（批评者视之为恶性循环）。希尔伯特的目标正是为它们辩护。为此他指出，这些都可以在公理系统（如《数学原理》的系统，或希尔伯特本人发展的系统）中被形式化。数学命题与证明由此变成公式，以及依严格界定的推导规则从公理出发的推导。用希尔伯特的话说，数学“变成可证明公式的清单”。如此，数学证明便服从元数学的、内容性的研究。于是，希尔伯特纲领的目标就是给出这样一个证明：在元数学层面、以内容性的方式，证明不可能推出矛盾，即不可能有对公式 $A$ 与其否定 $\neg A$ 的形式推导。

这一纲领目标的概要，由希尔伯特及其合作者在随后十年中充实。在概念方面，有穷观点与一致性证明的策略由希尔伯特（1928）、希尔伯特（1923）、希尔伯特（1926）以及贝尔奈斯（1928b）、贝尔奈斯（1922）、贝尔奈斯（1930）阐发；其中希尔伯特的文章“论无限”（1926）对有穷立场作了最详细的阐述。除希尔伯特与贝尔奈斯之外，另有若干人参与纲领的技术工作。在哥廷根的讲演中（Hilbert and Bernays, 1923; Hilbert, 1922a），希尔伯特与贝尔奈斯发展了 $\varepsilon$-演算，作为他们为算术与分析公理系统选定的最终形式系统。希尔伯特还在那里提出了以他所谓的 $\varepsilon$-替换法给出一致性证明的进路。Ackermann（1924）尝试把希尔伯特的想法扩展到一个分析系统，但该证明是错误的（见 Zach 2003）[^zach-2003]。当时正在哥廷根访问的冯·诺伊曼，于 1925 年（1927 年发表）为 $\varepsilon$-形式系统（不包括归纳公理）给出一个修正的一致性证明。在冯·诺伊曼工作的基础上，Ackermann 设计了一个新的 $\varepsilon$-替换程序并告知贝尔奈斯（见 Bernays 1928b）[^bernays-1928b]。在 1928 年博洛尼亚国际数学家大会的演讲“数学基础的问题”（1929）中，希尔伯特乐观地宣称，Ackermann 与冯·诺伊曼的工作已确立数论的一致性。他还说，分析学的证明已由 Ackermann 完成，“达到只剩一个纯算术的初等有穷性定理有待证明的程度”。

### 1.4 哥德尔不完全性定理的冲击

哥德尔的不完全性定理表明，希尔伯特的乐观为时过早。1930 年 9 月，库尔特·哥德尔在柯尼斯堡的一次会议上宣布第一个不完全性定理。在场的冯·诺伊曼立即认识到该结果对希尔伯特纲领的意义。会后不久，他写信给哥德尔，说自己找到了哥德尔结果的一个推论。而哥德尔此前已独立得到同一结果：第二个不完全性定理——它断言，《数学原理》系统不证明“《数学原理》系统一致”这一形式化命题（假如它一致的话）。然而，此前一致性证明所用的全部有穷推理方法，都被认为可在《数学原理》中形式化。因此，若《数学原理》的一致性能用 Ackermann 证明所用的方法证明，那么这个证明就应当能在《数学原理》中形式化；但第二个不完全性定理恰断言这不可能。贝尔奈斯在 1931 年 1 月研读哥德尔的论文后，也立即意识到其重要性。他在给哥德尔的信中写道（在假定有穷推理可在《数学原理》中形式化的前提下）：不完全性定理表明，《数学原理》的有穷一致性证明不可能。此后不久，冯·诺伊曼证明 Ackermann 的一致性证明有缺陷，并为所提出的 $\varepsilon$-替换程序给出一个反例（见 Zach 2003）[^zach-2003]。

1936 年，Gentzen 发表了一阶皮亚诺算术（$\text{PA}$）的一致性证明。哥德尔已证明这是必需的：Gentzen 的证明采用了 $\text{PA}$ 本身无法形式化的方法，即沿序数 $\varepsilon_0$ 作超限归纳。Gentzen 的工作标志着后哥德尔证明论以及相对化希尔伯特纲领工作的开端。Gentzen 传统中的证明论，按证明各系统一致性所需的有穷观点的扩张来分析公理系统。通常，系统的证明论强度以 **证明论序数** 度量，即沿其作超限归纳便足以证明一致性的那个序数；对 $\text{PA}$ 而言，该序数是 $\varepsilon_0$。（进一步讨论，见“证明论”与“证明论的发展”词条。）

## 2 有穷观点

希尔伯特数学哲学的基石，也是他自 1922b 起基础思想中实质上新颖的方面，是他所谓的有穷立场。这一方法论立场在于：把数学思想限定于“作为直接经验先于一切思想而直观地在场”的对象。它还要求，关于这些对象的运算与推理方法不引入抽象概念，尤其不诉诸完成了的无穷总体。

理解希尔伯特的有穷立场，有几个基本且相互关联的问题：

1. 有穷推理的对象是什么？
2. 哪些命题在有穷意义上有意义？
3. 哪些构造与推理方法是有穷地可接受的？

### 2.1 有穷对象与有穷主义认识论

希尔伯特在一段著名文字中刻画了有穷推理的领域；这段话在 20 世纪 20 年代希尔伯特所有较偏哲学的论文中表述大体相同（1931b; 1922b; 1928; 1926）：

> 作为使用逻辑推理、进行逻辑运算的条件，我们的表象能力须先被给予某种东西，即某些超逻辑的具体对象；它们作为直接经验，先于一切思想而直观地在场。逻辑推理若要可靠，就必须能在一切部分上完全通览这些对象；而它们出现、彼此有别、先后相继或相连成串这一事实，是连同对象本身一起被直接地、直观地给予的，既不能还原为任何别的东西，也不需要还原。这就是我认为数学、乃至一切科学思维、理解与交流所必需的基本哲学立场。（Hilbert, 1926, 376）

对希尔伯特来说，这些对象是 **符号**。就内容性数论的领域而言，所涉及的符号是诸如

> 1, 11, 111, 11111

希尔伯特究竟如何理解这些数字，很难回答。它们不是物理对象（例如纸上实际的笔画），因为总须能够再添一画来扩展一个数字（而且正如希尔伯特在“论无限”（1926）中也论证的，物理宇宙是否无限颇可怀疑）。按希尔伯特（1922b, 202）的说法，它们的“形状可以被我们普遍而确定地识别——独立于空间与时间、独立于符号产生时的特殊条件、也独立于成品中无关紧要的差异”。它们也不是心理构造：其性质是客观的，其存在却依赖直观的构造（见 Bernays 1923, 226）[^bernays-1923]。无论如何，有一点很清楚：它们在逻辑上原始，既不是概念（像弗雷格的数），也不是集合。这里首要的问题在于：它们不进入逻辑关系——例如不能对它们作任何谓述。至于其形而上学地位（按这些术语的通行意义，是抽象还是具体），倒在其次。在贝尔奈斯最成熟的有穷主义表述中（Hilbert and Bernays, 1939; Bernays, 1930），有穷主义的对象被刻画为 **形式对象**，由一个重复过程递归生成；笔画符号则是这些形式对象的具体表示。

希尔伯特认为有穷主义对象具有何种认识论地位，这个问题同样难以回答。要完成给无穷主义数学提供安全基础的任务，对有穷对象的通达就必须直接而确实。希尔伯特的哲学背景大体是康德式的，贝尔奈斯亦然——他密切隶属哥廷根以伦纳德·纳尔逊（Leonard Nelson）为中心的新康德主义学派。希尔伯特对有穷主义的刻画常常提到康德式直观，并把有穷主义对象说成直观地被给予者。的确，在康德认识论中，直接性是直观知识的定义性特征。问题在于：这里起作用的是哪一种直观？Mancosu（1998b）指出了这方面的一个转变：他论证说，希尔伯特早期论文中的直观是感性直观，后来著作中（如 Bernays 1928a）[^bernays-1928a] 则认定为康德意义上的纯粹直观。然而大约同时，希尔伯特（1928, 469）仍把起作用的直观认定为感性直观。在（1931b, 266–267）中，希尔伯特把有穷的思想方式看作除纯粹直观（如空间直观）与理性之外的又一个 **先天** 知识来源，声称自己“识别并刻画了伴随经验与逻辑的第三个知识来源”。贝尔奈斯与希尔伯特都以大体康德式的措辞为有穷知识辩护（尽管未走到给出先验演绎的地步）。他们把有穷推理刻画为一切数学乃至一切科学思维所依赖的推理——没有它，这类思想便不可能。（关于有穷主义的认识论，见 Kitcher 1976 与 Parsons 1998；关于希尔伯特符号理论的历史与哲学语境，见 Patton 2014；关于随后与德国哲学家 Aloys Müller 的辩论，特别见 Eder（即出）。）

### 2.2 有穷地有意义的命题与有穷推理

关于有穷数字的最基本判断，是相等与不相等。此外，有穷立场允许对有穷对象作运算，其中最基本的是连接。数字 11 与 111 的连接记作“$2 + 3$”；“11 与 111 连接所得的数值同 111 与 11 连接所得的数值相同”这一陈述，则记作“$2 + 3 = 3 + 2$”。在实际的证明论实践中，以及在（Hilbert and Bernays, 1934; Bernays, 1930）中明确地，这些基本运算被推广为递归定义的运算，典型的是原始递归，例如乘法与指数运算（关于指数运算相关的哲学困难，见 Parsons 1998；关于直观数学与有穷主义的扩展讨论，见 Parsons 2007）[^parsons-1998]。同样，有穷判断不仅可以涉及相等或不相等，还可以涉及基本的可判定性质，例如“是素数”。只要这类性质的特征函数本身有穷，它便是有穷可接受的。例如，把一个数字在其为素数时变换为 1、否则变换为 11，这一运算可用原始递归定义，因而是有穷的。这样的有穷命题可以由合取、析取、否定等通常的逻辑运算组合，也可以由有界量化组合。（Hilbert, 1926）举出“在 $p + 1$ 与 $p! + 1$ 之间有一个素数”这一命题为例，其中 $p$ 是某个大素数。该陈述是有穷可接受的，因为它“只是用来缩写”如下命题：$p + 1$ 或 $p + 2$ 或 $p + 3$ 或……或 $p! + 1$ 是素数。

成问题的有穷命题，是那些表达关于数字的普遍事实的命题，例如：对任何给定数字 $n, 1+n = n+1$。它成问题，是因为用希尔伯特的话说，它“从有穷主义观点看 **不可能被否定**”（1926, 378）。他这话的意思是：那个矛盾命题——存在一个数字 $n$ 使 $1+n \ne n+1$——不是有穷地有意义的。“毕竟，人不可能把所有数都试一遍”（1928, 470）。出于同一理由，一个有穷的普遍命题不应被理解为无穷合取，而“只应理解为一个假设性判断：当给出一个数字时，它才断言某种东西”（同上）。尽管在此意义上成问题，普遍的有穷陈述对希尔伯特证明论却特别重要，因为形式系统 $S$ 的一致性陈述正是这种普遍形式：对任何给定的公式序列 $P$，$P$ 都不是 $S$ 中矛盾的推导。

### 2.3 有穷运算与有穷证明

对理解有穷主义与理解希尔伯特证明论都至关重要的是：从有穷主义立场看，应当允许哪些运算与哪些证明原则？必须给出一般答案。这一点从希尔伯特证明论的要求即可看清。不能指望给定一个数学形式系统（甚至一个公式序列），人就能“看出”它一致，或看出它不可能是真正的不一致推导——一如我们能看出 $11 + 111 = 111 + 11$。一致性证明所需的，是一个把给定形式推导变换为特殊形式推导的运算，外加两项证明：该运算确实做到这一点，以及特殊种类的证明不可能是矛盾证明。要算作有穷一致性证明，该运算本身必须从有穷主义立场可接受，而所需的证明必须只用有穷可接受的原则。

希尔伯特从未给出关于哪些运算与证明方法从有穷主义立场可接受的一般说明，只给出他视为有穷的内容性有穷数论中的运算与推理方法实例。内容性归纳在施用于假设性、普遍性的有穷陈述时，在希尔伯特（1922b）中被明确接受。他（1923, 1139）说直观思维“包含对有限既有总体的递归与直观归纳”，并在 1928 年的一个例子中使用了指数运算。贝尔奈斯（1930）解释了指数运算如何可理解为对数字的有穷运算。希尔伯特与贝尔奈斯（1934）给出关于有穷内容性数论的唯一一般说明。据此，原始递归定义的运算与使用归纳的证明，都有穷可接受。所有这些方法都能在一个称为原始递归算术（$\text{PRA}$）的系统中形式化，该系统允许以原始递归定义函数，并对无量词公式作归纳（同上）。然而，希尔伯特与贝尔奈斯都未曾断言 **只有** 原始递归运算才算有穷；事实上，他们早在 1923 年就在表面上有穷的一致性证明中使用了一些非原始递归的方法（见 Tait 2002 与 Zach 2003）[^tait-2002][^zach-2003]。

更有趣的概念问题是：哪些运算 **应当** 被视为有穷的。希尔伯特对有穷立场究竟何在不完全清楚；因此，分析有穷主义运算与证明须满足哪些约束（认识论的及其他方面的），便留有一定余地。希尔伯特（见上文）把有穷数论的对象刻画成这样：它们“直观地被给予”，“在所有部分上可通览”。他还说，它们具有基本性质这一点必须对我们“直观地存在”。贝尔奈斯（1922, 216）提出，在有穷数学中只有“原始直观认知发挥作用”，并在 1930, 250 处结合有穷主义使用“直观明见性的观点”一语。把有穷主义主要视为关乎 **直观** 与直观知识的这一刻画，尤其为（Parsons, 1998）所强调；他论证说，按这种理解，能算作有穷的至多是那些可由加法与乘法经有界递归定义的算术运算。特别是，据他之见，指数运算与一般原始递归都不是有穷可接受的。

有穷主义与原始递归推理相重合这一论题，得到（Tait 1981；另见 2002, 2005b, 2019）[^tait-1981] 的有力辩护。与 Parsons 不同，Tait 拒绝把直观中的可表象性当作有穷的标志；相反，他把有穷推理视为“一切关于数的非平凡数学推理所预设的一种最小推理”，并把有穷运算与证明方法分析为隐含在“数是有限序列的形式”这一概念之中的东西。这一有穷主义分析得到希尔伯特以下主张的支持：有穷推理是逻辑与数学、乃至一切科学思维的前提（Hilbert 1931b, 267）。既然有穷推理是一切关于数的非平凡推理所预设的那部分数学，那么用 Tait 的话说，它在笛卡尔意义上是“不可怀疑的”；而这种不可怀疑性，正是有穷推理为数学提供希尔伯特所意图的认识论基础所需要的一切。

Kreisel（1960）提出另一种关于有穷证明的有趣分析，尽管它未提供同样详细的哲学辩护。其结果是：恰好那些能在一阶算术 $\text{PA}$ 中可证全的函数，才是有穷的。它基于反射原则这一证明论概念；更多细节见 Zach（2006），分析见 Dean（2015）。Kreisel（1970, Section 3.5）通过聚焦于什么“可视觉化”给出另一种分析，结果相同：有穷可证明性与 $\text{PA}$ 中的可证明性外延相同。

Tait 的技术分析得出：有穷主义函数恰好是原始递归函数，有穷主义数论真理恰好是在原始递归算术理论 $\text{PRA}$ 中可证明者。须强调，这一分析并非从有穷主义观点内部作出。由于“函数”与“证明”这些一般概念本身并非有穷的，有穷主义者无法理解 Tait 的论题——凡在 $\text{PRA}$ 中可证明者皆有穷主义地真。按 Tait 的看法，对有穷主义可证明性的恰当分析不得假定有穷主义本身能使用这类非有穷主义概念；Kreisel 的进路以及某些依赖反射原则或 $\omega$-规则对 Tait 的批评，都违反了这一要求（见 Tait 2002, 2005b）[^tait-2002]。另一方面也可论证：$\text{PRA}$ 作为“一切关于数的非平凡数学推理所预设者”的形式化太强。存在一些较弱但仍非平凡的理论，它们与比原始递归函数更小的函数类相关，例如 $\text{PV}$ 与 $\text{EA}$，分别与多项式时间函数和 Kalmar 初等函数相关（关于在 $\text{EA}$ 中能开展多少数学，见 Avigad 2003）[^avigad-2003]。Ganea（2010）以与 Tait 类似的分析，得出相应的 Kalmar 初等函数类为有穷主义函数类。关于有穷主义不同概念的进一步分析，另见 Incurvati（2019）。

## 3 形式主义、还原论与工具主义

外尔（1925）是对希尔伯特 1922b 与 1923 年方案的一种调停性回应，其中也包含若干重要批评。外尔把希尔伯特的事业描述为以无意义的公式游戏取代内容数学。他指出，希尔伯特想“确保的不是 **真**，而是分析学的 **一致性**”。他提出一个批评（呼应弗雷格早先的批评）：为什么应当以形式系统的一致性为据，去相信它所编码的前形式数学是真的？希尔伯特那份无意义的公式清单，难道不只是“分析学的无血幽灵”？外尔提出了一个解决方案：

> 数学若要继续作为一项严肃的文化关切，就必须赋予希尔伯特的公式游戏某种 **意义**；而我只看到一种可能：赋予它（包括其超限成分）一种独立的智识意义。理论物理学为我们提供了伟大的范例：那是一种与通常知识或现象知识性质完全不同的知识，后者纯粹表达直观中被给予的东西。在前一种情形中，每个判断都有其自身完全可在直观中实现的意义；理论物理学的陈述则绝非如此——在那里，面对经验时成问题的是 **系统整体**。（Weyl, 1925, 140）

与物理学的类比十分醒目；在希尔伯特自己的文字中，也能找到类似想法——或许他在这方面受到外尔的影响。希尔伯特最初的方案只专注于一致性，但他的思想有明显进展：朝着一种一般的还原论事业，而这在当时的科学哲学中相当常见（Giaquinto 1983 已指出此点）[^giaquinto-1983]。20 世纪 20 年代后半期，希尔伯特以保守性纲领取代一致性纲领：形式化数学应类比理论物理学来考虑。理论部分的最终辩护在于它相对“实在”数学的保守：理想数学每证明一个“实在”命题，该命题在直观上也为真。这就为超限数学的使用提供了辩护：它不仅内部一致，而且只证明真的直观命题（并且证明全部直观命题，因为直观数学的形式化本就是全部数学形式化的一部分）。

1926 年，希尔伯特引入实在公式与理想公式的区分。这一区分在 1922b 中尚未出现，在 1923 年只是有所暗示。在后一文中，希尔伯特先给出一个无量词数论的形式系统，并说“我们如此获得的可证明公式全都具有有限者的品格”（1139）；然后加入超限公理（即量词），以简化并完成该理论（1144）。他在这里首次作与理想元素方法的类比。他写道：“在我的证明论中，超限公理与公式被附加到有限公理上，正如在复变量理论中虚元素被附加到实在元素上，也正如在几何学中理想构造被附加到实际构造上”（同上）。希尔伯特在 1926 年明确引入理想命题概念，在 1928 年又首次在理想命题之外谈到 **实在命题**；此时他相当清楚：理论的实在部分只由可判定的、无变元公式构成。它们被设定为“直接可核验的”——类似于由自然律得出、可用实验检验的命题（1928, 475）。纲领的新图景是：经典数学要在一个系统中形式化，该系统包含内容性有穷数论中一切直接可核验（通过计算）命题的形式化。一致性证明应当表明：凡可由理想方法证明的实在命题都为真，即都能通过有穷计算直接核验。（诸如 $\varepsilon$-替换的实际证明一直属于此类：提供有穷程序，从实在陈述的证明中消去超限要素，尤其是从 $0 = 1$ 的证明中。）事实上，希尔伯特看出还有更强的结论：一致性证明不仅确立由理想方法可证明的实在公式为真；只要相应的自由变元公式可由理想方法推出，它还给出有穷普遍命题的有穷证明（1928, 474）。

除保守性之外，希尔伯特还建议对理论施加进一步限制：简单、证明简短、“思想节约”以及数学生产力。超限逻辑的形式系统并非任意：“这个公式游戏依某些确定规则进行，其中表达着我们思维的 **技术**。……我的证明论的根本想法不是别的，就是描述我们知性的活动，为我们的思维实际遵循的规则作记录”（Hilbert 1928, 475）[^hilbert-1928][^hilbert-1928-2]。当外尔（1928）最终背离直觉主义时，他强调的正是希尔伯特证明论的这一动机：不是把数学变成无意义的符号游戏，而是把它变成一门将科学（数学）的实践加以编纂的理论科学。（关于外尔与直觉主义及希尔伯特形式主义的关系，见 Mancosu and Ryckman 2002 与 Kish Bar-On 2021）[^mancosu-2021][^mancosu-2002]。

因此，希尔伯特的形式主义相当精致：它避开了两个关键反驳。（1）如果系统的公式没有意义，系统内的可推导性如何能产生任何信念？（2）为什么接受 $\text{PA}$ 系统，而不是其他任何一致的系统？这两个反驳在弗雷格那里都很熟悉；两个问题都（部分地）由关于实在陈述的保守性证明来回答。对（2），希尔伯特另有一个自然主义的接受标准：我们在选择系统时，受简单性、丰产性、一致性以及数学家实际所作所为的约束；外尔则会补充说，理论的最终检验是它在物理学中的用处。

大多数论述希尔伯特的数学哲学家都把他读作工具主义者（包括 Kitcher 1976、Resnik 1980、Giaquinto 1983、Sieg 1990，尤其是 Detlefsen 1986）[^detlefsen-1986][^giaquinto-1983][^kitcher-1976][^resnik-1980][^sieg-1990]。这些学者把希尔伯特关于理想命题“本身没有意义”（Hilbert, 1926, 381）的解释，读作经典数学只是 **纯粹的** 工具、超限数学的陈述没有真值。若这一读法准确，它就必须被理解为一种方法论工具主义：证明论纲领的成功执行将表明，人可以假装 **仿佛** 数学没有意义。因此，与物理学的类比并不是“超限命题没有意义，正如包含理论词的命题没有意义”，而是“超限命题无需直接的直观意义，正如人不必直接看见电子才能对它们作理论”。Hallett（1990）考虑到希尔伯特出身的 19 世纪数学背景，以及希尔伯特整个生涯的已刊与未刊文献（尤其是 Hilbert 1992，对理想元素方法最广泛的讨论）[^hilbert-1992]，得出如下结论：

> ［希尔伯特对哲学问题的处理］ **并非** 意在成为一种关于存在与真理之类的工具主义不可知论。恰恰相反，它意在为这类问题提供非怀疑论的、积极的解决方案，且以认知上可通达的措辞表述。看来，同一方案对数学理论与物理理论都成立。一旦新概念、“理想元素”或新的理论词被接受，它们便以 **任何** 理论实体存在的方式存在。（Hallett, 1990, 239）

## 4 希尔伯特纲领与哥德尔的不完全性定理

关于哥德尔不完全性定理对希尔伯特纲领的冲击，以及究竟是第一个还是第二个不完全性定理给出了 **致命一击**，一直存在争论。毫无疑问，最直接参与相关发展的人都确信这些定理具有决定性冲击。哥德尔在 1930 年 10 月发表的一则摘要中宣布第二个不完全性定理。其内容是：对《数学原理》、策梅洛—弗兰克尔集合论，或 Ackermann 与冯·诺伊曼所研究的那类系统，用可在这些系统中表述的方法，不可能给出一致性证明。在论文完整版中，哥德尔（1931）留有余地：可能存在某些有穷方法，它们无法在这些系统中形式化，却能给出所需的一致性证明。贝尔奈斯 1931 年 1 月致哥德尔的信中，第一反应亦然。他写道：“如果像冯·诺伊曼那样，把任何有穷考虑都可在系统 $P$ 中形式化视为确定——像您一样，我根本不认为这已成定论——那么结论就是：$P$ 的一致性不可能有有穷演证”（Gödel, 2003a, 87）。

哥德尔的定理如何冲击希尔伯特纲领？通过对符号序列（公式、证明）作细致的（“哥德尔”）编码，哥德尔表明：在包含足够多算术的理论 $T$ 中，可以构造一个公式 $Pr(x, y)$，它“说”$x$ 是（编码为）$y$ 的（公式的）证明。具体地说，若 $\ulcorner 0 = 1\urcorner$ 是公式 $0 = 1$ 的编码，那么 $Con_T = \forall x \neg Pr(x,\ulcorner 0 = 1\urcorner)$ 可以视为“说”$T$ 一致（没有数是 $T$ 中 $0 = 1)$ 的推导的编码）。第二个不完全性定理（G2）说：在对 $T$ 与编码装置的某些假定下，$T$ 不证明 $Con_T$。现在假设 $T$ 有一个有穷一致性证明。这种证明所用的方法想必可在 $T$ 中形式化。（“可形式化”大致是说：如果该证明使用推导上的有穷运算 $f$，把任何推导 $D$ 变换为简单形式的推导 $f (D)$；那么就有一个公式 $F(x, y)$，使得对所有推导 $D,T \vdash F(\ulcorner D\urcorner ,\ulcorner f (D)\urcorner)$。）$T$ 的一致性将有穷地表达为这个普遍假设：若 $D$ 是任何给定的符号序列，则 $D$ 不是 $T$ 中公式 $0 = 1$ 的推导。这一命题的形式化，是公式 $\neg Pr(x,\ulcorner 0 = 1\urcorner)$，其中变元 $x$ 自由出现。如果 $T$ 的一致性有一个有穷证明，其形式化将在 $T$ 中给出 $\neg Pr_T (x,\ulcorner 0 = 1\urcorner),$ 的一个推导，由此可在 $T$ 中通过对 $x$ 作简单的全称概括推出 $Con_T$。然而，$T$ 中 $Con_T$ 的推导被 G2 排除。

如前所述，哥德尔与贝尔奈斯起初认为，$\text{PA}$ 一致性证明的困难可以通过采用那些虽不能在 $\text{PA}$ 中形式化、却仍属有穷的方法来克服。这类方法按有穷主义的原初观念是否算作有穷，抑或构成对原有有穷主义观点的扩展，仍有争论。所考虑的新方法，包括希尔伯特（1931b; 1931a）提出的一种有穷版本的 $\omega$-规则。然而平心而论，大约自 1934 年之后，人们几乎普遍接受：哥德尔结果之前被接受为有穷的证明方法，全部可在 $\text{PA}$ 中形式化。对原有有穷主义立场的扩展已被提出，并以广义上有穷的理由得到辩护：例如 Gentzen（1936）在其 $\text{PA}$ 一致性证明中，把直到 $\varepsilon_0$ 的超限归纳称为“不可争辩的”；Takeuti（1987）给出另一种辩护。哥德尔（1958）提出了有穷主义立场的另一种扩展；上面提到的 Kreisel 的工作，也可看作另一次尝试——在保留希尔伯特原初观念精神的同时扩展有穷主义。

Detlefsen（1986; 2001; 1979）提出了绕过哥德尔第二定理对希尔伯特纲领之冲击的另一种尝试，并给出几条辩护路线。其中一条与刚才所述类似：论证某一版本的 $\omega$-规则有穷可接受，尽管无法形式化（然而见 Ignjatovic 1994）[^ignjatovic-1994]。Detlefsen 反对哥德尔第二定理通行解释的另一个论证，集中于形式化概念。哥德尔公式 $Con_T$ 这一“$T$ 一致”的特定形式化不可证明，并不蕴涵不存在其他公式——它们**在 $T$ 中可证**，且同样有资格被称为“$T$ 一致性的形式化”。这些公式依赖与标准形式化不同的可证明性谓词 $Pr_T$ 形式化。已知只要可证明性谓词服从某些一般可推导性条件，形式化的一致性陈述便不可证明。Detlefsen 论证说，这些条件并非一个谓词成为真正可证明性谓词的必要条件；确实存在违反可证明性条件的可证明性谓词，其产生的一致性公式 **在相应理论中可证**。然而，这些依赖非标准的可证明性概念，希尔伯特很可能不会接受（另见 Resnik 1974、Auerbach 1992 与 Steiner 1991）[^auerbach-1992][^resnik-1974][^steiner-1991]。

Smorynski（1977）论证说，单是第一个不完全性定理就已击败希尔伯特纲领。希尔伯特的目标不只是表明形式化数学一致，而且要以特定方式做到：表明理想数学绝不会导致与实在数学不符的结论。因此，理想数学若要成功，就必须对实在部分 **保守**——每当形式化的理想数学证明了一个实在公式 $P$，$P$ 本身（或其所表达的有穷命题）就必须有穷可证。在 Smorynski 看来，实在公式不仅包括数值等式及其组合，也包括带自由变元但无无界量词的一般公式。

现在，哥德尔第一个不完全性定理（G1）说：对任何足够强、一致的形式理论 $S$，都有句子 $G_S$ 为真但在 $S$ 中不可推导。按 Smorynski 的定义，$G_S$ 是一个实在句子。现在考虑一个形式化理想数学的理论 $T$，及其形式化实在数学的子理论 $S$。$S$ 满足 G1 的条件，因此 $S$ 不推导 $G_S$。然而，$T$ 作为全部数学（包括看出 $G_S$ 为真所需的部分）的形式化，确实推导 $G_S$。于是就有了一个实在陈述：它在理想数学中可证明，在实在数学中却不可证明。

Detlefsen（1986, Appendix；另见 1990）也针对这一论证为希尔伯特纲领作了辩护。他论证说，“希尔伯特式”工具主义通过否认理想数学必须对实在部分保守，绕开了来自 G1 的论证；所要求的只是实在可靠性（real-soundness）。希尔伯特式工具主义只要求理想理论不证明任何与实在理论相冲突的东西，并不要求它 **只** 证明实在理论也证明的实在陈述。

Franks（2009）对希尔伯特的事业作了相关的辩护与重新评价；McCarthy（2016）就哥德尔本人关于一致性与 G2 可证明性的问题给出另一种进路。Kripke（即出）表明，希尔伯特本人处理一致性证明的方式如何自然导向哥德尔式不完全性。Santos 等（即出）在 Artemov（2020）工作的基础上扩展，论证一种“部分有穷主义”容许与 G2 相容的一致性证明，且与希尔伯特本人后哥德尔时期的观点一致。相关提议另见 Schirn 与 Niebergall（2001）以及 Schirn（2019）。Zach（2004）就希尔伯特纲领中保守性与一致性问题的历史细节作了梳理。关于哥德尔定理与一致性证明的进一步讨论，见“哥德尔”与“哥德尔不完备定理”词条，以及 Cheng（2021）。

## 5 修正的希尔伯特纲领

即使不能给出算术的有穷一致性证明，寻找一致性证明的问题仍有价值。这类证明所用的方法尽管必须超出希尔伯特原初意义上的有穷主义，却可能为算术及更强理论的构造性内容提供真正的洞见。哥德尔的结果表明：不可能有对全部数学的绝对一致性证明。因此，哥德尔之后的证明论工作集中于相对结果——既相对于给出一致性证明的那个系统，也相对于所使用的证明方法。

在这种意义上的还原论证明论遵循两个传统。第一个主要由追随 Gentzen 与 Schütte 的证明论者开展，追求所谓 **序数分析** 的纲领，其范例是 Gentzen 对 $\text{PA}$ 的第一次一致性证明——通过直到 $\varepsilon_0 . \varepsilon_0$。它是某个超限（但可数）序数；然而，“直到 $\varepsilon_0$ 的归纳”在这里并不构成真正的超限程序。序数分析不使用无穷序数，而使用 **序数记号系统**，后者本身可在很弱（本质上有穷的）系统中形式化。系统 $T$ 的序数分析在下列条件满足时给出：（a）能构造一个序数记号系统，模拟某个序数 $\alpha_T$ 以下的序数，使得（b）可以有穷地证明：直到 $\alpha_T$ 的归纳原则的形式化 $TI(\alpha_T)$ 蕴涵 $T$ 的一致性（即 $S \vdash TI(\alpha_T)\rightarrow Con_T$）；并且（c）$T$ 对所有 $\beta \lt \alpha_T$ 证明 $TI(\beta)$（$S$ 是形式化有穷元数学的理论，一般是 $T$ 的弱子理论）。要具有任何基础意义，还要求能为直到 $\alpha_T$ 的超限归纳给出构造性论证。如前所述，Gentzen 与 Takeuti 对 $\varepsilon_0$——$\text{PA}$ 的证明论序数——做到了这一点；但对更强的理论，这变得更困难，哲学意义也逐步可疑。关于 Gentzen 一致性证明的综述，见“证明论”词条；可读的教科书表述见 Mancosu 等 2021；关于 Takeuti 的良序证明，见 Thomas-Bolduc and Darnell 2022。

Kreisel（1983; 1968）与 Feferman（Feferman, 1988; Feferman, 1993a）提出了一种在哲学上更令人满意的、以证明论措辞延续希尔伯特纲领的方式。这项工作从一种更宽的希尔伯特纲领观念出发：纲领旨在以受限手段为理想数学提供辩护。按这一观念，希尔伯特证明论的目标是表明：至少就某一类实在命题而言，理想数学不超出实在数学。希尔伯特所设想的那种有穷一致性证明本可做到这一点：理想数学若证明了一个实在命题，该命题便已可由实在（即有穷）方法证明。在某种意义上，这把理想数学还原为实在数学。理论 $T$ 到理论 $S$ 的 **证明论还原** 表明：就某一类命题而言，如果 $T$ 证明了一个命题，那么 $S$ 也证明它；而这一事实的证明本身是有穷的。于是，希尔伯特的证明论纲领可看作寻找从全部数学到有穷数学的证明论还原；相对化纲领寻找的则是另一种还原：从弱于全部经典数学的理论，还原到往往强于有穷数学的理论。证明论者已获得若干这类结果，包括把表面看来需要大量理想数学才能辩护的理论（如分析学的子系统）还原为有穷系统。（Feferman, 1993b）把这类结果与另一些结果结合起来——后者表明大部分乃至全部科学上可应用的数学都能在具备此类还原的系统中开展——用以反驳数学哲学中的不可或缺性论证。这类证明论还原的哲学意义，目前仍是争论的主题（Hofweber, 2000; Feferman, 2000）。

所谓反推数学的纲领——尤其由 Friedman 与 Simpson 发展——是希尔伯特纲领的另一延续。面对哥德尔结果表明并非全部经典数学都能还原为有穷数学，他们寻求回答：经典数学中有多少可以这样还原？反推数学研究哪些经典数学定理可在可还原为有穷数学（按上一段所论意义）的分析学弱子系统中证明，力求给该问题一个精确回答。一个典型结果是：泛函分析中的哈恩—巴拿赫定理可在称为 $WKL_0$（“弱柯尼希引理”）的理论中证明；$WKL_0$ 在 $\text{PRA}$ 之上对 $\Pi^{0}_2$ 句子（即形如 $\forall x\exists yA(x, y)$ 的句子）保守。（综述见 Simpson 1988；技术处理见 Simpson 1999。）[^simpson-1988][^simpson-1999]

## References（引用注释）

**以下文献从原文照录，不作翻译；中国文献译为中文。**

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

[^an-2006]: An extended version of the first revision of this entry can be found in Zach (2006).
[^ackermann-1924]: Ackermann, Wilhelm, 1924, “Begründung des ‘tertium non datur’ mittels der Hilbertschen Theorie der Widerspruchsfreiheit,” *Mathematische Annalen*, 93: 1–36.
[^artemov-2020]: Artemov, Sergei, 2020, “The provability of consistency,” arXiv:1902.07404.
[^auerbach-1992]: Auerbach, David, 1992, “How to say things with formalisms,” in *Proof, Logic, and Formalization*, Michael Detlefsen, ed., London: Routledge, 77–93.
[^avigad-2003]: Avigad, Jeremy, 2003, “Number theory and elementary arithmetic,” *Philosophia Mathematica*, 11: 257–284.
[^bernays-1922]: Bernays, Paul, 1922, “Über Hilberts Gedanken zur Grundlegung der Arithmetik,” *Jahresbericht der Deutschen Mathematiker-Vereinigung*, 31: 10–19. English translation in Mancosu (1998a, 215–222).
[^bernays-1923]: –––, 1923, “Erwiderung auf die Note von Herrn Aloys Müller: Über Zahlen als Zeichen,” *Mathematische Annalen*, 90: 159–63. English translation in Mancosu (1998a, 223–226).
[^bernays-1928a]: –––, 1928a, “Über Nelsons Stellungnahme in der Philosophie der Mathematik,” *Die Naturwissenschaften*, 16: 142–45.
[^bernays-1928b]: –––, 1928b,, “Zusatz zu Hilberts Vortrag über ‘Die Grundlagen der Mathematik,’” *Abhandlungen aus dem Mathematischen Seminar der Universität Hamburg*, 6: 88–92. English translation in: van Heijenoort (1967, 485–489).
[^bernays-1930]: –––, 1930, “Die Philosophie der Mathematik und die Hilbertsche Beweistheorie,” *Blätter für deutsche Philosophie*, 4: 326–67. Reprinted in Bernays (1976, 17–61). English translation in Mancosu (1998a, 234–265).
[^bernays-1976]: –––, 1976, *Abhandlungen zur Philosophie der Mathematik*, Darmstadt: Wissenschaftliche Buchgesellschaft.
[^cheng-2021]: Cheng, Yong, 2021, “Current Research on Gödel’s Incompleteness Theorems,” *Bulletin of Symbolic Logic*, 27(2): 113–67.
[^dean-2015]: Dean, Walter, 2015, “Arithmetical reflection and the provability of soundness,” *Philosophia Mathematica*, 23: 31–64, doi:10.1093/philmat/nku026
[^detlefsen-1979]: Detlefsen, Michael, 1979, “On interpreting Gödel’s second theorem,” *Journal of Philosophical Logic*, 8: 297–313. Reprinted with a postscript in Shanker (1988, 131–154).
[^detlefsen-1986]: –––, 1986, *Hilbert’s Program*, Dordrecht: Reidel.
[^detlefsen-1990]: –––, 1990, “On an alleged refutation of Hilbert’s program using Gödel’s first incompleteness theorem,” *Journal of Philosophical Logic*, 19: 343–377.
[^detlefsen-2001]: –––, 2001, “What does Gödel’s second theorem say?,” *Philosophia Mathematica*, 9: 37–71.
[^eder-nd]: Eder, Günther, forthcoming, “The Bernays-Müller debate,” *HOPOS: The Journal of the International Society for the History of Philosophy of Science*.
[^ewald-1996]: Ewald, William Bragg (ed.), 1996, *From Kant to Hilbert. A Source Book in the Foundations of Mathematics*, vol. 2, Oxford: Oxford University Press.
[^ewald-2013]: Ewald, William Bragg and Wilfried Sieg (eds.), 2013, *David Hilbert’s Lectures on the Foundations of Arithmetic and Logic 1917–1933*, Berlin and Heidelberg: Springer.
[^feferman-1988]: Feferman, Solomon, 1988, “Hilbert’s Program relativized: Proof-theoretical and foundational reductions,” *Journal of Symbolic Logic*, 53(2): 364–284.
[^feferman-1993a]: –––, 1993a, “What rests on what? The proof-theoretic analysis of mathematics,” in *Philosophy of Mathematics. Proceedings of the Fifteenth International Wittgenstein-Symposium, Part 1*, Johannes Czermak, ed., Vienna: Hölder-Pichler-Tempsky, 147–171. Reprinted in Feferman (1998, Ch. 10, 187–208).
[^feferman-1993b]: –––, 1993b, “Why a little bit goes a long way: Logical foundations of scientifically applicable mathematics,” *PSA 1992*, 2: 442–455. Reprinted in Feferman (1998, Ch. 14, 284–298). [[Preprint available online](http://math.stanford.edu/~feferman/papers/psa1992.pdf)].
[^feferman-1998]: –––, 1998, *In the Light of Logic*, Oxford: Oxford University Press.
[^feferman-2000]: –––, 2000, “Does reductive proof theory have a viable rationale?.” *Erkenntnis*, 53: 63–96.
[^franks-2009]: Franks, Curtis, 2009, *The Autonomy of Mathematical Knowledge: Hilbert’s Program Revisited*, Cambridge: Cambridge University Press.
[^ganea-2010]: Ganea, Mihai, 2010, “Two (or three) notions of finitism,” *Review of Symbolic Logic*, 3: 119–144.
[^gentzen-1936]: Gentzen, Gerhard, 1936,, “Die Widerspruchsfreiheit der reinen Zahlentheorie,” *Mathematische Annalen*, 112: 493–565. English translation in Gentzen (1969, 132–213).
[^gentzen-1969]: –––, 1969, *The Collected Papers of Gerhard Gentzen*, Amsterdam: North-Holland.
[^giaquinto-1983]: Giaquinto, Marcus, 1983, “Hilbert’s philosophy of mathematics,” *British Journal for Philosophy of Science*, 34: 119–132.
[^gödel-1931]: Gödel, Kurt, 1931, “Über formal unentscheidbare Sätze der *Principia Mathematica* und verwandter Systeme I,” *Monatshefte für Mathematik und Physik*, 38: 173–198. Reprinted and translated in Gödel (1986, 144–195).
[^gödel-1958]: –––, 1958, “Über eine bisher noch nicht benütze Erweiterung des finiten standpunktes,” *Dialectica*, 280–287. Reprinted and translated in Gödel (1990, 217–251).
[^gödel-1986]: –––, 1986, *Collected Works*, vol. 1, Oxford: Oxford University Press.
[^gödel-1990]: –––, 1990, *Collected Works*, vol. 2, Oxford: Oxford University Press.
[^gödel-2003]: –––, 2003, *Collected Works*, vol. 4, Oxford: Oxford University Press.
[^hallett-1990]: Hallett, Michael, 1990, “Physicalism, reductionism and Hilbert,” in *Physicalism in Mathematics*, Andrew D. Irvine, ed., Dordrecht: Reidel, 183–257.
[^hilbert-1899]: Hilbert, David, 1899, “Grundlagen der Geometrie,” in *Festschrift zur Feier der Enthüllung des Gauss-Weber-Denkmals in Göttingen*, Leipzig: Teubner, 1–92, 1st ed.
[^hilbert-1900a]: –––, 1900a, “Mathematische Probleme,” *Nachrichten von der Königlichen Gesellschaft der Wissenschaften zu Göttingen, Math.-Phys. Klasse*, 253–297. Lecture given at the International Congress of Mathematicians, Paris, 1900. Partial English translation in Ewald (1996, 1096–1105).
[^hilbert-1900b]: –––, 1900b, “Über den Zahlbegriff,” *Jahresbericht der Deutschen Mathematiker-Vereinigung*, 8: 180-184. English translation in Ewald (1996, 1089–1096).
[^hilbert-1905]: –––, 1905, “Über die Grundlagen der Logik und der Arithmetik,” in *Verhandlungen des dritten Internationalen Mathematiker-Kongresses in Heidelberg vom 8. bis 13. August 1904*, A. Krazer, ed., Leipzig: Teubner, 174–85. English translation in van Heijenoort (1967, 129–138).
[^hilbert-1918a]: –––, 1918a, “Axiomatisches Denken,” *Mathematische Annalen*, 78: 405–15. Lecture given at the Swiss Society of Mathematicians, 11 September 1917. Reprinted in Hilbert (1935, 146–156). English translation in Ewald (1996, 1105–1115).
[^hilbert-1918b]: –––, 1918b, “Prinzipien der Mathematik,” Lecture notes by Paul Bernays. Winter-Semester 1917/18. Typescript. Bibliothek, Mathematisches Institut, Universität Göttingen. Edited in Ewald and Sieg (2013, 59–221)..
[^hilbert-1922a]: –––, 1922a, “Grundlagen der Mathematik,” Vorlesung, Winter-Semester 1921/22. Lecture notes by Paul Bernays. Typescript. Bibliothek, Mathematisches Institut, Universität Göttingen. Edited in Ewald and Sieg (2013, 431–527).
[^hilbert-1922b]: –––, 1922b, “Neubegründung der Mathematik: Erste Mitteilung,” *Abhandlungen aus dem Seminar der Hamburgischen Universität*, 1: 157–177. Series of talks given at the University of Hamburg, July 25–27, 1921. Reprinted with notes by Bernays in Hilbert (1935, 157–177). English translation in Mancosu (1998a, 198–214) and Ewald (1996, 1115–1134).
[^hilbert-1923]: –––, 1923, “Die logischen Grundlagen der Mathematik,” *Mathematische Annalen*, 88: 151–165. Lecture given at the Deutsche Naturforscher-Gesellschaft, September 1922. Reprinted in Hilbert (1935, 178–191). English translation in Ewald (1996, 1134–1148).
[^hilbert-1926]: –––, 1926, “Über das Unendliche,” *Mathematische Annalen*, 95: 161–190. Lecture given Münster, 4 June 1925. English translation in van Heijenoort (1967, 367–392).
[^hilbert-1928]: –––, 1928, “Die Grundlagen der Mathematik,” *Abhandlungen aus dem Seminar der Hamburgischen Universität*, 6: 65–85. Reprinted in Ewald and Sieg (2013, 917–942). English translation in van Heijenoort (1967, 464–479).
[^hilbert-1929]: –––, 1929, “Probleme der Grundlegung der Mathematik,” *Mathematische Annalen*, 102: 1–9. Lecture given at the International Congress of Mathematicians, 3 September 1928. Reprinted in Ewald and Sieg (2013, 954–966). English translation in Mancosu (1998a, 227–233).
[^hilbert-1931a]: –––, 1931a, “Beweis des Tertium non datur,” *Nachrichten der Gesellschaft der Wissenschaften zu Göttingen. Math.-phys. Klasse*, 120-125. Reprinted in Ewald and Sieg (2013, 967–982).
[^hilbert-1931b]: –––, 1931b, “Die Grundlegung der elementaren Zahlenlehre,” *Mathematische Annalen*, 104: 485–494. Reprinted in Hilbert (1935, 192–195) and Ewald and Sieg (2013, 983–990). English translation in Ewald (1996, 1148–1157).
[^hilbert-1935]: –––, 1935, *Gesammelte Abhandlungen*, vol. 3, Berlin: Springer.
[^hilbert-1992]: –––, 1992, *Natur und mathematisches Erkennen*, Basel: Birkhäuser. Vorlesungen, 1919–20.
[^hilbert-1928-2]: Hilbert, David and Ackermann, Wilhelm, 1928, *Grundzüge der theoretischen Logik*, Berlin: Springer.
[^hilbert-1923-2]: Hilbert, David and Bernays, Paul, 1923, “Logische Grundlagen der Mathematik,” Vorlesung, Winter-Semester 1922-23. Lecture notes by Paul Bernays, with handwritten notes by Hilbert. Hilbert-Nachlaß, Niedersächsische Staats- und Universitätsbibliothek, Cod. Ms. Hilbert 567.
[^hilbert-1934]: –––, 1934, *Grundlagen der Mathematik*, vol. 1, Berlin: Springer.
[^hilbert-1939]: –––, 1939, *Grundlagen der Mathematik*, vol. 2, Berlin: Springer.
[^hofweber-2000]: Hofweber, Thomas, 2000, “Proof-theoretic reduction as a philosopher’s tool,” *Erkenntnis*, 53: 127–146.
[^ignjatovic-1994]: Ignjatovic, Aleksandar, 1994, “Hilbert’s program and the omega rule,” *Journal of Symbolic Logic*, 59: 322–343.
[^incurvati-2019]: Incurvati, Luca, 2019, “On the concept of finitism,” *Synthese*, 192: 2413–2436.
[^kish-bar-on-2021]: Kish-Bar-On, Kati, 2021, “Towards a New Philosophical Perspective on Hermann Weyl’s Turn to Intuitionism,” *Science in Context*, 34: 51–68.
[^kitcher-1976]: Kitcher, Philip, 1976, “Hilbert’s epistemology,” *Philosophy of Science*, 43: 99–115.
[^kreisel-1960]: Kreisel, Georg, 1960, “Ordinal logics and the characterization of informal notions of proof,” in *Proceedings of the International Congress of Mathematicians. Edinburgh, 14–21 August 1958*, J. A. Todd, ed., Cambridge: Cambridge University Press, 289–299.
[^kreisel-1968]: –––, 1968, “A survey of proof theory,” *Journal of Symbolic Logic*, 33: 321–388.
[^kreisel-1970]: –––, 1970, “Principles of proof and ordinals implicit in given concepts,” in *Intuitionism and Proof Theory*, A. Kino, J. Myhill, and R. E. Veseley, eds., Amsterdam: North-Holland.
[^kreisel-1983]: –––, 1983, “Hilbert’s programme,” in *Philosophy of Mathematics*, Paul Benacerraf and Hilary Putnam, eds., Cambridge: Cambridge University Press, 207–238, 2nd ed.
[^kripke-nd]: Kripke, Saul A., forthcoming, “The Collapse of the Hilbert Program: A Variation on the Gödelian Theme,” *Bulletin of Symbolic Logic*.
[^mancosu-1998a]: Mancosu, Paolo (ed.), 1998a, *From Brouwer to Hilbert. The Debate on the Foundations of Mathematics in the 1920s*, Oxford: Oxford University Press.
[^mancosu-1998b]: Mancosu, Paolo, 1998b, “Hilbert and Bernays on Metamathematics,” in (Mancosu, 1998a), 149–188. Reprinted in Mancosu (2010).
[^mancosu-1999]: –––, 1999, “Between Russell and Hilbert: Behmann on the foundations of mathematics,” *Bulletin of Symbolic Logic*, 5(3): 303–330. Reprinted in Mancosu (2010).
[^mancosu-2010]: –––, 2010, *The Adventure of Reason: Interplay Between Philosophy of Mathematics and Mathematical Logic, 1900–1940*, Oxford: Oxford University Press.
[^mancosu-2021]: Mancosu, Paolo, Sergio Galvan, and Richard Zach, 2021, *An Introduction to Proof Theory: Normalization, Cut-Elimination, and Consistency Proofs*. Oxford: Oxford University Press.
[^mancosu-2002]: Mancosu, Paolo and Ryckman, Thomas, 2002, “Mathematics and phenomenology: The correspondence between O. Becker and H. Weyl,” *Philosophia Mathematica*, 10: 130–202. Reprinted in Mancosu (2010).
[^mccarthy-2016]: McCarthy, T., 2016, “Gödel’s third incompleteness theorem,” *Dialectica* 70: 87–112.
[^parsons-1998]: Parsons, Charles, 1998, “Finitism and intuitive knowledge,” in *The Philosophy of Mathematics Today*, Matthias Schirn, ed., Oxford: Oxford University Press, 249–270.
[^parsons-2007]: –––, 2007, *Mathematical Thought and its Objects*, Cambridge: Cambridge University Press.
[^patton-2014]: Patton, Lydia, 2014, “Hilbert’s objectivity,” *Historia Mathematica*, 41(2): 188–203.
[^peckhaus-1990]: Peckhaus, Volker, 1990, *Hilbertprogramm und Kritische Philosophie*, Göttingen: Vandenhoeck und Ruprecht.
[^poincaré-1906]: Poincaré, Henri, 1906, “Les mathématiques et la logique,” *Revue de métaphysique et de morale*, 14: 294–317. English translation in Ewald (1996, 1038–1052).
[^resnik-1974]: Resnik, Michael D., 1974, “On the philosophical significance of consistency proofs,” *Journal of Philosophical Logic*, 3: 133–47.
[^resnik-1980]: –––, 1980, *Frege and the Philosophy of Mathematics*, Ithaca: Cornell University Press.
[^santos-nd]: Santos, Paulo Guilherme, Wilfried Sieg, and Reinhard Kahle, forthcoming, “A New Perspective on Completeness and Finitist Consistency,” *Journal of Logic and Computation*.
[^schirn-2019]: Schirn, Matthias, 2019, “The finite and the infinite: On Hilbert’s formalist approach before and after Gödel’s incompleteness theorems,” *Logique et Analyse*, 245: 1–34.
[^schirn-2001]: Schirn, Matthias, and Karl-Georg Niebergall, 2001, “Extensions of the finitist point of view,” *History and Philosophy of Logic*, 22(3): 135–61.
[^shanker-1988]: Shanker, Stuart G., 1988, *Gödel’s Theorem in Focus*, London: Routledge.
[^sieg-1990]: Sieg, Wilfried, 1990, “Reflections on Hilbert’s program,” in *Acting and Reflecting*, Wilfried Sieg, ed., Dordrecht: Kluwer, 171–82. Reprinted in Sieg (2013).
[^sieg-1999]: –––, 1999, “Hilbert’s programs: 1917–1922,” *Bulletin of Symbolic Logic*, 5(1): 1–44. Reprinted in Sieg (2013).
[^sieg-2013]: –––, 2013, *Hilbert’s Programs and Beyond*, New York: Oxford University Press.
[^simpson-1988]: Simpson, Stephen G., 1988, “Partial realizations of Hilbert’s program,” *Journal of Symbolic Logic*, 53(2): 349–363.
[^simpson-1999]: –––, 1999, *Subsystems of Second Order Arithmetic*, Berlin: Springer.
[^smorynski-1977]: Smorynski, Craig, 1977, “The incompleteness theorems,” in *Handbook of Mathematical Logic*, Jon Barwise, ed., Amsterdam: North-Holland, 821–865.
[^steiner-1975]: Steiner, Mark, 1975, *Mathematical Knowledge*, Ithaca: Cornell University Press.
[^steiner-1991]: –––, 1991, “Review of *Hilbert’s Program: An Essay on Mathematical Instrumentalism* (Detlefsen, 1986),” *Journal of Philosophy*, 88(6): 331–336.
[^tait-1981]: Tait, W. W., 1981, “Finitism,” *Journal of Philosophy*, 78: 524–546. Reprinted in Tait (2005a, 21–42).
[^tait-2002]: –––, 2002, “Remarks on finitism,” in *Reflections on the Foundations of Mathematics. Essays in Honor of Solomon Feferman*, Wilfried Sieg, Richard Sommer, and Carolyn Talcott, eds., Association for Symbolic Logic, LNL 15. Reprinted in Tait (2005a, 43–53). [[Preprint available online](https://www.researchgate.net/publication/2391294_Remarks_On_Finitism)]
[^tait-2005a]: –––, 2005a, *The Provenance of Pure Reason: Essays in the Philosophy of Mathematics and its History*, New York: Oxford University Press.
[^tait-2005b]: –––, 2005b, “Appendix to Chapters 1 and 2,” in Tait (2005a, 54–60).
[^tait-2019]: –––, 2019, “What Hilbert and Bernays meant by ‘finitism,’” in *Philosophy of Logic and Mathematics: Proceedings of the 41st International Ludwig Wittgenstein Symposium*, Gabriele M. Mras, Paul Weingartner, and Bernhard Ritter (eds.), Berlin: De Gruyter, 249–62.
[^takeuti-1987]: Takeuti, Gaisi, 1987, *Proof Theory* (Studies in Logic: 81), Amsterdam: North-Holland, 2nd edition.
[^thomas-bolduc-2022]: Thomas-Bolduc, Aaron, and Eamon Darnell, 2022, “Takeuti’s well-ordering proof: An accessible recontruction,” *The Australasian Journal of Logic*, 19(1): 1–31.
[^heijenoort-1967]: van Heijenoort, Jean (ed.), 1967, *From Frege to Gödel. A Source Book in Mathematical Logic, 1897–1931*, Cambridge, Mass.: Harvard University Press.
[^neumann-1927]: von Neumann, Johann, 1927, “Zur Hilbertschen Beweistheorie,” *Mathematische Zeitschrift*, 26: 1–46.
[^weyl-1921]: Weyl, Hermann, 1921, “Über die neue Grundlagenkrise der Mathematik,” *Mathematische Zeitschrift*, 10: 37–79. Reprinted in Weyl (1968, 143–180). English translation in Mancosu (1998a, 86–118).
[^weyl-1925]: –––, 1925, “Die heutige Erkenntnislage in der Mathematik,” *Symposion*, 1: 1–23. Reprinted in: Weyl (1968, 511–42). English translation in: Mancosu (1998a, 123–42).
[^weyl-1928]: –––, 1928, “Diskussionsbemerkungen zu dem zweiten Hilbertschen Vortrag über die Grundlagen der Mathematik,” *Abhandlungen aus dem Mathematischen Seminar der Universität Hamburg*, 6: 86–88. English translation in van Heijenoort (1967, 480–484).
[^weyl-1968]: –––, 1968, *Gesammelte Abhandlungen*, vol. 1, Berlin: Springer Verlag.
[^zach-1999]: Zach, Richard, 1999, “Completeness before Post: Bernays, Hilbert, and the development of propositional logic,” *Bulletin of Symbolic Logic*, 5(3): 331–366.
[^zach-2003]: –––, 2003, “The practice of finitism. Epsilon calculus and consistency proofs in Hilbert’s Program,” *Synthese*, 137: 211–259.
[^zach-2004]: –––, 2004, “Hilbert’s ‘Verunglückter Beweis,’ the first epsilon theorem, and consistency proofs,” *History and Philosophy of Logic*, 25: 79–94.
[^zach-2006]: –––, 2006, “Hilbert’s program then and now,” in: Dale Jacquette, ed., *Philosophy of Logic.* Handbook of the Philosophy of Science, vol. 5. Amsterdam: Elsevier, 411–447.

## 学术工具

* [如何引用本词条](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=hilbert-program)。
* [预览本词条的 PDF 版本](https://leibniz.stanford.edu/friends/preview/hilbert-program/)，见 [SEP 学会之友](https://leibniz.stanford.edu/friends/)。
* 在 [InPhO](https://www.inphoproject.org/entity?sep=hilbert-program&redirect=True) 查找与本词条相关的话题与思想家。
* 在 [PhilPapers](https://philpapers.org/sep/hilbert-program/) 查看本词条的增强文献目录及其数据库链接。

## 其他网络资源

[请向作者提出建议。]

## 相关词条

勒伊岑·艾赫贝特斯·扬·布劳威尔 | ε 演算 | 弗雷格-希尔伯特争论 | 库尔特·哥德尔 | 哥德尔不完备定理 | 大卫·希尔伯特 | 数学哲学中的形式主义 | 数学哲学中的直觉主义 | 《数学原理》 | 证明论 | 证明论的发展 | 伯特兰·罗素

**（译注：相关词条的中文站内链接将由管线在对应词条重译完成后统一挂接。）**
