# Independence and Large Cardinals
**First published Tue Apr 20, 2010**

*Koellner, Peter*

The independence results in arithmetic and set theory led to a proliferation of mathematical systems. One very general way to investigate the space of possible mathematical systems is under the relation of interpretability. Under this relation the space of possible mathematical systems forms an intricate hierarchy of increasingly strong systems. Large cardinal axioms provide a canonical means of climbing this hierarchy and they play a central role in comparing systems from conceptually distinct domains.

This article is an introduction to independence, interpretability, large cardinals and their interrelations. Section 1 surveys the classic independence results in arithmetic and set theory. Section 2 introduces the interpretability hierarchy and describes some of its basic features. Section 3 introduces the notion of a large cardinal axiom and discusses some of the central examples. Section 4 brings together the previous themes by discussing the manner in which large cardinal axioms provide a canonical means for climbing the hierarchy of interpretability and serve as an intermediary in the comparison of systems from conceptually distinct domains. Section 5 briefly touches on some philosophical considerations.

## 1. Independence

Let us begin with the notion of an *axiom system*. To motivate this notion consider the manner in which justification traditionally proceeds in mathematics. In reasoning about a given domain of mathematics (or, in fact, any domain) the question of justification is successively pushed back further and further until ultimately one reaches principles that do not admit more fundamental justification. The statements at this terminal stage are elected as *axioms* and the subject is then organized in terms of derivability from the base of axioms. In the case of arithmetic this led to the axiom system PA (Peano arithmetic) and in the case of set theory it led to the axiom system ZFC (Zermelo-Frankel set theory with the Axiom of Choice).

Two natural questions arise: (1) If the axioms do not admit of more fundamental justification then how does one justify them? (2) Is the base of axioms sufficiently rich that one can settle every sentence on this basis?

There are two traditional views concerning the epistemological status of axioms. On the first view the axioms do not admit further justification since they are *self-evident*. On the second view the axioms do not admit further justification since they are *definitive of the subject matter*. Each of these views concerning our first question leads to an associated optimistic view concerning our second question—according to the first optimistic view, all mathematical truths are derivable (in first-order logic) from self-evident truths, while according to the second optimistic view, all mathematical truths are derivable (in first-order logic) from statements that are definitive of the subject matter. Should either of these optimistic views turn out to be correct, then the question of justification in mathematics would take on a particularly simple form: Either a statement would be an axiom (in which case it would be self-evident or definitive of the subject matter (depending on the view under consideration)) or it would be derivable in first-order logic from some such statements.

Unfortunately, these optimistic views came to be challenged in 1931 by Gödel's incompleteness theorems. Here is one version of the second incompleteness theorem:

> **Theorem 1.1** (Gödel, 1931). *Assume that* PA *is consistent. Then* PA *does not prove* Con(PA).

Here Con(PA) is a statement of arithmetic that expresses the informal statement that PA is consistent.[^note-1] Under slightly stronger assumptions (for example, that PA is Σ01-sound[^note-2]) one can strengthen the conclusion by adding that PA does not prove ¬Con(PA); in other words, under this stronger assumption, Con(PA) is *independent* of PA. Thus, we have here a case of a statement of arithmetic (and, in fact, a very simple one) that cannot be settled on the basis of the standard axioms. Moreover, the theorem is completely general—it holds not just for PA but for any sufficiently strong formal system *T*.

This raises a challenge for the two aforementioned optimistic views concerning the nature of mathematical truth. To begin with it shows that we cannot work with a *fixed* axiom system *T*. We will always need to introduce new axioms. More importantly, it raises the question of how one is to justify these new axioms, for as one continues to add stronger and stronger axioms the claim that they are either self-evident or definitive of the subject matter will grow increasingly more difficult to defend.

Already in 1931 Gödel pointed out a natural way to justify new axioms. He pointed out that if one moves beyond the natural numbers and climbs the hierarchy of types (the sets of natural numbers, the sets of sets of natural numbers, etc.) one arrives at axioms (the axioms of second-order arithmetic PA₂, the axioms of third-order arithmetic PA₃, etc.) that settle the undecided statements that he discovered. The axiom system for the second level, PA₂, settles the statement left undecided at the first level, namely Con(PA); in fact, PA₂ proves Con(PA), which is the desired result. But now we have a problem at the second level. For the second incompleteness theorem shows that (under similar background assumptions to those above) PA₂ does not settle Con(PA₂). Fortunately, the axiom system for the third level, PA₃, settles the statement left undecided at the second level, namely Con(PA₂). This pattern continues. For every problem there is a solution and for every solution there is a new problem. In this way, by climbing the hierarchy of types one arrives at systems that successively settle the consistency statements that arise along the way.

The above hierarchy of types can be recast in the uniform setting of set theory. The set-theoretic hierarchy is defined inductively by starting with the emptyset, taking the powerset at successor stages α+1, and taking the union at limit levels λ:

> | *V*₀ | = ∅ |
> | --- | --- |
> | *V*_{α+1} | = *P*(*V*_{α}) |
> | *V*_{λ} | = ∪_{α < λ} *V*_{α} |

The *universe of sets* *V* is the union of all such stages: *V*=∪_{α∈On} *V*_{α}, where On is the class of ordinals. The first infinite level *V*_{ω} consists of all of the hereditarily finite sets[^note-3] and this level satisfies ZFC-Infinity. The sets at this level can be coded by natural numbers and in this way one can show that PA and ZFC-Infinity are mutually interpretable.[^note-4] The second infinite level *V*_{ω+1} is essentially *P*(ℕ) (or, equivalently, ℝ) and this level satisfies (a theory that is mutually interpretable with) PA₂. The third infinite level *V*_{ω+2} is essentially *P*(*P*(ℕ)) (or, equivalently, as the set of functions of real numbers) and this level satisfies (a theory that is mutually interpretable with) PA₃. The first three infinite levels thus encompass arithmetic, analysis and functional analysis and therewith most of standard mathematics. In this fashion, the hierarchy of sets and associated set-theoretic systems encompasses the objects and systems of standard mathematics.

Now, should it turn out to be the case that the consistency sentences (and the other, related sentences discovered by Gödel in 1931) were the *only* instances of undecidable statements, then the sequence of systems in the above hierarchy would catch every problem that arises. And although we would never have a *single* system that gave us a complete axiomatization of mathematical truth, we would have a *series* of systems that collectively covered the totality of mathematical truths.

Unfortunately, matters were not to be so simple. The trouble is that when one climbs the hierarchy of sets in this fashion the greater expressive resources that become available lead to more intractable instances of undecidable sentences and this is true already of the second and third infinite levels. For example, at the second infinite level one can formulate the statement PM (that all projective sets are Lebesgue measurable) and at the third infinite level one can formulate CH (Cantor's continuum hypothesis).[^note-5] These statements were intensively investigated during the early era of set theory but little progress was made. The explanation was ultimately provided by the subsequent independence techniques of Gödel and Cohen.

Gödel invented (in 1938) the method of *inner models* by defining the minimal inner model *L*. This model is defined just as *V* is defined except that at successor stages instead of taking the *full powerset* of the previous stage one takes the *definable powerset* of the previous stage, where for a given set *X* the definable powerset Def(*X*) of *X* is the set of all subsets of *X* that are definable over *X* with parameters from *X*:

> | *L*₀ | = ∅ |
> | --- | --- |
> | *L*_{α+1} | = Def(*L*_{α}) |
> | *L*_{λ} | = ∪_{α < λ} *L*_{α} |

The inner model *L* is the union of all such stages: *L* = ∪_{α∈On} *L*_{α}. Gödel showed that *L* satisfies (arbitrarily large fragments of) ZFC along with CH. It follows that ZFC cannot refute CH. Cohen complemented this result by inventing (in 1963) the method of *forcing* (or *outer models*). Given a complete Boolean algebra **B** he defined a model *V*^{**B**} and showed that ¬CH holds in *V*^{**B**}.[^note-6] This had the consequence that ZFC could not prove CH. Thus, these results together showed that CH is independent of ZFC. Similar results hold for PM and a host of other questions in set theory.

These instances of independence are more intractable in that no simple iteration of the hierarchy of types leads to their resolution. They led to a more profound search for new axioms.

Once again Gödel provided the first steps in the search for new axioms. In 1946 he proposed as new axioms *large cardinal axioms*—axioms of infinity that assert that there are very large levels of the hierarchy of types—and he went so far as to entertain a generalized completeness theorem for such axioms, according to which all statements of set theory could be settled by such axioms (Gödel 1946, 151)[^gödel-1946].

The purpose of the remainder of this entry is to describe the nature of independence (along with the hierarchy of interpretability) and the connection between independence and large cardinal axioms.

*Further Reading*: For more on the incompleteness theorems see Smoryński (1977)[^smoryński-1977], Buss (1998a)[^buss-1998a], and Lindström (2003)[^lindström-2003]. For more on the independence techniques in set theory see Jech (2003)[^jech-2003] and Kunen (1980)[^kunen-1980].

## 2. The Interpretability Hierarchy

Our aim is to investigate the space of mathematical theories (construed as recursively enumerable axiom systems). The ordering on the space of such theories that we will consider is that of *interpretability*. The informal notion of interpretability is ubiquitous in mathematics; for example, Poincaré provided an interpretation of two dimensional hyperbolic geometry in the Euclidean geometry of the unit circle; Dedekind provided an interpretation of analysis in set theory; and Gödel provided an interpretation of the theory of formal syntax in arithmetic.

We shall use a precise formal regimentation of this informal notion. Let *T*₁ and *T*₂ be recursively enumerable axiom systems. We say that *T*₁ is *interpretable* in *T*₂ (*T*₁ ≤ *T*₂) when, roughly speaking, there is a translation τ from the language of *T*₁ to the language of *T*₂ such that, for each sentence φ of the language of *T*₁, if *T*₁⊢φ then *T*₂⊢τ(φ).[^note-7] We shall write *T*₁ < *T*₂ when *T*₁≤ *T*₂ and *T*₂≰ *T*₁ and we shall write *T*₁≡ *T*₂ when both *T*₁≤ *T*₂ and *T*₂≤ *T*₁. In the latter case, *T*₁ and *T*₂ are said to be *mutually interpretable.* The equivalence class of all theories mutually interpretable with *T* is called the *interpretability degree of* *T*.

For ease of exposition we shall make three simplifying assumptions concerning the theories under consideration. First, we shall assume that all of our theories are couched in the language of set theory. There is no loss of generality in this assumption since every theory is mutually interpretable with a theory in this language. For example, as noted earlier, PA and ZFC-Infinity are mutually interpretable. Second, we shall assume that all of our theories contain ZFC-Infinity. Third, we shall assume that all of our theories are Σ01-sound.

The *interpretability hierarchy* is the collection of all theories (satisfying our three simplifying assumptions) ordered under the relation ≤. We now turn to a discussion of the structure of this hierarchy.

To begin with, there is a useful characterization of the relation ≤. Let us write *T*₁ ⊆ _{Π01} *T*₂ to indicate that every Π01-statement provable in *T*₁ is also provable in *T*₂. A central result in the theory of interpretability is that (granting our simplifying assumptions) *T*₁≤ *T*₂ iff *T*₁ ⊆ _{Π01} *T*₂. It follows from this characterization and the second incompleteness theorem that for any theory *T* the theory *T* + Con(T) is strictly stronger than *T*, that is, *T* < T + Con(T). Moreover, it follows from the arithmetized completeness theorem that the theory *T* + ¬Con(T) is interpretable in *T*, hence, *T* ≡ *T* + ¬Con(*T*).

In terms of interpretability there are three possible ways in which a statement φ can be independent of a theory *T*.

1. Single Jump. Only one of φ or ¬φ leads to a jump in strength, that is, *T* + φ > *T*    and    *T* + ¬φ ≡ *T* (or likewise with φ and ¬φ interchanged).
2. No Jump. Neither φ nor ¬φ lead to a jump in strength, that is, *T* + φ ≡ *T*    and    *T* + ¬φ ≡ *T*.
3. Double Jump. Both φ and ¬φ lead to a jump in strength, that is, *T* + φ > *T*    and    *T* + ¬φ > *T*.

It turns out that each of these possibilities is realized. For the first it suffices to take the Π01-sentence Con(T). For the second it is easy to see that there is no example that is Π01; the simplest possible complexity of such a sentence is Δ02 and it turns out that there are such examples; examples of this type of independence are called *Orey sentences*. For the third kind of independence there are Π01 instances. (This is a corollary of Lemma 14 on pages 128–129 of Lindström (2003)[^lindström-2003].)

These are all metamathematical examples, the kind of example that only a logician would construct. It is natural to ask whether there are “natural” examples, roughly the sort of example occurring in the normal course of mathematics. In the set theoretic case, such examples are abundant for the first two cases. For example, PM is an example of the first kind of independence and CH is an example of the second kind of independence. There are no known “natural” examples of the third kind of independence. In the arithmetical case, such examples are rare. There are examples of the first kind of independence (the most famous of which is a classic example due to Paris and Harrington) but none of the second or third kind of independence.

Notice that in the case of the third example the two theories above *T* are incomparable in the interpretability order. To construct a pair of such Π01-statements one uses a reciprocal form of the diagonal lemma to construct two Π01-statements that refer to one another. Using such techniques can show that the interpretability order is quite complex. For example, for any two theories *T*₁ and *T*₂ such that *T*₁ < *T*₂ there is a third theory *T* such that *T*₁ < *T* < *T*₂. Thus, the order on the degrees of interpretability is neither linearly ordered nor well-founded. (See Feferman (1960)[^feferman-1960].)

Remarkably, it turns out that when one restricts to those theories that “arise in nature” the interpretability ordering is quite simple: There are no descending chains and there are no incomparable elements—the interpretability ordering on theories that “arise in nature” is a wellordering. In particular, although there are natural examples of the first and second kind of independence (e.g. PM and CH, respectively, something to which we will return to below), there are no known natural examples of the third kind of independence.

So, for theories that “arise in nature”, we have a wellordered hierarchy under the interpretability ordering. At the base of the ordering one has the degree that is represented by our minimal theory ZFC-Infinity and there is only one way to proceed, namely, upward in terms of strength.

We have already seen one way of climbing the hierarchy of the degrees of interpretability, namely, by adding consistency statements. There are two drawbacks to this approach. First, if one starts with a theory that “arises in nature” and adds the consistency statement one lands in a degree that has no known representative that “arises in nature”. Second, the consistency statement does not take one very far up the hierarchy. Both of these drawbacks are remedied by a very natural class of axioms—the large cardinal axioms.

*Further Reading*: For more on the structure of the interpretability hierarchy see chapters 6–8 of Lindström (2003)[^lindström-2003].

## 3. Large Cardinal Axioms

Let Z₀ be the theory ZFC-Infinity-Replacement. (This theory is logically equivalent to our base theory ZFC-Infinity.) We shall successively strengthen Z₀ by reflectively adding axioms that assert certain levels of the universe of sets exist.

The standard model of Z₀ is *V*_{ω}. The Axiom of Infinity (in one formulation) simply asserts that this set exists. So, when we add the Axiom of Infinity, the resulting theory Z₁ (known as Zermelo set theory with Choice) not only proves the consistency of Z₀; it proves that there is a standard model of Z₀. Now the standard model of Z₁ is *V*_{ω+ω}. The Axiom of Replacement implies that this set exists. So, when we add the Axiom of Replacement, the resulting theory Z₂ (known as ZFC), not only proves the consistency of Z₁; it proves that there is a standard model of Z₁.

A standard model of Z₂ has the form *V*_{κ} where κ is a regular cardinal such that for all α < κ, 2^{α} < κ. Such a cardinal is called a (*strongly*) *inaccessible* cardinal. The next axiom in the hierarchy under consideration is the statement asserting that such a cardinal exists. The resulting theory ZFC + “There is a strongly inaccessible cardinal” proves that there is a level of the universe that satisfies ZFC. Continuing in this fashion one arrives at stronger and stronger axioms that assert the existence of larger and larger levels of the universe of sets. Before continuing with an outline of such axioms let us first draw the connection with the hierarchy of interpretability.

Recall our classification of the three types of independence. We noted that there are no known natural examples of the third kind of independence but that there are natural examples of the first and second kind of independence.

Natural examples of the second kind of independence are provided by the dual method of inner and outer models. For example, these methods show that the theories ZFC+CH and ZFC+ ¬CH are mutually interpretable with ZFC, that is, all three theories lie in the same degree. In other words, CH is an Orey sentence with respect to ZFC. What about that other sentence we introduced: PM?

Using the method of inner models Gödel showed that ¬PM holds in *L*. It follows that ZFC+ ¬PM is mutually interpretable with ZFC. But what about PM? To show that ZFC+PM is mutually interpretable with ZFC a natural approach would be to follow the approach used for CH and build an outer model of ZFC that satisfies PM. However, it is known that this cannot be done starting with ZFC alone. For it turns out (by a result of Shelah (1984)[^shelah-1984]) that ZFC+PM implies the consistency of ZFC and this implies, by the second incompleteness theorem, that ZFC+PM is not interpretable in ZFC. In a sense we have here a case of the independence of independence. More precisely, even if we assume that ZFC is consistent we cannot (in contrast to the case of CH) prove that PM is independent of ZFC. To establish the independence of PM from ZFC we need to assume the consistency of a *stronger* theory, namely, that of ZFC + “There is a strongly inaccessible cardinal”. For it turns out that ZFC+PM lies not in the interpretability degree of ZFC but rather in that of ZFC + “There is a strongly inaccessible cardinal”. To summarize: While CH is a case of the second type independence, PM is a case of the first type independence; it is similar to Con(ZFC) in that it is a sentence φ such that only one of φ or ¬φ leads to a jump in strength, only now there are two differences; the jump lands in a degree that is much stronger and it is represented by a natural theory.

In general, the (known) sentences of set theory are either like CH or PM. Some are like CH in that both ZFC+φ and ZFC+ ¬φ lie in the degree of ZFC. Others are like PM in that one of ZFC+φ and ZFC+ ¬φ lies in the degree of ZFC while the other lies in the degree of an extension of ZFC via a large cardinal axiom.

Let us now return to our overview of large cardinal axioms. After strongly inaccessible cardinals there are Mahlo cardinals, indescribable cardinals, and ineffable cardinals. All of these large cardinal axioms can be derived in a uniform way using the traditional variety of reflection principles (see Tait 2005) but there are limitations on how far this variety of reflection principles can take one. For under a very general characterization of such principles it is known that they cannot yield the Erdős cardinal κ(ω). See Koellner (2009)[^koellner-2009].

The large cardinals considered thus far (including κ(ω)) are known as *small* large cardinals. A large cardinal is *small* if the associated large cardinal axiom can hold in Gödel's constructible universe *L*, that is, if “*V* ⊨ κ is a φ-cardinal” is consistent, then “*L* ⊨ κ is a φ-cardinal” is consistent. Otherwise the large cardinal is *large*.

There is a simple template for formulating (large) large cardinal axioms is in terms of elementary embeddings. In general such an axiom asserts that there is a transitive class *M* and a non-trivial elementary embedding

> *j* : *V* → *M*.

To say that the embedding is non-trivial is just to say that it is not the identity, in which case there must be a least ordinal that is moved. This ordinal is called the *critical point of j* and denoted crit(*j*). The critical point is (typically) the large cardinal associated with the embedding. A cardinal κ is said to be *measurable* iff it is the critical point of some such embedding.[^note-8]

It is easy to see that for any such embedding *V*_{κ+1}⊆ *M* where κ = crit(*j*). This amount of agreement enables one to show that κ is strongly inaccessible, Mahlo, indescribable, ineffable, etc. To illustrate this let us assume that we have shown that κ is strongly inaccessible and let us show that κ has much stronger large cardinal properties. Since κ is strongly inaccessible in *V* and since (*V*_{κ+1})^{*M*} =*V*_{κ+1}, *M* also thinks that κ is strongly inaccessible. In particular, *M* thinks that there is a strongly inaccessible cardinal (namely, κ) below *j*(κ). But then by the elementarity of *j*, *V* must think the same thing of the preimage of *j*(κ), namely, κ, that is, *V* must think that there is a strongly inaccessible below κ. So κ cannot be the least strongly inaccessible cardinal. Continuing in this manner one can show that there are many strongly inaccessibles below κ and, in fact, that κ is Mahlo, indescribable, ineffable, etc. So measurable cardinals subsume the small large cardinals.

In fact, Scott showed that (in contrast to the small large cardinals) measurable cardinals cannot exist in Gödel's constructible universe. Let us be precise about this. Let *V*=*L* be the statement that asserts that all sets are constructible. Then for each small large cardinal axiom φ (to be precise, those listed above) if the theory ZFC+φ is consistent then so is the theory ZFC+φ+*V*=*L*. In contrast, the theory ZFC + “There is a measurable cardinal” proves ¬*V*=*L*. This may seem somewhat counterintuitive since *L* contains all of the ordinals and so if κ is a measurable cardinal then κ is an ordinal in *L*. The point is that *L* cannot “recognize” that κ is a measurable cardinal since it is too “thin” to contain the ultrafilter that witnesses the measurability of κ.

One way to strengthen a large cardinal axiom based on the above template is to demand greater agreement between *M* and *V*. For example, if one demands that *V*_{κ+2}⊆ *M* then the fact that κ is measurable (something witnessed by a subset of *P*(κ)) can be recognized by *M*. And so, by exactly the same argument that we used above, there must be a measurable cardinal below κ.

This leads to a progression of increasingly strong large cardinal axioms. It will be useful to discuss some of the major stepping stones in this hierarchy.

If κ is a cardinal and η>κ is an ordinal then κ is η-*strong* if there is a transitive class *M* and a non-trivial elementary embedding *j*: *V* → *M* such that crit(*j*)=κ, *j*(κ)>η and *V*_{η}⊆ *M*. A cardinal κ is *strong* iff it is η-strong for all η>κ. One can also demand that the embedding preserve certain classes: If *A* is a class, κ is a cardinal, and η>κ is an ordinal then κ is η-*A*-*strong* if there exists a *j*: *V* → *M* which witnesses that κ is η-strong and which has the additional feature that *j*(*A* ∩ *V*_{κ}) ∩ *V*_{η} = *A* ∩ *V*_{η}. The following large cardinal notion plays a central role in the search for new axioms.

> **Definition 3.1**. A cardinal κ is a *Woodin cardinal* if κ is strongly inaccessible and for all *A*⊆ *V*_{κ} there is a cardinal κ_{*A*} < κ such that
>
> > κ_{*A*} is η-*A*-strong,
>
> for each η such that κ_{*A*} < η < κ.[^note-9]

One can obtain stronger large cardinal axioms by forging a link between the embedding *j* and the amount of resemblance between *M* and *V*. For example, a cardinal κ is *superstrong* if there is a transitive class *M* and a non-trivial elementary embedding *j*: *V* → *M* such that crit(*j*)=κ and *V*_{j(κ)}⊆ *M*. If κ is superstrong then κ is a Woodin cardinal and there are arbitrarily large Woodin cardinals below κ.

One can also obtain strong large cardinal axioms by placing closure conditions on the target model *M*. For example, letting γ ≥ κ a cardinal κ is *γ-supercompact* if there is a transitive class *M* and a non-trivial elementary embedding *j*: *V* → *M* such that crit(*j*)=κ and ^{γ}*M*⊆ *M*, that is, *M* is closed under γ-sequences. (It is straightforward to see that if *M* is closed under γ-sequences then *H*(γ^{*+*})⊆ *M*; so this approach subsumes the previous approach.) A cardinal κ is *supercompact* if it is γ-supercompact for all γ ≥ κ. Now, just as in the previous approach, one can strengthen these axioms by forging a link between the embedding *j* and the closure conditions on the target model. A cardinal κ is *n-huge* if there is a transitive class *M* and a non-trivial elementary embedding *j*:*V* → *M* such that ^{*j* *n*}(κ)*M* ⊆ *M*, where κ=crit(*j*) and *j* ^{*i*+1}(κ) is defined to be *j*(*j* ^{*i*}(κ)).

One can continue in this vein, demanding greater agreement between *M* and *V*. The ultimate axiom in this direction would, of course, demand that *M* = *V*. This axiom was proposed by Reinhardt and shortly thereafter shown to be inconsistent (in ZFC) by Kunen. In fact, Kunen showed that, assuming ZFC, there can be a transitive class *M* and a non-trivial elementary embedding *j*: *V* → *M* such that *j* ‘‘ λ ∈ M, where λ=sup_{*n* < ω} *j* ^{*n*}(κ) and κ=crit(*j*). In particular, there cannot exists such an *M* and *j* such that *V*_{λ+1}⊆ *M*. This placed a limit on the amount of closure of the target model (in relation to the embedding).[^note-10]

Nevertheless, there is a lot of room below the above upper bound. For example, a very strong axiom is the statement that there is a non-trivial elementary embedding *j*:*V*_{λ+1}→ *V*_{λ+1}. The strongest large cardinal axiom in the current literature is the axiom asserting that there is a non-trivial elementary embedding *j*: *L*(*V*_{λ+1})→ *L*(*V*_{λ+1}) such that crit(*j*)<λ. In recent work, Woodin has discovered axioms much stronger than this.

*Further Reading*: For more on large cardinal axioms see Kanamori (2003)[^kanamori-2003].

## 4. Large Cardinal Axioms and the Interpretability Hierarchy

The large cardinal axioms discussed above are naturally well-ordered in terms of strength.[^note-11] This provides a natural way of climbing the hierarchy of interpretability. At the base we start with the theory ZFC-Infinity and then we climb to ZFC and up through ZFC+Φ for various large cardinal axioms Φ. Notice that for two large cardinal axioms Φ and Ψ, if Ψ is stronger than Φ then Ψ implies that there is a standard model of Φ and so we have a natural interpretation of ZFC+Φ in ZFC+Ψ.

We have already noted that ZFC+¬PM is mutually interpretable with ZFC+LC where LC is the large cardinal axiom “There is a strongly inaccessible cardinal” and that this is shown using the dual techniques of inner and outer model theory. It is a remarkable empirical fact that for *any* “natural” statement in the language of set theory φ one can generally find a large cardinal axiom Φ such that ZFC+φ and ZFC+Φ are mutually interpretable. Again, this is established using the dual techniques of inner and outer model theory only now large cardinals enter the mix. To establish that ZFC+Φ interprets ZFC+φ one generally starts with a model of ZFC+Φ and uses forcing to construct a model of ZFC+φ. In many cases the forcing construction involves “collapsing” the large cardinal associated with Φ and arranging the collapse in such a way that φ holds in the “rubble”. In the other direction, one generally starts with a model of ZFC+φ and then constructs an inner model (a model resembling *L* but able to accommodate large cardinal axioms) that contains the large cardinal asserted to exist by Φ. The branch of set theory known as *inner model theory* is devoted to the construction of such “*L*-like” models for stronger and stronger large cardinal axioms.

In this way the theories of the form ZFC+LC, where LC is a large cardinal axiom, provide a yardstick for measuring the strength of theories. They also act as intermediaries for comparing theories from conceptually distinct domains: Given ZFC+φ and ZFC+ψ one finds large cardinal axioms Φ and Ψ such that (using the methods of inner and outer models) ZFC+φ and ZFC+Φ are mutually interpretable and ZFC+ψ and ZFC+Ψ are mutually interpretable. One then compares ZFC+φ and ZFC+ψ (in terms of interpretability) by mediating through the natural interpretability relationship between ZFC+Φ and ZFC+Ψ. So large cardinal axioms (in conjunction with the dual method of inner and outer models) lie at the heart of the remarkable empirical fact that natural theories from completely distinct domains can be compared in terms of interpretability.

## 5. Some Philosophical Considerations

The main question that arises in light of the independence results is whether one can justify new axioms that settle the statements left undecided by the standard axioms. There are two views. On the first view, the answer is taken to be negative and one embraces a radical form of pluralism in which one has a plethora of equally legitimate extensions of the standard axioms. On the second view, the answer is taken (at least in part) to be affirmative, and the results simply indicate that ZFC is too weak to capture the mathematical truths. This topic is quite involved and lies outside the scope of the present article.

But there are other philosophical questions more directly related to the themes of this article. First, what is the significance of the empirical fact that the large cardinal axioms appear to be wellordered under interpretability? Second, what is the significance of the empirical fact that large cardinal axioms play a central role in comparing many theories from conceptually distinct domains? Let us consider these two questions in turn.

One might try to argue that the fact that the large cardinal axioms are wellordered under interpretability is a consideration in their favour. However, this would be a weak argument. For, as we have noted above, *all* “natural” theories appear to be wellordered under interpretability and this includes theories that are incompatible with one another. For example, it is straightforward to select “natural” theories from higher and higher degrees of theories in the wellordered sequence that are incompatible with one another. It follows that the feature of being wellordered under interpretability, while remarkable, can not be a point in favour of truth.

But large cardinal axioms have additional features that singles them out from the class of natural theories in the wellordered sequence of degrees. To begin with they provide the most natural way to climb the hierarchy of interpretability—they are the simplest and most natural manifestation of pure mathematical strength. But more important is the second component mentioned above, namely, the large cardinal axioms act as intermediaries in comparing theories from conceptually distinct domains. For recall how this works: Given ZFC+φ and ZFC+ψ one finds large cardinal axioms Φ and Ψ such that (using the methods of inner and outer models) ZFC+φ and ZFC+Φ are mutually interpretable and ZFC+ψ and ZFC+Ψ are mutually interpretable. One then compares ZFC+φ and ZFC+ψ (in terms of interpretability) by mediating through the natural interpretability relationship between ZFC+Φ and ZFC+Ψ.

It turns out that in many cases this is the *only known way* to compare ZFC+φ and ZFC+ψ, that is, in many cases there is no direct interpretation in either direction, instead one *must pass through the large cardinal axioms.* Can this additional feature be used to make a case for large cardinal axioms? The answer is unclear. However, what is clear is the absolute centrality of large cardinal axioms in set theory.

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=independence-large-cardinals). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/independence-large-cardinals/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=independence-large-cardinals&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](http://philpapers.org/sep/independence-large-cardinals/) at [PhilPapers](http://philpapers.org/), with links to its database. |

## Other Internet Resources

[Please contact the author with suggestions.]

## Related Entries

choice, axiom of | Gödel, Kurt | Gödel, Kurt: incompleteness theorems | set theory | set theory: alternative axiomatic theories | set theory: continuum hypothesis | set theory: large cardinals and determinacy

## Notes（原文脚注）

[^note-1]: It will be useful at this point to introduce some basic syntactic notions. The *language of first-order arithmetic* is the language consisting of the usual *logical symbols* (propositional connectives, quantifiers, and equality (=)) and the following *non-logical symbols*: The constant symbol 0, the unary successor function *S*, the binary operators + and ·, and the binary relation ≤. The *terms* are generated by starting with 0 and the variables and iteratively applying *S*, + and ·. A quantifier is *bounded* if it is of the form ∃*x* ≤ *t* or ∀*x*≤*t* where *t* is a term not involving *x*. A formula is a *bounded formula* (denoted Δ00) if all of its quantifiers are bounded. For *n* ≥ 0 the classes of formulas Σ0*n* and Π0*n* are defined as follows: Σ00 = Π00 = Δ00. Σ0*n*+1 is the set of formulas of the form ∃**x**φ where φ is Π0*n* and **x** is a (possibly empty) list of variables. Π0*n*+1 is the set of formulas of the form ∀**x**φ where φ is Σ0*n* and **x** is a (possibly empty) list of variables. The classes Σ0*n*, Π0*n* constitute the *arithmetical hierarchy of formulas*.

For a formal system *T* of arithmetic, a formula φ is (Π0*n*)^{*T*} if it is provably equivalent in *T* to a Π0*n* formula. Likewise, for (Σ0*n*)^{*T*}. A formula φ is (Δ0*n*)^{*T*} if it is provably equivalent in *T* to both a Σ0*n* formula and a Π0*n* formula. In many cases, when the context is clear, we shall drop reference to *T*.

A formal system *T* of arithmetic is Σ01-*complete* if it proves every true Σ01-statement. The system PA is Σ01-complete. The raises the question of whether PA can capture the truths at the next level of the arithmetical hierarchy, that is, the Π01 truths. The statement Con(PA) is a Π01-statement (informally it asserts “for all natural numbers *n*, *n* does not code a proof of a contradiction from the axioms of PA”). Thus, granting the consistency of PA, the incompleteness theorem shows that there is a Π01-truth that cannot be proved in PA.

[^note-2]: A system *T* is Σ01 *sound* iff for every Σ01-statement φ, if *T* proves φ then φ is true.

[^note-3]: In general, for a cardinal κ, a set *x* is of hereditarily cardinality of size less than κ, if *x* has size less than κ, all of the members of *x* have size less than κ, etc., in other words, the transitive closure of *x* has size less than κ. The set of all sets of hereditary cardinality less than κ is denoted *H*(κ). In particular, *H*(ω)=V_{ω}.

[^note-4]: For a more detailed treatment of this notion see the next section. The interpretation of PA in ZFC-Infinity was established during the early days of set theory. The interpretation of ZFC-Infinity in PA was established by Ackermann (1937)[^ackermann-1937].

[^note-5]: In descriptive set theory it is convenient to work with the “logician's reals”, that is, Baire space, ω^{ω}. This is the set of all infinite sequences of natural numbers (with the product topology (taking ω to be discrete)).

The *projective* sets of reals (or sets of *k*-tuples of reals) are obtained by starting with the closed subsets of (ω^{ω})^{*k*} and iterating the operations of complement and projection. For *A* ⊆ (ω^{ω})^{*k*}, the *complement* of *A* is simply (ω^{ω})^{*k*} − *A*. For *A* ⊆ (ω^{ω})^{*k*+1}, the *projection* of *A* is

> *p*[*A*] = {⟨ x₁, … ,x_{*k*} ⟩ ∈ (ω^{ω})^{*k*} | ∃ y, ⟨ x₁, … , *x*_{*k*}, *y* ⟩ ∈ *A*}.

(Think of the case where *k*+1=3. Here *A* is a subset of three-dimensional space and *p*[*A*] is the result of “projecting” *A* along the third axis onto the plane spanned by the first two axes.) We can now define the hierarchy of projective sets as follows: At the base level let Σ10 consist of the open subsets of (ω^{ω})^{*k*} and let Π10 consist of the closed subsets of (ω^{ω})^{*k*}. For each *n* such that 0 < *n* < ω, recursively define Π1*n* to consist of the complements of sets in Σ1*n* and Σ1*n*+1 to consist of the projections of sets in Π1*n*. The projective sets of (*k*-tuples of) reals are the sets appearing in this hierarchy. This hierarchy is also a proper hierarchy, as can be seen using universal sets and diagonalization.

It is a classical result of analysis (due to Luzin and Suslin in 1917) that the Σ11 sets are Lebesgue measurable.

[^note-6]: There are a number of different ways of formalizing forcing. One can forgo talk of models and treat the independence results proof-theoretically. One can also give a model-theoretic treatment and here there are two approaches. The first approach starts with a countable transitive model *M* of a sufficiently large fragment of ZFC and then (working in *V*) one actually builds an outer model *M*[*G*] that satisfies a large fragment of set theory and the statement one wishes to show is independent. The second approach involves working with class-size Boolean-valued models. Cohen took the first approach but we have found it simpler to take the second in our treatment. (We caution the reader that set theorists often speak of *V*[*G*] as if there were a model larger than the universe of sets. When they do so they are either thinking of *V* as a countable model (like *M* above) or thinking of *V*[*G*] as a Boolean valued model (like *V*^{**B**}). See Kunen (1980)[^kunen-1980], pp. 232–235 for further discussion.

[^note-7]: For a precise definition see chapter 6 of Lindström (2003)[^lindström-2003].

[^note-8]: The above formulation of large cardinal axioms invokes classes but there are equivalent formulations in terms of sets. For example, in the case of a measurable cardinal κ there is a subset of *P*(κ) (namely, a κ-complete ultrafilter over κ) witnessing that κ is measurable.

[^note-9]: It should be noted that in contrast to measurable and strong cardinals, Woodin cardinals are not characterized as the critical point of an embedding or collection of embeddings. In fact, a Woodin cardinal need not be measurable. However, if κ is a Woodin cardinal, then *V*_{κ} is a model of ZFC and *V*_{κ} satisfies that there is a proper class of strong cardinals.

[^note-10]: It is still open whether large cardinal axioms at the level of Reinhardt and beyond are inconsistent in ZF alone (that is, without invoking AC). Should they turn out to be consistent then one would have a hierarchy of “choiceless” large cardinal axioms that would climb the hierarchy of interpretability beyond the large cardinal axioms formulated in the context of ZFC.

[^note-11]: We should note that there are many large cardinal axioms that we have not discussed. The large cardinal axioms that have been investigated to date are *for the most part* known to be naturally well-ordered. However, there are some comparisons that remain open; for example, although it is known that a strongly compact cardinal is weaker than a supercompact cardinal it is not know how it compares with Woodin cardinals.

[^ackermann-1937]: Ackermann, Wilhelm, 1937, “Die Widerspruchsfreiheit der allgemeinen Mengenlehre,” *Mathematische Annalen*, 114: 305–315.

[^barwise-1977]: Barwise, Jon K., 1977, *Handbook of Mathematical Logic* (Studies in Logic and the Foundations of Mathematics: 90), Amsterdam: North-Holland.

[^buss-1998a]: Buss, Samuel R., 1998a, “First-Order Proof Theory of Arithmetic,” in Buss 1998b, 79–147.

[^buss-1998b]: –––, 1998b, *Handbook of Proof Theory* (Studies in Logic and the Foundations of Mathematics: 137), Amsterdam: North Holland.

[^feferman-1960]: Feferman, Solomon, 1960, “Arithmetization of metamathematics in a general setting,” *Fundamenta Mathematicae*, 49: 35–92.

[^foreman-2009]: Foreman, Matthew and Kanamori, Akihiro, 2009, *Handbook of Set Theory*, Berlin: Springer-Verlag.

[^gödel-1946]: Gödel, Kurt, 1946, “Remarks before the Princeton bicentennial conference on problems in mathematics,” in Gödel 1990, 150–153.

[^gödel-1986]: –––, 1986, *Collected Works I: Publications 1929–1936*, S. Feferman, J. Dawson, S. Kleene, G. Moore, R. Solovay, and J. van Heijenoort (eds.), Oxford: Oxford University Press.

[^gödel-1990]: –––, 1990, *Collected Works II: Publications 1938–1974*, S. Feferman, J. Dawson, S. Kleene, G. Moore, R. Solovay, and J. van Heijenoort (eds.), Oxford: Oxford University Press.

[^jech-2003]: Jech, Thomas J., 2003, *Set Theory* (Third Millennium Edition, Revised and Expanded), Berlin: Springer-Verlag.

[^kanamori-2003]: Kanamori, Akihiro, 2003, *The Higher Infinite: Large Cardinals in Set Theory from their Beginnings* (Springer Monographs in Mathematics), 2nd edition, Berlin: Springer.

[^koellner-2009]: Koellner, Peter, 2009, “On Reflection Principles,” *Annals of Pure and Applied Logic*, 157: 206–219.

[^kunen-1980]: Kunen, Kenneth, 1980, *Set theory: An Introduction to Independence Proofs* (Studies in Logic and the Foundations of Mathematics: 102), Amsterdam: North-Holland.

[^lindström-2003]: Lindström, Per, 2003, *Aspects of Incompleteness* (Lecture Notes in Logic: 10), 2nd edition, CITY: Association of Symbolic Logic.

[^shelah-1984]: Shelah, Saharon, 1984, “Can you take Solovay's inaccessible away?,” *Israel Journal of Mathematics*, 48(1): 1–47.

[^smoryński-1977]: Smoryński, Craig A., 1977, “The Incompleteness Theorems,” in Barwise 1977, 821–865.

[^tait-2005a]: Tait, William W., 2005a, “Constructing cardinals from below,” in Tait 2005b, 133-154.

[^tait-2005b]: –––, 2005b, *The Provenance of Pure Reason: Essays in the Philosophy of Mathematics and Its History*, Oxford: Oxford University Press.
