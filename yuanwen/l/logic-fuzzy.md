# Fuzzy Logic
**First published Tue Nov 15, 2016; substantive revision Thu Nov 11, 2021**

*Cintula, Petr, Fermüller, Christian G., Noguera, Carles*

Fuzzy logic is intended to model logical reasoning with vague or imprecise statements like “Petr is young (rich, tall, hungry, etc.)”. It refers to a family of many-valued logics, where the truth-values are interpreted as degrees of truth. The truth-value of a logically compound proposition, like “Carles is tall and Chris is rich”, is determined by the truth-value of its components. In other words, like in classical logic, one imposes truth-functionality.

Fuzzy logic emerged in the context of the theory of fuzzy sets, introduced by Lotfi Zadeh (1965)[^zadeh-1965]. A fuzzy set assigns a degree of membership, typically a real number from the interval $[0,1]$, to elements of a universe. Fuzzy logic arises by assigning degrees of truth to propositions. The standard set of truth-values (degrees) is the real unit interval $[0,1]$, where $0$ represents “totally false”, $1$ represents “totally true”, and the other values refer to partial truth, i.e., intermediate degrees of truth.[^note-1]

“Fuzzy logic” is often understood in a very wide sense which includes all kinds of formalisms and techniques referring to the systematic handling of *degrees* of some kind (see, e.g., Nguyen & Walker 2000). In particular in engineering contexts (fuzzy control, fuzzy classification, soft computing) it is aimed at efficient computational methods tolerant to suboptimality and imprecision (see, e.g., Ross 2010). This entry focuses on fuzzy logic in a restricted sense, established as a discipline of mathematical logic following the seminal monograph by Petr Hájek (1998)[^hájek-1998] and nowadays usually referred to as “mathematical fuzzy logic”. For details about the history of different variants of fuzzy logic we refer to Bělohlávek, Dauben, & Klir 2017.

Mathematical fuzzy logic focuses on logics based on a truth-functional account of partial truth and studies them in the spirit of classical mathematical logic, investigating syntax, model-theoretic semantics, proof systems, completeness, etc., both, at the propositional and the predicate level (see Cintula, Fermüller, Hájek, & Noguera 2011 and 2015)[^cintula-2015][^cintula-2011][^fermüller-2015][^hájek-2011].

## 1. Fuzzy connectives based on t-norms

The standard set of truth-values for fuzzy logics is the real unit interval $[0,1]$ with its natural ordering $\leq$, ranging from total falsity (represented by $0$) to total truth (represented by $1$) through a continuum of intermediate degrees of truth (see Sections 5 and 7 for alternative interpretations of truth constants and alternative sets of truth-values). A fundamental assumption of (mainstream) mathematical fuzzy logic is that connectives are to be interpreted truth-functionally over the set of degrees of truth. Such truth functions are assumed, in the standard setting, to behave classically on the extremal values $0$ and $1$. A very natural behavior of conjunction, disjunction, and negation is achieved by imposing $x \land y = \min\{x,y\}$, $x \lor y = \max\{x,y\}$, and $\neg x = 1 - x$ for each $x,y \in [0,1]$.

These three truth functions yield the original semantics of fuzzy logic proposed by Joseph Goguen (1975), later studied formally by, e.g., Gehrke, Walker, & Walker (1997). Many researchers still refer to it as “the fuzzy logic”. However, it has soon become apparent that this semantic framework is too poor to (1) encode/model numerous interesting aspects of reasoning and (2) to support a fully fledged theory of mathematical logic.

Another, non-idempotent, conjunction $\&$ is typically added to account for the intuition that applying a partially true hypothesis twice might lead to a different degree of truth than using it only once. Such a conjunction is usually interpreted by a binary operation on $[0,1]$, which is not necessarily idempotent, but still associative, commutative, non-decreasing in both arguments and has $1$ as neutral element. These operations are called *t-norms* (*triangular norms*) and their mathematical properties have been thoroughly studied (see Klement, Mesiar, & Pap 2000)[^klement-2000]. Prominent examples of t-norms are the already mentioned function $\min$, the standard product $\cdot$ of real numbers, and the Łukasiewicz t-norm: $x *_{Ł} y=\max\{x+y-1,0\}$. These three t-norms are actually continuous functions and any other continuous t-norm can be described as an *ordinal sum* of these three basic ones (Ling 1965; Mostert & Shields 1957)[^ling-1965][^mostert-1957].

Interestingly, each left-continuous t-norm determines a suitable choice for implication. Indeed, it is known that a t-norm $\ast$ is left-continuous if, and only if, there is a unique binary operation $\Rightarrow_\ast$ on $[0,1]$ satisfying the so-called *residuation condition:* $$ x \ast y \leq z\ \text{ if and only if }\ x \leq y \Rightarrow_\ast z. $$ The function $\Rightarrow_\ast$ is known as *residuum of $\ast$*, and it can be shown that $x \Rightarrow_\ast y = \max\{z \mid x \ast z \leq y\}$. The residua of the three mentioned prominent t-norms are: $x \Rightarrow_\min y = 1$ if $x\leq y$ and $y$ otherwise; $x \Rightarrow_\cdot y = 1$ if $x\leq y$ and $\frac{y}{x}$ otherwise; and $x \Rightarrow_{Ł} y = \min\{1, 1 - x+y\}$.

In the general t-norm setting, the negation is interpreted using the residuum. Namely, for a given left-continuous t-norm $\ast$ we set $\neg_\ast x = x\Rightarrow_\ast 0$. For the Łukasiewicz t-norm we obtain the negation $\neg_{Ł} x = 1 - x$ (known as Łukasiewicz negation or the standard involutive negation) whereas for the minimum and the product t-norms we obtain the same negation (known as Gödel negation): $\neg_\mathrm{G} 0 = 1$ and $0$ otherwise.

## 2. MTL: A fundamental fuzzy logic

The weakest logic with connectives interpreted by truth functions of the type described above is MTL (*Monoidal T-norm based Logic*, Esteva & Godo 2001)[^esteva-2001][^esteva-2001-2]. It is a logic with the primitive binary connectives $\mathbin{\&}, \to, \wedge$ and a truth-constant $\overline{0}$, and derivable connectives defined as: $$ \begin{align} \varphi \lor \psi &= ((\varphi \to \psi) \to \psi) \land ((\psi \to \varphi) \to \varphi),\\ \neg \varphi &= \varphi \to \overline{0}, \\ \varphi \leftrightarrow \psi &= (\varphi \to \psi) \land (\psi \to \varphi),\\ \overline{1} &= \neg \overline{0}. \end{align} $$ MTL is defined as a consequence relation by means of the semantics given by all left-continuous t-norms. Namely, given a particular left-continuous t-norm $\ast$ and a mapping from propositional variables to $[0,1]$, we define the $\ast$-evaluation of all formulas by interpreting $\&$ as $\ast$, the implication $\to$ as its residuum $\Rightarrow$, and $\land$ and $\overline{0}$ as $\min$ and $0$, respectively.

A formula *φ* is a consequence of a set of formulas *Γ* in MTL, denoted $\Gamma \models_\mathrm{MTL} \varphi$, if for each left-continuous t-norm $\ast$ and each $\ast$-evaluation $e$ such that $e(\psi) = 1$ for each $\psi \in \Gamma$ we have $e(\varphi) = 1$; in words, if the premises are totally true, so is the conclusion. A formula *φ* that always evaluates to $1$ (i.e. $\emptyset\models_\mathrm{MTL}\varphi$) is called valid or a tautology of MTL. Note that the formula $\varphi \mathbin{\&} \psi \to \varphi \land \psi$ is a tautology in MTL but the converse implication $\varphi \land \psi \to \varphi \mathbin{\&} \psi$ is not, i.e., the conjunction $\&$ is stronger than $\land$.

MTL can also be presented by a Hilbert-style proof system with the following axioms:

$$ \begin{align} (\varphi \to \psi) & \to ((\psi \to \chi) \to (\varphi \to \chi)) \\ \varphi \mathbin{\&} \psi & \to \varphi \\ \varphi\mathbin{\&}\psi & \to\psi\mathbin{\&}\varphi \\ \varphi \land \psi & \to \varphi \\ \varphi \land \psi & \to \psi \land \varphi \\ (\chi \to \varphi) & \to ((\chi\to \psi) \to (\chi \to \varphi\wedge \psi)) \\ (\varphi\mathbin{\&}\psi \to \chi) & \to (\varphi\to(\psi \to \chi)) \\ (\varphi\to(\psi \to \chi)) & \to (\varphi\mathbin{\&}\psi \to \chi) \\ ((\varphi \to \psi) \to \chi) & \to (((\psi \to \varphi)\to \chi)\to \chi) \\ \overline{0}& \to\varphi \\ \end{align} $$

and *modus ponens* as the only inference rule: from *φ* and $\varphi \to \psi$, infer *ψ*. We write $\Gamma \vdash_\mathrm{MTL} \varphi$ whenever there is a proof of *φ* from *Γ* in this system, i.e. there is a finite sequence of formulas which ends with *φ* and its members are instances of the axioms, elements of *Γ*, or follow from previous ones by the inference rule (*modus ponens*). This Hilbert-style system is a strongly complete (finitary) axiomatization of the logic MTL, i.e. for each set of premises *Γ* we have: $\Gamma \models_\mathrm{MTL} \varphi$ iff $\Gamma \vdash_\mathrm{MTL} \varphi$. The validity problem of $\mathrm{MTL}$ is known to be decidable, however its computational complexity has not yet been determined.

## 3. Łukasiewicz logic

Łukasiewicz logic can be defined by adding the axiom (known as Wajsberg axiom)$$((\varphi \to \psi) \to \psi) \to ((\psi \to \varphi) \to \varphi)$$ to the Hilbert-style proof system for MTL. It corresponds to the finitary version of the consequence relation defined with respect to evaluations based on the Łukasiewicz t-norm (in symbols: for each *finite* set of formulas *Γ* and each formula *φ*, we have $\Gamma \models_{Ł} \varphi$ iff $\Gamma \vdash_{Ł} \varphi$).[^note-2]

This logic was an early example of a many-valued logic, introduced by Jan Łukasiewicz and Alfred Tarski (1930), well before the inception of the theory of fuzzy sets, by means of an equivalent axiomatic system (with *modus ponens* as the only inference rule):

$$ \begin{align} \varphi &\to (\psi \to \varphi)\\ (\varphi \to \psi) &\to ((\psi \to \chi) \to (\varphi \to \chi))\\ ((\varphi \to \psi) \to \psi) &\to ((\psi \to \varphi) \to \varphi)\\ (\neg \psi \to \neg \varphi) &\to (\varphi \to \psi)\\ ((\varphi \to \psi) &\to (\psi \to \varphi)) \to (\psi \to \varphi). \end{align} $$

Łukasiewicz logic is the only t-norm based fuzzy logic where all connectives are interpreted by continuous functions, including the implication given by the function $x \Rightarrow_{Ł} y=\min\{1,1-x+y\}$. McNaughton’s theorem (1951) states that real-valued functions over [0,1] that interpret formulas of Łukasiewicz logic are exactly the continuous piecewise linear functions with integer coefficients. In terms of computational complexity, the validity problem for this logic is asymptotically not worse than in classical logic: it remains coNP-complete.

## 4. Gödel–Dummett logic

Gödel–Dummett logic, also known as Dummett’s LC or simply as Gödel logic, is another early example of a many-valued logic with truth-values in $[0,1]$. It was introduced by Michael Dummett (1959)[^dummett-1959] as the extension of intuitionistic logic by the axiom $$(\varphi \to \psi) \lor (\psi \to \varphi).$$ This formula enforces a linear order in the underlying (Kripke-style as well as algebraic) semantics. It also appears in the context of Kurt Gödel’s observation that it is impossible to characterize intuitionistic logic by finite truth tables (Gödel 1932)[^gödel-1932]. In the fuzzy logic setting, Gödel–Dummett logic can alternatively be obtained as an axiomatic extension of MTL by adding the axiom $\varphi \to \varphi \mathbin{\&} \varphi$, which amounts to requiring the idempotence of $\&$, and hence the interpretation of both conjunctions coincides. Semantically, Gödel–Dummett logic can also be defined as the consequence relation given by the minimum t-norm. It is distinguished as the only t-norm based logic where the validity of a formula in a given evaluation does not depend on the specific values assigned to the propositional variables, but only on the relative order of these values. In this sense, Gödel–Dummett logic can be seen as a logic of comparative truth. Like for Łukasiewicz logic, the computational complexity of testing validity remains coNP-complete.

## 5. Other notable fuzzy logics

Besides MTL (the logic of all left-continuous t-norms) and Łukasiewicz and Gödel–Dummett logics (each induced by a particular t-norm), one can consider logics *induced* by sets of t-norms or, in general, arbitrary axiomatic extensions of MTL. In particular, the logic of all *continuous* t-norms (Hájek’s basic fuzzy logic BL) is obtained by adding the axiom $$\varphi\mathbin{\&}(\varphi\to{{\psi}}) \to \psi\mathbin{\&}(\psi\to\varphi)$$ to those of MTL. Actually, for any set of continuous t-norms there is a finite axiomatization of the corresponding logic (Esteva, Godo, & Montagna 2003; Haniková 2014)[^esteva-2003][^esteva-2003-2][^haniková-2014]; in most cases the axiomatization captures semantic consequence from *finite* sets of premises. In particular, the logic of the third prominent continuous t-norm (algebraic product), known as Product logic, is the extension of BL by the axiom $$\neg\varphi \vee ((\varphi\to\varphi\mathbin{\&}{{\psi}})\to{{\psi}}).$$ On the other hand, not all axiomatic extensions of MTL can be given a t-norm based semantics. For example, classical logic can be axiomatized as MTL $+$ $\varphi\vee\neg \varphi$, but the axiom of excluded middle is not a tautology under any t-norm based interpretation.

There are also reasons to consider weaker fuzzy logics. For example, it can be argued that the assumptions forcing the interpretation of the conjunction & to be a t-norm are too strong. In particular, the assumption that $1$ is its neutral element enforces a definition of tautology as a formula always evaluated to $1$ and the consequence relation as preservation of the value $1$ – that is, $1$ is the only *designated value* in the semantics.[^note-3] A natural way to introduce logics with more than one designated truth-degree is to assume that the neutral element for the interpretation of & is a number $t <1$. It can be shown that in this situation the designated truth-degrees are exactly those greater than or equal to $t$. Such interpretations of conjunctions are called *uninorms*. The logic of left-continuous uninorms was axiomatized in Metcalfe & Montagna (2007).

Analogously, one may argue against commutativity or even against associativity of &. Axiomatizations of resulting logics are described in the literature (see Cintula, Horčík, & Noguera 2013; Jenei & Montagna 2003)[^cintula-2013]; an exception is the logic of non-commutative uninorms for which no natural axiomatic system is known.

Finally, taking into account that fuzzy logics, unlike classical logic, are typically not functionally complete, one can increase their expressive power by adding new connectives. The most commonly considered connectives are: truth-constants $\bar r$ for each rational number $r\in (0,1)$; unary connectives $\sim$ and $\triangle$ interpreted as ${\sim}x = 1-x$ and $\triangle x = 1$ if $x=1$ and $0$ otherwise; a binary connective $\odot$ interpreted as the usual algebraic product, etc. (Baaz 1996; Esteva, Gispert, Godo, & Noguera 2007; Esteva, Godo, & Montagna 2001; Esteva, Godo, Hájek, & Navara 2000)[^baaz-1996][^esteva-2007][^esteva-2001][^esteva-2000][^esteva-2001-2][^godo-2000][^hájek-2000][^montagna-2001].

A thorough overview of all the kinds of propositional fuzzy logics mentioned in this section (and a general theory thereof) can be found in the *Handbook of Mathematical Fuzzy Logic* (3 volumes, Cintula et al. 2011a,b, 2015)[^cintula-2015][^cintula-2011a].

## 6. Predicate logics

The propositional logic MTL can be given a first-order counterpart MTL$\forall$ in a predicate language $\mathcal{P\!L}$ (defined as in the classical case) in the following way. The semantics is given by structures in which predicate symbols are interpreted as functions mapping tuples of domain elements into truth-values. More precisely, given a left-continuous t-norm $\ast$, a $\ast$-structure ${\mathbf M}$ consists of a non-empty domain of elements $M$, a function $f_{\mathbf M}\colon M^n\to M$ for each $n$-ary function symbol $f\in \mathcal{P\!L}$, and a function $P_{\mathbf M}\colon M^n\to [0,1]$ for each $n$-ary predicate symbol $P\in \mathcal{P\!L}$. Fixing a valuation ${\mathrm v}$ of object variables in $M$, one defines values of terms ($\|f(t_1,\dots,t_n)\|^{\mathbf M}_{\mathrm v} = f_{\mathbf M}(\|t_1\|^{\mathbf M}_{\mathrm v},\dots,\|t_n\|^{\mathbf M}_{\mathrm v})$) and truth-values of atomic formulas ($\|P(t_1,\dots,t_n)\|^{\mathbf M}_{\mathrm v} = P_{\mathbf M}(\|t_1\|^{\mathbf M}_{\mathrm v},\dots,\|t_n\|^{\mathbf M}_{\mathrm v})$). Truth-values of a universally/existentially quantified formula are computed as infimum/supremum of truth-values of instances of the formula where the quantified variable runs over all elements of the domain $M$. Formally: $$ \begin{align} \|\forall x\, \varphi\|^{\mathbf M}_{\mathrm v} & = \inf\{\|\varphi\|^{\mathbf M}_{{\mathrm v}[x{:}a]} \mid a\in M\}\\ \|\exists x\,\varphi\|^{\mathbf M}_{\mathrm v} & = \sup\{\|\varphi\|^{\mathbf M}_{{\mathrm v}[x{:}a]}\mid a\in M\},\\ \end{align} $$ where ${\mathrm v}[x{:}a]$ is the valuation sending $x$ to $a$ and keeping values of other variables unchanged. The values of other formulas are computed by interpreting, as in propositional semantics, $\&$ as $\ast$, the implication $\to$ as its residuum $\Rightarrow_\ast$, and $\land$ and $\overline{0}$ as $\min$ and $0$, respectively.

The first-order logic MTL$\forall$ is then defined as the consequence relation given by the preservation of total truth (value $1$) in $\ast$-structures (allowing $\ast$ to run over all left-continuous t-norms). More precisely, we say that a first-order formula *φ* is a consequence of a set of formulas *Γ* (in symbols: $\Gamma \models_{\mathrm{MTL}\forall} \varphi$) if, for each left-continuous t-norm $\ast$ and each $\ast$-structure ${\mathbf M}$, we have $\|\varphi\|^{\mathbf M}_{\mathrm v} = 1$ for each valuation v, whenever $\|\psi\|^{\mathbf M}_{\mathrm v} = 1$ for each valuation v and each $\psi \in \Gamma$.

MTL$\forall$ can be given a strongly complete Hilbert-style proof system with the following axioms:

- (P) The first-order instances of the axioms of MTL
- $(\forall1 )$ $\forall x\,\varphi(x)\to\varphi(t)$, where the term $t$ is substitutable for $x$ in *φ*
- $(\exists1)$ $\varphi(t)\to \exists x\, \varphi(x)$, where the term $t$ is substitutable for $x$ in *φ*
- $(\forall2)$ $\forall x\,(\chi\to\varphi)\to(\chi\to \forall x\,\varphi)$, where $x$ is not free in *χ*
- $(\exists2)$ $\forall x\,(\varphi\to\chi)\to(\exists x\,\varphi\to\chi)$, where $x$ is not free in *χ*
- $(\forall3)$ $\forall x\,(\chi\vee\varphi)\to\chi\vee \forall x\,\varphi$, where $x$ is not free in *χ*.

The deduction rules of MTL$\forall$ are *modus ponens* plus the rule of *generalization:* from *φ* infer $\forall x\,\varphi$.

There are two ways of introducing first-order counterparts for other propositional t-norm based fuzzy logics. On the one hand, the axiomatization of MTL$\forall$ can be extended by adding the first-order instances of propositional axioms like those seen in the previous sections. In this manner one obtains syntactic presentations of first-order variants of, e.g., Łukasiewicz logic, Gödel–Dummett logic, Product logic, or Hájek’s basic fuzzy logic BL. On the other hand, the semantic definition of MTL$\forall$ can be easily modified by defining the consequence relations given by the corresponding (sets of) t-norms. Then, the natural question is whether, in each case, these two routes lead to the same logic (as it happened for MTL). For soundness there is no problem, as the axiomatic systems are easily checked to be sound with respect to their corresponding classes of structures. As for completeness, there is no general answer and the problem has to be considered case by case.

For Gödel–Dummett logic the axiomatic system is strongly complete with respect to its semantics. However, the set of tautologies of the semantics for Łukasiewicz logic is not recursively axiomatizable as shown by Bruno Scarpellini (1962)[^scarpellini-1962]. Emil Ragaz (1981)[^ragaz-1981] proved that it is actually $\Sigma_2$-complete in the sense of arithmetical hierarchy. The situation is even worse in the case of Product logic and Hájek’s basic fuzzy logic BL, where the sets of first-order tautologies of all structures given by continuous t-norms are as complex as true arithmetics (Montagna 2001)[^montagna-2001]. Completeness can be achieved either by adding a suitable infinitary inference rule to the Hilbert-style proof system, as done by Louise Hay (1963)[^hay-1963] for Łukasiewicz logic, or by generalizing the set of truth-values (see next section).

First-order counterparts of weaker fuzzy logics can be studied in analogous, syntactic and semantic, ways; see the survey presentation in Cintula, Horčík, & Noguera 2014.

## 7. Algebraic semantics

One of the main tools in the study of fuzzy logic is that of algebraic semantics. Roughly speaking, the idea is to replace the real unit interval with an arbitrary set and to interpret the connectives as operations of corresponding arities on that set.

An MTL-algebra, introduced by Francesc Esteva and Lluís Godo (2001), is a tuple ${\mathbf A} = \langle A, \&, \to, \wedge, \vee, \overline{0}, \overline{1} \rangle$ where

- $\langle A, \wedge, \vee, \overline{0}, \overline{1} \rangle$ is a bounded lattice
- $\langle A, \&, \overline{1} \rangle$ is a commutative monoid
- $(x\to y)\vee(y\to x) = \overline{1}$
- $x\mathbin{\&} y \leq z$ iff $x \leq y\to z$ (where $\leq$ is the lattice order induced by $\wedge$ or $\vee$).

If the lattice order is total, then ${\mathbf A}$ is called an MTL-chain. It is worth noting that MTL-algebras are a subvariety of residuated lattices which provide the algebraic semantics for substructural logics; the first pointer to the tight connection between these two families of logics.

MTL-algebras are a generalization of the t-norm based semantics explained above and provide a sound and complete semantics for MTL.[^note-4]

MTL-chains are the basic building blocks of the whole class of algebras, in the sense that each MTL-algebra can be decomposed as a *subdirect product* of chains. This implies that the logic is also complete with respect to the semantics of MTL-chains, which is then used as the first step in the proof of its completeness with respect to the t-norm based semantics (Jenei & Montagna 2002)[^jenei-2002].

Algebraic semantics is a universal tool for propositional logics. In particular, for any arbitrary fuzzy logic studied in the literature (even those not supporting a t-norm based semantics such as finite-valued fuzzy logics or the logic of non-commutative uninorms) one can find a corresponding class of algebras which can be decomposed as subdirect products of chains. This fact has led Libor Běhounek and Petr Cintula (2006)[^cintula-2006] to propose a definition of fuzzy logics as logics that are complete with respect to totally ordered algebraic structures.

The algebraic semantics can be used for first-order fuzzy logics in a rather straightforward way: just change the definition of a $\ast$-structure of the previous section to a structure that, instead of the interval [0,1] and $\ast$ and its residuum, uses an arbitary MTL-chain and its operation to compute truth-values of formulas. Given a propositional fuzzy logic, one can use this generalized semantics to obtain a recursively enumerable set of tautologies and a strong completeness theorem for a corresponding first-order Hilbert-style proof system.

## 8. Proof theory

It has been a considerable challenge to come up with analytic proof systems for fuzzy logics. These are systems that share important features, like the eliminability of cuts and the subformula property, with Gentzen’s sequent calculi for classical and intuitionistic logic (see entry on the development of proof theory). A major breakthrough has been achieved with the introduction of a hypersequent calculus for Gödel–Dummett logic by Arnon Avron (1991)[^avron-1991]. Hypersequent calculi arise from sequent calculi by defining inference rules that refer to finite multisets of sequents, rather than to single sequents. Hypersequents are interpreted, at the meta-level, as disjunctions of sequents. This interpretation implies that it is sound to add additional sequents (external weakening) or to replace multiple copies of the same sequent within a given hypersequent by a single copy of that sequent (external contraction). In the case of Gödel–Dummett logic, the rules for introducing logical connectives arise from the rules of Gentzen’s intuitionistic sequent calculus by simply adding side-hypersequents the upper and lower sequents of the original rule. For example, the sequent rule for introducing conjunction on the right-hand side $$\frac{\Gamma_1 \Rightarrow \phi \hspace{3ex} \Gamma_2 \Rightarrow \psi}{\Gamma_1,\Gamma_2 \Rightarrow \phi \wedge \psi}$$ where $\Gamma_1$ and $\Gamma_2$ are finite sequences of formulas, is turned into the following hypersequent rule: $$\frac{H \mid \Gamma_1 \Rightarrow \phi \hspace{3ex} H' \mid \Gamma_2 \Rightarrow \psi}{H \mid H' \mid \Gamma_1,\Gamma_2 \Rightarrow \phi \wedge \psi }$$ where $H$ and $H'$ denote the side-hypersequents, i.e., finite multisets of sequents added disjunctively to the exhibited sequents. This by itself does not change the corresponding logic (intuitionistic logic, in this case). The crucial additional structural rule is the so-called communication rule: $$\frac{H \mid \Gamma_1,\Pi_1 \Rightarrow \Delta_1 \hspace{3ex} H' \mid \Gamma_2,\Pi_2 \Rightarrow \Delta_2}{H \mid H' \mid \Gamma_1,\Gamma_2 \Rightarrow \Delta_1 \mid \Pi_2,\Pi_2 \Rightarrow \Delta_2}$$ Here $\Gamma_1, \Gamma_2,\Pi_1, \Pi_2$ are finite sequences of formulas; $\Delta_1$ and $\Delta_2$ are either single formulas or remain empty; $H$ and $H'$ denote the side-hypersequents, like above. To understand the impact of the communication rule, we present a derivation of the crucial axiom $(\varphi \to \psi) \lor (\psi \to \varphi)$, which features an application of this rule immediately below the intial (hyper)sequents: $$ \frac{\displaystyle\frac{\displaystyle\frac{\displaystyle\frac{\displaystyle\frac{\displaystyle\frac{\varphi \Rightarrow \varphi \hspace{5ex} \psi \Rightarrow \psi}{\varphi \Rightarrow \psi \mid \psi \Rightarrow \varphi}}{\Rightarrow \varphi \to \psi \mid \psi \Rightarrow \varphi}}{\Rightarrow \varphi \to \psi \mid\, \Rightarrow \psi \to \varphi}}{\Rightarrow (\varphi \to \psi) \vee (\psi \to \varphi) \mid\, \Rightarrow \psi \to \varphi}}{\Rightarrow (\varphi \to \psi) \vee (\psi \to \varphi) \mid\, \Rightarrow (\varphi \to \psi) \vee (\psi \to \varphi)}}{\Rightarrow (\varphi \to \psi) \lor (\psi \to \varphi)} $$

To obtain a hypersequent calculus for the fundamental fuzzy logic MTL one has to add the communication rule to a sequent system for the contraction-free version of intuitionistic logic (a well-studied example of a substructural logic). Analytic proof systems for other fuzzy logics, in particular Łukasiewicz logic, call for a more radical departure from traditional calculi, where the sequent components of hypersequents are interpreted differently than intuitionistic or classical sequents. Also labeled proof systems and various tableau calculi have been suggested. A detailed presentation of the corresponding state of the art can be found in Metcalfe, Olivetti, & Gabbay 2008 and Metcalfe 2011.

## 9. Semantics justifying truth-functionality

It is desirable, not only from a philosophical point of view, but also to a get a better grip on potential applications of fuzzy logics to relate the meaning of intermediary truth-values and corresponding logical connectives to basic models of reasoning with vague and imprecise notions. A number of such semantics that seek to justify particular choices of truth-functional connectives have been introduced. Just two of them are briefly described here.

Voting semantics is based on the idea that different agents (voters) may coherently judge the same proposition differently. The proportion of agents that accept a proposition *φ* as true may be seen as a truth-value. Without further restrictions this does not lead to a truth-functional semantics, but rather to an assignment of probabilities to propositions. But if one assigns a fixed *level of skepticism* to each agent and imposes some natural conditions that keep the judgments on logically complex statements consistent with those levels, then one can recover $\min$, $\max$, and $1-x$ as truth functions for conjunction, disjunction and negation, respectively. Details can be found in Lawry 1998.

Another intriguing model of reasoning that provides a justification for all propositional connectives of standard Łukasiewicz logic has been introduced by Robin Giles (1974)[^giles-1974]. It consists in a game, where two players, I and you, systematically reduce logically complex assertions (formulas) to simpler ones according to rules like the following:

- If I assert $\varphi \lor \psi$, then I have to assert either *φ* or *ψ*.
- If I assert $\varphi \land \psi$, then you choose one of the conjuncts and I have to assert either *φ* or *ψ*, accordingly.
- If I assert $\varphi \to \psi$, then I have to assert *ψ* if you assert *φ*.

The rules for quantified statements refer to a fixed domain, assuming that there is a constant symbol for each domain element one stipulates:

- If I assert $\forall x\, \varphi(x)$, then I have to assert $\varphi(c)$, for a constant $c$ chosen by you.
- If I assert $\exists x\, \varphi(x)$, then I have to assert $\varphi(c)$, for a constant $c$ chosen by myself.

The rules for your assertions are dual. At each state of the game an occurrence of a non-atomic formula in either the multiset of current assertions by me or by you is chosen and gets replaced by subformulas, as indicated by these rules, until only atomic assertions remain. A final game state is then evaluated according to the following betting scheme.

For each atomic formula there is a corresponding experiment which may either fail or succeed, but may show dispersion, i.e., it may yield different results when repeated. A fixed failure probability, called risk value, is assigned to each experiment and thus to each atomic formula. The players have to pay $\$$1 to the other player for each of their atomic assertion where the associated experiments fails. For any game starting with my assertion of *φ* my expected overall loss of money, if we both play rationally, can be shown to correspond to the inverse of the truth-value of *φ* evaluated in an interpretation of Łukasiewicz logic that assigns the inverse of the risk values as truth-values to atomic formulas. In particular, a formula is valid in Łukasiewicz logic if and only if, for every risk value assignment, I have a strategy that guarantees that my expected overall loss at the end of game is $0$ or negative.

Christian Fermüller and George Metcalfe (2009) have pointed out a correspondence between optimal strategies in Giles’s game and cut-free proofs in a hypersequent system for Łukasiewicz logic. The game has also been extended in Fermüller & Roschger 2014 to characterize various types of (semi-)fuzzy quantifiers, intended to model natural language expressions like “about half” or “almost all”.

Jeff Paris (2000)[^paris-2000] provided an overview over other semantics supporting various choices of truth functions; in particular, re-randomizing semantics (Hisdal 1988)[^hisdal-1988], similarity semantics (e.g., Ruspini 1991)[^ruspini-1991], acceptability semantics (Paris 1997)[^paris-1997], and approximation semantics (Paris 2000)[^paris-2000]. Let us also mention the resource-based semantics proposed in Běhounek 2009. Moreover there are different forms of evaluation games for various fuzzy logics besides the one of Giles for Łukasiewicz logic, outlined above. An overview over those semantic games was given in Fermüller 2015.

## 10. Fuzzy logic and vagueness

Modeling reasoning with vague predicates and propositions is often cited as the main motivation for introducing fuzzy logics. There are many alternative theories of vagueness, but there is a general agreement that the susceptibility to the sorites paradox is a main feature of vagueness. Consider the following version of the paradox:

- (1)$10^{100}$ is a huge number.
- (2)If $n$ is a huge number, then $n-1$ is also huge.

On the face of it, it seems not to be unreasonable to accept these two assumptions. By instantiating $n$ with $10^{100}$ in (2) and applying *modus ponens* with (1) as the other premise we conclude that $10^{100}-1$ is huge. By simply repeating this type of inference we arrive at the unreasonable statement

- (3)$0$ is a huge number.

Fuzzy logic suggests an analysis of the *sorites paradox* that respects the intuition that statement (2), while arguably not totally true, is almost true.

There are various ways to model this form of reasoning in t-norm-based fuzzy logics that dissolve the paradox. For example, one may declare that any instance of *modus ponens* is sound if the degree of truth of the conclusion is not lower than that of the strong conjunction of its premises.[^note-5] As indicated, one stipulates that every instance of (2) is true to degree $1-\epsilon$, for some very small number *ε*. Even if we declare (1) to be perfectly true, the statement that $10^{100}-1$ is huge, too, might then be less than perfectly true without sacrificing the soundness of instantiation and *modus ponens*. If, moreover, the degree of truth of the conjunction of two not perfectly true (and not perfectly false) statements is less than that of each conjunct, we may safely declare that statement (3) is perfectly false and nevertheless insist on the soundness of each step in the indicated chain of inferences. Informally speaking, the paradox disappears by assuming that repeatedly decreasing some perfectly huge number by a small amount leads to numbers of which it is less and less true that they are huge too.

An alternative truth-degree-based solution to the *sorites paradox* has been proposed in Hájek & Novák 2003. They introduce a new truth-functional connective modeling the expression “it is almost true that”. In this manner they formalize *sorites*-style reasoning within an axiomatic theory of an appropriate t-norm-based fuzzy logic.

Nicholas J.J. Smith (2005 and 2008) has argued that the so-called *closeness principle* captures the essence of vagueness. It expresses that statements of the same form about indistinguishable objects should remain close in respect of truth. It is a hallmark of many approaches to the sorites paradox that employ fuzzy logic that they are compatible with this principle.[^note-6]

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=logic-fuzzy). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/logic-fuzzy/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=logic-fuzzy&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/logic-fuzzy/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

- Hajek, Petr, “Fuzzy Logic”, *The Stanford Encyclopedia of Philosophy* (Fall 2016 Edition), Edward N. Zalta (ed.), URL = <[https://plato.stanford.edu/archives/fall2016/entries/logic-fuzzy/](https://plato.stanford.edu/archives/fall2016/entries/logic-fuzzy/)>. [This was the previous entry on fuzzy logic in the *Stanford Encyclopedia of Philosophy* — see the [version history](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=logic-fuzzy).]

## Related Entries

logic: algebraic propositional | logic: many-valued | logic: substructural | proof theory: development of | vagueness

## Notes（原文脚注）

[^note-1]: Note that truth-functionality implies that degrees of truth cannot be interpreted as probabilities or degrees of beliefs, since the latter do not combine functionally: the probability that “The sun shines at noon tomorrow and it rains at midnight” is not (just) determined by the probabilities of the two indicated events, since they are not independent in general.

[^note-2]: The equivalence does not hold for infinite sets of premises. Perhaps surprisingly, the general consequence relation is nevertheless compact in the usual sense: an infinite set of formulas is satisfiable, i.e., there is an evaluation evaluating all its formulas to $1$, whenever each finite subset is satisfiable.

[^note-3]: This follows from the residuation property and the intuition that an implication should be true if and only if the truth value of its consequent is at least as high as that of its antecedent. Indeed: $x\leq y$ iff $x \ast 1 \leq y $ iff $1 \leq x\Rightarrow y$ iff $x\Rightarrow y = 1$.

[^note-4]: An algebra $\mathbf A$ with domain [0,1] where $\wedge, \vee, \overline{0}, \overline{1}$ are $\min$, $\max$, $0$, and $1$, respectively, is an MTL-algebra if and only if $\&$ is a left-continuous t-norm and $\to$ its residuum. Taking any MTL-algebra $\mathbf A$ and defining evaluations as homomorphisms from formulas to $\mathbf A$, we can introduce the consequence relation $\models_{\mathbf A}$ in a similar fashion as done for MTL, that is, as preservation of the designated value $\overline{1}$. Then $\Gamma\vdash_\mathrm{MTL}\varphi$ iff $\Gamma\models_{\mathbf A}\varphi$ for each MTL-algebra $\mathbf A$.

[^note-5]: This amounts to require that the formula $\varphi \mathbin{\&} (\varphi \to \psi) \to \psi$ is a tautology, which is actually the case in usual fuzzy logics.

[^note-6]: This is in particular the case for formulations that are based on Łukasiewicz logic, where all connectives have continuous truth functions. Note, however, that the closeness principle arguably is not compatible with fuzzy logics like Gödel logic, that only refer to the relative *order* of truth values, but not to their metric distance.

[^supplementary-nd]: Supplementary document:

[^bibliography-nd]: [Bibliography Sorted by Topic](logic-fuzzy.readings-by-topic.md)

[^aguzzoli-2011]: Aguzzoli, Stefano, Simone Bova, and Brunella Gerla, 2011, “Free algebras and functional representation for fuzzy logics”, in Cintula, Petr, Petr Hájek, and Carles Noguera (eds.), *Handbook of Mathematical Fuzzy Logic*, Volume 2, (Mathematical Logic and Foundations, Volume 38), London: College Publications, pages 713–791.

[^avron-1991]: Avron, Arnon, 1991, “Hypersequents, Logical Consequence and Intermediate Logics for Concurrency”, *Annals of Mathematics and Artificial Intelligence*, 4(3–4): 225–248. doi:10.1007/BF01531058

[^baaz-1996]: Baaz, Matthias, 1996, “Infinite-Valued Gödel Logic with 0–1-Projections and Relativisations”, in Hájek, Petr (ed.), *Gödel’96: Logical Foundations of Mathematics, Computer Science, and Physics*, (Lecture Notes in Logic, Volume 6), Brno: Springer, pages 23–33.

[^baaz-2002]: Baaz, Matthias, Petr Hájek, Franco Montagna, and Helmut Veith, 2002, “Complexity of T-Tautologies”, *Annals of Pure and Applied Logic*, 113(1–3): 3–11.

[^baaz-2011]: Baaz, Matthias and Norbert Preining, 2011, “Gödel–Dummett Logics”, in Cintula, Petr, Petr Hájek, and Carles Noguera (eds.), *Handbook of Mathematical Fuzzy Logic*, Volume 2, (Mathematical Logic and Foundations, Volume 38), London: College Publications, pages 585–625.

[^badia-2021]: Badia, Guillermo and Carles Noguera, 2021, “Lindström theorems in graded model theory”, *Annals of Pure and Applied Logic*, 172(3): 102916. doi: 10.1016/j.apal.2020.102916

[^badia-2021-2]: –––, 2021, “A General Omitting Types Theorem in Mathematical Fuzzy Logic”, *IEEE Transactions on Fuzzy Systems*, 29(6): 1386–1394. doi: 10.1109/TFUZZ.2020.2975146

[^běhounek-2009]: Běhounek, Libor, 2009, “Fuzzy Logics Interpreted as Logics of Resources”, in Peliš, Michal (ed.), *The Logica Yearbook 2008*, London: College Publications, pages 9–21.

[^běhounek-2014]: –––, 2014, “In Which Sense Is Fuzzy Logic a Logic For Vagueness?”, in Łukasiewicz, Thomas, Rafael Peñaloza, and Anni-Yasmin Turhan (eds.), *PRUV 2014: Logics for Reasoning About Preferences, Uncertainty, and Vagueness*, (CEUR Workshop Proceedings, Volume 1205), Dresden: CEUR.

[^běhounek-2005]: Běhounek, Libor and Petr Cintula, 2005, “Fuzzy Class Theory”, *Fuzzy Sets and Systems*, 154(1): 34–55.

[^běhounek-2006]: –––, 2006, “Fuzzy Logics as the Logics of Chains”, *Fuzzy Sets and Systems*, 157(5): 604–610.

[^běhounek-2014-2]: Běhounek, Libor and Zuzana Haniková, 2014, “Set Theory and Arithmetic in Fuzzy Logic”, in Montagna, Franco (ed.), *Petr Hájek on Mathematical Fuzzy Logic*, (Outstanding Contributions to Logic, Volume 6), Cham: Springer, pages 63–89.

[^bělohlávek-2017]: Bělohlávek, Radim, Joseph W. Dauben, and George J. Klir, 2017, *Fuzzy Logic and Mathematics: A Historical Perspective*, Oxford: Oxford University Press. doi:10.1093/oso/9780190200015.001.0001

[^bělohlávek-2005]: Bělohlávek, Radim and Vilém Vychodil, 2005, *Fuzzy Equational Logic*, (Studies in Fuzziness and Soft Computing, Volume 186), Berlin and Heidelberg: Springer.

[^bobillo-2015]: Bobillo, Fernando, Marco Cerami, Francesc Esteva, Àngel García-Cerdaña, Rafael Peñaloza, and Umberto Straccia, 2015, “Fuzzy Description Logics”, in Cintula, Petr, Christian G. Fermüller, and Carles Noguera (eds.), *Handbook of Mathematical Fuzzy Logic*, Volume 3, (Mathematical Logic and Foundations, Volume 58), London: College Publications, pages 1105–1181.

[^bou-2011]: Bou, Félix, Francesc Esteva, Lluís Godo, and Ricardo Oscar Rodríguez, 2011, “On the Minimum Many-Valued Modal Logic Over a Finite Residuated Lattice”, *Journal of Logic and Computation*, 21(5): 739–790.

[^busaniche-2011]: Busaniche, Manuela and Franco Montagna, 2011, “Hájek’s Logic BL and BL-Algebras”, in Cintula, Petr, Petr Hájek, and Carles Noguera (eds.), *Handbook of Mathematical Fuzzy Logic*, Volume 1, (Mathematical Logic and Foundations, Volume 37), London: College Publications, pages 355–447.

[^ciabattoni-2012]: Ciabattoni, Agata, Nikolaos Galatos, and Kazushige Terui, 2012, “Algebraic Proof Theory for Substructural Logics: Cut-Elimination and Completions”, *Annals of Pure and Applied Logic*, 163(3): 266–290.

[^caicedo-2017]: Caicedo, Xavier, George Metcalfe, Ricardo Oscar Rodríguez, and Jonas Rogger, 2017, “Decidability of order-based modal logics”, *Journal of Computer and System Sciences*, 88: 53–74. doi:10.1016/j.jcss.2017.03.012

[^caicedo-2010]: Caicedo, Xavier and Ricardo Oscar Rodríguez, 2010, “Standard Gödel Modal Logics”, *Studia Logica*, 94(2): 189–214.

[^caicedo-2015]: –––, 2015, “Bi-modal Gödel logic over [0, 1]-valued Kripke frames”, *Journal of Logic and Computation*, 25(1): 37–55. doi: 10.1093/logcom/exs036

[^cicalese-2015]: Cicalese, Ferdinando and Franco Montagna, 2015, “Ulam–Rényi Game Based Semantics For Fuzzy Logics”, in Cintula, Petr, Christian G. Fermüller, and Carles Noguera (eds.), *Handbook of Mathematical Fuzzy Logic*, Volume 3, (Mathematical Logic and Foundations, Volume 58), London: College Publications, pages 1029–1062.

[^cignoli-1999]: Cignoli, Roberto, Itala M. D’Ottaviano, and Daniele Mundici, 1999, *Algebraic Foundations of Many-Valued Reasoning*, (Trends in Logic, Volume 7), Dordrecht: Kluwer.

[^cintula-2006]: Cintula, Petr, 2006, “Weakly Implicative (Fuzzy) Logics I: Basic Properties”, *Archive for Mathematical Logic*, 45(6): 673–704.

[^cintula-2019]: Cintula, Petr, Denisa Diaconescu, and George Metcalfe, 2019, “Skolemization and Herbrand theorems for lattice-valued logics”, *Theoretical Computer Science*, 768: 54–75. doi: 10.1016/j.tcs.2019.02.007

[^cintula-2009]: Cintula, Petr, Francesc Esteva, Joan Gispert, Lluís Godo, Franco Montagna, and Carles Noguera, 2009, “Distinguished Algebraic Semantics for T-norm Based Fuzzy Logics: Methods and Algebraic Equivalencies”, *Annals of Pure and Applied Logic*, 160(1): 53–81.

[^cintula-2015]: Cintula, Petr, Christian G. Fermüller, and Carles Noguera (eds.), 2015, *Handbook of Mathematical Fuzzy Logic*, volume 3, (Studies in Logic, Volume 58), London: College Publications.

[^cintula-2011a]: Cintula, Petr, Petr Hájek, and Carles Noguera (eds.), 2011a, *Handbook of Mathematical Fuzzy Logic*, volume 1 (Studies in Logic, Volume 37), London: College Publications.

[^cintula-2011b]: ––– (eds.), 2011b, *Handbook of Mathematical Fuzzy Logic*, volume 2 (Studies in Logic, Volume 38), London: College Publications.

[^cintula-2013]: Cintula, Petr, Rostislav Horčík, Carles Noguera, 2013, “Non-Associative Substructural Logics and their Semilinear Extensions: Axiomatization and Completeness Properties”, *The Review of Symbolic Logic*, 6(3): 394–423. doi:10.1017/S1755020313000099

[^cintula-2014]: –––, 2014, “The Quest for the Basic Fuzzy Logic”, in Montagna, Franco (ed.), *Petr Hájek on Mathematical Fuzzy Logic*, (Outstanding Contributions to Logic, Volume 6), Cham: Springer, pages 245–290. doi:10.1007/978-3-319-06233-4_12

[^cintula-2019-2]: Cintula, Petr, Paula Menchón, and Carles Noguera, 2019, “Toward a general frame semantics for modal many-valued logics”, *Soft Computing*, 23(7): 2233–2241. doi: 10.1007/s00500-018-3369-5

[^cintula-2011]: Cintula, Petr and Carles Noguera, 2011, “A General Framework for Mathematical Fuzzy Logic”, in Cintula, Petr, Petr Hájek, and Carles Noguera (eds.), *Handbook of Mathematical Fuzzy Logic*, Volume 1, (Mathematical Logic and Foundations, Volume 37), London: College Publications, pages 103–207.

[^cintula-2009-2]: Cintula, Petr and George Metcalfe, 2009, “Structural Completeness in Fuzzy Logics”, *Notre Dame Journal of Formal Logic*, 50(2): 153–183.

[^dellunde-2012]: Dellunde, Pilar, 2012, “Preserving Mappings in Fuzzy Predicate Logics”, *Journal of Logic and Computation*, 22(6): 1367–1389.

[^dellunde-2018]: Dellunde, Pilar, Àngel García-Cerdaña, and Carles Noguera, 2018, “Back-and-forth systems for fuzzy first-order models”, *Fuzzy Sets and Systems*, 345: 83–98.

[^di-1986]: Di Nola, Antonio and Giangiacomo Gerla, 1986, “Fuzzy Models of First-Order Languages”, *Zeitschrift für Mathematische Logik und Grundlagen der Mathematik*, 32(19–24): 331–340.

[^dummett-1959]: Dummett, Michael, 1959, “A Propositional Calculus with Denumerable Matrix”, *Journal of Symbolic Logic*, 24(2): 97–106. doi:10.2307/2964753

[^esteva-2007]: Esteva, Francesc, Joan Gispert, Lluís Godo, and Carles Noguera, 2007, “Adding Truth-Constants to Logics of Continuous T-norms: Axiomatization and Completeness Results”, *Fuzzy Sets and Systems*, 158(6): 597–618. doi:10.1016/j.fss.2006.11.010

[^esteva-2001]: Esteva, Francesc and Lluís Godo, 2001, “Monoidal T-norm Based Logic: Towards a Logic for Left-Continuous T-norms”, *Fuzzy Sets and Systems*, 124(3): 271–288. doi:10.1016/S0165-0114(01)00098-7

[^esteva-2003]: Esteva, Francesc, Lluís Godo, and Àngel García-Cerdaña, 2003, “On the Hierarchy of T-norm Based Residuated Fuzzy Logics”, in Fitting, Melvin and Ewa Orłowska (eds.), *Beyond Two: Theory and Applications of Multiple-Valued Logic*, (Studies in Fuzziness and Soft Computing, Volume 114), Heidelberg: Springer, pages 251–272.

[^esteva-2000]: Esteva, Francesc, Lluís Godo, Petr Hájek, and Mirko Navara, 2000, “Residuated Fuzzy Logics with an Involutive Negation”, *Archive for Mathematical Logic*, 39(2): 103–124. doi:10.1007/s001530050006

[^esteva-2011]: Esteva, Francesc, Lluís Godo, and Enrico Marchioni, 2011, “Fuzzy Logics with Enriched Language”, in Cintula, Petr, Petr Hájek, and Carles Noguera (eds.), *Handbook of Mathematical Fuzzy Logic*, Volume 2, (Mathematical Logic and Foundations, Volume 38), London: College Publications, pages 627–711.

[^esteva-2001-2]: Esteva, Francesc, Lluís Godo, and Franco Montagna, 2001, “The $L\Pi$ and $L\Pi\frac12$ Logics: Two Complete Fuzzy Systems Joining Łukasiewicz and Product Logics”, *Archive for Mathematical Logic*, 40(1): 39–67. doi:10.1007/s001530050173

[^esteva-2003-2]: –––, 2003, “Axiomatization of Any Residuated Fuzzy Logic Defined by a Continuous T-norm”, in Taner Bilgiç, Bernard De Baets, and Okyay Kaynak (eds.), *Fuzzy Sets and Systems: IFSA 2003*, (Lecture Notes in Computer Science, Volume 2715), Berlin/Heidelberg: Springer, pages 172–179. doi:10.1007/3-540-44967-1_20

[^fedel-2011]: Fedel, Martina, Hykel Hosni, and Franco Montagna, 2011, “A Logical Characterization of Coherence for Imprecise Probabilities”, *International Journal of Approximate Reasoning*, 52(8): 1147–1170, doi: 10.1016/j.ijar.2011.06.004.

[^fermüller-2015]: Fermüller, Christian G., 2015, “Semantic Games for Fuzzy Logics”, Cintula, Petr, Christian G. Fermüller, and Carles Noguera (eds.), 2015, *Handbook of Mathematical Fuzzy Logic*, volume 3, (Studies in Logic, Volume 58), London: College Publications, pages 969–1028.

[^fermüller-2009]: Fermüller, Christian G. and George Metcalfe, 2009, “Giles’s Game and Proof Theory for Łukasiewicz Logic”, *Studia Logica*, 92(1): 27–61. doi:10.1007/s11225-009-9185-2

[^fermüller-2014]: Fermüller, Christian G. and Christoph Roschger, 2014, “Randomized Game Semantics for Semi-Fuzzy Quantifiers”, *Logic Journal of the Interest Group of Pure and Applied Logic*, 22(3): 413–439. doi:10.1093/jigpal/jzt049

[^flaminio-2011]: Flaminio, Tommaso, Lluís Godo, and Enrico Marchioni, 2011, “Reasoning About Uncertainty of Fuzzy Events: An Overview”, in Cintula, Petr, Christian G. Fermüller, Lluís Godo, and Petr Hájek(eds.), *Understanding Vagueness: Logical, Philosophical, and Linguistic Perspectives*, (Studies in Logic, Volume 36), London: College Publications, pages 367–400.

[^flaminio-2015]: Flaminio, Tommaso and Tomáš Kroupa, 2015, “States of MV-Algebras”, in Cintula, Petr, Christian G. Fermüller, and Carles Noguera (eds.), *Handbook of Mathematical Fuzzy Logic*, Volume 3, (Mathematical Logic and Foundations, Volume 58), London: College Publications, pages 1183–1236.

[^font-2016]: Font, Josep Maria, 2016, *Abstract Algebraic Logic: An Introductory Textbook*, (Mathematical Logic and Foundations, Volume 60), London: College Publications.

[^galatos-2007]: Galatos, Nikolaos, Peter Jipsen, Tomasz Kowalski, and Hiroakira Ono, 2007, *Residuated Lattices: An Algebraic Glimpse at Substructural Logics*, (Studies in Logic and the Foundations of Mathematics, Volume 151), Amsterdam: Elsevier.

[^garcía-cerdaña-2010]: García-Cerdaña, Àngel, Eva Armengol, and Francesc Esteva, 2010, “Fuzzy Description Logics and T-norm Based Fuzzy Logics”, *International Journal of Approximate Reasoning*, 51(6): 632–655.

[^gehrke-1997]: Gehrke, Mai, Carol L. Walker, and Elbert A. Walker, 1997, “A Mathematical Setting for Fuzzy Logics”, *International Journal of Uncertainty, Fuzziness, and Knowledge-Based Systems*, 5(3): 223–238. doi:10.1142/S021848859700021X

[^gerla-2001]: Gerla, Giangiacomo, 2001, *Fuzzy Logic—Mathematical Tool for Approximate Reasoning*, (Trends in Logic, Volume 11), New York: Kluwer and Plenum Press.

[^giles-1974]: Giles, Robin, 1974, “A Non-Classical Logic for Physics”, *Studia Logica*, 33(4): 397–415. doi:10.1007/BF02123379

[^gödel-1932]: Gödel, Kurt, 1932, “Zum intuitionistischen Aussagenkalkül”, *Anzeiger Akademie Der Wissenschaften Wien*, 69: 65–66.

[^godo-2000]: Godo, Lluís, Francesc Esteva, and Petr Hájek, 2000, “Reasoning About Probability Using Fuzzy Logic”, *Neural Network World*, 10(5): 811–823.

[^goguen-1969]: Goguen, Joseph A., 1969, “The Logic of Inexact Concepts”, *Synthese*, 19(3–4): 325–373.

[^gottwald-2001]: Gottwald, Siegfried, 2001, *A Treatise On Many-Valued Logics*, (Studies in Logic and Computation, Volume 9), Baldock: Research Studies Press Ltd.

[^hájek-1998]: Hájek, Petr, 1998, *Metamathematics of Fuzzy Logic*, (Trends in Logic, Volume 4), Dordrecht: Kluwer.

[^hájek-2001]: –––, 2001, “On Very True”, *Fuzzy Sets and Systems*, 124(3): 329–333.

[^hájek-2005]: –––, 2005, “Making Fuzzy Description Logic More General”, *Fuzzy Sets and Systems*, 154(1): 1–15.

[^hájek-2006]: Hájek, Petr and Petr Cintula, 2006, “On Theories and Models in Fuzzy Predicate Logics”, *Journal of Symbolic Logic*, 71(3): 863–880.

[^hájek-2003]: Hájek, Petr and Zuzana Haniková, 2003, “A Development of Set Theory in Fuzzy Logic”, in Fitting, Melvin and Ewa Orłowska (eds.), *Beyond Two: Theory and Applications of Multiple-Valued Logic*, (Studies in Fuzziness and Soft Computing, Volume 114), Heidelberg: Springer, pages 273–285.

[^hájek-2011]: Hájek, Petr, Franco Montagna, Carles Noguera, 2011, “Arithmetical Complexity of First-Order Fuzzy Logics”, in Cintula, Petr, Petr Hájek, and Carles Noguera(eds.), *Handbook of Mathematical Fuzzy Logic*, Volume 2, (Mathematical Logic and Foundations, Volume 38), London: College Publications, pages 853–908.

[^hájek-2003-2]: Hájek, Petr and Vilém Novák, 2003, “The Sorites Paradox and Fuzzy Logic”, *International Journal of General Systems*, 32(4): 373–383. doi:10.1080/0308107031000152522

[^hájek-2000]: Hájek, Petr, Jeff Paris, and John C. Shepherdson, 2000, “The Liar Paradox and Fuzzy Logic”, *Journal of Symbolic Logic*, 65(1): 339–346.

[^haniková-2011]: Haniková, Zuzana, 2011, “Computational Complexity of Propositional Fuzzy Logics”, in Cintula, Petr, Petr Hájek, and Carles Noguera (eds.), *Handbook of Mathematical Fuzzy Logic*, Volume 2, (Mathematical Logic and Foundations, Volume 38), London: College Publications, pages 793–851.

[^haniková-2014]: –––, 2014, “Varieties Generated by Standard BL-Algebras”, *Order*, 31(1): 15–33. doi:10.1007/s11083-013-9285-5

[^hansoul-2013]: Hansoul, Georges and Bruno Teheux, 2013, “Extending Łukasiewicz Logics with a Modality: Algebraic Approach to Relational Semantics”, *Studia Logica*, 101(3): 505–545, doi: 10.1007/s11225-012-9396-9.

[^hay-1963]: Hay, Louise Schmir, 1963, “Axiomatization of the Infinite-Valued Predicate Calculus”, *Journal of Symbolic Logic*, 28(1): 77–86. doi:10.2307/2271339

[^hisdal-1988]: Hisdal, Ellen, 1988, “Are Grades of Membership Probabilities?” *Fuzzy Sets and Systems*, 25(3): 325–348. doi:10.1016/0165-0114(88)90018-8

[^horčík-2011]: Horčík, Rostislav, 2011, “Algebraic Semantics: Semilinear FL-Algebras”, in Cintula, Petr, Petr Hájek, and Carles Noguera (eds.), *Handbook of Mathematical Fuzzy Logic*, Volume 1, (Mathematical Logic and Foundations, Volume 37), London: College Publications, pages 283–353.

[^horn-1969]: Horn, Alfred, 1969, “Logic with Truth Values in a Linearly Ordered Heyting Algebra”, *The Journal of Symbolic Logic*, 34(3): 395–408.

[^jenei-2002]: Jenei, Sándor and Franco Montagna, 2002, “A Proof of Standard Completeness for Esteva and Godo’s Logic MTL”, *Studia Logica*, 70(2): 183–192. doi:10.1023/A:1015122331293

[^jeřábek-2010]: Jeřábek, Emil, 2010, “Bases of Admissible Rules of Łukasiewicz Logic”, *Journal of Logic and Computation*, 20(6): 1149–1163.

[^jeřábek-2003]: –––, 2003, “A Proof of Standard Completeness for Non-Commutative Monoidal T-norm Logic”, *Neural Network World*, 13(5): 481–489.

[^klement-2000]: Klement, Erich Peter, Radko Mesiar, and Endre Pap, 2000, *Triangular Norms*, (Trends in Logic, Volume 8), Dordrecht: Kluwer.

[^lawry-1998]: Lawry, Jonathan, 1998, “A Voting Mechanism for Fuzzy Logic”, *International Journal of Approximate Reasoning*, 19(3–4): 315–333. doi:10.1016/S0888-613X(98)10013-0

[^leştean-2011]: Leştean, Ioana and Antonio Di Nola, 2011, “Łukasiewicz Logic and MV-Algebras”, in Cintula, Petr, Petr Hájek, and Carles Noguera (eds.), *Handbook of Mathematical Fuzzy Logic*, Volume 2, (Mathematical Logic and Foundations, Volume 38), London: College Publications, pages 469–583.

[^ling-1965]: Ling, Cho-Hsin, 1965, “Representation of Associative Functions”, *Publicationes Mathematicae Debrecen*, 12: 189–212.

[^jan-1920]: Łukasiewicz, Jan, 1920, “O Logice Trójwartościowej”, *Ruch Filozoficzny*, 5: 170–171. English translation, “On Three-Valued Logic”, in McCall, Storrs (ed.), 1967, *Polish Logic* *1920–1939*, Oxford: Clarendon Press, pages 16–18, and in Jan Łukasiewicz, 1970, *Selected Works*, Borkowski, Ludwik (ed.), Amsterdam: North-Holland, pages 87–88.

[^jan-1930]: Łukasiewicz, Jan and Alfred Tarski, 1930, “Untersuchungen über den Aussagenkalkül”, *Comptes Rendus Des Séances de La Société Des Sciences et Des Lettres de Varsovie, Cl. III*, 23(iii): 30–50.

[^marra-2013]: Marra, Vincenzo and Luca Spada, 2013, “Duality, Projectivity, and Unification in Łukasiewicz Logic and MV-Algebras”, *Annals of Pure and Applied Logic*, 164(3): 192–210.

[^mcnaughton-1951]: McNaughton, Robert, 1951, “A Theorem About Infinite-Valued Sentential Logic”, *Journal of Symbolic Logic*, 16(1): 1–13. doi:10.2307/2268660

[^metcalfe-2011]: Metcalfe, George, 2011, “Proof Theory for Mathematical Fuzzy Logic”, Cintula, Petr, Petr Hájek, and Carles Noguera (eds.), 2011a, *Handbook of Mathematical Fuzzy Logic*, volume 1 (Studies in Logic, Volume 37), London: College Publications, pages 209–282.

[^metcalfe-2007]: Metcalfe, George and Franco Montagna, 2007, “Substructural Fuzzy Logics”, *Journal of Symbolic Logic*, 72(3): 834–864. doi:10.2178/jsl/1191333844

[^metcalfe-2008]: Metcalfe, George, Nicola Olivetti, and Dov M. Gabbay, 2008, *Proof Theory for Fuzzy Logics*, (Applied Logic Series, Volume 36), Dordrecht: Springer Netherlands.

[^montagna-2001]: Montagna, Franco, 2001, “Three Complexity Problems in Quantified Fuzzy Logic”, *Studia Logica*, 68(1): 143–152. doi:10.1023/A:1011958407631

[^montagna-2010]: Montagna, Franco and Carles Noguera, 2010, “Arithmetical Complexity of First-Order Predicate Fuzzy Logics Over Distinguished Semantics”, *Journal of Logic and Computation*, 20(2): 399–424. doi:10.1093/logcom/exp052

[^montagna-2006]: Montagna, Franco, Carles Noguera, and Rostislav Horčík, 2006, “On Weakly Cancellative Fuzzy Logics”, *Journal of Logic and Computation*, 16(4): 423–450.

[^montagna-nd]: Montagna, Franco and Hiroakira Ono, “Kripke Semantics, Undecidability and Standard Completeness for Esteva and Godo’s Logic MTL$\forall$”, *Studia Logica*, 71(2): 227–245.

[^mostert-1957]: Mostert, Paul S. and Allen L. Shields, 1957, “On the Structure of Semigroups on a Compact Manifold with Boundary”, *The Annals of Mathematics, Second Series*, 65(1): 117–143. doi:10.2307/1969668

[^mundici-1987]: Mundici, Daniele, 1987, “Satisfiability in Many-Valued Sentential Logic is NP-Complete”, *Theoretical Computer Science*, 52(1–2): 145–153.

[^mundici-1992]: –––, 1992, “The Logic of Ulam’s Game with Lies”, in Bicchieri, Cristina and Maria Luisa Dalla Chiara (eds.), *Knowledge, Belief, and Strategic Interaction* (*Castiglioncello*, *1989*), Cambridge: Cambridge University Press, 275–284.

[^mundici-2011]: –––, 2011, *Advanced Łukasiewicz Calculus and MV-Algebras*, (Trends in Logic, Volume 35), New York: Springer.

[^novák-2004]: Novák, Vilém, 2004, “On Fuzzy Type Theory”, *Fuzzy Sets and Systems*, 149(2): 235–273.

[^novák-2015]: –––, 2015, “Fuzzy Logic with Evaluated Syntax”, in Cintula, Petr, Christian G. Fermüller, and Carles Noguera (eds.), *Handbook of Mathematical Fuzzy Logic*, Volume 3, (Mathematical Logic and Foundations, Volume 58), London: College Publications, pages 1063–1104.

[^novák-2000]: Novák, Vilém, Irina Perfilieva, and Jiří Močkoř, 2000, *Mathematical Principles of Fuzzy Logic*, Dordrecht: Kluwer.

[^nguyen-2005]: Nguyen, Hung T. and Elbert A. Walker, 2005, *A First Course in Fuzzy Logic* (third edition), Chapman and Hall/CRC.

[^paris-1997]: Paris, Jeff, 1997, “A Semantics for Fuzzy Logic”, *Soft Computing*, 1(3): 143–147. doi:10.1007/s005000050015

[^paris-2000]: –––, 2000, “Semantics for Fuzzy Logic Supporting Truth Functionality”, in Vilém Novák and Irina Perfilieva (eds.), *Discovering the World with Fuzzy Logic*, (Studies in Fuzziness and Soft Computing. Volume 57), Heidelberg: Springer, pages 82–104.

[^pavelka-1979]: Pavelka, Jan, 1979, “On Fuzzy Logic I, II, and III”, *Zeitschrift für Mathematische Logik und Grundlagen der Mathematik*, 25: 45–52, 119–134, and 447–464.

[^ragaz-1981]: Ragaz, Matthias Emil, 1981, *Arithmetische Klassifikation von Formelmengen der unendlichwertigen Logik* (PhD thesis), Swiss Federal Institute of Technology, Zürich. doi:10.3929/ethz-a-000226207

[^rodríguez-2021]: Rodríguez, Ricardo Oscar and Amanda Vidal, 2021, “Axiomatization of Crisp Gödel Modal Logic”, *Studia Logica*, 109(2): 367–395. doi: 10.1007/s11225-020-09910-5

[^ross-2016]: Ross, Timothy J., 2016, *Fuzzy Logic with Engineering Applications* (fourth edition), Hoboken, NJ: Wiley.

[^ruspini-1991]: Ruspini, Enrique H., 1991, “On the Semantics of Fuzzy Logic”, *International Journal of Approximate Reasoning*, 5(1): 45–88. doi:10.1016/0888-613X(91)90006-8

[^scarpellini-1962]: Scarpellini, Bruno, 1962, “Die Nichtaxiomatisierbarkeit des unendlichwertigen Prädikatenkalküls von Łukasiewicz”, *Journal of Symbolic Logic*, 27(2): 159–170. doi:10.2307/2964111

[^smith-2005]: Smith, Nicholas J.J., 2005, “Vagueness as Closeness”, *Australasian Journal of Philosophy*, 83(2): 157–183. doi:10.1080/00048400500110826

[^smith-2008]: –––, 2008, *Vagueness and Degrees of Truth*, Oxford: Oxford University Press.

[^smith-2015]: –––, 2015, “Fuzzy Logics in Theories of Vagueness”, in Cintula, Petr, Christian G. Fermüller, and Carles Noguera (eds.), *Handbook of Mathematical Fuzzy Logic*, Volume 3, (Mathematical Logic and Foundations, Volume 58), London: College Publications, pages 1237–1281.

[^straccia-1998]: Straccia, Umberto, 1998, “A Fuzzy Description Logic”, in Mostow, Jack and Chuck Rich (eds.), *Proceedings of the 15th National Conference on Artificial Intelligence (AAAI 1998)*, Menlo Park: AAAI Press, pages 594–599.

[^teheux-2016]: Teheux, Bruno, 2016, “Modal definability based on Łukasiewicz validity relations”, *Studia Logica*, 104(2): 343–363. doi: 10.1007/s11225-015-9643-y

[^takeuti-1984]: Takeuti, Gaisi and Satako Titani, 1984, “Intuitionistic Fuzzy Logic and Intuitionistic Fuzzy Set Theory”, *Journal of Symbolic Logic*, 49(3): 851–866.

[^takeuti-1992]: –––, 1992, “Fuzzy Logic and Fuzzy Set Theory”, *Archive for Mathematical Logic*, 32(1): 1–32.

[^vetterlein-2015]: Vetterlein, Thomas, 2015, “Algebraic Semantics: The Structure of Residuated Chains”, in Cintula, Petr, Christian G. Fermüller, and Carles Noguera (eds.), *Handbook of Mathematical Fuzzy Logic*, Volume 3, (Mathematical Logic and Foundations, Volume 58), London: College Publications, pages 929–967.

[^vidal-2021]: Vidal, Amanda, 2021, “On transitive modal many-valued logics”, *Fuzzy Sets and Systems*, 407: 97–114. doi: 10.1016/j.fss.2020.01.011

[^vidal-2017]: Vidal, Amanda, Francesc Esteva, and Lluís Godo, 2017, “On modal extensions of Product fuzzy logic”, *Journal of Logic and Computation*, 27(1): 299–336. doi: 10.1093/logcom/exv046

[^zadeh-1965]: Zadeh, Lotfi A., 1965, “Fuzzy Sets”, *Information and Control*, 8(3): 338–353. doi:10.1016/S0019-9958(65)90241-X

[^zadeh-1975]: –––, 1975, “Fuzzy logic and approximate reasoning”, *Synthese*, 30: 407–428. doi: 10.1007/BF00485052
