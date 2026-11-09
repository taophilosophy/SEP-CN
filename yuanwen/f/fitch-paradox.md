# Fitch’s Paradox of Knowability
**First published Mon Oct 7, 2002; substantive revision Wed May 7, 2025**

*Brogaard, Berit, Salerno, Joe*

Fitch’s paradox of knowability (aka the knowability paradox or Church-Fitch Paradox) concerns any theory committed to the thesis that all truths are knowable. Historical examples of such theories arguably include Michael Dummett’s semantic antirealism (i.e., the view that any truth is verifiable), mathematical constructivism (i.e., the view that the truth of a mathematical formula depends on the mental constructions mathematicians use to prove those formulas), Hilary Putnam’s internal realism (i.e., the view that truth is what we would believe in ideal epistemic circumstances), Charles Sanders Peirce’s pragmatic theory of truth (i.e., that truth is what we would agree to at the limit of inquiry), logical positivism (i.e., the view that meaning is giving by verification conditions), Kant’s transcendental idealism (i.e., that all knowledge is knowledge of appearances), and George Berkeley’s idealism (i.e., that to be is to be perceivable).

The operative concept of “knowability” remains elusive but is meant to fall somewhere between equating truth uninformatively with what God would know and equating truth naively with what humans actually know. Equating truth with what God would know does not improve intelligibility, and equating it with what humans actually know fails to appreciate the objectivity and discoverability of truth. The middle way, what we might call *moderate antirealism*, can be characterized logically somewhere in the ballpark of the knowability principle:

$$\tag{K Principle} \forall p(p \rightarrow \Diamond Kp), $$

which says, formally, for all propositions $p$, if $p$ then it is possible to know that $p$.

The great problem for the middle way is *Fitch’s paradox*. It is the proof that shows (in a normal modal logic augmented with the knowledge operator) that “all truths are knowable” entails “all truths are known”:

$$\tag{K Paradox} \forall p(p \rightarrow \Diamond Kp) \vdash \forall p(p \rightarrow Kp). $$

As such the proof does the interesting work in collapsing moderate anti-realism into naive idealism.

What’s the paradox? Timothy Williamson (2000b) says the knowability paradox is not a paradox; it’s an “embarrassment”––an embarrassment to various brands of antirealism that have long overlooked a simple counterexample. He notes it’s “an affront” to various philosophical theories, but not to common sense. Others disagree. The paradox isn’t that the Fitch proof swiftly threatens the middle way. It’s that the Fitch proof, employing minimal epistemic modal resources, collapses the middle way into the naive way. The paradox, as articulated in Kvanvig (2006) and Brogaard and Salerno (2008), is that moderate antirealism appears not to be expressible as a distinct thesis, logically weaker than naive idealism. That is interesting and troublesome independently of one’s attitude for or against moderate antirealism.

## 1. Brief History

The literature on the knowability paradox emerges in response to a proof first published by Frederic Fitch in his 1963 paper, “A Logical Analysis of Some Value Concepts.” Theorem 5, as it was there called, threatens to collapse a number of modal and epistemic differences. Let ignorance be the failure to know some truth. Then Theorem 5 collapses a commitment to contingent ignorance into a commitment to necessary ignorance. For it shows that the existence of truths in fact unknown entails the existence of truths necessarily unknown. Formally,

$$\tag{Theorem 5} \exists p(p \wedge \neg Kp) \vdash \exists p(p \wedge \neg \Diamond Kp). $$

The converse of Theorem 5 is trivial (since truth entails possibility), so Fitch goes most of the way toward erasing any logical difference between the existence of contingent ignorance and the existence of necessary unknowability.

It is however the contrapositive of Theorem 5 that is usually referred to as the paradox:

$$\tag{K Paradox} \forall p(p \rightarrow \Diamond Kp) \vdash \forall p(p \rightarrow Kp). $$

It tells us that if any truth can be known then it follows that every truth is in fact known.

The earliest version of the proof was conveyed to Fitch by an anonymous referee in 1945. In 2005 we discovered that Alonzo Church was that referee (Salerno 2009b)[^salerno-2009b]. His reports are published in their entirety in Church (2009). Fitch apparently did not take the result to be paradoxical. He published the proof in 1963 to avert a kind of “conditional fallacy” that threatened his informed-desire analysis of value. The analysis roughly says: $x$ is valuable to $s$ just in case there is a truth $p$ such that were $s$ to known $p$ then she would desire $x$. The existence of unknowable truths ultimately explains why he restricts the propositional variables to knowable propositions. For an unknowable truth provides for an impossible antecedent in Fitch’s counterfactual, and ultimately trivializes the analysis. Since Fitch’s theory of value is not the context in which the paradox is widely discussed, we will say no more about it here.

Rediscovered in Hart and McGinn (1976) and Hart (1979), the result was taken to be a refutation of verificationism, the view that all meaningful statements (and so all truths) are verifiable. After all, if one accepts the knowability principle, $\forall p(p \rightarrow \Diamond Kp)$, she is committed to the absurd claim that all truths are known. Mackie (1980) and Routley (1981), among others at the time, point to difficulties with this general position but ultimately agree that Fitch’s result is a refutation of the claim that all truths are knowable, and that various forms of verificationism are imperiled for related reasons. Since the early eighties, however, there has been considerable effort to analyze the proof as paradoxical. Why after all should it be that an epistemic theory of truth collapses possible knowledge into actual knowledge? Intuitively, that truth is to be understood in terms of the epistemic capacities of non-omniscient agents is at least a coherent position—a position distinct from and more plausible than the thesis that all truths are known. Moreover, it has been thought strange that sophisticated versions of the epistemic theory of truth should fall prey to such swift deduction. Hence, the Church-Fitch proof has come to be known as the *paradox* of knowability.

There is no consensus about whether and where the proof goes wrong. We use this entry to lay out the proof and explore a range of proposed treatments.

## 2. The Paradox of Knowability

Fitch’s reasoning involves quantifying into sentence position. Our propositional variables $p$ and $q$ will take declarative statements as substituends. Let $K$ be the epistemic operator ‘it is known by someone at some time that.’ Let $\Diamond$ be the modal operator ‘it is possible that’.

Suppose the knowability principle (KP)—that all truths are knowable by somebody at some time:

$$\tag{KP} \forall p(p \rightarrow \Diamond Kp). $$

And suppose that collectively we are non-omniscient, that there is an unknown truth:

$$\tag{NonO} \exists p(p \wedge \neg Kp). $$

If this existential claim is true, then so is an instance of it:

$$\tag{1} p \wedge \neg Kp. $$

Now consider the instance of KP substituting line 1 for the variable $p$ in KP:

$$\tag{2} (p \wedge \neg Kp) \rightarrow \Diamond K(p \wedge \neg Kp) $$

It follows trivially that it is possible to know the conjunction expressed at line 1:

$$\tag{3} \Diamond K(p \wedge \neg Kp) $$

However, it can be shown independently that it is impossible to know this conjunction. Line 3 is false.

The independent result presupposes two very modest epistemic principles: first, knowing a conjunction entails knowing each of the conjuncts. Second, knowledge entails truth. Respectively,

$$\begin{align} \tag{A} K(p \wedge q) &\vdash Kp \wedge Kq \\ \tag{B} Kp &\vdash p \end{align}$$

Also presupposed are two modest modal principles: first, all theorems are necessary. Second, necessarily $\neg p$ entails that $p$ is impossible. Respectively,

$$\begin{align} \tag{C} &\text{If } \vdash p, \text{then } \vdash \Box p. \\ \tag{D} &\Box \neg p \vdash \neg \Diamond p. \end{align}$$

Consider the independent result:

$$\begin{align} \tag{4} K(p \wedge \neg Kp) &\quad\text{Assumption [for reductio]} \\ \tag{5} Kp \wedge K\neg Kp &\quad\text{from 4, by (A)} \\ \tag{6} Kp \wedge \neg Kp &\quad\text{from 5, applying (B) to the right conjunct} \\ \tag{7} \neg K(p \wedge \neg Kp) &\quad\text{from 4-6, by reductio,} \\ &\quad\quad\text{discharging assumption 4} \\ \tag{8}\Box \neg K(p \wedge \neg Kp) &\quad\text{from 7, by (C)} \\ \tag{9}\neg \Diamond K(p \wedge \neg Kp) &\quad\text{from 8, by (D)} \end{align}$$

Line 9 contradicts line 3. So a contradiction follows from KP and NonO. The advocate of the view that all truths are knowable must deny that we are non-omniscient:

$$\tag{10} \neg \exists p(p \wedge \neg Kp). $$

And it follows from that that all truths are actually known:

$$\tag{11} \forall p(p \rightarrow Kp). $$

The ally of the view that all truths are knowable (by somebody at some time) is forced absurdly to admit that every truth is known (by somebody at some time).

## 3. Logical Revisions

In this section we inspect the prospects for treating Fitch’s reasoning as invalid. Is Fitch’s epistemic reasoning in order? Is the logic of knowability classical logic? More to the point: does the knowability principle carry with it special considerations that warrant the revision of classical logic? If so, does this logical revision invalidate Fitch’s reasoning? And if the reasoning is invalid, are there closely related paradoxes that threaten the knowability principle without violating the relevant logical standards?

### 3.1 Epistemic Revision

The problem with Fitch’s reasoning is not with either of the epistemic inferences A or B. Though some have argued that knowing a conjunction does not entail knowing the conjuncts (Nozick 1981)[^nozick-1981], Williamson (1993) and Jago (2010) have shown that versions of the paradox do not require this distributive assumption. And questions about the factivity of $K$ may be defused rather quickly, since related paradoxes emerge replacing the factive operator “It is known that” with a non-factive operators, such as ‘It is rationally believed that’ (Mackie 1980: 92; Edgington 1985: 558–559; Tennant 1997: 252–259; Wright 2000: 357)[^edgington-1985][^mackie-1980][^tennant-1997][^wright-2000].

Deep and interesting discussions of the epistemic operators and/or temporal analogs in the context of Fitch’s paradox appear in many papers. Burgess (2009) considers the temporal analogs. van Benthem (2004; 2009), van Ditmarsh, et al. (2012), Berto et al. (2021) and Holliday (2018) explore the problem in dynamic epistemic frameworks. Palczewski (2007), Kelp and Pritchard (2009), Chase et al. (2018), and Heylen (2018) consider non-factive notions of knowledge and knowability. Linsky (2009), Paseau (2008), Jago (2010), Carrara et al. (2011), and Rosenblatt (2014) debate the prospects for typing knowledge.

### 3.2 Intuitionistic Revision

Williamson (1982) argues that Fitch’s proof is not a refutation of anti-realism, but rather a reason for the anti-realist to accept intuitionistic logic. Owing to a verificationist (or constructivist) reading of negation and existential quantification, intuitionistic logic validates neither the elimination of double negation,

$$ \neg \neg p \vdash p, $$

nor the following quantifier exchange rule:

$$ \neg \forall x\P[x] \vdash \exists x\neg\P[x]. $$

Without double negation elimination one cannot derive Fitch’s conclusion ‘all truths are known’ (at line 11) from ‘there is not a truth that is unknown’ (line 10). Consider line 10,

$$ \neg \exists p(p \wedge \neg Kp). $$

From this we may intuitionistically derive

$$ \forall p\neg(p \wedge \neg Kp). $$

But notice without double negation elimination,

$$ \neg(p \wedge \neg Kp) $$

does not entail

$$ p \rightarrow Kp. $$

Suppose

$$ \neg(p \wedge \neg Kp) $$

and suppose $p$ for conditional introduction. And suppose $\neg Kp$ for *reductio*. We may conjoin $p$ with $\neg Kp$ to get

$$ p \wedge \neg Kp $$

This contradicts our primary assumption. So, by *reductio*, $\neg \neg Kp$. Without double negation elimination, we cannot conclude $Kp$, and so, may not introduce the conditional

$$ p \rightarrow Kp $$

The intuitionist is however committed, by conditional introduction, to

$$ p \rightarrow \neg \neg Kp. $$

There is some debate about whether this consequence is sufficiently troublesome, but the intuitionistic anti-realist takes solace in the fact that she is not committed to the blatantly absurd claim that all truths are known. Very interesting discussion concerning the hopes and dreams of intuitionistic anti-realism in this context appears in Murzi (2010; 2012), Murzi et al. (2009) and Zardini(2015).

### 3.3 Problems for Intuitionistic Revision

Since Fitch’s reasoning is intuitionistically valid through line 10, the intuitionist anti-realist must accept that no truths are unknown: $\neg \exists p(p \wedge \neg Kp)$. Arguably this is harmful enough, for it appears that the anti-realist cannot give credence to the truism that (individually and collectively) we are non-omniscient. Williamson responds that the intuitionist anti-realist may naturally express our non-omniscience as “not all truths are known”:

$$\tag{12} \neg \forall p(p \rightarrow Kp) $$

This claim is classically, but not intuitionistically, equivalent to the non-omniscience thesis,

$$ \exists p(p \wedge \neg Kp). $$

That is because in intuitionistic logic the quantifier exchange rule, $\neg \forall x\P[x] \vdash \exists x \neg\P[x],$ is not unrestrictedly valid. Importantly the expression of non-omniscience at line $12, \neg \forall p(p \rightarrow Kp)$, is only classically, and not intuitionistically, inconsistent with line $10, \neg \exists p(p \wedge \neg Kp)$. So the intuitionist anti-realist can consistently give expression to the truism that we are non-omniscient (with line 12) while accepting the intuitionistic consequence derived at line 10. In effect, the anti-realist admits both that no truths are unknown and that not all truths are known. The satisfiability of this claim on intuitionistic grounds is demonstrated by Williamson (1988, 1992).

### 3.4 The Undecidedness Paradox of Knowability

A deeper problem is said to remain for the intuitionist anti-realist. Fitch’s paradox rests on the assumption that there are unknown truths. But consider the intuitionistically weaker assumption that there are undecided statements, that is, some $p$, such that $p$ is unknown and $\neg p$ is unknown. Formally,

$$\tag{Und} \exists p(\neg Kp \wedge \neg K\neg p) $$

If (Und) is true, then so is an instance of it:

$$\tag{i} \neg Kp \wedge \neg K\neg p. $$

And notice that the intuitionistically acceptable conclusion at line $10, \neg \exists p(p \wedge \neg Kp)$, is intuitionistically equivalent to the universal claim,

$$\tag{ii} \forall p(\neg Kp \rightarrow \neg p). $$

Deriving $\neg Kp \rightarrow \neg p$ and $\neg K\neg p \rightarrow \neg \neg p$ from (ii), and applying the conjuncts of (i), respectively, gives us the contradiction $\neg p \wedge \neg \neg p$. The intuitionist anti-realist is forced to admit absurdly that there are no undecided statements:

$$\tag{iii} \neg \exists p (\neg Kp \wedge \neg K \neg p) $$

The above argument is given by Percival (1990: 185). Since it is intuitionistically acceptable, it is meant to show that the intuitionist anti-realist is still in trouble.

In reply, the anti-realist again may utilize Williamson’s strategy jointly to revise logic and reconstruct an expression of the epistemic truism. Embrace only the intuitionistic consequences of KP (in this case, that there are no undecided statements), and give expression to the truism about undecidedness by claiming that not all statements are decided:

$$\tag{iv} \neg \forall p(Kp \vee K\neg p). $$

The reinterpretation of the undecidedness intuition at line (iv) gives us a claim that is classically, but not intuitionistically, equivalent to Und. And so, it is only classically, and not intuitionistically, inconsistent with the inference at line (iii).

Related undecidedness paradoxes of knowability are discussed in Wright (1987: 311), Williamson (1988: 426) and Brogaard and Salerno (2002: 146–148). The undecidedness paradoxes give the anti-realist even further reason to revise classical logic in favor of intuitionistic logic. When accompanied by a reconstrual of our epistemically modest intuitions, logical space for anti-realism is reclaimed.

What all this suggests is that intuitionist anti-realism is coherent. But is the approach well motivated? Is either the revision of classical logic or the clever reconstrual of our epistemic intuitions *ad hoc*?

The anti-realist’s purported right to give up classical logic in favor of intuitionistic logic has been defended independently. The argument finds its roots in Dummett (1976, and elsewhere). More recent interpretations of the anti-realist’s argument for logical revision appear in Wright (1992: Chp. 2), Tennant (1997: Chp. 7), and Salerno (2000). The details and success or failure of the arguments for logical revision is a topic for another time. For now it is enough to point out that the threat of Fitch’s paradox is not the anti-realist’s sole motivation for favoring a non-classical logic.

What about the reconstrual of our epistemic intuitions? Is it well motivated? According to Kvanvig (1995) it is not. Why should we grant that the intuitionistic treatments of non-omniscience and undecidedness are better than our initial common-sense treatments? And how is the anti-realist to explain away the apparent triviality of these common-sense treatments? These questions have not been answered.

Moreover, some of the intuitionistic consequences of KP are thought to be bad enough. Even if ‘there are no unknown truths’ or ‘there are no undecided statements’ are intuitionistically tolerable, the following appears not to be: If $p$ is unknown then $\neg p$. Formally, $\neg Kp \rightarrow \neg p$. This claim follows intuitionistically from $p \rightarrow \neg \neg Kp$, which we have already established as an intuitionistic consequence of KP. But $\neg Kp \rightarrow \neg p$ appears to be false for empirical discourse. Why should the fact that nobody ever knows $p$ be sufficient for the falsity of $p$? See Percival (1990) and Williamson (1988) for further discussions of this and related problems surrounding the application of intuitionist anti-realism to empirical discourse. DeVidi and Solomon (2001) disagree. They argue that the intuitionistic consequences are not unacceptable to one interested in an epistemic theory of truth—indeed they are central to an epistemic theory of truth.

For these reasons an appeal to intuitionist logic, by itself, is generally taken to be unsatisfying in dealing with the paradoxes of knowability. Exceptions include Burmüdez (2009), Dummett (2009), Rasmussen (2009) and Maffezioli, Naibo & Negri (2013).

### 3.5 Paraconsistent Revision

Another challenge to the logic of Fitch’s paradox is mentioned in Routley (1981) and defended by Beall (2000). The thought is that the correct logic of knowability is paraconsistent. In a paraconsistent logic contradictions do not trivialize a theory, because they do not ‘explode’. That is, in a paraconsistent logic the inference from $p \wedge \neg p$ to an arbitrary conclusion $r$ is not valid. Owing to this consideration some contradictions are permitted and thought to be possible.

Beall contends that (1) Fitch’s proof turns on the assumption that, for all statements $p$, the contradiction $Kp \wedge \neg Kp$ is impossible and (2) we have independent evidence for thinking $Kp \wedge \neg Kp$, for some $p$. The independent evidence lies in the [paradox of the knower](https://plato.stanford.edu/entries/epistemic-paradoxes/#KnoPar) (not to be mistaken with the paradox of knowability). The relevant version of the knower paradox may be demonstrated by considering the following self-referential sentence:

$$\tag{\(k\)} k \text{ is unknown.} $$

Assume for the sake of argument that $k$ is known. Then, presuming that knowledge entails truth, $k$ is true. But $k$ says that $k$ is unknown. So $k$ is unknown. Consequently, $k$ is both known and unknown. But then our assumption (i.e., that $k$ is known) is false, and provably so. And, granting that a proven falsehood is known to be false, it follows that it is known that $k$ is unknown. That is to say, it is known that $k$. But we have already shown that if it is known that $k$ then $k$ is both known and unknown. So it is proven that $k$ is both known and unknown. It is provably the case that the full description of our knowledge includes both $K(k)$ and $\neg K(k)$. That is the knower paradox.

Beall suggests that the knower gives us some independent evidence for thinking $Kp \wedge \neg Kp$, for some $p$, that the full description of human knowledge has the interesting feature of being inconsistent. With a paraconsistent logic, one may accept this without triviality. And so it is suggested that one go paraconsistent and embrace $Kp \wedge \neg Kp$ as a true consequence of the knowability principle. Beall concludes that Fitch’s reasoning, without a proper reply to the knower, is ineffective against the knowability principle. For Fitch’s reasoning allegedly turns on the assumption that, for all $p$, it is impossible that $Kp \wedge \neg Kp$.

Notice that our presentation of Fitch’s reasoning makes no explicit mention of the assumption that $Kp \wedge \neg Kp$ is impossible. So here we attempt to pinpoint exactly where Fitch’s reasoning goes wrong on the above account. It is claimed at line 9 (in the first section of this entry) that $K(p \wedge \neg Kp)$ is impossible. Of course $K(p \wedge \neg Kp)$ entails the contradiction $Kp \wedge \neg Kp$. And so, if the reasoning is that $K(p \wedge \neg Kp)$ is impossible because contradictions are impossible, then Beall would be directly attacking the argument presented herein. But notice the argument here is subtly different. It goes like this. $K(p \wedge \neg Kp)$ entails the contradiction $Kp \wedge \neg Kp$. So, by *reductio*, $K(p \wedge \neg Kp)$ is false. By necessitation, it follows that $K(p \wedge \neg Kp)$ is necessarily false. Depending on the paraconsistent logic, the paraconsistist may object to use of reductio, or may object to other inferences. The claim that $K(p \wedge \neg Kp)$ is impossible (at line 9) is inferred from this claim that $K(p \wedge \neg Kp)$ is necessarily false. This may trouble the paraconsistentist. By the lights of one living with contradiction, it may not follow that an inconsistent statement is impossible even if it is necessarily false. After all, on this account a necessarily false statement may be both false and true at some world, in which case the statement is both necessarily false and possible. If this is right then the inference from $\Box \neg p$ to $\neg \Diamond p$ has counterexamples and may not be employed to infer $\neg \Diamond K(p \wedge \neg Kp)$ from $\Box \neg K(p \wedge \neg Kp)$.

Beall’s insights turn on a number of things: (1) the strength of the independent evidence for true epistemic contradictions, (2) the adequacy of the proposed resolutions to the knower paradox, (3) the question of whether Fitch’s reasoning is ineffective without a resolution to the knower and (4) an interpretation for $\Box$ and $\Diamond$ that invalidates the relevant inference (from $\Box \neg p$ to $\neg \Diamond p)$ while remaining true to the role played by $\Diamond$ in the knowability principle. We leave these problems for further debate. But compare with Wansing (2002), where a paraconsistent constructive relevant modal logic with strong negation is proposed to block the paradox.

More recent developments of the paraconsistent approach appear in Beall (2009) and Priest (2009).

## 4. Semantic Restrictions

The remainder of proposals are restriction strategies. They reinterpret KP by restricting its universal quantifier. In effect, the restriction strategies invalidate Fitch’s reasoning by prohibiting the substitution-instances of KP that lead to paradox. In this section we examine semantic reasons for restricting the universal quantifier in KP.

### 4.1 Situations and Rigid Operations

Edgington (1985) offers a situation-theoretic diagnosis of Fitch’s paradox. She claims that the problem lies with the failure to distinguish between ‘knowing in a situation that $p$’ and ‘knowing that $p$ is the case in a situation’. In the latter case, the situation is (at least in part) that which the knowledge is about. In the former case, the situation is that in which the knowledge is had. For instance, I may know in my actual situation that I would be in pain in a counterfactual situation where my tooth is pulled. Importantly, the situation in which the knowledge takes place may be different from the situation that my knowledge is about. In a situation in which my tooth is *not* pulled, I may know things that are about a situation in which my tooth is pulled.

What are situations? The above example seems to suggest that situations are worlds. But situations may be less complete than worlds. That is, they need not have truth-values fixed for statements that are irrelevant to the context. Consider an example by Linstöm: I may know in a given perceptual situation $s$ that John (one of the participants of a card game) has the best hand and that none of the participants knows this. In this case my knowledge is of one situation $s^*$, the card game, but my knowledge is acquired in a different situation $s$, my perceptual situation. Situation $s^*$ is not only determined, but its relevant information is limited, by the context of the card game. And $s$ is fixed and limited by the context of the perceptual situation. Edgington prefers talk of situations rather than worlds, because knowledge of non-actual situations, unlike knowledge of non-actual worlds, does not require knowledge of an infinite amount of detail.

Making explicit the situation-theoretic distinction between ‘knowing in’ and ‘knowing about’, we may reinterpret the knowability principle: for each statement $p$ and situation $s$, if $p$ is true in $s$ then there is a situation $s^*$ in which it is known that $p$ is true in $s$. Edgington requires of knowability the less general thesis: if $p$ is true in an actual situation $s$ then there is a possible situation $s^*$ in which it is known that $p$ is true in $s$. Call this E-knowability or EKP:

$$\tag{EKP} \A p \rightarrow \Diamond K\A p, $$

where A is the actuality operator which may be read ‘In some actual situation’, and $\Diamond$ is the possibility operator to be read ‘In some possible situation’.

As we see, EKP restricts the knowability principle to actual truths, by saying $p$ is actually true only if there is a possible situation in which it is known that $p$ is actually true.

The important suggestion is this. Just as there may be actual knowledge of what is counterfactually the case, there may be counterfactual knowledge of what is actually the case. In fact, in light of Fitch’s proof, E-knowability requires the existence of such non-actual knowledge. Let us see why.

Actual truths of the form $p \wedge \neg Kp$ will have to be E-knowable. But $p \wedge \neg Kp$ cannot be actually known to be actually the case. The reasoning here is exactly analogous to Fitch’s reasoning.

The lesson is this. Since, for some $p, p \wedge \neg Kp$ is actually the case, E-knowability commits us to possible knowledge that $p \wedge \neg Kp$ is actually the case. Since this knowledge cannot be actual, E-knowability requires non-actual knowledge of what is actually the case. E-knowability then denies the following assumption: given a statement $p$, if it is known that $p$ in $s$, then in $s$ it is known that $p$. By Edgington’s analysis it is exactly this implicit assumption that leads Fitch’s reasoning astray. The paradox is blocked without it.

### 4.2 Problems for Situations

Since the actuality operator *rigidly* designates actual situations, the truth-value of statements of the form $\A p$ will not vary across possible situations. ‘$\A p$’ entails ‘in every situation $\A p$’. Thus, as Edgington is aware, if $\A p$ then it is necessary that $\A p$. This by itself poses a problem for EKP. The criticism is that Edgington’s approach is not general enough. Anyone who is likely to endorse the knowability principle is likely to think that it holds of all truths, not just those necessary truths involving the actuality operator. EKP appears to be a very limited thesis failing to specify an epistemic constraint on contingent truth (Williamson 1987a)[^williamson-1987a].

Further criticisms emerge when we attempt to say something informative about what constitutes non-actual knowledge of what is actually the case, so-called transworld knowability. If there is such non-actual knowledge, there is non-actual thought about an actual situation. So the non-actual thinker somehow has a concept of an actual situation. But how is it possible for a non-actual thinker to have a concept that is specifically about situations in this the actual world. It will not do for the thinker to express the thought ‘actually $p$’, since ‘actually’ will designate rigidly only situations in her own world. Moreover, since there is no causal link between the actual world $w_1$ and the relevant non-actual world $w_2$, it is unclear how non-actual thought in $w_2$ can be uniquely about $w_1$ (Williamson, 1987a: 257–258). Therefore, it is unclear how there might be non-actual knowledge about what is actually the case.

Of course actual knowledge about the non-actual is no better at singling out worlds. The special problem for the non-actual knower is that the content of her thought must be precisely the content that we grasp when we consider the truth of $\A p$. Being in the actual world we are able to single out this world uniquely. When we consider the truth of $\A p$ our context fixes the content of A specifically. So if it really is $\A p$ that is knowable by a non-actual knower, then it must be $\A p$ that she grasps—that is, it must be the very same concept that we grasp. But how this is possible is precisely the problem.

Related and additional criticisms of Edgington’s proposal appear in Wright (1987), Williamson (1987b; 2000b) and Percival (1991). Formal developments on the proposal, including points that address some of these concerns appear in Rabinowicz and Segerberg (1994), Lindström (1997), Rückert (2003), Edgington (2010), Fara (2010), Proietti and Sandu (2010), and Schlöder (2019).

Version of Edgington-style proposals involving actuality operators include Fuhrmann 2014, and Schlöder 2019. Fuhrmann argues that there is a plausible concept of knowability (one not decomposable into more basic possibility and knowledge operators) that evades the paradox. The proposal is related to a family of proposals, including Edgington’s, that utilize actuality operators to avoid the paradox. A benefit of Fuhrmann’s proposal is said to be that it does not involve transworld-knowability. Schlöder offers a refined understanding of counterfactual knowability that is grounded in possible courses of inquiry. There to we find a Edgington-like proposal that aims to avoid trans-world knowability concerns.

### 4.3 Modal Fallacies and Non-Rigid Statements

Kvanvig (1995) accuses Fitch of a modal fallacy. The fallacy is an illicit substitution into a modal context. Consider a familiar modal fallacy. For all persons $x$, there is a possible world in which $x$ is not the inventor of bifocals. (Even Ben Franklin, the actual inventor of bifocals, might not have invented them.) Therefore, there is a possible world in which the inventor of bifocals is not the inventor of bifocals. We can represent the argument formally. Let our quantifiers range over persons, and let ‘$i$’ be the non-rigid designator ‘the inventor of bifocals’. Consider the argument:

$$\begin{align*} &\forall x \Diamond \neg(x = i) \\ &\quad\text{Therefore,} \\ &\Diamond \neg(i = i) \end{align*}$$

Although anyone might not have been the inventor of bifocals, it does not follow (in fact it is false) that it is possible that the inventor of bifocals is not identical to the inventor of bifocals. After all, it is necessary that the inventor of bifocals is the inventor of bifocals.

The lesson is that we may not substitute unrestrictedly into modal contexts. Substitution into modal contexts, we might say, is permitted only if the substituting terms are rigid designators. In the case of Fitch’s result, our terms are sentences. The knowability principle, $\forall p(p \rightarrow \Diamond Kp)$, apparently allows us to substitute any sentence whatsoever for $p$. But notice that our quantifier has wide scope relative to $\Diamond$. We would expect that the lessons of quantified modal logic carry over to quantified propositional modal logic. If so, then we may not substitute for $p$ any statement that does not designate rigidly.

On Kvanvig’s diagnosis, the problem with Fitch’s reasoning is that when he substituted the conjunction $p \wedge \neg Kp$ for $p$ in KP (at line 2 of the result), he did not stop to determine whether $p \wedge \neg Kp$ is rigid. Kvanvig maintains that $p \wedge \neg Kp$ is not rigid. So Fitch’s result is fallacious owing to an illicit substitution into a modal context. But we may reconstrue $p \wedge \neg Kp$ as rigid. And when we do, the paradox evaporates.

Kvanvig proposes that quantified expressions are non-rigid. The reason he gives is that quantifiers designate different objects in different possible worlds. “Everyone in Jon’s Logic class must take the final” is about different students in different possible worlds. Were Sussie to have taken the class, the expression would have been about her. But she decided not to take the class, so actually it is not about her. $Kp$ is an abbreviation for ‘it is known by somebody at some time that $p$.’ So, $Kp$ is implicitly quantified. Explicitly it reads $\exists x\exists t(Kxpt),$ which says there is a being $x$ and a time $t$ such that $x$ knows that $p$ at $t$. Accordingly, on this account, the quantified expression that $Kp$ abbreviates is non-rigid. $\exists x\exists t(Kxpt)$ is about different beings and times in different modal contexts. For instance, the expression $\exists x\exists t(Kxpt)$ is about actual beings and times. But embedded in a modal context, e.g., $\Diamond \exists x\exists t(Kxpt),$ the expression is about possible beings and times. It says, ‘there is a possible world in which there is a being $x$ and time $t$ such that $x$ knows that $p$ at $t$.’

Now consider the relevant instance of Fitch’s non-omniscience thesis: $p \wedge \neg Kp$. Unabbreviated it reads, $p \wedge \neg \exists x\exists t(Kxpt),$ which says $p$ is true but nobody ever knows that $p$. The quantified expression is, on this view, a non-rigid designator. Uttered in the actual world, it is about actual beings and times. But, it is argued, embedded within the scope of a possibility operator the designation varies to be about possible beings and times. When Fitch substituted the true conjunction, $p \wedge \neg \exists x\exists t(Kxpt),$ for $p$ in the knowability principle, he substituted for $p$ a non-rigid designator, thereby altering the reference of the conjunction and perpetrating a modal fallacy.

Alternatively, Kvanvig suggests, we may characterize $Kp$ rigidly to say, ‘there is an actual being $x$ and actual time $t$ such that it is known by $x$ at $t$ that $p$.’ Since this expression designates rigidly (i.e., it makes reference to the actual world regardless of the modal context in which it appears), it may be substituted for $p$ in the knowability principle. The reinterpreted conjunction does not change its designation when embedded within the scope of $\Diamond$. Moreover, on this reading of the conjunction, the paradox dissolves. It is possible to know that the reinterpreted conjunction is true. There is no contradiction in supposing that some possible being at some possible time knows that $p$ is true but never known by an actual being at an actual time. The paradox dissolves.

Further discussion of modal fallacies and non-rigid statements appears in Brogaard and Salerno (2008) and Kennedy (2014).

### 4.4 Problems for Non-Rigidity

Williamson (2000b) defends Fitch’s reasoning against Kvanvig’s charge. He suggests that Kvanvig has no grounds for thinking that Fitch’s conjunction $p \wedge \neg \exists x\exists t(Kxpt)$ does not designate rigidly. The reason Williamson gives is this. An expression is non-rigid if, when uttered in a fixed context, it varies its reference with the circumstances under which it is evaluated. But Kvanvig gives no convincing reason for thinking that Fitch’s conjunction, as uttered in a fixed context, varies its reference in this way. At best Kvanvig has shown that the conjunction varies its reference when uttered in *varying* contexts, since his argument is that a quantified sentence, when uttered at different worlds, will be about different objects. To think that this is sufficient for non-rigidity, Williamson complains, is to confuse non-rigidity for indexicality. Importantly, indexicality does not imply non-rigidity. For instance, ‘I am tired’ is about me, and continues to be about me when I evaluate its truth-value in counterfactual circumstances. The sentence might have been false. Had I gotten enough sleep, I would not be tired. Uttered in a fixed context, ‘I’ rigidly designates, even though it is an indexical. That is, even though, had it been uttered in a different context by somebody else, it would have been about somebody other than me. Analogously, even if quantified expressions are indexicals, it does not follow that they are non-rigid. And so, even if Fitch’s conjunction is an indexical expression, we have not been given a reason to think that it is non-rigid. If this is correct, then we have no grounds for thinking that Fitch has committed the modal fallacy in question.

Kvanvig (2006) replies and develops other interesting themes in the *Knowability Paradox*, which is the only monograph to date dedicated to the topic.

## 5. Syntactic Restrictions

The foregoing restriction strategies involved semantic reasons for limiting universal quantification. In those cases, KP was restricted in light of considerations about situations, possible worlds, or rigid designation. Another kind of restriction strategy is syntactic. It limits the scope of universal quantification to those formulas that have a certain logical form or stand in a certain provability relation. Most generally,

$$ p \rightarrow \Diamond Kp, \text{ where } p \text{ has logical property } F. $$

$F$ should then be a logical property that restricts the quantifier in some principled way.

### 5.1 Cartesian Statements

Tennant (1997) focuses on the property of being Cartesian: A statement $p$ is Cartesian if and only if $Kp$ is not provably inconsistent. Accordingly, he restricts the principle of knowability to Cartesian statements. Call this restricted knowability principle T-knowability or TKP:

$$\tag{TKP} p \rightarrow \Diamond Kp, \text{ where } p \text{ is Cartesian.} $$

Notice that T-knowability is free of the paradoxes that we have discussed. It is free of Fitch’s paradox and the related undecidedness paradox. For both results substitute the problematic Fitch conjunction, $p \wedge \neg Kp$, for the variable in $p \rightarrow \Diamond Kp$, giving us $(p \wedge \neg Kp) \rightarrow \Diamond K(p \wedge \neg Kp)$. That is, they require that $p \wedge \neg Kp$ be knowable if true (line 2 of Fitch’s result). But $p \wedge \neg Kp$ is not Cartesian, since $K(p \wedge \neg Kp)$ is provably inconsistent (entailing the contradiction at line 6 of Fitch’s result). In effect, TKP offers the most tolerant restriction needed to prohibit the bothersome substitution. For it only prohibits substituting those statements for which it is logically impossible to know.

### 5.2 Basic Statements

Dummett (2001) agrees that the knowability theorist’s error lies in providing a blanket, rather than a restricted, knowability principle. And he agrees that the restriction should be syntactic. Dummett restricts the principle of knowability to “basic” statements and characterizes truth inductively from there. For Dummett,

$$\begin{array}{ll} p & \text{iff } \Diamond Kp, \text{ where } p \text{ is basic.} \\ p \text{ and } q &\text{iff } p \wedge q; \\ p \text{ or } q &\text{iff } p \vee q; \\ \text{if } p \text{ then } q &\text{iff } p \rightarrow q; \\ \text{it is not the case that } p &\text{iff } \neg p; \\ F[\text{Something}] &\text{iff } \exists x F[x]; \\ F[\text{Everything}] &\text{iff } \forall x F[x], \end{array}$$

where the logical constant on the right-hand side of each biconditional clause is understood as subject to the laws of intuitionistic logic.

Dummett’s knowability principle or DKP, like Tennant’s, is not threatened by the knowability paradoxes, and for the same reason. It restricts the class of statements that are subject to knowability. For Dummett’s case, the problematic Fitch conjunction, $p \wedge \neg Kp$, being compound, and so not basic, cannot replace the variable in $p \rightarrow \Diamond Kp$. The paradox is consequently averted.

### 5.3 Problems for the Syntactic Restrictions

The relative merits of these two restrictions are weighed by Tennant (2002). Tennant’s restriction is the less demanding of the two, since it bars only the substitution of those statements that are logically unknowable, and so, only those statements that are responsible for the paradoxes. Dummett’s restriction, by comparison, bars not only the substitution of these propositions, but also the substitution of logically complex proposition that are clearly knowable. Tennant also points out, if the knowability principle is the primary anti-realist motivation for revising classical logic, restricting that principle to basic statements can undermine arguments against a classical treatment of complex statements.

The main objections to the restriction strategies fall into two camps. In the first camp we find the charge that a given syntactic restriction on the knowability principle is not principled. From the second camp arise formulations of Fitch-like paradoxes that are not averted by the syntactic restrictions on knowable truth.

From the first camp Hand and Kvanvig (1999) protest that TKP has not been restricted in a principled manner—in effect, that we have been given no good reason, other than the threat of paradox, to restrict the principle to Cartesian statements. (An analogous claim may be made of Dummett’s DKP.) Tennant (2001b) replies to Hand and Kvanvig with general discussion about the admissibility of restrictions in the practice of conceptual analysis and philosophical clarification. By drawing analogies between his own restriction and others that are clearly admissible, he maintains that the Cartesian restriction is not *ad-hoc*. He also points out that TKP, rather than the unrestricted KP, serves as the more interesting point of contention between the semantic realist and anti-realist. The realist believes that it is possible for truth to be unknowable in principle. Fitch’s reasoning, at best, shows us that there is structural unknowability, that is, unknowability that is a function of logical considerations alone. But is there a more substantial kind of unknowability, for instance, unknowability that is a function of the recognition-transcendence of the non-logical subject-matter? A realist decrying the *ad hoc* nature of TKP (or DKP) fails to engage the knowability theorist at the heart of the realism debate.

Other complaints that Tennant’s restriction strategy is not principled appear in DeVidi and Kenyon (2003) and Hand (2003). Hand offers a way of restricting knowability in a principled manner.

These concerns may be waived upon noticing versions of the paradox that do not violate the proposed restrictions on the knowability principle. Williamson (2000a) asks us to consider the following paradox. Let $p$ be the decidable sentence ‘There is a fragment of Roman pottery at that spot.’ Let $n$ rigidly designate the number of books actually now on my desk. Let $E$ be the predicate ‘is even.’ Williamson constructs the conjunction,

$$ p \wedge(Kp \rightarrow En), $$

and contends that it is Cartesian. Knowing it, apparently, does not entail a contradiction. If he is right, we can apply to it TKP, giving

1. $(p \wedge(Kp \rightarrow En)) \rightarrow \Diamond K(p \wedge(Kp \rightarrow En))$.

Additionally, if $p$ is true and $Kp$ is false, then Williamson’s conjunction is true. So,

1. $(p \wedge \neg Kp) \rightarrow(p \wedge (Kp \rightarrow En))$.

Lines (1) and (2) yield

1. $(p \wedge \neg Kp) \rightarrow \Diamond K(p \wedge(Kp \rightarrow En))$.

Accepting the modest epistemic resources found in Fitch’s reasoning, one can prove the following theorem:

1. $K(p \wedge(Kp \rightarrow En)) \rightarrow En$.

Here is why. A conjunction is known only if its conjuncts are known. So, if $K(p \wedge(Kp \rightarrow En))$, then $Kp$. And only truths can be known. So, if $K(p \wedge(Kp \rightarrow En))$, then $Kp \rightarrow En$. Of course, $Kp$ and $Kp \rightarrow En$ jointly entail $En$. So theorem 4 is valid, if Fitch’s epistemic resources are. Now, 4 is a theorem, and so, holds in all possible worlds. So its consequent is possible if its antecedent is possible:

1. $\Diamond K(p \wedge(Kp \rightarrow En)) \rightarrow \Diamond En$.

From lines 3 and 5 we derive

1. $(p \wedge \neg Kp) \rightarrow \Diamond En$.

Since $n$ designates rigidly, it is not contingent whether $n$ is even. It follows then that line 6 yields

1. $(p \wedge \neg Kp) \rightarrow En$.

An analogous argument replacing ‘odd’ for ‘even’ gives us

1. $(p \wedge \neg Kp) \rightarrow \neg En$.

But then we have a contradiction resting on TKP and Fitch’s conjunction, $p \wedge \neg Kp$. The result involves substitutions of $p \wedge(Kp \rightarrow En)$ and $p \wedge(Kp \rightarrow \neg En)$ for $p$ in TKP, but Williamson maintains that neither violate the Cartesian restriction. Paradox regained.

Tennant (2001a) takes issue with Williamson’s claim that $p \wedge(Kp \rightarrow En)$ is Cartesian. In the case where $n$ is odd, $En$ expresses a necessary falsehood (for instance, ‘13 is even’). But then, line 4 tells us that $K(p \wedge(Kp \rightarrow En))$ implies something that is necessarily false. And if the falsity of ‘13 is even’ is a matter of *logical* necessity, then $p \wedge(Kp \rightarrow En)$ cannot be consistently known and therefore is not Cartesian. Hence, when $n$ is odd, the first part of Williamson’s proof (involving the predicate ‘is even’) does in fact violate the Cartesian restriction. By contrast, Williamson’s conjunction is Cartesian when $En$ is true. But, analogously, if the truth of $En$ is a matter of logical necessity, then $p \wedge(Kp \rightarrow \neg En)$ cannot be consistently known and is therefore not Cartesian. Hence, when $n$ is even, the second part of Williamson’s proof (involving the predicate ‘is odd’) violates the Cartesian restriction. Either way, Tennant argues, Williamson has not shown that TKP is an inadequate treatment of Fitch’s paradox.

The debate continues in Williamson (2009) and Tennant (2010).

Brogaard and Salerno (2002) develop other Fitch-like paradoxes against the restriction strategies. Note that Dummett’s knowability principle is a biconditional: $p \leftrightarrow \Diamond Kp$, where $p$ is basic. Tennant (2002) agrees that the knowability principle should preserve the factive nature of $\Diamond$K. So Brogaard and Salerno begin with the following strengthened knowability principle:

$$\begin{align}\tag{SKP} p \leftrightarrow \Diamond Kp,\,&\text{where } p \text{ satisfies the} \\ &\text{relevant syntactic condition} \end{align}$$

Moreover, pending further discussion of the logic of $K$, it is not implausible that the intuitionist knowability theorist wishes to validate the KK-principle:

$$\tag{KK} \Box(Kp \rightarrow KKp). $$

The principle says, necessarily, if $p$ is known then it is known that $p$ is known. One other resource is used, namely, the closure principle which says that the antecedent of a necessary conditional is possible only if the consequent is possible.

If these commitments are granted, one can derive Fitch’s result without violating Tennant’s Cartesian restriction:

$$\begin{array}{lll} 1. & p \wedge \neg Kp & \text{Assumption (Fitch conjunction)} \\ 2. & Kp \rightarrow KKp & \text{from KK} \\ 3. & p \rightarrow \Diamond Kp & \text{from SKP (left-to-right)} \\ 4. & \Diamond Kp & \text{from 1 and 3} \\ 5. & \Diamond KKp & \text{from 4 and 2, by closure} \\ 6. & \Diamond KKp \rightarrow Kp & \text{from SKP (right-to-left)} \\ 7. & Kp & \text{from 5 and 6} \\ 8. & Kp \wedge \neg Kp & \text{from 1 and 7} \end{array}$$

SKP is applied at lines 3 and 6 to $p$ and $Kp$, respectively. And these substituends do not violate the Cartesian restriction. Neither $Kp$, nor $KKp$, is self-contradictory. Nonetheless, the anti-realist is forced absurdly to admit that no truth is unknown.

Arguably, this result threatens Dummett’s restricted knowability principle as well. But that depends on whether we have applied the principle to basic statements only. $p$ is basic, but Dummett’s characterization of truth underdetermines the status of $Kp$. Perhaps it is basic, since $Kp$ is not truth-functionally complex. Nonetheless, the issue cannot be resolved without a discussion of $K$.

Brogaard and Salerno demonstrate other paradoxes against the restriction strategies. Those further results do not presuppose a commitment to the KK-principle. They hinge ultimately on the knowability theorist’s interpretation of $\Diamond$. When $\Diamond$ is metaphysical possibility or governed by a logic at least as strong as S4, the strong knowability principle (appropriately restricted), and taken as a necessary thesis, entails that there are no unknown truths. When $\Diamond$ is epistemic possibility, and the knowability principle is treated as a necessary thesis that is known, the knowability principle entails that, necessarily, there are no undecided statements. Unlike the undecidedness paradoxes of Wright (1987), Williamson (1988), and Percival (1990), the reasoning provided by Brogaard and Salerno does not violate Tennant’s Cartesian restriction. A response to Brogaard and Salerno appears in Rosenkranz (2004). Further discussion of the Cartesian restriction appears in Brogaard and Salerno (2006, 2008). Tennant (2009) is a further development and defense of the Cartesian strategy. A defense of the restriction strategy appears in Fischer (2013).

Much of what has been written on the knowability paradox comes in the form of attempts to express the relevant form of anti-realism without paradox. Proposals include Chalmers (2012), Dummett (2009), Edgington (2010), Fara (2010), Hand (2009, 2010), Jenkins (2005), Kelp and Pritchard (2009), Linsky (2009), Hudson (2009), Restall (2009), Tennant (2009), Alexander (2013), Dean & Kurokawa (2010), Proietti (2016).

Chalmers (2002, 2012: chap. 2), for instance, defends the idea that given enough qualitative information about the world we could in principle know the truth value of any claim. More specifically, his *scrutability thesis* says, if $D$ is a complete qualitative description of the world, then for all $T$, it is knowable a priori that $D$ (materially) implies $T$. Importantly, the knowability paradox does not threaten the claim that true Fitch-conjunctions are derivable a priori from a complete description of the world.

Dummett takes $\forall p(p \rightarrow \neg \neg Kp)$ to be the best expression of his brand of anti-realism and embraces its intuitionistic consequences with open arms. Edgington defends her knowability principle (viz., if actually $p$ then it is possible to know that actually $p)$ by making the case for some transworld knowability—specifically, in those cases where the merely possible knower shares the relevant causal history with the actual world. Hand defends anti-realism by pointing to the distinction between a verification-type and its token performances, and argues that the existence of a verification-type doesn’t entail its performability. The lesson there is that the anti-realist should think about truth less in terms of the performability of verification procedures and more in terms of the existence of verification-types. And Linsky regiments the epistemic principles and reasoning with a theory of types. The debates surrounding the proper characterization of semantic anti-realism go far beyond the scope of this entry. As for the knowability proof itself, there continues to be no consensus on whether and where it goes wrong.

Niche discussions of the paradox that do not fit well into any of the above sections include Salerno’s (2018) new paradox of happiness; Kvanvig’s (2010) argument that the paradox threatens Christianity itself owing to its doctrine of the incarnation of Christ; and Cresto’s (2017) argument that the knowability paradox raises doubts about Reflection Principle as a requirement on rationality. Chalmers (2011) examines an argument that not even all a priori truths are knowable. His main argument is formulable in a modal propositional logic with epistemic and actuality operators.

Weng Kin San (2020) proposes a logically weakest formulation of the knowability paradox. His generalization of the result improves on our understanding of what minimally it takes to have a Church-Fitch knowability paradox, and widens the range of modalities to which the result applies.

Historical discussions, besides Salerno’s 2009b discussion of the original referee reports, include Stephenson 2015 (who discusses Fitch’s result in relation to Kant’s transcendental idealism), Kearns 2021 (in relation to Berkeley’s metaphysical idealism), and Bös 2024. Bös shows that Husserl’s theory of meaning and truth is potentially susceptible to a Church-Fitch paradox. However, he defends an interpretation of Husserl that restricts the theory of truth in a way that is similar to Dummett 2001. Replies are foreshadowed in light of familiar objections to Dummett’s proposal. Goodsell, Hawthorne, and Yli-Vakkuri forthcoming reconsider the paradox, when framed against of backdrop of Alonzo Church’s higher-order logic and “intensionalist” theory of propositions. They argue that the Church-Fitch result, as an anti-verificationist argument, does not survive in Church’s framework. However, the authors propose two new arguments against verificationism that are claimed to survive a joint commitment to Church’s higher-order logic and intensionalism.

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=fitch-paradox). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/fitch-paradox/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=fitch-paradox&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/fitch-paradox/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

- [Archival Documentation Page](https://sites.google.com/site/knowability/archival) (Lists unpublished material between 1945 and 1963 on Fitch’s paradox)
- [New Essays on the Knowability Paradox](https://sites.google.com/site/knowability/) (Contents Page)

[Please contact the authors with other suggestions.]

## Related Entries

logic: intuitionistic | logic: paraconsistent | realism | realism: challenges to metaphysical

[^alexander-2013]: Alexander, S., 2013. “An Axiomatic Version of Fitch’s Paradox,” *Synthese*, 190: 2015–2020.

[^beall-2000]: Beall, J.C., 2000. “Fitch’s Proof, Verificationism, and the Knower Paradox,” *Australasian Journal of Philosophy*, 78: 241–247.

[^beall-2009]: –––, 2009. “Knowability and Possible Epistemic Oddities,” in Salerno (ed.) 2009a, 105–125.

[^benthem-2004]: van Benthem, J., 2004. “What One May Come to Know,” *Analysis*, 64(2): 95–105.

[^bermüdez-2009]: Bermüdez, J., 2009. “Truth, Indefinite Extensibility, and Fitch’s Paradox, ” in Salerno (ed.) 2009a, 76–90.

[^berto-2021]: Berto, F., and P. Hawke, 2021. “Knowability Relative to Information,” *Mind*, 130(517): 1–33. doi.org/10.1093/mind/fzy045

[^berto-2009]: –––, 2009. “Actions that Make us Know,” in Salerno (ed.) 2009a, 129–146.

[^bös-2024]: Bös, G. E., 2024. “A Logical Challenge to Correlationism: the Church–Fitch Paradox in Husserl’s Account of Fulfilment, Truth, and Meaning,” *Synthese*, 203(6): 1–25.

[^brogaard-2009]: Brogaard, B., 2009. “On Keeping Blue Swans and Unknowable Facts at Bay: a Case Study on Fitch’s Paradox,” in Salerno (ed.) 2009a, 241–251.

[^brogaard-2002]: Brogaard, B., and J. Salerno, 2002. “Clues to the Paradoxes of Knowability: Reply to Dummett and Tennant,” *Analysis*, 62: 143–150.

[^brogaard-2006]: –––, 2006. “Knowability and a Modal Closure Principle,” *American Philosophical Quarterly*, 43: 261–270.

[^brogaard-2008]: –––, 2008. “Knowability, Possibility and Paradox,” in V. Hendricks and D. Pritchard (eds.), *New Waves in Epistemology*, New York: Palgrave Macmillan.

[^bueno-2009]: Bueno, O., 2009. “Fitch’s Paradox and the Philosophy of Mathematics,” in Salerno (ed.) 2009a, 252–280.

[^burgess-2009]: Burgess, J., 2009. “Can Truth Out?,” in Salerno (ed.) 2009a, 147–162.

[^carrara-2011]: Carrara, M., and D. Fassio, 2011. “Why Knowledge Should Not Be Typed: An Argument Against the Type Solution to the Knowability Paradox,” *Theoria*, 77: 180–193.

[^chalmers-2002]: Chalmers, D.J., 2002. “Does Conceivability Entail Possibility?,” in Gendler and Hawthorne (eds.), *Conceivability and Possibility*, Oxford: Oxford University Press.

[^chalmers-2011]: –––, 2011. “Actuality and Knowability,” *Analysis*, 71(3): 411–419.

[^chalmers-2012]: –––, 2012. *Constructing the World*, Oxford: Oxford University Press.

[^chase-2018]: Chase, J., and P. Rush, 2018. “Factivity, Consistency and Knowability,” *Synthese*, 195: 899–918.

[^church-2009]: Church, A., 2009. “Referee Reports on Fitch’s ‘A Definition of Value’,” in Salerno (ed.) 2009a, 13–20.

[^costa-leite-2006]: Costa-Leite, A., 2006. “Fusions of Modal Logics and Fitch’s Paradox,” *Croatian Journal of Philosophy*, 6: 281–90.

[^cozzo-1994]: Cozzo, C., 1994. “What We Can Learn from the Paradox of Knowability,” *Topoi*, 13: 71–78.

[^cresto-2017]: Cresto, E., 2017. “Lost in Translation: Unknowable Propositions in Probabilistic Frameworks,” *Synthese*, 194: 3955–3977.

[^dean-2010]: Dean, W., and H. Kurokawa, 2010. “From the Knowability Paradox to the Existence of Proofs,” *Synthese*, 176: 177–225.

[^devidi-2003]: DeVidi, D., and T. Kenyon, 2003. “Analogues of Knowability,” *Australasian Journal of Philosophy*, 81(4): 481–495.

[^devidi-2001]: DeVidi, D., and G. Solomon, 2001. “Knowability and Intuitionistic Logic,” *Philosophia*, 28: 319–334.

[^ditmarsch-2012]: van Ditmarsch, H., W. van der Hoek, and P. Iliev, 2012. “Everything is Knowable—How to Get to Know Whether a Proposition is True,” *Theoria*, 78: 93–114.

[^dummett-1959]: Dummett, M., 1959. “Truth,” *Proceedings of the Aristotelian Society*, 59: 141–162.

[^dummett-1975]: –––, 1975. “The Philosophical Basis of Intuitionistic Logi,c” in H. Rose and J. Shepherdson (eds.), *Logic Colloquium ’73*, Amsterdam: North-Holland.

[^dummett-1976]: –––, 1976. “What is a Theory of Meaning? (II),” in G. Evans and J. McDowell (eds.), *Truth and Meaning*, Oxford: Clarendon Press, Chapter 4.

[^dummett-2001]: –––, 2001. “Victor’s Error,” *Analysis*, 61: 1–2.

[^dummett-2009]: –––, 2009. “Fitch’s Paradox of Knowability,” in Salerno (ed.) 2009a, 51–52.

[^edgington-1985]: Edgington, D., 1985. “The Paradox of Knowability,” *Mind*, 94: 557–568.

[^edgington-2010]: –––, 2010. “Possible Knowledge of Unknown Truth,” *Synthese*, 173: 41–52.

[^fara-2010]: Fara, M., 2010. “Knowability and the Capacity to Know,” *Synthese*, 173: 53–73.

[^fischer-2013]: Fischer, M., 2013. “Some Remarks on Restricting the Knowability Principle,” *Synthese*, 190: 63–88.

[^fitch-1963]: Fitch, F., 1963. “A Logical Analysis of Some Value Concepts,” *The Journal of Symbolic Logic*, 28: 135–142; reprinted in Salerno (ed.) 2009a, 21–28.

[^fuhrmann-2014]: Fuhrmann, A., 2014. “Knowability as Potential Knowledge,” *Synthese*, 191(7): 1627–1648.

[^goodsell-nd]: Goodsell, Z., J. Hawthorne, and T. Yli-Vakkuri, forthcoming. “Unknowable truths,” *The Journal of Philosophy*.

[^hand-2003]: Hand, M., 2003. “Knowability and Epistemic Truth,” *Australasian Journal of Philosophy*, 81(2): 216–228.

[^hand-2009]: –––, 2009. “Performance and Paradox,” in Salerno (ed.) 2009a, 283–301.

[^hand-2010]: –––, 2010. “Antirealism and Universal Knowability,” *Synthese*, 173: 25–39.

[^hand-1999]: Hand, M., and J. Kvanvig, 1999. “Tennant on Knowability,” *Australasian Journal of Philosophy*, 77: 422–428.

[^hart-1979]: Hart, W. D., 1979. “The Epistemology of Abstract Objects: Access and Inference,” *Proceedings of the Aristotelian Society*, 53 (Supplementary): 153–165.

[^hart-2009]: –––, 2009. “Invincible Ignorance,” in Salerno (ed.) 2009a, 320–323.

[^hart-1976]: Hart, W. D., and C. McGinn, 1976. “Knowledge and Necessity,” *Journal of Philosophical Logic*, 5: 205–208.

[^heylen-2018]: Heylen, J., 2018. “Factive Knowability and the Problem of Possible Omniscience,” *Philosophical Studies*, 177: 65–87.

[^holliday-2018]: Holliday, W., 2018. “Knowledge, Time, and Paradox: Introducing Sequential Epistemic Logic,” in H. van Ditmarsch and G. Sandu (eds.), *Jaakko Hintikka on Knowledge and Game-Theoretical Semantics*, Berlin: Springer, 363–394.

[^hudson-2009]: Hudson, R., 2009. “Faint-Hearted Anti-realism and Knowability,” *Philosophia*, 37: 511–523.

[^jago-2010]: Jago, M., 2010. “Closure on Knowability,” *Analysis*, 70: 648–659.

[^jenkins-2005]: Jenkins, C., 2005. “Realism and Independence,” *American Philosophical Quarterly*, 42: 199–209.

[^jenkins-2009]: –––, 2009. “The Mystery of the Disappearing Diamond,” in Salerno (ed.) 2009a, 302–319.

[^kearns-2021]: Kearns, S., 2021. “The Bishop’s Church: Berkeley’s Master Argument and the Paradox of Knowability,” *Canadian Journal of Philosophy*, 51(3): 1–16.

[^kelp-2009]: Kelp, C., and D. Pritchard, 2009. “Two Deflationary Approaches to Fitch-Style Reasoning,” in Salerno (ed.) 2009a, 324–338.

[^kennedy-2014]: Kennedy, N., 2014. “Defending the Possibility of Knowledge,” *Journal of Philosophical Logic*, 43: 579–601.

[^kvanvig-1995]: Kvanvig, J., 1995. “The Knowability Paradox and the Prospects for Anti-Realism,” *Noûs*, 29: 481–499.

[^kvanvig-2006]: –––, 2006. *The Knowability Paradox*. Oxford: Oxford University Press.

[^kvanvig-2009]: –––, 2009. “Restriction Strategies for Knowability: Some Lessons in False Hope,” in Salerno (ed.) 2009a, 205–222.

[^kvanvig-2010]: –––, 2010. “The Incarnation and the Knowability Paradox,” *Synthese*, 173: 89–105.

[^lindström-1997]: Lindström, S., 1997. “Situations, Truth and Knowability: A Situation-Theoretic Analysis of a Paradox of Fitch,” in E. Ejerthed and S. Lindström (eds.), *Logic, Action and Cognition: Essays in Philosophical Logic*. Dordrecht: Kluwer Academic Publishers, 183–210.

[^linsky-2009]: Linsky, B., 2009. “Logical Types in Arguments about Knowability and Belief,” in Salerno (ed.) 2009a, 163–179.

[^mackie-1980]: Mackie, J. L., 1980. “Truth and Knowability,” *Analysis*, 40: 90–92.

[^maffezioli-2013]: Maffezioli, P., A. Naibo, and S. Negri, 2013. “The Church-Fitch Knowability Paradox in the Light of Structural Proof Theory,” *Synthese*, 190: 2677–2716.

[^melia-1991]: Melia, J., 1991. “Anti-Realism Untouched,” *Mind*, 100: 341–342.

[^murzi-2012]: Murzi, J., 2012. “Manifestability and Epistemic Truth,” *Topoi*, 31: 17–26.

[^murzi-2010]: –––, 2010. “Knowability and Bivalence: Intuitionistic Solutions to the Paradox of Knowability,” *Philosophical Studies*, 149: 269–281.

[^murzi-2009]: Murzi, J., and S. Florio, 2009. “The Paradox of Idealization,” *Analysis*, 69: 461–469.

[^nozick-1981]: Nozick, R., 1981. *Philosophical Explanations*, Cambridge, MA: Harvard University Press, Chapter 3.

[^palczewski-2007]: Palczewski, R., 2007. “Distributed Knowability and Fitch’s Paradox,” *Studia Logica*, 86: 455–478.

[^paseau-2008]: Paseau, A., 2008. “Fitch’s Argument and Typing Knowledge,” *Notre Dame Journal of Formal Logic*, 49: 153–176.

[^percival-1990]: Percival, P., 1990. “Fitch and Intuitionistic Knowability,” *Analysis*, 50: 182–187.

[^percival-1991]: –––, 1991. “Knowability, Actuality and the Metaphysics of Context-Dependence,” *Australasian Journal of Philosophy*, 69: 82–97.

[^priest-2009]: Priest, G., 2009. “Beyond the Limits of Knowledge,” in Salerno (ed.) 2009a, 93–104.

[^proietti-2016]: Proietti, C., 2016. “The Fitch-Church Paradox and First Order Modal Logic,” *Erkenntnis*, 81: 87–104.

[^proietti-2010]: Proietti, C., and G. Sandu, 2010. “Fitch’s Paradox and Ceteris Paribus Modalities,” *Synthese*, 173: 75–87.

[^rabinowicz-1994]: Rabinowicz, W., and K. Segerberg, 1994. “Actual Truth, Possible Knowledge,” *Topoi*, 13: 101–115.

[^rasmussen-2009]: Rasmussen, S., 2009. “The Paradox of Knowability and the Mapping Objection,” in Salerno (ed.) 2009a, 53–75.

[^rasmussen-1982]: Rasmussen, S. A., and J. Ravnkilde, 1982. “Realism and Logic,” *Synthese*, 52: 379–437.

[^restall-2009]: Restall, G., 2009. “Not Every Truth Can Be Known (at least, not all at once),” in Salerno (ed.) 2009a, 339–354.

[^rosenblatt-2014]: Rosenblatt, L., 2014. “The Knowability Argument and the Syntactic Type-Theoretic Approach,” *Theoria*, 80: 201–221.

[^rosenkranz-2004]: Rosenkranz, S., 2004. “Fitch Back in Action Again?,” *Analysis*, 64(1): 67–71.

[^routley-1981]: Routley, R., 1981. “Necessary Limits to Knowledge: Unknowable Truths,” in M. Edgar, N. Otto, and Z. Gerhard (eds.), *Essays in Scientific Philosophy. Dedicated to Paul Weingartner/Philosophie als Wissenschaft. Paul Weingartner gewidmet*, Bad Reichenhall: Comes Verlag, 93–115.

[^rückert-2003]: Rückert, H., 2003. “A Solution to Fitch’s Paradox of Knowability,” in Gabbay, Rahman, Symons, Van Bendegem (eds.), *Logic, Epistemology and the Unity of Science*, Dordrecht: Kluwer Academic Publishers.

[^salerno-2000]: Salerno, J., 2000. “Revising the Logic of Logical Revision,” *Philosophical Studies*, 99: 211–227.

[^salerno-2009a]: ––– (ed.), 2009a. *New Essays on the Knowability Paradox*, Oxford: Oxford University Press.

[^salerno-2009b]: –––, 2009b. “Knowability Noir: 1945–1963,” in Salerno (ed.) 2009a, 29–48.

[^salerno-2018]: –––, 2018. “Knowability and a New Paradox of Happiness,” in H. van Ditmarsch and G. Sandu (eds.), *Jaakko Hintikka on Knowledge and Game-Theoretical Semantics*, Berlin: Springer, 457–474.

[^san-2020]: San, W. K., 2020. “Fitch’s Paradox and Level-Bridging Principles,” *Journal of Philosophy*, 117(1): 5–29.

[^schlöder-2019]: Schlöder, J., 2019. “Counterfactual Knowability Revisited,” *Synthese*, 198(2): 1123–1137.

[^stephenson-2015]: Stephenson, A., 2015. “Kant, the Paradox of Knowability, and the Meaning of ‘Experience’,” *Philosophers’ Imprint*, 15(27), [available online](http://hdl.handle.net/2027/spo.3521354.0015.027).

[^tennant-1997]: Tennant, N., 1997. *The Taming of the True*, Oxford: Oxford University Press, Chapter 8.

[^tennant-2001a]: –––, 2001a. “Is Every Truth Knowable? Reply to Williamson,” *Ratio*, XIV: 263–280.

[^tennant-2001b]: –––, 2001b. “Is Every Truth knowable? Reply to Hand and Kvanvig,” *Australasian Journal of Philosophy*, 79: 107–113.

[^tennant-2002]: –––, 2002. “Victor Vanquished,” *Analysis*, 62, 135–142.

[^tennant-2009]: –––, 2009. “Revamping the Restriction Strategy,” in Salerno (ed.) 2009a, 223–238.

[^tennant-2010]: –––, 2010. “Williamson’s Woes,” *Synthese*, 173: 9–23.

[^wansing-2002]: Wansing, H., 2002. “Diamonds are a philosopher’s best Friend: The Knowability Paradox and Modal Epistemic Relevance Logic,” *Journal of Philosophical Logic*, 31(6): 591–612.

[^williamson-1982]: Williamson, T., 1982. “Intuitionism Disproved?,” *Analysis*, 42: 203–207.

[^williamson-1987a]: –––, 1987a. “On the Paradox of Knowability,” *Mind*, 96: 256–61.

[^williamson-1987b]: –––, 1987b. “On Knowledge of the Unknowable,” *Analysis*, 47: 154–8.

[^williamson-1988]: –––, 1988. “Knowability and Constructivism,” *Philosophical Quarterly*, 38: 422–432.

[^williamson-1992]: –––, 1992. “On Intuitionistic Modal Epistemic Logic,” *Journal of Philosophical Logic*, 21: 63–89.

[^williamson-1993]: –––, 1993. “Verificationism and Non-Distributive Knowledge,” *Australasian Journal of Philosophy*, 71: 78–86.

[^williamson-2000a]: –––, 2000a. “Tennant on Knowable Truth,” *Ratio*, XIII: 99–114.

[^williamson-2000b]: –––, 2000b. *Knowledge and its Limits*, Oxford: Oxford University Press, Chapter 12.

[^williamson-2009]: –––, 2009. “Tennant’s Troubles,” in Salerno (ed.) 2009a, 183–204.

[^wright-1987]: Wright, C., 1987. *Realism, Meaning and Truth*, Oxford: Blackwell.

[^wright-1992]: –––, 1992. *Truth and Objectivity*, Cambridge, MA: Harvard University Press, Chapter 2.

[^wright-2000]: –––, 2000. “Truth as Sort of Epistemic: Putnam’s Peregrinations,” *Journal of Philosophy*, 97: 335–364.

[^zardini-2015]: Zardini, E., 2015. “Truth, Demonstration and Knowledge. A Classical Solution to the Paradox of Knowability,” *Theoria*, 30: 365–392.
