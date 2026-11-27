# 非精确概率 Imprecise Probabilities (Seamus Bradley)

> *首次发表于 2014 年 12 月 20 日；2019 年 2 月 19 日实质修订。*

## 1. 引言

概率论一直是一门成果极为丰硕的理论，几乎在每一个科学分支中都有应用。在哲学中，概率论的一些重要应用以贝叶斯主义之名而为人所知；这是一个极为成功的纲领（例如见 Howson and Urbach 2006; Bovens and Hartmann 2003; Talbott 2008）[^bovens-2003][^howson-2006][^talbott-2008]。但概率论似乎把远比应然更为丰富、更为确定的态度归派给信念。对于全球地表平均温度到 2080 年将上升四度以上这一事件，你的理性置信度应当是多少？也许是 0.75？为什么不是 0.75001？为什么不是 0.7497？该事件比掷两次公平硬币至少出现一次正面更可能还是更不可能？似乎有许多事件，我们可以（或许也应当）对之采取不如正统概率论所要求的那样精确的态度。在质疑正统的诸多理由中，坚持用单一实值概率函数表征信念状态，似乎是一种相当不现实的理想化，并且会带来一些颇为棘手的后果，我们将在后文讨论。诚然，人们早已认识到，概率论提供的只是关于信念的一种相当理想化的模型。早在 19 世纪中叶，乔治·布尔（George Boole）就说过：

> 若断言这种期望的强度——即便把它视为一种心灵情感——可以归结为某种数值标准，那将是不合乎哲学的。（Boole 1958 [1854]: 244）[^boole-1958]

出于这些理由以及许多其他理由，人们对 **非精确概率**（Imprecise Probability，IP）模型的兴趣日益增长。宽泛地说，这些模型以某种方式超出了概率论正统的范围。

IP 模型被用于若干领域，包括：

- 统计学（Walley 1991; Ruggeri et al. 2005; Augustin et al. 2014）[^augustin-2014][^ruggeri-2005][^walley-1991]
- 推理心理学（Pfeifer and Kleiter 2007）[^pfeifer-2007]
- 不确定性的语言加工（Wallsten and Budescu 1995）[^wallsten-1995]
- 对歧义与冲突的神经反应（Smithson and Pushkarskaya 2015）[^smithson-2015]
- 哲学（Levi 1980; Joyce 2011; Sturgeon 2008; Kaplan 1983; Kyburg 1983）[^joyce-2011][^kaplan-1983][^kyburg-1983][^levi-1980][^sturgeon-2008]
- 行为经济学（Ellsberg 1961; Camerer and Weber 1992; Smithson and Campbell 2009）[^camerer-1992][^ellsberg-1961][^smithson-2009]
- 数理经济学（Gilboa 1987）[^gilboa-1987]
- 工程学（Ferson and Ginzburg 1996; Ferson and Hajagos 2004; Oberguggenberger 2014）[^ferson-1996][^ferson-2004][^oberguggenberger-2014]
- 计算机科学（Cozman 2000; Cozman and Walley 2005）[^cozman-2000][^cozman-2005]
- 科学计算（Oberkampf and Roy 2010, chapter 13）[^oberkampf-2010]
- 物理学（Suppes and Zanotti 1991; Hartmann and Suppes 2010; Frigg et al. 2014）[^frigg-2014][^hartmann-2010][^suppes-1991]

本文梳理 IP 模型的多种动机，介绍大体属于这一领域的各种形式模型，并讨论这些框架面临的一些未决问题。重点是信念的形式模型。

### 1.1 术语概述

全文采用这样的惯例：讨论一个任意有意图的行动者（intentional agent）的信念，并称其为“你”。IP 的几位重要倡导者（包括 Good 与 Walley）也采用这一惯例。

本文讨论信念的形式模型，因此需要引入一定数量的形式工具。设有一个状态集 *Ω*，它表示世界可能所处的各种方式。有时 *Ω* 被描述为“可能世界”的集合。信念对象——即你所持有信念所关于的东西——可以用世界可能所处方式之集 *Ω* 的子集来表征。我们可以把命题 $X$ 等同于使之成真的状态集，或等同于它在其中成真的可能世界集。如果你对 $X$ 与 $Y$ 持有信念，那么你也对“$X\cap Y$”“$X \cup Y$”与“$\neg X$”持有信念，它们分别表示“$X$ 且 $Y$”“$X$ 或 $Y$”与“并非 $X$”。信念对象的集合是 *Ω* 的幂集；若 *Ω* 是无穷集，则是 *Ω* 的某个子集可测代数。

关于置信度的标准观点是：置信度由实数表征，信念状态由概率函数表征；这是一项规范性要求。概率函数是从信念代数到实数的函数 $p$，且满足：

- $0 = p(\emptyset) \le p(X) \le p(\Omega) = 1$
- 若 $X\cap Y = \emptyset$，则 $p(X\cup Y) = p(X) + p(Y)$

因此，若你的信念状态或信态由 $p$ 表征，则你对 $X$ 的置信度就是 $p$ 赋予 $X$ 的值，即 $p(X)$。

此外，在贝叶斯信念模型中，学习通过 **条件化** 实现。如果你得知命题 $E$（且未得知其他任何东西），那么你学习之后对 $X$ 的信念由 $p(X\mid E) = p(X\cap E)/p(E)$ 给出。

本文的主要关注点是另一条进路：它用概率函数的 **集合** 而非单一概率来表征信念。因此，不是由某个 $p$ 表征你的信念状态，而是由 $P$——一个由这类函数组成的集合——来表征。van Fraassen（1990）[^fraassen-1990] 称之为你的 **表征集**（representor），Levi 称之为 **信度集**（credal set）。后文将讨论解释表征集的各种方式；眼下可以这样理解：你的表征集是一个 **信度委员会**：其中每个概率函数代表委员会一名成员的意见，而委员会集体地表征你的信念。

由这些概念可以定义一些“汇总函数”，它们在非精确概率的讨论中经常使用。人们常常假定，你对命题 $X$ 的置信度由 $P(X) = \{p(X) : p\in P \}$ 表征。本文将采用这一记号惯例，但有一项保留：本文并不认为 $P(X)$ 足以充分表征你对 $X$ 的置信度。你对 $X$ 的 **下包络** 为：$\underline{P}(X)=\inf P(X)$。同样，**上包络** 为 $\overline{P}(X)=\sup P(X)$。二者在如下意义上是彼此的 **共轭**：$\overline{P}(X) = 1 - \underline{P}(\neg X)$。

关于概率集更新的标准假定是：学习 $E$ 之后你对 $X$ 的置信度由 $P(X\mid E) = \{p(X\mid E), p\in P, p(E) > 0\}$ 给出。学习 $E$ 之后的信念状态是 $P(\cdot\mid E) = \{p(\cdot\mid E), p\in P, p(E) > 0\}$。也就是说，由条件概率之集给出。

这里要事先强调：这些汇总函数——$P(\cdot)$、$\underline{P}(\cdot)$ 与 $\overline{P}(\cdot)$——并不能恰当地代表你的信念。这幅图景遗漏了信息。这一问题在后文讨论膨胀时将变得重要。

我们还需要讨论决策，因此将引入一个以赌局表述决策的简单模型。我们可以把有界实值函数 $f$ 视为“赌局”，即从某个集合 *Ω* 到实数的函数。若 *ω* 是真实状态，赌局 $f$ 支付 $f(\omega)$。我们假定，你对这种善的每一新增单位给予相同评价（赌局支付与效用呈线性），并且对风险问题无差别。你对这些赌局的态度，反映你对 *Ω* 中各种可能情形之可能性的态度。也就是说，若 *ω* 发生则赢得很多的赌局，在你认为 *ω* 越可能时就越有吸引力。特别地，考虑命题 $X$ 上的指示函数 $I_X$：若 $X$ 在现实世界为真则输出 $1$，否则输出 $0$。这是一类特殊的赌局，你对它们的态度直接反映你对相应命题的置信度。你认为 $I_X$ 越有价值，就认为 $X$ 越可能。我们称它们为指示赌局。

赌局按其期望值来评价。记 $E_{p}(f)$ 为赌局 $f$ 关于概率 $p$ 的期望值，定义如下：

$$ {E}_p(f) = \sum_{\Omega} p(\omega) f(\omega) $$

$f$ 在状态 *ω* 中价值多大，取决于 $f(\omega)$ 有多大。$f$ 在 *ω* 中的好处有多重要，取决于该状态有多可能，以 $p(\omega)$ 衡量。期望便是这些经概率加权的价值之和。关于期望效用的更多讨论，见 Briggs（2014）[^briggs-2014]。

接着定义 $\mathbf{E}_{P}(f)$ 为 $\mathbf{E}_{P}(f) = \{E_{p}(f) : p\in P \}$。即 $P$ 中各成员的期望值之集。对 $\mathbf{E}_{P}(f)$ 也有与 $P(X)$ 相同的保留：$\mathbf{E}_{P}(f)$ 在多大程度上充分表征你对赌局价值的态度，仍有疑问。在不引起歧义时，本文常省略下标“$P$”。进一步的技术细节见[形式附录](imprecise-probabilities.supplement-formal.md)。

### 1.2 一些重要区分

下文有几组区分十分重要。

IP 理论的一个重要参数，是该理论被设定具有的规范力量。非精确是义务性的，还是仅仅可允许的？它是 **始终** 可允许／义务性的，还是只在某些时候如此？或者，我们可能关心一个纯粹描述性的方案：刻画现实行动者的信度状态，而不关心规范问题。本文很少涉及最后一种可能。

还有助于把信念本身与对信念的引出区分开来，也与其内省通达区分开来。其他态度（价值、效用等）也是如此。你可能持有某些信念，在实践中乃至原则上都无法（精确地）引出。同样，你对自己信念的内省通达可能并不完美。这种不完美可以成为非精确性的一个来源。Bradley（2009）[^bradley-2009] 区分了许多不同的不完美内省来源。这种不完美可能源于你对所涉前景缺乏觉察、推理的有限性、对相关可能情形的无知，或源于你的证据或价值存在冲突（第 240–241 页）。关于不确定性类型的进一步讨论，见 Bradley and Drechsler（2014）。

一组证据有诸多方面可能影响你应当如何回应它。我们可以问证据 **有多少**（证据权重）。可以问证据是否均衡，或是否强烈偏向某个假说而非另一个（证据平衡）。证据可能因 **不完备** 而均衡：证据根本不够。证据也可能因 **冲突** 而均衡：不同证据支持不同假说。我们还可以问，证据告诉我们的东西是 **具体的**——例如硬币偏向正面的程度为 2/3——还是 **不具体的**——例如硬币偏向正面的程度介于 2/3 与 1 之间。这种具体性应区别于证据的模糊性或非确定性：硬币偏向程度 **约为** 2/3，这是模糊但具体的；硬币偏向程度确定地处于 2/3 与 1 之间的某处，这是确定但不具体的。同样，一个信度状态可以是非确定的、模糊的，也可以是不具体的，或二者兼有。确定但不具体的信念状态似乎会比非确定的信念状态更少见。

Isaac Levi（1974, 1985）[^levi-1974][^levi-1985] 区分了“非精确的”信度与“非确定的”信度（这里的引号表示：他使用“非精确”与“非确定”二词的方式，与本文采用的用法并不一致）。其想法是：有两类不同的信念状态，可能都需要转向 IP 的信念表征。在 Levi 的术语中，“非精确的”信念，在本文术语中就是不完美内省或不完美引出的信念；而“非确定的”信念则是（可能）被完美内省、却仍然非确定或不具体（或二者兼有）的信念。Levi 主张，有趣的现象是“非确定的”信度。Walley（1991）[^walley-1991] 也强调，要区分存在“正确”但未知概率的情形与“非确定性”情形。

关于 IP 的解释，还有一个与上述区分交叉的问题。这就是：我们把 $P$ 理解为对你信念的“完全”或“穷尽”表征，还是认为该表征不完备或不穷尽？暂且用下注解释来说。穷尽／非穷尽的区分可以通过下述问题划定：$P$ 是否把握了你下注倾向的 **全部且仅此**，还是 $P$ 只部分地把握了你的下注倾向？Walley 强调这一区分，并认为大多数模型都是非穷尽的。

部分由于 Levi 要求区分“非精确的”信念与“非确定的”信念，有人反对使用“非精确概率”一词。利用上述非确定、不具体与不完美内省信念之间的区分，我们可以在不使用“非精确”一词的情况下，保持 Levi 想要保持分离的各范畴。然后可以把“非精确”用作统称，涵盖所有这些缺乏精确性的情形。这样一来，我们也方便地与大量关于“非精确概率”的形式工作保持一致，该术语被用来涵盖非确定性的情形。这一用法至少可追溯到 Peter Walley 那本影响深远的著作 *Statistical Reasoning with Imprecise Probabilities*（Walley 1991）[^walley-1991]。

所以，“非精确”并不完全恰当，但“概率”也不完全恰当，因为 IP 的形式理论实际上关乎 **预现**（previsions，一种期望），而不只是关乎概率（指示函数的期望）。好在，若把 Imprecise Probability 缩写为“IP”，便可利用一些有用的歧义。

## 脚注

[^augustin-2014]: Augustin, Thomas, Frank P.A. Coolen, Gert de Cooman, and Matthias C.M. Troffaes (eds), 2014, *Introduction to Imprecise Probabilities*, John Wiley and Sons. New York.

[^boole-1958]: Boole, George. 1958 [1854], *The Laws of Thought*, Dover. New York.

[^bovens-2003]: Bovens, Luc, and Stephan Hartmann, 2003, *Bayesian epistemology*, Oxford University Press. Oxford.

[^bradley-2009]: Bradley, Richard, 2009, “Revising Incomplete Attitudes”, *Synthese*, 171: 235–256.

[^briggs-2014]: Briggs, R.A., 2014, “Normative Theories of Rational Choice: Expected Utility”, *The Stanford Encyclopedia of Philosophy*, (Fall 2014 Edition), Edward N. Zalta (ed.), URL = <[https://plato.stanford.edu/archives/fall2014/entries/rationality-normative-utility/](https://plato.stanford.edu/archives/fall2014/entries/rationality-normative-utility/)>.

[^camerer-1992]: Camerer, Colin, and Martin Weber, 1992, “Recent Developments in Modeling Preferences: Uncertainty and Ambiguity”, *Journal of Risk and Uncertainty*, 5: 325–370.

[^cozman-2000]: Cozman, Fabio, 2000, “Credal Networks”, *Artificial Intelligence*, 120: 199–233.

[^cozman-2005]: Cozman, Fabio, and Peter Walley, 2005, “Graphoid properties of epistemic irrelevance and independence”, *Annals of Mathematics and Artificial Intelligence*, 45: 173–195.

[^ellsberg-1961]: Ellsberg, Daniel, 1961, “Risk, ambiguity and the Savage axioms”, *Quarterly Journal of Economics*, 75: 643–696.

[^ferson-1996]: Ferson, Scott and Lev R. Ginzburg,1996, “Different methods are needed to propagate ignorance and variability”, *Reliability Engineering and System Safety*, 54 133–144.

[^ferson-2004]: Ferson, Scott and Janos G. Hajagos, 2004, “Arithmetic with uncertain numbers: Rigorous and (often) best possible answers”, *Reliability Engineering and System Safety*, 85 135–152.

[^fraassen-1990]: –––, 1990, “Figures in a Probability Landscape”, in *Truth or Consequences*, Michael Dunn and Anil Gupta (eds), 345–356, Springer. Dordrecht.

[^frigg-2014]: Frigg, Roman, Seamus Bradley, Hailiang Du, and Leonard A. Smith, 2014, “Laplace’s Demon and the Adventures of his Apprentices”, *Philosophy of Science*, 81: 31–59.

[^gilboa-1987]: Gilboa, Itzhak, 1987, “Expected Utility with Purely Subjective Non-additive Probabilities”, *Journal of Mathematical Economics*, 16: 65–88.

[^hartmann-2010]: Hartmann, Stephan, and Patrick Suppes, 2010, “Entanglement, Upper Probabilities and Decoherence in Quantum Mechanics”, in *EPSA Philosophical Issues in the Sciences: Launch of the European Philosophy of Science Association*, Mauricio Suárez, Mauro Dorato, and Miklós Rédei (eds), 93–103, Springer.

[^howson-2006]: Howson, Colin, and Peter Urbach, 2006, *Scientific Reasoning: the Bayesian Approach*, 3ʳᵈ edition, Open Court. Chicago.

[^joyce-2011]: –––, 2011, “A Defense of Imprecise Credence in Inference and Decision”, *Philosophical Perspectives*, 24: 281–323.

[^kaplan-1983]: Kaplan, Mark, 1983, “Decision theory as philosophy”, *Philosophy of Science*, 50: 549–577.

[^kyburg-1983]: Kyburg, Henry E., 1983, “Rational belief”, *The Brain and Behavioural Sciences*, 6: 231–273.

[^levi-1974]: Levi, Isaac, 1974, “On Indeterminate probabilities”, *Journal of Philosophy*, 71: 391–418.

[^levi-1980]: –––, 1980, *The Enterprise of Knowledge*, The MIT Press. Cambridge.

[^levi-1985]: –––, 1985, “Imprecision and Indeterminacy in Probability Judgment”, *Philosophy of Science*, 52: 390–409.

[^oberguggenberger-2014]: Oberguggenberger, Michael, 2014, “Engineering”, in Augustin et al. 2014: 291–304.

[^oberkampf-2010]: Oberkampf, William and Christopher Roy, 2010 *Verification and Validation in Scientific Computing*, Cambridge University Press. Cambridge.

[^pfeifer-2007]: Pfeifer, Niki, and Gernot D. Kleiter, 2007, “Human reasoning with imprecise probabilities: Modus ponens and denying the antecedent”, *Proceedings of the 5th International Symposium on Imprecise Probability: Theory and Application*: 347–356.

[^ruggeri-2005]: Ruggeri, Fabrizio, David Ríos and Jacinto Martín, 2005, “Robust Bayesian analysis”, *Handbook of Statistics*, 25 623–667, Elsevier. Amsterdam

[^smithson-2009]: Smithson, Michael, and Paul D. Campbell, 2009, “Buying and Selling Prices under Risk, Ambiguity and Conflict”, *Proceedings of the 6th International Symposium on Imprecise Probability: Theory and Application*.

[^smithson-2015]: Smithson, Michael, and Helen Pushkarskaya, 2015, “Ignorance and the Brain: Are there Distinct Kinds of Unknowns?” in *Routledge International Handbook of Ignorance Studies*, Matthias Gross and Linsey McGoey (eds), Routledge.

[^sturgeon-2008]: Sturgeon, Scott, 2008, “Reason and the grain of belief”, *Noûs*, 42: 139–165.

[^suppes-1991]: Suppes, Patrick, and Mario Zanotti, 1991, “Existence of Hidden Variables Having Only Upper Probability”, *Foundations of Physics*, 21: 1479–1499.

[^talbott-2008]: Talbott, William, 2008, “Bayesian Epistemology”, *The Stanford Encyclopedia of Philosophy* (Fall 2013 Edition), Edward N. Zalta (ed.), URL = <[https://plato.stanford.edu/archives/fall2013/entries/epistemology-bayesian/](https://plato.stanford.edu/archives/fall2013/entries/epistemology-bayesian/)>.

[^walley-1991]: Walley, Peter, 1991, *Statistical Reasoning with Imprecise Probabilities*, *Monographs on Statistics and Applied Probability*, Vol. 42. Chapman and Hall. London.

[^wallsten-1995]: Wallsten, Thomas, and David V. Budescu, 1995, “A review of human linguistic probability processing: General principles and empirical evidence”, *The Knowledge Engineering Review*, 10: 43–62.
