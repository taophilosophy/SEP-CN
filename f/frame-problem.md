# 框架问题 frame problem (Murray Shanahan)

**首次发表于 2004 年 2 月 23 日；2016 年 2 月 8 日实质修订。**

对大多数人工智能（AI）研究者而言，框架问题（frame problem）是这样一项挑战：如何在逻辑中表征行动的效果，而无须显式表征大量直觉上显而易见的非效果（non-effects）。但在许多哲学家看来，AI 研究者的框架问题牵涉到更广泛的认识论问题。原则上，我们究竟能否把为推出一个行动之后果所需要的推理限定在一定范围内？更一般地说，我们那种显然的能力——只依据与当下情境相关的东西便作出决定，而无须显式考虑一切不相关的东西——又当如何解释？

## 1 导言

框架问题最初是逻辑式人工智能（AI）中一个界定狭窄的技术问题，但它被心灵哲学家以一种加工改造过的形式接了过去，并获得更宽泛的解释。该问题既生于 AI 研究者的实验室，又被哲学家接手处理，两者之间的张力在 20 世纪 80 与 90 年代引发了一场有趣且时而激烈的争论。不过，由于狭窄的技术问题大体已获解决，晚近的讨论已较少纠缠于解释之争，而更多关注更宽泛的框架问题对认知科学的意涵。为把握这些问题，本文将首先考察技术面貌下的框架问题，继而检视哲学家重新诠释该问题的若干进路，最后评估框架问题在当今的意义。

## 2 逻辑中的框架问题

简言之，狭窄而技术性意义上的框架问题是这样的（McCarthy & Hayes 1969）[^mccarthy-1969]：运用数理逻辑，如何可能写出刻画行动效果的公式，而不必连带写出大量刻画这些行动之平凡而明显的非效果的公式？来看一个例子。这一困难无须动用完整的形式逻辑装置即可说明，但须谨记：魔鬼藏在数学细节里。假设我们写出两个公式，一个描述给物体上漆的效果，另一个描述移动物体的效果。

1. *Colour*(*x*, *c*) 在 *Paint*(*x*, *c*) 之后成立
2. *Position*(*x*, *p*) 在 *Move*(*x*, *p*) 之后成立

现在，假设有一个初始情境，其中 *Colour*(*A*, *Red*) 与 *Position*(*A*, *House*) 成立。按照演绎逻辑的机制，在行动 *Paint*(*A*, *Blue*) 之后施行行动 *Move*(*A*, *Garden*)，此时何者成立？凭直觉，我们预期 *Colour*(*A*, *Blue*) 与 *Position*(*A*, *Garden*) 成立。遗憾的是，事实并非如此。若借助情境演算（situation calculus）（McCarthy & Hayes 1969）[^mccarthy-1969] 之类合适的形式系统，用经典谓词逻辑把上述公式更形式化地写出，则由这两个公式只能得出 *Position*(*A*, *Garden*) 成立这一结论。原因在于，它们并未排除 *A* 的颜色被 *Move* 行动改变的可能性。

要扩充这类形式化、使正确的常识结论得以自动得出，最显白的办法是添加若干显式描述每个行动之非效果的公式。这类公式称作 **框架公理**（frame axioms）。就眼下的例子而言，我们需要一对框架公理。

1. 若 *Colour*(*x*, *c*) 事先成立，则 *Colour*(*x*, *c*) 在 *Move*(*x*, *p*) 之后成立
2. 若 *Position*(*x*, *p*) 事先成立，则 *Position*(*x*, *p*) 在 *Paint*(*x*, *c*) 之后成立

换言之，给物体上漆不会影响其位置，移动物体也不会影响其颜色。添入这两个公式（用谓词逻辑更形式化地写出）之后，所有想要的结论都能推出。然而，这远非令人满意的解决方案。由于 **大多数** 行动并不影响情境的 **大多数** 性质，在一个含 *M* 个行动与 *N* 个性质的论域中，我们一般不得不写出近乎 *MN* 条框架公理。无论这些公式注定要显式存储于计算机内存，抑或只是设计者规范的一部分，这都是一桩不受欢迎的负担。

于是，挑战在于：如何在形式逻辑中更简洁地刻画行动的非效果。看来我们需要的是某种方式，用以宣告如下一般经验法则：**除非** 有相反的证据，否则可以假定一个行动不会改变情境的某一给定性质。这一默认假定就是所谓的 **常识惯性定律**（common sense law of inertia）。（技术性的）框架问题可以看作形式化这条定律的任务。

这样做的主要障碍在于经典逻辑的 **单调性**（monotonicity）。在经典逻辑中，由一组公式可推出的结论集总是随公式的增添而 **扩大**。这就使得任何带有开放例外集的规则都无法得到表达，而常识惯性定律恰恰是这样一条规则。例如，日后我们或许想添入一个公式，刻画“把物体移进一桶油漆”这一情形对公理 3 构成的例外。但我们此前没有想到这个例外，这不应妨碍我们应用常识惯性定律、推出足够宽泛的（可废止的）结论以启动推理。

于是，基于逻辑的 AI 研究者投入大量精力，发展出各种 **非单调**（non-monotonic）推理形式系统——如 **限定理论**（circumscription）（McCarthy 1986）[^mccarthy-1986]——并考察它们在框架问题上的应用。然而这一切远非一帆风顺。前进路上最棘手的障碍之一，在所谓的 **耶鲁射击问题**（Yale shooting problem）（Hanks & McDermott 1987）[^hanks-1987][^mcdermott-1987]中暴露无遗：这个简单情境若用非单调形式系统天真地表征，便会引出反直观的结论。更麻烦的是，完整的解决方案还必须能应对并发行动、效果非确定的行动、连续变化以及具有间接衍生效应的行动。尽管有这些微妙之处，如今已有若干足以支撑基于逻辑之 AI 研究的技术性框架问题解决方案。改进与扩展固然仍在继续，但可以说尘埃已定：技术面貌下的框架问题已大体获得解决（Shanahan 1997; Lifschitz 2015）[^lifschitz-2015][^shanahan-1997]。

## 3 认识论的框架问题

现在转向经各路哲学家重新诠释的框架问题。哲学文献中第一次郑重提及框架问题，出自丹尼特（Dennett 1978, 125）。在丹尼特看来，谜题在于：“一个对世界持有诸多信念的认知生物”在执行行动时，如何更新这些信念，使之保持“大致忠于世界”？在《心智的模块性》（*The Modularity of Mind*）中，福多（Fodor）站到机器人设计者的立场上，怀着框架问题发问，所问大体相同：“机器的程序……如何判定机器人应当重新评估哪些信念——假定它已踏上这种或那种行动进程？”（Fodor 1983, 114）[^fodor-1983]。

初看之下，这一问题与令 AI 研究者绞尽脑汁的逻辑问题只有印象式的关联。与 AI 研究者的问题不同，哲学家的问题并非在形式逻辑的语境中提出，也不专门关乎行动的非效果。丹尼特在后来的一篇文章里承认挪用了 AI 研究者的术语（1987），但他随即重申自己的信念：借框架问题之机，AI 发现了“一个崭新的、深刻的认识论问题——原则上可以把握，却为历代哲学家所忽视”。

要理解这一问题，最好的办法是设想自己是一个机器人的设计者，这个机器人必须执行泡一杯茶之类的日常任务。此外，为让框架问题干净利落地凸显出来，必须把思想实验限定在一类特定的机器人设计上，即那些采用显式存储、类似句子的世界表征的设计——这正体现 **经典 AI**（classical AI）的方法论信条。以狭窄技术面貌攻克原初框架问题的 AI 研究者，正是在这一约束下工作的，因为基于逻辑的 AI 本是经典 AI 的一个变种。同情心智计算理论的哲学家——他们认为心理状态由若干命题态度组成，而心理过程是对这些命题的推理——同样倾向于认可这一规定。

现在，假设这个机器人要从橱柜里取出一只茶杯。杯子当下的位置作为一条句子记录在它的事实数据库中，与表征当下情境无数其他特征的句子并列——环境温度、手臂的构型、今天的日期、茶壶的颜色，等等。机器人握住杯子、把它从橱柜取出之后，需要更新这个数据库。杯子的位置显然变了，这是一条必须修订的事实。可还有哪些句子需要修改？环境温度未受影响，茶壶的位置未受影响。但倘若碰巧有一把勺子原本搁在杯里，那么勺子随容器而得的新位置也必须更新。

哲学家如今察觉到的认识论困难正在于此：机器人如何能限定范围，只重新考虑其行动所要求考虑的那些命题？对一个足够简单的机器人来说，这似乎算不上什么难题：它尽可以逐条检查自己的整个命题数据库，找出需要修改的条目。可是，设想这个机器人拥有近乎人类的智能，因而背负一个庞大的数据库，哪怕只是转动一下马达也得把数据库过一遍——这样的策略在计算上就开始显得难以施行了。

于是，AI 中一个相关议题被称作框架问题的 **计算方面**（computational aspect）（McDermott 1987）[^mcdermott-1987]：如何计算行动的后果，而不必让计算遍历该行动的非效果。多数符号 AI 程序处理框架问题计算方面的方案，是麦克德莫特（McDermott）所谓“睡狗”策略（sleeping dog strategy）的某种变体（McDermott 1987）[^mcdermott-1987]。其想法是：更新表征当下情境的数据结构以反映世界的变化时，并非其中每个部分都要检查；只需修改那些表征世界已变化侧面的部分，其余一概照旧（谨遵“莫惹睡狗”的格言）。在机器人与茶杯的例子里，落实睡狗策略就是让机器人更新它关于杯子位置与橱柜内容的信念，而不去操心某把可能、也未必在杯上或杯中的勺子——因为机器人的目标本来就不直接涉及任何勺子。

然而，哲学问题并没有被这个计算问题穷尽。悬而未决的哲学问题是：机器人凭什么能确定自己已成功修订了全部信念，使之与其行动的后果相符？唯有此时，它才有资格放心地应用“常识惯性定律”，假定世界的其余部分原封未动。福多发人深省地把这比作“哈姆雷特问题：何时停止思考”（Fodor 1987, 140）[^fodor-1987]，并称框架问题就是“工程师视角下的哈姆雷特问题”。照此理解，想避开框架问题，最显眼的办法是诉诸 **相关性**（relevance）概念。反驳者会说：在任一给定行动的语境中，只有情境的某些性质是相关的；于是，对行动后果的考量尽可以方便地限定在这些性质之上。

然而，诉诸相关性于事无补：困难现在变成——如何判定什么相关、什么不相关？而这取决于语境。再看从橱柜取出茶杯这一行动。若机器人的工作是泡茶，那么这一行动便于从茶壶向杯中注水便是相关的；但若机器人的任务是清洁橱柜，更相关的后果则是杯子原先垫托的表面随之显露。经典路数的 AI 研究者可以迎难而上，尝试指明哪些命题与哪些语境相关。但惠勒（Wheeler）（2005; 2008）等哲学家从德雷福斯（Dreyfus）（1992）得到启发，在此看出无穷倒退的威胁。诚如德雷福斯所言：“如果每个语境只能凭借被选为相关的特征来识别，而这些特征又要在更宽泛的语境中得到解释，AI 从业者就面临一场语境的倒退”（Dreyfus 1992, 289）[^dreyfus-1992]。

缓解无穷倒退威胁的一条出路，是诉诸这样一个事实：人类虽比今天的机器人聪明，却照样会犯错误（McDermott 1987）[^mcdermott-1987]。人们常常预见不到自己行动的每一个后果，**即便** 他们并不缺少推出这些后果所需的任何信息——任何象棋新手都能作证。福多断言：“框架问题极深；它深及对合理性的分析”（Fodor 1987）[^fodor-1987]。不过，合理性分析本可容纳计算资源的有限性——可用于推出相关结论的资源总是有限的（Simon 1957; Russell & Wefald 1991; Sperber & Wilson 1996）[^russell-1991][^simon-1957][^sperber-1996]。受限理性由于有时仓促断言而在逻辑上并不完备，但这也并不比人类思维更糟。然而，正如福多指出的，诉诸人类自身的局限，来为推理过程可及的信息种类划定一条启发式边界，这本身并未解决认识论的框架问题（Fodor 2000, Ch.2; Fodor 2008, Ch.4; see also Chow 2013）[^chow-2013][^fodor-2000][^fodor-2008]。因为它回避了边界如何划定的问题——也就是说，它没有回答原初的问题：如何指明什么与推理过程相关、什么不相关。

尽管如此，经典 AI 研究者若坚信语境倒退终会见底，仍可以选定自己的研究纲领——依据判定相关性的规则来构建系统，并从经典 AI 昔日的成功中汲取灵感。持异议的哲学家对此可能回应：AI 昔日的成功从来都局限于狭窄领域，或是下棋，或是在有限微型世界中的推理——在这些世界里，潜在相关命题的集合固定且预先已知。相形之下，人类智能应付的是一个开放的、不断变化的语境集合（Dreyfus 1992; Dreyfus 2008; Wheeler 2005; Wheeler 2008; Rietveld 2012）[^dreyfus-1992][^dreyfus-2008][^rietveld-2012][^wheeler-2005][^wheeler-2008]。不仅如此，经典 AI 研究者在整体论论证面前颇为脆弱。福多著作的一个关键主张是：圈定一个行动的后果时——正如科学中为理论寻求确认时——任何东西都可能相关（Fodor 1983, 105）[^fodor-1983]；当下情境中可能登场的性质并无 **先验**（a priori）界限。因此，在模块性论题中，福多借框架问题支持这样一个观点：心智的中央过程——那些参与固定信念的过程——是“信息上不封装的”（informationally unencapsulated），意即它们可以从任何来源汲取信息（Fodor 1983; Fodor 2000; Fodor 2008; Dreyfus 1991, 115–121; Dreyfus 1992, 258）[^dreyfus-1991][^dreyfus-1992][^fodor-1983][^fodor-2000][^fodor-2008]。在福多看来，这正是为这些过程给出计算说明的根本障碍。

人们很容易认为，福多的忧虑立足于一个谬误论证，其大意是：一个过程必须信息上封装，才可能在计算上可行。只需看看互联网搜索引擎的成效便可知道，凭着巧妙的索引技术，情况并非如此：向网络搜索引擎提交任意一对看似不相干的关键词（比如“香蕉”与“曼陀林”），不出一秒，它就能在数十亿之巨的网页数据库里找齐提及这两个关键词的每一个网页（如今无疑也包括本页）。但这并不是眼前的问题。重申要害：真正的问题是相关性。一个过程或许确实能把系统所知的一切——比如关于香蕉和曼陀林的一切——编成索引，但所谓的神秘之处在于：它究竟如何能首先弄清，芸芸万物之中偏偏是香蕉和曼陀林与它的推理任务相关？

总而言之，我们可以辨识出一个认识论的框架问题，并将其与计算上的对应问题区分开来。认识论的问题是：整体性的、开放的、语境敏感的相关性，如何可能被经典 AI 所用的那类命题式、类语言的表征所把握？与之对应的 **计算** 问题则是：既然相关性是整体性的、开放的、语境敏感的，一个推理过程如何能切实地把自己限定在恰好相关的东西之上？

## 4 常识惯性定律的形而上学

（Fodor 1987）[^fodor-1987]揭示了框架问题的又一个维度：常识惯性定律的形而上学辩护在那里受到了挑战。福多本人虽未把这一问题与更宽泛框架问题的其他方面清楚区分开来，但细察之下，它显出是一个独立的哲学难题。论证如下。如上所述，AI 研究者发展出的逻辑框架问题解决方案，典型地诉诸某种版本的常识惯性定律：情境的性质被默认为不因行动而改变。这一假定据说恰恰由最初引发逻辑框架问题的那个观察所证成——大多数东西在行动施行或事件发生时并不改变。

在福多看来，这一形而上学辩护站不住脚。首先，有些行动会改变很多很多东西。断言“给物体上漆对房内大多数物体的大多数性质几乎没有影响”的人，多半会承认引爆一枚炸弹确实影响其中大多数性质。可当我们追问“大多数性质”意所何指时，更深的困难就出现了：要让这些关于“大多数性质”的论断得以成立，我们的本体论里该收进哪些谓词？为把要点磨得更尖，福多引入了“冰箱子”（*fridgeon*）概念：任一粒子在给定时刻是 **冰箱子**，当且仅当福多的冰箱在那个时刻开着。如此说来，开关福多的冰箱这一简单动作，似乎就带来了天文数字的附带变化。在一个可能包含冰箱子的宇宙里，大多数行动果真能让大多数东西保持不变吗？

这里的要点不在逻辑。开关福多的冰箱对冰箱子的影响，尽可以毫无困难地简洁表征出来（Shanahan 1997, 25）[^shanahan-1997]。要点是形而上学的：常识惯性定律唯有在恰当的本体论——对对象与谓词的恰当选择——之下才谈得上证成。可是，什么样的本体论才能让常识惯性定律奏效？冰箱子之类显然要排除在外，那么支撑这一决断的又是哪条形而上学原则？

这些问题以及引出它们的论证，令人强烈联想到古德曼（Goodman）对归纳的讨论（Goodman 1954）[^goodman-1954]。古德曼的“新归纳之谜”，通称 *grue* 悖论（grue paradox），让我们考虑谓词 *grue*：它在时间 *t* 之前恰好对绿色对象为真，在时间 *t* 之后只对蓝色对象为真。谜题在于：在时间 *t* 之前受检的每一颗绿祖母绿，同样是一颗 grue 祖母绿的实例。于是，“所有祖母绿皆 grue”这一归纳推理，看起来并不比“所有祖母绿皆绿”更不合法。症结当然在谓词的选择。古德曼证明归纳推理唯有在恰当的谓词集合之下才行得通；福多则就常识惯性定律论证了几乎同一点。

费策尔（Fetzer）（1991）则提出了框架问题与归纳问题之间另一种密切关联。他写道：“归纳问题［是］为某些关于未来的推理而非另一些推理辩护的问题；框架问题同样是为某些关于未来的推理而非另一些推理辩护的问题；第二个问题是第一个问题的一个实例。”不过，这种框架问题观极有争议（Hayes 1991）[^hayes-1991]。

## 5 今天的框架问题

狭窄而技术性的框架问题，在 20 世纪 80 年代末到 90 年代初的基于逻辑的人工智能中催生了大量研究；其更宽泛的哲学意涵也大约在同一时期浮出水面。而在今天，各思想家赋予框架问题的重要性，往往取决于他们在其他问题上的立场。

在经典 AI 内部，逻辑框架问题的多种可行方案已相继发展出来；即便对严格遵循逻辑范式的研究者而言，它也不再被视为严重障碍（Shanahan 1997; Reiter 2001; Shanahan 2003; Lifschitz 2015）[^lifschitz-2015][^reiter-2001][^shanahan-1997][^shanahan-2003]。值得注意的是，倾向逻辑的 AI 研究者尽可以前后一贯地保留其方法论，同时——只要把自己的产品仅仅当作工程来看待——拒斥传统认知科学家“计算作用于表征对理解心灵至关重要”的信念。再者，经典 AI 的目标既然不是造出具有人类水平智能的计算机，而只是设计更好、更有用的计算机程序，它便对福多、德雷福斯之流的哲学反驳免疫。不过有一点意味深长：对全然置身符号表征范式之外的 AI 研究者——例如从事情境机器人学（situated robotics）的人——来说，逻辑框架问题压根不出现在其日常研究之中。

尽管可以论证框架问题甚至在联结主义环境中也会出现（Haselager & Van Rappard 1998; Samuels 2010）[^haselager-1998][^samuels-2010]，它的哲学分量大半承自经典假设——计算作用于表征具有解释价值——而这一假设已遭受相当长时间的猛烈抨击（Clark 1997; Wheeler 2005）[^clark-1997][^wheeler-2005]。尽管如此，许多心灵哲学家——福多与普利什恩（Pylyshyn）亦在其列——依然主张：人类心理过程主要由对一组命题的推理构成，而这些推理由某种形式的计算来执行。在这样的哲学家看来，认识论的框架问题及其计算对应物仍是实实在在的威胁。

在惠勒（Wheeler）等人看来，经典 AI 与认知科学立足的笛卡尔式假定必须先被推翻、代之以更海德格尔式的立场，框架问题才可能被克服（Dreyfus 2008; Wheeler 2005; 2008; Rietveld 2012）[^dreyfus-2008][^rietveld-2012][^wheeler-2005]。在惠勒（2005; 2008）看来，发端于布鲁克斯（Brooks）（1991）工作的 AI 情境机器人学运动正是正确道路的典范。德雷福斯部分同意，但坚称情境机器人学的早期产品“绕开了框架问题而非解决它”，因为“布鲁克斯的机器人只对环境中固定而可孤立的特征作出反应，对语境或变化着的意义则无动于衷”（Dreyfus 2008, 335）[^dreyfus-2008]。德雷福斯认为弗里曼（Freeman）（2000）的神经动力学工作才是更牢靠的基础，可供那种有望消解框架问题的海德格尔式 AI 进路立足（see also Shanahan 2010, Ch.5; Rietveld 2012; Bruineberg & Rietveld 2014）[^bruineberg-2014][^rietveld-2012][^shanahan-2010]。弗里曼的进路令德雷福斯印象深刻：意义的神经动力学记录既非表征亦非联想，而是（用动力系统的术语说）一个给可能反应分类的“吸引子（attractor）库”——“吸引子本身是过去经验的产物”（Dreyfus 2008, 354）[^dreyfus-2008]。

框架问题的一项哲学遗产，是它把注意力引向与整体论相关的一簇问题，即所谓信息非封装（informational unencapsulation）。回顾一下：倘若对“什么信息与一个过程相关”没有 **先验** 界限，该过程就是信息上不封装的（福多有时称之“各向同性的”，isotropic）。在晚近著作中，福多把“框架问题”一词用于一切信息上不封装的过程，而不限于推断变化之后果的那些过程（Fodor 2000, Ch.2; Fodor 2006, Ch.4）[^fodor-2000]。显然，理想化的合理性在此意义上是信息上不封装的。也有人提出，各向同性会损害民俗心理学的所谓“理论论”（theory theory）（Heal 1996）[^heal-1996]。（在希尔（Heal）看来，这为与之竞争的模拟论（simulation theory）提供了支持；但威尔克森（Wilkerson）（2001）论证，信息非封装对民俗心理学的这两种说明都是麻烦。）如福多所言，类比推理是“最纯粹形式的各向同性：一个恰恰依赖于在先前被假定不相关的认知域之间传递信息的过程”（Fodor 1983, 105）[^fodor-1983]。可以说，类比与隐喻思维的能力——创造性地跨越不同理解域之边界的天赋——正是人类认知威力之源（Lakoff & Johnson 1980; Mithen 1996）[^lakoff-1980]。因此，类比推理的信息非封装潜在地相当棘手；对那些把模块视作（语境不敏感的）专门家的模块化心智理论来说，尤为如此（Carruthers 2003; 2006）[^carruthers-2003]。

德雷福斯声称，这个“框架问题的极端版本”与其要求较低的诸亲缘问题一样，都是经典 AI 与认知科学之笛卡尔式假定的产物（Dreyfus 2008, 361）[^dreyfus-2008]。他主张，一种恰切的海德格尔式心灵说明，同样是在此处消解框架问题的基础；而且在这类情形中，我们“对世界中事物如何行事的背景熟悉”已足以让我们“退后一步，弄清何者相关、如何相关”。不过，考虑到相关性的整体性、开放性与语境敏感性，德雷福斯并未说明这种“弄清”是如何达成的。惠勒则从类似的海德格尔式立场主张，处理他所谓的“跨语境”框架问题，出路在于一种动力系统，其中“每一系统组分的因果贡献既部分地决定、又部分地取决于大量其他系统组分的因果贡献”（Wheeler 2008, 341）[^wheeler-2008]。沙纳汉（Shanahan）与巴尔斯（Baars）（2005; see also Shanahan 2010, Ch.6）[^shanahan-2010]基于全局工作空间理论（global workspace theory）（Baars 1988）[^baars-1988]提出了一个相关方案：大脑解决信息非封装问题的方式，是落实这样一种架构——a) 判定相关性的职责并不集中，而是分布于并行的专门过程之中；b) 一个逐步展开的全局工作空间状态整合来自多个领域的相关贡献。

## 参考文献

**以下文献从原文照录，不作翻译；中国文献条目（古今）一律译为中文。**

[^baars-1988]: Baars, B. (1988), *A Cognitive Theory of Consciousness*, Cambridge University Press.

[^brooks-1991]: Brooks, R.A. (1991), “Intelligence without Reason”, in *Proc. 12th International Conference on Artificial Intelligence*, pp. 569–595.

[^bruineberg-2014]: Bruineberg, J. & Rietveld, E. (2014), “Self-organization, Free Energy Minimization, and Optimal Grip on a Field of Affordances”, *Frontiers in Human Neuroscience*, 8: 559, doi:10.3389/fnhum.2014.00599

[^carruthers-2003]: Carruthers, P. (2003), “On Fodor's Problem”, *Mind and Language*, 18(5): 502–523.

[^carruthers-2006]: ––– (2006), *The Architecture of the Mind*, Oxford University Press

[^chow-2013]: Chow, S.J. (2013), “What’s the Problem with the Frame Problem?”, *Review of Philosophy and Psychology*, 4: 309–331.

[^clark-1997]: Clark, A. (1997), *Being There: Putting Brain, Body, and World Together Again*, MIT Press.

[^dennett-1978]: Dennett, D. (1978), *Brainstorms*, MIT Press.

[^dennett-1987]: ––– (1987), “Cognitive Wheels: The Frame Problem in Artificial Intelligence”, in Pylyshyn (1987).

[^dreyfus-1991]: Dreyfus, H.L. (1991), *Being-in-the-World: A Commentary on Heidegger's* Being and Time, *Division I*, MIT Press.

[^dreyfus-1992]: ––– (1992), *What Computers Still Can't Do*, MIT Press.

[^dreyfus-2008]: ––– (2008), “Why Heideggerian AI Failed and How Fixing It Would Require Making It More Heideggerian”, in *The Mechanical Mind in History*, P. Husbands, O. Holland & M. Wheeler (eds.), MIT Press, pp. 331–371.

[^fetzer-1991]: Fetzer, J.H. (1991), “The Frame Problem: Artificial Intelligence Meets David Hume”, in Ford & Hayes (1991).

[^fodor-1983]: Fodor, J.A. (1983), *The Modularity of Mind*, MIT Press.

[^fodor-1987]: ––– (1987), “Modules, Frames, Fridgeons, Sleeping Dogs, and the Music of the Spheres”, in Pylyshyn (1987).

[^fodor-2000]: ––– (2000), *The Mind Doesn't Work That Way*, MIT Press.

[^fodor-2008]: ––– (2008), *LOT 2: The Language of Thought Revisited*, Oxford University Press.

[^ford-1991]: Ford, K.M. & Hayes, P.J. (eds.) (1991), *Reasoning Agents in a Dynamic World: The Frame Problem*, JAI Press.

[^ford-1996]: Ford, K.M. & Pylyshyn, Z.W. (eds.) (1996), *The Robot's Dilemma Revisited: The Frame Problem in Artificial Intelligence*, Ablex.

[^freeman-2000]: Freeman, W.J. (2000), *How Brains Make Up Their Minds*, Phoenix.

[^goodman-1954]: Goodman, N. (1954), *Fact, Fiction, and Forecast*, Harvard University Press.

[^hanks-1987]: Hanks, S. & McDermott, D. (1987), “Nonmonotonic Logic and Temporal Projection”, *Artificial Intelligence*, 33(3): 379–412.

[^haselager-1998]: Haselager, W.F.G. & Van Rappard, J.F.H. (1998), “Connectionism, Systematicity, and the Frame Problem”, *Minds and Machines*, 8(2): 161–179.

[^hayes-1991]: Hayes, P.J. (1991), “Artificial Intelligence Meets David Hume: A Reply to Fetzer”, in Ford & Hayes (1991).

[^heal-1996]: Heal, J. (1996), “Simulation, Theory, and Content”, in *Theories of Theories of Mind*, eds. P.Carruthers & P.Smith, Cambridge University Press, pp. 75–89.

[^lakoff-1980]: Lakoff, G. & Johnson, M. (1980), *Metaphors We Live By*, University of Chicago Press.

[^lifschitz-2015]: Lifschitz, V. (2015), “The Dramatic True Story of the Frame Default”, *Journal of Philosophical Logic*, 44: 163–196.

[^mccarthy-1986]: McCarthy, J. (1986), “Applications of Circumscription to Formalizing Common Sense Knowledge”, *Artificial Intelligence*, 26(3): 89–116.

[^mccarthy-1969]: McCarthy, J. & Hayes, P.J. (1969), “Some Philosophical Problems from the Standpoint of Artificial Intelligence”, in *Machine Intelligence 4*, ed. D.Michie and B.Meltzer, Edinburgh University Press, pp. 463–502.

[^mcdermott-1987]: McDermott, D. (1987), “We've Been Framed: Or Why AI Is Innocent of the Frame Problem”, in Pylyshyn (1987).

[^mithen-1987]: Mithen, S. (1987), *The Prehistory of the Mind*, Thames & Hudson.

[^pylyshyn-1987]: Pylyshyn, Z.W. (ed.) (1987), *The Robot's Dilemma: The Frame Problem in Artificial Intelligence*, Ablex.

[^rietveld-2012]: Rietveld, R. (2012), “Context-switching and Responsiveness to Real Relevance”, in J.Kiverstein & M.Wheeler (eds.), *Heidegger and Cognitive Science: New Directions in Cognitive Science and Philosophy*, Palgrave Macmillan, pp. 105–135.

[^reiter-2001]: Reiter, R. (2001), *Knowledge in Action: Logical Foundations for Specifying and Implementing Dynamical Systems*, MIT Press.

[^russell-1991]: Russell, S. & Wefald, E. (1991), *Do the Right Thing: Studies in Limited Rationality*, MIT Press.

[^samuels-2010]: Samuels, R. (2010), “Classical Computationalism and the Many Problems of Cognitive Relevance”, *Studies in History and Philosophy of Science*, 41: 280–293.

[^shanahan-1997]: Shanahan, M. (1997), *Solving the Frame Problem: A Mathematical Investigation of the Common Sense Law of Inertia*, MIT Press.

[^shanahan-2003]: ––– (2003), “The Frame Problem”, in *The Macmillan Encyclopedia of Cognitive Science*, L. Nadel (ed.), Macmillan, pp. 144–150.

[^shanahan-2010]: ––– (2010), *Embodiment and the Inner Life: Cognition and Consciousness in the Space of Possible Minds*, Oxford University Press.

[^shanahan-2005]: Shanahan, M. & Baars, B.J. (2005), “Applying Global Workspace Theory to the Frame Problem”, *Cognition*, 98(2): 157–176.

[^simon-1957]: Simon, H. (1957), *Models of Man*, Wiley.

[^sperber-1996]: Sperber, D. & Wilson, D. (1996), “Fodor's Frame Problem and Relevance Theory”, *Behavioral and Brain Sciences*, 19(3): 530–532.

[^wheeler-2005]: Wheeler, M. (2005), *Reconstructing the Cognitive World: The Next Step*, MIT Press.

[^wheeler-2008]: ––– (2008), “Cognition in Context: Phenomenology, Situated Robotics, and the Frame Problem”, *International Journal of Philosophical Studies*, 16(3): 323–349.

[^wilkerson-2001]: Wilkerson, W.S. (2001), “Simulation, Theory, and the Frame Problem”, *Philosophical Psychology*, 14(2): 141–153.


## 学术工具

* [如何引用本词条](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=frame-problem)。
* [预览本词条的 PDF 版本](https://leibniz.stanford.edu/friends/preview/frame-problem/)，见 [SEP 学会之友](https://leibniz.stanford.edu/friends/)。
* 在 [InPhO](https://www.inphoproject.org/entity?sep=frame-problem&redirect=True) 查找与本词条相关的话题与思想家。
* 在 [PhilPapers](https://philpapers.org/sep/frame-problem/) 查看本词条的增强文献目录及其数据库链接。

## 其他网络资源

- [Psycoloquy 上的框架问题文章集](http://www.cogsci.ecs.soton.ac.uk/cgi/psyc/ptopic?topic=frame-problem&submit=View+Topic)，载于美国心理学会主办的同行评议电子期刊 Psycoloquy。

## 相关词条

人工智能：基于逻辑的 | 认知科学 | 民俗心理学：作为理论 | 民俗心理学：作为心理模拟 | 归纳：问题 | 形式学习理论 | 逻辑：行动 | 心智表征 | 心灵：计算理论
