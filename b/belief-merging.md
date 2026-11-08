# 信念合并与判断聚合 Belief Merging and Judgment Aggregation (Gabriella Pigozzi)

*首次发表于 2015 年 7 月 8 日；2025 年 6 月 9 日实质修订。*

群体往往须做决定，而决定可能颇为复杂，牵涉对若干相互关联问题的评估。例如，在大学里，招聘委员会通常要依据候选人的教学与研究素质斟酌人选。一个面临建桥决定的市议会，可能要求其成员表明赞成与否，并同时给出各自立场的理由（如经济与环境影响，抑或支出上的考量）。最后，陪审员须裁断被告的责任，方法是依相关法典为本案所规定的诸项条件表达判断。正如 Kornhauser 与 Sager（1986）论及真实的陪审团审判时所指出的，个体对逻辑上彼此关联诸命题的意见一旦聚合，便可能导致一种悖论性结果，即所谓的教义悖论。受法理学中这一教义悖论的启发，判断聚合问题引来政治学家、哲学家、逻辑学家、经济学家与计算机科学家的关注。与社会选择理论的关联表明，与偏好聚合问题（Arrow 1951/1963; Sen 1970）[^arrow-1951][^sen-1970] 相仿，不存在同时满足若干理想性质的判断聚合程序。

判断聚合要回答的问题是：如何界定那些能在集体层面保住个体理性的聚合程序。自哲学上看，这一问题关涉群体态度（如群体信念）的本性（Roth 2011）[^roth-2011]。市议会决定建桥时，该决定所依据的是个体的信念——例如相信桥会积极促进本地区经济活动的开展，且不构成环境威胁。于是，判断聚合的形式进路有助于阐明个体信念与集体信念之间的依赖关系（假若确有集体信念的话）。判断聚合所处理的问题，同样关涉社会认识论所研究的证言问题（Goldman 1999, 2004, 2010）[^goldman-1999]。专家小组里彼此相左的意见应当如何合并？理性的行动者又该如何回应这种分歧？

合并可能相互冲突的信息，并不只在人群须作决定时才成为问题。人工智能同样在探索如何将相互冲突的传感器信息、专家意见或数据库聚合为融贯的数据库（Bloch et al. 2001）[^bloch-2001]。异质传感器信息的合并可补单个传感器之短，提高整个系统的性能，其例见于智能手机中的手势识别、屏幕旋转与加速度计。分布式数据库有时须被同时访问与管理以共享数据；例如医院需要调取不同科室为病人采集的数据。互联网用户则能在各在线平台上看到已购用并品评过该产品者给出的评分。待合并的信息类型各不相同，其表示因而可以是数值的或符号的：数、语言值、统计概率分布、二元偏好、效用函数等。然而上举各例所处理的，都是合并来自异质来源的条目并管理冲突这一回事。在纯形式层面，信念合并所研究的，是把以命题逻辑表达、彼此独立而同等可靠的信息源融为一炉。与判断聚合一样，信念合并要处理的问题，是把若干以命题逻辑表达的个体基集融合成融贯的一个。既然两个学科所探究的问题在结构上相类，考察其间的联系便可看出这两套形式系统究竟有多相似。较实用地说，把信念合并所界定的算子施于判断聚合问题，便产生更宽的一类判断聚合算子，即所谓的基于距离的程序。

本词条的自趣，在于把判断聚合与信念合并这两支文献之间的联系明确勾画出来。下一节将简述判断聚合；欲求更全面的导论，读者可参阅（Grossi and Pigozzi 2014; Endriss 2016）[^endriss-2016][^grossi-2014]。

## 1. 判断聚合

判断聚合的形式研究，肇端于法理学文献中的“教义悖论”（Kornhauser and Sager 1986, 1993, 2004; Kornhauser 1992）[^kornhauser-1992][^kornhauser-1986]。据该悖论，法官在谋求一个共同而有证成的裁决时，确有可能陷入集体非理性。这一学科虽诞生未久，结构相类的问题却似乎早由 Poisson 在 1837 年点出（见 Elster 2013 所述）[^elster-2013]，其后意大利法学家 Vacca 于 1921 年亦有论及（见 Spector 2009）[^spector-2009]。

在 Kornhauser 与 Sager 所举的法庭案例（1993）里，一个三人法庭须裁决原告与被告之间的违约纠纷。依照合同法，被告须负违约责任（命题 *r*），当且仅当合同禁止被告做某行为 *X*（命题 *p*）而被告确已做了行为 *X*（命题 *q*）。假设三位法官的判断如表 1 所示。

*表 1：*

|   | 义务（*p*） | 行为（*q*） | 被告负有责任（*r*） |
| --- | --- | --- | --- |
| 法官 1 | 真 | 真 | 真 |
| 法官 2 | 真 | 假 | 假 |
| 法官 3 | 假 | 真 | 假 |
| 多数 | 真 | 真 | 假 |

表 1：教义悖论

命题 *r* 是结论，*p* 与 *q* 则是前提。这条法律教义因而可逻辑地写作 $(p\land q)\leftrightarrow r$，意谓前提 *p* 与 *q* 同为结论 *r* 的充要条件。表 1 显示每位法官都守着这条教义：唯有当她把两个前提都判为真时，才把结论判为真。倘若法官们就每一命题的判断按多数规则聚合其个体意见，得到的判断集便是 {*p*, *q*, 非 *r*}，这违反了法律教义。教义悖论即在此：各个人虽在逻辑上融贯，群体就诸命题下的判断却与法律教义不相容。上例中，法官们无法一面宣告被告不负责任，一面又声称其责任的两项条件俱已具备。法庭于是进退两难。要么只让法官就前提表态，法庭关于 *r* 的决定由前提上的多数逻辑地推得（基于前提的程序，亦称逐议题程序）；要么径以关于 *r* 的多数判断定谳（基于结论的程序，亦称逐案程序），前提上的意见一概不问。表 1 这类实例说明，两种程序可以得出相反的结论。在法庭一例中，法官须表态的议题被分作前提与结论。然而应当指出，判断聚合理论并不需要这种区分。纵不区分前提与结论，宣告被告不负责任的法庭决定（尽管多数赞成宣告其责任的两项判准）依旧与决定规则 $(p \land q) \leftrightarrow r$ 相违。

以多数规则界定集体结果而落得悖论，这并不是头一回。早在 1785 年，孔多塞侯爵便发现了如今称作孔多塞悖论的现象。给定一组个体偏好，若将各备选方案逐一成对比较并施行多数投票，集体结果中就可能出现非传递的偏好（或循环）：*x* 优于 *y*，*y* 优于 *z*，*z* 又优于 *x*，以致无法判任何备选方案为胜者。孔多塞悖论与判断聚合悖论之间的相似，很快被 Kornhauser 与 Sager（1986）及 List 与 Pettit（2004）察觉。个体偏好聚合成社会偏好排序的研究，是社会选择理论的中心课题（List 2013）[^list-2013]。诺贝尔奖得主 Kenneth Arrow 证明了这一划时代的结果：孔多塞偶然撞见的问题具有更大的普遍性，并不限于多数规则。阿罗不可能定理（Arrow 1951/1963; Morreau 2014）[^arrow-1951][^morreau-2014] 断言，给定三个或更多备选方案上的有限个体偏好集，没有任何聚合函数能同时满足若干看似合理的公理。与阿罗定理相仿的结果不少，它们都表明判断聚合的“不可能”。判断聚合的第一条不可能定理（List and Pettit 2002）[^list-2002][^list-2002-2] 之后，又有种种推广（Pauly and van Hees 2006; Dietrich 2006; Mongin 2008）[^dietrich-2006][^mongin-2008][^pauly-2006]。

此处仅把注意力局限于以命题逻辑语言 *L* 表述的判断之聚合（判断聚合问题亦可推广至模态逻辑、条件逻辑和谓词逻辑，见 Dietrich 2007；关于非古典逻辑与判断聚合的深入讨论，见 Grossi 2009、Porello 2017、Xuefeng 2018）[^dietrich-2007][^grossi-2009][^porello-2017][^xuefeng-2018]。个体借以表达判断的公式集，称为议程 $(A\subseteq L$）。议程不含双重否定（$\neg \neg \varphi$ 与 $\varphi$ 等价），对否定封闭（即若 $\varphi \in A$，则 $\neg \varphi \in A$ 亦在其中），且一般被假定不含重言式与矛盾式。例如，法庭一案的议程为 $A = \{p, \neg p, q, \neg q, p \wedge q, \neg (p \wedge q)\}$。Dietrich 与 List（2007a）证明：只要议程足够丰富（譬如法庭决定的议程，或 $\{p, \neg p, q, \neg q, p \to q, \neg (p \to q)\}$），能满足下文各项要求的判断聚合规则便只有独裁制一种。所谓独裁的聚合函数，指对任何输入，集体结果都取某一个（且始终同一个）个体即独裁者的判断；独裁者之外的一切个体输入均被弃置不顾。判断集是议程内一个融贯而完备的公式集 $J \subseteq A$。所谓完备，是指对议程的任一元素 $\varphi$，或 $\varphi\in A$ 或 $\neg \varphi\in A$（议程每一事项非受即拒）。给定由 *n* 个个体组成的群体，剖面即 *n* 元组的个体判断集 $\langle J_1, \ldots, J_n \rangle$。判断聚合规则 *F* 则是这样的函数：为每个剖面 $\langle J_1, \ldots, J_n\rangle$ 指派一个集体判断集 $F(J_1, \ldots, J_{n}) \subseteq A$。加于 *F* 的条件有如下几条：

**普遍域：** 凡由融贯、且相对于议程完备的判断集所成之剖面，皆可作为聚合函数的输入被接受。表 1 中教义悖论的那个剖面便是合法输入：法官们就议程上每一议题均表态接受或拒绝，且其意见守住了规则 $(p \wedge q) \leftrightarrow r$。

**集体理性：** 可作为输出被接受的，只有完备而融贯的集体判断。表 1 一例中的集体判断虽完备（群体对议程各项非接受即拒绝），却不融贯——它违反了规则 $(p \wedge q) \leftrightarrow r$。

**独立性：** 就每一命题而言，集体判断只依赖于个体对该命题的判断，不依赖于议程中其他（被视作独立的）命题。（此条件在判断聚合框架内重述了阿罗偏好聚合定理中的无关备选方案独立性条件。）逐命题的多数规则（如表 1 的法庭例子）即满足独立性：群体对议程某一事项的接受或拒绝，取决于多数个体是否接受或拒绝了该命题。

**全体一致保持：** 倘若全体个体对某一命题 *p*$\in$ *A* 的判断一致，则此判断必收入集体判断集。

这些条件看似并不苛求，然而可以证明：凡同时满足上述诸条件的判断聚合规则 *F*，无一不是独裁制。此一不可能结果格外意味深长——一旦把它改述于偏好框架之中，便可证明阿罗定理（就严格偏好排序而言）是它的一个推论（Dietrich and List 2007a）[^dietrich-2007a]。Dietrich 与 List 由此断言，判断聚合可视作比偏好聚合更为普遍的问题（此类改述的细节见 Grossi and Pigozzi 2014）[^grossi-2014]。

除了两类聚合问题之间的形式关联，自概念上看，判断聚合还把偏好聚合的问题扩展到更为一般的决策问题上去。社会选择所提供的模型诚然加深了我们对选举、公投、立法表决等熟悉集体决策问题的了解，但其着眼点主要在候选人、政策、行动等备选结果之间的集体取舍。它们刻画不了一整类决策问题——在这类问题里，群体须就逻辑上彼此关联的命题形成集体认可的信念或判断。可是，如导论诸例所示，这类决策问题并不罕见，也不限于法庭裁决。Pettit（2001）铸造了论辩困境一词，正为点明：只要一群人须就多个命题达成共同立场，此种问题便可能浮现。

不可能结果常带一层否定色彩，但它们同时也标出了突围的路径。放宽普遍域条件，或把集体理性条件弱化为仅要求集体判断融贯（而不必完备），都能取得融贯的集体结果。前者的例子是只考虑单向对齐的剖面（List 2002）[^list-2002][^list-2002-2]，此条件与偏好聚合中布莱克的单峰性相仿（Black 1948）[^black-1948]。放宽独立性条件亦可得可能性结果。法庭案例中那个基于前提的程序，便是违背独立性的聚合规则之一例：关于结论的集体立场，凭前提上的多数判断经逻辑蕴涵推得。更一般地，序列优先规则违背独立性却能保证群体立场融贯：议程诸元素依一预先固定的次序聚合，先前决定约束后续决定。判断聚合的详尽导论、更多不可能定理以及逃出此类结果的出路综述，读者可参阅（List and Puppe 2009; List 2013; Grossi and Pigozzi 2014; Endriss 2016）[^endriss-2016][^grossi-2014][^list-2013][^list-2009]。下一节介绍计算机科学中处理合并冲突信息的方式。我们将会看到，信念合并所引入的某些算子，恰是违反独立性条件的聚合程序之实例；而借这类算子，可以为判断聚合问题得出具体的聚合程序。

## 2. 信念合并

计算机科学家早已研究如何把若干独立且可能彼此冲突的信息源聚合成一个融贯的整体。如导论所举，此类例子有：智能体所接收的相互冲突的传感器信息之合并、为建造专家系统而对多个数据库的聚合，以及多智能体系统（Borgida and Imielinski 1984; Baral et al. 1992; Chawathe et al. 1994; Elmagarmid et al. 1999; Subrahmanian 1994; Kim 1995）[^baral-1992][^borgida-1984][^chawathe-1994][^elmagarmid-1999][^kim-1995][^subrahmanian-1994]。信念合并（或融合）所研究者，是把以命题逻辑表达的符号信息聚合为一个融贯的基。下文将显示，合并数个基的过程与信念变化（或曰信念修正）关系密切；后者自 1980 年代以来一直是形式哲学与计算机科学中的活跃课题，用意在于模拟人与人工智能体遇到新信息时如何改易其信念。修正是 Alchourrón、Gärdenfors 与 Makinson（即通常所称 AGM 理论）所辨析的三种主要理论变化之一，其余两种为扩充与收缩，他们并为三者各立合理性公设（Alchourrón et al. 1985; Gärdenfors 1988）[^alchourrón-1985][^gärdenfors-1988]。信念修正所关注者，是一个信念基在遭遇全新的、完全可靠的信息时如何变化——这条新信息可能与基中原有信念相抵牾。假如我听说新相识的 Rob 有个孩子，我径直把这信息添入，进而推出新的后果，这便是扩充。真正有趣的情形，则是新信息与旧信念相冲突。设我从一位共同的朋友处听出 Rob 并无子女，如今又听 Rob 亲口说他有孩子。为容纳这一新信息，我须作一次修正：剔除“他没有孩子”这一错误信念（连同可能依赖它的其他信念），加入“他确有一子”这一新输入，再推出可能的新后果（综述见 Hansson 2011，全面导论见 Fermé and Hansson 2018）[^fermé-2018][^hansson-2011]。与信念修正相仿，合并中“知识”一词的用法比认识论文献宽泛：它指智能体所接受的公式（即其知识库中的公式），未必为真。据此，“知识库”与“信念基”两名可互易使用。Grégoire 与 Konieczny（2006）认为，信念合并算子亦可用以聚合知识与信念之外的信息，如目标、观察与规范。

信念修正所关注者，是单一基在新信息添入后如何变化；信念融合要处理的，则是如何把若干各不相同且可能彼此冲突的基（如不同专家的意见、若干数据库、来自不同渠道的情报等）聚合起来，求得一个融贯的基。文献中提出的进路不止一种。以下先略述组合与仲裁，再转入 Konieczny 与 Pino Pérez 所界定、并已施用于判断聚合的合并算子。第一条进路所针对者，是聚合互不相同、可能彼此不一致的数据库（Baral et al. 1991; Baral et al. 1992）[^baral-1991][^baral-1992]。它承袭 Ginsberg 的主张：面对不一致的理论，应当考虑极大融贯子集（Ginsberg 1986）[^ginsberg-1986]；这里的理论，可以是由若干各自融贯、彼此却相冲突的智能体的信息取并而成。组合算子取诸知识库（有限逻辑公式集）之并，若并集在逻辑上不一致，再挑出若干极大融贯子集。这类组合算子的逻辑性质，已在（Konieczny 2000）[^konieczny-2000]中详考，并与（Konieczny and Pino Pérez 1998, 1999）[^konieczny-1998]界定的合并算子相较。组合与合并知识库，其间差别不止一端。其一，Baral 等人（1991, 1992）的方法依于句法，合并算子则恪守句法无涉原则。依句法无涉原则，对两个等价知识库施以运算，所得仍应是两个等价的知识库。比如 $K_1 = \{a, b\}$ 与 $K_{2}= \{a \wedge b\}$ 具有相同的逻辑后承。那么，取 $K_3 = \{\neg b\}$，把 $K_1$ 与 $K_3$ 合并，或把 $K_2$ 与 $K_3$ 合并，都会得到两个等价的知识库。反过来，$K_1$ 与 $K_3$ 的组合却未必与 $K_2$ 与 $K_3$ 的组合逻辑等价。令 $E_1 = K_1 \bigsqcup K_3$（$\bigsqcup$ 表示多重集求并）、$E_2 = K_2 \bigsqcup K_3$。$E_1$ 的极大融贯子集是 $\{a, b\}$ 与 $\{a, \neg b\}$，$E_2$ 的则是 $\{a \wedge b\}$ 与 $\{\neg b\}$。可见 $E_1$ 的每个极大融贯子集都蕴涵 $a$，而 $E_2$ 的极大融贯子集并非尽皆如此（此例取自 Konieczny 2000）[^konieczny-2000]。其二，使用组合算子时，知识库来源的信息被弃置不顾；这即是说，组合算子不像合并那样能顾到基数上的轻重。设四位医学专家就四种疫苗对 65 岁以上者的效力发表意见。令命题 $a, b, c, d$ 分别表示“疫苗 A（依次为 B、C、D）对 65 岁以上者有效”。若两位专家同认疫苗 A 与 B 对 65 岁以上者有效，一位专家以为疫苗 D 有效（而疫苗 A 无效），末一位专家与前两位一样认疫苗 A 有效，并认为若 B 对 65 岁以上者有效则 C 亦有效，四位专家的意见可表为四个知识库：$K_1 = K_{2}= \{a, b\}$、$K_{3}= \{\neg a, d\}$ 与 $K_4 = \{a, b\rightarrow c\}$。四基之并为 $\{a,\neg a, b, b\rightarrow c, d\}$，显然逻辑上不一致。取极大融贯子集，正是既避开不一致、又尽量多存信息的办法。本例的两个极大融贯子集是：$\{a, b,b\rightarrow c, d\}$ 与 $\{\neg a, b, b\rightarrow c, d\}$。也就是说，究竟该接受 *a* 还是 $\neg a$，我们无从判定。但多数知识库含 *a*，只有一个基含 $\neg a$。只要诸知识库一视同仁，直觉上所得的知识库就应含 *a*。倘若出于某种缘由 $K_{3}$ 比其余知识库更可信，那么我们也许宁可选取接受 $\neg a$ 的组合基。

融合知识库尚有另一类算子，即仲裁，其提出亦在九十年代初期（Revesz 1993, Liberatore and Schaerf 1995）[^liberatore-1995][^revesz-1993]。信念修正一般假定新信息必被接受，且须收进修正后的基。仲裁所处理的却是另一番局面：两个来源各执一词，而可靠程度不分高下（例如两位能力相若的专家、两名同样可信的证人）。既无理由舍其一，办法便不是以一个去修正另一个，而是把两个基融合起来。此项运算称作仲裁，是因为两个来源既然同等可靠，所得之基就应尽量兼收两者之长。Liberatore 与 Schaerf（1995）曾为两个信念基之间的仲裁立下公理，Revesz 的算子只满足其中数条。其方案之弊，在于仅能仲裁两个基。信念合并进路弥补了这一缺陷：有限多个基皆可合并为融贯的一个。

上述诸法皆不能顾及某一信息条目之受众多寡，因而那些算子都抓不住多数的意见。首倡为知识库合并设立多数公设者，是 Lin 与 Mendelzon（1999），其构思得自社会选择理论中的多数规则。不过他们的多数公设含有一个“部分支持”概念，用以标明知识合并在这一方面不同于投票：它并不止于清点支持命题 *a* 的基与含 $\neg a$ 的基孰多孰少。所谓一个知识库部分支持文字 *l*，是指存在某个命题 *a*，其中不出现 *l* 所含的任何原子，而该智能体相信 *l* 为真或 *a* 为真，却不知究系哪一个。Lin 与 Mendelzon（1999）给出了这些公设的模型论刻画以及若干具体合并算子。信念合并文献一般假定诸信息源可靠程度相同。化解冲突的一条途径，便是松动这一假定，譬如（Lin 1996）[^lin-1996][^lin-1996-2]将合并扩展至加权知识库，或转向优先知识库（Benferhat et al. 1998; Cholvy 1998; Delgrande et al. 2006）[^benferhat-1998][^cholvy-1998][^delgrande-2006]。

Konieczny 与 Pino Pérez（1998）厘定了一套新的合并算子公设，并依算子所满足的公理，辨明仲裁算子与多数算子之别。其后续工作（Konieczny and Pino Pérez 1999, 2002）[^konieczny-1999]又把框架推及完整性约束下的合并——所谓完整性约束，即一组自外部施加、合并后的基必须满足的条件（Kowalski 1978; Reiter 1988）[^kowalski-1978][^reiter-1988]。下节介绍 Konieczny 与 Pino Pérez 的形式框架；此框架因其弥补了先前诸说的短处，如今已是信念合并的标准框架。

信念合并所发展的形式方法，业已移植并施用于社会认识论的若干领域：选举与偏好聚合（Meyer et al. 2001）[^meyer-2001]、群体共识（Gauwin et al. 2005）[^gauwin-2005]，以及判断聚合（Pigozzi 2006）[^pigozzi-2006]——后者留待第 2.2 节再述。

### 2.1 完整性约束下合并的框架

Konieczny 与 Pino Pérez 所设的命题语言 *L*，由有限原子命题集 *At* 与通常联结词 $(\neg, \land, \lor , \rightarrow, \leftrightarrow )$ 生成。所谓解释，是把 0（假）或 1（真）指派给每一原子命题的全函数 $At \rightarrow \{0, 1\}$。举例说，若 $At =\{p, q, r\}$，那么 $(1, 0, 1)$ 这一解释便把真赋给 *p* 与 *r*、把假赋给 *q*。[^note-1] 一切解释之集记作 $W = \{0, 1\}^{At}$。任取公式 $\varphi \in L$，$\mymod(\varphi) = \{\omega \in W | \omega \models \varphi\}$ 即 $\varphi$ 的模型集，也就是使 $\varphi$ 成真的真值指派之集。试取表达教义之例中合同法的公式，则 $\mymod((p\land q) \leftrightarrow r) = \{(1,1,1), (1, 0, 0), (0, 1, 0), (0,0,0)\}.$ 按惯例，公式 $\varphi$ 只要至少有一个模型便是融贯的；而若使 $\Phi$ 中所有公式为真的每一解释都使 $\varphi$ 为真，则 $\varphi$ 可由公式集 $\Phi$ 推出。

信念基 $K_i$ 是一个有限的命题公式集，代表个体 *i* 所明白持有的信念。诸 $K_{i}$ 皆假定为融贯。一切融贯信念基之集记作 $\mathcal{K}$。合并公设所处理的，是信念基的多重集（信念剖面，早期论文则称信念集）$E = \{K_1, \ldots , K_{n}\}$。之所以用多重集，是因为其中元素可以重复出现，从而能够表示两个乃至更多智能体持有相同信念这一情形；唯其如此，才能顾及某项信息的受众之多寡，进而界定多数算子。为区别于通常的集合并 $\cup$，多重集之并记作 $\sqcup$，其定义为 $\{\varphi\} \sqcup \{\varphi\} = \{\varphi, \varphi\}$。两个信念剖面等价 $(E_1\equiv E_{2})$，当且仅当存在由 $E_1$ 到 $E_{2}$ 的双射 *f*，使得对任一 $B\in E_1$ 都有 $\models\land f(B)\leftrightarrow \land B$。

完整性约束所表示者，乃合并后诸基理应推出的额外条件；其用意在于保证个体信息条目的聚合能满足某一问题的特定要求。设市议会成员须决定在某个片区兴建何物。此时既可有预算上的约束（款额只够覆盖其中部分项目），也可有关于各项目能否并存的约束（该片区或不容停车场与游乐场并建，却容许游乐场与公共图书馆并建）。若以信念基 *IC* 记完整性约束之集（此集可为空集），则 $\Delta_{\IC}(E)$ 便表示在 *IC* 之下合并信念基多重集 *E* 所得的结果。直观地说，这结果将是一个融贯的信念基，既代表集体信念，又蕴涵 *IC*。

Konieczny 与 Pino Pérez（1999, 2002）就同等可靠来源之间的 *IC* 融合算子，立有如下公设。设 $E$, $E_1$, $E_{2}$, 为信念剖面，$K_1$, $K_{2}$ 为融贯信念基，$\IC$, $\IC_1$, $\IC_{2}$, 为完整性约束。$\Delta$ 是 *IC* 融合算子，当且仅当它满足下列合理性公设：

**(IC0)**

$\Delta_{\IC}(E) \models \IC$

**(IC1)**

若 $\IC$ 融贯，则 $\Delta_{\IC}(E)$ 亦融贯。

**(IC2)**

倘 $\land E$ 与 *IC* 相容，则 $\Delta_{\IC}(E)\equiv \land E\land \IC$

**(IC3)**

若 $E_1\equiv E_{2}$ 且 $\IC_1\equiv \IC_{2}$，则 $\Delta_{\IC_1}(E_1)\equiv \Delta_{\IC_2}(E_{2})$

**(IC4)**

若 $K_1 \models\IC$ 且 $K_{2} \models\IC$，则 $\Delta_{\IC}(\{K_1, K_{2}\})\land K_1$ 融贯，当且仅当 $\Delta_{\IC}(\{K_1, K_{2}\})\land K_{2}$ 融贯。

**(IC5)**

$\Delta_{\IC}(E_1) \land \Delta_{\IC}(E_{2}) \models\Delta_{\IC}(E_1\sqcup E_{2})$

**(IC6)**

倘 $\Delta_{\IC}(E_1) \land \Delta_{\IC}(E_{2})$ 融贯，则 $\Delta_{\IC}(E_1\sqcup E_{2}) \models \Delta_{\IC}(E_1) \land \Delta_{\IC}(E_{2})$

**(IC7)**

$\Delta_{\IC_{1}}(E) \land \IC_{2} \models\Delta_{\IC_{1\land} \IC_{2}} (E)$

**(IC8)**

若 $\Delta_{\IC_1}(E) \land \IC_{2}$ 融贯，则 $\Delta_{\IC_{1\land}\IC_{2}} (E) \models\Delta_{\IC_1}(E)$

为阐明上述公设，且看（Konieczny and Pino Pérez 1999）[^konieczny-1999]所举的一例。一群公寓业主打算改善其共有物业。会上主席提议：或建网球场，或建游泳池，或建私家车位。他同时指出，三个选项中若建了两个，年度维护费将大增（此即 *IC* 所对应者）。

(IC0) 保证合并所得的基满足完整性约束。此条显然该当施加：这些本就是在完整性约束下合并的公设，用心正是不让结果逸出约束。主席借合并算子可以预知，只要众人决定三处设施中至少建两处，便都会同意费用上涨。(IC1) 说：*IC* 融贯时，融合算子的结果同样融贯。理由如前——合并基的解释取自完整性约束的解释，故 *IC* 融贯则结果必融贯。(IC2) 说：只要信念剖面与 *IC* 的合取融贯，合并算子所得便是该合取本身。就眼前之例而言，若每位愿建两处以上设施者都认可费用上涨，而各业主所陈意见彼此融贯，则合并径直返回 *IC* 与个体意见之合取。(IC3) 说：若两个信念剖面 $E_1$ 与 $E_{2}$ 逻辑等价，$\IC_1$ 与 $\IC_{2}$ 亦相等价，则把前者与 $\IC_1$ 合并，与把后者与 $\IC_{2}$ 合并等价。此公设所表达的，是信念修正算子早已背上的原则（合并算子不过是其扩展，说见下文），亦即句法无涉原则：合并的结果只系于所并诸基的语义内容，不系于其句法写法。(IC4) 通称公平公设：合并 $K_1$ 与 $K_{2}$ 时不得偏袒任何一方；结果与其中之一相容，当且仅当与另一方相容。此乃一项对称要求，凡厚此薄彼的算子皆不能满足。(IC5) 与 (IC6) 首见于（Revesz 1997）[^revesz-1997]，二者合而言之：若两群体至少在一项上意见相合，融合结果便落在这一相合项上。故若业主可分为两派，一派欲建网球场与游泳池，一派欲建游泳池与停车场，则建游泳池将获选为群体的最终决定。末了，(IC7) 与 (IC8) 担保：若 $E$ 在 $\IC_1$ 与 $\IC_{2}$ 之下的合并结果与 $\IC_{2}$ 相容，则让 $E$ 则在更严的约束——即 IC1 与 $\IC_{2}$ 之合取——下合并时，$\IC_1$ 仍然得到满足。此项要求出于自然：说得不那么形式些，(IC7) 与 (IC8) 合起来的意思是，游泳池若在三个备选方案中获选，则备选缩为网球场与游泳池两处时，它仍当获选。这末两条公设，是（Katsuno and Mendelzon 1991）[^katsuno-1991]中修正公设 R5 与 R6 的推广；该文自模型论角度剖析修正算子，并以相对于解释上某一序的最小改动，刻画了满足 AGM 合理性公设（Alchourrón et al. 1985）[^alchourrón-1985]的修正算子。与 Katsuno、Mendelzon 的公设一样，(IC7) 与 (IC8) 保证接近性概念不至于失范：某结果若在 $\IC_1$ 下为合并算子所选，则在更严的约束 $\IC_1 \land \IC_{2}$ 下，它仍是距 $\IC_{2}$ 最近者（即仍会入选），前提是 $\Delta_{\IC_1}(E) \land \IC_{2}$ 融贯。Katsuno 与 Mendelzon 的模型论进路中，修正算子借选取新信息中最接近的解释来改易初始信念基；*IC* 合并算子亦犹是，它在完整性约束中挑出距诸信念基最近的那个解释。准此，信念合并可视为信念修正向多个信念基的推广（Grégoire and Konieczny 2006）[^grégoire-2006]。

$\IC$ 融合算子之下另分两类。*IC 多数融合*算子务求把总体不满降至最低（此概念由 Lin and Mendelzon 1996 引入）[^lin-1996][^lin-1996-2]；*IC 仲裁算子*则力求把个体不满在各智能体之间均摊。多数算子之旨趣近于社会选择理论中的功利主义，仲裁则取意于平等主义。

对任一整数 $n$，以 $E^n$ 记含 *n* 份 *E* 的多重集。*IC 多数*算子还须满足下述附加公设：

**(Maj)**

$\exists n \Delta_{\IC} (E_1\sqcup E^{n}_{2}) \models\Delta_{\IC}(E_{2})$

由此可见，(Maj) 所断言的是：把 $E_{2}$ 重复足够多遍，即足以使 $E_{2}$ 成为群体意见。所需遍数视具体情形而定。

除 (IC0)–(IC8) 之外，*IC 仲裁*算子另有如下一条刻画公设：

**(Arb)**

设 IC1 与 IC2 逻辑独立。若 $$\begin{align} \Delta_{\IC_1}(K_1) &\equiv \Delta_{\IC_2}(K_{2}), \textrm{ and}\\ \Delta_{\IC_{1} \leftrightarrow \neg \IC_{2}} (\{K_1, K_{2}\}) &\equiv (\IC_1\leftrightarrow \neg \IC_{2}), \textrm{ then} \\ \Delta_{\IC_{1}\lor \IC_{2}} (\{K_1, K_{2}\}) &\equiv \Delta_{\IC_1}(K_1).\end{align}$$

此公理直观上说的是：仲裁算子择取那些与 *IC* 融贯的中位结果。待下一节以模型论方式表述后，该算子的行止便更为显豁。

试举一例，以见多数算子与仲裁算子行为之别。设三位朋友须决定是否为一位共同的熟人合送生日礼物。设其中两人想送她一本书并请她外出晚餐，第三位朋友则不愿为这两样礼物出一分钱。若群体以多数定夺，三位朋友便议定送书并请客，第三位朋友将大为不快。反之，若用仲裁算子，结果非送书即请客，三人的不满程度因而相当——每人信念基中恰有一个公式未获满足，故此“不满之量”对三人相同。

文献中的融合算子可分两类：基于句法者与基于模型者。前者以命题公式为输入，通常着眼于信念剖面的极大融贯子集；后者所取作合并输入者，则是公式的解释，故每个信念基被视作一个模型集，其公式如何写就便无关痛痒。请回忆第 2 节开头用来说明信念基组合依赖句法的那个例子：$K_1 = \{a, b\}$、$K_2 = \{a \wedge b\}$ 与 $K_3 = \{\neg b\}$。基于句法的融合会把 $a, b, a \wedge b, \neg b$ 当作输入，基于模型的融合则取 $mod(K_1) = mod(K_2) = \{(1, 1)\}$ 与 $mod(K_3) = \{(1,0), (0,0)\}$。既然基于模型的算子已施用于判断聚合问题，下文便专注于这一类合并算子；至于基于句法的融合，读者可参阅（Baral et al. 1992; Konieczny 2000; Grégoire and Konieczny 2006）[^baral-1992][^grégoire-2006][^konieczny-2000]。

### 2.2 基于距离的进路

基于模型的 *IC* 融合算子所做的，是在完整性约束 *IC* 的诸模型之中挑出较受偏好者；偏好关系因算子而异。如此，集体信念集 $\Delta_{\IC}(E)$ 必是一切入选模型皆真的公式所成之集，且满足 *IC*。就前举市议会之例而言，这意味着“既建游乐场又建停车场”永远不会入选为决定结果。偏好信息一般表现为全预序（预序即自反且传递的关系）$\le$，它由解释 $\omega$ 与剖面 *E* 之间的距离概念 *d* 所诱导，记作 $d(\omega,E)$。直观上，这是要挑出一个集体结果：在满足完整性约束的前提下，它离一切个体信念基最近（距离概念尚待界定）。须注意，基于距离的融合算子并不总能给出唯一结果；此点在讨论信念合并在判断聚合上的应用时再谈。

前文已见，多数算子的特点在于力求总体不满最小，仲裁算子则力求局部不满最小。所以不妨把距离视作刻画“不满”的手段。信念修正有所谓经济原则，受其启发，合并的结果应尽量多地保存每个个体信念基 $K_i$ 的信息。换句话说，既然各信息源同样可靠，合并时就应从各源删削得越少越好。于是办法便是：挑选出使 *IC* 的诸模型与信念剖面 *E* 的诸模型之间距离最小者。形式上可表述如下：

$$ \mymod(\Delta_{\IC}(E)) = \mymin (\mymod (\IC), \le_{d}) $$

所谓解释之间的距离，是一个全函数 $d: W \times W \rightarrow R^{+}$，且对一切 $\omega, \omega'\in W$ 满足：

1. $d(\omega ,\omega') = d(\omega',\omega )$
2. $d(\omega ,\omega') = 0 \textrm{ 当且仅当 } \omega =\omega'$。

第一点说的就是距离的对称性。设有三个信念基：$K_1 = K_3 = \{a, b, \neg c, d\}$ 与 $K_2 = \{\neg a, b, c, d\}$。以 $\omega_i$ 记 $K_i$ 的解释，则 $\omega_1 = \omega_3 = (1,1,0,1)$、$\omega_2 = (0,1,1,1)$。第一点要求 $d(\omega_1 ,\omega_2) = d(\omega_2 ,\omega_1)$。第二点则说：两个解释若相同，距离即为 0，于是 $d(\omega_1 ,\omega_3) = 0$。[^note-2]

要找出使得到信念剖面距离最小的 *IC* 模型，须分两步走。第一步，算出每个满足 *IC* 的解释（亦即每个候选合并基）与每个个体信念基之间的距离。此处的用意，是量化每个个体意见距每个可能集体结果有多远（须知结果是在满足 *IC* 的解释中选取的）。第二步，把上述各个体距离聚合起来，界定集体距离，即信念剖面到 *IC* 每一模型的距离——这相当于量化群体距每一可能结果多远。末了，使此距离最小者（或许不止一个基）入选为结果。

第一步要界定的是解释 $\omega$ 与信念基 *K* 之间的距离，即 $\omega$ 到 *K* 诸模型的最短距离。形式写作：$d(\omega, K) = \mymin_{\omega'\in \mymod(K)} d(\omega, \omega')$。倘若 *K* 有两个以上模型（譬如 $K_i = \{a \vee b\}$ 便有 $\{(0,1) (1,0), (1,1)\}$ 三个模型），则 $\omega'$ 取距 $\omega$ 最近的那个。

如今可以界定解释 $\omega$ 与信念剖面 *E* 之间的距离了，第二步正需要此物。所需者是一个聚合函数 $D: R^{+n} \rightarrow R^{+}$：它接受第一步所算出的 *IC* 诸模型与各信念基 $K_i$ 之间的距离，把它们聚合成一个集体距离，即 $D(\omega, E) = D(d(\omega, K_1)$, $d(\omega, K_2)$, $\ldots$, $d(\omega, K_n))$。如此便在一切解释之集 *W* 上得了全预序。合并算子于是可以挑出所有使得到剖面 *E* 距离最小的解释。

就技术而言，聚合函数 $D: R^{+n} \rightarrow R^{+}$ 给每个非负实数的 *n* 元组指派一个非负实数。对任意的 $x_1,\ldots, x_{n}, x, y \in R^{+}$，D 具备如下性质：

1. 若 $x\ge y$，则 $D(x_1,\ldots , x,\ldots , x_{n})\ge D(x_1,\ldots , y,\ldots , x_{n})$
2. $D(x_1,\ldots , x,\ldots , x_{n})=0$ 当且仅当 $x_1=\ldots =x_{n}=0$
3. $D(x)=x$

合并算子得出何种结果，显然系于所择取的诸距离函数 *d* 与 *D*。最早的一批方案（Lin and Mendelzon 1999; Revesz 1993）[^lin-1999][^revesz-1993]取 *d* 为汉明距离（定义见下），取 *D* 为求和或取最大值（分别记作 $D_{\Sigma}$ 与 $D_{\mymax}$）。[^note-3] *D* 若取求和，全局距离便是诸个体距离之和；相应的合并算子是多数算子，人称最小和算子，因为它专挑使和最小的解释。用 $D_{\mymax}$ 的合并算子则称最小最大算子，所输出者是使得到诸个体基的最大距离最小的判断集（Brams et al. 2007b）[^brams-2007b]。其用意在于让与最不满者的分歧降至最低。采用 $D_{\Sigma}$ 或 $D_{\mymax}$ 时，入选者可能恰是两个相反的结果（Brams et al. 2007b; Eckert and Klamler 2007）[^brams-2007b][^eckert-2007]。

汉明距离在信念修正中一向常用，其想法至为浅显：它数一数两个解释在几个命题字母上取值不同。比如 $\omega = (1, 0, 0)$ 与 $\omega' = (0, 1, 0)$，两解释对第一、第二个命题的指派互异，故 $d(\omega, \omega') = 2$。同样著称的是极端距离：两解释相同则距为 0，否则为 1。然而距离之择取并不限于此二者，尚有其他距离同样满足前述公设（Konieczny and Pino Pérez 1999, 2002）[^konieczny-1999]。把诸个体距离之和降至最小，便是 *IC* 多数合并算子的一例。下节将见此算子施用于论辩困境。

基于距离的进路，恰好把仲裁算子与多数算子之别点破。词典最大算子即仲裁算子之一例。它可取 *d* 为汉明距离，并将每个解释到 *n* 个基 $K_i$ 的距离列成一个序列；先在智能体集上定一个次序，再以诸距离序列之间的词典序界定解释上的预序；最终由 $D_{\textit{leximax}}$ 取最小值。其用意在于：多数算子拣选使总体分歧最小的方案（例如把个体距离之和压至最低）；仲裁算子却注目于分歧如何分布，拣选对众人较为公平的方案，务使各人对所选结果的不满大致均分。请回想前举生日礼物之例。此点本乎汉明距离的定义：距离越大，两解释分歧越深（此所谓“分歧”，仅指两解释给同一公式指派了不同真值）。设信念剖面 *E* 含三个基，又设 *IC* 的两个模型 $\omega$ 与 $\omega'$ 在汉明距离求和之下皆为 $D_{\Sigma} (\omega, E) = D_{\Sigma} (\omega', E) = 6$，而在距离的词典序之下则分别为 $D_{\textit{leximax}}(\omega, E)= (2,2,2)$ 与 $D_{\textit{leximax}}(\omega', E)= (5,1,0)$。此时多数算子无从分辨 $\omega$ 与 $\omega'$（两者之和同为 6），仲裁算子却宁取 $\omega$ 而舍 $\omega'$，盖 $\omega$ 分配个体分歧比 $\omega'$ 更为公允。

前已提及，Liberatore 与 Schaerf 乃最早倡议仲裁算子者之一。可惜其进路只容两个基，且合并所得必为二基之一。这类算子在某些场合会给出可疑结果，例如（Konieczny and Pino Pérez 2002）[^konieczny-2002]所举者。设两位金融专家就四支股票 *a, b, c*、*d* 为你献策。第一位认为四支皆涨（记作 $\varphi_1= \{(1, 1, 1, 1)\}$），第二位则断定四支皆跌 $(\varphi_{2}= \{(0, 0, 0, 0)\})$。依 Liberatore 与 Schaerf 的仲裁算子，所得为 $\{(1, 1, 1, 1), (0, 0, 0, 0)\},$ 意即第一位或第二位专家完全说对了。反之，若施用 Konieczny 与 Pino Pérez 式的仲裁算子，则有 $\{(0, 0, 1, 1)$, $(0, 1, 0, 1)$, $(0, 1, 1, 0)$, $(1, 0, 0, 1)$, $(1, 0, 1, 0)$, $(1, 1, 0, 0)\}$。此结果可解为：既假定诸来源同样可靠，我们便无可偏袒，于是合理的立场是两说或将同真。话虽如此，凡结果只能取诸个体所提基之一者，Liberatore 与 Schaerf 的算子仍可一用。譬如两位医生会诊商定病人疗法，多半须择定两种方案之一，因为把疗法混杂起来既未必可行，又不免危险。

有一条表示定理（Konieczny and Pino Pérez 1999, 2002）[^konieczny-1999]保证：*IC* 合并算子的每一子类（多数算子与仲裁算子）皆对应于解释上之一族预序（此与 Katsuno、Mendelzon（1991）为信念修正算子所证的表示定理相映）。[^note-4]

下面说明信念合并如何施用于判断聚合问题。

## 3. 信念合并在论辩困境上的应用

把个体信念基合并为集体基，与判断聚合问题颇有相通之处：两者都欲把个体输入聚合成群体结果，且都借逻辑来形式化各基的内容。如第 1 节所示，没有哪种聚合程序能确保群体判断既融贯又完备。然而计算机科学所引入的合并算子却能保证结果融贯，因为这类算子不满足独立性。某命题上的集体判断，不只取决于个体就该命题的判断，还取决于对议程中一切其他条目的考量。因此，把合并方法的成果移用于个体判断的聚合，乃顺理成章（Pigozzi 2006）[^pigozzi-2006]。

判断聚合中的不可能定理，与 *IC* 合并算子能够确保集体结果融贯这一事实，如何得以两全？答案在于：合并算子违背了独立性条件——而这正是不可能定理加于聚合函数的要求之一。独立性之所以看似可取，是因为它使聚合函数免遭策略性操纵（Dietrich 2006; Dietrich and List 2007b）[^dietrich-2006][^dietrich-2007b]：既然如此，个体便没有动机为求对己有利的结果而提交不诚实的判断集。然而文献中早有非议，认为独立性并不适合充当聚合逻辑上彼此关联命题的要求（Chapman 2002; Mongin 2008）[^chapman-2002][^mongin-2008]。悖论性结果之所以能避开，端赖 *IC* 把不可接受的结果挡在门外。不过应当指出，判断聚合中的集体理性条件（要求输出逻辑融贯）所起的作用，恰与信念合并中的 *IC* 相当，同样是把不一致的多数判断之类挡在门外。再者，纵使把额外的完整性约束明确引入判断聚合框架，其不可能结果仍旧成立（见 Dietrich and List 2008b; Grandi 2012）[^dietrich-2008b][^grandi-2012]。

有人指出（Brams et al. 2007a）[^brams-2007a]：多数投票恰使汉明距离之和最小。也就是说，只要逐命题多数投票所得判断集融贯，最小和规则选出的便是同一结果。多数投票自有其民主的资历。此外，重视基于距离的多数程序，还因为聚合个体判断的目的本应是得出正确决定，而非公平分摊各人的不满。多数投票与正确决定之间的认识论关联，见于孔多塞陪审团定理：只要投票者彼此独立、各人正确的概率相同且高于随机，多数规则便能保证择定正确决定。群体愈大，如此择定的概率愈近于 1（关于此点及多数规则的更多形式论证，见 List 2013）[^list-2013]。

且看三位法官之例，施用最小和规则会得到什么。法律教义对应 $\IC= \{(p\land q) \leftrightarrow r\}$。法庭以剖面 $E=\{K_1 , K_{2} , K_{3}\}$ 表示，即含三位法官判断集 $K_1 , K_{2} , K_3$ 的多重集。三个判断集及其模型如下：

\begin{align} K_1 &= \{p, q, r\} \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \mymod(K_1) &= \{(1, 1, 1)\};\\ K_{2} &= \{p, \neg q, \neg r\} \ \ \ \ \ \ \ \ \ \ \ \ \mymod(K_{2}) &= \{(1, 0, 0)\};\\ K_{3} &= \{\neg p, q, \neg r\} \ \ \ \ \ \ \ \ \ \ \ \ \mymod(K_{3}) &= \{(0, 1, 0)\}.\\ \end{align}

表 2 给出使汉明距离之和最小的多数算子所得的结果。表的第一列是命题变项 *p*、*q*、*r* 的全部解释；凡非 *IC* 模型的解释，皆以底纹标示。举例说，$(1,0,1)$ 便不能入选为集体结果，因为它违犯了法律教义。$d_H (\cdot,K_1)$、$d_H(\cdot,K_{2})$、$d_H(\cdot,K_{3})$ 三列中的数目，是各 $K_i$ 距相应解释的汉明距离；末一列则为汉明距离之和。

*表 2*

|   | $d_{H}(\cdot,K_{1})$ | $d_{H}(\cdot,K_{2})$ | $d_{H}(\cdot,K_{3})$ | $\Sigma(d_{H} (\cdot,E))$ |
| --- | --- | --- | --- | --- |
| $(1,1,1)$ | 0 | 2 | 2 | 4 |
| $(1,1,0)$ | 1 | 1 | 1 | 3 |
| $(1,0,1)$ | 1 | 3 | 1 | 5 |
| $(1,0,0)$ | 2 | 2 | 0 | 4 |
| $(0,1,1)$ | 1 | 1 | 3 | 5 |
| $(0,1,0)$ | 2 | 0 | 2 | 4 |
| $(0,0,1)$ | 2 | 2 | 2 | 6 |
| $(0,0,0)$ | 3 | 1 | 1 | 5 |

表 2

由此可见，若无 *IC*，基于距离的多数算子所选出的结果，与逐命题多数投票相同，即不融贯的 $(1,1,0)$——这恰是距 *E* 最近的结果。但合并算子不能取 $(1,1,0)$，因为它违犯 IC。撇开底纹之行，可作集体判断集候选者只有四个解释：$(1,1,1)$、$(1,0,0)$、$(0,1,0)$ 与 $(0,0,0)$。其中三个使距离达到最小。可见采用基于距离的聚合，集体不一致便得以避免。只是此法未必总能给出唯一结果：在法庭一例中，该聚合便以 $(1,1,1)$、$(1,0,0)$、$(0,1,0)$ 三个模型为群体立场。就技术而言，这称为无决断的程序；若欲求得唯一结果，须再配上一条决胜规则（社会选择理论中即如此）。

计算机科学所发展的合并技术虽可用于判断聚合问题，却并不意味着两门学科志趣相同。前文已见，信念合并的初衷在于界定聚合不同来源信息的方式。各来源获取信息的机会未必均等，故此处并不假定有一个外部给定的议程——这与判断聚合框架有别，后者要求个体就一组既定条目陈述意见。二者的差异还不止于所聚合输入的类型，其输出亦不相同：信念合并输出一个满足某些完整性约束的集体基，判断聚合则输出关于既定议程的集体判断。

尚有另一差别：判断聚合假定成员皆理性，故各人所提交的判断集莫不融贯；信念合并不作此假定，智能体所交的信念基纵与 *IC* 相违亦可（Grégoire 2004）[^grégoire-2004]。某个体的判断若违反完整性约束，该判断集自然不入群体立场候选之列，但其输入并不会被弃置，合并且仍会把它算上。至于对某一事项弃权不表态，在信念合并的设定中亦不难兼顾：设个体须就 *p*、*q*、*r* 表态，而某智能体确信 *q* 与 *r*、对 *p* 则无定见，此时可表为 $\mymod(K_1)= \{(1, 1, 1),$ $(0, 1, 1)\}$，距离照此计算。判断聚合框架中，对判断集的完备性要求也已放宽。List 与 Pettit（2002）最先在超级多数规则与全体一致规则的语境下讨论放宽完备性；后来证明（Gärdenfors 2006; Dokow and Holzman 2010）[^dokow-2010][^gärdenfors-2006]，一旦不再假定判断集完备，任何独立而全体一致的聚合函数皆是弱寡头制的，即由个体中的某个子集决定集体结果。此说较独裁制为温和，尽管子集仅含一人时仍退为独裁。Dietrich 与 List（2008a）亦独立得出与（Dokow and Holzman 2010）[^dokow-2010]相当的寡头规则结果。

末了，判断聚合明确容许句法依赖，而基于模型的合并进路则否。当一个判断问题可以两个逻辑等价而句法各异的议程来陈述时，便可能引出决定框定问题（Cariani et al. 2008）[^cariani-2008]，或逻辑上的议程操纵（Dietrich 2006）[^dietrich-2006]。

信念合并与判断聚合之间关系的形式探究，见于（Everaere et al. 2015, 2017）[^everaere-2015]。如前所述，信念合并以命题信念基的剖面为输入，诸基代表某个个体的信念，并不拘于某一既定议程；判断聚合则要求个人就一组特定议题提出判断。其分析立足于一项假定：由个体信念可以导出其关于议程条目的意见。职是之故，（Everaere et al. 2015）[^everaere-2015]界定了投影函数 *p*（假定对一切个体相同），其职分正是自智能体的信念（信念合并之输入）推出其判断（判断聚合算子之输入）。举例说，某个体若仅信 $a\land b$，而议程条目之一为 *a*，则投影函数可推出此人就 *a* 投“是”。反之，若她仅信 *a*，而议程条目之一为 $a\land b$，她便多半无从就该条目表态。正因如此，（Everaere et al. 2015）[^everaere-2015]中的个体判断集不必完备（个体对议程某些议题可以弃权）。借投影 *p*，该文考虑了自信念基剖面导出集体判断的两条路径：一为“先合并后投影”，即先用合并算子合并诸个体信念基，再以投影 *p* 算出集体判断；一为“先投影后聚合”，即先由 *p* 算出各人的判断集，再以判断聚合程序聚合，定出关于既定议程的集体判断。于是问题便是：两条路径所得集体判断是否相合。文中分两种情形：一般情形（议程不完备）与议程完备的情形（议程含一切可能的解释）。例如议程 $A= \{\neg a \land \neg b, \neg a \land b, a \land \neg b, a \land b\}$ 完备，而 $A= \{\neg a \land \neg b, \neg a \land b, a \land \neg b\}$ 则不完备。设某个体相信 $a\land b$，其判断集在前一议程中为 $(0,0,0,1)$，在后一议程中为 $(0,0,0)$；取“先合并后投影”抑或“先投影后合并”，所得集体结果便可能不同。至于巧择议程即可操纵结果一事，判断聚合文献已有探究（Dietrich 2016, Lang et al. 2016）[^dietrich-2016][^lang-2016]。在一般情形下，IC 合并方法所得，可能异于采用满足全体一致或多数保持性质的判断聚合算子所得[^note-5]。较可乐观者，议程完备之时，对某些满足与若干 IC 合并公设相近之性质的判断聚合算子来说，两条路径所得的集体判断互相吻合。

晚近，基于距离的算子又施用于判断聚合的新课题：动态理性的判断聚合。传统上，判断聚合着眼于静态聚合——个体提交判断，再以某种程序将其聚合。但在更切实际的情境中，新信息随时可能到来。此时当如何聚合判断？Dietrich 与 List 追问道：集体判断能否是动态理性的，即能否针对新信息理性地改易（Dietrich and List 2024）[^dietrich-2024]。所谓一条判断聚合规则相对于某修正算子具有动态理性，是指：先在新信息之下各自修正判断、再行聚合，与径直以新信息修正旧的集体判断，二者结果相同。例如基于距离的修正算子，能在融贯地纳入新信息的同时只对判断作最小改动，故而是保理性的。Dietrich 与 List 考察判断聚合规则与修正算子达成动态理性的条件，指出其中困难种种，并给出一条相关的不可能定理；也探讨了逃出该不可能结果的若干出路（放宽对聚合规则或修正算子的条件而得）。

### 3.1 扩展与批评

前节用以合并三位法官判断集的最小和规则，其原则与著名的偏好聚合规则凯梅尼规则相同（Kemeny 1959）[^kemeny-1959]。与社会选择的情形不同，判断聚合文献起初偏重公理化方法，具体聚合规则之提出与研究者寥寥。应该说，正是计算机科学与多智能体系统研究者的兴趣，促成了更多具体聚合规则的界定以及彼此关系之探究。最小化这一观念在信念合并中举足轻重，在社会选择理论的若干投票规则定义中同样是一条原则。例如最小和规则，已证明与判断聚合文献晚近引入的若干其他规则相当（Lang et al. 2017）[^lang-2017]。

计算机科学家对聚合方法的兴致，可由一事见之：判断聚合如今已列入计算社会选择这一跨学科领域，而该领域正推动计算机科学与社会选择理论互通声气。聚合规则的计算问题，即属计算社会选择所关心者。把复杂性理论施于聚合规则，其用意是在实用层面评定规则可否采纳，即施行该规则的算法是否可行。若某规则的结果“易于”算出，该规则便可接受；“易于”者，指能以算法在最坏情形下于与输入规模成多项式增长的时间内求得（只有在某些病态情形下，我们才会企盼一条在可预见的将来给不出结果的规则）。反过来，一条规则若可被操纵，则只要个体“难以”操纵它，仍属可接受。是故研究聚合规则的计算复杂性，或可揭示：某规则纵可操纵，个体实际上却难以施行操纵。基于距离的程序之计算复杂性已有研究（Endriss et al. 2012; Endriss and de Haan 2015）[^endriss-2015][^endriss-2012]。汉明规则在判断聚合中所需计算甚巨，恰与偏好聚合中凯梅尼规则同样计算繁重这一平行结果相映——此点最早由 Bartholdi 等人（1989）与 Hudry（1989）揭出。为避开基于距离的程序之繁重计算，有人另提一条新规：平均投票者规则（Grandi 2012）[^grandi-2012]在众个体所交判断集之中，选取距离之和最小者，故其结果必为已提交判断集之一。这既减轻了计算负担，又同时选出最具代表性的个体。

判断聚合的基于距离方法，另有一种推广见（Miller and Osherson 2009）[^miller-2009]。该文不仅把前文施于教义悖论的合并算子作了推广（改用一般度量），还为判断聚合另立三种基于距离的程序。当逐命题多数意见汇成不融贯的集体判断集时，端点法便择取（依某种距离度量）最接近的融贯集体判断集为群体结果；完全法与输出法则设法对剖面作最小改动，俾使输出成为逐命题一致的集体判断集，二者之别在于输出法容许修改后的剖面中个体判断集互不一致。

Duddy 与 Piggins（2012）对以汉明距离衡量判断集表示怀疑。其难处在于：议程若含逻辑上彼此关联的命题，汉明距离便可能重复计数，因为它对此类相互依赖视若无睹。举例说，设两人都接受命题 *q*，却在 $p\land q$ 上相左（一人接受该合取，一人拒斥）。此情形唯当他们在 *p* 上相左时方可能出现。两个判断集 $K_1 = \{\neg p, q, \neg(p\land q)\}$ 与 $K_{2} = \{p, q, (p\land q)\}$ 之间的汉明距离为 2。既然正是对 *p* 的分歧引出了对 $p\land q$ 的分歧，距离理应只是 1。为解此弊，有人另提一种距离：把一个判断集转换为另一判断集所需的最小融贯改动之数。

## 4. 其他论题

信念合并是一门抽象理论，所处理者是聚合符号输入的问题，至于这些条目究竟是信念、知识、欲望抑或规范，则不加限定；择取何种合并算子，须视输入的类型而定。判断聚合的框架也已扩展，可容纳其他类型态度的聚合，其例见（Dietrich and List 2010）[^dietrich-2010]。

信念合并文献也研究策略性操纵问题（Evaraere et al. 2007）。某聚合程序若不能防策略，则对可能结果有所偏好的个体便可谎报真实信念以操纵结果，从而取得较合己意的结局。一般而论，取汉明距离时合并算子不能防策略，取极端距离时则能。判断聚合中策略行为研究的近期综述，见（Baumeister et al. 2017）[^baumeister-2017]。

凡可假定有事实真相（例如被告究竟有否杀人）、而每个智能体对此各持（带噪声的）意见的场合，皆可考察信念合并算子的求真性质（Hartmann et al. 2010; Hartmann and Sprenger 2012; Cevolani 2014）[^cevolani-2014][^hartmann-2010][^hartmann-2012]。此时的问题便是：某种聚合方法能否择定正确决定。Williamson（2009）主张，就判断聚合而言，最善之策是聚合判断所据的证据，如此方能得出正确决定。他倡导的三步方案区分三类命题：证据、信念与判断。证据者，乃智能体信念与判断之依据，正是合并技术所宜施用的对象；至于判断，则宜交由决策理论处置——后者把信念度与效用映射为判断。

## 脚注

[^note-1]: 原子命题之集 *At* 假定为有序：即有一序，使 *p* 先于 *q*，*q* 又先于 *r*。故 $(1,0,0)$ 所表示的解释，是把真赋给 *p*、把假赋给 *q* 与 *r*。

[^note-2]: 严格而论，*d* 是伪距离，因三角不等式 $(\forall \omega, \omega', \omega'' \in W$, $d(\omega, \omega') \le d(\omega, \omega'') + d(\omega'', \omega'))$ 并不必须成立。Konieczny 与 Pino Pérez（2002）证明：*d* 若满足三角不等式，则 $D_{\Sigma}$ 满足 *迭代* 公理：

**($\IC_{\textit{It}}$)**

若 $\varphi \vdash \IC$，则 $\exists n \Delta_{\IC}^{n} (E,\varphi) \vdash\varphi$

[^note-3]: 与决策理论中的最小最大规则相类，取最大算子意在择取使最坏分歧降至最低的结果。此类算子不能满足合并的全部公设，故称准合并算子（Konieczny and Pino Pérez 2002）[^konieczny-2002]。

[^note-4]: 信念修正与信念合并之间渊源甚深。尤须指出，合并算子可看作修正算子的推广（Konieczny and Pino Pérez 2002）[^konieczny-2002]。更确切地说，设 $\Delta$ 为 *IC* 合并算子，则由 $\varphi * \IC= \Delta_{\IC}(\varphi)$ 所定义的算子 $*$ 便是 AGM 修正算子（Alchourrón *et al.* 1985）[^alchourrón-1985]。至于反方向——AGM 修正算子是否定义 *IC* 合并算子——答案较复杂，约略可说：一修正算子能定义合并 *IC* 算子，当且仅当该修正算子系以距离来界定者。

[^note-5]: 多数保持性质所保证的是：逐命题多数投票所得若为融贯的判断集，则判断聚合程序必须择取同一判断集（Lang et al. 2017）[^lang-2017]。

## References（引用注释）

**以下文献从原文照录，不作翻译；中国文献译为中文。**

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

[^alchourrón-1985]: Alchourrón, C.E., P. Gärdenfors, and D. Makinson, 1985, “On the Logic of Theory Change: Partial Meet Functions for Contraction and Revision”, *Journal of Symbolic Logic*, 50: 510–530.
[^arrow-1951]: Arrow, K., 1951/1963, *Social Choice and Individual Values*, New York: Wiley.
[^baral-1991]: Baral, C., S. Kraus, and J. Minker, 1991, “Combining Multiple Knowledge Bases”, *IEEE Transactions on Knowledge and Data Engineering*, 3(2): 208–220.
[^baral-1992]: Baral, C., S. Kraus, J. Minker, and V. Subrahmanian, 1992, “Combining Multiple Knowledge Bases Consisting of First Order Theories”, *Computational Intelligence*, 8(1): 45–71.
[^bartholdi-1989]: Bartholdi, J., C. Tovey, and M. Trick, 1989, “The Computational Difficulty of Manipulating an Election”, *Social Choice and Welfare*, 6: 227–241.
[^baumeister-2017]: Baumeister, D., J. Rothe, and A.K. Selker, 2017, “Strategic Behavior in Judgment Aggregation”, in U. Endriss (ed.), *Trends in Computational Social Choice*, AI Access, pp. 145–168.
[^benferhat-1998]: Benferhat, S., D. Dubois, J. Lang, H. Prade, A. Saffiotti, and P. Smets, 1998, “A General Approach for Inconsistency Handling and Merging Information in Prioritized Knowledge Bases”, in *Proceedings of the Sixth International Conference on Principles of Knowledge Representation and Reasoning* (KR’98), San Francisco: Morgan Kaufmann, pp. 466–477.
[^black-1948]: Black, D., 1948, “On the Rationale of Group Decision Making”, *The Journal of Political Economy*, 56: 23–34.
[^bloch-2001]: Bloch, I., A. Hunter, A. Ayoun, S. Benferhat, P. Besnard, L. Cholvy, R. Cooke, D. Dubois and H. Fargier, 2001, “Fusion: general concepts and characteristics”, *International Journal of Intelligent Systems*, 16: 1107–1134.
[^borgida-1984]: Borgida, A. and T. Imielinski, 1984, “Decision Making in Committees: A Framework for Dealing with Inconsistency and Non-Monotonicity”, in *Proceedings of the Workshop on Non-Monotonic Reasoning*, New Paltz, NY, pp. 21–32.
[^brams-2007a]: Brams, S.J., D.M. Kilgour, and M.R. Sanver, 2007a, “A Minimax Procedure for Negotiating Multilateral Treaties”, in R. Avenhaus and I. W. Zartman (eds.), *Diplomacy Games: Formal Models and International Negotiations*, Berlin: Springer, pp 265–282.
[^brams-2007b]: –––, 2007b, “A Minimax Procedure for Electing Committees”, *Public Choice*, 132: 401–420.
[^cariani-2008]: Cariani, F., M. Pauly, and J. Snyder, 2008, “Decision Framing in Judgment Aggregation”, *Synthese*, 163(1): 1–24.
[^cevolani-2014]: Cevolani, G., 2014, “Truth Approximation, Belief Merging and Peer Disagreement”, *Synthese*, 191(11): 2383–2401.
[^chapman-2002]: Chapman, B., 2002, “Rational Aggregation”, *Politics, Philosophy, Economics*, 1(3): 337–354.
[^chawathe-1994]: Chawathe, S., H. Garcia Molina, J. Hammer, K. Ireland, Y. Papakonstantinou, J. Ullman, and J. Widom, 1994, “The TSIMMIS Project: Integration of Heterogeneous Information Sources”, in *Proceedings of IPSJ Conference*, Tokyo: Information Processing Society of Japan, pp. 7–18.
[^cholvy-1998]: Cholvy, L., 1998, “Reasoning about Merged Information”, in D.M. Gabbay, and Ph. Smets (eds.), *Handbook of Defeasible Reasoning and Uncertainty Management Systems*, Vol. 3, Dordrecht: Kluwer Academic Publishers, pp. 233–263.
[^condorcet-1785]: Condorcet, N. de, 1785, *Essai sur l’Application de l’Analyse à la Probabilité des Décisions Rendues à la Pluralité des Voix*, Paris.
[^delgrande-2006]: Delgrande, J.P., D. Dubois, and J. Lang, 2006, “Iterated Revision as Prioritized Merging”, in *Proceedings of the 10ᵗʰ International Conference on Knowledge Representation and Reasoning* (KR’06), Menlo Park, CA: AAAI Press, pp. 210–220.
[^dietrich-2006]: Dietrich, F., 2006, “Judgment Aggregation: (Im)Possibility Theorems”, *Journal of Economic Theory*, 126: 286–298.
[^dietrich-2007]: –––, 2007, “A Generalised Model of Judgment Aggregation”, *Social Choice and Welfare*, 28(4): 529–565.
[^dietrich-2016]: –––, 2016, “Judgment Aggregation and Agenda Manipulation”, *Games and Economic Behavior*, 95: 113–136.
[^dietrich-2007a]: Dietrich, F. and C. List, 2007a, “Arrow’s Theorem in Judgment Aggregation”, *Social Choice and Welfare*, 29: 19–33.
[^dietrich-2007b]: –––, 2007b, “Strategy-proof Judgment Aggregation”, *Economics and Philosophy*, 23: 269–300.
[^dietrich-2008a]: –––, 2008a, “Judgment Aggregation Without Full Rationality”, *Social Choice and Welfare*, 31: 15–39.
[^dietrich-2008b]: –––, 2008b, “Judgment Aggregation Under Constraints”, in T. Boylan and R. Gekker, eds., *Economics, Rational Choice and Normative Philosophy*, Routledge, pp. 111–123.
[^dietrich-2010]: –––, 2010, “The Aggregation of Propositional Attitudes: Towards a General Theory”, in *Oxford Studies in Epistemology* (Volume 3), Oxford: Oxford University Press, pp. 215–234.
[^dietrich-2024]: –––, 2024, “Dynamically Rational Judgment Aggregation”, *Social Choice and Welfare*, 63: 531–580.
[^dokow-2010]: Dokow, E. and R. Holzman, 2010, “Aggregation of Binary Evaluations with Abstentions”, *Journal of Economic Theory*, 145(2): 544–561.
[^duddy-2012]: Duddy, C. and A. Piggins, 2012, “A Measure of Distance Between Judgment Sets”, *Social Choice and Welfare*, 39: 855–867.
[^eckert-2007]: Eckert, D. and C. Klamler, 2007, “How puzzling is judgment aggregation? Antipodality in distance-based aggregation rules”, Working paper, University of Graz.
[^elmagarmid-1999]: Elmagarmid, A., M. Rusinliewicz, and A. Sheth (eds.), 1999, *Management of Heterogeneous and Autonomous Database Systems*, San Francisco: Morgan Kaufmann.
[^elster-2013]: Elster, J., 2013, “Excessive Ambitions (II)”, *Capitalism and Society*, 8(1): Article 1 [[Elster 2013 available online](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=2207111)]
[^endriss-2016]: Endriss, U., 2016, “Judgment Aggregation”, in F. Brandt, V. Conitzer, U. Endriss, J. Lang, A. Procaccia (eds.), *Handbook of Computational Social Choice*, Cambridge: Cambridge University Press, pp. 399–426.
[^endriss-2015]: Endriss, U. and R. de Haan, 2015, “Complexity of the Winner Determination Problem in Judgment Aggregation: Kemeny, Slater, Tideman, Young”, in *Proceedings of the 14th International Conference on Autonomous Agents and Multiagent Systems*, IFAAMAS, pp. 117–125.
[^endriss-2012]: Endriss, U., U. Grandi, and D. Porello, 2012, “Complexity of Judgment Aggregation”, *Journal of Artificial Intelligence Research*, 45: 481–514.
[^everaere-2007]: Everaere, P., S. Konieczny, and P. Marquis, 2007, “The Strategy-Proofness Landscape of Merging”, *Journal of Artificial Intelligence Research (JAIR)*, 28: 49–105.
[^everaere-2015]: –––, 2015, “Belief Merging versus Judgment Aggregation”, in *Proceedings of the 14th International Conference on Autonomous Agents and Multiagent Systems* (AAMAS 15), IFAAMAS, pp. 999–1007.
[^everaere-2017]: –––, 2017, “An Introduction to Belief Merging and its Links to Judgment Aggregation”, in U. Endriss (ed.), *Trends in Computational Social Choice*, AI Access Books, pp. 123–143.
[^fermé-2018]: Fermé, E. and S.O. Hansson, 2018, *Belief Change. Introduction and Overview*, Cham: Springer.
[^gärdenfors-1988]: Gärdenfors, P., 1988, *Knowledge in Flux: Modeling the Dynamics of Epistemic States*, Cambridge, MA: MIT Press.
[^gärdenfors-2006]: –––, 2006, “A Representation Theorem for Voting with Logical Consequences”, *Economics and Philosophy*, 22: 18–190.
[^gauwin-2005]: Gauwin, O., S. Konieczny, and P. Marquis, 2005, “Conciliation and Consensus in Iterated Belief Merging”, in *Proceedings of the 8th European Conference on Symbolic and Quantitative Approaches to Reasoning with Uncertainty*, Berlin: Springer, pp. 514–526.
[^ginsberg-1986]: Ginsberg, M., 1986, “Counterfactuals”, *Artificial Intelligence*, 30(1): 35–79.
[^goldman-1999]: Goldman, A., 1999, *Knowledge in a Social World*, Oxford: Oxford University Press.
[^goldman-2004]: –––, 2004, “Group Knowledge versus Group Rationality: Two Approaches to Social Epistemology”, *Episteme: A Journal of Social Epistemology*, 1(1): 11–22.
[^goldman-2010]: –––, 2010, “Social Epistemology”, *The Stanford Encyclopedia of Philosophy* (Summer 2010 Edition), Edward N. Zalta (ed.), URL = <[https://plato.stanford.edu/archives/sum2010/entries/epistemology-social/](https://plato.stanford.edu/archives/sum2010/entries/epistemology-social/)>.
[^grégoire-2004]: Grégoire, E., 2004, “Extension of a Distance-based Fusion Framework”, in *Proceedings of the 8th International Conference on Sensor Fusion: Architectures, Algorithms and Applications*, pp. 282–286.
[^grégoire-2006]: Grégoire, E. and S. Konieczny, 2006, “Logic-based Approaches to Information Fusion”, *Information Fusion*, 7: 4–18.
[^grandi-2012]: Grandi, U., 2012, *Binary Aggregation with Integrity Constraints*, Ph.D. thesis, ILLC, University of Amsterdam [[Grandi 2012 available online](https://www.illc.uva.nl/Research/Publications/Dissertations/DS-2012-08.text.pdf)].
[^grossi-2009]: Grossi, D., 2009, “Unifying Preference and Judgment Aggregation”, in *Proceedings of the 8th International Conference on Autonomous Agents and Multiagent Systems*, pp. 217–224.
[^grossi-2014]: Grossi, D. and G. Pigozzi, 2014, *Judgment Aggregation: A Primer*, San Rafael, CA: Morgan & Claypool.
[^hansson-2011]: Hansson, S.O., 2011, “Logic of Belief Revision”, *The Stanford Encyclopedia of Philosophy* (Fall 2011 Edition), Edward N. Zalta (ed.), URL = <[https://plato.stanford.edu/archives/fall2011/entries/logic-belief-revision/](https://plato.stanford.edu/archives/fall2011/entries/logic-belief-revision/)>.
[^hartmann-2010]: Hartmann, S., G. Pigozzi, and J. Sprenger, 2010, “Reliable Methods of Judgment Aggregation”, *Journal of Logic and Computation*, 20(2): 603–617.
[^hartmann-2012]: Hartmann, S. and J. Sprenger, 2012, “Judgment Aggregation and the Problem of Tracking the Truth”, *Synthese*, 187(1): 209–221.
[^hudry-1989]: Hudry, O., 1989, *Recherches d’Ordres Médians: Complexité, Algorithmique et Problèmes Combinatoires*, Ph.D. thesis, Telecom Paris Tech.
[^katsuno-1991]: Katsuno, H. and A.O. Mendelzon, 1991, “Propositional Knowledge Base Revision and Minimal Change”, *Artificial Intelligence*, 52: 263–294.
[^kemeny-1959]: Kemeny, J., 1959, “Mathematics without numbers”, *Daedalus*, 88: 577–591.
[^kim-1995]: Kim, W. (ed.), 1995, *Modern Database Systems: The Object Model, Interoperability and Beyond*, New York: Addison Wesley.
[^konieczny-2000]: Konieczny, S., 2000, “On the Difference between Merging Knowledge Bases and Combining them”, in A.G. Cohn, F. Giunchiglia, and B. Selman, (eds.), *KR2000: Principles of Knowledge Representation and Reasoning*, San Francisco: Morgan Kaufmann, pp. 135–144.
[^konieczny-1998]: Konieczny, S. and R. Pino Pérez, 1998, “On the Logic of Merging”, in *Proceedings of the 6th International Conference on Principles of Knowledge Representation and Reasoning*, San Francisco: Morgan Kaufmann, pp. 488–498.
[^konieczny-1999]: –––, 1999, “Merging with Integrity Constraints”, in *Proceedings of the 5th European Conference on Symbolic and Quantitative Approaches to Reasoning with Uncertainty* (ECSQARU ’99), LNAI 1638, pp. 233–244.
[^konieczny-2002]: –––, 2002, “Merging Information under Constraints: A Logical Framework”, *Journal of Logic and Computation*, 12: 773–808.
[^kornhauser-1992]: Kornhauser, L.A., 1992, “Modeling Collegial Courts. II. Legal Doctrine”, *Journal of Law, Economics, and Organization*, 8: 441–470.
[^kornhauser-1986]: Kornhauser, L.A. and L.G. Sager, 1986, “Unpacking the Court”, *Yale Law Journal*, 96: 82–117.
[^kornhauser-1993]: –––, 1993, “The One and the Many: Adjudication in Collegial Courts”, *California Law Review*, 81: 1–51.
[^kornhauser-2004]: –––, 2004, “The Many as One: Integrity and Group Choice in Paradoxical Cases”, *Philosophy & Public Affairs*, 32(3): 249–276.
[^kowalski-1978]: Kowalski, R., 1978, “Logic for data description”, in H.G.J. Minker (ed.), *Logic and data bases*, New York: Plenum, pp. 77–102.
[^lang-2016]: Lang, J., M. Slavkovik, and S. Vesic, 2016, “Agenda Separability in Judgment Aggregation”, in *Proceedings of the Thirtieth Conference on Artificial Intelligence*, Palo Alto: Association for the Advancement of Artificial Intelligence (AAAI), pp. 1016–1022.
[^lang-2017]: Lang, J., G. Pigozzi, M. Slavkovik, L. van der Torre, and S. Vesic, 2017, “A Partial Taxonomy of Judgment Aggregation Rules and their Properties”, *Social Choice and Welfare*, 48(2): 327–356.
[^liberatore-1995]: Liberatore, P. and M. Schaerf, 1995, “Arbitration: a Commutative Operator for Belief Revision”, in *Proceedings of the Second World Conference on the Fundamentals of Artificial Intelligence*, pp. 217–228, Paris: Angkor Press.
[^liberatore-1998]: –––, 1998, “Arbitration (or How to Merge Knowledge Bases)”, *IEEE Transactions on Knowledge and Data Engineering*, 10(1): 76–90.
[^lin-1995]: Lin, J., 1995, *Frameworks for Dealing with Conflicting Information and Applications*, Ph.D. thesis, University of Toronto.
[^lin-1996]: –––, 1996, “Integration of Weighted Knowledge Bases”, *Artificial Intelligence*, 83: 363–378.
[^lin-1996-2]: Lin, J. and A. Mendelzon, 1996, “Merging databases under constraints”, *International Journal of Cooperative Information Systems*, 7: 55–76.
[^lin-1999]: –––, 1999, “Knowledge Base Merging by Majority”, in *Dynamic Worlds: From the Frame Problem to Knowledge Management*, R. Pareschi and B. Fronhöfer (eds), Norwell, MA: Kluwer, pp. 195–218.
[^list-2002]: List, C., 2002, “A Possibility Theorem on Aggregation over Multiple Interconnected Propositions”, *Mathematical Social Sciences*, 45(1): 1–13.
[^list-2013]: –––, 2013, “Social Choice Theory”, *The Stanford Encyclopedia of Philosophy* (Winter 2013 Edition), Edward N. Zalta (ed.), URL = <[https://plato.stanford.edu/archives/win2013/entries/social-choice/](https://plato.stanford.edu/archives/win2013/entries/social-choice/)>.
[^list-2002-2]: List, C. and P. Pettit, 2002, “Aggregating sets of judgments: an impossibility result”, *Economics and Philosophy*, 18: 89–110.
[^list-2004]: –––, 2004, “Aggregating Sets of Judgments: Two Impossibility Results Compared”, *Synthese*, 140: 207–235.
[^list-2009]: List, C. and C. Puppe, 2009, “Judgment Aggregation: A Survey”, in P. Anand, C. Puppe, and P. Pattanaik (eds.), *The Handbook of Rational and Social Choice*, Oxford: Oxford University Press, pp. 457–482.
[^meyer-2001]: Meyer, T., A. Ghose, and S. Chopra, 2001, “Social Choice, Merging and Elections”, in *Proceedings of the 6th European Conference on Symbolic and Quantitative Approaches to Reasoning with Uncertainty*, Benferhat and Besnard (eds.), Vol. 2143 of *Lecture Notes in Artificial Intelligence*, Berlin: Springer, pp. 466–477.
[^miller-2009]: Miller, M.K. and D. Osherson, 2009, “Methods for Distance-based Judgment Aggregation”, *Social Choice and Welfare*, 32(4): 575–601.
[^mongin-2008]: Mongin, P., 2008, “Factoring Out the Impossibility of Logical Aggregation”, *Journal of Economic Theory*, 141: 100–113.
[^morreau-2014]: Morreau, M., 2014, “Arrow’s Theorem”, *The Stanford Encyclopedia of Philosophy* (Winter 2014 Edition), Edward N. Zalta (ed.), URL = <[https://plato.stanford.edu/archives/win2014/entries/arrows-theorem/](https://plato.stanford.edu/archives/win2014/entries/arrows-theorem/)>.
[^pauly-2006]: Pauly, M. and M. van Hees, 2006, “Logical Constraints on Judgment Aggregation”, *Journal of Philosophical Logic*, 35: 569–585.
[^pettit-2001]: Pettit, P., 2001, “Deliberative Democracy and the Discursive Dilemma”, *Philosophical Issues*, 11: 268–299.
[^pigozzi-2006]: Pigozzi, G., 2006, “Belief merging and the discursive dilemma: an argument-based account to paradoxes of judgment aggregation”, *Synthese*, 152: 285–298.
[^poisson-1837]: Poisson, S.D., 1837, *Recherches sur la probabilité des jugements en matière criminelle et en matière civile: précédées des règles générales du calcul des probabilités*, Paris.
[^porello-2017]: Porello, D., 2017, “Judgment Aggregation in Non-Classical Logics”, *Journal of Applied Non-Classical Logics*, 27(1–2): 106–139.
[^reiter-1988]: Reiter, R., 1988, “On Integrity Constraints”, in M.Y. Vardi (ed.), *Proceedings of the Second Conference on the Theoretical Aspects of Reasoning about Knowledge*, San Francisco: Morgan Kaufmann, pp. 97–111.
[^revesz-1993]: Revesz, P., 1993, “On the Semantics of Theory Change: Arbitration between Old and New Information”, in C. Beeri (ed.), *Proceedings of the Twelfth ACM Symposium on Principles of Database Systems*, Washington D.C., pp. 71–82.
[^revesz-1997]: –––, 1997, “On the Semantics of Arbitration”, *International Journal of Algebra and Computation*, 7(2): 133–160.
[^roth-2011]: Roth, A.S., 2011, “Shared Agency”, *The Stanford Encyclopedia of Philosophy* (Spring 2011 Edition), E.N. Zalta (ed.), URL = <[https://plato.stanford.edu/archives/spr2011/entries/shared-agency](https://plato.stanford.edu/archives/spr2011/entries/shared-agency)>.
[^sen-1970]: Sen, A.K., 1970, *Collective Choice and Social Welfare*, San Francisco: Holden-Day.
[^spector-2009]: Spector, H., 2009, “The Right to a Constitutional Jury”, *Legisprudence*, 3(1): 111–123.
[^subrahmanian-1994]: Subrahmanian, V.S., 1994, “Amalgamating Knowledge Bases”, *ACM Transactions on Database Systems*, 19(2): 291–331.
[^vacca-1921]: Vacca, R., 1921, “Opinioni Individuali e Deliberazioni Collettive”, *Rivista Internazionale di Filosofia del Diritto*, 52: 52–59.
[^willamson-2009]: Willamson, J., 2009, “Aggregating Judgments by Merging Evidence”, *Journal of Logic and Computation*, 19(3): 461–473.
[^xuefeng-2018]: Xuefeng, W., 2018, “Judgment Aggregation in Nonmonotonic Logic”, *Synthese*, 195(8): 3651–3683.

## 学术工具

* [如何引用本词条](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=belief-merging)。
* [预览本词条的 PDF 版本](https://leibniz.stanford.edu/friends/preview/belief-merging/)，见 [SEP 学会之友](https://leibniz.stanford.edu/friends/)。
* 在 [InPhO](https://www.inphoproject.org/entity?sep=belief-merging&redirect=True) 查找与本词条相关的话题与思想家。
* 在 [PhilPapers](https://philpapers.org/sep/belief-merging/) 查看本词条的增强文献目录及其数据库链接。

## 其他网络资源

请与作者联系，提出建议。

## 相关词条

阿罗定理 | 社会认识论 | 陪审团定理 | 信念修正的逻辑 | 社会选择理论 | 社会程序的形式化进路

**（译注：相关词条的中文站内链接将由管线在对应词条重译完成后统一挂接。）**

## 致谢

笔者谨向 Eric Pacuit 与更新版词条的一位匿名审稿人致谢，他们的许多宝贵意见与本词条内容及可读性之改进大有裨益；并感谢 Erman Acar 指出前一版本中的若干笔误。
