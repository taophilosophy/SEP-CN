# Connexive Logic
**First published Fri Jan 6, 2006; substantive revision Thu Jun 1, 2023**

*Wansing, Heinrich*

Many prominent systems of non-classical logic are subsystems of what is generally called ‘classical logic.’ Systems of connexive logic are *contra-classical* in the sense that they are neither subsystems nor extensions of classical logic. Connexive logics have a standard logical vocabulary and comprise certain non-theorems of classical logic as theses. Since classical propositional logic is Post-complete, any additional axiom in its language gives rise to the trivial system, so that any non-trivial system of connexive logic will have to leave out some theorems of classical logic. The name ‘connexive logic’ was introduced by Storrs McCall (1963, 1964) and suggests that systems of connexive logic are motivated by some ideas about coherence or connection between the premises and the conclusions of valid inferences or between the antecedent and the succedent (consequent) of valid implications. The kind of coherence in question concerns the meaning of implication and negation (see the entries on indicative conditionals, the logic of conditionals, counterfactuals, and negation). One basic idea is that no formula provably implies or is implied by its own negation. This conception may be expressed by requiring that for every formula *A*,

> ⊬ ~*A* → *A* and ⊬ *A* → ~ *A*,

but usually the underlying intuitions are expressed by requiring that certain schematic formulas are theorems:

> AT: ~(~*A* → *A*) and
> AT′: ~(*A* → ~*A*).

The first formula is often called *Aristotle’s Thesis*. If this non-theorem of classical logic is found plausible, then the second principle, AT′, would seem to enjoy the same degree of plausibility. Indeed, also AT′ is sometimes referred to as Aristotle’s Thesis, for example in Routley 1978, Mortensen 1984, Routley and Routley 1985, and Ferguson 2016. As McCall (1975, p. 435) explains,

> [c]onnexive logic may be seen as an attempt to formalize the species of implication recommended by Chrysippus:
>
> > And those who introduce the notion of connection say that a conditional is sound when the contradictory of its consequent is incompatible with its antecedent. (Sextus Empiricus, translated in Kneale and Kneale 1962, p. 129.)[^kneale-1962]

Using intuitionistically acceptable means only, the pair of theses AT and AT′ is equivalent in deductive power with another pair of schemata, which in established terminology are called *(Strong) Boethius’ Theses* (cf. Routley 1978)[^routley-1978] and which may be viewed, in addition with their converses, as capturing Chrysippus’ idea:

> BT: (*A* → *B*) → ~(*A* → ~*B*) and
> BT′: (*A* → ~*B*) → ~(*A* → *B*).

The names ‘Aristotle’s Theses’ and ‘Boethius’ Theses’ are, of course, not arbitrarily chosen. As to AT, it is argued in Aristotle’s *Prior Analytics* 57b14 that it is impossible that if not-*A*, then *A*, see Łukasiewicz 1957, p. 50. Note, however, that Łukasiewicz and Kneale (1957, p. 66) maintain that Aristotle is making a mistake here. Moreover, Boethius has been said to hold in *De Syllogismo Hypothetico* 843D that ‘if *A* then not-*B*’ is the negation of ‘if *A*, then *B*’, (“he said that the negative of *Si est A, est B* was *Si est A, non est B,*” Kneale and Kneale 1962, p. 191)[^kneale-1962]. If we look at *De Syllogismo Hypothetico* 843C-D, we find:

> Sunt autem hypotheticae propositiones, aliae quidem affirmativae, aliae negativae […] affirmativa quidem, ut cum dicimus, si est *a*, est *b*; si non est *a*, est *b*; negativa, si est *a*, non est *b*, si non est *a*, non est *b*. Ad consequentem enim propositionem respiciendum est, ut an affirmativa an negativa sit propositio judicetur. (Note that there is a misprint in Migne’s edition from 1860, where instead of the first occurrence of “si non est *a*, est *b*” in the above quote there is “si non est *a*, non est *b*”.)

Boethius here draws a distinction between affirmative and negative conditionals and explains that negative conditionals have the form ‘if *a*, then not *b*’ and ‘if not *a*, then not *b*.’ This statement is quite different from the reading offered by Kneale and Kneale. Note that AT follows from BT′ and AT′ follows from BT in logics in which *A* → *A* is theorem and modus ponens is an admissible inference rule.

Let *L* be a language containing a unary connective ~ (negation) and a binary connective → (implication). A logical system in a language extending *L* is called a *connexive logic* if AT, AT′, BT, and BT′ are theorems and, moreover, implication is non-symmetric, i.e., (*A* → *B*) → (*B* → *A*) fails to be a theorem (so that → can hardly be understood as a bi-conditional). This is the now standard notion of connexive logic. The connective → in a system of connexive logic is said to be a *connexive implication*.

Systems of connexive logic have been motivated and arrived at by different considerations. One motivation comes from relevance logic and the idea that semantic consequence is a content relationship, see section 3.1. Moreover, principles of connexive logic have been discussed in conditional logic, see section 3.2 and the entries on indicative conditionals, the logic of conditionals, and counterfactuals, in different accounts of negation, see section 3.3 and the entry on negation, and in approaches to contra-classical logics, see section 3.4. Another motivation emerges from empirical research on the interpretation of negated conditionals in natural language and the aim to adequately model the semantical intuitions revealed by these investigations, see section 3.5.

Richard Angell in his seminal paper on connexive logic (1962) aimed at developing a logic of subjunctive, counterfactual conditionals in which what he called a ‘principle of subjunctive contrariety,’ ∼((*A* → *B*) ∧ (*A* → ~*B*)), is provable. His proof system, **PA1**, contains BT as an axiom. Also Kapsner and Omori (2017) suggest that a connexive implication is suitable for formalizing counterfactual conditionals, whereas Cantwell (2008), for example, suggested a system of connexive logic to formalize indicative natural language conditionals. According to McCall (1975, p. 451), “[o]ne of the most natural interpretations of connexive implication is as a species of physical or ‘causal’ implication,” and in McCall (2014) he argues that “[t]he logic of causal and subjunctive conditionals is … connexive, since ‘If X is dropped, it will hit the floor’ contradicts ‘If X is dropped, it will not hit the floor’.” Boethius’ Thesis BT indeed appears on a list of principles every “precausal” connective should satisfy, see Urchs 1994. McCall (2012, p. 437), however, concedes that “causal logic is still very much an ongoing project, and no agreed-on formulation of it has yet been achieved.” Moreover, the characteristic connexive principles are valid for the analysis of conditionals, generics, and disposition statements presented in van Rooij and Schulz 2019, 2020.

Further motivation for systems of connexive logic comes from more instrumental studies. In McCall 1967, connexive implication is motivated by reproducing in a first-order language all valid moods of Aristotle’s syllogistic (see the entry on Aristotle’s logic). In particular, the classically invalid inference from ‘All *A* is *B*’ to ‘Some *A* is *B*’ is obtained by translating ‘Some *A* is *B*’ as ∃*x*(~(*A*(*x*) → ~*B*(*x*))), where → is a connexive implication. In Wansing 2007, connexive implication is motivated by introducing a negation connective into Categorial Grammar in order to express negative information about membership in syntactic categories (see the entry on typelogical grammar). Consider, for example, the syntactic category (type) (*n* → *s*) of intransitive verbs, i.e., of expressions that in combination with a name (an expression of type *n*) result in a sentence (an expression of type *s*). The idea is that an expression is of type ~(*n* → *s*) iff in combination with a name it results in an expression that is not a sentence. In other words, an expression belongs to type ~(*n* → *s*) iff it is of type (*n* → ~*s*). In the short note Besnard 2011, Aristotle’s thesis AT′ is motivated as expressing a notion of rule consistency for rule-based systems in knowledge representation. A further motivation arises from the problem of modelling conditional obligations in deontic logic. Weiss (2019) suggests to understand a certain implication that validates Aristotle’s theses and weak versions of Boethius’ theses (cf. sections 2 and 3.2) as expressing a conditional obligation operator. Yet another motivation arises from the problem of modelling conditional obligations in deontic logic. Another motivation in terms of applications comes from non-classical mathematics. There is an extended literature on mathematical theories based on non-classical logics, including intuitionistic, fuzzy, relevant, and linear arithmetic and paraconsistent set theory. Early contributions in the context of connexive logic are McCall’s 1967 connexive class theory, and Wiredu’s 1974 paper on connexive set theory. Ferguson (2016, 2019) takes up the challenge of investigating the prospects for a connexive mathematics and explores the feasibility of a connexive arithmetic.

### 1. Diverging and additional notions of connexivity

There are several further and some diverging notions of a connexive logic. In particular, the second decade of the 21st century has (unfortunately) seen the introduction of confusingly many new notions of connexivity and non-uniform terminology. McCall (1966) introduced connexive logics as systems ranging from logics in which no proposition implies or is implied by its own negation to logics in which BT is provable (together with non-symmetry of implication), and, similarly, Mares and Paoli (2019) characterize connexive logics as systems having some or all of AT, AT′, BT, and BT′ among their theorems (without explicitly requiring non-symmetry of implication). In McCall 2012, AT′ and BT are said to be the distinguishing marks of connexive logic, but note that AT and BT′ are valid in the system **CC1** due to Angell (1962) and MacCall (1966) as well. Logics in which some but not all of AT, AT′, BT, and BT′ are provable (or valid) are called ‘demi-connexive’ in Wansing, Omori, and Ferguson 2016 (without explicitly requiring non-symmetry of implication), and are said to be *quasi-connexive* in Jarmużek and Malinowski 2019a. The identification of the negation of (*A* → *B*) with (*A* → ~*B*), ascribed to Boethius by Kneale and Kneale (1962), suggests a strengthening of BT and BT′ to the equivalences:

> BTe: (*A* → *B*) *↔* ~(*A →* ~*B*), and
> BTe′: (*A* → ~*B*) ↔ ~(*A* → *B*).

Sylvan 1989 refers to BTe as a principle of *hyperconnexive* logic. The principles BTe and BTe′ are characteristic of the connexive logics developed subsequent to the definition of the connexive logic **C** and its quantified version **QC** in Wansing 2005. According to McCall (2012), the converse of BT (the right-to-left direction of BTe) is highly unintuitive in light of what he takes to be counterexamples from English. For a rejoinder see Wansing and Skurt 2018.

Kapsner (2012, 2019) refers to a logic that satisfies AT, AT′, BT, and BT′ and, moreover, satisfies the requirements

> Unsat1: In no model, *A* → ~*A* is satisfiable (for any *A*), and in no model, *~A* → *A* is satisfiable (for any *A*), and
> Unsat2: In no model, *A* → *B* and *A* → ~*B* are simultaneously satisfiable (for any *A* and *B*)

as *strongly connexive*, whereas if the conditions Unsat1 and Unsat2 are not both satisfied, the system is only called *weakly connexive*. Kapsner motivates the extra conditions by two intuitions, namely that it is not the case that a formula *A* should imply or be implied by its own negation, and that if *A* implies *B*, then *A* does not imply not-*B* (and if *A* implies not-*B*, then *A* does not imply *B*). These intuitions may, however, also be seen to motivate ⊬ ~*A* → *A* and ⊬ *A* → ~ *A*, respectively (*A* →*B*) ⊬ (*A* → ~*B*) and (*A* → ~*B*) ⊬ (*A* → *B*) instead of Unsat1 and Unsat2. Moreover, imposing Unsat1 and Unsat2 precludes systems that satisfy the variable sharing property (i.e., broadly relevant or *sociative* logics in Routley’s (1989) terminology, for which it holds that if *A* → *B* is a theorem, then *A* and *B* share at least one propositional variable) and satisfy the deduction theorem from being connexive. So far only few strongly connexive logics satisfying the non-symmetry of implication condition are known, namely the system **CC1**, which, however, “is an awkward system in many ways” (McCall 2012, p. 429)[^mccall-2012], see section 4.1, and the Boolean connexive relatedness logics from Jarmużek and Malinowski 2019a, see section 4.4. In Wansing and Unterhuber 2019, logics that validate Boethius’ theses only in rule form ((*A* → *B*) ⊢ ~(*A* → ~*B*) and (*A* → ~*B*) ⊢ ~(*A* → *B*)) are called *weakly connexive*. Weiss (2019) considers a language with classical negation, ¬, classical implication, ⊃, and another binary conditional, →, (notation adjusted). He calls a logic *half-connexive* if it validates the Weak Boethius’ Theses:

> BTw: (*A* → *B*) ⊃ ¬(*A* → ¬*B*), and
> BTw′: (*A* → ¬*B*) ⊃ ¬(*A* → *B*),

and refers to a logic as connexive if in addition it validates AT and AT′ for → and ¬. The Weak Boethius’ Thesis BTw was introduced in Pizzi 1977 as “conditional Boethius’ thesis” for the connexive implication seen as standing for a counterfactual conditional.

In Kapsner 2019, the demand of strong connexivity is evaluated as “too stringent a requirement,” and the notion of *plain humble connexivity* is introduced by restricting Aristotle’s theses, Boethius’ theses, Unsat1, and Unsat2 to satisfiable antecedents. A survey of the terminology and various notions of connexivity used in the literature is presented in the [Supplement on Terminology](logic-connexive.supplement.md). It remains to be seen whether all the notions in addition to the established concept of connexive logic will turn out to be conducive.

If a language is used in which implication is not taken as primitive but is defined in terms of other connectives, connexive logics could also be seen as diverging from the orthodoxy of classical logic by giving a deviant account of those connectives. A definition of a connexive implication in terms of negation, conjunction, and necessity can be found in McCall 1966 and Angell 1967b. More recently, Francez (2020) suggested the notion of “poly-connexivity” to highlight a modification of the familiar falsity conditions of conjunctions and disjunctions (in addition to adopting falsity conditions of implications as expressed by BTe′).

### 2. History of connexive logic

McCall (2012) emphasizes that there is a history of two thousand three hundred years of connexive implication. Historical remarks on connexive logic may be found, for instance, in Kneale and Kneale 1962, Sylvan 1989, Priest 1999, Nasti De Vincentis 2002, Nasti De Vincentis 2004, Nasti De Vincentis 2006, Estrada-González & Ramirez-Cámara 2020, and McCall 2012. In the latter survey, McCall refers to ~((*A* → *B*) ∧ (~*A* → *B*)) as *Aristotle’s Second Thesis* and, following Martin 2004, to Angell’s principle of subjunctive contrariety ~((*A* → *B*) ∧ (*A* → ~*B*)) as *Abelard’s First Principle*, which is called *Strawson’s Thesis* in, for example, Routley 1978 and Mortensen 1984. Aristotle’s Second Thesis and Abelard’s First Principle are interderivable with BT and with BT′, respectively, using intuitionistic principles only. Besides Peter Abelard, another medieval philosopher who discussed and endorsed connexive principles was Richard Kilwardby, see Johnston 2019. El-Rouayheb (2009, p. 215) reports on a critical discussion in thirteenth-century Arabic philosophy of Aristotle’s thesis AT for impossible antecedents. Modern connexive logic commenced with Nelson 1930, Angell 1962, and McCall 1966, while MacColl (1878) may be regarded as a forerunner. After small numbers of publications from the 1960s until the 1990s, with S. McCall, R. Routley, and C. Pizzi as the main contributors, in the 21st century a vigorous new interest in connexive logic emerged. Remarks on the history of modern connexive logic can be found in sections 3–5.

One question arising from a historical point of view is that of exegetical correctness. Can Aristotle’s and Boethius’ theses indeed be traced back to Aristotle and Boethius? Lenzen (2020) believes that Aristotle and Boethius intended the theses named after them as “applicable only to ‘normal’ conditionals with antecedents which are not self-contradictory.” He states correspondingly restricted versions of Aristotle’s theses in the language of modal propositional logic, principles which according to Lenzen (2019) can be found in Leibniz’s writings (after a transformation from Leibniz’s term logic into a system of propositional logic) and where, notation adjusted, ↠ stands for strict implication:

> LEIB1 ◊*A* ↠ ~(*A* ↠ ~*A*), and
> LEIB2 ◊~*A* ↠ ~(~*A* ↠ *A*),

cf. also the modalized versions of AT′ and BT in Unterhuber 2016. Lenzen remarks that LEIB1 and LEIB2 are theorems of almost all systems of normal modal logic and therefore do not lead to any non-classical system of connexive logic. A similar observation is made in Kapsner 2019. As to Boethius, the question has been raised whether it is adequate to render his term logic as a propositional logic (see Martin 1991, McCall 2012)[^martin-1991][^mccall-2012], and Bonevac and Dever (2012, p. 192) refer to Abelard’s First Principle as the most famous thesis attributed to Boethius but note that they fail to find it in Boethius. Irrespective of these exegetical issues, however, the challenge of connexive logic remains, namely to define nontrivial and well-motivated logical systems that validate both Aristotle’s and Boethius’ theses and satisfy non-symmetry of implication. Another question arising from the long history of connexive logic is in which sense the system nowadays called *classical logic* is indeed classical. A critical discussion of the classicality of classical logic from the point of view of paraconsistent and connexive logic can found in Wansing and Odintsov 2016.

A monograph developing a system of connexive logic in the context of solving a broad range of paradoxes is Angell 2002. The first monograph devoted to connexive logic sice its revival in the first two decades of the 21st century, though not a comprehensive study of connexive logic, is Francez 2021. Starting from the connexive logics **C** and **QC**, Francez discuses topics such as the already mentioned idea of ``polyconnexivity'', certain variations of Boethius’ theses (cf. section 3.6), and a connexive theory of classes.

### 3. Perspectives on connexive logic

Systems of connexive logic can be looked and arrived at from different perspectives. Although some of these viewpoints are closely interrelated, it may be helpful to briefly outline them separately.

#### 3.1 Connexivity and relevance

Routley (1978), see also Sylvan 1989 (2000, chapter 5), suggested a conception of connexive logic different from McCall’s. If the requirement of a connection between antecedent and succedent of a valid implication is understood as a content connection, and if a content connection obtains if antecedent and succedent are *relevant* to each other, then “the general classes of connexive and relevant logics are one and the same” (Routley 1978, p. 393)[^routley-1978], cf. also Sarenac and Jennings 2003, where the connection between McCall’s connexive system **CC1**, presented in section 4.1, and relevance preservation is studied.

Since every non-trivial system of connexive logic in the vocabulary of classical logic has to omit some classical tautologies, and since the standard paradoxes of non-relevant, material implication can be avoided by rejecting Conjunctive Simplification, i.e., (*A* ∧ *B*) → *A* and (*A* ∧ *B*) → *B*, Routley requires for a connexive logic the rejection or qualification of Conjunctive Simplification (or equivalent schemata). Although according to Routley (1978, Routley *et al*. 1982)[^routley-1982] and Routley and Routley (1985) the idea of negation as cancellation, see sections 3.3 and 4.3., motivates both the failure of Conjunctive Simplification and AT’ and BT, the model-theoretic semantics for connexive logics developed in Routley 1978, see section 4.2, makes use of what has later come to be known as the *Routley star negation*, see the entry on negation.

If the contraposition rule and uniform substitution are assumed and implication is transitive, the combination of Conjunctive Simplification and Aristotle’s Theses results in negation inconsistency, i.e., there are formulas *A* such that *A* and its negation ~*A* are both theorems, see, for example, Woods 1968 and Thompson 1991. Non-trivial negation inconsistent logics (with a transitive consequence relation) must be paraconsistent. Using certain three-valued truth tables, Mortensen (1984) pointed out that there are inconsistent but non-trivial systems satisfying both AT′ and Simplification. Examples of non-trivial inconsistent systems of connexive logic satisfying Conjunctive Simplification are presented in section 4.5. The availability of such connexive systems may be appreciated in view of the fact that Zermelo-Fraenkel set theory based on a system of connexive logic with Simplification is inconsistent, see Wiredu 1974. Mortensen (1984) also pointed out that the addition of AT′ to the relevance logic **R** of Anderson and Belnap has a trivializing effect, a fact shown in Routley *et al.* 1982 as well.

The relation between connexive logic and relevance logic can also be seen as follows. Let *A* and *B* be contingent formulas of classical propositional logic, i.e., formulas that are neither constantly false nor constantly true. It is well-known that then the following holds in classical logic:

1. Not: ~*A* ⊢ *A*
2. If *A* ⊢ *B*, then not: *A* ⊢ ~*B*
3. If *A* ⊢ *B*, then *A* and *B* share some propositional variable (sentence letter)

If property (iii) is generalized to arbitrary formulas *A* and *B*, it is called the *variable sharing property* or *variable sharing principle*, which is generally seen as a necessary condition on a logic to count as a relevance logic (see the entry logic: relevance). So-called *containment logics* (also called *Parry systems* or s*ystems of analytic implication*, see Parry 1933, Anderson and Belnap 1975, Fine 1986, Ferguson 2015)[^anderson-1975][^ferguson-2015][^fine-1986][^parry-1933], satisfy the strong relevance requirement that if ⊢ *A* → *B*, then every propositional variable of *B* is also a propositional variable of *A*. The variable sharing property indicates a content connection between *A* and *B* if *B* is derivable from *A* (or, semantically, *A* entails *B*). The properties (i) and (ii) may be viewed to express a content connection requirement on the derivability relation in a *negative way*. If one wants to express these constraints in terms of the provability of object language formulas, one naturally arrives at Aristotle’s and Boethius’ theses.

Connexive relevance logics that combine the ternary frame semantics from relevance logic and the adjustment of falsity conditions along the lines of the connexive logic **C** (see section 4.5.1) have been studied in Omori 2016a and Francez 2019, cf. sections 4.2 and 4.5.

#### 3.2 Conditional logic

Principles of connexive logic have been discussed in conditional logic (see the entry logic: conditional), beginning with Ramsey’s (1929) comments on what is now called the *Ramsey Test*, as pointed out, e.g., in McCall 2012 and Ferguson 2014:

> If two people are arguing “If *p* will *q*?” and are both in doubt as to *p*, they are adding *p* hypothetically to their stock of knowledge and arguing on that basis about *q*; so that in a sense “If *p*, *q*” and “If *p*, *~q*” are contradictories (notation adjusted).

Angell (1966, 1967a, 1978) refers to AT′ as the Law of Conditional Non-Contradiction. Usually, Abelard’s First Principle, ~((*A* → *B*) ∧ (*A* → *~B*)) is considered as a principle of conditional non-contradiction and as such is endorsed by some philosophers, e.g., Gibbard (1981, p. 231), Lowe (1995, p. 47), and Bennett (2003, p. 84), without making any reference to connexive logic. Conditional non-contradiction fails, however, to be a valid principle in the semantics suggested by Stalnaker (1968) and Lewis (1973), cf. the discussion in Unterhuber 2013. The restrictedly connexive logics presented in Weiss 2019 that validate Aristotle’s theses, BTw, and BTw′ stand in the tradition of Stalnaker and Lewis and are given an algebraic semantics that builds on the algebraic semantics for conditional logics from Nute 1980.

Another motivation for connexive logic from the perspective of conditional logic has been presented by John Cantwell (2008) without noting that the introduced propositional logic is a system of connexive logic. Cantwell considers the denial of indicative conditionals in natural language and argues that the denial of, say, the conditional ‘If Oswald didn’t kill Kennedy, Jack Ruby did.’ amounts to the assertion that if Oswald didn’t shoot Kennedy then neither did Jack Ruby. This suggests that (*A* → ~*B*) is semantically equivalent with ~(*A* → *B*). Also Claudio Pizzi’s work on logics of consequential implication has been motivated in the context of conditional logic, see Pizzi 1977 and section 5.

#### 3.3 Negation

As the characteristic connexive principles exhibit an implication and a negation connective, it is not very surprising that connexive logic can be approached also from considerations on the notion of negation. Two different perspectives emerge with the ideas of negation as cancellation (erasure, neutralization, or subtraction) and negation as falsity. Negation as cancellation is a conception of negation that can be traced back to Aristotle’s *Prior Analytics* and is often associated with Strawson, who held that a “contradiction cancels itself and leaves nothing” (1952, p. 3). Routley (1978, Routley *et al*. 1982)[^routley-1982], Routley and Routley 1985, and Priest 1999 use the notion of subtraction negation to motivate connexive principles. Routley and Routley (1985, p. 205) present the cancellation view of negation as follows:

> ∼*A* deletes, neutralizes, erases, cancels *A* (and similarly, since the relation is symmetrical, *A* erases ∼*A*), so that ∼*A* together with *A* leaves nothing, no content. The conjunction of *A* and ∼*A* says nothing, so nothing more specific follows. In particular, *A* ∧ ∼*A* does not entail *A* and does not entail ∼*A*.

Note that if a logic implements the cancellation view of negation, it will also be paraconsistent because the *ex contradictione quodlibet* principle, (*A* ∧ ∼*A*) ⊢ *B*, will not be valid. (The idea of *ex contradictione nihil sequitur* is discussed in Wagner 1991.)[^wagner-1991] According to the Routleys, a connection between the subtraction account of negation and Aristotle’s thesis AT′ then arises as follows (Routley and Routley 1985, p. 205)[^routley-1985]:

> Entailment is inclusion of logical content. So, if *A* were to entail ~*A*, it would include as part of its content, what neutralizes it, ~*A*, in which event it would entail nothing, having no content. So it is not the case that *A* entails ~*A*, that is Aristotle’s thesis ~(*A* → ~*A*) holds.

Accordingly then, for Routley (Routley *et al*. 1982, p. 82)[^routley-1982] connexivism has two leading theses, namely:

> 1. Simplification (*A* ∧ *B* → *A*, *A* ∧ *B* → *B*) fails to hold, and its use ... is what is responsible for the paradoxes of implication ...
> 2. Every statement is self-consistent, symbolically *A* ◇ *A*, where the relation of consistency with, symbolised ◇, is interconnected with implication in the standard fashion: *A* ◇ *B* ↔. ~(*A* → ~*B*).

The cancellation view of negation has been heavily criticized in Wansing and Skurt 2018, where it is stressed that connexive logic can be detached from the notion of negation as erasure and the failure of Conjunctive Simplification.

The notion of negation as definite falsity, in contrast to negation as absence of truth, does not support the failure of Conjunctive Simplification but rather the failure of *ex contradictione quodlibet* if it is coupled with an understanding of inference as information flow, because the information that *A* ∧ ~*A* does not necessarily give the information that *B*, for any *B* whatsoever. This suggests a separate treatment of (support of) truth and (support of) falsity conditions, which enables adopting the falsity conditions for implications represented by BTe′.

#### 3.4 Contra-classicality

Humberstone (2000) calls a logic *contra-classical* just in case not every formula provable in the logic is provable in classical logic (and, moreover, considers a more demanding notion of a contra-classical logic by requiring that there is no way of translating its connectives in such a way that one obtains a subsystem of classical logic). There are several different kinds of contra-classical logics, such as, for example, Abelian logics containing the axiom schema ((*A* → *B*) → *B*) → *A*, connexive logics, and logics of logical bilattices. The negation, truth order conjunction, weak implication, and information order disjunction fragment of Arieli and Avron’s (1996) bilattice logic **BL**_{⊃}, for example, is a standard propositional vocabulary containing a negation, a conjunction, a disjunction, and a conditional. It is a non-trivial but inconsistent logic and as such contra-classical.

In Omori and Wansing 2018, a way of obtaining contra-classical logics is delineated, and in Estrada-Gónzalez 2019 it is discussed in more detail. Following the pattern of the presentation of the connexive logic **C**, cf. section 4.5.1, the general idea is that of keeping some standard (support of) truth conditions for a logical operation and modifying its (support of) falsity conditions. From a bilateralist perspective that treats truth and falsity as well as provability and disprovability or refutability as separate semantical, respectively proof-theoretical dimensions that are on a par, there is also the strategy of keeping some standard (support of) falsity conditions for a logical operation and modifying its (support of) truth conditions. Connexive logic can be seen as contributing to the exploration of roads to contra-classicality.

#### 3.5 Empirical perspective

In McCall 2012 one can find some results on testing the endorsement of connexive principles (AT′, BT, and BT stated as a rule) given by indicative conditionals in English in concrete form on a group of 89 non-expert philosophy students at McGill University in Canada. These findings support the intuition that laymen speakers of English subscribe to those connexive principles to a rather high degree: 88% in the case of AT′, 85% in the case of BT in rule form, and 84% in the case of BT.

Empirical studies on Aristotle’s theses have been carried out by Pfeifer (2012), Pfeifer and Tulkki (2017), and Pfeifer and Yama (2017). In one experiment, presented in Pfeifer 2012, the sample consisted of 141 psychology students (110 females and 31 males) at the University of Salzburg, Austria. Both AT and AT′ were tested as abstract as well as concrete indicative conditionals. In a second experiment, 40 students without training in logic (20 females and 20 males) had to solve tasks involving concrete indicative conditionals in English. In this case, scope ambiguities arising from the negation of conditionals were ruled out. Both experiments provide evidence against the interpretation of indicative conditionals in English as Boolean implication and support the connexive reading of negated implications expressed by Aristotle’s theses. Pfeifer sees these findings as strong evidence for interpreting indicative conditionals as conditional events. This interpretation predicts that people should strongly believe that Aristotle’s theses are valid because the only coherent assessment for them is the probability value 1.

Pfeifer and Tulkki (2017) tested the interpretation of subjunctive versus indicative conditionals among a group of 60 students of the University of Helsinki, Finland, (30 females and 30 males) and found no statistically significant differences between the endorsement of AT and AT′ (72%, respectively 77%). Another experiment presented in Pfeifer and Yama 2017 found no cultural differences between the Western samples and an Eastern sample when testing the endorsement of AT and AT′ among 63 Japanese university students from the Graduate School of Literature and Human Behavioral Sciences at Osaka City University, with an endorsement of AT and AT′ by 65% and 76% of the participants, respectively.

Khemlani *et al*. 2014 report on an experiment testing a sample of 21 native English-speaking participants on denying concrete natural language conditionals (against the background of Johnson-Laird’s mental model theory, assuming classical logic). Whereas 28% of the participants endorsed denial conditions in accordance with classical logic, 34% endorsed denial conditions according to Boethius’ thesis BT.

Another experiment on the negation of indicative conditionals is presented in Egré and Politzer 2013. They consider weakenings of the classical conjunctive understanding of ~(*A* → *B*) as (*A* ∧ ~*B*) and the connexive reading as (*A* → *~B*), namely (*A* ∧ ◊~*B*), respectively (*A* → ◊~*B*). Exploiting the flexibility of the “tweaking of the falsity conditions”-approach to connexive logic, presented in sections 3.7 and 4.5, Omori 2019 interprets (*A* → ◊~*B*) in a variant of the modal logic **BK** from Odintsov and Wansing 2010 by suitably adjusting the falsity condition for implications (*A* → *B*), so that ~(*A* → *B*) is provably equivalent with (*A* → ◊~*B*).

#### 3.6 Proof-theoretical perspective

Modern modal logic started as a syntactical enterprise with C.I. Lewis, who defined a series of axiom systems to capture notions of strict implication. In a similar vein, Lewis’ student E. Nelson came up with an axiom system from which Aristotle’s and Boethius’ theses can be derived. The system is called **NL** in Mares and Paoli 2019, where its axioms and inference rules are presented as follows (we here use schematic letters for arbitrary formulas instead of propositional variables and a different symbol for negation):

| 1.1 | *A* → *A* |
| --- | --- |
| 1.2 | (*A*\|*B*) → (*B*\|*A*) |
| 1.3 | *A* → ~~*A* |
| 1.4 | (*A* → *B*) → (*A* ◦ *B*) |
| 1.5 | (*A* ≠ *B* ≠ C) → (((*A* → *B* ) ∧ (*B* → *C* )) → (*A* → *C* )) |
| 1.6 | (*A* ∧ *B*) = (*B* ∧ *A*) |
| 1.7 | ((*A* ∧ *B* ) → *C* ) → ((*A* ∧ ~*C* ) → ~*B* ) |
|   |   |
| R1 | if ⊢ *A* and ⊢ (*A* → *B*), then ⊢ *B* (modus ponens) |
| R2 | if ⊢ *A* and ⊢ *B*, then ⊢ (*A* ∧ *B*) (adjunction) |

where ◦ is a primitive binary consistency operator, (A|B) (inconsistency) is defined as ~(*A* ◦ *B*), *A* = *B* is defined as (*A* → *B*) ∧ (*B* → *A*), *A* ≠ *B* as ~ (*A* = *B*), and *A* ≠ *B* ≠ *C* is an abbreviation of (*A* ≠ *B*) ∧ (*B* ≠ *C*) ∧ (*A* ≠ *C*).

Providing a sound and complete semantics for **NL** is an open problem in connexive logic. Angell’s (1962) axiomatic proof system **PA1** can also be seen as belonging to the proof-theoretical tradition because it is incomplete with respect the truth tables presented by Angell. However, Angell proved **PA1** to be sound with respect to these truth tables, thereby for the first time presenting a non-triviality proof for a formal system of connexive logic. Providing an *intuitive* sound and complete semantics for **PA1** is another open problem in connexive logic. (Routley [1978, p. 409] admits that his characterization is “not intuitively very satisfying: as it stands the modelling is rather complex, with the modelling conditions exceeding in number the postulates they model, and basic connexive postulates like Boethius, instead of being validated in a natural way, have fairly intractable conditions.”)

In proof-theoretic semantics, proof systems of a suitable form are seen as providing a meaning theory, see the entry proof-theoretic semantics. In that spirit, Francez (2016) presents two natural deduction proof systems for a propositional language with negation and implication, one in which AT, AT′, BT, and BT′ are provable, and another one in which AT, AT′, and the following variations of Boethius’ theses are provable:

> B3: (*A* → *B*) → ~(~*A* → *B*) and
> B4: (*~A*→ *B*) → ~(*A* → *B*).

Francez motivates these principles by certain natural language discourses and a “dual Ramsey Test” that modifies the Ramsey test by assuming that in the course of arguing “If *p* will *q*?,” ~*p* is hypothetically added to a stock of knowledge. Francez’ natural deduction rules are straightforwardly obtained by modifying the natural deduction rules for the negation and implications fragment of David Nelsons’s four-valued constructive logic **N4**, cf. Kamide and Wansing 2012, in the manner that leads from **N4** to the constructive connexive logic **C** from Wansing 2005, cf. section 4.5.1. In Francez 2019 the natural deduction system that gives AT, AT′, BT, and BT′ is relevantized as in the familiar natural deduction proof system for the implication fragment of the relevant logic **R** by introducing subscripts for book-keeping in order to avoid empty, irrelevant implication introductions. Omori (2016b) adds conjunction and disjunction to the language of Francez 2016, gives an axiomatization and a characterizing semantics for the natural deduction system that allows to prove B3 and B4, and observes that although AT and AT′ are valid, BT, and BT′ are invalid, which prompts him to call the provable equivalence ~(*A* → *B*) ↔ (~*A* → *B*) “half-connexive”.

The natural deduction proof system in Wansing 2016b can be seen a contribution to a bilateralist proof-theoretic semantics for certain connexive logics given in terms of provability as well as refutability conditions. In addition to a connexive implication that internalizes a notion of provability into the object language, there is also a connexive co-implication that internalizes a refutability relation. The resulting bi-connexive logic **2C** is a connexive variant of the bi-intuitionistic logic **2Int** from Wansing 2016a, 2018. A natural deduction calculus for a quantum logic satisfying Aristotle’s theses is presented in Kamide 2017.

According to Schroeder-Heister 2009, Gentzen’s sequent calculus is a “more adequate formal model of hypothetical reasoning” than natural deduction, and proof-theoretic semantics has also been developed with respect to various kinds of sequent calculi. Sequent systems for connexive logics can be found in Wansing 2007, Wansing 2008, McCall 2014, Kamide and Wansing 2011, 2016, Kamide, Shramko and Wansing 2017, and Kamide 2019.

#### 3.7 Semantical perspective

A central approach to connexive logic is given by many-valued and model-theoretic semantics in terms of truth values or support of truth and support of falsity conditions. As explained in Omori and Wansing 2019, the semantics of several connexive logics can be described as either (i) modifying some standard (support of) truth conditions of conditionals of a certain kind or keeping standard truth conditions in combination with more complex model structures, or (ii) as tweaking the standard (support of) falsity conditions of certain familiar implications. Given the multitude of different connexive logics and the flexibility of the adjustment of falsity conditions in combination with standard (support of) truth conditions, this classification provides a general perspective.

A key observation for this classificatory enterprise comes from Omori and Sano 2015, where a mechanical procedure is described for turning truth tables using the four generalized truth values of first-degree entailment logic, **FDE**, see the entries on truth values and relevance logic and Omori and Wansing 2017, into pairs of positive and negative conditions in terms of containing or not containing the classical truth values 0 and 1. Then, in McCall’s system **CC1** a connexive conditional *A* → *B* receives a designated value (is true) in a model just in case (i) *A* does not receive a designated value or *B* does *and* (ii) 0 belongs to the value of *A* iff it belongs to the value of *B*. In this sense, the connexive implication of Angell-McCall is obtained by adding a condition to the truth condition for Boolean implication.

The consequential conditional in the logics of consequential implication investigated by Pizzi (1977, 1991, 1993, 1996, 2004, 2005, 2008, 2018) and Pizzi and Williamson (1997, 2005) validates Aristotle’s theses but fails to validate Boethius’ theses. It is thus connexive only in a weak sense, but since the consequential implication is a strict conditional that is required to satisfy some extra condition, also logics of consequential implication fit into the classificatory scheme provided by the semantical perspective. The following table is a slight extension of the summarizing overview from Omori and Wansing 2019 (with pointers to the relevant sections of the present entry), where the approaches above the double line adjust (support of) truth conditions (or add semantical machinery to standard truth conditions), whereas the approach below the double line tweaks (support of) falsity conditions:

|   | *conditional* | *negation* | *consequence relation* |
| --- | --- | --- | --- |
| Angell-McCall, section 4.1 | material + tweak | classical | standard |
| Routley, section 4.2 | relevant + ‘generation relation’ | star | standard |
| Priest, section 4.3 | strict + tweak | classical | non-standard |
| Jarmużek and Malinowski, section 4.4 | material + double-barreld analysis | classical | standard |
| Pizzi, section 5 | strict + tweak | classical | standard |
|   |   |   |   |
| Wansing, section 4.5 | various kinds | De Morgan | standard |

A dialogical semantical treatment of connexive logic can be found in Rahman and Rückert 2001.

## 4. Systems of connexive logic

### 4.1 Algebraic connexive logic

Whereas the basic ideas of connexive logic can be traced back to antiquity, the search for formal systems with connexive implication seems to have begun only in the 19th century in the work of H. MacColl (1878), see also Rahman and Redmond 2008. The basic idea of connexive implication was spelled out also by E. Nelson (1930), and a more recent formal study of systems of connexive logic started in the 1960s. In McCall 1966, S. McCall presented an axiomatization of a system of propositional connexive logic semantically introduced by Angell (1962) in terms of certain four-valued matrices. The language of McCall’s logic **CC1** contains as primitive (notation adjusted) a unary connective ~ (negation) and the binary connectives ∧ (conjunction) and → (implication). Disjunction ∨ and equivalence ↔ are defined in the usual way. The schematic axioms and the rules of **CC1** are as follows:

| A1 | (*A* → *B*) → ((*B* → *C*) → (*A* → *C*)) |
| --- | --- |
| A2 | ((*A* → *A*) → *B*) → *B* |
| A3 | (*A*→ *B*) → ((*A* ∧ *C*) → (*B* ∧ *C*)) |
| A4 | (*A* ∧ *A*) → (*B* → *B*) |
| A5 | (*A* ∧ (*B* ∧ *C*)) → (*B* ∧ (*A* ∧ *C*)) |
| A6 | (*A* ∧ *A*) → ((*A* → *A*) → (*A* ∧ *A*)) |
| A7 | *A* → (*A* ∧ (*A* ∧ *A*)) |
| A8 | ((*A* → ~*B*) ∧ *B*) → ~*A* |
| A9 | (*A* ∧ ~(*A* ∧ ~*B*)) → *B* |
| A10 | ~(*A* ∧ ~(*A* ∧ *A*)) |
| A11 | (~*A* ∨ ((*A* → *A*) → *A*)) ∨ (((*A* → *A*) ∨ (*A* → *A*)) → *A*) |
| A12 | (*A* → *A*) → ~(*A* → ~*A*) |
|   |   |
| R1 | if ⊢ *A* and ⊢ (*A* → *B*), then ⊢ *B* (modus ponens) |
| R2 | if ⊢ *A* and ⊢ *B*, then ⊢ (*A* ∧ *B*) (adjunction) |

Among these axiom schemata, only A12 is contra-classical. The system **CC1** is characterized by the following four-valued truth tables with designated values 1 and 2:

| <table class="cell-center cellpad-small-dense all-rules vert-top grayborder avoid-break"> <tbody> <tr> <td>~</td> <td>&nbsp;</td> </tr> <tr> <td>1</td> <td>4</td> </tr> <tr> <td>2</td> <td>3</td> </tr> <tr> <td>3</td> <td>2</td> </tr> <tr> <td>4</td> <td>1</td> </tr> </tbody> </table> | <table class="cell-center cellpad-small-dense all-rules vert-top grayborder avoid-break"> <tbody> <tr> <td>&and;</td> <td>1</td> <td>2</td> <td>3</td> <td>4</td> </tr> <tr> <td>1</td> <td>1</td> <td>2</td> <td>3</td> <td>4</td> </tr> <tr> <td>2</td> <td>2</td> <td>1</td> <td>4</td> <td>3</td> </tr> <tr> <td>3</td> <td>3</td> <td>4</td> <td>3</td> <td>4</td> </tr> <tr> <td>4</td> <td>4</td> <td>3</td> <td>4</td> <td>3</td> </tr> </tbody> </table> | <table class="cell-center cellpad-small-dense all-rules vert-top grayborder avoid-break"> <tbody> <tr> <td>&rarr;</td> <td>1</td> <td>2</td> <td>3</td> <td>4</td> </tr> <tr> <td>1</td> <td>1</td> <td>4</td> <td>3</td> <td>4</td> </tr> <tr> <td>2</td> <td>4</td> <td>1</td> <td>4</td> <td>3</td> </tr> <tr> <td>3</td> <td>1</td> <td>4</td> <td>1</td> <td>4</td> </tr> <tr> <td>4</td> <td>4</td> <td>1</td> <td>4</td> <td>1</td> </tr> </tbody> </table> |
| --- | --- | --- |

McCall emphasizes that the logic **CC1** is only one among many possible systems satisfying the theses of Aristotle and Boethius. Although **CC1** *is* a system of connexive logic, its algebraic semantics appears to be only a formal tool with little explanatory capacity. In **CC1**, the constant truth functions **1**, **2**, **3**, and **4** can be defined as follows (McCall1966, p. 421): **1** := (*p* → *p*), **2** := ~(*p* ↔ ~*p*), **3** := (*p* ↔ ~*p*), **4** := ~(*p*→ *p*), for some sentence letter *p*. As Routley and Montgomery (1968, p. 95) point out, **CC1** “can be given a semantics by associating the matrix value 1 with logical necessity, value 4 with logical impossibility, value 2 with contingent truth, and value 3 with contingent falsehood. However, many anomalies result; e.g. the conjunction of two contingent truths yields a necessary truth”. Moreover, McCall points out that **CC1** has some properties that are difficult to justify if the name ‘connexive logic’ is meant to reflect the fact that in a valid implication *A* → *B* there exists some form of connection between the antecedent *A* and the succedent *B*. Axiom A4, for example, is bad in this respect. On the other hand, **CC1** might be said to undergenerate, since (*A* ∧ *A*) → *A* and *A* → (*A* ∧ *A*) fail to be theorems of **CC1**. Routley and Montgomery (1968) showed that the addition of the latter formulas to only a certain subsystem of **CC1** leads to inconsistency. For a defense of Angell’s **PA1** against Routley and Montgomery’s critical observations see Bode 1979.

These observations may well have distracted many non-classical logicians from connexive logic at that time. If the validity of Aristotle’s and Boethius’ Theses is distinctive of connexive logics, it is, however, not quite clear how damaging the above criticism is. In order to construct a more satisfactory system of connexive logic, McCall (1975) defined the notions of a connexive algebra and a connexive model and presented an axiom system **CFL** that is characterized by the class of all connexive models. In the language of **CFL**, however, every implication is first-degree, i.e., no nesting of → is permitted. McCall refers to a result by R. Meyer showing that the valid implications of **CFL** form a subset of the set of valid material equivalences and briefly discusses giving up the syntactic restriction to first-degree implication. Meyer (1977) showed that the first-degree fragment of the normal modal logic **S5** (and in fact every normal modal logic between **KT** and **S5**, cf. the entry logic: modal) and **CFL** are equivalent in the following sense: all theorems of **CFL** are provable in **S5** if the connexive implication *A* → *B* is defined as □(*A* ⊃ *B*) ∧ (*A* ≡ *B*), where ⊃ and ≡ are classical implication and equivalence, respectively, and every first-degree theorem of **S5** is provable in **CFL** if □*A* (“it is necessary that *A*”) is defined as (~*p* ∨ *p*)→*A*. In summary, it seems fair to say that as the result of the investigations into connexive logic in the 1960s and 1970s, connexive logic, its ancient roots notwithstanding, appeared as a sort of exotic branch of non-classical logic.

More recently, Cantwell (2008) presented a truth table semantics for a system of connexive logic together with a proof-theoretical characterization. The truth tables for negation and implication are taken from Belnap 1970, but Cantwell's three-valued truth table for the conditional can already be found in a paper by William Cooper (1968). Like Cantwell, Cooper wanted to formally model how conditional sentences in the indicative mood and expressed by means of *if-then* are used in ordinary conversational English. (Whereas Cantwell takes the entire three-element set of truth values as the co-domain of assignment functions for propositional variables, Cooper restricts assignment functions to mappings from the set of propositional variables to the two-element set of classical truth values.) Cantwell considers a language containing the constantly false proposition ⊥ and the following three-valued truth tables for negation, conjunction, disjunction, and implication with designated values T and − (where ‘T’ stands for truth and ‘F’ for falsity):

| <table class="cell-center cellpad-small-dense all-rules vert-top grayborder avoid-break"> <tbody> <tr> <td>~</td> <td>&nbsp;</td> </tr> <tr> <td>T</td> <td>F</td> </tr> <tr> <td>F</td> <td>T</td> </tr> <tr> <td>&minus;</td> <td>&minus;</td> </tr> </tbody> </table> | <table class="cell-center cellpad-small-dense all-rules vert-top grayborder avoid-break"> <tbody> <tr> <td>&and;</td> <td>T</td> <td>F</td> <td>&minus;</td> </tr> <tr> <td>T</td> <td>T</td> <td>F</td> <td>&minus;</td> </tr> <tr> <td>F</td> <td>F</td> <td>F</td> <td>F</td> </tr> <tr> <td>&minus;</td> <td>&minus;</td> <td>F</td> <td>&minus;</td> </tr> </tbody> </table> |
| --- | --- |
| <table class="cell-center cellpad-small-dense all-rules vert-top grayborder avoid-break"> <tbody> <tr> <td>&or;</td> <td>T</td> <td>F</td> <td>&minus;</td> </tr> <tr> <td>T</td> <td>T</td> <td>T</td> <td>T</td> </tr> <tr> <td>F</td> <td>T</td> <td>F</td> <td>&minus;</td> </tr> <tr> <td>&minus;</td> <td>T</td> <td>&minus;</td> <td>&minus;</td> </tr> </tbody> </table> | <table class="cell-center cellpad-small-dense all-rules vert-top grayborder avoid-break"> <tbody> <tr> <td>&rarr;</td> <td>T</td> <td>F</td> <td>&minus;</td> </tr> <tr> <td>T</td> <td>T</td> <td>F</td> <td>&minus;</td> </tr> <tr> <td>F</td> <td>&minus;</td> <td>&minus;</td> <td>&minus;</td> </tr> <tr> <td>&minus;</td> <td>T</td> <td>F</td> <td>&minus;</td> </tr> </tbody> </table> |

In this system, introduced as a system of conditional negation, **CN**, (*A* → ~*B*) and ~(*A* → *B*) have the same value under every assignment of truth values to propositional variables. Cantwell’s system thus validates BTe and BTe′, and it turns out to be the connexive logic **MC** from Wansing 2005, see section 4.5.3, extended by the Law of Excluded Middle, *A* ∨ ~*A*. A certain expansion of **CN** is studied in Olkhovikov 2002, 2016 and, independently, in Omori 2016c, see section 4.5.3.

A three-valued logic that validates Aristotle’s theses but not Boethius’ theses and that is subminimally connexive and Kapsner strong in the terminology of Estrada-González & Ramirez-Cámara 2016 is the three-valued logic **MRSᴾ** that was introduced in Estrada-González 2008. In Estrada-González & Ramirez-Cámara 2016, **MRSᴾ** is discussed against the background of Cantwell’s three-valued connexive logic **CN** and Mortensen’s (1984) three-valued connexive logic, dubbed **M3V** by McCall (2012).

McCall (2014) presents a cut-free sequent calculus for a system of connexive logic that he calls “connexive Gentzen.” The calculus has the non-standard feature of using pairs of axioms that are not logical truths. An annotation with subscripts is used to enable the elimination of dependencies on such non-standard axioms in the course of a derivation. The resulting system differs from **CC1** in that *p* → (*p* ∧ *p*) and (*p* ∧ *p*)→ *p* are provable, and it is shown to be sound with respect to certain four-valued matrices. Sound and complete cut-free sequent calculi for certain constructive and modal connexive logics have been presented for the first time in Wansing 2008 and Kamide and Wansing 2011.

### 4.2 Connexive logic based on ternary frames for relevance logics (Australian Plan)

In the late 1970s and the 1980s, connexive logic was subjected to semantical investigations based on ternary frames for relevance logics, making use of the Routley star negation that is distinctive of logics “on the Australian Plan,” cf. Meyer and Martin 1986. Routley (1978) obtained a semantic characterization of Aristotle’s Thesis AT′ and Boethius’ Thesis BT using a ‘generation relation’ *G* between a formula *A* and a possible world *s*. The semantics employs model structures F = <*T*, *K*, *R*, *S*, *U*, *G*, *>, where *K* is a non-empty set of possible worlds, *T* ∈ *K* is a distinguished world (the ‘real world’), *R*, *S*, and *U* are ternary relations on *K*, *G* is a generation relation, and * is a function on *K* mapping every world *s* to its ‘opposite’ or ‘reverse’ *s**. A valuation is a function *v* that sends pairs of worlds and propositional variables into {0,1}, satisfying the following heredity condition: if *R*(*T*, *s*, *u*) and *v*(*p*, *s*) = 1, then *v*(*p*, *u*) = 1. Intuitively, *G*(*A*, *t*) is supposed to mean that everything that holds in world *t* is implied by *A*. A model is a structure M = <F, *v*>. The relation M, *t* ⊨ *A* (“*A* is true at *t* in M”) is inductively defined as follows:

> M, *t* ⊨ *p* iff *v*(*p*, *t*) = 1
> M, *t* ⊨ ~*A* iff M, *t** ⊭ *A*
> M, *t* ⊨ (*A* ∧ *B*) iff there are *s*, *u* with *Stsu* M, *s* ⊨ *A* and M, *u* ⊨ *B*
> M, *t* ⊨ (*A* ∨ *B*) iff there are *s*, *u* with *Utsu* M, *s* ⊨ *A* or M, *u* ⊨ *B*
> M, *t* ⊨ (*A* → *B*) iff for all *s*, *u* if *Rtsu* and M, *s* ⊨ *A*, then M, *u* ⊨ *B*

[Note: whenever there is little chance for ambiguity, we replace *R*(*x*, *y*, *z*) by *Rxyz*.]

Moreover, it is required that for every formula *A* and world *t*, *G*(*A*, *t*) implies M, *t* ⊨ *A*. A formula *A* is true in model M iff M, *T* ⊨ *A*, and *A* is valid with respect to a class of models if *A* is true in all models from that class. AT′ is semantically characterized by the following property of models: ∃*t* (*R*(*T**, *t*, *t**) and *G*(*A*, *t*)), and BT is characterized by ∀*w*∃*s*, *t*, *u* (*R*(*w*, *s*, *t*), *R*(*w**, *s*, *u*), *G*(*A*, *s*), and *R*(*T*, *t*, *u**)).

Mortensen (1984), who considers AT′, explains that Routley’s characterization of AT′ is “not particularly intuitively enlightening” and points out that in certain logics with a ternary relational models semantics another characterization of AT′ is available, namely the condition that for every model M the set C_{*A*} := {*s* : M, *s* ⊨ *A* and M, *s* ⊭ ~*A*} is non-empty. Like Routley’s non-recursive requirement that *G*(*A*, *t*) implies M, *t* ⊨ *A*, Mortensen’s condition is not a purely structural condition, since it mentions the truth relation ⊨. Mortensen (1984, p. 114) maintains that the condition *C*_{*A*} ≠ ∅ “is closest to the way we think of Aristotle,” and emphasizes that for a self-inconsistent proposition *A*, the set *C*_{*A*} must be empty, whence AT′ is to be denied. Mortensen also critically discusses the addition of AT′ to the relevance logic **E**. In this context, AT′ amounts to the condition that no implication is true at the world *T**.

A more regular semantics for extensions of the basic relevance logic **B** (not to be confused with the truth valued read as “both true and false”) by either AT′ or BT has been presented in Brady 1989. In this semantics, conjunction is defined in the standard way, and there is a non-empty subset of worlds *O* ⊆ *K*. The set *O* contains the distinguished element *T* used to define truth in a model. The extended model structures contain a function ℑ that maps sets of worlds, and in particular, interpretations of formulas (alias propositions) *I*(*A*) to sets of worlds in such a way that a formula *A* is true at a world *t* iff *t* ∈ ℑ(*I*(*A*)). This allows Brady to state model conditions capturing AT′ and BT as follows:

> AT′: If *t* ∈ *O*, then (∃*x*, *y* ∈ ℑ(*f*)) *Rt***xy** , for any proposition *f*;
>
> BT: (∃*x*,*y* ∈ ℑ(*f*)) (∃*z* ∈ *K*) (*Rtxz* and *Rt***yz**), for any proposition *f* and any *t* ∈ *K*.

Note that these clauses still are not purely structural conditions but conditions on the interpretation of formulas. Also the investigations into connexive logics based on ternary frames did not, as it seems, lead to establishing connexive logic as a fully recognized branch of non-classical logic.

### 4.3 Connexive logic based on subtraction negation

Albeit according to Routley (1978), Routley *et al*. (1982) and Routley and Routley (1985) there is a close relation between connexive logic and the idea of negation as cancellation, Routley suggested a semantics using a generation relation and the star negation in ternary frames for relevance logics, whereas connexive logics based in a straightforward way on the cancellation view of negation have been worked out by Priest (1999). Priest (1999) directly translates a definition of entailment that enforces the null-content account of contradictions into evaluation clauses. A model is a structure M = <*W*, *g*, *v*>, where *W* is a non-empty set of possible worlds, *g* is a distinguished element from *W*, and *v* is a valuation function from the set of propositional variables into the set of classical truth values {1, 0}. Two clauses for evaluating implications at possible worlds are considered (notation adjusted):

> (a) M, *s* ⊨ *A* → *B* iff (i) there is a world *u* with M, *u* ⊨ *A* and (ii) for every world *u*, M, *u* ⊨ *A* then M, *u* ⊨ *B*;
> (b) M, *s* ⊨ *A* → *B* iff (i) there is a world *u* with M, *u* ⊨ *A*, (ii) there is a world *u* with M, *u* ⊭ *B*, and (iii) for every world *u*, M, *u* ⊨ *A* then M, *u* ⊨ *B*.

Condition (i) ensures that nothing is implied by an unsatisfiable antecedent. The evaluation clauses for the other connectives are classical. A formula *A* is true in a model (M ⊨ *A*) iff M, *g* ⊨ *A*; and *A* is valid iff *A* is true in every model. Condition (ii) ensures that the law of contraposition is valid. A set Δ of formulas is true in a model iff every element of Δ is true in the model.

There are two notions of entailment (Δ ⊨ *A*), one coming with clause (a) the other with clause (b):

> (a) Δ⊨ *A* iff Δ is true in some model, and every model in which Δ is true is a model in which *A* is true;
> (b) Δ⊨ *A* iff Δ is true in some model, ~*A* is true in some model, and every model in which Δ is true is a model in which *A* is true.

These two connexive logics arise from the idea of negation as cancellation in a straightforward way. They are neither monotonic nor closed under uniform substitution. Proof systems and decision procedures for them can be obtained from a straightforward faithful translation τ into the modal logic **S5**, cf. the entry logic: modal. For implications *A* → *B* the translation is defined as follows, where ⊃ is material implication and ¬ is classical negation:

> (a) ◊τ(*A*) ∧ □(τ(*A*) ⊃ τ(*B*));
> (b) ◊τ(*A*) ∧ ◊¬τ(*B*) ∧ □(τ(*A*) ⊃ τ(*B*)).

Ferguson (2015) observes that the intersection of the semantical consequence relations of variant (a) of Priest’s logic and the negation, conjunction, disjunction fragment of Bochvar’s 3-valued logic (cf. the entry many-valued logic) results in a known system of containment logic, namely the system **RC** presented in Johnson 1976.

Although the semantics of Priest’s connexive logics is simple and transparent, the underlying idea of subtraction negation is not unproblematic. Priest (1999, 146) mentions strong fallibilists who “endorse each of their views, but also endorse the claim that some of their views are false”. Their contradictory opinions in fact hardly are contentless, so that the cancellation account of negation and, as a result, systems of connexive logic based on subtraction negation appear not to be very well-motivated. In Skurt and Wansing 2018, it is argued that the metaphoric notion of negation as cancellation is conceptually unclear and that Routley’s (Routley *et al*. 1982)[^routley-1982]) suggestion to replace it by a notion of negation as subtraction in generalized arithmetic is unclear at least insofar as it has not been worked out in detail.

### 4.4 Boolean connexive relatedness logic

The Boolean connexive logics of Jarmużek and Malinowski 2019a are obtained in the framework of *relating logic*, a generalization of *relatedness logic*. The latter is an instance of what Sylvan (1989, p. 166) calls a “double-barrelled” analysis of implications, an analysis that complements truth conditions with an additional “sieve” or “filter” that tightens the relation between antecedent and succedent. If the relation is meant to be a relevance relation, this is an example of what Schurz 1998 calls “relevance post validity” in contrast to “relevance in validity” as investigated in relevance logic. Boolean connexive logics extend the language of classical propositional logic using conjunction, disjunction, and Boolean negation by a relating implication, →ʷ, the semantics of which is constrained by a binary relation *R* on the set of all formulas. A model then is a pair <*v*,*R*>, where *v* is a classical valuation function. The truth condition for relating implication imposes the relatedness constraint:

> <*v*,*R*> ⊨ *A* →ʷ *B* iff [(<*v*,*R*> ⊭ *A* or <*v*,*R*> ⊨ *B*) and *R*(*A*, *B*)]

and a notion of validity with respect to a relation *R* is defined: *R* ⊨ *A* iff for every valuation *v*, *v*,*R* ⊨ *A*.

In order to obtain connexive logics, Jarmużek and Malinowski introduce the following conditions on binary relations *R*:

> (a1) *R* is (a1) iff for any *A*: not *R*(*A*, ~*A*)
> (a2) *R* is (a2) iff for any *A*: not *R*(~*A*, *A*)
> (b1) *R* is (b1) iff for arbitrary *A*, *B*: (i) if *R*(*A*, *B*) then not *R*(*A*, ~*B*) and (ii) R((*A* →ʷ *B*), ~(*A* →ʷ ~*B*)) (b2) *R* is (b2) iff for arbitrary *A*, *B*: (i) if *R*(*A*, *B*) then not *R*(*A*, ~*B*) and (ii) R((*A* →ʷ ~*B*), ~(*A* →ʷ *B*)).

These conditions suffice to validate Aristotle’s and Boethius theses. A correspondence between Aristotle’s and Boethius theses and conditions on *R* is obtained if the relations *R* are required to be closed under negation, i.e., for all formulas *A* and *B*, *R*(*A*, *B*) implies *R*(~*A*, ~*B*). Then,

> (a1) *R* is (a1) iff *R* ⊨ ~(*A* →ʷ ~*A*)
> (a2) *R* is (a2) iff *R* ⊨ ~(~*A* →ʷ *A*)
> (b1) *R* is (b1) iff *R* ⊨ (*A* →ʷ *B*) →ʷ ~(*A* →ʷ ~*B*)
> (b2) *R* is (b2) iff *R* ⊨ (*A* →ʷ ~*B*) →ʷ ~(*A* →ʷ *B*).

However, these correspondences come at a price. Jarmużek and Malinowski point out that imposing negation closure validates the otherwise refutable formula ~((*A* →ʷ *B*) ∧ ~*B* ∧ ~(~*A* →ʷ ~*B*)) with respect to any relation *R*. Jarmużek and Malinowski also show that these five conditions are independent of each other and therefore give rise to 2⁵ different logics. The two connexive ones (alias properly connexive ones in Jarmużek and Malinowski’s terminology), i.e., the logic defined by means of conditions (a1), (a2), (a3), and (4) and the logic defined by in addition requiring negation closure, are also Kapsner strong. Moreover, Jarmużek and Malinowski present sound and complete tableau calculi for these 2⁵ logics.

### 4.5 **FDE**-based connexive logics (American Plan)

The basic paraconsistent logic **FDE** of first-degree entailment lacks a primitive implication connective and lends itself to adding an implication connective that validates Aristotle’s and Boethius’ theses by using the falsity conditions of implications as expressed by BTe′. This is possible because negation is treated according to “the American Plan,” i.e., by making use of four semantical values: **T** (“told true only”), **F** (“told false only”), **N** (“neither told true nor told false”), and **B** (“both told true and told false”), so that support of truth and support of falsity emerge as two independent semantical dimensions:

> *A* receives the value **T** at state *t* iff *t* supports the truth of *A* but not the falsity of *A*;
> *A* receives the value **F** at *t* iff *t* supports the falsity of *A* but not the truth of *A*;
> *A* receives the value **N** at *t* iff *t* neither supports the truth of *A* nor supports the falsity of *A*;
> *A* receives the value **B** at *t* iff *t* supports both the truth and the falsity of *A*.

Negation is then understood as leading from support of truth to support of falsity, and vice versa. The method of tweaking the (support of) falsity conditions can be applied to a number of different conditionals, ranging from constructive, relevant, and material (Boolean) implication to very weak implications studied in conditional logic with the help of so-called *Segerberg frames*.

#### 4.5.1 **FDE**-based constructive connexive logic

A system of connexive logic with an intuitively plausible possible worlds semantics using a binary relation between worlds has been introduced in Wansing 2005. In this paper it is observed that a modification of the falsification conditions for negated implications in possible worlds models for David Nelson’s constructive four-valued logic with strong negation results in a connexive logic, called **C**, which inherits from Nelson’s logic an interpretation in terms of information states pre-ordered by a relation of possible expansion of these states. For Nelson’s constructive logics see, for example, Almukdad and Nelson 1984, Gurevich 1977, Nelson 1949, Odintsov 2008, Routley 1974, Thomason 1969, Wansing 2001, Kamide and Wansing 2012.

The key observation for obtaining **C** is simple: in the presence of the double negation introduction law, it suffices to validate both BT′ and its converse ~(*A* → *B*) → (*A* → ~*B*). In other words, an interpretation of the falsification conditions of implications is called for, which deviates from the standard conditions. In Nelson’s systems of constructive logic, the double negation laws hold, and the relational semantics for these logics is such that falsification and verification of formulas are dealt with separately. The system **N4** extends **FDE** by intuitionistic implication, however, the falsification conditions of implications are the classical ones expressed by the schema ~(*A* → *B*) ↔ (*A* ∧ ~*B*). To obtain a connexive implication, it is therefore enough to assume another interpretation of the falsification conditions of implications, namely the one expressed by BTe′: (*A* → ~*B*) ↔ ~(*A* → *B*).

Consider the language *L* := {∧, ∨, →, ~} based on a denumerable set of propositional variables. Equivalence ↔ is defined as usual. The schematic axioms and rules of the logic **C** are:

| a1 | the axioms of intuitionistic positive logic |
| --- | --- |
| a2 | ~~*A* ↔ *A* |
| a3 | ~(*A* ∨ *B*) ↔ (~*A* ∧ ~*B*) |
| a4 | ~(*A* ∧ *B*) ↔ (~*A* ∨ ~*B*) |
| a5 | ~(*A* → *B*) ↔ (*A* → ~ *B*) |
|   |   |
| R1 | modus ponens |

Clearly, a5 is the only contra-classical axiom of **C**. The consequence relation ⊢_{**C**} (derivability in **C**) is defined as usual. A **C**-frame is a pair F = <*W*, ≤ >, where ≤ is a reflexive and transitive binary relation on the non-empty set *W*. Let <*W*, ≤ >⁺ be the set of all *X* ⊆ *W* such that if *u* ∈ *X* and *u* ≤ *w*, then *w* ∈ *X*. A **C**-model is a structure M = <*W*, ≤, *v*⁺, *v*^{−} >, where <*W*, ≤ > is a **C**-frame and *v*⁺ and *v*^{−} are valuation functions from the set of propositional variables into <*W*, ≤ >⁺. Intuitively, *W* is a set of information states. The function *v*⁺ sends a propositional variable *p* to the states in *W* that support the truth of *p*, whereas *v*^{−} sends *p* to the states that support the falsity of *p*. M = <*W*, ≤, *v*⁺, *v*^{−} > is said to be the model based on the frame <*W*, ≤ >. The relations M, *t* ⊨⁺ *A* (“M supports the truth of *A* at *t*”) and M, *t* ⊨^{−} *A* (“M supports the falsity of *A* at *t*”) are inductively defined as follows:

> M, *t* ⊨⁺ *p* iff *t* ∈ *v*⁺(*p*)
> M, *t* ⊨^{−} *p* iff *t* ∈ *v*^{−}(*p*)
> M, *t* ⊨⁺ (*A* ∧ *B*) iff M, *t* ⊨⁺ *A* and M, *t* ⊨⁺ *B*
> M, *t* ⊨^{−} (*A* ∧ *B*) iff M, *t* ⊨^{−} *A* or M, *t* ⊨^{−} *B*
> M, *t* ⊨⁺ (*A* ∨ *B*) iff M, *t* ⊨⁺*A* or M, *t* ⊨⁺ *B*
> M, *t* ⊨^{−} (*A* ∨ *B*) iff M, *t* ⊨^{−} *A* and M, *t* ⊨^{−} *B*
> M, *t* ⊨⁺ (*A* → *B*) iff for all *u* ≥ *t* (M, *u* ⊨⁺ *A* implies M, *u* ⊨⁺ *B*)
> M, *t* ⊨^{−} (*A* → *B*) iff for all *u* ≥ *t* (M, *u* ⊨⁺ *A* implies M, *u* ⊨^{−} *B*)
> M, *t* ⊨⁺ ~*A* iff M, *t* ⊨^{−} *A*
> M, *t* ⊨^{−} ~*A* iff M, *t* ⊨⁺ *A*

If M = <*W*, ≤, *v*⁺, *v*^{−} > is a **C**-model, then M ⊨ *A* (“*A* is valid in M”) iff for every *t* ∈ *W*, M, *t* ⊨⁺ *A*. F ⊨ *A* (“*A* is valid on F”) iff M ⊨ *A* for every model M based on F. A formula is **C**-valid iff it is valid on every frame. Support of truth and support of falsity for arbitrary formulas are persistent with respect to the relation ≤ of possible expansion of information states. That is, for any **C**-model M = <*W*, ≤, *v*⁺, *v*^{−} > and formula *A*, if *s* ≤ *t*, then M, *s* ⊨⁺ *A* implies M, *t* ⊨⁺ *A* and M, *s* ⊨^{−} *A* implies M, *t* ⊨^{−} *A*. It can easily be shown that a negation normal form theorem holds. The logic **C** is characterized by the class of all **C**-frames: for any *L*-formula *A*, ⊢_{**C**} *A* iff *A* is **C**-valid. Moreover, **C** satisfies the disjunction property and the constructible falsity property. If ⊢_{**C**} *A* ∨ *B*, then ⊢_{**C**} *A* or ⊢_{**C**} *B*. If ⊢_{**C**} ~(*A* ∧ *B*), then ⊢_{**C**} ~ *A* or ⊢_{**C**} ~*B*. Decidability of **C** follows from a faithful embedding into positive intuitionistic propositional logic.

Like Nelson’s four-valued constructive logic **N4**, **C** is a paraconsistent logic (cf. the entry logic: paraconsistent). Note that **C** contains contradictions, for example: ⊢_{**C**} ((*p* ∧ ~*p*) → (~*p* ∨ *p*)) and ⊢_{**C**} ~((*p* ∧ ~*p*) → (~*p* ∨ *p*)). It is obvious from the above presentation that **C** differs from **N4** only with respect to the falsification (or support of falsity) conditions of implications. As in **N4**, provable strong equivalence is a congruence relation, i.e., the set {*A* : ⊢_{**C**} *A*} is closed under the rule *A* ↔ *B*, ~*A* ↔ ~*B* / *C*(*A*) ↔ *C*(*B*). Wansing (2005) also introduces a first-order extension **QC** of **C**. Kamide and Wansing (2011) present a sound and complete sequent calculus for **C** and show the cut-rule to be admissible, which means that it can be dispensed with.

Whereas the direction from right to left of Axiom a5 can be justified by rejecting the view that if *A* implies *B* and *A* is inconsistent, *A* implies any formula, in particular *B*, the direction from left to right seems rather strong. If the verification conditions of implications are dynamic (in the sense of referring to other states in addition to the state of evaluation), then a5 indicates that the falsification conditions of implications are dynamic as well. The falsity of (*A* → *B*) thus implies that if *A* is true, *B* is *false*. Yet, one might wonder why it is not required that the falsity of (*A*→ *B*) implies that if *A* is true, *B* is *not true*. This cannot be expressed in a language with just one negation, ~, expressing falsity instead of absence of truth (classically at the state of evaluation or intuitionistically at all related states). If one adds to **C** the further axiom ~*A* → (*A* → *B*) to obtain a connexive variant of Nelson’s three-valued logic **N3**, intuitionistic negation ¬ is definable by setting: ¬*A* := *A* → ~*A*. Then a5 might be replaced by

> a5′: ~(*A* → *B*) ↔ (*A* → ¬*B*).

The resulting system satisfies AT, AT′, BT, and BT′ because *A* → ¬~*A* and ~*A* → ¬*A* are theorems. For BT, for example, we have:

| 1. | *A* → *B* | assumption |
| --- | --- | --- |
| 2. | *B* → ¬~*B* | theorem |
| 3. | *A* → ¬~*B* | 1, 2, transitivity of → |
| 4. | (*A* → ¬~*B*) → ~(*A* → ~*B*) | axiom a5′ |
| 5. | ~(*A* → ~*B*) | 3, 4, R1 |
| 6. | (*A* → *B*) → ~(*A* → ~*B*) | 1, 5, deduction theorem |

This logic, however, is the trivial system consisting of every *L*-formula (a fact not noticed in Wansing 2005 (Section 6) but pointed out in the online version of that paper).

The system **C** is a conservative extension of positive intuitionistic logic. In **C**, strong negation is interpreted in such a way that it turns the intuitionistic implication of its negation-free sublanguage into a connexive implication. Analogously, strong negation may be added to positive dual intuitionistic logic to obtain a system with a connexive co-implication, and to bi-intuitionistic logic, or to the logic **2Int** from Wansing 2016a that also contains an implication and a co-implication connective, to obtain systems with both a connexive implication and a connexive co-implications, see Wansing 2008, 2016b, and Kamide and Wansing 2016.

The systems **C** and **QC** are connexive but not Kapsner strong. This is hardly surprising because these logics are paraconsistent and allow formulas *A* and ~*A* to be simultaneously satisfiable in the sense that a state and all its possible expansions may support the truth of both *A* and ~*A*. As a result, *A* → ~*A* and ~*A* → *A* are satisfiable. If *A* → ~*A* and ~*A* → *A* are unsatisfiable, strong connexivity is in conflict with at the same time satisfying the deduction theorem and defining semantical consequence as preservation of support of truth: *A* → ~*A* would entail ~(*A* → ~*A*), ~*A* → *A* would entail ~(~*A* → *A*), and the formulas (*A* → ~*A*) → ~(*A* → ~*A*) and (~*A* → *A*) → ~(~*A* →*A*) would be valid instead of unsatisifable.

#### 4.5.2 **FDE**-based connexive relevance logic

The starting point for Hitoshi Omori’s (2016a) definition of a connexive extension of the basic relevance logic **BD** (see the entry logic: relevance) is to find a proof theory for extensions of **BD** with negation treated according to the American Plan. Priest and Sylvan (1992) posed this as an open problem, and Omori gives a partial solution by defining a connexive variant **BDW** of **BD**. The semantics uses models based on ternary frames. There is a base state *g*, the four truth values are represented as subsets of the set of classical truth values {0,1}, and interpretations are defined in the style of Dunn (cf. Omori and Wansing 2017)[^omori-2017][^wansing-2017]. A model is quadruple <*g*, *W*, *R*, *I*>, where *W* is a non-empty set (of states), *g*∈*W*, *R* is a three-place relation on *W* with *Rgxy* iff *x* = *y*, and *I* is a function that maps pairs consisting of a state and a propositional variable to subsets of {0,1}. The interpretation function *I* is then extended to an assignment of truth values at states for all formulas as follows:

> 1 ∈ *I*(*w*, ~*A*) iff 0 ∈ *I*(*w*, *A*)
> 0 ∈ *I*(*w*, ~*A*) iff 1 ∈ *I*(*w*, *A*)
> 1 ∈ *I*(*w*, *A* ∧ *B*) iff [1 ∈ *I*(*w*, *A*) and 1 ∈ *I*(*w*, *B*)]
> 0 ∈ *I*(*w*, *A* ∧ *B*) iff [0 ∈ *I*(*w*, *A*) or 0 ∈ *I*(*w*, *B*)]
> 1 ∈ *I*(*w*, *A* ∨ *B*) iff [1 ∈ *I*(*w*, *A*) or 1 ∈ *I*(*w*, *B*)]
> 0 ∈ *I*(*w*, *A* ∨ *B*) iff [0 ∈ *I*(*w*, *A*) and 0 ∈ *I*(*w*, *B*)]
> 1 ∈ *I*(*w*, *A* → *B*) iff for all *x*, *y* ∈ *W*: if *Rwxy* and 1 ∈ *I*(*x*, *A*), then 1 ∈ *I*(*y*, *B*)
> 0 ∈ *I*(*w*, *A* → *B*) iff for all *x*, *y* ∈ *W*: if *Rwxy* and 1 ∈ *I*(*x*, *A*), then 0 ∈ *I*(*y*, *B*)

An axiomatization of **BDW** is obtained from the axiom system for **BD** by adding BTe′. Like the constructive connexive logic **C**, the connexive relevance logic **BDW** is negation inconsistent but non-trivial.

#### 4.5.3 Material connexive logic

Adding *ex contradictione quodlibet* to system **C** has a trivializing effect, and adding the Law of Excluded Middle to **C** does not result in a logic that has positive classical propositional logic as a fragment. However, if implications *A* → *B* are understood as material, Boolean implications, then a separate treatment of falsity conditions again allows introducing a system of connexive logic. The resulting system **MC** may be called a system of material connexive logic. The semantics is quite obvious: a model M is just a function from the set of all literals, i.e., propositional variables or negated propositional variables, into the set of classical truth values {1, 0}. Truth of a formula *A* in a model M (M ⊨ *A*) is inductively defined as follows:

> M ⊨ *p* iff *v*(*p*) = 1
> M ⊨ (*A* ∧ *B*) iff M ⊨ *A* and M ⊨ *B*
> M ⊨ (*A* ∨ *B*) iff M ⊨ *A* or M ⊨ *B*
> M ⊨ (*A* → *B*) iff M ⊭ *A* or M ⊨ *B*
>
> M ⊨ ~*p* iff *v*(~*p*) = 1
> M ⊨ ~~*A* iff M ⊨ *A*
> M ⊨ ~(*A* ∧ *B*) iff M ⊨ ~*A* or M ⊨ ~*B*
> M ⊨ ~(*A* ∨ *B*) iff M ⊨ ~*A* and M ⊨ ~*B*
> M ⊨ ~(*A* → *B*) iff M ⊭ *A* or M ⊨ ~*B*

A formula is valid iff it is true in all models. (Alternatively, one could use the semantics of **C** and require the set of states of a frame to be a singleton.) The set of all valid formulas is axiomatized by the following set of axiom schemata and rules:

| a1_{c} | the axioms of classical positive logic |
| --- | --- |
| a2 | ~~*A* ↔ *A* |
| a3 | ~(*A* ∨ *B*) ↔ (~*A* ∧ ~*B*) |
| a4 | ~(*A* ∧ *B*) ↔ (~*A* ∨ ~*B*) |
| a5 | ~(*A* → *B*) ↔ (*A* → ~*B*) |
|   |   |
| R1 | modus ponens |

The logic **MC** can be faithfully embedded into positive classical logic, whence **MC** is decidable. The following truth tables for **MC**, while considering a language with a classical negation, resulting in a system called “dialetheic Belnap Dunn Logic,” **dBD**, are given in Omori 2016c:

| <table class="cell-center cellpad-small-dense all-rules vert-top grayborder avoid-break"> <tbody> <tr> <td>~</td> <td>&nbsp;</td> </tr> <tr> <td>T</td> <td>F</td> </tr> <tr> <td>B</td> <td>B</td> </tr> <tr> <td>N</td> <td>N</td> </tr> <tr> <td>F</td> <td>T</td> </tr> </tbody> </table> | <table class="cell-center cellpad-small-dense all-rules vert-top grayborder avoid-break"> <tbody> <tr> <td>&and;</td> <td>T</td> <td>B</td> <td>N</td> <td>F</td> </tr> <tr> <td>T</td> <td>T</td> <td>B</td> <td>N</td> <td>F</td> </tr> <tr> <td>B</td> <td>B</td> <td>B</td> <td>F</td> <td>F</td> </tr> <tr> <td>N</td> <td>N</td> <td>F</td> <td>N</td> <td>F</td> </tr> <tr> <td>F</td> <td>F</td> <td>F</td> <td>F</td> <td>F</td> </tr> </tbody> </table> |
| --- | --- |
| <table class="cell-center cellpad-small-dense all-rules vert-top grayborder avoid-break"> <tbody> <tr> <td>&or;</td> <td>T</td> <td>B</td> <td>N</td> <td>F</td> </tr> <tr> <td>T</td> <td>T</td> <td>T</td> <td>T</td> <td>T</td> </tr> <tr> <td>B</td> <td>T</td> <td>B</td> <td>T</td> <td>B</td> </tr> <tr> <td>N</td> <td>T</td> <td>T</td> <td>N</td> <td>N</td> </tr> <tr> <td>F</td> <td>T</td> <td>B</td> <td>N</td> <td>F</td> </tr> </tbody> </table> | <table class="cell-center cellpad-small-dense all-rules vert-top grayborder avoid-break"> <tbody> <tr> <td>&rarr;</td> <td>T</td> <td>B</td> <td>N</td> <td>F</td> </tr> <tr> <td>T</td> <td>T</td> <td>B</td> <td>N</td> <td>F</td> </tr> <tr> <td>B</td> <td>T</td> <td>B</td> <td>N</td> <td>F</td> </tr> <tr> <td>N</td> <td>B</td> <td>B</td> <td>B</td> <td>B</td> </tr> <tr> <td>F</td> <td>B</td> <td>B</td> <td>B</td> <td>B</td> </tr> </tbody> </table> |

The formula ~(*A* → *B*) → (*A* ∧ ~*B*) is, of course, not a theorem of **MC**. Like **C**, **MC** is a paraconsistent logic containing contradictions. The connexive logic **MC** differs from the four-valued logic **HBe** presented in Avron 1991 by making use of the above clause that guarantees the validity of BTe′, i.e.,

> M ⊨ ~(*A* → *B*) iff M ⊭ *A* or M ⊨ ~*B*

instead of the clause

> M ⊨ ~(*A* → *B*) iff M ⊨ *A* and M ⊨ ~*B*.

As already mentioned, Cantwell’s three-valued connexive logic **CN** can be obtained by extending **MC** with the Law of Excluded Middle and, semantically, by requiring that for every propositional variable *p* and every model M, M ⊨ *p* or M ⊨ ~*p*. There is another three-valued connexive logic that is strictly stronger than **CN**, namely the “dialetheic Logic of Paradox,” **dLP**, studied in Omori 2016c, which turned out to be equivalent with the system **LImp** from Olkhovikov 2002 (published in English translation in 2016). Whilst Olkhovikov uses a unary operator L, understood as a kind of necessity operator, in the language of **LImp**, Omori uses a unary consistency operator, ○, in the language of **dLP**. The connective L is definable in **dLP**, and the connective ○ is definable in **LImp**. It is shown in Omori 2016c that **dLP** is inconsistent, definitionally complete, and Post complete. Both, Omori (2016c) and Olkhovikov (2016) consider a first-order extension of **dLP**, respectively **LImp**.

#### 4.5.4 Connexive conditional logic

It is quite natural to obtain an **FDE**-based connexive logic by starting form David Nelson’s logic **N4** because the latter system’s intuitionistic implication is the weakest conditional satisfying modus ponens and the deduction theorem. The conditionals studied within conditional logic in the tradition of Robert Stalnaker and David Lewis, where the conditional is usually written as ‘□→’, are much weaker than intuitionistic or relevant implication. The project of taking the basic system of conditional logic **CK** introduced by Brian Chellas (1975) as the point of departure for obtaining connexive conditional logics has been carried out in Wansing and Unterhuber 2019, and a similar approach is considered in Kapsner and Omori 2017. Whereas the semantics for the Lewis-Nelson models from Kapsner and Omori 2017 uses binary relations *R_{A}* on a non-empty set of states, for every formula *A*, the Chellas-Segerberg semantics employed in Wansing and Unterhuber 2019 uses binary relations *R_{X}* on a non-empty set of states, for subsets *X* of the set of all states. Both versions of the semantics can be equipped with sound and complete tableau calculi (although Kapsner and Omori only present the models), but the Chellas-Segerberg semantics is suitable for developing a purely structural correspondence theory in terms of properties of relations that are language-independent insofar as they are not relativized to a formula.

A pair <*W*, *R*> is a *Chellas frame* (or just a frame) iff *W* is a non-empty set, intuitively understood as a set of information states, and *R* ⊆ *W* × *W* × ℘(*W*), where ℘( *W*) is the powerset of *W*. Instead of *Rww*′ *X* one usually writes *wR*_{*X*}*w*′. Let *W*, *R* be a frame such that for all *X* ⊆ *W* and *w*, *w*′ ∈ *W*, *wR*_{*X*}*w*′ implies *w*′ ∈ *X*. Then M = <*W*, *R*, *v*⁺, *v*^{−}> is a model for the connexive conditional logic **CCL** iff *v*⁺ and *v*^{−} are valuation functions from the set of propositional variables into ℘( *W*), the support of truth and support of falsity conditions for propositional variables, negated formulas, conjunctions, and disjunctions are defined as in the case of **C**-models and, moreover,

> M, *w* ⊨⁺ (*A* □→ *B*) iff for all *u* ∈ *W* such that *wR*_{[[*A*]]}*u* it holds that M, *u* ⊨⁺ *B*
> M, *w* ⊨^{−} (*A* □→ *B*) iff for all *u* ∈ *W* such that *wR*_{[[*A*]]}*u* it holds that M, *u* ⊨^{−} *B*,

where [[*A*]] is the set of states that support the truth of *A*.

If <*W*, *R*> is a *Chellas frame*, a triple <*W*, *R*, *P*> is said to be a *Segerberg frame* (or a general frame) for **CCL** if *P* is a binary relation on ℘(*W*) that satisfies certain closure conditions. A quintuple M = <*W*, *R*, *P*, *v*⁺, *v*^{−}> then is a general model for **CCL** if <*W*, *R*, *P*> is a general frame for **CCL**, <*W*, *R*, *v*⁺, *v*^{−}> is a model for **CCL**, and for every propositional variable *p*, [[*p*]],[[~*p*]] ∈ *P*. The closure conditions on *P* are exactly the conditions guaranteeing that for every formula *A*, [[*A*]],[[~*A*]] ∈ *P* if for every propositional variable *p*, [[*p*]],[[~*p*]] ∈ *P*. If [[*A*]],[[~*A*]] is seen as the proposition expressed by *A*, then a general model for **CCL** is rich enough to guarantee that every proposition expressed by a formula is available. This is needed for a purely structural correspondence theory. The formula *A* □→ *A*, for example, is valid on a general frame iff it satisfies the frame condition:

> C_{*A* □→ *A*}: For all *X* ⊆ *W* and *w*, *w*′ ∈ *W*, *wR*_{*X*}*w*′ implies *w*′ ∈ *X*.

General frames for **CCL** are required to satisfy condition C_{*A* □→ *A*} in order to make sure that Boethius’ theses are indeed validated. In Unterhuber and Wansing 2019 sound and complete tableau calculi are presented for **CCL** and the weaker system **cCL** that validates Aristotle’s theses but not Boethius’ theses and that is obtained by giving up C_{*A* □→ *A*}. In Wansing and Unterhuber 2019 these results are then extended to systems that are obtained by adding a constructive implication to the language of **cCL** and **CCL**.

McCall (2012) classifies the principles he calls *Abelard’s First Principle* and *Aristotle’s Second Thesis* (cf. section 2) as connexive principles. In Wansing and Skurt 2018 it is argued that since Aristotle’s Second Thesis and Abelard’s First Principle both involve conjunction, one may think of obtaining motivation for them from the idea of negation as cancellation and from the failure of Simplification as justified by the erasure model of negation. Like the other connexive logics considered in the present section, **CCL** is a system in which Abelard’s First Principle and Aristotle’s Second Thesis fail to be valid.

### 4.6 Connexive modal logics

There is a growing literature on modal extensions of connexive logics. In Wansing 2005, the language of the connexive logic **C** is extended by modal operators □ and ◊ (“it is possible that”) to define a connexive and constructive analogue **CK** of the smallest normal modal logic **K**. The system **CK** is shown to be faithfully embeddable into **QC**, to be decidable, and to enjoy the disjunction property and the constructible falsity property.

It is well-known that intuitionistic propositional logic can be faithfully embedded into the normal modal logic **S4**, which, like **K**, is based on classical propositional logic (cf. the entries logic: intuitionistic and logic: modal). There exists a translation γ, due to Gödel, such that a formula *A* of intuitionistic logic is intuitionistically valid iff *A*’s γ-translation is valid in **S4**. In particular, intuitionistic implication is understood as strict material implication: γ(*A* → *B*) = □(γ(*A*) ⊃ γ(*B*)). Kamide and Wansing (2011) define a sequent calculus for connexive **S4** based on **MC**. This system, **CS4**, is shown to be complete with respect to a relational possible worlds semantics. The proof uses a faithful embedding of **CS4** into positive, negation-free **S4**. Moreover, it is shown that the cut-rule is an admissible rule in **CS4** and that the constructive connexive logic **C** stand to **CS4** as intuitionistic logic stands to **S4**. In the faithful embedding, the modal translation of negated implications is as expected: γ(~(*A* → *B*)) = □(γ(*A*) ⊃ γ(*~B*)). A similar translation is used in Odintsov and Wansing 2010 to embed **C** into a modal extension **BS4** of Belnap and Dunn’s four-valued logic.

In **CS4** the modal operators □ and ◊ are syntactic duals of each other: the equivalence between □*A* and ~◊~*A* and between ◊*A* and ~□~*A* is provable. Kamide and Wansing (2011) also present a cut-free sequent calculus for a connexive constructive version **CS4**^{*d–*} of **S4** without syntactic duality between □ and ◊. The relational possible worlds semantics for **CS4**^{*d–*} is not fully compositional, cf. Odintsov and Wansing 2004. **CS4**^{*d–*} is faithfully embeddable into positive **S4** and decidable. Moreover **C** is faithfully embeddable into **CS4**^{*d–*}.

Modal Boolean connexive relatedness logics are investigated in Jarmużek and Malinowski 2019b, a modal extension of a “bi-classical” paraconsistent connexive logic is introduced in Kamide 2019, and connexive variants of various modal extensions of **FDE** that are extensions of **MC** are studied in Odintsov, Skurt, and Wansing 2019.

## 5. Connexive logics and consequential logics

Aristotle’s and Boethius’ theses express, as it seems, some pre-theoretical intuitions about meaning relations between negation and implication. But it is not clear that a language must contain only one negation operation and only one implication. The language of bi-intuitionistic logic contains two negations, the language of the bi-intuitionistic connexive logics in Wansing 2016b and Kamide & Wansing 2016 contain three negations, and the language of systems of *consequential implication* comprises two implication connectives together with one negation, see Pizzi 1977, 1991, 1993, 1996, 1999, 2004, 2005, 2008, 2018, Pizzi and Williamson 1997, 2005. Pizzi (2008, p. 127) considers a notion of *consequential relevance*, namely that “[t]he antecedent and the consequent of a true conditional cannot have incompatible modal status,” and suggests to capture consequential relevance by requiring that in any true conditional *A* → *B*, (i) *A* strictly implies *B* and (ii) *A* and *B* have the same modal status in the sense that □*A* ⊃ □*B*, □*B* ⊃ □*A*, ◊*A* ⊃ ◊*B*, and ◊*B* ⊃ ◊*A* are ture, where ⊃ is material implication. Moreover, it is required that □*A* ⊃ ◊*A* is always true.

In Pizzi and Williamson 1997, a conditional satisfying (i) and (ii) is called an *analytic consequential implication* and the notion of a normal system of analytic consequential implication is defined. ‘Normal’ here means that such a system contains certain formulas and is closed under certain rules. The smallest normal consequential logic that satisfies AT is called **CI**. Alternatively, **CI** can be characterized as the smallest normal system that satisfies the Weak Boethius’ Thesis, i.e, (*A* → *B*) ⊃ ¬(*A* → ¬*B*), where → is consequential implication and ¬ is classical negation. In Omori and Wansing 2019 the semantics of **CI** is presented in a way showing that the semantics of the consequential conditional is obtained by tweaking the truth conditions of strict implication in Kripke models with a serial accessibility relation (so that □*A* ⊃ ◊*A* is valid). The standard truth conditions are supplemented by requiring equal modal status for the antecedent and the consequent.

Pizzi and Williamson (1997) show that **CI** can be faithfully embedded into the normal modal logic **KD**, and vice versa. Analytic consequential implication is interpreted according to the following translation function φ:

> φ(*A* → *B*) = □(φ*A* ⊃ φ*B*) ∧ (□φ*B* ⊃ □φ*A*) ∧ (◊φ*B* ⊃ ◊φ*A*)

As Pizzi and Williamson (1997, p. 571) point out, their investigation is a “contribution to the modal treatment of logics intermediate between logics of consequential implication and connexive logics.” They emphasize a difficulty of regarding consequential implication as a genuine implication connective by showing that in any normal system of consequential logic that admits modus ponens for consequential implication and contains BT, the following formulas are provable:

> (a) (*A* → *B*) ≡ (*B →* *A*),
> (b) (*A* → *B*) ≡ ¬(*A* → ¬*B*)

where ≡ is classical equivalence. Since (*A* → *B*) ↔ ~(*A* → ~*B*) is a theorem of **C** and other connexive logics, the more problematic fact, from the point of view of this system, is the provability of (a). Pizzi and Williamson also show that in any normal system of consequential logic that contains BT, the formula (*A* → *B*) ≡ (*A* ≡ *B*) is provable if (*A* → *B*) ⊃ (*A* ⊃ *B*) is provable, in other words, consequential implication collapses into classical equivalence if (*A* → *B*) ⊃ (*A* ⊃ *B*) is provable. The construction of Aristotelian squares of opposition and their combination to Aristotelian cubes in systems of consequential implication is considered in Pizzi 2008. Two kinds of consequential implication are discussed and compared to each other in Pizzi 2018.

## 6. Summary

In summary, it may be said that connexive logic, although it is contra-classical and unusual in various respects, is not just a formal game or gimmick. There are several kinds of systems of connexive logics with different kinds of semantics and proof systems, and in the 21st century the subject has been experiencing a renaissance. The intuitions captured by systems of connexive logic can be traced back to ancient roots, and applications of connexive logics range from Aristotle’s syllogistic to Categorial Grammar, the study of causal implications, and connexive mathematics.

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=logic-connexive). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/logic-connexive/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=logic-connexive&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/logic-connexive/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

- Angell, R.B., 1966, “[Three logics of subjunctive conditionals](http://www.rbangell.com/pdf/papers-articles/Three%20Logics%20of%20Subjunctive%20Conditionals%20%20001.PDF),” paper presented August 12, 1966 at Colloquium on Logic and Foundations of Mathematics, Hannover, Germany.
- Estrada-González, L., 2019, “[The Bochum Plan and the Foundations of Contra-Classical Logics](https://www.cle.unicamp.br/eprints/index.php/CLE_e-Prints/about),” CLE e-Prints.
- Vidal, M., 2017, “[When Conditional Logic met Connexive Logic](https://www.semanticscholar.org/paper/When-Conditional-Logic-met-Connexive-Logic-Vidal/f09b43946aecc562120f8cdb4e23f94498a1b43a),” IWCS 2017 – 12th International Conference on Computational Semantics.
- *IfCoLog Journal of Logics and their Applications*, Vol. (3), No 3 (2016), “[Special Issue: Connexive Logics](https://www.collegepublications.co.uk/ifcolog/?00007).”
- *Logic and Logical Philosophy*, Vol. 28, No 3 (2019), “[Special Issue: Advances in Connexive Logic](https://apcz.umk.pl/czasopisma/index.php/LLP/issue/view/1613/showToc).”
- [The connexive logic website](https://sites.google.com/site/connexivelogic/home). This is a website for everyone interested in connexive logic, collecting information about events on connexive logic and keeping an updated list of publications related to connexive logic.

## Related Entries

Abelard [Abailard], Peter | Aristotle, General Topics: logic | Boethius, Anicius Manlius Severinus | conditionals | conditionals: counterfactual | grammar: typelogical | Kilwardby, Robert | logic: classical | logic: conditionals | logic: intuitionistic | logic: many-valued | logic: modal | logic: paraconsistent | logic: relevance | negation

## Acknowledgments

The author would like to thank Hitoshi Omori for many stimulating discussions on connexive logic and comments on a draft version of this entry, Wolfgang Lenzen for making available an excerpt from Boethius’ *De Syllogismo Hypothetico*, and Hans Rott and Andreas Kapsner for some helpful remarks.

[^almukdad-1984]: Almukdad A. and Nelson, D., 1984, “Constructible Falsity and Inexact Predicates”, *Journal of Symbolic Logic*, 49: 231–233.

[^anderson-1975]: Anderson, A.R. and Belnap, N.D., 1975, *Entailment: The Logic of Relevance and Necessity, Volume I*, Princeton: Princeton University Press.

[^angell-1962]: Angell, R.B., 1962, “A Propositional Logic with Subjunctive Conditionals”, *Journal of Symbolic Logic*, 27: 327–343.

[^angell-1967a]: –––, 1967a, “Three Logics of Subjunctive Conditionals (Abstract)”, *Journal of Symbolic Logic*, 32: 297–308.

[^angell-1967b]: –––, 1967b, “Connexive Implication, Modal Logic and Subjunctive Conditionals”, lecture delivered in Chicago, 5 May 1967, *IfCoLog Journal of Logics and their Applications*, 2016, 3: 297–308.

[^angell-1978]: –––, 1978, “Tre logiche dei condizionali congiuntivi”, in: C. Pizzi (ed), *Leggi di natura, modalità, ipotesi. La logica del ragionamento controfattuale*, Milan: Feltrinelli, 156–180; Italian translation of Angell 1966, see Other Internet Resources.

[^angell-2002]: –––, 2002, *A-Logic*, Lanham: University Press of America.

[^arieli-1996]: Arieli, O. and Avron, A., 1996, “Reasoning with Logical Bilattices”, *Journal of Logic, Language and Information*, 5: 25–63

[^avron-1991]: Avron, A., 1991, “Natural 3-valued Logics–Characterization and Proof Theory”, *Journal of Symbolic Logic*, 56: 276–294.

[^belnap-1970]: Belnap, N.D., 1970, “Conditional Assertion and Restricted Quantification”, *Noûs*, 4: 1–13.

[^bennett-2003]: Bennett, J., 2003, *A Philosophical Guide to Conditionals*, Oxford: Clarendon Press.

[^besnard-2011]: Besnard, P., 2011, “A Logical Analysis of Rule Inconsistency”, *International Journal of Semantic Computing*, 5: 271–280.

[^bode-1979]: Bode, J., 1979, “The Possibility of a Conditional Logical ”, *Notre Dame Journal of Formal Logic*, 20: 147–154.

[^boethius-1860]: Boethius, A.M.S., 1860, *De Syllogismo Hypothetico*, J.P. Migne (ed.), Patrologia Latina 64, Paris, 831–876.

[^brady-1989]: Brady, R., 1989, “A Routley-Meyer Affixing Style Semantics for Logics Containing Aristotle’s Thesis”, *Studia Logica*, 48: 235–241.

[^cantwell-2008]: Cantwell, J., 2008, “The Logic of Conditional Negation”, *Notre Dame Journal of Formal Logic*, 49: 245–260.

[^chellas-1975]: Chellas, B., 1975, “Basic Conditional Logic”, *Journal of Philosophical Logic*, 4: 133–153.

[^cooper-1968]: Cooper, W., 1968, “The Propositional Logic of Ordinary Discourse”, *Inquiry*, 11: 295–320.

[^el-rouayheb-2009]: El-Rouayheb, K., 2009, “Impossible Antecedents and Their Consequences: Some Thirteenth- Century Arabic Discussions”, *History and Philosophy of Logic* 30: 209–225.

[^egré-2013]: Egré, P. and Politzer, G., 2013, “On the negation of indicative conditionals”, in: M. Franke, M. Aloni and F. Roelofsen (eds), *Proceedings of the 19th Amsterdam Colloquium*, 10–18 [[Egré & Politzer 2013 available online](http://maloni.humanities.uva.nl/AC2013/AC_proceedings.pdf)].

[^estrada-gonzález-2008]: Estrada-González, L., 2008, “Weakened Semantics and the Traditional Square of Opposition”, *Logica Universalis*, 2: 155–165.

[^estrada-gonzález-2016]: Estrada-González, L. and Ramirez-Cámara, E., 2016, “A Comparison of Connexive Logics”, *IfCoLog Journal of Logics and their Applications*, 3: 341–355.

[^estrada-gonzález-2020]: –––, 2020, “A Nelsonian Response to ‘the Most Embarrassing of All Twelfth-century Arguments’”, *History and Philosophy of Logic*, 41: 101–113.

[^ferguson-2014]: Ferguson, T.M., 2014, “Ramsey’s Footnote and Priest’s Connexive Logics”, abstract, ASL Logic Symposium 2012, *Bulletin of Symbolic Logic*, 20: 387–388.

[^ferguson-2015]: –––, 2015, “Logics of Nonsense and Parry Systems”, *Journal of Philosophical Logic*, 44: 65–80.

[^ferguson-2016]: –––, 2016, “On Arithmetic Formulated Connexively”, *IfCoLog Journal of Logics and their Applications*, 3: 357–376.

[^ferguson-2019]: –––, 2019, “Inconsistent Models (and Infinite Models) for Arithmetics with Constructible Falsity”, *Logic and Logical Philosophy*, 28: 389–407.

[^fine-1986]: Fine, K., 1986, “Analytic Implication”, *Notre Dame Journal of Formal Logic*, 27: 169–179.

[^francez-2016]: Francez, N., 2016, “Natural Deduction for Two Connexive Logics”, *IfCoLog Journal of Logics and their Applications*, 3: 479–504.

[^francez-2019]: –––, 2019 “Relevant Connexive Logic”, *Logic and Logical Philosophy*, 28: 409–425.

[^francez-2020]: –––, 2020, “A Poly-Connexive Logic”, *Logic and Logical Philosophy*, 29: 143–157.

[^francez-2021]: –––, 2021, *A View of Connexive Logic*, London: College Publications.

[^gibbard-1981]: Gibbard, A. 1981, “Two Recent Theories of Conditionals”, in: W.L. Harper, R. Stalnaker, and C.T. Pearce (eds), *Ifs*, Dordrecht: Reidel.

[^gurevich-1977]: Gurevich, Y., 1977, “Intuitionistic Logic with Strong Negation”, *Studia Logica*, 36: 49–59.

[^humberstone-2000]: Humberstone, L., 2000, “Contra-Classical Logics”, *Australasian Journal of Philosophy*, 78(4): 438–474.

[^jarmużek-2019a]: Jarmużek, T. and Malinowski, J., 2019a, “Boolean Connexive Logics: Semantics and Tableau Approach”, *Logic and Logical Philosophy*, 28: 427–448.

[^jarmużek-2019b]: –––, 2019b, “Modal Boolean connexive logics. Semantic and tableau approach”, *Bulletin of the Section of Logic*, 48: 213–243.

[^johnson-1976]: Johnson, F.A., 1976, “A Three-valued Interpretation for a Relevance Logic”, *The Relevance Logic Newsletter*, 1: 123–128. [[Johnson 1976 available online](https://philarchive.org/rec/JOHATI-2).]

[^johnston-2019]: Johnston, S., 2019, “Per Se Modality and Natural Implication. An Account of Connexive Logic in Robert Kilwardby,” *Logic and Logical Philosophy*, 28: 449–479.

[^kamide-2016]: Kamide, N., 2016, “Cut-free Systems for Restricted Bi-intuitionistic Logic and its Connexive Extension”, *Proceedings of the 46th International Symposium on Multiple-Valued Logic (ISMVL)*, Sapporo, Japan, IEEE Computer Society, 137–142.

[^kamide-2017]: –––, 2017, “Natural Deduction for Connexive Paraconsistent Quantum Logic”, *Proceedings of the 47th International Symposium on Multiple-Valued Logic (ISMVL)*, Novi Sad, Serbia, IEEE Computer Society, 207–212.

[^kamide-2019]: –––, 2019, “Bi-Classical Connexive Logic and its Modal Extension: Cut-elimination, Completeness and Duality”, *Logic and Logical Philosophy*, 28: 481–511.

[^kamide-2011]: Kamide, N. and Wansing, H., 2011, “Connexive Modal Logic Based on Positive S4”, in: J.-Y. Beziau and M. Conigli (eds), *Logic without Frontiers. Festschrift for Walter Alexandre Carnielli on the Occasion of His 60th Birthday*, London: College Publications, 389–409.

[^kamide-2012]: –––, 2012, “Proof theory of Nelson’s Paraconsistent Logic: A Uniform Perspective”, *Theoretical Computer Science*, 415: 1–38.

[^kamide-2016-2]: –––, 2016, “Completeness of connexive Heyting-Brouwer logic”, *IfCoLog Journal of Logics and their Applications*, 3: 441–466.

[^kamide-2017-2]: Kamide, N., Shramko. Y., and Wansing, H., 2017, “Kripke Completeness of Bi-intuitionistic Multilattice Logic and its Connexive Variant”, *Studia Logica*, 105: 1193–1219.

[^kapsner-2012]: Kapsner, A., 2012, “Strong Connexivity”, *Thought*, 1: 141–145.

[^kapsner-2019]: –––, 2019, “Humble Connexivity”, *Logic and Logical Philosophy*, 28: 513–536.

[^kapsner-2017]: Kapsner, A. and Omori, H., 2017, “Counterfactuals in Nelson Logic”, *Proceedings of LORI 2017*, Berlin: Springer, 497–511.

[^khemlani-2014]: Khemlani, S., Orenes, I., and Johnson-Laird, P.N., 2014, “The Negation of Conjunctions, Conditionals, and Disjunctions”, *Acta Psychologica*, 151: 1–7.

[^kneale-1957]: Kneale, W., 1957, “Aristotle and the Consequentia Mirabilis”, *The Journal of Hellenic Studies*, 77: 62–66.

[^kneale-1962]: Kneale, W. and Kneale, M., 1962, *The Development of Logic*, London: Duckworth.

[^lenzen-2019]: Lenzen, W., 2019, “Leibniz’s Laws of Consistency and the Philosophical Foundations of Connexive Logic”, *Logic and Logical Philosophy*, 28: 537–551.

[^lenzen-2020]: Lenzen, W., 2020, “A Critical Examination of the Historical Origins of Connexive Logic”, *History and Philosophy of Logic*, 41: 16–35.

[^lewis-1973]: Lewis, D., 1973, *Counterfactuals*, Oxford: Basil Blackwell.

[^lowe-1995]: Lowe, E.J., 1995, “The Truth about Counterfactuals”, *The Philosophical Quarterly*, 45: 41–59.

[^lowe-1951]: Łukasiewicz, J. 1951, *Aristotle’s Syllogistic from the Standpoint of Modern Formal Logic*, Oxford: Clarendon Press.

[^maccoll-1878]: MacColl, H., 1878, “The Calculus of Equivalent Statements (II)”, *Proceedings of the London Mathematical Society 1877–78*, 9: 177–186.

[^mares-2019]: Mares, E. and Paoli, F., 2019, “C.I. Lewis, E.J. Nelson, and the Modern Origins of Connexive Logic”, *Organon F*, 26: 405–426.

[^martin-1991]: Martin, C.J., 1991, “The Logic of Negation in Boethius”, *Phronesis*, 36: 277–304.

[^martin-2004]: –––, 2004, “Logic”, in: J. Brower and K. Guilfoy (eds), *The Cambridge Companion to Abelard*, Cambridge: Cambridge University Press, 158–199.

[^mccall-1963]: McCall, S., 1963, *Non-classical Propositional Calculi*, Ph.D. Dissertation, Oxford University.

[^mccall-1964]: ––– 1964, “A New Variety of Implication,” (abstract),*Journal of Symbolic Logic*, 29: 151–152.

[^mccall-1966]: –––, 1966, “Connexive Implication”, *Journal of Symbolic Logic*, 31: 415–433.

[^mccall-1967]: –––, 1967, “Connexive Implication and the Syllogism”, *Mind*, 76: 346–356.

[^mccall-1975]: –––, 1975, “Connexive Implication”, § 29.8 in: A.R. Anderson and N.D. Belnap, *Entailment. The Logic of Relevance and Necessity* (Volume 1), Princeton: Princeton University Press, 434–446.

[^mccall-2012]: –––, 2012, “A History of Connexivity”, in: D.M. Gabbay *et al*. (eds), *Handbook of the History of Logic. Volume 11. Logic: A History of its Central Concepts*, Amsterdam: Elsevier, 415–449.

[^mccall-2014]: –––, 2014, “Connexive Gentzen”, *Logic Journal of the IGPL*, 22: 964–981.

[^meyer-1977]: Meyer, R.K, 1977, “S5–The Poor Man’s Connexive Implication”, *The Relevance Logic Newsletter*, 2: 117–123. [[Meyer 1977 available online](http://aal.ltumathstats.com/curios/relevance-logic-newsletter).]

[^meyer-1986]: Meyer, R.K. and Martin, E.P., 1986, “Logic on the Australian Plan”, *Journal of Philosophical Logic*, 15: 305–332.

[^mortensen-1984]: Mortensen, C., 1984, “Aristotle’s Thesis in Consistent and Inconsistent Logics”, *Studia Logica*, 43: 107–116.

[^nasti-2002]: Nasti De Vincentis, M., 2002, *Logiche della connessività. Fra logica moderna e storia della logica antica*, Bern: Haupt. 2002.

[^nasti-2004]: –––, 2004, “From Aristotle’s Syllogistic to Stoic Conditionals: *Holzwege* or Detectable Paths?”, *Topoi*, 23: 113–37.

[^nasti-2006]: –––, 2006, “Conflict and Connectedness: Between Modern Logic and History of Ancient Logic”, in: E. Ballo and M. Franchella (eds), *Logic and Philosophy in Italy*, Monza: Polimetrica, 229–251.

[^nelson-1949]: Nelson, D., 1949, “Constructible Falsity”, *Journal of Symbolic Logic*, 14: 16–26.

[^nelson-1930]: Nelson, E.J., 1930, “Intensional Relations”, *Mind*, 39: 440–453.

[^nute-1980]: Nute, D., 1980, *Topics in Conditional Logic*, Dordrecht: Reidel.

[^odintsov-2008]: Odintsov, S., 2008, *Constructive Negations and Paraconsistency*, Dordrecht: Springer-Verlag.

[^odintsov-2019]: Odintsov S., Skurt, D. and Wansing, H., 2019, “Connexive variants of modal logics over FDE”, in: A. Zamansky and O. Arieli (eds), *Arnon Avron on Semantics ands Proof Theory of Non-Classical Logics*, Cham: Springer, 295–318.

[^odintsov-2004]: Odintsov S. and Wansing, H., 2004, “Constructive Predicate Logic and Constructive Modal Logic. Formal Duality versus Semantical Duality”, in: V. Hendricks *et al*. (eds.), *First-Order Logic Revisited*, Berlin: Logos Verlag, 269–286.

[^odintsov-2010]: –––, 2010, “Modal Logics with Belnapian Truth Values”, *Journal of Applied Non-Classical Logics*, 20: 279–301.

[^olkhovikov-2002]: Olkhovikov, G.K., 2002, “On a New Three-Valued Paraconsistent Logic”, in: *Logic of Law and Tolerance*, Yekaterinburg: Ural State University Press, 96–113, translated by T.M. Ferguson, *IfCoLog Journal of Logics and their Applications*, 3: 317–334.

[^olkhovikov-2016]: –––, 2016 “A Complete, Correct, and Independent Axiomatization of the First-Order Fragment of a Three-Valued Paraconsistent Logic”, *IfCoLog Journal of Logics and their Applications*, 3: 335–340.

[^omori-2016a]: Omori, H., 2016a, “A Simple Connexive Extension of the Basic Relevant Logic BD”, *IfCoLog Journal of Logics and their Applications*, 3: 467–478.

[^omori-2016b]: –––, 2016b, “A Note on Francez’ Half-Connexive Formula”, IfCoLog Journal of Logics and their Applications, 3: 505–512.

[^omori-2016c]: –––, 2016c, “From paraconsistent logic to dialetheic logic”, in: H. Andreas and P. Verdée (eds.), *Logical Studies of Paraconsistent Reasoning in Science and Mathematics*, Berlin: Springer, pp. 111–134.

[^omori-2019]: –––, 2019, “Towards a Bridge over Two Approaches in Connexive Logic”, *Logic and Logical Philosophy*, 28: 553–566.

[^omori-2015]: Omori H. and Sano, K., 2015, “Generalizing Functional Completeness in Belnap-Dunn Logic”, *Studia Logica*, 103: 883–917.

[^omori-2017]: Omori H. and Wansing, H., 2017, “40 years of FDE:An Introductory Overview”, *Studia Logica*, 105: 1021–1049.

[^omori-2018]: ––– 2018, “ On Contra-classical Variants of Nelson Logic N4 and its Classical Extension”, *Review of Symbolic Logic*, 11: 805–820.

[^omori-2019-2]: –––, 2019, “Connexive Logics. An Overview and Current Trends”, *Logic and Logical Philosophy*, 28: 371–387.

[^parry-1933]: Parry, W.T., 1933, “Ein Axiomensystem für eine neue Art von Implikation (analytische Implikation)”, *Ergebnisse eines mathematischen Kolloquiums*, 4: 5–6.

[^pfeifer-2012]: Pfeifer, N., 2012, “Experiments on Aristotle’s Thesis: Towards an experimental philosophy of conditionals”, *The Monist*, 95: 223–240.

[^pfeifer-2017]: Pfeifer, N. and Tulkki, L., 2017, “Conditionals, Counterfactuals, and Rational Reasoning. An Experimental Study on Basic Principles”, *Minds and Machines*, 27: 119–165.

[^pfeifer-2017-2]: Pfeifer, N. and Yama, H., 2017, “Counterfactuals, Indicative Conditionals, and Negation under Uncertainty: Are there Cross-cultural Differences?”, in: Gunzelmann, G., Howes, A., Tenbrink, T., and Davelaar, E. (eds), *Proceedings of the 39th Cognitive Science Society Meeting*, 2882–2887.

[^pizzi-1977]: Pizzi, C., 1977, “Boethius’ Thesis and Conditional Logic”, *Journal of Philosophical Logic*, 6: 283–302.

[^pizzi-1991]: –––, 1991, “Decision Procedures for Logics of Consequential Implication”, *Notre Dame Journal of Formal Logic*, 32: 618–636.

[^pizzi-1993]: –––, 1993, “Consequential Implication: A Correction”, *Notre Dame Journal of Formal Logic*, 34: 621–624.

[^pizzi-1996]: –––, 1996, “Weak vs. Strong Boethius’ Thesis: A Problem in the Analysis of Consequential Implication”, in: A. Ursini and P. Aglinanó (eds), *Logic and Algebra*, New York: Marcel Dekker, 647–654.

[^pizzi-1999]: –––, 1999, “A Modal Framework for Consequential Implication and the Factor Law”, *Contemporary Mathematics*, 313–326.

[^pizzi-2004]: –––, 2004, “Contenability and the Logic of Consequential Implication”, *Logic Journal of the IGPL*, 12: 561–579.

[^pizzi-2005]: –––, 2005, “Aristotle’s Thesis between Paraconsistency and Modalization”, *Journal of Applied Logic*, 3: 119–131.

[^pizzi-2008]: –––, 2008, “Aristotle’s Cubes and Consequential Implication”, *Logica Universalis*, 2: 143–153.

[^pizzi-2018]: –––, 2018 “Two Kinds of Consequential Implication”, *Studia Logica*, 106: 453–480.

[^pizzi-1997]: Pizzi, C. and Williamson, T., 1997, “Strong Boethius’ Thesis and Consequential Implication”, *Journal of Philosophical Logic*, 26: 569–588.

[^pizzi-2005-2]: –––, 2005, “Conditional Excluded Middle in Systems of Consequential Implication”, *Journal of Philosophical Logic*, 34: 333–362.

[^priest-1999]: Priest, G., 1999, “Negation as Cancellation and Connexive Logic”, *Topoi*, 18: 141–148.

[^rahman-2001]: Rahman, S. and Rückert, H., 2001, “Dialogical Connexive Logic”, *Synthese*, 127: 105–139.

[^rahman-2008]: Rahman, S. and Redmond, J., 2008, “Hugh MacColl and the Birth of Logical Pluralism”, in D. Gabbay and J. Woods (eds.), *British Logic in the Nineteenth Century* (Handbook of the History of Logic: Volume 4), Amsterdam: Elsevier, 533–604.

[^ramsey-1929]: Ramsey, F.P., 1929, “General Propositions and Causality”, in: F. Ramsey, *Philosophical Papers*, H. A. Mellor (ed.), Cambridge: Cambridge University Press, 1990.

[^rooij-2019]: Rooij, R. van and Schulz, K. 2019, “Conditionals, causality and conditional probability”, *Journal of Logic, Language and Information*, 28: 55–71.

[^rooij-2020]: –––, 2020, “Generics and typicality: A bounded rationality approach”, *Linguistics and Philosophy*, 43: 88–117.

[^routley-1974]: Routley, R., 1974, “Semantical Analyses of Propositional Systems of Fitch and Nelson”, *Studia Logica*, 33: 283–298.

[^routley-1978]: –––, 1978, “Semantics for Connexive Logics. I”, *Studia Logica*, 37: 393–412.

[^routley-1982]: Routley, R., Meyer, R., Plumwood, V. and Brady, R., 1982, *Relevant Logics and Their Rivals*, Atascadero, CA: Ridgeview Publishing Company.

[^routley-1968]: Routley, R. and Montgomery, H., 1968, “On Systems Containing Aristotle’s Thesis”, *Journal of Symbolic Logic*, 33: 82–96.

[^routley-1985]: Routley, R. and Routley V., 1985, “Negation and Contradiction”, *Revista Columbiana de Mathemáticas*, 19: 201–231.

[^sarenac-2003]: Sarenac, D. and Jennings, R.E., 2003, “The Preservation of Relevance”, *Eidos*, 17: 23–36.

[^schroeder-heister-2009]: Schroeder-Heister, P., 2009, “Sequent Calculi and Bidirectional Natural Deduction: on the Proper Basis of Proof-theoretic Semantics”, in: M. Peliš (ed), *The Logica Yearbook 2008*, London: College Publications, 237–251.

[^schurz-1998]: Schurz, G., 1998, “Relevance in Deductive Reasoning: a Critical Overview”, in: G. Schurz and M. Ursic (eds), *Beyond Classical Logic*, Conceptus-Studien, St. Augustin: Academia Verlag, 9–56.

[^stalnaker-1968]: Stalnaker, R. 1968, “A Theory of Conditionals”, in: N. Rescher (ed.), *Studies in Logical Theory* (American Philosophical Quarterly Monograph Series: Volume 2), Oxford: Blackwell, 98–112.

[^strawson-1952]: Strawson, P., 1952, *Introduction to Logical Theory*, Oxford: Oxford University Press.

[^sylvan-1989]: Sylvan, R., 1989, “A Preliminary Western History of Sociative Logics”, chapter 4 of *Bystanders’ Guide to Sociative Logics*, Research Series in Logic and Metaphysics #9, Australian National University, Canberra, published as chapter 5 of *Sociative Logics and their Applications. Essays by the Late Richard Sylvan*, D. Hyde and G. Priest (eds.), Aldershot: Ashgate Publishing, 2000.

[^thomason-1969]: Thomason, R., 1969, “A Semantical Study of Constructive Falsity”, *Zeitschrift für mathematische Logik und Grundlagen der Mathematik*, 15: 247–257.

[^thompson-1991]: Thompson, B., 1991, “Why is Conjunctive Simplification Invalid?”, *Notre Dame Journal of Formal Logic*, 32: 248–254.

[^unterhuber-2013]: Unterhuber, M., 2013, *Possible Worlds Semantics for Indicative and Counterfactual Conditionals. A Formal Philosophical Inquiry into Chellas-Segerberg Semantics*, Heusenstamm: Ontos Verlag.

[^urchs-1994]: Urchs, M., 1994, “On the Logic of Event-causation. Jaśkowski-style Systems of Causal Logic”, *Studia Logica*, 53: 551–578.

[^wagner-1991]: Wagner, G., 1991, Ex Contradictione Nihil Sequitur, in: *Proceedings IJCAI 1991*, San Francisco: Morgan Kaufmann, 538–543.

[^wansing-2001]: Wansing, H., 2001, “Negation”, in: L. Goble (ed.), *The Blackwell Guide to Philosophical Logic*, Cambridge, MA: Basil Blackwell Publishers, 415–436.

[^wansing-2005]: –––, 2005, “Connexive Modal Logic”, in R. Schmidt *et al*. (eds.), *Advances in Modal Logic. Volume 5*, London: King’s College Publications, 367–383. [[Wansing 2005 available online](http://www.aiml.net/volumes/volume5/).]

[^wansing-2007]: –––, 2007, “A Note on Negation in Categorial Grammar”, *Logic Journal of the Interest Group in Pure and Applied Logics*, 15: 271–286.

[^wansing-2008]: –––, 2008, “Constructive Negation, Implication, and Co-implication”, *Journal of Applied Non-Classical Logics*, 18: 341–364.

[^wansing-2016a]: –––, 2016a, “Falsification, natural deduction, and bi-intuitionistic logic”, *Journal of Logic and Computation*, 26 (2016): 425–450; first online 17 July 2013, doi:10.1093/logcom/ext035

[^wansing-2016b]: –––, 2016b, “Natural Deduction for Bi-Connexive Logic and a Two-Sorted Typed λ-Calculus”, *IfCoLog Journal of Logics and their Applications*, 3: 413–439.

[^wansing-2017]: –––, 2017, “A more general general proof theory”, *Journal of Applied Logic*, 25: 23–46.

[^wansing-nd]: Wansing, H., Omori, H. and Ferguson, T.M., “The Tenacity of Connexive Logic: Preface to the Special Issue”, *IfCoLog Journal of Logics and their Applications*, 3: 279–296.

[^wansing-2018]: Wansing, H. and Skurt, D., 2018, “Negation as Cancellation, Connexive Logic, and qLPm”, *Australasian Journal of Logic*, 15: 476–488.

[^wansing-2019]: Wansing, H. and Unterhuber, M., 2019, “Connexive Conditional Logic. Part I”, *Logic and Logical Philosophy*, 28: 567–610.

[^weiss-2019]: Weiss, Y., 2019, “Connexive Extensions of Regular Conditional Logic”, *Logic and Logical Philosophy*, 28: 611–627.

[^wiredu-1974]: Wiredu, J.E., 1974, “A Remark on a Certain Consequence of Connexive Logic for Zermelo’s Set Theory”, *Studia Logica*, 33: 127–130.

[^woods-1968]: Woods, J., 1968, “ Two Objections to System CC1 of Connexive Implication”, *Dialogue*, 7: 473–475.
