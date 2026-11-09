# logic-justification — supplement（supplement）

> （《logic-justification》词条补充材料，源：plato.stanford.edu/entries/logic-justification/supplement.html）

#### Supplement to Justification Logic

## Some More Technical Matters

- 1. Mathematical Logic Tradition
- 2. Logical Awareness and Constant Specifications
- 3. Single-Agent Possible World Models for $\mathsf{J}$
- 4. Realization Theorems
- 5. Multi-Agent Justification Models
- 6. Self-referentiality of Justifications

### 1. Mathematical Logic Tradition

Several well-known mathematical notions which appeared prior to Justification Logic have sometimes been perceived as related to the BHK idea: Kleene realizability (Troelstra 1998), Curry-Howard isomorphism (Girard, Taylor, and Lafont 1989, Troelstra and Schwichtenberg 1996), Kreisel-Goodman theory of constructions (Goodman 1970, Kreisel 1962, Kreisel 1965), just to name a few. These interpretations have been very instrumental for understanding intuitionistic logic, though none of them qualifies as the *BHK* semantics.

Kleene realizability revealed a fundamental *computational content* of formal intuitionistic derivations, however it is still quite different from the intended *BHK* semantics. Kleene realizers are computational programs rather then proofs. The predicate ‘*r realizes F* ’ is not decidable, which leads to some serious deviations from intuitionistic logic. Kleene realizability is not adequate for the intuitionistic propositional calculus $\mathsf{IPC}$. There are realizable propositional formulas not derivable in $\mathsf{IPC}$ (Rose 1953).[^note-supp-note-8]

The Curry-Howard isomorphism transliterates natural derivations in $\mathsf{IPC}$ to typed $\lambda$-terms thus providing a generic functional reading for logical derivations. However the foundational value of this interpretation is limited since, as proof objects, Curry-Howard $\lambda$-terms denote nothing but derivations in $\mathsf{IPC}$ itself and thus yield a circular provability semantics for the latter.

An attempt to formalize the *BHK* semantics directly was made by Kreisel in his theory of constructions (Kreisel 1962, Kreisel 1965). The original variant of the theory was inconsistent; difficulties already occurred at the propositional level. In (Goodman 1970) this was fixed by introducing a stratification of constructions into levels, which ruined the *BHK* character of this semantics. In particular, a proof of $A \rightarrow B$ was no longer a construction that could be applied to any proof of $A$

### 2. Logical Awareness and Constant Specifications

Two examples in $\mathsf{J}$ are presented, showing modal theorems of $\mathsf{K}$, and realizations for them. In the examples indices on constants have been omitted.

**Example 1.** This shows how to build a justification of a conjunction from justifications of the conjuncts. In traditional modal language, this principle is formalized as $\Box A \wedge \Box B \rightarrow \Box ( A \wedge B)$. In $\mathsf{J}$ this idea is expressed in the more precise justification language.

1. $A \rightarrow ( B \rightarrow ( A \wedge B))$ (propositional axiom)
2. $c :( A \rightarrow ( B \rightarrow ( A \wedge B))$) (from 1 by Axiom Internalization)
3. $x : A \rightarrow [ c \cdot x ]:( B \rightarrow ( A \wedge B))$ (from 2 by Application and Modus Ponens)
4. $x : A \rightarrow ( y : B \rightarrow [[ c \cdot x ] \cdot y ]:( A \wedge B))$ (from 3 by Application and propositional reasoning)
5. $x : A \wedge y : B \rightarrow [[ c \cdot x ] \cdot y ]:( A \wedge B)$ (from 5 by propositional reasoning)

The derived formula 5 contains the constant $c$, which was introduced in line 2, and the complete reading of the result of this derivation is:

> $x : A \wedge y : B \rightarrow [[ c \cdot x ] \cdot y ]:( A \wedge B)$, given $c :( A \rightarrow ( B \rightarrow ( A \wedge B))$).

**Example 2.** This example shows how to build a justification of a disjunction from justifications of either of the disjuncts. In the usual modal language this is represented by $\Box A \vee \Box B \rightarrow \Box ( A \vee B)$. Here is the corresponding result in $\mathsf{J}$.

1. $A \rightarrow ( A \vee B)$ (classical logic)
2. $a :( A \rightarrow ( A \vee B))$ (from 1 by Axiom Internalization)
3. $x : A \rightarrow [ a \cdot x ]:( A \vee B)$ (from 2 by Application and Modus Ponens)
4. $B \rightarrow ( A \vee B)$ (by classical logic)
5. $b :( B \rightarrow ( A \vee B))$ (from 4 by Axiom Internalization)
6. $y : B \rightarrow [ b \cdot y ]:( A \vee B)$ (from 5 by Application and Modus Ponens)
7. [$a \cdot x ]:( A \vee B ) \rightarrow [ a \cdot x$ + $b \cdot y ]:( A \vee B)$ (by Sum)
8. [$b \cdot y ]:( A \vee B ) \rightarrow [ a \cdot x$ + $b \cdot y ]:( A \vee B)$ (by Sum)
9. $(x : A \vee y : B ) \rightarrow [ a \cdot x$ + $b \cdot y ]:( A \vee B)$ (from 3, 6, 7, and 8 by propositional reasoning)

The complete reading of the result of this derivation is:

> $(x : A \vee y : B ) \rightarrow [ a \cdot x + b \cdot y ]:( A \vee B)$, given $a :( A \rightarrow ( A \vee B))$ and $b :( B \rightarrow ( A \vee B))$.

### 3. Single-Agent Possible World Models for $\mathsf{J}$

Here are two models in each of which $x : P \rightarrow x :( P \wedge Q)$ is not valid. $(P$ and $Q$ are atomic and $x$ is a justification variable.) It was pointed out that a formula $t : X$ might fail at a possible world either because $X$ is not believable there (it is false at some accessible world), or because $t$ is not an appropriate reason for $X$. The two models illustrate both versions.

First, consider the model $\mathcal{M}$ having a single state, $\Gamma$, accessible to itself, and with an evidence function such that $\mathcal{E} ( x , Z)$ is $\Gamma$, for every formula $Z$. In this model, $x$ serves as‘universal’ evidence. Use a valuation such that $\mathcal{V} ( P)$ = $\Gamma$ and $\mathcal{V} ( Q)$ = $\varnothing$. Then one has $\mathcal{M} , \Gamma$ ⊩ $x : P$ but not-$\mathcal{M} , \Gamma$ ⊩ $x :( P \wedge Q)$ because, even though $x$ serves as universal evidence, $P \wedge Q$ is not believable at $\Gamma$ in the Hintikka/Kripke sense because $Q$ is not true.

Next consider the model $\mathcal{N}$, again having a single state $\Gamma$ accessible to itself. This time take $\mathcal{V}$ to be the mapping assigning $\Gamma$ to every propositional letter. But also, set $\mathcal{E} ( x , P)$ = $\Gamma , \mathcal{E} ( x , Z)$ = $\varnothing$ for $Z \ne P$, and otherwise $\mathcal{E}$ doesn’t matter for this example. Then of course both $P$ and $P \wedge Q$ are believable at $\Gamma$, but $\mathcal{N} , \Gamma$ ⊩ $x : P$ and not-$\mathcal{N} , \Gamma$ ⊩ $x :( P \wedge Q)$, the latter because $x$ does not serve as evidence for $P \wedge Q$ at $\Gamma$.

In Hintikka/Kripke models, believability and knowability are essentially semantic notions, but the present treatment of evidence is more of a syntactic nature. For example, the model $\mathcal{N}$ above also invalidates $x : P \rightarrow x :( P \wedge P)$. At first glance this is surprising, since in any standard logic of knowledge or belief $\Box P \rightarrow \Box ( P \wedge P)$ is valid. But, just because $x$ serves as evidence for $P$, it need not follow that it also serves as evidence for $P \wedge P$. The formulas are syntactically different, and effort is needed to recognize that the later formula is a redundant version of the former. To take this to an extreme, consider the formula $x : P \rightarrow x :( P \wedge P \wedge$ … $\wedge P )$, where the consequent has as many conjuncts as there are elementary particles in the universe! In brief, Hintikka/Kripke style knowledge is knowledge of *propositions*, but justification terms justify *sentences*.

### 4. Realization Theorems

Here is an example of an $\mathsf{S4}$-derivation realized as an $\mathsf{LP}$-derivation in the style of the Realization theorem. There are two columns in the table below. The first is a Hilbert-style $\mathsf{S4}$-derivation of a modal formula $\Box A \vee \Box B \rightarrow \Box ( \Box A \vee B)$. The second column displays corresponding steps of an $\mathsf{LP}$-derivation of a formula:

> $x : A \vee y : B \rightarrow ( a \cdot ! x$ + $b \cdot y ):( x : A \vee B)$

with constant specification

> $\{a :( x : A \rightarrow x : A \vee B ), b :( B \rightarrow x : A \vee B ) \}$.

*Comparing derivations in $\mathsf{S4}$ and $\mathsf{LP}$*

|   | Derivation in $\mathsf{S4}$ | Derivation in $\mathsf{LP}$ |
| --- | --- | --- |
| 1. | $\Box A \rightarrow \Box A \vee B$ | $x : A \rightarrow x : A \vee B$ |
| 2. | $\Box ( \Box A \rightarrow \Box A \vee B)$ | $a :( x : A \rightarrow x : A \vee B)$ |
| 3. | $\Box \Box A \rightarrow \Box ( \Box A \vee B)$ | !$x : x : A \rightarrow ( a \cdot ! x ):( x : A \vee B)$ |
| 4. | $\Box A \rightarrow \Box \Box A$ | $x : A \rightarrow ! x : x : A$ |
| 5. | $\Box A \rightarrow \Box ( \Box A \vee B)$ | $x : A \rightarrow ( a \cdot ! x ):( x : A \vee B)$ |
| 5$'$. |   | $(a \cdot ! x ):( x : A \vee B ) \rightarrow ( a \cdot ! x$ + $b \cdot y ):( x : A \vee B)$ |
| 5$''$. |   | $x : A \rightarrow ( a \cdot ! x$ + $b \cdot y ):( x : A \vee B)$ |
| 6. | $B \rightarrow \Box A \vee B$ | $B \rightarrow x : A \vee B$ |
| 7. | $\Box ( B \rightarrow \Box A \vee B)$ | $b :( B \rightarrow x : A \vee B)$ |
| 8. | $\Box B \rightarrow \Box ( \Box A \vee B)$ | $y : B \rightarrow ( b \cdot y ):( x : A \vee B)$ |
| 8$'$. |   | $(b \cdot y ):( x : A \vee B ) \rightarrow ( a \cdot ! x$ + $b \cdot y ):( x : A \vee B)$ |
| 8$''$. |   | $y : B \rightarrow ( a \cdot ! x$ + $b \cdot y ):( x : A \vee B)$ |
| 9. | $\Box A \vee \Box B \rightarrow \Box ( \Box A \vee B)$ | $x : A \vee y : B \rightarrow ( a \cdot ! x$ + $b \cdot y ):( x : A \vee B)$ |

Extra steps $5' , 5'' , 8'$, and $8''$ are needed in the $\mathsf{LP}$ case to reconcile different internalized proofs of the same formula: $(a \cdot ! x ):( x : A \vee B)$ and $(b \cdot y ):( x : A \vee B)$. The resulting realization respects Skolem’s idea that negative occurrences of existential quantifiers (here over proofs hidden in the modality of provability) are realized by free variables whereas positive occurrences are realized by functions of those variables.

Proof theory plays an important role in the study of Justification Logics. Axiom systems we represented in this article, and a sequent calculus was introduced in (Artemov 1995, Artemov 2001). It has the curious disadvantage that it is cut free, but does not have the subformula property—no version with the subformula property is known. More recently, other kinds of proof procedures for Justification Logics have been created. Kurokawa uses hypersequents to provide a comprehensive proof-theoretical treatment of major systems of Justification Logic, (Kurokawa 2009), including those which combine implicit and explicit knowledge. These systems are notoriously hard to analyze and Kurokawa’s results constitute a remarkable fundamental contribution to this area.

Realizations have been investigated for their own sake, (Fitting 2009). The basic results all are algorithmic in nature. For example, in Modal Logic a Replacement Theorem holds just as it does classically: if $X \equiv X'$ is provable in a normal modal logic then so is $F \equiv F '$ where $F$ is a formula and $F'$ is like $F$ except that some subformula occurrence $X$ has been replaced with $X'$. Indeed this can be strengthened to establish that if $X \rightarrow X'$ is provable, and $X$ has a *positive* designated subformula occurrence in $F$, while $F'$ replaces that occurrence with $X'$, then $F \rightarrow F '$ is provable. This does not carry over in a simple way to Justification Logic. Roughly speaking, an occurrence of $X$ in a formula $F$ of Justification Logic may be within the scope of various justification terms, and in $F'$ these will need to be ‘adjusted’ to take into account a justification for $X \rightarrow X'$. It turns out this is not simple, but an algorithm for doing so has been developed, (Fitting 2006, Fitting 2009).

Here is another result having a similar proof. In a modal sequent calculus argument a typical step is the following.

$$\notag \frac{S_{1} \rightarrow S_{2} , X \quad\quad S_{1} \rightarrow S_{2} , Y}{S_{1} \rightarrow S_{2} , X \wedge Y} $$

The notion of a realization easily extends from formulas to sequents. Suppose both of the premise sequents above have realizations, and one would like a realization for the consequent sequent. The problem is, the two premise realizations may be quite different. Algorithmic machinery for merging them has been developed that does exactly this. This algorithm, in turn, serves as part of a new algorithm for the Realization Theorem itself.

Finally, all initial realization proofs were constructive and were based on some kind of cut-free proof system. But non-constructive, semantic arguments have been developed, which allow the extension of realization machinery substantially. For instance, it is now known that the family of modal logics having justification counterparts is infinite. Artemov and Fitting 2019 contains a detailed investigation along these lines.

### 5. Multi-Agent Justification Models

To simplify the language, one can use the forgetful projection which replaces explicit knowledge assertions $t : X$ by $\mathbf{J}X$ where $\mathbf{J}$ stands for so-called *justified common knowledge* modality. Modality $\mathbf{J}$ is a stronger version of common knowledge: $\mathbf{J}X$ states all agents share sufficient evidence for $X$. In a formal setting, in Kripke models, $\mathbf{J}X \rightarrow \mathbf{C}X$, but not necessarily $\mathbf{C}X \rightarrow \mathbf{J}X$ (Artemov 2006).

Informally, the traditional common knowledge modality (Fagin, Halpern, Moses, and Vardi 1995) is represented by the condition

> $\mathbf{C}X \Leftrightarrow X \wedge EX \wedge E^{2}X \wedge$ … $\wedge E^{n}X \wedge$ …

whereas for the justified common knowledge operator $\mathbf{J}$ one has

> $\mathbf{J}X \Rightarrow X \wedge EX \wedge E^{2}X \wedge$ … $\wedge E^{n}X \wedge$ …

Justified common knowledge has the same modal principles as McCarthy’s common knowledge (McCarthy, Sato, Hayashi, and Igarishi 1978). In (Cubitt and Sugden 2003) a case is made that David Lewis’ version of common knowledge (more properly, belief) is not identified with unlimited iteration of knowledge operators, but is much closer to justified common knowledge. (See the encyclopedia article on Common Knowledge). A good example of such a Lewis-McCarthy-Artemov justified common knowledge assertion, $\mathbf{J}X$, which is stronger than the usual common knowledge, $\mathbf{C}X$, is provided by situations following a public announcement of $X$ (Plaza 2007) after which $X$ holds at all states, not only at reachable states. Note that public announcements are the usual means for attaining common knowledge, and they lead to justified common knowledge $\mathbf{J}$ rather than the usual common knowledge $\mathbf{C}$.

The axiomatic description of justified common knowledge $\mathbf{J}$ is significantly simpler than that of $\mathbf{C}$ . According to (Antonakos 2007), in the standard epistemic scenarios, justified common knowledge $\mathbf{J}$ is conservative with respect to the usual common knowledge $\mathbf{C}$ and hence provides a lighter alternative to the latter.

### 6. Self-referentiality of Justifications

Let us consider an example which was suggested by the well-known *Moore’s paradox*:

> *It will rain but I don’t believe that it will.*

If $R$ stands for *it will rain*, then a modal formalization is:

> $M = R \wedge \neg \Box R$.

The Moore sentence $M$ is easily satisfiable, hence consistent, e.g., whenever the weather forecast wrongly shows “no rain”. However, it is impossible to know Moore’s sentence because

> $\neg \Box M = \neg \Box ( R \wedge \neg \Box R)$

holds in any modal logic containing $\mathsf{T}$ . Here is a derivation.

1. $(R \wedge \neg \Box R ) \rightarrow R$ (logical axiom)
2. $\Box (( R \wedge \neg \Box R ) \rightarrow R)$ (Necessitation)
3. $\Box ( R \wedge \neg \Box R ) \rightarrow \Box R$, (from 2 by Distribution)
4. $\Box ( R \wedge \neg \Box R ) \rightarrow ( R \wedge \neg \Box R)$ (Factivity in $\mathsf{T})$
5. $\Box ( R \wedge \neg \Box R ) \rightarrow \neg \Box R$ (from 4 in Boolean logic)
6. $\neg \Box ( R \wedge \neg \Box R)$ (from 3 and 5 in Boolean logic)

Furthermore, here is how this derivation is realized in $\mathsf{LP}$.

1. $(R \wedge \neg [ c \cdot x ]: R ) \rightarrow R$ (logical axiom)
2. $c :(( R \wedge \neg [ c \cdot x ]: R ) \rightarrow R)$ (Constant Specification)
3. $x :( R \wedge \neg [ c \cdot x ]: R ) \rightarrow [ c \cdot x ]: R$ (from 2 by Application)
4. $x :( R \wedge \neg [ c \cdot x ]: R ) \rightarrow ( R \wedge \neg [ c \cdot x ]: R)$ (Factivity)
5. $x :( R \wedge \neg [ c \cdot x ]: R ) \rightarrow \neg [ c \cdot x ]: R$ (from 4 by Boolean logic)
6. $\neg x :( R \wedge \neg [ c \cdot x ]: R)$ (from 3 and 5 in Boolean logic)

Note that Constant Specification in line 2 is self-referential.
