# common-knowledge — proof2-04（supplement）

> （《common-knowledge》词条补充材料，源：plato.stanford.edu/entries/common-knowledge/proof2-04.html）

#### Supplement to Common Knowledge

## Proof of Proposition 2.4

**Proposition 2.4**. If $\omega \in \mathbf{K}^*_N (E)$ and $E \subseteq F$, then $\omega \in \mathbf{K}^*_N (F)$.

**Proof**. If $E \subseteq F$, then as we observed earlier, $\mathbf{K}_i (E) \subseteq \mathbf{K}_i (F)$, so

$$ \mathbf{K}^{1}_N (E) = \bigcap_{i\in N} \mathbf{K}_i (E) = \bigcap_{i\in N} \mathbf{K}_i (F) = \mathbf{K}^{1}_N (F) $$

If we now set $E' = \mathbf{K}^n_{N}(E)$ and $F' = \mathbf{K}^n_N(F),$ then by the argument just given we have

$$ \mathbf{K}^{n+1}_N(E) = \mathbf{K}^1_N(E') \subseteq \mathbf{K}^1_N(F') = \mathbf{K}^{n+1}_N(F) $$

so we have $m$ᵗʰ level mutual knowledge for every $n \ge 1$.

Hence

$$ \text{if } \omega \in \bigcap_{n=1}^{\infty} \mathbf{K}^n_N(E) \text{ then } \omega \in \bigcap_{n=1}^{\infty} \mathbf{K}^n_N(F). $$

$\Box$

Return to Common Knowledge
