# common-knowledge — proof2-08（supplement）

> （《common-knowledge》词条补充材料，源：plato.stanford.edu/entries/common-knowledge/proof2-08.html）

#### Supplement to Common Knowledge

## Proof of Proposition 2.8

**Proposition 2.8**. $\mathbf{L}^*_N(E) \subseteq \mathbf{K}^*_N(E)$, that is, Lewis-common knowledge of $E$ implies common knowledge of $E$.

**Proof**. Suppose that $\omega \in \mathbf{L}^*_N(E)$. By definition, there is a basis proposition $A^*$ such that $\omega \in A^*$. It suffices to show that for each $m \ge 1$ and for all agents $i_1, i_2 , \ldots ,i_m \in N$,

$$ \omega \in \mathbf{K}_{i_1}\mathbf{K}_{i_2} \ldots \mathbf{K}_{i_m}(E) $$

We prove the result by induction on $m$. The $m = 1$ case follows at once from (L1) and (L3). Now if we assume that for $m = k, \omega \in \mathbf{L}^*_N (E)$ implies $\omega \in \mathbf{K}_{i_1}\mathbf{K}_{i_2} \ldots \mathbf{K}_{i_k}(E)$, then $\mathbf{L}^*_N(E) \subseteq \mathbf{K}_{i_1}\mathbf{K}_{i_2} \ldots \mathbf{K}_{i_k}(E)$ because $\omega$ is an arbitrary possible world, so $\mathbf{K}_{i_1}(A^*) \subseteq \mathbf{K}_{i_1}\mathbf{K}_{i_2} \ldots \mathbf{K}_{i_k}(E)$ by (L3). Since (L2) is the case and the agents of $N$ are $A^*$-symmetric reasoners,

$$ \mathbf{K}_{i_1}(A^*) \subseteq \mathbf{K}_{i_1}\mathbf{K}_{i_2} \ldots \mathbf{K}_{i_{k+1}}(E) $$

for any $i_{k+1} \in N$, so $\omega \in \mathbf{K}_{i_1}\mathbf{K}_{i_2} \ldots \mathbf{K}_{i_{k+1}}(E)$ by (L1), which completes the induction since $i_1, i_2 , \ldots ,i_k, i_{k+1}$ are $k + 1$ arbitrary agents of $N.$ $\Box$

Return to Common Knowledge
