# logic-inductive — appendix2（supplement）

> （《logic-inductive》词条补充材料，源：plato.stanford.edu/entries/logic-inductive/appendix2.html）

#### Supplement to Inductive Logic

## Appendix 2

## Axioms and Some Theorems for Conditional Probability

In this appendix we cover two topics. First we will show how several important theorems about probabilities, stated in the main text, can be derived from the axioms supplied in the main text. Second, an alternative axiomatization of conditional probability will be stated. These alternative axioms are individually much weaker than the usual axioms supplied in the main text, but they are jointly equivalent to those axioms — i.e. the axioms in the main text are derivable from these weaker axioms, and *vice versa*.

Let’s first restate the axioms from the main text.

Let $L$ be a language of interest — i.e. any bit of language in which the inductive arguments of interest may be expressed — and let $\vDash$ be the logical entailment relation for this language. A conditional probability function (i.e. a probabilistic support function) is a function $P$ from pairs of statements of $L$ to real numbers that satisfies (at least) the following axioms.

1. There are statements $U$, $V$, $X$, and $Y$ such that $P[U \mid V] \neq P[X \mid Y]$ this *nontrivality axiom* rules out the function $P$ that assigns probability value 1 to every argument;

For all statements $A$, $B$, and $C$ in $L$:

1. $0 \le P[A \mid B] \le 1$ premises support conclusions to some degree measured by real numbers between 0 and 1;
2. If $B \vDash A$, then $P[A \mid B] = 1$ the premises of a logical entailment support its conclusion to degree 1;
3. If $C \vDash B$ and $B \vDash C$, then $P[A \mid B] = P[A \mid C]$ logically equivalent premises support a conclusion to the same degree;
4. If $C \vDash \neg(A \cdot B)$, then $P[(A \vee B) \mid C] = P[A \mid C] + P[B \mid C]$, unless $P[D \mid C] = 1$ for every statement $D$;
5. $P[(A \cdot B) \mid C] = P[A \mid (B \cdot C)] \times P[B \mid C]$.

Here are the theorems stated in the main text, together with their derivations.

- $P[\neg A \mid C] = 1 - P[A \mid C]$, unless $P[D \mid C] = 1$ for every statement $D$. *Proof*: From axioms 3 and 5 we have $1 = P[A \vee \neg A \mid C] = P[A \mid C] + P[\neg A \mid C]$, so $1 - P[A \mid C] = P[\neg A \mid C]$, *unless* $P[D \mid C] = 1$ for all statements $D$.
- If $(C \cdot B) \vDash A$, then $P[A \mid C] \ge P[B \mid C]$. *Proof*: Suppose that $(C \cdot B) \vDash A$. Then (it’s a theorem of deductive logic that) $C \vDash \neg (B \cdot \neg A)$. So, from axioms 2 and 5 we have, *unless* $P[D \mid C] = 1$ for all statements $D$, $1 \ge P[B \vee \neg A \mid C] =$ $P[B \mid C] + P[\neg A \mid C] =$ $P[B \mid C] + 1 - P[A \mid C]$, so $0 \ge P[B \mid C] - P[A \mid C]$, so $P[A \mid C] \ge P[B \mid C]$.
- If $(C \cdot B) \vDash A$ and $(C \cdot A) \vDash B$, then $P[A \mid C] = P[B \mid C]$. *Proof*: Follows directly from Theorem 2.
- Let $A_1$, $A_2$, …, $A_n$ be $n$ statements such that, for each pair of them $A_i$ and $A_j$, $C \vDash \neg(A_i \cdot A_j)$. Then $P[(A_1 \vee (A_2 \vee (A_3 \vee (\ldots \vee (A_{n-1} \vee A_n)\ldots)))) \mid C] =$ $P[A_1 \mid C] + P[A_2 \mid C] + \ldots + P[A_n \mid C]$, unless $P[D \mid C] = 1$ for every statement $D$. *Proof*: Follows by mathematical induction on the number $n$ of disjuncts. Axiom 5 is the basis case, where $n = 2$. The induction hypothesis is to suppose it holds for $n = k$ disjuncts. Then show that it holds for $n = k+1$ disjuncts. By the induction hypothesis it holds for the $k$ disjuncts $A_2$, …, $A_{k+1}$. And it holds for the two disjuncts consisting of $A_1$ and the sentence $(A_2 \vee (A_3 \vee (\ldots \vee (A_{k} \vee A_{k+1}) \ldots)))$. So it holds for all $k+1$ disjuncts.

Here is an alternative, weaker-looking collection of axioms for conditional probability. This axiomatzation does not even assume that the probability values lie between 0 and 1. Rather, that can be proved from these axioms. Indeed, all of the above standard axioms (and theorems) can be proved from these axioms.

Let $L$ be a language of interest — i.e. any bit of language in which some inductive arguments of interest may be expressed — and let $\vDash$ be the logical entailment relation for this language. A conditional probability function (i.e. a probabbilistic support function) is a function $P$ from pairs of statements of $L$ to real numbers that satisfies (at least) the following axioms.

1. For some statements $U$, $V$, $X$, and $Y$, $P[U \mid V] \neq P[X \mid Y]$;

For all statements $A$, $B$, and $C$ in $L$:

1. If $B \vDash A$, then $P[A \mid B] \ge P[C \mid C]$;
2. $P[A \mid (B \cdot C)] \ge P[A \mid (C \cdot B)]$;
3. $P[A \mid C] \ge P[(A \cdot B) \mid C]$;
4. $P[(A \cdot C) \mid C] \ge P[A \mid C ]$;
5. $P[C \mid C] = P[(A \cdot C) \mid C] + P[(\neg A \cdot C) \mid C]$, unless $P[\neg C \mid C] \ge P[C \mid C]$;
6. $P[((A \cdot B) \cdot C) \mid C] = $ $P[(A \cdot (B \cdot C)) \mid (B \cdot C)] \times P[(B \cdot C) \mid C]$.
