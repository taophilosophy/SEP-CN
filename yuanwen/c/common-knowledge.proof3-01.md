# common-knowledge — proof3-01（supplement）

> （《common-knowledge》词条补充材料，源：plato.stanford.edu/entries/common-knowledge/proof3-01.html）

#### Supplement to Common Knowledge

## Proof of Proposition 3.1

**Proposition 3.1**. Let $\Omega$ be a finite set of states of the world. Suppose that

1. Agents i and j have a common prior probability distribution $\mu(\cdot)$ over the events of $\Omega$ such that $\mu(\omega) \gt 0$ for each $\omega \in \Omega$, and
2. It is common knowledge at *ω* that $i$’s posterior probability of event $E$ is $q_i(E)$ and that $j$’s posterior probability of $E$ is $q_j(E).$

Then $q_i(E) = q_j(E).$

**Proof.** Let $\mathcal{M}$ be the meet of all the agents’ partitions, and let $\mathcal{M}(\omega)$ be the element of $\mathcal{M}$ containing *ω*. Since $\mathcal{M}(\omega)$ consists of cells common to every agents information partition, we can write

$$ \mathcal{M}(\omega) = \bigcup_k H_{ik}, $$

where each $H_{ik} \in \mathcal{H}_i$. Since $i$’s posterior probability of event $E$ is common knowledge, it is constant on $\mathcal{M}(\omega),$ and so

$$ q_i(E) = \mu(E \mid H_{ik}) \text{ for all } k $$

Hence,

$$ \mu(E \cap H_{ik}) = q_i(E) \mu(H_{ik}) $$

and so

$$\begin{align} \mu(E \cap \mathcal{M}(\omega)) &= \mu(E \cap \bigcup_k H_{ik}) = \mu(\bigcup_k E \cap H_{ik}) \\ &= \sum_k \mu(E \cap H_{ik}) = \sum_k q_i(E) \mu(H_{ik}) \\ &= q_i(E) \sum_k \mu(H_{ik}) = q_i(E) \mu(\bigcup_k H_{ik}) \\ &= q_i(E) \mu(\mathcal{M}(\omega)) \end{align}$$

Applying the same argument to $j$, we have

$$ \mu(E \cap \mathcal{M}(\omega)) = q_j(E)\mu(\mathcal{M}(\omega)) $$

so we must have $q_i(E) = q_j(E).$ $\Box$

Return to Common Knowledge
