# 模糊逻辑 Fuzzy Logic (Petr Cintula、Christian G. Fermüller、Carles Noguera)

*首次发表于 2016 年 11 月 15 日；2021 年 11 月 11 日实质修订。*

模糊逻辑想刻画的是含“Petr 年轻（有钱、个子高、肚子饿等）”这类模糊、不精确语句的逻辑推理。它指一族多值逻辑，真值被解释为真值度。复合命题（如“Carles 个子高，Chris 有钱”）的真值由各组成部分的真值决定。也就是说，和经典逻辑一样，这里也要求真值函项性。

模糊逻辑诞生于 Lotfi Zadeh（1965）提出的模糊集合论。模糊集合给论域中每个元素指定一个隶属度，通常是区间 $[0,1]$ 里的实数；模糊逻辑则给命题指定真值度。标准的真值（度）集合就是实数单位区间 $[0,1]$：$0$ 表示“完全不真”，$1$ 表示“完全真”，其余值表示部分真，也就是介于两者之间的真值度。[^note-1]

“模糊逻辑”常被用在很宽的意义上，泛指各种系统处理某类 **度** 的形式化方法与技术（例如 Nguyen & Walker 2000）。在工程语境中（模糊控制、模糊分类、软计算），它追求的是能容忍次优和不精确的高效计算方法（例如 Ross 2010）。本词条讲的模糊逻辑取狭义，即自 Petr Hájek（1998）那部开创性专著之后确立为数学逻辑分支、如今通称“数学模糊逻辑”的部分。各变体的历史细节，见 Bělohlávek, Dauben, & Klir 2017。

数学模糊逻辑关注以“部分真”的真值函项说明为基础的逻辑，并按经典数学逻辑的路子来研究：句法、模型论语义、证明系统、完全性等，命题层面和谓词层面都要管（见 Cintula, Fermüller, Hájek, & Noguera 2011、2015）[^cintula-2015][^cintula-2011][^fermüller-2015][^hájek-2011]。

## 1 基于 t-范数的模糊联结词

模糊逻辑的标准真值集合是实数单位区间 $[0,1]$，按自然序 $\leq$ 排列：从完全假（$0$）经过连续不断的中间真值度，到完全真（$1$）（真常项的其他解释与真值的其他集合，见第 5、7 节）。主流数学模糊逻辑有个基本假设：联结词要在真值度集合上按真值函项方式解释，而且在标准设定下，这种真值函项在端点 $0$、$1$ 上要表现得像经典逻辑。若对每个 $x,y \in [0,1]$ 规定 $x \land y = \min\{x,y\}$、$x \lor y = \max\{x,y\}$、$\neg x = 1 - x$，合取、析取与否定的行为就非常自然。

这三个真值函项就是 Joseph Goguen（1975）最初提出的模糊逻辑语义，后来 Gehrke, Walker, & Walker（1997）等人对之作了形式研究。不少人仍把它称作“模糊逻辑”。但人们很快看出，这个语义框架太单薄：既编码不了推理的许多有趣方面，也撑不起一套完整的数学逻辑理论。

通常还会添一个非幂等合取 $\&$，因为把一个部分真的假设用两次，真值度可能和只用一次不同。这种合取通常用 $[0,1]$ 上的一个二元运算解释：它未必幂等，但可结合、可交换、对两个变元都单调不减，并以 $1$ 为单位元。这类运算叫 **t-范数**（**三角范数**），其数学性质研究得很透（见 Klement, Mesiar, & Pap 2000）[^klement-2000]。著名 t-范数有：前文提过的 $\min$、实数标准乘法 $\cdot$，以及 Łukasiewicz t-范数 $x *_{Ł} y=\max\{x+y-1,0\}$。这三个都是连续函数；任何别的连续 t-范数，都可写成这三个基本 t-范数的 **序和**（Ling 1965; Mostert & Shields 1957）[^ling-1965][^mostert-1957]。

有意思的是，每个左连续 t-范数都对应一个合适的蕴涵。事实上，t-范数 $\ast$ 左连续，当且仅当 $[0,1]$ 上恰有一个二元运算 $\Rightarrow_\ast$ 满足所谓 **剩余条件**：$$ x \ast y \leq z\ \text{ 当且仅当 }\ x \leq y \Rightarrow_\ast z. $$ 这个 $\Rightarrow_\ast$ 叫 *$\ast$ 的剩余*，并且可以证明 $x \Rightarrow_\ast y = \max\{z \mid x \ast z \leq y\}$。三个著名 t-范数的剩余分别是：$x \Rightarrow_\min y = 1$（当 $x\leq y$），否则为 $y$；$x \Rightarrow_\cdot y = 1$（当 $x\leq y$），否则为 $\frac{y}{x}$；以及 $x \Rightarrow_{Ł} y = \min\{1, 1 - x+y\}$。

在一般的 t-范数设定里，否定靠剩余来解释：给定左连续 t-范数 $\ast$，令 $\neg_\ast x = x\Rightarrow_\ast 0$。Łukasiewicz t-范数给出否定 $\neg_{Ł} x = 1 - x$（即 Łukasiewicz 否定，或称标准对合否定）；最小与乘积 t-范数给出的否定相同，称为 Gödel 否定：$\neg_\mathrm{G} 0 = 1$，否则为 $0$。

## 2 MTL：一种基础模糊逻辑

用上述类型真值函项解释联结词的最弱逻辑是 MTL（*幺半群 t-范数逻辑*，Esteva & Godo 2001）[^esteva-2001][^esteva-2001-2]。它的原始二元联结词是 $\mathbin{\&}, \to, \wedge$，另有真常项 $\overline{0}$；可导出联结词定义为：$$ \begin{align} \varphi \lor \psi &= ((\varphi \to \psi) \to \psi) \land ((\psi \to \varphi) \to \varphi),\\ \neg \varphi &= \varphi \to \overline{0}, \\ \varphi \leftrightarrow \psi &= (\varphi \to \psi) \land (\psi \to \varphi),\\ \overline{1} &= \neg \overline{0}. \end{align} $$ MTL 的后承关系由所有左连续 t-范数给出的语义来定义。给定左连续 t-范数 $\ast$ 与从命题变元到 $[0,1]$ 的映射，把 $\&$ 解释为 $\ast$、蕴涵 $\to$ 解释为其剩余 $\Rightarrow$、$\land$ 与 $\overline{0}$ 解释为 $\min$ 与 $0$，就得到全部公式的 $\ast$-赋值。

若对每个左连续 t-范数 $\ast$ 和每个 $\ast$-赋值 $e$，只要 $e(\psi) = 1$ 对所有 $\psi \in \Gamma$ 成立，就有 $e(\varphi) = 1$，则称公式 $\varphi$ 是公式集 $\Gamma$ 在 MTL 中的后承，记作 $\Gamma \models_\mathrm{MTL} \varphi$；说白了，前提完全真，结论也完全真。始终取值 $1$ 的公式 $\varphi$（即 $\emptyset\models_\mathrm{MTL}\varphi$）叫 MTL 的有效式或重言式。要注意，$\varphi \mathbin{\&} \psi \to \varphi \land \psi$ 在 MTL 中是重言式，反方向的 $\varphi \land \psi \to \varphi \mathbin{\&} \psi$ 却不是——合取 $\&$ 比 $\land$ 强。

MTL 也可以写成希尔伯特式证明系统，公理如下：

$$ \begin{align} (\varphi \to \psi) & \to ((\psi \to \chi) \to (\varphi \to \chi)) \\ \varphi \mathbin{\&} \psi & \to \varphi \\ \varphi\mathbin{\&}\psi & \to\psi\mathbin{\&}\varphi \\ \varphi \land \psi & \to \varphi \\ \varphi \land \psi & \to \psi \land \varphi \\ (\chi \to \varphi) & \to ((\chi\to \psi) \to (\chi \to \varphi\wedge \psi)) \\ (\varphi\mathbin{\&}\psi \to \chi) & \to (\varphi\to(\psi \to \chi)) \\ (\varphi\to(\psi \to \chi)) & \to (\varphi\mathbin{\&}\psi \to \chi) \\ ((\varphi \to \psi) \to \chi) & \to (((\psi \to \varphi)\to \chi)\to \chi) \\ \overline{0}& \to\varphi \\ \end{align} $$

推理规则只有 **肯定前件**：由 $\varphi$ 与 $\varphi \to \psi$ 推出 $\psi$。若在这个系统里能从 $\Gamma$ 证明 $\varphi$——也就是有一个以 $\varphi$ 结尾的有限公式序列，其中每一项或是公理实例、或是 $\Gamma$ 的元素、或由前面各项按 **肯定前件** 得出——就记作 $\Gamma \vdash_\mathrm{MTL} \varphi$。这套希尔伯特式系统是 MTL 的强完全（有穷）公理化：对每个前提集 $\Gamma$，$\Gamma \models_\mathrm{MTL} \varphi$ 当且仅当 $\Gamma \vdash_\mathrm{MTL} \varphi$。已知 $\mathrm{MTL}$ 的有效性问题可判定，但计算复杂性还未定。

## 3 Łukasiewicz 逻辑

Łukasiewicz 逻辑是在 MTL 的希尔伯特式证明系统中加入 Wajsberg 公理 $$((\varphi \to \psi) \to \psi) \to ((\psi \to \varphi) \to \varphi)$$ 得到的。它对应的是按 Łukasiewicz t-范数赋值所定义后承关系的有穷版本：对每个 **有限** 公式集 $\Gamma$ 和每个公式 $\varphi$，$\Gamma \models_{Ł} \varphi$ 当且仅当 $\Gamma \vdash_{Ł} \varphi$。[^note-2]

这是多值逻辑的早期例子：Jan Łukasiewicz 与 Alfred Tarski（1930）在模糊集合论问世之前很久就提出了它，用的是等价公理系统，推理规则只有 **肯定前件**：

$$ \begin{align} \varphi &\to (\psi \to \varphi)\\ (\varphi \to \psi) &\to ((\psi \to \chi) \to (\varphi \to \chi))\\ ((\varphi \to \psi) \to \psi) &\to ((\psi \to \varphi) \to \varphi)\\ (\neg \psi \to \neg \varphi) &\to (\varphi \to \psi)\\ ((\varphi \to \psi) &\to (\psi \to \varphi)) \to (\psi \to \varphi). \end{align} $$

Łukasiewicz 逻辑是唯一的基于 t-范数的模糊逻辑：其中所有联结词——包括由 $x \Rightarrow_{Ł} y=\min\{1,1-x+y\}$ 给出的蕴涵——都由连续函数解释。McNaughton 定理（1951）说，在 [0,1] 上解释 Łukasiewicz 逻辑公式的实值函数，正好是整系数的连续分段线性函数。论计算复杂性，它的有效性问题渐近地不比经典逻辑糟：仍是 coNP 完全的。

## 4 Gödel–Dummett 逻辑

Gödel–Dummett 逻辑又叫 Dummett 的 LC，或简称 Gödel 逻辑，也是真值取在 $[0,1]$ 中的早期多值逻辑。Michael Dummett（1959）把它作为直觉主义逻辑加公理 $$(\varphi \to \psi) \lor (\psi \to \varphi)$$ 的扩张提出。这条公式在底层语义（无论 Kripke 式还是代数式）中强制一个线性序；它也出现在 Kurt Gödel 的观察里：直觉主义逻辑不可能用有穷真值表刻画（Gödel 1932）[^gödel-1932]。在模糊逻辑中，Gödel–Dummett 逻辑也可以由 MTL 加公理 $\varphi \to \varphi \mathbin{\&} \varphi$ 得到，这等于要求 $\&$ 幂等，于是两个合取的解释重合。语义上，它还可定义为最小 t-范数给出的后承关系。它的特别之处是：在基于 t-范数的逻辑里，只有它使得公式在给定赋值下的有效性不取决于命题变元的具体取值，而只取决于这些值的相对顺序；因此可以说，Gödel–Dummett 逻辑是关于比较真值的逻辑。和 Łukasiewicz 逻辑一样，检验有效性的计算复杂性仍是 coNP 完全的。

## 5 其他值得注意的模糊逻辑

除了 MTL（所有左连续 t-范数的逻辑）以及 Łukasiewicz、Gödel–Dummett 逻辑（各由某个特定 t-范数诱导），还可以考虑由一组 t-范数 **诱导** 的逻辑，或更一般地，MTL 的任意公理化扩张。特别地，所有 **连续** t-范数的逻辑，即 Hájek 的基本模糊逻辑 BL，就是 MTL 加公理 $$\varphi\mathbin{\&}(\varphi\to{{\psi}}) \to \psi\mathbin{\&}(\psi\to\varphi)$$ 得到的。事实上，任何一组连续 t-范数，其对应逻辑都有有穷公理化（Esteva, Godo, & Montagna 2003; Haniková 2014）[^esteva-2003][^esteva-2003-2][^haniková-2014]；多数情况下，公理化刻画的是从 **有限** 前提集出发的语义后承。第三个著名连续 t-范数（代数乘积）的逻辑叫乘积逻辑，是 BL 加公理 $$\neg\varphi \vee ((\varphi\to\varphi\mathbin{\&}{{\psi}})\to{{\psi}})$$ 的扩张。反过来，并非 MTL 的每个公理化扩张都能有基于 t-范数的语义：比如经典逻辑可公理化为 MTL $+$ $\varphi\vee\neg \varphi$，但排中律在任何基于 t-范数的解释下都不是重言式。

也有理由考虑更弱的模糊逻辑。比如可以说，逼着合取 & 的解释成为 t-范数的那些假设太强了。尤其是“$1$ 是单位元”这条，就逼着重言式只能是始终取值 $1$ 的公式、后承关系只能是值 $1$ 的保持，也就是把 $1$ 当成语义里唯一的 **指定值**。[^note-3] 要引入有多个指定真值度的逻辑，办法之一是让 & 的解释以某个数 $t <1$ 为单位元。可以证明，这时指定真值度正好是大于或等于 $t$ 的那些值。这种合取解释叫 *uninorm*。左连续 uninorm 的逻辑由 Metcalfe & Montagna（2007）公理化。

同理，也有人反对 & 可交换，甚至反对它可结合。所得逻辑的公理化文献里有（见 Cintula, Horčík, & Noguera 2013; Jenei & Montagna 2003）[^cintula-2013]；例外是非交换 uninorm 的逻辑，目前还没有已知的自然公理系统。

最后，模糊逻辑和经典逻辑不同，通常不是函项完全的，所以可以加新联结词来增强表达力。最常加的有：对每个有理数 $r\in (0,1)$ 的真常项 $\bar r$；一元联结词 $\sim$ 与 $\triangle$，前者解释为 ${\sim}x = 1-x$，后者在 $x=1$ 时取 $\triangle x = 1$、否则取 $0$；二元联结词 $\odot$，解释为通常的代数乘积；等等（Baaz 1996; Esteva, Gispert, Godo, & Noguera 2007; Esteva, Godo, & Montagna 2001; Esteva, Godo, Hájek, & Navara 2000）[^baaz-1996][^esteva-2007][^esteva-2001][^esteva-2000][^esteva-2001-2][^godo-2000][^hájek-2000][^montagna-2001]。

本节提到的各类命题模糊逻辑（及其一般理论），详尽综述见 *Handbook of Mathematical Fuzzy Logic*（3 卷，Cintula et al. 2011a,b, 2015）[^cintula-2015][^cintula-2011a]。

## 6 谓词逻辑

命题逻辑 MTL 可以在一阶谓词语言 $\mathcal{P\!L}$（定义同经典情形）中给出一阶对应物 MTL$\forall$。语义由结构给出：谓词符号解释为把论域元素元组映到真值的函数。确切地说，给定左连续 t-范数 $\ast$，一个 $\ast$-结构 ${\mathbf M}$ 包括：非空元素域 $M$；对每个 $n$ 元函数符号 $f\in \mathcal{P\!L}$ 的一个函数 $f_{\mathbf M}\colon M^n\to M$；对每个 $n$ 元谓词符号 $P\in \mathcal{P\!L}$ 的一个函数 $P_{\mathbf M}\colon M^n\to [0,1]$。把对象变元在 $M$ 中的赋值 ${\mathrm v}$ 固定下来，就能定义项的值（$\|f(t_1,\dots,t_n)\|^{\mathbf M}_{\mathrm v} = f_{\mathbf M}(\|t_1\|^{\mathbf M}_{\mathrm v},\dots,\|t_n\|^{\mathbf M}_{\mathrm v})$）和原子公式的真值（$\|P(t_1,\dots,t_n)\|^{\mathbf M}_{\mathrm v} = P_{\mathbf M}(\|t_1\|^{\mathbf M}_{\mathrm v},\dots,\|t_n\|^{\mathbf M}_{\mathrm v})$）。全称或存在量化公式的真值，取公式各实例真值的下确界或上确界，量化变元遍历域 $M$ 的全部元素。形式地：$$ \begin{align} \|\forall x\, \varphi\|^{\mathbf M}_{\mathrm v} & = \inf\{\|\varphi\|^{\mathbf M}_{{\mathrm v}[x{:}a]} \mid a\in M\}\\ \|\exists x\,\varphi\|^{\mathbf M}_{\mathrm v} & = \sup\{\|\varphi\|^{\mathbf M}_{{\mathrm v}[x{:}a]}\mid a\in M\},\\ \end{align} $$ 其中 ${\mathrm v}[x{:}a]$ 是把 $x$ 送到 $a$、其余变元保持不变的赋值。其他公式的值照命题语义算：$\&$ 解释为 $\ast$，蕴涵 $\to$ 解释为其剩余 $\Rightarrow_\ast$，$\land$ 与 $\overline{0}$ 分别解释为 $\min$ 与 $0$。

一阶逻辑 MTL$\forall$ 的后承关系，定义为在 $\ast$-结构中保持完全真（值 $1$），其中 $\ast$ 遍历所有左连续 t-范数。更确切地说，称一阶公式 $\varphi$ 是公式集 $\Gamma$ 的后承（记作 $\Gamma \models_{\mathrm{MTL}\forall} \varphi$），如果对每个左连续 t-范数 $\ast$ 和每个 $\ast$-结构 ${\mathbf M}$，只要 $\|\psi\|^{\mathbf M}_{\mathrm v} = 1$ 对所有赋值 v 与所有 $\psi \in \Gamma$ 成立，就有 $\|\varphi\|^{\mathbf M}_{\mathrm v} = 1$ 对所有赋值 v 成立。

MTL$\forall$ 可以写成强完全的希尔伯特式证明系统，公理如下：

- (P) MTL 公理的一阶实例
- $(\forall1 )$ $\forall x\,\varphi(x)\to\varphi(t)$，其中项 $t$ 在 $\varphi$ 中可代入 $x$
- $(\exists1)$ $\varphi(t)\to \exists x\, \varphi(x)$，其中项 $t$ 在 $\varphi$ 中可代入 $x$
- $(\forall2)$ $\forall x\,(\chi\to\varphi)\to(\chi\to \forall x\,\varphi)$，其中 $x$ 在 $\chi$ 中不自由
- $(\exists2)$ $\forall x\,(\varphi\to\chi)\to(\exists x\,\varphi\to\chi)$，其中 $x$ 在 $\chi$ 中不自由
- $(\forall3)$ $\forall x\,(\chi\vee\varphi)\to\chi\vee \forall x\,\varphi$，其中 $x$ 在 $\chi$ 中不自由。

MTL$\forall$ 的推理规则，是 **肯定前件** 再加 **概括规则**：由 $\varphi$ 推出 $\forall x\,\varphi$。

给其他基于 t-范数的命题模糊逻辑配一阶对应物，有两条路。第一条是把 MTL$\forall$ 的公理化扩一扩，加入前几节那些命题公理的一阶实例，于是得到 Łukasiewicz 逻辑、Gödel–Dummett 逻辑、乘积逻辑、Hájek 基本模糊逻辑 BL 等的一阶变体的句法呈现。第二条是改动 MTL$\forall$ 的语义定义，改为由相应 t-范数（集合）给出后承关系。接下来自然要问：每种情形下，这两条路是否通向同一个逻辑（MTL 就是如此）？可靠性不成问题，因为这些公理系统相对于相应结构类很容易验证可靠；完全性则没有一般答案，只能一案一议。

对 Gödel–Dummett 逻辑，公理系统相对于其语义是强完全的。但 Łukasiewicz 逻辑的语义重言式集合，正如 Bruno Scarpellini（1962）所证明的，不是递归可公理化的；Emil Ragaz（1981）进一步证明，它在算术层级意义上是 $\Sigma_2$-完全的。乘积逻辑和 Hájek 基本模糊逻辑 BL 更糟：由连续 t-范数给出的所有结构，其一阶重言式集合与真正的算术一样复杂（Montagna 2001）[^montagna-2001]。要得到完全性，可以给希尔伯特式证明系统加合适的无穷推理规则——Louise Hay（1963）对 Łukasiewicz 逻辑就是这么做的——或者推广真值集合（见下一节）。

更弱的模糊逻辑的一阶对应物，也可照样从句法、语义两方面研究；综述见 Cintula, Horčík, & Noguera 2014。

## 7 代数语义

研究模糊逻辑的一大工具是代数语义。粗略说，就是把实数单位区间换成任意一个集合，把联结词解释成该集合上相应元数的运算。

Francesc Esteva 与 Lluís Godo（2001）引入的 MTL-代数，是一个元组 ${\mathbf A} = \langle A, \&, \to, \wedge, \vee, \overline{0}, \overline{1} \rangle$，满足：

- $\langle A, \wedge, \vee, \overline{0}, \overline{1} \rangle$ 是有界格
- $\langle A, \&, \overline{1} \rangle$ 是可交换幺半群
- $(x\to y)\vee(y\to x) = \overline{1}$
- $x\mathbin{\&} y \leq z$ 当且仅当 $x \leq y\to z$（$\leq$ 是由 $\wedge$ 或 $\vee$ 诱导的格序）。

若格序是全序，${\mathbf A}$ 就叫 MTL-链。值得一提的是，MTL-代数是剩余格的一个子簇，而剩余格正是子结构逻辑的代数语义所在——这是这两族逻辑紧密相关的最早线索。

MTL-代数是上述基于 t-范数语义的推广，给 MTL 提供了可靠且完全的语义。[^note-4]

MTL-链是整个代数类的基本构件：每个 MTL-代数都能分解成链的 **次直积**。这意味着该逻辑相对于 MTL-链语义也完全；证明它相对于基于 t-范数语义完全时，第一步靠的就是这一点（Jenei & Montagna 2002）[^jenei-2002]。

代数语义是命题逻辑的通用工具。文献里研究的任何模糊逻辑——甚至不支持基于 t-范数语义的，如有穷值模糊逻辑或非交换 uninorm 的逻辑——都能找到相应的代数类，且可分解为链的次直积。有鉴于此，Libor Běhounek 与 Petr Cintula（2006）提议把模糊逻辑定义为相对于全序代数结构完全的逻辑。

代数语义用在一阶模糊逻辑上相当直接：把上一节 $\ast$-结构的定义改一下，不用区间 [0,1] 和 $\ast$ 及其剩余，而用任意 MTL-链及其运算来算公式真值。给定一个命题模糊逻辑，这套推广语义就能给出递归可枚举的重言式集合，以及相应一阶希尔伯特式证明系统的强完全性定理。

## 8 证明论

给模糊逻辑找分析型证明系统，一直是个不小的挑战。这类系统有些重要特征与 Gentzen 为经典逻辑、直觉主义逻辑建立的矢列演算相同，比如切消性和子公式性质（见“证明论的发展”词条）。Arnon Avron（1991）为 Gödel–Dummett 逻辑引入超矢列演算，是个重大突破。超矢列演算从矢列演算变来：推理规则指涉的是矢列的有限多重集，而不是单个矢列。在元层面，超矢列读作矢列的析取。这样一来，添加额外矢列（外弱化），或在同一个超矢列里把某矢列的多份拷贝换成一份（外收缩），都是可靠的。就 Gödel–Dummett 逻辑说，引入逻辑联结词的规则只需在 Gentzen 直觉主义矢列演算的规则上，给上下矢列各加侧超矢列。例如，右侧引入合取的矢列规则 $$\frac{\Gamma_1 \Rightarrow \phi \hspace{3ex} \Gamma_2 \Rightarrow \psi}{\Gamma_1,\Gamma_2 \Rightarrow \phi \wedge \psi}$$ 其中 $\Gamma_1$ 与 $\Gamma_2$ 是有限公式序列，变成这样的超矢列规则：$$\frac{H \mid \Gamma_1 \Rightarrow \phi \hspace{3ex} H' \mid \Gamma_2 \Rightarrow \psi}{H \mid H' \mid \Gamma_1,\Gamma_2 \Rightarrow \phi \wedge \psi }$$ 其中 $H$、$H'$ 是侧超矢列，即以析取方式附加到所示矢列上的有限矢列多重集。光这一步并不改变相应逻辑（这里是直觉主义逻辑）。真正新增的关键结构规则，是所谓通信规则：$$\frac{H \mid \Gamma_1,\Pi_1 \Rightarrow \Delta_1 \hspace{3ex} H' \mid \Gamma_2,\Pi_2 \Rightarrow \Delta_2}{H \mid H' \mid \Gamma_1,\Gamma_2 \Rightarrow \Delta_1 \mid \Pi_2,\Pi_2 \Rightarrow \Delta_2}$$ 这里 $\Gamma_1, \Gamma_2,\Pi_1, \Pi_2$ 是有限公式序列；$\Delta_1$、$\Delta_2$ 或是单个公式，或为空；$H$、$H'$ 仍是侧超矢列。为看清通信规则的作用，下面给出关键公理 $(\varphi \to \psi) \lor (\psi \to \varphi)$ 的推导，通信规则就用在初始（超）矢列的正下方：$$ \frac{\displaystyle\frac{\displaystyle\frac{\displaystyle\frac{\displaystyle\frac{\displaystyle\frac{\varphi \Rightarrow \varphi \hspace{5ex} \psi \Rightarrow \psi}{\varphi \Rightarrow \psi \mid \psi \Rightarrow \varphi}}{\Rightarrow \varphi \to \psi \mid \psi \Rightarrow \varphi}}{\Rightarrow \varphi \to \psi \mid\, \Rightarrow \psi \to \varphi}}{\Rightarrow (\varphi \to \psi) \vee (\psi \to \varphi) \mid\, \Rightarrow \psi \to \varphi}}{\Rightarrow (\varphi \to \psi) \vee (\psi \to \varphi) \mid\, \Rightarrow (\varphi \to \psi) \vee (\psi \to \varphi)}}{\Rightarrow (\varphi \to \psi) \lor (\psi \to \varphi)} $$

要给基本模糊逻辑 MTL 配超矢列演算，就得把通信规则加到无收缩版直觉主义逻辑（结构逻辑里研究得很透的例子）的矢列系统上。其他模糊逻辑——尤其是 Łukasiewicz 逻辑——的分析型证明系统，则要更彻底地背离传统演算：超矢列里的矢列成分得按不同于直觉主义、经典矢列的方式来解释。此外还有标签证明系统和各种表列演算。研究现状的详细介绍，见 Metcalfe, Olivetti, & Gabbay 2008 以及 Metcalfe 2011。

## 9 为真值函项性提供辩护的语义

把中间真值以及相应逻辑联结词的含义，同含模糊、不精确概念的推理的基本模型挂起钩来，很有好处：不只是哲学上有意义，也能更好把握模糊逻辑的应用前景。为此已提出若干语义，替特定的真值函项联结词选择作辩护；这里只简述两个。

投票语义的想法是：不同的行动者（投票者）可以融贯地对同一命题给出不同判断。把接受命题 $\varphi$ 为真的人所占比例看作真值。若不加限制，这得不到真值函项语义，只会给命题指派概率。但若给每个行动者定一个固定的 **怀疑水平**，再加一些自然条件，使他们对逻辑复合陈述的判断与这些水平相容，就能把 $\min$、$\max$、$1-x$ 分别还原为合取、析取、否定的真值函项。细节见 Lawry 1998。

Robin Giles（1974）提出另一个有趣的推理模型，能为 Łukasiewicz 逻辑的全部命题联结词提供辩护。这是一场博弈：两个玩家（我和“你”）按下面这类规则，把逻辑复合的断言（公式）一步步化归为更简单的断言：

- 我若断言 $\varphi \lor \psi$，就必须断言 $\varphi$ 或 $\psi$。
- 我若断言 $\varphi \land \psi$，就由你挑一个合取项，我相应地断言 $\varphi$ 或 $\psi$。
- 我若断言 $\varphi \to \psi$，那么你一旦断言 $\varphi$，我就得断言 $\psi$。

量化陈述的规则要预设一个固定域，并假定每个域元素都有约定的常项符号：

- 我若断言 $\forall x\, \varphi(x)$，就得对由你选定的常项 $c$ 断言 $\varphi(c)$。
- 我若断言 $\exists x\, \varphi(x)$，就得对由我自己选定的常项 $c$ 断言 $\varphi(c)$。

关于你方断言的规则与此对偶。博弈每走一步，就从你或我的当前断言多重集里挑一个非原子公式的出现，按上述规则换成子公式，直到只剩原子断言。最后的博弈状态按下注方案来评估。

每个原子公式都对应一个实验：它可能成功，也可能失败，还可能有分散性，即重复做会给出不同结果。每个实验、因而每个原子公式，都定一个固定的失败概率，叫风险值。玩家每有一个原子断言对应的实验失败，就要付给对方 $\$$1。若博弈从我的断言 $\varphi$ 开始、双方都理性行事，可以证明我的期望总损失，等于在 Łukasiewicz 逻辑的某个解释下 $\varphi$ 真值的倒数；这个解释把风险值的倒数指派给原子公式。特别地，公式在 Łukasiewicz 逻辑中有效，当且仅当无论风险值怎么指派，我都有策略保证博弈结束时期望总损失不大于 $0$。

Christian Fermüller 与 George Metcalfe（2009）指出，Giles 博弈的最优策略，与 Łukasiewicz 逻辑超矢列系统中的无切证明相对应。Fermüller & Roschger 2014 又把该博弈推广，用来刻画各种（半）模糊量词，以便为“大约一半”“几乎所有”这类自然语言说法建模。

Jeff Paris（2000）综述了支持各种真值函项选择的其他语义，尤其是重随机化语义（Hisdal 1988）[^hisdal-1988]、相似性语义（如 Ruspini 1991）[^ruspini-1991]、可接受性语义（Paris 1997）[^paris-1997] 与近似语义（Paris 2000）[^paris-2000]。Běhounek 2009 提出的基于资源的语义也值得一提。另外，除上文概述的 Giles 为 Łukasiewicz 逻辑设计的博弈，各种模糊逻辑还有不同形式的评估博弈；Fermüller 2015 对这类语义博弈作了综述。

## 10 模糊逻辑与模糊性

人们常说，引入模糊逻辑的主要动机，是要为含模糊谓词、模糊命题的推理建模。模糊性理论不少，但一般认为，容易陷入堆垛悖论是模糊性的主要特征。看下面这个悖论版本：

- (1)$10^{100}$ 是个巨大的数。
- (2)若 $n$ 是巨大的数，则 $n-1$ 也是巨大的数。

乍看之下，接受这两个假设并不算不合理。把 (2) 里的 $n$ 换成 $10^{100}$，再拿 (1) 作另一前提用 **肯定前件**，就推出 $10^{100}-1$ 是巨大的。照这样一路推下去，便得到不合理的陈述

- (3)$0$ 是个巨大的数。

模糊逻辑对 **堆垛悖论** 给出一种分析，照顾到这样一个直觉：陈述 (2) 虽然算不上完全真，但几乎是真的。

在基于 t-范数的模糊逻辑里，有好几种办法给这种推理建模并消解悖论。比如可以规定：只要结论的真值度不低于其前提强合取的真值度，任何 **肯定前件** 实例都算可靠。[^note-5] 如前所说，规定 (2) 的每个实例都以 $1-\epsilon$ 的程度为真，$\epsilon$ 是某个很小的数。这样，即便宣布 (1) 完全真，“$10^{100}-1$ 也是巨大的”仍可能不是完全真，而实例化和 **肯定前件** 的可靠性并不受损。再者，若两个不完全真（也不完全假）的陈述，其合取的真值度低于任一合取项，我们就可以放心宣布 (3) 完全假，同时仍坚持推理链每一步都可靠。通俗地说，悖论之所以消失，是因为把一个完全巨大的数反复减去一小点，就越来越说不上所得的数“也是巨大的”了。

Hájek & Novák 2003 另提出一种基于真值度的 **堆垛悖论** 解法：引入一个新联结词，替“几乎可以说是”这一说法建模。这样，他们就在合适的基于 t-范数的模糊逻辑里，用公理理论形式化了 **堆垛** 式推理。

Nicholas J.J. Smith（2005、2008）主张，模糊性的本质就在所谓 **接近原则** 里：关于不可区分对象的同形式陈述，在真值上应当彼此接近。许多借助模糊逻辑处理堆垛悖论的进路，其标志之一正是与该原则相容。[^note-6]

## 脚注

[^note-1]: 要注意，真值函项性意味着真值度不能解释为概率或信念度，因为后者不是按函项方式结合的：“明天中午出太阳、午夜下雨”的概率，并不（只）由这两个事件的概率决定，因为它们一般并不独立。

[^note-2]: 这个等价对于无限前提集不成立。不过也许出人意料，一般的后承关系仍是通常意义上的紧致：只要每个有限子集都可满足，无限公式集就可满足——也就是存在一个赋值，把其中所有公式都赋值为 $1$。

[^note-3]: 这从剩余性质加上一个直觉推得：蕴涵为真，当且仅当其后续真值不低于前件。确实：$x\leq y$ 当且仅当 $x \ast 1 \leq y$ 当且仅当 $1 \leq x\Rightarrow y$ 当且仅当 $x\Rightarrow y = 1$。

[^note-4]: 设代数 $\mathbf A$ 的域为 [0,1]，$\wedge, \vee, \overline{0}, \overline{1}$ 分别是 $\min$, $\max$, $0$, $1$；则它是 MTL-代数，当且仅当 $\&$ 是左连续 t-范数、$\to$ 是其剩余。任取 MTL-代数 $\mathbf A$，把赋值定义为公式到 $\mathbf A$ 的同态，便可像对 MTL 那样引入后承关系 $\models_{\mathbf A}$，即保持指定值 $\overline{1}$。于是对每个 MTL-代数 $\mathbf A$，$\Gamma\vdash_\mathrm{MTL}\varphi$ 当且仅当 $\Gamma\models_{\mathbf A}\varphi$。

[^note-5]: 这等于要求 $\varphi \mathbin{\&} (\varphi \to \psi) \to \psi$ 是重言式；在通常的模糊逻辑里，它确实是。

[^note-6]: 基于 Łukasiewicz 逻辑、所有联结词都有连续真值函项的表述，尤其如此。但要注意，接近原则大概与 Gödel 逻辑这类模糊逻辑不相容：后者只看真值的相对 *顺序*，不管它们之间的度量距离。

## References（引用注释）

**以下文献从原文照录，不作翻译；中国文献译为中文。**

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

[^supplementary-nd]: Supplementary document:
[^bibliography-nd]: [Bibliography Sorted by Topic](logic-fuzzy.readings-by-topic.md)
[^aguzzoli-2011]: Aguzzoli, Stefano, Simone Bova, and Brunella Gerla, 2011, “Free algebras and functional representation for fuzzy logics”, in Cintula, Petr, Petr Hájek, and Carles Noguera (eds.), *Handbook of Mathematical Fuzzy Logic*, Volume 2, (Mathematical Logic and Foundations, Volume 38), London: College Publications, pages 713–791.
[^avron-1991]: Avron, Arnon, 1991, “Hypersequents, Logical Consequence and Intermediate Logics for Concurrency”, *Annals of Mathematics and Artificial Intelligence*, 4(3–4): 225–248. doi:10.1007/BF01531058
[^baaz-1996]: Baaz, Matthias, 1996, “Infinite-Valued Gödel Logic with 0–1-Projections and Relativisations”, in Hájek, Petr (ed.), *Gödel’96: Logical Foundations of Mathematics, Computer Science, and Physics*, (Lecture Notes in Logic, Volume 6), Brno: Springer, pages 23–33.
[^baaz-2002]: Baaz, Matthias, Petr Hájek, Franco Montagna, and Helmut Veith, 2002, “Complexity of T-Tautologies”, *Annals of Pure and Applied Logic*, 113(1–3): 3–11.
[^baaz-2011]: Baaz, Matthias and Norbert Preining, 2011, “Gödel–Dummett Logics”, in Cintula, Petr, Petr Hájek, and Carles Noguera (eds.), *Handbook of Mathematical Fuzzy Logic*, Volume 2, (Mathematical Logic and Foundations, Volume 38), London: College Publications, pages 585–625.
[^badia-2021]: Badia, Guillermo and Carles Noguera, 2021, “Lindström theorems in graded model theory”, *Annals of Pure and Applied Logic*, 172(3): 102916. doi: 10.1016/j.apal.2020.102916
[^badia-2021-2]: –––, 2021, “A General Omitting Types Theorem in Mathematical Fuzzy Logic”, *IEEE Transactions on Fuzzy Systems*, 29(6): 1386–1394. doi: 10.1109/TFUZZ.2020.2975146
[^běhounek-2009]: Běhounek, Libor, 2009, “Fuzzy Logics Interpreted as Logics of Resources”, in Peliš, Michal (ed.), *The Logica Yearbook 2008*, London: College Publications, pages 9–21.
[^běhounek-2014]: –––, 2014, “In Which Sense Is Fuzzy Logic a Logic For Vagueness?”, in Łukasiewicz, Thomas, Rafael Peñaloza, and Anni-Yasmin Turhan (eds.), *PRUV 2014: Logics for Reasoning About Preferences, Uncertainty, and Vagueness*, (CEUR Workshop Proceedings, Volume 1205), Dresden: CEUR.
[^běhounek-2005]: Běhounek, Libor and Petr Cintula, 2005, “Fuzzy Class Theory”, *Fuzzy Sets and Systems*, 154(1): 34–55.
[^běhounek-2006]: –––, 2006, “Fuzzy Logics as the Logics of Chains”, *Fuzzy Sets and Systems*, 157(5): 604–610.
[^běhounek-2014-2]: Běhounek, Libor and Zuzana Haniková, 2014, “Set Theory and Arithmetic in Fuzzy Logic”, in Montagna, Franco (ed.), *Petr Hájek on Mathematical Fuzzy Logic*, (Outstanding Contributions to Logic, Volume 6), Cham: Springer, pages 63–89.
[^bělohlávek-2017]: Bělohlávek, Radim, Joseph W. Dauben, and George J. Klir, 2017, *Fuzzy Logic and Mathematics: A Historical Perspective*, Oxford: Oxford University Press. doi:10.1093/oso/9780190200015.001.0001
[^bělohlávek-2005]: Bělohlávek, Radim and Vilém Vychodil, 2005, *Fuzzy Equational Logic*, (Studies in Fuzziness and Soft Computing, Volume 186), Berlin and Heidelberg: Springer.
[^bobillo-2015]: Bobillo, Fernando, Marco Cerami, Francesc Esteva, Àngel García-Cerdaña, Rafael Peñaloza, and Umberto Straccia, 2015, “Fuzzy Description Logics”, in Cintula, Petr, Christian G. Fermüller, and Carles Noguera (eds.), *Handbook of Mathematical Fuzzy Logic*, Volume 3, (Mathematical Logic and Foundations, Volume 58), London: College Publications, pages 1105–1181.
[^bou-2011]: Bou, Félix, Francesc Esteva, Lluís Godo, and Ricardo Oscar Rodríguez, 2011, “On the Minimum Many-Valued Modal Logic Over a Finite Residuated Lattice”, *Journal of Logic and Computation*, 21(5): 739–790.
[^busaniche-2011]: Busaniche, Manuela and Franco Montagna, 2011, “Hájek’s Logic BL and BL-Algebras”, in Cintula, Petr, Petr Hájek, and Carles Noguera (eds.), *Handbook of Mathematical Fuzzy Logic*, Volume 1, (Mathematical Logic and Foundations, Volume 37), London: College Publications, pages 355–447.
[^ciabattoni-2012]: Ciabattoni, Agata, Nikolaos Galatos, and Kazushige Terui, 2012, “Algebraic Proof Theory for Substructural Logics: Cut-Elimination and Completions”, *Annals of Pure and Applied Logic*, 163(3): 266–290.
[^caicedo-2017]: Caicedo, Xavier, George Metcalfe, Ricardo Oscar Rodríguez, and Jonas Rogger, 2017, “Decidability of order-based modal logics”, *Journal of Computer and System Sciences*, 88: 53–74. doi:10.1016/j.jcss.2017.03.012
[^caicedo-2010]: Caicedo, Xavier and Ricardo Oscar Rodríguez, 2010, “Standard Gödel Modal Logics”, *Studia Logica*, 94(2): 189–214.
[^caicedo-2015]: –––, 2015, “Bi-modal Gödel logic over [0, 1]-valued Kripke frames”, *Journal of Logic and Computation*, 25(1): 37–55. doi: 10.1093/logcom/exs036
[^cicalese-2015]: Cicalese, Ferdinando and Franco Montagna, 2015, “Ulam–Rényi Game Based Semantics For Fuzzy Logics”, in Cintula, Petr, Christian G. Fermüller, and Carles Noguera (eds.), *Handbook of Mathematical Fuzzy Logic*, Volume 3, (Mathematical Logic and Foundations, Volume 58), London: College Publications, pages 1029–1062.
[^cignoli-1999]: Cignoli, Roberto, Itala M. D’Ottaviano, and Daniele Mundici, 1999, *Algebraic Foundations of Many-Valued Reasoning*, (Trends in Logic, Volume 7), Dordrecht: Kluwer.
[^cintula-2006]: Cintula, Petr, 2006, “Weakly Implicative (Fuzzy) Logics I: Basic Properties”, *Archive for Mathematical Logic*, 45(6): 673–704.
[^cintula-2019]: Cintula, Petr, Denisa Diaconescu, and George Metcalfe, 2019, “Skolemization and Herbrand theorems for lattice-valued logics”, *Theoretical Computer Science*, 768: 54–75. doi: 10.1016/j.tcs.2019.02.007
[^cintula-2009]: Cintula, Petr, Francesc Esteva, Joan Gispert, Lluís Godo, Franco Montagna, and Carles Noguera, 2009, “Distinguished Algebraic Semantics for T-norm Based Fuzzy Logics: Methods and Algebraic Equivalencies”, *Annals of Pure and Applied Logic*, 160(1): 53–81.
[^cintula-2015]: Cintula, Petr, Christian G. Fermüller, and Carles Noguera (eds.), 2015, *Handbook of Mathematical Fuzzy Logic*, volume 3, (Studies in Logic, Volume 58), London: College Publications.
[^cintula-2011a]: Cintula, Petr, Petr Hájek, and Carles Noguera (eds.), 2011a, *Handbook of Mathematical Fuzzy Logic*, volume 1 (Studies in Logic, Volume 37), London: College Publications.
[^cintula-2011b]: ––– (eds.), 2011b, *Handbook of Mathematical Fuzzy Logic*, volume 2 (Studies in Logic, Volume 38), London: College Publications.
[^cintula-2013]: Cintula, Petr, Rostislav Horčík, Carles Noguera, 2013, “Non-Associative Substructural Logics and their Semilinear Extensions: Axiomatization and Completeness Properties”, *The Review of Symbolic Logic*, 6(3): 394–423. doi:10.1017/S1755020313000099
[^cintula-2014]: –––, 2014, “The Quest for the Basic Fuzzy Logic”, in Montagna, Franco (ed.), *Petr Hájek on Mathematical Fuzzy Logic*, (Outstanding Contributions to Logic, Volume 6), Cham: Springer, pages 245–290. doi:10.1007/978-3-319-06233-4_12
[^cintula-2019-2]: Cintula, Petr, Paula Menchón, and Carles Noguera, 2019, “Toward a general frame semantics for modal many-valued logics”, *Soft Computing*, 23(7): 2233–2241. doi: 10.1007/s00500-018-3369-5
[^cintula-2011]: Cintula, Petr and Carles Noguera, 2011, “A General Framework for Mathematical Fuzzy Logic”, in Cintula, Petr, Petr Hájek, and Carles Noguera (eds.), *Handbook of Mathematical Fuzzy Logic*, Volume 1, (Mathematical Logic and Foundations, Volume 37), London: College Publications, pages 103–207.
[^cintula-2009-2]: Cintula, Petr and George Metcalfe, 2009, “Structural Completeness in Fuzzy Logics”, *Notre Dame Journal of Formal Logic*, 50(2): 153–183.
[^dellunde-2012]: Dellunde, Pilar, 2012, “Preserving Mappings in Fuzzy Predicate Logics”, *Journal of Logic and Computation*, 22(6): 1367–1389.
[^dellunde-2018]: Dellunde, Pilar, Àngel García-Cerdaña, and Carles Noguera, 2018, “Back-and-forth systems for fuzzy first-order models”, *Fuzzy Sets and Systems*, 345: 83–98.
[^di-1986]: Di Nola, Antonio and Giangiacomo Gerla, 1986, “Fuzzy Models of First-Order Languages”, *Zeitschrift für Mathematische Logik und Grundlagen der Mathematik*, 32(19–24): 331–340.
[^dummett-1959]: Dummett, Michael, 1959, “A Propositional Calculus with Denumerable Matrix”, *Journal of Symbolic Logic*, 24(2): 97–106. doi:10.2307/2964753
[^esteva-2007]: Esteva, Francesc, Joan Gispert, Lluís Godo, and Carles Noguera, 2007, “Adding Truth-Constants to Logics of Continuous T-norms: Axiomatization and Completeness Results”, *Fuzzy Sets and Systems*, 158(6): 597–618. doi:10.1016/j.fss.2006.11.010
[^esteva-2001]: Esteva, Francesc and Lluís Godo, 2001, “Monoidal T-norm Based Logic: Towards a Logic for Left-Continuous T-norms”, *Fuzzy Sets and Systems*, 124(3): 271–288. doi:10.1016/S0165-0114(01)00098-7
[^esteva-2003]: Esteva, Francesc, Lluís Godo, and Àngel García-Cerdaña, 2003, “On the Hierarchy of T-norm Based Residuated Fuzzy Logics”, in Fitting, Melvin and Ewa Orłowska (eds.), *Beyond Two: Theory and Applications of Multiple-Valued Logic*, (Studies in Fuzziness and Soft Computing, Volume 114), Heidelberg: Springer, pages 251–272.
[^esteva-2000]: Esteva, Francesc, Lluís Godo, Petr Hájek, and Mirko Navara, 2000, “Residuated Fuzzy Logics with an Involutive Negation”, *Archive for Mathematical Logic*, 39(2): 103–124. doi:10.1007/s001530050006
[^esteva-2011]: Esteva, Francesc, Lluís Godo, and Enrico Marchioni, 2011, “Fuzzy Logics with Enriched Language”, in Cintula, Petr, Petr Hájek, and Carles Noguera (eds.), *Handbook of Mathematical Fuzzy Logic*, Volume 2, (Mathematical Logic and Foundations, Volume 38), London: College Publications, pages 627–711.
[^esteva-2001-2]: Esteva, Francesc, Lluís Godo, and Franco Montagna, 2001, “The $L\Pi$ and $L\Pi\frac12$ Logics: Two Complete Fuzzy Systems Joining Łukasiewicz and Product Logics”, *Archive for Mathematical Logic*, 40(1): 39–67. doi:10.1007/s001530050173
[^esteva-2003-2]: –––, 2003, “Axiomatization of Any Residuated Fuzzy Logic Defined by a Continuous T-norm”, in Taner Bilgiç, Bernard De Baets, and Okyay Kaynak (eds.), *Fuzzy Sets and Systems: IFSA 2003*, (Lecture Notes in Computer Science, Volume 2715), Berlin/Heidelberg: Springer, pages 172–179. doi:10.1007/3-540-44967-1_20
[^fedel-2011]: Fedel, Martina, Hykel Hosni, and Franco Montagna, 2011, “A Logical Characterization of Coherence for Imprecise Probabilities”, *International Journal of Approximate Reasoning*, 52(8): 1147–1170, doi: 10.1016/j.ijar.2011.06.004.
[^fermüller-2015]: Fermüller, Christian G., 2015, “Semantic Games for Fuzzy Logics”, Cintula, Petr, Christian G. Fermüller, and Carles Noguera (eds.), 2015, *Handbook of Mathematical Fuzzy Logic*, volume 3, (Studies in Logic, Volume 58), London: College Publications, pages 969–1028.
[^fermüller-2009]: Fermüller, Christian G. and George Metcalfe, 2009, “Giles’s Game and Proof Theory for Łukasiewicz Logic”, *Studia Logica*, 92(1): 27–61. doi:10.1007/s11225-009-9185-2
[^fermüller-2014]: Fermüller, Christian G. and Christoph Roschger, 2014, “Randomized Game Semantics for Semi-Fuzzy Quantifiers”, *Logic Journal of the Interest Group of Pure and Applied Logic*, 22(3): 413–439. doi:10.1093/jigpal/jzt049
[^flaminio-2011]: Flaminio, Tommaso, Lluís Godo, and Enrico Marchioni, 2011, “Reasoning About Uncertainty of Fuzzy Events: An Overview”, in Cintula, Petr, Christian G. Fermüller, Lluís Godo, and Petr Hájek(eds.), *Understanding Vagueness: Logical, Philosophical, and Linguistic Perspectives*, (Studies in Logic, Volume 36), London: College Publications, pages 367–400.
[^flaminio-2015]: Flaminio, Tommaso and Tomáš Kroupa, 2015, “States of MV-Algebras”, in Cintula, Petr, Christian G. Fermüller, and Carles Noguera (eds.), *Handbook of Mathematical Fuzzy Logic*, Volume 3, (Mathematical Logic and Foundations, Volume 58), London: College Publications, pages 1183–1236.
[^font-2016]: Font, Josep Maria, 2016, *Abstract Algebraic Logic: An Introductory Textbook*, (Mathematical Logic and Foundations, Volume 60), London: College Publications.
[^galatos-2007]: Galatos, Nikolaos, Peter Jipsen, Tomasz Kowalski, and Hiroakira Ono, 2007, *Residuated Lattices: An Algebraic Glimpse at Substructural Logics*, (Studies in Logic and the Foundations of Mathematics, Volume 151), Amsterdam: Elsevier.
[^garcía-cerdaña-2010]: García-Cerdaña, Àngel, Eva Armengol, and Francesc Esteva, 2010, “Fuzzy Description Logics and T-norm Based Fuzzy Logics”, *International Journal of Approximate Reasoning*, 51(6): 632–655.
[^gehrke-1997]: Gehrke, Mai, Carol L. Walker, and Elbert A. Walker, 1997, “A Mathematical Setting for Fuzzy Logics”, *International Journal of Uncertainty, Fuzziness, and Knowledge-Based Systems*, 5(3): 223–238. doi:10.1142/S021848859700021X
[^gerla-2001]: Gerla, Giangiacomo, 2001, *Fuzzy Logic—Mathematical Tool for Approximate Reasoning*, (Trends in Logic, Volume 11), New York: Kluwer and Plenum Press.
[^giles-1974]: Giles, Robin, 1974, “A Non-Classical Logic for Physics”, *Studia Logica*, 33(4): 397–415. doi:10.1007/BF02123379
[^gödel-1932]: Gödel, Kurt, 1932, “Zum intuitionistischen Aussagenkalkül”, *Anzeiger Akademie Der Wissenschaften Wien*, 69: 65–66.
[^godo-2000]: Godo, Lluís, Francesc Esteva, and Petr Hájek, 2000, “Reasoning About Probability Using Fuzzy Logic”, *Neural Network World*, 10(5): 811–823.
[^goguen-1969]: Goguen, Joseph A., 1969, “The Logic of Inexact Concepts”, *Synthese*, 19(3–4): 325–373.
[^gottwald-2001]: Gottwald, Siegfried, 2001, *A Treatise On Many-Valued Logics*, (Studies in Logic and Computation, Volume 9), Baldock: Research Studies Press Ltd.
[^hájek-1998]: Hájek, Petr, 1998, *Metamathematics of Fuzzy Logic*, (Trends in Logic, Volume 4), Dordrecht: Kluwer.
[^hájek-2001]: –––, 2001, “On Very True”, *Fuzzy Sets and Systems*, 124(3): 329–333.
[^hájek-2005]: –––, 2005, “Making Fuzzy Description Logic More General”, *Fuzzy Sets and Systems*, 154(1): 1–15.
[^hájek-2006]: Hájek, Petr and Petr Cintula, 2006, “On Theories and Models in Fuzzy Predicate Logics”, *Journal of Symbolic Logic*, 71(3): 863–880.
[^hájek-2003]: Hájek, Petr and Zuzana Haniková, 2003, “A Development of Set Theory in Fuzzy Logic”, in Fitting, Melvin and Ewa Orłowska (eds.), *Beyond Two: Theory and Applications of Multiple-Valued Logic*, (Studies in Fuzziness and Soft Computing, Volume 114), Heidelberg: Springer, pages 273–285.
[^hájek-2011]: Hájek, Petr, Franco Montagna, Carles Noguera, 2011, “Arithmetical Complexity of First-Order Fuzzy Logics”, in Cintula, Petr, Petr Hájek, and Carles Noguera(eds.), *Handbook of Mathematical Fuzzy Logic*, Volume 2, (Mathematical Logic and Foundations, Volume 38), London: College Publications, pages 853–908.
[^hájek-2003-2]: Hájek, Petr and Vilém Novák, 2003, “The Sorites Paradox and Fuzzy Logic”, *International Journal of General Systems*, 32(4): 373–383. doi:10.1080/0308107031000152522
[^hájek-2000]: Hájek, Petr, Jeff Paris, and John C. Shepherdson, 2000, “The Liar Paradox and Fuzzy Logic”, *Journal of Symbolic Logic*, 65(1): 339–346.
[^haniková-2011]: Haniková, Zuzana, 2011, “Computational Complexity of Propositional Fuzzy Logics”, in Cintula, Petr, Petr Hájek, and Carles Noguera (eds.), *Handbook of Mathematical Fuzzy Logic*, Volume 2, (Mathematical Logic and Foundations, Volume 38), London: College Publications, pages 793–851.
[^haniková-2014]: –––, 2014, “Varieties Generated by Standard BL-Algebras”, *Order*, 31(1): 15–33. doi:10.1007/s11083-013-9285-5
[^hansoul-2013]: Hansoul, Georges and Bruno Teheux, 2013, “Extending Łukasiewicz Logics with a Modality: Algebraic Approach to Relational Semantics”, *Studia Logica*, 101(3): 505–545, doi: 10.1007/s11225-012-9396-9.
[^hay-1963]: Hay, Louise Schmir, 1963, “Axiomatization of the Infinite-Valued Predicate Calculus”, *Journal of Symbolic Logic*, 28(1): 77–86. doi:10.2307/2271339
[^hisdal-1988]: Hisdal, Ellen, 1988, “Are Grades of Membership Probabilities?” *Fuzzy Sets and Systems*, 25(3): 325–348. doi:10.1016/0165-0114(88)90018-8
[^horčík-2011]: Horčík, Rostislav, 2011, “Algebraic Semantics: Semilinear FL-Algebras”, in Cintula, Petr, Petr Hájek, and Carles Noguera (eds.), *Handbook of Mathematical Fuzzy Logic*, Volume 1, (Mathematical Logic and Foundations, Volume 37), London: College Publications, pages 283–353.
[^horn-1969]: Horn, Alfred, 1969, “Logic with Truth Values in a Linearly Ordered Heyting Algebra”, *The Journal of Symbolic Logic*, 34(3): 395–408.
[^jenei-2002]: Jenei, Sándor and Franco Montagna, 2002, “A Proof of Standard Completeness for Esteva and Godo’s Logic MTL”, *Studia Logica*, 70(2): 183–192. doi:10.1023/A:1015122331293
[^jeřábek-2010]: Jeřábek, Emil, 2010, “Bases of Admissible Rules of Łukasiewicz Logic”, *Journal of Logic and Computation*, 20(6): 1149–1163.
[^jeřábek-2003]: –––, 2003, “A Proof of Standard Completeness for Non-Commutative Monoidal T-norm Logic”, *Neural Network World*, 13(5): 481–489.
[^klement-2000]: Klement, Erich Peter, Radko Mesiar, and Endre Pap, 2000, *Triangular Norms*, (Trends in Logic, Volume 8), Dordrecht: Kluwer.
[^lawry-1998]: Lawry, Jonathan, 1998, “A Voting Mechanism for Fuzzy Logic”, *International Journal of Approximate Reasoning*, 19(3–4): 315–333. doi:10.1016/S0888-613X(98)10013-0
[^leştean-2011]: Leştean, Ioana and Antonio Di Nola, 2011, “Łukasiewicz Logic and MV-Algebras”, in Cintula, Petr, Petr Hájek, and Carles Noguera (eds.), *Handbook of Mathematical Fuzzy Logic*, Volume 2, (Mathematical Logic and Foundations, Volume 38), London: College Publications, pages 469–583.
[^ling-1965]: Ling, Cho-Hsin, 1965, “Representation of Associative Functions”, *Publicationes Mathematicae Debrecen*, 12: 189–212.
[^jan-1920]: Łukasiewicz, Jan, 1920, “O Logice Trójwartościowej”, *Ruch Filozoficzny*, 5: 170–171. English translation, “On Three-Valued Logic”, in McCall, Storrs (ed.), 1967, *Polish Logic* *1920–1939*, Oxford: Clarendon Press, pages 16–18, and in Jan Łukasiewicz, 1970, *Selected Works*, Borkowski, Ludwik (ed.), Amsterdam: North-Holland, pages 87–88.
[^jan-1930]: Łukasiewicz, Jan and Alfred Tarski, 1930, “Untersuchungen über den Aussagenkalkül”, *Comptes Rendus Des Séances de La Société Des Sciences et Des Lettres de Varsovie, Cl. III*, 23(iii): 30–50.
[^marra-2013]: Marra, Vincenzo and Luca Spada, 2013, “Duality, Projectivity, and Unification in Łukasiewicz Logic and MV-Algebras”, *Annals of Pure and Applied Logic*, 164(3): 192–210.
[^mcnaughton-1951]: McNaughton, Robert, 1951, “A Theorem About Infinite-Valued Sentential Logic”, *Journal of Symbolic Logic*, 16(1): 1–13. doi:10.2307/2268660
[^metcalfe-2011]: Metcalfe, George, 2011, “Proof Theory for Mathematical Fuzzy Logic”, Cintula, Petr, Petr Hájek, and Carles Noguera (eds.), 2011a, *Handbook of Mathematical Fuzzy Logic*, volume 1 (Studies in Logic, Volume 37), London: College Publications, pages 209–282.
[^metcalfe-2007]: Metcalfe, George and Franco Montagna, 2007, “Substructural Fuzzy Logics”, *Journal of Symbolic Logic*, 72(3): 834–864. doi:10.2178/jsl/1191333844
[^metcalfe-2008]: Metcalfe, George, Nicola Olivetti, and Dov M. Gabbay, 2008, *Proof Theory for Fuzzy Logics*, (Applied Logic Series, Volume 36), Dordrecht: Springer Netherlands.
[^montagna-2001]: Montagna, Franco, 2001, “Three Complexity Problems in Quantified Fuzzy Logic”, *Studia Logica*, 68(1): 143–152. doi:10.1023/A:1011958407631
[^montagna-2010]: Montagna, Franco and Carles Noguera, 2010, “Arithmetical Complexity of First-Order Predicate Fuzzy Logics Over Distinguished Semantics”, *Journal of Logic and Computation*, 20(2): 399–424. doi:10.1093/logcom/exp052
[^montagna-2006]: Montagna, Franco, Carles Noguera, and Rostislav Horčík, 2006, “On Weakly Cancellative Fuzzy Logics”, *Journal of Logic and Computation*, 16(4): 423–450.
[^montagna-nd]: Montagna, Franco and Hiroakira Ono, “Kripke Semantics, Undecidability and Standard Completeness for Esteva and Godo’s Logic MTL$\forall$”, *Studia Logica*, 71(2): 227–245.
[^mostert-1957]: Mostert, Paul S. and Allen L. Shields, 1957, “On the Structure of Semigroups on a Compact Manifold with Boundary”, *The Annals of Mathematics, Second Series*, 65(1): 117–143. doi:10.2307/1969668
[^mundici-1987]: Mundici, Daniele, 1987, “Satisfiability in Many-Valued Sentential Logic is NP-Complete”, *Theoretical Computer Science*, 52(1–2): 145–153.
[^mundici-1992]: –––, 1992, “The Logic of Ulam’s Game with Lies”, in Bicchieri, Cristina and Maria Luisa Dalla Chiara (eds.), *Knowledge, Belief, and Strategic Interaction* (*Castiglioncello*, *1989*), Cambridge: Cambridge University Press, 275–284.
[^mundici-2011]: –––, 2011, *Advanced Łukasiewicz Calculus and MV-Algebras*, (Trends in Logic, Volume 35), New York: Springer.
[^novák-2004]: Novák, Vilém, 2004, “On Fuzzy Type Theory”, *Fuzzy Sets and Systems*, 149(2): 235–273.
[^novák-2015]: –––, 2015, “Fuzzy Logic with Evaluated Syntax”, in Cintula, Petr, Christian G. Fermüller, and Carles Noguera (eds.), *Handbook of Mathematical Fuzzy Logic*, Volume 3, (Mathematical Logic and Foundations, Volume 58), London: College Publications, pages 1063–1104.
[^novák-2000]: Novák, Vilém, Irina Perfilieva, and Jiří Močkoř, 2000, *Mathematical Principles of Fuzzy Logic*, Dordrecht: Kluwer.
[^nguyen-2005]: Nguyen, Hung T. and Elbert A. Walker, 2005, *A First Course in Fuzzy Logic* (third edition), Chapman and Hall/CRC.
[^paris-1997]: Paris, Jeff, 1997, “A Semantics for Fuzzy Logic”, *Soft Computing*, 1(3): 143–147. doi:10.1007/s005000050015
[^paris-2000]: –––, 2000, “Semantics for Fuzzy Logic Supporting Truth Functionality”, in Vilém Novák and Irina Perfilieva (eds.), *Discovering the World with Fuzzy Logic*, (Studies in Fuzziness and Soft Computing. Volume 57), Heidelberg: Springer, pages 82–104.
[^pavelka-1979]: Pavelka, Jan, 1979, “On Fuzzy Logic I, II, and III”, *Zeitschrift für Mathematische Logik und Grundlagen der Mathematik*, 25: 45–52, 119–134, and 447–464.
[^ragaz-1981]: Ragaz, Matthias Emil, 1981, *Arithmetische Klassifikation von Formelmengen der unendlichwertigen Logik* (PhD thesis), Swiss Federal Institute of Technology, Zürich. doi:10.3929/ethz-a-000226207
[^rodríguez-2021]: Rodríguez, Ricardo Oscar and Amanda Vidal, 2021, “Axiomatization of Crisp Gödel Modal Logic”, *Studia Logica*, 109(2): 367–395. doi: 10.1007/s11225-020-09910-5
[^ross-2016]: Ross, Timothy J., 2016, *Fuzzy Logic with Engineering Applications* (fourth edition), Hoboken, NJ: Wiley.
[^ruspini-1991]: Ruspini, Enrique H., 1991, “On the Semantics of Fuzzy Logic”, *International Journal of Approximate Reasoning*, 5(1): 45–88. doi:10.1016/0888-613X(91)90006-8
[^scarpellini-1962]: Scarpellini, Bruno, 1962, “Die Nichtaxiomatisierbarkeit des unendlichwertigen Prädikatenkalküls von Łukasiewicz”, *Journal of Symbolic Logic*, 27(2): 159–170. doi:10.2307/2964111
[^smith-2005]: Smith, Nicholas J.J., 2005, “Vagueness as Closeness”, *Australasian Journal of Philosophy*, 83(2): 157–183. doi:10.1080/00048400500110826
[^smith-2008]: –––, 2008, *Vagueness and Degrees of Truth*, Oxford: Oxford University Press.
[^smith-2015]: –––, 2015, “Fuzzy Logics in Theories of Vagueness”, in Cintula, Petr, Christian G. Fermüller, and Carles Noguera (eds.), *Handbook of Mathematical Fuzzy Logic*, Volume 3, (Mathematical Logic and Foundations, Volume 58), London: College Publications, pages 1237–1281.
[^straccia-1998]: Straccia, Umberto, 1998, “A Fuzzy Description Logic”, in Mostow, Jack and Chuck Rich (eds.), *Proceedings of the 15th National Conference on Artificial Intelligence (AAAI 1998)*, Menlo Park: AAAI Press, pages 594–599.
[^teheux-2016]: Teheux, Bruno, 2016, “Modal definability based on Łukasiewicz validity relations”, *Studia Logica*, 104(2): 343–363. doi: 10.1007/s11225-015-9643-y
[^takeuti-1984]: Takeuti, Gaisi and Satako Titani, 1984, “Intuitionistic Fuzzy Logic and Intuitionistic Fuzzy Set Theory”, *Journal of Symbolic Logic*, 49(3): 851–866.
[^takeuti-1992]: –––, 1992, “Fuzzy Logic and Fuzzy Set Theory”, *Archive for Mathematical Logic*, 32(1): 1–32.
[^vetterlein-2015]: Vetterlein, Thomas, 2015, “Algebraic Semantics: The Structure of Residuated Chains”, in Cintula, Petr, Christian G. Fermüller, and Carles Noguera (eds.), *Handbook of Mathematical Fuzzy Logic*, Volume 3, (Mathematical Logic and Foundations, Volume 58), London: College Publications, pages 929–967.
[^vidal-2021]: Vidal, Amanda, 2021, “On transitive modal many-valued logics”, *Fuzzy Sets and Systems*, 407: 97–114. doi: 10.1016/j.fss.2020.01.011
[^vidal-2017]: Vidal, Amanda, Francesc Esteva, and Lluís Godo, 2017, “On modal extensions of Product fuzzy logic”, *Journal of Logic and Computation*, 27(1): 299–336. doi: 10.1093/logcom/exv046
[^zadeh-1965]: Zadeh, Lotfi A., 1965, “Fuzzy Sets”, *Information and Control*, 8(3): 338–353. doi:10.1016/S0019-9958(65)90241-X
[^zadeh-1975]: –––, 1975, “Fuzzy logic and approximate reasoning”, *Synthese*, 30: 407–428. doi: 10.1007/BF00485052

## 学术工具

* [如何引用本词条](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=logic-fuzzy)。
* [预览本词条的 PDF 版本](https://leibniz.stanford.edu/friends/preview/logic-fuzzy/)，见 [SEP 学会之友](https://leibniz.stanford.edu/friends/)。
* 在 [InPhO](https://www.inphoproject.org/entity?sep=logic-fuzzy&redirect=True) 查找与本词条相关的话题与思想家。
* 在 [PhilPapers](https://philpapers.org/sep/logic-fuzzy/) 查看本词条的增强文献目录及其数据库链接。

## 其他网络资源

- Hajek, Petr, “Fuzzy Logic”, *The Stanford Encyclopedia of Philosophy* (Fall 2016 Edition), Edward N. Zalta (ed.), URL = <[https://plato.stanford.edu/archives/fall2016/entries/logic-fuzzy/](https://plato.stanford.edu/archives/fall2016/entries/logic-fuzzy/)>. [这是《斯坦福哲学百科全书》先前关于模糊逻辑的词条——见[版本历史](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=logic-fuzzy)。]

## 相关词条

代数命题逻辑 | 多值逻辑 | 子结构逻辑 | 证明论的发展 | 模糊性

**（译注：相关词条的中文站内链接将由管线在对应词条重译完成后统一挂接。）**
