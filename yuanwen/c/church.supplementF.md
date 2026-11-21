# church — supplementF（supplement）

> （《church》词条补充材料，源：plato.stanford.edu/entries/church/supplementF.html）

#### Supplement to Alonzo Church

## F. Paradox and Comparison with Tarski

- F.1 The Derivation of GP
- F.2 Comparison with Tarski
- F.3 Reducibility, Definability and Truth
- F.4 Tarski’s Theorem
- F.5 Church’s Formal Analysis of RM

### F.1 The Derivation of GP

The following is Church’s derivation of GP (Grelling’s paradox) within STT plus the axioms for $D(v, F)$ in the style that metamathematical arguments are sometimes presented in his text. Only the spacing of the lines has been changed. The starred numbers refer to sections of Church’s text.

The antinomy in simple type theory is obtained as follows. We use the abbreviations “P”, “gen.”, “ded.thm.”, “subst.eq.”, “ex.inst.”, “neg.$\exists$”, “S” to refer to propositional calculus, rule of generalization, deduction theorem and analogues of \*513, \*518, \*338, \*509 in the functional calculus of higher order.

By \*,

$$D(v,F), D(v,\het) \vdash F(x) \equiv_{x} \het (x)$$

Hence by subst.eq.,

$$D(v,F), \nsim F(v), D(v,\het) \vdash \nsim \het (v)$$

Hence by ex.inst. and axiom \*\*\*,

$$\het(v), D(v, \het) \vdash \nsim\het (v)$$

Hence by ded.thm.,

$$D(v,\het) \vdash \het(v) \supset \nsim\het(v)$$

Hence by P,

$$D(v, \het) \vdash \nsim\het(v)$$

Hence by the axiom \*\*\*,

$$D(v, \het) \vdash \nsim(\exists F) \hdot D(v, F) \cdot \nsim F(v)$$

Hence by the neg.$\exists$ and P,

$$D(v, \het) \vdash D(v, F) \supset F F(v)$$

Hence by S,

$$D(v, \het) \vdash D(v, \het) \supset \het(v)$$

Hence by modus ponens,

$$D(v, \het) \vdash \het(v)$$

Thus from the hypothesis $D(v, \het)$ we have a proof both of $\nsim\het(v)$ and of $\het(v)$ Hence by ded.thm. and P,

$$\vdash \nsim D(v, \het)$$

Hence by gen.,

$$\vdash(v) \nsim D(v, \het)$$

Hence by neg.$\exists$,

$$\vdash \nsim(\exists v) D(v, \het)$$

But this contradicts \*\*

### F.2 Comparison with Tarski

In section 3 of (1976), Church defines $\stL$ to be the full ramified language with Val constants defined for every $r$-type, but always of level 1 (“predicative” in Russell’s terminology). The language $\rL_n$ results by deleting all variables of order greater than $n$ and only allowing variables of order $n$ to occur as free variables. The language $\rL_1$, which is a first order logic in more or less the usual sense, lacks any Val constants (since their lowest order is 2), and only individual variables are quantified. The language $\rL_2$, like ordinary second order logic allows quantifiers to bind first order predicate and propositional variables, but there are also predicates of first order predicates representing propositional functions of level 2, and these are not bindable variables. This yields a hierarchy of languages, $\rL_1$, $\rL_2$,…, $\rL_{n+1}$,…, indexed by positive integers, where each subsequent language serves as a semantical meta-language for the previous one. Church comments that it is merely matter of terminology whether $\stL$ is regarded as a hierarchy of orders or as an infinite sequence of languages. But he goes on to stress that Tarski’s resolution of the semantical antinomies simply requires that the semantical predicates must belong in the meta-language and hence Russell’s resolution of, e.g., Grelling’s paradox may be viewed as a special case of Tarski’s. To bolster this conclusion Church shows how truth and satisfaction may be defined within the system of orders, and after adding the axioms reducibility, he derives a version of Tarski’s theorem about truth.

### F.3 Reducibility, Definability and Truth

The structure of the $r$-types and the associated ban on impredicative definitions excludes many principles required for the standard theories of natural and real numbers, as well as higher set theory; and to remedy this problem, Russell proposed the axioms of reducibility, defined for each distinct type, whereby propositional functions of higher order are guaranteed to be provably equivalent to propositional functions of the first level (in every type). Russell called these “first order” or “predicative” functions. Reducibility solves the mathematical problem—but Church’s focus in (1976) is on GP and the question whether reducibility together with the semantical principles regarding *Val* allows the resurgence of GP. In what follows we continue to trade in Val for the slightly simpler, but for present purposes, equally general, $D$, but we return to Val when necessary.

Reducibility implies that there is a propositional function of level 1 that is provably equivalent to het of a fixed arbitrary level, as defined by \*\*\*\* in the text:

$$\tag{12′} (\exists H^{1/1}) \hdot H(v) \equiv v (\exists F^{1/n}) D(v, F) \cdot \nsim F(v).$$

No contradiction is forthcoming from this, even with the help of predicative counterparts of (6′) and (7′), unless it is possible to establish *in addition* that *some word* (of whatever level) *denotes* a first level propositional function equivalent to het (of whatever level).

$$\tag{8′} (\exists v)(\exists G^{1/1}) D^{m+2}(v, G) \hdot G(x) \equiv_{x} \het^{m+1}(x).$$

As Church remarks, the formal counterpart of this, (8) of (1976), formulated in terms of Val does not seem to be forthcoming merely by the addition of reducibility; and the same seems to be true of the version (8′) in terms of $D$. Hence, it doesn’t seem that GP is derivable in the system. But this is no proof that it isn’t, and so Church concludes only that “This is an empiric justification of the axioms of reducibility, based on the failure of the direct attempt to restore Grelling’s antinomy by means of them (1976 [BE:. 805]).

Cantor’s theorem in the form CL discussed above in connection with GP, is obviously relevant here, (but Church makes no mention of it). The condition that some word, v, denotes het (in the sense that $D(v, \het)$ holds) is equivalent to the condition that het is in the range of $D$, assuming that $D$ is a well-defined function with a well-defined domain and range. (It could be a function from words as individuals to the extensions of unary propositional functions of level 1.) CL then implies that het cannot be in the range of $D$, since het is the diagonal function determined by $D$. That is, het consists of those words that do not have the properties they denote. But when it comes down to it, the semantical notion of denotation is not doing the work here. Any function that takes words to properties or words to sets can formally replace $D.$ For example, a function that takes words to numbers would work as well. We cannot have a word for het, not because we cannot invent names for definite things in our midst (compare \*\*), but because of how het is defined in terms of $D.$ It’s possible to have a word for het, just not one for which $D$ is defined.

In the last paragraphs of (1976) Church makes some similar remarks about het (without mentioning Cantor’s theorem) and draws some conclusions concerning the Tarski hierarchy of languages/metalanguages. He notes that in the system with Val and reducibility, we have:

$$\tag{14} G^{1/1}(x) \equiv_{x} \het^{ n+1}(x) \supset_{avG} \nsim \val^{2}(a,v,G)$$ $$\tag{15} (\exists G^{1/1}) \hdot G(x) \equiv_{x} \het^{n+1}(x).$$

He remarks that

> The principle significance of theorems (14) and (15) is that there must be, among the values of the variables in $\rL_1$ of $r$-type $1/1$, propositional functions such that no coextensive function is expressible by a propositional form in $\rL_1$, but only in some language arbitrarily far along in the hierarchy $\rL_1$ , $\rL_2$,…

Thus, he takes these two theorems to imply a basic definability result related to Tarski’s theorem (see the next paragraph and n. 26 of 1976). (15) asserts that given het of an arbitrary level, $n+1$, there is a propositional function of level 1 coextensive with it; and this combined with (14) entails:

$$\nsim \val^{2}(a,v,G),$$

which says that the “propositional form” (open sentence), $v$, does not express $G$. Putting $D$ for Val in (14), the result is just further confirmation that there can be no word for het, since

$$\nsim D(v, G),$$

asserts that the arbitrarily chosen word, $v$, does not denote the first level propositional function, $G$. Any word for $G$ can be present only in some language farther along in the hierarchy of sublanguages of $\stL$.

### F.4 Tarski’s Theorem

Church points out that this result concerning (14) and (15) “is to be expected in light of Tarski’s theorem about truth”, and in note 28 towards the end of (1976), he indicates how a form of that theorem can be obtained for $\rL_1$.

For the following, it is best to keep in mind that unlike familiar uninterpreted first order languages, $\rL_1$ is a fully interpreted language. For example, the individual variables and unary predicates of $\rL_1$ range over the already fixed objects of type i and (i) respectively. The following wff of L2 is Church’s definition of truth for propositions of order 1—the propositions expressed by wff of type 0 of $\rL_1$:

$$\Tr^{2} (v) \rightarrow(\exists p^{0/1} ) \hdot \val^{2} (v,p) \cdot p,$$

Now replace $\het(x)$ in each of (14) and (15) by the predicate $\Tr^{2} (v)$ (a predicate of $\rL_2$). Assuming that $\rL_1$ and $\rL_2$ are consistent and that $\Tr^{2} (v)$ is true of exactly the true sentences of $\rL_1$, (15), so altered, asserts that there must be a propositional function in range of the unary propositional functions of $\rL_1$ that is coextensive with $\Tr^{2} (v)$, if that range is to be “extensionally complete” (1976; n. 26); but this together with (14), so altered, entails that no propositional form of $\rL_1$ in one free variable has the same extension as $\Tr^{2} (v)$. (Recall that the *sentences* of $\rL_1$, like all sentences, are individuals, so they can be values of $v$.) This is essentially Tarski’s theorem. In the second paragraph, Church stresses that (14) and (15) imply not only the indefinability of the extensional $\Tr^{2} (v)$ but also of the intensional $\het(x)$, and he hints that other semantical notions will turn out to be similarly indefinable.

Much of foregoing is prefigured in Church’s review (1950c) of a paper of Irving Copi’s claiming that RTT with reducibility is either inconsistent or redundant. But Copi assumes that it is possible without ado to add a name for the property of heterologicality to RTT and Church remarks that:

> To this it seems that the authors of Principia, at the time of the publication of their first edition, might have replied simply that from the existence of properties of a certain kind it does not necessarily follow that a particular such property can be named. (1950c: 221)

Church’s view seems to be no word for het can be a member of the domain of $D$ and no propositional form expressing het can be in the domain of Val.

In a final footnote of (1976), Church considers strengthening the system by adding principles (strengthening (4) and (11) to biconditionals) that seem to say that if a function is expressible (or nameable, as per $D)$ anywhere in the hierarchy, it is expressible (nameable) everywhere; and he thinks that this may result in a violation of Tarski’s resolution of the paradoxes. He nevertheless conjectures that the resulting system would be consistent.

Finally, we note that much earlier than (1976), in the hitherto unpublished (1949b), Church gives a demonstration of the derivability of GP within the elegant system (1940) of STT with axioms defining a denotation predicate. Church’s argument uses the devices of Gödel numbering and lambda abstraction, but it is essentially the same argument we have outlined above using a simpler language. But it is important to note that as regards *just* the derivation of Grelling’s paradox in STT, all of the account given in (1976) and in (1995a) was already available in (1949b). However, the important indefinability result of (1976), using the axioms of reducibility, is not present in (1949b). Nevertheless, Church (1949b) notes the similarity of his derivation of GP within STT and Tarski’s use of the liar paradox to derive the theorem on truth. In fact, from the contradiction resulting from Grelling’s paradox, Church (1949b) concludes that no word denotes the property of being heterological. This result is obtained without the help of reducibility since the underlying system is STT rather than RTT.

### F.5 Church’s Formal Analysis of RM

Church adds a symbol, here represented by $\sequiv$, for propositional identity and gives fifteen axioms and schemata providing, he insists, exactly what is required to derive RM in STT with $\sequiv$. In order to give a brief reconstruction of Church’s derivation, we will allow propositions of the form *proposition $p$ is in the class $m$* to play the role usually played by propositions of the form *every proposition in $m$ is true.* This allows us in principle to dispense with seven of the axioms. (Church notes this is possible.) We also leave the relevant comprehension principles ((5) and (6) of Church paper unstated. Church prefaces each step of his derivation with a sentence from Russell’s informally stated argument in Appendix B of *Principles of Mathematics*, so that

> what is being done is not a later imposition upon Russell of something he would not have recognized as his own thought. (1984 [BE: 817])

This wonderful detail must be omitted from the following.

The complications of Church’s presentation stem mainly from his desire to reduce Russell’s assumption that identical propositions must have identical constituents to its simplest terms. At one point, Church formulates this principle as a metalinguistic semantical principle concerning names—that names of different things give rise to sentences that express different propositions (1984 [BE: 819]), but his formalization does not rely on this principle. Instead, Structure is represented in the object language (Church’s 1a and 1b) asserting that if the proposition that *every proposition in $m$ is true* is the same as the proposition that *every proposition in $n$ is true*, then $n$ and $m$ are coextensive. In terms of the simpler propositions of the form *$p$ is in $m$*, the corresponding principle is the following:

$$\tag{1} \nsim(q) [ n(q) \equiv m(q)] \supset (p)(q) \nsim [n(p) \sequiv m(q)] $$

which asserts that if $n$ and $m$ are not coextensive, then the propositions $n(p)$ and $m(q)$ are never the same; or the contrapositive: if for some $p$ and $q$, $n(p)$ and $m(q)$ are the same, then $m$ and $n$ are coextensive. Church gives a separate proof from his axioms of (his version of) (1) using his axioms 3, 8 and 11. It is not clear that the same holds for the present version. Now, following Church’s steps 2 and 3 gives: (The bold type indicates the special role of $\stw$ and $\stp 0$ in the argument as emerges in the resolution of the paradox in terms of RTT. See below.)

$$\tag{2} \stw(r) \equiv_r (\exists m)(\exists q) [r \sequiv m(q) \cdot \nsim m(r)]$$ $$\tag{3} \stp 0 \sequiv \stw(s)$$

where s is any fixed proposition. (2) and (3) are hypotheses that are later discharged using the comprehension principles. That is, the existence of $\stw$ and $\stp 0$ is guaranteed by those principles. It is now possible to derive that $\stp 0$ and $\nsim \stp 0$ using the seemingly weak principle 1 and some of the other axioms. Assuming that $\stw(\stp 0)$, infer $\stw(s) \sequiv m(q) \cdot \nsim m(\stw(s))$. Then for $p' = \stw(s)$ and $q' = m(q)$, the negation of the consequent of (1) is satisfied and hence by contraposition, $\stw$ and $m$ are coextensive. So since $\nsim m(\stw(s))$, by (3), $\nsim m(\stp 0)$, and it follows that $\nsim w(\stp 0)$. (The argument relies on Church’s axiom 3, which gives propositional identity the usual properties of identity.) The proof from the assumption that $\nsim \stw(\stp 0)$ proceeds as usual. The Structure principle, (1), is not needed for this. The righthand side of (2) is satisfied by $\stw$ and $\stp 0$ and hence $w(\stp 0)$.

One might wonder why Church engaged in this more or less routine exercise. One important reason is that he thought that Russell’s structured propositions are needed in a Russellian (as opposed to a Fregean) analysis of statements of assertion and belief:

> If following the early Russell, we hold that the object of an assertion or of a belief is a proposition and then impose on propositions the strong conditions of identity which this requires…we therefore find no alternative except ramified type theory, with axioms of reducibility, and with axioms and axiom schemata 1–15 appropriately modified. (1984 [BE: 821)

Church observes that “the antinomy is immediately resolved by ramified type theory” and, moreover, that there is no reason to suppose that it is restored by reducibility (1984 [BE: 821]). RTT requires that in (2), $\stw$ must be of higher order than the quantified variable m and so the required equality of $\stw$ and $m$ is lost. Likewise, $\stp 0$ must be of higher order than $m(q)$ and so the required identity of the latter two is lost. In the last paragraphs, Church indicates how the axioms might be appropriately modified within the system of $r$-types of (1976) with reducibility.
