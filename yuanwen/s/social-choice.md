# Social Choice Theory
**First published Wed Dec 18, 2013; substantive revision Fri Oct 14, 2022**

*List, Christian*

Social choice theory is the study of collective decision procedures and mechanisms. It is not a single theory, but a cluster of models and results concerning the aggregation of individual inputs (e.g., votes, preferences, judgments, welfare) into collective outputs (e.g., collective decisions, preferences, judgments, welfare). Central questions are: How can a group of individuals choose a winning outcome (e.g., policy, electoral candidate) from a given set of options? What are the properties of different voting systems? When is a voting system democratic? How can a collective (e.g., electorate, legislature, collegial court, expert panel, or committee) arrive at coherent collective preferences or judgments on some issues, on the basis of its members’ individual preferences or judgments? How can we rank different social alternatives in an order of social welfare? Social choice theorists study these questions not just by looking at examples, but by developing general models and proving theorems.

Pioneered in the 18th century by Nicolas de Condorcet and Jean-Charles de Borda and in the 19th century by Charles Dodgson (also known as Lewis Carroll), social choice theory took off in the 20th century with the works of Kenneth Arrow, Amartya Sen, and Duncan Black. Its influence extends across economics, political science, philosophy, mathematics, and recently computer science and biology. Apart from contributing to our understanding of collective decision procedures, social choice theory has applications in the areas of institutional design, welfare economics, and social epistemology.

## 1. History of social choice theory

### 1.1 Condorcet

The two scholars most often associated with the development of social choice theory are the Frenchman Nicolas de Condorcet (1743–1794) and the American Kenneth Arrow (1921–2017). Condorcet was a liberal thinker in the era of the French Revolution who was pursued by the revolutionary authorities for criticizing them. After a period of hiding, he was eventually arrested, though apparently not immediately identified, and he died in prison (see McLean and Hewitt 1994)[^mclean-1994]. In his *Essay on the Application of Analysis to the Probability of Majority Decisions* (1785), he advocated a particular voting system, pairwise majority voting, and presented his two most prominent insights. The first, known as *Condorcet’s jury theorem*, is that if each member of a jury has an equal and independent chance better than random, but worse than perfect, of making a correct judgment on whether a defendant is guilty (or on some other factual proposition), the majority of jurors is more likely to be correct than each individual juror, and the probability of a correct majority judgment approaches 1 as the jury size increases. Thus, under certain idealized conditions, majority rule is good at ‘tracking the truth’ (e.g., Grofman, Owen, and Feld 1983)[^grofman-1983].

Condorcet’s second insight, often called *Condorcet’s paradox*, is the observation that majority preferences can be ‘irrational’ (specifically, intransitive) even when individual preferences are ‘rational’ (specifically, transitive). Suppose, for example, that one third of a group prefers alternative $x$ to $y$ to $z$, a second third prefers $y$ to $z$ to $x$, and a final third prefers $z$ to $x$ to $y$. Then there are majorities (of two thirds) for $x$ against $y$, for $y$ against $z$, and for $z$ against $x$: a ‘cycle’, which violates transitivity. Furthermore, no alternative is a *Condorcet winner*, an alternative that beats, or at least ties with, every other alternative in pairwise majority contests.

Condorcet anticipated a key theme of modern social choice theory: majority rule is at once a plausible method of collective decision making and yet subject to some surprising problems. Resolving or bypassing these problems remains one of social choice theory’s core concerns.

### 1.2 Arrow and his influence

While Condorcet had investigated a *particular* voting method (majority voting), Arrow, who won the Nobel Memorial Prize in Economics in 1972, introduced a *general* approach to the study of preference aggregation, partly inspired by his teacher of logic, Alfred Tarski (1901–1983), from whom he had learnt relation theory as an undergraduate at the City College of New York (Suppes 2005)[^suppes-2005]. Arrow considered a class of *possible* aggregation methods, which he called *social welfare functions*, and asked which of them satisfy certain axioms or desiderata. He proved that, surprisingly, there exists no method for aggregating the preferences of two or more individuals over three or more alternatives into collective preferences, where this method satisfies five seemingly plausible axioms, discussed below.

This result, known as *Arrow’s impossibility theorem*, prompted much work and many debates in social choice theory and welfare economics. William Riker (1920–1993), who inspired the Rochester school in political science, interpreted it as a mathematical proof of the impossibility of populist democracy (e.g., Riker 1982)[^riker-1982]. Others, most prominently Amartya Sen (born 1933), who won the 1998 Nobel Memorial Prize, took it to show that ordinal preferences are insufficient for making satisfactory social choices and that social decisions require a richer informational basis. Commentators also questioned whether Arrow’s desiderata on an aggregation method are as innocuous as claimed or whether they should be relaxed.

The lessons from Arrow’s theorem depend, in part, on how we interpret an Arrovian social welfare function. The use of ordinal preferences as the ‘aggreganda’ may be easier to justify if we interpret the aggregation rule as a *voting method* than if we interpret it as a *social evaluation method*. Sen argued that when a social planner seeks to rank different social alternatives in an order of social desirability (thereby employing some aggregation rule as a social evaluation method), it may be justifiable and even necessary to use additional information over and above ordinal preferences, such as interpersonally comparable welfare measurements (e.g., Sen 1982)[^sen-1982] or information about people’s capabilities to achieve valuable functionings (e.g., Sen 1992)[^sen-1992].

Arrow himself held the view

> ‘that interpersonal comparison of utilities has no meaning and … that there is no meaning relevant to welfare comparisons in the measurability of individual utility.’ (1951/1963: 9)

This view was influenced by neoclassical economics, associated with scholars such as Vilfredo Pareto (1848–1923), Lionel Robbins (1898–1984), John Hicks (1904–1989), co-winner of the Economics Nobel Prize with Arrow, and Paul Samuelson (1915–2009), another Nobel Laureate. Arrow’s theorem demonstrates the stark implications of the ‘ordinalist’ assumptions of neoclassical thought. For a critique of this restrictive ordinalist approach to welfare economics, see also the work of Kotaro Suzumura (1944–2020) (e.g., Suzumura 2000)[^suzumura-2000].

Nowadays most social choice theorists have moved beyond the negative interpretations of Arrow’s theorem and are interested in the trade-offs involved in finding satisfactory decision procedures and the possibilities opened up by relaxing certain restrictive assumptions. Sen has promoted this ‘possibilist’ interpretation of social choice theory (e.g., in his 1998 Nobel lecture). Moreover, as Fabienne Peter has argued, by moving beyond the narrow informational basis leading to the classic impossibility results, social choice theory can become a more promising framework for policy evaluation and offer resources for taking into account the situated nature of people’s agency, inequalities between them, and issues of gender (Peter 2003)[^peter-2003].

In contemporary social choice theory, it is perhaps fair to say, Arrow’s axiomatic method is more influential than his impossibility theorem itself (on the axiomatic method, see Thomson 2000)[^thomson-2000]. The paradigmatic kind of result in formal work is now the ‘characterization theorem’. Here the aim is to identify a set of plausible necessary and sufficient conditions that uniquely characterize a particular solution (or class of solutions) to a given type of collective decision problem. An early example is Kenneth May’s (1952)[^may-1952] characterization of majority rule, discussed below.

### 1.3 Borda, Carroll, Black, and others

Condorcet and Arrow are not the only founding figures of social choice theory. Condorcet’s contemporary and co-national Jean-Charles de Borda (1733–1799) defended a voting system that is often seen as a prominent alternative to majority voting. The *Borda count*, formally defined later, avoids Condorcet’s paradox but violates one of Arrow’s conditions, the *independence of irrelevant alternatives*. Thus the debate between Condorcet and Borda is a precursor to some modern debates on how to respond to Arrow’s theorem.

The origins of this debate precede Condorcet and Borda. In the Middle Ages, Ramon Llull (c1235–1315) proposed the aggregation method of pairwise majority voting, while Nicolas Cusanus (1401–1464) proposed a variant of the Borda count (McLean 1990)[^mclean-1990]. In 1672, the German scholar and jurist Samuel von Pufendorf (1632–1694) compared simple majority, qualified majority, and unanimity rules and offered an analysis of the structure of preferences that can be seen as a precursor to later discoveries (e.g., on *single-peakedness*, discussed below) (Gaertner 2005)[^gaertner-2005].

In the 19ᵗʰ century, the British mathematician and clergyman Charles Dodgson (1832–1898), better known as Lewis Carroll, independently rediscovered some of Condorcet’s and Borda’s insights and also developed a theory of proportional representation. It was largely thanks to the Scottish economist Duncan Black (1908–1991) that Condorcet’s, Borda’s, and Dodgson’s social-choice-theoretic ideas were drawn to the attention of the modern research community (McLean, McMillan, and Monroe 1995)[^mclean-1995][^mclean-1995-2]. Black also made several discoveries related to majority voting, some of which are discussed below.

In France, George-Théodule Guilbaud ([1952] 1966) wrote an important but often overlooked paper, revisiting Condorcet’s theory of voting from a logical perspective and sparking a French literature on the *Condorcet effect*, the logical problem underlying Condorcet’s paradox, which has only recently received more attention in Anglophone social choice theory (Monjardet 2005)[^monjardet-2005]. In particular, Guilbaud anticipated some of the ideas underlying recent work on the aggregation of judgments. For further contributions on the history of social choice theory, see McLean, McMillan, and Monroe (1996), McLean and Urken (1995), McLean and Hewitt (1994), and a special issue of *Social Choice and Welfare*, edited by Salles (2005)[^salles-2005].

## 2. Three formal arguments for majority rule

To introduce social choice theory formally, it helps to consider a simple decision problem: a collective choice between two alternatives.

### 2.1 The concept of an aggregation rule

Let $N = \{1, 2, \ldots ,n\}$ be a set of individuals, where $n \ge 2$. These individuals have to choose between two alternatives (candidates, policies etc.). Each individual $i \in N$ casts a vote, denoted $v_i$, where

- $v_i = 1$ represents a vote for the first alternative,
- $v_i = -1$ represents a vote for the second alternative, and optionally
- $v_i = 0$ represents an abstention (for simplicity, we set this possibility aside in this section).

A combination of votes across the individuals, $\langle v_1, v_2 , \ldots ,v_n\rangle$, is called a *profile*. For any profile, the group seeks to arrive at a social decision $v$, where

- $v = 1$ represents a decision for the first alternative,
- $v = -1$ represents a decision for the second alternative, and
- $v = 0$ represents a tie.

An *aggregation rule* is a function $f$ that assigns to each profile $\langle v_1, v_2 , \ldots ,v_n\rangle$ (in some domain of admissible profiles) a social decision $v = f(v_1, v_2 , \ldots ,v_n)$. Examples are:

> *Majority rule*: For each profile $\langle v_1, v_2 , \ldots ,v_n\rangle$,
>
> $$ f(v_1,v_2,\ldots,v_n) = \begin{cases} 1 & \begin{aligned} &\text{if } v_1+v_2+\cdots+v_n \gt 0 \\ &\text{(there are more 1s than -1s)}\end{aligned} \\ 0 & \begin{aligned} &\text{if } v_1+v_2+\cdots+v_n = 0 \\ &\text{(there are as many 1s as -1s)}\end{aligned}\\ -1 & \begin{aligned} &\text{if } v_1+v_2+\cdots+v_n \lt 0\\ &\text{(there are more -1s than 1s)}\end{aligned} \end{cases}$$
>
> *Dictatorship*: For each profile $\langle v_1, v_2 , \ldots ,v_n\rangle$,
>
> $$ f(v_1, v_2 , \ldots ,v_n) = v_i, $$
>
> where $i \in N$ is an antecedently fixed individual (the ‘dictator’).
>
> *Weighted majority rule*: For each profile $\langle v_1, v_2 , \ldots ,v_n\rangle$,
>
> $$ f(v_1,v_2,\ldots,v_n) = \begin{cases} 1 & \text{if } w_1v_1+w_2v_2+\cdots+w_nv_n \gt 0 \\ 0 & \text{if } w_1v_1+w_2v_2+\cdots+w_nv_n = 0 \\ -1 & \text{if } w_1v_1+w_2v_2+\cdots+w_nv_n \lt 0 \end{cases}$$
>
> where $w_1, w_2 , \ldots ,w_n$ are real numbers, interpreted as the ‘voting weights’ of the $n$ individuals.

Two points about the concept of an aggregation rule are worth noting. First, under the standard definition, an aggregation rule is defined *extensionally*, not *intensionally*: it is a *mapping* (*functional relationship*) between individual inputs and collective outputs, not a *set of explicit instructions* (a *rule* in the ordinary-language sense). Different sets of instructions could in principle give rise to the same mapping from inputs to outputs. Secondly, an aggregation rule is defined for a fixed set of individuals $N$ and a fixed decision problem, so that majority rule in a group of two individuals is a different mathematical object from majority rule in a group of three. One potential disadvantage of this way of defining an aggregation rule is that it makes it harder to determine how a given aggregation rule is to be extended to inputs outside the function’s formal domain. By contrast, if we were given an explicit set of instructions, it might be easier to infer, for instance, how these are to be extended from the case of $n$ individuals and three alternatives to the case of $n + 1$ individuals and four alternatives.

To illustrate, Tables 1 and 2 show majority rule for groups of sizes two and three as extensional objects. The rows of each table correspond to the different possible profiles of votes; the final column displays the resulting social decisions.

| *Individual 1’s vote* | *Individual 2’s vote* | *Collective decision* |
| --- | --- | --- |
| 1 | 1 | 1 |
| 1 | $-1$ | 0 |
| $-1$ | 1 | 0 |
| $-1$ | $-1$ | $-1$ |

*Table 1:* Majority rule among two individuals

| *Individual 1’s vote* | *Individual 2’s vote* | *Individual 3’s vote* | *Collective decision* |
| --- | --- | --- | --- |
| 1 | 1 | 1 | 1 |
| 1 | 1 | $-1$ | 1 |
| 1 | $-1$ | 1 | 1 |
| 1 | $-1$ | $-1$ | $-1$ |
| $-1$ | 1 | 1 | 1 |
| $-1$ | 1 | $-1$ | $-1$ |
| $-1$ | $-1$ | 1 | $-1$ |
| $-1$ | $-1$ | $-1$ | $-1$ |

*Table 2:* Majority rule among three individuals

The present way of representing an aggregation rule helps us see how many possible aggregation rules there are. Suppose there are $k$ profiles in the domain of admissible inputs (in the present example, $k = 2^n$, since each of the $n$ individuals has two choices, with abstention disallowed). Suppose, further, there are $l$ possible social decisions for each profile (in the example, $l = 3$, allowing ties). Then there are $l^k$ possible aggregation rules: the relevant table has $k$ rows, and in each row, there are $l$ possible ways of specifying the final entry (the collective decision). Thus the number of possible aggregation rules grows exponentially with the number of admissible profiles and the number of possible decision outcomes.

To select an aggregation rule non-arbitrarily from this large class of possible ones, some constraints are needed. I now consider three formal arguments for majority rule.

### 2.2 A procedural argument for majority rule

The first involves imposing some ‘procedural’ requirements on the relationship between individual votes and social decisions and showing that majority rule is the only aggregation rule satisfying them. May (1952)[^may-1952] introduced four such requirements:

> *Universal domain*: The domain of admissible inputs of the aggregation rule consists of all logically possible profiles of votes $\langle v_1, v_2 , \ldots ,v_n\rangle$, where each $v_i \in \{-1,1\}$.
>
> *Anonymity*: For any admissible profiles $\langle v_1, v_2 , \ldots ,v_n\rangle$ and $\langle w_1, w_2 , \ldots ,w_n\rangle$ that are permutations of each other (i.e., one can be obtained from the other by reordering the entries), the social decision is the same, i.e., $f(v_1, v_2 , \ldots ,v_n) = f(w_1, w_2 , \ldots ,w_n)$.
>
> *Neutrality*: For any admissible profile $\langle v_1, v_2 , \ldots ,v_n\rangle$, if the votes for the two alternatives are reversed, the social decision is reversed too, i.e., $f(-v_1, -v_2 , \ldots ,-v_n) = -f(v_1, v_2 , \ldots ,v_n)$.
>
> *Positive responsiveness*: For any admissible profile $\langle v_1, v_2 , \ldots ,v_n\rangle$, if some voters change their votes in favour of one alternative (say the first) and all other votes remain the same, the social decision does not change in the opposite direction; if the social decision was a tie prior to the change, the tie is broken in the direction of the change, i.e., if [$w_i \gt v_i$ for some $i$ and $w_j = v_j$ for all other $j$] and $f(v_1, v_2 , \ldots ,v_n) = 0$ or 1, then $f(w_1, w_2 , \ldots ,w_n) = 1$.

Universal domain requires the aggregation rule to cope with any level of ‘pluralism’ in its inputs; anonymity requires it to treat all voters equally; neutrality requires it to treat all alternatives equally; and positive responsiveness requires the social decision to be a positive function of the way people vote. May proved the following:

> *Theorem* (May 1952)[^may-1952]: An aggregation rule satisfies universal domain, anonymity, neutrality, and positive responsiveness if and only if it is majority rule.

Apart from providing an argument for majority rule based on four plausible procedural desiderata, the theorem helps us characterize other aggregation rules in terms of which desiderata they violate. Dictatorships and weighted majority rules with unequal individual weights violate anonymity. Asymmetrical supermajority rules (under which a supermajority of the votes, such as two thirds or three quarters, is required for a decision in favour of one of the alternatives, while the other alternative is the default choice) violate neutrality. This may sometimes be justifiable, for instance when there is a presumption in favour of one alternative, such as a presumption of innocence in a jury decision. Symmetrical supermajority rules (under which neither alternative is chosen unless it is supported by a sufficiently large supermajority) violate positive responsiveness. A more far-fetched example of an aggregation rule violating positive responsiveness is the inverse majority rule (here the alternative *rejected* by a majority wins).

May’s theorem has been generalized in a variety of ways, including to the mathematically interesting but unrealistic case of infinite sets of voters (Fey 2004)[^fey-2004] and to choices between multiple options (e.g., Cantillon and Rangel 2002, offering a May-style characterization of pairwise majority voting; and Goodin and List 2006, offering a May-style characterization of plurality rule)[^cantillon-2002][^goodin-2006].

### 2.3 An epistemic argument for majority rule

Condorcet’s jury theorem provides a consequentialist argument for majority rule. The argument is ‘epistemic’, insofar as the aggregation rule is interpreted as a truth-tracking device (e.g., Grofman, Owen and Feld 1983; List and Goodin 2001)[^grofman-1983][^list-2001][^list-2001-2].

Suppose the aim is to make a judgment on some procedure-independent fact or state of the world, denoted $X$. In a jury decision, the defendant is either guilty $(X = 1)$ or innocent $(X = -1)$. In an expert-panel decision on the safety of some technology, the technology may be either safe $(X = 1)$ or not $(X = -1)$. Each individual’s vote expresses a judgment on that fact or state, and the social decision represents the collective judgment. The goal is to reach a factually correct collective judgment. Which aggregation rule performs best at ‘tracking the truth’ depends on the relationship between the individual votes and the relevant fact or state of the world.

Condorcet assumed that each individual is better than random at making a correct judgment (the competence assumption) and that different individuals’ judgments are stochastically independent, given the state of the world (the independence assumption). Formally, let $V_1, V_2 , \ldots ,V_n$ (capital letters) denote the random variables generating the specific individual votes $v_1, v_2 , \ldots ,v_n$ (small letters), and let $V = f(V_1, V_2 , \ldots ,V_n)$ denote the resulting random variable representing the social decision $v = f(v_1, v_2 , \ldots ,v_n)$ under a given aggregation rule $f$, such as majority rule. Condorcet’s assumptions can be stated as follows:

> *Competence*: For each individual $i \in N$ and each state of the world $x \in \{-1,1\}, Pr(V_i = x | X = x) = p \gt 1/2$, where $p$ is the same across individuals and states.
>
> *Independence*: The votes of different individuals $V_1, V_2 , \ldots ,V_n$ are independent of each other, conditional on each value $x \in \{-1,1\}$ of $X$.

Under these assumptions, majority voting is a good truth-tracker:

> *Theorem* (Condorcet’s jury theorem): For each state of the world $x \in \{-1,1\}$, the probability of a correct majority decision, $Pr(V = x | X = x)$, is greater than each individual’s probability of a correct vote, $Pr(V_i = x | X = x)$, and converges to 1, as the number of individuals $n$ increases.[^note-1]

The first conjunct (‘is greater than each individual’s probability’) is the *non-asymptotic conclusion*, the second (‘converges to 1’) the *asymptotic conclusion*. One can further show that, if the two states of the world have an equal prior probability (i.e., $Pr(X = 1) = Pr(X = -1) = 1/2)$, majority rule is the most reliable of all aggregation rules, maximizing $Pr(V = X)$ (e.g., Ben-Yashar and Nitzan 1997)[^ben-yashar-1997].

Although the jury theorem is often invoked to demonstrate the epistemic merits of democracy (for recent discussions, see, e.g., Landemore 2012 and Goodin and Spiekermann 2018)[^goodin-2018], its assumptions are highly idealistic. The competence assumption is not a conceptual claim but an empirical one and depends on any given decision problem. Although an average (not necessarily equal) individual competence above 1/2 may be sufficient for Condorcet’s conclusion (e.g., Grofman, Owen, and Feld 1983; Boland 1989; Kanazawa 1998)[^boland-1989][^grofman-1983][^kanazawa-1998],[^note-2] the theorem ceases to hold if individuals are randomizers (no better and no worse than a coin toss) or if they are worse than random $(p \lt 1/2)$. In the latter case, the probability of a correct majority decision is *less* than each individual’s probability of a correct vote and converges to 0, as the jury size increases. The theorem’s conclusion can also be undermined in less extreme cases (Berend and Paroush 1998)[^berend-1998], for instance when each individual’s reliability, though above 1/2, is an exponentially decreasing function approaching 1/2 with increasing jury size.

Similarly, whether the independence assumption is true depends on the decision problem in question. Although Condorcet’s conclusion is robust to the presence of some interdependencies between individual votes, the structure of these interdependencies matters (e.g., Boland 1989; Ladha 1992; Estlund 1994; Berend and Sapir 2007; Pivato 2017)[^berend-2007][^boland-1989][^estlund-1994][^ladha-1992][^pivato-2017]. If all individuals’ votes are perfectly correlated with one another or mimic a small number of opinion leaders, the collective judgment is no more reliable than the judgment among a small number of independent individuals.

Bayesian networks, as employed in Pearl’s account of causation (2000), have been used to model the effects of voter dependencies on the jury theorem and to distinguish between stronger and weaker variants of conditional independence (Dietrich and List 2004; Dietrich and Spiekermann 2013)[^dietrich-2004][^dietrich-2013][^list-2004]. This work suggests that, under realistic assumptions, Condorcet’s asymptotic conclusion fails to hold, and the probability of a correct majority decision converges, at most, to a number strictly below 1 (e.g., the probability that the jury’s evidence is not misleading). Furthermore, Dietrich (2008)[^dietrich-2008][^dietrich-2008-2] has argued that Condorcet’s original two assumptions are never simultaneously justified, in the sense that, even when they are both true, one cannot obtain evidence to support both at once.

Finally, game-theoretic work challenges an implicit assumption of the jury theorem, namely that voters will always reveal their judgments truthfully. Even if all voters prefer a correct to an incorrect collective judgment, they may still have incentives to misrepresent their individual judgments. This can happen when, conditional on the event of being pivotal for the outcome, a voter expects a higher chance of bringing about a correct collective judgment by voting *against* his or her own private judgment than by voting in line with it (Austin-Smith and Banks 1996; Feddersen and Pesendorfer 1998)[^feddersen-1998].

### 2.4 A utilitarian argument for majority rule

Another consequentialist argument for majority rule is utilitarian rather than epistemic. It does not require the existence of an independent fact or state of the world that the collective decision is supposed to track. Suppose each voter gets some utility from the collective decision, which depends on whether the decision matches his or her vote (preference): specifically, each voter gets a utility of 1 from a match between his or her vote and the collective outcome and a utility of 0 from a mismatch.[^note-3] The Rae-Taylor theorem then states that if each individual has an equal prior probability of preferring each of the two alternatives, majority rule maximizes each individual’s expected utility (see, e.g., Mueller 2003)[^mueller-2003].

Relatedly, majority rule minimizes the number of frustrated voters (defined as voters on the losing side) and maximizes total utility across voters. Brighouse and Fleurbaey (2010) generalize this result. Define voter $i$’s *stake* in the decision, $d_i$, as the utility difference between his or her preferred outcome and his or her dispreferred outcome. The Rae-Taylor theorem rests on an implicit equal-stakes assumption, i.e., $d_i = 1$ for every $i \in N$. Brighouse and Fleurbaey show that when stakes are allowed to vary across voters, total utility is maximized not by majority rule, but by a weighted majority rule, where each individual $i$’s voting weight $w_i$ is proportional to his or her stake $d_i$.

## 3. The aggregation of preferences

At the heart of social choice theory is the analysis of preference aggregation, understood as the aggregation of several individuals’ preference rankings of two or more social alternatives into a single, collective preference ranking (or choice) over these alternatives. The basic framework, which is still standard, was introduced by Arrow (1951/1963).

### 3.1 The basic framework

Consider a set $N = \{1, 2, \ldots ,n\}$ of individuals $(n \ge 2)$. Let $X = \{x, y, z, \ldots \}$ be a set of social alternatives, for example possible worlds, policy platforms, election candidates, or allocations of goods. Each individual $i \in N$ has a *preference ordering* $R_i$ over these alternatives: a complete and transitive binary relation on $X$.[^note-4] For any $x, y \in X$, $xR_i y$ means that individual $i$ weakly prefers $x$ to $y$. We write $xP_i y$ if $xR_i y$ and not $yR_i x$ (‘individual $i$ strictly prefers $x$ to $y$’), and $xI_i y$ if $xR_i y$ and $yR_i x$ (‘individual $i$ is indifferent between $x$ and $y$’).

A combination of preference orderings across the individuals, $\langle R_1, R_2 , \ldots ,R_n\rangle$, is called a *profile*. A *preference aggregation rule*, $F$, is a function that assigns to each profile $\langle R_1, R_2 , \ldots ,R_n\rangle$ (in some domain of admissible profiles) a social preference relation $R = F(R_1, R_2 , \ldots ,R_n)$ on $X$. When $F$ is clear from the context, we simply write $R$ for the social preference relation corresponding to $\langle R_1, R_2 , \ldots ,R_n\rangle$.

For any $x, y \in X$, *xRy* means that $x$ is socially weakly preferred to $y$. We also write $xPy$ if $xRy$ and not $yRx$ (‘$x$ is strictly socially preferred to $y$’), and $xIy$ if $xRy$ and $yRx$ (‘$x$ and $y$ are socially tied’). For generality, the requirement that $R$ be complete and transitive is not built into the definition of a preference aggregation rule.

The paradigmatic example of a preference aggregation rule is *pairwise majority voting*, as discussed by Condorcet. Here, for any profile $\langle R_1, R_2 , \ldots ,R_n\rangle$ and any $x, y \in X$, $xRy$ if and only if at least as many individuals have $xR_i y$ as have $yR_i x$, formally $|\{i \in N : xR_i y\}| \ge |\{i \in N : yR_i x\}|.$ As we have seen, this does not guarantee transitive social preferences.[^note-5]

How frequent are intransitive majority preferences? It can be shown that the proportion of preference profiles (among all possible ones) that lead to cyclical majority preferences increases with the number of individuals $(n)$ and the number of alternatives $(|X|).$ If all possible preference profiles are equally likely to occur (the so-called ‘impartial culture’ scenario), majority cycles should therefore be probable in large electorates (Gehrlein 1983)[^gehrlein-1983]. (Technical work further distinguishes between ‘top-cycles’ and cycles below a possible Condorcet-winning alternative.) However, the probability of cycles can be significantly lower under certain systematic, even small, deviations from an impartial culture (List and Goodin 2001: Appendix 3; Tsetlin, Regenwetter, and Grofman 2003; Regenwetter et al. 2006)[^list-2001][^list-2001-2][^regenwetter-2006][^tsetlin-2003].

### 3.2 Arrow’s theorem

Abstracting from pairwise majority voting, Arrow suggested the following conditions on a preference aggregation rule, $F$.

> *Universal domain*: The domain of $F$ is the set of all logically possible profiles of complete and transitive individual preference orderings.
>
> *Ordering*: For any profile $\langle R_1, R_2 , \ldots ,R_n\rangle$ in the domain of $F$, the social preference relation $R$ is complete and transitive.
>
> *Weak Pareto principle*: For any profile $\langle R_1, R_2 , \ldots ,R_n\rangle$ in the domain of $F$, if for all $i \in N$, $xP_i y,$ then $xPy.$
>
> *Independence of irrelevant alternatives*: For any two profiles $\langle R_1, R_2 , \ldots ,R_n\rangle$ and $\langle R^*_1, R^*_2,\ldots, R^*_n\rangle$ in the domain of $F$ and any $x, y \in X$, if for all $i \in N$, $R_i$’s ranking between $x$ and $y$ coincides with $R^*_i$’s ranking between $x$ and $y$, then $xRy$ if and only if $xR^*y.$
>
> *Non-dictatorship*: There does not exist an individual $i \in N$ such that, for all $\langle R_1, R_2 , \ldots ,R_n\rangle$ in the domain of $F$ and all $x, y \in X, xP_i y$ implies $xPy.$

Universal domain requires the aggregation rule to cope with any level of ‘pluralism’ in its inputs. Ordering requires it to produce ‘rational’ social preferences, avoiding Condorcet cycles. The weak Pareto principle requires that when all individuals strictly prefer alternative $x$ to alternative $y$, so does society. Independence of irrelevant alternatives requires that the social preference between any two alternatives $x$ and $y$ depend only on the individual preferences between $x$ and $y$, not on individuals’ preferences over other alternatives. Non-dictatorship requires that there be no ‘dictator’, who always determines the social preference, regardless of other individuals’ preferences. (Note that pairwise majority voting satisfies all of these conditions except ordering.)

> *Theorem* (Arrow 1951/1963)[^arrow-1951]: If $|X| \gt 2$, there exists no preference aggregation rule satisfying universal domain, ordering, the weak Pareto principle, independence of irrelevant alternatives, and non-dictatorship.

It is evident that this result carries over to the aggregation of other kinds of orderings, as distinct from preference orderings, such as (i) belief orderings over several hypotheses (ordinal credences), (ii) multiple criteria that a single decision maker may use to generate an all-things-considered ordering of several decision options, and (iii) conflicting value rankings to be reconciled.

Examples of other such aggregation problems to which Arrow’s theorem has been applied include: intrapersonal aggregation problems (e.g., May 1954; Hurley 1985)[^hurley-1985][^may-1954], theory choice (e.g., Okasha 2011; cf. Morreau 2015)[^morreau-2015][^okasha-2011], evidence amalgamation (e.g., Stegenga 2013)[^stegenga-2013], the aggregation of multiple similarity orderings into an all-things-considered similarity ordering (e.g., Morreau 2010; Kroedel and Huber 2013)[^kroedel-2013][^morreau-2010], decision-making under normative uncertainty (e.g., MacAskill 2016)[^macaskill-2016], and radical interpretation in the face of competing criteria of interpretation choice (Hattiangadi 2020)[^hattiangadi-2020]. In each case, the plausibility of Arrow’s theorem depends on the case-specific plausibility of Arrow’s ordinalist framework and the theorem’s conditions.

Generally, if we consider Arrow’s framework appropriate and his conditions indispensable, Arrow’s theorem raises a serious challenge. To avoid it, we must relax at least one of the five conditions or give up the restriction of the aggregation rule’s inputs to orderings and defend the use of richer inputs, as discussed in Section 4. In what follows, we consider non-dictatorial escape routes from Arrow’s theorem.

### 3.3 Possibilities of preference aggregation

#### 3.3.1 Relaxing universal domain

One way to avoid Arrow’s theorem is to relax universal domain. If the aggregation rule is required to accept as input only preference profiles that satisfy certain ‘cohesion’ conditions, then aggregation rules such as pairwise majority voting will produce complete and transitive social preferences. The best-known cohesion condition is *single-peakedness* (Black 1948)[^black-1948].

A profile $\langle R_1, R_2 , \ldots ,R_n\rangle$ is *single-peaked* if the alternatives can be aligned from ‘left’ to ‘right’ (e.g., on some cognitive or ideological dimension) such that each individual has a most preferred position on that alignment with decreasing preference as alternatives get more distant (in either direction) from the most preferred position. Formally, this requires the existence of a linear ordering $\Omega$ on $X$ such that, for every triple of alternatives $x, y, z \in X$, if $y$ lies between $x$ and $z$ with respect to $\Omega$, it is not the case that $xR_i y$ and $zR_i y$ (this rules out a ‘cave’ between $x$ and $z$, at $y)$. Single-peakedness is plausible in some democratic contexts. If the alternatives in $X$ are different tax rates, for example, each individual may have a most preferred tax rate (which will be lower for a libertarian individual than for a socialist) and prefer other tax rates less as they get more distant from the ideal.

Black (1948)[^black-1948] proved that if the domain of the aggregation rule is restricted to the set of all profiles of individual preference orderings satisfying single-peakedness, majority cycles cannot occur, and the most preferred alternative of the median individual relative to the relevant left-right alignment is a Condorcet winner (assuming $n$ is odd). Pairwise majority voting then satisfies the rest of Arrow’s conditions—a point also discussed in detail by Arrow (1951/1963).

Other domain-restriction conditions with similar implications include *single-cavedness*, a geometrical mirror image of single-peakedness (Inada 1964)[^inada-1964], *separability into two groups* (*ibid.*), and *latin-squarelessness* (Ward 1965)[^ward-1965], the latter two more complicated combinatorial conditions (for a review, see Gaertner 2001)[^gaertner-2001]. Sen (1966)[^sen-1966] showed that all these conditions imply a weaker condition, *triple-wise value-restriction*. It requires that, for every triple of alternatives $x, y, z \in X$, there exists one alternative in $\{x, y, z\}$ and one rank $r \in \{1, 2, 3\}$ such that no individual ranks that alternative in $r$ᵗʰ place among $x, y$, and $z$. For instance, all individuals may agree that $y$ is not bottom $(r = 3)$ among $x, y$, and $z$. Triple-wise value-restriction suffices for transitive majority preferences.

There has been much discussion on whether, and under what conditions, real-world preferences fall into such a restricted domain. It has been suggested, for example, that group deliberation can induce single-peaked preferences, by leading participants to focus on a shared cognitive or ideological dimension (a ‘meta-agreement’) (Miller 1992; Knight and Johnson 1994; Dryzek and List 2003)[^dryzek-2003][^knight-1994][^miller-1992]. Experimental evidence from deliberative opinion polls, where participants’ preferences were elicited before and after a period of group deliberation, is consistent with this hypothesis (List, Luskin, Fishkin, and McLean 2013)[^list-2013], though further empirical work is needed. For a critical assessment of the idea of deliberation-induced ‘meta-agreement’, see Ottonelli and Porello (2013). For a recent computational study, see Rafiee Rad and Roy (2021).

#### 3.3.2 Relaxing ordering

Preference aggregation rules are normally expected to produce orderings as their outputs, but sometimes we may only require partial orderings or not fully transitive binary relations. An aggregation rule that produces transitive but often incomplete social preferences is the *Pareto dominance rule*: here, for any profile $\langle R_1, R_2 , \ldots ,R_n\rangle$ and any $x, y \in X$, $xRy$ if and only if, for all $i \in N$, $xP_i y$. An aggregation rule that produces complete but often intransitive social preferences is the *Pareto extension rule*: here, for any profile $\langle R_1, R_2 , \ldots ,R_n\rangle$ and any $x, y \in X$, $xRy$ if and only if it is not the case that, for all $i \in N$, $yP_i x$. Both rules have a unanimitarian spirit, giving each individual veto power either against the *presence* of a weak social preference for $x$ over $y$ or against its *absence*.

Gibbard (1969)[^gibbard-1969] proved that even if we replace the requirement of transitivity with what he called *quasi-transitivity*, the resulting possibilities of aggregation are still very limited. Call a preference relation $R$ *quasi-transitive* if the induced strict relation $P$ is transitive (while the indifference relation $I$ need not be transitive). Call an aggregation rule *oligarchic* if there is a subset $M \subseteq N$ (the ‘oligarchs’) such that (i) if, for all $i \in M$, $xP_i y,$ then $xPy,$ and (ii) if, for some $i \in M$, $xP_i y$, then $xRy.$ The Pareto extension rule is an example of an oligarchic aggregation rule with $M = N$. In an oligarchy, the oligarchs are jointly decisive and have individual veto power. Gibbard proved the following:

> *Theorem* (Gibbard 1969)[^gibbard-1969]: If $|X| \gt 2$, there exists no preference aggregation rule satisfying universal domain, quasi-transitivity and completeness of social preferences, the weak Pareto principle, independence of irrelevant alternatives, and non-oligarchy.

#### 3.3.3 Relaxing the weak Pareto principle

The weak Pareto principle is arguably hard to give up. One case in which we may lift it is that of spurious unanimity, where a unanimous preference for $x$ over $y$ is based on mutually inconsistent reasons (e.g., Mongin 1997; Gilboa, Samet, and Schmeidler 2004)[^gilboa-2004][^mongin-1997]. For instance, two men may each prefer to fight a duel (alternative $x)$ to not fighting it (alternative $y)$ because each over-estimates his chances of winning. There may exist no mutually agreeable probability assignment over possible outcomes of the duel (i.e., who would win) that would ‘rationalize’ the unanimous preference for $x$ over $y$. In this case, the unanimous preference is a bad indicator of social preferability$.$ This example, however, depends on the fact that the alternatives of fighting and not fighting are not fully specified outcomes but uncertain prospects. Arguably, the weak Pareto principle is more plausible in cases without uncertainty.

An aggregation rule that becomes possible when the weak Pareto principle is dropped is an *imposed rule*, where, for any profile $\langle R_1, R_2 , \ldots ,R_n\rangle$, the social preference relation $R$ is an antecedently fixed (‘imposed’) ordering $R_{\textit{imposed}}$ of the alternatives. Though completely unresponsive to individual preferences, this aggregation rule satisfies the rest of Arrow’s conditions. Another possibility, which is no less degenerate, would make one individual an ‘inverse dictator’. Here, for any profile $\langle R_1, R_2 , \ldots ,R_n\rangle$ and any $x, y \in X$, we have $xRy$ if and only if $yR_i x,$ where $i$ is some antecedently fixed individual. Thus the social preference is always the opposite of individual $i$’s preference. Formally, this aggregation rule satisfies all of Arrow’s conditions except the weak Pareto principle.

Although, from a democratic perspective, the idea that unanimous individual preferences should be respected at the social level (at least when the unanimity isn’t ‘spurious’) seems difficult to contest, we will consider a critique of the Pareto principle in Section 3.4 below.

#### 3.3.4 Relaxing independence of irrelevant alternatives

A common way to obtain possible preference aggregation rules is to give up independence of irrelevant alternatives. Almost all familiar voting methods over three or more alternatives that involve some form of preferential voting (with voters being asked to express full or partial preference orderings) violate this condition.

A standard example is *plurality rule*: here, for any profile $\langle R_1, R_2 , \ldots ,R_n\rangle$ and any $x, y \in X$, $xRy$ if and only if $|\{i \in N$ : for all $z \ne x$, $xP_i z\}| \ge |\{i \in N$ : for all $z \ne y$, $yP_i z\}|.$ Informally, alternatives are socially ranked in the order of how many individuals most prefer each of them. Plurality rule avoids Condorcet’s paradox, but runs into other problems. Most notably, an alternative that is majority-dispreferred to every other alternative may win under plurality rule: if 34% of the voters rank $x$ above $y$ above $z, 33$% rank $y$ above $z$ above $x$, and 33% rank $z$ above $y$ above $x$, plurality rule ranks $x$ above each of $y$ and $z$, while pairwise majority voting would rank $y$ above $z$ above $x$ ($y$ is the Condorcet winner). By disregarding individuals’ lower-ranked alternatives, plurality rule also violates the weak Pareto principle. However, plurality rule may be plausible in ‘restricted informational environments’, where the balloting procedure collects information only about voters’ top preferences, not about their full preference rankings (Goodin and List 2006)[^goodin-2006].

A second example of a preference aggregation rule that violates independence of irrelevant alternatives is the *Borda count* (e.g., Saari 1990)[^saari-1990]. Here, for any profile $\langle R_1, R_2 , \ldots ,R_n\rangle$ and any $x, y \in X$, $xRy$ if and only if $\sum_{i \in N} |\{z \in X : xR_i z\}| \ge \sum_{i \in N} |\{z \in X : yR_i z\}|.$ Informally, each voter assigns a score to each alternative, which depends on its rank in his or her preference ranking. The most-preferred alternative gets a score of $k$ (where $k = |X$|), the second-most-preferred alternative a score of $k - 1$, the third-most-preferred alternative a score of $k - 2$, and so on. Alternatives are then socially ordered in terms of the sums of their scores across voters: the alternative with the largest sum-total is top, the alternative with the second-largest sum-total next, and so on.

To see how this violates independence of irrelevant alternatives, consider the two profiles of individual preference orderings over four alternatives $(x, y, z, w)$ in Tables 3 and 4.

|   | *Individual 1* | *Individuals 2 to 7* | *Individuals 8 to 15* |
| --- | --- | --- | --- |
| *1ˢᵗ preference* | $y$ | $x$ | $z$ |
| *2ⁿᵈ preference* | $x$ | $z$ | $x$ |
| *3ʳᵈ preference* | $z$ | $w$ | $y$ |
| *4ᵗʰ preference* | $w$ | $y$ | $w$ |

*Table 3:* A profile of individual preference orderings

|   | *Individual 1* | *Individuals 2 to 7* | *Individuals 8 to 15* |
| --- | --- | --- | --- |
| *1ˢᵗ preference* | $x$ | $x$ | $z$ |
| *2ⁿᵈ preference* | $y$ | $z$ | $x$ |
| *3ʳᵈ preference* | $w$ | $w$ | $y$ |
| *4ᵗʰ preference* | $z$ | $y$ | $w$ |

*Table 4:* A slightly modified profile of individual preference orderings

In Table 3, the Borda scores of the four alternatives are:

- $x$: $9 \cdot 3 + 6 \cdot 4 = 51$,
- $y$: $1 \cdot 4 + 6 \cdot 1 + 8 \cdot 2 = 26$,
- $z$: $1 \cdot 2 + 6 \cdot 3 + 8 \cdot 4 = 52$,
- $w$: $1 \cdot 1 + 6 \cdot 2 + 8 \cdot 1 = 21$,

leading to a social preference for $z$ over $x$ over $y$ over $w$. In Table 4, the Borda scores are:

- $x$: $7 \cdot 4 + 8 \cdot 3 = 52$,
- $y$: $1 \cdot 3 + 6 \cdot 1 + 8 \cdot 2 = 25$,
- $z$: $1 \cdot 1 + 6 \cdot 3 + 8 \cdot 4 = 51$,
- $w$: $7 \cdot 2 + 8 \cdot 1 = 22$,

leading to a social preference for $x$ over $z$ over $y$ over $w$. The only difference between the two profiles lies in Individual 1’s preference ordering, and even here there is no change in the relative ranking of $x$ and $z$. Despite identical individual preferences between $x$ and $z$ in Tables 3 and 4, the social preference between $x$ and $z$ is reversed, a violation of independence of irrelevant alternatives.

Such violations are common in real-world voting rules, and they make preference aggregation potentially vulnerable to strategic voting and/or strategic agenda setting. In Section 3.5, I illustrate this in the case of strategic voting.

### 3.4 The liberal paradox

Although the weak Pareto principle is arguably one of the least contentious ones of Arrow’s conditions, Sen (1970a)[^sen-1970a] offered a critique of it that applies when the aggregation rule is interpreted not as a voting method, but as a social evaluation method which a social planner can use to rank social alternatives in an order of social desirability. Here, the alternatives are understood not as coarse-grained electoral options but as more richly specified states of society. Sen showed that, in this setting, the Pareto principle conflicts with a ‘liberal’ principle, which—he suggested—a social planner ought to respect.

The liberal principle requires that each individual be given some basic rights, to the effect that his or her preferences are sometimes socially decisive (i.e., cannot be overridden by others’ preferences). Intuitively, each individual has a personal sphere in which this individual alone should be able to decide what happens. To give a trivial example, I alone should be able to decide whether I sleep on my right side or on my left side, and the same should be true for everyone else. So, if two social alternatives, $x$ and $y$, differ only with respect to the side on which individual $i$ sleeps, then individual $i$’s preference between $x$ and $y$ should determine the social preference between $x$ and $y$. (Recall that alternatives are here understood as richly specified states of society.) Sen’s ‘minimal liberal’ requirement says that at least two individuals in society should have such a decisiveness right between two alternatives each. The requirement is ‘minimal’ because we would ideally want not just two individuals, but everyone to have such rights, and we would ideally want those rights to concern more than a single pair of alternatives each.

> *Minimal liberalism*: There are at least two distinct individuals $i, j \in N$ who are each decisive on at least one pair of alternatives; i.e., there is at least one pair of (distinct) alternatives $x, y \in X$ such that, for every profile $\langle R_1, R_2 , \ldots ,R_n\rangle$, $xP_i y$ implies $xPy$, and $yP_i x$ implies $yPx,$ and at least one pair of (distinct) alternatives $x^*, y^* \in X$ such that, for every profile $\langle R_1, R_2 , \ldots ,R_n\rangle$, $x^*P_j y^*$ implies $x^*Py^*,$ and $y^*P_jx^*$ implies $y^*Px^*.$

To illustrate the conflict between minimal liberalism and the weak Pareto principle, Sen asked us to imagine a society that consists of two individuals, Lewd and Prude, faced with the decision of who among them (if any) should read a controversial book, *Lady Chatterley’s Lover*. In Sen’s story, Lewd most prefers that Prude read the book (alternative $x)$, second-most prefers that he (Lewd) read the book himself (alternative $y)$, and least prefers that neither of the two read the book $(z)$. Prude most prefers that neither read the book $(z)$, second-most prefers that he (Prude) read the book himself $(x)$, and least prefers that Lewd read the book $(y)$. Assuming Lewd is decisive over the pair $y$ and $z$, society should prefer $y$ to $z$. Assuming Prude is decisive over the pair $x$ and $z$, society should prefer $z$ to $x$. But since Lewd and Prude both prefer $x$ to $y$, the weak Pareto principle (applied to $N = \{$Lewd, Prude$\})$ implies that society should prefer $x$ to $y$. So, we are faced with a social preference cycle: $x$ is socially preferred to $y, y$ is socially preferred to $z$, and $z$ socially preferred to $x$. Sen generalized this problem—now known as the ‘liberal paradox’—as follows.

> *Theorem* (Sen 1970a)[^sen-1970a]: There exists no preference aggregation rule satisfying universal domain, acyclicity of social preferences, the weak Pareto principle, and minimal liberalism.

This result suggests that if we wish to respect individual rights, we may sometimes have to sacrifice Paretian efficiency. Hence, Sen’s spoke of the ‘impossibility of a Paretian liberal’. An alternative conclusion is that the weak Pareto principle can be rendered compatible with minimal liberalism only if the domain of admissible preference profiles is suitably restricted, for instance to preferences that are ‘tolerant’ or not ‘meddlesome’ (Blau 1975; Craven 1982; Gigliotti 1986; Sen 1983)[^blau-1975][^craven-1982][^gigliotti-1986][^sen-1983]. Lewd’s and Prude’s preferences in Sen’s example are ‘meddlesome’. Each of them ‘meddles’ with the other’s private sphere.

However, several authors have challenged the relevance of Sen’s result, by arguing that his ‘minimal liberalism’ condition uses an inadequate formalization of the notion of individual rights (e.g., Gaertner, Pattanaik, and Suzumura 1992; Dowding and van Hees 2003)[^dowding-2003][^gaertner-1992].

### 3.5 The Gibbard-Satterthwaite theorem

So far we have discussed *preference aggregation rules*, which map profiles of individual preference orderings to social preference relations. We now consider *social choice rules*, whose output, instead, is one or several winning alternatives. Formally, a *social choice rule*, $f$, is a function that assigns to each profile $\langle R_1, R_2 , \ldots ,R_n\rangle$ (in some domain of admissible profiles) a social choice set $f(R_1, R_2 , \ldots ,R_n) \subseteq X$. A social choice rule $f$ can be derived from a preference aggregation rule $F$, by defining $f(R_1, R_2 , \ldots ,R_n) = \{x \in X$ : for all $y \in X$, $xRy\}$ where $R = F(R_1, R_2 , \ldots ,R_n)$; the reverse does not generally hold. We call the set of sometimes-chosen alternatives the *range* of $f$.[^note-6]

The *Condorcet winner criterion* defines a social choice rule, where, for each profile $\langle R_1, R_2 , \ldots ,R_n\rangle$, $f(R_1, R_2 , \ldots ,R_n)$ contains every alternative in $X$ that wins or at least ties with every other alternative in pairwise majority voting. As shown by Condorcet’s paradox, this may produce an empty choice set. By contrast, plurality rule and the Borda count induce social choice rules that always produce non-empty choice sets. They also satisfy the following basic conditions (the last for $|X| \ge 3)$:

> *Universal domain*: The domain of $f$ is the set of all logically possible profiles of complete and transitive individual preference orderings.
>
> *Non-dictatorship*: There does not exist an individual $i \in N$ such that, for all $\langle R_1, R_2 , \ldots ,R_n\rangle$ in the domain of $f$ and all $x$ in the range of $f$, $yR_i x$ where $y \in f(R_1, R_2 , \ldots ,R_n)$.[^note-7]
>
> *The range constraint*: The range of $f$ contains at least three distinct alternatives (and ideally all alternatives in $X)$.

When supplemented with an appropriate tie-breaking criterion, the plurality and Borda rules can further be made ‘resolute’:

> *Resoluteness*: The social choice rule $f$ always produces a unique winning alternative (a singleton choice set). (We then write $x = f(R_1, R_2 , \ldots ,R_n)$ to denote the winning alternative for the profile $\langle R_1, R_2 , \ldots ,R_n\rangle$.)

Surprisingly, this list of conditions conflicts with the following further requirement.

> *Strategy-proofness*: There does not exist a profile $\langle R_1, R_2 , \ldots ,R_n\rangle$ in the domain of $f$ at which $f$ is manipulable by some individual $i \in N$, where *manipulability* means the following: if $i$ submits a *false* preference ordering $R'_i$ $(\ne R_i)$, the winner is an alternative $y'$ that $i$ strictly prefers (according to $R_i)$ to the alternative $y$ that would win if $i$ submitted the *true* preference ordering $R_i$.[^note-8]
>
> *Theorem* (Gibbard 1973; Satterthwaite 1975)[^gibbard-1973][^satterthwaite-1975]: There exists no social choice rule satisfying universal domain, non-dictatorship, the range constraint, resoluteness, and strategy-proofness.

This result raises important questions about the trade-offs between different requirements on a social choice rule. A dictatorship, which always chooses the dictator’s most preferred alternative, is trivially strategy-proof. The dictator obviously has no incentive to vote strategically, and no-one else does so either, since the outcome depends only on the dictator.

To see that the Borda count violates strategy-proofness, recall the example of Tables 3 and 4 above. If Individual 1 in Table 3 truthfully submits the preference ordering $yP_1 xP_1 zP_1 w$, the Borda winner is $z$, as we have seen. If Individual 1 falsely submits the preference ordering $xP_1 yP_1 wP_1 z$, as in Table 4, the Borda winner is $x$. But Individual 1 prefers $x$ to $z$ according to his or her true preference ordering (in Table 3), and so he or she has an incentive to vote strategically.

Moulin (1980)[^moulin-1980] has shown that when the domain of the social choice rule is restricted to single-peaked preference profiles, pairwise majority voting and other so-called ‘median voting’ schemes can satisfy the rest of the conditions of the Gibbard-Satterthwaite theorem. Similarly, when collective decisions are restricted to binary choices alone, which amounts to dropping the range constraint, majority voting satisfies the rest of the conditions. Other possible escape routes from the theorem open up if resoluteness is dropped. In the limiting case in which all alternatives are always chosen, the other conditions are vacuously satisfied.

The requirement of strategy-proofness has been challenged too. One line of argument is that, even when there exist strategic incentives in the technical sense of the Gibbard-Satterthwaite theorem, individuals will not necessarily act on them. They would require *detailed information* about others’ preferences and *enough computational power* to figure out what the optimal strategically modified preferences would be. Neither requirement is generally met. Bartholdi, Tovey, and Trick (1989) showed that, due to computational complexity, some social choice rules are resistant to strategic manipulation: it may be an NP-hard problem for a voter to determine how to vote strategically. In this vein, Harrison and McDaniel (2008) provide experimental evidence suggesting that the ‘Kemeny rule’, an extension of pairwise majority voting designed to avoid Condorcet cycles, is ‘behaviourally incentive-compatible’: i.e., strategic manipulation is computationally hard.

Dowding and van Hees (2008) have argued that not all forms of strategic voting are normatively problematic. They distinguish between ‘sincere’ and ‘insincere’ forms of manipulation and argue that only the latter but not the former are normatively troublesome. Sincere manipulation occurs when a voter (i) votes for a compromise alternative whose chances of winning are thereby increased and (ii) genuinely prefers that compromise alternative to the alternative that would otherwise win. For example, in the 2000 US presidential election, supporters of Ralph Nader (a third-party candidate with little chance of winning) who voted for Al Gore to increase his chances of beating George W. Bush engaged in sincere manipulation in the sense of (i) and (ii). Plurality rule is susceptible to sincere manipulation, but not vulnerable to insincere manipulation.

## 4. The aggregation of welfare measures or qualitative ratings

One way to respond to the impossibility results of preference aggregation is to argue that mere rankings of alternatives in an order of preference provide insufficient information for making satisfactory collective decisions. The idea is that if we enrich the informational basis of social choice, we can avoid some of the negative results. This can be done in at least two ways. The first, which has received the most attention, is to replace preference orderings with richer welfare measures, which may allow interpersonal comparisons. The bulk of this section will be devoted to this proposal. A second, recently popular proposal is to replace preference orderings with qualitative ratings of the alternatives. This will be discussed at the end of the section.

### 4.1 Sen’s extension of Arrow’s framework

An assumption built into Arrow’s framework is that preferences are ordinal and not interpersonally comparable: preference orderings contain no information about each individual’s strength of preference or about how to compare different individuals’ preferences with one another. Statements such as ‘Individual 1 prefers alternative $x$ more than Individual 2 prefers alternative $y$’ or ‘Individual l prefers a switch from $x$ to $y$ more than Individual 2 prefers a switch from $x^*$ to $y^*$’ are considered meaningless.

In voting contexts, this assumption may be plausible, as we often may not be able to elicit more information from voters than their ordinal rankings of the options. But in welfare-evaluation contexts—when a social planner seeks to rank different social alternatives in an order of social welfare—the use of richer information may be justified. Sen (1970b)[^sen-1970b] generalized Arrow’s framework to incorporate such richer information.

As before, consider a set $N = \{1, 2, \ldots ,n\}$ of individuals $(n \ge 2)$ and a set $X = \{x, y, z, \ldots \}$ of social alternatives. Now each individual $i \in N$ has a *welfare function* $W_i$ over these alternatives, which assigns a real number $W_i (x)$ to each alternative $x \in X$, interpreted as a measure of $i$’s welfare under alternative $x$. Any welfare function on $X$ induces an ordering on $X$, but the converse is not true: welfare functions encode more information. A combination of welfare functions across the individuals, $\langle W_1, W_2 , \ldots ,W_n\rangle$, is called a *profile*.

A *social welfare functional* (*SWFL*), also denoted $F$, is a function that assigns to each profile $\langle W_1, W_2 , \ldots ,W_n\rangle$ (in some domain of admissible profiles) a social preference relation $R = F(W_1, W_2 , \ldots ,W_n)$ on $X$, with the familiar interpretation. Again, when $F$ is clear from the context, we write $R$ for the social preference relation corresponding to $\langle W_1, W_2 , \ldots ,W_n\rangle$. The *output* of a SWFL is similar to that of a preference aggregation rule (again, we do not build the completeness or transitivity of $R$ into the definition[^note-9]), but its *input* is richer.

What we gain from this depends on how much of the enriched informational input we allow ourselves to use in determining society’s preferences: technically, it depends on our assumption about measurability and interpersonal comparability of welfare.

### 4.2 Measurability and interpersonal comparability of welfare

By assigning real numbers to alternatives, welfare profiles contain a lot of information over and above the profiles of orderings on $X$ they induce. Many different assignments of *numbers* to alternatives can give rise to the same *orderings*. But we may not consider all this information meaningful. Some of it could be an artifact of the numerical representation. For example, the difference between the profile $\langle W_1, W_2 , \ldots ,W_n\rangle$ and its scaled-up version $\langle 10\cdot W_1, 10 \cdot W_2,\ldots , 10\cdot W_n\rangle$, where everything is the same in proportional terms, could be like the difference between length measurements in centimeters and in inches. The two profiles might be seen as alternative representations of the exact same information, just on different scales.

To express different assumptions about which information is truly encoded by a profile of welfare functions and which information is not (and should thus be seen, at best, as an artifact of the numerical representation), it is helpful to introduce the notion of *meaningful statements*. Some examples of statements about individual welfare that are candidates for meaningful statements are the following (the present formulations come from List 2003a; for earlier analyses, see Bossert 1991 and Bossert and Weymark 1996: Section 5)[^bossert-1991][^bossert-1996][^list-2003a]:

> *A level comparison*: Individual *i’*s welfare under alternative $x$ is at least as great as individual $j$’s welfare under alternative $y$, formally $W_i (x) \ge W_j (y)$. (The comparison is *intrapersonal* if $i = j$, and *interpersonal* if $i \ne j$.)

> *A unit comparison*: The ratio of [individual $i$’s welfare gain or loss if we switch from alternative $y_1$ to alternative $x_1$] to [individual $j$’s welfare gain or loss if we switch from alternative $y_2$ to alternative $x_2$] is $\lambda$, where $\lambda$ is some real number, formally $((W_i (x_1) - W_i (y_1)) / (W_j (x_2) - W_j (y_2)) = \lambda$. (Again, the comparison is *intrapersonal* if $i = j$, and *interpersonal* if $i \ne j$.)

> *A zero comparison*: Individual $i$’s welfare under alternative $x$ is greater than / equal to / less than zero, formally $\textit{sign}(W_i (x)) = \lambda$, where $\lambda \in \{-1, 0, 1\}$ and $\textit{sign}$ is a real-valued function that maps strictly negative numbers to $-1$, zero to 0, and strictly positive numbers to $+1$.

Arrow’s view, as noted, is that only intrapersonal level comparisons are meaningful, while all other kinds of comparisons are not. Sen (1970b)[^sen-1970b] formalized various assumptions about measurability and interpersonal comparability of welfare by (i) defining an equivalence relation on welfare profiles that specifies when two profiles count as ‘containing the same information’, and (ii) requiring any profiles in the same equivalence class to generate the same social preference ordering. Of the three kinds of comparison statements introduced above, the meaningful ones are those that are invariant in each equivalence class. Arrow’s ordinalist assumption can be expressed as follows:

> *Ordinal measurability with no interpersonal comparability (ONC)*: Two profiles $\langle W_1, W_2 , \ldots ,W_n\rangle$ and $\langle W^*_1, W^*_2,\ldots, W^*_n\rangle$ contain the same information whenever, for each $i \in N$, $W^*_i = \phi_i (W_i)$, where $\phi_i$ is some positive monotonic transformation, possibly different for different individuals.

Thus the individual welfare functions in any profile can be arbitrarily monotonically transformed (‘stretched or squeezed’) without informational loss, thereby ruling out any interpersonal comparisons or even intrapersonal unit comparisons.

If welfare is cardinally measurable but still interpersonally non-comparable, we have:

> *Cardinal measurability with no interpersonal comparability (CNC)*: Two profiles $\langle W_1, W_2 , \ldots ,W_n\rangle$ and $\langle W^*_1, W^*_2,\ldots, W^*_n\rangle$ contain the same information whenever, for each $i \in N$, $W^*_i = a_i W_i + b_i$, where the $a_i$s and $b_i$s are real numbers (with $a_i \gt 0)$, possibly different for different individuals.

Here, each individual’s welfare function is unique up to positive affine transformations (‘scaling and shifting’), but there is still no common scale across individuals. This renders intrapersonal level and unit comparisons meaningful, but rules out interpersonal comparisons and zero comparisons.

Interpersonal level comparability is achieved under the following enriched variant of ordinal measurability:

> *Ordinal measurability with interpersonal level comparability (OLC)*: Two profiles $\langle W_1, W_2 , \ldots ,W_n\rangle$ and $\langle W^*_1, W^*_2,\ldots, W^*_n\rangle$ contain the same information whenever, for each $i \in N$, $W^*_i = \phi(W_i)$, where $\phi$ is the same positive monotonic transformation for all individuals.

Here, a profile of individual welfare functions can be arbitrarily monotonically transformed (‘stretched or squeezed’) without informational loss, but the same transformation must be used for all individuals, thereby rendering interpersonal level comparisons meaningful.

Interpersonal unit comparability is achieved under the following enriched variant of cardinal measurability:

> *Cardinal measurability with interpersonal unit comparability (CUC)*: Two profiles $\langle W_1, W_2 , \ldots ,W_n\rangle$ and $\langle W^*_1, W^*_2,\ldots, W^*_n\rangle$ contain the same information whenever, for each $i \in N$, $W^*_i = aW_i + b_i$, where $a$ is the same real number for all individuals $(a \gt 0)$ and the $b_i$s are real numbers.

Here, the welfare functions in each profile can be re-scaled and shifted without informational loss, but the same scalar multiple (though not necessarily the same shifting constant) must be used for all individuals, thereby rendering interpersonal unit comparisons meaningful.

Zero comparisons, finally, become meaningful under the following enriched variant of ordinal measurability (List 2001)[^list-2001][^list-2001-2]:

> *Ordinal measurability with zero comparability (ONC$+0)$*: Two profiles $\langle W_1, W_2 , \ldots ,W_n\rangle$ and $\langle W^*_1, W^*_2,\ldots, W^*_n\rangle$ contain the same information whenever, for each $i \in N$, $W^*_i = \phi_i (W_i)$, where $\phi_i$ is some positive monotonic and zero-preserving transformation, possibly different for different individuals. (Here *zero-preserving* means that $\phi_i(0) = 0$.)

This allows arbitrary stretching and squeezing of individual welfare functions without informational loss, *provided the welfare level of zero remains fixed*, thereby ensuring zero comparability.

Several other measurability and interpersonal comparability assumptions have been discussed in the literature. The following ensures the meaningfulness of interpersonal comparisons of both levels and units:

> *Cardinal measurability with full interpersonal comparability (CFC)*: Two profiles $\langle W_1, W_2 , \ldots ,W_n\rangle$ and $\langle W^*_1, W^*_2,\ldots, W^*_n\rangle$ contain the same information whenever, for each $i \in N$, $W^*_i = aW_i + b$, where $a, b$ are the same real numbers for all individuals $(a \gt 0)$.

Lastly, intra- and interpersonal comparisons of all *three* kinds (level, unit, and zero) are meaningful if we accept the following:

> *Ratio-scale measurability with full interpersonal comparability (RFC)*: Two profiles $\langle W_1, W_2 , \ldots ,W_n\rangle$ and $\langle W^*_1, W^*_2,\ldots, W^*_n\rangle$ contain the same information whenever, for each $i \in N$, $W^*_i = aW_i$, where $a$ is the same real number for all individuals $(a \gt 0)$.

Which assumption is warranted depends on how welfare is interpreted. If welfare is *hedonic utility*, which can be experienced only from a first-person perspective, interpersonal comparisons are harder to justify than if welfare is the *objective satisfaction of subjective preferences or desires* (the *desire-satisfaction* view) or an *objective good or state* (an *objective-list* view). The desire-satisfaction view may render interpersonal comparisons empirically meaningful (by relating the interpersonally significant maximal and minimal levels of welfare for each individual to the attainment of his or her most and least preferred alternatives), but arguably not in a normatively attractive way (Hausman 1995)[^hausman-1995]. Different individuals’ most preferred alternatives may differ significantly with respect to how costly they are, for instance due to some individuals’ expensive tastes or adaptive preferences, and it is not obvious whether it is fair to treat a modest individual’s welfare under, say, a diet of cheap food as being equal to the welfare of someone who finds only caviar satisfactory. Resource-based, functioning-based, or primary-goods-based currencies of welfare, by contrast, may allow interpersonal comparisons in a way that is less morally problematic.

### 4.3 Possibilities of welfare aggregation

Once we introduce interpersonal comparisons of welfare levels or units, or zero comparisons, there exist possible SWFLs satisfying the analogues of Arrow’s conditions as well as stronger desiderata. In a welfare-aggregation context, Arrow’s impossibility can therefore be traced to a lack of interpersonal comparability (for detailed analyses, see Sen 1977 and Roberts 1980)[^roberts-1980][^sen-1977].

As noted, a SWFL respects a given assumption about measurability and interpersonal comparability if, for any two profiles $\langle W_1, W_2 , \ldots ,W_n\rangle$ and $\langle W^*_1, W^*_2,\ldots, W^*_n\rangle$ that are deemed to contain the same information, we have $F(W_1, W_2 , \ldots ,W_n) = F(W^*_1, W^*_2,\ldots, W^*_n)$. Arrow’s conditions and theorem can be restated as follows:

> *Universal domain*: The domain of $F$ is the set of all logically possible profiles of individual welfare functions.
>
> *Ordering*: For any profile $\langle W_1, W_2 , \ldots ,W_n\rangle$ in the domain of $F$, the social preference relation $R$ is complete and transitive.
>
> *Weak Pareto principle*: For any profile $\langle W_1, W_2 , \ldots ,W_n\rangle$ in the domain of $F$, if for all $i\in N$ $W_i (x) \gt W_i (y)$, then $xPy$.
>
> *Independence of irrelevant alternatives*: For any two profiles $\langle W_1, W_2 , \ldots ,W_n\rangle$ and $\langle W^*_1, W^*_2,\ldots, W^*_n\rangle$ in the domain of $F$ and any $x, y \in X$, if for all $i \in N$ $W_i(x) = W^*_i(x)$ and $W_i (y) = W^*_i(y)$, then $xRy$ if and only if $xR^*y$.
>
> *Non-dictatorship*: There does not exist an individual $i \in N$ such that, for all $\langle W_1, W_2 , \ldots ,W_n\rangle$ in the domain of $F$ and all $x, y \in X, W_i (x) \gt W_i (y)$ implies $xPy$.
>
> *Theorem*: Under ONC (or CNC, as Sen 1970b has shown)[^sen-1970b], if $|X| \gt 2$, there exists no SWFL satisfying universal domain, ordering, the weak Pareto principle, independence of irrelevant alternatives, and non-dictatorship.

Crucially, however, each of OLC, CUC, and ONC$+0$ is sufficient for the existence of SWFLs satisfying all other conditions:

> *Theorem* (combining several results from the literature, as illustrated below): Under each of OLC, CUC, and ONC$+0$, there exist SWFLs satisfying universal domain, ordering, the weak Pareto principle, independence of irrelevant alternatives, and non-dictatorship (as well as stronger conditions).

Some examples of such SWFLs come from political philosophy and welfare economics. A possible SWFL under OLC is a version of Rawls’s difference principle (1971).

> *Maximin*: For any profile $\langle W_1, W_2 , \ldots ,W_n\rangle$ and any $x, y \in X$, $xRy$ if and only if $\min_{i\in N}(W_i (x)) \ge \min_{i \in N}(W_i (y))$.

While maximin rank-orders social alternatives in terms of the welfare level of the worst-off individual alone, its lexicographic extension (*leximin*), which was endorsed by Rawls himself, uses the welfare level of the second-worst-off individual as a tie-breaker when there is tie at the level of the worst off, the welfare level of the third-worst-off individual as a tie-breaker when there is a tie at the second stage, and so on. (Note, however, that Rawls focused on primary goods, rather than welfare, as the relevant ‘currency’.) This satisfies the *strong* (not just weak) *Pareto principle*, requiring that if for all $i\in N$ $W_i (x) \ge W_i (y)$, then $xRy$, and if in addition for some $i \in N$ $W_i (x) \gt W_i (y)$, then $xPy.$

An example of a possible SWFL under CUC is classical utilitarianism.

> *Utilitarianism*: For any profile $\langle W_1, W_2 , \ldots ,W_n\rangle$ and any $x, y \in X$, $xRy$ if and only if $W_1 (x) + W_2 (x) + \ldots + W_n (x) \ge W_1 (y) + W_2 (y) + \ldots + W_n (y)$.

Finally, an example of a possible SWFL under ONC$+0$ is a variant of a frequently used, though rather simplistic poverty measure.

> *A head-count rule*: For any profile $\langle W_1, W_2 , \ldots ,W_n\rangle$ and any $x, y \in X$, $xRy$ if and only if $|\{i \in N : W_i (x) \lt 0\}| \lt |\{i \in N : W_i (y) \lt 0\}|$ or $[|\{i \in N : W_i (x) \lt 0\}| = |\{i \in N : W_i (y) \lt 0\}|$ and $xR_jy],$ where $j \in N$ is some antecedently fixed tie-breaking individual.

While substantively less compelling than maximin or utilitarian rules, head-count rules require only zero-comparability of welfare (List 2001)[^list-2001][^list-2001-2].

An important conclusion, therefore, is that Rawls’s difference principle, the classical utilitarian principle, and even the head-count method of poverty measurement can all be seen as solutions to Arrow’s aggregation problem that become possible once we go beyond Arrow’s framework of ordinal, interpersonally non-comparable preferences.

Under CFC, one can provide a simultaneous characterization of Rawlsian maximin and utilitarianism (Deschamps and Gevers 1978)[^deschamps-1978]. It uses two additional axioms. One, *minimal equity*, requires (in the words of Sen 1977: 1548)[^sen-1977] ‘that a person who is going to be best off anyway does not *always* strictly have his way’, and another, *separability*, requires that two welfare profiles that coincide for some subset $M \subseteq N$ while everyone in $N\setminus M$ is indifferent between all alternatives in $X$ lead to the same social ordering.

> *Theorem* (Deschamps and Gevers 1978)[^deschamps-1978]: Under CFC, any SWFL satisfying universal domain, ordering, the strong Pareto principle, independence of irrelevant alternatives, anonymity (as in May’s theorem), minimal equity, and separability is either leximin or of a utilitarian type (meaning that, except possibly when there are ties in sum-total welfare, it coincides with the utilitarian SWFL defined above).

Finally, the additional information available under RFC makes ‘prioritarian’ SWFLs possible.[^note-10] Like utilitarian SWFLs, they rank-order social alternatives on the basis of welfare sums across the individuals in $N$, but rather than summing up welfare directly, they sum up concavely transformed welfare, giving greater marginal weight to lower levels of welfare.

> *Prioritarianism*: For any profile $\langle W_1, W_2 , \ldots ,W_n\rangle$ and any $x, y \in X$, $xRy$ if and only if
>
> $$ W_1^r(x) + W_2^r (x) + \ldots + W_n ^r(x) \ge W_1^r (y) + W_2^r (y) + \ldots + W_n ^r(y),$$
>
> where $0 \lt r \lt 1$.

Prioritarianism requires RFC and not merely CFC because, by design, the prioritarian social ordering for any welfare profile is not invariant under changes in welfare levels (shifting).

### 4.4 Applications

The present welfare-aggregation framework has been applied to several areas. Elements of it have been used in analyses of distributive justice (e.g., Roemer 1996)[^roemer-1996], proposed as improvements over standard cost-benefit analysis in policy-making contexts (e.g., Adler 2012, 2019)[^adler-2019], and applied to health economics (e.g., Tsuchiya and Miyamoto 2009).

The framework has also been generalized to variable-population choice problems, so as to formalize population ethics in the tradition of Parfit (1984)[^parfit-1984]. Here, we must rank-order social alternatives (e.g., possible worlds) in which different individuals exist. Let $N(x)$ denote the set of individuals existing under alternative $x$. For example, the set $N(x)$ could differ from the set $N(y)$, when $x$ and $y$ are distinct alternatives (this generalizes our previous assumption of a fixed set $N)$. The variable-population case raises questions such as whether a world with a smaller number of better-off individuals is better than, equally good as, or worse than a world with a larger number of worse-off individuals. (The focus here is on axiological questions about the relative goodness of such worlds, not normative questions about the rightness or wrongness of bringing them about.)

Parfit (1984)[^parfit-1984] and others argued that classical utilitarianism is subject to the *repugnant conclusion*: a world with a very large number of individuals whose welfare levels are barely above zero could have a larger sum-total of welfare, and therefore count as better, than a world with a smaller number of very well-off individuals.

Blackorby, Donaldson, and Bossert (e.g., 2005) have axiomatically characterized different variable-population welfare aggregation methods that avoid the repugnant conclusion and satisfy some other desiderata. One solution is the following:

> *Critical-level utilitarianism*: For any profile $\langle W_1, W_2 , \ldots ,W_n\rangle$ and any $x, y \in X$, $xRy$ if and only if
>
> $$ \sum_{i\in N(x)}[W_i (x) - c] \ge \sum_{i\in N(y)}[W_i(y) - c], $$
>
> where $c \ge 0$ is some ‘critical level’ of welfare above which the quality of life counts as ‘decent/good’.

Critical-level utilitarianism avoids the repugnant conclusion when the parameter $c$ is set sufficiently large. It requires stronger measurability of welfare than classical utilitarianism, since it generates a social ordering $R$ that is not generally invariant under re-scaling of welfare units or shifts in welfare levels. Even the rich setting of RFC would force the critical level $c$ to be zero, thereby collapsing critical-level utilitarianism into classical utilitarianism and making it vulnerable to the repugnant conclusion again. As Blackorby, Bossert, and Donaldson (1999: 420) note,

> ‘[s]ome information environments that are ethically adequate in fixed-population settings have ethically unattractive consequences in variable-population environments.’

Thus, in the variable-population case, a more significant enrichment of the informational basis of Arrow’s original framework is needed to avoid impossibility results.

The SWFL approach has been generalized to the case in which each individual has multiple welfare functions (e.g., a $k$-tuple of them), capturing (i) multiple opinions about each individual’s welfare (e.g., Roberts 1995; Ooghe and Lauwers 2005)[^ooghe-2005][^roberts-1995] or (ii) multiple dimensions of welfare (e.g., List 2004a)[^list-2004a]. In this case, we are faced not only with issues of measurability and interpersonal comparability, but also with issues of inter-opinion or inter-dimensional comparability. To obtain compelling possibility results, comparability across both individuals and dimensions/opinions is needed. A related literature addresses multidimensional inequality measurement (for an introductory review, see Weymark 2006)[^weymark-2006].

In the philosophy of biology, the one-dimensional and multi-dimensional SWFL frameworks have been used (by Okasha 2009 and Bossert, Qi, and Weymark 2013)[^bossert-2013][^okasha-2009] to analyse the notion of group fitness, defined as a function of individual fitness indicators.

### 4.5 From rankings to ratings

A distinct way of amending the informational basis of social choice, which is also feasible in electoral contexts, is to ask voters to express qualitative ratings, rather than rankings, of the alternatives. Two such proposals have received particular attention: first, ‘approval voting’, and secondly, more general forms of ‘grade aggregation’.

Approval voting only modifies rather than enriches the informational basis of social choice. Here, individuals indicate which alternatives they approve of, where ‘approving’ can mean something like saying ‘yes’ to an alternative, or ‘good’, or ‘satisfactory’. Each individual can approve of as many or as few alternatives as he or she wishes. This partitions the set of alternatives into two subsets: the approved and the non-approved ones. Alternatives are not fully ranked from top to bottom. Formally, for each individual $i \in N$, let $A_i$ be the subset of $X$ consisting of those alternatives which individual $i$ approves of. Then the set $X\setminus A_i$ contains the non-approved alternatives. Call $A_i$ individual $i$’s *approval ballot*. The task is to find a way of aggregating any given profile of approval ballots, $\langle A_1, A_2 , \ldots ,A_n\rangle$, into a collective outcome, which also takes the form of a subset of $X$, consisting of the collectively approved or winning alternatives. Thus an *aggregation rule* is a function $f$ that assigns to each profile $\langle A_1, A_2 , \ldots ,A_n\rangle$ (typically in the domain of all possible approval ballots) a subset of $X$, denoted $f(A_1, A_2 , \ldots ,A_n)$.

Brams and Fishburn (1978, 1983)[^fishburn-1978] proposed the following aggregation rule, which they called *approval voting*: for each profile $\langle A_1, A_2 , \ldots ,A_n\rangle$, the set $f(A_1, A_2 , \ldots ,A_n)$ of winning alternatives consists of all those alternatives that receive the largest number of individual approvals, i.e., all those alternatives $x \in X$ such that, for every other alternative $y \in X$, $|\{i \in N : x \in A_i\}| \ge |\{i \in N : y\in A_i\}|.$

We can think of approval voting as a generalization of plurality rule. Under plurality rule, each voter votes for only one alternative—normally his or her most preferred one—and the alternative with the largest number of votes wins (or if there are several alternatives with an equal largest number of votes, they are tied for winning). Under approval voting, each voter can instead vote for any number of alternatives; again, the alternative with the most votes wins (or there may be ties). Plurality rule is like approval voting with a domain restriction to approval ballots in which each voter may approve of only one alternative. While it may seem counterintuitive to allow different voters to vote for different numbers of alternatives, note that approving of more alternatives does not necessarily give a voter more influence. In the limit, approving of all alternatives is equivalent to abstaining or approving of none of them, since such an approval ballot makes no difference to the relative vote tallies. Approval voting can also be interpreted as implementing a form of ‘yes’/‘no’ or ‘pass’/‘fail’ grading of the alternatives. For an alternative to ‘win’ or to be collectively ‘approved’, it must secure a maximal number of ‘yes’ or ‘pass’ grades.

There is some debate on whether approval voting incentivizes voters to express their evaluations of the alternatives truthfully. If the individuals’ underlying preferences are *dichotomous* (i.e., they each partition the alternatives into only two indifference classes, namely the preferred and the dispreferred alternatives), then approval voting is strategy-proof, and each voter has an incentive to vote for all and only his or her preferred alternatives (Brams and Fishburn 1978)[^brams-1978][^fishburn-1978]. However, if preferences aren’t dichotomous, then approval voting loses this property (Niemi 1984)[^niemi-1984]. The real-world strategic incentives under approval voting thus depend on the structure of the voters’ preferences.

Approval voting can be axiomatically characterized in terms of adjusted versions of May’s four condition, extended to the setting of approval balloting. Specifically, approval voting is the unique aggregation rule for approval ballots that satisfies universal domain, neutrality, positive responsiveness, and a strengthened version of anonymity called ‘optionwise anonymity’ (Goodin and List 2006)[^goodin-2006]. The latter condition formalizes a principle that Brams and Fishburn informally describe as follows: ‘In effect, the principle of “one person, one vote” under plurality voting becomes the principle of “one candidate, one vote” under approval voting. That is, each voter makes judgments about every candidate under approval voting, so the tie-in of a vote is not to the voter but rather to the candidate’ (Brams and Fishburn 1983: 12)[^brams-1983]. For other axiomatic characterizations, see Fishburn (1978, 1988)[^fishburn-1978][^fishburn-1988] and Sertel (1988)[^sertel-1988]. For extensions of approval voting to settings in which voters express not only approvals but also full rankings of the alternatives, see Brams and Sanver (2009).

While approval voting implements a form of ‘yes’/‘no’ or ‘pass’/‘fail’ grading of the alternatives, a more general grading-based approach to social choice has been advocated by Balinski and Laraki (2007, 2011). Under their proposal, voters each assign grades to the alternatives, drawn for instance from the familiar spectrum of school grades A, B, C etc., and these grades are then aggregated into collective grades, on the basis of which a winning alternative can be chosen. Their preferred version of this proposal—which they call ‘majority judgment’—defines each alternative’s collective grade as a *median grade* relative to the individually assigned grades, i.e., a grade that divides the individuals into an equal number whose grade is no lower and an equal number whose grade is no higher. For instance, if an alternative receives the grades A, B, B, E, and E from a group of five individuals, then the median grade is B. When the number of individuals is even, there could be an interval of median or ‘middlemost’ grades. An attractive feature of this way of defining the collective grade is that ‘every grade other than a grade in the middlemost interval is condemned by an absolute majority of the judges as being either too high or too low’ (Balinski and Laraki 2007: 8723). Balinski and Laraki further argue that this proposal would lead voters to express considered evaluations of the alternatives in an intuitively intelligible format and incentivize truthfulness, as discussed below.

To formalize this, let $S$ be the set of all available grades (‘$S$’ for grading scale), where $S$ is non-empty and linearly ordered from highest to lowest. For instance, $S$ could be $\{$A, B, C, D, E$\}$ or $\{ \text{Distinction,}$ $\text{Merit,}$ $\text{Pass,}$ $\text{Fail}\}.$ Each individual $i$’s *assignment of grades* to the alternatives in $X$ is a function $G_i$ that assigns to each element $x \in X$ a grade $G_i (x)$ from the set $S$. A combination of grade assignments across the individuals in $N$, $\langle G_1, G_2 , \ldots ,G_n\rangle$, is called a *profile of grade assignments*. A *grade aggregation rule* is a function $f$ that assigns to each profile of grade assignments $\langle G_1, G_2 , \ldots ,G_n\rangle$ (in some domain of admissible ones) a collective grade assignment $G = f(G_1, G_2 , \ldots ,G_n)$, where, for each $x \in X, G(x)$ is the collective grade for $x$.

Balinski and Laraki propose several conditions that a satisfactory grade aggregation rule should satisfy. In particular, they suggest that $f$ should be (i) defined for the *universal domain* of all possible profiles of individual grade assignments; (ii) *neutral* in the familiar sense of treating all alternatives equally; (iii) *anonymous* in the equally familiar sense of treating all voters equally; (iv) *unanimous* in the sense that if all individuals assign the same grade to an alternative, this becomes the collective grade; (v) *monotonic* in the sense that if some individuals raise their grade for an alternative (other grades remaining equal), this doesn’t lower the resulting collective grade, and if all individuals raise the grade, this correspondingly raises the collective grade; (vi) *independent of irrelevant alternatives* in the sense that the collective grade for any alternative depends only on the individual grades for that alternative, not on the individual grades for other alternatives, and (vii) *continuous* (which becomes relevant when $S$ is a subset of the real numbers) in the sense that small changes in the individual grades for an alternative lead only to small changes in the collective grade. A grade aggregation rule that satisfies conditions (i) to (vii) is called a *social grading function*.

Balinski and Laraki show that, among the social grading functions, the so-called ‘order methods’ stand out. For any given profile of individual grade assignments $\langle G_1, G_2 , \ldots ,G_n\rangle$, an *order method* (with parameter $k)$ assigns to each alternative $x \in X$ the $k$ᵗʰ highest grade the alternative has been individually assigned, i.e., the $k$ᵗʰ highest grade in the list $G_1 (x), G_2 (x), \ldots ,G_n (x)$. The most salient example of an order method is the *median method*, already mentioned above, which assigns to each option the median grade it has been individually assigned. This is the order method with parameter $k = (n+1)/2$, when $n$ is odd. (When $n$ is even, the definition requires some adjustment.) The following result holds:

> *Theorem* (Balinski and Laraki 2007): A social grading function is strategy-proof in grading if and only if it is an order method.

Here, a grade aggregation rule is said to be *strategy-proof in grading* if it satisfies two conditions: first, when an individual’s grade for an alternative $x \in X$ is higher than the collectively assigned grade, then this individual can at most lower (and never raise) the collective grade for $x$ by unilaterally changing his or her individual grade; and second, when an individual’s grade for an alternative $x \in X$ is lower than the collectively assigned grade, then this individual can at most raise (and never lower) the collective grade for $x$ by unilaterally changing his or her individual grade. Strategy-proofness in grading means that, when the goal is to assign collective grades to the alternatives in $X$ and voters each seek to achieve collective grades that are as close as possible to their individual grades, they will not be incentivized to misrepresent their grades. In short, truthful expression of grades will be a (weakly) dominant strategy.

However, incentives to vote strategically may reoccur if the collectively assigned grades are used to choose one of the alternatives. As Balinski and Laraki point out, ‘[w]hen rank orderings are the principal goal instead of grades, the strategic behavior of the judges may change’ (2007: 8724), and *strategy-proofness in ranking* as opposed to *strategy-proofness in grading* is not achievable in a social grading function (*ibid.*), a result somewhat analogous to the Gibbard-Satterthwaite theorem. Note further that the collective grades alone are often insufficient to determine a unique winning alternative; two or more alternatives might each receive the same top grade. This raises to question of how to break such ties in the grades, and a number of possible criteria have been proposed. For discussion, see Fabre (2021)[^fabre-2021].

The key challenge for the grading-based approach to social choice is to ensure that the grades have a common meaning for all voters. Unless an ‘A’-grade, for instance, has the same meaning for all voters, the entire exercise of aggregating individually assigned grades would not be meaningful. Some voters might be tougher graders than others, and it will then not be possible to infer that an ‘A’-grade from one voter is a stronger quality signal than a ‘B’-grade from another. Just as Sen’s SWFL approach avoids the impossibility results of social choice only if we can assume interpersonal comparability of welfare, so the grading-based approach allows us to make meaningful social choices only if grades are interpersonally comparable in an appropriate sense. For a technical development of this critique of the grading-based approach, see Morreau (2016)[^morreau-2016].

## 5. The aggregation of judgments

The objective of a collective decision need not always be the choice of a winning alternative or the ranking of several alternatives in an order of social preference. Rather, many decision-making bodies have to aggregate individual sets of judgments on multiple, logically connected propositions into collective sets of judgments.

A court may have to judge whether a defendant is liable for breach of contract on the basis of whether there was a valid contract in place and whether there was a breach. An expert panel may have to judge whether atmospheric greenhouse-gas concentrations will exceed a particular threshold by 2050, whether there is a causal chain from greater greenhouse-gas concentrations to temperature increases, and whether the temperature will increase. Legislators may have to judge whether a particular end is socially desirable, whether a proposed policy is the best means for achieving that end, and whether to pursue that policy.

In each case, the ‘aggreganda’ are not simply preference orderings, welfare assignments, or ratings over some set of alternatives, as in the models discussed in the previous sections. Rather, the ‘aggreganda’ are entire systems of judgments or beliefs on some interconnected issues. The theory of judgment aggregation represents them using formal logic. At the end of this section, we also briefly consider the aggregation of probabilistic judgments or credences.

### 5.1 The paradoxes of judgment aggregation

The contemporary field of judgment-aggregation theory was inspired by a series of ‘paradoxes’, with which we begin. Kornhauser and Sager (1986) described the following problem, now known as the ‘doctrinal paradox’. (A structurally similar problem was discovered by Vacca 1921 and, as Elster 2013 points out, by Poisson 1837.)[^elster-2013][^poisson-1837][^vacca-1921] A three-judge court has to make judgments on the following propositions:

- $p$: The defendant was contractually obliged not to do action $X$.
- $q$: The defendant did action $X$.
- $r$: The defendant is liable for breach of contract.

According to legal doctrine, the *premises* $p$ and $q$ are jointly necessary and sufficient for the *conclusion* $r$. Suppose the individual judges hold the views shown in Table 5.

|   | *$p$ (obligation)* | *$q$ (action)* | *$r$ (liability)* |
| --- | --- | --- | --- |
| *Judge 1* | True | True | True |
| *Judge 2* | False | True | False |
| *Judge 3* | True | False | False |
| *Majority* | True | True | False |

*Table 5:* An example of the ‘doctrinal paradox’

Although each individual judge respects the relevant legal doctrine, there is a majority for $p$, a majority for $q$, and yet a majority against $r$—in breach of the legal doctrine. The court faces a dilemma: it can *either* go with the majority judgments on the premises $(p$ and $q)$ and reach a ‘liable’ verdict by logical inference (the *issue-by-issue* or *premise-based approach*); $or$ go with the majority judgment on the conclusion $(r)$ and reach a ‘not liable’ verdict, ignoring the majority judgments on the premises (the *case-by-case* or *conclusion-based approach*). The ‘doctrinal paradox’ consists in the fact that these two approaches may lead to opposite outcomes.

We can learn another lesson from this example. Relative to the legal doctrine, the majority judgments are logically inconsistent. Formally expressed, the set of majority-accepted propositions, $\{p, q$, *not r*$\}$, is inconsistent relative to the constraint $r$ *if and only if* $(p$ *and* $q)$. This observation was the starting point of the more recent, formal-logic-based literature on judgment aggregation.

The possibility of inconsistent majority judgments is not tied to the presence of a legal doctrine or other explicit side constraint (as pointed out by Pettit 2001, who called this phenomenon the ‘discursive dilemma’)[^pettit-2001]. Suppose, for example, an expert panel has to make judgments on three propositions (and their negations):

- $p$: Atmospheric CO$_2$ will exceed 600ppm by 2050.
- *if* $p$ *then* $q$: If atmospheric CO$_2$ exceeds this level by 2050, there will be a temperature increase of more than 3.5° by 2100.
- $q$: There will be a temperature increase of more than 3.5° by 2100.

If individual judgments are as shown in Table 6, the majority judgments are inconsistent: despite individually consistent judgments, the set of majority-accepted propositions, $\{p$, *if* $p$ *then* $q$, *not* $q\}$, is logically inconsistent.

|   | $p$ | *if* $p$ *then* $q$ | $q$ |
| --- | --- | --- | --- |
| *Expert 1* | True | True | True |
| *Expert 2* | False | True | False |
| *Expert 3* | True | False | False |
| *Majority* | True | True | False |

*Table 6:* A majoritarian inconsistency

Note that the patterns of judgments in Tables 5 and 6 are structurally equivalent to the pattern of preferences leading to Condorcet’s paradox when we reinterpret those preferences as judgments on propositions of the form ‘$x$ is preferable to $y$’, ‘$y$ is preferable to $z$’, and so on, as shown in Table 7 (List and Pettit 2004; an earlier interpretation of preferences along these lines can be found in Guilbaud [1952] 1966)[^list-2004]. Here, the set of majority-accepted propositions is inconsistent relative to the constraint of transitivity.

|   | *‘x preferable to y’* | *‘y preferable to z’* | *‘x preferable to z’* |
| --- | --- | --- | --- |
| *Individual 1* (prefers $x$ to $y$ to $z)$ | True | True | True |
| *Individual 2* (prefers $y$ to $z$ to $x)$ | False | True | False |
| *Individual 3* (prefers $z$ to $x$ to $y)$ | True | False | False |
| *Majority* (prefers $x$ to $y$ to $z$ to $x$, a ‘cycle’) | True | True | False |

*Table 7:* Condorcet’s paradox, propositionally reinterpreted

A general combinatorial result subsumes all these phenomena. Call a set of propositions *minimal inconsistent* if it is a logically inconsistent set, but all its proper subsets are consistent.

> *Proposition* (Dietrich and List 2007a; Nehring and Puppe 2007)[^dietrich-2007a][^nehring-2007]: Propositionwise majority voting may generate inconsistent collective judgments if and only if the set of propositions (and their negations) on which judgments are to be made has a minimal inconsistent subset of three or more propositions.

In the examples of Tables 6, 5, and 7, the minimal inconsistent sets of size (at least) three are: $\{p$, *if p then q*, *not q*$\}$, which is minimal inconsistent *simpliciter*; $\{p, q$, *not r*$\}$, which is minimal inconsistent relative to the side constraint *r if and only if* (*p and q*); and $\{$‘$x$ is preferable to $y$’, ‘$y$ is preferable to $z$’, ‘$z$ is preferable to $x \textrm{'} \}$, which is minimal inconsistent relative to a transitivity constraint on preferability.

### 5.2 The basic framework and a simple impossibility result

The problem of judgment aggregation can be formalized as follows. Let $N = \{1, 2, \ldots ,n\}$ be a set of individuals $(n \ge 2)$. The propositions on which judgments are to be made are represented by sentences from propositional logic (or some other, expressively richer logic, such as a predicate, modal, or conditional logic, as discussed in Dietrich 2007)[^dietrich-2007]. We define the *agenda*, $X$, as a finite set of propositions, closed under single negation $(\neg)$.[^note-11] For example, $X$ could be $\{p, \neg p, p\rightarrow q, \neg(p\rightarrow q), q, \neg q\}$, as in the expert-panel case.

Each individual $i \in N$ has a *judgment set* $J_i$, defined as a subset $J_i \subseteq X$ and interpreted as the set of propositions that individual $i$ accepts. A judgment set is *consistent* if it is a logically consistent set of propositions[^note-12] and *complete* (relative to $X)$ if it contains a member of every proposition-negation pair $p, \neg p \in X$.

A combination of judgment sets across the individuals, $\langle J_1, J_2 , \ldots ,J_n\rangle$, is called a *profile*. A *judgment aggregation rule*, $F$, is a function that assigns to each profile $\langle J_1, J_2 , \ldots ,J_n\rangle$ (in some domain of admissible profiles) a collective judgment set $J = F(J_1, J_2 , \ldots ,J_n) \subseteq X$, interpreted as the set of propositions accepted by the group as a whole. As before, when $F$ is clear from the context, we write $J$ for the collective judgment set corresponding to $\langle J_1, J_2 , \ldots ,J_n\rangle$. Again, for generality, we build no rationality requirement on $J$ (such as consistency or completeness) into the definition of a judgment aggregation rule.

The simplest example of a judgment aggregation rule is *propositionwise majority voting*. Here, for any profile $\langle J_1, J_2 , \ldots ,J_n\rangle,$ $J = \{p \in X : |\{i \in N : p \in J_i\}| \gt n/2\}$. As we have seen, this may produce inconsistent collective judgments.

Consider the following conditions on an aggregation rule:

> *Universal domain*: The domain of $F$ is the set of all logically possible profiles of consistent and complete individual judgment sets.
>
> *Collective rationality*: For any profile $\langle J_1, J_2 , \ldots ,J_n\rangle$ in the domain of $F$, the collective judgment set $J$ is consistent and complete.
>
> *Anonymity*: For any two profiles $\langle J_1, J_2 , \ldots ,J_n\rangle$ and $\langle J^*_1, J^*_2, \ldots ,J^*_n\rangle$ that are permutations of each other, $F(J_1, J_2 , \ldots ,J_n) = F(J^*_1, J^*_1, \ldots ,J^*_n)$.
>
> *Systematicity*: For any two profiles $\langle J_1, J_2 , \ldots ,J_n\rangle$ and $\langle J^*_1, J^*_2, \ldots ,J^*_n\rangle$ in the domain of $F$ and any $p, q \in X$, if for all $i \in N$, $p \in J_i$ if and only if $q \in J^*_i$, then $p \in J$ if and only if $q \in J^*.$

The first three conditions are analogous to universal domain, ordering, and anonymity in preference aggregation. The last is the counterpart of independence of irrelevant alternatives, though stronger: it requires that (i) the collective judgment on any proposition $p \in X$ (of which a binary ranking proposition such as ‘$x$ is preferable to $y$’ is a special case) depend only on individual propositions on $p$ (the *independence* part), and (ii) the pattern of dependence between individual and collective judgments be the same across all propositions in $X$ (the *neutrality* part). Formally, *independence* is the special case with quantification restricted to $p = q$. Propositionwise majority voting satisfies all these conditions, except the consistency part of collective rationality.

> *Theorem* (List and Pettit 2002)[^list-2002]: If $\{p, q, p\wedge q\} \subseteq X$ (where $p$ and $q$ are mutually independent propositions and ‘$\wedge$’ can also be replaced by ‘$\vee$’ or ‘$\rightarrow$’), there exists no judgment aggregation rule satisfying universal domain, collective rationality, anonymity, and systematicity.

Like other impossibility theorems, this result is best interpreted as describing the trade-offs between different conditions on an aggregation rule. The result has been generalized and strengthened in various ways, beginning with Pauly and van Hees’s (2006) proof that the impossibility persists if anonymity is weakened to non-dictatorship (for other generalizations, see Dietrich 2006 and Mongin 2008)[^dietrich-2006][^dietrich-2008][^dietrich-2008-2][^mongin-2008].

### 5.3 More general impossibility results

As we have seen, in preference aggregation, the ‘boundary’ between possibility and impossibility results is easy to draw: when there are only two decision alternatives, all of the desiderata on a preference aggregation rule reviewed above can be satisfied (and majority rule does the job); when there are three or more alternatives, there are impossibility results. In judgment aggregation, by contrast, the picture is more complicated. What matters is not the number of propositions in $X$ but the nature of the logical interconnections between them.

Impossibility results in judgment aggregation have the following generic form: for a given class of agendas, the aggregation rules satisfying a particular set of conditions (usually, a domain condition, a rationality condition, and some responsiveness conditions) are non-existent or degenerate (e.g., dictatorial). Different kinds of agendas trigger different instances of this scheme, with stronger or weaker conditions on the aggregation rule leading to an impossibility depending on the properties of the agenda. The significance of combinatorial properties of the agenda was first discovered by Nehring and Puppe (2002, Other Internet Resources) in a mathematically related but interpretationally distinct framework (strategy-proof social choice over so-called property spaces). Three kinds of agenda stand out:

> *A non-simple agenda*: $X$ has a minimal inconsistent subset of three or more propositions.
>
> *A pair-negatable agenda*: $X$ has a minimal inconsistent subset $Y$ that can be rendered consistent by negating a pair of propositions in it. (Equivalently, $X$ is not isomorphic to a set of propositions whose only connectives are $\neg$ and $\leftrightarrow$ in standard propositional logic; see Dokow and Holzman 2010a.)[^dokow-2010a]
>
> *A path-connected agenda* (or *totally blocked*, in Nehring and Puppe 2002, Other Internet Resources): Any pair of contingent propositions in $X$ is connected by a path of conditional entailments. Formally, for any contingent $p, q \in X$, there exist $p_1, p_2 , \ldots ,p_k \in X$ with $p_1 = p$ and $p_k = q$ such that $p_1$ conditionally entails $p_2, p_2$ conditionally entails $p_3,\ldots$, and $p_{k-1}$ conditionally entails $p_k$. (Here, $p_i$ *conditionally entails* $p_j$ if $p_i \cup Y$ entails $p_j$ for some $Y \subseteq X$ consistent with each of $p_i$ and $\neg p_j$; and $p$ is *contingent* if neither $\{p\}$, nor $\{\neg p\}$ is logically inconsistent.)

Some agendas have two or more of these properties. The agendas in our ‘doctrinal paradox’ and ‘discursive dilemma’ examples are both non-simple and pair-negatable. To illustrate, take the agenda from the expert-panel example, $X = \{p, \neg p, p\rightarrow q, \neg(p\rightarrow q), q, \neg q\}$. It is non-simple, because it has a minimal inconsistent subset of size 3, namely $\{p, p\rightarrow q, \neg q\}$, and it is pair-negatable, because it has a minimal inconsistent subset, namely $Y = \{p, p\rightarrow q, \neg q\}$, in which we can find a pair of propositions, namely $\{p, \neg q\}$, such that if we replace these with their negations in $Y$, the resulting set is consistent (note that $\{\neg p, p\rightarrow q, q\}$ is consistent). An example of an agenda which has all three combinatorial properties is the *preference agenda*, $X = \{$‘$x$ is preferable to $y$’, ‘$y$ is preferable to $x$’, ‘$x$ is preferable to $z$’, ‘$z$ is preferable to $x$’, $\ldots \}$, assuming preferability is transitive and complete and there are three or more alternatives $x, y, z, \ldots$, over which preferability is defined. The following result holds:

> *Theorem* (Dietrich and List 2007b; Dokow and Holzman 2010a; building on Nehring and Puppe 2002, Other Internet Resources)[^dietrich-2007b][^dokow-2010a]: If $X$ is non-simple, pair-negatable, and path-connected, there exists no judgment aggregation rule satisfying universal domain, collective rationality, independence, unanimity preservation (requiring that, for any unanimous profile $\langle J, J, \ldots ,J\rangle,$ $F(J, J, \ldots ,J) = J)$, and non-dictatorship.[^note-13]

Applied to the preference agenda, this result yields Arrow’s theorem (for strict preference orderings) as a corollary (for a precursor result, see Nehring 2003)[^nehring-2003].[^note-14] Thus Arrovian preference aggregation can be reinterpreted as a special case of judgment aggregation.

The literature contains several variants of this theorem. One variant drops the agenda property of path-connectedness and strengthens independence to systematicity. A second variant drops the agenda property of pair-negatability and imposes a monotonicity condition on the aggregation rule (requiring that additional support never hurt an accepted proposition) (Nehring and Puppe 2010, reformulating a result from Nehring and Puppe 2002, Other Internet Resources)[^nehring-2010]. A final variant drops both path-connectedness and pair-negatability while imposing both systematicity and monotonicity (*ibid.*).

In each case, the agenda properties are not only sufficient but also (if $n \ge 3)$ necessary for the result (Nehring and Puppe 2002 [Other Internet Resources], 2010; Dokow and Holzman 2010a)[^dokow-2010a]. Note also that path-connectedness implies non-simplicity. Therefore, non-simplicity need not be listed among the theorem’s conditions, though it is needed in the variants dropping path-connectedness.

### 5.4 Possibilities of judgment aggregation

#### 5.4.1 Relaxing universal domain

As in preference aggregation, one way to avoid the present impossibility results is to relax universal domain. If the domain of admissible profiles of individual judgment sets is restricted to those satisfying specific ‘cohesion’ conditions, propositionwise majority voting produces consistent collective judgments.

The simplest cohesion condition is *unidimensional alignment* (List 2003b)[^list-2003b]. A profile $\langle J_1, J_2 , \ldots ,J_n\rangle$ is *unidimensionally aligned* if the individuals in $N$ can be ordered from left to right (e.g., on some cognitive or ideological dimension) such that, for every proposition $p \in X$, the individuals accepting $p$ (i.e., those with $p \in J_i)$ are either all to the left, or all to the right, of those rejecting $p$ (i.e., those with $p \not\in J_i)$. Table 8 gives an example. Here the individuals are ordered from left to right in the order 1-2-3-4-5, and for each proposition the individuals accepting the proposition (corresponding to the ‘True’ entries in the table) are on the opposite side of those rejecting the proposition (corresponding to the ‘False’ entries). For any profile satisfying this condition, the majority judgments coincide with the judgments of the median individual relative to the given left-right ordering (if $n$ is odd) (individual 3 in Table 8), or with the intersection of the judgment sets of the two middle individuals (if $n$ is even). Assuming individual judgments are consistent, the majority judgments then inherit their consistency. By implication, on unidimensionally aligned domains, propositionwise majority voting will satisfy the rest of the conditions on judgment aggregation rules reviewed above (assuming there are no majority ties).

|   | *Individual 1* | *Individual 2* | *Individual 3* | *Individual 4* | *Individual 5* |
| --- | --- | --- | --- | --- | --- |
| $p$ | True | True | False | False | False |
| $q$ | True | True | True | True | False |
| $r$ | False | False | False | True | True |
| $p \wedge q \wedge r$ | False | False | False | False | False |

*Table 8:* Unidimensional alignment

In analogy with the case of single-peakedness in preference aggregation, several less restrictive conditions already suffice for consistent majority judgments. One such condition (introduced in Dietrich and List 2010a, where a survey is provided)[^dietrich-2010a] generalizes Sen’s triple-wise value-restriction. A profile $\langle J_1, J_2 , \ldots ,J_n\rangle$ is *value-restricted* if every minimal inconsistent subset $Y \subseteq X$ has a pair of elements $p, q$ such that no individual $i \in N$ has $\{p, q\} \subseteq J_i$. Value-restriction prevents any minimal inconsistent subset of $X$ from becoming majority-accepted, and hence ensures consistent majority judgments. Applied to the preference agenda, value-restriction reduces to Sen’s equally named condition.

#### 5.4.2 Relaxing collective rationality

While the requirement that collective judgments be consistent is widely accepted, the requirement that collective judgments be complete (in $X)$ is more contentious. In support of completeness, one might say that a given proposition would not be included in $X$ unless it is supposed to be collectively adjudicated. Against completeness, one might say that there are circumstances in which the level of disagreement on a particular proposition (or set of propositions) is so great that forming a collective view on it is undesirable or counterproductive.

Judgment aggregation rules violating collective completeness while satisfying (all or most of) the other conditions introduced above include: *unanimity rule*, where, for any profile $\langle J_1, J_2 , \ldots ,J_n\rangle$, $J = \{p \in X : p \in J_i$ for all $i \in N\}$; *supermajority rules*, where, for any profile $\langle J_1, J_2 , \ldots ,J_n\rangle$, $J = \{p \in X : |\{i \in N : p \in J_i\}| \gt qn\}$ for a suitable acceptance quota $q \in$ (0.5,1); and *conclusion-based rules*, where a subset $Y \subseteq X$ of logically independent propositions (and their negations) is designated as a set of conclusions and $J = \{p \in Y : |\{i \in N : p \in J_i\}| \gt n/2\}$. In the multi-member court example of Table 5, the set of conclusions is simply $Y = \{r, \neg r\}$.

Given consistent individual judgment sets, unanimity rule guarantees consistent collective judgment sets, because the intersection of several consistent sets of propositions is always consistent. Supermajority rules guarantee consistent collective judgment sets too, provided the quota $q$ is chosen to be at least $(k-1)/k$, where $k$ is the size of the largest minimal inconsistent subset of $X$ (Dietrich and List 2007a)[^dietrich-2007a]. The reason is combinatorial: any $k$ distinct supermajorities of the relevant size will always have at least one individual in common. So, for any minimal inconsistent set of propositions (which is at most of size $k)$ to be supermajority-accepted, at least one individual would have to accept all the propositions in the set, contradicting this individual’s consistency. Conclusion-based rules, finally, produce consistent collective judgment sets by construction, but always leave non-conclusions undecided.

Gärdenfors (2006)[^gärdenfors-2006] and more generally Dietrich and List (2008) and Dokow and Holzman (2010b) have shown that if—while relaxing completeness—we require collective judgment sets to be *deductively closed* (i.e., for any $p \in X$ entailed by $J$, it must be that $p \in J)$, we face an impossibility result again. For the same agendas that lead to the impossibility result reviewed in Section 5.3, there exists no judgment aggregation rule satisfying universal domain, collective consistency and deductive closure, independence, unanimity preservation, and non-oligarchy. An aggregation rule is called *oligarchic* if there is an antecedently fixed subset $M \subseteq N$ (the ‘oligarchs’) such that, for any profile $\langle J_1, J_2 , \ldots ,J_n\rangle$, $J = \{p \in X : p \in J_i$ for all $i \in M\}$. Unanimity rule and dictatorships are special cases with $M = N$ and $M = \{i\}$ for some $i \in N$, respectively.

The downside of oligarchic aggregation rules is that they either lapse into dictatorship or lead to stalemate, with the slightest disagreements between oligarchs resulting in indecision (since every oligarch has veto power on every proposition).

#### 5.4.3 Relaxing systematicity/independence

A variety of judgment aggregation rules become possible when we relax systematicity/independence. Recall that systematicity combines an independence and a neutrality requirement. Relaxing only neutrality does not get us very far, since for many agendas there are impossibility results with independence alone, as illustrated in Section 5.3.

One much-discussed class of aggregation rules violating independence consists of the *premise-based rules*. Here, a subset $Y \subseteq X$ of logically independent propositions (and their negations) is designated as a set of *premises*, as in the court example. For any profile $\langle J_1, J_2 , \ldots ,J_n\rangle , J = \{p \in X : J_Y$ entails $p\}$ where $J_Y$ are the majority-accepted propositions among the premises, formally $\{p \in Y : |\{i \in N : p \in J_i\}| \gt n/2\}$. Informally, majority votes are taken on the premises, and the collective judgments on all other propositions are determined by logical implication. If the premises constitute a logical basis for the entire agenda, a premise-based rule guarantees consistent and (absent ties) complete collective judgment sets. (For a more general definition, see Dietrich and Mongin 2010. The procedural and epistemic properties of premise-based rules are discussed, e.g., in Pettit 2001; Chapman 2002; Bovens and Rabinowicz 2006; Dietrich 2006.)[^bovens-2006][^chapman-2002][^dietrich-2006][^dietrich-2010][^dietrich-2010-2][^pettit-2001]

A generalization is given by the *sequential priority rules* (List 2004b; see Dietrich 2015 for further generalization)[^dietrich-2015][^list-2004b]. Here, for each profile $\langle J_1, J_2 , \ldots ,J_n\rangle$, the propositions in $X$ are collectively adjudicated in a fixed order of priority, for instance, a temporal or epistemic one. The collective judgment on each proposition $p \in X$ is made as follows. If the majority judgment on $p$ is consistent with collective judgments on prior propositions, this majority judgment prevails; otherwise the collective judgment on $p$ is determined by the implications of prior judgments. By construction, this guarantees consistent and (absent ties) complete collective judgments. However, it is *path-dependent*: the order in which propositions are considered may affect the outcome, specifically when the underlying majority judgments are inconsistent. For example, when this aggregation rule is applied to the profiles in Tables 5, 6, and 7 (but not 8), the collective judgments depend on the order in which the propositions are considered. Thus sequential priority rules are vulnerable to *agenda manipulation*. Similar phenomena occur in sequential pairwise majority voting in preference aggregation (e.g., Riker 1982)[^riker-1982].

Another prominent class of aggregation rules violating independence is given by the *distance-based rules* (Pigozzi 2006, building on Konieczny and Pino Pérez 2002; Miller and Osherson 2009)[^konieczny-2002][^miller-2009][^pigozzi-2006]. A distance-based rule is defined in terms of some distance metric between judgment sets, for example the *Hamming distance*, where, for any two judgment sets $J$, $J' \subseteq X$, $d(J, J') = |\{p \in X : \text{ not } [p \in J \Leftrightarrow p \in J']\}|.$ Each profile $\langle J_1, J_2 , \ldots ,J_n\rangle$ is mapped to a consistent and complete judgment set $J$ that minimizes the sum-total distance from each of the $J_i$s. (As an aside: applied to the preference agenda, the Hamming-distanced-based rule becomes equivalent to the ‘Kemeny rule’, already briefly mentioned earlier.) Distance-based rules can be interpreted as capturing the idea of identifying compromise judgments. Unlike premise-based or sequential priority rules, they do not require a distinction between premises and conclusions or any other order of priority among the propositions.

As in preference aggregation, the cost of relaxing independence is the loss of strategy-proofness. The conjunction of independence and monotonicity is necessary and sufficient for the non-manipulability of a judgment aggregation rule by strategic voting (Dietrich and List 2007c; for related results, see Nehring and Puppe 2002 [Other Internet Resources])[^dietrich-2007c]. Thus we cannot generally achieve strategy-proofness without relaxing either universal domain, or collective rationality, or unanimity preservation, or non-dictatorship. In practice, we must therefore look for ways of rendering opportunities for strategic manipulation less of a threat.

### 5.5 Probabilistic opinion pooling

A distinct and framework-transcendent way of avoiding the impossibility results of judgment aggregation is to give up the binary (‘Yes’/‘No’, ‘True’/‘False’) format of judgments and to assume that they take the form of subjective probabilities or credences. The resulting aggregation problem is that of *probabilistic opinion pooling* (Stone 1961; Aczél and Wagner 1980; Lehrer and Wagner 1981; McConway 1981; Genest and Zidek 1986; and Mongin 1995)[^acze-1980][^genest-1986][^genest-1986-2][^lehrer-1981][^mcconway-1981][^mongin-1995][^stone-1961]. Some key works on it predate the contemporary literature on ‘binary’ judgment aggregation, but the problem has recently received renewed attention.

In this probabilistic rather than binary setting, each individual $i \in N$ has an *opinion function* $Pr_i$ on a given agenda $X$ (which is here typically an algebra of propositions), where, for each $p \in X$, $Pr_i(p)$ is the subjective probability or degree of belief (a real number in the interval [0,1]) that individual $i$ assigns to $p$. The function $Pr_i$ is normally assumed to be probabilistically coherent.[^note-15] The aim is to find an *opinion pooling rule*, again denoted $F$, which assigns to each admissible profile $\langle Pr_1, Pr_2,\ldots, Pr_n\rangle$ of individual opinion functions a collective opinion function $Pr$, which should ideally also be probabilistically coherent. For each $p \in X, Pr(p)$ is interpreted as the subjective probability or degree of belief that is collectively assigned to $p$. A structurally similar aggregation problem can be found in the literature on peer disagreement, where an individual epistemic agent seeks to reconcile several potentially conflicting assignments of probabilities to some propositions—typically the agent’s own probability assignment and those of some epistemic peers—so as to arrive at an all-things-considered probability assignment (for an overview, see, e.g., Christensen and Lackey 2013)[^christensen-2013].

A classic result shows that, in this probabilistic framework, conditions similar to those leading to an impossibility in the binary case can now be non-trivially satisfied. These conditions are:

> *Universal domain*: The domain of $F$ is the set of all logically possible profiles of probabilistically coherent opinion functions on $X$.
>
> *Collective coherence*: For any profile $\langle Pr_1, Pr_2,\ldots, Pr_n\rangle$ in the domain of $F$, the collectively assigned opinion function $Pr$ on $X$ is probabilistically coherent.
>
> *Zero preservation*: For any profile $\langle Pr_1, Pr_2,\ldots, Pr_n\rangle$ and proposition $p \in X$, if $Pr_i(p) = 0$ for all $i \in N$, then the collectively assigned probability is $Pr(p) = 0$.
>
> *Independence*: For any two profiles $\langle Pr_1, Pr_2,\ldots, Pr_n\rangle$ and $\langle Pr^*_1, Pr^*_2, \ldots ,Pr^*_n\rangle$ in the domain of $F$ and any $p \in X$, if for all $i \in N$ $Pr_i(p) = Pr^*_i(p)$, then $Pr(p) = Pr^*(p)$.

The following holds:

> *Theorem* (Aczél and Wagner 1980; McConway 1981)[^acze-1980][^mcconway-1981]: Suppose $X$ is an algebra containing more than two contingent, non-equivalent proposition-negation pairs. Then a probabilistic opinion pooling rule satisfies universal domain, collective coherence, zero preservation, and independence if and only if it is a linear pooling rule.

Such a rule is defined as follows. Let $w_1, w_2 , \ldots ,w_n \ge 0$ be an assignment of weights to the $n$ individuals with $w_{1 }+ w_{2 }+ \ldots_{ }+ w_n = 1$. Then the corresponding *linear pooling rule* assigns to each profile $\langle Pr_1, Pr_2,\ldots, Pr_n\rangle$ of probabilistically coherent opinion functions the collective opinion function $Pr = w_1 Pr_1 + w_2 Pr_2 + \ldots + w_n Pr_n.$ Thus the collective probability assigned to each proposition $p \in X$ is a weighted linear average of the individual probabilities assigned to $p$. Linear pooling rules range from ones with perfectly equal weights (which thereby satisfy anonymity) to ones that concentrate all weight on one individual (i.e., dictatorships). A noteworthy lesson is that essentially the same conditions that characterize the class of dictatorial aggregation rules in the case of binary judgment aggregation now characterize the class of linear pooling rules.

At first sight, one might think that probabilistic opinion pooling is free from any troubling impossibility results. However, linear pooling, and thus any opinion pooling rule satisfying the above-stated conditions, has some defects. The first is this. Suppose we require that whenever all individuals consider two propositions $p$ and $q$ probabilistically independent (perhaps conditional on a third proposition $r)$, this probabilistic independence judgment be preserved in the collective probability assignments. A rationale for requiring this is that judgments of probabilistic independence may encode insights about which propositions (or events described by them) are causally relevant or irrelevant to which others. Unfortunately, however, linear pooling (except in its degenerate dictatorial form) does not generally preserve unanimously held conditional independence judgments (Genest and Wagner 1987)[^genest-1987], and so we would again get an impossibility result if we added this preservation requirement to our list of earlier conditions, together with non-dictatorship.

The second defect is the following. Suppose the individuals in $N$ learn some new information that prompts them to revise their opinions on the propositions in $X$, where revision takes the form of Bayesian conditionalization or some generalization of it. It is plausible to require that if we aggregate their post-revision probability assignments, the result will be the same as the one we would have got if we had first aggregated the pre-revision probability assignments and then revised the resulting collective probability assignments on the basis of the learnt information. More formally expressed, suppose $L$ is the learnt information, and suppose $Pr_1 |L, Pr_2 |L, \ldots ,Pr_n|L$ are the results of conditionalizing the $n$ individuals’ opinion functions on the new information.[^note-16] Then, assuming that all the profiles involved are in the domain of our opinion pooling rule, we require that aggregation (via $F)$ and revision (via |) commute, i.e.,

> $F(Pr_1 |L, Pr_2 |L,\ldots, Pr_n|L) = F(Pr_1, Pr_2,\ldots, Pr_n)|L$.

Again, linear pooling (except in its degenerate dictatorial form) does not generally satisfy this requirement (often called ‘external Bayesianity’), and so we would also get an impossibility result if we added it to our list of conditions, together with non-dictatorship (Madansky 1964). Subsequent work has shown that if we aggregate probabilities by geometric rather than linear averaging, we can make aggregation and revision commute (Genest 1984; Genest et al. 1986)[^genest-1984][^genest-1986][^genest-1986-2], though we must then lift the independence requirement on the opinion pooling rule. This finding has been picked up in more recent work and has sparked a small but growing philosophical literature on Bayesian group beliefs (e.g., Dietrich 2010, 2019; Russell, Hawthorne, and Buchak 2015; and Baccelli and Stewart 2020)[^baccelli-2020][^dietrich-2010][^dietrich-2019][^dietrich-2010-2][^russell-2015]. The key question here is this: under what conditions can a group whose opinions are given by aggregating its members’ opinions constitute a rational Bayesian agent?

Other work has considered probabilistic opinion pooling with general (i.e., non-algebra) agendas (Dietrich and List 2017)[^dietrich-2017] and with imprecise probabilities (Stewart and Ojea Quintana 2018)[^stewart-2018], as well as more general forms of attitude aggregation, which subsume binary judgment aggregation, probability/credence aggregation, and Arrovian preference aggregation as special cases (e.g., Dietrich and List 2010b; Dokow and Holzman 2010c)[^dietrich-2010b][^dokow-2010c].

## 6. Other topics

As should be evident, social choice theory is a vast field. Areas not covered in this entry, or mentioned only in passing, include: preference and welfare aggregation under risk and uncertainty (how to aggregate individual preferences or individual welfare into social preferences when the prospects to be ranked have risky or uncertain outcomes, to which at most probabilities can be assigned; e.g., Mongin and Pivato 2016)[^mongin-2016]; theories of fair division (how to divide one or several divisible or indivisible goods, such as cakes or houses, between several claimants; e.g., Brams and Taylor 1996 and Moulin 2004)[^brams-1996][^moulin-2004]; theories of matching (how to allocate university places to applicants or donated organs to patients; e.g., Gale and Shapley 1963; Roth and Sotomayor 1992; Klaus, Malove, and Rossi 2016)[^klaus-2016][^roth-1992]; behavioural social choice theory (analyzing empirical evidence of voting behaviour under various aggregation rules; e.g., Regenwetter et al. 2006)[^regenwetter-2006]; empirical social choice theory (analysing surveys and experiments on people’s intuitions about distributive justice; e.g., Gaertner and Schokkaert 2012)[^gaertner-2012]; topological social choice theory (studying social-choice-theoretic questions using tools from mathematical topology; e.g., Chichilnisky 1980; Heal 1997)[^chichilnisky-1980][^heal-1997]; computational social choice theory (analysing computational properties of aggregation rules, including their computational complexity; e.g., Bartholdi, Tovey, and Trick 1989; Brandt, Conitzer, and Endriss 2013)[^bartholdi-1989][^brandt-2013]; the study of collective decision-making in non-human animals (studying group decisions in a variety of animal species from social insects to primates; see, e.g., Conradt and Roper 2003)[^conradt-2003]; and applications to social epistemology beyond Condorcet’s jury theorem and judgment aggregation (e.g., the analysis of group doxastic states and their relationship to individual doxastic states; e.g., Goldman 2004, 2010; Lackey 2016)[^goldman-2004][^goldman-2010][^lackey-2016].

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=social-choice). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/social-choice/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=social-choice&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/social-choice/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

- Nehring, K. and C. Puppe, 2002, “[Strategy-Proof Social Choice on Single-Peaked Domains: Possibility, Impossibility and the Space Between](http://faculty.econ.ucdavis.edu/faculty/nehring/papers/sp-ema-march02.pdf),” unpublished manuscript.
- [The Society for Social Choice and Welfare](http://www.unicaen.fr/recherche/mrsh/scw/)
- [The Computational Social Choice Website](http://research.illc.uva.nl/COMSOC/)

## Related Entries

[Belief Merging and Judgment Aggregation](https://plato.stanford.edu/entries/belief-merging/)  | [Normative Economics and Economic Justice](https://plato.stanford.edu/entries/economic-justice/)  | [Jury Theorems](https://plato.stanford.edu/entries/jury-theorems/)  | [Voting Methods](https://plato.stanford.edu/entries/voting-methods/) | Arrow’s theorem | Condorcet, Marie-Jean-Antoine-Nicolas de Caritat, Marquis de: in the history of feminism | consequentialism | Cusanus, Nicolaus [Nicolas of Cusa] | Pufendorf, Samuel Freiherr von | Rawls, John | Tarski, Alfred

### Acknowledgments

I am grateful to the editors, their reviewers, Franz Dietrich, Iain McLean, and Michael Morreau for comments.

## Notes（原文脚注）

[^note-1]: When $n$ is even, the first part of the theorem only holds for group sizes $n$ above a certain lower bound (which depends on $p)$, due to the possibility of majority ties. When $n$ is odd, it holds for any $n \gt 1$.

[^note-2]: If different individuals have different *known* levels of reliability, weighted majority voting outperforms simple majority voting at maximizing the probability of a correct decision, with each individual’s voting weight proportional to $\log(p/(1-p))$, where $p$ is the individual’s reliability as defined above (Shapley and Grofman 1984; Grofman, Owen, and Feld 1983; Ben-Yashar and Nitzan 1997)[^ben-yashar-1997][^grofman-1983][^shapley-1984].

[^note-3]: Optionally, one can stipulate that the utility from a tie is 1/2.

[^note-4]: Completeness requires that, for any $x, y \in X$, $xR_iy$ or $yR_ix,$ and transitivity requires that, for any $x, y, z \in X$, if $xR_iy$ and $yR_iz$, then $xR_iz.$

[^note-5]: In the classic example, there are three individuals with preference orderings $xP_1 yP_1 z, yP_2 zP_2 x$, and $zP_3 xP_3 y$ over three alternatives $x, y$, and $z$. The resulting majority preferences are cyclical: we have $xPy$, $yPz$, and yet $zPx$.

[^note-6]: Formally, $\{x \in X : x \in f(R_1,R_2 ,\ldots ,R_n)$ for some $\langle R_1,R_2 ,\ldots ,R_n\rangle$ in the domain of $f\}$.

[^note-7]: For present purposes, one can stipulate that the last clause (for all $x$ in the range of $f$, $yR_ix$ where $y \in f(R_1, R_2 , \ldots ,R_n))$ is violated if $f(R_1, R_2 , \ldots ,R_n)$ is empty.

[^note-8]: Formally, $y'P_iy$, where $y' = f(R_1,\ldots, R'_i, \ldots ,R_n)$ and $y = f(R_1 , \ldots ,R_i , \ldots ,R_n)$, assuming that $\langle R_1,\ldots$, $R'_i$, $\ldots ,R_n\rangle$ is in the domain of $f$. The definition presupposes that the social choice sets for the profiles $\langle R_1, \ldots ,R_i , \ldots ,R_n\rangle$ and $\langle R_1,\ldots$, $R'_i$, $\ldots ,R_n\rangle$ are singleton.

[^note-9]: Sen, like Arrow in his definition of social welfare functions (as opposed to functionals), required $R$ to be an ordering by definition.

[^note-10]: Technically, this requires a domain restriction to positive welfare profiles.

[^note-11]: Formally, $X = \{p, \neg p : p \in X^+\}$, where $X^+$ is a set of un-negated propositions. To avoid technicalities, we assume that $X$ contains no contradictory or tautological propositions.

[^note-12]: In principle, consistency can be defined relative to some side constraint such as the legal doctrine in the ‘doctrinal paradox’ example.

[^note-13]: See also the remark on the relationship between path-connectedness and non-simplicity at the end of this subsection.

[^note-14]: An earlier mathematically related, though interpretationally distinct contribution is Wilson’s work on abstract aggregation (1975).

[^note-15]: We call an opinion function $Pr$ on $X$ *probabilistically coherent* if it is extendable to a probability function (with standard properties) on the smallest algebra that includes $X$. An *algebra* is a set of propositions that is closed under negation and conjunction. If $X$ is itself an algebra, as often assumed, then a probabilistically coherent opinion function on $X$ is simply a probability function. In the context of probabilistic opinion pooling, $X$ is often assumed to be an algebra generated by some underlying set of possible worlds, e.g., the set of all subsets of it, with negation understood as set-theoretic complementation and conjunction understood as set-theoretic conjunction. If we wish to lift the assumption that $X$ is finite, then every reference to an algebra in this section must be replaced with a reference to a $\sigma$-algebra.

[^note-16]: The learnt information $L$ could be either simply the truth of some proposition (an event) or, more generally, a likelihood function. Much of the earlier literature in statistics on ‘external Bayesianity’ uses the latter modelling option, while some of the recent philosophical literature uses the former. Depending on how $L$ is modelled, conditionalization then takes the form either of classical Bayesian conditionalization or of its generalization to the case of likelihood functions.

[^acze-1980]: Aczél, J. and C. Wagner, 1980, “A characterization of weighted arithmetic means,” *SIAM Journal of Algebraic Discrete Methods*, 1: 259–260.

[^adler-2011]: Adler, M. D., 2011, *Well-Being and Fair Distribution: Beyond Cost-Benefit Analysis*, Oxford: Oxford University Press.

[^adler-2019]: –––, 2019, *Measuring Social Welfare: An Introduction*, Oxford: Oxford University Press.

[^arrow-1951]: Arrow, K., 1951/1963, *Social Choice and Individual Values*, New York: Wiley.

[^austen-smith-1996]: Austen-Smith, D. and J. S. Banks, 1996, “Information Aggregation, Rationality, and the Condorcet Jury Theorem,” *American Political Science Review*, 90: 34–45.

[^baccelli-2020]: Baccelli, J. and R. T. Stewart, 2020, “Support for geometric pooling,” *Review of Symbolic Logic*, first online 21 October 2020. doi:10.1017/S1755020320000416

[^bartholdi-1989]: Bartholdi, J. J., C. A. Tovey, and M. A. Trick, 1989, “The computational difficulty of manipulating an election,” *Social Choice and Welfare*, 6: 227–241.

[^ben-yashar-1997]: Ben-Yashar, R. and S. Nitzan, 1997, “The optimal decision rule for fixed-size committees in dichotomous choice situations: the general result,” *International Economic Review*, 38: 175–186.

[^berend-1998]: Berend, D. and J. Paroush, 1998, “When is Condorcet’s Jury Theorem valid?” *Social Choice and Welfare*, 15: 481–488.

[^berend-2007]: Berend, D. and L. Sapir., 2007, “Monotonicity in Condorcet’s Jury Theorem with dependent voters,” *Social Choice and Welfare*, 28: 507–528.

[^black-1948]: Black, D., 1948, “On the Rationale of Group Decision-Making,” *Journal of Political Economy*, 56: 23–34.

[^blackorby-1999]: Blackorby, C., W. Bossert, and D. Donaldson, 1999, “Information Invariance in Variable-Population Social-Choice Problems,” *International Economic Review*, 40: 403–422.

[^blackorby-2005]: –––, 2005, *Population Issues in Social Choice Theory, Welfare Economics, and Ethics*, Cambridge: Cambridge University Press.

[^blau-1975]: Blau, J. H., 1975, “Liberal Values and Independence,” *Review of Economic Studies*, 42: 395–401.

[^boland-1989]: Boland, P. J., 1989, “Majority systems and the Condorcet jury theorem,” *Statistician*, 38: 181–189.

[^bossert-1991]: Bossert, W., 1991, “On intra- and interpersonal utility comparisons,” *Social Choice and Welfare*, 8: 207–219.

[^bossert-1996]: Bossert, W. and J. A. Weymark, 1996, “Utility in social choice,” *Handbook of Utility Theory* (Volume 2), S. Barberà, P. J. Hammond and C. Seidel (eds.), Boston: Kluwer.

[^bossert-2013]: Bossert, W., C. X. Qi, and J. A. Weymark, 2013, “Extensive social choice and the measurement of group fitness in biological hierarchies,” *Biology and Philosophy*, 28: 75–98.

[^bovens-2006]: Bovens, L. and W. Rabinowicz, 2006, “Democratic Answers to Complex Questions: An Epistemic Perspective,” *Synthese*, 150: 131–153.

[^brams-1978]: Brams, S. J. and P. C. Fishburn, 1978, “Approval voting,” *American Political Science Review*, 72: 831–847.

[^brams-1983]: –––, 1983, *Approval Voting*, Boston: Birkhäuser.

[^brams-1996]: Brams, S. J. and A. D. Taylor, 1996, *Fair Division: From Cake-Cutting to Dispute Resolution*, Cambridge: Cambridge University Press.

[^brandt-2013]: Brandt, F., V. Conitzer, and U. Endriss, 2013, “Computational Social Choice,” *Multiagent Systems*, G. Weiss (ed.), Cambridge, MA: MIT Press, pp. 213–283.

[^brighouse-2010]: Brighouse, H. and M. Fleurbaey, 2010, “Democracy and Proportionality,” *Journal of Political Philosophy*, 18: 137–155.

[^cantillon-2002]: Cantillon, E. and A. Rangel, 2002, “A graphical analysis of some basic results in social choice,” *Social Choice and Welfare*, 19: 587–611.

[^chapman-2002]: Chapman, B., 2002, “Rational Aggregation,” *Politics, Philosophy and Economics*, 1: 337–354.

[^chichilnisky-1980]: Chichilnisky, G., 1980, “Social choice and the topology of spaces of preferences,” *Advances in Mathematics*, 37: 165–176.

[^christensen-2013]: Christensen, D. and J. Lackey (eds.), 2013, *The Epistemology of Disagreement: New Essays*, New York: Oxford University Press.

[^condorcet-1785]: Condorcet, Nicolas de, 1785, *Essay sur l’Application de l’Analyse à la Probabilité des Décisions Rendue à la Pluralité des Voix*, Paris.

[^conradt-2003]: Conradt, L. and T. J. Roper, 2003, “Group decision-making in animals,” *Nature*, 421: 155–158.

[^craven-1982]: Craven, J., 1982, “Liberalism and Individual Preferences,” *Theory and Decision*, 14: 351–360.

[^deschamps-1978]: Deschamps, R. and L. Gevers, 1978, “Leximin and utilitarian rules: A joint characterization,” *Journal of Economic Theory*, 17: 143–163.

[^dietrich-2006]: Dietrich, F., 2006, “Judgment Aggregation: (Im)Possibility Theorems,” *Journal of Economic Theory*, 126: 286–298.

[^dietrich-2007]: –––, 2007, “A generalised model of judgment aggregation,” *Social Choice and Welfare*, 28: 529–565.

[^dietrich-2008]: –––, 2008, “The premises of Condorcet’s jury theorem are not simultaneously justified,” *Episteme*, 5: 56–73.

[^dietrich-2010]: –––, 2010, “Bayesian group belief,” *Social Choice and Welfare*, 35: 595–626.

[^dietrich-2015]: –––, 2015, “Aggregation theory and the relevance of some issues to others,” *Journal of Economic Theory*, 160: 463–493.

[^dietrich-2019]: –––, 2019, “A theory of Bayesian groups,” *Noûs*, 53: 708–736.

[^dietrich-2004]: Dietrich, F. and C. List, 2004, “A Model of Jury Decisions Where All Jurors Have the Same Evidence,” *Synthese*, 142: 175–202.

[^dietrich-2007a]: –––, 2007a, “Judgment aggregation by quota rules: majority voting generalized,” *Journal of Theoretical Politics*, 19: 391–424.

[^dietrich-2007b]: –––, 2007b, “Arrow’s theorem in judgment aggregation,” *Social Choice and Welfare*, 29: 19–33.

[^dietrich-2007c]: –––, 2007c, “Strategy-proof judgment aggregation,” *Economics and Philosophy*, 23: 269–300.

[^dietrich-2008-2]: –––, 2008, “Judgment aggregation without full rationality,” *Social Choice and Welfare*, 31: 15–39.

[^dietrich-2010a]: –––, 2010a, “Majority voting on restricted domains,” *Journal of Economic Theory*, 145: 512–543.

[^dietrich-2010b]: –––, 2010b, “The aggregation of propositional attitudes: towards a general theory,” *Oxford Studies in Epistemology*, 3: 215–234.

[^dietrich-2017]: –––, 2017, “Probabilistic Opinion Pooling Generalized: Parts I and II,” *Social Choice and Welfare* 48(4): 747–814.

[^dietrich-2010-2]: Dietrich, F. and P. Mongin, 2010, “The premise-based approach to judgment aggregation,” *Journal of Economic Theory*, 145: 562–582.

[^dietrich-2013]: Dietrich, F. and K. Spiekermann, 2013, “Epistemic Democracy with Defensible Premises,” *Economics and Philosophy*, 29(1): 87–120.

[^dokow-2010a]: Dokow, E. and R. Holzman, 2010a, “Aggregation of binary evaluations,” *Journal of Economic Theory*, 145: 495–511.

[^dokow-2010b]: –––, 2010b, “Aggregation of binary evaluations with abstentions,” *Journal of Economic Theory*, 145: 544–561.

[^dokow-2010c]: –––, 2010c, “Aggregation of non-binary evaluations,” *Advances in Applied Mathematics*, 45: 487–504.

[^dowding-2003]: Dowding, K. and M. van Hees, 2003, “The Construction of Rights,” *American Political Science Review*, 97: 281–293.

[^dowding-2008]: –––, 2008, “In Praise of Manipulation,” *British Journal of Political Science*, 38: 1–15.

[^dryzek-2003]: Dryzek, J. and C. List, 2003, “Social Choice Theory and Deliberative Democracy: A Reconciliation,” *British Journal of Political Science*, 33: 1–28.

[^elster-2013]: Elster, J., 2013, “Excessive Ambitions (II),” *Capitalism and Society*, 8, Issue 1, Article 1.

[^estlund-1994]: Estlund, D., 1994, “Opinion Leaders, Independence, and Condorcet’s Jury Theorem,” *Theory and Decision*, 36: 131–162.

[^fabre-2021]: Fabre, A., 2021, “Tie-breaking the highest median: alternatives to the majority judgment,” *Social Choice and Welfare*, 56: 101–124.

[^feddersen-1998]: Feddersen, T. J. and W. Pesendorfer, 1998, “Convicting the Innocent,” *American Political Science Review*, 92: 23–35.

[^fey-2004]: Fey, M., 2004, “May’s theorem with an infinite population,” *Social Choice and Welfare*, 23: 275–293.

[^fishburn-1978]: Fishburn, P. C., 1978, “Axioms for Approval Voting: Direct Proof,” *Journal of Economic Theory*, 19: 180–185.

[^fishburn-1988]: –––, 1988, “Corrigendum,” *Journal of Economic Theory*, 45: 212.

[^gaertner-2001]: Gaertner, W., 2001, *Domain Conditions in Social Choice Theory*, Cambridge: Cambridge University Press.

[^gaertner-2005]: –––, 2005, “De jure naturae et gentium: Samuel von Pufendorf’s contribution to social choice theory and economics,” *Social Choice and Welfare*, 25: 231–241.

[^gaertner-1992]: Gaertner, W., P. K. Pattanaik, and K. Suzumura, 1992, “Individual Rights Revisited,” *Economica*, 59: 161–177.

[^gaertner-2012]: Gaertner, W. and E. Schokkaert, 2012, *Empirical Social Choice: Questionnaire-Experimental Studies on Distributive Justice*, Cambridge: Cambridge University Press.

[^gale-1962]: Gale, D. and L. S. Shapley, 1962, “College admissions and the stability of marriage,” *American Mathematical Monthly*, 69: 9–15.

[^gärdenfors-2006]: Gärdenfors, P., 2006, “An Arrow-like theorem for voting with logical consequences,” *Economics and Philosophy*, 22: 181–190.

[^gehrlein-1983]: Gehrlein, W. V., 1983, “Condorcet’s Paradox,” *Theory and Decision*, 15: 161–197.

[^genest-1984]: Genest, C., 1984, “A characterization theorem for externally Bayesian groups,” *Annals of Statistics*, 12: 1100–1105.

[^genest-1986]: Genest, C., K. J. McConway, and M. J. Schervish, 1986, “Characterization of externally Bayesian pooling operators,” *Annals of Statistics* 14: 487–501.

[^genest-1987]: Genest, C. and K. Wagner, 1987, “Further evidence against independence preservation in expert judgement synthesis,” *Aequationes Mathematicae*, 32: 74–86.

[^genest-1986-2]: Genest, C. and J. V. Zidek, 1986, “Combining Probability Distributions: A Critique and Annotated Bibliography,” *Statistical Science*, 1: 113–135.

[^gibbard-1969]: Gibbard, A., 1969, “Social Choice and the Arrow Conditions,” Unpublished manuscript. [[Gibbard 1969 available online (pdf)](http://www-personal.umich.edu/~gibbard/Gibbard1968-Social-Choice-Arrow-Conditions.pdf)]

[^gibbard-1973]: –––, 1973, “Manipulation of voting schemes: a general result,” *Econometrica*, 41: 587–601.

[^gigliotti-1986]: Gigliotti, G. A., 1986, “Comment on Craven,” *Theory and Decision*, 21: 89–95.

[^gilboa-2004]: Gilboa, I., D. Samet, and D. Schmeidler, 2004, “Utilitarian Aggregation of Beliefs and Tastes,” *Journal of Political Economy*, 112: 932–938.

[^goldman-2004]: Goldman, A., 2004, “Group Knowledge versus Group Rationality: Two Approaches to Social Epistemology,” *Episteme, A Journal of Social Epistemology*, 1: 11–22.

[^goldman-2010]: –––, 2010, “Why Social Epistemology Is Real Epistemology,” *Social Epistemology*, A. Haddock, A. Millar, and D. Pritchard (eds.), Oxford: Oxford University Press.

[^goodin-2006]: Goodin, R. E. and C. List, 2006, “A Conditional Defense of Plurality Rule: Generalizing May’s Theorem in a Restricted Informational Environment,” *American Journal of Political Science*, 50: 940–949.

[^goodin-2018]: Goodin, R. E. and K. Spiekermann, 2018, *An Epistemic Theory of Democracy*, Oxford: Oxford University Press.

[^grofman-1983]: Grofman, B., G. Owen, and S. L. Feld, 1983, “Thirteen theorems in search of the truth,” *Theory and Decision*, 15: 261–278.

[^guilbaud-1952]: Guilbaud, G. T., [1952] 1966, “Theories of the General Interest, and the Logical Problem of Aggregation,” *Readings in Mathematical Social Science*, P. F. Lazarsfeld and N. W. Henry (eds.), Cambridge, MA: MIT Press, pp. 262–307.

[^harrison-2008]: Harrison, G. W. and T. McDaniel, 2008, “Voting Games and Computational Complexity,” *Oxford Economic Papers*, 60: 546–565.

[^hattiangadi-2020]: Hattiangadi, A., 2020, “Radical Interpretation and The Aggregation Problem,” *Philosophy and Phenomenological Research*, 101: 283–303.

[^hausman-1995]: Hausman, D., 1995, “The Impossibility of Interpersonal Utility Comparisons,” *Mind*, 104: 473–490.

[^heal-1997]: Heal, G. M. (ed.), 1997, *Topological Social Choice*, Heidelberg: Springer.

[^hurley-1985]: Hurley, S., 1985, “Supervenience and the Possibility of Coherence,” *Mind*, 94: 501–525.

[^inada-1964]: Inada, K.-I., 1964, “A Note on the Simple Majority Decision Rule,” *Econometrica*, 32: 525–531.

[^kanazawa-1998]: Kanazawa, S., 1998, “A brief note on a further refinement of the Condorcet Jury Theorem for heterogeneous groups,” *Mathematical Social Sciences*, 35: 69–73.

[^klaus-2016]: Klaus, B., D. F. Manlove, and F. Rossi, 2016, “Matching under preferences,” *Handbook of Computational Social Choice*, F. Brandt, V. Conitzer, U. Endriss, J. Lang, and A. D. Procaccia (eds.), Cambridge: Cambridge University Press, pp. 333–355.

[^knight-1994]: Knight, J. and J. Johnson, 1994, “Aggregation and Deliberation: On the Possibility of Democratic Legitimacy,” *Political Theory*, 22: 277–296.

[^konieczny-2002]: Konieczny, S. and R. Pino Pérez, 2002, “Merging Information Under Constraints: A Logical Framework,” *Journal of Logic and Computation*, 12: 773–808.

[^kornhauser-1986]: Kornhauser, L. A. and L. G. Sager, 1986, “Unpacking the Court,” *Yale Law Journal*, 96: 82–117.

[^kroedel-2013]: Kroedel, T. and F. Huber, 2013, “Counterfactual Dependence and Arrow,” *Noûs*, 47(3): 453–466.

[^lackey-2016]: Lackey, J., 2016, “What Is Justified Group Belief?” *Philosophical Review*, 125: 341–396.

[^ladha-1992]: Ladha, K., 1992, “The Condorcet Jury Theorem, Free Speech and Correlated Votes,” *American Journal of Political Science*, 36: 617–634.

[^landemore-2013]: Landemore, H., 2013, *Democratic Reason: Politics, Collective Intelligence, and the Rule of the Many*, Princeton: Princeton University Press.

[^lehrer-1981]: Lehrer, K. and C. Wagner, 1981, *Rational Consensus in Science and Society*, Dordrecht/Boston: Reidel.

[^list-2001]: List, C., 2001, “A Note on Introducing a ‘Zero-Line’ of Welfare as an Escape-Route from Arrow’s Theorem,” *Pacific Economic Review*, 6, special section in honour of Amartya Sen, 223–238.

[^list-2003a]: –––, 2003a, “Are Interpersonal Comparisons of Utility Indeterminate?” *Erkenntnis*, 58: 229–260.

[^list-2003b]: –––, 2003b, “A Possibility Theorem on Aggregation over Multiple Interconnected Propositions,” *Mathematical Social Sciences*, 45: 1–13 (with Corrigendum in *Mathematical Social Sciences*, 52: 109–110).

[^list-2004a]: –––, 2004a, “Multidimensional Welfare Aggregation,” *Public Choice*, 119: 119–142.

[^list-2004b]: –––, 2004b, “A Model of Path-Dependence in Decisions over Multiple Propositions,” *American Political Science Review*, 98: 495–513.

[^list-2001-2]: List, C. and R. E. Goodin, 2001, “Epistemic Democracy: Generalizing the Condorcet Jury Theorem,” *Journal of Political Philosophy*, 9: 277–306.

[^list-2013]: List, C., R. C. Luskin, J. S. Fishkin, and I. McLean, 2013, “Deliberation, Single-Peakedness, and the Possibility of Meaningful Democracy: Evidence from Deliberative Polls,” *Journal of Politics*, 75: 80–95.

[^list-2002]: List, C. and P. Pettit, 2002, “Aggregating Sets of Judgments: An Impossibility Result,” *Economics and Philosophy*, 18(1): 89–110.

[^list-2004]: –––, 2004, “Aggregating Sets of Judgments: Two Impossibility Results Compared,” *Synthese*, 140: 207–235.

[^macaskill-2016]: MacAskill, W., 2016, “Normative Uncertainty as a Voting Problem,” *Mind*, 125: 967–1004.

[^may-1952]: May, K. O., 1952, “A set of independent, necessary and sufficient conditions for simple majority decision,” *Econometrica*, 20: 680–684.

[^may-1954]: –––, 1954, “Intransitivity, Utility, and the Aggregation of Preference Patterns,” *Econometrica*, 22: 1–13.

[^mcconway-1981]: McConway, K. J., 1981, “Marginalization and Linear Opinion Pools,” *Journal of the American Statistical Association*, 76: 410–414.

[^mclean-1990]: McLean, I., 1990, “The Borda and Condorcet principles: Three medieval applications,” *Social Choice and Welfare*, 7: 99–108.

[^mclean-1994]: McLean, I. and F. Hewitt (eds.), 1994, *Condorcet: Foundations of Social Choice and Political Theory*, Cheltenham: Edward Elgar Publishing.

[^mclean-1995]: McLean, I. S., A. McMillan, and B. L. Monroe, 1995, “Duncan Black and Lewis Carroll,” *Journal of Theoretical Politics*, 7: 107–123.

[^mclean-1996]: ––– (eds.), 1996, *A Mathematical Approach to Proportional Representation: Duncan Black on Lewis Carroll*, Dordrecht: Kluwer.

[^mclean-1995-2]: McLean, I. and A. B. Urken (eds.), 1995, *Classics of Social Choice*, Ann Arbor: University of Michigan Press.

[^miller-1992]: Miller, D., 1992, “Deliberative Democracy and Social Choice,” *Political Studies*, 40 (special issue): 54–67.

[^miller-2009]: Miller, M. K. and D. Osherson, 2009, “Methods for distance-based judgment aggregation,” *Social Choice and Welfare*, 32: 575–601.

[^monjardet-2005]: Monjardet, B., 2005, “Social choice theory and the ‘Centre de Mathématique Sociale’: some historical notes,” *Social Choice and Welfare*, 25: 433–456.

[^mongin-1995]: Mongin, P., 1995, “Consistent Bayesian aggregation,” *Journal of Economic Theory*, 66: 313–351.

[^mongin-1997]: –––, 1997, “Spurious Unanimity and the Pareto Principle,” Paper presented at the Conference on Utilitarianism, New Orleans, March 1997. [[Mongin 1997 available online (pdf)](http://eprints.lse.ac.uk/23942/1/Spurious_Unanimity_and_the_Pareto_Principle_(LSERO).pdf)]

[^mongin-2008]: –––, 2008, “Factoring Out the Impossibility of Logical Aggregation,” *Journal of Economic Theory*, 141: 100–113.

[^mongin-2016]: Mongin, P. and M. Pivato, 2016, “Social preference and social welfare under risk and uncertainty,” *Oxford Handbook of Well-Being and Public Policy*, M. Adler and M. Fleurbaey (eds.), Oxford: Oxford University Press.

[^morreau-2010]: Morreau, M., 2010, “It simply does not add up: Trouble with overall similarity,” *Journal of Philosophy*, 107: 469–490.

[^morreau-2015]: –––, 2015, “Theory Choice and Social Choice: Kuhn Vindicated,” *Mind,* 124: 239–262.

[^morreau-2016]: –––, 2016, “Grading in Groups,” *Economics and Philosophy*, 32: 323–352.

[^moulin-1980]: Moulin, H., 1980, “On Strategy-Proofness and Single Peakedness,” *Public Choice*, 35: 437–455.

[^moulin-2004]: –––, 2004, *Fair Division And Collective Welfare*, Cambridge, MA: MIT Press.

[^mueller-2003]: Mueller, D. C., 2003, *Public Choice III*, Cambridge: Cambridge University Press.

[^nehring-2003]: Nehring, K., 2003, “Arrow’s theorem as a corollary,” *Economics Letters*, 80: 379–382.

[^nehring-2007]: Nehring, K. and C. Puppe, 2007, “The structure of strategy-proof social choice—Part I: General characterization and possibility results on median spaces,” *Journal of Economic Theory*, 135: 269–305.

[^nehring-2010]: –––, 2010, “Abstract Arrovian Aggregation,” *Journal of Economic Theory*, 145: 467–494.

[^niemi-1984]: Niemi, R. G., 1984, “The Problem of Strategic Behavior under Approval Voting,” *American Political Science Review*, 78: 952–958.

[^okasha-2009]: Okasha, S., 2009, “Individuals, groups, fitness and utility: multi-level selection meets social choice theory,” *Biology and Philosophy*, 24: 561–584.

[^okasha-2011]: –––, 2011, “Theory Choice and Social Choice: Kuhn versus Arrow,” *Mind*, 120: 83–115.

[^ooghe-2005]: Ooghe, E. and L. Lauwers, 2005, “Non-dictatorial extensive social choice,” *Economic Theory*, 25: 721–743.

[^ottonelli-2013]: Ottonelli, V. and D. Porello, 2013, “On the elusive notion of meta-agreement,” *Politics, Philosophy and Economics*, 12: 68–92.

[^parfit-1984]: Parfit, D., 1984, *Reasons and Persons*, Oxford: Oxford University Press.

[^pauly-2006]: Pauly, M. and M. van Hees, 2006, “Logical Constraints on Judgment Aggregation,” *Journal of Philosophical Logic*, 35: 569–585.

[^pearl-2000]: Pearl, J., 2000, *Causality: models, reasoning, and inference*, Cambridge: Cambridge University Press.

[^peter-2003]: Peter, F., 2003, “Gender and the foundations of social choice: The role of situated agency,” *Feminist Economics*, 9: 13–32.

[^pettit-2001]: Pettit, P., 2001, “Deliberative Democracy and the Discursive Dilemma,” *Philosophical Issues*, 11: 268–299.

[^pigozzi-2006]: Pigozzi, G., 2006, “Belief merging and the discursive dilemma: an argument-based account to paradoxes of judgment aggregation,” *Synthese*, 152: 285–298.

[^pivato-2017]: Pivato, M., 2017, “Epistemic democracy with correlated voters,” *Journal of Mathematical Economics*, 72: 51–69.

[^poisson-1837]: Poisson, S. D., 1837, *Recherches sur la probabilité des jugements en matière criminelle et en matière civile: précédées des règles générales du calcul des probabilités*, Paris: Bachelier, Imprimeur-Libraraire.

[^rafiee-2021]: Rafiee Rad, S. and O. Roy, 2021, “Deliberation, Single-Peakedness, and Coherent Aggregation,” *American Political Science Review*, first online 22 February 2021. doi:10.1017/S0003055420001045

[^rawls-1971]: Rawls, J., 1971, *A Theory of Justice*, Cambridge, MA: Harvard University Press.

[^regenwetter-2006]: Regenwetter, M., B. Grofman, A. A. J. Marley, and I. Tsetlin, 2006, *Behavioral Social Choice*, Cambridge: Cambridge University Press.

[^riker-1982]: Riker, W., 1982, *Liberalism against Populism*, San Francisco: W.H. Freeman and Co.

[^roberts-1980]: Roberts, K.W.S., 1980, “Interpersonal Comparability and Social Choice Theory,” *Review of Economic Studies*, 47(2): 421-439.

[^roberts-1995]: Roberts, K.W.S., 1995, “Valued Opinions or Opinionated Values: The Double Aggregation Problem,” *Choice, Welfare and Development: A Festschrift in Honour of Amartya Sen*, K. Basu, P. K. Pattanaik, and K. Suzumura (eds.), Oxford: Oxford University Press, pp. 141–165.

[^roemer-1996]: Roemer, J. E., 1996, *Theories of Distributive Justice*, Cambridge, MA: Harvard University Press.

[^roth-1992]: Roth, A. E. and M. Sotomayor, 1992, “Two-sided matching,” *Handbook of Game Theory with Economic Applications* (Volume 1), R. Aumann and S. Hart (eds.), Amsterdam: North Holland, pp. 485–541.

[^russell-2015]: Russell, J. S., J. Hawthorne, and L. Buchak, 2015, “Groupthink,” *Philosophical Studies*, 172: 1287–1309.

[^saari-1990]: Saari, D. G., 1990, “The Borda dictionary,” *Social Choice and Welfare*, 7: 279–317.

[^salles-2005]: Salles, M. (edited with introduction), 2005, “The history of Social Choice,” Special issue, *Social Choice and Welfare*, 25: 229–564.

[^satterthwaite-1975]: Satterthwaite, M., 1975, “Strategy-proofness and Arrow’s conditions: existence and correspondence theorems for voting procedures and social welfare functions,” *Journal of Economic Theory*, 10: 187–217.

[^sen-1966]: Sen, A. K., 1966, “A Possibility Theorem on Majority Decisions,” *Econometrica*, 34: 491–499.

[^sen-1970a]: –––, 1970a, “The Impossibility of a Paretian Liberal,” *Journal of Political Economy*, 78: 152–157.

[^sen-1970b]: –––, 1970b, *Collective Choice and Social Welfare*, San Francisco: Holden-Day.

[^sen-1977]: –––, 1977, “On weights and measures: informational constraints in social welfare analysis,” *Econometrica*, 45: 1539–1572.

[^sen-1982]: –––, 1982, *Choice, Welfare and Measurement*, Oxford: Blackwell.

[^sen-1983]: –––, 1983, “Liberty and social choice,” *Journal of Philosophy*, 80: 5–28.

[^sen-1992]: –––, 1992, *Inequality Reexamined*, Cambridge, MA: Harvard University Press.

[^sen-1998]: –––, 1998, “The Possibility of Social Choice,” Nobel lecture, December 8, 1998, Stockholm. [[Sen 1998 available online (pdf)](http://www.nobelprize.org/nobel_prizes/economics/laureates/1998/sen-lecture.pdf)]

[^sertel-1988]: Sertel, M. R., 1988, “Characterizing Approval Voting,” *Journal of Economic Theory*, 45: 207–211.

[^shapley-1984]: Shapley, L. and B. Grofman, 1984, “Optimizing group judgment accuracy in the presence of interdependencies,” *Public Choice*, 43: 329–343.

[^stegenga-2013]: Stegenga, J., 2013, “An impossibility theorem for amalgamating evidence,” *Synthese*, 190: 2391–2411.

[^stewart-2018]: Stewart, R. T. and I. Ojea Quintana, 2018, “Probabilistic Opinion Pooling with Imprecise Probabilities,” *Journal of Philosophical Logic*, 47: 17–45.

[^stone-1961]: Stone, M., 1961, “The Opinion Pool,” *Annals of Mathematical Statistics*, 32: 1339–1342.

[^suppes-2005]: Suppes, P., 2005, “The pre-history of Kenneth Arrow’s social choice and individual values,” *Social Choice and Welfare*, 25: 319–226.

[^suzumura-2000]: Suzumura, K., 2000, “Welfare economics beyond welfarist-consequentialism,” *Japanese Economic Review*, 51: 1–32.

[^thomson-2000]: Thomson, W., 2000, “On the axiomatic method and its recent applications to game theory and resource allocation,” *Social Choice and Welfare*, 18: 327–386.

[^tsetlin-2003]: Tsetlin, I., M. Regenwetter, and B. Grofman, 2003, “The Impartial Culture Maximizes the Probability of Majority Cycles,” *Social Choice and Welfare*, 21: 387–398.

[^tsuchiya-2019]: Tsuchiya, A. and J. Miyamoto, 2019, “Social Choice in Health and Health Care,” *The Handbook of Rational and Social Choice*, P. Anand, P. Pattanaik, and C. Puppe (eds.), Oxford: Oxford University Press, pp. 524–540.

[^vacca-1921]: Vacca, R., 1921, “Opinioni Individuali e Deliberazioni Collettive,” *Rivista Internazionale di Filosofia del Diritto*, 52: 52–59.

[^ward-1965]: Ward, B., 1965, “Majority Voting and Alternative Forms of Public Enterprises,” *The Public Economy of Urban Communities*, J. Margolis (ed.), Baltimore: Johns Hopkins Press.

[^weymark-2006]: Weymark, J., 2006, “The Normative Approach to the Measurement of Multidimensional Inequality,” *Inequality and Economic Integration*, F. Farina and E. Savaglio (eds.), London: Routledge, pp. 303–328.

[^wilson-1975]: Wilson, R., 1975, “On the Theory of Aggregation,” *Journal of Economic Theory*, 10: 89–99.
