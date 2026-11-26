# Provability Logic
**First published Wed Apr 2, 2003; substantive revision Mon Mar 4, 2024**

*Verbrugge, Rineke (L.C.)*

Provability logic is a modal logic that is used to investigate what arithmetical theories can express in a restricted language about their provability predicates. The logic has been inspired by developments in meta-mathematics such as Gödel’s incompleteness theorems of 1931 and Löb’s theorem of 1953. As a modal logic, provability logic has been studied since the early seventies, and has had important applications in the foundations of mathematics.

From a philosophical point of view, provability logic is interesting because the concept of provability in a fixed theory of arithmetic has a unique and non-problematic meaning, other than concepts like necessity and knowledge studied in modal and epistemic logic. Furthermore, provability logic provides tools to study the notion of self-reference.

## 1. The history of provability logic

Two strands of research have led to the birth of provability logic. The first one stems from a paper by K. Gödel (1933)[^gödel-1933], where he introduces translations from intuitionistic propositional logic into modal logic (more precisely, into the system nowadays called S4), and briefly mentions that provability can be viewed as a modal operator. Even earlier, C.I. Lewis started the modern study of modal logic by introducing strict implication as a kind of deducibility, where he may have meant deducibility in a formal system like Principia Mathematica, but this is not clear from his writings.

The other strand starts from research in meta-mathematics: what can mathematical theories say about themselves by encoding interesting properties? In 1952, L. Henkin posed a deceptively simple question inspired by Gödel’s incompleteness theorems. In order to formulate Henkin’s question, some more background is needed. As a reminder, Gödel’s first incompleteness theorem states that, for a sufficiently strong formal theory like Peano Arithmetic, any sentence asserting its own unprovability is in fact unprovable. On the other hand, from “outside” the formal theory, one can see that such a sentence is true in the standard model, pointing to an important distinction between truth and provability.

More formally, let $\ulcorner A \urcorner$ denote the Gödel number of arithmetical formula $A$, which is the result of assigning a numerical code to $A$. Let $\Prov$ be the formalized provability predicate for Peano Arithmetic, which is of the form $\exists p \, \Proof(p,x)$. Here, $\Proof$ is the formalized proof predicate of Peano Arithmetic, and $\Proof(p,x)$ stands for “Gödel number $p$ codes a correct proof from the axioms of Peano Arithmetic of the formula with Gödel number $x$”. (For a more precise formulation, see Smoryński (1985)[^smoryński-1985], Davis (1958)[^davis-1958].) Now, suppose that Peano Arithmetic proves $A \leftrightarrow \neg$ $\Prov (\ulcorner A \urcorner)$, then by Gödel’s result, $A$ is not provable in Peano Arithmetic, and thus it is true, for in fact the self-referential sentence $A$ states “I am not provable”.

Henkin on the other hand wanted to know whether anything could be said about sentences asserting their own provability: supposing that Peano Arithmetic proves $B \leftrightarrow \Prov(\ulcorner B \urcorner)$, what does this imply about $B$? Three years later, M. Löb took up the challenge and answered Henkin’s question in a surprising way. Even though all sentences provable in Peano Arithmetic are indeed true about the natural numbers, Löb showed that the formalized version of this fact, $\Prov(\ulcorner B \urcorner) \rightarrow B$, can be proved in Peano Arithmetic only in the trivial case that Peano Arithmetic already proves $B$ itself. This result, now called Löb’s theorem, immediately answers Henkin’s question. (For a proof of Löb’s theorem, see Section 4.) Löb also showed a formalized version of his theorem, namely that Peano Arithmetic proves

$$ \Prov(\ulcorner \Prov(\ulcorner B\urcorner ) \rightarrow B\urcorner ) \rightarrow \Prov(\ulcorner B \urcorner ). $$

In the same paper, Löb formulated three conditions on the provability predicate of Peano Arithmetic, that form a useful modification of the complicated conditions that Hilbert and Bernays introduced in 1939 for their proof of Gödel’s second incompleteness theorem. In the following, derivability of $A$ from Peano Arithmetic is denoted by $\PA \vdash A$:

1. If $\PA \vdash A$, then $\PA \vdash \Prov(\ulcorner A \urcorner )$;
2. $\PA \vdash \Prov(\ulcorner A\rightarrow B\urcorner) \rightarrow ( \Prov(\ulcorner A \urcorner ) \rightarrow \Prov(\ulcorner B \urcorner ));$
3. $\PA \vdash \Prov(\ulcorner A \urcorner ) \rightarrow \Prov(\ulcorner \Prov(\ulcorner A \urcorner ) \urcorner ).$

These Löb conditions, as they are called nowadays, seem to cry out for a modal logical investigation, where the modality $\Box$ stands for provability in PA. Ironically, the first time that the formalized version of Löb’s theorem was stated as the modal principle

$$ \Box(\Box A \rightarrow A) \rightarrow \Box A $$

was in a paper by Smiley in 1963 about the logical basis of ethics, which did not consider arithmetic at all. More relevant investigations, however, seriously started only almost twenty years after publication of Löb’s paper. The early 1970s saw the rapid development of propositional provability logic, where several researchers in different countries independently proved the most important results, discussed in Sections 2, 3, and 4. Propositional provability logic turned out to capture exactly what many formal theories of arithmetic can say by propositional means about their own provability predicate. More recently, researchers have investigated the boundaries of this approach and have proposed several interesting more expressive extensions of provability logic (see Section 5).

## 2. The axiom system of propositional provability logic

The logical language of propositional provability logic contains, in addition to propositional atoms and the usual truth-functional operators as well as the contradiction symbol $\bot$, a modal operator $\Box$ with intended meaning “is provable in $T$,” where $T$ is a sufficiently strong formal theory, let us say Peano Arithmetic (see Section 4). $\Diamond A$ is an abbreviation for $\neg\,\Box\neg\, A$. Thus, the language is the same as that of modal systems such as K and S4 presented in the entry modal logic.

### 2.1 Axioms and rules

Propositional provability logic is often called GL, after Gödel and Löb. (Alternative names found in the literature for equivalent systems are L, G, KW, K4W, and PrL). The logic GL results from adding the following axiom to the basic modal logic K:

$$\tag{GL} \Box(\Box A \rightarrow A) \rightarrow \Box A. $$

As a reminder, because GL extends K, it contains all formulas having the form of a propositional tautology. For the same reason, GL contains the

$$\tag{Distribution Axiom} \Box(A \rightarrow B) \rightarrow (\Box A \rightarrow \Box B). $$

Furthermore, it is closed under the Modus Ponens Rule, which allows to derive $B$ from $A \rightarrow B$ and $A$, and the Generalization Rule, which says that if $A$ is a theorem of GL, then so is $\Box A$.

The notion $\GL \vdash A$ denotes provability of a modal formula $A$ in propositional provability logic. It is not difficult to see that the modal axiom $\Box A \rightarrow \Box\Box A$ (known as Axiom 4 of modal logic) is indeed provable in GL. To prove this, one uses the substitution $A \wedge \Box A$ for $A$ in the axiom (GL). Then, seeing that the antecedent of the resulting implication follows from $\Box A$, one applies the Distribution Axiom and the Generalization Rule as well as some propositional logic.

Note that GL proves many unexpected theorems that are not shared with other well-known modal logics such as K and S4. For example, one instantiation of the axiom GL is $\Box(\Box\bot \rightarrow \bot) \rightarrow \Box\bot$, from which it follows by the other axioms and rules that $\Box\Diamond A \rightarrow \Box B$ for any formulas $A$ and $B$.[^note-1] Unless explicitly stated otherwise, in the sequel “provability logic” stands for the system GL of propositional provability logic.

As to the *proof theory* of provability logic, Valentini (1983)[^valentini-1983] proved that a standard sequent calculus formulation of GL obeys *cut elimination*, which means, roughly formulated, that each formula provable from GL in the sequent calculus also has a GL sequent proof “without detours” (see the entry the development of proof theory for a precise explanation of cut elimination). In recent years, there has been renewed interest in the proof theory of GL, see for example Goré and Ramanayake (2008, 2012) and Goré, Ramanayake and Shillito (2021). Cut-elimination leads to the desirable *subformula property* for GL, because all formulas that appear in a cut-free proof are subformulas of the endsequent formulas.

For recent proof-theoretic investigations of provability logic based on different cut-free sequent calculi see (Negri 2005, 2014; Poggiolesi 2009)[^negri-2005][^negri-2014][^poggiolesi-2009]. Negri presents two equivalent labelled sequent calculi for GL and a syntactic proof of cut elimination. Even if a full subformula property does not hold for these calculi because of the labelling, the usual consequences of the subformula property can be established: The labelled formalism allows a direct completeness proof, which can be used to establish decidability as well as the finite model property, which means that any formula that is not provable has a *finite* counter-model.

An intriguing new proof-theoretical development is Shamkanov’s expansion of sequent-style proof systems by allowing *circular proofs* (Shamkanov 2014)[^shamkanov-2014]. Consider a sequent system for K4, the modal system resulting from GL by replacing the axiom GL by the weaker axiom $\Box A \rightarrow \Box\Box A$ (axiom 4). However, suppose that open hypotheses are allowed, provided that the same sequent occurs strictly below that hypothesis in the proof tree. Formulated more technically, one can find a circular derivation from an ordinary derivation tree by linking each of its non-axiomatic leaves with an identical interior node. Shamkanov (2014)[^shamkanov-2014] proved that the resulting system is consistent and that moreover, in general, each sequent has a GL-derivation if and only if it has a circular K4-derivation. Circular proofs also provide a method to show proof-theoretically that Lyndon’s interpolation theorem holds for GL (Shamkanov 2011)[^shamkanov-2011]. Standard interpolation for GL had already been proved before by different methods (Boolos 1979; Smoryński 1978; Rautenberg 1983)[^boolos-1979][^rautenberg-1983][^smoryński-1978] and so had uniform interpolation (Shavrukov 1993b, Bílková 2016, Férée et al. [Other Internet Resources])[^bílková-2016][^shavrukov-1993b]. (For more information about Lyndon’s interpolation theorem for first-order logic, see also the entry first-order model theory ).

### 2.2 The fixed point theorem

The main “modal” result about provability logic is the fixed point theorem, which D. de Jongh and G. Sambin independently proved in 1975 (Sambin 1976, Smoryński 1985, de Jongh forthcoming)[^smoryński-1985][^sambin-1976]. Even though it is formulated and proved by strictly modal methods, the fixed point theorem still has great arithmetical significance. It says essentially that self-reference is not really necessary, in the following sense. Suppose that all occurrences of the propositional variable $p$ in a given formula $A(p)$ are under the scope of the provability operator, for example $A(p) = \neg\Box p$, or $A(p) = \Box(p \rightarrow q)$. Then there is a formula $B$ in which $p$ does not appear, such that all propositional variables that occur in $B$ already appear in $A(p),$ and such that

$$ \GL \vdash B \leftrightarrow A(B). $$

This formula $B$ is called a *fixed point* of $A(p)$. Moreover, the fixed point is unique, or more accurately, if there is another formula $C$ such that $ \GL \vdash C \leftrightarrow A(C)$, then we must have $ \GL \vdash B \leftrightarrow C$. Most proofs in the literature give an algorithm by which one can compute the fixed point (see Smoryński 1985, Boolos 1993, Sambin and Valentini 1982, Lindström 2006)[^boolos-1993][^smoryński-1985][^sambin-1982][^lindström-2006][^sambin-1982-2][^lindström-2006-2]. A particularly short and clear proof, as well as a very efficient algorithm to compute fixed points, can be found in Reidhaar-Olson (1990)[^reidhaar-olson-1990].

For example, suppose that $A(p) = \neg \, \Box p$. Then the fixed point produced by such an algorithm is $\neg \, \Box\bot$, and indeed one can prove that

$$ \GL \vdash \neg\,\Box\bot \leftrightarrow \neg\,\Box(\neg\,\Box\bot). $$

If this is read arithmetically, the direction from left to right is just the formalized version of Gödel’s second incompleteness theorem: if a sufficiently strong formal theory $T$ like Peano Arithmetic does not prove a contradiction, then it is not provable in $T$ that $T$ does not prove a contradiction. Thus, sufficiently strong consistent arithmetical theories cannot prove their own consistency. We will turn to study the relation between provability logic and arithmetic more precisely in Section 4, but to that end another “modal” aspect of GL needs to be provided first: semantics.

## 3. Possible worlds semantics and topological semantics

Provability logic has suitable possible worlds semantics, just like many other modal logics. As a reminder, a possible worlds model (or Kripke model) is a triple $M = \langle W,R,V \rangle$, where $W$ is a non-empty set of possible worlds, $R$ is a binary accessibility relation on $W$, and $V$ is a valuation that assigns a truth value to each propositional variable for each world in $W$. The pair $F = \langle W,R \rangle$ is called the frame of this model. The notion of truth of a formula $A$ in a model $M$ at a world $W$, notation $M,w \models A$, is defined inductively. Let us repeat only the most interesting clause, the one for the provability operator $\Box$:

$$ M,w \models \Box A \text{ iff for every } w', \text{ if } wRw', \text{ then } M,w' \models A. $$

See the entry modal logic for more information about possible worlds semantics in general.

### 3.1 Characterization and modal soundness

The modal logic K is valid in all Kripke models. Its extension GL however, is not: we need to restrict the class of possible worlds models to a more suitable one. Let us say that a formula $A$ is valid in frame $F$, notation $F \models A$, iff $A$ is true in all worlds in Kripke models $M$ based on $F$. It turns out that the new axiom (GL) of provability logic corresponds to a condition on frames, as follows:

For all frames $F = \langle W,R \rangle, F \models \Box(\Box p \rightarrow p) \rightarrow \Box p$ iff $R$ is transitive and conversely well-founded.

Here, *transitivity* is the well-known property that for all worlds $w_1$, $w_2$, $w_3$ in $W$, if $w_1 Rw_2$ and $w_2 Rw_3$, then $w_1 Rw_3$. A relation is *conversely well-founded* iff there are no infinite ascending sequences, that is sequences of the form $w_1 Rw_2 Rw_3 R \ldots$. Note that conversely well-founded frames are also irreflexive, for if $wRw$, this gives rise to an infinite ascending sequence $wRwRwR\ldots$.

The above correspondence result immediately shows that GL is modally sound with respect to the class of possible worlds models on transitive conversely well-founded frames, because all axioms and rules of GL are valid on such models. The question is whether completeness also holds: for example, the formula $\Box A \rightarrow \Box\Box A$, which is valid on all transitive frames, is indeed provable in GL, as was mentioned in Section 1. But is *every* formula that is valid on all transitive conversely well-founded frames also provable in GL?

### 3.2 Modal completeness

Unaware of the arithmetical significance of GL, K. Segerberg proved in 1971 that GL is indeed complete with respect to transitive conversely well-founded frames; D. de Jongh and S. Kripke independently proved this result as well. Segerberg showed that GL is complete even with respect to the more restricted class of finite transitive irreflexive trees, a fact which later turned out to be very useful for Solovay’s proof of the arithmetical completeness theorem (see Section 4).

The modal soundness and completeness theorems immediately give rise to a decision procedure to check for any modal formula $A$ whether $A$ follows from GL or not, by depth-first search through irreflexive transitive trees of bounded depth. Looking at the procedure a bit more precisely, it can be shown that GL is decidable in the computational complexity class PSPACE, like the well-known modal logics K, T and S4. This means that there is a Turing machine that, given a formula $A$ as input, answers whether $A$ follows from GL or not; the size of the memory that the Turing machine needs for its computation is only polynomial in the length of $A$. One can show that the decision problem for GL (again, like the decision problems for K, T and S4) is PSPACE-*complete*, in the sense that all other problems in PSPACE are no harder than deciding whether a given formula is a theorem of GL. (See Goré and Kelly 2007 [Other Internet Resources] for the description of an automated theorem prover for GL.)

To give some more perspective on complexity, the class P of functions computable in an amount of time polynomial in the length of the input, is included in PSPACE, which in turn is included in the class EXPTIME of functions computable in exponential time (see the entry computability and complexity). It remains a famous open problem whether these two inclusions are strict, although many complexity theorists believe that they are. Some other well-known modal logics, like epistemic logic with common knowledge, are decidable in EXPTIME, thus they may be more complex than GL, depending on the open problems.

### 3.3 Failure of strong completeness

Many well-known modal logics $S$ are not only complete with respect to an appropriate class of frames, but even *strongly complete*. In order to explain strong completeness, we need the notion of *derivability from a set of assumptions*. A formula $A$ is derivable from the set of assumptions *Γ* in a modal logic $S$, written as $\Gamma \vdash A$, if $A$ is in *Γ* or $A$ follows from formulas in *Γ* and axioms of $S$ by applications of Modus Ponens and the Generalization Rule. Here, the Generalization Rule can only be applied to derivations without assumptions (see Hakli and Negri 2010).

Now a modal logic $S$ is *strongly complete* if for all (finite or infinite) sets *Γ* and all formulas $A$:

If, on appropriate $S$-frames, $A$ is true in all worlds in which all formulas of *Γ* are true, then $\Gamma \vdash A$ in the logic $S$.

This condition holds for systems like K, M, K4, S4, and S5. If restricted to finite sets *Γ*, the above condition corresponds to completeness.

Strong completeness does not hold for provability logic, however, because *semantic compactness* fails. Semantic compactness is the property that for each infinite set *Γ* of formulas,

If every finite subset $\Delta$ of *Γ* has a model on an appropriate $S$-frame, then *Γ* also has a model on an appropriate $S$-frame.

As a counterexample, take the infinite set of formulas

$$\begin{align} \Gamma &= \{\Diamond p_0, \Box(p_0 \rightarrow \Diamond p_1), \Box(p_1 \rightarrow \Diamond p_2), \Box(p_2 \rightarrow \Diamond p_3), \ldots, \\ &\qquad\ \Box(p_n \rightarrow \Diamond p_{n+1}), \ldots\} \end{align}$$

Then for every finite subset $\Delta$ of *Γ*, one can construct a model on a transitive, conversely well-founded frame and a world in the model where all formulas of $\Delta$ are true. So by modal soundness, GL does not prove $\bot$ from $\Delta$ for any finite $\Delta \subseteq \Gamma$, and *a fortiori* GL does not prove $\bot$ from *Γ*, as any GL-proof is finite. On the other hand, it is easy to see that there is no model on a transitive, conversely well-founded frame where in any world, all formulas of *Γ* hold. Thus $\bot$ follows semantically from *Γ*, but is not provable from it in GL, contradicting the condition of strong completeness.[^note-2]

### 3.4 Topological semantics for provability logic

As an alternative to possible worlds semantics, many modal logics may be given topological semantics. Clearly, propositions can be interpreted as subsets of a topological space. It is also easy to see that the propositional connective $\wedge$ corresponds to the set-theoretic operation $\cap$, while $\vee$ corresponds to $\cup$, $\neg$ corresponds to the set-theoretic complement, and $\rightarrow$ corresponds to $\subseteq$. Modal logics that contain the reflection axiom $\Box A \rightarrow A$ enjoy a particularly natural interpretation of the modal operators as well. For these logics, $\Diamond$ corresponds to the closure operator in a topological space, while $\Box$ corresponds to the interior. To see why these interpretations are appropriate, notice that the reflection axiom corresponds to the fact that each set is included in its closure and each set includes its interior.

However, provability logic does *not* prove reflection, as the instantiation $\Box\bot \rightarrow \bot$ of reflection would lead to a contradiction with the axiom (GL).

Provability logic therefore needs a different approach. Based on a suggestion by J. McKinsey and A. Tarski (1944), L. Esakia (1981, 2003)[^esakia-1981][^esakia-2003] investigated the interpretation of $\Diamond$ as the derived set operator $d$, which maps a set $B$ to the set of its limit points $d(B)$. To explain the consequences of this interpretation of $\Diamond$, we need two more definitions, namely of the concepts *dense-in-itself* and *scattered*. A subset $B$ of a topological space is called *dense-in-itself* if $B \subseteq d(B)$. A topological space is called *scattered* if it has no non-empty subset that is dense-in-itself. The ordinals in their interval topology form examples of scattered spaces. Esakia (1981)[^esakia-1981] proved an important correspondence: he showed that a topological space *satisfies the axiom GL* if and only if the space is *scattered*. This correspondence soon led to the result, independently found by Abashidze (1985)[^abashidze-1985] and Blass (1990)[^blass-1990], that provability logic is complete with respect to any ordinal $\ge \omega^\omega$.

In the previous decades, topological semantics for provability logic has seen a veritable revival, especially in the study of Japaridze’s bimodal provability logic GLB, an extension of GL (Japaridze 1986)[^japaridze-1986]. The logic GLB turns out to be *modally incomplete* with respect to its possible worlds semantics, in the sense that it does not correspond to any class of frames.[^note-3] This feature places bimodal GLB in sharp contrast with unimodal GL, which corresponds to the class of finite transitive irreflexive trees, as mentioned above. Beklemishev et al. (2009) showed that GLB is, however, complete with respect to its *topological* semantics (see also Beklemishev 2009, Icard 2011)[^beklemishev-2009][^beklemishev-2009-2][^icard-2011]. Intriguing reverberations of Esakia’s correspondence between GL and scattered topological spaces can even be found in topological studies of spatial and epistemic logics (see Aiello et al. 2007)[^aiello-2007]. (See Section 5.4 for further discussion about GLB).

## 4. Provability logic and Peano Arithmetic

From the time GL was formulated, researchers wondered whether it was adequate for formal theories like Peano Arithmetic (PA): does GL prove *everything* about the notion of provability that can be expressed in a propositional modal language and can be proved in Peano Arithmetic, or should more principles be added to GL? To make this notion of adequacy more precise, we define a *realization* (sometimes called translation or interpretation) to be a function *f* that assigns to each propositional atom of modal logic a sentence of arithmetic, where

- $f(\bot)=\bot;$
- $f$ respects the logical connectives, for example, $f(B \rightarrow C) = (f(B) \rightarrow f(C));$ and
- $\Box$ is translated as the provability predicate $\Prov$, so $f(\Box B) = \Prov(\ulcorner f(B)\urcorner ).$

### 4.1 Arithmetical soundness

It was already clear in the early 1970s that GL is *arithmetically sound* with respect to PA, formally:

$$ \text{If } \GL \vdash A, \text{then for all realizations } f, \PA \vdash f(A).$$

To give some taste of meta-mathematics, let us sketch the soundness proof.

**Proof sketch of arithmetical soundness**. PA indeed proves realizations of propositional tautologies, and provability of the Distribution Axiom of GL translates to

$$ \PA \vdash \Prov(\ulcorner A \rightarrow B\urcorner ) \rightarrow (\Prov(\ulcorner A\urcorner ) \rightarrow \Prov(\ulcorner B\urcorner )) $$

for all formulas *A* and *B*, which is just Löb’s second derivability condition (see Section 1). Moreover, PA obeys Modus Ponens, as well as the translation of the Generalization Rule:

$$ \text{If } \PA \vdash A, \text{then } \PA \vdash \Prov(\ulcorner A\urcorner ), $$

which is just Löb’s first derivability condition. Finally, the translation of the main axiom (GL) is indeed provable in PA:

$$ \PA \vdash \Prov(\ulcorner \Prov(\ulcorner A\urcorner ) \rightarrow A\urcorner ) \rightarrow \Prov(\ulcorner A\urcorner ). $$

This is exactly the formalized version of Löb’s theorem mentioned in Section 1.

Let us give a sketch of the proof of Löb’s theorem itself from his derivability conditions (the proof of the formalized version is similar). The proof is based on Gödel’s diagonalization lemma, which says that for any arithmetical formula $C(x)$ there is an arithmetical formula $B$ such that

$$ \PA \vdash B \leftrightarrow C(\ulcorner B\urcorner ). $$

In words, the formula $B$ says “I have property $C$.”

**Proof of Löb’s theorem:**. Suppose that $\PA \vdash \Prov(\ulcorner A\urcorner ) \rightarrow A$; we need to show that $\PA \vdash A$. By the diagonalization lemma, there is a formula $B$ such that

$$ \PA \vdash B \leftrightarrow (\Prov(\ulcorner B\urcorner ) \rightarrow A). $$

From this it follows by Löb’s first and second derivability conditions plus some propositional reasoning that

$$ \PA \vdash \Prov(\ulcorner B\urcorner ) \leftrightarrow \Prov(\ulcorner \Prov(\ulcorner B\urcorner ) \rightarrow A\urcorner ). $$

Thus, again by Löb’s second condition,

$$ \PA \vdash \Prov(\ulcorner B\urcorner ) \rightarrow (\Prov(\ulcorner \Prov(\ulcorner B\urcorner ) \urcorner ) \rightarrow \Prov(\ulcorner A\urcorner )). $$

On the other hand Löb’s third condition gives

$$ \PA \vdash \Prov(\ulcorner B\urcorner ) \rightarrow \Prov(\ulcorner \Prov(\ulcorner B\urcorner )\urcorner ), $$

thus

$$ \PA \vdash \Prov(\ulcorner B\urcorner ) \rightarrow \Prov(\ulcorner A\urcorner ). $$

Together with the assumption that $PA \vdash \Prov(\ulcorner A\urcorner ) \rightarrow A$, this gives

$$ \PA \vdash \Prov(\ulcorner B\urcorner ) \rightarrow A. $$

Finally, the equation produced by the diagonalization lemma implies that $\PA \vdash B$, so $\PA \vdash \Prov(\ulcorner B\urcorner )$, thus

$$ \PA \vdash A, $$

as desired.

Note that substituting $\bot$ for $A$ in Löb’s theorem, we derive that $\PA \vdash \neg\, \Prov(\ulcorner \bot\urcorner )$ implies $\PA \vdash \bot$, which is just the contraposition of Gödel’s second incompleteness theorem.

### 4.2 Arithmetical completeness

The landmark result in provability logic is R. Solovay’s arithmetical completeness theorem of 1976, showing that GL is indeed adequate for Peano Arithmetic:

$$ \GL \vdash A \text{ if and only if for all realizations } f, \PA \vdash f(A). $$

This theorem says essentially that the modal logic GL captures everything that Peano Arithmetic can truthfully say in modal terms about its own provability predicate. The direction from left to right, arithmetical soundness of GL, is discussed above. Solovay set out to prove the other, much more difficult, direction by contraposition. His proof is based on intricate self-referential techniques, and only a small glimpse can be given here.

The modal completeness theorem by Segerberg was an important first step in Solovay’s proof of arithmetical completeness of GL with respect to Peano Arithmetic. Suppose that GL does not prove the modal formula $A$. Then, by modal completeness, there is a finite transitive irreflexive tree such that $A$ is false at the root of that tree. Now Solovay devised an ingenious way to simulate such a finite tree in the language of Peano Arithmetic. Thus he found a realization $f$ from modal formulas to sentences of arithmetic, such that Peano Arithmetic does not prove $f(A)$.

Solovay’s completeness theorem provides an alternative way to construct many arithmetical sentences that are not provable in Peano Arithmetic. For example, it is easy to make a possible worlds model to show that GL does not prove $\Box p \vee \Box\neg\, p$, so by Solovay’s theorem, there is an arithmetical sentence $f(p)$ such that Peano Arithmetic does not prove $\Prov(\ulcorner f(p)\urcorner ) \vee \Prov(\ulcorner \neg\, f(p)\urcorner )$. In particular, this implies that neither $f(p)$ nor $\neg\, f(p)$ is provable in Peano Arithmetic; for suppose on the contrary that $\PA \vdash f(p)$, then by Löb’s first condition and propositional logic, $\PA \vdash \Prov(\ulcorner f(p)\urcorner ) \vee \Prov(\ulcorner \neg\, f(p)\urcorner )$, leading to a contradiction, and similarly if one supposes that $\PA \vdash \neg\, f(p)$.

Solovay’s theorem is so significant because it shows that an interesting fragment of an undecidable formal theory like Peano Arithmetic—namely that which arithmetic can express in propositional terms about its own provability predicate—can be studied by means of a decidable modal logic, GL, with a perspicuous possible worlds semantics.

## 5. The scope of provability logic

In this section, some trends in research on provability logic are discussed. One important strand concerns the limits on the scope of GL, where the main question is, for which formal theories, other than Peano Arithmetic, is GL the appropriate propositional provability logic? Next, we discuss some generalizations of propositional provability logic in more expressive modal languages.

### 5.1 Boundaries

Since the late 1980s, logicians have investigated many other systems of arithmetic that are weaker than Peano Arithmetic. Often these logicians took their inspiration from computability issues, for example the study of functions computable in polynomial time. They have given a partial answer to the question: “For which theories of arithmetic does Solovay’s arithmetical completeness theorem (with respect to the appropriate provability predicate) still hold?” To discuss this question, two concepts are needed. $\Delta_0$-formulas are arithmetical formulas in which all quantifiers are bounded by a term, for example

$$ \forall y \le \bs\bs 0 \: \forall z \le y \: \forall x \le y + z \: (x + y \le (y+(y+z))), $$

where $\bs$ is the successor operator (“$+1$”). The arithmetical theory $I \Delta_0$ (where I stands for “induction”), is similar to Peano Arithmetic, except that it allows less induction: the induction scheme

$$ A(0) \wedge \forall x\, (A(x) \rightarrow A(\bs x)) \rightarrow \forall x \, A(x) $$

is restricted to $\Delta_0$-formulas $A$.

As De Jongh and others (1991) pointed out, arithmetical completeness certainly holds for theories $T$ that satisfy the following two conditions:

1. $T$ proves induction for $\Delta_0$-formulas, and $T$ proves EXP, the formula expressing that for all $x$, its power $2^x$ exists. In more standard notation: $T$ extends $I \Delta_0$+EXP;
2. $T$ does not prove any false sentences of the form $\exists x\, A(x)$, with $A(x)$ a $\Delta_0$-formula.

For such theories, arithmetical soundness and completeness of GL hold, provided that $\Box$ translates to $\Prov_T$, a natural provability predicate with respect to a sufficiently simple axiomatization of $T$. Thus for modal sentences $A$:

$$ \GL \vdash A \text{ if and only if for all realizations } f,T \vdash f(A). $$

It is not clear yet whether Condition 1 gives a lower bound on the scope of provability logic. For example, it is still an open question whether GL is the provability logic of $I \Delta_0+\Omega_1$, a theory which is somewhat weaker than $I \Delta_0$+EXP in that $\Omega_1$ is the axiom asserting that for all $x$, its power $x^{\log(x)}$ exists. Provability logic GL is arithmetically sound with respect to $I \Delta_0+\Omega_1$, but except for some partial results by Berarducci and Verbrugge (1993), providing arithmetic realizations consistent with $I \Delta_0+\Omega_1$ for a restricted class of sentences consistent with GL, the question remains open. Its answer may hinge on open problems in computational complexity theory.

The above result by De Jongh et al. shows a strong feature of provability logic: for many different arithmetical theories, GL captures exactly what those theories say about their own provability predicates. At the same time this is a weakness. For example, propositional provability logic does not point to any differences between those theories that are finitely axiomatizable and those that are not.

### 5.2 Interpretability logic

In order to be able to speak in a modal language about important distinctions between theories, researchers have extended provability logic in many different ways. Let us mention a few. One extension is to add a binary modality $\interprets$, where for a given arithmetical theory $T$, the modal sentence $A \interprets B$ is meant to stand for “$T+B$ is interpretable in $T+A$” (Švejdar, 1983). De Jongh and Veltman (1990) investigated modal semantics for several interpretability logics, while De Jongh and Visser (1991) proved the explicit fixed-point property for the most important ones. Visser characterized the interpretability logic of the most common finitely axiomatized theories, and Berarducci and Shavrukov independently characterized the one for PA, which is not finitely axiomatizable. It appears that indeed, the interpretability logic of finitely axiomatizable theories is different from the interpretability logic of Peano Arithmetic (see Montagna 1987; Visser 1990, 1998; Berarducci 1990, Shavrukov 1988; Joosten and Visser 2000)[^visser-1998][^berarducci-1990][^joosten-2000][^montagna-1987][^shavrukov-1988][^visser-1990][^visser-1998-2].

### 5.3 Propositional quantifiers

Another way to extend the framework of propositional provability logic is to add propositional quantifiers, so that one can express principles like Goldfarb’s:

$$ \forall p \,\forall q \,\exists r \: \Box((\Box p \vee \Box q) \leftrightarrow \Box r), $$

saying that for any two sentences there is a third sentence which is provable if and only if either of the first two sentences is provable. This principle is provable in Peano Arithmetic (see e.g. Artemov and Beklemishev 1993)[^artemov-1993]. The set of sentences of GL with propositional quantifiers that is arithmetically valid turns out to be undecidable (Shavrukov 1997)[^shavrukov-1997].

### 5.4 Japaridze’s bimodal and polymodal provability logics

Japaridze’s (1988)[^japaridze-1988] bimodal logic GLB has two $\Box$-like provability operators, denoted by $[0]$ and $[1]$, with their dual $\Diamond$-like operators $\langle 0\rangle$ and $\langle 1\rangle$, respectively. In Japaridze’s interpretation, one can think of $[0]$ as standing for the standard provability predicate in Peano Arithmetic. On the other hand, $[1]$ corresponds to a stronger provability predicate, namely *ω*-*provabilty*.

Let us define the concepts that are needed to understand this intended interpretation of GLB. An arithmetical theory $T$ is defined to be *ω*-*consistent* if and only if for all formulas A with free variable $x$, $T\vdash \neg\, A(I_n)$ for all $n$ implies that $T \not\vdash \exists x \, A(x)$; here, $I_n$ is the numeral of $n$, i.e., the term $\bs\bs\ldots\bs 0$ with $n$ occurrences of the successor operator $\bs$. Peano Arithmetic (PA) is the most well-known example of an *ω*-consistent theory (see also Gödel’s incompleteness theorems). Now let PA$^+$ be the arithmetical theory whose axioms are those of PA together with all sentences $\forall x \, \neg \, A(x)$ such that for every $n$, PA$\vdash \neg \, A(I_n)$. Now *ω*-provability is simply provability in PA$^+$, so it is the dual of *ω*-consistency.

Japaridze’s bimodal provability logic GLB can be axiomatized by the axioms and rules of GL (see Section 2), formulated separately for [0] and [1]. In addition, GLB has two mixed axioms, namely: $$\tag{Monotonicity} [0] A \rightarrow [1] A $$ $$\tag{\(\Pi^0_1\)-completeness} \langle 0\rangle A \rightarrow [1]\langle 0\rangle A $$ Japaridze’s logic is decidable and has a reasonable Kripke semantics, and it is arithmetically sound and complete with respect to Peano Arithmetic (Japaridze 1988, Boolos 1993)[^boolos-1993][^japaridze-1988].

A polymodal analogue of Japaridze’s GLB, named GLP, has received a lot of attention in recent years. GLP has infinitely many $\Box$-like provability operators, denoted by boxes $[n]$ for every natural number $n$, with their dual $\Diamond$-like operators $\langle n\rangle$. Again, one can think of $[0]$ as standing for the standard provability predicate in Peano Arithmetic, $\langle 1\rangle$ for *ω*-provability, etcetera. GLP has been axiomatized by starting from the axioms and rules of GL (see Section 2), formulated separately for each $[n]$. In addition, GLP has three mixed axiom schemes, namely, as formulated by Beklemishev (2010): $$ [m] A \rightarrow [n] A, \mbox{ for } m \leq n $$ $$ \langle k\rangle A \rightarrow [n]\langle k\rangle A, \mbox{ for } k \lt n $$ $$ [m] A \rightarrow [n][m] A, \mbox{ for } m \leq n $$

GLP has been endowed with a Kripke semantics with respect to which it is complete, and has also been shown to be arithmetically complete with respect to Peano Arithmetic (see Beklemishev 2010a, 2011a)[^beklemishev-2010a][^beklemishev-2011a]. Just like for GL, the decision problem for GLP is PSPACE-complete (Shapirovsky 2008)[^shapirovsky-2008], while its closed fragment is polynomial time decidable (Pakhomov 2014)[^pakhomov-2014].

Over the last three decades, a number of results have been proved about the polymodal logic GLP of strong provability predicates. Here follow some particularly fruitful topics:

- the closed fragment of GLP (see Ignatiev 1993; Beklemishev, Joosten and Vervoort 2005)[^beklemishev-2005][^ignatiev-1993][^beklemishev-2005-2];
- GLP and proof-theoretic ordinals (Beklemishev 2004)[^beklemishev-2004];
- Neighbourhood semantics for GLP (Shamkanov 2020)[^shamkanov-2020][^shamkanov-2020-2];
- Interpolation theorems for GLP (see Beklemishev 2010b, Shamkanov 2011)[^shamkanov-2011][^beklemishev-2010b];
- The relationship between topological semantics and set theory, among others particular large cardinal axioms and stationary reflection (see Beklemishev 2011b; Beklemishev and Gabelaia 2013, 2014; Fernández-Duque 2014; Aguilera and Fernández-Duque 2017)[^beklemishev-2011b][^beklemishev-2013][^beklemishev-2014][^fernández-duque-2014][^aguilera-2017][^beklemishev-2014-2][^beklemishev-2014-3][^fernández-duque-2014-2].

### 5.5 Predicate provability logic

Finally, one can of course study predicate provability logic. The language is that of predicate logic without function symbols, together with the operator $\Box$. Here, the situation becomes much more complex than in the case of propositional provability logic. To begin with, the straightforward quantified version of GL does not have the fixed-point property, is not complete with respect to any class of Kripke frames, and is not arithmetically complete with respect to Peano Arithmetic (Montagna, 1984; see Rybakov 2023 for recent generalizations)[^montagna-1984][^rybakov-2023]. The question then arises: Is there any nicely axiomatized predicate provability logic that is adequate, proving exactly the valid principles of provability? The answer is unfortunately a resounding no: Vardanyan (1986)[^vardanyan-1986] has proved on the basis of ideas by Artemov (1985a)[^artemov-1985a] that the set of sentences of predicate provability logic all of whose realizations are provable in PA is not even recursively enumerable but $\Pi^0_2$-complete, so it has no reasonable axiomatization. Visser and De Jonge (2006) showed that there is no escape from Vardanyan’s theorem by proving a generalization: For a wide range of arithmetical theories $T$, the set of sentences of predicate provability logic all of whose realizations are provable in $T$ turns out to be $\Pi^0_2$-complete as well. Recently, however, Borges and Joosten (2020, 2022) showed that a fragment of predicate provability logic based on a strictly positive language containing the propositional connective $\wedge$, the modal operator $\Diamond$, and the quantifier $\forall$ is arithmetically complete and still decidable.

### 5.6 Other generalizations

Left out in the above discussion are many other important strands of research in provability logic and its extensions. The interested reader is pointed to the following areas:

- the provability logic of intuitionistic arithmetic (see Troelstra 1973; Visser 1982, 1999, 2002, 2008; Iemhoff 2000, 2001, 2003; Ardeshir and Mojtahedi 2018; Litak and Visser 2018, forthcoming; Mojtahedi 2022 [Other Internet Resources]; Visser and Zoethout 2021; van der Giessen and Iemhoff 2021; van der Giessen 2023; Shillito 2023)[^shillito-2023][^ardeshir-2018][^giessen-2023][^giessen-2021][^iemhoff-2000][^iemhoff-2001][^iemhoff-2003][^litak-2018][^troelstra-1973][^visser-1982][^visser-1999][^visser-2002][^visser-2008];
- classification of provability logics (see Visser 1980, Artemov 1985b, Beklemishev 1989, Beklemishev et al. 1999)[^artemov-1985b][^beklemishev-1989][^beklemishev-1999][^beklemishev-1999-2][^visser-1980][^visser-1989][^visser-1999];
- Rosser orderings and proof speed-up (see Guaspari and Solovay 1979, Švejdar 1983, Montagna 1992)[^guaspari-1979][^montagna-1992];
- several kinds of bimodal provability logics with provability operators for different theories (see Carlson 1986; Smoryński 1985; Beklemishev 1994, 1996; Visser 1995)[^smoryński-1985][^beklemishev-1994][^beklemishev-1996][^carlson-1986][^visser-1995];
- provability logics for standard provability combined with unusual provability predicates externally enumerating PA, such as Feferman’s and Parikh’s provability predicates and slow provability predicates (see Feferman 1960; Parikh 1971; Montagna 1978; Visser 1989; Carbone and Montagna 1990; Shavrukov 1994; Lindström 1994, 2006; Henk and Pakhomov 2016 (Other Internet Resources));
- analysis of Gödel’s second incompleteness theorem using provability and interpretability logics (Visser 2016; 2020)[^visser-2016];
- the logic of explicit proofs (see Artemov 1994, 2001; Artemov and Montagna 1994; Yavorskaya 2001; Artemov and Iemhoff 2007; Kuznets and Studer 2019)[^artemov-1994][^artemov-2001][^artemov-2007][^artemov-1994-2][^kuznets-2019][^yavorskaya-2001];
- correspondence between provability logic and justification logics (see Artemov and Nogina 2005; Shamkanov 2016 (Other Internet Resources); Fitting 2020);
- relevant provability logic based on the relevance logic R (see Mares 2000)[^mares-2000];
- applications of provability logic in proof theory (see Beklemishev 1999, 2003, 2004, 2005, 2006)[^beklemishev-2004][^beklemishev-2005][^beklemishev-1999][^beklemishev-2003][^beklemishev-2005-2][^beklemishev-2006][^beklemishev-1999-2][^beklemishev-2006-2];
- proof theory of propositional modal logics closely related to the provability logic GL, namely, Grzegorczyk logic (Grz) and weak Grezgorczyk logic (wGrz) (see Litak 2007; Maksimova 2014; Goré and Ramanayake 2014; Dyckhoff and Negri 2016; Savateev and Shamkanov 2019, 2021)[^dyckhoff-2016][^goré-2014][^litak-2007][^maksimova-2014][^savateev-2019][^savateev-2021];
- positive provability logics and reflection calculus (see Beklemishev 2012, 2014, 2018a, 2018b; Dashkov 2012)[^beklemishev-2014][^beklemishev-2012][^beklemishev-2014-2][^beklemishev-2018a][^beklemishev-2018b][^beklemishev-2014-3][^dashkov-2012];
- generalizations of the polymodal provability logic GLP, namely provability logics with transfinitely many modalities (see Beklemishev et al. 2014; Fernández-Duque and Joosten 2013a, 2013b, 2014, 2018; Joosten 2021; Beklemishev and Pakhomov 2022)[^beklemishev-2014][^fernández-duque-2014][^fernández-duque-2018][^beklemishev-2014-2][^beklemishev-2014-3][^beklemishev-2022][^fernández-duque-2014-2][^fernández-duque-2013a][^fernández-duque-2013b][^joosten-2021];
- relations between provability logic and the $\mu$-calculus (see van Benthem 2006, Visser 2005, Alberucci and Facchini 2009)[^alberucci-2009][^benthem-2006][^visser-2005]; and
- provability algebras, also called diagonalizable algebras or Magari algebras (see Magari 1975a, 1975b; Montagna 1979, 1980a, 1980b; Bernardi and D’Aquino 1988; Shavrukov 1993a, 1993b, 1997; Zambella 1994; for recent results on their elementary theories, see Pakhomov 2012, 2014a (Other Internet Resources), 2015.

For the reader who would like to contribute to the area of provability logic and its generalizations, Beklemishev and Visser (2006)[^visser-2006] have proposed an annotated list of intriguing open problems.

## 6. Philosophical significance

Even though propositional provability logic is a modal logic with a kind of “necessity” operator, it withstands Quine’s (1976) controversial critique of modal notions as unintelligible, already because of its clear and unambiguous arithmetic interpretation. For example, unlike for many other modal logics, formulas with nested modalities like $\Box\Diamond p \rightarrow \Box\bot$ are not problematic, nor are there any disputes about which ones should be tautologies. In fact, provability logic embodies all the desiderata that Quine (1953)[^quine-1953] set out for syntactic treatments of modality.

Quine’s main arrows were pointed towards modal predicate logics, especially the construction of sentences that contain modal operators under the scope of quantifiers (“quantifying in”). In predicate provability logic, however, where quantifiers range over natural numbers, both *de dicto* and *de re* modalities have straightforward interpretations, contrary to the case of other modal logics (see the note on the *de dicto* / *de re* distinction). For example, formulas like

$$ \forall x\, \Box\, \exists y \,(y=x) $$

are not at all problematic. If the number $n$ is assigned to $x$, then $\Box \,\exists y\,(y = x)$ is true with respect to this assignment iff the sentence $\exists y\,(y=I_n)$ is provable in Peano Arithmetic; here, $I_n$ is the numeral of $n$, i.e., the term $\bs\bs\ldots\bs 0$ with $n$ occurrences of the successor operator $\bs$. This sentence is true for all $n$ in the standard model of the natural numbers, and $\forall x \,\Box\, \exists y \,(y = x)$ is even provable in Peano Arithmetic.

By the way, the Barcan Formula

$$ \forall x \,\Box\, A(x) \rightarrow \Box\, \forall x\, A(x) $$

is not true for the integers, let alone provable (for example, take for $A(x)$ the formula “$x$ does not code a proof of $\bot$”). Its converse

$$ \Box\, \forall x \, A(x) \rightarrow \forall x \, \Box\, A(x) $$

on the other hand, is provable in Peano Arithmetic for any formula $A$.

Provability logic has very different principles from other modal logics, even those with a seemingly similar purpose. For example, while provability logic captures provability in formal theories of arithmetic, epistemic logic endeavors to describe knowledge, which could be viewed as a kind of informal provability. In many versions of epistemic logic, one of the most important principles is the truth axiom (5):

$$ \mbox{S5} \vdash \Box A \rightarrow A, (\text{if one knows } A, \text{ then } A \text{ is true}). $$

The analogous principle clearly does not hold for GL: after all,

$$ \text{if } \GL \vdash \Box A \rightarrow A, \text{ then } \GL \vdash A. $$

Thus, it seems misguided to compare the strength of both notions or to combine them in one modal system.

Since the 1940s, there has been a lot of interest among philosophers of mathematics in the concept of informal provability or *absolute provability* (Gödel 1946, Kreisel 1967)[^gödel-1946][^kreisel-1967], including controversies about its proper definition (see Leach-Krouse 2013; Kennedy 2014; Crocco 2019; for good discussions of these controversies)[^crocco-2019][^kennedy-2014][^leach-krouse-2013]. Williamson (2016)[^williamson-2016] gives the following definition: “A mathematical hypothesis is *absolutely provable* if and only if it can in principle be known by a normal mathematical process.”. At any rate, it is clear that the concept of absolute provability is very different from the concept of *formal provability* in a given formal system, which is the central notion in the rest of this article on provability logic.

Related to the concept of absolutely provable statements is that of *absolutely undecidable statements*, namely, those statements $A$ for which neither $A$ nor $\neg A$ is absolutely provable. An interesting question is whether Gödel’s Disjunction holds: Is it the case that either “the mind cannot be mechanized ” or “there are absolutely undecidable statements”? Fascinating takes on this question can be found in (Koellner 2016, Leach-Krouse 2016, Williamson 2016)[^koellner-2016][^leach-krouse-2016][^williamson-2016].

Discussions of the consequences of Gödel’s incompleteness theorems sometimes involve confusion around the notion of provability, giving rise to claims that humans could beat formal systems in “knowing” theorems; see (Davis 1990, 1993; Franzén 1995; Lindström 2001)[^davis-1990][^davis-1993][^lindström-2001] for good critical discussions of such claims.

All in all, formal provability is a precisely defined concept, much more so than truth and knowledge. Thus, self-reference within the scope of provability does not lead to semantic paradoxes like the Liar. Instead, it has led to some of the most important results about mathematics, such as Gödel’s incompleteness theorems.

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

### General references on provability logic

### History

### Cut-elimination for provability logic

### The fixed point theorem

### Possible worlds semantics and topological semantics

### Provability and Peano Arithmetic

### The scope of provability logic: boundaries

### Interpretability logic

### Propositional quantifiers

### Japaridze’s bimodal and polymodal provability logics

### Predicate provability logic

### Other generalizations

### Philosophical significance

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=logic-provability). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/logic-provability/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=logic-provability&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/logic-provability/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

### Papers and Presentations

- Férée, H., I. van der Giessen, S. van Gool, and I. Shillito, 2024, “[Mechanised Uniform Interpolation for Modal Logics K, GL and iSL](https://arxiv.org/abs/2402.10494)”, manuscript at arxiv.org.
- Fitting, M., 2020, “[A Second GL Justification Logic](https://id144254.securedata.net/melvinfitting/bookspapers/pdf/papers/GLJustification.pdf),” manuscript available on the author’s website.
- Goré, R. and J. Kelly, 2007, “[Automated Proof Search in Gödel-Löb Provability Logic](https://www.dcs.bbk.ac.uk/~roman/blc/gore-kelly-provability.pdf),” presented at the [British Logic Colloquium](http://www.dcs.bbk.ac.uk/~roman/blc/) 2007.
- Henk, P., and Pakhomov, F., 2016, “[Slow and Ordinary Provability for Peano Arithmetic](https://arxiv.org/pdf/1602.01822v2.pdf),” manuscript at arxiv.org.
- Mojtahedi, M., 2022, “[On Provability Logic of HA](https://arxiv.org/abs/2206.00445),” manuscript at arxiv.org.
- Pakhomov, F., 2014a, “[On Elementary Theories of GLP-algebras](http://arxiv.org/abs/1412.4439),” manuscript at arxiv.org.
- Verbrugge, Rineke, [Presentation slides on provability logic](https://rinekeverbrugge.nl/wp-content/uploads/2017/02/VerbruggeProvability-Logic-clc11-1.pdf), slides, University of Groningen
- Visser, Albert, 1986, [On formal provability versus human provability](https://www.phil.uu.nl/onderwijs/cki/cki10/cki/slides/lucasac.pdf) (in Dutch), online manuscript, University of Utrecht.

### Other Sites

- [Open problems in Provability Logic](http://www.mi.ras.ru/~bekl/problems.html), maintained by Lev Beklemishev
- [Mailing list Foundations of Mathematics (FOM)](https://mathweb.ucsd.edu/~sbuss/FOM/), maintained by Sam Buss

## Related Entries

artificial intelligence: logic-based | computability and complexity | Curry’s paradox | Fitch’s paradox of knowability | Gödel, Kurt | Gödel, Kurt: incompleteness theorems | Hilbert, David: program in the foundations of mathematics | logic, history of: modal logic | logic: classical | logic: epistemic | logic: intuitionistic | logic: justification | logic: modal | logic: relevance | mathematics, philosophy of | mathematics: constructive | model theory | possible worlds | *Principia Mathematica* | proof theory: development of | Quine, Willard Van Orman | self-reference | set theory: independence and large cardinals | Turing, Alan

### Acknowledgments

I would like to express my immense gratitude to Lev Beklemishev, who was so kind as to write me a long letter in 2017, including many literature references to developments in provability logic as seen from his perspective. Thanks are also due to Albert Visser, Sara Uckelman, Rajeev Goré, Giovanni Sambin, Vítězslav Švejdar, Sara Negri, Joost Joosten, Ian Shillito, Wesley Holliday, Revantha Ramanayake, Anupam Das, Shawn Standefer, Toby Meadows, Edson Bezerra, Nils Kürbis, and Tadeusz Litak for their suggestions of improvements and additions to the 2017 and/or 2024 versions of this article.

This 2024 version of the article on provability logic is dedicated to the memory of three Nestors of provability logic and the meta-mathematics of first-order arithmetic: Franco Montagna (1948–2015), Sol Feferman (1928–2016), and Petr Hájek (1940–2016).

## Notes（原文脚注）

[^note-1]: Below we will present a more detailed proof sketch of GL $\vdash \Box\Diamond A \rightarrow \Box B$, a simple but surprising theorem that was suggested to us by Nils Kurbis. Let us first gather some ingredients. Note that in the modal logic K, so certainly in GL, we have that for each formula $ C $, the two formulas $ C \rightarrow \bot$ and $\neg C$ are logically equivalent and may be replaced by each other. The same holds for the two formulas $\Diamond C$ and $\neg\Box\neg C$. Moreover, by the Generalization Rule, the Distribution Axiom, and the Modus Ponens rule, we have the following derived rule for all formulas $C, D$: If GL $\vdash C \rightarrow D$, then GL $\vdash \Box C \rightarrow \Box D$. Here follows the promised proof sketch.

1. GL $\vdash \bot \rightarrow \neg A$ (tautology of propositional logic)
2. GL $\vdash \Box \bot \rightarrow \Box\neg A$ (from line 1 by the derived rule above)
3. GL $\vdash \bot \rightarrow B$ (tautology of propositional logic)
4. GL $\vdash \Box\bot \rightarrow \Box B$ (from line 3 by the derived rule above)
5. GL $\vdash \Box(\Box \bot \rightarrow \bot) \rightarrow \Box\bot $ (axiom GL)
6. GL $\vdash \Box(\Box \bot \rightarrow \bot) \rightarrow \Box B $ (from lines 4, 5 by hypothetical syllogism)
7. GL $\vdash \Diamond A \rightarrow (\Box \bot \rightarrow \bot) $ (from line 2 by contraposition and the above-mentioned equivalences)
8. GL $\vdash \Box\Diamond A \rightarrow \Box(\Box \bot \rightarrow \bot) $ (from line 7 by the derived rule above)
9. GL $\vdash \Box\Diamond A \rightarrow \Box B $ (from lines 6, 8 by hypothetical syllogism).

Note that semantically, it is easy to see that the formula $\Box\Diamond A \rightarrow \Box B $ is valid on transitive, conversely well-founded frames (see Section 3). After all, each formula of the form $\Box\Diamond A$ can only hold in the end-points of transitive, conversely well-founded frames; and in all the end-points of such frames, we also have $\Box\bot$, and therefore $\Box B$ for every formula $B$.

[^note-2]: It turns out that almost the same counterexample works for intuitionistic provability logic, even for the version without $\Diamond$, which was proved by Ian Shillito (2023, Theorem 13.2.1). As suggested by Rosalie Iemhoff, one only needs to replace each $\Diamond$ in the example above by $\neg\Box\neg$.

[^note-3]: Holliday and Litak (2019) strengthened this result by showing that GLB is not only Kripke frame incomplete, but even incomplete with respect to Boolean algebras for which the $\Diamond$ operator is *completely additive*, that is, for any set $X$ of elements, if $\bigvee X$ exists, then $\bigvee\{\Diamond x \mid x \in X \}$ also exists and $\Diamond\bigvee X = \bigvee\{\Diamond x \mid x \in X \}$. One of the nice aspects of their result is that the bimodal provability logic GLB is the first naturally occurring modal logic that shows such incompleteness with respect to completely additive Boolean algebras. Note that the logic that Van Benthem (1979)[^benthem-1979] originally used to show the existence of a modally incomplete logic was also a (slightly artificial) variation on provability logic, namely, $K$ with the extra axiom $\Box\Diamond\top\rightarrow \Box(\Box(\Box p \rightarrow p) \rightarrow p)$, a weakening of GL.

[^artemov-2006]: Artemov, S.N., 2006, “Modal Logic in Mathematics,” in P. Blackburn, et al. (eds.), *Handbook of Modal Logic*, Amsterdam: Elsevier, pp. 927–970.

[^artemov-2004]: Artemov, S.N. and L.D. Beklemishev, 2004, “Provability Logic,” in *Handbook of Philosophical Logic*, Second Edition, D. Gabbay and F. Guenthner, eds., Volume 13, Dordrecht: Kluwer, pp. 229–403.

[^boolos-1979]: Boolos, G., 1979, *The Unprovability of Consistency: An Essay in Modal Logic*, Cambridge: Cambridge University Press.

[^boolos-1993]: –––, 1993, *The Logic of Provability*, New York and Cambridge: Cambridge University Press.

[^jongh-1998]: de Jongh, D.H.J. and G. Japaridze, 1998, “The Logic of Provability,” in *Handbook of Proof Theory*, Buss, S.R. (ed.), Amsterdam: North-Holland, pp. 475-546.

[^lindström-1996]: Lindström, P., 1996, “Provability Logic—A Short Introduction,” *Theoria*, 52(1–2): 19–61.

[^segerberg-1971]: Segerberg, K., 1971, *An Essay in Classical Modal Logic*, Uppsala: Filosofiska Föreningen och Filosofiska Institutionen vid Uppsala Universitet.

[^logic-provability-2000]: Švejdar, V., 2000, “On Provability Logic,” *Nordic Journal of Philosophy*, 4: 95–116.

[^smoryński-1984]: Smoryński, C., 1984, “Modal Logic and Self-Reference,” in D.M. Gabbay and F. Guenthner (eds.), *Handbook of Philosophical Logic* (Volume II: Extensions of Classical Logic), Dordrecht: Springer, pp. 441–495.

[^smoryński-1985]: Smoryński, C., 1985, *Self-Reference and Modal Logic*, New York: Springer-Verlag.

[^verbrugge-1996]: Verbrugge, R. 1996, “Provability” in *The Encyclopedia of Philosophy* (Supplement), D.M. Borchert (ed.), New York: Simon and Schuster MacMillan, pp. 476–478.

[^visser-1998]: Visser, A., 1998, “Provability Logic,” in *Routledge Encyclopedia of Philosophy*, W. Craig (ed.), London: Routledge, pp. 793–797.

[^benthem-1978]: van Benthem, J.F.A.K., 1978, “Four Paradoxes,” *Journal of Philosophical Logic*, 7(1): 49–72.

[^boolos-1991]: Boolos, G. and G. Sambin, 1991, “Provability: The Emergence of a Mathematical Modality,” *Studia Logica*, 50(1): 1–23.

[^gödel-1933]: Gödel, K., 1933, “Eine Interpretation des intuitionistischen Aussagenkalküls,” *Ergebnisse eines Mathematischen Kolloquiums*, 4: 39–40; translation “An Interpretation of the Intuitionistic Propositional Calculus,” in K. Gödel, *Collected Works*, S. Feferman et al. (eds.), Oxford and New York: Oxford University Press, Volume 1, 1986, pp. 300–302.

[^gödel-1931]: –––, 1931, “Über Formal Unentscheidbare Sätze der Principia Mathematica und Verwandter Systeme I,” *Monatshefte für Mathematik und Physik*, 38: 173–198.

[^halbach-2014]: Halbach, V., and A. Visser, 2014, “The Henkin Sentence,” in M. Mazano, I. Sain, and E. Alonso (eds.), *The Life and Work of Leon Henkin: Essays on His Contributions*, Dordrecht: Springer International Publishing, pp. 249–263.

[^henkin-1952]: Henkin, L., 1952, “A Problem Concerning Provability,” *Journal of Symbolic Logic*, 17: 160.

[^henkin-1954]: –––, 1954, “Review of G. Kreisel: On a Problem of Leon Henkin’s,” *Journal of Symbolic Logic*, 19(3): 219–220.

[^hilbert-1939]: Hilbert, D. and P. Bernays, 1939, *Grundlagen der Mathematik*, volume 2, Berlin/Heidelberg/New York: Springer-Verlag.

[^jongh-nd]: de Jongh, D.H.J., forthcoming, “Notes on my Scientific Life,” in N. Bezhanishvili, R. Iemhoff and F. Yang (eds.), *Dick de Jongh on Intuitionistic and Provability Logic*, Cham: Springer.

[^kreisel-1953]: Kreisel, G., 1953, “On a Problem of Leon Henkin’s,” *Indagationes Mathematicae*, 15: 405–406.

[^lewis-1912]: Lewis, C.I., 1912, “Implication and the Algebra of Logic,” *Mind*, 21: 522–531.

[^löb-1955]: Löb, M.H., 1955, “Solution of a Problem of Leon Henkin,” *Journal of Symbolic Logic*, 20: 115–118.

[^macintyre-1973]: Macintyre, A.J. and H. Simmons, 1973, “Gödel’s Diagonalization Technique and Related Properties of Theories,” *Colloquium Mathematicum*, 28: 165–180.

[^magari-1975a]: Magari, R., 1975a, “The Diagonalizable Algebras,” *Bollettino della Unione Mathematica Italiana*, 12: 117–125.

[^magari-1975b]: –––, 1975b, “Representation and Duality Theory for Diagonalizable Algebras,” *Studia Logica*, 34(4): 305–313.

[^smiley-1963]: Smiley, T.J., 1963, “The Logical Basis of Ethics,” *Acta Philosophica Fennica*, 16: 237–246.

[^smoryński-1991]: Smoryński, C., 1991, “The Development of Self-reference: Löb’s Theorem,” in T. Drucker (ed.), *Perspectives on the History of Mathematical Logic*, Basel: Birkhäuser, pp. 110–133.

[^avron-1984]: Avron, A., 1984, “On Modal Systems Having Arithmetical Interpretations,” *The Journal of Symbolic Logic*, 49(3): 935–942.

[^bílková-2016]: Bílková, M., 2016, “Uniform Interpolation in Provability Logics,” in J. van Eijck, R. Iemhoff, and J.J. Joosten (eds.), *Liber Amicorum Alberti: A Tribute to Albert Visser*, London: College Publications, pp. 57–90.

[^goré-2008]: Goré, R. and R. Ramanayake, 2008, “Valentini’s Cut-Elimination for Provability Logic Resolved,” in *Advances in Modal Logic* (Volume 7), C. Areces and R. Goldblatt (eds.), London: College Publications, pp. 67–86.

[^goré-2012]: Goré, R. and R. Ramanayake, 2012, “Valentini’s Cut-Elimination for Provability Logic Resolved,” *Review of Symbolic Logic*, 5(2): 212–238.

[^goré-2021]: Goré, R., Ramanayake, R., and Shillito, I., 2021, “Cut-Elimination for Provability Logic by Terminating Proof-Search: Formalised and Deconstructed Using Coq,” in *Automated Reasoning with Analytic Tableaux and Related Methods: 30th International Conference, TABLEAUX 2021*, Cham: Springer International Publishing, pp. 299–313.

[^maksimova-1989a]: Maksimova, L.L., 1989a, “A Continuum of Normal Extensions of Modal Provability Logic with the Interpolation Property,” *Sibirskii Matematicheskii Zhurnal*, 30(6): 122–131.

[^maksimova-1989b]: Maksimova, L.L., 1989b, “Definability Theorems in Normal Extensions of the Probability Logic,” *Studia Logica*, 48(4): 495–507.

[^negri-2005]: Negri, S., 2005, “Proof Analysis in Modal Logic,” *Journal of Philosophical Logic*, 50: 507–544.

[^negri-2014]: Negri, S., 2014, “Proofs and Countermodels in Non-classical Logics,” *Logica Universalis*, 8(1): 25–60.

[^poggiolesi-2009]: Poggiolesi, F., 2009, “A Purely Syntactic and Cut-free Sequent Calculus for the Modal Logic of Provability,” *The Review of Symbolic Logic*, 2(4): 593–611.

[^rautenberg-1983]: Rautenberg, W., 1983, “Modal Tableau Calculi and Interpolation,” *Journal of Philosophical Logic*, 12(4): 403–423.

[^sambin-1982]: Sambin, G., and S. Valentini, 1982, “The Modal Logic of Provability. The Sequential Approach,” *Journal of Philosophical Logic*, 11(3): 311–342.

[^shamkanov-2011]: Shamkanov, D.S., 2011, “Interpolation Properties for Provability Logics GL and GLP,” *Proceedings of the Steklov Institute of Mathematics*, 274(1): 303–316.

[^shamkanov-2014]: –––, 2014, “Circular Proofs for the Gödel-Löb Provability Logic,” *Mathematical Notes*, 96(4): 575–585.

[^shamkanov-2020]: –––, 2020, “Non-well-founded Derivations in the Gödel-Löb Provability Logic,” *Review of Symbolic Logic*, 13(4): 776–796.

[^smoryński-1978]: Smoryński, C., 1978, “Beth’s Theorem and Self-referential Sentences,” *Studies in Logic and the Foundations of Mathematics*, 96: 253–261.

[^valentini-1983]: Valentini, S., 1983, “The Modal Logic of Provability: Cut-Elimination,” *Journal of Philosophical Logic*, 12: 471–476.

[^benthem-nd]: van Benthem, J., forthcoming, “An Abstract Look at the Fixed-Point Theorem for Provability Logic,” in N. Bezhanishvili, R. Iemhoff and F. Yang (eds.), *Dick de Jongh on Intuitionistic and Provability Logic*, Cham: Springer.

[^jongh-1988]: de Jongh, D.H.J., and F. Montagna, 1988, “Provable Fixed Points,” *Zeitschrift fur mathematische Logik und Grundlagen der Mathematik*, 34(3): 229–250.

[^lindström-2006]: Lindström, P., 2006, “Note on Some Fixed Point Constructions in Provability Logic,” *Journal of Philosophical Logic*, 35(3): 225–230.

[^reidhaar-olson-1990]: Reidhaar-Olson, L., 1990, “A New Proof of the Fixed-point Theorem of Provability Logic,” *Notre Dame Journal of Formal Logic*, 31(1): 37–43.

[^sambin-1976]: Sambin, G., 1976, “An Effective Fixed Point Theorem in Intuitionistic Diagonalizable Algebras (The Algebraization of the Theories Which Express Theor, IX),” *Studia Logica* 35: 345–361.

[^sambin-1982-2]: Sambin, G., and S. Valentini, 1982, “The Modal Logic of Provability. The Sequential Approach,” *Journal of Philosophical Logic*, 11(3): 311–342.

[^abashidze-1985]: Abashidze, M., 1985, “Ordinal Completeness of the Gödel-Löb Modal System,” (in Russian) in *Intensional Logics and the Logical Structure of Theories*, Tbilisi: Metsniereba, pp. 49–73.

[^aiello-2007]: Aiello, M., I. Pratt-Hartmann and J. van Benthem (eds.), 2007, *Handbook of Spatial Logics*, Berlin: Springer-Verlag.

[^beklemishev-2009]: Beklemishev, L.D. 2009, “Ordinal Completeness of Bimodal Provability Logic GLB,” In *International Tbilisi Symposium on Logic, Language, and Computation*, Berlin: Springer-Verlag, pp. 1–15.

[^beklemishev-2009-2]: Beklemishev, L.D., G. Bezhanishvili, and T. Icard, 2009, “On Topological Models of GLP,” in R. Schindler (ed.), *Ways of Proof Theory* (Ontos Mathematical Logic: Volume 2), Frankfurt: Ontos Verlag, pp. 133–153.

[^benthem-1979]: van Benthem, J.F.A.K., 1979, “Syntactic Aspects of Modal Incompleteness Theorems,” *Theoria*, 45(2): 63–77.

[^blass-1990]: Blass, A., 1990, “Infinitary Combinatorics and Modal Logic,” *Journal of Symbolic Logic*, 55(2): 761–778.

[^esakia-1981]: Esakia, L., 1981, “Diagonal Constructions, Löb’s Formula and Cantor’s Scattered Spaces,” (in Russian), in *Studies in Logic and Semantics*, Z. Mikeladze (ed.), Tbilisi: Metsniereba, pp. 128–143.

[^esakia-2003]: –––, 2003, “Intuitionistic Logic and Modality via Topology,” *Annals of Pure and Applied Logic*, 127: 155–170.

[^goré-2009]: Goré, R., 2009, “Machine Checking Proof Theory: An Application of Logic to Logic,” In *ICLA ’09: Proceedings of the 3rd Indian Conference on Logic and Its Applications*, Berlin: Springer-Verlag, pp. 23–35.

[^hakli-2012]: Hakli, R. and S. Negri, 2012, “Does the Deduction Theorem Fail for Modal Logic?,” *Synthese* 187(3): 849–867.

[^holliday-2019]: Holliday, W.H. and Litak, T., 2019, “Complete Additivity and Modal Incompleteness,” *The Review of Symbolic Logic*, 12(3): 487–535.

[^icard-2011]: Icard, T.F. III, 2011, “A Topological Study of the Closed Fragment of GLP,” *Journal of Logic and Computation*, 21(4): 683–696; first published online 2009, doi:10.1093/logcom/exp043

[^japaridze-1986]: Japaridze, G.K., 1986, *The Modal Logical Means of Investigation of Provability*, Thesis in Philosophy (in Russian), Moscow.

[^mckinsey-1944]: McKinsey, J.C.C. and A. Tarski, 1944, “The Algebra of Topology,” *Annals of Mathematics*, 45: 141–191.

[^shillito-2023]: Shillito, I., 2023, *New Foundations for the Proof Theory of Bi-Intuitionistic and Provability Logics Mechanized in Coq*, Ph.D. Thesis, Canberra: The Australian National University.

[^verbrugge-2021]: Verbrugge, R., 2021, “Zero-One Laws for Provability Logic: Axiomatizing Validity in Almost All Models and Almost All Frames,” in L. Libkin (ed.), *Proceedings of the 36th Annual ACM/IEEE Symposium on Logic in Computer Science (LICS)*, Rome: IEEE Press.

[^davis-1958]: Davis, M., 1958, *Computability and Unsolvability*, New York, McGraw-Hill; reprinted with an additional appendix, New York, Dover Publications 1983.

[^feferman-1960]: Feferman, S., 1960, “Arithmetization of Metamathematics in a General Setting,” *Fundamenta Mathematicae*, 49(1): 35–92.

[^hájek-1993]: Hájek, P. and P. Pudlák, 1993, *Metamathematics of First-Order Arithmetic*, Berlin: Springer-Verlag.

[^solovay-1976]: Solovay, R.M., 1976, “Provability Interpretations of Modal Logic,” *Israel Journal of Mathematics*, 25: 287–304.

[^berarducci-1993]: Berarducci, A. and R. Verbrugge, 1993, “On the Provability Logic of Bounded Arithmetic,” *Annals of Pure and Applied Logic*, 61: 75–93.

[^buss-1986]: Buss, S.R., 1986, *Bounded Arithmetic*, Naples: Bibliopolis.

[^jongh-1991]: de Jongh, D.H.J., M. Jumelet and F. Montagna, 1991, “On the Proof of Solovay’s Theorem,” *Studia Logica*, 50(1): 51–70.

[^parikh-1971]: Parikh, R., 1971, “Existence and Feasibility in Arithmetic“, *The Journal of Symbolic Logic*, 36(3): 494–508.

[^areces-2001]: Areces, C., Hoogland, E. and de Jongh, D.H.J., 2001, “Interpolation, Definability and Fixed-points in Interpretability Logics“, in M. Zakharyaschev, K. Segerberg, M. de Rijke and H. Wansing (eds.), *Advances in Modal Logic* (Volume 2), Stanford: CSLI Publications, pp. 35–58.

[^berarducci-1990]: Berarducci, A., 1990, “The Interpretability Logic of Peano Arithmetic,” *Journal of Symbolic Logic*, 55: 1059–1089.

[^bílková-2009]: Bílková, M., de Jongh, D. and Joosten, J.J., 2009, “Interpretability in PRA,” *Annals of Pure and Applied Logic*, 161(2): 128–138.

[^jongh-1990]: de Jongh, D.H.J., and F. Veltman, 1990, “Provability Logics for Relative Interpretability,” in P.P. Petkov (ed.), *Mathematical Logic: Proceedings of the Heyting 1988 Summer School in Varna, Bulgaria*, Boston: Plenum Press, pp. 31–42.

[^jongh-1991-2]: de Jongh, D.H.J., and A. Visser, 1991, “Explicit Fixed Points in Interpretability Logic,” *Studia Logica*, 50(1): 39–49.

[^joosten-2000]: Joosten, J.J., and Visser, A., 2000, “The Interpretability Logic of All Reasonable Arithmetical Theories,” *Erkenntnis*, 53(1-2): 3–26.

[^joosten-nd]: Joosten, J.J., Mas Rovira, J., Mikec, L., and Vuković, M., forthcoming, “An Overview of Verbrugge Semantics, a.k.a. Generalised Veltman Semantics,” in N. Bezhanishvili, R. Iemhoff and F. Yang (eds.), *Dick de Jongh on Intuitionistic and Provability Logic*, Cham: Springer.

[^mikec-2020]: Mikec, L. and Vuković, M., 2020, “Interpretability Logics and Generalised Veltman Semantics,” *The Journal of Symbolic Logic*, 85(2): 749–772.

[^montagna-1987]: Montagna, F., 1987, “Provability in Finite Subtheories of PA,” *Journal of Symbolic Logic*, 52(2): 494–511.

[^shavrukov-1988]: Shavrukov, V.Yu., 1988, “The Logic of Relative Interpretability over Peano Arithmetic,” Technical Report No. 5, Moscow: Steklov Mathematical Institute (in Russian).

[^logic-provability-1983]: Švejdar, V., 1983, “Modal Analysis of Generalized Rosser Sentences,” *Journal of Symbolic Logic*, 48: 986–999.

[^visser-1990]: Visser, A., 1990, “Interpretability Logic,” in P.P. Petkov (ed.), *Mathematical Logic: Proceedings of the Heyting 1988 Summer School in Varna, Bulgaria*, Boston: Plenum Press, pp. 175–209.

[^visser-1998-2]: –––, 1998, “An Overview of Interpretability Logic,” in M. Kracht et al. (eds.), *Advances in Modal Logic* (Volume 1), Stanford: CSLI Publications, pp. 307–359.

[^artemov-1993]: Artemov, S.N. and L.D. Beklemishev, 1993, “On Propositional Quantifiers in Provability Logic,” *Notre Dame Journal of Formal Logic*, 34: 401–419.

[^shavrukov-1997]: Shavrukov, V.Yu., 1997, “Undecidability in Diagonalizable Algebras,” *Journal of Symbolic Logic*, 62: 79–116.

[^beklemishev-2004]: Beklemishev, L.D., 2004, “Provability Algebras and Proof-Theoretic Ordinals, I,” *Annals of Pure and Applied Logic*, 128: 103–123.

[^beklemishev-2010a]: –––, 2010a, “Kripke Semantics for Provability Logic GLP,” *Annals of Pure and Applied Logic*, 161(6): 756–774.

[^beklemishev-2010b]: –––, 2010b, “On the Craig Interpolation and the Fixed Point Properties of GLP,” in S. Feferman et al. (eds.), *Proofs, Categories and Computations* (Tributes, 13), London: College Publications, pp. 49–60.

[^beklemishev-2011a]: –––, 2011a, “A Simplified Proof of Arithmetical Completeness Theorem for Provability Logic GLP,” *Proceedings Steklov Institute of Mathematics*, 274(1): 25–33.

[^beklemishev-2011b]: –––, 2011b, “Ordinal Completeness of Bimodal Provability Logic GLB,” in N. Bezhanishvili et al. (eds.), *Logic, Language, and Computation, 8th International Tbilisi Symposium TbiLLC 2009* (Lecture Notes in Computer Science: Volume 6618), Heidelberg: Springer, pp. 1–15.

[^beklemishev-2013]: Beklemishev, L.D., and D. Gabelaia, 2013, “Topological Completeness of the Provability Logic GLP,” *Annals of Pure and Applied Logic*, 164(12): 1201–1223.

[^beklemishev-2014]: –––, 2014, “Topological Interpretations of Provability Logic,“ in G. Bezhanishvili (ed.), *Leo Esakia on Duality in Modal and Intuitionistic Logics* (Outstanding Contributions to Logic: Volume 4), Heidelberg: Springer, pp. 257–290.

[^beklemishev-2005]: Beklemishev, L.D., J. Joosten and M. Vervoort, 2005, “A Finitary Treatment of the Closed Fragment of Japaridze’s Provability Logic,” *Journal of Logic and Computation*, 15(4): 447–463.

[^fernández-duque-2014]: Fernández-Duque, D. and J.J. Joosten, 2014, “Well-orders on the Transfinite Japaridze Algebra,” *Logic Journal of the IGPL*, 22 (6): 933–963.

[^fernández-duque-2018]: Fernández-Duque, D. and Joosten, J.J., 2018, “The Omega-Rule Interpretation of Transfinite Provability Logic,” *Annals of Pure and Applied Logic*, 169(4): 333–371.

[^ignatiev-1993]: Ignatiev, K.N., 1993, “On Strong Provability Predicates and the Associated Modal Logics,” *Journal of Symbolic Logic*, 58: 249–290.

[^japaridze-1988]: Japaridze, G., 1988, “The Polymodal Provability Logic,” In *Intensional Logics and the Logical Structure of Theories: Material from the Fourth Soviet-Finnish Symposium on Logic*, Telavi, pp. 16–48.

[^pakhomov-2014]: Pakhomov, F.N., 2014, “On the Complexity of the Closed Fragment of Japaridze’s Provability Logic,” *Archive for Mathematical Logic*, 53(7-8): 949–967.

[^shamkanov-2020-2]: Shamkanov, D., 2020, “Global Neighbourhood Completeness of the Provability Logic GLP,” in N. Olivetti, R. Verbrugge, S. Negri, and G. Sandu (eds.), *Proceedings Advances in Modal Logic* (Volume 13), London: College Publications, pp. 581–595.

[^artemov-1985a]: Artemov, S.N., 1985a, “Nonarithmeticity of Truth Predicate Logics of Provability,” *Doklady Akademii Nauk SSSR*, 284: 270–271 (in Russian); English translation in *Soviet Mathematics Doklady*, 32: 403–405.

[^borges-2020]: Borges, A.A. and Joosten, J.J., 2020, “Quantified Reflection Calculus with One Modality,” in N. Olivetti, R. Verbrugge, S. Negri, and G. Sandu (eds.), *Proceedings Advances in Modal Logic* (Volume 13), London: College Publications, pp. 13–32.

[^borges-2022]: –––, 2022, “An Escape from Vardanyan’s Theorem,” *The Journal of Symbolic Logic*, first online 13 May 2022. doi:10.1017/jsl.2022.38

[^borges-2022-2]: Borges, A.A., 2022, “Towards a Coq Formalization of a Quantified Modal Logic,” in C. Benzmüller and J. Otten (eds.), *Proceedings of the 4th Workshop on Automated Reasoning in Quantified Non-Classical Logics (ARQNL 2022)*, CEUR Workshop Proceedings, pp. 13–27.

[^mcgee-1987]: McGee, V. and G. Boolos, 1987, “The Degree of the Set of Sentences of Predicate Provability Logic that are True under Every Interpretation,” *Journal of Symbolic Logic*, 52: 165–171.

[^montagna-1984]: Montagna, F., 1984, “The Predicate Modal Logic of Provability,” *Notre Dame Journal of Formal Logic*, 25(2): 179–189.

[^rybakov-2023]: Rybakov, M., 2023, “Predicate Counterparts of Modal Logics of Provability: High Undecidability and Kripke Incompleteness,” *Logic Journal of the IGPL*, first online 28 February 2023. doi:10.1093/jigpal/jzad002

[^vardanyan-1986]: Vardanyan, V.A., 1986, “Arithmetic Complexiy of Predicate Logics of Provability and their Fragments,” *Doklady Akademii Nauk SSSR*, 288: 11–14 (in Russian); English translation in *Soviet Mathematics Doklady*, 33: 569–572.

[^visser-2006]: Visser, A. and M. de Jonge, 2006, “No Escape from Vardanyan’s Theorem,” *Archive of Mathematical Logic*, 45(5): 539–554.

[^aguilera-2017]: Aguilera, J.P. and Fernández-Duque, D., 2017, “Strong Completeness of Provability Logic for Ordinal Spaces,” *The Journal of Symbolic Logic*, 82(2): 608–628.

[^alberucci-2009]: Alberucci, L., and A. Facchini, 2009, “On Modal μ-Calculus and Gödel-Löb logic,” *Studia Logica*, 91: 145–169.

[^ardeshir-2018]: Ardeshir, M. and Mojtahedi, M., 2018, “The $Σ_1$-Provability Logic of HA,” *Annals of Pure and Applied Logic*, 169(10): 997–1043.

[^artemov-1985b]: Artemov, S.N., 1985b,“On Modal Logics Axiomatizing Provability,” *Izvestiya Akadademii Nauk SSSR, Seriya Matematicheskaya*, 49(6): 1123–1154 (in Russian); English translation in *Mathematics of the USSR–Izvestiya*, 27(3): 402–429.

[^artemov-1994]: –––, 1994, “Logic of Proofs,” *Annals of Pure and Applied Logic*, 67(2): 29–59.

[^artemov-2001]: –––, 2001, “Explicit Provability and Constructive Semantics,” *Bulletin of Symbolic Logic*, 7: 1–36.

[^artemov-2007]: Artemov, S.N. and R. Iemhoff, 2007, “The Basic Intuitionistic Logic of Proofs,” *Journal of Symbolic Logic*, 72(2): 439–451.

[^artemov-1994-2]: Artemov, S.N. and F. Montagna, 1994, “On First-order Theories with Provability Operator,” *Journal of Symbolic Logic*, 59(4): 1139–1153.

[^artemov-2005]: Artemov, S.N. and Nogina, E., 2005, “Introducing Justification into Epistemic Logic,” *Journal of Logic and Computation*, 15(6): 1059–1073.

[^beklemishev-1989]: Beklemishev, L.D., 1989, “On the Classification of Propositional Provability Logics,” *Izvestiya Akademii Nauk SSSR, Seriya Matematicheskaya.*, 53(5): 915–943 (in Russian); English translation in *Mathematics of the USSR–Izvestiya*, 35 (1990) 247–275.

[^beklemishev-1994]: –––, 1994, “On Bimodal Logics of Provability,” *Annals of Pure and Applied Logic*, 68: 115–160.

[^beklemishev-1996]: –––, 1996, “Bimodal Logics for Extensions of Arithmetical Theories,” *Journal of Symbolic Logic*, 61: 91–124.

[^beklemishev-1999]: –––, 1999, “Parameter-Free Induction and Provably Total Computable Functions,” *Theoretical Computer Science*, 224: 13–33.

[^beklemishev-2003]: –––, 2003, “Proof-theoretic Analysis by Iterated Reflection,” *Archive for Mathematical Logic*, 6(42): 515–552.

[^beklemishev-2005-2]: –––, 2005, “Reflection Principles and Provability Algebras in Formal Arithmetic,” *Uspekhi Matematicheskikh Nauk*, 60(2): 3–78. (in Russian); English translation in: *Russian Mathematical Surveys*, 60(2): 197–268.

[^beklemishev-2006]: –––, 2006, “The Worm Principle,” in *Lecture Notes in Logic 27. Logic Colloquium ’02*, Z. Chatzidakis, P. Koepke, and W. Pohlers (eds.), Natick (MA): AK Peters, pp. 75–95.

[^beklemishev-2012]: –––, 2012, “Calibrating Provability Logic: From Modal Logic to Reflection Calculus,” in T. Bolander, T. Braüner, S. Ghilardi, and L. Moss (eds.), *Advances in Modal Logic* (Volume 9), London: College Publications, pp. 89–94.

[^beklemishev-2014-2]: –––, 2014, “Positive Provability Logic for Uniform Reflection Principles,” *Annals of Pure and Applied Logic*, 165 (1): 82–105.

[^beklemishev-2018a]: –––, 2018a, “A Note on Strictly Positive Logics and Word Rewriting Systems,” in S. Odintsov (ed.), *Larisa Maksimova on Implication, Interpolation, and Definability* (Outstanding Contributions to Logic: Volume 15), Cham: Springer, pp.61–70.

[^beklemishev-2018b]: –––, 2018b, “Reflection Calculus and Conservativity Spectra “, *Russian Mathematical Surveys*, 73(4): 569–613.

[^beklemishev-2014-3]: Beklemishev, L.D., D. Fernández-Duque, and J.J. Joosten, 2014, “On Provability Logics with Linearly Ordered Modalities,” *Studia Logica*, 102(3): 541–566.

[^beklemishev-2022]: Beklemishev, L. D., and Pakhomov, F. N., 2022, “Reflection Algebras and Conservation Results for Theories of Iterated Truth,” *Annals of Pure and Applied Logic*, 173(5): 103093.

[^beklemishev-1999-2]: Beklemishev, L.D., M. Pentus and N. Vereshchagin, 1999, *Provability, Complexity, Grammars*, American Mathematical Society Translations (Series 2, Volume 192).

[^beklemishev-2006-2]: Beklemishev, L.D. and A. Visser, 2006, “Problems in the Logic of Provability,” in D.M. Gabbay, S.S. Goncharov and M. Zakharyashev (eds.), *Mathematical Problems from Applied Logic I: Logics for the XXIst Century* (International Mathematical Series, Volume 4), New York: Springer, pp. 77–136.

[^benthem-2006]: van Benthem, J., 2006, “Modal Frame Correspondences and Fixed-points,” *Studia Logica*, 83(1-3): 133–155.

[^bernardi-1988]: Bernardi, C. and D’Aquino, P., 1988, “Topological Duality for Diagonalizable Algebras“, *Notre Dame Journal of Formal Logic*, 29(3): 345–364.

[^carbone-1990]: Carbone, A. and Montagna, F., 1990, “Much Shorter Proofs: A Bimodal Investigation,” *Mathematical Logic Quarterly*, 36(1): 47–66.

[^carlson-1986]: Carlson, T., 1986, “Modal Logics with Several Operators and Provability Interpretations,” *Israel Journal of Mathematics*, 54(1): 14–24.

[^dashkov-2012]: Dashkov, E.V., 2012, “On the Positive Fragment of the Polymodal Provability Logic GLP,” *Mathematical Notes*, 91 (3): 318–333.

[^dyckhoff-2016]: Dyckhoff, R and Negri, S., 2016, A Cut-free Sequent System for Grzegorczyk Logic, with an Application to the Gödel–McKinsey–Tarski Embedding, *Journal of Logic and Computation*, 26: 169–187.

[^fernández-duque-2014-2]: Fernández-Duque, D., 2014, “The Polytopologies of Transfinite Provability Logic,“ *Archive for Mathematical Logic*, 53(3-4): 385–431.

[^fernández-duque-2013a]: Fernández-Duque, D. and J.J. Joosten, 2013a, “Hyperations, Veblen Progressions, and Transfinite Iteration of Ordinal Functions,” *Annals of Pure and Applied Logic* 164 (7-8): 785–801, [[available online](http://www.sciencedirect.com/science/article/pii/S0168007213000109)].

[^fernández-duque-2013b]: Fernández-Duque, D. and J.J. Joosten, 2013b, “Models of Transfinite Provability Logic,” *Journal of Symbolic Logic*, 78(2): 543–561, [[available online](http://projecteuclid.org/DPubS?service=UI&version=1.0&verb=Display&handle=euclid.jsl/1368627064)].

[^giessen-2023]: van der Giessen, I., 2023, “Admissible Rules for Six Intuitionistic Modal Logics,” *Annals of Pure and Applied Logic*, 174(4): 103233.

[^giessen-2021]: van der Giessen, I. and Iemhoff, R., 2021, “Sequent Calculi for Intuitionistic Gödel–Löb Logic,” *Notre Dame Journal of Formal Logic*, 62(2): 221–246.

[^goré-2014]: Goré, R and Ramanayake, R., 2014, “Cut-elimination for Weak Grzegorczyk Logic Go,” *Studia Logica*, 102(1): 1–27.

[^guaspari-1979]: Guaspari, D. and R.M. Solovay, 1979, “Rosser Sentences,” *Annals of Mathematical Logic*, 16: 81–99.

[^iemhoff-2000]: Iemhoff, R., 2000, “A Modal Analysis of some Principles of the Provability Logic of Heyting Arithmetic,” in *Advances in Modal Logic* (Volume 2), M. Zakharyashev et al. (eds.), Stanford: CSLI Publications, pp. 319–354.

[^iemhoff-2001]: –––, 2001, “On the Admissible Rules of Intuitionistic Propositional Logic,” *Journal of Symbolic Logic*, 66: 281–294.

[^iemhoff-2003]: –––, 2003, “Preservativity Logic: An Analogue of Interpretability Logic for Constructive Theories,” *Mathematical Logic Quarterly*, 49(3): 1–21.

[^iemhoff-2005]: Iemhoff, R., de Jongh, D. and Zhou, C., 2005, “Properties of Intuitionistic Provability and Preservativity Logics,” *Logic Journal of the IGPL*, 13(6): 615–636.

[^joosten-2021]: Joosten, J.J., 2021, “Münchhausen Provability,” *The Journal of Symbolic Logic*, 86(3): 1006–1034.

[^kuznets-2019]: Kuznets, R. and Studer, T., 2019, *Logics of Proofs and Justifications*, London: College Publications.

[^lindström-1994]: Lindström, P., 1994, “The Modal Logic of Parikh Provability,” *Filosofiska Meddelanden*, Gröna Serien, Gothenburg: Göteborgs Universitetet.

[^lindström-2006-2]: Lindström, P., 2006, “On Parikh Provability: An Exercise in Modal Logic,” in H. Lagerlund, S. Lindström, and R. Sliwinski (eds.), *Modality Matters: Twenty-Five Essays in Honour of Krister Segerberg*, Uppsala: Uppsala Philosophical Studies (Volume 53), pp. 53–287.

[^litak-2007]: Litak, L., 2007, “The Non-Reflexive Counterpart of Grz,” *Bulletin of the Section of Logic*, 36(3–4): 195–208.

[^litak-2018]: Litak, T. and Visser, A., 2018, “Lewis Meets Brouwer: Constructive Strict Implication,” *Indagationes Mathematicae*, 29(1): 36–90.

[^litak-nd]: –––, forthcoming, “Lewisian Fixed Points I: Two Incomparable Constructions,” in N. Bezhanishvili, R. Iemhoff and F. Yang (eds.), *Dick de Jongh on Intuitionistic and Provability Logic*, Cham: Springer.

[^maksimova-2014]: Maksimova, L.L., 2014, “The Lyndon Property and Uniform Interpolation over the Grzegorczyk Logic,” *Siberian Mathematical Journal*, 55(1): 118–124.

[^mares-2000]: Mares, E.D., 2000, “The Incompleteness of RGL,” *Studia Logica*, 65: 315–322.

[^mojtahedi-nd]: Mojtahedi, M., forthcoming, “The $Σ_1$-provability logic of HA revisited,” in N. Bezhanishvili, R. Iemhoff and F. Yang (eds.), *Dick de Jongh on Intuitionistic and Provability Logic*, Cham: Springer.

[^montagna-1978]: Montagna, F.,1978, “On the algebraization of a Feferman’s predicate,” *Studia Logica*, 37(3): 221–236.

[^montagna-1979]: –––, 1979, “On the Diagonalizable Algebra of Peano Arithmetic,” *Bollettino della Unione Matematica Italiana*, B(5), 16: 795–812.

[^montagna-1980a]: –––, 1980a, “Interpretations of the First-order Theory of Diagonalizable Algebras in Peano Arithmetic,” *Studia Logica*, 39: 347–354.

[^montagna-1980b]: –––, 1980b, “Undecidability of the First-order Theory of Diagonalizable Algebras, ” *Studia Logica*, 39: 355–359.

[^montagna-1992]: –––, 1992, “Polynomially and Superexponentially Shorter Proofs in Fragments of Arithmetic,” *Journal of Symbolic Logic*, 57: 844–863.

[^pakhomov-2012]: Pakhomov, F.N., 2012, “Undecidability of the Elementary Theory of the Semilattice of GLP-words,” *Sbornik: Mathematics*, 203(8): 1211.

[^pakhomov-2015]: Pakhomov, F.N., 2015, “On Elementary Theories of Ordinal Notation Systems Based on Reflection Principles,” *Proceedings of the Steklov Institute of Mathematics*, 289: 194–212.

[^savateev-2019]: Savateev, Y., and Shamkanov, D., 2019, “Cut Elimination for the Weak Modal Grzegorczyk Logic via Non-well-founded Proofs,” in R. Iemhoff, M. Moortgat, M. and R. de Queiroz (eds.), *Proceedings of WoLLIC 2019*, Heidelberg: Springer, pp. 569–583.

[^savateev-2021]: –––, 2021, “Non-well-founded Proofs for the Grzegorczyk Modal Logic,” *The Review of Symbolic Logic*, 14(1): 22–50.

[^shamkanov-2016]: Shamkanov, D.S., 2016, “A Realization Theorem for the Gödel–Löb Provability Logic,” *Sbornik: Mathematics*, 207(9): 1344–1360.

[^shapirovsky-2008]: Shapirovsky, I., 2008, “PSPACE-decidability of Japaridze’s Polymodal Logic,” *Advances in Modal Logic*, 7: 289–304.

[^shavrukov-1993a]: Shavrukov, V.Yu., 1993a, “A Note on the Diagonalizable Algebras of PA and ZF,” *Annals of Pure and Applied Logic*, 61: 161–173.

[^shavrukov-1993b]: –––, 1993b, “Subalgebras of Diagonalizable Algebras of Theories Containing Arithmetic,” *Dissertationes Mathematicae*, 323.

[^shavrukov-1994]: –––, 1994, “A Smart Child of Peano’s,” *Notre Dame Journal of Formal Logic*, 35(2): 161–185.

[^troelstra-1973]: Troelstra, A.S., 1973, *Metamathematical Investigation of Intuitionistic Arithmetic and Analysis*, Berlin: Springer-Verlag.

[^visser-1980]: Visser, A., 1980, *Aspects of Diagonalization and Provability*, Ph.D. Thesis, Utrecht: University of Utrecht.

[^visser-1982]: –––, 1982, “On the Completeness Principle: A Study of Provability in Heyting’s Arithmetic and Extensions,” *Annals of Mathematical Logic*, 22(3): 263–295.

[^visser-1989]: –––, 1989, “Peano’s Smart Children: A Provability Logical Study of Systems with Built-in Consistency,” *Notre Dame Journal of Formal Logic*, 30(2): 161–196.

[^visser-1995]: –––, 1995, “A Course on Bimodal Provability Logic,” *Annals of Pure and Applied Logic*, 73(1): 109–142.

[^visser-1999]: –––, 1999, “Rules and Arithmetics,” *Notre Dame Journal of Formal Logic*, 40(1): 116–140.

[^visser-2002]: –––, 2002, “Substitutions of $\Sigma_1$ Sentences: Explorations between Intuitionistic Propositional Logic and Intuitionistic Arithmetic,” *Annals of Pure and Applied Logic*, 114: 227–271.

[^visser-2005]: –––, 2005, “Löb’s Logic Meets the μ-Calculus,” in A. Middeldorp, V. van Oostrom, F. van Raamsdonk and R. de Vrijer (eds.), *Processes, Terms and Cycles: Steps on the Road to Infinity*, Berlin: Springer, pp. 14–25.

[^visser-2008]: –––, 2008, “Closed Fragments of Provability Logics of Constructive Theories,” *Journal of Symbolic Logic*, 73: 1081–1096.

[^visser-2016]: –––, 2016, “The Second Incompleteness Theorem: Reflections and Ruminations,” in L. Horsten and P. Welch (eds.), *Gödel’s Disjunction: The Scope and Limits of Mathematical Knowledge*, Oxford: Oxford University Press, pp. 67–91.

[^visser-2020]: –––, 2020, “Another Look at the Second Incompleteness Theorem,” *The Review of Symbolic Logic*, 13(2): 269–295.

[^visser-2019]: Visser, A. and Zoethout, J., 2019, “Provability Logic and the Completeness Principle,” *Annals of Pure and Applied Logic*, 170(6): 718–753.

[^yavorskaya-2001]: Yavorskaya, T., 2001, “Logic of Proofs and Provability,” *Annals of Pure and Applied Logic*, 113(1-3): 345–372.

[^zambella-1994]: Zambella, D., 1994, “Shavrukov’s Theorem on the Subalgebras of Diagonalizable Algebras for Theories Containing $I \Delta_0 + \exp$,” *Notre Dame Journal of Formal Logic*, 35: 147–157.

[^crocco-2019]: Crocco, G., 2019, “Informal and Absolute Proofs: Some Remarks from a Gödelian Perspective,” *Topoi*, 38: 561–575.

[^davis-1990]: Davis, M., 1990, “Is Mathematical Insight Algorithmic?,” Commentary on Roger Penrose, The Emperor’s New Mind, *Behavioral and Brain Sciences*, 13: 659–660.

[^davis-1993]: –––, 1993, “How Subtle is Gödel’s Theorem? More on Roger Penrose” (Commentary on Roger Penrose, The Emperor’s New Mind), *Behavioral and Brain Sciences*, 16: 611–612.

[^egré-2005]: Egré, P., 2005, “The Knower Paradox in the Light of Provability Interpretations of Modal Logics,” *Journal of Logic, Language, and Information*, 14(1): 13–48.

[^franzén-2005]: Franzén, T., 2005, *Gödel’s Theorem: An Incomplete Guide to its Use and Abuse*, Boca Raton, Florida: CRC Press.

[^gödel-1946]: Gödel, K., 1946, “Remarks Before the Princeton Bicentennial Conference on Problems in Mathematics,” reprinted in S. Feferman et al. (eds.), *Kurt Gödel Collected Works, Volume II: Publications 1938–1975*, New York, Oxford: Oxford University Press, 1990, pp. 150–153.

[^kaplan-1960]: Kaplan, D. and R. Montague, 1960, “A Paradox Regained,” *Notre Dame Journal of Formal Logic*, 1(3): 79–90.

[^kennedy-2014]: Kennedy, J., 2014, “Gödel’s 1946 Princeton Bicentennial Lecture: An Appreciation,” in J. Kennedy (ed.), *Interpreting Gödel: Critical Essays*, Cambridge: Cambridh=ge University Press, pp.109–130.

[^koellner-2016]: Koellner, P., 2016, “Gödel’s Disjunction,” in L. Horsten and P. Welch (eds.), *Gödel’s Disjunction: The Scope and Limits of Mathematical Knowledge*, Oxford: Oxford University Press, pp. 148–188.

[^kreisel-1967]: Kreisel, G., 1967, “Informal Rigour and Completeness Proofs,” in I. Lakatos (ed.), *Problems in the Philosophy of Mathematics*, Amsterdam: North-Holland, pp. 138–157.

[^leach-krouse-2013]: Leach-Krouse, G.E., 2013, “Conceptions of Absolute Provability,” Ph.D. Thesis, Note Dame: Notre Dame University.

[^leach-krouse-2016]: Leach-Krouse, G.E., 2016, “Provability, Mechanism, and the Diagonal Problem,” in L. Horsten and P. Welch (eds.), *Gödel’s Disjunction: The Scope and Limits of Mathematical Knowledge*, Oxford: Oxford University Press, pp. 211–242.

[^lindström-2001]: Lindström, P, 2001, “Penrose’s New Argument,” *Journal of Philosophical Logic*, 30: 241–250.

[^montague-1963]: Montague, R., 1963, “Syntactical Treatments of Modality, with Corollaries on Reflection Principles and Finite Axiomatizability,” *Acta Philosophica Fennica*, 16: 153–67.

[^quine-1966]: Quine, W.V., 1966, “Necessary Truth,” in Quine, W.V., *The Ways of Paradox and Other Essays*, New York: Random House, pp. 48–56.

[^quine-1953]: –––, 1953, “Three Grades of Modal Involvement,” in *Proceedings of the 11th International Congress of Philosophy*, Amsterdam: North-Holland, pp. 65-81; reprinted in W.V. Quine, *The Ways of Paradox and Other Essays*, New York: Random House, 1966, pp. 156–174.

[^vos-2023]: de Vos, M., Verbrugge, R., and Kooi, B., 2023, “Solutions to the Knower Paradox in the Light of Haack’s Criteria,” *Journal of Philosophical Logic*, 52: 1101–1132.

[^williamson-2016]: Williamson, T., 2016, “Absolute Provability and Safe Knowledge of Axioms,” in L. Horsten and P. Welch (eds.), *Gödel’s Disjunction: The Scope and Limits of Mathematical Knowledge*, pp. 243–253.
