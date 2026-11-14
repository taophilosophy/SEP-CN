# logics-for-games — figdesc（supplement）

> （《logics-for-games》词条补充材料，源：plato.stanford.edu/entries/logics-for-games/figdesc.html）

#### Supplement to Logics for Analyzing Games

## Long descriptions for some figures in Logics for Analyzing Games

Most of these figures are tree diagrams made up of a root node connected with links to child nodes and they in turn to their child nodes. The following terminology is used:

- **link** means a connector of some sort between two nodes. Unless otherwise specified the link is a plain line. Links may be specified as dashed, dotted, or bold
- **parent node** is the node that the current node is immediately descended from.
- **child nodes** are the nodes that the current node is parent of. Children are always linked to their parents.
- **root node** is the first node of the tree from which all others are descended.
- **leaf node** is a node with no children.
- **sibling nodes** are nodes that share a common parent. Some trees have links between sibling nodes.
- **tier** refers to nodes that are at the same level (visually) from the root node. Tier 1 contains the root node. In a few cases a child node may be more than one tier below its parent.

Each tree is described in a nested list from top (the root node) to bottom (leaf nodes) and from left to right (e.g., a parent node is described then its children nodes, in a sublist, from left to right).

### Figure 1 description

(terminology intro)

This is a fairly simple tree diagram of players and choices. A bold link indicates the choice made by the parent player.

- Player *A*
- $1,0$ (left choice, bold link to parent)
- Player *E*
- $0,3$ (left choice, bold link to parent)
- $2,2$ (right choice)

### Figure 2 description

(terminology intro)

A three tier tree

- Player *A*
- Player *E* (link label is Left)
- $\win_A$ (link label is left)
- $\win_E$ (link label is right)
- Player *E* (link label is Right)
- $\win_E$ (link label is left)
- $\win_A$ (link label is right)

### Figure 3 description

(terminology intro)

A three tier tree

- Player *A*
- Player *E* (link label is ‘*a*’)
- $O_1$ (link label is ‘*c*’)
- $O_2$ (link label is ‘*d*’)
- Player *E* (link label is ‘*b*’)
- $O_3$ (link label is ‘*c*’)
- $O_4$ (link label is ‘*d*’)

### Figure 4 description

(terminology intro)

Two trees each with three tiers. The first tree

- Player *A*
- *p*
- Player *E*
- *q*
- *r*

The second tree

- Player *E*
- Player *A*
- *p*
- *q*
- Player *A*
- *p*
- *r*

### Figure 5 description

(terminology intro)

Two trees each with three tiers and with dashed lines linking the second tier nodes in both trees with the same children (two distinct sets). Both sets are labeled ‘*Z*’ in the actual diagram, but, in the description below one set will be marked as Z1 and the other as Z2. For the first tree.

- Player *A*
- Player *E* (link label is *a*, this is part of the Z1 set)
- $O_1$ (link label is *e*)
- $O_2$ (link label is *d*)
- Player *E* (link label is *b*, this is part of the Z2 set)
- $O_3$ (link label is *f*)
- $O_4$ (link label is *g*)
- Player *E* (link label is *c*, this is part of the Z2 set)
- $O_3$ (link label is *f*)
- $O_4$ (link label is *g*)

For the second tree.

- Player *A*
- Player *E* (link label is *a*, this is part of the Z1 set)
- $O_1$ (link label is *e*)
- $O_2$ (link label is *d*)
- Player *E* (link label is *b*, this is part of the Z2 set)
- $O_3$ (link label is *f*)
- $O_4$ (link label is *g*)

### Figure 6 description

(terminology intro)

A three tier tree. The second tier nodes have no text associated with them.

- root *r*
- unlabeled node (link back is labeled $R_A$)
- $\win_E$ (link back is labeled $R_E$)
- $\win_A$ (link back is labeled $R_E$)
- unlabeled node (link back is labeled $R_A$)
- $\win_A$ (link back is labeled $R_E$)
- $\win_E$ (link back is labeled $R_E$)

### Figure 7 description

(terminology intro)

A three tier tree

- Player *A*
- Player *E* (link back is labeled $\move_A$)
- *p* (link back is labeled $\move_E$)
- *p* (link back is labeled $\move_E$)
- Player *E* (link back is labeled $\move_A$)
- $p,q$ (link back is labeled $\move_E$)
- *q* (link back is labeled $\move_E$)

### Figure 8 description

(terminology intro)

A three tier tree

- Player *A*
- Player *E* (link back is labeled *a*)
- $O_1$ (link back is labeled *d*, between this and its sibling node $O_2$ is the expression $\substack{\prec_A\\\succ_E}$)
- $O_2$ (link back is labeled *c*, besides the expression between here and sibling node $O_2$ there is between here and same tier node $O_3$ another expression $\substack{\prec_A\\\succ_E}$)
- Player *E* (link back is labeled *b*)
- $O_3$ (link back is labeled *e*, besides the expression between here and same tier node $O_2$ there is between this and its sibling node $O_4$ the expression $\substack{\prec_A\\\approx_E}$)
- $O_4$ (link back is labeled *c*, note expression previously described between here and $O_3$)

### Figure 9 description

(terminology intro)

A three tier tree, some of the links are bold.

- Player *A*
- Player *E*
- $O_1$ (link back is bold and labeled $\best_E$, between this and its sibling node $O_2$ is the expression $\substack{\prec_A\\\approx_E}$)
- $O_2$ (link back is bold and labeled $\best_E$, besides the expression between here and sibling node $O_2$ there is between here and same tier node $O_3$ another expression $\substack{\prec_A\\\succ_E}$)
- Player *E* (link back is bold and labeled $\best_A$)
- $O_3$ (link back is bold and labeled $\best_E$, besides the expression between here and same tier node $O_2$ there is between this and its sibling node $O_4$ the expression $\substack{\prec_A\\\succ_E}$)
- $O_4$ (note expression previously described between here and $O_3$)

### Figure 10 description

(terminology intro)

A three tier tree

- Player *E*
- $m'$ (with a label of *A*; link back has a label of $h_L$; a dashed line labeled *A* links to its sibling node described later)
- $\win_A$ (link back is labeled $p_L$)
- $\win_E$ (link back is labeled $p_R$)
- $m$ (with a label of *A*; link back has a label of $h_R$; a dashed line labeled *A* links to its sibling node described earlier)
- $\win_E$ (link back is labeled $p_L$)
- $\win_A$ (link back is labeled $p_R$)

### Figure 11 description

(terminology intro)

A four tier tree. Note that Players are labeled with capital letters but that most of the links are using lowercase letters.

- Player *E*
- $m'$ (labeled with a capital *A*; link back is labeled with lowercase *a*; a dashed line labeled with a capital *A* links to its tier 2 sibling node described later)
- $\win_E$ (this is on tier 4 not 3)
- *n* (this is on tier 3; labeled with a capital *A*; a dashed line labeled with a capital *E* links to another tier 3 node described later)
- $\win_E$ (link back is labeled lowercase *c*)
- $\win_A$ (link back is labeled lowercase *d*)
- *m* (labeled with a capital *A*; link back is labeled with lowercase *b*; a dashed line labeled with a capital *A* links to its tier 2 sibling node described earlier)
- $n'$ (labeled with a capital *E*; a dashed line labeled with a capital *E* links to another tier 3 node described earlier)
- $\win_A$ (link back is labeled lowercase *c*)
- $\win_E$ (link back is labeled lowercase *d*)
- $\win_A$ (this is on tier 4 not 3)

### Figure 12 description

(terminology intro)

A four tier tree. Note that capital letters *A* and *E* refer to players.

- Nature
- *v* (labeled with a capital A; a dashed line labeled with a capital *A* links to its sibling node on tier 2 described later)
- Player *E* (link back is labeled *f*)
- $O_1$ (link back is labeled *c*)
- $O_2$ (link back is labeled *d*)
- Player *E* (link back is labeled *g*)
- $O_3$ (link back is labeled *c*; $\prec_E$ is between it and its sibling node described next)
- $O_4$ (link back is labeled *d*; $\prec_E$ is between it and its sibling node described previously)
- *w* (labeled with a capital A; a dashed line labeled with a capital *A* links to its sibling node on tier 2 described earlier)
- Player *E* (link back is labeled *f*)
- $O_5$ (link back is labeled *e*)
- $O_1$ (link back is labeled *c*)
- $O_2$ (link back is labeled *d*)
- Player *E* (link back is labeled *g*)
- $O_3$ (link back is labeled *c*; $\succ_E$ is between it and its sibling node described next)
- $O_4$ (link back is labeled *d*; $\succ_E$ is between it and its sibling node described previously)

### Figure 13 description

(terminology intro)

This is similar to figure 12 except that the root node of that tree (Nature) is dropped (hence two trees of three tiers instead of one of four tiers).

First tree

- *v* (labeled with a capital A; a dashed line labeled with a capital *A* links this root node to the other tree's root node described later)
- Player *E* (link back is labeled *f*)
- $O_1$ (link back is labeled *c*
- $O_2$ (link back is labeled *d*)
- Player *E* (link back is labeled *g*)
- $O_3$ (link back is labeled *c*; $\prec_E$ is between it and its sibling node described next)
- $O_4$ (link back is labeled *d*; $\prec_E$ is between it and its sibling node described previously)

Second tree

- *w* (labeled with a capital A; a dashed line labeled with a capital *A* links this root node to the other tree's root node described earlier)
- Player *E* (link back is labeled *f*)
- $O_5$ (link back is labeled *e*)
- $O_1$ (link back is labeled *c*)
- $O_2$ (link back is labeled *d*)
- Player *E* (link back is labeled *g*)
- $O_3$ (link back is labeled *c*; $\succ_E$ is between it and its sibling node described next)
- $O_4$ (link back is labeled *d*; $\succ_E$ is between it and its sibling node described previously)

### Figure 14 description

(terminology intro)

Similar to Figure 13 with the most notable exceptions being that the dashed line linking the two root nodes is labeled with $\leq_A$ above and $\geq_E$ below.

First tree

- *v* (labeled with a capital A)
- Player *E* (link back is labeled *a*)
- $O_1$ (link back is labeled *c*)
- $O_2$ (link back is labeled *d*)
- Player *E* (link back is labeled *b*)
- $O_3$ (link back is labeled *c*; $\prec_E$ is between it and its sibling node described next)
- $O_4$ (link back is labeled *d*; $\prec_E$ is between it and its sibling node described previously)

Second tree

- *w* (labeled with a capital A)
- Player *E* (link back is labeled *a*)
- $O_5$ (link back is labeled *e*)
- $O_1$ (link back is labeled *c*)
- $O_2$ (link back is labeled *d*)
- Player *E* (link back is labeled *b*)
- $O_3$ (link back is labeled *c*; $\succ_E$ is between it and its sibling node described next)
- $O_4$ (link back is labeled *d*; $\succ_E$ is between it and its sibling node described previously)

### Figure 15 description

(terminology intro)

This has three trees

The first tree has three tiers

- Player *A*
- $1,0$ (the link back is bold)
- Player *E*
- $0,3$ (the link back is bold)
- $2,2$

The second tree is similar to the first except that the leaf node, $2,2$, is dropped.

- Player *A*
- $1,0$ (the link back is bold)
- Player *E*
- $0,3$ (the link back is bold)

The third tree is similar to the first except that the node, Player *E*, and all its children are dropped.

- Player *A*
- $1,0$ (the link back is bold)

### Figure 16 description

(terminology intro)

Three similar trees each of three tiers. Below each tree is a fourth tier which contains an expression.

All three trees are identical to the first tree of figure 15 except for the fourth tier expression.

- Player *A*
- $1,0$ (the link back is bold; below this node in the fourth tier is the variable *x*)
- Player *E*
- $0,3$ (the link back is bold; below this node in the fourth tier is the variable *y*)
- $2,2$ (below this node in the fourth tier is the variable *z*)

The expression in the first tree for the fourth tier is $x \mathbin{\approx_{A,E}} y \mathbin{\approx_{A,E}} z$

The expression in the second tree for the fourth tier is $x \mathbin{\approx_{A,E}} y \mathbin{>_{A,E}} z$

The expression in the third tree for the fourth tier is $x \mathbin{>_{A,E}} y \mathbin{>_{A,E}} z$

### Figure 17 description

(terminology intro)

This is a three tier tree.

- Player *A*
- $(1,1)$ (this is on the third tier; the link back is labeled with a capitalized ‘Left’)
- Player *E* (the link back is labeled with a capitalized ‘Right’)
- $(1,1)$ (the link back is labeled with a lowercase ‘left’)
- $(2,1)$ (the link back is labeled with a lowercase ‘right’)

### Figure 18 description

(terminology intro)

This figure has two parts: Game Structure and Event Model

The Game Structure is a three tier tree with all nodes enclosed in circles.

- Player *A*
- Player *E* (link back is labeled *a*)
- empty circle (link back is labeled *d*)
- empty circle (link back is labeled *e*)
- Player *E* (link back is labeled *b*)
- empty circle (link back is labeled *e*)
- empty circle (link back is labeled *f*)
- Player *E* (link back is labeled *c*)
- empty circle (link back is labeled *f*)

Event Model has two sections each with a title and a diagram.

The first is titled “Moves for Player *A*” and the diagram is of the letters *a*, *b*, and *c* equidistant in a row with *a* and *b* linked with a dashed line labeled with a capital *E*.

The second is titled “Moves for Player *E*” and the diagram is of the letters *d*, *e*, and *f* equidistant in a row with *d* and *e* linked with a dashed line labeled with a capital *A*.

### Figure 19 description

(terminology intro)

This figure has three levels each with a title and a diagram

- first is titled “tree level 1” and the diagram is a single empty circle
- second is titled “tree level 2” and the diagram is three empty circles equidistant apart in a row. The first and second circles are connected by a dashed line labeled *E*
- third is titled “tree level 3” and the diagram is five empty circles in a row. The first and second are connected by a dashed line labeled *A*. The second and third by a dashed line labeled *E*.

### Figure 20 description

(terminology intro)

A three tiered tree very similar to the Game Structure tree in figure 18. All nodes are enclosed in circles.

- Player *A*
- Player *E* (link back is labeled *a*; a dashed line labeled *E* connects to its first sibling described later)
- empty circle (link back is labeled *d*; a dashed line labeled *A* connects to its sibling node described next)
- empty circle (link back is labeled *e*; ; a dashed line labeled *A* connects to its sibling node described previously; in addition a dashed line labeled *E* connects to a node in the same tier described later)
- Player *E* (link back is labeled *b*; a dashed line labeled *E* connects to its first sibling described earlier)
- empty circle (link back is labeled *e*; a dashed line labeled *E* connects to a node in the same tier described earlier)
- empty circle (link back is labeled *f*)
- Player *E* (link back is labeled *c*)
- empty circle (link back is labeled *f*)

### Figure 21 description

(terminology intro)

A tree diagram consisting of only lines but no text. The root node has three children of which the first and last have no children. The middle child has two children of which the first has no children; the second child is marked by a large dot and has three children with no children.

### Figure 22 description

(terminology intro)

A tree diagram of three tiers

- Player *A*
- $3,0$ (link back is bold and labeled with a capitalized “Left”
- Player *E* (link back is labeled with a capitalized “Right”
- $0,2$ (link back is bold and labeled with a lowercase “left”
- This node is a table

  |   | *E* |   |
  | --- | --- | --- |
  | *A* | $4,4$ | $1,0$ |
  | $1,0$ | $2,2$ |   |

  (the link back is labeled “right”)

### Figure 23 description

(terminology intro)

A three tier tree diagram though dissimilar from the previous ones being horizontal rather than verticall. Also all links are arrows going from parent to child unless otherwise stated

- $t_0$
- $t_1^{''}$
- $t_2^{'''}$ (two dotted lines descend from this node)
- $t_1^{'}$
- $t_2^{''}$ (one dotted lines descends from this node)
- $t_2^{'}$ (one dotted lines descends from this node)
- $t_1$
- $t_2$ (one dotted line descends from this node)

### Figure 24 description

(terminology intro)

A diagram consisting of the names of five cities which are connected by train, plane, or taxi.

- Luxembourg visually is in the center with the other four cities forming a ring around it. It is connected to all of the other five cities in the following ways
- to Amersterdam by train and plane
- to Koblenz by train
- to Saarbruecken by train and taxi
- to Brussels by train
- the other cities are connected each to only two other cities other than Luxembourg (the previous and next in the ring)
- Amsterdam to Brussels by train and plane
- Brussels to Saarbruecken by plane
- Saarbruecken to Koblenz by train
- Koblenz to Amsterdam by train
