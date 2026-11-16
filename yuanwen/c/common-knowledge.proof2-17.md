# common-knowledge — proof2-17（supplement）

> （《common-knowledge》词条补充材料，源：plato.stanford.edu/entries/common-knowledge/proof2-17.html）

#### Supplement to Common Knowledge

## Proof of Proposition 2.17

**Proposition 2.17** (Aumann 1976) Let $\mathcal{M}$ be the meet of the agents’ partitions $\mathcal{H}_i$ for each $i \in N$. A proposition $E \subseteq \Omega$ is common knowledge for the agents of $N$ at *ω* iff $\mathcal{M}(\omega) \subseteq E$. In Aumann (1976), $E$ is *defined* to be common knowledge at *ω* iff $\mathcal{M}(\omega) \subseteq E$.

**Proof**. $(\Leftarrow)$ By Lemma 2.16, $\mathcal{M}(\omega)$ is common knowledge at *ω*, so $E$ is common knowledge at *ω* by Proposition 2.4.

$(\Rightarrow)$ We must show that $\mathbf{K}^*_N (E)$ implies that $\mathcal{M}(\omega) \subseteq E$. Suppose that there exists $\omega' \in \mathcal{M}(\omega)$ such that $\omega' \not\in E.$ Since $\omega' \in \mathcal{M}(\omega), \omega'$ is reachable from *ω*, so there exists a sequence $0, 1, \ldots ,m-1$ with associated states $\omega_1, \omega_2 , \ldots ,\omega_m$ and information sets $\mathcal{H}_{i_{ k} }(\omega_k)$ such that $\omega_0 = \omega,$ $\omega_m = \omega',$ and $\omega_k \in \mathcal{H}_{i_k}(\omega_{k+1}).$ But at information set $\mathcal{H}_{i_{ k} }(\omega_m)$, agent $i_k$ does not know event $E$. Working backwards on $k$, we see that event $E$ cannot be common knowledge, that is, agent $i_1$ cannot rule out the possibility that agent $i_2$ thinks that … that agent $i_{m-1}$ thinks that agent $i_m$ does not know $E.$ $\Box$

Return to Common Knowledge
