# reasoning-defeasible — suppl1（supplement）

> （《reasoning-defeasible》词条补充材料，源：plato.stanford.edu/entries/reasoning-defeasible/suppl1.html）

#### Supplement to Defeasible Reasoning

## John Pollock’s System

In defining what beliefs are warranted, given a directed graph representing a cognitive state, Pollock first defines a *partial status assignment* that assigns the statuses “defeated” or “undefeated” to some of the nodes of the graph.

An assignment $\sigma$ is a partial status assignment iff:

1. $\sigma$ assigns “undefeated” to all nodes that are such that neither they nor any of their ancestors are defeated by any nodes in the graph.
2. $\sigma$ assigns “undefeated” to $\alpha$ iff $\sigma$ assigns “undefeated” to all the immediate ancestors of $\alpha$, and all nodes defeating $\alpha$ are assigned “defeated”.
3. $\sigma$ assigns “defeated” to a node $\alpha$ iff either $\alpha$ has an immediate ancester that is assigned “defeated”, or there is a node $\beta$ that defeats $\alpha$ and that is assigned “undefeated”.

An assignment $\sigma$ is a *status assignment* iff $\sigma$ is a *maximal* partial status assignment. A node is *defeated outright* iff no status assignment assigns “undefeated” to it. If some status assignments assign “defeated” to it, and some assign “undefeated” to it, then it is *provisionally defeated*. A node is warranted if it is neither defeated outright nor provisionally defeated; that is, if every status assignment assigns “undefeated” to it. Here are some of the consequences of Pollock’s definitions:

- A node $\alpha$ is undefeated iff all its immediate ancestors are undefeated and all nodes defeating $\alpha$ are defeated.
- If some immediate ancestor of $\alpha$ is defeated outright, then $\alpha$ is defeated outright.
- If some node defeating $\alpha$ is undefeated, then $\alpha$ is defeated outright.
- If $\alpha$ is self-defeating, then $\alpha$ is defeated outright.
