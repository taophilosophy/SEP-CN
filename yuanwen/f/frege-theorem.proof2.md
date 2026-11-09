# frege-theorem — proof2（supplement）

> （《frege-theorem》词条补充材料，源：plato.stanford.edu/entries/frege-theorem/proof2.html）

#### Supplement to Frege’s Theorem and Foundations for Arithmetic

## Derivation of the Law of Extensions

[Note: We use $\epsilon F$ to denote the extension of the concept $F$.]

We want to show, for an arbitrarily chosen concept P and an arbitrarily chosen object $c$, that $c\in\epsilon P\equiv Pc$.

$(\rightarrow)$ Assume $c\in\epsilon P$ to show $Pc)$. Then, by the definition of $\in$, it follows that

$\exists H(\epsilon P\eqclose \epsilon H \amp Hc)$

Suppose that $Q$ is such a property. Then, we know

$\epsilon P\eqclose \epsilon Q \amp Qc$

But, by Basic Law V, the first conjunct implies $\forall x(Px\equiv Qx)$. So from the fact that $Qc$, it follows that $Pc$.

$(\leftarrow)$ Assume $Pc$ (to show $c\in\epsilon P)$. Then, by the Existence of Extensions principle, $P$ has an extension, namely, $\epsilon P$. So by the laws of identity, we know $\epsilon P =\epsilon P$. We may conjoin this with our assumption to conclude

$\epsilon P\eqclose \epsilon P\amp Pc$

Now by existential generalizing on the concept $P$, it follows that

$\exists H(\epsilon P\eqclose \epsilon H \amp Hc)$

Thus, by the definition of $\in$, it follows that $c\in\epsilon P$.
