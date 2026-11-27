# qt-quantlog — supplement（supplement）

> （《qt-quantlog》词条补充材料，源：plato.stanford.edu/entries/qt-quantlog/supplement.html）

#### Supplement to Quantum Logic and Probability Theory

## The Basic Theory of Ordering Relations

What follows is the briefest possible summary of the order-theoretic notions used in the main text. For a good introduction to this material, see Davey & Priestley (1990). More advanced treatments can be found in Grätzer (1998) and Birkhoff (1967).

- 1. Ordered Sets
- 2. Lattices
- 3. Ortholattices
- 4. Orthomodularity
- 5. Closure Operators, Interior Operators and Adjunctions

### 1. Ordered Sets

A *partial ordering*—henceforth, just an ordering—on a set $P$ is a reflexive, anti-symmetric, and transitive binary relation $\unlhd$ on $P$. Thus, for all $p, q, r \in P$, we have

1. $p \unlhd p$
2. $p \unlhd q$ and $q \unlhd p$ only if $p = q$.
3. if $p \unlhd q$ and $q \unlhd r$ then $p \unlhd r$

If $p \unlhd q$, we speak of $p$ as being *less than*, or *below* $q$, and of $q$ as being *greater than*, or *above* $p$, in the ordering.

A *partially ordered set*, or *poset*, is a pair $(P, \unlhd)$ where $P$ is a set and $\unlhd$ is a specified ordering on $P$. It is usual to let $P$ denote both the set and the structure, leaving $\unlhd$ tacit wherever possible. Any collection of subsets of some fixed set $X$, ordered by set-inclusion, is a poset; in particular, the full power set $\wp(X)$ is a poset under set inclusion.

Let $P$ be a poset. The *meet*, or *greatest lower bound*, of $p, q \in P$, denoted by $p\wedge q$, is the greatest element of $P$—if there is one—lying below both $p$ and $q$. The *join*, or *least upper bound*, of $p$ and $q$, denoted by $p\vee q$, is the least element of $P$—if there is one—lying above both $p$ and $q$. Thus, for any elements $p, q, r$ of $P$, we have

1. if $r \unlhd p\wedge q$, then $r \unlhd p$ and $r \unlhd q$
2. if $p\vee q \unlhd r$, then $p \unlhd r$ and $q \unlhd r$

Note that $p\wedge p = p\vee p = p$ for all $p$ in $P$. Note also that $p \unlhd q$ iff $p\wedge q = p$ iff $p\vee q = q$.

Note that if the set $P = \wp(X)$, ordered by set-inclusion, then $p\wedge q = p\cap q$ and $p\vee q = p\cup q$. However, if $P$ is an arbitrary collection of subsets of $X$ ordered by inclusion, this need not be true. For instance, consider the collection $P$ of all subsets of $X = \{1,2,\ldots ,n\}$ having even cardinality. Then, for instance, $\{1,2\}\vee \{2,3\}$ does not exist in $P$, since there is no *smallest* set of 4 elements of $X$ containing $\{1,2,3\}$. For a different sort of example, let $X$ be a vector space and let $P$ be the set of *subspaces* of $X$. For subspaces $\mathbf{M}$ and $\mathbf{N}$, we have

$$\mathbf{M}\wedge \mathbf{N} = \mathbf{M}\cap \mathbf{N}, \textrm{ but } \mathbf{M}\vee \mathbf{N} = \textrm{span} (\mathbf{M}\cup \mathbf{N}).$$

The concepts of meet and join extend to infinite subsets of a poset $P$. Thus, if $A\subseteq P$, the meet of $A$ is the largest element (if any) below $A$, while the join of $A$ is the least element (if any) above $A$. We denote the meet of $A$ by $\wedge\, A$ or by $\wedge_{a\in A}\, a$. Similarly, the join of $A$ is denoted by $\vee\, A$ or by $\vee_{a\in A}\, a$.

### 2. Lattices

A *lattice* is a poset $(L, \unlhd)$ in which every pair of elements has both a meet and a join. A *complete lattice* is one in which *every* subset of $L$ has a meet and a join. Note that $\wp(X)$ is a complete lattice with respect to set inclusion, as is the set of all subspaces of a vector space. The set of finite subsets of an infinite set $X$ is a lattice, but not a complete lattice. The set of subsets of a finite set having an even number of elements is an example of a poset that is not a lattice.

A lattice $(L, \unlhd)$ is *distributive* iff meets distribute over joins and vice versa:

$$p \wedge (q\vee r) = (p\wedge q) \vee (p\wedge r),$$

and

$$p \vee (q\wedge r) = (p\vee q) \wedge (p\vee r)$$

The power set lattice $\wp(X)$, for instance, is distributive (as is any lattice of sets in which meet and join are given by set-theoretic intersection and union). On the other hand, the lattice of subspaces of a vector space is not distributive, for reasons that will become clear in a moment.

A lattice $L$ is said to be bounded iff it contains a smallest element 0 and a largest element 1. Note that any complete lattice is automatically bounded. For the balance of this appendix, *all lattices are assumed to be bounded*, absent any indication to the contrary.

A *complement* for an element $p$ of a (bounded) lattice $L$ is another element $q$ such that $p \wedge q = 0$ and $p \vee q = 1$.

In the lattice $\wp(X)$, every element has exactly one complement, namely, its usual set-theoretic complement. On the other hand, in the lattice of subspaces of a vector space, an element will typically have infinitely many complements. For instance, if $L$ is the lattice of subspaces of 3-dimensional Euclidean space, then a complement for a given plane through the origin is provided by any line through the origin not lying in that plane.

**Proposition**: If $L$ is distributive, an element of $L$ can have at most one complement.

**Proof**: Suppose that $q$ and $r$ both serve as complements for $p$. Then, since $L$ is distributive, we have

$$ \begin{align} q & = q \wedge 1 \\ & = q \wedge (p \vee r)\\ & = (q\wedge p) \vee (q\wedge r)\\ & = 0 \vee (q\wedge r)\\ & = q\wedge r\\ \end{align} $$

Hence, $q \unlhd r$. Symmetrically, we have $r \unlhd q$; thus, $q = r$.

Thus, no lattice in which elements have multiple complements is distributive. In particular, the subspace lattice of a vector space (of dimension greater than 1) is not distributive.

If a lattice $is$ distributive, it may be that some of its elements have a complement, while others lack a complement. A distributive lattice in which every element has a complement is called a *Boolean lattice* or a *Boolean algebra.* The basic example, of course, is the power set $\wp(X)$ of a set $X$. More generally, any collection of subsets of $X$ closed under unions, intersections and complements is a Boolean algebra; a theorem of Stone and Birkhoff tells us that, up to isomorphism, every Boolean algebra arises in this way.

### 3. Ortholattices

In some non-uniquely complemented (hence, non-distributive) lattices, it is possible to pick out, for each element $p$, a preferred complement $p'$ in such a way that

1. if $p \unlhd q$ then $q' \unlhd p'$
2. $p'' = p$

When these conditions are satisfied, one calls the mapping $p\rightarrow p'$ an *orthocomplementation* on $L$, and the structure $(L, \unlhd ,')$ an *orthocomplemented lattice*, or an *ortholattice* for short.

Note again that if a distributive lattice can be orthocomplemented at all, it is a Boolean algebra, and hence can be orthocomplemented in only one way. In the case of $L(\mathbf{H})$ the orthocomplementation one has in mind is $\mathbf{M} \rightarrow \mathbf{M}^{\bot}$ where $\mathbf{M}^{\bot}$ is defined as in Section 1 of the main text. More generally, if $\mathbf{V}$ is any inner product space (complete or not), let $L(\mathbf{V})$ denote the set of subspaces $\mathbf{M}$ of $\mathbf{V}$ such that $\mathbf{M} = \mathbf{M}^{\bot \bot}$ (such a subspace is said to be algebraically closed). This again is a complete lattice, orthocomplemented by the mapping $\mathbf{M} \rightarrow \mathbf{M}^{\bot}$.

### 4. Orthomodularity

There is a striking order-theoretic characterization of the lattice of closed subspaces of a Hilbert space among lattices $L(\mathbf{V})$ of closed subspaces of more general inner product spaces. An ortholattice $L$ is said to be orthomodular iff, for any pair $p, q$ in $L$ with $p \unlhd q$,

$$ \tag{OMI} (q\wedge p')\vee p = q. $$

Note that this is a weakening of the distributive law. Hence, a Boolean lattice is orthomodular. It is not difficult to show that if $\mathbf{H}$ is a Hilbert space, then $L(\mathbf{H})$ is orthomodular. The striking converse of this fact is due to Amemiya and Araki (1966):

**Theorem**: Let $\mathbf{V}$ be an inner product space (over $\mathbf{R}, \mathbf{C}$ or the quaternions) such that $L(\mathbf{V})$ is orthomodular. Then $\mathbf{V}$ is complete, i.e., a Hilbert space.

### 5. Closure Operators, Interior Operators and Adjunctions

Let $P$ and $Q$ be posets. A mapping $f : P \rightarrow Q$ is *order preserving* iff for all $p,q \in P$, if $p \unlhd q$ then $f(p) \unlhd f(q)$.

A *closure* *operator* on a poset $P$ is an order-preserving map $\mathbf{cl} : P \rightarrow P$ such that for all $p \in P$,

- $\mathbf{cl}(\mathbf{cl}(p)) = \mathbf{cl}(p)$
- $p \unlhd \mathbf{cl}(p)$.

Dually, an *interior operator* on $P$ is an order-preserving mapping $\mathbf{int} : P \rightarrow P$ on $P$ such that for all $p \in P$,

- $\mathbf{int}(\mathbf{int}(p)) = \mathbf{int}(p)$
- $\mathbf{int}(p) \unlhd p$

Elements in the range of $\mathbf{cl}$ are said to be *closed*; those in the range of $\mathbf{int}$ are said to be *open*. If $P$ is a (complete) lattice, then the set of closed, respectively open, subsets of $P$ under a closure or interior mapping is again a (complete) lattice.

By way of illustration, suppose that $\mathcal{O}$ and $\mathcal{C}$ are collections of subsets of a set $X$ with $\mathcal{O}$ closed under arbitrary unions and $\mathcal{C}$ under arbitrary intersections. For any set $A \subseteq X$, let

$$ \begin{align} \mathbf{cl}(A) & = \cap \{C\in \mathcal{C} \mid A \subseteq C\}, \textrm{ and}\\ \mathbf{int}(A) & = \cup \{O\in \mathcal{O} \mid O \subseteq A\} \end{align} $$

Then $\mathbf{cl}$ and $\mathbf{int}$ are interior operators on $\wp(X)$, for which the closed and open sets are precisely $\mathcal{C}$ and $\mathcal{O}$, respectively. The most familiar example, of course, is that in which $\mathcal{O}, \mathcal{C}$ are the open and closed subsets, respectively, of a topological space. Another important special case is that in which $\mathcal{C}$ is the set of linear subspaces of a vector space $\mathbf{V}$; in this case, the mapping *span* :$ \wp(\mathbf{V}) \rightarrow \wp(\mathbf{V})$ sending each subset of $\mathbf{V}$ to its span is a corresponding closure.

An *adjunction* between two posets $P$ and $Q$ is an ordered pair $(f, g)$ of mappings $f : P \rightarrow Q$ and $g : Q \rightarrow P$ connected by the condition that, for all $p \in P, q \in Q$

$$ f(p) \unlhd q \textrm{ if and only if } p \unlhd g(q). $$

In this case, we call $f$ a *left adjoint* for $g$, and call $g$ a *right adjoint* for $f$. Two basic facts about adjunctions, both easily proved, are the following:

**Proposition**: Let $f : L \rightarrow M$ be an order-preserving map between complete lattices $L$ and $M$. Then

1. $f$ preserves arbitrary joins if and only if it has a right adjoint.
2. $f$ preserves arbitrary meets if and only if it has a left adjoint.

**Proposition**: Let $(f, g)$ be an adjunction between complete lattices $L$ and $M$. Then

1. $g \circ f : L \rightarrow L$ is a closure operator.
2. $f \circ g : M \rightarrow M$ is an interior operator.

Return to Quantum Logic and Quantum Probability
