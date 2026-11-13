# Descriptive Decision Theory
**First published Tue Sep 26, 2017**

*Chandler, Jake*

Descriptive decision theory is concerned with characterising and explaining regularities in the choices that people are disposed to make. It is standardly distinguished from a parallel enterprise, normative decision theory, which seeks to provide an account of the choices that people *ought* to be disposed to make. Much of the work in this area has been devoted to the building and testing of formal models that aim to improve on the descriptive adequacy of a framework known as “Subjective Expected Utility” (SEU). This adequacy was first called into question in the middle of the last century and further challenged by a slew of experimental work in psychology and economics from the mid 1960s onwards.

This entry first sketches out the basic commitments of SEU, before moving on to some of its best-known empirical shortcomings and a small selection of those models that have been proposed to supersede it. The relation between descriptive decision theory and its normative counterpart is then discussed, drawing some connections with a number of related topics in the philosophical literature.[^note-1]

## 1. The Standard Model: Subjective Expected Utility

The canonical theory of choice—*Subjective Expected Utility* (SEU)—owes its inception to the work of Savage (1954), building on previous contributions by De Finetti (1937), Ramsey (1931) and von Neumann and Morgenstern (1947). It offers a homogenous treatment of both decisions under “*risk*”—situations in which the decision maker has knowledge of, or holds firm beliefs regarding, the objective probabilities of all events pertinent to the success of his or her actions—and decisions under “*uncertainty*”—in which he or she does not. In its non-normative incarnation, it proposes at the very least that agents can be described *as if*:

1. associating with the possible consequences of the acts available to them two numerical quantities:
2. a “*utility*” corresponding to the degree to which they would desire the outcome to occur and
3. a “*subjective probability*” corresponding to their degree of confidence in the occurrence of the outcome given the performance of the act, a degree of confidence which may or may not be given by a corresponding assessment of objective probabilities;
4. being such that their preferences between acts, and hence their dispositions to chose certain acts over others, are determined by these quantities in such a way that acts are ranked by their *subjective expected utility*, i.e., the subjective probability-weighted sum of the utilities of their possible outcomes.

Ontologically bolder incarnations of the view have it that agents are so describable because they *really do* have degrees of belief and desires, introspectively familiar psychological states, that determine their preferences and choices in such a manner.

A number of important formal results, known as “representation theorems”, show that this claim about describability can be derived from a set of *prima facie* plausible general principles, aka “postulates” or “axioms”, pertaining to the agents’ preferences over acts. Furthermore, not only are these axioms *collectively sufficient* to derive SEU’s claim, but a significant proper subset of them also turn out to be *individually necessary*. Unsurprisingly then, much of the work on assessing the empirical adequacy of SEU has focused on the testing of the aforementioned axioms. Such tests could, in the best case, undermine a key reason to endorse the claim and, in the worst, provide grounds to reject it. Accordingly, a brief sketch of Savage’s own early result is in order.

### 1.1 Savage’s representation theorem

In Savage’s framework, *acts* are modelled as functions that map possible *states* of the world to *outcomes*, the consequences, if you wish, of carrying out the relevant act in the relevant state of nature. The set of acts will be denoted by $\mathcal{A}=\{f_1, f_2,\ldots g_1, g_2 \ldots\}$, the set of states by $\mathcal{S}=\{s_1, s_2,\ldots\}$ and the set of outcomes by $\mathcal{X}=\{x_1, x_2,\ldots,x_n\}$. For present purposes, it can be assumed that the acts considered are *simple*, i.e., that their range is finite. An act will be called “*constant*” if and only if it maps all states onto one same outcome. Sets of states, also known as *events*, will be denoted by upper-case letters $A_1, A_2,\ldots, B_1, B_2, \ldots$ etc. The set of such events will be denoted by $\mathcal{E}$. $E_i^f$ will denote the set of states that the act $f$ maps onto outcome $x_i$, i.e., $\{s\in\mathcal{S}: f(s)=x_i\}$. It will also be useful to denote by $fAg$ the act that maps the states in $A$ to the same outcomes that $f$ does and the states outside of $A$ to the same outcomes that $g$ does.

The agent’s choice dispositions at a given point in time are taken to be determined by his or her preferences, in such a way that, from any set of particular acts, the agent is liable to choose all and only those acts to which no other act is strictly preferred. $f\succeq g$ will denote the fact that an agent finds act $f$ to be no less desirable than act $g$. $\succ$ (strict preference) and $\sim$ (indifference) respectively stand for the asymmetric and symmetric parts of $\succeq$, so that $f\succ g$ iff $f\succeq g$ but not $g\succeq f$ and $f\sim g$ iff both $f\succeq g$ and $g\succeq f$. It is convenient to extend this preference relation to the set of outcomes by setting, for all outcomes $x_1$ and $x_2$, $x_1\succeq x_2$ iff the constant act that yields $x_1$ in all states is weakly preferred to the one that yields $x_2$ in all states.

Savage proves that there exists a certain specific set of constraints on preference orderings over acts that will be satisfied if and only if this ordering is representable by a real-valued function $U$ with domain $\mathcal{A}$ (so that $f\succeq g$ iff $U(f)\succeq U(g)$), such that

$$\tag{1} U(f)= \sum\limits_{i=1}^n P(E_i^f)u(x_i)$$

where $u : \mathcal{X}\mapsto \mathbb{R}$ is a consequence utility function unique up to positive linear transformation and $P: \mathcal{S}\mapsto [0,1]$ is a unique subjective probability function, satisfying $P(\varnothing)=0$, $P(\mathcal{S})=1$, and the finite additivity property $P(A\cup B)=P(A)+P(B)$ for all disjoint events $A,B$. In other words, $U$ returns the sum of the utilities of the possible outcomes, each multiplied by the subjective probability of the set of states which are mapped onto that outcome.

For the case in which $\mathcal{X}$ is finite, Savage’s set of axioms numbers six. Only three of these, however, make an appearance in the subsequent discussion. The first requires no comment:

**Weak Order** $\succeq$ is a weak order, that is: it is both transitive (for all acts $f, g, h$: if $f\succeq g$ and $g\succeq h$, then $f\succeq h$) and complete (for all acts $f, g$: either $f\succeq g$ or $g\succeq f$).

The second tells us that, in comparing two acts, one ignores their behaviour on the set of states in which they have identical consequences:

**Sure-Thing** For all acts $f, g, h, h'$ and any event $A$: $fAh\succeq gAh$ iff $fAh'\succeq gAh'$.

The third is given as follows:

**Weak Comparative Probability** For all outcomes $x_1,x_2,x_3,x_4$ and events $A,B$: if $x_1\succ x_2$ and $x_3\succ x_4$, then $x_1Ax_2\succeq x_1Bx_2$ iff $x_3Ax_4\succeq x_3Bx_4$.

The rationale for its proposal lies in the idea that, if $x_1\succ x_2$, then $x_1Ax_2\succeq x_1Bx_2$ reflects a commitment to the claim that $A$ is at least as probable as $B$, and hence, so too must $x_3Ax_4\succeq x_3Bx_4$, when $x_3\succ x_4$.

These three conditions, it should be noted, are individually necessary for SEU representability, so that any SEU maximizer must satisfy them. In addition, Savage proposes two further non-necessary, aka “structural”, conditions—respectively known as “Non-Degeneracy” and “Small Event Continuity”, as well as a further, necessary, condition of “Eventwise Monotonicity”, which tells us that, under certain mild circumstances, the result of replacing one or more occurrences of a given outcome by another will yield a preferred act if and only if the new outcome is preferred to the original.

### 1.2 Savage’s proof

With all this in hand, Savage’s result can be established as follows. First, one introduces a relation of “subjective comparative probability” $\unrhd$, such that $A\unrhd B$ iff for all outcomes $x_1$ and $x_2$ such that $x_1\succ x_2$, $x_1Ax_2\succeq x_2Ax_1$ iff $x_1Bx_2\succeq x_2Bx_1$. Savage’s axioms can then be shown to ensure that $\unrhd$ satisfies a number of appropriate properties, with Small Event Continuity ensuring that $\unrhd$ is representable by a subjective probability function $P$ that is unique. It is worth noting that, in the presence of Weak Comparative Probability, it is mainly the Sure-Thing principle that allows the derivation of the additivity property of $P$.

Second, using these axioms again, it can then be established that an agent is indifferent between any two acts that, for each outcome, assign equal probabilities to the respective sets of states that they each map onto that outcome. In other words:

**State Neutrality** If $P_f=P_g$, then $f\sim g$, where $P_f(x_i) = P(E^f_i)$.

Since it can also be shown that, for every lottery $P$ in $\mathcal{P}$, there exists an act $f$ such that $P_f=P$, the important upshot of this result is that one can effectively simplify the representation of the agent’s preferences over acts, recasting them as preferences over the smaller set $\mathcal{P}$ of so-called *subjective lotteries*, i.e., subjective probability distributions over outcomes. To simplify notation, the preference relation over $\mathcal{P}$ will be denoted by the same symbol, $\succeq$, allowing context to disambiguate.

A further application of the axioms lets us establish that these preferences over lotteries satisfy three important properties: (i) a “Mixture Weak Order” condition, requiring the preferences over lotteries to be transitive and complete, (ii) a “Mixture Continuity” condition, the details of which are not of importance here and finally (iii) an “Independence” condition, which, alongside the ordering condition, will be the focus of considerable discussion in what follows.

To present this last condition, one more definition is required, alongside a piece of notation: For any two lotteries $P_f$ and $P_g$ and $\lambda\in[0,1]$, one can define a third simple lottery $\lambda P_f + (1-\lambda)P_g$ in $\mathcal{P}$, the $\lambda$-mixture of $P_f$ and $P_g$, by setting $(\lambda P_f + (1-\lambda)P_g)(x)$, the probability assigned to outcome $x$ by the mixture lottery, equal to $\lambda P_f(x) + (1-\lambda)P_g(x)$. It is heuristically useful to think of $\lambda P_f + (1-\lambda)P_g$ as a higher-order lottery that yields a probability of $\lambda$ of playing lottery $P_f$ and a complementary probability of playing $P_g$. The condition then reads:

**Independence** For all acts $f, g$ and $h$ and all $\lambda\in(0,1]$: $P_f\succeq P_g$ iff $\lambda P_f + (1-\lambda) P_h\succeq \lambda P_g + (1-\lambda) P_h$.

The proof is then completed by appealing to a result of von Neumann and Morgenstern (1947), which shows that the aforementioned trio of properties is necessary and sufficient for the representability of $\succeq$ by a function $U$ such that

$$U(P_f)=\sum\limits_{i=1}^{n}P_f(x_i)u(x_i),$$

where $u : \mathcal{X}\mapsto \mathbb{R}$ is a consequence utility function unique up to positive linear transformation.

### 1.3 The probability triangle

The *probability triangle* (aka “Marschak-Machina triangle”) offers a helpful visual representation of preferences over the space of lotteries over $\{x_1, x_2, x_3\}$, with $x_3\succ x_2 \succ x_1$. Since, for any $P\in \mathcal{P}$, $P(x_2)= 1- P(x_1)-P(x_3)$, one can represent the situation two-dimensionally, with lotteries appearing as points in a unit triangle in which the horizontal axis gives us $P(x_1)$ and the vertical one gives us $P(x_3)$. The northwestern, southwestern and southeastern corners respectively correspond to the lotteries yielding $x_3, x_2$ and $x_1$ for sure.

Now, as is easily demonstrated, SEU is committed to

**Stochastic Dominance** For all acts $f$ and $g$: if, for any outcome $x$, the probability according to $P_f$ of obtaining an outcome that is weakly preferred to $x$ is at least as great as the corresponding probability according to $P_g$ (in other words: $\sum_{\{y\in\mathcal{X}: y\succeq x\}} P_f(y)$ $\geq$ $\sum_{\{y\in\mathcal{X}: y\succeq x\}} P_g(y)$), then $P_f\succeq P_g$.

Indeed, the above principle follows from Independence and is in fact *equivalent* to Savage’s Eventwise Monotonicity condition, given the other conditions in place (Grant 1995)[^grant-1995]. Therefore lotteries become increasingly preferred both as one moves north and as one moves west, since, in doing either, one shifts probability from a less to a more preferred outcome (from $x_2$ to $x_3$ when moving north and from $x_1$ to $x_2$ when moving west). The indifference curves are hence upward-sloping. Steeper slopes correspond to greater risk aversion, in the following sense: northeastern movements increase the spread of the distribution, i.e., the degree of risk involved, shifting probabilities from the middle outcome ($x_2$) to the extremal ones ($x_1$ and $x_3$). The steeper the indifference curve, the greater an increase in probability of the best outcome is required in order to compensate for this increased risk. SEU clearly also requires that indifference curves be both linear and parallel.[^note-2] To illustrate:

*Figure 1*

![right triangle with the with the 90 degree angle on the bottom left and labeled '0'. The other two angles are each labeled '1'. The vertical side is labeled 'P(x_3)' and the horizontal side labeled 'P(x_1)'. Five parallel diagonal lines in the triangle from the bottom left to top right.](../assets/decision-theory-descriptive/fig1.svg)

Figure 1

Although SEU continues to enjoy widespread support as a normative model of choice behaviour (though see Section 5 below), it is no longer generally taken to be descriptively adequate. A number of substantial deviations from its predictions were noted as early as the 1950s and early 1960s by the likes of Allais (1953a,b) and Ellsberg (1961) and further investigated in the 1970s. These observations led to the development of alternative models whose own predictive consequences have become the focus of extensive testing in the past three decades or so.[^note-3]

## 2. The Issue of Independence

### 2.1 Allais’ paradoxes

Allais (1953a: 527) considered hypothetical preferences revealed by choices taken from two respective menus of lotteries yielding various increments in wealth with various objective probabilities, one containing $P_1$ and $P_2$ below, the other $P_3$ and $P_4$:

*Figure 2*

![circle with P1 with a line labeled '1' to the right pointing to '$1M'](../assets/decision-theory-descriptive/fig2a.svg)

(a)

![circle with P2 with a line labeled '.1' to '$5M' and a line labeled '.89' to '$1M' and a line labeled '.01' to '$0''](../assets/decision-theory-descriptive/fig2c.svg)

(b)

![circle with P3 with a line labeled '.11' to '$1M' and a line labeled '.89' to '$0''](../assets/decision-theory-descriptive/fig2b.svg)

(c)

![circle with P4 with a line labeled '.1' to '$5M' and a line labeled '.9' to '$0''](../assets/decision-theory-descriptive/fig2d.svg)

(d)

Figure 2

He claimed that, for a substantial proportion of agents, one would find that $P_{1}\succ P_{2}$ and $P_{4}\succ P_{3}$ (call these the “*Allais preferences*”). However, on the assumptions that (i) the subjects’ degrees of belief align themselves with the objective probabilities given and (ii) the outcomes can be adequately characterised entirely in terms of the associated changes in level of wealth, such a combination of preferences runs contrary to Independence. More specifically, it runs counter to the special case of the principle, according to which the substitution of a common “consequence”, i.e., lottery, in a pair of mixtures leave the order of preference unchanged:

**Common Consequence** For all acts $f, g, h, h'$ and $\lambda\in(0,1]$:

$$\begin{split} \lambda P_f + (1-\lambda) P_h\succeq \lambda P_g + (1-\lambda) P_h\\ \textrm{ iff }\lambda P_f + (1-\lambda) P_{h'}\succeq \lambda P_g + (1-\lambda) P_{h'}. \end{split} $$

To see why, let $\lambda=0.11$, $Q_1$ (the “consequence” common to $P_1$ and $P_2$) be a lottery yielding $$1$M for sure, $Q_2$ be a lottery yielding $$5$M with probability $10/11$ and $\$0$ otherwise, and finally $Q_3$ (the “consequence” common to $P_3$ and $P_4$) a lottery yielding $\$0$ for sure. $P_1$ turns out to be a $\lambda$-mixture of $Q_1$ and $Q_1$, $P_2$ one of $Q_2$ and $Q_1$, $P_3$ one of $Q_1$ and $Q_3$ and $P_4$ one of $Q_2$ and $Q_3$. This is probably best seen by considering the decision trees representing the corresponding compound lotteries:

*Figure 3*

![circle with P1 with a line labeled '.11' to a circle with Q1 which has a line labeled '1' to '$1M'. Another line from P1 labeled '1' goes to a circle also with Q1 which has a line labeled '1' to '$1M'.](../assets/decision-theory-descriptive/fig3a.svg)

(a)

![circle with P2 with a line labeled '.11' to a circle with Q2 which has a line labeled '10/11' to '$5M' and a line labeled '1/11' to '$0'. A second line from P1 labeled '.89' goes to a circle with Q1 which has a line labeled '1' to '$1M' ''](../assets/decision-theory-descriptive/fig3c.svg)

(b)

![circle with P3 with a line labeled '.11' to a circle with Q1 which has a line labeled '1' to '$1M'. Another line from P1 labeled '1' goes to a circle with Q3 which has a line labeled '1' to '$0'.](../assets/decision-theory-descriptive/fig3b.svg)

(c)

![circle with P4 with a line labeled '.11' to a circle with Q2 which has a line labeled '10/11' to '$5M' and a line labeled '1/11' to '$0'. A second line from P1 labeled '.89' goes to a circle with Q3 which has a line labeled '1' to '$0' ''](../assets/decision-theory-descriptive/fig3d.svg)

(d)

Figure 3

The upshot of this, by Common Consequence, is then that $P_1\succeq P_2$ iff $P_3\succeq P_4$.[^note-4]

The probability triangle affords a helpful illustration of the incompatibility of the Allais preferences with SEU. Indeed, the segments connecting $P_1$ and $ P_2$, on the one hand, and $ P_3$ and $P_4$ on the other are parallel, so that an EU maximiser, whose indifference curves are also parallel, would be incapable of exhibiting the modal preferences, since no pair of indifference curves could be, as required, such that one crosses the segment $[P_1,P_2]$ from below while the other crosses $[P_3,P_4]$ from above:

*Figure 4*

![Similar to figure 1 except no diagonal lines and the vertical side is labeled 'P(x_1)' and the horizontal 'P(x_3)'. In addition a short vertical segment starts at the right angle vertice and is labeled 'P_1' at the bottom and 'P_2' at the top. Another short vertical segment that seems to be the same length is on the right connecting the horizontal line of the triangle to its hypotenuse; it is labeled 'P_3' on the bottom and 'P_4' on the top.](../assets/decision-theory-descriptive/fig4.svg)

Figure 4

In addition to the above, which has come to be known as the *Common Consequence* problem, a further issue, the *Common Ratio* problem, was suggested by Allais (1953a: 529–530). The difficulty this time concerned a further consequence of Independence, which tells us that the order of preference between two identically-weighted mixtures that share a common component lottery is unaffected by a change in the mixture weight:

**Common Ratio** For all acts $f,g,h$ and $\lambda,\gamma\in(0,1]$:

$$\begin{split} \lambda P_f + (1-\lambda) P_h\succeq \lambda P_g + (1-\lambda) P_h\\ \textrm{ iff } \gamma P_f + (1-\gamma) P_h\succeq \gamma P_g + (1-\gamma) P_h. \end{split}$$

A presentation of the relevant pairs of options will not be given here. Note simply that, here again, the problematic choices turn out to involve two pairs of options whose respective corresponding segments in the probability triangle run parallel.[^note-5]

A number of experimental studies in the 1960s and 1970s subsequently confirmed the robustness of the effects uncovered by Allais. Slovic & Tversky (1974), for example, report that 17 out of 29 (59%) of subjects in their study exhibit Allais preferences in their investigation of the Common Consequence problem. See MacCrimmon & Larson (1979) for a helpful summary of this and other early work and further data of their own.

Since the late 1970s, a considerable number of generalisations of SEU have been devised to accommodate the problematic preference patterns. A brief survey of these is provided in the following subsection.

### 2.2 Theoretical responses

#### 2.2.1 Probabilistic sophistication

A substantial proportion of the responses to Allais-type phenomena have involved generalisations of SEU that remain conservative enough to preserve the requirement of what Machina & Schmeidler (1992) call “*probabilistic sophistication*”: that preferences over acts reduce to preferences over lotteries and that these in turn obey Mixture Weak Order, Mixture Continuity and Stochastic Dominance, if not Independence.[^note-6] Machina & Schmeidler offer an axiomatic characterisation of probabilistically sophisticated preferences that gives up Savage’s Sure-Thing condition, which plays a critical role in the derivation of Independence, and retains the remainder of his conditions. Since the Sure-Thing principle, however, *also* plays an important role in ensuring the existence of a suitable probability distribution over the set of events, they strengthen the Weak Comparative Probability condition to the following:

**Strong Comparative Probability** For all outcomes $x_1,x_2,x_3,x_4$, acts $f, g$ and disjoint events $A,B$: if $x_1\succ x_2$ and $x_3\succ x_4$, then $x_1Ax_2Bf\succeq x_2Ax_1Bf$ iff $x_3Ax_4Bg\succeq x_4Ax_3Bg$.

where $x_1Ax_2Bf$ denotes the act that yields $x_1$ for all $s\in A$, outcome $x_2$ for all $s\in B$ and $f(s)$ for all other $s$. They then offer a correspondingly amended account of the proposed correspondence between the subjective qualitative probability and preference relations, proposing that, if $x_1\succ x_2$, then $A\unrhd B$ iff $x_1Ax_2Bf\succeq x_2Ax_1Bf$.

#### 2.2.2 Models with Betweenness

Among the models of probabilistically sophisticated preferences that do not satisfy Independence and, more specifically, do not impose the property of *parallelism* of indifference curves, a number still satisfy a weaker principle that imposes *linearity*, namely:

**Betweenness** For all acts $f$ and $g$ and $\lambda\in[0,1]$: if $P_f\sim P_g$, then $P_f\sim \lambda P_f + (1-\lambda) P_g$.

This is notably the case of *Weighted Utility* (WU) (Chew & MacCrimmon 1979; Chew 1983)[^chew-1983][^chew-1979][^maccrimmon-1979], which proposes that the summands in the expected utility formula each be multiplied by a corresponding weight, so that preferences between lotteries are representable by the more general functional

$$\tag{2}U(f)=\sum\limits_{i=1}^{n} P_f(x_i)u(x_i)\Bigg(w(x_i)/\sum\limits_{i=1}^{n} w(x_i)P_f(x_i)\Bigg)$$

where $w$ is a positive real-valued function on $\mathcal{X}$. If $w$ is constant, one recovers the EU functional. The incorporation of weights accommodates Allais preferences by allowing indifference curves to “fan out” from a single intersection located in the quadrant to the southwest of the probability triangle. These curves become steeper, and hence represent a greater degree of risk aversion, as one moves northwest, in the direction of increasingly preferred lotteries. A suitably placed intersection allows indifference curves to cross both $[P_1,P_2]$ from below and $[P_3,P_4]$ from above, as required.[^note-7]

#### 2.2.3 Models without Betweenness

There is however substantial evidence that the linearity of indifference curves isn’t any more empirically adequate that their parallelism (see Camerer & Ho 1994 for a survey)[^camerer-1994] and a number of models of probabilistically sophisticated preferences give up on Betweenness too. The best known of these is undoubtedly *Rank Dependent Utility* (RDU), a version of which was first proposed by Quiggin (1982).[^note-8] To present the proposal in functional form, it will be assumed that the subscripts associated with each outcome in $\mathcal{X}$ indicate increasing order of preference, so that $x_1\preceq x_2\preceq \ldots \preceq x_n$ and hence $\bigcup\limits_{j=i}^{n} E^{f}_{j}$ is the event given which $f$ yields an outcome at least as preferable as $x_i$. RDU proposes:

$$\tag{3} U(f)=u(x_1) + \sum\limits_{i=2}^{n} \Big(u(x_i)-u(x_{i-1})\Big) w \Bigg(P\bigg(\bigcup\limits_{j=i}^{n} E^{f}_{j}\bigg)\Bigg)$$

where $w : [0,1]\mapsto[0,1]$ is a strictly increasing probability weighting function, such that $w(0)=0$ and $w(1)=1$. In other words: the utility of a lottery is equal to the sum of the marginal utility contributions of the outcomes, each multiplied by the weighted probability of obtaining an outcome that is at least as preferable (the marginal contribution of $x_1$ is $u(x_1)$ and its associated multiplier is $w\big(P(\{\mathcal{S}\})\big)=w(1)=1$). If $w$ is the identity function, so that $w\circ P=P$, it turns out that one recovers the expected utility functional. If not, a suitable choice of $w$ enables one to recover the Allais preferences. To see how, assume for simplicity that $u(0)=0$. One then has $P_1\succ P_2$ iff

$$u(1)w(1)>u(1)w(0.99)+\big(u(5)-u(1)\big)w(0.1)$$

and $P_4\succ P_3$ iff $u(5)w(0.1)>u(1)w(0.11)$. This implies that the preferences will be recovered by having $w$ be such that $w(1)-w(0.99)>w(0.11)-w(0.1)$, so that a difference in probability of $0.01$ has a greater impact at the higher end of the probability scale than it does towards its relatively lower end.[^note-9]

It should be noted that RDU is itself a special case of what is perhaps the best known alternative to SEU, Kahneman & Tversky’s *Cumulative Prospect Theory* (Tversky & Kahneman 1992)[^tversky-1992], which earned Kahneman a Nobel Prize in Economics in 2002. This model generalises RDU by introducing a *reference point*, an outcome that partitions the set of outcomes into positive and negative subsets, according to whether these are strictly preferred or strictly dispreferred to it. *Two* probability transformation functions, $w^+$ and $w^-$, are then involved in the preference functional: $w^+$ in determining the utility contributions of the negative outcomes and $w^-$ playing an analogous role in relation to that of the positive ones. RDU is recovered when $w^+$ is the dual of $w^+$.

While RDU does not satisfy Independence, it does satisfy a weakening of this principle known as “Ordinal Independence” (Green & Jullien 1988)[^green-1988]. This principle is presented as a constraint on the *cumulative distribution functions* (cdf) corresponding to various lotteries, which return, for each $x_i$, the probability of obtaining an outcome that is no better than $x_i$ (i.e., an outcome $x_j$, with $j\leq i$). The cdf corresponding to $P_f$ shall be denoted by $F$. We then have

**Ordinal Independence** For all acts $f,f',g$ and $g'$ and subsets $A$ of $\mathcal{X}$: If $P_f\succeq P_g$, and

1. for all $x\in A$, $F(x)=G(x)$ and $F'(x)=G'(x)$
2. for all $x\notin A$, $F(x)=F'(x)$ and $G'(x)=G'(x)$

then $P_{f'}\succeq P_{g'}$.[^note-10]

The constraint can more helpfully be put as follows: In comparing two acts, one ignores the values of their respective cdf’s on the set of outcomes with respect to which they agree. It is easily verified that the Allais preferences are consistent with this principle. Given probabilistic sophistication, Ordinal Independence can itself be derived from a constraint on preferences over acts known as “Comonotonic Independence”, presented in Subsection 3.2.1 below. Wakker (2010) offers a textbook introduction to RDU and Cumulative Prospect Theory, as well as to related treatments of the issues discussed in the next section.

## 3. The Issue of Probabilistic Belief

### 3.1 Ellsberg’s Three Colour paradox

In another classic challenge to SEU, Ellsberg (1961) asked subjects to consider a setup in which an urn contains 30 red balls and 60 black or yellow balls in unknown relative proportions and report their preferences between various bets on the colour of a ball drawn at random from the urn. The preferences elicited were the ones holding between $f_1$ and $g_1$ below, on the one hand, and $f_2$ and $g_2$, on the other:

|   | $\overbrace{\phantom{30 balls}}^{\textrm{30 balls}}$ | $\overbrace{\phantom{45630 balls}}^{\textrm{60 balls}}$ |   |
| --- | --- | --- | --- |
|   | r | b | y |
| $f_1$ | $100 | $0 | $0 |
| $g_1$ | $0 | $100 | $0 |
| $f_2$ | $100 | $0 | $100 |
| $g_2$ | $0 | $100 | $100 |

Ellsberg reported that a majority of subjects exhibited the preferences $f_1\succ g_1$, but $g_2\succ f_2$, an instance of a phenomenon that has come to be known as *ambiguity aversion*: a relative preference for betting on events of known rather than unknown (“ambiguous”) probability.

If one grants that the outcomes are adequately characterised in sole terms of associated changes in level of wealth, these “Ellsberg preferences” stand in direct contradiction with Savage’s Sure-Thing principle. These preferences also violate Machina & Schmeidler’s Strong Comparative Probability principle, on the natural assumption that the subjects strictly prefer the outcome $\$100$ to the outcome $\$0$. And indeed it is easy to see that the Ellsberg preferences are inconsistent with probabilistic sophistication. More specifically, they are incompatible with its being the case that both (i) the decision maker’s preferences over acts are reducible to preferences over corresponding lotteries over outcomes, generated by an assignment of subjective probabilities to the set of events and (ii) he or she partially orders these lotteries by first-order stochastic dominance. To see why, assume that these conditions hold. Note first that $P_{g_1}$ would stochastically dominate $P_{f_1}$ if and only if $P(\{b\})\geq P(\{r\})$ and that $P_{f_2}$ would stochastically dominate $P_{g_2}$ if and only if $P(\{r\})\geq P(\{b\})$. $f_1\succ g_1$ would entail that $P_{g_1}$ does not stochastically dominate $P_{f_1}$, and hence that $P(\{r\}) > P(\{b\})$. But $g_2\succ f_2$ would entail that $P_{f_2}$ does not stochastically dominate $P_{g_2}$, and hence that $P(\{b\})> P(\{r\})$. Contradiction.

Considerable empirical evidence has confirmed Ellsberg’s informal observations and related phenomena (beginning with Becker & Brownson 1964 and including classic studies such as Slovic & Tversky 1974 and MacCrimmon & Larsson 1979; see the classic Camerer & Weber 1992, as well as the more up-to-date Trautmann & van de Kuilen 2015, for further details)[^becker-1964][^camerer-1992][^maccrimmon-1979][^slovic-1974][^trautmann-2015] and the literature now contains a substantial number of generalisations of SEU that can accommodate these.

### 3.2 Theoretical responses

#### 3.2.1 Non-additive “probabilities”

One prominent weakening of SEU that is capable of accommodating the Ellsberg cases is *Choquet Expected Utility* (CEU), initially proposed by Schmeidler (1989). The key concept in its representation of preferences is that of a *capacity*: a function $v : \mathcal{E}\mapsto [0,1]$, such that $v(\varnothing)=0$, $v(\mathcal{S})=1$ and, for all $A, B\in \mathcal{E}$, $A\subseteq B$ implies $v(A)\leq v(B)$. One can think of this as a kind of non-additive “probability” function, since the additivity property, according to which $v(A\cup B)=v(A)+v(B)$ for disjoint events $A$ and $B$, does not hold. As with the presentation of RDU, the convention here is that the indices associated with the outcomes indicate increasing preference, so that, again, $\bigcup\limits_{j=i}^{n} E^{f}_{j}$ is the event given which $f$ yields an outcome at least as preferable as $x_i$. CEU proposes:

$$\tag{4} U(f)=u(x_1) + \sum\limits_{i=2}^{n} \Big(u(x_i)-u(x_{i-1})\Big) v \Bigg(\bigcup\limits_{j=i}^{n} E^{f}_{j}\Bigg)$$

On this suggestion, then an act is valued by the sum of the marginal utility contributions of the outcomes, each multiplied by the capacity of the event given which that act would yield an outcome that is at least as preferable. There are obvious formal similarities here with RDU and, in fact, the latter can be viewed as the special case of CEU in which the decision maker’s capacities are derived from his or her probabilistic degrees of belief by a probability weighting function ($v=w\circ P$).[^note-11]

Returning to the Ellsberg preferences in the three colour problem, it is easy to see that $f_1\succ g_1$ iff $v(\{r\}) > v(\{b\})$ and $g_2\succ f_2$ iff $v(\{b,y\}) > v(\{r,y\})$. These inequalities obviously cannot be simultaneously satisfied in special cases in which $c$ is additive and indeed, in such cases, CEU reduces to SEU. In the more general case, there is no problem: let $v$, for instance, be such that:

$$\begin{aligned} v(\{r\})&=v(\{r,y\})=v(\{b,y\})=\nicefrac{1}{3}\\ v(\{b\})&=v(\{y\})=0\\ v(\{b,y\})&=\nicefrac{2}{3}. \end{aligned}$$

Gilboa (1987) and Wakker (1989) have both provided axiomatisations of the proposal in a Savage framework. The key distinguishing feature of these is the effective restriction of Savage’s Sure-Thing principle to particular kinds of sets of acts:

**Comonotonic Sure-Thing** For all acts $f, g, h, h'$ and any event $A$: if $fAh$, $gAh$, $fAh'$ and $fAh'$ are comonotonic, then $fAh\succeq gAh$ iff $fAh'\succeq gAh'$.

where two acts $f$ and $g$ are *comonotonic* iff, there are no two states $s_1$ and $s_2$, such that $f(s_1)\succ f(s_2)$ but $g(s_2)\succ g(s_1)$, or again iff $f$ and $g$ yield orderings of states by desirability of associated consequence that are jointly consistent (Chew & Wakker 1996)[^chew-1996]. Clearly, the Ellsberg preferences are perfectly compatible with this weakening of the Sure-Thing principle, since the acts involved are not comonotonic. For instance, $f_1(r)\succ f_1(b)$ but $f_2(b)\succ f_2(r)$.[^note-12]

#### 3.2.2 Multiple priors

The capacity that was used above to illustrate the consistency of CEU with Ellsberg-style preferences has a noteworthy property: it is *convex*, meaning that it is such that, for all $A,B\in\mathcal{E}$,

$$v(A\cup B) + v(A\cap B) \geq v(A) + v(B).$$

It has been shown by Schmeidler (1986) that, if convexity of capacities is imposed, CEU becomes a special case of an approach known as *Maxmin Expected Utility* (MEU) (Gilboa & Schmeidler 1989)[^gilboa-1989][^schmeidler-1989], which represents the decision maker as maximising minimum expected utility across a non-empty set of probability functions $\Gamma$ on $\mathcal{X}$, so that:

$$\tag{5} U(f)=\inf\limits_{P\in\Gamma} \Big(\sum\limits_{i=1}^n P(E_i^f)u(x_i)\Big) \label{eq:MEU}$$

The specific connection is the following: a CEU maximiser with respect to a convex capacity $v$ is an EU maxminer over the so-called *core* of $v$, defined as the set of probability functions that assign, for every event, a probability that is at least as great as the capacity assigned to that event by $v$: $\{P\in\mathcal{P}: P(A)\geq v(A), \forall A\in\mathcal{E}\}$.

Now a common, but not mandatory, interpretation of $\Gamma$ is that it corresponds to the set of objective probability assignments that the decision maker takes to be consistent with his or her evidence. In view of the result just flagged out, this in turn invites an interpretation of capacities as lower estimates of objective probabilities. More specifically, a CEU maximiser whose capacity is convex can be interpreted as considering possible all and only those assignments of objective probabilities that are consistent with the lower estimates given by that capacity. This interpretation of the capacity in the particular example at hand is obviously particularly tempting, as $\nicefrac{1}{3}$ and $\nicefrac{2}{3}$ constitute plausible lower bounds on the decision maker’s estimates of the probabilities of $\{r\}$ and $\{b,y\}$, respectively.

If one interprets $\Gamma$ this way, relaxing CEU with convex capacities to MEU becomes an attractive option, since it allows one to not only model Ellsberg preferences but also accommodate the preferences of decision makers whose views on objective probabilities cannot simply be captured in terms of lower estimates (for example, those involving commitments to certain facts about ratios of probabilities). Due to space considerations, the details of the axiomatic treatment of MEU are omitted here.[^note-13]

Still, MEU remains rather restrictive, as it enforces a fairly radical form of ambiguity aversion. One popular generalisation of the model, $\alpha-$*MEU* (Ghirardato *et al.* 2004), proposes that the preferences imposed by MEU lie only at one end of a spectrum of possible ambiguity aversion, captured by the following weakening of $(\ref{eq:MEU})$:

$$\tag{6}U(f)=\alpha\inf\limits_{P\in\Gamma} \Big(\sum\limits_{i=1}^n P(E_i^f)u(x_i)\Big) + (1-\alpha)\sup\limits_{P\in\Gamma} \Big(\sum\limits_{i=1}^n P(E_i^f)u(x_i)\Big)$$

where $\alpha\in[0,1]$. With $\alpha=1$, one recovers the highly ambiguity-averse MEU. With $\alpha=0$, we have strongly ambiguity-loving preferences. The parameter $\alpha$ is thus in a sense interpretable as a measure of ambiguity aversion.[^note-14]^{,}[^note-15]

Just as with MEU, however, $\alpha$-MEU restricts its attention to extremal expected utilities (in this instance best- as well as worst-case). A popular class of proposals allows for the full range of expected utilities across $\Gamma$ to be factored in, by supplementing the multiple prior model with a *higher order probability distribution* $\mu$. One well-known functional form, that notably features in the “*Smooth Model*” of Klibanoff *et al.* (2005), involves taking the expectation, relative to $\mu$, of the *weighted* expected utilities, relative to the members of $\Gamma$:

$$\tag{7}U(f)=\sum\limits_{P\in \Gamma} \mu(P) \Phi\Big(\sum\limits_{i=1}^n P(E_i^f)u(x_i)\Big)$$

A concave $\Phi$ will overweigh low expected utilities, resulting in relatively ambiguity-averse preferences.

## 4. The Issue of Weak Order

### 4.1 Transitivity

While all models mentioned above impose transitivity on preferences, there is a long history of investigating possible violations of the principle, both with respect to choice under certainty and choice under risk. Regarding the latter, in a classic early study, Tversky (1969), suggested significant systematic violations of the transitivity of strict preference, which is entailed by that of weak preference, in relation to a series of lotteries $P_1$–$P_5$, each offering a chance $p_i$ of receiving a prize $x_i$ and a complementary chance of receiving nothing:

|   | $p_i$ | $x_i$ |
| --- | --- | --- |
| $P_1$ | $\nicefrac{7}{24}$ | $$5$ |
| $P_2$ | $\nicefrac{8}{24}$ | $$4.75$ |
| $P_3$ | $\nicefrac{9}{24}$ | $$4.5$ |
| $P_4$ | $\nicefrac{10}{24}$ | $$4.25$ |
| $P_5$ | $\nicefrac{11}{24}$ | $$4$ |

Tversky took his data to suggest that a significant number of subjects were prone to expressing strict preferences for each lottery over its immediate successor, but a strict preference for the last lottery over the first. He proposed that these subjects ranked adjacent lotteries by mere payoff as the differences in the probabilities of winning were barely perceptible, but took probability of winning into consideration in the comparison between $P_1$ and $P_5$, since the difference in values there was large. Although Tversky’s results were later replicated, it should be noted that there is ongoing controversy surrounding the level of empirical support for intransitive preference (see Regenwetter *et al.* 2011 for a recent literature review)[^regenwetter-2011].

Intransitivities of a somewhat different kind are also predicted by Loomes & Sugden’s (1982, 1987) *Regret Theory*.[^note-16] The guiding idea behind this proposal is that the appreciation of a given outcome in a given state is an essentially comparative matter. It is determined by the regret (or the rejoicement) associated with the thought that the alternatively available acts would have led, in the same circumstances, to a particular set of alternative outcomes. In the special case of binary alternatives, this intuition translates into the following *menu-dependent* preference functional:

$$\tag{8}\label{eqn:RT}U_{\{f,g\}}(f)=\sum\limits_{s\in\mathcal{S}} P\big(\{s\}\big) M\big(f(s), g(s)\big)$$

where $M: \mathcal{X}\times\mathcal{X}\mapsto \mathbb{R}$ is a comparative utility function that is increasing in its first argument and non-decreasing in its second. In their discussion of the framework, Loomes & Sugden present things equivalently as follows:

$$\tag{9} \label{eqn:RT'} f\succeq g\text{ iff } \sum\limits_{s\in\mathcal{S}} P\big(\{s\}\big) \Psi \big(f(s),g(s)\big) \geq 0$$

where $\Psi \big(f(s),g(s)\big)$ is defined as $M\big(f(s),g(s)\big)-M\big(g(s),f(s)\big)$. This quantity thus corresponds to the net balance of regret/rejoicement associated with choosing $f$ over $g$ in states $s$. Depending on the properties of $\Psi$, decision makers can be characterised as being ‘regret-neutral’, ‘regret-averse’ or even ‘regret-seeking’. Regret neutrality corresponds to the case in which, for all $x_1,x_2,x_3\in \mathcal{X}$,

$$\Psi(x_1, x_3)=\Psi(x_1, x_2)+\Psi(x_2, x_3).$$

Under these conditions, choice behaviour is consistent with SEU. Regret aversion corresponds to the situation in which $\Psi$ satisfies the following convexity requirement: for $x_1\succ x_2\succ x_3$,

$$\Psi(x_1, x_3)>\Psi(x_1, x_2)+\Psi(x_2, x_3).$$

Loomes & Sugden (1982) have shown that, at least under the assumption of probabilistic independence of the lotteries involved, this type of disposition can predict both the Common Consequence and the Common Ratio effects: Regret Theory does not entail Independence.[^note-17]

To obtain a sense of the violations of transitivity predicted by Regret Theory, here is an example due to Loomes & Sugden 1987. Assume convexity of $\Psi$ and consider the following decision problem, where $x_1\prec x_2\prec x_3$ and $P(A_i)=\nicefrac{1}{3}$:

|   | $A_1$ | $A_2$ | $A_3$ |
| --- | --- | --- | --- |
| $f$ | $x_1$ | $x_2$ | $x_3$ |
| $g$ | $x_3$ | $x_1$ | $x_2$ |
| $h$ | $x_2$ | $x_3$ | $x_1$ |

According to Regret Theory, $f\succ g$ iff

$$\Psi(x_1,x_3)+\Psi(x_2,x_1)+\Psi(x_3,x_2)>0.$$

Convexity of $\Psi$ will ensure that this inequality holds. By similar reasoning, it can then be established that $g\succ h$ and $h\succ f$.[^note-18]

The above example also clearly demonstrates that Regret Theory permits violations of State Neutrality, since the different acts yield the same probability distributions over outcomes. Loomes & Sugden (1987) further show that violations of Stochastic Dominance are licensed by their model. However, in spite of these departures from orthodoxy, it should be noted that Regret Theory retains a number of other strong consequences of SEU, including the Sure-Thing principle, as well as Betweenness for probabilistically independent distributions. An instructive axiomatisation of a generalisation of $(\ref{eqn:RT})$ to finite menus is offered in Sugden 1993. See Bleichrodt & Wakker 2015 for a clear overview of the framework, and its relation to the experimental data.

### 4.2 Completeness

Although the issue comes last in this catalogue of empirical challenges to SEU, early doubts regarding the empirical adequacy of the completeness assumption were aired by the very architects of the framework, including von Neumann & Morgenstern (1947: 630) and Savage (1954: 21). For instance, von Neumann & Morgenstern write:

> It is very dubious, whether the idealization of reality which treats this postulate as a valid one, is appropriate or even convenient.

Failure of completeness has been claimed to stem both from either (i) incompleteness in judgments of comparative probability or (ii) incompleteness in preferences between outcomes. Both sources of incompleteness can be handled in “*multi-prior expected multi utility*” models, which offer what one might call a “supervaluationist” representation of preferences over acts, as follows:

$$ f\succeq g \text{ iff, for all } \langle P, u\rangle\in \Phi, \sum\limits_{i=1}^n P(E_i^f)u(x_i)\geq \sum\limits_{i=1}^n P(E_i^g)u(x_i)$$

where $\Phi$ is a set of pairs of probability and utility functions. Due to space considerations, axiomatic details are left out here. The interested reader is referred to the recent general treatment given by Galaabaatar & Karni (2013), who relate their results to important earlier work by the likes of Bewley (1986), Seidenfeld *et al.* (1995), Ok *et al.* (2012), and Nau (2006), among others.

## 5. Descriptive vs Normative Decision Theory

While it was fairly immediately recognised that Allais had demonstrated an empirical shortcoming of SEU, it is important to note that his ambitions somewhat outstripped this achievement. He further suggested that his findings also give reason to doubt the *normative* adequacy of the theory. On his view, two types of consideration can be brought to the table in the assessment of a theory of rational choice. The first is a demonstration that the theory deductively follows from, or lies in logical conflict with, various general principles of secure epistemic standing. The second is a body of experimental evidence regarding

> the conduct of persons who, one has reason in other respects [(“that is on criteria that are free of all reference to any consideration of random choice.”)] to believe, act rationally. (Allais 1953b: 34)[^allais-1953b][^note-19]

However, he found no adequate evidence of the first kind that could be marshalled to support anything quite as strong as SEU. He rejected, for instance, Marschak’s (1951) “long-run success” argument for expected utility maximisation in situations of risk (Allais 1953b: 70–73)[^allais-1953b]. He did grant the existence of a “consistency” requirement according to which

> a man will be deemed to act rationally (a) if he pursues ends that are mutually consistent (i.e., not contradictory), (b) if he employs means that are appropriate to these ends. (Allais 1953b: 78)[^allais-1953b]

But, this requirement, he claimed, simply entailed that preferences over lotteries be weakly ordered and satisfy Stochastic Dominance. This left data on choice behaviour to adjudicate on the further commitments of SEU. This data, in his view, clearly supported the rational permissibility of violating Independence.

Savage did not explicitly discuss the probative force of the collective preferences of his peers in relation to Allais’ cases. He did however comment on the bearing of *his own* personal preferences, which Allais had famously elicited from him at a Paris symposium 1952 and which found themselves in violation of the recommendations of SEU . Granting that it would have been irrational for him to maintain both these preferences and a commitment to the normative adequacy of his axioms, he reported that further “reflection” inclined him to revise the former, judging these to have been in error, on par with a logical inconsistency in beliefs. This fact, he claimed, entitled him to retain his normative commitments (see Savage 1952: 101–103).[^note-20] Since it is easy to surmise that Savage took his own inclinations to be representative of those of the population at large, his comments have been widely taken to implicitly suggest an alternative experimental route to the testing of theories of rational choice. (See Slovic & Tversky 1974 and Jallais & Pradier 2005. This is also the view of Ellsberg, who offers, in Ch. 1 of his 1961 doctoral dissertation, reprinted as Ellsberg 2001, a worthwhile discussion of the issues of present interest, with Zappia 2016 providing a recent philosophically-oriented discussion.). This procedure would involve determining, not whether certain decision makers exhibit patterns of preference proscribed by the theory, but whether they still exhibit such patterns *after* reflection on their conflict with the theory’s basic axioms.

A number of studies set out to test the normative adequacy of SEU along the proposed lines. MacCrimmon (1968) reported violations, in a sample of experienced business executives, of a wide range of consequences of SEU, a number of which persisted after subjects were notably provided with considerations both supporting and undermining these principles. Those principles with respect to which offending preferences were later corrected included most notably Transitivity and Stochastic Dominance. Allais- or Ellsberg-style preferences were substantially more resilient, however, a fact confirmed in a later study by Slovic & Tversky (1974). Another type of resilience of preferences, not considered by Savage, was more recently investigated by van de Kuilen & Wakker (2006). They studied the effects of providing feedback on decision outcomes on the prevalence of common consequence effects in sequences of choices, finding, however, a significant reduction in SEU violations.

In spite of a long-standing tradition of bringing to bear theories of rational choice on various philosophical problems,[^note-21] the issue of the potential relevance of descriptive decision theory to its normative counterpart does not appear to have sparked much interest in the philosophical community. Allais’ challenge to Savage has largely been ignored in the philosophical literature.[^note-22]

Having said this, a fair amount of philosophical attention has been devoted to the related issue of the connection between norms of *reasoning* and observed patterns of *inference*. One influential line of thought to be found there, which seems pertinent to Allais’ claims, originates in Goodman’s discussion of the justification of inductive reasoning. On his view,

> [t]he task of formulating rules that define the difference between valid and invalid inductive inferences is much like the task of defining any term with an established usage. (Goodman 1965: 66)[^goodman-1965]

Just as semantic analyses can be endorsed on the basis of providing good systematisations of a set of intuitions regarding the applicability of particular terms in particular situations, Goodman claims, normative theories of reasoning can similarly be justified by their good fit with “the particular…inferences we actually make and sanction” (Goodman 1965: 63)[^goodman-1965]: no further considerations are required in order to be able to endorse a particular principle as rationally binding.

Goodman’s discussion is a brief one and, on our reading at least, leaves open a number of questions. Should we admit as relevant any considerations beyond observed patterns of inference, such as properties of long-run convergence to the truth, and so on? To whom does “we” refer to when Goodman speaks of “the particular…inferences we actually make and sanction”? Experts? The human population at large? Should we be circumscribing the class of relevant inferences to those judgments that one might want to call “considered”? These are important matters to settle. Indeed, a certain combination of answers to these—entailing that the justification of normative theories of reasoning hinges entirely on their ability to systematise “immediate and untutored” inferential dispositions observed in the general population—notoriously led Cohen (1981) to endorse the startling claim that, since normative and descriptive models are borne of the very same data set, behavioural evidence is in principle incapable of establishing human irrationality. For further discussion of this general topic, see for instance Stich (1990: Ch. 4), Stein (1996: Ch. 5), Stanovich (1999: Ch. 1), and Thagard (1982).[^note-23]

Although neither Allais nor Goodman draw the connection, a potential justification for the evidential relevance of experimental data in normative theory building can perhaps be sought in the literature on the Condorcet Jury Theorem and related results.[^note-24] This theorem tells us that, under certain conditions, the probability that a majority verdict, with regards to a particular matter, in a group of $n$ minimally reliable people casting yes/no votes on a particular question converges to 1 as $n$ tends to infinity, converging more quickly the greater the individual reliabilities. Furthermore, majority reliability reaches significant levels, even given very limited individual reliability, for fairly modest group sizes. Of course, the issue of interest does not quite fit that specific model: while the expression of Allais preferences can be arguably interpreted as a “vote” against the normative adequacy of Independence, the expression of preferences consonant with this principle can hardly be interpreted as a vote in favour of it.

Finally, while this section has focused on the issue of the bearing of descriptive decision theory on its normative counterpart, it should be noted that there has been some discussion of the converse direction of influence. Both Guala (2000) and Starmer (2005) have argued that the development of descriptive theories of choice has been guided by a bias towards retaining a core of principles taken to be normatively adequate. In the case of decision making under risk these are essentially the transitivity component of Weak Order and Stochastic Dominance, which are satisfied according to the vast majority of non-SEU theories that have been developed to date.[^note-25] Starmer claims to find an argument justifying this practise in a well-known paper by Friedman and Savage (1952). This line of thought, which Starmer takes issue with, proceeds from the assumption that bona fide principles of rationality would be evident as such to most subjects and that decision makers will accordingly behave in line with them.

## 6. Further Reading

While the philosophical literature on the topic remains rather sparse, there is no shortage of first-rate summaries in the economics and psychology literatures. For thorough presentations of the technical results referred to in Section 1, see Fishburn (1970: Ch. 14) or the slightly less detailed Kreps (1988: Ch. 9). Ch. 3 of Joyce (1999) is also helpful here. Regarding the literature on Independence specifically, discussed in Section 2, see Machina (1987), Starmer (2000) and Weber & Camerer (1987). Regarding the issue of probabilistic belief specifically, discussed in Section 3, see Camerer & Weber (1992), Etner *et al.* (2012), Gilboa & Marinacci (2013), Machina & Siniscalchi (2014), and Trautmann & van de Kuilen (2015).A number of broader surveys cover both the above issues, and some. These include most notably Camerer (1995) and the excellent Sugden (2004). Finally, for a clear and detailed historical account of the development of the experimental literature on decision-making, see Heukelom (2014).

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=decision-theory-descriptive). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/decision-theory-descriptive/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=decision-theory-descriptive&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](http://philpapers.org/sep/decision-theory-descriptive/) at [PhilPapers](http://philpapers.org/), with links to its database. |

## Other Internet Resources

- [Bibliography](https://personal.eur.nl/wakker/refs/webrfrncs.docx), Annotated, in Word, by Peter Wakker; a useful resources that starts with a list of keywords and abbreviations, but consists mostly of an annotated list of references with links to the paper when available.
- [Decision Theory Forum](https://groups.google.com/forum/#!forum/decision_theory_forum), on Google Groups; includes regular posts from leading decision theorists, including conference annoucements and the like.

## Related Entries

belief, formal representations of | decision theory | economics: philosophy of | preferences | probabilities, imprecise | rational choice, normative: expected utility

### Acknowledgments

I am extremely grateful to John Quiggin, Peter Wakker, Paul Weirich and Greg Wheeler for helpful comments on an earlier draft of this entry. Any remaining omissions, errors or inaccuracies remain, of course, my own responsibility.

## Notes（原文脚注）

[^note-1]: Disclaimer: The literature on the topic is absolutely vast, comprising thousands of papers spread across a number of academic disciplines. Accordingly, only an extremely selective glimpse at some of the relevant work can be provided. One particularly noteworthy omission is the issue of sequential, aka “dynamic”, choice, which would have required an entire further entry to present in a satisfactory manner. Space considerations have also precluded a discussion of a number of important empirical phenomena associated with choice behaviour, including so-called framing effects and preference reversals. For further details regarding these issues, as well as the points touched upon in this entry, the interested reader is referred to the excellent surveys listed below in Section 6.

[^note-2]: Each will consist in those points $(P(x_1), P(x_3))$ such that

$$u(x_1)P(x_1)+ u(x_2)(1-P(x_1)-P(x_3)) + u(x_3)P(x_3)$$

is equal to some constant expected utility value $c$. Rearranging this, one obtains the linear equation

$$P(x_3)= [u(x_2) - u(x_1)]/[u(x_3) - u(x_4)]P(x_1)+c-u(x_2),$$

the slope of the line being independent of $P(x_1)$ and $P(x_2)$.

[^note-3]: In what follows, the various methodological and statistical issues pertaining to the assessment of the models on offer have been glossed over. Hey (2014) provides a useful discussion, from this angle, of a number of important studies. Salient issues include the choice of methods of preference elicitation, the stochastic specification of the models, and a set of more fundamental problems connected with hypothesis testing and model selection.

[^note-4]: It is well known that Independence, a principle governing *single* choices, can be recovered from a number of conditions on temporal *sequences* of choices. Violations of the principle therefore immediately raise the question of where further to pin the blame. Due to space considerations, discussion of these issues has been omitted. The interested reader is referred to Section 4 of Sugden’s (2004) excellent survey article.

[^note-5]: This presentation of Allais’ paradoxes as respectively pertaining to the Common Consequence and Common Ratio principles is owed to Mongin (2009).

[^note-6]: Regarding the empirical adequacy of Stochastic Dominance, Tversky and Kahneman (1986) observe, perhaps not entirely surprisingly, significant violations of the principle when (but only when) the dominance relation is not immediately evident. It should be noted that a number of early Mixture-Independence-free models did not satisfy this requirement. These included most famously the weighted probability model of Handa (1977) and Kahneman & Tversky’s closely related *Prospect Theory* (1979), which essentially restricted the violations tolerated by Handa’s model to those cases that are “transparent”. Stochastic Dominance *is* however a feature of the successors of these proposals, discussed below.

[^note-7]: It should be noted that this general pattern of fanning out that must be imposed by WU to accommodate the local pattern of fanning out characteristic of Allais preferences lands the model in trouble elsewhere. Indeed further data has been collected that is consistent with an additional local pattern of *fanning in* towards the northwest of the triangle (see for instance Camerer 1989)[^camerer-1989]. Other Betweenness-satisfying models of probabilistically sophisticated preferences can better accommodate this data by allowing for *mixed fanning* patterns. These include Chew’s *Implicit Utility* (Chew 1989)[^chew-1989], which generalises WU, and Gul’s *Disappointment Aversion* (Gul 1991)[^gul-1991].

[^note-8]: Other models in this category include *Quadratic Utility* (Chew, Epstein, & Segal 1991)[^chew-1991] and *Lottery Dependent Utility* (Becker & Sarin 1987)[^becker-1987], which generalises WU.

[^note-9]: In note 7 above, it was pointed out that WU is unable to accommodate certain mixed fanning patterns suggested by the data. This is not the case with RDU, which shares in this respect the flexibility noted in relation with Implicit Utility and Disappointment Aversion.

[^note-10]: This formulation is due to Quiggin (1992).

[^note-11]: For more on this, see Sections 10.1 to 10.5 of Wakker (2010).

[^note-12]: It should be noted that Cumulative Prospect Theory can also be formulated as a sign-dependent generalisation of CEU. In this formulation, the functional form involves both a positive and a negative capacity. Wakker & Tversky (1993) offer an axiomatisation that notably restricts the Sure-Thing principle to sets of acts that are not only comonotonic but also *cosigned*, i.e., such that for all acts $f,g$ in that set, there exists no state $s$ such that $f(s)\succ 0$ but $g(s)\prec 0$, where $0$ designates the reference point.

[^note-13]: Gilboa & Schmeidler (1989) provided their initial axiomatic characterisation in a special case of the Savage setup, the Anscombe-Aumann (AA) framework (Anscombe & Aumann 1963)[^anscombe-1963], which has not been discussed in this entry. In this setting, additional structure is imposed on the set of outcomes, which are modeled as assignments of objective probabilities to the members of a set of further alternatives. Gilboa & Schmeidler’s axioms were more recently translated into the classic Savage model by Ghirardato *et al.* (2003), who also present a analogue of the AA-style axiomatisation of CEU due to Schmeidler (1989).

[^note-14]: It is not clear, however, what value of this parameter would correspond to ambiguity-neutrality. As Etner *et al.* (2012) note, the most likely candidate, the value $\nicefrac{1}{2}$, does not lead one to recover SEU, which is a plausible model for ambiguity neutral preferences.

[^note-15]: MEU subsumes Wald’s (1950) much earlier *Minimax* approach to decision making under *complete* suspension of judgment regarding objective probabilities (the approach is so called, because it involves minimisation of maximum loss). Wald’s model corresponds to the special case in which $\Gamma =\mathcal{P}$. $\alpha$-MEU subsumes Hurwicz’s (1951) *Generalized Bayes-Minimax* approach in the same manner. See Ch. 13 of Luce & Raiffa (1957) for an overview of these precursors and their axiomatic foundations.

[^note-16]: This proposal is equivalent, for pairwise choices, to Fishburn’s ()1989 *Skew-Symmetric Additive Utility theory*.

[^note-17]: As Loomes & Sugden (1987) later note, in the special case of preferences over independent distributions over three outcomes, Regret Theory yields indifference curves that are consistent with those generated by WU, given certain parameter values, fanning out from a point located in the southwestern quadrant, outside the probability triangle.

[^note-18]: Regret Theory proposes to replace SEU with a more general model that accommodates certain behaviours that can be plausibly interpreted as violating Transitivity or Independence. It is suggestive, however, of an alternative position which interprets these behaviours in a manner that renders them *consistent* with the standard model. This position involves “*fine-graining*” the description of the outcomes involved, so as to distinguish

- (a)two menu-*dependent* outcomes (e.g., its being the case that $x_1$ rather than $x_3$ versus its being the case that $x_1$ rather than $x_2$; denote these respectively by $\langle x_1, x_3\rangle$ and $\langle x_1, x_2\rangle$) with corresponding menu-*independent* utilities (e.g., $u(\langle x_1, x_3\rangle)$ versus $u(\langle x_1, x_2\rangle)$),

where Regret Theory only recognises

- (b)one menu-*independent* outcome (e.g., its being the case that $x_1$) with two menu-*dependent* utilities (e.g., $M(x_1, x_3)$ versus $M(x_1, x_2)$).

Note that the general strategy of fine-graining outcome descriptions to defuse apparent counterexamples to expected utility maximisation has been carried out with respect to a variety cases and in a variety of manners. For more on this, see Buchak (2013: Ch. 4) and works referenced therein, including Broome (1991), Weber (1998), and Weirich (1986).

[^note-19]: This kind of line of thinking, it appears, may have precedents in the decision theoretic literature. Jallais *et al.* (2008) claim that the appeal to “expert behaviour” was also pivotal in the emergence of SEU as a popular normative theory, finding such a reliance in both Bernouilli’s writings on the St Petersburg game and Condorcet’s critique thereof.

[^note-20]: Savage did not elaborate on the rationale underpinning this test, but one view prevalent among some of his contemporaries was that bona fide principles of rationality are self-evident. Morgenstern (1979: 180) provides a case in point, claiming that:

> [SEU] is normative in the sense that the theory is “absolutely convincing” which implies that men will act accordingly. If they deviate from the theory, an explanation of the theory and of their deviation will cause them to readjust their behavior

[^note-21]: For illustrations, see Section 4 of the entry titled normative theories of rational choice: expected utility.

[^note-22]: This is not to say, of course, that SEU is uncontroversial in philosophy. The completeness requirement has been a long-time suspect, in terms of normative, in addition to empirical, adequacy. Anand (2009) offers a rather critical review of the case for transitivity of rational preferences, as does Maher (1993: Ch. 2), who remains more optimistic. The normative adequacy of the assumption of probabilistic belief has also been under scrutiny for many years. It has been claimed for instance that probabilistic beliefs have insufficient structure (i) to be able to model a doxastic state that rationality requires to reflect not only the balance, but also what Keynes (1921) called the “weight”, of evidence (see, e.g., Joyce 2005)[^joyce-2005] or again (ii) to be able to model certain types of rationally permissible agnosticism, as suggested by van Fraassen’s “Water/Wine” problem (van Fraassen 1989)[^fraassen-1989]. See the entry titled imprecise probabilities for further various endorsements of multiple prior models in the philosophical literature, as well as the entry titled formal representations of belief. For cases in which probabilistic belief holds, in cases of decision making under risk, philosophical thinking has tended to take a more orthodox line. One notable recent exception here is Buchak (2013), who has defended the normative adequacy of RDU. See Chs. 5–7 of her book. Doubts regarding Independence are also voiced in an accessible handbook entry by McClennen (2009). See Maher (1993: Ch. 3) for a less pessimistic survey of the considerations.

[^note-23]: Unsurprisingly, analogous questions crop up in the recent experimental philosophy literature, in which it is suggested that empirical frequencies of intuitions regarding the applicability of a term may serve as defeasible evidence in favour of, or against, a particular theory of how the term ought to be applied. There, for instance, one also finds the recommendation that attention be focused on the judgments of the subset of the population that one would independently identify as “experts” (see, e.g., Hales 2006)[^hales-2006].

[^note-24]: The connection has however been noted in the experimental philosophy literature, by Sytsma & Livengood 2014 and Talbot 2014. See List & Pettit (2011: Ch. 4) for accessible presentation of the theorem, which is also discussed in the entry titled social choice theory.

[^note-25]: Though see Mongin (2009) for an alternative perspective on the development of alternatives to SEU.

[^allais-1953a]: Allais, Maurice, 1953a, “Le Comportement de l’Homme Rationnel devant le Risque: Critique des Postulats et Axiomes de l’Ecole Américaine”, *Econometrica*, 21(4): 503–546. doi:10.2307/1907921

[^allais-1953b]: –––, 1953b, “Fondements d’une Théorie Positive des Choix Comportant un Risque et Critique des Postulats et Axiomes de L’Ecole Américaine”, *Econométrie, Colloques Internationaux du CNRS*, XL: 257–332; page reference is to the translation titled “The Foundations of a Positive Theory of Choice Involving Risk and a Criticism of the Postulates and Axioms of the American School” in Allais & Hagen 1979: 27–145. doi:10.1007/978-94-015-7629-1_2

[^allais-1979]: Allais, Maurice and Ole Hagen (ed.), 1979, *Expected Utility Hypotheses and the Allais Paradox*, (Theory and Decision Library, 21), Dordrecht: Reidel. doi:10.1007/978-94-015-7629-1

[^anscombe-1963]: Anscombe, F.J., and R.J. Aumann, 1963, “A Definition of Subjective Probability”, *Annals of Mathematics and Statistics*, 34(1): 199–205. doi:10.1214/aoms/1177704255

[^anand-2009]: Anand, Paul, 2009, “Rationality and Intransitive Preference: Foundations for The Modern View”, in Anand, Pattanaik, & Puppe 2009: 156–172. doi:10.1093/acprof:oso/9780199290420.003.0007

[^anand-2009-2]: Anand, Paul, Prastanta K. Pattanaik, and Clemens Puppe (ed.), 2009, *The Handbook of Rational and Social Choice*, Oxford: Oxford University Press. doi:10.1093/acprof:oso/9780199290420.001.0001

[^becker-1964]: Becker, Selwyn W. and Fred O. Brownson, 1964, “What Price Ambiguity? Or the Role of Ambiguity in Decision-Making”, *Journal of Political Economy*, 72(1): 62–73. doi:10.1086/258854

[^becker-1987]: Becker, Joao L., and Rakesh K. Sarin, 1987, “Lottery Dependent Utility”, *Management Science*, 33(11): 1367–1382. doi:10.1287/mnsc.33.11.1367

[^bewley-1986]: Bewley, Truman F., 1986, “Knightian Decision Theory: Part I”, Cowles Foundation discussion paper no. 807. Reprinted with minor changes, 2002, *Decisions in Economics and Finance*, 25(2): 79–110. doi:10.1007/s102030200006

[^bleichrodt-2015]: Bleichrodt, Han and Peter P. Wakker, 2015, “Regret Theory: A Bold Alternative to the Alternatives”, *Economic Journal*, 125(583): 493–532. doi:10.1111/ecoj.12200

[^broome-1991]: Broome, John, 1991, *Weighing Goods: Equality, Uncertainty, and Time*, Oxford: Basil Blackwell.

[^buchak-2013]: Buchak, Lara, 2013, *Risk and Rationality*, Oxford: Oxford University Press. doi:10.1093/acprof:oso/9780199672165.001.0001

[^camerer-1989]: Camerer, Colin F., 1989, “An Experimental Test of Several Generalized Utility Theories”, *Journal of Risk and Uncertainty*, 2(1): 61–104. doi:10.1007/BF00055711

[^camerer-1995]: –––, 1995, “Individual Decision Making”, in John H. Kagel and Alvin E. Roth (ed.), *Handbook of Experimental Economics*, Princeton, NJ: Princeton University Press, pp. 587–703.

[^camerer-1994]: Camerer, Colin F. and Teck-Hua Ho, 1994, “Violations of the Betweenness Axiom and Nonlinearity in Probability”, *Journal of Risk and Uncertainty*, 8(2): 167–96. doi:10.1007/BF01065371

[^camerer-1992]: Camerer, Colin and Martin Weber, 1992, “Recent Developments in Modeling Preferences: Uncertainty and Ambiguity”, *Journal of Risk and Uncertainty*, 5(4): 325–370. doi:10.1007/BF00122575

[^chew-1983]: Chew Soo Hong, 1983, “A Generalization of the Quasilinear Mean with Applications to the Measurement of Income Inequality and Decision Theory Resolving the Allais Paradox”, *Econometrica*, 51(4): 1065–1092. doi:10.2307/1912052

[^chew-1989]: –––, 1989, “Axiomatic Utility Theories with the Betweenness Property”, *Annals of Operations Research*, 19(1): 273–298. doi:10.1007/BF02283525

[^chew-1991]: Chew Soo Hong, L.G. Epstein and U. Segal, 1991, “Mixture Symmetry and Quadratic Utility”, *Econometrica*, 59(1): 139–163. doi:10.2307/2938244

[^chew-1979]: Chew Soo Hong, and K. MacCrimmon, 1979, “Alpha-Nu Choice Theory: A Generalization of Expected Utility Theory”, Working Paper 669, University of British Columbia.

[^chew-1996]: Chew Soo Hong and Peter Wakker, 1996, “The Comonotonic Sure-Thing Principle”, *Journal of Risk and Uncertainty*, 12(1): 5–27. doi:10.1007/BF00353328

[^cohen-1981]: Cohen, L. Jonathan, 1981, “Can Human Irrationality be Experimentally Demonstrated?”, *Behavioral and Brain Sciences*, 4(3): 317–370. doi:10.1017/S0140525X00009092

[^finetti-1937]: de Finetti, Bruno, 1937, “La Prévision: Ses Lois Logiques, ses Sources Subjectives”, *Annales de l’Institut Henri Poincaré*, 7: 1–68.

[^ellsberg-1961]: Ellsberg, Daniel, 1961, “Risk, Ambiguity, and the Savage Axioms”, *Quarterly Journal of Economics*, 75(4): 643–669. doi:10.2307/1884324

[^ellsberg-2001]: –––, 2001, *Risk, Ambiguity, and Decision*, New York & London: Garland.

[^etner-2012]: Etner, Johanna, Megleria Jeleva, and Jean-Marc Tallon, 2012, “Decision Theory under Ambiguity”, *Journal of Economic Surveys*, 26(2): 234–270. doi:10.1111/j.1467-6419.2010.00641.x

[^fishburn-1970]: Fishburn, Peter C., 1970, *Utility Theory for Decision Making*, (Publications in Operations Research, No. 18), New York: John Wiley and Sons.

[^fishburn-1989]: –––, 1989, “Non-Transitive Measurable Utility for Decision under Uncertainty”, *Journal of Mathematical Economics*, 18(2): 187–207. doi:10.1016/0304-4068(89)90021-9

[^friedman-1952]: Friedman, Milton and L.J. Savage, 1952, “The Expected-Utility Hypothesis and the Measurability of Utility”, *Journal of Political Economy*, 60(6): 463–474. doi:10.1086/257308

[^galaabaatar-2013]: Galaabaatar, Tsogbadral and Edi Karni, 2013, “Subjective Expected Utility with Incomplete Preferences”, *Econometrica*, 81(1): 255–284. doi:10.3982/ECTA9621

[^ghirardato-2003]: Ghirardato, Paolo, Fabio Maccheroni, Massimo Marinacci, and Marciano Siniscalchi, 2003, “A Subjective Spin on Roulette Wheels”, *Econometrica*, 71(6): 1897–1908. doi:10.1111/1468-0262.00472

[^gilboa-1987]: Gilboa, Itzhak, 1987, “Expected Utility with Purely Subjective Non-Additive Probabilities”, *Journal of Mathematical Economics*, 16(1): 65–88. doi:10.1016/0304-4068(87)90022-X

[^gilboa-2013]: Gilboa, Itzhak and Massimo Marinacci, 2013, “Ambiguity and the Bayesian Paradigm”, in D. Acemoglu, M. Arellano, and E. Dekel (ed.), *Advances in Economics and Econometrics: Theory and Applications*, (Tenth World Congress of the Econometric Society), New York: Cambridge University Press.

[^gilboa-1989]: Gilboa, Itzhak and David Schmeidler, 1989, “Maxmin Expected Utility with a Non-Unique Prior”, *Journal of Mathematical Economics*, 18(2): 141–153. doi:10.1016/0304-4068(89)90018-9

[^goodman-1965]: Goodman, Nelson, 1965, *Fact, Fiction and Forecast*, second edition, Indianapolis, IN: Bobbs-Merrill.

[^grant-1995]: Grant, Simon, 1995, “Subjective Probability without Monotonicity: Or How Machina’s Mom May also Be Probabilistically Sophisticated”, *Econometrica*, 63(1): 159 189. doi:10.2307/2951701

[^green-1988]: Green, Jerry R. and Bruno Jullien, 1988, “Ordinal Independence in Nonlinear Utility Theory”, *Journal of Risk and Uncertainty*, 1(4): 355–387. doi:10.1007/BF00117641

[^guala-2000]: Guala, Francesco, 2000, “The Logic of Normative Falsification: Rationality and Experiments in Decision Theory”, *Journal of Economic Methodology*, 7(1): 59–93. doi:10.1080/135017800362248

[^gul-1991]: Gul, Faruk, 1991, “A Theory of Disappointment Aversion”, *Econometrica*, 59(3): 667–686. doi:10.2307/2938223

[^hales-2006]: Hales, Steven D., 2006, *Relativism and the Foundations of Philosophy*, Cambridge, MA: MIT Press.

[^handa-1977]: Handa, Jagdish, 1977, “Risk, Probabilities and a New Theory of Cardinal Utility”, *Journal of Political Economy*, 85(1): 97–122. doi:10.1086/260547

[^harless-1994]: Harless, David W. and Colin F. Camerer, 1994, “The Predictive Utility of Generalized Expected Utility Theories”, *Econometrica*, 62(6): 1251–1289. doi:10.2307/2951749

[^heukelom-2014]: Heukelom, Floris, 2014, *Behavioral Economics: A History*, Cambridge: Cambridge University Press. doi:10.1017/CBO9781139600224

[^hey-2014]: Hey, John Denis, 2014, “Choice Under Uncertainty: Empirical Methods and Experimental Results”, in Machina & Viscusi 2014: 809–850.

[^hurwicz-1951]: Hurwicz, Leonid, 1951, “Some Specification Problems and Applications to Econometric Models”, *Econometrica*, 19(3): 343–344.

[^jallais-2005]: Jallais, Sophie and Pierre-Charles Pradier, 2005, “The Allais Paradox and its Immediate Consequences for Expected Utility Theory”, in Philippe Fontaine and Robert Leonard (ed.) *The Experiment in the History of Economics*, London: Routledge, pp. 25–49.

[^jallais-2008]: Jallais, Sophie, Pierre-Charles Pradier, and David Teira, 2008, “Facts, Norms and Expected Utility Functions”, *History of the Human Sciences*, 21(2): 45–62. doi:10.1177/0952695108091414

[^joyce-1999]: Joyce, James M., 1999, *The Foundations of Causal Decision Theory*, Cambridge: Cambridge University Press. doi:10.1017/CBO9780511498497

[^joyce-2005]: –––, 2005, “How Probabilities Reflect Evidence”, *Philosophical Perspectives*, 19(1): 153–178. doi:10.1111/j.1520-8583.2005.00058.x

[^kahneman-1979]: Kahneman, Daniel and Amos Tversky, 1979, “Prospect Theory: An Analysis of Decision under Risk”, *Econometrica*, 47(2): 263–291. doi:10.2307/1914185

[^keynes-1921]: Keynes, John Maynard, 1921, *A Treatise on Probability*, London: Macmillan.

[^klibanoff-2005]: Klibanoff, Peter, Massimo Marinacci, and Sujoy Mukerji, 2005, “A Smooth Model of Decision Making Under Ambiguity”, *Econometrica*, 73(6): 1849–1892. doi:10.1111/j.1468-0262.2005.00640.x

[^kreps-1988]: Kreps, David M., 1988, *Notes on the Theory of Choice*, Boulder, CO: Westview Press.

[^list-2011]: List, Christian and Philip Pettit, 2011, *Group Agency: The Possibility, Design, and Status of Corporate Agents*, Oxford: Oxford University Press. doi:10.1093/acprof:oso/9780199591565.001.0001

[^loomes-1982]: Loomes, Graham and Robert Sugden, 1982, “Regret Theory: An Alternative Theory of Rational Choice under Uncertainty”, *Economic Journal*, 92(386): 805–824. doi:10.2307/2232669

[^loomes-1987]: –––, 1987, “Some implications of a More General Form of Regret Theory”, *Journal of Economic Theory*, 41(2): 270–287. doi:10.1016/0022-0531(87)90020-2

[^luce-1957]: Luce, R. Duncan and Howard Raiffa, 1957, *Games and Decisions: Introduction and Critical Survey*, New York: Wiley.

[^machina-1987]: Machina, Mark J., 1987, “Choice under Uncertainty: Problems Solved and Unsolved”, *Journal of Economic Perspectives*, 1(1): 121–154. doi:10.1257/jep.1.1.121

[^machina-1992]: Machina, Mark J. and David Schmeidler, 1992, “A more Robust Definition of Subjective Probability”, *Econometrica*, 60(4): 745–780. doi:10.2307/2951565

[^machina-2014]: Machina, Mark J., and Marciano Siniscalchi, 2014, “Ambiguity and Ambiguity Aversion”, in Machina & Viscus 2014i 2014: 729–807.

[^machina-2014-2]: Machina, Mark J. and Kip Viscusi (ed.), 2014, *Handbook of the Economics of Risk and Uncertainty*, Volume 1, Amsterdam: Elsevier.

[^maccrimmon-1968]: MacCrimmon, Kenneth R., 1968, “Descriptive and Normative Implications of the Decision-Theory Postulates”, in K. Borch and J. Mossin (ed.), *Risk and Uncertainty*, New York: St. Martins Press, pp. 3–32.

[^maccrimmon-1979]: MacCrimmon, Kenneth R. and Stig Larsson, 1979, “Utility Theory: Axioms versus ‘Paradoxes’”, in Allais & Hagen 1979: 333–409. doi:10.1007/978-94-015-7629-1_15

[^maher-1993]: Maher, Patrick, 1993, *Betting on Theories*, Cambridge: Cambridge University Press.

[^marschak-1951]: Marschak, Jacob, 1951, “Why ‘Should’ Statisticians and Businessmen Maximize ‘Moral Expectation’”, *Proceedings of the Second Berkeley Symposium on Mathematical Statistics and Probability*, Berkeley: University of California Press, pp. 493–506.

[^may-1954]: May, Kenneth O., 1954, “Intransitivity, Utility, and the Aggregation of Preference Patterns”, *Econometrica*, 22(1): 1–13. doi:10.2307/1909827

[^mcclennen-2009]: McClennen, Edward F., 2009, “The Normative Status of the Independence Principle”, in Anand, Pattanaik, & Puppe 2009: 140–155. doi:10.1093/acprof:oso/9780199290420.003.0006

[^mongin-2009]: Mongin, Philippe, 2009, “Duhemian Themes in Expected Utility Theory”, Anastasios Brenner & Jean Gayon (eds), *French Studies In The Philosophy Of Science*, (Boston Studies In The Philosophy Of Science, 276), Springer, pp. 303–357. doi:10.1007/978-1-4020-9368-5_13

[^mongin-2014]: –––, 2014, “Le Paradoxe d’Allais. Comment Lui Rendre sa Signification Perdue?”, *Revue Économique*, 65(5): 743–779.

[^morgenstern-1979]: Morgenstern, Oskar, 1979, “Some Reflections on Utility”, in Allais & Hagen 1979: 175–184. doi:10.1007/978-94-015-7629-1_6

[^nau-2006]: Nau, Robert, 2006, “The Shape of Incomplete Preferences”, *Annals of Statistics*, 34: 2430–2448. doi:10.1214/009053606000000740

[^ok-2012]: Ok, Efe A., Pietro Ortoleva, and Gil Riella, 2012, “Incomplete Preferences under Uncertainty: Indecisiveness in Beliefs versus Tastes”, *Econometrica*, 80(4): 1791–1808. doi:10.3982/ECTA8040

[^quiggin-1982]: Quiggin, John, 1982, “A Theory of Anticipated Utility”, *Journal of Economic Behavior and Organization*, 3(4): 323–343. doi:10.1016/0167-2681(82)90008-7

[^quiggin-1992]: –––, 1992, *Generalized Expected Utility Theory: The Rank Dependent Model*, Dordrecht: Kluwer.

[^ramsey-1931]: Ramsey, Frank P., 1931, “Truth and Probability”, in R.B. Braithwaite (ed.) *The Foundations of Mathematics and other Logical Essays*, New York: Harcourt and Brace, pp. 156–198.

[^regenwetter-2011]: Regenwetter, Michel, Jason Dana, and Clinton P. Davis-Stober, 2011, “Transitivity of Preferences”, *Psychological Review*, 118(1): 42–56. doi:10.1037/a0021150

[^savage-1954]: Savage, Leonard J., 1954, *The Foundations of Statistics*, New York: Wiley, Second Edition.

[^schmeidler-1986]: Schmeidler, David, 1986, “Integral Representation without Additivity”, *Proceedings of the American Mathematical Society*, 97(2): 255–261.

[^schmeidler-1989]: –––, 1989, “Subjective Probability and Expected Utility without Additivity”, *Econometrica*, 57(3): 571–587. doi:10.2307/1911053

[^seidenfeld-1995]: Seidenfeld, Teddy, Mark J. Schervish, and Joseph B. Kadane, 1995, “A Representation of Partially Ordered Preferences”, *Annals of Statistics*, 23(6): 2168–2217. doi:10.1214/aos/1034713653

[^slovic-1974]: Slovic, Paul and Amos Tversky, 1974, “Who Accepts Savage’s Axiom?”, *Systems Research and Behavioral Science*, 19(6): 368–373. doi:10.1002/bs.3830190603

[^stanovich-1999]: Stanovich, Keith E., 1999, *Who Is Rational? Studies of Individual Differences in Reasoning*, Mahwah, NJ: Lawrence Erlbaum Associates.

[^starmer-2000]: Starmer, Chris, 2000, “Developments in Non-Expected Utility Theory: The Hunt for a Descriptive Theory of Choice under Risk”, *Journal of Economic Literature*, 38(2): 332–382. doi:10.1257/jel.38.2.332

[^starmer-2005]: –––, 2005, “Normative Notions in Descriptive Dialogues”, *Journal of Economic Methodology*, 12(2): 277–289. doi:10.1080/13501780500086206

[^stein-1996]: Stein, Edward, 1996, *Without Good Reason: The Rationality Debate in Philosophy and Cognitive Science*, Oxford: Clarendon Press.

[^stich-1990]: Stich, Stephen P., 1990, *The Fragmentation of Reason*, Cambridge, MA: MIT Press.

[^sugden-1993]: Sugden, Robert, 1993, “An Axiomatic Foundation For Regret Theory”, *Journal of Economic Theory*, 60(1): 159–180. doi:10.1006/jeth.1993.1039

[^sugden-2004]: –––, 2004, “Alternatives to Expected Utility: Foundations”, in Salvador Barberà, Peter J. Hammond, and Christian Seidl (ed.), *Handbook of Utility Theory: Volume 2 Extensions*, Boston, MA: Springer, pp. 685–755.

[^sytsma-2014]: Sytsma, Justin and Jonathan Livengood, 2014, *The Theory and Practice of Experimental Philosophy*, Peterborough, ON: Broadview Press.

[^talbot-2014]: Talbot, Brian, 2014, “Why so Negative? Evidence Aggregation and Armchair Philosophy”, *Synthèse*, 191(16): 3865–3896. doi:10.1007/s11229-014-0509-z

[^thagard-1982]: Thagard, Paul, 1982, “From the Descriptive to the Normative in Psychology and Logic”, *Philosophy of Science*, 49(1): 24–42. doi:10.1086/289032

[^trautmann-2015]: Trautmann, Stefan T., and Gijs van de Kuilen, 2015, “Ambiguity Attitudes”, in Gideon Keren & George Wu (ed.), *The Wiley Blackwell Handbook of Judgment and Decision Making*, Oxford: Blackwell, 89–116.

[^tversky-1969]: Tversky, Amos, 1969, “Intransitivity of Preferences”, *Psychological Review*, 76(1): 31–48. doi:10.1037/h0026750

[^tversky-1986]: Tversky, Amos and Daniel Kahneman, 1986, “Rational Choice and the Framing of Decisions”, *The Journal of Business*, 59(4): 251–278.

[^tversky-1992]: –––, 1992, “Advances in Prospect Theory: Cumulative Representation of Uncertainty”, *Journal of Risk and Uncertainty*, 5(4): 297–323. doi:10.1007/BF00122574

[^kuilen-2006]: van de Kuilen, Gijs and Peter P. Wakker, 2006, “Learning in the Allais Paradox”, *Journal of Risk and Uncertainty*, 33(3): 155–164. doi:10.1007/s11166-006-0390-3

[^fraassen-1989]: van Fraassen, Bas C., 1989, *Laws and Symmetry*, Oxford: Oxford University Press. doi:10.1093/0198248601.001.0001

[^neumann-1947]: von Neumann, John and Oskar Morgenstern, 1947, *Theory of Games and Economic Behavior*, second edition, Princeton: Princeton University Press.

[^wald-1950]: Wald, Abraham, 1950, *Statistical Decision Functions*. New York: John Wiley and Sons.

[^wakker-1989]: Wakker, Peter P., 1989, “Continuous Subjective Expected Utility with Nonadditive Probabilities”, *Journal of Mathematical Economics*, 18(1): 1–27. doi:10.1016/0304-4068(89)90002-5

[^wakker-2010]: –––, 2010, *Prospect Theory: For Risk and Ambiguity*, Cambridge: Cambridge University Press.

[^wakker-1993]: Wakker, Peter P. and Amos Tversky, 1993, “An Axiomatization of Cumulative Prospect Theory”, *Journal of Risk and Uncertainty*, 7(2): 147–175. doi:10.1007/BF01065812

[^weber-1998]: Weber, Michael, 1998, “The Resilience of the Allais Paradox”, *Ethics*, 109(1): 94–118. doi:10.1086/233875

[^weber-1987]: Weber, Michael and Colin F. Camerer, 1987, “Recent Developments in Modelling Preferences under Risk”, *OR Spektrum*, 9(3): 129–151. doi:10.1007/BF01721094

[^weirich-1986]: Weirich, Paul, 1986, “Expected Utility and Risk”, *British Journal for the Philosophy of Science*, 37(4): 419–442. doi:10.1093/bjps/37.4.419

[^zappia-2016]: Zappia, Carlo, 2016, “Daniel Ellsberg and the Validation of Normative Propositions”, *Oeconomia*, 6(1): 57–79. doi:10.4000/oeconomia.2276
