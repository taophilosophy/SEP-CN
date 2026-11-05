# 隐私与信息技术 privacy and information technology (Jeroen van den Hoven, Martijn Blaauw, Wolter Pieters, and Martijn Warnier)

*首次发表于 2014 年 11 月 20 日；2024 年 10 月 4 日实质修订。*

人类珍视自己的隐私以及对个人生活领域的保护。他们珍视一定程度的控制权，即由谁掌握关于他们的何种信息。他们当然不希望自己的个人信息随时随地被任何人获取。但信息技术的最新进展威胁着隐私，削弱了对个人数据的控制，并因个人数据被获取而带来一系列负面后果的可能性。20 世纪下半叶，作为对个人数据处理水平不断提高的回应，各国建立了数据保护制度。21 世纪已成为大数据与先进信息技术（例如深度学习与生成式 AI 的各种形式）、大型科技公司兴起与平台经济的世纪，随之而来的是 EB（艾字节）级数据的存储与处理。

爱德华·斯诺登的爆料，以及更近的剑桥分析案（Cadwalladr & Graham-Harrison 2018）[^cadwalladr-2018]，表明对负面后果的担忧是真实存在的。收集、存储和检索大量关于电话交谈、互联网搜索和电子支付的数据的技术能力如今已经就位，并被政府机构与企业行为者同样例行使用。中国的崛起，以及先进数字技术用于监控与控制在规模和传播上的大规模使用，只加剧了许多人的担忧。对企业而言，关于客户和潜在客户的个人数据如今也是一项关键资产。大型科技公司（谷歌、亚马逊、脸书、微软、苹果）以个人数据为中心的商业模式的规模和目的，已由肖莎娜·祖博夫（Shoshana Zuboff，2019）以“监控资本主义”（surveillance capitalism）为标签作了详细描述。

与此同时，隐私的含义与价值仍是相当有争议的主题。新技术日益增强的力量，加上对隐私日益模糊与缺乏共识，引发了涉及法律、政策与伦理的问题。这些概念性争论与问题，有许多都处在对《通用数据保护条例》（GDPR）的解释与分析语境中——该条例于 2018 年春季由欧盟通过，是欧盟 1995 年指令的继任者，其适用远超欧盟边界之外。

本文的重点是探讨信息技术与隐私之间的关系。我们将既说明信息技术及其创新对隐私构成的具体威胁，也指出信息技术 **本身** 如何能够通过以可称为“隐私敏感”、“隐私增强”或“尊重隐私”的方式发展来克服这些隐私担忧。我们还将讨论新兴技术在这场辩论中的作用，并说明道德辩论本身如何受到信息技术的影响。

## 1 隐私的概念与隐私的价值

关于隐私的讨论与技术的使用交织在一起。在西方世界开启隐私辩论的那篇出版物，是由报纸印刷机和摄影术的引入所引发的。塞缪尔·沃伦（Samuel D. Warren）与路易斯·布兰代斯（Louis Brandeis）在《哈佛法律评论》上撰文讨论隐私（Warren & Brandeis 1890）[^warren-1890]，部分是为了抗议当时记者的侵扰活动。他们主张，基于“不可侵犯的人格”（inviolate personality）原则，存在一种“独处的权利”（right to be left alone）。自那篇文章发表以来，关于隐私的辩论一直由两类主张所推动：一类是个人有权决定他人可在多大程度上接触自己的主张（Westin 1967）[^westin-1967]，另一类是社会有权了解个人的主张。由于信息是接触个人的基石，隐私辩论与信息技术的发展共同演化——并且是对信息技术发展的回应。因此，很难把隐私概念和数据保护讨论，与计算机、互联网、移动计算以及这些基础技术的众多应用的发展方式分离开来。

### 1.1 宪法性隐私与信息性隐私

受美国法律后续发展的启发，可以区分出（1）宪法性（或决断性）隐私与（2）侵权法上的（或信息性）隐私（DeCew 1997）[^decew-1997]。前者指在那些被视为私密与个人的事务（例如使用避孕药具或堕胎的决定）上，不受他人干涉地自行作出决定的自由。后者关涉个人对他人接触关于自身的信息行使控制的利益，通常被称为“信息性隐私”。这里不妨想一想在脸书或其他社交媒体上披露的信息。这类信息很容易超出个人的控制。

关于隐私的陈述可以是描述性的，也可以是规范性的，取决于它们是用来描述人们如何界定隐私的情境与条件以及他们如何评价这些情境与条件，还是用来表明对信息的使用或信息处理应当有所约束。这些条件或约束通常涉及关于个人的个人信息，或可能影响个人的信息处理方式。规范性意义上的信息性隐私，通常指个人拥有对以下诸项接触的直接或间接控制的、非绝对的道德权利：（1）关于自身的信息；（2）他人可能获取关于自身信息的情境；（3）可用于生成、处理或传播关于自身信息的技术。

### 1.2 关于隐私价值的诸种说明

关于隐私的辩论几乎总是围绕着新技术展开，从遗传学和对生物标志物的广泛研究、脑成像、无人机、可穿戴传感器与传感器网络、社交媒体、智能手机、闭路电视，到政府的网络安全计划、直接营销、RFID 标签、大数据、头戴式显示器和搜索引擎。面对新技术的洪流及其对个人信息与隐私的影响，基本上有两种反应：第一种反应，为 IT 行业和研发部门中的许多人所持有，认为在数字时代我们毫无隐私，也没有办法保护它，所以我们应该适应新世界并放下此事（Sprenger 1999）[^sprenger-1999]。另一种反应是，我们的隐私比以往任何时候都更重要，我们能够而且必须努力保护它。

在关于隐私的文献中，关于隐私的性质与价值有许多相互竞争的说明（Negley 1966; Rössler 2005）[^negley-1966][^rössler-2005]。在光谱的一端，**还原论** 说明主张，隐私主张实际上是关于其他价值和其他从道德角度看重要的事物的。根据这些观点，隐私的价值可还原为这些其他价值或价值来源（Thomson 1975）[^thomson-1975]。沿着这些思路得到辩护的提议提到了财产权、安全、自主、亲密或友谊、民主、自由、尊严，或效用与经济价值。还原论说明认为，隐私的重要性应当用那些其他价值与价值来源来解释，其含义也应当据此澄清（Westin 1967）[^westin-1967]。相反的观点则认为，隐私本身就有价值，其价值与重要性并非派生自其他考量（关于讨论见 Rössler 2004）[^rössler-2004]。把隐私与个人生活领域理解为一种人权的观点，就是这种非还原论概念的一个例子。

更晚近，一种与新的信息技术相关的隐私说明被提出，它承认对隐私的诉求背后有一簇相互关联的道德主张，但坚持认为并不存在一个单一的、本质性的隐私关注核心。这种方法被称为簇式说明（cluster accounts）（DeCew 1997; Solove 2006; van den Hoven 1999; Allen 2011; Nissenbaum 2004）[^allen-2011][^decew-1997][^hoven-1999][^nissenbaum-2004][^solove-2006]。

在关于自由的新共和主义概念的基础上，已经发展出新的隐私说明。它们处理 21 世纪监控资本主义的主要行动者对“基于数据”的权力的积累，以及国家行动者以数据驱动的监控所造成的问题，其灵感来自菲利普·佩蒂特（Philip Pettit）关于作为非支配（non-domination）的自由的说明（Pettit 2001）[^pettit-2001]。这些新共和主义说明解释了为什么当各方拥有关于个人的海量信息时，个人会感到脆弱——即使这些信息并没有以对个人的消极自由或积极自由产生负面影响的方式被利用。接触个人数据构成了对数据主体行使专断权力的基础。一位好主人的奴隶在某个时间点上可能没有什么可抱怨的，但他知道事情可能变化，一旦主人决定如此。数据保护使个人免受数据驱动的支配和专断权力的使用。关于这种说明见（Roberts 2015）[^roberts-2015]，关于国家监控的新共和主义说明见（Smith 2020）[^smith-2020]。

从描述性视角看，近期对隐私说明谱系的进一步补充是认识论说明，其中隐私概念主要从知识或其他认识论状态的角度来分析。拥有隐私意味着他人不知道某些私人命题；缺乏隐私意味着他人确实知道某些私人命题（Blaauw 2013）[^blaauw-2013]。这种“拥有隐私”概念的一个重要方面是，它被视为一种关系（Rubel 2011; Matheson 2007; Blaauw 2013）[^blaauw-2013][^matheson-2007][^rubel-2011]，具有三个论元位置：一个主体（*S*）、一组命题（*P*）和一组个人（*I*）。这里 *S* 是拥有（某种程度的）隐私的主体。*P* 由主体希望保持私密的那些命题构成（把这一组中的命题称为“私人命题”），而 *I* 由相对于其而言 *S* 希望使这些私人命题保持私密的那些个人构成。

另一个有用的区分是欧洲路径与美国路径之间的区分。一项文献计量研究（Heersmink et al. 2011）[^heersmink-2011]表明，这两种路径在文献中是彼此分离的。第一种路径以“数据保护”来概念化信息性隐私问题，第二种以“隐私”来概念化。在讨论隐私问题与技术的关系时，数据保护概念最为有用，因为它对保护的对象是什么以及通过哪些技术手段可以保护数据，给出了一个相对清晰的概念图景。同时，它也引出“为何应当保护数据”这一问题的答案，指向若干独特的道德理由与根据，基于这些理由与根据，对个人数据的技术性、法律性和制度性保护可以得到辩护。信息性隐私因此被重新表述为对个人数据的保护（van den Hoven 2008）[^hoven-2008]。这种说明展示了隐私、技术与数据保护如何相互关联，而又不把隐私与数据保护混为一谈。

### 1.3 个人数据

个人信息或数据，是指与个别个人相关联或可与其相关联的信息或数据。例子包括明确陈述的特征，如个人的出生日期、性偏好、行踪、宗教信仰，也包括你计算机的 IP 地址或与这类信息相关的元数据。此外，个人数据也可以是更隐晦的形式，例如来自社交媒体的、可与个人相关联的行为数据。个人数据可以与因其他原因被视为敏感、珍贵或重要的数据相对照，如秘方、金融数据或军事情报。用于保护其他信息的数据（如密码）在此不予考虑。尽管这类安全措施（密码）可能有助于隐私，但它们的保护只是对保护其他（更私密的）信息起工具性作用，因此这类安全措施的质量不在我们这里的考虑范围之内。

在哲学语义学中，有一个相关区分，即描述性标签对个人的指称性（referential）使用与归属性（attributive）使用之间的区分（van den Hoven 2008）[^hoven-2008]。法律上把个人数据定义为可与自然人相关联的数据。这种关联可以有两种方式：指称性模式和非指称性模式。法律主要关注描述或属性的“指称性使用”，即基于说话者与认识对象之间（可能的）相识关系的那种使用。“肯尼迪的凶手必定是疯子”——在法庭上指着他说的这句话——就是一个指称性使用描述的例证。这可以与归属性使用的描述相对照，如“肯尼迪的凶手必定是疯子，无论他是谁”。在后一种情形中，描述的使用者并不——而且可能永远不会——认识他正在谈论或打算指涉的人。如果法律对个人数据的定义作指称性解释，那么许多在某个时间点可能被用于个人的数据将不受保护；也就是说，对这些数据的处理不会因与隐私或个人生活领域相关的道德理由而受到约束，因为它并不以一种直接的方式“指涉”个人，因此不构成严格意义上的“个人数据”。

### 1.4 保护个人数据的道德理由

可以区分出以下类型保护个人数据、以及为他人接触这些数据提供直接或间接控制的道德理由（van den Hoven 2008）[^hoven-2008]：

1. 防止伤害：他人对个人银行账户、个人资料、社交媒体账户、云存储库、特征和行踪的不受限制的接触，可以以多种方式被用于伤害数据主体。
2. 信息不平等：个人数据已成为市场上具有经济价值的商品。个人通常不处于就自身数据的使用订立合同的有利地位，也没有手段去核查交易伙伴是否遵守合同条款。数据保护法律、规制与治理旨在为起草关于个人数据传输与交换的合同确立公平条件，并为数据主体提供制衡、救济保障以及监督合同条款遵守情况的手段。灵活定价、价格定向与价格欺诈、动态谈判，通常是在信息不对称和接触信息的巨大差距的基础上进行的。此外，营销中的选择建模、政治竞选中的微定向、政策执行中的助推，都利用了委托人与代理人之间基本的信息不平等。
3. 信息不义与歧视：在一个领域或语境（例如医疗保健）中提供的个人信息，在另一个领域或语境（如商业交易）中使用时可能改变其含义，并可能导致对个人的歧视与不利。这与尼森鲍姆（Nissenbaum，2004）关于语境完整性的讨论，以及范登霍芬（van den Hoven，2008）与纳根博格（Nagenborg，2009）关于沃尔泽式正义领域（Walzerian spheres of justice）的讨论相关。
4. 侵蚀道德自主与人的尊严：缺乏隐私可能使个人暴露于影响其选择的外部力量，并使其作出本来不会作出的决定。大规模监控导致这样一种局面：个人因为知道他人正在看着他们，而惯常地、系统性地、持续地作出选择与决定。这影响了他们作为自主存在者的地位，并对他们和社会产生有时被称为“寒蝉效应”（chilling effect）的影响。与之密切相关的，是对尊重个人与人的尊严之侵犯的考量。与个人身份相关的数据的大量积累（例如脑机接口、身份图谱、数字分身或数字孪生、对个人社交网络拓扑的分析）可能使人产生这样的观念：由于关于某个人的信息如此之多，我们因而认识这个人。可以论证，能够基于个人的大数据来把这个人弄清楚，构成一种认识论上和道德上的不谦逊（Bruynseels & van den Hoven 2015）[^bruynseels-2015][^hoven-2015]，它未能尊重这一事实：人是具有私人心理状态的主体，这些心理状态具有某种从外部视角（第三人或第二人视角）无法企及的性质——无论这种外部视角多么详尽和准确。尊重隐私因此将意味着承认人的这种道德现象学，即承认一个人永远比先进数字技术所能揭示的更多。

这些考量都为限制和约束对个人数据的接触、并为个人提供对其数据的控制提供了充分的道德理由。

### 1.5 法律、规制与对接触的间接控制

承认保护个人数据存在道德理由之后，几乎所有国家都施行了数据保护法律。这些法律背后的基本道德原则，是数据主体对处理的知情同意要求，它（至少在原则上）为主体提供对上述潜在负面影响的控制。此外，处理个人信息要求明确其目的、限制其使用、告知个人并允许其纠正不准确之处，数据的持有者对监督机构负责（OECD 1980）[^oecd-1980]。由于不可能以传统方式保证所有这些领域和应用中所有类型的数据处理都遵守这些规则与法律，所谓的“隐私增强技术”（PETs）和身份管理系统在许多情形中被期待取代人工监督。21 世纪在隐私方面的挑战，是确保技术被设计成把隐私要求纳入软件、架构、基础设施和工作流程，从而使隐私侵犯不太可能发生。新一代隐私法规（以欧盟的核心 GDPR 为代表）如今通常要求“设计即隐私”（privacy by design）的进路。《通用数据保护条例》第 25 条明确说明“设计”（by design）与“默认”（by default）是强制性的。数据生态系统与社会技术系统、供应链、组织（包括激励结构、业务流程、技术硬件与软件、人员培训）都应被设计成使隐私侵犯发生的可能性尽可能低。关于设计即隐私的责任之讨论，见（Colonna 2022）[^colonna-2022]。

## 2 信息技术对隐私的影响

关于隐私的辩论几乎总是围绕着新技术展开，从遗传学和对生物标志物的广泛研究、脑成像、无人机、可穿戴传感器与传感器网络、社交媒体、智能手机、闭路电视，到政府的网络安全计划、直接营销、监控、RFID 标签、大数据、头戴式显示器和搜索引擎。本节讨论其中一些新技术的影响，特别聚焦于信息技术。

### 2.1 信息技术的发展

“信息技术”指用于存储、处理和分发信息的自动化系统。通常这涉及计算机和通信网络的使用。信息系统中可存储或处理的信息量取决于所使用的技术。过去几十年，技术容量依据摩尔定律迅速增长。这适用于存储容量、处理能力和通信带宽。我们现在能够存储和处理 EB 级的数据。举例来说，要把 100 EB 的数据存储在 720 MB 的 CD-ROM 光盘上，需要几乎触及月球的一摞光盘。

这些发展从根本上改变了我们处理信息和提供信息的实践。迅速的变化增加了审慎考虑效果之可取性的需要。有些人甚至谈到数字革命作为一次类似工业革命的技术飞跃，或数字革命作为一场类似哥白尼、达尔文和弗洛伊德革命的、对人性与世界的理解上的革命（Floridi 2008）[^floridi-2008]。无论在技术意义上还是在认识论意义上，人们都强调连接性与互动性。物理空间变得不那么重要，信息无处不在，社会关系也随之调整。

既然我们已从对接触和/或使用个人信息施加约束的道德理由的角度描述了隐私，那么信息技术所施加的日益增加的连接性就引发了许多问题。在描述意义上，接触增加了；在规范意义上，这要求考虑这一发展的可取性，并评估由技术（Lessig 1999）[^lessig-1999]、制度和/或法律实施规制的潜力。

随着连接性增加对信息的接触，它也为行动者根据新的信息来源采取 **行动** 增加了可能性。当这些来源包含个人信息时，伤害、不平等、歧视和自主丧失的风险很容易出现。例如，你的敌人可能更容易查明你在哪里，用户在在线环境中可能被诱惑以感知到的益处换取隐私，雇主可能利用在线信息来避免雇用某些群体的人。此外，可能是系统而非用户决定显示哪些信息，从而只让用户看到与其个人资料匹配的新闻。虽然严格意义上的个人数据并非在所有画像、推荐和过滤情形中都被用于各种实践和商业目的，但只要能够获得稳定而稳健的用户画像，就足以在一段时间内针对个体用户，而不论该用户是谁。

虽然技术在设备层面运行，但信息技术由一套复杂的社会技术实践系统构成，其使用语境构成讨论它在改变接触信息可能性方面的作用、从而影响隐私的基础。我们将在以下各节讨论一些具体发展及其影响。

### 2.2 互联网

互联网最初在 1960 年代构想、在 1980 年代作为交换信息的科学网络发展起来，其设计目的并非为了分离信息流（Michener 1999）[^michener-1999]。当时并未预见今天的万维网，也未预见互联网被滥用的可能性。社交网站是为在现实生活中相识的人群内部使用而出现的——起初大多在学术环境中——而不是为全球用户社群而发展的（Ellison 2007）[^ellison-2007]。人们曾假设与密友分享不会造成任何伤害，隐私与安全只有在网络扩大时才进入议程。这意味着隐私关注往往不得不作为附加物而非设计内建（by-design）来处理。

互联网隐私讨论的一个主要主题围绕 cookie 的使用（Palmer 2005）[^palmer-2005]。Cookie 是网站存储在用户计算机上的小段数据，目的是实现网站的个性化。然而，有些 cookie 可被用于跨多个网站追踪用户（追踪 cookie），例如使用户最近在一个完全不同的网站上查看过的产品得以做广告。同样，所生成信息的用途并不总是清楚。要求用户同意使用 cookie 的法律在提高控制水平方面并不总是成功，因为同意请求干扰了任务流程，用户可能只是点掉任何同意请求（Leenes & Kosta 2015）[^leenes-2015]。同样，嵌入在其他网站中的社交网站功能（如“点赞”按钮）可能使社交网站识别用户访问过的网站（Krishnamurthy & Wills 2009）[^krishnamurthy-2009]。

云计算加剧了许多隐私担忧（Ruiter & Warnier 2011; Hassan et al. 2022）[^hassan-2022][^ruiter-2011]。以前，虽然信息可从网络上获得，但用户数据和程序仍存储在本地，从而防止程序供应商接触数据和使用的统计数据。在云计算中，数据和程序都在线上（在云中），用户生成的数据和系统生成的数据用于什么并不总是清楚。此外，由于数据位于世界其他地方，甚至并不总是清楚适用哪部法律、哪些机构可以要求接触数据。在线服务和应用程序（如搜索引擎和游戏）收集的数据在此尤其令人担忧。应用程序使用和传送哪些数据（浏览历史、联系人列表等）并不总是清楚，即使清楚，用户可用的唯一选择也可能是不使用该应用。这也适用于基础模型和大型语言模型（如 ChatGPT）的使用。这些模型的使用已在若干国家被禁止或因隐私理由而受到严格限制，因为无法排除个人数据正被以违反适用数据保护规范的方式使用（见下文讨论）。

互联网隐私的一些特殊特征（社交媒体和大数据）将在以下各节讨论。

### 2.3 社交媒体

社交媒体带来额外的挑战。问题不仅涉及限制接触信息的道德理由，也涉及限制 **邀请** 用户提交各种个人信息的道德理由。社交网站邀请用户生成更多数据，以提高网站的价值（“你的个人资料已完成……%”）。用户被 **诱惑** 用个人数据交换使用服务的益处，并把这些数据和他们的注意力作为服务的支付。此外，用户甚至可能没有意识到他们被诱惑提供什么信息，如前述其他网站上“点赞”按钮的情形。仅仅限制对个人信息的接触并不能公正处理这里的问题，更根本的问题在于引导用户的分享行为。当服务免费时，数据是作为一种支付形式而被需要的。

限制用户分享诱惑的一种方式是要求默认隐私设置严格。即便如此，这也限制了其他用户（“朋友的朋友”）的接触，但并不限制服务提供者的接触。此外，这类限制降低了社交网站本身的价值和可用性，并可能减少这类服务的积极效果。隐私友好默认设置的一个具体例子是选择加入（opt-in）而非选择退出（opt-out）的进路。当用户必须采取明确行动来分享数据或订阅服务或邮件列表时，所产生的效果对用户而言可能更可接受。然而，很多仍取决于这一选择如何被框定（Bellman, Johnson, & Lohse 2001）。

### 2.4 人工智能与大数据

近年来人工智能（AI）的迅速出现与成熟，对用户的隐私构成严重威胁。更快更大的计算基础设施，连同越来越大的数据集——即所谓的“大数据”——推动了人工智能技术的迅速采用。这使得以迄今未见过的规模监控和画像用户成为可能（Zuboff 2019）[^zuboff-2019]。

用户在在线时生成大量（元）数据。这不仅包括用户明确输入的数据，还包括元数据，如用户行为的统计数据：访问过的网站、点击过的链接、输入的搜索词等。数据挖掘可被用于从这类数据中提取模式，随后用于生成特定的用户画像。这类用户画像为数据挖掘公司所珍视。生成的用户画像可用于定向广告，也可用于例如识别用户是否为政治或其他社会群体的成员。这些可能只影响在线体验（所显示的广告），但取决于哪些方接触信息，它们也可能在完全不同的语境中影响用户。特别是，大数据和人工智能技术可用于对用户画像（Hildebrandt 2008）[^hildebrandt-2008][^hildebrandt-2008-2]，生成用户属性典型组合的模式，随后可用于预测兴趣和行为。一个无辜的应用是“你可能还喜欢……”，但取决于可用的数据，可能作出更敏感的推导，如最可能的宗教或性偏好。这些推导随后又可能导致不平等待遇或歧视。当一个用户可以被归入某个特定群体，哪怕只是概率性地，这可能影响他人采取的行动（Taylor, Floridi, & Van der Sloot 2017）。例如，画像可能导致拒绝保险或信用卡，此时利润是歧视的主要原因。当这类决定基于画像时，可能难以质疑它们，甚至难以找出其背后的解释。画像也可能被组织或可能的未来政府用于其政治议程上对特定群体的歧视，以寻找目标并拒绝他们接触服务，或更糟。

大数据不仅仅产生于互联网交易。同样，数据也可能在购物时、在公共场所或私人空间的监控摄像头记录时（得益于更好的人工智能驱动计算机视觉技术，见 Curzon et al. 2021）[^curzon-2021]、或在使用基于智能卡的公共交通支付系统时被收集。所有这些数据都可用于为公民画像，并基于这类画像作出决定。例如，购物数据可用于向特定个人发送关于健康饮食习惯的信息，但同样也可用于保险决定。根据欧盟数据保护法（GDPR），处理个人数据需要数据主体的许可（通常是“知情同意”）（或基于现行法律明确规定的理由的正当化），而且这些数据只能为其被收集的目的而处理。因此，具体挑战是（a）当用户没有明确参与交易时（如监控情形）如何获得许可，以及（b）如何防止“功能蔓延”（function creep），即数据在收集后被用于不同目的（例如 DNA 数据库可能发生的情形（Dahl & Sætnan 2009）[^dahl-2009]）。

一个特别的担忧可能来自遗传学和基因组数据（Tavani 2004, Bruynseels & van den Hoven, 2015）[^tavani-2004]。与其他数据一样，基因组学可用于作出预测，尤其可预测疾病风险。除了他人接触详细用户画像的问题之外，这里的一个根本问题是个人是否应该知道关于她自己的已知情况。一般而言，可以说用户有权接触存储的关于他们的任何信息，但在这种情形下，也可能尤其存在一种不知的权利，即当对数据的了解（如疾病风险）会降低福祉时（例如因引起恐惧而没有带来治疗）。就前面的例子而言，人们可能也不想知道自己购物行为的模式。

近来，大型语言模型（如 ChatGPT（OpenAI，其他网络资源））已变得非常流行。这类模型借助通过互联网抓取生成的大规模数据集（Germain 2023 [其他网络资源]）以及其他数据集训练而成。这些 AI 模型的确切隐私风险在很大程度上仍属未知，但存在风险，例如泄漏（可能涉及隐私敏感的）训练数据（Inan et al. 2021 [其他网络资源]）。总体而言，人工智能领域仍在快速发展，尚不清楚这将如何影响最终用户的隐私。旨在应对 AI 技术的立法仍处于制定过程中，尚未在实践中经受检验（Hill 2023）[^hill-2023]。可解释 AI（Došilović 2018; Angelov 2021）[^angelov-2021][^došilović-2018]似乎是控制 AI 技术所出现的一个核心机制，尽管如果不谨慎使用，这些机制本身也带来风险（de Bruijn, Warnier & Janssen 2022）。

### 2.5 移动设备

随着用户越来越多地拥有智能手机等联网设备，移动设备收集和发送的数据越来越多。这些设备通常包含一系列产生数据的传感器，包括 GPS（定位）、运动传感器和摄像头，并可能通过互联网或其他网络传输所产生的数据。一个特别的例子涉及位置数据。许多移动设备有记录用户位置的 GPS 传感器，但即使没有 GPS 传感器，也可以推导出近似位置，例如通过监测可用的无线网络。由于位置数据把在线世界与用户的物理环境联系起来，并可能造成身体伤害（跟踪、假期入室盗窃等），这类数据通常被视为特别敏感。

这些设备中有许多也包含摄像头，当应用程序可以访问时，可用于拍照。这些也可被视为传感器，它们生成的数据可能特别私密。对于摄像头这类传感器，人们假定用户知道它们何时被激活，隐私取决于这种知晓。对于网络摄像头，通常有指示灯指示摄像头是否开启，但这个灯可能被恶意软件操纵。一般而言，处理个人数据的“可重构技术”（Dechesne, Warnier & van den Hoven 2011）引发了用户对配置的知晓问题。

### 2.6 物联网

连接到互联网的设备不限于智能手机等用户拥有的计算设备。许多设备包含芯片和/或连接到所谓的物联网。RFID（射频识别）芯片可在有限距离内被读取，因此你可以把它举在阅读器前，而不必插入。欧盟和美国的护照带有保护生物识别数据的 RFID 芯片，但在尝试读取这类设备时，像用户国籍这样的信息可能轻易泄漏（见 Richter, Mostowski & Poll 2008 [其他网络资源]）。“智能”RFID 也嵌入公共交通支付系统。“哑”RFID（基本只包含一个数字）出现在多种产品中，作为条形码的替代，并用于物流。尽管如此，一旦知道某人携带含芯片的物品，这类芯片就仍可用于追踪这个人。

在家庭中，有自动读取和发送电力和水消耗的智能电表，以及可由所有者远程控制的恒温器和其他设备。这类设备同样生成统计数据，可用于挖掘和画像。将来，越来越多的家用电器将被连接，每件都生成自己的信息。环境智能（Brey 2005）[^brey-2005]和普适计算，连同物联网（Friedewald & Raabe 2011）[^friedewald-2011]，也使得基于明确偏好和隐含观察而自动使环境适应用户成为可能，而用户自主是考虑这类设备隐私意涵时的中心主题。总体而言，转向以服务为导向的商品供给，供应商通过 IT 和相关连接性获知产品如何使用，要求考虑相关的隐私与透明度问题（Pieters 2013）[^pieters-2013]。例如，当连接的设备包含麦克风时需要告知用户，以及它如何和何时被使用。

### 2.7 电子政务

政府和公共行政也因先进 IT 系统的可用性而经历了彻底的变革。这些变化的例子包括生物识别护照、在线电子政务服务、投票系统、各种在线公民参与工具和平台，或在线访问议会和政府委员会会议的录音。

考虑选举投票的情形。信息技术可能在投票过程的不同阶段发挥作用，对选民隐私产生不同影响。大多数国家要求选举须以无记名投票方式举行，以防止贿选和胁迫。在这种情形下，选民被假定应保密其投票，**即使她想要公开它**。对于用于投票的信息技术，这被定义为无收据性或抗胁迫的要求（Delaune, Kremer & Ryan 2006）。在投票站，当局确保选民保密投票，但邮寄或在线投票时这种监控不可能实现，甚至无法通过技术手段强制执行，因为总有人在选民投票时看着。在这种情形下，隐私不仅是权利，也是义务，而信息技术的发展在选民履行这一义务的可能性，以及当局核实这一点（的能力）方面，发挥着重要作用。更广泛地说，电子民主倡议可能改变隐私在政治进程中被看待的方式。

更一般而言，隐私在民主中对于防止不当影响很重要。虽然投票过程中缺乏隐私可能导致贿选和胁迫，但也有更微妙的方式影响民主进程，例如通过定向的（错误）信息运动。公民在线上的（政治）活动（如社交媒体上）由于可通过行为画像定向而便利了这类尝试。与线下政治活动相比，隐藏偏好和活动更加困难，保密被违反的可能性更大，影响舆论的尝试变得更可扩展。

### 2.8 监控

信息技术被用于各种监控任务。它可用于增强和扩展传统监控系统，如闭路电视和其他摄像系统，例如使用人脸识别技术在人群中识别特定个人，或监控特定地点的不受欢迎行为。这类方法与其他技术（如监控物联网设备）结合时变得更加强大（Motlagh et al. 2017）[^motlagh-2017]。

除了增强现有监控系统，ICT 技术如今主要用于数字领域，通常统称为“监控资本主义”（Zuboff 2019）[^zuboff-2019]。如前面第 2.4 节所述，社交媒体和其他在线系统被用于收集关于个人的大量数据——或是“自愿”的，因为用户订阅特定服务（谷歌、脸书），或是以不那么透明的方式收集各种用户相关数据而不自愿。随后用数据分析和机器学习技术生成个体用户的预测模型，这些模型可用于例如定向广告，也可用于更恶意的意图，如欺诈或影响选举的微定向（Albright 2016 [其他网络资源]）或英国脱欧等公投（Cadwalladr 2019, 其他网络资源）。政府和营利公司之间围绕涉及敏感数据的大型数据计划的联系，总体而言增加了对隐私的威胁。

除了私营部门的监控产业，政府构成另一个大规模使用监控技术的传统群体，无论是通过情报机构还是执法部门。这类监控系统通常以诉诸“更大的善”和保护公民来正当化，但其使用也有争议。对于这类系统，人们通常希望确保对隐私的任何负面影响与技术所带来的益处成比例。尤其由于这类系统通常笼罩在秘密之中，外人难以看出这类系统是否被按比例使用，或是否确实对其任务有用（Lawner 2002）[^lawner-2002]。当政府为监控目的使用私营部门数据或服务时，这一点尤为紧迫（Campbell 2023 [其他网络资源]）。

通信系统中几乎普遍使用良好的加密技术，也使得收集有效监控信息更加困难，导致越来越多地呼吁在通信系统中设置仅供政府使用的“后门”（back doors）。从隐私立场看，这可能被评价为不受欢迎的，不仅因为它使政府接触私人对话，也因为它降低了采用这一技术的通信系统的整体安全性（Abelson et al. 2015）[^abelson-2015]。

## 3 信息技术本身如何能解决隐私问题？

虽然信息技术通常被视为隐私问题的 **原因**，但也有几种方式信息技术可以帮助解决这些问题。有可用于设计隐私保护系统的规则、指导方针或最佳实践。这类可能性从有伦理依据的设计方法论，到使用加密保护个人信息免受未经授权的使用。特别是，来自信息安全领域、旨在保护信息免受未经授权访问的方法，可以在保护个人数据方面发挥关键作用。

### 3.1 设计方法

价值敏感设计提供了一种“在设计全过程中以有原则且全面的方式考虑人类价值的、有理论依据的技术设计进路”（Friedman et al. 2006）[^friedman-2006]。它提供了一套规则和指导方针，用于怀着特定价值来设计系统。这样一种价值可以是“隐私”，因此价值敏感设计可用作设计隐私友好 IT 系统的方法（van den Hoven et al. 2015）[^hoven-2015]。卡沃基安（Cavoukian，2009）等人倡导的“设计即隐私”进路，可被视为特别聚焦于隐私的价值敏感设计进路之一（Warnier et al. 2015）[^warnier-2015]。更晚近，“隐私工程”（privacy engineering）这类进路（Ceross & Simpson 2018）[^ceross-2018]通过旨在提供一套更实用、可部署的方法以实现系统范围的隐私，扩展了设计即隐私进路。

设计即隐私进路以原则的形式为设计隐私保护系统提供高层指导方针。这些原则的核心是“数据保护需要以主动而非被动的方式看待，使设计即隐私成为预防性的而不仅仅是补救性的”（Cavoukian 2010）[^cavoukian-2010]。设计即隐私的要点是，数据保护应在产品生命周期的所有阶段处于中心地位，从初始设计到运营使用和处置（关于设计即隐私进路的批判性分析见 Colesky et al. 2016）[^colesky-2016]。克拉克（Clarke，2009）提出的隐私影响评估进路提出了类似的观点。它提出“一种系统性的过程，用于评估一个项目、倡议或拟议系统或方案对隐私的潜在影响”（Clarke 2009）[^clarke-2009]。注意，这些进路不应仅仅被视为审计进路，而应被视为使隐私意识和合规成为组织与工程文化之组成部分的手段。

还有若干可用于设计隐私保护 IT 系统的行业指导方针。例如，支付卡行业数据安全标准（见 PCI DSS v3.2, 2018, [其他网络资源]）为信用卡行业及其合作伙伴（零售商、银行）领域中隐私和安全敏感系统的设计提供了非常清晰的指导方针。各种国际标准化组织（ISO）标准（Hone & Eloff 2002）[^hone-2002]也作为最佳实践和指导方针的来源，尤其是关于信息安全方面，用于设计隐私友好系统。此外，欧盟数据保护指令所形成的原则本身基于 70 年代初的公平信息实践（Gellman 2014）——透明度、目的、相称性、接触、转移——在技术上是中立的，因此也可被视为高层的“设计原则”。怀着这些规则和指导方针设计的系统，原则上应当符合欧盟隐私法，并尊重其用户的隐私。

上述规则和原则为设计隐私保护系统提供高层指导，但这并不意味着如果遵循这些方法论，所产生的 IT 系统就会（自动）隐私友好。一些设计原则相当含糊和抽象。所谓透明的设计或为相称性而设计，指的是什么？在设计特定系统时，原则需要被解释并置于语境中。但不同的人会不同地解释这些原则，导致不同的设计选择，对隐私产生不同影响。计算机系统的设计与实现之间也有区别。在实现阶段会引入软件缺陷，其中一些可被利用来破坏系统并提取私人信息。如何实现无缺陷的计算机系统仍是一个开放的研究问题（Hoare 2003）[^hoare-2003]。此外，实现是另一个选择与解释的阶段：系统设计可以以无限多种方式实现。而且，对于任何超出平凡系统的系统，很难验证实现是否符合其设计/规格（Loeckx, Sieber, & Stansifer 1985）。对于“保护隐私”这类非功能性要求或一般而言的安全属性，这甚至更加困难。

一些针对隐私问题的具体解决方案旨在提高用户的意识和同意水平。这些解决方案可被视为将知情同意概念应用于技术相关隐私问题的一种尝试（Custers et al. 2018）[^custers-2018]。这与隐私设置和政策应当可以向用户解释的观念相关（Pieters 2011）[^pieters-2011]。例如，隐私教练（Privacy Coach）在面对 RFID 标签时支持顾客作出隐私决定（Broenink et al. 2010 [其他网络资源]）。然而，用户处理这类选择的能力有限，提供过多选择很容易导致道德过载问题（van den Hoven, Lokhorst, & van de Poel 2012）。一个技术解决方案是支持把用户设定的隐私政策与网站或应用发布的政策自动匹配。

更晚近，IEEE、欧洲委员会、世界卫生组织（《人工智能健康伦理与治理》）和许多其他机构开始认识到，设计思维需要在我们对当今时代问题的伦理思考中发挥更大的作用。这对数字治理具有影响，因为透明度和问责要求清晰呈现价值和隐含要求；在一个图式或层级中，这允许设计者通过语境敏感的规范、以抽象程度递减的规格，把抽象价值或核心道德概念转化为设计要求（van de Poel 2013, 2020; Veluwenkamp & van den Hoven 2023）[^veluwenkamp-2023]。

### 3.2 隐私增强技术

越来越多的软件工具可为用户提供某种形式的隐私（通常是匿名性），这类工具通常被称为隐私增强技术（Danezis & Gürses 2010 [其他网络资源]）。例子包括 Tor（Dingledine, Mathewson, & Syverson 2004）和 Freenet（Clarke et al. 2001）[^clarke-2001]等通信匿名化工具，以及有许多商业软件包的身份管理系统（见下文）。通信匿名化工具允许用户匿名浏览网页（用 Tor）或匿名分享内容（Freenet）。它们采用多种密码学技术和安全协议，以确保匿名通信这一目标。这两个系统都利用了众多用户同时使用系统这一特性，它提供了 *k*-匿名（Sweeney 2002）[^sweeney-2002]：对于 *k* 的大值，任何个人都不能从大小为 *k* 的群体中被唯一地区分出来。取决于系统，*k* 的值可以在几百到几十万之间变化。在 Tor 中，消息被加密并沿着众多不同的计算机路由，从而掩盖消息的原始发送者（由此提供匿名性）。同样，在 Freenet 中，内容以加密形式为系统的所有用户所存储。由于用户自身没有必要的解密密钥，他们不知道系统在他们自己的计算机上存储了什么内容。这提供了可否认性和隐私。系统可以在任何时间检索加密内容并将其发送给不同的 Freenet 用户。

隐私增强技术也有其缺点。例如，Tor——允许互联网上匿名通信和浏览的工具——容易受到一种攻击，在特定情况下，用户的匿名性不再得到保证（Back, Möller, & Stiglic 2001; Evans, Dingledine, & Grothoff 2009）。Freenet（和其他工具）有类似问题（Douceur 2002）[^douceur-2002]。注意，这类攻击要奏效，攻击者需要获得大量资源，而这在实践中只有国家情报机构才能现实地做到。然而，还有其他风险。对普通用户而言，正确配置这类软件工具很困难，当工具配置不正确时，用户的匿名性不再得到保证。而且总存在这样的风险：运行隐私保护软件的计算机被木马（或其他数字害虫）感染，它会监控所有通信并知道用户身份。

提供匿名性的另一个选择是通过特殊软件对数据进行匿名化。存在去除患者姓名并把年龄信息缩减为区间的工具：年龄 35 于是表示为落在 30–40 的范围内。这类匿名化软件背后的观念是，记录不再能与个人相关联，而数据的相关部分仍可用于科学或其他目的。这里的问题是，很难把数据匿名化到所有与个人的关联都被移除，而所产生的匿名化数据仍对研究目的有用。研究者已表明，几乎总是可能通过使用复杂的统计方法（Danezis, Diaz, & Troncoso 2007）和组合多个包含个人信息的数据库（Anderson 2008）[^anderson-2008]来重构与个人的关联。*k*-匿名这类技术也可能有助于把数据泛化得足够充分，从而无法对数据去匿名化（LeFevre et al. 2005）[^lefevre-2005]。

更一般而言，论点是人们希望限制基于对数据的公开分析、从所披露内容中能推导出关于个人的信息，即所谓的统计披露控制。实现这一点的一种方式是生成具有大致相同统计属性、但基于不同个人条目的合成数据（Abowd & Vilhuber, 2008; Raghunathan, 2021）。不同的合成数据方法可能在准确性与隐私之间取得不同平衡。这类技术与差分隐私（Dwork, 2006）概念相关，差分隐私是一种度量，表明当某人的数据在数据集中时，披露的风险只会变得可忽略地更大。该术语也与通过在数据中注入噪声来实现差分隐私的方法相关（Liu et al., 2024）。

### 3.3 密码学

密码学长期以来用作保护数据的手段，可追溯到两千多年前的凯撒密码。现代密码学技术在任何需要存储（从而保护）个人数据的 IT 系统中都至关重要，例如通过为浏览（HTTPS）和组网（VPN）提供安全（保密）连接。但注意，密码学本身不提供任何针对数据泄露的保护；只有当它在特定语境中被正确应用时，才成为个人数据周围的“围栏”。此外，因更快的计算机或新的攻击而过时的密码学方案，可能对（长期）隐私构成威胁。

密码学是一个庞大的领域，因此这里的任何描述都不完整。相反，重点将放在一些较新的密码学技术上，特别是同态加密，它们有潜力在个人数据的处理和搜索中变得非常重要。

存在多种用于搜索加密数据的技术（Song et al. 2000, Wang et al. 2016）[^song-2000][^wang-2016]，它们提供了一种隐私保护形式（数据被加密）和对敏感数据的选择性接触。一种可用于设计隐私保护系统的相对较新的技术是“同态加密”（Gentry 2009, Acar et al. 2018）[^acar-2018][^gentry-2009]。同态加密允许数据处理者处理加密数据，即用户可以以加密形式发送个人数据，并取回一些有用结果——例如在线朋友喜欢的电影推荐——以加密形式。原始用户随后可以再次解密结果并使用它，而不向数据处理者泄露任何个人数据。例如，同态加密可用于聚合加密数据，从而同时允许隐私保护和有用的（匿名化）聚合信息。该技术目前未被广泛应用；如果想对当今系统中存储的大量数据应用全同态加密，存在严重的性能问题。然而，原始同态加密方案的变体正在出现，如某种程度同态加密（Badawi et al. 2018），显示出在实践中更广泛应用的前景。

区块链技术背后的主要观念最初在关于比特币的开创性论文中描述（Nakamoto, n.d. [其他网络资源]）。区块链基本上是一种分布式账本，以不可抵赖的方式存储交易，而无需使用可信第三方。密码学用于确保所有交易得到区块链成员的“批准”，并以与先前交易相连且无法移除的方式存储。尽管专注于数据完整性且并非固有匿名，区块链技术使许多隐私相关应用成为可能（Yli-Huumo et al. 2016, Karame and Capkun 2018）[^karame-2018][^yli-huumo-2016]，如匿名加密货币（Narayanan et al. 2016）[^narayanan-2016]和自主主权身份（见下文）。

### 3.4 身份管理

用户在线标识符的使用和管理在当前的互联网和社交网络中至关重要。在线声誉对用户和公司都变得越来越重要。在大数据时代，关于用户的正确信息具有越来越大的货币价值。

“单点登录”框架，由独立第三方（OpenID）提供，也由脸书、微软和谷歌等大公司提供（Ko et al. 2010），使用户能够用单一在线身份连接到众多在线服务。这些在线身份通常直接与个人的现实世界（离线）身份相关联；事实上，脸书、谷歌等要求这种登录形式（den Haak 2012）[^haak-2012]。从隐私角度看，要求在线身份与“现实世界”身份之间的直接关联是有问题的，因为它们允许对用户画像（Benevenuto et al. 2012）[^benevenuto-2012]。并非所有用户都会意识到公司以此方式收集的数据量有多大，或构建用户详细画像有多么容易。如果画像信息与其他技术（如通过 cookie 和追踪 cookie 的隐式认证）结合，画像甚至更容易（Mayer & Mitchell 2012）[^mayer-2012]。

从隐私角度看，更好的解决方案是使用基于属性的认证（Goyal et al. 2006）[^goyal-2006]，它允许基于用户属性（如他们的朋友、国籍、年龄等）接触在线服务。取决于所用的属性，它们仍可能被追溯到特定个人，但这不再关键。此外，用户不再能被追踪到不同服务，因为他们可以用不同属性访问不同服务，这使得跨多笔交易追踪在线身份变得困难，从而为用户提供不可关联性。近来（Allen 2016 [其他网络资源]），自主主权身份的概念出现了，它旨在让用户对其数字身份拥有完全的所有权和控制。区块链技术被用于让用户无需传统可信第三方即可控制数字身份（Baars 2016）[^baars-2016]。

## 4 隐私、技术与责任

在前几节中，我们概述了技术可能如何影响隐私，以及它们可能如何有助于减轻不良影响。这些发展是技术发展、对隐私价值的解释和社会责任分配之间相互作用的一部分。作为本文的最后部分，我们讨论隐私与信息技术的这些动态方面。

### 4.1 新兴技术与我们对隐私的理解

首先，有一些未来和新兴技术可能产生更为深远的影响。例如，考虑脑机接口（BCI）。如果计算机直接连接到大脑，不仅行为特征受隐私考量约束，甚至一个人的思想也有变得公开的风险，他人的决定可能基于这些思想。此外，这类技术可能使改变一个人的行为成为可能。因此，这类发展需要进一步考虑保护隐私的理由。特别是，当大脑过程可能受到外部影响时，自主将是一个需要重新考虑以确保充分保护的价值。脑机接口正处于商业化的边缘（Drew 2023）[^drew-2023]。马斯克的神经连接（Neuralink [其他网络资源]）和类似初创公司以多种方式寻求利用大脑数据。世界上一些最优秀的睡眠研究者写了一封公开信（Stickgold, Zadra, and Haar 2021 [其他网络资源]），表达他们对定向梦境孵化的担忧，这是一种通过卧室中的智能设备引导人们梦境的 AI 辅助技术。读心软件在判断人们在想什么或看什么方面每年都在进步（Brown 2024）[^brown-2024]。截瘫患者借助软件仅凭思维就能操纵计算机屏幕上的光标（Abiri et. al. 2020）[^abiri-2020]。

这些和其他发展已促使一个欧洲神经科学家联合会警告说，“人工智能驱动的大脑数据处理可能使接触心理信息成为可能，并把隐私辩论带入部分未勘探的领域。法律体系装备精良，足以保护‘外部场所’（locus externus）（行为、言语表达、书面文本等），但装备不足，难以保护‘内部场所’（locus internus）（如未说出的信息、前意识偏好、态度和信念）”（Ienca et al. 2022）[^ienca-2022]。

这些神经-AI 发展也引发了把隐私保护扩展到心理领域、并在思想自由权之外引入认知自由权的呼吁。后者关涉我们自由地思想任何我们想要的内容，前者关涉我们自由地选择思维模式，以及不被欺骗关于我们如何达到心理表征。

除了对照当前道德规范评价信息技术，还需要考虑技术变革影响规范本身的可能性（Boenink, Swierstra & Stemerding 2010）。因此，技术不仅通过改变信息的可及性影响隐私，也通过改变隐私规范本身影响隐私。例如，社交网站邀请用户分享比他们本来可能分享的更多的信息。这种“过度分享”（oversharing）成为某些群体内部被接受的惯例。对于未来和新兴技术，也可以预期这类影响，因此在试图减轻影响时应当把它们纳入考虑。

另一个根本性问题是，鉴于未来（甚至当前）的信息连接水平，通过试图向可能以不良方式使用信息的方隐藏信息来保护隐私是否可行。古特维尔特（Gutwirth）与德赫特（De Hert，2008）论证，通过透明度来保护隐私可能更可行，即要求行动者为关于个人所作的决定提供正当理由，从而坚持决定不基于不合法信息。这种进路有自身的问题，因为可能难以证明错误信息被用于决定。尽管如此，公民很可能会反过来开始收集那些收集他们数据者（如政府）的数据。这种“反监控”（counter(sur)veillance）可用于收集关于信息使用的信息，从而改善问责（Gürses et al. 2016）[^gürses-2016]。开源运动也可能促进数据处理的透明度。在这种语境下，透明度可被视为一种有助于隐私的亲伦理条件（Turilli & Floridi 2009）[^turilli-2009]。

有人论证，环境伦理学中众所周知的预防原则，也可能在应对新兴信息技术方面发挥作用（Pieters & van Cleeff 2009; Som, Hilty & Köhler 2009）[^pieters-2009]。该原则将确保：对于信息技术对社会不存在不可逆影响（例如就权力关系和平等而言）的举证责任，由倡导新技术者承担。在这个意义上，预防原则随后可用于在监管层面施加限制，与赋权用户相结合或作为其替代，从而可能有助于防止用户侧的信息过载。除了关于预防原则可欲与不可欲特征的普遍争论，对它的挑战在于将其转译为社会影响和社会可持续性，以及应用于行动者有意行为所导致的结果。鉴于自然威胁或事故的发生在本质上是概率性的，而那些对信息不当使用感兴趣者则策略性地行动，这需要一种不同的风险进路（即安全（security）而非安全性（safety））。此外，预防原则的拥护者需要将其与其他重要原则（即知情同意和自主）相平衡。

### 4.2 技术、能动性与责任

技术变革也与隐私问题中的能动性和责任应置于何处的问题相关。尽管有可用的技术解决方案，许多关于隐私的选择有意或无意地留给了用户。这涉及第三方处理数据需同意的法律要求、在社交网络服务等上自愿披露各种形式的信息，以及在不同水平的隐私保护的可选技术服务之间作出选择。一个关键问题是个人在多大程度上能够应对这一责任。有人指出，对隐私的态度与实际隐私行为之间存在落差，即所谓的“隐私悖论”（Kokolakis 2017; Gerber, Gerber & Volkamer 2018）[^gerber-2018][^kokolakis-2017]。也就是说，虽然个人声称在意隐私，但它在作出技术选择或披露决定时似乎扮演相对次要的角色。这可能是由于感知到的披露益处的普遍性、实际决策时的疏忽，或可能是“放弃”保护隐私的努力（隐私疲劳/虚无主义；Choi, Park & Jung 2018; Hoffmann, Lutz & Ranzini 2016; Van Ooijen, Segijn & Opree 2022）。

此外，界面的设计可能被刻意塑造以刺激个人尽可能多地披露信息，因为这符合在线服务的利益。这些所谓的“暗黑模式”（dark patterns）（Waldman 2020）[^waldman-2020]干扰了个人把隐私价值纳入其决定的能力。暗黑模式是“敌对性认知脚手架”（hostile cognitive scaffolding）的一种形式，其中在线环境被设计为服务于用户以外的他人利益（Timms & Spurrett 2023）[^timms-2023]。如果确实如此，问题是既有的社会技术系统所施加的选择架构，是否成功地使个人能够应对分配给他们的责任；如果不能，应当对此采取什么措施，谁负责创造适当条件。似乎清楚的是，选择过载或过度选择（Waldman 2020）[^waldman-2020]不是有助于承担责任的条件。

既有的社会技术系统所施加的选择架构是否使个人能够应对分配给他们的责任这一问题，也与技术相关隐私是否首先是一个个人问题的问题相关联。许多伤害可以论证与个人之间的比较相关，而非了解关于某一个体的敏感数据，这使得隐私成为一种公共善（Regan 2015）[^regan-2015]。

### 4.3 隐私与其他价值

在隐私与信息技术的关系中，我们因此看到（a）我们对隐私的理解可能被技术发展所改变，以及（b）对隐私的理解对相关的责任分配很重要。因此，社会动态在隐私与技术的关系中扮演关键角色。但这类动态不限于单一价值。因此，最后有必要指出，并非信息技术的所有社会影响都关涉隐私（Pieters 2017）[^pieters-2017]。例子包括社交网站对友谊的影响（与参与和幸福等价值相关），以及电子选举结果的可验证性（与公平价值相关）。因此，价值敏感设计进路和信息技术的影响评估不应只关注隐私，因为信息技术也影响许多其他价值。

## 参考文献

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## 学术工具

* [如何引用本词条](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=it-privacy)。
* [预览本词条的 PDF 版本](https://leibniz.stanford.edu/friends/preview/it-privacy/)，见 [SEP 学会之友](https://leibniz.stanford.edu/friends/)。
* 在 [InPhO](https://www.inphoproject.org/entity?sep=it-privacy&redirect=True) 查找与本词条相关的话题与思想家。
* 在 [PhilPapers](https://philpapers.org/sep/it-privacy/) 查看本词条的增强文献目录及其数据库链接。

## 其他网络资源

* Albright, J.，2016 年，“[特朗普的竞选团队如何利用新的数据产业综合体赢得选举](https://blogs.lse.ac.uk/usappblog/2016/11/26/how-trumps-campaign-used-the-new-data-industrial-complex-to-win-the-election/)”，LSE 美国中心，USApp 美国政治与政策博客。
* Allen, C.，2016 年，[通往自主主权身份之路](https://www.coindesk.com/markets/2016/04/27/the-path-to-self-sovereign-identity)，Coindesk。
* Broenink, G. 等，2010 年，“[隐私教练：在物联网中支持顾客隐私](http://arxiv.org/abs/1001.4459)”，*arXiv 手稿* 1001.4459。
* Cadwalladr, C.，2019 年，[脸书在脱欧中的角色——及对民主的威胁](https://www.ted.com/talks/carole_cadwalladr_facebook_s_role_in_brexit_and_the_threat_to_democracy)。TED 演讲。
* Campbell, D.，2023 年，[美国间谍技术公司 Palantir 赢得 3.3 亿英镑 NHS 合同引发患者隐私忧虑](https://www.theguardian.com/society/2023/nov/21/patient-privacy-fears-us-spy-tech-firm-palantir-wins-nhs-contract)，《卫报》。
* Danezis, G. 与 S. Gürses，2010 年，“[对十年隐私技术的批判性回顾](http://homes.esat.kuleuven.be/~sguerses/papers/DanezisGuersesSurveillancePets2010.pdf)”。
* [电子隐私信息中心（EPIC）](http://epic.org/)。
* [欧盟委员会：数据保护](https://ec.europa.eu/info/law/law-topic/data-protection_en)。
* Gellman, R.，2014 年，“[公平信息实践：一部基础历史](http://bobgellman.com/rg-docs/rg-FIPShistory.pdf)”，版本 2.12，2014 年 8 月 3 日，在线手稿。
* Germain, R.，2023 年，“[谷歌称将抓取你在线发布的所有内容用于 AI](https://gizmodo.com/google-says-itll-scrape-everything-you-post-online-for-1850601486)”，Gizmodo。
* Inan, H. A. 等，2021 年，“[语言模型中的训练数据泄漏分析](https://arxiv.org/abs/2101.05405)”，arXiv.org。
* Nakamoto, S.，[比特币：一种点对点电子现金系统](https://bitcoin.org/bitcoin.pdf)，www.bitcoin.org。
* [Neuralink（神经连接）](https://neuralink.com/)。
* [OpenAI：ChatGPT](https://chat.openai.com/)。
* PCI DSS（即支付卡行业数据安全标准），v3.2（2018），[PCI DSS 相关文件](https://www.pcisecuritystandards.org/document_library)，PCI 安全标准委员会。
* Richter, H. 等，2008 年，“[对护照的指纹采集](http://cs.ru.nl/E.Poll/papers/nluug.pdf)”，发表于 NLUUG 春季安全会议。
* Stickgold, Robert 等，2021 年，[广告入梦已成现实：现在怎么办](https://dxe.pubpub.org/pub/dreamadvertising/release/1)——关于梦境孵化技术新近发展及其伦理意涵的评论文章。
* [美国国务院：隐私政策](https://www.state.gov/privacy-policy/)。
* [美国财政部：1974 年隐私法](https://home.treasury.gov/footer/privacy-act)。

## 相关词条

计算机与道德责任 | 搜索引擎伦理 | 信息 | 信息技术与道德价值 | 隐私 | 网络社交与伦理学

**（译注：相关词条的中文站内链接将由管线在对应词条重译完成后统一挂接。）**

[^abelson-2015]: Abelson, H., Anderson, R., Bellovin, S. M., Benaloh, J., Blaze, M., Diffie, W., & Rivest, R. L., 2015, “Keys under doormats: mandating insecurity by requiring government access to all data and communications”, *Journal of Cybersecurity*, 1(1): 69–79.

[^abiri-2020]: Abiri, R., Borhani, S., Kilmarx, J., Esterwood, C., Jiang, Y., & Zhao, X., 2020, “A usability study of low-cost wireless brain-computer interface for cursor control using online linear mode”, IEEE transactions on human-machine systems, 50(4): 287–297.

[^abowd-2008]: Abowd, J. M., & Vilhuber, L., 2008, “How protective are synthetic data?”, in J. Domingo-Ferrer & Y. Saygun (eds.), *Privacy in Statistical Databases* (LNCS, volume 5262), Berlin, Heidelberg: Springer, pp. 239–246f.

[^acar-2018]: Acar, A., Aksu, H., Uluagac, A. S., & Conti, M., 2018, “A survey on homomorphic encryption schemes: Theory and implementation”, *ACM Computing Surveys* (CSUR), 51(4): 79.

[^allen-2011]: Allen, A., 2011, *Unpopular Privacy: What Must We Hide?* Oxford: Oxford University Press.

[^anderson-2008]: Anderson, R.J., 2008, *Security Engineering: A guide to building dependable distributed systems*, Indianapolis, IN: Wiley.

[^angelov-2021]: Angelov, P. P., Soares, E. A., Jiang, R., Arnold, N. I., & Atkinson, P. M., 2021, “Explainable artificial intelligence: an analytical review”, *Wiley Interdisciplinary Reviews: Data Mining and Knowledge Discovery*, 11(5): e1424.

[^baars-2016]: Baars, D., 2016, *Towards Self-Sovereign Identity using Blockchain Technology*, Ph.D. Thesis, University of Twente.

[^back-2001]: Back, A., U. Möller, & A. Stiglic, 2001, “Traffic analysis attacks and trade-offs in anonymity providing systems”, in *Information Hiding*, Berlin: Springer, pp. 245–257.

[^al-2018]: Al Badawi, A., Veeravalli, B., Mun, C. F., & Aung, K. M. M., 2018, “High-performance FV somewhat homomorphic encryption on GPUs: An implementation using CUDA”, *IACR Transactions on Cryptographic Hardware and Embedded Systems*, 2: 70–95. doi: 10.13154/tches.v2018.i2.70-95

[^bellman-2001]: Bellman, S., E.J. Johnson, & G.L. Lohse, 2001, “On site: to opt-in or opt-out?: it depends on the question”, *Communications of the ACM*, 44(2): 25–27.

[^benevenuto-2012]: Benevenuto, F., T. Rodrigues, M. Cha, & V. Almeida, 2012, “Characterizing user navigation and interactions in online social networks”, *Information Sciences*, 195: 1–24.

[^blaauw-2013]: Blaauw. M.J., 2013, “The Epistemic Account of Privacy”, *Episteme*, 10(2): 167–177.

[^boenink-2010]: Boenink, M., T. Swierstra, & D. Stemerding, 2010, “Anticipating the interaction between technology and morality: a scenario study of experimenting with humans in bionanotechnology”, *Studies in Ethics, Law, and Technology*, 4(2): 1–38. doi:10.2202/1941-6008.1098

[^brey-2005]: Brey, P., 2005, “Freedom and privacy in ambient intelligence”, *Ethics and Information Technology*, 7(3): 157–166.

[^brown-2024]: Brown, C. M. L., 2024, “Neurorights, Mental Privacy, and Mind Reading” *Neuroethics*, 17(2): 1–19.

[^bruijn-2022]: de Bruijn, H., Warnier, M., & Janssen, M., 2022. “The perils and pitfalls of explainable AI: Strategies for explaining algorithmic decision-making”, *Government information quarterly*, 39(2): 101666.

[^bruynseels-2015]: Bruynseels, K & M.J van den Hoven, 2015, “How to do Things with personal Big Biodata”, in B. Roessler and D. Mokrokinska (eds.), *Social Dimensions of Privacy: Interdisciplinary Perspectives*, Cambridge: Cambridge University Press, pp. 122–40.

[^cadwalladr-2018]: Cadwalladr, C., and Graham-Harrison, E., 2018, “The Cambridge analytica files”, *The Guardian*, 21: 6–7.

[^cavoukian-2009]: Cavoukian, A., 2009, *Privacy by Design*, Ottowa: Information and Privacy Commissioner of Ontario, Canada. [[Cavoukian 2009 available online](https://web.archive.org/web/20160330122525/https://www.ipc.on.ca/images/resources/privacybydesign.pdf) (PDF)].

[^cavoukian-2010]: –––, 2010, “Privacy by Design: The Definitive workshop”, *Identity in the Information Society*, 3(2): 121–126.

[^ceross-2018]: Ceross, A., and A. Simpson, 2018, “Rethinking the Proposition of Privacy Engineering”, in *Proceedings of New Security Paradigms Workshop* (NSPW 18, Windsor, UK), New York: Association for Computing Machinery, 89–102. doi:10.1145/3285002.3285006

[^choi-2018]: Choi, H., Park, J., & Jung, Y., 2018, “The role of privacy fatigue in online privacy behavior”, *Computers in Human Behavior*, 81, 42–51.

[^clarke-2009]: Clarke, R., 2009, “Privacy impact assessment: Its origins and development”, *Computer law & security review*, 25(2): 123–135.

[^clarke-2001]: Clarke, I., O. Sandberg, B. Wiley, & T. Hong, 2001, “Freenet: A distributed anonymous information storage and retrieval system”, in *Designing Privacy Enhancing Technologies*, Berlin: Springer, pp. 46–66.

[^colesky-2016]: Colesky, M., J.-H. Hoepman, and C. Hillen, 2016, “A critical analysis of privacy design strategies”, *IEEE Security and Privacy Workshops* (SPW), first online O4 August 2016, doi:10.1109/SPW.2016.23

[^colonna-2022]: Colonna, L., 2022, “Addressing the Responsibility Gap in Data Protection by Design: Towards a More Future-oriented, Relational, and Distributed Approach”, *Tilburg Law Review*, 27(1).

[^curzon-2021]: Curzon, J., Kosa, T. A., Akalu, R., & El-Khatib, K., 2021, “Privacy and artificial intelligence”, *IEEE Transactions on Artificial Intelligence*, 2(2), 96–108.

[^custers-2018]: Custers, B., et al., 2018, “Consent and privacy”, *The Routledge Handbook of the Ethics of Consent*, London: Routledge, pp. 247–258.

[^dahl-2009]: Dahl, J. Y., & A.R. Sætnan, 2009, “It all happened so slowly: On controlling function creep in forensic DNA databases”, *International journal of law, crime and justice*, 37(3): 83–103.

[^danezis-2007]: Danezis, G., C. Diaz, & C. Troncoso, 2007, “Two-sided statistical disclosure attack”, in *Proceedings of the 7th international conference on Privacy enhancing technologies*, Berlin: Springer, pp. 30–44.

[^decew-1997]: DeCew, Judith Wagner, 1997, *Pursuit of Privacy: Law, Ethics, and the Rise of Technology*, Ithaca, NY: Cornell University Press.

[^dechesne-2013]: Dechesne, F., M. Warnier, & J. van den Hoven, 2013, “Ethical requirements for reconfigurable sensor technology: a challenge for value sensitive design”, *Ethics and Information Technology*, 15(3): 173–181.

[^delaune-2006]: Delaune, S., S. Kremer, & M. Ryan, 2006, “Coercion-resistance and receipt-freeness in electronic voting”, in the *Proceedings of the 19th IEEE Computer Security Foundations Workshop*, IEEE Computer Society Press, pages 28–39. [[Delaune et al. 2006 available online](http://www.loria.fr/~skremer/Publications/b2hd-DKR-csfw06.html)]

[^dingledine-2004]: Dingledine, R., N. Mathewson, & P. Syverson, 2004, “Tor: The second-generation onion router”, in *Proceedings of the 13th conference on USENIX Security Symposium* (Volume 13), Berkeley, CA: USENIX Association, pp. 303–320 [[Dingledine et al. 2004 available online (pdf)](https://www.usenix.org/legacy/publications/library/proceedings/sec04/tech/full_papers/dingledine/dingledine.pdf?CFID=597263069&CFTOKEN=54138242)]

[^došilović-2018]: Došilović, F. K., Brčić, M., & Hlupić, N., 2018, “Explainable artificial intelligence: A survey” In *41st International convention on information and communication technology, electronics and microelectronics (MIPRO)* pp. 0210–0215, IEEE.

[^douceur-2002]: Douceur, J., 2002, “The Sybil attack”, in *Peer-to-peer Systems*, Berlin: Springer, pp. 251–260.

[^drew-2023]: Drew, L., 2023, “Decoding the business of brain-computer interfaces”, *Nature Electronics*, 6(2), 90–95.

[^dwork-2006]: Dwork, C., 2006, “Differential Privacy”, in M. Bugliesi, B. Preneel, V. Sassone, and I. Wegener (eds.), *Automata, Languages and Programming*, ICALP 2006 (Lecture Notes in Computer Science: 4052), Springer, Berlin, Heidelberg.

[^ellison-2007]: Ellison, N. B., 2007, “Social network sites: Definition, history, and scholarship”, *Journal of Computer-Mediated Communication*, 13(1): 210–230.

[^evans-2009]: Evans, N.S., R. Dingledine, & C. Grothoff, 2009, “A practical congestion attack on Tor using long paths”, in *Proceedings of the 18th conference on USENIX security symposium*, Berkeley, CA: USENIX Association, pp. 33–50. [[Evans et al. 2009 available online](https://www.usenix.org/legacy/events/sec09/tech/full_papers/evans.pdf)]

[^falgoust-2016]: Falgoust, M., 2016, “Data Science and Designing for Privacy”, *Techné: Research in Philosophy and Technology*, 20 (1): 51–68.

[^floridi-2008]: Floridi, L., 2008, “Artificial intelligence's new frontier: Artificial companions and the fourth revolution”, *Metaphilosophy*, 39(4–5): 651–655.

[^friedewald-2011]: Friedewald, M. & O. Raabe, 2011, “Ubiquitous computing: An overview of technology impacts”, *Telematics and Informatics*, 28(2): 55–65.

[^friedman-2006]: Friedman, B., P.H. Kahn, Jr, & A. Borning, 2006, “Value sensitive design and information systems”, in *Human-computer interaction in management information systems: Foundations*, P. Zhang & D. Galletta (eds.), Armonk: M.E. Sharp, 4.

[^gentry-2009]: Gentry, C., 2009, “Fully homomorphic encryption using ideal lattices”, in *Proceedings of the 41st annual ACM symposium on Theory of computing*, ACM, pp. 169–178.

[^gerber-2018]: Gerber, N., P. Gerber, and M. Volkamer. “Explaining the privacy paradox: A systematic review of literature investigating privacy attitude and behavior”, *Computers & security* 77 (2018): 226–261.

[^goyal-2006]: Goyal, V., O. Pandey, A. Sahai, & B. Waters, 2006, “Attribute-based encryption for fine-grained access control of encrypted data”, in *Proceedings of the 13th ACM conference on Computer and communications security*, ACM, pp. 89–98.

[^gürses-2016]: Gürses, S., A. Kundnani, & J. Van Hoboken, 2016, “Crypto and empire: the contradictions of counter-surveillance advocacy”, *Media, Culture & Society*, 38(4): 576–590.

[^gutwirth-2008]: Gutwirth, S. & P. De Hert, 2008, “Regulating profiling in a democratic constitutional state”, in Hildebrandt and Gutwirth 2008: 271–302.

[^haak-2012]: den Haak, B., 2012, “Integrating user customization and authentication: the identity crisis”, *Security & Privacy, IEEE*, 10(5): 82–85.

[^hassan-2022]: Hassan, J., Shehzad, D., Habib, U., Aftab, M. U., Ahmad, M., Kuleev, R., & Mazzara, M., 2022, “The rise of cloud computing: data protection, privacy, and open research challenges – a systematic literature review (SLR)”, *Computational intelligence and neuroscience*, 2022: 8303504. doi:10.1155/2022/8303504

[^heersmink-2011]: Heersmink, R., J. van den Hoven, N.J. van Eck, & J. van den Berg, 2011. “Bibliometric mapping of computer and information ethics”, *Ethics and information technology*, 13(3): 241–249.

[^hildebrandt-2008]: Hildebrandt, M., 2008, “Defining Profiling: A New Type of Knowledge?” in Hildebrandt and Gutwirth 2008: 17–45.

[^hildebrandt-2008-2]: Hildebrandt, M. & S. Gutwirth (eds.), 2008, *Profiling the European Citizen: Cross-disciplinary Perspectives*, Dordrecht: Springer Netherlands.

[^hill-2023]: Hill, G., 2023 “The emerging artificial intelligence (AI) and national uniform legislation”, *Australian Law Journal*, 97(5), 303–306.

[^hoare-2003]: Hoare, T., 2003, “The verifying compiler: A grand challenge for computing research”, in *Proceedings of the 12th international conference on Compiler construction*, Berlin: Springer, pp. 262–272.

[^hoffmann-2016]: Hoffmann, C. P., C. Lutz, and G. Ranzini., 2016, “Privacy cynicism: A new approach to the privacy paradox” *Cyberpsychology: Journal of Psychosocial Research on Cyberspace*, 10(4).

[^hone-2002]: Hone, K. & J.H.P. Eloff, 2002, “Information security policy – what do international information security standards say?”, *Computers & Security*, 21(5): 402–409.

[^hoven-1999]: van den Hoven, J., 1999, “Privacy and the Varieties of Informational Wrongdoing”, *Australian Journal of Professional and Applied Ethics*, 1(1): 30–44.

[^hoven-2008]: –––, 2008, “Information technology, privacy, and the protection of personal data”, in *Information technology and moral philosophy*, J. Van Den Hoven and J. Weckert (eds.), Cambridge: Cambridge University Press, pp. 301–322.

[^hoven-2012]: van den Hoven, J., G.J. Lokhorst, & I. Van de Poel, 2012, “Engineering and the problem of moral overload”, *Science and engineering ethics*, 18(1): 143–155.

[^hoven-2015]: van den Hoven, J., Vermaas, P., & Van de Poel, I. (eds.), 2015, *Handbook of Ethics, Values and Technological Design*, Dordrecht: Springer.

[^ienca-2022]: Ienca, M., Fins, J. J., Jox, R. J., Jotterand, F., Voeneky, S., Andorno, R., Ball, T., Castelluccia, C., Chavarriaga, R., Chneiweiss, H., Ferretti, A., Friedrich, O., Hurst, S., Merkel, G., Molnar-Gabor, F., Rickli, J., Scheibner, J., Vayena, E., Yuste, R. & Kellmeyer, P., 2022, “Towards a governance framework for brain data” *Neuroethics*, 15(2): 20.

[^karame-2018]: Karame, G., and Capkun, S., 2018, “Blockchain Security and Privacy”, *IEEE Security Privacy*, 16(4), 11–12.

[^ko-2010]: Ko, M.N., G.P. Cheek, M. Shehab, & R. Sandhu, 2010, “Social-networks connect services”, *Computer*, 43(8): 37–43.

[^kokolakis-2017]: Kokolakis, S., 2017, “Privacy attitudes and privacy behaviour: A review of current research on the privacy paradox phenomenon”, *Computers & security*, 64: 122–134.

[^krishnamurthy-2009]: Krishnamurthy, B. & C.E. Wills, 2009. “On the leakage of personally identifiable information via online social networks”, in *WOSN 09: Proceedings of the 2nd ACM workshop on Online Social Networks*, New York: Association for Computing Machinery, pp. 7–12.

[^lawner-2002]: Lawner, K. J., 2002, “Post-September 11th International Surveillance Activity – A Failure of Intelligence: The Echelon Interception System & (and) the Fundamental Right to Privacy in Europe”, *Pace International Law Review*, 14(2): 435–480.

[^leenes-2015]: Leenes, R., and E. Kosta, 2015, “Taming the cookie monster with dutch law-a tale of regulatory failure”, *Computer Law & Security Review* 31(3): 317–335.

[^lefevre-2005]: LeFevre, K., D.J. DeWitt, & R. Ramakrishnan, 2005, “Incognito: Efficient full-domain k-anonymity”, in *Proceedings of the 2005 ACM SIGMOD International Conference on Management of Data*, New York: Association of Computing Machinery, pp. 49–60.

[^lessig-1999]: Lessig, Lawrence, 1999, *Code and Other Laws of Cyberspace*, New York: Basic Books.

[^liu-2024]: Liu, W., Zhang, Y., Yang, H., & Meng, Q., 2024, “A survey on differential privacy for medical data analysis”. *Annals of Data Science*, 11(2): 733–747.

[^loeckx-1985]: Loeckx, J., K. Sieber, & R.D. Stansifer, 1985, *The foundations of program verification*, Chichester: John Wiley & Sons.

[^matheson-2007]: Matheson, David, 2007, “Unknowableness and Informational Privacy”, *Journal of Philosophical Research*, 32: 251–67.

[^mayer-2012]: Mayer, J.R. & J.C. Mitchell, 2012, “Third-party web tracking: Policy and technology”, in *Security and Privacy (SP) 2012 IEEE Symposium on*, IEEE, pp. 413–427.

[^michener-1999]: Michener, J., 1999, “System insecurity in the Internet age”, *Software*, IEEE, 16(4): 62–69.

[^motlagh-2017]: Motlagh, N. H., Bagaa, M., & Taleb, T., 2017, “UAV-based IoT platform: A crowd surveillance use case”, *IEEE Communications Magazine*, 55(2): 128–134.

[^nagenborg-2009]: Nagenborg, M., 2009, “Designing spheres of informational justice”, *Ethics and Information Technology*, 11(3): 175–179.

[^narayanan-2016]: Narayanan, A., Bonneau, J., Felten, E., Miller, A., & Goldfeder, S., 2016, *Bitcoin and cryptocurrency technologies: a comprehensive introduction*, Princeton: Princeton University Press.

[^negley-1966]: Negley, G., 1966, “Philosophical Views on the Value of Privacy”, *Law and Contemporary Problems*, 31: 319–325.

[^nissenbaum-2004]: Nissenbaum, Helen, 2004, “Privacy as Contextual Integrity”, *Washington Law Review*, 79: 101–139.

[^oecd-1980]: OECD, 1980 [2013], *The OECD Privacy Framework*, 2013, [available in PDF](http://www.oecd.org/sti/ieconomy/oecd_privacy_framework.pdf); revised and expanded from the original *Guidelines on the Protection of Privacy and Transborder Flows of Personal Data*, Organization for Economic Co-operation and Development, [[1980 version available online](http://www.oecd.org/sti/ieconomy/oecdguidelinesontheprotectionofprivacyandtransborderflowsofpersonaldata.htm)]

[^ooijen-2022]: van Ooijen, I., Segijn, C. M., & Opree, S. J., 2022, “Privacy cynicism and its role in privacy decision-making”, *Communication Research*, 51(2). doi:10.1177/00936502211060984

[^palmer-2005]: Palmer, D.E., 2005, “Pop-ups, cookies, and spam: toward a deeper analysis of the ethical significance of internet marketing practices”, *Journal of business ethics*, 58(1–3): 271–280.

[^pettit-2001]: Pettit, P., 2001, *A theory of freedom: from the psychology to the politics of agency*, Oxford: Oxford University Press.

[^pieters-2011]: Pieters, W., 2011, “Explanation and trust: what to tell the user in security and AI?”, *Ethics and information technology*, 13(1): 53–64.

[^pieters-2013]: –––, 2013, “On thinging things and serving services: technological mediation and inseparable goods”, *Ethics and information technology*, 15(3): 195–208.

[^pieters-2017]: –––, 2017, “Beyond individual-centric privacy: Information technology in social systems” *The Information Society*, 33(5): 271–281.

[^pieters-2009]: Pieters, W. & A. van Cleeff, 2009, “The precautionary principle in a world of digital dependencies”, *Computer*, 42(6): 50–56.

[^van-2013]: Van de Poel, I., 2013, “Translating values into design requirements”, in D. P. Michelfelder, N. McCarthy, and D. E. Goldberg (eds.), *Philosophy and engineering: Reflections on practice, principles and process*, Dordrecht: Springer, pp. 253–266.

[^van-2020]: –––, 2020, “Values and design” in D. P. Michelfelder & N. Doorn (eds.), *The Routledge Handbook of the Philosophy of Engineering*, London: Routledge, pp. 300–314.

[^raghunathan-2021]: Raghunathan, T. E., 2021, “Synthetic data”, *Annual Review of Statistics and its Application*, 8(1): 129–140.

[^regan-2015]: Regan, P. M., 2015, “Privacy and the common good: revisited”, *Social dimensions of privacy: Interdisciplinary perspectives*, Cambridge: Cambridge University Press, pp. 50–70. doi:10.1017/CBO9781107280557.004

[^roberts-2015]: Roberts, A., 2015, “A Republican Account of the Value of Privacy”, *European Journal of Political Theory*, 14(3): 320–344

[^rössler-2004]: Rössler, Beate (ed.), 2004, *Privacies: Philosophical Evaluations*, Stanford, CA: Stanford University Press.

[^rössler-2005]: Rössler, Beate, 2005, *The value of privacy*, Cambridge: Polity Press.

[^rössler-2001]: –––, 2001 [2005], *The Value of Privacy*, Cambridge: Polity Press; original German version *Der Wert des Privaten*, Frankfurt am Main: Suhrkamp Verlag, 2001.

[^rubel-2011]: Rubel, Alan, 2011, “The Particularized Judgment Account of Privacy”, *Res Publica*, 17(3): 275–90.

[^ruiter-2011]: Ruiter, J. & M. Warnier, 2011, “Privacy Regulations for Cloud Computing: Compliance and Implementation in Theory and Practice”, in *Computers, Privacy and Data Protection: an Element of Choice*, S. Gutwirth, Y. Poullet, P. De Hert, and R. Leenes (eds.), Dordrecht: Springer Netherlands, pp. 361–376.

[^smith-2020]: Smith, P. T., 2020, “A neo-republican theory of just state surveillance”, *Moral Philosophy and Politics*, 7(1): 49–71.

[^solove-2006]: Solove, D., 2006, “A Taxonomy of Privacy”, *University of Pennsylvania Law Review*, 154: 477–564.

[^som-2009]: Som, C., L.M. Hilty, & A.R. Köhler, 2009, “The precautionary principle as a framework for a sustainable information society”, *Journal of business ethics*, 85(3): 493–505.

[^song-2000]: Song, D.X., D. Wagner, & A. Perrig, 2000, “Practical techniques for searches on encrypted data”, in *Proceedings of the 2000 IEEE Symposium on Security and Privacy* (S&P 2000), Berkeley, CA, pp. 44–55. doi:10.1109/SECPRI.2000.848445.

[^sprenger-1999]: Sprenger, Polly, 1999, “Sun on Privacy: ‘Get Over It’”, *Wired*, 26 January 1999. [[Sprenger 1999 available online](https://www.wired.com/1999/01/sun-on-privacy-get-over-it/)]

[^sweeney-2002]: Sweeney, L., 2002, “K-anonymity: A model for protecting privacy”, *International Journal of Uncertainty, Fuzziness and Knowledge-Based Systems*, 10(05): 557–570.

[^tavani-2004]: Tavani, H.T., 2004, “Genomic research and data-mining technology: Implications for personal privacy and informed consent”, *Ethics and information technology*, 6(1): 15–28.

[^taylor-2017]: Taylor, L., L. Floridi, and B. Van der Sloot (eds.), 2017, *Group privacy: New challenges of data technologies* (Philosophical Studies Series: Vol. 126), Dordrecht: Springer.

[^thomson-1975]: Thomson, Judith Jarvis, 1975, “The Right to Privacy”, *Philosophy and Public Affairs*, 4: 295–314.

[^turilli-2009]: Turilli, M. & L. Floridi, 2009, “The ethics of information transparency”, *Ethics and Information Technology*, 11(2): 105–112.

[^timms-2023]: Timms, R. & Spurrett, D., 2023, “Hostile Scaffolding” *Philosophical Papers*, 52(1): 53–82. doi:10.1080/05568641.2023.2231652

[^veluwenkamp-2023]: Veluwenkamp, H., & van den Hoven, J., 2023, “Design for values and conceptual engineering”, *Ethics and Information Technology*, 25(1): 2.

[^waldman-2020]: Waldman, A. E., 2020, “Cognitive biases, dark patterns, and the ‘privacy paradox’”, *Current opinion in psychology*, 31: 105–109.

[^wang-2016]: Wang, Y., Wang, J., and Chen, X., 2016, “Secure searchable encryption: a survey”, *Journal of Communications and Information Networks*, 1(4): 52–65.

[^warnier-2015]: Warnier, M., Dechesne, F., and Brazier, F.M.T., 2015, “Design for the Value of Privacy”, in J. van den Hoven, P. Vermaas, I. van de Poel (eds.), *Handbook of Ethics, Values, and Technological Design*, Dordrecht: Springer, 431–445.

[^warren-1890]: Warren, Samuel D. & Louis D. Brandeis, 1890, “The Right to Privacy”, *Harvard Law Review*, 4(5): 193–220. [[Warren and Brandeis 1890 available online](http://www.jstor.org/stable/1321160)]

[^westin-1967]: Westin, Alan F., 1967, *Privacy and Freedom*, New York: Atheneum.

[^yli-huumo-2016]: Yli-Huumo, J., Ko, D., Choi, S., Park, S., and Smolander, K., 2016, “Where is current research on blockchain technology? – a systematic review”, *PloS One*, 11(10): e0163477. doi:10.1371/journal.pone.0163477

[^zuboff-2019]: Zuboff, S., 2019, *The age of surveillance capitalism: the fight for the future at the new frontier of power*, London: Profile Books.
