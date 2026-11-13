# 动态语义 Dynamic Semantics (Rick Nouwen、Adrian Brasoveanu、Jan van Eijck、Albert Visser)

*首次发表于 2010 年 8 月 23 日；2016 年 7 月 12 日实质修订。*

动态语义是自然语言语义学的一种视角，强调信息随时间增长。在这一意义表征进路中，文本或话语的片段充当更新既有语境的指令：以新信息作用于语境，所得即更新后的语境。一句话概括：意义即语境变化潜能。

必须意识到这一视角的抽象性，方能防备种种不当推论。其一，人们容易以为动态语义或更新语义至少部分地承诺了语义学的内在论观念，因为信息状态是“内在的”——即完全包含于个体心灵/大脑之中。换言之，人们可能以为动态语义的信息状态就是普特南（1975）所称“方法论唯我论意义上的状态”。参见科学实在论、心灵计算理论、心理内容外在论与窄内容诸词条。然而，这一一般框架对状态究竟是什么未置一词。状态完全可以涵盖解释者所嵌入的环境，从而包含“外在”成分。

第二种可能的误解是：动态语义或更新语义与经典的真值条件语义学完全对立（比较经典逻辑与一阶模型论诸词条）。事实上，本词条马上便会阐明：动态语义是对真值条件语义学的推广，而非截然不同的另起炉灶。经典意义成为话语行动成功施行的“前置条件”（*preconditions*）。动态语义学家主张：*compositional meanings*（组合性意义）具有函数或关系的本性；经典意义可以从关系性的动态意义中恢复出来——作为向其“输入”坐标的*projections*（投射）。

使用抽象框架，其意不在给出经验预测——那是框架内部具体实现的任务。动态语义框架（i）提供一个思考方向，（ii）使我们得以从框架的数学研究中引入方法。由此可知：“自然语言意义是否内在地是动态的”这一问题并没有经验答案。尽管如此，仍可断言：把解释当作线性有序的过程来研究，证明是卓有成效的。

动态语义聚焦发送者与接收者的话语行动，就这一点而言，它接近哲学中面向使用的意义进路，如维特根斯坦与达米特的工作。但不宜把动态语义与这些进路轻易画上等号。作为抽象框架，动态语义与许多看待意义与解释的哲学立场相容。动态语义的目标是为意义与解释建模（*model*）。为此无需回答更宽泛的哲学问题——例如，究竟是什么使主体得以与这些意义相关联。比如，在动态谓词逻辑中，我们把 *horse*（马）的意义当作既定的，而不断言“主体拥有 *horse* 概念意味着什么”；我们只是规定主体拥有它。这并不是说这类问题——它们正是维特根斯坦与达米特工作的核心——最终无须回答；只是说，即便一个模型不回答它们，模型本身也可以饶有趣味。（要注意：动态语义试图给出系统而组合性的意义说明，这使其精神气质与维特根斯坦后期哲学判然有别。）

动态语义的一种进路是“话语表现理论”（*discourse representation theory*，DRT，Kamp 1981）[^kamp-1981]。（与坎普进路密切相关的是艾琳·海姆的“文件变化语义学”（*file change semantics*，FCS，Heim 1983a）[^heim-1983a]与 Seuren（1985）的话语语义学。）DRT 中的意义是所谓的“话语表现结构”（*discourse representation structures*，DRS）。这些结构是一类储存具体信息片段的数据库。DRS 本身是静态对象，但 DRT 仍堪称动态语义框架：它使我们能把意义的组合过程理解为一个合并（*merging*）话语表现结构的过程。如此，信息变化便内嵌为解释过程不可分割的一部分。

本词条的主要关注点是动态语义的第二种进路，途中我们会不时以 DRT 作参照。在这第二种进路中，动态意义是行动的类型——由其所引发的变化来个体化的东西。这是与“动态谓词逻辑”（*dynamic predicate logic*，DPL，Groenendijk and Stokhof 1991a）[^groenendijk-1991a]相联系的进路。按照这一动态语义传统，意义是对“接收者的信息状态将如何受到修改”的一种规定。例如，它可以是一个函数，把旧信息状态映射到一个已按该意义所含信息*updated*（更新）的状态；或者，它也可以是一个关系，表达该意义所带来的信息变化属于何种类型。（关于这一传统的早期工作，参见 Groenendijk and Stokhof 1991a,b; Muskens 1991; Dekker 1993; Vermeulen 1993; van Eijck 1994; Vermeulen 1994; Krahmer 1995; van den Berg 1996; Groenendijk et al. 1996; Aloni 1997; Muskens et al. 1997）[^aloni-1997][^berg-1996][^dekker-1993][^eijck-1994][^groenendijk-1991a][^groenendijk-1996][^krahmer-1995][^muskens-1991][^muskens-1997][^vermeulen-1993][^vermeulen-1994]。

## 1. 作为过程的解释

陈述句的解释既可当作产物，也可当作过程。取产物视角，关注的是给定情境下的真概念；取过程视角，对命题的解释则是信息更新的一步——它让我们用一个更准确的新知识状态替换原有的知识状态。动态语义取的是过程视角。

### 1.1 更新语义

更新语义是“解释即过程”观念的一种特定实现方式。其核心思想非常简单。我们从一个简单模型出发：一位听者/接收者依次接收信息条目。任一时刻听者都处于某种状态——她拥有某些信息；传入信息以系统的方式修改这一状态。我们把传入条目的意义分析为它们对接收者信息状态之改变的贡献。由此，意义成了行动，或者更准确地说，成了 *action types*（行动类型）：它们不是某个给定状态到另一状态的具体改变，而是这类具体改变的共同之处。

### 1.2 作为更新逻辑的命题逻辑

命题逻辑（否定、析取与合取的逻辑）可以按如下方式看作更新逻辑。设有三个基本命题 $p, q$ 与 $r$，对其真假一无所知，则共有八种可能：$\{ \bar{p} \bar{q} \bar{r}, p \bar{q} \bar{r}, \bar{p} q \bar{r}, \bar{p} \bar{q} r, pq \bar{r}, p \bar{q} r, \bar{p} qr, pqr \}$。其中 $\bar{p} \bar{q} \bar{r}$ 应读作：$p, q, r$ 皆不为真；$p \bar{q} \bar{r}$ 读作：$p$ 为真而 $q$ 与 $r$ 为假；依此类推。现在宣告 $\neg p$（“非 $p$”），八种可能中四种随之消失，剩下 $\{\bar{p} \bar{q} \bar{r}, \bar{p} q \bar{r}, \bar{p} \bar{q} r, \bar{p} qr\}$。再宣告 $q \vee \neg r$（“$q$ 或非 $r$”），可能情形 $\bar{p} \bar{q} r$ 遭到排除，剩下 $\{ \bar{p} \bar{q} \bar{r}, \bar{p} q \bar{r}, \bar{p} qr \}$。如此类推。$\neg p$ 与 $q \vee \neg r$ 这类命题的意义，便可看作从可能集到其子集的映射。

可能的集合代表知识状态。上例中，$\{ \bar{p} \bar{q} \bar{r}, p \bar{q} \bar{r}, \bar{p} q \bar{r}, \bar{p} \bar{q} r, pq \bar{r}, p \bar{q} r, \bar{p} qr, pqr \}$ 代表对命题 $p, q, r$ 全然无知的状态；$\{ pq \bar{r} \}$ 这样的单元集代表对它们的完全知识；空集 $\varnothing$ 则代表处理 $p, q$ 与 $r$ 的不相容陈述后陷入的不一致状态。下面我们逐一列出命题语言诸陈述的动态意义：

- 原子陈述：即 $p, q, r$。相应的更新行动，是从当前语境中选出字母未被打杠（加横线）的那些可能。
- 否定陈述：形如 $\neg \phi$。相应的更新行动，是从当前语境中选出构成 $\phi$ 陈述所选可能集之补集的那些可能。
- 陈述的合取：形如 $\phi \wedge \psi$。相应的更新行动，是从当前语境中选出构成 $\phi$ 陈述与 $\psi$ 陈述对当前语境所作选择之交的那些可能。
- 陈述的析取：形如 $\phi \vee \psi$。相应的更新行动，是从当前语境中选出构成 $\phi$ 陈述与 $\psi$ 陈述所作选择之并的那些可能。

由此，命题联结词的意义成为这样一类操作：从代表某一知识状态的旧语境，转到代表处理命题信息后所得知识状态的新语境。

### 1.3 程序设计语句及其执行

将更新语义的行动与程序设计语句及其执行作比较，颇有教益：这种比较初步展示了量化在动态环境中的运作方式。命令式语言的程序设计语句在机器状态的语境中得到解释（或“执行”），机器状态则可视为值在寄存器上的分配。设寄存器以变量 $x, y, z$ 命名，其内容为自然数，则下面便是一个机器状态：

$$ \begin{array}{|c|c|}\hline x & 12 \\\hline y & 117 \\\hline z & 3 \\\hline \end{array} $$

若语句 $z := x$ 在此状态中被执行（即“解释”）——按 C 语法，该语句本有更简单的形式 $z = x)$——结果便是新的机器状态：

$$ \begin{array}{|c|c|}\hline x & 12 \\\hline y & 117 \\\hline z & 12 \\\hline \end{array} $$

在此状态中执行语句序列 $x := y$; $y := z$，则结果是：

$$ \begin{array}{|c|c|}\hline x & 117 \\\hline y & 12 \\\hline z & 12 \\\hline \end{array} $$

这说明：序列 $z := x$; $x := y$; $y := z$ 的执行效果是 $x$ 与 $y$ 的值互换，附带一个副作用——$z$ 的旧值就此丢失。换言之，程序 $z := x$; $x := y$; $y := z$ 的意义可看作从输入机器状态 $s$ 到输出机器状态 $s'$ 的映射，后者与 $s$ 的差异如下：$s'(x) = s(y)$ 且 $s'(y) = s(x)$（即 $x$ 与 $y$ 的输入值在输出状态中互换），同时 $s'(z) = s'(y)$。

现在考虑存在量词“存在一个 $x$ 使得 $A$”。假设把这个量词加进命令式程序设计语言，它的意义会是什么？它将是一条指令——用一个具有性质 $A$ 的新值替换 $x$ 的旧值。这可以分解为“存在 $x$”与测试“$A$”两个部分。一个公式/指令是测试（*test*），如果它所贡献的更新逐一取出输入语境中的状态，检验其是否满足特定条件：满足者纳入输出语境，不满足者弃之。换言之，测试就是这样一种更新——取一个输入语境，输出其一个子集。上文“作为更新逻辑的命题逻辑”一节中的命题逻辑公式全是测试。

“存在 $x$”与测试“$A$”两个部分由顺序复合粘合为一体：“$\exists x$; $A$”。单看“$\exists x$”部分，它的自然意义是什么？一条指令——用某个任意新值替换 $x$ 的旧值。这同样是输入状态与输出状态之间的关系；与 $x := y$ 这类确定赋值的差别在于，此时该关系不是函数。事实上，量词的这种关系性意义正体现在人所共知的一阶逻辑塔斯基式真值定义之中（比较塔斯基的真值定义词条）：

> $\exists x\phi$ 在模型 $M$ 中相对于变元指派 $\alpha$ 为真，当且仅当：存在某个变元指派 $\beta$，$\beta$ 与 $\alpha$ 至多在指派给 $x$ 的值上不同，且 $\phi$ 在 $M$ 中相对于指派 $\beta$ 为真。

塔斯基定义中隐含着一个关系：它成立于指派 $\alpha$ 与 $\beta$ 之间，当且仅当对一切异于 $x$ 的变元 $y$ 都有 $\alpha(y) = \beta(y)$。这一关系常被称为“x 的随机重置”（*random reset of x*），记作 [$x$]。对任意变元 $x$，全指派之间的二元关系 [$x$] 都是等价关系——即自反、对称且传递的二元关系。下文将看到，这类关系如何在一阶谓词逻辑的动态化版本中发挥作用。

若取 [$x$] 作为 “$\exists x$” 的意义，须注意：其性质与测试迥然不同——它会在输出语境中产生新值。相比之下，测试式更新所得到的输出语境总是输入语境的子集，因而相对于输入语境永远不可能含有任何新内容。

### 1.4 动态语义中的语境（*context*）概念

信息状态常被称为语境（*contexts*）：状态是“解释”（即对形式语言或自然语言表达式作语义赋值）的前置条件。“语境”一词的使用也表明，我们关心的并非接收者全部状态，而只是它同所聚焦表达式/信息条目之解释相关的方面。因此，动态传统中的意义常被称为“语境变化潜能”（*context change potentials*）。

大而观之，动态语义中意义所致的变化确实关乎*context*（语境）的诸方面；但须注意，语义学家谈论语境时所指可能五花八门（比较认知语境主义与指示词诸词条），不同观点由此催生出处理不同问题的动态语义诸变种。这些问题包括：为代词指称构造恰当机制（比较回指与指称诸词条）；解释条件句的语义学（比较条件句与条件句逻辑诸词条）；对断言与预设之区分作语义处理并发展“预设投射”理论（比较断言、言语行为、含义、语用学诸词条）；解释话语的解释如何受到说话者与听者之间既有共同基础的影响与引导，并发展关于共同基础如何随话语推进而演化的理论（比较语用学与含义诸词条）。

语境牵涉两个互不相干的区分。其一是语境与修改语境者之间的区分：此时语境是信息状态或其适当抽象（比较信息的语义概念词条），语境修改者则是所接收信息条目的（意义）。若无正确类型的预设信息状态，信息便无从接收。在经典静态谓词逻辑（比较经典逻辑与一阶模型论诸词条）中，恰当的对应物是：信息状态为一个指派（环境）或指派集，所接收信息为一个指派集。其二是语境与内容之间的区分：此时语境近似于接收者的存储容量，加上种种可能影响新表达式/信息条目之解释的特征；内容则是所存储的（事实性、真值条件性）信息。例如，此意义上的语境可以是一组寄存器/变量，或者以 DRT/FCS 的术语说，话语所指或文件；内容则可以是某个指派集，抑或世界/指派对——后者约束这些话语所指的取值，也约束哪些世界是现实世界的现实候选。

举一个例子来说明这些区分。设信息状态为一个二元组：一个有限的话语所指集，加上一个世界/指派对的集合，其中指派的定义域恰为该话语所指有限集。这样的状态便是第一意义上的语境；话语所指集则是第二意义上的语境。一种基本更新是内容更新——约束世界/指派对的集合，而令所指集保持不变。另一种基本更新是扩展所指集——扩充已分配的存储容量：把给定的世界/指派对改造为世界与扩展指派的配对；扩展指派受旧指派约束，但在新所指上取一切可能值。于是，此例中的更新过程是二维的：既有内容更新，又有第二意义上的语境更新。

## 2. 动态谓词逻辑

### 2.1. 概念基础

为自然语言建立动态语义框架的动机，首先且最主要来自人称代词的指称与不定名词短语指称之间潜在的依赖关系。这类依赖最简单的例子是共指性的话语回指，例如：

- (1) *Mary met a student yesterday. He needed help.*（玛丽昨天遇到一位学生。他需要帮助。）

值得注意的是：这一句列与单个句子意义相同：

- (2) *Yesterday, Mary met a student who needed help.*（昨天，玛丽遇到一位需要帮助的学生。）

假设不定词是存在量词，则 (2) 的分析并不难：它只是说存在一个 $x$——是学生，昨天遇到玛丽，当时需要她的帮助。用谓词逻辑表示：

- (3) $\exists x(\texttt{student}(x)\wedge\texttt{met}(m,x)\wedge\texttt{need-help}(x))$

然而，(1) 这个等价的两句例子却得不到类似的分析。原因在于解释是组合性的（*compositional*，参见组合性词条的讨论）：组合性分析会先给出 *Mary met a student yesterday*（玛丽昨天遇到一位学生）的分析，形如 $\exists x(\texttt{student}(x)\wedge\texttt{met}(m,x))$；第二个句子则对应于 $\texttt{need-help}(x)$。再假设合并多句的默认方式是合取，我们便得到：

- (4) $\exists x(\texttt{student}(x)\wedge\texttt{met}(m,x))\wedge\texttt{need-help}(x)$

$x$ 的最后一次出现未被约束——在经典谓词逻辑中，我们并没有得到 (1) 与 (2) 的等价翻译。结论是：要在静态语义框架内说明 (1) 与 (2) 的等价性，就无法为单个句子保持组合性解释，而不得不把 (1) 中的话语当作整体来解释。

这有悖直觉。我们知道 (1) 中单个句子是什么意思，也想捕捉这些意义与其他意义组合成一个有意义整体的潜能——这个整体对应于一个句子序列。动态语义让我们能在句子与超句子两个层面给出完全组合性的意义分析。其做法是保证：与经典谓词逻辑相反，在经典谓词逻辑语法的*dynamic*（动态）解释下，(3) 与 (4) *are*（恰恰）等价。特别地，下式在动态谓词逻辑中有效：

$$\exists x(\psi \wedge \phi) \textrm{ 当且仅当 } \exists x(\psi)\wedge \phi$$

在这种自然语言动态语义中，句子的意义不再对应一组真值条件，而对应于施加在语境上的行动。行动分两类。像 $\texttt{need-help}(x)$ 或 $\texttt{met}(m,x)$ 这样的谓述是测试（*tests*）：它们只检查当前语境中每个状态/指派给 $x$ 的值是否满足相关谓词；当且仅当满足，测试便把未经改变的指派传递到输出语境。相比之下，存在量词不是测试——它有能力随机重置其相关变元的值，从而改变语境。于是，$\exists x(\psi)$ 取一个语境，随机改变其中每个指派上 $x$ 的值，若这些改动后的指派还满足测试 $\psi$ 所贡献的条件，便把它们传递到输出语境。

这一语义的主要推论之一：存在量词的辖域原则上不受限制。它改变某变元的值；在该变元再次变化之前，任何后续测试访问的都是这次设置的特定值。这也意味着，存在量化的语义可以完全抛开辖域来给出：$\exists x$ 的意义是这样一种行动——取一个语境，返回同一语境，只是其中 $x$ 的值至多被随机替换为另一个值。（下文将详细展开。）

至此，“动态语义”一词（应用于自然语言时）已显现两种含义。首要的一层：动态语义是一般观念——逻辑陈述表达的不是真值条件，而是施加于语境的行动（语境可以多种方式概念化）。第二层理解：动态语义指一组理论立场，见于关于某些自然语言现象之语义学的争论，最突出者是代词回指。（下文就预设（*presupposition*）给出对动态语义的类似理解。）就回指而言，这一理论性理解体现为两个假说的结合：(i) 代词对应于变元；(ii) 不定词是非量词性的——它们只贡献一个动态的变元指派更新。由第二个假说可知，“动态语义”的这种理论用法已预设了更一般的观点：意义是施加于语境的行动。

在转向动态谓词逻辑的定义之前，须注意：动态语义处理回指的路线并非文献中仅有的一条。我们也可以放弃“代词对应变元”的想法，转而赋予代词一种更繁复的意义——类似有定描述语的意义。在当代传统中，这类想法早在蒯因（1960）与吉奇（1962）便已萌芽，后经（尤其是）埃文斯（1977, 1980）、Parsons（1978，其他网络资源）、海姆（1990）与 Elbourne（2001, 2005）臻于成熟。相关讨论参见 Nouwen（forthcoming）。

### 2.2 动态谓词逻辑的严格刻画

上一小节初步窥见了动态语义框架的基本目标：定义一种逻辑语义，使陈述表达行动；具体说，使存在量化有能力重置变元，从而*changing*（改变）语境。如何做到这一点？线索来自对普通谓词逻辑中存在量化定义的考察。设我们使用固定变元集 $\textsf{VAR}$ 在固定论域 $D$ 上的全指派，则全指派之集 $\textsf{ASSIGN}$ 便是从 $\textsf{VAR}$ 到 $D$ 的所有（全）函数之集。

令 $P(x)$ 这类原子公式的意义为集合 $F$：一切使 $\alpha(x)$ 为满足 $P$ 之对象的指派 $\alpha$ 的集合。

现在定义：$$ \alpha[x]\beta := \forall v \in \textsf{VAR}\setminus\{x\}\ (\alpha(v) = \beta(v)). $$ 于是 [$x$] 就是二元关系“指派 $\beta$ 是（至多）重置指派 $\alpha$ 中变元 $x$ 之值的结果”。如前所述，这是变元指派上的等价关系。$\exists x P(x)$ 的意义 $G$ 便是：$$ G := \{\alpha \in \textsf{ASSIGN } \mid \exists \beta \in F \alpha[x]\beta \}. $$ 也就是说，$G$ 是这样一些指派的集合：对 $x$ 重置成功，且经此重置得到 $F$ 中的指派。换个角度看，$G$ 恰是下述关系 $R$ 的定义域（*the domain of*）：$$\alpha R\beta := \alpha[x]\beta \textrm{ 且 } \beta \in F. $$

可以说，$G$ 是重置行动 $R$ 的前置条件。$\textsf{DPL}$ 的想法在于：$\exists x P(x)$ 的意义不取前置条件 $G$（经典静态一阶逻辑的做法），而取重置行动 $R$。如此并不损失信息——$G$ 总能从 $R$ 重新得到。再者，关系 $R$ 的值域由这样一些指派 $\beta$ 组成：与前置条件 $G$ 中的指派相比，其差异至多在 $x$ 的值上，且也在 $F$ 中（即 $\beta(x)$ 属于 $P$ 的解释）。二元关系 $R$ 值域中存储的 $x$ 值，恰是满足 $P$ 的那些 $x$ 值——即我们要找的值。

更一般地，我们取指派之间的二元关系（*binary relations*）为 $\textsf{DPL}$-意义。这类关系可视为（对）重置行动（*resetting actions*）的建模。这是建模行动的一种惯用法——简单得近乎朴素，却广为人知且实用：行动被看作行动之前的世界状态与行动之后相应状态之间的关系。

以下是完整定义。设非空论域 $D$、变元集 $\textsf{VAR}$，以及基调为 $\Sigma$ 的模型 $\mathcal{M}=\langle D, I\rangle$。原子条件 $\pi$ 形如 $P(x_0 , \ldots ,x_{n-1})$，其中 $P\in \Sigma$ 元数为 $n$；原子重置 $\varepsilon$ 形如 $\exists v$，$v$ 为变元。$\Sigma$ 上的谓词逻辑语言由下式给出（$\cdot$ 为合取，${\sim}$ 为否定）：

$$ \phi ::= \bot \mid \top \mid \pi \mid \varepsilon \mid \phi \cdot \phi \mid {\sim}(\phi). $$

指派是 $\textsf{ASSIGN} := D^{\textsf{VAR}}$ 中的元素 $\alpha , \beta ,\ldots$。此语言的动态/关系语义定义如下：

- $\alpha[\bot]\beta := \alpha \ne \alpha$。
- $\alpha[\top]\beta := \alpha = \beta$。
- $\alpha[P(x_0 , \ldots ,x_{n-1})]\beta := \alpha = \beta$，且 $\langle \alpha(x_0), \ldots ,\alpha(x_{n-1})\rangle \in I(P)$；此处 $P\in \Sigma$ 的元数为 $n$。
- $\alpha[\exists v]\beta := \alpha[v]\beta$
- $\alpha[\phi \cdot \psi]\beta :=$ 存在 $\gamma$，使 $\alpha[\phi]\gamma$ 且 $\gamma[\psi]\beta$；简记为 $\alpha[\phi]\gamma[\psi]\beta$。
- $\alpha[{\sim}(\phi)]\beta := \alpha = \beta$，且不存在 $\gamma$ 使 $\alpha[\phi]\gamma$。

注意：合取 $\cdot$ 解释为关系复合；否定 ${\sim}$ 则基本上解释为取补——相对于被否定公式所表关系的定义域取补。

真以关系意义来定义：基本上，我们把指派之间的二元关系投射到其第一坐标：

$$\alpha \vDash \phi := \exists \beta\ \alpha[\phi]\beta.$$

蕴涵 $\phi \rightarrow \psi$ 可定义为 ${\sim}(\phi \cdot {\sim}\psi)$。将真值定义应用于此，得：

> $\alpha \vDash \phi \rightarrow \psi \textrm{ 当且仅当 } \forall \beta(\alpha[\phi]\beta \Rightarrow \beta \vDash \psi)$：即任何由前件 $\phi$ 更新 $\alpha$ 而得的指派 $\beta$，都满足后件 $\psi$。

关系意义还给出如下漂亮的动态衍推定义：

$$\phi \vDash \psi := \forall \alpha , \beta(\alpha[\phi]\beta \Rightarrow \exists \gamma \beta[\psi]\gamma).$$

这一定义由汉斯·坎普在其开创性论文（Kamp 1981）中首次引入。非形式地说：任何已并入 $\phi$ 所贡献之更新的指派 $\beta$，都保证支持/满足 $\psi$。

注意：${\sim}\phi$ 等价于 $(\phi \rightarrow \bot)$；$(\phi \rightarrow \psi)$ 为真，当且仅当 $\phi \vDash \psi$。同样重要的是，$\forall x (\phi)$ 可定义为 $(\exists x \rightarrow \phi)$。

$\exists v$ 的一种可行替代记法是 [$v := ?$]（随机重置），以凸显其与程序设计语言中随机赋值的关联。

谓词符号的解释是条件（*conditions*）：它们是对角线 $\{\langle \alpha , \alpha \rangle \mid \alpha \in \textsf{ASSIGN}\}$（即 $\top$ 的意义）的子集。对角线的子集皆为测试：不修改任何东西，只放行合格者（满足条件者），淘汰不合格者。把指派集 $F$ 映为条件 $\{\langle \alpha , \alpha \rangle \mid \alpha \in F\}$ 的映射 $\textsf{diag}$，正是经典静态世界与动态世界之间的纽带。例如，$\textsf{diag}(F)$ 与 $\textsf{diag}(G)$ 的关系复合即 $\textsf{diag}(F\cap G)$。

经典一阶逻辑（FOL）可在 $\textsf{DPL}$ 中作如下解释。设 FOL 语言具有如下联结词与量词：$\top , \bot , \wedge , \rightarrow , \exists x$。翻译方式如下：

- $( )^*$ 与原子公式及 $\rightarrow$ 可交换
- $(\phi \wedge \psi)^* := \phi^* \cdot \psi^*$
- $(\exists x(\phi))^* := \neg \neg(\exists x \cdot \phi^*)$

由此得到：$[\phi^*]$ 是 $\phi$ 的经典解释的对角线。这一翻译是组合性的，它表明 FOL 可取作 $\textsf{DPL}$ 的一个片段（*fragment*）。

反过来，任何 $\textsf{DPL}$-公式 $\phi$ 皆可翻译为谓词逻辑公式 $\phi$°，使 $[\phi]$ 的定义域恰为 $\phi$° 的经典解释。定义这一翻译的途径之一，是借助带 Floyd-Hoare 规则的前置条件演算（Eijck and de Vries 1992）[^eijck-1992]；下面是它的一个变体。取标准谓词逻辑的语言，增添菱形模态 $\langle \psi \rangle \phi$：$\psi$ 遍历 DPL 公式，而 $\alpha \vDash \langle \psi \rangle \phi$ 当且仅当存在指派 $\beta$ 使 $\alpha[\psi]\beta$ 且 $\beta \vDash \phi$。下列等价式表明，这一扩张并不增加表达能力。

- $\langle \bot \rangle \phi \leftrightarrow \bot$。
- $\langle \top \rangle \phi \leftrightarrow \phi$。
- $\langle P(x_1 \ldots x_n)\rangle \phi \leftrightarrow (P(x_1 \ldots x_n) \wedge \phi)$。
- $\langle \exists v\rangle \phi \leftrightarrow \exists v\phi$。
- $\langle \psi_1 \cdot \psi_2\rangle \phi \leftrightarrow \langle \psi_1\rangle \langle \psi_2\rangle \phi$。
- $\langle{\sim}(\psi)\rangle \phi \leftrightarrow(\neg(\langle \psi \rangle \top) \wedge \phi)$。

所以在弱的意义上说，“$\textsf{DPL}$ 中没有新事情发生”：我们不能定义任何在 FOL 中无法定义的集合。诸模态的等价式确定了一个翻译 ( )°，它给出实现给定后置条件的最弱前置条件；下一节将示例说明这种翻译。

### 2.3 示例：驴子句

动态谓词逻辑的优点之一是：它能对驴子句作平直的组合性分析（Geach 1962；参见回指词条）[^geach-1962]。

- (5) 如果一位农夫拥有一头驴，他就打它。（If a farmer owns a donkey, he beats it.）

显然，代词 $he$ 与 $it$ 分别同不定词 *a farmer* 与 *a donkey* 存在依赖关系。简言之，经典分析处理 (5) 的难处是：它只提供两种选择，合起来仍覆盖不了 (5) 的可能意义。若把不定词处理为指称某位特定农夫与某头特定的驴，把代词处理为单纯捡起这些实体，我们便得到 (5) 的一种可行却不凸显的读法。而最突出的读法刻画拥有关系与殴打关系共变：任何在拥有（*own*）关系中的农夫-驴对，也在殴打（*beat*）关系之中。显然，须把不定词解释为量词；但一旦如此，它们便无法约束条件句后件中的变元——组合性分析会把代词贡献的变元置于条件句前件中存在量词的经典辖域之外。就是说，(6) 给不出 (5) 的正确真值条件。

- (6) $(\exists x(\textrm{farmer}(x)\wedge \exists y(\textrm{donkey}(y)\wedge\textrm{own}(x,y))))\rightarrow\textrm{beat}(x,y)$

(6) 的动态版本是 (7)，它给出正确的真值条件：对 $x$ 与 $y$ 的任何随机重置——只要 $x$ 是农夫、$y$ 是 $x$ 拥有的驴——便有 $x$ 打 $y$。

- (7) $\exists x\cdot \textrm{farmer}(x)\cdot \exists y\cdot \textrm{donkey}(y)\cdot \textrm{own}(x,y)\rightarrow \textrm{beat}(x,y)$

有趣的是，( )° 把 (7) 翻译到谓词逻辑，所得并非 (6) 而是 (8)。故问题不在于谓词逻辑无法表达驴子条件句的真值条件，而在于 (8) 这样的句子不太可能是组合性解释过程的最终产物（但参见 Barker and Shan 2008）[^barker-2008]。

- (8) $\neg \exists x (\textrm{farmer} (x) \wedge \exists y (\textrm{donkey} (y) \wedge \textrm{own}(x,y) \wedge \neg \textrm{beat}(x,y))).$

(8) 可从 (6) 如此推导：

$$ \begin{array}{l} (\langle(\exists x \cdot Fx \cdot \exists y \cdot Dy \cdot Hxy ) \rightarrow Bxy \rangle \top) ° \\ = (\langle{\sim}((\exists x \cdot Fx \cdot \exists y \cdot Dy \cdot Hxy ) \cdot {\sim} Bxy ) \rangle \top) ° \\ = \neg(\langle(\exists x \cdot Fx \cdot \exists y \cdot Dy \cdot Hxy ) \cdot {\sim} Bxy \rangle \top) ° \\ =\ldots \\ = \neg \exists x (Fx \wedge \exists y (Dy \wedge Hxy \wedge \neg Bxy ))).\\ \end{array} $$

### 2.4 动态广义量化

动态谓词逻辑得以成功应用于自然语言中量化与回指的交互，系于一个事实：在 DPL 中存在量化是动态的，全称量化则不然。若全称量化也是动态的，会怎样？首先，平行于随机重置行动 $\exists x$ 去定义全称量化行动 $\forall x$，毫无意义：全称量化只有在给定论域（*restrictor*，限制域）上、相对于某个给定性质（*scope*，辖域）才有意义。其次，若给 $\forall x(\phi)(\psi)$ 一个动态解释，它会预测全称量词可以像存在量词那样跨越小句边界与单数代词建立回指关系。对 (9) 这类情形，这显然不可取。

- (9) 每个男孩都写了一篇文章。#他还写了一份研究计划。（Every boy wrote an essay. #He wrote a research proposal too.）

然而，一旦转向复数回指（*plural anaphora*），情况立刻不同：全称量化的静态性质——事实上还有其他非不定广义量词的静态性质——不应被想当然地接受。例如，(10) 允许一种读法，其中 *they* 与 *every boy* 形成回指关联。

- (10) 每个男孩都写了一篇文章。他们也都写了一份研究计划。（Every boy wrote an essay. They wrote a research proposal too.）

设想像 (10) 这样的例子应得到动态处理（替代解释的辨析参见早前的评论与 Nouwen, forthcoming），结论便只能是：全称量词不应获得静态解释。接下来的问题是：何种解释才恰当，它又如何把 (9) 中不受接受的回指情形与 (10) 的情形区分开。一种方案是区分两类值：量词在其辖域内约束变元所取的值，与该变元在量词辖域之外获得的指派值。（这一策略例如参见 Kamp and Reyle 1993，讨论参见 Nouwen 2007。）[^kamp-1993][^nouwen-2007]为了解释 (10)，可让 (10) 首句中受量词约束的变元出现遍历个体男孩，而该变元在量词辖域之外（即第二句中）被指派全体男孩的复数整体。然而，正如 van den Berg（1996）最早指出的，此路只走到一半：在话语中，代词不仅能访问与量词相联系的复数整体，还能访问这些量词所牵涉的关系。例如，(11) 第二句中的代词 $it$ 与主语中对男孩们的量化共变，结果第二句被理解为：每个男孩提交了他（$he$）写的那篇文章（参见 van den Berg 1996; Krifka 1996; Nouwen 2003; Brasoveanu 2007, 2008）[^berg-1996][^brasoveanu-2007][^krifka-1996][^nouwen-2003]。

- (11) 每个男孩都写了一篇文章。他们每个人都把它投给了一份期刊。（Every boy wrote an essay. Each of them submitted it to a journal.）

广义量化与复数回指之动态处理的主导思想是：表示复数值时不把复数整体指派给变元，而是采纳一种允许指派函数之复数整体（如集合）的语境概念。设 (11) 的首句被译成带动态量词的动态谓词逻辑：$\forall x(\textrm{boy}(x))(\exists y\cdot \textrm{essay}(y)\cdot \textrm{wrote}(x,y))$。解释这类公式需要收集指派函数：$x$ 取值为男孩，$y$ 取值为该男孩所写文章。全称量词要求此类收集涵盖谓词 *boy* 的一切可能值。到了后续话语，我们便能访问所有 $x$ 值之集（即全体男孩）与所有 $y$ 值之集（即男孩们所写文章），也能访问一个个男孩-文章对。在 (11) 首句之后的语境指派集中，每个原子指派 $f$ 都满足：$f(y)$ 是男孩 $f(x)$ 写的文章。要解释 (11) 的回指情形，只差一个假设：那里的全称量化遍历指派函数，而不只是遍历值。实现这一思想的诸种方式，参见 van den Berg (1996), Nouwen (2007, forthcoming), Brasoveanu (2007, 2008, 2013)。

结论是：只要语境概念结构得当，量词一般都能获得动态解释。一个重要推论是：这类分析能扩展到非名词性量词（Brasoveanu 2007）[^brasoveanu-2007]。像 (11) 这样的情形可描述为量化从属的情形；结构化语境进路可以看作旨在为从属背后的机制开一扇窗。至于情态从属的情形（Roberts 1987, 1989）[^roberts-1987]，如著名的 (12)，亦可获得平行处理。

- (12) 可能有一匹狼进来。它可能会吃掉你。（A wolf might come in. It may eat you.）

情态词 *might* 引入一个作用于可能世界之上的量词，其辖域覆盖不定词 *a wolf*——正如上文 (11) 中 *every boy* 的辖域覆盖 *an essay*。因此，(12) 首句所贡献的更新，其输出指派函数之集将存储两类内容：一是 *might* 贡献的可能世界之集，这些世界相对于现实世界是认知上可能的；二是在这些认知可达世界中进来的狼之集。(12) 的第二句便可进一步展开世界与狼之间的依赖：要求至少某些认知可能性满足——相应的狼不但进来，还要吃掉你。

### 2.5 回指之外的动态性

回指与预设（见下文）固然是常被认为需要动态语义分析的核心语言现象，但原则上，语境的任何方面都可能成为某现象的目标——只要该现象值得对解释作动态分析。Barker（2002）对模糊陈述所提供信息的处理颇具启发性。Barker 假设语境含有 *tall*（高）这类模糊形容词的精确标准。如此一来，(19) 这样的句子可以有两种截然不同的用法。(19) John is tall（约翰很高）。若信息状态含有关于什么算作 *tall* 的足够精确的信息，说出 (19) 便可用于提供约翰身高的信息；反之，若听者对 *tall* 这类表达式的恰当精确化一无所知（比如他是外星人或外国人），却掌握约翰的身高信息，则 (19) 可用于提供关于标准本身的信息。

## 3. 预设

### 3.1 预设与联结词的动态语义

语境在预设中作用关键。像 (13) 这样的句子预设约翰迟到了；但把它放进一个恰恰提供该信息的语境——如 (14)——预设便消失了。在 (14) 中，约翰迟到属*asserted*（断言）的内容，而非预设。

- (13) Mary knows that John is late（玛丽知道约翰迟到了）
- (14) John is late and Mary knows that he is late.（约翰迟到了，玛丽也知道这一点。）

斯托尔内克（1973）把预设看作以假定的共同知识为基础。说出像 (13) 这样的句子，就是*takes for granted*（视之为当然）：“约翰迟到”已是共同知识。在此意义上，(13) 要求说话语境已然具备这一共同知识。相比之下，(14) 没有这种要求，原因很直白：(14) 的第一个合取支断言了第二个合取支所视之为当然的内容。斯托尔内克的关键假设是：解释是增量的——对形如 [$S$1 and $S$2] 的句子，$S$2 的解释发生在一个已被 $S$1 更新过的语境中。图式如下：

- (15) ${C}[{S1 \textrm{ 且 } S2}] = ({C}[{S1}])({S2})$

斯托尔内克对 (15) 图式的解读是语用的：在话语中遇到一串小句时，我们*in light of*（根据）一个已被前述小句之解释所充实的语境来解释这些小句。这一增量解释思想简单却有力，对具有合取性解释的复杂话语（如带 *and* 的并列结构、陈述句的简单序列）完全适用。既然合取中的合取支具有断言之力（*assertoric force*），它们便可用来更新语境、创设一个新的局部语境。问题在于：预设并不只在合取环境中消失。与 (14) 一样，(16) 同样不要求“约翰迟到”是共同知识；但这里第一个析取支并不具有断言之力（讨论例如参见 Schlenker 2009）[^schlenker-2009]。何种语用规则能解释 (16) 中预设的缺失，并不显然。

- (16) 约翰要么没迟到，要么玛丽不知道他迟到了。（Either John is not late or Mary does not know that he is late.）

像 (16) 这样的例子令人怀疑 (15) 这类增量解释图式的价值。此外，(15) 对解释如何推进所作的假设也颇为僭越：断言一个命题内容为 $p$ 的小句，并不会自动使 $p$ 成为共同知识。毋宁说，这样的断言应视为一项*proposal*（提议）——提议把 $p$ 确立为共同知识。$p$ 是否成为共同基础（*common ground*），取决于其他对话者是否愿意接受该命题（例如，不对这一断言提出异议）。换言之，(15) 似乎不适合刻画信息流动（的动态性）背后的语用学。

一个可能的出路：把 (15) 看作语义规则而非语用规则，用动态的解释概念来表述。这一方案最突出地见于 Heim 1983b，上承 Karttunen 1973。卡尔图宁区分全局语境（*global contexts*，当前句子据以赋值）与局部语境（*local contexts*，当前小句——或潜在的某个小于小句的实体——据以解释）。现在的想法是：像 (15) 这样的规则可以表达 *and* 的语义学。(15) 中 $C$ 为全局语境；合取语义学的关键部分是：$S$2 的局部语境就是用 $S$1 更新全局语境的结果。于是，(14) 之所以没有预设，仅仅由于 *and* 的动态*semantics*（语义学）。而要解释 (16) 中预设的缺失，只需给出一个析取语义学：第二个析取支的局部语境已用第一个析取支的否定作了更新。Krahmer and Muskens 1996 提供了这样一种说明，还捕捉到（双重）否定与回指之间的交互。

为更具体起见，设语境是可能世界之集，用简单小句 $S$ 对 $C$ 的更新 $C[S]$ 为 $C\cap p$，其中 $p$ 是 $S$ 的命题内容：用小句更新 $C$，输出的就是 $C$ 中该小句为真的那些世界。(18) 中的规则展示了英语主要命题算子动态解释的一个海姆式片段。

- (17) ${C}[{\textrm{非 } S1}] = {C} \backslash {C}[{S1}]$ ${C}[{S1 \textrm{ 且 } S2}] = ({C}[{S1}])[{S2}]$ ${C}[{\textrm{若 }S1, \textrm{ 则 } S2}] = ({C}[{\textrm{非 }S1}]) \cup ({C}[{S1}])[{S2}]$ ${C}[{S1 \textrm{ 或 } S2}] = {C}[{S1}] \cup ({C}[{\textrm{非 }S1}])[{S2}]$

有人质疑这种动态解释的解释力：该框架无法说明，为什么表面上不存在任何自然语言表达来编码 (17) 的极小变体——比如第二个析取支 $S$2 的局部语境取 $C[S1]$ 而非 $C[\textrm{非 }S1]$；比如 $S$1 的局部语境基于用 $S$2 所作的更新；再比如干脆没有任何局部语境，如 (18)（例如参见 Soames 1989）[^soames-1989]。

- (18) ${C}[{S1 \textrm{ 或 } S2}] = {C}[{S1}] \cup {C}[{S2}]$

面对这类批评，预设投射的静态进路近来有所复兴：施伦克的语用进路（Schlenker 2008, 2009）、Chemla 的语用进路（2008，其他网络资源），以及 George（2008）与 Fox（2008）的语义（三值）进路。不过，正如 Rothschild 指出的，仍有一条路让沿 (17) 路线的语义学获得解释力：为此必须证明，联结词的可许动态解释共享某些性质。Rothschild（2011）证明，只要假设语境变化潜能遵循某些有定义性（*definedness*）原则，一个有解释力且经验上充分的预设动态处理便是可能的。设 $C[S]$（对简单小句 $S$）仅在 $S$ 的任何预设于 $C$ 中所有世界皆为真时有定义。(17) 中的规则决定复杂语句的有定义性条件：例如按 (17)，[not S] 在 $C$ 中无定义，仅当 $S$ 在 $C$ 中无定义。Rothschild 的洞见是：约束所得的有定义性条件，便可约束动态解释。

### 3.2 预设与动态认知逻辑

认知逻辑是模态逻辑的一个分支，研究“$i$ 知道”这一模态（比较认知逻辑、信念修正逻辑词条）。约在 2000 年前后，认知逻辑发生了动态转向，引入对状态变化的关注——不过此时状态被取作一组主体之知识的表征。

固定一组基本命题 $P$ 与一组主体 $I$，则 $P$ 与 $I$ 的一个知识状态包含：一个可能世界之集 $W$；一个赋值函数 $V$，给 $W$ 中每个 $w$ 指派 $P$ 的一个子集（若 $w \in W$，则 $V(w)$ 列出在 $w$ 中为真的基本命题）；以及对每个主体 $i \in I$ 的一个关系 $R_i$，陈述 $i$ 的认知相似性（若 $wR_i w'$，则主体 $i$ 无法把世界 $w$ 与世界 *w$'$* 区分开）。认知模型 $M = (W, V, \{R_i \mid i \in I\})$ 通称多模态克里普克模型；点式认知模型则是带有指定世界 $w_0$（代表现实世界）的认知模型。

给定认知状态 $(M, w_0) = ((W, V, \{ R_i \mid i \in I\}), w_0)$，公开宣告 $\phi$ 之后会发生什么？直观上，$M$ 的世界集 $W$ 被限制到 $\phi$ 成立的那些世界 $w \in W$，赋值函数 $V$ 与认知关系 $R_i$ 也相应受限。新模型记作 $M\mid\phi$。若 $\phi$ 在 $w_0$ 中为真，公共宣告 $\phi$ 的意义可看作从 $(M, w_0)$ 到 $(M\mid\phi , w_0)$ 的一个映射；若 $\phi$ 在 $w_0$ 中为假，则更新无从谈起。

Veltman 的更新逻辑可以在公共宣告逻辑（比较共同知识词条）中得到容纳：允许形如 $\Diamond \phi$ 的公共宣告，其模态读作“共同知识之下的可达性”。若一组主体的 $S$5 知识状态（比较认知逻辑词条）被公共宣告 $\Diamond \phi$ 更新，则当 $\phi$ 在模型中某处为真时，更新毫无改变（此时 $M\mid\Diamond \phi$ 等于 $M$）；否则更新便产生不一致——公共宣告被假定为真。这与更新逻辑的定义正相吻合。

带交际更新的认知逻辑，其逻辑工具箱名为动态认知逻辑（DEL）。DEL 起于对公共宣告之认知与信念效应的分析（Plaza 1989; Gerbrandy 1999）[^gerbrandy-1999][^plaza-1989]。公共宣告之所以引人注目，在于它创造共同知识。此外还有多种宣告——私人宣告、群组宣告、秘密共享、说谎等——同样具有明确界定的认知效应。Baltag et al. 1999 与 Baltag and Moss 2004 为一大类更新行动提出了一般框架；Benthem et al. 2006 进一步推广为完备的交际与变化逻辑，其丰富行动允许改变世界的事实；Ditmarsch et al. 2006 则给出了动态认知逻辑的教科书式处理。

在认知逻辑的设置下，带预设的言说之交际情境可如此表示。先在一个多主体信念（或知识）状态中，表示说话者对听众知识或信念的假设；再为交际行动对信念状态的影响建模。在动态认知逻辑中处理带预设的言说，一个简单办法是把预设 $P$ 建模为公共宣告“$P$ 是共同知识”。若 $P$ 确为共同知识，用该信息更新不改变任何东西；若 $P$ 不是共同知识，该言说便为假——公开宣告假命题，产生不一致的知识状态。

### 3.3. 预设之外

动态语义特别适合刻画不同类型的语言材料如何作用于信息状态的不同方面。尤其值得注意：动态语义能高效建模议题内容（*at-issue*）与非议题内容（*non-at issue*）之别——前者由陈述句的说出所断言，后者只起次要作用。例如，(19) 的议题内容是“约翰的邻居昨天被捕”：这是说话者意欲断言的消息；同位语 *who I have never met*（我从未见过他）则不在议题之内。一个观察角度是：对话者只有意在质疑“邻居被捕”这一事实时，才会以 *No! That's not true!*（不对！那不是真的！）回应 (19)；若只是想表达对说话者“从未见过邻居”之声称的怀疑，便不会如此。

- (19) John's neighbour, who I have never met, was arrested yesterday.（约翰的那位我从未谋面的邻居昨天被捕了。）

动态语义是分析此类句子解释过程的合适框架：它自然而然地允许对分离的信息流建模。例如，AnderBois et al. 2015 为 (19) 这类句子提供了一种说明：主句更新一个局部的可能世界集；更新后的集合可视为共同基础更新的潜在候选。相比之下，同位语直接更新共同基础——与其说它是*proposed*（提议性）的共同基础更新，不如说它是一次*imposed*（强加性）更新（另一种动态逻辑参见 Nouwen 2007）[^nouwen-2007]。AnderBois et al. 2015 的想法，部分得益于示证语（evidentials）领域类似思想的成功应用；特别参见 Murray 2014。

## 4. 在类型化逻辑中编码动态性

组合性始终是自然语言语义学使用逻辑系统的一大关切（参见组合性词条）。借助高阶逻辑（参见二阶与高阶逻辑、丘奇类型论词条），可以给出诸如自然语言量化系统的彻底组合性说明——经典蒙塔古语法即为示范（Montague 1974a,b, 1973；比较逻辑形式词条）[^montague-1974a]。本节评述动态进路如何扩展到高阶系统。动态语义与类型论之间的联系，更像一段情缘而非一桩稳定的婚姻：这一联系并无内在必要。此处之所以处理它，是为了说明蒙塔古语法对动态语义的历史影响。

蒙塔古语法的诸动态版本，多数发展的实为动态谓词逻辑（DPL）的高阶版本：Groenendijk and Stokhof 1990; Chierchia 1992, 1995; Muskens 1994, 1995, 1996; Eijck 1997; Eijck and Kamp 1997; Kohlhase et al. 1996; Kuschert 2000 皆属此类。这些系统都从 DPL 进路继承了一个特征（或者说缺陷）：重新指派是破坏性的。DRT 则无此问题——Kamp 1981 与 Kamp and Reyle 1993 的话语表现构造算法以有限定义域上的函数来陈述，并且细心地谈论“取一个新鲜的话语所指”来扩展验证函数的定义域，对每个待处理的新名词短语皆然。

在外延蒙塔古语法中，“a man”（一个男人）译作：

$$\lambda P\exists x(\textrm{man } x \wedge Px).$$

此处 $P$ 的类型为 $e \rightarrow t$，是 VP 槽位的变元：这里假定 VP 指称实体的集合。

在 Groenendijk and Stokhof 1990 的动态蒙塔古语法（DMG）中，不定 NP 的翻译引入一个回指索引（anaphoric index）。“a man” 译作

$$\lambda P\lambda a\lambda a' \cdot \exists x(\textrm{man }x \wedge Pu_i (u_i \mid x) aa').$$

外延蒙塔古语法的基本类型为 e 与 t；DMG 的基本类型则是 $e, t$ 与 $m (m$ 即标记 marker）。状态为标记挑出实体，故可视为类型 $m \rightarrow e$ 的对象。把 $m \rightarrow e$ 缩写为 $s$（即“状态” state），类型 $s \rightarrow s \rightarrow t$ 的对象便称为状态转移。“a man” 的 DMG 翻译中，变元 $P$ 的类型为 $m \rightarrow s \rightarrow s \rightarrow t$：VP 意义的类型由此从 $e \rightarrow t$ 提升到这一类型。注意 $\rightarrow$ 向右结合，故 $m \rightarrow s \rightarrow s \rightarrow t$ 是 $m \rightarrow(s \rightarrow(s \rightarrow t))$ 的简写。诚然，DMG 可以看作一次系统性替换的结果——实体换成标记，真值换成状态转移。“is happy”（快乐）的 VP 意义是一个把标记映到状态转移的函数：标记 $u_i$ 的状态转移检查输入状态是否把 $u_i$ 映到一个快乐的实体，并检查输出语境是否等于输入语境。变元 $a$、*a$'$* 遍历状态；表达式 $(u_i \mid x)a$ 表示把 $a$ 中 $u_i$ 的值重置为 $x$ 的结果——$u_i$ 的旧值就此销毁（破坏性指派）。指称标记 $u_i$ 上的回指索引 $i$ 由翻译引入；事实上，翻译正是从带索引的不定名词短语 “a man$_i$” 出发。蒙塔古式组合性与动态语义的联系，连同基本的蒙塔古要素与动态要素，在 Muskens 1991, 1995, 1996 提出的类型化变化逻辑（Logic of Change）中要透明流畅得多。正因如此，Muskens 的组合性 DRT 很可能已成为当前组合性动态语义研究的事实标准与出发点。另一种处理由增量类型逻辑（ITL）给出——它是类型化逻辑的“栈语义”扩展，基于无变元索引，避开破坏性指派问题。Vermeulen 1993 发展的 DPL 栈语义，基本想法是用栈式指派替换普通 DPL 的破坏性指派（后者在重置时丢弃旧值），让旧值得以重用：栈式指派给每个变元指派一个值栈，栈顶即当前值；存在量化把新值压入栈，也可弹出栈以重用先前指派的值。Eijck 2000 的 ITL 实为栈语义的类型化版本，用的是单个栈。

设定一个实体论域，语境便是实体的有限列表。若 $c$ 是长度为 $n$ 的语境，其元素记作 $c[0]$, $\ldots ,c[n-1]$，其长度记作 $\lvert c\rvert$。长度为 $i$ 的语境之类型记作 $[e]^i$。若 $c$ 属于 $[e]^i$，则 $\{0, \ldots ,i-1\}$ 型对象可充当 $c$ 的索引。若 $c \in[e]^i$ 且 $j \in \{0, \ldots ,i-1\}$，则 $c[j]$ 是语境中位置 $j$ 处那个类型为 e 的对象。语境上的一项关键操作是用元素作扩展：若 $c :: [e]^i$ 且 $x :: e$（$c$ 为长度 $i$ 的语境，$x$ 为实体），则 $c\mathbin{{}^{\wedge}} x$ 是长度 $i+1$ 的语境，元素为 $c$[0], $\ldots ,c[i-1], x$。于是 $\mathbin{{}^{\wedge}}$ 是类型为 $[e]^i \rightarrow e \rightarrow[e]^{i+1}$ 的算子。还要注意：像 $[e]^i$ 这样的类型实为多态类型，$i$ 起类型变元的作用。参见 Milner 1978。

ITL 中没有破坏性指派，不定名词短语在句法上也不携带索引。“a man” 的 ITL 翻译从语境拾取索引，如下所示：

$$\lambda P\lambda c\lambda c' \cdot \exists x (\textrm{man } x \mathbin{{}^{\wedge}} P\lvert c\rvert (c^x)c').$$

此处 $P$ 是类型为 $\{0, \ldots ,i\} \rightarrow[e]^{i+1} \rightarrow [e]^j \rightarrow t$ 的变元；$c$ 是类型 [$e]^i$ 的变元，代表长度 $i$ 的输入语境；$c'$ 是类型 [$e]^j$ 的变元，代表输出语境。注意：$P$ 的类型 $\{0, \ldots ,i\} \rightarrow [e]^{i+1} \rightarrow [e]^j \rightarrow t$ 表明，$P$ 先取范围 $\{0, \ldots ,i\}$ 内的一个索引，再取一个适配该范围的语境（长度 $i+1$），再取一个长度未知的语境，然后给出真值。$P$ 是一元谓词的类型，提升到语境改变者的层面，方式如下。提升谓词不用变元遍历对象来构造类型 $e$ 的表达式，而用变元遍历输入语境的尺寸，构造出一个指称该语境改变者的表达式。

“a man” 的 ITL 翻译具有类型 $$(\{0, \ldots ,i\} \rightarrow[e]^{i+1} \rightarrow [e]^j \rightarrow t) \rightarrow [e]^i \rightarrow [e]^j \rightarrow t.$$ 在 $P\lvert c\rvert (c\mathbin{{}^{\wedge}} x)c'$ 中，变元 $P$ 标记 VP 解释的槽位；$\lvert c\rvert$ 把输入语境的长度交给 $P$，拾取值 $i$——语境扩展时下一个可用槽位的位置。该槽位由一个指称男人的对象 $x$ 填充。注意 $c\mathbin{{}^{\wedge}} x[\lvert c\rvert ] = c\mathbin{{}^{\wedge}} x[i] = x$：索引 $i$ 正是从语境中挑出该男人的凭据。

要说明动态高阶系统可在 ITL 中表达，只需展示相应动态算子如何定义。设 $\phi$ 与 $\psi$ 的类型为语境转移，即 [$e] \rightarrow[e] \rightarrow t$（以 [$e$] 表示任意语境），$c, c', c''$ 的类型为 [$e$]。则动态存在量词、动态否定与动态复合可定义如下：

$$ \begin{align*} \cal{E} & := \lambda cc'\cdot \exists x(c \mathbin{{}^{\wedge}} x = c') \\ {\sim}\phi & := \lambda cc'\cdot (c = c' \mathbin{{}^{\wedge}} \neg \exists c'' \phi cc'') \\ \phi ; \psi & := \lambda cc'\cdot \exists c''(\phi cc'' \mathbin{{}^{\wedge}} \psi cc') \end{align*} $$

动态蕴涵 $\Rightarrow$ 依常法由 ${\sim}(\phi; {\sim}\psi)$ 定义。

ITL 与 Muskens 式组合性 DRT 并非不能兼容；例如参见 Bittner 2014。本节以一条评论作结：融合蒙塔古式组合性与动态语义的系统，其版图远未测绘完毕。近来一系列融合基于连续（continuation-based）与动态语义的贡献，正在探索整合与推广二者的新途径；参见 de Groote 2006, Bumford and Barker 2013, Charlow 2014, Bumford 2015, and Martin 2016。

## 5. 结语

希望以上文字能让读者体会到：动态语义是处理意义与信息的一条成果丰硕、灵活自如的进路。它自带一套灵活工具，还有一批“杀手级应用”——驴子句的组合性处理、回指关联之说明、预设投射之说明、认知更新之说明，以及不同（非议题）更新种类间的细粒度区分。动态语义是形式语义学中极为活跃的子领域；以动态进路处理的现象，其跨语言范围正以越来越快的速度扩展。

## References（引用注释）

**以下文献从原文照录，不作翻译；中国文献译为中文。**

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

[^anderbois-2015]: AnderBois, Scott, Adrian Brasoveanu, and Robert Henderson, 2015, “At-issue Proposals and Appositive Impositions in Discourse”, *Journal of Semantics*, 32: 93–138. doi:10.1093/jos/fft014
[^aloni-1997]: Aloni, Maria, 1997, “Quantification in Dynamic Semantics”, in *Proceedings of the Eleventh Amsterdam Colloquium*, P. Dekker (ed.), 73–78.
[^baltag-2004]: Baltag, Alexandru and Lawrence S. Moss, 2004, “Logics for Epistemic Programs”, *Synthese*, 139(2): 165–224. doi:10.1023/B:SYNT.0000024912.56773.5e
[^baltag-1999]: Baltag, Alexandru, Lawrence S. Moss, and Slawomir Solecki, 1999, “The Logic of Public Announcements, Common Knowledge, and Private Suspicions”, Technical Report SEN-R9922, CWI, Amsterdam. [[Baltag et al. 1999 available online](http://www.cs.indiana.edu/cgi-bin/techreports/TRNNN.cgi?trnum=TR534)]
[^barker-2002]: Barker, Chris, 2002, “The Dynamics of Vagueness”, *Linguistics and Philosophy*, 25(1): 1–36.
[^barker-2008]: Barker, Chris and Chung-chieh Shan, 2008, “Donkey Anaphora is In-scope Binding”, *Semantics and Pragmatics*, 1: 1–46. doi:10.3765/sp.1.1
[^beaver-1997]: Beaver, David, 1997, “Presupposition”, in van Benthem and ter Meulen 1997: 939–1008.
[^beaver-2001]: –––, 2001, *Presupposition and Assertion in Dynamic Semantics*, Stanford: CSLI Publications.
[^benthem-1989]: Benthem, Johan van, 1989, “Semantic Parallels in Natural Language and Computation”, in *Logic Colloquium, Granada, 1987*, Heinz-Dieter Ebbinghaus et al. (eds.), Amsterdam: Elsevier, 331–375.
[^benthem-1996]: –––, 1996, *Exploring Logical Dynamics*, Stanford: CSLI & Folli.
[^benthem-1997]: Benthem, Johan van and Alice ter Meulen (eds.), 1997, *Handbook of Logic and Language*, Amsterdam: Elsevier.
[^benthem-2006]: Benthem, Johan van, Jan van Eijck, and Barteld Kooi, 2006, “Logics of Communication and Change”, *Information and Computation*, 204(11): 1620–1662. doi:10.1016/j.ic.2006.04.006
[^berg-1996]: van den Berg, Martin H., 1996, *The Internal Structure of Discourse*, Ph.D. Thesis, ILLC Dissertation Series 1996–3, Amsterdam: ILLC Publications.
[^bittner-2014]: Bittner, Maria, 2014, *Temporality: Universals and Variation*, Hoboken, NJ: Wiley-Blackwell.
[^brasoveanu-2007]: Brasoveanu, Adrian, 2007, *Structured Nominal and Modal reference*, Ph.D. Thesis, Rutgers University.
[^brasoveanu-2008]: –––, 2008, “Donkey Pluralities: Plural Information States Versus Non-Atomic Individuals”, *Linguistics and Philosophy*, 31 (2): 129–209. doi:10.1007/s10988-008-9035-0
[^brasoveanu-2013]: –––, 2013, “The Grammar of Quantification and the Fine Structure of Interpretation Contexts”, *Synthese*, 190(15): 3001–3051. doi:10.1007/s11229-012-0118-7
[^bumford-2015]: Bumford, Dylan, 2015, “Incremental Quantification and the Dynamics of Pair-list Phenomena”, *Semantics and Pragmatics*, 8(9): 1–70. doi:10.3765/sp.8.9
[^bumford-2013]: Bumford, Dylan and Chris Barker, 2013, “Association with Distributivity and the Problem of Multiple Antecedents for Singular Different”, in *Linguistics and Philosophy*, 36(5): 355–369. doi:10.1007/s10988-013-9139-z
[^charlow-2014]: Charlow, Simon, 2014, *On the Semantics of Exceptional Scope*, Ph.D. Thesis, New York University.
[^chierchia-1992]: Chierchia, Gennaro, 1992, “Anaphora and Dynamic Binding”, *Linguistics and Philosophy*, 15(2): 111–183. [[Chierchia 1992 available online](http://scholar.harvard.edu/chierchia/publications/anaphora-and-dynamic-binding)]
[^chierchia-1995]: –––, 1995, *Dynamics of Meaning: Anaphora, Presupposition, and the Theory of Grammar*, Chicago: University of Chicago Press.
[^dekker-1993]: Dekker, Paul Jacques Edgar, 1993, *Transsentential Meditations, ups and downs in dynamic semantics*, Ph.D. Thesis, University of Amsterdam, ILLC. [[Dekker 1993 available online](http://hdl.handle.net/11245/1.392554)]
[^ditmarsch-2006]: Ditmarsch, Hans van, Wiebe van der Hoek, and Barteld Kooi, 2006, *Dynamic Epistemic Logic* (Synthese Library: Volume 337), Dordrecht: Springer.
[^eijck-1994]: Eijck, Jan van, 1994, “Presupposition Failure—a Comedy of Errors”, *Formal Aspects of Computing*, 6(supplement 1): 766–787. doi:10.1007/BF01213602
[^eijck-1997]: –––, 1997, “Typed Logics with States”, *Logic Journal of the IGPL*, 5(5): 623–645. doi:10.1093/jigpal/5.5.623
[^eijck-2000]: –––, 2000, “On the Proper Treatment of Context in NL”, in *Computational Linguistics in the Netherlands 1999; Selected Papers from the Tenth CLIN Meeting*, Paola Monachesi (ed.), Utrecht Institute of Linguistics OTS, 41–51.
[^eijck-1992]: Eijck, Jan van and Fer-Jan de Vries, 1992, “Dynamic Interpretation and Hoare Deduction”, *Journal of Logic, Language, and Information*, (1)1: 1–44. doi:10.1007/BF00203385
[^eijck-1997-2]: Eijck, Jan van and Hans Kamp, 1997, “Representing Discourse in Context”, in van Benthem and ter Meulen 1997: 179–237.
[^elbourne-2001]: Elbourne, Paul, 2001, “E-Type Anaphora as NP-Deletion”, *Natural Language Semantics*, 9(3): 241–288. doi:10.1023/A:1014290323028
[^elbourne-2005]: –––, 2005, *Situations and Individuals*, Cambridge, MA: MIT Press.
[^evans-1977]: Evans, Gareth, 1977, “Pronouns, Quantifiers and Relative Clauses (I)”, *Canadian Journal of Philosophy*, 7(3): 467–536.
[^evans-1980]: –––, 1980, “Pronouns”, *Linguistic Inquiry*, 11(2): 337–362.
[^fox-2008]: Fox, Danny, 2008, “Two Short Notes on Schlenker’s theory of Presupposition Projection”, *Theoretical Linguistics*, 34(3): 237–252. doi:10.1515/THLI.2008.016
[^geach-1962]: Geach, Peter Thomas, 1962 [1980], *Reference and Generality: An Examination of Some Medieval and Modern Theories*, Ithaca, NY: Cornell University Press. Third revised edition: 1980.
[^george-2008]: George, Benjamin Ross, 2008, *Presupposition Repairs: a Static, Trivalent Approach to Predicting Projection*, M.A. Thesis, UCLA.
[^gerbrandy-1999]: Gerbrandy, Jelle, 1999, “Dynamic Epistemic Logic”, in *Logic, Language and Computation, Vol. 2*, Lawrence S. Moss, Jonathan Ginzburg, and Maarten de Rijke (eds.), Stanford: CSLI Publications.
[^groenendijk-1990]: Groenendijk, Jeroen and Martin Stokhof, 1990, “Dynamic Montague Grammar”, in *Papers from the Second Symposium on Logic and Language*, L. Kalman and L. Polos (eds.), Budapest: Akademiai Kiadoo, 3–48.
[^groenendijk-1991a]: –––, 1991a, “Dynamic Predicate logic”, *Linguistics and Philosophy*, 14(1): 39–100. doi:10.1007/BF00628304
[^groenendijk-1991b]: –––, 1991b, “Two Theories of Dynamic Semantics”, in *JELIA ‘90, European Workshop on Logics in AI* (Lecture Notes in Computer Science: Volume 478), Jan van Eijck (ed.), Berlin: Springer, 55–64. doi:10.1007/BFb0018433
[^groenendijk-1996]: Groenendijk, Jeroen, Martin Stokhof, and Frank Veltman, 1996, “Coreference and Modality”, in *Handbook of Contemporary Semantic Theory*, Shalom Lappin (ed.), Oxford: Blackwell, 179–213.
[^groeneveld-1995]: Groeneveld, Willem, 1995, *Logical Investigations into Dynamic Semantics*, Ph.D. Thesis, University of Amsterdam.
[^groote-2006]: de Groote, Philippe, 2006, “Towards a Montagovian Account of Dynamics”, in *Proceedings of Semantics and Linguistic Theory (SALT) 16*, Masayuki Gibson and Jonathan Howell (eds.), 1–16. doi:10.3765/salt.v16i0.2952
[^heim-1983a]: Heim, Irene, 1983a, “File Change Semantics and the Familiarity Theory of Definiteness”, in *Meaning, Use and Interpretation of Language*, Rainer Bäuerle, Christoph Schwarze, and Arnim von Stechow (eds.), Berlin: De Gruyter, 164–189.
[^heim-1983b]: –––, 1983b, “On the Projection Problem for Presuppositions”, *Proceedings of the Second West Coast Conference on Formal Linguistics*, Michael Barlow, Dan P. Flickinger and MIchael T. Wescoat (eds.), Stanford, CA: Stanford University Department of Lingustics, 114–126.
[^heim-1990]: –––, 1990, “E-Type Pronouns and Donkey Anaphora”, *Linguistics and Philosophy*, 13(2): 137–138.
[^hollenberg-1996]: Hollenberg, Marco and Kees Vermeulen, 1996, “Counting Variables in a Dynamic Setting”, *Journal of Logic and Computation*, 6(5): 725–744. doi:10.1093/logcom/6.5.725
[^kamp-1981]: Kamp, Hans, 1981, “A Theory of Truth and Semantic Representation”, in *Formal Methods in the Study of Language*, Jeroen Groenendijk, Theo Janssen, and Martin Stokhof (eds.), Amsterdam: Mathematisch Centrum, 277–322.
[^kamp-1993]: Kamp, Hans and Uwe Reyle, 1993, *From Discourse to Logic*, Dordrecht: Kluwer.
[^karttunen-1973]: Karttunen, Lauri, 1973, “Presuppositions of Compound Sentences”, *Linguistic Inquiry*, 4(2): 169–193.
[^karttunen-1974]: –––, 1974, “Presupposition and Linguistic Context”, *Theoretical Linguistics*, 1: 181–194.
[^kohlhase-1996]: Kohlhase, Michael, Susanna Kuschert, and Manfred Pinkal, 1996, “A Type-Theoretic Semantics for $\lambda$-DRT”, in *Proceedings of the Tenth Amsterdam Colloquium*, Paul Dekker and Martin Stokhof (eds.), Amsterdam: ILLC Publications.
[^krahmer-1995]: Krahmer, Emiel, 1995, *Discourse and Presupposition*, Ph.D. Thesis, Tilburg University; revised and published under the title *Presupposition and Anaphora*, Stanford: CSLI Publications, 1998.
[^krahmer-1996]: Krahmer, Emiel and Reinhard Muskens, 1996, “Negation and Disjunction in Discourse Representation Theory” *Journal of Semantics*, 12: 357–376. doi: 10.1093/jos/12.4.357
[^krifka-1996]: Krifka, Manfred, 1996, “Parametrized Sum Individuals for Plural Reference and Partitive Quantification” *Linguistics and Philosophy*, 19: 555–598. [[Krifka 1996 available online (pdf)](http://amor.cms.hu-berlin.de/~h2816i3x/Publications/Krifka%201996%20Plural%20Anaphora.PDF)]
[^kuschert-2000]: Kuschert, Susanna, 2000, *Dynamic Meaning and Accommodation*, Ph.D. Thesis, Universität des Saarlandes.
[^martin-2016]: Martin, Scott, 2016, “Supplemental Update”, *Semantics and Pragmatics*, 9(5). doi:10.3765/sp.9.5
[^milner-1978]: Milner, Robin, 1978, “A Theory of Type Polymorphism in Programming”, *Journal of Computer and System Sciences*, 17: 348–375.
[^montague-1973]: Montague, Richard, 1973, “The Proper Treatment of Quantification in Ordinary English”, in *Approaches to Natural Language*, Jaakko Hintikka, Julius Moravcsik, and Patrick Suppes (eds.), Dordrecht: Reidel, 221–242.
[^montague-1974a]: –––, 1974a, “English as a Formal Language”, in Montague 1974c: 188–221.
[^montague-1974b]: –––, 1974b, “Universal Grammar”, in Montague 1974c: 222–246.
[^montague-1974c]: –––, 1974c, *Formal Philosophy; Selected Papers of Richard Montague*, R.H. Thomason (ed.), New Haven and London: Yale University Press.
[^murray-2014]: Murray, Sarah E., 2014, “Varieties of Update”, *Semantics and Pragmatics*, 7: 1–53. doi:10.3765/sp.7.2
[^muskens-1991]: Muskens, Reinhard, 1991, “Anaphora and the Logic of Change”, in *JELIA ‘90, European Workshop on Logics in AI* (Lecture Notes in Computer Science: Volume 478), Jan van Eijck (ed.), Berlin and New York, 414–430. doi:10.1007/BFb0018456
[^muskens-1994]: –––, 1994, “A Compositional Discourse Representation Theory”, in *Proceedings 9ᵗʰ Amsterdam Colloquium*, Paul Dekker and Martin Stokhof (eds.), Amsterdam: ILLC Publications, 467–486.
[^muskens-1995]: –––, 1995, “Tense and the Logic of Change”, in *Lexical Knowledge in the Organization of Language*, U. Egli et al. (ed.), Amsterdam: John Benjamins, 147–183.
[^muskens-1996]: –––, 1996, “Combining Montague Semantics and Discourse Representation”, *Linguistics and Philosophy*, 19: 143–186.
[^muskens-1997]: Muskens, Reinhard, Johan van Benthem, and Albert Visser, 1997, “Dynamics”, in van Benthem and ter Meulen 1997: 587–648.
[^nouwen-2003]: Nouwen, Rick, 2003, “Complement Anaphora and Interpretation”, *Journal of Semantics*, 20: 73–113.
[^nouwen-2007]: –––, 2007, “On Dependent Pronouns and Dynamic Semantics”, *Journal of Philosophical Logic*, 36(2): 123–154.
[^nouwen-nd]: –––, forthcoming, “E-type Pronouns: Congressmen, Sheep and Paychecks”, in L. Matthewson, C. Meier, H. Rullmann, and T.E. Zimmerman (eds.), *The Blackwell Companion to Semantics*, Oxford: Wiley.
[^plaza-1989]: Plaza, Jan A., 1989, “Logics of Public Communications”, in *Proceedings of the 4ᵗʰ International Symposium on Methodologies for Intelligent Systems*, M.L. Emrich, M.S. Pfeifer, M. Hadzikadic, and Z.W. Ras (eds.), Amsterdam: North Holland, 201–216.
[^putnam-1975]: Putnam, Hilary, 1975, “The Meaning of ‘Meaning’”, in *Philosophical Papers* (Volume 2), Cambridge: Cambridge University Press.
[^quine-1960]: Quine, Willard van Orman, 1960, *Word and Object*, Cambridge, MA: MIT Press.
[^roberts-1987]: Roberts, Craige, 1987, *Modal Subordination, Anaphora and Distributivity*, Ph.D. Thesis, University of Massachusetts/Amherst; New York: Garland, 1990.
[^roberts-1989]: –––, 1989, “Modal Subordination and Pronominal Anaphora in Discourse”, *Linguistics and Philosophy*, 12: 683–721.
[^rothschild-2011]: Rothschild, Daniel, 2011, “Explaining Presupposition Projection with Dynamic Semantics”, *Semantics and Pragmatics*, 4(3): 1“43.
[^sandt-1992]: Sandt, Rob A. van der, 1992, “Presupposition Projection as Anaphora Resolution”, *Journal of Semantics* (Special Issue: Presupposition, Part 2), 9: 333–377. doi:10.1093/jos/9.4.333
[^schlenker-2007]: Schlenker, Philippe, 2007, “Anti-dynamics: Presupposition Projection without Dynamic Semantics”, *Journal of Logic, Language and Information*, 16(3): 325–356.
[^schlenker-2008]: –––, 2008, “Be Articulate: A Pragmatic Theory of Presupposition Projection”, *Theoretical Linguistics*, 34(3): 157–212.
[^schlenker-2009]: –––, 2009, “Local Contexts”, *Semantics and Pragmatics*, 2(3): 1–78.
[^seuren-1985]: Seuren, Pieter, 1985, *Discourse Semantics*, Oxford: Blackwell.
[^soames-1989]: Soames, Scott, 1989, “Presuppositions”, in Dov M. Gabbay & Franz Guenther (eds.), *Handbook of Philosophical Logic*, vol. IV, 553–616. Dordrecht. doi:10.1007/978-94-009-1171-0_9
[^stalnaker-1972]: Stalnaker, Robert C., 1972, “Pragmatics”, in *Semantics of Natural Language*, Donald Davidson and Gilbert Harman (eds.), Dordrecht: Reidel, 380–397. doi:10.1007/978-94-010-2557-7_11
[^stalnaker-1973]: –––, 1973, “Presuppositions”, *Journal of Philosophical Logic*, 2: 447–457.
[^stalnaker-1974]: –––, 1974, “Pragmatic Presuppositions”, in *Semantics and Philosophy*, Milton K. Munitz and Peter K. Unger (eds.), New York: New York University Press, 197–213.
[^veltman-1991]: Veltman, Frank, 1991, “Defaults in Update Semantics”, in *Conditionals, Defaults and Belief Revision*, Hans Kamp (ed.), Edinburgh: Dyana Deliverable R2.5A.
[^veltman-1996]: –––, 1996, “Defaults in Update Semantics”, *Journal of Philosophical Logic*, 25: 221–261.
[^vermeulen-1993]: Vermeulen, C.F.M., 1993, “Sequence Semantics for Dynamic Predicate Logic”, *Journal of Logic, Language and Information*, 2: 217–254. doi:10.1007/BF01050788
[^vermeulen-1994]: –––, 1994, *Explorations of the Dynamic Environment*, Ph.D. thesis, Utrecht University.
[^vermeulen-1995]: –––, 1995, “Merging without Mystery, Variables in Dynamic Semantics”, *Journal of Philosophical Logic*, 24: 405–450.
[^werth-2000]: Werth, Paul, 2000, *Text Worlds: Representing Conceptual Space in Discourse*, London: Pearson Education/Longman.
[^zeevat-1989]: Zeevat, Hank, 1989, “A Compositional Approach to Discourse Representation Theory”, *Linguistics and Philosophy*, 12(1): 95–131. doi:10.1007/BF00627399

## 学术工具

* [如何引用本词条](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=dynamic-semantics)。
* [预览本词条的 PDF 版本](https://leibniz.stanford.edu/friends/preview/dynamic-semantics/)，见 [SEP 学会之友](https://leibniz.stanford.edu/friends/)。
* 在 [InPhO](https://www.inphoproject.org/entity?sep=dynamic-semantics&redirect=True) 查找与本词条相关的话题与思想家。
* 在 [PhilPapers](https://philpapers.org/sep/dynamic-semantics/) 查看本词条的增强文献目录及其数据库链接。

## 其他网络资源

- Chemla, Emmanuel, 2008, “[Similarity: Towards a Unified Account of Scalar Implicatures, Free Choice Permission and Presupposition Projection](http://semanticsarchive.net/Archive/WI1ZTU3N/Chemla-SIandPres.html),” unpublished manuscript, Ecole Normale Superieur.（Emmanuel Chemla：《相似性：对标量含义推理、自由选择许可与预设投射的统一说明》，未刊稿，巴黎高等师范学院。）
- Parsons, Terence, 1978, “[Pronouns as Paraphrases](http://www.philosophy.ucla.edu/people/faculty/tparsons/Pronouns%20as%20Paraphrases/Pronouns%20as%20Paraphrases.pdf),”, unpublished manuscript, University of Massachusetts/Amherst.（Terence Parsons：《代词作释义》，未刊稿，马萨诸塞大学阿默斯特分校。）

## 相关词条

回指 | 断言 | 共同知识 | 组合性 | 直陈条件 | 认识语境论 | 话语表征理论 | 心灵外在主义 | 含义 | 指代词 | 语义概念的信息 | 经典逻辑 | 条件逻辑 | 认知逻辑 | 信念修正的逻辑 | 二阶逻辑与高阶逻辑 | 逻辑形式 | 狭义心理内容 | 心灵计算理论 | 一阶模型论 | 语用学 | 指称 | 科学实在论 | 言语行为 | 塔尔斯基的真理定义 | 丘奇类型论

**（译注：相关词条的中文站内链接将由管线在对应词条重译完成后统一挂接。）**
