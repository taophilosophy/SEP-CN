# common-knowledge — proof2-18（supplement）

> （《common-knowledge》词条补充材料，源：plato.stanford.edu/entries/common-knowledge/proof2-18.html）

#### Supplement to Common Knowledge

## Proof of Proposition 2.18

**Proposition 2.18**. Let $C^*_N$ be the greatest fixed point of $f_E$. Then $C^*_N (E) = K^*_N (E)$.

**Proof**. We have shown that $\mathbf{K}^*_N (E)$ is a fixed point of $f_E$, so we only need to show that $\mathbf{K}^*_N(E)$ is the greatest fixed point. Let $B$ be a fixed point of $f_B$. We want to show that $B \subseteq \mathbf{K}^k_N(E)$ for each value $k\ge 1$. We will proceed by induction on $k$. By hypothesis,

$$ B = f_E (B) = \mathbf{K}^1_N (E\cap B) \subseteq \mathbf{K}^1_N (E) $$

by monotonicity, so we have the $k=1$ case. Now suppose that for $k=m,$ $B \subseteq \mathbf{K}^m_N(E).$ Then by monotonicity,

$$\tag{i} \mathbf{K}^1_N(B) \subseteq \mathbf{K}^1_N \mathbf{K}^m_N (E) = \mathbf{K}^{m+1}_N(E) $$

We also have:

$$\tag{ii} B = \mathbf{K}^1_N (E\cap B) \subseteq \mathbf{K}^1_N (B) $$

by monotonicity, so combining (i) and (ii) we have:

$$ B \subseteq \mathbf{K}^1_N (B) \subseteq \mathbf{K}^{m+1}_{N}(E) $$

completing the induction. $\Box$

Return to Common Knowledge
