# frege-theorem — proof3（supplement）

> （《frege-theorem》词条补充材料，源：plato.stanford.edu/entries/frege-theorem/proof3.html）

#### Supplement to Frege’s Theorem and Foundations for Arithmetic

## Derivation of the Principle of Extensionality from Basic Law V

[Note: We use $\epsilon F$ to denote the extension of the concept $F$.]

Assume *Extension*(x) and *Extension*(y). Then $\exists F(x\eqclose \epsilon F)$ and $\exists G(y\eqclose \epsilon G)$. Let $P,Q$ be arbitrary such concepts; i.e., suppose $x\eqclose \epsilon P$ and $y \eqclose \epsilon Q$.

Now to complete the proof, assume $\forall z(z\in x \equiv z\in y)$. It then follows that $\forall z(z\in\epsilon P\equiv z\in\epsilon Q)$. So, by the Law of Extensions and the principles of predicate logic, we may convert both conditions in the universalized biconditional to establish that $\forall z(Pz\equiv Qz)$. So by Basic Law V, $\epsilon P =\epsilon Q$. So $x = y$.
