# frege-theorem — subproof2（supplement）

> （《frege-theorem》词条补充材料，源：plato.stanford.edu/entries/frege-theorem/subproof2.html）

#### Supplement to Frege’s Theorem and Foundations for Arithmetic

## Proof of Hume's Principle from Basic Law V—*Grundgesetze*-Style

[Note: We use $\epsilon F$ to denote the extension of the concept $F$.]

Let $P,Q$ be arbitrarily chosen concepts. We want to show:

$\#P\eqclose \#Q \equiv P\apprxclose Q$

$(\rightarrow)$ Assume $\#P = \#Q$ (to show: $P\approx Q$). Note that since $P\approx P$ (Fact 2, subsection on Equinumerosity), we know by the Lemma for Hume's Principle that $\epsilon P\in \#P$. But then, by identity substitution, $\epsilon P\in\#Q$. So, again by the Lemma for Hume's Principle, $P\approx Q$.

$(\leftarrow)$ Assume $P\approx Q$ (to show: $\#P = \#Q$). By definition of $\#$, we have to show $\epsilon P^{\approx} = \epsilon Q^{\approx}$. So, by Basic Law V, we have to show $\forall x(P^{\approx}x\equiv Q^{\approx}x)$. We pick an arbitrary object $b$ (to show: $P^{\approx}b \equiv Q^{\approx}b$).

$(\rightarrow)$ Assume $P^{\approx}b$. Then, by definition of $P^{\approx}$ and *λ*-Conversion, $\exists H(b\eqclose \epsilon H \amp H \apprxclose P)$. Let $R$ be an arbitrary such concept; so $b\eqclose \epsilon R\amp R\apprxclose P$. From the second conjunct and our initial hypothesis, it follows (by the transitivity of equinumerosity) that $R\apprxclose Q$. So, reassembling what we know, it follows that $b\eqclose \epsilon R\amp R\apprxclose Q$. By existential generalization, it follows that $\exists H(b\eqclose \epsilon H \amp H \apprxclose Q)$. So by *λ*-Conversion,

$[\lambda x \, \exists H(x\eqclose \epsilon H\amp H\apprxclose Q)]b$

It follows from this, by definition of $Q^{\approx}$, that $Q^{\approx}b$.

$(\leftarrow)$ (Exercise)
