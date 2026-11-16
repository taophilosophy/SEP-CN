# 本体论与信息系统 Ontology and Information Systems (Adam Pease)

*首次发表于 2026 年 1 月 3 日。*

两个主体交流时，必须对所用符号的含义拥有一批相当分量的共同理解。人类曾试图把其中一部分共同含义编入词典。计算机与信息科学面对的挑战则是：如何让机器分享人类所用符号目录的至少一部分，并分享其含义。与机器打交道，必须靠数学来陈述含义，不能靠交流主体的经验与直觉。信息系统中的本体论（ontology）正是致力于为符号建立共同含义的领域。领域内的实践者各自可以编制符号清单，并给出不同定义。

把本体论发展成一门学科，动机之一是软件开发中的常见问题：不同程序员在代码里使用符号的方式会随时间改变，使系统出现并非本意的表现。为应对这一问题，人们着手对概念编目、标准化与复用，并把成果记录为一套标签与定义。建立本体论有助于避免概念漂移（Magne 2017; Lu et al. 2019; Pancha 2016）[^magne-2017][^pancha-2016]，也能支持软件系统之间互通。

## 1. 导论

在信息与计算机科学中，本体研究关心的是：为了在计算机上完成某种计算，如何定义或描述 **存在** 之物（含想象之物与可能之物）。在哲学里，本体论常被描述为“研究存在什么”（参见社会本体论、逻辑本体论与自然语言本体论诸词条）。哲学本体论因此声称要辨明：实在由哪些基本构成组成，它们各属什么范畴，彼此又有何关系。计算机与信息科学中的本体论与哲学相同之处，是同样研究范畴（参见范畴词条）；不同之处在于重心落在实践上：用形式句法记录一份范畴清单，且往往配以某种形式语义。有些信息科学本体论还进一步要求把这些范畴的定义形式化。作为计算机与信息科学的一个领域，本体论也可恰当地说成研究存在什么；但它研究的未必是最终存在之物，而是在某个相关领域中、为某种计算目的而被假定存在之物。计算机科学家对范畴的形而上学地位——它们究竟真实存在，还是仅属人类建构——兴趣不大，更看重它们在计算中的实际用途。除范畴之外，计算机与信息科学中的本体论还可以编录个体与关系。

计算机科学中一个流行的本体定义是“对概念化的刻画”（Gruber 1993）[^gruber-1993]。不过这样说，还得解释何谓刻画、何谓概念化。概念化是理解某一概念结构的方式：既看该概念与其他概念的关系，也看可能支配它的原则。因此，概念化包含了一种理解，即一个概念如何把它所统摄的对象（无论抽象还是具体）与其他事物区分开。历史上，这种理解可以落实为人类语言中的词典条目或百科条目。概念常用单词或短语作标签；概念既然是这些词与短语的含义，便不属于句法的一部分。不同人类语言用不同符号，却能表达同一概念——尽管能否做到真正精确的翻译仍有争论（Levine & Lateef-Jan 2017）[^levine-2017]。词语是 **指称** 的一种手段（参见指称词条）。我们希望：用到“乞力马扎罗山”这类专名时，听者已握有足够多的相关共同信息，想传达的意思便能传达到。但换成“对象”“美”这类更抽象的概念，麻烦就来了。概念一旦以某种方式表达出来供交流，我们就可以追问“刻画”究竟意味着什么。若不依靠人对词或词组意图含义的直觉，也不依靠人的澄清对话，那就得另想办法记录观念或思想。

自计算机科学界采用以来，“本体”一词的用法日益宽泛。带自然语言定义的词语汇编也被称作本体论，其实叫词汇表即可，无须为已有旧名的事物另造新词。刻画本体的其他进路还有：分类法语言（Dallwitz 1980）[^dallwitz-1980]或统一建模语言（UML：Rumbaugh, Jacobson, & Booch 2004）[^rumbaugh-2004]；也有人认为概念名称加二元关系构成的图已足够，例如语义网络（Woods 1975）[^woods-1975]、知识图谱（可用资源描述框架（RDF：见下文“其他网络资源”中的 RDF 链接）表述），或图数据库（Kaliyar 2015）[^kaliyar-2015]。描述逻辑（Baader, Calvanese, McGuinness, Nardi, & Patel-Schneider 2007）[^baader-2007]是刻画本体时相当流行的选择。最形式化的刻画，则是一阶逻辑（Enderton 1972）[^enderton-1972]、模态逻辑或高阶逻辑这类表达力强的数学逻辑中的一组公式（参见模态逻辑与高阶逻辑词条）。

构建本体论最重要的两个动机是：(i) 有助于防止概念漂移；(ii) 支持系统之间的互操作。先说第一点：软件开发中的常见问题是，不同程序员在代码里使用符号串的方式会随时间变化，使系统出现并非本意的表现。本体论把概念标准化并使之可复用，以此防止某段代码中由某个字符串表达的概念，日后漂移成另一个概念。再说互操作：所建本体的类型，至少部分取决于预期用途。用途大体分三类，最终都落到某种计算实现上，同一应用中可能三者兼有：(1) 人与人交流；(2) 机器与机器、或人与机器交流；(3) 计算。

在 (1) 中，本体论用于统一系统开发者之间的术语与理解。标签或定义的集合未必会被精确搬进某个形式化计算系统。这类本体论服务于人际理解，可以依赖由名称而来的概念直觉，也可以依赖自然语言定义。把专门术语的含义固定进词汇表，有助于排除某些解释，例如因一词多义而生的误解。

在 (2) 中，系统所用的标签集构成一项标准，人与软件系统共同遵循。开发该系统的各方就所用符号集达成一致，并就若干定义达成一致；这些定义至少部分以自然语言给出，要靠人的智能去解读。

在 (3) 中，一组概念取得了完整的计算表征：符号集的意图含义以计算形式被完整刻画，例如用可在机器上运行的数学逻辑来写。人对概念仍可能有未被逻辑语言完整捕捉的直觉，但这属于应予纠正的缺陷或疏漏。

按这三类划分本体，只是理解其用法的框架，并非互斥的刚性分类。比如，一个严格用计算性数学逻辑实现的本体，也可以供人裁决术语分歧，而不用于支配软件系统的行为。

## 2. 历史

信息科学采用的本体论观念植根于哲学史，可上溯至“波菲利之树”（指 3 世纪希腊新柏拉图主义者、提尔的波菲利：Franklin 1986）[^franklin-1986]。当时用树这种抽象结构来展示概念间的关系。

这种抽象结构此后成为描绘本体区分的主导图式，从林奈（1758）的生物分类学一直用到今天。中世纪大量关于范畴的写作都是对亚里士多德著作的评注（参见中世纪范畴词条）。中世纪以后，范畴编目逐渐摆脱对亚里士多德的依附；科学方法兴起，又带动了在自然科学中定义范畴的兴趣，林奈的著作即其例。

另有一项较少人知却格外值得注意的努力，早于林奈：约翰·威尔金斯 1685 年那部卷帙浩繁的《论一种真实字符与哲学语言》（Subbiondo 1992）[^subbiondo-1992]。书中用数百页篇幅铺开一棵单一的概念树，每个概念都带自然语言定义。其中不少内容（如生物范畴）只有历史意义，但有些创新已预示了逻辑函数在本体定义中的现代用法，例如把“手套”视为一种函数，指称覆盖身体某一部位的衣物。尤其值得注意的是，他不只以分类法呈现概念，还配了一套书面与口头语言，让这些范畴进入语法，以构成一种更完善、免于歧义的语言（Eco 1995）[^eco-1995]。

弗雷格与皮尔士（参见弗雷格词条、皮尔士的演绎逻辑词条）为现代数学逻辑奠基之前，本体中的概念都不外乎用自然语言非形式地定义。因此在现代计算机出现以前，只有人能处理本体。

在计算机科学采用“本体”一词之前，人工智能（AI）界长期用形式逻辑以及受逻辑启发的系统（如 Prolog：Clocksin & Mellish 2003）[^clocksin-2003]来定义概念。逻辑理论汇编（Farquhar, Fikes, & Rice 1997）[^farquhar-1997]显示，一般概念的许多逻辑定义可以写成文档；但当时这些概念尚未整合，无法合入单一而一致的理论中共同使用。

另一条知识表示路线也见于某些信息科学本体，即语义网络（Woods 1975; Lehmann 1992；另见计算语言学词条“表征主义进路”一节）[^lehmann-1992][^woods-1975]。它又称知识图谱，常实现于图数据库（Robinson, Webber, & Eifrem 2015）[^robinson-2015]，由一组带标签的节点与弧按图排列，陈述实体间的关系。此路数在 1970 年代的 AI 中一度流行，到 2020 年代再度流行。

20 世纪 70—80 年代盛行的专家系统，大概是最早使用计算性本体的系统，只是当时还没有这个名称。但若把“一组符号加上某种定义这些概念的符号语言”所构成的计算产品算作本体，那么这类系统确实含有本体。Mycin（Buchanan & Shortliffe 1985）[^buchanan-1985]、Prospector（Duda, Gaschnig, & Hart 1979）[^duda-1979]以及许多专家系统都在 70 与 80 年代陆续开发出来。

语义网络与一阶逻辑是 AI 中最早的两大知识表示范式，也是“整洁派”与“邋遢派”之争（Crevier 1993; Poirier 2024; Gonçalves & Cozman 2021）[^crevier-1993][^gonçalves-2021][^poirier-2024]的标本：知识表示要不要形式化的数学？整洁派主张推理须有坚实理论基础；邋遢派则认为系统“能用”即可，完成任务不必有理论支撑。这场争论呼应了关于 **经验论** 是否成立的更大论辩（参见逻辑经验论词条）。及至 90 年代中期，计算机科学界开始意识到：一批命名概念本身便是资源，其价值在某种程度上不取决于具体用途。

专家系统的知识工程难题还有一条回应，早于“本体”一词进入计算机科学，即 Cyc 项目（Lenat & Guha 1989）[^lenat-1989]。Cyc 是商业项目，构想为支撑 AI 应用的常识知识库，也是迄今规模最大的尝试：在计算系统中用表达力强的逻辑汇集概念与定义。当时人们已经认识到，本体研究的一个重要方向是“上层本体论”（见第 3 节），即许多领域都可能需要、且可共同持有的一组概念。最早依此构想的上层本体有：建议上层合并本体论（SUMO：Niles & Pease 2001; Pease 2011）[^niles-2001][^pease-2011]、面向语言与认知工程的描述性本体论（DOLCE：Gangemi, Guarino, Masolo, Oltramari, & Schneider 2002）[^gangemi-2002]与基本形式本体论（BFO：Arp, Smith, & Spear 2015; Smith, Grenon, & Goldberg 2004）[^arp-2015][^smith-2004]，此后继起的还有很多（见下文“其他网络资源”中的上层本体链接）。本体语言与新的本体同步演化：专家系统或实现于 Prolog（Clocksin & Mellish 2003）[^clocksin-2003]，或实现于 Clips（Riley, Culbert, Savely, & Lopez 1987）[^riley-1987]、OPS5（Brownston, Farrell, Kant, & Martin 1985）[^brownston-1985]这类“外壳”。有些本体用可执行的语言定义，借助它们能回答问题或检验一致性。针对各类数学逻辑的定理证明语言，表达力逐级抬升：一阶逻辑（Sutcliffe & Suttner 1998）[^sutcliffe-1998]、带类型一阶逻辑（Sutcliffe, Schulz, Claessen, & Baumgartner 2012）[^sutcliffe-2012]、模态逻辑（Raths & Otten 2012）[^raths-2012]、高阶逻辑（Benzmüller, Rabe, & Sutcliffe 2008）[^benzmüller-2008]，并在自动定理证明器上落地（Sutcliffe 2010）[^sutcliffe-2010]。知识交换格式（KIF：Genesereth & Fikes 1992）[^genesereth-1992]与本体网络语言（OWL）族等描述逻辑语言（Bechhofer et al. 2004）[^bechhofer-2004]，则是专为支撑本体而开发的。

## 3. 领域本体论与上层本体论

**上层本体论** 是一组不针对任何特定应用领域的概念。一个概念是否属于上层本体，并没有客观标准，只能在同一本体内部相对于其他术语来判定。有些上层本体力求精简，只收少量最一般的概念；有些则从最一般一路收到较专门的概念。许多领域本体是作为上层本体的扩展建成的：上层本体从“一切事物”这个类起步，逐层细化，为物理事物与抽象事物、关系与函数等添上范畴（有时还附定义）。不过，上层本体到领域本体的分界是人为划定的。领域本体不会从“一切事物”类开始作范畴分解；但许多并不扩展上层本体的领域本体，仍需少数极一般的范畴，例如物理对象或过程。

什么算一个领域，取决于视角，也取决于实践者的目标。用于防止药物不良相互作用的某个应用（Zhao, Yin, Zhang, Zhang, & Chen 2023）[^zhao-2023]，涉及药物化学的概念可能不多；用于支持药物合成的应用，则可能完全没有“药物相互作用”这一概念。反过来，一个关于药物的更一般本体，可能两者兼备甚至更多，但药物编目未必详尽。

现存的领域本体在数量上远超上层本体（见下文“其他网络资源”中的本体链接）。

## 4. 本体论承诺

一个本体应当承诺什么，又该把什么留而不论？倘若本体论承诺（参见本体论承诺词条）应当尽量少，那就可以只承诺“实体”与“关系”两个范畴，别无他词。只有两个概念的最小本体几乎不作任何承诺，可它描述世界、帮助各方建立共同概念与定义的用处也几乎为零。这里有一处明显张力：既不愿许下会把本体限死在少数狭窄语境的承诺，又希望承诺尽量多，以便促成共识。

但在本体中创建并定义一个概念，是否必然构成承诺？这要看定义怎么作。试看一强一弱两个例子。若断言 $\exists x \: \text{unicorn}(x)$，这就作了一个多半既强又不明智的承诺。若断言 $\forall x \: (\text{unicorn}(x) \implies \exists y \: (\text{horn}(y) \land \text{part}(y,x)))$，则只是作了一种较弱、多半无害的承诺：后一公式仅承诺 **若** 有独角兽存在，它便长角。就一个未必被设定存在的想象实体规定其性状，这是相当弱的承诺。在计算性本体（以及更广的哲学讨论）中，本体论承诺的实践问题，归结为理论是否不假，即是否与用软件应用有效建模世界相容。一个本体不必能建模世间一切知识，才配得上实际用处。于是问题变成：某一本体在多大程度上排斥有用的世界模型，又在多大程度上支撑各种模型的定义。也可以只关心那些会排除其他合理承诺的承诺。若本体作了明显糟糕的建模选择，例如要求地球是平的，便犯了 **作为之误**，排除了它的许多可能用途。若概念或范畴太少、定义太少，建模能力便有限；回避对建模所需概念的承诺（例如省略空间或时间关系，或省略建模时间与行动的手段），则犯了 **不作为之误**。什么都不说，自然不会说错。难处在于：尽可能多地对世界有所陈述，同时不说假话。

承诺选择的一个例子（参见随时间同一性词条）是延存论与持续论之争：对象有没有时间部分，这些部分又如何相关（Haslanger & Kurtz 2006）[^haslanger-2006]？可是，关于部分关系或同一性的单一观念，是否非得在诸替代方案中择一（参见相对同一性词条）？对象的属性可以变，同一性却可以不变。形式本体不只产出计算上有用的产品，还开出一间实验室，供我们探究自己如何看待世界。人或许会设想不同观点或理论相冲突；但在所采用的逻辑中拿不出形式证明时，对建模选择之冲突的担忧，至多只是未经检验的假设。反过来，若证明了逻辑矛盾，便有数学依据断言该冲突真实存在，并可着手调和。举例说，人们可能非形式地假定同一性必含不可分辨性（参见不可分辨者的同一性词条）（对所有属性 $F$，$\forall F(Fx \leftrightarrow Fy \implies x=y)$）；但除非把这一本体论承诺写成公理——写进自动定理证明器或其他推理系统能执行的代码——它只是一种可能的不良选择，实践中已被绕开。

若一个本体承诺每一实体都在空间与时间中占有一席之地，便排除了数这类无时间实体。若一个本体承诺物理事物（在空间与时间中占位）与抽象事物（不在空间或时间中占位）之别，则只是备下了可用的建模设施。它并未许下会排除世界某一重要方面或观点的承诺。

力求本体论承诺最小，与希望本体只含最小一套原语，出于同一种愿望。究竟需要多少概念？概念数目有上限吗？以人类语言为参照，答案似乎是否定的：表达新概念的新词不断被造出来。“智能手机”“自拍”都是为表达原先不存在的概念而造。当然也可以拿现成的词凑个近似说法，例如“我把我的——那种带触摸屏、又能当电话使的小型计算机——从兜里掏了出来”；可这样说话效率极低，还会丢掉“智能手机”这个现代词的许多含义。人固然可以在交流中临时把每个概念都定义一遍，以免 **先验地** 承诺一堆带定义的词；同样，也可以从小套原语出发，逐步搭出本体的术语集合——但每当新术语与定义显得需要，就把它们存档，效率更高。

支持“原语宜少”的一条论据是：小集合比大集合好学好记。这里可以借用现代软件开发的教训。计算机初兴时还没有可复用的软件库；如今大型库已是现代开发不可或缺的环节。重复发明通用抽象并不划算。通用抽象之多，使现代编程语言有数以万计的函数可供复用；没有哪个程序员需要把函数全学会，项目里没用到的函数也不会碍事——编译器不会把它们编进可运行的程序。可复用组件能加快开发，也能提高系统间的兼容性。再打一个比方：一页纸容得下的英语词典，论统一词义之功用，远不及《韦氏词典》（Merriam-Webster 2003）[^merriam-webster-2003]或《牛津英语词典》（Oxford English Dictionary 2020）[^oxford-2020]这样的大型词典。

## 5. 按理论要素看本体论

有些本体关心顶层或一般范畴（常称“上层本体论”），而不针对某一领域特有概念（见第 3 节）。它们的清册大体相近：要有物理实体与抽象实体、实体与对象、过程、属性、各类数，并把它们定义清楚，以组织概念空间，尽量给抽象留出余地。波菲利之树（见第 2 节）也提供了 **种差** 的范例，即说明每个概念如何区别于其他概念。一个概念若未经区分，在本体里不过是别的概念的同义词。本体学者的第一关，就是学会写这类描述，并拒斥一切给不出精确种差的候选概念。

所有著名上层本体都至少含有下列关于概念的某种版本：

* 物/实体——一切事物的类。
* 物理——在空间与时间中占位的一切事物的类。
* 过程/行动/事件——*发生* 之事的类。
* 对象/物理物——*存在* 之物的类，即可触知的实体。
* 材料/质料——可细分而仍保持同一性的事物的类（参见物质名词词条）。
* 物理对象/微粒对象——不可细分而仍保持同一性的事物的类。
* 抽象/不可触物——不在空间与时间中占位的事物的类。
* 关系——实体之间关系的类。
* 性质/属性。
* 函数——函数关系的类：对关系中每一元素或元素的每一唯一组合，都有唯一的另一元素与之对应。

关系汇编则少见得多。少数几类关系（如传递关系类）直接内置在语义网社群所用的本体网络语言（OWL）里，而非在本体语言中定义，因为 OWL 表达不了这一性质。其余常见的关系类别有对称、自反、反对称等。

某些本体中常见的关系如下：

* 物理部分/“具有”——一个物理实体把另一个物理实体当作物理部分，如门有门把手、车有车轮（参见分体论词条）。
* 时间部分——一个事件或过程把另一事件或过程当作父过程的一部分（参见时间部分词条）。
* 物理位置——某物位于某一区域或另一对象之处（参见位置与分体论词条）。
* 子类/“是”——一类事物比另一类更专门。
* 实例——一个个体实体是某个类的成员。
* 格角色（Fillmore 1968; Gisborne & Donaldson 2019）[^fillmore-1968][^gisborne-2019]，如施事、受事、工具等。
* 事件间的时间关系（如 Allen 1984）[^allen-1984]：先于、相接、居于……期间、开始于等。

## 6. 按逻辑语言看本体论

被称为本体的东西大多以某种形式语言陈述，但也有一些并不使用带形式（数学）语义的语言。本质上是词汇表的本体，只收集词语与自然语言定义；人必须亲自阅读，消解歧义，再推断它们如何用于具体问题。拼写或语法检查器能帮忙写这类文档，但机器或数学过程无从判定诸定义是否彼此冲突。自然语言本体正因这些短处，才促使人们改用形式语言来建本体。

本体中最简单的形式语言是分类法与图形语言。分类法里，自动化唯一能查出的是成环：$A$ 是 $B$ 的父节点（可能经传递），反之亦然。分类法的形式语义是：子节点所指概念比父节点更专门，即 $\forall x : \text{child-class}(x) \implies \text{parent-class}(x)$。

最简单的图语言由命名节点与弧组成。图除“某些关系成立”外没有内在形式语义，最简可写作 $G = (V,E)$，即由顶点与边构成；但通常还会有一套可复用的边标签（关系）$R$，且不应有与任何东西都不相连的“孤儿”节点——$G = (V,E,R)$，并满足：

$$\forall x \in V : \exists r,y: x r y \land r \in R \land y \in V.$$

随后可用某种元语言为特定节点与弧符号给出形式语义，例如规定“PhysicalPart”弧具有传递性。但许多知识图谱与语义网络并无形式化刻画，只在某个软件系统里实现。须注意：软件实现不等于形式语义。语义是数学构造，独立于任何实现而存在。程序可以执行数学所蕴含的限制；同一套语义，不同的程序也可以用不同办法实现。

描述逻辑是一阶逻辑的子集，其创立意在提供一种推理可判定的逻辑语言：像命题逻辑那样可判定，但表达力更强。一阶逻辑只是半可判定的——矛盾能在有限时间内发现，却无法保证定理证明器能在有限时间内判定“无矛盾”。发现矛盾这件事至关重要，因为计算上最高效的自动定理证明系统正是靠反证法工作的。

不过，OWL 的一些变体超出了描述逻辑，既失去严格可判定性，又不支持标准一阶逻辑全部内容（Baader et al. 2007）[^baader-2007]。一阶自动定理证明亦有相当进展，可避开最坏情形的不可判定（Geoff Sutcliffe & Desharnais 2024）[^sutcliffe-2024][^sutcliffe-2024-2]。故而在“用哪种逻辑解决哪类问题”上，实践者意见分歧。

OWL 族这类描述逻辑（Baader, Horrocks, & Sattler 2005）[^baader-2005][^horrocks-2005]把一些关键词纳入逻辑，而这些关键词的定义要靠元语言给出，因为描述逻辑本身道不尽它们的语义。OWL 在定义自身语言时，必须动用一阶逻辑来陈述其中部分关键词的语义。此外 OWL 还配有 SWRL 语言（Horrocks, Patel-Schneider, Bechhofer, & Tsarkov 2005）[^horrocks-2005]，为描述逻辑补上表达规则的能力。保留 SWRL 语义的一种实现，走一阶逻辑定理证明器（Tsarkov, Riazanov, Bechhofer, & Horrocks 2004）[^bechhofer-2004][^tsarkov-2004]；另一些实现用 Drools 规则引擎（见“其他网络资源”），而它是产生式系统，不是逻辑（Shapiro 2001）[^shapiro-2001]，因而丢掉了 SWRL 的部分语义。

以更强语言（一阶逻辑或更高）定义的本体较少见（显眼的例外是 SUMO（Niles & Pease 2001; Pease 2011）[^niles-2001][^pease-2011]与 Cyc（Lenat 1995）[^lenat-1995]）。逻辑表达力越强，能就概念陈述的东西越多，可供机器推理的余地也越大：或用本体回答问题，或检验其一致性。举例说，在命题逻辑里可以取命题项 $S =$“苏格拉底是人”与 $M =$“苏格拉底会死”，断言 $S \implies M$；但这样一来，得为每个人（最好还为每个生物）都断言一次这层蕴含。到了谓词演算，一条更一般的规则只须写一次：

$$\forall x \: \text{Organism}(x) \implies \text{Mortal}(x)$$

以及

$$\forall x \: \text{Man}(x) \implies \text{Organism}(x).$$

再往上走到一阶逻辑之外，就可以只写一次传递性公理，让它对“传递关系”类型的一切实例普遍成立，无须为每种此类关系重复一遍。逻辑语言越有表达力，编码知识、形成概括就越省力；因此，任何本体规模的度量，都必须把所计公式的逻辑表达力一并算进去。

本体语言及其可用的推理机还有一个问题：逻辑语言支不支持数与算术。度量与度量化的时间都在世界里，可极少有本体采用能与“会算数”的推理系统配套的逻辑。SNARK（Waldinger et al. 2004）[^waldinger-2004]是这样一个推理机，自带语言。带算术的 TPTP 类型化一阶形式（TFA：Sutcliffe, Schulz, Claessen, & Baumgartner 2012）[^sutcliffe-2012]是另一种语言，由少数定理证明器实现，如 iProver（Korovin 2008）[^korovin-2008]与 Vampire（Kovács & Voronkov 2013）[^kovács-2013]。

用表达力较弱的逻辑实现本体，会把更多定义留给直觉与解释。这类本体可用于人与人之间的术语标准化，再由人在软件中落实这些概念：人得确保程序正确使用概念并体现其本意。若本体作者同时是软件作者，实现多半合于本意；但旁人若拿该本体去支配自己的软件，理解就可能不同，这是个风险。系统规模一大，或长期使用下去，风险更甚。没有自动化来保证解释一致，要让大家对概念含义保持同样的直觉，就越发困难。

人很容易把自己的知识或解释当成别人的。Newton1990 就是个好例子：仅凭节奏辨认一段旋律有多难，提供节奏的人要意识到自己给的信息不够，也同样难。本体学者可能以为，一个标签或一句自然语言描述就足以约束符号的解释；但没有详细的形式刻画，旁人给出另一种解释实在容易。刻画越细、越形式化，就越可能避免彼此冲突的解释。

对于确有基于分类法或图语言的本体实现的系统，开发者可以用过程式代码给概念加约束，如流行的 Java 或 Python；也可以选更具声明性的辅助语言，如 Prolog、SWRL 或 Clips。

用表达力较弱的逻辑语言，好处是计算效率高。描述逻辑可判定，查询必定终止；一阶逻辑只半可判定，拿不出满足查询的证明时，查询可能不终止；高阶逻辑的性能保证更少。不过，避开推理的理论最坏情形已有相当进展（Sutcliffe & Desharnais 2023）[^sutcliffe-2023]，即便在大规模理论上性能也有提升（Pease, Sutcliffe, Siegel, & Trac 2010）[^pease-2010][^sutcliffe-2010]。再者，为满足特定应用的性能限制，可以轻易把表达力强的公式从本体中撤下，同时仍把它们作为一套术语定义保留，用以统一人的理解。

## 7. 本体论的评估

由无利害关系的第三方对本体作客观评估的情形很少，Mascardi, Cordi, & Rosso 2007 是其中一例，但评的是上层本体，不是一般本体。若干客观度量如下：

* 是否采用数学逻辑，若采用，是哪一种。逻辑语言的选择决定了每个概念的定义中哪些方面可形式表达，哪些只能以非形式的自然语言注释补足。
* 该逻辑是否已落成计算系统，例如配了自动定理证明器或推理引擎。不少带形式语义的逻辑并未为计算而实现。若本体以未实现的逻辑定义（且规模不小），就无从验证它无矛盾；要提问，也只能靠人算出结果。
* 用了哪种自动推理机（如果有）来验证公式，验证又有什么局限。描述逻辑推理机（如 FaCT++（Tsarkov & Horrocks 2006）[^tsarkov-2006]或 Pellet（Sirin, Parsia, Grau, Kalyanpur, & Katz 2007）[^sirin-2007]）能保证 OWL 本体中不出现类型冲突。一阶推理机能检验一阶逻辑的本体，可陈述的内容多于描述逻辑，但一阶逻辑半可判定，故不保证找出全部冲突。一阶模型发现器只要找到模型便保证一致，但受模型发现器本身的局限，只宜分析规模较小的公式集合。高阶逻辑定理证明器能尝试验证弱表达力逻辑写不出的更多陈述，可这类系统的性能使它们更不易找出可能存在的全部矛盾。
* 概念数量，可再细分为实例、类与关系。
* 公式数量及其类型，即是否
* 为基公式（不含任何变量）
* 蕴含或析取的数目
* 含给定元数关系的公式数（图与描述逻辑限于二元关系）
* 需要某一表达力水平的公式数，例如：
* 命题逻辑（无变量）
* 描述逻辑（分类/类型推理）
* 一阶逻辑（只对词项量化）
* 模态逻辑（以及具体用了哪些模态算子与支撑公理）
* 高阶逻辑（对公式量化）
* 含数与/或算术表达式的公式数

有些本体为术语准备了词法映射，例如映射到 WordNet（Fellbaum 1998）[^fellbaum-1998]，可用一种或多种人类语言；于是可以度量词法映射有多少条、覆盖多少种语言。

上述各项度量，其余条件相同时，可以说是多多益善。

也可以就非技术特征作评估，例如流行度、工具支持、标准符合度或许可方式。人们还常主张，本体必须合乎对某一总体哲学原则的某种解读。所援引的原则不一：实在论（参见实在论词条）、后现代主义与相对主义（参见相对主义词条）、实证主义（参见逻辑经验论与奥古斯特·孔德词条）。

## 8. 本体论与大语言模型

大语言模型（Jurafsky & Martin 2000）[^jurafsky-2000]是语言的模型，不是世界的模型（Bender, Gebru, McMillan-Major, & Shmitchell 2021）[^bender-2021]。大语言模型生成的文本明显违背人类对世界的认识时，人们颇带拟人色彩地称之为“幻觉”。对此提出的一条对策，是用 **神经—符号** 进路把大语言模型与逻辑推理结合起来（Hitzler & Sarker 2021）[^hitzler-2021]：既可用符号表述的知识训练大语言模型（Chattopadhyay, Dandekar, & Roy 2025）[^chattopadhyay-2025]，也可把符号知识写进提示词（Lewis et al. 2020）[^lewis-2020]。大语言模型还能用来对齐术语本体（Hertling & Paulheim 2023）[^hertling-2023]。

这一方向的大部分工作，所用本体以知识图谱表述。这样做有可能促使大语言模型遵循分类关系这类事实、成本或数量这类度量，或物理部分关系这类简单关系。若改用表达力强的逻辑所定义的本体，大语言模型便有望遵循世界中更复杂的关系；至于如何实现，尚待观察。

## 9. 本体论的应用

本体可以只用作确保概念共识的工具，也可以用于推理，或两者兼用。关于本体应用的综述有 Qaswar et al. 2022; Poli, Healy, & Kameas 2010; Uschold & Jasper 1999 等。许多本体是作为独立产品开发的，充当词汇标准，并非某个运行中系统的组成部分；也有许多本体在应用中只由其作者使用，用以展示其价值，并非为了解决某个具体应用需求。

本体在应用中的用途包括检索（Suomela & Kekäläinen 2005）[^suomela-2005]、自然语言处理（Bateman, Hois, Ross, & Tenbrink 2010; Behr, Völkenrath, & Kockmann 2023）[^bateman-2010][^behr-2023]、物联网（Qaswar et al. 2022）[^qaswar-2022]与工程（Zheng et al. 2021）[^zheng-2021]。生物学是本体开发投入甚多的应用领域（Stevens & Lord 2009; Kramer & Beißbarth 2017）[^kramer-2017][^stevens-2009]。这类本体的实现常为数据库，把此类产品称作本体，出自作者的视角，并非产品本身有何特征。

## 10. 未来方向

本体论仍有广阔的用武之地，尤其是为世界的各个侧面构建越来越庞大、越来越形式化的理论。计算机科学中本体论最一般层面的研究，已开始受惠于与所谓 **计算形而上学** 的合作（Kirchner, Benzmüller, & Zalta 2019; Fitelson & Zalta 2007）[^fitelson-2007][^kirchner-2019]。Casati & Varzi 1999 与 Casati & Varzi 1994 等工作，把物理世界的某些方面形式化，展示了可以在计算上实现的完整形式公理化。

把物理世界某一侧面的本体形式化，目前似乎还没有可用的计算理论；这方面有一项基础工作可作例子，即关于实体或类实体行动的理论：它要说明：在某一分解层次上，材料的某部分具备哪些性质时，整体也具备这些性质。例如，行走的一个时间切片何时不再算行走，而只是一个迈步、一次运动？蛋糕的一块何时不再是蛋糕，而成为一个糖分子？要靠什么关系或概念来陈述这些粒度界限，并确定整体的性质如何为部分所具有？一个类的粒度在多大程度上也适用于它的子类？

“能力问题”这一观念为评估本体的计算能力指出了一个方向（Wiśniewski, Potoniec, Ławrynowicz, & Keet 2019; Bezerra, Freitas, & Santana da Silva 2013）[^bezerra-2013][^wiśniewski-2019]。该研究方向试图汇集可以向本体提出的问题，据以衡量其知识程度。难处在于：汇成一个覆盖面广的问题语料库，还要找到检验办法，又不至于让本体只为应付测试而写。Cohen et al. 1998 是一个大体采此进路的大型项目。

描述逻辑虽是本体最广泛使用的一族语言，日后的工作却可能越来越多地采用表达力更强的逻辑；OWL 逻辑族本身也在逐步纳入表达力更强的语言。自动定理证明社群一直在为表达力更强的逻辑制定标准，并在定理证明器中实现（Sutcliffe 2024）[^sutcliffe-2024][^sutcliffe-2024-2]；本体领域的更多项目或可从中获益。

## 参考文献

**以下文献从原文照录，不作翻译；中国文献条目（古今）一律译为中文。**

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

[^allen-1984]: Allen, James, 1984, “Towards a General Theory of Action and Time,” *Artificial Intelligence*, 23: 123–154.
[^arp-2015]: Arp, Robert, Barry Smith, and Andrew D. Spear, 2015, *Building Ontologies with Basic Formal Ontology*, Cambridge, MA: MIT Press.
[^baader-2007]: Baader, Franz, Diego Calvanese, Deborah L. McGuinness, Daniele Nardi, and Peter F. Patel-Schneider (eds.), 2007, *The Description Logic Handbook*, 2nd edition, Cambridge: Cambridge University Press.
[^baader-2005]: Baader, Franz, Ian Horrocks, and Ulrike Sattler, 2005, “Description Logics as Ontology Languages for the Semantic Web,” in Dieter Hutter & Werner Stephan (eds.), *Mechanizing Mathematical Reasoning: Essays in Honor of Jörg H. Siekmann on the Occasion of his 60th Birthday*, pp. 228–248, Berlin, Heidelberg: Springer. doi:10.1007/978-3-540-32254-2_14
[^bateman-2010]: Bateman, John A., Joana Hois, Robert Ross, and Thora Tenbrink, 2010, “A Linguistic Ontology of Space for Natural Language Processing,” *Artificial Intelligence*, 174(14): 1027–1071. doi:10.1016/j.artint.2010.05.008
[^bechhofer-2004]: Bechhofer, Sean, Frank van Harmelen, Jim Hendler, Ian Horrocks, Deborah McGuinness, Peter Patel-Schneijder, and Lynn Andrea Stein, 2004, *OWL Web Ontology Language Reference* (W3C Recommendation), Mike Dean & Guus Schreijber (eds.), World Wide Web Consortium (W3C).
[^behr-2023]: Behr, Alexander S., Marc Völkenrath, and Norbert Kockmann, 2023, “Ontology Extension with NLP-Based Concept Extraction for Domain Experts in Catalytic Sciences,” *Knowledge and Information Systems*, 65(12): 5503–5522. doi:10.1007/s10115-023-01919-1
[^bender-2021]: Bender, Emily M., Timnit Gebru, Angelina McMillan-Major, and Shmargaret Shmitchell, 2021, “On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?” in *Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency*, pp. 610–623, New York: Association for Computing Machinery. doi:10.1145/3442188.3445922
[^benzmüller-2008]: Benzmüller, Christoph, Florian Rabe, and Geoff Sutcliffe, 2008, “THF0 – the Core of the TPTP Language for Higher-Order Logic,” in Alessandro Armando, Peter Baumgartner, & Gilles Dowek (eds.), *Automated Reasoning*, pp. 491–506, Berlin, Heidelberg: Springer.
[^bezerra-2013]: Bezerra, Camila, Fred Freitas, and Filipe Santana da Silva, 2013, “Evaluating Ontologies with Competency Questions,” in *2013 IEEE/WIC/ACM International Joint Conferences on Web Intelligence (WI) and Intelligent Agent Technologies (IAT)*, pp. 284–285. doi:10.1109/WI-IAT.2013.199
[^brownston-1985]: Brownston, Lee, Robert Farrell, Elaine Kant, and Nancy Martin, 1985, *Programming Expert Systems in OPS5: An Introduction to Rule-Based Programming*, Reading, MA: Addison-Wesley.
[^buchanan-1985]: Buchanan, Bruce G., and Edward H. Shortliffe (eds.), 1985, *Rule-Based Expert Systems: The MYCIN Experiments of the Stanford Heuristic Programming Project*, Reading, MA: Addison-Wesley.
[^casati-1994]: Casati, Roberto, and Achille C. Varzi, 1994, *Holes and Other Superficialities*, Cambridge, MA: MIT Press.
[^casati-1999]: –––, 1999, *Parts and Places: The Structures of Spatial Representation*, Cambridge, MA: MIT Press.
[^chattopadhyay-2025]: Chattopadhyay, Aniruddha, Raj Dandekar, and Kaushik Roy, 2025, “Learning and Reasoning with Model-Grounded Symbolic Artificial Intelligence Systems,” in Leilani H. Gilpin, Eleonora Giunchiglia, Pascal Hitzler, & Emile van Krieken (eds.), *Proceedings of the 19th International Conference on Neurosymbolic Learning and Reasoning*, Vol. 284, pp. 957–976, PMLR. [[Chattopadhyay et al. 2025 available online](https://proceedings.mlr.press/v284/chattopadhyay25a.html)]
[^clocksin-2003]: Clocksin, William F., and Christopher S. Mellish, 2003, *Programming in Prolog*, 5th edition, Berlin, Heidelberg: Springer. doi:10.1007/978-3-642-55481-0
[^cohen-1998]: Cohen, Paul, Robert Schrag, Eric Jones, Adam Pease, Albert Lin, Barbara Starr, David Gunning, Murray Burke, 1998, “The DARPA High Performance Knowledge Bases Project,” *AI Magazine*, 19(4).
[^crevier-1993]: Crevier, Daniel, 1993, *AI: The Tumultuous History of the Search for Artificial Intelligence*, New York: Basic Books, Inc.
[^dallwitz-1980]: Dallwitz, M. J., 1980, “A General System for Coding Taxonomic Descriptions,” *Taxon*, 29(1): 41–46.
[^duda-1979]: Duda, R. O., J. Gaschnig, and P. E. Hart, 1979, “Model Design in the PROSPECTOR Consultant Program for Mineral Exploration,” in D. Michie (ed.), *Expert Systems in the Microelectronic Age*, pp. 153–167, Edinburgh: Edinburgh University Press.
[^eco-1995]: Eco, Umberto, 1995, *The Search for the Perfect Language [Ricerca della lingua perfetta nella cultura europea]*, Oxford: Blackwell.
[^enderton-1972]: Enderton, Herbert Bruce, 1972, *A Mathematical Introduction to Logic*, New York: Academic Press.
[^farquhar-1997]: Farquhar, Adam, Richard Fikes, and James Rice, 1997, “The Ontolingua Server: A Tool for Collaborative Ontology Construction,” *International Journal of Human-Computer Studies*, 46(6): 707–727. doi:10.1006/ijhc.1996.0121
[^fellbaum-1998]: Fellbaum, Christiane (ed.), 1998, *WordNet: An Electronic Lexical Database*, Cambridge, MA: MIT Press.
[^fillmore-1968]: Fillmore, Charles J., 1968, “The Case for Case,” in Emmon Bach & Robert T. Harms (eds.), *Universals in Linguistic Theory*, pp. 0–88, New York: Holt, Rinehart, & Winston.
[^fitelson-2007]: Fitelson, Branden, and Edward N. Zalta, 2007, “Steps Toward a Computational Metaphysics,” *Journal of Philosophical Logic*, 36(2): 227–247. doi:10.1007/s10992-006-9038-7
[^franklin-1986]: Franklin, James, 1986, “Aristotle on Species Variation,” *Philosophy*, 61(236): 245–252.
[^gangemi-2002]: Gangemi, Aldo, Nicola Guarino, Claudio Masolo, Alessandro Oltramari, and Luc Schneider, 2002, “Sweetening Ontologies with DOLCE,” in Asunción Gómez-Pérez & V. Richard Benjamins (eds.), *Knowledge Engineering and Knowledge Management: Ontologies and the Semantic Web: 13th International Conference, EKAW 2002 Sigüenza, Spain, October 1–4, 2002 Proceedings*, pp. 166–181, Berlin, Heidelberg: Springer. doi:10.1007/3-540-45810-7_18
[^genesereth-1992]: Genesereth, M. R., and R. E. Fikes, 1992, *Knowledge Interchange Format, Version 3.0 Reference Manual* (No. Logic-92-1), Stanford, CA: Stanford University. [[Genensereth & Fikes 1992 available online](http://logic.stanford.edu/publications/genesereth/kif.pdf)]
[^gisborne-2019]: Gisborne, Nikolas, and James Donaldson, 2019, “Thematic Roles and Events,” in Robert Truswell (ed.), *The Oxford Handbook of Event Structure*, pp. 236–264, Oxford: Oxford University Press.
[^gonçalves-2021]: Gonçalves, Bernardo, and Fabio Gagliardi Cozman, 2021, “The Future of AI: Neat or Scruffy?” in *Intelligent Systems: 10th Brazilian Conference, BRACIS 2021, Virtual Event, November 29 – December 3, 2021, Proceedings, Part II*, pp. 177–192, Berlin, Heidelberg: Springer. doi:10.1007/978-3-030-91699-2_13
[^gruber-1993]: Gruber, Thomas R., 1993, “A Translation Approach to Portable Ontology Specifications,” *Knowledge Acquisition*, 5(2): 199–220. doi:10.1006/knac.1993.1008
[^haslanger-2006]: Haslanger, Sally Anne, and Roxanne Marie Kurtz (eds.), 2006, *Persistence: Contemporary Readings*, Cambridge, MA: MIT Press.
[^hertling-2023]: Hertling, Sven, and Heiko Paulheim, 2023, “OLaLa: Ontology Matching with Large Language Models,” in *Proceedings of the 12th Knowledge Capture Conference 2023*, pp. 131–139, New York, NY: Association for Computing Machinery. doi:10.1145/3587259.3627571
[^hitzler-2021]: Hitzler, Pascal, and Md. Kamruzzaman Sarker, 2021, “Neuro-Symbolic Artificial Intelligence: The State of the Art,” in *Neuro-Symbolic Artificial Intelligence*, Thousand Oaks, CA: Sage. [[Hitzler & Sarker 2021 available online](https://www.gbv.de/dms/tib-ub-hannover/1786636506.pdf)]
[^horrocks-2005]: Horrocks, Ian, Peter F. Patel-Schneider, Sean Bechhofer, and Dmitry Tsarkov, 2005, “OWL Rules: A Proposal and Prototype Implementation,” *Journal of Web Semantics*, 3(1): 23–40. doi:10.1016/j.websem.2005.05.003
[^jurafsky-2000]: Jurafsky, Daniel, and James H. Martin, 2000, *Speech and Language Processing: An Introduction to Natural Language Processing, Computational Linguistics, and Speech Recognition*, 1st edition, Upper Saddle River, PA: Prentice Hall.
[^kaliyar-2015]: Kaliyar, Rohit Kumar, 2015, “Graph Databases: A Survey,” in Abhishek Swaroop & Vishnu Sharma (eds.), *International Conference on Computing, Communication and Automation (ICCCA-2015)*, pp. 785–790, Curran Assoc. doi:10.1109/CCAA.2015.7148480
[^kirchner-2019]: Kirchner, Daniel, Christoph Benzmüller, and Edward N. Zalta, 2019, “Computer Science and Metaphysics: A Cross-Fertilization,” *Open Philosophy*, 2(1): 230–251. doi:doi:10.1515/opphil-2019-0015
[^korovin-2008]: Korovin, Konstantin, 2008, “iProver – an Instantiation-Based Theorem Prover for First-Order Logic (System Description),” in Alessandro Armando, Peter Baumgartner, & Gilles Dowek (eds.), *Automated Reasoning*, pp. 292–298, Berlin, Heidelberg: Springer.
[^kovács-2013]: Kovács, Laura, and Andrei Voronkov, 2013, “First-Order Theorem Proving and Vampire,” in *Proceedings of the 25th International Conference on Computer Aided Verification*, Vol. 8044, pp. 1–35, New York, NY: Springer. doi:10.1007/978-3-642-39799-8_1
[^kramer-2017]: Kramer, Frank, and Tim Beißbarth, 2017, “Working with Ontologies,” in *Methods in Molecular Biology*, 1525: 123–135, Berlin, Heidelberg: Springer. doi:10.1007/978-1-4939-6622-6_6
[^lehmann-1992]: Lehmann, F., 1992, *Semantic Networks in Artificial Intelligence*, Amsterdam: Elsevier Science Inc.
[^lenat-1995]: Lenat, D., 1995, “Cyc: A Large-Scale Investment in Knowledge Infrastructure,” *Comm. ACM*, 38(11).
[^lenat-1989]: Lenat, Douglas B., and R. V. Guha, 1989, *Building Large Knowledge-Based Systems; Representation and Inference in the Cyc Project*, 1st edition, USA: Reading, MA: Addison-Wesley.
[^levine-2017]: Levine, S. J., and K. Lateef-Jan, 2017, *Untranslatability Goes Global*, Abingdon: Routledge.
[^lewis-2020]: Lewis, Patrick, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman Goyal, Heinrich Küttler, Mike Lewis, Wen-tau Yih, Tim Rocktäschel, Sebastian Riedel, and Douwe Kiela, 2020, “Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks,” in H. Larochelle, M. Ranzato, R. Hadsell, M. F. Balcan, & H. Lin (eds.), *Advances in Neural Information Processing Systems*, Vol. 33, pp. 9459–9474, Red Hook, NY: Curran Associates, Inc. [[Lewis et al. 2020 available online](https://proceedings.neurips.cc/paper_files/paper/2020/file/6b493230205f780e1bc26945df7481e5-Paper.pdf)]
[^linnaeus-1758]: Linnaeus, Carl von, 1758, *Systema naturae per regna tria naturae: secundum classes, ordines, genera, species, cum characteribus, differentiis, synonymis, locis*, Vol. V.1, Stockholm: Salvius. [[Linnaeus 1758 available online](https://archive.org/details/mobot31753000798865/page/n1/mode/2up)]
[^lu-2019]: Lu, Jie, Anjin Liu, Fan Dong, Feng Gu, João Gama, and Guangquan Zhang, 2019, “Learning Under Concept Drift: A Review,” *IEEE Transactions on Knowledge and Data Engineering*, 31(12): 2346–2363. doi:10.1109/TKDE.2018.2876857
[^magne-2017]: Magne, Matthew, 2017, “Data Drift Happens: 7 Pesky Problems with People Data,” *InformationWeek*, July 19. [[Magne 2017 available online](https://www.informationweek.com/data-management/data-drift-happens-7-pesky-problems-with-people-data)]
[^mascardi-2007]: Mascardi, V., V. Cordi, and P. Rosso, 2007, “A Comparison of Upper Ontologies,” in Matteo Baldoni, Antonio Boccalatte, Flavio De Paoli, Maurizio Martelli, & Viviana Mascardi (eds.), *Proceedings of WOA 2007*, pp. 55–64, Torino: Seneca.
[^merriam-webster-2003]: Merriam-Webster, 2003, *Merriam-Webster’s Collegiate Dictionary*, 11th edition, Springfield, MA: Merriam-Webster.
[^newton-1990]: Newton, L., 1990, *Overconfidence in the Communication of Intent: Heard and Unheard Melodies*, Ph.D. Thesis, Stanford, CA: Stanford University.
[^niles-2001]: Niles, Ian, and Adam Pease, 2001, “Toward a Standard Upper Ontology,” in Chris Welty & Barry Smith (eds.), *Proceedings of the 2nd International Conference on Formal Ontology in Information Systems (FOIS-2001)*, pp. 2–9, New York: Association for Computing Machinery.
[^oxford-2020]: Oxford English Dictionary, 2020, *OED Online*, Oxford: Oxford University Press. [[OED available online](https://www.oed.com/)]
[^pancha-2016]: Pancha, Girish, 2016, “Big Data’s Hidden Scourge: Data Drift,” *CMSWire*, April 8. [[Pancha 2016 available online](https://www.cmswire.com/big-data/big-datas-hidden-scourge-data-drift/)]
[^pease-2011]: Pease, Adam, 2011, *Ontology: A Practical Guide*, Angwin, CA: Articulate Software Press.
[^pease-2010]: Pease, Adam, Geoff Sutcliffe, Nick Siegel, and Steven Trac, 2010, “Large Theory Reasoning with SUMO at CASC,” *AI Communications, Special Issue on Practical Aspects of Automated Reasoning*, 23(2–3): 137–144.
[^poirier-2024]: Poirier, Lindsay, 2024, “Neat vs. Scruffy: How Early AI Researchers Classified Epistemic Cultures of Knowledge Representation,” *IEEE Annals of the History of Computing*, PP(99): 1–29. doi:10.1109/MAHC.2024.3498692
[^poli-2010]: Poli, Roberto, Michael Healy, and Achilles Kameas, 2010, *Theory and Applications of Ontology: Computer Applications*, Berlin, Heidelberg: Springer.
[^qaswar-2022]: Qaswar, Fahad, M. Rahmah, Muhammad Ahsan Raza, A. Noraziah, Basem Alkazemi, Z. Fauziah, Mohd. Khairul Azmi Hassan, and Ahmed Sharaf, 2022, “Applications of Ontology in the Internet of Things: A Systematic Analysis,” *Electronics*, 12(1), 111. doi:10.3390/electronics12010111
[^raths-2012]: Raths, Thomas, and Jens Otten, 2012, “The QMLTP Problem Library for First-Order Modal Logics,” in Bernhard Gramlich, Dale Miller, & Uli Sattler (eds.), *Automated Reasoning*, pp. 454–461, Berlin, Heidelberg: Springer.
[^riley-1987]: Riley, Gary, Chris Culbert, Robert T. Savely, and Frank Lopez, 1987, “CLIPS: An Expert System Tool for Delivery and Training,” in J. S. Denton, M. S. Freeman, & M. Vereen (ed.), *Third Conference on Artificial Intelligence for Space Applications – Part I*, pp. 53–57, NASA. [[Riley et al. 1987 available online](https://ntrs.nasa.gov/api/citations/19880006986/downloads/19880006986.pdf)]
[^robinson-2015]: Robinson, Ian, Jim Webber, and Emil Eifrem, 2015, *Graph Databases*, 2nd edition, Beijing: O’Reilly.
[^rumbaugh-2004]: Rumbaugh, James, Ivar Jacobson, and Grady Booch, 2004, *Unified Modeling Language Reference Manual*, 2nd edition, Pearson Higher Education.
[^shapiro-2001]: Shapiro, Stuart C., 2001, “Review of ”Knowledge Representation: Logical, Philosophical, and Computational Foundations“ by John F. Sowa,” *Computational Linguistics – COLI*.
[^sirin-2007]: Sirin, Evren, Bijan Parsia, Bernardo Cuenca Grau, Aditya Kalyanpur, and Yarden Katz, 2007, “Pellet: A Practical OWL-DL Reasoner,” *Web Semant.*, 5(2): 51–53. doi:10.1016/j.websem.2007.03.004
[^smith-2004]: Smith, Barry, Pierre Grenon, and Louis Goldberg, 2004, “Biodynamic Ontology: Applying Bfo in the Biomedical Domain,” *Studies in Health and Technology Informatics*, 102: 20–38.
[^stevens-2009]: Stevens, Robert, and Phillip Lord, 2009, “Application of Ontologies in Bioinformatics,” in Steffen Staab & Rudi Studer (eds.), *Handbook on Ontologies*, pp. 735–756, Berlin, Heidelberg: Springer.
[^subbiondo-1992]: Subbiondo, Joseph L. (ed.), 1992, *John Wilkins and 17th-Century British Linguistics*, Amsterdam: John Benjamins.
[^suomela-2005]: Suomela, Sari, and Jaana Kekäläinen, 2005, “Ontology as a Search-Tool: A Study of Real Users’ Query Formulation With and Without Conceptual Support,” in David E. Losada & Juan M. Fernández-Luna (eds.), *Advances in Information Retrieval*, pp. 315–329, Berlin, Heidelberg: Springer.
[^sutcliffe-2010]: Sutcliffe, Geoff, 2010, “The TPTP World – Infrastructure for Automated Reasoning,” in Edmund M. Clarke & Andrei Voronkov (eds.), *Logic for Programming, Artificial Intelligence, and Reasoning*, pp. 1–12, Berlin, Heidelberg: Springer.
[^sutcliffe-2024]: –––, 2024, “Stepping Stones in the TPTP World,” in C. Benzmüller, M. Heule, & R. Schmidt (eds.), *Proceedings of the 12th International Joint Conference on Automated Reasoning*, pp. 30–50, Berlin, Heidelberg: Springer.
[^sutcliffe-2023]: Sutcliffe, Geoff, and Martin Desharnais, 2023, “The 11th IJCAR Automated Theorem Proving System Competition – CASC-J11,” *AI Communications*, 36(2): 73–91.
[^sutcliffe-2024-2]: –––, 2024, “The CADE-29 Automated Theorem Proving System Competition – CASC-29,” *AI Communications*, 37(4): 485–503. doi:10.3233/AIC-230325
[^sutcliffe-2012]: Sutcliffe, Geoff, Stephan Schulz, Koen Claessen, and Peter Baumgartner, 2012, “The TPTP Typed First-Order Form with Arithmetic,” in Nikolaj Bjørner & Andrei Voronkov (eds.), *Logic for Programming, Artificial Intelligence, and Reasoning* (LPAR 2012), pp. 406–419, Berlin, Heidelberg: Springer.
[^sutcliffe-1998]: Sutcliffe, Geoff, and Christian Suttner, 1998, “The TPTP Problem Library,” *J. Autom. Reason.*, 21: 177–203, Berlin, Heidelberg: Springer. doi:10.1023/A:1005806324129
[^tsarkov-2006]: Tsarkov, Dmitry, and Ian Horrocks, 2006, “FaCT++ Description Logic Reasoner: System Description,” in *Proceedings of the Third International Joint Conference on Automated Reasoning*, pp. 292–297, Berlin, Heidelberg: Springer. doi:10.1007/11814771_26
[^tsarkov-2004]: Tsarkov, Dmitry, Alexandre Riazano, Sean Bechhofer, and Ian Horrocks, 2004, “Using Vampire to Reason with OWL,” in Sheila A. McIlraith, Dimitris Plexousakis, & Frank van Harmelen (eds.), *The Semantic Web – ISWC 2004*, pp. 471–485, Berlin, Heidelberg: Springer.
[^uschold-1999]: Uschold, Mike, and Jasper, Robert, 1999, “A Framework for Understanding and Classifying Ontology Applications,” in Richard Benjamins (ed.) *Proceedings of the IJCAI-99 Workshop on Ontologies and Problem-Solving Methods (KRR5)*, Vol. 2, Amsterdam: CEUR.
[^waldinger-2004]: Waldinger, Richard, Douglas E. Appelt, John Fry, David Israel, Peter Jarvis, David Martin, Susanne Riehemann, Mark E. Stickel, Mabry Tyson, Jerry Hobbs, and Jennifer Dungan, 2004, “Deductive Question Answering from Multiple Resources,” in Mark Maybury (ed.), *New Directions in Question Answering*, pp. 253–262, Berlin, Heidelberg: Springer.
[^wiśniewski-2019]: Wiśniewski, Dawid, Jedrzej Potoniec, Agnieszka Ławrynowicz, and C. Maria Keet, 2019, “Analysis of Ontology Competency Questions and Their Formalizations in SPARQL-OWL,” *Journal of Web Semantics*, 59 (100534). doi:10.1016/j.websem.2019.100534
[^woods-1975]: Woods, W. A., 1975, “What’s in a Link: Foundations for Semantic Networks,” in D. G. Bobrow & A. M. Collins (eds.), *Representation and Understanding: Studies in Cognitive Science*, pp. 35–82, New York: Academic Press.
[^zhao-2023]: Zhao, Yan, Jun Yin, Li Zhang, Yong Zhang, and Xing Chen, 2023, “Drug–Drug Interaction Prediction: Databases, Web Servers and Computational Models,” *Briefings in Bioinformatics*, 25(1): bbad445. doi:10.1093/bib/bbad445
[^zheng-2021]: Zheng, Xiaochen, Jinzhi Lu, Rebeca Arista, Xiaodu Hu, Joachim Lentes, Fernando Ubis, Jyri Sorvari, and Dimitris Kiritsis, 2021, “Development of an Application Ontology for Knowledge Management to Support Aircraft Assembly System Design,” in Emilio M. Sanfilippo, Oliver Kutz, Nicolas Troquard, et al. (eds.), *JOWO*, Volume 2969, CEUR-WS.org. [[Zheng et al. 2021 available online](https://ceur-ws.org/Vol-2969/paper21-FOMI.pdf)]

## 学术工具

* [如何引用本词条](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=ontology-is)。
* [预览本词条的 PDF 版本](https://leibniz.stanford.edu/friends/preview/ontology-is/)，见 [SEP 学会之友](https://leibniz.stanford.edu/friends/)。
* 在 [InPhO](https://www.inphoproject.org/entity?sep=ontology-is&redirect=True) 查找与本词条相关的话题与思想家。
* 在 [PhilPapers](https://philpapers.org/sep/ontology-is/) 查看本词条的增强文献目录及其数据库链接。

## 其他网络资源

* [上层本体论](https://en.wikipedia.org/wiki/Upper_ontology)，维基百科条目。
* [本体论](https://github.com/semantalytics/awesome-semantic-web?tab=readme-ov-file#ontologies)，GitHub 资源集。
* [资源描述框架](https://www.w3.org/RDF/)，见 www.w3.org。
* [Drools 规则引擎](https://www.drools.org)。

## 相关词条

逻辑与本体论 | 本体论承诺 | 自然语言本体论

**（译注：相关词条的中文站内链接将由管线在对应词条重译完成后统一挂接。）**

## 致谢

作者感谢 Stephan Schulz 与各位匿名审稿人的细致审读，本词条因之改进。
