# reasoning-defeasible — suppl1（supplement）

> （《reasoning-defeasible》词条补充材料，源：plato.stanford.edu/entries/reasoning-defeasible/suppl1.html）

#### Supplement to Defeasible Reasoning

## John Pollock’s System

In defining what beliefs are warranted, given a directed graph representing a cognitive state, Pollock first defines a *partial status assignment* that assigns the statuses “defeated” or “undefeated” to some of the nodes of the graph.

An assignment *σ* is a partial status assignment iff:

1. *σ* assigns “undefeated” to all nodes that are such that neither they nor any of their ancestors are defeated by any nodes in the graph.
2. *σ* assigns “undefeated” to *α* iff *σ* assigns “undefeated” to all the immediate ancestors of *α*, and all nodes defeating *α* are assigned “defeated”.
3. *σ* assigns “defeated” to a node *α* iff either *α* has an immediate ancester that is assigned “defeated”, or there is a node *β* that defeats *α* and that is assigned “undefeated”.

An assignment *σ* is a *status assignment* iff *σ* is a *maximal* partial status assignment. A node is *defeated outright* iff no status assignment assigns “undefeated” to it. If some status assignments assign “defeated” to it, and some assign “undefeated” to it, then it is *provisionally defeated*. A node is warranted if it is neither defeated outright nor provisionally defeated; that is, if every status assignment assigns “undefeated” to it. Here are some of the consequences of Pollock’s definitions:

- A node *α* is undefeated iff all its immediate ancestors are undefeated and all nodes defeating *α* are defeated.
- If some immediate ancestor of *α* is defeated outright, then *α* is defeated outright.
- If some node defeating *α* is undefeated, then *α* is defeated outright.
- If *α* is self-defeating, then *α* is defeated outright.
