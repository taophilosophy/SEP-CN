# proof-theory — appendix-c（supplement）

> （《proof-theory》词条补充材料，源：plato.stanford.edu/entries/proof-theory/appendix-c.html）

#### Supplement to Proof Theory

## C. Bar Induction, Spector’s Result, and the Ω-rule

Here we discuss the principle of bar induction, Spector’s proof and a relationship between bar induction and an infinitary proof rule devised by Buchholz.

- C.1 Bar induction
- C.2 An outline of Spector’s interpretation
- C.3 Bar induction and Buchholz’ Ω-rule

### C.1 Bar induction

The Bar Theorem is a theorem about trees. It occupies a prominent place in Brouwer’s development of intuitionist mathematics and has also played a central role in proof theory in the 1960s and 1970s. Here we will give a brief account of it since it is essential to Spector’s functional interpretation of second order arithmetic. Its proof-theoretic analysis provides a nice demonstration of Buchholz’ Ω-rule.

Definition C.1 Let $\bbN^*$ be the set of all finite sequences of natural numbers including the empty sequence $\langle\rangle$. $\bbN^*$ can be viewed as an infinite tree which grows from the root $\langle\rangle$ upwards. If $s\in\bbN^*$, $m\in\bbN$ and $s=\langle s_0,\ldots s_k\rangle$ then the immediate successor nodes or children of *s* are of the form $s*\langle m\rangle$ defined as $\langle s_0,\ldots,s_k,m\rangle$. *t* is a node *above* *s* if *t* is of the form $s*\langle k_0\rangle*\ldots*\langle k_r\rangle$.

A bar of $\bbN^*$ is a subclass *B* of $\bbN^*$ such that every infinite path through $\bbN^*$ goes through *B*; in Brouwer’s terminology, every infinite path is “barred” by *B*. More formally this is defined as follows. For a function $f:\bbN\to \bbN$ and $n\in\bbN$, $\bar{f}n$ denotes the sequence $\langle f(0),\ldots, f(n-1)\rangle (\bar{f}0= \langle\rangle)$. A *bar* *B* for $\bbN^*$ is a subclass of $\bbN^*$ such that for all $f:\bbN\to\bbN$ there exists $n\in\bbN$ such that $\bar fn\in B$.

Bar induction is the following principle:

$$ \tag*{\(\BI_{\igen}\)} \textrm{Hyp 1}\land \textrm{Hyp 2}\land \textrm{Hyp 3}\land\textrm{Hyp 4} \to Q(\langle \rangle) $$

where

$$\begin{align} \tag{Hyp 1} & B \textrm{ is a bar}\\ \tag{Hyp 2} & \forall s\in \bbN^*\,\forall n\in\bbN\,(s\in B\rightarrow s*\langle n\rangle\in B)\\ \tag{Hyp 3} & \forall s\in \bbN^*\,(s\in B\to s\in Q) \\ \tag{Hyp 4} &\forall s\in\bbN^*\,[(\forall k\in\bbN\;s*\langle k\rangle \in Q)\to s\in Q]. \end{align}$$

Clause (Hyp 4) asserts that the property of being in *Q* propagates to a node *s* if all its children belong to *Q*. Since all nodes in the bar belong to *Q* by (Hyp 3), the intuitive idea behind this principle is that the clauses (Hyp 1–4) guarantee that membership in *Q* “percolates” from the bar all the way down to the root.[^note-51]

Brouwer’s justification for the Bar theorem (1927), that is, of the general validity of Bar Induction, rests on the idea that any canonical proof of (Hyp 1) in infinitary logic has a particular structure which allows one, when supplied with proofs of (Hyp 2–4), to transform it into a proof of $Q(\langle \rangle)$. With hindsight, one could say that Brouwer is assuming that a canonical proof is something like a cut-free proof in $\omega$-logic.

The notions of Definition C.1 can be easily formalized in the language of second order arithmetic. If one doesn’t impose any restrictions on the complexity of the bar *B* and the predicate *Q* (i.e., allowing them to be expressed by any formula of the language), then $\BI_{\igen}$ is surprisingly strong when classical logic is assumed as shown by Howard (1963, section 2.3).

Theorem C.2 $\BI_{\igen}$ implies full second order comprehension ${\bCA}$ (actually $\bAC$) and is conservative over $\bZ_2$ for $\Pi^1_4$ sentences.[^note-52] (Conservativity for $\Pi^1_4$ sentences is not shown in (Howard, 1963).)

On the other hand, when the ambient logic is intuitionist, $\BI_{\igen}$ is much weaker than $\bZ_2$. To obtain an intuitionist theory of that strength based on the idea of Bar Induction one needs to consider Bar Induction on higher types.

### C.2 An outline of Spector’s interpretation

In his 1960, Spector gave a consistency proof of $\bZ_2$ by means of a functional interpretation. To find a class of functionals sufficient unto the task of lifting the D-interpretation to $\bZ_2$, he defined the so-called bar recursive functionals. The crucial step in the interpretation is to furnish a functional interpretation of the negative translation of $\BI_{\igen}$, which by Theorem C.2 gives rise to an interpretation of $\bZ_2$. For this he extended intuitionist $\BI_{\igen}$ to all finite types. Bar induction for type $\sigma$, $\BI_{\sigma}$, is formulated similar to $\BI_{\igen}$, the difference being that instead of just looking at the tree of all finite sequences of natural numbers $\bbN^*$, one takes the full tree of finite sequences $\langle F_1,\ldots,F_r\rangle$ of objects $F_i$ of type $\sigma$, $\cT_{\sigma}$. A bar of the latter is defined in complete analogy to a bar of $\bbN^*$.

Instead of $\BI_{\sigma}$, Spector’s extension of **T** has a scheme, $\bBR_{\sigma}$ for defining functionals by *bar recursion* on the tree $\cT_{\sigma}$. The first step is to interpret the theory $\bHA^{\sharp}+\BI_{\sigma}$ in Spector’s $\bT+\bBR_{\sigma}$, where $\bHA^{\sharp}$ is the theory $\bHA^{\omega}$ augmented by the axioms

$$ \tag{c1}\label{D} A\leftrightarrow A^D $$

with $A^D$ being the Gödel Dialectica interpretation of *A*. A functional interpretation of $A\leftrightarrow A^D$ follows from observing that $(A\leftrightarrow A^D)^D$ is identical to $(A\leftrightarrow A)^D$. With this one can see that $\bHA^{\sharp}+\BI_{\sigma}$ has a functional interpretation in $\bT+ \bBR_{\sigma}$.

The next step, which furnishes the interpretation of classical $\BI_{\igen}$ (and thereby of full ${\bCA}$) is to look at the negative interpretation of some instances of $\BI_{\sigma}$ in $\bHA^{\sharp}+\BI_{\sigma}$. The main task is to verify the negative interpretation of (Hyp 1) of special forms of $\BI_{\sigma}$,

$$\tag{c2}\label{h1} \forall f\exists n\,P(\bar{f}n) $$

with the predicate $P(c)$ being of the form $\exists Z\,B(Z,c)$ where $B(Z,c)$ is quantifier free and *c* is of type $\sigma$ (see Howard 1968, Lemma 4D). The negative translation of $(\ref{h1})$ is

$$ \forall f\,\neg\neg\exists n\, P(\bar{f}n)^N\mbox{; i.e., }\forall f\,\neg\neg \exists n\,\neg\neg \exists Z\,B(Z,\bar{f}n) $$

since $B(Z,c)$ is quantifier free. The *D*-translation of the latter formula is the same as that of $\forall f\exists n\neg\neg\exists Z\,B(Z,\bar{f}n)$. Note that a generalization of Markov’s principle is a consequence of ($\ref{D}$). As a result, $\forall f\neg\neg\exists n\,P(\bar{f}n)^N$ is equivalent in $\bHA^{\sharp}$ to $\forall f\exists n\,P(\bar{f}n)^N$, so (Hyp 1) has been restored. Spector was rather cautious not to claim that his theory $T+\bBR$ gives a constructive interpretation of $\bZ_2$.

> The author believes that the bar theorem is itself questionable, and that until the bar theorem can be given a suitable foundation, the question of whether bar induction is intuitionistic is premature. (Spector 1962: 2)

The question of constructivity of bar recursion was also answered in the negative by Kreisel; cf. section 5.3. On closer inspection of the proof, one is left with the impression that logically complex comprehensions are traded in for inductions on highly complex higher type relations.[^note-53] That notwithstanding, Spector’s result is quite remarkable and his interpretation has been applied to extract computational information from classical proofs (Kohlenbach 2007).

### C.3 Bar induction and Buchholz’ Ω-rule

By Theorem C.2, $\BI_{\igen}$ with classical logic is very strong. If the background logic is assumed to be just intuitionist, then is a lot weaker, namely of the same strength as the theory of non-iterated inductive definitions $\bID_1$ (which has the Bachmann-Howard ordinal as its proof-theoretic ordinal; see section 5.3.1). So $\BI_{\igen}$ is an example of a theory where the law of excluded middle makes an enormous difference. A classical theory of the same strength as intuitionist $\BI_{\igen}$ is obtained by requiring the bar *B* to be a set. This theory is usually denoted by $\BI$. An equivalent formalization of $\BI$ is given by the schema of quantifier elimination (see Feferman 1970b):

$$ \tag{\(\forall^2\textrm{-E}\)} \forall X\,A(X) \to A(F) $$

for any arithmetical formula $A(X)$ and arbitrary $\cL_2$-formula $F(u)$, where $A(F)$ arises from $A(X)$ by replacing all occurrences of the form $t\in X$ in the formula by $F(t)$.

Ever since the great successes with the $\omega$-rule, which restored cut elimination in arithmetic, proof theorists were looking for stronger forms of infinitary proof rules that could bring about cut elimination for genuinely impredicative theories. Buchholz was the first who succeeded in finding such a rule. He introduced the Ω-rule in Buchholz 1977a, and extended versions of it are the central tool in Buchholz and Schütte 1988. A sequent calculus version of it was used in Rathjen and Weiermann 1993 to give a proof-theoretic bound on Kruskal’s theorem and this is the version we will briefly discuss. According to the intuitionist interpretation of an implication (called the Brouwer-Heyting-Kolmogorov (BHK) interpretation) the truth of an implication $C\to D$ is explained in terms of a construction that transforms any proof of *C* into a proof of *D*. This idea may serve as a first approach to the Ω-rule:

- $(\tilde{\Omega})$If for every cut free proof[^note-54] $\cD$ of $\forall X A(X)$ we have $\cT(\cD)\vdash\Theta\Rightarrow \Xi$, then $\cT$ is considered to be a proof of $\Theta,\forall XF(X)\Rightarrow \Xi$.

Since any cut free proof of $\forall XA(X)$ can be transformed into a proof of $A(F)$, just by the operation $\cT$ of substituting $F(t)$ for $t\in X$ in $A(X)$, this rule allows one to prove $(\forall^2\mbox{-E})$. However, $(\tilde{\Omega})$ is just too naive an approach since this rule does not behave well with respect to cut elimination, particularly since side formulae (assumptions) are not taken into account. So the actual Ω-rule takes a rather more involved form:

Definition C.3

- $(\Omega)$If for all finite sets of $\Sigma^1_1$-formulae $\Gamma$ and $\Pi^1_1$-formulae $\Delta$, every cut free proof $\cD$ of $$\Gamma\Rightarrow \Delta, \forall X A(X)$$ can be transformed into a proof $\cT(\cD)$ of $\Gamma,\Theta\Rightarrow \Delta,\Xi$, then $\cT$ is considered to be a proof of $\Theta,\forall XF(X)\Rightarrow \Xi$.

With the help of the Ω-rule one obtains an ordinal analysis of (**BI**.); see Buchholz and Schütte 1988 and Rathjen and Weiermann 1993. In view of Brouwer’s speculative justification of bar induction, it is perhaps gratifying to see that a proof-theoretic analysis of (**BI**) can be obtained via a rule that embodies transformations on infinite canonical proof trees.


## Notes（原文脚注，引自主文）

[^note-51]: 51. Brouwer did not include (Hyp 2) among the hypothesis. It expresses the “monotonicity” of the bar. Classically it’s rather superfluous but intuitionistically it is essential as Kleene observed: $\BI_{\igen}$ formulated without (Hyp 2) yields instances of excluded middle that are incompatible with Brouwer’s continuity principles (Kleene & Vesley 1965: 7.14).

[^note-52]: 52. A bar *B* gives rise to a well-founded ordering $\prec$ on $\bbN^*$ where $t\prec s$ means that *t* is a node above *s* and $t\notin B$. Viewed in this way, $\BI_{\igen}$ is a principle of transfinite induction along $\prec$. For the implication $\BI_{\igen}\to{\bCA}$ to hold it is important that *B* can be of arbitrary complexity. Thus the moral drawable from this is that impredicative comprehension can be deduced from transfinite induction on impredicatively defined orderings.

[^note-53]: 53. Girard is also very skeptical about the intuitionistic setting of Spector’s interpretation: “all these topics have *nothing to do* with intuitionism” (Girard 1987: 479).

[^note-54]: 54. As a matter of clarification, cut free proofs are not allowed to contain other instances of $\tilde{\Omega}$.

### Notes to Appendix D