# reasoning-defeasible — suppl2（supplement）

> （《reasoning-defeasible》词条补充材料，源：plato.stanford.edu/entries/reasoning-defeasible/suppl2.html）

#### Supplement to Defeasible Reasoning

## Semantic Inheritance Networks

A path is a sequence of links in a graph $G$, with the final node of each link being the initial node of the next, where all the links, with the possible exception of the last one, are positive. A *generalized* path is a sequence of links that can contain negative links anywhere, and more than one. Each path has both an initial node and a final node. A path can be taken as representing an assertion about an individual: that the individual corresponding to the initial node belongs to the category corresponding to the final node. The *degree* of a path is the length of the longest generalized path connecting the path’s initial node to its final node.

Horty, Thomason, and Touretzky define the relation of *support* between graphs (cognitive states) and paths (assertions) by mathematical induction on the degree of the path. Direct links (paths of length one) are always supported by the graph.

1. If *σ* is a positive path, $x \rightarrow \sigma^1 \rightarrow u \rightarrow y$, then $G$ supports *σ* iff:
2. $G$ supports path $x \rightarrow \sigma^1 \rightarrow u$.
3. $u \rightarrow y$ is a direct link in $G$.
4. The negative link $x \notrightarrow y$ does not belong to $G$.
5. for all $v, \tau$ such that $G$ supports $x \rightarrow \tau \rightarrow v$, with the negative link $v \notrightarrow y$ in $G$, there exist $z, \tau^1 , \tau^2$ such that $z \rightarrow y$ is in $G$, and either $z = x$, or $G$ supports the path $x \rightarrow \tau^1 \rightarrow z \rightarrow \tau^2 \rightarrow v$.
6. If *σ* is a negative path, $x \rightarrow \sigma^1 \rightarrow u \notrightarrow y$, then $G$ supports *σ* iff:
7. $G$ supports path $x \rightarrow \sigma^1 \rightarrow u$.
8. $u \notrightarrow y$ is a direct negative link in $G$.
9. The positive link $x \rightarrow y$ does not belong to $G$.
10. for all $v, \tau$ such that $G$ supports $x \rightarrow \tau \rightarrow v$, with the positive link $v \rightarrow y$ in $G$, there exist $z, \tau^1 , \tau^2$ such that $z \notrightarrow y$ is in $G$, and either $z = x$, or $G$ supports the path $x \rightarrow \tau^1 \rightarrow z \rightarrow \tau^2 \rightarrow v$.

The definition ensures that each potentially conflicting path be preempted by a path with a specificity-based priority.
