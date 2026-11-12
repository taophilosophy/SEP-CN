# 生物信息 Biological Information (Marc Artiga)

*首次发表于 2024 年 7 月 19 日。*

信息概念在生物科学中被广泛使用。信息概念在分子生物学中居核心地位，那里习惯谈论翻译、转录、校对、冗余、DNA 文库、遗传密码、基因编辑或遗传程序。基因也被认为携带关于我们演化过去的信息。信息是认知科学的关键概念；据说认知系统以信息为食，这与心理表征、神经信号、神经递质等说法相关。动物交流亦然：信号通常被理解为信息载体；叫声、颜色、形状或气味携带关于捕食者、食物或身份的信息。激素也作为信号起作用，触发细胞内的信号通路。信息传递的变化也一直是宏观演化中的关键主题。在生物学中，信息话语的中心性与影响力难以夸大。

信息概念的这种普遍使用，引出一系列有趣问题。这些说法都指同一实体，还是指不同实体？信息的本性是什么？它可以被度量吗？信息话语纯粹是隐喻，还是应当照字面理解？信息概念有启发性，还是应当抛弃？信息是否起实质性的解释作用？是什么决定信号的信息内容？我们应当对信息持实在论吗？它可以还原为其他属性吗？本词条将处理其中一些问题。

这些问题常在各具体争论的语境中被处理，其中许多细节与不同论证和立场相关。尽管如此，也可辨认出一些反复出现的主题。本词条从一些一般问题开始（§1）；我们将讨论信息的关联意义（§1.1）与目的论意义（§1.2），并简要考察反实在论与消除论挑战（§1.3）。随后转向信息起核心作用的两个具体争论：分子生物学（§2）与动物交流（§3）。

## 1. 信息概念

与许多源自日常语言的表达一样，信息概念在生物科学中以不同方式使用。有时信息概念用于纯粹外部用途：它揭示我们怎样认识，而非对象有何属性。例如，当等位基因频率的差异被认为携带关于演化过去的信息时（如用于推断两个物种的系统发生距离），并不假定细胞或生物体使用或利用这一信息；毋宁说，我们可以用等位基因频率发现某些事实。这是信息的推论用法，而非解释用法。如此理解，基因携带信息，正如出土骨骼携带关于已灭绝物种的信息、年轮携带关于树龄的信息、红移携带关于膨胀宇宙的信息。

然而，信息话语常常把某种特定属性归予生物实体，而这种属性并不主要捕捉我们实践的认识属性。神经尖峰携带信息这一主张，似乎赋予它们某种关于性；当分子生物学家断言密码子为某些氨基酸编码时，他们似乎在归予某种指令性内容，它以某种方式告诉转录与翻译机器应如何进行。警报叫声携带关于捕食者的信息，似乎并不依赖我们的认识实践。表面上看，这些用法归予一种特定的客观属性，而不只是揭示我们能从中得知什么。这正是多数注意力所集中的信息意义，也是本词条的焦点。

作为初步近似，此意义的信息可刻画为三特征：非对称、规范性、非普遍。动物交流提供清楚例子：信息非对称，因为长尾黑颚猴发出警报时携带关于逼近之蛇的信息，蛇本身却不携带关于该叫声的信息。信息通常也是规范性的：它可以准确／不准确、真／假，或得到满足／未得到满足。若实际并无蛇逼近，信号便是虚假或不准确的。最后，信息在两方面不普遍：第一，有些动物特征携带信息，并非全部如此；第二，那些携带信息的特征也只关于有限的事实集合。当然，这只是生物实践所提示的基线刻画。这一分析是否准确，或在一般情形或具体情形中应被扩展、还原还是彻底抛弃，正是核心争点之一。

人们已投入大量精力，发展一种能容纳这些特征、并澄清生物学中信息概念用法的信息概念。本节将考察一种源自香农数学理论的理解方式，以及受该观点启发的更丰富概念。随后转向目的论进路，它们试图克服先前说明的某些困难；最后考察一些替代观点，它们试图把不同进路的洞见整合为融贯整体。

### 1.1 关联信息

进一步刻画生物科学中信息用法的第一种策略，诉诸香农（1948）的信息数学理论。香农主要关心一个设计问题：如何确定最优编码，以使交流中的错误最小化。他非常抽象地提出该问题（图 1）：给定“信源”的特定状态，“发送者”通过“信道”向“接收者”传递消息，信道可能引入噪声。设计者须设计最优编码系统，使接收者能以平均尽可能小的误差正确恢复信源状态。

*Figure 1*

![a series of nodes from left to right. 'Information source' with arrow to 'Transmitter' (combo labeled Message) with arrow labeled 'Signal' to an unlabeled node with another arrow labeled 'Received Signal' with arrow to 'Receiver' with arrow to 'Destination' (last two also labeled 'Message'). A node below labeled 'Noise Source' has an arrow to the unlabeled node in the middle.](../assets/information-biological/figure1.svg)

图 1

为解决这一问题，香农重拾并精炼奈奎斯特或哈特利等理论家此前用过的信息概念。在香农的刻画中，信源信息量大致可理解为有序程度（更准确地说，是其熵）。直觉上，信息量反映：信源可能处于一切状态，其实际状态有多大不确定性。具有许多等可能状态的信源，伴随高度不确定性（信息）。由此可定义互信息概念：两个事件空间携带互信息，当且仅当其中一个的状态改变另一个的概率分布。换言之，互信息可理解为衡量：知道一个变量的实际状态能在多大程度上减少关于另一个变量的不确定性。互信息越大，原消息能被重建得越准确。这些系统之间有多少信息，取决于系统状态平均改变概率的程度。因此，互信息捕捉所传递信息的平均量，并完全由二者统计关联决定。在数学上，互信息由描述状态空间的联合概率分布定义。这就是为什么香农的互信息概念有时被称为“关联信息”（但请注意，香农进路也包括熵或惊异度等一些并非关于关联的度量）。

毫无疑问，基因、警报信号或神经尖峰在此意义上携带信息。然而，许多人怀疑这一概念能否充分捕捉实际科学实践所归予的相关属性。如我们所见，刻画生物信息概念的常见方式建议它具三特征：非对称、规范性、非普遍；关联（香农）信息则不具备这些特征。第一，关联信息是对称的：若 *A* 携带关于 *B* 的信息，则 *B* 携带关于 *A* 的信息。若两个事件空间的状态统计相关，相关性是双向的。第二，它不是规范性的，即它似乎没有真值或准确性条件；*A* 携带的关于 *B* 的信息取决于二者实际统计关联，而这种关联没有清楚意义上的真假或准确与否。第三，信息也是普遍的：按对图 1 的通常解释，对可扮演信源、信道等角色的实体种类没有限制。因此，几乎任何物理系统都携带信息，且携带大量信息。结果，许多人认为生物信息的相关概念不能直接按香农进路理解。正因如此，关联信息（按香农式理解）通常与语义信息相对照。

然而晚近，人们采用不同策略，以挽救香农信息理论的某些要素，并发展受这些想法启发的说明。一方面，一些作者质疑通常假定的香农信息与语义信息之间的截然区分。例如，曼（2020）主张香农进路已提供一种语义信息理论（另见 Isaac 2019; Martínez 2019）[^isaac-2019][^martínez-2019]。另一些研究者发展了以不同方式超越香农度量的关联进路（Pocheville 2018; Scarantino 2015）[^pocheville-2018][^scarantino-2015]。例如，斯卡兰蒂诺（2015）发展出一种概率差异制造者说明，受香农信息与贝叶斯决策论启发，依据哪些状态的概率被改变、改变了多少以及后验概率是什么。波舍维尔（2018）的提议结合干预与其效果之间的香农互信息（捕捉因果特异性）与柯尔莫哥洛夫复杂度（反映序列复杂度及两序列间的算法互信息）。在波舍维尔的说明中，通过诉诸干预打破了互信息的对称性（另见 Calcott et al. 2020）[^calcott-2020]。

另一种（尽管如我们将见，相关的）进路，运用演化博弈论提供的形式工具研究信息与信号（导论见 Skyrms 2010; O’Connor 2020）[^o’connor-2020][^skyrms-2010]。就我们的目的而言，最相关的博弈是所谓“信号博弈”（见 Alexander 2002 [2021]）[^alexander-2002]。简言之，这些博弈论模型通常包括两个（或更多）参与者，一些扮演“发送者”，另一些扮演“接收者”。世界可处于不同状态，发送者观察并发出信号。接收者观察信号（不能直接观察世界）并执行行动。最后，发送者与接收者各有收益，取决于在给定世界状态下执行何种行动。由于有不同信号可选，发送者与接收者可遵循不同策略以协调行动。

这些高度理想化的模型已被用于研究信号的许多属性。例如，已表明在两参与者、两世界状态、两信号、两行动且利益共同的博弈中，信号系统不仅是纳什均衡（一组策略，其中无人能单方面偏离并改善收益），而且是唯一的吸引子。任何开始采用其他策略的互动参与者都会趋向这两个均衡之一（Huttegger 2007; Bruner et al. 2018）[^bruner-2018][^huttegger-2007]。简言之，这意味着在这些模型中，交流必然演化。因此，这些模型表明信号的出现既不以发送者也不以接收者的智能为前提。胡特格（2007）还主张，若世界状态概率不同，参与者有时可能收敛到“混同均衡”：总是发送同一信号（不论观察到的世界状态）并总是执行同一行动。也可用不同方式修改博弈：改变状态、信号或行动数目；考虑连续而非离散值（O’Connor 2014）[^o’connor-2014]；增加参与者（Skyrms 2009, 2010）[^skyrms-2009]；考虑部分或完全利益冲突情形（Martínez & Godfrey-Smith 2016）[^martínez-2016] 等等。关于这些模型的文献不断增长，已被用于为这些及相关领域的有趣主张辩护。

这些模型也提供一种新的信息观。斯凯姆斯（2010）为信号的信息内容提供度量，即一个向量，指明信号在多大程度上改变世界状态的概率。在此语境中，“改变概率”不应理解为信号因果地影响世界，而是技术意义：给定信号时世界状态发生的概率，相对于无信号时同一世界状态的概率差异。假设世界可处于四个等概率状态：S1、S2、S3、S4。若信号 *M* 仅在 S1 与 S3 发送，*M* 的信息内容为 $\langle 1, \infty, 1,-\infty\rangle$，因为它把 S1 与 S3 的概率各提高 1 比特（$-\infty$ 只是取对数的结果）。若 *M* 仅在 S3 发送，其信息内容为 $\langle -\infty, -\infty, 2,-\infty\rangle$。斯凯姆斯进路影响很大，并催生一系列类似提议（如 Isaac 2019）[^isaac-2019]。卡尔科特、波舍维尔与格里菲思（2020）主张斯凯姆斯进路未能捕捉信息“流”，并发展一种替代说明，把信号网络解释为因果图，按此信息取决于信号对行动的因果特异性程度。谢伊、戈弗雷-史密斯与曹（2018）采取多元论进路，定义两种信息概念：信息内容，捕捉给定信号时世界状态的概率；功能内容，取决于世界状态在信号稳定化中所起的作用。某种意义上，功能内容可理解为对目的论信息理论建模的方式（见下文与 Godfrey-Smith 2020）[^godfrey-smith-2020]。

最后，一些受香农进路广泛启发的替代提议，以反事实分析信息关系。伯奇（2014）把信号的命题内容定义为它在最近分离均衡中会携带的信息，即存在世界状态到信号一一映射的最近均衡。同样，为容纳欺骗情形，斯凯姆斯与巴雷特（2019）建议信号内容由发送者与接收者利益共同的子博弈决定。从另一视角，科恩与梅斯金（2006）主张：*x* 是 *F* 携带关于 *y* 是 *G* 的信息，当且仅当反事实条件句“若 *y* 不是 *G*，则 *x* 本不会曾是 *F*”非空真（内容反事实理论的经典版本见 Fodor 1987）[^fodor-1987]。

面对如此丰富的不同统计信息概念，可以采取不同态度。一方面，可主张其中之一是规定生物信息本性的正确方式。或者采取多元论，承认不同概念在不同语境或不同解释目的中有用（如 Shea, Godfrey-Smith, & Cao 2018）。还有一种选择：其中一些概念也许有认识效用，但没有一个捕捉生物信息的本性。为这一观点提供动机的一种方式，是坚持这些概念都未捕捉非对称、规范性且非普遍的信息意义。此外，由于这些进路定义在简化模型上，它们有非常精确、可作预测并提供可度量信息概念的优点，但它们与实际交流案例的联系变得更间接、更可疑。

无论如何，两个主张难以否认。第一，关联信息概念以及这些模型的工作，对理解生物信息的不同方面极为有用。第二，无论人们如何看待生物信息的本性，概率关系对人类与非人动物都重要，因此理解我们如何利用它是重要研究课题（Millikan 2004; Stegmann 2015）[^millikan-2004][^stegmann-2015]。

### 1.2 目的论信息

分析超越关联信息的生物信息概念的最著名替代框架，诉诸生物功能概念（Millikan 1984）[^millikan-1984]。功能概念是有希望的起点，因为它具备刻画语义信息的三个特征：一方面它是规范性的；性状的功能是该性状应当产生的效果，未能实现它意味着该性状功能失调或运作错误。于是，真／准确与假／不准确之别或可最终解释为某种功能失调。再者，功能通常是非对称的：眨眼的基本功能是把泪水铺过眼球，反之不然。最后，功能多半（也许专有地）归予生物体的某些性状，且每个性状只有部分效果算作其功能，故不普遍。因此，可试图用“具有功能”来分析“携带语义信息”（参 Maynard-Smith 2000）[^maynard-2000]。不幸的是，尽管有这些优点，这个简单提议不太可能成功，因为许多功能性性状并不具有该词任何相关意义上的语义信息。心脏应当泵血，但它不起信息作用。因此还需补充别的东西。

一种策略诉诸“发送者”与“接收者”。有趣的是，发送者-接收者框架的原始动机之一来自交流理论，尤其是香农进路；第二个经典来源是刘易斯（1969）关于惯例的说明。简言之，关键想法是：信息在两个（或更多）能动者或机制互动中涌现：发送者感知世界的某方面并发出信号，接收者收到后对世界采取行动。发送者与接收者的角色可由整个生物体扮演，也可由生物体部分或其他机制扮演。原则上可用因果术语定义发送者与接收者，故分析不循环。“发送者”与“接收者”角色通常在很抽象的层面描述，这当然有助于寻找一切信息系统之间的共同结构（想必也是香农原初动机）。

诉诸发送者与接收者引出一系列有趣问题。何种实体（生物体之外）可扮演发送者与接收者？此问题的不同回答十分重要，例如在遗传信息语境中；如下文所见，对发送者与接收者本性的不同看法导致对遗传信息的不同看法（神经科学中的平行讨论见 Cao 2012 与 Artiga 2016）[^artiga-2016][^cao-2012]。另一问题关涉是否总需要发送者与接收者二者。一些作者纯粹以发送者发展其观点（如 Neander 2017）[^neander-2017]，另一些则专诉诸接收者（Fresco, Ginsburg, & Jablonka 2020; Jablonka 2002; Stegmann 2009）[^jablonka-2002][^stegmann-2009]。第三个问题：什么决定信息内容？一些人认为内容主要由接收者过去的使用决定（Millikan 1984）[^millikan-1984]，另一些人采取基于生产者的进路（Neander 2017; Schulte 2018）[^neander-2017][^schulte-2018]。然而，以发送者与接收者框定信息关系并非没有风险：戈弗雷-史密斯（2014）警告一种倾向，即把任何似乎涉及信息关系的互动都强行作发送者-接收者解释。

无论如何，尽管目的论理论在争论中作用显著，这一进路仍是重大反对的目标。一般地说，生物信息的目的论观点不仅继承目的论进路的一般优点，也继承其困难（见词条：生物学中的目的论概念）。因此，在提供完全令人满意的生物信息理论时，也须考虑与功能概念不同（且不相容）分析方式相关的问题，以及经典问题。其中包括与功能不确定性潜在来源相关的忧虑，以及著名的“沼泽人”问题。若闪电击中沼泽，纯凭运气创造出唐纳德·戴维森的逐分子精确复制品，按目的论理论，他的任何状态都不携带信息，因为它们缺乏正确种类的演化功能。许多人认为这一后果难以接受。

部分由于这些理由，越来越多人倾向提供混合说明，把功能要素与关联信息及其他资源结合起来。伯格斯特伦与罗斯瓦尔（2011）建议，若我们把香农信息视为决策过程的结果而非关联度量（这除其他外意味着诉诸功能），就能找到某种非对称性并避开无差别反对。莱恩（2014）主张香农进路需补充“携带信息”与“具有携带信息的功能”之别。在认知科学语境中，尼安德（2017）与谢伊（2018）发展出包含功能、关联信息以及结构对应等其他特征的说明。马丁内斯（2019）以速率失真函数等各种交流理论概念补充目的论进路（另见 Mann 2020）[^mann-2020]。混合说明有时被设想为给纯关联说明添加要素，有时则旨在表明这些看似新异的特征其实已隐含在信息数学理论中。无论如何，混合说明提供了一条丰富的未来研究途径。

### 1.3 反实在论与消除论

至此我们主要关注把信息话语照字面理解、并寻求更详细规定生物信息之本性与解释价值的观点。然而一些哲学家与生物学家采取另一种视角。这里简要考察两个维度的批评：实在论／反实在论之分与消除论。它们大致对应以下问题：“信息”指称一种起某些因果与解释作用的真实属性，还是仅仅是“有用的虚构”？我们应当保留并提倡它在生物科学中的使用，还是应当劝阻？

第一，须把关于信息的实在论问题与关于表征的经典实在论争论区分开。确实，可能在一个争论中是实在论者，在另一个中则不是：例如，动物交流争论中的信息消除论者通常接受信号存在（如 Rendall, Owren, & Ryan 2009）。反之，一些批评设定心理表征的人拥抱信息概念（如 Chemero 2009）[^chemero-2009]。尽管两个争论显然相关，我们的问题具体关涉信息，尤其是语义信息（香农信息的存在一般不受质疑）。

迄今讨论的多数进路采取实在论态度，因为它们把语义信息视为某些状态所携带的真实属性，并起某些因果与解释作用。确实，多数实在论者也是还原论者，即主张语义信息可用更基本的术语解释（如诉诸关联、功能、发送者-接收者结构等）。

然而也有其他观点得到辩护，尽管其显赫程度因领域而异。在遗传信息语境中，非还原论实在论似乎由 Williams（1992: 10–13）与 Dawkins（1995: 4）暗示，尽管这些形而上学观点很少从哲学视角得到详细辩护。同样，可大致归为工具主义的观点在分子生物学（如 Sarkar 2000）[^sarkar-2000] 与神经科学中得到辩护，后者通常与关于表征的工具主义相联（Sprevak 2013; Cao 2022）[^cao-2022][^sprevak-2013]。莱维（2011）为生物学中的信息虚构主义辩护，主张信息概念是一种“阈限”隐喻，即“在可注意性门槛附近运作”，但仍在生物学理解中起真实作用。

与实在论／反实在论讨论平行的问题是：我们应保留并提倡信息概念在生物科学中的使用，还是劝阻？在每个与信息概念相关的争论中，通常都能找到消除论立场。如下文所见，这些立场在遗传信息（如 Griffiths 2001）[^griffiths-2001] 或动物交流（Rendall et al. 2009）[^rendall-2009] 语境中得到辩护，尽管它们在领域中属边缘立场。相反，在认知科学中，关于语义信息的消除论有一定支持，并引发重要而持久的争论（Chemero 2009; Hutto & Myin 2013, 2017）[^chemero-2009][^hutto-2013]。

如上所示，第一节考察的许多问题在具体争论中得到更详细展开。因此，为进一步深入这些问题、更好理解信息概念如何在生物学不同领域发挥作用，让我们聚焦两个领域：遗传信息与动物交流。

## 2. 遗传信息

如上所示，信息概念在分子生物学中作用显著，那里习惯谈论翻译、转录、校对、冗余、文库、遗传密码、基因编辑或遗传程序。信息对分子生物学“中心法则”的发展也至关重要，并与发育系统论、表观遗传学或先天性概念等极具争议的问题相关。因此，它是语义信息争论蓬勃发展的关键领域之一。

处理遗传信息问题时，第一个告诫是：基因概念本身充满复杂性（见 Meunier 2022 [2023]）[^meunier-2022]。在经典遗传学中，基因通常被定义为表型差异的差异制造者；而分子基因是一段 DNA（Falk 1986; Griffiths & Stotz 2013）[^falk-1986][^griffiths-2013]。此外，须把 DNA 一般功能与某段特定 DNA 的功能区分开。基因还扮演多种角色；有些为蛋白质或氨基酸编码，另一些起调控作用，就此而言也许更恰当地描述为阅读者，而非携带信息的机制。基因有时是消息，有时是信息源（Godfrey-Smith 1999）[^godfrey-smith-1999]。这些关于基因本性的形而上学问题，可能对信息话语的解释有重要后果。为简单起见，我们将尽可能搁置它们。

那么，首先为何把生物信息归予基因？基因在生物体发育以及个体间性状遗传中起关键作用。让我们先简要描述转录与翻译过程的关键方面，它们说明信息概念的中心作用，并有助于理解讨论的某些细节。基因表达过程包括多种实体与步骤：DNA 是由四种核碱基（胞嘧啶 [C]、鸟嘌呤 [G]、腺嘌呤 [A]、胸腺嘧啶 [T]）、一个糖和一个磷酸基团组成的大分子，呈双螺旋结构。在称为“转录”的过程中，某些 DNA 序列复制为“信使 RNA”即 *mRNA*（例外：胸腺嘧啶 T 换成尿嘧啶 U）。随后，mRNA 以多种方式改变（如 RNA 剪接），并运出细胞核进入细胞质。mRNA 到达核糖体后，这一大分子按 mRNA 中的序列把氨基酸连接起来，此过程称为“翻译”。这些连接起来的氨基酸构成蛋白质分子的构件。

制造蛋白质过程中的一个核心方面，是所谓“遗传密码”的存在，它把 RNA 序列的三联体（“密码子”）映射到氨基酸（尽管有些密码子不为氨基酸编码，而指示“起始”与“终止”功能）。例如，RNA 序列 CGT 映射到氨基酸“精氨酸”，AGT 映射到“丝氨酸”。破译遗传密码是遗传学与分子生物学发展的关键一步。遗传密码具组合性，且常被说成（其意义有待阐明）任意。这表明该过程的某些步骤类似于符号现象。密码还具有高度特异性：每个三联体为特定氨基酸编码。尽管不同三联体可为同一氨基酸编码（三联体有 64 种可能组合，氨基酸只有 20 种），在此意义上遗传密码被称为“简并的”。

把信息归予基因，常与一个更具体的主张相关。按分子生物学所谓“中心法则”，遗传信息只朝一个方向流动：从 DNA 到 RNA，再到蛋白质（见 Šustar 2007）。克里克（1958 年发表）的原始表述是：

> **中心法则**。它声称，一旦“信息”进入蛋白质，“它就不能再出来”。更详细地说，信息从核酸到核酸、或从核酸到蛋白质的传递是可能的，但从蛋白质到蛋白质、或从蛋白质到核酸的传递则不可能。此处信息指序列的“精确”决定，或是核酸中碱基的序列，或是蛋白质中氨基酸残基的序列。（1958: 153，强调为原文所有）

反过来，一些人诉诸这一法则，以维护并解释当代生物学研究的一个主导观念，即后天获得的特征不能遗传（魏斯曼主义）（Maynard Smith 2000; Sarkar 1996）[^maynard-2000][^sarkar-1996]。因此，信息概念在分子生物学中的使用有各种动机，其中一些位于当代生物学某个关键假设的核心。结果，“基因是否携带信息”的问题，与“基因是否起某种特权的演化或发育作用”的问题纠缠在一起。

就我们的目的而言，区分两个不同主张可能有用。第一个想法是基因携带信息。为捍卫这一建议，须表明某种可敬的信息概念能证明“编码”“遗传程序”“转录”“翻译”等表达的恰当性。实现这一目标也许还须确认信息所起的某种因果或解释作用。

第二个不同主张通常与前一主张相伴：基因起某种“独特的”、“特殊的”或“特权的”解释作用，使它们区别于发育或遗传中涉及的许多其他机制。关于遗传信息的争论之所以引人关注，正源于这种所谓的特权解释作用。例如，生物学家梅纳德·史密斯（2000）同时捍卫两个主张，并推动了对该问题的重新关注（见 Godfrey-Smith 2000a; Maynard Smith 2000; Sarkar 2000; Sterelny 2000）[^godfrey-smith-2000a][^maynard-2000][^sarkar-2000][^sterelny-2000]。但请注意，两个主张彼此独立：人可以主张基因在发育中起某种独特解释作用，而不依赖信息概念（如 Godfrey-Smith 2000b; Austin 2015）[^austin-2015][^godfrey-smith-2000b]；也可以承认基因携带信息，而不假定这以任何特殊方式使它们与众不同（如 Sarkar 2000）[^sarkar-2000]。

### 2.1 对信息模型的批评

信息进路受到不同视角的批评（如 Griesemer 2005）[^griesemer-2005]。一条批评强调：一旦人们把基因视为信息性的，便往往把其他因果因素视为该信息表达的单纯使能条件。信息观强烈支持基因控制并指导发育、而其他因素留在背景中的想法。确实，信息模型被比作先成论（如 Oyama 1985; Moss 1992）[^moss-1992][^oyama-1985]。在其经典形式中，先成论主张生物体从自身的微缩形式发育而来，因而发育被理解为生长。结果，先成论不是解释有组织、有分化的成体如何从组织与分化较少的细胞发育而来，而是否认该现象。批评者主张，信息模型常提示类似的发育图景：假定一段 DNA 含有建造一只手的指令，实际上并不解释手如何发育，却助长一种错误直觉，仿佛已经给出了解释（Lehman 1970: 34）[^lehman-1970]。此外，批评者继续说，把基因视为某种特殊或特权的因果因素，为“先天”与“后天”、“自然”与“教养”等经典区分提供了基础，而这些区分已产生有害影响（Oyama 1985）[^oyama-1985]。另一些人对遗传信息这一想法本身更为苛刻。例如，萨卡尔（1996）借助 1960、70 年代分子生物学的发展，主张“信息”是一个“冒充理论概念的隐喻”，它给出分子生物学可能解释的误导图景（另见 Griffiths 2001）[^griffiths-2001]。

被称为发育系统论（DST）的运动所做的批评尤其有影响（Oyama 1985; Griffiths & Gray 1994; Griffiths & Knight 1998）[^griffiths-1994][^griffiths-1998][^oyama-1985]。DST 理论家提出所谓“对等论题”，按此

> 影响发育的众多因果因素所扮演的角色，并不能整齐地分为两类：一类专由 DNA 要素扮演，另一类专由非 DNA 要素扮演。（Griffiths & Gray 2005: 420）[^griffiths-2005]

尽管基因在发育中起不可或缺的作用，许多其他发育机制亦然。例如，构成表观遗传继承系统的许多机制，如 DNA 甲基化模式、膜或细胞器，会在亲子之间产生相似性，并与核与线粒体机器并行运作。因此，他们主张基因在任何方面都不享有特权。当然，给定特定环境因素，基因有时可能有一组可靠效果；但给定特定基因，环境因素也可能有一组可靠效果。这一观点深受莱沃丁（1974, 2002）批评的影响：他批评我们通常能区分基因与环境因素在产生表型结果中的因果责任这一想法。

对等论题成为许多批评的焦点。一种回应承认基因是与其他同等必要因素并列的一组原因，但同时指出一组使基因在某方面独特或特殊的特征。斯特雷尔尼、史密斯与迪基森（1996）主张，基因的信息角色独特，但非唯一；许多其他具有功能的发育机制（鸣唱学习、食物偏好、中心粒……）也携带信息。此外，由于只关注 DNA，其中一些机制被忽视。谢伊（2007, 2011）接受格里菲思的对等论题，但不认为承认基因携带信息就蕴含许多发育因素也携带信息，因为只有继承系统才能作为其功能的一部分携带语义信息。施特格曼（2012）主张“对等论题”可有不同定义；有些定义没问题但也琐屑（如基因与环境因素都是原因，故对等），另一些则争议大得多。使用对等论题者的挑战，是提出一种可信而有趣的“对等”意义。在晚近著作中，保罗·格里菲思与卡罗拉·施托茨拒绝强版本的对等论题。他们承认核酸作为蛋白质模板起独特作用，且核酸的遗传是关键创新，使因果特异的发育因素能从一细胞转移到另一细胞（Griffiths & Stotz 2013; Stotz & Griffiths 2017b）[^griffiths-2013][^stotz-2017b]。

### 2.2 遗传学中的信息进路

部分为回应这些批评，人们作了多种尝试，以发展能澄清并支撑遗传信息理论角色的说明。一方面，尽管基因无疑携带香农意义上的关联信息，许多人认为这一概念不适合维护一种特殊的解释作用；除其他外，如我们所见，该意义上的信息是普遍的。确实，基因常与功能失调的结果而非设计效果更相关：例如，橡子基因组与腐烂的相关性比与生长的相关性更强（Sterelny, Smith, & Dickison 1996; Griffiths & Gray 1994）[^griffiths-1994]。为处理此点及其他忧虑，一些依赖关联信息概念的晚近提议倾向于聚焦遗传物质的特异性或因果特征（Bourrat 2019; Calcott, Pocheville, & Griffiths 2020; Pocheville 2018）[^bourrat-2019][^pocheville-2018]。在晚近工作中，施托茨与格里菲思主张因果特异性与某种信息形式相关。更准确地说，他们借鉴沃特斯（2007）与韦伯（2006）此前工作，主张只有高度特异的因果关系才是信息性的，并诉诸伍德沃德干预主义因果观定义该概念（Griffiths & Stotz 2013; Stotz & Griffiths 2017a）[^griffiths-2013][^stotz-2017a]。施特格曼（2014）补充说，DNA 不仅高度因果特异，还是“外部排序过程”，即控制过程中每一步的外部过程。据他，这一特征或可解释其独特解释作用，并为其信息载体地位提供根据。

或者，可拥抱目的论进路以避开这些忧虑（Maynard Smith 2000）[^maynard-2000]。第一，与关联不同，功能不普遍（如光或温度等与发育相关的环境特征没有功能）。第二，功能不必是最常见的效果，故即便效果 $E_1$ 比 $E_2$ 更频繁，也不蕴含 $E_1$ 必是其功能。然而如我们所见，许多功能项并不携带相关意义上的信息，故功能不能说明全部（Shea 2007）[^shea-2007]。为支持一段 DNA 的信息本性（它最终可用于维护独特解释作用），须发展极为精细的说明，其中可能包括（但不限于）生物功能。

雅布隆卡（2002）的提议诉诸接收者或解释者的功能（另见 Fresco, Ginsburg, & Jablonka 2020）。据她，当接收者对 *S* 有演化出的反应，且 *S* 形式变化对应接收者变化时，实体或过程 *S* 携带信息。因此，食谱、警报叫声、DNA 序列、日照长度或天空外观都携带信息，只要有功能性接收者存在。在此意义上，信息由解释者赋予（Jablonka 2002: 586）[^jablonka-2002]。这与“信号是携带信息的特殊系统、其中还有演化出的发送者”相容。然而在雅布隆卡的说明中，尽管基因携带信息，它们并不享有特权（信息或解释）地位。

谢伊（2007）提出替代说明。其提议依赖他自己的信息目的论语义说明，诉诸发送者-接收者系统与关联信息，尽管他的多数洞见也可被其他目的论理论家接受。第一，在具有演化功能的性状中，他聚焦继承系统，即功能为产生可遗传变异的系统。DNA 及其相关发育机器（细胞与环境因素）在此意义上算作继承系统，因为其功能是产生可遗传表型。在此框架中，发育系统扮演接收者，DNA 扮演中介。其进路的一个有趣特点是不依赖 DNA 的任何特定特征，如编码的特异性或所谓的任意性。

另一些人质疑把分子生物学中某些机制描述为发送者与接收者。例如，莱维（2011）主张，所谓遗传信息并无真正的发送者。同样，戈弗雷-史密斯（2014）主张基因组涉及阅读者（细胞内转录翻译机器），但没有清楚的发送者，故基因可能作为“线索”而非信号起作用（关于线索／信号之别，见 §3）。他还探讨发送者与接收者如何在典范-边缘轴上变化。相反，卡尔科特（2014）与普拉纳（2014）主张基因扮演发送者与接收者角色，故它们是产生并阅读信息的机制，而非携带信息者。

常被提及以帮助刻画遗传信息的另一属性是任意性（Godfrey-Smith 2000a; Maynard Smith 2000; Sarkar 2000; Sterelny 2000, Fox Keller 2009）[^fox-2009][^godfrey-smith-2000a][^maynard-2000][^sarkar-2000][^sterelny-2000]。这一概念与莫诺（1970）的“无偿性”（gratuité）相关，需要更多阐发，且争议极大；用戈弗雷-史密斯的话说（2000a: 205），它是“生物学中有用却难以捉摸的概念”。例如，梅纳德·史密斯（2000）以符号学意义理解“任意性”，即形式（化学成分）与意义（基因被开启或关闭）之间缺乏必然性；此处的清楚类比是语言意义，通常说语言意义是任意的，即替代的声音可同样好地代表任何给定内容。因此，想法是：若转录翻译机器的其余部分相应修改，DNA 碱基与三联体之间许多映射都可能。这与弗朗西斯·克里克著名建议相关：遗传密码结构是“冻结的偶然”，初次出现时高度偶然，此后极难改变。据梅纳德·史密斯，遗传密码的任意性是证成遗传信息归予、并使它成为特殊因果类型的核心特征之一。

然而任意性概念难以精确化，许多人主张理解该概念的标准方式未能给出生物信息的定义性属性（Stotz & Griffiths 2017a）[^stotz-2017a]。一个忧虑是：若有足够多因果链，任何关系都可能显得任意（Godfrey-Smith 2000a）[^godfrey-smith-2000a]。施特格曼（2004）对捕捉遗传密码任意性的某些标准方式作了有洞见的批评，主张其中多数也适用于许多其他生化关系。尽管如此，他仍捍卫遗传密码的任意性，其意义是：密码子需要某些化学与结构属性来指定氨基酸，但这些属性并非由某种化学原理决定。他还认为，这一任意性概念并不蕴含基因携带语义信息。莱恩（2019）以其所称分子“适配器”发展任意性说明，即把两个原本不相关的属性耦合起来、使它们作为中介而非协作原因运作的机制。普拉纳与卡尔克曼（2021）主张，通常被混在一起的有两个不同任意性概念，部分因为人类语言同时例示二者。一个指存在本可替代实际信号的替代结构，另一个指信号与内容之间缺乏相似。

此争论中还有三个区分相关。一方面，一个重要区分关涉“近端”信息与“终极”信息，取决于遗传信息是否构成性地依赖演化史。目的论说明通常假定前者，因为它们常拥抱功能病因论，即功能取决于被选择的效果（Millikan 1989; Neander 1991）[^millikan-1989][^neander-1991]。例如，谢伊（2007）主张遗传信息有助于对适应性复杂性的系统发生解释，这不同于个体发生解释。相反，格里菲思（2016）主张遗传信息必须有助于解释发育，而终极信息在此任务上失败。若两个生物体含同一等位基因，一个源自祖先，另一个由突变“新出现”，二者在解释发育上地位相同，但只有前者可有基于演化过去的信息（这与沼泽人问题相关；见 §1.2）。

第二个区分关涉核酸携带的是关于 DNA 某些直接因果产物（如 mRNA 或蛋白质）的信息，还是关于表型（理解为整个生物体的属性，如大小、行为模式或形状）的信息。例如，一些人认为遗传信息关涉氨基酸或蛋白质的产生（Godfrey-Smith 2004）[^godfrey-smith-2004]，另一些人则认为它关于表型或环境特征（Shea 2007; Sterelny et al. 1996）[^shea-2007][^sterelny-1996]。科伊夫（2020）主张目的论理论的某些核心主张与基因携带关于表型的远端信息不相容。一个相关区分关涉基因携带关于“何种实体”的信息；例如，施特格曼（2005）主张基因携带关于合成“过程”（而非其“产物”）的信息，正如苹果派食谱携带关于如何烤派而非关于派本身的信息。他还建议 DNA 转录的近端产物是 RNA，而非氨基酸或蛋白质，故若真选取近端效果，连蛋白质也不会被表征。

此点与另一问题相关。尽管迄今我们假定信息是描述性的（即应说明世界某部分如何），信息也可是指令性的，即说明人在世界中应如何行动。这很重要，因为许多接受基因携带信息的人假定它是某种指导性（即指令性）内容；如梅纳德·史密斯（2000）所建议，“它是食谱，不是蓝图”。认为内容是指令性的一个理由，是蛋白质或表型（最可信的内容）是 DNA 合成的效果，而 DNA “事先”规定导致特定产物的操作种类与顺序（Stegmann 2005）[^stegmann-2005]。此外，尽管基因有助于产生哪种分子或性状很清楚，它描述性地表征哪种环境特征却远不清楚。戈弗雷-史密斯（1999）建议内容是指令性的，因为若有某种不匹配，错误在解释机制而非基因（故其适合方向为世界到心灵）。按谢伊，基因是“推-拉”表征（见下文），即同时携带指示性与指令性内容。例如，为浓密毛发编码的基因，其内容会是“环境寒冷，长出浓密毛发”。

总之，核酸无疑携带关联信息，但许多人认为这一事实无法支撑基因在遗传与发育中应有的特殊解释作用。能否刻画一种足以支撑特殊或特权解释作用的替代信息概念，仍有争议。相关地，这一争论的结果可能对密切相关的概念有重要后果，如“遗传程序”观念（见 Moss 1992; Godfrey-Smith 2000b; Fox Keller 2001; Baetu 2012; Planer 2014）[^baetu-2012][^fox-2001][^godfrey-smith-2000b][^moss-1992][^planer-2014]。

## 3. 动物交流

非人动物交流（简称“动物交流”）是不断成长的研究领域。交流已在许多物种中得到确认，包括蛙、蚂蚁、马鹿、座头鲸、象海豹与鸣禽，形式多样，从声音、气味到行为模式。动物交流引出一系列复杂而有趣的问题，如信号与意义的本性、交流（含语言）演化、信号可靠性，或交流与认知的关系。本节只关注与生物信息概念最直接相关的方面。

交流中，信息通常归予信号，但同样，信号概念本身仍有争议。信号（如警报叫声与求偶展示）常与线索（如足迹）区分开。按梅纳德·史密斯与哈珀（2003: 3）提供的最广为接受的定义，信号是

> 任何改变其他生物体行为的行为或结构，它因该效果而演化，且其有效是因为接收者的反应也已演化。

有趣的是，这一定义未提及信号携带信息，尽管梅纳德·史密斯与哈珀（2003: 3）明确说

> [从该定义]可推出：信号必携带信息——关于信号发送者的状态或未来行动，或关于外部世界——且该信息为接收者所关注。

另一些人明确以信息术语定义信号；例如，奥特（1974: 385）建议信号是“由自然选择塑造或维持的行为、生理或形态特征，因为它们向其他生物体传递信息”。布拉德伯里与维伦坎普（1998: 2）则把交流定义为“从发送者向接收者提供信息”。相反，线索是用于获取关于世界之信息的行动或结构，但它并非为传递信息而演化。警报叫声与足迹都可能指示捕食者存在，但只有前者演化为向接收者传递此信息。

动物信号与生物信息的密切联系引出一些重要问题：“信息”应如何理解？该信息的内容是什么？是否存在不诉诸信息概念的理解交流的替代框架？信息视角与交流、认知有何联系？

### 3.1 功能指称

当代最早关于动物交流的争论之一发生在 1970、80 年代，关涉动物信号能否指称外部世界中的对象与事件，还是只能指示内部状态或行为倾向（见 Smith 1977: 77）[^smith-1977]。具有告知接收者世界状态（而非发送者特征）之功能的信号，被称为“功能指称的”，因为其功能角色类似人类语言中的词（Hauser 1996: 509）[^hauser-1996]。这场争论的部分动机，来自一种广泛观点：只有人类能就世界中的对象与事件交流（见 Allen & Hauser 1993）[^allen-1993]。

有趣的是，即便功能指称的支持者也承认，信号也指示或携带关于情感状态、个体身份或后续行为的信息（Seyfarth, Cheney, & Marler 1980; Macedonia & Evans 1993）[^macedonia-1993]。这场争论迫使论者反思信号与信息的本性。例如，在一篇有影响的论文中，马其顿与埃文斯（1993）以两个属性定义指称性信号。第一，一切引发刺激必须属于共同范畴（即信号特异性或“产生标准”）；第二，信号的存在应足以在无引发刺激时产生行为（“知觉标准”）。最终，经验证据与理论研究倾向于把信号视为功能指称的；这场讨论使该立场在动物行为学中逐渐成为主流。

### 3.2 影响进路与信息进路

然而，交流的信息进路受到另一角度的攻击。道金斯（1976）在《自私的基因》中提出基因之眼视角。作为该视角的延伸，道金斯与克雷布斯（1978）提议，信号应被视为个体利用另一动物肌肉力量的手段。按此观点，信号是操纵接收者的手段：信号的功能是使接收者以有利于发送者的方式行动，不论是否也有利于接收者：

> 当动物（行动者）做出某个似乎是选择之结果的行为，以影响另一动物（反应者）的感觉器官，使反应者的行为变得有利于行动者时，便说发生了交流。（Dawkins & Krebs 1978: 283）[^dawkins-1978]。

他们的批评包含两个关键想法。第一，经典病因论视角假定交流发生在合作的生物体之间。道金斯与克雷布斯则强调发送者利益的作用，把交流理解为一场斗争：一方寻求影响并操纵接收者，另一方抵抗。第二，他们主张，只有在合作框架内，把交流理解为信息传递才有意义，因此提出一种操纵论范式，回避信息概念。

由于克雷布斯与道金斯是在“信号必须以合作能动者为前提”的假定上发展批评，许多研究转而解释交流的可靠性，并厘清支撑其存在的机制。人们提出亲缘选择、互惠或著名的 handicap 原则（Zahavi 1975）[^zahavi-1975] 等机制；迄今这些机制都预设，平均而言接收者至少部分有意投入交流（Wheeler et al. 2011）[^wheeler-2011]。因此，就此而言，现有证据似乎指向：发送者与接收者至少需要部分共同利益（但见 Martínez & Godfrey-Smith 2016）[^martínez-2016]。

在后来的论文中，克雷布斯与道金斯（1984）澄清（或部分修改）了两个重要方面。一方面，他们承认合作可能比先前论文所暗示的更常见。然而若果真如此，人们会问：把交流描述为操纵、其中有“操纵者”与“受害者”（在合作情形中扮演“自愿受害者”），在许多情形中是否误导。另一方面，他们似乎并未完全拒绝信息视角，而是淡化其重要性；他们最终把观点表述为：信息（不只理解为关联，而是语义信息；Krebs & Dawkins 1984: 395）[^krebs-1984] 不如操纵、或说服的影响“重要”或“切题”（确实，道金斯 2003: 97–103 称赞某些信息模型）[^dawkins-2003]。这些想法催生了一个有趣传统：把信号理解为对接收者具有某种“影响”的状态，并认为信息概念不适用，或至少远不如通常所想的那样核心。

晚近，伦德尔、欧文与瑞安等生物学家的工作延续这种对信息进路的怀疑，并引发有趣讨论（如见 Rendall et al. 2009 及若干回应：Font & Carazo 2010; Ruxton & Schaefer 2011; Scarantino 2010; Scott-Phillips 2010; Seyfarth, Cheney, Bergman, et al. 2010）[^font-2010][^rendall-2009][^ruxton-2011][^scarantino-2010][^scott-2010]。第一，他们主张“信息”概念本身常定义不清。第二，他们建议，对信息的排他关注（他们主张这与对诚实交流的关注相伴）使研究者忽视许多影响信号设计的方面，如知觉偏差（Owren, Rendall, & Ryan 2010）。弗里克、比希与莫雷诺（2019）也发展出一种基于组织而非演化的影响说明。

该传统的支持者有时反对交流的信息进路，理由是它要求发送者与接收者利用心理表征，类似人类语言交流所涉表征（Rendall & Owren 2013）[^rendall-2013]。然而有人回应说，这一反对没有根据，因为信息研究者既未隐含也未明言假定蜜蜂、狐獴或黑顶山雀利用类似人类认知过程的表征（Seyfarth, Cheney, Bergman, et al. 2010）。

作为回应，同情信息视角的人主张，研究的某些方面其实支持其进路。一方面，假定信号携带信息数十年来一直是富有成效的假定（Seyfarth, Cheney, Bergman, et al. 2010）。此外，它与当代动物心灵研究一致，后者假定学习或归类等认知能力利用信息（Wheeler et al. 2011）[^wheeler-2011]。

尽管这场争论通常以对抗方式框定，也可以把两种观点视为互补而非冲突（Ruxton & Schaefer 2011; Scarantino 2010; Stegmann 2013b；但见 Kalkman 2019）[^kalkman-2019][^ruxton-2011][^scarantino-2010][^stegmann-2013b]。影响进路对分析信号“形式”相关的许多属性（即可检测性、与接收者偏差的关系等）非常有用，且在生物体间存在显著利益冲突时能提供有启发性的视角；信息进路则可能阐明其他方面，如内容、引发行为，或交流的可靠性与维持。例如，鸟类求偶鸣唱的复杂性与变异性提示它们可能携带关于歌者质量的信息，但其重要功能也可能包括防止厌倦与习惯化（Searcy 1992; Rendall, Owren, & Ryan 2009）[^searcy-1992]。每种视角都可能有助于洞察交流的不同方面。无论如何，这种折中与论者的一些主张并不融洽，故它最终是否是融贯、稳定而有成果的立场，仍有待观察。

### 3.3 动物交流研究中的信息

事实上，如今多数动物交流研究采取信息（而非影响）进路，其中信号可具功能指称性，这引出关于信号与内容本性的一系列重要问题。不幸的是，尽管人们普遍使用信息，却很少定义它。鉴于当前科学实践，“信息”概念的最佳解释与解释作用是什么？

研究者常把信息概念描述为“不确定性的减少”，这提示关联信息概念（如 Seyfarth, Cheney, Bergman, et al. 2010）。一些工作甚至明确使用香农交流理论，较精确地分析交流的某些方面，如信道容量或信号库的复杂度（Haldane & Spurway 1954; McCowan et al. 1999; Wilson 1962）[^haldane-1954][^mccowan-1999][^wilson-1962]。然而，当科学家给出明确的交流定义时，多数诉诸信号的标准定义（Maynard-Smith & Harper 2003; Searcy & Nowicki 2005）[^maynard-2003][^searcy-2005]，而这些定义以目的论术语界定信号（见上）。部分原因是 §1.1 所述关联信息的普遍性问题（Kalkman 2019）[^kalkman-2019]。因此，一种描述现状的方式是：多数研究实际上对信号与信息的本性采取目的论进路，而一些工具与明确描述更符合关联信息概念。普法伊费尔（2006）与萨卡尔（2013）对动物交流研究中使用关联信息提出一些反对。作为回应，曼（2018）为该领域使用交流数学理论作了有趣分析与辩护。另一方面，决策论工作提供了一种不同于香农信息进路的定量信息度量，它基于信号如何改变某些事件的先验概率（Kight et al. 2013）[^kight-2013]。这一进路深刻影响了斯凯姆斯（2010）及上文综述的依赖其工作的后续文献（另见 Scarantino 2015）[^scarantino-2015]。

就交流的标准目的论进路（如梅纳德·史密斯与哈珀 2003 的广泛使用定义）而言，仍有争议点。例如，斯科特-菲利普斯（2008）以共同适应解释梅纳德·史密斯与哈珀的分析，据他，这不同于且优于基于信息的进路。反过来，斯卡兰蒂诺（2013）主张，若不诉诸信息概念，斯科特-菲利普斯（以及梅纳德·史密斯与哈珀）的提议过于宽松，因为它把某些强制情形误分类为信号。于是他发展出概率差异制造者理论，试图结合香农交流理论与贝叶斯决策论的洞见，按此信号的信息内容是各状态增量支持与总体支持的结合（Scarantino 2013, 2015）[^scarantino-2013]。然而，这一进路或类似进路能否解决宽松性问题，仍有争议（Kalkman 2019; Artiga 2021）[^artiga-2021][^kalkman-2019]。

有趣的是，在分子生物学（以及神经科学）中，发送者与接收者的存在与本性充满困难，而动物交流有非常自然的解释：发送者与接收者就是生物体。尽管如此，施特格曼（2009）捍卫基于接收者的目的论进路，按此信号地位与信息完全取决于接收者（回应见 Artiga 2014）[^artiga-2014]。另一争议问题关涉交流语用方面对发送者与接收者所要求的认知复杂度（Bar-On & Moore 2018）[^bar-on-2018][^bar-on-2018-2]。

动物信号的内容仍是争议中的研究主题。一个重要问题：动物信号携带的信息是描述性还是指令性？米利肯（1995, 2004）著名地主张，动物交流中的许多信号是她所称的“推-拉”表征，即同时携带描述性与指令性内容的表征。这一概念影响很大，被应用于许多关于表征内容的争论。另一方面，晚近日益显赫的另一视角（与信号是否功能指称的经典争论有些联系）建议，信号也具有表达主义意义（McAninch, Goodrich, & Allen 2009）。这些提议与晚近对交流语用方面及人类语言起源的兴趣相关（Bar-On 2018）[^bar-on-2018][^bar-on-2018-2]。

## References（引用注释）

**以下文献从原文照录，不作翻译；中国文献译为中文。**

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

[^alexander-2002]: Alexander, J. McKenzie, 2002 [2021], “Evolutionary Game Theory”, in *The Stanford Encyclopedia of Philosophy* (Summer 2021), Edward N. Zalta (ed.), URL = <[https://plato.stanford.edu/archives/sum2021/entries/game-evolutionary/](https://plato.stanford.edu/archives/sum2021/entries/game-evolutionary/)>.
[^allen-1993]: Allen, Colin and Marc Hauser, 1993, “Communication and Cognition: Is Information the Connection?”, *PSA: Proceedings of the Biennial Meeting of the Philosophy of Science Association*, 1992(2): 80–91.
[^andrews-2018]: Andrews, Kristin and Jacob Beck (eds), 2018, *The Routledge Handbook of Philosophy of Animal Minds* (Routledge Handbooks in Philosophy), Abingdon/New York: Routledge. doi:10.4324/9781315742250
[^artiga-2014]: Artiga, Marc, 2014, “Signaling without Cooperation”, *Biology & Philosophy*, 29(3): 357–378. doi:10.1007/s10539-014-9436-0
[^artiga-2016]: –––, 2016, “Teleosemantic Modeling of Cognitive Representations”, *Biology & Philosophy*, 31(4): 483–505. doi:10.1007/s10539-016-9525-3
[^artiga-2021]: –––, 2021, “Signals Are Minimal Causes”, *Synthese*, 198(9): 8581–8599. doi:10.1007/s11229-020-02589-0
[^austin-2015]: Austin, Christopher J., 2015, “The Dispositional Genome: *Primus Inter Pares*”, *Biology & Philosophy*, 30(2): 227–246, doi:10.1007/s10539-014-9454-y.
[^bar-on-2018]: Bar-On, Dorit, 2018, “Communicative Intentions, Expressive Communication, and Origins of Meaning”, in Andrews and Beck 2018: 301–312 (ch. 28).
[^bar-on-2018-2]: Bar-On, Dorit and Richard Moore, 2018, “Pragmatic Interpretation and Signaler-Receiver Asymmetries in Animal Communication”, in Andrews and Beck 2018: 291–300 (ch. 27).
[^baetu-2012]: Baetu, Tudor M., 2012, “Genomic Programs as Mechanism Schemas: A Non-Reductionist Interpretation”, *The British Journal for the Philosophy of Science*, 63(3): 649–671. doi:10.1093/bjps/axr042
[^bergstrom-2011]: Bergstrom, Carl T. and Martin Rosvall, 2011, “The Transmission Sense of Information”, *Biology & Philosophy*, 26(2): 159–176. doi:10.1007/s10539-009-9180-z
[^birch-2014]: Birch, Jonathan, 2014, “Propositional Content in Signalling Systems”, *Philosophical Studies*, 171(3): 493–512. doi:10.1007/s11098-014-0280-5
[^bourrat-2019]: Bourrat, Pierrick, 2019, “Variation of Information as a Measure of One-to-One Causal Specificity”, *European Journal for Philosophy of Science*, 9(1): article 11. doi:10.1007/s13194-018-0224-6
[^bradbury-1998]: Bradbury, Jack W. and Sandra Lee Vehrencamp, 1998, *Principles of Animal Communication*, Sunderland, MA: Sinauer Associates.
[^bruner-2018]: Bruner, Justin, Cailin O’Connor, Hannah Rubin, and Simon M. Huttegger, 2018, “David Lewis in the Lab: Experimental Results on the Emergence of Meaning”, *Synthese*, 195(2): 603–621. doi:10.1007/s11229-014-0535-x
[^calcott-2014]: Calcott, Brett, 2014, “The Creation and Reuse of Information in Gene Regulatory Networks”, *Philosophy of Science,*81(5): 879–890. doi: 10.1086/677687
[^calcott-2020]: Calcott, Brett, Arnaud Pocheville, and Paul Griffiths, 2020, “Signals That Make a Difference”, *The British Journal for the Philosophy of Science*, 71(1): 233–258. doi:10.1093/bjps/axx022
[^cao-2012]: Cao, Rosa, 2012, “A Teleosemantic Approach to Information in the Brain”, *Biology & Philosophy*, 27(1): 49–71. doi:10.1007/s10539-011-9292-0
[^cao-2022]: –––, 2022, “Putting Representations to Use”, *Synthese*, 200(2): article 151. doi:10.1007/s11229-022-03522-3
[^chemero-2009]: Chemero, Anthony, 2009, *Radical Embodied Cognitive Science* (A Bradford Book), Cambridge, MA: MIT Press.
[^cohen-2006]: Cohen, Jonathan and Aaron Meskin, 2006, “An Objective Counterfactual Theory of Information”, *Australasian Journal of Philosophy*, 84(3): 333–352. doi:10.1080/00048400600895821
[^crick-1958]: Crick, Francis, 1958, “On Protein Synthesis”, in The *Biological Replication of Macromolecules* (Symposia of the Society for Experimental Biology, 12), New York: Academic Press, 138–163. [[Crick 1958 available online](https://wellcomecollection.org/works/z3d5fnyg)]
[^dawkins-1976]: Dawkins, Richard, 1976, *The Selfish Gene*, New York: Oxford University Press.
[^dawkins-1995]: –––, 1995, *River out of Eden: A Darwinian View of Life* (Science Masters Series), New York: Basic Books.
[^dawkins-2003]: –––, 2003, *A Devil’s Chaplain: Selected Essays*, Latha Menon (ed.), London: Weidenfeld & Nicolson.
[^dawkins-1978]: Dawkins, Richard and John R. Krebs, 1978, “Animal Signals: Information or Manipulation?”, in *Behavioural Ecology: An Evolutionary Approach*, John R. Krebs and Nicholas B. Davies (eds), first edition, Sunderland, MA: Sinauer Associates, 282–309.
[^falk-1986]: Falk, Raphael, 1986, “What Is a Gene?”, *Studies in History and Philosophy of Science Part A*, 17(2): 133–173. doi:10.1016/0039-3681(86)90024-5
[^fodor-1987]: Fodor, Jerry A., 1987, *Psychosemantics: The Problem of Meaning in the Philosophy of Mind* (Explorations in Cognitive Science 2), Cambridge, Mass: MIT Press.
[^font-2010]: Font, Enrique and Pau Carazo, 2010, “Animals in Translation: Why There Is Meaning (but Probably No Message) in Animal Communication”, *Animal Behaviour*, 80(2): e1–e6. doi:10.1016/j.anbehav.2010.05.015
[^fox-2001]: Fox Keller, Evelyn, 2001, “Beyond the Gene but beneath the Skin”, in *Cycles of Contingency: Developmental Systems and Evolution* (Life and Mind: Philosophical Issues in Biology and Psychology), Susan Oyama, Paul E. Griffiths, and Russell D. Gray (eds), Cambridge, MA: MIT Press, 299–312 (ch. 21).
[^fox-2009]: –––, 2009, “Rethinking the Meaning of Biological Information”, *Biological Theory*, 4(2): 159–166. doi:10.1162/biot.2009.4.2.159
[^fresco-2020]: Fresco, Nir, Simona Ginsburg, and Eva Jablonka, 2020, “Functional Information: A Graded Taxonomy of Difference Makers”, *Review of Philosophy and Psychology*, 11(3): 547–567. doi:10.1007/s13164-018-0410-7
[^frick-2019]: Frick, Ramiro, Leonardo Bich, and Alvaro Moreno, 2019, “An Organisational Approach to Biological Communication”, *Acta Biotheoretica*, 67(2): 103–128. doi:10.1007/s10441-019-09342-2
[^godfrey-smith-1999]: Godfrey-Smith, Peter, 1999, “Genes and Codes: Lessons from the Philosophy of Mind?”, in *Where Biology Meets Psychology: Philosophical Essays*, Valerie Gray Hardcastle (ed.), Cambridge, MA: MIT Press, 305–332 (ch. 15). doi:10.7551/mitpress/7220.003.0017
[^godfrey-smith-2000a]: –––, 2000a, “Information, Arbitrariness, and Selection: Comments on Maynard Smith”, *Philosophy of Science*, 67(2): 202–207. doi:10.1086/392770
[^godfrey-smith-2000b]: –––, 2000b, “On the Theoretical Role of ‘Genetic Coding’”, *Philosophy of Science*, 67(1): 26–44. doi:10.1086/392760
[^godfrey-smith-2004]: –––, 2004, “Genes Do Not Encode Information for Phenotypic Traits”, in *Contemporary Debates in Philosophy of Science* (Contemporary Debates in Philosophy 2), Christopher Hitchcock (ed.), Malden, MA: Blackwell Publishing, 275–289.
[^godfrey-smith-2011]: –––, 2011, “Review of *Signals: Evolution, Learning, and Information*, by Brian Skyrms”, *Mind*, 120(480): 1288–1297. doi:10.1093/mind/fzs002
[^godfrey-smith-2014]: –––, 2014, “Sender-Receiver Systems within and between Organisms”, *Philosophy of Science*, 81(5): 866–878. doi:10.1086/677686
[^godfrey-smith-2020]: –––, 2020, “In the Beginning There Was Information?”, *Studies in History and Philosophy of Science Part C: Studies in History and Philosophy of Biological and Biomedical Sciences*, 80: 101239. doi:10.1016/j.shpsc.2019.101239
[^griesemer-2005]: Griesemer, James, 2005, “The Informational Gene and the Substantial Body: On the Generalization of Evolutionary Theory By Abstraction”, in *Idealization XII, Correcting the Model: Idealization and Abstraction in the Sciences* (Poznań Studies in the Philosophy of the Sciences and the Humanities 86), Martin R. Jones and Nancy Cartwright (eds), Amsterdam/New York: Rodopi, 59–115.
[^griffiths-2001]: Griffiths, Paul E., 2001, “Genetic Information: A Metaphor In Search of a Theory”, *Philosophy of Science*, 68(3): 394–412. doi:10.1086/392891
[^griffiths-2016]: –––, 2016, “Proximate and Ultimate Information in Biology”, in *The Philosophy of Philip Kitcher*, Mark Couch and Jessica Pfeifer (eds), New York: Oxford University Press, 74–97. doi:10.1093/acprof:oso/9780199381357.003.0004
[^griffiths-1994]: Griffiths, Paul E. and Russell D. Gray, 1994, “Developmental Systems and Evolutionary Explanation”:, *Journal of Philosophy*, 91(6): 277–304. doi:10.2307/2940982
[^griffiths-2005]: –––, 2005, “Discussion: Three Ways to Misunderstand Developmental Systems Theory”, *Biology & Philosophy*, 20(2–3): 417–425. doi:10.1007/s10539-004-0758-1
[^griffiths-1998]: Griffiths, Paul E. and Robin D. Knight, 1998, “What Is the Developmentalist Challenge?”, *Philosophy of Science*, 65(2): 253–258. doi:10.1086/392636
[^griffiths-2013]: Griffiths, Paul E. and Karola Stotz, 2013, *Genetics and Philosophy: An Introduction* (Cambridge Introductions to Philosophy and Biology), Cambridge/New York: Cambridge University Press. doi:10.1017/CBO9780511744082
[^haldane-1954]: Haldane, John B. S. and Helen Spurway, 1954, “A Statistical Analysis of Communication in ‘Apis mellifera’ and a Comparison with Communication in Other Animals”, *Insectes Sociaux*, 1(3): 247–283. doi:10.1007/BF02222949
[^hauser-1996]: Hauser, Marc D., 1996, *The Evolution of Communication*, Cambridge, MA: MIT Press. doi:10.7551/mitpress/2867.001.0001
[^huttegger-2007]: Huttegger, Simon M., 2007, “Evolution and the Explanation of Meaning”, *Philosophy of Science*, 74(1): 1–27. doi:10.1086/519477
[^hutto-2013]: Hutto, Daniel D. and Erik Myin, 2013, *Radicalizing Enactivism: Basic Minds without Content*, Cambridge, MA: MIT Press. doi:10.7551/mitpress/9780262018548.001.0001
[^hutto-2017]: –––, 2017, *Evolving Enactivism: Basic Minds Meet Content*, Cambridge, MA: MIT Press. doi:10.7551/mitpress/9780262036115.001.0001
[^isaac-2019]: Isaac, Alistair M. C., 2019, “The Semantics Latent in Shannon Information”, *The British Journal for the Philosophy of Science*, 70(1): 103–125. doi:10.1093/bjps/axx029
[^jablonka-2002]: Jablonka, Eva, 2002, “Information: Its Interpretation, Its Inheritance, and Its Sharing”, *Philosophy of Science*, 69(4): 578–605. doi:10.1086/344621
[^kalkman-2019]: Kalkman, David, 2019, “New Problems for Defining Animal Communication in Informational Terms”, *Synthese*, 196(8): 3319–3336. doi:10.1007/s11229-017-1598-2
[^kight-2013]: Kight, Caitlin R., John M. McNamara, David W. Stephens, and Sasha R. X. Dall, 2013, “Communication as Information Use: Insights from Statistical Decision Theory”, in Stegmann 2013a: 89–112 (ch. 3). doi:10.1017/CBO9781139003551.006
[^kõiv-2020]: Kõiv, Riin, 2020, “Elusive Vehicles of Genetic Representation”, *Biology & Philosophy*, 35(1): article 24. doi:10.1007/s10539-020-9741-8
[^krebs-1984]: Krebs, John R. and Richard Dawkins, 1984, “Animal Signals: Mind-Reading and Manipulation”, in *Behavioural Ecology: An Evolutionary Approach*, John R. Krebs and Nicholas B. Davies (eds), second edition, Sunderland, MA: Sinauer Associates, 380–402.
[^lean-2014]: Lean, Oliver M., 2014, “Getting the Most out of Shannon Information”, *Biology & Philosophy*, 29(3): 395–413. doi:10.1007/s10539-013-9410-2
[^lean-2019]: –––, 2019, “Chemical Arbitrariness and the Causal Role of Molecular Adapters”, *Studies in History and Philosophy of Science Part C: Studies in History and Philosophy of Biological and Biomedical Sciences*, 78: 101180. doi:10.1016/j.shpsc.2019.101180
[^lehman-1970]: Lehman, Daniel S., 1970, “Semantic and Conceptual Issues in the Nature-Nurture Problem”, in *Development and Evolution of Behavior: Essays in Memory of T. C. Schneirla* (A Series of Books in Psychology), Lester R. Aronson, Ethel Tobach, Daniel S. Lehman, and Jay S. Rosenblatt (eds), San Francisco, CA: W. H. Freeman, 17–52.
[^levy-2011]: Levy, Arnon, 2011, “Information in Biology: A Fictionalist Account”, *Noûs*, 45(4): 640–657. doi:10.1111/j.1468-0068.2010.00792.x
[^lewis-1969]: Lewis, David K., 1969, *Convention: A Philosophical Study*, Cambridge, MA: Harvard University Press.
[^lewontin-1974]: Lewontin, Richard, 1974, “Annotation: The Analysis of Variance and the Analysis of Causes”, *American Journal of Human Genetics*, 26(3): 400–411.
[^lewontin-2000]: –––, 2000, *The Triple Helix: Gene, Organism, and Environment*, Cambridge, MA: Harvard University Press.
[^macedonia-1993]: Macedonia, Joseph M. and Christopher S. Evans, 1993, “Essay on Contemporary Issues in Ethology: Variation among Mammalian Alarm Call Systems and the Problem of Meaning in Animal Signals”, *Ethology*, 93(3): 177–197. doi:10.1111/j.1439-0310.1993.tb00988.x
[^mann-2018]: Mann, Stephen Francis, 2018, “Attribution of Information in Animal Interaction”, *Biological Theory*, 13(3): 164–179. doi:10.1007/s13752-018-0299-5
[^mann-2020]: –––, 2020, “Consequences of a Functional Account of Information”, *Review of Philosophy and Psychology*, 11(3): 669–687. doi:10.1007/s13164-018-0413-4
[^martínez-2019]: Martínez, Manolo, 2019, “Representations Are Rate-Distortion Sweet Spots”, *Philosophy of Science*, 86(5): 1214–1226. doi:10.1086/705493
[^martínez-2016]: Martínez, Manolo and Peter Godfrey-Smith, 2016, “Common Interest and Signaling Games: A Dynamic Analysis”, *Philosophy of Science*, 83(3): 371–392. doi:10.1086/685743
[^meunier-2022]: Meunier, Robert, 2022 [2023], “Gene”, in *The Stanford Encyclopedia of Philosophy* (Fall 2023), Edward N. Zalta and Uri Nodelman (eds), URL = <[https://plato.stanford.edu/archives/fall2023/entries/gene/](https://plato.stanford.edu/archives/fall2023/entries/gene/)>.
[^maynard-2000]: Maynard Smith, John, 2000, “The Concept of Information in Biology”, *Philosophy of Science*, 67(2): 177–194. doi:10.1086/392768
[^maynard-2003]: Maynard Smith, John and David Harper, 2003, *Animal Signals* (Oxford Series in Ecology and Evolution), Oxford/New York: Oxford University Press. doi:10.1093/oso/9780198526841.001.0001
[^mcaninch-2009]: McAninch, Andrew, Grant Goodrich, and Colin Allen, 2009, “Animal Communication and Neo-Expressivism”, in *The Philosophy of Animal Minds*, Robert W. Lurz (ed.), Cambridge/New York: Cambridge University Press, 128–144. doi:10.1017/CBO9780511819001.008
[^mccowan-1999]: McCowan, Brenda, Sean F. Hanser, and Laurance R. Doyle, 1999, “Quantitative Tools for Comparing Animal Communication Systems: Information Theory Applied to Bottlenose Dolphin Whistle Repertoires”, *Animal Behaviour*, 57(2): 409–419. doi:10.1006/anbe.1998.1000
[^millikan-1984]: Millikan, Ruth Garrett, 1984, *Language, Thought, and Other Biological Categories: New Foundations for Realism*, Cambridge, MA: MIT Press.
[^millikan-1989]: –––, 1989, “In Defense of Proper Functions”, *Philosophy of Science*, 56(2): 288–302. doi:10.1086/289488
[^millikan-1995]: –––, 1995, “Pushmi-Pullyu Representations”, *Philosophical Perspectives*, 9: 185–200. doi:10.2307/2214217
[^millikan-2004]: –––, 2004, *Varieties of Meaning: The 2002 Jean Nicod Lectures*, Cambridge, MA: MIT Press.
[^monod-1970]: Monod, Jacques, 1970, *Le hasard et la nécessité: essai sur la philosophie naturelle de la biologie moderne*, Paris: Éditions du Seuil.
[^moss-1992]: Moss, Lenny, 1992, “A Kernel of Truth? On the Reality of the Genetic Program”, *PSA: Proceedings of the Biennial Meeting of the Philosophy of Science Association*, 1992(1): 335–348. doi:10.1086/psaprocbienmeetp.1992.1.192766
[^neander-1991]: Neander, Karen, 1991, “Functions as Selected Effects: The Conceptual Analyst’s Defense”, *Philosophy of Science*, 58(2): 168–184. doi:10.1086/289610
[^neander-2017]: –––, 2017, *A Mark of the Mental: In Defense of Informational Teleosemantics* (Life and Mind: Philosophical Issues in Biology and Psychology), Cambridge, MA: The MIT Press. doi:10.7551/mitpress/9780262036146.001.0001
[^o’connor-2014]: O’Connor, Cailin, 2014, “Evolving Perceptual Categories”, *Philosophy of Science*, 81(5): 840–851. doi:10.1086/677885
[^o’connor-2020]: –––, 2020, *Games in the Philosophy of Biology* (Cambridge Elements. Elements in the Philosophy of Biology), Cambridge/New York: Cambridge University Press. doi:10.1017/9781108616737
[^otte-1974]: Otte, Daniel, 1974, “Effects and Functions in the Evolution of Signaling Systems”, *Annual Review of Ecology and Systematics*, 5: 385–417. doi:10.1146/annurev.es.05.110174.002125
[^owren-2010]: Owren, Michael J., Drew Rendall, and Michael J. Ryan, 2010, “Redefining Animal Signaling: Influence versus Information in Communication”, *Biology & Philosophy*, 25(5): 755–780. doi:10.1007/s10539-010-9224-4
[^oyama-1985]: Oyama, Susan, 1985, *The Ontogeny of Information: Developmental Systems and Evolution*, Cambridge/New York: Cambridge University Press.
[^pfeifer-2006]: Pfeifer, Jessica, 2006, “The Use of Information Theory in Biology: Lessons from Social Insects”, *Biological Theory*, 1(3): 317–330. doi:10.1162/biot.2006.1.3.317
[^planer-2014]: Planer, Ronald J., 2014, “Replacement of the ‘Genetic Program’ Program”, *Biology & Philosophy*, 29(1): 33–53. doi:10.1007/s10539-013-9388-9
[^planer-2021]: Planer, Ronald J. and David Kalkman, 2021, “Arbitrary Signals and Cognitive Complexity”, *The British Journal for the Philosophy of Science*, 72(2): 563–586. doi:10.1093/bjps/axz018
[^pocheville-2018]: Pocheville, Arnaud, 2018, “Biological Information as Choice and Construction”, *Philosophy of Science*, 85(5): 1012–1025. doi:10.1086/699832
[^rendall-2013]: Rendall, Drew and Michael J. Owren, 2013, “Communication without Meaning or Information: Abandoning Language-Based and Informational Constructs in Animal Communication Theory”, in Stegmann 2013a: 151–188 (ch. 6). doi:10.1017/CBO9781139003551.010
[^rendall-2009]: Rendall, Drew, Michael J. Owren, and Michael J. Ryan, 2009, “What Do Animal Signals Mean?”, *Animal Behaviour*, 78(2): 233–240. doi:10.1016/j.anbehav.2009.06.007
[^ruxton-2011]: Ruxton, Graeme D. and H. Martin Schaefer, 2011, “Resolving Current Disagreements and Ambiguities in the Terminology of Animal Communication: Definitions in Animal Communication”, *Journal of Evolutionary Biology*, 24(12): 2574–2585. doi:10.1111/j.1420-9101.2011.02386.x
[^sarkar-1996]: Sarkar, Sahotra, 1996, “Biological Information: A Skeptical Look at Some Central Dogmas of Molecular Biology”, in *The Philosophy and History of Molecular Biology: New Perspectives* (Boston Studies in the Philosophy of Science 183), Sahotra Sarkar (ed.), Dordrecht/Boston: Kluwer Academic, 187–232.
[^sarkar-2000]: –––, 2000, “Information in Genetics and Developmental Biology: Comments on Maynard Smith”, *Philosophy of Science*, 67(2): 208–213. doi:10.1086/392771
[^sarkar-2013]: –––, 2013, “Information in Animal Communication: When and Why Does It Matter?1”, in Stegmann 2013a: 189–206 (ch. 7). doi:10.1017/CBO9781139003551.011
[^scarantino-2010]: Scarantino, Andrea, 2010, “Animal Communication between Information and Influence”, *Animal Behaviour*, 79(6): e1–e5. doi:10.1016/j.anbehav.2010.03.005
[^scarantino-2013]: –––, 2013, “Animal Communication as Information-Mediated Influence”, in Stegmann 2013a: 63–88 (ch. 2). doi:10.1017/CBO9781139003551.005
[^scarantino-2015]: –––, 2015, “Information as a Probabilistic Difference Maker”, *Australasian Journal of Philosophy*, 93(3): 419–443. doi:10.1080/00048402.2014.993665
[^schulte-2018]: Schulte, Peter, 2018, “Perceiving the World Outside: How to Solve the Distality Problem for Informational Teleosemantics”, *The Philosophical Quarterly*, 68(271): 349–369.
[^scott-2008]: Scott‐Phillips, Thomas C., 2008, “Defining Biological Communication”, *Journal of Evolutionary Biology*, 21(2): 387–395. doi:10.1111/j.1420-9101.2007.01497.x
[^scott-2010]: –––, 2010, “Animal Communication: Insights from Linguistic Pragmatics”, *Animal Behaviour*, 79(1): e1–e4. doi:10.1016/j.anbehav.2009.10.013
[^searcy-1992]: Searcy, William A., 1992, “Song Repertoire and Mate Choice in Birds”, *American Zoologist*, 32(1): 71–80. doi:10.1093/icb/32.1.71
[^searcy-2005]: Searcy, William A. and Stephen Nowicki, 2005, *The Evolution of Animal Communication: Reliability and Deception in Signaling Systems* (Monographs in Behavior and Ecology), Princeton, NJ: Princeton University Press. doi:10.1515/9781400835720
[^seyfarth-1980]: Seyfarth, Robert M., Dorothy L. Cheney, and Peter Marler, 1980, “Vervet Monkey Alarm Calls: Semantic Communication in a Free-Ranging Primate”, *Animal Behaviour*, 28(4): 1070–1094. doi:10.1016/S0003-3472(80)80097-2
[^seyfarth-2010]: Seyfarth, Robert M., Dorothy L. Cheney, Thore Bergman, Julia Fischer, Klaus Zuberbühler, and Kurt Hammerschmidt, 2010, “The Central Importance of Information in Studies of Animal Communication”, *Animal Behaviour*, 80(1): 3–8. doi:10.1016/j.anbehav.2010.04.012
[^shannon-1948]: Shannon, Claude E., 1948, “A Mathematical Theory of Communication”, *Bell System Technical Journal*, 27(3): 379–423. doi:10.1002/j.1538-7305.1948.tb01338.x
[^shea-2007]: Shea, Nicholas, 2007, “Representation in the Genome and in Other Inheritance Systems”, *Biology & Philosophy*, 22(3): 313–331. doi:10.1007/s10539-006-9046-6
[^shea-2011]: –––, 2011, “Developmental Systems Theory Formulated as a Claim about Inherited Representations”, *Philosophy of Science*, 78(1): 60–82. doi:10.1086/658110
[^shea-2018]: –––, 2018, *Representation in Cognitive Science*, Oxford University Press.
[^shea-2018-2]: Shea, Nicholas, Peter Godfrey-Smith, and Rosa Cao, 2018, “Content in Simple Signalling Systems”, *The British Journal for the Philosophy of Science*, 69(4): 1009–1035. doi:10.1093/bjps/axw036
[^skyrms-2009]: Skyrms, Brian, 2009, “Evolution of Signalling Systems with Multiple Senders and Receivers”, *Philosophical Transactions of the Royal Society B: Biological Sciences*, 364(1518): 771–779. doi:10.1098/rstb.2008.0258
[^skyrms-2010]: –––, 2010, *Signals: Evolution, Learning, and Information*, Oxford/New York: Oxford University Press. doi:10.1093/acprof:oso/9780199580828.001.0001
[^skyrms-2019]: Skyrms, Brian and Jeffrey A. Barrett, 2019, “Propositional Content in Signals”, *Studies in History and Philosophy of Science Part C: Studies in History and Philosophy of Biological and Biomedical Sciences*, 74: 34–39. doi:10.1016/j.shpsc.2019.01.005
[^smith-1977]: Smith, W. John, 1977, *The Behavior of Communicating: An Ethological Approach*, Cambridge, MA: Harvard University Press.
[^sprevak-2013]: Sprevak, Mark, 2013, “Fictionalism about Neural Representations”:, *The Monist*, 96(4): 539–560. doi:10.5840/monist201396425
[^stegmann-2004]: Stegmann, Ulrich E., 2004, “The Arbitrariness of the Genetic Code”, *Biology & Philosophy*, 19(2): 205–222. doi:10.1023/B:BIPH.0000024412.82219.a6
[^stegmann-2005]: –––, 2005, “Genetic Information as Instructional Content”, *Philosophy of Science*, 72(3): 425–443. doi:10.1086/498472
[^stegmann-2009]: –––, 2009, “A Consumer-Based Teleosemantics for Animal Signals”, *Philosophy of Science*, 76(5): 864–875. doi:10.1086/605820
[^stegmann-2012]: –––, 2012, “Varieties of Parity”, *Biology & Philosophy*, 27(6): 903–918. doi:10.1007/s10539-012-9331-5
[^stegmann-2013a]: ––– (ed.), 2013a, *Animal Communication Theory: Information and Influence*, Cambridge/New York: Cambridge University Press. doi:10.1017/CBO9781139003551
[^stegmann-2013b]: –––, 2013b, “Introduction: A Primer on Information and Influence in Animal Communication”, in Stegmann 2013a: 1–40. doi:10.1017/CBO9781139003551.002
[^stegmann-2014]: –––, 2014, “Causal Control and Genetic Causation”, *Noûs*, 48(3): 450–465. doi:10.1111/j.1468-0068.2012.00867.x
[^stegmann-2015]: –––, 2015, “Prospects for Probabilistic Theories of Natural Information”, *Erkenntnis*, 80(4): 869–893. doi:10.1007/s10670-014-9679-9
[^sterelny-2000]: Sterelny, Kim, 2000, “The ‘Genetic Program’ Program: A Commentary on Maynard Smith on Information in Biology”, *Philosophy of Science*, 67(2): 195–201. doi:10.1086/392769
[^sterelny-1996]: Sterelny, Kim, Kelly C. Smith, and Michael Dickison, 1996, “The Extended Replicator”, *Biology & Philosophy*, 11(3): 377–403. doi:10.1007/BF00128788
[^stotz-2017a]: Stotz, Karola and Paul E. Griffiths, 2017a, “Biological Information, Causality, and Specificity: An Intimate Relationship”, in *From Matter to Life: Information and Causality*, Sara Imari Walker, Paul C. W. Davies, and George F. R. Ellis (eds), Cambridge: Cambridge University Press, 366–390. doi:10.1017/9781316584200.015
[^stotz-2017b]: –––, 2017b, “Genetic, Epigenetic, and Exogenetic Information”, in *The Routledge Handbook of Evolution and Philosophy*, Richard Joyce (ed.), New York: Routledge, 106–119 (ch. 8).
[^predrag-2007]: Šustar, Predrag, 2007, “Crick’s Notion of Genetic Information and the ‘Central Dogma’ of Molecular Biology”, *The British Journal for the Philosophy of Science*, 58(1): 13–24. doi:10.1093/bjps/axl018
[^waters-2007]: Waters, C. Kenneth, 2007, “Causes That Make a Difference”, *The Journal of Philosophy*, 104(11): 551–579. doi:10.5840/jphil2007104111
[^weber-2006]: Weber, Marcel, 2006, “The Central Dogma as a Thesis of Causal Specificity”, *History and Philosophy of the Life Sciences*, 28(4): 595–609.
[^wheeler-2011]: Wheeler, Brandon C., William A. Searcy, Morten H. Christiansen, Michael C. Corballis, Julia Fischer, Christoph Grüter, Daniel Margoliash, Michael J. Owren, Tabitha Price, Robert Seyfarth, and Markus Wild, 2011, “Communication”, in *Animal Thinking: Contemporary Issues in Comparative Cognition* (Strüngmann Forum Reports), Randolf Menzel and Julia Fischer (eds), Cambridge: MA: The MIT Press, 187–206 (ch. 13). doi:10.7551/mitpress/9187.003.0018
[^williams-1992]: Williams, George C., 1992, *Natural Selection: Domains, Levels, and Challenges* (Oxford Series in Ecology and Evolution 4), New York: Oxford University Press. doi:10.1093/oso/9780195069327.001.0001
[^wilson-1962]: Wilson, Edward O., 1962, “Chemical Communication among Workers of the Fire Ant *Solenopsis saevissima* (Fr. Smith) 2. An Information Analysis of the Odour Trail”, *Animal Behaviour*, 10(1–2): 148–158. doi:10.1016/0003-3472(62)90142-2
[^zahavi-1975]: Zahavi, Amotz, 1975, “Mate Selection—A Selection for a Handicap”, *Journal of Theoretical Biology*, 53(1): 205–214. doi:10.1016/0022-5193(75)90111-3

## 学术工具

* [如何引用本词条](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=information-biological)。
* [预览本词条的 PDF 版本](https://leibniz.stanford.edu/friends/preview/information-biological/)，见 [SEP 学会之友](https://leibniz.stanford.edu/friends/)。
* 在 [InPhO](https://www.inphoproject.org/entity?sep=information-biological&redirect=True) 查找与本词条相关的话题与思想家。
* 在 [PhilPapers](https://philpapers.org/sep/information-biological/) 查看本词条的增强文献目录及其数据库链接。

## 其他网络资源

- Godfrey-Smith, Peter and Kim Sterelny, “Biological Information”, *Stanford Encyclopedia of Philosophy* (Summer 2024 Edition), Edward N. Zalta & Uri Nodelman (eds.), URL = <[https://plato.stanford.edu/archives/sum2024/entries/information-biological/](https://plato.stanford.edu/archives/sum2024/entries/information-biological/)>. [This was the previous entry on this topic in the *Stanford Encyclopedia of Philosophy* – see the [version history](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=information-biological).]

## 相关词条

动物认知 | 演化博弈论 | 基因 | genetics: genotype/phenotype distinction | 分子遗传学 | 信息 | 语义概念的信息 | 心理内容的目的论 | 心理表征 | 生物学中的目的论观念

**（译注：相关词条的中文站内链接将由管线在对应词条重译完成后统一挂接。）**
