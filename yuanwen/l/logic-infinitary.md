# Infinitary Logic
**First published Sun Jan 23, 2000; substantive revision Wed Sep 6, 2023**

*Bell, John L.*

Traditionally, expressions in formal systems have been regarded as signifying finite inscriptions which are—at least in principle—capable of actually being written out in primitive notation. However, the fact that (first-order) formulas may be identified with natural numbers (via “Gödel numbering”) and hence with finite *sets* makes it no longer necessary to regard formulas as inscriptions, and suggests the possibility of fashioning “languages” some of whose formulas would be naturally identified as *infinite sets*. A “language” of this kind is called an *infinitary language*: in this article I discuss those infinitary languages which can be obtained in a straightforward manner from first-order languages by allowing conjunctions, disjunctions and, possibly, quantifier sequences, to be of infinite length. In the course of the discussion it will be seen that, while the expressive power of such languages far exceeds that of their finitary (first-order) counterparts, very few of them possess the “attractive” features (e.g., compactness and completeness) of the latter. Accordingly, the infinitary languages that do in fact possess these features merit special attention.

In §1 the basic syntax and semantics of infinitary languages are laid down; their expressive power is then displayed by means of examples. §2 is devoted to those infinitary languages which permit only finite quantifier sequences: these languages turn out to be relatively well-behaved. §3 is devoted to a discussion of the *compactness problem* for infinitary languages and its connection with purely set-theoretical questions concerning “large” cardinal numbers. In §4 an argument is sketched which shows that most “infinite quantifier” languages have a *second-order* nature and are, *ipso facto*, highly incomplete. §5 provides a brief account of a certain special class of sublanguages of infinitary languages for which a satisfactory generalization of the compactness theorem can be proved. This section includes a subsection on the definition of admissible sets. Historical and bibliographical remarks are provided in §6.

## 1. Definition and Basic Properties of Infinitary Languages

Given a pair κ, λ of infinite cardinals such that λ ≤ κ, we define a class of infinitary languages in each of which we may form conjunctions and disjunctions of sets of formulas of cardinality < κ, and quantifications over sequences of variables of length < λ.

Let L — the (finitary) *base language* — be an arbitrary but fixed first-order language with any number of extralogical symbols. The infinitary language L(κ,λ) has the following *basic symbols*:

- All symbols of L
- A set Var of individual variables, where the cardinality of Var (written: |Var|) is κ
- A logical operator ∧ (*infinitary conjunction*)

The class of *preformulas* of L(κ,λ) is defined recursively as follows:

- Each formula of L is a preformula;
- if φ and ψ are preformulas, so are φ∧ψ and ¬φ;
- if Φ is a set of preformulas such that |Φ| < κ, then ∧Φ is a preformula;
- if φ is a preformula and *X* ⊆ Var is such that |*X*| < λ, then ∃*X*φ is a preformula;
- all preformulas are defined by the above clauses.

If Φ is a set of preformulas indexed by a set *I*, say Φ = {φ_{*i*} : *i* ∈ *I*}, then we agree to write ∧Φ for:

> ∧_{*i*∈*I*} φ

or, if *I* is the set of natural numbers, we write ∧Φ for:

> φ₀ ∧ φ₁ ∧ …

If *X* is a set of individual variables indexed by an ordinal α, say *X* = {*x*_{ξ} : ξ < α}, we agree to write (∃*x*_{ξ})_{ξ<α}φ for ∃*X*φ.

The logical operators ∨, →, ↔ are defined in the customary manner. We also introduce the operators ∨ (*infinitary disjunction*) and ∀ (*universal quantification*) by

> ∨Φ =*_{df}* ¬∧{ ¬φ : φ ∈ Φ}
>
> ∀Xφ =*_{df}* ¬∃X¬φ,

and employ similar conventions as for ∧, ∃ .

Thus L(κ,λ) is the infinitary language obtained from L by permitting conjunctions and disjunctions of length < κ and quantifications[^note-1] of length < λ. Languages L(κ,ω) are called *finite-quantifier* languages, the rest *infinite-quantifier* languages. Observe that L(ω,ω) is just L itself.

Notice the following *anomaly* which can arise in an infinitary language but not in a finitary one. In the language L(ω₁,ω), which allows countably infinite conjunctions but only finite quantifications, there are preformulas with so many free variables that they cannot be “closed” into sentences of L(ω₁,ω) by prefixing quantifiers. Such is the case, for example, for the L(ω₁,ω)-preformula

> *x*₀ < *x*₁  ∧  *x*₁ < *x*₂  ∧  …  ∧  *xₙ* < *x*_{*n*+1} …,

where L contains the binary relation symbol <. For this reason we make the following

> Definition. A *formula* of L(κ,λ) is a preformula which contains < λ free variables. The set of all formulas of L(κ,λ) will be denoted by Form(L(κ,λ)) or simply Form(κ,λ) and the set of all sentences by Sent(L(κ,λ)) or simply Sent(κ,λ).

In this connection, observe that, in general, nothing would be gained by considering “languages” L(κ,λ) with λ > κ. For example, in the “language” L(ω,ω₁), formulas will have only finitely many free variables, while there will be a host of “useless” quantifiers able to bind infinitely many free variables.[^note-2]

Having defined the syntax of L(κ,λ), we next sketch its *semantics*. Since the extralogical symbols of L(κ,λ) are just those of L, and it is these symbols which determine the form of the structures in which a given first-order language is to be interpreted, it is natural to define an L(κ,λ)-structure to be simply an L-structure. The notion of a formula of L(κ,λ) being *satisfied* in an L-structure *A* (by a sequence of elements from the domain of *A*) is defined in the same inductive manner as for formulas of L except that we must add two extra clauses corresponding to the clauses for ∧Φ and ∃Xφ in the definition of preformula. In these two cases we naturally define:

> ∧Φ is satisfied in *A* (by a given sequence)  ⇔  for all φ ∈ Φ, φ is satisfied in *A* (by the sequence);
>
> ∃*X*φ is satisfied in *A*  ⇔  there is a sequence of elements from the domain of *A* in bijective correspondence with *X* which satisfies φ in *A*.

These informal definitions need to be tightened up in a rigorous development, but their meaning should be clear to the reader. Now the usual notions of *truth, validity, satisfiability*, and *model* for formulas and sentences of L(κ,λ) become available. In particular, if *A* is an L-structure and σ ∈ Sent(κ,λ), we shall write *A* ⊨ σ for A is a model of σ, and ⊨ σ for σ *is valid*, that is, for all *A*, *A* ⊨ σ. If Δ ⊆ Sent(κ,λ), we shall write Δ ⊨ σ for σ *is a logical consequence of* Δ, that is, each model of Δ is a model of σ.

We now give some examples intended to display the expressive power of the infinitary languages L(κ,λ) with κ ≥ ω₁. In each case it is well-known that the notion in question cannot be expressed in any first-order language.

Characterization of the standard model of arithmetic in L(ω₁,ω). Here the *standard model of arithmetic* is the structure N = ⟨*N*, +, ·, *s*, 0⟩, where *N* is the set of natural numbers, +, ·, and 0 have their usual meanings, and *s* is the successor operation. Let L be the first-order language appropriate for N. Then the class of L-structures isomorphic to N coincides with the class of models of the conjunction of the following L(ω₁,ω) sentences (where 0 is a name of 0):

> ∧_{*m*∈ω} ∧_{*n*∈ω} *s*^{*m*}0 + *s*^{*n*}0 = *s*^{*m*+*n*}0
>
> ∧_{*m*∈ω} ∧_{*n*∈ω} *s*^{*m*}0 · *s*^{*n*}0 = *s*^{*m*·*n*}0
>
> ∧_{*m*∈ω} ∧_{*n*∈ω−{*m*}} *s*^{*m*}0 ≠ *s*^{*n*}0
>
> ∀*x*∨_{*m*∈ω} *x* = *s*^{*m*}0

The terms *sⁿx* are defined recursively by

> | *s*⁰*x* | = | *x* |
> | --- | --- | --- |
> | *s*^{*n*+1}*x* | = | *s*(*sⁿx*) |

Characterization of the class of all finite sets in L(ω₁,ω). Here the base language has no extralogical symbols. The class of all finite sets then coincides with the class of models of the L(ω₁,ω)-sentence

> ∨_{*n*∈ω} ∃*v*₀ … ∃*vₙ*∀*x*(*x* = *v*₀ ∨ … ∨ *x* = *vₙ*).

Truth definition in L(ω₁,ω) for a countable base language L. Let L be a countable first-order language (for example, the language of arithmetic or set theory) which contains a name *n* for each natural number *n*, and let σ₀, σ₁, … be an enumeration of its sentences. Then the L(ω₁,ω)-formula

> Tr(*x*)  =*_{df}*  ∨_{*n*∈ω} (x = n ∧ σ*ₙ*)

is a *truth predicate* for L inasmuch as the sentence

> Tr(*n*) ↔ σ*ₙ*

is valid for each *n*.

Characterization of well-orderings in L(ω₁,ω₁). The base language L here includes a binary predicate symbol ≤. Let σ₁ be the usual L-sentence characterizing linear orderings. Then the class of L-structures in which the interpretation of ≤ is a well-ordering coincides with the class of models of the L(ω₁,ω₁) sentence σ = σ₁ ∧ σ₂, where

> σ₂ =*_{df}* (∀*vₙ*)_{*n*∈ω} ∃*x* [∨_{*n*∈ω} (*x = vₙ*) ∧ ∧_{*n*∈ω} (*x* ≤ *vₙ*)].

Notice that the sentence σ₂ contains an *infinite quantifier*: it expresses the essentially *second-order* assertion that every countable subset has a least member. It can in fact be shown that the presence of this infinite quantifier is essential: the class of well-ordered structures cannot be characterized in any finite-quantifier language. This example indicates that infinite-quantifier languages such as L(ω₁,ω₁) behave rather like second-order languages; we shall see that they share the latters' defects (incompleteness) as well as some of their advantages (strong expressive power).

Many extensions of first-order languages can be *translated* into infinitary languages. For example, consider the generalized quantifier language L(*Q*₀) obtained from L by adding a new quantifier symbol *Q*₀ and interpreting *Q*₀*x*φ(*x*) as *there exist infinitely many x such that* φ(*x*). It is easily seen that the sentence *Q*₀*x*φ(*x*) has the same models as the L(ω₁,ω)-sentence

> ¬∨_{*n*∈ω} ∃*v*₀…∃*vₙ*∀*x*[φ(*x*) → (*x = v*₀ ∨ … ∨ *x = vₙ*)].

Thus L(*Q*₀) is, in a natural sense, translatable into L(ω₁,ω). Another language translatable into L(ω₁,ω) in this sense is the *weak second-order language* obtained by adding a countable set of monadic predicate variables to L which are then interpreted as ranging over all *finite* sets of individuals.

Languages with arbitrarily long conjunctions, disjunctions and (possibly) quantifications may also be introduced. For a fixed infinite cardinal λ, the language L(∞,λ) is defined by specifying its class of formulas, Form(∞,λ), to be the union, over all κ ≥ λ, of the sets Form(κ,λ). Thus L(∞,λ) allows arbitrarily long conjunctions and disjunctions, in the sense that if Φ is an arbitrary subset of Form(∞,λ), then both ∧Φ and ∨Φ are members of Form(∞,λ). But L(∞,λ) admits only quantifications of length < λ: all its formulas have < λ free variables. The language L(∞,∞) is defined in turn by specifying its class of formulas, Form(∞,∞), to be the union, over all infinite cardinals λ, of the classes Form(∞,λ). So L(∞,∞) allows arbitrarily long quantifications in addition to arbitrarily long conjunctions and disjunctions. Note that Form(∞,λ) and Form(∞,∞) are proper classes in the sense of Gödel-Bernays set theory. Satisfaction of formulas of L(∞,λ) and L(∞,∞) in a structure may be defined by an obvious extension of the corresponding notion for L(κ,λ).

## 2. Finite-Quantifier Languages

We have remarked that infinite-quantifier languages such as L(ω₁,ω₁) resemble second-order languages inasmuch as they allow quantification over infinite sets of individuals. The fact that this is not permitted in finite-quantifier languages suggests that these may be in certain respects closer to their first-order counterparts than might be evident at first sight. We shall see that this is indeed the case, notably in the case of L(ω₁,ω).

The language L(ω₁,ω) occupies a special place among infinitary languages because—like first-order languages—it admits an effective *deductive apparatus*. In fact, let us add to the usual first-order axioms and rules of inference the new axiom scheme

> ∧Φ → φ

for any countable set Φ ⊆ Form(ω₁,ω) and any φ ∈ Φ, together with the new rule of inference

> | φ₀, φ₁, …, φ*ₙ*, … |
> | --- |
> | ∧_{*n*∈ω} φ_{*n*} |

and allow deductions to be of countable length. Writing ⊢* for deducibility in this sense, we then have the

> L(ω₁,ω)-Completeness Theorem. For any σ ∈ Sent(ω₁,ω), ⊨ σ  ⇔  ⊢*σ

As an immediate corollary we infer that this deductive apparatus is *adequate for deductions from countable sets of premises in* L(ω₁,ω). That is, with the obvious extension of notation, we have, for any *countable* set Δ ⊆ Sent(ω₁,ω)

> (2.1) Δ ⊨ σ  ⇔  Δ⊢*σ

This completeness theorem can be proved by modifying the usual Henkin completeness proof for first-order logic, or by employing Boolean-algebraic methods. Similar arguments, applied to suitable further augmentations of the axioms and rules of inference, yield analogous completeness theorems for many other finite-quantifier languages.

If just deductions of countable length are admitted, then no deductive apparatus for L(ω₁,ω) can be set up which is adequate for deductions from *arbitrary* sets of premises, that is, for which (2.1) would hold for every set Δ ⊆ Sent(ω₁,ω), *regardless of cardinality*. This follows from the simple observation that there is a first-order language L and an uncountable set Γ of L(ω₁,ω)-sentences such that Γ *has no model but every countable subset of* Γ *does*. To see this, let L be the language of arithmetic augmented by ω₁ new constant symbols {c_{ξ} : ξ < ω₁} and let Γ be the set of L(ω₁,ω)-sentences {σ} ∪ {*c*_{ξ} ≠ c_{η} : ξ ≠ η}, where σ is the L(ω₁,ω)-sentence characterizing the standard model of arithmetic. This example also shows that the *compactness theorem* fails for L(ω₁,ω) and so also for any L(κ,λ) with κ ≥ ω₁.

Another result which holds in the first-order case but fails for L(κ,ω) with κ ≥ ω₁ (and also for L(ω₁,ω₁), although this is more difficult to prove) is the *prenex normal form theorem*. A sentence is *prenex* if all its quantifiers appear at the front; we give an example of an L(ω₁,ω)-sentence which is not equivalent to a conjunction of prenex sentences. Let L be the first-order language without extralogical symbols and let σ be the L(ω₁,ω)-sentence which characterizes the class of finite sets. Suppose that σ were equivalent to a conjunction

> ∧_{*i*∈*I*} σ*ᵢ*

of prenex L(ω₁,ω)-sentences σ*ᵢ*. Then each σ*ᵢ* is of the form

> *Q*₁*x*₁ … *Q*ₙ*xₙ* φ*ᵢ*(*x*₁*,…, xₙ*),

where each *Qₖ* is ∀ or ∃ and φ*ᵢ* is a (possibly infinitary) conjunction or disjunction of formulas of the form *xₖ* = *xₗ* or *xₖ* ≠ *xₗ*. Since each σ*ᵢ* is a sentence, there are only finitely many variables in each φ*ᵢ*, and it is easy to see that each φ*ᵢ* is then equivalent to a first-order formula. Accordingly each σ*ᵢ* may be taken to be a first-order sentence. Since σ is assumed to be equivalent to the conjunction of the σ*ᵢ*, it follows that σ and the set Δ = {σ*ᵢ* : *i* ∈ *I*} have the same models. But obviously σ, and hence also Δ, have models of all finite cardinalities; the compactness theorem for sets of first-order sentences now implies that Δ, and hence also σ, has an infinite model, contradicting the definition of σ.

Turning to the *Löwenheim-Skolem theorem*, we find that the *downward* version has adequate generalizations to L(ω₁,ω) (and, indeed, to all infinitary languages). In fact, one can show in much the same way as for sets of first-order sentences that if Δ ⊆ Sent(ω₁,ω) has an infinite model of cardinality ≥ |Δ|, it has a model of cardinality the larger of ℵ₀, |Δ|. In particular, any L(ω₁,ω)-sentence with an infinite model has a countable model.

On the other hand, the *upward* Löwenheim-Skolem theorem in its usual form *fails* for all infinitary languages. For example, the L(ω₁,ω)-sentence characterizing the standard model of arithmetic has a model of cardinality ℵ₀ but no models of any other cardinality. However, all is not lost here, as we shall see.

We define the *Hanf number* h(L) of a language L to be the least cardinal κ such that, if an L-sentence has a model of cardinality κ, it has models of arbitrarily large cardinality. The existence of h(L) is readily established. For each L-sentence σ not possessing models of arbitrarily large cardinality let κ(σ) be the least cardinal κ such that σ does not have a model of cardinality κ. If λ is the supremum of all the κ(σ), then, if a sentence of L has a model of cardinality λ, it has models of arbitrarily large cardinality.

Define the cardinals μ(α) recursively by

> | μ(0) | = | ℵ₀ |
> | --- | --- | --- |
> | μ(α+1) | = | 2^{μ(α)} |
> | μ(λ) | = | ∑_{α<λ} μ(α), for limit λ. |

Then it can be shown that

> h(L(ω₁,ω)) = μ(ω₁),

similar results holding for other finite-quantifier languages. The values of the Hanf numbers of infinite-quantifier languages such as L(ω₁,ω₁) are sensitive to the presence or otherwise of large cardinals, but must in any case greatly exceed that of L(ω₁,ω).

A result for L which generalizes to L(ω₁,ω) but to no other infinitary language is the

> Craig Interpolation Theorem: If σ,τ ∈ Sent(ω₁,ω) are such that ⊨ σ → τ, then there is θ ∈ Sent(ω₁,ω) such that ⊨ σ → θ and ⊨ θ → τ, and each extralogical symbol occurring in θ occurs in both σ and τ.

The proof is a reasonably straightforward extension of the first-order case.

Finally, we mention one further result which generalizes nicely to L(ω₁,ω) but to no other infinitary language. It is well known that, if *A* is any finite L-structure with only finitely many relations, there is an L-sentence σ characterizing *A* up to isomorphism. For L(ω₁,ω) we have the following generalization known as

> Scott's Isomorphism Theorem. If *A* is a countable L-structure with only countably many relations, then there is an L(ω₁,ω)-sentence whose class of countable models coincides with the class of L-structures isomorphic with *A*.

The restriction to *countable* structures is essential because countability cannot in general be expressed by an L(ω₁,ω)-sentence.

The language L(∞,ω) may also be counted as a finite-quantifier language. The concept of equivalence of structures with respect to this language is of especial significance: we call two (similar) structures *A* and *B* (∞,ω)-*equivalent*, written *A* ≡_{∞ω} *B*, if the same sentences of L(∞,ω) hold in both *A* and *B*. This relation can, first of all, be characterized in terms of the notion of partial isomorphism. A *partial isomorphism* between *A* and *B* is a nonempty family *P* of maps such that:

- For each *p* ∈ *P*, dom(*p*) is a substructure of *A*, ran(*p*) is a substructure of B, and *p* is an isomorphism of its domain onto its range; and
- If *p* ∈ *P*, *a* ∈ *A*, *b* ∈ *B*, then there exist *r*, *s* ∈ *P* both extending *p* such that *a* ∈ dom(*r*), *b* ∈ ran(*s*) (“back and forth” property).

If a partial isomorphism exists between *A* and *B*, we say that *A* and *B* are partially isomorphic and write *A* ≅_{*p*} B. We then have

> Karp's Partial Isomorphism Theorem. For any similar structures *A*, *B*, *A* ≡_{∞ω} *B* ⇔ *A* ≅_{*p*} *B*.

There is also a version of Scott's isomorphism theorem for L(∞,ω), namely,

> (2.2) Given any structure *A*, there is an L(∞,ω)-sentence σ such that, for all structures *B*, *A* ≅_{*p*} *B* ⇔ *B* ⊨ σ.

Partial isomorphism and (∞,ω)-equivalence are related to the notion of *Boolean isomorphism*. To define this we need to introduce the idea of a Boolean-valued model of set theory. Given a complete Boolean algebra *B*, the *universe* *V*^{(*B*)} *of B-valued sets*, also known as the *B-extension of the universe V of sets*, is obtained by first defining, recursively on α,

> *V*_{α}^{(*B*)} = {*x*: *x* is a function ∧ range(*x*) ⊆ *B* ∧ ∃ξ<α[domain(*x*) ⊆ *V*_{ξ}^{(*B*)}]}

and then setting

> *V*^{(*B*)} = {*x*: ∃α(*x* ∈ *V*_{α}^{(*B*)})}.

Members of *V*^{(*B*)} are called *B-valued sets*. It is now easily seen that a *B*-valued set is precisely a *B*-valued function with domain a set of *B*-valued sets. Now let L be the first-order language of set theory and let L^{(*B*)} be the language obtained by adding to L a name for each element of *V*^{(*B*)} (we shall use the same symbol for the element and its name). One can now construct a mapping [·]^{(*B*)} of the (sentences of the) language L^{(*B*)} into *B*: for each sentence σ of L^{(*B*)}, the element [σ]^{(*B*)} of *B* is the “Boolean truth value” of σ in *V*^{(*B*)}. This mapping [·]^{(*B*)} is defined so as to send all the theorems of Zermelo-Fraenkel set theory to the top element 1 of *B*, i.e., to “truth”; accordingly, *V*^{(*B*)} may be thought of as a *Boolean-valued model of set theory*. In general, if [σ]^{(*B*)} = 1, we say that σ is *valid* in *V*^{(*B*)}, and write *V*^{(*B*)} ⊨ σ.

Now each *x* ∈ *V* has a canonical representative *x* in *V*^{(*B*)}, satisfying

> *x* = *y* iff *V*^{(*B*)} ⊨ *x* = *y* *x* ∈ *y* iff *V*^{(*B*)} ⊨ *x* ∈ *y*

We say that two similar structures *A*, *B* are Boolean isomorphic, written *A* ≅_{*b*} *B*, if, for some complete Boolean algebra *B*, we have *V*^{(*B*)} ⊨ *A* ≅ *B*, that is, if there is a Boolean extension of the universe of sets in which the canonical representatives of *A* and *B* are isomorphic with Boolean value 1. It can then be shown that:

> (2.3) *A* ≡_{∞ω} *B* ⇔ *A* ≅_{*b*} *B*.

This result can be strengthened through category-theoretic formulation. For this we require the concept of a(n) (elementary) *topos*. To introduce this concept, we start with the familiary category of Set of sets and mappings. Set has the following key properties:

1. There is a “terminal” object 1 such that, for any object *X*, there is a unique map *X* → 1 (for 1 we may take any one-element set, in particular, {0}).
2. Any pair of objects *X*,Y has a Cartesian product *X* × *Y*.
3. for any pair of objects one can form the “exponential” object *Y*^{*X*} of all maps from *X* → *Y*.
4. There is a “truth-value” object Ω such that for each object *X* there is a natural correspondence between subobjects (subsets) of *X* and maps *X* → Ω. (For Ω we may take the set 2 = {0,1}; maps *X* → Ω are then *characteristic functions* on *X*.)

All four of these conditions can be formulated in category-theoretic language — a category satisfying them is called a *topos*. The category Set is a topos; so also are (i) the category Set^{(*B*)} of Boolean-valued sets and mappings in any Boolean extension *V*^{(*B*)} of the universe of sets; (ii) the category of sheaves of sets on a topological space; (iii) the category of all diagrams of maps of sets

> *X*₀ → *X*₁ → *X*₂ → …

The objects of each of these categories may be regarded as sets which are *varying* in some manner: in case (i) over a *Boolean algebra*; in case (ii) over a topological *space*; in case (iii) over (discrete) time. A topos may be conceived, then, as a universe of “variable” sets. The familiar category Set is the special limiting case of a topos in which the “variation” of the objects has been reduced to zero.

Just as in set theory, “logical operators” can be defined on the truth-value object in any topos. These are maps ¬: Ω → Ω; ∧, ∨, ⇒: Ω × Ω → Ω corresponding to the logical operations of negation, conjunction, disjunction and implication. With these operations, Ω becomes a Heyting algebra, thus embodying in general the laws not of classical but of intutionistic logic. In this sense intuitionistic logic is “internalized” in a topos: intuitionistic logic is the logic of variable sets. (Of course, classical logic is internalized in certain toposes, for instance Set and Set^{(*B*)} for any complete Boolean algebra *B*.)

Any topos may be conceived as possible “universe of discourse” in which mathematical assertions may be interpreted and mathematical constructions may be performed. Mathematical assertions are rendered interpretable in a topos E by expression within E's *internal language* — a type-theoretic version of the usual language of set theory. In a manner analogous to Boolean-valued validity, one can introduce an appropriate notion of validity in E of a sentence σ of its internal language. Again, we write E ⊨ σ for “σ is valid in E”.

A topos E is said to be *full* if, for any set *I*, the *I*-fold copower[^note-3] ∐_{*I*}1 of its terminal object exists in E. ∐_{*I*}1 may be thought of as the canonical representative in E of the set *I*; accordingly, we write it simply as *I*. (In *V*^{(*B*)} this coincides with *I* as previously defined.) All the toposes mentioned above are full.

Now let E be a full topos. If *A* = (*A*, *R*, …) is a structure, write *A* for (*A*, *R*, …). Two structures *A* and *B* are said to be *topos isomorphic*, written *A* ≅_{*t*} *B*, if, for some topos E defined over the category of sets, we have E ⊨ *A* ≅ *B*. In other words two structures are topos isomorphic if their canonical representatives are isomorphic in the internal language of some topos. It can then be shown that

> (2.4) *A* ≡_{∞ω} *B* ⇔ *A* ≅_{*t*} *B*.

Accordingly (∞,ω)-equivalence may be regarded as isomorphism in the extremely general context of universes of “variable” sets. In this respect (∞,ω)-equivalence is an “invariant” notion of isomorphism.

## 3. The Compactness Property

As we have seen, the compactness theorem in its usual form fails for all infinitary languages. Nevertheless, it is of some interest to determine whether infinitary languages satisfy some suitably modified version of the theorem. This so-called *compactness problem* turns out to have a natural connection with purely set-theoretic questions involving “large” cardinal numbers.

We construct the following definition. Let κ be an infinite cardinal. A language L is said to be κ-*compact* (resp. *weakly* κ*-compact*) if whenever Δ is a set of L-sentences (resp. a set of L-sentences of cardinality ≤ κ) and each subset of Δ of cardinality < κ has a model, so does Δ. Notice that the usual compactness theorem for L is precisely the assertion that L is ω-compact. One reason for according significance to the κ-compactness property is the following. Call L κ-*complete* (resp. *weakly* κ-*complete*) if there is a deductive system *P* for L with deductions of length < κ such that, if Δ is a *P*-consistent[^note-4] set of L-sentences (resp. such that |Δ| ≤ κ), then Δ has a model. Observe that such a *P* will be adequate for deductions from arbitrary sets of premises (of cardinality ≤ κ) in the sense of §2. It is easily seen that if L is κ-complete or weakly κ-complete, then L is κ-compact or weakly κ-compact. Thus, if we can show that a given language is *not* (weakly) κ-compact, then there can be no deductive system for it with deductions of length < κ adequate for deductions from arbitrary sets of premises (of cardinality ≤ κ).

It turns out, in fact, that most languages L(κ,λ) fail to be even weakly κ-compact, and, for those that are, κ must be an exceedingly *large* cardinal. We shall need some definitions.

An infinite cardinal κ is said to be *weakly inaccessible* if

> (a) λ < κ → λ⁺ < κ, (where λ⁺ denotes the cardinal successor of λ), and
>
> (b) | *I* | < κ and λ*ᵢ* < κ (for all *i* ∈ *I*) ⇒ ∑_{*i*∈*I*} λ_{*i*} < κ.

If in addition

> (c) λ < κ ⇒ 2^{λ} < κ,

then κ is said to be (*strongly*)*inaccessible*. Since ℵ₀ is inaccessible, it is normal practice to confine attention to those inaccessible, or weakly inaccessible, cardinals that exceed ℵ₀. Accordingly, inaccessible or weakly inaccessible cardinals will always be taken to be *uncountable*. It is clear that such cardinals—if they exist—must be extremely large; and indeed the Gödel incompleteness theorem implies that the existence of even weakly inaccessible cardinals cannot be proved from the usual axioms of set theory.

Let us call a cardinal κ *compact* (resp. *weakly compact*) if the language L(κ,κ) is κ-compact (resp. weakly κ-compact). Then we have the following results:

> (3.1) ℵ₀ *is compact*. This is, of course, just a succinct way of expressing the compactness theorem for first-order languages.
>
> (3.2) κ is *weakly compact* ⇒ L(κ,ω) is *weakly* κ-*compact* ⇒ κ is *weakly inaccessible*. Accordingly, it is consistent (with the usual axioms of set theory) to assume that no language L(κ,ω) with κ ≥ ω₁ is weakly κ-compact, or, *a fortiori*, weakly κ-complete.
>
> (3.3) Suppose κ is inaccessible. Then κ is *weakly compact*  ⇔  L(κ,ω) is *weakly* κ-*compact*. Also, Also κ is weakly compact ⇒ *there is a set of* κ *inaccessibles before* κ. Thus a weakly compact inaccessible cardinal is exceedingly large; in particular it cannot be the first, second, …, *nᵗʰ*, … inaccessible.
>
> (3.4) κ *is compact* ⇒ κ *is inaccessible*. (But, by the result immediately above, the converse fails.)

Let Constr stand for Gödel's axiom of constructibility; recall that Constr is consistent with the usual axioms of set theory.

> (3.5) *If* Constr *holds, then there are no compact cardinals*.
>
> (3.6) *Assume* Constr *and let* κ *be inaccessible. Then* κ *is weakly compact* ⇔ L(ω₁,ω) *is weakly* κ-*compact for all* L.
>
> (3.7) *If* Constr *holds, then there are no cardinals* κ *for which* L(ω₁,ω) *is compact*. Accordingly, it is consistent with the usual axioms of set theory to suppose that there is no cardinal κ such that all languages L(ω₁,ω) are κ-complete. This result is to be contrasted with the fact that *all* first-order languages are ω-complete.

The import of these results is that the compactness theorem fails very badly for most languages L(κ,λ) with κ ≥ ω₁.

Some historical remarks are in order here. In the 1930s mathematicians investigated various versions of the so-called *measure problem* for sets, a problem which arose in connection with the theory of Lebesgue measure on the continuum. In particular, the following very simple notion of measure was formulated. If *X* is a set, a (countably additive two-valued nontrivial) *measure* on *X* is a map μ on the power set P*X* to the set {0, 1} satisfying:

> (a) μ(*X*) = 1,
>
> (b) μ({*x*}) = μ(∅) = 0 for all *x* ∈*X*, and
>
> (c) if *A* is any countable family of mutually disjoint subsets of *X*, then μ(∪*A*) = ∑{μ(*Y*) : *Y* ∈ *A*}.

Obviously, whether a given set supports such a measure depends only on its cardinality, so it is natural to define a cardinal κ to be *measurable* if all sets of cardinality κ support a measure of this sort. It was quickly realized that a measurable cardinal must be inaccessible, but the falsity of the converse was not established until the 1960s when Tarski showed that measurable cardinals are weakly compact and his student Hanf showed that the first, second, etc. inaccessibles are not weakly compact (cf. (3.3)). Although the conclusion that measurable cardinals must be monstrously large is now normally proved without making the detour through weak compactness and infinitary languages, the fact remains that these ideas were used to establish the result in the first instance.

## 4. Incompleteness of Infinite-Quantifier Languages

Probably the most important result about first-order languages is the *Gödel completeness theorem* which of course says that the set of all valid formulas of any first-order language L can be generated from a simple set of axioms by means of a few straightforward rules of inference. A major consequence of this theorem is that, if the formulas of L are coded as natural numbers in some constructive way, then the set of (codes of) valid sentences is *recursively enumerable*. Thus, the completeness of a first-order language implies that the set of its valid sentences is *definable* in a particularly simple way. It would accordingly seem reasonable, given an *arbitrary* language L, to turn this implication around and suggest that, if the set of valid L-sentences is *not* definable in some simple fashion, then *no* meaningful completeness result can be established for L, or, as we shall say, that L is *incomplete*. In this section we are going to employ this suggestion in sketching a proof that “most” *infinite quantifier* languages are incomplete in this sense.

Let us first introduce the formal notion of *definability* as follows. If L is a language, *A* an L-structure, and *X* a subset of the domain *A* of *A*, we say that *X* is *definable in* *A* by a formula φ(*x, y*₁,…,*yₙ*) of L if there is a sequence *a*₁,…,*aₙ* of elements of *A* such that *X* is the subset of all elements *x* ∈ *A* for which φ(*x, a*₁,…,*aₙ*) holds in *A*.

Now write *Val*(L) for the set of all the *valid* L-sentences, i.e., those that hold in every L-structure. In order to assign a meaning to the statement “*Val*(L) is definable”, we have to specify

1. a structure *C*(L)—the *coding structure* for L;
2. a particular one-one map—the *coding map*—of the set of formulas of L into the domain of *C*(L).

Then, if we identify *Val*(L) with its image in *C*(L) under the coding map, we shall interpret the statement “*Val*(L) is definable” as the statement “*Val*(L), regarded as a subset of the domain of *C*(L), is definable in *C*(L) by a formula of L.”

For example, when L is the first-order language L of arithmetic, Gödel originally used as coding structure the standard model of arithmetic ℕ and as coding map the well-known function obtained from the prime factorization theorem for natural numbers. The recursive enumerability of *Val*(L) then means simply that the set of codes (“Gödel numbers”) of members of *Val*(L) is definable in ℕ by an L-formula of the form ∃*y*φ(*x, y*), where φ(*x, y*) is a recursive formula.

Another, equivalent, coding structure for the first-order language of arithmetic is the structure[^note-5] ⟨*H*(ω), ∈ ⨡ *H*(ω)⟩ of *hereditarily finite sets*, where a set *x* is *hereditarily finite* if *x*, its members, its members of members, etc., are all finite. This coding structure takes account of the fact that first-order formulas are naturally regarded as finite sets.

Turning now to the case in which L is an infinitary language L(κ,λ), what would be a suitable coding structure in this case? We remarked at the beginning that infinitary languages were suggested by the possibility of thinking of formulas as set-theoretical objects, so let us try to obtain our coding structure by thinking about what kind of set-theoretical objects we should take infinitary formulas to be. Given the fact that, for each φ∈Form(κ,λ), φ and its subformulas, subsubformulas, etc., are all of length < κ,[^note-6] a moment's reflection reveals that formulas of L(κ,λ) “correspond” to sets *x hereditarily of cardinality* < κ in the sense that *x*, its members, its members of members, etc., are all of cardinality < κ. The collection of all such sets is written *H*(κ). *H*(ω) is the collection of *hereditarily finite* sets introduced above, and *H*(ω₁) that of all *hereditarily countable* sets.

For simplicity let us suppose that the only extralogical symbol of the base language L is the binary predicate symbol ∈ (the discussion is easily extended to the case in which L contains additional extralogical symbols). Guided by the remarks above, as coding structure for L(κ,λ) we take the structure,

> H(κ) =*_{df}* ⟨*H*(κ), ∈ ⨡ *H*(κ)⟩.

Now we can define the coding map of Form(κ,λ) into H(κ). First, to each basic symbol *s* of L(κ,λ) we assign a code object ^{⌈}*s*^{⌉} ∈ *H*(κ) as follows. Let {*v*_{ξ}: ξ < κ} be an enumeration of the individual variables of L(κ,λ).

> | Symbol | Code Object | Notation |
> | --- | --- | --- |
> | ¬ | 1 | ^{⌈}¬^{⌉} |
> | ∧ | 2 | ^{⌈}∧^{⌉} |
> | ∧ | 3 | ^{⌈}∧^{⌉} |
> | ∃ | 4 | ^{⌈}∃^{⌉} |
> | ∈ | 5 | ^{⌈} ∈ ^{⌉} |
> | = | 6 | ^{⌈}=^{⌉} |
> | *v*_{ξ} | ⟨0,ξ⟩ | ^{⌈}*v*_{ξ}^{⌉} |

Then, to each φ ∈ Form(κ,λ) we assign the code object ^{⌈}φ^{⌉} recursively as follows:

> ^{⌈}*v*_{ξ} = *v*_{η}^{⌉}  =*_{df}*  ⟨^{⌈}*v*_{ξ}^{⌉}, ^{⌈}=^{⌉}, ^{⌈}*v*_{η}^{⌉}⟩,
>
> ^{⌈}*v*_{ξ} ∈ *v*_{η}^{⌉}  =*_{df}*  ⟨^{⌈}*v*_{ξ}^{⌉}, ^{⌈}∈^{⌉}, ^{⌈}*v*_{η}^{⌉}⟩;

for φ, ψ ∈ Form(κ,λ),

> ^{⌈}φ ∧ ψ^{⌉}  =*_{df}*  ⟨^{⌈}φ^{⌉}, ^{⌈}∧^{⌉}, ^{⌈}ψ^{⌉}⟩
>
> ^{⌈}¬φ^{⌉}  =*_{df}*  ⟨^{⌈}¬^{⌉}, ^{⌈}φ^{⌉}⟩
>
> ^{⌈}∃*X*φ^{⌉}  =*_{df}*  ⟨^{⌈}∃^{⌉}, {^{⌈}*x*^{⌉}: *x* ∈ *X*}, ^{⌈}φ^{⌉}⟩;

and finally if Φ ⊆ Form(κ,λ) with |Φ| < κ,

> ^{⌈}∧Φ^{⌉}  =*_{df}*  ⟨^{⌈}∧^{⌉}, {^{⌈}φ^{⌉}: φ ∈ Φ}⟩.

The map φ ↦ ^{⌈}φ^{⌉} from Form(κ,λ) into *H*(κ) is easily seen to be one-one and is the required coding map. Accordingly, we agree to identify *Val*(L(κ,λ)) with its image in *H*(κ) under this coding map.

When is *Val*(L(κ,λ)) a *definable* subset of H(κ)? In order to answer this question we require the following definitions.

An L-formula is called a Δ₀-*formula* if it is equivalent to a formula in which all quantifiers are of the form ∀*x*∈*y* or ∃*x*∈*y* (i.e., ∀*x*(*x*∈*y* → …) or ∃*x*(*x*∈*y* ∧ …)). An L-formula is a Σ₁-*formula* if it is equivalent to one which can be built up from atomic formulas and their negations using only the logical operators ∧, ∨, ∀*x*∈*y*, ∃*x*. A subset *X* of a set *A* is said to be Δ₀ (resp. Σ₁) *on A* if it is definable in the structure ⟨*A*, ∈ ⨡ *A*⟩ by a Δ₀- (resp. Σ₁-) formula of L.

For example, if we identify the set of natural numbers with the set *H*(ω) of hereditarily finite sets in the usual way, then for each *X* ⊆ *H*(ω) we have:

> *X* is Δ₀ on *H*(ω) ⇔ *X* is recursive
>
> *X* is Σ₁ on *H*(ω) ⇔ *X* is recursively enumerable.

Thus the notions of Δ₀- and Σ₁-set may be regarded as generalizations of the notions of *recursive* and *recursively enumerable* set, respectively.

The completeness theorem for L implies that *Val*(L) — regarded as a subset of *H*(ω) — is recursively enumerable, and hence Σ₁ on *H*(ω). Similarly, the completeness theorem for L(ω₁,ω) (see §2) implies that *Val*(L(ω₁,ω)) — regarded as a subset of *H*(ω₁) — is Σ₁ on *H*(ω₁). However, this pleasant state of affairs collapses completely as soon as L(ω₁,ω₁) is reached. For one can prove

> Scott's Undefinability Theorem for L(ω₁,ω₁). *Val*(L(ω₁,ω₁)) *is not definable in* H(ω₁) *even by an* L(ω₁,ω₁)-*formula*; *hence* a fortiori *Val*(L(ω₁,ω₁)) *is not* Σ₁ *on* *H*(ω₁).

This theorem is proved in much the same way as the well-known result that the set of (codes of) valid sentences of the second-order language of arithemetic L² is not second-order definable in its coding structure ℕ. To get this latter result, one first observes that ℕ is characterized by a single L²-sentence, and then shows that, if the result were false, then “truth in ℕ” for L²-sentences would be definable by an L²-formula, thereby violating Tarski's theorem on the undefinability of truth.

Accordingly, to prove Scott's undefinability theorem along the above lines, one needs to establish:

> (4.1) *Characterizability of the coding structure* H(ω₁) *in* L(ω₁,ω₁): there is an L(ω₁,ω₁)-sentence τ₀ such that, for all L-structures *A*, *A* ⊨ τ₀  ⇔  *A* ≅ H(ω₁).
>
> (4.2) *Undefinability of truth for* L(ω₁,ω₁)-*sentences* *in the coding structure*: there is no L(ω₁,ω₁)-formula φ(*v*₀) such that, for all L(ω₁, ω₁)-sentences σ, H(ω₁) ⊨ σ↔φ(^{⌈}σ^{⌉}).
>
> (4.3) *There is a term* *t*(*v*₀, *v*₁) *of* L(ω₁,ω₁) *such that, for each pair of sentences* σ, τ *of* L(ω₁,ω₁), H(ω₁)  ⊨  [*t*(^{⌈}σ^{⌉},^{⌈}τ^{⌉}) = ^{⌈}σ → τ^{⌉}].

(4.1) is proved by analyzing the set-theoretic definition of H(ω₁) and showing that it can be “internally” formulated in L(ω₁,ω₁). (4.2) is established in much the same way as Tarski's theorem on the undefinability of truth for first- or second-order languages. (4.3) is obtained by formalizing the definition of the coding map σ ↦ ^{⌈}σ^{⌉} in L(ω₁,ω₁).

Armed with these facts, we can obtain Scott's undefinability theorem in the following way. Suppose it were false; then there would be an L(ω₁,ω₁)-formula θ(*v*₀) such that, for all L(ω₁,ω₁)-sentences σ,

> (4.4) H(ω₁) ⊨ θ(^{⌈}σ^{⌉})  iff   σ ∈ *Val*(L(ω₁,ω₁)).

Let τ₀ be the sentence given in (4.1). Then we have, for all L(ω₁,ω₁)-sentences σ,

> H(ω₁) ⊨ σ   iff   (τ₀ → σ) ∈ *Val*(L(ω₁,ω₁)),

so that, by (4.4),

> H(ω₁) ⊨ σ   iff   H(ω₁) ⊨ θ(^{⌈}τ₀ → σ^{⌉}).

If *t* is the term given in (4.3), it would follow that

> H(ω₁) ⊨ σ↔θ(*t*(^{⌈}τ₀^{⌉}, ^{⌈}σ^{⌉})).

Now write φ(*v*₀) for the L(ω₁,ω₁)-formula θ(*t*(^{⌈}τ₀^{⌉}, ^{⌈}σ^{⌉})). Then

> H(ω₁) ⊨ σ↔φ(^{⌈}σ^{⌉}),

contradicting (4.2), and completing the proof.

Thus *Val*(L(ω₁,ω₁)) is not definable *even by an* L(ω₁,ω₁)-*formula*, so *a fortiori* L(ω₁,ω₁) is incomplete. Similar arguments show that Scott's undefinability theorem continues to hold when ω₁ is replaced by any successor cardinal κ⁺; accordingly the languages L(κ⁺,κ⁺) are all incomplete.[^note-7]

## 5. Sublanguages of L(ω₁,ω) and the Barwise Compactness Theorem

Given what we now know about infinitary languages, it would seem that L(ω₁,ω) is the only one to be reasonably well behaved. On the other hand, the failure of the compactness theorem to generalize to L(ω₁,ω) in any useful fashion is a severe drawback as far as applications are concerned. Let us attempt to analyze this failure in more detail.

Recall from §4 that we may code the formulas of a first-order language L as hereditarily finite sets, i.e., as members of *H*(ω). In that case each finite set of (codes of) L-sentences is also a member of *H*(ω), and it follows that the compactness theorem for L can be stated in the form:

> (5.1) If Δ ⊆ Sent(L) is such that each subset Δ₀ ⊆ Δ, Δ₀ ∈ *H*(ω) has a model, so does Δ.

Now it is well-known that (5.1) is an immediate consequence of the *generalized completeness theorem* for L, which, stated in a form similar to that of (5.1), becomes the assertion:

> (5.2) If Δ ⊆ Sent(L) and σ ∈ Sent(L) satisfy Δ ⊨ σ, then there is a deduction *D* of σ from Δ such that *D* ∈ *H*(ω).[^note-8]

In §2 we remarked that the compactness theorem for L(ω₁,ω) fails very strongly; in fact, we constructed a set Γ ⊆ Sent(ω₁,ω) such that

> (5.3) Each countable subset of Γ has a model but Γ does not.

Recall also that we introduced the notion of *deduction* in L(ω₁,ω); since such deductions are of countable length it quickly follows from (5.3) that

> (5.4) There is a sentence[^note-9]σ ∈ Sent(ω₁,ω) such that Γ ⊨ σ, but there is no deduction of σ in L(ω₁,ω) from Γ.

Now the formulas of L(ω₁, ω) can be coded as members of H(ω₁), and it is clear that H(ω₁) is closed under the formation of countable subsets and sequences. Accordingly (5.3) and (5.4) may be written:

> (5.3 *bis*) Each Γ₀ ⊆ Γ such that Γ₀ ∈ H(ω₁) has a model, but Γ does not;
>
> (5.4 *bis*) There is a sentence σ ∈ Sent(ω₁,ω) such that Γ ⊨ σ, but there is no deduction *D* ∈ *H*(ω₁) of σ from Γ.

It follows that (5.1) and (5.2) fail when “L” is replaced by “L(ω₁,ω)” and “H(ω)” by “H(ω₁)”. Moreover, it can be shown that the set Γ ⊆ Sent(ω₁,ω) in (5.3 *bis*) and (5.4 *bis*) may be taken to be Σ₁ on *H*(ω₁). Thus the compactness and generalized completeness theorems fail even for Σ₁-sets of L(ω₁, ω)-sentences.

We see from (5.4 *bis*) that the reason why the generalized completeness theorem fails for Σ₁-sets in L(ω₁,ω) is that, roughly speaking, *H*(ω₁) is not “closed” under the formation of deductions from Σ₁-sets of sentences in *H*(ω₁). So in order to remedy this it would seem natural to replace *H*(ω₁) by sets *A* which are, in some sense, closed under the formation of such deductions, and then to consider just those formulas whose codes are in *A*.

We now give a sketch of how this can be done.

First, we identify the symbols and formulas of L(ω₁,ω) with their codes in *H*(ω₁), as in §4. For each countable transitive[^note-10] set *A*, let

> L_{*A*} = Form(L(ω₁,ω)) ∩ *A*.

We say that L*_{A}* is a *sublanguage* of L(ω₁,ω) if the following conditions are satisfied:

1. L ⊆ L*_{A}*
2. if φ, ψ ∈ L*_{A}*, then φ ∧ ψ ∈ L*_{A}* and ¬φ ∈ L*_{A}*
3. if φ ∈ L*_{A}* and *x* ∈ *A*, then ∃*x*φ ∈ L*_{A}*
4. if φ(*x*) ∈ L*_{A}* and *y* ∈ *A*, then φ(*y*) ∈ L*_{A}*
5. if φ ∈ L*_{A}*, every subformula of φ is in L*_{A}*
6. if Φ ⊆ L*_{A}* and Φ ∈ *A*, then ∧Φ ∈ L*_{A}*.

The notion of deduction in L*_{A}* is defined in the customary way; if Δ is a set of sentences of L*_{A}* and φ ∈ L*_{A}*, then a *deduction* of φ from Δ in L*_{A}* is a deduction of φ from Δ in L(ω₁, ω) every formula of which is in L*_{A}*. We say that φ is *deducible* from Δ in L*_{A}* if there is a deduction *D* of φ from Δ in L*_{A}*; under these conditions we write Δ ⊢*_{A}* φ. In general, *D* will not be a member of *A*; in order to ensure that such a deduction can be found in *A* it will be necessary to impose further conditions on *A*.

Let *A* be a countable transitive set such that L*_{A}* is a sublanguage of L(ω₁, ω) and let Δ be a set of sentences of L*_{A}*. We say that *A* (or, by abuse of terminology, L*_{A}*) is Δ-*closed* if, for any formula φ of L*_{A}* such that Δ ⊢*_{A}* φ, there is a deduction *D* of φ from Δ such that *D* ∈ *A*. It can be shown that the only countable language which is Δ-closed for *arbitrary* Δ is the first-order language L, i.e., when *A* = *H*(ω). However J. Barwise discovered that there are countable sets *A* ⊆ *H*(ω₁) whose corresponding languages L*_{A}* differ from L and yet are Δ-closed *for all* Σ₁-*sets of sentences* Δ. Such sets *A* are called *admissible sets*; roughly speaking, they are extensions of the hereditarily finite sets in which recursion theory—and hence proof theory—are still possible (for the full definition, see Section 5.1 below).

From Barwise's result one obtains immediately the

> Barwise Compactness Theorem. *Let* A *be a countable admissible set and let* Δ *be a set of sentences of* L_{*A*} *which is* Σ₁ *on* A. *If each* Δ′ ⊆ Δ *such that* Δ′ ∈ A *has a model, then so does* Δ.

The presence of “Σ₁” here indicates that this theorem is a generalization of the compactness theorem for *recursively enumerable* sets of sentences.

Another version of the Barwise compactness theorem, useful for constructing models of set theory, is the following. Let ZFC be the usual set of axioms for Zermelo-Fraenkel set theory, including the axiom of choice. Then we have:

> 5.5 Theorem. Let A be a countable transitive set such that A = ⟨*A*, ∈ ⨡ *A*⟩ is a model of ZFC. *If* Δ *is a set of sentences of* L*_{A}* which is definable in A by a formula of the language of set theory and if each Δ′ ⊆ Δ *such that* Δ′ ∈ *A has a model, so does* Δ.

To conclude, we give a simple application of this theorem. Let *A* = ⟨*A*, ∈ ⨡ *A*⟩ be a model of ZFC. A model *B* = ⟨*B, E*⟩ of ZFC is said to be a *proper end-extension* of *A* if (i) *A* ⊆ *B*, (ii) *A* ≠ *B*, (iii) *a* ∈ *A, b* ∈ *B*, *bEa* ⇒ *b*∈*A*. Thus a proper end-extension of a model of ZFC is a proper extension in which no “new” element comes “before” any “old” element. As our application of 5.5 we prove

> 5.6 Theorem. Each countable transitive model of ZFC has a proper end-extension.
>
> Proof. Let *A* = ⟨*A*, ∈ ⨡ *A*⟩ be a transitive model of ZFC and let L be the first-order language of set theory augmented by a name a for each *a* ∈ *A*, and an additional constant c. Let Δ be the set of L*_{A}*-sentences comprising:
>
> - all axioms of ZFC;
> - c ≠ a, for each *a* ∈ *A*;
> - ∀*x*(*x* ∈ a → ∨_{*b*∈*a*} *x* = b), for each *a* ∈ *A*;
> - a ∈ b, for each *a* ∈ *b* ∈ *A*.
>
> It is easily shown that Δ is a subset of *A* which is definable in *A* by a formula of the language of set theory. Also, each subset Δ′ ⊆ Δ such that Δ′ ∈ *A* has a model. For the set *C* of all *a* ∈ *A* for which a occurs in Δ′ belongs to *A* — since Δ′ does — and so, if we interpret c as any member of the (necessarily nonempty) set *A − C*, then *A* is a model of Δ′. Accordingly, (5.5) implies that Δ has a model ⟨*B, E*⟩. If we interpret each constant a as the element *a* ∈ *A*, then ⟨*B, E*⟩ is a proper end-extension of *A*. The proof is complete.

The reader will quickly see that the first-order compactness theorem will not yield this result.

### 5.1 Definition of the Concept of Admissible Set

A nonempty transitive set *A* is said to be *admissible* when the following conditions are satisfied:

1. if *a, b* ∈ *A*, then {*a, b*} ∈ *A* and ∪*A* ∈ *A*;
2. if *a* ∈ *A* and *X* ⊆ *A* is Δ₀ on *A*, then *X* ∩ *a* ∈ *A*;
3. if *a* ∈ *A*, *X* ⊆ *A* is Δ₀ on *A*, and ∀*x*∈*a*∃*y*(<*x*,*y*> ∈ *X*), then, for some *b* ∈ *A*, ∀*x*∈*a*∃*y*∈*b*(<*x*,*y*> ∈ *X*).

Condition (ii) — the Δ₀-*separation scheme* — is a restricted version of Zermelo's axiom of separation. Condition (iii) — a similarly weakened version of the axiom of replacement — may be called the Δ₀-*replacement scheme*.

It is quite easy to see that if *A* is a transitive set such that <*A*, ∈ | *A*> is a model of ZFC, then *A* is admissible. More generally, the result continues to hold when the power set axiom is omitted from ZFC, so that both *H*(ω) and *H*(ω₁) are admissible. However, since the latter is uncountable, the Barwise compactness theorem fails to apply to it.

## 6. Historical and Bibliographical Remarks

§§1 and 2. Infinitary propositional and predicate languages seem to have made their first explicit appearance in print with the papers of Scott and Tarski [1958] and Tarski [1958]. The completeness theorem for L(ω₁,ω), as well as for other infinitary languages, was proved by Karp [1964]. The Hanf number calculations for L(ω₁,ω) were first performed by Morley [1965]. The nondefinability of well-orderings in finite-quantifier languages was proved by Karp [1965] and Lopez-Escobar [1966]. The interpolation theorem for L(ω₁,ω) was proved by Lopez-Escobar [1965] and Scott's isomorphism theorem for L(ω₁,ω) by Scott [1965]. Negri [2021] extends the idea of geometric logic originating in topos theory to L(ω₁,ω).

Karp's partial isomorphism theorem was first proved in Karp [1965]; see also Barwise [1973]. Result (2.2) appears in Chang [1968], result (2.3) in Ellentuck [1976] and result (2.4) in Bell [1981].

§3. Results (3.2) and (3.3) are due to Hanf [1964], with some refinements by Lopez-Escobar [1966] and Dickmann [1975], while (3.4) was proved by Tarski. Result (3.5) is due to Scott [1961], (3.6) to Bell [1970] and [1972]; and (3.7) to Bell [1974]. Measurable cardinals were first considered by Ulam [1930] and Tarski [1939]. The fact that measurable cardinals are weakly compact was noted in Tarski [1962].

§4. Concerning the undefinability theorem for L(ω₁,ω₁). Carol Karp remarks (1964, 166), “At the International Congress of Logic, Methodology and the Philosophy of Science at Stanford University in 1960, Dana Scott circulated an outline of a proof of the impossibility of a complete definable formal system for (γ+, γ+) languages with a single two-place predicate symbol in addition to the equality symbol.” Scott never published his result, and a fully detailed proof first appeared in Karp [1964]. The approach to the theorem adopted here is based on the account given in Dickmann [1975].

§5. The original motivation for the results presented in this section came from Kreisel; in his [1965] he pointed out that there were no compelling grounds for choosing infinitary formulas solely on the grounds of “length”, and proposed instead that definability or “closure” criteria be employed. Kreisel's suggestion was taken up with great success by Barwise [1967], where his compactness theorem was proved. The notion of admissible set is due to Platek [1966]. Theorem (5.6) is taken from Keisler [1974].

For further reading on the subject of infinitary languages, see Aczel [1973], Dickmann [1975], Karp [1964], Keisler [1974], and Makkai [1977]. A useful account of the connection between infinitary languages and large cardinals can be found in Chapter 10 of Drake [1974].

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=logic-infinitary). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/logic-infinitary/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=logic-infinitary&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](http://philpapers.org/sep/logic-infinitary/) at [PhilPapers](http://philpapers.org/), with links to its database. |

## Other Internet Resources

- [A Primer on Infinitary Logic](http://homepages.math.uic.edu/~marker/inf.pdf), by David Marker (Mathematics, Statistics, and Computer Science, University of Illinois/Chicago).

## Related Entries

Boolean algebra: the mathematics of | category theory | logic: classical

## Notes（原文脚注）

## Notes to Infinitary Logic

[^note-1]: Observe, however, that while the formation rules for L(κ,λ) allow the deployment of infinitely many quantifiers, each preformula can contain only finitely many *alternations* of quantifiers. Languages permitting infinite quantifier alternations have been developed in the literature, but we shall not discuss them here.

[^note-2]: This remark loses its force when the base language contains predicate symbols with infinitely many argument places. However, this possibility is excluded here since our base language is a conventional first-order language.

[^note-3]: The *I*-*fold* copower of an object *A* is an object

> ∐_{*I*} *A*

together with arrows

> | *A* | →_{σ}*i* | ∐_{*I*}*A* | (*i* ∈ *I*) |
> | --- | --- | --- | --- |

such that, for any arrows ƒ_{*i*} : *A* → *B* (*i* ∈ *I*), there is a unique arrow

> | ∐_{*I*}*A* | →_{*h*} | *B* |
> | --- | --- | --- |

for which ƒ_{*i*} = *h* ○ σ_{*i*} for all *i* ∈ *I*.

[^note-4]: I.e., such that no contradictions can be derived from Δ using the deductive machinery in *P*.

[^note-5]: If *A* is a set, ∈ ⨡ *A* denotes the membership relation on *A*, i.e., {⟨*x, y*⟩ ∈ *A* × *A* : *x* ∈ *y*}.

[^note-6]: Strictly speaking, this is only the case when κ is *regular*, that is, not the limit of < κ cardinals each of which is < κ. In view of the fact that “most” cardinals are regular, we shall take this as read.

[^note-7]: It should be pointed out, however, that there are languages L(κ,λ) apart from L(ω,ω) and L(ω₁,ω) which are complete; for example, all languages L(κ⁺,ω) and L(λ,λ) with inaccessible λ.

[^note-8]: This is just a consequence of the fact that a first-order deduction is a finite sequence, hence a member of *H*(ω).

[^note-9]: Take σ to be any logically false sentence!

[^note-10]: A set *A* is *transitive* if *x* ∈ *y* ∈ *A* ⇒ *x* ∈ *A*.

[^aczel-1973]: Aczel, P., 1973, “Infinitary Logic and the Barwise Compactness Theorem”, *Proceedings of the 1971 Bertrand Russell Memorial Logic Conference* (Uldum, Denmark), J. Bell, J. Cole, G. Priest, and A. Slomson (eds.), Leeds: Bertrand Russell Memorial Logic Conference, 234–277.

[^barwise-1967]: Barwise, J., 1967, *Infinitary Logic and Admissible Sets*. Ph.D. Thesis, Stanford University.

[^barwise-1973]: –––, 1973, “Back and Forth through Infinitary Logic. Studies in Model Theory”, in *Studies in Mathematics* (Volume 8), Buffalo: Mathematical Association of American, pp. 5–34.

[^barwise-1975]: –––, 1975, *Admissible Sets and Structures*, Berlin: Springer-Verlag.

[^barwise-1985]: Barwise, J. and S. Feferman (eds.), 1985, *Handbook of Model-Theoretic Logics*, New York: Springer-Verlag.

[^baumgartner-1974]: Baumgartner, J., 1974, “The Hanf number for complete L_{ω1},ω sentences (without GCH)”, *Journal of Symbolic Logic*, 39: 575–578.

[^bell-1970]: Bell, J. L., 1970, “Weak Compactness in Restricted Second-Order Languages”, *Bulletin of the Polish Academy of Sciences*, 18: 111–114.

[^bell-1972]: –––, 1972, “On the Relationship between Weak Compactness in L_{ω1}, ω, L_{ω1}, ω₁, and Restricted Second-Order Languages”, *Archive for Mathematical Logic*, 15: 74–78.

[^bell-1974]: –––, 1974, “On Compact Cardinals”, *Zeitschrift für Mathematical Logik und Grundlagen der Mathematik*, 20: 389–393.

[^bell-1981]: –––, 1981, “Isomorphism of Structures in S-toposes”, *Journal of Symbolic Logic*, 43 (3): 449–459.

[^chang-1968]: Chang, C.C., 1968, “Some Remarks on the Model Theory of Infinitary Languages”. in *The Syntax and Semantics of Infinitary Languages* (Lecture Notes in Mathematics: Volume 72), J. Barwise (ed.), Springer-Verlag, Berlin, 36-63.

[^dickmann-1975]: Dickmann, M. A., 1975, *Large Infinitary Languages*, Amsterdam: North-Holland.

[^drake-1974]: Drake, F.R., 1974, *Set Theory: An Introduction to Large Cardinals*, Amsterdam: North-Holland Publishing Company.

[^ellentuck-1976]: Ellentuck, E., 1976, “Categoricity Regained”, *Journal of Symbolic Logic*, 41 (3): 639–643.

[^hanf-1964]: Hanf, W. P., 1964, *Incompactness in Languages with Infinitely Long Expressions*, Amsterdam: North-Holland.

[^karp-1964]: Karp, C., 1964, *Languages with Expressions of Infinite Length*, Amsterdam: North-Holland.

[^karp-1965]: –––, 1965, “Finite-Quantifier Equivalence” in *The Theory of Models*, J. Addison, L. Henkin, and A. Tarski (eds.), Amsterdam: North-Holland, 407–412.

[^keisler-1974]: Keisler, H. J., 1974, *Model Theory for Infinitary Logic*, Amsterdam: North-Holland.

[^keisler-2004]: Keisler, H. J., and Julia F. Knight, 2004, “Barwise: Infinitary Logic And Admissible Sets”, *Journal of Symbolic Logic*, 10(1): 4–36

[^kolaitis-1992]: Kolaitis, P. and M. Vardi, 1992, “Fixpoint Logic vs. Infinitary Logic in Finite-Model Theory,” *Proceedings of the Seventh Annual IEEE Symposium on Logic in Computer Science* (LICS '92), IEEE, pp. 46-57; [available online](http://www.cs.rice.edu/~vardi/papers/lics92rj.pdf), doi:10.1109/LICS.1992.185518

[^kreisel-1965]: Kreisel, G., 1965, “Model-Theoretic Invariants, Applications to Recursive and Hyperarithmetic Operations”, in *The Theory of Models*, J. Addison, L. Henkin, and A. Tarski (eds.), Amsterdam: North-Holland, 190-205.

[^kueker-1975]: Kueker, D., 1975, “Back-and-forth arguments in infinitary languages”, in *Infinitary Logic: In Memoriam Carol Karp* (Lecture Notes in Mathematics: Volume 492), D. Kueker (ed.), Berlin: Springer-Verlag.

[^lopez-escobar-1965]: Lopez-Escobar, E. G. K., 1965, “An Interpolation Theorem for Infinitely Long Sentences”, *Fundamenta Mathematicae*, 57: 253–272.

[^lopez-escobar-1966]: –––, 1966, “On Defining Well-Orderings”, *Fundamenta Mathematicae*, 59: 13–21.

[^makkai-1977]: Makkai, M., 1977, “Admissible Sets and Infinitary Logic”, *Handbook of Mathematical Logic*, J. Barwise (ed.), Amsterdam: North-Holland, 233-282.

[^morley-1965]: Morley, M., 1965, “Omitting Classes of Elements”, *The Theory of Models*, J. Addison, L. Henkin, and A. Tarski (eds.), Amsterdam: North-Holland, 265-273.

[^nadel-1985]: Nadel, M., 1985, “L_{ω1},ω and Admissible Fragments”, in J. Barwise and S. Feferman (eds.) 1985, 271–287.

[^negri-2021]: Negri, Sara, 2021, “Geometric Rules in Infinitary Logic”, in O. Arieli and A. Zamansky (eds.), *Arnon Avron on Semantics and Proof Theory of Non-Classical Logics*, Cham: Springer, 265–293. doi:10.1007/978-3-030-71258-7_12

[^platek-1966]: Platek, R., 1966, *Foundations of Recursion Theory*, Ph.D. Thesis, Stanford University.

[^scott-1961]: Scott, D., 1961, “Measurable Cardinals and Constructible Sets”, *Bulletin of the Academy of Polish Sciences*, 9: 521–524.

[^scott-1965]: –––, 1965, “Logic with Denumerably Long Formulas and Finite Strings of Quantifiers”, *The Theory of Models*, J. Addison, L. Henkin, and A. Tarski (eds.), Amsterdam: North-Holland, 329-341.

[^scott-1958]: Scott, D., and A. Tarski, 1958, “The sentential calculus with infinitely long expressions”, *Colloquium Mathematicum*, 16: 166–170.

[^shelah-2012]: Shelah, Saharon, 2012, “Nice infinitary logics”, *Journal of the American Mathematical Society*, 25: 395-427, [available online](http://www.ams.org/journals/jams/2012-25-02/S0894-0347-2011-00712-1/), doi:10.1090/S0894-0347-2011-00712-1

[^tarski-1939]: Tarski, A., 1939, “Ideale in völlständingen Mengenkörpern I”, *Fundamenta Mathematicae*, 32: 140–150.

[^tarski-1958]: –––, 1958, “Remarks on predicate logic with infinitely long expressions”, *Colloquium Mathematicum*, 16: 171–176.

[^tarski-1962]: –––, 1962, “Some problems and results relevant to the foundations of set theory”, in E, Nagel, P. Suppes and A. Tarski (eds.), *Logic, Methodology and Philosophy of Science*, Stanford: Stanford University Press, 123-135.

[^ulam-1930]: Ulam, S., 1930, “Zur Masstheorie in der algemeinen Mengenlehre”, *Fundamenta Mathematicae*, 16: 140–150.
