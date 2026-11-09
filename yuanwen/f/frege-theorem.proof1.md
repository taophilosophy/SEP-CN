# frege-theorem — proof1（supplement）

> （《frege-theorem》词条补充材料，源：plato.stanford.edu/entries/frege-theorem/proof1.html）

#### Supplement to Frege’s Theorem and Foundations for Arithmetic

## First Derivation of the Contradiction

[Note: We use $\epsilon F$ to denote the extension of the concept $F$. We use the expression ‘$F(\epsilon G)$’ to more clearly express the fact that the extension of the concept $G$ falls under $F$.]

The $\lambda$-expression which denotes the concept *being the extension of a concept one doesn’t fall under* is

$[\lambda x \, \exists F(x\eqclose \epsilon F \amp \neg Fx)]$

As we saw in the text, we know that such a concept as this exists, by the Comprehension Principle for Concepts. Let ‘$P$’ abbreviate this name of the concept. So $\epsilon P$ exists, by the Existence of Extensions principle.

Now suppose that $P(\epsilon P)$, i.e., suppose

[$\lambda x \, \exists F(x\eqclose \epsilon F \amp \neg Fx)](\epsilon P)$

Then, by the principle of $\lambda$-Conversion, it follows that

$\exists F[\epsilon P\eqclose \epsilon F\amp \neg F(\epsilon P)]$

Let $H$ be an arbitrary such concept. So we know the following about $H$

$\epsilon P\eqclose \epsilon H\amp \neg H (\epsilon P)$

Now given Law V, it follows from the first conjunct that $\forall x(Px\equiv Hx)$. So since $\neg H(\epsilon P)$, it follows that $\neg P(\epsilon P)$, contrary to hypothesis.

So suppose instead that $\neg P(\epsilon P)$. But, now, by $\lambda$-conversion, it follows that:

$\neg\exists F[\epsilon P\eqclose \epsilon F\amp \neg F(\epsilon P)]$,

i.e.,

$\forall F[\epsilon P\eqclose \epsilon F\rightarrow F(\epsilon P)]$

But by instantiating this universal claim to $P$, it follows from the self-identity of $\epsilon P$ that $P(\epsilon P)$, contrary to hypothesis.

Contradiction.
