# Normative Theories of Rational Choice: Rivals to Expected Utility
**First published Mon May 16, 2022**

*Buchak, Lara*

*Expected utility theory*, which holds that a decision-maker ought to maximize expected utility, is the prevailing theory of instrumental rationality. Nonetheless, four major challenges have arisen to the claim that the theory characterizes all rational preferences. These challenges are the phenomena of infinite or unbounded value, incommensurable goods, imprecise probabilities, and risk-aversion. The challenges have been accompanied by alternative theories that attempt to do better.

Expected utility theory consists of three components. The first is a utility function that assigns real numbers to consequences. The second is a probability function that assigns real numbers between 0 and 1 to every possible event. The final component is an “aggregation norm” that holds that the value of an act is its expected utility value relative to these two functions, and that rational preferences track expected utility value (see the entry on expected utility theory). Each challenge to EU theory can be thought of as a rejection of one or more of the three components as normative, and alternatives generally replace or extend the relevant component.

It has long been observed that typical individuals do not in fact conform to expected utility theory, and in response, a number of descriptive alternatives have arisen, particularly in the field of economics (see Starmer 2000, Sugden 2004, Schmidt 2004 for surveys; see also the entry on descriptive decision theory)[^schmidt-2004][^starmer-2000][^sugden-2004]. This article will primarily discuss views that have been put forth as normative.

## 1. Expected Utility Theory

### 1.1 The Theory

Decision theory concerns individuals’ preferences among both *consequences* (sometimes called “outcomes”) and *gambles*. The theory as originally developed focused on decisions with monetary consequences (e.g., receiving $10 in a game of chance), but subsequent developments broadened their focus to include decisions with non-monetary consequences as well (e.g., eating a large omelet, eating a smaller omelet, being stuck in the rain without an umbrella, lugging an umbrella around in the sunshine). Most contemporary authors define consequences to include any facts about a decision-maker’s situation that matter to her—so monetary consequences must technically describe a decision-maker’s total fortune, and non-monetary consequences must technically describe the entire world that the decision-maker finds herself in—though these full descriptions are often omitted when a decision will not alter the surrounding facts. Let the consequence set be $\cX.$ A *utility function* $\uf: \cX \rightarrow \cR$ assigns values to consequences, with the constraint that the individual prefers (or should prefer), of two consequences, the one with the higher utility value, and is indifferent between any two consequences with the same utility value. Thus the utility function in some sense represents how the individual values consequences.

Gambles come in one of two forms, depending on whether we are dealing with the “objective probability” or “subjective probability” version of the theory. In the objective probability version, a gamble is a *lottery* that assigns probabilities to consequences. Consider, for example, a lottery that yields $100 with probability 0.5, $300 with probability 0.3, and $200 with probability 0.2. We can represent this lottery as {$100, 0.5; $300, 0.3; $200, 0.2}. More generally, lotteries have the form $L = \{x_1, p_1;\ldots; x_n, p_n\},$ where $x_i \in \cX$ and $p_i$ is the probability that consequence $x_i$ obtains. Lotteries needn’t be restricted to a finite set of consequences; they could instead be continuous.

In the subjective probability version, a gamble is an *act* (sometimes called as “Savage act”; Savage 1954)[^savage-1954] that assigns consequences to possible states of the world. Consider, for example, the act of cracking an extra egg into one’s omelet, when the egg may be rotten: if the egg is fresh, the consequence will be a large omelet, but if the egg is rotten, the consequence will be a ruined omelet. We can represent this act a as {extra egg is fresh, large omelet; extra egg is rotten, ruined omelet}, and we can represent the act of not cracking the extra egg as {extra egg is rotten or fresh, small omelet}. More generally, acts have the form $g = \{E_1, x_1;\ldots; E_n, x_n\},$ where $x_i \in\cX,$ $E_i \subseteq \cS$ is an *event* (a subset of the state space), and $x_i$ obtains when the true state of the world is in $E_i.$ Again, acts needn’t be restricted to a finite set of consequences. In the subjective probability version, the individual has a *probability function* $p$ that assigns to each $E_i$ a number between 0 and 1 (inclusive), which represents her subjective probabilities, also called “degrees of belief” or “credences”. The probability function is *additive* in the sense that if $E$ and $F$ are mutually exclusive, then $p(E v F) = p(E) + p(F).$ (For some of the discussion, it does not matter if we are talking about lotteries or acts, so I will use the variables *A*, *B*, *C*… to range over lotteries or acts.)

The core principle of expected utility theory concerns how the utility values of gambles are related to the utility values of consequences. In particular, the slogan of expected utility theory is that *rational agents maximize expected utility*. The expected utility (EU) of a lottery, relative to an individual’s utility function $\uf,$ is:

$$ \EU(L) = \sum_{i = 1}^{n} p_{i} \uf(x_{i}) $$

The expected utility of an act, relative to an individual’s utility function $\uf$ and probability function $p,$ is:

$$ \EU(g) = \sum_{i = 1}^{n} p(E_{i}) \uf(x)_{i} $$

Continuous versions of these are defined using an integral instead of a sum.

Expected utility theory holds that an individual’s preferences order gambles according to their expected utility, or ought to do so: $A \succcurlyeq B$ iff $\EU(A) \ge \EU(B).$ Generally, weak preference $(\succcurlyeq)$ is taken to be basic and strict preference $(\succ)$ and indifference $(\sim)$ defined in the usual way ($A \succ B$ iff $A \succcurlyeq B$ and not-$(B \succcurlyeq A)$; $A \sim B$ iff $A \succcurlyeq B$ and $B \succcurlyeq A$).

We can take utility and probability to be basic, and the norm to tell us what to prefer; alternatively, we can take preferences to be basic, and the utility and probability functions to be derived from them. Say that a utility (and probability) function *represents* a preference relation $\succcurlyeq$ *under EU- maximization* just in case:

- $u$ represents $\succcurlyeq$ under EU-maximization (objective probabilities): for all lotteries $L_1$ and $L_2,$ $$L_1 \succcurlyeq L_2 \text{ iff } \EU(L_1) \ge \EU(L_2),$$ where EU is calculated relative to $u.$
- $u$ and $p$ represent $\succcurlyeq$ under EU-maximization (subjective probabilities): for all acts $f$ and $g,$ $$f \succcurlyeq g \text{ iff } \EU(f) \ge \EU(g), $$ where EU is calculated relative to $u$ and $p.$

A *representation theorem* exhibits a set of axioms (call it [axioms]) such that the following relationship holds:

- Representation Theorem (objective probabilities): If a preference relation over lotteries satisfies [axioms], then there is a utility function $u,$ unique up to positive affine transformation, that represents the preference relation under EU-maximization.
- Representation Theorem (subjective probabilities): If a preference relation over lotteries satisfies [axioms], then there is a utility function $u,$ unique up to positive affine transformation, and a unique probability function $p$ that represent the preference relation under EU-maximization.

“Unique up to positive affine transformation” means that any utility function $u'$ that also represents the preference relation can be transformed into $u$ by multiplying by a constant and adding a constant (to borrow an example from a different domain: temperature scales are unique up to positive affine transformation, because although temperature can be represented by Celsius or Fahrenheit, Celsius can be transformed into Fahrenheit by multiplying by 9/5 and adding 32).

The first and most historically important axiomatization of the objective probabilities version of expected utility theory is that of von Neumann and Morgenstern (1944). The axioms are as follows (slightly different versions appear in the original):

- Completeness: For all lotteries $L_1$ and $L_2 : L_1 \succcurlyeq L_2$ or $L_2 \succcurlyeq L_1.$
- Transitivity: For all lotteries $L_1, L_2,$ and $L_3$: If $L_1 \succcurlyeq L_2$ and $L_2 \succcurlyeq L_3,$ then $L_1 \succcurlyeq L_3.$
- Continuity: For all lotteries $L_1, L_2,$ and $L_3$: If $L_1 \succcurlyeq L_2$ and $L_2 \succcurlyeq L_3,$ then there is some real number $p\in [0, 1]$ such that $L_2 \sim\{L_1, p$; $L_3, 1 - p\}$
- Independence: For all lotteries $L_1,$ $L_2,$ $L_3$ and all $0 \lt p \le 1$: $$ L_1 \succcurlyeq L_2 \Leftrightarrow \{L_1, p; L_3, 1 - p\} \succcurlyeq \{L_2, p; L_3, 1 - p\} $$

The most historically important axiomatization of the subjective probabilities version of expected utility theory is that of Savage (1954), though other prominent versions include Ramsey (1926), Jeffrey (1965), Armendt (1986, 1988), and Joyce (1999). These generally include axioms that are analogues of the von Neumann-Morgenstern axioms, plus some additional axioms that will not be our focus.

The first two of the axioms that will be our focus are (as above) *completeness* and *transitivity*:

- Completeness: For all acts $f$ and $g$: $f \succcurlyeq g$ or $f \succcurlyeq g.$
- Transitivity: For all acts $f,$ $g,$ and $h$: If $f \succcurlyeq g$ and $g \succcurlyeq h,$ then $f \succcurlyeq h.$

The third is some version of continuity, sometimes called an *Archimedean Axiom*.

The final axiom is a *separability* axiom. Savage’s version of this axiom is known as the sure-thing principle. Where $f_E h$ is an act that agrees with *f* on event *E* and agrees with *h* elsewhere:

- Sure-thing Principle: For all acts $f_E h,$ $g_E h,$ $f_E j,$ and $g_E j$: $$f_E h \succcurlyeq g_E h \Leftrightarrow f_E j \succcurlyeq g_E j$$

In other words, if two acts agree on what happens on not-*E*, then one’s preference between them should be determined only by what happens on E. Other separability axioms include Jeffrey’s Averaging (1965) and Köbberling and Wakker’s Tradeoff Consistency (2003).

Because representation theorems link, on the one hand, preferences that accord with the axioms and, on the other hand, a utility (and probability) function whose expectation the individual maximizes, a challenge to one of the three components of expected utility theory must also be a challenge to one (or more) of the axioms.

### 1.2 Components

#### 1.2.1 Utility

Since representation theorems show that a utility (and probability) function can be derived from preferences—that having a particular expectational utility function is mathematically equivalent to having a particular preference ordering—they open up a number of possibilities for understanding the utility function. There are two questions here: what the utility function corresponds to (the metaphysical question), and how we determine an individual’s utility function (the epistemic question).

The first question is whether the utility function corresponds to a real-world quantity, such as strength of desire or perceived desirability or perceived goodness, or whether it is merely a convenient way to represent preferences. The former view is known as *psychological realism* (Buchak 2013)[^buchak-2013] or *weak realism* (Zynda 2000)[^zynda-2000], and is held by Allais (1953) and Weirich (2008, 2020), for example. The latter view is known as *formalism* (Hansson 1988)[^hansson-1988], *operationalism* (Bérmudez 2009), or the *representational viewpoint* (Wakker 1994)[^wakker-1994], and is particularly associated with decision theorists from the mid-twentieth century (Luce & Raiffa 1957, Arrow 1951, Harsanyi 1977)[^arrow-1951][^harsanyi-1977][^luce-1957], and with contemporary economists.

The second question is what facts are relevant to determining someone’s utility function. Everyone in the debate accepts that preferences provide evidence for the utility function, but there is disagreement about whether there may be other sources of evidence as well. *Constructivists* hold that an individual’s utility function is defined by her preferences—utility is “constructed” from preference—so there are can be no other relevant facts (discussed in Dreier 1996, Buchak 2013)[^buchak-2013][^dreier-1996]; this view is also called *strong realism* (Zynda 2000)[^zynda-2000]. *Non-constructive realists*, by contrast, hold that there are other sources of evidence about the utility function: for example, an individual might have introspective access to her utility function. This latter view only makes sense if one is a psychological realist, though one can pair constructivism with either psychological realism or formalism.

A key fact to note about the utility function is that it is *real-valued*: each consequence can be assigned a real number. This means that no consequence is of *infinite value*, and all consequences are *comparable*. As we will see, each of these two properties invites a challenge.

#### 1.2.2 Probability

Given that a probability function can also be derived from preferences, a similar question arises about the nature and determination of the probability function. One could hold that the probability function represents some real-world quantity, such as partial belief; or one could hold that the probability function is merely a way of representing some feature of betting behavior. There is also disagreement about what facts are relevant to determining someone’s probability function: some hold that it is determined from betting behavior or from the deliverances of a representation theorem while others take it to be primitive (see Eriksson & Hájek 2007)[^eriksson-2007].

Probability is *real-valued* and *pointwise* (“sharp”, “precise”), meaning that there is a unique number representing an individual’s belief in or evidence for an event. Again, this property will invite a challenge.

#### 1.2.3 Expectation

We can see the *norm* of expected utility in one of two ways: maximize expected utility, or have preferences that obey the axioms. Because of this, normative arguments for expected utility can argue either for the functional form itself or for the normativity of the axioms. Examples of the former include the argument that expected utility maximizers do better in the long run, though these arguments fell out of favor somewhat as the popularity of the realist interpretations of utility waned. Examples of the latter include the idea that each axiom is itself an obvious constraint and the idea that the axioms follow from consequentialist (or means-ends rationality) principles. Of particular note is a proof that non-EU maximizers will either be inconsistent or non-consequentialist over time (Hammond 1988)[^hammond-1988]; how alternative theories have fared under dynamic choice has been a significant focus of arguments about their rationality.

The idea that EU maximization is the correct norm can be challenged on several different grounds, as we will see. Those who advocate for non-EU theories respond to the arguments listed above by either arguing that the new norm doesn’t actually fall prey to the argument (e.g., provide a representation theorem with supposedly more intuitive axioms) or that it is nonetheless okay if it does.

## 2. Infinite and Unbounded Utility

### 2.1 The Challenge from Infinite and Unbounded Utility

The first challenge to EU maximization stems from two ways that infinite utility can arise in decision situations.

First, some particular outcome might have *infinite utility* or infinite disutility. For example, *Pascal’s Wager* is motivated by the idea that eternal life with God has infinite value, so one should “wager for God” as long as one assigns some non-zero probability to God’s existence (Pascal 1670)[^pascal-1670]. If a particular outcome has infinite (dis)value, then the Continuity Axiom or the Archimedean Axiom will not hold. (See discussions in Hacking 1972 and Hájek 2003, and a related issue for utilitarianism in Vallentyne 1993, Vallentyne & Kagan 1997, and Bostrom 2011.)[^bostrom-2011][^hacking-1972][^hájek-2003][^vallentyne-1993][^vallentyne-1997]

Second, all outcomes might have finite utility value, but this value might be *unbounded*, which, in combination with allowing that there can be infinitely many *states*, gives rise to various paradoxes. The most famous of these is the *St. Petersburg Paradox*, first introduced by Nicolas Bernoulli in a 1713 letter (published in J. Bernoulli *DW*). Imagine a gamble whose outcome is determined by flipping a fair coin until it comes up heads. If it lands heads for the first time on the *n*ᵗʰ flip, the recipient gets $$2^n$; thus the gamble has infinite expected monetary value for the person who takes it (it has a $\lfrac{1}{2}$ probability of yielding $2, a $\lfrac{1}{4}$ probability of yielding $4, a $\lfrac{1}{8}$ probability of yielding $8, and so forth, and

$$\left(\frac{1}{2}\right)(2) + \left(\frac{1}{4}\right)(4) + \left(\frac{1}{8}\right)(8) + \ldots \rightarrow \infty.$$

While this version can be resolved by allowing utility to diminish marginally in money—so that the gamble has finite expected utility—if the payoffs are in utility rather than money, then the gamble will have infinite expected utility.

Related paradoxes and problems abound. One centers around a pair of games, the *Pasadena game* and the *Altadena game* (Nover & Hájek 2004)[^nover-2004]. The Pasadena game is also played by flipping a fair coin until it lands heads; here, the player receives $\$({-1})^{n-1}(2^n/n)$ if the first heads occurs on the *n*ᵗʰ flip. Thus, its payoffs alternate between positive and negative values of increasing size, so that its terms can be rearranged to yield any sum whatsoever, and its expectation does not exist. The Altadena game is identical to the Pasadena game, except that every payoff is raised by a dollar. Again, its terms can be rearranged to yield any value, and again its expectation does not exist. However, it seems (contra EU maximization) that the Altadena game should be preferred to the Pasadena game, since the former *state-wise dominates* the latter—it is better in every possible state of the world (see also Colyvan 2006, Fine 2008, Hájek & Nover 2008)[^colyvan-2006][^colyvan-2008][^fine-2008][^hájek-2008]. Similarly, it seems that the *Petrograd game*, which increases each payoff of the St. Petersburg game by $1, should be preferred to the St. Petersburg game, even though EU maximization will say they have the same (infinite) expectation (Colyvan 2008)[^colyvan-2008].

(See also Broome’s (1995) discussion of the two-envelope paradox; Arntzenius, Elga, and Hawthorne’s (2004) discussion of diachronic puzzles involving infinite utility; and McGee’s (1999) argument that the utility function ought to be bounded, which will dissolve the above paradoxes.)

### 2.2 Proposals

Several proposals retain the basic EU norm, but reject the idea that the utility function ranges only over the real numbers. Some hold that the utility function can take *hyper-real* values (Skala 1975, Sobel 1996)[^skala-1975][^sobel-1996]. Others hold that the utility function can take *surreal* values (Hájek 2003, Chen & Rubio 2020)[^chen-2020][^hájek-2003]. These proposals allow for versions of the Continuity/Archimedean Axiom. Another alternative is to use a vector-valued (i.e., *lexicographic*) utility function, which rejects these axioms (see discussion in Hájek 2003)[^hájek-2003].

A different kind of response is to subsume EU maximization under a more general norm that also applies when utility is infinite. Bartha (2007, 2016) defines *relative utility*, which is a three-place relation that compares two outcomes or lotteries relative to a third “base point” that is worse than both. The relative utility of $A$ to $B$ with base-point $Z$ (written $(A, B; Z)$) will be:

- If $A,$ $B$ and $Z$ are finitely valued gambles: $$\frac{u(A) - u(Z)}{u(B) - u(Z)},$$ as in standard EU maximization
- If $A$ is infinitely valued and $B$ and $Z$ are not: $\infty$

Relative utility ranges over the extended real numbers $\{\cR \cup \infty\}.$ “Finite” and “infinite” values can be determined from preferences. Furthermore, relative utility is expectational

$$U(\{A, p; A', 1-p\}, B; Z) = pU(A, B; Z) + (1-p)U(A', B; Z)$$

and has a representation theorem consisting of the standard EU axioms minus Continuity. (See Bartha 2007 for application to infinite-utility consequences and Bartha 2016 for application to unbounded-utility consequences.)[^bartha-2007][^bartha-2016]

When considering only the paradoxes of unbounded utility (not those of infinite utility), there are other ways to subsume EU maximization under a more general norm. Colyvan (2008) defines *relative expected utility* (unrelated to Bartha’s relative utility) of act $f = \{E_1, x_1;\ldots; E_n, x_n\}$ over $g = \{E_1, y_1;\ldots; E_n, y_n\}$ as:

$$\REU(f,g) = \sum_{i = 1}^{n} p(E_{i}) \left(u(x_{i}) - u(y_{i})\right)$$

In other words, one takes the difference in utility between $f$ and $g$ in each state, and weights this value by the probability of each state. Colyvan similarly defines the infinite state-space case as

$$\REU(f,g) = \sum_{i = 1}^{\infty} p(E_{i}) \left(u(x_{i}) - u(y_{i})\right).$$

The new norm is that $f \succcurlyeq g$ iff $\REU(f, g) \ge 0.$ This rule agrees with EU maximization in cases of finite state spaces, but also agrees with state-wise dominance; so it can require that the Altadena game is preferred to the Pasadena game and the Petrograd game is preferred to the St. Petersburg game. (See also Colyvan & Hájek 2016.)[^colyvan-2016]

A more modest extension of standard EU maximization is suggested by Easwaran (2008). He points out that although the Pasadena and Altadena games lack a “strong” expectation, they do have a “weak” expectation. (The difference corresponds to the difference between the strong and weak law of large numbers.). Thus, we can hold that a decision-maker is required to value a gamble at its weak expectation, which is equivalent to its strong expectation if the latter exists. (See also Gwiazda 2014, Easwaran 2014b; relatedly, Fine (2008) shows that these two games and the St. Petersberg paradox can be assigned finite values that are consistent with EU theory.).

Lauwers and Vallentyne (2016) combine an extension of Easwaran’s proposal to *infinite* weak expectations with an extension of Colyvan’s proposal to *cardinal* relative expectation that can be *interval-valued*. Meacham (2019) extends Colyvan’s proposal to cover cases in which the acts to be compared have utilities that are to be compared in different states, and cases in which probabilities are act-dependent; his *difference minimizing theory* re-orders each gamble from worst consequence to best consequence, before taking their relative expectation. A key difference between these two extensions is that difference minimizing theory adheres to *stochastic dominance* and a related principle called *stochastic equivalence*. (See also discussion in Seidenfeld, Schervish, & Kadane 2009; Hájek 2014; Colyvan & Hájek 2016.)[^colyvan-2016][^hájek-2014][^seidenfeld-2009]

In a more radical departure from standard EU maximization, Easwaran (2014a) develops an axiomatic decision theory *based* on state-wise dominance, that starts with utility and probability and derives a normative preference relation. In cases that fit the standard parameters of EU maximization, this theory can be made to agree with EU maximization; but it also allows us to compare some acts with infinite value, and some acts that don’t fit the standard parameters (e.g., incommensurable acts, acts with probabilities that are comparative but non-numerical).

Finally, one could *truncate* the norm of EU maximization. Some have argued that that for a gamble involving very small probabilities, we should discount those probabilities down to zero, regardless of the utilities involved. When combined with a way of aggregating the remaining possibilities, this strategy will yield a finite value for the unbounded-utility paradoxes, and also allow people who attribute a very small probability to God’s existence to avoid wagering for God. (This idea traces back to Nicolaus Bernoulli, Daniel Bernoulli, d’Alambert, Buffon, and Borel [see Monton 2019 for a historical survey]; contemporary proponents of this view include Jordan 1994, Smith 2014, Monton 2019.)[^jordan-1994][^monton-2019][^smith-2014]

## 3. Incommensurability

### 3.1 The Challenge from Incommensurability

Another challenge to expected utility maximization is to the idea that preferences are totally ordered—to the idea that consequences can be ranked according to a single, consistent utility function. In economics, this idea goes back at least to Aumann (1962); in philosophy, it has been taken up more recently by ethicists. Economists tend to frame the challenge as a challenge to the idea that the *preference* relation is complete, and ethicists to the idea that the *betterness* relation is complete. I use $\succcurlyeq$ to represent whichever relation is at issue, recognizing that some proposals may be more compelling in one case than the other.

The key claim is that there are some pairs of options for which it is false that one is preferred to (or better than) the other, but it is also false that they are equi-preferred (or equally good). Proposed examples include both the mundane and the serious: a Mexican restaurant and a Chinese restaurant; a career in the military and a career as a priest; and, in an example due to Sartre (1946), whether to stay with one’s ailing mother or join the Free French. Taking up the second of these examples: it is not the case that a career in the military is preferred to (or better than) a career as a priest, nor *vice versa*; but it is also not the case that they are equi-preferred (or equally good). Call the relation that holds between options in these pairs *incommensurability*.

Incommensurability is most directly a challenge to Completeness, since on the most natural interpretation of $\succcurlyeq,$ the fact that $A$ and $B$ are incommensurable means that neither $A \succcurlyeq B$ nor $B \succcurlyeq A.$ But incommensurability can instead be framed as a challenge to Transitivity, if we assume that incommensurability is indifference, or define $A \succcurlyeq B$ as the negation of $B \succ A$ (thus assuming Completeness by definition). To see this, notice that if two options $A$ and $B$ are incommensurable, then “sweetening” $A$ to a slightly better $A^+$ will still leave $A^+$ and $B$ incommensurable. For example, if $A$ is a career in the military and $A^+$ is this career but with a slightly higher salary, the latter is still incommensurable with a career as a priest. This pattern suffices to show that the relation $\sim$ is intransitive, since $A \sim B$ and $B \sim {A^+},$ but ${A^+} \succ A$ (de Sousa 1974).

There are four options for understanding incommensurability. *Epistemicists* hold that there is always some fact of the matter about which of the three relations $(\succ,$ $\prec,$ $\sim)$ holds, but that it is sometimes difficult or impossible to determine which one—thus incommensurability is merely apparent. They can model the decision problem in the standard way, but as a problem of uncertainty about values: one does not know whether one is in a state in which $A \succcurlyeq B,$ but one assigns some probability to that state, and maximizes expected utility taking these kinds of uncertainties into account. *Indeterminists* hold that it is indeterminate which relation holds, because these relations are vague; thus incommensurability is a type of vagueness (Griffin 1986, Broome 1997, Sugden 2009, Constantinescu 2012)[^broome-1997][^constantinescu-2012][^griffin-1986][^sugden-2009]. *Incomparabilists* hold that in cases of incommensurability, $A$ and $B$ simply cannot be compared (de Sousa 1974, Raz 1988, Sinnott-Armstrong 1988)[^raz-1988][^sinnott-armstrong-1988]. Finally, those who hold that incommensurability is *parity* hold that there is a fourth relation than can obtain between $A$ and $B$: $A$ and $B$ are “on a par” if $A$ and $B$ can be compared but it is not the case that one of the three relations holds (Chang 2002a, 2002b, 2012, 2015, 2016)[^chang-2002a][^chang-2002b][^chang-2012][^chang-2015][^chang-2016]. (Taxonomy from Chang 2002b; see also Chang 1997.)[^chang-1997][^chang-2002b]

### 3.2 Proposals: Definitions

Aumann (1962) shows that if we have a partial but not total preference ordering, then we can represent it by a utility function (not unique-up-to-positive-affine-transformation) such that $A \succ B$ implies $\EU(A) \gt \EU(B),$ but not *vice versa*. Aumann shows that there will be at least one utility function that represents the preference ordering according to (objective) EU maximization. Thus, we can represent a preference ordering as the *set of all utility functions* that “one-way” represent the decision-maker’s preferences. Letting $\EU_u(A)$ be the expected utility of $A$ given utility function $u$:

$$\begin{align} \cU = \big\{u \mid {}&(A \succ B \Rightarrow \EU_u (A) \succ \EU_u (B)) \\ &{}\amp (A \sim B \Rightarrow \EU_u (A) = \EU_u (B))\big\}. \end{align}$$

If there is no incommensurability, then there will be a single (expectational) utility function in $\cU,$ as in standard EU theory. But when neither $A \succ B$ nor $B \succ A$ nor $A \sim B,$ there will be some $u \in\cU$ such that $\EU_u (A) \gt \EU_u (B),$ and some $u'\in\cU$ such that $\EU_{u'}(B) \gt \EU_{u'}(A)$; and *vice versa*.

Chang (2002a,b) proposes a similar strategy, but she takes value facts to be basic, and defines the betterness relation—plus a new “parity” relation we will denote “$\parallel$”—from them, instead of the reverse. In addition, she defines these relations in terms of the *evaluative differences* between $A$ and $B,$ i.e., $(A - B)$ is the set of all licensed differences in value between $A$ and $B.$ If $(A - B) = \varnothing,$ then $A$ and $B$ are *incomparable*; however, if $(A - B) \ne \varnothing,$ the relevant relations are:

- $A \succ B$ iff $(A - B)$ contains only positive numbers
- $B \succ A$ iff $(A - B)$ contains only negative numbers
- $A \sim B$ iff $(A - B)$ contains only 0
- $A \parallel B$ otherwise

$(A - B)$ might be generated by a set of utility functions, each of which represents a possible substantive completion of the underlying value that utility represents (discussed in Chang 2002b)[^chang-2002b]; alternatively, it might be that there is parity “all the way down” (discussed in Chang 2016, where she also replaces the definition in terms of explicit numerical differences with one in terms of bias)[^chang-2016].

Rabinowicz (2008) provides a model that allows for both parity and grades of incomparability. On his proposal, the betterness relation is represented by a class $K$ of “permissible preference orderings”, each of which may be complete or incomplete. He defines:

$$ \begin{align} x \succ y & \text{ iff } (\forall R\in K)(x \succ_R y)\\ x \sim y & \text{ iff } (\forall R\in K)(x \sim _R y)\\ x \parallel y & \text{ iff } (\exists R\in K)(x \succ_R y) \amp (\exists R \in K)(x \succ_R x)\\ \end{align} $$

(He defines $\succcurlyeq$ as the union of several “atomic” possibilities for $K.$) Letting $x\relT y$ hold iff $x \succ y$ or $y \succ x$ or $x \sim y,$ he then defines:

- $x$ and $y$ are fully comparable iff $(\forall R \in K)(xT_R y)$
- $x$ and $y$ are fully on a par iff they are fully comparable and $x\parallel y$
- $x$ and $y$ are incomparable iff $(\forall R\in K)(\text{not-}(xT _Ry))$
- $x$ and $y$ are weakly incomparable iff $(\exists R\in K)(\text{not-}(xT_Ry)$

Class $K$ won’t necessarily give rise to a utility function.

### 3.3 Proposals: Decision Rules

If the decision-maker’s preferences are represented by a set of utility functions $\cU,$ then a number of possible decision rules suggest themselves. All the proposed rules focus on selection of *permissible* options from a set of alternatives $\cS,$ rather than an aggregation function or a complete ranking of options (we can always recover the former from the latter, but not *vice versa*). To understand the first three of these rules, we can imaginatively think of each possible utility function as a “committee member”, and posit a rule for choice based on facts about the opinions of the committee.

First, we might choose any option which *some* committee member endorses; that is, we might choose any option which maximizes expected utility relative to *some* utility function:

$$ \text{Permissible choice set } = \{ A \mid (\exists u \in \cU) (\forall B \in \cS)(\EU_u (A) \ge \EU_u (B))\}$$

Levi (1974) terms this rule *E-admissibility*, and Hare (2010) calls it *prospectism*. (See section 4.3.3 for Levi’s full proposal, and for extensions of this rule to the case in which the decision-maker does not have a single probability function.)

Aumann suggests that we can choose any *maximal* option: any option that isn’t worse, according to all committee members, than some other particular option; that is, an option to which no other option is (strictly) preferred (assigned a higher utility by all utility functions):

$$ \text{Permissible choice set } = \{A \mid (\forall B \in \cS ) (\exists u \in \cU)(\EU_u (A) \ge \EU_u (B)) \}$$

This is a more permissive rule than E-admissibility: every E-admissible option will be maximal, but not *vice versa*. To see the difference between the two rules, notice that if the decision-maker has two possible rankings, $A \gt B \gt C$ and $C \gt B \gt A,$ then all three options will be maximal but only $A$ and $C$ will be E-admissible (no particular option is definitively preferred to $B,$ so $B$ is maximal; but it is definitive that something is preferred to $B,$ so $B$ is not E-admissible).

A final possibility is that we can choose any option that is not *interval dominated* by another act (Schick 1979, Gert 2004)[^gert-2004][^schick-1979], where an interval dominated option has a lower “best” value than some other option’s “worst” value:

$$ \text{Permissible choice set } = \{ A \mid (\forall B \in \cS )(\text{max}_u \EU_u (A) \ge \text{min}_u \EU_u (B))\} $$

This is a more permissive rule than both E-admissibility and maximality.

A different type of rule first looks at the options’ possible utility values in each state, before aggregating over states; this is what Hare’s (2010) *deferentialism* requires. To find out if an option O is permissible under deferentialism, we consider how it fares if we, in each state, make the assumptions most favorable to it. First, “regiment” the utility functions in $\cU$ so that there’s some pair of consequences $\{x, y\}$ such that $(\forall u \in\cU)(u(x) = 1 \amp u(y) = 0)$; this allows only one representative utility function for each possible completion of the decision-maker’s preference. Next, take all the possible “state-segments”—the possible utility assignments in each state—and cross them together in every possible arrangement to get an “expanded” set of utility functions (for example, this will contain every possible utility function in $E$ coupled with every possible utility function not-$E$). Then $A$ is permissible iff $A$ maximizes expected utility relative to *some* utility function in this expanded set.

## 4. Imprecise Probabilities or Ambiguity

### 4.1 The Challenge from Imprecise Probabilities or Ambiguity

A third challenge to expected utility maximization holds that subjective probabilities need not be “sharp” or “precise”, i.e., need not be a single, point-wise function. (In economics, this phenomenon is typically called *ambiguity*.) There are three historically significant motivations for imprecise probabilities.

The first is that decision makers treat subjective (or unknown) probabilities differently from objective probabilities in their decision-making behavior. The classic example of this is the Ellsberg Paradox (Ellsberg 1961, 2001)[^ellsberg-1961][^ellsberg-2001]. Imagine you face an urn filled with 90 balls that are red, black, and yellow, from which a single ball will be drawn. You know that 30 of the balls are red, but you know nothing about the proportion of black and yellow balls. Do you prefer $f_1$ or $f_2$; and do you prefer $f_3$ or $f_4$?

- $f_1$: $100 if the ball is red; $0 if the ball is black or yellow.
- $f_2$: $100 if the ball is black; $0 if the ball is red or yellow.
- $f_3$: $100 if the ball is red or yellow; $0 if the ball is black.
- $f_4$: $100 if the ball is black or yellow; $0 if the ball is red.

Most people appear to (strictly) prefer $f_1$ to $f_2$ and (strictly) prefer $f_4$ to $f_3.$ They would rather bet on the known or objective probability than the unknown or subjective one—in the first pair, red has an objective probability of $\lfrac{1}{3}$, whereas black has a possible objective probability ranging from 0 to $\lfrac{2}{3}$; in the second pair, black or yellow has an objective probability of $\lfrac{2}{3}$ whereas red or yellow has a possible objective probability ranging from $\lfrac{1}{3}$ to 1. These preferences violate the Sure-thing Principle. (To see this, notice that the only difference between the two pairs of acts is that the first pair yields $0 on yellow and the second pair yields $100 on yellow.)

The second motivation for imprecise probability is that even if all the relevant probabilities are subjective, a decision-maker’s betting behavior might depend on how reliable or well-supported by evidence those probabilities are. Consider a decision-maker who may bet on three different tennis matches: in the first, she knows a lot about the players and knows they are very evenly matched; in the second, she knows nothing whatsoever about either player; and in the third, she knows that one of the two players is much better than the other, but she does not know which one. In each of the matches, the decision-maker should presumably assign equal probability to each player winning, since her information in favor of each is symmetrical; nonetheless, it seems rational to bet only on the first match and not on the other two (Gärdenfors & Sahlin 1982; see also Ellsberg 1961)[^ellsberg-1961][^gärdenfors-1982].

A final motivation for imprecise probability is that evidence doesn’t always determine precise probabilities (Levi 1974, 1983; Walley 1991; Joyce 2005; Sturgeon 2008; White 2009; Elga 2010)[^elga-2010][^joyce-2005][^levi-1974][^levi-1983][^sturgeon-2008][^walley-1991][^white-2009]. Assume a stranger approaches you and pulls three items out of a bag: a regular-sized tube of toothpaste, a live jellyfish, and a travel-sized tube of toothpaste; you are asked to assign probability to the proposition that the next item he pulls out will be another tube of toothpaste—but it seems that you lack enough evidence to do so (Elga 2010)[^elga-2010].

### 4.2 Proposals: Probability Representations

To accommodate imprecise probabilities in decision-making, we need both an alternative way to represent probabilities and an alternative decision rule that operates on the newly-represented probabilities. There are two primary ways to represent imprecise probabilities.

The first is to assign an *interval*, instead of a single number, to each proposition. For example, in the Ellsberg case:

$$ \begin{align} p(\RED) & = [\lfrac{1}{3}], \\ p(\YELLOW) & = [0, \lfrac{2}{3}]; \\ p(\BLACK) & = [0, \lfrac{2}{3}].\\ \end{align} $$

The second is to represent the individual’s beliefs as a *set* of probability functions. For example, in the Ellsberg case:

$$ \cQ = \{p\in\cP \mid p(\RED) = \lfrac{1}{3}\} $$

This means, for example, that the probability distribution $p(\rR, \rB, \rY) = \langle \lfrac{1}{3}, 0, \lfrac{2}{3}\rangle$ and the probability distribution $\langle \lfrac{1}{3}, \lfrac{1}{3}, \lfrac{1}{3}\rangle$ are both compatible with the available evidence or possible “completion” of the individual’s beliefs.

Each set-probability representation gives rise to an interval representation (assuming the set of probability functions is convex); but the set-probability representation provides more structure to the relationships between propositions. (A different proposal retains a precise probability function but refines the objects over which utility and probability range (Bradley 2015; Stefánsson & Bradley 2015, 2019)[^bradley-2015][^stefánsson-2015][^stefánsson-2019]; see discussion in section 5.2.)

### 4.3 Proposals: Decision Rules

We will examine rules for decision-making with imprecise probabilities in terms of how they evaluate the Ellsberg choices; for ease of exposition we will assume $u(\$0) = 0$ and $u(\$100) = 1.$ All proposals here are equivalent to EU maximization when there is a single probability distribution in the set, so all will assign utility $\lfrac{1}{3}$ to $f_1$ and $\lfrac{2}{3}$ to $f_4$ in the Ellsberg gamble; they differ in how they value the other acts.

#### 4.3.1 Aggregative Decision Rules using Sets of Probabilities

The first type of decision rule associates to each act a single value, and yields a complete ranking of acts; call these *aggregative rules*. The rules in this section use sets of probabilities.

Before we discuss these rules, it will be helpful to keep in mind three aggregative rules that operate under complete ignorance, i.e., when we have no information whatsoever about the state of the world. The first is maximin, which says to pick the option with the highest minimum utility. The second is maximax, which says to pick the option with the highest maximum utility. The third, known as the Hurwicz criterion, says to take a weighted average, for each option, of the minimum and maximum utility, where the weight $\alpha \in [0, 1]$ represents a decision-maker’s level of optimism/pessimism (Hurwicz 1951a)[^hurwicz-1951a]:

$$ H(f) = (1 - \alpha)(\text{min}_u(f)) + \alpha(\text{max}_u(f))$$

Using the set-probability representation, we can associate to each probability distribution an expected utility value, to yield a set of expected utility values. Let $\EU_p(f)$ be the expected utility of $f$ given probability distribution $p.$

One proposal is that the value of an act is its minimum expected utility value; thus, a decision-maker should *maximize her minimum expected utility* (Wald 1950; Hurwicz 1951b; Good 1952; Gilboa & Schmeidler 1989)[^gilboa-1989][^good-1952][^hurwicz-1951b][^schmeidler-1989][^wald-1950]:

$$\text{Γ-maximin}(f) = \text{min}_p (\EU_p(f))$$

This rule is also sometimes known as MMEU. For the Ellsberg choices, the minimum expected utilities are, for $f_1$, $f_2$, $f_3$, and $f_4$, respectively: $\lfrac{1}{3},$ $0,$ $\lfrac{1}{3},$ and $\lfrac{2}{3},$. These values rationalize the common preference for $f_1 \gt f_2$ and $f_4 \gt f_3.$ Conversely, an individual who *maximizes her maximum expected utility*—who uses Γ-maximax—would have the reverse preferences.

Γ-maximin appears too pessimistic. We might instead use an EU-analogue of Hurwicz criterion: take a *weighted average of the minimum expected utility and the maximum expected utility*, with weight $\alpha \in[0, 1]$ corresponding to a decision-maker’s level of pessimism (Hurwicz 1951b; Shackle 1952; Luce & Raiffa 1957; Ellsberg 2001; Ghirardato et al. 2003)[^ellsberg-2001][^ghirardato-2003][^hurwicz-1951b][^luce-1957][^shackle-1952]:

$$\alpha\text{-maximin}(f) = (1 - \alpha)(\text{min}_p (\EU_p (f))) + \alpha(\text{max}_p (\EU_p(f)))$$

In the Ellsberg choice, this model will assign $\alpha(\lfrac{2}{3})$ to $f_2$ and $(1 - \alpha)(\lfrac{1}{3}) + \alpha(1)$ to $f_3,$ making these acts disprefered to $f_1$ and $f_4,$ respectively, if $\alpha \lt \lfrac{1}{2}$; preferred to $f_1$ and $f_4$ if $\alpha \gt \lfrac{1}{2}$; and indifferent to $f_1$ and $f_4$ if $\alpha = \lfrac{1}{2}.$

Instead, we can assume the decision-maker considers two quantities when evaluating an act: the EU of the act, according to her “best estimate” at the probabilities ($\text{est}_p),$ and the minimum EU of the act as the probability ranges over $\cQ$; she also assigns a degree of confidence $\varrho \in[0, 1]$ to her estimated probability distribution. The value of an act will then be a weighted average of her best estimate EU and the minimum EU, with her best estimate weighed by her degree of confidence (Hodges & Lehmann 1952; Ellsberg 1961)[^ellsberg-1961][^hodges-1952]:

$$E(f) = \varrho(\text{est}_p (\EU_p(f))) + (1 - \varrho)(\text{min}_p (\EU_p(f)))$$

In the Ellsberg pairs, assuming the “best estimate” is that yellow and black each have probability $\lfrac{1}{3}$, this will assign $\varrho(\lfrac{1}{3})$ to $f_2$ and $\varrho(\lfrac{2}{3}) + (1 - \varrho)(\lfrac{1}{3})$ to $f_3,$ making these acts disprefered to $f_1$ and $f_4,$ respectively, as long as $\varrho \lt 1.$

We can also combine these two proposals (Ellsberg 2001)[^ellsberg-2001]:

$$ E(f) = \varrho(\text{est}_p \EU_p(f)) + (1 - \varrho) [(1 - \alpha)(\text{min}_p \EU_p(f)) + \alpha(\text{max}_p \EU_p(f))]$$

This model will rationalize the common preferences for many choices of $\varrho$ and $\alpha$ (setting $\varrho = 0$ or $\alpha = 0$ yields previously-mentioned models).

We might add additional structure to the representation: to each probability function, the decision-maker assigns a degree of “reliability”, which tracks how much relevant information the decision-maker has about the states of nature (Good 1952; Gärdenfors & Sahlin 1982)[^gärdenfors-1982][^good-1952]. A decision-maker selects a desired threshold level of epistemic reliability. She then considers all probability functions above this threshold, and maximizes the minimum expected utility (Γ-maximin) with respect to these probability functions. (In principle, a different decision rule could be used in this step.) For the decision-maker deciding whether to bet on tennis matches, the above-threshold probability functions for the first match may include only $p(P1 \text{WINS}) \approx 0.5,$ but for the second and third match may also include $p(P1 \text{WINS}) \approx 0$; thus betting on P1 in the first match will have a higher value than betting on P1 in the other matches.

#### 4.3.2 Aggregative Decision Rules: Choquet Expected Utility

A different kind of rule is *Choquet expected utility*, also known as *cumulative* utility (Schmeidler 1989; Gilboa 1987)[^gilboa-1987][^schmeidler-1989]. This rule starts with a function $v$ which, like a probability function, obeys $v(E)\in[0, 1],$ $v(0) = 0,$ $v(1) = 1,$ and $A \subseteq B$ implies $v(A) \le v(A).$ Unlike a probability function, however, $v$ is non-additive; and $v$ is not straightforwardly used to calculate an expectation. (Many economists refer to this function as a “non-additive subjective probability function”.). Choquet expected utility is a member of the *rank-dependent* family (Quiggin 1982, Yaari 1987, Kahneman & Tversky 1979, Tversky & Kahneman 1992, Wakker 2010)[^kahneman-1979][^quiggin-1982][^tversky-1992][^wakker-2010][^yaari-1987]. Functions in this family let the weight of an event in an act’s overall value depend on both the probability-like element and the event’s position in the ordering of an act, e.g., whether it is the worst or best event for that act. Formally, let $g' = \{E_1, x_1;\ldots; E_n, x_n\}$ be a re-ordering of act $g$ from worst event to best event, so that $u(x_1) \le \ldots \le u(x_n).$ The *Choquet expected utility* of $g'$ (and therefore of $g$) is:

$$ \CEU(g') = u(x_{1}) + \sum_{i = 2}^{n} v\left(\bigcup_{j = i}^{n} E_{j}\right) \left(u(x_{i}) - u(x_{i - 1})\right)$$

If $v$ is additive, then $v$ is an (additive) probability function and CEU reduces to EU. If $v$ is convex $(v(E) + v(F) \le v(EF) + v(E v F)),$ then the individual is *uncertainty-averse*.

In the Ellsberg example, we are given $p(\RED) = \lfrac{1}{3}$ and $p(\BLACK \lor \YELLOW) = \lfrac{2}{3},$ and so we can assume $v(\RED) = \lfrac{1}{3}$ and $v(\BLACK \lor \YELLOW) = \lfrac{2}{3}.$ A person who is “ambiguity averse” will assign $v(\BLACK) + v(\YELLOW) \le v(\BLACK \lor \YELLOW)$; let us assume $v(\BLACK) = v(\YELLOW) = \lfrac{1}{9}.$ Similarly, she will assign $v(\RED \lor \YELLOW) + v(\BLACK) \le 1$; let us assume $v(\RED \lor \YELLOW) = \lfrac{4}{9}.$

Then the values of the acts will be:

$$ \begin{align} \CEU(f_1) & = 0 + v(\RED)(1 - 0) & = \lfrac{1}{3}\\ \CEU(f_2) & = 0 + v(\BLACK)(1 - 0) & = \lfrac{1}{9}\\ \CEU(f_3) & = 0 + v(\RED \lor \YELLOW)(1 - 0) &= \lfrac{4}{9}\\ \CEU(f_4) & = 0 + v(\BLACK \lor \YELLOW)(1 - 0) &= \lfrac{2}{3}\\ \end{align} $$

This assignment recovers the Ellsberg preferences.

Axiomatizations of CEU use a restricted version of the separability condition (the “Comonotonic” Sure-thing Principle or “Comonotonic” Tradeoff Consistency): namely, the condition only holds when all of the acts in its domain are *comonotonic*, i.e., when the worst-to-best ranking of the events coincides for all the acts (Gilboa 1987, Schmeidler 1989, Wakker 1989, Chew & Wakker 1996, Köbberling & Wakker 2003; see also Wakker 2010, who also notes the relationship between CEU and $\alpha$-maximin.)[^chew-1996][^gilboa-1987][^gilboa-1989][^köbberling-2003][^schmeidler-1989][^wakker-1989][^wakker-2010]

#### 4.3.3 Decision Rules that Select from a Menu

Another different type of proposal focuses on selection of *permissible* options from a set of alternatives $\cS,$ rather than a complete ranking of options. As in section 3.3, we can imaginatively think of each possible probability distribution in a set $\cQ$ as a “committee member”, and posit a rule for choice based on facts about the opinions of the committee. (The first three rules are versions of the rules for sets of utility functions in 3.3, and can be combined to cover sets of probability/utility pairs.)

The first possibility is that a decision-maker is permitted to pick an act just in case *some* committee member is permitted to pick it over all the alternatives: just in case it maximizes expected utility relative to *some* probability function in the set. This is known as *E-admissibility* (Levi 1974, 1983, 1986; Seidenfeld, Schervish, & Kadane 2010)[^levi-1974][^levi-1983][^levi-1986][^seidenfeld-2010]:

$$ \text{Permissible choice set } = \{A \mid (\exists p\in\cQ )(\forall B \in \cS)(\EU_p(A) \ge \EU_p(B))\}$$

Levi in fact tells a more complicated story about what a decision-maker is permitted to choose, in terms of a procedure that rules out successively more and more options. First, the procedure selects from all the options just the ones that are E-admissible. Next, the procedure selects from the E-admissible options just the ones that are *P-admissible*: options that “do best” at preserving the E-admissible options (the idea being that a rational agent should keep her options open). Finally, the procedure selects from the P-admissible options just the ones that are *S-admissible*: options that maximize the minimum utility. (Note that this last step involves maximin, not Γ-maximin.)

A more permissive rule than E-admissibility permits a choice as long there is *no* particular alternative that the committee members *unanimously* (strictly) prefer. As in the case of utility-sets, this rule is known as *maximality* (Walley 1991)[^walley-1991]:

$$ \text{Permissible choice set } = \{A \mid (\forall B\in\cS)(\exists p \in\cQ )(\EU_p(A) \ge \EU_p (B))\}$$

(See section 3.3 for an example of the difference between E-admissibility and maximality.)

More permissive still is the rule that a choice is permissible as long as it is not *interval dominated* (Schick 1979, Kyburg 1983)[^kyburg-1983][^schick-1979]: its maximum value isn’t lower than the minimum value of some other act.

$$\text{Permissible choice set } = \{A \mid (\forall B\in \cS)(\text{max}_p \EU_p(A) \ge \text{min}_p \EU_p(B))\}$$

For a proof showing that Γ-maximax implies E-admissibility; Γ-maximin implies maximality; E-admissibility implies maximality; and maximality implies interval dominance, see Troffaes (2007).

A final approach is to interpret ambiguity as indeterminacy: one committee member has the “true” probability function, but it is indeterminate which one. If all probability functions agree that an option is permissible to choose, then it is determinately permissible to choose; if all agree that it is impermissible to choose, it is determinately impermissible to choose; and if some hold that it is permissible and others hold that it is impermissible, it is indeterminate whether it is permissible (Rinard 2015)[^rinard-2015].

These rules in this section allow but do not obviously *explain* the Ellsberg choices unless supplemented by an additional rule (e.g., Levi’s more complicated story or one of the rules from section 4.3.1), since any choice between $f_1$ and $f_2$ and between $f_3$ and $f_4$ appears to be E-admissible, maximal, and non-interval-dominated.

### 4.4 Normative Questions

For those who favor non-sharp probabilities, two sets of normative questions arise. The first set is epistemic: whether it is epistemically rational not to have sharp probabilities (White 2009; Elga 2010; Joyce 2011; Hájek & Smithson 2012; Seidenfeld et al. 2012; Mayo-Wilson & Wheeler 2016; Schoenfield 2017; Vallinder 2018; Builes et al 2022; Konek ms. – see Other Internet Resources)[^builes-2022][^elga-2010][^hájek-2012][^joyce-2011][^mayo-wilson-2016][^schoenfield-2017][^seidenfeld-2012][^white-2009][^vallinder-2018].

The second set of questions question is practical. Some hold that ambiguity aversion is not well-motivated by practical reasons and so we have no reason to account for it (Schoenfield 2020)[^schoenfield-2020]. Others hold that some particular decision rule associated with non-sharp probabilities leads to bad consequences, e.g., in virtue of running afoul of the principles mentioned in section 1.2.3. Of particular interest is how these decision rules can be extended to sequential choice (Seidenfeld 1988a,b; Seidenfeld et al. 1990; Elga 2010; Bradley and Steele 2014; Chandler 2014; Moss 2015; Sud 2014; Rinard 2015)[^bradley-2014][^chandler-2014][^elga-2010][^moss-2015][^rinard-2015][^seidenfeld-1988a][^seidenfeld-1990][^sud-2014].

## 5. Risk Aversion

### 5.1 The Challenge from Risk Aversion

A final challenge to expected utility maximization is to the norm itself—to the idea that a gamble should be valued at its *expectation*. In particular, some claim that it is rationally permissible for individuals to be risk-averse (or risk-seeking) in a sense that conflicts with EU maximization.

Say that an individual is *risk-averse* in money (or any numerical good) if she prefers the consequences of a gamble to be less “spread out”; this concept is made precise by Rothschild and Stiglitz’s idea of *dispreferring mean-preserving spreads* (1972). As a special case of this, a person who is risk-averse in money will prefer $\$x$ to any gamble whose mean monetary value is $\$x.$ If an EU maximizer is risk-averse in money, then her utility function will be concave (it diminishes marginally, i.e., each additional dollar adds less utility than the previous dollar); if an EU maximizer is risk-seeking in money, then her utility function will be convex (Rothschild & Stiglitz 1972)[^rothschild-1972]. Therefore, EU theory equates risk-aversion with having a diminishing marginal utility function.

However, there are intuitively at least two different reasons that someone might have for being risk-averse. Consider a person who loves coffee but cannot tolerate more than one cup. Consider another person whose tolerance is very high, such that the first several cups are each as pleasurable as the last, but who has a particular attitude towards risk: it would take a very valuable upside in order for her to give up a guaranteed minimum number of cups. Both will prefer 1 cup of coffee to a coin-flip between 0 and 2, but intuitively they value cups of coffee very differently, and have very different reasons for their preference. This example generalizes: we might consider a person who is easily saturated with respect to money (once she has a bit of money, each additional bit matters less and less to her); and another person who is a miser—he likes each dollar just as much as the last—but nonetheless has the same attitude towards gambling as our coffee drinker. Both will disprefer mean-preserving spreads, but intuitively have different attitudes towards money and different reasons for this preference. Call the attitude of the second person in each pair *global sensitivity* (Allais 1953, Watkins 1977, Yaari 1987, Hansson 1988, Buchak 2013)[^allais-1953][^buchak-2013][^hansson-1988][^watkins-1977][^yaari-1987].

This kind of example gives rise to several problems. First, if EU maximization is supposed to *explain why* someone made a particular choice, it ought to be able to distinguish these two reasons for preference; but if global sensitivity can be captured at all, it will have to be captured by a diminishing marginal utility function, identical to that of the first person in each pair. Second, if one adopts a view of the utility function according to which the decision-maker has introspective access to it, a decision-maker might report that she has preferences like the tolerant coffee drinker or the miser—her utility function is linear—but nonetheless if she maximizes EU her utility function will have to be concave; so EU maximization will get her utility function wrong. Finally, even if one holds that a decision-maker does not have introspective access to her utility function, if a decision-maker displays global sensitivity, then she will have some preferences that cannot be captured by an expectational utility function (Allais 1953, Hansson 1988, Buchak 2013)[^allais-1953][^buchak-2013][^hansson-1988].

A related worry displays a troubling implication of EU maximization’s equating risk-aversion with diminishing marginal utility. Rabin’s (2000) *Calibration Theorem* shows that if an EU-maximizer is mildly risk-averse in modest-stakes gambles, she will have to be absurdly risk-averse in high-stakes gambles. For example, if an individual would reject the gamble {−$100, 0.5; $110, 0.5} at any wealth level, then she must also reject the gamble {−$1000, 0.5; $n, 0.5} for any $n$ whatsoever.

Finally, the *Allais Paradox* identifies a set of preferences that are intuitive but cannot be captured by any expectational utility function (Allais 1953)[^allais-1953]. Consider the choice between the following two lotteries:

- $L_1 : \{\$5,000,000, 0.1; $0, 0.9\}$
- $L_2 : \{\$1,000,000, 0.11; \$0, 0.89\}$

Separately, consider the choice between the following two lotteries:

- $L_3 : \{\$1,000,000, 0.89; \$5,000,000, 0.1; \$0, 0.01\}$
- $L_4 : \{\$1,000,000, 1\}$

Most people (strictly) prefer $L_1$ to $L_2,$ and (strictly) prefer $L_4$ to $L_3,$ but there are no values $u(\$0),$ $u(\$1\rM),$ and $u(\$5\rM)$ such that $\EU(L_1) \gt \EU(L_2)$ and $\EU(L_4) \gt \EU(L_3).$ The Allais preferences violate the Independence Axiom; when the lotteries are suitably reframed as acts (e.g., defined over events such as the drawing of a 100-ticket lottery), they violate the Sure-thing Principle or related separability principles.

### 5.2 Proposals

There have been a number of descriptive attempts to explain global sensitivity, by those who are either uninterested in normative questions or assume that EU is the correct normative theory. The most well-known of these are prospect theory (Kahneman & Tversky 1979; Tversky & Kahneman 1992)[^kahneman-1979][^tversky-1992] and generalized utility theory (Machina 1982, 1983, 1987)[^machina-1982][^machina-1983][^machina-1987]; others are mentioned in the discussion below. See Starmer (2000) for an overview.

Some normative proposals seek to accommodate global sensitivity *within* expected utility theory, by making the inputs of the utility function more fine-grained. Proponents of this “refinement strategy” hold that decision-makers prefer $L_4$ to $L_3$ because the $0 outcome in $L_3$ would induce regret that one forewent a sure $1M (alternatively, because $L_4$ includes psychological certainty) and therefore that the consequence-descriptions should include these facts. Thus, the correct description of $L_3$ is:

$$L_3 : \{\$1,000,000, 0.89; \$5,000,000, 0.1; \$0 \textit{ and regret, } 0.01\}$$

Once these gambles are correctly described, there is no direct conflict with EU maximization (Raiffa 1986, Weirich 1986, Schick 1991, Broome 1991, Bermúdez 2009, Pettigrew 2015, Buchak 2015)[^bermúdez-2009][^broome-1991][^buchak-2015][^pettigrew-2015][^schick-1991][^weirich-1986]. The problem of when two outcomes that appear the same should be distinguished is taken up by Broome (1991), Pettit (1991), and Dreier (1996).

The thought that the value of a consequence depends on what might have been is systematized by Bradley and Stefánsson (2017). Their proposal uses a version of expected utility theory developed by Jeffrey (1965) and axiomatized by Bolker (1966). Jeffrey replaces the utility function by a more general “desirability” function Des, which applies not just to consequences but also to prospects; indeed, it doesn’t distinguish between “ultimate” consequences and prospects, since its inputs are propositions. Bradley and Stefánsson propose to widen the domain of Des to include counterfactual propositions, thus allowing that preferences for propositions can depend on counterfacts. For example, a decision-maker can prefer “I choose the risky options and get nothing, and I wouldn”t have been guaranteed anything if I had chosen differently’ to “I choose the risky option and get nothing, and I would have been guaranteed something if I had chosen differently”, which will rationalize the Allais preferences. (Incidentally, their proposal can also rationalize preferences that seemingly violate EU because of fairness considerations, as in an example from Diamond (1967).)

In a different series of articles (Stefánsson & Bradley 2015, 2019)[^bradley-2015][^stefánsson-2015][^stefánsson-2019], these authors again employ Jeffrey’s framework, but this time widen the domain of Des to include *chance propositions* (in addition to factual prospects), propositions like “the chance that I get $100 is 0.5”. They hold that a rational decision-maker can have a preference between various chances of $X,$ even on the supposition that $X$ obtains (she need not obey “Chance Neutrality”). They capture the idea of disliking risk as such by holding that even though a rational agent must maximize expected desirability, she need not have a $\Des$ function of $X$ that is expectational with respect to the Des function of chance propositions about $X$ (she need not obey “Linearity”). For example, $\Des(\text{“I get \$100”})$ need not be equal to $2(\Des(\text{“the chance that I get \$100 is 0.5”})).$ (This does not conflict with maximizing expected desirability, because it concerns only the relationship between particular inputs to the $\Des$ function, and does not concern the decision-maker’s subjective probabilities.). This proposal can also rationalize the Ellsberg preferences (section 4.1), because it allows the decision-maker to assign different probabilities to the various chance propositions (see also Bradley 2015)[^bradley-2015].

Other proposals hold that we should reject the aggregation norm of expected utility. The earliest of these came from Allais himself, who held that decision-makers care not just about the mean utility of a gamble, but also about the dispersion of values. He proposes that individuals maximize expected utility plus a measure of the riskiness of a gamble, which consists in a multiple of the standard deviation of the gamble and a multiple of its skewness. Formally, if $s$ stands for the standard deviation of $L$ and $m$ stands for the skewness of $L,$ then the utility value of $L$ will be (Allais 1953, Hagen 1979)[^allais-1953][^hagen-1979]:

$$\text{AH}(L) = \EU(L) + F(s, m/s^2) + \varepsilon$$

where $\varepsilon$ is an error term. He thus proposes that riskiness is an independently valuable property of a gamble, to be combined with (and traded off against) its expected utility. This proposal essentially treats the riskiness of a gamble as a property that is (dis)valuable in itself (see also Nozick 1993 on symbolic utility)[^nozick-1993].

A final approach treats global sensitivity as a feature of the decision-maker’s way of aggregating utility values. It might be that a decision-maker’s utility and probability function are not yet enough to tell us what he should prefer; he must also decide how much weight to give to what happens in worse states versus what happens in better states. In *risk-weighted expected utility* (Buchak 2013)[^buchak-2013], a generalization of Quiggin’s (1982) *anticipated utility* and a member of the rank-dependent family (see section 4.3.2), this decision is represented by his *risk function*.

Formally, let $g' = \{E_1, x_1;\ldots; E_n, x_n\}$ be a re-ordering of act $g$ from worst event to best event, so that $u(x_1) \le \ldots \le u(x_n).$ Then the *risk-weighted expected utility* of $g$ is:

$$ \REU (g') = u(x_{1}) + \sum_{i = 2}^{n} r \left(\sum_{j = i}^{n} p(E_{j})\right) \left(u(x_{i}) - u( x_{i - 1})\right)$$

with $0 \le r(p) \le 1,$ $r(0) = 0$ and $r(1) = 1,$ and $r(p)$ non-decreasing.

The risk function measures the weight of the top $p$-portion of consequences in the evaluation of an act—how much the decision-maker cares about benefits that obtain only in the top $p$-portion of states. (One could also think of the risk function as describing the solution to a distributive justice problem among one’s future possible selves—it says how much weight a decision-maker gives to the interests of the top $p$-portion of his future possible selves.) A *risk-avoidant* person is someone with a convex risk function: as benefits obtain in a smaller and smaller portion of states, he gives proportionally less and less weight to them. A *risk-inclined* person is someone with a concave risk function. And a *globally neutral person* is someone with a linear risk function, i.e., an EU maximizer.

Diminishing marginal value and global sensitivity are captured, respectively, by the utility function and the risk function. Furthermore, the Allais preferences can be accommodated by a convex risk function (Segal 1987, Prelec 1998, Buchak 2013; but see Thoma & Weisberg 2017)[^buchak-2013][^prelec-1998][^thoma-2017]. Thus, REU maximization holds that decision-makers have the Allais preferences because they care more about what happens in worse scenarios than better scenarios, or are more concerned with the minimum value than potential gains above the minimum.

The representation theorem for REU combines conditions from two existing theorems (Machina & Schmeidler 1992, Köbberling and Wakker 2003)[^köbberling-2003][^machina-1992], replacing the separability condition with two weaker conditions. One of these conditions fixes a unique probability function of events (Machina & Schmeidler’s “Strong Comparative Probability”, 1992)[^machina-1992] and the other fixes a unique risk function of probabilities; the latter is a restricted version of the separability condition (Köbberling & Wakker’s [2003] “Comonotonic” Tradeoff Consistency; see section 4.3.2). Since the representation theorem derives a unique probability function, a unique risk function, and a unique (up to positive affine transformation) utility function, it separates the contribution of diminishing marginal value and global sensitivity to a given preference ordering. One can disprefer mean-preserving spreads as a result of either type of risk-aversion, or a combination of both.

### 5.3 Normative Issues

Proposals that seek to retain EU but refine the outcome space face two particular worries. One of these is that the constraints of decision theory end up trivial (Dreier 1996)[^dreier-1996]; the other is that they saddle the decision-maker with preferences over impossible objects (Broome 1991)[^broome-1991].

For theories that reject the Sure-thing Principle or the Independence Axiom, several potential worries arise, including the worry that these axioms are intuitively correct (Harsanyi 1977, Savage 1954, Samuelson 1952; see discussion in McClennen 1983, 1990)[^harsanyi-1977][^mcclennen-1983][^mcclennen-1990][^samuelson-1952][^savage-1954]; that decision-makers will evaluate consequences inconsistently (Samuelson 1952, Broome 1991)[^broome-1991][^samuelson-1952]; and that decision-makers will reject cost-free information (Good 1967, Wakker 1988, Buchak 2013, Ahmed & Salow 2019, Campbell-Moore & Salow 2020)[^ahmed-2019][^buchak-2013][^campbell-moore-2020][^good-1967][^wakker-1988]. The most widely discussed worry is that these theories will leave decision-makers open to diachronic inconsistency (Raiffa 1968; Machina 1989; Hammond 1988; McClennen 1988, 1990; Seidenfeld 1988a,b; Maher 1993; Rabinowicz 1995, 1997; Buchak 2013, 2015, 2017; Briggs 2015; Joyce 2017; Thoma 2019)[^briggs-2015][^buchak-2013][^buchak-2015][^buchak-2017][^hammond-1988][^joyce-2017][^machina-1989][^maher-1993][^mcclennen-1988][^mcclennen-1990][^rabinowicz-1995][^rabinowicz-1997][^raiffa-1968][^seidenfeld-1988a][^thoma-2019].

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=rationality-normative-nonutility). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/rationality-normative-nonutility/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=rationality-normative-nonutility&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/rationality-normative-nonutility/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

- Konek, Jason, manuscript, “[Epistemic Conservativity and Imprecise Credence](https://dl.dropboxusercontent.com/s/6yl8sx0rkko0cey/ecic.pdf)”

## Related Entries

consequentialism | decision theory | decision theory: descriptive | infinity | Pascal’s wager | probabilities, imprecise | rational choice, normative: expected utility | risk | St. Petersburg paradox

[^ahmed-2019]: Ahmed, Arif and Bernhard Salow, 2019, “Don’t Look Now”, *The British Journal for the Philosophy of Science*, 70(2): 327–350. doi:10.1093/bjps/axx047

[^allais-1953]: Allais, Maurice, 1953, “Le Comportement de l’Homme Rationnel devant le Risque: Critique des Postulats et Axiomes de l’École Americaine”, *Econometrica*, 21(4): 503–546. doi:10.2307/1907921

[^armendt-1986]: Armendt, Brad, 1986, “A Foundation for Causal Decision Theory”, *Topoi*, 5(1): 3–19. doi:10.1007/BF00137825

[^armendt-1988]: –––, 1988, “Conditional Preference and Causal Expected Utility”, in William Harper and Brian Skyrms (eds.), *Causation in Decision, Belief Change, and Statistics*, Dordrecht: Kluwer, Volume II, pp. 3–24.

[^arntzenius-2004]: Arntzenius, Frank, Adam Elga, and John Hawthorne, 2004, “Bayesianism, Infinite Decisions, and Binding”, *Mind*, 113(450): 251–283. doi:10.1093/mind/113.450.251

[^arrow-1951]: Arrow, Kenneth, 1951, “Alternative Approaches to the Theory of Choice in Risk-Taking Situations”, *Econometrica*, 19: 404–437. doi:10.2307/1907465

[^aumann-1962]: Aumann, Robert J., 1962, “Utility Theory without the Completeness Axiom”, *Econometrica*, 30(3): 445–462. doi:10.2307/1909888

[^bartha-2007]: Bartha, Paul F.A., 2007, “Taking Stock of Infinite Values: Pascal’s Wager and Relative Utilities”, *Synthese*, 154(1): 5–52. doi:10.1007/s11229-005-8006-z

[^bartha-2016]: –––, 2016, “Making Do Without Expectations”, *Mind*, 125(499): 799–827. doi:10.1093/mind/fzv152

[^bermúdez-2009]: Bermúdez, José Luis, 2009, *Decision Theory and Rationality*, Oxford: Oxford University Press. doi:10.1093/acprof:oso/9780199548026.001.0001

[^bernoulli-1975]: Bernoulli, Jakob, [*DW*] 1975, *Die Werke von Jakob Bernoulli*, Band III, Basel: Birkhäuser. A translation from this by Richard J. Pulskamp of [Nicolas Bernoulli’s letters concerning the St. Petersburg Game is available online](https://web.archive.org/web/20200725100737/http://cerebro.xu.edu/math/Sources/NBernoulli/correspondence_petersburg_game.pdf).

[^bolker-1966]: Bolker, Ethan D., 1966, “Functions Resembling Quotients of Measures”, *Transactions of the American Mathematical Society*, 124(2): 292–312. doi:10.2307/1994401

[^bostrom-2011]: Bostrom, Nick, 2011, “Infinite Ethics”, *Analysis and Metaphysics*, 10: 9–59.

[^bradley-2015]: Bradley, Richard, 2015, “Ellsberg’s Paradox and the Value of Chances”, *Economics and Philosophy*, 32(2): 231–248. doi:10.1017/S0266267115000358

[^bradley-2017]: Bradley, Richard and H. Orri Stefánsson, 2017, “Counterfactual Desirability”, *British Journal for the Philosophy of Science*, 68(2): 482–533. doi:10.1093/bjps/axv023

[^bradley-2014]: Bradley, Seamus and Katie Siobhan Steele, 2014, “Should Subjective Probabilities be Sharp?”, *Episteme*, 11(3): 277–289. doi:10.1017/epi.2014.8

[^briggs-2015]: Briggs, Rachael, 2015, “Costs of Abandoning the Sure-Thing Principle”, *Canadian Journal of Philosophy*, 45(5–6): 827–840. doi:10.1080/00455091.2015.1122387

[^broome-1991]: Broome, John, 1991, *Weighing Goods: Equality, Uncertainty, and Time*, Oxford: Blackwell Publishers Ltd.

[^broome-1995]: –––, 1995, “The Two-Envelope Paradox”, *Analysis*, 55(1): 6–11. doi:10.2307/3328613

[^broome-1997]: –––, 1997, “Is Incommensurability Vagueness?”, in Ruth Chang (ed), *Incommensurability, Comparability, and Practical Reason*, Cambridge, MA: Harvard University Press, pp. 67–89.

[^buchak-2013]: Buchak, Lara, 2013, *Risk and Rationality*, Oxford: Oxford University Press. doi:10.1093/acprof:oso/9780199672165.001.0001

[^buchak-2015]: –––, 2015, “Revisiting Risk and Rationality: A Reply to Pettigrew and Briggs”, *Canadian Journal of Philosophy*, 45(5–6): 841–862. doi:10.1080/00455091.2015.1125235

[^buchak-2017]: –––, 2017, “Replies to Commentators”, *Philosophical Studies*, 174(9): 2397–2414. doi:10.1007/s11098-017-0907-4

[^builes-2022]: Builes, David, Sophie Horowitz, and Miriam Schoenfield, 2022, “Dilating and Contracting Arbitrarily”, *Noûs*, 56(1): 3–20. doi:10.1111/nous.12338

[^campbell-moore-2020]: Campbell-Moore, Catrin and Bernhard Salow, 2020, “Avoiding Risk and Avoiding Evidence”, *Australasian Journal of Philosophy*, 98(3): 495–515. doi:10.1080/00048402.2019.1697305

[^chandler-2014]: Chandler, Jake, 2014, “Subjective Probabilities Need Not Be Sharp”, *Erkenntnis*, 79(6): 1273–1286. doi:10.1007/s10670-013-9597-2

[^chang-1997]: Chang, Ruth, 1997, “Introduction”, in Ruth Chang (ed.), *Incommensurability, Incomparability, and Practical Reason*, Cambridge, MA: Harvard University Press, pp. 1–34.

[^chang-2002a]: –––, 2002a, *Making Comparisons Count*, London and New York: Routledge, Taylor & Francis Group.

[^chang-2002b]: –––, 2002b, “The Possibility of Parity”, *Ethics*, 112(4): 659–688. doi:10.1086/339673

[^chang-2012]: –––, 2012, “Are Hard Choices Cases of Incomparability?”, *Philosophical Issues*, 22: 106–126. doi:10.1111/j.1533-6077.2012.00239.x

[^chang-2015]: –––, 2015, “Value Incomparability and Incommensurability”, in *Oxford Handbook of Value Theory*, Iwao Hirose and Jonas Olson (eds.), Oxford: Oxford University Press.

[^chang-2016]: –––, 2016, “Parity: An Intuitive Case”, *Ratio* (new series), 29(4): 395–411. doi:10.1111/rati.12148

[^chen-2020]: Chen, Eddy Keming and Daniel Rubio, 2020, “Surreal Decisions”, *Philosophy and Phenomenological Research*, 100(1): 54–74. doi:10.1111/phpr.12510

[^chew-1996]: Chew, Soo Hong and Peter Wakker, 1996, “The Comonotonic Sure-Thing Principle”, *Journal of Risk and Uncertainty*, 12(1): 5–27. doi:10.1007/BF00353328

[^colyvan-2006]: Colyvan, Mark, 2006, “No Expectations”, *Mind*, 115(459): 695–702. doi:10.1093/mind/fzl695

[^colyvan-2008]: –––, 2008, “Relative Expectation Theory”, *Journal of Philosophy*, 105(1): 37–44. doi:10.5840/jphil200810519

[^colyvan-2016]: Colyvan, Mark and Alan Hájek, 2016, “Making Ado without Expectations”, *Mind*, 125(499): 829–857. doi:10.1093/mind/fzv160

[^constantinescu-2012]: Constantinescu, Cristian, 2012, “Value Incomparability and Indeterminacy”, *Ethical Theory and Moral Practice*, 15(1): 57–70. doi:10.1007/s10677-011-9269-8

[^de-1974]: De Sousa, Ronald B., 1974, “The Good and the True”, *Mind*, 83(332): 534–551. doi:10.1093/mind/LXXXIII.332.534

[^diamond-1967]: Diamond, Peter, 1967, “Cardinal Welfare, Individualistic Ethics, and Interpersonal Comparison of Utility: A Comment”, *Journal of Political Economy*, 75(5): 765–766. doi:10.1086/259353

[^dreier-1996]: Dreier, James, 1996, “Rational Preference: Decision Theory as a Theory of Practical Rationality”, *Theory and Decision*, 40(3): 249–276. doi:10.1007/BF00134210

[^easwaran-2008]: Easwaran, Kenny, 2008, “Strong and Weak Expectations”, *Mind*, 117(467): 633–641. doi:10.1093/mind/fzn053

[^easwaran-2014a]: –––, 2014a, “Decision Theory without Representation Theorems”, *Philosophers’ Imprint*, 14: art. 27 (30 pages). [[Easwaran 2014 available online](http://hdl.handle.net/2027/spo.3521354.0014.027)]

[^easwaran-2014b]: –––, 2014b, “Principal Values and Weak Expectations”, *Mind*, 123(490): 517–531. doi:10.1093/mind/fzu074

[^elga-2010]: Elga, Adam, 2010, “Subjective Probabilities Should be Sharp”, *Philosophers Imprint*, 10: art. 5 (11 pages). [[Elga 2010 available online](http://hdl.handle.net/2027/spo.3521354.0010.005)]

[^ellsberg-1961]: Ellsberg, Daniel, 1961, “Risk, Ambiguity, and the Savage Axioms”, *Quarterly Journal of Economics*, 75(4): 643–669. doi:10.2307/1884324

[^ellsberg-2001]: –––, 2001, *Risk, Ambiguity, and Decision*, New York: Garland.

[^eriksson-2007]: Eriksson, Lina and Alan Hájek, 2007, “What Are Degrees of Belief?”, *Studia Logica: An International Journal for Symbolic Logic*, 86(2): 183–213. doi:10.1007/s11225-007-9059-4

[^fine-2008]: Fine, Terrence L., 2008, “Evaluating the Pasadena, Altadena, and St Petersburg Gambles”, *Mind*, 177(467): 613–632. doi:10.1093/mind/fzn037

[^gärdenfors-1982]: Gärdenfors, Peter and Nils-Eric Sahlin, 1982, “Unreliable Probabilities, Risk Taking, and Decision Making”, *Synthese*, 53(3): 361–386. doi:10.1007/BF00486156

[^gert-2004]: Gert, Joshua, 2004, “Value and Parity”, *Ethics*, 114(3): 492–510. doi:10.1086/381697

[^ghirardato-2003]: Ghirardato, Paolo, Fabio Maccheroni, Massimo Marinacci, and Marciano Siniscalchi, 2003, “A Subjective Spin on Roulette Wheels”, *Econometrica*, 71(6): 1897–1908. doi:10.1111/1468-0262.00472

[^gilboa-1987]: Gilboa, Itzhak, 1987, “Expected Utility with Purely Subjective Non-Additive Probabilities”, *Journal of Mathematical Economics*, 16(1): 65–88. doi:10.1016/0304-4068(87)90022-X

[^gilboa-1989]: Gilboa, Itzhak and David Schmeidler, 1989, “Maximin Expected Utility Theory with Non-Unique Prior”, *Journal of Mathematical Economics*, 18(2):141–153. doi:10.1016/0304-4068(89)90018-9

[^griffin-1986]: Griffin, James, 1986, *Well-Being: Its Meaning, Measurement, and Moral Importance*, Oxford: Clarendon Press. doi:10.1093/0198248431.001.0001

[^good-1952]: Good, I. J., 1952, “Rational Decisions”, *Journal of the Royal Statistical Society: Series B (Methodological)*, 14(1): 107–114. doi:10.1111/j.2517-6161.1952.tb00104.x

[^good-1967]: –––, 1967, “On the Principle of Total Evidence”, *British Journal for the Philosophy of Science*, 17(4): 319–321. doi:10.1093/bjps/17.4.319

[^gwiazda-2014]: Gwiazda, Jeremy, 2014, “Orderly Expectations”, *Mind*, 123(490): 503–516. doi:10.1093/mind/fzu059

[^hacking-1972]: Hacking, Ian, 1972, “The Logic of Pascal’s Wager”, *American Philosophical Quarterly*, 9(2): 186–192.

[^hagen-1979]: Hagen, Ole, 1979, “Towards a Positive Theory of Preference Under Risk”, in Maurice Allais and Ole Hagen (eds.), *Expected Utility Hypothesis and the Allais Paradox*, Dordrecht: D. Reidel, pp. 271–302.

[^hájek-2003]: Hájek, Alan, 2003, “Waging War on Pascal’s Wager”, *Philosophical Review*, 112(1): 27–56. doi:10.1215/00318108-112-1-27

[^hájek-2014]: –––, 2014, “Unexpected Expectations”, *Mind*, 123(490): 533–567. doi:10.1093/mind/fzu076

[^hájek-2008]: Hájek, Alan and Harris Nover, 2008, “Complex Expectations”, *Mind*, 117(467): 643–664. doi:10.1093/mind/fzn086

[^hájek-2012]: Hájek, Alan and Michael Smithson, 2012, “Rationality and Indeterminate Probabilities”, *Synthese*, 187(1): 33–48. doi:10.1007/s11229-011-0033-3

[^hammond-1988]: Hammond, Peter J., 1988, “Consequentialist Foundations for Expected Utility”, *Theory and Decision*, 25(1): 25–78. doi:10.1007/BF00129168

[^hansson-1988]: Hansson, Bengt, 1988, “Risk-aversion as a Problem of Conjoint Measurement”, in Peter Gärdenfors and Nils-Eric Sahlin (eds.), *Decision, Probability, and Utility*, Cambridge: Cambridge University Press, pp. 136–158. doi:10.1017/CBO9780511609220.010

[^hare-2010]: Hare, Caspar, 2010, “Take the Sugar”, *Analysis*, 70(2): 237–247. doi:10.1093/analys/anp174

[^harsanyi-1977]: Harsanyi, John C., 1977, “On the Rationale of the Bayesian Approach: Comments on Professor Watkins’s Paperm”, in Butts and Hintikka (eds.), *Foundational Problems in the Special Sciences*, Dordrecht: D. Reidel.

[^hodges-1952]: Hodges, J.L., Jr. and E.L. Lehman, 1952, “The Uses of Previous Experience in Reaching Statistical Decisions”, *Annals of Mathematical Statistics*, 23(3): 396–407. doi:10.1214/aoms/1177729384

[^hurwicz-1951a]: Hurwicz, Leonid, 1951a, “A Class of Criteria for Decision-Making under Ignorance”, *Cowles Commission Discussion Paper: Statistics No. 356* [[Hurwicz 1951a available online](http://web.archive.org/web/20220607060550/https://cowles.yale.edu/sites/default/files/files/pub/cdp/s-0356.pdf)].

[^hurwicz-1951b]: –––, 1951b, “The Generalized Bayes-Minimax Principle”, *Cowles Commission Discussion Paper: Statistics No. 355*, [[Hurwicz 1951b available online](http://web.archive.org/web/20220421193512/https://cowles.yale.edu/sites/default/files/files/pub/cdp/s-0355.pdf)].

[^jeffrey-1965]: Jeffrey, Richard, 1965, *The Logic of Decision*, New York: McGraw-Hill Inc.

[^jordan-1994]: Jordan, Jeff, 1994, “The St. Petersburg Paradox and Pascal’s Wager”, *Philosophia*, 23(1–4): 207–222. doi:10.1007/BF02379856

[^joyce-1999]: Joyce, James M., 1999, *The Foundations of Causal Decision Theory*, Cambridge: Cambridge University Press. doi:10.1017/CBO9780511498497

[^joyce-2005]: –––, 2005, “How Probabilities Reflect Evidence”, *Philosophical Perspectives*, 19(1): 153–179. doi:10.1111/j.1520-8583.2005.00058.x

[^joyce-2011]: –––, 2011, “A Defense of Imprecise Credences in Inference and Decision Making”, *Philosophical Perspectives*, 24: 281–323. doi:10.1111/j.1520-8583.2010.00194.x

[^joyce-2017]: –––, 2017, “Commentary on Lara Buchak’s Risk and Rationality”, *Philosophical Studies*, 174(9): 2385–2396. doi:10.1007/s11098-017-0905-6

[^kahneman-1979]: Kahneman, Daniel and Amos Tversky, 1979, “Prospect Theory: An Analysis of Decision under Risk”, *Econometrica*, 47(2): 263–291. doi:10.2307/1914185

[^köbberling-2003]: Köbberling, Veronika and Peter P. Wakker, 2003, “Preference Foundations for Nonexpected Utility: A Generalized and Simplified Technique”, *Mathematics of Operations Research*, 28(3): 395–423. doi:10.1287/moor.28.3.395.16390

[^kyburg-1968]: Kyburg, Henry E., 1968, “Bets and Beliefs”, *American Philosophical Quarterly*, 5(1): 63–78.

[^kyburg-1983]: –––, 1983, “Rational Belief”, *Behavioral and Brain Sciences*, 6(2): 231–245. doi:10.1017/S0140525X00015661

[^lauwers-2016]: Lauwers, Luc and Peter Vallentyne, 2016, “Decision Theory without Finite Standard Expected Value”, *Economics and Philosophy*, 32(3): 383–407. doi:10.1017/S0266267115000334

[^levi-1974]: Levi, Isaac, 1974, “On Indeterminate Probabilities”, *The Journal of Philosophy*, 71(13): 391–418. doi:10.2307/2025161

[^levi-1983]: –––, 1983, *The Enterprise of Knowledge*, Cambridge, MA: MIT Press.

[^levi-1986]: –––, 1986, “The Paradoxes of Allais and Ellsberg”, *Economics and Philosophy*, 2(1): 23–53. doi:10.1017/S026626710000078X

[^luce-1957]: Luce, R. Duncan and Howard Raiffa, 1957, *Games and Decisions*, New York: John Wiley & Sons, Inc..

[^machina-1982]: Machina, Mark J., 1982, “‘Expected Utility’ Analysis without the Independence Axiom”, *Econometrica*, 50(2): 277–323. doi:10.2307/1912631

[^machina-1983]: –––, 1983, “Generalized Expected Utility Analysis and the Nature of Observed Violations of the Independence Axiom”, in B.P. Stigum and F. Wenstop (eds.) *Foundations of Utility and Risk Theory with Applications*, Dordrecht: D. Reidel, pp. 263–293.

[^machina-1987]: –––, 1987, “Choice Under Uncertainty: Problems Solved and Unsolved”, *Journal of Economic Perspectives*, 1(1): 121–154. doi:10.1257/jep.1.1.121

[^machina-1989]: –––, 1989, “Dynamic Consistency and Non-expected Utility Models of Choice Under Uncertainty”, *Journal of Economic Literature*, 27(4): 1622–1668.

[^machina-1992]: Machina, Mark J. and David Schmeidler, 1992, “A More Robust Definition of Subjective Probability”, *Econometrica*, 60(4): 745–780. doi:10.2307/2951565

[^maher-1993]: Maher, Patrick, 1993, *Betting on Theories*, Cambridge: Cambridge University Press. doi:10.1017/CBO9780511527326

[^mayo-wilson-2016]: Mayo-Wilson, Conor and Gregory Wheeler, 2016, “Scoring Imprecise Credences: A Mildly Immodest Proposal”, *Philosophy and Phenomenological Research*, 93(1): 55–87. doi:10.1111/phpr.12256

[^mcclennen-1983]: McClennen, Edward F., 1983, “Sure-thing doubts”, in B.P. Stigum and F. Wenstop (eds.), *Foundations of Utility and Risk Theory with Applications*, Dordrecht: D. Reidel, pp. 117–136.

[^mcclennen-1988]: –––, 1988, “Ordering and Independence: A Comment on Professor Seidenfeld”, *Economics and Philosophy*, 4(2): 298–308. doi:10.1017/S0266267100001115

[^mcclennen-1990]: –––, 1990, *Rationality and Dynamic Choice: Foundational Explorations*, Cambridge: Cambridge University Press. doi:10.1017/CBO9780511983979

[^mcgee-1999]: McGee, Vann, 1999, “An Airtight Dutch Book”, *Analysis*, 59(4): 257–265. doi:10.1093/analys/59.4.257

[^meacham-2019]: Meacham, Christopher J.G., 2019, “Difference Minimizing Theory”, *Ergo*, 6(35): 999–1034. doi:10.3998/ergo.12405314.0006.035

[^monton-2019]: Monton, Bradley, 2019, “How to Avoid Maximizing Expected Utility”, *Philosophers’ Imprint*, 19: art. 18 (25 pages). [[Monton 2019 available online](http://hdl.handle.net/2027/spo.3521354.0019.018)]

[^moss-2015]: Moss, Sarah, 2015, “Credal Dilemmas”, *Noûs*, 49(4): 665–683. doi:10.1111/nous.12073

[^nover-2004]: Nover, Harris and Alan Hájek, 2004, “Vexing Expectations”, *Mind*, 113(450): 237–249. doi:10.1093/mind/113.450.237

[^nozick-1993]: Nozick, Robert, 1993, “Decision-Value”, Chapter 2 of *The Nature of Rationality*, Princeton, NJ: Princeton University Press.

[^pascal-1670]: Pascal, Blaise, 1670, *Pensées*, Paris.

[^pettigrew-2015]: Pettigrew, Richard, 2015, “Risk, Rationality and Expected Utility Theory”, *Canadian Journal of Philosophy*, 45(5–6): 798–826. doi:10.1080/00455091.2015.1119610

[^pettit-1991]: Pettit, Philip, 1991, “Decision Theory and Folk Psychology”, in Michael Bacharach and Susan Hurley (eds.), *Foundations of Decision Theory*, Oxford: Basil Blackwell Ltd., pp. 147–175.

[^prelec-1998]: Prelec, Drazen, 1998, “The Probability Weighting Function”, *Econometrica*, 66(3): 497–527. doi:10.2307/2998573

[^quiggin-1982]: Quiggin, John, 1982, “A Theory of Anticipated Utility”, *Journal of Economic Behavior & Organization*, 3(4): 323–343. doi:10.1016/0167-2681(82)90008-7

[^rabin-2000]: Rabin, Matthew, 2000, “Risk Aversion and Expected-Utility Theory: A Calibration Theorem”, *Econometrica*, 68(5): 1281–1292. doi:10.1111/1468-0262.00158

[^rabinowicz-1995]: Rabinowicz, Wlodek, 1995, “To Have One’s Cake and Eat It, Too: Sequential Choice and Expected-Utility Violations:”, *Journal of Philosophy*, 92(11): 586–620. doi:10.2307/2941089

[^rabinowicz-1997]: –––, 1997, “On Seidenfeld’s Criticism of Sophisticated Violations of the Independence Axiom”, *Theory and Decision*, 43(3): 279–292. doi:10.1023/A:1004920611437

[^rabinowicz-2008]: –––, 2008, “Value Relations”, *Theoria*, 74: 18–49. doi:10.1111/j.1755-2567.2008.00008.x

[^raiffa-1968]: Raiffa, Howard, 1968, *Decision Analysis: Introductory Lectures on Choices Under Uncertainty*, Reading, MA: Addison-Wesley.

[^ramsey-1926]: Ramsey, Frank, 1926 [1931], “Truth and Probability”, Ch. VII of F. Ramsey, *The Foundations of Mathematics and other Logical Essays*, edited by R.B. Braithwaite, London: Kegan Paul Ltd., 1931, 156–198.

[^raz-1988]: Raz, Joseph, 1988, “Incommensurability”, chapter 13 of *The Morality of Freedom*, Oxford: Oxford University Press, pp. 321–368.

[^rinard-2015]: Rinard, Susanna, 2015, “A Decision Theory for Imprecise Probabilities”, *Philosophers’ Imprint*, 15: art. 7 (16 pages). [[Rinard 2015 available online](http://hdl.handle.net/2027/spo.3521354.0015.007)]

[^rothschild-1972]: Rothschild, Michael and Joseph E Stiglitz, 1972, “Addendum to ‘Increasing Risk: I. A Definition’”, *Journal of Economic Theory*, 5(2): 306. doi:10.1016/0022-0531(72)90112-3

[^samuelson-1952]: Samuelson, Paul A., 1952, “Probability, Utility, and the Independence Axiom”, *Econometrica*, 20(4): 670–678. doi:10.2307/1907649

[^sartre-1946]: Sartre, Jean-Paul, 1946, *L'Existentialisme est un humanisme*, Paris: Nagel. Translated as *Existentialism is a Humanism*, Carol Macomber (trans.), New Haven, CT: Yale University Press, 2007.

[^savage-1954]: Savage, Leonard, 1954, *The Foundations of Statistics*, New York: John Wiley and Sons.

[^schick-1979]: Schick, Frederic, 1979, “Self-Knowledge, Uncertainty, and Choice”, *British Journal for the Philosophy of Science*, 30(3): 235–252. doi:10.1093/bjps/30.3.235

[^schick-1991]: –––, 1991, *Understanding Action: An Essay on Reasons*, Cambridge: Cambridge University Press. doi:10.1017/CBO9781139173858

[^schmeidler-1989]: Schmeidler, David, 1989, “Subjective Probability and Expected Utility without Additivity”, *Econometrica*, 57(3): 571–587. doi:10.2307/1911053

[^schmidt-2004]: Schmidt, Ulrich, 2004, “Alternatives to Expected Utility: Formal Theories”, chapter 15 of *Handbook of Utility Theory*, Salvador Barberà, Peter J. Hammond, and Christian Seidl (eds.), Boston: Kluwer, pp. 757–837.

[^schoenfield-2017]: Schoenfield, Miriam, 2017, “The Accuracy and Rationality of Imprecise Credences”, *Noûs*, 51(4): 667–685. doi:10.1111/nous.12105

[^schoenfield-2020]: –––, 2020, “Can Imprecise Probabilities be Practically Motivated? A Challenge to the Desirability of Ambiguity Aversion”, *Philosophers’ Imprint*, 20: art. 30 (21 pages). [[Schoenfield 2020 available online](http://hdl.handle.net/2027/spo.3521354.0020.030)]

[^segal-1985]: Segal, Uzi, 1985, “Some Remarks on Quiggin’s Anticipated Utility”, *Journal of Economic Behavior and Organization*, 8(1): 145–154. doi:10.1016/0167-2681(87)90027-8

[^seidenfeld-1988a]: Seidenfeld, Teddy, 1988a, “Decision Theory without ‘Independence’ or without ‘Ordering’”, *Economics and Philosophy*, 4(2): 267–290. doi:10.1017/S0266267100001085

[^seidenfeld-1988b]: –––, 1988b, “Rejoinder”, *Economics and Philosophy*, 4(2): 309–315. doi:10.1017/S0266267100001127

[^seidenfeld-1990]: Seidenfeld, Teddy, Mark J. Schervish, and Joseph B. Kadane, 1990, “Decisions Without Ordering”, in E. Seig (ed.), *Acting and Reflecting: The Interdisciplinary Turn in Philosophy*, Dordrecht: Kluwer: 143–70.

[^seidenfeld-2009]: –––, 2009, “Preference for Equivalent Random Variables: A Price for Unbounded Utilities”, *Journal of Mathematical Economics*, 45(5–6): 329–340. doi:10.1016/j.jmateco.2008.12.002

[^seidenfeld-2010]: –––, 2010, “Coherent Choice Functions Under Uncertainty”, *Synthese*, 172(1): 157–176. doi:10.1007/s11229-009-9470-7

[^seidenfeld-2012]: –––, 2012, “Forecasting with Imprecise Probabilities”, *International Journal of Approximate Reasoning*, 53(8): 1248–1261. doi:10.1016/j.ijar.2012.06.018

[^sinnott-armstrong-1988]: Sinnott-Armstrong, Walter, 1988, *Moral Dilemmas*, Oxford: Blackwell.

[^shackle-1952]: Shackle, G.L.S., 1952, *Expectations in Economics*, Cambridge: Cambridge University Press.

[^skala-1975]: Skala, Heinz J., 1975, *Non-Archimedean Utility Theory*, Dordrecht: D. Reidel.

[^smith-2014]: Smith, Nicholas J.J., 2014, “Is Evaluative Compositionality a Requirement of Rationality?”, *Mind*, 123(490): 457–502. doi:10.1093/mind/fzu072

[^sobel-1996]: Sobel, Jordan Howard, 1996, “Pascalian Wagers”, *Synthese*, 108(1): 11–61. doi:10.1007/BF00414004

[^starmer-2000]: Starmer, Chris, 2000, “Developments in Non-Expected Utility Theory: The Hunt for a Descriptive Theory of Choice under Risk”, *Journal of Economic Literature*, 38(2): 332–382. doi:10.1257/jel.38.2.332

[^stefánsson-2015]: Stefánsson, H. Orri and Richard Bradley, 2015, “How Valuable Are Chances?”, *Philosophy of Science*, 82(4): 602–625. doi:10.1086/682915

[^stefánsson-2019]: –––, 2019, “What Is Risk Aversion?”, *The British Journal for the Philosophy of Science*, 70(1): 77–102. doi:10.1093/bjps/axx035

[^sturgeon-2008]: Sturgeon, Scott, 2008, “Reason and the Grain of Belief”, *Noûs*, 42(1): 139–165. doi:10.1111/j.1468-0068.2007.00676.x

[^sud-2014]: Sud, Rohan, 2014, “A Forward Looking Decision Rule for Imprecise Credences”, *Philosophical Studies*, 167(1): 119–139. doi:10.1007/s11098-013-0235-2

[^sugden-2004]: Sugden, Robert, 2004, “Alternatives to Expected Utility: Foundations”, Chapter 14 of *Handbook of Utility Theory*, Salvador Barberà, Peter J. Hammond, and Christian Seidl (eds.), Boston: Kluwer, pp. 685–755.

[^sugden-2009]: –––, 2009, “On Modelling Vagueness—and on *Not* Modelling Incommensurability”, *Aristotelian Society Supplementary Volume*, 83: 95–113. doi:10.1111/j.1467-8349.2009.00174.x

[^thoma-2019]: Thoma, Johanna, 2019, “Risk Aversion and the Long Run”, *Ethics*, 129(2): 230–253. doi:10.1086/699256

[^thoma-2017]: Thoma, Johanna and Jonathan Weisberg, 2017, “Risk Writ Large”, *Philosophical Studies*, 174(9): 2369–2384. doi:10.1007/s11098-017-0916-3

[^troffaes-2007]: Troffaes, Matthias C.M., 2007, “Decision Making under Uncertainty Using Imprecise Probabilities”, *International Journal of Approximate Reasoning*, 45(1): 17–29. doi:10.1016/j.ijar.2006.06.001

[^tversky-1992]: Tversky, Amos and Daniel Kahneman, 1992, “Advances in Prospect Theory: Cumulative Representation of Uncertainty”, *Journal of Risk and Uncertainty*, 5(4): 297–323. doi:10.1007/BF00122574

[^wakker-1988]: Wakker, Peter P., 1988, “Nonexpected Utility as Aversion of Information”, *Journal of Behavioral Decision Making*, 1(3): 169–175. doi:10.1002/bdm.3960010305

[^wakker-1989]: –––, 1989, *Additive Representations of Preferences, A New Foundation of Decision Analysis*, Dordrecht: Kluwer.

[^wakker-1994]: –––, 1994, “Separating Marginal Utility and Probabilistic Risk-aversion”, *Theory and Decision*, 36: 1–44. doi:10.1007/BF01075296

[^wakker-2010]: –––, 2010, *Prospect Theory: For Risk and Ambiguity*, Cambridge: Cambridge University Press. doi:10.1017/CBO9780511779329

[^wald-1950]: Wald, Abraham, 1950, *Statistical Decision Functions,* New York: John Wiley & Sons.

[^walley-1991]: Walley, Peter, 1991, “The Importance of Imprecision”, Ch. 5 of *Statistical Reasoning with Imprecise Probabilities* (Monographs on Statistics and Applied Probability 42), London: Chapman and Hall, pp. 207–281.

[^watkins-1977]: Watkins, J.W.N., 1977, “Towards a Unified Decision Theory: A Non-Bayesian Approach”, in R. Butts and J. Hintikka (eds.), *Foundational Problems in the Special Sciences*, Dordrecht: D. Reidel.

[^weirich-1986]: Weirich, Paul, 1986, “Expected Utility and Risk”, *British Journal for the Philosophy of Science*, 37(4): 419–442. doi:10.1093/bjps/37.4.419

[^weirich-2008]: –––, 2008, “Utility Maximization Generalized”, *Journal of Moral Philosophy*, 5(2): 282–299. doi:10.1163/174552408X329019

[^weirich-2020]: –––, 2020, *Rational Responses to Risks*, New York: Oxford University Press. doi:10.1093/oso/9780190089412.001.0001

[^white-2009]: White, Roger, 2009, “Evidential Symmetry and Mushy Credence”, in T. Szabo Gendler & J. Hawthorne (eds.), *Oxford Studies in Epistemology*, Oxford: Oxford University Press, pp. 161–186.

[^vallentyne-1993]: Vallentyne, Peter, 1993, “Utilitarianism and Infinite Utility”, *Australasian Journal of Philosophy*, 71(2): 212–217. doi:10.1080/00048409312345222

[^vallentyne-1997]: Vallentyne, Peter and Shelly Kagan, 1997, “Infinite Value and Finitely Additive Value Theory”, *The Journal of Philosophy*, 94(1): 5–26. doi:10.2307/2941011

[^vallinder-2018]: Vallinder, Aron, 2018, “Imprecise Bayesianism and Global Belief Inertia”, *The British Journal for the Philosophy of Science*, 69(4): 1205–1230. doi:10.1093/bjps/axx033

[^von-1944]: Von Neumann, John and Oskar Morgenstern, 1944, *Theory of Games and Economic Behavior*, Princeton, NJ: Princeton University Press.

[^yaari-1987]: Yaari, Menahem E., 1987, “The Dual Theory of Choice under Risk”, *Econometrica*, 55(1): 95–115. doi:10.2307/1911158

[^zynda-2000]: Zynda, Lyle, 2000, “Representation Theorems and Realism about Degrees of Belief”, *Philosophy of Science*, 67(1): 45–69. doi:10.1086/392761
