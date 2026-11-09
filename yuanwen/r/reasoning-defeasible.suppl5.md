# reasoning-defeasible — suppl5（supplement）

> （《reasoning-defeasible》词条补充材料，源：plato.stanford.edu/entries/reasoning-defeasible/suppl5.html）

#### Supplement to Defeasible Reasoning

## Models of Higher-Order Probability

A model of higher-order probability consists of $W$, a set of possible worlds, together with a function that assigns to each world $w$ a probability function $\mu_w$. Let’s assume that these probability functions are non-standard, that is, they may assign infinitesimal probabilities to some sets of worlds. Let $[W]$ be the partition of $W$ in terms of probabilistic agreement: worlds $w$ and $w'$ belong to the same cell of $[W]$ just in case they are assigned exactly the same probability function.

Let $A$ be a subset of $[W]$. The set-theoretic union of $A$, $\bigcup A$, is a proposition expressible entirely in terms of probabilities (that is, entirely in terms of Boolean combinations of $\Rightarrow$ conditionals). In the finite case, Miller’s principle states that, for all worlds $w$ and all propositions $B$ and $C$:

$\mu_w (C / B \cap \bigcup A) = \Sigma_{w' \in \cup A}\, \mu_{w'}(C / B) \times \mu_w (\{w\})$

The logic of extreme higher-order probabilities consists of Lewis’s $VC$ conditional logic, minus Strong Centering, and plus the following two axiom schemata, which I call Skyrms’s axioms (Koons 2000, Appendix B):

$(p \Rightarrow(q \Rightarrow r)) \leftrightarrow((p \amp q) \Rightarrow r)$

$[(p \Rightarrow \neg(q \Rightarrow r)) \amp \neg((p \amp q) \Rightarrow \bot)] \leftrightarrow \neg((p \amp q) \Rightarrow r)$

In both cases, “$p$” must be a Boolean combination of $\Rightarrow$-conditionals. The variables “$q$” and “$r$” may be replaced by any two formulas. The formula $\neg((p \amp q) \Rightarrow \bot)$ expresses the joint possibility of $p$ and $q$ (in the sense that they don’t defeasibly imply a logical absurdity, $\bot)$.
