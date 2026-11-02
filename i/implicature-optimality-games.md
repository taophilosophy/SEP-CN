# 优选论和博弈论对含义的研究方法 Optimality-Theoretic and Game-Theoretic Approaches to Implicature and Michael Franke)

*首次发表于 2006 年 12 月 1 日；2026 年 7 月 2 日实质修订。*

语言语用学研究表达式的语境依赖的使用与解释。语用学中或许最重要的概念是格赖斯（Grice）的（1967）会话含义。它的基础是这样一种洞见：借助理性合作行为的一般原则，我们通过一个句子的 **使用** 所传达的内容，可以多于与该句子相联系的 **常规语义意义**。例如，格赖斯论证说，‘or’（或者）的排他性解读——按照这种解读，我们从“约翰或玛丽来了”推出约翰和玛丽并非都来——并不是由‘or’的语义意义造成的，而应当由会话含义理论来说明。在这个具体例子中——一个所谓数量含义（Quantity implicature）的典型例子——听话者的推论被看作源于如下事实：说话者本可以使用一个对照性的、信息上更强的表达式，却选择了不使用。其他含义可能源于听话者认为说话者视为正常事态的东西，即刻板解读。对这两类含义而言，听话者对一个表达式所作的（语用）解释都涉及他认为说话者使用该表达式的原因。但显然，说话者的这个原因也必须涉及关于听话者推理的假设。

本词条讨论会话含义的形式化说明，它明确考虑了说话者与听话者的互动推理（例如双方关于彼此的信念、话语语境的有关方面等），并把会话含义还原性地解释为有目标的、经济最优的语言使用所产生的结果。与传统的含义分析一样，本词条假定句子具有既存的语义意义，并主要关注一般会话含义（generalized conversational implicatures）。

## 1 双向优选论

### 1.1 双向优选论与数量含义

优选论（Optimality Theory，OT）是这样一种语言学理论：它假定语言选择受一组候选对象或备选项之间的竞争所支配。在标准优选论中（Prince & Smolensky, 1993），最优候选是最好地满足一组可违反约束的那个。在音系学中取得成功之后，优选论也被用于句法学、语义学与语用学。优选论式语义学的原始想法是：把候选对象看作听话者能够指派给给定表达式的备选解读，并用约束来描述对表达式—解读配对的总体偏好，从而为解读建模。布吕特纳（Blutner 1998, 2000）扩展了这一原始版本，还把说话者本可以使用却没有使用的备选表达式（或形式）也考虑在内。对话语用学而言，诉诸备选表达式/形式是说明数量含义的标准做法。因此，最优化应当从两个方向来理解：听话者的方向与说话者的方向。根据布吕特纳的双向优选论（Bi-OT），最优的并不仅仅是相对于形式的解读，而是形式—解读配对。就形式—解读配对之间的“优于”关系‘$\gt$’而言，配对 $\langle f,i\rangle$ 被称为是 **（强）最优** 的，当且仅当它满足以下两个条件：

$$\begin{align} \neg \exists i' &: \langle f,i'\rangle \gt \langle f,i\rangle \\ \neg \exists f' &: \langle f', i\rangle \gt \langle f,i\rangle \end{align}$$

第一个条件要求 $i$ 是形式 $f$ 的一个最优解读。在双向优选论中，这个条件被看作是从听话者视角的最优化。布吕特纳提出：$\langle f,i'\rangle \gt \langle f,i\rangle$ 当且仅当 $i'$ 是 $f$ 的一个比 $i$ 更可能或更刻板的解读：$P(i'\mid \llbracket f\rrbracket) \gt P(i\mid \llbracket f \rrbracket)$（其中 $\llbracket f\rrbracket$ 表示 $f$ 的语义意义，$P(B\mid A)$ 是在给定 $A$ 的条件下 $B$ 的条件概率，定义为 $P(A\cap B)/P(A)$）。第二个条件被认为涉及说话者的最优化：对于说话者而言，$\langle f,i\rangle$ 要成为最优的，就必须是她不能用更优的形式 $f'$ 来表达 $i$。$\langle f',i\rangle \gt \langle f,i\rangle$ 当且仅当要么 (i) $P(i\mid \llbracket f'\rrbracket) \gt P(i\mid \llbracket f\rrbracket)$，要么 (ii) $P(i\mid\llbracket f'\rrbracket = P(i\mid\llbracket f\rrbracket)$ 且 $f'$ 是比 $f$ 复杂度更低的表达 $i$ 的形式。

双向优选论说明了经典的数量含义。一个方便（尽管有争议）的例子是数词的“恰好”解读。为举例起见，让我们假定数词在语义上具有“至少”意义。[^note-1] 不过，我们仍想说明这样一种直觉：“三个孩子来参加聚会了”通常被解读为说 **恰好** 三个孩子来参加聚会了。做到这一点的一种方式是假定说话者可以使用的备选表达式都具有形式“（**至少**）$n$ 个孩子来参加聚会了”，而听话者的备选解读则是 $i_n$ 型的，意为“**恰好** $n$ 个孩子来参加聚会了”。[^note-2] 如果我们再次为举例起见假定，所有相关解读都被认为是同样可能的，并且已经普遍假定有些孩子来了、但不多于四个，那么强最优的形式—解读配对可以从下表中读出：

| $P(i\mid \llbracket f\rrbracket)$ | $i_1$ | $i_2$ | $i_3$ | $i_4$ |
| --- | --- | --- | --- | --- |
| ‘one’ | $\Rightarrow$¼ | ¼ | ¼ | ¼ |
| ‘two’ | 0 | $\Rightarrow ⅓$ | $⅓$ | $⅓$ |
| ‘three’ | 0 | 0 | $\Rightarrow$ ½ | ½ |
| ‘four’ | 0 | 0 | 0 | $\Rightarrow 1$ |

在这张表中，条目 $P(i_3 \mid \llbracket$‘two’$\rrbracket) = ⅓$，因为 $P(i_3 \mid \{i_2,i_3,i_4\}) = ⅓$。注意，按照这一推理，‘two’ 被解读为“恰好 2”（如箭头所示），因为：

1. $P(i_2 \mid \llbracket$‘two’$\rrbracket) = ⅓$ 高于任何备选表达式‘$n$’的 $P(i_2 \mid \llbracket$‘$n \textrm{'} \rrbracket)$，并且
2. 所有其他与数词表达式的语义意义相容的解读都 **被阻断**：例如，存在另一个表达式，对它而言 $i_4$ 是更好的解读，即具有更高条件概率的解读。

就数词而言，备选表达式的语义意义产生一个线性序。如果我们继续像迄今所做的那样把解读取得足够具体，那么这一点对双向优选论分析就是决定性的。考虑对问题“谁来参加聚会了？”的下列备选回答：

1. 约翰来参加聚会了。
2. 约翰或比尔来参加聚会了。

假定约翰和比尔是仅有的相关人士，并且预设有人来参加聚会了。在这种情况下，说明双向最优推理的表如下所示（其中 $i_x$ 是只有 $x$ 来了的解读）：

| $P(i\mid \llbracket f\rrbracket)$ | $i_j$ | $i_b$ | $i_{jb}$ |
| --- | --- | --- | --- | --- |
| ‘John’ | $\Rightarrow ½$ | 0 | $½$ |
| ‘Bill’ | 0 | $\Rightarrow ½$ | $½$ |
| ‘John and Bill’ | 0 | 0 | $\Rightarrow 1$ |
| ‘John or Bill’ | $⅓$ | $⅓$ | $⅓$ |

这张表正确地预测出（1）被解读为说 **只有** 约翰来了。但现在考虑析取（2）。直观上，这个回答应当被解读为说：要么只有约翰来了，要么只有比尔来了。然而，容易看出，这一预测只有当“约翰来了”和“比尔来了”不被认为是备选形式时才成立。双向优选论预测：如果“约翰来了”和“比尔来了”也被认为是备选项，那么该析取就是不可解读的，因为具体的解读 $i_j$、$i_b$ 和 $i_{jb}$ 都能由其他形式更好地表达。一般而言，可以看到：如果备选表达式的语义意义不是线性有序、而是仅部分有序的，那么上面概括的数量含义推导就会产生部分错误的预测。

事实证明，双向优选论的这一问题比它表面看来要小。直观上，像（2）这样的回答提示说话者拥有不完全的信息（她不知道约翰或比尔中谁来了）。但我们迄今所考虑的解读是世界状态，并不编码说话者知识的不同程度。所以，要在双向优选论（或在任何其他数量含义分析中）中考虑这一点，我们应当允许代表说话者不同知识状态的备选解读。阿洛尼（Aloni 2007）给出了一种对无知含义（ignorance implicatures）的双向优选论说明——无知含义是像上面这样的推断，即说话者缺乏某些可能相关的信息——以及对 **无差别含义**（*indifference implicatures*）的说明（即说话者认为某些信息不够相关、不值得传达）。此外，可以证明：就无知含义而言，双向优选论的预测与舒尔茨和范罗艾（Schulz & Van Rooij）在各种（合作）论文中称为“*Grice*”的语用解读函数相一致（例如 Schulz & Van Rooij, 2006）。在这些论文中，据称 *Grice* 实现了格赖斯的质量准则与第一条数量准则，并且证明了借助它（连同一条附加的能力假设）我们可以说明许多会话含义，包括（1）和（2）的含义。

### 1.2 对霍恩分工的双向优选论分析

双向优选论也能说明 **霍恩的语用分工**（*Horn’s division of pragmatic labor*），或有时按莱文森（Levinson 2000）的说法被另称为 **M-含义**。据霍恩，由这一语用分工可以推出：虽然（形态上）**无标记** 表达式通常经由格赖斯的关系准则获得无标记的（即刻板的）解读，但 **有标记** 表达式——形态上复杂、词汇化程度较低——往往获得有标记的（即非刻板的）解读。霍恩（Horn 1984）主张，这源于格赖斯两条数量次准则与关系准则、方式准则之间的相互作用，并且对有标记表达式的解读而言，关键的是同时存在一个无标记的备选表达式。为了说明这一点，考虑以下著名例子：

1. 约翰杀了治安官。
2. 约翰导致治安官死亡。

我们通常把无标记的（3）解读为刻板的杀人（故意），而有标记的（4）则提示约翰以更间接的方式、也许是无意地杀了治安官。布吕特纳（Blutner 1998, 2000）表明这可以在双向优选论中得到说明。取 $i_{st}$ 为更可能的解读，即约翰以刻板方式杀了治安官，而 $i_{\neg st}$ 是约翰以不寻常方式导致治安官死亡的解读。由于（3）比（4）复杂度更低，并且 $i_{st}$ 是与（3）的语义意义相容的更刻板的解读，因此可以预测（3）被解读为 $i_{st}$。于是，借助他的 **强** 最优概念（即对说话者和听话者都最优），布吕特纳能说明句子通常获得最可能的、或刻板的解读这一直觉。然而，按照这一最优概念，布吕特纳还不能解释更复杂的形式（4）如何能有解读，尤其不能解释它为何会被解读为非刻板的杀人。原因在于：在假定（4）与（3）具有相同语义意义的条件下，刻板解读不仅对（3）是听话者最优的，对（4）也是。

## 2 含义与博弈论

第一个系统地探索把博弈论用于把交流说明为 **策略性推理** 的是普拉尚特·帕里克（Prashant Parikh），见其 1988 年的学位论文（Parikh 1988）。[^parikh-1988] 帕里克的理论基于他所谓的 **部分信息博弈**（*games of partial information*），围绕博弈论的解概念 **帕累托最优纳什均衡** 展开，并在一系列论文与专著中被精炼并应用于各种现象，包括但不限于含义加强的话语意义（例如 Parikh 1991, 1992, 2000, 2001, 2010, 2019, 2024）。[^parikh-1991] 另一个值得注意的早期贡献是阿舍、谢尔与威廉姆斯（Asher, Sher, and Williams 2001）的工作，他们试图用博弈论思想来合理化格赖斯的会话准则。下面我们聚焦于基于所谓信号博弈中迭代推理的含义研究方法。德克尔与范罗艾（Dekker and van Rooij 2000）以及弗兰克与耶格（Franke and Jäger 2012）探讨了优选论与博弈论之间的关系。史蒂文斯与本茨（Stevens and Benz 2018）给出了博弈论语用学的另一份深刻概述。

### 2.1 信号博弈

戴维·刘易斯（David Lewis 1969）引入信号博弈来解释消息如何能被用来传达某种东西，尽管这些消息没有既存的意义。在语用学中我们想做类似的事情：解释一个表达式实际传达了什么，而该表达式的实际解读由其常规语义意义所欠定。为了在博弈论中说明语用推断，帕里克（Parikh 1991, 1992）引入了部分信息博弈。这些博弈很像刘易斯的原始信号博弈，不同之处在于：消息具有常规语义意义，说话者只说为真的消息。为了提供一份宽广的概述，我们略过了刘易斯信号博弈与帕里克部分信息博弈之间有趣而微妙的差异。

于是，一个信号博弈是发送者 $s$ 与接收者 $r$ 之间的一个非对称信息博弈。发送者观察到 $s$ 与 $r$ 所处的状态 $t$，而接收者必须实施一个行动。发送者 $s$ 可以通过发送一条消息来试图影响 $r$ 所采取的行动。$T$ 是状态集，$F$ 是形式集，即消息集。这些消息已经具有语义意义，由语义解读函数 $\llbracket \cdot \rrbracket$ 给出，该函数把 $T$ 的一个子集指派给每个形式。发送者将在每个状态发送一条消息/形式，因此一个 **发送者策略** $S$ 是从 $T$ 到 $F$ 的一个函数。接收者将在听到一条具有特定语义意义的消息后实施一个行动，但就目前的目的而言，我们可以把行动简单地看作解读。于是一个 **接收者策略** $R$ 是把一条消息映射到一个解读（即 $T$ 的一个子集）的函数。说话者与听话者的一个 **效用函数** 表示交谈者所关心的是什么，因此效用函数为说话者与听话者认为相关的信息建模（实现了格赖斯的相关准则）。为简单起见，通常假定 $s$ 与 $r$ 的效用函数（$U_s$ 与 $U_r$）相同（实现了格赖斯的合作原则），并且它们依赖于 (i) 实际状态 $t$，(ii) 接收者对消息 $f$（由 $s$ 在 $t$ 中按照各自策略 $R$ 与 $S$ 发送）的解读 $i$，即 $i = R(S(t))$，以及 (iii)（在 2.3 节中）发送者所使用的形式 $f = S(t)$。自然被看作按照 $T$ 上的某个（公共已知的）概率分布 $P$ 来选取状态。关于这一概率函数，每个发送者—接收者策略组合 $\langle S,R\rangle$ 对玩家 $e \in \{s,r\}$ 的期望（或平均）效用可以如下确定：

$$ \text{EU}_e (S,R)= \sum_{t\in T} P(t) \times U_e (t,S(t),R(S(t))). $$

一个信号博弈被看作单个话语及其解读的一个（简化的、抽象的）模型，它包含语用推理语境中某些最为相关的特征：信息的不对称性（说话者知道世界状态，听话者不知道）、一个带有相关语义意义的话语备选项概念（在消息/形式集中）、以及一个关于什么算作相关信息的灵活表征（通过效用函数）。如果这还不够——例如如果我们想要听话者也拥有不与说话者共享的部分信息（比如当说话者不确定什么对听话者真正相关时）——那也可以容易地容纳进一个更复杂的博弈模型，但我们在这里不打算深入更复杂的模型。发送者与接收者的策略编码使用和解读语言的特殊方式。期望效用概念评价（在给定语境中）使用和解读语言的方式有多好。对话语现象给出博弈论解释，旨在把那些对应于经验上被证实的、作为博弈问题的最优/理性解行为的发送者—接收者策略对区分出来。

博弈论的标准解概念是 **纳什均衡**。一个信号博弈的纳什均衡是一对策略 $\langle$*S$^*$*,*R$^*$*$\rangle$，它具有如下性质：无论发送者还是接收者都无法通过单方面偏离来增加其期望效用。因此，*S$^*$* 是对 *R$^*$* 的最优反应，且 *R$^*$* 是对 *S$^*$* 的最优反应。博弈论文献中有大量纳什均衡的精炼。此外，还有均衡分析的替代方案，其中最突出的两种是：(i) 对智能体推理过程的显式形式化，如认知博弈论中所做的那样（例如 Perea 2012）[^perea-2012]，以及 (ii) 演化博弈论的变体（例如 Sandholm 2010）[^sandholm-2010]，它们研究在逐渐的最优化过程（如模仿或向父母学习）下智能体行为倾向的动态变化。这些问题也与对语言语用学的应用相关，下面我们将用 M-含义/霍恩的语用分工的例子来演示。

### 2.2 对霍恩分工的博弈论说明

帕里克（Parikh 1988, 1991, 1992）提出用博弈论来说明消歧与含义。事实证明，同样的提议也能用来说明霍恩的语用分工。帕里克假定一条消息（或形式）$f_u$ 在语义上有歧义，可以具有刻板解读 $t_{st}$ 与非刻板解读 $t_{\neg st}$，且 $P(t_{st}) \gt P(t_{\neg st})$。然而，这两种意义也可以由一个更复杂的形式无歧义地表达。例如，解读 $t_{\neg st}$ 不仅可以由 $f_u$ 表达，也可以由字面上表达它的形式 $f_m$ 表达。与所谓昂贵信号博弈中的惯例一样，并且也与帕里克的提议一致，发送者的效用函数可以分解为一个收益函数与一个成本函数：$U_s (t,f,i) = B_s (t,i) - C(f)$，其中 $i$ 是一个解读。我们采用如下收益函数：$B_s (t,i) = 1$ 若 $i = t$，否则 $B_s (t,i) = 0$。有歧义消息 $f_u$ 的成本低于无歧义消息 $f_m$ 的成本。我们可以不失一般性地假定 $C(f_u) = 0 \lt C(f_m)$。在把信号博弈用于分析人类交流时，通常假定：用昂贵的消息获得成功交流，总比用廉价的消息获得失败交流要好，这意味着 $C(f_m)$ 尽管大于 $C(f_u)$，仍必须保持足够小。如果我们把自己限制在一个有 2 个状态（$t_{st}$ 与 $t_{\neg st}$）和 3 条消息（$f_u$ 以及字面上表达这两个状态的两种形式）的博弈中，并像以前那样考虑发送者与接收者策略，那么产生双射映射 $\{\langle t_{st},f_u\rangle , \langle t_{\neg st},f_m\rangle \}$ 的发送者与接收者策略组合就是该博弈的一个纳什均衡。直观上，这也是消歧博弈的正确解，因为有歧义消息 $f_u$ 表达刻板解读 $t_{st}$，而非刻板状态 $t_{\neg st}$ 由有标记的、更昂贵的消息 $f_m$ 表达。遗憾的是，映射 $\{\langle t_{st},f_m\rangle , \langle t_{\neg st},f_u\rangle \}$——其中较廉价的消息表示非刻板情境——也是该博弈的一个纳什均衡，这意味着在当前的实现中，博弈论的标准解概念还不能单独区分出所期望的结果。

这时就轮到均衡精炼和/或替代解概念的考虑了。帕里克（Parikh 1988, 1991, 1992）观察到，在上述两个均衡中，第一个帕累托支配第二个——它是唯一的帕累托纳什均衡——因此应当偏好前者。范罗艾（Van Rooij 2004）建议：由于霍恩的语用分工不仅涉及语言使用，也涉及语言组织，人们应当从演化的观点来看待信号博弈，并利用演化博弈论中那些解释帕累托最优解涌现的变体。作为第三种替代方案，范罗艾（van Rooij 2008）在德亚赫（De Jaegher 2008）一些想法的基础上提出，也可以利用前向归纳（一种推理对手出人意料的行动的特殊博弈论方式）来区分出所期望的均衡。作为利用交谈者认知状态详细建模的方法的一个例子，弗兰克（Franke 2014a）建议，我们应当区分涉及相当清晰的 **特设**（*ad hoc*）推理的 M-含义情形（如（5）与（6））与可能具有更语法化对比的情形（如（3）与（4））。

1. 特纳太太唱了《甜蜜的家》（Home Sweet Home）。
2. 特纳太太发出一系列大致对应于《甜蜜的家》乐谱的声音。

弗兰克建议，用于推理（5）与（6）的博弈模型应当包含一个备选项不对称性的要素：虽然（说话者可以预期）听话者在听到（6）时会认为（5）是一个备选话语，这是合理的，但（说话者相信）听话者在听到（5）时会认为（6）是一个潜在备选话语，这却相当不可信。这种备选项的不对称性转化为听话者在不同消息之后对语境所将具有的不同信念。说话者可以预见到这一点，而一个实际观察到（6）的听话者可以推理他自己的反事实语境表征——如果说话者说了（5）而非（6），他本会具有的那一表征。弗兰克表明，当与语境表征中的这种不对称性配对时，一个简单的迭代最优反应推理模型（我们接下来就转向它）也给出了所期望的结果。

### 2.3 数量含义与迭代推理

与 M-含义的情形不同，许多数量含义依赖于备选表达式在逻辑强度上的差异：从“三”到语用地加强的“恰好三”解读的推断（我们在 1.1 节中勾勒的）依赖于如下事实：备选表达式“四”在语义上更强，即“四”在语义上蕴涵“三”，但在所假定的“至少”语义下并非相反。为了把语义强度的考虑带入博弈论语用学，我们必须赋予常规意义在博弈模型或解概念中某种作用。下面，我们考察两种相似而不同的可能性，它们以关于交谈者理性的（高阶）推理链来阐发语用推理，并在此过程中处理语义意义。

把语义意义带入博弈论语用学的一种直截了当而高效的方式，就是简单地把信号博弈中发送者与接收者的可行策略集限制在符合常规意义的那些策略上：发送者只能选择对实际状态为真的形式，接收者只能选择在观察到的消息的外延之中的解读。这也许显得粗糙，从一开始就排除了非字面语言使用、说谎、欺骗与错误的情形，但它可能有助于合理化合作性的、寻求信息的交谈者之间常见的语用推理模式。基于这种对服从真理的策略的限制，帕万（Pavan 2013）与罗思柴尔德（Rothschild 2013）独立地证明，存在一个既有的非均衡解概念，能很好地合理化数量含义，即 **迭代可采纳性**（*iterated admissibility*），也称 **弱占优策略的迭代消去**。不深入细节，这一解概念的总体想法是：从整个可行策略集（都符合语义意义）出发，然后迭代地消去所有这样的策略 $X$：对于对手剩余策略中对手可能采取的策略，不存在会使 $X$ 成为理性之事的 **谨慎信念**。（谨慎信念是指不排除任何尚未被消去的对手策略的信念。）在重复迭代消去中存活的策略集，随后与（一种特殊的）共同理性信念相容。总之，迭代可采纳性是一种消去式方法：从所有（服从真理的）策略集出发，每一步消去一些策略，直到我们剩下一个稳定的、再也无法消去任何东西的策略集。

限制只关注真实策略的一个替代方案，是用语义意义来约束语用推理的起点。这样做的进路包括 **最优断言进路**（*optimal assertions approach*）（Benz 2006, Benz & van Rooij 2007）[^benz-2006][^benz-2007]、**迭代最优反应模型**（例如 Franke 2009, 2011, Jäger 2014）[^franke-2009][^jäger-2014]，以及相关的 **概率模型**（例如 Frank & Goodman 2012, Goodman & Stuhlmüller 2013, Franke & Jäger 2014）[^frank-2012][^franke-2014][^goodman-2013][^jäger-2014]。统一这些进路的总体想法可以直接追溯到格赖斯，尤其是说话者应当最大化其话语中所含相关信息的量的观念。由于话语所含的信息通常被看作语义信息（而非语用地受限或调制的意义），实现格赖斯式说话者的一种简单方式是假定他们通过考虑字面解释者对每个备选项会作何反应来选择话语。语用听众随后基于说话者在上述意义上是格赖斯式的信念而最优地回应。换言之，这些进路定义一个心理理论（Theory-of-Mind）推理序列：从一个（非理性的、哑的）字面解释者出发，一个格赖斯式说话者基于字面解读（近似）理性地行动，而一个格赖斯式听众基于格赖斯式说话者的行为（近似）理性地解读。有些贡献允许最优反应的进一步迭代，另一些则不允许；有些贡献也考察以字面发送者开始的推理序列；有些贡献假定智能体严格理性，另一些则允许对经典理性选择的概率近似（概述与比较见 Franke & Jäger 2014）。[^franke-2014][^jäger-2014]

迭代最优反应进路与先前提到的基于迭代可采纳性的进路之间的一个关键区别是：前者并不收缩策略集，而是允许在每一步有不同的最优反应集。这也使得（某些）迭代最优反应进路能够处理交谈者偏好不一致的语用推理情形，即格赖斯的合作性假定不成立的情形，或者存在偏离语义意义的额外激励的情形（关于非合作语境中推理的博弈模型，参见例如 Franke, de Jager & van Rooij 2012, de Jaegher & van Rooij 2014, Franke & van Rooij 2015）。[^franke-2015] 迭代最优反应模型与迭代可采纳性之间的另一个区别是：后者本身并不说明霍恩的语用分工（讨论见 Franke 2014b 与 Pavan 2014）。[^franke-2014b][^franke-2014][^pavan-2014]

为了说明迭代最优反应推理在一个简单（合作）情形中如何运作，让我们再简要地看看数词表达式。取一个有 4 个状态（或世界）$W = \{w_1, w_2, w_3, w_4\}$ 的信号博弈，其中下标给出参加我们聚会的孩子的恰好/最大数目，以及 4 条消息 $F = \{$‘one’,‘two’,‘three’, ‘four’$\}$，作为“$n$ 个孩子来参加我们的聚会”的简写。在新格赖斯式的“至少”解读下，数词的意义构成一个蕴涵链：

$$ \llbracket `\text{four}\rsquo \rrbracket \subset \llbracket `\text{three}\rsquo \rrbracket \subset \llbracket `\text{two}\rsquo \rrbracket \subset \llbracket `\text{one}\rsquo \rrbracket, $$

因为例如 $\llbracket$‘three’$\rrbracket = \{w_3, w_4\}$。一个字面解释者（否则对语境因素一无所知）会对每条消息作出回应，等概率地选择任何真的解读。所以，例如，如果字面解释者听到“three”，他会选择 $w_3$ 或 $w_4$，各以概率 $½$。但这意味着，对于一个想传达实际世界是 $w_3$ 的说话者而言，表达式的最优选择会是“three”，因为这使字面解释者选择 $w_3$ 的机会最大化。具体地说，如果说话者选择“one”，字面听众选择 $w_3$ 的机会是 ¼；对“two”是 ⅓；对“three”是 $½$；对“four”则是零，因为 $w_3$ 不是 $\llbracket$‘three’$\rrbracket$ 的元素。所以，一个理性的格赖斯式说话者在 $w_3$ 中选择 $\llbracket$‘three’$\rrbracket$，而其他任何状态都不选——对所有其他状态用平行论证容易看出。但这意味着，一个听到“three”的格赖斯式解释者将推断出实际世界必定是 $w_3$。

这一语用推理方案的不同扩展在后续工作中被提出。一种是包含概率选择函数来为智能体的近似理性选择建模，从而允许与实验数据有更直接的联系（概述见 Franke & Jäger 2016, Goodman & Frank 2016）。[^franke-2016][^goodman-2016] 这类概率语用模型已被应用于许多感兴趣的现象，包括对语境中指称表达式的推理（Frank & Goodman 2012）[^frank-2012]、无知含义（Goodman & Stuhlmüller 2013）[^goodman-2013]、标量含义上的语境效应（Degen et al. 2015）[^degen-2015]、数词的非字面解读（Kao et al. 2014）[^kao-2014]、与特定语调相关的语用意义调制（Bergen & Goodman 2015, Stevens 2016）[^bergen-2015][^stevens-2016]，以及复杂句中的数量含义（Bergen et al. 2016, Potts et al. 2016）。[^bergen-2016][^potts-2016] 这些语用推理模型还被成功用于自然语言处理应用（Andreas & Klein 2016, Monroe et al. 2017）[^andreas-2016][^monroe-2017] 以及语言学研究的其他领域，如社会语言学（Burnett 2019）。[^burnett-2019] 另一个近来的进路是允许所涉及表达式的语义意义具有不确定性，并允许交谈者的信念与偏好以及“共同基础”（common ground）其他方面具有不确定性（例如 Brochhagen 2017）。[^brochhagen-2017] 最后，在近来的工作中，被说明的语用现象已不仅限于一般会话含义，还包括特殊会话含义（particular conversational implicature）、显义（explicatures）或自由充实（free enrichment）（例如 Parikh 2010）[^parikh-2010]、预设分析（Qing et al. 2016）[^qing-2016]，以及礼貌（例如 Clark 2012, Yoon et al. 2020）。[^clark-2012][^yoon-2020]

## 3 结论

双向优选论与博弈论是相当自然且相似的形式化框架，用于形式化格赖斯关于语境中互动性、目标导向的语用推理的观念。近来的发展转向认知博弈论或演化博弈论，或转向用于经验数据的概率模型。最后，我们指出，与这里所探索的类似的形式技术适用于不同领域中更广泛的问题，例如哲学（如 Parikh 2019）[^parikh-2019]、语言演化（如 Ahern and Clark 2014; Brochhagen, Franke, and Rooij 2018; Carcassi 2020）[^ahern-2014][^carcassi-2020]，以及计算语言学（如 Vogel et al. 2014, Cohn-Gordon, Goodman, and Potts 2019）。[^vogel-2014]

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## 学术工具

> |   | [如何引用本词条](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=implicature-optimality-games)。 |
> | --- | --- |
> |   | [预览本词条的 PDF 版本](https://leibniz.stanford.edu/friends/preview/implicature-optimality-games/)（[SEP 之友协会](https://leibniz.stanford.edu/friends/)）。 |
> |   | [查找与本词条相关的话题与思想家](https://www.inphoproject.org/entity?sep=implicature-optimality-games&redirect=True)（互联网哲学本体论项目，InPhO）。 |
> |   | [本词条的增强文献目录](https://philpapers.org/sep/implicature-optimality-games/)（[PhilPapers](https://philpapers.org/)），含其数据库链接。 |

## 其他网络资源

- [概率语言理解：理性言语行为框架导论](http://www.problang.org/)，由格雷戈里·斯孔特拉斯（Gregory Scontras）、迈克尔·亨利·泰斯勒（Michael Henry Tessler）与迈克尔·弗兰克（Michael Franke）所著的互动式网络读本，介绍概率语用推理模型。

## 相关词条

语义和语用中的默认 | 博弈论 | 保罗·格莱斯 | 含义 | 逻辑与游戏 | 语用学

## Notes（原文脚注）

## Notes to Optimality-Theoretic and Game-Theoretic Approaches to Implicature

[^note-1]: 这一假定是有争议的。那些不接受这一假定的人应当想想其他例子，其中备选表达式的语义意义就推论而言构成一个线性链。标度 $\langle \text{and, or} \rangle$ 同样可以，就像 $\langle \text{all, most, some} \rangle$ 一样，前提是量词‘all’与‘most’产生一种存在性预设。

[^note-2]: 备选表达式的选择对任何数量含义分析都是决定性的。加兹达（Gazdar 1979）等人假定，备选项与某些词项是 **约定地**（conventionally）相联系的。然而，假定这一选择（也）取决于所提出的问题，和/或取决于对话中什么是相关的，似乎更自然（参见例如 van Rooij, 2004）。

[^note-3]: 这一定义不如布吕特纳的实际定义普遍，但对眼下这个例子而言结果相同。

[^ahern-2014]: Ahern, C. and R. Clark, 2014, ‘Diachronic Processes in Language as Signaling Under Conflicting Interests’, *The Evolution of Language: Proceedings of EVOLANG10*, E. A. Cartmill et al. (eds.), Singapore: World Scientific Press, 25–32.

[^andreas-2016]: Andreas, J. and D. Klein, 2016, ‘Reasoning about Pragmatics with Neural Listeners and Speakers’, *Proceedings of the 2016 Conference on Empirical Methods in Natural Language Processing*, pp. 1173–1182.

[^aloni-2007]: Aloni, M., 2007, ‘Expressing Ignorance or Indifference. Modal Implicatures in Bi-Directional Optimality Theory’, in B. ten Cate and Henk Zeevat (eds.), *Logic, Language and Computation: Papers from the 6th International Tbilisi Symposium*, Berlin, Heidelberg: Springer, 1–20.

[^asher-2001]: Asher, N., I. Sher, and M. Williams, 2001, ‘Game Theoretical Foundations for Gricean Constraints’, in *Proceedings of the 13th Amsterdam Colloquium*, R. van Rooy and M. Stokhof (eds.), Amsterdam: Institute for Logic, Language, and Cognition, 31–37.

[^benz-2006]: Benz, A., 2006, ‘Utility and Relevance of Answers’, in A. Benz, G. Jäger and R. van Rooij (eds.), *Game Theory and Pragmatics*, New York: Palgrave McMillan, 195–214.

[^benz-2007]: Benz, A. and R. van Rooij, 2007, ‘Optimal Assertions, and What They Implicate. A Uniform Game Theoretic Approach’, *Topoi*, 26: 63–78.

[^bergen-2016]: Bergen, L., R. Levy and N. D. Goodman, 2016, ‘Pragmatic Reasoning through Semantic Inference’, *Semantics and Pragmatics*, 9: 1–83.

[^bergen-2015]: Bergen, L. and N. D. Goodman, 2015, ‘The Strategic Use of Noise in Pragmatic Reasoning’, *Topics in Cognitive Science*, 7: 336–350.

[^blutner-1998]: Blutner, R., 1998, ‘Lexical Pragmatics’, *Journal of Semantics*, 15: 115–162.

[^blutner-2000]: –––, 2000, ‘Some Aspects of Optimality in Natural Language Interpretation’, *Journal of Semantics*, 17: 189–216.

[^brochhagen-2017]: Brochhagen, T., 2017, ‘Signalling under Uncertainty: Interpretative Alignment without a Common Prior’, *British Journal for the Philosophy of Science*, 71: 471–496.

[^brochhagen-2018]: Brochhagen, T., M. Franke, and R. van Rooij, 2018, ‘Co-evolution of Lexical Meaning and Pragmatic Use’, *Cognitive Science*, 42(8): 2757–2789.

[^burnett-2019]: Burnett, H., 2019, ‘Signalling Games, Sociolinguistics and the Construction of Style’, *Linguistics and Philosophy*, 42: 419–450.

[^carcassi-2020]: Carcassi, F., 2020, ‘The Cultural Evolution of Scalar Categorization’, Ph.D. Thesis, University of Edinburgh.

[^clark-2012]: Clark, R., 2012, *Meaningful Games*, Cambridge, MA: MIT Press.

[^cohn-gordon-2019]: Cohn-Gordon, R., N. D. Goodman, and C. Potts, 2019, ‘An Incremental Iterated Response Model of Pragmatics’, *Proceedings of the Society for Computation in Linguistics*, New York: Linguistic Society of America, 81–90.

[^degen-2015]: Degen, J., M. H. Tessler and N. D. Goodman, 2015, ‘Wonky Worlds: Listeners Revise World Knowledge When Utterances Are Odd’, in D. C. Noelle et al. (eds.), *Proceedings of CogSci 37*, 548–553.

[^dekker-2000]: Dekker, P. and R. van Rooij (2000). ‘Bi-Directional Optimality Theory: An Application of Game Theory’, *Journal of Semantics* 17, 217–242

[^ebert-2009]: Ebert, C. and G. Jäger, 2009, ‘Pragmatic Rationalizability’, in A. Riester and T. Solstand (eds.), *Proceedings of Sinn und Bedeutung 14*, SFB 732, vol. 5, University of Stuttgart, 1–15.

[^frank-2012]: Frank, M. C. and N. D. Goodman, 2012, ‘Predicting Pragmatic Reasoning in Language Games’, *Science*, 336: 998.

[^franke-2009]: Franke, M., 2009, ‘Signal to Act’, Ph.D. dissertation, University of Amsterdam.

[^franke-2011]: –––, 2011, ‘Quantity Implicatures, Exhaustive Interpretation, and Rational Conversation’, *Semantics and Pragmatics*, 4(1): 1–81.

[^franke-2014a]: –––, 2014a, ‘Pragmatic Reasoning about Unawareness’, *Erkenntnis*, 79: 729–767.

[^franke-2014b]: –––, 2014b, ‘On Admissibility in Game Theoretic Pragmatics: A Reply to Pavan (2013)’, *Linguistics and Philosophy*, 37: 249–256.

[^franke-2012]: Franke, M. and G. Jäger, 2012, ‘Bidirectional Optimization from Reasoning and Learning in Games’, *Journal of Logic, Language and Information*, 21(1): 117–139

[^franke-2014]: –––, 2014, ‘Pragmatic Back-and-Forth Reasoning’, in S. Pistoia Reda (ed.), *Semantics, Pragmatics and the Case of Scalar Implicatures*, New York: Palgrave MacMillan, 170–200.

[^franke-2016]: –––, 2016, ‘Probabilistic Pragmatics, or why Bayes’ Rule is Probably Important for Pragmatics’, *Zeitschrift für Sprachwissenschaft*, 35:3–44.

[^franke-2012-2]: Franke, M., S. T. de Jager and R. van Rooij, 2012, ‘Relevance in Cooperation and Conflict’, *Journal of Logic and Computation*, 22: 23–54.

[^franke-2015]: Franke, M. and R. van Rooij, 2015, ‘Strategies of Persuasion, Manipulation and Propaganda: Psychological and Social Aspects’, in J. van Benthem, S. Gosh and R. Verbrugge (eds.), *Models of Strategic Reasoning: Logics, Games and Communities*, Berlin: Springer, 255–291.

[^gazdar-1979]: Gazdar, G., 1979, *Pragmatics*, London: Academic Press.

[^grice-1967]: Grice, H.P., 1967, ‘Logic and Conversation’, *William James Lectures*, Harvard University, reprinted in *Studies in the Way of Words*, 1989, Cambridge, MA: Harvard University Press.

[^goodman-2013]: Goodman, N. D. and A. Stuhlmüller, 2013, ‘Knowledge and Implicature: Modeling Language Understanding as Social Cognition’, *Topics in Cognitive Science*, 5: 173–184.

[^goodman-2016]: Goodman, N. D. and M. C. Frank, 2016, ‘Pragmatic Language Interpretation as Probabilistic Inference’, *Trends in Cognitive Sciences*, 20: 818–829.

[^horn-1984]: Horn, L., 1984, ‘Towards a New Taxonomy of Pragmatic Inference: Q-based and R-based Implicature’. In: D. Schiffrin (ed.), *Meaning, Form, and Use in Context: Linguistic Applications*, GURT84, 11–42, Washington; Georgetown University Press.

[^de-2008]: De Jaegher, K., 2008, ‘The Evolution of Horn’s Rule’, *Journal of Economic Methodology*, 15: 275–284.

[^de-2014]: De Jaegher, K. and R. van Rooij, 2014, ‘Game-Theoretic Pragmatics Under Conflicting and Common Interests’, *Erkenntnis*, 79: 769–820.

[^jäger-2002]: Jäger, G., 2002, ‘Some Notes on the Formal Properties of Bidirectional Optimality Theory’, *Journal of Logic, Language and Information*, 11: 427–451.

[^jäger-2014]: –––, 2014, ‘Rationalizable Signaling’, *Erkenntnis*, 79: 673–706.

[^kao-2014]: Kao, J. et al., 2014, ‘Nonliteral Understanding of Number Words’, *Proceedings of the National Academy of Science*, 111(33): 12002–12007.

[^levinson-2000]: Levinson, S. C., 2000, *Presumptive Meanings. The Theory of Generalized Conversational Implicature*, Cambridge, MA: MIT Press.

[^lewis-1969]: Lewis, D., 1969, *Convention*, Cambridge, MA: Harvard University Press.

[^monroe-2017]: Monroe, W., R. X. D. Hawkins, N. D. Goodman and C. Potts, 2017, ‘Colors in Context: A Pragmatic Neural Model for Grounded Language Understanding’, *Transactions of the Association for Computational Linguistics*, Volume 5, pp. 325–338. doi:10.1162/tacl_a_00064

[^parikh-1988]: Parikh, P., 1988, *Language and Strategic Inference*, Ph.D. Thesis, Stanford University.

[^parikh-1991]: –––, 1991, ‘Communication and Strategic Inference’, *Linguistics and Philosophy*, 14: 473–513.

[^parikh-1992]: –––, 1992, ‘A Game-Theoretic Account of Implicature’, *Proceedings of the 4th TARK Conference*, San Francisco: Morgan Kaufmann, 85–94 [[Parikh 1992 available online](http://www.tark.org/proceedings/tark_mar22_92/p85-parikh.pdf)].

[^parikh-2000]: –––, 2000, ‘Communication, Meaning, and Interpretation’, *Linguistics and Philosophy*, 23: 185–212.

[^parikh-2001]: –––, 2001, *The Use of Language*, Stanford, CA: CSLI Publications.

[^parikh-2010]: –––, 2010, *Language and Equilibrium*, Cambridge, MA: The MIT Press.

[^parikh-2019]: –––, 2019, *Communication and Content*, Berlin: Language Science Press.

[^parikh-2024]: –––, 2024, *Meaning Is Everywhere: Language, Artificial Intelligence, Society*, Indianapolis: Hackett Publishing Company.

[^pavan-2013]: Pavan, S., 2013, ‘Scalar Implicatures and Philosophy’, *Linguistics and Philosophy*, 36: 261–290.

[^pavan-2014]: –––, 2014, ‘Rationality in Game-theoretic Pragmatics: A Response to Franke (2014)’, *Linguistics and Philosophy*, 37: 257–261.

[^perea-2012]: Perea, A., 2012, *Epistemic Game Theory: Reasoning and Choice*, Cambridge: Cambridge University Press.

[^potts-2016]: Potts, C., D. Lassiter, R. Levy and M.C. Frank, 2016, ‘Embedded Implicatures as Pragmatic Inferences Under Compositional Lexical Uncertainty’, *Journal of Semantics*, 33: 755–802.

[^prince-1993]: Prince, A. and P. Smolensky, 1993, *Optimality Theory. Constraint interaction in generative grammar*, Cambridge, MA: MIT Press.

[^qing-2016]: Qing, C., N. Goodman and D. Lassiter, 2016, ‘A Rational Speech-Act Model of Projective Content’, in *Proceedings of the 38th Annual Conference of the Cognitive Science Society* (CogSci 2016). [[Qing, et al. 2016 available online](https://api.semanticscholar.org/CorpusID:9740188)]

[^rooij-2004]: Rooij, R. van, 2004, ‘Signalling Games Select Horn Strategies’, *Linguistics and Philosophy*, 27: 493–527.

[^rooij-2008]: –––, 2008, ‘Game Theory and Quantity Implicatures’, *Journal of Economic Methodology*, 15: 261–274.

[^rothschild-2013]: Rothschild, D., 2013, ‘Game Theory and Scalar Implicatures’, *Philosophical Review*, 27: 438–478.

[^sandholm-2010]: Sandholm, W. H., 2010, *Population Games and Evolutionary Dynamics*, Cambridge, MA: MIT Press.

[^schulz-2006]: Schulz, K., and R. van Rooij, 2006, ‘Pragmatic Meaning and Non-monotonic Reasoning: The Case of Exhaustive Interpretation’, *Linguistics and Philosophy*, 29: 205–250.

[^stevens-2016]: Stevens, J., 2016, ‘Focus Games’, *Linguistics and Philosophy*, 39: 395–441.

[^stevens-2018]: Stevens, J. and A. Benz, 2018, ‘Game-theoretic Approaches to Pragmatics’, *Annual Review of Linguistics*, 4: 173–191.

[^yoon-2020]: Yoon, E., M. Tessler, N. Goodman and M. Frank, 2020, ‘Polite Speech Emerges From Competing Social Goals’, *Open Mind*, 4: 71–87.

[^vogel-2014]: Vogel, A., M.C. Frank, D. Jurafsky, and C. Potts, 2014, ‘Learning to Reason Pragmatically with Cognitive Limitations’, *Proceedings of the 36th Annual Meeting of the Cognitive Science Society*, Paul Bello, Marcello Guarini, Marjorie McShane, and Brian Scassellati (eds.), Cognitive Science Society and Curran Associates, Inc., 3055–3060.
