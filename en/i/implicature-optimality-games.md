# Optimality-Theoretic and Game-Theoretic Approaches to Implicature
**First published Fri Dec 1, 2006; substantive revision Thu Jul 2, 2026**

*van Rooij, Robert, Franke, Michael*

Linguistic pragmatics studies the context-dependent use and interpretation of expressions. Perhaps the most important notion in pragmatics is Grice’s (1967)[^grice-1967] *conversational implicature*. It is based on the insight that by means of general principles of rational cooperative behavior we can communicate more with the *use* of a sentence than the *conventional semantic meaning* associated with it. Grice has argued, for instance, that the exclusive interpretation of ‘or’—according to which we infer from ‘John or Mary came’ that John and Mary didn’t come both—is not due to the semantic meaning of ‘or’ but should be accounted for by a theory of conversational implicature. In this particular example,—a typical example of a so-called Quantity implicature—the hearer’s implication is taken to follow from the fact that the speaker could have used a contrasting, and informatively stronger expression, but chose not to. Other implicatures may follow from what the hearer thinks that the speaker takes to be normal states of affairs, i.e., stereotypical interpretations. For both types of implicatures, the hearer’s (pragmatic) interpretation of an expression involves what he takes to be the speaker’s reason for using this expression. But obviously, this speaker’s reason must involve assumptions about the hearer’s reasoning as well.

In this entry we will discuss formal accounts of conversational implicatures that explicitly take into account the interactive reasoning of speaker and hearer (e.g., what speaker and hearer believe about each other, the relevant aspects of the context of utterance etc.) and that aim to reductively explain conversational implicature as the result of goal-oriented, economically optimised language use. For this entry, just as in traditional analyses of implicatures, we will assume that sentences have a pre-existing semantic meaning and will mostly focus on generalised conversational implicatures.

## 1. Bidirectional Optimality Theory

### 1.1 Bidirectional OT and Quantity implicatures

Optimality Theory (OT) is a linguistic theory which assumes that linguistic choices are governed by competition between a set of candidates, or alternatives. In standard OT (Prince & Smolensky, 1993)[^prince-1993] the optimal candidate is the one that satisfies best a set of violable constraints. After its success in phonology, OT has also been used in syntax, semantics and pragmatics. The original idea of optimality-theoretic semantics was to model interpretation by taking the candidates to be the alternative interpretations that the hearer could assign to a given expression, with constraints describing general preferences over expression-interpretation pairs. Blutner (1998, 2000)[^blutner-1998][^blutner-2000] extended this original version by taking also alternative expressions, or forms, into account that the speaker could have used, but did not. The reference to alternative expressions/forms is standard in pragmatics to account for Quantity implicatures. Optimization should thus be thought of from two directions: that of the hearer, and that of the speaker. What is optimal, according to Blutner’s Bidirectional-OT (Bi-OT), is not just interpretations with respect to forms, but rather form-interpretation pairs. In terms of a ‘better than’ relation ‘$\gt$’ between form-interpretation pairs, the pair $\langle f,i\rangle$ is said to be **(strongly) optimal** iff it satisfies the following two conditions:

$$\begin{align} \neg \exists i' &: \langle f,i'\rangle \gt \langle f,i\rangle \\ \neg \exists f' &: \langle f', i\rangle \gt \langle f,i\rangle \end{align}$$

The first condition requires that $i$ is an optimal interpretation of form $f$. In Bi-OT this condition is thought of as optimization from the hearer’s point of view. Blutner proposed that $\langle f,i'\rangle \gt \langle f,i\rangle$ iff $i'$ is a more likely, or stereotypical, interpretation of $f$ than $i$ is: $P(i'\mid \llbracket f\rrbracket) \gt P(i\mid \llbracket f \rrbracket)$ (where $\llbracket f\rrbracket$ denotes the semantic meaning of $f$, and $P(B\mid A)$ the conditional probability of $B$ given $A$, defined as $P(A\cap B)/P(A))$. The second condition is taken to involve speaker’s optimization: for $\langle f,i\rangle$ to be optimal for the speaker, it has to be the case that she cannot use a more optimal form $f'$ to express $i. \langle f',i\rangle \gt \langle f,i\rangle$ iff either (i) $P(i\mid \llbracket f'\rrbracket) \gt P(i\mid \llbracket f\rrbracket)$, or (ii) $P(i\mid\llbracket f'\rrbracket = P(i\mid\llbracket f\rrbracket)$ and $f'$ is a less complex form to express $i$ than $f$ is.

Bi-OT accounts for classical Quantity implicatures. A convenient (though controversial) example is the ‘exactly’-interpretation of number terms. Let us assume, for the sake of example, that number terms semantically have an ‘at least’-meaning.[^note-1] Still, we want to account for the intuition that the sentence “Three children came to the party” is normally interpreted as saying that *exactly* three children came to the party. One way to do this is to assume that the alternative expressions that the speaker could use are of the form “(*At least*) $n$ children came to the party”, while the alternative interpretations for the hearer are of type $i_n$ meaning that “*Exactly* $n$ children came to the party”.[^note-2] If we assume, again for the sake of example, that all relevant interpretations are considered equally likely and that it is already commonly assumed that some children came, but not more than four, the strongly optimal form-interpretation pairs can be read off the following table:

| $P(i\mid \llbracket f\rrbracket)$ | $i_1$ | $i_2$ | $i_3$ | $i_4$ |
| --- | --- | --- | --- | --- |
| ‘one’ | $\Rightarrow$¼ | ¼ | ¼ | ¼ |
| ‘two’ | 0 | $\Rightarrow ⅓$ | $⅓$ | $⅓$ |
| ‘three’ | 0 | 0 | $\Rightarrow$ ½ | ½ |
| ‘four’ | 0 | 0 | 0 | $\Rightarrow 1$ |

In this table the entry $P(i_3 \mid \llbracket$‘two’$\rrbracket) = ⅓$ because $P(i_3 \mid \{i_2,i_3,i_4\}) = ⅓$. Notice that according to this reasoning ‘two’ is interpreted as ‘exactly 2’ (as indicated by an arrow) because:

1. $P(i_2 \mid \llbracket$‘two’$\rrbracket) = ⅓$ is higher than $P(i_2 \mid \llbracket$‘$n \textrm{'} \rrbracket)$ for any alternative expression ‘$n$’, and
2. all other interpretations compatible with the semantic meaning of the numeral expression are *blocked*: there is, for instance, another expression for which $i_4$ is a better interpretation, i.e., an interpretation with a higher conditional probability.

With numeral terms, the semantic meanings of the alternative expressions give rise to a linear order. This turns out to be crucial for the Bi-OT analysis, if we continue to take the interpretations as specific as we have done so far. Consider the following alternative answers to the question “Who came to the party?”:

1. John came to the party.
2. John or Bill came to the party.

Suppose that John and Bill are the only relevant persons and that it is presupposed that somebody came to the party. In that case the table that illustrates bidirectional optimality reasoning looks as follows (where $i_x$ is the interpretation that only $x$ came):

| $P(i\mid \llbracket f\rrbracket)$ | $i_j$ | $i_b$ | $i_{jb}$ |
| --- | --- | --- | --- |
| ‘John’ | $\Rightarrow ½$ | 0 | $½$ |
| ‘Bill’ | 0 | $\Rightarrow ½$ | $½$ |
| ‘John and Bill’ | 0 | 0 | $\Rightarrow 1$ |
| ‘John or Bill’ | $⅓$ | $⅓$ | $⅓$ |

This table correctly predicts that (1) is interpreted as saying that *only* John came. But now consider the disjunction (2). Intuitively, this answer should be interpreted as saying that either only John, or only Bill came. It is easy to see, however, that this is predicted only if ‘John came’ and ‘Bill came’ are not taken to be alternative forms. Bi-OT predicts that in case also ‘John came’ and ‘Bill came’ are taken to be alternatives, the disjunction is uninterpretable, because the specific interpretations $i_j, i_b$, and $i_{jb}$ all can be expressed better by other forms. In general, one can see that in case the semantic meanings of the alternative expressions are not linearly, but only partially ordered, the derivation of Quantity implicatures sketched above gives rise to partially wrong predictions.

As it turns out, this problem for Bi-OT seems larger than it really is. Intuitively, an answer like (2) suggests that the speaker has incomplete information (she doesn’t know who of John or Bill came). But the interpretations that we considered so far are world states that do not encode different amounts of speaker knowledge. So, to take this into account in Bi-OT (or in any other analysis of Quantity implicatures) we should allow for alternative interpretations that represent different knowledge states of the speaker. Aloni (2007)[^aloni-2007] gives a Bi-OT account of ignorance implicatures (inferences, like the above, that the speaker lacks certain bits of possibly relevant information), alongside *indifference implicatures* (that the speaker does not consider bits of information relevant enough to convey). Moreover, it can be shown that, as far as ignorance implicatures are concerned, the predictions of Bi-OT line up with the pragmatic interpretation function called ‘*Grice*’ in various (joint) papers of Schulz and Van Rooij (e.g., Schulz & Van Rooij, 2006)[^schulz-2006]. In these papers it is claimed that *Grice* implements the Gricean maxim of Quality and the first maxim of Quantity, and it is shown that in terms of it (together with an additional assumption of competence) we can account for many conversational implicatures, including the ones of (1) and (2).

### 1.2 A Bi-OT analysis of Horn’s division

Bi-OT can also account for *Horn’s division of pragmatic labor* or *M-implicatures*, as they are alternatively sometimes called after Levinson (2000)[^levinson-2000]. From this division of pragmatic labor it follows, according to Horn, that while (morphologically) *unmarked* expressions typically get an unmarked, or stereotypical interpretation via Grice’s maxim of Relation, *marked* expressions—being morphologically complex and less lexicalised—tend to receive a marked, non-stereotypical, interpretation. Horn (1984)[^horn-1984] claimed that this follows from the interaction between both Gricean submaxims of Quantity, and the maxims of Relation and Manner, and that for the interpretation of marked expressions it is crucial that an alternative unmarked expression is available as well. To illustrate, consider the following well-known example:

1. John killed the sheriff.
2. John caused the sheriff to die.

We typically interpret the unmarked (3) as meaning stereotypical killing (on purpose), while the marked (4) suggests that John killed the sheriff in a more indirect way, maybe unintentionally. Blutner (1998, 2000)[^blutner-1998][^blutner-2000] shows that this can be accounted for in Bi-OT. Take $i_{st}$ to be the more plausible interpretation where John killed the sheriff in the stereotypical way, while $i_{\neg st}$ is the interpretation where John caused the sheriff’s death in an unusual way. Because (3) is less complex than (4), and $i_{st}$ is the more stereotypical interpretation compatible with the semantic meaning of (3), it is predicted that (3) is interpreted as $i_{st}$. Thus, in terms of his notion of *strong* optimality, i.e., optimality for both speaker and hearer, Blutner can account for the intuition that sentences typically get the most plausible, or stereotypical, interpretation. In terms of this notion of optimality, however, Blutner is not able yet to explain how the more complex form (4) can have an interpretation at all, in particular, why it will be interpreted as non-stereotypical killing. The reason is that on the assumption that (4) has the same semantic meaning as (3), the stereotypical interpretation would be hearer-optimal not only for (3), but also for (4).

To account for the intuition that (4) is interpreted in a non-stereotypical way, Blutner (2000)[^blutner-2000] introduces a weaker notion of optimality that also takes into account a notion of *blocking*: one form’s pragmatically assigned meaning can take away, so to speak, that meaning from another, less favorable form. In the present case, the stereotypical interpretation is intuitively blocked for the cumbersome form (4) by the cheaper alternative expression (3). Formally, a form-interpretation pair $\langle f,i\rangle$ is **weakly optimal**[^note-3] iff there is neither a strongly optimal $\langle f,i'\rangle$ such that $\langle f,i'\rangle \gt \langle f,i\rangle$ nor a strongly optimal $\langle f',i\rangle$ such that $\langle f',i\rangle \gt \langle f,i\rangle$. All form-interpretation pairs that are strongly optimal are also weakly optimal. However, a pair that is not strongly optimal like $\langle$(4),$i_{\neg st}\rangle$ can still be weakly optimal: since neither $\langle$(4),$i_{st}\rangle$ nor $\langle$(3),$i_{\neg st}\rangle$ is strongly optimal, there is no objection for $\langle$(4),$i_{\neg st}\rangle$ to be a (weakly) optimal pair. As a result, the marked (4) will get the non-stereotypical interpretation. In general, application of the above definition of weak optimality can be difficult, but Jäger (2002)[^jäger-2002] gives a concise algorithm for computing weakly optimal form-interpretation pairs.

## 2. Implicatures and Game Theory

The first to systematically explore the use of game theory for an account of communication as *strategic inference* was Prashant Parikh in his 1988 dissertation (Parikh 1988)[^parikh-1988]. Parikh’s theory is based on what he calls *games of partial information*, revolves around the game-theoretic solution concept of *Pareto-optimal Nash equilibrium* and has been refined and applied to various phenomena, including but not restricted to implicature-strengthened utterance meaning, in a series of articles and monographs (e.g., Parikh 1991, 1992, 2000, 2001, 2010, 2019, 2024)[^parikh-1991][^parikh-1992][^parikh-2000][^parikh-2001][^parikh-2010][^parikh-2019][^parikh-2024]. Another noteworthy early contribution is the work of Asher, Sher, and Williams (2001), which tries to rationalize Grice’s Maxims of Conversation using ideas from game theory. In the following we focus on approaches to implicatures based on so-called iterative reasoning in signaling games. The relation between optimality theory and game theory is explored by Dekker and van Rooij (2000) and Franke and Jäger (2012). Stevens and Benz (2018) give another insightful overview of game-theoretic pragmatics.

### 2.1 Signaling games

David Lewis (1969)[^lewis-1969] introduced signaling games to explain how messages can be used to communicate something, although these messages do not have a pre-existing meaning. In pragmatics we want to do something similar: explain what is actually communicated by an expression whose actual interpretation is underspecified by its conventional semantic meaning. To account for pragmatic inferences in game theory, Parikh (1991, 1992)[^parikh-1991][^parikh-1992] introduced games of partial information. These games are much like Lewis’s original signalling games, except that messages are taken to have a conventional semantic meaning, and speakers are assumed to say only messages that are true. In the interest of a broad overview, we gloss over interesting but subtle differences between Lewis’ signaling games and Parikh’s games of partial information.

A signaling game, then, is a game of asymmetric information between a sender $s$ and a receiver $r$. The sender observes the state $t$ that $s$ and $r$ are in, while the receiver has to perform an action. Sender $s$ can try to influence the action taken by $r$ by sending a message. $T$ is the set of states, $F$ the set of forms, or messages. The messages already have a semantic meaning, given by the semantic interpretation function $\llbracket \cdot \rrbracket$ which assigns to each form a subset of $T$. The sender will send a message/form in each state, a *sender strategy* $S$ is thus a function from $T$ to $F$. The receiver will perform an action after hearing a message with a particular semantic meaning, but for present purposes we can think of actions simply as interpretations. A *receiver strategy* $R$ is then a function that maps a message to an interpretation, i.e., a subset of $T$. A *utility function* for speaker and hearer represents what interlocutors care about, and so the utility function models what speaker and hearer consider to be relevant information (implementing Grice’s Maxim of Relevance). For simplicity, it is normally assumed that the utility functions of $s$ and $r (U_s$ and $U_r)$ are the same (implementing Grice’s cooperative principle), and that they depend on (i) the actual state $t$, (ii) the receiver’s interpretation, $i$, of the message $f$ sent by $s$ in $t$ according to their respective strategies $R$ and $S$, i.e., $i = R(S(t))$, and (iii) (in section 2.3) the form $f = S(t)$ used by the sender. Nature is taken to pick the state according to some (commonly known) probability distribution $P$ over $T$. With respect to this probability function, the expected, or average, utility of each sender-receiver strategy combination $\langle S,R\rangle$ for player $e \in \{s,r\}$ can be determined as follows:

$$ \text{EU}_e (S,R)= \sum_{t\in T} P(t) \times U_e (t,S(t),R(S(t))). $$

A signaling game is taken to be a (simplified, abstract) model of a single utterance and its interpretation, which includes some of the arguably most relevant features of a context for pragmatic reasoning: an asymmetry of information (speaker knows the world state, hearer does not), a notion of utterance alternatives (in the set of messages/forms) with associated semantic meaning, and a flexible representation of what counts as relevant information (via utility functions). If this is not enough, e.g., if we want the listener to have partial information not shared by the speaker as well (such as when the speaker is uncertain about what is really relevant for the listener), that can easily be accommodated into a more complex game model, but we refrain from going more complex here. The strategies of sender and receiver encode particular ways of using and interpreting language. The notion of expected utility evaluates how good ways of using and interpreting language are (in the given context). Game-theoretic explanations of pragmatic phenomena aim to single out those sender-receiver strategy pairs that correspond to empirically attested behavior as optimal and/or rational solution of the game problem.

The standard solution concept of game theory is *Nash equilibrium*. A Nash equilibrium of a signaling game is a pair of strategies $\langle$*S$^*$*,*R$^*$*$\rangle$ which has the property that neither the sender nor the receiver could increase his or her expected utility by unilateral deviation. Thus, *S$^*$* is a best response to *R$^*$* and *R$^*$* is a best response to *S$^*$*. There are plenty of refinements of Nash equilibrium in the game-theoretic literature. Moreover, there are alternatives to equilibrium analyses, the two most prominent of which are: (i) explicit formalizations of agents’ reasoning processes, such as is done in epistemic game theory (e.g., Perea 2012)[^perea-2012], and (ii) variants of evolutionary game theory (e.g., Sandholm 2010)[^sandholm-2010] that study the dynamic changes in agents’ behavioral disposition under gradual optimization procedures, such as by imitation or learning from parents. These issues are relevant for applications to linguistic pragmatics as well, as we will demonstrate presently with the example of M-implicatures/Horn’s division of pragmatic labor.

### 2.2 A game-theoretic explanation of Horn’s division

Parikh (1988, 1991, 1992)[^parikh-1988][^parikh-1991][^parikh-1992] proposed the use of game theory to account for disambiguation and implicature. As it turns out, the same proposal can be used to account for Horn’s division of pragmatic labour as well. Parikh assumes that a message, or form, $f_u$, is semantically ambiguous, and can have a stereotypical interpretation, $t_{st}$, and a non-stereotypical interpretation $t_{\neg st}$, with $P(t_{st}) \gt P(t_{\neg st})$. Both meanings, however, could be expressed unambiguously as well by a more complex form. Interpretation $t_{\neg st}$, for instance, can be expressed not only by $f_u$, but by form $f_m$ as well that literally expresses it. As is usual in so-called costly signalling games, and also consistent with Parikh’s proposal, the sender’s utility function can be decomposed into a benefit and a cost function, $U_s (t,f,i) = B_s (t,i) - C(f)$, where $i$ is an interpretation. We adopt the following benefit function: $B_s (t,i) = 1$ if $i = t$, and $B_s (t,i) = 0$ otherwise. The cost of the ambiguous message $f_u$ is lower than the cost of the unambiguous message $f_m$. We can assume without loss of generality that $C(f_u) = 0 \lt C(f_m)$. In the use of signalling games for the analysis of human communication it is standard to assume that it is always better to have successful communication with a costly message than unsuccessful communication with a cheap message, which means that $C(f_m)$, though greater than $C(f_u)$, must remain reasonably small. If we limit ourselves to a game with 2 states, $t_{st}$ and $t_{\neg st}$, and three messages, $f_u$ and the two forms that literally express the two states, and think of sender and receiver strategies as before, the combination of sender and receiver strategies that gives rise to the bijective mapping $\{\langle t_{st},f_u\rangle , \langle t_{\neg st},f_m\rangle \}$ is a Nash equilibrium of this game. Intuitively, this is also the correct solution of the disambiguation game, because the ambiguous message $f_u$ expresses the stereotypical interpretation $t_{st}$, while the non-stereotypical state $t_{\neg st}$ is expressed by the marked and costlier message $f_m$. Unfortunately, also the mapping $\{\langle t_{st},f_m\rangle , \langle t_{\neg st},f_u\rangle \}$—where the lighter message denotes the non-stereotypical situation—is a Nash equilibrium of the game, which means that on the present implementation the standard solution concept of game theory cannot yet single out the desired outcome.

This is were considerations of equilibrium refinements and/or alternative solution concepts come in. Parikh (1988, 1991, 1992)[^parikh-1988][^parikh-1991][^parikh-1992] observes that of the two equilibria mentioned above, the first one Pareto-dominates the second—being the unique Pareto-Nash equilibrium—and that for this reason the former should be preferred. Van Rooij (2004)[^rooij-2004] suggests that because Horn’s division of pragmatic labor involves not only language use but also language organization, one should look at signaling games from an evolutionary point of view, and make use of those variants of evolutionary game theory that explain the emergence of Pareto-optimal solutions. As a third alternative, following some ideas of De Jaegher (2008)[^de-2008], van Rooij (2008)[^rooij-2008] proposes that one could also make use of forward induction (a particular game-theoretic way of reasoning about surprising moves of the opponent) to single out the desired equilibrium. As an example of an approach that draws on detailed modelling of the epistemic states of interlocutors, Franke (2014a)[^franke-2014a] suggests that we should distinguish cases of M-implicature that involve rather clear *ad hoc* reasoning, such as (5) and (6), from cases with a possibly more grammaticalized contrast, such as between (3) and (4).

1. Mrs T sang ‘Home Sweet Home’.
2. Mrs T produces a series of sounds roughly corresponding to the score of ‘Home Sweet Home’.

Franke suggests that the game model for reasoning about (5) and (6) should contain an element of asymmetry of alternatives: whereas it is reasonable (for a speaker to expect that) a listener would consider (5) to be an alternative utterance when hearing (6), it is quite implausible that (a speaker believes that) a listener will consider (6) a potential alternative utterance when hearing (5). This asymmetry of alternatives translates into different beliefs that the listener will have about the context after different messages. The speaker can anticipate this, and a listener who has actually observed (6) can reason about his own counterfactual context representation that he would have had if the speaker had said (5) instead. Franke shows that, when paired with this asymmetry in context representation, a simple model of iterated best response reasoning, to which we turn next, gives the desired result as well.

### 2.3 Quantity implicatures and iterated reasoning

Unlike the case of M-implicatures, many Quantity implicatures hinge on the fact that alternative expressions differ with respect to logical strength: the inference from ‘three’ to the pragmatically strengthed ‘exactly three’-reading, that we sketched in Section 1.1, draws on the fact that the alternative expression ‘four’ is semantically stronger, i.e., ‘four’ semantically entails ‘three’, but not the other way around, under the assumed ‘at least’-semantics. In order to bring considerations of semantic strength to bear on game-theoretic pragmatics, we must assign conventional meaning some role in either the game model or the solution concept. In the following, we look at two similar, but distinct possibilities of treating semantic meaning in approaches that spell out pragmatic reasoning as chains of (higher-order) reasoning about interlocutors’ rationality.

A straightforward and efficient way of bringing semantic meaning into game-theoretic pragmatics is to simply restrict the set of viable strategies of sender and receiver in a signaling game to those strategies that conform to conventional meaning: a sender can only select forms that are true of the actual state, and the receiver can only select interpretations which are in the denotation of an observed message. This may seem crude and excludes cases of non-literal language use, lying, cheating and error from the start, but it may serve to rationalize common patterns of pragmatic reasoning among cooperative, information-seeking interlocutors. Based on such a restriction to truth-obedient strategies, it has been shown independently by Pavan (2013)[^pavan-2013] and Rothschild (2013)[^rothschild-2013] that there is an established non-equilibrium solution concept that nicely rationalizes Quantity implicatures, namely *iterated admissibility*, also known as *iterated elimination of weakly dominated strategies*. Without going into detail, the general idea of this solution concept is to start with the whole set of viable strategies (all conforming to semantic meaning) and then to iteratively eliminate all strategies $X$ for which there is no *cautious belief* about which of the opponent’s remaining strategies the opponent will likely play that would make $X$ a rational thing to do. (A cautious belief is one that does not exclude any opponent strategy that has not been eliminated so far.) The set of strategies that survive repeated iterations of elimination are then compatible with (a particular kind of) common belief in rationality. In sum, iterated admissibility is an eliminative approach: starting from the set of all (truth-abiding) strategies, some strategies are weeded out at every step until we remain with a stable set of strategies from which nothing can be eliminated anymore.

An alternative to restricting attention to only truthful strategies is to use semantic meaning to constrain the starting point of pragmatic reasoning. Approaches that do so are the *optimal assertions approach* (Benz 2006, Benz & van Rooij 2007)[^benz-2006][^benz-2007], *iterated best response models* (e.g., Franke 2009, 2011, Jäger 2014)[^franke-2009][^franke-2011][^franke-2014][^jäger-2014], and related *probabilistic models* (e.g., Frank & Goodman 2012, Goodman & Stuhlmüller 2013, Franke & Jäger 2014)[^frank-2012][^franke-2014][^goodman-2013][^jäger-2014]. The general idea that unifies these approaches can be traced directly to Grice, in particular the notion that speakers should maximize the amount of relevant information contained in their utterances. Since information contained in an utterance is standardly taken to be semantic information (as opposed to pragmatically restricted or modulated meaning), a simple way of implementing Gricean speakers is to assume that they choose utterances by considering how a literal interpreter would react to each alternative. Pragmatic listeners then react optimally based on the belief that the speaker is Gricean in the above sense. In other words, these approaches define a sequence of Theory-of-Mind reasoning: starting with a (non-rational, dummy) literal interpreter, a Gricean speaker acts (approximately) rationally based on literal interpretation, while a Gricean listener interprets (approximately) rationally based on the behavior of a Gricean speaker. Some contributions allow for further iterations of best responses, others do not; some contributions also look at reasoning sequences that start with literal senders; some contributions assume that agents are strictly rational, others allow for probabilistic approximations to classical rational choice (see Franke & Jäger 2014 for overview and comparison)[^franke-2014][^jäger-2014].

A crucial difference between iterated best response approaches and the previously mentioned approach based on iterated admissibility is that the former does not shrink a set of strategies but allows for a different set of best responses at each step. This also makes it so that (some) iterated best response approaches can deal with pragmatic reasoning in cases where interlocutors’ preferences are not aligned, i.e., where the Gricean assumption of cooperativity does not hold, or where there are additional incentives to deviate from semantic meaning (for more about game models for reasoning in non-cooperative contexts, see, e.g., Franke, de Jager & van Rooij 2012, de Jaegher & van Rooij 2014, Franke & van Rooij 2015)[^franke-2012][^franke-2014][^franke-2012-2][^franke-2015]. Another difference between iterated best response models and iterated admissibility is that the latter do not by itself account for Horn’s division of pragmatic labor (see Franke 2014b and Pavan 2014 for discussion)[^franke-2014b][^franke-2014][^pavan-2014].

To illustrate how iterated best response reasoning works in a simple (cooperative) case, let us look briefly at numerical expressions again. Take a signaling game with 4 states, or worlds, $W = \{w_1, w_2, w_3, w_4\}$ where the indices give the exact/maximal number of children that came to our party, and four messages $F = \{$‘one’,‘two’,‘three’, ‘four’$\}$, as shorthand for ‘$n$ children came to our party’. On a neo-Gricean ‘at least’-interpretation of numerals, the meanings of the numeral expressions form an implication chain:

$$ \llbracket `\text{four}\rsquo \rrbracket \subset \llbracket `\text{three}\rsquo \rrbracket \subset \llbracket `\text{two}\rsquo \rrbracket \subset \llbracket `\text{one}\rsquo \rrbracket, $$

because, for instance, $\llbracket$‘three’$\rrbracket = \{w_3, w_4\}$. A literal interpreter, who is otherwise oblivious to contextual factors, would respond to every message by choosing any true interpretation with equal probability. So, for instance, if the literal interpreter hears ‘three’, he would choose $w_3$ or $w_4$, each with probability $½$. But that means that an optimal choice of expression for a speaker who wants to communicate that the actual world is $w_3$ would be ‘three’, because this maximizes the chance that the literal interpreter selects $w_3$. Concretely, if the speaker chooses ‘one’, the chance that the literal listener chooses $w_3$ is ¼; for ‘two’ it’s ⅓; for ‘three’ it’s $½$, and for ‘four’ it’s zero, because $w_3$ is not an element of $\llbracket$‘three’$\rrbracket$. So, a rational Gricean speaker selects $\llbracket$‘three’$\rrbracket$ in $w_3$ and nowhere else, as is easy to see by a parallel argument for all other states. But that means that a Gricean interpreter who hears ‘three’ will infer that the actual world must be $w_3$.

Different extensions of this pragmatic reasoning scheme have been proposed in later work. One is to include probabilistic choice functions to model agents’ approximately rational choices, so as to allow for a much more direct link with experimental data (for overview see Franke & Jäger 2016, Goodman & Frank 2016)[^franke-2016][^goodman-2016]. Such probabilistic pragmatic models have been applied to a number of phenomena of interest, including reasoning about referential expressions in context (Frank & Goodman 2012)[^frank-2012], ignorance implicatures (Goodman & Stuhlmüller 2013)[^goodman-2013], context effects on scalar implicatures (Degen et al. 2015)[^degen-2015], non-literal interpretation of number terms (Kao et al. 2014)[^kao-2014], pragmatic meaning modulation associated with particular intonation (Bergen & Goodman 2015, Stevens 2016)[^bergen-2016][^bergen-2015][^goodman-2016][^stevens-2016], and Quantity implicatures in complex sentences (Bergen et al. 2016, Potts et al. 2016)[^bergen-2016][^potts-2016]. These models of pragmatic reasoning have furthermore been used successfully also in natural language processing applications (Andreas & Klein 2016, Monroe et al. 2017)[^andreas-2016][^monroe-2017] and other areas of linguistic research, such as sociolinguistics (Burnett 2019)[^burnett-2019]. Another recent approach is to allow for uncertainty of the semantic meanings of the involved expressions, and for uncertainty of the beliefs and preferences of the participants of thee conversation and of other aspects of the ‘common ground’ (e.g., Brochhagen 2017)[^brochhagen-2017]. Finally, in recent work more pragmatic phenomena are accounted for than just generalised conversational implicatures, such as particular conversational implicature, explicatures or free enrichment (e.g., Parikh 2010)[^parikh-2010], the analysis of presupposition (Qing et al. 2016)[^qing-2016], and politeness (e.g. Clark 2012, Yoon et al. 2020)[^clark-2012][^yoon-2020].

## 3. Conclusion

Bidirectional Optimality Theory and Game Theory are quite natural, and similar, frameworks to formalize Gricean ideas about interactive, goal-oriented pragmatic reasoning in context. Recent developments turn towards epistemic or evolutionary game theory or to probabilistic models for empirical data. Finally, we remark that formal techniques similar to what is explored here are applicable to a wider range of problems in diverse areas, such as philosophy (e.g., Parikh 2019)[^parikh-2019], language evolution (e.g., Ahern and Clark 2014; Brochhagen, Franke, and Rooij 2018; Carcassi 2020)[^ahern-2014][^brochhagen-2018][^carcassi-2020], as well as computational linguistics (e.g. Vogel et al. 2014, Cohn-Gordon, Goodman, and Potts 2019)[^cohn-gordon-2019][^vogel-2014].

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=implicature-optimality-games). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/implicature-optimality-games/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=implicature-optimality-games&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/implicature-optimality-games/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

- [Probabilistic language understanding: An introduction to the Rational Speech Act framework](http://www.problang.org/), an interactive web-book, by Gregory Scontras, Michael Henry Tessler and Michael Franke, which introduces probabilistic pragmatic reasoning models.

## Related Entries

defaults in semantics and pragmatics | game theory | Grice, Paul | implicature | logic: and games | pragmatics

## Notes（原文脚注）

[^note-1]: This assumption is controversial. Those who don’t accept this assumption should think of other examples where the semantic meanings of the alternative expressions form a linear chain with respect to inference. The scale $\langle \text{and, or} \rangle$ would do equally well, just as $\langle \text{all, most, some} \rangle$, if the quantifiers ‘all’ and ‘most’ give rise to an existential presupposition.

[^note-2]: The choice of alternative expressions is crucial for any analysis of Quantity implicatures. Gazdar (1979)[^gazdar-1979], among others, assumes that alternatives are *conventionally* associated with certain lexical items. It seems more natural, however, to assume that this choice depends (also) on the question being asked, and/or what is relevant in the conversation (see, for instance, van Rooij, 2004)[^rooij-2004].

[^note-3]: This definition is less general than Blutner’s actual definition, but comes down to the same for the example at hand.

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
