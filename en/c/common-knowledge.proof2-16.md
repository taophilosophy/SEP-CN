# common-knowledge — proof2-16（supplement）

> （《common-knowledge》词条补充材料，源：plato.stanford.edu/entries/common-knowledge/proof2-16.html）

#### Supplement to Common Knowledge

## Proof of Lemma 2.16

**Lemma 2.16**. $\mathcal{M}(\omega)$ is common knowledge for the agents of $N$ at *ω*.

**Proof**. Since $\mathcal{M}$ is a coarsening of $\mathcal{H}_i$ for each $i \in N,$ $\mathbf{K}_i (\mathcal{M}(\omega))$. Hence, $\mathbf{K}^1_N (\mathcal{M}(\omega)),$ and since by definition $\mathbf{K}_i (\mathcal{M}(\omega)) = \{ \omega \mid \mathcal{H}_i (\omega) \subseteq \mathcal{M}(\omega)\} = \mathcal{M}(\omega)$,

$$ \mathbf{K}^{1}_N (\mathcal{M}(\omega)) = \bigcap_{i \in N} \mathbf{K}_i (\mathcal{M}(\omega)) = \mathcal{M}(\omega) $$

Applying the recursive definition of mutual knowledge, for any $m \ge 1$,

$$\begin{align} \mathbf{K}^m_N(\mathcal{M}(\omega)) &= \bigcap_{i \in N}\mathbf{K}_i (\mathbf{K}^{m-1}_{N}(\mathcal{M}(\omega)) \\ &= \bigcap_{i \in N}\mathbf{K}_i (\mathcal{M}(\omega)) \\ &= \mathcal{M}(\omega) \end{align}$$

so, since $\omega \in \mathcal{M}(\omega)$, by definition we have $\omega \in \mathbf{K}^*_N (\mathcal{M}(\omega)).$ $\Box$

Return to Common Knowledge
