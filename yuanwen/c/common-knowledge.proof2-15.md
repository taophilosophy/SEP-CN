# common-knowledge — proof2-15（supplement）

> （《common-knowledge》词条补充材料，源：plato.stanford.edu/entries/common-knowledge/proof2-15.html）

#### Supplement to Common Knowledge

## Proof of Lemma 2.15

**Lemma 2.15**. $\omega' \in \mathcal{M}(\omega)$ iff $\omega '$ is reachable from *ω*.

**Proof**. Pick an arbitrary world $\omega \in \Omega$, and let

$$ \mathcal{R}(\omega) = \bigcup_{n=1}^{\infty} \bigcup_{i_1,i_2 ,\ldots ,i_n \in N} \mathcal{H}_{i_n}(\ldots(\mathcal{H}_{i_2}(\mathcal{H}_{i_1}(\omega))\ldots) $$

that is, $\mathcal{R}(\omega)$ is the set of all worlds that are reachable from *ω*. Clearly, for each $i \in N,$ $\mathcal{H}_i (\omega) \subseteq \mathcal{R}(\omega)$, which shows that $\mathcal{R}$ is a coarsening of the partitions $\mathcal{H}_i,$ $i \in N$. Hence $\mathcal{M}(\omega) \subseteq \mathcal{R}(\omega)$, as $\mathcal{M}$ is the finest common coarsening of the $\mathcal{H}_i$’s.

We need to show that $\mathcal{R}(\omega) \subseteq \mathcal{M}(\omega)$ to complete the proof. To do this, it suffices to show that for any sequence $i_1, i_2 , \ldots ,i_n \in N$

$$\tag{1} \mathcal{H}_{i_n}(\ldots(\mathcal{H}_{i_2} (\mathcal{H}_{i_1}(\omega))\ldots) $$

We will prove (1) by induction on $n$. By definition, $\mathcal{H}_i (\omega) \subseteq \mathcal{M}(\omega)$ for each $i \in N,$ proving (1) for $n = 1$. Suppose now that (1) obtains for $n = k$, and for a given $i \in N$, let $\omega^* \in \mathcal{H}_i(A)$ where $A = \mathcal{H}_{i_k} (\ldots(\mathcal{H}_{i_2} (\mathcal{H}_{i_1}(\omega)))$. By induction hypothesis, $A \subseteq \mathcal{M}(\omega)$. Since $\mathcal{H}_i (A)$ states that $i_1$ thinks that $i_2$ thinks that $\ldots i_k$ thinks that $i$ thinks that $\omega^*$ is possible, $A$ and $\mathcal{H}_i (\omega^*)$ must overlap, that is, $\mathcal{H}_i (\omega^*) \cap A \ne \varnothing$. If $\omega^* \not\in \mathcal{M}(\omega),$ then $\mathcal{H}_i (\omega^*) \not\subseteq \mathcal{M}(\omega)$, which implies that $\mathcal{M}$ is not a common coarsening of the $\mathcal{H}_i$’s, a contradiction. Hence $\omega^* \in \mathcal{M}(\omega)$, and since $i$ was chosen arbitrarily from $N$, this shows that (1) obtains for $n = k + 1.$ $\Box$

Return to Common Knowledge
