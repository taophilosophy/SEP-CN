# nonwellfounded-set-theory — harsanyi-type-spaces（supplement）

> （《nonwellfounded-set-theory》词条补充材料，源：plato.stanford.edu/entries/nonwellfounded-set-theory/harsanyi-type-spaces.html）

#### Supplement to Non-wellfounded Set Theory

## Universal Harsanyi type spaces

In the main body of this entry, we have been concerned with streams, trees, and sets, especially in settings where one wants one object to be a part (in some sense) of another, this to be a part of yet another, and so on ad infinitum. These are the standard motivating examples for the Anti-Foundation Axiom and related modeling techniques. In this section, we broaden the discussion by turning to another field.

Type spaces are mathematical structures used in theoretical parts of economics and game theory. The are used to model settings where agents are described by their *types*, and these types give us “beliefs about the world”, “beliefs about each other's beliefs about the world”, “beliefs about each other's beliefs about each other's beliefs about the world”, etc. That is, the formal concept of a type space is intended to capture in one structure an unfolding infinite hierarchy related to *interactive belief*.

John C. Harsanyi (1967) makes a related point as follows:

> It seems to me that the basic reason why the theory of games with incomplete information has made so little progress so far lies in the fact that these games give rise, or at least appear to give rise, to an infinite regress in reciprocal expectations on the part of the players.

This quote is from the landmark papers he published in 1967 and 1968, showing how to convert a game with incomplete information into one with complete yet imperfect information. Many of the details are not relevant here and would take us far from our topic. But three points are noteworthy. First, the notion of types goes further than what we described above: an agent *A*'s type involves (or induces) beliefs about the types of the other agents, their types involve beliefs about *A*'s type, etc. So the notion of a type is already circular.

Second, despite this circularity, the informal concept of a *universal type space* (as a single type space in which all types may be found) is widespread in areas of non-cooperative game theory and economic theory. And finally, the *formalization* of type spaces was left open: Harsanyi did not really formalize type spaces in his original papers (he used the notion); this was left to later researchers. Work started with Böge and Eisele (1979) and continued in several papers up through that of Heifetz and Samet(1998). It was later realized that there is a connection to the kind of work that is emphasized in this entry, and this connection is what we are concerned with, both in this section and in

> [A supplement on additional related modeling of circularity](nonwellfounded-set-theory.modeling-circularity.md)

Getting back to our very rough informal description above, what exactly are “beliefs”? And how can a structure contain types which give rise to beliefs about other types? What is the relation of this to the infinite hierarchy of beliefs about beliefs about … beliefs about the world? Can we characterize the space of all possible types?

Again, we are not concerned with conceptual matters concerning beliefs and games in this entry. Most of the important papers for our study are technical contributions dealing with the matter of *universal type spaces*. We are concerned with the conceptual matters related to our own topics, and with some of the technical matters connected with measure theory, probability, and the like.

Returning to type spaces, we recall that the usual modeling of belief in game theory is via probability. So we would expect that *type spaces should be probabilistic versions of Kripke models*. One should replace the functor ℘ with something like Δ where

> Δ(*W*) = {μ : μ is a probability measure on *W*}}.

Indeed, this is the case: most proposals in the literature do end up studying certain mappings from a space *X* to some variation of the functor Δ applied to *X*. This is our third clue of the connection. But note that this informal description leaves many loose ends: if *W* is just a set, how do we know that it has any probability measures? Does it matter which σ-algebra we use?

For the remainder of this discussion, we need the notion of a measurable space, which is defined in the following supplementary document:

> [Measurable Spaces](nonwellfounded-set-theory.measurable-spaces.md)

Let *S* be a fixed measurable space. A *type space over S* is a tuple T = (*M*, σ, *N*, τ), where *M* and *M* are measurable spaces, and

> σ : *M* → Δ(*S* × *N*)
>
> τ : *N* → Δ(*S* × *M*)

What we are describing would be better called a *two-player type space over S*, and the spaces *M* and *M* are the spaces of the two players. The idea is that *S* represents the possible “states of nature”, each *m* ∈ *M* is a possible “type” of the first player, and each *n* ∈ *N* is a possible type for the second. Each player does not know the exact state of nature or which type of player he or she faces. But each does have some probabilistic “opinion” on this matter: each σ(*m*) gives a measure on *S* × *N*, and so the first player can measure subsets of both *S* and *N* (using marginals).

One assumption incorporated into our definition is that the players “know” their own types. This is why σ(*m*) is a measure on *S* × *N* and not *S* × *M* × *N*. However, each μ ∈ Δ( *S* × *N*) and each *m* ∈ *M* together define a measure μ^{*}_{*m*} on the larger product *S* × *M* × *N* by concentrating μ on *m*:

> μ^{*}_{*m*}(*E*) = μ(*m*)({(*s*,*n*) : (*s*,*m*,*n*) ∈ *E*}).

Everything we said for the first player goes through for the second, mutatis mutandis, and so we also have measures ρ^{*}_{*n*} ∈ Δ (*S* × *M* × *N*) for each ρ ∈ Δ(*S* × *M*) and each *n* ∈ *N*.

The basic modal language for a type space over *S* would have the following sentences:

1. Each measurable subset *A* of *S* is taken as an atomic sentence.
2. If φ is a sentence and *p* ∈ [0,1], then both *B*¹_{*p*} φ and *B*²_{*p*} φ are sentences.
3. If φ and ψ are sentences, then so is φ ∧ ψ.

We read *B*ⁱ_{*p*} φ as saying that player *i* believes the probability of φ to be at least *p*.

We define a semantics for this language, interpreting each sentence φ by subset [φ] ⊆ *S* × *M* × *N* as follows:

1. [*A*] = *A* × *M* × *N*.
2. [*B*¹_{*p*} φ] = {(*s*, *m*, *n*): (σ(*m*)^{*}_{*m*}([φ]) ≥ p}
3. [*B*²_{*p*} φ] = {(*s*, *m*, *n*): (τ(*n*)^{*}_{*n*}([φ]) ≥ *p*}
4. [φ ∧ ψ] = [φ] ∩ [ψ].

One may also add negation or implication to the language, with the semantics from classical logic. A good first exercise would then be to show that

> [*B*¹_{*p*} φ → *B*¹₁ *B*¹_{*p*} φ] = *S* × *M* × *N*.

This is an echo of the assumption agents know their types: they are able to introspect on their own beliefs, and to do so with certainty.

**Reformulation of the problem of universal type spaces.** The language of beliefs is more natural than the formulation of type spaces (and it also came first), and so the reason for introducing type spaces is to interpret that language. One then wants a type space T^{*} which is rich enough to contain all possible types. It might be better to work on the semantic side, and consider, for each space T and each point *x* = (*s*,*m*,*n*), the theory of *x*; this is the set of sentences φ such that *x* ∈ [φ]. Let us call this set *th*(T,*x*). One wants a space T^{*} with the property that for all type spaces T and all *x* from it, there is a unique point *x*^{*} ∈ T^{*}, th(T,x) = th(T^{*},*x*^{*}). Intuitively, points with the same theory represent players with the same beliefs, beliefs about beliefs, etc., so they should be identified for the purposes of game theory. These theories then serve as surrogates for the types. A universal space T^{*} would contain a point realizing each theory of any point *x* (in any space), exactly one copy in fact. The mathematical problem is then to find such a space. Note that it is not clear that such a space exists in the first place: one requires the space T^{*} to be a set, and perhaps the universality requirement would force it to be a proper class.
