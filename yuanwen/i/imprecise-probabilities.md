# Imprecise Probabilities
**First published Sat Dec 20, 2014; substantive revision Tue Feb 19, 2019**

*Bradley, Seamus*

It has been argued that imprecise probabilities are a natural and intuitive way of overcoming some of the issues with orthodox precise probabilities. Models of this type have a long pedigree, and interest in such models has been growing in recent years. This article introduces the theory of imprecise probabilities, discusses the motivations for their use and their possible advantages over the standard precise model. It then discusses some philosophical issues raised by this model. There is also a historical appendix which provides an overview of some important thinkers who appear sympathetic to imprecise probabilities.

## 1. Introduction

Probability theory has been a remarkably fruitful theory, with applications in almost every branch of science. In philosophy, some important applications of probability theory go by the name Bayesianism; this has been an extremely successful program (see for example Howson and Urbach 2006; Bovens and Hartmann 2003; Talbott 2008)[^bovens-2003][^howson-2006][^talbott-2008]. But probability theory seems to impute much richer and more determinate attitudes than seems warranted. What should your rational degree of belief be that global mean surface temperature will have risen by more than four degrees by 2080? Perhaps it should be 0.75? Why not 0.75001? Why not 0.7497? Is that event more or less likely than getting at least one head on two tosses of a fair coin? It seems there are many events about which we can (or perhaps should) take less precise attitudes than orthodox probability requires. Among the reasons to question the orthodoxy, it seems that the insistence that states of belief be represented by a single real-valued probability function is quite an unrealistic idealisation, and one that brings with it some rather awkward consequences that we shall discuss later. Indeed, it has long been recognised that probability theory offers only a rather idealised model of belief. As far back as the mid-nineteenth century, we find George Boole saying:

> It would be unphilosophical to affirm that the strength of that expectation, viewed as an emotion of the mind, is capable of being referred to any numerical standard. (Boole 1958 [1854]: 244)[^boole-1958]

For these, and many other reasons, there is growing interest in *Imprecise Probability* (IP) models. Broadly construed, these are models of belief that go beyond the probabilistic orthodoxy in one way or another.

IP models are used in a number of fields including:

- Statistics (Walley 1991; Ruggeri et al. 2005; Augustin et al. 2014)[^augustin-2014][^ruggeri-2005][^walley-1991]
- Psychology of reasoning (Pfeifer and Kleiter 2007)[^pfeifer-2007]
- Linguistic processing of uncertainty (Wallsten and Budescu 1995)[^wallsten-1995]
- Neurological response to ambiguity and conflict (Smithson and Pushkarskaya 2015)[^smithson-2015]
- Philosophy (Levi 1980; Joyce 2011; Sturgeon 2008; Kaplan 1983; Kyburg 1983)[^joyce-2011][^kaplan-1983][^kyburg-1983][^levi-1980][^sturgeon-2008]
- Behavioural economics (Ellsberg 1961; Camerer and Weber 1992; Smithson and Campbell 2009)[^camerer-1992][^ellsberg-1961][^smithson-2009]
- Mathematical economics (Gilboa 1987)[^gilboa-1987]
- Engineering (Ferson and Ginzburg 1996; Ferson and Hajagos 2004; Oberguggenberger 2014)[^ferson-1996][^ferson-2004][^oberguggenberger-2014]
- Computer science (Cozman 2000; Cozman and Walley 2005)[^cozman-2000][^cozman-2005]
- Scientific computing (Oberkampf and Roy 2010, chapter 13)[^oberkampf-2010]
- Physics (Suppes and Zanotti 1991; Hartmann and Suppes 2010; Frigg et al. 2014)[^frigg-2014][^hartmann-2010][^suppes-1991]

This article identifies a variety of motivations for IP models; introduces various formal models that are broadly in this area; and discusses some open problems for these frameworks. The focus will be on formal models of belief.

### 1.1 A summary of terminology

Throughout the article I adopt the convention of discussing the beliefs of an arbitrary intentional agent whom I shall call “you”. Prominent advocates of IP (including Good and Walley) adopt this convention.

This article is about formal models of belief and as such, there needs to be a certain amount of formal machinery introduced. There is a set of states $\Omega$ which represents the ways the world could be. Sometimes $\Omega$ is described as the set of “possible worlds”. The objects of belief—the things you have beliefs about—can be represented by subsets of the set of ways the world could be $\Omega$. We can identify a proposition $X$ with the set of states which make it true, or, with the set of possible worlds where it is true. If you have beliefs about $X$ and $Y$ then you also have beliefs about “$X\cap Y$”, “$X \cup Y$” and “$\neg X$”; “$X$ and $Y$”, “$X$ or $Y$” and “it is not the case that $X$” respectively. The set of objects of belief is the power set of $\Omega$, or if $\Omega$ is infinite, some measurable algebra of the subsets of $\Omega$.

The standard view of degree of belief is that degrees of belief are represented by real numbers and belief states by probability functions; this is a normative requirement. Probability functions are functions, $p$, from the algebra of beliefs to real numbers satisfying:

- $0 = p(\emptyset) \le p(X) \le p(\Omega) = 1$
- If $X\cap Y = \emptyset$ then $p(X\cup Y) = p(X) + p(Y)$

So if your belief state or doxastic state is represented by $p$, then your degree of belief in $X$ is the value assigned to $X$ by $p$; that is, $p(X)$.

Further, learning in the Bayesian model of belief is effected by *conditionalisation*. If you learn a proposition $E$ (and nothing further) then your post-learning belief in $X$ is given by $p(X\mid E) = p(X\cap E)/p(E)$.

The alternative approach that will be the main focus of this article is the approach that represents belief by a *set* of probability functions instead of a single probability. So instead of having some $p$ represent your belief state, you have $P$, a set of such functions. van Fraassen (1990) calls this your *representor*, Levi calls it a *credal set*. I will discuss various ways you might interpret the representor later but for now we can think of it as follows. Your representor is a *credal committee*: each probability function in it represents the opinions of one member of a committee that, collectively, represents your beliefs.

From these concepts we can define some “summary functions” that are often used in discussions of imprecise probabilities. Often, it is assumed that your degree of belief in a proposition, $X$, is represented by $P(X) = \{p(X) : p\in P \}$. I will adopt this notational convention, with the proviso that I don’t take $P(X)$ to be an adequate representation of your degree of belief in $X$. Your *lower envelope* of $X$ is: $\underline{P}(X)=\inf P(X)$. Likewise, your *upper envelope* is $\overline{P}(X)=\sup P(X)$. They are *conjugates* of each other in the following sense: $\overline{P}(X) = 1 - \underline{P}(\neg X)$.

The standard assumption about updating for sets of probabilities is that your degree of belief in $X$ after learning $E$ is given by $P(X\mid E) = \{p(X\mid E), p\in P, p(E) > 0\}$. Your belief state after having learned $E$ is $P(\cdot\mid E) = \{p(\cdot\mid E), p\in P, p(E) > 0\}$. That is, by the set of conditional probabilities.

I would like to emphasise already that these summary functions—$P(\cdot)$, $\underline{P}(\cdot)$ and $\overline{P}(\cdot)$—are not properly representative of your belief. Information is missing from the picture. This issue will be important later, in our discussion of dilation.

We shall need to talk about decision making so we shall introduce a simple model of decisions in terms of gambles. We can view bounded real valued functions $f$ as “gambles” that are functions from some set $\Omega$ to real numbers. A gamble $f$ pays out $f(\omega)$ if $\omega$ is the true state. We assume that you value each further unit of this good the same (the gambles’ pay outs are linear in utility) and you are indifferent to concerns of risk. Your attitude to these gambles reflects your attitudes about how likely the various contingencies in $\Omega$ are. That is, gambles that win big if $\omega$ look more attractive the more likely you consider $\omega$ to be. In particular, consider the indicator function $I_X$ on a proposition $X$ which outputs $1$ if $X$ is true at the actual world and $0$ otherwise. These are a particular kind of gamble, and your attitude towards them straightforwardly reflects your degree of belief in the proposition. The more valuable you consider $I_X$, the more likely you consider $X$ to be. Call these indicator gambles.

Gambles are evaluated with respect to their expected value. Call $E_{p}(f)$ the expected value of gamble $f$ with respect to probability $p$, and define it as:

$$ {E}_p(f) = \sum_{\Omega} p(\omega) f(\omega) $$

How valuable you consider $f$ to be in state $\omega$ depends on how big $f(\omega)$ is. How important the goodness of $f$ in $\omega$ is depends on how likely the state is, measured by $p(\omega)$. The expectation is then the sum of these probability-weighted values. See Briggs (2014) for more discussion of expected utility.

Then we define $\mathbf{E}_{P}(f)$ as $\mathbf{E}_{P}(f) = \{E_{p}(f) : p\in P \}$. That is, the set of expected values for members of $P$. The same proviso holds of $\mathbf{E}_{P}(f)$ as held of $P(X)$: that is, the extent to which $\mathbf{E}_{P}(f)$ fully represents your attitude to the value of a gamble is open to question. I will often drop the subscript “$P$” when no ambiguity arises from doing so. Further technical details can be found in the [formal appendix](imprecise-probabilities.supplement-formal.md).

### 1.2 Some important distinctions

There are a number of distinctions that it is important to make in what follows.

An important parameter in an IP theory is the normative force the theory is supposed to have. Is imprecision obligatory or is it merely permissible? Is it *always* permissible/obligatory, or only sometimes? Or we might be interested in a purely descriptive project of characterising the credal states of actual agents, with no interest in normative questions. This last possibility will concern us little in this article.

It is also helpful to distinguish belief itself from the elicitation of that belief and also from your introspective access to those beliefs. The same goes for other attitudes (values, utilities and so on). It may be that you have beliefs that are not amenable to (precise) elicitation, in practice or even in principle. Likewise, your introspective access to your own beliefs might be imperfect. Such imperfections could be a source of imprecision. Bradley (2009) distinguishes many distinct sources of imperfect introspection. The imperfection could arise from your unawareness of the prospect in question, the boundedness of your reasoning, ignorance of relevant contingencies, or because of conflict in your evidence or in your values (pp. 240–241). See Bradley and Drechsler (2014) for further discussion of types of uncertainty.

There are a variety of aspects of a body of evidence that could make a difference to how you ought to respond to it. We can ask *how much* evidence there is (weight of evidence). We can ask whether the evidence is balanced or whether it tells heavily in favour of one hypothesis over another (balance of evidence). Evidence can be balanced because it is *incomplete*: there simply isn’t enough of it. Evidence can also be balanced if it is *conflicted*: different pieces of evidence favour different hypotheses. We can further ask whether evidence tells us something *specific*—like that the bias of a coin is 2/3 in favour of heads—or unspecific—like that the bias of a coin is between 2/3 and 1 in favour of heads. This specificity should be distinguished from vagueness or indeterminacy of evidence: that a coin has bias *about* 2/3 is vague but specific, while that a coin has bias definitely somewhere between 2/3 and 1 is determinate but unspecific. Likewise, a credal state could be indeterminate, fuzzy, or it could be unspecific, or it could be both. It seems like determinate but unspecific belief states will be rarer than indeterminate ones.

Isaac Levi (1974, 1985) makes a distinction between “imprecise” credences and “indeterminate” credences (the scare quotes are indicating that these aren’t uses of the terms “imprecise” and “indeterminate” that accord with the usage I adopt in this article). The idea is that there are two distinct kinds of belief state that might require a move to an IP representation of belief. An “imprecise” belief in Levi’s terminology is an imperfectly introspected or elicited belief in mine, while an “indeterminate” belief is a (possibly) perfectly introspected belief that is still indeterminate or unspecific (or both). Levi argues that the interesting phenomenon is “indeterminate” credence. Walley (1991) also emphasises the distinction between cases where there is a “correct” but unknown probability from cases of “indeterminacy”.

There is a further question about the interpretation of IP that cross-cuts the above. This is the question of whether we understand $P$ as a “complete” or “exhaustive” representation of your beliefs, or whether we take the representation to be incomplete or non-exhaustive. Let’s talk in terms of the betting interpretation for a moment. The exhaustive/non-exhaustive distinction can be drawn by asking the following question: does $P$ capture *all and only* your dispositions to bet or does $P$ only partially capture your dispositions to bet? Walley emphasises this distinction and suggests that most models are non-exhaustive.

Partly because of Levi’s injunction to distinguish “imprecise” from “indeterminate” belief, some have objected to the use of the term “imprecise probability”. Using the above distinction between indeterminate, unspecific and imperfectly introspected belief, we can keep separate the categories Levi wanted to keep separate all without using the term “imprecise”. We can then use “imprecise” as an umbrella term to cover all these cases of lack of precision. Conveniently, this allows us to stay in line with the wealth of formal work on “Imprecise Probabilities” which term is used to cover cases of indeterminacy. This usage goes back at least to Peter Walley’s influential book *Statistical Reasoning with Imprecise Probabilities* (Walley 1991)[^walley-1991].

So, “Imprecise” is not quite right, but neither is “Probability” since the formal theory of IP is really about *previsions* (sort of expectations) rather than just about probability (expectations of indicator functions). Helpfully, if I abbreviate Imprecise Probability to “IP” then I can exploit some useful ambiguities.

## 2. Motivations

Let’s consider, in general terms, what sort of motivations one might have for adopting models that fall under the umbrella of IP. The focus will be on models of rational belief, since these are the models that philosophers typically focus on, although it is worth noting that statistical work using IP isn’t restricted to this interpretation. Note that no one author endorses all of these arguments, and indeed, some authors who are sympathetic to IP have explicitly stated that they don’t consider certain of these arguments to be good (for example Mark Kaplan does not endorse the claim that concerns about descriptive realism suggest allowing incompleteness).

### 2.1 Ellsberg decisions

There are a number of examples of decision problems where we are intuitively drawn to go against the prescriptions of precise probabilism. And indeed, many experimental subjects do seem to express preferences that violate the axioms. IP offers a way of representing these intuitively plausible and experimentally observed choices as rational. One classic example of this is the *Ellsberg problem* (Ellsberg 1961)[^ellsberg-1961].

> I have an urn that contains ninety marbles. Thirty marbles are red. The remainder are blue or yellow in some unknown proportion.

Consider the indicator gambles for various events in this scenario. Consider a choice between a bet that wins if the marble drawn is red (I), versus a bet that wins if the marble drawn is blue (II). You might prefer I to II since I involves *risk* while II involves *ambiguity*. A prospect is risky if its outcome is uncertain but its outcomes occur with known probability. A prospect is ambiguous if the outcomes occur with unknown or only partially known probabilities. Now consider a choice between a bet that wins if the marble drawn is not blue (III) versus a bet that wins if the marble drawn is not red (IV). Now it is III that is ambiguous, while IV is unambiguous but risky, and thus IV might seem better to you if you preferred risky to ambiguous prospects. Such a pattern of preferences (I preferred to II but IV preferred to III) cannot be rationalised as the choices of a precise expected utility maximiser. The gambles are summarised in the table.

*Table 1:*

|   | R | B | Y |
| --- | --- | --- | --- |
| I | 1 | 0 | 0 |
| II | 0 | 1 | 0 |
| III | 1 | 0 | 1 |
| IV | 0 | 1 | 1 |

Table 1: The Ellsberg bets. The urn contains 30 red marbles and 60 blue/yellow marbles

Let the probabilities for red, blue and yellow marbles be $r$, $b$ and $y$ respectively. If you were an expected utility maximiser and preferred I to II, then $r > b$ and a preference for IV over III entails that $r+y < y +b$. No numbers can jointly satisfy these two constraints. Therefore, no probability function is such that an expected utility maximiser with that probability would choose in the way described above. While by no means universal, these preferences are a robust feature of many experimental subjects’ response to this sort of example (Camerer and Weber 1992; Fox and Tversky 1995)[^camerer-1992][^fox-1995]. Some experiments suggest that Ellsberg-type patterns of preference are rarer than normally recognised (Binmore et al. 2012; Voorhoeve et al. 2016)[^binmore-2012][^voorhoeve-2016]. For more on ambiguity attitudes, see Trautmann and van der Kuilen (2016).

The imprecise probabilist can model the situation as follows: $P(R)=1/3, P(B)=P(Y)=[0,2/3]$. Note that this expression of the belief state misses out some important details. For example, for all $p\in P$, we have $p(B)=2/3-p(Y)$. For the point being made here, this detail is not important. Modelling the ambiguity allows us to rationalise real agents’ preferences for bets on red. To flesh this story out would require a lot more to be said about decision making, (see section 3.3) but the intuition is that aversion to ambiguity explains the preference for I over II and IV over III.

As Steele (2007) points out, the above analysis rationalises the Ellsberg choices only if we are dealing with genuinely indeterminate or unspecific beliefs. If we were dealing with a case of imperfectly introspected belief then there would exist some $p$ in the representor such that rational choices maximise $E_{p}$. For the Ellsberg choices, there is no such $p$.

This view on the lessons of the Ellsberg game is not uncontroversial. Al-Najjar and Weinstein (2009) offer an alternative view on the interpretation of the Ellsberg preferences. Their view is that the distinctive pattern of Ellsberg choices is due to agents applying certain heuristics to solve the decisions that assume that the odds are manipulable. In real-life situations, if someone offers you a bet, you might think that they must have some advantage over you in order for it to be worth their while offering you the bet. Such scepticism, appropriately modelled, can yield the Ellsberg choices within a simple game theoretic precise probabilistic model.

### 2.2 Incompleteness and incomparability

Various arguments for (precise) probabilism assume that some relation or other is complete. Whether this is a preference over acts, or some “qualitative probability ordering”, the relation is assumed to hold one way or the other between any two elements of the domain. This hardly seems like it should be a principle of rationality, especially in cases of severe uncertainty. That is—to take the preference example—it is reasonable to have no preference in either direction. This is an importantly different attitude to being *indifferent* between the options. Mark Kaplan argues this point as follows:

> Both when you are indifferent between $A$ and $B$ and when you are undecided between $A$ and $B$ you can be said not to prefer either state of affairs to the other. Nonetheless, indifference and indecision are distinct. When you are indifferent between $A$ and $B$, your failure to prefer one to the other is born of a determination that they are equally preferable. When you are undecided, your failure to prefer one to the other is born of no such determination. (Kaplan 1996: 5)[^kaplan-1996]

There is a standard *behaviourist* response to the claim that incomparability and indifference should be distinguished. In short, the claim is that it is a distinction that cannot be inferred from actual agents’ choice behaviour. Ultimately, in a given choice situation you must choose one of the options. Which you choose can be interpreted as being (weakly) preferred. Joyce offers the following criticism of this appeal to behaviourism.

> There are just too many things worth saying that cannot be said within the confines of strict behaviorism… The basic difficulty here is that it is impossible to distinguish contexts in which an agent’s behavior really does reveal what she wants from contexts in which it does not without appealing to additional facts about her mental state… An even more serious shortcoming is behaviorism’s inability to make sense of *rationalizing explanations* of choice behavior. (Joyce 1999: 21)[^joyce-1999]

On top of this, behaviourists cannot make sense of the fact that incomparable goods are *insensitive to small improvements*. That is, if $A$ and $B$ are two goods that you have no preference between (for example, bets on propositions with imprecise probabilities) and if $A^+$ is a good slightly better than $A$, then it might still be incomparable with $B$. This distinguishes incomparability from indifference, since indifference “ties” will be broken by small improvements. So the claim that there is no behavioural difference between indifference and incomparability is false.

Kaplan argues that not only is violating the completeness axiom permissible, it is, in fact, sometimes obligatory.

> [M]y reason for rejecting as falsely precise the demand that you adopt a … set of preferences [that satisfy the preference axioms] is not the usual one. It is not that this demand is not humanly satisfiable. For if *that* were all that was wrong, the demand might still play a useful role as a regulative ideal—an ideal which might then be legitimately invoked to get you to “solve” your decision problem as the orthodox Bayesian would have you do. My complaint about the orthodox Bayesian demand is rather that it imposes the wrong regulative ideal. For if you have [such a] set of preferences then you have a determinate assignment of [$p$] to every hypothesis—and then you are not giving evidence its due. (Kaplan 1983: 571)[^kaplan-1983]

He notes that it is not the case that it is always unreasonable or impossible for you to have precise beliefs: in that case precision could serve as a regulative ideal. Precise probabilism does still serve as something of a regulative ideal, but it is the belief of an ideal agent *in an idealised evidential position*. Idealised evidential positions are approximated by cases where you have a coin of a known bias. Precise probabilists and advocates of IP both agree that precise probabilism is an idealisation, and a regulative ideal. However, they differ as to what kind of idealisation is involved. Precise probabilists think that what precludes us from having precise probabilistic beliefs is merely a lack of computational power and introspective capacity. Imprecise probabilists think that even agents ideal in this sense might (and possibly *should*) fail to have precise probabilistic beliefs when they are not in an ideal *evidential* position.

At least some of the axioms of preference are not normative constraints. We can now ask what can be proved in the absence of the “purely structural”—non-normative—axioms? This surely gives us a handle on what is really required of the structure of belief.

It seems permissible to fail to have a preference between two options. Or it seems reasonable to fail to consider either of two possibilities more likely than the other. And these failures to assent to certain judgements is not the same as considering the two elements under consideration to be *on a par* in any substantive sense. That said, precise probabilism is serving as a regulative ideal. That is, precision might still be an unattained (possibly unattainable) goal that informs agents as to how they might improve their credences. Completeness of preference is what the thoroughly informed agent ought to have. Without complete preference, standard representation theorems don’t work. However, for each *completion* of the incomplete preference ordering—for each complete ordering that extends the incomplete preference relation—the theorem follows. So if we consider the set of probability functions that are such that some completion of the incomplete preference is represented by that function, then we can consider this set to be representing the beliefs associated with the incomplete preference. We also get, for each completion, a utility function unique up to linear transformation. This, in essence, was Kaplan’s position (see Kaplan 1983; 1996)[^kaplan-1983].

Joyce (1999: 102–4) and Jeffrey (1984: 138–41) both make similar claims. A particularly detailed argument along these lines for comparative belief can be found in Hawthorne (2009). Indeed, this idea has a long and distinguished history that goes back at least as far as B.O. Koopman (1940). I.J Good (1962), Terrence Fine (1973) and Patrick Suppes (1974) all discussed ideas along these lines. Seidenfeld, Schervish, and Kadane (1995) give a representation theorem for preference that don’t satisfy completeness. (See Evren and Ok 2011; Pedersen 2014; and Chu and Halpern 2008, 2004; for very general representation theorems)[^chu-2004][^chu-2008][^evren-2011][^pedersen-2014][^pedersen-2014-2].

### 2.3 Weight of evidence, balance of evidence

Evidence influences belief. Joyce (2005) suggests that there is an important difference between the weight of evidence and the balance of evidence. He argues that this is a distinction that precise probabilists struggle to deal with and that the distinction is worth representing. This idea has been hinted at by a great many thinkers including J.M. Keynes, Rudolf Carnap, C.S. Pierce and Karl Popper (see references in Joyce 2005; Gärdenfors and Sahlin 1982)[^gärdenfors-1982][^joyce-2005]. Here’s Keynes’ articulation of the intuition:

> As the relevant evidence at our disposal increases, the magnitude of the probability of the argument may either decrease or increase, according as the new knowledge strengthens the unfavourable or the favourable evidence; but *something* seems to have increased in either case,—we have a more substantial basis upon which to rest our conclusion. I express this by saying than an accession of new evidence increases the *weight* of an argument. (Keynes 1921: 78, Keynes’ emphasis)[^keynes-1921]

Consider tossing a coin known to be fair. Let’s say you have seen the outcome of a hundred tosses and roughly half have come up heads. Your degree of belief that the coin will land heads should be around a half. This is a case where there is weight of evidence behind the belief.

Now consider another case: a coin of unknown bias is to be tossed. That is, you have not seen any data on previous tosses. In the absence of any relevant information about the bias, symmetry concerns might suggest you take the chance of heads to be around a half. This opinion is different from the above one. There is no *weight* of evidence, but there is nothing to suggest that your attitudes to $H$ and $T$ should be different. So, on *balance*, you should have the same belief in both.

However, these two different cases get represented as having the same probabilistic belief, namely $p(H)=p(T)=0.5$. In the fair coin case, this probability assignment comes from having evidence that suggests that the chance of heads is a half, and the prescription to have your credences match chances (*ceteris paribus*). In the unknown bias case, by contrast, one arrives at the same assignment in a different way: nothing in your evidence supports one proposition over the other so some “principle of indifference” reasoning suggests that they should be assigned the same credence (see Hájek 2011, for discussion of the principle of indifference)[^hájek-2011].

If we take seriously the “ambiguity aversion” discussed earlier, when offered the choice between betting on the fair coin’s landing heads as opposed to the unknown-bias coin’s landing heads, it doesn’t seem unreasonable to prefer the former. Recall the preference for unambiguous gambles in the Ellsberg game in section 2.1. But if both coins have the same subjective probabilities attached, what rationalises this preference for betting on the fair coin? Joyce argues that there is a difference between these beliefs that is worth representing. IP *does* represent the difference. The first case is represented by $P(H)=\{0.5\}$, while the second is captured by $P(H)=[0,1]$.

Scott Sturgeon puts this point nicely when he says:

> *[E]vidence and attitude aptly based on it must match in character*. When evidence is essentially sharp, it warrants sharp or exact attitude; when evidence is essentially fuzzy—as it is most of the time—it warrants at best a fuzzy attitude. In a phrase: evidential precision begets attitudinal precision; and evidential imprecision begets attitudinal imprecision. (Sturgeon 2008: 159 Sturgeon’s emphasis)[^sturgeon-2008]

Wheeler (2014) criticises Sturgeon on this “character matching” thesis. However, an argument for IP based on the nature of evidence only requires that the character of the evidence sometimes allows (or mandates?) imprecise belief and not that the characters must always match. In opposition, Schoenfield (2012) argues that evidence always supports precise credence, but that for reasons of limited computational capacity, real agents needn’t be required to have precise credences. However, her argument only really supports the claim that *sometimes* indeterminacy is due to complexity of the evidence and computational complexity. She doesn’t have an argument against the claims Levi, Kaplan, Joyce and others make that there are evidential situations that warrant imprecise attitudes.

Strictly speaking, what we have here is only half the story. There *is* a difference between the representations of belief as regards weight and balance. But that still leaves open the question of exactly what is representing the weight of evidence? What aspect of the belief reflects this difference? One might be tempted to view $\overline{P}(H)-\underline{P}(H)$ as a measure of the weight of evidence for $H$. Walley (1991) tentatively suggests as much. However, this would get wrong cases of conflicting evidence. (Imagine two equally reliable witnesses: one tells you the coin is biased towards heads, the other says the bias is towards tails.) The question of whether and how IP does better than precise probabilism has not yet received an adequate answer. Researchers in IP have, however, made progress on distinguishing cases where your beliefs happen to have certain symmetry properties from cases where your beliefs capture evidence about symmetries in the objects of belief. This *is* a distinction that the standard precise model of belief fails to capture (de Cooman and Miranda 2007)[^cooman-2007].

The precise probabilist can respond to the weight/balance distinction argument by pointing to the property of *resiliency* (Skyrms 2011)[^skyrms-2011] or *stability* (Leitgeb 2014)[^leitgeb-2014]. The idea is that probabilities determined by the weight of evidence change less in response to new evidence than do probabilities determined by balance of evidence alone. That is, if you’ve seen a hundred tosses of the coin, seeing it land heads doesn’t affect your belief much, while if you’ve not seen any tosses of the coin, seeing it land heads has a bigger effect on your beliefs. Thus, the distinction is represented in the precise probabilistic framework in the conditional probabilities. The distinction, though, is one that cannot rationalise the preference for betting on the fair coin. One could develop a resiliency-weighted expected value and claim that this is what you should maximise, but this would be as much of a departure from orthodox probabilism as IP is. If someone were to develop such a theory, then its merits could be weighed against the merits of IP type models.

Another potential precise response would be to suggest that there is weight of evidence for $H$ if many propositions that are evidence for $H$ are fully believed, or if there is a chance proposition (about $H$) that is near to fully believed. This is in contrast to cases of mere balance where few propositions that are evidence for $H$ are fully believed, or where probability is spread out over a number of chance hypotheses. The same comments made above about resiliency apply here: such distinctions can be made, but this doesn’t get us to a theory that can rationalise ambiguity aversion.

The phenomenon of dilation (section 3.1) suggests that the kind of argument put forward in this section needs more care and further elaboration.

### 2.4 Suspending judgement

You are sometimes in a position where none of your evidence seems to speak for or against the truth of some proposition. Arguably, a reasonable attitude to take towards such a proposition is suspension of judgement.

> When there is little or no information on which to base our conclusions, we cannot expect reasoning (no matter how clever or thorough) to reveal a most probable hypothesis or a uniquely reasonable course of action. There are limits to the power of reason. (Walley 1991: 2)[^walley-1991]

Consider a coin of unknown bias. The Bayesian agent must have a precise belief about the coin’s landing heads on the next toss. Given the complete lack of information about the coin, it seems like it would be better just to suspend judgement. That is, it would be better not to have any particular precise credence. It would be better to avoid betting on the coin. But there just isn’t room in the Bayesian framework to do this. The probability function must output some number, and that number will sanction a particular set of bets as desirable.

Consider $\underline{P}(X)$ as representing the degree to which the evidence supports $X$. Now consider $I(X) = 1- (\underline{P}(X) + \underline{P}(\neg X))$. This measures the degree to which the evidence is silent on $X$. Huber (2009) points out that precise probabilism can then be understood as making the claim that no evidence is ever silent on any proposition. That is, $I(X)=0$ for all $X$. One can never suspend judgement. This is a nice way of seeing the strangeness of the precise probabilist’s attitude to evidence. Huber is making this point about Dempster-Shafer belief functions (see historical appendix, section 7), but it carries over to IP in general.

The committed precise probabilist would respond that setting $p(X)=0.5$ *is* suspending judgement. This *is* the maximally noncommittal credence in the case of a coin flip. More generally, suspending judgement should be understood in terms of maximising entropy (Jaynes 2003; Williamson 2010: 49–72)[^jaynes-2003][^williamson-2010]. The imprecise probabilist could argue that this only *seems* to be the right way to be noncommittal if you are wedded to the precise probabilist representation of belief. That is, the MaxEnt approach makes sense if you are already committed to representation of belief by a single precise probability, but loses its appeal if credal sets are available. Suspending judgement is something you do when the evidence doesn’t determine your credence. But for the precise probabilist, there is no way to signal the difference between suspension of judgement and strong evidence of probability half. This is just the weight/balance argument again.

To make things more stark, consider the following delightfully odd example from Adam Elga:

> A stranger approaches you on the street and starts pulling out objects from a bag. The first three objects he pulls out are a regular-sized tube of toothpaste, a live jellyfish, and a travel-sized tube of toothpaste. To what degree should you believe that the next object he pulls out will be another tube of toothpaste? (2010: 1)

In this case, unlike in the coin case, it really isn’t clear what intuition says about what would be the “correct” precise probabilist suspension of judgement. What Maximum Entropy methods recommend will depend on seemingly arbitrary choices about the formal language used to model the situation. Williamson is well aware of this language relativity problem. He argues that choice of a language encodes some of our evidence.

Another response to this argument would be to take William James’ response to W.K. Clifford (Clifford 1901; James 1897)[^clifford-1901][^james-1897]. James argued that as long as your beliefs are consistent with the evidence, then you are free to believe what you like. So there is *no need* to ever suspend judgement. Thus, the precise probabilist’s inability to do so is no real flaw. This attitude, which is sometimes called *epistemic voluntarism*, is close to the sort of *subjectivism* espoused by Bruno de Finetti, Frank Ramsey and others.

There does seem to be a case for an alternative method of suspending judgement in order to allow you to avoid making any bets when your evidence is very incomplete, ambiguous or imprecise. If your credences serve as your standard for the acceptability of bets, they should allow for both sides of a bet to fail to be acceptable. A precise probabilist cannot do this since if a bet has (precise) expected value $e$ then taking the other side of that bet (being the bookie) has expected value $-e$. If acceptability is understood as nonnegative expectation, then at least one side of any bet is acceptable to a precise agent. This seems unsatisfactory. Surely genuine suspension of judgement involves being unwilling to risk money on the truth of a proposition at any odds.

Inspired by the famous “Bertrand paradox”, Chandler (2014) offers a neat argument that the precise probabilist cannot jointly satisfy two desiderata relating to suspension of judgment about a variable. First desideratum: if you suspend judgement about the value of a bounded real variable $X$, then it seems that different intervals of possible values for $X$ of the same size should be treated the same by your epistemic state. Second desideratum: if $Y$ essentially describes the same quantity as $X$, then suspension of judgement about $X$ should entail suspension of judgement about $Y$. Let’s imagine now that you have precise probabilities and that you suspend judgement about $X$. By the first desideratum, you have a uniform distribution over values of $X$. Now consider $Y = 1/X$. $Y$ essentially describes the same quantity that $X$ did. But a uniform distribution over $X$ entails a non-uniform distribution over $Y$. So you do not suspend judgement over $Y$. A real-world case of variables so related is “ice residence time in clouds” and “ice fall rate in clouds”. These are inversely related, but describe essentially the same element of a climate system (Stainforth et al. 2007: 2154)[^stainforth-2007].

So a precise probabilist cannot satisfy these reasonable desiderata of suspension of judgement. An imprecise probabilist can: for example, the set of all probability functions over $X$ satisfies both desiderata. There may be more informative priors that also represent suspension of judgement, but it suffices for now to point out that IP seems better able to represent suspension of judgement than precise probabilism. Section 5.5 of Walley (1991), discusses IP’s prospects as a method for dealing with suspension of judgement.

### 2.5 Unknown correlations

Haenni et al. (2011) motivate imprecise probabilities by showing how they can arise from precise probability judgements. That is, if you have a precise probability for $X$ and a precise probability for $Y$, then you can put bounds on $p(X\cap Y)$ and $p(X \cup Y)$, even if you don’t know how $X$ and $Y$ are related. These bounds give you intervals of possible probability values for the compound events.

For example, you know that $p(X \cap Y)$ is bounded above by $p(X)$ and by $p(Y)$ and thus by $\min\{p(X),p(Y)\}$. If $p(X) \gt 0.5$ and $p(Y) \gt 0.5$ then $X$ and $Y$ must overlap. So $p(X\cap Y)$ is bounded below by $p(X)+p(Y)-1$. But, by definition, $p(X \cap Y)$ is also bounded below by $0$. So we have the following result: if you know $p(X)$ and you know $p(Y)$, then, you know

$$ \max\{0,p(X)+p(Y)-1\} \le p(X \cap Y) \le \min\{p(X),p(Y)\}. $$

Likewise, bounds can be put on $p(X \cup Y)$. $p(X\cup Y)$ can’t be bigger than when $X$ and $Y$ are disjoint, so it is bounded above by $p(X)+p(Y)$. It is also bounded above by $1$, and thus by the minimum of those expressions. It is also bounded below by $p(X)$ and by $p(Y)$ and thus by their maximum. Putting this together,

$$\max\{p(X),p(Y)\} \le p(X\cup Y) \le \min\{p(X)+p(Y),1\}.$$

These constraints are effectively what you get from de Finetti’s Fundamental Theorem of Prevision (de Finetti 1990 [1974]: 112; Schervish, Seidenfeld, and Kadane 2008)[^finetti-1990][^schervish-2008].

So if your evidence constrains your belief in $X$ and in $Y$, but is silent on their interaction, then you will only be able to pin down these compound events to certain intervals. Any choice of a particular probability function will go beyond the evidence in assuming some particular evidential relationship between $X$ and $Y$. That is, $p(X)$ and $p(X\mid Y)$ will differ in a way that has no grounding in your evidence.

### 2.6 Nonprobabilistic chances

What if the objective chances were not probabilities? If we endorse some kind of connection between known objective chances and belief—for example, a principle of direct inference or Lewis’ Principal Principle (Lewis 1986)[^lewis-1986]—then we might have an additional reason to endorse imprecise probabilism. It seems to be a truth universally acknowledged that chances ought to be probabilities, but it is a “truth” for which very little argument has been offered. For example, Schaffer (2007) makes obeying the probability axioms one of the things required in order to play the “chance role”, but offers no argument that this should be the case. Joyce says “some have held objective chances are not probabilities. This seems unlikely, but explaining why would take us too far afield” (2009: 279, fn.17). Various other discussions of chance—for example in statistical mechanics (Loewer 2001; Frigg 2008)[^frigg-2008][^loewer-2001] or “Humean chance” (Lewis 1986, 1994)[^lewis-1986][^lewis-1994]—take for granted that chances should be precise and probabilistic (Dardashti et al. 2014 is an exception)[^dardashti-2014]. Obviously things are confused by the use of the concept of chance as a way of interpreting probability theory. There is, however, a perfectly good pre-theoretic notion of chance: this is what probability theory was originally invented to reason about, after all. This pre-theoretic chance still seems like the sort of thing that we should apportion our belief to, in some sense. And there is very little argument that chances must always be probabilities. If the chances were nonprobabilistic in a particular way, one might argue that your credences ought to be nonprobabilistic in the same way. What form a chance-coordination norm should take if chances and credences were to have non-probabilistic formal structures is currently an open problem.

I want to give a couple of examples of this idea. First consider some physical process that doesn’t have a limiting frequency but has a frequency that varies, always staying within some interval. This would be a process that is chancy, but fairly predictable. It might be that the best description of such a system is to just put bounds on its relative frequency. Such processes have been studied using IP models (Kumar and Fine 1985; Grize and Fine 1987; Fine 1988)[^fine-1988][^grize-1987][^kumar-1985], and have been discussed as a potential source of imprecision in credence (Hájek and Smithson 2012)[^hájek-2012]. A certain kind of non-standard understanding of a quantum-mechanical event leads naturally to upper probability models (Suppes and Zanotti 1991; Hartmann and Suppes 2010)[^hartmann-2010][^suppes-1991]. John Norton has discussed the limits of probability theory as a logic of induction, using an example which, he claims, admits no reasonable probabilistic attitude (Norton 2007, 2008a,b)[^norton-2007][^norton-2008a]. One might hope that IP offers an inductive logic along the lines Norton sketches. Norton himself has expressed scepticism on this line (Norton 2007)[^norton-2007], although Benétreau-Dupin (2015) has defended IP as a candidate system for Norton’s project. Finally, particular views on vagueness might well prompt a rethinking of the formal structure of chance (Bradley 2016)[^bradley-2016][^bradley-2016-2].

### 2.7 Group belief

Suppose we wanted our epistemology to apply not just to individuals, but to “group agents” like committees, governments, companies, and so on. Such agents may be made up of members who disagree. Levi (1986, 1999) has argued that representation of such conflict is better handled with sets of probabilities than with precise probabilities. There is a rich literature on combining or aggregating the (probabilistic) opinions of members of groups (Genest and Zidek 1986)[^genest-1986] but the outcome of such aggregation does not adequately represent the *disagreement* among the group. Some forms of aggregation also fail to respect plausible constraints on group belief. For example, if every member of the group agrees that $X$ and $Y$ are probabilistically independent, then it seems plausible to require that the group belief respects this unanimity. It is, however, well known that linear pooling—a simple and popular form of aggregation—does not respect this desideratum. Consider two probability functions $p, q$ such that $p(X) = p(Y) = 1/3$ and $p(X\mid Y)=p(X)$ while $q(X) = q(Y) = 2/3$ and $q(X\mid Y)=q(X)$. Consider aggregating these two probabilities by taking an unweighted average of them: $r = p/2 + q/2$. Now, calculation shows that $r(X\cap Y) = 5/18$ while $r(X)r(Y) = 1/4$, thus demonstrating that $r$ does not consider $X$ and $Y$ to be independent. So such an aggregation method does not satisfy the above desideratum (Kyburg and Pittarelli 1992; Cozman 2012)[^cozman-2012][^kyburg-1992]. For more on judgement aggregation in groups, see List and Pettit (2011), especially chapter 2.

Elkin and Wheeler (2016) argue that resolving disagreement among precise probabilist peers should involve an imprecise probability. Stewart and Quintana (2018) argue that imprecise aggregation methods have some nice properties that no precise aggregation method do.

If committee members have credences *and* utilities that differ among the group, then no precise probability-utility pair distinct from the probabilities and utilities of the agents can satisfy the *Pareto condition* (Seidenfeld, Kadane, and Schervish 1989)[^seidenfeld-1989]. The Pareto condition requires that the group preference respect agreement of preference among the group. That is, if all members of the group prefer $A$ to $B$ (that is, if each group member finds that $A$ has higher expected utility than $B$) then the aggregate preference (as determined by the aggregate probability-utility pair) should satisfy that preference. Since this “consensus preservation” is a reasonable requirement on aggregation, this result shows that precise models of group agents are problematic. Walley discusses an example of a set of probabilities where each probability represents the beliefs of a member of a group, then $P$ is an incomplete description of the beliefs of each agent, in the sense that if all members of $P$ agree on something, then that thing is something each agent believes. Sets of probabilities allow us to represent an agent who is *conflicted* in their judgements (Levi 1986, 1999)[^levi-1986][^levi-1999].

> Ideally rational agents may face choices where there is no best option available to them. Indeterminacy in probability judgement and unresolved conflicts between values lead to predicaments where at the moment of choice the rational agent recognizes more than one such preference ranking of the available options in [the set of available choices] to be permissible. (Levi 1999: 510)[^levi-1999]

Levi also argued that individual agents can be in conflict in the same way as groups, and thus that individuals’ credal states are also better represented by sets of probabilities. (Levi also argued for the *convexity* of credal states, which brings him into conflict with the above argument about independence (see historical appendix section 3).) One doesn’t need to buy the claim that groups and individuals must be modelled in the same way to take something away from this idea. One merely needs to accept the idea that an individual can be *conflicted* in such a way that a reasonable representation of her belief state—or belief and value state—is in terms of sets of functions. Bradley (2009) calls members of such sets “avatars”. This suggests that we interpret an individual’s credal set as a *credal committee* made up of her avatars. This interpretation of the representor is due to Joyce (2011), though Joyce attributes it Adam Elga. This committee represents all the possible prior probabilities you could have that are consistent with the evidence. Each credal committee member is a fully opinionated Jamesian voluntarist. The committee as a whole, collectively, is a Cliffordian objectivist.

## 3. Philosophical questions for IP

This section collects some problems for IP noted in the literature.

### 3.1 Dilation

Consider two logically unrelated propositions $H$ and $X$. Now consider the four “state descriptions” of this simple model as set out in Figure 1. So $a=H\cap X$ and so on. Now define $Y=a \cup d$. Alternatively, consider three propositions related in the following way: $Y$ is defined as “$H$ if and only if $X$”.

*Figure 1:*

![[A square with four quadrants, first column is labeled 'H' and second 'not H'; first row is labeled 'X' and second 'not X'. First quadrant (first column/first row) is shaded and has an 'a' on it; second quadrant (second column, first row) is not shaded and has a 'b' on it; third quadrant (first column, second row) is unshaded and has a 'c' on it; and last quadrant (second column, second row) is shaded and has a 'd' on it.]](../assets/imprecise-probabilities/two-by-two.png)

Figure 1: A diagram of the relationships after Seidenfeld (1994); $Y$ is the shaded area

Further imagine that $p(H\mid X) = p(H) = 1/2$. No other relationships between the propositions hold except those required by logic and probability theory. It is straightforward to verify that the above constraints require that $p(Y) = 1/2$. The probability for $X$, however, is unconstrained.

Let’s imagine you were given the above information, and took your representor to be the full set of probability functions that satisfied these constraints. Roger White suggested an intuitive gloss on how you might receive information about propositions so related and so constrained (White 2010)[^white-2010]. White’s puzzle goes like this. I have a proposition $X$, about which you know nothing at all. I have written whichever is true out of $X$ and $\neg X$ on the *Heads* side of a fair coin. I have painted over the coin so you can’t see which side is heads. I then flip the coin and it lands with the $X$ uppermost. $H$ is the proposition that the coin lands heads up. $Y$ is the proposition that the coin lands with the “$X$” side up.

Imagine if you had a precise prior that made you certain of $X$ (this is compatible with the above constraints since $X$ was unconstrained). Seeing $X$ land uppermost now should be evidence that the coin has landed heads. The game set-up makes it such that these apparently irrelevant instances of evidence *can* carry information. Likewise, being very confident of $X$ makes $Y$ very good evidence for $H$. If instead you were sure $X$ was false, $Y$ would be solid gold evidence of $H$’s falsity. So it seems that $p(H\mid Y)$ is proportional to prior belief in $X$ (indeed, this can be proven rather easily). Given the way the events are related, observing whether $X$ or $\neg X$ landed uppermost is a noisy channel to learn about whether or not $H$ landed uppermost.

So let’s go back to the original imprecise case and consider what it means to have an imprecise belief in $X$. Among other things, it means considering possible that $X$ could be very likely. It is consistent with your belief state that $X$ is such that if you knew what proposition $X$ was, you would consider it very likely. In this case, $Y$ would be good evidence for $H$. Note that in this case learning that the coin landed $\neg X$ uppermost—call this $Y'$—would be just as good evidence against $H$. Likewise, $X$ might be a proposition that you would have very low credence in, and thus $Y$ would be evidence *against* $H$.

Since you are in a state of ignorance with respect to $X$, your representor contains probabilities that take $Y$ to be good evidence that $H$ and probabilities that take $Y$ to be good evidence that $\neg H$. So, despite the fact that $P(H)=\{1/2\}$ we have $P(H\mid Y) = [0,1]$. This phenomenon—posteriors being wider than their priors—is known as dilation. The phenomenon has been thoroughly investigated in the mathematical literature (Walley 1991; Seidenfeld and Wasserman 1993; Herron, Seidenfeld, and Wasserman 1994; Pedersen and Wheeler 2014)[^herron-1994][^pedersen-2014][^pedersen-2014-2][^seidenfeld-1994][^seidenfeld-1993][^walley-1991][^wheeler-2014]. Levi and Seidenfeld reported an example of dilation to Good following Good (1967). Good mentioned this correspondence in his follow up paper (Good 1974)[^good-1974]. Recent interest in dilation in the philosophical community has been generated by White’s paper (White 2010)[^white-2010].

White considers dilation to be a problem since learning $Y$ doesn’t *seem* to be relevant to $H$. That is, since you are ignorant about $X$, learning whether or not the coin landed $X$ up doesn’t seem to tell you anything about whether the coin landed heads up. It seems strange to argue that your belief in $H$ should *dilate* from $1/2$ to $[0,1]$ upon learning $Y$. It feels as if this should just be irrelevant to $H$. However, $Y$ is only really irrelevant to $H$ when $p(X)=1/2$. Any other precise belief you might have in $X$ is such that $Y$ now affects your posterior belief in $H$. Figure 2 shows the situation for one particular belief about how likely $X$ is; for one particular $p\in P$. The horizontal line can shift up or down, depending on what the committee member we focus on believes about $X$. $p(H\mid Y)$ is a half only if the prior in $X$ is also a half. However, the imprecise probabilist takes into account *all the ways $Y$ might affect belief in $H$*.

*Figure 2:*

![[A square with two columns labeled 'H' and 'not H' and two rows, a narrow one labeled 'X' and a wide one labeled 'not X'. The first quadrant (first column, first row) is shaded and has a 'Y' on it; second quadrant (second column, first row) is not shaded and has a 'not Y' on it; third quadrant (first column, second row) is unshaded with a 'not Y' on it and the fourth quadrant (second column, second row) is shaded and has a 'Y' on it.]](../assets/imprecise-probabilities/joyces-diagram.png)

Figure 2: A member of the credal committee (after Joyce (2011))

Consider a group of agents who each had precise credences in the above coin case and differed in their priors on $X$. They would all start out with prior of a half in $H$. After learning $Y$, these agents would differ in their posterior opinions about $H$ based on their differing dispositions to update. The group belief would dilate. However, no agent in the group has acted in any way unreasonably. If we take Levi’s suggestion that individuals can be conflicted just like groups can, then it seems that individual agents can have their beliefs dilate just like groups can.

There are two apparent problems with dilation. First, the belief-moving effect of apparently irrelevant evidence; and second, the fact that learning some evidence can cause your belief-intervals to widen. The above comments speak to the first of these. Pedersen and Wheeler (2014) also are focused on mitigating this worry. We turn now to the second worry.

Even if we accept dilation as a fact of life for the imprecise probabilist, it is still *weird*. Even if all of the above argument is accepted, it still seems strange to say that your belief in $H$ is dilated, *whatever you learn*. That is, whether you learn $Y$ or $Y'$, your posterior belief in $H$ looks the same: $[0,1]$. Or perhaps, what it shows to be weird is that your initial credence was precise.

Hart and Titelbaum (2015) suggest that dilation is strange because conditionalising on a biconditional (which is, after all, what you are doing in the above example) is unintuitive even in the precise case. Whether all cases of dilation can be explained away in this manner remains to be seen. Gong and Meng (2017) likewise see dilation as a problem of mis-specified statistical inference, rather than a problem for IP per se.

Beyond this seeming strangeness, White suggests a specific way that being subject to dilation is an indicator of a defective epistemology. White suggests that dilation examples show that imprecise probabilities violate the *Reflection Principle* (van Fraassen 1984)[^fraassen-1984]. The argument goes as follows:

> given that you know now that whether you learn $Y$ or you learn $Y'$ your credence in $H$ will be $[0,1]$ (and you will certainly learn one or the other), your current credence in $H$ should also be $[0,1]$.

The general idea is that you should set your credences to what you expect your credences to be in the future. More specifically, your credence in $X$ should be the expectation of your future possible credences in $X$ over the things you might learn. Given that, for all the things you might learn in this example your credence in $H$ would be the same, you should have that as your prior credence also. Your prior should be such that $P(H) = [0,1]$. So having a precise prior credence in $H$ to start with is irrational. That’s how the argument against dilation from reflection goes. Your prior $P$ is not fully precise though. Consider $P(H \cap Y)$. That is, the prior belief in the conjunction is imprecise. So the alleged problem with dilation and reflection is not as simple as “your precise belief becomes imprecise”. The problem is “your precise belief *in $H$* becomes imprecise”; or rather, your precise belief in $H$ *as represented by $P(H)$* becomes imprecise.

The issue with reflection is more basic. What exactly does reflection require of imprecise probabilists in this case? Now, it is obviously the case that each credal committee member’s prior credence is its expectation over the possible future evidence (this is a theorem of probability theory). But somehow, it is felt, the *credal state as a whole* isn’t sensitive to reflection in the way the principle requires. Each $p\in P$ satisfies the principle, but the awkward symmetries of the problem conspire to make $P$ as a whole violate the principle. This looks to be the case if we focus on $P(H)$ as an adequate representation of that part of the belief state. But as noted earlier, this is not an adequate way of understanding the credal state. Note that while learning $Y$ and learning $Y'$ both prompt revision to a state where the posterior belief in $H$ is represented as an interval by $[0,1]$, the credal states *as sets of probabilities* are not the same. Call the state after learning $Y$, $P'$ and the state after learning $Y'$, $P''$. So $P' = \{p(\cdot \mid Y), p\in P\}$ and $P'' = \{p(\cdot\mid Y'), p\in P\}$. While it is true that $P'(H) = P''(H)$, $P' \neq P''$ as sets of probabilities, since if $p\in P'$ then $p(Y) = 1$ whereas if $p\in P''$ then $p(Y) = 0$. So one lesson we should learn from dilation is that imprecise belief is represented by *sets of functions* rather than by a set-valued function (see also, Joyce 2011; Topey 2012; Bradley and Steele 2014b)[^bradley-2014b][^joyce-2011][^topey-2012].

So dilation can perhaps be tamed or rationalised, and the issue with reflection can be mitigated. But there is still a puzzle that dilation raises: in the precise context we have a nice result – due to Good (1967) – that says roughly that learning new information has positive expected value. Information has positive value. This result is, to some extent, undermined by dilation. Bradley and Steele (2016) suggest that there is some sense in which Good’s result can be partially salvaged in the IP setting.

It seems that examples of dilation undermine the earlier claim that imprecise probabilities allow you to represent the difference between the weight and balance of evidence (see section 2.3): learning $Y$ appears to give rise to a belief which one would consider as representing *less evidence* since it is more spread out. This is so because the prior credence in the dilation case is precise, not through weight of evidence, but through the symmetry discussed earlier. We cannot take narrowness of the interval $[\underline{P}(X), \overline{P}(X)]$ as a characterisation of weight of evidence since the interval can be narrow for reasons other than because lots of evidence has been accumulated. So my earlier remarks on weight/balance should not be read as the claim that imprecise probabilities can always represent the weight/balance distinction. What is true is that *there are* cases where imprecise probabilities can represent the distinction in a way that impacts on decision making. This issue is far from settled and more work needs to be done on this topic.

### 3.2 Belief inertia

Imagine there are two live hypotheses $H_1$ and $H_2$. You have no idea how likely they are, but they are mutually exclusive and exhaustive. Then you acquire some evidence $E$. Some simple probability theory shows that for every $p\in P$ we have the following relationship (using $p_i = p(E\mid H_i)$ for $i=1,2$).

$$\begin{align} p(H_1\mid E) & = {{p(E\mid H_1)p(H_1)} \over {p_1 p(H_1) +p_2 p(H_2)}} \\ & = {{p_1 p(H_1)} \over {p_2 + (p_1 - p_2) p(H_1)}}\\ \end{align}$$

If your prior in $H_1$ is *vacuous*—if $P(H_1) = [0,1]$—then the above equation shows that your posterior is vacuous as well. That is, if $p(H_1) = 0$ then $p(H_1\mid E) = 0$ and likewise for $p(H_1) = 1 = p(H_1\mid E)$, and since the right hand side of the above equation is a continuous function of $p(H_1)$, for every $r\in [0,1]$ there is some $p(H_1)$ such that $p(H_1\mid E) = r$. So $P(H_1\mid E)=[0,1]$.

It seems like the imprecise probabilist cannot learn from vacuous priors. This problem of belief inertia goes back at least as far as Levi (1980), chapter 13. Walley also discusses the issue, but appears unmoved by it: he says that vacuous posterior probabilities are just a consequence of adopting a vacuous prior:

> The vacuous previsions really are rather trivial models. That seems appropriate for models of “complete ignorance” which is a rather trivial state of uncertainty. On the other hand, one cannot expect such models to be very useful in practical problems, notwithstanding their theoretical importance. If the vacuous previsions are used to model prior beliefs about a statistical parameter for instance, they give rise to vacuous posterior previsions… However, prior previsions that are close to vacuous and make nearly minimal claims about prior beliefs can lead to reasonable posterior previsions. (Walley 1991: 93)[^walley-1991]

Joyce (2011) and Rinard (2013) have both discussed this problem. Rinard’s solution to it is to argue that this shows that the vacuous prior is never a legitimate state of belief. Or rather, that we only ever need to model your beliefs using non-vacuous priors, even if these are incomplete descriptions of your belief state. This is similar to Walley’s “non-exhaustive” representation of belief. Vallinder (2018) suggests that the problem of belief inertia is quite a general one. Castro and Hart (forthcoming) use the looming danger of belief inertia to argue against what I have called an "objectivist" interpretation of IP.

An alternative solution to this problem, (inspired by Wilson 2001; and Cattaneo 2008; 2014)[^cattaneo-2008][^wilson-2001], would modify the update rule in such a way that those extreme priors that give extremely small likelihoods to the evidence are excised from the representor. More work would need to be done to make this precise and show how exactly the response would go.

### 3.3 Decision making

One important use that models of belief can be put to is as part of a theory of rational decision. IP is no different. Decision making with imprecise probabilities has some problems, however.

The problem for IP decision making, in short, is that your credal committee can disagree on what the best course of action is, and when they do, it is unclear how you should act (recall the definitions in section 1.1). Imagine betting on a coin of unknown bias. Consider the indicator gambles on heads and tails. Both bets have imprecise expectation $[0,1]$. How are you supposed to compare these expectations? The bets are incomparable. (If the coin case appears to have too much exploitable symmetry, consider unit bets on Elga pulling toothpaste or jellyfish from his bag.) This incomparability, argues Williamson, leads to decision making paralysis, and this highlights a flaw in the epistemology (2010: 70). This argument seems to be missing the point, however, if one of our motivations for IP is precisely to be able to represent such incompatibility of prospects (see section 2.2)! The incommensurability of options entailed by IP is not a bug, it’s a feature. Decision making with imprecise probabilities is discussed by Seidenfeld (2004), Troffaes (2007), Seidenfeld, Schervish, and Kadane (2010), Bradley (2015), Williams (2014), Huntley, Hable, and Troffaes (2014).

A more serious worry confronts IP when you have to make sequences of decisions. There is a rich literature in economics on sequences of decisions for agents who fail to be orthodox expected utility maximisers (Seidenfeld 1988; 1994; Machina 1989; Al-Najjar and Weinstein 2009, and the references therein)[^al-najjar-2009][^machina-1989][^seidenfeld-1988]. This topic was brought to the attention of philosophers again after the publication of Elga’s (2010) paper *Subjective Probabilities Should Be Sharp* which highlights the problem with a simple decision example, although a very similar example appears in Hammond (1988) in relation to Seidenfeld’s discussion of Levi’s decision rule “E-admissibility” (Seidenfeld 1988)[^seidenfeld-1988].

A version of the problem is as follows. You are about to be offered two bets on a coin of unknown bias, $A$ and $B$, one after the other. The bets pay out as follows:

- $A$ loses 10 if the coin lands heads and wins 15 otherwise
- $B$ wins 15 if the coin lands heads and loses 10 otherwise

If we assume you have beliefs represented by $P(H)=[0,1]$, these bets have expectations of $[-10,15]$. Refusing each bet has expectation of 0. So accepting and refusing $A$ are incomparable with respect to your beliefs. Likewise for $B$. The problem is that refusing *both* bets seems to be irrational, since accepting both bets gets you a guaranteed payoff of 5. Elga argues that no decision rule for imprecise probabilities can rule out refusing both bets. He then argues that this shows that imprecise probabilities are bad epistemology. Neither argument works. Chandler (2014) and Sahlin and Weirich (2014) both point out that a certain kind of imprecise decision rule does make refusing both bets impermissible and Elga has acknowledged this in an erratum to his paper. Bradley and Steele (2014a) argue that decision rules that make refusing both bets merely permissible are legitimate ways to make imprecise decisions. They also point out that the rule that Chandler, and Sahlin and Weirich advocate has counterintuitive consequences in other decision problems.

Moss (2015) relates Elga-style IP decision problems to moral dilemmas and uses the analogy to explain the conflicting intuitions in Elga’s problem. Sud (2014) and Rinard (2015) both also offer alternative decision theories for imprecise probabilities. Bradley (2019) argues that all three struggle to accommodate a version of the Ellsberg decisions discussed above.

Even if Elga’s argument worked and there were no good imprecise decision rules, that wouldn’t show that IP was a faulty model of belief. We want to be able to represent the suspension of judgement on various things, including on the relative goodness of a number of options. Such incommensurability inevitably brings with it some problems for sequential decisions (see, for example, Broome 2000)[^broome-2000], but this is not an argument against the epistemology. As Bradley and Steele note, Elga’s argument—if it were valid—could *mutatis mutandis* be used as an argument that there are no incommensurable goods and this seems too strong.

### 3.4 Interpreting IP

Imprecise probabilities aren’t a radically new theory. They are merely a slight modification of existing models of belief for situations of ambiguity. Often your credences will be precise enough, and your available actions will be such that you act more or less *as if* you were a strict Bayesian. One might analogize imprecise probabilities as the “Theory of Relativity” to the strict Bayesian “Newtonian Mechanics”: all but indistinguishable in all but the most extreme situations. This analogy goes deeper: in both cases, the theories are “empirically indistinguishable” in normal circumstances, but they both differ radically in some conceptual respects. Namely, the role of absolute space in Newtonian mechanics/GR; how to model ignorance in the strict/imprecise probabilist case. Howson (2012) makes a similar analogy between modelling belief and models in science. Both involve some requirement to be somewhat faithful to the target system, but in each case faithfulness must be weighed up against various theoretical virtues like simplicity, computational tractability and so on. Likewise Hosni (2014) argues that what model of belief is appropriate is somewhat dependent on context. There is of course an important disanalogy in that models of belief are supposed to be *normative* as well as descriptive, whereas models in science typically only have to play a descriptive role. Walley (1991) discusses a similar view but is generally sceptical of such an interpretation.

#### 3.4.1 What is a belief?

One standard interpretation of the probability calculus is that probabilities represent “degrees of belief” or “credences”. This is more or less the concept that under consideration so far. But what is a degree of belief? There are a number of ways of cashing out what it is that a representation of degree of belief is actually representing.

One of the most straightforward understandings of degree of belief is that credences are interpreted in terms of an agent’s limiting willingness to bet. This is an idea which goes back to Ramsey (1926) and de Finetti (1964, 1990 [1974]). The idea is that your credence in $X$ is $\alpha$ just in case $\alpha$ is the value at which you are indifferent between the gambles:

- Win $1-\alpha$ if $X$, lose $\alpha$ otherwise
- Lose $1- \alpha $ if $X$, win $\alpha$ otherwise

This is the “betting interpretation”. This is the interpretation behind Dutch book arguments: this interpretation of belief makes the link between betting quotients and belief strong enough to sanction the Dutch book theorem’s claim that *beliefs* must be probabilistic. Williamson in fact takes issue with IP because IP cannot be given this betting interpretation (2010: 68–72). He argues that Smith’s and Walley’s contributions notwithstanding (see [formal appendix](imprecise-probabilities.supplement-formal.md)), the single-value betting interpretation makes sense as a standard for credence in a way that the one-sided betting interpretation doesn’t. The idea is that you may refuse all bets unless they are at extremely favourable odds by your lights. Such behaviour doesn’t speak to your credences. However, *if you were to offer a single value* then this tells us something about your epistemic state. There is something to this idea, but it must be traded off against the worry that *forcing* agents to have such single numbers systematically misrepresents their epistemic states. As Kaplan puts it

> The mere fact that you nominate $0.8$ under the *compulsion* to choose some determinate value for [$p(X)$] hardly means that you have a *reason* to choose $0.8$. The orthodox Bayesian is, in short, guilty of advocating false precision. (Kaplan 1983: 569, Kaplan’s emphasis)[^kaplan-1983]

A related interpretation of credence is to understand credence as being just a representation of an agent’s dispositions to act. This interpretation sees credence as that function such that your elicited preferences and observed actions can be represented as those of an expected utility maximiser with respect to that probability function (Briggs 2014: section 2.2)[^briggs-2014]. Your credences *just are* that function that represents you as a rational agent. For precise probabilism, “rational agent” means “expected utility maximiser”. For imprecise probabilism, rational agent must mean something slightly different. A slightly more sophisticated version of this sort of idea is to understand credence to be exactly that component of the preference structure that the probability function represents in the representation theorem. Recall the discussion of incompleteness (section 2.2). IP represents you as the agent conflicted between all the $p \in P$ such that unless the $p$ agree that $X$ is better than $Y$ or vice versa, you find them incomparable. What a representation theorem actually proves is a matter of some dispute (see Zynda 2000; Hájek 2008; Meacham and Weisberg 2011)[^hájek-2008][^meacham-2011][^zynda-2000].

One might take the view that credence is modelling some kind of mental or psychological quantity in the head. Strength of belief is a real psychological quantity and it is this that credence should measure. Unlike the above views, this interpretation of credence isn’t easy to operationalise. It also seems like this understanding of strength of belief distances credence from its role in understanding decision making. The above *behaviourist* views take belief’s role in decision making to be central to or even definitional of what belief is. This psychological interpretation seems to divorce belief from decision. Whether there are such stable neurological structures is also a matter of some controversy (Fumagalli 2013; Smithson and Pushkarskaya 2015)[^fumagalli-2013][^smithson-2015].

A compromise between the behaviourist views and the psychological views is to say that belief is characterised *in part* by its role in decision making. This leaves room for belief to play an important role in other things, like assertion or reasoning and inference. So the answer to the question “What is degree of belief?” is: “Degree of belief is whatever psychological factors play the role imputed to belief in decision making contexts, assertion behaviour, reasoning and inference”. There is room in this characterisation to understand credence as measuring some sort of psychological quantity that causally relates to action, assertion and so on. This is a sort of functionalist reading of what belief is. Eriksson and Hájek (2007) argue that “degree of belief” should just be taken as a primitive concept in epistemology. The above attempts to characterise degree of belief then fill in the picture of the role degree of belief plays.

#### 3.4.2 What is a belief in $X$?

So now we have a better idea of what it is that a model of belief should do. But which part of our model of belief is representing which part of the belief state? The first thing to say is that $P(X)$ is *not* an adequate representation of the belief in $X$. That is, one of the values of the credal set approach is that it can capture certain kinds of non-logical relationships between propositions that are lost when focusing on, say, the associated set of probability values. For example, consider tossing a coin of unknown bias. $P(H)=P(T)=[0,1]$, but this fails to represent the important fact that $p(H)=1-p(T)$ for all $p\in P$. Or that getting a heads on the first toss is at least as likely as heads on two consecutive tosses. These facts that aren’t captured by the sets-of-values view can play an important role in reasoning and decision.

$P(X)$ might be a *good enough* representation of belief for some purposes. For example in the Ellsberg game these sets of probability values (and their associated sets of expectations) are enough to rationalise the non-probabilistic preferences. How good the representation needs to be depends on what it will be used for. Representing the sun as a point mass is a good enough representation for basic orbital calculations, but obviously inadequate if you are studying coronal mass ejections, solar flares or other phenomena that depend on details of the internal dynamics of the sun.

### 3.5 Regress

Imprecise probabilities is a theory born of our limitations as reasoning agents, and of limitations in our evidence base. If only we had better evidence, a single probability function would do. But since our evidence is weak, we must use a set. In a way, the same is true of precise probabilism. If only we knew the truth, we could represent belief with a truth-valuation function, or just a set of sentences that are fully believed. But since there are truths we don’t know, we must use a probability to represent our intermediate confidence. And indeed, the same problem arises for the imprecise probabilist. Is it reasonable to assume that we know what set of probabilities best represents the evidence? Perhaps we should have a set of sets of probabilities… Similar problems arise for theories of vagueness (Sorensen 2012)[^sorensen-2012]. We objected to precise values for degrees of belief, so why be content with sets-valued beliefs with precise boundaries? This is the problem of “higher-order vagueness” recast as a problem for imprecise probabilism. Why is sets of probabilities the right level to stop the regress at? Why not sets of sets? Why not second-order probabilities? Why not single probability functions? Williamson (2014) makes this point, and argues that a single precise probability is the correct level at which to get off the “uncertainty escalator”. Williamson advocates the betting interpretation of belief, and his argument here presupposes that interpretation. But the point is still worth addressing: for a particular interpretation of what belief is, what sort of level of uncertainty is appropriate. For the *functionalist* interpretation suggested above, this is something of a pragmatic choice. The further we allow this regress to continue, the harder it is to deal with these belief-representing objects. So let’s not go further than we need.

We have seen arguments above that IP does have some advantage over precise probabilism, in the capacity to represent suspending judgement, the difference between weight and balance of evidence and so on. So we must go *at least* this far up the uncertainty escalator. But for the sake of practicality we need not go any further, even though there are hierarchical Bayes models that would give us a well-defined theory of higher-order models of belief. This is, ultimately, a pragmatic argument. Actual human belief states are probably immensely complicated neurological patterns with all the attendant complexity, interactivity, reflexivity and vagueness. We are *modelling* belief, so it is about choosing a model at the right level of complexity. If you are working out the trajectory of a cannonball on earth, you can safely ignore the gravitational influence of the moon on the cannonball. Likewise, there will be contexts where simple models of belief are appropriate: perhaps your belief state is just a set of sentences of a language, or perhaps just a single probability function. If, however, you are modelling the tides, then the gravitational influence of the moon needs to be involved: the model needs to be more complex. This suggests that an adequate model of belief under severe uncertainty may need to move beyond the single probability paradigm. But a pragmatic argument says that we should only move as far as we need to. So while you need to model the moon to get the tides right, you can get away without having Venus in your model. This relates to the contextual nature of appropriateness for models of belief mentioned earlier. If one were attempting to provide a *complete* formal characterisation of the ontology of belief, then these regress worries would be significantly harder to avoid.

Let’s imagine that we had a second order probability $\mu$ defined over the set of (first order) probabilities $P$. We could then reduce uncertainty to a single function by $p^*(X) = \sum_P \mu(p)p(X)$ (if $P$ is finite, in the interests of keeping things simple I discuss only this case). Now if $p^*(X)$ is what is used in decision making, then there is no real sense in which we have a genuine IP model, and it cannot rationalise the Ellsberg choice, nor can it give rise to incomparability. If there is some alternative use that $\mu$ is put to, a use that allows incomparability and that rationalises Ellsberg choices, then it might be a genuine rival to credal sets, but it represents just as much of a departure from the orthodox theory as IP does.

Gärdenfors and Sahlin’s *Unreliable Probabilities* model enriches a basic IP approach with a “reliability index” (see the [historical appendix](imprecise-probabilities.supplement-historical.md)). Lyon (2017) enriches the standard IP picture in a different way: he adds a privileged “best guess” probability. This modification allows for better aggregation of elicited IP estimates. How best to interpret such a model is still an open question. Other enriched IP models are no doubt available.

### 3.6 What makes a good imprecise belief?

There are, as we have seen, certain structural properties that are necessary conditions on rational belief. What exactly these are depends on your views. However, there are further ways of assessing belief. Strongly believing true things and strongly believing the negations of false things seem like good-making-features of beliefs. For the case of precise credences, we can make this precise. There is a large literature on “scoring rules”: methods for measuring how good a probability is relative to the actual state of the world (Brier 1950; Savage 1971; Joyce 2009; Pettigrew 2011)[^brier-1950][^joyce-2009][^pettigrew-2011][^savage-1971]. These are numerical methods of measuring how good a probability is given the true state of the world.

For the case of imprecise probabilities, however, the situation looks bleak. No real valued scoring rule for imprecise probabilities can have the desirable property of being *strictly proper* (Seidenfeld, Schervish, and Kadane 2012)[^seidenfeld-2012]. Schoenfield (2017) presents a simple version of the result. Since strict propriety is a desirable property of a scoring rule (Bröcker and Smith 2007; Joyce 2009; Pettigrew 2011)[^bröcker-2007][^joyce-2009][^pettigrew-2011], this failing is serious. So further work is needed to develop a well-grounded theory of how to assess imprecise probabilities. Mayo-Wilson and Wheeler (2016) provide a neater version of the proof, and offer a property weaker than strict propriety that an imprecise probability scoring rule can satisfy. Carr (2015) and Konek (forthcoming) both present positive suggestions for moving forward with imprecise scoring rules. Levinstein (forthcoming) suggests that the problem really only arises for determinately imprecise credences, but not for indeterminate credence.

## 4. Summary

Imprecise probabilities offer a model of rational belief that does away with some of the idealisation required by the orthodox precise probability approach. Many motivations for such a move have been put forward, and many views on IP have been discussed. There are still several open philosophical questions relating to IP, and this is likely to be a rich field of research for years to come.

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=imprecise-probabilities). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/imprecise-probabilities/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=imprecise-probabilities&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](http://philpapers.org/sep/imprecise-probabilities/) at [PhilPapers](http://philpapers.org/), with links to its database. |

## Other Internet Resources

- Bradley, Seamus, 2013, “[Weak rationality and imprecise choice](http://www.lse.ac.uk/CPNSS/research/currentResearchProjects/ChoiceGroup/PDF_files/bradleyS-ImpreciseChoice.pdf),” LSE Choice Group Working Paper.
- Cozman, Fabio, [An Informal Introduction to the Theory of Sets of Probabilities](http://www.cs.cmu.edu/~qbayes/Tutorial/)
- [SIPTA: the Society for Imprecise Probability, Theory and Applications](http://www.sipta.org/)
- [PhilPapers category Imprecise Credences](http://philpapers.org/browse/imprecise-credences)

## Related Entries

belief, formal representations of | epistemic utility arguments for epistemic norms | epistemology: Bayesian | probability, interpretations of | rational choice, normative: expected utility | statistics, philosophy of | vagueness

### Acknowledgments

Many thanks to Teddy Seidenfeld, Greg Wheeler, Paul Pedersen, Aidan Lyon, Catrin Campbell-Moore, Stephan Hartmann, the ANU Philosophy of Probability Reading Group, and an anonymous referee for helpful comments on drafts of this article.

[^al-najjar-2009]: Al-Najjar, Nabil I., and Jonathan Weinstein, 2009, “The Ambiguity Aversion Literature: A Critical Assessment”, *Economics and Philosophy*, 25: 249–284.

[^augustin-2014]: Augustin, Thomas, Frank P.A. Coolen, Gert de Cooman, and Matthias C.M. Troffaes (eds), 2014, *Introduction to Imprecise Probabilities*, John Wiley and Sons. New York.

[^benétreau-dupin-2015]: Benétreau-Dupin, Yann, 2015, “The Bayesian who knew too much”, *Synthese*, 192:5 1527–1542.

[^binmore-2012]: Binmore, Ken and Lisa Stewart and Alex Voorhoeve, 2012, “How much ambiguity aversion? Finding indifferences between Ellsberg’s risk and ambiguous bets”, *Journal of Risk and Uncertainty*, 45: 215–238.

[^blackwell-1954]: Blackwell, D., and M. A. Girschick, 1954, *Theory of Games and Statistical Decisions*, Wiley. New York.

[^boole-1958]: Boole, George. 1958 [1854], *The Laws of Thought*, Dover. New York.

[^bovens-2003]: Bovens, Luc, and Stephan Hartmann, 2003, *Bayesian epistemology*, Oxford University Press. Oxford.

[^bradley-2009]: Bradley, Richard, 2009, “Revising Incomplete Attitudes”, *Synthese*, 171: 235–256.

[^bradley-2017]: –––, 2017, *Decision theory with a human face* Cambridge University Press. Cambridge.

[^bradley-2014]: Bradley, Richard, and Mareile Drechsler, 2014, “Types of Uncertainty”, *Erkenntnis*. 79: 1225–1248.

[^bradley-2015]: Bradley, Seamus, 2015, “How to choose among choice functions”, *Proceedings of the Ninth International Symposium on Imprecise Probability: Theories and Applications*, 57–66 URL = <[http://www.sipta.org/isipta15/data/paper/9.pdf](http://www.sipta.org/isipta15/data/paper/9.pdf)>.

[^bradley-2016]: –––, 2016, “Vague chance?”, *Ergo*, 3:20

[^bradley-2019]: –––, 2019, “A counterexample to three imprecise decision theories”, *Theoria*, 85:1 18–30

[^bradley-2014a]: Bradley, Seamus, and Katie Steele, 2014a, “Should Subjective Probabilities be Sharp?” *Episteme*, 11: 277–289.

[^bradley-2014b]: –––, 2014b, “Uncertainty, Learning and the ‘Problem’ of Dilation”, *Erkenntnis*. 79: 1287–1303.

[^bradley-2016-2]: –––, 2016, “Can free evidence be bad? Value of information for the imprecise probabilist”, *Philosophy of Science*, 83:1 1–28

[^brady-2012]: Brady, Michael and Rogério Arthmar, 2012, “Keynes, Boole and the interval approach to probability”, *History of Economic Ideas*, 20:3 65–84.

[^brier-1950]: Brier, Glenn, 1950, “Verification of Forecasts Expressed in Terms of Probability”, *Monthly Weather Review*, 78: 1–3.

[^briggs-2014]: Briggs, R.A., 2014, “Normative Theories of Rational Choice: Expected Utility”, *The Stanford Encyclopedia of Philosophy*, (Fall 2014 Edition), Edward N. Zalta (ed.), URL = <[https://plato.stanford.edu/archives/fall2014/entries/rationality-normative-utility/](https://plato.stanford.edu/archives/fall2014/entries/rationality-normative-utility/)>.

[^broome-2000]: Broome, John, 2000, “Incommensurable Values”, in *Well-Being and Morality: Essays in Honour of James Griffin*, R. Crisp and B. Hooker (eds), 21–38, Clarendon Press. Oxford.

[^bröcker-2007]: Bröcker, Jochen, and Leonard A. Smith, 2007, “Scoring Probabilistic Forecasts; On the Importance of Being Proper”, *Weather and Forecasting*, 22: 382–388.

[^camerer-1992]: Camerer, Colin, and Martin Weber, 1992, “Recent Developments in Modeling Preferences: Uncertainty and Ambiguity”, *Journal of Risk and Uncertainty*, 5: 325–370.

[^carr-2015]: Carr, Jennifer, 2015 “Chancy accuracy and imprecise credence”, *Philosophical Topics* 29 67–81.

[^castro-nd]: Castro, Clinton and Casey Hart, forthcoming, “The imprecise impermissivists dilemma”, *Synthese*.

[^cattaneo-2008]: Cattaneo, Marco, 2008, “Fuzzy Probabilities based on the Likelihood Function”, in *Soft Methods for Handling Variability and Imprecision*, D. Dubois, M. A. Lubiano, H. Prade, M. A. Gil, P. Grzegorzewski, and O. Hryniewicz (eds), 43–50, Springer.

[^cattaneo-2014]: –––, 2014, “A Continuous Updating Rule for Imprecise Probabilities”, in *Information Processing and Management of Uncertainty in Knowledge Based Systems*, Anne Laurent, Oliver Strauss, Bernadette Bouchon-Meunier, and Ronald R. Yager (eds), 426–435, Springer.

[^chandler-2014]: Chandler, Jacob, 2014, “Subjective Probabilities Need Not Be Sharp”, *Erkenntnis*. 79: 1273–1286.

[^chu-2004]: Chu, Francis, and Joseph Y. Halpern, 2004, “Great expectations. Part II: Generalized expected utility as a universal decision rule”, *Artificial Intelligence*, 159: 207–230.

[^chu-2008]: –––, 2008, “Great expectations. Part I: On the customizability of General Expected Utility”, *Theory and Decision*, 64: 1–36.

[^clifford-1901]: Clifford, William Kingdom, 1901, “The Ethics of Belief”, in *Lectures and Essays*, Leslie Stephen and Frederick Pollock (eds), 2:161–205, 3ʳᵈ Edition, Macmillan. London.

[^cooman-2007]: de Cooman, Gert, and Enrique Miranda, 2007, “Symmetry of models versus models of symmetry”, in *Probability and Inference: Essays in Honor of Henry E. Kyburg Jnr.*, William Harper and Gregory Wheeler (eds), 67–149, Kings College Publications.

[^cozman-2000]: Cozman, Fabio, 2000, “Credal Networks”, *Artificial Intelligence*, 120: 199–233.

[^cozman-2012]: –––, 2012, “Sets of probability distributions, independence and convexity”, *Synthese*, 186: 577–600.

[^cozman-2005]: Cozman, Fabio, and Peter Walley, 2005, “Graphoid properties of epistemic irrelevance and independence”, *Annals of Mathematics and Artificial Intelligence*, 45: 173–195.

[^dardashti-2014]: Dardashti, Radin, Luke Glynn, Karim Thébault, and Mathias Frisch, 2014, “Unsharp Humean chances in statistical physics: a reply to Beisbart”, in *New Directions in the Philosophy of Science*, Maria Carla Galavotti, Dennis Dieks, Wenceslao J. Gonzalez, Stephan Hartmann, Thomas Uebel, and Marcel Weber (eds), 531–542, Springer. Dordrecht.

[^elga-2010]: Elga, Adam, 2010, “Subjective Probabilities should be Sharp”, *Philosophers’ Imprint*, 10.

[^elkin-2016]: Elkin, Lee and Gregory Wheeler, 2016 “Resolving peer disagreements through imprecise probabilities”, *Noûs*, 52:2 260–278.

[^ellsberg-1961]: Ellsberg, Daniel, 1961, “Risk, ambiguity and the Savage axioms”, *Quarterly Journal of Economics*, 75: 643–696.

[^eriksson-2007]: Eriksson, Lena, and Alan Hájek, 2007, “What Are Degrees of Belief?” *Studia Logica*, 86: 183–213.

[^evren-2011]: Evren, Özgür, and Efe Ok, 2011, “On the multi-utility representation of preference relations”, *Journal of Mathematical Economics*, 47: 554–563.

[^ferson-1996]: Ferson, Scott and Lev R. Ginzburg,1996, “Different methods are needed to propagate ignorance and variability”, *Reliability Engineering and System Safety*, 54 133–144.

[^ferson-2004]: Ferson, Scott and Janos G. Hajagos, 2004, “Arithmetic with uncertain numbers: Rigorous and (often) best possible answers”, *Reliability Engineering and System Safety*, 85 135–152.

[^fine-1973]: Fine, Terrence L., 1973, *Theories of Probability: An Examination of Foundations*, Academic Press. New York.

[^fine-1988]: –––, 1988, “Lower Probability Models for Uncertainty and Nondeterministic Processes”, *Journal of Statistical Planning and Inference*, 20: 389–411.

[^finetti-1964]: de Finetti, Bruno, 1964, “Foresight: Its Logical Laws, Its Subjective Sources”, in *Studies in Subjective Probability Studies in Subjective Probability*, Henry E. Kyburg and Howard E. Smokler (eds), 97–158, Wiley. New York.

[^finetti-1990]: –––, 1990 [1974], *Theory of Probability*, Wiley Classics Library, Vol. 1, Wiley. New York.

[^fox-1995]: Fox, Craig R., and Amos Tversky, 1995, “Ambiguity aversion and comparative ignorance”, *Quarterly Journal of Economics*, 110: 585–603.

[^fraassen-1984]: van Fraassen, Bas, 1984, “Belief and the Will”, *Journal of Philosophy*, 81: 235–256.

[^fraassen-1990]: –––, 1990, “Figures in a Probability Landscape”, in *Truth or Consequences*, Michael Dunn and Anil Gupta (eds), 345–356, Springer. Dordrecht.

[^frigg-2008]: Frigg, Roman, 2008, “Humean chance in Boltzmannian statistical mechanics”, *Philosophy of Science*, 75: 670–681.

[^frigg-2014]: Frigg, Roman, Seamus Bradley, Hailiang Du, and Leonard A. Smith, 2014, “Laplace’s Demon and the Adventures of his Apprentices”, *Philosophy of Science*, 81: 31–59.

[^fumagalli-2013]: Fumagalli, Roberto, 2013, “The Futile Search for True Utility”, *Economics and Philosophy*, 29: 325–347.

[^gärdenfors-1979]: Gärdenfors, Peter, 1979, “Forecasts, Decisions and Uncertain Probabilities”, *Erkenntnis*, 14: 159–181.

[^gärdenfors-1982]: Gärdenfors, Peter, and Nils-Eric Sahlin, 1982, “Unreliable probabilities, risk taking and decision making”, *Synthese*, 53: 361–386.

[^genest-1986]: Genest, Christian, and James V. Zidek, 1986, “Combining Probability Distributions: A Critique and Annotated Bibliography”, *Statistical Science*, 1: 114–135.

[^gilboa-1987]: Gilboa, Itzhak, 1987, “Expected Utility with Purely Subjective Non-additive Probabilities”, *Journal of Mathematical Economics*, 16: 65–88.

[^glymour-1980]: Glymour, Clark, 1980, “Why I am not a Bayesian”, in *Theory and Evidence*, 63–93. Princeton University Press. Princeton.

[^gong-2017]: Gong, Ruobin and Xiao-Li Meng, 2017 “Judicious judgment meets unsettling update: dilation, sure loss and Simpson’s paradox”, URL = <[https://arxiv.org/abs/1712.08946](https://arxiv.org/abs/1712.08946)>.

[^good-1962]: Good, Irving John, 1962, “Subjective probability as the measure of a non-measurable set”, in *Logic, Methodology and Philosophy of Science: Proceedings of the 1960 International Congress*, 319–329.

[^good-1967]: –––, 1967, “On the principle of total evidence”, *British Journal for the Philosophy of Science*, 17: 319–321.

[^good-1974]: –––, 1974, “A little learning can be dangerous”, *British Journal for the Philosophy of Science*, 25: 340–342.

[^good-1983]: –––, 1983 [1971], “Twenty-Seven principles of rationality”, in *Good Thinking: The Foundations of Probability and its Applications Good Thinking: The Foundations of Probability and its Applications*, 15–19. University of Minnesota Press. Minnesota.

[^grize-1987]: Grize, Yves L., and Terrence L. Fine, 1987, “Continuous Lower Probability-Based Models for Stationary Processes with Bounded and Divergent Time Averages”, *The Annals of Probability*, 15: 783–803.

[^haenni-2009]: Haenni, Rolf, 2009, “Non-additive degrees of belief”, in Huber and Schmidt-Petri 2009: 121–160.

[^haenni-2011]: Haenni, Rolf, Jan-Willem Romeijn, Gregory Wheeler, and Jon Williamson, 2011, *Probabilistic Logic and Probabilistic Networks*, Synthese Library. Dordrecht.

[^hájek-2003]: Hájek, Alan, 2003, “What conditional probabilities could not be”, *Synthese*, 137: 273–323.

[^hájek-2008]: –––, 2008, “Arguments for—or against—probabilism?” *British Journal for the Philosophy of Science*, 59: 793–819.

[^hájek-2011]: –––, 2011, “Interpretations of Probability”, *The Stanford Encyclopedia of Philosophy* (Winter 2012 Edition), Edward N. Zalta (ed.), URL = <[https://plato.stanford.edu/archives/win2012/entries/probability-interpret/](https://plato.stanford.edu/archives/win2012/entries/probability-interpret/)>.

[^hájek-2012]: Hájek, Alan, and Michael Smithson, 2012, “Rationality and Indeterminate Probabilities”, *Synthese*, 187: 33–48.

[^halpern-2003]: Halpern, Joseph Y., 2003, *Reasoning about uncertainty*, MIT press. Cambridge.

[^hammond-1988]: Hammond, Peter, 1988, “Orderly Decision Theory”, *Economics and Philosophy*, 4: 292–297.

[^harsanyi-1955]: Harsanyi, John, 1955, “Cardinal welfare, individualistic ethics and interpersonal comparisons of utility”, *Journal of Political Economy*, 63: 309–321.

[^hart-2015]: Hart. Casey and Michael Titelbaum, 2015 “Intuitive dilation?”, *Thought*, 4 252–262.

[^hartmann-2010]: Hartmann, Stephan, and Patrick Suppes, 2010, “Entanglement, Upper Probabilities and Decoherence in Quantum Mechanics”, in *EPSA Philosophical Issues in the Sciences: Launch of the European Philosophy of Science Association*, Mauricio Suárez, Mauro Dorato, and Miklós Rédei (eds), 93–103, Springer.

[^hawthorne-2009]: Hawthorne, James, 2009, “The Lockean Thesis and the Logic of Belief”, in Huber and Schmidt-Petri 2009: 49–74.

[^herron-1994]: Herron, Timothy, Teddy Seidenfeld, and Larry Wasserman, 1994, “The Extent of Dilation of Sets of Probabilities and the Asymptotics of Robust Bayesian Inference”, in *PSA: Proceedings of the Biennial Meeting of the Philosophy of Science Association*, 250–259.

[^hill-2013]: Hill, Brian, 2013, “Confidence and decision”, *Games and Economic Behavior*, 82 675–692.

[^hosni-2014]: Hosni, Hykel, 2014, “Towards a Bayesian theory of second order uncertainty: Lessons from non-standard logics”, in *David Makinson on classical methods for non-classical problems*, Sven Ove Hansson (ed.), 195–221, Springer. Dordrecht.

[^howson-2012]: Howson, Colin, 2012, “Modelling Uncertain Inference”, *Synthese*, 186: 475–492.

[^howson-2006]: Howson, Colin, and Peter Urbach, 2006, *Scientific Reasoning: the Bayesian Approach*, 3ʳᵈ edition, Open Court. Chicago.

[^huber-2009]: Huber, Franz, 2009, “Belief and Degrees of Belief”, in Huber and Schmidt-Petri 2009: 1–33.

[^huber-2014]: –––, 2014, “Formal Representations of Belief”, *Stanford Encyclopedia of Philosophy* (Spring 2014 Edition), E. N. Zalta (ed.), URL = <[https://plato.stanford.edu/archives/spr2014/entries/formal-belief/](https://plato.stanford.edu/archives/spr2014/entries/formal-belief/)>.

[^huber-2009-2]: Huber, Franz and Cristoph Schmidt-Petri (eds), 2009, *Degrees of Belief*, Springer. Dordrecht.

[^huntley-2014]: Huntley, Nathan, Robert Hable, and Matthias Troffaes, 2014, “Decision making”, in Augustin et al. 2014: 190–206.

[^james-1897]: James, William, 1897, “The Will to Believe”, in *The Will to Believe and other essays in popular philosophy*, 1–31. Longmans, Green and Co. New York.

[^jaynes-2003]: Jaynes, Edwin T., 2003, *Probability Theory: The Logic of Science*, Cambridge University Press. Cambridge.

[^jeffrey-1983]: Jeffrey, Richard, 1983, *The Logic of Decision*, 2ⁿᵈ edition. University of Chicago Press. Chicago.

[^jeffrey-1984]: –––, 1984, “Bayesianism with a Human Face”, in *Testing Scientific Theories*, John Earman (ed.), 133–156, University of Minnesota Press. Minnesota.

[^jeffrey-1987]: –––, 1987, “Indefinite Probability Judgment: A Reply to Levi”, *Philosophy of Science*, 54: 586–591.

[^joyce-1999]: Joyce, James M., 1999, *The Foundations of Causal Decision Theory*, *Cambridge studies in probability, induction and decision theory*, Cambridge University Press. Cambridge.

[^joyce-2005]: –––, 2005, “How Probabilities Reflect Evidence”, *Philosophical Perspectives*, 19: 153–178.

[^joyce-2009]: –––, 2009, “Accuracy and Coherence: Prospects for an Alethic Epistemology of Partial Belief”, in Huber and Schmidt-Petri 2009: 263–297.

[^joyce-2011]: –––, 2011, “A Defense of Imprecise Credence in Inference and Decision”, *Philosophical Perspectives*, 24: 281–323.

[^kadane-1999]: Kadane, Joseph B., Mark J. Schervish, and Teddy Seidenfeld, 1999, *Rethinking the Foundations of Statistics*, Cambridge University Press. Cambridge.

[^kaplan-1983]: Kaplan, Mark, 1983, “Decision theory as philosophy”, *Philosophy of Science*, 50: 549–577.

[^kaplan-1996]: –––, 1996, *Decision Theory as Philosophy*, Cambridge University Press. Cambridge.

[^keynes-1921]: Keynes, J. M., 1921, *A Treatise on Probability*, Macmillan. London.

[^konek-nd]: Konek, Jason, forthcoming “Epistemic conservativity and imprecise credence”, *Philosophy and Phenomenological Research*

[^koopman-1940]: Koopman, B. O., 1940, “The Bases of Probability”, *Bulletin of the American Mathematical Society*, 46: 763–774.

[^kumar-1985]: Kumar, Anurag, and Terrence L. Fine, 1985, “Stationary Lower Probabilities and Unstable Averages”, *Zeitschrift für Wahrscheinlichkeitstheorie und verwandte Gebiete*, 69: 1–17.

[^kyburg-1983]: Kyburg, Henry E., 1983, “Rational belief”, *The Brain and Behavioural Sciences*, 6: 231–273.

[^kyburg-1987]: –––, 1987, “Bayesian and non-Bayesian evidential updating”, *Artificial Intelligence*, 31: 271–293.

[^kyburg-2003]: –––, 2003, “Are there degrees of belief?” *Journal of Applied Logic*: 139–149.

[^kyburg-1992]: Kyburg, Henry E., and Michael Pittarelli, 1992, *Set-based Bayesianism*.

[^kyburg-2001]: Kyburg, Henry E., and Choh Man Teng, 2001, *Uncertain Inference*, Cambridge University Press. Cambridge.

[^leitgeb-2014]: Leitgeb, Hannes, 2014, “The stability theory of belief”, *The Philosophical Review*, 123: 131–171.

[^levi-1974]: Levi, Isaac, 1974, “On Indeterminate probabilities”, *Journal of Philosophy*, 71: 391–418.

[^levi-1980]: –––, 1980, *The Enterprise of Knowledge*, The MIT Press. Cambridge.

[^levi-1982]: –––, 1982, “Ignorance, Probability and Rational Choice”, *Synthese*, 53: 387–417.

[^levi-1985]: –––, 1985, “Imprecision and Indeterminacy in Probability Judgment”, *Philosophy of Science*, 52: 390–409.

[^levi-1986]: –––, 1986, *Hard Choices: decision making under unresolved conflict*, Cambridge University Press. Cambridge.

[^levi-1999]: –––, 1999, “Value commitments, value conflict and the separability of belief and value”, *Philosophy of Science*, 66: 509–533.

[^levinstein-nd]: Levinstein, Ben, forthcoming, “Imprecise epistemic values and imprecise credences”, *Australasian Journal of Philosophy*.

[^lewis-1986]: Lewis, David, 1986, “A Subjectivist’s Guide to Objective Chance (and postscript)”, in *Philosophical Papers II*, 83–132. Oxford University Press. Oxford.

[^lewis-1994]: –––, 1994, “Humean Supervenience Debugged”, *Mind*, 103: 473–490.

[^list-2011]: List, Christian, and Philip Pettit, 2011, *Group Agency*, Oxford University Press. Oxford.

[^loewer-2001]: Loewer, B., 2001, “Determinism and chance”, *Studies in the History and Philosophy of Modern Physics*, 32: 609–620.

[^lyon-2017]: Lyon, Aidan, 2017, “Vague Credences”, *Synthese*, 194:10 3931–3954.

[^machina-1989]: Machina, Mark J., 1989, “Dynamic Consistency and Non-Expected Utility Models of Choice Under Uncertainty”, *Journal of Economic Literature*, 27: 1622–1668.

[^mayo-wilson-2016]: Mayo-Wilson, Conor and Gregory Wheeler, 2016, “Scoring imprecise credences: a mildly immodest proposal”, *Philosophy and Phenomenological Research*, 93:1 55–78.

[^meacham-2011]: Meacham, Christopher, and Jonathan Weisberg, 2011, “Representation Theorems and the Foundations of Decision Theory”, *Australasian Journal of Philosophy*, 89: 641–663.

[^miranda-2008]: Miranda, Enrique, 2008, “A survey of the theory of coherent lower previsions”, *International Journal of Approcimate Reasoning*, 48: 628–658.

[^miranda-2014]: Miranda, Enrique, and Gert de Cooman, 2014, “Lower previsions”, in Augustin et al. 2014, pp. 28–55.

[^moss-2015]: Moss, Sarah, 2015, “Credal Dilemmas”, *Noûs*, 49:4 665–683.

[^norton-2007]: Norton, John, 2007, “Probability disassembled”, *British Journal for the Philosophy of Science*, 58: 141–171.

[^norton-2008a]: –––, 2008a, “Ignorance and Indifference”, *Philosophy of Science*, 75: 45–68.

[^norton-2008b]: –––, 2008b, “The dome: An Unexpectedly Simple Failure of Determinism”, *Philosophy of Science*, 75: 786–798.

[^oberguggenberger-2014]: Oberguggenberger, Michael, 2014, “Engineering”, in Augustin et al. 2014: 291–304.

[^oberkampf-2010]: Oberkampf, William and Christopher Roy, 2010 *Verification and Validation in Scientific Computing*, Cambridge University Press. Cambridge.

[^pedersen-2014]: Pedersen, Arthur Paul, 2014, “Comparative Expectations”, *Studia Logica*. 102: 811–848.

[^pedersen-2014-2]: Pedersen, Arthur Paul, and Gregory Wheeler, 2014, “Demystifying Dilation”, *Erkenntnis*.79: 1305–1342.

[^pettigrew-2011]: Pettigrew, Richard, 2011, “Epistemic Utility Arguments for Probabilism”, *The Stanford Encyclopedia of Philosophy* (Winter 2011 Edition), Edward N. Zalta (ed.), URL = <[https://plato.stanford.edu/archives/win2011/entries/epistemic-utility/](https://plato.stanford.edu/archives/win2011/entries/epistemic-utility/)>.

[^pfeifer-2007]: Pfeifer, Niki, and Gernot D. Kleiter, 2007, “Human reasoning with imprecise probabilities: Modus ponens and denying the antecedent”, *Proceedings of the 5th International Symposium on Imprecise Probability: Theory and Application*: 347–356.

[^quaeghebeur-2014]: Quaeghebeur, Erik, 2014, “Desirability”, in Augustin et al. 2014: 1–27.

[^ramsey-1926]: Ramsey, F. P., 1926, “Truth and Probability”, in *The Foundations of Mathematics and other Logical Essays*, 156–198. Routledge. London.

[^rinard-2013]: Rinard, Susanna, 2013, “Against Radical Credal Imprecision”, *Thought*, 2: 157–165.

[^rinard-2015]: –––, 2015, “A decision theory for imprecise probabilities”, *Philosophers’ Imprint*, 15 1–16.

[^ruggeri-2005]: Ruggeri, Fabrizio, David Ríos and Jacinto Martín, 2005, “Robust Bayesian analysis”, *Handbook of Statistics*, 25 623–667, Elsevier. Amsterdam

[^sahlin-2014]: Sahlin, Nils-Eric, and Paul Weirich, 2014, “Unsharp Sharpness”, *Theoria*, 80: 100–103.

[^savage-1972]: Savage, Leonard J., 1972 [1954], *The Foundations of Statistics*, 2nd edition, Dover. New York.

[^savage-1971]: –––, 1971, “Elicitation of Personal Probabilities and Expectation”, *Journal of the American Statistical Association*, 66: 783–801.

[^schaffer-2007]: Schaffer, Jonathan, 2007, “Deterministic Chance?” *British Journal for the Philosophy of Science*, 58: 114–140.

[^schervish-2008]: Schervish, Mark J., Teddy Seidenfeld, and Joseph B. Kadane, 2008, “The fundamental theorems of prevision and asset pricing”, *International Journal of Approximate Reasoning*, 49: 148–158.

[^schoenfield-2012]: Schoenfield, Miriam, 2012, “Chilling out on epistemic rationality”, *Philosophical Studies*, 158: 197–219.

[^schoenfield-2017]: –––, 2017, “The accuracy and rationality of imprecise credence”, *Noûs*, 51:4 667–685.

[^seidenfeld-1988]: Seidenfeld, Teddy, 1988, “Decision theory without ‘independence’ or without ‘ordering’. What’s the difference?” *Economics and Philosophy*: 267–290.

[^seidenfeld-1994]: –––, 1994, “When normal and extensive form decisions differ”, *Logic, Methodology and Philosophy of Science*, IX: 451–463.

[^seidenfeld-2004]: –––, 2004, “A contrast between two decision rules for use with (convex) sets of probabilities: Gamma-maximin versus E-admissibility”, *Synthese*, 140: 69–88.

[^seidenfeld-1989]: Seidenfeld, Teddy, Joseph B. Kadane, and Mark J. Schervish, 1989, “On the shared preferences of two Bayesian decision makers”, *The Journal of Philosophy*, 86: 225–244.

[^seidenfeld-1995]: Seidenfeld, Teddy, Mark J. Schervish, and Joseph B. Kadane, 1995, “A Representation of Partially Ordered Preferences”, *Annals of Statistics*, 23: 2168–2217.

[^seidenfeld-2010]: –––, 2010, “Coherent choice functions under uncertainty”, *Synthese*, 172: 157–176.

[^seidenfeld-2012]: –––, 2012, “Forecasting with imprecise probabilities”, *International Journal of Approximate Reasoning*, 53: 1248–1261.

[^seidenfeld-1993]: Seidenfeld, Teddy, and Larry Wasserman, 1993, “Dilation for sets of probabilities”, *Annals of Statistics*, 21: 1139–1154.

[^skyrms-2011]: Skyrms, Brian, 2011, “Resiliency, Propensities and Causal Necessity”, in *Philosophy of Probability: Contemporary Readings*, Antony Eagle (ed.), 529–536, Routledge. London.

[^smith-1961]: Smith, Cedric A.B, 1961, “Consistency in Statistical Inference and Decision”, *Journal of the Royal Statistical Society. Series B (Methodological)*, 23: 1–37.

[^smithson-2009]: Smithson, Michael, and Paul D. Campbell, 2009, “Buying and Selling Prices under Risk, Ambiguity and Conflict”, *Proceedings of the 6th International Symposium on Imprecise Probability: Theory and Application*.

[^smithson-2015]: Smithson, Michael, and Helen Pushkarskaya, 2015, “Ignorance and the Brain: Are there Distinct Kinds of Unknowns?” in *Routledge International Handbook of Ignorance Studies*, Matthias Gross and Linsey McGoey (eds), Routledge.

[^sorensen-2012]: Sorensen, Roy, 2012, “Vagueness”, *The Stanford Encyclopedia of Philosophy* (Winter 2013 Edition), Edward N. Zalta (ed.), URL = <[https://plato.stanford.edu/archives/win2013/entries/vagueness/](https://plato.stanford.edu/archives/win2013/entries/vagueness/)>.

[^stainforth-2007]: Stainforth, David A., Miles R. Allen, E. R. Tredger, and Leonard A. Smith, 2007, “Confidence uncertainty and decision-support relevance in climate models”, *Philosophical Transactions of the Royal Society*, 365: 2145–2161.

[^steele-2007]: Steele, Katie, 2007, “Distinguishing indeterminate belief from ‘risk averse’ preference”, *Synthese*, 158: 189–205.

[^stewart-2018]: Stewart, Rush T. and Ignacio Ojea Quintana, 2018 “Probabilistic opinion pooling with imprecise probabilities”, *Journal of Philosophical Logic*, 47:1 17–45.

[^sturgeon-2008]: Sturgeon, Scott, 2008, “Reason and the grain of belief”, *Noûs*, 42: 139–165.

[^sud-2014]: Sud, Rohan, 2014, “A forward looking decision rule for imprecise credences”, *Philosophical Studies*, 167 119–139.

[^suppes-1974]: Suppes, Patrick, 1974, “The Measurement of Belief”, *Journal of the Royal Statistical Society B*, 36: 160–191.

[^suppes-1991]: Suppes, Patrick, and Mario Zanotti, 1991, “Existence of Hidden Variables Having Only Upper Probability”, *Foundations of Physics*, 21: 1479–1499.

[^talbott-2008]: Talbott, William, 2008, “Bayesian Epistemology”, *The Stanford Encyclopedia of Philosophy* (Fall 2013 Edition), Edward N. Zalta (ed.), URL = <[https://plato.stanford.edu/archives/fall2013/entries/epistemology-bayesian/](https://plato.stanford.edu/archives/fall2013/entries/epistemology-bayesian/)>.

[^topey-2012]: Topey, Brett, 2012, “Coin flips, credences and the Reflection Principle”, *Analysis*, 72: 478–488.

[^trautmann-2016]: Trautmann, Stefan and Guijs van der Kuilen, 2016 “Ambiguity Attitudes”, *Blackwell Handbook of Judgement and Decision-Making*, 89–116.

[^troffaes-2007]: Troffaes, Matthias, 2007, “Decision Making under Uncertainty using Imprecise Probabilities”, *International Journal of Approximate Reasoning*, 45: 17–29.

[^troffaes-2014]: Troffaes, Matthias, and Gert de Cooman, 2014, *Lower Previsions*, Wiley. New York.

[^vallinder-2018]: Vallinder, Aron, 2018 “Imprecise Bayesianism and global belief inertia”, *British Journal for the Philosophy of Science*, 69:4 1205–1230.

[^vicig-2007]: Vicig, Paolo, Marco Zaffalon, and Fabio G. Cozman, 2007, “Notes on ‘Notes on conditional previsions’”, *International Journal of Approximate Reasoning*, 44: 358–365.

[^vicig-2012]: Vicig, Paolo, and Teddy Seidenfeld, 2012, “Bruno de Finetti and imprecision: Imprecise Probability Does not Exist!” *International Journal of Approximate Reasoning*, 53: 1115–1123.

[^voorhoeve-2016]: Voorhoeve, Alex, Ken Binmore, Arnaldur Stefansson and Lisa Stewart,2016 “Ambiguity attitudes, framing and consistency”, *Theory and Decision*, 81:3 313–337.

[^walley-1991]: Walley, Peter, 1991, *Statistical Reasoning with Imprecise Probabilities*, *Monographs on Statistics and Applied Probability*, Vol. 42. Chapman and Hall. London.

[^walley-1982]: Walley, Peter, and Terrence L. Fine, 1982, “Towards a frequentist theory of upper and lower probability”, *The Annals of Statistics*, 10: 741–761.

[^wallsten-1995]: Wallsten, Thomas, and David V. Budescu, 1995, “A review of human linguistic probability processing: General principles and empirical evidence”, *The Knowledge Engineering Review*, 10: 43–62.

[^weatherson-2002]: Weatherson, Brian, 2002, “Keynes, uncertainty and interest rates”, *Cambridge Journal of Economics*: 47–62.

[^weichselberger-2000]: Weichselberger, Kurt, 2000, “The theory of interval-probability as a unifying concept for uncertainty”, *International Journal of Approximate Reasoning*, 24: 149–170.

[^wheeler-2014]: Wheeler, Gregory, 2014, “Character matching and the Locke pocket of belief”, in *Epistemology, Context and Formalism*, Franck Lihoreau and Manuel Rebuschi (eds), 185–194, Synthese Library. Dordrecht.

[^wheeler-2011]: Wheeler, Gregory, and Jon Williamson, 2011, “Evidential Probability and Objective Bayesian Epistemology”, in *Philosophy of Statistics*, Prasanta S. Bandyopadhyay and Malcom Forster (eds), 307–332, North-Holland. Amsterdam.

[^white-2010]: White, Roger, 2010, “Evidential Symmetry and Mushy Credence”, in *Oxford Studies in Epistemology*, T. Szabo Gendler and J. Hawthorne (eds), 161–186, Oxford University Press.

[^williams-2014]: Williams, J. Robert G., 2014, “Decision-making under indeterminacy”, *Philosophers’ Imprint*, 14: 1–34.

[^williams-1976]: Williams, P. M., 1976, “Indeterminate Probabilities”, in *Formal Methods in the Methodology of Empirical Sciences*, Marian Przelęcki, Klemens Szaniawski, and Ryszard Wójcicki (eds), 229–246, D. Reidel Publishing Company.

[^williams-2007]: –––, 2007, “Notes on conditional previsions”, *International Journal of Approximate Reasoning*, 44: 366–383.

[^williamson-2010]: Williamson, Jon, 2010, *In Defense of Objective Bayesianism*, Oxford University Press. Oxford.

[^williamson-2014]: –––, 2014, “How uncertain do we need to be?” *Erkenntnis*. 79: 1249–1271.

[^wilson-2001]: Wilson, Nic, 2001, “Modified upper and lower probabilities based on imprecise likelihoods”, in *Proceedings of the 2nd International Symposium on Imprecise Probabilities and their Applications*.

[^zynda-2000]: Zynda, Lyle, 2000, “Representation Theorems and Realism about Degrees of Belief”, *Philosophy of Science*, 67: 45–69.
