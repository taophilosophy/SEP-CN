# Constructive Mathematics
**First published Tue Nov 18, 1997; substantive revision Thu Aug 25, 2022**

*Bridges, Douglas, Palmgren, Erik, Ishihara, Hajime*

Constructive mathematics is distinguished from its traditional counterpart, classical mathematics, by the strict interpretation of the phrase “there exists” as “we can construct”. In order to work constructively, we need to re-interpret not only the existential quantifier but all the logical connectives and quantifiers as instructions on how to construct a proof of the statement involving these logical expressions.

In this article we introduce modern constructive mathematics based on the BHK-interpretation of the logical connectives and quantifiers. We discuss four major varieties of constructive mathematics, with particular emphasis on the two varieties associated with Errett Bishop and Per Martin-Löf, which can be regarded as minimal constructive systems. We then outline progress in (informal) constructive reverse mathematics, a research programme seeking to identify principles, such as Brouwer’s fan theorem, that, added to the minimal constructive varieties, facilitate proofs of important analytic theorems. After a brief discussion of constructive algebra, economics, and finance, the entry ends with two appendices: one on certain logical principles that hold in classical, intuitionistic, and recursive mathematics and which, added to Bishop’s constructive mathematics, facilitate the proof of certain useful theorems of analysis; and one discussing approaches to a constructive development of general topology.

## 1. Introduction

Before mathematicians assert something (other than an axiom) they are supposed to have proved it true. What, then, do mathematicians mean when they assert a disjunction $P \vee Q$, where $P$ and $Q$ are syntactically correct statements in some (formal or informal) mathematical language? A natural — although, as we shall see, not the unique — interpretation of this disjunction is that not only does (at least) one of the statements $P, Q$ hold, but also we can decide which one holds. Thus just as mathematicians will assert $P$ only when they have decided that $P$ holds by proving it, they may assert $P \vee Q$ only when they either can produce a proof of $P$ or else produce one of $Q$.

With this interpretation, however, we run into a serious problem in the special case where $Q$ is the negation, $\neg P$, of $P$. To assert $\neg P$ is to show that $P$ implies a contradiction (such as $0 = 1)$. But it will often be that mathematicians have neither a proof of $P$ nor one of $\neg P$. To see this, we need only reflect on the following *Goldbach conjecture* (GC):

Every even integer $\gt 2$ can be written as a sum of two primes,

which remains neither proved nor disproved despite the best efforts of many of the leading mathematicians since it was first raised in a letter from Goldbach to Euler in 1742. We are forced to conclude that, *under the very natural decidability interpretation of P* $\vee Q$, only a stubborn optimist can retain a belief in the *law of excluded middle* (**LEM**):

For every statement $P$, either $P$ or $\neg P$ holds.

Classical logic gets round this by widening the interpretation of disjunction: it interprets $P \vee Q$ as $\neg(\neg P\wedge \neg Q)$, or in other words, “it is contradictory that both $P$ and $Q$ be false”. In turn, this leads to the *idealistic* interpretation of existence, in which $\exists xP(x)$ means $\neg \forall x\neg P(x)$ (“it is contradictory that $P(x)$ be false for every $x$”). It is on these interpretations of disjunction and existence that mathematicians have built the grand, and apparently impregnable, edifice of classical mathematics which serves a foundation for the physical, the social, and (increasingly) the biological sciences. However, the wider interpretations come at a cost: for example, when we pass from our initial, natural interpretation of $P \vee Q$ to the unrestricted use of the idealistic one, $\neg(\neg P\wedge \neg Q)$, the resulting mathematics cannot generally be interpreted within computational models such as recursive function theory.

This point is illustrated by a well-worn example, the proposition:

There exist irrational numbers $a, b$ such that $a^b$ is rational.

A slick classical proof goes as follows. Either $\sqrt{2}^{\sqrt{2}}$ is rational, in which case we take $a = b = \sqrt{2}$; or else $\sqrt{2}^{\sqrt{2}}$ is irrational, in which case we take $a = \sqrt{2}^{\sqrt{2}}$ and $b = \sqrt{2}$ (see Dummett 1977 [2000], 6)[^dummett-1977]. But as it stands, this proof does not enable us to pinpoint which of the two choices of the pair $(a,b)$ has the required property. In order to determine the correct choice of $(a,b)$, we would need to decide whether $\sqrt{2}^{\sqrt{2}}$ is rational or irrational, which is precisely to employ our initial interpretation of disjunction with $P$ the statement “$\sqrt{2}^{\sqrt{2}}$ is rational”.

Here is another illustration of the difference between interpretations. Consider the following simple statement about the set $\bR$ of real numbers:

$$ \tag{*} \forall x \in \bR (x = 0 \vee x \ne 0), $$

where, for reasons that we divulge shortly, $x \ne 0$ means that we can find a rational number $r$ with $0 \lt r \lt \abs{x}$. A natural computational interpretation of (*) is that we have a procedure which, applied to any real number $x$, either tells us that $x = 0$ or else tells us that $x \ne 0$. (For example, such a procedure might output 0 if $x = 0$, and 1 if $x \ne 0$.) However, because the computer can handle real numbers only by means of finite rational approximations, we have the problem of *underflow*, in which a sufficiently small positive number can be misread as 0 by the computer; so there cannot be a decision procedure that justifies the statement (*). In other words, we cannot expect (*) to hold under our natural computational interpretation of the quantifier $\forall$ and the connective $\vee$.

Let’s examine this from another angle. Let $G(n)$ act as shorthand for the statement “$2n + 2$ is a sum of two primes”, where $n$ ranges over the positive integers, and define an infinite binary sequence $\ba = (a_1 ,a_2,\ldots)$ as follows:

$$ a_n = \begin{cases} 0 &\text{if } G(k) \text{ holds for all } k \le n \\ 1 &\text{if } \neg G(k) \text{ holds for some } k \le n \\ \end{cases} $$

There is no question that $\ba$ is a computationally well-defined sequence, in the sense that we have an algorithm for computing $a_n$ for each $n$: check the even numbers $4,6,8,\ldots ,2n+2$ to determine whether each of them is a sum of two primes; in that case, set $a_n = 0$, and in the contrary case, set $a_n = 1$. Now consider the real number whose $n$ᵗʰ binary digit is $a_n$:

$$\begin{align*} x &= (0\cdot a_1 a_2 \cdots)_{2} \\ &= 2^{-1}a_1 + 2^{-2}a_2 + \cdots \\ &=\sum_{n=1}^{\infty} 2^{-n}a_n. \end{align*}$$

If (*) holds under our computational interpretation, then we can decide between the following two alternatives:

- $2^{-1}a_1 + 2^{-2}a_2 + \cdots = 0$, which implies that $a_n = 0$ for every $n$;
- we can find a positive integer $N$ such that $2^{-1}a_1 + 2^{-2}a_2 + \cdots \gt 2^{-N}$.

In the latter case, by testing $a_1 ,\ldots ,a_N$, we can find $n \le N$ such that $a_n = 1$. Thus the computational interpretation of (*) enables us to decide whether there exists $n$ such that $a_n = 1$; in other words, it enables us to decide the status of the Goldbach Conjecture. An example of this type, showing that a constructive proof of some classical result $P$ would enable us to solve the Goldbach conjecture (and, by similar arguments, many other hitherto open problems, such as the Riemann hypothesis), is called a *Brouwerian example* for, or even a *Brouwerian counterexample* to, the statement $P$ (though it is not a counterexample in the normal sense of that word).

The use of the Goldbach Conjecture here is purely dramatic. For, the argument of the preceding paragraph can be modified to show that, under our computational interpretation, (*) implies the *limited principle of omniscience* (**LPO**):

For each binary sequence $(a_1 ,a_2, \ldots)$ either $a_n = 0$ for all $n$ or else there exists $n$ such that $a_n = 1$,

which is generally regarded as an essentially nonconstructive principle for several reasons. First, its recursive interpretation,

There is a recursive algorithm which, applied to any recursively defined binary sequence $(a_1 ,a_2, \ldots)$, outputs 0 if $a_n = 0$ for all $n$, and outputs 1 if $a_n = 1$ for some $n$,

is provably false within recursive function theory, even with classical logic (see Bridges & Richman [1987], Chapter 3); so if we want to allow a recursive interpretation of all our mathematics, then we cannot use LPO. Secondly, there is a model theory (Kripke models) in which it can be shown that LPO is not constructively derivable (Bridges & Richman [1987], Chapter 7).

## 2. The Constructive Interpretation of Logic

It should, by now, be clear that a full-blooded computational development of mathematics disallows the idealistic interpretations of disjunction and existence upon which most classical mathematics depends. In order to work constructively, we need to return from the classical interpretations to the natural constructive ones:

| $\vee$ (or): | to prove $P \vee Q$ we must either have a proof of $P$ or have a proof of $Q$. |
| --- | --- |
| $\wedge$ (and): | to prove $P \wedge Q$ we must have both a proof of $P$ and a proof of $Q$. |
| $\Rightarrow$ (implies): | a proof of $P \rightarrow Q$ is an algorithm that converts any proof of $P$ into a proof of $Q$. |
| $\neg$ (not): | to prove $\neg P$ we must show that $P$ implies $0 = 1$. |
| $\exists$ (there exists): | to prove $\exists xP(x)$ we must construct an object $x$ and prove that $P(x)$ holds. |
| $\forall$ (for each/all): | a proof of $\forall x\in S P(x)$ is an algorithm that, applied to any object $x$ and to the data proving that $x\in S$, proves that $P(x)$ holds. |

These *BHK-interpretations* (the name reflects their origin in the work of Brouwer, Heyting, and Kolmogorov) can be made more precise using Kleene’s notion of *realizability*; see (Dummett [1977/2000], 222–234; Beeson [1985], Chapter VII).

There is a common misunderstanding that constructive mathematics is just mathematics without proofs by contradiction (reductio-ad-absurdum arguments). This is *not* the case. Consider typical proofs that $\sqrt{2}$ is irrational: these start with the assumption '$\sqrt{2}$ is rational', then proceed by elementary, and fully constructive, steps to arrive at a contradiction. Such a procedure is a perfectly constructive proof that $\sqrt{2}$ is not rational; indeed, the constructive interpretation of '$\neg p$' is precisely that assuming $p$ leads to a contradiction. The misunderstanding alluded to at this start of this paragraph is caused by confusing a proof, like the foregoing, of a negated statement with one of the following type: assume $\neg p$, derive a contradiction, and conclude that $p$ must hold. From a constructive point of view, the most one can obtain from the latter type of proof is the conclusion $\neg\neg p$; the final step, claiming that $p$ must hold, is nonconstructive.

To reinforce this point, consider a proof of the form

> Assume there is no such thing as a boojum; then argue constructively to arrive at a contradiction.

Such a proof does not normally contain the algorithmic information enabling us to establish *constructively* that there exists a boojum after all. More formally, a constructive proof of $\neg\neg \exists x P(x)$ does not automatically allow us to conclude that $\exists x P(x)$.

To summarise: to prove $\neg p$, we may, and normally do, assume $p$ and derive a contradiction. To prove $p$, it is *not enough* to assume $\neg p$ and derive a contradiction.

We turn now to intuitionistic logic in practice. What sort of things are we looking for if we are serious about developing mathematics in such a way that when a theorem asserts the existence of an object $x$ with a property $P(x)$, then the proof of the theorem embodies algorithms for constructing $x$ and for demonstrating, by whatever calculations are necessary, that $x$ has the property $P(x)$. Here are some examples of theorems, each followed by an informal description of the requirements for its constructive proof.

1. For each real number $x$, either $x = 0$ or $x \ne 0$. *Proof requirement*: An algorithm which, applied to a given real number $x$, decides whether $x = 0$ or $x \ne 0$. Note that, in order to make this decision, the algorithm might use not only the data describing $x$ but also the data showing that $x$ is actually a real number.
2. Each nonempty subset $S$ of $\bR$ *that is bounded above has a least upper bound*. *Proof requirement*: An algorithm which, applied to a set $S$ of real numbers, a member $s$ of $S$, and an upper bound for $S$,
3. computes an object $b$ and shows that $b$ is a real number;
4. shows that $x \le b$ for each $x \in S$; and
5. given a real number $b' \lt b$, computes an element $x$ of $S$ such that $x \gt b'$.
6. If $f$ is a continuous real-valued mapping on the closed interval $[0,1]$ such that $f(0)\cdot f(1) \lt 0$, then there exists $x$ such that $0 \lt x \lt 1$ and $f(x) = 0$. *Proof requirement*: An algorithm which, applied to the function $f$, a modulus of continuity for $f$, and the values $f(0)$ and $f(1)$,
7. computes an object $x$ and shows that $x$ is a real number between 0 and 1; and
8. shows that $f(x) = 0$.
9. If $f$ is a continuous real-valued mapping on the closed interval $[0,1]$ such that $f(0)\cdot f(1) \lt 0$, then for each $\varepsilon \gt 0$ there exists $x$ such that $0 \lt x \lt 1$ and $\abs{f(x)} \lt \varepsilon$. *Proof requirement*: An algorithm which, applied to the function $f$, a modulus of continuity for $f$, the values $f(0)$ and $f(1)$, and a positive number $\varepsilon$,
10. computes an object $x$ and shows that $x$ is a real number between 0 and 1; and
11. shows that $\abs{f(x)} \lt \varepsilon$.

We already have reasons for doubting that (A) has a constructive proof. If the proof requirements for (B) can be fulfilled, then, given any mathematical statement $P$, we can apply our proof of (B) to compute a rational approximation $z$ to the supremum $\sigma$ of the set

$$ S = \{0\} \cup \{x \in \bR: P \wedge x = 1\} $$

with error $\lt \bfrac{1}{4}$. We can then determine whether $z \gt \bfrac{1}{4}$, in which case $\sigma \gt 0$, or $z \lt \bfrac{3}{4}$, when $\sigma \lt 1$. In the first case, there exists $x \in S$ with $x \gt 0$, so we must have $x = 1$ and therefore $P$. In the case $\sigma \lt 1$, we have $\neg P$. Thus (B) implies the law of excluded middle.

However, in Bishop’s constructive theory of the real numbers, based on Cauchy sequences with a preassigned convergence rate, we can prove the following *constructive least-upper-bound principle*:

> Let $S$ be a nonempty subset of $\bR$ that is bounded above. Then $S$ has a least upper bound if and only if it is *upper-order located*, in the sense that for all real numbers $\alpha , \beta$ with $\alpha \lt \beta$, either $\beta$ is an upper bound for $S$ or else there exists $x \in S$ with $x \gt \alpha$ (Bishop & Bridges [1985], p. 37, Proposition (4.3)).

In passing, we mention an alternative development of the constructive theory of $\bR$ based on interval arithmetic; see Chapter 2 of Bridges & Vîță [2006].

Each of statements (C) and (D), which are classically equivalent, is a version of the Intermediate Value Theorem. In these statements, a *modulus of continuity* for $f$ is a set $\Omega$ of ordered pairs $(\varepsilon ,\delta)$ of positive real numbers with the following two properties:

- for each $\varepsilon \gt 0$ there exists $\delta \gt 0$ such that $(\varepsilon ,\delta) \in \Omega$
- for each $(\varepsilon , \delta) \in \Omega$, and for all $x,y \in [0,1]$ with $\abs{x - y} \lt \delta$, we have $\abs{f(x) - f(y)} \lt \varepsilon$.

Statement (C) entails another essentially nonconstructive principle, the *lesser limited principle of omniscience* (**LLPO**):

For each binary sequence $(a_1,a_2,\ldots)$ with at most one term equal to 1, either $a_n = 0$ for all even $n$ or else $a_n = 0$ for all odd $n$.

Statement (D), a weak form of (C), can be proved constructively, using an interval-halving argument of a standard type. The following stronger constructive intermediate value theorem, which suffices for most practical purposes, is proved using an approximate-interval-halving argument:

Let $f$ be a continuous real-valued mapping on the closed interval $[0,1]$ such that $f(0)\cdot f(1) \lt 0$. Suppose also that $f$ is *locally nonzero*, in the sense that for each $x \in [0,1]$ and each $r \gt 0$, there exists $y$ such that $\abs{x - y} \lt r$ and $f(y) \ne 0$. Then there exists $x$ such that $0 \lt x \lt 1$ and $f(x) = 0$.

The situation of the intermediate value theorem is typical of many in constructive analysis, where we find one classical theorem with several constructive versions, some or all of which may be equivalent under classical logic.

There is one omniscience principle whose constructive status is less clear than that of **LPO** and **LLPO**—namely, *Markov’s principle* (**MP**):

For each binary sequence $(a_n)$, if it is contradictory that all the terms $a_n$ equal 0, then there exists a term equal to 1.

This principle is equivalent to a number of simple classical propositions, including the following:

- For each real number $x$, if it is contradictory that $x$ equal 0, then $x \ne 0$ (in the sense we mentioned earlier).
- For each real number $x$, if it is contradictory that $x$ equal 0, then there exists $y \in \bR$ such that $xy = 1$.
- For each one-one continuous mapping $f : [0,1] \rightarrow \bR$, if $x \ne y$, then $f(x) \ne f(y)$.

Markov’s principle represents an unbounded search: if you have a proof that all terms $a_n$ being 0 leads to a contradiction, then, by testing the terms $a_1,a_2,a_3,\ldots$ in turn, you are guaranteed to come across a term equal to 1; but this guarantee does not extend to an assurance that you will find the desired term before the end of the universe. Most practitioners of constructive mathematics view Markov’s principle with at least suspicion, if not downright disbelief. Such views are reinforced by the observation that there is a Kripke Model showing that **MP** is not constructively derivable (Bridges & Richman [1987], 137–138.)

## 3. Varieties of Constructive Mathematics

The desire to retain the possibility of a computational interpretation is one motivation for using the constructive reinterpretations of the logical connectives and quantifiers that we gave above; but it is not exactly the motivation of the pioneers of constructivism in mathematics. In this section we look at some of the different approaches to constructivism in mathematics over the past 130 years.

### 3.1 Intuitionistic Mathematics

In the late nineteenth century, certain individuals—most notably Kronecker and Poincaré—had expressed doubts about, or even disapproval of, the idealistic, nonconstructive methods used by some of their contemporaries; but it is in the polemical writings of L.E.J. Brouwer (1881–1966), beginning with his Amsterdam doctoral thesis, Brouwer [1907], and continuing over the next forty-seven years, that the foundations of a precise, systematic approach to constructive mathematics were laid. In Brouwer’s philosophy, known as intuitionism, mathematics is a free creation of the human mind, and an object exists if and only if it can be (mentally) constructed. If one takes that philosophical stance, then one is inexorably drawn to the foregoing constructive interpretation of the logical connectives and quantifiers: for how could a proof of the impossibility of the non-existence of a certain object $x$ describe a mental construction of $x$?

Brouwer was not the clearest expositor of his ideas, as is shown by the following quotation:

> Mathematics arises when the subject of two-ness, which results from the passage of time, is abstracted from all special occurrences. The remaining empty form [the relation of $n$ to $n+1$] of the common content of all these two-nesses becomes the original intuition of mathematics and repeated unlimitedly creates new mathematical subjects. (quoted in Kline [1972], 1199–2000)

A modern version of Brouwer’s view was given by Errett Bishop (Bishop [1967], p. 2):

> The primary concern of mathematics is number, and this means the positive integers. We feel about number the way Kant felt about space. The positive integers and their arithmetic are presupposed by the very nature of our intelligence and, we are tempted to believe, by the very nature of intelligence in general. The development of the positive integers from the primitive concept of the unit, the concept of adjoining a unit, and the process of mathematical induction carries complete conviction. In the words of Kronecker, the positive integers were created by God.

However obscure Brouwer’s writings could be, one thing was always clear: for him, mathematics took precedence over logic. One might say, as Hermann Weyl did in the following passage, that Brouwer saw classical mathematics as flawed precisely in its use of classical logic without reference to the underlying mathematics:

> According to [Brouwer’s] view and reading of history, classical logic was abstracted from the mathematics of finite sets and their subsets. … Forgetful of this limited origin, one afterwards mistook that logic for something above and prior to all mathematics, and finally applied it, without justification, to the mathematics of infinite sets. This is the Fall and original sin of set theory, for which it is justly punished by the antinomies. It is not that such contradictions showed up that is surprising, but that they showed up at such a late stage of the game. (Weyl [1946])

In particular, this misuse of logic led to nonconstructive existence proofs which, in Weyl’s words, “inform the world that a treasure exists without disclosing its location”.

In order to describe the logic used by the intuitionist mathematician, it was necessary first to analyse the mathematical processes of the mind, from which analysis the logic could be extracted. In 1930, Brouwer’s most famous pupil, Arend Heyting, published a set of formal axioms which so clearly characterise the logic used by the intuitionist that they have become universally known as the axioms for intuitionistic logic (Heyting [1930]). These axioms captured the informal BHK-interpretation of the connectives and quantifiers that we gave earlier.

Intuitionistic mathematics, **INT**, diverges from other types of constructive mathematics in its interpretation of the term “sequence”. Normally, a sequence in constructive mathematics is given by a rule which determines, in advance, how to construct each of its terms; such a sequence may be said to be *lawlike* or *predeterminate*. Brouwer generalised this notion of a sequence to include the possibility of constructing the terms one-by-one, the choice of each term being made freely, or subject only to certain restrictions stipulated in advance. Most manipulations of sequences do not require that they be predeterminate, and can be performed on these more general *free choice sequences*.

Thus, for the intuitionist, a real number $\bx = (x_1 ,x_2,\ldots)$—essentially, a Cauchy sequence of rational numbers—need not be given by a rule: its terms $x_1 ,x_2,\ldots$, are simply rational numbers, successively constructed, subject only to some kind of Cauchy restriction such as the following one used by Bishop [1967]:

$$ \forall m\forall n \left[ \abs{x_m - x_n} \le \left(\frac{1}{m} + \frac{1}{n}\right)\right] $$

Once free choice sequences are admitted into mathematics, so, perhaps to one’s initial surprise, are certain strong choice principles. Let $P$ be a subset of $\bN^{\bN} \times \bN$ (where $\bN$ denotes the set of natural numbers and, for sets $A$ and $B, B^A$ denotes the set of mappings from $A$ into $B)$, and suppose that for each $\ba \in \bN^{\bN}$ there exists $n \in \bN$ such that $(\ba,n) \in P$. From a constructive point of view, this means that we have a procedure, applicable to sequences, that computes $n$ for any given $\ba$. According to Brouwer, the construction of an element of $\bN^{\bN}$ is forever incomplete: a generic sequence $\ba$ is *purely extensional*, in the sense that at any given moment we can know nothing about $\ba$ other than a finite set of its terms. It follows that our procedure must be able to calculate, from some finite initial sequence $(a_0 ,\ldots ,a_N)$ of terms of $\ba$, a natural number $n$ such that $P(\ba,n)$. If $\bb \in \bN^{\bN}$ is any sequence such that $b_{k} = a_{k}$ for $0 \le k \le N$, then our procedure must return the same $n$ for $\bb$ as it does for $\ba$. This means that $n$ is a continuous function of $\ba$ with respect to the topology on $\bN^{\bN}$ given by the metric

$$ \varrho : (\ba,\bb) \rightsquigarrow \inf\{2^{-n} : a_k = b_k \text{ for } 0 \le k \le n\}. $$

We are therefore led to the following *principle of continuous choice*, which we divide into a continuity part and a choice part.

**CC1** : Any function from $\bN^{\bN}$ to $\bN$ is continuous.

**CC2** : If $P \subseteq \bN^{\bN} \times \bN$, and for each $\ba \in \bN^{\bN}$ there exists $n \in \bN$ such that $(\ba,n) \in P$, then there is a function $f : \bN^{\bN} \rightarrow \bN$ such that $(\ba,f(\ba)) \in P$ for all $\ba \in \bN^{\bN}$.

If $P$ and $f$ are as in CC2, then we say that $f$ is a *choice function* for $P$.

The omniscience principles LPO and LLPO are demonstrably false under the hypotheses CC1–2; but MP is consistent with it. Among the remarkable consequences of CC1–2 are the following.

- Any function from $\bN^{\bN}$ or $2^{\bN}$ to a metric space is pointwise continuous.
- Every mapping from a nonempty complete separable metric space to a metric space is pointwise continuous.
- Every map from the real line $\bR$ to itself is pointwise continuous.
- Let $X$ be a complete separable normed space, $Y$ a normed space, and $(u_n)$ a sequence of linear mappings from $X$ to $Y$ such that for each unit vector $x$ of $X$, $$ \phi(x) = \sup\{ \Vert u_n(x)\rVert : n \in \bN \} $$ exists. Then there exists $c \gt 0$ such that $\lVert u_n (x)\rVert \le c$ for all $n\in \bN$ and all unit vectors $x$ of $X$ (*Uniform boundedness principle*).

Each of these statements appears to contradict known classical theorems. However, the comparison with classical mathematics should not be made superficially: in order to understand that there is no real contradiction here, we must appreciate that the meaning of such terms as “function” and even “real number” in intuitionistic mathematics is quite different from that in the classical setting. (In practice, intuitionistic mathematics cannot be compared, readily and directly, with classical mathematics.)

Brouwer’s introspection over the nature of functions and the continuum led him to a second principle, which, unlike that of continuous choice, is classically valid. This principle requires a little more background for its explanation.

For any set $S$ we denote by $S^*$ the set of all finite sequences of elements of $S$, including the empty sequence $(\ )$. If $\alpha = (a_1 ,\ldots ,a_n)$ is in $S^*$, then $n$ is called the *length* of $\alpha$ and is denoted by $\abs{\alpha}$. If $m \in \bN$, and $\alpha$ is a finite or infinite sequence in $S$ of length at least $m$, then we denote by $\bar{\alpha}(m)$ the finite sequence consisting of the first $m$ terms of $\alpha$. Note that $\bar{\alpha}(0) = (\ )$ and $\abs{\bar{\alpha}(0)}$ = 0 . If $\alpha \in S^*$ and $\beta = \bar{\alpha}(m)$ for some $m$, we say that $\alpha$ is an *extension* of $\beta$, and that $\beta$ is a *restriction* of $\alpha$.

A subset $\sigma$ of $S$ is said to be *detachable* (from $S)$ if

$$ \forall x\in S (x \in \sigma \vee x \not\in \sigma). $$

A detachable subset $\sigma$ of $\bN^*$ is called a *fan* if

- it is closed under restriction: for each $\alpha \in \bN^*$ and each $n$, if $\bar{\alpha}(n) \in S$, then $\bar{\alpha}(k) \in S$ whenever $0 \le k \le n$; and
- for each $\alpha \in \sigma$, the set $$ \{ \alpha^* n \in S: n \in \bN \} $$ is finite or empty, where $\alpha^* n$ denotes the finite sequence obtained by adjoining the natural number $n$ to the terms of $\alpha$.

A *path* in a fan $\sigma$ is a sequence $\alpha$, finite or infinite, such that $\bar{\alpha}(n) \in \sigma$ for each applicable $n$. We say that a path $\alpha$ is *blocked* by a subset $B$ if some restriction of $\alpha$ is in $B$; if no restriction of $\alpha$ is in $B$, we say that $\alpha$ *misses* $B$. A subset $B$ of a fan $\sigma$ is called a *bar* for $\sigma$ if each infinite path of $\sigma$ is blocked by $B$; a bar $B$ for $\sigma$ is *uniform* if there exists $n \in \bN$ such that each path of length $n$ is blocked by $B$.

At last we can state Brouwer’s next principle of intuitionism, *the fan theorem for detachable bars* (FT$_D$):

Every detachable bar of a fan is uniform.

In its classical contrapositive form, FT$_D$ is known as *König’s Lemma*: if for every $n$ there exists a path of length $n$ that misses $B$, then there exists an infinite path that misses $B$ (see Dummett 1977 [2000], 49–53)[^dummett-1977]. (Of course, classically the condition of detachability is superfluous.) It is simple to construct a Brouwerian counterexample to König’s Lemma.

Brouwer actually posited the fan theorem without the restriction of detachability of the bar. Attempts to prove that more general fan theorem constructively rely on an analysis of how we could know that a subset is a bar, and led Brouwer to a notion of *bar induction*; this is discussed in Section 3.6 of the entry on intuitionism in the philosophy of mathematics; another good reference for bar induction is van Atten (2004). We shall return to fan theorems in Section 4.

Of the many applications of Brouwer’s principles, the most famous is his *uniform continuity theorem* (which follows from the pointwise continuity consequences of CC1-2 together a form of fan theorem more general than FT$_D)$:

> Every mapping from a compact (that is, complete, totally bounded) metric space into a metric space is uniformly continuous.

The reader is warned once again to interpret this carefully within Brouwer’s intuitionistic framework, and not to jump to the erroneous conclusion that intuitionism contradicts classical mathematics. It is more sensible to regard the two types of mathematics as incomparable. For further discussion, see the entry on intuitionistic logic.

Unfortunately — and perhaps inevitably, in the face of opposition from mathematicians of such stature as Hilbert — Brouwer’s intuitionist school of mathematics and philosophy became more and more involved in what, at least to classical mathematicians, appeared to be quasi-mystical speculation about the nature of constructive thought, to the detriment of the practice of constructive mathematics itself. This unfortunate polarisation between the Brouwerians and the Hilbertians culminated in the notorious Grundlagenstreit of the 1920s, details of which can be found in the Brouwer biographies by van Dalen [1999, 2005] and van Stigt [1990].

### 3.2 Recursive Constructive Mathematics

In the late 1940s, the Russian mathematician A.A. Markov began the development of an alternative form of constructive mathematics, **RUSS**, which is, essentially, recursive function theory with intuitionistic logic (Markov [1954], Kushner [1985]). In this variety the objects are defined by means of Gödel-numberings, and the procedures are all recursive; the main distinction between RUSS and the classical recursive analysis developed after the work of Turing, Church, and others in 1936 clarified the nature of computable processes is that the logic used in RUSS is intuitionistic.

One obstacle faced by the mathematician attempting to come to grips with RUSS is that, being expressed in the language of recursion theory, it is not easily readable; indeed, on opening a page of Kushner’s excellent lectures [1985], one might be forgiven for wondering whether this is analysis or logic. (This remark should be tempered with reference to the two relatively readable books on classical recursive analysis by Aberth [1980, 2001].) Fortunately, one can get to the heart of RUSS by an axiomatic approach due to Richman [1983] (see also Chapter 3 of Bridges & Richman [1987]).

First, we define a set $S$ to be *countable* if there is a mapping from a detachable subset of $\bN$ onto $S$. With intuitionistic logic we cannot prove that every subset of $\bN$ is detachable (the reader is invited to provide a Brouwerian example to demonstrate this). Countable subsets of $\bN$ in Richman’s axiomatic approach are the counterparts of recursively enumerable sets in the normal development of RUSS.

By a *partial function* on $\bN$ we mean a mapping whose domain is a subset of $\bN$; if the domain is $\bN$ itself, then we call the function a *total function* on $\bN$. Richman’s approach to RUSS is based on intuitionistic logic and a single axiom of *computable partial functions* (**CPF**):

There is an enumeration $\phi_0 ,\phi_1,\ldots$ of the set of all partial functions from $\bN$ to $\bN$ with countable domains.

It is remarkable what can be deduced cleanly and quickly using this principle. For example, we can prove the following result, which almost immediately shows that **LLPO**, and hence **LPO**, are false in the recursive setting.

> There is a total function $f : \bN \times \bN \rightarrow \{0,1\}$ such that
>
> - for each $m$ there exists at most one $n$ such that $f(m,n) = 1$; and
> - for each total function $f : \bN \rightarrow \{0,1\}$, there exist $m,k$ in $\bN$ such that $f(m,2k+f(m)) = 1$.

Of more interest, however, are results such as the following within RUSS.

- *Specker’s Theorem* (Specker [1949]): There exists a strictly increasing sequence $(r_1 ,r_2,\ldots)$ of rational numbers in the closed interval $[0,1]$ such that for each $x \in \bR$ there exist $N \in \bN$ and $\delta \gt 0$ such that $\abs{x - r_n} \ge \delta$ for all $n \ge N$.
- For each $\varepsilon \gt 0$, there exists a sequence $(I_1 ,I_2,\ldots)$, of bounded open intervals in $\bR$ such that $\bR \subseteq \bigcup_{n=1}^{\infty} I_n$ and $\sum_{n=1}^N \abs{I_n} \lt \varepsilon$ for each N. (Such a sequence of intervals is called an $\varepsilon$-*singular cover* of $\bR$.)
- There exists a pointwise continuous function $f : [0,1] \rightarrow \bR$ that is not uniformly continuous.
- There exists a positive-valued uniformly continuous function $f : [0,1] \rightarrow \bR$ whose infimum is 0.

From a classical viewpoint, these results fit into place when one realises that words such as “function” and “real number” should be interpreted as “recursive function” and “recursive real number” respectively. Note that the second of the above four recursive theorems is a strong recursive counterexample to the open-cover compactness property of the (recursive) real line; and the fourth is a recursive counterexample to the classical theorem that every uniformly continuous mapping of a compact set into $\bR$ attains its infimum.

### 3.3 Bishop’s Constructive Mathematics

Progress in all varieties of constructive mathematics was relatively slow throughout the next decade and a half. What was needed to raise the profile of constructivism in mathematics was a top-ranking classical mathematician to show that a thoroughgoing constructive development of deep analysis was possible without a commitment to Brouwer’s non-classical principles or to the machinery of recursive function theory. This need was fulfilled in 1967, with the appearance of Errett Bishop’s monograph *Foundations of Constructive Analysis* [1967] (see also Bishop & Bridges [1985]), the product of an astonishing couple of years in which, working in the informal but rigorous style used by normal analysts, Bishop provided a constructive development of a large part of twentieth-century analysis, including the Stone-Weierstrass Theorem, the Hahn-Banach and separation theorems, the spectral theorem for self-adjoint operators on a Hilbert space, the Lebesgue convergence theorems for abstract integrals, Haar measure and the abstract Fourier transform, ergodic theorems, and the elements of Banach algebra theory. Thus, at a stroke, he gave the lie to the commonly-held view expressed so forcefully by Hilbert:

> Taking the principle of excluded middle from the mathematician would be the same, say, as proscribing the telescope to the astronomer or to the boxer the use of his fists. (Hilbert [1928])

Not only did Bishop’s mathematics, **BISH**, have the advantage of readability — if you open Bishop’s book at any page, what you see is clearly recognisable as analysis, even if, from time to time, his moves in the course of a proof may appear strange to one schooled in the use of the law of excluded middle — but, unlike intuitionistic or recursive mathematics, it admits many different interpretations. Intuitionistic mathematics, recursive constructive mathematics, and even classical mathematics all provide models of BISH. In fact, the results and proofs in BISH can be interpreted, with at most minor amendments, in any reasonable model of computable mathematics, such as, for example, Weihrauch’s Type Two Effectivity Theory (Weihrauch [2000]; Bauer [2005]).

How is this multiple interpretability achieved? At least in part by Bishop’s refusal to pin down his primitive notion of “algorithm” or, in his words, “finite routine”. This refusal has led to the criticism that his approach lacks the precision that a logician would normally expect of a foundational system. However, this criticism can be overcome by looking more closely at what practitioners of BISH actually do when they prove theorems: in practice, they are doing *mathematics with intuitionistic logic*. Experience shows that the restriction to intuitionistic logic always forces mathematicians to work in a manner that, at least informally, can be described as algorithmic; so *algorithmic mathematics appears to be equivalent to mathematics that uses only intuitionistic logic*. If that is the case, then we can practice constructive mathematics using intuitionistic logic on any reasonably defined mathematical objects, not just some class of “constructive objects”.

This view, more or less, appears to have first been put forward by Richman [1990, 1996]. Taking the logic as the primary characteristic of constructive mathematics, it does not reflect the primacy of mathematics over logic that was part of the belief of Brouwer, Heyting, Markov, Bishop, and other pioneers of constructivism. On the other hand, it does capture the essence of constructive mathematics in practice.

Thus one might distinguish between the *ontological constructivism* of Brouwer and others who are led to constructive mathematics through a belief that mathematical objects are mental creations, and the *epistemological constructivism* of Richman and those who see constructive mathematics as characterised by its methodology, based on the use of intuitionistic logic. Of course, the former approach to constructivism inevitably leads to the latter; and the latter is certainly not inconsistent with a Brouwerian ontology.

To do actual mathematics we need more than just intutionistic logic. For Bishop, the building blocks of mathematics were the positive integers (see the quote from Bishop [1967] in Section 3.1 above). Among the early formal systems for BISH were Myhill’s [1975] axiomatic foundation based on primitive notions of number, set, and function; Feferman’s [1975] system for *explicit mathematics*; and Friedman’s [1977] intuitionistic ZF set theory. The two most favoured formal underpinnings of BISH at this stage are constructive Zermelo-Fraenkel set theory (CZF), in Aczel and Rathjen [2010, in Other Internet Resources], and intuitionistic type theory, in Martin-Löf [1975, 1984].

### 3.4 Martin-Löf’s Constructive Type Theory

Before ending our tour of varieties of modern constructive mathematics, we visit a fourth variety, **ML**, based on Per Martin-Löf’s intuitionistic type theory. Martin-Löf published his *Notes on Constructive Mathematics* [1968], based on lectures he had given in Europe in 1966–68; so his involvement with constructivism in mathematics goes back at least to the period of Bishop’s writing of *Foundations of Constructive Analysis*. Martin-Löf’s book is in the spirit of RUSS, rather than BISH; indeed, its author did not have access to Bishop’s book until his own manuscript was finished. Martin-Löf later turned his attention to his theory of types as a foundation for Bishop-style constructive mathematics.

Here, in his own words, is an informal explanation of the ideas underlying ML:

> We shall think of *mathematical objects* or *constructions*. Every mathematical object is of a certain kind or *type* [… and] is always given together with its type. … A type is defined by describing what we have to do in order to construct an object of that type. … Put differently, a type is well-defined if we understand … what it means to be an object of that type. Thus, for instance $\bN \rightarrow \bN$ [functions from $\bN$ to $\bN$] is a type, not because we know particular number theoretic functions like the primitive recursive ones, but because we think we understand the notion of number theoretic function *in general*. (Martin-Löf [975])

In particular, in this system every proposition can be represented as a type: namely, the type of proofs of the proposition. Conversely, each type determines a proposition: namely, the proposition that the type in question is inhabited. So when we think of a certain type $T$ as a proposition, we interpret the formula

$$ x \in T $$

as “$x$ is a proof of the proposition $T$”.

Martin-Löf goes on to construct new types, such as Cartesian products and disjoint unions, from old. For example, the Cartesian product

$$ (\Pi x \in A) B(x) $$

is the type of functions that take an arbitrary object $x$ of type $A$ into an object of type $B(x)$. In the propositions-as-proofs interpretation, where $B(x)$ represents a proposition, the above Cartesian product corresponds to the universal proposition

$$ (\forall x \in A) B(x). $$

Martin-Löf distinguishes carefully between proofs and derivations: a *proof object* is a witness to the fact that some proposition has been proved; whereas a *derivation* is the record of the construction of a proof object. Also, he exercises two basic forms (one dare not say “types” here) of *judgement*. The first is a relation between proof objects and propositions, the second a property of some propositions. In the first case, the judgement is either one that a proof object $a$ is a witness to a proposition $A$, or else one that two proof objects $a$ and $b$ are equal and both witness that $A$ has been proved. The first case of the second form of judgement states that a proposition $A$ is well-formed, and the second records that two propositions $A$ and $B$ are equal.

There is a careful, and highly detailed, set of rules for formalising ML. We will not go into those here, but refer the reader to other sources such as Sambin & Smith [1998].

When actually doing constructive mathematics in type theory, one often needs to equip completely presented sets (types) with an equivalence relation, the combination being known as a *setoid*. Mappings are then functions that respect those equivalence relations. This is in close agreement with the way Bishop presented his informal theory of sets. The dependent types of Martin-Löf are useful for constructing subsets. For instance, the real numbers can be constructed using the $\Sigma$-type (see Martin-Löf [1984]):

$$ (\Sigma x \in \bN_+\rightarrow \bQ)(\Pi m \in \bN_+)(\Pi n \in \bN_+)\left[\abs{x_{m} - x_{n}} \le \left(\frac{1}{m} + \frac{1}{n}\right)\right], $$

An element of this type $B$ is thereby a pair consisting of a convergent sequence $\bx$ of rationals and a proof $p$ that it is convergent. A suitable equivalence relation ${\sim}$ on $R$ is defined by taking $(x,p)\sim(y,q)$ to mean

$$ \forall m \in \bN_+ \left(\abs{x_{m} - y_{m}} \le \frac{2}{m}\right). $$

The resulting *setoid of real numbers* is $\bR = (R,{\sim})$. We can readily prove that

$$ \forall x \in \bR\, \exists n \in Z (n \lt x \lt n+2) $$

and then, using the type-theoretic axiom of choice (see Section 4 below), find a function $f : \bR\rightarrow \bZ$ such that $f(x) \lt x \lt f(x)+2$. However, there is no reason to believe that the function $f$ respects the equivalence relations—that is, that $f(x) = f(y)$ holds if $x \sim y$.

Every constructive proof embodies an algorithm that, in principle, can be extracted and recast as a computer program; moreover, the constructive proof is itself a verification that the algorithm is correct — that is, meets its specification. One major advantage of Martin-Löf’s formal approach to constructive mathematics is that it greatly facilitates the extraction of programs from proofs. This has led to serious work on the implementation of constructive mathematics in various locations (see Martin-Löf [1980], Constable [1986], Hayashi & Nakano [1988], Schwichtenberg [2009]). Some recent implementations of type theory for proof extraction are Coq and Agda (see the links in Other Internet Resources).

## 4. Axioms of Choice and the Continuum Hypothesis

The full axiom of choice can be stated as follows:

If $A,B$ are inhabited sets, and $S$ a subset of $A \times B$ such that

$$ \forall x\in A\,\exists y\in B((x,y) \in S), $$

then there exists a *choice function* $f : A \rightarrow B$ such that

$$ \forall x\in A ((x,f(x)) \in S). $$

Now, if this is to hold under a constructive interpretation, then for a given $x \in A$, the value $f(x)$ of the choice function will depend not only on $x$ *but also on the data proving that $x$ belongs to $A.$* In general, we cannot expect to produce a choice function of this sort. However, the BHK interpretation of the hypotheses in the axiom is that there is an algorithm $\mathcal{A}$ which, applied to any given $x \in A$, produces an element $y \in B$ such that $(x,y) \in S$. If $A$ is a *completely presented set*, one for which no work beyond the construction of each element in the set is required to prove that the element does indeed belong to $A$, then we might reasonably expect the algorithm $\mathcal{A}$ to be a choice function. In Martin-Löf’s type theory, *every set is completely presented* and, in keeping with the BHK interpretation, the axiom of choice is derivable.

On the other hand, in Bishop-style mathematics, completely presented–––or, in his terminology, *basic*–––sets are rare, one example being $\bN$; so we might expect that the axiom of choice would not be derivable. In fact, as was shown by Diaconescu [1975] and Goodman & Myhill [1978], and prefigured by Bishop himself in Problem 2 on page 58 of Bishop 1967, the axiom of choice implies the law of excluded middle. Clearly, the Diaconescu-Goodman-Myhill theorem applies only under the assumption that not every set is completely presented.

Constructive mathematicians not working in ML typically reject the full axiom of choice but embrace the axiom of countable choice, in which the domain of choice is $\bN$, and dependent choice. But some prefer to work without even countable choice, on the grounds that to speak of an infinity of choices without giving a rule presents a difficulty that is just as great whether or not the infinity is denumerable. Interestingly, Lebesgue made precisely this point in a letter to Borel (see Moore [2013], page 316):

> I agree completely with Hadamard when he states that to speak of an infinity of choices without giving a rule presents a difficulty that is just as great whether or not the infinity is denumerable.

The effect of abandoning even countable choice is the exclusion of many theorems that, as they stand, are proved using sequential, choice-based arguments. But those who advocate avoiding choice would argue that avoiding choice forces you to formulate things better.

A particular case of interest is the Fundamental Theorem of Algebra: every complex polynomial has at least one root in the complex plane. Richman [2000] has shown that without countable choice, although we can construct only isolated (possibly multiple) roots, we can construct arbitrarily close approximations to the multiset of roots. Such an approach focusses on finding an approximate linear factorization of the polynomial, rather than on finding separate approximations to each of its roots.

For further analysis of the axiom of choice in set theory and type theory see Martin-Löf [2006], and the SEP entries on category theory, type theory, and intuitionistic type theory.

We now recall the *power set axiom* of classical set theory: if $X$ is a set, then so is its *power set* $$ \textrm{sb}(X)≡ \{S: S \subset X\}. $$ Since this definition is impredicative, most constructive mathematicians hesitate to regard $\textrm{sb}(X)$ as a set. What they normally use, and we shall adopt, as the constructive replacement for the power set axiom is the *axiom of exponentiation* : If $A$ and $B$ are sets, then so is the set of all mappings from $A$ into $B$. In particular, the class $2^{\bN}$ of all binary sequences is a set.

In order to discuss the Continuum Hypothesis, we need notions of comparative size for classes $A$ and $B$. We say that

- $A$ is *equinumerous with* $B$ if there exists a bijective mapping of $A$ onto $B$, and that
- $A$ is *cardinally included in* $B$ if $A$ is equinumerous with a subclass of $B$.

In the first case we write $A$ ≅ $B$, and in the second, $A ≲ B$.

A consequence of the axiom of replacement in constructive Zermelo–Fraenkel set theory, CZF, is that if $A$ is a set and $B$ is a class that is equinumerous with $A$, then $B$ is also a set. It follows that the class $$ \textrm{dch}(\bN)≡ \{S \subset\bN : \forall x \in \bN (x \in S \vee x \not\in S)\} $$ of detachable subsets of $\bN$, being equivalent to $2^{\bN}$, is a set.

Classically, every subset of $\bN$ is detachable from $\bN$, so $\textrm{dch}(\bN)$ = $\textrm{sb}(\bN)$. But this is not the case constructively: if for each statement $p$ the set $$ \{x \in 1 : p \vee \neg p \} $$ were in $\textrm{dch}(\bN)$, then we could derive the law of excluded middle.

The *classical Continuum Hypothesis* states that there is no set whose cardinality lies strictly between that of the set $\bN$ and that of $\textrm{sb}(\bN)$. We can state this more formally as follows: $$ \forall C(\bN ≲ C≲ \textrm{sb}(\bN) \Rightarrow C \cong \bN \vee C \cong \textrm{sb}(\bN)) $$ or, equivalently, $$ \forall C(\bN ≲ C≲ \textrm{sb}(\bN) \wedge \neg(C ≲ \bN) \Rightarrow C \cong \textrm{sb}(\bN)) $$ Constructively acceptable classical equivalents of these two statements are: $$ \forall C(\bN ≲ C ≲ \textrm{dch}(\bN) \Rightarrow C \cong \bN \vee C \cong \textrm{dch}(\bN)) $$ and the one that we take as our *constructive Continuum Hypothesis*, $\textrm{CH}$, $$ \forall C(\bN ≲ C≲ \textrm{dch}(\bN) \wedge \neg(C \cong \bN) \Rightarrow C \cong \textrm{dch}(\bN)) $$

We sketch a proof that $\textrm{CH}$ implies the law of excluded middle. First we note that $2^{\bN}$ is uncountable in the strong sense: Cantor’s diagonal argument shows that if $S$ is a countable subset of $2^{\bN}$, then there exists $f \in 2^{\bN}$ such that $f \notin S$. Assuming $\textrm{CH}$, we now define $$ X≡ \{S \in \textrm{dch}(\bN) : p \vee \neg p \}$$ and $$ \textrm{C}≡\bN \cup X. $$ Then $\bN ≲C≲\textrm{dch}(\bN)$. If $C \cong \bN $, then $p \vee \neg p $ is false, which is absurd. Hence $\neg (C \cong \bN)$ and therefore $C \cong \textrm{dch}(\bN)$. But $\textrm{dch}(\bN)$, being equinumerous with $2^{\bN}$ , is uncountable, so there exists $S \in \textrm{dch}(\bN)$ that does not belong to the countable subset $\bN$ of $\textrm{dch}(\bN)$. Thus $S \in C $, and therefore $p \vee \neg p $ holds.

Incidentally, although, in light of the BHK interpretation of '$\vee$', the first of our two constructive statements classically equivalent to the classical Continuum Hypothesis might appear to be stronger than $\textrm{CH}$, since the latter implies the law of excluded middle it is constructively equivalent to the former.

The foregoing work on $\textrm{CH}$ can be formalised in CZF, which is equiconsistent with classical Zermelo–Fraenkel set theory, ZF. If we allow ourselves to invoke the Gödel–Cohen theorem that the Continuum Hypothesis is independent of ZF, then we can draw some interesting conclusions by looking more closely at our proof that $\textrm{CH}$ implies LEM. To do so, take $p=\textrm{CH}$ in our proof, so that $$ X≡ \{S \in \textrm{dch}(\bN) : \textrm {CH} \vee \neg \textrm{CH} \}. $$ If $X=0$, then $\neg (\textrm{CH} \vee \neg \textrm{CH})$, which is absurd; so $\neg(X=0)$. On the other hand, if $X$ is inhabited — that is, contains a point — then $\textrm{CH} \vee \neg \textrm{CH}$, so under the constructive interpretation of '$\vee$', either we have a proof of $\textrm{CH}$ or else we have a proof of $\neg \textrm{CH}$. Since this runs counter to the aforementioned Gödel–Cohen theorem, we may regard $X$ as an explicit example of a set that is not empty but for which it is impossible to construct a member. This, in itself, is not uninteresting; but it also gives a new insight into the constructive status of $\textrm{CH}$. From our proof that $\textrm{CH}$ implies LEM we see that the set $C≡\bN \cup X$ satisfies $$ \bN≲C≲\textrm{dch}(\bN) \wedge \neg(C \cong \bN). $$ Also, $$ \neg(C \cong \textrm{dch}(\bN)) \Rightarrow X=0, $$ which is absurd, so $\neg\neg(C \cong \textrm{dch}(\bN))$. On the other hand, $$ C \cong \textrm{dch}(\bN) \Rightarrow \textrm{CH} \vee \neg \textrm{CH}. $$ Thus, provided $\textrm{CH}$ is independent of CZF (which, in view of equiconsistency of CZF and ZF, it had better be), we see that $C$ is an explicit example of a set that has the property $$ \bN≲C≲\textrm{dch}(\bN) \wedge \neg(C\cong \bN) \wedge \neg \neg (C \cong \textrm{dch}(\bN)) $$ but, within CZF, cannot be proved equinumerous with $\textrm{dch}(\bN)$.

## 5. Constructive Reverse Mathematics

In the 1970s, Harvey Friedman initiated a research programme of *reverse mathematics,* aiming to classify mathematical theorems according to their equivalence to one of a small number of set-theoretic principles (Friedman 1975)[^friedman-1975]. This classification reveals interesting, sometimes remarkable, differences in proof-theoretic complexity. For example, although the Ascoli–Arzelà theorem is used in the standard proof of Peano’s existence theorem for solutions of ordinary differential equations (Hurewicz [1958], page 10), a reverse-mathematical analysis shows that the former is equivalent to a strictly stronger set-theoretic principle than the one equivalent to Peano’s theorem (Simpson [1984], Theorems 3.9 and 4.2). The standard treatise on classical reverse mathematics is (Simpson [1999/2009]).

Around the turn of this century, Veldman (see Other Internet Resources), in the Netherlands, and Ishihara [2005, 2006], in Japan, independently initiated a programme of *constructive reverse mathematics* (CRM), based on intuitionistic, rather than classical, logic. (Note, though, that the first published work in the modern era of CRM is probably that of Julian and Richman [1984], which was twenty years ahead of its time.) In this section of the article, we describe a less formal approach to CRM, in the style and framework of BISH. The aim of that CRM program is to classify the theorems in the three standard models—CLASS, INT, and RUSS—according to which principles we must, and need only, add to BISH in order to prove them.

We stress that we restrict ourselves here to *informal* CRM, in which we take for granted the principles of function- and set-construction described in the first chapters of Bishop [1967] or Bishop & Bridges [1985], and we work in the informal, though rigorous, style of the practising analyst, algebraist, topologist, … .

In practice, CRM splits naturally into two parts. In the first of these, we consider a theorem $T$ of INT or RUSS, and try to find some principle, valid in that model and other than $T$ itself, whose addition to BISH is necessary and sufficient for a constructive proof of $T$. In the second part of CRM we deal with a theorem $T$ of CLASS that we suspect is nonconstructive, and we try to prove that $T$ is equivalent, over BISH, to one of a number of known essentially-nonconstructive principles, such as MP, LLPO, LPO, or LEM. For an example of this part of CRM, we mention our earlier proof that the classical least-upper-bound principle implies, and hence is equivalent to, LEM.

Incidentally, there is a strong argument for Brouwer [1921] being the first to deal with reverse-mathematical ideas: his Brouwerian counterexamples (see the one using the Goldbach conjecture, in Section 1 above) lie squarely in the second part of CRM. Even if Brouwer did not state those examples as logical equivalences, but as implications of the type

$$ P \Rightarrow \text{ some nonconstructive principle}, $$

it is hard to believe that he was unaware that the right-hand-side implied the left in such cases.

### 5.1 Fan theorems in CRM

To illustrate the first part of CRM, we now concentrate on theorems of the type

$$ \text{BISH } \vdash \text{ FT}_? \Leftrightarrow T, $$

where FT$_?$ is some form of Brouwer’s fan theorem, and $T$ is a theorem of INT. To do so, we need to distinguish between certain types of bar for the *complete binary fan* $2^*$ (the set of all finite sequences in $\{0,1\})$.

Let $\alpha \equiv (\alpha_1 ,\alpha_2, \ldots)$ be a finite or infinite binary sequence. The *concatenation* of $\alpha$ with another string $\beta$ is

$$ \alpha^{\frown}\beta \equiv (\alpha_1 ,\alpha_2 ,\ldots ,\alpha_n ,\beta_1 ,\ldots ,\beta_m). $$

For $b$ in $\{0,1\}$ we write $\alpha^{\frown}b$ rather than $\alpha^{\frown}(b)$. By a $\mathsf{c}$-*subset* of $2^*$ we mean a subset $B$ of $2^*$ such that

$$\tag{1} B = \{u \in 2^* : \forall v\in 2^* (u^{\frown}v \in D)\} $$

for some detachable subset $D$ of $2^*$. Every detachable subset of $2^*$ is a $\mathsf{c}$-subset. On the other hand, by a $\Pi^{0}_1$-*subset* of $2^*$ we mean a subset $B$ of $2^*$ with the following property: there exists a detachable subset $S$ of $2^* \times \bN$ such that

$$ \forall u\in 2^*\,\forall n\in \bN\, ((u,n) \in S \Rightarrow (u^{\frown}0,n) \in S \wedge (u^{\frown}1,n) \in S) $$

and

$$ B = \{u \in 2^* :\forall n\in \bN((u,n) \in S)\}. $$

Every $\mathsf{c}$-subset $B$ of $2^*$ is a $\Pi^{0}_1$-subset: simply take $S = D \times \bN$, where $D$ is a detachable subset of $2^*$ such that (1) holds.

If $?$ denotes a property of subsets of $2^*$, then Brouwer’s *fan theorem for* $?$-*bars* tells us that every bar with the property $?$ is a uniform bar. We are particularly interested in the fan theorem for detachable bars (already discussed in Section 3.1):

FT$_D$: Every detachable bar of the complete binary fan is uniform;

the fan theorem for $\mathsf{c}$-*bars* (that is, bars that are $\mathsf{c}$-subsets):

FT$_{\mathsf{c}}$: Every c-bar of the complete binary fan is uniform;

the fan theorem for $\Pi^{0}_1$-*bars* (that is, bars that are $\Pi^{0}_1$-subsets):

FT$_{\Pi^{0}_1}$: Every $\Pi^{0}_1$-bar of the complete binary fan is uniform;

and the full fan theorem:

FT: Every bar of the complete binary fan is uniform.

Note that, relative to BISH,

FT $\Rightarrow$ FT$_{\Pi^{0}_1} \Rightarrow$ FT$_c \Rightarrow$ FT$_D$.

Lubarsky and Diener [2014] have shown that these implications are strict.

Typically, we want to prove that FT$_?$ is equivalent, over BISH, to the proposition that, for every set $S$ of an appropriate sort, some pointwise property of the form

$$\tag{2} \forall x \in S \exists t \in T P(s,t) $$

actually holds uniformly in the form

$$\tag{3} \exists t \in T \forall s \in S P(s,t). $$

Our strategy for attacking this problem is two-fold. First, given a set $S$ of the appropriate sort, we construct a ?-subset $N$ of $2^*$ such that

- if (2) holds, then $B$ is a bar, and
- if $B$ is a uniform bar, then (3) holds.

This, though, is only half of the solution. To prove that the implication from (3) to (2) implies FT$_?$, we consider a ?-subset $B$ of $2^*$ and construct a corresponding set $S$ such that

- if $B$ is a bar, then (2) holds, and
- if (3) holds, then $B$ is a uniform bar.

The canonical example of such results is that of Julian and Richman [1984], in which $S$ is the set of values of a given uniformly continuous mapping $f : [0,1] \rightarrow \bR, T$ is the set of positive real numbers, and

$$ P(s,t) \equiv (s \ge t). $$

The pointwise property we consider is

$$ \forall x \in [0,1] \exists t \gt 0 (f(x) \ge t), $$

its uniform version being

$$ \exists t \gt 0 \forall x \in [0,1] (f(x) \ge t). $$

The Julian-Richman results are as follows.

**Theorem 1**: Let $f : [0,1] \rightarrow \bR$ be uniformly continuous. Then there exists a detachable subset $B$ of $2^*$ such that

- if $f(x) \gt 0$ for each $x \in [0,1]$, then $B$ is a bar, and
- if $B$ is a uniform bar, then $\inf f \gt 0$.

**Theorem 2**: Let $B$ be a detachable subset of $2^*$. Then there exists a uniformly continuous $f : [0,1] \rightarrow \bR$ such that

- if $B$ is a bar, then $f(x) \gt 0$ for each $x \in [0,1]$, and
- if inf $f \gt 0$, then $B$ is a uniform bar.

The proofs of these two theorems are subtle and tricky; see Julian & Richman [1984].

The two Julian-Richman theorems together reveal that, relative to BISH, the fan theorem FT$_D$ is equivalent to the *positivity principle*, **POS**:

Each positive-valued, uniformly continuous function on $[0,1]$ has a positive infimum.

It follows that POS is derivable in INT, in which the full fan theorem, not just FT$_D$, is a standard principle. The situation is quiet the opposite in RUSS, where there exist both a detachable bar of $2^*$ that is not uniform and a positive-valued, uniformly continuous function on $[0,1]$ that has infimum equal to 0; see Chapters 5 and 6 of Bridges & Richman [1987].

Berger and Ishihara [2005] have taken a different, indirect route to establishing the equivalence of POS and FT$_c$. They establish a chain of equivalences between POS, FT$_c$, and four principles of the type “if there is at most one object with property $P$, then there is one such object”. The four unique-existence principles are:

**CIN!**: Each descending sequence of inhabited closed located subsets of a compact metric space with at most one common point has inhabited intersection (Cantor’s intersection theorem with uniqueness.) Note that a subset $S$ of a metric space $(X,\rho)$ is *located* if for each $x$ in $X$ the infimum distance from $x$ to $S$ exists.

**MIN!**: Each uniformly continuous, real-valued function on a compact metric space with at most one minimum point has a minimum point.

**WKL!** Each infinite tree with at most one infinite branch has an infinite branch (the weak König lemma with uniqueness).

**FIX!**: Each uniformly continuous function from a compact metric space into itself with at most one fixed point and with approximate fixed points has a fixed point.

In, for example, the last of these, we say that a map $f$ of a metric space $(X,\varrho)$ into itself

- *has at most one fixed point* if $\varrho(f(x),x) + \varrho(f(y),y) \gt 0$ whenever $\varrho(x,y) \gt 0$;
- *has approximate fixed points* if for each $\varepsilon \gt 0$ there exists $x \in X$ such that $\varrho(f(x),x) \lt \varepsilon$.

A major open problem in CRM is that of finding a form of the fan theorem that is equivalent, over BISH, to the *uniform continuity theorem for* $[0,1]$,

**UCT**$_{[0,1]}$: Every pointwise continuous mapping of $[0,1]$ into $\bR$ is uniformly continuous,

the proposition for which Brouwer originally developed his proof of the fan theorem. (Note that UCT$_{[0,1]}$ is equivalent, relative to BISH, to the general uniform continuity theorem for metric spaces: Every pointwise continuous mapping of a complete, totally bounded metric space into a metric space is uniformly continuous. See, for example, Loeb [2005].)

It follows from results of Berger [2006] that

BISH $\vdash$ UCT$_{[0,1]}\Rightarrow$ FT$_c$.

Also, Diener and Loeb (2008) have proved that

BISH $\vdash$ FT$_{\Pi^{0}_1} \Rightarrow$ UCT$_{[0,1]}$.

However, we do not know if either of these implications can be replaced by a bi-implication. Perhaps UCT$_{[0,1]}$, and hence the full uniform continuity theorem for compact metric spaces, is equivalent, relative to BISH, to some natural, but as yet unidentified, version of the fan theorem.

For additional material on the fan theorem in constructive reverse mathematics, see, for example, Berger & Bridges [2007]; Diener [2008, 2012]; Diener & Loeb [2009]; and Diener & Lubarsky [2014]. In Dent [2013], there is a clear, though complex, diagram illustrating the interconnections between fan theorems, continuity, and omniscience principles (see Other Internet Resources).

Interested readers may pursue the topic of constructive reverse mathematics in greater detail in the following supplementary document:

> [Ishihara’s principle $\BDN$ and the anti-Specker Property](mathematics-constructive.supplement1.md)

## 6. Constructive Algebra and Topology

Constructive mathematicians initially concentrated their efforts on the field of analysis, with considerable success—witness the wealth of functional analysis developed in Bishop [1967]. This does not mean that, for example, algebra has been sidelined from the constructive enterprise: the material in the monograph by Mines *et al* [1986] can be regarded as a substantial algebraic counterpart to the constructive analysis carried out by Bishop. Much more recently, Lombardi and Quitté [2011] have published the first large volume of a proposed two-volume work on constructive algebra. However, not being expert in algebra, and being aware of the danger of making this article too long to hold the reader’s attention, we choose not to discuss constructive analysis or algebra in any detail; rather, in the following supplementary document, we turn to constructive topology, describing some rather different approaches to that subject:

> [Approaches to Constructive Topology](mathematics-constructive.supplement2.md)

## 7. Constructive Mathematical Economics and Finance

Investigations in constructive mathematical economics date back to a series of papers on preference, utility, and demand from 1982 onwards; see Bridges [1999]. In his doctoral thesis, Hendtlass [2013] substantially weakened the conditions for the existence of a demand function; he also produced a wealth of results in fixed-point theory and its applications, in particular to constructivisations of two classical proofs of the existence of an economic equilibrium.

In 2015, Berger and Svindland began a research project on constructive mathematical finance, at Ludwig-Maximilians-Universität in Munich.They first showed that the fundamental theorem on asset pricing, the separating hyperplane theorem, and Markov’s Principle are constructively equivalent (Berger & Svindland [2016]). Their more recent work has concentrated on how to circumvent the nonconstructivity of the classical extreme value theorem in order to prove the existence of extreme points for functions in the presence of even relatively weak convexity properties (Berger & Svindland [2016a]). Their project suggests that mathematical finance, like mathematical economics, may be a rich source of elegant, practical constructive theorems.

## 8. Concluding Remarks

The traditional route taken by mathematicians wanting to analyse the constructive content of mathematics is the one that follows classical logic; in order to avoid decisions, such as whether or not a real number equals 0, that cannot be made by a real computer, the mathematician then has to keep within strict algorithmic boundaries such as those formed by recursive function theory. In contrast, the route taken by the constructive mathematician follows intuitionistic logic, which automatically takes care of computationally inadmissible decisions. This logic (together with an appropriate set- or type-theoretic framework) suffices to keep the mathematics within constructive boundaries. Thus the mathematician is free to work in the natural style of an analyst, algebraist (e.g., Mines *et al.* [1988]), geometer, topologist (e.g., Bridges & Vîță [2011], Sambin forthcoming), or other normal mathematician, the only constraints being those imposed by intuitionistic logic. As Bishop and others have shown, the traditional belief promulgated by Hilbert and still widely held today, that intuitionistic logic imposes such restrictions as to render the development of serious mathematics impossible, is patently false: large parts of deep modern mathematics can be, and have been, produced by purely constructive methods. Moreover, the link between constructive mathematics and programming holds great promise for the future implementation and development of abstract mathematics on the computer.

For further information about the state of modern constructive mathematics, we recommend the forthcoming *Handbook of Constructive Mathematics* [Bridges et al., eds, 2023].

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

### References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

### Related Literature

- Heijenoort, Jean van, 1967, *From Frege to Gödel: A Source Book in Mathematical Logic 1879–1931*, Cambridge, MA: Harvard University Press.
- Hilbert, David, 1928, “Die Grundlagen der Mathematik”, Hamburger Mathematische Einzelschriften 5, Teubner, Leipzig. Reprinted in English translation in van Heijenoort 1967.

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=mathematics-constructive). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/mathematics-constructive/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=mathematics-constructive&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/mathematics-constructive/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

- [The Agda Wiki](http://wiki.portal.chalmers.se/agda/pmwiki.php), a typed functional programming language and proof assistant, Göteborg University and Chalmers University of Technology.
- [Agda](https://en.wikipedia.org/wiki/Agda_(programming_language)), entry in Wikipedia.
- [The Coq Proof Assistant](https://coq.inria.fr), Inria, 1984–2017.
- [Coq](https://en.wikipedia.org/wiki/Coq), entry in Wikipedia.
- [James Dent’s Diagram](https://docs.zoho.com/file/3rxha57eec879e68f420c810738a9e966f4e9).
- Bauer, A., 2005, “[Realizability as the connection between computable and constructive mathematics](http://math.andrej.com/2005/08/23/realizability-as-the-connection-between-computable-and-constructive-mathematics/)”.
- Veldman, W., 2014, “[Brouwer’s Fan Theorem as an Axiom and as a Contrast to Kleene’s Alternative](https://arxiv.org/abs/1106.2738)”, arxiv:1106.2738https://arxiv.org/abs/1106.2738.

## Related Entries

Brouwer, Luitzen Egbertus Jan | logic, history of: intuitionistic logic | logic: intuitionistic | mathematics, philosophy of | mathematics, philosophy of: intuitionism | set theory: constructive and intuitionistic ZF | type theory: intuitionistic

### Acknowledgments

Bridges thanks Philip Catton for kindly advising him about an early version of this entry; Fred Richman, the late Ray Mines, Bill Julian, Hajime Ishihara, Helmut Schwichtenberg, and Peter Schuster, for decades of friendship, mathematical collaboration, and support during visits to their institutions; Luminita Vîţă, Hannes Diener, Matt Hendtlass, Maarten McKubre-Jordens, Josef Berger, Iris Loeb, and many other students, postdocs, and colleagues, for their participation in the constructive programme; the University of Buckingham, England, for giving him opportunity and encouragement at the start of his academic career; and the Universities of Waikato and Canterbury, for supporting him in New Zealand since 1989. Last, but not least, he thanks Hajime Ishihara for stepping into the authorial breach made by the untimely death of Erik Palmgren.

[^aberth-1980]: Aberth, O., 1980, *Computable Analysis*, New York: McGraw-Hill.

[^aberth-2001]: –––, 2001,*Computable Calculus*, New York: Academic Press.

[^bauer-2005]: Bauer, A., 2005, “Realizability as the connection between computable and constructive Mathematics”, Lecture notes for a tutorial at a satellite seminar of CCA2005, Kyoto, Japan [[available online](http://math.andrej.com/2005/08/23/realizability-as-the-connection-between-computable-and-constructive-mathematics/)].

[^beeson-1985]: Beeson, M., 1985, *Foundations of Constructive Mathematics*, Heidelberg: Springer Verlag.

[^berger-2006]: Berger, J., 2006, “The logical strength of the uniform continuity theorem”, in *Logical Approaches to Computational Barriers*, A. Beckmann, U. Berger, B. Löwe, and J. V. Tucker (eds.), Heidelberg: Springer Verlag.

[^berger-2007]: Berger, J., and Bridges, D.S., 2007, “A fan-theoretic equivalent of the antithesis of Specker’s theorem”, *Proceedings of Royal Dutch Mathematical Society (Indagationes Mathematicae)* (Indag. Math. N.S.), 18(2): 195–202.

[^berger-2009]: –––, 2009, “The fan theorem and positive-valued uniformly continuous functions on compact intervals”, *New Zealand Journal of Mathematics*, 38: 129–135.

[^berger-2005]: Berger, J., and Ishihara, H., 2005, “Brouwer’s fan theorem and unique existence in constructive analysis”, *Mathematical Logic Quarterly*, 51(4): 360–364.

[^berger-2006-2]: Berger, J., and Schuster, P.M., 2006, “Classifying Dini’s theorem”, *Notre Dame Journal of Formal Logic*, 47: 253–262.

[^berger-2016]: Berger, J., and Svindland, G., 2016, “A separating hyperplane theorem, the fundamental theorem of asset pricing, and Markov’s principle ”, *Annals of Pure and Applied Logic*, 167: 1161–1170.

[^berger-2016a]: –––, 2016a, “Convexity and constructive infima”, *Archive for Mathematical Logic*, 55: 873–881.

[^bishop-1967]: Bishop, E., 1967, *Foundations of Constructive Analysis*, New York: McGraw-Hill.

[^bishop-1973]: –––, 1973, *Schizophrenia in Contemporary Mathematics* (American Mathematical Society Colloquium Lectures), Missoula: University of Montana; reprinted in *Errett Bishop: Reflections on Him and His Research*, American Mathematical Society Memoirs 39.

[^bishop-1985]: Bishop, E. and Bridges, D., 1985, *Constructive Analysis*, (Grundlehren der mathematischen Wissenschaften, 279), Heidelberg: Springer Verlag.

[^bourbaki-1984]: Bourbaki, N., 1984, *Éléments d’histoire des mathématiques*, Paris: Masson; English-language edition, *Elements of the History of Mathematics*, J. Meldrum (trans.), 2006, Berlin: Springer Verlag.

[^bridges-1999]: Bridges, D.S., 1999, “Constructive methods in mathematical economics”, in *Zeitschrift für Nationalökonomie* (Supplement), 8: 1–21.

[^bridges-2007]: Bridges, D.S., and Diener, H., 2007, “The pseudocompactness of [0, 1] is equivalent to the uniform continuity theorem”, *Journal of Symbolic Logic*, 72(4): 1379–1383.

[^bridges-1987]: Bridges, D.S., and Richman, F., 1987, *Varieties of Constructive Mathematics*, London Mathematical Society Lecture Notes 97, Cambridge: Cambridge University Press.

[^bridges-2006]: Bridges, D.S. and Vîță, L.S., 2006, *Techniques of Constructive Analysis*, Heidelberg: Springer Verlag.

[^bridges-2011]: –––, 2011, *Apartness and Uniformity—A Constructive Development*, Heidelberg: Springer Verlag.

[^bridges-nd]: Bridges, D.S., Ishihara, H., Rathjen, M.J., and Schwichtenberg, H. (eds), forthcoming, *Handbook of Constructive Mathematics*, Cambridge: Cambridge University Press.

[^brouwer-1907]: Brouwer, L.E.J., 1907, *Over de Grondslagen der Wiskunde*, Doctoral Thesis, University of Amsterdam; reprinted with additional material, D. van Dalen (ed.), by Matematisch Centrum, Amsterdam, 1981.

[^brouwer-1908]: –––, 1908, “De onbetrouwbaarheid der logische principes”, *Tijdschrift voor Wijsbegeerte*, 2: 152–158.

[^brouwer-1921]: –––, 1921, “Besitzt jede reelle Zahl eine Dezimalbruchentwicklung?”, *Mathematische Annalen*, 83: 201–210.

[^brouwer-1924]: –––, 1924, “Beweis, dass jede volle Funktion gleichmässig stetig ist”, *Proceedings of Royal Dutch Mathematical Society*, 27: 189–193.

[^brouwer-1924a]: –––, 1924A, “Bemerkung zum Beweise der gleichmässigen Stetigkeit voller Funktionen”, *Proceedings of Royal Dutch Mathematical Society*, 27: 644–646.

[^cederquist-1996]: Cederquist, J., and Negri, S., 1996, “A constructive proof of the Heine-Borel covering theorem for formal reals”, in *Types for Proofs and Programs* (Lecture Notes in Computer Science, Volume 1158), 62–75, Berlin: Springer Verlag.

[^constable-1986]: Constable, R., *et al*., 1986, *Implementing Mathematics with the Nuprl Proof Development System*, Englewood Cliffs, NJ: Prentice-Hall.

[^coquand-1992]: Coquand, T., 1992, “An intuitionistic proof of Tychonoff’s theorem”, *Journal of Symbolic Logic*, 57: 28–32.

[^coquand-2009]: –––, 2009, “Space of valuations”, *Annals of Pure and Applied Logic*, 157: 97–109.

[^coquand-2016]: –––, 2016, “Type Theory”, *Stanford Encyclopedia of Philosophy* (Winter 2016 Edition), Edward N. Zalta (ed.), URL = <[https://plato.stanford.edu/entries/type-theory/](https://plato.stanford.edu/archives/win2016/entries/type-theory/)>.

[^coquand-2009-2]: Coquand, T., and Spitters, B., 2009, “Integrals and Valuations”, *Journal of Logic and Analysis*, 1(3): 1–22.

[^coquand-2003]: Coquand, T., Sambin, G., Smith, J., and Valentini, S., 2003, “Inductively generated formal topologies”, *Annals of Pure and Applied Logic*, 124: 71–106.

[^curi-2010]: Curi, G., 2010, “On the existence of Stone-Čech compactification”, *Journal of Symbolic Logic*, 75: 1137–1146.

[^dent-2013]: Dent, J.E., 2013, *Anti-Specker Properties in Constructive Reverse Mathematics*, Ph.D. thesis, University of Canterbury, Christchurch, New Zealand.

[^diaconescu-1975]: Diaconescu, R., 1975, “Axiom of choice and complementation”, *Proceedings of the American Mathematical Society*, 51: 176–178.

[^diener-2008]: Diener, H., 2008, *Compactness under Constructive Scrutiny*, Ph.D. thesis, Christchurch, New Zealand: University of Canterbury.

[^diener-2008a]: –––, 2008a, “Generalising compactness”, *Mathematical Logic Quarterly*, 51(1): 49–57.

[^diener-2012]: –––, 2012,“Reclassifying the antithesis of Specker’s theorem”, *Archive for Mathematical Logic*, 51: 687–693.

[^diener-2009]: Diener, H., and Loeb, I., 2009, “Sequences of Real Functions on [0, 1] in Constructive Reverse Mathematics”, *Annals of Pure and Applied Logic*, 157(1): 50–61.

[^diener-2013]: Diener, H., and Lubarsky, R., 2013, “Separating the fan theorem and its weakenings”, in *Logical Foundations of Computer Science* (Lecture Notes in Computer Science, 7734), S. Artemov and A. Nerode (eds.), Berlin: Springer Verlag.

[^dummett-1977]: Dummett, Michael, 1977 [2000], *Elements of Intuitionism* (Oxford Logic Guides, 39), Oxford: Clarendon Press, 1977; 2nd edition, 2000. [Page references are to the 2nd edition.]

[^ewald-1996]: Ewald, W., 1996, *From Kant to Hilbert: A Source Book in the Foundations of Mathematics* (Volume 2), Oxford: Clarendon Press.

[^feferman-1975]: Feferman, S, 1975, “A language and axioms for explicit mathematics”, in *Algebra and Logit*, J. N. Crossley (ed.), Heidelberg: Springer Verlag, pp. 87–139.

[^feferman-1979]: –––, 1979, “Constructive theories of functions and classes”, in *Logic Colloquium ‘78*, M. Boffa, D. van Dalen, and K. McAloon (eds.), Amsterdam: North Holland, pp. 159–224.

[^friedman-1975]: Friedman, H., 1975, “Some systems of second order arithmetic and their use”, in *Proceedings of the 17th International Congress of Mathematicians*, Vancouver, BC, 1974.

[^friedman-1977]: –––, 1977, “Set theoretic foundations for constructive analysis”, *Annals of Mathematics*, 105 (1): 1–28.

[^goodman-1978]: Goodman, N.D., and Myhill, J., 1978, “Choice Implies Excluded Middle”, *Zeitschrift für Logik und Grundlagen der Mathematik*, 24: 461.

[^hayashi-1988]: Hayashi, S., and Nakano, H., 1988, *PX: A Computational Logic*, Cambridge MA: MIT Press.

[^hendtlass-2013]: Hendtlass, M., 2013, *Constructing fixed points and economic equilibria*, Ph.D. thesis, University of Leeds.

[^heyting-1930]: Heyting, A., 1930, “Die formalen Regeln der intuitionistischen Logik”, *Sitzungsberichte der Preussische Akadademie der Wissenschaften. Berlin*, 42–56.

[^heyting-1971]: –––, 1971, *Intuitionism—an Introduction*, 3rd edition, Amsterdam: North Holland.

[^hilbert-1925]: Hilbert, D., 1925, “Über das Unendliche”, *Mathematische Annalen*, 95: 161–190; translation, “On the Infinite”, by E. Putnam and G. Massey, in *Philosophy of Mathematics: Selected Readings*, P. Benacerraf and H. Putnam (eds.), Englewood Cliffs, NJ: Prentice Hall, 1964, 134–151.

[^hurewicz-1958]: Hurewicz, W., 1958, *Lectures on Ordinary Differential Equations*, Cambridge, MA: MIT Press.

[^ishihara-1992]: Ishihara, H., 1992, “Continuity properties in constructive mathematics”, *Journal of Symbolic Logic*, 57 (2): 557–565.

[^ishihara-1994]: –––, 1994, “A constructive version of Banach’s inverse mapping theorem”, *New Zealand Journal of Mathematics*, 23: 71–75.

[^ishihara-2005]: –––, 2005, “Constructive Reverse mathematics: compactness properties”, in *From Sets and Types to Analysis and Topology: Towards Practicable Foundations for Constructive Mathematics*, L. Crosilla and P. Schuster (eds.), Oxford: The Clarendon Press.

[^ishihara-2006]: –––, 2006, “Reverse mathematics in Bishop’s constructive mathematics”, *Philosophia Scientiae* (Cahier Special), 6: 43–59.

[^ishihara-2013]: –––, 2013, “Relating Bishop’s function spaces to neighbourhood spaces”, *Annals of Pure and Applied Logic*, 164: 482–490.

[^johnstone-1982]: Johnstone, P.T., 1982, *Stone Spaces*, Cambridge: Cambridge University Press.

[^johnstone-2003]: –––, 2003, “The point of pointless topology”, *Bulletin of the American Mathematical Society*, 8: 41–53.

[^joyal-1984]: Joyal, A., and Tierney, M., 1984, “An extension of the Galois theory of Grothendieck”, *Memoirs of the American Mathematical Society*, 309: 85 pp.

[^julian-1984]: Julian, W.H., and Richman, F., 1984, “A uniformly continuous function on [0, 1] that is everywhere different from its infimum”, *Pacific Journal of Mathematics*, 111: 333–340.

[^kushner-1985]: Kushner, B., 1985, *Lectures on Constructive Mathematical Analysis*, Providence, RI: American Mathematical Society.

[^lietz-2004]: Lietz, P., 2004, *From Constructive Mathematics to Computable Analysis via the Realizability Interpretation*, Dr. rer. nat. dissertation, Universität Darmstadt, Germany.

[^lietz-1803]: Lietz, P., and Streicher, T., “Realizability models refuting Ishihara’s boundedness principle”, *Annals of Pure and Applied Logic*, 163(12): 1803–1807.

[^loeb-2005]: Loeb, I., 2005, “Equivalents of the (Weak) Fan Theorem”, *Annals of Pure and Applied Logic*, 132: 51–66.

[^lombardi-2011]: Lombardi, H., Quitté, C., 2011, *Algèbre Commutative. Méthodes constructives*, Nanterre, France: Calvage et Mounet.

[^lorenzen-1955]: Lorenzen, P., 1955, *Einführung in die operative Logik und Mathematik* (Grundlehren der mathematischen Wissenschaften, Volume 78), 2nd edition, 1969, Heidelberg: Springer.

[^lubarsky-2014]: Lubarsky, R., and Diener, H., 2014, “Separating the Fan Theorem and Its Weakenings”, *Journal of Symbolic Logic*, 79(3): 792–813.

[^markov-1954]: Markov, A.A., 1954, *Theory of Algorithms*, Trudy Mat. Istituta imeni V.A. Steklova, 42, Moskva: Izdatel’stvo Akademii Nauk SSSR.

[^marquis-2015]: Marquis, J.-P., “Category Theory”, 2015, *The Stanford Encyclopedia of Philosophy* (Winter 2015 Edition), Edward N. Zalta (ed.), URL = <[https://plato.stanford.edu/archives/win2015/entries/category-theory/](https://plato.stanford.edu/archives/win2015/entries/category-theory/)>.

[^martin-löf-1968]: Martin-Löf, P., 1968, *Notes on Constructive Analysis*, Stockholm: Almquist & Wiksell.

[^martin-löf-1975]: –––, 1975, “An intuitionistic theory of types: predicative part”, in *Logic Colloquium 1973*, H.E. Rose and J.C. Shepherdson (eds.), Amsterdam: North-Holland.

[^martin-löf-1980]: –––, 1980, “Constructive mathematics and computer programming”, in *Proc. 6th. Int. Congress for Logic, Methodology and Philosophy of Science*, L. Jonathan Cohen (ed.), Amsterdam: North-Holland.

[^martin-löf-1984]: –––, 1984, *Intuitionistic Type Theory*, Notes by Giovanni Sambin of a series of lectures given in Padova, June 1980, Naples: Bibliopolis.

[^martin-löf-2006]: –––, 2006, “100 years of Zermelo’s axiom of choice: what was the problem with it?”, *The Computer Journal*, 49(3): 345–350.

[^menger-1940]: Menger, K., 1940, “Topology without points”, *Rice Institute Pamphlet*, 27(1): 80–107 [[available online](https://scholarship.rice.edu/handle/1911/9052)].

[^mines-1988]: Mines, R., Richman, F., and Ruitenburg, W., 1988, *A Course in Constructive Algebra*, Universitext, Heidelberg: Springer Verlag.

[^moerdijk-1984]: Moerdijk, I., 1984, “Heine-Borel does not imply the fan theorem”, *Journal of Symbolic Logic*, 49(2): 514–519.

[^moore-2013]: Moore, G.H., 2013, *Zermelo’s Axiom of Choice: Its Origins, Development, and Influence*, New York: Dover.

[^myhill-1973]: Myhill, J., 1973, “Some Properties of Intuitionistic Zermelo-Fraenkel Set Theory”, in *Cambridge Summer School in Mathematical Logic*, A. Mathias and H. Rogers (eds.), Lecture Notes in Mathematics, 337, Heidelberg: Springer Verlag, 206–231.

[^myhill-1975]: –––, 1975, “Constructive Set Theory”, *Journal of Symbolic Logic*, 40(3): 347–382.

[^naimpally-2009]: Naimpally, S., 2009, *Proximity Approach to Problems in Topology and Analysis*, Munich: Oldenbourg Verlag.

[^naimpally-1970]: Naimpally, S., and Warrack, B.D., 1970, *Proximity Spaces* (Cambridge Tracts in Math. and Math. Phys., Volume 59), Cambridge: Cambridge University Press.

[^nordström-1990]: Nordström, B., Peterson, K., and Smith, J.M., 1990, “Programming in Martin-Löf’s Type Theory”, Oxford: Oxford University Press.

[^palmgren-2007]: Palmgren, E., 2007, “A constructive and functorial embedding of locally compact metric spaces into locales”, *Topology and its Applications*, 154: 1854–1880.

[^palmgren-2008]: –––, 2008, “Resolution of the uniform lower bound problem in constructive analysis”, *Mathematical Logic Quarterly*, 54: 65–69.

[^palmgren-2009]: –––, 2009, “From intuitionistic to formal topology: some remarks on the foundations of homotopy theory”, in: *Logicism, Intuitionism and Formalism—what has become of them?*, S. Lindström, E. Palmgren, K. Segerberg, and V. Stoltenberg-Hansen (eds.), 237–253, Berlin: Springer Verlag.

[^petrakis-2016]: Petrakis, I., 2016, “A constructive function-theoretic approach to topological compactness”, in *Logical Methods in Computer Science 2016*, IEEE Computer Society Publications: 605–614.

[^petrakis-2016a]: –––, 2016a, “The Urysohn Extension Theorem for Bishop Spaces”, in S. Artemov and A. Nerode (eds.), *Symposium on Logical Foundations in Computer Science 2016* (Lecture Notes in Computer Science 9537), Berlin: Springer Verlag, 299–316.

[^picado-2011]: Picado, J., and Pultr, A., 2011, *Frames and Locales: Topology without Points*, Basel: Birkhäuser Verlag.

[^richman-1983]: Richman, F., 1983, “Church’s Thesis Without Tears”, *Journal of Symbolic Logic*, 48: 797–803.

[^richman-1990]: –––, 1990, “Intuitionism as generalization”, *Philosophia Mathematica*, 5: 124–128.

[^richman-1996]: –––, 1996, “Interview with a constructive mathematician”, *Modern Logic*, 6: 247–271.

[^richman-2000]: –––, 2000, “The Fundamental Theorem of Algebra: A Constructive Treatment Without Choice”, *Pacific Journal of Mathematics*, 196: 213–230.

[^riesz-1908]: Riesz, F., 1908, “Stetigkeitsbegriff und abstrakte Mengenlehre”, *Atti IV Congresso Internationale Matematica Roma II*, 18–24.

[^sambin-1987]: Sambin, G., 1987, “Intuitionistic formal spaces—a first communication”, in *Mathematical Logic and its Applications*, D. Skordev (ed.), 187–204, New York: Plenum Press.

[^sambin-nd]: –––, forthcoming, *The Basic Picture: Structures for Constructive Topology*, Oxford: Oxford University Press.

[^sambin-1998]: Sambin, G., and Smith, J. (eds.), 1998, *Twenty Five Years of Constructive Type Theory*, Oxford: Clarendon Press.

[^schuster-2005]: Schuster, P.M., 2005, “What is continuity, constructively?”, *Journal of Universal Computer Science*, 11: 2076–2085

[^schuster-2006]: –––, 2006, “Formal Zariski topology: positivity and points”, *Annals of Pure and Applied Logic*, 137: 317–359.

[^schwichtenberg-2009]: Schwichtenberg, H., 2009, “Program extraction in constructive analysis”, in *Logicism, Intuitionism and Formalism—what has become of them?*, S. Lindström, E. Palmgren, K. Segerberg, and V. Stoltenberg-Hansen (eds.), Berlin: Springer Verlag, 255–275.

[^simpson-1984]: Simpson, S.G., 1984, “Which set existence axioms are needed to prove the Cauchy/Peano theorem for ordinary differential equations”, *Journal of Symbolic Logic*, 49(3): 783–802.

[^simpson-2009]: –––, 2009, *Subsystems of Second Order Arithmetic*, second edition, Cambridge: Cambridge University Press.

[^specker-1949]: Specker, E., 1949, “Nicht konstruktiv beweisbare Sätze der Analysis”, *Journal of Symbolic Logic*, 14: 145–158.

[^steinke-2011]: Steinke, T.A., 2011, *Constructive Notions of Compactness in Apartness Spaces*, M.Sc. Thesis, University of Canterbury, Christchurch, New Zealand.

[^troelstra-1978]: Troelstra, A.S., 1978, “Aspects of Constructive Mathematics”, in *Handbook of Mathematical Logic*, J. Barwise (ed.), Amsterdam: North-Holland.

[^troelstra-1988]: Troelstra, A.S., and van Dalen, D., 1988, *Constructivism in Mathematics: An Introduction* (two volumes), Amsterdam: North Holland.

[^atten-2004]: van Atten, M., 2004, *On Brouwer*, Belmont: Wadsworth/Thomson Learning.

[^dalen-1981]: van Dalen, D., 1981, *Brouwer’s Cambridge Lectures on Intuitionism*, Cambridge: Cambridge University Press.

[^dalen-1999]: –––, 1999, *Mystic, Geometer and Intuitionist: The Life of L.E.J. Brouwer* (Volume 1), Oxford: Clarendon Press.

[^dalen-2005]: –––, 2005, *Mystic, Geometer, and Intuitionist: The Life of L.E.J. Brouwer* (Volume 2), Oxford: Clarendon Press.

[^stigt-1990]: van Stigt, W.P., 1990, *Brouwer’s Intuitionism*, Amsterdam: North-Holland.

[^vickers-2005]: Vickers, S., 2005, “Localic completion of generalized metric spaces I”, *Theory and Applications of Categories*, 14(15): 328–356.

[^waaldijk-2005]: Waaldijk, F., 2005, *On the foundations of constructive mathematics*, *Foundations of Science*, 10(3): 249–324.

[^wallman-1938]: Wallman, H., 1938, “Lattices of topological spaces”, *Annals of Mathematics*, 39: 112–126.

[^weihrauch-2000]: Weihrauch, K., 2000, *Computable Analysis* (EATCS Texts in Theoretical Computer Science), Heidelberg: Springer Verlag.

[^weyl-1946]: Weyl, H., 1946, “Mathematics and Logic”, *American Mathematical Monthly*, 53(1): 2–13.

[^whitehead-1919]: Whitehead, A.N., 1919, *An Enquiry Concerning the Principles of Natural Knowledge*, Cambridge: Cambridge University Press, second edition, 1925.
