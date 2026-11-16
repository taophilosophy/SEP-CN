# common-knowledge — proof3-11（supplement）

> （《common-knowledge》词条补充材料，源：plato.stanford.edu/entries/common-knowledge/proof3-11.html）

#### Supplement to Common Knowledge

## Proof of Proposition 3.11

**Proposition 3.11** (Aumann 1987) If each agent $i \in$ N is *ω*-Bayes rational at each possible world $\omega \in \Omega$, then the agents are following an Aumann correlated equilibrium. If the CPA is satisfied, then the correlated equilibrium is objective.

**Proof.** We must show that $s : \Omega \rightarrow S$ as defined by the $\mathcal{H}_i$-measurable $s_i$’s of the Bayesian rational agents is an objective Aumann correlated equilibrium. Let $i \in n$ and $\omega \in \Omega$ be given, and let $g_i : \Omega \rightarrow S_i$ be any function that is a function of $s_i$. Since $s_i$ is constant over each cell of $\mathcal{H}_i, g_i$ must be as well, that is, $g_i$ is $\mathcal{H}_i$-measurable. By Bayesian rationality,

$$ E(u_i \circ s \mid \mathcal{H}_i)(\omega) \ge E(u_i (g_i,s_{-i}) \mid \mathcal{H}_i)(\omega) $$

Since *ω* was chosen arbitrarily, we can take iterated expectations to get

$$ E(E(u_i \circ s \mid \mathcal{H}_i)(\omega)) \ge E(E(u_i (g_i,s_{-i}) \mid \mathcal{H}_i)(\omega)) $$

which implies that

$$ E(u_i \circ s) \ge E(u_i (g_i,s_{-i})) $$

so $s$ is an Aumann correlated equilibrium.

Return to Common Knowledge
