# 逻辑代数的传统 The Algebra of Logic Tradition (Stanley Burris、Javier Legris)

*首次发表于 2009 年 3 月 2 日；2021 年 2 月 12 日实质修订。*

**逻辑代数**（algebra of logic）作为展示逻辑底层数学结构的 **显式** 代数系统，由乔治·布尔（George Boole，1815–1864）在《逻辑的数学分析》（*The Mathematical Analysis of Logic*，1847）中引入，因此须与更一般的 **代数逻辑**（algebraic logic）进路相区别。布尔开创的方法论在十九世纪由威廉·斯坦利·杰文斯（William Stanley Jevons，1835–1882）、查尔斯·桑德斯·皮尔士（Charles Sanders Peirce，1839–1914）、恩斯特·施罗德（Ernst Schröder，1841–1902）等人成功延续，从而在（数学）逻辑中确立了一个传统。自布尔的第一部书，直到第一次世界大战后怀特海（Alfred North Whitehead，1861–1947）与罗素（Bertrand Russell，1872–1970）巨著《数学原理》（*Principia Mathematica*，1910–1913）产生影响为止，逻辑代数的各种版本都是数理逻辑最发达的形式，尤其体现在施罗德三卷本《逻辑代数讲义》（*Vorlesungen über die Algebra der Logik*，1890–1905）中。此外，这一传统激发了勒文海姆（Leopold Löwenheim，1878–1957）的研究，最终催生模型论。1941 年，塔斯基（Alfred Tarski，1901–1983）又在《论关系演算》一文中，回到施罗德《逻辑代数》所呈现的皮尔士关系代数。逻辑代数传统在“逻辑作为演算”（Logic as Calculus）而非“逻辑作为普遍语言”（Logic as Universal Language）这一观念中起了关键作用。除塔斯基的关系代数，代数传统在逻辑中的影响还可见于范畴论等其他数学理论。不过这一影响超出本词条范围；本词条分为 10 节。

## 1 导论

布尔《逻辑的数学分析》呈现许多有趣的逻辑新意：它开启了十九世纪逻辑的数学化，并以 **算法** 替代传统逻辑所用的 **目录** 进路（通过对普通代数略作修改；即便目录进路也发展出归约程序）。它不再罗列有效论证形式，而是依据一般原理与规则判定论证的有效性。此外，它为在公设系统基础上证明逻辑规律提供了有效方法。正如布尔后来所写，它是一门真正的“推理科学”，而非传统三段论那样的“记忆术”（Boole 1997: 136）[^boole-1997]。全书写至四分之三处、结束三段论逻辑讨论之后，布尔开始发展那些将用于《思维规律》（1854）的一般工具，以大大扩展传统逻辑：允许论证有许多前提并涉及许多类。为处理这一扩展逻辑中无限多的可能论证，他提出若干定理，为算法分析提供关键工具——目录法已不可行。

布尔的想法独立于莱布尼茨等更早的先行者而构思出来，产生于英国数学的特定语境（见 Peckhaus 2009）[^peckhaus-2009]。据维克托·桑切斯·巴伦西亚（Víctor Sánchez Valencia），自 1879 年亚历山大·麦克法兰（Alexander MacFarlane）《逻辑代数原理》出版后，源于布尔的传统便被称为 **逻辑代数**（见 Sánchez Valencia 2004: 389）[^sánchez-2004]。麦克法兰把“布尔所提出的关于性质的解析推理方法”视为一种代数（见 MacFarlane 1879: 3）。

这一进路不同于通常所谓的 **代数逻辑**；二者虽有一些重叠，但历史发展不同。代数逻辑被理解为：

> ［逻辑的］ **一种风格**，其中概念与关系由数学符号表达［$\ldots$］，以便数学技术得以应用。此处数学主要指代数，即处理某集合上有限运算的那部分数学。（Hailperin 2004: 323）[^hailperin-2004]

代数逻辑已可见于莱布尼茨、雅各布·伯努利等近代思想家的著作，无疑是布尔进路的重要先导。从更广的视角看，二者都属于形式科学中 **符号知识** 的传统，这一传统最早由莱布尼茨构想（见 Esquisabel 2012）[^esquisabel-2012]。这种代数逻辑观念在法国启蒙运动中由孔狄亚克与孔多塞的工作在某种程度上延续（见 Grattan-Guinness 2000: 14 以下）[^grattan-guinness-2000]

布尔处理逻辑问题的方法论可描述如下：

1. 把逻辑材料翻译为合适的方程；
2. 应用代数技术求解这些方程；
3. 若可能，把解译回原语言。

换言之，逻辑问题的符号表述与逻辑方程的求解构成了布尔的方法（见 Sánchez Valencia 2004: 389）[^sánchez-2004]。

后来，在 1864 年的《纯粹逻辑》中，杰文斯把布尔关于不相交集合之并的部分运算改为现代的无限制并，并消除了布尔对不可解释项的可疑使用（见 Jevons 1890）[^jevons-1890]。皮尔士（1880）通过赋予“所有 $A$ 是 $B$”以现代含义，明确取消了从全称陈述推出特称陈述的亚里士多德式导出。此外，他把关于类的逻辑代数扩展为关于二元关系的逻辑代数，并引入一般和与积以处理量化。恩斯特·施罗德受赫尔曼（1809–1877）与罗伯特·格拉斯曼（1815–1901）先前工作的启发，利用皮尔士发展的框架，在三卷本《逻辑代数讲义》（1890–1910）中发展并系统化了十九世纪逻辑代数的成就。

戈特洛布·弗雷格（Gottlob Frege，1848–1925）1879–1903 年间基于 **公理化** 进路的逻辑贡献，在当时影响很小（皮尔士世纪之交发展的 **图式** 系统亦如此）。怀特海与罗素拒斥逻辑代数进路及其以方程为主的表述和代数符号。他们转而采用深受弗雷格公理系统启发的进路，并使用皮亚诺（Giuseppe Peano）发展的记号，即逻辑联结词、关系符号与量词。

二十世纪头二十年，逻辑代数在普拉顿·谢尔盖耶维奇·波列茨基（Platon Sergeevich Poretzsky，1846–1907）、路易·库蒂拉（Louis Couturat，1868–1914）、勒文海姆与海因里希·贝曼（Heinrich Behmann，1891–1970）的工作中得到进一步发展（见 Styazhkin 1969）[^styazhkin-1969]。尤其，逻辑代数中的消去定理影响了一阶与二阶逻辑片段的判定程序（见 Mancosu, Zach, Badesa 2009）。

第一次世界大战后，起初采纳代数进路的希尔伯特（David Hilbert，1862–1943）转向《数学原理》的进路，逻辑代数遂失宠。然而，1941 年塔斯基把关系代数处理为一个由等式定义的类。这样的类除十九世纪所考虑的 **给定论域上一切二元关系的集合** 之外，还有许多模型；正如布尔代数除十九世纪所研究的 **幂集布尔代数** 之外还有许多。1948–1952 年间，塔斯基与其学生钦（Chin）和汤普森（Thompson）创建柱形代数，作为一阶逻辑的代数逻辑伴侣；1956 年哈尔莫斯（Paul Halmos，1916–2006）出于同一目的引入多元代数。正如哈尔莫斯（1956 b, c, d）所指出的，这些新代数逻辑倾向于聚焦于它们捕捉一阶逻辑的程度，以及其泛代数方面（如公理化与结构定理）。至于激发其创造的一阶逻辑本身有何本性，它们却很少提供洞见。

## 2 1847——逻辑代数现代版本的开端

1847 年末，布尔与奥古斯都·德摩根（Augustus De Morgan，1806–1871）各出版了一部逻辑书：布尔的《逻辑的数学分析》（1847）与德摩根的《形式逻辑》（1847）。德摩根的做法是把传统演绎逻辑（通常称“亚里士多德逻辑”）的每一方面剖析到最细微成分，考虑推广这些成分的方式，然后有时尝试用这些成分构建逻辑系统。不幸的是，他始终未能把最好的想法整合成一个重要系统。他省略等号符号，使发展等式逻辑代数成为不可能。看来综合并非德摩根的强项。

德摩根 1847 年的书属于十九世纪初兴起的一场逻辑研究复兴，代表人物包括法国的约瑟夫·迪耶兹·热尔戈纳（Joseph Diez Gergonne，1771–1859）与波希米亚的伯纳德·波尔查诺（Bernhard Bolzano，1781–1848）等。英国的乔治·边沁与威廉·汉密尔顿也属于这场复兴，他们的研究聚焦于传统三段论中直言句变体的本性，包括所谓“谓词的量化”，例如“所有 $A$ 都是某些 $B$”或“某些 $A$ 是全部 $B$”。人们认为，这一问题要求扩展亚里士多德的三段论逻辑，并需要某种符号方法来处理这类陈述、为其不同类型提供分类（见 Heinemann 2015 第 2、3 章）[^heinemann-2015]。

布尔从完全不同的视角接近逻辑：如何把亚里士多德逻辑装入符号代数的外衣。使用符号代数是他在微分方程研究中、以及其年轻朋友兼导师邓肯·法夸尔森·格雷戈里（Duncan Farquharson Gregory，1813–1844）的论文中早已熟悉的主题；格雷戈里曾尝试把几何等其他主题装入符号代数语言。既然符号代数在微分方程中的应用是通过引入微分算子进行的，布尔自然会去寻找适用于亚里士多德逻辑领域的算子。他很快想到使用“选择”算子：例如红色选择算子会从类中选出红色成员。在 1854 年的书中，布尔意识到省略选择算子、直接与类打交道更简单。（不过他保留选择算子，以支持其主张：他的逻辑规律最终并不基于关于语言用法的观察，而深植于人心过程。）本文此后讨论布尔 1847 年的书时，选择算子已替换为更简单的直接类表述。

既然符号代数只是普通代数的句法侧面，布尔就需要为代数中的通常运算与常项找到解释，以建立关于类的逻辑代数。乘法解释为交，从而引出他唯一的新规律——乘法的幂等律 $XX = X$，重新发现了莱布尼茨已表述过的一条逻辑规律。加法定义为并，前提是所处理的是 **不相交** 的类；减法定义为类差，前提是从一个类中减去其子类。其他情形下，加法与减法运算干脆没有定义，或如布尔所写，是 **不可解释的**。通常的算术规律告诉布尔：1 必是全集，$1 - X$ 必是 $X$ 的补。

布尔系统的下一步是把四类直言命题翻译为方程。例如“所有 $X$ 是 $Y$”变为 $X = XY$，“有些 $X$ 是 $Y$”变为 $V = XY$，其中 $V$ 是新符号。为在三段论中消去中项，布尔从普通代数借来一条消去定理，但它对他的逻辑代数太弱；这将在 1854 年的书中得到补救。布尔发现，用上述特称命题（即带存在含义者）的翻译，他不能总推出所需结论，于是添加了变体 $X = VY$、$Y = VX$ 与 $VX = VY$（见词条“布尔”）。

十九世纪的符号代数远不止多项式代数，布尔曾试验哪些结果与工具可能适用于逻辑代数。例如，他用无穷级数展开证明了自己的一个结果。他对普通代数可能性的着迷，使他考虑这样的问题：若把幂等律换成 $X^3 = X$，逻辑会是什么样？他的后继者，尤其杰文斯，很快把类上的运算收窄为我们今天所用的并、交与补。

如前所述，在其 1847 年小书写至四分之三处、结束其系统中传统亚里士多德三段论推导之后，布尔宣布他的逻辑代数能作远为一般的应用。接着他补充了关于展开项、解释方程、以及用长除法把方程中一个类用其他类表示（附加边条件）的一般定理。

布尔的定理在 1854 年得到完成与完善，为分析无限多论证形式提供了算法。这开启了一个崭新而富有成果的视角，背离传统逻辑进路——数百年来，学者们费力编造巧妙口诀，以记住一份极小的有效换位与三段论目录及其相互关系。

德摩根的《形式逻辑》未获显著认可，主要因为它是一大堆细小事实的汇集，缺乏重要综合。布尔《逻辑的数学分析》具有强有力方法，引起德摩根与阿瑟·凯莱（Arthur Cayley，1821–1895）等少数学者的注意；但立刻出现了关于布尔逻辑代数运作方式的严肃问题：它与普通代数究竟有多紧密的联系？布尔如何为自己的逻辑代数程序辩护？事后看来，相当确定的是，布尔并不知道其系统为何有效。他追随格雷戈里，主张要证明使用普通代数是正当的，只需检查乘法的交换律 $XY = YX$ 与分配律 $X(Y + Z) = XY + XZ$；这显然错误。尽管如此，他也可能在足够多情形中检查过自己的结果，从而为“其系统正确”这一信念提供了实质支持。

## 3 1854——布尔对其逻辑代数的最终表述

在第二部书《思维规律》中，布尔不仅把代数方法应用于传统逻辑，还尝试对逻辑作若干改革。他先扩充其 1847 年逻辑代数的规律（未明说先前的三条公理清单不足），并对推理规则（在方程两边施行同一运算）作了评论。但随后他随口说，其系统的基础实际上系于一条（新）原理：只需检查论证在类符号仅取 0 与 1 两个值、运算为通常算术运算时是否正确，便足以判定该论证。我们称此为 **布尔的 0-1 规则**。布尔采纳这一新基础，未给出任何有意义的辩护，未赋特殊名称，书中其余部分对它的少量提及通常也表述笨拙。关于这条 0-1 规则的现代分析，见 Burris & Sankappanavar 2013。

《思维规律》中逻辑代数的发展大体沿 1847 年书的路数进行，翻译方案有微小改动，选择算子被类取代。这里有一条新的、非常重要的定理，即消去定理（修正了他 1847 年所用的那条）。给定类符号 $x, y, z$ 等的一个方程 $F(x,y, z, \ldots) = 0$，消去其中某些类符号后所得最一般的结论，可如此获得：（1）以一切可能方式把 0 与 1 代入 $F(x, y, z, \ldots)$ 中待消去的符号；（2）把这些不同的代入实例相乘，并令乘积等于 0。于是，从 $F(x, y, z) = 0$ 消去 $y$ 与 $z$，得到 $F(x, 0, 0)F(x, 0, 1)F(x, 1, 0)F(x, 1, 1) = 0$。这条定理在布尔对亚里士多德三段论的阐释中也起了重要作用。

从逻辑代数的观点看，1854 年的处理有时不如 1847 年书优雅，但它对布尔如何思考其逻辑代数的基础提供了更丰富的洞见。论逻辑的最后一章（第十五章）试图对亚里士多德换位与三段论给出统一证明。（奇怪的是，第十五章之前布尔未给出任何涉及特称命题的论证实例。）第十五章的细节相当繁复，主要因为应用消去定理与展开定理时表达式规模增大。布尔把大部分工作直接留给读者。后来的评论者往往略过此章，似乎无人逐条推演其细节。

除 0-1 规则与消去定理外，1854 年的表述主要因布尔为其逻辑代数所作的辩护而有趣。他论证：在符号代数中，以部分运算作等式推演完全可以接受，正如运算为全时那样，只要前提与结论中的项可解释。他说普通代数处理不可解释的 $\sqrt{-1}$（−1 的平方根）时就是这样。（复数的几何解释早由韦塞尔、阿尔冈与高斯认识，但直到 1830 年代高斯与哈密顿的出版物，较大数学共同体对复数可接受性的疑虑才被克服。奇怪的是，1854 年布尔仍把 $\sqrt{-1}$ 视为不可解释。）

关于布尔的逻辑代数进路，有若干顾虑：

1. 他的逻辑代数与数的代数之间有无实质联系，抑或二者如此相似纯属偶然？
2. 在聚焦方程的代数逻辑中，能否处理特称命题？
3. 在等式推演中使用不可解释的项，真的可以接受吗？
4. 布尔使用的是“亚里士多德式”语义（传统逻辑所预设的语义，其中词项外延非空）吗？

## 4 杰文斯：基于全运算的逻辑代数

曾师从德摩根的杰文斯，是第一个对布尔系统提出替代方案的人。1863 年他写信给布尔，说布尔的加法运算当然应换成更自然的“相容或”（或“并”），从而引出规律 $X + X = X$。布尔完全拒绝这一建议（它会摧毁其基于普通代数的系统），并中断了通信。杰文斯在 1864 年的《纯粹逻辑》中发表其系统（重印于 Jevons 1890）[^jevons-1890]。所谓“纯粹”，指他不依赖数的代数：把类换成谓词，前者关涉量，后者关涉质；其规律直接由相容析取与合取这些（全）基本运算导出。但他保留布尔以方程作为其逻辑代数中陈述的基本形式。

由于采用德摩根以大写/小写字母表示补的约定，杰文斯的系统不适合为现代布尔代数提供等式公理。不过他不断改进公理系统与推理规则，最终实质上得到了关于 **基项**（即把类符号视为常项而非变元的项）的现代布尔代数系统。

必须注意，现代等式逻辑处理的是 **全称量化** 的方程（十九世纪会称之为 **规律**）。在十九世纪的逻辑代数中，可以把“所有 $X$ 是 $Y$”翻译为方程 $X = XY$。这 **不** 应视为全称量化表达式 $(\forall X)(\forall Y)(X = XY)$。$X$ 与 $Y$ 应作为常项（或图式字母）处理。只含常项（无变元）的项称为 **基** 项。

通过在谓词代数（等价地，类代数）这一特殊框架中作此分析，杰文斯在现代等式逻辑的发展中起了重要作用。如前所述，布尔为其系统给出的等式公理集不充分，最初从格雷戈里的两条规律加上自己的幂等律开始；伴随的还有德摩根的推理规则：可以在等式两边施行同一运算（布尔逻辑代数中的基本运算是加、减、乘）而得到等式。布尔后来转向简单而有力（却未加解释）的 0-1 规则。

用全运算取代布尔的基本运算后，杰文斯在此后许多年间持续完善其系统的公理与规则。我们今天视为理所当然的一些等式逻辑要素，杰文斯花了相当多年才解决：

**自反律**（$A=A$）。1864 年杰文斯把它列为一公设（1890, p. 11），随后在 §24 中称 $A = A$ 为“无用的同一命题”。在其 1869 年论代换的论文中，它成为“同一律”。在《科学原理》（1874）中，它是三条“思维基本规律”之一。

**对称律**（由 $A = B$ 得 $B = A$）。1864 年杰文斯写道：“$A = B$ 与 $B = A$ 是同一陈述。”这是他此后坚持的立场。1874 年他写道：

> 我将认为 $A = B$ 与 $B = A$ 两个形式表达的是以不同方式写出的同一同一性。

至于其逻辑代数的最终形式，我们转向他在《科学原理》（1874）中散布于 40 页的诸规律；此时他已把先前所用的 + 换成 $\ORjev$，显然是为进一步远离与数的代数的任何相似外表：

组合规律

$$ \begin{align} A &= AA = AAA = \& c & \mbox{Law of Simplicity (p. 33)}\\ AB &= BA & \mbox{A Law of Commutativeness (p. 35)}\\ A \ORjev A & = A &\mbox{Law of Unity (p. 72)}\\ A \ORjev B &= B \ORjev A &\mbox{A Law of Commutativeness (p. 72)}\\ A(B \ORjev C) &= AB \ORjev AC & \mbox{(no name given) (p. 76)}\\ \end{align} $$

思维规律

$$ \begin{align} A &= A & \mbox{Law of Identity (p. 74)}\\ Aa &= o & \mbox{Law of Contradiction (p. 74)}\\ A &= AB \ORjev Ab & \mbox{Law of Duality (p. 74)}\\ \end{align} $$

至于其唯一的推理规则，杰文斯选择了代换原则——用现代术语说，这实质上是基项替换与传递性的组合。他表明如何由此导出相等的传递性；他本也可导出对称性，却未这样做。结合律缺失——它隐含于其表达式不加括号的做法之中。

直到《演绎逻辑研究》（1880），杰文斯才提到麦科尔（McColl）用重音符号表示否定。他指出麦科尔的记号可用于对复杂括起的项取否定，随后说，大体上他觉得德摩根的记号——他一贯使用的记号——更为优雅。

## 5 皮尔士：以包摄为逻辑代数的基础

皮尔士于 1860 年代末开始研究逻辑代数。在《论布尔逻辑演算的一项改进》（Peirce 1867）[^peirce-1867]中，他独立得出杰文斯早先已得的结论：须以全运算“并”取代布尔的加法部分运算（见 CP 3.3.6）。在重要的 1880 年论文《论逻辑代数》中，皮尔士悄然告别传统外延语义，引入现代语义的一个通常假定：概念的外延（理解为类）可以为空（也可以为全集）。他并陈述了我们今天所用的直言命题真值条件。例如他说，若 $A$ 与 $B$ 都是空类，则命题“所有 $A$ 是 $B$”为真。限制换位——即从“所有 $A$ 是 $B$”推出“有些 $B$ 是 $A$”——不再是有效推理。皮尔士对其背离传统存在语义的理由与功过未置一词。

皮尔士还告别布尔与杰文斯以相等为基本初始词的做法，改用可有不同解释的“包摄”关系（子类关系、蕴涵等）。他陈述包摄关系的偏序性质，进而把 + 与 × 定义为最小上界与最大下界——他隐含假定这类界存在——并列出如今称为格的、带两个二元运算的代数之关键等式性质。随后他宣称分配律可由之推出，但说证明过于冗长而省略。这一视角的丰饶在其 1885 年的开创性论文中显而易见。在那里，皮尔士基于蕴涵（以符号“$-\kern-.4em<$”表示）的五条公理引入命题逻辑系统，其中包括如今所谓的皮尔士律。这确实使逻辑代数更为优雅。

## 6 德摩根与皮尔士：逻辑代数中的关系与量词

德摩根在 1846 至 1863 年间写了六篇题为《论三段论》的论文（重印于 De Morgan 1966）[^de-1966]。在推广三段论的努力中，他在系列第二篇（1850）里用一般二元关系取代系词“是”。通过允许三段论两个前提使用不同二元关系，他进而引入两个二元关系的复合来表达三段论结论。在这一追求推广三段论的过程中，他引入了二元关系上的其他各种运算，包括逆运算，并为这些运算发展了一部分演算。其主题的主要论文是系列第四篇《论三段论，第 IV 篇，兼论关系逻辑》，1859 年发表（见 De Morgan 1966）[^de-1966]。

继德摩根之后，皮尔士在 1870 年论文《关系逻辑记号描述：由布尔逻辑演算概念之扩充而来》中，把布尔的工作提升到二元关系框架。在二元关系上，除并、交、补之外，还有复合与逆这些自然运算。二元关系被刻画为有序对的集合（见 3.328）。他在 1870 至 1883 年间研究这一新演算。与德摩根一样，皮尔士也考虑了关系上的若干其他自然运算。其主题的主要论文是《论逻辑代数》（1880）。通过使用以 Σ 表示的无限制并、以 Π 表示的无限制交，皮尔士由此把量词引入其逻辑代数。

在 1882 年《关系代数简述》（重印于 De Morgan 1966）中，他用这些量词，借某类系数上的运算来定义关系上的运算。引入关系概念之功归于德摩根，但皮尔士被视为关系理论的真正创立者（例如见 Tarski 1941: 73）[^tarski-1941]。然而，皮尔士并未发展这一理论。正如卡利克斯托·巴德萨所写，“关系演算从来不合皮尔士的口味”（Badesa 2004: 32）[^badesa-2004]。他认为它因类运算与关系运算结合而过于复杂。相反，自 1885 年起，他宁愿发展一种包含量词、却不含关系运算的“一般代数”。由此，他得到了如今所谓一阶逻辑的一种初等而通俗的表述（见 Badesa 2004, *loc. cit.*）[^badesa-2004]。

## 7 施罗德对逻辑代数的系统化

德国数学家恩斯特·施罗德在逻辑代数传统中起了关键作用。一个很好的例子是他要求皮尔士给出分配律的证明——分配律是带两个二元运算的代数的关键等式性质之一。皮尔士（1885）承认自己无法给出证明。多年后，亨廷顿（Huntington，1904: 300–301）描述了他 1903 年 12 月收到的一封皮尔士来信的部分内容，该信声称提供了缺失的证明——显然，皮尔士在施罗德 1902 年去世后偶然翻到了久已遗失的纸页。皮尔士向亨廷顿解释说，他原先假定施罗德的质疑有充分根据。至于他论文的这一表面缺陷，他写道，它“应被加入那份因流感而犯、充斥该文的错误清单……”实际上，皮尔士的证明并未纠正错误，因为分配律在一般格中并不成立；相反，他的证明引入了补运算——他用了公理

> 若 $a$ 不含于 $b$ 的补，则 $a$ 与 $b$ 有共同下界。

在其先前代数工作的基础上，施罗德于十九世纪末写成百科全书式的三卷本《逻辑代数讲义》（1890–1905），以包摄框架与皮尔士所呈现的现代类语义为基础。这部著作是他代数研究的成果，显示出不同影响。施罗德旨在建立一种可应用于许多数学领域的一般代数理论，其中逻辑代数居于核心。正如杰拉尔丁·布雷迪所指出的，它首次阐述了抽象格论，首次在戴德金之后阐述其链论，最全面地发展了关系演算，并基于关系演算处理数学基础（见 Brady 2000: 143 以下）[^brady-2000]

第一卷讨论类的等式逻辑，主要结果是布尔 1854 年的消去定理。针对皮尔士分配律主张的三个相当复杂的反例出现在第一卷附录中，其中一个涉及拟群的 990 个恒等式。戴德金（1897）在该卷基础上，对格（他称之为 **对偶群**）作了优雅的现代抽象表述；在此文中，他给出皮尔士分配律主张的一个五元反例。

第二卷扩充第一卷所发展的类逻辑代数，使其能处理存在陈述。首先，施罗德用现代语义证明：不能用方程表达“有些 $X$ 是 $Y$”。但他指出，用否定方程很容易表达，即 $XY \ne 0$。第二卷以方程与否定方程研究类演算，试图覆盖第一卷的同一主题，尤其用了相当篇幅寻找消去定理。处理若干特例后，施罗德把这一主题推荐为重要研究领域——对消去定理的追寻将被称为消去问题。

施罗德主要受皮尔士工作启发，在《逻辑代数讲义》第三卷考察二元关系的逻辑代数。正如塔斯基曾指出的，皮尔士的工作由施罗德以非常彻底而系统的方式延续并扩展。他特别着迷的一项任务是：给定该代数中的方程 $E(x, y, z, \ldots) = 0$，对其他关系符号求出其中一个关系符号（比如 $x$）的一般解。他设法在给定一个特解 $x = x0$ 的情况下，找到一个非凡的项 $S(t, y, z, \ldots)$，具有如下性质：（1）对任意关系 $t$ 的选择，$x = S(t, y, z, \ldots)$ 都给出 $E = 0$ 的解；（2）$E = 0$ 的每个解 $x$ 都可通过选取合适的 $t$ 以此方式获得。皮尔士对施罗德执着于解方程问题不以为然，并指出施罗德的参数解有点骗人：关系逻辑代数的表达力如此之强，以致计算项 $S(t, y, z, \ldots)$ 实质上就是在执行检验 $E(t, y, z, \ldots) = 0$ 的步骤；若答案为是，$S(t, y, z, \ldots)$ 就返回 $t$，否则返回 $x0$。

总之，施罗德构造了现代谓词逻辑的代数版本，也构造了关系理论。他把它应用于不同领域（例如康托的集合论），并把其代数记号视为一种一般或普遍语言（*pasigraphy*，见 Peckhaus 2004 与 Legris 2012）[^legris-2012][^peckhaus-2004]。值得注意的是，勒文海姆 1940 年仍认为它像集合论一样合理。据他看，施罗德解关系方程的想法是斯科伦函数的前身，施罗德启发了勒文海姆对著名定理的表述与证明：每一有无限模型的“算术”语句都有可数模型。施罗德的关系演算是诺伯特·维纳（Norbert Wiener，1894–1964）在哈佛的博士论文基础（Wiener 1913）[^wiener-1913]。据布雷迪，维纳首次对关系演算作了公理化处理，比塔斯基的公理化早二十多年（见 Brady 2000: 165）[^brady-2000]。

## 8 亨廷顿：逻辑代数的公理化研究

十九世纪与二十世纪之交，希尔伯特（David Hilbert，1862–1943）在《几何基础》中把欧几里得几何呈现为一门不依赖图形证明的公理化学科（Hilbert 1899）[^hilbert-1899]。这引发了一股研究数学公理系统的热潮；尤其人们想知道公理是否独立，以及哪些初始词能导出最优雅的系统。爱德华·弗米利耶·亨廷顿（Edward Vermilye Huntington，1874–1952）是最早为逻辑代数考察这一问题的人之一。他给出逻辑代数的三种公理化，表明每一公理集都独立，且三者等价（见 Huntington 1904）[^huntington-1904]。1933 年，他带着三组新公理回到这一主题，其中一组包含如下三个方程（1933: 280）：

$$ \begin{align} a + b &= b + a \\ (a + b) + c &= a + (b + c) \\ (a' + b')' + (a' + b)' &= a. \end{align} $$

此后不久，赫伯特·罗宾斯（Herbert Robbins，1915–2001）猜想第三个方程可被稍简单的

$$ [(a + b)' + (a + b')']' = a. $$

亨廷顿与罗宾斯都无法证明，后来它又经受住许多人的努力，甚至包括塔斯基及其伯克利才俊学派。在温克（Winker）部分结果的基础上，阿贡国家实验室威廉·麦库恩（William McCune）设计的自动定理证明器 EQP 于 1996 年找到罗宾斯猜想的证明。这一成就经 Kolata 2010 而广为人知。

据亨廷顿（1933: 278），“布尔代数”一词由亨利·M. 谢弗（Henry M. Sheffer，1882–1964）引入；谢弗在文中表明，可用单一基本运算——今称谢弗竖——给出布尔代数的五方程公理化（见 Sheffer 1913）[^sheffer-1913]。怀特海与罗素在《数学原理》第二版序言中宣称，谢弗竖是自《数学原理》出版以来逻辑的最大进展。（相比之下，希尔伯特与阿克曼（1928）说谢弗竖只是奇趣。）两人都未意识到，几十年前施罗德已发现谢弗竖的对偶也是这样的运算；施罗德为自己的运算所选符号是一把双刃剑。

1930 年代，加勒特·伯克霍夫（Garrett Birkhoff，1911–1996）确立了等式逻辑的基本结果，即（1）代数的等式类恰是在同态、子代数与直积下封闭的类；（2）等式逻辑基于五条规则：自反、对称、传递、替换与代换。1940 年代，塔斯基加入等式逻辑的发展；该主题自 1950 年代至今进展迅速。

## 9 斯通：逻辑代数的模型

传统逻辑研究类之间的某些简单关系，即 **是……的子类** 与 **与……有非空交**。然而，一旦采用公理化进路，除显然模型之外的可能模型问题便浮现。贝尔特拉米于 1860 年代末引入非欧几何模型。1890 年代，施罗德与戴德金构造格论公理的模型，以表明分配律不能由之推出。但涉及类代数时，施罗德只考虑标准模型，即每一模型都是给定类的全部子类之集。

对布尔代数公理之一般模型的研究直到 1920 年代末才起步，很快在马歇尔·哈维·斯通（Marshall Harvey Stone，1903–1989）的工作中达到很高水平（见其 1936、1937 年论文）。他关心线性算子环的结构，并意识到中心幂等元——即与环中所有其他算子在乘法下交换（即对环中一切 $L$，$EL = LE$）、且在乘法下幂等（$EE = E$）的算子 $E$——起重要作用。中心幂等元以自然方式构成一个布尔代数。

沿此方向，斯通追问任意布尔代数的结构，并通过证明 **每一布尔代数都同构于一个集合布尔代数** 作答。在关于布尔代数的工作中，他注意到同态核与环论所研究的理想之间有某种类比——这使他给这类核取名“理想”。不久后，他发现布尔代数与布尔环之间的翻译；在此翻译下，布尔代数的理想恰对应相应布尔环的理想。他的下一项重大贡献是建立布尔代数与某些拓扑空间（今称布尔空间或斯通空间）之间的对应。这一对应后来被证明是构造奇异布尔代数的宝贵工具。斯通的这些结果至今仍是逻辑代数发展的范式。

受《逻辑代数》第三卷中对关系之一阶陈述的简略处理启发，勒文海姆（1915）表明：若这类陈述能在无限域中满足，则也能在可数域中满足。1920 年，斯科伦（Thoralf Skolem，1887–1963）通过引入斯科伦范式简化了勒文海姆的证明；1928 年，斯科伦又以更简单的想法取代范式，即使用今称斯科伦函数者。他用这些函数把一阶语句转换为全称语句，即转换为所有量词皆为全称（$\forall$）的前束式语句。

## 10 斯科伦：量词消去与可判定性

斯科伦深受施罗德《逻辑代数》影响，从其博士论文开始。后来他特别关心类演算中消去定理的追寻。在其 1919 年论文中，他确立了关于格的一些结果；尤其是，他表明可以判定全称霍恩句（即矩阵为诸原子的析取——原子或否定或肯定，其中至多一个肯定——的全称句）的有效性，所用程序我们今天认作多项式时间算法。该算法基于在由全称霍恩句导出的产生规则下，求一个有限偏格的最小不动点。这一结果等价于格的统一字问题，虽与斯科伦对勒文海姆定理的著名贡献同在一文，却被遗忘，直到 1990 年代初偶然重新发现。（惠特曼（Whitman，1941）对较为有限的格等式判定问题给出另一解法；它作为格的字问题解法而广为人知。）

斯科伦（1920）对施罗德就类演算提出的消去问题给出优雅解法。若对每一 $n = 1, 2, \ldots$ 添加表达“至少有 $n$ 个元素”的谓词，则有一个简单（但常冗长）的程序，可把关于类的一阶公式转换为无量词公式。这尤其表明类演算的一阶理论是可判定的。莫斯托夫斯基（Mostowski，1952）用这一量词消去结果分析单结构直幂与直和的一阶性质；费弗曼与沃（Feferman and Vaught，1959）随后对一般直和与直积作同样处理。

量词消去成为数理逻辑中证明可判定性的主要方法；而希尔伯特与阿克曼（1928）把证明可判定性列为数理逻辑的主要问题——由于丘奇与图灵的著名不可判定性结果，这一目标在后续版本中被放弃。

## 11 塔斯基与代数逻辑的复兴

模型论可视为希尔伯特元数学方法论与逻辑代数传统的产物，具体体现于勒文海姆与斯科伦的结果。但为该学科奠定经典基础的是塔斯基。模型论研究形式语言与其在“实现”（即为语言变元指定论域，并为其初始符号指定解释）中的解释之间的关系。若该解释使语言中某语句陈述了真事情，则该解释是该语句的 **模型**（见词条“模型论”）。模型基本上由代数结构构成；模型论成为一门自主数学学科，其根源不仅在逻辑代数，也在抽象代数（见 Sinaceur 1999）[^sinaceur-1999]。

除模型论外，塔斯基在 1941 年《论关系演算》一文中复兴了关系代数。他先勾勒一种允许对元素与关系两者量化的形式逻辑，然后更细致地研究该系统中只涉及关系变元的无量词公式。在列出施罗德第三卷所呈现的关系代数中显然成立的一组公理后，他证明这些公理可把无量词关系公式归约为方程。于是，其关系演算成为对某一等式理论的研究；他指出，这一等式理论与全部二元关系研究的关系，正如布尔代数的等式理论与集合全部子集研究的关系。这引出与布尔代数中已提出并解决的问题平行的问题，例如：其关系代数公理的每一模型是否同构于某集合上的关系代数？其中一个问题已由阿尔温·科尔塞尔特（Arwin Korselt，1864–1947）回答：二元关系理论中存在一阶语句，它不等价于关系演算里的任何方程——因此，关系演算表达力明确弱于关系的一阶理论。实际上，关系代数的表达力恰等价于只有三个变元的一阶逻辑。然而，若在关系代数（关系演算）中想形式化一个含有配对公理之类内容的集合论，则可把许多变元归约为三个变元，从而可用方程表达该理论的任一阶语句。蒙克（Monk）证明：与类演算不同，二元关系演算没有有限等式基（见 Monk 1964）[^monk-1964]。塔斯基与吉万特（Tarski and Givant，1987）表明，关系代数的等式逻辑表达力极强，足以在其中展开一阶集合论。

此外，柱形代数由塔斯基在 1948–1952 年间与其学生路易丝·钦（Louise Chin）和弗雷德里克·汤普森（Frederick Thompson）合作引入（见 Henkin & Tarski 1961）[^henkin-1961]，以创建一种能捕捉二元关系一阶理论表达力的逻辑代数。柱形代数本质上是配备一元柱形运算 $C_x$ 的布尔代数，这些运算意在捕捉存在量词（$\exists x$）。多元代数是为一阶逻辑建立逻辑代数的另一进路——由哈尔莫斯（1956c）创立。这些系统中的工作焦点，同样是看能在多大程度上平行于斯通 1930 年代关于布尔代数的结果。

## References（引用注释）

**以下文献从原文照录，不作翻译；中国文献译为中文。**

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

### Primary Sources

### Secondary Sources

[^boole-1847]: Boole, G., 1847, *The Mathematical Analysis of Logic, Being an Essay Towards a Calculus of Deductive Reasoning*, Cambridge: Macmillan, Barclay, & Macmillan; reprinted Oxford: Basil Blackwell, 1951.
[^boole-1854]: –––, 1854, *An Investigation of The Laws of Thought on Which are Founded the Mathematical Theories of Logic and Probabilities*, London: Macmillan; reprint by Dover 1958.
[^boole-1997]: –––, 1997. *Selected Manuscripts on Logic and its Philosophy*, Ivor Grattan-Guinness and Gérard Bornet (eds.), Basel, Boston, Berlin, Birkhäuser: Springer.
[^couturat-1905]: Couturat, Louis, 1905, *L’Algèbre de la Logique*, Paris: Gauthier-Villars; 2ⁿᵈ edition, Paris: Blanchard 1980.
[^dedekind-1897]: Dedekind, R., 1897, “Über Zerlegungen von Zahlen durch ihre grössten gemeinsamen Teiler”, reprinted in *Gesammelte mathematische Werke* (1930–1932), 2: 103–147.
[^dedekind-1930]: –––, 1930–1932, *Gesammelte mathematische Werke*, Robert Fricke, Emmy Noether, Öystein Ore (eds.), Braunschweig: Friedr. Vieweg & Sohn.
[^de-1847]: De Morgan, A., 1847, *Formal Logic: or, the Calculus of Inference, Necessary and Probable*, London: Taylor and Walton; reprinted London: The Open Court Company 1926.
[^de-1966]: –––, 1966, *On the Syllogism and Other Logical Writings*, a posthumous collection of De Morgan’s papers on logic, edited by Peter Heath, New Haven: Yale University Press.
[^feferman-1959]: Feferman, S. and R.L. Vaught, 1959, “The first order properties of products of algebraic systems”, *Fundamenta Mathematica*, 47: 57–103.
[^frege-1879]: Frege, F., 1879, *Begriffsschrift: eine der arithmetischen nachgebildete Formelsprache des reinen Denkens*, Halle a. S.: Louis Nebert.
[^frege-1884]: –––, 1884, *Die Grundlagen der Arithmetik:eine logisch-mathematische Untersuchung über den Begriff der Zahl*, Breslau: W. Koebner.
[^frege-1893]: –––, 1893/1903, *Grundgesetze der Arithmetik, begriffsschriftlich abgeleitet*, 2 vols, Jena: Verlag Hermann Pohle.
[^halmos-1956a]: Halmos, P.R., 1956a, “Algebraic logic. I. Monadic Boolean algebras”, *Compositio Mathematica*, 12: 217–249.
[^halmos-1956b]: –––, 1956b, “The basic concepts of algebraic logic”, *American Mathematical Monthly*, 63: 363–387.
[^halmos-1956c]: –––, 1956c, “Algebraic logic. II. Homogeneous locally finite polyadic Boolean algebras of infinite degree”, *Fundamenta Mathematica*, 43: 255–325.
[^halmos-1956d]: –––, 1956d, “Algebraic logic. III. Predicates, terms, and operations in polyadic algebras”, *Transactions of the American Mathematical Society*, 83: 430–470.
[^halmos-1957]: –––, 1957, “Algebraic logic. IV. Equality in polyadic algebras”, *Transactions of the American Mathematical Society*, 86: 1–27.
[^halmos-1962]: –––, 1962, *Algebraic logic*, New York: Chelsea Publishing Co.
[^henkin-1974]: Henkin, L. and J.D. Monk, 1974, “Cylindric algebras and related structures”, in L. Henkin et al. (eds.), *Proceedings of the Tarski Symposium*, Proceedings of Symposia in Pure Mathematics, vol. XXV, Providence, RI: American Mathematical Society, pp. 105–121.
[^henkin-1961]: Henkin, L. and A. Tarski, 1961, “Cylindric algebras”, in *Lattice Theory, Proceedings of Symposia in Pure Mathematics 2*, R. P. Dilworth (ed.), Providence, RI: American Mathematical Society, pp. 83–113.
[^hilbert-1899]: Hilbert, D., 1899, *The Foundations of Geometry*; reprinted Chicago: Open Court 1980, 2ⁿᵈ edition.
[^hilbert-1928]: Hilbert, D. and W. Ackermann, 1928, *Grundzüge der theoretischen Logik*, Berlin: Springer.
[^huntington-1904]: Huntington, E.V., 1904, “Sets of independent postulates for the algebra of logic”, *Transactions of the American Mathematical Society*, 5: 288–309.
[^huntington-1933]: –––, 1933, “New sets of independent postulates for the algebra of logic, with special reference to Whitehead and Russell’s Principia Mathematica”, *Transactions of the American Mathematical Society*, 35(1): 274–304.
[^jevons-1869]: Jevons, W.S., 1869, *The Substitution of Similars, the True Principle of Reasoning, Derived from a Modification of Aristotle’s Dictum*, London: Macmillan and Co.
[^jevons-1870]: –––, 1870, *Elementary Lessons in Logic, Deductive and Inductive*, London: Macmillan & Co.; reprinted 1957.
[^jevons-1874]: –––, 1874, *The Principles of Science, A Treatise on Logic and the Scientific Method*, London and New York: Macmillan and Co.; reprinted 1892.
[^jevons-1880]: –––, 1880, *Studies in Deductive Logic. A Manual for Students*, London and New York: Macmillan and Co.
[^jevons-1883]: –––, 1883, *The Elements of Logic*, New York and Chicago: Sheldon & Co.
[^jevons-1890]: –––, 1890, *Pure Logic and Other Minor Works*, Robert Adamson and Harriet A. Jevons (eds), New York: Lennox Hill Pub. & Dist. Co.; reprinted 1971.
[^jónsson-1951]: Jónsson, B. and A. Tarski, 1951, “Boolean Algebras with Operators. Part I”, *American Journal of Mathematics*, 73(4): 891–939.
[^kolata-1996]: Kolata, G., 1996, “Computer Math Proof Shows Reasoning Power”, *The New York Times*, December 10 (Technology Section, Cybertimes Column). [[Available Online](http://www.nytimes.com/library/cyber/week/1210math.html)]
[^löwenheim-1915]: Löwenheim, L., 1915, “Über möglichkeiten im Relativkalül”, *Mathematische Annalen*, 76(4): 447–470.
[^löwenheim-1940]: –––, 1940, “Einkleidung der Mathematik in Schröderschen Relativkalkul”, *Journal of Symbolic Logic*, 5: 1–17.
[^macfarlane-1879]: Macfarlane, A., 1879, *Principles of the Algebra of Logic. With Examples*, Edinburgh: David Douglas.
[^monk-1964]: Monk, J. D., 1964, “On Representable Relation Algebras”, *The Michigan Mathematical Journal*, 11: 207–210.
[^mostowski-1952]: Mostowski, A., 1952, “On direct products of theories”, *Journal of Symbolic Logic*, 17: 1–31.
[^peirce-1867]: Peirce, C.S., 1867, “On an Improvement in Boole’s Calculus of Logic”, *Proceedings of the American Academy of Arts and Sciences*, 7: 250–261; reprinted in Peirce 1933 [CP], vol. III, pp. 1–19.
[^peirce-1870]: Peirce, C.S., 1870, “Description of a notation for the logic of relatives, resulting from an amplification of the conceptions of Boole’s calculus of logic”, *Memoirs of the American Academy*, 9: 317–378; reprinted in *Collected Papers* 1933: Volume III, 27–98.
[^peirce-1880]: –––, 1880, “On the algebra of logic. Chapter I: Syllogistic. Chapter II: The logic of non-relative terms. Chapter III: The logic of relatives”, *American Journal of Mathematics*, 3: 15–57; reprinted in *Collected Papers* 1933: Volume III, 104–157.
[^peirce-1885]: –––, 1885, “On the Algebra of Logic: A Contribution to the Philosophy of Notation”, *American Journal of Mathematics* 7(2): 180–202; reprinted in *Collected Papers* 1933: Volume III, 359–403.
[^peirce-1933]: –––, 1933 [CP], *Collected Papers*, Charles Hartshorne and Paul Weiss (eds.), Cambridge: Harvard University Press.
[^schröder-1890]: Schröder, E., 1890–1910, *Algebra der Logik, Vols. I–III*; reprint Chelsea 1966.
[^sheffer-1913]: Sheffer, H.M., 1913, “A set of five independent postulates for Boolean algebras, with application to logical constants”, *Transactions of the American Mathematical Society*, 14(4): 481–488.
[^skolem-1919]: Skolem, T., 1919, “Untersuchungen über die Axiome des Klassenkalküls und Über Produktations- und Summationsprobleme, welche gewisse Klassen von Aussagen betreffen”, *Videnskapsselskapets skrifter, I. Matematisk-naturvidenskabelig*, klasse 3; reprinted in Skolem 1970: 66–101.
[^skolem-1920]: –––, 1920, “Logisch-kombinatorische Untersuchungen über die Erfülbarkeit oder Beweisbarkeit mathematischer Sätze nebst einem Theoreme über dichte Menge”, *Videnskapsselskapets skrifter, I. Matematisk-naturvidenskabelig*, klasse 6: 1–36.
[^skolem-1922]: –––, 1922, “Einige Bemerkungen zur axiomatischen Begrundung der Mengenlehre”, *Matematikerkongressen i Helsingfors den 4–7 Juli 1922, Den femte skandinaviska matematikerkongressen, Redogörelse*, Helsinki: Akademiska Bokhandeln; reprinted in Skolem 1970: 189–206.
[^skolem-1928]: –––, 1928, “Über die mathematische Logik”, *Norsk Mathematisk Tidsskrift*, 10: 125–142; in van Heijenoort 1967: 508–524.
[^skolem-1970]: –––, 1970, *Selected Works in Logic*, Oslo: Universitetsforlaget.
[^stone-1936]: Stone, M.H., 1936, “The theory of representations for Boolean algebras”, *Transactions of the American Mathematical Society*, 40(1): 37–111.
[^stone-1937]: –––, 1937, “Applications of the theory of Boolean rings to general topology”, *Transactions of the American Mathematical Society*, 41(3): 375–481.
[^tarski-1941]: Tarski, A., 1941, “On the calculus of relations”, *The Journal of Symbolic Logic*, 6(3): 73–89
[^tarski-1987]: Tarski, A. and S. Givant, 1987, *Set Theory Without Variables*, (Series: Colloquium Publications, Volume 1), Providence: American Mathematical Society.
[^whitehead-1910]: Whitehead, A.N., and B. Russell, 1910–1913, *Principia Mathematica I–III*, Cambridge: Cambridge University Press.
[^whitman-1941]: Whitman, P.M., 1941, “Free lattices”, *Annals of Mathematics*, second series, 42(1): 325–330.
[^wiener-1913]: Wiener, N., 1913, *A Comparison between the treatment of the algebra of relatives by Schroeder and that by Whitehead and Russell*, Ph.D. thesis, Harvard University (Norbert Wiener Papers. MC 22. Institute Archives and Special Collections, MIT Libraries, Cambridge, Massachusetts).
[^badesa-2004]: Badesa, Calixto, 2004, *The Birth of Model Theory. Löwenheim Theorem in the Frame of the Theory of Relations*, Princeton & Oxford: Princeton University Press.
[^brady-2000]: Brady, Geraldine, 2000, *From Peirce to Skolem*, Amsterdam et al.: North-Holland.
[^burris-2013]: Burris. Stanley & H.P. Sankappanavar, 2013, “The Horn Theory of Boole’s Partial Algebras”, *The Bulletin of Symbolic Logic*, 19(1): 97–105.
[^esquisabel-2012]: Esquisabel, Oscar M., 2012, “Representing and Abstracting. An Analysis of Leibniz’s Concept of Symbolic Knowledge”, in Abel Lassalle Casanave (ed.), *Symbolic Knowledge from Leibniz to Husserl*, London: College Publications, pp. 1–49.
[^gabbay-2004]: Gabbay, Dov. M. & John Woods (eds.), 2004, *Handbook of the History of Logic. Volume 3, The Rise of Modern Logic: From Leibniz to Frege*, Amsterdam et al.: Elsevier North Holland.
[^grattan-guinness-1991]: Grattan-Guinness, Ivor, 1991, “The Correspondence between George Boole and Stanley Jevons, 1863–1864”, *History and Philosophy of Logic*, 12(1): 15–35
[^grattan-guinness-2000]: –––, 2000, *The Search for Mathematical Roots,1870–1940. Logic, Set Theories and the Foundations of Mathematics from Cantor trough Russell to Gödel*, Princeton & Oxford: Princeton University Press.
[^hailperin-2004]: Hailperin, Theodore, 2004, “Algebraical Logic 1685–1900”, in Gabbay & Woods 2004: 323–388.
[^haaparanta-2009]: Haaparanta, Leila (ed.), 2009, *The Development of Modern Logic*, New York and Oxford: Oxford University Press.
[^heinemann-2015]: Heinemann, Anna-Sophie, 2015, *Quantifikation des Prädikats und numerisch definiter Syllogismus*, Münster: Mentis 2015.
[^legris-2012]: Legris, Javier, 2012, “Universale Sprache und Grundlagen der Mathematik bei Ernst Schröder”, in G. von Löffladt (ed.), *Mathematik – Logik – Philosophie. Ideen und ihre historischen Wechselwirkungen*, Frankfurt a. M.: Harri Deutsch, pp. 255–269.
[^mancosu-2009]: Mancosu, Paolo, Richard Zach, and Calixto Badesa, 2009, “The Development of Mathematical Logic from Russell to Tarski: 1900–1935”, in Haaparanta 2009: 318–471
[^peckhaus-1997]: Peckhaus, Volker, 1997, *Logik, Mathesis universalis und allgemeine Wissenschaft*, Berlin: Akademie Verlag.
[^peckhaus-2004]: –––, 2004, “Schröder’s Logic”, in Gabbay & Woods 2004: pp. 557–609.
[^peckhaus-2009]: –––, 2009, “The Mathematical Origins of Nineteenth-Century Algebra of Logic”, in Haaparanta 2009: 159–195.
[^sánchez-2004]: Sánchez Valencia, Victor, 2004, “The Algebra of Logic”, in Gabbay & Woods 2004: pp. 389–544.
[^sinaceur-1999]: Sinaceur, Hourya, 1999, *Corps et Modèles. Essai sur l’histoire de l’algèbre réelle*, 2ⁿᵈ ed., Paris: Vrin.
[^styazhkin-1969]: Styazhkin, N. I., 1969, *History of Mathematical Logic from Leibniz to Peano*, Cambridge, MA: MIT Press.
[^van-1967]: Van Heijenoort, Jean, 1967, “Logic as Calculus and Logic as Language”, *Synthese*, 17: 324–330

## 学术工具

* [如何引用本词条](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=algebra-logic-tradition)。
* [预览本词条的 PDF 版本](https://leibniz.stanford.edu/friends/preview/algebra-logic-tradition/)，见 [SEP 学会之友](https://leibniz.stanford.edu/friends/)。
* 在 [InPhO](https://www.inphoproject.org/entity?sep=algebra-logic-tradition&redirect=True) 查找与本词条相关的话题与思想家。
* 在 [PhilPapers](https://philpapers.org/sep/algebra-logic-tradition/) 查看本词条的增强文献目录及其数据库链接。

## 其他网络资源

[欢迎向作者提出建议。]

## 相关词条

代数 | 乔治·布尔 | 莱布尼茨对 19 世纪逻辑学的影响 | 模型论 | 一阶模型论

**（译注：相关词条的中文站内链接将由管线在对应词条重译完成后统一挂接。）**
