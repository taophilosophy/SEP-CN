# logic-inductive — sup-uncertain-inf（supplement）

> （《logic-inductive》词条补充材料，源：plato.stanford.edu/entries/logic-inductive/sup-uncertain-inf.html）

#### Supplement to Inductive Logic

## Some Prominent Approaches to the Representation of Uncertain Inference

The following figure indicates a relationship among six of the most prominent approaches to uncertain inference. The arrows point from more general to less general representation schemes; the double arrow connects a pair of equally general schemes. For example, the *Dempster-Shafer* representation contains the *probability functions* as a special case.

![Figure 1](../assets/logic-inductive/fig1.svg)

*Representations of Uncertainty*

These representations are often described as measures on events, or states, or propositions, or sets of possibilities. But deductive logics are usually described in terms of statements or sentences of a language. So let’s follow suit throughout this discussion.

*Plausibility relations* (Friedman & Halpern 1995) constitute the most general of these representations. They satisfy the weakest axioms, the weakest constraints on the logic of uncertainty. For a *plausibility relation* $\succcurlyeq$ between sentences, an expression ‘$A \succcurlyeq B$’, says that $A$ is at least as plausible as $B$. The axioms for plausibility relations say that tautologies are more plausible than contradictions, any two logically equivalent sentences are plausibility-related to other sentence in precisely the same way, a sentence is no more plausible than the sentences it logically entails, and the *at least as plausible* relation is transitive. These axioms make plausibility relations *weak partial orders* on the relative plausibility of sentences. They permits some sentences to be incomparable with respect to plausibility—neither more plausible, nor less plausible, nor equally plausible to one another.

*Qualitative probability relations* are *plausibility relations* for which three additional axioms are satisfied. One of these additional axioms says that when a sentence $S$ is logically incompatible with both sentence $A$ and sentence $B$, then $A \succcurlyeq B$ holds *just in case* $(A \textrm{ or } S) \succcurlyeq(B \textrm{ or } S)$ holds as well. Now, suppose that a *qualitative probability relation* satisfies one additional (two-part) axiom. Then it can be shown to be *representable* by a *probability function*—i.e., given any *qualitative probability relation* $\succcurlyeq$, there is a unique probability function $P$ such that $A \succcurlyeq B$ just in case $P[A] \ge P[B]$. So quantitative *probability* may be viewed as essentially just a way of placing a numerical measure on sentences that uniquely emulates the *is at least as plausible as* relation specified by *qualitative probability* (see Koopman 1940; Savage 1954; Hawthorne & Bovens 1999; Hawthorne 2009).

*Probability* (i.e., *quantitative probability*) is a measure of *plausibility* that assigns a number between 0 and 1 to each sentence. Intuitively, the *probability* of a sentence $S$, $P[S] = r$, says that $S$ *is plausible to degree r*, or that *the rational degree of confidence (or belief) that* $S$ *is true is* $r$. The axioms for *probabilities* basically require two things. First, tautologies get probability 1. Second, when $A$ and $B$ contradict each other, the probability of the disjunction $(A \textrm{ or } B)$ must be the sum of the probabilities of $A$ and of $B$ individually. It is primarily in regard to this second axiom that *probability* differs from each of the other quantitative measures of uncertainty.

Like *probability*, *Dempster-Shafer belief functions* (Shafer 1976, 1990) measure *appropriate belief strengths* on a scale between 0 and 1, with contradictions and tautologies at the respective extremes. But whereas the *probability* of a disjunction of incompatible claims must equal the sum of the parts, *Dempster-Shafer belief functions* only require such disjunctions be *believed at least as strongly as* the sum of the *belief strengths* of the parts. So these functions are a generalization of *probability*. By simply tightening up the *Dempster-Shafer* axiom about how disjunctions are related to their parts we get back a restricted class of *Dempster-Shafer functions* that just is the class of *probability functions*. *Dempster-Shafer* functions are primarily employed as a logic of evidential support for hypotheses. In that realm they are a generalization of the idea of evidential support embodied by *probabilistic inductive logic*. There is some controversy as to whether such a generalization is useful or desirable, or whether simple *probability* is too narrow to represent important evidential relationships captured by some *Dempster-Shafer functions*.

There is a sense in which the other two quantitative measures of uncertainty, *possibility functions* and *ranking functions*, are definable in terms of formulas employing the *Dempster-Shafer functions*. But this is not the best way to understand them. *Possibility functions* (Zadeh 1965 1978; Dubois & Prade 1980, 1990) are generally read as representing *the degree of uncertainty* in a claim, where such uncertainty is often attributed to vagueness or fuzziness. These functions are formally like *probability functions* and *Dempster-Shafer functions*, but they subscribe to a simpler addition rule: the *degree of uncertainty* of a disjunction is the greater of the *degrees of uncertainty* of the parts. Similarly, the *degree of uncertainty* of a conjunction is the smaller of the *uncertainties* of the parts.

*Ranking functions* (Spohn 1988) supply a measure of how surprising it would be if a claim turned out to be true, rated on a scale from 0 (not at all surprising) to infinity. Tautologies have *rank* 0 and contradictions are infinitely surprising. Logically equivalent claims have the same *rank*. The *rank* of a disjunction is equal to the *rank* of the lower ranking disjunct. These functions may be used to represent a kind of *order-of-magnitude* reasoning about the plausibility of various claims.

See Halpern 2003 for a good comparative treatment of all of these approaches.

Here are the axioms for the *Plausibility Relations* and the *Qualitative Probability Relations*. We may specify them in terms of a formal language $L$ for either sentential logic or for predicate logic. In this formal language we employ the following expressions to represent the standard logical terms: ‘not’, ‘${\neg}$’; ‘and’, ‘$\cdot$’; ‘or’, ‘$\vee$’. We represent the standard *logical entailment* relation with the symbol ‘$\vDash$’—i.e., the expression ‘$B \vDash A$’ says “*B logically entails A*” and the expression ‘$\vDash A$’ says “$A$ is a tautology”.

Axioms for the *Plausibility Relations* Each *plausibility relation* $\succcurlyeq$ satisfies the following axioms:

1. if $\vDash A$, then *not* ${\neg}A \succcurlyeq A$;
2. if $B \vDash A$, then $A \succcurlyeq B$;
3. if $A \vDash B$ and $B \vDash A$ (i.e., if $A$ is logically equivalent to $B$), then: (1) if $A \succcurlyeq C$, then $B \succcurlyeq C$; and (2) if $D \succcurlyeq A$, then $D \succcurlyeq B$;
4. if $A \succcurlyeq B$ and $B \succcurlyeq C$, then $A \succcurlyeq C$.

Axioms for the *Qualitative Probability Relations* To get the *qualitative probability relations* we add the axioms

1. if $\vDash{\neg}(A\cdot C)$ and $\vDash{\neg}(B\cdot C)$, then $A \succcurlyeq B$ if and only if $(A \vee C) \succcurlyeq(B \vee C)$.
2. $A \succcurlyeq B$ or $B \succcurlyeq$ A;

The typical axioms for *quantitative probability* are as follows:

1. for all sentences $A, 0 \le P[A] \le 1$;
2. if $\vDash C$, then $P[C] = 1$;
3. if $\vDash{\neg}(A\cdot B)$, then $P[(A \vee B)] = P[A] + P[B]$.

Axioms 1–6 for the *qualitative probability relations* are probabilistically sound with respect to the quantitative probability functions. That is, for each given probability function $P$, define a relation $\succcurlyeq$ such that $A \succcurlyeq B$ *just in case* $P[A] \ge P[B]$. Then it can be shown that $\succcurlyeq$ must satisfy axioms 1–6. However, not every qualitative probability relation that satisfies axioms 1–6 may be represented by a probability function. To get that we must add one further *structural axiom*.

First we need to define a bit more notation. Two sentences are defined as *equally plausible*, $A \approx B$, just when both $A \succcurlyeq B$ and $B \succcurlyeq A$. One sentence is defined as *more plausible* than another, $A \succ B$, just when $A \succcurlyeq B$ but *not* $B \succcurlyeq A$.

Let’s say that a qualitative probability relation $\succcurlyeq$ is *fine-grained* just in case it satisfies the following axiom:

1. if $A \succ B$, then (for each natural number $n$) there is some tautology consisting of a disjunction of $n$ sentences, $\vDash(S_1 \vee S_2 \vee \ldots \vee S_n)$, where for each distinct $S_i$ and $S_j$ we have $\vDash{\neg}(S_{i} \cdot S_{j})$ (each distinct $S_i$ and $S_j$ are inconsistent with one another) and where $S_i \approx S_j$ (they are equally plausible), and such that for each of the $S_i$, $A \succ(B \vee S_i).$

Think of each sentence $S_i$ as saying that in some fair lottery consisting of $n$ tickets, ticket $i$ will win (where exactly one ticket must win, and where each ticket has the same chance of winning).

It can be proved that for each *fine-grained* qualitative probability relation $\succcurlyeq$ there is a unique probability function $P$ such that $A \succcurlyeq B$ *just in case* $P[A] \ge P[B]$.

Now, call a qualitative probability relation $\succcurlyeq$ *properly extendable* just in case it can be extended to a *fine-grained* qualitative probability relation (perhaps defined on a larger language, i.e., a language containing additional sentences). Then for every *properly extendable* qualitative probability relation $\succcurlyeq$ there is a probability function $P$ such that $A \succcurlyeq B$ *just in case* $P[A] \ge P[B]$. In general a given *properly extendable* qualitative probability relation may have many such representing probability functions, corresponding to different ways of extending it to *fine-grained* qualitative probability relations.

Thus, the quantitative probability functions may be viewed as just useful ways of representing *properly extendable* qualitative probability relations on a convenient numerical scale.

[Back to Text]
