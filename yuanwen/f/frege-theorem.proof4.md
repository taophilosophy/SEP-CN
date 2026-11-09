# frege-theorem — proof4（supplement）

> （《frege-theorem》词条补充材料，源：plato.stanford.edu/entries/frege-theorem/proof4.html）

#### Supplement to Frege’s Theorem and Foundations for Arithmetic

## Proof of Lemma Concerning Zero

Let $P$ be an arbitrarily chosen concept. We want to show $\#P = 0\equiv\neg\exists xPx$.

$(\rightarrow)$ Assume $\#P = 0$. Then, by definition of $0, \#P = \#[\lambda z \, z\neq z]$. So by Hume's Principle, $P$ is equinumerous to $[\lambda z \, z\neq z]$. So, by the definition of equinumerosity, there is an R that maps every object falling under $P$ to a unique object falling under $[\lambda z \, z\neq z]$ and vice versa. Suppose, for reductio, that $\exists xPx$, say $Pa$. Then there is an object, say $b$, such that $Rab$ and $[\lambda z \, z\neq z]b$. But, then, by $\lambda$-Conversion, $b$ is not self-identical, which contradicts the laws of identity.

$(\leftarrow)$ Suppose $\neg\exists xPx$. Now as we have seen, the laws of identity guarantee that no object falls under the concept $[\lambda z \, z\neq z]$. But then any relation you please bears witness to the fact that $P$ is equinumerous with $[\lambda z \, z\neq z]$. For let $R$ be some arbitrary relation. Then (a) every object falling under P bears R to a unique object falling under $[\lambda z \, z\neq z]$ (since there are no objects falling under $P$ ), and (b) every object falling under $[\lambda z \, z\neq z]$ is such that there is a unique object falling under $P$ that bears $R$ to it (since there are no objects exemplifying $[\lambda z \, z\neq z])$. Since $P$ is therefore equinumerous with $[\lambda z \, z\neq z]$, it follows by Hume's Principle, that $\#[\lambda z \, z\neq z] = \#P$. But, then, by definition, $0 = \#P$.
