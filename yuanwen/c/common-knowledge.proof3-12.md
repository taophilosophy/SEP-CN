# common-knowledge — proof3-12（supplement）

> （《common-knowledge》词条补充材料，源：plato.stanford.edu/entries/common-knowledge/proof3-12.html）

#### Supplement to Common Knowledge

## Proof of Proposition 3.12

**Proposition 3.12** (Bicchieri 1993) In an extensive form game of perfect information, the agents follow the backwards induction solution if the following conditions are satisfied for each agent $i$ at each information set $I^{ik}$:

1. $i$ is rational, $i$ knows this and $i$ knows the game, and
2. At any information set $I^{jk+1}$ that immediately follows $I^{ik},$ $i$ knows at $I^{ik}$ what $j$ knows at $I^{jk+1}$.

**Proof.** The proof is by induction on $m$, the number of potential moves in the game. If $m = 1$, then at $I^{i1}$, by (a) agent $i$ chooses a strategy which yields $i$ her maximum payoff, and this is the backwards induction solution for a game with one move.

Now suppose the proposition holds for games having at most $m = r$ potential moves. Let $\Gamma$ be a game of perfect information with $r + 1$ potential moves, and suppose that $(\alpha)$ and $(\beta)$ are satisfied at every node of $\Gamma$. Let $I^{i1}$ be the information set corresponding to the root of the tree for $\Gamma$. At $I^{i1},$ $i$ knows that (a) and (b) obtain for each of the subgames that start at the information sets which immediately follow $I^{i1}$. Then $i$ knows that the outcome of play for each of these subgames is the backwards induction solution for that subgame. Hence, at $I^{i1}$, $i$’s payoff maximizing strategy is a branch of the tree starting from $I^{i1}$ which leads to a subgame whose backwards induction solution is best for $i$, and since $i$ is rational, $i$ chooses such a branch at $I^{i1}$. But this is the backwards induction solution for the entire game $\Gamma$, so the proposition is proved for $m = r + 1$.

Return to Common Knowledge
