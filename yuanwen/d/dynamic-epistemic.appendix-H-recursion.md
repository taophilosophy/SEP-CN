# dynamic-epistemic — appendix-H-recursion（supplement）

> （《dynamic-epistemic》词条补充材料，源：plato.stanford.edu/entries/dynamic-epistemic/appendix-H-recursion.html）

#### Supplement to Dynamic Epistemic Logic

## Appendix H: Recursive definition of languages with action models

Formally, the grammar (EAL) is defined by double recursion as follows. First, let $(\text{EAL}^0)$ be the language (ML) of modal logic, and let $\AM_*^0$ be the set of pointed action models whose precondition qformulas all come from the language $(\text{EAL}^0)$. Then, whenever $(\text{EAL}^n)$ and $\AM_*^n$ are both defined, we define the language $(\text{EAL}^{n+1})$ and the set $\AM_*^{n+1}$ as follows:

$$\begin{gather*}\tag{\(\text{EAL}^{n+1}\)} F \ccoloneqq p \mid F\land F \mid \lnot F \mid [a]F \mid [A,e]F \\ \small p\in\sP,\; a\in\sA,\; (A,e)\in\AM_*^n \end{gather*}$$

and we let $\AM_*^{n+1}$ be the set of pointed action models whose precondition formulas all come from the language $(\text{EAL}^{n+1})$. Finally, we define (EAL) as the union $$ \text{(EAL)} \coloneqq \bigcup_{n\in\mathbb{N}} (\text{EAL}^n) $$ of all languages $(\text{EAL}^n)$ and we define $\AM_*$ to be the union $$ \AM_* \coloneqq \bigcup_{n\in\mathbb{N}} \AM_*^n $$ of all sets $\AM_*^n$. For convenience, we let $\AM^n$ denote the set of all action models whose precondition formulas are all in the language $(\text{EAL}^n)$, and we let $\AM$ denote the set of all action models whose precondition formulas are all in the language (EAL). A useful lemma is the following.

**Inclusion Lemma.** $m\leq n$ implies $(\text{EAL}^m)\subseteq(\text{EAL}^n)$ and $\AM^m\subseteq\AM^n$.

We often need a complete, well-founded binary relation on (EAL)-formulas that orders these formulas in such a way that the right side of each of the following equivalences—the EAL reduction axioms—has a “smaller” position in the ordering than does the left side (so that going left to right in a reduction axiom “reduces” the position in the ordering).

1. $[A,e]p\leftrightarrow(\pre(e)\to p)$ for letters $p\in\sP$
2. $[A,e](G\land H)\leftrightarrow([A,e]G\land[A,e]H)$
3. $[A,e]\lnot G\leftrightarrow(\pre(e)\to\lnot[A,e]G)$
4. $[A,e][a]G\leftrightarrow (\pre(e)\to\bigwedge_{e R_a f} [a][A,f]G)$

A natural strict dictionary ordering is given as follows. First, for each [EAL]-formula *F*, let $d(F)$ denote the *(non–precondition-recursing) formation depth* of *F* and $D(F)$ denote the *post-action (non–precondition-recursing) formation depth* of *F*.

$$\begin{align*} d(p) &= 0 \text{ for letters }p\in\sP \\ d(F\land G) &= 1 + \max(d(F),d(G)) \\ d(\lnot F) &= 1+d(F) \\ d([a]F) &= 1+d(F) \\ d([A,e]F) &= 1+d(F) \end{align*}$$

$$\begin{align*} D(p) &= 0 \text{ for letters }p\in\sP \\ D(F\land G) &= \max(D(F),D(G)) \\ D(\lnot F) &= D(F) \\ D([a]F) &= D(F) \\ D([A,e]F) &= d(F) \end{align*}$$

The number $d(F)$ tells us the maximum number of steps required to construct a part of *F* without counting recursive steps used to construct preconditions of action models. The number $D(F)$ tells us the maximum number of steps required to construct a part of a formula in *F* that comes just after an action, again without counting recursive steps used for precondition construction. (So in each case, a “step” is a recursive call to the grammar $(\text{EAL}^n)$ for some fixed *n* such that $F\in(\text{EAL}^n)$.) Proceeding, let $L(F)$ denote the *recursion level* of the (EAL)-formula *F*; that is, $L(F)$ is the smallest non-negative integer *n* such that $F\in(\text{EAL}^n)$. Finally, we order (EAL)-formulas as follows: assign to each (EAL)-formula *F* the pair $(L(F),D(F))$ and then order according to the strict dictionary ordering on pairs of integers (i.e., order first by the left number and then by the right number).

**Dictionary Ordering of (EAL)-formulas.** $F\lt G$ means that either $L(F)\lt L(G)$ or else both $L(F)=L(G)$ and $D(F)\lt D(G)$.

Note that we have $L(\pre^A(e))\lt L([A,e]F)$ for each $(A,e)\in\AM_*$ and $F\in\text{(EAL)}$. One can then check that the following holds.

**EAL Dictionary Ordering Lemma.** For each of the schemes 1–4 listed above, if $F_1$ denotes the formula on the left side of the equivalence and $F_2$ denotes the formula on the right, then $F_2\lt F_1$.

Another useful ordering introduced by van Ditmarsch, van der Hoek, and Kooi (2007) is given by assigning a non-negative integer “complexity” $c(F)$ to each (EAL)-formula and then ordering according to the usual strict ordering on the integers.

$$\begin{align*} c(p) &= 0 \text{ for letters }p\in\sP \\ c(F\land G) &= 1+\max(c(F),c(G)) \\ c(\lnot F) &= 1+c(F) \\ c([a]F) &= 1+c(F) \\ c([A,e]F) &= (4+c(A))\cdot c(F) \\ c(A) &= \max\{c(\pre^A(f)) \mid f \text{ is an event in } A\} \end{align*}$$

**EAL Complexity Ordering Lemma (van Ditmarsch, van der Hoek, and Kooi 2007).** For each of the schemes 1–4 listed above, if $F_1$ denotes the formula on the left side of the equivalence and $F_2$ denotes the formula on the right, then $c(F_2)\lt c(F_1)$.

The ordering lemmas make precise the idea that the right side of a given reduction axiom is “less complex” than the left side. These lemmas are used extensively to prove important results whose proof, like that of the Reduction Theorem, calls for an induction on (EAL)-formulas.

Finally, we note that showing the correctness of our definition of the binary satisfaction relation $\models$ between the class $\sC_*$ of pointed Kripke models and the set of (EAL)-formulas can be done by way of an induction as well. In particular, we may use the ordering lemmas or the value *n* for the languages $(\text{EAL}^n)$—the latter is probably most natural—to provide an inductive construction of a binary satisfaction relation ${\models}\;\subseteq\; \sC_*\times\text{(EAL)}$ between pointed Kripke models and (EAL)-formulas that minimally extends the binary satisfaction relation ${\models}\;\subseteq\;\sC_*\times\text{(ML)}$ for the basic modal language (see [Appendix A](dynamic-epistemic.appendix-A-kripke.md)) such that for each $[A,e]G\in\text{(EAL)}$, we have the following:

- $M,w\models[A,e]G$ holds if and only if $M,w\not\models\pre^A(e)$ or $M[A],(w,e)\models G$, where the Kripke model $M[A]$ is defined via the BMS product update (Baltag, Moss, and Solecki 1998).

Correctness of the definition of satisfaction relations for other action model-style languages can be shown using similar methods.

← beginning of main article
