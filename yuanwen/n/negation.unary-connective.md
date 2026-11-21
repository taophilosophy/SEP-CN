# negation — unary-connective（supplement）

> （《negation》词条补充材料，源：plato.stanford.edu/entries/negation/unary-connective.html）

#### Supplement to Negation

## Additional Conceptions of Negation as a Unary Connective

- 1. Negation as the Routley star
- 2. Negation as inconsistency
- 3. Negation as contradictoriness
- 4. Negation as falsity
- 5. Negation as cancellation
- 6. Negation by iteration
- 7. Perfect negation

### 1. Negation as the Routley star

The so-called “Routley star”, a semantical device introduced into non-classical logic by the Routleys (1972) (Valerie Plumwood, formerly Routley, and Richard Sylvan, né Routley), is a one-place function $(\cdot )^*$ from information states into information states and may be used to invalidate the unrestricted and the negated *ex contradictione* principles. The idea is that a negated formula $\neg A$ is true at a state $w$ in a model $\cal M$ iff $A$ is not true at $w^*$: ${\cal M},w \models \neg A$ iff ${\cal M}, w^* \not \models A$. If the premises of the *ex contradictione* principles, $A \vdash B$ and $A \vdash \neg B$, are valid, then for every state $w$ from $\cal M$'s set of states, ${\cal M},w \models A$ implies both ${\cal M},w \models B$ and ${\cal M},w^* \not \models B$. However, this obviously does not ensure in general that ${\cal M},w \models A$ implies ${\cal M},w^* \not \models C$ or ${\cal M},w \models C$ for an arbitrary formula $C$.

Its flexibility notwithstanding, the star semantics has been criticized for example by van Benthem (1979) and Copeland (1979) for lack of intuitive meaning and for not giving rise to an “applied” semantics. Smiley (1993, 17–18) remarks that the Routley star “is merely a device for preserving a recursive treatment of the connectives” and that it does not provide an explanation of negation until it is itself supplemented by an explanation. The relation between the Routley star semantics for negation and the interpretation of negation in (in)compatibility models has been investigated by Dunn (1993) and Restall (1999). Restall uses the compatibility semantics to make sense of the Routley star and assumes that the compatibility relation is symmetric, serial (alias “directed”), and satisfies the following “convergence” condition:

$$\forall x (\exists y(xCy) \Rightarrow \exists y \forall z(xCy \amp z \leq y))).$$

Since $C$ is serial, one may focus on what Mares (2004, 78) calls the Star Postulate: $$\forall x \exists y(xCy \amp \forall z (xCz \Rightarrow z \leq y )).$$ If the Star Postulate is satisfied, for every state $w$ there exists a non-empty set of maximal (with respect to $\leq$) states compatible with $w$. Therefore, to every state $w$ one may assign a unique state $w^*$ from that set and put ${\cal M},w \models \neg A$ iff ${\cal M}, w^* \not \models A$.

It is thus possible to define the Routley star $w^*$ of $w$ as one of the maximal states compatible with $w$. As Restall notes, symmetry of $C$ guarantees that for every state $w$, $w \leq w^{**}$. If in addition it is required that $w^{**} \leq w$, the Double Negation Law and the De Morgan laws hold. Restall (1999, 63) concludes that “we have a reading of the Routley star which makes a great deal of sense”.

In Odintsov and Wansing 2021 it is shown how the Routley star negation can be obtained from Dimiter Vakarelov’s theory of negation and that the propositional logic HYPE from Leitgeb 2019 coincides with the logic characterized by the class of all involutive Routley star information frames, thereby obtaining a considerably simplified semantics for HYPE, see also Punčochář and Sedlár 2022. A Routley star semantic for first-order HYPE is presented in Speranski 2021. The metaphysics of the Routley star operation is investigated in Zalta 2024.

### 2. Negation as inconsistency

The idea of negation as inconsistency is to understand *it is not the case that $A$* as *$A$ implies absurdity* or, more generally, as *$A$ implies something unwanted*. The latter gives Allen Hazen’s notion of subminimal negation (Hazen 1992), suggested by Lloyd Humberstone. This notion of negation as inconsistency is reasonable if implication is taken to be primitive and not itself defined in terms of negation and disjunction (or negation and conjunction). In Gabbay 1988, the notion of negation of inconsistency is introduced by requiring that the negation $*A$ of $A$ is derivable from a set of premises $\Delta$ iff there is an unwanted formula $U$ that is derivable from $\Delta \cup \{A\}$. The non-empty set of unwanted formulas has to be distinct from the set of all formulas and it must not contain any theorems.

If a single unwanted formula $U$ is assumed and $U$ is not supposed to be such that any formula can be derived from it, the idea of negation as inconsistency leads to minimal negation as fundamental. Both contraposition and constructive contraposition are derivable if the standard left and right sequent rules for constructive implication are assumed: $$\begin{array}{cc} \begin{array}{c} \begin{array}{c} \\ A \vdash B \end{array} \;\; \begin{array}{c} B \vdash B \quad U \vdash U \\ \hline B, (B\rightarrow U) \vdash U \end{array} \\ \hline \begin{array}{c} A, (B \rightarrow U) \vdash U\\ \hline (B \rightarrow U) \vdash (A \rightarrow U) \end{array} \end{array} & \begin{array}{c} \begin{array}{c} \\ A \vdash (B \rightarrow U) \end{array} \;\; \begin{array}{c} B \vdash B \quad U \vdash U \\ \hline B, (B \rightarrow U) \vdash U \end{array}\\ \hline \begin{array}{c} B, A \vdash U \\ \hline B \vdash (A \rightarrow U) \end{array} \end{array} \end{array}$$

If there exists more than one unwanted formula, contraposition still holds, but it is not guaranteed that the two branches in the derivation on the right of constructive contraposition involve the same unwanted formula $U$.

Intuitionistic negation is a paradigm case of a negation as inconsistency. The constant $\bot$ may be picked as the unwanted formula that is unwanted because any formula whatsoever can be derived from it. In Dunn 1993 it has been shown that the familiar Kripke semantics for intuitionistic logic and the semantics in terms of compatibility frames with a reflexive and symmetric compatibility relation coincide. In Wansing 2001 it is observed that a unary connective $*$ is a negation as inconsistency for a language that contains $*$ and $\wedge$ (the latter being governed by standard single-conclusion sequent rules) and a derivability relation $\vdash$ such that for no formula $A$, both $\varnothing \vdash A$ and $\varnothing \vdash *A$, whenever $*$ satisfies (i) what Humberstone (2011) calls selective contraposition: $$\Delta , A \vdash B \slashrel \Delta , *B \vdash *A$$ , (ii) the Law of Non-Contradiction $* (A \wedge *A)$, and (iii) double negation introduction.

### 3. Negation as contradictoriness

It is often held that syntactically a contradictory pair of formulas is a pair $\{A , \neg A\}$ consisting of a formula $A$ and its negation $\neg A$ (see the entry on contradiction). However, one may also reverse this perspective and try to characterize negation in terms of contradictoriness. This could be a non-trivial task because according to Grimm (2005, 55), on a most conservative account there are “some 240 senses of contradiction.” Moreover, there is the methodological view, emphasized by Humberstone (2019), that it is preferable not to ask what makes $\{A , \neg A\}$a contradictory pair, but to ask what in general makes two formulas $A$ and $B$ contradictories, thereby purifying conditions of contradictoriness of any explicit reference to a unary (negation) connective. Two formulas $A$ and $B$ (or the propositions expressed by them) are then subcontraries with respect to a multiple-conclusion consequence relation, $\Vdash$, if $\varnothing \Vdash \{A, B\}$, and they are contraries if $ \{A, B\} \Vdash \varnothing $. Accordingly, unary connectives *σ* and *κ* are subcontrary-forming, respectively contrary-forming with respect to $\Vdash$ if for any formula $A$, we have $\varnothing \Vdash \{A, \sigma (A) \}$, respectively $ \{A, \kappa(A)\} \Vdash \varnothing $, and a unary connective is contradictory-forming if it is both subcontrary-forming and contrary-forming.

Nevertheless, one may ask whether there are different conceptions of contradictoriness depending on how conditions of subcontrariety and contrariety are expressed in the object language by means of a negation connective $\neg$ and maybe additional vocabulary.

According to Priest (1999, 103; 2006, Chapter 4), theories of negation are, in the first place, theories about the relationship of contradiction, and according to Aristotle (*Cat.* 13b1–3), two statements are contradictories if, necessarily, one is true and the other is false. In Priest’s opinion, the Aristotelian conception leads to the view that the Law of the Excluded Middle (LEM) and the Law of Non-Contradiction are provable:

$$ \vdash (A \vee\neg A) \qquad \vdash \neg (A \wedge \neg A). $$

According to another conception of contradictoriness, $\{A , \neg A\}$ is a contradictory pair if, necessarily, if $A$ is true, then $\neg A$ is false and, moreover, $A$ and $\neg A$ cannot both be false. These conditions may be captured by the following inference principles:

$$ A \vdash \neg \neg A \qquad \vdash \neg (\neg A \wedge \neg \neg A). $$

The subsequent table (notation adjusted) is taken from Wansing 2006 and lists several pairs of conditions that may each be regarded as syntactic characterizations of notions of contradictoriness. In the table, **CPL** stands for classical propositional logic, **IPL** for intuitionistic propositional logic, and **MIN** for Johansson’s minimal logic. Whereas the properties [1] correspond to the Aristotelian conception of contradictoriness, the less familiar notion of contradictoriness captured by [2] is an understanding of contradictoriness according to which intuitionistic negation is contradictory-forming, although it fails to satisfy the LEM. Wansing (2006) also distinguishes different conceptions of contrariety in terms of derivability and non-derivability conditions. For a critical discussion of Priest’s views on negation see Humberstone 2019.

In Lenzen 1996 a certain non-derivability condition is suggested as a necessary property of any “real” negation $\neg$, namely that there exists a formula $A$ with $A \not \vdash \neg A$. This condition may be seen as a meta-level counterpart of a classically invalid principle characteristic of connexive logic, viz. Aristotle’s Thesis $\neg (A \rightarrow \neg A)$. A systematic study of negation in the context of multiple-conclusion consequence relations that takes into account non-derivability rules is Marcos 2005, where Lenzen’s condition is supplemented by also requiring that there exists a formula $A$ with $\neg A \not \vdash A$.

|   | $\mathit \{ A, \neg A\}$ *is contradictory iff* | **CPL** | **IPL** | **N3** | **N4** | **MIN** |
| --- | --- | --- | --- | --- | --- | --- |
| [1] | $\vdash \neg (A \wedge \neg A )$, $\vdash A \vee \neg A $ | ✓ | – | – | – | – |
|   | $\vdash \neg (A \wedge \neg A )$, $\vdash \neg A \vee \neg \neg A $ | ✓ | – | – | – | – |
|   | $\vdash \neg (A \wedge \neg A )$, $\neg \neg A \vdash A $ | ✓ | – | – | – | – |
|   | $A \vdash \neg \neg A$, $\vdash A \vee \neg A $ | ✓ | – | – | – | – |
|   | $A \vdash \neg \neg A$, $\vdash \neg A \vee \neg \neg A $ | ✓ | – | – | – | – |
| [2] | $A \vdash \neg \neg A$, $\vdash \neg (\neg A \wedge \neg \neg A)$ | ✓ | ✓ | – | – | – |
|   | $A \vdash \neg \neg A$, $\neg \neg A \vdash A$ | ✓ | – | ✓ | ✓ | – |
|   | $\vdash \neg (\neg A \wedge \neg \neg A)$, $\vdash A \vee \neg A$ | ✓ | – | – | – | – |
|   | $\vdash \neg (\neg A \wedge \neg \neg A )$, $\vdash \neg A \vee \neg \neg A $ | ✓ | – | – | – | – |
|   | $\vdash \neg (\neg A \wedge \neg \neg A )$, $\neg \neg A \vdash A$ | ✓ | – | – | – | – |
|   | $\neg \neg A \vdash A$, $\vdash A \vee \neg A$ | ✓ | – | – | – | – |
|   | $\neg \neg A \vdash A $, $\vdash \neg A \vee \neg \neg A $ | ✓ | – | – | – | – |
|   | $\neg \neg A \vdash A$, $\vdash \neg (\neg A \wedge \neg \neg A )$ | ✓ | – | – | – | – |

*Table 1*

### 4. Negation as falsity

Another idea often associated with the notion of negation as a connective is that the negation $\neg A$ of a formula $A$ expresses the falsity of $A$. If the principle of bivalence, saying that a proposition cannot be neither true nor false and, in addition, cannot both be true and false, is assumed and $\neg A$ expresses the falsity of $A$, then $\neg A$ is true iff $A$ is false.[^note-s1] If the principle of bivalence is given up and truth and falsity are kept apart as two independent notions, there still remain some basic principles negation as falsity satisfies under quite natural assumptions. In the possible worlds semantics of Nelson’s constructive logics with strong negation, the worlds are viewed as information states endowed with a reflexive and transitive relation $\leq$ understood as a relation of possible expansion of states, and two semantical relations between a state and a formula are discriminated, namely **support of truth**, $\models ^+$, and **support of falsity**, $\models ^-$. In this setting, both the support of truth and the support of falsity of atomic formulas $p$ are persistent with respect to $\leq$: if $w \leq u$, then ${\cal M},w \models^+ p$ implies ${\cal M},u \models^+ p$ and ${\cal M},w \models^- p$ implies ${\cal M},u \models^- p$.

In accordance with the notion of negation as falsity, an information state $w$ in a model $\cal M$ supports the truth of the strong negation $\osim A$ of $A$ iff $w$ supports the falsity of $A$: ${\cal M}, w\models ^+ \osim A$ iff ${\cal M}, w\models ^- A$. Furthermore, it is determined that a state supports the falsity of $\osim A$ iff it supports the truth of $A$: ${\cal M}, w\models ^- \osim A$ iff ${\cal M}, w\models ^+ A$. Strong negation thus serves as a toggle between support of truth and support of falsity. As a result, both double negation introduction and double negation elimination are valid in the sense that their truth is supported by every state of any model. Moreover, if the usual falsification conditions for conjunctions and disjunctions are assumed, every De Morgan law emerges as valid. Contrary to what is the case with negation as impossibility evaluated in compatibility models and negation as inconsistency, strong negation as falsity does not, however, inevitably validate contraposition.

Another interesting feature of strong negation is that provable equivalence is not a congruence relation, i.e., the replacement rule $$\mathord{\vdash A \leftrightarrow B} \slashrel \mathord{\vdash C[p/A] \leftrightarrow C[p/B]}$$ is not valid, where $C[p/A]$ is the result of uniformly substituting $A$ for some atomic formula $p$ in $C$. The replacement property, however, does hold for a stronger notion of equivalence: $$ \mathord{\vdash A \Leftrightarrow B} \slashrel \mathord{\vdash C[p/A] \Leftrightarrow C[p/B]},$$ where $A \Leftrightarrow B$ is defined as $(A \leftrightarrow B) \wedge (\osim A \leftrightarrow \osim B)$. The latter replacement property also reflects the treatment of truth and falsity as two primitive and equally important notions. A comprehensive algebraic study of Nelson’s constructive logics with strong negation can be found in Odintsov 2008; substructural subsystems of Nelson’s logics have been considered in Wansing 1993.[^note-s2] Logics of falsification are also studied in Kapsner 2014, Kürbis 2019.

### 5. Negation as cancellation

The co-implication connective is also sometimes referred to as “subtraction”, the idea being that $(A \coimp B)$ may be understood as expressing the result of subtracting the content of $B$ from the content of $A$. The co-negation $(\top \coimp A)$ then subtracts the content of $A$ from the truth. One may wonder whether such a subtraction amounts to the annihilation or cancellation of the content of $A$. Cancellation is an action type, and the idea of negation as cancellation is sometimes traced back to Strawson, who explains contradictions in agentive terms:

> Contradicting oneself is like writing something down and then erasing it, or putting a line through it. A contradiction cancels itself and leaves nothing. (1952, 3)

If the idea of cancellation in acts of contradictions is applied to obtain an understanding of sentential negation, the content of or proposition expressed by $\osim A$ is the result of erasing or cancelling the proposition expressed by $A$. The idea of negation as cancellation is described by Routley and Routley (1985, 205) as follows:[^note-s3]

> $\osim A$ deletes, neutralizes, erases, cancels $A$ (and similarly, since the relation is symmetrical, $A$ erases $\osim A$), so that $\osim A$ together with $A$ leaves nothing, no content. The conjunction of $A$ and $\osim A$ says nothing, so nothing more specific follows. In particular, $A \wedge \osim A$ does not entail $A$ and does not entail $\osim A$.

According to the Routleys, principles characteristic of connexive logic then emerge as plausible, such as the so-called **Aristotle’s theses**, $\osim (A \rightarrow \osim A)$ and $\osim (\osim A \rightarrow A)$, cf. the entry on connexive logic. If entailment is understood as content inclusion, it might seem that $A$ does not entail $\osim A$, and that $\osim A$ does not entail $A$ because the content of $A$ does not include the content of its own neutralizer, $\osim A$, and the content of $\osim A$ does not include the content of its own neutralizer, $A$. For the Routleys, negation as cancellation also renders the so-called **Boethius’ theses**, $(A \rightarrow B) \rightarrow \osim (A \rightarrow \osim B)$ and $(A \rightarrow \osim B) \rightarrow \osim (A \rightarrow B)$, plausible. If $A$ entails $B$, and thus the content of $B$ is contained in the content of $A$, then $A$ does not contain the content of the neutralizer of $B$, and similarly for the second thesis of Boethius.

Priest (1999) takes up the idea of negation as cancellation and develops from it a simple formal system that satisfies some principles of connexive logic. The first thesis of Boethius is not valid in classical logic, but it is true in a classical model if the antecedent $A$ is true in the model. Accordingly, Priest uses an evaluation clause for implication in possible worlds models ensuring that $(A \rightarrow B)$ is true only if $A$ is satisfiable (true at some possible world): ${\cal M}, w \models (A \rightarrow B)$ iff (i) there is a world $w'$ with ${\cal M}, w' \models A$, and (ii) for every world $u$, ${\cal M}, u \models A$ implies ${\cal M}, u \models B$. If, in addition, it is required that $B$ fails to be true at some world, contraposition is enforced (see Priest 1999 and the entry on connexive logic).

A critical discussion of negation as cancellation and especially its supposed relation to connexive logic can be found in Wansing and Skurt 2018.

### 6. Negation by iteration

The conception of negation by iteration addresses the question whether there could be a unary connective, §, such that §§$A$ is interderivable with $\neg A$ for the negation operation $\neg$ of some given logic conservatively extended by §. Such a connective § is a demi-negation or a square root of negation for $\neg$.

In Kamide 2017, for example, two variants, **IP** and **CP**, of Nelson’s paraconsistent logic **N4** and its classical variant using material instead of intuitionistic implication are defined. In **IP**, respectively **CP**, double negations behave as intuitionistic negation, respectively classical negation. The unary operations of these systems are demi-negations (if added to **N4**, respectively its classical variant), and one may wonder whether these demi-negations are negations at all. This question is discussed in Omori and Wansing 2018, where it is noted that Kamide’s negations not only satisfy the minimal conditions from Marcos 2005 for a unary connective to be regarded as a negation, but also that the truth condition for them is exactly the one for negation in **FDE**.

The systems **IP** and **CP** deviate from the more familiar counterparts they are variants of only as far as the falsity conditions for demi-negated formulas are concerned. In the context of extensions of **FDE**, this modification is part of a general strategy for obtaining contra-classical logics, logics that are neither extensions nor sublogics of classical logic, cf. Humberstone 2000b and Section 2.6.

Satoru Niki (2023) analyzes the non-trivial negation inconsistency of Kamide’s logics and studies subsystems of **IP** and **CP** with a focus on a system **MP**, in which the double negation behaves as the negation of Johansson’s minimal logic.

### 7. Perfect negation

It might be expected that a notion of “perfect negation” is rather restrictive and precludes many contenders from the status of a negation connective. The syntactical and the semantical concepts of perfect negation developed by Arnon Avron (1999, 2002) are, indeed, sophisticated notions that, taken together, basically designate only classical negation as perfect. Avron considers consequence relations between finite multisets of formulas and single-conclusion consequence relations between multisets of formulas and single formulas.[^note-s4] With respect to a multiple-conclusion consequence relation, a unary connective $\neg$ is called an internal negation iff it shifts formulas from antecedent to succedent position and *vice versa*:

$$ A, \Delta \vdash \Gamma \mbox{ iff } \Delta \vdash \Gamma , \neg A; \quad \quad \neg A , \Delta \vdash \Gamma \mbox{ iff } \Delta \vdash \Gamma , A.$$

If $\vdash $ is a single-conclusion consequence relation in a language containing $\neg$, the connective $\neg$ is said to be an **internal negation** for $\vdash$, and $\vdash$ is said to be **strongly symmetrical with respect to** $\neg$ iff there exists a multiple-conclusion consequence relation $\vdash '$ for the same language such that $\neg$ is an internal negation for $\vdash '$ and $\Delta \vdash A$ holds just in case $\Delta \vdash ' A$ (Avron 1999, Definition 3). If $\vdash$ is strongly symmetrical with respect to $\neg$, then $\neg$ satisfies double negation introduction, double negation elimination, and contraposition. A unary connective $*$ is a perfect negation with respect to a single-conclusion consequence relation $\vdash$ from the syntactic point of view if the relation $\vdash$ is strongly symmetrical with respect to $*$. This property is enjoyed by negation operations in quite a few logics, but not, for example, in intuitionistic logic.

In addition to a syntactic notion of perfectness, Avron also introduces a number of semantical notions of normality, including a notion of strong normality. Among the logics considered by Avron (1999, 2002) only Boolean negation in classical logic turns out to be perfect from both the syntactical and the semantical point of view.


## Notes（原文脚注，引自主文）

[^note-s1]: 1. It has often been noted that bivalence must be distinguished from the validity of the Law of Excluded Middle (see e.g. entry on contradiction). The LEM is valid, for instance, in Priest’s (1979) logic of paradox **LP**, although **LP** is a three-valued logic, see entries on many-valued logic and paraconsistent logic. Moreover, it can be shown that every Tarskian consequence relation has a bivalent, although not necessarily compositional semantics, cf. Malinowski 1993, Shramko and Wansing 2011, Chapter 9.

[^note-s2]: 2. The basic systems of Nelson’s constructive logics with strong negation, **N4** and **N4**$^{\bot}$, have a four-valued possible worlds semantics. The underlying four-valued first-degree entailment logic is closely related to early Buddhist logic, cf. Dunn 2000, Priest 2010, and the entry on contradiction.

[^note-s3]: 3. Routley and Routley (1985) also discuss Wittgenstein’s remarks about contradictions and negation, and note that Wittgenstein “runs together, in a way that is ultimately incoherent, exclusion and cancellation models of negation.”

[^note-s4]: 4. Avron does not, however, assume that these relations are monotonic, i.e., that $\Delta \vdash \Gamma$ implies $\Delta \cup \Delta ' \vdash \Gamma \cup \Gamma '$, with the restriction that $\Gamma \cup \Gamma '$ contains at most one formula in the case of single-conclusion consequence relations.