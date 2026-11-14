# 框架问题 The Frame Problem (Murray Shanahan)

*首次发表于 2004 年 2 月 23 日；2016 年 2 月 8 日实质修订。*

对大多数人工智能（AI）研究者而言，框架问题是这样一项挑战：在逻辑中表征行动的种种效应，却无须显式表征大量直觉上一望可知的非效应。但在许多哲学家眼里，AI 研究者的框架问题折射出更宽泛的认识论议题。原则上，我们能否把为推导行动之后果所需的推理限定在一定范围之内？更一般地说，又该如何解释我们显然具备的一种能力：仅凭当下情境中相关的东西便能决策，而无须显式考虑一切不相关者？

## 1. 引言

框架问题起先只是逻辑式人工智能（AI）中一个界域狭窄的技术性问题。后来心灵哲学家以添枝加叶、经过改易的形式把它接了过去，赋予其更宽泛的解释。它一头出生于 AI 研究者的实验室，另一头经哲学家之手处置，这一张力在二十世纪八九十年代激起了一场有趣且时而相当激烈的论辩。既然这个狭窄的技术问题已大体获解，近来的讨论便不再集中于解释之争，而更多着眼于宽泛意义上的框架问题对认知科学的意蕴。为把握这些论题，本文先考察技术面貌下的框架问题，继而检视哲学家重释该问题的若干进路，最后评估框架问题在当下的意义。

## 2. 逻辑中的框架问题

简言之，狭窄技术形式下的框架问题即是如此（McCarthy & Hayes 1969）[^mccarthy-1969]。借助数理逻辑，我们如何能写出刻画行动效应的公式，而不必再写出一大批伴随公式，去刻画那些行动平淡无奇、一望而知的非效应？且看一例。这一困难无须动用形式逻辑的全套器械即可说明，但须牢记：魔鬼藏在数学细节之中。设我们写下两个公式，一个刻画给物体上漆的效应，另一个刻画移动物体的效应。

1. *Paint*(*x*, *c*) 执行后 *Colour*(*x*, *c*) 成立
2. *Move*(*x*, *p*) 执行后 *Position*(*x*, *p*) 成立

现在设有一个初始情境，其中 *Colour*(*A*, *Red*) 与 *Position*(*A*, *House*) 成立。依照演绎逻辑的机制，在动作 *Paint*(*A*, *Blue*) 之后又执行动作 *Move*(*A*, *Garden*)，此时何者成立？直观上，我们预期 *Colour*(*A*, *Blue*) 与 *Position*(*A*, *Garden*) 成立。可惜事情并非如此。若以经典谓词逻辑把上述内容写得更严格，并采用某种适于表征时间与动作的形式系统——例如情景演算（situation calculus，McCarthy & Hayes 1969）[^mccarthy-1969]——那么这两个公式仅足以支持 *Position*(*A*, *Garden*) 成立这一结论。原因在于，它们并未排除 *A* 的颜色被 *Move* 动作改变的可能性。

要扩充这样一种形式化，让正确的常识结论水到渠成地随之而出，最直接的办法是添上一批显式描述每个行动之非效应的公式。这类公式称为 *frame axioms*（框架公理）。就手头这个例子来说，我们需要一对框架公理。

1. *Colour*(*x*, *c*) 若事先成立，则经 *Move*(*x*, *p*) 之后依然成立
2. *Position*(*x*, *p*) 若事先成立，则经 *Paint*(*x*, *c*) 之后依然成立

换句话说，给物体上漆不会改变其位置，移动物体也不会改变其颜色。添上这两个公式（用谓词逻辑写得更严格）之后，想要的结论便都能推出。可是这远非令人满意的解法。既然 **大多数** 行动并不触动情境的 **大多数** 属性，那么在一个含 *M* 个行动与 *N* 个属性的论域中，我们通常就得写出近于 *MN* 条框架公理。这套公式无论注定要显式存进机器内存，还是只作为设计者规范的一部分，都是一桩不受欢迎的负担。

这样，挑战就在于找到一种办法，用形式逻辑更经济地捕获行动的非效应。我们需要的似乎是某种把那条经验法则一般地宣布出来的方式：**除非** 有证据表明相反，方可假定一个行动会改变情境的给定属性。这一默认假定名为 *common sense law of inertia*（常识惯性定律）。（技术上的）框架问题可以看作把这条定律形式化的任务。

做到这一点的主要障碍，是经典逻辑的 *monotonicity*（单调性）。在经典逻辑中，由一组公式可推出的结论集只会随公式的增添而 **扩大**。于是，任何带有开放式例外集的规则都无法表达，而常识惯性定律恰是这样一条规则。比如说，往后我们也许想补一条公式，刻画把物体移进油漆桶时对公理 3 出现的那个例外。但我们先前没有想到这个例外，这不应妨碍我们运用常识惯性定律、推出足够宽的（可废止的）结论集，使推理得以启动。

正因如此，基于逻辑的 AI 研究者花了大量力气去发展各式 *non-monotonic*（非单调）推理形式系统——例如 *circumscription*（限定推理）（McCarthy 1986）[^mccarthy-1986]——并考察其对框架问题的应用。然而事情从未一帆风顺。前进路上最麻烦的绊脚石之一，由所谓的 *Yale shooting problem*（耶鲁射击问题）（Hanks & McDermott 1987）[^hanks-1987][^mcdermott-1987] 呈现出来：一个简单场景，若用非单调形式系统天真表征，便会引出违背直观的结论。雪上加霜的是，完备的解法还必须兼容并发行动、效果不确定的行动、连续变化，以及带间接衍生后果的行动。尽管有这些讲究，如今技术框架问题的解法已不止一种，足以支撑基于逻辑的 AI 研究。改进与扩展仍在涌现，但可以说尘埃落定：技术面貌下的框架问题已大体得解（Shanahan 1997; Lifschitz 2015）[^lifschitz-2015][^shanahan-1997]。

## 3. 认识论的框架问题

接下来看各位哲学家各自重新解释下的框架问题。哲学文献中第一次重要提及框架问题的，是丹尼特（Dennett）（1978, 125）。谜题据他所说在于：一个“对世界抱有诸多信念……的认知生物”在执行行动之际如何更新这些信念，使其依旧“大致忠实于世界”？福多（Fodor）在《心智的模块性》（*The Modularity of Mind*）里换位到机器人工程师的视角，心中带着框架问题。他提出了几乎一样的问题：“……机器的程序如何决定机器人应当重新评估哪些信念——既然它已着手这条或那条行动路线？”（Fodor 1983, 114）[^fodor-1983]。

乍看之下，这个问题与困扰 AI 研究者的那个逻辑问题只有印象层面的关联。哲学家的提问不同于 AI 研究者的问题：它并不以形式逻辑为语境，也不专门关乎行动的非效应。在后来的一篇文章里，丹尼特承认自己挪用了 AI 研究者的术语（1987）。但他随即重申其信念：AI 在框架问题中发现了一个“新的、深刻的认识论问题——原则上可以通达，却未为历代哲学家所注意”。

理解这个问题的最好办法，是设想自己是一位机器人设计者，造出的机器要完成诸如泡一杯茶这样的日常任务。而且，为了让框架问题干净利落地突显出来，还必须把思想实验约束在一类机器人设计之内——即采用显式存储、句子式世界表征的那一类，这正体现 *classical AI*（经典 AI）的方法论信条。以狭窄技术面貌攻克原始框架问题的 AI 研究者，正是在此约束之下工作，因为基于逻辑的 AI 本就是经典 AI 的一支。而对心灵计算理论抱同情态度的哲学家——他们主张心理状态由一组组命题态度构成，心理过程则是对相关命题施行的推理——同样惯于接受这一规定。

现在设这台机器人要从橱柜里取出一只茶杯。杯子此刻的位置以一个句子存于事实数据库，与表征当下情境无数其他特征的句子并列：环境温度、手臂构型、今天的日期、茶壶颜色，诸如此类。抓住杯子、将其自橱柜取出之后，机器人便要更新这一数据库。杯子的位置显然变了，这是一条亟待修订的事实。可还有哪些句子需要改动？环境温度未变，茶壶的位置未变。但倘若恰好有一把勺子原搁在杯中，勺子的新位置——随容器而来——便也得更新。

哲学家在此辨认出的认识论困难是这样的：机器人凭其行动，如何能把它必须重新考虑的命题限定在一定范围内？对一台足够简单的机器人来说，这似乎不算什么难题——它大可逐条查遍整个命题数据库，找出哪些须要修改。可是，一旦设想这台机器人具备接近人类的智能水平，从而哪怕只是转动一下马达，也得背负一个庞大的事实数据库逐一检查，这种策略便开始显得在计算上难以为继。

于是，AI 中一个相关问题得名框架问题的 *computational aspect*（计算侧面）（McDermott 1987）[^mcdermott-1987]：如何计算一个行动的后果，而计算无须遍历该行动的非效应。多数符号式 AI 程序处理框架问题计算侧面的方案，是麦克德莫特（McDermott）所谓“睡狗”策略（“sleeping dog” strategy）的某种变体（McDermott 1987）[^mcdermott-1987]。其要旨在于：表征当下情境的数据结构被更新以反映世界变化时，并非每个部分都须受检。只需修改表征世界已变侧面的部分，其余一概照旧（谨遵“莫惹睡狗”的箴言）。就机器人与茶杯这个例子而言，我们可以如此运用睡狗策略：让机器人更新其对杯子位置与橱柜内容的信念，却不必操心某个可能、也可能不在杯上或杯中的勺子。机器人的目标本不直接牵涉任何勺子。

但哲学问题并没有被这个计算议题穷尽。尚待解决的哲学问题是：机器人究竟如何才能断定，它已成功修订其全部信念，使之与其行动的后果相符？唯有此时，它才谈得上安全地应用“常识惯性定律”、假定世界其余部分原封未动。福多颇具启发性地将此比作“哈姆雷特问题：何时停止思考”（Fodor 1987, 140）[^fodor-1987]，并声称框架问题就是“从工程师视角看到的哈姆雷特问题”。照此理解，规避框架问题的显眼途径是诉诸 *relevance*（相关性）观念。反方的论证是：在任一给定行动的语境中，情境中只有某些属性相关，对行动后果的考虑尽可便利地限于这些属性。

可是，诉诸相关性无济于事。难点此刻变成：如何判定什么相关、什么不相关——而这取决于语境。再看从橱柜取出茶杯这个行动。若机器人的差事是沏茶，那么“便于从茶壶向杯中注水”便是相关的后果；若它的任务是打扫橱柜，更相关的后果，则是让原先被杯子压住的表面显露出来。经典范式的 AI 研究者可以迎难而上，尝试规定什么命题与什么语境相关。但惠勒（Wheeler）（2005; 2008）等哲学家从德雷福斯（Dreyfus）（1992）处得到提示，在此看出无穷回归的威胁。德雷福斯的原话是：“倘若每个语境都只能凭被选为相关的特征来识别，又须在更宽的语境中获得解释，AI 从业者便陷入语境的无穷回归”（Dreyfus 1992, 289）[^dreyfus-1992]。

化解无穷回归威胁的一条路子，是抓住这样一个事实：人固然比今天的机器人聪明，却照样出错（McDermott 1987）[^mcdermott-1987]。行动的后果，人时常预见不全，**即便** 推导这些后果所需的信息一样不缺——随便哪个象棋新手都可以作证。福多断言：“框架问题深不可测；其深直抵对理性的分析”（Fodor 1987）[^fodor-1987]。然而，理性分析容得下用于推出相关结论的计算资源之有限（Simon 1957; Russell & Wefald 1991; Sperber & Wilson 1996）[^russell-1991][^simon-1957][^sperber-1996]。有限理性有时会仓促定论，在逻辑上有瑕，但并不比人类思维本身更糟。不过，正如福多指出的：借人类自身的局限，来证成为推理过程可得的信息种类施加一条启发式边界，这本身并未解决认识论的框架问题（Fodor 2000, Ch.2; Fodor 2008, Ch.4; see also Chow 2013）[^chow-2013][^fodor-2000][^fodor-2008]。因为它避而不谈这条启发式边界如何划定——也就是说，它没有回应最初的问题：如何规定什么与推理过程相关、什么不相关。

尽管如此，倘若经典 AI 研究者深信语境的回归终有见底之日，他们仍会选定这样一条研究议程：从经典 AI 往日的成功中汲取灵感，构建以相关性判定规则为基础的系统。异议哲学家随即可以指出：AI 往日的成功一向局促于狭窄领域——下棋，或在受限微世界（microworld）中的推理，其中潜在相关命题的集合既固定又事先已知。相比之下，人类智能却能应对一个开放而变动不居的语境集合（Dreyfus 1992; Dreyfus 2008; Wheeler 2005; Wheeler 2008; Rietveld 2012）[^dreyfus-1992][^dreyfus-2008][^rietveld-2012][^wheeler-2005][^wheeler-2008]。再者，经典 AI 研究者也难逃来自整体论（holism）的论证。福多著作的一个关键主张是：划定行动的后果，一如科学中为理论求确证，任何东西都可能相关（Fodor 1983, 105）[^fodor-1983]。当下情境中可能牵涉的属性，并无任何 *a priori*（先验）界限。因此，福多在模块性论题中借框架问题支撑如下观点：心灵的核心过程——即参与信念确立的那些过程——“在信息上不封装”（informationally unencapsulated），意谓它们可从任何来源撷取信息（Fodor 1983; Fodor 2000; Fodor 2008; Dreyfus 1991, 115–121; Dreyfus 1992, 258）[^dreyfus-1991][^dreyfus-1992][^fodor-1983][^fodor-2000][^fodor-2008]。在福多看来，这正是为这些过程提供计算说明的根本障碍。

人们很乐意把福多的忧虑归因于一个谬误论证，其大意是：过程唯有在信息上封装，才可能在计算上可行。只需看看互联网搜索引擎之高效便知，凭借精巧的索引技术，实情并非如此。把任何一对看似不相干的关键词（比如“香蕉”与“曼陀林”）提交给网络搜索引擎，不足一秒便有回音。它能在数十亿网页的数据库中揪出提及这两个关键词的每一个页面（自然，如今也少不了本页）。但这并非眼下的问题。真正的问题——重复一遍——在于相关性。一个过程或许当真能索引到系统所知的一切香蕉与曼陀林之事，可所谓的神秘却在于：它到底凭什么能够先弄明白，天下事偏偏是香蕉与曼陀林同它的推理任务相关？

总之，我们既能把认识论的框架问题辨认出来，也能把它与计算层面的对应问题区分开。认识论的问题是：整体性、开放式、语境敏感的相关性，如何可能为经典 AI 所用的那类命题性、类语言表征所捕获？与之相应的 **计算** 问题则是：既然相关性是整体性、开放式、语境敏感的，一个推理过程又如何能够以计算上可行的方式，把自己局限于相关之物？

## 4. 常识惯性的形而上学

福多（Fodor 1987）[^fodor-1987] 揭开了框架问题的又一个维度：常识惯性定律的形而上学辩护在那里受到诘难。福多本人虽未把这一问题与宽泛框架问题的其他方面明确分开，但一经审视，它便显为一个独立的哲学谜题。论证如下。如前所述，AI 研究者所发展的逻辑框架问题诸解法，通常都诉诸某种版本的常识惯性定律——情境的属性默认不因行动而改变。这一假定据说正是由最初引出逻辑框架问题的那个观察来辩护的：行动执行、事件发生，大多数东西依然如故。

照福多的说法，这层形而上学辩护站不住脚。首先，有的行动改变的东西数不胜数。主张给物体上漆对屋里大多数物体的大多数属性几乎毫无影响的人，多半不得不承认：引爆一枚炸弹，实实在在影响其中大多数属性。而当追问“大多数属性”究何所指时，更深的困难便浮现了：要让任何关于“大多数属性”的主张得以成立，我们的本体论该收入哪些谓词？为把要点磨得更锐，福多引入“冰箱子”（fridgeon）概念：任一粒子在给定时刻是 *fridgeon*，当且仅当福多的冰箱恰在那一刻开着。如此一来，开或关福多的冰箱这个再简单不过的动作，似乎就引出了天文数字级的附带变化。在一个可能包含冰箱子的宇宙里，“大多数行动使大多数东西保持不变”还能成立吗？

这里的要点不在逻辑。开关福多的冰箱之于冰箱子的效应，可以轻而易举地以简洁方式表征出来（Shanahan 1997, 25）[^shanahan-1997]。要点另有所在——形而上学。常识惯性定律唯有在合适的本体论——对象与谓词选择得当——之下才谈得上辩护。可要让常识惯性定律行得通，怎样才算合适的本体论？冰箱子之流显然当予排除，可支撑这一取舍的又是什么形而上学原则？

这串问题连同引出它们的论证，与古德曼（Goodman）对归纳的讨论遥相呼应（Goodman 1954）[^goodman-1954]。古德曼的“归纳新谜”——通称 *grue paradox*（绿蓝悖论）——请我们留意谓词 *grue*：时刻 *t* 之前，它仅对绿色对象为真；时刻 *t* 之后，仅对蓝色对象为真。谜题是：凡在时刻 *t* 之前受检的绿色祖母绿，无一不是 grue 祖母绿的一个实例。于是“所有祖母绿皆 grue”这一归纳推断，看起来与“所有祖母绿皆绿”一样正当。当然，症结在谓词的选择。古德曼证明：归纳推断唯有在合适的谓词集合之下才奏效；福多则就常识惯性定律论证了几乎同样的道理。

费策尔（Fetzer）（1991）提出了框架问题与归纳问题之间的另一种紧密关系。他写道：“归纳问题［在于］为关于未来的某些推断、而非另一些推断提供辩护。框架问题亦然——［同样在于］为关于未来的某些推断、而非另一些推断辩护。第二个问题是第一个的特例。”不过，这种框架问题观争议极大（Hayes 1991）[^hayes-1991]。

## 5. 今天的框架问题

狭窄技术形态的框架问题，在二十世纪八十年代末至九十年代初的基于逻辑的人工智能研究中催生了大量工作；其更宽泛的哲学意涵也差不多同时浮出水面。而今天，各思想家给框架问题安排多大的分量，通常取决于他们在其他议题上的立场。

在经典 AI 内部，逻辑框架问题的多种可行解法已然成形；即便对严格恪守基于逻辑范式的人而言，它也不再被视作严重障碍（Shanahan 1997; Reiter 2001; Shanahan 2003; Lifschitz 2015）[^lifschitz-2015][^reiter-2001][^shanahan-1997][^shanahan-2003]。值得一提：逻辑取向的 AI 研究者尽可首尾一致地保留其方法论。同时，只要把自己的产品仅仅视为工程，便可拒斥传统认知科学家“要理解心灵，计算比表征更重要”这一信条。再者，倘若经典 AI 的目标并非造出具有人类级智能的计算机，而只是设计更好用、更有益的程序，那么福多、德雷福斯之流的哲学反对就对它无可奈何。然而耐人寻味的是：对彻底走出符号表征范式的 AI 研究者——比如投身情境机器人学（situated robotics）的人——来说，逻辑框架问题压根不在其日常研究之列。

固然有人主张框架问题即便在联结主义（connectionist）背景下也会出现（Haselager & Van Rappard 1998; Samuels 2010）[^haselager-1998][^samuels-2010]，它的哲学意义大半承自经典假设——计算相对于表征具有解释价值；这一假设已遭受经年的猛烈抨击（Clark 1997; Wheeler 2005）[^clark-1997][^wheeler-2005]。尽管如此，仍有许多心灵哲学家——福多与派利夏恩（Pylyshyn）便在其列——坚持如下看法：人类心理过程主要由一组命题之上的推理构成，而这些推理靠某种形式的计算来执行。在这些人看来，认识论框架问题及其计算对应物依旧是切切实实的威胁。

在惠勒等人眼中，经典 AI 与认知科学立在笛卡尔式的地基上；要克服框架问题，先得推翻这些假定，改取更海德格尔式的立场（Dreyfus 2008; Wheeler 2005; 2008; Rietveld 2012）[^dreyfus-2008][^rietveld-2012][^wheeler-2005]。据惠勒（2005; 2008），AI 中由布鲁克斯（Brooks）（1991）的工作肇始的情境机器人学运动，正是应当走的路。德雷福斯部分赞同，却主张情境机器人学的早期产品“只是巧妙绕开了框架问题，并未解决它”，因为“布鲁克斯的机器人只对环境中固定而可孤立的特征作反应，不理会语境与变化不居的意义”（Dreyfus 2008, 335）[^dreyfus-2008]。在德雷福斯看来，弗里曼（Freeman）（2000）的神经动力学工作才是更牢靠的根基，足以承托那种框架问题可能在其间消解的海德格尔式 AI 取向（另见 Shanahan 2010, Ch.5; Rietveld 2012; Bruineberg & Rietveld 2014）[^bruineberg-2014][^rietveld-2012][^shanahan-2010]。弗里曼的取径令德雷福斯折服：意义的神经动力学记录既非表征亦非联想，而是（借用动力系统的术语）一个为可能响应分类的“吸引子库”，“吸引子自身便是过往经验的产物”（Dreyfus 2008, 354）[^dreyfus-2008]。

框架问题留下的一项哲学遗产，是它把人们的目光引向与整体论（holism）——亦即所谓信息非封装性（informational unencapsulation）——相关的一整簇问题。回顾一下：所谓一个过程信息上不封装，指的就是与它相关的信息没有 *a priori*（先验）边界（福多有时用“isotropic”，即各向同性）。在近年的著述里，福多把“框架问题”一词用在一切信息上不封装的过程上，不再限于推断变化之后果的那些过程（Fodor 2000, Ch.2; Fodor 2006, Ch.4）[^fodor-2000]。显而易见，理想化的理性在此意义上便是信息上不封装的。还有人提出，各向同性会侵蚀所谓民间心理学（folk psychology）的理论论（theory theory）（Heal 1996）[^heal-1996]。（在希尔（Heal）看来，这为与之竞长的模拟论（simulation theory）助了一臂之力；但威尔克森（Wilkerson）（2001）论证，信息非封装性对民间心理学的两种说明皆为难题。）福多说过，类比推理便是“最纯粹形态的各向同性：一个过程，恰恰依赖在先前被假定互不相关的诸认知领域之间传递信息”（Fodor 1983, 105）[^fodor-1983]。不妨说，类比与隐喻思维的能力——创造性地跨越不同理解领域之边界的天赋——正是人类认知伟力的源头（Lakoff & Johnson 1980; Mithen 1996）[^lakoff-1980]。故而类比推理的信息非封装性潜在地极为棘手；对那些视模块为（语境不敏感的）专门家的模块性心灵理论而言，尤其如此（Carruthers 2003; 2006）[^carruthers-2003]。

德雷福斯声称，这个“框架问题的极端版本”与其要求较低的诸同族问题一样，同为经典 AI 与认知科学之笛卡尔式假定的产物（Dreyfus 2008, 361）[^dreyfus-2008]。他主张：一套恰当的海德格尔式心灵说明，同样是于此消解框架问题的基石；况且在此类情形下，我们“对世间事物如何行事的背景熟悉”已足以让我们“退后一步，想清楚何者相关、何以相关”。可是，鉴于相关性那整体的、开放式、语境敏感的品格，这种“想清楚”究竟如何达成，德雷福斯并未说明。惠勒则从相近的海德格尔式立场宣称：要解决他所谓的“跨语境”框架问题，须靠一种动力系统。按他的表述，“每一系统组分的因果贡献既部分地决定、又部分地取决于大量其他系统组分的因果贡献”（Wheeler 2008, 341）[^wheeler-2008]。沙纳汉（Shanahan）与巴斯（Baars）（2005; see also Shanahan 2010, Ch.6）[^shanahan-2010] 立足全局工作空间理论（global workspace theory）（Baars 1988）[^baars-1988] 提出相关方案：大脑通过具体实现一种架构，为信息非封装性问题纳入一个解答。在这架构中，a) 判定相关性的职责不经中央集中，而分布于诸并行专门过程之间；b) 一个按序列展开的全局工作空间状态，整合来自多个领域的相关贡献。

## 参考文献

**以下文献从原文照录，不作翻译；中国文献条目（古今）一律译为中文。**

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

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

- Psycoloquy（一份由美国心理学会主办的同行评议电子期刊）上的[框架问题专题文章](http://www.cogsci.ecs.soton.ac.uk/cgi/psyc/ptopic?topic=frame-problem&submit=View+Topic)。

## 相关词条

基于逻辑的人工智能 | 认知科学 | 作为理论的民间心理学 | 作为心理模拟的民间心理学 | 归纳问题 | 形式化学习理论 | 行动的逻辑 | 心理表征 | 心灵计算理论

**（译注：相关词条的中文站内链接将由管线在对应词条重译完成后统一挂接。）**
