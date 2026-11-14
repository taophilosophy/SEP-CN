# The Continuum Hypothesis
**First published Wed May 22, 2013**

*Koellner, Peter*

The continuum hypothesis (CH) is one of the most central open problems in set theory, one that is important for both mathematical and philosophical reasons.

The problem actually arose with the birth of set theory; indeed, in many respects it stimulated the birth of set theory. In 1874 Cantor had shown that there is a one-to-one correspondence between the natural numbers and the algebraic numbers. More surprisingly, he showed that there is no one-to-one correspondence between the natural numbers and the real numbers. Taking the existence of a one-to-one correspondence as a criterion for when two sets have the same size (something he certainly did by 1878), this result shows that there is more than one level of infinity and thus gave birth to the higher infinite in mathematics. Cantor immediately tried to determine whether there were any infinite sets of real numbers that were of *intermediate* size, that is, whether there was an infinite set of real numbers that could not be put into one-to-one correspondence with the natural numbers and could not be put into one-to-one correspondence with the real numbers. The *continuum hypothesis* (under one formulation) is simply the statement that there is no such set of real numbers. It was through his attempt to prove this hypothesis that led Cantor do develop set theory into a sophisticated branch of mathematics.[^note-1]

Despite his efforts Cantor could not resolve CH. The problem persisted and was considered so important by Hilbert that he placed it first on his famous list of open problems to be faced by the 20ᵗʰ century. Hilbert also struggled to resolve CH, again without success. Ultimately, this lack of progress was explained by the combined results of Gödel and Cohen, which together showed that CH *cannot* be resolved on the basis of the axioms that mathematicians were employing; in modern terms, CH is independent of Zermelo-Fraenkel set theory extended with the Axiom of Choice (ZFC).

This independence result was quickly followed by many others. The independence techniques were so powerful that set theorists soon found themselves preoccupied with the meta-theoretic enterprise of proving that certain fundamental statements could *not* be proved or refuted within ZFC. The question then arose as to whether there were ways to settle the independent statements. The community of mathematicians and philosophers of mathematics was largely divided on this question. The *pluralists* (like Cohen) maintained that the independence results effectively settled the question by showing that it *had no answer*. On this view, one could adopt a system in which, say CH was an axiom and one could adopt a system in which ¬CH was an axiom and that was the end of the matter—there was no question as to which of two incompatible extensions was the “correct” one. The *non-pluralists* (like Gödel) held that the independence results merely indicated the paucity of our means for circumscribing mathematical truth. On this view, what was needed were new axioms, axioms that are both justified and sufficient for the task. Gödel actually went further in proposing candidates for new axioms—large cardinal axioms—and he conjectured that they would settle CH.

Gödel's program for large cardinal axioms proved to be remarkably successful. Over the course of the next 30 years it was shown that large cardinal axioms settle many of the questions that were shown to be independent during the era of independence. However, CH was left untouched. The situation turned out to be rather ironic since in the end it was shown (in a sense that can be made precise) that although the standard large cardinal axioms effectively settle all question of complexity strictly below that of CH, they cannot (by results of Levy and Solovay and others) settle CH itself. Thus, in choosing CH as a test case for his program, Gödel put his finger precisely on the point where it fails. It is for this reason that CH continues to play a central role in the search for new axioms.

In this entry we shall give an overview of the major approaches to settling CH and we shall discuss some of the major foundational frameworks which maintain that CH does not have an answer. The subject is a large one and we have had to sacrifice full comprehensiveness in two dimensions. First, we have not been able to discuss the major philosophical issues that are lying in the background. For this the reader is directed to the entry “Large Cardinals and Determinacy”, which contains a general discussion of the independence results, the nature of axioms, the nature of justification, and the successes of large cardinal axioms in the realm “below CH”. Second, we have not been able to discuss every approach to CH that is in the literature. Instead we have restricted ourselves to those approaches that appear most promising from a philosophical point of view and where the mathematics has been developed to a sufficiently advanced state. In the approaches we shall discuss—forcing axioms, inner model theory, quasi-large cardinals—the mathematics has been pressed to a very advanced stage over the course of 40 years. And this has made our task somewhat difficult. We have tried to keep the discussion as accessible as possible and we have placed the more technical items in the endnotes. But the reader should bear in mind that we are presenting a bird's eye view and that for a higher resolution at any point the reader should dip into the suggested readings that appear at the end of each section.[^note-2]

There are really two kinds of approaches to new axioms—the *local* approach and the *global* approach. On the local approach one seeks axioms that answer questions concerning a specifiable fragment of the universe, such as *V*_{ω+1} or *V*_{ω+2}, where CH lies. On the global approach one seeks axioms that attempt to illuminate the *entire* structure of the universe of sets. The global approach is clearly much more challenging. In this entry we shall start with the local approach and toward the end we shall briefly touch upon the global approach.

Here is an overview of the entry: Section 1 surveys the independence results in cardinal arithmetic, covering both the case of regular cardinals (where CH lies) and singular cardinals. Section 2 considers approaches to CH where one successively verifies a hierarchy of approximations to CH, each of which is an “effective” version of CH. This approach led to the remarkable discovery of Woodin that it is possible (in the presence of large cardinals) to have an effective failure of CH, thereby showing, that the effective failure of CH is as intractable (with respect to large cardinal axioms) as CH itself. Section 3 continues with the developments that stemmed from this discovery. The centerpiece of the discussion is the discovery of a “canonical” model in which CH fails. This formed the basis of a network of results that was collectively presented by Woodin as a case for the failure of CH. To present this case in the most streamlined form we introduce the strong logic Ω-logic. Section 4 takes up the competing foundational view that there is no solution to CH. This view is sharpened in terms of the *generic multiverse conception of truth* and that view is then scrutinized. Section 5 continues the assessment of the case for ¬CH by investigating a parallel case for CH. In the remaining two sections we turn to the global approach to new axioms and here we shall be much briefer. Section 6 discusses the approach through inner model theory. Section 7 discusses the approach through quasi-large cardinal axioms.

## 1. Independence in Cardinal Arithmetic

In this section we shall discuss the independence results in cardinal arithmetic. First, we shall treat of the case of regular cardinals, where CH lies and where very little is determined in the context of ZFC. Second, for the sake of comprehensiveness, we shall discuss the case of singular cardinals, where much more can be established in the context of ZFC.

### 1.1 Regular Cardinals

The addition and multiplication of infinite cardinal numbers is trivial: For infinite cardinals κ and λ,

> κ + λ = κ ⋅ λ = max{κ,λ}.

The situation becomes interesting when one turns to exponentiation and the attempt to compute κ^{λ} for infinite cardinals.

During the dawn of set theory Cantor showed that for every cardinal κ,

> 2^{κ} > κ.

There is no mystery about the size of 2^{*n*} for finite *n*. The first natural question then is where 2^{ℵ₀} is located in the aleph-hierarchy: Is it ℵ₁, ℵ₂, …, ℵ₁₇ or something much larger?

The cardinal 2^{ℵ₀} is important since it is the size of the continuum (the set of real numbers). Cantor's famous *continuum hypothesis* (CH) is the statement that 2^{ℵ_{0}} = ℵ₁. This is a special case of the *generalized continuum hypothesis* (GCH) which asserts that for all α, 2^{ℵ_{α}} = ℵ_{α+1}. One virtue of GCH is that it gives a complete solution to the problem of computing κ^{λ} for infinite cardinals: Assuming GCH, if κ ≤ λ then κ^{λ} = λ⁺; if cf(κ) ≤ λ ≤ κ then κ^{λ} = κ⁺; and if λ < cf(κ) then κ^{λ} = κ.

Very little progress was made on CH and GCH. In fact, in the early era of set theory the only other piece of progress beyond Cantor's result that 2^{κ} > κ (and the trivial result that if κ ≤ λ then 2^{κ} ≤ 2^{λ}) was König's result that cf(2^{κ}) > κ. The explanation for the lack of progress was provided by the independence results in set theory:

**Theorem 1.1** (Gödel 1938a, 1938b)[^gödel-1938a][^gödel-1938b].

*Assume that* ZFC *is consistent. Then* ZFC + CH *and* ZFC + GCH *are consistent.*

To prove this Gödel invented the method of *inner models* —he showed that CH and GCH held in the minimal inner model *L* of ZFC. Cohen then complemented this result:

**Theorem 1.2** (Cohen 1963)[^cohen-1963].

*Assume that* ZFC *is consistent. Then* ZFC + ¬CH *and* ZFC + ¬GCH *are consistent.*

He did this by inventing the method of *outer models* and showing that CH failed in a *generic extension* *V*^{*B*} of *V*. The combined results of Gödel and Cohen thus demonstrate that assuming the consistency of ZFC, it is in principle impossible to settle either CH or GCH in ZFC.

In the Fall of 1963 Easton completed the picture by showing that for infinite regular cardinals κ the *only* constraints on the function κ ↦ 2^{κ} that are provable in ZFC are the trivial constraint and the results of Cantor and König:

**Theorem 1.3** (Easton 1963).

*Assume that* ZFC *is consistent. Suppose* *F* *is a* (*definable class*) *function defined on infinite regular cardinals such that* *if* κ ≤ λ *then* *F*(κ) ≤ *F*(λ)*,* *F*(κ) > κ*, and* cf(*F*(κ)) > κ*.*

*Then* ZFC + “*For all infinite regular cardinals* κ, 2^{κ} = *F*(κ)” *is consistent.*

Thus, set theorists had pushed the cardinal arithmetic of regular cardinals as far as it could be pushed within the confines of ZFC.

### 1.2 Singular Cardinals

The case of cardinal arithmetic on singular cardinals is much more subtle. For the sake of completeness we pause to briefly discuss this before proceeding with the continuum hypothesis.

It was generally believed that, as in the case for regular cardinals, the behaviour of the function κ ↦ 2^{κ} would be relatively unconstrained within the setting of ZFC. But then Silver proved the following remarkable result:[^note-3]

**Theorem 1.4** (Silver 1974).

*If* ℵ_{δ} *is a singular cardinal of uncountable cofinality, then, if* GCH *holds below* ℵ_{δ}*, then* GCH *holds at* ℵ_{δ}*.*

It turns out that (by a deep result of Magidor, published in 1977) GCH can first fail at ℵ_{ω} (assuming the consistency of a supercompact cardinal). Silver's theorem shows that it cannot first fail at ℵ_{ω1} and *this is provable in* ZFC.

This raises the question of whether one can “control” the size of 2^{ℵ_{δ}} with a weaker assumption than that ℵ_{δ} is a singular cardinal of uncountable cofinality such that GCH holds below ℵ_{δ}. The natural hypothesis to consider is that ℵ_{δ} is a singular cardinal of uncountable cofinality which is *a strong limit cardinal*, that is, that for all α < ℵ_{δ}, 2^{α} < ℵ_{δ}. In 1975 Galvin and Hajnal proved (among other things) that under this weaker assumption there is indeed a bound:

**Theorem 1.5** (Galvin and Hajnal 1975).

*If* ℵ_{δ} *is a singular strong limit cardinal of uncountable cofinality then* 2^{ℵ_{δ}} < ℵ_{(|δ|^{cf(δ)})⁺}.

It is possible that there is a jump—in fact, Woodin showed (again assuming large cardinals) that it is possible that for all κ, 2^{κ} = κ⁺⁺. What the above theorem shows is that in ZFC there is a provable bound on how big the jump can be.

The next question is whether a similar situation prevails with singular cardinals of countable cofinality. In 1978 Shelah showed that this is indeed the case. To fix ideas let us concentrate on ℵ_{ω}.

**Theorem 1.6** (Shelah 1978).

*If* ℵ_{ω} *is a strong limit cardinal then* 2^{ℵ_{ω}} < ℵ_{(2^{ℵ0}})⁺.

One drawback of this result is that the bound is sensitive to the actual size of 2^{ℵ₀}, which can be anything below ℵ_{ω}. Remarkably Shelah was later able to remedy this with the development of his pcf (possible cofinalities) theory. One very quotable result from this theory is the following:

**Theorem 1.7** (Shelah 1982).

*If* ℵ_{ω} *is a strong limit cardinal then* (*regardless of the size of* 2^{ℵ₀}) 2^{ℵ_{ω}} < ℵ_{ω4}.

In summary, although the continuum function at regular cardinals is relatively unconstrained in ZFC, the continuum function at singular cardinals is (provably in ZFC) constrained in significant ways by the behaviour of the continuum function on the smaller cardinals.

*Further Reading*: For more cardinal arithmetic see Jech (2003)[^jech-2003]. For more on the case of singular cardinals and pcf theory see Abraham & Magidor (2010) and Holz, Steffens & Weitz (1999).

## 2. Definable Versions of the Continuum Hypothesis and its Negation

Let us return to the continuum function on regular cardinals and concentrate on the simplest case, the size of 2^{ℵ₀}. One of Cantor's original approaches to CH was by investigating “simple” sets of real numbers (see Hallett (1984)[^hallett-1984], pp. 3–5 and §2.3(b)). One of the first results in this direction is the Cantor-Bendixson theorem that every infinite closed set is either countable or contains a perfect subset, in which case it has the same cardinality as the set of reals. In other words, CH holds (in this formulation) when one restricts one's attention to closed sets of reals. In general, questions about “definable” sets of reals are more tractable than questions about arbitrary sets of reals and this suggests looking at definable versions of the continuum hypothesis.

### 2.1 Three Versions

There are three different formulations of the continuum hypothesis—the *interpolant* version, the *well-ordering* version, and the *surjection* version. These versions are all equivalent to one another in ZFC but we shall be imposing a definability constraint and in this case there can be interesting differences (our discussion follows Martin (1976)[^martin-1976]). There is really a hierarchy of notions of definability—ranging up through the Borel hierarchy, the projective hierarchy, the hierarchy in *L*(ℝ), and, more generally, the hierarchy of universally Baire sets—and so each of these three general versions is really a hierarchy of versions, each corresponding to a given level of the hierarchy of definability (for a discussion of the hierarchy of definability see §2.2.1 and §4.6 of the entry “Large Cardinals and Determinacy”).

#### 2.1.1 Interpolant Version

The first formulation of CH is that there is no *interpolant*, that is, there is no infinite set *A* of real numbers such that the cardinality of *A* is strictly between that of the natural numbers and the real numbers. To obtain definable versions one simply asserts that there is no “definable” interpolant and this leads to a hierarchy of definable interpolant versions, depending on which notion of definability one employs. More precisely, for a given pointclass Γ in the hierarchy of definable sets of reals, the corresponding definable interpolant version of CH asserts that there is no interpolant in Γ.

The Cantor-Bendixson theorem shows that there is no interpolant in Γ in the case where Γ is the pointclass of closed sets, thus verifying this version of CH. This was improved by Suslin who showed that this version of CH holds for Γ where Γ is the class of Σ̰11 sets. One cannot go much further within ZFC—to prove stronger versions one must bring in stronger assumptions. It turns out that axioms of definable determinacy and large cardinal axioms achieve this. For example, results of Kechris and Martin show that if Δ̰1*n*-determinacy holds then this version of CH holds for the pointclass of Σ̰1n+1 sets. Going further, if one assumes AD^{*L*(ℝ)} then this version of CH holds for all sets of real numbers appearing in *L*(ℝ). Since these hypotheses follow from large cardinal axioms one also has that stronger and stronger large cardinal assumptions secure stronger and stronger versions of this version of the effective continuum hypothesis. Indeed large cardinal axioms imply that this version of CH holds for *all* sets of reals in the definability hierarchy we are considering; more precisely, if there is a proper class of Woodin cardinals then this version of CH holds for all universally Baire sets of reals.

#### 2.1.2 Well-ordering Version

The second formulation of CH asserts that every well-ordering of the reals has order type less than ℵ₂. For a given pointclass Γ in the hierarchy, the corresponding definable well-ordering version of CH asserts that every well-ordering (coded by a set) in Γ has order type less than ℵ₂.

Again, axioms of definable determinacy and large cardinal axioms imply this version of CH for richer notions of definability. For example, if AD^{*L*(ℝ)} holds then this version of CH holds for all sets of real numbers in *L*(ℝ). And if there is a proper class of Woodin cardinals then this version of CH holds for all universally Baire sets of reals.

#### 2.1.3 Surjection Version

The third version formulation of CH asserts that there is no surjection ρ : ℝ → ℵ₂, or, equivalently, that there is no prewellordering of ℝ of length ℵ₂. For a given pointclass Γ in the hierarchy of definability, the corresponding surjection version of CH asserts that there is no surjection ρ : ℝ → ℵ₂ such that (the code for) ρ is in Γ.

Here the situation is more interesting. Axioms of definable determinacy and large cardinal axioms have bearing on this version since they place bounds on how long definable prewellorderings can be. Let δ̰1*n* be the supremum of the lengths of the Σ̰1*n*-prewellorderings of reals and let Θ^{*L*(ℝ)} be the supremum of the lengths of prewellorderings of reals where the prewellordering is definable in the sense of being in *L*(ℝ). It is a classical result that δ̰11 = ℵ₁. Martin showed that δ̰12 ≤ ℵ₂ and that if there is a measurable cardinal then δ̰13 ≤ ℵ₃. Kunen and Martin also showed under PD, δ̰14 ≤ ℵ₄ and Jackson showed that under PD, for each n < ω, δ̰1*n* < ℵ_{ω}. Thus, assuming that there are infinitely many Woodin cardinals, these bounds hold. Moreover, the bounds continue to hold regardless of the size of 2^{ℵ₀}. Of course, the question is whether these bounds can be improved to show that the prewellorderings are shorter than ℵ₂. In 1986 Foreman and Magidor initiated a program to establish this. In the most general form they aimed to show that large cardinal axioms implied that this version of CH held for all universally Baire sets of reals.

#### 2.1.4 Potential Bearing on CH

Notice that in the context of ZFC, these three hierarchies of versions of CH are all successive approximations of CH and in the limit case, where Γ is the pointclass of all sets of reals, they are equivalent to CH. The question is whether these approximations can provide any insight into CH itself.

There is an asymmetry that was pointed out by Martin, namely, that a definable counterexample to CH is a real counterexample, while no matter how far one proceeds in verifying definable versions of CH at no stage will one have touched CH itself. In other words, the definability approach could refute CH but it could not prove it.

Still, one might argue that although the definability approach could not prove CH it might provide some evidence for it. In the case of the first two versions we now know that CH holds for all definable sets. Does this provide evidence of CH? Martin pointed out (before the full results were known) that this is highly doubtful since in each case one is dealing with sets that are atypical. For example, in the first version, at each stage one secures the definable version of CH by showing that all sets in the definability class have the perfect set property; yet such sets are atypical in that assuming AC it is easy to show that there are sets without this property. In the second version, at each stage one actually shows not only that each well-ordering of reals in the definability class has ordertype less than ℵ₂, but also that it has ordertype less than ℵ₁. So neither of these versions really illuminates CH.

The third version actually has an advantage in this regard since not all of the sets it deals with are atypical. For example, while all Σ̰11-sets have length less than ℵ₁, there are Π̰11-sets of length ℵ₁. Of course, it could turn out that even if the Foreman-Magidor program were to succeed the sets could turn out to be atypical in another sense, in which case it would shed little light on CH. More interesting, however, is the possibility that in contrast to the first two versions, it would actually provide an actual counterexample to CH. This, of course, would require the failure of the Foreman-Magidor program.

### 2.2 The Foreman-Magidor Program

The goal of the Foreman-Magidor program was to show that large cardinal axioms also implied that the third version of CH held for all sets in *L*(ℝ) and, more generally, all universally Baire sets. In other words, the goal was to show that large cardinal axioms implied that Θ^{*L*(ℝ)} ≤ ℵ₂ and, more generally, that Θ^{*L*(A,ℝ)} ≤ ℵ₂ for each universally Baire set *A*.

The motivation came from the celebrated results of Foreman, Magidor and Shelah on Martin's Maximum (MM), which showed that assuming large cardinal axioms one can always force to obtain a precipitous ideal on ℵ₂ without collapsing ℵ₂ (see Foreman, Magidor & Shelah (1988)). The program involved a two-part strategy:

1. Strengthen this result to show that assuming large cardinal axioms one can always force to obtain a *saturated* ideal on ℵ₂ without collapsing ℵ₂.
2. Show that the existence of such a saturated ideal implies that Θ^{*L*(ℝ)} ≤ ℵ₂ and, more generally that Θ^{*L*(A,ℝ)} ≤ ℵ₂ for every universally Baire set *A*.

This would show that show that Θ^{*L*(ℝ)} ≤ ℵ₂ and, more generally that Θ^{*L*(A,ℝ)} ≤ ℵ₂ for every universally Baire set *A*.[^note-4]

In December 1991, the following result dashed the hopes of this program.

**Theorem 2.1** (Woodin).

*Assume that the non-stationary ideal on* ℵ₁ *is saturated and that there is a measurable cardinal. Then* δ̰12 = ℵ₂*.*

The point is that the hypothesis of this theorem can always be forced assuming large cardinals. Thus, it is possible to have Θ^{*L*(ℝ)} > ℵ₂ (in fact, δ̰13 > ℵ₂).

Where did the program go wrong? Foreman and Magidor had an approximation to (B) and in the end it turned out that (B) is true.

**Theorem 2.2** (Woodin).

*Assume that there is a proper class of Woodin cardinals and that there is a saturated ideal on* ℵ₂*. Then for every* A ∈ Γ^{∞}*,* Θ^{*L*(A,ℝ)} ≤ ℵ₂*.*

So the trouble is with (A).

This illustrates an interesting contrast between our three versions of the effective continuum hypothesis, namely, that they can come apart. For while large cardinals rule out definable counterexamples of the first two kinds, they cannot rule out definable counterexamples of the third kind. But again we must stress that they cannot prove that there *are* such counterexamples.

But there is an important point: Assuming large cardinal axioms (AD^{*L*(ℝ)} suffices), although one can produce outer models in which δ̰13 > ℵ₂ it is not currently known how to produce outer models in which δ̰13 > ℵ₃ or even Θ^{*L*(ℝ)} > ℵ₃. Thus it is an open possibility that from ZFC +AD^{*L*(ℝ)} one can prove Θ^{*L*(ℝ)} ≤ ℵ₃. Were this to be the case, it would follow that although large cardinals cannot rule out the definable failure of CH *they can rule out the definable failure of* 2^{ℵ₀} = ℵ₂. This could provide some insight into the size of the continuum, underscoring the centrality of ℵ₂.

*Further Reading*: For more on the three effective versions of CH see Martin (1976)[^martin-1976]; for more on the Foreman-Magidor program see Foreman & Magidor (1995) and the introduction to Woodin (1999)[^woodin-1999].

## 3. The Case for ¬CH

The above results led Woodin to the identification of a “canonical” model in which CH fails and this formed the basis of his an argument that CH is false. In Section 3.1 we will describe the model and in the remainder of the section we will present the case for the failure of CH. In Section 3.2 we will introduce Ω-logic and the other notions needed to make the case. In Section 3.3 we will present the case.

### 3.1 ℙ_{*max*}

The goal is to find a model in which CH is false and which is canonical in the sense that its theory cannot be altered by set forcing in the presence of large cardinals. The background motivation is this: First, we know that in the presence of large cardinal axioms the theory of second-order arithmetic and even the entire theory of *L*(ℝ) is invariant under set forcing. The importance of this is that it demonstrates that our main independence techniques cannot be used to establish the independence of questions about second-order arithmetic (or about *L*(ℝ)) in the presence of large cardinals. Second, experience has shown that the large cardinal axioms in question seem to answer all of the major known open problems about second-order arithmetic and *L*(ℝ) and the set forcing invariance theorems give precise content to the claim that these axioms are “effectively complete”.[^note-5]

It follows that if ℙ is any homogeneous partial order in *L*(ℝ) then the generic extension *L*(ℝ)^{ℙ} inherits the generic absoluteness of *L*(ℝ). Woodin discovered that there is a very special partial order ℙ_{*max*} that has this feature. Moreover, the model *L*(ℝ)^{ℙ_{*max*}} satisfies ZFC + ¬CH. The key feature of this model is that it is “maximal” (or “saturated”) with respect to sentences that are of a certain complexity and which can be shown to be consistent via set forcing over the model; in other words, if these sentences *can hold* (by set forcing over the model) then they *do hold* in the model. To state this more precisely we are going to have to introduce a few rather technical notions.

There are two ways of stratifying the universe of sets. The first is in terms of ⟨*V*_{α} | α ∈ On ⟩, the second is in terms of ⟨*H*(κ) | κ ∈ Card⟩, where *H*(κ) is the set of all sets which have cardinality less than κ and whose members have cardinality less than κ, and whose members of members have cardinality less than κ, and so on. For example, *H*(ω) = *V*_{ω} and the theories of the structures *H*(ω₁) and *V*_{ω+1} are mutually interpretable. This latter structure is the structure of second-order arithmetic and, as mentioned above, large cardinal axioms give us an “effectively complete” understanding of this structure. We should like to be in the same position with regard to larger and larger fragments of the universe and the question is whether we should proceed in terms of the first or the second stratification.

The second stratification is potentially more fine-grained. Assuming CH one has that the theories of *H*(ω₂) and *V*_{ω+2} are mutually interpretable and assuming larger and larger fragments of GCH this correspondence continues upward. But if CH is false then the structure *H*(ω₂) is less rich than the structure *V*_{ω2}. In this event the latter structure captures full third-order arithmetic, while the former captures only a small fragment of third-order arithmetic but is nevertheless rich enough to express CH. Given this, in attempting to understand the universe of sets by working up through it level by level, it is sensible to use the potentially more fine-grained stratification.

Our next step is therefore to understand *H*(ω₂). It actually turns out that we will be able to understand slightly more and this is somewhat technical. We will be concerned with the structure ⟨*H*(ω₂), ∈, *I*_{NS}, *A*^{*G*}⟩ ⊧ φ, where *I*_{NS} is the non-stationary ideal on ω₁ and *A*^{*G*} is the interpretation of (the canonical representation of) a set of reals *A* in *L*(ℝ). The details will not be important and the reader is asked to just think of *H*(ω₂) along with some “extra stuff” and not worry about the details concerning the extra stuff.[^note-6]

We are now in a position to state the main result:

**Theorem 3.1** (Woodin 1999)[^woodin-1999].

*Assume* ZFC *and that there is a proper class of Woodin cardinals. Suppose that* *A* ∈ *P* (ℝ) ∩ *L*(ℝ) *and* φ *is a* Π₂*-sentence* (*in the extended language with two additional predicates* ) *and there is a set forcing extension* *V*[*G*] *such that* ⟨*H*(ω₂), ∈, *I*_{NS}, *A*^{*G*}⟩ ⊧ φ

(*where* *A*^{*G*} *is the interpretation of* *A* *in* *V* [*G*])*. Then* *L*(ℝ)^{ℙ_{*max*}} ⊧ “⟨*H*(ω₂), ∈, *I*_{NS}, A⟩ ⊧ φ”.

There are two key points: First, the theory of *L*(ℝ)^{ℙ_{*max*}} is “effectively complete” in the sense that it is invariant under set forcing. Second, the model *L*(ℝ)^{ℙ_{*max*}} is “maximal” (or “saturated”) in the sense that it satisfies all Π₂-sentences (about the relevant structure) that can possibly hold (in the sense that they can be shown to be consistent by set forcing over the model).

One would like to get a handle on the theory of this structure by axiomatizing it. The relevant axiom is the following:

**Definition 3.2** (Woodin 1999)[^woodin-1999].

Axiom (∗): AD^{*L*(ℝ)} holds and *L*(P(ω₁)) is a ℙ_{*max*}-generic extension of *L*(ℝ).

Finally, this axiom settles CH:

**Theorem 3.3** (Woodin 1999)[^woodin-1999].

*Assume* (∗)*. Then* 2^{ω} = ℵ₂*.*

### 3.2 Ω-Logic

We will now recast the above results in terms of a strong logic. We shall make full use of large cardinal axioms and in this setting we are interested in logics that are “well-behaved” in the sense that the question of what implies what is not radically independent. For example, it is well known that CH is expressible in full second-order logic. It follows that in the presence of large cardinals one can always use set forcing to flip the truth-value of a purported logical validity of full second-order logic. However, there are strong logics—like ω-logic and β-logic—that do not have this feature—they are well-behaved in the sense that in the presence of large cardinal axioms the question of what implies what cannot be altered by set forcing. We shall introduce a very strong logic that has this feature—Ω-logic. In fact, the logic we shall introduce can be characterized as the *strongest* logic with this feature (see Koellner (2010)[^koellner-2010] for further discussion of strong logics and for a precise statement of this result).

#### 3.2.1 Ω-logic

**Definition 3.4.**

Suppose that *T* is a countable theory in the language of set theory and φ is a sentence. Then

T ⊧_{Ω} φ

if for all complete Boolean algebras *B* and for all ordinals α,

if *V**B*α ⊧ T then *V**B*α ⊧ φ.

We say that a statement φ is Ω-*satisfiable* if there exists an ordinal α and a complete Boolean algebra *B* such that *V**B*α ⊧ φ, and we say that φ is Ω-*valid* if ∅ ⊧_{Ω} φ. So, the above theorem says that (under our background assumptions), the statement “φ is Ω-satisfiable” is generically invariant and in terms of Ω-validity this is simply the following:

**Theorem 3.5** (Woodin 1999)[^woodin-1999].

*Assume* ZFC *and that there is a proper class of Woodin cardinals. Suppose that* *T* *is a countable theory in the language of set theory and* φ *is a sentence. Then for all complete Boolean algebras* *B**,*

T ⊧_{Ω} φ iff *V*^{*B*} ⊧ “T ⊧_{Ω} φ.”

Thus this logic is robust in that the question of what implies what is invariant under set forcing.

#### 3.2.2 The Ω Conjecture

Corresponding to the semantic relation ⊧_{Ω} there is a quasi-syntactic proof relation ⊢_{Ω}. The “proofs” are certain robust sets of reals (universally Baire sets of reals) and the test structures are models that are “closed” under these proofs. The precise notions of “closure” and “proof” are somewhat technical and so we will pass over them in silence.[^note-7]

Like the semantic relation, this quasi-syntactic proof relation is robust under large cardinal assumptions:

**Theorem 3.6** (Woodin 1999)[^woodin-1999].

*Assume* ZFC *and that there is a proper class of Woodin cardinals. Suppose* *T* *is a countable theory in the language of set theory,* φ *is a sentence, and* *B* *is a complete Boolean algebra. Then*

T ⊢_{Ω} φ iff *V*^{*B*} ⊧ ‘T ⊢_{Ω} φ’.

Thus, we have a semantic consequence relation and a quasi-syntactic proof relation, both of which are robust under the assumption of large cardinal axioms. It is natural to ask whether the soundness and completeness theorems hold for these relations. The soundness theorem is known to hold:

**Theorem 3.7** (Woodin 1999)[^woodin-1999].

*Assume* ZFC*. Suppose* *T* *is a countable theory in the language of set theory and* φ *is a sentence. If* T ⊢_{Ω} φ *then* T ⊧_{Ω} φ*.*

It is open whether the corresponding completeness theorem holds. The Ω Conjecture is simply the assertion that it does:

**Conjecture 3.8** (Ω **Conjecture** ).

Assume ZFC and that there is a proper class of Woodin cardinals. Then for each sentence φ,

∅ ⊧_{Ω} φ iff ∅ ⊢_{Ω} φ.

We will need a strong form of this conjecture which we shall call the Strong Ω Conjecture. It is somewhat technical and so we will pass over it in silence.[^note-8]

#### 3.2.3 Ω-Complete Theories

Recall that one key virtue of large cardinal axioms is that they “effectively settle” the theory of second-order arithmetic (and, in fact, the theory of *L*(ℝ) and more) in the sense that in the presence of large cardinals one cannot use the method of set forcing to establish independence with respect to statements about *L*(ℝ). This notion of invariance under set forcing played a key role in Section 3.1. We can now rephrase this notion in terms of Ω-logic.

**Definition 3.9.**

A theory *T* is Ω-*complete* for a collection of sentences Γ if for each φ ∈ Γ, T ⊧_{Ω} φ or T ⊧_{Ω} ¬φ.

The invariance of the theory of *L*(ℝ) under set forcing can now be rephrased as follows:

**Theorem 3.10** (Woodin 1999)[^woodin-1999].

*Assume* ZFC *and that there is a proper class of Woodin cardinals. Then* ZFC *is* Ω*-complete for the collection of sentences of the form* “*L*(ℝ) ⊧ φ”*.*

Unfortunately, it follows from a series of results originating with work of Levy and Solovay that traditional large cardinal axioms do not yield Ω-complete theories at the level of Σ21 since one can always use a “small” (and hence large cardinal preserving) forcing to alter the truth-value of CH.

**Theorem 3.11.**

*Assume* *L* *is a standard large cardinal axiom. Then* ZFC + L *is not* Ω*-complete for* Σ21*.*

### 3.3 The Case

Nevertheless, if one supplements large cardinal axioms then Ω-complete theories are forthcoming. This is the centerpiece of the case against CH.

**Theorem 3.12** (Woodin).

*Assume that there is a proper class of Woodin cardinals and that the Strong* Ω *Conjecture holds.*

*There is an axiom* *A* *such that* ZFC + *A* *is* Ω*-satisfiable and* ZFC + *A* *is* Ω*-complete for the structure* *H*(ω₂)*.* *Any such axiom* *A* *has the feature that* ZFC + *A* ⊧_{Ω} ‘*H*(ω₂) ⊧ ¬CH’.

Let us rephrase this as follows: For each *A* satisfying (1), let

> *T*_{*A*} = {φ | ZFC + *A* ⊧_{Ω} ‘*H*(ω₂) ⊧ ¬φ’}.

The theorem says that if there is a proper class of Woodin cardinals and the Ω Conjecture holds, then there are (non-trivial) Ω-complete theories *T*_{*A*} of *H*(ω₂) and all such theories contain ¬CH.

It is natural to ask whether there is greater agreement among the Ω-complete theories *T*_{*A*}. Ideally, there would be just one. A recent result (building on Theorem 5.5) shows that if there is one such theory then there are many such theories.

**Theorem 3.13** (Koellner and Woodin 2009)[^koellner-2009].

*Assume that there is a proper class of Woodin cardinals. Suppose that* *A* *is an axiom such that*

i.  ZFC + *A* *is* Ω*-satisfiable and* ii.  ZFC + *A* *is* Ω*-complete for the structure* *H*(ω₂)*.*

*Then there is an axiom* *B* *such that*

i′.  ZFC + *B* *is* Ω*-satisfiable and* ii′.  ZFC + *B* *is* Ω*-complete for the structure* *H*(ω₂)

*and* *T*_{*A*}≠*T*_{*B*}*.*

How then shall one select from among these theories? Woodin's work in this area goes a good deal beyond Theorem 5.1. In addition to isolating an axiom that satisfies (1) of Theorem 5.1 (assuming Ω-satisfiability), he isolates a very special such axiom, namely, the axiom (∗) (“star”) mentioned earlier.

This axiom can be phrased in terms of (the provability notion of) Ω-logic:

**Theorem 3.14** (Woodin).

*Assume* ZFC *and that there is a proper class of Woodin cardinals. Then the following are equivalent*:

(∗)*.* *For each* Π₂*-sentence* φ *in the language for the structure* ⟨*H*(ω₂), ∈, *I*_{NS}, *A* | *A* ∈ 𝒫 (ℝ) ∩ *L*(ℝ)⟩ *if* ZFC + “⟨*H*(ω₂), ∈, *I*_{NS}, *A* | *A* ∈ 𝒫 (ℝ) ∩ *L*(ℝ)⟩ ⊧ φ” *is* Ω*-consistent, then* ⟨*H*(ω₂), ∈, *I*_{NS}, *A* | *A* ∈ 𝒫 (ℝ) ∩ *L*(ℝ)⟩ ⊧ φ.

It follows that of the various theories *T*_{*A*} involved in Theorem 5.1, there is one that stands out: The theory *T*_{(∗)} given by (∗). This theory maximizes the Π₂-theory of the structure ⟨*H*(ω₂), ∈, *I*_{NS}, *A* | *A* ∈ 𝒫 (ℝ) ∩ *L*(ℝ)⟩.

The continuum hypothesis fails in this theory. Moreover, in the maximal theory *T*_{(∗)} given by (∗) the size of the continuum is ℵ₂.[^note-9]

To summarize: Assuming the Strong Ω Conjecture, there is a “good” theory of *H*(ω₂) and all such theories imply that CH fails. Moreover, (again, assuming the Strong Ω Conjecture) there is a maximal such theory and in that theory 2^{ℵ₀} = ℵ₂.

*Further Reading*: For the mathematics concerning ℙ_{*max*} see Woodin (1999)[^woodin-1999]. For an introduction to Ω-logic see Bagaria, Castells & Larson (2006). For more on incompatible Ω-complete theories see Koellner & Woodin (2009). For more on the case against CH see Woodin (2001a,b, 2005a,b).

## 4. The Multiverse

The above case for the failure of CH is the strongest known local case for axioms that settle CH. In this section and the next we will switch sides and consider the pluralist arguments to the effect that CH does not have an answer (in this section) and to the effect that there is an equally good case for CH (in the next section). In the final two section we will investigate optimistic global scenarios that provide hope of settling the issue.

The pluralist maintains that the independence results effectively settle the undecided questions by showing that they have no answer. One way of providing a foundational framework for such a view is in terms of the multiverse. On this view there is not a single *universe* of set theory but rather a *multiverse* of legitimate candidates, some of which may be preferable to others for certain purposes but none of which can be said to be the “true” universe. The *multiverse conception of truth* is the view that a statement of set theory can only be said to be true simpliciter if it is true in all universes of the multiverse. For the purposes of this discussion we shall say that a statement is *indeterminate according to the multiverse conception* if it is neither true nor false according to the multiverse conception. How radical such a view is depends on the breadth of the conception of the multiverse.

### 4.1 Broad Multiverse Views

The pluralist is generally a non-pluralist about certain domains of mathematics. For example, a strict finitist might be a non-pluralist about PA but a pluralist about set theory and one might be a non-pluralist about ZFC and a pluralist about large cardinal axioms and statements like CH.

There is a form of radical pluralism which advocates pluralism concerning all domains of mathematics. On this view any consistent theory is a legitimate candidate and the corresponding models of such theories are legitimate candidates for the domain of mathematics. Let us call this the *broadest multiverse* view. There is a difficulty in articulating this view, which may be brought out as follows: To begin with, one must pick a background theory in which to discuss the various models and this leads to a difficult. For example, according to the broad multiverse conception, since PA cannot prove Con(PA) (by the second incompleteness theorem, assuming that PA is consistent) there are models of PA + ¬Con(PA) and these models are legitimate candidates, that is, they are universes within the broad multiverse. Now to arrive at this conclusion one must (in the background theory) be in a position to prove Con(PA) (since this assumption is required to apply the second incompleteness theorem in this particular case). Thus, from the perspective of the background theory used to argue that the above models are legitimate candidates, the models in question satisfy a false Σ01-sentence, namely, ¬Con(PA). In short, there is a lack of harmony between what is held at the meta-level and what is held at the object-level.

The only way out of this difficulty would seem to be to regard each viewpoint—each articulation of the multiverse conception—as provisional and, when pressed, embrace pluralism concerning the background theory. In other words, one would have to adopt a multiverse conception of the multiverse, a multiverse conception of the multiverse conception of the multiverse, and so on, off to infinity. It follows that such a position can never be fully articulated—each time one attempts to articulate the broad multiverse conception one must employ a background theory but since one is a pluralist about that background theory this pass at using the broad multiverse to articulate the conception does not do the conception full justice. The position is thus difficult to articulate. One can certainly take the pluralist *stance* and try to *gesture toward* or *exhibit* the view that one intends by provisionally settling on a particular background theory but then advocate pluralism regarding *that* when pressed. The view is thus something of a “moving target”. We shall pass over this view in silence and concentrate on views that can be articulated within a foundational framework.

We will accordingly look at views which embrace non-pluralism with regard to a given stretch of mathematics and for reasons of space and because this is an entry on set theory we will pass over the long debates concerning strict finitism, finitism, predicativism, and start with views that embrace non-pluralism regarding ZFC.

Let the *broad multiverse* (based on ZFC) be the collection of all models of ZFC. The broad multiverse conception of truth (based on ZFC) is then simply the view that a statement of set theory is true simpliciter if it is provable in ZFC. On this view the statement Con(ZFC) and other undecided Π01-statements are classified as indeterminate. This view thus faces a difficulty parallel to the one mentioned above concerning radical pluralism.

This motivates the shift to views that narrow the class of universes in the multiverse by employing a strong logic. For example, one can restrict to universes that are ω-models, β-models (i.e., wellfounded), etc. On the view where one takes ω-models, the statement Con(ZFC) is classified as true (though this is sensitive to the background theory) but the statement PM (all projective sets are Lebesgue measurable) is classified as indeterminate.

For those who are convinced by the arguments (surveyed in the entry “Large Cardinals and Determinacy”) for large cardinal axioms and axioms of definable determinacy, even these multiverse conceptions are too weak. We will follow this route. For the rest of this entry we will embrace non-pluralism concerning large cardinal axioms and axioms of definable determinacy and focus on the question of CH.

### 4.2 The Generic Multiverse

The motivation behind the generic multiverse is to grant the case for large cardinal axioms and definable determinacy but deny that statements such as CH have a determinate truth value. To be specific about the background theory let us take ZFC + “There is a proper class of Woodin cardinals” and recall that this large cardinal assumption secures axioms of definable determinacy such as PD and AD^{*L*(ℝ)}.

Let the *generic multiverse* 𝕍 be the result of closing *V* under generic extensions and generic refinements. One way to formalize this is by taking an external vantage point and start with a countable transitive model *M*. The generic multiverse based on *M* is then the smallest set 𝕍_{*M*} such that M ∈ 𝕍_{*M*} and, for each pair of countable transitive models (*N*, *N*[*G*]) such that *N* ⊧ ZFC and *G* ⊆ ℙ is *N*-generic for some partial order in ℙ ∈ *N*, if either *N* or *N*[*G*] is in 𝕍_{*M*} then both *N* and *N*[*G*] are in 𝕍_{*M*}.

Let the *generic multiverse conception of truth* be the view that a statement is true simpliciter iff it is true in all universes of the generic multiverse. We will call such a statement a *generic multiverse truth*. A statement is said to be *indeterminate according to the generic multiverse conception* iff it is neither true nor false according to the generic multiverse conception. For example, granting our large cardinal assumptions, such a view deems PM (and PD and AD^{*L*(ℝ)}) true but deems CH indeterminate.

### 4.3 The Ω Conjecture and the Generic Multiverse

Is the generic multiverse conception of truth tenable? The answer to this question is closely related to the subject of Ω-logic. The basic connection between generic multiverse truth and Ω-logic is embodied in the following theorem:

**Theorem 4.1** (Woodin).

*Assume* ZFC *and that there is a proper class of Woodin cardinals. Then, for each* Π₂*-statement* φ *the following are equivalent*:

φ *is a generic multiverse truth.* φ *is* Ω*-valid.*

Now, recall that by Theorem 3.5, under our background assumptions, Ω-validity is generically invariant. It follows that given our background theory, the notion of generic multiverse truth is robust with respect to Π₂-statements. In particular, for Π₂-statements, the statement “φ is indeterminate” is *itself* determinate according to the generic multiverse conception. In this sense the conception of truth is not “self-undermining” and one is not sent in a downward spiral where one has to countenance multiverses of multiverses. So it passes the first test. Whether it passes a more challenging test depends on the Ω Conjecture.

The Ω Conjecture has profound consequences for the generic multiverse conception of truth. Let

> 𝒱_{Ω} = {φ | ∅ ⊧_{Ω} φ}

and, for any specifiable cardinal κ, let

> 𝒱_{Ω}(*H*(κ⁺)) = {φ | ZFC ⊧_{Ω}“*H*(κ⁺) ⊧ φ”},

where recall that *H*(κ⁺) is the collection of sets of hereditary cardinality less than κ⁺. Thus, assuming ZFC and that there is a proper class of Woodin cardinals, the set 𝒱_{Ω} is Turing equivalent to the set of Π₂ generic multiverse truths and the set 𝒱_{Ω}(*H*(κ⁺)) is precisely the set of generic multiverse truths of *H*(κ⁺).

To describe the bearing of the Ω Conjecture on the generic-multiverse conception of truth, we introduce two Transcendence Principles which serve as constraints on any tenable conception of truth in set theory—a *truth constraint* and a *definability constraint*.

**Definition 4.2** (Truth Constraint).

Any tenable multiverse conception of truth in set theory must be such that the Π₂-truths (according to that conception) in the universe of sets are not recursive in the truths about *H*(κ) (according to that conception), for any specifiable cardinal.

This constraint is in the spirit of those principles of set theory—most notably, reflection principles—which aim to capture the pretheoretic idea that the universe of sets is so rich that it cannot “be described from below”; more precisely, it asserts that any tenable conception of truth must respect the idea that the universe of sets is so rich that truth (or even just Π₂-truth) cannot be described in some specifiable fragment. (Notice that by Tarski's theorem on the undefinability of truth, the truth constraint is trivially satisfied by the standard conception of truth in set theory which takes the multiverse to contain a single element, namely, *V*.)

There is also a related constraint concerning the definability of truth. For a specifiable cardinal κ, set *Y* ⊆ ω is *definable in* *H*(κ⁺) *across the multiverse* if *Y* is definable in the structure *H*(κ⁺) of each universe of the multiverse (possibly by formulas which depend on the parent universe).

**Definition 4.3** (Definability Constraint).

Any tenable multiverse conception of truth in set theory must be such that the Π₂-truths (according to that conception) in the universe of sets are definable in *H*(κ) across the multiverse universe, for any specifiable cardinal κ.

Notice again that by Tarski's theorem on the undefinability of truth, the definability constraint is trivially satisfied by the degenerate multiverse conception that takes the multiverse to contain the single element *V*. (Notice also that if one modifies the definability constraint by adding the requirement that the definition be *uniform* across the multiverse, then the constraint would automatically be met.)

The bearing of the Ω Conjecture on the tenability of the generic-multiverse conception of truth is contained in the following two theorems:

**Theorem 4.4** (Woodin).

*Assume* ZFC *and that there is a proper class of Woodin cardinals. Suppose that the* Ω *Conjecture holds. Then* 𝒱_{Ω} *is recursive in* 𝒱_{Ω}(*H*(δ+0))*, where* δ₀ *is the least Woodin cardinal.*

**Theorem 4.5** (Woodin).

*Assume* ZFC *and that there is a proper class of Woodin cardinals. Suppose that the* Ω *Conjecture holds. Then* 𝒱_{Ω} *is definable in* *H*(δ+0)*, where* δ₀ *is the least Woodin cardinal.*

In other words, if there is a proper class of Woodin cardinals and if the Ω Conjecture holds then the generic multiverse conception of truth violates both the Truth Constraint (at δ₀) and the Definability Constraint (at δ₀).

There are actually sharper versions of the above results that involve *H*(*c*⁺) in place of *H*(δ+0).

**Theorem 4.6** (Woodin).

*Assume* ZFC *and that there is a proper class of Woodin cardinals. Suppose that the* Ω *Conjecture holds. Then* 𝒱_{Ω} *is recursive in* 𝒱_{Ω}(*H*(*c*⁺))*.*

**Theorem 4.7** (Woodin).

*Assume* ZFC *and that there is a proper class of Woodin cardinals. Suppose that the* Ω *Conjecture holds and that the* AD⁺ *Conjecture holds. Then* 𝒱_{Ω} *is definable in* *H*(*c*⁺)*.*

In other words, if there is a proper class of Woodin cardinals and if the Ω Conjecture holds then the generic-multiverse conception of truth violates the Truth Constraint at the level of third-order arithmetic, and if, in addition, the AD⁺ Conjecture holds, then the generic-multiverse conception of truth violates the Definability Constraint at the level of third-order arithmetic.

### 4.4 Is There a Way Out?

There appear to be four ways that the advocate of the generic multiverse might resist the above criticism.

First, one could maintain that the Ω Conjecture is just as problematic as CH and hence like CH it is to be regarded as indeterminate according to the generic-multiverse conception of truth. The difficulty with this approach is the following:

**Theorem 4.8** (Woodin).

*Assume* ZFC *and that there is a proper class of Woodin cardinals. Then, for any complete Boolean algebra* 𝔹*,*

*V* ⊧ Ω-conjecture iff *V*^{𝔹} ⊧ Ω-conjecture.

Thus, in contrast to CH, the Ω Conjecture cannot be shown to be independent of ZFC + “There is a proper class of Woodin cardinals” via set forcing. In terms of the generic multiverse conception of truth, we can put the point this way: While the generic-multiverse conception of truth deems CH to be indeterminate, it does *not* deem the Ω Conjecture to be indeterminate. So the above response is not available to the advocate of the generic-multiverse conception of truth. The advocate of that conception *already* deems the Ω Conjecture to be determinate.

Second, one could grant that the Ω Conjecture is determinate but maintain that it is false. There are ways in which one might do this but that does not undercut the above argument. The reason is the following: To begin with there is a closely related Σ₂-statement that one can substitute for the Ω Conjecture in the above arguments. This is the statement that the Ω Conjecture is (non-trivially) Ω-satisfiable, that is, the statement: There exists an ordinal α and a universe *V′* of the multiverse such that

> *V′*_{α} ⊧ ZFC + “There is a proper class of Woodin cardinals”

and

> *V′*_{α} ⊧ “The Ω Conjecture”.

This Σ₂-statement is invariant under set forcing and hence is one adherents to the generic multiverse view of truth must deem determinate. Moreover, the key arguments above go through with this Σ₂-statement instead of the Ω Conjecture. The person taking this second line of response would thus also have to maintain that this statement is false. But there is substantial evidence that this statement is *true*. The reason is that there is no known example of a Σ₂-statement that is invariant under set forcing relative to large cardinal axioms and which cannot be settled by large cardinal axioms. (Such a statement would be a candidate for an *absolutely undecidable* statement.) So it is reasonable to expect that this statement is resolved by large cardinal axioms. However, recent advances in inner model theory—in particular, those in Woodin (2010)[^woodin-2010]—provide evidence that no large cardinal axiom can refute this statement. Putting everything together: It is very likely that this statement is in fact *true* ; so this line of response is not promising.

Third, one could reject either the Truth Constraint or the Definability Constraint. The trouble is that if one rejects the Truth Constraint then on this view (assuming the Ω Conjecture) Π₂ truth in set theory is reducible *in the sense of Turing reducibility* to truth in *H*(δ₀) (or, assuming the Strong Ω Conjecture, *H*(*c*⁺)). And if one rejects the Definability Constraint then on this view (assuming the Ω Conjecture) Π₂ truth in set theory is reducible *in the sense of definability* to truth in *H*(δ₀) (or, assuming the Strong Ω Conjecture, *H*(*c*⁺)). On either view, the reduction is in tension with the acceptance of non-pluralism regarding the background theory ZFC + “There is a proper class of Woodin cardinals”.

Fourth, one could embrace the criticism, reject the generic multiverse conception of truth, and admit that there are some statements about *H*(δ+0) (or *H*(*c*⁺), granting, in addition, the AD⁺ Conjecture) that are true simpliciter but not true in the sense of the generic-multiverse, and yet nevertheless continue to maintain that CH is indeterminate. The difficulty is that any such sentence φ is qualitatively just like CH in that it can be forced to hold and forced to fail. The challenge for the advocate of this approach is to modify the generic-multiverse conception of truth in such a way that it counts φ as determinate and yet counts CH as indeterminate.

In summary: There is evidence that the only way out is the fourth way out and this places the burden back on the pluralist—the pluralist must come up with a modified version of the generic multiverse.

*Further Reading*: For more on the connection between Ω-logic and the generic multiverse and the above criticism of the generic multiverse see Woodin (2011a)[^woodin-2011a]. For the bearing of recent results in inner model theory on the status of the Ω Conjecture see Woodin (2010)[^woodin-2010].

## 5. The Local Case Revisited

Let us now turn to a second way in which one might resist the local case for the failure of CH. This involves a parallel case for CH. In Section 5.1 we will review the main features of the case for ¬CH in order to compare it with the parallel case for CH. In Section 5.2 we will present the parallel case for CH. In Section 5.3 we will assess the comparison.

### 5.1 The Case for ¬CH

Recall that there are two basic steps in the case presented in Section 3.3. The first step involves Ω-completeness (and this gives ¬CH) and the second step involves maximality (and this gives the stronger 2^{ℵ₀} = ℵ₂). For ease of comparison we shall repeat these features here:

The first step is based on the following result:

**Theorem 5.1** (Woodin).

*Assume that there is a proper class of Woodin cardinals and that the Strong* Ω *Conjecture holds.*

*There is an axiom* *A* *such that* ZFC + *A* *is* Ω*-satisfiable and* ZFC + *A* *is* Ω*-complete for the structure* *H*(ω₂)*.* *Any such axiom* *A* *has the feature that* ZFC + *A* ⊧_{ Ω}“*H*(ω₂) ⊧ ¬CH”.

Let us rephrase this as follows: For each *A* satisfying (1), let

> *T*_{*A*} = {φ | ZFC + *A* ⊧_{Ω} “*H*(ω₂) ⊧ ¬φ”}.

The theorem says that if there is a proper class of Woodin cardinals and the Strong Ω Conjecture holds, then there are (non-trivial) Ω-complete theories *T*_{*A*} of *H*(ω₂) and all such theories contain ¬CH. In other words, under these assumptions, there is a “good” theory and all “good” theories imply ¬CH.

The second step begins with the question of whether there is greater agreement among the Ω-complete theories *T*_{*A*}. Ideally, there would be just one. However, this is not the case.

**Theorem 5.2** (Koellner and Woodin 1999)[^woodin-1999].

*Assume that there is a proper class of Woodin cardinals. Suppose that* *A* *is an axiom such that*

i.  ZFC + *A* *is* Ω*-satisfiable and* ii.  ZFC + *A* *is* Ω*-complete for the structure* *H*(ω₂)*.* *Then there is an axiom* *B* *such that*  i′.  ZFC + *B* *is* Ω*-satisfiable and* ii′.  ZFC + *B* *is* Ω*-complete for the structure* *H*(ω₂)

*and* *T*_{*A*}≠*T*_{*B*}*.*

This raises the issue as to how one is to select from among these theories? It turns out that there is a maximal theory among the *T*_{*A*} and this is given by the axiom (∗).

**Theorem 5.3** (Woodin).

*Assume* ZFC *and that there is a proper class of Woodin cardinals. Then the following are equivalent*:

(∗)*.* *For each* Π₂*-sentence* φ *in the language for the structure* ⟨*H*(ω₂), ∈, *I*_{NS}, *A* | *A* ∈ 𝒫 (ℝ) ∩ *L*(ℝ)⟩ *if* ZFC + “⟨*H*(ω₂), ∈, *I*_{NS}, *A* | *A* ∈ 𝒫 (ℝ) ∩ *L*(ℝ)⟩ ⊧ φ” *is* Ω*-consistent, then* ⟨*H*(ω₂), ∈, *I*_{NS}, *A* | *A* ∈ 𝒫 (ℝ) ∩ *L*(ℝ)⟩ ⊧ φ.

So, of the various theories *T*_{*A*} involved in Theorem 5.1, there is one that stands out: The theory *T*_{(∗)} given by (∗). This theory maximizes the Π₂-theory of the structure ⟨*H*(ω₂), ∈, *I*_{NS}, *A* | *A* ∈ 𝒫 (ℝ) ∩ *L*(ℝ)⟩. The fundamental result is that in this maximal theory

> 2^{ℵ₀} = ℵ₂.

### 5.2 The Parallel Case for CH

The parallel case for CH also has two steps, the first involving Ω-completeness and the second involving maximality.

The first result in the first step is the following:

**Theorem 5.4** (Woodin 1985).

*Assume* ZFC *and that there is a proper class of measurable Woodin cardinals. Then* ZFC + CH *is* Ω*-complete for* Σ21*.*

Moreover, up to Ω-equivalence, CH is the unique Σ21-statement that is Ω-complete for Σ21; that is, letting *T*_{*A*} be the Ω-complete theory given by ZFC + *A* where *A* is Σ21, all such *T*_{*A*} are Ω-equivalent to *T*_{CH} and hence (trivially) all such *T*_{*A*} contain CH. In other words, there is a “good” theory and all “good” theories imply CH.

To complete the first step we have to determine whether this result is robust. For it could be the case that when one considers the next level, Σ22 (or further levels, like third-order arithmetic) CH is no longer part of the picture, that is, perhaps large cardinals imply that there is an axiom *A* such that ZFC + *A* is Ω-complete for Σ22 (or, going further, all of third order arithmetic) and yet *not* all such *A* have an associated *T*_{*A*} which contains CH. We must rule this out if we are to secure the first step.

The most optimistic scenario along these lines is this: The scenario is that there is a large cardinal axiom *L* and axioms *A*→ such that ZFC + *L* + *A*→ is Ω-complete for all of third-order arithmetic and all such theories are Ω-equivalent and imply CH. Going further, perhaps for each specifiable fragment *V*_{λ} of the universe of sets there is a large cardinal axiom *L* and axioms *A*→ such that ZFC + *L* + *A*→ is Ω-complete for the entire theory of *V*_{λ} and, moreover, that such theories are Ω-equivalent and imply CH. Were this to be the case it would mean that for each such λ there is a unique Ω-complete picture of *V*_{λ} and we would have a unique Ω-complete understanding of arbitrarily large fragments of the universe of sets. This would make for a strong case for new axioms completing the axioms of ZFC and large cardinal axioms.

Unfortunately, this optimistic scenario fails: Assuming the existence of one such theory one can construct another which differs on CH:

**Theorem 5.5** (Koellner and Woodin 2009)[^koellner-2009].

*Assume* ZFC *and that there is a proper class of Woodin cardinals. Suppose* *V*_{λ} *is a specifiable fragment of the universe (that is sufficiently large) and suppose that there is a large cardinal axiom* *L* *and axioms* *A*→ *such that*

ZFC + *L* + *A*→ is Ω-complete for Th(*V*_{λ}).

*Then there are axioms* *B*→ *such that*

ZFC + *L* + *B*→ is Ω-complete for Th(*V*_{λ})

*and the first theory* Ω*-implies* CH *if and only if the second theory* Ω*-implies* ¬CH.

This still leaves us with the question of existence and the answer to this question is sensitive to the Ω Conjecture and the AD⁺ Conjecture:

**Theorem 5.6** (Woodin).

*Assume that there is a proper class of Woodin cardinals and that the* Ω *Conjecture holds. Then there is no recursive theory* *A*→ *such that* ZFC + *A*→ *is* Ω*-complete for the theory of* *V*_{δ0}+1*, where* δ₀ *is the least Woodin cardinal.*

In fact, under a stronger assumption, the scenario must fail at a much earlier level.

**Theorem 5.7** (Woodin).

*Assume that there is a proper class of Woodin cardinals and that the* Ω *Conjecture holds. Assume that the* AD⁺ *Conjecture holds. Then there is no recursive theory* *A*→ *such that* ZFC + *A*→ *is* Ω*-complete for the theory of* Σ23*.*

It is open whether there can be such a theory at the level of Σ22. It is conjectured that ZFC + ◇ is Ω-complete (assuming large cardinal axioms) for Σ22.

Let us assume that it is answered positively and return to the question of uniqueness. For each such axiom *A*, let *T*_{*A*} be the Σ22 theory computed by ZFC + *A* in Ω-logic. The question of uniqueness simply asks whether *T*_{*A*} is unique.

**Theorem 5.8** (Koellner and Woodin 2009)[^koellner-2009].

*Assume that there is a proper class of Woodin cardinals. Suppose that* *A* *is an axiom such that*

i. ZFC + *A* *is* Ω*-satisfiable and* ii. ZFC + *A* *is* Ω*-complete for* Σ22.

*Then there is an axiom* *B* *such that*

i′. ZFC + *B* *is* Ω*-satisfiable and* ii′. ZFC + *B* *is* Ω*-complete for* Σ22

*and* *T*_{*A*}≠*T*_{*B*}*.*

This is the parallel of Theorem 5.2.

To complete the parallel one would need that CH is among all of the *T*_{*A*}. This is not known. But it is a reasonable conjecture.

**Conjecture 5.9.**

Assume large cardinal axioms.

There is an Σ22 axiom *A* such that ZFC + *A* is Ω-satisfiable and ZFC + *A* is Ω-complete for the Σ22. Any such Σ22 axiom *A* has the feature that ZFC + *A* ⊧_{Ω} CH.

Should this conjecture hold it would provide a true analogue of Theorem 5.1. This would complete the parallel with the first step.

There is also a parallel with the second step. Recall that for the second step in the previous subsection we had that although the various *T*_{*A*} did not agree, they all contained ¬CH and, moreover, from among them there is one that stands out, namely the theory given by (∗), since this theory maximizes the Π₂-theory of the structure ⟨*H*(ω₂), ∈, *I*_{NS}, *A* | *A* ∈ P (ℝ) ∩ *L*(ℝ)⟩. In the present context of CH we again (assuming the conjecture) have that although the *T*_{*A*} do not agree, they all contain CH. It turns out that once again, from among them there is one that stands out, namely, the maximum one. For it is known (by a result of Woodin in 1985) that if there is a proper class of measurable Woodin cardinals then there is a forcing extension satisfying all Σ22 sentences φ such that ZFC + CH + φ is Ω-satisfiable (see Ketchersid, Larson, & Zapletal (2010)). It follows that if the question of existence is answered positively with an *A* that is Σ22 then *T*_{*A*} must be this maximum Σ22 theory and, consequently, all *T*_{*A*} agree when *A* is Σ22. So, assuming that there is a *T*_{*A*} where *A* is Σ22, then, although not all *T*_{*A*} agree (when *A* is arbitrary) there is one that stands out, namely, the one that is maximum for Σ22 sentences.

Thus, *if* the above conjecture holds, then the case of CH parallels that of ¬CH, only now Σ22 takes the place of the theory of *H*(ω₂).

### 5.3 Assessment

Assuming that the conjecture holds the case of CH parallels that of ¬CH, only now Σ22 takes the place of the theory of *H*(ω₂): Under the background assumptions we have:

1. 
2. there are *A* such that ZFC + *A* is Ω-complete for *H*(ω₂)
3. for every such *A* the associated *T*_{*A*} contains ¬CH, and
4. there is a *T*_{*A*} which is maximal, namely, *T*_{(∗)} and this theory contains 2^{ℵ₀} = ℵ₂.
5. 
6. there are Σ22-axioms *A* such that ZFC + *A* is Ω-complete for Σ22
7. for every such *A* the associated *T*_{*A*} contains CH, and
8. there is a *T*_{*A*} which is maximal.

The two situations are parallel with regard to maximality but in terms of the level of Ω-completeness the first is stronger. For in the first case we are not just getting Ω-completeness with regard to the Π₂ theory of *H*(ω₂) (with the additional predicates), rather we are getting Ω-completeness with regard to *all* of *H*(ω₂). This is arguably an argument in favour of the case for ¬CH, even granting the conjecture.

But there is a stronger point. There is evidence coming from inner model theory (which we shall discuss in the next section) to the effect that the conjecture is in fact *false*. Should this turn out to be the case it would break the parallel, strengthening the case for ¬CH.

However, one might counter this as follows: The higher degree of Ω-completeness in the case for ¬CH is really illusory since it is an artifact of the fact that under (∗) the theory of *H*(ω₂) is in fact mutually interpretable with that of *H*(ω₁) (by a deep result of Woodin). Moreover, this latter fact is in conflict with the spirit of the Transcendence Principles discussed in Section 4.3. Those principles were invoked in an argument to the effect that CH does not have an answer. Thus, when all the dust settles the real import of Woodin's work on CH (so the argument goes) is *not* that CH is false but rather that CH very likely has an answer.

It seems fair to say that at this stage the status of the local approaches to resolving CH is somewhat unsettled. For this reason, in the remainder of this entry we shall focus on global approaches to settling CH. We shall very briefly discuss two such approaches—the approach via inner model theory and the approach via quasi-large cardinal axioms.

## 6. The Ultimate Inner Model

Inner model theory aims to produce “*L*-like” models that contain large cardinal axioms. For each large cardinal axiom Φ that has been reached by inner model theory, one has an axiom of the form *V* = *L*^{Φ}. This axiom has the virtue that (just as in the simplest case of *V* = *L*) it provides an “effectively complete” solution regarding questions about *L*^{Φ} (which, by assumption, is *V*). Unfortunately, it turns out that the axiom *V* = *L*^{Φ} is incompatible with *stronger* large cardinal axioms Φ'. For this reason, axioms of this form have never been considered as plausible candidates for new axioms.

But recent developments in inner model theory (due to Woodin) show that everything changes at the level of a supercompact cardinal. These developments show that if there is an inner model *N* which “inherits” a supercompact cardinal from *V* (in the manner in which one would expect, given the trajectory of inner model theory), then there are two remarkable consequences: First, *N* is close to *V* (in, for example, the sense that for sufficiently large singular cardinals λ, *N* correctly computes λ⁺). Second, *N* inherits all known large cardinals that exist in *V*. Thus, in contrast to the inner models that have been developed thus far, an inner model at the level of a supercompact would provide one with an axiom that could *not* be refuted by stronger large cardinal assumptions.

The issue, of course, is whether one can have an “*L*-like” model (one that yields an “effectively complete” axiom) at this level. There is reason to believe that one can. There is now a candidate model *L*^{Ω} that yields an axiom *V* = *L*^{Ω} with the following features: First, *V* = *L*^{Ω} is “effectively complete.” Second, *V* = *L*^{Ω} is compatible with all large cardinal axioms. Thus, on this scenario, the ultimate theory would be the (open-ended) theory ZFC + *V* = *L*^{Ω} + LCA, where LCA is a schema standing for “large cardinal axioms.” The large cardinal axioms will catch instances of Gödelian independence and the axiom *V* = *L*^{Ω} will capture the remaining instances of independence. This theory would imply CH and settle the remaining undecided statements. Independence would cease to be an issue.

It turns out, however, that there are other candidate axioms that share these features, and so the spectre of pluralism reappears. For example, there are axioms *V* = *L*Ω*S* and *V* = *L*Ω(∗). These axioms would also be “effectively complete” and compatible with all large cardinal axioms. Yet they would resolve various questions differently than the axiom *V* = *L*^{Ω}. For example, the axiom, *V* = *L*Ω(∗) would imply ¬CH. How, then, is one to adjudicate between them?

*Further Reading*: For an introduction to inner model theory see Mitchell (2010)[^mitchell-2010] and Steel (2010)[^steel-2010]. For more on the recent developments at the level of one supercompact and beyond see Woodin (2010)[^woodin-2010].

## 7. The Structure Theory of *L*(*V*_{λ+1})

This brings us to the second global approach, one that promises to select the correct axiom from among *V* = *L*^{Ω}, *V* = *L*Ω*S*, *V* = *L*Ω(∗), and their variants. This approach is based on the remarkable analogy between the structure theory of *L*(ℝ) under the assumption of AD^{*L*(ℝ)} and the structure theory of *L*(*V*_{λ+1}) under the assumption that there is an elementary embedding from *L*(*V*_{λ+1}) into itself with critical point below λ. This *embedding assumption* is the strongest large cardinal axiom that appears in the literature.

The analogy between *L*(ℝ) and *L*(*V*_{λ+1}) is based on the observation that *L*(ℝ) is simply *L*(*V*_{ω+1}). Thus, λ is the analogue of ω, λ⁺ is the analogue of ω₁, and so on. As an example of the parallel between the structure theory of *L*(ℝ) under AD^{*L*(ℝ)} and the structure theory of *L*(*V*_{λ+1}) under the embedding axiom, let us mention that in the first case, ω₁ is a measurable cardinal in *L*(ℝ) and, in the second case, the analogue of ω₁—namely, λ⁺—is a measurable cardinal in *L*(*V*_{λ+1}). This result is due to Woodin and is just one instance from among many examples of the parallel that are contained in his work.

Now, we have a great deal of information about the structure theory of *L*(ℝ) under AD^{*L*(ℝ)}. Indeed, as we noted above, this axiom is “effectively complete” with regard to questions about *L*(ℝ). In contrast, the embedding axiom on its own is not sufficient to imply that *L*(*V*_{λ+1}) has a structure theory that fully parallels that of *L*(ℝ) under AD^{*L*(ℝ)}. However, the existence of an already rich parallel is evidence that the parallel extends, and we can supplement the embedding axiom by adding some key components. When one does so, something remarkable happens: the supplementary axioms become *forcing fragile*. This means that they have the potential to erase independence and provide non-trivial information about *V*_{λ+1}. For example, these supplementary axioms might settle CH and much more.

The difficulty in investigating the possibilities for the structure theory of *L*(*V*_{λ+1}) is that we have not had the proper lenses through which to view it. The trouble is that the model *L*(*V*_{λ+1}) contains a large piece of the universe—namely, *L*(*V*_{λ+1})—and the theory of this structure is radically underdetermined. The results discussed above provide us with the proper lenses. For one can examine the structure theory of *L*(*V*_{λ+1}) in the context of ultimate inner models like *L*^{Ω}, *L*Ω*S*, *L*Ω(∗), and their variants. The point is that these models can accommodate the embedding axiom and, within each, one will be able to compute the structure theory of *L*(*V*_{λ+1}).

This provides a means to select the correct axiom from among *V* = *L*^{Ω}, *V* = *L*Ω*S*, *V* = *L*Ω(∗), and their variants. One simply looks at the *L*(*V*_{λ+1}) of each model (where the embedding axiom holds) and checks to see which has the true analogue of the structure theory of *L*(ℝ) under the assumption of AD^{*L*(ℝ)}. It is already known that certain pieces of the structure theory *cannot* hold in *L*^{Ω}. But it is open whether they can hold in *L*Ω*S*.

Let us consider one such (very optimistic) scenario: The true analogue of the structure theory of *L*(ℝ) under AD^{*L*(ℝ)} holds of the *L*(*V*_{λ+1}) of *L*Ω*S* but not of any of its variants. Moreover, this structure theory is “effectively complete” for the theory of *V*_{λ+1}. Assuming that there is a proper class of λ where the embedding axiom holds, this gives an “effectively complete” theory of *V*. And, remarkably, part of that theory is that *V* *must* be *L*Ω*S*. This (admittedly very optimistic) scenario would constitute a very strong case for axioms that resolve all of the undecided statements.

One should not place too much weight on this particular scenario. It is just one of many. The point is that we are now in a position to write down a list of definite questions with the following features: First, the questions on this list will have answers—independence is not an issue. Second, if the answers converge then one will have strong evidence for new axioms settling the undecided statements (and hence non-pluralism about the universe of sets); while if the answers oscillate, one will have evidence that these statements are “absolutely undecidable” and this will strengthen the case for pluralism. In this way the questions of “absolute undecidability” and pluralism are given mathematical traction.

*Further Reading*: For more on the structure theory of *L*(*V*_{λ+1}) and the parallel with determinacy see Woodin (2011b)[^woodin-2011b].

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=continuum-hypothesis). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/continuum-hypothesis/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=continuum-hypothesis&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](http://philpapers.org/sep/continuum-hypothesis/) at [PhilPapers](http://philpapers.org/), with links to its database. |

## Other Internet Resources

[Please contact the author with suggestions.]

## Related Entries

Gödel, Kurt | set theory | set theory: early development | set theory: large cardinals and determinacy

## Notes（原文脚注）

[^note-1]: See Hallett (1984)[^hallett-1984] for further historical information on the role of CH in the early foundations of set theory.

[^note-2]: We have of necessity presupposed much in the way of set theory. The reader seeking additional detail—for example, the definitions of regular and singular cardinals and other fundamental notions—is directed to one of the many excellent texts in set theory, for example Jech (2003)[^jech-2003].

[^note-3]: To say that GCH holds below δ is just to say that 2^{ℵ_{α}} = ℵ_{α+1} for all ω ≤ α < δ and to say that GCH holds at δ is just to say that 2^{ℵ_{δ}} = ℵ_{δ+1}).

[^note-4]: To see this argue as follows: Assume large cardinal axioms at the level involved in (A) and (B) and assume that there is a proper class of Woodin cardinals. Suppose for contradiction that there is a prewellordering in *L*(ℝ) of length ℵ₂. Now, using (A) force to obtain a saturated ideal on ℵ₂ without collapsing ℵ₂. In this forcing extension, the original prewellordering is still a prewellordering in *L*(ℝ) of length ℵ₂, which contradicts (B). Thus, the original large cardinal axioms imply that Θ^{*L*(ℝ)} ≤ ℵ₂. The same argument applies in the more general case where the prewellordering is universally Baire.

[^note-5]: For more on the topic of invariance under set forcing and the extent to which this has been established in the presence of large cardinal axioms, see §4.4 and §4.6 of the entry “Large Cardinals and Determinacy”.

[^note-6]: The non-stationary ideal *I*_{NS} is a proper class from the point of view of *H*(ω₂) and it manifests (through Solovay’s theorem on splitting stationary sets) a non-trivial application of AC. For further details concerning *A*^{*G*} see §4.6 of the entry “Large Cardinals and Determinacy”.

[^note-7]: Here are the details: Let *A* ∈ Γ^{∞} and *M* be a countable transitive model of ZFC. We say that *M* is *A*-*closed* if for all set generic extensions *M*[*G*] of *M*, *A* ∩ *M*[*G*] ∈ *M*[*G*]. Let *T* be a set of sentences and φ be a sentence. We say that *T* ⊢_{Ω} φ if there is a set *A* ⊆ ℝ such that

1. *L*(*A*, ℝ) ⊧ AD⁺,
2. 𝒫 (ℝ) ∩ *L*(*A*, ℝ) ⊆ Γ^{∞}, and
3. for all countable transitive *A*-closed *M*, *M* ⊧ “*T* ⊧_{Ω} φ”, where here AD⁺ is a strengthening of AD.

[^note-8]: Here are the details: First we need another conjecture: (The AD⁺ Conjecture) Suppose that *A* and *B* are sets of reals such that *L*(*A*, ℝ) and *L*(*B*, ℝ) satisfy AD⁺. Suppose every set

> *X* ∈ 𝒫 (ℝ) ∩ (*L*(*A*, ℝ) ∪ *L*(*B*, ℝ))

is ω₁-universally Baire. Then either

> (Δ̰21)^{*L*(*A*,ℝ)} ⊆ (Δ̰21)^{*L*(*B*,ℝ)}

or

> (Δ̰21)^{*L*(*B*,ℝ)} ⊆ (Δ̰21)}^{*L*(*A*,ℝ)}.

(Strong Ω conjecture) Assume there is a proper class of Woodin cardinals. Then the Ω Conjecture holds and the AD⁺ Conjecture is Ω-valid.

[^note-9]: As mentioned at the end of Section 2.2 it could be the case (given our present knowledge) that large cardinal axioms imply that Θ^{*L*(ℝ)} < ℵ₃ and, more generally, rule out the definable failure of 2^{ℵ₀} = ℵ₂. This would arguably further buttress the case for 2^{ℵ₀} = ℵ₂.

[^abraham-2010]: Abraham, U. and M. Magidor, 2010, “Cardinal arithmetic,” in Foreman and Kanamori 2010.

[^bagaria-2006]: Bagaria, J., N. Castells, and P. Larson, 2006, “An Ω-logic primer,” in J. Bagaria and S. Todorcevic (eds), *Set theory*, Trends in Mathematics, Birkhäuser, Basel, pp. 1–28.

[^cohen-1963]: Cohen, P., 1963, “The independence of the continuum hypothesis I,” *Proceedings of the U.S. National Academy of Sciemces*, 50: 1143–48.

[^foreman-2010]: Foreman, M. and A. Kanamori, 2010, *Handbook of Set Theory*, Springer-Verlag.

[^foreman-1995]: Foreman, M. and M. Magidor, 1995, “Large cardinals and definable counterexamples to the continuum hypothesis,” *Annals of Pure and Applied Logic* 76: 47–97.

[^foreman-1988]: Foreman, M., M. Magidor, and S. Shelah, 1988, “Martin's Maximum, saturated ideals, and non-regular ultrafilters. Part i,” *Annals of Mathematics* 127: 1–47.

[^gödel-1938a]: Gödel, K., 1938a. “The consistency of the axiom of choice and of the generalized continuum-hypothesis,” *Proceedings of the U.S. National Academy of Sciences*, 24: 556–7.

[^gödel-1938b]: Gödel, K., 1938b. “Consistency-proof for the generalized continuum-hypothesis,” *Proceedings of the U.S. National Academy of Sciemces*, 25: 220–4.

[^hallett-1984]: Hallett, M., 1984, *Cantorian Set Theory and Limitation of Size*, Vol. 10 of *Oxford Logic Guides*, Oxford University Press.

[^holz-1999]: Holz, M., K. Steffens, and E. Weitz, 1999, *Introduction to Cardinal Arithmetic*, Birkhäuser Advanced Texts, Birkhäuser Verlag, Basel.

[^jech-2003]: Jech, T. J., 2003, *Set Theory: Third Millennium Edition, Revised and Expanded*, Springer-Verlag, Berlin.

[^ketchersid-2010]: Ketchersid, R., P. Larson, and J. Zapletal, 2010, “Regular embeddings of the stationary tower and Woodin's Sigma-2-2 maximality theorem.” *Journal of Symbolic Logic* 75(2):711–727.

[^koellner-2010]: Koellner, P., 2010, “Strong logics of first and second order,” *Bulletin of Symbolic Logic* 16(1): 1–36.

[^koellner-2009]: Koellner, P. and W. H. Woodin, 2009, “Incompatible Ω-complete theories,” *The Journal of Symbolic Logic* 74 (4).

[^martin-1976]: Martin, D. A., 1976, “Hilbert's first problem: The Continuum Hypothesis,” in F. Browder (ed.), *Mathematical Developments Arising from Hilbert's Problems*, Vol. 28 of *Proceedings of Symposia in Pure Mathematics*, American Mathematical Society, Providence, pp. 81–92.

[^mitchell-2010]: Mitchell, W., 2010, “Beginning inner model theory,” in Foreman and Kanamori 2010.

[^steel-2010]: Steel, J. R., 2010, “An outline of inner model theory,” in Foreman and Kanamori 2010.

[^woodin-1999]: Woodin, W. H., 1999, *The Axiom of Determinacy, Forcing Axioms, and the Nonstationary Ideal*, Vol. 1 of *de Gruyter Series in Logic and its Applications*, de Gruyter, Berlin.

[^woodin-2001a]: –––, 2001a, “The continuum hypothesis, part I,” *Notices of the American Mathematical Society* 48(6): 567–576.

[^woodin-2001b]: –––, 2001b, “The continuum hypothesis, part II,” *Notices of the American Mathematical Society* 48(7): 681–690.

[^woodin-2005a]: –––, 2005a, “The continuum hypothesis,” in R. Cori, A. Razborov, S. Todorĉević and C. Wood (eds), *Logic Colloquium 2000*, Vol. 19 of *Lecture Notes in Logic*, Association of Symbolic Logic, pp. 143–197.

[^woodin-2005b]: –––, 2005b, “Set theory after Russell: the journey back to Eden,” in G. Link (ed.), *One Hundred Years Of Russell's Paradox: Mathematics, Logic, Philosophy* , Vol. 6 of *de Gruyter Series in Logic and Its Applications*, Walter De Gruyter Inc, pp. 29–47.

[^woodin-2010]: –––, 2010, “Suitable extender models I,” *Journal of Mathematical Logic* 10(1–2): 101–339.

[^woodin-2011a]: –––, 2011a, “The Continuum Hypothesis, the generic-multiverse of sets, and the Ω-conjecture,” in J. Kennedy and R. Kossak, (eds), *Set Theory, Arithmetic, and Foundations of Mathematics: Theorems, Philosophies*, Vol. 36 of *Lecture Notes in Logic*, Cambridge University Press.

[^woodin-2011b]: –––, 2011b, “Suitable extender models II,” *Journal of Mathematical Logic* 11(2): 115–436.
