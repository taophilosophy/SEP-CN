# 动态语义 dynamic semantics (Rick Nouwen, Adrian Brasoveanu, Jan van Eijck, and Albert Visser)

*首次发表于 2010 年 8 月 23 日；2016 年 7 月 12 日实质修订。*

动态语义是自然语言语义学的一种视角，强调信息随时间的增长。作为一种意义表示进路，它把文本或话语的片段看作指令：用新信息更新既有语境，得到的结果就是更新后的语境。用一句口号概括：意义即语境变化潜能。

需要注意的是这一视角的抽象性，以防各种不当推论。其一，人们容易以为动态语义或更新语义至少部分地承诺了内在主义的意义观，因为信息状态是「内在的」——即完全包含在个体的心智/大脑之中。换言之，人们可能认为动态语义的信息状态就是普特南（Putnam 1975）所说的「方法论唯我论意义上的状态」（参见科学实在论、心灵的计算理论、关于心理内容的外在主义、狭义心理内容各词条）。然而，这一一般框架并未说明状态究竟是什么。状态完全可以包含解释者所处的环境，从而带有一个「外在」成分。

第二种可能的误解是：动态语义或更新语义与古典真值条件语义学截然对立（参「古典逻辑」「一阶模型论」词条）。事实上，本词条稍后会说明，动态语义给出的是真值条件语义学的一种推广，而非彻底不同的替代方案：古典意义成为话语行动取得成功的*preconditions*（前提条件）。动态语义学家主张，*compositional meanings*（组合性意义）具有函数或关系的本性；古典意义则可以作为向「输入」坐标的*projections*（投影），从关系性动态意义中恢复出来。

采用抽象框架的目的并不在于给出经验预测——那是框架内各项具体实现的任务。动态语义框架 (i) 提供一种思考方向，(ii) 使我们得以引入关于该框架的数学研究中的方法。由此可知，「自然语言意义是否在本质上动态」这个问题没有经验答案。不过仍可以说：把解释作为线性有序过程来研究，已被证明颇有成效。

动态语义关注发送者与接收者的话语行动，因此在一定意义上接近哲学中以使用为导向的意义进路，如维特根斯坦与达米特的工作。但不宜把二者轻易等同：作为抽象框架，动态语义与许多看待意义与解释的哲学方式相容，它旨在对意义与解释进行*建模*。做这种建模，并不需要回答更宽泛的哲学问题，比如究竟是什么使主体得以与这些意义发生关联。例如在动态谓词逻辑中，我们把「马」的意义视为既定，并不对主体拥有「马」这一概念意味着什么作出实质断言，只是规定主体拥有它。这并非说这类问题（它们居于维特根斯坦与达米特工作的中心）最终不必回答，而只是说：一个模型即便不回答它们，也可以有价值。（动态语义力图给出系统而组合性的意义说明，这使它在精神上明显不同于维特根斯坦后期哲学。）

动态语义的第一种进路是*话语表现理论*（discourse representation theory，DRT；Kamp 1981）[^kamp-1981]。与坎普的进路密切相关的是艾琳·海姆的*文件变化语义学*（file change semantics，FCS；Heim 1983a）[^heim-1983a]，以及 Seuren 1985 的话语语义学。DRT 中的意义是所谓*话语表现结构*（discourse representation structures，DRSs）：这类结构是一种数据库，含特定的信息片段。DRS 本身是静态对象，但 DRT 仍可称为动态语义框架——因为它使我们能把组合意义的过程理解为*合并*话语表现结构的过程，信息变化由此成为解释过程的组成部分。

本词条的主要焦点是第二种进路，途中也会与 DRT 比较。在这一进路中，动态意义是行动的类型——由其所造成的变化来个体化。这是与*动态谓词逻辑*（dynamic predicate logic，DPL；Groenendijk and Stokhof 1991a）[^groenendijk-1991a] 相联系的进路。按这一传统，意义是对接收者信息状态将如何被修改的说明：它可以是一个函数，把旧信息状态映射为用该意义所含信息*更新*过的状态；也可以是一个关系，表达该意义所造成的那种信息变化。（早期工作见 Groenendijk and Stokhof 1991a,b；Muskens 1991；Dekker 1993；Vermeulen 1993；van Eijck 1994；Vermeulen 1994；Krahmer 1995；van den Berg 1996；Groenendijk et al. 1996；Aloni 1997；Muskens et al. 1997）[^aloni-1997][^berg-1996][^dekker-1993][^eijck-1994][^groenendijk-1991a][^groenendijk-1996][^krahmer-1995][^muskens-1991][^muskens-1997][^vermeulen-1993][^vermeulen-1994]

## 1. 作为过程的解释

陈述句的解释可以看作产物，也可以看作过程。产物视角聚焦于给定情境中的真；过程视角则把命题的解释视为一个信息更新步骤——以新的、更准确的知识状态取代原有的知识状态。动态语义关注的正是作为过程的解释。

### 1.1 更新语义学

更新语义是落实「解释即过程」这一想法的一种具体方式。其核心想法很简单：我们设定一个听者/接收者的简单模型，他按顺序接收信息项。听者在每一时刻都处于某个状态，拥有某些信息；这一状态被进来的信息以系统的方式修改。于是我们把所接收信息项的意义分析为它们对接收者信息状态变化的贡献——意义由此被视为行动，更准确地说，是*行动类型*：不是把某个给定状态变成另一状态的具体变化，而是这类具体变化所共有者。

### 1.2 作为更新逻辑的命题逻辑

命题逻辑（关于否定、析取与合取的逻辑）可以看作一种更新逻辑，方式如下。设有三个基本命题 $p, q$ 与 $r$，我们对它们的真值一无所知，于是共有八种可能：$\{ \bar{p} \bar{q} \bar{r}, p \bar{q} \bar{r}, \bar{p} q \bar{r}, \bar{p} \bar{q} r, pq \bar{r}, p \bar{q} r, \bar{p} qr, pqr \}$。其中 $\bar{p} \bar{q} \bar{r}$ 读作「$p, q, r$ 皆不真」，$p \bar{q} \bar{r}$ 读作「$p$ 真而 $q$ 与 $r$ 假」，依此类推。若此时宣告 $\neg p$（「并非 $p$」），其中四种可能随之消失，剩下 $\{\bar{p} \bar{q} \bar{r}, \bar{p} q \bar{r}, \bar{p} \bar{q} r, \bar{p} qr\}$。若接着宣告 $q \vee \neg r$（「$q$ 或非 $r$」），可能 $\bar{p} \bar{q} r$ 被排除，剩下 $\{ \bar{p} \bar{q} \bar{r}, \bar{p} q \bar{r}, \bar{p} qr \}$。如此继续。我们可以把 $\neg p$、$q \vee \neg r$ 这类命题的意义，看作从可能集合到其子集的映射。

可能集合表示知识状态。上例中，$\{ \bar{p} \bar{q} \bar{r}, p \bar{q} \bar{r}, \bar{p} q \bar{r}, \bar{p} \bar{q} r, pq \bar{r}, p \bar{q} r, \bar{p} qr, pqr \}$ 表示对命题 $p, q, r$ 完全无知的状态；像 $\{ pq \bar{r} \}$ 这样的单元素集合表示对这些命题的完全知识状态；空集 $\varnothing$ 则表示处理关于 $p, q$ 与 $r$ 的不相容陈述后所得的不一致状态。下面列出本命题语言各陈述的动态意义：

- *原子陈述*：即 $p, q, r$。相应的更新行动，是从当前语境中选出该字母未被划掉（未加上划线）的那些可能。
- *否定陈述*：形式为 $\neg \phi$。相应的更新行动，是从当前语境中选出构成 $\phi$ 陈述所选可能集合之补集的那些可能。
- *合取陈述*：形式为 $\phi \wedge \psi$。相应的更新行动，是从当前语境中选出构成 $\phi$ 与 $\psi$ 陈述从当前语境所作选择之交集的那些可能。
- *析取陈述*：形式为 $\phi \vee \psi$。相应的更新行动，是从当前语境中选出构成 $\phi$ 与 $\psi$ 陈述所作选择之并集的那些可能。

由此，命题联结词的意义就是从表示知识状态的旧语境到新语境的运算，而新语境表示处理相应命题信息后所得的知识状态。

### 1.3 程序语句及其执行

把更新语义中的行动与程序语句及其执行作比较，颇有启发，因为它第一次显示出量化在动态环境中如何运作。命令式语言的程序语句是在机器状态的语境中被解释（「执行」）的，而机器状态可以看作给各寄存器赋值。设寄存器以变量 $x, y, z$ 命名，内容为自然数，则下面是一个机器状态：

$$ \begin{array}{|c|c|}\hline x & 12 \\\hline y & 117 \\\hline z & 3 \\\hline \end{array} $$

若在该状态中执行语句 $z := x$，也就是对它作「解释」（C 语法中该语句写起来更简单：$z = x$），所得是一个新的机器状态：

$$ \begin{array}{|c|c|}\hline x & 12 \\\hline y & 117 \\\hline z & 12 \\\hline \end{array} $$

若在此状态中执行语句序列 $x := y$；$y := z$，则结果为：

$$ \begin{array}{|c|c|}\hline x & 117 \\\hline y & 12 \\\hline z & 12 \\\hline \end{array} $$

这说明，序列 $z := x$；$x := y$；$y := z$ 的结果是 $x$ 与 $y$ 的值被交换，附带的效果是 $z$ 的旧值丢失。换言之，程序 $z := x$；$x := y$；$y := z$ 的意义可以看作从输入机器状态 $s$ 到输出机器状态 $s'$ 的映射：该输出状态在若干方面不同于 $s$——$s'(x) = s(y)$ 且 $s'(y) = s(x)$（即 $x$ 与 $y$ 在输入时的值在输出状态中被交换），而 $s'(z) = s'(y)$。

现在考虑存在量词「存在一个 $x$，使得 $A$」。若把这一量词加入命令式编程语言，它的意义会是什么？它会是一条指令：用一个具有性质 $A$ 的新值取代 $x$ 的旧值。这可分解为「存在 $x$」与检验「$A$」两部分。所谓*检验*，是一种更新：它逐个取出输入语境中的状态，检验其是否满足某一条件，满足者纳入输出语境，不满足者弃去——故检验的输出语境总是输入语境的子集。上文「作为更新逻辑的命题逻辑」一节中，命题逻辑的全部公式都是检验。

两部分「存在 $x$」与检验「$A$」由顺序合成连接：「$\exists x$；$A$」。其中「$\exists x$」的自然意义，会是一条用任意新值取代 $x$ 旧值的指令。它同样是输入状态与输出状态之间的关系，但与 $x := y$ 这类确定赋值不同：这个关系不是函数。量词的这种关系性意义，正出现在众所周知的一阶逻辑塔尔斯基式真定义中（参「塔尔斯基的真定义」词条）：

> $\exists x\phi$ 在模型 $M$ 中相对于变量赋值 $\alpha$ 为真，当且仅当存在某个变量赋值 $\beta$：$\beta$ 与 $\alpha$ 至多在对 $x$ 的赋值上不同，且 $\phi$ 在 $M$ 中相对于赋值 $\beta$ 为真。

塔尔斯基定义中隐含着一个关系：它在赋值 $\alpha$ 与赋值 $\beta$ 之间成立，当且仅当对所有不同于 $x$ 的变量 $y$ 都有 $\alpha(y) = \beta(y)$。这一关系常被称为*对 x 的随机重置*，写作 [$x$]。对任意变量 $x$，完全赋值之间的二元关系 [$x$] 是赋值之间的等价关系，即自反、对称、传递的二元关系。下文将看到这类关系如何在一阶谓词逻辑的动态化版本中发挥作用。

若采用 [$x$] 作为「$\exists x$」的意义，则要注意其意义在本性上与检验大不相同：它在输出语境中创造新值。相反，以检验作更新所得的输出语境总是输入语境的子集，因而相对于输入语境绝不可能含有任何新东西。

### 1.4 动态语义中的语境概念

信息状态常被称为*语境*，因为状态是「解释」——即对形式语言或自然语言表达式作语义评价——的前提条件。「语境」一词也表明，我们关心的不是接收者的总体状态，而只是其中与所关注表达式/信息项的解释相关的方面。因此，在动态传统中，意义常被称为*语境变化潜能*。

尽管宽泛地说，动态语义中意义所带来的变化确实涉及*语境*的各方面，但语义学家谈语境时可以意指很不同的东西（参「认知语境主义」「索引词」词条），而这些不同看法催生了处理不同问题的各种动态语义变体。相关问题包括：为代词回指构造适当的机制（参「回指」「指称」词条）；解释条件句的语义（参「条件句」「条件句逻辑」词条）；对断言与预设的区分给出语义处理（参「断言」「言语行为」「含义」「语用学」词条）；发展「预设投射」理论，说明话语解释如何受说话者与听者之间共同基础的影响与引导；以及说明共同基础随话语推进如何发展（参「语用学」「含义」词条）。

语境在两个彼此独立的区分中起作用。第一个区分是语境与修改语境者之间：这里的语境是信息状态或它的某种适当抽象（参「信息的语义概念」词条），语境修改者则是所接收信息项的（意义）。信息不可能在不具备正确类型的预设信息状态的情况下被接收。古典静态谓词逻辑中的恰当对应物如下：信息状态是一个赋值（环境）或赋值集合，所接收的信息是一个赋值集合。第二个区分是语境与内容之间：这里的语境类似接收者的存储容量，以及可能影响新表达式/信息项如何被解释的其他各种特征；内容是所存储的（事实性、真值条件性的）信息。因此，此意义上的语境可以是寄存器/变量集合，或用 DRT/FCS 的术语说，是话语所指或文件；内容则是某个赋值集合，或者也许是约束这些话语所指之值与「现实世界之活候选」世界集合的世界/赋值对集合。

下面用一个例子说明这些区分。假定把信息状态看成一个由有限话语所指集合与世界/赋值对集合构成的对，其中赋值的定义域是给定的有限话语所指集合。这样的状态就是第一种意义上的语境，而话语所指集合则是第二种意义上的语境。一种基本更新是内容更新：约束世界/赋值对的集合，而让所指集合保持不变。第二种基本更新是所指集合的扩充：扩展已分配的存储容量，即把给定的世界/赋值对修改为世界与扩充赋值构成的对——扩充赋值受旧赋值约束，但在新所指上取一切可能值。于是，此例中的更新过程是二维的：既有内容的更新，也有第二种意义上的语境的更新。

## 2. 动态谓词逻辑

### 2.1. 概念基础

自然语言动态语义框架的动机，首先来自人称代词的指称与不定名词短语的指称之间可能存在的依赖关系。最简单的情形是同指性的话语回指，如：

- (1) *Mary met a student yesterday. He needed help.*（玛丽昨天遇见了一个学生。他需要帮助。）

可以看到，这一句子序列与下面这个单句意义相同：

- (2) *Yesterday, Mary met a student who needed help.*（昨天，玛丽遇见了一个需要帮助的学生。）

若假定不定词是存在量词，(2) 的分析就很简单：它只是说存在一个 $x$，它是学生、昨天遇见了玛丽、并且当时需要她的帮助。用谓词逻辑表示为：

- (3) $\exists x(\texttt{student}(x)\wedge\texttt{met}(m,x)\wedge\texttt{need-help}(x))$

然而，(1) 中那个等价的两句例子却没有类似的分析。这是因为解释是*组合性的*（讨论见「组合性」词条）：在组合分析中，我们会先得到对*玛丽昨天遇见了一个学生*的分析，其形式为 $\exists x(\texttt{student}(x)\wedge\texttt{met}(m,x))$；同样，第二句对应 $\texttt{need-help}(x)$。若假定组合多个句子的默认方式是合取，便得到：

- (4) $\exists x(\texttt{student}(x)\wedge\texttt{met}(m,x))\wedge\texttt{need-help}(x)$

$x$ 的最后一次出现不受约束，因此在古典谓词逻辑中，我们尚未得到 (1) 与 (2) 的等价翻译。由此可知：要在静态语义框架内说明 (1) 与 (2) 的等价，就无法维持对单个句子的组合性解释，而不得不假定 (1) 中的话语是作为整体被解释的。

这违反直觉。我们知道 (1) 中各单句的意义，也希望把握这些意义与其他意义结合、形成有意义的整体（对应一个句子序列）的潜能。动态语义能够给出句子层面与句子间层面的充分组合性意义分析：它保证，与古典谓词逻辑不同，在古典谓词逻辑句法的*动态*解释中，(3) 与 (4) *是*等价的。特别地，下式在动态谓词逻辑中有效：

$$\exists x(\psi \wedge \phi) \textrm{ iff } \exists x(\psi)\wedge \phi$$

在这类自然语言动态语义中，句子的意义不对应于真值条件集合，而对应于在语境上执行的行动。行动有两类。像 $\texttt{need-help}(x)$ 或 $\texttt{met}(m,x)$ 这样的谓述是*检验*：它们只检查当前语境中每个状态/赋值是否给 $x$ 指派了满足相应谓词的值，若（且仅若）如此，检验便把未改动的赋值传给输出语境。存在量词则不是检验，它有潜力通过随机重置其关联变量的值来改变语境。因此，$\exists x(\psi)$ 取一个语境，随机改变该语境中每个赋值里 $x$ 的值，并在这些改变后的赋值也满足检验 $\psi$ 所贡献的条件时，把它们传给输出语境。

这一语义的主要后果之一是：存在量词的作用域原则上是无限的。它改变某个变量的值，在该变量再次被改变之前，任何后续检验都访问那个被设定的值。这也意味着，存在量化的语义无需参照任何作用域即可给出：$\exists x$ 的意义就是这样一个行动——取一个语境，返回同一语境，其中至多把 $x$ 的值随机替换为另一个值。（下文将详细展开。）

于是，「动态语义」一词（用于自然语言时）浮现出两种含义。首先是作为一般想法：逻辑陈述表达的不是真值条件，而是语境上的行动（语境可以作各种概念化）。其次是作为一组理论立场——它们出现于关于某些自然语言现象（最著名的是代词回指）的语义学争论中（关于预设，可参见下文的类似动态语义处理）。就回指而言，这一理论含义体现为两个假说的结合：(i) 代词对应变量；(ii) 不定词是非量化的，只贡献一个动态的变量赋值更新。由第二个假说可见，动态语义的这一理论用法预设了更一般的观点：意义是语境上的行动。

在转而定义动态谓词逻辑之前，应当注意：动态语义处理回指的路线并不是文献中唯一的一条。我们也可以放弃「代词对应变量」的想法，赋予代词一种更精致的意义，类似于限定摹状词的意义。在当代传统中，这类想法早在 Quine 1960 与 Geach 1962 即已出现，后经（尤其是）Evans（1977, 1980）、Parsons（1978，其他网络资源）、Heim（1990）与 Elbourne（2001, 2005）发展成熟。讨论见 Nouwen（即将出版）。

### 2.2 动态谓词逻辑的刻画

上一小节初步展示了动态语义框架的基本目标：定义一种逻辑语义，使陈述表达行动，尤其是使存在量化具有重置变量、从而*改变*语境的潜力。线索来自普通谓词逻辑中存在量化的定义。假定在固定变量集 $\textsf{VAR}$ 与固定域 $D$ 上使用完全赋值，则完全赋值集合 $\textsf{ASSIGN}$ 就是一切从 $\textsf{VAR}$ 到 $D$ 的（完全）函数构成的集合。

设像 $P(x)$ 这样的原子公式的意义，是使 $\alpha(x)$ 为满足 $P$ 之对象的全体赋值 $\alpha$ 构成的集合 $F$。

现在定义：$$ \alpha[x]\beta := \forall v \in \textsf{VAR}\setminus\{x\}\ (\alpha(v) = \beta(v)). $$ 于是 [$x$] 就是二元关系「赋值 $\beta$ 是在赋值 $\alpha$ 中（至多）重置变量 $x$ 的值所得的结果」。如前所述，这是变量赋值上的等价关系。于是 $\exists x P(x)$ 的意义 $G$ 为：$$ G := \{\alpha \in \textsf{ASSIGN } \mid \exists \beta \in F\ \alpha[x]\beta \}. $$ 也就是说，$G$ 由那些可以就 $x$ 被成功重置、并因重置而得到属于 $F$ 的赋值的赋值组成。换个说法，$G$ 是由 $$\alpha R\beta := \alpha[x]\beta \textrm{ and } \beta \in F. $$ 给出的关系 $R$ 的*定义域*。

可以说，$G$ 是重置行动 $R$ 的前提条件。$\textsf{DPL}$ 的想法则是：把 $\exists x P(x)$ 的意义取为重置行动 $R$，而不是（如古典静态一阶逻辑那样）取为前提条件 $G$。这样并不丢失信息，因为 $G$ 总能从 $R$ 得到。而且，关系 $R$ 的值域由这样的赋值 $\beta$ 构成：它们与前提条件 $G$ 中的赋值至多在 $x$ 的值上不同，并且也属于 $F$（即 $\beta(x)$ 在 $P$ 的解释中）。二元关系 $R$ 的值域中所存的 $x$ 值，正是满足 $P$ 的 $x$ 值，即我们所要寻找的值。

更一般地，我们把赋值之间的*二元关系*取作 $\textsf{DPL}$ 意义。这类关系可以视为对*重置行动*的建模。这是对行动的一种虽显简单化、却著名而有用的建模方式的实例：一个行动被看作行动前的世界状态与行动后相应状态之间的关系。

以下是完整定义。设有非空域 $D$、变量集 $\textsf{VAR}$，以及签名 $\Sigma$ 的模型 $\mathcal{M}=\langle D, I\rangle$。原子条件 $\pi$ 的形式为 $P(x_0 , \ldots ,x_{n-1})$，其中 $P\in \Sigma$ 的元数为 $n$；原子重置 $\varepsilon$ 的形式为 $\exists v$，其中 $v$ 是变量。$\Sigma$ 的谓词逻辑语言定义如下（$\cdot$ 为合取，${\sim}$ 为否定）：

$$ \phi ::= \bot \mid \top \mid \pi \mid \varepsilon \mid \phi \cdot \phi \mid {\sim}(\phi). $$

赋值是 $\textsf{ASSIGN} := D^{\textsf{VAR}}$ 的元素 $\alpha , \beta ,\ldots$。该语言的动态/关系语义定义如下：

- $\alpha[\bot]\beta := \alpha \ne \alpha$。
- $\alpha[\top]\beta := \alpha = \beta$。
- $\alpha[P(x_0 , \ldots ,x_{n-1})]\beta := \alpha = \beta$ 且 $\langle \alpha(x_0), \ldots ,\alpha(x_{n-1})\rangle \in I(P)$，其中 $P\in \Sigma$ 的元数为 $n$。
- $\alpha[\exists v]\beta := \alpha[v]\beta$。
- $\alpha[\phi \cdot \psi]\beta :=$ 存在 $\gamma$，使得 $\alpha[\phi]\gamma$ 且 $\gamma[\psi]\beta$，简写为 $\alpha[\phi]\gamma[\psi]\beta$。
- $\alpha[{\sim}(\phi)]\beta := \alpha = \beta$ 且不存在 $\gamma$，使得 $\alpha[\phi]\gamma$。

注意，合取 $\cdot$ 解释为关系合成，否定 ${\sim}$ 则基本解释为相对于被否定公式所指关系之定义域的补。

真依关系性意义来定义：我们基本上是把赋值之间的二元关系投影到其第一坐标上。

$$\alpha \vDash \phi := \exists \beta\ \alpha[\phi]\beta.$$

蕴涵 $\phi \rightarrow \psi$ 可以定义为 ${\sim}(\phi \cdot {\sim}\psi)$。把真定义应用于此，得到：

> $\alpha \vDash \phi \rightarrow \psi \textrm{ iff } \forall \beta(\alpha[\phi]\beta \Rightarrow \beta \vDash \psi)$，即任何由前件 $\phi$ 更新 $\alpha$ 所得的赋值 $\beta$ 都满足后件 $\psi$。

关系性意义还给出下面这个漂亮的动态衍推定义：

$$\phi \vDash \psi := \forall \alpha , \beta(\alpha[\phi]\beta \Rightarrow \exists \gamma \beta[\psi]\gamma).$$

这一动态衍推定义最早由汉斯·坎普在其开创性论文 Kamp 1981 中引入。非正式地说，它说的是：任何吸收了 $\phi$ 所贡献之更新的赋值 $\beta$，都保证支持/满足 $\psi$。

注意，${\sim}\phi$ 等值于 $(\phi \rightarrow \bot)$，而 $(\phi \rightarrow \psi)$ 为真当且仅当 $\phi \vDash \psi$。同样重要的是：$\forall x (\phi)$ 可以定义为 $(\exists x \rightarrow \phi)$。

$\exists v$ 还有一种可能的记法：[$v := ?$]（随机重置），它强调了与编程语言中随机赋值的联系。

谓词符号的解释是*条件*，即对角线 $\{\langle \alpha , \alpha \rangle \mid \alpha \in \textsf{ASSIGN}\}$（也就是 $\top$ 的意义）的子集。对角线的子集是检验：它们不修改任何东西，只放过合格的（满足条件的），丢弃不合格的。映射 $\textsf{diag}$ 把赋值集合 $F$ 送到条件 $\{\langle \alpha , \alpha \rangle \mid \alpha \in F\}$，它是古典静态世界与动态世界之间的纽带。例如，$\textsf{diag}(F)$ 与 $\textsf{diag}(G)$ 的关系合成就是 $\textsf{diag}(F\cap G)$。

古典一阶逻辑（FOL）可以如下在 $\textsf{DPL}$ 中得到解释。假定 FOL 语言有下列联结词与量词：$\top , \bot , \wedge , \rightarrow , \exists x$。翻译如下：

- $( )^*$ 与原子公式、与 $\rightarrow$ 可交换
- $(\phi \wedge \psi)^* := \phi^* \cdot \psi^*$
- $(\exists x(\phi))^* := \neg \neg(\exists x \cdot \phi^*)$

由此得到：$[\phi^*]$ 是 $\phi$ 之古典解释的对角线。这一翻译是组合性的，它表明 FOL 可以视为 $\textsf{DPL}$ 的一个*片段*。

反过来，任何 $\textsf{DPL}$ 公式 $\phi$ 都可翻译为谓词逻辑公式 $\phi$°，使 $[\phi]$ 的定义域恰为 $\phi$° 的古典解释。定义这一翻译的方式之一，是采用带 Floyd-Hoare 规则的前提条件演算（Eijck and de Vries 1992）[^eijck-1992]；下面是一个变体。取标准谓词逻辑语言，加入菱形模态 $\langle \psi \rangle \phi$，其中 $\psi$ 取遍 DPL 公式，且 $\alpha \vDash \langle \psi \rangle \phi$ 当且仅当存在赋值 $\beta$，使 $\alpha[\psi]\beta$ 且 $\beta \vDash \phi$。下面的等值式表明，这一扩充并不增加表达力。

- $\langle \bot \rangle \phi \leftrightarrow \bot$。
- $\langle \top \rangle \phi \leftrightarrow \phi$。
- $\langle P(x_1 \ldots x_n)\rangle \phi \leftrightarrow (P(x_1 \ldots x_n) \wedge \phi)$。
- $\langle \exists v\rangle \phi \leftrightarrow \exists v\phi$。
- $\langle \psi_1 \cdot \psi_2\rangle \phi \leftrightarrow \langle \psi_1\rangle \langle \psi_2\rangle \phi$。
- $\langle{\sim}(\psi)\rangle \phi \leftrightarrow(\neg(\langle \psi \rangle \top) \wedge \phi)$。

因此，在一种弱意义上，「$\textsf{DPL}$ 中并无新事发生」：凡是能在 DPL 中定义的集合，FOL 也都能定义。这些模态等值式确定了一个翻译 (  )°，它给出达成给定后条件的最弱前提条件；下一节将示例说明这类翻译。

### 2.3 例：驴子句

动态谓词逻辑的一项长处是：它允许对驴子句作直截了当的组合分析（Geach 1962；见「回指」词条）[^geach-1962]。

- (5) If a farmer owns a donkey, he beats it.（如果一位农夫拥有一头驴子，他就会打它。）

显然，代词 $he$ 与 $it$ 分别与不定词 *a farmer*、*a donkey* 之间存在依赖关系。简言之，(5) 在古典分析中的困难在于：这种分析只有两种选择，而两者合起来并不能覆盖 (5) 的可能意义。若把不定词处理为指称某位特定的农夫与某头特定的驴子，把代词处理为径直拾取同一实体，便得到 (5) 的一种可能却并不显著的读法。最显著的读法描述拥有关系与殴打关系之间的共变：任何处于*拥有*关系的农夫-驴子对，也处于*殴打*关系。显然，我们需要把不定词解释为量词。可若这样做，它们就无法约束条件句后件中的变量，因为组合分析会把代词所贡献的变量置于条件句前件中诸存在量词的古典作用域之外。也就是说，(6) 并不给出 (5) 的正确真值条件。

- (6) $(\exists x(\textrm{farmer}(x)\wedge \exists y(\textrm{donkey}(y)\wedge\textrm{own}(x,y))))\rightarrow\textrm{beat}(x,y)$

(6) 的动态版本是 (7)，它给出正确的真值条件：$x$ 与 $y$ 的任何随机重置，只要 $x$ 是农夫、且 $y$ 是 $x$ 拥有的驴子，就也使 $x$ 打 $y$。

- (7) $\exists x\cdot \textrm{farmer}(x)\cdot \exists y\cdot \textrm{donkey}(y)\cdot \textrm{own}(x,y)\rightarrow \textrm{beat}(x,y)$

有趣的是，(7) 翻译为谓词逻辑后所得不是 (6)，而是 (8)。所以问题并不在于谓词逻辑无法表达驴子条件句的真值条件，而在于像 (8) 这样的句子不大可能是组合性解释过程的最终产物（但参 Barker and Shan 2008）[^barker-2008]。

- (8) $\neg \exists x (\textrm{farmer} (x) \wedge \exists y (\textrm{donkey} (y) \wedge \textrm{own}(x,y) \wedge \neg \textrm{beat}(x,y))).$

下面是由 (6) 推得 (8) 的过程：

$$ \begin{array}{l} (\langle(\exists x \cdot Fx \cdot \exists y \cdot Dy \cdot Hxy ) \rightarrow Bxy \rangle \top) ° \\ = (\langle{\sim}((\exists x \cdot Fx \cdot \exists y \cdot Dy \cdot Hxy ) \cdot {\sim} Bxy ) \rangle \top) ° \\ = \neg(\langle(\exists x \cdot Fx \cdot \exists y \cdot Dy \cdot Hxy ) \cdot {\sim} Bxy \rangle \top) ° \\ =\ldots \\ = \neg \exists x (Fx \wedge \exists y (Dy \wedge Hxy \wedge \neg Bxy ))).\\ \end{array} $$

### 2.4 动态广义量化

动态谓词逻辑之所以能成功处理自然语言中量化与回指的交互，取决于一个事实：在 DPL 中，存在量化是动态的，全称量化则不是。倘若全称量化也是动态的，情况会如何？首先要注意，与随机重置行动 $\exists x$ 平行地定义一个全称量化行动 $\forall x$ 并无意义：全称量化只有在给定域（*限定语*）上、并相对于某个给定性质（*作用域*）才有意义。其次，若给 $\forall x(\phi)(\psi)$ 以动态解释，它就会预测全称量词能像存在量词那样，跨小句边界与单数代词建立回指关系。对 (9) 这类情形，这显然不可取。

- (9) Every boy wrote an essay. #He wrote a research proposal too.（每个男孩都写了一篇文章。#他也写了一篇研究计划。）

- (9) Every boy wrote an essay. #He wrote a research proposal too.（每个男孩都写了一篇文章。#他也写了一篇研究计划。）

然而，一旦考察*复数回指*，便会看出全称量化（事实上，还有其他非不定词类的广义量词）的静态本性不可视为理所当然。例如，(10) 允许一种读法，其中 *they* 与 *every boy* 有回指联系。

- (10) Every boy wrote an essay. They wrote a research proposal too.（每个男孩都写了一篇文章。他们也写了一篇研究计划。）

- (10) Every boy wrote an essay. They wrote a research proposal too.（每个男孩都写了一篇文章。他们也写了一篇研究计划。）

假定 (10) 这类例子应当作动态处理（讨论见前文对替代解释的评注以及 Nouwen 即将出版），结论只能是：全称量词不应被赋予静态解释。接下来的问题是：何种解释恰当，这种解释又如何区分 (9) 中不顺畅的回指与 (10) 中的回指？一种选项是区分量词在其作用域内所约束的变量之值，与在该量词作用域外赋给该变量的值（例如 Kamp and Reyle 1993 采用这一策略，讨论见 Nouwen 2007）[^kamp-1993][^nouwen-2007]。为说明 (10)，人们会让 (10) 第一句中受量词约束的变量出现取各个男孩为值，而在量词作用域之外（即第二句中）让该变量取全体男孩构成的复数。然而，正如 van den Berg (1996) 首先表明的，这种方案只走了一半：在话语中，代词不仅能访问与量词相关联的复数，还能访问这些量词所参与的关系。例如在 (11) 的第二句中，代词 $it$ 与主语位置上对男孩的量化共变，使第二句被理解为每个男孩都提交了 $he$ 所写的那篇文章（参 van den Berg 1996；Krifka 1996；Nouwen 2003；Brasoveanu 2007, 2008）[^berg-1996][^brasoveanu-2007][^krifka-1996][^nouwen-2003]。

- (11) Every boy wrote an essay. Each of them submitted it to a journal.（每个男孩都写了一篇文章。他们每个人都把它投给了一家期刊。）

- (11) Every boy wrote an essay. Each of them submitted it to a journal.（每个男孩都写了一篇文章。他们每个人都把它投给了一家期刊。）

动态处理广义量化与复数回指的主导想法，不是给变量指派复数来表征复数值，而是采用一种允许赋值函项之复数（例如集合）的语境概念。设 (11) 第一句译为带动态量词的动态谓词逻辑式：$\forall x(\textrm{boy}(x))(\exists y\cdot \textrm{essay}(y)\cdot \textrm{wrote}(x,y))$。这类公式的解释要求收集这样的赋值函项：其中 $x$ 的值是男孩，$y$ 的值是该男孩所写的一篇文章；全称量词则要求这类收集涵盖谓词 *boy* 的一切可能值。于是，在随后的话语中，我们可以访问全体 $x$ 值（全体男孩）、全体 $y$ 值（男孩们所写的文章），以及各个男孩-文章对：(11) 第一句之后语境赋值集合中的每个原子赋值 $f$ 都满足，$f(y)$ 是由男孩 $f(x)$ 所写的一篇文章。要说明 (11) 中的回指，只须假定那里的全称量化涉及对赋值函项的全称量化，而不只是对值的量化。实现这一想法的各种方式见 van den Berg (1996)、Nouwen (2007, 即将出版)、Brasoveanu (2007, 2008, 2013)。

结论是：只要给定结构适当的语境概念，量词一般都能得到动态解释。一个重要后果是，这类分析可推广到非名词性量词（Brasoveanu 2007）[^brasoveanu-2007]。(11) 这类情形可描述为量化从属，而结构化语境进路可以看作意在打开一扇窗，窥见从属背后的机制。情态从属的情形（Roberts 1987, 1989）[^roberts-1987]，如著名的 (12)，可以得到平行处理。

- (12) A wolf might come in. It may eat you.（可能有一只狼进来。它可能会吃掉你。）

- (12) A wolf might come in. It may eat you.（可能有一只狼进来。它可能会吃掉你。）

情态词 *might* 引入一个对可能世界的量词，其作用域涵盖不定词 *a wolf*，正如上文 (11) 中 *every boy* 的作用域涵盖 *an essay*。因此，(12) 第一句所贡献之更新的输出（赋值函项集合）将存储两样东西：*might* 所贡献的一组相对于现实世界在认识上可能的世界，以及一组在这些认识可达世界中进来的狼。(12) 的第二句于是可以进一步展开世界与狼之间的依赖关系，要求至少某些认识可能性满足：相应的狼不仅进来，而且吃掉你。

### 2.5 回指之外的动态性

回指与预设（见下文）可以说是需要动态语义分析的核心语言现象，但原则上语境的任何方面都可能成为某一现象的目标，而该现象值得对解释作动态分析。Barker 2002 对模糊陈述所提供信息的处理即是一例。Barker 假定语境含有 *tall* 这类模糊形容词的精确标准。像 (19) 这样的句子于是可以有两种不同用法。(19) John is tall.（约翰很高。）若信息状态含有关于什么算 *tall* 的（足够）精确信息，说出 (19) 便可用来提供关于约翰身高的信息。然而，若听者对 *tall* 这类表达式的恰当精确化毫无概念（比方说，他是外星人或外国人），却掌握关于约翰身高的信息，那么 (19) 便可用来提供关于标准的信息。

## 3. 预设

### 3.1 预设与联结词的动态语义

语境在预设中起重要作用。像 (13) 这样的句子预设约翰迟到了。但若把这句话放进一个提供该信息的语境，如 (14)，预设便消失了：(14) 中约翰迟到是被*断言*的，而非被预设的。

- (13) Mary knows that John is late（玛丽知道约翰迟到了）
- (14) John is late and Mary knows that he is late.（约翰迟到了，而玛丽知道他迟到了。）

- (13) Mary knows that John is late（玛丽知道约翰迟到了）
- (14) John is late and Mary knows that he is late.（约翰迟到了，而玛丽知道他迟到了。）

斯托尔内克（Stalnaker 1973）认为，预设基于假定的共同知识。说出像 (13) 这样的句子，即*视为理所当然*：约翰迟到是共同知识。在此意义上，(13) 要求说出它的语境中这一共同知识已然就位。相反，(14) 没有这种要求，原因很简单：(14) 的第一个合取支断言了第二个合取支视为理所当然的东西。斯托尔内克的关键假定是：解释是增量的——对 [$S$1 and $S$2] 形式的句子，$S$2 的解释发生在一个已用 $S$1 更新过的语境中。图示如下：

- (15) ${C}[{S1 \textrm{ and } S2}] = ({C}[{S1}])({S2})$

斯托尔内克对 (15) 图式的解释是语用性的：在话语中遇到一连串小句时，我们*依据*一个已被先前小句之解释所告知的语境来解释这些小句。这一增量解释的想法简单而有力，对具有合取解释的复杂话语（例如以 *and* 连接的并列结构、陈述句的简单序列）完全说得通：合取中的各合取支具有断言力量，可用来更新语境，从而创造新的局部语境。然而问题在于：预设并不只在合取环境中消失。与 (14) 一样，(16) 也不要求约翰迟到是共同知识，可这里第一个析取支并没有断言力量（讨论见 Schlenker 2009）[^schlenker-2009]。何种语用规则能说明 (16) 中预设的缺失，并不显然。

- (16) Either John is not late or Mary does not know that he is late.（要么约翰没有迟到，要么玛丽不知道他迟到了。）

- (16) Either John is not late or Mary does not know that he is late.（要么约翰没有迟到，要么玛丽不知道他迟到了。）

(16) 这类例子使人怀疑 (15) 这类增量解释图式是否有价值。此外，(15) 对解释如何进行的假定也颇显武断：断言一个命题内容为 $p$ 的小句，并不自动使 $p$ 成为共同知识；这样的断言更应视为使 $p$ 成为共同知识的*提议*，而 $p$ 是否成为共同基础，取决于其他对话者是否愿意接受该命题（例如不反对该断言）。换言之，(15) 似乎不适于刻画信息流（之动态）的语用学。

一条可能的出路是：不把 (15) 看作语用规则，而看作以动态解释概念表述的语义规则。这一点最著名地见于 Heim 1983b（追随 Karttunen 1973）。Karttunen 区分*全局语境*与*局部语境*：前者是评价当前句子所相对的语境，后者是解释当前小句（或潜在地某个次小句实体）所相对的语境。现在的想法是：像 (15) 这样的规则可以表达 *and* 的语义。在 (15) 中，$C$ 是全局语境；合取语义的关键部分在于，$S$2 的局部语境是用 $S$1 更新全局语境的结果。因此，(14) 中没有预设，仅仅是由于 *and* 的动态*语义*。要说明 (16) 中预设的缺失，只须给出一种析取语义，使第二个析取支的局部语境已用第一个析取支的否定更新过；这样的说明见 Krahmer and Muskens 1996，它同时刻画了（双重）否定与回指之间的交互。

为更具体起见，假定语境是可能世界集合，且用简单小句 $S$ 更新 $C$ 所得 $C[S]$ 就是 $C\cap p$，其中 $p$ 是 $S$ 的命题内容：用一个小句更新 $C$，输出的便是 $C$ 中使该小句为真的世界。(18) 中的规则展示了英语主要命题算子之动态解释的一个海姆式片段。

- (17) ${C}[{\textrm{not } S1}] = {C} \backslash {C}[{S1}]$ ${C}[{S1 \textrm{ and } S2}] = ({C}[{S1}])[{S2}]$ ${C}[{\textrm{If }S1, \textrm{ then } S2}] = ({C}[{\textrm{not }S1}]) \cup ({C}[{S1}])[{S2}]$ ${C}[{S1 \textrm{ or } S2}] = {C}[{S1}] \cup ({C}[{\textrm{not }S1}])[{S2}]$

有人质疑这种动态解释的解释价值，理由是：该框架无法说明，为何似乎没有自然语言表达式编码 (17) 的某种最小变体——例如第二个析取支 $S$2 的局部语境是 $C[S1]$ 而非 $C[\textrm{not }S1]$，或 $S$1 的局部语境基于用 $S$2 作更新，或如 (18) 那样根本没有局部语境（例如见 Soames 1989）[^soames-1989]。

- (18) ${C}[{S1 \textrm{ or } S2}] = {C}[{S1}] \cup {C}[{S2}]$

鉴于这类批评，近年来静态的预设投射进路重新兴起，如 Schlenker（2008, 2009）、Chemla（2008，其他网络资源）的语用进路，以及 George（2008）、Fox（2008）的语义（三值）进路。不过正如 Rothschild 所指出的，有一条路径可以使 (17) 式的语义具有解释力：须表明，联结词的可允许动态解释共享某些性质。Rothschild (2011) 表明，若假定语境变化潜能遵守某些有定性原则，则对预设作既有解释力、又经验上充分的动态处理是可能的。假定（对简单小句 $S$）$C[S]$ 有定义，当且仅当 $S$ 的任何预设都在 $C$ 的所有世界中为真。(17) 中的规则确定了复杂陈述的有定性条件；例如按 (17)，[not S] 在 $C$ 中无定义，仅当 $S$ 在 $C$ 中无定义。Rothschild 的洞见是：我们可以通过约束所得到的有定性条件来约束动态解释。

### 3.2 预设与动态认知逻辑

认知逻辑即知识的逻辑，是模态逻辑的一个分支，研究「$i$ 知道……」这一模态（参「认知逻辑」「信念修正逻辑」词条）。认知逻辑中的动态转向发生在 2000 年前后，把焦点引向状态变化，只不过此时的「状态」被看作一组能动者之知识的表征。

若固定一组基本命题 $P$ 与一组能动者 $I$，则 $P$ 与 $I$ 的知识状态由三部分构成：一个可能世界集合 $W$；一个赋值函数 $V$，给 $W$ 中每个 $w$ 指派 $P$ 的一个子集（若 $w \in W$，则 $V(w)$ 列出在 $w$ 中为真的基本命题）；以及对每个能动者 $i \in I$ 的一个关系 $R_i$，陈述 $i$ 的认识相似性（若 $wR_i w'$，意即能动者 $i$ 无法区分世界 $w$ 与世界 *w$'$*）。认知模型 $M = (W, V, \{R_i \mid i \in I\})$ 即所谓多模态克里普克模型；带点认知模型则是带有指定世界 $w_0$（代表现实世界）的认知模型。

若作出一个公共宣告 $\phi$，给定的认知状态 $(M, w_0) = ((W, V, \{ R_i \mid i \in I\}), w_0)$ 会发生什么？直观地说，$M$ 的世界集合 $W$ 被限制为那些使 $\phi$ 成立的 $w \in W$，赋值函数 $V$ 与认识关系 $R_i$ 也相应受限。称新模型为 $M\mid\phi$：若 $\phi$ 在 $w_0$ 中为真，则公共宣告 $\phi$ 的意义可以看作从 $(M, w_0)$ 到 $(M\mid\phi , w_0)$ 的映射；若 $\phi$ 在 $w_0$ 中为假，则不可能更新。

Veltman 的更新逻辑可以容纳进公共宣告逻辑（参「共同知识」词条）：允许形如 $\Diamond \phi$ 的公共宣告，其中该模态读作「在共同知识下可达」。若一组能动者的 $S$5 知识状态（参「认知逻辑」词条）用公共宣告 $\Diamond \phi$ 更新，则当 $\phi$ 在模型某处为真时，更新不改变任何东西（因为此时 $M\mid\Diamond \phi$ 等于 $M$）；否则更新导致不一致（因为公共宣告被假定为真）。这与更新逻辑的定义相符。

带交流更新的认知逻辑，其逻辑工具箱称为动态认知逻辑，简称 DEL。DEL 始于对公共宣告之认识效应与信念效应的分析（Plaza 1989；Gerbrandy 1999）[^gerbrandy-1999][^plaza-1989]。公共宣告之所以有趣，在于它创造共同知识。此外还有私下宣告、群体宣告、秘密分享、谎言等各种宣告，它们也具有明确定义的认识效应。Baltag et al. 1999 与 Baltag and Moss 2004 提出了涵盖一大类更新行动的通用框架；Benthem et al. 2006 进一步推广为完整的交流与变化逻辑，其行动得到丰富化，允许改变世界的事实。动态认知逻辑的教科书式处理见 Ditmarsch et al. 2006。

在认知逻辑框架内，可以如下表征带有预设的说出行为的交流情境：先表征说话者关于其听众知道或相信什么的假定（即一个多能动者信念或知识状态），再建模交流行动对该信念状态的影响。在动态认知逻辑中处理带预设的说出行为，一种简单方式是把预设 $P$ 建模为公共宣告「$P$ 是共同知识」。若 $P$ 确是共同知识，用此信息更新不改变任何东西；若 $P$ 不是共同知识，则该说出行为为假，而对假命题的公共宣告会产生不一致的知识状态。

### 3.3. 超越预设

动态语义特别适合描述不同类型的语言材料如何影响信息状态的不同方面。尤其，它能有效建模*议题*内容与*非议题*内容之别：前者如陈述句的说出所断言的内容，后者起某种次要作用。例如 (19) 的议题内容是约翰的邻居昨天被捕，这是说话者意图断言的信息；同位语 *who I have never met* 则非议题内容。看出这一点的一种方式是：对话者只有在意图质疑邻居被捕这一事实时，才能以 *No! That's not true!* 回应 (19)；若只是想表达对说话者所谓从未见过邻居的不信，则不能。

- (19) John's neighbour, who I have never met, was arrested yesterday.（约翰的邻居——我从未见过他——昨天被捕了。）

- (19) John's neighbour, who I have never met, was arrested yesterday.（约翰的邻居——我从未见过他——昨天被捕了。）

动态语义是分析这类句子被解释时所发生之事的适当框架，因为它天然允许对彼此分离的信息流建模。例如 AnderBois et al. 2015 对 (19) 这类句子给出如下说明：主句更新一个局部的可能世界集合，更新后的集合可以看作用以更新共同基础的潜在候选；同位语则直接更新共同基础——与其说是*提议的*共同基础更新，不如说是*强加的*更新（关于另一种动态逻辑，见 Nouwen 2007）[^nouwen-2007]。AnderBois et al. 2015 的想法部分受到类似观念的启发，那些观念已在传信范畴（evidentials）领域得到成功应用；特别见 Murray 2014。

## 4. 在类型化逻辑中编码动态性

组合性一直是自然语言语义学使用逻辑系统时的一项重要关切（见「组合性」词条）。借助高阶逻辑（见「二阶与高阶逻辑」「丘奇类型论」词条），可以对自然语言的量化系统等给出彻底组合性的说明，古典蒙塔古语法即已展示这一点（Montague 1974a,b, 1973；参「逻辑形式」词条）[^montague-1974a]。下面回顾动态进路如何扩展至高阶系统。动态语义与类型论之间的联系更像联络而非稳固婚姻：二者之间并无内在的必然联系；此处处理这一联系，是为说明蒙塔古语法对动态语义的历史影响。

蒙塔古语法的大多数动态版本提案，发展的其实是动态谓词逻辑（DPL）的高阶版本：Groenendijk and Stokhof 1990；Chierchia 1992, 1995；Muskens 1994, 1995, 1996；Eijck 1997；Eijck and Kamp 1997；Kohlhase et al. 1996；Kuschert 2000 皆属此列。这些系统都从 DPL 进路继承了一个特征（或缺陷）：重新赋值具有破坏性。DRT 则没有这个问题：Kamp 1981 与 Kamp and Reyle 1993 的话语表现构造算法以定义域有限的函数来表述，并谨慎地谈论「取一个新鲜话语所指」以扩展验证函数的定义域——每处理一个新名词短语即如此。

在外延蒙塔古语法中，「a man」翻译为：

$$\lambda P\exists x(\textrm{man } x \wedge Px).$$

这里 $P$ 的类型为 $e \rightarrow t$，是 VP 槽位的变量；假定 VP 指称实体集合。

在 Groenendijk and Stokhof 1990 的动态蒙塔古语法（DMG）中，不定名词短语的翻译引入一个回指索引。「a man」的翻译为

$$\lambda P\lambda a\lambda a' \cdot \exists x(\textrm{man }x \wedge Pu_i (u_i \mid x) aa').$$

DMG 不像古典外延蒙塔古语法那样以 e 与 t 为基本类型，而以 $e, t$ 与 $m$（m 指标记）为基本类型。状态为标记挑出实体，因此可看作类型为 $m \rightarrow e$ 的对象。把 $m \rightarrow e$ 缩写为 $s$（「状态」），类型为 $s \rightarrow s \rightarrow t$ 的对象便称为状态转换。「a man」在 DMG 翻译中的变量 $P$ 类型为 $m \rightarrow s \rightarrow s \rightarrow t$，因此 VP 的意义已从类型 $e \rightarrow t$ 提升到这一类型。注意 $\rightarrow$ 右结合，故 $m \rightarrow s \rightarrow s \rightarrow t$ 是 $m \rightarrow(s \rightarrow(s \rightarrow t))$ 的缩写。事实上，DMG 可以看作系统地用标记替换实体、用状态转换替换真值的结果。「is happy」的 VP 意义是一个把标记映射到状态转换的函数；标记 $u_i$ 的状态转换将检查输入状态是否把 $u_i$ 映射到一个快乐的实体，以及输出语境是否等于输入语境。变量 $a$、*a$'$* 取状态为值，表达式 $(u_i \mid x)a$ 表示把 $a$ 中 $u_i$ 的值重置为 $x$ 的结果，于是 $u_i$ 的旧值被销毁（破坏性赋值）。指称标记 $u_i$ 上的回指索引 $i$ 由翻译引入；事实上，翻译从带索引的不定名词短语「a man$_i$」出发。蒙塔古式组合性与动态语义之间的联系，以及蒙塔古式与动态的基本要素，在 Muskens 1991, 1995, 1996 提出的类型化变化逻辑中要透明、精炼得多；因此，Muskens 的组合性 DRT 大概是当前组合性动态语义研究的*事实*标准与出发点。另一种处理见于增量类型化逻辑（ITL）：它是对一种「栈语义」的类型化逻辑扩展，栈语义基于无变量索引，避免了破坏性赋值问题。Vermeulen 1993 所发展的 DPL 栈语义，其基本想法是以允许旧值复用的栈值赋值，取代普通 DPL 中重置时丢弃旧值的破坏性赋值：栈值赋值给每个变量指派一个值栈，栈顶为当前值；存在量化把一个新值压入栈，但也可以弹出栈以复用先前指派的值。Eijck 2000 的 ITL 事实上是栈语义的类型化版本，使用单一栈。

假定一个实体域，语境是实体的有限列表。若 $c$ 是长度为 $n$ 的语境，则称其元素为 $c[0]$、$\ldots ,c[n-1]$，称其长度为 $\lvert c\rvert$；长度为 $i$ 的语境，其类型记作 $[e]^i$。若 $c$ 是 $[e]^i$ 中的语境，则类型为 $\{0, \ldots ,i-1\}$ 的对象可以作为索引进入 $c$。若 $c \in[e]^i$ 且 $j \in \{0, \ldots ,i-1\}$，则 $c[j]$ 是语境中位置 $j$ 上出现的类型 e 的对象。语境的一项关键运算是用元素扩充：若 $c :: [e]^i$ 且 $x :: e$（$c$ 是长度为 $i$ 的语境，$x$ 是一个实体），则 $c\mcaret x$ 是长度为 $i+1$ 的语境，其元素为 $c$[0]、$\ldots ,c[i-1], x$。因此 $\mcaret$ 是类型为 $[e]^i \rightarrow e \rightarrow[e]^{i+1}$ 的算子。还应注意，$[e]^i$ 这类类型事实上是多态类型，$i$ 充当类型变量。见 Milner 1978。

ITL 中没有破坏性赋值，不定名词短语在句法上也不带索引。ITL 对「a man」的翻译从语境中取得索引，如下：

$$\lambda P\lambda c\lambda c' \cdot \exists x (\textrm{man } x \mcaret P\lvert c\rvert (c^x)c').$$

这里 $P$ 是类型为 $\{0, \ldots ,i\} \rightarrow[e]^{i+1} \rightarrow [e]^j \rightarrow t$ 的变量，$c$ 是类型为 [$e]^i$、代表长度为 $i$ 之输入语境的变量，$c'$ 是类型为 [$e]^j$、代表输出语境的变量。注意类型 $\{0, \ldots ,i\} \rightarrow [e]^{i+1} \rightarrow [e]^j \rightarrow t$ 对 $P$ 而言表明：$P$ 先取范围 $\{0, \ldots ,i\}$ 中的一个索引，再取一个适合此范围的语境（长度为 $i+1$ 的语境），再取一个长度未知的语境，然后给出真值。$P$ 是一元谓词的类型，按如下方式提升到语境变化者的层面：提升后的谓词不用一个在类型 $e$ 的对象上取值的变量来构成表达式，而用在输入语境大小上取值的变量，构成指称该语境之变化者的表达式。

ITL 对「a man」的翻译具有类型 $$(\{0, \ldots ,i\} \rightarrow[e]^{i+1} \rightarrow [e]^j \rightarrow t) \rightarrow [e]^i \rightarrow [e]^j \rightarrow t.$$ 在 $P\lvert c\rvert (c\mcaret x)c'$ 中，$P$ 变量标记 VP 解释的槽位；$\lvert c\rvert$ 把输入语境的长度给 $P$，取得值 $i$——即语境被扩充时下一个可用槽位的位置。该槽位由一个指称某人的对象 $x$ 填充。注意 $c\mcaret x[\lvert c\rvert ] = c\mcaret x[i] = x$，故索引 $i$ 用于从语境中挑出那个人。

要看出动态高阶系统可在 ITL 中表达，只须表明如何定义适当的动态运算。假定 $\phi$ 与 $\psi$ 具有语境转换的类型，即类型 [$e] \rightarrow[e] \rightarrow t$（用 [$e$] 表示任意语境），且 $c, c', c''$ 的类型为 [$e$]。于是可如下定义动态存在量词、动态否定与动态合成：

$$ \begin{align*} \cal{E} & := \lambda cc'\cdot \exists x(c \mcaret x = c') \\ {\sim}\phi & := \lambda cc'\cdot (c = c' \mcaret \neg \exists c'' \phi cc'') \\ \phi ; \psi & := \lambda cc'\cdot \exists c''(\phi cc'' \mcaret \psi cc') \end{align*} $$

动态蕴涵 $\Rightarrow$ 按通常方式借助 ${\sim}(\phi; {\sim}\psi)$ 定义。

ITL 与 Muskens 式组合性 DRT 并不相斥，例如见 Bittner 2014。本节最后要指出：整合蒙塔古式组合性与动态语义的系统范围，远未被完全勘定。近来一系列整合「基于延续的语义」与动态语义的工作，正在探索整合与推广二者的新方式；见 de Groote 2006、Bumford and Barker 2013、Charlow 2014、Bumford 2015、Martin 2016。

## 5. 结论

希望上文已使读者感到，动态语义是处理意义与信息加工的一种富有成果而灵活的进路。它带来一套灵活的工具，以及一批「杀手级应用」：驴子句的组合处理、回指联结的说明、预设投射的说明、认识更新的说明，以及对不同种类（非议题）更新之间精细区别的刻画。动态语义是形式语义学中一个非常活跃的子领域，而以动态进路处理的现象在跨语言上的范围正日益扩大。

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

- Chemla, Emmanuel, 2008, 「[相似性：走向标量含义、自由选择许可与预设投射的统一说明](http://semanticsarchive.net/Archive/WI1ZTU3N/Chemla-SIandPres.html)」，未刊稿，巴黎高等师范学院（Ecole Normale Superieur）。
- Parsons, Terence, 1978, 「[代词作为释义](http://www.philosophy.ucla.edu/people/faculty/tparsons/Pronouns%20as%20Paraphrases/Pronouns%20as%20Paraphrases.pdf)」，未刊稿，马萨诸塞大学阿默斯特分校。

## 相关词条

回指 | 断言 | 共同知识 | 组合性 | 直陈条件 | 认识语境论 | 话语表征理论 | 心灵外在主义 | 含义 | 指代词 | 语义概念的信息 | 经典逻辑 | 条件逻辑 | 认知逻辑 | 信念修正的逻辑 | 二阶逻辑与高阶逻辑 | 逻辑形式 | 狭义心理内容 | 心灵计算理论 | 一阶模型论 | 语用学 | 指称 | 科学实在论 | 言语行为 | 塔尔斯基的真理定义 | 丘奇类型论

**（译注：相关词条的中文站内链接将由管线在对应词条重译完成后统一挂接。）**
