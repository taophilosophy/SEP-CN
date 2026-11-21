# Category Theory
**First published Fri Dec 6, 1996; substantive revision Thu Aug 29, 2019**

*Marquis, Jean-Pierre*

Category theory has come to occupy a central position in contemporary mathematics and theoretical computer science, and is also applied to mathematical physics. Roughly, it is a general mathematical theory of structures and of systems of structures. As category theory is still evolving, its functions are correspondingly developing, expanding and multiplying. At minimum, it is a powerful language, or conceptual framework, allowing us to see the universal components of a family of structures of a given kind, and how structures of different kinds are interrelated. Category theory is both an interesting object of philosophical study, and a potentially powerful formal tool for philosophical investigations of concepts such as space, system, and even truth. It can be applied to the study of logical systems in which case category theory is called “categorical doctrines” at the syntactic, proof-theoretic, and semantic levels. Category theory even leads to a different theoretical conception of set and, as such, to a possible alternative to the standard set theoretical foundation for mathematics. As such, it raises many issues about mathematical ontology and epistemology. Category theory thus affords philosophers and logicians much to use and reflect upon.

## 1. General Definitions, Examples and Applications

### 1.1 Definitions

Categories are algebraic structures with many complementary natures, e.g., geometric, logical, computational, combinatorial, just as groups are many-faceted algebraic structures. Eilenberg & Mac Lane (1945) introduced categories in a purely auxiliary fashion, as preparation for what they called functors and natural transformations. The very definition of a category evolved over time, according to the author’s chosen goals and metamathematical framework. Eilenberg & Mac Lane at first gave a purely abstract definition of a category, along the lines of the axiomatic definition of a group. Others, starting with Grothendieck (1957)[^grothendieck-1957] and Freyd (1964)[^freyd-1964], elected for reasons of practicality to define categories in set-theoretic terms.

An alternative approach, that of Lawvere (1963, 1966)[^lawvere-1963][^lawvere-1966], begins by characterizing the category of categories, and then stipulates that a category is an object of that universe. This approach, under active development by various mathematicians, logicians and mathematical physicists, lead to what are now called “higher-dimensional categories” (Baez 1997, Baez & Dolan 1998a, Batanin 1998, Leinster 2002, Hermida *et al*. 2000, 2001, 2002)[^baez-1997][^baez-1998a][^batanin-1998][^hermida-2000][^hermida-2001][^hermida-2002][^leinster-2002]. The very definition of a category is not without philosophical importance, since one of the objections to category theory as a foundational framework is the claim that since categories are *defined* as sets, category theory cannot provide a philosophically enlightening foundation for mathematics. We will briefly go over some of these definitions, starting with Eilenberg’s & Mac Lane’s (1945) algebraic definition. However, before going any further, the following definition will be required.

**Definition**: A mapping $e$ will be called an *identity* if and only if the existence of any product $e\alpha$ or $\beta e$ implies that $e\alpha = \alpha$ and $\beta e = \beta$

Here is the original definition of a category.

**Definition** (Eilenberg & Mac Lane 1945)[^eilenberg-1945]: A category $\mathbf{C}$ is an aggregate $\mathbf{Ob}$ of abstract elements, called the *objects* of $\mathbf{C}$, and abstract elements **Map**, called *mappings* of the category. The mappings are subject to the following five axioms:

(C1) Given three mappings $\alpha_1, \alpha_2$ and $\alpha_3$, the triple product $\alpha_3 (\alpha_2\alpha_1)$ is defined if and only if $(\alpha_3\alpha_2)\alpha_1$ is defined. When either is defined, the associative law

$$ \alpha_3 (\alpha_2\alpha_1) = (\alpha_3\alpha_2)\alpha_1 $$

holds. This triple product is written $\alpha_3\alpha_2\alpha_1.$

(C2) The triple product $\alpha_3\alpha_2\alpha_1$ is defined whenever both products $\alpha_3\alpha_2$ and $\alpha_2\alpha_1$ are defined.

(C3) For each mapping *α*, there is at least one identity $e_1$ such that $\alpha e_1$ is defined, and at least one identity $e_2$ such that $e_2\alpha$ is defined.

(C4) The mapping $e_X$ corresponding to each object $X$ is an identity.

(C5) For each identity $e$ there is a unique object $X$ of $\mathbf{C}$ such that $e_X = e.$

As Eilenberg & Mac Lane promptly remark, objects play a secondary role and could be entirely omitted from the definition. Doing so, however, would make the manipulation of the applications less convenient. It is practically suitable, and perhaps psychologically more simple to think in terms of mappings and objects. The term “aggregate” is used by Eilenberg & Mac Lane themselves, presumably so as to remain neutral with respect to the background set theory one wants to adopt.

Eilenberg & Mac Lane defined categories in 1945 for reasons of rigor. As they note:

> It should be observed first that the whole concept of a category is essentially an auxiliary one; our basic concepts are essentially those of a functor and of natural transformation (…). The idea of a category is required only by the precept that every function should have a definite class as domain and a definite class as range, for the categories are provided as the domains and ranges of functors. Thus one could drop the category concept altogether and adopt an even more intuitive standpoint, in which a functor such as “Hom” is not defined over the category of “all” groups, but for each particular pair of groups which may be given. The standpoint would suffice for applications, inasmuch as none of our developments will involve elaborate constructions on the categories themselves. (1945, chap. 1, par. 6, p. 247)

Things changed in the following ten years, when categories started to be used in algebraic topology and homological algebra. Mac Lane, Buchsbaum, Grothendieck and Heller were considering categories in which the collections of morphisms between two fixed objects have an additional structure. More specifically, given any two objects $X$ and $Y$ of a category $\mathbf{C}$, the *set* $\mathbf{Hom}(X, Y)$ of morphisms from $X$ to $Y$ form an abelian group. Furthermore, for reasons related to the ways homology and cohomology theories are linked, the definition of a category had to satisfy an additional formal property (which we will leave aside for the moment): it had to be self-dual. These requirements lead to the following definition.

**Definition**: A category $\mathbf{C}$ can be described as a set $\mathbf{Ob}$, whose members are the objects of $\mathbf{C}$, satisfying the following three conditions:

*Morphism* : For every pair $X, Y$ of objects, there is a set $\mathbf{Hom}(X, Y)$, called the *morphisms* from $X$ to $Y$ in $\mathbf{C}.$ If $\boldsymbol{f}$ is a morphism from $X$ to $Y$, we write $\boldsymbol{f} : X \rightarrow Y.$

*Identity* : For every object $X$, there exists a morphism $\mathbf{id}_X$ in $\mathbf{Hom}(X, X)$, called the *identity* on $X.$

*Composition* : For every triple $X, Y$ and $Z$ of objects, there exists a partial binary operation from $\mathbf{Hom}(X, Y) \times \mathbf{Hom}(Y, Z)$ to $\mathbf{Hom}(X, Z)$, called the composition of morphisms in $\mathbf{C}.$ If $\boldsymbol{f}: X \rightarrow Y$ and $\boldsymbol{g}: Y \rightarrow Z$, the composition of $f$ and $g$ is notated $(\boldsymbol{g} \circ \boldsymbol{f}): X \rightarrow Z.$

Identity, morphisms, and composition satisfy two axioms:

*Associativity* : If $\boldsymbol{f}: X \rightarrow Y, \boldsymbol{g}: Y \rightarrow Z$ and $\boldsymbol{h}: Z \rightarrow W$, then $\boldsymbol{h} \circ (\boldsymbol{g} \circ \boldsymbol{f}) = (\boldsymbol{h} \circ \boldsymbol{g}) \circ \boldsymbol{f}.$

*Identity* : If $\boldsymbol{f}: X \rightarrow Y$, then $(\mathbf{id}_Y \circ \mathbf{f}) = \boldsymbol{f}$ and $(\boldsymbol{f} \circ \id_X) = \boldsymbol{f}.$

This is the definition one finds in most textbooks of category theory. As such it explicitly relies on a set theoretical background and language. An alternative, suggested by Lawvere in the early sixties, is to develop an adequate language and background framework for a category of categories. We will not present the formal framework here, for it would take us too far from our main concern, but the basic idea is to define what are called weak $n$-categories (and weak *ω*-categories), and what had been called categories would then be called weak 1-categories (and sets would be weak 0-categories). (See, for instance, Baez 1997, Makkai 1998, Leinster 2004, Baez & May 2010, Simpson 2011.)[^baez-1997][^baez-2011][^baez-2010][^baez-2010-2][^leinster-2004][^makkai-1998][^simpson-2011]

Also in the sixties, Lambek proposed to look at categories as deductive systems. This begins with the notion of a *graph*, consisting of two classes *Arrows* and *Objects*, and two mappings between them, $\boldsymbol{s}: \Arrows \rightarrow \Objects$ and $\boldsymbol{t}: \Arrows \rightarrow \Objects$, namely the source and the target mappings. The arrows are usually called the “oriented edges” and the objects “nodes” or “vertices”. Following this, a *deductive system* is a graph with a specified arrow:

(R1) $\mathbf{id}_X : X \rightarrow X$,

and a binary operation on arrows:

(R2) Given $\boldsymbol{f}: X \rightarrow Y$ and $\boldsymbol{g}: Y \rightarrow Z$, the composition of $\boldsymbol{f}$ and $\boldsymbol{g}$ is $(\boldsymbol{g} \circ \boldsymbol{f}): X \rightarrow Z.$

Of course, the objects of a deductive system are normally thought of as *formulas*, the arrows are thought of as *proofs* or *deductions*, and operations on arrows are thought of as *rules of inference*. A *category* is then defined thus:

**Definition** (Lambek): A *category* is a deductive system in which the following equations hold between proofs: for all $\boldsymbol{f}: X \rightarrow Y, \boldsymbol{g}: Y \rightarrow Z$ and $\boldsymbol{h}: Z \rightarrow W$,

(E1) $\boldsymbol{f} \circ \id_X = \boldsymbol{f}$,   $\mathbf{id}_Y \circ \boldsymbol{f} = \boldsymbol{f}$,   $\boldsymbol{h} \circ (\boldsymbol{g} \circ \boldsymbol{f}) = (\boldsymbol{h} \circ \boldsymbol{g}) \circ \boldsymbol{f}.$

Thus, by imposing an adequate equivalence relation upon proofs, any deductive system can be turned into a category. It is therefore legitimate to think of a category as an algebraic encoding of a deductive system. This phenomenon is already well-known to logicians, but probably not to its fullest extent. An example of such an algebraic encoding is the Lindenbaum-Tarski algebra, a Boolean algebra corresponding to classical propositional logic. Since a Boolean algebra is a poset, it is also a category. (Notice also that Boolean algebras with appropriate homomorphisms between them form another useful category in logic.) Thus far we have merely a change of vocabulary. Things become more interesting when first-order and higher-order logics are considered. The Lindenbaum-Tarski algebra for these systems, when properly carried out, yields categories, sometimes called “conceptual categories” or “syntactic categories” (Mac Lane & Moerdijk 1992, Makkai & Reyes 1977, Pitts 2000)[^mac-1992][^makkai-1977][^pitts-2000].

### 1.2 Examples

Almost every known example of a mathematical structure with the appropriate structure-preserving map yields a category.

1. The category *Set* with objects sets and morphisms the usual functions. There are variants here: one can consider partial functions instead, or injective functions or again surjective functions. In each case, the category thus constructed is different.
2. The category *Top* with objects topological spaces and morphisms continuous functions. Again, one could restrict morphisms to *open* continuous functions and obtain a different category.
3. The category *hoTop* with objects topological spaces and morphisms equivalence classes of homotopic functions. This category is not only important in mathematical practice, it is at the core of algebraic topology, but it is also a fundamental example of a category in which morphisms are *not* structure preserving functions.
4. The category *Vec* with objects vector spaces and morphisms linear maps.
5. The category *Diff* with objects differential manifolds and morphisms smooth maps.
6. The categories *Pord* and *PoSet* with objects preorders and posets, respectively, and morphisms monotone functions.
7. The categories *Lat* and *Bool* with objects lattices and Boolean algebras, respectively, and morphisms structure preserving homomorphisms, i.e., $(\top , \bot , \wedge , \vee)$ homomorphisms.
8. The category *Heyt* with objects Heyting algebras and $(\top , \bot , \wedge , \vee , \rightarrow)$ homomorphisms.
9. The category *Mon* with objects monoids and morphisms monoid homomorphisms.
10. The category *AbGrp* with objects abelian groups and morphisms group homomorphisms, i.e. $(1, \times, (-)^{-1})$ homomorphisms.
11. The category *Grp* with objects groups and morphisms group homomorphisms, i.e. $(1, \times, (-)^{-1})$ homomorphisms.
12. The category *Rings* with objects rings (with unit) and morphisms ring homomorphisms, i.e. $(0, 1, +, \times)$ homomorphisms.
13. The category *Fields* with objects fields and morphisms fields homomorphisms, i.e. $(0, 1, +, \times)$ homomorphisms.
14. Any deductive system $T$ with objects formulae and morphisms proofs.

These examples nicely illustrates how category theory treats the notion of structure in a uniform manner. Note that a category is characterized by its morphisms, and not by its objects. Thus the category of topological spaces with open maps differs from the category of topological spaces with continuous maps — or, more to the point, the categorical properties of the latter differ from those of the former.

We should underline again the fact that not all categories are made of structured sets with structure-preserving maps. Thus any preordered set is a category. For given two elements $p, q$ of a preordered set, there is a morphism $\boldsymbol{f}: p \rightarrow q$ if and only if $p \le q.$ Hence a preordered set is a category in which there is at most one morphism between any two objects. Any monoid (and thus any group) can be seen as a category: in this case the category has only one object, and its morphisms are the elements of the monoid. Composition of morphisms corresponds to multiplication of monoid elements. That the monoid axioms correspond to the category axioms is easily verified.

Hence the notion of category generalizes those of preorder and monoid. We should also point out that a groupoid has a very simple definition in a categorical context: it is a category in which every morphism is an isomorphism, that is for any morphism $\boldsymbol{f}: X \rightarrow Y$, there is a morphism $\boldsymbol{g}: Y \rightarrow X$ such that $\boldsymbol{f} \circ \boldsymbol{g} = \mathbf{id}_Y$ and $\boldsymbol{g} \circ \boldsymbol{f} = \mathbf{id}_X.$

### 1.3 Fundamental Concepts of the Theory

Category theory unifies mathematical structures in two different ways. First, as we have seen, almost every set theoretically defined mathematical structure with the appropriate notion of homomorphism yields a category. This is a unification provided *within* a set theoretical environment. Second, and perhaps even more important, once a type of structure has been defined, it is imperative to determine how new structures can be constructed out of the given one. For instance, given two sets $A$ and $B$, set theory allows us to construct their Cartesian product $A \times B.$ It is also imperative to determine how given structures can be decomposed into more elementary substructures. For example, given a finite Abelian group, how can it be decomposed into a product of certain of its subgroups? In both cases, it is necessary to know how structures of a certain kind may combine. The nature of these combinations might appear to be considerably different when looked at from a purely set theoretical perspective.

Category theory reveals that many of these constructions are in fact certain objects in a category having a “universal property”. Indeed, from a categorical point of view, a Cartesian product in set theory, a direct product of groups (Abelian or otherwise), a product of topological spaces, and a conjunction of propositions in a deductive system are all instances of a categorical product characterized by a universal property. Formally, a *product* of two objects $X$ and $Y$ in a category $\mathbf{C}$ is an object $Z$ of $\mathbf{C}$ *together* with two morphisms, called the projections, $\boldsymbol{p}: Z \rightarrow X$ and $\boldsymbol{q}: Z \rightarrow Y$ such that—and this is the universal property—for all objects $W$ with morphisms $\boldsymbol{f}: W \rightarrow X$ and $\boldsymbol{g}: W \rightarrow Y$, there is a unique morphism $\boldsymbol{h}: W \rightarrow Z$ such that $\boldsymbol{p} \circ \boldsymbol{h} = \boldsymbol{f}$ and $\boldsymbol{q} \circ \boldsymbol{h} = \boldsymbol{g}.$

Note that we have defined $a$ product for $X$ and $Y$ and not *the* product for $X$ and $Y.$ Indeed, products and other objects with a universal property are defined only up to a (unique) isomorphism. Thus in category theory, the nature of the elements constituting a certain construction is irrelevant. What matters is the way an object is related to the other objects of the category, that is, the morphisms going in and the morphisms going out, or, put differently, how certain structures can be mapped into a given object and how a given object can map its structure into other structures of the same kind.

Category theory reveals how different kinds of structures are related to one another. For instance, in algebraic topology, topological spaces are related to groups (and modules, rings, etc.) in various ways (such as homology, cohomology, homotopy, K-theory). As noted above, groups with group homomorphisms constitute a category. Eilenberg & Mac Lane invented category theory precisely in order to clarify and compare these connections. What matters are the morphisms between categories, given by functors. Informally, functors are structure-preserving maps between categories. Given two categories $\mathbf{C}$ and $\mathbf{D}$, a functor $F$ from $\mathbf{C}$ to $\mathbf{D}$ sends objects of $\mathbf{C}$ to objects of $\mathbf{D}$, and morphisms of $\mathbf{C}$ to morphisms of $\mathbf{D}$, in such a way that composition of morphisms in $\mathbf{C}$ is preserved, i.e., $F(\boldsymbol{g} \circ \boldsymbol{f}) = F(\boldsymbol{g}) \circ F(\boldsymbol{f})$, and identity morphisms are preserved, i.e., $F(\mathbf{id}_X ) = \mathbf{id}_{FX}.$ It immediately follows that a functor preserves commutativity of diagrams between categories. Homology, cohomology, homotopy, K-theory are all example of functors.

A more direct example is provided by the power set operation, which yields two functors on the category of sets, depending on how one defines its action on functions. Thus given a set $X, \wp(X)$ is the usual set of subsets of $X$, and given a function $\boldsymbol{f}: X \rightarrow Y, \wp(\boldsymbol{f}): \wp(X) \rightarrow \wp(Y)$ takes a subset $A$ of $X$ and maps it to $B = \boldsymbol{f}(A)$, the image of $\boldsymbol{f}$ restricted to $A$ in $X.$ It is easily verified that this defines a functor from the category of sets into itself.

In general, there are many functors between two given categories, and the question of how they are connected suggests itself. For instance, given a category $\mathbf{C}$, there is always the identity functor from $\mathbf{C}$ to $\mathbf{C}$ which sends every object/morphism of $\mathbf{C}$ to itself. In particular, there is the identity functor over the category of sets.

Now, the identity functor is related in a natural manner to the power set functor described above. Indeed, given a set $X$ and its power set $\wp(X)$, there is a function $\mathbf{h}_X$ which takes an element $x$ of $X$ and sends it to the singleton set $\{x\}$, a subset of $X$, i.e., an element of $\wp(X).$ This function in fact belongs to a family of functions indexed by the objects of the category of sets $\{\mathbf{h}_Y : Y \rightarrow \wp(X)| Y \text{ in } \mathbf{Ob(Set)}\}.$ Moreover, it satisfies the following commutativity condition: given any function $\boldsymbol{f}: X \rightarrow Y$, the identity functor yields the same function $\boldsymbol{Id}(\boldsymbol{f}): \boldsymbol{Id}(X) \rightarrow \boldsymbol{Id}(Y).$ The commutativity condition thus becomes: $\mathbf{h}_Y \circ \boldsymbol{Id}(\boldsymbol{f}) = \wp(\boldsymbol{f}) \circ \mathbf{h}_X.$ Thus the family of functions $\boldsymbol{h}({\text{-}})$ relates the two functors in a natural manner. Such families of morphisms are called *natural transformations* between functors. Similarly, natural transformations between models of a theory yield the usual homomorphisms of structures in the traditional set theoretical framework.

The above notions, while important, are not fundamental to category *theory*. The latter heading arguably include the notions of limit/colimit; in turn, these are special cases of what is certainly the cornerstone of category theory, the concept of adjoint functors, first defined by Daniel Kan in 1956 and published in 1958.

Adjoint functors can be thought of as being conceptual inverses. This is probably best illustrated by an example. Let $U: \mathbf{Grp} \rightarrow \mathbf{Set}$ be the forgetful functor, that is, the functor that sends to each group $G$ its underlying set of elements $U(G)$, and to a group homomorphism $\boldsymbol{f}: G \rightarrow H$ the underlying set function $U(\boldsymbol{f}): U(G) \rightarrow U(H).$ In other words, $U$ forgets about the group structure and forgets the fact that morphisms are group homomorphisms. The categories $\mathbf{Grp}$ and $\mathbf{Set}$ are certainly not isomorphic, as categories, to one another. (A simple argument runs as follows: the category $\mathbf{Grp}$ has a zero object, whereas $\mathbf{Set}$ does not.) Thus, we certainly cannot find an inverse, in the usual algebraic sense, to the functor $U.$ But there are many non-isomorphic ways to define a group structure on a given set $X$, and one might hope that among these constructions at least one is functorial and systematically related to the functor $U.$ What is the conceptual inverse to the operation of forgetting all the group theoretical structure and obtaining a set? It is to construct a group from a set solely on the basis of the concept of group and nothing else, i.e., with no extraneous relation or data. Such a group is constructed “freely”; that is, with no restriction whatsoever except those imposed by the axioms of the theory. In other words, all that is remembered in the process of constructing a group from a given set is the fact that the resulting construction has to be a group. Such a construction exists; it is functorial and it yields what are called *free groups*. In other words, there is a functor $F: \mathbf{Set} \rightarrow \mathbf{Grp}$, which to any set $X$ assigns the free group $F(X)$ on $X$, and to each function $\boldsymbol{f}: X \rightarrow Y$, the group homomorphism $F(\boldsymbol{f}): F(X) \rightarrow F(Y)$, defined in the obvious manner. The situation can be described thusly: we have two conceptual contexts, a group theoretical context and a set theoretical context, and two functors moving systematically from one context to the other in opposite directions. One of these functors is elementary, namely the forgetful functor $U.$ It is apparently trivial and uninformative. The other functor is mathematically significant and important. The surprising fact is that $F$ is related to $U$ by a simple rule and, in some sense, it arises from $U.$ One of the striking features of adjoint situations is precisely the fact that fundamental mathematical and logical constructions arise out of given and often elementary functors.

The fact that $U$ and $F$ are conceptual inverses expresses itself formally as follows: applying $F$ first and then $U$ does not yield the original set $X$, but there is a fundamental relationship between $X$ and $UF(X).$ Indeed, there is a function *η*: $X \rightarrow UF(X)$, called the *unit of the adjunction*, that simply sends each element of $X$ to itself in $UF(X)$ and this function satisfies the following universal property: given any function $\boldsymbol{g}: X \rightarrow U(G)$, there is a unique *group homomorphism* $\boldsymbol{h}: F(X) \rightarrow G$ such that $U(\boldsymbol{h}) \circ \eta = \boldsymbol{g}.$ In other words, $UF(X)$ is the best possible solution to the problem of inserting elements of $X$ into a group (what is called “insertion of generators” in the mathematical jargon). Composing $U$ and $F$ in the opposite order, we get a morphism $\xi : FU(G) \rightarrow G$, called the *counit of the adjunction*, satisfying the following universal property: for any group homomorphism $\boldsymbol{g}: F(X) \rightarrow G$, there is a unique function $\boldsymbol{h}: X \rightarrow U(G)$ such that $\xi \circ F(\boldsymbol{h}) = \boldsymbol{g}$. In other words, $FU(G)$ constitutes the best possible solution to the problem of finding a representation of $G$ as a quotient of a free group. If $U$ and $F$ were simple algebraic inverses to one another, we would have the following identity: $UF = I_{\mathbf{Set}}$ and $FU = I_{\mathbf{Grp}}$, where $I_{\mathbf{Set}}$ denotes the identity functor on $\mathbf{Set}$ and $I_{\mathbf{Grp}}$ the identity functor on $\mathbf{Grp}.$ As we have indicated, these identities certainly do not hold in this case. However, some identities do hold: they are best expressed with the help of the commutative diagrams:

| $\begin{array}{rcl} U & \xrightarrow{\eta\,\circ\,U} & UFU \\ & \searrow & \downarrow \scriptsize{U \circ \xi} \\ & & U \end{array}$ |   | \\begin{array}{rcl} F & \\xrightarrow{F\\,\\circ\\,\\eta} & FUF \\\\ & \\searrow & \\downarrow \\scriptsize{\\xi \\circ F} \\\\ & & F \\end{array} |
| --- | --- | --- |

where the diagonal arrows denote the appropriate identity natural transformations.

This is but one case of a very common situation: every free construction can be described as arising from an appropriate forgetful functor between two adequately chosen categories. The number of mathematical constructions that can be described as adjoints is simply stunning. Although the details of each one of these constructions vary considerably, the fact that they can all be described using the same language illustrates the profound unity of mathematical concepts and mathematical thinking. Before we give more examples, a formal and abstract definition of adjoint functors is in order.

**Definition**: Let $F: \mathbf{C} \rightarrow \mathbf{D}$ and $G: \mathbf{D} \rightarrow \mathbf{C}$ be functors going in opposite directions. $F$ is a *left adjoint* to $G (G$ a *right adjoint* to $F)$, denoted by $F \dashv G$, if there exists natural transformations $\eta : I_{\mathbf{C}} \rightarrow GF$ and $\xi: FG \rightarrow I_{\mathbf{D}}$, such that the composites

$$ G \xrightarrow{\eta\,\circ\,G} GFG \xrightarrow{G\,\circ\,\xi} G $$

and

$$ F \xrightarrow{F\,\circ\,\eta} FGF \xrightarrow{\xi\,\circ\,F} F $$

are the identity natural transformations. (For different but equivalent definitions, see Mac Lane 1971 or 1998, chap. IV.)[^mac-1971][^mac-1998]

Here are some of the important facts regarding adjoint functors. Firstly, adjoints are unique up to isomorphism; that is any two left adjoints $F$ and $F'$ of a functor $G$ are naturally isomorphic. Secondly, the notion of adjointness is formally equivalent to the notion of a universal morphism (or construction) and to that of representable functor. (See, for instance Mac Lane 1998, chap. IV.)[^mac-1998] Each and every one of these notions exhibit an aspect of a given situation. Thirdly, a left adjoint preserves all the colimits which exist in its domain, and, dually, a right adjoint preserves all the limits which exist in its domain.

We now give some examples of adjoint situations to illustrate the pervasiveness of the notion.

1. Instead of having a forgetful functor going into the category of sets, in some cases only a part of the structure is forgotten. Here are two standard examples:
2. There is an obvious forgetful functor $U$: **AbGrp** $\rightarrow$ **AbMon** from the category of abelian groups to the category of abelian monoids: $U$ forgets about the inverse operation. The functor $U$ has a left adjoint $F$: **AbMon** $\rightarrow$ **AbGrp** which, given an abelian monoid $M$, assigns to it the best possible abelian group $F(M)$ such that $M$ can be embedded in $F(M)$ as a submonoid. For instance, if $M$ is $\mathbb{N}$, then $F(\mathbb{N})$ “is” $\mathbb{Z}$, that is, it is isomorphic to $\mathbb{Z}.$
3. Similarly, there is an obvious forgetful functor $U: \mathbf{Haus} \rightarrow \mathbf{Top}$ from the category of Hausdorff topological spaces to the category of topological spaces which forgets the Hausdorff condition. Again, there is a functor $F: \mathbf{Top} \rightarrow \mathbf{Haus}$ such that $F \dashv U.$ Given a topological space $X, F(X)$ yields the best Hausdorff space constructed from $X$: it is the quotient of $X$ by the closure of the diagonal $\overline{\Delta}_X \subseteq X \times X$, which is an equivalence relation. In contrast with the previous example where we had an embedding, this time we get a quotient of the original structure.
4. Consider now the category of *compact* Hausdorff spaces **kHaus** and the forgetful functor $U$: **kHaus** $\rightarrow \mathbf{Top}$, which forgets the compactness property and the separation property. The left adjoint to this $U$ is the Stone-Cech compactification.
5. There is a forgetful functor $U: \textbf{Mod}_R \rightarrow$ **AbGrp** from a category of $R$-modules to the category of abelian groups, where $R$ is a commutative ring with unit. The functor $U$ forgets the action of $R$ on a group $G.$ The functor $U$ has both a left and a right adjoint. The left adjoint is $R \otimes -$: **AbGrp** $\rightarrow \mathbf{Mod}_R$ which sends an abelian group $G$ to the tensor product $R \otimes G$ and the right adjoint is given by the functor $\mathbf{Hom}(R, -)$: **AbGrp** $\rightarrow \mathbf{Mod}_R$ which assigns to any group $G$ the modules of linear mappings $\mathbf{Hom}(R, G).$
6. The case where the categories $\mathbf{C}$ and $\mathbf{D}$ are posets deserves special attention here. Adjoint functors in this context are usually called *Galois connections*. Let $\mathbf{C}$ be a poset. Consider the diagonal functor $\Delta : \mathbf{C} \rightarrow \mathbf{C} \times \mathbf{C}$, with $\Delta(X) = \langle X, X\rangle$ and for $\boldsymbol{f}: X \rightarrow Y, \Delta(\boldsymbol{f}) = \langle \boldsymbol{f}, \boldsymbol{f}\rangle : \langle X, X\rangle \rightarrow \langle Y, Y\rangle.$ In this case, the left-adjoint to $\Delta$ is the coproduct, or the sup, and the right-adjoint to $\Delta$ is the product, or the inf. The adjoint situation can be described in the following special form: $$ \frac{X \vee Y \le Z}{X \le Z, Y \le Z}\Updownarrow \qquad \frac{Z \le X \wedge Y}{Z \le Y, Z \le X}\Updownarrow $$ where the vertical double arrow can be interpreted as rules of inference going in both directions.
7. Implication can also be introduced. Consider a functor with a parameter: $(- \wedge X): \mathbf{C} \rightarrow \mathbf{C}.$ It can easily be verified that when $\mathbf{C}$ is a poset, the function $(- \wedge X)$ is order preserving and therefore a functor. A right adjoint to $(- \wedge X)$ is a functor that yields the largest element of $\mathbf{C}$ such that its infimum with $X$ is smaller than $Z.$ This element is sometimes called the relative pseudocomplement of $X$ or, more commonly, the *implication*. It is denoted by *X $\Rightarrow$ Z* or by $X \supset Z.$ The adjunction can be presented as follows: $$ \frac{Y \wedge X \le Z}{Y \le X \Rightarrow Z}\Updownarrow $$
8. The negation operator $\neg X$ can be introduced from the last adjunction. Indeed, let $Z$ be the bottom element $\bot$ of the lattice. Then, since $Y \wedge X \le \bot$ is always true, it follows that $Y \le X \Rightarrow \bot$ is also always true. But since $X \Rightarrow \bot \le X$ is always the case, we get at the numerator that $(X \Rightarrow \bot \wedge X) = \bot.$ Hence, $X \Rightarrow \bot$ is the largest element disjoint from $X.$ We can therefore put $\neg X =_{def} X \Rightarrow \bot.$
9. Limits, colimits, and all the fundamental constructions of category theory can be described as adjoints. Thus, products and coproducts are adjoints, as are equalizers, coequalizers, pullbacks and pushouts, etc. This is one of the reasons adjointness is central to category theory itself: because all the fundamental operations of category theory arise from adjoint situations.
10. An *equivalence of categories* is a special case of adjointness. Indeed, if in the above triangular identities the arrows $\eta : I_{\mathbf{C}} \rightarrow GF$ and $\xi : FG \rightarrow I_{\mathbf{D}}$ are natural *isomorphisms*, then the functors $F$ and $G$ constitute an *equivalence* of categories. In practice, it is the notion of equivalence of categories that matters and not the notion of isomorphism of categories.

It is easy to prove certain facts about these operations directly from the adjunctions. Consider, for instance, implication. Let $Z = X.$ Then we get at the numerator that $Y \wedge X \le X$, which is always true in a poset (as is easily verified). Hence, $Y \le X \Rightarrow X$ is also true for all $Y$ and this is only possible if $X \Rightarrow X = \top$, the top element of the lattice. Not only can logical operations be described as adjoints, but they naturally arise as adjoints to basic operations. In fact, adjoints can be used to define various structures, distributive lattices, Heyting algebras, Boolean algebras, etc. (See Wood, 2004.)[^wood-2004] It should be clear from the simple foregoing example how the formalism of adjointness can be used to give syntactic presentations of various logical theories. Furthermore, and this is a key element, the standard universal and existential quantifiers can be shown to be arising as adjoints to the operation of substitution. Thus, quantifiers are on a par with the other logical operations, in sharp contrast with the other algebraic approaches to logic. (See, for instance Awodey 1996 or Mac Lane & Moerdijk 1992.)[^awodey-1996][^mac-1992] More generally, Lawvere showed how syntax and semantics are related by adjoint functors. (See Lawvere 1969b.)[^lawvere-1969b]

Dualities play an important role in mathematics and they can be described with the help of equivalences between categories. In other words, many important mathematical theorems can be translated as statements about the existence of adjoint functors, sometimes satisfying additional properties. This is sometimes taken as expressing the *conceptual* content of the theorem. Consider the following fundamental case: let $\mathbf{C}$ be the category whose objects are the locally compact abelian groups and the morphisms are the continuous group homomorphisms. Then, the Pontryagin duality theorem amounts to the claim that the category $\mathbf{C}$ is equivalent to the category $\mathbf{C}$°, that is, to the opposite category. Of course, the precise statement requires that we describe the functors $F: \mathbf{C} \rightarrow \mathbf{C}$° and $G: \mathbf{C}$° $\rightarrow \mathbf{C}$ and prove that they constitute an equivalence of categories.

Another well known and important duality was discovered by Stone in the thirties and now bears his name. In one direction, an arbitrary Boolean algebra yields a topological space, and in the other direction, from a (compact Hausdorff and totally disconnected) topological space, one obtains a Boolean algebra. Moreover, this correspondence is functorial: any Boolean homomorphism is sent to a continuous map of topological spaces, and, conversely, any continuous map between the spaces is sent to a Boolean homomorphism. In other words, there is an equivalence of categories between the category of Boolean algebras and the dual of the category of Boolean spaces (also called Stone spaces). (See Johnstone 1982 for an excellent introduction and more developments.)[^johnstone-1982] The connection between a category of algebraic structures and the opposite of a category of topological structures established by Stone’s theorem constitutes but one example of a general phenomenon that did attract and still attracts a great deal of attention from category theorists. Categorical study of duality theorems is still a very active and significant field, and is largely inspired by Stone’s result. (For recent applications in logic, see, for instance Makkai 1987, Taylor 2000, 2002a, 2002b, Caramello 2011.)[^caramello-2011][^makkai-1987]

## 2. Brief Historical Sketch

It is difficult to do justice to the short but intricate history of the field. In particular it is not possible to mention all those who have contributed to its rapid development. With this word of caution out of the way, we will look at some of the main historical threads.

Categories, functors, natural transformations, limits and colimits appeared almost out of nowhere in a paper by Eilenberg & Mac Lane (1945) entitled “General Theory of Natural Equivalences.” We say “almost,” because their earlier paper (1942) contains specific functors and natural transformations at work, limited to groups. A desire to clarify and abstract their 1942 results led Eilenberg & Mac Lane to devise category theory. The central notion at the time, as their title indicates, was that of natural transformation. In order to give a general definition of the latter, they defined functor, borrowing the term from Carnap, and in order to define functor, they borrowed the word ‘category’ from the philosophy of Aristotle, Kant, and C. S. Peirce, but redefining it mathematically.

After their 1945 paper, it was not clear that the concepts of category theory would amount to more than a convenient language; this indeed was the status quo for about fifteen years. Category theory was employed in this manner by Eilenberg & Steenrod (1952), in an influential book on the foundations of algebraic topology, and by Cartan & Eilenberg (1956)[^eilenberg-1956], in a ground breaking book on homological algebra. (Curiously, although Eilenberg & Steenrod defined categories, Cartan & Eilenberg simply assumed them!) These books allowed new generations of mathematicians to learn algebraic topology and homological algebra directly in the categorical language, and to master the method of diagrams. Indeed, without the method of diagram chasing, many results in these two books seem inconceivable, or at the very least would have required a considerably more intricate presentation.

The situation changed radically with Grothendieck’s (1957)[^grothendieck-1957] landmark paper entitled “Sur quelques points d’algèbre homologique”, in which the author employed categories intrinsically to define and construct more general theories which he (Grothendieck 1957)[^grothendieck-1957] then applied to specific fields, e.g., to algebraic geometry. Kan (1958)[^kan-1958] showed that adjoint functors subsume the important concepts of limits and colimits and could capture fundamental concepts in other areas (in his case, homotopy theory).

At this point, category theory became more than a convenient language, by virtue of two developments.

1. Employing the axiomatic method and the language of categories, Grothendieck (1957)[^grothendieck-1957] defined in an abstract fashion types of categories, e.g., additive and Abelian categories, showed how to perform various constructions in these categories, and proved various results about them. (It should be pointed out that Mac Lane in his 1950 paper had made a previous attempt which introduced certain key ideas, for instance using arrows to define certain fundamental concepts and that Buchsbaum had essentially introduced the notion of an abelian category independently under the name of “exact category” in 1955.) In a nutshell, Grothendieck showed how to develop part of homological algebra in an abstract setting of this sort. From then on, a specific category of structures, e.g., a category of sheaves over a topological space $X$, could be seen as a token of an abstract category of a certain type, e.g., an Abelian category. One could therefore immediately see how the methods of, e.g., homological algebra could be applied to, for instance, algebraic geometry. Furthermore, it made sense to look for other types of abstract categories, ones that would encapsulate the fundamental and formal aspects of various mathematical fields in the same way that Abelian categories encapsulated fundamental aspects of homological algebra.
2. Thanks in large part to the efforts of Freyd and Lawvere, category theorists gradually came to see the pervasiveness of the concept of adjoint functors. Not only does the existence of adjoints to given functors permit definitions of abstract categories (and presumably those which are defined by such means have a privileged status) but as we mentioned earlier, many important theorems and even theories in various fields can be seen as equivalent to the existence of specific functors between particular categories. By the early 1970s, the concept of adjoint functors was seen as central to category theory.

With these developments, category theory became an autonomous field of research, and pure category theory could be developed. And indeed, it did grow rapidly as a discipline, but also in its applications, mainly in its source contexts, namely algebraic topology and homological algebra, but also in algebraic geometry and, after the appearance of Lawvere’s Ph.D. thesis, in universal algebra. This thesis also constitutes a landmark in this history of the field, for in it Lawvere proposed the category of categories as a foundation for category theory, set theory and, thus, the whole of mathematics, as well as using categories for the study of the logical aspects of mathematics.

Over the course of the 1960s, Lawvere outlined the basic framework for an entirely original approach to logic and the foundations of mathematics. He achieved the following:

- Axiomatized the category of sets (Lawvere 1964)[^lawvere-1964] and of categories (Lawvere 1966)[^lawvere-1966];
- Gave a categorical description of theories that was independent of syntactical choices and sketched how completeness theorems for logical systems could be obtained by categorical methods (Lawvere 1967);
- Characterized Cartesian closed categories and showed their connections to logical systems and various logical paradoxes (Lawvere 1969);
- Showed that the quantifiers and the comprehension schemes could be captured as adjoint functors to given elementary operations (Lawvere 1966, 1969, 1970, 1971)[^lawvere-1966][^lawvere-1970][^lawvere-1971];
- Argued that adjoint functors should generally play a major foundational role through the notion of “categorical doctrines” (Lawvere 1969).

Meanwhile, Lambek (1968, 1969, 1972)[^lambek-1968][^lambek-1969][^lambek-1972] described categories in terms of deductive systems and employed categorical methods for proof-theoretical purposes.

All this work culminated in another notion, thanks to Grothendieck and his school: that of a *topos*. Even though toposes appeared in the 1960s, in the context of algebraic geometry, again from the mind of Grothendieck, it was certainly Lawvere and Tierney’s (1972)[^tierney-1972] elementary axiomatization of a topos which gave impetus to its attaining foundational status. Very roughly, an elementary topos is a category possessing a logical structure sufficiently rich to develop most of “ordinary mathematics”, that is, most of what is taught to mathematics undergraduates. As such, an elementary topos can be thought of as a categorical theory of sets. But it is also a generalized topological space, thus providing a direct connection between logic and geometry. (For more on the history of categorical logic, see Marquis & Reyes 2012, Bell 2005.)[^bell-2005][^marquis-2012]

The 1970s saw the development and application of the topos concept in many different directions. The very first applications outside algebraic geometry were in set theory, where various independence results were recast in terms of topos (Tierney 1972, Bunge 1974, but also Blass & Scedrov 1989, Blass & Scedrov 1992, Freyd 1980, Mac Lane & Moerdijk 1992, Scedrov 1984)[^blass-1989][^blass-1992][^bunge-1974][^freyd-1980][^mac-1992][^moerdijk-1984][^scedrov-1984][^tierney-1972]. Connections with intuitionistic and, more generally constructive mathematics were noted early on, and toposes are still used to investigate models of various aspects of intuitionism and constructivism (Lambek & Scott 1986, Mac Lane & Moerdijk 1992, Van der Hoeven & Moerdijk 1984a, 1984b, 1984c, Moerdijk 1984, Moerdijk 1995a, Moerdijk 1998, Moerdijk & Palmgren 1997, Moerdijk & Palmgren 2002, Palmgren 2012, Palmgren 2018. For more on the history of topos theory, see McLarty 1992 and Bell 2012)[^bell-2012][^lambek-1986][^lambek-1986-2][^mac-1992][^mclarty-1992][^moerdijk-1984][^moerdijk-1995a][^moerdijk-1998][^moerdijk-1997][^moerdijk-2002][^palmgren-2012][^palmgren-2018][^van-1984a][^van-1984b][^van-1984c].

More recently, topos theory has been employed to investigate various forms of constructive mathematics or set theory (Joyal & Moerdijk 1995, Taylor 1996, Awodey 2008)[^awodey-2008][^joyal-1995][^joyal-1996][^taylor-1996], recursiveness, and models of higher-order type theories generally. The introduction of the so-called “effective topos” and the search for axioms for synthetic domain theory are worth mentioning (Hyland 1982, Hyland 1988, 1991, Hyland *et al*. 1990, McLarty 1992, Jacobs 1999, Van Oosten 2008, Van Oosten 2002 and the references therein)[^hyland-1982][^hyland-1988][^hyland-1991][^hyland-1990][^jacobs-1999][^mclarty-1992][^van-2002][^van-2008]. Lawvere’s early motivation was to provide a new foundation for differential geometry, a lively research area which is now called “synthetic differential geometry” (Lawvere 2000, 2002, Kock 2006, Bell 1988, 1995, 1998, 2001, Moerdijk & Reyes 1991)[^bell-1988][^bell-1988-2][^bell-1995][^bell-1998][^bell-2001][^kock-2006][^lawvere-2000][^lawvere-2002][^moerdijk-1991][^reyes-1991][^reyes-1991-2]. This is only the tip of the iceberg; toposes could prove to be for the 21st century what Lie groups were to the 20th century.

From the 1980s to the present, category theory has found new applications. In theoretical computer science, category theory is now firmly rooted, and contributes, among other things, to the development of new logical systems and to the semantics of programming. (Pitts 2000, Plotkin 2000, Scott 2000, and the references therein)[^pitts-2000][^plotkin-2000][^scott-2000]. Its applications to mathematics are becoming more diverse, even touching on theoretical physics, which employs higher-dimensional category theory — which is to category theory what higher-dimensional geometry is to plane geometry — to study the so-called “quantum groups” and quantum field theory (Majid 1995, Baez & Dolan 2001 and other publications by these authors)[^baez-2001][^majid-1995].

## 3. Philosophical Significance

Category theory challenges philosophers in two ways, which are not necessarily mutually exclusive. On the one hand, it is certainly the task of philosophy to clarify the general epistemological and ontological status of categories and categorical methods, both in the practice of mathematics and in the foundational landscape. On the other hand, philosophers and philosophical logicians can employ category theory and categorical logic to explore philosophical and logical problems. I now discuss these challenges, briefly, in turn.

Category theory is now a common tool in the mathematician’s toolbox; that much is clear. It is also clear that category theory organizes and unifies much of mathematics. Contemporary mathematical fields would not be what they are without category theory, for instance algebraic topology, homological algebra, homotopy theory and homotopical algebra, representation theory, arithmetic geometry and algebraic geometry. (See for instance Mac Lane 1971, 1998 or Pedicchio & Tholen 2004.)[^mac-1971][^mac-1998][^pedicchio-2004] No one will deny these simple facts. Furthermore, vast portions of contemporary mathematics now rest on a different practice which rely, in large part, on the manipulation of new graphical notations, on the one hand, and on different levels of abstraction, on the other hand. It is not simply that category theory and the mathematical disciplines developed within that framework use commutative diagrams, although this in itself leads to some interesting philosophical explorations, as for instance in De Toffoli 2017, but category theorists have seen the need to develop systematic and formal graphical languages to express directly various forms of argumentations. (See, for instance, Joyal & Street 1993; Joyal, Street & Verity 1996; Fong & Spivak 2019, Other Internet Resources.)[^joyal-1993][^joyal-1996] Whereas since Bourbaki, mathematics was done “up to isomorphism”, in some cases, it is now done “up to equivalence” or up to “bi-equivalence” or even up to “n-equivalence”. (For an attempt at clarifying what these levels of abstraction mean, see Marquis 2014, Marquis 2016.)[^marquis-2014][^marquis-2016]

Doing mathematics in a categorical framework is almost always radically different from doing it in a set-theoretical framework (the exception being working with the internal language of a Boolean topos; whenever the topos is not Boolean, then the main difference lies in the fact that the logic is *intuitionistic*). Hence, as is often the case when a different conceptual framework is adopted, many basic issues regarding the nature of the objects studied, the nature of the knowledge involved, and the nature of the methods used have to be reevaluated. We will take up these three aspects in turn.

Two facets of the nature of mathematical objects within a categorical framework have to be emphasized. First, objects are always given in a category. An object exists in and depends upon an ambient category. Furthermore, an object is characterized by the morphisms going in it and/or the morphisms coming out of it. Second, objects are always characterized up to isomorphism (in the best cases, up to a unique isomorphism). There is no such thing, for instance, as *the* natural numbers. However, it can be argued that there is such a thing as *the concept* of natural numbers. Indeed, the concept of natural numbers can be given unambiguously, via the Dedekind-Peano-Lawvere axioms, but what this concept refers to in specific cases depends on the context in which it is interpreted, e.g., the category of sets or a topos of sheaves over a topological space. Thus, it seems that sense does not determine reference in a categorical context. It is hard to resist the temptation to think that category theory embodies a form of structuralism, that it describes mathematical objects as structures since the latter, presumably, are always characterized up to isomorphism. Thus, the key here has to do with the kind of criterion of identity at work within a categorical framework and how it resembles any criterion given for objects which are thought of as forms in general. One of the standard objections presented against this view is that if objects are thought of as structures and only as *abstract* structures, meaning here that they are separated from any specific or concrete representation, then it is impossible to locate them within the mathematical universe. (See Hellman 2003 for a standard formulation of the objection, McLarty 1993, Awodey 2004, Landry & Marquis 2005, Shapiro 2005, Landry 2011, Linnebo & Pettigrew 2011, Hellman 2011, Shapiro 2011, McLarty 2011, Logan 2015 for relevant material on the issue.)[^awodey-2004][^hellman-2003][^hellman-2011][^landry-2011][^landry-2005][^linnebo-2011][^logan-2015][^mclarty-1993][^mclarty-2004][^mclarty-2005][^mclarty-2011][^shapiro-2005][^shapiro-2011]

A slightly different way to make sense of the situation is to think of mathematical objects as *types* for which there are tokens given in different contexts. This is strikingly different from the situation one finds in set theory, in which mathematical objects are defined uniquely and their reference is given directly. Although one can make room for types within set theory via equivalence classes or isomorphism types in general, the *basic* criterion of identity within that framework is given by the axiom of extensionality and thus, ultimately, reference is made to specific sets. Furthermore, it can be argued that the relation between a type and its token is *not* represented adequately by the membership relation. A token does not belong to a type, it is not an element of a type, but rather it is an instance of it. In a categorical framework, one always refers to a *token* of a type, and what the theory characterizes directly is the type, not the tokens. In this framework, one does not have to locate a type, but tokens of it are, at least in mathematics, epistemologically required. This is simply the reflection of the interaction between the abstract and the concrete in the epistemological sense (and not the ontological sense of these latter expressions.) (See Ellerman 1988, Ellerman 2017, Marquis 2000, Marquis 2006, Marquis 2013.)[^ellerman-1988][^ellerman-2017][^marquis-2000][^marquis-2006][^marquis-2013]

The history of category theory offers a rich source of information to explore and take into account for an historically sensitive epistemology of mathematics. It is hard to imagine, for instance, how algebraic geometry and algebraic topology could have become what they are now without categorical tools. (See, for instance, Carter 2008, Corfield 2003, Krömer 2007, Marquis 2009, McLarty 1994, McLarty 2006.)[^carter-2008][^krömer-2007][^marquis-2006][^marquis-2009][^mclarty-1994][^mclarty-2006] Category theory has lead to reconceptualizations of various areas of mathematics based on purely abstract foundations. Moreover, when developed in a categorical framework, traditional boundaries between disciplines are shattered and reconfigured; to mention but one important example, topos theory provides a direct bridge between algebraic geometry and logic, to the point where certain results in algebraic geometry are directly translated into logic and vice versa. Certain concepts that were geometrical in origin are more clearly seen as logical (for example, the notion of coherent topos). Algebraic topology also lurks in the background. (See, for instance, Caramello 2018 for a systematic exploitation of the idea of toposes as bridges in mathematics.)[^caramello-2018] On a different but important front, it can be argued that the distinction between mathematics and metamathematics cannot be articulated in the way it has been. All these issues have to be reconsidered and reevaluated.

Moving closer to mathematical practice, category theory allowed for the development of methods that have changed and continue to change the face of mathematics. It could be argued that category theory represents the culmination of one of deepest and most powerful tendencies in twentieth century mathematical thought: the search for the most general and abstract ingredients in a given situation. Category theory is, in this sense, the legitimate heir of the Dedekind-Hilbert-Noether-Bourbaki tradition, with its emphasis on the axiomatic method and algebraic structures. (For a different reading, see Rodin 2014.)[^rodin-2014] When used to characterize a specific mathematical domain, category theory reveals the frame upon which that area is built, the overall structure presiding to its stability, strength and coherence. The structure of this specific area, in a sense, might not need to rest on anything, that is, on some solid soil, for it might very well be just one part of a larger network that is without any Archimedean point, as if floating in space. To use a well-known metaphor: from a categorical point of view, Neurath’s ship has become a spaceship.

Still, it remains to be seen whether category theory should be “on the same plane,” so to speak, as set theory, whether it should be taken as a serious alternative to set theory as a foundation for mathematics, or whether it is foundational in a different sense altogether. (That this very question applies even more forcefully to topos theory will not detain us.)

Lawvere from early on promoted the idea that a category of categories could be used as a foundational framework. (See Lawvere 1964, 1966.)[^lawvere-1964][^lawvere-1966] This proposal now rests in part on the development of higher-dimensional categories, also called weak $n$-categories. (See, for instance Makkai 1998.)[^makkai-1998] The advent of topos theory in the seventies brought new possibilities. Mac Lane has suggested that certain toposes be considered as a genuine foundation for mathematics. (See Mac Lane 1986.)[^mac-1986] Lambek proposed the so-called free topos as the best possible framework, in the sense that mathematicians with different philosophical outlooks might nonetheless agree to adopt it. (See Couture & Lambek 1991, 1992, Lambek 1994.)[^couture-1991][^couture-1992] He has also argued that there is no topos that can thoroughly satisfy a classical mathematician. (See Lambek 2004.)[^lambek-2004] (For more on the various foundational views among category theorists, see Landry & Marquis 2005.)[^landry-2005]

Arguments have been advanced for and against category theory as a foundational framework. (Blass 1984 surveys the relationships between category theory and set theory. Feferman 1977, Bell 1981, and Hellman 2003 argue against category theory. See Marquis 1995 for a quick overview and proposal and McLarty 2004 and Awodey 2004 for replies to Hellman 2003.)[^awodey-2004][^bell-1981][^blass-1984][^feferman-1977][^hellman-2003][^marquis-1995][^mclarty-2004] The debate has advanced slowly but surely. It has been recognized that it is possible to present a foundational framework in the language of category theory, be it in the form of the Elementary Theory of the Category of Sets, ETCS, or a category of categories, of Makkai Structuralist foundations for abstract mathematics, SFAM. Thus, it seems that the community no longer question the logical and the conceptual autonomy of these approaches, to use the terminology introduced by Linnebo & Pettigrew 2011. The main issue seems to be whether one can provide a philosophically satisfying justification for one of those framework. (See Hellman 2013, Landry 2013, Marquis 2013b, McLarty 2018.)[^hellman-2013][^landry-2013][^landry-2018][^marquis-2013b][^mclarty-2018]

This matter is further complicated by the fact that the foundations of category theory itself have yet to be clarified. For there may be many different ways to think of a universe of higher-dimensional categories as a foundations for mathematics. It is safe to say that we now have a good understanding of what are called $(\infty, 1)$-categories and important mathematical results have been obtained in that framework. (See, for instance, Cisinski 2019 for a presentation.)[^cisinski-2019] An adequate language for the universe of arbitrary higher-dimensional categories still has to be presented together with definite axioms for mathematics. (See Makkai 1998 for a short description of such a language. A different approach based on homotopy theory but with closed connections with higher-dimensional categories has been proposed by Voevodsky et al. and is being vigorously pursued. See the book *Homotopy Type Theory*, by Awodey et al. 2013.)[^awodey-2013][^makkai-1998]

It is an established fact that category theory is employed to study logic and philosophy. Indeed, categorical logic, the study of logic by categorical means, has been under way for about 40 years now and still vigorous. Some of the philosophically relevant results obtained in categorical logic are:

- The hierarchy of categorical doctrines: regular categories, coherent categories, Heyting categories and Boolean categories; all these correspond to well-defined logical systems, together with deductive systems and completeness theorems; they suggest that logical notions, including quantifiers, arise naturally in a specific order and are not haphazardly organized (see Walsh 2017 for a philosophical justification of logical connectives using category theory and Halvorson & Tsementzis 2018 for a look from the point of view of scientific theories)[^walsh-2017];
- Joyal’s generalization of Kripke-Beth semantics for intuitionistic logic to sheaf semantics (Lambek & Scott 1986, Mac Lane & Moerdijk 1992)[^lambek-1986][^lambek-1986-2][^mac-1992];
- Coherent and geometric logic, so-called, whose practical and conceptual significance has yet to be explored (Makkai & Reyes 1977, Mac Lane & Moerdiejk 1992, Johnstone 2002, Caramello 2011b, 2012a)[^caramello-2012a][^mac-1992][^makkai-1977];
- The notions of generic model and classifying topos of a theory (Makkai & Reyes 1977, Boileau & Joyal 1981, Bell 1988, Mac Lane & Moerdijk 1992, Johnstone 2002, Caramello 2012b)[^bell-1988][^bell-1988-2][^boileau-1981][^caramello-2012b][^mac-1992][^makkai-1988][^makkai-1977][^moerdijk-2002];
- The notion of strong conceptual completeness and the associated theorems (Makkai & Reyes 1977, Butz & Moerdijk 1999, Makkai 1981, Pitts 1989, Johnstone 2002)[^makkai-1999][^makkai-1989][^makkai-1977][^moerdijk-2002][^pitts-1989][^pitts-1989-2];
- Geometric proofs of the independence of the continuum hypothesis and other strong axioms of set theory (Tierney 1972, Bunge 1974, Freyd 1980, 1987, Blass & Scedrov 1983, 1989, 1992, Mac Lane & Moerdijk 1992)[^blass-1983][^blass-1989][^blass-1992][^bunge-1974][^freyd-1980][^freyd-1987][^freyd-1987-2][^mac-1992][^tierney-1972];
- Models and development of constructive mathematics (see bibliography below);
- Synthetic differential geometry, an alternative to standard and non-standard analysis (Kock 1981, Bell 1998, 2001, 2006)[^bell-1998][^bell-2001][^kock-2006];
- The construction of the so-called effective topos, in which every function on the natural numbers is recursive (McLarty 1992, Hyland 1982, 1991, Van Oosten 2002, Van Oosten 2008)[^hyland-1982][^hyland-1991][^hyland-2002][^mclarty-1991][^mclarty-1992][^van-2002][^van-2008];
- Categorical models of linear logic, modal logic, fuzzy sets, and general higher-order type theories (Reyes 1991, Reyes & Zawadoski 1993, Reyes & Zolfaghari 1991, 1996, Makkai & Reyes 1995, Ghilardi & Zawadowski 2002, Rodabaugh & Klement 2003, Jacobs 1999, Taylor 1999, Johnstone 2002, Blute & Scott 2004, Awodey & Warren 2009, Awodey et al. 2013, Kishida 2018, Cockett &Seely 2018)[^awodey-2013][^awodey-2009][^blute-2004][^cockett-2018][^ghilardi-2002][^jacobs-1999][^kishida-2018][^makkai-1995][^reyes-1991][^reyes-1993][^reyes-1991-2][^reyes-1996][^taylor-1999];
- A graphical syntax called “sketches” (Barr & Wells 1985, 1999, Makkai 1997a, 1997b, 1997c, Johnstone 2002)[^barr-1985][^barr-1999][^makkai-1997a][^makkai-1997b][^makkai-1997c].
- Quantum logic, the foundations of quantum physics and quantum field theory (Brunetti et al. 2003, Abramsky & Duncan 2006, Heunen et al. 2009, Baez & Stay 2010, Baez & Lauda 2011, Coecke 2011, Isham 2011, Döring 2011, Eva 2017, Coecke & Kissinger 2018)[^abramsky-2006][^baez-2011][^baez-2010][^baez-2010-2][^brunetti-2003][^coecke-2011][^coecke-2018][^döring-2011][^eva-2017][^heunen-2009][^isham-2011].

Categorical tools in logic offer considerable flexibility, as is illustrated by the fact that almost all the surprising results of constructive and intuitionistic mathematics can be modeled in a proper categorical setting. At the same time, the standard set-theoretic notions, e.g. Tarski’s semantics, have found natural generalizations in categories. Thus, categorical logic has roots in logic as it was developed in the twentieth century, while at the same time providing a powerful and novel framework with numerous links to other parts of mathematics.

Category theory also bears on more general philosophical questions. From the foregoing disussion, it should be obvious that category theory and categorical logic ought to have an impact on almost all issues arising in philosophy of logic: from the nature of identity criteria to the question of alternative logics, category theory always sheds a new light on these topics. Similar remarks can be made when we turn to ontology, in particular formal ontology: the part/whole relation, boundaries of systems, ideas of space, etc. Ellerman (1988)[^ellerman-1988] has bravely attempted to show that category theory constitutes a theory of universals, one having properties radically different from set theory, which is also seen as a theory of universals. Moving from ontology to cognitive science, MacNamara & Reyes (1994) have tried to employ categorical logic to provide a different logic of reference. In particular, they have attempted to clarify the relationships between count nouns and mass terms. Other researchers are using category theory to study complex systems, cognitive neural networks, and analogies. (See, for instance, Ehresmann 2018, Ehresmann & Vanbremeersch 1987, 2007, Healy 2000, Healy & Caudell 2006, Arzi-Gonczarowski 1999, Brown & Porter 2006.)[^brown-2006][^ehresmann-2018][^ehresmann-2007][^ehresmann-1987][^healy-2000][^healy-2006] Finally, philosophers of science have turned to category theory to shed a new light on issues related to structuralism in science. (See, for instance, Brading & Landry 2006, Bain 2013, Lam & Wüthrich 2015, Eva 2016, Lal & Teh 2017, Landry 2007, 2012, 2018.)[^bain-2013][^brading-2006][^eva-2016][^eva-2017][^lal-2017][^lam-2015][^landry-2007][^landry-2012][^landry-2013][^landry-2018][^landry-2017]

Category theory offers thus many philosophical challenges, challenges which will hopefully be taken up in years to come.

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=category-theory). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/category-theory/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=category-theory&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/category-theory/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

- Cheng, E. & Lauda, A., 2004, [*Higher-Dimensional Categories: an illustrated guide book*](http://eugeniacheng.com/wp-content/uploads/2017/02/cheng-lauda-guidebook.pdf).
- Fong, B. and Spivak, D., 2019, “[Graphical Regular Logic](https://arxiv.org/pdf/1812.05765v2.pdf)”, available at arXiv.org.
- [The category theory mailing list](http://www.mta.ca/~cat-dist/) (with many links and useful information)
- [The n-category Cafe, A blog on higher-dimensional categories, physics and philosophy](http://golem.ph.utexas.edu/category/)
- [The nLab](https://ncatlab.org/nlab/show/HomePage/) (an open access resource on categories and higher-dimensional categories)
- [Logic Matters](https://www.logicmatters.net/categories/) Peter Smith’s blog on logic. It contains a page on category theory with many references and discussions.
- [The Catsters’ Category Theory Videos, introducing the basic concepts of category theory](https://www.youtube.com/watch?v=yeQcmxM2e5I&list=PLlGXNwjYhXYxKVa67r0pKuYufECy713bv/)
- [Math3Ma](https://www.math3ma.com/categories/) A math blog that contains introductions to the main concepts of category theory, set theory and other mathematical topics

## Related Entries

logic: classical | mathematics, philosophy of | set theory

[^readers-nd]: Readers may find the following useful:

[^programmatic-nd]: [Programmatic Reading Guide](category-theory.bib.md)

[^programmatic-nd-2]: The citations in this guide and in the text above can all be found in the list below.

[^abramsky-2006]: Abramsky, S. & Duncan, R., 2006, “A Categorical Quantum Logic”, *Mathematical Structures in Computer Science*, 16 (3): 469–489.

[^adamek-1990]: Adamek, J. *et al*., 1990, *Abstract and Concrete Categories: The Joy of Cats*, New York: Wiley.

[^adamek-1994]: Adamek, J. *et al*., 1994, Locally Presentable and Accessible Categories, Cambridge: Cambridge University Press.

[^arzi-gonczaworski-1999]: Arzi-Gonczaworski, Z., 1999, “Perceive This as That — Analogies, Artificial Perception, and Category Theory”, *Annals of Mathematics and Artificial Intelligence*, 26 (1): 215–252.

[^awodey-1996]: Awodey, S., 1996, “Structure in Mathematics and Logic: A Categorical Perspective”, *Philosophia Mathematica*, 3: 209–237.

[^awodey-2004]: –––, 2004, “An Answer to Hellman’s Question: Does Category Theory Provide a Framework for Mathematical Structuralism”, *Philosophia Mathematica*, 12: 54–64.

[^awodey-2006]: –––, 2006, *Category Theory*, Oxford: Clarendon Press.

[^awodey-2007]: –––, 2007, “Relating First-Order Set Theories and Elementary Toposes”, *The Bulletin of Symbolic*, 13 (3): 340–358.

[^awodey-2008]: –––, 2008, “A Brief Introduction to Algebraic Set Theory”, *The Bulletin of Symbolic*, 14 (3): 281–298.

[^awodey-2013]: Awodey, S., et al., 2013, *Homotopy Type Theory: Univalent Foundations of Mathematics*, The Univalent Foundations Program.

[^awodey-2000]: Awodey, S. & Butz, C., 2000, “Topological Completeness for Higher Order Logic”, *Journal of Symbolic Logic*, 65 (3): 1168–1182.

[^awodey-2002]: Awodey, S. & Reck, E. R., 2002, “Completeness and Categoricity I. Nineteen-Century Axiomatics to Twentieth-Century Metalogic”, *History and Philosophy of Logic*, 23 (1): 1–30.

[^awodey-2002-2]: –––, 2002, “Completeness and Categoricity II. Twentieth-Century Metalogic to Twenty-first-Century Semantics”, *History and Philosophy of Logic*, 23 (2): 77–94.

[^awodey-2009]: Awodey, S. & Warren, M., 2009, “Homotopy theoretic Models of Identity Types”, *Mathematical Proceedings of the Cambridge Philosophical Society*, 146 (1): 45–55.

[^baez-1997]: Baez, J., 1997, “An Introduction to $n$-Categories”, *Category Theory and Computer Science*, Lecture Notes in Computer Science (Volume 1290), Berlin: Springer-Verlag, 1–33.

[^baez-1998a]: Baez, J. & Dolan, J., 1998a, “Higher-Dimensional Algebra III. $n$-Categories and the Algebra of Opetopes”, *Advances in Mathematics*, 135: 145–206.

[^baez-1998b]: –––, 1998b, “Categorification”, *Higher Category Theory* (Contemporary Mathematics, Volume 230), Ezra Getzler and Mikhail Kapranov (eds.), Providence: AMS, 1–36.

[^baez-2001]: –––, 2001, “From Finite Sets to Feynman Diagrams”, *Mathematics Unlimited – 2001 and Beyond*, Berlin: Springer, 29–50.

[^baez-2011]: Baez, J. & Lauda, A.D., 2011, “A Pre-history of $n$-Categorical Physics”, *Deep Beauty: Understanding the Quantum World Through Mathematical Innovation*, H. Halvorson (ed.), Cambridge: Cambridge University Press, 13–128.

[^baez-2010]: Baez, J. & May, P. J., 2010, *Towards Higher Category Theory*, Berlin: Springer.

[^baez-2010-2]: Baez, J. & Stay, M., 2010, “Physics, Topology, Logic and Computation: a Rosetta Stone”, *New Structures for Physics* (Lecture Notes in Physics 813), B. Coecke (ed.), New York, Springer: 95–172.

[^baianu-1987]: Baianu, I. C., 1987, “Computer Models and Automata Theory in Biology and Medecine”, *Mathematical Modelling*, 7: 1513–1577.

[^bain-2013]: Bain, J., 2013, “Category-theoretic Structure and Radical Ontic Structural Realism”, *Synthese*, 190: 1621–1635.

[^barr-1985]: Barr, M. & Wells, C., 1985, *Toposes, Triples and Theories*, New York: Springer-Verlag.

[^barr-1999]: –––, 1999, *Category Theory for Computing Science*, Montreal: CRM.

[^batanin-1998]: Batanin, M., 1998, “Monoidal Globular Categories as a Natural Environment for the Theory of Weak $n$-Categories”, *Advances in Mathematics*, 136: 39–103.

[^bell-1981]: Bell, J. L., 1981, “Category Theory and the Foundations of Mathematics”, *British Journal for the Philosophy of Science*, 32: 349–358.

[^bell-1982]: –––, 1982, “Categories, Toposes and Sets”, *Synthese*, 51 (3): 293–337.

[^bell-1986]: –––, 1986, “From Absolute to Local Mathematics”, *Synthese*, 69 (3): 409–426.

[^bell-1988]: –––, 1988, “Infinitesimals”, *Synthese*, 75 (3): 285–315.

[^bell-1988-2]: –––, 1988, *Toposes and Local Set Theories: An Introduction*, Oxford: Oxford University Press.

[^bell-1995]: –––, 1995, “Infinitesimals and the Continuum”, *Mathematical Intelligencer*, 17 (2): 55–57.

[^bell-1998]: –––, 1998, *A Primer of Infinitesimal Analysis*, Cambridge: Cambridge University Press.

[^bell-2001]: –––, 2001, “The Continuum in Smooth Infinitesimal Analysis”, *Reuniting the Antipodes — Constructive and Nonstandard Views on the Continuum* (Synthese Library, Volume 306), Dordrecht: Kluwer, 19–24.

[^bell-2005]: –––, 2005, “The Development of Categorical Logic”, in *Handbook of Philosophical Logic* (Volume 12), 2nd ed., D.M. Gabbay, F. Guenthner (eds.), Dordrecht: Springer, pp. 279–362.

[^bell-2012]: –––, 2012, “Types, Sets and Categories”, in *Handbook of the History of Logic: Sets and Extensions in the Twentieth Century* (Volume 6), 1st edition, D. Gabbay, A. Kanamori, J. Woods (eds.), Amsterdam: North Holland, pp. 633–687.

[^birkoff-1999]: Birkoff, G. & Mac Lane, S., 1999, Algebra, 3ʳᵈ ed., Providence: AMS.

[^blass-1984]: Blass, A., 1984, “The Interaction Between Category Theory and Set Theory”, in *Mathematical Applications of Category Theory* (Volume 30), Providence: AMS, 5–29.

[^blass-1983]: Blass, A. & Scedrov, A., 1983, “Classifying Topoi and Finite Forcing”, *Journal of Pure and Applied Algebra*, 28: 111–140.

[^blass-1989]: –––, 1989, *Freyd’s Model for the Independence of the Axiom of Choice*, Providence: AMS.

[^blass-1992]: –––, 1992, “Complete Topoi Representing Models of Set Theory”, *Annals of Pure and Applied Logic* , 57 (1): 1–26.

[^blute-2004]: Blute, R. & Scott, P., 2004, “Category Theory for Linear Logicians”, in *Linear Logic in Computer Science*, T. Ehrhard, P. Ruet, J-Y. Girard, P. Scott (eds.), Cambridge: Cambridge University Press, 1–52.

[^boileau-1981]: Boileau, A. & Joyal, A., 1981, “La logique des topos”, *Journal of Symbolic Logic*, 46 (1): 6–16.

[^borceux-1994]: Borceux, F., 1994, *Handbook of Categorical Algebra*, 3 volumes, Cambridge: Cambridge University Press.

[^brading-2006]: Brading, K. & Landry, E., 2006, “Scientific Structuralism: Presentation and Representation”, *Philosophy of Science*, 73: 571–581.

[^brown-2006]: Brown, R. & Porter, T., 2006, “Category Theory: an abstract setting for analogy and comparison”, *What is Category Theory?*, G. Sica (ed.), Monza: Polimetrica: 257–274.

[^brunetti-2003]: Brunetti, R. & Fredenhagen, K & Verch, R., 2003, “The Generally Covariant Locality Principle – a new paradigm for local quantum field theory”, *Communications in Mathematical Physics*, 237 (1–2): 31–68.

[^buchsbaum-1955]: Buchsbaum, D.A., 1955, “Exact Categories and Duality”, *Transactions of the American Mathematical Society*, 80 (1): 1–34.

[^bunge-1974]: Bunge, M., 1974, “Topos Theory and Souslin’s Hypothesis”, *Journal of Pure and Applied Algebra*, 4: 159–187.

[^bunge-1984]: –––, 1984, “Toposes in Logic and Logic in Toposes”, *Topoi*, 3 (1): 13–22.

[^caramello-2011]: Caramello, O., 2011, “A Characterization Theorem for Geometric Logic”, *Annals of Pure and Applied Logic*,162, 4: 318–321.

[^caramello-2012a]: –––, 2012a, “Universal Models and Definability”, *Mathematical Proceedings of the Cambridge Philosophical Society*, 152 (2): 279–302.

[^caramello-2012b]: –––, 2012b, “Syntactic Characterizations of Properties of Classifying Toposes”, *Theory and Applications of Categories*, 26 (6): 176–193.

[^caramello-2018]: –––, 2018, *Theories, Sites, Toposes*, Oxford: Oxford University Press.

[^carter-2008]: Carter, J., 2008, “Categories for the working mathematician: making the impossible possible”, *Synthese*, 162 (1): 1–13.

[^cisinski-2019]: Cisinski, J.-C., 2019, *Higher Categories and Homotopical Algebra*, Cambridge: Cambridge University Press.

[^cockett-2001]: Cockett, J. R. B. & Seely, R. A. G., 2001, “Finite Sum-product Logic”, *Theory and Applications of Categories* (electronic), 8: 63–99.

[^cockett-2018]: Cockett, J. R. B. & Seely, R. A. G., 2018, “Proof Theory of the Cut Rule”, in *Categories for the Working Philosopher*, E. Landry (ed.), Oxford: Oxford University Press: 223–261.

[^coecke-2011]: Coecke, B., 2011, “A Universe of Processes and Some of its Guises”, *Deep Beauty: Understanding the Quantum World through Mathematical Innovation*, Cambridge: Cambridge University Press: 129–186.

[^coecke-2018]: Coecke, B. & Kissinger, A., 2018, “Categorical Quentum Mechanics I: Causal Quantum Processes”, *Categories for the Working Philosopher*, E. Landry (ed.), Oxford: Oxford University Press: 286–328.

[^couture-1991]: Couture, J. & Lambek, J., 1991, “Philosophical Reflections on the Foundations of Mathematics”, *Erkenntnis*, 34 (2): 187–209.

[^couture-1992]: –––, 1992, “Erratum:”Philosophical Reflections on the Foundations of Mathematics“”, *Erkenntnis*, 36 (1): 134.

[^crole-1994]: Crole, R. L., 1994, Categories for Types, Cambridge: Cambridge University Press.

[^de-2017]: De Toffoli, S., 2017, “Chasing the diagram – the use of visualizations in algebraic reasoning ”, *The Review of Symbolic Logic*, 10 (1): 158–186.

[^dieudonné-1960]: Dieudonné, J. & Grothendieck, A., 1960 [1971], *Éléments de Géométrie Algébrique*, Berlin: Springer-Verlag.

[^döring-2011]: Döring, A., 2011, “The Physical Interpretation of Daseinisation”, *Deep Beauty: Understanding the Quantum World through Mathematical Innovation*, Cambridge: Cambridge University Press: 207–238.

[^ehresmann-2018]: Ehresmann, A., 2018, “Applications of Categories to Biology and Cognition”, *Categories for the Working Philosopher*, E. Landry (ed.), Oxford: Oxford University Press: 358–380.

[^ehresmann-2007]: Ehresmann, A. & Vanbremeersch, J.-P., 2007, *Memory Evolutive Systems: Hierarchy, Emergence, Cognition*, Amsterdam: Elsevier

[^ehresmann-1987]: –––, 1987, “Hierarchical Evolutive Systems: a Mathematical Model for Complex Systems”, *Bulletin of Mathematical Biology*, 49 (1): 13–50.

[^eilenberg-1956]: Eilenberg, S. & Cartan, H., 1956, *Homological Algebra*, Princeton: Princeton University Press.

[^eilenberg-1942]: Eilenberg, S. & Mac Lane, S., 1942, “Group Extensions and Homology”, *Annals of Mathematics*, 43: 757–831.

[^eilenberg-1945]: –––, 1945, “General Theory of Natural Equivalences”, *Transactions of the American Mathematical Society*, 58: 231–294.

[^eilenberg-1952]: Eilenberg, S. & Steenrod, N., 1952, *Foundations of Algebraic Topology*, Princeton: Princeton University Press.

[^ellerman-1988]: Ellerman, D., 1988, “Category Theory and Concrete Universals”, *Erkenntnis*, 28: 409–429.

[^ellerman-2017]: –––, 2017, “Category Theory and Set Theory as Theories about Complementary Types of Universals”, *Logic and Logical Philosophy*, 26 (2): 145–162.

[^eva-2016]: Eva, B., 2016, “Category Theory and Physical Structuralism”, *European Journal for Philosophy of Science*, 6 (2): 231–246.

[^eva-2017]: –––, 2017, “Topos Theoretic Quantum Realism”, *The British Journal for the Philosophy of Science*, 68 (4): 1149–1181.

[^feferman-1977]: Feferman, S., 1977, “Categorical Foundations and Foundations of Category Theory”, *Logic, Foundations of Mathematics and Computability*, R. Butts (ed.), Reidel, 149–169.

[^feferman-2004]: –––, 2004, “Typical Ambiguity: trying to have your cake and eat it too”, *One Hundred Years of Russell’s Paradox*, G. Link (ed.), Berlin: De Gruyter, 135–151.

[^freyd-1964]: Freyd, P., 1964, *Abelian Categories. An Introduction to the Theory of Functors*, New York: Harper & Row.

[^freyd-1965]: –––, 1965, “The Theories of Functors and Models”. *Theories of Models*, Amsterdam: North Holland, 107–120.

[^freyd-1972]: –––, 1972, “Aspects of Topoi”, *Bulletin of the Australian Mathematical Society*, 7: 1–76.

[^freyd-1980]: –––, 1980, “The Axiom of Choice”, *Journal of Pure and Applied Algebra*, 19: 103–125.

[^freyd-1987]: –––, 1987, “Choice and Well-Ordering”, *Annals of Pure and Applied Logic*, 35 (2): 149–166.

[^freyd-1990]: –––, 1990, *Categories, Allegories*, Amsterdam: North Holland.

[^freyd-2002]: –––, 2002, “Cartesian Logic”, *Theoretical Computer Science*, 278 (1–2): 3–21.

[^freyd-1987-2]: Freyd, P., Friedman, H. & Scedrov, A., 1987, “Lindembaum Algebras of Intuitionistic Theories and Free Categories”, *Annals of Pure and Applied Logic*, 35 (2): 167–172.

[^galli-2000]: Galli, A. & Reyes, G. & Sagastume, M., 2000, “Completeness Theorems via the Double Dual Functor”, *Studia Logical*, 64 (1): 61–81.

[^ghilardi-1989]: Ghilardi, S., 1989, “Presheaf Semantics and Independence Results for some Non-classical first-order logics”, *Archive for Mathematical Logic*, 29 (2): 125–136.

[^ghilardi-2002]: Ghilardi, S. & Zawadowski, M., 2002, *Sheaves, Games & Model Completions: A Categorical Approach to Nonclassical Porpositional Logics*, Dordrecht: Kluwer.

[^goldblatt-1979]: Goldblatt, R., 1979, *Topoi: The Categorical Analysis of Logic, Studies in logic and the foundations of mathematics*, Amsterdam: Elsevier.

[^grothendieck-1957]: Grothendieck, A., 1957, “Sur Quelques Points d’algèbre homologique”, *Tohoku Mathematics Journal*, 9: 119–221.

[^grothendieck-nd]: Grothendieck, A. *et al*., *Séminaire de Géométrie Algébrique*, Vol. 1–7, Berlin: Springer-Verlag.

[^hatcher-1982]: Hatcher, W. S., 1982, *The Logical Foundations of Mathematics*, Oxford: Pergamon Press.

[^healy-2000]: Healy, M. J., 2000, “Category Theory Applied to Neural Modeling and Graphical Representations”, *Proceedings of the IEEE-INNS-ENNS International Joint Conference on Neural Networks: IJCNN200, Como, vol. 3*, M. Gori, S-I. Amari, C. L. Giles, V. Piuri (eds.), IEEE Computer Science Press, 35–40.

[^healy-2006]: Healy, M. J., & Caudell, T. P., 2006, “Ontologies and Worlds in Category Theory: Implications for Neural Systems”,*Axiomathes*, 16 (1–2): 165–214.

[^hellman-2003]: Hellman, G., 2003, “Does Category Theory Provide a Framework for Mathematical Structuralism?”, *Philosophia Mathematica*, 11 (2): 129–157.

[^hellman-2006]: –––, 2006, “Mathematical Pluralism: the case of smooth infinitesimal analysis”, *Journal of Philosophical Logic*, 35 (6): 621–651.

[^hellman-2011]: –––, 2011,“Foundational Frameworks”, in *Foundational Theories of Classical and Constructive Mathematics*, G. Sommaruga (ed.), New York: Springer: 53–70.

[^hellman-2013]: Hellman, G., 2013, “Neither Categorical nor Set-Theoretic Foundations”, *The Review of Symbolic Logic*, 6 (1): 16–23.

[^hermida-2000]: Hermida, C. & Makkai, M. & Power, J., 2000, “On Weak Higher-dimensional Categories I”, *Journal of Pure and Applied Algebra*, 154 (1–3): 221–246.

[^hermida-2001]: –––, 2001, “On Weak Higher-dimensional Categories 2”, *Journal of Pure and Applied Algebra*, 157 (2–3): 247–277.

[^hermida-2002]: –––, 2002, “On Weak Higher-dimensional Categories 3”, *Journal of Pure and Applied Algebra*, 166 (1–2): 83–104.

[^heunen-2009]: Heunen, C. & Landsmann, N. & Spitters, B., 2009, “A Topos for Algebraic Quantum Theory”, *Communications in Mathematical Physics*, 291 (1): 63–110.

[^hyland-1982]: Hyland, J. M. E., 1982, “The Effective Topos”, *Studies in Logic and the Foundations of Mathematics* (Volume 110), Amsterdam: North Holland, 165–216.

[^hyland-1988]: –––, 1988, “A Small Complete Category”, *Annals of Pure and Applied Logic*, 40 (2): 135–165.

[^hyland-1991]: –––, 1991, “First Steps in Synthetic Domain Theory”, *Category Theory (Como 1990)* (Lecture Notes in Mathematics, Volume 1488), Berlin: Springer, 131–156.

[^hyland-2002]: –––, 2002, “Proof Theory in the Abstract”, *Annals of Pure and Applied Logic*, 114 (1–3): 43–78.

[^hyland-1990]: Hyland, J. M. E. & Robinson, E. P. & Rosolini, G., 1990, “The Discrete Objects in the Effective Topos”, *Proceedings of the London Mathematical Society (3)*, 60 (1): 1–36.

[^isham-2011]: Isham, C.J., 2011, “Topos Methods in the Foundations of Physics”, *Deep Beauty: Understanding the Quantum World through Mathematical Innovation*, Cambridge: Cambridge University Press: 187–206.

[^jacobs-1999]: Jacobs, B., 1999, *Categorical Logic and Type Theory*, Amsterdam: North Holland.

[^johnstone-1977]: Johnstone, P. T., 1977, *Topos Theory*, New York: Academic Press.

[^johnstone-1979a]: –––, 1979a, “Conditions Related to De Morgan’s Law”, *Applications of Sheaves* (Lecture Notes in Mathematics, Volume 753), Berlin: Springer, 479–491.

[^johnstone-1979b]: –––, 1979b, “Another Condition Equivalent to De Morgan’s Law”, *Communications in Algebra*, 7 (12): 1309–1312.

[^johnstone-1981]: –––, 1981, “Tychonoff’s Theorem without the Axiom of Choice”, *Fundamenta Mathematicae*, 113 (1): 21–35.

[^johnstone-1982]: –––, 1982, *Stone Spaces*, Cambridge:Cambridge University Press.

[^johnstone-1985]: –––, 1985, “How General is a Generalized Space?”, *Aspects of Topology*, Cambridge: Cambridge University Press, 77–111.

[^johnstone-2001]: –––, 2001, “Elements of the History of Locale Theory”, *Handbook of the History of General Topology*, Vol. 3, Dordrecht: Kluwer, 835–851.

[^johnstone-2002a]: –––, 2002a, *Sketches of an Elephant: a Topos Theory Compendium. Vol. 1* (Oxford Logic Guides, Volume 43), Oxford: Oxford University Press.

[^joyal-1995]: Joyal, A. & Moerdijk, I., 1995, *Algebraic Set Theory*, Cambridge: Cambridge University Press.

[^joyal-1993]: Joyal, A. and Street, R., 1993, “Braided Tensor Categories”, *Advances in Mathematics*, 102 (1): 20–78.

[^joyal-1996]: Joyal, A., Street, R. and Verity, D., 1996, “Traced Monoidal Categories”, *Mathematical Proceedings of the Cambridge Philosophical Society*, 119 (3): 447–468.

[^kan-1958]: Kan, D. M., 1958, “Adjoint Functors”, *Transactions of the American Mathematical Society*, 87: 294–329.

[^kishida-2018]: Kishida, K., 2018, “Categories and Modalities”, in *Categories for the Working Philosopher*, E. Landry (ed.), Oxford, Oxford University Press: 163–222.

[^kock-2006]: Kock, A., 2006, *Synthetic Differential Geometry* (London Mathematical Society Lecture Note Series, Volume 51), Cambridge: Cambridge University Press, 2nd ed.

[^krömer-2007]: Krömer, R., 2007, *Tool and Objects: A History and Philosophy of Category Theory*, Basel: Birkhäuser.

[^la-1994]: La Palme Reyes, M., John Macnamara, Gonzalo E. Reyes, and Houman Zolfaghari, 1994, “The non-Boolean Logic of Natural Language Negation”, *Philosophia Mathematica*, 2 (1): 45–68.

[^la-1999]: –––, 1999, “Count Nouns, Mass Nouns, and their Transformations: a Unified Category-theoretic Semantics”, *Language, Logic and Concepts*, Cambridge: MIT Press, 427–452.

[^lal-2017]: Lal, R. & Teh, N., 2017, “Categorical Generalization and Physical Structuralism”, *British Journal for the Philosophy of Science*, 68 (1): 213–251.

[^lambek-1968]: Lambek, J., 1968, “Deductive Systems and Categories I. Syntactic Calculus and Residuated Categories”, *Mathematical Systems Theory*, 2: 287–318.

[^lambek-1969]: –––, 1969, “Deductive Systems and Categories II. Standard Constructions and Closed Categories”, *Category Theory, Homology Theory and their Applications I*, Berlin: Springer, 76–122.

[^lambek-1972]: –––, 1972, “Deductive Systems and Categories III. Cartesian Closed Categories, Intuitionâ‰ istic Propositional Calculus, and Combinatory Logic”, *Toposes, Algebraic Geometry and Logic* (Lecture Notes in Mathematics, Volume 274), Berlin: Springer, 57–82.

[^lambek-1982]: –––, 1982, “The Influence of Heraclitus on Modern Mathematics”, *Scientific Philosophy Today*, J. Agassi and R.S. Cohen (eds.), Dordrecht, Reidel, 111–122.

[^lambek-1986]: –––, 1986, “Cartesian Closed Categories and Typed lambda calculi”, *Combinators and Functional Programming Languages* (Lecture Notes in Computer Science, Volume 242), Berlin: Springer, 136–175.

[^lambek-1989a]: –––, 1989a, “On Some Connections Between Logic and Category Theory”, *Studia Logica*, 48 (3): 269–278.

[^lambek-1989b]: –––, 1989b, “On the Sheaf of Possible Worlds”, *Categorical Topology and its relation to Analysis, Algebra and Combinatorics*, Teaneck: World Scientific Publishing, 36–53.

[^lambek-1993]: –––, 1993, “Logic without Structural Rules”, *Substructural Logics* (Studies in Logic and Computation, Volume 2), Oxford: Oxford University Press, 179–206.

[^lambek-1994a]: –––, 1994a, “Some Aspects of Categorical Logic”, *Logic, Methodology and Philosophy of Science IX* (Studies in Logic and the Foundations of Mathematics, Volume 134), Amsterdam: North Holland, 69–89.

[^lambek-1994b]: –––, 1994b, “Are the Traditional Philosophies of Mathematics Really Incompatible?”, *Mathematical Intelligencer*, 16 (1): 56–62.

[^lambek-1994c]: –––, 1994c, “What is a Deductive System?”, *What is a Logical System?* (Studies in Logic and Computation, Volume 4), Oxford: Oxford University Press, 141–159.

[^lambek-2004]: –––, 2004, “What is the world of Mathematics? Provinces of Logic Determined”, *Annals of Pure and Applied Logic*, 126: 1–3, 149–158.

[^lambek-1981]: Lambek, J. & Scott, P.J., 1981, “Intuitionistic Type Theory and Foundations”, *Journal of Philosophical Logic*, 10 (1): 101–115.

[^lambek-1983]: –––, 1983, “New Proofs of Some Intuitionistic Principles”, *Zeitschrift für Mathematische Logik und Grundlagen der Mathematik*, 29 (6): 493–504.

[^lambek-1986-2]: –––, 1986, *Introduction to Higher Order Categorical Logic*, Cambridge: Cambridge University Press.

[^lam-2015]: Lam, V. & Wütrich, C., 2015, “No Categorical Support for Radical Ontic Structural Realism”, *British Journal for the Philosophy of Science*, 66 (3): 605–634.

[^landry-1999]: Landry, E., 1999, “Category Theory: the Language of Mathematics”, *Philosophy of Science*, 66 (3) (Supplement): S14–S27.

[^landry-2001]: –––, 2001, “Logicism, Structuralism and Objectivity”, *Topoi*, 20 (1): 79–95.

[^landry-2007]: –––, 2007, “Shared Structure need not be Shared Set-structure”, *Synthese*, 158 (1): 1–17.

[^landry-2011]: –––, 2011, “How to be a Structuralist all the way down”, *Synthese*, 179: 435–454.

[^landry-2012]: –––, 2012, “Methodological Structural Realism”, in *Sructure, Objects, and Causality*, E. Landry & D. Rickles (eds.), Dordrecht, Reidel: 29–59.

[^landry-2013]: –––, 2013, “The Genetic versus The Axiomatic Method: responding to Feferman 1977”, *The Review of Symbolic Logic*, 6 (1): 24–50.

[^landry-2018]: –––, 2018, “Structural Realism and Category Mistakes”, in *Categories for the Working Philosopher*, E. Landry (ed.), Oxford, Oxford University Press: 430–449.

[^landry-2005]: Landry, E. & Marquis, J.-P., 2005, “Categories in Context: Historical, Foundational and philosophical”, *Philosophia Mathematica*, 13: 1–43.

[^landry-2017]: –––, 2017, *Categories for the Working Philosophers*, Oxford: Oxford University Press.

[^lawvere-1963]: Lawvere, F. W., 1963, “Functorial Semantics of Algebraic Theories”, *Proceedings of the National Academy of Sciences U.S.A.*, 50: 869–872.

[^lawvere-1964]: –––, 1964, “An Elementary Theory of the Category of Sets”, *Proceedings of the National Academy of Sciences U.S.A.*, 52: 1506–1511.

[^lawvere-1965]: –––, 1965, “Algebraic Theories, Algebraic Categories, and Algebraic Functors”, *Theory of Models*, Amsterdam: North Holland, 413–418.

[^lawvere-1966]: –––, 1966, “The Category of Categories as a Foundation for Mathematics”, *Proceedings of the Conference on Categorical Algebra*, La Jolla, New York: Springer-Verlag, 1–21.

[^lawvere-1969a]: –––, 1969a, “Diagonal Arguments and Cartesian Closed Categories”, *Category Theory, Homology Theory, and their Applications II*, Berlin: Springer, 134–145.

[^lawvere-1969b]: –––, 1969b, “Adjointness in Foundations”, *Dialectica*, 23: 281–295.

[^lawvere-1970]: –––, 1970, “Equality in Hyper doctrines and Comprehension Schema as an Adjoint Functor”, *Applications of Categorical Algebra*, Providence: AMS, 1–14.

[^lawvere-1971]: –––, 1971, “Quantifiers and Sheaves”, *Actes du Congrès International des Mathématiciens, Tome 1*, Paris: Gauthier-Villars, 329–334.

[^lawvere-1972]: –––, 1972, “Introduction”, *Toposes, Algebraic Geometry and Logic*, Lecture Notes in Mathematics, 274, Springer-Verlag, 1–12.

[^lawvere-1975]: –––, 1975, “Continuously Variable Sets: Algebraic Geometry = Geometric Logic”, *Proceedings of the Logic Colloquium Bristol 1973*, Amsterdam: North Holland, 135–153.

[^lawvere-1976]: –––, 1976, “Variable Quantities and Variable Structures in Topoi”, *Algebra, Topology, and Category Theory*, New York: Academic Press, 101–131.

[^lawvere-1992]: –––, 1992, “Categories of Space and of Quantity”, *The Space of Mathematics*, Foundations of Communication and Cognition, Berlin: De Gruyter, 14–30.

[^lawvere-1994a]: –––, 1994a, “Cohesive Toposes and Cantor’s lauter Ensein ”, *Philosophia Mathematica*, 2 (1): 5–15.

[^lawvere-1994b]: –––, 1994b, “Tools for the Advancement of Objective Logic: Closed Categories and Toposes”, *The Logical Foundations of Cognition* (Vancouver Studies in Cognitive Science, Volume 4), Oxford: Oxford University Press, 43–56.

[^lawvere-2000]: –––, 2000, “Comments on the Development of Topos Theory”, *Development of Mathematics 1950–2000*, Basel: Birkhäuser, 715–734.

[^lawvere-2002]: –––, 2002, “Categorical Algebra for Continuum Micro Physics”, *Journal of Pure and Applied Algebra*, 175 (1–3): 267–287.

[^lawvere-2003]: –––, 2003, “Foundations and Applications: Axiomatization and Education. New Programs and Open Problems in the Foundation of Mathematics”, *Bulletin of Symbolic Logic*, 9 (2): 213–224.

[^lawvere-2003-2]: Lawvere, F. W. & Rosebrugh, R., 2003, *Sets for Mathematics*, Cambridge: Cambridge University Press.

[^lawvere-1997]: Lawvere, F. W. & Schanuel, S., 1997, *Conceptual Mathematics: A First Introduction to Categories*, Cambridge: Cambridge University Press.

[^leinster-2002]: Leinster, T., 2002, “A Survey of Definitions of $n$-categories”, *Theory and Applications of Categories*, (electronic), 10: 1–70.

[^leinster-2004]: –––, 2004, *Higher Operads, Higher Categories*, London Mathematical Society Lecture Note Series, 298, Cambridge: Cambridge University Press.

[^leinster-2014]: –––, 2014, *Basic Category Theory*, Cambridge: Cambridge University Press.

[^linnebo-2011]: Linnebo, O. & Pettigrew, R., 2011, “Category Theory as an Autonomous Foundation”, *Philosophia Mathematica*, 19 (3): 227–254.

[^logan-2015]: Logan, S., 2015, “Category Theory is a Contentful Theory”, *Philosophia Mathematica*, 23 (1): 110–115.

[^lurie-2009]: Lurie, J., 2009, *Higher Topos Theory*, Princeton: Princeton University Press.

[^mac-1950]: Mac Lane, S., 1950, “Dualities for Groups”, *Bulletin of the American Mathematical Society*, 56: 485–516.

[^mac-1969]: –––, 1969, “Foundations for Categories and Sets”, *Category Theory, Homology Theory and their Applications II*, Berlin: Springer, 146–164.

[^mac-1969-2]: –––, 1969, “One Universe as a Foundation for Category Theory”, *Reports of the Midwest Category Seminar III*, Berlin: Springer, 192–200.

[^mac-1971]: –––, 1971, “Categorical algebra and Set-Theoretic Foundations”, *Axiomatic Set Theory*, Providence: AMS, 231–240.

[^mac-1975]: –––, 1975, “Sets, Topoi, and Internal Logic in Categories”, *Studies in Logic and the Foundations of Mathematics* (Volumes 80), Amsterdam: North Holland, 119–134.

[^mac-1981]: –––, 1981, “Mathematical Models: a Sketch for the Philosophy of Mathematics”, *American Mathematical Monthly*, 88 (7): 462–472.

[^mac-1986]: –––, 1986, *Mathematics, Form and Function*, New York: Springer.

[^mac-1988]: –––, 1988, “Concepts and Categories in Perspective”, *A nCentury of Mathematics in America, Part I*, Providence: AMS, 323–365.

[^mac-1989]: –––, 1989, “The Development of Mathematical Ideas by Collision: the Case of Categories and Topos Theory”, *Categorical Topology and its Relation to Analysis, Algebra and Combinatorics*, Teaneck: World Scientific, 1–9.

[^mac-1996]: –––, 1996, “Structure in Mathematics. Mathematical Structuralism”, *Philosophia Mathematica*, 4 (2): 174–183.

[^mac-1997]: –––, 1997, “Categorical Foundations of the Protean Character of Mathematics”, *Philosophy of Mathematics Today*, Dordrecht: Kluwer, 117–122.

[^mac-1998]: –––, 1998, *Categories for the Working Mathematician*, 2ⁿᵈ edition, New York: Springer-Verlag.

[^mac-1992]: Mac Lane, S. & Moerdijk, I., 1992, *Sheaves in Geometry and Logic*, New York: Springer-Verlag.

[^macnamara-1994]: MacNamara, J. & Reyes, G. (eds.), 1994, *The Logical Foundation of Cognition*, Oxford: Oxford University Press.

[^majid-1995]: Majid, S., 1995, *Foundations of Quantum Group Theory*, Cambridge: Cambridge University Press.

[^makkai-1987]: Makkai, M., 1987, “Stone Duality for First-Order Logic”, *Advances in Mathematics*, 65 (2): 97–170.

[^makkai-1988]: –––, 1988, “Strong Conceptual Completeness for First Order Logic”, *Annals of Pure and Applied Logic*, 40: 167–215.

[^makkai-1997a]: –––, 1997a, “Generalized Sketches as a Framework for Completeness Theorems I”, *Journal of Pure and Applied Algebra*, 115 (1): 49–79.

[^makkai-1997b]: –––, 1997b, “Generalized Sketches as a Framework for Completeness Theorems II”, *Journal of Pure and Applied Algebra*, 115 (2): 179–212.

[^makkai-1997c]: –––, 1997c, “Generalized Sketches as a Framework for Completeness Theorems III”, *Journal of Pure and Applied Algebra*, 115 (3): 241–274.

[^makkai-1998]: –––, 1998, “Towards a Categorical Foundation of Mathematics”, *Lecture Notes in Logic* (Volume 11), Berlin: Springer, 153–190.

[^makkai-1999]: –––, 1999, “On Structuralism in Mathematics”, *Language, Logic and Concepts*, Cambridge: MIT Press, 43–66.

[^makkai-1989]: Makkai, M. & Paré, R., 1989, *Accessible Categories: the Foundations of Categorical Model Theory*, Contemporary Mathematics 104, Providence: AMS.

[^makkai-1977]: Makkai, M. & Reyes, G., 1977, *First-Order Categorical Logic*, Springer Lecture Notes in Mathematics 611, New York: Springer.

[^makkai-1995]: –––, 1995, “Completeness Results for Intuitionistic and Modal Logic in a Categorical Setting”, *Annals of Pure and Applied Logic*, 72 (1): 25–101.

[^marquis-1993]: Marquis, J.-P., 1993, “Russell’s Logicism and Categorical Logicisms”, *Russell and Analytic Philosophy*, A. D. Irvine & G. A. Wedekind (eds.), Toronto, University of Toronto Press, 293–324.

[^marquis-1995]: –––, 1995, “Category Theory and the Foundations of Mathematics: Philosophical Excavations”, *Synthese*, 103: 421–447.

[^marquis-2000]: –––, 2000, “Three Kinds of Universals in Mathematics?”, in *Logical Consequence: Rival Approaches and New Studies in Exact Philosophy: Logic, Mathematics and Science*, Vol. II, B. Brown & J. Woods (eds.), Oxford: Hermes, 191–212.

[^marquis-2006]: –––, 2006, “Categories, Sets and the Nature of Mathematical Entities”, in *The Age of Alternative Logics. Assessing philosophy of logic and mathematics today*, J. van Benthem, G. Heinzmann, Ph. Nabonnand, M. Rebuschi, H. Visser (eds.), Springer, 181–192.

[^marquis-2009]: –––, 2009, *From a Geometrical Point of View: A Study in the History and Philosophy of Category Theory*, Berlin: Springer.

[^marquis-2013]: –––, 2013, “Mathematical Forms and Forms of Mathematics: leaving the shores of extensional mathematics”, *Synthese*, 190 (12): 2141–2164.

[^marquis-2013b]: –––, 2013b, “Categorical Foundations of Mathematics or how to provide foundations for abstract mathematics”, *The Review of Symbolic Logic*, 6 (1): 51–75.

[^marquis-2014]: –––, 2014, “Mathematical Abstraction, Conceptual Variation and Identity”, *Logic, Methodology and Philosophy of science – logic and science facing the new technologies*, P. Schroeder-Heister, et al. (eds.), London: College Publications, 299–322.

[^marquis-2016]: –––, 2016, “Stairway to Heaven”, *The Mathematical Intelligencer*, 38 (3): 41–51.

[^marquis-2012]: Marquis, J.-P. & Reyes, G., 2012, “The History of Categorical Logic: 1963–1977”, *Handbook of the History of Logic*, Vol. 6, D. Gabbay & J. Woods (eds.), Amsterdam: Elsevier, 689–800.

[^mclarty-1986]: McLarty, C., 1986, “Left Exact Logic”, *Journal of Pure and Applied Algebra*, 41 (1): 63–66.

[^mclarty-1990]: –––, 1990, “Uses and Abuses of the History of Topos Theory”, *British Journal for the Philosophy of Science*, 41: 351–375.

[^mclarty-1991]: –––, 1991, “Axiomatizing a Category of Categories”, *Journal of Symbolic Logic*, 56 (4): 1243–1260.

[^mclarty-1992]: –––, 1992, *Elementary Categories, Elementary Toposes*, Oxford: Oxford University Press.

[^mclarty-1993]: –––, 1993, “Numbers Can be Just What They Have to”, *Noûs*, 27: 487–498.

[^mclarty-1994]: –––, 1994, “Category Theory in Real Time”, *Philosophia Mathematica*, 2 (1): 36–44.

[^mclarty-2004]: –––, 2004, “Exploring Categorical Structuralism”, *Philosophia Mathematica*, 12: 37–53.

[^mclarty-2005]: –––, 2005, “Learning from Questions on Categorical Foundations”, *Philosophia Mathematica*, 13 (1): 44–60.

[^mclarty-2006]: –––, 2006, “Emmy Noether’s set-theoretic topology: from Dedekind to the rise of functors”, *The Architecture of Modern Mathematics*, J.J. Gray & J. Ferreiros, Oxford: Oxford University Press, 187–208.

[^mclarty-2011]: –––, 2011, “Recent Debate over Categorical Foundations”, in *Foundational Theories of Classical and Constructive Mathematics*, G. Sommaruga (ed.), New York: Springer: 145–154.

[^mclarty-2018]: –––, 2018, “The Role of Set Theory in Mathematics”, in *Categories for the Working Philosopher*, E. Landry (ed.), Oxford, Oxford University Press: 1–17.

[^moerdijk-1984]: Moerdijk, I., 1984, “Heine-Borel does not imply the Fan Theorem”, *Journal of Symbolic Logic*, 49 (2): 514–519.

[^moerdijk-1995a]: –––, 1995a, “A Model for Intuitionistic Non-standard Arithmetic”, *Annals of Pure and Applied Logic*, 73 (1): 37–51.

[^moerdijk-1998]: –––, 1998, “Sets, Topoi and Intuitionism”, *Philosophia Mathematica*, 6 (2): 169–177.

[^moerdijk-1997]: Moerdijk, I. & Palmgren, E., 1997, “Minimal Models of Heyting Arithmetic”, *Journal of Symbolic Logic*, 62 (4): 1448–1460.

[^moerdijk-2002]: –––, 2002, “Type Theories, Toposes and Constructive Set Theory: Predicative Aspects of AST”, *Annals of Pure and Applied Logic*, 114 (1–3): 155–201.

[^moerdijk-1991]: Moerdijk, I. & Reyes, G., 1991, *Models for Smooth Infinitesimal Analysis*, New York: Springer-Verlag.

[^palmgren-2012]: Palmgren, E., 2012, “Constructivist and Structuralist Foundations: Bishop’s and Lawvere’s Theories of Sets”, *Annals of Pure and Applied Logic*, 63: 1384–1399.

[^palmgren-2018]: Palmgren, E., 2018, “A Constructive Examination of a Russell-style Ramified Type Theory”, *The Bulletin of Symbolic Logic*, 24 (1): 90–106.

[^pareigis-1970]: Pareigis, B., 1970, *Categories and Functors*, New York: Academic Press.

[^pedicchio-2004]: Pedicchio, M. C. & Tholen, W., 2004, *Categorical Foundations*, Cambridge: Cambridge University Press.

[^peirce-1991]: Peirce, B., 1991, *Basic Category Theory for Computer Scientists*, Cambridge: MIT Press.

[^peruzzi-2006]: Peruzzi, A., 2006, “The Meaning of Category Theory for 21st Century Philosophy”, *Axiomathes*, 16 (4): 424–459.

[^peruzzi-2016]: –––, 2016, “Category Theory and the Search for Universals: A Very Short Guide for Philosophers”, in *Modern Logic 1850–1950, East and West*, F. Abeles & M. Muller (eds.), Basel: Birkhauser, 159–182.

[^pitts-1987]: Pitts, A. M., 1987, “Interpolation and Conceptual Completeness for Pretoposes via Category Theory”, *Mathematical Logic and Theoretical Computer Science* (Lecture Notes in Pure and Applied Mathematics, Volume 106), New York: Dekker, 301–327.

[^pitts-1989]: –––, 1989, “Conceptual Completeness for First-order Intuitionistic Logic: an Application of Categorical Logic”, *Annals of Pure and Applied Logic*, 41 (1): 33–81.

[^pitts-1992]: –––, 1992, “On an Interpretation of Second-order Quantification in First-order Propositional Intuitionistic Logic”, *Journal of Symbolic Logic*, 57 (1): 33–52.

[^pitts-2000]: –––, 2000, “Categorical Logic”, *Handbook of Logic in Computer Science, Vol.5*, Oxford: Oxford Unversity Press, 39–128.

[^pitts-1989-2]: Pitts, A. M. & Taylor, P., 1989, “A Note of Russell’s Paradox in Locally Cartesian Closed Categories”, *Studia Logica*, 48 (3): 377–387.

[^plotkin-2000]: Plotkin, B., 2000, “Algebra, Categories and Databases”, *Handbook of Algebra, Vol. 2*, Amsterdam: Elsevier, 79–148.

[^porter-2004]: Porter, T., 2004, “Interpreted Systems and Kripke Models for Multiagent Systems from a Categorical Perspective”, *Theoretical Computer Science*, 323 (1–3): 235–266.

[^reyes-1991]: Reyes, G., 1991, “A Topos-theoretic Approach to Reference and Modality”, *Notre Dame Journal of Formal Logic*, 32 (3): 359–391.

[^reyes-1974]: –––, 1974, “From Sheaves to Logic”, in *Studies in Algebraic Logic*, A. Daigneault (ed.), Providence: AMS.

[^reyes-1993]: Reyes, G. & Zawadowski, M., 1993, “Formal Systems for Modal Operators on Locales”, *Studia Logica*, 52 (4): 595–613.

[^reyes-1991-2]: Reyes, G. & Zolfaghari, H., 1991, “Topos-theoretic Approaches to Modality”, *Category Theory (Como 1990)* (Lecture Notes in Mathematics, Volume 1488), Berlin: Springer, 359–378.

[^reyes-1996]: –––, 1996, “Bi-Heyting Algebras, Toposes and Modalities”, *Journal of Philosophical Logic*, 25 (1): 25–43.

[^riehl-2016]: Riehl, E., 2016, *Category Theory in Context*, Mineola: Dover.

[^rodabaugh-nd]: Rodabaugh, S. E. & Klement, E. P. (eds.), *Topological and Algebraic Structures in Fuzzy Sets: A Handbook of Recent Developments in the Mathematics of Fuzzy Sets* (Trends in Logic, Volume 20), Dordrecht: Kluwer.

[^rodin-2014]: Rodin, A., 2014, *Axiomatic Method and Category Theory* (Synthese Library: Volume 364), New York: Springer.

[^scedrov-1984]: Scedrov, A., 1984, *Forcing and Classifying Topoi*, Providence: AMS.

[^scott-2000]: Scott, P.J., 2000, “Some Aspects of Categories in Computer Science”, *Handbook of Algebra, Vol. 2*, Amsterdam: North Holland, 3–77.

[^seely-1984]: Seely, R. A. G., 1984, “Locally Cartesian Closed Categories and Type Theory”, *Mathematical Proceedings of the Cambridge Mathematical Society*, 95 (1): 33–48.

[^shapiro-2005]: Shapiro, S., 2005, “Categories, Structures and the Frege-Hilbert Controversy: the Status of Metamathematics”, *Philosophia Mathematica*, 13 (1): 61–77.

[^shapiro-2011]: –––, 2011,“Foundations: Structures, Sets, and Categories”, in *Foundational Theories of Classical and Constructive Mathematics*, G. Sommaruga (ed.), New York: Springer: 97–110.

[^sica-2006]: Sica, G. (ed.), 2006, *What is Category Theory?*, Firenze: Polimetrica.

[^simpson-2011]: Simpson, C., 2011, *Homotopy Theory of Higher Categories*, Cambridge: Cambridge University Press.

[^spivak-2014]: Spivak, D., 2014, *Category Theory for the Sciences*, Cambridge: MIT Press.

[^taylor-1996]: Taylor, P., 1996, “Intuitionistic sets and Ordinals”, *Journal of Symbolic Logic*, 61: 705–744.

[^taylor-1999]: –––, 1999, *Practical Foundations of Mathematics*, Cambridge: Cambridge University Press.

[^tierney-1972]: Tierney, M., 1972, “Sheaf Theory and the Continuum Hypothesis”, *Toposes, Algebraic Geometry and Logic*, F.W. Lawvere (ed.), Springer Lecture Notes in Mathematics 274, 13–42.

[^van-2002]: Van Oosten, J., 2002, “Realizability: a Historical Essay”, *Mathematical Structures in Computer Science*, 12 (3): 239–263.

[^van-2008]: –––, 2008, *Realizability: an Introduction to its Categorical Side* (Studies in Logic and the Foundations of Mathematics, Volume 152), Amsterdam: Elsevier.

[^van-1984a]: Van der Hoeven, G. & Moerdijk, I., 1984a, “Sheaf Models for Choice Sequences”, *Annals of Pure and Applied Logic*, 27 (1): 63–107.

[^van-1984b]: –––, 1984b, “On Choice Sequences determined by Spreads”, *Journal of Symbolic Logic*, 49 (3): 908–916.

[^van-1984c]: –––, 1984c, “Constructing Choice Sequences for Lawless Sequences of Neighbourhood Functions”, *Models and Sets* (Lecture Notes in Mathematics, Volume 1103), Berlin: Springer, 207–234.

[^walsh-2017]: Walsh, P., 2017, “Categorical Harmony and Path Induction”, *The Review of Symbolic Logic*, 10 (2): 301–321.

[^wood-2004]: Wood, R.J., 2004, “ Ordered Sets via Adjunctions”, *Categorical Foundations*, M. C. Pedicchio & W. Tholen (eds.), Cambridge: Cambridge University Press.

[^yanofski-2003]: Yanofski, N., 2003, “A Universal Approach to Self-Referential Paradoxes, Incompleteness and Fixed Points”, *The Bulletin of Symbolic Logic*, 9 (3): 362–386.
