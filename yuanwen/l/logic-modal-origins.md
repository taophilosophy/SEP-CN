# Modern Origins of Modal Logic
**First published Tue Nov 16, 2010; substantive revision Fri Jun 25, 2021**

*Ballarin, Roberta*

Modal logic can be viewed broadly as the logic of different sorts of modalities, or modes of truth: alethic (“necessarily”), epistemic (“it is known that”), deontic (“it ought to be the case that”), or temporal (“it is always the case that”) among others. Common logical features of these operators justify the common label. In the strict sense however, the term “modal logic” is reserved for the logic of the alethic modalities, as opposed for example to temporal or deontic logic. From a merely technical point of view, any logic with non-truth-functional operators, including first-order logic, can be regarded as a modal logic: in this perspective the quantifiers too can be regarded as modal operators (as in Montague 1960)[^montague-1960]. Nonetheless, we follow the traditional understanding of modal logics as not including full-fledged first-order logic. In this perspective it is the modal operators that can be regarded as restricted quantifiers, ranging over special entities like possible worlds or temporal instants. Arthur Prior was one of the first philosophers/logicians to emphasize that the modal system **S5** can be translated into a fragment of first-order logic, which he called “the uniform monadic first-order predicate calculus” (Prior and Fine 1977: 56)[^prior-1977]. Monadic, since no relation between worlds needs to be stated for **S5**; and uniform as only one variable is needed to quantify over worlds (instants) when bound, and to refer to the privileged state (the actual world or the present time) when free (see Prior and Fine 1977)[^prior-1977]. Concerning the technical question of which model-theoretic features characterize modal logics understood as well-behaved fragments of first-order logic, see Blackburn and van Benthem’s “Modal Logic: A Semantic Perspective” (2007a).

The scope of this entry is the recent historical development of modal logic, strictly understood as the logic of necessity and possibility, and particularly the historical development of systems of modal logic, both syntactically and semantically, from C.I. Lewis’s pioneering work starting in 1912, with the first systems devised in 1918, to S. Kripke’s work in the early 1960s. In that short span of time of less than fifty years, modal logic flourished both philosophically and mathematically. Mathematically, different modal systems were developed and advances in algebra helped to foster the model theory for such systems. This culminated in the development of a formal semantics that extended to modal logic the successful first-order model theoretic techniques, thereby affording completeness and decidability results for many, but not all, systems. Philosophically, the availability of different systems and the adoption of the possible worlds model-theoretic semantics were naturally accompanied by reflections on the nature of possibility and necessity, on distinct sorts of necessities, on the role of the formal semantics, and on the nature of the possible worlds, to mention just a few. In particular, the availability of different systems brings to the fore the philosophical question of which modal logic is the correct one, under some intended interpretation of the modal operators, e.g., as logical or metaphysical necessity. Questions concerning the interpretability of modal logic, especially quantified modal logic, were insistently raised by Quine. All such questions are not pursued in this entry which is mostly devoted to the formal development of the subject. On Quine’s interpretative concerns see Ballarin 2021.

Modal logic is a rich and complex subject matter. This entry does not present a complete survey of all the systems developed and of all the model theoretic results proved in the lapse of time under consideration. It does however offer a meaningful survey of the main systems aiming to be useful to those looking for an historical outline of the subject matter that, even if not all-inclusive, delineates the most interesting model theoretic results and indicates further lines of exploration. Bull and Segerberg’s (1984: 3) useful division of the original sources of modal logic into three distinct traditions—syntactic, algebraic, and model theoretic—is adopted. For other less influential traditions, see Bull and Segerberg (1984: 16). See also Lindström and Segerberg’s “Modal Logic and Philosophy” (2007). The main focus of this entry is on propositional modal logic, while only some particular aspects of the semantics of quantified modal logic are briefly discussed. For a more detailed treatment of quantified modal logic, consult the SEP entry on modal logic. Concerning the entry’s notation, notice that $\Rightarrow$ is adopted in place of Lewis’s fishhook for strict implication, and $\Leftrightarrow$ for strict equivalence.

## 1. The Syntactic Tradition

In a 1912 pioneering article in *Mind* “Implication and the Algebra of Logic” C.I. Lewis started to voice his concerns on the so-called “paradoxes of material implication”. Lewis points out that in Russell and Whitehead’s *Principia Mathematica* we find two “startling theorems: (1) a false proposition implies any proposition, and (2) a true proposition is implied by any proposition” (1912: 522). In symbols:

$$\tag{1} \neg p \rightarrow(p \rightarrow q) $$

and

$$\tag{2} p \rightarrow(q \rightarrow p) $$

Lewis has no objection to these theorems in and of themselves:

> In themselves, they are neither mysterious sayings, nor great discoveries, nor gross absurdities. They exhibit only, in sharp outline, the meaning of “implies” which has been incorporated into the algebra. (1912: 522)

However, the theorems are inadequate *vis-à-vis* the intended meaning of “implication” and our actual modes of inference that the intended meaning tries to capture. So Lewis has in mind an intended meaning for the conditional connective $\rightarrow$ or $\supset$, and that is the meaning of the English word “implies”. The meaning of “implies” is that “of ordinary inference and proof” (1912: 531) according to which a proposition implies another proposition if the second can be logically deduced from the first. Given such an interpretation, (1) and (2) ought not to be theorems, thus propositional logic may be regarded as unsound *vis-à-vis* the reading of $\rightarrow$ as logical implication. Consider (2) for example: from the sheer truth of a proposition $p$ it does not (logically) follow that $p$ follows logically from any proposition whatsoever. Additionally, given the intended, strict reading of $\rightarrow$ as logical implication and the equivalence of $(\neg p\rightarrow q)$ and $(p\vee q)$, Lewis infers that disjunction too must be given a new intensional sense, according to which $(p\vee q)$ holds just in case if $p$ were not the case it would have to be the case that $q$.

Considerations of this sort, based on the distinction between extensional and intensional readings of the connectives, were not original to Lewis. Already in 1880 Hugh MacColl in the first of a series of eight papers on *Symbolical Reasoning* published in *Mind* claimed that $(p\rightarrow q)$ and $(\neg p\vee q)$ are not equivalent: $(\neg p\vee q)$ follows from $(p\rightarrow q)$, but not vice versa (MacColl 1880: 54)[^maccoll-1880]. This is the case because MacColl interprets $\vee$ as regular extensional disjunction, and $\rightarrow$ as intensional implication, but then from the falsity of $p$ or the truth of $q$ it does not follow that $p$ without $q$ is logically impossible. In the second paper of the series, MacColl distinguishes between certainties, possibilities and variable statements, and introduces Greek letters as indices to classify propositions. So $\alpha^{\varepsilon}$ expresses that *α* is a certainty, $\alpha^{\eta}$ that *α* is an impossibility, and $\alpha^{\theta}$ that *α* is a variable, i.e., neither a certainty nor an impossibility (MacColl 1897: 496–7)[^maccoll-1897]. Using this threefold classification of statements, MacColl proceeds to distinguish between causal and general implication. A causal implication holds between statements *α* and *β* if whenever *α* is true *β* is true, and *β* is not a certainty. A general implication holds between *α* and *β* whenever *α* and not$-\beta$ is impossible, thus in particular whenever *α* is an impossibility or *β* a certainty (1897: 498). The use of indices opened the door to the iteration of modalities, and the beginning of the third paper of the series (MacColl 1900: 75–6)[^maccoll-1900] is devoted to clarifying the meaning of statements with iterated indices, including *τ* for truth and *ι* for negation. So for example $A^{\eta \iota \varepsilon}$ is read as “It is certain that it is false that *A* is impossible” (note that the indices are read from right to left). Interestingly, Bertrand Russell’s 1906 review of MacColl’s book *Symbolic Logic and its Applications* (1906) reveals that Russell did not understand the modal idea of the variability of a proposition, hence wrongly attributed to MacColl a confusion between sentences and propositions, as Russell conferred variability only to sentences whose *meaning*, hence truth value, was not fixed. Similarly, certainty and impossibility are for Russell material properties of propositional functions (true of everything or of nothing) and not modal properties of propositions. It might be said that MacColl’s work came too early and fell on deaf ears. In fact, Rescher reports on Russell’s declared difficulty in understanding MacColl’s symbolism and, more importantly, argues that Russell’s view of logic had a negative impact on the development of modal logic (“Bertrand Russell and Modal Logic” in Rescher 1974: 85–96)[^rescher-1974]. Despite MacColl’s earlier work, Lewis can be regarded as the father of the syntactic tradition, not only because of his greater influence on later logicians, but especially for his development of various systems containing the new intensional connectives.

### 1.1 The Lewis Systems

In “The Calculus of Strict Implication” (1914) Lewis suggests two possible alternatives to the extensional system of Whitehead and Russell’s *Principia Mathematica*. One way of introducing a system of strict implication consists in eliminating from the system those theorems that, like (1) and (2) above, are true only for material implication but not for strict implication, thereby obtaining a sound system for both material and strict implication, though in neither case complete. The second, more fruitful alternative consists in introducing a new system of strict implication, still modeled on the Whitehead and Russell system of material implication, that will contain (all or a part of) extensional propositional logic as a proper part, but aspiring to completeness for at least strict implication. This second option is further developed in *A Survey of Symbolic Logic* (1918). There Lewis introduces a first system meant to capture the ordinary, strict sense of implication, guided by the idea that:

> Unless “implies” has some “proper” meaning, there is no criterion of validity, no possibility even of *arguing the question* whether there is one or not. And yet the question *What* is the “proper” meaning of “implies”? remains peculiarly difficult. (1918: 325)

The 1918 system takes as primitive the notion of impossibility $(\neg \Diamond)$, defines the operator of strict implication in its terms, and still employs an operator of intensional disjunction. However, Post will prove that this system leads to the collapse of necessity to truth—alternatively, of impossibility to falsity—since from one of its theorems $((p\Rightarrow q)\Leftrightarrow(\neg \Diamond q\Rightarrow \neg \Diamond p))$ it can be proved that $(\neg p\Leftrightarrow \neg \Diamond p)$. In 1920, “Strict Implication—An Emendation”, Lewis fixes the system substituting the weaker axiom $((p\Rightarrow q)\Rightarrow(\neg \Diamond q\Rightarrow \neg \Diamond p))$ for the old one. Finally, in Appendix II of the Lewis and Langford’s volume *Symbolic Logic* (1932: 492–502) “The Structure of the System of Strict Implication” the (weakened) 1918 system is given a new axiomatic base.

In the 1932 Appendix C.I. Lewis introduces five different systems. The modal primitive symbol is now the operator of possibility $\Diamond$, strict implication $(p\Rightarrow q)$ is defined as $\neg \Diamond(p\wedge \neg q)$, and $\vee$ is ordinary extensional disjunction. The necessity operator $\Box$ can also be introduced and defined, though Lewis does not, in the usual way as $\neg \Diamond \neg$.

Where $p, q$, and $r$ are propositional variables, System **S1** has the following axioms:

Axioms for **S1**

$$ \begin{align} \tag{B1} (p\wedge q)&\Rightarrow(q\wedge p) \\ \tag{B2} (p\wedge q)&\Rightarrow p \\ \tag{B3} p&\Rightarrow(p\wedge p) \\ \tag{B4} ((p\wedge q)\wedge r)&\Rightarrow(p\wedge(q\wedge r)) \\ \tag{B5} p&\Rightarrow \neg \neg p \\ \tag{B6} ((p\Rightarrow q)\wedge(q\Rightarrow r)) & \Rightarrow(p\Rightarrow r) \\ \tag{B7} (p\wedge(p\Rightarrow q)) & \Rightarrow q \\ \end{align} $$

Axiom B5 was proved redundant by McKinsey (1934)[^mckinsey-1934], and can thereby be ignored.

The rules are (1932: 125–6):

Rules for **S1**

*Uniform Substitution* A valid formula remains valid if a formula is uniformly substituted in it for a propositional variable.

*Substitution of Strict Equivalents* Either of two strictly equivalent formulas can be substituted for one another.

*Adjunction* If *Φ* and *Ψ* have been inferred, then $\Phi \wedge \Psi$ may be inferred.

*Strict Inference* If *Φ* and $\Phi \Rightarrow \Psi$ have been inferred, then *Ψ* may be inferred.

System **S2** is obtained from System **S1** by adding what Lewis calls “the consistency postulate”, since it obviously holds for $\Diamond$ interpreted as consistency:

$$\tag{B8} \Diamond(p\wedge q)\Rightarrow \Diamond p $$

System **S3** is obtained from system **S1** by adding the axiom:

$$\tag{A8} ((p\Rightarrow q)\Rightarrow(\neg \Diamond q\Rightarrow \neg \Diamond p)) $$

System **S3** corresponds to the 1918 system of *A Survey*, which Lewis originally considered the correct system for strict implication. By 1932, Lewis has come to prefer system **S2**. The reason, as reported in Lewis 1932: 496, is that both Wajsberg and Parry derived in system **S3**—in its 1918 axiomatization—the following theorem:

$$(p\Rightarrow q)\Rightarrow((q\Rightarrow r)\Rightarrow(p\Rightarrow r)),$$

which according to Lewis ought not to be regarded as a valid principle of deduction. In 1932 Lewis is not sure that the questionable theorem is not derivable in **S2**. Should it be, he would then adjudicate **S1** as the proper system for strict implication. However, Parry (1934)[^parry-1934] will later prove that neither A8 nor

$$(p\Rightarrow q)\Rightarrow((q\Rightarrow r)\Rightarrow(p\Rightarrow r))$$

can be derived in **S2**.

A further existence axiom can be added to all these systems:

$$\tag{B9} (\exists p, q)(\neg(p\Rightarrow q)\wedge \neg(p\Rightarrow \neg q)) $$

The addition of B9 makes it impossible to interpret $\Rightarrow$ as material implication, since in the case of material implication it can be proved that for any propositions $p$ and $q, ((p\rightarrow q)\vee(p\rightarrow \neg q))$ (1932: 179). From B9 Lewis proceeds to deduce the existence of at least four logically distinct propositions: one true and necessary, one true but not necessary, one false and impossible, one false but not impossible (1932: 184–9).

Following Becker (1930)[^becker-1930], Lewis considers three more axioms:

Three additional axioms

$$ \begin{align} \tag{C10} \neg \Diamond \neg p &\Rightarrow \neg \Diamond \neg \neg \Diamond \neg p\\ \tag{C11} \Diamond p & \Rightarrow \neg \Diamond \neg \Diamond p\\ \tag{C12} p&\Rightarrow \neg \Diamond \neg \Diamond p\\ \end{align} $$

System **S4** adds axiom C10 to the basis of **S1**. System **S5** adds axiom C11, or alternatively C10 and C12, to the basis of **S1**. Lewis concludes Appendix II by noting that the study of logic is best served by focusing on systems weaker than **S5** and not exclusively on **S5**.

Paradoxes of strict implication similar to those of material implication arise too. Given that strict implication $(p\Rightarrow q)$ is defined as $\neg \Diamond(p\wedge \neg q)$, it follows that an impossible proposition implies anything, and that a necessary proposition is implied by anything. Lewis argues that this is as it ought to be. Since impossibility is taken to be logical impossibility, i.e., ultimately a contradiction, Lewis argues that from an impossible proposition like $(p\wedge \neg p)$, both $p$ and $\neg p$ follow. From $p$ we can derive $(p\vee q)$, for any proposition $q$. From $\neg p$ and $(p\vee q)$, we can derive $q$ (1932: 250). The argument is controversial since one can argue that the principle $(p\Rightarrow(p\vee q))$ should not be a theorem of a system aiming to express ordinary implication (see, e.g., Nelson 1930: 447)[^nelson-1930]. Whatever the merits of this argument, those who disagreed with Lewis started to develop a logic of entailment based on the assumption that entailment requires more than Lewis’s strict implication. See, for example, Nelson 1930, Strawson 1948, and Bennett 1954. See also the SEP entry on relevance logic.

Notice that it was Lewis’s search for a system apt to express strict implication that made Quine reject modal systems as based on a use-mention confusion insofar as such systems were formulated to express at the object level proof-theoretic or semantic notions like consistency, implication, derivability and theoremhood (in fact, whenever $p\rightarrow q$ is a propositional theorem, system **S1**, and so all the other stronger Lewis systems too, can prove $p\Rightarrow q$ (Parry 1939: 143)[^parry-1939]).

### 1.2 Other Systems and Alternative Axiomatizations of the Lewis Systems

Gödel in “An Interpretation of the Intuitionistic Propositional Calculus” (1933) is the first to propose an alternative axiomatization of the Lewis system **S4** that separates the propositional basis of the system from the modal axioms and rules. Gödel adds the following rules and axioms to the propositional calculus.

$$\begin{align*} \tag{Necessitation} \textrm{If } \mvdash \alpha &\textrm{ then } \mvdash \Box \alpha, \\ \tag{Axiom K} \mvdash \Box(p\rightarrow q)&\rightarrow(\Box p\rightarrow \Box q), \\ \tag{Axiom T} \mvdash \Box p&\rightarrow p\textrm{, and} \\ \tag{Axiom 4} \mvdash \Box p&\rightarrow \Box \Box p.\\ \end{align*} $$

Initially, Gödel employs an operator $B$ of provability to translate Heyting’s primitive intuitionistic connectives, and then observes that if we replace $B$ with an operator of necessity we obtain the system **S4**. Gödel also claims that a formula $\Box p\vee \Box q$ is not provable in **S4** unless either $\Box p$ or $\Box q$ is provable, analogously to intuitionistic disjunction. Gödel’s claim will be proved algebraically by McKinsey and Tarski (1948). Gödel’s short note is important for starting the fruitful practice of axiomatizing modal systems separating the propositional calculus from the strictly modal part, but also for connecting intuitionistic and modal logic.

Feys (1937)[^feys-1937] is the first to propose system **T** by subtracting axiom 4 from Gödel’s system **S4** (see also Feys 1965: 123–124)[^feys-1965]. In *An Essay in Modal Logic* (1951) von Wright discusses alethic, epistemic, and deontic modalities, and introduces system **M**, which Sobociński (1953)[^sobociński-1953] will prove to be equivalent to Feys’ system **T**. Von Wright (1951: 84–90)[^wright-1951] proves that system **M** contains Lewis’s **S2**, which contains **S1**—where system **S** is said to contain system **S′** if all the formulas provable in **S′** can be proved in **S** too. System **S3**, an extension of **S2**, is not contained in **M**. Nor is **M** contained in **S3**. Von Wright finds **S3** of little independent interest, and sees no reason to adopt **S3** instead of the stronger **S4**. In general, the Lewis systems are numbered in order of strength, with **S1** the weakest and **S5** the strongest, weaker systems being contained in the stronger ones.

Lemmon (1957)[^lemmon-1957] also follows Gödel in axiomatizing modal systems on a propositional calculus base, and presents an alternative axiomatization of the Lewis systems. Where **PC** is the propositional calculus base, **PC** may be characterized as the following three rules (1957: 177):

A characterization of propositional calculus **PC**

**PCa**

If *α* is a tautology, then $\mvdash \alpha$

**PCb**

Substitution for propositional variables

**PCc**

Material detachment/*Modus Ponens*: if *α* and $\alpha \rightarrow \beta$ are tautologies, then so is *β*

Further rules in Lemmon’s system are:

**(a)**

If $\mvdash \alpha$ then $\mvdash \Box \alpha$ (Necessitation)

**(a′)**

If *α* is a tautology or an axiom, then $\mvdash \Box \alpha$

**(b)**

If $\mvdash \Box(\alpha \rightarrow \beta)$ then $\mvdash \Box(\Box \alpha \rightarrow \Box \beta)$

**(b′)**

Substitutability of strict equivalents.

Further axioms in Lemmon’s system are:

$$ \begin{align} \tag{1} \Box(p \rightarrow q)&\rightarrow \Box(\Box p\rightarrow \Box q) \\ \tag{\(1'\)} \Box(p\rightarrow q)&\rightarrow(\Box p\rightarrow \Box q) &\textrm{(Axiom K)} \\ \tag{2} \Box p&\rightarrow p &\textrm{(Axiom T)} \\ \tag{3} (\Box(p\rightarrow q)\wedge \Box(q\rightarrow r))&\rightarrow \Box(p\rightarrow r)\\ \end{align} $$

Using the above rules and axioms Lemmon defines four systems. System **P1**, which is proved equivalent to the Lewis system **S1**, employs the propositional basis (**PC**), rules (a′)—necessitation of tautologies and axioms—and (b′), and axioms (2) and (3). System **P2**, equivalent to **S2**, employs (**PC**), rules (a′) and (b), and axioms (2) and (1′). System **P3**, equivalent to **S3**, employs (**PC**), rule (a′), and axioms (2) and (1). System **P4**, equivalent to **S4**, employs (**PC**), rule (a), and axioms (2) and (1). In Lemmon’s axiomatization it is easy to see that **S3** and von Wright’s system **M** (Feys’ **T**) are not included in each other, given **M**’s stronger rule of necessitation and **S3**’s stronger axiom (1) in place of (1′) = K. In general, Lemmon’s axiomatization makes more perspicuous the logical distinctions between the different Lewis systems.

Lemmon considers also some systems weaker than **S1**. Of particular interest is system **S0.5** which weakens **S1** by replacing rule (a′) with the weaker rule (a″):

**(a″)**

If *α* is a tautology, then $\mvdash \Box \alpha$.

Lemmon interprets system **S0.5** as a formalized metalogic of the propositional calculus, where $\Box \alpha$ is interpreted as “*α* is a tautology”.

We call “normal” the systems that include **PC**, axiom K and the rule of necessitation. System **K** is the smallest normal system. System **T** adds axiom T to system **K**. System **B** (the Brouwersche system) adds axiom B

$$\mvdash p\Rightarrow \Box \Diamond p \quad\textrm{(equivalent to Becker’s C12)}$$

to system **T**. **S4** adds axiom 4 (equivalent to Becker’s C10) to system **T**. **S5** adds axioms B and 4, or alternatively axiom E

$$\mvdash \Diamond p\Rightarrow \Box \Diamond p \quad \textrm{(equivalent to Becker’s C11)}$$

to system **T**. Lewis’s systems **S1**, **S2**, and **S3** are non-normal given that they do not contain the rule of Necessitation. For the relationship between these (and other) systems, and the conditions on frames that the axioms impose, consult the SEP entry on modal logic.

Only a few of the many extensions of the Lewis systems that have been discussed in the literature are mentioned here. Alban (1943)[^alban-1943] introduces system **S6** by adding to **S2** the axiom $\mvdash \Diamond \Diamond p$. Halldén (1950)[^halldén-1950] calls **S7** the system that adds the axiom $\mvdash \Diamond \Diamond p$ to **S3**, and **S8** the system that extends **S3** with the addition of the axiom $\mvdash \neg \Diamond \neg \Diamond \Diamond p$. While the addition of an axiom of universal possibility $\mvdash \Diamond p$ would be inconsistent with all the Lewis systems, since they all contain theorems of the form $\mvdash \Box p$, systems **S6**, **S7** and **S8** are consistent. Instead, the addition of either of these axioms to **S4**, and so also to **S5**, results in an inconsistent system, given that in **S4** $\mvdash \Diamond \Diamond p\Rightarrow \Diamond p$. Halldén also proved that a formula is a theorem of **S3** if and only if it is a theorem of both **S4** and **S7** (1950: 231–232), thus **S4** and **S7** are two alternative extensions of **S3**.

## 2. The Matrix Method and Some Algebraic Results

In “Philosophical Remarks on Many-Valued Systems of Propositional Logic” (1930; but Łukasiewicz 1920 is a preliminary Polish version of the main ideas of this paper), Łukasiewicz says:

> When I recognized the incompatibility of the traditional theorems on modal propositions in 1920, I was occupied with establishing the system of the ordinary “two-valued” propositional calculus by means of the matrix method. I satisfied myself at the time that all theses of the ordinary propositional calculus could be proved on the assumption that their propositional variables could assume only two values, “0” or “the false”, and “1” or “the true”. (1970: 164)

This passage illustrates well how Łukasiewicz was thinking of logic in the early twenties. First, he was thinking in algebraic terms, rather than syntactically, concerning himself not so much with the construction of new systems, but with the evaluation of the systems relatively to sets of values. Secondly, he was introducing three-valued matrices to make logical space for the notion of propositions (eminently about future contingents) that are neither true nor false, and that receive the new indeterminate value ½. Ironically, later work employing his original matrix method will show that the hope of treating modal logic as a three-valued system cannot be realized. See also the SEP entry on many-valued logic.

A matrix for a propositional logic *L* is given by (i) a set *K* of elements, the truth-values, (ii) a non-empty subset $D\subseteq K$ of designated truth-values, and (iii) operations on the set *K*, that is, functions from $n$-tuples of truth-values to truth-values, that correspond to the connectives of *L*. A matrix satisfies a formula *A* under an assignment *σ* of elements of *K* to the variables of *A* if the value of *A* under *σ* is a member of *D*, that is, a designated value. A matrix satisfies a formula if it satisfies it under every assignment *σ*. A matrix for a modal logic *M* extends a matrix for a propositional logic by adding a unary function that corresponds to the connective $\Diamond$.

Matrices are typically used to show the independence of the axioms of a system as well as their consistency. The consistency of two formulas *A* and *B* is established by a matrix that, under an assignment *σ*, assigns designated values to both formulas. The independence of formula *B* from formula *A* is established by a matrix that (i) preserves the validity of the rules of the system and that (ii) under an interpretation *σ* assigns a designated value to *A* but not to *B*. Parry (1939)[^parry-1939] uses the matrix method to show that the number of modalities of Lewis’s systems **S3** and **S4** is finite. A modality is a modal function of one variable that contains only the operators $\neg$ and $\Diamond$. The degree of a modality is given by the number of $\Diamond$ operators contained. A proper modality is of degree higher than zero. Proper modalities can be of four different forms:

$$\begin{align} \tag{1} \neg \ldots \Diamond p\\ \tag{2} \Diamond \ldots \Diamond p\\ \tag{3} \neg \ldots \Diamond \neg p\\ \tag{4} \Diamond \ldots \neg p.\\ \end{align}$$

The improper modalities are $p$ and $\neg p$ (1939: 144). Parry proves that **S3** has 42 distinct modalities, and that **S4** has 14 distinct modalities. It was already known that system **S5** has only 6 distinct modalities since it reduces all modalities to modalities of degree zero or one. Parry introduces system **S4.5** by adding to **S4** the following axiom:

$$\mvdash \neg \Diamond \neg \Diamond \neg \Diamond p\Rightarrow \neg \Diamond p.$$

The system reduces the number of modalities of **S4** from 14 to 12 (or 10 proper ones). The addition of the same axiom to Lewis’s system **S3** results in a system with 26 distinct modalities. Moreover, if we add

$$\mvdash \neg \Diamond \neg \Diamond \Diamond p\Rightarrow \neg \Diamond \neg \Diamond p$$

to **S3** we obtain a distinct system with 26 modalities also intermediate between **S3** and **S4**. Therefore the number of modalities does not uniquely determine a system. Systems **S1** and **S2**, as well as **T** and **B**, have an infinite number of modalities (Burgess 2009, chapter 3 on Modal Logic, discusses the additional systems **S4.2** and **S4.3** and explains well the reduction of modalities in different systems)[^burgess-2009].

A *characteristic* matrix for a system *L* is a matrix that satisfies all and only the theorems of *L*. A matrix is *finite* if its set *K* of truth-values is finite. A finite characteristic matrix yields a decision procedure, where a system is decidable if every formula of the system that is not a theorem is falsified by some finite matrix (this is the finite model property). Yet Dugundji (1940)[^dugundji-1940] shows that none of **S1**–**S5** has a finite characteristic matrix. Hence, none of these systems can be viewed as an $n$-valued logic for a finite $n$. Later, Scroggs (1951)[^scroggs-1951] will prove that every proper extension of **S5** that preserves detachment for material implication and is closed under substitution has a finite characteristic matrix.

Despite their lack of a finite characteristic matrix, McKinsey (1941)[^mckinsey-1941] shows that systems **S2** and **S4** are decidable. To prove these results McKinsey introduces modal matrices $(K, D, -, *, \times)$, with $-$, $*$, and $\times$ corresponding to negation, possibility, and conjunction respectively. A matrix is *normal* if it satisfies the following conditions:

1. if $x \in D$ and $(x\Rightarrow y) \in D$ and $y \in K$, then $y \in D$,
2. if $x \in D$ and $y \in D$, then $x\times y \in D$,
3. if $x \in K$ and $y \in K$ and $x\Leftrightarrow y \in D$, then $x = y$.

These conditions correspond to Lewis’s rules of strict inference, adjunction and substitution of strict equivalents. The structure of McKinsey’s proof is as follows. The proof employs three steps. First, using an unpublished method of Lindenbaum explained to him by Tarski which holds for systems that have the rule of Substitution for propositional variables, McKinsey shows that there is an **S2**-characteristic matrix $M = (K, D, -, *, \times)$ that does not satisfy condition (iii) and is therefore non-normal. *M* is a trivial matrix whose domain is the set of formulas of the system, whose designated elements are the theorems of the system, and whose operations are the connectives themselves. The trivial matrix *M* does not satisfy (iii) given that for some distinct formulas *A* and *B*, $A\Leftrightarrow B$ is an **S2**-theorem. Second, McKinsey shows how to construct from *M* a normal, but still infinite, **S2**-characteristic matrix $M_1 = (K_1, D_1, -_1, *_1, \times_1 )$, whose elements are equivalence classes of provably equivalent formulas of **S2**, i.e., of formulas *A* and *B* such that $A\Leftrightarrow B$ is a theorem of **S2**, and whose operations are revised accordingly. For example, if $E(A)$ is the set of formulas provably equivalent to *A* and $E(A)\in K_1$, then $-_1 E(A) = E(-A)= E(\neg A). M_1$ satisfies exactly the formulas satisfied by *M* without violating condition (iii), hence it is a characteristic normal matrix for **S2** ($M_1$ is the Lindenbaum algebra for **S2**). Finally, it is shown that for every formula *A* that is not a theorem of **S2** there is a finite and normal matrix (a sub-algebra of $M_1)$ that falsifies it. A similar proof is given for **S4**.

A matrix is a special kind of algebra. An algebra is a matrix without a set *D* of designated elements. Boolean algebras correspond to matrices for propositional logic. According to Bull and Segerberg (1984: 10) the generalization from matrices to algebras may have had the effect of encouraging the study of these structures independently of their connections to logic and modal systems. The set of designated elements *D* in fact facilitates a definition of validity with respect to which the theorems of a system can be evaluated. Without such a set the most obvious link to logic is severed. A second generalization to classes of algebras, rather than merely to individual algebras, was also crucial to the mathematical development of the subject matter. Tarski is the towering figure in such development.

Jónsson and Tarski (1951 and 1952) introduce the general idea of Boolean algebras with operators, i.e., extensions of Boolean algebras by addition of operators that correspond to the modal connectives. They prove a general representation theorem for Boolean algebras with operators that extends Stone’s result for Boolean algebras (every Boolean algebra can be represented as a set algebra). This work of Jónsson and Tarski evolved from Tarski’s purely mathematical study of the algebra of relations and includes no reference to modal logic or even logic in general. Jónsson and Tarski’s theorem is a (more general) algebraic analog of Kripke’s later semantic completeness results, yet this was not realized for some time. Not only was Tarski unaware of the connection, but it appears that both Kripke and Lemmon had not read the Jónsson and Tarski papers at the time in which they did their modal work in the late fifties and sixties, and Kripke claims to have reached the same result independently.

Lemmon (1966a and 1966b) adapts the algebraic methods of McKinsey to prove decidability results and representation theorems for various modal systems including **T** (though apparently in ignorance of Jónsson and Tarski’s work). In particular, he extends McKinsey’s method by introducing a new technique for constructing finite algebras of subsets of a Kripke model structure (discussed in the next section of this entry). Lemmon (1966b: 191)[^lemmon-1966b] attributes to Dana Scott the main result of his second 1966 paper. This is a general representation theorem proving that algebras for modal systems can be represented as algebras based on the power set of the set *K* in the corresponding Kripke’s structures. As a consequence, algebraic completeness translates into Kripke’s model theoretic completeness. So, Lemmon elucidates very clearly the connection between Kripke’s models whose elements are worlds and the corresponding algebras whose elements are sets of worlds that can be thought of as propositions, thereby showing that the algebraic and model theoretic results are deeply connected. Kripke (1963a)[^kripke-1963a] is already explicit on this connection. In *The Lemmon Notes* (1977), written in collaboration with Dana Scott and edited by Segerberg, the 1966 technique is transformed into a purely model theoretic method which yields completeness and decidability results for many systems of modal logic in as general a form as possible (1977: 29).

See also the SEP entry on the algebra of logic tradition. For a basic introduction to the algebra of modal logic, consult Hughes and Cresswell 1968, Chapter 17 on “Boolean Algebra and Modal Logic”. For a more comprehensive treatment, see chapter 5 of Blackburn, de Rijke, and Venema 2001. See also Goldblatt 2003.

## 3. The Model Theoretic Tradition

### 3.1 Carnap

In the early 1940s the recognition of the semantical nature of the notion of logical truth led Rudolf Carnap to an informal explication of this notion in terms of Leibnizian possible worlds. At the same time, he recognized that the many syntactical advances in modal logic from 1918 on were still not accompanied by adequate semantic considerations. One notable exception was Gödel’s interpretation of necessity as provability and the resulting preference for **S4**. Carnap instead thought of necessity as logical truth or analyticity. Considerations on the properties of logically true sentences led him to think of **S5** as the right system to formalize this ‘informal’ notion. Carnap’s work in the early forties would then be focused on (1) defining a formal semantic notion of *L*-truth apt to represent the informal semantic notions of logical truth, necessity, and analyticity, that is, truth in virtue of meaning alone (initially, he drew no distinction between these notions, but clearly thought of analyticity as the leading idea); and (2) providing a formal semantics for quantified **S5** in terms of the formal notion of *L*-truth with the aim of obtaining soundness and completeness results, that is, prove that all the theorems of quantified **S5** are *L*-true, and that all the *L*-truths (expressible in the language of the system) are theorems of the system.

The idea of quantified modal systems occurred to Ruth Barcan too. In “A Functional Calculus of First Order Based on Strict Implication” (1946a) she added quantification to Lewis’s propositional system **S2**; Carnap (1946)[^carnap-1946] added it to **S5**. Though some specific semantic points about quantified modal logic will be considered, this entry is not focused on the development of quantified modal logic, but rather on the emergence of the model theoretic formal semantics for modal logic, propositional or quantified. For a more extensive treatment of quantified modal logic, consult the SEP entry on modal logic.

In “Modalities and Quantification” (1946) and in *Meaning and Necessity* (1947), Carnap interprets the object language operator of necessity as expressing at the object level the semantic notion of logical truth:

> [T]he guiding idea in our constructions of systems of modal logic is this: a proposition $p$ is logically necessary if and only if a sentence expressing $p$ is logically true. That is to say, the modal concept of the logical necessity of a proposition and the semantical concept of the logical truth or analyticity of a sentence correspond to each other. (1946: 34)

Carnap introduces the apparatus of state-descriptions to define the formal semantic notion of *L*-truth. This formal notion is then to be used to provide a formal semantics for **S5**.

A state-description for a language *L* is a class of sentences of *L* such that, for every atomic sentence $p$ of *L*, either $p$ or $\neg p$, but not both, is contained in the class. An atomic sentence *holds in* a state-description *R* if and only if it belongs to *R*. A sentence $\neg A$ (where *A* need not be atomic) holds in *R* if and only if *A* does not hold in *R*; $(A\wedge B)$ holds in *R* if and only if both *A* and *B* hold in *R*, and so on for the other connectives in the usual inductive way; $(\forall x)Fx$ holds in *R* if and only if all the substitution instances of $Fx$ hold in *R*. The *range* of a sentence is the class of state-descriptions in which it holds. Carnap’s notion of validity or *L*-truth is a maximal notion, i.e., Carnap defines a sentence to be valid or *L*-true if and only if it holds in *all* state-descriptions. In later work Carnap adopts models in place of state-descriptions. Models are assignments of values to the primitive non-logical constants of the language. In Carnap’s case predicate constants are the only primitive constants to which the models assign values, since individual constants are given a fixed pre-model interpretation and value assignments to variables are done independently of the models (1963a).

It is important to notice that the definition of *L*-truth does not employ the notion of truth, but rather only that of holding-in-a-state-description. Truth is introduced later as what holds in the real state description. To be an adequate formal representation of analyticity, *L*-truth must respect the basic idea behind analyticity: truth in virtue of meaning alone. In fact, the *L*-truths of a system *S* are such that the semantic rules of *S* suffice to establish their truth. Informally, state-descriptions represent something like Leibnizian possible worlds or Wittgensteinian possible states of affairs and the range of state-descriptions for a certain language is supposed to exhaust the range of alternative possibilities describable in that language.

Concerning modal sentences, Carnap adopts the following conventions (we use $\Box$ in place of Carnap’s operator *N* for logical necessity). Let *S* be a system:

1. A sentence $\Box A$ is true in *S* if and only if $A$ is *L*-true in *S* (so a sentence $\Box A$ is true in *S* if and only if $A$ holds in all the state descriptions of *S*);
2. A sentence $\Box A$ is *L*-true in *S* if and only if $\Box A$ is true in *S* (so all state-descriptions agree in their evaluation of modal sentences).

From which it follows that:

1. $\Box A$ is *L*-true in *S* if and only if $A$ is *L*-true in *S*.

Carnap’s conventions hold also if we substitute “truth in a state description of *S*” for “truth in *S*”.

Carnap assumes a fixed domain of quantification for his quantified system, the functional calculus with identity **FC**, and consequently for the modal functional calculus with identity **MFC**, a quantified form of **S5**. The language of **FC** contains denumerably many individual constants, the universe of discourse contains denumerably many individuals, each constant is assigned an individual of the domain, and no two constants are assigned the same individual. This makes sentences like $a = a$ *L*-true, and sentences like $a = b$ *L*-false (1946: 49). Concerning **MFC**, the Barcan formula and its converse are both *L*-true, that is,

$$\mvDash(\forall x)\Box Fx\leftrightarrow \Box(\forall x)Fx.$$

This result is guaranteed by the assumption of a fixed domain of quantification. Carnap proves that **MFC** is sound, that is, all its theorems are *L*-true, and raises the question of completeness for both **FC** and **MFC**. Gödel proved completeness for the first order predicate calculus with identity, but the notion of validity employed was truth in every non-empty domain of quantification, including finite domains. Carnap instead adopts one unique denumerable domain of quantification. The adoption of a fixed denumerable domain of individuals generates some additional validities already at the pre-modal level which jeopardize completeness, for example “There are at least two individuals”, $(\exists x)(\exists y)(x\ne y)$, turns out to be valid (1946: 53).

A consequence of the definitions of state-descriptions for a language and *L*-truth is that each atomic sentence and its negation turn out to be true at some, but not all, state-descriptions. Hence, if $p$ is atomic both $\Diamond p$ and $\Diamond \neg p$ are *L*-true. Hence, Lewis’s rule of Uniform Substitution fails (if $p\wedge \neg p$ is substituted for $p$ in $\Diamond p$ we derive $\Diamond(p\wedge \neg p)$, which is *L*-false, not *L*-true). This is noticed by Makinson (1966a)[^makinson-1966a] who argues that what must be done is reinstate substitutivity and revise Carnap’s naïve notion of validity (as logical necessity) in favor of a schematic Quinean notion (“A *logical truth …* *is definable as a sentence from which we get only truths when we substitute sentences for its simple sentences*” Quine 1970: 50)[^quine-1970] that will not make sentences like $\Diamond p$ valid. Nonetheless, Carnap proves the soundness and completeness of propositional **S5**, which he calls “**MPC**” for “modal propositional calculus”, following Wajsberg. The proof however effectively employs a schematic notion of validity.

It has been proved that Carnap’s notion of maximal validity makes completeness impossible for quantified **S5**, i.e., that there are *L*-truths that are not theorems of Carnap’s **MFC**. Let $A$ be a non-modal sentence of **MFC**. By convention (1), $\Box A$ is true in **MFC** if and only if $A$ is *L*-true in **MFC**. But $A$ is also a sentence of **FC**, thus if *L*-true in **MFC** it is also *L*-true in **FC**, since the state descriptions (models) of modal functional logic are the same as those of functional logic (1946: 54). This means that the state descriptions hold the triple role of (i) first-order models of **FC** thereby defining first-order validity, (ii) worlds for **MFC** thereby defining truth for $\Box A$ sentences of **MFC**, and (iii) models of **MFC** thereby defining validity for **MFC**. The core of the incompleteness argument consists in the fact that the non-validity of a first-order sentence $A$ can be represented in the modal language, as $\neg \Box A$, but all models agree on the valuation of modal sentences, making $\neg \Box A$ valid. Roughly, and setting aside complications created by the fact that Carnap’s semantics has only denumerable domains, if $A$ is a first-order non-valid sentence of **FC**, $A$ is true in some but not all the models or state-descriptions. Given Carnap’s conventions, it follows that $\neg \Box A$ is true in **MFC**. But then $\neg \Box A$ is *L*-true in **MFC**, i.e., in **MFC** $\mvDash \neg \Box A$. Given that the non-valid first-order sentences are not recursively enumerable, neither are the validities for the modal system **MFC**. But the class of theorems of **MFC** is recursively enumerable. Hence, **MFC** is incomplete *vis-à-vis* Carnap’s maximal validity. Cocchiarella (1975b)[^cocchiarella-1975b] attributes the result to Richard Montague and Donald Kalish. See also Lindström 2001: 209 and Kaplan 1986: 275–276.

### 3.2 Kripke’s Possible Worlds Semantics

Carnap’s semantics is indeed a precursor of Possible Worlds Semantics (PWS). Yet some crucial ingredients are still missing. First, the maximal notion of validity must be replaced by a new universal notion. Second, state-descriptions must make space for possible worlds understood as indices or points of evaluation. Last, a relation of accessibility between worlds needs to be introduced. Though Kripke is by no means the only logician in the fifties and early sixties to work on these ideas, it is in Kripke’s version of PWS that *all* these innovations are present. Kanger (1957)[^kanger-1957], Montague (1960, but originally presented in 1955), Hintikka (1961)[^hintikka-1961], and Prior (1957)[^prior-1957] were all thinking of a relation between worlds, and Hintikka (1961)[^hintikka-1961] like Kripke (1959a)[^kripke-1959a] adopted a new notion of validity that required truth in all arbitrary sets of worlds. But Kripke was the only one to characterize the worlds as simple points of evaluation (in 1963a). Other logicians were still thinking of the worlds fundamentally as models of first-order logic, though perhaps Prior in his development of temporal logic was also moving towards a more abstract characterization of instants of time. Kripke’s more abstract characterization of the worlds is crucial in the provision of a link between the model theoretic semantics and the algebra of modal logic. Kripke saw very clearly this connection between the algebra and the semantics, and this made it possible for him to obtain model theoretic completeness and decidability results for various modal systems in a systematic way. Goldblatt (2003: section 4.8) argues convincingly that Kripke’s adoption of points of evaluation in the model structures is a particularly crucial innovation. Such a generalization opens the door to different future developments of the model theory and makes it possible to provide model theories for intensional logics in general. For these reasons, in this entry we devote more attention to Kripke’s version of PWS. For a more comprehensive treatment of the initial development of PWS, including the late fifties work on **S5** of the French logician Bayart, the reader is referred to Goldblatt 2003. On the differences between Kanger’s semantics and standard PWS semantics, see Lindström 1996 and 1998.

Kripke’s 1959a “A Completeness Theorem in Modal Logic” contains a model theoretic completeness result for a quantified version of **S5** with identity. In Kripke’s semantic treatment of quantified **S5**, which he calls S5*$^=$, an assignment of values to a formula $A$ in a domain of individuals $D$ assigns a member of $D$ to each free individual variable of $A$, a truth value $T$ or $F$ to each propositional variable of $A$, and a set of ordered $n$-tuples of members of $D$ to each $n$-place predicate variable of $A$ (the language for the system contains no non-logical constants). Kripke defines a *model over a non-empty domain* $D$ of individuals as an ordered pair $(G, K)$, such that $G\in K, K$ is an *arbitrary* subset of assignments of values to the formulas of S5*$^=$, and all $H\in K$ agree on the assignments to individual variables. For each $H\in K$, the value that $H$ assigns to a formula $B$ is defined inductively. Propositional variables are assigned $T$ or $F$ by hypothesis. If $B$ is $P(x_1, \ldots, x_n)$, $B$ is assigned $T$ if and only if the $n$-tuple of elements assigned to $x_1$, …, $x_n$ belongs to the set of $n$-tuples of individuals that $H$ assigns to $P. H$ assigns $T$ to $\neg B$ if and only if it assigns $F$ to $B. H$ assigns $T$ to $B\wedge C$ if and only if it assigns $T$ to $B$ and to $C$. If $B$ is $x = y$ it is assigned $T$ if and only if $x$ and $y$ are assigned the same value in $D$. If $B$ is $(\forall x)Fx$ it is assigned $T$ if and only if $Fx$ is assigned $T$ for every assignment to $x$. $\Box B$ is assigned $T$ if and only if $B$ is assigned $T$ by every $H\in K$.

The most important thing to be noticed in the 1959 model theory is the definition of validity. A formula $A$ is said to be *valid in a model* $(G, K)$ in $D$ if and only if it is assigned $T$ in $G$, to be *valid in a domain* $D$ if and only if it is valid in every model in $D$, and to be *universally valid* if and only if it is valid in every non-empty domain. Kripke says:

> In trying to construct a definition of universal logical validity, it seems plausible to assume not only that the universe of discourse may contain an arbitrary number of elements and that predicates may be assigned any given interpretations in the actual world, but also that *any combination of possible worlds may be associated with the real world with respect to some group of predicates*. In other words, it is plausible to assume that no further restrictions need be placed on $D, G$, and $K$, except the standard one that $D$ be non-empty. This assumption leads directly to our definition of universal validity. (1959a: 3)

This new universal notion of validity is much more general than Carnap’s maximal validity. The elements $H$ of $K$ still correspond to first-order models, like Carnap’s state-descriptions, and in each Kripke model the elements $H$ of $K$ are assigned the same domain $D$ of individuals and the individual variables have a fixed cross-model assignment. So far the only significant divergence from Carnap is that different Kripke models can have domains of different cardinality. This by itself is sufficient to reintroduce completeness for the non-modal part of the system. But the most significant development, and the one that makes it possible to prove completeness for the modal system, is the definition of validity not as truth in all worlds of a maximal structure of worlds, but as truth across all the subsets of the maximal structure. The consideration of arbitrary subsets of possible worlds, makes it possible for Kripke’s model theory to disconnect validity from necessity. While necessities are relative to a model, hence to a set of worlds, validities must hold across all such sets. This permits the reintroduction of the rule of Uniform Substitution. To see this intuitively in a simple case, consider an atomic sentence $p$. The classical truth-table for $p$ contains two rows, one where $p$ is true and one where $p$ is false. Each row is like a possible world, or an element $H$ of $K$. If we only consider this complete truth table, we are only considering maximal models that contain two worlds (it makes no difference which world is actual). By the definition of truth for a formula $\Box B, \Box p$ is false in all the worlds of the maximal model, and $\Diamond p$ is true in all of them. If validity is truth in all worlds of this maximal model, like for Carnap, it follows that $\mvDash \Diamond p$, but in **S5** $\nmvdash\Diamond p$. If instead we define validity as Kripke does, we have to consider also the non-maximal models that contain only one world, that is, incomplete truth-tables that cancel some rows. Hence, there are two more models to be taken into consideration: one which contains only one world $H=G$ where $p$ is true, hence so is $\Box p$, and one which contains only one world $H=G$ where $p$ is false and so is $\Box p$ as well as $\Diamond p$. Thanks to this last model $\nmvDash \Diamond p$. Notice that the crucial innovation is the definition of validity as truth across all subsets of worlds, not just the maximal subset. The additional fact that validity in a model is defined as truth at the actual world of the model—as opposed to truth at all worlds of the model—though revealing of the fact that Kripke did not link the notion of necessity to the notion of validity, is irrelevant to this technical result.

Kripke’s completeness proof makes use of Beth’s method of semantic tableaux. A semantic tableau is used to test whether a formula $B$ is a semantic consequence of some formulas $A_1, \ldots, A_n$. The tableau assumes that the formulas $A_1, \ldots, A_n$ are true and $B$ is false and is built according to rules that follow the definitions of the logical connectives. For example, if a formula $\neg A$ is on the left column of the tableau (where true formulas are listed), $A$ will be put on the right column (where false formulas are listed). To deal with modal formulas, sets of tableaux must be considered, since if $\Box A$ is on the right column of a tableau, a new auxiliary tableau must be introduced with $A$ on its right column. A main tableau and its auxiliary tableaux form a set of tableaux. If a formula $A\wedge B$ is on the right column of the main tableau, the set of tableaux splits into two new sets of tableaux: one whose main tableau lists $A$ on its right column and one whose main tableau lists $B$ on the right column. So we have to consider alternative sets of tableaux. A semantic tableau is closed if and only if all its alternative sets are closed. A set of tableaux is closed if it contains a tableau (main or auxiliary) that reaches a contradiction in the form of (i) one and the same formula $A$ appearing in both its columns or (ii) an identity formula of the form $a = a$ in its right side (this is an oversimplification of the definition of a closed tableau, but not harmful for our purposes). Oversimplifying once more, the structure of Kripke’s completeness proof consists of proving that a semantic tableau used to test whether a formula $B$ is a semantic consequence of formulas $A_1, \ldots, A_n$ is closed if and only (i) in S5*$^=$ $A_1, \ldots, A_n\vdash B$ and (ii) $A_1, \ldots, A_n\vDash B$. This last result is achieved by showing how to build models from semantic tableaux. As a consequence of (i) and (ii) we have soundness and completeness for S5*$^=$, that is: $A_1, \ldots, A_n\vdash B$ if and only if $A_1, \ldots, A_n\vDash B$.

The 1959 paper contains also a proof of the modal counterpart of the Löwenhein-Skolem theorem for first-order logic, according to which if a formula is satisfiable in a non-empty domain then it is satisfiable, and hence valid (true in $G)$, in a model $(G, K)$ in a domain $D$, where *both* $K$ and $D$ are either finite or denumerable; and if a formula is valid in every finite or denumerable domain it is valid in every domain.

Kripke’s 1962 “The Undecidability of Monadic Modal Quantification Theory” develops a parallel between first-order logic with one dyadic predicate and first-order monadic modal logic with just two predicate letters, to prove that this fragment of first-order modal logic is already undecidable.

Of great importance is the paper “Semantical Analysis of Modal Logic I” (Kripke 1963a)[^kripke-1963a] where normal systems are treated. It is here that Kripke fully develops the analogy with the algebraic results of Jónsson and Tarski and proves completeness and decidability for propositional systems **T**, **S4**, **S5**, and **B** (the Brouwersche system), which is here introduced. Kripke claims to have derived on his own the main theorem of “Boolean Algebras with Operators” by an algebraic analog of his own semantical methods (69, fn. 2). It is in this paper that the two additional crucial generalizations of the model theory are introduced. The first is the new understanding of the elements $H$ of $K$ as simple indices, not assignments of values. Once this change is introduced, the models have to be supplemented by an auxiliary function *Φ* needed to assign values to the propositional variables relative to worlds. Hence, while in the 1959 model theory

> *there can be no two worlds in which the same truth-value is assigned to each atomic formula* [which] turns out to be convenient perhaps for **S5**, but it is rather inconvenient when we treat normal MPC’s in general (1963a: 69)

we can now have world duplicates. What is most important about the detachment of the elements of $K$ from the evaluation function is that it opens the door to the general consideration of modal frames, sets of worlds plus a binary relation between them, and the correspondence of such frames to modal systems. So, the second new element of the paper, the introduction of a relation $R$ between the elements of $K$, naturally accompanies the first. Let it be emphasized once again that the idea of a relation between worlds is not new to Kripke. For example, it is already present as an alternativeness relation in Montague 1960, Hintikka 1961, and Prior 1962, where the idea is attributed to Peter Geach.

In 1963a Kripke “asks various questions concerning the relation $R$” (1963a: 70). First, he shows that every satisfiable formula has a connected model, i.e., a model based on a model structure $(G, K, R)$ where for all $H\in K$, $G\mathrel{R*}H$, where $R*$ is the ancestral relation corresponding to $R$. Hence, only connected models need to be considered. Then, Kripke shows the nowadays well-known results that axiom 4 corresponds to the transitivity of the relation $R$, that axiom $B$ correspond to symmetry, and that the characteristic axiom of **S5** added to system **T** corresponds to $R$ being an equivalence relation. Using the method of tableaux, completeness for the modal propositional systems **T**, **S4**, **S5**, and **B** *vis-à-vis* the appropriate class of models (reflexive structures for **T**) is proved. The decidability of these systems, including the more complex case of **S4**, is also proved. (For a more detailed treatment of frames, consult the SEP entry on modal logic.)

In the 1965 paper “Semantical Analysis of Modal Logic II”, Kripke extends the model theory to treat non-normal modal systems, including Lewis’s **S2** and **S3**. Though these systems are considered somewhat unnatural, their model theory is deemed elegant. Completeness and decidability results are proved *vis-à-vis* the proper class of structures, including the completeness of **S2** and **S3**, and the decidability of **S3**. To achieve these results, the model theory is extended by the introduction of non-normal worlds which do not respect the standard Leibnizian interpretation of $\Box$ as truth in every accessible world, and that make every formula of the form $\Box B$ false. This leads to a corresponding revision of the interpretation of $\Box$, and to the introduction of a new element $N\subseteq K$ in the model structures $(G, K, R, N). N$ is the subset of normal worlds which respect the standard interpretation of $\Box$. Non-normal worlds are needed to prevent the validity of formulas like $\Box\Box A$ even when $\Box A$ is valid, by basically allowing A but not $\Box A$ to be true in every world accessible from the actual world and thus $\Box A$ but not $\Box\Box A$ to hold in the actual world. This is required as the systems under consideration do not have a full rule of necessitation. Another interesting aspect of the non-normal systems is that in the model theoretic results that pertain to them, $G$ (the actual world) plays an essential role, in particular in the **S2** and **S3** model structures the actual world has to be normal. Instead, the full rule of necessitation that holds in normal systems eliminates the need of non-normal worlds and makes the choice of $G$ model theoretically irrelevant.

The great success of the Kripkean model theory notwithstanding, it is worth emphasizing that not all modal logics are complete. For incompleteness results see Makinson 1969, for a system weaker than **S4**; and Fine 1974, S. Thomason 1974, Goldblatt 1975, and van Benthem 1978, for systems between **S4** and **S5**. Some modal formulas impose conditions on frames that cannot be expressed in a first-order language, thus even propositional modal logic is fundamentally second-order in nature. Insofar as the notion of validity on a frame abstracts from the interpretation function, it implicitly involves a higher-order quantification over propositions. On the correspondence between frame validity and second-order logic and on the model-theoretic criteria that distinguish the modal sentences that are first-order expressible from those that are essentially second-order see Blackburn and van Benthem’s “Modal Logic: A Semantic Perspective” (2007a).

In 1963b, “Semantical Considerations on Modal Logic”, Kripke introduces a new generalization to the models of quantified modal systems. In 1959 a model was defined in a domain $D$. As a result all worlds in one model had the same cardinality. In 1963b models are not given in a domain, hence worlds in the same model can be assigned different domains by a function *Ψ* that assigns domains to the elements $H$ of $K$. Given the variability of domains across worlds, Kripke can now construct counter-examples both to the Barcan Formula

$$(\forall x)\Box Fx\rightarrow\Box(\forall x)Fx$$

and its converse

$$\Box(\forall x)Fx\rightarrow(\forall x)\Box Fx.$$

The Barcan formula can be falsified in structures with growing domains. For example, a model with two worlds, $G$ and one other possible world $H$ extending it. The domain of $G$ is $\{a\}$ and $Fa$ is true in $G$. The domain of $H$ is the set $\{a, b\}$ and $Fa$, but not $Fb$, is true in $H$. In this model $(\forall x)\Box Fx$ but not $\Box(\forall x)Fx$ is true in $G$. To disprove the converse of the Barcan formula we need models with decreasing domains. For example, a model with two worlds $G$ and $H$, where the domain of $G$ is $\{a, b\}$ and the domain of $H$ is $\{a\}$, with $Fa$ and $Fb$ true in $G, Fa$ true in $H$, but $Fb$ false in $H$. This model requires that we assign a truth-value to the formula $Fb$ in the world $H$ where the individual $b$ does not exist (is not in the domain of $H)$. Kripke points out that from a model theoretical point of view this is just a technical choice. (Kripke’s system has no individual constants so our explanation is simplified for brevity; for example, to be exact, we should not say that $Fb$ is true in $H$ but rather that $Fx$ is so true under the assignment of $b$ to $x.$)

Kripke reconstructs a proof of the converse Barcan formula in quantified **T** and shows that the proof goes through only by allowing the necessitation of a sentence containing a free variable. But if free variables are instead to be considered as universally bound, this step is illicit. Necessitating directly an open formula, without first closing it, amounts to assuming what is to be proved. Kripke’s remarks constitute an objection not so much to the rule of Necessitation, but (following Quine) to the theoremhood of open formulas of first-order logic. Prior 1956 contains a proof of the Barcan formula in the alternative formulation

$$\Diamond(\exists x)Fx\rightarrow(\exists x)\Diamond Fx.$$

Kripke does not discuss the details of Prior’s proof. Prior’s proof for the Barcan formula adopts Łukasiewicz’s rules for the introduction of the existential quantifier. The second of these rules states that if $\mvdash A\rightarrow B$ then $\mvdash A\rightarrow(\exists x)B$. Prior applies the rule to

$$\mvdash \Diamond Fx\rightarrow \Diamond Fx$$

and derives

$$\mvdash \Diamond Fx\rightarrow(\exists x)\Diamond Fx$$

which he then necessitates to

$$\mvdash\Box(\Diamond Fx\rightarrow(\exists x)\Diamond Fx).$$

As seen, Kripke objects to the necessitation of open formulas. Indeed, if open formulas are understood as universally closed, $\Diamond Fx\rightarrow(\exists x)\Diamond Fx$ is to be read as $(\forall x)(\Diamond Fx\rightarrow(\exists x)\Diamond Fx)$ and Prior’s proof will not go through. On the other hand, the open formula $\Diamond Fx\rightarrow(\exists x)\Diamond Fx$ is already ‘problematic’ insofar as it does not hold in a model with two worlds $G$ and $H$, where the domain of $G$ is $\{a\}$ and the domain of $H$ is $\{a, b\}$, and where $Fa$ is false in both $G$ and $H$, but $Fb$ is true in $H$. In this model $\Diamond Fx$ is true but $(\exists x)\Diamond Fx$ is false in $G$. In this counter-model $\Diamond Fx$ is made true in $G$ by the individual $b$ that is not in the domain of $G$.

In general, Existential Generalization, for example in the form of Łukasiewicz’s rule that if $\mvdash A\rightarrow B$ then $\mvdash A\rightarrow(\exists x)B$, does not preserve validity if we allow that $Fx$ may be made true at a world by an individual that does not exist there. When discussing the Converse of the Barcan Formula, Kripke blamed the Necessitation of open formulas, though suggesting that the problem lies not so much in the rule of Necessitation but rather in the alleged theoremhood of the open formulas to which it is applied, and by extension in the validity of the rules of existential generalization and universal instantiation. Kripke’s discussion of this question is limited, also because his modal systems do not employ individual constants, which would reinstate the possibility of proving both the Barcan Formula and its Converse without employing theorems with free variables.

The discussion of the Barcan Formula and its Converse has accompanied the development of quantified modal logic, as these formulas are linked both to the technical questions of how to combine Classical Quantification Theory with Modal Logic and how to define validity for quantified modal systems, as well as to the philosophical questions surrounding the variability of domains and the interpretations of the quantifiers. Proof theoretically, the most straightforward combination of classical quantification theory and modal logic makes both the Barcan Formula and its Converse theorems. Model theoretically, intra-model domain variability is a welcome generalization. We do not discuss here the technical solutions open to logicians who wish to build systems sound for variable domains, that is, systems that, like Kripke’s, do not allow proofs of the Barcan and its Converse (Deutsch 1994 and Linsky and Zalta 1994 contain useful overviews of the various technical options; see also the SEP entry on the possibilism-actualism debate)[^deutsch-1994][^linsky-1994].

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

### Introductory Texts

### Primary Literature

### Secondary Literature

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=logic-modal-origins). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/logic-modal-origins/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up this entry topic](https://www.inphoproject.org/entity?sep=logic-modal-origins&redirect=True) at the [Internet Philosophy Ontology Project](https://www.inphoproject.org/) (InPhO). |
> |   | [Enhanced bibliography for this entry](http://philpapers.org/sep/logic-modal-origins/) at [PhilPapers](http://philpapers.org/), with links to its database. |

## Other Internet Resources

- [Basic Concepts in Modal Logic](https://mally.stanford.edu/notes.pdf), by Edward N. Zalta (course notes)
- [Modal Logic Handbook](https://www.csc.liv.ac.uk/~frank/MLHandbook/), by P. Blackburn, J. van Benthem, and F. Wolter

## Related Entries

algebra of logic tradition | Boolean algebra: the mathematics of | logic: algebraic propositional | logic: classical | logic: deontic | logic: hybrid | logic: intensional | logic: many-valued | logic: modal | logic: relevance | logic: temporal | Łukasiewicz, Jan | modality: medieval theories of | possibilism-actualism debate | possible objects | possible worlds | Prior, Arthur

### Acknowledgments

I would like to thank Max Weiss who has assisted me with the initial 2010 version of this entry and Harry Deutsch for constructive feedback on a previous version of the last section of this entry.

[^please-nd]: Please note that the distinction in the bibliography between introductory texts, primary, and secondary literature is partially artificial.

[^blackburn-2001]: Blackburn, Patrick, Maarten de Rijke, and Yde Venema, 2001, *Modal Logic*, Cambridge: Cambridge University Press. doi:10.1017/CBO9781107050884

[^chellas-1980]: Chellas, Brian F., 1980, *Modal Logic: an Introduction*, Cambridge: Cambridge University Press.

[^fitting-1998]: Fitting, M. and Richard L. Mendelsohn, 1998, *First-Order Modal Logic*, Dordrecht: Kluwer Academic Publishers.

[^garson-2013]: Garson, James W., 2013, *Modal Logic for Philosophers*, Cambridge: Cambridge University Press.

[^hughes-1968]: Hughes, G.E. and M.J. Cresswell, 1968, *An Introduction to Modal Logic*, London: Methuen.

[^hughes-1984]: –––, 1984, *A Companion to Modal Logic*, London: Methuen.

[^hughes-1996]: –––, 1996, *A New Introduction to Modal Logic*, London: Routledge.

[^alban-1943]: Alban, M.J., 1943, “Independence of the Primitive Symbols of Lewis’s Calculi of Propositions”, *Journal of Symbolic Logic*, 8(1): 25–26. doi:10.2307/2267978

[^anderson-1957]: Anderson, Alan Ross, 1957, “Independent Axiom Schemata for Von Wright’s M”, *Journal of Symbolic Logic*, 22(3): 241–244. doi:10.2307/2963591

[^barcan-1946a]: Barcan (Marcus), Ruth C., 1946a, “A Functional Calculus of First Order Based on Strict Implication”, *Journal of Symbolic Logic*, 11(1): 1–16. doi:10.2307/2269159

[^barcan-1946b]: –––, 1946b, “The Deduction Theorem in a Functional Calculus of First Order Based on Strict Implication”, *Journal of Symbolic Logic*, 11(4): 115–118. doi:10.2307/2268309

[^barcan-1947]: –––, 1947, “The Identity of Individuals in a Strict Functional Calculus of Second Order”, *Journal of Symbolic Logic*, 12(1): 12–15. doi:10.2307/2267171

[^bayart-1958]: Bayart, Arnould, 1958, “Correction de la Logique Modal du Premier et du Second Ordre S5”, *Logique et Analyse*, 1: 28–45.

[^bayart-1959]: –––, 1959, “Quasi-Adéquation de la Logique Modal du Second Ordre S5 et Adéquation de la Logique Modal du Premier Ordre S5”, *Logique et Analyse*, 2: 99–121.

[^becker-1930]: Becker, Oskar, 1930, “Zur Logik der Modalitäten”, *Jahrbuch für Philosophie und Phänomenologische Forschung*, 11: 497–548.

[^bennett-1954]: Bennett, Jonathan, 1954, “Meaning and Implication”, *Mind*, 63(252): 451–463.

[^bernays-1926]: Bernays, Paul, 1926, “Axiomatische Untersuchung des Aussagenkalküls der *Principia Mathematica*”, *Mathematische Zeitschrift*, 25: 305–320.

[^bernays-1948]: –––, 1948, “Review of Rudolf Carnap’s ‘Modalities and Quantification’ (1946)”, *Journal of Symbolic Logic*, 13(4): 218–219. doi:10.2307/2267149

[^bernays-1950]: –––, 1950, “Review of Rudolf Carnap’s *Meaning and Necessity*”, *Journal of Symbolic Logic*, 14(4): 237–241. doi:10.2307/2269233

[^bull-1964]: Bull, R.A., 1964, “A Note on the Modal Calculi S4.2 and S4.3”, *Zeitschrift für Mathematische Logik und Grundlagen der Mathematik*, 10(4): 53–55. doi:10.1002/malq.19640100403

[^bull-1965]: –––, 1965, “An Algebraic Study of Diodorean Modal Systems”, *Journal of Symbolic Logic*, 30(1): 58–64. doi:10.2307/2270582

[^bull-1966]: –––, 1966, “Than All Normal Extensions of S4.3 Have the Finite Model Property”, *Zeitschrift für Mathematische Logik und Grundlagen der Mathematik*, 12: 341–344. doi:10.1002/malq.19660120129

[^bull-1968]: –––, 1968, “An Algebraic Study of Tense Logics with Linear Time”, *Journal of Symbolic Logic*, 33(1): 27–38. doi:10.2307/2270049

[^carnap-1946]: Carnap, Rudolf, 1946, “Modalities and Quantification”, *Journal of Symbolic Logic*, 11(2): 33–64. doi:10.2307/2268610

[^carnap-1947]: –––, 1947, *Meaning and Necessity*, Chicago: University of Chicago Press, 2ⁿᵈ edition with supplements, 1956.

[^carnap-1963a]: –––, 1963a, “My Conception of the Logic of Modalities”, in Schlipp 1963: 889–900.

[^carnap-1963b]: –––, 1963b, “My Conception of Semantics”, in Schlipp 1963: 900–905.

[^dugundji-1940]: Dugundji, James, 1940, “Note on a Property of Matrices for Lewis and Langford’s Calculi of Propositions”, *Journal of Symbolic Logic*, 5(4): 150–151. doi:10.2307/2268175

[^dummett-1959]: Dummett, M.A.E. and E.J. Lemmon, 1959, “Modal Logics between S4 and S5”, *Zeitschrift für Mathematische Logik und Grundlagen der Mathematik*, 5(5): 250–264. doi:10.1002/malq.19590051405

[^feys-1937]: Feys, Robert, 1937, “Les Logiques Nouvelles des Modalités”, *Revue Néoscolastique de Philosophie*, 40(56): 517–553.

[^feys-1963]: –––, 1963, “Carnap on Modalities”, in Schlipp 1963: 283–297.

[^feys-1965]: –––, 1965, *Modal Logics*, in *Collection de Logique Mathématique* (Volume 4), J. Dopp (ed.), Louvain: E. Nauwelaerts.

[^fine-1974]: Fine, Kit, 1974, “An Incomplete Logic Containing S4”, *Theoria*, 40(1): 23–29. doi:10.1111/j.1755-2567.1974.tb00076.x

[^gödel-1933]: Gödel, Kurt, 1933, “Eine Interpretation des Intuitionistischen Aussagenkalküls”, *Ergebnisse eines Mathematischen Kolloquiums*, 4: pp. 39–40. English translation “An Interpretation of the Intuitionistic Propositional Calculus”, with an introductory note by A.S. Troelstra, in *Kurt Gödel. Collected Works*, Vol. 1: *Publications 1929–1936*, S. Feferman, J.W. Dawson, S.C. Kleene, G.H. Moore, R.M. Solovay, and J. van Heijenoort (eds.), Oxford: Oxford University Press, 1986, pp. 296–303.

[^goldblatt-1975]: Goldblatt, R.I., 1975, “First-order Definability in Modal Logic”, *Journal of Symbolic Logic*, 40(1): 35–40. doi:10.2307/2272267

[^halldén-1948]: Halldén, Sören, 1948, “A Note Concerning the Paradoxes of Strict Implication and Lewis’s System S1”, *Journal of Symbolic Logic*, 13(1): 138–139. doi:10.2307/2267814

[^halldén-1950]: –––, 1950, “Results Concerning the Decision Problem of Lewis’s Calculi S3 and S6”, *Journal of Symbolic Logic*, 14(4): 230–236. doi:10.2307/2269232

[^halldén-1951]: –––, 1951, “On the Semantic Non-Completeness of Certain Lewis Calculi”, *Journal of Symbolic Logic*, 16(2): 127–129. doi:10.2307/2266686

[^hintikka-1961]: Hintikka, Jaakko, 1961, “Modality and Quantification”, *Theoria*, 27(3): 119–28; expanded version in Hintikka 1969: 57–70. doi:10.1111/j.1755-2567.1961.tb00020.x

[^hintikka-1963]: –––, 1963, “The Modes of Modality”, *Acta Philosophica Fennica*, 16: 65–81. Reprinted in Hintikka 1969: 71–86.

[^hintikka-1969]: –––, 1969, *Models for Modalities*, Dordrecht: D. Reidel.

[^jónsson-1951]: Jónsson, Bjarni and Alfred Tarski, 1951, “Boolean Algebras with Operators. Part I”, *American Journal of Mathematics*, 73(4): 891–939. doi:10.2307/2372123

[^jónsson-1952]: –––, 1952, “Boolean Algebras with Operators. Part II”, *American Journal of Mathematics*, 74(1): 127–162. doi:10.2307/2372074

[^kanger-1957]: Kanger, Stig, 1957, *Provability in Logic*, (Acta Universitatis Stockholmiensis, Stockholm Studies in Philosophy, Vol. 1), Stockholm: Almqvist and Wiksell.

[^kripke-1959a]: Kripke, Saul A., 1959a, “A Completeness Theorem in Modal Logic”, *Journal of Symbolic Logic*, 24(1): 1–14. doi:10.2307/2964568

[^kripke-1959b]: –––, 1959b, “Semantical Analysis of Modal Logic” (abstract from the Twenty-Fourth Annual Meeting of the Association for Symbolic Logic), *Journal of Symbolic Logic*, 24(4): 323–324. doi:10.1017/S0022481200123321

[^kripke-1962]: –––, 1962, “The Undecidability of Monadic Modal Quantification Theory”, *Zeitschrift für Mathematische Logik und Grundlagen der Mathematik*, 8(2): 113–116. doi:10.1002/malq.19620080204

[^kripke-1963a]: –––, 1963a, “Semantical Analysis of Modal Logic I. Normal Modal Propositional Calculi”, *Zeitschrift für Mathematische Logik und Grundlagen der Mathematik*, 9(5–6): 67–96. doi:10.1002/malq.19630090502

[^kripke-1963b]: –––, 1963b, “Semantical Considerations on Modal Logic”, *Acta Philosophica Fennica*, 16: 83–94.

[^kripke-1965]: –––, 1965, “Semantical Analysis of Modal Logic II. Non-normal Modal Propositional Calculi”, in *Symposium on the Theory of Models*, J.W. Addison, L. Henkin, and A. Tarski (eds.), Amsterdam: North-Holland, pp. 206–220.

[^kripke-1967a]: –––, 1967a, “Review of E.J. Lemmon ‘Algebraic Semantics for Modal Logics I’ (1966a)”, *Mathematical Reviews*, 34: 1021–1022.

[^kripke-1967b]: –––, 1967b, “Review of E.J. Lemmon ‘Algebraic Semantics for Modal Logics II’ (1966b)”, *Mathematical Reviews*, 34: 1022.

[^lemmon-1957]: Lemmon, E.J., 1957, “New Foundations for Lewis Modal Systems”, *Journal of Symbolic Logic*, 22(2): 176–186. doi:0.2307/2964179

[^lemmon-1966a]: –––, 1966a, “Algebraic Semantics for Modal Logics I”, *Journal of Symbolic Logic*, 31(1): 46–65. doi:10.2307/2270619

[^lemmon-1966b]: –––, 1966b, “Algebraic Semantics for Modal Logics II”, *Journal of Symbolic Logic*, 31(2): 191–218. doi:10.2307/2269810

[^lemon-1977]: Lemon, E.J. (with Dana Scott), 1977, *The “Lemmon Notes”. An Introduction to Modal Logic* (American Philosophical Quarterly Monograph Series, vol. 11), K. Segerberg (ed.), Oxford: Basil Blackwell.

[^lewis-1912]: Lewis, C.I., 1912, “Implication and the Algebra of Logic”, *Mind*, 21(84): 522–531. doi:10.1093/mind/XXI.84.522

[^lewis-1914]: –––, 1914, “The Calculus of Strict Implication”, *Mind*, 23(1): 240–247. doi:10.1093/mind/XXIII.1.240

[^lewis-1918]: –––, 1918, *A Survey of Symbolic Logic*, Berkeley: University of California Press.

[^lewis-1920]: –––, 1920, “Strict Implication—An Emendation”, *Journal of Philosophy, Psychology and Scientific Methods*, 17(11): 300–302. doi:10.2307/2940598

[^lewis-1932]: Lewis, C.I. and C.H. Langford, 1932, *Symbolic Logic*, London: Century; 2ⁿᵈ edition 1959, New York: Dover.

[^jan-1920]: Łukasiewicz, Jan, 1920, “O Logice Trójwartościowej”, *Ruch Filozoficzny*, 5: 170–171.

[^jan-1930]: –––, 1930, “Philosophische Bemerkungen zu Mehrwertigen Systemen des Aussagenkalküls”, *Comptes Rendus des Séances de la Société des Sciences et des Lettres de Varsovie*, 23: 51–77. Translated and reprinted in Łukasiewicz 1970: 153–178.

[^jan-1970]: –––, 1970, *Selected Works*, L. Borkowski (ed.), Amsterdam: North-Holland.

[^jan-1931]: Łukasiewicz, Jan and Alfred Tarski, 1931,“Investigations into the Sentential Calculus”, in Alfred Tarski, 1956, *Logic, Semantics, Metamathematics*, Oxford: Clarendon Press, pp. 38–59.

[^maccoll-1880]: MacColl, Hugh, 1880, “Symbolical Reasoning”, *Mind*, 5(17): 45–60. doi:10.1093/mind/os-V.17.45

[^maccoll-1897]: –––, 1897, “Symbolical Reasoning (II)”, *Mind*, 6(4): 493–510. doi:10.1093/mind/VI.4.493

[^maccoll-1900]: –––, 1900, “Symbolical Reasoning (III)”, *Mind*, 9(36): 75–84. doi:10.1093/mind/IX.36.75

[^maccoll-1906]: –––, 1906, *Symbolic Logic and its Applications*, London: Longmans, Green, and Co.

[^makinson-1966a]: Makinson, David C., 1966a, “How Meaningful are Modal Operators?”, *Australasian Journal of Philosophy*, 44(3): 331–337. doi:10.1080/00048406612341161

[^makinson-1966b]: –––, 1966b, “On Some Completeness Theorems in Modal logic”, *Zeitschrift für Mathematische Logik und Grundlagen der Mathematik*, 12: 379–384. doi:10.1002/malq.19660120131

[^makinson-1969]: –––, 1969, “A Normal Modal Calculus Between T and S4 Without the Finite Model Property”, *Journal of Symbolic Logic*, 34(1): 35–38. doi:10.2307/2270978

[^mckinsey-1934]: McKinsey, J.C.C., 1934, “A Reduction in Number of the Postulates for C.I. Lewis’ System of Strict Implication”, *Bulletin of the American Mathematical Society* (New Series), 40(6): 425–427. doi:10.1090/S0002-9904-1934-05881-6

[^mckinsey-1941]: –––, 1941, “A Solution of the Decision Problem for the Lewis Systems S2 and S4, with an Application to Topology”, *Journal of Symbolic Logic*, 6(4): 117–134. doi:10.2307/2267105

[^mckinsey-1944]: –––, 1944, “On the Number of Complete Extensions of the Lewis Systems of Sentential Calculus”, *Journal of Symbolic Logic*, 9(2): 42–45. doi:10.2307/2268020

[^mckinsey-1945]: –––, 1945, “On the Syntactical Construction of Systems of Modal Logic”, *Journal of Symbolic Logic*, 10(3): 83–94. doi:10.2307/2267027

[^mckinsey-1944-2]: McKinsey, J.C.C. and Alfred Tarski, 1944, “The Algebra of Topology”, *Annals of Mathematics*, 45(1): 141–191. doi:10.2307/1969080

[^mckinsey-1946]: –––, 1946, “On Closed Elements in Closure Algebras”, *Annals of Mathematics*, 47(1): 122–162. doi:10.2307/1969038

[^mckinsey-1948]: –––, 1948, “Some Theorems about the Sentential Calculi of Lewis and Heyting”, *Journal of Symbolic Logic*, 13(1): 1–15. doi:10.2307/2268135

[^montague-1960]: Montague, Richard, 1960, “Logical Necessity, Physical Necessity, Ethics, and Quantifiers”, *Inquiry*, 3(1–4): 259–269. doi:10.1080/00201746008601312

[^nelson-1930]: Nelson, Everett J., 1930, “Intensional Relations”, *Mind*, 39(156): 440–453. doi:10.1093/mind/XXXIX.156.440

[^parry-1934]: Parry, William Tuthill, 1934, “The Postulates for ‘Strict Implication’”, *Mind*, 43(169): 78–80. doi:10.1093/mind/XLIII.169.78

[^parry-1939]: –––, 1939, “Modalities in the Survey System of Strict Implication”, *Journal of Symbolic Logic*, 4(4): 137–154. doi:10.2307/2268714

[^prior-1955]: Prior, Arthur N., 1955, *Formal Logic*, Oxford: Clarendon Press.

[^prior-1956]: –––, 1956, “Modality and Quantification in S5”, *Journal of Symbolic Logic*, 21(1): 60–62. doi:10.2307/2268488

[^prior-1957]: –––, 1957, *Time and Modality*, Oxford: Clarendon Press.

[^prior-1962]: –––, 1962, “Possible Worlds”, *Philosophical Quarterly*, 12(46): 36–43. doi:10.2307/2216837

[^prior-1977]: Prior, Arthur N. and Kit Fine, 1977, *Worlds, Times and Selves*, Amherst, MA: University of Massachusetts Press.

[^quine-1947a]: Quine, W.V., 1947a, “The Problem of Interpreting Modal Logic”, *Journal of Symbolic Logic*, 12(2): 43–48. doi:10.2307/2267247

[^quine-1947b]: –––, 1947b, “Review of *The Deduction Theorem in a Functional Calculus of First Order Based on Strict Implication* by Ruth C. Barcan (1946b)”, *Journal of Symbolic Logic*, 12(3): 95–96. doi:10.2307/2267230

[^quine-1970]: –––, 1970, *Philosophy of Logic*, Cambridge, MA: Harvard University Press.

[^russell-1906]: Russell, Bertrand, 1906, “Review of Hugh MacColl *Symbolic Logic and Its Applications* (1906)”, *Mind*, 15(58): 255–260. doi:10.1093/mind/XV.58.255

[^schlipp-1963]: Schlipp, Paul Arthur (ed.), 1963, *The Philosophy of Rudolf Carnap* (The Library of Living Philosophers: Volume 11), La Salle: Open Court.

[^scroggs-1951]: Scroggs, Schiller Joe, 1951, “Extensions of the Lewis System S5”, *Journal of Symbolic Logic*, 16(2): 112–120. doi:10.2307/2266683

[^segerberg-1968]: Segerberg, Krister, 1968, “Decidability of S4.1”, *Theoria*, 34(1): 7–20. doi:10.1111/j.1755-2567.1968.tb00335.x

[^segerberg-1971]: –––, 1971, *An Essay in Classical Modal Logic*, 3 volumes, (Filosofiska Studier, Vol. 13), Uppsala: Uppsala Universitet.

[^simons-1953]: Simons, Leo, 1953, “New Axiomatizations of S3 and S4”, *Journal of Symbolic Logic*, 18(4): 309–316. doi:10.2307/2266554

[^sobociński-1953]: Sobociński, Boleslaw, 1953, “Note on a Modal System of Feys-von Wright”, *Journal of Computing Systems*, 1(3): 171–178.

[^sobociński-1962]: –––, 1962, “A Contribution to the Axiomatization of Lewis’ System S5”, *Notre Dame Journal of Formal Logic*, 3(1): 51–60. doi:10.1305/ndjfl/1093957059

[^strawson-1948]: Strawson, P.F., 1948, “Necessary Propositions and Entailment-Statements”, *Mind*, 57(226): 184–200. doi:10.1093/mind/LVII.226.184

[^thomason-1973]: Thomason, Richmond H., 1973, “Philosophy and Formal Semantics”, in *Truth, Syntax and Modality*, Hugues Leblanc (ed.), Amsterdam: North-Holland, pp. 294–307.

[^thomason-1973-2]: Thomason, Steven K., 1973, “A New Representation of S5”, *Notre Dame Journal of Formal Logic*, 14(2): 281–284. doi:10.1305/ndjfl/1093890907

[^thomason-1974]: –––, 1974, “An Incompleteness Theorem in Modal Logic”, *Theoria*, 40(1): 30–34. doi:10.1111/j.1755-2567.1974.tb00077.x

[^benthem-1978]: van Benthem, Johan, 1978, “Two Simple Incomplete Modal Logics”, *Theoria*, 44: 25–37. doi:10.1111/j.1755-2567.1978.tb00830.x

[^benthem-1984]: –––, 1984, “Possible Worlds Semantics: A Research Program that Cannot Fail?”, *Studia Logica*, 43: 379–393.

[^wright-1951]: von Wright, G.H., 1951, *An Essay in Modal Logic* (Studies in Logic and the Foundations of Mathematics: Volume V), L.E.J. Brouwer, E.W. Beth, and A. Heyting (eds.), Amsterdam: North-Holland.

[^whitehead-1910]: Whitehead, Alfred North and Bertrand Russell, 1910, *Principia Mathematica* (Volume I), Cambridge: Cambridge University Press.

[^ballarin-2005]: Ballarin, Roberta, 2005, “Validity and Necessity”, *Journal of Philosophical Logic*, 34(3): 275–303. doi:10.1007/s10992-004-7800-2

[^ballarin-2021]: –––, 2021, “Quine on Modality”, in *The Routledge Handbook of Modality*, Otávio Bueno and Scott A. Shalkowski (eds.), New York: Routledge, pp. 390–399.

[^belnap-1981]: Belnap, Nuel D., Jr., 1981, “Modal and Relevance Logics: 1977”, in *Modern Logic: A Survey*, Evandro Agazzi (ed.), Dordrecht: D. Reidel, pp. 131–151. doi:10.1007/978-94-009-9056-2_8

[^blackburn-2007a]: Blackburn, Patrick and Johan van Benthem, 2007a, “Modal Logic: A Semantic Perspective”, in Blackburn, van Benthem, and Wolter 2007b: chapter 1.

[^blackburn-2007b]: Blackburn, Patrick, Johan van Benthem, and Frank Wolter, (eds.), 2007b, *Handbook of Modal Logic* (Studies in Logic and Practical Reasoning: Volume 3), Amsterdam: Elsevier.

[^bull-1984]: Bull, Robert and Krister Segerberg, 1984, “Basic Modal Logic”, in *Extensions of Classical Logic* (Handbook of Philosophical Logic: Volume 2), D.M. Gabbay and F. Guenthner (eds.), Dordrecht: Kluwer, pp. 1–88. doi:10.1007/978-94-009-6259-0_1

[^burgess-2009]: Burgess, John P., 2009, *Philosophical Logic*, Princeton: Princeton University Press.

[^cocchiarella-1975a]: Cocchiarella, Nino B., 1975a, “Logical Atomism, Nominalism, and Modal Logic”, *Synthese*, 31(1): 23–62. doi:10.1007/BF00869470

[^cocchiarella-1975b]: –––, 1975b, “On the Primary and Secondary Semantics of Logical Necessity”, *Journal of Philosophical Logic*, 4(1): 13–27. doi:10.1007/BF00263118

[^copeland-2002]: Copeland, B. Jack, 2002, “The Genesis of Possible Worlds Semantics”, *Journal of Philosophical Logic*, 31(2): 99–137. doi:10.1023/A:1015273407895

[^curley-1975]: Curley, E.M., 1975, “The Development of Lewis’ Theory of Strict Implication”, *Notre Dame Journal of Formal Logic*, 16(4): 517–527. doi:10.1305/ndjfl/1093891890

[^deutsch-1994]: Deutsch, Harry, 1994, “Logic for Contingent Beings”, *Journal of Philosophical Research*, 19: 273–329.

[^goldblatt-2003]: Goldblatt, Robert, 2003, “Mathematical Modal Logic: A View of its Evolution”, in *Logic and the Modalities in the Twentieth Century* (Handbook of the History of Logic: Volume 7), D.M. Gabbay and J. Woods (eds.), Amsterdam: Elsevier, pp. 1–98. [2003, *Journal of Applied Logic*, 1(5–6): 309–392. doi:10.1016/S1570-8683(03)00008-9]

[^kaplan-1966]: Kaplan, David, 1966, “Review of Saul A. Kripke, *Semantical Analysis of Modal Logic I. Normal Modal Propositional Calculi* (1963a)”, *Journal of Symbolic logic*, 31(1): 120–122. doi:10.2307/2270649

[^kaplan-1986]: –––, 1986, “Opacity”, in *The Philosophy of W.V. Quine* (The Library of Living Philosophers: Volume 18), Lewis Edwin Hahn and Paul Arthur Schlipp (eds.), La Salle: Open Court, pp. 229–289.

[^lindström-1996]: Lindström, Sten, 1996, “Modality Without Worlds: Kanger’s Early Semantics for Modal Logic”, in *Odds and Ends. Philosophical Essays Dedicated to Wlodek Rabinowicz on the Occasion of his Fiftieth Birthday*, S. Lindström, R. Sliwinski, and J. Österberg (eds.), Uppsala, Sweden, pp. 266–284.

[^lindström-1998]: –––, 1998, “An Exposition and Development of Kanger’s Early Semantics for Modal Logic”, in *The New Theory of Reference: Kripke, Marcus, and its Origins*, P.W. Humphreys, and J.H. Fetzer (eds.), Dordrecht: Kluwer, pp. 203–233.

[^lindström-2001]: –––, 2001, “Quine’s Interpretation Problem and the Early Development of Possible Worlds Semantics”, *Uppsala Philosophical Studies*, 50: 187–213.

[^lindström-2007]: Lindström, Sten and Krister Segerberg, 2007, “Modal Logic and Philosophy”, in Blackburn, van Benthem, and Wolter 2007b: chapter 1.

[^linsky-1994]: Linsky, Bernard and Edward N. Zalta, 1994, “in Defense of the Simplest Quantified Modal Logic”, *Philosophical Perspectives*, 8: 431–458.

[^linsky-1971]: Linsky, Leonard (ed.), 1971, *Reference and Modality*, Oxford: Oxford University Press.

[^löb-1966]: Löb, M.H., 1966, “Extensional Interpretations of Modal Logic”, *Journal of Symbolic Logic*, 31(1): 23–45. doi:10.2307/2270618

[^rahman-2007]: Rahman, Shahid and Juan Redmond, 2007, *Hugh MacColl: An Overview of his Logical Work with Anthology*, London: College Publications.

[^rescher-1974]: Rescher, Nicholas, 1974, *Studies in Modality*, Oxford: Basil Blackwell.

[^zakharyaschev-2001]: Zakharyaschev, Michael, Krister Segerberg, Maarten de Rijke, and Heinrich Wansing, 2001, “The Origins of Modern Modal Logic”, in *Advances in Modal Logic 2*, M. Zakharyaschev, K. Segerberg, M. de Rijke, and H. Wansing (eds.), Stanford: CSLI Publications, pp. 11–38.
