# artificial-intelligence — oscar（supplement）

> （《artificial-intelligence》词条补充材料，源：plato.stanford.edu/entries/artificial-intelligence/oscar.html）

#### Supplement to Artificial Intelligence

## The OSCAR Project

OSCAR, according to Pollock, will eventually be not just an intelligent computer program, but an artificial person. (Lest it be thought that this is spinning Pollock’s work in the direction of the stunningly ambitious, note that the subtitle of (Pollock 1995) is “A Blueprint for How to Build a Person,”, and that his prior book (1989) was *How to Build a Person*.) However, though persons have an array of perceptual powers (effectors that allow them to manipulate their environments, linguistic abilities, etc.) OSCAR, at least in the near term, will not have this breadth. OSCAR’s strong suit is the “intellectual” side of personhood. Pollock thus intends OSCAR to be an “artificial intellect”, or, to use his neologism, an artilect. An artilect is a rational agent; Pollock’s concern is thus with rationality. As to the roles of AI and philosophy addressing this concern, Pollock writes:

> The implementability of a theory of rationality is a necessary condition for its correctness. This amounts to saying that philosophy needs AI just as much as AI needs philosophy. A partial test of the correctness of a theory of rationality is that it can form the basis of an autonomous rational agent, and to establish that conclusively, one must actually build an AI system implementing the theory. It behooves philosophers to keep this in mind when constructing their theories, because it takes little reflection to see that many kinds of otherwise popular theories are not implementable. (Pollock 1995: xii)

The distinguishing feature of OSCAR *qua* artilect, at least so far, is that the system is able to perform sophisticated defeasible reasoning.^{[[^note-o1]]} The study of defeasible reasoning was started by Roderick Chisholm (1957, 1966, 1977) and Pollock (1965, 1967, 1974), long before AI took the project under a different name (nonmonotonic reasoning). Both Chisholm and Pollock, as we noted above, assume that reasoning proceeds by constructing *arguments*, and Pollock takes reasons to provide the atomic links in arguments. Conclusive reasons are reasons that aren’t defeasible; conclusive reasons logically entail their conclusions. On the other hand, prima facie reasons provide support for their conclusions, but can be defeated. Defeaters overthrow or defeat prima facie reasons, and come in two forms: defeaters can provide a reason for denying the conclusion, and they can also attack the connection between the premises and the conclusion. As an example of the latter given by Pollock, consider: The proposition ‘$a$ looks red to me’ is a prima facie reason for an agent to believe ‘$a$ is red’. But if you know as well that $a$ is illuminated by red lights, and that such lights can make things look red when they aren’t, the connection is threatened. You don’t have a reason for thinking that it’s not the case that $a$ is red, but the inference in question is shot down: it’s defeated.

We can bring a good deal of this to life, even within our space constraints, by considering how OSCAR supplies a solution to the lottery paradox (LP), which arises as follows. Suppose you hold one ticket $t_k$, for some $k \leq 1000000$, in a fair lottery consisting of 1 million tickets, and suppose it is known that one and only one ticket will win. Since the probability is only $.000001$ of $t_k$’s being drawn, it seems reasonable to believe that $t_k$ will not win. (Of course, to make this side of the apparent antinomy more potent, we can stipulate that the lottery has, say, a *quadrillion* tickets. In this case, it’s probably much more likely that you will be struck dead by a meteorite the next time you leave a building, than it is that you will win. And isn’t it true that you firmly believe, now, that when you walk outside tomorrow you *won’t* be struck dead in this way? If so, then presumably you should believe, of your ticket, that it won’t win!) By the same reasoning it seems that you ought to believe that $t_1$ will not win, that $t_2$ will not win, …, that $t_{1000000}$ will not win (where you skip over $k$). Therefore it is reasonable to believe $$ \lnot \exists t_i \mbox{($ t_i$ will win)} $$ But on the other hand we know that $$ \exists t_i \mbox{($ t_i$ will win)} $$ We thus find ourselves caught in an outright contradiction (or at least caught in a web of irrationality, since believing at once that $\phi$ and $\neg \phi$ seems quite irrational).

What is Pollock’s diagnosis of this paradox? In a nutshell, it’s this: Since as rational beings we ought never to believe both $p_i$ and $\lnot p_i$, and since if we know anything we *know* that a certain ticket *will* win, we must conclude that it’s not the case that we ought to believe that $t_k$ will not win. We must replace this belief with a *defeasible* belief based on that fact that we have but a *prima facie* reason for believing that $t_k$ will not win.

Our situation can be described more carefully in Pollockian terms, which indicates that this situation is a case of collective defeat. Suppose that we are warranted in believing $r$ and that we have equally good prima facie reasons for $p_1, p_2, \ldots, p_n$, where $\{p_1, p_2, \ldots, p_n\} \cup r$ is inconsistent, but no proper subset of $p_1,p_2,\ldots, p_n$ is inconsistent with $r$. Then, for every $p_i$: $$ \{r \land p_1 \land \ldots p_{i-1} \land p_{i+1} \land \ldots p_n \} \vdash \lnot p_i $$

In this case we have equally strong support for each $p_i$ and each $\lnot p_i$, so they collectively defeat one another. Here is how Pollock at one point expresses the principle of collective defeat, operative in this case:

> If we are warranted in believing $r$ and we have equally good independent *prima facie* reasons for each member of a minimal set of propositions deductively inconsistent with $r$, and none of these prima facie reasons is defeated in any other way, then none of the propositions in the set is warranted on the basis of these *prima facie* reasons. (Pollock 1995, p. 62)

Recall Pollock’s insistence upon the *implementability* of theories of rationality. The neat thing is that OSCAR allows us to implement collective defeat – indeed, though we will not go that far here, we can even implement in OSCAR the solution to LP (and the paradox of the preface as well, as Pollock (1995) shows). These particular implementations are too detailed and technical to present in the present venue. But we can show here the use of OSCAR to solve, in natural-deductive form, some simple problems in deductive logic that philosophers give students in introductory philosophy and logic. Let’s start by giving OSCAR this problem: $ \{ (p\rightarrow q), (q \lor s) \rightarrow r \} \vdash p \rightarrow r $ The reader will be spared the details concerning how this query is encoded and supplied to OSCAR, and so on. We move directly to what OSCAR instantly returns in response to the query:

```
===========================================================================
ARGUMENT #1
This is an undefeated argument of strength 1.0 for:
      (p -> r)
which is of ultimate interest.

 2. ((q v s) -> r)     GIVEN
 1. (p -> q)     GIVEN
 6. (q -> r)     disj-antecedent-simp from { 2 }
     |----------------------------------------------------------
     | Suppose:  { p }
     |----------------------------------------------------------
     | 3.  p     SUPPOSITION
     | 5.  q     modus-ponens1 from { 1 , 3 }
     | 8.  r     modus-ponens1 from { 6 , 5 }
 9. (p -> r)     CONDITIONALIZATION from { 8 }
===========================================================================
```

Notice how nice this output is: it conforms to the kind of natural deduction routinely taught to students in elementary philosophy and logic. For example, it would be easy enough to have OSCAR solve the bulk of the exercises supplied in *Language, Proof, and Logic* (Barwise & Etchemendy 1999), which teaches the system $\mathcal F$, so named because it’s a Fitch-style natural deduction system. Of course, some of these exercises involve quantifiers. Here is a query that corresponds to one of the hardest problems in (Barwise & Etchemendy 1994), which teaches a natural-deduction system very similar to $\mathcal F$: $$ \vdash \exists x (B(x) \rightarrow \forall y B(y)) $$

Using quantifier shift, OSCAR produces the following as a solution, in less than a tenth of a second.

```
===========================================================================
ARGUMENT #1
This is a deductive argument for:
      (some x)(( Bird x) -> (all y)( Bird y))
 which is of ultimate interest.

    |----------------------------------------------------------
    | Suppose:  { ~(some x)(( Bird x) -> (all y)( Bird y)) }
    |----------------------------------------------------------
    | 2.  ~(some x)(( Bird x) -> (all y)( Bird y))  REDUCTIO-SUPPOSITION
    | 5.  (all x)~(( Bird x) -> (all y)( Bird y))   neg-eg from { 2 }
    | 6.  ~(( Bird x3) -> (all y)( Bird y))     UI from { 5 }
    | 7.  ( Bird x3)     neg-condit from { 6 }
    | 8.  ~(all y)( Bird y)     neg-condit from { 6 }
    | 9.  (some y)~( Bird y)     neg-ug from { 8 }
    | 10.  ~( Bird @y5)     EI from { 9 }
11. (some x)(( Bird x) -> (all y)( Bird y))     REDUCTIO from { 10 , 7 }
===========================================================================
```

How good is OSCAR, matched against the ambitious goal of literally building a person? Here only two points will be made; both should be uncontroversial.

First, certainly expressivity is a problem for OSCAR. Can OSCAR handle reasoning that seems to require intensional operators?^{[[^note-o2]]} There does not appear to be any such work with the system. Perhaps Pollock had such work in mind for the future, but at present, OSCAR is merely at the level of elementary extensional logic. (Of course, the technique of encoding down, encapsulated above, could be used in conjunction with OSCAR.)

A second, and not unrelated, concern, is that while Pollock’s method of finding rigorous innovation by striving to build a system capable of handling paradoxes is fruitful (and doubtless especially congenial to philosophers), the fact is that he has so far based his work on *simple* paradoxes and puzzles. Can OSCAR handle more difficult paradoxes? It would be nice, for example, if OSCAR could automatically find a solution to Newcomb’s Paradox (NP) (Nozick 1970). As some readers will know, this paradox involves constructions (e.g., backtracking conditionals) quite beyond first-order logic. In addition, there are now *infinitary* paradoxes in the literature (e.g., see Bringsjord & van Heuveln 2003), and it’s hard to see how OSCAR could be used to even represent the key parts of these paradoxes. Since some humans dissect and discuss NP and infinitary paradoxes (etc.) in connection with various more expressive logics, humans would appear to be functioning as artilects beyond the reach of at least the current version of OSCAR.

On the other hand, part of the reason for including coverage herein of OSCAR-based AI work is that such a direction, with roots in argument-based epistemology that runs back to the 1950s, the same time modern AI started up (recall that the 1956 Dartmouth conference was held in 1956), promises to continue to provide a fruitful approach into the future. Evidence for this can be found in the form of Pollock’s (2006) *Thinking about Acting: Logical Foundations for Rational Decision Making*, a philosophically sophisticated AI-relevant investigation of planning and rational decision-making for resource-bounded agents. Unfortunately, AI and philosophy lost Pollock prematurely, and after his passing, OSCAR went into a period of quiet stasis. Fortunately, the system has been resurrected by Kevin O’Neill, and can be obtained at [OSCAR, Rensselaer Artificial Intelligence and Reasoning Laboratory (RAIR)](https://rair.cogsci.rpi.edu/projects/automated-reasoners/oscar). Moreover, initial experiments with OSCAR in the area of AI planning indicate a bright future (initial results can be found at [Initial Explorations [RAIR]](https://rair.cogsci.rpi.edu/sep_oscar/)).


## Notes（原文脚注，引自主文）

[^note-o1]: O1. It must be said here that, for a while at least, OSCAR was also distinguished by being quite a fast automated theorem prover (ATP). I say ‘was’ because there has of late been a new wave of faster and faster first-order provers. Speed in machine reasoning is an exceedingly relative concept. What’s fast today is inevitably slow tomorrow; it all hinges on what the competition is doing. In OSCAR’s case, the competition now includes not just the likes of Otter (see e.g. Wos et al. 1992; and go to the [Automated Deduction at Argonne](http://www-unix.mcs.anl.gov/AR/) page for a wonderful set of resources related to Otter), but also Vampire (Vronkov 1995). (Vampire’s core algorithm coincides with Otter’s, but increased speed can come from many sources, including how propositions are indexed and organized.) It seems to me that some of OSCAR’s speed derives from the fact that in searching for proofs OSCAR approximates some form of goal analysis as a technique for finding proofs in a natural deduction format. Goal analysis will be familiar to those philosophers who have taught natural deduction. The performance of OSCAR and other systems can be found at the [TPTP](http://www.cs.miami.edu/%7Etptp) site.

[^note-o2]: O2. Why is this a problem? First-order logic has issues with representing statements of the form *“Person X knows that ‘Roses are red’.”* or *“Person Y does not believe that ‘Roses are red’.”* Such statements are known as *intensional statements*. Statements such as *“Roses are red.”* or “$3^2 + 4^2 = 5^2$” are known as extensional statements. When we try to model intensional statements in first-order logic, we quickly run into problems (Anderson 1983; Bringsjord & Govindarajulu 2012).