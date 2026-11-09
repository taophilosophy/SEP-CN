# nonwellfounded-set-theory — modeling-circularity（supplement）

> （《nonwellfounded-set-theory》词条补充材料，源：plato.stanford.edu/entries/nonwellfounded-set-theory/modeling-circularity.html）

#### Supplement to Non-wellfounded Set Theory

## Additional related modeling of circularity

At this point, we have presented the main points in this entry: an introduction to the mathematics of hypersets and specifically to work with the axiom *AFA*, and an exploration of the conceptual dualities that appear to lie at the heart of the matter. In this supplement, we want to mention briefly two matters related to the instances of circularity mentioned earlier. The goal here is to show how the perspective of coalgebra widens the scope of circular phenomena. That is, the two sections below represent treatments that use coalgebra more than hypersets.

### Universal Harsanyi type spaces and coalgebraic modal logic

We mentioned in [our supplement on universal Harsanyi type spaces](nonwellfounded-set-theory.harsanyi-type-spaces.md) the problem of finding *universal type spaces*. We point out here that this amounts to finding a final coalgebra for a certain endofunctor on a certain category. Then we discuss what is known about this matter. Finally, we bring matters back to the overall points of this entry.

There are some clues that coalgebra could be connected to type spaces. The first is that the notion of “belief” in the game theory literature is typically a probabilistic one. If we replace “belief” with “knowledge” above, then we have a very-well-studied notion, the formalization of knowledge by *possible worlds semantics*. The mathematical structures for possible worlds semantics are sets *W* of *worlds* with two functions, one giving for each world *w* ∈ *W* some set of “atomic propositions” true at *w*, and the other giving for each *w* some set of worlds which are said to be “possible from *w*”. These structures are essentially the coalgebras in the category Set of sets of the functor

> *F*(*x*) = ℘(*x*) × ℘(AtProp)

where AtProp is a set of atomic propositions and ℘ is the power set functor on sets. What we have with type spaces looks similar, the main difference being that ℘ is replaced by its counterpart Δ, replacing “subsets” by “probability measures on”.

The second clue has to do with the role of the universal type space in this field. Types are taken to be elements of the universal type space. In the universal type space all possible types are uniquely represented, and the idea is that two types with exactly the same beliefs about the underlying world of “nature” plus the types of the other players are taken to be undistinguishable. This is the same ideology as we find concerning *final coalgebras*, in which (under suitable hypotheses) points with the same behavior are identified.

The remainder of this section is a summary of what is known and a pointer to the literature, especially Heifetz and Samet (1998), Moss and Viglizzo (2006) and Viglizzo (2005).

The first relevant category is Meas , the category of measurable spaces and measurable functions between them. We have seen the definitions in [the supplement on measurable spaces](nonwellfounded-set-theory.harsanyi-type-spaces.md). We also saw the definition of Δ(*M*), the set of probability measures on the space *M*. What we did not see is the way Δ acts on morphisms to give a functor. If *f* : *M* → *N* is measurable, then for μ ∈ Δ(*M*) and *A* ∈ Σ′,

> (Δ f)(μ)(A) = μ(*f*⁻¹(*A*)).

That is, (Δ f)(μ) = μ ⋅ *f*⁻¹.

The category Meas has products and coproducts. The product space is the categorical product, and the coproduct is given by disjoint unions. However, Meas does not preserve weak pullbacks, and (worse) it does not preserve ωᵒᵖ limits (see Viglizzo 2005). We are not going to spell out the definitions here, but we mention them to point out that the failure of Δ to have various properties is directly related to the difficulty of the problem of constructing universal type spaces; for functors with nicer properties, the result comes more easy, and the techniques are more well-known.

The class of *measure polynomial functors* is the smallest class of functors on Meas containing the identity, the constant spaces *M* and closed under products, coproducts, and Δ.

> **Theorem** Every measure polynomial functor has a final coalgebra.

This result is not quite what we want in the formalization of universal type spaces. For one thing, there are no “players” around. We'll discuss matters for the case of two players; the more general case is basically the same. We repeat our earlier definition of a two-player type space: it is a tuple (*M*, σ, N, τ), where *M* and *N* are measurable spaces, and

> *σ*   :  *M* → Δ(*S* × *N*) *τ*   :  *N* → Δ(*S* × *M*)

Now we first of all want to reformulate this in terms of coalgebras. We fix *S* and take as our category *C* the category of pairs (*M*, *C*) of measurable spaces, with a morphism from (*M*₁, *N*₁) to (*M*₂, *N*₂) just being a pair of morphisms (*f*, *g*), where *f*   :  *M*₁ → *M*₂ and *g*   :  *N*₁ → *N*₂ We have an endofunctor *Δ*   :  *C* → *C* given by

> | Δ(*M*, *N*) | = | (Δ(*S* × *N*), Δ(*S* × *M*)) |
> | --- | --- | --- |
> | Δ(*f*, *g*) | = | ((id_{*S*} × *g*), ((id_{*S*} × *f*)) |

In these terms, we can say that a type space is a coalgebra of Δ on *C*. Further, every morphism between type spaces preserves the modal language of probabilistic belief which we discussed in [ our earlier supplement on universal Harsanyi type spaces](nonwellfounded-set-theory.harsanyi-type-spaces.md). In fact, these coalgebra morphisms had been considered in the literature earlier, before the connection to coalgebra was realized. Similarly, the matter of constructing a universal type space had been re-cast into that of constructing a final coalgebra (but not under that exact name) for Δ on *C*.

Most efforts to find such a final coalgebra had gone proceeded along a well-worn path of *finality via infinite iteration*. Categorically, this means taking an ωᵒᵖ-limit of the sequence obtained by iterating the functor, beginning with a final object. However, this functor Δ lacks some properties needed to make this construction work. The breakthrough came in Heifetz and Samet (1998). The point is that one can take the idea seriously that final coalgebras are like the records of possible observations of a system. Taking the idea seriously means that in the absence of a known final coalgebra, one may attempt to construct one out of the theories of all points in all coalgebras. The pleasant surprise is that this works. From the point of view of this entry, this suggests that the chart of dualities might be of some help in solving mathematical problems. The construction of Heifetz and Samet (1998) was generalized to the coalgebraic setting in Moss and Viglizzo (2006).

## Fractal sets and completely iterative algebras

Our final topic is the link between the mathematics of hypersets and coalgebras on the one hand, and fractal sets on the other.[^note-sup-note-14]

**Completely iterative algebras** Let *F* be an endofunctor on a category *C* with coproducts. A *completely iterative algebra* (*cia*) for *F* is an algebra (*A*, *a*) for *F* such that for all *e*   :  *X* → *FX* + *A*, there is a unique *e*^{†}   :  *X* → *A* such that the diagram below commutes:

> |   | *X* | *e* → | *FX* + *A* |
> | --- | --- | --- | --- |
> | *e*^{†} | ↓ |   | ↓  *Fe*^{†} + *id*_{*A*} |
> |   | *A* | ← [*a*, *id*_{*A*}] | *FA* + *A* |

There are two main kinds of examples for us. The first is from set theory. We take *C* to be Class, *F* to be ℘, and (*A*, *a*) to be (*V*, *i*). (Here, as earlier, *i*   :   ℘*V* → *V* is the identity, regarding a set of sets as a set.) Assuming *AFA*, we have a cia. This is the content of the Extended Graphs Theorem: what we called an extended graph corresponds to a function of the form *e*   :  *G* → ℘ *G* + *V*, and a decoration corresponds to *e*^{†}.

The fact that the universe (*V*, *i*) is a cia extends in two ways. First, every final coalgebra of any functor on any category is a cia, provided the category has a coproduct operation +. And returning to Class, the universe (*V*, *i*) is a cia of many other functors, including all of the power polynomials. This is the connection of the concept from this section to set theory.

It is the second kind of cia examples which connect our topic to fractal sets. We briefly recall a few definitions concerning metric spaces.

A *metric space* is a pair (*X*, *d*) where *X* is a set, and *d*   :  *X* × *X* → *R* has the following distance-like properties:

1. *d*(*x*, *y*) = 0 iff *x* = *y*.
2. *d*(*x*, *y*) = *d*(*y*, *x*).
3. *d*(*x*, *z*) ≤ *d*(*x*, *y*) + *d*(*y*, *z*).

A sequence *x*₀, *x*₁, *x*₂, … *converges to* *y* if for every ε > 0 there is some natural number *n* such that for all *m* > *n*, *d*(*x*ₙ, *y*) < ε. A *Cauchy sequence* in *X* is a sequence of points with the property that for every ε > 0 there is some number *N* such that for *m*, *n* > *N*, *d*(*x*_{*m*}, *x*_{*n*}) < ε. A metric space is *complete* if every Cauchy sequence in it has a limit; this limit is then unique.

Let (*X*, *d*) be a complete metric space. Consider the set *C*(*X*) of all non-empty compact subspaces of *X* together with the *Hausdorff metric* *h*; for two compact subsets *A* and *B* of *X*

> *h*(*A*, *B*)   =   max {*d*(*A* → *B*), *d*(*B* → *A*}

where *d*(*A* → *B*) = max_{*a* ∈ *A*} min_{*b* ∈ *B*} *d*(*a*, *b*). (*C*(*X*), *h*) is then a complete metric space.

CMS is the category of complete metric spaces with distances measured in the interval [0,1] together with maps *f*   :  *X* → *Y* such that *d*_{*Y*}(*fx*, *fy*) ≤ *d*_{*X*}(*x*, *y*) for all *x*, *y* ∈ *X*. These maps are called *non-expanding*. A stronger condition is that *f* be *ε-contracting*: for some ε < 1 we have that *d*_{*Y*}(*fx*, *fy*) ≤ ε ⋅ *d*_{*X*}(*x*, *y*) for all *x*, *y* ∈ *X*. If *f,g*   :  *X* → *Y*, we measure the distance between *f* and *g* by taking the supremum of *d*_{*Y*}(*fx*, *gx*) as *x* ranges over *X*. We write this as *d*(*f*, *g*). A functor *F* on CMS is called ε-*contracting* if there exists a constant ε < 1 such that for all non-expanding maps *f,g*   :  *X* → *Y*, *d*(*Ff*, *Ff*) ≤ ε ⋅ *d*(*f*, *g*)

> **Theorem** [Adámek and Reitermann (1994)] Let *F* be a contracting endofunctor on the category CMS of complete metric spaces. Then every non-empty *F*-algebra (*A*, *a*) is completely iterative.

**An example** Here is an example which is mathematically suggestive. We use the cia property to show that every system of equations like the one below has a *unique* solution in the unit interval of real numbers *I*= [0,1].

> | (2) | *x*₁ ≈ .5 *x*₂ |
> | --- | --- |
> |   | *x*₂ ≈ .5 *x*₃ + .5 *x*₅ |
> |   | *x*₃ ≈ .5 *x*₂ + *x*₅ |
> |   | *x*₄ ≈ .5 *x*₅ + *x*₅ |
> |   | … |

Let *F* be the functor on CMS taking a space (*X*, *d*) to the space (*X* + *X*, *d*^{*}), where *d*^{*} measures distances in the same copy of *X* by taking half the corresponding distance in (*X*, *d*) ; otherwise, *d*^{*}(*x*, *y*) = 1.

We use the following example (*I*, *a*) of an algebra for *F*: *I*= [0,1], and *a* : *FI* → *I* is given by *a*(inl(x)) = .5 *x*, and *a*(inr(x)) = .5 *x* + .5.

So (*I*, *a*) is a cia for *F*. We use this, taking *X* to be our set of variables, made into a metric space by setting *d*(*x*_{*m*}, *x*_{*n*}) = 1 unless *n* = *n*. We define *e* : *X* → *FX* + *I* as suggested from our example above: *e*(*x*₁) = *e*(*x*₁) = inl(inl(*x*₂)), *e*(*x*₁) = inl(inr(*x*₃)), etc. This particular system does not use the *I* summand, and the inr and inl just code whether the “ + .5 ” appears on the right of the equation.

Then the cia property gives a unique solution map *e*^{†}   : *X* → *I*. Tracing through the definitions of the functions involved shows that this is the desired solution.

**The Cantor set, again** Let *I* be the unit interval [0,1] , an object in CMS. The Cantor “middle third” set *c* may be obtained via the cia structure on *C*(*I*), the space of compact subsets of *I* with a metric as defined earlier in this supplement.

We take for *F*   :  CMS → CMS the functor which takes a metric space (*X*, *d*) to (*X*,1/3 ⋅ *d*). This is 1/3-contracting, and we use the non-empty *F*-algebra (*C*(*I*), α), where

> α(*S*)   =   (1/3 ⋅ *S*) ∪ (2/3 + 1/3 ⋅ *S*).

To use the cia structure, let *X* be a one-point space, and then let *e*   :  *X* → *X* + *C*(*I*) be inl. Then the solution is a map *e*^{†}   :  *X* → *C*(*I*). Its value on the point of *X* is then some *c* ∈ *C*(*I*) such that *c* = 1/3 ⋅ *c* ∪ (2/3 + 1/3 ⋅ *c*), just as desired. The uniqueness of *c* then also follows from the uniqueness of solutions in cias.

**The explanation** It might be useful to see why an equation like *c* = *c* /3 ∪ 2/3 + *c*/3 is related to the procedure of removing the middle third from each element in a collection of intervals.

Let *X* be the set of non-empty compact subsets of [0,1]. We define a function *f*   :  *X* → *X* by

> *f*(*f*)   =   (1/3 ⋅ *a*) ∪ (2/3 + 1/3 ⋅ *a*)

We want to solve *x* ≈ *f*(*x*). We start with an arbitrary *f* ∈ *A*. Then we form a sequence

> | *c*₀ | = | *a* |
> | --- | --- | --- |
> | *c*_{*n*+1} | = | *f*(*c*_{*n*}(*a*)) |

The space *X* has enough limits (this is where completeness enters), and the sequence *c*_{*n*}(*a*) is a Cauchy sequence in it. And so we have around to guarantee that it will have a limit. Call this limit *a*^{*} . Since *f* is continuous, we have

> *f*(*a*^{*})   =   *f*(*lim*_{*n*}*c*_{*n*}(*a*))   =   *lim*_{*n*}*f*(*c*_{*n*}(*a*))   =   *lim*_{*n*} *c*_{*n*+1}(*a*)   =   *a*^{*}.

Thus *a*^{*} is a solution to our equation, as desired. But the function *f* is actually, contracting in certain precise sense, and so by a standard metric argument, *a*^{*} will not depend on *a*: starting the iteration at any non-empty compact set would give the same result.

This follows iterative definition of the Cantor set. Let's take *a* to be [0,1] itself. Note that removing the middle-third of [0,1] is gives *f*(*a*). That is, rather than think of removal, think of shrinking the interval by one-third, putting one piece on [0,1/3] and the other on [2/3, 1] . It just so happens that these operations produce the same thing. And this coincidence persists at the second step: *f*(*f*(*a*)) consists of the four pieces [0,1/9] , [2/9, 1/3], [2/3, 7/9], and [8/9, 1]. So the iterative method is giving us the terms of the iteration sequence beginning with [0,1]. Finally, the iteration sequence *beginning with* [0,1] is a shrinking sequence of sets, and then by the way limits are calculated in *X*, the limit is exactly the intersection of the shrinking sequence.
