# imprecise-probabilities — supplement-historical（supplement）

> （《imprecise-probabilities》词条补充材料，源：plato.stanford.edu/entries/imprecise-probabilities/supplement-historical.html）

#### Supplement to Imprecise Probabilities

## Historical appendix: Theories of imprecise belief

In this section we review some authors who held views that were or can be interpreted as IP friendly. This list is not exhaustive: these authors are those who have been influential or who had particularly interesting theories. These sections offer mere sketches of the often rich and interesting theories that have been put forward.

- 1. J.M. Keynes
- 2. I.J. Good
- 3. Isaac Levi
- 4. Henry Kyburg
- 5. The SIPTA community
- 6. Richard Jeffrey
- 7. Arthur Dempster and Glenn Shafer
- 8. Peter Gärdenfors and Nils-Eric Sahlin

### 1. J.M. Keynes

In his *Treatise on Probability* Keynes argued that “probabilities” needn’t always be amenable to numerical comparisons (Keynes 1921). He said:

> [N]o exercise of the practical judgment is possible, by which a numerical value can actually be given to the probability of every argument. So far from our being able to measure them, it is not even clear that we are always able to place them in an order of magnitude. Nor has any theoretical rule for their evaluation ever been suggested. The doubt, in view of these facts, whether any two probabilities are in every case even theoretically capable of comparison in terms of numbers, has not, however, received serious consideration. There seems to me to be exceedingly strong reasons for entertaining the doubt. (Keynes 1921: 29)

> I maintain … that there are some pairs of probabilities between the members of which *no* comparison of magnitude is possible; that we can say, nevertheless, of some pairs of relations of probability that the one is greater and the other less, although it is not possible to measure the difference between them; and that in a very special type of case … a meaning can be given to a *numerical* comparison of magnitude. (Keynes 1921: 36, Keynes’ emphasis)

Keynes’ *Theory of Probability* contains the diagram reproduced in Figure H1, and it’s clear from this that he thought there could be degrees of belief that were not numerically comparable. Keynes interprets the *O* and *I* as the contradiction and tautology respectively and *A* is a proposition with a numerically measurable probability. The lines connect those propositions (denoted by letters) that can be compared. So *V* and *W* can be compared and *W* is more likely that *V* (since it is closer to *I*). Those propositions without lines between them (for example *X* and *Y*) are incomparable. Keynes’ own discussion of the diagram is on page 42 of Keynes (1921).

![[A line with endpoints 'O' and 'I' and a point about two-thirds of the way from 'O' to 'I' labeled 'A'. A wide curve above the line goes from 'O' to 'I' with a point partway labeled 'U'. A second curve below the first also goes from 'O' to 'I' and has points 'V', 'W', and 'X' marked on it. A third curve initial starts between the first and second curves at 'O' but intersects the second curve at 'W' and goes below before ending also at 'I'; a point 'Z' is marked on the first part of this curve and a point 'X' on the second part. A last curve connects points 'V' on the second curve and point 'A' on the line.]](../assets/imprecise-probabilities/keynes.png)

\*Figure H1:\* Keynes’ view of probability

Weatherson (2002) interprets Keynes as favouring some sort of IP view since sets of functions (or intervals of values) naturally give rise to the sorts of incomparabilities that Keynes takes to be features of belief. Keynes took (conditional) probability to be a sort of logical relationship that held between propositions (Hájek 2011: 3.2), rather than as strength of belief. So whether Keynes would have approved of IP models is unclear. See Kyburg (2003) for a discussion of Keynes’ view by someone sympathetic to IP, and see Brady and Arthmar (2012) for further discussion of Kaynes’ view.

### 2. I.J. Good

I.J. Good, mathematician, statistician, student of G.H. Hardy and Bletchley Park code-breaker, was an early advocate of something like IP.

> In principle these [probability] axioms should be used in conjunction with inequality judgements and therefore only lead to inequality discernments… Most subjective probabilities are regarded as belonging only to some interval of values. (Good 1983 [1971]: 15)

Good is usually associated with the “black box model of belief”. The idea here is that at the core of your epistemic state is a “black box” which you cannot look inside. The black box outputs “discernments”: qualitative probability judgements like “$X$ is more likely than $Y$”. The idea is that inside the black box there is a numerical and precise probability function that you only have indirect and imperfect access to (Good 1962).

It isn’t wholly clear from Good’s writings on this topic whether the precise probability in the black box is supposed to be a genuine part of an agent’s epistemic state or whether talk of the precise black box probability is just a calculational device. Good is often interpreted as being in the former camp (by Levi for example), but the following quote suggests he might have been in the latter camp:

> It is often convenient to forget about the inequality for the sake of simplicity and to simply use precise estimates. (Good 1983 [1971]: 16)

The way Good talks in his (1962)—especially around page 77—also suggests that Good’s view isn’t quite the “black box” interpretation that is attributed to him. In any case, Good is certainly interpreted as holding the view that IP is required since belief is only imperfectly available to introspection.

### 3. Isaac Levi

Isaac Levi has been a prominent defender of a particular brand of IP since the seventies (Levi 1974, 1980, 1985, 1986). Levi’s brand of IP is developed carefully and thoroughly over the course of several books and articles, the most important being *The Enterprise of Knowledge* (Levi 1980) and *Hard Choices* (Levi 1986). Levi has several motivations for being dissatisfied with the precise probabilistic orthodoxy. One of Levi’s motivations for IP is captured by the following quote:

> [I]t is sometimes rational to make no determinate probability judgement and, indeed, to make maximally indeterminate judgements. Here I am supposing … that refusal to make a determinate probability judgement does not derive from a lack of clarity about one’s credal state. To the contrary, it may derive from a very clear and cool judgement that on the basis of the available evidence, making a numerically determinate judgement would be unwarranted and arbitrary. (Levi 1985: 396)

Another motivation for Levi’s brand of IP is connected to his general picture of the structure of an agent’s mental state at a time. Levi’s view is that your belief state at a time can be captured by two components. The first component is your *Corpus of Knowledge*, $K$, which “encodes the set of sentences … to whose certain truth [you are] committed” (Levi 1974: 395). $K$ is a deductively closed set of sentences. In any model of partial belief and uncertain inference, there are some things about which you are uncertain. But in every case there are some things that are taken for granted. Imagine a toy example of drawing marbles from an urn. The observed frequencies of colours is used as evidence to infer something about the frequencies of colours in the urn. In this model, you take for granted that you are accurately recognising the colours and are not being deceived by an evil demon or anything like that (or, more prosaically, that the draws are probabilistically independent of each other and each draw has the same probabilities associated with it, i.e. that the draws are independent and identically distributed, i.i.d.). That’s not to say that we couldn’t model a situation where there was some doubt about the observations: the point is that in the simple case, that sort of funny business is just ruled out. “No funny business” is in $K$, if you like. There are certain aspects of the situation that are taken for granted: that are outside the modelling process. This is the same in science: when we model the load stress of a particular design of bridge, we take for granted the basic physics of rigid bodies and the facts about the materials involved.

The second part of Levi’s view of your belief state is captured by your *confirmational commitments* which describe how you are disposed to change your belief in response to certain kinds of evidence. $C$ is a function that takes your corpus $K$ as input and outputs “your beliefs”: some object that informs your decision making behaviour and constrains how your attitudes change in response to evidence. Levi argues in favour of this bipartite epistemology as follows:

> One of the advantages of introducing confirmational commitments is that confirmational commitments and states of full belief can vary independently without incoherence… [T]he separability of confirmational commitment and state of full belief is important to the study of conditions under which changes in credal state are justified. If this separability is ignored and attention is focused on changes in credal state directly, the distinction between changes in credal state that are changes in confirmational commitment and changes in full belief is suppressed without argument. (Levi 1999: 515)

Levi sees precise Bayesianism as suppressing this distinction. The only way a Bayesian agent updates is through conditionalisation. Levi has more to say on the subject of the defects of Bayesianism, but we don’t have room to discuss his criticisms.

For Levi, the output of $C(K)$ is a set of probability functions, $P$, with the following properties:

- $P$ is non-empty.
- $P$ is convex, meaning if $p,q\in P$ then for $0 \ge \lambda\ge 1$, $\lambda p + (1-\lambda) q \in P$.
- If you learn $E$ with certainty and nothing else, then $C(K+E) = Q$ where $Q = \{p(\cdot \mid E)\}$.

The first and third of these properties shouldn’t strike anyone as particularly surprising or unusual. The second, however, needs further comment. Recall that Levi thought that sets of probabilities were useful as a way of representing conflict. If you are conflicted between $p$ and $q$ (represented by both being in your representor) then any convex combination of $p$ and $q$ will:

> have all the earmarks of potential resolutions of the conflict; and, given the assumption that one should not preclude potential resolutions when suspending judgement between rival systems… all weighted averages of the two [probability] functions are thus taken into account. (Levi 1980: 192).

Levi’s reasons for taking linear averages of precise credal states (and only linear averages) to be particularly pertinent as resolutions of conflict aren’t particularly clearly spelled out. Levi does appeal to a theorem from Blackwell and Girschick (1954) and to Harsanyi’s theorem (Harsanyi 1955) as reasons to think that conflicts in values (utility functions) should be resolved through linear averaging (Levi 1980: 175; Levi 1986: 78). The premises of these arguments are not particularly discussed or justified in Levi’s set up. The argument for *credal convexity* is less clear, but see (Levi 1980: chap. 9). A further puzzle for Levi’s view is that these potential resolutions of conflict might not respect probabilistic independencies that $p$ and $q$ agree on (see section 2.7)

### 4. Henry Kyburg

Henry Kyburg’s view on rational belief bears some similarities to Levi’s (both were students of Ernest Nagel). Both take there to be some corpus of knowledge $K$—Kyburg’s term is *Evidential Corpus*—which is part of what determines your credal state. However, Kyburg’s *Evidential Probabilities* are quite different to Levi’s picture of rational belief.

Kyburg’s $K$ is a collection of sentences of a logical language that includes the expressive resources to say things like “the proportion of $F$s that are $G$s is between $l$ and $u$”. Such evidential corpora are indexed by a significance level at which the claims in the corpus are valid. Levi doesn’t say a great deal about how the confirmational commitment $C$ constrains your credal state except to say that if $X$ is a sentence in $K$ then if $p \in C(K)$ then $p(X)=1$. Kyburg has a lot more to say about this step. He develops a set of rules for dealing with conflicts of information in the corpus.

Evidential probabilities are a kind of “interval-valued” probability together with a thorough theory for inferring them from statistical data, and for logically reasoning about them. The intervals aren’t necessarily interpretable as sets of probability functions: that is, they can violate some of the properties of credal sets discussed in the formal appendix. The theory is most fully set out in Kyburg and Teng (2001) (see also, Wheeler and Williamson (2011); Haenni et al. (2011)). The theory is discussed more with an eye to the concerns of psychologists and experimental economists in Kyburg (1983).

### 5. The SIPTA community

Drawing on the work of Bruno de Finetti, C.A.B. Smith and Peter Williams, there is a rich tradition of IP research that culminates in the body of work developed by those associated with SIPTA: the Society for Imprecise Probability, Theory and Applications ([http://www.sipta.org/](http://www.sipta.org/)). SIPTA only came into being in 2002, and the ISIPTA conferences have only been running since 1999, but one can trace a common thread of research back much further. Among the important works contributing to this tradition are: Fine (1973), Suppes (1974), Williams (1976), Walley and Fine (1982), Kyburg (1987), Seidenfeld (1988), Walley (1991), Kadane, Schervish, and Seidenfeld (1999), de Cooman and Miranda (2007), Troffaes and de Cooman (2014) and Augustin et al. (2014). One main strand of work in this tradition is outlined in the [formal appendix](imprecise-probabilities.supplement-formal.md). See Miranda (2008) for a recent survey of some work in this tradition, and Augustin et al. (2014) for a book length introduction. A recent comment on the history of imprecise probabilities can be found in Vicig and Seidenfeld (2012). Work in what I am calling the “SIPTA tradition” isn’t just focussed on IP as a model of rational belief, but on IP as a useful tool in statistics and other disciplines as well: IP as a model of some non-deterministic process, IP as a tool for classification of data…

The popularity of the term “Imprecise Probability” for the class of models we are interested in is due, in large part, to the influence of Peter Walley’s 1991 book *Statistical Reasoning with Imprecise Probabilities*. This book was, until very recently, the most complete description of the theory of imprecise probabilities. Walley brought together and extended the above mentioned results and produced a rich and deep theory of statistics on the basis of IP. Despite being mainly devoted to the exposition of the formal machinery of IP, Walley’s book contains a lot of interesting material on the philosophical foundations of IP. In particular, sections 1.3–1.7, the sections on the interpretation of IP (2.10, 2.11), and chapter 5 all contain interesting philosophical discussion that in many ways anticipates recent philosophical debates on IP. It wouldn’t be uncharitable to describe a lot of recent philosophical work on IP as footnotes to Walley (although referencing Walley in a footnote appears to be as close as some authors get to actually engaging with him). Engagement by philosophers with this community has sadly been rather limited, excepting Levi, Kyburg and their students. This is unfortunate since many philosophically rich topics emerge in the course of this sort of research, for example, the many distinct independence concepts for IP (Kyburg and Pittarelli 1992; Cozman and Walley 2005; Cozman 2012), the rational requirements on group belief (Seidenfeld, Kadane, and Schervish 1989) or the distinction between symmetries in the model and models constrained to satisfy certain symmetries (de Cooman and Miranda 2007).

### 6. Richard Jeffrey

Richard Jeffrey is sometimes taken to be someone whose views are consonant with the IP tradition. In reality, Jeffrey’s view is a little more complicated. In *The Logic of Decision* (Jeffrey 1983), Jeffrey develops a representation theorem based on mathematical work by Ethan Bolker that uses premises that are interestingly weaker than those of Savage’s classic theorem (Savage 1972 [1954]). Agents still have complete and transitive preferences, but they have those preferences over a space where the “belief” and “value” parts aren’t straightforwardly separable. In Savage’s theorem, in contrast, the “states” and “outcomes” are distinct spaces. The representation that arises in Jeffrey’s framework is not unique, in the following sense. If $(p,v)$ is a probability-utility representation of the preference relation, then there exists a *λ* such that $(p',v')$ also represents the preference, where $p'$ and $v'$ are defined as:

$$\begin{align} p'(X) &= p(X)[1-\lambda v(X)] \\ v'(X) &= v(X)[(1+\lambda)/(1+\lambda v(X))] \end{align}$$

Indeed, there will be infinitely many such representations (Jeffrey 1983: chap. 8; Joyce 1999: 133–5). Jeffrey argued that an epistemology built on such a representation theorem gives

> one clear version of Bayesianism in which belief states… are naturally identified with infinite sets of probability functions, so that degrees of belief in particular propositions will normally be determined only up to an appropriate quantization, i.e., they will be interval-valued (so to speak). (Jeffrey 1984)

Jeffrey claims that his theory subsumes Levi’s theory. Levi (1985) responds that his theory and Jeffrey’s are importantly distinct, and Jeffrey (1987) recants.

This aspect of Jeffrey’s work—the Jeffrey-Bolker representation theorem—cannot be taken as a basis for imprecise probabilities in the sense we are considering. Jeffrey notes this point:

> [T]he indeterminacy of [$p$] and [$v$] that is implied by Bolker’s uniqueness theorem takes place within a context of total determinacy about preference and indifference. Thus it has nothing to do with the decision-theoretical questions that Levi addresses. (Jeffrey 1987: 590)

The indeterminacy of the belief in this setting is due to the inseparability of the beliefs and the values (as captured by the above mentioned alternative representations). However, Jeffrey also takes a line that is more IP-friendly. He says:

> I do not take belief states to be determined by full preference rankings of rich Boolean algebras of propositions, for our actual preference rankings are fragmentary… [E]ven if my theory were like Savage’s in that full rankings of whole algebras always determine unique probability functions, the actual partial rankings that characterize real people would determine belief states that are infinite sets of probability functions on the full algebras. (Jeffrey 1984: 139)

Jeffrey’s main concern in his 1984 paper is with scientific reasoning, and with a solution to the Problem of Old Evidence originally introduced by Glymour (1980). However, with respect to decision theory, he seems much less certain of the role of IP. In places, Jeffrey seems to agree with Levi:

> Where the agent’s attitudes are characterized by a set of $[(p,v)]$ pairs, some of which give one ranking of the options and some another, I see decision theory as silent… I don’t think that to count as rational you always have to have definite preferences or indifferences, any more than you always have to have precise probabilistic judgments. Nor does Levi. (Jeffrey 1987: 589)

Jeffrey here seems to be suggesting that IP is at least permissible. However, he ends up thinking that applying the principle of indifference (in some form) is a legitimate way to “sharpen up” your beliefs and values (and thus your preferences). After likening his position to Kaplan’s—see section 2.2—Jeffrey says:

> I differ from Kaplan, who would see my adoption of the uniform distribution as unjustifiable precision, whereas I think I would adopt it as a precise characterization of my uncertainty. Having more hopes for locally definite judgmental probabilities than Levi does, I am less dedicated to judgmental sets [of probabilities] as characterizations of uncertainty… I attribute less psychological immediacy than Levi does to sets of judgemental probability functions; and in decision theory, where he assigns them a central systematic role, I use them peripherally and *ad hoc*. (1987: 589)

In summary then, Jeffrey sides with Levi with respect to epistemology—modulo the emphasis on permissibility rather than obligation—but has a more orthodox view of decision theory. So care must be taken when appealing to Jeffrey as an advocate of IP. Richard Bradley (2017) develops an IP-friendly version of decision theory that is clearly inspired by the work of Richard Jeffrey.

### 7. Arthur Dempster and Glenn Shafer

Dempster–Shafer belief theory builds a theory of rational belief on an infinite monotone capacity $bel$ and its conjugate $plaus(X) = 1-bel(\neg X)$ (see the [formal appendix](imprecise-probabilities.supplement-formal.md)). $bel(X)$ is interpreted as the degree to which your evidence supports $X$. The interesting aspect of DS theory is its method for *combining* different bodies of evidence. So if $bel_1$ represents the degree to which a certain body of evidence supports various hypotheses and $bel_2$ captures the degree of support of another body of evidence, then DS theory gives you a method for working out the degree to which the combination of the evidence supports hypotheses. This is a distinct process from conditionalisation which also has an analogue in DS theory (see Kyburg 1987 for discussion of the difference). In any case, DS theory can be, in a sense, subsumed within the credal sets approach, since every DS belief function is the lower envelope of some set of probabilities (Theorem 2.4.1 on p.34 of Halpern 2003). Discussing the details would take us too far afield, so I point the interested reader to the following references: (Halpern 2003: 32–40, 92–5; Kyburg and Teng 2001: 104–12; Haenni 2009: 132–47; Huber 2014: section 3.1).

### 8. Peter Gärdenfors and Nils-Eric Sahlin

Gärdenfors and Sahlin (1982) introduce a theory that they term *Unreliable Probabilities* (the theory builds on Gärdenfors 1979). It bears some resemblance to Kyburg’s theory—they in fact discuss Kyburg—but it is a theory built with decision making in mind. The basic idea is that you have a set of probabilities and attached to each probability function is an indicator of its reliability. Depending on the circumstances, you pick some reliability threshold *ρ* and restrict your attention to the set of probabilities that are at least as reliable as that threshold. They then have a story about how decision making should go with this set. Note that they don’t really need a *measure* of reliability, all they need is something to *order* the probabilities in $P$. The threshold then becomes some cut-off probability: anything less reliable than it doesn’t make the cut.

Gärdenfors and Sahlin (1982) don’t really discuss this measure of reliability a great deal. Presumably reliability increases as evidence comes in that supports that probability function. Gärdenfors and Sahlin offer an example to illustrate how reliability is supposed to work. They consider three tennis matches. In match $A$, you know that the two tennis players are of roughly the same level and that it will be a tight match. In match $B$, you have never even heard of either player and so cannot judge whether or not they are well matched. In match $C$ you have heard that the players are really unevenly matched: one player is much better than the other, but you do not know which of the players is significantly better. If we graphed reliability of a probability against how likely that probability thinks it is that the player serving first will win, the graphs would be as follows: graph $A$ would be very sharply peaked about $0.5$; graph $B$ would be quite spread out; graph $C$ would be a sort of “U” shape with high reliability at both ends, lower in the middle. See Figure H2. Graph $A$ is peaked because you know that the match will be close. You have reliable information that the player serving has about a 50% chance of winning. Graph $B$ is spread out because you have no such information in this case. In case $C$, you know that the probability functions that put the chances at near 50-50 are unreliable: all you know is that the match will be one-sided.

![[three graphs each showing just the first quadrant. The first labeled 'A' has a dotted line depicting a bell curve, the second labeled 'B' has a dotted straight horizontal line, and the third labeled 'C' has an upside down bell curve.]](../assets/imprecise-probabilities/unreliable-graphs.png)

\*Figure H2:\* Graphs of reliability against probability server wins point

In summary, the unreliable probabilities approach enriches a credal set with a *reliability index*. See Levi (1982) for a critical discussion of unreliable probabilities. Cattaneo (2008) gives some content to the reliability index of a probability by interpreting it in terms of the likelihood of the evidence given by that probability. Another formal theory that seems inspired by the reliability approach is that of Brian Hill (2013).
