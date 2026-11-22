# Zermelo’s Axiomatization of Set Theory
**First published Tue Jul 2, 2013**

*Hallett, Michael*

The first axiomatisation of set theory was given by Zermelo in his 1908 paper “*Untersuchungen über die Grundlagen der Mengenlehre, I*” (Zermelo 1908b)[^zermelo-1908b], which became the basis for the modern theory of sets. This entry focuses on the 1908 axiomatisation; a further entry will consider later axiomatisations of set theory in the period 1920–1940, including Zermelo's second axiomatisation of 1930.

## 1. The Axioms

The introduction to Zermelo's paper makes it clear that set theory is regarded as a fundamental theory:

> Set theory is that branch of mathematics whose task is to investigate mathematically the fundamental notions “number”, “order”, and “function”, taking them in their pristine, simple form, and to develop thereby the logical foundations of all of arithmetic and analysis; thus it constitutes an indispensable component of the science of mathematics. (1908b: 261)[^note-1]

This is followed by an acknowledgment that it is necessary to replace the central assumption that we can ‘assign to an arbitrary logically definable notion a “set”, or “class”, as its “extension” ’ (1908b: 261). Zermelo goes on:

> In solving the problem [this presents] we must, on the one hand, restrict these principles [distilled from the actual operation with sets] sufficiently to exclude all contradictions and, on the other, take them sufficiently wide to retain all that is valuable in this theory. (1908b: 261)

The ‘central assumption’ which Zermelo describes (let us call it the Comprehension Principle, or CP) had come to be seen by many as the principle behind the derivation of the set-theoretic inconsistencies. Russell (1903: §104) says the following:

> Perhaps the best way to state the suggested solution [of the Russell-Zermelo contradiction] is to say that, if a collection of terms can only be defined by a variable propositional function, then, though a class as many may be admitted, a class as one must be denied. We took it as axiomatic that the class as one is to be found wherever there is a class as many; but this axiom need not be universally admitted, and appears to have been the source of the contradiction. By denying it, therefore, the whole difficulty will be overcome.

But it is by no means clear that ‘the whole difficulty’ is thereby ‘overcome’. Russell makes a clear identification of the principle he cites (a version of CP) as the source of error, but this does not in the least make it clear what is to take its place.[^note-2] In his *Grundgesetze* (see e.g., Frege 1903: §146–147)[^frege-1903] Frege recognises that his (in)famous Law V is based on a conversion principle which allows us to assume that for any concept (function), there is an object which contains precisely those things which fall under that concept (or for which the function returns the value ‘True’). Law V is then the principle which says that two such extension objects *a*, *b* stemming from two concepts *F*, *G* are the same if, and only if, *F* and *G* are extensionally equivalent. Frege clearly considers the ‘conversion’ of concepts to extensions as fundamental; he also regards it as widely used in mathematics (even if only implicitly), and thus that he is not ‘doing anything new’ by using such a principle of conversion and the attendant ‘basic law of logic’, Law V. (The CP follows immediately from Law V.) Frege was made aware by Russell (1902)[^russell-1902] that his Law V is contradictory, since Russell's paradox flows easily from it. In the Appendix to *Grundgesetze* (Frege 1903)[^frege-1903], Frege says this:

> Hardly anything more unwelcome can befall a scientific writer than to have one of the foundations of his edifice shaken after the work is finished. This is the position into which I was put by a letter from Mr Bertrand Russell as the printing of this volume was nearing completion. The matter concerns my Basic Law (V). I have never concealed from myself that it is not as obvious as the others nor as obvious as must properly be required of a logical law. Indeed, I pointed out this very weakness in the foreword to the first volume, p. VII. I would gladly have dispensed with this foundation if I had known of some substitute for it. Even now, I do not see how arithmetic can be founded scientifically, how the numbers can be apprehended as logical objects and brought under consideration, if it is not—at least conditionally—permissible to pass from a concept to its extension. May I always speak of the extension of a concept, of a class? And if not, how are the exceptions to be recognised? May one always infer from the extension of one concept's coinciding with that of a second that every object falling under the first concept also falls under the latter? These questions arise from Mr Russell's communication. …What is at stake here is not my approach to a foundation in particular, but rather the very possibility of any logical foundation of arithmetic. (p. 253)[^note-3]

The difficulty could hardly be summed up more succinctly. It was the replacement of assumptions involving the unfettered conversion of concepts to objects which was Zermelo's main task in his axiomatisation.

Zermelo's system was based on the presupposition that

> Set theory is concerned with a “domain” 𝔅 of individuals, which we shall call simply “objects” and among which are the “sets”. If two symbols, *a* and *b*, denote the same object, we write *a* = *b*, otherwise *a* ≠ *b*. We say of an object *a* that it “exists” if it belongs to the domain 𝔅; likewise we say of a class 𝔎 of objects that “there exist objects of the class 𝔎” if 𝔅 contains at least one individual of this class. (1908b: 262)

Given this, the one fundamental relation is that of set membership, ‘ε’ , which allows one to state that an object *a* belongs to, or is in, a set *b*, written ‘*a* ε *b*’.[^note-4] Zermelo then laid down seven axioms which give a partial description of what is to be found in *B*. These can be described as follows:

1. *Extensionality* This says roughly that sets are determined by the elements they contain.
2. *Axiom of Elementary Sets* This asserts (a) the existence of a set which contains no members (denoted ‘0’ by Zermelo, now commonly denoted by ‘∅’); (b) the existence, for any object *a*, of the singleton set {*a*} which has *a* as its sole member; and (c) the existence, for any two objects *a*, *b*, of the unordered pair {*a*, *b*}, which has just *a*, *b* as its members.
3. *Separation* (*Aussonderungsaxiom*) This asserts that, for any given set *a*, and any given ‘definite’ property of elements in 𝔅 (more on this below), one can ‘separate’ out from *a* as a set just those elements which satisfy the given property.
4. *Power Set* This says that for any set, the collection of all subsets of that set is also a set.
5. *Union* This says that for any set, the collection of the members of the members of that set also forms a set.
6. *Choice* This says that for any set of pairwise disjoint, non-empty sets, there exists a set (which is a subset of the union set to which the given set gives rise) which contains exactly one member from each member of the given set.
7. *Infinity* This final axiom asserts the existence of an infinitely large set which contains the empty set, and for each set *a* that it contains, also contains the set {*a*}. (Thus, this infinite set must contain ∅, {∅}, {{∅}}, ….)

With the inclusion of this last, Zermelo explicitly rejects any attempt to *prove* the existence of an infinite collection from other principles, as we find in Dedekind (1888: §66), or in Frege via the establishment of what is known as ‘Hume's Principle’.

The four central axioms of Zermelo's system are the Axioms of Infinity and Power Set, which together show the existence of uncountable sets, the Axiom of Choice, to which we will devote some space below, and the Axiom of Separation. This latter allows that any ‘definite’ property φ does in fact give rise to a set, namely the set of all those things which are already included in some set *a* and which have the property φ, in other words, gives rise to a certain subset of *a*, namely the subset of all the φ-things in *a*. Thus, it follows from this latter that there will generally be many sets giving partial extensions of φ, namely the φ-things in *a*, the φ-things in *b*, the φ-things in *c*, and so on. However, there will be no guarantee of the existence of a unique extension-set for φ, as, of course, there is under the CP, namely *a* = {*x* : φ(*x*)}.

Zermelo shows that, on the basis of his system, the two central paradoxes, that of the greatest set and that of Russell, cannot arise. In fact, Zermelo proves:

> Every set *M* possesses at least one subset *M*₀ that is not an element of *M*. (1908b: 265)

The proof is an easy modification of the argument for Russell's Paradox, using the contradiction this time as *a reductio*. By Separation, let *M*₀ be the subset of *M* consisting of those elements *x* of *M* such that *x* ∉ *x*. Now either *M*₀ ∈ *M*₀ or *M*₀ ∉ *M*₀. Assume that *M*₀ ∈ *M*₀. Since *M*₀ is a subset of *M*, this tells us that *M*₀ ∈ *M*. But *M*₀ is then a member of *M* which fails to satisfy the condition for belonging to *M*₀, showing that *M*₀ ∉ *M*₀, which is a contradiction. Hence, necessarily, *M*₀ ∉ *M*₀. But now if we suppose that *M*₀ were in *M*, then *M*₀ itself is bound to be in *M*₀ by the defining condition of this set. Hence, *M*₀ ∉ *M* on pain of contradiction. The argument for the Russell paradox is used here to constructive effect: one person's contradiction is another person's *reductio*. Zermelo comments:

> It follows from the theorem that not all objects *x* of the domain 𝔅 can be elements of one and the same set; that is, the domain 𝔅 is not itself a set, and this disposes of the “Russell antinomy” so far as we are concerned. (1908b: 265)

For, in the absence of something like the CP, there is no overriding reason to think that there must *be* a universal set.[^note-5]

But although this deals with the Russell paradox and the paradox of the universal set, it does not tackle the general consistency of the system. Zermelo was well aware of this, as is clear from the Introduction to his paper:

> I have not yet even been able to prove rigorously that my axioms are “consistent”, though this is certainly very essential; instead I have had to confine myself to pointing out now and then that the “antinomies” discovered so far vanish one and all if the principles here proposed are adopted as a basis. But I hope to have done at least some useful spadework hereby for subsequent investigations in such deeper problems. (1908b: 262)

It should be remarked in passing that Zermelo doesn't deal specifically with the Burali-Forti paradox either, for the simple reason that it cannot be properly formulated in his system, since it deals either with well-orderings generally or with the general concept of ordinal number. We will come back to this below. However, assuming that the known paradoxes *can* be avoided, another question comes to the fore: if the Separation Axiom is to be the basic principle for the workaday creation of sets, is it *adequate*? This question, too, will be taken up later.

There were attempts at the statement of axioms before Zermelo, both publicly and in private correspondence.[^note-6] In particular, Cantor, in correspondence with Hilbert and Dedekind in the late 1890s, had endeavoured to describe some principles of set existence[^note-7] which he thought were legitimate, and would not give rise to the construction of what he called ‘inconsistent totalities’, totalities which engender contradictions. (The best known of these totalities were the totality of all ordinals and the totality of all cardinals.) These principles included those of set union and a form of the replacement axiom, as well as principles which seem to guarantee that every cardinal number is an aleph, which we call for short the ‘Aleph Hypothesis (AH)’.

Despite this, there are reasons for calling Zermelo's system the first real axiomatisation of set theory. It is clear above all that Zermelo's intention was to reveal the fundamental nature of the theory of sets and to preserve its achievements, while at the same time providing a general replacement for the CP.

## 2. The Background to Zermelo's Axiomatisation

### 2.1 Hilbert's Axiomatic Method

Hilbert's early work on the axiomatic method is an important part of the context of Zermelo's axiomatisation. Hilbert developed a particular version of the axiomatic approach to fundamental mathematical theories in his work on geometry in the period 1894–1904 (see Hallett and Majer 2004)[^hallett-2004]. This was to be seen as a distinct alternative to what Hilbert called the ‘genetic approach’ to mathematics. (For a short, historically informed description, see Felgner 2010: 169–174.)[^felgner-2010] Ebbinghaus's book on Zermelo makes it very clear how embedded Zermelo was in the Hilbert foundational circle in the early years of the century.[^note-8] This is not meant to suggest that Zermelo adopted Hilbert's approach to the foundations of mathematics in all its aspects. Indeed, Zermelo developed his own, distinctive approach to foundational matters which was very different from Hilbert's, something which emerges quite clearly from his later work. Nevertheless, there are two elements of Zermelo's procedure which fit very well with Hilbert's foundational approach in the early part of the century. The first element concerns what might be called the programmatic element of Hilbert's treatment of the foundations of mathematics as it emerged in the later 1890s, and especially with regard to the notion of mathematical existence. And the second concerns proof analysis, a highly important part of Hilbert's work on Euclidean geometry and geometrical systems generally. These matters are intricate, and cannot be discussed adequately here (for fuller discussion, see both Hallett 2008 and 2010a)[^hallett-2008][^hallett-2010a]. But it is important for understanding Zermelo's work fully that a rough account be given.

#### 2.1.1 Programmatic elements

First, Hilbert adopted the view that a mature presentation of a mathematical theory must be given axiomatically. This, he claims, requires several things:

1. The postulation of the existence of a domain, of a ‘system (or systems) of things’.
2. The insistence, however, that nothing is known about those things except what is expressed in, or can be derived from, a finite list of axioms.
3. The requirement, along with this, of finite proofs, which begin with axioms and proceed from these to a conclusion by a ‘finite number of inferences’ (i.e., acceptable inferential steps).
4. The rather imprecise notion of the ‘completeness’ of the axiomatisation, which involves, loosely, showing that the axioms can prove all that they ‘ought’ to prove.
5. The provision of a consistency proof for these axioms, showing that no contradiction is derivable by a proof constructed in the system given.

For one thing, Hilbert was very clear (especially in his unpublished lectures on geometry: see Hallett and Majer 2004)[^hallett-2004] that, although a domain is asserted to ‘exist’, all that is known about the objects in the domain is what is given to us by the axioms and what can be derived from these through ‘finite proof’. In other words, while a domain is postulated, nothing is taken to be known about the things in it independently of the axioms laid down and what they entail. The basic example was given by geometrical systems of points, lines and planes; although the geometrical domain is made up of these things, nothing can be assumed known about them (in particular no ‘intuitive’ geometrical knowledge from whatever source) other than what is given in the axioms or which can be derived from them by legitimate inference. (The axioms themselves might sum up, or be derived from, ‘intuitive’ knowledge, but that is a different matter. And even here it is important that we can detach the axioms from their intuitive meanings.)

Secondly, while ‘existence’ of the objects is just a matter (as Zermelo says) of belonging to the domain (a fact which is established by the axioms or by proofs from those axioms), the mathematical existence of the domain itself, and (correspondingly) of the system set out by the axioms, is established only by a consistency proof for the axioms. Thus, to take the prime example, the ‘existence’ of Euclidean geometry (or more accurately Euclidean geometries) is shown by the consistency proofs given by means of analytic geometry.[^note-9] Thus, the unit of consistency is not the concept nor the individual propositions, but rather the system of axioms as a whole, and different systems necessarily give accounts of different primitives. The expectation is that when a domain is axiomatised, attention will turn (at some point) to a consistency proof, and this will deal finally with the question of mathematical existence. In any case, the task of showing existence is a mathematical one and there is no further ontological or metaphysical mystery to be solved once the axioms are laid down.

Many aspects of Hilbert's position are summed up in this passage from his 1902 lectures on the foundations of geometry: the axioms ‘create’ the domains, and the consistency proofs justify their existence. As he puts it:

> The things with which mathematics is concerned are defined through axioms, *brought into life*.
>
> The axioms can be taken quite arbitrarily. However, if these axioms contradict each other, then no logical consequences can be drawn from them; the system defined then does not exist for the mathematician. (Hilbert 1902: 47 or Hallett and Majer 2004: 563)[^hallett-2004][^hilbert-1902]

This notion of ‘definition through axioms’, what came to be known as the method of ‘implicit definition’, can be seen in various writings of Hilbert's from around 1900. His attitude to existence is illustrated in the following passage from his famous paper on the axiomatisation of the reals:

> The objections which have been raised against the existence of the totality of all real numbers and infinite sets generally lose all their justification once one has adopted the view stated above [the axiomatic method]. By the set of the real numbers we do not have to imagine something like the totality of all possible laws governing the development of a fundamental series, but rather, as has been set out, a system of things whose mutual relations are given by the *finite and closed* systems of axioms I–IV [for complete ordered fields] given above, and about which statements only have validity in the case where one can derive them via a finite number of inferences from those axioms. (Hilbert 1900b: 184)[^hilbert-1900b][^note-10]

The parallels between this ‘axiomatic method’ of Hilbert's and Zermelo's axiomatisation of set theory are reasonably clear, if not exact.[^note-11] Particularly clear are the assumption of the existence of a ‘domain’ 𝔅, the statement of a finite list of axioms governing its contents, and the recognition of the requirement of a general consistency proof. There's also implicit recognition of the requirements of ‘finite proof’; this leads us to the second important aspect of the Hilbertian background, namely proof analysis and the use of the Axiom of Choice.

#### 2.1.2 Proof analysis and Zermelo's Well-Ordering Theorem [WOT]

A great deal of Hilbert's work on geometry concerned the analysis of proofs, of what can, or cannot, be derived from what. Much of Hilbert's novel work on geometry involved the clever use of (arithmetical) models for geometrical systems to demonstrate a succession of independence results, which, among other things, often show how finely balanced various central assumptions are.[^note-12] Moreover, a close reading of Hilbert's work makes it clear that the development of an appropriate axiom system itself goes hand-in-hand with the reconstruction and analysis of proofs.

One straightforward kind of proof analysis was designed to reveal what assumptions there are behind accepted ‘theorems’, and this is clearly pertinent in the case of Zermelo's Axiom of Choice (his sixth axiom) and the WOT. What Zermelo's work showed, in effect, is that the ‘choice’ principle behind the Axiom is a necessary and sufficient condition for WOT; and he shows this by furnishing a Hilbertian style proof for the theorem, i.e., a conclusion which follows from (fairly) clear assumptions by means of a finite number of inferential steps. Indeed, the Axiom is chosen so as to make the WOT provable, and it transpired subsequently that it also made provable a vast array of results, mainly (but not solely) in set theory and in set-theoretic algebra. To understand the importance of Zermelo's work, it's necessary to appreciate the centrality of the WOT.

### 2.2 The Well-Ordering Problem and the Well-Ordering Theorem

#### 2.2.1 The importance of the problem before Zermelo

In one of the fundamental papers in the genesis of set theory, Cantor (1883a)[^cantor-1883a] isolated the notion of a well-ordering on a collection as one of the central conceptual pillars on which number is built. Cantor took the view that the notion of a counting number must be based on an underlying ordering of the set of things being counted, an ordering in which there is a first element counted, and, following any collection of elements counted, there must be a next element counted, assuming that there are elements still uncounted. This kind of ordering he called a ‘well-ordering’, which we now define as a total-ordering with an extra condition, namely that any subset has a least element in the ordering. Cantor recognised that each distinct well-ordering of the elements gives rise to a distinct counting number, what he originally called an ‘*Anzahl* [enumeral]’, later an ‘*Ordnungszahl* [ordinal number]’, numbers which are conceptually quite different from *cardinal numbers* or *powers*, meant to express just the size of collections.[^note-13] This distinction is hard to perceive at first sight. Before Cantor and the rise of the modern theory of transfinite numbers, the standard counting numbers were the ordinary finite numbers.[^note-14] And, crucially, for finite collections, it turns out that any two orderings of the same underlying elements, which are certainly well-orderings in Cantor's sense, are order-isomorphic, i.e., not essentially distinct.[^note-15] This means that one can in effect identify a number arrived at by counting (an ordinal number) with the cardinal number of the collection counted. Thus, the ordinary natural numbers appear in two guises, and it is possible to determine the size of a finite collection directly by counting it. Cantor observed that this ceases to be the case in rather dramatic fashion once one considers infinite collections; here, the same elements can give rise to a large variety of distinct well-orderings.

Nevertheless, Cantor noticed that if one collects together all the countable ordinal numbers, i.e., the numbers representing well-orderings of the set of natural numbers, this collection, which Cantor called the *second number-class* (the first being the set of natural numbers), must be of greater cardinality than that of the collection of natural numbers itself. Moreover, this size is the cardinal *successor* to the size of the natural numbers in the very clear sense that any infinite subset of the second number-class is either of the power of the natural numbers or of the power of the whole class; thus, there can be no size which is strictly intermediate. The process generalises: collect together all the ordinal numbers representing well-orderings of the second number-class to form the third number-class, and this must be the immediate successor in size to that of the second number-class, and so on. In this way, Cantor could use the ordinal numbers to generate an infinite sequence of cardinalities or powers. This sequence was later (Cantor 1895)[^cantor-1895] called the aleph-sequence, ℵ₀ (the size of the natural numbers), ℵ₁ (expressing the size of the second number-class), ℵ₂ (expressing the size of the third number-class), and so on. Since the intention was that ordinal numbers could be generated arbitrarily far, then so too, it seems, could the alephs.

This raises the possibility of reinstating the centrality of the ordinal numbers as the fundamental numbers even in the case of infinite sets, thus making ordinality the foundation of cardinality for all sets. In work after 1883, Cantor attempted to show that the alephs actually represent a scale of infinite cardinal number. For instance, it is shown that the ordinal numbers are comparable, i.e., for any two ordinal numbers α, β, either α < β, α = β or α > β, a desirable, perhaps essential, property of counting numbers. Through this, comparability therefore transfers to the alephs, and Cantor was able to give clear and appropriate arithmetical operations of addition, multiplication and exponentiation, generalising the corresponding notions for finite collections, and the statement and proof of general laws concerning these.

In 1878, Cantor had put forward the hypothesis that there is no infinite power between that of the natural numbers and the continuum. This became known as Cantor's Continuum Hypothesis (CH). With the adumbration of the number classes, CH takes on the form that the continuum has the power of the second number-class, and with the development of the aleph-scale, it assumes the form of a conjecture about the exponentiation operation in the generalised cardinal arithmetic, for it can be expressed in the form 2^{ℵ₀} = ℵ₁. The *continuum problem* more generally construed is really the problem of where the power of the continuum is in the scale of aleph numbers, and the generalised continuum hypothesis is the conjecture that taking the power set of an infinite set corresponds to moving up just one level in the aleph scale. For example, in 1883, Cantor had assumed (without remark) that the set of all real functions has the size of the third number-class. Given the CH, this then becomes the conjecture that 2^{ℵ₁} = ℵ₂.

But adopting the aleph scale as a framework for infinite cardinality depends on significant assumptions. It is clear that any collection in well-ordered form (given that it is represented by an ordinal) must have an aleph-number representing its size, so clearly the aleph-sequence represents the sizes (or *powers* as Cantor called them) of all the well-ordered sets. However, can *any* set be put into well-ordered form? A particular question of this form concerns the continuum itself: if the continuum is equivalent to the second number-class, then clearly it can be well-ordered, and indeed this is a necessary condition for showing that the continuum is represented at all in the scale. But *can* it be well-ordered? More generally, to assume that *any* cardinality is represented in the scale of aleph numbers is to assume in particular that *any* set can be well-ordered. And to assume that the aleph-sequence is *the* scale of infinite cardinal number is to assume at the very least that sets generally can be compared cardinally; i.e., that for any *M*, *N*, either *M* ≼ *N* or *N* ≼ *M*, COMP for short. But is this correct?

When introducing the notion of well-ordering in 1883, Cantor expressed his belief that the fact that any set (‘manifold’) can be well-ordered is ‘a law of thought [Denkgesetz]’, thus putting forward what for convenience we can call the well-ordering hypothesis (WOH):

> The concept of *well-ordered set* reveals itself as fundamental for the theory of manifolds. That it is always possible to arrange any *well-defined* set in the form of a *well-ordered* set is, it seems to me, a very basic law of thought, rich in consequences, and particularly remarkable in virtue of its general validity. I will return to this in a later memoir. (Cantor 1883a or 1932: 169)[^cantor-1883a][^cantor-1932]

Cantor says nothing about what it might mean to call the well-ordering hypothesis a ‘law of thought’, and he never did return to this question directly; however, in one form or another, this claim is key. It could be that Cantor at this time considered the WOH as something like a logical principle.[^note-16] This, however, is not particularly clear, especially since the study of formal logic adequate for mathematical reasoning was only in its infancy, and the set concept itself was new and rather unclearly delimited. Another suggestion is that well-orderability is intrinsic to the way that ‘well-defined’ sets are either presented or conceived, e.g., that it is impossible to think of a collection's being a set without at the same time allowing that its elements can be arranged ‘discretely’ in some way, or even that such arrangement can be automatically deduced from the ‘definition’. Thus, if one views sets as necessary for mathematics, and one holds that the concept of set itself necessarily involves the discrete arrangement of the elements of the set, then WOH might appear necessary, too. But all of this is imprecise, not least because the notion of set itself was imprecise and imprecisely formulated. One clear implication of Cantor's remark is that he regards the WOH as something which does not require proof. Nonetheless, not long after he had stated this, Cantor clearly had doubts both about the well-orderability of the continuum and about cardinal comparability (see Moore 1982: 44)[^moore-1982]. All of this suggested that the WOH, and the associated hypothesis that the alephs represent the scale of infinite cardinality, do require proof, and cannot just be taken as ‘definitional’. Thus, it seemed clear that the whole Cantorian project of erecting a scale of infinite size depends at root on the correctness of the WOH.

Work subsequent to 1884 suggests that Cantor felt the need to supply arguments for well-ordering. For instance (Cantor 1895: 493)[^cantor-1895] to show that every infinite set *T* has a countable subset (and thus that ℵ₀ is the smallest cardinality), Cantor set out to *prove the existence* of a subset of *T* which is well-ordered like the natural numbers. The key point to observe here is that Cantor felt it necessary to *exhibit* a well-ordered subset of *T*, and did not simply proceed by first assuming (by appeal to his ‘*Denkgesetz*’) that *M* can be arranged in well-ordered form. He exhibits such a subset in the following way:

> *Proof.* If one has removed from *T* a finite number of elements *t*₁, *t*₂, …, *t*_{ν−1} according to some rule, then the possibility always remains of extracting a further element *t*_{ν}. The set {*t*_{ν}}, in which ν denotes an arbitrary finite, cardinal number, is a subset of *T* with the cardinal number ℵ₀, because {*t*_{ν}} ∼ {ν}. (Cantor 1895: 493)[^cantor-1895]

In 1932, Zermelo edited Cantor's collected papers (Cantor 1932)[^cantor-1932], and commented on this particular proof as follows:

> The “proof” of Theorem A, which is purely intuitive and logically unsatisfactory, recalls the well-known primitive attempt to arrive at a *well-ordering* of a given set by successive removal of arbitrary elements. We arrive at a correct proof only when we *start from* an already *well-ordered* set, whose smallest transfinite initial segment in fact has the cardinal number ℵ₀ sought. (Zermelo in Cantor 1932: 352)[^cantor-1932]

The second context in which an argument was given was an attempt by Cantor (in correspondence first with Hilbert and then Dedekind) to show that every set must have an aleph-number as a cardinal.[^note-17] What Cantor attempts to show, in effect, is the following. Assume that Ω represents the sequence of all ordinal numbers, and assume (for a *reductio* argument) that *V* is a ‘multiplicity’ which is not equivalent to any aleph. Then Cantor argues that Ω can be ‘projected’ into *V*, in turn showing that *V* must be what he calls an ‘inconsistent multiplicity’, i.e., not a legitimate set. It will follow that all sets have alephs as cardinals, since they will always be ‘exhausted’ by such a projection by some ordinal or other, in which case they will be cardinally equivalent to some ordinal number-class.[^note-18] Zermelo's dismissal of this attempted proof is no surprise, given the comments just quoted. But he also comments further here exactly on this ‘projection’:

> The weakness of the proof outlined lies precisely here. It is *not* proved that the whole series of numbers Ω can be “projected into” any multiplicity *V* which does not have an aleph as a cardinal number, but this is rather taken from a somewhat vague “intuition”. Apparently *Cantor* imagines the numbers of Ω successively and arbitrarily assigned to elements of *V* in such a way that every element of *V* is only used once. *Either* this process must then come to an end, in that all elements of *V* are used up, in which case *V* would be then be coordinated with an *initial* segment of the number series, and its power consequently an aleph, contrary to assumption; *or* *V* would remain inexhaustible and would then contain a component equivalent to the whole of Ω, thus an inconsistent component. Here, the intuition of time [*Zeitanschauung*] is being applied to a process which goes beyond all intuition, and a being [*Wesen*] supposed which can make *successive* arbitrary choices and thereby define a subset *V*′ of *V* which is not definable by the conditions given. (Zermelo in Cantor 1932: 451)[^cantor-1932][^note-19]

If it really is ‘successive’ selection which is relied on, then it seems that one must be assuming a subset of instants of time which is well-ordered and which forms a base ordering from which the ‘successive’ selections are made. In short, what is really presupposed is a well-ordered subset of temporal instants which acts as the basis for a recursive definition. Even in the case of countable subsets, if the ‘process’ is actually to come to a conclusion, the ‘being’ presupposed would presumably have to be able to distinguish a (countably) infinite, discrete sequence of instants within a finite time, and this assumption is, as is well-known, a notoriously controversial one. In the general case, the position is actually worse, for here the question of the well-orderability of the given set depends at the very least on the existence of a well-ordered subset of temporal instants of arbitrarily high infinite cardinality. This appears to go against the assumption that time is an ordinary continuum, i.e., of cardinality 2^{ℵ₀}, unless of course the power set of the natural numbers itself is too ‘big’ to be counted by any ordinal, in which case much of the point of the argument would be lost, for one of its aims is presumably to show that the power of the continuum is somewhere in the aleph-sequence.[^note-20]

Part of what is at issue here, at least implicitly, is what constitutes a proof. It seems obvious that if a set is non-empty, then it must be possible to ‘choose’ an element from it (i.e., there must exist an element in it). Indeed, the obviousness of this is enshrined in the modern logical calculus by the way the inference principle of Existential Instantiation (EI) usually works: from ∃*xPx* one assumes *Pc*, where ‘*c*’ is a new constant, and reasons on that basis; whatever can be inferred from *P*(*c*) (as long as it does not itself contain the new constant ‘*c*’) is then taken to be inferable from ∃*xPx* alone. Furthermore, it is clear how this extends to finite sets (or finite extensions) by stringing together successive inferential steps. But how can such an inferential procedure be extended to infinite sets, if at all?

Some evidence of the centrality of WOH is provided by Problem 1 on Hilbert's list of mathematical problems in his famous lecture to the International Congress of Mathematicians in Paris in 1900. He notes Cantor's conviction of the correctness of CH, and its ‘great probability’, then goes on to mention another ‘remarkable assertion’ of Cantor's, namely his belief that the continuum, although not (in its natural order) in well-ordered form, can be rearranged as a well-ordered set. However, Russell, writing at roughly the same time, expressed doubts about precisely this:

> Cantor assumes as an axiom that every class is the field of some well-ordered series, and deduces that all cardinals can be correlated with ordinals …. This assumption seems to me unwarranted, especially in view of the fact that no one has yet succeeded in arranging a class of 2^{α₀} terms in a well-ordered series. (Russell 1903: 322–323)[^russell-1903]

He goes on:

> We do not know that of any two different cardinal numbers one must be the greater, and it may be that 2^{α₀} is neither greater nor less that α₁ and α₂ and their successors, which may be called well-ordered cardinals because they apply to well-ordered series. (Russell 1903: 323)[^russell-1903][^note-21]

And recall that, at the International Congress of Mathematicians in Heidelberg in 1904, König had given an apparently convincing proof that the continuum *cannot* be an aleph. König's argument, as we know, turned out to contain fatal flaws, but in any case, the confusion it exhibits is instructive.[^note-22]

In short, the clear impression in the immediate period leading up to Zermelo's work was *both* that only the WOH would provide a solid foundation on which to build a reasonable notion of infinite cardinal number as a proper framework for tackling CH, *and* that WOH requires justification, that it must become, in effect, the WOT, the WO-Theorem. In short, establishing the WOT was closely bound up with the clarification of what it is to count as a set.

#### 2.2.2 Zermelo's 1904 Proof of the Well-Ordering Theorem

Zermelo's approach to the well-ordering problem took place in three stages. He published a proof of WOT in 1904 (Zermelo 1904, an extract from a letter to Hilbert)[^zermelo-1904], where he first introduced the ‘choice’ principle, a principle designed (despite the name it has come to bear) to move away from the Cantorian ‘choosing’ arguments which almost universally preceded Zermelo's work, and which postulates that arbitrary ‘choices’ have already been made. This paper produced an outcry, to which Zermelo responded by producing a new proof (1908a), which again uses the choice principle, but this time in a somewhat different form and expressed now explicitly as an axiom. The first three pages of this paper give the new proof; this was then followed by seventeen pages which reply in great detail to many of the objections raised against the first proof. These consisted in objections to the choice principle itself, and also objections to the unclarity of the underlying assumptions about, and operation with, sets used in the proof. This paper was followed just two months later by Zermelo's official axiomatisation (1908b), an axiomatisation which to a large degree was prefigured in the paper (1908a).

Zermelo's 1904 proof can be briefly described.

**(1)**

Let *M* be an arbitrarily given set, and let **M** be its power set. Assume given what Zermelo calls a ‘covering’ of **M**, i.e., a function γ from non-empty elements of **M** to *M* such that γ(*X*) ∈ *X*, in other words, what would now be called a choice function. The argument then shows that such a γ determines a unique well-ordering of *M*.[^note-23]

**(2)**

Using a fixed such γ, Zermelo then defines the so-called γ-sets *M*_{γ}. These satisfy the following conditions: *M*_{γ} ⊆ *M*; *M*_{γ} is well-ordered by some ordering ≺ specific to *M*_{γ}; If a ∈ *M*_{γ}, then *a* must determine an initial segment *A* of *M*_{γ} under ≺; but now γ and ≺ must be related in such a way that *a* = γ(*M* − *A*), i.e., *a* is the ‘distinguished element’ (as Zermelo calls it) of the complement of *A* in *M*.

**(3)**

There clearly are γ sets: {*m*₁} is one such, where *m*₁ = γ(*M*) and where we take the trivial well-ordering. The set {*m*₁, *m*₂} is also a γ-set, where again *m*₁ = γ(*M*), *m*₂ = γ(*M* − {*m*₁}), and {*m*₁, *m*₂} is given the ordering which places *m*₂ after *m*₁. (Note that {*m*₁, *m*₂} with the other ordering would not be a γ-set.) In fact, it is easy to see that if *M*′ ⊆ *M* is to be a γ-set, then condition (2)(c) means that ≺ is uniquely (one is tempted to say, recursively) determined.

**(4)**

Indeed, following this, Zermelo shows that of any two distinct γ-sets, one is identical to an initial segment of the other, and the well-ordering of the latter extends the well-ordering of the former.

**(5)**

Zermelo now considers the set *L*_{γ}, which is the union taken over all the γ-sets. It is not difficult to see that *L*_{γ} itself must be a γ-set, indeed, the largest such. By definition, *L*_{γ} ⊆ *M*; but Zermelo shows that equality must hold. If not, then *M* − *L*_{γ} would be a non-empty subset of *M*, in which case we can consider γ(*M* − *L*_{γ}) = *m*₁′. Now form *L*_{γ}′ *L*_{γ} ∪ {*m*₁′}, and supply it with the well-ordering which is the same as that in *L*_{γ}, except that we extend it by fixing that *x* ≺ *m*₁′ for any *x* ∈ *L*_{γ}. Clearly now *L*_{γ}′ is a γ-set, but one which properly extends *L*_{γ}, which is a contradiction. Thus *L*_{γ}′ = *M*, and so *M* can be well-ordered by the ordering of *L*_{γ}′.[^note-24]

As Zermelo points out (p. 516 of his paper), the WOT establishes a firm foundation for the theory of infinite cardinality; in particular, it shows, he says, that every set (‘for which the totality of its subsets etc. has a sense’) can be considered as a well-ordered set ‘and its power considered as an aleph’. Later work of Hartogs (see Hartogs 1915)[^hartogs-1915] showed that, not only does WOT imply COMP as Zermelo shows, but that COMP itself implies WOT, and thus in turn Zermelo's choice principle. Thus, it is not just COMP which is necessary for a reasonable theory of infinite cardinality, but WOT itself. Despite Zermelo's endorsement here, the correctness of the hypothesis that the scale of aleph numbers represents *all* cardinals (AH, for short) is a more complicated matter, for it involves the claim that every set is actually equivalent to an initial segment of the ordinals, and not just well-orderable. In axiomatic frameworks for sets, therefore, the truth of AH depends very much on which ordinals are present as sets in the system.

The subsequent work showing the independence of AC from the other axioms of set theory vindicates Zermelo's pioneering work; in this respect, it puts Zermelo's revelation of the choice principle in a similar position as that which Hilbert ascribes to the Parallel Postulate in Euclid's work. Hilbert claims that Euclid must have realised that to establish certain ‘obvious’ facts about triangles, rectangles etc., an entirely *new* axiom (Euclid's Parallel Postulate) was necessary, and moreover that Gauß was the first mathematician ‘for 2100 years’ to see that Euclid had been right (see Hallett and Majer 2004:261–263 and 343–345)[^hallett-2004]. This ‘pragmatic attitude’, which is on display in Zermelo's second paper on well-ordering from 1908, became, in effect, the reigning attitude towards the choice principle: If certain problems are to be solved, then the choice principle must be adopted. In 1908, Zermelo brings out this parallel explicitly:

> Banishing fundamental facts or problems from science merely because they cannot be dealt with by means of certain prescribed principles would be like forbidding the further extension of the theory of parallels in geometry because the axiom upon which this theory rests has been shown to be unprovable. (Zermelo 1908a: 115)[^zermelo-1908a]

Zermelo does not in 1904 call the choice principle an axiom; it is, rather, designated a ‘logical principle’. What Zermelo has to say by way of an explanation is very short:

> This logical principle cannot, to be sure, be reduced to a still simpler one, but it is applied without hesitation everywhere in mathematical deduction. (Zermelo 1904: 516)[^zermelo-1904]

It is not clear from this whether he thinks of the choice principle as a ‘law of thought’, as the term ‘logical principle’ might suggest, or whether he thinks it is just intrinsic to mathematical reasoning whenever sets are involved, a position suggested by the reference to its application ‘everywhere in mathematical deduction’. By the time of his second well-ordering paper of 1908, Zermelo seems to have moved away from the idea of AC as a ‘logical’ principle in the sense of a logical law, and appears to put the emphasis more on the view of it as intrinsic to the subject matter; there it appears as Axiom IV, and, as we saw, Axiom VI of Zermelo 1908b.[^note-25]

#### 2.2.3 Objections to the 1904 Proof

There were three central objections.

1. Objections to the Choice Principle.
2. Objections to Zermelo's general operation with sets, especially well-orderings.
3. Objections to impredicative definitions.

Let us briefly deal with these.

(a) The objections to the choice principle were of two kinds. The main objection was put forward by Borel in 1905 in the *Mathematische Annalen* (Borel 1905)[^borel-1905], the journal which published Zermelo's paper, and it is also widely discussed in correspondence between some leading French mathematicians, and also published in that year in the same Journal (see Hadamard et al. 1905)[^hadamard-1905]. The objection is basically that Zermelo's principle fails to specify a ‘law’ or ‘rule’ by which the choices are effected; in other words, the covering used is not explicitly defined, which means that the resulting well-ordering is not explicitly defined either. In a letter to Borel, Hadamard makes it clear that the opposition in question is really that between the assumption of the existence of an object which is fully described, and of the existence of an object which is *not* fully described (see Hadamard et al. 1905, esp. 262)[^hadamard-1905]. In his reply, Zermelo remarks that the inability to describe the choices is why the choice principle is in effect an *axiom*, which has to be added to the other principles. In effect, the position is that if one wants to do certain things which, e.g., rely on the WOT, then the choice principle is indispensable. His position, to repeat, is like the one that Euclidean geometry takes towards parallels.

(b) An objection to the choice principle was also put forward by Peano. This objection seems to be that since the choice principle cannot be proved ‘syllogistically’ (i.e., from the principles of Peano's *Formulario*), then it has to be rejected (see Peano 1906)[^peano-1906]. (Peano does think, however, that finite versions of the choice principle are provable, relying essentially on repeated applications of a version for classes of the basic logical principle EI mentioned above (§2.2.1). Zermelo's reply is the following. Axiom systems like Peano's are constructed so as to be adequate for mathematics; but how does one go about selecting the ‘basic principles’ required? One cannot assemble a complete list of adequate principles, says Zermelo, without careful inspection of actual mathematics and thereby a careful assessment of what principles are actually necessary to such a list, and such inspection would show that the choice principle is surely one such; in other words, a selection of principles such as Peano's is very much a *post hoc* procedure. The reply to Peano is of a piece with the reply to Borel, and recalls strongly the invocation in Zermelo (1908b: 261)[^zermelo-1908b], that it is necessary to distill principles from the actual operation with sets. He supports his claim that the choice principle is necessary by a list of seven problems which ‘in my opinion, could not be dealt with at all without the principle of choice’ (Zermelo 1908a: 113)[^zermelo-1908a].[^note-26] In particular he points out that the principle is indispensable for any reasonable theory of infinite cardinality, for only it guarantees the right results for infinite unions/sums, and in addition is vital for making sense of the very definition of infinite product. That Peano cannot establish the choice principle from his principles, says Zermelo, strongly suggests that his list of principles is not ‘complete’ (Zermelo 1908a: 112)[^zermelo-1908a].

(c) Another line of objection, represented in different ways by Bernstein (Bernstein 1905)[^bernstein-1905], Jourdain (Jourdain 1904, 1905b)[^jourdain-1904][^jourdain-1905b] and Schoenflies (Schoenflies 1905)[^schoenflies-1905], was that Zermelo's general operation with sets in his proof was dangerous and flirts with paradox. (See also Hallett 1984, 176–182.)[^hallett-1984] In its imprecise form, the objection is that Zermelo is less than explicit about the principles he uses in 1904, and that he employs procedures which are reminiscent of those used crucially in the generation of the Burali-Forti antinomy, e.g., in showing that if the set *L*_{γ} ≠ *M*, then it can be extended. (What if *L*_{γ} is already the collection *W*?)

Zermelo's reply is dismissive, but there is something to the criticism. Certainly Zermelo's 1904 proof attempts to show that WOT can be proved while by-passing the general abstract theory of well-ordering and its association with the Cantorian ordinals, and therefore also bypassing ‘the set *W*’ (as it was widely known) of *all* Cantorian ordinals (denoted ‘Ω’ by Cantor), and consequently the Burali-Forti antinomy. However, whatever Zermelo's *intention*, there is no *explicit* attempt to exclude the possibility that *L*_{γ} = *W* and thus the suggestion that antinomy might threaten. Of course, Zermelo, referring to critics who ‘base their objections upon the “Burali-Forti antinomy” ’, declares that this antinomy ‘*is without significance* for my point of view, since the principles I employed *exclude* the existence of a set *W* [of all ordinals]’ (Zermelo 1908a: 128, with earlier hints on 118–119)[^zermelo-1908a] that the real problem is with the ‘more elementary’ Russell antinomy. It is also true that at the end of the 1904 paper, Zermelo states that the argument holds for those sets *M* ‘for which the totality of subsets, and so on, is meaningful’, which, in retrospect is clearly a hint at important restrictions on set formation. Even so, Zermelo's attitude is unfair. It could be that the remark about ‘the totality of subsets etc.’ is an indirect reference to difficulties with the comprehension principle, but even so the principle is not repudiated explicitly in the 1904 paper, neither does Zermelo put in its place another principle for the conversion of properties to sets, which is what the *Aussonderungsaxiom* of the 1908 axiomatisation does. Moreover, he does not say that the existence principles on which the proof is based are the *only* set existence principles, and he does not divorce the proof of the theorem from the Cantorian assumptions about well-ordering and ordinals. Indeed, Zermelo assumes that ‘every set can be well-ordered’ is equivalent to the Cantorian ‘every cardinality is an aleph’ (Zermelo 1904: 141)[^zermelo-1904]. And despite his later claim (Zermelo 1908a: 119)[^zermelo-1908a], he does *appear* to use the ordinals and the informal theory of well-ordering in his definition of γ-sets, where a γ-set is ‘any well-ordered *M*_{γ}…’, without any specification of how ‘well-ordered set’ is to be defined. What assurance is there that *this* can all be reduced to Zermelo's principles? One important point here is that it had not yet been shown that all the usual apparatus of set-theoretic mathematics (relations, ordering relations, functions, cardinal equivalence functions, order-isomorphisms, etc.) could be reduced to a few simple principles of set existence. All of this was to come in the wake of Zermelo's axiomatisation, and there is little doubt that this line of criticism greatly influenced the shape of the second proof given in 1908, of which a little more below.

(d) The last line of objection was to a general feature of the 1904 proof, which was not changed in the second proof, namely the use of what became known as ‘impredicative definition’. An impredicative definition is one which defines an object *a* by a property *A* which itself involves reference, either direct or indirect, to all the things with that property, and this must, of course, include *a* itself. There is a sense, then, in which the definition of *a* involves a circle. Both Russell and Poincaré became greatly exercised about this form of definition, and saw the circle involved as being ‘vicious’, responsible for all the paradoxes. If one thinks of definitions as like construction principles, then indeed they are illegitimate. But if one thinks of them rather as ways of singling out things which are already taken to exist, then they are not illegitimate. In this respect, Zermelo endorses Hilbert's view of existence. To show that some particular thing ‘exists’ is to show that it is in 𝔅, i.e., to show by means of a finite proof from the axioms that it exists in 𝔅. What ‘exists’, then, is really a matter of what the axioms, taken as a whole, determine. If the separation, power set and choice principles are axioms, then for a given *M* in the domain, there will be choice functions/sets on the subsets of *M*, consequently well-orderings, and so forth; if these principles are not included as axioms, then such demonstrations of existence will not be forthcoming. From this point of view, defining within the language deployed is much more like what Zermelo calls ‘determination’, since definitions, although in a certain sense arbitrary, have to be supported by existence proofs, and of course in general it will turn out that a given extension can be picked out by several, distinct ‘determinations’. In short, Zermelo's view is that definitions pick out (or determine) objects from among the others in the domain being axiomatised; they are not themselves responsible for showing their *existence*. In the end, the existence of a domain 𝔅 has to be guaranteed by a consistency proof for the collection of axioms. Precisely this view about impredicative definitions was put forward in Ramsey (1926: 368–369)[^ramsey-1926] and then later in Gödel's 1944 essay on Russell's mathematical logic as part of his analysis of the various things which could be meant by Russell's ambiguously stated Vicious Circle Principle. (See Gödel 1944: 136, 127–128 of the reprinting in Gödel 1990. See also Hadamard's letters in Hadamard et al. 1905.)[^gödel-1944][^gödel-1990][^hadamard-1905] To support his view, Zermelo points out that impredicative definitions are taken as standard in established mathematics, particularly in the way that the least upper bound is defined; witness the Cauchy proof of the Fundamental Theorem of Algebra. Once again, Zermelo's reply is coloured by the principle of looking at the actual practice of mathematics.[^note-27]

#### 2.2.4 Zermelo's second proof of the WOT, 1908

As mentioned, Zermelo published a second proof of the WOT, submitted to *Mathematische Annalen* just two weeks before the submission of his ‘official’ axiomatisation, and published in the same volume as that axiomatisation. This proof is too elaborate to be described here; a much fuller description can be found in Hallett (2010b: 94–103)[^hallett-2010b], but some brief remarks about it must be made nevertheless. Recall that the purpose of the proof was, in large part, to reply to (some of) the criticisms raised in objection to the 1904 proof, and not least to clarify the status of the choice principle.

Suppose *M* is the set given, and suppose (using Zermelo's notation) that 𝔘*M* is the set of its subsets (‘*Untermengen*’). The basic procedure in the 1904 proof was to single out certain subsets of *M* and to show that these can in effect be ‘chained’ together, starting from modest beginnings (and using the choice function γ); thus we have {*m*₁}, where *m*₁ = γ(*M*), {*m*₁, *m*₂}, where again *m*₁ = γ(*M*) and *m*₂ = γ(*M* − {*m*₁}), and so on. In this way, the proof shows that one can ‘build up’ to the whole of *M* itself.[^note-28] This ‘build-up’ is one of the things which provoked scepticism, and particularly the step which shows that *M* itself must be embraced by it. In the 1908 proof, the basic idea is to start from *M* itself, and consider ‘cutting down’ by the element ‘chosen’ by the choice principle, instead of building up. Thus, if one accepts that if *M* is a legitimate set, then so is 𝔘*M*, and there is not the same danger of extending into inconsistent sets, not even the appearance of danger. Again the key thing is to show that the sets defined are in fact ‘chained’ together and are in the right way exhaustive.

In the 1904 proof, there are points where it looks as if Zermelo is appealing to arbitrary well-orderings, and thus indirectly arbitrary ordinals. This is avoided in the 1908 proof (as it could have been in the 1904 proof) by focusing on the particular ‘chain’ which the proof gives rise to. It is this chain itself which exhibits the well-ordering.

In the modern understanding of set theory, to show that there is a well-ordering on *M* would be to show that there is a set of ordered pairs of members of *M* which is a relation satisfying the right properties of a well-ordering relation over *M*. It is well to remember that Zermelo's task in 1908 was constrained in that he had to establish the existence of a well-ordering using only the set-theoretical material *available to him*. This material did not involve the general notion of ordinal and cardinal numbers, not even the general notions of relation and function. What Zermelo used, therefore, was the *particular* relation *a* ⊆ *b* of being a subset, and it is important to observe that the chain produced is ordered by this relation.

Why would one expect this latter to work? Well, the chain produced is naturally a subset well-ordering, for it is both linear and also such that the intersection of arbitrary elements of members of the chain is itself a member of the chain, and thus there is a natural subset-least element for each subset of members of the chain. But the wider explanation is hinted at towards the end of Zermelo's proof. Suppose a set *M* is (speaking informally) *de facto* well-ordered by an ordering relation ≺. Call the set ℜ_{≼}(*a*) = {*x* ∈ *M* : *a* ≼ *x*} the ‘remainder [*Rest*]’ determined by *a* and the ordering ≺. Consider now the set of ‘remainders’ given by this ordering, i.e., {ℜ_{≼}(*x*) : *x* ∈ *M*}. This set is in fact well-ordered by reverse inclusion, where the successor remainder to ℜ_{≼}(*a*) is just the remainder determined by *a*'s successor *a*′ under ≺, and where intersections are taken at the limit elements (the intersection of a set of remainders is again a remainder). But not only is this set well-ordered by reverse inclusion, the ordering is *isomorphic* to the ordering ≺ on *M*, that is:

> *a* ≺ *b* if and only if ℜ_{≼}(*b*) ⊂ ℜ_{≼}(*a*).

Zermelo's 1908 construction is now meant to define a ‘remainder set’ directly without detour through some ≺; the resultant inclusion ordering is then ‘mirrored’ on *M*. The key thing is to show that the chain of subsets of *M* picked out really matches *M* itself. But if there were some element *a* ∈ *M* which did not correspond to a remainder ℜ_{≼}(*a*), then it must be possible to use the choice function to ‘squeeze’ another remainder into the chain, which would contradict the assumption that all the sets with the appropriate definition are already in the chain.[^note-29] We have spoken of functions and relations here. But in fact Zermelo avoids such talk. He defines *M* as being ‘well-ordered’ when each element in *M* ‘corresponds’ uniquely to such a ‘remainder’ (Zermelo 1908a: 111)[^zermelo-1908a]. This shows, says Zermelo, that the theory of well-ordering rests ‘exclusively upon the elementary notions of set theory’, and that ‘the uninformed are only too prone to look for some mystical meaning behind Cantor's relation *a* ≺ *b*’ (Zermelo 1908a)[^zermelo-1908a].

One can be considerably more precise about the relation between orderings on *M* and ‘remainder inclusion orderings’ in 𝔘*M*. Much of this was worked out in Hessenberg (1906)[^hessenberg-1906], and was therefore known to Zermelo (Zermelo and Hessenberg were in regular contact), and simplified greatly by Kuratowski in the 1920s. We will have reason to refer to Kuratowski briefly in the next section.[^note-30]

What about the choice principle? In 1904, this is framed in effect as a choice function, whose domain is the non-empty subsets on *M*. But in 1908, Zermelo frames it differently:

> Axiom IV. A set *S* that can be decomposed into a set of disjoint parts *A*, *B*, *C*, …, each containing at least one element, possesses at least one subset *S*₁ having exactly one element in common with each of the parts *A*, *B*, *C*, … considered. (Zermelo 1908a: 110)[^zermelo-1908a]

In other words, the choice principle is now cast in a *set* form, and not in the function form of 1904.

In the 1908 axiomatisation, the axiom is stated in much the same way, but is called there (though not in the well-ordering paper) the ‘Axiom of Choice’. However, the 1908 paper on WOT does say that the axiom provides a set (the *S*₁) of ‘simultaneous choices’, to distinguish them from the ‘successive choices’ used in the pre-Zermelo versions of well-ordering. It is to be noted that in 1921, Zermelo wrote to Fraenkel in partial repudiation of the designation ‘Axiom of Choice’, saying that ‘there is no sense in which my theory deals with a real “choice” ’.[^note-31]

#### 2.2.5 The Axioms of the 1908 WOT Paper

What axioms governing set-existence does Zermelo rely on in Zermelo (1908a)[^zermelo-1908a]? At the start of the paper, Zermelo list two ‘postulates’ that he explicitly depends on, a version of the separation axiom, and the power set axiom. Later on he lists Axiom IV, which, as noted, asserts the existence of a choice set for any set of disjoint non-empty sets. In addition to this, Zermelo makes use of the existence of various elementary sets, though he doesn't say exactly which principles he relies on. In the axiomatisation which follows two weeks later, Zermelo adopts all these axioms, but adds clarification about the elementary sets. He also adds the Axiom of Infinity, to guarantee that there are infinite sets, and the Axiom of Extensionality, which codifies the assumption that sets are really determined by their members, and not by the accidental way in which these members are selected. In addition, as we have noted, he now calls the Axiom of Choice by this name.

## 3. The Major Problems with Zermelo's System

Zermelo's system, although it forms the root of all modern axiomatisations of set theory, initially faced various difficulties. These were:

1. Problems with the Axiom of Choice.
2. Problem with the formulation of the Separation Axiom.
3. Problems of ‘completeness’, one of Hilbert's important desiderata on the adequacy of an axiom system. Specifically, there were problems representing ordinary mathematics purely set-theoretically, and also problems representing fully the transfinite extension of mathematics which Cantor had pioneered.

The problems concerning the Axiom of Choice were discussed above; we now discuss the difficulties with the formulation of Separation and those of ‘completeness’.

### 3.1 Separation

The problem with the Axiom of Separation is not with the obviousness of the principle; it *seems* straightforward to accept that if one has a set of objects, one can separate off a subclass of this set by specifying a property, and treat this in turn as a set. The question here is a subtler one, namely that of how to formulate this principle as an axiom. What means of ‘separating off’ are to be accepted? What are allowable as the properties? As a matter of practice, we use a language to state the properties, and in informal mathematics, this is a mixture of natural language and special mathematical language. The Richard Paradox (see Richard 1905 and also the papers of Poincaré 1905, 1906a,b)[^poincaré-1905][^poincaré-1906a][^richard-1905] makes it clear that one has to be careful when defining properties, and that the unregulated use of ‘ordinary language’ can lead to unexpected difficulties.

Zermelo's answer to this, in moving from the system of the second well-ordering paper to the axiomatisation, is to try specifying what properties are to be allowed. He calls the properties to be allowed ‘definite properties’ (‘*Klassenaussagen*’ or ‘propositional functions’), and states:

> A question or assertion 𝔈 is said to be “*definite*” if the fundamental relations of the domain, by means of the axioms and the universally valid laws of logic, determine without arbitrariness whether it holds or not. Likewise a “propositional function” 𝔈(*x*), in which the variable term *x* ranges over all individuals of a class 𝔎, is said to be “definite” if it is definite for each single individual *x* of the class 𝔎. Thus the question whether *a* ε *b* or not is always definite, as is the question whether *M* ⊆ *N* or not.

Zermelo asserts that this shows that paradoxes involving the notions of definability (e.g., Richard's) or denotation (König's) are avoided, implying that what is crucial is the restriction to the ‘fundamental relations of the domain’ (so, ε, =).

The basic problem is that it is not explained by Zermelo what the precise route is from the fundamental relations ε and = to a given ‘definite property’; it is this which gives rise to a general doubt that the Separation Axiom is not, in fact, a safe replacement for the comprehension principle (see Fraenkel 1927: 104)[^fraenkel-1927]. This plays into the hands of those, who, like Poincaré, consider adoption of the Separation Axiom as insufficiently radical in the search for a solution to the paradoxes. Poincaré writes:

> Mr. Zermelo does not allow himself to consider the set of all the objects which satisfy a certain condition because it seems to him that this set is never closed; that it will always be possible to introduce new objects. On the other hand, he has no scruple in speaking of the set of objects which are part of a certain *Menge* *M* and which also satisfy a certain condition. It seems to him that one cannot possess a *Menge* without possessing at the same time all its elements. Among these elements, he will choose those which satisfy a given condition, and will be able to make this choice very calmly, without fear of being disturbed by the introduction of new and unforeseen elements, since he already has all these elements in his hands. By positing beforehand this *Menge* *M*, he has erected an enclosing wall which keeps out the intruders who could come from without. But he does not query whether there could be intruders from within whom he enclosed inside his wall. (Poincaré 1909: 477; p. 59 of the English translation)[^poincaré-1909]

Here, Poincaré is referring indirectly to his view that the paradoxes are due to impredicative set formation, and this of course will be still be possible even with the adoption of the Axiom of Separation.

The problem of the lack of clarity in Zermelo's account was addressed by Weyl in 1910 (Weyl 1910; see especially p. 113)[^weyl-1910] and then again by Skolem in 1922 (Skolem 1923, p. 139 of the reprint)[^skolem-1923]. What Weyl and Skolem both proposed, in effect, is that the question of what ‘definite properties’ are can be solved by taking these to be the properties expressed by 1-place predicate formulas in what we now call first-order logic. In effect, we thus have a recursive definition which makes the definite properties completely transparent by giving each time the precise route from ε, = to the definite property in question. This does not deal with all aspects of Poincaré's worry, but it does make it quite clear what definite properties are, and it does also accord with Zermelo's view that the relations =, ε are at root the only ones used.[^note-32]

Fraenkel (1922 and later) took a different approach with a rather complicated direct axiomatisation of the notion of definite property, using recursive generation from the basic properties giving a notion which appears to be a subset of the recursively defined first-order properties.

Zermelo accepted none of these approaches, for two reasons. First, he thought that the recursive definitions involved make direct use of the notion of finite number (a fact pointed out by Weyl 1910)[^weyl-1910], which it ought to be the business of set theory to explain, not to presuppose. Secondly, he became aware that using essentially a first-order notion condemns the axiomatic system to countable models, the fundamental fact pointed out in Skolem (1923)[^skolem-1923]. His own approach was, first, to give a different kind of axiomatisation (see Zermelo 1929)[^zermelo-1929], and then to use (in Zermelo 1930)[^zermelo-1930] an essentially second-order notion in characterising the axiom of separation.[^note-33]

### 3.2 Completeness

There were also problems with the completeness of Zermelo's theory, since there were important theoretical matters with which Zermelo does not deal, either for want of appropriate definitions showing how certain constructions can be represented in a pure theory of sets, or because the axioms set out in Zermelo's system are not strong enough.

#### 3.2.1 Representing Ordinary Mathematics

Zermelo gives no obvious way of representing much of ‘ordinary mathematics’, yet it is clear from his opening remarks that he regards the task of the theory of sets to stand as *the* fundamental theory which should ‘investigate mathematically the fundamental notions “number”, “order”, and “function” ’. (See §1.)

The first obvious question concerns the representation of the ordinary number systems. The natural numbers are represented by Zermelo as by ∅, {∅}, {{∅}}, …, and the Axiom of Infinity gives us a set of these. Moreover, it seems that, since both the set of natural numbers and the power set axiom are available, there are enough sets to represent the rationals and the reals, functions on reals etc. What are missing, though, are the details: how exactly does one represent the right equivalence classes, sequences etc.? And assuming that one *could* define the real numbers, how does one characterise the field operations on them? In addition, as mentioned previously, Zermelo has no natural way of representing either the general notions of relation or of function. This means that his presentation of set theory has no natural way of representing those parts of mathematics (like real analysis) in which the general notion of function plays a fundamental part.

A further difficulty is that the lack of the notion of function makes the general theory of the comparison of sets by size (or indeed by order) cumbersome. Zermelo does develop a way of expressing, for disjoint sets *a*, *b*, that *a* is of the same size as *b*, by first defining a ‘product’ of two disjoint sets, and then isolating a set of unordered pairs (a certain subset of this product) which ‘maps’ one of the sets one-to-one onto the other. But this is insufficiently general, and does not in any case indicate any way to introduce ‘the’ size of *a*. Russell's method (defining the cardinality of *M* as the set *card*(*M*) = {*N* : *N* ∼ *M*} (where ‘∼’ means ‘cardinally equivalent to’) is clearly inappropriate, since with a set *a* = {*b*}, *card*(*a*) (which should be the cardinal number 1) is as big as the universe, and the union set of 1 would indeed be the universal ‘set’. Over and above this, there is the more specific problem of defining the aleph numbers.

The second major difficulty is along the same lines, concerning, not functions, but relations, and thus ordering relations and ordinal numbers. As we have seen (in §2.2.4), Zermelo has the beginnings of an answer to this in his second proof of the WOT, for this uses a theory of subset-orderings to represent the underlying ordering of a set. It turns out that the method given in this particular case suggests the right way to capture the general notion.

#### 3.2.2 Ordinality

Zermelo's idea (1908a) was pursued by Kuratowski in the 1920s, thereby generalising and systematising work, not just of Zermelo, but of Hessenberg and Hausdorff too, giving a simple set of necessary and sufficient conditions for a subset ordering to represent a linear ordering. He also argues forcefully that it is in fact *undesirable* for set theory to go beyond this and present a general theory of ordinal *numbers*:

> In reasoning with transfinite numbers one implicitly uses an axiom asserting their *existence*; but it is desirable both from the logical and mathematical point of view to pare down the system of axioms employed in demonstrations. Besides, this reduction will free such reasoning from a foreign element, which increases its æsthetic value. (Kuratowski 1922: 77)[^kuratowski-1922]

The assumption here is clearly that the (transfinite) numbers will have to be added to set theory as new primitives. Kuratowski however undertakes to *prove* that the transfinite numbers can be dispensed with for a significant class of applications.[^note-34] Application of the ordinal numbers in analysis, topology, etc. often focuses on some process of definition by transfinite recursion over these numbers. Kuratowski succeeds in showing that in a significant class of cases of this kind, the ordinals can be avoided by using purely set-theoretic methods which are reproducible in Zermelo's system. As he notes:

> From the viewpoint of Zermelo's axiomatic theory of sets, one can say that the method explained here allows us to deduce theorems of a certain well-determined general type *directly* from Zermelo's axioms, that is to say, without the introduction of any independent, supplementary axiom about the existence of transfinite numbers. (Kuratowski 1922: 77)[^kuratowski-1922][^note-35]

It is in this reductionist context that Kuratowski develops his very general theory of maximal inclusion orderings, which shows, in effect, that all orderings on *a* can really be represented as inclusion orderings on appropriate subsets of the power set of *a*, thus reducing ordering to Zermelo's primitive relation ε.

One immediate, and quite remarkable, result of this work is that it shows how one can *define* the general notions of relation and function in purely set-theoretic terms. It had long been recognised that relations/functions can be conceived as sets of ordered pairs, and Kuratowski's work now shows how to define the ordered pair primitively. The ordered pair (*a*, *b*) can be considered informally as the unordered pair *M* = {*a*, *b*}, together with an ordering relation *a* < *b*. Suppose this relation is treated now via the theory of inclusion chains. The only maximal inclusion chains in the power set of *M* are {∅, {*a*}, {*a*, *b*}} and {∅, {*b*}, {*a*, *b*}}. Using Kuratowski's definition of the ordering ‘<’ derived from a maximal inclusion chain, these chains must then correspond to the orderings *a* < *b* and *b* < *a* on {*a*, *b*} respectively. If ∅ is ignored, the resulting chain {{*a*}, {*a*, *b*}} is thus associated with the relation *a* < *b*, and so with the ordered set (pair) (*a*, *b*). It is then quite natural to *define* (*a*, *b*) as {{*a*}, {*a*, *b*}} (see Kuratowski 1921: 170–171)[^kuratowski-1921]. One can now define the product *a* × *b* of *a* and *b* as the set of all ordered pairs whose first member is in *a* and whose second member is in *b*; relations on *a* can now be treated as subsets of *a* × *a*, and functions from *a* to *b* as certain subsets of *a* × *b*. Thus, many of the representational problems faced by Zermelo's theory are solved at a stroke by Kuratowski's work, building as it does on Zermelo's own.

#### 3.2.3 Cardinality

But there was a problem concerning cardinality which is independent of the problem of definitional reduction. It was pointed out by both Fraenkel and Skolem in the early 1920s that Zermelo's theory cannot provide an adequate account of cardinality. The axiom of infinity and the power set axiom together allow the creation of sets of cardinality ≥ ℵ_{*n*} for each natural number *n*, but this (in the absence of a result showing that 2^{ℵ₀} > ℵ_{*n*} for every natural number *n*) is not enough to guarantee a set whose power is ≥ ℵ_{ω}, and a set of power ℵ_{ω} is a natural next step (in the Cantorian theory) after those of power ℵ_{*n*}. Fraenkel proposed a remedy to this (as did Skolem independently) by proposing what was called the *Ersetzungsaxiom*, the Axiom of Replacement (see Fraenkel 1922: 231 and Skolem 1923: 225–226)[^fraenkel-1922][^skolem-1923]. This says, roughly, that the ‘functional image’ of a set must itself be a set, thus if *a* is a set, then {*F*(*x*) : *x* ∈ *a*} must also be a set, where ‘*F*’ represents a functional correspondence. Such an axiom is certainly sufficient; assume that *a*₀ is the set of natural numbers {0, 1, 2, …}, and now assume that to each number *n* is associated an *a*_{*n*} with power ℵ_{*n*}. Then according to the replacement axiom, *a* = {*a*₀, *a*₁, *a*₂, …} must be a set, too. This set is countable, of course, but (assuming that the *a*_{*n*} are all disjoint) the union set of *a* must have cardinality at least ℵ_{ω}.

The main difficulty with the Replacement Axiom is that of how to formulate the notion of a functional correspondence. This was not solved satisfactorily by Fraenkel, but the Weyl/Skolem solution works here, too: a functional correspondence is (in effect) just any first-order 2-place predicate ϕ(*x*, *y*) which satisfies the condition of uniqueness, i.e., ∀*x*, *y*, *z*{[ϕ(*x*, *y*) ∧ ϕ(*x*, *z*)] → *y* = *z*}. With this solution, the Replacement Axiom will be (as required) stronger than Zermelo's original Separation Axiom and indeed can replace it; however, in Fraenkel's system, one can prove his version of the Replacement Axiom from his version of the Separation Axiom, which shows that his separate definition of function is not sufficiently strong. (For details, see Hallett 1984: 282–286.)[^hallett-1984]

Zermelo initially had doubts about the Replacement Axiom (see the letter to Fraenkel from 1922 published in Ebbinghaus 2007: 137)[^ebbinghaus-2007][^fraenkel-1922], but he eventually accepted it, and a form of it was included in his new axiomatisation published in 1930 (Zermelo 1930)[^zermelo-1930]. Skolem's formulation is the one usually adopted, though it should be noted that von Neumann's own formulation is rather different and indeed stronger.[^note-36]

#### 3.2.4 Ordinals

Although Kuratowski's work solved many of the representational problems for Zermelo's theory, and the Replacement Axiom shows how the most obvious cardinality gap can be closed, there still remained the issue (Kuratowski's view to one side) of representing accurately the full extent of the theory which Cantor had developed, with the transfinite numbers as fully fledged objects which ‘mirror’ the size/ordering of sets. Once the ordinal number-classes are present, the representation of the alephs is not a severe problem, which means that the representation of transfinite numbers amounts to assuring the existence of sufficiently many transfinite *ordinal* numbers. Indeed, as was stated above, the hypothesis that the scale of aleph numbers is sufficient amounts to the claim that any set can be ‘counted’ by some ordinal. There are then two interrelated problems for the ‘pure’ theory of sets: one is to show how to define ordinals as sets in such a way that the natural numbers generalise; the other problem is to make sure that there are enough ordinals to ‘count’ all the sets.

The problem was fully solved by von Neumann in his work on axiomatic set theory from the early 1920s. Cantor's fundamental theorems about ordinal numbers, showing that the ordinals are the *representatives* of well-ordered sets, are the theorem that every well-ordered set is order-isomorphic to an initial segment of the ordinals, and that every ordinal is itself the order-type of the set of ordinals which precede it. These results prove crucial in the von Neumann treatment. Von Neumann's basic idea was explained by him as follows:

> What we really wish to do is to take as the basis of our considerations the proposition: ‘Every ordinal is the type of the set of all ordinals that precede it’. But in order to avoid the vague notion ‘type’, we express it in the form: ‘Every ordinal is the set of the ordinals that precede it’. (von Neumann 1923, p. 347 of the English translation)[^neumann-1923]

According to von Neumann's idea, 1 is just {0}, 2 is just {0, 1}, 3 is just {0, 1, 2} and so on. On this conception, the first transfinite ordinal ω is just {0, 1, 2, 3, …, *n*, …}, and generally it's clear that the immediate successor of any ordinal α is just α ∪ {α}. If we identify 0 with ∅, as Zermelo did, then we have available a reduction of the general notion of ordinal to pure set theory, where the canonical well-ordering on the von Neumann ordinals is just the subset relation, i.e., α < β just in case α ⊂ β, which von Neumann later shows is itself equivalent to saying α ∈ β. (See von Neumann 1928, p. 328 of the reprinting.)[^neumann-1928] So again, inclusion orderings are fundamental.

Von Neumann gives a general definition of his ordinals, namely that a set α is an ordinal number if and only if it is a set ordered by inclusion, the inclusion ordering is a well-ordering, and each element ξ in α equals the set of elements in the initial segment of the ordering determined by ξ. This connects directly with Kuratowski's work in the following way. Suppose *M* is a well-ordered set which is then mirrored by an inclusion chain **M** in the power set of *M*. Then the first few elements of the inclusion chain will be the sets ∅, {*a*}, {*a*, *b*}, {*a*, *b*, *c*}, …, where *a*, *b*, *c*, … are the first, second, third …elements in the well-ordering of *M*. The von Neumann ordinal corresponding to *M* will also be an inclusion ordering whose first elements will be

> ∅, {∅}, {∅, {∅}}, {∅, {∅}, {∅, {∅}}}, …

(in other words, 0, 1, 2, 3…), and we have 0 ⊂ 1 ⊂ 2 ⊂ 3 ⊂… in mirror image of ∅ ⊂ {*a*} ⊂ {*a*, *b*} ⊂ {*a*, *b*, *c*} ⊂ …

These von Neumann ordinals had, in effect, been developed before von Neumann's work. The fullest published theory, and closest to the modern account, is to be found in Mirimanoff's work published in 1917 and 1921 (see Mirimanoff 1917a,b, 1921)[^mirimanoff-1917a][^mirimanoff-1921], though he doesn't take the final step of identifying the sets he characterises with the ordinals (for an account of Mirimanoff's work, see Hallett 1984: 273–275)[^hallett-1984]. It is also clear that Russell, Grelling and Hessenberg were close to von Neumann's general set-theoretic definition of ordinals. But crucially Zermelo himself developed the von Neumann conception of ordinals in the years 1913–1916, (for a full account, see Hallett 1984: 277–280 and Ebbinghaus 2007: 133–134)[^ebbinghaus-2007][^hallett-1984]. Zermelo's idea was evidently well-known to the Göttingen mathematicians, and there is an account of it in Hilbert's lectures ‘*Probleme der mathematischen Logik*’ from 1920, pp. 12–15.[^note-37]

Despite all these anticipations, it is still right to ascribe the theory to von Neumann. For it was von Neumann who revealed the extent to which a full theory of the ordinals depends on the Axiom of Replacement. As he wrote later:

> A treatment of ordinal number closely related to mine was known to Zermelo in 1916, as I learned subsequently from a personal communication. Nevertheless, the fundamental theorem, according to which to each well-ordered set there is a similar ordinal, could not be rigorously proved because the replacement axiom was unknown. (von Neumann 1928: 374, n. 2)[^neumann-1928]

The theorem von Neumann states is the central result of Cantor's mentioned here in the second paragraph of this section. As von Neumann goes on to point out here (also p. 374), it is the possibility of definition by transfinite induction which is key, and a rigorous treatment of this requires being able to prove at each stage in a transfinite inductive process that the collection of functional correlates to a set is itself a set which can thus act as a new argument at the next stage. It is just this which the replacement axiom guarantees. Once justified, definition by transfinite induction can be used as the basis for completely general definitions of the arithmetic operations on ordinal numbers, for the definition of the aleph numbers, and so on. It also allows a fairly direct transformation of Zermelo's first (1904) proof of the WOT into a proof that every set can be represented by (is equipollent with) an ordinal number, which shows that in the Zermelo system with the Axiom of Replacement added there *are* enough ordinal numbers.[^note-38]

It is thus remarkable that von Neumann's work, designed to show how the transfinite ordinals can be incorporated directly into a pure theory of sets, builds on and coalesces with both Kuratowski's work, designed to show the *dispensability* of the theory of transfinite ordinals, and also the axiomatic extension of Zermelo's theory suggested by Fraenkel and Skolem.

## 4. Further reading

For a summary of the Cantorian theory as it stood in the early years of the twentieth century, see Young and Young (1906)[^young-1906], and the magisterial Hausdorff (1914)[^hausdorff-1914]; for further reading on the development of set theory, see the books Ferreiros 1999, Hallett 1984, Hawkins 1970, and Moore 1982. See also the various papers on the history of set theory by Akihiro Kanamori (especially Kanamori 1996, 1997, 2003, 2004, 2012)[^kanamori-1996][^kanamori-1997][^kanamori-2003][^kanamori-2004][^kanamori-2012] and the joint paper with Dreben (Dreben and Kanamori 1997)[^dreben-1997][^kanamori-1997]. For the place of set theory in the development of modern logic, see Mancosu et al., 2009, especially pages 345–352.

For an account of the various axiom systems and the role of the different axioms, see Fraenkel et al. (1973). For a detailed summary of the role of the Axiom of Choice, and insight into the question of its status as a logical principle, see Bell (2009)[^bell-2009].

This entry will be supplemented by a further entry on axiomatizations of set theory after Zermelo from 1920 to 1940.

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

Most of the original sources surrounding Zermelo's work were written in German, and some in French; when translations of these works into English are available, bibliographic information for the translations follows the citation of the original text. Similarly for older, relatively inaccessible texts that have been republished in more current works.

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=zermelo-set-theory). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/zermelo-set-theory/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=zermelo-set-theory&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](http://philpapers.org/sep/zermelo-set-theory/) at [PhilPapers](http://philpapers.org/), with links to its database. |

## Other Internet Resources

[Please contact the author with suggestions.]

## Related Entries

Russell’s paradox | set theory | set theory: alternative axiomatic theories | set theory: early development

## Notes（原文脚注）

[^note-1]: Page number specifications on their own will refer to Zermelo (1908b)[^zermelo-1908b]. The translations of Zermelo are all taken from Zermelo (2010)[^zermelo-2010], where the original pagination is preserved and where the original German can be found.

[^note-2]: As Russell admits:

> …the question arises: which propositional functions define classes which are single terms as well as many, and which do not? And with this question our real difficulties begin. (Russell 1903: 103)[^russell-1903]

[^note-3]: This is taken from the official English translation.

[^note-4]: Zermelo uses ‘ε’ to denote set membership rather than now standard ‘∈’.

[^note-5]: Various things should be noted here. Firstly, Zermelo's argument goes back to 1902 (see Felgner 2010: 167)[^felgner-2010]; he had discovered the Russell paradox independently as early as 1900. Secondly, Zermelo's analysis is already present, in effect, in Russell (1903: §100) where ‘the Contradiction’ is discussed explicitly. Thirdly, the Burali-Forti paradox was treated by Jourdain as a reductio, but it wasn't at all clear which premise in its derivation was under attack (see Hallett 1981)[^hallett-1981].

[^note-6]: See, for example, the principles set out at the beginning of Dedekind 1888, and later the paper published by Harward in 1905 (Harward 1905; Moore 1976)[^harward-1905][^moore-1976].

[^note-7]: For a review of these principles, see Felgner 2010: 174–175. The relevant correspondence of Cantor can be found in Cantor 1991, with English translations in Ewald 1996: volume 2.

[^note-8]: See Ebbinghaus 2007, in particular 36–47. See also Peckhaus 1990. Also helpful is the chronology of Zermelo's career in Zermelo 2010: 42–51, and also the introductory section on Zermelo's life and work.

[^note-9]: Note that, while the notion of consistency itself is stated in syntactic terms, the proofs given in the geometrical work are relative consistency proofs effected by semantic arguments. The demonstration of consistency is in fact by the exhibition [‘*Aufweisung*’] of what we would now call a model.

[^note-10]: See also Hilbert's famous paper on mathematical problems from 1900 (Hilbert 1900a: 265–266)[^hilbert-1900a].

[^note-11]: Hilbert (1918: 411; 152 of reprint, 1112 of English translation) cites Zermelo's work as an example of solving specific problems by means of the axiomatic method. He repeats this in some lectures from 1920:

> Die axiomatische Methode ist durch keine andere ersetzbar. Sie ist und bleibt das unserem Geist angemessene, unentbehrliche Hilfsmittel der exakten Forschung in jedem Gebiete; sie ist fruchtbar und logisch unanfechtbar. Um einen bestimmten Zweig der Wissenschaft zu erforschen, sucht man diesen auf eine möglichst geringe Anzahl von möglichst einfachen und anschaulichen Prinzipien zurückzuführen. Diese Prinzipien heissen Axiome. Nur dadurch gewinnt man eine klare Uebersicht über die ganze Disziplin, wie auch die Möglichkeit ihrer weiteren Entwicklung, dass man ihre Axiome sammelt und als solche aufstellt.
>
> Das glänzendste Beispiel einer vollendeten Ausgestaltung der axiomatischen Methode bietet das betrachtete Axiomensystem von Zermelo. (Hilbert 1920: 33–34.)[^hilbert-1920]

[^note-12]: For an analysis of Hilbert's work of this kind, see Hallett 2008.

[^note-13]: Two sets *M* and *N* are said to have the same size or power or cardinality if they can be put into one-to-one onto correspondence. In this case we say that *M* ≃ *N*. If *M* has the same power as a subset of *N*, we say that *M* ≼ *N*; if in addition to this *M* ≃ *N* fails, we say that *M* ≺ *N*, and that *N* has greater power than *M*. A set is said to be countable if it can be put into one-to-one onto correspondence with the set of natural numbers.

[^note-14]: However, for a survey of other, quite different, attempts to count with infinite numbers, both before Cantor and after, see Mancosu 2009.

[^note-15]: Two ordered sets *A*₁ with ordering *R*₁ and *A*₂ with ordering *R*₂ are said to be order-isomorphic if there is a function *f* which puts them into one-to-one onto correspondence and in addition is such that, for any two elements *a*, *b* in *A*₁, *aR*₁*b* if and only if *f*(*a*)*R*₂*f*(*b*). Thus, *f* shows that the ordering of *A*₁ is reflected in the ordering of *A*₂.

[^note-16]: Recall that the phrase ‘laws of thought [*Gesetze des Denkens*]’ is used by Frege (1879, Vorwort) to refer to logical laws, laws which ‘transcend all particulars [*über allen Besonderheiten erhaben*]’.

[^note-17]: The letters can all be found in Cantor 1991, with English translations, and an important and informative introduction, in Ewald 1996: Volume 2, 923–940. For commentary, see Hallett 1984.

[^note-18]: Hardy (1904: §2) and Jourdain (1905a, among other places) later endorsed a similar ‘selection’ method to show, respectively, that the continuum has a subset of the power of the second number-class and that every cardinal number is an aleph.

[^note-19]: ‘Component’ was Cantor's original term for a subset.

[^note-20]: One could in consequence say that Zermelo's criticism reveals a circularity similar to that revealed in many of the “proofs” of the Euclidean Parallel Postulate.

[^note-21]: Following Cantor, we would put ‘ℵ’ in place of Russell's ‘α’.

[^note-22]: For an account of König's lecture, its aftermath and Zermelo's rôle and comments, see Ebbinghaus 2007: 50–53.

[^note-23]: Zermelo attributes to Erhard Schmidt the idea that each covering gives rise to a well-ordering; see Zermelo 1904: 516.

[^note-24]: For comments on how to move from the informal ‘successive selection’ argument to Zermelo's proof of the WOT, see Hausdorff 1914: 134–136.

[^note-25]: In later work on the set axioms, however, Zermelo again calls AC a ‘logical principle’. See, for example, Zermelo 1930: 31.

[^note-26]: The enumeration of such problems is clearly associated with Zermelo's remark in the 1904 paper that the choice principle cannot be reduced to anything simpler, and ‘*wird aber in der mathematischen Deduktion überall unbedenklich angewendet*’ (Zermelo 1904: 516)[^zermelo-1904].

[^note-27]: For a more detailed account of Poincaré's position, and a brief account of the Cauchy proof, see Hallett 2010b: 109–112, and the further references given there.

[^note-28]: Of course, the proof itself avoids the psychological casting which this explanation has given it.

[^note-29]: This is shown in Zermelo's proof by the demonstration that there is in fact a one-one correspondence between the ‘remainders’ and the set of singletons determined by *M*, i.e., {{*x*} : *x* ∈ *M*}. Using ‘initial segments’ (and unions instead of intersections) with the inclusion relation, not reverse inclusion, would also work just as well, but taking remainders has the advantage of being able to ‘build down’ from the whole of *M* instead of ‘up’ from ∅.

[^note-30]: For an illuminating account of Zermelo's second proof, see Hausdorff 1914: 136–139. For a discussion of Kuratowki's (and other) fundamental work in relation to Zermelo's, see Hallett 2010b: §3.3, or (in more detailed fashion) Hallett 1984: chapter 7, §3(b), 256–266.

[^note-31]: See Ebbinghaus 2007: 285. The central points were reported in Fraenkel 1922: 232–233.

[^note-32]: As the paper (Mancosu et al. 2009: 349)[^mancosu-2009][^mancosu-2009-2] points out, Skolem knew of Weyl's work, since he had reviewed Weyl (1910)[^weyl-1910] in 1912.

[^note-33]: For a much fuller account, see Ebbinghaus 2010. For further subtleties, see Hallett 1984.

[^note-34]: Before the general acceptance of the von Neumann ordinals in the later 1920s and the consequent ‘reduction’ of the full theory of the ordinals to ‘pure’ set theory, there was a vigorous debate about the independent importance of the transfinite numbers. We cannot go into this here.

[^note-35]: For a more elaborate account of Kuratowski's results, see Hallett (1984, 2010b)[^hallett-1984][^hallett-2010b].

[^note-36]: Von Neumann's formulation will be examined in a later article for this Encyclopedia.

[^note-37]: These lectures can be found in Chapter 2 of Ewald et al. 2013; see also the Introduction to this chapter, §4.2.

[^note-38]: For an account of the Axiom of Replacement, and in particular von Neumann's work with it, see Kanamori 2012.

[^bell-2009]: Bell, J., 2009, *The Axiom of Choice*, London: College Publications.

[^benacerraf-1964]: Benacerraf, P. and H. Putnam (eds.), 1964, *Philosophy of Mathematics: Selected Readings*, Oxford: Basil Blackwell.

[^benacerraf-1983]: ––– (eds.), 1983, *Philosophy of Mathematics: Selected Readings*, Second Edition, Cambridge: Cambridge University Press.

[^bernstein-1905]: Bernstein, F., 1905, “Über die Reihe der transfiniten Ordnungszahlen”, *Mathematische Annalen* 60: 187–193.

[^borel-1905]: Borel, E., 1905, “Quelque remarques sur les principes de la théorie des ensembles”, *Mathematische Annalen* 60: 194–195.

[^browder-1976]: Browder, F. (ed.), 1976, *Mathematical Developments Arising from the Hilbert Problems*, Volume 28 of *Proceedings of Symposia in Pure Mathematics*, Providence: American Mathematical Society.

[^cantor-1883a]: Cantor, G., 1883a, “Ueber unendliche, lineare Punktmannichfaltigkeiten” *Mathematische Annalen* 21: 545–591. Reprinted in Cantor 1883b and in Cantor 1932: 165–209. English translation in Ewald 1996, Volume 2.

[^cantor-1883b]: –––, 1883b, *Grundlagen einer allegemeinen Mannigfaltichkeitslehre. Ein mathematisch-philosophischer Versuch in der Lehre des Unendlichen*, Leipzig: B. G. Teubner.

[^cantor-1895]: –––, 1895, “Beiträge zur Begründung der transfiniten Mengenlehre, Erster Artikel”, *Mathematische Annalen* 46: 481–512. Reprinted in Cantor 1932: 282–311. English translation in Cantor 1915.

[^cantor-1897]: –––, 1897, “Beiträge zur Begründung der transfiniten Mengenlehre, Zweiter Artikel”, *Mathematische Annalen* 49: 207–246. Reprinted in Cantor 1932: 312–351. English translation in Cantor 1915.

[^cantor-1915]: –––, 1915, *Contributions to the Founding of the Theory of Transfinite Numbers*, La Salle: Open Court. English translation of Cantor 1895, 1897 by Philip E. B. Jourdain.

[^cantor-1932]: –––, 1932, *Gesammelte Abhandlungen mathematischen und philosophischen Inhalts, mit eläuternden Anmerkungen sowie mit Ergänzungen aus dem Briefwechsel Cantor-Dedekind herausgegeben von Ernst Zermelo*, Berlin: Springer.

[^cantor-1991]: –––, 1991, *Georg Cantor: Briefe. Herausgegeben von Herbert Meschkowski*, Berlin: Springer

[^dedekind-1888]: Dedekind, R., 1888, *Was sind und was sollen die Zahlen?*, Braunschweig: Vieweg und Sohn. Also reprinted in Dedekind 1932: 335–391; English translation in Ewald 1996: 787–833.

[^dedekind-1932]: –––, 1932, *Gesammelte mathematische Werke. Band 3. Herausgegeben von Robert Fricke, Emmy Noether and Öystein Ore*, Braunschweig: Friedrich Vieweg und Sohn. Reprinted with some omissions by Chelsea Publishing Co., New York, 1969.

[^dreben-1997]: Dreben, B. and A. Kanamori, 1997, “Hilbert and set theory”, *Synthese*, 110: 77–125.

[^ebbinghaus-2007]: Ebbinghaus, H.-D., 2007, *Ernst Zermelo: An Approach to His Life and Work*, Berlin: Springer.

[^ebbinghaus-2010]: –––, 2010, “Introductory note to *Über den Begriff von Definitheit in der Axiomatik* [Zermelo 1929]”, in Zermelo 2010: 352–357.

[^ewald-1996]: Ewald, W. (ed.), 1996, *From Kant to Hilbert*, Oxford: Oxford University Press.

[^ewald-2013]: Ewald, W., W. Sieg, and M. Hallett (eds.), 2013, *David Hilbert's Lectures on the Foundations of Logic and Arithmetic, 1917–1933*, Volume 3 of *Hilbert's Lectures on the Foundations of Mathematics and Physics, 1891–1933*, Berlin: Springer.

[^felgner-2010]: Felgner, U., 2010, “Introductory note to *Untersuchungen über die Grundlagen der Mengenlehre, I* [Zermelo 1908b]”, in Zermelo 2010: 160–188.

[^ferreiros-1999]: Ferreiros, J., 1999, *Labyrinth of Thought: A History of Set Theory and its Role in Modern Mathematics*, Science Networks Historical Studies, Basel: Birkhäuser. Second Revised Edition, 2007

[^fraenkel-1973]: Fraenkel, A., Y. Bar-Hillel, and A. Levy, 1973, *Foundations of Set Theory*. Amsterdam: North-Holland Publishing.

[^fraenkel-1922]: Fraenkel, A. A., 1922, “Zu den Grundlagen der Cantor-Zermeloschen Mengenlehre”, *Mathematische Annalen* 86: 230–237.

[^fraenkel-1927]: –––, 1927, *Zehn Vorlesungen über die Grundlegung der Mengenlehre*, Leipzig: B. G. Teubner.

[^frege-1879]: Frege, G., 1879, *Begriffsschrift, eine der arithmetischen nachgebildete Formelsprache des reinen Denkens*, Halle: Louis Nebert. Reprinted in Frege 1964, English translation in van Heijenoort 1967: 1–82.

[^frege-1893]: –––, 1893, *Grundgesetze der Arithmetik*, Band 1, Jena: Hermann Pohle. English translation by Philip Ebert and Marcus Rossberg, *Frege, The Basic Laws of Arithmetic, Derived using Concept-Script*, Oxford: Oxford University Press, forthcoming.

[^frege-1903]: –––, 1903, *Grundgesetze der Arithmetik*, Band II, Jena: Hermann Pohle. English translation by Philip Ebert and Marcus Rossberg, *Frege, The Basic Laws of Arithmetic, Derived using Concept-Script*, Oxford: Oxford University Press, forthcoming.

[^frege-1964]: –––, 1964, *Begriffsschrift und andere Aufsätze. Mit E. Husserls und H. Scholz’ Anmerkungen herausgegeben von Ignacio Angelelli*, Darmstadt: Wissenschaftliche Buchgesellschaft.

[^gödel-1944]: Gödel, K., 1944, “Russell's mathematical logic”, in P. A. Schillp (ed.), *The Philosophy of Bertrand Russell*, pp. 125–153, La Salle: Open Court. Reprinted in Benacerraf and Putnam 1964: 211–232; Benacerraf and Putnam 1983: 447–469; and in Gödel 1990: 119–141.

[^gödel-1990]: –––, 1990, *Kurt Gödel: Collected Works*, Volume 2, edited by Solomon Feferman et al., Oxford: Oxford University Press.

[^haaparanta-2009]: Haaparanta, L. (ed.), 2009, *The Development of Modern Logic*, Oxford: Oxford University Press.

[^hadamard-1905]: Hadamard, J. et al., 1905, “Cinq letters sur la théorie des ensembles”, *Bulletin de la société mathématique de France*, 33: 261–273. Letters between Baire, Borel, Lebesgue and Hadamard on objections to, and defense of, Zermelo's 1904 proof of the well-ordering theorem.

[^hallett-1981]: Hallett, M., 1981, “Russell, Jourdain and ‘limitation of size’”, *British Journal for the Philosophy of Science*, 32: 381–399.

[^hallett-1984]: –––, 1984, *Cantorian Set Theory and Limitation of Size*, Oxford: Clarendon Press.

[^hallett-2008]: –––, 2008, “The ‘purity of method’ in Hilbert's *Grundlagen der Geometrie*”, in P. Mancosu (ed.), *The Philosophy of Mathematical Practice*, pp. 198–255, Oxford: Clarendon Press.

[^hallett-2010a]: –––, 2010a, “Frege and Hilbert”, in M. Potter and T. Ricketts (eds.), *The Cambridge Companion to Frege*, Cambridge: Cambridge University Press.

[^hallett-2010b]: –––, 2010b, “Introductory note to Zermelo's two papers on the well-ordering theorem”, in Zermelo 2010: 80–115.

[^hallett-2004]: Hallett, M. and U. Majer (eds.), 2004, *David Hilbert's Lectures on the Foundations of Geometry, 1891–1902*, Volume 1 of *Hilbert's Lectures on the Foundations of Mathematics and Physics, 1891–1933*, Berlin: Springer.

[^hardy-1904]: Hardy, G. H., 1904, “A theorem concerning the infinite cardinal numbers”, *Quarterly Journal of Pure and Applied Mathematics* 35: 87–94.

[^hartogs-1915]: Hartogs, F., 1915, “Über das Problem der Wohlordnung”, *Mathematische Annalen*, 76: 438–442.

[^harward-1905]: Harward, A. E., 1905, “On the transfinite numbers”, *Philosophical Magazine* 10(6): 439–460.

[^hausdorff-1914]: Hausdorff, F., 1914, *Grundzüge der Mengenlehre*, Leipzig: Von Veit.

[^hawkins-1970]: Hawkins, T., 1970, *Lebesgue's Theory of Integration*. New York: Blaisdell. Reprinted by the Chelsea Publishing Company, New York, 1979.

[^heijenoort-1967]: van Heijenoort, J. (ed.), 1967, *From Frege to Gödel: A Source Book in Mathematical Logic*, Cambridge, Massachusetts: Harvard University Press.

[^heinzmann-1986]: Heinzmann, G., 1986, *Poincaré, Russell, Zermelo et Peano. Textes de la discusion (1906–1912) sur les fondements des mathématiques: des antinomies à la prédicativité*, Paris: Albert Blanchard.

[^hessenberg-1906]: Hessenberg, G., 1906, “Grundbegriffe der Mengenlehre”, *Abhandlungen der neuen Fries'schen Schule (Neue Folge)* 1: 479–706.

[^hilbert-1899]: Hilbert, D., 1899, “Grundlagen der Geometrie”, in *Festschrift zur Feier der Enthüllung des Gauss-Weber-Denkmals in Göttingen*, Leipzig: B. G. Teubner. Republished as Chapter 5 in Hallett and Majer 2004.

[^hilbert-1900a]: –––, 1900a, “Mathematische Probleme”, *Nachrichten von der königlichen Gesellschaft der Wissenschaften zu Göttingen, mathematisch-physikalische Klasse*, pp. 253–296. English translation by Mary Winston Newson, 1902, “Mathematical Problems” *Bulletin of the American Mathematical Society* 8: 437–479.

[^hilbert-1900b]: –––, 1900b, “Über den Zahlbegriff”, *Jahresbericht der deutschen Mathematiker-Vereinigung* 8: 180–185. Reprinted (with small modifications) in Second to Seventh Editions of Hilbert 1899.

[^hilbert-1902]: –––, 1902, “Grundlagen der Geometrie”. Ausarbeitung by August Adler for lectures in the Sommersemester of 1902 at the Georg-August Universität, Göttingen. Library of the Mathematisches Institut. Published as Chapter 6 in Hallett and Majer 2004.

[^hilbert-1918]: –––, 1918, “Axiomatisches Denken”, *Mathematische Annalen*, 78: 405–415. Reprinted in Hilbert 1935: 146–156; English translation in Ewald 1996: volume 2, pp. 1105–1115.

[^hilbert-1920]: –––, 1920, “Probleme der mathematischen Logik”, Lecture notes for a course held in the Wintersemester of 1920 at the Georg-August Universität, Göttingen, ausgearbeitet by Moses Schönfinkel and Paul Bernays. Library of the Mathematisches Institut, Universität Göttingen. Published in Ewald et al. 2013, Chapter 2.

[^hilbert-1935]: –––, 1935, *Gesammelte Abhandlungen, Band 3*. Berlin: Julius Springer.

[^jourdain-1904]: Jourdain, P. E. B., 1904, “On the transfinite cardinal numbers of well-ordered aggregates”, *Philosophical Magazine* 7(6): 61–75.

[^jourdain-1905a]: –––, 1905a, “On a proof that every aggregate can be well-ordered”, *Mathematische Annalen* 60: 465–470.

[^jourdain-1905b]: –––, 1905b, “On transfinite numbers of the exponential form”, *Philosophical Magazine* 9(6): 42–56.

[^kanamori-1996]: Kanamori, A., 1996, “The mathematical development of set theory from Cantor to Cohen”, *Bulletin of Symbolic Logic* 2: 1–71.

[^kanamori-1997]: –––, 1997, “The mathematical import of Zermelo's well-ordering theorem”, *Bulletin of Symbolic Logic* 3: 281–311.

[^kanamori-2003]: –––, 2003, “The empty set, the singleton, and the ordered pair”, *Bulletin of Symbolic Logic* 9: 273–298.

[^kanamori-2004]: –––, 2004, “Zermelo and set theory”, *Bulletin of Symbolic Logic* 10: 487–553.

[^kanamori-2012]: –––, 2012, “In praise of replacement”, *Bulletin of Symbolic Logic*, 18: 46–90.

[^kuratowski-1921]: Kuratowski, C., 1921, “Sur la notion de l'ordre dans la théorie des ensembles”, *Fundamenta Mathematicae* 2: 161–171.

[^kuratowski-1922]: –––, 1922, “Une méthode d'élimination des nombres transfini des raisonnements mathématiques”, *Fundamenta Mathematicae* 3: 76–108.

[^mancosu-2009]: Mancosu, P., 2009, “Measuring the size of infinite collections of natural numbers: was Cantor's theory of infinite number inevitable?”, *Review of Symbolic Logic* 2: 612–646.

[^mancosu-2010]: –––, 2010, *The Adventure of Reason: Interplay Between Philosophy of Mathematics and Mathematical Logic, 1900–1940*. Oxford: Oxford University Press.

[^mancosu-2009-2]: Mancosu, P., R. Zach, and C. Badesa, 2009, “The development of mathematical logic from Russell to Tarski, 1900–1935”, in Haaparanta 2009: 318–470. Reprinted in Mancosu 2010: 5–119.

[^mirimanoff-1917a]: Mirimanoff, D., 1917a, “Les antinomies de Russell et de Burali-Forti et le problème fondamental de la théorie des ensembles”, *L'enseignement mathématique* 19: 37–52.

[^mirimanoff-1917b]: –––, 1917b, “Remarques sur la théorie des ensembles et les antinomies Cantoriennes (I)”, *L'enseignement mathématique* 19: 208–217.

[^mirimanoff-1921]: –––, 1921, “Remarques sur la théorie des ensembles et les antinomies Cantoriennes (II)”, *L'enseignement mathématique* 21: 29–52.

[^moore-1976]: Moore, G., 1976, “Ernst Zemelo, A. E. Harward, and the axiomatisation of set theory”, *Historia Mathematica* 3: 206–209.

[^moore-1982]: –––, 1982, *Zermelo's Axiom of Choice: Its Origins, Development and Influence*. Berlin: Springer.

[^peano-1906]: Peano, G., 1906, “Additione”, *Revista di mathematica* 8: 143–157. Reprinted in Heinzmann 1986: 106–120.

[^peckhaus-1990]: Peckhaus, V., 1990, *Hilbertprogramm und kritische Philosophie: das Göttinger Modell interdisziplinärer Zusammenarbeit zwischen Mathematik und Philosophie*, Volume 7 of *Studien zur Wissenschafts- Sozial- und Bildungsgeschichte*, Göttingen: Vandenhoek and Ruprecht.

[^poincaré-1905]: Poincaré, H., 1905, “Les mathématiques et la logique”, *Revue de métaphysique et de morale* 13: 815–835. Reprinted with alterations in Poincaré 1908: Part II, Chapter 3; and, with these alterations noted, in Heinzmann 1986: 11–34. English translation in Ewald 1996: 1021–1038.

[^poincaré-1906a]: –––, 1906a, “Les mathématiques et la logique”, *Revue de métaphysique et de morale* 14: 17–34. Reprinted with alterations in Poincaré 1908: Part II, Chapter 3; and, with these alterations noted, in Heinzmann 1986: 35–53. English translation in Ewald 1996: 1038–1052.

[^poincaré-1906b]: –––, 1906b, “Les mathématiques et la logique”, *Revue de métaphysique et de morale* 14: 294–317. Reprinted with alterations in Poincaré 1908: Part II, Chapter 5; and, with these alterations noted, in Heinzmann 1986: 35–53. English translation in Ewald 1996: 1052–1071.

[^poincaré-1908]: –––, 1908, *Science et méthode*, Paris: Ernst Flammarion. English translation in Poincaré 1913b, and retranslated by Francis Maitland as *Science and Method,* New York: Dover Publications.

[^poincaré-1909]: –––, 1909, “Le logique de l'infini”, *Revue de métaphysique et de morale* 17: 462–482. Reprinted in Poincaré 1913a: 7–31.

[^poincaré-1913a]: –––, 1913a, *Dernières Pensées*, Paris: Ernest Flammarion. English translation published in 1963 as *Mathematics and Science: Last Essays,* New York: Dover Publications.

[^poincaré-1913b]: –––, 1913b, *The Foundations of Science*, New York: Science Press. Preface by Poincaré and an Introduction by Josiah Royce. Contains English translation by G. B. Halsted of Poincaré 1908.

[^ramsey-1926]: Ramsey, F. P., 1926, “The foundations of mathematics”, *Proceedings of the London Mathematical Society* 25 (Second Series): 338–384. Reprinted in Ramsey 1931: 1–61, and Ramsey 1978: 152–212.

[^ramsey-1931]: –––, 1931, *The Foundations of Mathematics and Other Logical Essays*, R. B. Braithwaite (ed.), London: Routledge and Kegan Paul, London.

[^ramsey-1978]: –––, 1978, *Foundations: Essays in Philosophy, Logic, Mathematics and Economics*, D. H. Mellor (ed.), London: Routledge and Kegan Paul.

[^richard-1905]: Richard, J., 1905, “Les principes des mathématiques et le problème des ensembles”, *Révue général des sciences pures et appliqués* 16: 541. English translation in van Heijenoort 1967: 142–144.

[^russell-1902]: Russell, B., 1902, Letter to Frege. In Heijenoort 1967: 124–125.

[^russell-1903]: –––, 1903, *The Principles of Mathematics*, Volume 1, Cambridge: Cambridge University Press.

[^schoenflies-1905]: Schoenflies, A., 1905, “Über wohlgeordnete Mengen”, *Mathematische Annalen* 60: 181–186.

[^skolem-1923]: Skolem, T., 1923, “Einige Bemerkungen zur axiomatischen Begründung der Mengenlehre”, *Matimatikerkrongressen i Helsingfors den 4–7 Juli 1922, Den femte skandinaiska matematikerkongressen, redogörelse, 1923*, pp. 217–232. Reprinted in Skolem 1970: 137–152 which also preserves the original pagination. English translation in Heijenoort 1967: 290–301.

[^skolem-1970]: –––, 1970, *Selected Papers in Logic*, Oslo: Universitetsforlaget. Edited by Jens Erik Fenstad.

[^neumann-1923]: von Neumann, J., 1923, “Zur Einführung der transfiniten Zahlen”, *Acta Litterarum ac Scientiarum Regiæ Universitatis Hungaricæ Francisco-Josephinæ. Sectio Scientiæ-Mathematicæ* 1, pp. 199–208. Reprinted in von Neumann 1961: 24–33. English translation in van Heijenoort 1967: 346–354.

[^neumann-1928]: –––, 1928, “Über die Definition durch transfinite Induktion und verwandte Fragen der allgemeinen Mengenlehre”, *Mathematische Annalen* 99: 373–391. Reprinted in von Neumann 1961: 320–338.

[^neumann-1961]: –––, 1961, *John von Neumann: Collected Works*, Volume 1, Oxford: Pergamon Press.

[^weyl-1910]: Weyl, H., 1910, “Über die Definitionen der mathematischen Grundbegriffe”, *Mathematisch-naturwissenschaftliche Blätter* 7, pp. 93–95, 109–113. Reprinted in Weyl 1968, Volume 1, 298–304.

[^weyl-1968]: –––, 1968, *Gesammelte Abhandlungen*, 4 Volumes, Berlin: Springer.

[^young-1906]: Young, W. H. and G. C. Young, 1906, *The Theory of Sets of Points*, Cambridge: Cambridge University Press.

[^zermelo-1904]: Zermelo, E., 1904, “Beweis, daß jede Menge wohlgeordnet werden kann”, *Mathematische Annalen* 59: 514–516. Reprinted in Zermelo 2010: 114–119, with a facing-page English translation, and an Introduction by Michael Hallett (2010b). English translation also in van Heijenoort 1967: 139–141.

[^zermelo-1908a]: –––, 1908a, “Neuer Beweis für die Möglichkeit einer Wohlordnung”, *Mathematische Annalen* 65: 107–128. Reprinted in Zermelo 2010: 120–159, with a facing-page English translation, and an Introduction by Michael Hallett (2010b). English translation also in van Heijenoort 1967: 183–198.

[^zermelo-1908b]: –––, 1908b, “Untersuchungen über die Grundlagen der Mengenlehre, I”, *Mathematische Annalen* 65: 261–281. Reprinted in Zermelo 2010: 189–228, with a facing-page English translation, and an Introduction by Ulrich Felgner (2010). English translation also in van Heijenoort 1967: 201–215.

[^zermelo-1929]: –––, 1929, “Über den Begriff von Definitheit in der Axiomatik”, *Fundamenta Mathematicae* 14: 339–344. Reprinted with facing-page English translation in Zermelo 2010: 358–367, with an Introduction by Heinz-Dieter Ebbinghaus (2010).

[^zermelo-1930]: –––, 1930, “Über Grenzzahlen und Mengenbereiche: Neue Untersuchungen über die Grundlagen der Mengenlehre”, *Fundamenta Mathematicae* 16: 29–47. Reprinted with facing-page English translation in Zermelo 2010: 400–431, with an Introduction by Akihiro Kanamori. English translation also in Ewald 1996, Volume 2, pp. 1219–1233.

[^zermelo-2010]: –––, 2010, *Collected Works. Volume I: Set Theory, Miscellanea*, H.-D. Ebbinghaus and A. Kanamori (eds.), Berlin: Springer.
