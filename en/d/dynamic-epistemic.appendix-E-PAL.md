# dynamic-epistemic — appendix-E-PAL（supplement）

> （《dynamic-epistemic》词条补充材料，源：plato.stanford.edu/entries/dynamic-epistemic/appendix-E-PAL.html）

#### Supplement to Dynamic Epistemic Logic

## Appendix E: Technical details of Public Announcement Logic

In this appendix, we take a closer look at some of the technical details of Public Announcement Logic.

- 1. Schematic validity
- 2. Expressivity and succinctness
- 3. Gerbrandy-Groeneveld announcements
- 4. Consistency-preserving announcements and Arrow Update Logic
- 5. Arbitrary Public Announcement Logic: quantification over announcements

### 1. Schematic validity

Fix a language $\Lang$ and a semantics for this language. To say that an $\Lang$-formula *F* is *schematically valid* means that *F* is valid and that *F* remains valid whenever we obtain a new $\Lang$-formula by replacing, for each propositional letter in *F*, all occurrences of that letter by some other $\Lang$-formula. To say that $\Lang$ itself is *schematically valid* means that every valid formula in $\Lang$ is schematically valid. (Validity may be restricted to some specific class of models; however, if no class is mentioned, then the class of all models is assumed, as we will do now.) For example, let $\Lang$ be the language (ML) of basic multi-modal logic. Then the formula $$ p\to(q\to p) $$ is schematically valid: no matter what (ML)-formula we use to replace *p* or *q*, we always obtain a valid (ML)-formula. In fact, we can show that replacing letters in valid (ML)-formulas by (ML)-formulas preserves validity of *every* valid (ML)-formula; that is, (ML) is schematically valid. This proof is by induction on the length of derivations for multi-modal $\mathsf{K}$: each axiom is schematically valid and each rule preserves schematic validity. Since an (ML)-formula is valid (for the class of all pointed Kripke models) if and only if it is derivable in multi-modal $\mathsf{K}$, the result follows.

The language (PAL) is *not* schematically valid. In particular, the reduction axiom for propositional letters, which states that

$$ [F!]p\leftrightarrow(F\to p) \text{ for letters }p\in\sP $$

is not schematically valid. To see why, consider the formula obtained by replacing *F* with the letter *q* and *p* with the formula $[a]q$:

$$ [q!][a]q\leftrightarrow(q\to[a]q) \text{ (not valid)} $$

This formula says that the statement “after the announcement of *q*, agent *a* knows *q*” is equivalent to the statement “if *q* is true, then agent *a* knows *q*”. This supposed equivalence is formally and intuitively incorrect: an agent can come to know some truth after it is announced without knowing that truth in advance; that is, the left side $[q!][a]q$ can be true while the right side $q\to[a]q$ is false. Indeed, the primary purpose of a public announcement is to bring about knowledge by conveying information that the agents do not already have. The valid equivalence, which follows by Reduction Axiom 4, says something very different: $$ [q!][a]q\leftrightarrow(q\to[a][q!]q) . $$ This says that *a*’s knowledge of *q* after the announcement comes about if and only if, whenever *q* is true, *a* knows *before* the announcement that the possible future announcement of *q* would ensure that *q* is true. That this is correct follows immediately from the fact that PAL announcements are truthful and completely trustworthy: the announcement of a formula guarantees that the formula is true. This leads us to the key difference between the two equivalences: the valid one correctly equates post-announcement knowledge with pre-announcement knowledge of truths that a possible future announcement would convey, whereas the invalid one incorrectly equates post-announcement knowledge with what is currently known independent of what is to be announced.

Note that the axiomatization of $\PAL$ uses the letters *F*, *G*, and *H* to represent arbitrary formulas and the letter *p* to represent an arbitrary propositional letter. Formally speaking, each of these symbols is to be understood as a propositional letter, with the assumption that instances of a given axiom are obtained by replacing letters *F*, *G*, and *H* by (PAL)-formulas and the letter *p* by any letter. Therefore, to say that a given $\PAL$ axiom is schematically valid means that the axiom is valid (*i.e.,* each instance is valid) and, further, we obtain a valid formula whenever we replace one or more of *F*, *G*, *H*, or *p* by an *arbitrary* (PAL)-formula. In particular, this substitution need not respect the convention given in the axiomatization of $\PAL$ that restricts replacements of *p* to replacements by other letters. And herein is the source of non-schematic validity of (PAL): violating the requirement that *p* must be replaced by another letter allows us to replace *p* by a non-letter in the valid Reduction Axiom 1 and obtain a new, non-valid formula. Of course in making this replacement, the new formula we obtain is not an instance of Reduction Axiom 1 (because we violated the replacement rule for *p*). Nevertheless, that we can obtain a non-valid formula from a valid one by letter replacement shows that (PAL) is not schematically valid.

Schematic validity is generally taken for granted when it comes to classical (modal) logic. It is therefore noteworthy that PAL, which is obtained as an extension of the language of classical multi-modal logic, is not schematically valid. In particular, one must take care when inferring that a formula *F* is valid in light of the fact that *F* has the same form as a known valid formula. We saw an example above where this can go wrong: from the valid Reduction Axiom 1 we obtained (by a replacement that violated this axiom's restriction on letters) a formula with the same form that turned out to be invalid. In general, writing $F(p/G)$ to denote the formula obtained from *F* by replacing all instances of *p* by *G*, the following is a rule that is not valid in PAL:

**Schematic Substitution Rule (*not* valid for PAL):** from *F*, infer $F(p/G)$ for any formula *G* in the language.

But we do have the following kind of substitution rule in PAL:

**Equivalence Substitution Rule (van Ditmarsch, van der Hoek, and Kooi 2007):** if $\PAL\vdash G\leftrightarrow H$, then $\PAL\vdash F(p/G)\leftrightarrow F(p/H)$.

Note that this rule is not part of the axiomatization of $\PAL$; however, it can be proved that it is an admissible rule (i.e., the rule is derivable from the axiomatization of $\PAL$, in the sense that if the hypotheses are $\PAL$-derivable, then one can prove that the conclusion is as well).

Though not all (PAL)-formulas are schematically valid, there are some (PAL)-formulas that in fact are schematically valid. The formula $p\to(q\to p)$ is a simple example. An important result is that the set of schematically valid (PAL)-formulas—either over the class of transitive and Euclidean models with finitely many agents or over the class of all models with infinitely many agents—is decidable and axiomatizable; that is, there is an algorithm that can identify whether a given (PAL)-formula is schematically valid, and the collection of schematically valid (PAL)-formulas can be captured via an axiomatic system (Holliday et al. 2010, 2012). Whether this result holds for other classes of models is open as of the time of writing.

### 2. Expressivity and succinctness

The Reduction Theorem tells us that every (PAL)-formula *F* is provably equivalent to an announcement-free (ML)-formula $F^\circ$. Put another way, every formula containing public announcements can be rewritten so as to express exactly the same thing without using any public announcements. Therefore, even though the language (PAL) of Public Announcement Logic is defined as an extension of the language (ML) of basic multi-modal logic, this extension does not let us say anything that could not already be said before.

**PAL Expressivity Theorem (Plaza 1989, 2007; Gerbrandy and Groeneveld 1997).** (PAL) and (ML) are equally expressive (over the class of all pointed Kripke models). That is, whenever $\Lang$ is any one of our languages (PAL) and (ML) and $\Lang'$ is the other, we have the following: for each $\Lang$-formula *F*, there is an $\Lang'$-formula *G* such that $\models F\leftrightarrow G$.

This is a curious result: at first it seems like we have gained something by adding public announcements. In particular, the model-transforming operation of deleting worlds where the announced formula does not hold seems like something genuinely new; this is, after all, a *dynamic* take on what was before a purely *static* semantics. Nevertheless, the PAL Expressivity Theorem tells us that, at least from the point of view of expressivity, new formulas for public announcements and an extended semantics to accommodate the corresponding model-transforming operation are not needed. This may seem like bad news for the PAL approach. But this is not the whole story, since using the announcement-free language to express public announcements comes with another cost.

**PAL Succinctness Theorem (Lutz 2006; French et al. 2011, 2013).** (PAL) is exponentially more succinct than (ML) over the class $\sC_{\mathsf{K}}$ of all Kripke models (Lutz 2006) and over the class $\sC_{\mathsf{S5}}$ of reflexive, transitive, and Euclidean Kripke models (French et al. 2011, 2013): for each $\sC\in\{\sC_{\mathsf{K}},\sC_{\mathsf{S5}}\}$, there there is a sequence of (PAL)-formulas such that the size of the *n*-th formula $F_n$ (in terms of the number of symbols) is a linear function of *n* but the smallest (ML)-formula $F_n'$ satisfying $\sC\models F\leftrightarrow F_n'$ has size at least $2^n$.

This tells us that while we can express public announcement statements in the basic language (ML), doing so will in general require us to use exponentially more space. By way of analogy, we think of an advanced student of a foreign language: though she can express herself well in the foreign tongue, she may not have the ability to express every concept in the foreign language using a single word short phrase and so must sometimes use many words when speaking this language, even though she can make things much shorter in her mother tongue. So it is that the basic modal language (ML) can express fully the concepts of (PAL), though doing so will sometimes take exponentially more space.

This gives us two main reasons to stick with the PAL approach despite the seemingly bad news conveyed by the PAL Expressivity Theorem. First, using public announcements can save us an exponential amount of space. Second, the PAL approach provides us with a direct and intuitively appealing means of reasoning about truthful, completely trustworthy public announcements. That is, public announcements are *dynamic* operations that transform Kripke models (and hence agent knowledge and belief) in accordance with the information conveyed by what is announced, and using public announcements explicitly in the language can save us an exponential amount of space.

### 3. Gerbrandy-Groeneveld announcements

The model-transforming operation brought about by a public announcement of *F* was defined above as a *world-deleting* operation: delete all non-*F* worlds along with any arrows to or from these worlds. This method of *world-deleting* update was introduced by Plaza (1989, 2007). Gerbrandy and Groeneveld (1997) introduced an alternative *arrow-deleting* method: delete only the arrows pointing to non-*F* worlds. Defining new formulas $[F!_g]G$ with the intended meaning that *G* is true after the Gerbrandy–Groeneveld (GG) announcement of *F*, we are led to the following formal semantics:

- $M,w\models[F!_g]G$ holds if and only if $M[F!_g],w\models G$, where the model $$ M[F!_g] = (W[F!_g],R[F!_g],V[F!_g]) $$ is defined by:
- $W[F!_g]\coloneqq W$ — retain all worlds,
- $xR[F!_g]_ay$ if and only if $xR_ay$ and $M,y\models F$ — delete arrows if and only if they point to non-*F* worlds, and
- $v\in V[F!_g](p)$ if and only if $v\in V(p)$ — leave the valuation the same at all worlds.

Note that this semantics does not require that the announcement be truthful. That is, since we only delete arrows to non-*F* worlds, we do not run into a difficulty if we want to determine what is true of a non-*F* world *w* after the GG-announcement of *F*: we simply delete arrows to non-*F* worlds (including those pointing to *w*) and then check what is true at *w* in the resulting model. This provides a natural way for us to drop the assumption made for Plaza-style world-deleting announcements that announcements are truthful. While this alternative may have some intuitive appeal, the two approaches turn out to be expressively equivalent: the language of modal logic (ML) with GG-announcements is just as expressive as the language (ML) itself, and hence it follows by the PAL Expressivity Theorem that (ML) with GG-announcements is just as expressive as (ML) with Plaza-announcements (= (PAL)).

In the remainder of the article, “public announcements” will refer to Plaza-announcements.

### 4. Consistency-preserving announcements and Arrow Update Logic

GG-announcements, like Plaza-announcements, maintain the assumption that announcements are completely trustworthy. For the Plaza approach, the agents’ trust of the announcement leads them to all together delete worlds that violate the announcement (along with arrows to and from these worlds). For the GG approach, the agents’ trust of the announcement leads them to all together eliminate arrows that point to a world that violates the announcement, effectively eliminating those worlds from the list of considered possibilities. In each case, a consequence of this complete trust is that the agents run into trouble when they receive inconsistent information. In particular, on announcement of a contradiction such as the propositional constant $\bot$ for falsehood, all agents’ beliefs become trivialized: the formulas $[\bot!][a]F$ and $[\bot!_g][a]F$ are valid for all agents *a* and all formulas *F*. In essence, an announcement of a contradiction brings each agent into a confused state of doxastic contradiction in which she believes anything and everything is true. This led Steiner (2006) to consider *consistency-preserving public announcements*, a variation of GG-announcements in which agents avoid arrow deletions that would lead to doxastic contradiction. Other studies of consistency preservation include Aucher (2008) and Aucher et al. (2009). Steiner’s construction is a special case of a generalized approach to arrow deletion introduced by Kooi and Renne (2011a,b).

The language \\eqref{AUL} of arrow update logic is given by the following grammar: $$\begin{align*}\taglabel{AUL} F & \ccoloneqq p \mid F \land F \mid \lnot F \mid [a]F \mid [U]F \\ U & \ccoloneqq (F,a,F) \mid (F,a,F),U \\ & \qquad \small p\in\sP,\; a\in\sA \end{align*}$$ Each triple $(G,a,G')$ is called an *a-arrow specification* with *source condition G* and *target condition $G'$*. A finite, comma-separated sequence *U* of arrow specifications for one or more agents is called an *arrow update*. When it is convenient, we identify an arrow update *U* with the finite set consisting of the arrow specifications in *U*.

An arrow update *U* describes the following Kripke model-transforming operation: save every *a*-arrow from a world *x* to a world $x'$ if *U* contains an *a*-arrow specification $(F,a,F')$ such that *F* is true at the source world *x* and $F'$ is true at the target world $x'$; delete all other arrows in the model. Formally, this is defined as follows.

- $M,w\models[U]F$ holds if and only if $M*U,w\models F$, where the model $$ M*U=(W*U,R*U,V*U) $$ is defined by:
- $W*U\coloneqq W$ — retain all worlds,
- $x(R*U)_ax'$ if and only if $xR_ax'$ and there exists $(G,a,G')\in U$ such that $M,x\models G$ and $M,x'\models G'$ — delete arrows that do not satisfy an arrow specification in *U*, and
- $v\in V*U(p)$ if and only if $v\in V(p)$ — leave the valuation the same at all worlds.

Using the propositional constant $\top$ for truth, the GG-announcement formula $[F!_g]G$ is equivalent to the \\eqref{AUL}-formula $$ [\{(\top,a,F)\mid a\in\sA\}]G, $$ and the Plaza-announcement formula $[F!]G$ is equivalent to the \\eqref{AUL}-formula $$ F\to[\{(\top,a,F)\mid a\in\sA\}]G. $$ Arrow updates are therefore a generalization of both types of public announcement. Steiner’s (2006) consistency-preserving public announcement with *F* is equivalent to Kooi and Renne's (2011a) “cautious update” with *F*, which is the arrow update $\CaU$ (called ”$\CU$” in Kooi and Renne 2011a) defined by

$$ \CaU(F) \coloneqq \{ ([a]\lnot F,a,\top)\mid a\in\sA \} \cup \{ (\may{a}F,a,F)\mid a\in\sA \}. $$

Intuitively, $\CaU(F)$ says that if agent *a* believes that *F* is false, then *a*-arrows departing the current world should remain because she rejects an update she knows to be false. That is, we preserve *a*-arrows whose source is an $[a]\lnot F$-world and whose target is a $\top$-world (i.e., whose target is any world at all). However, if she believes that *F* might be true, then all *a*-arrows leading to a non-*F* world should be deleted because she is willing to accept information that does not contradict her beliefs. That is, we preserve *a*-arrows whose source is an $\may{a}F$-world only if their target is an *F*-world. We delete all arrows that do not satisfy one of the two kinds of arrow specifications that make up $\CaU(F)$.

A key limitation of arrow updates is that the information is assumed to be public: all agents together perform the same arrow update. So while arrow updates are a generalization of public announcements, this generalization still retains the assumption that the model-changing action is common knowledge among the agents. *Generalized Arrow Update Logic* (Kooi and Renne 2011b) drops this common knowledge assumption. We discuss Generalized Arrow Update Logic in Appendix I. Finally, we mention that Kooi and Renne (2011a) also present a *common knowledge* extension of \\eqref{AUL}, but this has not yet been extended to the generalized arrow update setting.

Having briefly surveyed consistency-preserving public announcements, Arrow Update Logic, and Generalized Arrow Update Logic, we return to the primary topic of this section: public announcements.

### 5. Arbitrary Public Announcement Logic: quantification over announcements

We may think of public announcement logic as a theory that tells us whether a given formula *F* is made true by some specific announcement *G* we have fixed in advance. But we might wish to look at this the other way around: is there some announcement *G* that will bring out the truth of our given formula *F*? Balbiani et al. (2008) introduced Arbitrary Public Announcement Logic (APAL) for studying such questions. The language \\eqref{APAL} of Arbitrary Public Announcement Logic extends the language (PAL) of Public Announcement Logic by adding new “arbitrary announcement” formulas $[*!]F$ to express that “after every announcement, *F* is true”: $$\begin{gather*}\taglabel{APAL} F \ccoloneqq p \mid F\land F \mid \lnot F\mid [a]F \mid [F!]F \mid [*!]F \\ \small p\in\sP,\; a\in\sA \end{gather*}$$ The dual arbitrary announcement modality $\may{*!}$ defined by setting $$ \may{*!}F \coloneqq \lnot[*!]\lnot F $$ allows us to express “after some announcement, *F* is true”. Semantically, the formula $[*!]F$ is interpreted as follows: to say that $[*!]F$ is true means that *F* is true after the announcement of any formula *G* of multi-modal logic (ML). Hence

$$ [*!]F \text{ is intuitively equivalent to } \bigwedge_{G\in\text{(ML)}}[F!]F. $$

Of course the conjunction above is not a formula in our language (since it is infinite), but this expression gives the intuition of what we are after. In particular, the modal $[*!]$ acts as a *universal quantifier* over (ML)-formula announcements (“after every (ML)-announcement”), and the dual $\may{*!}$ acts as an *existential quantifier* over (ML)-formula announcements (“after some (ML)-announcement”). Quantification is restricted to (ML)-formulas so as to avoid circularity in the semantics: were quantification to range over all \\eqref{APAL}-formulas, $[*!]F$ would be true at a pointed model only if *F* holds after the formula $[*!]F$ is itself announced at that pointed model, and this would require us to already know the truth value of $[*!]F$ at that pointed model. Restricting the range of quantification to (ML)-formulas avoids this circularity. Further, we note it follows by the PAL Expressivity Theorem (Section 2) that restricting the range to (ML)-formulas is no different (in terms of expressivity) than restricting the range to (PAL)-formulas.

Formally, \\eqref{APAL}-formulas are evaluated by extending the binary truth relation $\models$ between pointed Kripke models and (PAL)-formulas as follows:

- $M,w\models[*!]G$ holds if and only if we have $M,w\models[G!]F$ for all $G\in\text{(ML)}$.

Balbiani et al. (2008) obtained a number of results on the relative expressivity of \\eqref{APAL}, (PAL), and (ML).

**Theorem (Balbiani et al. 2008).** Over the class of all pointed $\mathsf{S5}$ Kripke models with agent set $\sA$, we have each of the following.

- If $|\sA|=1$ (i.e., there is only one agent), then \\eqref{APAL}, (PAL), and (ML) are equally expressive.
- If $|\sA|\gt 1$ (i.e., there is more than one agent), then \\eqref{APAL} is strictly more expressive than both (PAL) and (ML).

The axiomatic theory of Arbitrary Public Announcement Logic is a deceptively simple extension of $\mathsf{S5}$ Public Announcement Logic obtained by adding one new axiom and one new rule. However, the proof of completeness is difficult and highly technical. We present the axiomatic theory, state the soundness and completeness results, and present two complexity results.

**The axiomatic theory $\APAL$.**

- Axiom schemes and rules for $\PAL$ based on multi-agent $\mathsf{S5}$.
- $[*!]F\to[G!]F$ for $G\in\text{(ML)}$ “Arbitrary announcements may be instantiated by specific (ML)-formulas.”
- Arbitrary Announcement Rule: from $F\to[G!][p!]H$ with *p* not occurring in *F*, *G*, or *H*, infer $F\to[G!][*!]H$. “If *H* obtains after an announcement by an otherwise unused letter *p*, then *H* obtains after an arbitrary announcement.”

**$\APAL$ Soundness and Completeness (Balbiani et al. 2008).** $\APAL$ is sound and complete with respect to the collection $\sC_*$ of pointed $\mathsf{S5}$ Kripke models. That is, for each \\eqref{APAL}-formula *F*, we have that $\APAL\vdash F$ if and only if $\sC_*\models F$.

**APAL Complexity.** Let $\sC_{\mathsf{S5}}$ be the class of Kripke models such that each binary accessibility relation is reflexive, transitive, and symmetric.

- The satisfiability problem for \\eqref{APAL} over $\sC_{\mathsf{S5}}$ is undecidable (French and van Ditmarsch 2008).
- The model checking problem for \\eqref{APAL} over $\sC_{\mathsf{S5}}$ is PSPACE-complete (Balbiani et al. 2008).

APAL provides a convenient language for reasoning about Fitch’s paradox (Fitch 1963), which concerns the seemingly strange result that the existence of unknown truths implies not all truths are knowable. Following the suggestion of van Benthem (2004), Balbiani et al. (2008) identify “*F* is knowable by agent *a*” with $\may{*!}[a]F$. This equates “knowability” with “being known after some announcement”. We then may express “all truths are knowable” using the scheme $F\to\may{*!}[a]F$. We note that this scheme is not valid: the formula $p\land\lnot[a]p$ (“*p* is true but *a* does not know it”) is satisfiable but can never be known by *a* (because *a*’s knowledge of the first conjunct *p* implies the negation of the second conjunct $\lnot[a]p$). Therefore, if *p* is a truth unknown to agent *a*, then the formula $p\land\lnot[a]p$ is another truth unknown to agent *a* but agent *a* cannot come to know this lattermost truth. That is, the following assumptions are jointly inconsistent:

- $p\land\lnot[a]p$ — “*p* is an unknown truth.”
- $F\to\may{*!}[a]F$ for each $F\in\eqref{APAL}$ — “All truths are knowable.”

We refer the reader to the discussions in van Benthem (2004), Balbiani et al. (2008), and Brogaard and Salerno (2012) for further details. Also, for an alternative interpretation of “all truths are knowable” based on the \\eqref{APAL}-formula $\may{*!}([a]F\lor[a]\lnot F)$ (“it is possible for *a* to come to know *whether* *F* is true”), see van Ditmarsch et al. (2012b).

Ågotnes et al. (2010) study a variant of APAL known as “group announcement logic”. In this logic, new modal formulas having the form $\may{B!}F$ for a group $B\subseteq\sA$ of agents express that “the group *B* can make an announcement that makes *F* true”. The semantics of these new formulas is given as follows:

- $M,w\models\may{B!}F$ holds if and only if we have $M,w\models\may{\bigwedge_{a\in B}[a]G_a!}F$ for some function $G:B\to\text{(ML)}$ mapping each agent $a\in B$ to a formula $G_a\in\text{(ML)}$.

That is, to say that $\may{B!}F$ is true means that there is a collection of (ML)-formulas $G_a$, one formula for each agent *a* in the group *B*, such that if each agent knows her formula and this knowledge is then announced, then *F* is true. For details, the reader is referred to Ågotnes et al. (2010).

← beginning of main article
