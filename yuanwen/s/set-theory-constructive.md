# Set Theory: Constructive and Intuitionistic ZF
**First published Fri Feb 20, 2009; substantive revision Thu Feb 22, 2024**

*Crosilla, Laura*

Constructive and intuitionistic Zermelo-Fraenkel set theories are axiomatic theories of sets in the style of Zermelo-Fraenkel set theory (ZF) which are based on intuitionistic logic. They were introduced in the 1970’s and they represent a formal context within which to codify mathematics based on intuitionistic logic (see the entry on constructive mathematics). They are formulated on the standard first order language of Zermelo-Fraenkel set theory and make no direct use of inherently constructive ideas. In working in constructive and intuitionistic ZF we can thus to some extent rely on our familiarity with ZF and its heuristics.

Notwithstanding the similarities with classical set theory, the concepts of set defined by *constructive* and *intuitionistic* set theories differ considerably from that of the classical tradition; they also differ from each other. The techniques utilised to work within them, as well as to obtain metamathematical results about them, also diverge in some respects from the classical tradition because of their commitment to intuitionistic logic. In fact, as is common in intuitionistic settings, a plethora of semantic and proof-theoretic methods are available for the study of constructive and intuitionistic set theories.

This entry introduces the main features of constructive and intuitionistic set theories. As the field is expanding at a fast pace, we can only briefly recall some key aspects of results and available techniques. We focus more on constructive set theory to highlight important foundational issues that arise within it. Note that we omit a conspicuous part of the literature on constructive and intuitionistic ZF which relates to their categorical interpretations. This area has seen major developments over the years, so much so that an adequate treatment of that progress would require a substantial extension of this entry. The interested reader might wish to consult the entry on category theory and its references (see also its supplement programmatic reading guide).

## 1. The Essence of Constructive and Intuitionistic Set Theory

Constructive and intuitionistic Zermelo-Fraenkel set theories are based on intuitionistic rather than classical logic, and represent a natural environment within which to codify and study mathematics based on intuitionistic logic. For constructive ZF, the main focus has been to represent the mathematical practice of Bishop (Bishop 1967, Bishop and Bridges 1985)[^bishop-1967][^bishop-1985].

For the basic concepts and the driving ideas of intuitionistic logic, constructive mathematics and intuitionism, the reader may wish to consult the following entries:

- intuitionistic logic,
- the development of intuitionistic logic,
- constructive mathematics,
- intuitionism in the philosophy of mathematics,
- Luitzen Egbertus Jan Brouwer.

For classical set theory, see the entry on set theory.

Constructive and intuitionistic ZF are based on the same first-order language as classical ZF set theory, which has only the binary predicate symbol $\in$ (membership) as non-logical symbol. That is, they are formulated on the basis of intuitionistic first-order logic with equality, plus the binary predicate symbol $\in$. We can thus take advantage of the simplicity of the set-theoretic language and of our familiarity with it (Myhill 1975)[^myhill-1975]. As with Bishop-style constructive mathematics, Constructive and intuitionistic ZF are *compatible* with the classical tradition, in the sense that all of their theorems are *classically true*. In fact, the two formal systems that we shall consider, Constructive Zermelo-Fraenkel (CZF) and Intuitionistic Zermelo-Fraenkel (IZF), give rise to full classical ZF by the simple addition of the principle of the excluded middle.

### 1.1 Axiomatic freedom

Classical Zermelo-Fraenkel set theory is based on classical first-order predicate logic with equality. On top of the logical principles are axioms and schemata which describe the notion of set the theory codifies. These principles can be classified into three kinds. First, there are principles that enable us to form new sets from given ones. For example, the axiom of pair allows us to form a set which is the pair of two given sets. Secondly, there are principles that establish properties of the set theoretic structure. For example, the axiom of extensionality identifies all sets having the same elements. Third, and finally, there are axioms asserting the existence of specific sets. Thus the axiom of infinity states that there is an infinite set. These principles all together are usually called the set-theoretic principles.

When introducing versions of ZF based on intuitionistic logic, the first step is to eliminate from the logic the principle of the excluded middle (EM). The next step is to choose a good stock of set-theoretic principles which faithfully represent the desired notion of constructive set. These tasks turn out to be more challenging than one at first might have expected. In fact, as is well known, systems based on a “weaker” logic have the ability to distinguish between statements which are equivalent from the point of view of a “stronger” logic. In the case of set theory, some of the ZF axioms or schemata are often presented by one of many classically equivalent formulations. Classically it is only a matter of convenience which one to use at a specific time. When working on the basis of intuitionistic logic, however, various formulations of a classical axiom may turn out to be distinct (non-equivalent). In fact, one can envisage new statements which are classically equivalent to a ZF axiom but intuitionistically separate from it (for example CZF’s subset collection axiom (Aczel 1978)[^aczel-1978]).

As to the first step, consisting in eliminating the principle of excluded middle from the logic, it turns out that simply evicting this principle from the underlying logic is insufficient; that is, it is not enough to take the intuitionistic rather than the classical predicate calculus as our basis. We also need to ensure that the set theoretic axioms do not bring undesirable forms of excluded middle back into our theory. For example, as noted by Myhill (1973), we need extra care in choosing an appropriate statement for the axiom of foundation. Foundation is introduced in set theory to rule out sets which are members of themselves and thus $\in$-chains of sets. The usual formulation of foundation asserts that each inhabited set (a set with at least one element) has a least element with respect to the membership relation. This statement, however, can be shown to yield constructively unacceptable instances of excluded middle on the basis of modest set-theoretic assumptions. Therefore the usual formulation of foundation has to be omitted from a set theory based on intuitionistic logic. For a proof, see the supplementary document:

> [Set-theoretic principles incompatible with intuitionistic logic](set-theory-constructive.incompatible-set-axs.md).

The typical move in formulating set theories based on intuitionistic logic is then to replace foundation with the classically equivalent schema of set induction, which does not have the same “side effects” but has similar consequences.[^note-1]

As to the second step, related to the selection of a good stock of set-theoretic principles, the schemata of replacement and separation, and the axiom of power set have attracted most attention. For the exact formulation of these principles see the supplementary document:

> [Axioms of CZF and IZF](set-theory-constructive.axioms-CZF-IZF.md).

Here the following is a typical scenario. Given what are classically two variants of a single set-theoretic principle, their classical proof of equivalence requires at some point an instance of the excluded middle. However, in general this proof of equivalence will not carry through to an intuitionistic context, and thus what are classically two forms of one principle may result into two distinct principles when working intuitionistically. Choosing one rather than the other of them may therefore influence the notion of set we thus define. In the context of *constructive* set theories like CZF, power set and separation are replaced by intuitionistically weaker principles. One reason for this is that the full strength of power set and full separation are seen as unnecessary, since their weaker substitutes seem to suffice for carrying out constructive mathematics. Another reason is that they are seen as philosophically problematic, since they may introduce forms of impredicativity within the set theory (see the section on Predicativity in constructive set theory). The case of replacement versus collection is somehow more complex (see, for example, the articles (Friedman and Scedrov 1985)[^friedman-1985][^scedrov-1985], (Rathjen 2005)[^rathjen-2005] and (Rathjen 2012)[^rathjen-2012]). It is worth stressing that while adopting the usual formulation of foundation goes against the very assumption of intuitionistic logic as background logic, the principles of separation and power set have no incompatibility with intuitionistic logic at all, so much so that they are integral part of the intuitionistic theory of sets IZF (Friedman 1973a)[^friedman-1973a].

To summarise, in formulating a set theory based on intuitionistic logic, the first task is to expel the principle of excluded middle, including those instances of it which might be hidden in familiar formulations of set-theoretic axioms. The next task is to choose one version of each classical principle which best characterises the desired notion of set. This opens up a range of choices one can make, as a plurality of intuitionistic principles may correspond to one classical principle. It should be stressed that from a constructive point of view this plurality of options (and thus systems), rather than causing uneasiness, is a highly desirable situation, as it constitutes a form of “axiomatic freedom”. For example, it allows us to differentiate between a number of mathematical notions, thus better capturing our intuitions of them as distinct. It also gives us the freedom to choose the notions and theories which best suit a given context. In addition, by adopting intuitionistic logic we can include within our theories principles which are classically very strong, without having to commit to their classical strength. For example, one can add a notion of inaccessible set to a weak constructive set theory and obtain a predicative theory, while the same notion embedded in a classical context becomes extremely strong (see the sections on Predicativity in constructive set theory and Large sets in constructive and intuitionistic ZF). Finally, a rich area of (meta-theoretical) study of the relations between the resulting distinct set-theoretic systems naturally arises. As one could expect, this freedom also has a price, as a highly technical study of the axiomatic theories might be necessary to distinguish their principles as well as to unveil some of their subtleties. This again can be seen as an advantage, since it forces us to a deeper and clearer analysis of the mathematical notions involved and prompts us to develop new sophisticated tools.

### 1.2 Constructive versus intuitionistic set theory

Although there are many systems of sets based on intuitionistic logic, we can distinguish two main trends within the literature. According to the first one, we take all of what is available in classical ZF set theory and only modify those principles, such as foundation, which have a clear incompatibility with intuitionistic logic. This gives rise to set theories such as Intuitionistic Zermelo-Fraenkel, IZF, a variant of which was introduced as early as in (Friedman 1973a)[^friedman-1973a]. (See Beeson 1985, Chapters 8 and 9 and Scedrov 1985 for two surveys on IZF.)[^beeson-1985][^scedrov-1985] The rationale behind these theories appears to be that of granting the mathematician the most powerful tools possible, as long as compatibility with intuitionistic logic is preserved. According to the second approach, in addition to the adherence to intuitionistic logic we also introduce restrictions on the set-theoretic principles admitted, as far as the resulting system complies with the constructive mathematical practice. Theories of this second kind can thus be seen as the outcome of a double process of restriction with respect to classical ZF. First there is a restriction to intuitionistic logic, then a restriction is imposed on the set-theoretic constructions allowed. The latter is motivated by (1) the observation that weaker principles appear to suffice for the constructive mathematical practice and (2) the desire to adhere to a form of predicativity (see the next section for a clarification of this notion of predicativity). Paradigmatic examples of the latter kind of systems are Myhill’s Constructive Set Theory (Myhill 1975)[^myhill-1975], Friedman’s system B (Friedman 1977)[^friedman-1977] and Aczel’s Constructive Zermelo-Fraenkel set theory CZF (Aczel 1978; 1982; 1986, Aczel & Rathjen 2001; Aczel & Rathjen 2010, Other Internet Resources)[^aczel-1978][^aczel-2001]. We can also say that in this second approach the foundational motivation influences the practice to a higher degree.

In the following, we make use of a convention which is often in place today, according to which the adjective “intuitionistic” refers to those set theories, such as IZF, which are impredicative, while “constructive” refers to set theories, such as CZF, which comply with a form of predicativity. Note, however, that this convention is not always followed in the literature. In fact, the adjective “constructive” has also been used to denote impredicative theories, and “intuitionistic” to refer to predicative foundational theories such as Martin-Löf type theory (Martin-Löf 1975; 1984)[^martin-löf-1975]. It is also worth noting that the present convention on the use of the words “constructive” and “intuitionistic” differs from that made in the context of constructive mathematics (see, for example, the entry on constructive mathematics and also Bridges and Richman 1987)[^bridges-1987].

### 1.3 Predicativity in constructive set theory

Predicativism has its origins in the writings of Poincaré and Russell, who responded to the paradoxes that were discovered in Cantor’s and Frege’s set theories in the early 20th century. Subsequently Weyl made fundamental contributions to the study of predicative mathematics (Weyl 1918, see also Feferman 1988)[^feferman-1988][^weyl-1918]. According to one notion, a definition is *impredicative* if it defines an object by reference to a totality which includes the object to be defined. With his Vicious Circle Principle (VCP), Russell intended to eliminate the circularity in mathematics that arises from such impredicative definitions. Russell gave various formulations of the VCP, one of which is:

> Whatever contains an apparent variable must not be a possible value of that variable (Russell 1908, in van Heijenoort 1967, 163)[^heijenoort-1967][^russell-1908].

Poincaré, Russell and Weyl’s foundational analysis of predicativity has paved the way for a variety of logical analyses of the notion. The most commonly accepted analysis is due to Feferman and Schütte (independently) following lines indicated by Kreisel (Kreisel 1958, Feferman 1964 and Schütte 1965; 1965a)[^feferman-1964][^kreisel-1958][^schütte-1965]. Here proof theory has played a pivotal role. In very rough terms, the idea was to single out a collection of theories (a transfinite progression of systems of ramified second order arithmetic indexed by ordinals) by means of which to characterise a certain notion of predicative ordinal. Feferman and Schütte’s proof theoretic analysis of these theories has identified an ordinal, usually referred to as $\Gamma_0$, which is the least non-predicative ordinal according to this notion. A formal system is considered *predicatively justifiable* if it is proof-theoretically reducible to a system of ramified second order arthmetic indexed by an ordinal less then $\Gamma_0$. Therefore in proof theory $\Gamma_0$ is usually considered as representing the limit of predicativity. (See Feferman 2005 for a more accurate informal account of this notion of predicativity and for further references. See also Crosilla 2017. The reader may also consult the section on predicativism in the entry on philosophy of mathematics and the entry on paradoxes and contemporary logic)[^crosilla-2017][^feferman-2005].

For *constructive* foundational theories a more “liberal” approach to predicativism has been suggested, starting from work in the late 1950’s of Lorenzen, Myhill and Wang (see *e.g.* Lorenzen and Myhill 1959)[^lorenzen-1959]. The driving idea is that so-called *inductive definitions* ought to be allowed in the realm of constructive mathematics. The intuitive justification of inductive definitions is related to the fact that they can be expressed by means of finite rules, in a “bottom-up” way. The proof-theoretic strength of theories of inductive definitions goes well beyond Feferman and Schütte’s bound (Buchholz, Feferman, Pohlers and Sieg 1981)[^buchholz-1981]. Thus relatively strong theories are considered predicative in today’s foundations of constructive mathematics. This more liberal notion of predicativity has often been termed *generalised predicativity*. (See Crosilla 2022 for discussion)[^crosilla-2022]. In this entry we simply write *predicativity* for generalised predicativity and call *predicativity given the natural numbers* the better known form of predicativity which arises in the classical context and was analysed by Kreisel, Feferman and Schütte.

An example of a predicative theory in this sense is the constructive set theory CZF, as its proof-theoretic strength is the same as that of a theory of one inductive definition known as ID$_1$. The system IZF, instead, is impredicative, as its proof-theoretic strength equates that of the whole of classical ZF (Friedman 1973a)[^friedman-1973a].

In set theories based on intuitionistic logic, predicativity is usually achieved by restricting the principles of separation and power set, as these appear to be the main sources of impredicativity (when the infinity axiom is assumed).

#### 1.3.1 Impredicativity of Separation

The schema of separation allows us to form a subset of a given set whose elements satisfy a given property (expressed by a formula in the language of set theory). Given a set $B$ and a formula $\phi(X)$, separation allows us to construct a new set, the set of those elements $X$ of $B$ for which $\phi$ holds. This is usually informally represented as: $\{X \in B : \phi(X)\}$. Separation may lead to impredicativity in case the formula $\phi$ contains unbounded quantifiers ranging over the whole universe of sets; in fact, in defining the new set by separation we may thus refer to this very set, contradicting Russell’s VCP. For example, if we define a set $C$ by separation as $\{X\in B : \forall Y \psi(X,Y)\}$, then $C$ is among the $Y$’s that need to be checked for the property $\psi$. This form of impredicativity is avoided in constructive set theory by restricting the separation schema: by requiring that all quantifiers occurring in the formula $\phi$ range only over “previously constructed” sets. Syntactically, this means that given a set $B$, we can form a new set $\{X \in B : \phi(X)\}$ by separation only if all quantifiers in $\phi$ are bounded; that is, only if all quantifiers in $\phi$ are of the form $\forall X (X\in Y \rightarrow \ldots)$ or $\exists X(X\in Y \wedge \ldots)$, for some set $Y$.

We can confirm that constraining separation in this way avoids impredicativity, by observing that the proof theoretic strength of CZF, which has only restricted separation, is within the range of predicativity. However, by adding full separation to CZF one obtains an impredicative theory, in fact, one with the same proof-theoretic strength as full second order arithmetic (Lubarsky 2006)[^lubarsky-2006]. See also Section 5 for a discussion of the role of proof theory in analysing constructive and intuitionistic set theories.

#### 1.3.2 Impredicativity of Powerset

The power set axiom allows us to form a *set* of all subsets of a given set. An example of impredicative use of power set is given by the definition of a subset of the natural numbers, $N$, as follows: $B := \{n \in N : \forall C \subseteq N \phi(n, C)\}$, where $\phi$ can be taken to be a bounded formula. A form of circularity arises here as $B$ itself is among the subsets of $N$ which need to be checked for $\phi$. As emphasized by Myhill (1975, 354), power set is hard to justify from a constructive point of view: it gathers together all the subsets of a given set, but does not prescribe a rule that "constructs" the set out of previously given sets, as predicativity would seem to require.

Myhill writes:

> Power set seems especially nonconstructive and impredicative compared with the other axioms: it does not involve, as the others do, putting together or taking apart sets that one has already constructed but rather selecting out of the totality of all sets those that stand in the relation of inclusion to a given set. (Myhill 1975, 351)[^myhill-1975].

Power set seems particularly problematic in the case of infinite sets, as "we have no idea of what an arbitrary subset of an infinite set is; there is no way of generating them all and so we have no way to form the set of all of them" (Myhill 1975, 354)[^myhill-1975]. As a consequence, there seems to be no way of giving constructive sense to the set of all subsets of an infinite set.

Myhill crucially observes that power set is not needed for constructive mathematics Bishop-style, as it can be replaced by one of its consequences. This is often called Myhill’s *exponentiation axiom* and states that we can form a *set* of all functions from one given set to another. This axiom is clearly equivalent to power set in a classical context, where subsets of a given set may be represented by characteristic functions. In the absence of the principle of excluded middle, however, power set and exponentiation are not equivalent. Myhill’s fundamental observation is that exponentiation suffices to carry out the mathematics of (Bishop 1967)[^bishop-1967]; for example, it allows for the construction of the (Cauchy) real numbers within constructive set theory. Myhill claims that exponentiation is constructively meaningful because a function is a rule, a finite object which can actually be given.

He also writes that the case of power set is different from that of exponentiation as:

> even in the case of infinite sets $A$ and $B$ we do have an idea of an arbitrary mapping from $A$ into $B$. An arbitrary mapping from $\mathbf{Z}$ into $\mathbf{Z}$ is a partial recursive function together with a proof that the computation always terminates; a similar account can be given of an arbitrary real function. There is no corresponding explanation of “arbitrary *subset*”. (Myhill 1975, 354)[^myhill-1975].

Myhill’s exponentiation axiom is now part of all major systems of constructive set theory. In the case of CZF, in fact, one has a strengthening of exponentiation, known as subset collection, which is also a weakening of power set. A generalisation of exponentiation can also be found in constructive type theory.

In the case of CZF, the claim that adding the power set axiom induces impredicativity can be substantiated by a technical result. Rathjen (2012b) shows that CZF augmented by the power set axiom exceeds the strength of classical Zermelo set theory, and thus the addition of the power set axiom to CZF brings us to a fully impredicative theory. This also shows that the implication from power set to subset collection can not be reversed, as CZF’s proof-theoretic strength is way below that of Zermleo set-theory. In other terms, the power set axiom is much stronger than both exponentiation and subset collection.

#### 1.3.3 The constructive universe of sets

Having introduced appropriate constraints to power set and separation, we could now face a substantial objection. Constructive and intuitionistic set theories can be seen as modifications of classical ZF set theory that are obtained by: (1) replacing classical with intuitionistic logic, and (2) accurately choosing, among various classically equivalent principles, those which seem more appropriate for given purposes. For example, we might choose principles which suffice to represent a certain mathematical practice, like, for example, Bishop style mathematics. The resulting notion of set, however, might become obscure and the choice of the set-theoretic principles might appear to a certain degree as arbitrary. In the case of intuitionistic ZF, one can justify the choice of the set-theoretic principles by examining its semantical interpretations, as Heyting semantics, or by looking at its categorical models. In the case of constructive set theory, to hinder this kind of objection, Aczel has given an interpretation of CZF in a version of Martin-Löf type theory (Aczel 1978)[^aczel-1978]. The claim is that a clear constructive meaning is thus assigned to CZF’s notion of set by looking at its meaning in Martin-Löf type theory, since the latter is usually considered as representing an accurate and fully motivated formulation of a constructive notion of set. Aczel’s interpretation of CZF in constructive type theory is given by interpeting sets as *trees* in type theory. That is, in constructive type theory the universe of sets of CZF is represented by a type, V, of iterative sets built over the universe, U, of small types (Aczel 1978; Martin-Löf 1984)[^aczel-1978][^martin-löf-1984]. This interpretation clearly highlights the (generalised) predicativity of CZF, whose sets can be seen as trees built up inductively, and whose set theoretic universe also has a clear inductive structure.

The predicativity of CZF and related systems is consonant with philosophical positions which are often associated with the use of intuitionistic logic. For example, it would seem that if we *construct* the mathematical objects, resorting to impredicative definitions would produce an undesirable form of circularity (see, e.g., (Gödel 1944)[^gödel-1944]). This clearly contrasts with a view often associated with classical set theory, for which our mathematical activity can be seen as a gradual disclosure of properties of the universe of sets, whose existence is independent from us. Such a view is usually bound up with the use of classical logic and impredicativity in studying the set-theoretic universe. Predicativity is also often seen as related to the time-honoured distinction between actual and potential infinity. Predicative (and thus, in particular, constructive) theories are often seen as avoiding reference to actual infinity, and only committing to potential infinity (Dummett 2000, Fletcher 2007, Feferman 1964)[^dummett-2000][^feferman-1964][^fletcher-2007]. This again seems particularly in harmony with those philosophical positions which highlight the human dimension of our mathematical activity, by seeing, for example, the mathematical objects and the truth of statements about them as dependent on us. Another related aspect is often seen as pertaining to predicativity: if the universe of sets is built up in stages by our own mathematical activity, then it would be natural also to see it as *open ended*. For this reason, in a constructive context, where the rejection of classical logic meets the requirement of predicativity, the universe of sets is often described as an open concept, a universe “in fieri”. This idea is especially well exemplified within constructive type theory, where the notion of type-theoretic universe has been deliberately left open by Per Martin-Löf (by not postulating specific elimination rules for it). The open ended nature of the universe of sets has paved the way for extensions of it by reflection principles. These have been investigated both within type theory and constructive set theory. See (Rathjen 2005a)[^rathjen-2005a] for a survey of results and a foundational discussion, and also section 5.2. For a formal analysis of the constructive universe of sets and a comparison with the Von Neumann hierarchy, see (Ziegler 2014)[^ziegler-2014].

## 2. Origins of Constructive and Intuitionistic Set Theories

Intuitionistic versions of Zermelo-Fraenkel set theories were introduced in the early 1970s by Friedman and Myhill. In (Friedman 1973)[^friedman-1973] the author presents a study of formal properties of various intuitionistic systems and introduces for them an extension of Kleene’s realisability method. The realisability technique is applied in (Myhill 1973)[^myhill-1973] to show the existence property for a version of intuitionistic Zermelo-Fraenkel set theory (with replacement in place of collection). In another fundamental contribution Friedman extends the double negation translation of intuitonistic logic to relate classical and intuitionistic set theories (Friedman 1973a)[^friedman-1973a]. These first papers already address the relation between some major intuitionistic set theories and classical ZF. They also clarify a key feature of set theory based on intuitionistic logic, mainly that it is amenable to powerful constructive semantic interpretations, like realizability. These techniques are applied to the study of crucial metatheoretical properties which are typical of the constructive approach and which are enjoyed by some constructive and intuitionistic set theories (see the section on Semantic techniques). This groundbreaking work has been fully exploited and substantially extended in work by, among others, Beeson, McCarty and Rathjen (see, e.g., Beeson 1985; McCarty 1984, Rathjen 2005, 2005b, 2006b, 2012)[^beeson-1985][^mccarty-1984][^rathjen-2005][^rathjen-2005b][^rathjen-2006b][^rathjen-2012].

Constructive set theory from the very start has a more distinctive foundational vocation and it is bound up with Bishop’s mathematics. In fact, in 1967 Bishop published the book “Foundations of constructive analysis” (Bishop 1967)[^bishop-1967], which opened up a new era for mathematics based on intuitionistic logic (see the entry on constructive mathematics). The monograph stimulated fresh attempts in the logical community to clarify and formally represent the principles which were used by Bishop, though only at an informal level. First attempts by Goodman and Myhill (Goodman and Myhill 1972)[^goodman-1972] made use of versions of Gödel’s system T (see also (Bishop 1970)[^bishop-1970] for a similar attempt). Myhill, however, reached the conclusion that the resulting formalisation was too complex and artificial (Myhill 1975, 347)[^myhill-1975]. Myhill proposed instead a system which is closer to the informal notion of set originally utilised by Bishop and also closer to the set-theoretic tradition. Myhill writes (1975, 347):

> We refuse to believe that things have to be this complicated - the argumentation of (Bishop 1967)[^bishop-1967] looks very smooth and seems to fall directly from a certain concept of what sets, functions, etc. are, and we wish to discover a formalism which isolates the principles underlying this conception in the same way that Zermelo-Fraenkel set theory isolates the principles underlying classical (nonconstructive) mathematics. We want these principles to be such as to make the process of formalization completely trivial, as it is in the classical case.

We observe here that Myhill’s constructive set theory had distinguished notions of function, natural number and set; it thus closely represented a constructive tradition in which functions and natural numbers are conceptually independent from sets. Another fundamental step in the development of constructive set theory was Friedman’s “Set-theoretical foundations for constructive analysis” (Friedman 1977)[^friedman-1977]. Here, among other systems, a system called B is defined which has further restrictions on the set-theoretic principles compared with Myhill’s (in particular, it has no set induction). It also has a restricted form of the axiom of dependent choice. System B is there shown to be expressive enough to represent the constructive analysis of Bishop (1967) whilst being at the same time proof-theoretically very weak (due to the absence of set induction). System B is in fact a conservative extension of arithmetic (thus it is well below the limit of predicativity given the natural numbers briefly recalled in section 1.3). Myhill and Friedman’s systems were subsequently modified by Aczel, to obtain a system, CZF (Constructive Zermelo-Fraenkel), that is fully compatible with the ZF language (Aczel 1978, 1982, 1986; Aczel and Rathjen 2001; 2010)[^aczel-1978][^aczel-1982][^aczel-1986][^aczel-2001]. CZF also included no choice principles. Aczel gave an interpretation of CZF in Martin-Löf type theory with the aim of corroborating the constructive nature of the set theory. He also strengthened some of the principles of Myhill’s system (namely, collection and exponentiation) on the ground that the stronger versions are still validated by the interpretation in type theory.

Other foundational systems for Bishop-style constructive mathematics were introduced in the early 1970’s. For example: *explicit mathematics* by S. Feferman (Feferman 1975)[^feferman-1975], and the already mentioned *Intuitionistic Type Theory* (Martin-Löf 1975; 1984)[^martin-löf-1975]. Constructive type theory is usually considered the most satisfactory foundation for constructive mathematics Bishop-style. Both type theory and explicit mathematics can be seen as expressing more directly the computational content of constructive mathematics. Type theory, in particular, can be read as a very general and expressive programming language. Constructive and intuitionistic set theories display their computational content only indirectly through their semantic interpretations (see *e.g.* (Aczel 1977), (Lipton 1995)[^lipton-1995] and the section on Semantic techniques).

## 3. The Axioms Systems CZF and IZF

For a reader who is already familiar with ZF set theory, we now briefly recall the axioms of the systems CZF and IZF. For a full list and an explanation of their axioms we refer instead to the supplementary document:

> [Axioms of CZF and IZF](set-theory-constructive.axioms-CZF-IZF.md).

CZF and IZF are formulated on the basis of intuitionistic first-order logic with equality, having only $\in$ (membership) as an additional non-logical binary predicate symbol. Their set-theoretic axioms are as follows.

| $\mathbf{IZF}$ | $\mathbf{CZF}$ |
| --- | --- |
| Extensionality | *(same)* |
| Pair | *(same)* |
| Union | *(same)* |
| Infinity | *(same)* |
| Separation | Restricted Separation |
| Collection | Strong Collection |
| Powerset | Subset Collection |
| Set Induction | *(same)* |

Note that in IZF the schema of separation is unrestricted. In CZF, Collection is strengthened to compensate for restricted separation. Subset collection is a strengthening of Myhill’s exponentiation axiom, thus substituting for ZF’s Powerset.

## 4. Constructive Choice Principles

When discussing the role of classical set theory as a foundation for mathematics, one usually considers the theory ZFC, that is, the axiom system ZF plus the axiom of choice (AC). One might therefore wonder what is the status of the axiom of choice in intuitionistic settings. The question is particularly significant because at its first appearance the axiom of choice was often seen as controversial and highly non-constructive. In constructive contexts, however, one witnesses a peculiar phenomenon. The usual form of the axiom of choice is validated by theories of types such as Martin-Löf type theory, where the Curry-Howard correspondence holds (See Section 3.4 of the entry on constructive mathematics). On the other hand, the assumption of the axiom of choice gives rise to instances of the excluded middle in *extensional* contexts, where a form of separation is also available. This is the case, for example, of constructive and intuitionistic ZF. (For the proof, see the supplementary document on [Set-theoretic Principles Incompatible with Intuitionistic Logic](set-theory-constructive.incompatible-set-axs.md).) A proof of the incompatibility of AC with extensional set theories based on intuitionistic logic seems to have first appeared in (Diaconescu 1975)[^diaconescu-1975] in a categorical context. Goodman and Myhill give an argument for set theories based on intuitionistic logic (Goodman and Myhill 1978)[^goodman-1978].

Although the axiom of choice is incompatible with both constructive and intuitionistic ZF, other choice principles may be added to the basic systems without producing the same undesirable results. For example one could add the principle of *countable choice* (AC$_0)$ or that of *dependent choice* (DC). In fact, both have been often employed in the constructive mathematical practice. (For their exact formulation see the supplementary document on Axioms of CZF and IZF.)

In (Aczel 1978)[^aczel-1978] the author also considered a choice principle called the *Presentation Axiom*, which asserts that every set is the surjective image of a so-called *base*. A base is a set, say $B$, such that every relation with domain $B$ extends a function with domain $B$.

The compatibility of all these forms of choice with constructive set theory has been proved by Aczel by extending his interpretation of CZF in Martin-Löf type theory (Aczel 1982)[^aczel-1982]. Rathjen (2006) has also considered various constructive choice principles and their mutual relations.

A final remark: although constructive and intuitionistic set theories are compatible with the principles of choice just mentioned, the set theories are often defined without any choice principles. This has the aim of allowing for a “pluralistic” foundational approach. In particular, one would like to obtain a foundational theory compatible with those contexts (*e.g.* categorical models of set theory) in which even these weaker principles of choice may not be validated. For similar ideas in the context of constructive type theory, see (Maietti and Sambin 2005, Maietti 2009)[^maietti-2009][^maietti-2005]. We wish also to mention here Richman’s appeal for a constructive mathematics which makes no use of choice principles (Richman 2000; 2001)[^richman-2000].

## 5. Proof Theory and Semantics of Constructive and Intuitionistic ZF

In considering a certain mathematical practice (or a theory used to codify it) from a philosophical perspective, we need to clarify with the greatest possible precision the assumptions which are made within it as well as the consequences which arise from those assumptions. This is particularly true when working with theories which are based on a weaker logic than the classical one, for which a deeper, more precise insight is mandatory. Many technical tools are available which can help us clarify those aspects. Among the available instruments, there are proof-theoretic techniques, such as proof-theoretic interpretations, as well as semantic techniques, such as realisability, Kripke models, Heyting-valued semantics. In fact, in the literature one often witnesses the interplay of proof-theoretic and semantic techniques. We here give a cursory look into some of these topics and suggest further reading.

### 5.1 Proof-theoretic strength

A fundamental theme in proof theory (in particular in the branch of this discipline known as ordinal analysis) is the classification of theories by means of transfinite ordinals which measure their "consistency strength" and "computational power". These ordinals give an indication of how strong a theory is, and therefore offer a way of comparing different theories. For example, the ordinal $\varepsilon_0$ is the proof-theoretic ordinal of Peano Arithmetic, and is much smaller than the ordinal $\Gamma_0$, usually referred to as "the limit of predicativity" (see section 1.3 above). This is indicative that there are predicatively acceptable theories which are much stronger than Peano Arithmetic.

As discussed in section 1, the step from classical ZF to its intuitionistic variants requires us to choose a suitable formulation for each set-theoretic axiom: one classical axiom may have a number of intuitionistic variants which turn out to be non-equivalent to each other. This is sometimes reflected by the proof-theoretic strength of the resulting theories, which may vary depending on which principles we choose. For example, we already noted that in CZF we do not have full separation and power set, which are replaced by the predicatively acceptable principles of bounded separation and subset collection, respectively. However, if we add to CZF either of these principles, we obtain impredicative theories. The impredicativity of the resulting theories is witnessed by the fact that their proof-theoretic strenght far exceeds that of CZF.

It is not surprising that investigations on the proof-theoretic strength of constructive and intutionistic set theories have been a crucial meta-theoretical tool for understanding these theories and their relations with each other. Investigations on the proof-theoretic strength of a theory are rich and informative. In particular, Feferman (1993) has argued that a proof-theoretic analysis may help us establish whether a certain theory complies with a given philosophical framework: for example, the analysis may reveal that a theory is predicative or finitistic etc. Furthermore, as a by-product of the proof-theoretic analysis we sometimes obtain simple independence proofs. In fact, we can show that a theory cannot prove a specific principle because adding it to the theory would increase the theory’s proof-theoretic strength. For example, CZF does not prove the powerset axiom, as the addition of powerset to CZF gives rise to a much stronger theory. Proof-theoretic interpretations have also been employed to compare constructive and intuitionistic ZF set theories among each others, as well as with their classical counterparts, and also with other foundational systems for constructive mathematics, such as constructive type theory and explicit mathematics (see e.g., Griffor and Rathjen 1994, Tupailo 2003)[^griffor-1994][^rathjen-2003][^tupailo-2003]. For a definition of the notion of proof-theoretic strength and for surveys on proof theory see, for example, (Rathjen 1999, 2006b)[^rathjen-1999][^rathjen-2006b].

Although CZF and IZF are the most widely studied systems, numerous other systems for constructive and intuitionistic set theory have been considered in the literature so far. The proof-theoretic strength of a number of constructive and intuitionistic set theories has been established by a variety of tools, like, for example, an extension to set theory of the double negation interpretation (originated in (Friedman 1973a)[^friedman-1973a]), and a variety of other proof-theoretic interpretations, often resulting from a careful combination of semantic and proof theoretic techniques. In many cases the proof theoretic strength of a system has been determined by a chain of interpretations between constructive and classical systems, and by using a variety of tools, from relisability to more "traditional" proof theoretic techniques, as ordinal analysis (see, for example, Beeson 1985; Griffor and Rathjen 1994; Rathjen 2012b)[^beeson-1985][^griffor-1994][^rathjen-2012b]. In particular, realisability has turned out to be very useful, due to its flexibility. As to the outcomes of these investigations, some of the systems analysed turn out to be as weak as arithmetic, as, for example, Friedman’s system B (Friedman 1977)[^friedman-1977]; other systems are as strong as full classical ZF, as IZF (Friedman 1973a)[^friedman-1973a]. There are also systems of intermediate strength, as CZF. The strength of the latter theory, in fact, equals that of a theory of one inductive definition known as ID$_1$. The fact that CZF has the same strength as ID$_1$ is taken to confirm the (generalised) predicativity of the set theory, and to prove that it exceeds the limit of predicativity given the natural numbers, since ID$_1$’s proof theoretic ordinal is well above $\Gamma_0$.

As a final remark: while the strength of CZF is well below that of second-order arithmetic, the simple addition of excluded middle to CZF gives us (full) ZF. This should be contrasted with IZF, which already has the strength of ZF (Friedman 1973a)[^friedman-1973a]. The limited proof theoretic strength of CZF compared with IZF has often been considered one of the main advantages of constructive over intuitionistic set theory. In a sense, it would seem that CZF makes the most of its use of intuitionistic logic, as it characterises a notion of (generalised) predicative set which is sufficiently strong for the development of much of constructive mathematics but also weak enough to avoid impredicativity. Interestingly, when some large set axioms have been added to constructive set theory, a similar pattern has emerged, as the strength of the resulting theory is well below that of the corresponding classical theory.

### 5.2 Large sets in constructive and intuitionistic ZF

A prominent area of research in classical set theory is that of large cardinals (see the entry on set theory). In constructive contexts, the ordinals are not linearly ordered. (For the notion of constructive ordinal and a brief discussion of its properties, see the supplementary document on: [Set-theoretic Principles Incompatible with Intuitionistic Logic](set-theory-constructive.incompatible-set-axs.md).) As a consequence, cardinal numbers do not play the same role as in the classical setting.

One can nonetheless study the impact of *large set axioms* over intuitionistic and constructive set theories. For example, one can add to constructive and intuitionistic set theories an axiom asserting the existence of inaccessible sets, which classically correspond to strongly inaccessible levels of the von Neumann hierarchy.[^note-2] The addition of large set axioms to intuitionistic ZF was first proposed by Friedman and Scedrov (Friedman and Scedrov 1984)[^friedman-1984]. They introduced inaccessible sets, Mahlo sets, and elementary embedding to express supercompactness, hugeness, and Reinhardt’s axiom over IZF. One of their aim was to shed light on the corresponding classical notions; another was to study the impact of these principles on metatheoretical properties of the original set theories. Friedman and Scedrov have shown, for example, that the addition of large set axioms does not compromise the validity of the disjunction and numerical existence properties for IZF.

In the context of constructive set theory, large sets have been introduced by Aczel in the form of so-called *regular sets* to express inductive definitions of sets (Aczel 1986)[^aczel-1986]. Rathjen and collaborators have determined the proof-theoretic strength of a number of extensions of CZF by large set axioms, expressing largeness notions corresponding to inaccessibility, Mahloness and weak compactness (see, e.g., Rathjen et al. 1998; Rathjen 1998; Rathjen 1999, Rathjen 2003a)[^rathjen-1998][^rathjen-1999][^rathjen-2003a][^rathjen-1998-2]. The study of large sets in the context of constructive set theories has been further expanded by Ziegler and Matthews in their Ph.D. theses (Ziegler 2014a, Matthews 2021)[^matthews-2021][^ziegler-2014a]. Ziegler 2014a is an investigation into large sets and large set axioms in the context of CZF. Among other things, Ziegler uses a new modified cumulative hierarchy to characterise large sets’ arrangement in the set theoretic universe. He develops a constructive theory of clubs, presents a characterisation theorem for Mahlo sets (connecting classical and constructive approaches to Mahloness) and presents a characterisation theorem for 2-strong sets. He then studies elementary embeddings of the set theoretic universe into a transitive class model of CZF. Matthews (2021) studies elementary embeddings in the context of both classical and intuitionistic theories without powerset. Jeon and Matthews ms. [Other Internet Resources] further this study by considering large set axioms on the basis of constructive set theories, including CZF. While the proof-theoretic strength of the extensions of CZF by small large sets is weaker than that of Second-order Peano Arithmetic, they show that the proof-theoretic strength of large large sets (large set notions defined in terms of elementary embeddings) vastly exceeds that of ZFC.

Another notion that has played a crucial role in classical set theory, also in relation with large cardinal assumptions, is that of the constructible hierarchy, L. Lubarsky (1993) first studied the constructible hierarchy in the context of IZF. Matthews and Rathjen (2024) further study the constructible hierarchy to clarify its structure and role within constructive set theories. For example, they investigate whether L can be thought of as an inner model in the usual sense and show that the constructive case is importantly different from the classical one. For example, they prove that it is possible for there to be an ordinal which is not in the constructible universe.

From a foundational perspective, an objection could be raised to extensions of constructive set theory by large set axioms. In classical set theory, large cardinals can be seen as an incarnation of higher infinity. How do we justify these principles constructively? It may be thought that the constructive justification of these notions should rely again on the type theoretic interpretation. In the case of set theories extended with so-called “small” large set principles, there are, in fact, corresponding extensions of constructive type theory by universes and so-called $W$-types. From this perspective, the justification of extensions by large sets is thus bound up with the question of the limits of Martin-Löf type theory (Rathjen 2005)[^rathjen-2005]. We also note that the addition of inacessible set axioms to a weak subsystem of CZF (with no set induction) produces a theory of strength $\Gamma_0$, the ordinal singled out by Feferman and Schütte as the limit of predicativity given the natural numbers (Crosilla and Rathjen 2001; see also section 1.3)[^crosilla-2001]. This is witness to the fact that by working in a constructive, predicative context, we can tame important traditionally strong set-theoretic notions. For stronger large set assumptions, other justifications would seem to be required. See, e.g., Ziegler 2014 for discussion.

Crosilla and Rathjen’s set theory with inaccessible sets (but no set induction) is proof theoretically rather weak, but mathematically quite expressive. For example, it has been used to verify that the addition of Voevodsky’s Univalence Axiom to Martin-Löf type theory does not engender impredicativity (Rathjen 2017)[^rathjen-2017]. The axiom of Univalence was introduced by Voevodsky as part of his Univalent Foundations programme (Voevodsky 2015)[^voevodsky-2015]. (For Univalent Foundations, see the entries on type theory and on intuitionistic type theory). Voevodsky gave a model of constructive type theory with the Univalence Axiom which is based on Kan simplicial sets (see Kapulkin & Lumsdaine 2012). The simplicial model of constructive type theory with univalence developed in the above article is carried out within an extension of ZFC with inaccessible cardinals. This prompted the question whether one could give a more constructive model of this type theory, and, in particular, whether the type theory is predicative. Bezem, Coquand and Huber (2014) have proposed a model of this type theory in cubical sets which is computational and “can be expressed in a constructive metalogic”. Rathjen (2017) has verified that this new model can be codified in a suitable extension of CZF by inaccessible sets which is much weaker than classical set theory with inaccessible cardinals. In fact, it turns out that if we take as starting point a relatively weak type theory, i.e., one without W-types, and extend it by the Univalence Axiom, the resulting theory has proof theoretic strength $\Gamma_0$ (Rathjen 2017)[^rathjen-2017]. To show this, one proves that the cubical model by Bezem, Coquand and Huber can be carried out in an extension of the system introduced in Crosilla and Rathjen (2001) by (bounded) Relativized Dependent Choice. It follows from (Crosilla and Rathjen 2001)[^crosilla-2001] and (Rathjen 2003)[^rathjen-2003] that the latter has proof theoretic ordinal $\Gamma_0$.

### 5.3 Metamathematical properties of constructive and intuitionistic ZF and semantic techniques

A variety of interpretations for intuitionistic logic have been extended to intuitionistic and constructive set theories, such as realisability, Kripke models and Heyting-valued semantics. All these techniques have been applied to obtain metamathematical results about the set theories.

#### 5.3.1 Disjunction and existence properties of constructive and intuitionistic ZF

Some intuitionistic set theories satisfy certain “hallmark” metamathematical properties, such as the *disjunction* and the *existence properties*. They can also be shown to be consistent with the addition of principles which go beyond what we most typically consider constructive. Among these are, for example, *Church Thesis* and *Markov’s principle*. For a description of these principles in the context of intuitionistic logic, the reader may wish to consult sections 4.2 and 5.2 of the entry on intuitionistic logic or Troelstra and van Dalen’s book *Constructivism in Mathematics* (Troelstra and van Dalen 1988)[^troelstra-1988].

Here we recall the disjunction and existence properties, formulated for a set theory $T$. The informal motivation for the disjunction and the existence properties is based on our understanding of the constructive proofs of disjunctive and existential statements (respectively). In fact, it seems reasonable to expect that if we constructively prove a disjunction $\phi \vee \psi$, then we should also be able to prove $\phi$ or prove $\psi$. Similarly, if we prove an existential statement, then we should be able to prove that a witness to that statement is definable within our theory.

Although such properties seem quite natural and are fairly easy to establish for arithmetical theories, they turn out to pose considerable technical challenges in the case of set theories, due to their transfinite hierarchies of sets and the extensionality axiom. In fact, prominent constructive and intuitionistic set theories turn out not to possess the existence property, as discussed in the next section.

Let $T$ be a theory whose language, $L(T)$, encompasses the language of set theory. Moreover, for simplicity, we shall assume that $L(T)$ has a constant $\omega$ denoting the set of von Neumann natural numbers and for each $n$ a constant $c_n$ denoting the $n$-th element of $\omega$.

A theory $T$ has the **disjunction property** (DP) if whenever $T$ proves $(\phi \vee \psi)$ for sentences $\phi$ and $\psi$ of $L(T)$, then $T$ proves $\phi$ or $T$ proves $\psi$.

The **existence property** has two distinct versions in the context of set theory: the *numerical existence property* (NEP) and the **existence property** (EP). Let $\theta(x)$ be a formula with at most $x$ free. We say that:

**(1)**

$T$ has the NEP if whenever $T$ proves $\exists x \in \omega \theta(x)$, then, for some natural number $n$, $T$ proves $\theta(c_n)$.

**(2)**

$T$ has the EP if whenever $T$ proves $\exists x\theta$(x), then there is a formula $\phi(x)$ with exactly $x$ free, so that $T$ proves $\exists !x(\phi(x) \wedge \theta(x))$.

As realisability techniques have proved crucial in investigations on the existence and disjunction properties for constructive and intuitionistic set theories, we discuss the outcomes of these studies in the next section.

#### 5.3.2 Realisability

Realisability has been one of the first and principal tools in the research surrounding set theories based on intuitionistic logic, starting from the early contributions by Friedman and Myhill (Friedman 1973, Myhill 1973)[^friedman-1973][^myhill-1973]. Realisability semantics for intuitionistic arithmetic were first proposed by Kleene (Kleene 1945)[^kleene-1945] and extended to higher order Heyting arithmetic by Kreisel and Troelstra (Kreisel and Troelstra 1970)[^kreisel-1970]. For the definition of realisability for arithmetic see section 5.2 of the entry on intuitionistic logic. A realisability similar to Kreisel and Troelstra was applied to systems of higher order arithmetic by Friedman (Friedman 1973)[^friedman-1973]. Myhill introduced a variant of this realisability which resembles Kleene’s slash (Myhill 1973; Kleene 1962, 1963)[^kleene-1962][^kleene-1963][^myhill-1973]. He thus proved that a version of IZF with replacement in place of collection (called IZF$_{Rep})$ has the DP, the NEP and the EP. These results were further extended in (Myhill 1975; Friedman and Scedrov 1983)[^friedman-1983][^myhill-1975]. While Friedman and Myhill gave realisability models for extensional set theories, Beeson developed a notion of realisability for non-extensional set theories. He then studied metatheoretical properties of the extensional set theories via an interpretation in their non-extensional counterparts. He thus proved that IZF (with collection) has the DP and NEP (Beeson 1985)[^beeson-1985]. Subsequently McCarty introduced realisability for IZF directly for extensional set theory (McCarty 1984; 1986)[^mccarty-1984]. Realisability semantics for variants of CZF have been considered, for example, in (Crosilla and Rathjen 2001; Rathjen 2006a)[^crosilla-2001][^rathjen-2006a]. The realisability in the latter article is inspired by McCarty’s and has the important feature that, as McCarty’s for IZF, it is a self-validating semantics for CZF (that is, this notion of realisability can be formalised in CZF and each theorem of CZF is realised provably in CZF). Rathjen has made use of this notion of realisability to show that CZF (and a number of extensions of it) have the DP and the NEP (Rathjen 2005b)[^rathjen-2005b].

Another kind of realisability that has proved very useful is Lifschitz realisability. Lifschitz (1979) introduced a modification of Kleene’s realizability for Heyting arithmetic which has the peculiarity of validating a weak form of Church’s Thesis (CT) with a uniqueness condition, but not CT itself. Lifschitz realisability was extended to second order arithmetic by van Oosten (1990). It was subsequently extended to full IZF by Cheng and Rathjen, who employed it to obtain a number of independence results, as well as validating the so called Lesser Limited Principle of Omniscience (LLPO) (for LLPO see the entry on constructive mathematics).

The question of which set theories satisfy the existence property turned out to be particularly difficult to solve. (Friedman and Scedrov 1985)[^friedman-1985][^scedrov-1985] used Kripke models to show that IZF (that is, the system with collection) does not have the EP, while as mentioned above, the system IZF$_{Rep}$ (which has replacement in place of collection) does have the EP. This prompted Beeson to pose the question [Beeson 1985, IX][^beeson-1985]:

> Does any reasonable set theory with collection have the existence property?

A first answer to Beeson’s question came with (Rathjen 2012)[^rathjen-2012], where the author introduced the notion of *weak* existence property: the focus here is finding a provably definable *set* of witnesses for every existential theorem. He then introduced a form of realizability based on general set recursive functions, where a realizer for an existential statement provides a *set* of witnesses for the existential quantifier, rather than a single witness. Rathjen combined this notion of realizability with truth to yield that a number of theories with collection do enjoy the weak existence property (while IZF does not). Among them, in particular, the theory CZF without subset collection plus Myhill’s exponentiation axiom, CZF$_{Exp}$. In fact, Rathjen claimed that by combining these results with further work he had carried out, he could show that CZF$_{Exp}$ (and a number of other theories) do have the existence property. A striking observation is that these theories are formulated with collection; consequently the failure of the existence property in the case of IZF can not be attributed only to collection, but to the interplay between this scheme and unrestricted separation.

As to the prominent question of whether CZF itself has the existence property, this has been solved in the negative by Swan (2014). There the author made use of three well devised realisability models and embeddings between them, to show that even the weak existence property fails for CZF. In so doing he also showed that CZF’s subset collection schema is the culprit. As clearly highlighted in (Swan 2014)[^swan-2014] the fact that CZF does not have EP does not indicate some weakness in CZF as a constructive theory. Even if Swan proved essentially that CZF asserts the existence of mathematical objects that it does not know how to construct, still CZF does have natural interpretations in which these objects can be constructed, like, for example, Aczel’s interpretation into type theory (Aczel 1978)[^aczel-1978].

For a survey of results in intuitionistic set theory see (Beeson 1985, Chapter IX)[^beeson-1985]. For the corresponding developments in CZF, see (Rathjen 2005b, 2006, 2012)[^rathjen-2005b][^rathjen-2006][^rathjen-2012] and (Swan 2014)[^swan-2014].

#### 5.3.3 Kripke models and Heyting-valued semantics

Kripke models for intuitionistic set theories have been used in Friedman and Scedrov 1985 to show that IZF does not have the EP (and combining this with the results in Myhill 1973 we have that IZF$_{Rep}$ does not prove IZF)[^myhill-1973]. Kripke models have more recently been applied to clarify the relation between the constructive substitutes of the power set axiom: Myhill’s exponentiation axiom and Aczel’s subset collection schema. It is clear that the power set axiom implies both of these principles, and that subset collection implies exponentiation. On the other hand, each of the latter two principles does not imply power set, as the theory CZF with power set in place of subset collection is much stronger than CZF and CZF$_{Exp}$ (Rathjen 2012b)[^rathjen-2012b]. In fact, CZF and CZF$_{Exp}$ have the same proof theoretic strength (Griffor and Rathjen 1994)[^griffor-1994]; therefore to investigate the relation between subset collection and exponentiation in constructive set theory one needed to develop tools other then proof theoretic methods. Lubarsky (2005) used Kripke models to show that Myhill’s exponentiation axiom does not imply Aczel’s subset collection (on the basis of CZF minus subset collection plus full separtion). In Lubarsky and Rathjen 2007, the authors applied the technique of Kripke models to show that also the consequences of the theories CZF and CZF$_{Exp}$ are different. Aczel and Rathjen (2001) had shown that the class of Dedekind real numbers forms a set in CZF, by using subset collection. Lubarsky and Rathjen (2007) showed that CZF$_{Exp}$ does not suffice to prove the same statement.

Kripke models have been applied also to separate varieties of the Fan theorem in Diener and Lubarsky 2013. Lubarsky (2023) presents an overview of model-theoretic techniques, introducing both Heyting-valued and Kripke models, and constructions that combine both of those ideas. Kripke models for constructive set theory are employed in Iemhoff 2010, Iemhoff and Passmann 2021, and Iemhoff and Passmann 2023. Iemhoff (2010) constructs Kripke models for subtheories of constructive set theory by using constructions from classical model theory such as constructible sets and generic extensions. She proves that under the main construction all axioms except the collection axioms can be shown to hold in the constructed Kripke model. Iemhoff and Passmann (2021) investigate the logical structure of an important subsystem of CZF, intuitionistic Kripke-Platek set theory, IKP. They show that the first-order logic of IKP is intuitionistic first-order logic.

Heyting-valued semantics for intuitionistic set theories were obtained by Grayson (1979) as a counterpart for Boolean models for classical set theory. They have been generalized especially via categorical semantics (for an introduction see MacLane and Moerdijk 1992)[^maclane-1992]. Heyting-valued semantics have found application to independence results in (Scedrov 1981; 1982)[^scedrov-1981]. A constructive treatment has been given in Gambino 2006. (See also Lubarsky 2009.)[^lubarsky-2009] See Ziegler 2012 for a generalization of realisability and Heyting models for constructive set theory.

#### 5.3.4 Categorical models of constructive and intuitionistic set theory

Categorical models of constructive and intuitionistic set theories have flourished over the years. The notions of topos and sheaf play an essential role here (see, e.g., Fourman 1980 and Fourman and Scott 1980)[^fourman-1980][^fourman-1980-2]. For an overview of the main concepts, see the entry on category theory and the references provided there (see in particular the supplement Programmatic Reading Guide). For developments that relate more specifically to constructive set theories, see *e.g.* (Simpson 2005)[^simpson-2005] and (Awodey 2008)[^awodey-2008], as well as the web page: [algebraic set theory](http://www.phil.cmu.edu/projects/ast/).

### 5.4 Variants of Constructive and Intuitionistic Set Theories: Set Theories with Urelements and Non-extensional Set Theories

Sometimes systems of intuitionistic and constructive set theory have been presented with the natural numbers as a separate sort of urelements, that is, primitive objects with no elements (Friedman 1977; Myhill 1975; Beeson 1985)[^beeson-1985][^friedman-1977][^myhill-1975]. Constructively, this is a natural choice which is in agreement with ideas expressed, for example, by Bishop (1967), among others. In Bishop’s monograph the natural numbers are taken as a fundamental concept on which all the other mathematical concepts are based. From a technical point of view, if the natural numbers are taken as primitive and distinct from their set-theoretic representations, the axiom of infinity then takes the form: “there is a set of natural numbers (as urelements)”. A more general form of urelements in constructive set theories have been considered in Cantini and Crosilla 2008. Here a variant of constructive set theory is proposed which combines an intensional and partial notion of operation with CZF’s extensional notion of set (see also Cantini and Crosilla 2010)[^cantini-2010].

The axiom of extensionality is a common feature of all the systems discussed so far. However, in a context in which the computational content of a statement is considered to be crucial, an intensional theory might be more appropriate. For example, constructive type theory and explicit mathematics both encapsulate some form of intensionality. Intuitionistic set theories without extensionality have been considered in the literature (Friedman 1973a, Beeson 1985)[^beeson-1985][^friedman-1973a][^friedman-1985]. Their motivation, however, has been not computational but technical in nature, due to the difficulties that extensionality brings about when studying metamathematical properties of intuitionistic set theories.

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=set-theory-constructive). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/set-theory-constructive/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=set-theory-constructive&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/set-theory-constructive/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

- Awodey, S., [Algebraic Set theory](http://www.phil.cmu.edu/projects/ast/), Carnegie Mellon.
- Jeon, H., Matthews, R., m.s., “[Very large set axioms over constructive set theories](https://arxiv.org/abs/2204.05831)”, manuscript at arxiv.org.

[Please contact the author with further suggestions.]

## Related Entries

Brouwer, Luitzen Egbertus Jan | category theory | choice, axiom of | logic, history of: intuitionistic logic | logic: intuitionistic | mathematics, philosophy of | mathematics, philosophy of: intuitionism | mathematics: constructive | paradoxes: and contemporary logic | proof theory | semantics: proof-theoretic | set theory | set theory: alternative axiomatic theories | set theory: early development | set theory: non-wellfounded | type theory | type theory: intuitionistic

### Acknowledgments

I thank Andrea Cantini, Michael Rathjen and Peter Schuster for valuable comments on an earlier version of this entry. My thanks also to the referee for helpful suggestions and to the editors for their useful comments and their kind assistance with the html files.

## Notes（原文脚注）

[^note-1]: Note that one could also choose to leave out foundation (and set-induction) altogether. One may then wish to add an axiom, called antifoundation, which allows for the formation of non-well-founded sets, also called hypersets (see Aczel 1988 or Barwise and Moss 1996)[^aczel-1988][^barwise-1996]. In fact, a constructive treatment of non-well-founded sets can be given which mirrors the classical one (see for example Rathjen 2004)[^rathjen-2004]. Further, by using a construction by Hällnas and Lindström of non-well-founded sets as limits of finite approximations (Lindström 1989)[^lindström-1989], one can see that in constructive contexts the antifoundation axiom comes as proof-theoretically “inexpensive” if compared with set induction (Rathjen 2003)[^rathjen-2003].

[^note-2]: Inaccessible sets in CZF corresponds in ZFC to $V_k$ for $k$ a strongly inaccessible cardinal, where $V_k$ denotes the $k$-th level of the von Neumann hierarchy (Crosilla and Rathjen 2001)[^crosilla-2001].

[^aczel-1978]: Aczel, P., 1978, “The Type Theoretic Interpretation of Constructive Set Theory”, in *Logic Colloquium ‘77*, A. MacIntyre, L. Pacholski, J. Paris (eds.), Amsterdam and New York: North-Holland, pp. 55–66.

[^aczel-1982]: –––, 1982, “The type theoretic interpretation of constructive set theory: choice principles”, in *The L.E.J. Brouwer Centenary Symposium*, A. S. Troelstra and D. van Dalen (eds.), Amsterdam and New York: North-Holland, pp. 1–40.

[^aczel-1986]: –––, 1986, “The type theoretic interpretation of constructive set theory: inductive definitions”, in *Logic, Methodology, and Philosophy of Science VII*, R.B. Marcus, G.J. Dorn, and G.J.W. Dorn (eds.), Amsterdam and New York: North-Holland, pp. 17–49.

[^aczel-1988]: –––, 1988, *Non-wellfounded Sets* (CSLI Lecture Notes 14), Stanford: CSLI.

[^aczel-2001]: Aczel, P., and M. Rathjen, 2001, “Notes on Constructive Set Theory”, Report No. 40, 2000/2001, Djursholm: Institut Mittag-Leffler, [[available online](http://www.mittag-leffler.se/sites/default/files/IML-0001-40.pdf)]

[^aczel-2002]: Aczel, P., and N. Gambino, 2002, “Collection principles in dependent type theory”, in *Types for Proofs and Programs* (Lecture Notes in Computer Science 2277), P. Callaghan, Z. Luo, J. McKinna, and R. Pollack (eds.), Berlin: Springer, pp. 1–23.

[^awodey-2008]: Awodey, S., 2008, “A Brief Introduction to Algebraic Set Theory”, *The Bulletin of Symbolic*, 14 (3): 281–298.

[^barwise-1996]: Barwise, J., and L. Moss, 1996, *Vicious Circles* (CSLI Lecture Notes 60), Stanford: CSLI.

[^beeson-1985]: Beeson, M., 1985, *Foundations of Constructive Mathematics*, Berlin: Springer.

[^bezem-2014]: Bezem, M., C. Thierry, and S. Huber, 2014, “A model of type theory in cubical sets”, in 19th International Conference on Types for Proofs and Programs (TYPES 2013), Matthes, R. and Schubert, A. (eds.), Dagstuhl: Schloss Dagstuhl–Leibniz-Zentrum fuer Informatik, pp. 107–128.

[^bishop-1967]: Bishop, E., 1967, *Foundations of Constructive Analysis*, New York: McGraw-Hill.

[^bishop-1970]: –––, 1970, “Mathematics as a numerical language”, in *Intuitionism and Proof Theory*, A. Kino, J. Myhill, and R. E. Vesley (eds.), Amsterdam: North-Holland, pp. 53–71.

[^bishop-1985]: Bishop, E., and D. Bridges, 1985, *Constructive Analysis*, Berlin and Heidelberg: Springer.

[^bridges-1987]: Bridges, D., and F. Richman, 1987, *Varieties of Constructive Mathematics*, Cambridge: Cambridge University Press.

[^buchholz-1981]: Buchholz, W., S. Feferman, W. Pohlers, and W. Sieg, 1981, *Iterated Inductive Definitions and Subsystems of Analysis*, Berlin: Springer.

[^cantini-2008]: Cantini, A., and L. Crosilla, 2008, “Constructive set theory with operations”, in A. Andretta, K. Kearnes, D. Zambella (eds.), *Logic Colloquium 2004* (Lecture Notes in Logic 29), Cambridge: Cambridge University Press, pp. 47–83.

[^cantini-2010]: –––, 2010, “Explicit operational set theory”, in R. Schindler (ed.), *Ways of Proof Theory*, Frankfurt: Ontos, pp. 199–240.

[^chen-2012]: Chen, R.-M. and M. Rathjen, 2012, “Lifschitz Realizability for Intuitionistic Zermelo-Fraenkel Set Theory”, *Archive for Mathematical Logic*, 51: 789–818.

[^crosilla-2017]: Crosilla, L., 2017, “Predicativity and Feferman”, in G. Jäger and W. Sieg (eds.), *Feferman on Foundations* (Outstanding Contributions to Logic: Volume 13), Cham: Springer, pp. 423–447.

[^crosilla-2022]: –––, 2022, “Predicativity and Constructive Mathematics”, in Oliveri, G., Ternullo, C. and Boscolo, S. (eds.), *Objects, Structures, and Logics* (Boston Studies in the Philosophy and History of Science: Volume 339), Cham: Springer.

[^crosilla-2001]: Crosilla, L., and M. Rathjen, 2001, “Inaccessible set axioms may have little consistency strength”, *Annals of Pure and Applied Logic*, 115: 33–70.

[^diaconescu-1975]: Diaconescu, R., 1975, “Axiom of choice and complementation”, *Proceedings of the American Mathematical Society*, 51: 176–178.

[^diener-2013]: Diener, H., and R. Lubarsky, 2013, “Separating the Fan Theorem and Its Weakenings”, in S. N. Artemov and A. Nerode (eds.), *Proceedings of LFCS ‘13* (Lecture Notes in Computer Science 7734), Dordrecht: Springer, pp. 280–295.

[^dummett-2000]: Dummett, M., 2000, *Elements of Intuitionism*, second edition, (Oxford Logic Guides 39), New York: Oxford University Press.

[^feferman-1964]: Feferman, S., 1964, “Systems of predicative analysis”, *Journal of Symbolic Logic*, 29: 1–30.

[^feferman-1975]: –––, 1975, “A language and axioms for explicit mathematics”, in *Algebra and Logic* (Lecture Notes in Mathematics 450), J. Crossley (ed.), Berlin: Springer, pp. 87–139.

[^feferman-1988]: –––, 1988, “Weyl vindicated: Das Kontinuum seventy years later”, in *Temi e prospettive della logica e della scienza contemporanee*, C. Cellucci and G. Sambin (eds), pp. 59–93.

[^feferman-1993]: –––, 1993, “What rests on what? The proof-theoretic analysis of mathematics”, in *Philosophy of Mathematics*, Part I, Proceedings of the 15th International Wittgenstein Symposium. Vienna: Verlag Hölder-Pichler-Tempsky.

[^feferman-2005]: –––, 2005, “Predicativity”, in *Handbook of the Philosophy of Mathematics and Logic*, S. Shapiro (ed.), Oxford: Oxford University Press.

[^fletcher-2007]: Fletcher, P., 2007, “Infinity”, in *Handbook of the Philosophy of Logic*, D. Jacquette, (ed.), Amsterdam: Elsevier, pp. 523–585.

[^fourman-1980]: Fourman, M.P., 1980, “Sheaf models for set theory”, *Journal of Pure Applied Algebra*, 19: 91–101.

[^fourman-1980-2]: Fourman, M.P., and D.S. Scott, 1980, “Sheaves and logic”, in *Applications of Sheaves* (Lecture Notes in Mathematics 753), M.P. Fourman, C.J. Mulvey and D.S. Scott (eds.), Berlin: Springer, pp. 302–401.

[^friedman-1973]: Friedman, H., 1973, “Some applications of Kleene’s methods for intuitionistic systems”, in *Proceedings of the 1971 Cambridge Summer School in Mathematical Logic* (Lecture Notes in Mathematics 337), A.R.D. Mathias and H. Rogers (eds.), Berlin: Springer, pp. 113–170.

[^friedman-1973a]: –––, 1973a, “The consistency of classical set theory relative to a set theory with intuitionistic logic”, *Journal of Symbolic Logic*, 38: 315–319.

[^friedman-1977]: –––, 1977, “Set-theoretical foundations for constructive analysis”, *Annals of Mathematics*, 105: 1–28.

[^friedman-1983]: Friedman, H., and A. Scedrov, 1983, “Set existence property for intuitionistic theories with dependent choice”, *Annals of Pure and Applied Logic*, 25: 129–140.

[^friedman-1984]: –––, 1984, “Large sets in intuitionistic set theory”, *Annals of Pure and Applied Logic*, 27: 1–24.

[^friedman-1985]: –––, 1985, “The lack of definable witnesses and provably recursive functions in intuitionistic set theory”, *Advances in Mathematics*, 57: 1–13.

[^gambino-2006]: Gambino, N., 2006, “Heyting-valued interpretations for constructive set theory”, *Annals of Pure and Applied Logic*, 137: 164–188.

[^gödel-1944]: Gödel, 1944, “Russell’s mathematical logic”, *The Philosophy of Bertrand Russell* (Library of Living Philosophers), P. Schilpp (ed.), New York: Tudor, 1951, pp. 123–153.

[^goodman-1972]: Goodman, N.D., and J. Myhill, 1972, “The formalization of Bishop’s constructive mathematics”, in *Toposes, Algebraic Geometry and Logic* (Lecture Notes in Mathematics 274), F.W. Lawvere (ed.), Berlin: Springer, pp. 83–96.

[^goodman-1978]: –––, 1978, “Choice implies excluded middle”, *Zeitschrift für mathematische Logik und Grundlagen der Mathematik*, 24(5): 461.

[^grayson-1979]: Grayson, R.J., 1979, “Heyting-valued models for intuitionistic set theory”, in *Applications of Sheaves* (Lecture Notes in Mathematics 753), M.P. Fourman, C.J. Mulvey, and D.S. Scott (eds.), Berlin: Springer, pp. 402–414.

[^griffor-1994]: Griffor, E., and M. Rathjen, 1994, “The strength of some Martin-Löf type theories”, *Archive Mathematical Logic*, 33: 347–385.

[^heijenoort-1967]: van Heijenoort, J., 1967, *From Frege to Gödel. A Source Book in Mathematical Logic 1879–1931*, Cambridge: Harvard Univ. Press.

[^ihemoff-2010]: Ihemoff, R., 2010, “Kripke models for subtheories of CZF”, *Archive for Mathematical Logic*, 49: 147–167.

[^iemhoff-2021]: Iemhoff, R., and R. Passmann, 2021, “Logics of intuitionistic Kripke-Platek set theory”, *Annals of Pure and Applied Logic*, 172: 103014.

[^iemhoff-2023]: –––, 2023, “Logics and admissible rules of constructive set theories”, *Philosophical Transactions of the Royal Society A*, 381 (2248). doi:10.1098/rsta.2022.0018

[^kapulkin-2021]: Kapulkin, C. and P.L. Lumsdaine, 2021, “The simplicial model of univalent foundations (after Voevodsky)”, *Journal of the European Mathematical Society*, 23(6): 2071–2126

[^kleene-1945]: Kleene, S.C., 1945, “On the interpretation of intuitionistic number theory”, *Journal of Symbolic Logic*, 10: 109–124.

[^kleene-1962]: –––, 1962, “Disjunction and existence under implication in elementary intuitionistic formalisms”, *Journal of Symbolic Logic*, 27: 11–18.

[^kleene-1963]: –––, 1963, “An addendum”, *Journal of Symbolic Logic*, 28: 154–156.

[^kreisel-1958]: Kreisel, G., 1958, “Ordinal logics and the characterization of informal concepts of proof”, *Proceedings of the International Congress of Mathematicians* (14–21 August 1958), Paris: Gauthier-Villars, pp. 289–299.

[^kreisel-1970]: Kreisel, G., and A. S. Troelstra, 1970, “Formal systems for some branches of intuitionistic analysis”, *Annals of Mathematical Logic*, 1: 229–387.

[^lifschitz-1979]: Lifschitz, V., 1979, “CT$_0$ is stronger than CT$_0$!”, *Proceedings of the American Mathematical Society*, 73(1): 101–106.

[^lindström-1989]: Lindström, I., 1989, “A construction of non-well-founded sets within Martin-Löf type theory”, *Journal of Symbolic Logic*, 54: 57–64.

[^lipton-1995]: Lipton, J., 1995, “Realizability, set theory and term extraction”, in *The Curry-Howard isomorphism* (Cahiers du Centre de Logique de l’Universite Catholique de Louvain 8), Louvain-la-Neuve: Academia, pp. 257–364.

[^lorenzen-1959]: Lorenzen, P., and J. Myhill, 1959, “Constructive definition of certain analytic sets of numbers”, *Journal of Symbolic Logic*, 24: 37–49.

[^lubarsky-1993]: Lubarsky, R., 1993, “Intuitionistic L”, in J.N. Crossley, J.B. Remmel, R.A. Shore, and M.E. Sweedler (eds.), *Logical Methods* (Progress in Computer Science and Applied Logic: Volume 12), Birkhäuser, Boston, MA, 555–571.

[^lubarsky-2005]: –––, 2005, “Independence results around constructive ZF”, *Annals of Pure and Applied Logic*, *132*: 209–225.

[^lubarsky-2006]: –––, 2006, “CZF and second order arithmetic”, *Annals of Pure and Applied Logic*, *141*: 29–34.

[^lubarsky-2009]: –––, 2009, “Topological Forcing Semantics with Settling”, in S. N. Artemov and A. Nerode (eds.), *Proceedings of LFCS ‘09* (Lecture Notes in Computer Science 5407), Dordrecht: Springer, pp. 309–322.

[^lubarsky-2023]: –––, 2023, “Inner and Outer Models for Constructive Set Theories”, in D. Bridges, H. Ishihara, M. Rathjen, and H. Schwichtenberg (eds.), *The Handbook of Constructive Mathematics*, Cambridge: Cambridge University Press, pp. 584–635.

[^lubarsky-2007]: Lubarsky, R., and M. Rathjen, 2007, “On the Constructive Dedekind Reals”, in in S. N. Artemov and A. Nerode (eds.), *Proceedings of LFCS 2007* (Lecture Notes in Computer Science 4514), Dordrecht: Springer, pp. 349–362.

[^maclane-1992]: MacLane, S., and I. Moerdijk, 1992, “Sheaves in Geometry and Logic”, New York: Springer.

[^maietti-2009]: Maietti, M.E., 2009, “A minimalist two-level foundation for constructive mathematics “, *Annals of Pure and Applied Logic*, 160(3): 319–354.

[^maietti-2005]: Maietti, M.E., and G. Sambin, 2005, “Toward a Minimalist Foundation for Constructive Mathematics”, in *From Sets and Types to Topology and Analysis: Towards Practicable Foundations for Constructive Mathematics* (Oxford Logic Guides 48), L. Crosilla, and P. Schuster (eds.), Oxford: Oxford University Press.

[^martin-löf-1975]: Martin-Löf, P., 1975, “An intuitionistic theory of types: predicative part”, in H.E. Rose and J. Sheperdson (eds.), *Logic Colloquium ‘73*, Amsterdam: North-Holland, pp. 73–118.

[^martin-löf-1984]: –––, 1984, “Intuitionistic Type Theory”, Naples: Bibliopolis.

[^matthews-2021]: Matthews, R. M. A., 2021, “Large Cardinals in Weakened Axiomatic Theories”, Ph.D. Thesis, University of Leeds, [[Matthews 2021 available online](http://etheses.whiterose.ac.uk/29589/)].

[^matthews-2024]: Matthews, R., and M. Rathjen, 2024, “Constructing the Constructible Universe Constructively”, *Annals of Pure and Applied Logic*, 175(3). doi:10.1016/j.apal.2023.103392

[^mccarty-1984]: McCarty, D.C., 1984, “Realisability and Recursive Mathematics”, D.Phil. Dissertation, *Philosophy*, Oxford University.

[^mccarty-1986]: –––, 1986, “Realizability and recursive set theory”, *Annals of Pure and Applied Logic*, 32: 153–183.

[^myhill-1973]: Myhill, J., 1973, “Some properties of Intuitionistic Zermelo-Fraenkel set theory”, in *Proceedings of the 1971 Cambridge Summer School in Mathematical Logic* (Lecture Notes in Mathematics 337), A.R.D. Mathias, and H. Rogers(eds.), Berlin: Springer, pp. 206–231.

[^myhill-1975]: –––, 1975, “Constructive set theory”, *Journal of Symbolic Logic*, 40: 347–382.

[^oosten-1990]: van Oosten, J., 1990, “Lifschitz’s Realizability”, *The Journal of Symbolic Logic*, 55: 805–821.

[^powell-1975]: Powell, W., 1975, “Extending Gödel’s negative interpretation to ZF”, *Journal of Symbolic Logic*, 40: 221–229.

[^rathjen-1998]: Rathjen, M., 1998, “The Higher Infinite in Proof Theory”, in J. Makowsky & E. Ravve (eds.), *Logic Colloquium ’95: Proceedings of the Annual European Summer Meeting of the Association of Symbolic Logic*, in Haifa, Israel, August 1995, Cambridge: Cambridge University Press, pp. 275–304.

[^rathjen-1999]: –––, 1999, “The realm of ordinal analysis”, in *Sets and Proofs* (London Mathematical Society Lecture Notes 258), Cambridge: Cambridge University Press, pp. 219–279.

[^rathjen-2003]: –––, 2003, “The anti-foundation axiom in constructive set theories”, in *Games, logic, and constructive sets* (CSLI Lecture Notes 161), Stanford: CSLI Publication, pp. 87–108.

[^rathjen-2003a]: –––, 2003a, “Realizing Mahlo set theory in type theory”, *Archive for Mathematical Logic*, 42: 89–101.

[^rathjen-2004]: –––, 2004, “Predicativity, circularity, and anti-foundation”, in *One hundred years of Russell’s paradox* (Logic and its Applications 6), G. Link (ed.), Berlin: de Gruyter, pp. 191–219.

[^rathjen-2005]: –––, 2005, “Replacement versus Collection and related topics in constructive Zermelo-Fraenkel Set Theory”, *Annals of Pure and Applied Logic*, 136: 156–174.

[^rathjen-2005a]: –––, 2005a, “The constructive Hilbert program and the limits of Martin-Löf type theory”, *Synthese*, 147: 81–120.

[^rathjen-2005b]: –––, 2005b, “The disjunction and related properties for constructive Zermelo-Fraenkel set theory”, *Journal of Symbolic Logic*, 70(4): 1232–1254.

[^rathjen-2006]: –––, 2006, “Choice principles in constructive and classical set theories”, *Logic Colloquium ‘02* (Lecture Notes in Logic 27), Z. Chatzidakis, P. Koepke, and W. Pohlers (eds.), Wellesley, Massachusetts: A.K. Peters, 299–326.

[^rathjen-2006a]: –––, 2006a, “Realizability for constructive Zermelo-Fraenkel set theory”, in *Logic Colloquium ‘03* (Lecture Notes in Logic 24), V. Stoltenberg-Hansen and J. Väänänen (eds.), Wellesley, Massachusets: A.K. Peters, pp. 282–314.

[^rathjen-2006b]: –––, 2006b, “Theories and ordinals in proof theory”, *Synthese*, 148(3): 719–743.

[^rathjen-2008]: –––, 2008, “The natural numbers in constructive set theory”, *Mathematical Logic Quarterly*, 54: 287–312.

[^rathjen-2012]: –––, 2012, “From the weak to the strong existence property”, *Annals of Pure and Applied Logic*, 163: 1400–1418.

[^rathjen-2012b]: –––, 2012b, “Constructive Zermelo-Fraenkel Set Theory, Power Set, and the Calculus of Constructions”, in *Epistemology versus Ontology: Essays on the Philosophy and Foundations of Mathematics in Honour of Per Martin-Löf*, (Logic, Epistemology and the Unity of Science Series), P. Dybjer, S. Lindström, E. Palmgren and G. Sundhölm (eds.), New York and Dordrecht: Springer Verlag.

[^rathjen-2017]: –––, 2017, “Proof Theory of Constructive Systems: Inductive Types and Univalence”, in G. Jäger, and W. Sieg (eds.), *Feferman on Foundations* (Outstanding Contributions to Logic: Volume 13), Cham: Springer, pp. 385–419.

[^rathjen-2023]: –––, 2023, “An Introduction to Constructive Set Theories: An Appetizer”, in D. Bridges, H. Ishihara, M. Rathjen, and H. Schwichtenberg (eds.), *The Handbook of Constructive Mathematics*, Cambridge: Cambridge University Press, pp. 20–60.

[^rathjen-1998-2]: Rathjen, M., E. Griffor, and E. Palmgren, 1998, “Inaccessibility in constructive set theory and type theory”, *Annals of Pure and Applied Logic*, 94: 181–200.

[^richman-2000]: Richman, F., 2000, “The fundamental theorem of algebra: a constructive development without choice”, *Pacific Journal of Mathematics*, 196: 213–230.

[^richman-2001]: –––, 2001, “Constructive mathematics without choice”, in *Reuniting the Antipodes: Constructive and Nonstandard Views of the Continuum* (Synthese Library 306), P. Schuster, *et al*. (eds.), Dordrecth: Kluwer, pp. 199–205.

[^russell-1908]: Russell, B., 1908, “Mathematical logic as based on the theory of types”, *American Journal of Mathematics*, 30: 222–262. Reprinted in van Heijenoort (1967), 150–182.

[^scedrov-1981]: Scedrov, A., 1981, “Consistency and independence results in Intuitionistic set theory” in *Constructive mathematics* (Lecture Notes in Mathematics 873), F. Richman (ed.), Berlin: Springer, pp. 54–86.

[^scedrov-1982]: –––, 1982, “Independence of the fan theorem in the presence of continuity principles” in *The L.E.J. Brouwer Centenary Symposium*, A.S. Troelstra, and D. van Dalen (eds.), Amsterdam: North-Holland, pp. 435–442.

[^scedrov-1985]: –––, 1985, “Intuitionistic set theory” in *Harvey Friedman’s research on the foundations of mathematics*, L.A. Garrubgtib *et al*. (eds.), Amsterdam: Elsevier.

[^schütte-1965]: Schütte, K., 1965, “Predicative well-orderings”, in *Formal Systems and Recursive Functions*, J. Crossley and M. Dummett (eds.), Amsterdam: North-Holland, pp. 279–302.

[^schütte-1965a]: –––, 1965a, “Eine Grenze für die Beweisbarkeit der Transfiniten Induktion in der verzweigten Typenlogik”, *Archiv für mathematische Logik und Grundlagenforschung*, 7: 45–60.

[^simpson-2005]: Simpson, A., 2005, “Constructive set theories and their category-theoretic models”, in *From Sets and Types to Topology and Analysis: Towards Practicable Foundations for Constructive Mathematics* (Oxford Logic Guides 48), L. Crosilla and P. Schuster (eds.), Oxford: Oxford University Press.

[^swan-2014]: Swan, A.W., 2014, “CZF does not have the existence property”, *Annals of Pure and Applied Logic*, 165: 1115–1147.

[^troelstra-1988]: Troelstra, A.S., and van Dalen, D., 1988, *Constructivism in Mathematics* (two volumes), Amsterdam: North Holland.

[^tupailo-2003]: Tupailo, S., 2003, “Realization of constructive set theory into Explicit Mathematics: a lower bound for impredicative Mahlo universe”, *Annals of Pure and Applied Logic*, 120: 165–196.

[^voevodsky-2015]: Voevodsky, V., 2015, “An experimental library of formalized mathematics based on univalent foundations”, *Mathematical Structures in Computer Science*, 25: 1278–1294.

[^weyl-1918]: Weyl, H., 1918, “Das Kontinuum. Kritische Untersuchungen über die Grundlagen der Analysis”, Veit, Leipzig.

[^ziegler-2012]: Ziegler, Albert, 2012, “Generalizing realizability and Heyting models for constructive set theory”, *Annals of Pure and Applied Logic*, 163 (2): 175–184.

[^ziegler-2014]: –––, 2014, “A cumulative hierarchy of sets for constructive set theory”, *Mathematical Logic Quarterly*, 60 (1-2): 21–30.

[^ziegler-2014a]: –––, 2014a, “Large sets in constructive set theory”, Ph.D. Thesis, University of Leeds, [[available online](http://etheses.whiterose.ac.uk/8370/)]
