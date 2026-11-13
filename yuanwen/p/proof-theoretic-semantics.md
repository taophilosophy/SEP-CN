# Proof-Theoretic Semantics
**First published Wed Dec 5, 2012; substantive revision Fri Aug 18, 2023**

*Schroeder-Heister, Peter*

Proof-theoretic semantics is an alternative to truth-condition semantics. It is based on the fundamental assumption that the central notion in terms of which meanings are assigned to certain expressions of our language, in particular to logical constants, is that of *proof* rather than *truth*. In this sense proof-theoretic semantics is *semantics in terms of proof*. Proof-theoretic semantics also means the *semantics of proofs*, i.e., the semantics of entities which describe how we arrive at certain assertions given certain assumptions. Both aspects of proof-theoretic semantics can be intertwined, i.e. the semantics of proofs is itself often given in terms of proofs.

Proof-theoretic semantics has several roots, the most specific one being Gentzen’s remarks that the introduction rules in his calculus of natural deduction define the meanings of logical constants, while the elimination rules can be obtained as a consequence of this definition (see section 2.2.1). More broadly, it belongs to what Prawitz called *general proof theory* (see section 1.1). Even more broadly, it is part of the tradition according to which the meaning of a term should be explained by reference to the way it is *used* in our language.

Within philosophy, proof-theoretic semantics has mostly figured under the heading “theory of meaning”. This terminology follows Dummett, who claimed that the theory of meaning is the basis of theoretical philosophy, a view which he attributed to Frege. The term “proof-theoretic semantics” was proposed by Schroeder-Heister (1991; used already in the 1980s in lectures in Stockholm) in order not to leave the term “semantics” to denotationalism alone—after all, “semantics” is the standard term for investigations dealing with the meaning of linguistic expressions. Furthermore, unlike “theory of meaning”, the term “proof-theoretic semantics” covers philosophical and technical aspects likewise. In 1999, the first conference with this title took place in Tübingen, the second and third in 2013 and 2019, respectively. Many others have followed at various places. The first textbook with this title appeared in 2015 (Francez 2015)[^francez-2015][^francez-2015-2].

## 1. Background

### 1.1 General proof theory: consequence vs. proofs

The term “general proof theory” was coined by Prawitz. In general proof theory, “proofs are studied in their own right in the hope of understanding their nature”, in contradistinction to Hilbert-style “reductive proof theory”, which is the “attempt to analyze the proofs of mathematical theories with the intention of reducing them to some more elementary part of mathematics such as finitistic or constructive mathematics” (Prawitz, 1972, p. 123)[^prawitz-1972]. In a similar way, Kreisel (1971) asks for a re-orientation of proof theory. He wants to explain “recent work in proof theory from a neglected point of view. Proofs and their representations by formal derivations are treated as principal objects of study, not as mere tools for analyzing the consequence relation.” (Kreisel, 1971, p. 109)[^kreisel-1971] Whereas Kreisel focuses on the dichotomy between a theory of proofs and a theory of provability, Prawitz concentrates on the different goals proof theory may pursue. However, both stress the necessity of studying proofs as fundamental entities by means of which we acquire demonstrative (especially mathematical) knowledge. This means in particular that proofs are epistemic entities which should not be conflated with formal proofs or derivations. They are rather what derivations denote when they are considered to be representations of arguments. (However, in the following we often use “proof” synonymously with “derivation”, leaving it to the reader to determine whether formal proofs or proofs as epistemic entities are meant.) In discussing Prawitz’s (1971) survey, Kreisel (1971, p. 111) explicitly speaks of a “mapping” between derivations and mental acts, and considers it a task of proof theory to elucidate this mapping, including the investigation of the identity of proofs, a topic that Prawitz and Martin-Löf had put on the proof-theoretic agenda.

This means that in general proof theory we are not solely interested in whether B follows from A, but in the way by means of which we arrive at B starting from A. In this sense general proof theory is intensional and epistemological in character, whereas model theory, which is interested in the consequence relation and not in the way of establishing it, is extensional and metaphysical.

### 1.2 Inferentialism, intuitionism, anti-realism

Proof-theoretic semantics is inherently inferential, as it is inferential activity which manifests itself in proofs. It thus belongs to *inferentialism* (a term coined by Brandom, see his 1994; 2000)[^brandom-1994] according to which inferences and the rules of inference establish the meaning of expressions, in contradistinction to *denotationalism*, according to which denotations are the primary sort of meaning. Inferentialism and the ‘meaning-as-use’ view of semantics is the broad philosophical framework of proof-theoretic semantics. This general philosophical and semantical perspective merged with constructive views which originated in the philosophy of mathematics, especially in mathematical intuitionism. Most forms of proof-theoretic semantics are intuitionistic in spirit, which means in particular that principles of classical logic such as the law of excluded middle or the double negation law are rejected or at least considered problematic. This is partly due to the fact that the main tool of proof-theoretic semantics, the calculus of natural deduction, is biased towards intuitionistic logic, in the sense that the straightforward formulation of its elimination rules is the intuitionistic one. There classical logic is only available by means of some rule of indirect proof, which, at least to some extent, destroys the symmetry of the reasoning principles (see section 3.5). If one adopts the standpoint of natural deduction, then intuitionistic logic is a natural logical system. Also the BHK (Brouwer-Heyting-Kolmogorov) interpretation of the logical signs plays a significant role. This interpretation is not a unique approach to semantics, but comprises various ideas which are often more informally than formally described. Of particular importance is its functional view of implication, according to which a proof of $A \rightarrow B$ is a constructive function which, when applied to a proof of A yields a proof of B. This functional perspective underlies many conceptions of proof-theoretic semantics, in particular those of Lorenzen, Prawitz and Martin Löf (see sections 2.1.1, 2.2.2, 2.2.3).

According to Dummett (1975), the logical position of intuitionism corresponds to the philosophical position of anti-realism. The realist view of a recognition-independent reality is the metaphysical counterpart of the view that all sentences are either true or false independent of our means of recognizing it. Major parts of proof-theoretic semantics follow Dummett and his association with anti-realism.

### 1.3 Gentzen-style proof theory: Reduction, normalization, cut elimination

Gentzen’s calculus of natural deduction and its rendering by Prawitz is the background to most approaches to proof-theoretic semantics. Natural deduction is based on at least three central ideas:

- *Discharge of assumptions*: Assumptions can be “discharged” or “eliminated” in the course of a derivation, so the central notion of natural deduction is that of a derivation *depending on assumptions*.
- *Separation*: Each primitive rule schema contains only a single logical constant.
- *Introductions and eliminations*: The rules for logical constants come in pairs. The introduction rule(s) allow(s) one to infer a formula with the constant in question as its main operator, the elimination rule(s) permit(s) to draw consequences from such a formula.

In Gentzen’s natural deduction system for first-order logic derivations are written in tree form and based on the well-known rules. For example, implication has the following introduction and elimination rules

$$ \begin{prooftree} \AxiomC{$[A]$} \noLine \UnaryInfC{$B$} \RightLabel{$\,\to$I} \UnaryInfC{$A\to B$} \end{prooftree} \hspace{6em} \begin{prooftree} \AxiomC{$A\to B$} \AxiomC{$A$} \RightLabel{$\,\to$E} \BinaryInfC{$B$} \end{prooftree} $$

where the brackets indicate the possibility to discharge occurrences of the assumption A. The *open assumptions* of a derivation are those assumptions on which the end-formula depends. A derivation is called *closed*, if it has no open assumption, otherwise it is called *open*. If we deal with quantifiers, we have to consider open individual variables (sometimes called “parameters”), too. Metalogical features crucial for proof-theoretic semantics and for the first time systematically investigated and published by Prawitz (1965) include:

*Reduction*: For every detour consisting of an introduction immediately followed by an elimination there is a reduction step removing this detour.

*Normalization*: By successive applications of reductions, derivations can be transformed into normal forms which contain no detours.

For implication the standard reduction step removing detours is the following:

$$ \begin{prooftree} \AxiomC{$[A]$} \noLine\UnaryInfC{$\vdots$} \noLine\UnaryInfC{$B$} \UnaryInfC{$A\to B$} \AxiomC{$|$} \noLine\UnaryInfC{$A$} \BinaryInfC{$B$} \end{prooftree} \hspace{1em} \text{reduces to} \hspace{1em} \begin{prooftree} \AxiomC{$|$} \noLine\UnaryInfC{$A$} \noLine\UnaryInfC{$\vdots$} \noLine\UnaryInfC{$B$} \end{prooftree} $$

A simple, but very important corollary of normalization is the following: *Every closed derivation in intuitionistic logic can be reduced to a derivation using an introduction rule in the last step.* We also say that intuitionistic natural deduction satisfies the “*introduction form property*”. In proof-theoretic semantics this result figures prominently under the heading “fundamental assumption” (Dummett, 1991, p. 254)[^dummett-1991]. The “fundamental assumption” is a typical example of a philosophical re-interpretation of a technical proof-theoretic result.

*Further Reading:*

For the general orientation of *proof-theoretic semantics*, see the special issue of *Synthese* edited by Kahle and Schroeder-Heister (2006), the reader edited by Piecha and Schroeder-Heister (2016b), the textbook by Francez (2015), and the surveys by Wansing (2000) and by Schroeder-Heister (2016).

For the philosophical position and development of *proof theory*, see the entry on Hilbert’s program, the entry on the development of proof theory as well as Prawitz (1971).

For *intuitionism*, see the entry on intuitionistic logic, the entry on intuitionism in the philosophy of mathematics and the entry on the development of intuitionistic logic.

For *anti-realism*, see the entry on challenges to metaphysical realism as well as Tennant (1987; 1997) and Tranchini (2010; 2012a).

For *Gentzen-style proof-theory and the theory of natural deduction*, see the entry on natural deduction systems in logic as well as, in addition to Gentzen’s (1934/35) original presentation, Jaśkowski’s (1934) theory of suppositions, Prawitz’s (1965) classical monograph, Tennant (1978; 2017), Troelstra and Schwichtenberg (2000), Negri and von Plato (2001), Mancosu, Galvan and Zach (2021), and Andrzej Indrzejczak’s entry on [natural deduction in the *Internet Encyclopedia of Philosophy*. ](https://iep.utm.edu/nat-ded/)

## 2. Some versions of proof-theoretic semantics

### 2.1 The semantics of implication: Admissibility, derivability, rules

The semantics of implication lies at the heart of proof-theoretic semantics. In contradistinction to classical truth-condition semantics, implication is a logical constant in its own right. It has also the characteristic feature that it is tied to the concept of consequence. It can be viewed as expressing consequence at the sentential level due to modus ponens and to what in Hilbert-style systems is called the deduction theorem, i.e. the equivalence of $\Gamma ,A \vdash B$ and $\Gamma \vdash A \rightarrow B$.

A very natural understanding of an implication $A \rightarrow B$ is reading it as expressing the inference rule which allows one to pass over from A to B. Licensing the step from A to B on the basis of $A \rightarrow B$ is exactly, what modus ponens says. And the deduction theorem can be viewed as the means of establishing a rule: Having shown that B can be deduced from A justifies the rule that from A we may pass over to B. A rule-based semantics of implication along such lines underlies several conceptions of proof-theoretic semantics, notably those by Lorenzen, von Kutschera and Schroeder-Heister.

#### 2.1.1 Operative logic

Lorenzen, in his *Introduction to Operative Logics and Mathematics* (1955) starts with logic-free (atomic) calculi, which correspond to production systems or grammars. He calls a rule *admissible* in such a system if it can be added to it without enlarging the set of its derivable atoms. The implication arrow $\rightarrow$ is interpreted as expressing admissibility. An implication $A \rightarrow B$ is considered to be valid, if, when read as a rule, it is admissible (with respect to the underlying calculus). For iterated implications $(=$ rules) Lorenzen develops a theory of admissibility statements of higher levels. Certain statements such as

$$A \rightarrow A \quad\text{ or }\quad ((A \rightarrow B), (B \rightarrow C)) \rightarrow(A \rightarrow C) $$

hold independently of the underlying calculus. They are called *universally admissible* [“allgemeinzulässig”]), and constitute a system of positive implicational logic. In a related way, laws for universal quantification $\forall$ are justified using admissibility statements for rules with schematic variables.

For the justification of the laws for the logical constants $\land , \lor , \exists$ and $\bot$, Lorenzen uses an *inversion principle* (a term he coined). In a very simplified form, without taking variables in rules into account, the inversion principle says that everything that can be obtained from every defining condition of A can be obtained from A itself. For example, in the case of *disjunction*, let A and B each be a defining condition of $A\lor B$ as expressed by the primitive rules $A \rightarrow A\lor B$ and $B \rightarrow A\lor B$. Then the inversion principle says that $A\lor B \rightarrow C$ is admissible assuming $A \rightarrow C$ and $B \rightarrow C$, which justifies the elimination rule for disjunction. The remaining connectives are dealt with in a similar way. In the case of $\bot$, the absurdity rule $\bot \rightarrow A$ is obtained from the fact that there is no defining condition for $\bot$.

#### 2.1.2 Gentzen semantics

In what he calls “Gentzen semantics”, von Kutschera (1968) gives, as Lorenzen, a semantics of logically complex implication-like statements $A_1,\ldots,A_n \rightarrow B$ with respect to calculi K which govern the reasoning with atomic sentences. The fundamental difference to Lorenzen is the fact that $A_1,\ldots,A_n \rightarrow B$ now expresses a *derivability* rather than an *admissibility* statement.

In order to turn this into a semantics of the logical constants of propositional logic, von Kutschera argues as follows: When giving up bivalence, we can no longer use classical truth-value assignments to atomic formulas. Instead we can use calculi which prove or refute atomic sentences. Moreover, since calculi not only generate proofs or refutations but arbitrary derivability relations, the idea is to start directly with derivability in an atomic system and extend it with rules that characterize the logical connectives. For that von Kutschera gives a sequent calculus with rules for the introduction of n-ary propositional connectives in the succedent and antecedent, yielding a sequent system for generalized propositional connectives. Von Kutschera then goes on to show that the generalized connectives so defined can all be expressed by the standard connectives of intuitionistic logic (conjunction, disjunction, implication, absurdity).

*Further Reading:*

For extensions of expressive completeness in the style of von Kutschera: Wansing (1993a).

#### 2.1.3 Natural deduction with higher-level rules

When developing a general schema for inference rules for arbitrary logical constants, Schroeder-Heister (1984) proposed, as a semantical requirement, that a logically complex formula expresses the content or *common content* of *systems of rules*. A rule R is either a formula A or has the form $R_1,\ldots,R_n \Rightarrow A$, where $R_1,\ldots,R_n$ are rules. These so-called “higher-level rules” generalize the idea that rules may discharge assumption formulas to the case where they may discharge assumption rules (i.e., rules used as assumptions). For the standard connectives this means that $A\land B$ expresses the content of the pair $(A,B)$; $A \rightarrow B$ expresses the content of the rule $A \Rightarrow B$; $A\lor B$ expresses the common content of A and B; and absurdity $\bot$ expresses the common content of the empty family of rule systems. For arbitrary n-ary propositional connectives this leads to a natural deduction system with generalized introduction and elimination rules. These general connectives are shown to be definable in terms of the standard ones, which establishes the expressive completeness of the standard intuitionistic connectives.

### 2.2 The Semantics of derivations as based on introduction rules

#### 2.2.1 Inversion principles and harmony

In his *Investigations into Logical Deduction*, Gentzen makes some (frequently quoted) programmatic remarks on the semantic relationship between introduction and elimination inferences in natural deduction.

> The introductions represent, as it were, the ‘definitions’ of the symbols concerned, and the eliminations are no more, in the final analysis, than the consequences of these definitions. This fact may be expressed as follows: In eliminating a symbol, we may use the formula with whose terminal symbol we are dealing only ‘in the sense afforded it by the introduction of that symbol’. (Gentzen, 1934/35, p. 80)[^gentzen-1934]

This cannot mean, of course, that the elimination rules are *deducible* from the introduction rules in the literal sense of the word; in fact, they are not. It can only mean that they can be *justified* by them in some way.

> By making these ideas more precise it should be possible to display the E-inferences as unique functions of their corresponding I-inferences, on the basis of certain requirements. (ibid., p. 81)

So the idea underlying Gentzen’s programme is that we have “definitions” in the form of introduction rules and some sort of semantic reasoning which, by using “certain requirements”, validate the elimination rules.

By adopting Lorenzen’s term and adapting its underlying idea (see section 2.1.1) to the context of natural deduction, Prawitz (1965) formulated an “inversion principle” to make Gentzen’s remarks more precise:

> Let $\alpha$ be an application of an elimination rule that has B as consequence. Then, deductions that satisfy the sufficient condition […] for deriving the major premiss of $\alpha$, when combined with deductions of the minor premisses of $\alpha$ (if any), already “contain” a deduction of B; the deduction of B is thus obtainable directly from the given deductions without the addition of $\alpha$. (p. 33)

Here the sufficient conditions are given by the premisses of the corresponding introduction rules. Thus the inversion principle says that a derivation of the conclusion of an elimination rule can be obtained without an application of the elimination rule if its major premiss has been derived using an introduction rule in the last step, which means that a combination

$$\begin{prooftree} \AxiomC{$\vdots$} \RightLabel{I-inference} \UnaryInfC{$A$} \AxiomC{$\{\mathcal{D}_i\}$} \RightLabel{E-inference} \BinaryInfC{$B$} \end{prooftree}$$

of steps, where $\{\mathcal{D}_i\}$ stands for a (possibly empty) list of deductions of minor premisses, can be avoided.

The relationship between introduction and elimination rules is often described as “harmony” (Dummett 1973, pp. 396–397)[^dummett-1973], or as governed by a “principle of harmony” (Tennant, 1978, p. 74)[^tennant-1978]. This terminology is not uniform and sometimes not even fully clear. It essentially expresses what is also meant by “inversion”. Even if “harmony” is a term which suggests a symmetric relationship, it is frequently understood as expressing a conception based on introduction rules as, e.g., in Read’s (2010) “general elimination harmony” (although occasionally one includes elimination-based conceptions as well). Sometimes harmony is supposed to mean that connectives are strongest or weakest in a certain sense given their introduction or their elimination rules. This idea underlies Tennant’s (1978) harmony principle, and also Popper’s and Koslow’s structural characterizations (see section 2.4). The specific relationship between introduction and elimination rules as formulated in an inversion principle excludes alleged inferential definitions such as that of the connective *tonk*, which combines an introduction rule for disjunction with an elimination rule for conjunction, and which has given rise to a still ongoing debate on the format of inferential definitions. Formal characterizations of harmony have used the translation of inference rules into second-order propositional logic (Girard’s system F) and have become a central topic of intensional proof-theoretic semantics (Tranchini, 2023)[^tranchini-2023].

*Further Reading:*

For *logical connectives* in general, see the entry on sentence connectives in formal logic.

For *inversion principles*, see Schroeder-Heister (2007).

For *variants of proof-theoretic harmony*, see Francez (2015), Schroeder-Heister (2016) and Tranchini (2023).

#### 2.2.2 Proof-theoretic validity

Proof-theoretic validity is the leading approach in proof-theoretic semantics. As a technical concept it was developed by Prawitz (1971; 1973; 1974), by turning a proof-theoretic validity notion based on ideas by Tait (1967) and originally used to prove strong normalization, into a semantical concept. Dummett provided much philosophical underpinning to this notion (see Dummett, 1991)[^dummett-1991]. The objects which are primarily valid are proofs as representations of arguments. In a secondary sense, single rules can be valid if they lead from valid proofs to valid proofs. In this sense, validity is a global rather than a local notion. It applies to arbitrary derivations over a given atomic system, which defines derivability for atoms. Calling a proof *canonical*, if it uses an introduction rule in the last step, proof-theoretic validity is based on the following three ideas:

1. The priority of closed canonical proofs.
2. The reduction of closed non-canonical proofs to canonical ones.
3. The substitutional view of open proofs.

*Ad 1:* The definition of validity is based on Gentzen’s idea that introduction rules are ‘self-justifying’ and give the logical constants their meaning. This self-justifying feature is only used for closed proofs, which are considered primary over open ones.

*Ad 2:* Noncanonical proofs are justified by reducing them to canonical ones. Thus reduction procedures (detour reductions) as used in normalization proofs play a crucial role. As they justify arguments, they are also called “justifications” by Prawitz. This definition again only applies to closed proofs, corresponding to the introduction form property of closed normal derivations in natural deduction (see section 1.3).

*Ad 3:* Open proofs are justified by considering their closed instances. These closed instances are obtained by replacing their open assumptions with closed proofs of them, and their open variables with closed terms. For example, a proof of B from A is considered valid, if every closed proof, which is obtained by replacing the open assumption A with a closed valid proof of A, is valid. In this way, open assumptions are considered to be placeholders for closed proofs, which is why we may speak of a substitutional interpretation of open proofs.

This yields the following definition of proof-theoretic validity:

1. Every closed proof in the underlying atomic system is valid.
2. A closed canonical proof is considered valid, if its immediate subproofs are valid.
3. A closed noncanonical proof is considered valid, if it reduces to a valid closed canonical proof or to a closed proof in the atomic system.
4. An open proof is considered valid, if every closed proof obtained by replacing its open assumptions with closed valid proofs and its open variables with closed terms is valid.

Formally, this definition has to be relativized to the atomic system considered (see section 2.6), and to a set of available justifications (proof reductions). Furthermore, *proofs* are here understood as *candidates* of valid proofs (“arguments” in Prawitz’s terminology), which means that the rules from which they are composed are not fixed. They look like proof trees, but their individual steps can have an arbitrary (finite) number of premisses and can eliminate arbitrary assumptions. The definition of validity singles out those proof structures which are ‘real’ proofs on the basis of the given reduction procedures.

Validity with respect to every choice of an atomic system can be viewed as a generalized notion of logical validity. In fact, if we consider the standard reductions of intuitionistic logic, then all derivations in intuitionistic logic are valid independent of the atomic system considered. This is semantical *correctness*. We may ask if the converse holds, viz. whether for any proof that is valid for every atomic system, there is a corresponding derivation in intuitionistic logic. That intuitionistic logic is complete in this sense is known as Prawitz’s conjecture (see Prawitz, 1973; 2013)[^prawitz-1973]. There are certain doubts concerning the validity of this conjecture for systems that go beyond implicational logic. In any case it will depend on the precise formulation of the notion of validity, in particular on its handling of atomic systems (see section 2.8).

For a more formal definition and detailed examples demonstrating validity, as well as some remarks on Prawitz’s conjecture see the

> [Supplement on Examples of Proof-theoretic Validity](proof-theoretic-semantics.examples.md).

*Further Reading:*

For a detailed exposition of further developments of *Prawitz’s theory of proof-theoretic validity*, in particular his theory of grounds, see Piccolomini d’Aragona (2023).

For a *computational interpretation of proof-theoretic validity* as a method for tactical proof see Gheorghiu and Pym (2022, other internet resources).

#### 2.2.3 Constructive type theory

Martin-Löf’s type theory (Martin-Löf, 1984)[^martin-löf-1984] is a leading approach in constructive logic and mathematics. Philosophically, it shares with Prawitz the three fundamental assumptions of standard proof-theoretic semantics, mentioned in section 2.2.2: the priority of closed canonical proofs, the reduction of closed non-canonical proofs to canonical ones and the substitutional view of open proofs. However, Martin-Löf’s type theory has at least two characteristic features which go beyond other approaches in proof-theoretic semantics:

1. The consideration of proof objects and the corresponding distinction between proofs-as-objects and proofs-as-demonstrations.
2. The view of formation rules as intrinsic to the proof system rather than as external rules.

The first idea goes back to the Curry-Howard correspondence (see de Groote, 1995; Sørensen and Urzyczyn, 2006)[^groote-1995][^sørensen-2006], according to which the fact that a formula A has a certain proof can be codified as the fact that a certain term t is of type A, whereby the formula A is identified with the type A. This can be formalized in a calculus for type assignment, whose statements are of the form $t {:} A$. A proof of $t {:} A$ in this system can be read as showing that t is a proof of A. Martin-Löf (1995; 1998) has put this into a philosophical perspective by distinguishing this two-fold sense of proof in the following way. First we have proofs of statements of the form $t {:} A$. These statements are called *judgements*, their proofs are called *demonstrations*. *Within* such judgements the term t represents a *proof* of the *proposition* A. A proof in the latter sense is also called a *proof object*. When demonstrating a judgement $t {:} A$, we demonstrate that t is a proof (object) for the proposition A. Within this two-layer system the *demonstration* layer is the layer of argumentation. Unlike proof objects, demonstrations have epistemic significance; their judgements carry assertoric force. The proof layer is the layer at which meanings are explained: The meaning of a proposition A is explained by telling what counts as a proof (object) for A. The distinction made between canonical and non-canonical proofs is a distinction at the propositional and not at the judgemental layer. This implies a certain explicitness requirement. When I have proved something, I must not only have a justification for my proof *at my disposal* as in Prawitz’s notion of validity, but at the same time have to be *certain* that this justification fulfills its purpose. This certainty is guaranteed by a demonstration. Mathematically, this two-fold sense of proof develops its real power only when types may depend on terms. Dependent types are a basic ingredient of of Martin-Löf’s type theory and related approaches.

The second idea makes Martin-Löf’s approach strongly differ from all other definitions of proof-theoretic validity. The crucial difference, for example, to Prawitz’s procedure is that it is not *metalinguistic* in character, where “metalinguistic” means that propositions and candidates of proofs are specified first and then, by means of a definition in the metalanguage, it is fixed which of them are valid and which are not. Rather, propositions and proofs come into play only in the context of demonstrations. For example, if we assume that something is a proof of an implication $A \rightarrow B$, we need not necessarily show that both A and B are well-formed propositions outright, but, in addition to knowing that A is a proposition, we only need to know that B is a proposition *provided that* A *has been proved*. Being a proposition is expressed by a specific form of judgement, which is established in the same system of demonstration which is used to establish that a proof of a proposition has been achieved.

In Martin-Löf’s theory, proof-theoretic semantics receives a strongly ontological component. A recent debate deals with the question of whether proof objects have a purely ontological status or whether they codify knowledge, even if they are not epistemic acts themselves. More recently, Martin-Löf has embedded his approach into a theory of interaction between assertions, challenges and obligations (Martin-Löf 2019)[^martin-löf-2019] which gives his proof-theoretic semantics a pragmatic aspect and also relates it to dialogical semantics (see section 3.9).

Martin-Löf’s type theory has found its most significant mathematical application in homotopy theory, leading to homotopy type theory (HoTT) and the univalent foundations programme (The Univalent Foundations Program 2013)[^univalent-2013]. The latter is often (sometimes controversially) considered a novel foundational approach to mathematics in the intuitionistic spirit, as an alternative to classical set-theoretic approaches.

*Further Reading:*

For the history and philosophy of *Martin-Löf*’*s type theory* see Sommaruga (2000). For *type theory* in general, for *homotopy type theory*, and for the *univalent foundations* programme, see the entry on intuitionistic type theory and the entry on type theory.

### 2.3 Clausal definitions and definitional reasoning

Proof-theoretic semantics normally focuses on logical constants. This focus is practically never questioned, apparently because it is considered so obvious. In proof theory, little attention has been paid to atomic systems, although there has been Lorenzen’s early work (see section 2.1.1), where the justification of logical rules is embedded in a theory of arbitrary rules, and Martin-Löf’s (1971) theory of iterated inductive definitions where introduction and elimination rules for atomic formulas are proposed. The rise of logic programming has widened this perspective. From the proof-theoretic point of view, logic programming is a theory of atomic reasoning with respect to clausal definitions of atoms. Definitional reflection is an approach to proof-theoretic semantics that takes up this challenge and attempts to build a theory whose range of application goes beyond logical constants.

#### 2.3.1 The challenge from logic programming

In logic programming we are dealing with program clauses of the form

$$ A \Leftarrow B_1 , \ldots ,B_m $$

which *define* atomic formulas. Such clauses can naturally be interpreted as describing introduction rules for atoms. From the point of view of proof-theoretic semantics the following two points are essential:

(1) Introduction rules (clauses) for logically compound formulas are not distinguished in principle from introduction rules (clauses) for atoms. Interpreting logic programming proof-theoretically motivates an extension of proof-theoretic semantics to arbitrary atoms, which yields a semantics with a much wider realm of applications.

(2) Program clauses are not necessarily well-founded. For example, the head of a clause may occur in its body. Well-founded programs are just a particular sort of programs. The use of arbitrary clauses without further requirements in logic programming is a motivation to pursue the same idea in proof-theoretic semantics. One would admit any sort of introduction rules and not just those of a special form, and in particular not necessarily ones which are well-founded. This carries the idea of definitional freedom, which is a cornerstone of logic programming, over to semantics, again widening the realm of application of proof-theoretic semantics.

The idea of considering introduction rules as meaning-giving rules for atoms is closely related to the theory of inductive definitions in its general form, according to which inductive definitions are systems of rules (see Aczel, 1977)[^aczel-1977].

#### 2.3.2 Definitional reflection

The theory of definitional reflection (Hallnäs, 1991; 2006; Hallnäs and Schroeder-Heister, 1990/91; Schroeder-Heister, 1993)[^hallnäs-1991][^hallnäs-1990][^schroeder-heister-1993] takes up the challenge from logic programming and gives a proof-theoretic semantics not just for logical constants but for arbitrary expressions, for which a clausal definition can be given. Formally, this approach starts with a list of clauses which is the *definition* considered. Each clause has the form

$$ A \Leftarrow \Delta $$

where the head A is an atomic formula (atom). In the simplest case, the body $\Delta$ is a list of atoms $B_1,\ldots,B_m$, in which case a definition looks like a definite logic program. We often consider an extended case where $\Delta$ may also contain some structural implication ‘$\Rightarrow$’, and sometimes even some structural universal quantification, which essentially is handled by restricting substitution. If the definition of A has the form

$$ \mathbb{D}_A\ \left\{ \begin{array}{rcl} A & \Leftarrow & \Delta_1 \\ & \vdots & \\ A & \Leftarrow & \Delta_n \end{array} \right. $$

then A has the following introduction and elimination rules

$$ \begin{prooftree} \AxiomC{$\Delta_1$} \UnaryInfC{$A$} \end{prooftree} \;\cdots\; \begin{prooftree} \AxiomC{$\Delta_n$} \UnaryInfC{$A$} \end{prooftree} $$ $$ \begin{prooftree} \AxiomC{$A$} \AxiomC{$[\Delta_1]$} \noLine\UnaryInfC{$C$} \AxiomC{$\cdots$} \AxiomC{$[\Delta_n]$} \noLine\UnaryInfC{$C$} \QuaternaryInfC{$C$} \end{prooftree} $$

The introduction rules, also called rules of *definitional closure*, express reasoning ‘along’ the clauses. The elimination rule is called the *principle of definitional reflection*, as it reflects upon the definition as a whole. If $\Delta_1,\ldots,\Delta_n$ exhaust *all possible conditions* to generate A according to the given definition, and if each of these conditions entails the very same conclusion C, then A itself entails this conclusion. If the clausal definition is viewed as an inductive definition, this principle can be viewed as expressing the extremal clause in inductive definitions: Nothing else beyond the clauses given defines A. Obviously, definitional reflection is a generalized form of the inversion principles discussed. It develops its genuine power in definitional contexts with free variables that go beyond purely propositional reasoning, and in contexts which are not well-founded. An example of a non-wellfounded definition is the definition of an atom R by its own negation:

$$ \mathbb{D}_R \;\{\; R \Leftarrow (R \Rightarrow \bot) $$

Defining an atom by its negation is a standard example in logic programming. In the context of definitional reflection it was suggested by Hallnäs. It is here discussed in detail in the

> [Supplement on Definitional Reflection and Paradoxes](proof-theoretic-semantics.definitional-reflection.md).

*Further Reading:*

For *non-wellfoundedness* and *paradoxes* see the entry on self-reference and the entry on Russell’s paradox.

### 2.4 Structural characterization of logical constants

There is a large field of ideas and results concerning what might be called the “structural characterization” of logical constants, where “structural” is here meant both in the proof-theoretic sense of “structural rules” and in the sense of a framework that bears a certain structure, where this framework is again proof-theoretically described. Some of its authors use a semantical vocabulary and at least implicitly suggest that their topic belongs to proof-theoretic semantics. Others explicitly deny these connotations, emphasizing that they are interested in a characterization which establishes the logicality of a constant. The question “What is a logical constant?” can be answered in proof-theoretic terms, even if the semantics of the constants themselves is truth-conditional: Namely by requiring that the (perhaps truth-conditionally defined) constants show a certain inferential behaviour that can be described in proof-theoretic terms. However, as some of the authors consider their characterization at the same time as a semantics, it is appropriate that we mention some of these approaches here.

The most outspoken structuralist with respect to logical constants, who explicitly understands himself as such, is Koslow. In his *Structuralist Theory of Logic* (1992) he develops a theory of logical constants, in which he characterizes them by certain “implication relations”, where an implication relation roughly corresponds to a finite consequence relation in Tarski’s sense (which again can be described by certain structural rules of a sequent-style system). Koslow develops a structural theory in the precise metamathematical sense, which does not specify the domain of objects in any way beyond the axioms given. If a language or any other domain of objects equipped with an implication relation is given, the structural approach can be used to single out logical compounds by checking their implicational properties.

In his early papers on the foundations of logic, Popper (1947a; 1947b; Binder et al., eds., 2022)[^binder-2022][^binder-2022-2] gives inferential characterizations of logical constants in proof-theoretic terms. He uses a calculus of sequents and characterizes logical constants by certain derivability conditions for such sequents. His terminology clearly suggests that he intends a proof-theoretic semantics of logical constants, as he speaks of “inferential definitions” and the “trivialization of mathematical logic” achieved by defining constants in the way described. Although his presentation is not free from conceptual imprecision and error, he anticipated many ideas now common in proof-theoretic semantics, such as the delineation of logical constants by means of certain minimality or maximality conditions with respect to introduction or elimination rules.

Important contributions to the logicality debate that characterize logical constants inferentially in terms of sequent calculus rules are those by Kneale (1956) and Hacking (1979). A thorough account of logicality is proposed by Došen (1980; 1989) in his theory of logical constants as “punctuation marks”, expressing structural features at the logical level. He understands logical constants as following certain double-line rules for sequents which can be read in both directions. For example, conjunction and disjunction obey (in classical logic, with multiple-formulae succedents) the double-line rules

$$ \xlongequal[{\Large \Gamma \,\vdash\, A \,\land\, B,\, \Delta}] {{\Large \Gamma \,\vdash\, A,\, \Delta\quad \Gamma \,\vdash\, B,\, \Delta}} \hspace{2em} \xlongequal[{\Large \Gamma,\, A \,\lor\, B \,\vdash\, \Delta}] {{\Large \Gamma,\, A \,\vdash\, \Delta\quad \Gamma,\, B \,\vdash\, \Delta}} $$

Došen is able to give characterizations which include systems of modal logic. He explicitly considers his work as a contribution to the logicality debate and not to any conception of proof-theoretic semantics. Sambin et al., in their Basic Logic (Sambin, Battilotti, and Faggian, 2000)[^sambin-2000], explicitly understand what Došen calls double-line rules as fundamental meaning giving rules. The double-line rules for conjunction and disjunction are read as implicit definitions of these constants, which by some procedure can be turned into the explicit sequent-style rules we are used to. So Sambin et al. use the same starting point as Došen, but interpret it not as a structural description of the behaviour of constants, but semantically as their implicit definition.

There are several other approaches to a uniform proof-theoretic characterization of logical constants, all of which at least touch upon issues of proof-theoretic semantics. Such theories are Belnap’s Display Logic (Belnap, 1982)[^belnap-1982], Wansing’s Logic of Information Structures (Wansing, 1993b)[^wansing-1993b], generic proof editing systems and their implementations such as the Edinburgh Logical Framework (Harper, Honsell, and Plotkin, 1987)[^harper-1987] and many successors which allow the specification of a variety of logical systems. Since the rise of linear and, more generally, substructural logics there are various approaches dealing with logics that differ with respect to restrictions on their structural rules (see section 3.10). A recent movement away from singling out a particular logic as the true one towards a more pluralist stance (see, e.g., Beall and Restall, 2006)[^beall-2006], which is interested in what different logics have in common without any preference for a particular logic, can be seen as a shift away from semantical justification towards structural characterization.

*Further Reading:*

For *Popper’s theory of logical constants* see Binder et al. (2022), Piecha (2023).

For *logical constants* and their *logicality* see the entry on logical constants.

For *linear* and *substructural logics* see the entry on linear logic, and the entry on substructural logics.

For *pluralism in logic*, see the entry on on logical pluralism.

### 2.5 Categorial proof theory

There is a considerable literature on category theory in relation to proof theory, and, following seminal work by Lawvere, Lambek and others (see Lambek and Scott, 1986)[^lambek-1986], category theory itself can be viewed as a kind of abstract proof theory. If one looks at an arrow $A \rightarrow B$ in a category as a kind of abstract proof of B from A, we have a representation which goes beyond pure derivability of B from A (as the arrow has its individuality), but does not deal with the particular syntactic structure of this proof. For intuitionistic systems, proof-theoretic semantics in categorial form comes probably closest to what denotational semantics is in the classical case.

One of the most highly developed approaches to categorial proof theory is due to Došen. He has not only advanced the application of categorial methods in proof theory (e.g., Došen and Petrić, 2004)[^došen-2004], but also shown how proof-theoretic methods can be used in category theory itself (Došen, 2000)[^došen-2000]. Most important for categorial logic in relation to proof-theoretic semantics is that in categorial logic, arrows always come together with an identity relation, which in proof-theory corresponds to the identity of proofs. In this way, ideas and results of categorial proof theory pertain to what may be called intensional proof-theoretic semantics (see section 3.7), that is, the study of proofs as entities in their own right, not just as vehicles to establish consequences (Došen, 2006; 2016)[^došen-2006].

As there is the strong relationship between arrows in the categorial sense and proofs in the sense of deductive reasoning, there are categorial analogues to practically all concepts dealt with in the deductive realm, often with novel methods, ideas and results that supplement deductive approaches in a very productive way. Categorial proof-theoretic semantics is a very broad research area that runs in parallel to the deductive perspective adopted in this entry ― the deductive perspective is by far more common in philosophy. In the field of intuitionistic logic, categorial logic covers highly advanced topics: beyond standard quantifier logic dependent type theories in the tradition of Martin-Löf (see section 2.2.3) including homotopy type theory. For many other logical systems categorial semantics have been developed, including classical logic and various substructural logics such as linear logic.

A philosophically highly significant general feature of categorial proof-theory is its inherently hypothetical character. This is due to the fact that it starts from hypothetical statements $A \rightarrow B$ (arrows) rather than categorical statements A (“categorical” as opposed to “hypothetical”, not “categorial” which is used here for “pertaining to category theory”). It this way it overcomes a paradigm of standard, in particular validity-based, proof-theoretic semantics (see section 3.6).

*Further Reading:*

For *categorial approaches* in general see the entry on category theory and the entry on structuralism in the philosophy of mathematics.

For *categorial proof-theoretic semantics* see Pym, Ritter, and Robinson (2023, other internet resources).

### 2.6 Atomic systems

Proof-theoretic semantics is predominantly concerned with logical constants. Even if one agrees with this orientation — the theory of definitional reflection (see section 2.3.2) is an exception to it — we must nonetheless fix the status of atomic sentences and their proofs. In model-theoretic semantics the truth of a logically complex sentence is defined with respect to a structure, which is called a “model” of this sentence. This structure determines, which atomic sentences are true and which are not. Whether a complex sentence is true hinges on its atomic constituents. This is quite analogous in proof-theoretic semantics. Whether a proof of a complex sentence is valid depends on the atomic base of the system under consideration. Here an atomic base is normally considered a calculus for the generation of atomic sentences: Proofs of atomic sentences in the atomic base are per se valid. Similar to the model-theoretic definition of logical truth as truth with respect to all structures, in proof-theoretic semantics one would define logically valid proofs as proofs which are valid with respect to all atomic bases.

There are various options which atomic systems should be considered to be candidates for atomic bases. (1) The simplest would be Herbrand models as used in the theory of logic programming, which are just collections of atomic sentences. Proof-theoretically, these would be calculi consisting of axioms only, without proper rules of inference. (2) In the writings of Lorenzen (see section 2.1.1) and Prawitz (see section 2.2.2) atomic systems are considered lists of production rules, that is, calculi with axioms and rules of the form $A_1,\ldots,A_n \Rightarrow B$ allowing one to generate B from $A_1,\ldots,A_n$. (3) More involved systems may contain atomic rules that allow one to discharge assumptions, quite in analogy to logical rules such as implication introduction. (4) Generalizing this idea one may admit rules for atoms that discharge rules themselves, that is, rules of higher levels (see section 2.1.3). (5) Even further advanced would be atomic systems that incorporate rules of definitional reflection (see section 2.3.2). — Many other sorts of rules for atoms constituting atomic systems may be imagined.

For proof-theoretic semantics, the critical point here is that certain formal results depend on which types of atomic systems are admitted. This holds in particular for the issue of semantical completeness (see section 2.8). The investigation of which atomic systems, when taken as atomic bases of proof-theoretic semantics, lead to which formal system at the logical level, has just begun (see Sandqvist 2015b; Piecha and Schroeder-Heister, 2016a; Stafford 2023, other internet resources)[^piecha-2016a][^sandqvist-2015b][^stafford-2023]. It should be noted that this is an intensional feature of proof-theoretic semantics: We are not just interested in which atoms are generated by the various forms of atomic systems, but how this is done, that is, by which type of rules this is achieved. This is a crucial difference to model-theoretic semantics, which is purely extensional in this respect. For further intensional features of proof-theoretic semantics see section 3.7.

### 2.7 Sentence-based semantics

Instead of defining the validity of proofs of sentences, one can define the proof-theoretic validity of sentences directly. In the definition of validity of logically complex sentences one would then discard the reference to proofs of these sentences. This does not mean that one is giving up the proof-theoretic approach, as one would still refer to proofs in the atomic base. Proofs come in at the atomic level, but not at the logical level. This approach is technically much simpler to elaborate than the one based on the validity of proofs (see section 2.2.2), but still sufficient to discuss basic topics such as semantical completeness (see section 2.8). In fact, from a proof of a sentence A which is valid in the sense of section 2.2.2, the validity of A in the sense of sentence-based semantics can be inferred; and conversely, from the validity of A in sentence-based semantics a (though degenerate) valid proof of A can be constructed. In a sense, sentence-based semantics is related to the proof-theoretic semantics inherent in Martin-Löf’s system (see section 2.2.3), where in the case of elementary logic (where dependent types do not play any role), the proof information t of a judgement $t{:}A$ can be discarded in favour of the simplified judgement $A\ \textit{true}$.

One possible definition of the validity of sentences in minimal propositional logic with respect to an atomic system S as its atomic base in propositional logic would be the following:

1. An atomic formula A is S-valid, if it is derivable in S.
2. A conjunction $A\land B$ is S-valid, if both A and B are S-valid.
3. A disjunction $A\lor B$ is S-valid, if either A or B is S-valid.
4. An implication $A \rightarrow B$ is S valid, if for every extension $S'$ of S, if A if $S'$-valid then B is $S'$-valid.

Note that in the statement of hypothetical validity reference is made to arbitrary extensions of the atomic base considered. As in the formal definition of the validity of proofs, considering base-extensions is used to ensure monotonicity and to avoid vacuous validity. In the literature, following Sandqvist (2015a), the term “base-extension semantics” is often used in a more specific sense: namely for a special form of sentence-based semantics, in which disjunction receives a deviant interpretation.

Validity in sentence-based semantics depends on the choice of atomic systems. This choice is what makes sentence-based semantics proof-theoretic. As indicated in section 2.6, the type of atomic system counts, as does the extension relation considered for implications and consequence statements.

### 2.8 Semantical completeness

Proof-theoretic semantics is intuitionistic in spirit, at least by its origin. Correspondingly, Prawitz (1971) conjectured that those consequence statements $\Gamma \vDash A$, which are justified by proofs valid with respect to any atomic base, are exactly the derivability statements $\Gamma \vdash A$ of the formal system of intuitionistic logic. Within the framework of sentence semantics, which for the issue of validity in relation to semantical completeness is easier to handle than the framework of valid proofs, this conjecture turned out to be false. Harrop’s rule

$$ \begin{prooftree} \AxiomC{$\neg A \to (B \lor C)$} \UnaryInfC{$(\neg A \to B) \lor (\neg A \to C)$} \end{prooftree} $$

which is not derivable (but only admissible) in intuitionistic logic can be validated in this framework (Piecha and Schroeder-Heister, 2019)[^piecha-2019]. However, when the extension structure of atomic bases is modified beyond the set-theoretical superset relation, the picture changes and Kripke’s completeness proof for intuitionistic logic becomes applicable to the proof-theoretic framework (Goldfarb 2016; Stafford and Nascimento 2023)[^goldfarb-2016][^stafford-2023]. Another way to avoid incompleteness is to give disjunction a non-standard interpretation, for example by requiring that the minor premisses and conclusion of the rule of $\lor$-elimination can always be considered atomic (see Sandqvist, 2015a)[^sandqvist-2015a].

*Further Reading:*

For Prawitz’s completeness conjecture see the [Supplement on Examples of Proof-theoretic Validity](proof-theoretic-semantics.examples.md).

For the role of Harrop’s rule in the context of admissibility statements for intuitionistic logic, see the entry on intuitionistic logic.

## 3. Extensions and alternatives to standard proof-theoretic semantics

### 3.1 Elimination rules as basic

Most approaches to proof-theoretic semantics consider introduction rules as basic, meaning giving, or self-justifying, whereas the elimination inferences are justified as valid with respect to the given introduction rules. This conception has at least three roots: The first is a verificationist theory of meaning according to which the assertibility conditions of a sentence constitute its meaning. The second is the idea that we must distinguish between what gives the meaning and what are the consequences of this meaning, as not all inferential knowledge can consist of applications of definitions. The third one is the primacy of assertion over other speech acts such as assuming or denying, which is implicit in all approaches considered so far.

One might investigate how far one gets by considering elimination rules rather than introduction rules as a basis of proof-theoretic semantics. Some ideas towards a proof-theoretic semantics based on elimination rather than introduction rules have been sketched by Dummett (1991, Ch. 13), albeit in a very rudimentary form. A more precise definition of validity based on elimination inferences is due to Prawitz (1971; 2007; see also Schroeder-Heister 2015)[^schroeder-heister-2015]. Its essential idea is that a closed proof is considered valid, if the result of applying an elimination rule to its end formula is a valid proof or reduces to one. For example, a closed proof of an implication $A \rightarrow B$ is valid, if, for any given closed valid proof of A, the result of applying modus ponens

$$\begin{prooftree} \AxiomC{$A \to B$} \AxiomC{$A$} \BinaryInfC{$B$} \end{prooftree}$$

to these two proofs is a valid proof of B, or reduces to such a proof. This conception keeps two of the three basic ingredients of Prawitz-style proof-theoretic semantics (see section 2.2.2): the role of proof reduction and the substitutional view of assumptions. Only the canonicity of proofs ending with introductions is turned into the canonicity of proofs ending with eliminations.

### 3.2 Negation and denial

Standard proof-theoretic semantics is assertion-centred in that assertibility conditions determine the meaning of logical constants. Corresponding to the intuitionistic way of proceeding, the negation $\neg A$ of a formula A is normally understood as implying absurdity $A \rightarrow \bot$, where $\bot$ is a constant which cannot be asserted, i.e., for which no assertibility condition is defined. This is an ‘indirect’ way of understanding negation. In the literature there has been the discussion of what, following von Kutschera (1969), might be called ‘direct’ negation. By that one understands a one-place primitive operator of negation, which cannot be, or at least is not, reduced to implying absurdity. It is not classical negation either. It rather obeys rules which dualize the usual rules for the logical constants. Sometimes it is called the “denial” of a sentence, sometimes also “strong negation” (see Odintsov, 2008)[^odintsov-2008]. Typical rules for the denial ${\sim}A$ of A are

$$ \begin{prooftree} \AxiomC{${\sim}A$} \AxiomC{${\sim}B$} \BinaryInfC{${\sim}(A \lor B)$} \end{prooftree} \hspace{1.5em} \begin{prooftree} \AxiomC{${\sim}A$} \UnaryInfC{${\sim}(A \land B)$} \end{prooftree} \hspace{1.5em} \begin{prooftree} \AxiomC{${\sim}B$} \UnaryInfC{${\sim}(A \land B)$} \end{prooftree} $$

Essentially, the denial rules for an operator correspond to the assertion rules for the dual operator. Several logics of denial have been investigated, in particular Nelson’s (1949) logics of “constructible falsity” motivated by Nelson with respect to a certain realizability semantics. The main focus has been on his systems later called N3 and N4 which differ with respect to the treatment of contradiction (N4 is N3 without *ex contradictione quodlibet*). Using denial any approach to proof-theoretic semantics can be dualized by just exchanging assertion and denial and turning from logical constants to their duals. In doing so, one obtains a system based on refutation $(=$ proof of denial) rather than proof. It can be understood as applying a Popperian view to proof-theoretic semantics by keeping its intuitionistic spirit. Formally, it leads to systems such as dual intuitionistic logic by giving them a proof-theoretic semantics.

Another approach would be to not just dualize assertion-centered proof-theoretic semantics in favour of a denial-centered refutation-theoretic semantics, but to see the relation between rules for assertion and for denial as governed by an inversion principle or principle of definitional reflection of its own. This would be a principle of what might be called “assertion-denial-harmony”. Whereas in standard proof-theoretic semantics, inversion principles control the relationship between assertions and assumptions (or consequences), such a principle would now regulate the relationship between assertion and denial. Given certain defining conditions of A, it would say that the denial of every defining condition of A leads to the denial of A itself. For conjunction and disjunction this leads to the common pairs of assertion and denial rules

$$ \begin{prooftree} \AxiomC{$A$} \UnaryInfC{$A \lor B$} \end{prooftree} \hspace{1.5em} \begin{prooftree} \AxiomC{$B$} \UnaryInfC{$A \lor B$} \end{prooftree} \hspace{1.5em} \begin{prooftree} \AxiomC{${\sim}A$} \AxiomC{${\sim}B$} \BinaryInfC{${\sim}(A \lor B)$} \end{prooftree} $$ $$ \begin{prooftree} \AxiomC{$A$} \AxiomC{$B$} \BinaryInfC{$A \land B$} \end{prooftree} \hspace{1.5em} \begin{prooftree} \AxiomC{${\sim}A$} \UnaryInfC{${\sim}(A \land B)$} \end{prooftree} \hspace{1.5em} \begin{prooftree} \AxiomC{${\sim}B$} \UnaryInfC{${\sim}(A \land B)$} \end{prooftree} $$

This idea can easily be generalized to definitional reflection, yielding a reasoning system in which assertion and denial are intertwined. It has parallels to the deductive relations between the forms of judgement studied in the traditional square of opposition (Schroeder-Heister, 2012a; Zeilberger, 2008)[^schroeder-heister-2012a][^zeilberger-2008]. It should be emphasized that the denial operator is here an external sign indicating a form of judgement and not a logical operator. This means in particular that it cannot be iterated.

The idea that both assertion and denial conditions give meaning to a sentence and thus to logical operations also figures under the term “bilateralism”, a term coined by Rumfitt.

*Further Reading*

For the proof-theoretic semantics of *negation and denial* see Tranchini (2012b), Wansing (2001; 2017), as well as the special issue on *assertion and denial* edited by Carrara, Chiffi and De Florio (2017) and the entry on negation, the entry on connexive logic and the entry on contradiction.

For the idea of bilateralism see Rumfitt (2000), Kürbis (2016; 2019), Drobyshevich (2021) and the special issue on *bilateralism and proof-theoretic semantics* edited by Sara Ayhan (2023).

For Popperianism and proof theoretic semantics see Binder et al. (2022), Kapsner (2014).

### 3.3 Harmony and reflection in the sequent calculus

Gentzen’s sequent calculus exhibits a symmetry between right and left introduction rules which suggest to look for a harmony principle that makes this symmetry significant for proof-theoretic semantics. At least three lines have been pursued to deal with this phenomenon. (i) Either the right-introduction or or the left-introduction rules are considered to be introduction rules. The opposite rules (left-introductions and right-introductions, respectively) are then justified using the corresponding elimination rules. This means that the methods discussed before are applied to whole sequents rather than formulas within sequents. Unlike these formulas, the sequents are not logically structured. This approach builds on definitional reflection, which applies harmony and inversion to rules for arbitrarily structured entities rather than for logical compounds only. It has been pursued by de Campos Sanz and Piecha (2009). (ii) The right- and left-introduction rules are derived from a characterization in the sense of Došen’s double line rules (section 2.4), which is then read as a definition of some sort. The top-down direction of a double-line rule is already a right- or a left-introduction rule. The other one can be derived from the bottom-up direction by means of certain principles. This is the basic meaning-theoretic ingredient of Sambin et al.’s *Basic Logic* (Sambin, Battilotti, and Faggian, 2000)[^sambin-2000]. (iii) The right- and left-introduction rules are seen as expressing an interaction between sequents using the rule of cut. Given either the right- or the left-rules, the complementary rules express that everything that interacts with its premisses in a certain way so does with its conclusion. This idea of interaction is a generalized symmetric principle of definitional reflection. It can be considered to be a generalization of the inversion principle, using the notion of interaction rather than the derivability of consequences (see Schroeder-Heister, 2013)[^schroeder-heister-2013]. All three approaches apply to the sequent calculus in its classical form, with possibly more than one formula in the succedent of a sequent, including structurally restricted versions as investigated in linear and other logics. Therefore this topic touches very much the issue of substructural logic and of substructural approaches to proof-theoretic semantics (see section 3.10).

### 3.4 Subatomic structure and natural language

Even if, as in definitional reflection, we are considering definitional rules for atoms, their defining conditions do not normally decompose these atoms. A proof-theoretic approach that takes the internal structure of atomic sentences into account, has been proposed by Więckowski (2008; 2011; 2016; 2021). He uses introduction and elimination rules for atomic sentences, where these atomic sentences are not just reduced to other atomic sentences, but to subatomic expressions representing the meaning of predicates and individual names. Apart from its foundational significance, this can be seen as a first step towards natural language applications of proof-theoretic semantics. A further step in this direction has been undertaken by Francez, who developed a proof-theoretic semantics for several fragments of English (see Francez, Dyckhoff, and Ben-Avi, 2010; Francez and Dyckhoff, 2010; Francez and Ben-Avi, 2015; Francez, 2022)[^francez-2015][^francez-2022][^francez-2015-2][^francez-2010][^francez-2010-2]. Specifically, Francez is able to use the proof-theoretic approach to deal with scope ambiguity and many other issues of semantic meaning variation. Besides computer science, natural language grammar and natural language semantics will play a key role in the practical application of proof-theoretic semantics.

*Further Reading*

For the proof-theoretic semantics of *natural language* see Francez (2015, Part II).

### 3.5 Classical logic

Proof-theoretic semantics is intuitionistically biased. This is due to the fact that natural deduction as its preferred framework has certain features which make it particularly suited for intuitionistic logic. In classical natural deduction the *ex falso quodlibet*

$$\begin{prooftree} \AxiomC{$\bot$} \UnaryInfC{$A$} \end{prooftree}$$

is replaced with the rule of *classical reductio ad absurdum*

$$\begin{prooftree} \AxiomC{$[A\to \bot]$} \noLine\UnaryInfC{$\bot$} \UnaryInfC{$A$} \end{prooftree}$$

In allowing to discharge $A \rightarrow \bot$ in order to infer A, this rule undermines the *subformula principle*. Furthermore, in containing both $\bot$ and $A \rightarrow \bot$, it refers to two different logical constants in a single rule, so there is no *separation* of logical constants any more. Finally, as an elimination rule for $\bot$ it does not follow the general pattern of introductions and eliminations. As a consequence, it destroys the *introduction form property* that every closed derivation can be reduced to one which uses an introduction rule in the last step.

Classical logic fits very well with the multiple-succedent sequent calculus. There we do not need any additional principles beyond those assumed in the intuitionistic case. Just the structural feature of admitting more than one formula in the succedent suffices to obtain classical logic. As there are plausible approaches to establish a harmony between right-introduction and left-introduction in the sequent calculus (see section 3.3), classical logic appears to be perfectly justified. However, this is only convincing if reasoning is appropriately framed as a multiple-conclusion process, even though this does not correspond to our standard practice where we focus on single conclusions. One could try to develop an appropriate intuition by arguing that reasoning towards multiple conclusions delineates the area in which truth lies rather than establishing a single proposition as true. However, this intuition is hard to maintain and cannot be formally captured without serious difficulties. Philosophical approaches such as those by Shoesmith and Smiley (1978) and proof-theoretic approaches such as proof-nets (see Girard, 1987; the entry on linear logic)[^girard-1987] are attempts in this direction.

A fundamental reason for the failure of the introduction form property in classical logic is the indeterminism inherent in the laws for disjunction. $A\lor B$ can be inferred from A as well as from B. Therefore, if the disjunction laws were the only way of inferring $A\lor B$, the derivability of $A\lor \neg A$, which is a key principle of classical logic, would entail that of either A or of $\neg A$, which is absurd. A way out of this difficulty is to abolish indeterministic disjunction and use instead its classical de Morgan equivalent $\neg(\neg A \land \neg B)$. This leads essentially to a logic without proper disjunction. In the quantifier case, there would be no proper existential quantifier either, as $\exists xA$ would be understood in the sense of $\neg \forall x\neg A$. If one is prepared to accept this restriction, then certain harmony principles can be formulated for classical logic.

As Karl Popper was the first to observe (see Binder et al., 2022)[^binder-2022][^binder-2022-2], the simple combination of rules for classical and intuitionistic connectives collapses into the classical system. More sophisticated theories that combine classical and intuitionistic systems in a faithful way are found in *ecumenical systems* (see Pimentel and Pereira 2021). Approaches to classical logic originally developed in computer science by algorithmic considerations, in particular in the context of proof search, are Michel Parigot’s $\lambda \mu$-calculus (Parigot 1992)[^parigot-1992] and the application of the focusing method to classical logic (Liang and Miller, 2009; 2024)[^liang-2009]. Both approaches rest on the idea that by certain indexing techniques a single formula in the multiple-formula succedent of a classical sequent can be distinguished and dealt with individually.

*Further Reading*

For *classical logic* in general see the entry on classical logic.

### 3.6 Hypothetical reasoning

Standard approaches to proof-theoretic semantics, especially Prawitz’s validity-based approach (section 2.2.2), take closed derivations as basic. The validity of open derivations is defined as the transmission of validity from closed derivations of the assumptions to a closed derivation of the assertion, where the latter is obtained by substituting a closed derivation for an open assumption. Therefore, if one calls closed derivations ‘categorical’ and open derivations ‘hypothetical’, one may characterize this approach as following two fundamental ideas: (I) The primacy of the categorical over the hypothetical, (II) the transmission view of consequence. These two assumptions (I) and (II) may be viewed as *dogmas of standard semantics*. “Standard semantics” here not only means standard proof-theoretic semantics, but also classical model-theoretic semantics, where these dogmas are assumed as well. There one starts with the definition of truth, which is the categorical concept, and defines consequence, the hypothetical concept, as the transmission of truth from conditions to consequent. From this point of view, constructive semantics, including proof-theoretic semantics, exchange the concept of truth with a concept of construction or proof, and interpret “transmission” in terms of a constructive function or procedure, but otherwise leave the framework untouched.

There is nothing wrong in principle with these dogmas. However, there are phenomena that are difficult to deal with in the standard framework. Such a phenomenon is non-wellfoundedness, especially circularity, where we may have consequences without transmission of truth and provability (see section 3.8). Another phenomenon are substructural distinctions, where it is crucial to include the structuring of assumptions from the very beginning (see section 3.10). Moreover, and this is most crucial, we might define things in a certain way without knowing in advance of whether our definition or chain of definitions is well-founded or not. We do not first involve ourselves into the metalinguistic study of the definition we start with, but would like to start to reason immediately. This problem does not obtain if we restrict ourselves to the case of logical constants, where the defining rules are trivially well-founded. But the problem arises immediately, when we consider more complicated cases that go beyond logical constants.

This makes it worthwhile to proceed in the other direction and start with the hypothetical concept of consequence, i.e., characterize consequence directly without reducing it to the categorical case. Philosophically this means that the categorical concept is a limiting concept of the hypothetical one. In the classical case, truth would be a limiting case of consequence, namely consequence without hypotheses. This program is closely related to the approach of categorial proof theory (see section 2.5), which is based on the primacy of hypothetical entities (“arrows”). Formally, it would give preference to the sequent calculus over natural deduction, since the sequent calculus allows the manipulation of the assumption side of a sequence by means of left-introduction rules. In a term-annotated system, we would not annotate formulas, but hypothetical statements by terms. If a hypothetical statement is expressed by a sequent in the form $A \vdash B$, we would not annotate it as $x{:}A \vdash t(x){:}B$ as in the Curry-Howard correspondence, but in a way like $f{:}(A \vdash B)$. That is, the full hypothetical statement would be annotated, which makes the parallel to the categorial approach, where f would be the arrow $f : A \rightarrow B$, obvious.

*Further Reading*

For *hypothetical reasoning* and *intensional proof theoretic semantics* see Došen (2003; 2016) and Schroeder-Heister (2012c, 2016).

### 3.7 Intensional proof-theoretic semantics

As mentioned in the first section (1.1), proof-theoretic semantics is intensional in spirit, as it is interested in proofs and not just provability. For proof-theoretic semantics it is not only relevant, whether B follows from A, but also, in which way we can establish that B follows from A. In other words, the identity of proofs is an important issue. However, though this is prima facie obvious and proof-theoretic semanticists would normally agree with this abstract claim, the practice in proof-theoretic semantics is often different, and the topic of the identity of proofs is much neglected. It very frequently happens that rules which are equally powerful are identified. For example, when principles of harmony are discussed, and one considers the standard introduction rule for conjunction $$\begin{prooftree} \AxiomC{$A$} \AxiomC{$B$} \BinaryInfC{$A\land B$} \end{prooftree}$$

many proof-theoretic semanticists would consider it irrelevant whether one chooses the pair of projections

$$ \begin{prooftree} \AxiomC{$A \land B$} \UnaryInfC{$A$} \end{prooftree} \hspace{1.5em} \begin{prooftree} \AxiomC{$A\land B$} \UnaryInfC{$B$} \end{prooftree} $$

or the pair

$$ \begin{prooftree} \AxiomC{$A \land B$} \UnaryInfC{$A$} \end{prooftree} \hspace{1.5em} \begin{prooftree} \AxiomC{$A\land B$} \AxiomC{$A$} \BinaryInfC{$B$} \end{prooftree} $$

as the elimination rules for conjunction. The second pair of rules would often be considered to be just a more complicated variant of the pair of projections. However, from an intensional point of view, these two pairs of rules are not identical. Identifying them corresponds to identifying $A \land B$ and $A \land (A \rightarrow B)$, which is only extensionally, but not intensionally correct. As Došen has frequently argued (e.g., Došen 1997; 2006)[^došen-1997], formulas such as $A \land B$ and $A \land(A \rightarrow B)$ are equivalent, but not isomorphic. Here “isomorphic” means that when proving one formula from the other and vice versa, we obtain, by combining these two proofs, the identity proof. This is not the case in this example.

Pursuing this idea leads to principles of harmony and inversion which are different from the standard ones. As harmony and inversion lie at the heart of proof-theoretic semantics, many of its issues are touched. Taking the topic of intensionality seriously means reshaping many fields of proof-theoretic semantics (see Schroeder-Heister, 2022)[^schroeder-heister-2022]. This has repercussions in various neighbouring fields such as the treatment of paradoxes. The first monograph on intensional proof-theoretic semantics, with particular emphasis on the topic of paradoxes, has been written by Tranchini (2023).

Since the identity of proofs is a basic topic of categorial proof theory (see section 2.5), the latter will require more attention in proof-theoretic semantics than is currently the case.

### 3.8. Paradoxes

The logical, mathematical and semantical paradoxes, which play a crucial role in logic and the philosophy of mathematics, receive a novel rendering in the framework of proof-theoretic semantics. If one formulates paradoxes in the context of introduction and elimination rules, one can apply to them the proof-theoretic machinery of proof-reduction. Suppose introduction and elimination rules for set terms are given as follows (in a kind of naive set theory):

$$ \begin{prooftree} \AxiomC{$A(t)$} \UnaryInfC{$t \in \{x:A(x)\}$} \end{prooftree} \hspace{1.5em} \begin{prooftree} \AxiomC{$t \in \{x:A(x)\}$} \UnaryInfC{$A(t)$} \end{prooftree} $$

Then, for r as $\{x: x \not\in x\}$, we can infer $r \in r$ from $r \not\in r$ and vice versa, which is a natural deduction variant of Russell’s paradox. Now Prawitz (1965, Appendix B) observed that the derivation of absurdity arising from Russell’s paradox is non-normalizable, a feature that Tennant (1982) was able to demonstrate for a vast range of paradoxes. From the standpoint of proof-theoretic semantics, a non-normalizable proof may well be considered invalid, at least not valid in the sense in which a normalizable proof is valid. This means that we obtain a proof-theoretic criterion to tell whether we have a meaningful proof or not, and proofs of the paradoxes would not be meaningful in this sense. The Prawitz-Tennant analysis of paradoxes has opened up the field of the proof-theory of paradoxes, which goes way beyond proof-theoretic semantics in the narrower sense. It is closely related to the aspect of intensionality (see section 3.7) and also to the idea of definitional reflection (see section 2.3.2 and the [Supplement on Definitional Reflection and Paradoxes](proof-theoretic-semantics.definitional-reflection.md)).

A particularly interesting paradox from the point of view of proof-theoretic semantics is Ekman’s paradox. It results from codifying an implicational variant of Russell’s paradox in minimal propositional logic. It turns out that, depending on how reductions of detour derivations are formulated, certain derivations in minimal propositional logic are not normalizable. This sheds a strong light on the concept of proof reduction, which is absolutely essential in natural-deduction style proof-theoretic semantics: much depends on its careful definition. In fact, the concept of proof reduction constitutes the concept of proof identity and goes way beyond the extensional idea that “detours” in proofs are removed.

*Further Reading*

For *Russell’s paradox in general* see the entry on Russell’s paradox.

For the treatment of *paradoxes in proof-theoretic semantics*, including Ekman’s paradox see Tranchini (2023).

### 3.9 Reduction, game theory and dialogues

While deduction is forward-directed, passing from sentences already established to further sentences by means of justified rules, reduction proceeds backwards, trying to find an argument for a given claim. It thus belongs to proof search. Various methods of proof search have been discovered and discussed in computer science: resolution and tableau systems are prominent examples. However, from a semantical perspective, reductive approaches are not conceptually secondary to deduction but are theories in their own right. One might even suggest that reductive methods are primary from the semantical point of view, as the search for an argument, or the possible ways of searching for it, constitute the meaning of a given claim. This idea has been adopted, for example, in dialogical or game-theoretical semantics, but can and should be incorporated in proof-theoretic semantics in general. This is a major desideratum of proof-theoretic semantics, which so far is predominantly based on deduction rather than reduction.

*Further Reading*

For the idea of *reductive logic* and its semantics see the monograph by David Pym and Eike Ritter (2004).

For *dialogical logic* see the entry on dialogical logic as well as Thomas Piecha’s entry on [dialogical logic](https://iep.utm.edu/dial-log/) the *Internet Encyclopedia of Philosophy*.

For game-theoretical approaches in logic see the entry on logic and games.

### 3.10 Substructural approaches

As soon as one treats proof-theoretic semantics in the framework of the sequent calculus and thus focuses on hypothetical rather than categorical claims, the area of logics with restricted structural rules, called “substructural logics”, demands semantical consideration. Here the way assumptions are introduced and kept in one’s discourse represents a much more fine-grained structure than assumptions in natural deduction, where they are normally considered to be sets of statements. Due to the possibility of structuring the succedent of a sequent in an analogous way, proof-theoretic semantics looses its intuitionistic bias without necessarily becoming classical. Within the framework of substructural logic, deviant logical systems such as relevant logic or resource-sensitive logics can easily be modelled. A particularly interesting topic is the logic of bunched implications, which distinguishes different, but co-existing ways of structuring assumptions and conclusions (see Pym, 2002)[^pym-2002]. Substructural logic is well-established as a general tool to *describe* logical systems within a single emcompassing structural framework. Whether substructural logic *eo ipso* represents a semantical framework, is still an open question.

*Further Reading*

For *substructural logic* in general see the entry on substructural logics.

## 4. Conclusion and outlook

Standard proof-theoretic semantics has practically exclusively been occupied with logical constants. Logical constants play a central role in reasoning and inference, but are definitely not the exclusive, and perhaps not even the most typical sort of entities that can be defined inferentially. A framework is needed that deals with inferential definitions in a wider sense and covers both logical and extra-logical inferential definitions alike. The idea of definitional reflection with respect to arbitrary definitional rules (see section 2.3.2) and also natural language applications (see secton 3.4) point in this direction, but farther reaching conceptions can be imagined. Furthermore, the concentration on harmony, inversion principles, definitional reflection and the like is somewhat misleading, as it might suggest that proof-theoretic semantics consists of only that. It should be emphasized that already when it comes to arithmetic, stronger principles are needed in addition to inversion. However, in spite of these limitations, proof-theoretic semantics has already gained very substantial achievements that can compete with more widespread approaches to semantics.

*Further Reading*

For contributions on a variety of aspects of proof-theoretic semantics see the reader edited by Piecha and Wehmeier (2024, open access).

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=proof-theoretic-semantics). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/proof-theoretic-semantics/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=proof-theoretic-semantics&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/proof-theoretic-semantics/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

- Gheorghiu, Alexander V., and David Pym (2022), “[Proof-Theoretic Semantics and Tactical Proof](http://www0.cs.ucl.ac.uk/staff/D.Pym/Proof_theoretic_Semantics_and_Tactical_Proof.pdf),” online manuscript, [arXiv:2301.02302](https://arxiv.org/abs/2301.02302)
- [“Natural Deduction”](https://iep.utm.edu/nat-ded/), *The Internet Encyclopedia of Philosophy*, entry by Andrzej Indrzejczak
- [“Dialogical Logic”](https://iep.utm.edu/dial-log/), *The Internet Encyclopedia of Philosophy*, entry by Thomas Piecha
- Pym, David, Eike Ritter, and Edmund Robinson (2023). “[Categorical Proof-theoretic Semantics](https://doi.org/10.48550/arXiv.2302.09031),” manuscript (submitted), [arXiv:2302.09031](https://arxiv.org/abs/2302.09031) [math.LO].
- Stafford, Will (2023). “Prawitz’s Conjecture is False; So What?” manuscript (submitted), [arXiv:2305.09310](https://arxiv.org/abs/2305.09310) [math.LO].

## Related Entries

category theory | connectives: sentence connectives in formal logic | contradiction | Curry’s paradox | Hilbert, David: program in the foundations of mathematics | logic, history of: intuitionistic logic | logic: and games | logic: classical | logic: connexive | logic: dialogical | logic: intuitionistic | logic: linear | logic: substructural | logical constants | logical pluralism | mathematics, philosophy of: intuitionism | mathematics, philosophy of: structuralism | natural deduction systems in logic | negation | paradoxes: and contemporary logic | proof theory: development of | realism: challenges to metaphysical | Russell’s paradox | self-reference | truth: revision theory of | type theory | type theory: intuitionistic

### Acknowledgments

I would like to thank the editors, especially Ed Zalta, and the anonymous reviewers for many helpful comments and suggestions.

[^aczel-1977]: Aczel, Peter (1977). “An Introduction to Inductive Definitions”, in *Handbook of Mathematical Logic*, John Barwise (ed.), Amsterdam: North-Holland, pp. 739–782.

[^ayhan-2021]: Ayhan, Sara (2021). “What is the Meaning of Proofs? A Fregean Distinction in Proof-Theoretic Semantics”, *Journal of Philosophical Logic*, 50: 571–591. doi:10.1007/s10992-020-09577-2.

[^ayhan-2023]: Ayhan, Sara, ed. (2023). *Bilateralism and Proof-Theoretic Semantics*, Special Issue of *Bulletin of the Section of Logic*: 52.

[^beall-2006]: Beall, J.C. and Greg Restall (2006). *Logical Pluralism*, Oxford: Oxford University Press.

[^belnap-1982]: Belnap, Nuel D. (1982). “Display Logic”, *Journal of Philosophical Logic*, 11: 375–417. doi:10.1007/BF00284976

[^binder-2022]: Binder, David, Thomas Piecha, and Peter Schroeder-Heister, eds. (2022). *The Logical Writings of Karl Popper*, Berlin: Springer. doi:10.1007/978-3-030-94926-6

[^binder-2022-2]: Binder, David, Thomas Piecha, and Peter Schroeder-Heister (2022). “Popper’s theory of deductive logic”, *The Logical Writings of Karl Popper*, David Binder et al., eds., Berlin: Springer, 1–79. doi:10.1007/978-3-030-94926-6_1

[^brandom-1994]: Brandom, Robert B. (1994). *Making It Explicit: Reasoning, Representing, and Discursive Commitment*, Cambridge, MA: Harvard University Press.

[^brandom-2000]: ––– (2000). *Articulating Reasons: An Introduction to Inferentialism*, Cambridge, MA: Harvard University Press.

[^carrara-2017]: Carrara, Massimiliano, Daniele Chiffi and Ciro De Florio, eds. (2017). *Logical Investigations on Assertion and Denial*, Special Issue of *Journal of Applied Logic*, 25, Supplement: S1–S122. doi:10.1016/j.jal.2017.11.003

[^campos-2009]: de Campos Sanz, Wagner and Thomas Piecha (2009). “Inversion by Definitional Reflection and the Admissibility of Logical Rules”, *Review of Symbolic Logic*, 2: 550–569. doi:10.1017/S1755020309990165

[^groote-1995]: de Groote, Philippe, ed. (1995). *The Curry-Howard Isomorphism*, Volume 8 of *Cahiers du Centre de Logique*, Academia-Bruyland.

[^došen-1980]: Došen, Kosta (1980). *Logical Constants: An Essay in Proof Theory*, D. Phil. Thesis, Oxford University.

[^došen-1989]: ––– (1989). “Logical Constants as Punctuation Marks”, *Notre Dame Journal of Formal Logic*, 30: 362–381. doi:10.1305/ndjfl/1093635154

[^došen-1997]: ––– (1997). “Logical Consequence: A Turn in Style”, in: Dalla Chiara,M.L., K. Doets, D. Mundici, J. van Benthem (eds.), *Logic and Scientific Methods: Volume One of the Tenth International Congress of Logic, Methodology and Philosophy of Science, Florence, August 1995*, Dordrecht: Kluwer, 289–311.

[^došen-2000]: ––– (2000). *Cut Elimination in Categories*, Berlin: Springer.

[^došen-2003]: ––– (2003). “Identity of proofs based on normalization and generality”, *Bulletin of Symbolic Logic*, 9: 477–503. doi:10.2178/bsl/1067620091

[^došen-2006]: ––– (2006). “Models of deduction”, in: Kahle and Schroeder-Heister, eds. (2006), pp. 639–657. doi:10.1007/s11229-004-6290-7

[^došen-2016]: ––– (2016). “On the paths of categories”, in: Piecha and Schroeder-Heister, eds. (2016b), pp. 65–77. doi:10.1007/978-3-319-22686-6_4

[^došen-2004]: ––– and Zoran Petrić (2004). *Proof-Theoretical Coherence*, London: College Publications.

[^drobyshevich-2021]: Drobyshevich, Sergey (2021). “Tarskian Consequence Relations Bilaterally: Some Familiar Notions”. *Synthese*, 198 (Suppl 22): S5213-S5240. doi:10.1007/s11229-019-02267-w.

[^dummett-1973]: Dummett, Michael (1973). *Frege: Philosophy of Language*, London: Duckworth.

[^dummett-1975]: ––– (1975). “The Philosophical Basis of Intuitionistic Logic”, in: H.E. Rose and J.C. Shepherdson (eds.), *Proceedings of the Logic Colloquium ’73*, *Studies in Logic and the Foundations of Mathematics*, 80: 5–40. doi:10.1016/S0049-237X(08)71941-4

[^dummett-1991]: ––– (1991). *The Logical Basis of Metaphysics*, London: Duckworth.

[^francez-2015]: Francez, Nissim (2015). *Proof-theoretic Semantics*, London: College Publications.

[^francez-2022]: ––– (2022). “Proof-Theoretic Semantics as a Resource for Expressing Semantic Variability”, *Synthese* 200, article 294. doi:10.1007/s11229-022-03780-1

[^francez-2015-2]: ––– and Gilad Ben-Avi (2015). “A proof-theoretic reconstruction of generalized quantifiers”, *Journal of Semantics*, 32: 313–371. doi:10.1093/jos/ffu001

[^francez-2010]: ––– and Roy Dyckhoff (2010). “Proof-theoretic Semantics for a Natural Language Fragment”, *Linguistics and Philosophy*, 33: 447–477. doi:10.1007/s10988-011-9088-3

[^francez-2010-2]: –––, Roy Dyckhoff, and Gilad Ben-Avi (2010). “Proof-Theoretic Semantics for Subsentential Phrases”, *Studia Logica*, 94: 381–401. doi:10.1007/s11225-010-9241-y

[^gentzen-1934]: Gentzen, Gerhard (1934/35). “Untersuchungen über das logische Schließen”, *Mathematische Zeitschrift*, 39: 176–210, 405–431; English translation in *The Collected Papers of Gerhard Gentzen*, M. E. Szabo (ed.), Amsterdam: North Holland, 1969, pp. 68–131. doi:10.1007/BF01201353

[^girard-1987]: Girard, Jean-Yves (1987). “Linear Logic”, *Theoretical Computer Science*, 50: 1–102. doi:10.1016/0304-3975(87)90045-4

[^goldfarb-2016]: Goldfarb, Warren (2016). “On Dummett’s proof-theoretic justifications of logical laws´”, *Advances in Proof-theoretic Semantics*, Thomas Piecha and Peter Schroeder-Heister, eds., Berlin: Springer, pp. 195–210. doi:10.1007/978-3-319-22686-6_13

[^hacking-1979]: Hacking, Ian (1979). “What is Logic?”, *Journal of Philosophy*, 76: 285–319. doi:10.2307/2025471

[^hallnäs-1991]: Hallnäs, Lars (1991). “Partial Inductive Definitions”, *Theoretical Computer Science*, 87: 115–142. doi:10.1016/S0304-3975(06)80007-1

[^hallnäs-2006]: ––– (2006). “On the proof-theoretic foundation of general definition theory”, *Synthese*, 148: 589–602. doi:10.1007/s11229-004-6291-6

[^hallnäs-1990]: Hallnäs, Lars and Peter Schroeder-Heister (1990/91). “A proof-theoretic approach to logic programming: I. Clauses as rules. II. Programs as definitions”, *Journal of Logic and Computation*, 1: 261–283, 635–660. doi:10.1093/logcom/1.2.261 , doi:10.1093/logcom/1.5.635

[^harper-1987]: Harper, Robert, Furio Honsell, and Gordon Plotkin (1987). “A Framework for Defining Logics”, *Journal of the Association for Computing Machinery*, 40: 194–204. doi:10.1145/138027.138060

[^jaśkowski-1934]: Jaśkowski, Stanisław (1934). “On the Rules of Suppositions in Formal Logic”, *Studia Logica*, 1: 5–32 (reprinted in S. McCall (ed.), *Polish Logic 1920–1939*, Oxford 1967, pp. 232–258.

[^jäger-1998]: Jäger, Gerhard and Robert F. Stärk (1998). “A Proof-Theoretic Framework for Logic Programming”, *Handbook of Proof Theory*, Samuel R. Buss (ed.), Amsterdam: Elsevier, pp. 639–682.

[^kahle-2006]: Kahle, Reinhard and Peter Schroeder-Heister, eds. (2006). *Proof-Theoretic Semantics*, Special issue of *Synthese*, Volume 148. doi:10.1007/s11229-004-6292-5

[^kapsner-2014]: Kapsner, Andreas (2014). *Logics and Falsifications: A New Perspective on Constructivist Semantics*, Berlin: Springer.

[^kneale-1956]: Kneale, William (1956). “The Province of Logic”, *Contemporary British Philosophy*, H. D. Lewis (ed.), London: Allen and Unwin, pp. 237–261.

[^koslow-1992]: Koslow, Arnold (1992). *A Structuralist Theory of Logic*, Cambridge: Cambridge University Press.

[^kreisel-1971]: Kreisel, Georg (1971). “A Survey of Proof Theory II”, *Proceedings of the Second Scandinavian Logic Symposium*, J. E. Renstad (ed.), Amsterdam: North-Holland, pp. 109–170. doi:10.1016/S0049-237X(08)70845-0

[^kreuger-1994]: Kreuger, Per (1994). “Axioms in Definitional Calculi”, *Extensions of Logic Programming*: *Proceedings of the 4th International Workshop, ELP’93, St. Andrews, U.K., March/April 1993* (Lecture Notes in Computer Science, Voluem 798), Roy Dyckhoff (ed.), Berlin: Springer, pp. 196–205. doi:10.1007/3-540-58025-5_57

[^kürbis-2016]: Kürbis, Nils (2016). “Some Comments on Ian Rumfitt’s Bilateralism”, *Journal of Philosophical Logic* 45:623–644. doi:10.1007/s10992-016-9395-9

[^kürbis-2019]: ––– (2019). *Proof and Falisity: A Logical Investigation*, Cambridge University Press.

[^lambek-1986]: Lambek, J. and P.J. Scott (1986). *Introduction to Higher Order Categorical Logic*, Cambridge: Cambridge University Press.

[^liang-2009]: Liang, Chuck and Dale Miller (2009). “Focusing and Polarization in Linear, Intuitionistic, and Classical Logics”. *Theoretical Computer Science*, 410(46): 4747–4768. doi:10.1016/j.tcs.2009.07.041

[^liang-2024]: ––– (2024). “Focusing Gentzen’s LK Proof System”, *Peter Schroeder-Heister on Proof-Theoretic Semantics*, T. Piecha and K. F. Wehmeier, eds. Berlin: Springer, pp. 275-313. doi:10.1007/978-3-031-50981-0_9

[^lorenzen-1955]: Lorenzen, Paul (1955). *Einführung in die operative Logik und Mathematik*, Berlin: Springer; 2nd edition, 1969.

[^mancosu-2021]: Mancosu, Paolo, Sergio Galvan and Richard Zach (2021). *An Introduction to Proof Theory: Normalization, Cut-Elimination, and Consistency Proofs*, Oxford University Press.

[^martin-löf-1971]: Martin-Löf, Per (1971). “Hauptsatz for the intuitionistic theory of iterated inductive definitions”, *Proceedings of the Second Scandinavian Logic Symposium*, J. E. Fenstad (ed.), Amsterdam: North-Holland, pp. 179–216. doi:10.1016/S0049-237X(08)70847-4

[^martin-löf-1984]: ––– (1984). *Intuitionistic Type Theory*, Napoli: Bibliopolis.

[^martin-löf-1995]: ––– (1995). “Verificationism Then and Now”, *The Foundational Debate: Complexity and Constructivity in Mathematics and Physics*, Werner DePauli-Schimanovich, Eckehart Köhler, and Friedrich Stadler (eds.), Dordrecht: Kluwer, pp. 187–196.

[^martin-löf-1998]: ––– (1998). “Truth and Knowability: On the Principles C and K of Michael Dummett”, *Truth in Mathematics*, Harold G. Dales and Gianluigi Oliveri (eds.), Oxford: Clarendon Press, pp. 105–114.

[^martin-löf-2019]: ––– (2019). “Logic and Ethics”. *Proof-Theoretic Semantics: Assessment and Future Perspectives. Proceedings of the Third Tübingen Conference on Proof-Theoretic Semantics, March 2019*, T. Piecha and P. Schroeder-Heister (eds.), University of Tübingen, pp. 227–235 (transcript of lecture). doi:10.15496/publikation-35319

[^negri-2001]: Negri, Sara and Jan von Plato (2001). *Structural Proof Theory*, Cambridge University Press.

[^nelson-1949]: Nelson, David (1949). “Constructible Falsity”, *Journal of Symbolic Logic*, 14: 16–26. doi:10.2307/2268973

[^odintsov-2008]: Odintsov, Sergei P. (2008). *Constructive Negations and Paraconsistency*, Berlin: Springer.

[^parigot-1992]: Parigot, Michel (1992). “$\lambda \mu$-Calculus: An Algorithmic Interpretation of Classical Natural Deduction”. *Logic Programming and Automated Reasoning*, A. Voronkov (ed.), Berlin: Springer, pp. 190–201. doi:10.1007/BFb0013061

[^piccolomini-2023]: Piccolomini d’Aragona, Antonio (2023). *Prawitz*’*s Epistemic Grounding. An Investigation into the Power of Deduction*, Berlin, Springer 2023.

[^piecha-2016]: Piecha, Thomas (2016). “Completeness in Proof-Theoretic Semantics”. In: Piecha and Schroeder-Heister, eds. (2016b), pp. 231–251. doi:10.1007/978-3-319-22686-6_15

[^piecha-2023]: ––– (2023). “Karl Popper on deduction”, Perspectives on Deduction, Antonio Piccolomini d’Aragona (ed.), Berlin: Springer.

[^piecha-2015]: –––, Wagner de Campos Sanz and Peter Schroeder-Heister (2015). “Failure of Completeness in Proof-Theoretic Semantics”, *Journal of Philosophical Logic*, 44: 321–335. doi:10.1007/s10992-014-9322-x

[^piecha-2016a]: ––– and Peter Schroeder-Heister (2016a). “Atomic Systems in Proof-Theoretic Semantics: Two Approaches”, in: Redmond, J., O. P. Martins, Á.N. Fernández *Epistemology, Knowledge and the Impact of Interaction*, Cham: Springer, pp. 47–62. doi:10.1007/978-3-319-26506-3_2

[^piecha-2016b]: ––– and Peter Schroeder-Heister, eds. (2016b). *Advances in Proof-Theoretic Semantics*, Cham: Springer (Open Access). doi:10.1007/978-3-319-22686-6

[^piecha-2019]: ––– and Peter Schroeder-Heister (2019). “Incompleteness of Intuitionistic Propositional Logic with Respect to Proof-Theoretic Semantics”, *Studia Logica*, 107: 233–246. doi:10.1007/s11225-018-9823-7

[^piecha-2024]: ––– and Kai Wehmeier, eds. (2024). *Peter Schroeder-Heister on Proof-Theoretic Semantics*, Berlin: Springer. doi:10.1007/978-3-031-50981-0

[^pimentel-2019]: Pimentel, Elaine, Luiz Carlos Pereira, and Valeria de Paiva (2019). “An Ecumenical Notion of Entailment”, *Synthese* 198 (S22): 5391–5413. doi:10.1007/s11229-019-02226-5

[^popper-1947a]: Popper, Karl Raimund (1947a). “Logic without Assumptions”, *Proceedings of the Aristotelian Society*, 47: 251–292. Reprinted in Binder et al., eds. (2022). doi:10.1007/978-3-030-94926-6_2

[^popper-1947b]: ––– (1947b). “New Foundations for Logic”, *Mind*, 56: 193–235; corrections, *Mind*, 57: 69–70. Reprinted in Binder et al., eds (2022). doi:10.1007/978-3-030-94926-6_3

[^prawitz-1965]: Prawitz, Dag (1965). *Natural Deduction: A Proof-Theoretical Study*, Stockholm: Almqvist & Wiksell; reprinted Mineola, NY: Dover Publications, 2006.

[^prawitz-1971]: ––– (1971). “Ideas and Results in Proof Theory”, *Proceedings of the Second Scandinavian Logic Symposium* (Oslo 1970), Jens E. Fenstad (ed.), Amsterdam: North-Holland, pp. 235–308. doi:10.1016/S0049-237X(08)70849-8

[^prawitz-1972]: ––– (1972). “The Philosophical Position of Proof Theory”, *Contemporary Philosophy in Scandinavia*, R. E. Olson and A. M. Paul (eds.), Baltimore, London: John Hopkins Press, pp. 123–134.

[^prawitz-1973]: ––– (1973). “Towards a Foundation of a General Proof Theory”, *Logic, Methodology and Philosophy of Science IV*, Patrick Suppes, et al. (eds.), Amsterdam: North-Holland, pp. 225–250.

[^prawitz-1974]: ––– (1974). “On the Idea of a General Proof Theory”, *Synthese*, 27: 63–77. doi:10.1007/BF00660889

[^prawitz-1985]: ––– (1985). “Remarks on some Approaches to the Concept of Logical Consequence”, *Synthese*, 62: 152–171. doi:10.1007/BF00486044

[^prawitz-2006]: ––– (2006). “Meaning Approached via Proofs”, *Synthese*, 148: 507–524. doi:10.1007/s11229-004-6295-2

[^prawitz-2007]: ––– (2007). “Pragmatist and Verificationist Theories of Meaning”, *The Philosophy of Michael Dummett*, Randall E. Auxier and Lewis Edwin Hahn (eds.), La Salle: Open Court, pp. 455–481.

[^prawitz-2013]: ––– (2013). “An Approach to General Proof Theory and a Conjecture of a Kind of Completeness of Intuitionistic Logic Revisited”, *Advances in Natural Deduction*, Edward Hermann Haeusler, Luiz Carlos Pereira, and Valeria de Paiva (eds.), Berlin: Springer. doi:10.1007/978-94-007-7548-0_12

[^prawitz-2015]: ––– (2015). “Explaining deductive inference”, *Dag Prawitz on Proofs and Meaning* , H. Wansing (ed.), Berlin: Springer, pp. 65–100. doi:10.1007/978-3-319-11041-7_3

[^prawitz-2024]: ––– (2024). “The validity of inference and argument”, *Peter Schroeder-Heister on Proof-Theoretic Semantics*, Thomas Piecha and Kai F. Wehmeier. (eds.) Berlin: Springer, pp 135-160. doi:10.1007/978-3-031-50981-0_4

[^pym-2002]: Pym, David (2002). *The Semantics and Proof Theory of the Logic of Bunched Implications*, Dordrecht: Kluwer.

[^pym-2004]: ––– and Eike Ritter (2004). *Reductive Logic and Proof Search: Proof Theory, Semantics, and Control*, Oxford: Clarendon Press.

[^read-2010]: Read, Stephen (2010). “General-Elimination Harmony and the Meaning of the Logical Constants”, *Journal of Philosophical Logic*, 39: 557–576. doi:10.1007/s10992-010-9133-7

[^rumfitt-2000]: Rumfitt, Ian (2000). “‘Yes’ and ‘No’”, *Mind* 109: 781–823. doi:10.1093/mind/109.436.781

[^sambin-2000]: Sambin, Giovanni, Giulia Battilotti, and Claudia Faggian (2000). “Basic Logic: Reflection, Symmetry, Visibility”, *Journal of Symbolic Logic*, 65: 979–1013. doi:10.2307/2586685

[^sandqvist-2009]: Sandqvist, Tor (2009). “Classical Logic without Bivalence”, *Analysis*, 69: 211–218. doi:10.1093/analys/anp003

[^sandqvist-2015a]: ––– (2015a). “Base-extension semantics for intuitionistic sentential logic”, *Logic Journal of the IGPL*, 23: 719–731. doi:10.1093/jigpal/jzv021

[^sandqvist-2015b]: ––– (2015b). “Hypothesis-discharging rules in atomic bases”, *Dag Prawitz on Proofs and Meaning* , H. Wansing (ed.), Berlin: Springer, pp. 313–328. doi:10.1007/978-3-319-11041-7_14

[^schroeder-heister-1984]: Schroeder-Heister, Peter (1984). “A natural extension of natural deduction”, *Journal of Symbolic Logic*, 49: 1284–1300. doi:10.2307/2274279

[^schroeder-heister-1991]: ––– (1991). “Uniform Proof-Theoretic Semantics for Logical Constants (Abstract)”, *Journal of Symbolic Logic*, 56: 1142. doi:10.2307/2275092

[^schroeder-heister-1993]: ––– (1993). “Rules of Definitional Reflection”, *Proceedings of the 8th Annual IEEE Symposium on Logic in Computer Science*, Los Alamitos: IEEE Press, pp. 222–232. doi:10.1109/LICS.1993.287585

[^schroeder-heister-2006]: ––– (2006). “Validity Concepts in Proof-Theoretic Semantics”, *Synthese*, 148: 525–571. doi:10.1007/s11229-004-6296-1

[^schroeder-heister-2007]: ––– (2007). “Generalized Definitional Reflection and the Inversion Principle”, *Logica Universalis*, 1: 355–376. doi:10.1007/s11787-007-0018-7

[^schroeder-heister-2012a]: ––– (2012a). “Definitional Reasoning in Proof-Theoretic Semantics and the Square of Opposition”, *The Square of Opposition: A General Framework for Cognition*, Jean-Yves Béziau and Gillman Payette (eds.), Bern: Peter Lang, pp. 323–349. doi:10.15496/publikation-72333

[^schroeder-heister-2012c]: ––– (2012c). “The Categorical and the Hypothetical: A Critique of some Fundamental Assumptions of Standard Semantics”. In: *Synthese* 187, pp. 925–942. doi:10.1007/s11229-011-9910-z

[^schroeder-heister-2013]: ––– (2013). “Definitional Reflection and Basic Logic”, *Annals of Pure and Applied Logic*, 164(4): 491–501. doi:10.1016/j.apal.2012.10.010

[^schroeder-heister-2015]: ––– (2015). “Proof-theoretic validity based on elimination rules”. In: Haeusler, Edward Hermann, Wagner de Campos Sanz and Bruno Lopes, eds., *Why is this a Proof? Festschrift for Luiz Carlos Pereira*, London: College Publications, pp. 159–176. doi:10.15496/publikation-70825

[^schroeder-heister-2016]: ––– (2016). “Open Problems in Proof-Theoretic Semantics”. In: Piecha and Schroeder-Heister, eds. (2016b), pp. 253–283. doi:10.1007/978-3-319-22686-6_16

[^schroeder-heister-2022]: ––– (2022). “Axiomatic thinking, identity of proofs and the quest for an intensional proof-theoretic semantics”. In: F. Ferreira, R. Kahle and G. Sommaruga (eds.), *Axiomatic Thinking I*, Berlin: Springer, pp. 145–165. doi:10.1007/978-3-030-77657-2_8

[^shoesmith-1978]: Shoesmith, D. J. and Timothy J. Smiley (1978). *Multiple-Conclusion Logic*, Cambridge: Cambridge University Press.

[^sommaruga-2000]: Sommaruga, Giovanni (2000). *History and Philosophy of Constructive Type Theory*, Dordrecht: Kluwer.

[^sørensen-2006]: Sørensen, Morten Heine B. and Pawel Urzyczyn (2006). *Lectures on the Curry-Howard Isomorphism*, Amsterdam: Elsevier.

[^stafford-2023]: Stafford, Will and Victor Nascimento (2023). “Following all the rules: intuitionistic completeness for generalised proof-theoretic validity”, *Analysis*. doi:10.1093/analys/anac100

[^tait-1967]: Tait, W. W: (1967). “Intensional Interpretations of Functionals of Finite Type I”, *Journal of Symbolic Logic*, 32: 198–212. doi:10.2307/2271658

[^tennant-1978]: Tennant, Neil (1978). *Natural Logic*, Edinburgh: Edinburgh University Press.

[^tennant-1982]: ––– (1982). “Proof and Paradox”, *Dialectica*, 36: 265–296. doi:10.1111/j.1746-8361.1982.tb00820.x

[^tennant-1987]: ––– (1987). *Anti-Realism and Logic: Truth as Eternal*, Oxford: Clarendon Press.

[^tennant-1997]: ––– (1997). *The Taming of the True*, Oxford: Clarendon Press.

[^tennant-2017]: ––– (2017). *Core Logic*, Oxford University Press.

[^univalent-2013]: The Univalent Foundations Program (2013). *Homotopy Type Theory: Univalent Foundations of Mathematics*, Princeton: Institute for Advanced Study.

[^tranchini-2010]: Tranchini, Luca (2010). *Proof and Truth: An Anti-Realist Perspective*, Milano: Edizioni ETS, 2013; reprint of Ph.D. dissertation, Department of Philosophy, University of Tuebingen, 2010, [available online](http://nbn-resolving.de/urn:nbn:de:bsz:21-opus-54715).

[^tranchini-2012a]: ––– (2012a). “Truth from a Proof-Theoretic Perspective”. In: *Topoi* 31, pp. 47–57. doi:10.1007/s11245-012-9121-3

[^tranchini-2012b]: ––– (2012b). “Natural Deduction for Dual Intuitionistic Logic”, *Studia Logica*, 100: 631–648. doi:10.1007/s11225-012-9417-8

[^tranchini-2016]: ––– (2016). “Proof-Theoretic Semantics, Paradoxes, and the Distinction between Sense and Denotation”, *Journal of Logic and Computation*, 26, pp. 495–512. doi:10.1093/logcom/exu028

[^tranchini-2023]: ––– (2023). *Harmony and Paradox: Intensional Aspects of Proof-Theoretic Semantics*, Berlin: Springer.

[^troelstra-1988]: Troelstra, Anne S. and Dirk van Dalen (1988). *Constructivism in Mathematics: An Introduction*, Amsterdam: North-Holland.

[^troelstra-2000]: Troelstra, A. S. and H. Schwichtenberg (2000). *Basic Proof Theory*, Cambridge University Press (second edition 2012).

[^kutschera-1968]: von Kutschera, Franz (1968). “Die Vollständigkeit des Operatorensystems $\{\neg , \land , \lor , \supset \}$ für die intuitionistische Aussagenlogik im Rahmen der Gentzensemantik”, *Archiv für mathematische Logik und Grundlagenforschung*, 11: 3–16. doi:10.1007/BF01973339

[^kutschera-1969]: ––– (1969). “Ein verallgemeinerter Widerlegungsbegrifff für Gentzenkalküle”, *Archiv für mathematische Logik und Grundlagenforschung*, 12: 104–118. doi:10.1007/BF01969697

[^wansing-1993a]: Wansing, Heinrich (1993a). “Functional Completeness for Subsystems of Intuitionistic Propositional Logic”, *Journal of Philosophical Logic*, 22: 303–321. doi:10.1007/BF01049305

[^wansing-1993b]: ––– (1993b). *The Logic of Information Structures* (Lecture Notes in Artificial Intelligence, Volume 681), Berlin: Springer Springer.

[^wansing-2000]: ––– (2000). “The Idea of a Proof-Theoretic Semantics and the Meaning of the Logical Operations”, *Studia Logica*, 64: 3–20. doi:10.1023/A:1005217827758

[^wansing-2001]: ––– (2001). “Negation”, *The Blackwell Guide to Philosophical Logic*, L. Goble (ed.), Cambridge, MA: Blackwell, pp. 415–436.

[^wansing-2017]: ––– (2017). “A More General General Proof Theoy”, *Journal of Applied Logic*, 25: 23–46. doi:10.1016/j.jal.2017.01.002.

[^więckowski-2008]: Więckowski, Bartosz (2008). “Predication in Fiction”, in *The Logica Yearbook 2007*, M. Peliš (ed.), Prague: Filosofia, pp. 267–285.

[^więckowski-2011]: ––– (2011). “Rules for Subatomic Derivation”, *Review of Symbolic Logic*, 4: 219–236. doi:10.1017/S175502031000033X

[^więckowski-2016]: ––– (2016). “Subatomic Natural Deduction for a Naturalistic First-Order Language with Non-Primitive Identity”, *Journal of Logic, Language and Information*, 25: 215–268. doi:10.1007/s10849-016-9238-7

[^więckowski-2021]: ––– (2021). “Subatomic Negation”, *Journal of Logic, Language and Information*, 30: 207–262. doi:10.1007/s10849-020-09325-4

[^zeilberger-2008]: Zeilberger, Noam (2008). “On the Unity of Duality”, *Annals of Pure and Applied Logic*, 153: 66–96. doi:10.1016/j.apal.2008.01.001
