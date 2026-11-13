# The Axiom of Choice
**First published Tue Jan 8, 2008; substantive revision Fri Dec 10, 2021**

*Bell, John L.*

The principle of set theory known as the *Axiom of Choice* has been hailed as “probably the most interesting and, in spite of its late appearance, the most discussed axiom of mathematics, second only to Euclid’s axiom of parallels which was introduced more than two thousand years ago” (Fraenkel, Bar-Hillel & Levy 1973, §II.4)[^fraenkel-1973]. The fulsomeness of this description might lead those unfamiliar with the axiom to expect it to be as startling as, say, the Principle of the Constancy of the Velocity of Light or the Heisenberg Uncertainty Principle. But in fact the Axiom of Choice as it is usually stated appears humdrum, even self-evident. For it amounts to nothing more than the claim that, given any collection of mutually disjoint nonempty sets, it is possible to assemble a new set—a *transversal* or *choice set*—containing exactly one element from each member of the given collection. Nevertheless, this seemingly innocuous principle has far-reaching mathematical consequences—many indispensable, some startling—and has come to figure prominently in discussions on the foundations of mathematics. It (or its equivalents) have been employed in countless mathematical papers, and a number of monographs have been exclusively devoted to it.

## 1. Origins and Chronology of the Axiom of Choice

In 1904 Ernst Zermelo formulated the Axiom of Choice (abbreviated as *AC* throughout this article) in terms of what he called *coverings* (Zermelo 1904)[^zermelo-1904]. He starts with an arbitrary set $M$ and uses the symbol $M'$ to denote an arbitrary nonempty subset of $M$, the collection of which he denotes by M. He continues:

> Imagine that with every subset $M'$ there is associated an arbitrary element $m_{1}'$, that occurs in $M'$ itself; let $m_{1}'$ be called the “distinguished” element of $M'$. This yields a “covering” $g$ of the set $M$ by certain elements of the set $M$. The number of these coverings is equal to the product [of the cardinalities of all the subsets $M'$] and is certainly different from 0.

The last sentence of this quotation—which asserts, in effect, that coverings always exist for the collection of nonempty subsets of any (nonempty) set—is Zermelo’s first formulation of the Axiom of Choice[^note-1]. This is now usually stated in terms of *choice functions*: here a choice function on a collection $\sH$ of nonempty sets is a map $f$ with domain $\sH$ such that $f(X) \in X$ for every $X \in \sH$.

As a very simple example, let $\sH$ be the collection of nonempty subsets of $\{0, 1\}$, i.e., $\sH = \{\{0\}, \{1\}, \{0,1\}\}$. Then $\sH$ has the two distinct choice functions $f_{1}$ and $f_{2}$ given by:

\begin{align} f_{1}(\{0\}) &= 0 \\ f_{1}(\{1\}) &= 1 \\ f_{1}(\{0, 1\}) &= 0 \\ f_{2}(\{0\}) &= 0 \\ f_{2}(\{1\}) &= 1 \\ f_{2}(\{0, 1\}) &= 1 \end{align}

A more interesting example of a choice function is provided by taking $\sH$ to be the set of (unordered) pairs of real numbers and the function to be that assigning to each pair its least element. A different choice function is obtained by assigning to each pair its greatest element. Clearly many more choice functions on $\sH$ can be defined.

Stated in terms of choice functions, Zermelo’s first formulation of *AC* reads:

**AC1**: Any collection of nonempty sets has a choice function.

**AC1** can be reformulated in terms of *indexed* or *variable sets*. An indexed collection of sets $\sA = \{A_{i}: i \in I\}$ may be conceived as a *variable set*, to wit, as a set *varying* over the index set $I$. Each $A_{i}$ is then the “value” of the variable set $\sA$ at *stage* $i$. A *choice function* on $\sA$ is a map $f: I \rightarrow \bigcup_{i\in I} A_{i}$ such that $f(i) \in A_{i}$ for all $i\in I$. A choice function on $\sA$ is thus a “choice” of an element of the variable set $\sA$ at each stage; in other words, a choice function on $\sA$ is a *variable element* of $\sA$. **AC1** is then equivalent to the assertion

**AC2**: Any indexed collection of sets has a choice function.

Informally speaking, **AC2** amounts to the assertion that a variable set with an element at each stage has a variable element.

**AC1** can also be reformulated in terms of relations, viz.

**AC3**: For any relation $R$ between sets $A$, $B$,

$$ {\forall x\inn A}\ \exists y\inn B[R(x,y)] \Rightarrow \exists f[f: A \rightarrow B \amp {\forall x\inn A}[R(x,fx)]]. $$

In other words, every relation contains a function having the same domain.

Finally **AC3** is easily shown to be equivalent (in the usual set theories) to:[^note-2]

**AC4**: Any surjective function has a right inverse.

In a 1908 paper Zermelo introduced a modified form of *AC*. Let us call a *transversal* (or *choice set*) for a family of sets $\sH$ any subset $T \subseteq \bigcup \sH$ for which each intersection $T \cap X$ for $X \in \sH$ has exactly one element. As a very simple example, let $\sH = \{\{0\}, \{1\}, \{2, 3\}\}$. Then $\sH$ has the two transversals $\{0, 1, 2\}$ and $\{0, 1, 3\}$. A more substantial example is afforded by letting $\sH$ be the collection of all lines in the Euclidean plane parallel to the $x$-axis. Then the set $T$ of points on the $y$-axis is a transversal for $\sH$.

Stated in terms of transversals, then, Zermelo’s second (1908) formulation of *AC* amounts to the assertion that any family of mutually disjoint nonempty sets has a transversal.[^note-3]

Zermelo asserts that “the purely objective character” of this principle “is immediately evident.” In making this assertion Zermelo meant to emphasize the fact that in this form the principle makes no appeal to the possibility of making “choices”. It may also be that Zermelo had the following “combinatorial” justification of the principle in mind. Given a family $\sH$ of mutually disjoint nonempty sets, call a subset $S \subseteq \bigcup \sH$ a *selector* for $\sH$ if $S\cap X \ne \varnothing$ for all $X \in \sH$. Clearly selectors for $\sH$ exist; $\bigcup \sH$ itself is an example. Now one can imagine taking a selector $S$ for $\sH$ and “thinning out” each intersection $S \cap X$ for $X\in \sH$ until it contains just a single element. The result is a transversal for $\sH$. This argument, suitably refined, yields a precise derivation of *AC* in this formulation from the set-theoretical principle known as *Zorn’s lemma* (see below).

Let us call Zermelo’s 1908 formulation the *combinatorial* axiom of choice:

**CAC**: Any collection of mutually disjoint nonempty sets has a transversal.

It is to be noted that **AC1** and **CAC** for *finite* collections of sets are both provable (by induction) in the usual set theories. But in the case of an *infinite* collection, even when each of its members is finite, the question of the existence of a choice function or a transversal is problematic[^note-4]. For example, as already mentioned, it is easy to come up with a choice function for the collection of pairs of real numbers (simply choose the smaller element of each pair). But it is by no means obvious how to produce a choice function for the collection of pairs of *arbitrary sets* of real numbers.

Zermelo’s original purpose in introducing *AC* was to establish a central principle of Cantor’s set theory, namely, that every set admits a well-ordering and so can also be assigned a cardinal number. Zermelo’s 1904 introduction of the axiom, as well as the use to which he put it, provoked considerable criticism from the mathematicians of the day. The chief objection raised was to what some saw as its highly non-constructive, even idealist, character: while the axiom asserts the possibility of making a number of—perhaps even an uncountable number—of arbitrary “choices”, it gives no indication whatsoever of how these latter are actually to be effected, of how, otherwise put, choice functions are to be *defined*. This was particularly objectionable to mathematicians of a “constructive” bent such as the so-called French Empiricists Baire, Borel and Lebesgue, for whom a mathematical object could be asserted to exist only if it can be defined in such a way as to characterize it uniquely. Zermelo’s response to his critics came in the form in two papers in 1908. In the first of these, as remarked above, he reformulated *AC* in terms of transversals; in the second (1908a) he made explicit the further assumptions needed to carry through his proof of the well-ordering theorem. These assumptions constituted the first explicit presentation of an axiom system for set theory.

As the debate concerning the Axiom of Choice rumbled on, it became apparent that the proofs of a number of significant mathematical theorems made essential use of it, thereby leading many mathematicians to treat it as an indispensable tool of their trade. Hilbert, for example, came to regard *AC* as an essential principle of mathematics[^note-5] and employed it in his defence of classical mathematical reasoning against the attacks of the intuitionists. Indeed his ε-operators are essentially just choice functions (see the entry on the epsilon calculus).

Although the usefulness of *AC* quickly become clear, doubts about its soundness remained. These doubts were reinforced by the fact that it had certain strikingly counterintuitive consequences. The most spectacular of these was Banach and Tarski’s *paradoxical decompositions of the sphere* (Banach and Tarski 1924)[^banach-1924]: any solid sphere can be split into finitely many pieces which can be reassembled to form two solid spheres of the same size; and any solid sphere can be split into finitely many pieces in such a way as to enable them to be reassembled to form a solid sphere of arbitrary size. (See Wagon 1993.)[^wagon-1993]

It was not until the middle 1930s that the question of the soundness of *AC* was finally put to rest with Kurt Gödel’s proof of its consistency relative to the other axioms of set theory.

Here is a brief chronology of *AC*:[^note-6]

| 1904/1908 | Zermelo introduces axioms of set theory, explicitly formulates *AC* and uses it to prove the well-ordering theorem, thereby raising a storm of controversy. |
| --- | --- |
| 1904 | Russell recognizes *AC* as the *multiplicative axiom*: the product of arbitrary nonzero cardinal numbers is nonzero. |
| 1914 | Hausdorff derives from *AC* the existence of nonmeasurable sets in the “paradoxical” form that $\bfrac{1}{2}$ of a sphere is congruent to $\bfrac{1}{3}$ of it (Hausdorff 1914)[^hausdorff-1914]. |
| 1922 | Fraenkel introduces the “permutation method” to establish independence of *AC* from a system of set theory with atoms (Fraenkel 1922)[^fraenkel-1922]. |
| 1924 | Building on the work of Hausdorff, Banach and Tarski derive from *AC* their paradoxical decompositions of the sphere. |
| 1926 | Hilbert introduces into his proof theory the “transfinite” or “epsilon” axiom as a version of *AC* . (Hilbert 1926)[^hilbert-1926]. |
| 1936 | Lindenbaum and Mostowski extend and refine Fraenkel’s permutation method, and prove the independence of various statements of set theory weaker than *AC* . (Lindenbaum and Tarski 1938)[^lindenbaum-1938] |
| 1935–38 | Gödel establishes relative consistency of *AC* with the axioms of set theory (Gödel 1938a, 1938b, 1939, 1940)[^gödel-1938a][^gödel-1938b][^gödel-1940]. |
| 1950s | Mendelson, Shoenfield and Specker, working independently, use the permutation method to establish the independence of various forms of *AC* from a system of set theory without atoms, but also lacking the axiom of foundation (Mendelson 1956, 1958, Shoenfield 1955, Specker 1957)[^mendelson-1956][^mendelson-1958][^shoenfield-1955][^specker-1957]. |
| 1963 | Paul Cohen proves independence of *AC* from the standard axioms of set theory (Cohen 1963, 1964)[^cohen-1963][^cohen-1964]. |

## 2. Independence and Consistency of the Axiom of Choice

As stated above, in 1922 Fraenkel proved the independence of *AC* from a system of set theory containing “atoms”. Here by an *atom* is meant a pure individual, that is, an entity having no members and yet distinct from the empty set (so *a fortiori* an atom cannot be a set). In a system of set theory with atoms it is assumed that one is given an infinite set $A$ of atoms. One can build a universe $V(A)$ of sets over $A$ by starting with $A$, adding all the subsets of $A$, adjoining all the subsets of the result, etc., and iterating transfinitely. $V(A)$ is then a model of set theory with atoms. The kernel of Fraenkel’s method for proving the independence of *AC* is the observation that, since atoms cannot be set-theoretically distinguished, any permutation of the set $A$ of atoms induces a structure-preserving permutation—an *automorphism*—of the universe $V(A)$ of sets built from $A$. This idea may be used to construct another model $Sym(V)$ of set theory—a *permutation* or *symmetric model*—in which a set of mutually disjoint pairs of elements of $A$ has no choice function.

Now let us suppose that we are given a group $G$ of automorphisms of $A$. Let us say that an automorphism $\pi$; of $A$ *fixes* an element $x$ of $V(A)$ if $\pi(x) = x$. Clearly, if $\pi \in G$ fixes every element of $A$, it also fixes every element of $V(A)$. Now it may be the case that, for certain elements $x \in V(A)$, the fixing of the elements of a *subset* of $A$ by any $\pi\in G$ suffices to fix $x$. We are therefore led to define a *support* for $x$ to be a subset $X$ of $A$ such that, whenever $\pi\in G$ fixes each member of $X$, it also fixes $x$. Members of $V(A)$ possessing a *finite* support are called *symmetric*.

We next define the universe $Sym(V)$ to consist of the *hereditarily symmetric* members of $V(A)$, that is, those $x\in V(A)$ such that $x$, the elements of $x$, the elements of elements of $x$, etc., are all symmetric. $Sym(V)$ is also a model of set theory with set of atoms $A$, and $\pi$ induces an automorphism of $Sym(V)$.

Now suppose $A$ to be partitioned into a (necessarily infinite) mutually disjoint set $P$ of pairs. Take $G$ to be the group of permutations of $A$ which fix all the pairs in $P$. Then $P\in Sym(V)$; it can now be shown that $Sym(V)$ contains no choice function on $P$. For suppose $f$ were a choice function on $P$ and $f \in Sym(V)$. Then $f$ has a finite support which may be taken to be of the form $\{a_{1}, \ldots, a_{n}, b_{1},\ldots,b_{n}\} with each pair \{a_{i}, b_{i}\} \in P$. Since $P$ is infinite, we may select a pair $\{c, d\} = U$ from $P$ different from all the $\{a_{i}, b_{i}\}$. Now we define $\pi \in G$ so that $\pi$ fixes each $a_{i}$ and $b_{i}$ and interchanges $c$ and $d$. Then $\pi$ also fixes $f$. Since $f$ was supposed to be a choice function on $P$, and $U \in P$, we must have $f(U) \in U$, that is, $f(U) = c$ or $f(U) = d$. Since $\pi$ interchanges $c$ and $d$, it follows that $\pi(f(U)) \ne f(U)$. But since $\pi$ is an automorphism, it also preserves function application, so that $\pi(f(U)) = \pi f(\pi(U))$. But $\pi(U) = U$ and $\pi f = f$, whence $\pi(f(U)) = f(U)$. We have duly arrived at a contradiction, showing that the universe $Sym(V)$ contains no choice function on $P$.

The point here is that for a symmetric function $f$ defined on $P$ there is a finite list $L$ of pairs from $P$ the fixing of all of whose elements suffices to fix $f$, and hence also all the values of $f$. Now, for any pair $U$ in $P$ but not in $L$ , a permutation $\pi$ can always be found which fixes all the elements of the pairs in $L$, but does not fix the members of $U$. Since $\pi$ must fix the value of $f$ at $U$, that value cannot lie in $U$. Therefore $f$ cannot “choose” an element of $U$, so *a fortiori* $f$ cannot be a choice function on $P$.

This argument shows that collections of *sets of atoms* need not necessarily have choice functions, but it fails to establish the same fact for the “usual” sets of mathematics, for example the set of real numbers. This had to wait until 1963 when Paul Cohen showed that it is consistent with the standard axioms of set theory (which preclude the existence of atoms) to assume that a countable collection of pairs of sets of real numbers fails to have a choice function. The core of Cohen’s method of proof—the celebrated method of *forcing*—was vastly more general than any previous technique; nevertheless his independence proof also made essential use of permutation and symmetry in essentially the form in which Fraenkel had originally employed them.

Gödel’s proof of the relative consistency of *AC* with the axioms of set theory (see the entry on Kurt Gödel) rests on an entirely different idea: that of *definability*. He introduced a new hierarchy of sets—the *constructible* hierarchy—by analogy with the cumulative type hierarchy. We recall that the latter is defined by the following recursion on the ordinals, where $\sP(X)$ is the power set of $X$, $\alpha$ is an ordinal, and $\lambda$ is a limit ordinal::

\begin{align} V_0 &= \varnothing \\ V_{\alpha+1} &= \sP(V_{\alpha}) \\ V_{\lambda} &= {\bigcup}_{\alpha \lt \lambda} V_{\alpha} \end{align}

The constructible hierarchy is defined by a similar recursion on the ordinals, where $\Def(X)$ is the set of all subsets of $X$ which are first-order definable in the structure $(X, \in, (x)_{x\in X})$:[^note-7]

\begin{align} L_0 &= \varnothing \\ L_{\alpha+1} &= \Def(L_{\alpha}) \\ L_{\lambda} &= {\bigcup}_{\alpha\lt \lambda} L_{\alpha} \end{align}

The *constructible universe* is the class $L = \bigcup_{\alpha\in \Ord} L_{\alpha}$; the members of $L$ are the *constructible sets*. Gödel showed that (assuming the axioms of Zermelo-Fraenkel set theory **ZF**) the structure $(L, \in)$ is a model of **ZF** and also of *AC* as well as the Generalized Continuum Hypothesis). The relative consistency of *AC* with **ZF** follows.

It was also observed by Gödel (1964) (and, independently, by Myhill and Scott 1971, Takeuti 1963 and Post 1951)[^myhill-1971] that a simpler proof of the relative consistency of *AC* can be formulated in terms of *ordinal definability*. If we write $\rD(X)$ for the set of all subsets of $X$ which are first-order definable in the structure $(X, \in)$, then the class OD of *ordinal definable sets* is defined to be the union $\bigcup_{\alpha\in \Ord} D(V_{\alpha})$. The class HOD of *hereditarily ordinal definable sets* consists of all sets $a$ for which $a$, the members of $a$, the members of members of $a$, … etc., are all ordinal definable. It can then be shown that the structure (HOD, $\in$) is a model of **ZF** + *AC* , from which the relative consistency of *AC* with **ZF** again follows.[^note-8]

## 3. Maximal Principles and Zorn’s Lemma

The Axiom of Choice is closely allied to a group of mathematical propositions collectively known as *maximal principles*. Broadly speaking, these propositions assert that certain conditions are sufficient to ensure that a partially ordered set contains at least one *maximal element*, that is, an element such that, with respect to the given partial ordering, no element strictly exceeds it.

To see the connection between the idea of a maximal element and *AC*, let us return to the latter’s formulation **AC2** in terms of indexed sets. Accordingly suppose we are given an indexed family of nonempty sets $\sA = \{A_{i}:i \in I\}.$ Let us define a *potential choice function* on $\sA$ to be a function $f$ whose domain is a subset of $I$ such that $f(i) \in A_{i}$ for all $i\in J$. (Here the use of the qualifier *potential* is suggested by the fact that the domain is a subset of $I$; recall that a choice function $f$ on $\sA$ has the same properties as what we are now calling potential choice functions except that the domain of $f$ is required to be all of $I$, not just a subset.) The set $P$ of potential choice functions on $\sA$ can be partially ordered by inclusion: we agree that, for potential choice functions $f, g \in P$, the relation $f \le g$ holds provided that the domain of $f$ is included in that of $g$ and the value of $f$ at an element of its domain coincides with the value of $g$ there. It is now easy to see that the maximal elements of $P$ with respect to the partial ordering $\le$ are precisely the choice functions on $\sA$.

*Zorn’s Lemma* is the best-known principle ensuring the existence of such maximal elements. To state it, we need a few definitions. Given a partially ordered set $(P, \le)$, an *upper bound* for a subset $X$ of $P$ is an element $a\in P$ for which $x\le a$ for every $x\in X$; a *maximal element* of $P$ may then be defined as an element $a$ for which the set of upper bounds of $\{a\}$ coincides with $\{a\}$, which essentially means that no element of $P$ is strictly larger than $a$. A *chain* in $(P,\le)$ is a subset $C$ of $P$ such that, for any $x$, $y\in P$, either $x\le y$ or $y\le x$. $P$ is said to be *inductive* if every chain in $P$ has an upper bound. Now Zorn’s Lemma asserts:

**Zorn’s Lemma** (**ZL**): Every nonempty inductive partially ordered set has a maximal element.

Why is Zorn’s Lemma plausible? Here is an informal argument. Given a nonempty inductive partially ordered set $(P,\le)$, pick an arbitrary element $p_{0}$ of $P$. If $p_{0}$ is maximal, stop there. Otherwise pick an element $p_{1} \gt p_{0}$; if $p_{1}$ is maximal, stop there. Otherwise pick an element $p_{2} \gt p_{1}$, and repeat the process. If none of the elements $p_{0} \lt p_{1} \lt p_{2} \lt \ldots \lt p_{n} \lt \ldots$ is maximal, the $p_{i}$ form a chain which, since $P$ is inductive, has an upper bound $q_{0}$. If $q_{0}$ is maximal, stop there. Otherwise the procedure can be repeated with $q_{0} \lt q_{1}$, …, and then iterated. This process must eventually terminate, since otherwise the union of the chains so generated would constitute a proper class, making $P$ itself a proper class contrary to assumption. The point at which the process terminates yields a maximal element of $P$.

This argument, suitably rigorized, gives a proof[^note-9] of **ZL** from **AC1** in Zermelo-Fraenkel set theory: in this proof **AC1** is used to “pick” the elements referred to in the informal argument.

Another version of Zorn’s Lemma can be given in terms of collections of sets. Given a collection $\sH$ of sets, let us call a *nest* in $\sH$ any subcollection $\sN$ of $\sH$ such that, for any pair of members of $\sN$, one is included in the other.[^note-10] Call $\sH$ *strongly inductive* if the union of any nest in $\sH$ is a member of $\sH$. Zorn’s Lemma may then be equivalently restated as the assertion that any nonempty strongly inductive collection $\sH$ of sets has a maximal member, that is, a member properly included in no member of $\sH$. This may in turn be formulated in a dual form. Call a family of sets *strongly reductive* if it is closed under intersections of nests. Then any nonempty strongly reductive family of sets has a *minimal* element, that is, a member properly including no member of the family.

**AC2** is now easily derived from Zorn’s Lemma in this alternative form. For the set $P$ of potential choice functions on an indexed family of sets $\sA$ is clearly nonempty and is readily shown to be strongly inductive; so Zorn’s lemma yields the existence of a choice function on $\sA$.

**CAC** can be derived from **ZL** in a way echoing the “combinatorial” justification of **CAC** sketched above. Accordingly suppose we are given a family $\sH$ of mutually disjoint nonempty sets; call a subset $S \subseteq \bigcup \sH$ a *sampling* for $\sH$ if, for any $X\in \sH$, either $X \subseteq S$ or $S \cap X$ is nonempty and finite. Minimal samplings are precisely transversals for $\sH$;[^note-11] and the collection $\sT$ of samplings is clearly nonempty since it contains $\bigcup \sH$. So if it can be shown that $\sT$ is strongly reductive,[^note-12] Zorn’s lemma will yield a minimal element of $\sT$ and so a transversal for $\sH$. The strong reductiveness of $\sT$ may be seen as follows: suppose that $\{S_{i}: i\in I\}$ is a nest of samplings; let $S = {\bigcap}_{i\in I} S_{i}$. We need to show that $S$ is itself a sampling; to this end let $X \in \sH$ and suppose $\neg(X \subseteq S)$. Then there is $i \in I$ for which $\neg(X \subseteq S_{i})$; since $S_{i}$ is a sampling, $S_{i}\cap X$ is finite and nonempty, say $S_{i}\cap X = \{x_{1}, \ldots, x_{n}\}$. Clearly $S\cap X$ is then finite; suppose for the sake of contradiction that $S\cap X = \varnothing$. Then for each $k = 1,\ldots,n$ there is $i_k \in I$ for which $\neg(x_k \in S_{i_k})$. It follows that $\neg(S_{i} \subseteq S_{i_k})$, for $k = 1, \ldots, n$. So, since the $S_{i}$ form a chain, each $S_{i_k}$ is a subset of $S_{i}$. Let $S_{j}$ be the least of $S_{i_1},\ldots, S_{i_k}$; then $S_{j}\subseteq S_{i}$. But since $\neg(x_{k} \in S_{j})$, for $k = 1, \ldots, n$, it now follows that $S_{j} \cap X = \varnothing$, contradicting the fact that $S_{j}$ is a sampling. Therefore $S \cap X\ne \varnothing$; and $S$ is a sampling as claimed.

We note that while Zorn’s lemma and the Axiom of Choice are set-theoretically equivalent, it is much more difficult to derive the former from the latter than vice-versa.

Here is a brief chronology of maximal principles.

| 1909 | Hausdorff introduces first explicit formulation of a maximal principle and derives it from *AC* (Hausdorff 1909)[^hausdorff-1909] |
| --- | --- |
| 1914 | Hausdorff’s *Grundzüge der Mengenlehre* (one of the first books on set theory and general topology) includes several maximal principles. |
| 1922 | Kuratowski formulates and employs several maximal principles in avoiding use of transfinite ordinals (Kuratowski 1922)[^kuratowski-1922]. |
| 1926–28 | Bochner and others independently introduce maximal principles (Bochner 1928, Moore 1932)[^bochner-1928][^moore-1932]. |
| 1935 | Max Zorn, apparently unacquainted with previous formulations of maximal principles, publishes (Zorn 1935)[^zorn-1935] his definitive version thereof later to become celebrated as his lemma (**ZL**). **ZL** was first formulated in Hamburg in 1933, where Chevalley and Artin quickly “adopted” it. It seems to have been Artin who first recognized that **ZL** would yield *AC*, so that the two are equivalent (over the remaining axioms of set theory). Zorn regarded his principle less as a theorem than as an *axiom*—he hoped that it would supersede cumbersome applications in algebra of transfinite induction and well-ordering, which algebraists in the Noether school had come to regard as “transcendental” devices. |
| 1939–40 | Teichmüller, Bourbaki and Tukey independently reformulate **ZL** in terms of “properties of finite character”(Bourbaki 1939, Teichmuller 1939, Tukey 1940)[^bourbaki-1939][^teichmuller-1939]. |

## 4. Mathematical Applications of the Axiom of Choice

The Axiom of Choice has numerous applications in mathematics, a number of which have proved to be formally equivalent to it[^note-13]. Historically the most important application was the first, namely:

**The Well-Ordering Theorem** (Zermelo 1904, 1908)[^zermelo-1904][^zermelo-1908]. Every set can be well-ordered.

After Zermelo published his 1904 proof of the well-ordering theorem from *AC*, it was quickly seen that the two are equivalent.

Another early equivalent of *AC* is

**The Multiplicative Axiom** (Russell 1906)[^russell-1906]. The product of any set of non-zero cardinal numbers is non-zero.

Early applications of *AC* include:

- Every infinite set has a denumerable subset. This principle, again weaker than *AC*, cannot be proved without it in the context of the remaining axioms of set theory.
- Every infinite cardinal number is equal to its square. This was proved equivalent to *AC* in Tarski 1924.
- Every vector space has a basis (initiated by Hamel 1905)[^hamel-1905]. This was proved equivalent to *AC* in Blass 1984.
- Every field has an algebraic closure (Steinitz 1910)[^steinitz-1910]. This assertion is weaker than *AC*, indeed is a consequence of the (weaker) compactness theorem for first-order logic (see below).
- There is a Lebesgue nonmeasurable set of real numbers (Vitali 1905)[^vitali-1905]. This was shown much later to be a consequence of **BPI** (see below) and hence weaker than *AC*. Solovay (1970) established its independence of the remaining axioms of set theory.

A significant “folklore” equivalent of *AC* is

**The Set-Theoretic Distributive Law**. For an arbitrary doubly-indexed family of sets $\{M_{i,j}: i \in I,j \in J\}$, and where $J^I$ is the set of all functions with domain $I$ and which take values in $J$:

$$ \bigcap_{i\in I} \bigcup_{j\in J} M_{i,j} = \bigcup_{f\in J^I} \bigcap_{i\in I} M_{i,f(i)} $$

A much-studied special case of *AC* is the

**Principle of Dependent Choices** (Bernays 1942, Tarski 1948)[^bernays-1942][^tarski-1948]. For any nonempty relation $R$ on a set $A$ for which $\range(R) \subseteq \domain(R)$, there is a function $f: \omega \rightarrow A$ such that, for all $n\in \omega, R(f(n),f(n+1))$. This principle, although (much) weaker than *AC*, cannot be proved without it in the context of the remaining axioms of set theory.

Mathematical equivalents of *AC* include:

- **Tychonov’s Theorem** (1930): the product of compact topological spaces is compact. This was proved equivalent to *AC* in Kelley 1950. But for compact Hausdorff spaces it is equivalent to **BPI** (see below) and hence weaker than *AC*
- **Löwenheim-Skolem-Tarski Theorem** (Löwenheim 1915, Skolem 1920, Tarski and Vaught 1957)[^tarski-1957]: a first-order sentence having a model of infinite cardinality $\kappa$ also has a model of any infinite cardinality $\mu$ such that $\mu \le \kappa$. This was proved equivalent to *AC* by Tarski.
- **Krein-Milman Theorem**: the unit ball $B$ of the dual of a real normed linear space has an extreme point, that is, one which is not an interior point of any line segment in $B$. This was proved equivalent to *AC* in Bell and Fremlin 1972a. There it is shown that, given any indexed family $\sA$ of nonempty sets, there is a natural bijection between choice functions on $\sA$ and the extreme points of the unit ball of the dual of a certain real normed linear space constructed from $\sA$.
- Every distributive lattice has a maximal ideal. This was proved equivalent to *AC* in Klimovsky 1958, and for lattices of sets in Bell and Fremlin 1972.
- Every commutative ring with identity has a maximal ideal. This was proved equivalent to *AC* by Hodges 1979.

There are a number of mathematical consequences of *AC* which are known to be weaker[^note-14] than it, in particular:

- **The Boolean Prime Ideal Theorem** (**BPI**): every Boolean algebra has a maximal (or prime) ideal. This was shown to be weaker than *AC* in Halpern and Levy 1971.
- **The Stone Representation Theorem for Boolean algebras** (Stone 1936)[^stone-1936]: every Boolean algebra is isomorphic to a field of sets. This is equivalent to **BPI** and hence weaker than *AC*
- **Compactness Theorem for First-Order Logic** (Gödel 1930, Malcev 1937, others): if every finite subset of a set of first-order sentences has a model, then the set has a model. This was shown, in Henkin 1954, to be equivalent to **BPI**, and hence weaker than *AC*.
- **Completeness Theorem for First-Order Logic** (Gödel 1930, Henkin 1954): each consistent set of first-order sentences has a model. This was shown by Henkin in 1954 to be equivalent to **BPI**, and hence weaker than *AC*. If the cardinality of the model is specified in the right way, the assertion becomes equivalent to *AC*.

Finally, there is

- **The Sikorski Extension Theorem for Boolean algebras** (Sikorski 1949): every complete Boolean algebra is injective, i.e., for any Boolean algebra $A$ and any complete Boolean algebra $B$, any homomorphism of a subalgebra of $A$ into $B$ can be extended to the whole of $A$.

The question of the equivalence of this with *AC* is one of the few remaining interesting open questions in this area; while it clearly implies **BPI**, it was proved independent of **BPI** in Bell 1983.

Many of these theorems are discussed in Bell and Machover (1977).

## 5. The Axiom of Choice and Logic

An initial connection between *AC* and logic emerges by returning to its formulation **AC3** in terms of relations, namely: any binary relation contains a function with the same domain. This version of **AC** is naturally expressible within a second-order language $L$ with individual variables $x$, $y$, $z$, … and function variables $f$, $g$, $h$, …. In $L$, binary relations are represented by formulas $\phi(x, y)$ with two free individual variables $x$, $y$. The counterpart in $L$ of the assertion **AC3** is then

> **ACL**:
> $\forall x \exists y \phi(x, y) \rightarrow \exists f \forall x \phi(x, fx).$

This scheme of sentences is the standard logical form of *AC*.

Zermelo’s original form of the Axiom of Choice, **AC1**, can be expressed as a scheme of sentences within a suitably strengthened version of $L$. Accordingly we now suppose $L$ to contain in addition predicate variables $X$, $Y$, $Z$, … and second-order function variables $F$, $G$, $H$, …. Here a second-order function variable $F$ may be applied to a predicate variable $X$ to yield an individual term $FX$. The scheme of sentences

> **AC1L**:
> $\forall X [\Phi(X) \rightarrow \exists x X(x)] \rightarrow \exists F \forall X[\Phi(X) \rightarrow X(FX)]$

is the direct counterpart of **AC1** in this strengthened second-order language. In words, **AC1L** asserts that, if each predicate having a certain property $\Phi$ has instances, then there is a function $F$ on predicates such that, for any predicate $X$ satisfying $\Phi$, $FX$ is an instance of $X$. Here predicates are playing the role of sets.

Up to now we have tacitly assumed our background logic to be the usual classical logic. But the true depth of the connection between **AC** and logic emerges only when *intuitionistic* or *constructive* logic is brought into the picture. It is a remarkable fact that, assuming only the framework of intuitionistic logic together with certain mild further presuppositions, the Axiom of Choice can be shown to entail the cardinal rule of classical logic, the law of excluded middle—the assertion that $A \vee \neg A$ for any proposition $A$. To be precise, using the rules of intuitionistic logic within our augmented language $L$, we shall derive[^note-15] the law of excluded middle from **AC1L** conjoined with the following additional principles:

**Predicative Comprehension**: $\exists X \forall x[X(x) \leftrightarrow \phi(x)]$, where $\phi$ contains no bound function or predicate variables.

**Extensionality of Functions**: $\forall X \forall Y \forall F[X \approx Y \rightarrow FX = FY]$, where $X \approx Y$ is an abbreviation for $\forall x[X(x) \leftrightarrow Y(x)]$, that is, $X$ and $Y$ are *extensionally equivalent*.

**Two Distinct Individuals**: $\uO \ne \uI$, where $\uO$ and $\uI$ are individual constants.

Now let $A$ be a given proposition. By Predicative Comprehension, we may introduce predicate constants $U$, $V$ together with the assertions

\begin{align} \tag{1} &\forall x[U(x) \leftrightarrow (A \vee x = 0)] \\ \notag &\forall x[V(x) \leftrightarrow (A \vee x = 1)] \end{align}

Let $\Phi(X)$ be the formula $X \approx U \vee X \approx V$. Then clearly we may assert $\forall X[\Phi(X) \rightarrow \exists xX(x)]$ so **AC1L** may be invoked to assert $\exists F \forall X[\Phi(X) \rightarrow X(FX)]$. Now we can introduce a function constant $K$ together with the assertion

$$ \tag{2} \forall X[\Phi(X) \rightarrow X(KX)]. $$

Since evidently we may assert $\Phi(U)$ and $\Phi(V)$, it follows from (2) that we may assert $U(KU)$ and $V(KV)$, whence also, using (1),

$$ [A \vee KU = 0] \wedge [A \vee KV = 1]. $$

Using the distributive law (which holds in intuitionistic logic), it follows that we may assert

$$ A \vee [KU = 0 \wedge KV = 1]. $$

From the presupposition that $0 \ne 1$ it follows that

$$ \tag{3} A \vee KU \ne KV $$

is assertable. But it follows from (1) that we may assert $A \rightarrow U ≈ V$, and so also, using the Extensionality of Functions, $A \rightarrow KU = KV$. This yields the assertability of $KU \ne KV \rightarrow \neg A$, which, together with (3) in turn yields the assertability of

$$ A \vee \neg A $$

that is, the law of excluded middle.

The fact that the Axiom of Choice implies Excluded Middle seems at first sight to be at variance with the fact that the former is often taken as a *valid* principle in systems of constructive mathematics governed by intuitionistic logic, e.g. Bishop’s Constructive Analysis[^note-16] and Martin-Löf’s Constructive Type Theory[^note-17], in which Excluded Middle is not affirmed. In Bishop’s words, “A choice function exists in constructive mathematics because a choice is *implied by the very meaning of existence*.” Thus, for example, the antecedent $\forall x \exists y \phi(x,y)$ of **ACL**, given a constructive construal, just *means* that we have a procedure which, applied to each $x$, yields a $y$ for which $\phi(x, y)$. But this is precisely what is expressed by the consequent $\exists f \forall x \phi(x,fx)$ of **ACL**.

To resolve the difficulty, we note that in deriving Excluded Middle from **ACL1** essential use was made of the principles of Predicative Comprehension and Extensionality of Functions[^note-18]. It follows that, in systems of constructive mathematics affirming **AC** (but not Excluded Middle) *either the principle of Predicative Comprehension or the principle of Extensionality of Functions must fail*. While the principle of Predicative Comprehension can be given a constructive justification, no such justification can be provided for the principle of Extensionality of Functions. Functions on predicates are given intensionally, and satisfy just the corresponding principle of Intensionality $\forall X \forall Y \forall F[X = Y \rightarrow FX = FY]$. The principle of Extensionality can easily be made to fail by considering, for example, the predicates $P$: *rational featherless biped* and $Q$: *human being* and the function $K$ on predicates which assigns to each predicate the number of words in its description. Then we can agree that $P \approx Q$ but $KP = 3$ and $KQ = 2$.

In intuitionistic set theory (that is, set theory based on intuitionistic as opposed to classical logic—we shall abbreviate this as **IST**) and in topos theory the principles of Predicative Comprehension and Extensionality of Functions (both appropriately construed) hold and so there **AC** implies Excluded Middle.[^note-19] ^{,} [^note-20]

The derivation of Excluded Middle from *AC* was first given by Diaconescu (1975) in a category-theoretic setting. His proof employed essentially different ideas from the proof presented above; in particular, it makes no use of extensionality principles but instead employs the idea of the quotient of an object (or set) by an equivalence relation. It is instructive to formulate Diaconescu’s argument within **IST**. To do this, let us call a subset $U$ of a set $A$ *detachable* if there is a subset $V$ of $A$ for which $U \cap V = \varnothing$ and $U \cup V = A$. Diaconescu’s argument amounts to a derivation from **AC4** (see above) of the assertion that every subset of a set is detachable, from which Excluded Middle readily follows. Here it is.

First, given $U \subseteq A$, an *indicator* for $U$ (in $A$) is a map $g: A \times 2 \rightarrow 2$ satisfying

$$ U = \{ x \in A: g(x,0) = g(x,1) \} $$

It is then easy to show that a subset is detachable if and only if it has an indicator.

Now we show that, if **AC4** holds, then any subset of a set has an indicator, and hence is detachable.

For $U \subseteq A$, let $R$ be the binary relation on $A + A = A \times \{0\} \cup A \times \{1\}$ given by

$$ R = \{ ((x,0),(x,0)) : x \in A \} \cup \{ ((x,1),(x,1)) : x \in A \} \cup \{ ((x,0),(x,1) : x \in A \} \cup \{ ((x,1),(x,0) \} : x \in A $$

It can be checked that $R$ is an equivalence relation. Write $r$ for the natural map from $A + A$ to the quotient[^note-21] $Q$ of $(A + A)$ by $R$ which carries each member of $A + A$ to its $R-$equivalence class.

Now apply **AC4** to obtain a map $f: Q \rightarrow A + A$ satisfying $f(X) \in X$ for all $X \in Q$. It is then not hard to show that, writing $\pi_{1}$ for projection on the first coordinate,

$$ \tag{*} \mbox{for } n=0,1 \mbox{ and } x \in A, \pi_1(f(r(x,n))) = x; $$

and

$$ \tag{**} x \in U \leftrightarrow f(r(x,0)) = f(r(x,1)). $$

Now define $g: A \times 2 \rightarrow 2$ by $g = \pi_{2} \circ f \circ r$, where $\pi_2$ is a projection on the second coordinate. Then $g$ is an indicator for $U$, as the following equivalences show:

\begin{align} x \in U &\leftrightarrow f(r(x,0))=f(r(x,1)) \ldots \mbox{by (**)} \\ &\leftrightarrow \pi_{1}(f(r(x,0))) = \pi_{1}(f(r(x,1))) \wedge \pi_{2}(f(r(x,0))) = \pi_{2}(f(r(x,1))) \\ &\leftrightarrow \pi_{2}(f(r(x,0))) = \pi_{2}(f(r(x,1))) \ldots \mbox{using (*)} \\ &\leftrightarrow g(x,0) = g(x,1). \end{align}

The proof is complete.

It can be shown (Bell 2006)[^bell-2006] that each of a number of intuitionistically invalid logical principles, including the law of excluded middle, is *equivalent* (in intuitionistic set theory) to a suitably weakened version of the axiom of choice. Accordingly these logical principles may be viewed as choice principles.

Here are the logical principles at issue:

| **SLEM** | $\alpha \vee \neg \alpha$ ($\alpha$ any sentence) |
| --- | --- |
| **Lin** | $(\alpha \rightarrow \beta) \vee (\beta \rightarrow \alpha)$ ($\alpha$, $\beta$ any sentences) |
| **Stone** | $\neg \alpha \vee \neg\neg \alpha$ ($\alpha$ any sentence) |
| **Ex** | $\exists x[ \exists x \alpha(x) \rightarrow \alpha(x)]$ ($\alpha(x)$ any formula with at most $x$ free) |
| **Un** | $\exists x[\alpha(x) \rightarrow \forall x\alpha(x)]$ ($\alpha(x)$ any formula with at most $x$ free) |
| **Dis** | $\forall x[\alpha \vee \beta(x)] \rightarrow \alpha\vee\forall x\beta(x)$ ($\alpha$ any sentence, $\beta(x)$ any formula with at most $x$ free) |

Over intuitionistic logic, **Lin**, **Stone** and **Ex** are consequences of **SLEM**; and **Un** implies **Dis**. All of these schemes follow, of course, from the full law of excluded middle, that is **SLEM** for arbitrary formulas.

In what follows the empty set is denoted by 0, $\{0\}$ by 1, and $\{0, 1\}$ by 2.

We formulate the following choice principles—here $X$ is an arbitrary set, $\Fun(X)$ the class of functions with domain $X$ and $\phi(x,y)$ an arbitrary formula of the language of set theory with at most the free variables $x$, $y$:

| **AC**$_X$ | $\forall x\in X\ \exists y \phi(x,y) \rightarrow \exists f \in \Fun(X)\ \forall x \in X\ \phi(x,fx)$ |
| --- | --- |
| **AC**$^*_X$ | ${\exists f \inn \Fun(X)} [{\forall x\inn X}\ \exists y \phi(x,y) \rightarrow {\forall x \inn X}\ \phi(x,fx)]$ |
| **DAC**$_X$ | $\forall f \inn Fun(X)\ {\exists x \inn X}\ \phi(x,fx) \rightarrow {\exists x \inn X}\ \forall y \phi(x,y)$ |
| **DAC**$^*_X$ | ${\exists f \inn \Fun(X)}\ [{\exists x\inn X}\ \phi(x,fx) \rightarrow {\exists x \inn X}\ \forall y \phi(x,y)]$ |

The first two of these are forms of *AC* for $X$; while classically equivalent, in **IST** **AC**$^*_X$ implies **AC**$_X$, but not conversely. The principles **DAC**$_X$ and **DAC**$^*_X$ are *dual* forms of the axiom of choice for $X$: classically they are both equivalent to **AC**$_X$ and **AC**$^*_X$ but intuitionistically **DAC**$^*_X$ implies **DAC**$_X$, and not conversely.

We also formulate the *weak extensional selection principle*, in which $\alpha(x)$ and $\beta(x)$ are any formulas with at most the variable $x$ free:

**WESP**: ${\exists x\inn 2}\ \alpha(x) \wedge {\exists x \inn 2}\ \beta(x) \rightarrow {\exists x \inn 2}\ {\exists y \inn 2}\ [\alpha(x) \wedge \beta(y) \wedge [{\forall x \inn 2}\ [\alpha(x) \leftrightarrow \beta(x)] \rightarrow x = y]].$

This principle, a straightforward consequence of the axiom of choice, asserts that, for any pair of instantiated properties of members of 2, instances may be assigned to the properties in a manner that depends just on their extensions.

Each of the logical principles tabulated above is equivalent (in **IST**) to a choice principle. In fact:

- **WESP** and **SLEM** are equivalent over **IST**.
- **AC**$^*_1$ and **Ex** are equivalent over **IST**.

Further, while **DAC**$_1$ is easily seen to be provable in **IST**, we have

- **DAC**$^*_1$ and **Un** are equivalent over **IST**.

Next, while **AC**$_2$ is easily proved in **IST**, by contrast we have

- **DAC**$_2$ and **Dis** are equivalent over **IST**.
- Over **IST**, **DAC**$^*_2$ is equivalent to **Un**, and hence also to **DAC**$^*_1$.

In order to provide choice schemes equivalent to **Lin** and **Stone** we introduce

**ac**$^*_X$: ${\exists f \inn 2^X} [{\forall x\inn X}\ {\exists y \inn 2}\ \phi(x,y) \rightarrow {\exists x \inn X}\ \phi(x,fx)]$

**wac**$^*_X$: ${\exists f \inn 2^X} [{\forall x \inn X}\ {\exists y \inn 2}\ \phi(x,y) \rightarrow {\forall x \inn X}\ \phi(x,fx)]$ provided it is provable in **IST** that $\forall x[\phi(x,0) \rightarrow \neg\phi(x,1)]$

Clearly **ac**$^*_X$ is equivalent to

${\exists f \inn 2^X}[{\forall x \inn X}[\phi(x,0) \vee \phi(x,1)] \rightarrow {\forall x \inn X}\ \phi(x,fx)]$

and similarly for **dac**$^*_X$.

Then, over **IST**, **ac**$^*_1$ and **dac**$^*_1$ are equivalent, respectively, to **Lin** and **Stone**.

These results show just how deeply choice principles interact with logic, when the background logic is assumed to be intuitionistic. In a classical setting where the Law of Excluded Middle is assumed these connections are obliterated.

Readers interested in the topic of the axiom of choice and type theory may consult the following supplementary document:

> [The Axiom of Choice and Type Theory](axiom-choice.choice-and-type-theory.md)

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=axiom-choice). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/axiom-choice/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=axiom-choice&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](http://philpapers.org/sep/axiom-choice/) at [PhilPapers](http://philpapers.org/), with links to its database. |

## Other Internet Resources

- [A home page for the axiom of choice](http://www.math.vanderbilt.edu/~schectex/ccc/choice.html), maintained by Eric Schecter (Vanderbilt).

## Related Entries

category theory | Gödel, Kurt | logic, history of: intuitionistic logic | logic: intuitionistic | mathematics: constructive | set theory: constructive and intuitionistic ZF | set theory: Zermelo’s axiomatization of | type theory: intuitionistic

### Acknowledgments

The author and editors would like to thank Jesse Alama for carefully reading this piece and making many valuable suggestions for improvement.

## Notes（原文脚注）

[^note-1]: Zermelo does not, however, actually give the principle an explicit name at this point. ( He does so only in 1908, where he uses the term “postulate of choice”. We note that Zermelo here uses the term “product” , which is the reason why a number of mathematicians (in particular Russell and Ramsey) referred to the axiom as the “multiplicative axiom” (see §4 below).

[^note-2]: A function $f$: $A \rightarrow B$ is *surjective* if for any element $b \in B$ there is $a \in A$ such that $f(a) = b$. A *right inverse* to $f$ is a function $g: B \rightarrow A$ such that, for any $x\in B$, $f(g(x) = x$.

[^note-3]: Zermelo’s formulation reads literally:

> A set $S$ that can be decomposed into a set of disjoint parts $A$, $B$, $C$, … , each containing at least one element, possess at least one subset $S_{1}$ having exactly one element with each of the parts $A$, $B$, $C$, … , considered.

[^note-4]: The difficulty here is amusingly illustrated by an anecdote due to Bertrand Russell. A millionaire possesses an infinite number of pairs of shoes, and an infinite number of pairs of socks. One day, in a fit of eccentricity, the millionaire summons his valet and asks him to select one shoe from each pair. When the valet, accustomed to receiving precise instructions, asks for details as to how to perform the selection, the millionaire suggests that the left shoe be chosen from each pair. Next day the millionaire proposes to the valet that he select one *sock* from each pair. When asked as to how *this* operation is to be carried out, the millionaire is at a loss for a reply, since, unlike shoes, there is no intrinsic way of distinguishing one sock of a pair from the other. In other words, the selection of the socks must be truly arbitrary.

[^note-5]: In 1923 Hilbert asserted:

> The essential idea on which the axiom of choice is based constitutes a general logical principle which, even for the first elements of mathematical inference, is indispensable.

(Quoted in section 4.8 of Moore 1982.)[^moore-1982]

[^note-6]: For a detailed history of the Axiom of Choice, see Moore 1982.

[^note-7]: Here ($x)_{x\in X}$ indicates that all the members of $X$ are taken as designated elements of the structure, i.e. as being named by constant symbols in the associated first-order language.

[^note-8]: For a detailed account of the proof of the independence of the Axiom of Choice, see Bell 2005 or Jech 1973.

[^note-9]: For the proof of *ZL* from *AC* in **ZF**, see Mendelson 1987 (Ch. 4, sect. 5). For a proof not using ordinals, and so formulable in Zermelo set theory, see Bourbaki 1950 or Lawvere and Rosebrugh 2003 (Appendix B).

[^note-10]: Thus a nest in $S$ is a chain in $S$ partially ordered by set inclusion.

[^note-11]: That minimal samplings are transversals requires demonstration. Suppose $S$ is a minimal sampling; then, given $X\in \sI$ either (1) $S\cap X$ is finite nonempty or (2) $X \subseteq S$. In case (1) $S\cap X$ cannot contain two distinct elements because the removal of one of them from $S$ would yield a sampling smaller than $S$, violating its minimality. So in this case $S\cap X$ must be a singleton. In case (2) $S$ cannot contain two distinct elements $a$, $b$ since, if it did, $S' = [(S - X) \cup \{a\}]$ would be a sampling smaller than $S$ (notice that $S' \cap X = \{a\}$ and the relations of $S'$ with the members of $\sI - \{X\}$ are the same as those of $S$), again violating the minimality of $S$. So in this case $X$, and *a fortiori* $S\cap X$ must be a singleton.

[^note-12]: Had we elected to follow more closely the intuitive combinatorial derivation of *AC* as sketched above by using selectors instead of samplings we would have encountered the obstacle that—unlike the set of samplings—the set of selectors is not necessarily reductive.

[^note-13]: For equivalents of the Axiom of Choice, see Rubin and Rubin 1985; for consequences, see Howard and Rubin 1998.

[^note-14]: “Weaker” here means that, within the context of the axioms of set theory (minus, of course, *AC*), the proposition in question is entailed by *AC*, but not vice-versa.

[^note-15]: The idea of the proof goes back to Goodman and Myhill 1978, which was itself built on a result of Diaconescu 1975. See below.

[^note-16]: See Bishop and Bridges 1985.

[^note-17]: See Supplementary Document. For an analysis of various versions of *AC* within constructive type theory, see Martin-Löf 2006.

[^note-18]: Also, of course, use was made of $0 \ne 1$, but this assumption is so weak that it may be consistently added to virtually any axiomatic system.

[^note-19]: But in weak set theories lacking the axiom of extensionality the derivation of Excluded Middle from *AC* does not go through: some form of extensionality, or the existence of quotient sets for equivalence relations, needs to be assumed. See Bell 2008.

[^note-20]: With Zorn’s Lemma the situation is otherwise. For despite its equivalence to *AC* in classical set theory, in intuitionistic set theory Zorn’s Lemma *does not imply* **LEM:** in fact, it has no “non-constructive” logical consequences whatsoever (Grayson 1975, Bell 1997)[^bell-1997][^grayson-1975]. Thus Zorn’s Lemma is considerably weaker than *AC* in intuitionistic set theory. Intuitionistic equivalents of Zorn’s Lemma are scarce; a few have been formulated in Bell 2003.

[^note-21]: That is, the set of all $R$-equivalence classes of members of $A$.

### Notes to Supplementary Document: The Axiom of Choice and Type Theory

1. Dependent types were actually first studied in the late 1960s by de Bruijn and his colleagues at the University of Eindhoven in connection with the AUTOMATH project. CDTT has been employed as a basis for various computational devices employed for the verification of mathematical theories and of software and hardware systems in computer science.

2. Analogous constructive versions of set theory, incorporating choice principles, have been developed by Peter Aczel. See Aczel 1978, 1982, 2005 and Aczel & Rathjen 2001.

3. This idea was advanced by Curry and Feys 1958 and later by Howard 1980. As the *Curry-Howard correspondence* it has come to play an important role in theoretical computer science.

4. For a complete specification of the operations and rules of DCTT, see Chapter 10 of Jacobs 1999 or Gambino & Aczel 2005.

5. See §4.

6. It is interesting to note that Ramsey 1926 also asserted the tautological character of *AC* but for quite different reasons. Like Zermelo, Ramsey construed—and accepted the truth of—*AC* as asserting the objective existence of choice functions, given extensionally and so independently of the manner in which they might be described. But the intensional nature of constructive mathematics, and, in particular, of **CDTT**, decrees that nothing is given completely independently of its description. This leads to a strong construal of the quantifiers which, as we have observed, essentially trivializes *AC* by rendering the antecedent of the implication constituting it essentially equivalent to the consequent. It is remarkable that *AC* can be considered tautological both from an extensional and from an intensional point of view.

7. While in classical set theory each singleton in this sense is either empty or a one-element set, in intuitionistic set theory there are many additional “intermediate” sets qualifying as singletons.

[^aczel-1978]: Aczel, P., 1978. “The type-theoretic interpretation of constructive set theory,” in A. ManIntyre, L. Pacholski, and J. Paris (eds.), *Logic Colloquium 77*, Amsterdam: North-Holland, pp. 55–66.

[^aczel-1982]: –––, 1982. “The type-theoretic interpretation of constructive set theory: choice principles,” in A. S. Troelstra and D. van Dalen (eds.), *The L.E.J. Brouwer Centenary Symposium*, Amsterdam: North-Holland, pp. 1–40.

[^aczel-2002]: Aczel, P. and N. Gambino, 2002. “Collection principles in dependent type theory,” in P. Callaghan, Z. Luo, J. McKinna and R. Pollack (eds.), *Types for Proofs and Programs* (Lecture Notes on Computer Science, Volume 2277), Berlin: Springer, pp. 1–23.

[^aczel-2005]: –––, 2005. “The generalized type-theoretic interpretation of constructive set theory,” *Journal of Symbolic Logic*, 71/1: 67–103. [[Preprint available online in compressed Postscript](http://www.cs.man.ac.uk/~petera/gambino-aczel.ps.gz)]

[^aczel-2013]: Aczel, P., Berg, B. and J. Granstrom, 2013. “Are there enough injective sets?,” *Studia Logica*, 101(3): 467–482.

[^aczel-2001]: Aczel, P. and M. Rathjen, 2001. *Notes on Constructive Set Theory*. Technical Report 40, Mittag-Leffler Institute, The Swedish Royal Academy of Sciences. [[Preprint available online](http://www.mittag-leffler.se/sites/default/files/IML-0001-40.pdf)]

[^banach-1924]: Banach, S. and Tarski, A., 1924. “Sur la décomposition des ensembles de points en parties respectivement congruentes,” *Fundamenta Mathematicae*, 6: 244–277.

[^bell-1983]: Bell, J.L., 1983. “On the strength of the Sikorski extension theorem for Boolean algebras,” *Journal of Symbolic Logic*, 48: 841–846.

[^bell-1988]: –––, 1988. *Toposes and Local Set Theories: An Introduction*, Oxford: Clarendon Press.

[^bell-1997]: –––, 1997. “Zorn’s lemma and complete Boolean algebras in intuitionistic type theories,” *Journal of Symbolic Logic*, 62: 1265–1279.

[^bell-2003]: –––, 2003. “Some new intuitionistic equivalents of Zorn’s Lemma,” *Archive for Mathematical Logic*, 42: 811–814.

[^bell-2005]: –––, 2005. *Set Theory: Boolean-valued Models and Independence Proofs*, Oxford: Clarendon Press.

[^bell-2006]: –––, 2006. “Choice principles in intuitionistic set theory,” in *A Logical Approach to Philosophy*, Devidi, D. and Kenyon, T.(eds.), Berlin: Springer, 36–44.

[^bell-2008]: –––, 2008. “The axiom of choice and the law of excluded middle in weak set theories,” *Mathematical Logic Quarterly*, 48: 841–846.

[^bell-2009]: –––, 2009. *The Axiom of Choice*, London: College Publications.

[^bell-2011]: –––, 2011. “The axiom of choice in an elementary theory of operations and sets” in *Analysis and Interpretation in the Exact Sciences*, Devidi, D. and Kenyon, T.(eds.), Berlin: Springer, 163–175.

[^bell-1972]: Bell, J.L. and Fremlin, D., 1972. “The maximal ideal theorem for lattices of sets,” *Bulletin of the London Mathematical Society*, 4: 1–2.

[^bell-1972a]: –––, 1972a. “A geometric form of the axiom of choice,” *Fundamenta Mathematicae*, 77: 167–170.

[^bell-1977]: Bell, J.L. and Machover, M. , 1977. *A Course in Mathematical Logic*. Amsterdam: North-Holland.

[^bernays-1942]: Bernays, P., 1942. “A system of axiomatic set theory, Part III,” *Journal of Symbolic Logic*, 7: 65–89.

[^bishop-1985]: Bishop, E. and Bridges, D., 1985. *Constructive Analysis*, Berlin: Springer.

[^blass-1984]: Blass, A., 1984. “Existence of bases implies the axiom of choice,” in *Axiomatic Set Theory*, Baumgartner, Martin and Shelah (eds.) (Contemporary Mathematics Series, Volume 31), American Mathematical Society, pp. 31–33.

[^bochner-1928]: Bochner, S., 1928. “Fortsetzung Riemannscher Flachen,” *Mathematische Annalen*, 98: 406–421.

[^bourbaki-1939]: Bourbaki, N., 1939. *Elements de Mathematique, Livre I: Theorie des Ensembles*, Paris: Hermann.

[^bourbaki-1950]: –––, 1950.“Sur le theoreme de Zorn,” *Archiv dem Mathematik*, 2: 434–437.

[^cohen-1963]: Cohen, P.J., 1963. “The independence of the continuum hypothesis I,” *Proceedings of the U.S. National Academy of Sciemces*, 50: 1143–48. [The independence of the Axiom of Choice from the standard axioms of set theory, ZF, is part of Theorem 1 of this paper.]

[^cohen-1964]: –––, 1964. “The independence of the continuum hypothesis II,” *Proceedings of the U.S. National Academy of Sciemces*, 51: 105–110.

[^cohen-1966]: –––, 1966. *Set Theory and the Continuum Hypotheis*, New York: Benjamin.

[^curry-1958]: Curry, H.B. and R. Feys, 1958. *Combinatory Logic*, Amsterdam: North Holland.

[^devidi-2004]: Devidi, D., 2004. “Choice principles and constructive logics,” *Philosophia Mathematica*, 12(3): 222–243.

[^diaconescu-1975]: Diaconescu, R., 1975. “Axiom of choice and complementation,” *Proceedings of the American Mathematical Society*, 51: 176–8.

[^fraenkel-1922]: Fraenkel, A., 1922. “Zu den Grundlagen der Cantor-Zermeloschen Mengenlehre”, *Mathematische Annalen*, 86: 230–237.

[^fraenkel-1922a]: Fraenkel, A., 1922a.“Über den Begriff ‘definit’ und die Unabhängigkeit des Auswahlsaxioms,” *Sitzungsberichte der Preussischen Akademie der Wissenschaften, Physik-math. Klasse*, 253–257. Translated in van Heijenoort, From Frege to Gödel: A Source Book in Mathematical Logic 1879–1931, Harvard University Press, 1967, pp. 284–289.

[^fraenkel-1973]: Fraenkel, A., Y. Bar-Hillel and A. Levy, 1973. *Foundations of Set Theory*, Amsterdam: North-Holland, 2ⁿᵈ edition.

[^gödel-1938a]: Gödel, K., 1938a. “The consistency of the axiom of choice and of the generalized continuum-hypothesis,” *Proceedings of the U.S. National Academy of Sciences*, 24: 556–7.

[^gödel-1938b]: Gödel, K., 1938b. “Consistency-proof for the generalized continuum-hypothesis,” *Proceedings of the U.S. National Academy of Sciemces*, 25: 220–4.

[^gödel-1940]: Gödel, K., 1940. *The Consistency of the Axiom of Choice and of the Generalized Continuum-Hypothesis with the Axioms of Set Theory*, Annals of Mathematics Studies, No. 3, Princeton: Princeton University Press.

[^gödel-1964]: Gödel, K., 1964. “Remarks before the Princeton Bicentennial Conference,” in *The Undecidable*, Martin Davis (ed.), CITY: Raven Press, pp. 84–88.

[^goodman-1978]: Goodman, N. and Myhill, J., 1978. “Choice implies excluded middle,” *Zeitschrift fur Mathematische Logik und Grundlagen der Mathematik* , 24(25–30): 461.

[^grattan-guinness-2012]: Grattan-Guinness, I., 2012. “Jourdain, Russell and the axiom of choice: a new document,” *Russell: The Journal of the Bertrand Russell Archives*, 32(1): 69–74.

[^grayson-1975]: Grayson, R.J., 1975. “A sheaf approach to models of set theory,” M.Sc. Thesis, Mathematics Department, Oxford University.

[^halpern-1971]: Halpern, , J.D. and Levy, A., 1971. “The Boolean prime ideal theorem does not imply the axiom of choice,” *Axiomatic Set Theory*, Proceedings of Symposia in Pure Mathematics, Vol. XIII, Part I. American Mathematical Society, pp. 83–134.

[^hamel-1905]: Hamel, G., 1905. “Eine Basis aller Zahlen und die unstetigen Lösungen der Funktionalgleichung: *f(x* + *y*) = *f(x*) + *f(y*),” *Mathematische Annalen*, 60: 459–62.

[^hausdorff-1909]: Hausdorff, F., 1909. “Die Graduierung nach dem Endverlauf,” *Königlich Sächsichsen Gesellschaft der Wissenschaften zu Leipzig, Math.—Phys. Klasse, Sitzungberichte*, 61: 297–334.

[^hausdorff-1914]: –––, 1914. *Grundzüge der Mengenlehre*, Leipzig: de Gruyter. Reprinted, New York: Chelsea, 1965.

[^hausdorff-1914a]: –––, 1914a. “Bemerkung über den Inhalt von Punktmengen,” *Mathematische Annalen*, 75: 428–433.

[^hilbert-1926]: Hilbert D., 1926. “Über das Unendliche,” *Mathematische Annalen*, 95. Translated in J. van Heijenoort (ed.) *From Frege to Gödel: A Source Book in Mathematical Logic, 1879–1931*, Cambridge, MA: Harvard University Press, 1967, pp. 367–392.

[^hodges-1979]: Hodges, W., 1979. “Krull implies Zorn,” *Journal of the London Mathematical Society*, 19: 285–7.

[^howard-1998]: Howard, P. and Rubin, J. E., 1998. *Consequences of the Axiom of Choice*, American Mathematical Society Surveys and Monographs, Vol. 59.

[^howard-1980]: Howard, W. A., 1980. “The formulae-as-types notion of construction,” in J. R. Hindley and J. P. Seldin (eds.), *To H. B. Curry: Essays on Combinatorial Logic. Lambda Calculus and Formalism*, New York and London: Academic Press, pp. 479–490.

[^jacobs-1999]: Jacobs, B., 1999. *Categorical Logic and Type Theory*, Amsterdam: Elsevier.

[^jech-1973]: Jech, T., 1973. *The Axiom of Choice*, Amsterdam: North-Holland.

[^kelley-1950]: Kelley, J.L., 1950. “The Tychonoff product theorem implies the axiom of choice,” *Fundamenta Mathematicae*, 37: 75–76.

[^klimovsky-1958]: Klimovsky, G., 1958. “El teorema de Zorn y la existencia de filtros a ideales maximales en los reticulados distributivos,” *Revista de la Union Matematica Argentina* , 18: 160–64.

[^kuratowski-1922]: Kuratowski, K., 1922. “Une méthode d’élimination des nombres transfinis des raissonements mathématiques,” *Fundamenta Mathematicae*, 3: 76–108.

[^lawvere-2003]: Lawvere, F. W. and Rosebrugh, R., 2003. *Sets for Mathematics*, Cambridge: Cambridge University Press.

[^lindenbaum-1938]: Lindenbaum, A., and Mostowski, A., 1938. “Über die Unabhängigkeit des Auswahlsaxioms und einiger seiner Folgerungen,” *Comptes Rendus des Séances de la Société des Sciences et des Lettres de Varsovie*, 31: 27–32.

[^maietti-2005]: Maietti, M.E., 2005. “Modular correspondence between dependent type theories and categories including pretopoi and topoi,” *Mathematical Structures in Computer Science*, 15/6: 1089–1145.

[^martin-löf-1975]: Martin-Löf, P., 1975. “An Intuitionistic theory of types; predicative part,” in H. E. Rose and J. C. Shepherdson (eds.), *Logic Colloquium 73*, Amsterdam: North-Holland, pp. 73–118.

[^martin-löf-1982]: –––, 1982. “Constructive mathematics and computer programming,” in L. C. Cohen, J. Los, H. Pfeiffer, and K.P. Podewski (eds.), *Logic, Methodology and Philosophy of Science VI*, Amsterdam: North-Holland, pp. 153–179.

[^martin-löf-1984]: –––, 1984. *Intuitionistic Type Theory*, Naples: Bibliopolis.

[^martin-löf-2006]: –––, 2006. “100 years of Zermelo’s axiom of choice: what was the problem with it?,” *The Computer Journal*, 49(3): 345–350.

[^mendelson-1956]: Mendelson, E., 1956. “The independence of a weak axiom of choice,” *Journal of Symbolic Logic*, 21: 350–366.

[^mendelson-1958]: –––, 1958. “The axiom of fundierung and the axiom of choice,” *Arkiv fur Mathematische Logik und Grundlagenforschung*, 4: 67–70.

[^mendelson-1987]: –––, 1987. *Introduction to Mathematical Logic*, CITY: Wadsworth & Brooks, 3rd edition.

[^moore-1982]: Moore, G.H., 1982. *Zermelo’s Axiom of Choice*, Berlin: Springer-Verlag.

[^moore-1932]: Moore, R.L., 1932. *Foundations of Point Set Theory*, Anerican Mathematical Society Colloquium Publications, vol. 13.

[^myhill-1971]: Myhill, J. and Scott, D.S., 1971. “Ordinal definability,” *Axiomatic Set Theory*. Proceedings of Symposia in Pure Mathematics, Vol. XIII, Part I. American Mathematical Society, pp. 271–8.

[^post-1953]: Post, E.L., 1953. “A necessary condition for definability for transfinite von Neumann-Gödel set theory sets, with an application to the problem of the existence of a definable well-ordering of the continuum.” Preliminary Report, *Bulletin of the American Mathematical Society*, 59: 246.

[^ramsey-1926]: Ramsey, F. P., 1926. “The foundations of mathematics,” *Proceedings of the London Mathematical Society*, 25: 338–84. Reprinted in *The Foundations of Mathematics and Other Essays*, D.H. Mellor, ed. London: Routledge, 2001.

[^rubin-1985]: Rubin, H. and Rubin, J. E., 1985. *Equivalents of the Axiom of Choice II*, Amsterdam: North-Holland.

[^rubin-1954]: Rubin, H. and Scott, D.S., 1954. “Some topological theorems equivalent to the prime ideal theorem,” *Bulletin of the American Mathematical Society*, 60: 389.

[^russell-1906]: Russell, B., 1906. “On some difficulties in the theory of transfinite numbers and order types,” *Proceedings of the London Mathematical Society*, 4(2): 29–53.

[^shoenfield-1955]: Shoenfield, J. R., 1955. “The independence of the axiom of choice,” *Journal of Symbolic Logic*, 20: 202.

[^sikorski-1948]: Sikorski, R., 1948. “A theorem on extensions of homomorphisms,” *Annales de la Societé Polonaise de Mathématiques*, 21: 332–35.

[^solovay-1970]: Solovay, R., 1970. “A model of set theory in which every set of reals is Lebesgue measurable,” *Annals of Mathematics*, 92: 1–56.

[^specker-1957]: Specker, E., 1957. “Zur Axiomatik der Mengenlehre (Fundierungs- und Auswahlaxiom),” *Zeit. Math. Logik und Grund.*, 3: 173–210.

[^steinitz-1910]: Steinitz, E., 1910. “Algebraische Theorie der Körper,” *Journal für die Reine und angewandte Mathematik (Crelle)*, 137: 167–309.

[^stone-1936]: Stone, M.H., 1936. “The theory of representations for Boolean algebras,” *Transactions of the American Mathematical Society*, 40: 37–111.

[^tait-1994]: Tait, W. W., 1994. “The law of excluded middle and the axiom of choice,” in *Mathematics and Mind*, A. George (ed.), New York: Oxford University Press, pp. 45–70.

[^takeuti-1961]: Takeuti, G., 1961. “Remarks on Cantor’s Absolute,” *Journal of the Mathematical Society of Japan*, 13: 197–206.

[^tarski-1948]: Tarski, A., 1948. “Axiomatic and algebraic aspects of two theorems on sums of cardinals,” *Fundamenta Mathematicae*, 35: 79–104.

[^tarski-1957]: Tarski, A., and Robert L. Vaught, 1957. “Arithmetical extensions of relational systems,” *Compositio Mathematica*, 13: 81–102. [[Tarski & Vaught 1957 available online](http://www.numdam.org/article/CM_1956-1958__13__81_0.pdf)]

[^teichmuller-1939]: Teichmuller, O., 1939. “Brauch der Algebraiker das Auswahlaxiom?” *Deutsches Mathematik*, 4: 567–577.

[^vitali-1905]: Vitali, G., 1905. *Sul problema della misura dei gruppi di punti di una retta*, Bologna: Tip. Gamberini e Parmeggiani.

[^wagon-1993]: Wagon, S., 1993.*The Banach-Tarski Paradox*, Cambridge University Press.

[^zermelo-1904]: Zermelo, E., 1904. “Neuer Beweis, dass jede Menge Wohlordnung werden kann (Aus einem an Herrn Hilbert gerichteten Briefe)”, *Mathematische Annalen*, 59: 514–16. Translated in J. van Heijenoort (ed.), *From Frege to Gödel: A Source Book in Mathematical Logic, 1879–1931*, Cambridge, MA: Harvard University Press, 1967, pp. 139–141.

[^zermelo-1908]: –––, 1908. Neuer Beweis für die Möglichkeit einer Wohlordnung, *Mathematische Annalen*, 65: 107–128. Translated in J. van Heijenoort (ed.), *From Frege to Gödel: A Source Book in Mathematical Logic, 1879–1931*, Cambridge, MA: Harvard University Press, 1967, pp. 183–198.

[^zermelo-1908a]: –––, 1908a.“Untersuchungen uber die Grundlagen der Mengenlehre,” *Mathematische Annalen*, 65: 107–128. Translated in J. van Heijenoort (ed.), *From Frege to Gödel: A Source Book in Mathematical Logic, 1879–1931*, Cambridge, MA: Harvard University Press, 1967, pp. 199–215.

[^zorn-1935]: Zorn, M., 1935. A remark on method in transfinite algebra, *Bulletin of the American Mathematical Society*, 41: 667–70.
