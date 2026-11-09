# dynamic-epistemic — appendix-J-CDL（supplement）

> （《dynamic-epistemic》词条补充材料，源：plato.stanford.edu/entries/dynamic-epistemic/appendix-J-CDL.html）

#### Supplement to Dynamic Epistemic Logic

## Appendix J: Conditional Doxastic Logic

The language \eqref{CDL} of *conditional doxastic logic* is defined by the following grammar:

$$\begin{gather*}\taglabel{CDL} F \ccoloneqq p \mid F\land F \mid \lnot F\mid B_a^FF \\ \small p\in\sP,\; a\in\sA \end{gather*}$$

We think of the formula $B_a^FG$ as saying that agent *a* believes *F* after conditionalization (or static belief revision) by *G*. The satisfaction relation $\models$ between pointed plausibility models and formulas of \eqref{CDL} and the set $\sem{F}_M$ of worlds in the plausibility model *M* at which formula *F* is true are defined by the following recursion.

- $\sem{F}_M\coloneqq\{w\in W\mid M,w\models F\}$.
- $M,w\models p$ holds if and only if $w\in V(p)$.
- $M,w\models F\land G$ holds if and only if $M,w\models F$ and $M,w\models G$.
- $M,w\models\lnot F$ holds if and only if $M,w\not\models F$.
- $M,w\models B_a^GF$ holds if and only if $\min_a(\sem{G}_M\cap\cc_a(w))\subseteq\sem{F}_M$. $B_a^GF$ means that “*F* is true at the most plausible *G*-worlds consistent with *a*’s information”.

In the language \eqref{CDL}, the operator $K_a$ for possession of information may be defined as follows:

$$ K_a F \text{ denotes } B_a^{\lnot F}\bot, $$

where $\bot$ is the propositional constant for falsehood. We then have the following.

**Theorem (Baltag and Smets 2008b).** For each pointed plausibility model $(M,w)$, we have: $$ M,w\models B_a^{\lnot F}\bot \text{ iff } M,v\models F \text{ for each }v \text{ with } v\simeq_a w. $$ So the \eqref{CDL}-abbreviation of $K_aF$ as $B_a^{\lnot F}\bot$ gives the same meaning in \eqref{CDL} for “possession of information” as we had in $(K\Box)$.

The validities of \eqref{CDL} are axiomatized as follows.

**The axiomatic theory $\CDL$ (Baltag, Renne, and Smets 2015).**

- Axiom schemes and rules for classical propositional logic
- $B_a^F(G_1\to G_2)\to (B_a^FG_1\to B_a^FG_2)$
- $B_a^FF$
- $B_a^F\bot\to B_a^{F\land G}\bot$
- $\lnot B_a^F\lnot G\to( B_a^FH\to B_a^{F\land G}H)$
- $B_a^{F\land G}H\to B_a^F(G\to H)$
- $B_a^{F\land G}H\to B_a^{G\land F}H$
- $B_a^FH\to B_a^G B_a^FH$
- $\lnot B_a^FH\to B_a^G\lnot B_a^FH$
- $B_a^F\bot\to\lnot F$

**$\CDL$ Soundness and Completeness (Board 2004; Baltag and Smets 2008b; Baltag, Renne, and Smets 2015).** $\CDL$ is sound and complete with respect to the collection $\sC_*$ of pointed plausibility models. That is, for each \eqref{CDL}-formula *F*, we have $\CDL\vdash F$ if and only if $\sC_*\models F$.

← beginning of main article
