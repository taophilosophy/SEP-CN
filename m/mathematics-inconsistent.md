# 不一致数学 inconsistent (Chris Mortensen)
*首次发表于 1996 年 7 月 2 日；2022 年 11 月 30 日实质修订。*

不一致数学研究这样一类数学理论：把经典数学公理安置在一种能容忍矛盾、而不使一切句子皆成定理的（非经典）逻辑框架之中，由此得到的理论。

## 1 数学基础

不一致数学在历史上始于基础之争。弗雷格与罗素提议把数学奠基于朴素集合论原则：每个谓词都有一个集合。可朴素原则转眼就导出罗素集的存在性证明——由一切不属于自身的集合组成的集合，它既属于又不属于自身。罗素等人注意到的这一悖论及同类集合论悖论，促使人们构造一致的集合理论来充当数学基础；其中最著名的当属策梅洛-弗伦克尔集合论 ZF。但 ZF 与 NBG 一类的理论各有特设之嫌：不得不容纳多条相互独立的原则，而非单一的简单概括公理。于是，da Costa（1974）、Brady（1971, 1989）、Priest、Routley 与 Norman（1989, pp. 152, 498）等人主张：更好的做法是保留自然概括公理的全部力量，容忍集合论中一定程度的不一致。Brady 尤其在其专著（2006）中扩展、精简并简化了朴素集合论上的这些结果；清晰的述评另见 Restall 的书评（2007）。

这些构造当然要求我们至少抛弃布尔逻辑的一条原则——**矛盾相容原则**（*ex contradictione quodlibet*，ECQ）：从矛盾可推出任意命题（亦称爆炸）。顺带一提，C.I.刘易斯证明：由析取三段论原则（DS）（从 *A* 或 *B* 与非 *A* 推出 *B*）出发，经一个简单论证即可得 ECQ。所以 DS 也必须抛弃。显然，ECQ 会让任何不一致理论平凡化（平凡性=一切句子皆可证）。非平凡性应当视为有趣理论的约束：平凡理论对数学计算毫无用处——它不把理论中的原理与其否定区分开。同样，大量争论（Burgess 1981, Mortensen 1983）[^burgess-1981][^mortensen-1983] 清楚表明：抛弃 DS 并不那么反直觉，尤其当一种合理解释浮现之后——它说明 DS 在哪些特殊条件下仍然成立。

还应当指出：Brady 对不一致朴素集合论的构造，为弗雷格-罗素逻辑主义的复兴敞开了大门（简言之，逻辑主义主张数学可还原为逻辑）。人们普遍认为——连弗雷格本人也不例外——逻辑主义已被罗素悖论重创。倘若罗素矛盾不扩散，那就没有明显的理由否定：朴素集合论为数学提供了充分的基础，而且朴素集合论可经朴素概括模式从逻辑中导出。唯一需要的改动，是换用一种容忍不一致的逻辑。更激进的是，Weber 在一系列论文（2010）、（2012）、（2013）中把不一致当作积极的优点：它使我们能解决康托尔留下的几个未决问题——良序定理与选择公理可证，而连续统假设为假（2012, 284）。其中一些结果被证得既真又假；Weber 在此着力推进的是 **经典回收** 的证明——一项表明传统结果仍可证明的工程（2010, 72）。这是令人振奋的新天地。Weber 还证明了此工程不可或缺的一点：康托尔定理继续成立——它不依赖被弗协调主义者质疑的过强逻辑原则。在他看来，保住康托尔定理至关重要：在不一致集合论中，不同阶的无穷依然可用。

此外，数学自带一套元语言机制——谈论数学本身的机制。它包括这些概念：（i）数学语句与语法其他部分的名称，（ii）自指，（iii）证明，（iv）真理。哥德尔对数学哲学的贡献在于表明：前三个概念可以在算术理论中得到严格表达——尽管是在要么不一致、要么不完备的理论之中。而上述两种替代中，前者（不一致）的一个结构良好的实例，其可能性从未被认真对待——又是因为对 ECQ 的执念。然而，自然语言似乎自带真谓词；与自指相结合，便产生说谎者悖论——“这句话是假的”——一种不一致。Priest（1987）与 Priest、Routley、Norman（1989, p. 154）论证：说谎者必须被视为既真又假的陈述，一个真矛盾。这构成了研究不一致理论的又一个理由——某些矛盾为真的主张，即所谓 **双面真理论**。Kripke（1975）则提出以另一种方式给真谓词建模：在一个一致而不完备的理论中。下文可见，不完备与不一致密切相关。

把动机简化来说：数学与许多别的科学一样，会遭遇反常、谜题与悖论。悖论典型地以矛盾的面目出现——其中存在接受矛盾两方的理由。数学的进步至少部分地靠消除反常、代之以一致的重构；这一直是处理反常的典型办法，而注意到矛盾出现在数学基础之中，又为它提供了便利。但二十世纪晚期人们注意到另一条路：接受矛盾，发展出同时容纳矛盾双方的数学理论。倘若矛盾理论立于一条含布尔原则 Ex Contradictione Quodlibet（ECQ：从矛盾得出一切）的逻辑基础之上，这条路便走不通。所以 ECQ 必须抛弃——所幸这被证明可能，而且在数学上直截了当。剩下的是一片富饶的田野：新颖的数学应用自具趣味；它们绕开“该采纳哪些基础原则”的恼人问题，在远离基础的领域——数论、分析——里发展矛盾。这就是不一致数学。

## 2 算术

但以上所言皆关乎基础，而数学并非其基础。因此还有一层独立的动机：看看 **无论何处**、一旦放松一致性约束，还能剩下什么样的数学结构。可若把这看作对经典数学所研究结构的任何意义上的拒斥，就错了：不一致的结构是对已知结构的 **增补**。

Robert K. Meyer（1976）看来是第一个想到不一致算术理论的人。彼时他更关心一个一致理论的命运——他的相干算术 R#：相当于皮亚诺算术的公理，配以量化相干逻辑 RQ 作底；Meyer 盼望相干逻辑这个较弱的基础能容纳更多模型。他料中了。事实证明存在整整一族不一致算术理论；例如见 Meyer and Mortensen（1984）。与上文复兴逻辑主义的议论相呼应，Meyer 主张：这些算术理论为复兴的希尔伯特纲领提供了基础。希尔伯特纲领，是严格形式化数学、再以简单的有穷/归纳程序证明其一致性的工程；人们普遍认为它已被哥德尔第二不完备性定理重创——按该定理，算术的一致性在算术内部不可证。但 Meyer 构造的一个后果是：在他的算术 R# 之内，可以用有穷手段证明——无论碰巧有什么矛盾，它们都伤不了任何数值计算。于是，只要改用容忍不一致的逻辑，希尔伯特“确凿证明数学无虞”的目标就在很大程度上可以实现。

Meyer 与 Mortensen 所用的算术模型，后来被证明允许对真谓词作不一致表示；它们还允许表示自然数算术之外的结构——环与域，连同其序性质；公理化亦已给出。最近，有限不一致算术塌缩模型——一个严格大于 Meyer 与 Mortensen 模型类的类——已被 Graham Priest 完全刻画。塌缩模型的造法：把经典模型的论域塌缩到由各种同余关系生成的同余类。同一同余类的成员一经等同，所得理论便是不一致的。例如，Meyer 的初始构造把整数按 **模 2** 同余塌缩——0 与 2 落入同余类，于是在某个合适的三值逻辑里，0=2 与非-(0=2) 同时成立。Priest 证明这类模型取某种一般形式（见 Priest 1997、2000）。严格说来，Priest 把“小集团模型”也纳入其中，走得略远了些——Paris 与 Pathmanathan（2006）后来修正了这一点，Paris 与 Sirokfskich（2008）又推广到无穷情形。更近，Tedder（2015）换用不同的背景逻辑——Avron 的 A3——为有限塌缩模型类取得了公理化。

## 3 分析

人们很难忽视分析学及其特例——微积分——的例子。模型论进路见 Mortensen（1990, 1995）。

Meyer 对自然数的原初进路（即 R#）是公理化的，不是模型论的。公理化进路后来也被 McKubre-Jordens 与 Weber（2012）用于 **分析**：以弗协调逻辑为底公理化分析，把 Meyer 经 R# 处理算术的做法向前推进了一大步。同一批作者（2017）又以弗协调推理重做了阿基米德手中的积分论——它用的是穷竭法。这给出“直到不一致”的结果：人们能证明“经典结果或矛盾”。随后经经典的斧钺——对经典为假（不一致）的第二个析取支施用析取三段论——经典结果便可重新夺回。

追求这一方向当然重要而值得，但这里要敲一记温和的警钟：公理化工程与不一致数学略有不同。如前所述，Meyer 在这一阶段是个一致主义者——他寻求的是一个带容忍不一致之逻辑的一致理论。出于类似动机，他还致力于解决他所谓的“伽马问题”：本质上就是，公理理论 R# 能否被证明包含经典皮亚诺算术作为子理论。若果真如此，他对 R# 非平凡性的证明将立即产出经典皮亚诺算术否定一致性的一个新证明！注意，这并不与哥德尔第二定理相抵——因为伽马结果的证明想必不会局限于有穷技术。（就 Meyer 的理论而言，答案是否。）

事实证明，整个分析学里处处可见独特的不一致洞见。本节余下的例子取自 Mortensen（1995）。例如：（1）Robinson（1974）的非标准分析以无穷小——小于任何实数的量——及其倒数（无穷大数）为基础。它有一个不一致版本，在计算上自有优势：可丢弃高阶无穷小。有趣的是，微分论坐拥这些优势，积分论却没有。Da Costa（2000）以不同的背景逻辑得到类似结果。（2）分析中不一致的另一个用武之地是拓扑学：人们容易观察到，切割与粘贴空间的做法被描述为把一个边界与另一个“认同”。可以证明：这可在不一致理论中描述——两个边界既同一又不同一——而且还可进一步论证，这就是对该实践最自然的描述。（3）另一个应用是不一致连续函数类。并非所有经典不连续的函数都能作不一致处理，但有些能——例如对所有 *x*<0，*f*(*x*)=0；对所有 *x*≥0，*f*(*x*)=1。不一致扩展把第一个 < 换成 ≤，并具有独特的结构性质。这些不一致函数在存在不连续跳变的动态系统中——如量子测量系统——可能大有用处。对这类函数求微分即得 delta 函数，Dirac 曾把它用于量子测量的研究。（4）再者是众所周知的不一致线性方程组，如（i）*x*+*y*=1 与（ii）*x*+*y*=2。这样的系统可能出现在自动控制的语境中。经典上鲜有求解此类系统的工作，但可以证明：在不一致向量空间中存在良态的解。（5）最后，拓扑学与动力学中还有一个应用。给定一个看似可设想的假定：无论何事发生或何者为真，都是在（时空）点的一个开集上发生或为真。那么动力学可能路径的逻辑就是开集逻辑，也就是直觉主义逻辑——它出类拔萃地支持不完备理论。理由在于，这种空间中命题之否定的自然说明是：否定成立于包含原命题点集之布尔补的最大开集——它一般小于布尔补。然而，以闭集规定拓扑空间，与以开集规定它同样合理；而闭集的逻辑已知是弗协调的——支持不一致的非平凡理论；例如见 Goodman（1981）。于是，给定另一个看似同样可设想的假定——无论何者为真，都在点的一个闭集上为真——不一致理论就很可能成立。理由在于：对命题之否定的自然说明是，否定成立于包含该命题布尔否定的最小闭集；这意味着在交叠的边界上，命题与其否定同时成立。因此，动力学理论决定着它们自己的可能命题逻辑，以及相应的、可能不一致的理论——它们与其不完备对应物同样自然。

关于闭集逻辑与边界作为矛盾理论之自然处境，见 Mortensen（2003, 2010）。Weber 与 Cotnoir（2015）也探究了边界的不一致性——它源自三条原则的不相容：（i）存在边界；（ii）空间在拓扑上连通；（iii）离散实体可以接触（彼此之间没有空间）。这个问题极为有趣，因为三条都合理；尤其，我们的世界里似乎确有边界。这一说明起初令人惊讶之处在于：边界竟是“空的”——空实体总归有悖部分学的精神。但细想并不那么骇人：它们只是在一种意义上为空——不一致地拥有成员。

范畴论照亮了许多数学结构；它确实曾被提议为数学的另一种基础。这般普遍性不可避免地撞上与集合论概括类似的难题；例如见 Hatcher 1982（pp. 255–260）。因此，不一致解有同样的用武之地。还有一族重要的范畴结构——拓扑斯（toposes）：它们支持开集逻辑的方式，与集合支持布尔逻辑的方式恰成平行。许多人以此作为直觉主义之基础观点的辩护。然而可以证明：拓扑斯支持闭集逻辑，一如它们支持开集逻辑——这是迄今为止唯一的弗协调逻辑范畴论语义。但这不该视作对直觉主义的反驳，而该视作一个论证：不一致的理论作为数学研究对象同样合理。见 Mortensen（1995 第 11 章，合著者 Lavers）。这一立场如今已被 Estrada-González（2010, 2015a, 2015b）接手、扩展并有力辩护。同一作者（2016）进而为平凡理论提供范畴论描述，意在表明：平凡性对数学理论而言并非那么无趣的特征。笔者仍然不被说服——平凡理论对数学计算肯定无用；但这些论证的巧妙必须承认。

不完备／直觉主义与不一致／弗协调之间的对偶，至少有两副面孔。其一是上述拓扑（开/闭）对偶；其二则是 Routley 星对偶。句子集 *S* 的 Routley 星 ＊ 定义为 *S** =_{*df*} {*A*: ~*A* 不属于 *S*}。它由 Routley 夫妇（1972）发现，原是相干逻辑的语义工具：＊ 运算在大类德摩根逻辑的不一致理论与不完备理论之间往返对偶。例如，对皮亚诺算术施加星运算，便得到一个演绎封闭、不一致、完备、非平凡的经典算术理论——它包含全部 PA，给哥德尔不完备性结果出了道有趣的难题（见 Mortensen 2013）。两种对偶还会相互作用：* 为开集与闭集算术理论给出独特的对偶定理与不变性定理。基于这些结果，我们尽可以说：两种数学——直觉主义的与弗协调的——同样合理。

## 4 几何不一致

几何学方向之一，是应用于解释不一致图画的现象。其中最著名的，或许是 M. C. 埃舍尔的杰作《观景楼》《瀑布》与《上行与下行》。这一传统其实可以上溯数千年至庞贝。埃舍尔的许多直觉似乎取自瑞典艺术家 Oscar Reutersvärd——后者 1934 年起便开始其不一致创作；埃舍尔还与英国数学家罗杰·彭罗斯积极合作。Cowan、Francis、Penrose 等理论家曾多次尝试以经典一致数学刻画不一致图画的数学结构。然而正如 Mortensen（1997）所论：没有任何一致的数学理论能捕捉“人正在看一件不可能之物”的那种感觉；唯不一致理论能捕捉那份知觉的内容。这相当于为弗协调性提出一种认知辩护。于是，人们可以进而展示一批候选的不一致理论，以充当这些不一致内容。在这点上与经典数学有类似之处：射影几何是一门经典且一致的数学理论，它之所以有趣，是因为我们是长着眼睛的造物——它解释了事物在透视中为何显得是那个样子。

不一致几何研究在 Mortensen（2002a）中继续推进：范畴论被用来一般地刻画各理论与其一致截断、不完备对偶之间的关系。至于视觉“悖论”与哲学上更常见的语言悖论（如说谎者）之别，通俗说明见 Mortensen（2002b）。

晚近，若干类不一致图形已获得不一致的数学描述——例如埃舍尔立方体（见于其版画《观景楼》）、路特斯瓦德-彭罗斯三角等。见 Mortensen（2010）。

这又引出一个有趣的问题。自欧几里得以降，归谬法在几何证明中已被用到极致（假设你想证的命题之反面，再导出矛盾）。但我们这里有的是另一种技术：调用一个矛盾来描述不一致图形的模样，以证明其内容货真价实地矛盾。若成功，这便是下述证明：人类的概念化活动超出了单纯可能的东西（即一致的东西）。讨论见 Mortensen（2019, 2022）。

还有一点：这些几何悖论是否支持彻底的双面真理论？答案是否。若你能画出一幅矛盾的图画，那便有 **某物** 存在，它是不一致的；而且，互异的不一致图形蕴涵矛盾类型之间的分野——ECQ 不容许这种分野。但不可把话说过了头：没有什么规定，图画有内容、内容就必须以某种方式为 **真**——许多图画的内容纯属虚构。这一主题的进一步讨论见 Mortensen（2019a）。

## 5 分块渗透

晚近，一种处理矛盾的一般性替代技术登场了。Brown 与 Priest（2004）提出一种他们名为“分块渗透”的技术：从不一致前提出发的推理，先把假设拆成一致的理论（分块），导出相应结论；再把（渗透）这些结论传给另一个分块，继续导出进一步结论。他们提出：牛顿在微积分中求导数的原初推理，正是这种形式。这是一条有趣而新颖的进路，但它必须顶住如下反对：要相信由此得到的结论，就应当同等相信全部前提；因此，一种更常见形式的论证——整体诉诸前提而不打碎它们——终将应当登场。反对意见因而是：分块渗透属于发现语境，而非辩护语境。

后来，Benham 等（2014）把这些方法扩展到狄拉克 delta 函数——应用的类拓宽了，技术也得到加强。但那里同时显露出：（一大类）分块渗透应用与（一致的）非标准分析之间存在密切的平行：分块渗透靠“跳到无穷小为零的分块”来求导，非标准分析则靠“把导数定义为仅取标准部分”来求导。当然，两种技术的等价并不表明谁在解释上更深。进展值得期待。

## 6 结论

总而言之：近来出现了相当多同情不一致数学事业的哲学材料。Colyvan（2000）处理了“不一致数学理论蕴涵不一致数学对象为其论题”的问题；他还接下重要任务：说明不一致数学如何能拥有一个 **应用的** 分支。Priest（2013）与 Colyvan 一样，注意到不一致数学给柏拉图主义的配方添了料。Berto（2007）对悖论与基础问题作了有用的综述，并给出触及重大哲学问题（如不完备性定理）的若干算术结果。Van Bendegem（2014）追索一个有趣的动机：变化总是反常的状态，故永远变化便蕴涵永远反常——无穷小、复数与无穷皆是例子。但对“不一致总是反常”的想法应持谨慎——单单因为，不一致只是数学研究的更多素材而已。

应当再次强调：这些结构绝不挑战或拒斥现有数学，而是拓展我们对“数学上可能”的构想。这反过来又把数学多元主义的问题磨得更尖；例如见 Davies（2005）、Hellman 与 Bell（2006）或 Priest（2013）。诸家对数学多元主义的版本各异，但大意是：不相容的数学理论可以同样为真。其理据在于这样的观察：存在不同的数学“宇宙”，其中成立着不同的、乃至不相容的数学定理或定律。著名例子：经典数学与直觉主义数学互不相容；带选择公理与不带选择公理的 ZF 式集合宇宙互不相容。倘若说带选择公理的 ZF 是真数学、不带选择公理的 ZF 是假数学，那就荒谬了——只要它们都是数学上良态理论的合法例子。

数学哲学的首要问题无疑是 **数学是什么**。拓扑对偶、Routley 星这类对偶运算强化了这一点：不完备／不一致的对偶，作为数学的例子同样合理。从这个角度看，关于该接受直觉主义数学、经典数学还是不一致数学的争论，似乎没有意义——它们全是数学论题的一部分。Shapiro（2014；对照见其 2002）有力地提出了这一点。Shapiro 的独特立场还有别的成分：数学作为结构的科学；数学多元主义蕴涵逻辑多元主义（逻辑多元主义另见 Beall and Restall 2006）[^beall-2006]。但这些此处不表。

无论如何，笔者以为：若把数学首先看作允许不一致的数学理论、其次才看作那些理论内部的对象，那么某种版本的数学多元主义显然为真。当然，把不相容的理论视为命题结构，它们的共存没有任何问题。理论的优先性也合乎一个自然的观察：数学的认识论是演绎证明。只有当人把“数学对象优先、作为理论的真理制造者”当作出发点时，才须操心这些对象如何设法共存。

## References（引用注释）

**以下文献从原文照录，不作翻译；中国文献译为中文。**

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

[^beall-2006]: Beall, J.C. and G. Restall, 2006, *Logical Pluralism*, Oxford: The Clarendon Press.
[^benham-2014]: Benham, R., C. Mortensen and G. Priest, 2014, “Chunk and Permeate III: The Dirac Delta Function”, *Synthese*, 191(13): 3057-3062. doi:10.1007/s11229-014-0473-7
[^berto-2007]: Berto, F., 2007, *How to Sell a Contradiction*, London: College Publications.
[^brady-1971]: Brady, R., 1971, “The Consistency of the Axioms of Abstraction and Extensionality in a Three-Valued Logic”, *Notre Dame Journal of Formal Logic*, 12: 447–453.
[^brady-1989]: –––, 1989, “The Nontriviality of Dialectical Set Theory”, in G. Priest, R. Routley and J. Norman (eds.), *Paraconsistent Logic*, Munich: Philosophia Verlag.
[^brady-2006]: –––, 2006, *Universal Logic*, Stanford: CSLI Publications.
[^brown-2004]: Brown, B., and G. Priest, 2004, “Chunk and Permeate: A Paraconsistent Inference Strategy. Part I: The Infinitesimal Calculus”, *The Journal of Philosophical Logic*, 33: 379–388.
[^burgess-1981]: Burgess, J., 1981, “Relevance, a Fallacy?”, *Notre Dame Journal of Formal Logic*, 22: 97–104.
[^colyvan-2000]: Colyvan, M., 2000, “Applying Inconsistent Mathematics”, *New Waves in the Philosophy of Mathematics*, O.Bueno and O. Limmbo (eds.), London: Palgrave McMillan, 160-172.
[^da-1974]: Da Costa, Newton C.A., 1974, “On the Theory of Inconsistent Formal Systems”, *Notre Dame Journal of Formal Logic*, 15: 497–510.
[^da-2000]: –––, 2000, “Paraconsistent Mathematics”, in D. Batens *et al*. (eds.), *Frontiers of Paraconsistent Logic*, Hertfordshire: Research Studies Press, 165–180.
[^davies-2005]: Davies, E.B., 2005 “A Defence of Mathematical Pluralism ”, *Philosophia Mathematica*, 13: 252–276.
[^estrada-gonzález-2010]: Estrada-González, L., 2010, “Complement-Topoi and Dual Intuitionistic Logic”, *Australasian Journal of Logic*, 9: 26–44.
[^estrada-gonzález-2015a]: –––, 2015a, “The Evil Twin: The Basics of Complement-toposes”, in Beziau, Chakraborty and Dutta (eds.), *New Directions in Paraconsistent Logic*, Dordrecht: Springer: 375-425.
[^estrada-gonzález-2015b]: –––, 2015b, “From (paraconsistent) topos logic to Universal (topos) logic”, in Koslow and Buchsbaum (eds.), *The Road to Universal Logic: Festschrift for Jean-Yves Beziau on his Fiftieth Birthday*, Dordrecht: Springer, 263-295.
[^estrada-gonzález-2016]: –––, 2016, “Prospects for Triviality”, in H. Andreas and P. Verdee (eds.), *Logical Studies of Paraconsistent Reasoning in Science and Mathematics*, Dordrecht: Springer, 81-89.
[^goodman-1981]: Goodman, N., 1981, “The Logic of Contradictions”, *Zeitschrift fur Mathematische Logic und Grundlagen der Arithmetik*, 27: 119–126.
[^hatcher-1982]: Hatcher, W. S., 1982, *The Logical Foundations of Mathematics*, Oxford: Pergamon.
[^hellman-2006]: Hellman, G. and J. Bell, 2006, “Pluralism and the Foundations of Mathematics”, in C.K. Waters et al. (eds.), *Scientific Pluralism* (Minnesota Studies in the Philosophy of Science, Volume XIX), Minneapolis: University of Minnesota Press.
[^kripke-1975]: Kripke, S., 1975, “Outline of a Theory of Truth”, *The Journal of Philosophy*, 72: 690–716.
[^mckubre-jordens-2012]: McKubre-Jordens, M., and Zach Weber, 2012, “Real Analysis and Paraconsistent Logic”, *Journal of Philosophical Logic*, 41(5): 901–922.
[^meyer-1976]: Meyer, R. K., 1976, “Relevant Arithmetic”, *Bulletin of the Section of Logic of the Polish Academy of Sciences*, 5: 133–137.
[^meyer-1984]: Meyer, R. K. and C. Mortensen, 1984, “Inconsistent Models for Relevant Arithmetics”, *The Journal of Symbolic Logic*, 49: 917–929.
[^mortensen-1983]: Mortensen, C., 1983, “Reply to Burgess and to Read”, *Notre Dame Journal of Formal Logic*, 24: 35–40.
[^mortensen-1990]: –––, 1990, “Models for Inconsistent and Incomplete Differential Calculus”, *Notre Dame Journal of Formal Logic*, 31: 274–285.
[^mortensen-1995]: –––, 1995, *Inconsistent Mathematics*, Kluwer Mathematics and Its Applications Series, Dordrecht: Kluwer. [[Errata available online](https://www.adelaide.edu.au/directory/chris.mortensen?dsn=directory.file;field=data;id=15292;m=view).]
[^mortensen-1997]: –––, 1997, “Peeking at the Impossible”, *Notre Dame Journal of Formal Logic*, 38: 527–534.
[^mortensen-2000]: –––, 2000, “Prospects for Inconsistency”, in D. Batens *et al*. (eds.), *Frontiers of Paraconsistent Logic*, London: Research Studies Press, 203–208.
[^mortensen-2002a]: –––, 2002a, “Towards a Mathematics of Impossible Pictures”, in W. Carnielli, M. Coniglio and I. D’Ottaviano (eds.), *Paraconsistency: The Logical Way to the Infinite*, (Lecture Notes in Pure and Applied Mathematics, Volume 228), New York: Marcel Dekker, 445–454.
[^mortensen-2002b]: –––, 2002b, “Paradoxes Inside and Outside Language”, *Language and Communication*, 22: 301–311.
[^mortensen-2003]: –––, 2003, “Closed Set Logic”, in R. Brady (ed.), *Relevant Logics and Their Rivals* (Volume II), Aldershot: Ashgate, pp. 252-262 (especially 255-6).
[^mortensen-2006]: –––, 2006, “An Analysis of Inconsistent and Incomplete Necker Cubes”, *Australasian Journal of Logic*, 4: 216–225.
[^mortensen-2010]: –––, 2010, *Inconsistent Geometry* (Studies in Logic, Volume 27), London: College Publications (King’s College).
[^mortensen-2011]: –––, 2011, “Merge”, *Australasian Journal of Logic*, 9: 135–141.
[^mortensen-2013]: –––, 2013, “Arithmetic Starred”, in K. Tanaka, F. Berto, E. Mares and F. Paoli (eds.), *Paraconsistency: Logic and Applications*, Dordrecht: Springer, 309–314.
[^mortensen-2019]: –––, 2019, “Euclid's Geometry: the Case of Contradiction”, *Journal of Modern Greek Studies* (Australia and New Zealand), Special Issue, 2019, 71–83.
[^mortensen-2019a]: –––, 2019a, “Dialethism and Impossible Figures”, in A. Rieger and G. Young (eds.), *Dialetheism and Its Applications*, Cham: Springer International Publishing, 185–194.
[^mortensen-2022]: –––, 2022, *The Impossible Arises*, Bloomington, Indiana University Press.
[^paris-2006]: Paris, J., and Pathmanathan, N., 2006, “A Note on Priest’s Finite Arithmetics”, *The Journal of Philosophical Logic*, 35: 529–537.
[^paris-2008]: Paris, J., and Sirokofskich, A., 2008, “On LP-models of Arithmetic”, *The Journal of Symbolic Logic*, 73(1): 212–226.
[^priest-1987]: Priest, G., 1987, *In Contradiction*, Dordrecht: Nijhoff; second expanded edition, Oxford: The Clarendon Press, 2006.
[^priest-1997]: –––, 1997, “Inconsistent Models for Arithmetic: I, Finite Models”, *The Journal of Philosophical Logic*, 26: 223–235.
[^priest-2000]: –––, 2000, “Inconsistent Models for Arithmetic: II, The General Case”, *The Journal of Symbolic Logic*, 65: 1519–29.
[^priest-2013]: –––, 2013, “Mathematical Pluralism”, *Logic Journal of IGPL*, 21(1): 4–13: doi:10.1093/jzs018
[^priest-1989]: Priest, G., R. Routley and J. Norman (eds.), 1989, *Paraconsistent Logic*, Munich: Philosophia Verlag.
[^restall-2007]: Restall, G., 2007, “Review of Brady *Universal Logic*”, *Bulletin of Symbolic Logic*, 13(4): 544–547.
[^robinson-1974]: Robinson, A., 1974, *Non-standard Analysis*, Amsterdam: North-Holland, revised edition.
[^routley-1972]: Routley, R. and V. Routley, 1972, “The Semantics of First Degree Entailment”, *Noûs*, 6: 335–359.
[^shapiro-2002]: Shapiro, S., 2002, “Inconsistency and Incompleteness”, *Mind*, 111: 817–832.
[^shapiro-nd]: –––, “Structures and Logics: a Case for (a) Relativism”, *Erkenntnis*, 79: 309–329.
[^tedder-2015]: Tedder, A., 2015,“Axioms for Finite Collapse Models of Arithmetic”, *The Review of Symbolic Logic*, 8(3): 529-539.
[^van-2014]: Van Bendegem, J-P., 2014, “Inconsistency in Mathematics and the Mathematics of Inconsistency”, *Synthese*, 191(13), 3063-3078.
[^weber-2010]: Weber, Z., 2010, “Transfinite Numbers in Paraconsistent Set Theory”, *The Review of Symbolic Logic*, 3(1): 71-92.
[^weber-2012]: –––, 2012, “Transfinite Cardinals in Paraconsistent Set Theory”, *The Review of Symbolic Logic*, 5(2): 269–293.
[^weber-2013]: –––, 2013, “Notes on Inconsistent Set Theory”, in K. Tanaka, F. Berto, E. Mares and F. Paoli (eds.), *Paraconsistency: Logic and Applications*, Dordrecht: Springer, 315–328.
[^weber-2015]: ––– and Cotnoir, A.J., 2015, “Inconsistent Boundaries”, *Synthese*, 192: 1267–1294. doi:10.1007/511229-014-0614-2
[^weber-2017]: Weber, Z., and M. McKubre-Jordens, 2017, “Paraconsistent Measurement of the Circle”, *Australasian Journal of Logic*, 14(1): doi:10.26686/ajl.v14i1.4034

## 学术工具

* [如何引用本词条](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=mathematics-inconsistent)。
* [预览本词条的 PDF 版本](https://leibniz.stanford.edu/friends/preview/mathematics-inconsistent/)，见 [SEP 学会之友](https://leibniz.stanford.edu/friends/)。
* 在 [InPhO](https://www.inphoproject.org/entity?sep=mathematics-inconsistent&redirect=True) 查找与本词条相关的话题与思想家。
* 在 [PhilPapers](https://philpapers.org/sep/mathematics-inconsistent/) 查看本词条的增强文献目录及其数据库链接。

## 其他网络资源

[欢迎向作者提出建议。]

## 相关词条

矛盾 | 次协调逻辑 | 数学哲学 | 自我指涉

**（译注：相关词条的中文站内链接将由管线在对应词条重译完成后统一挂接。）**
