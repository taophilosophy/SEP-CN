# common-knowledge — proof2-05（supplement）

> （《common-knowledge》词条补充材料，源：plato.stanford.edu/entries/common-knowledge/proof2-05.html）

#### Supplement to Common Knowledge

## Proof of Proposition 2.5

**Proposition 2.5**. $\omega \in \mathbf{K}^m_N(A)$ iff

**(1)**

For all agents $i_1, i_2 , \ldots ,i_m \in N, \omega \in \mathbf{K}_{i_1}\mathbf{K}_{i_2} \ldots \mathbf{K}_{i_m}(A)$

Hence, $\omega \in \mathbf{K}^*_N (A)$ iff (1) is the case for each $m \ge 1$.

**Proof**. Note first that

$$\begin{align} \tag{2} &\bigcap_{i_1\in N} \mathbf{K}_{i_1} \big( \bigcap_{i_2\in N} \mathbf{K}_{i_2} \big( \cdots \big( \bigcap_{i_{m-1}\in N} \mathbf{K}_{i_{m-1}} \big( \bigcap_{i_m\in N} \mathbf{K}_{i_m}(A) \big) \big) \big) \big) \\ &= \bigcap_{i_1\in N} \mathbf{K}_{i_1} \big( \bigcap_{i_2\in N} \mathbf{K}_{i_2} \big( \cdots \big( \bigcap_{i_{m-1}\in N} \mathbf{K}_{i_{m-1}}(\mathbf{K}^1_N(A)) \big) \big) \big) \\ &= \bigcap_{i_1\in N} \mathbf{K}_{i_1} \big( \bigcap_{i_2\in N} \mathbf{K}_{i_2} \big( \cdots \big( \bigcap_{i_{m-2}\in N} \mathbf{K}_{i_{m-2}}(\mathbf{K}^2_N(A)) \big) \big) \big) \\ &\,\,\,\vdots \\ &=\bigcap_{i_1 \in N} \mathbf{K}_{i_1}(\mathbf{K}^{m-1}_N(A)) \\ &=\mathbf{K}^m_N(A) \end{align}$$

By (2),

$$ \mathbf{K}^m_N(A) \subseteq \mathbf{K}_{i_1}\mathbf{K}_{i_2} \cdots \mathbf{K}_{i_m}(A) $$

for $i_1, i_2 , \ldots ,i_m \in N$, so if $\omega \in \mathbf{K}^m_N(A)$ then condition (1) is satisfied. Condition (1) is equivalent to

$$ \omega \in \bigcap_{i_1\in N} \mathbf{K}_{i_1} \big( \bigcap_{i_2\in N} \mathbf{K}_{i_2} \big( \cdots \big( \bigcap_{i_{m-1}\in N} \mathbf{K}_{i_{m-1}} \big( \bigcap_{i_m\in N} \mathbf{K}_{i_m}(A) \big) \big) \big) \big) $$

so by (2), if (1) is satisfied then $\omega \in \mathbf{K}^m_N(A).$ $\Box$

Return to Common Knowledge
