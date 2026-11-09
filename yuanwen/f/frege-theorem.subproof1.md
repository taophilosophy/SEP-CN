# frege-theorem — subproof1（supplement）

> （《frege-theorem》词条补充材料，源：plato.stanford.edu/entries/frege-theorem/subproof1.html）

#### Supplement to Frege’s Theorem and Foundations for Arithmetic

## Proof of the Lemma for Hume's Principle

[Note: We use $\epsilon F$ to denote the extension of the concept $F$.]

Let $P,Q$ be arbitrarily chosen concepts. We want to show:

$\epsilon Q \in \#P \equiv Q\approx P$

So, by definition of $\#P$, we have to show:

$\epsilon Q \in \epsilon P^{\approx} \equiv Q\approx P$,

where $P^{\approx}$ was previously defined as $[\lambda x \, \exists H(x\eqclose \epsilon H \amp H\apprxclose F)]$.

We prove this by appealing to the following instance of the Law of Extensions:

*Fact*: $\epsilon Q\in\epsilon P^{\approx}\equiv P^{\approx}(\epsilon Q)$

$(\rightarrow)$ Assume $\epsilon Q\in \epsilon P^{\approx}$ (to show: $Q \approx P$). Then, by the above Fact, we know $P^{\approx}(\epsilon Q)$. So by the definition of $P^{\approx}$:

$[\lambda x \,\exists H(x\eqclose \epsilon H\amp H\approx P)](\epsilon Q)$

By $\lambda$-conversion, this implies:

$\exists H(\epsilon Q =\epsilon H\amp H\approx P)$

Suppose $R$ is an arbitrary such concept:

$$\tag{1} \epsilon Q\eqclose \epsilon R \amp R\apprxclose P $$

Then by Basic Law V, the first conjunct implies $\forall x(Qx\equiv Rx)$. Since the material equivalence of two concepts implies their equinumerosity (Fact 1, subsection on Equinumerosity, in the main part of the entry), it follows that $Q\approx R$. So from this result and the second conjunct of (1), it follows that $Q\approx P$, by the transitivity of equinumerosity (Fact 4 in the subsection on Equinumerosity).

$(\leftarrow)$ Assume $Q\approx P$ (to show $\epsilon Q\in \epsilon P^{\approx}$). Then, by identity introduction, we know: $\epsilon Q =\epsilon Q\amp Q\approx P$. So, by existential generalization:

$\exists H(\epsilon Q\eqclose \epsilon H \amp H\approx P)$

And by $\lambda$-Conversion:

$[\lambda x \, \exists H(x\eqclose \epsilon H \amp H\approx P)](\epsilon Q)$

Hence, by definition, $P^{\approx}(\epsilon Q)$. So, by the above Fact, $\epsilon Q\in \epsilon P^{\approx}$.
