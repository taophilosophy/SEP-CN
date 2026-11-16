# Paradoxes and Contemporary Logic
**First published Tue Oct 16, 2007; substantive revision Wed Apr 30, 2025**

*Cantini, Andrea, Bruni, Riccardo*

By “paradox” one usually means a statement claiming something which goes beyond (or even against) ‘common opinion’ (what is usually believed or held). Paradoxes form a natural object of philosophical investigation ever since the origins of rational thought; they have been invented as part of complex arguments and as tools for refuting philosophical theses (think of the celebrated paradoxes credited to Zeno of Elea, concerning motion, the continuum, the opposition between unity and plurality, or of the arguments entangling the notions of truth and vagueness, credited to the Megarian School, and Eubulides of Miletus). Paradoxes—termed as *Insolubilia*—form also a substantial part of logical and philosophical investigations during the Middle Ages.

This entry concentrates on the emergence of non-trivial logical themes and notions from the discussion on paradoxes from the beginning of the 20th century until 1945, and attempts to assess their importance for the development of contemporary logic. Paradoxes involving vagueness, knowledge, belief, and space and time are treated in separate entries.

A terminological warning is in order. The word “antinomy” is used below as alternative to, and synonymous with, “paradox”. Most paradoxes—but not all—involve contradictions; for such cases, we often use the word “contradiction” as well.

## 1. Introduction

Between the end of the 19th century and the beginning of the 20th century, the foundations of logic and mathematics were affected by the discovery of a number of difficulties—the so-called paradoxes—involving *fundamental notions and basic methods of definition and inference*, which were usually accepted as unproblematic. Since then paradoxes have acquired a new role in contemporary logic: indeed, they have led to theorems (usually negative results, such as unprovability and undecidability) and they are not simply confined to the realm of a sterile dialectic. Several basic notions of logic, as it is presently taught, have reached their present shape at the end of a process which has been often triggered by various attempts to solve paradoxes. This is especially true for the notions of *set* and *collection* in general, for the basic *syntactical and semantical concepts of standard classical logic* (logical languages of a given order, the notion of satisfiability, definability). After the first forty years, the by-products of the paradoxes included axiomatizations of set theory, a systematic development of type theory, the foundations of semantics, a theory of formal systems (at least *in nuce*), besides the introduction of the dichotomy *predicative/impredicative* which was important for conceptual reasons, but also for the future of proof theoretical methods.

## 2. Paradoxes: early developments (1897–1917)

Early work on paradoxes of particular importance pertained to the following notions:

1. ordinal and cardinal numbers (Burali-Forti, Cantor);
2. property, set, class (Russell, Zermelo);
3. proposition and truth (Russell);
4. definability and the arithmetical (or atomistic) continuum (Richard, König, Bernstein, Berry, Grelling).

Some of these contradictions are already treated as separate entries in this encyclopedia (liar paradox, Russell’s paradox); the emphasis here will be on the background problems, their mutual links and the interaction with foundational and philosophical issues.

### 2.1 Difficulties involving ordinal and cardinal numbers

The earliest modern paradoxes concerned the notions of ordinal and cardinal number. Burali-Forti, a mathematician of Peano’s school, attempted to prove that the ordinal numbers are not linearly ordered. Assuming by contradiction that the class $\mathbf{ON}$ of all ordinals could be linearly ordered, he observed that then $\mathbf{ON}$ itself would be well-ordered and it would possess an ordinal $\Omega \in \mathbf{ON}$. Thus $\mathbf{ON}$ would be similar (order-isomorphic) to a proper initial segment of itself, the one determined by $\Omega$, contradicting a well-known theorem about well-ordered sets. The result was published in 1897 and, though Burali-Forti’s original aim is impossible to achieve, his argument showed that the collection $\mathbf{ON}$ is problematic at best (Moore-Garciadiego 1981)[^moore-1981].

The father of set theory, Cantor, had noticed similar difficulties already in 1895 (as witnessed by Bernstein and by letters to Hilbert and Dedekind). Indeed, in a second letter to Dedekind of August 31, 1899 Cantor pointed out another problem, involving the notion of the cardinal number and implying that one cannot consistently think of “the set of all conceivable sets”, say $M$. Were $M$ a genuine set, then it would possess a cardinal number $m$, which would be the maximum cardinal number. But one could also consider the set $\wp(M)$ of all subsets of $M$, and by Cantor’s theorem the cardinality of $\wp(M)$ ought to be strictly bigger than the purported maximum $m$: contradiction.

As a consequence, Cantor suggested a crucial distinction—still regarded as “subjective”, i.e., mathematically not precise, by Hilbert (as late as 1904, see van Heijenoort 1967, p. 131)[^heijenoort-1967]—between totalities that cannot be conceived as a whole (the *inconsistent* ones) and those which can be regarded as completed (*fertige Menge*). Roughly, the former is a collection that cannot be an element of other collections, whereas the latter is a small collection, which can be an element of other collections (see also the entry on the early development of set theory). This corresponds to the distinction between *classes* and *sets*, later made precise and axiomatized in the class-theoretic approach (von Neumann, Bernays, Gödel); it is reminiscent of the Russellian limitation-of-size doctrine (see 3.1 below; Garciadiego 1992)[^garciadiego-1992].

In the case of the difficulty discovered by Burali-Forti, the consequence for Cantor was that the multiplicity (*Mannigfaltigkeit*) of ordinal numbers is itself well-ordered, but is not a set: hence, no ordinal can be assigned to it, and the antinomy is resolved.

### 2.2 Russell’s contradiction

The second famous published antinomy (Russell 1903, paragraphs 78, 101–106; Frege 1903, Appendix, dated October 1902; see the entry Russell’s paradox and Klement 2010)[^frege-1903][^russell-1903][^klement-2010] takes us from Cantor’s paradise into the realm of the foundations of logic and the philosophy of mathematics. It is strikingly simple, involves only predicate application, and it has an explicit self-referential (*reflexive*) character. In Russell’s own words (June 16, 1902, letter to Frege, translation in van Heijenoort 1963, pp. 124–125),

> let $w$ be the predicate: to be a predicate that cannot be predicated of itself. Can $w$ be predicated of itself? From each answer, the opposite follows. Likewise, there is no class (as a totality) of those classes which, each taken as a totality, do not belong to themselves. From this I conclude that under certain circumstances a definable collection does not form a totality.

Russell was at first entangled in the study of “the contradictions in the relation of continuous quantity to number and the continuum” (cited in Moore 1995, p. 219)[^moore-1995], and he obtained his contradiction (May 1901) as a result of considering the antinomy arising with Cantor’s theorem (see Russell 1903, footnote 7, par. 344; par. 100, p. 101)[^russell-1903]. Russell probably realized the importance of the discovery only after Frege’s reply. The effect of the antinomy is that it is impossible to have an abstraction operation $\phi \mapsto \{x \mid \phi \}$ mapping injectively any concept (property) *φ* into its extension (the class of all $x$ such that $\phi(x))$ (i.e., so that if the classes defined by *φ* and *ψ* are equal, then $\phi(a)\leftrightarrow \psi(a)$, for every object $a)$. As a consequence, it is also impossible to lay out the foundations of set theory on a *pure logical notion of set* where membership faithfully mirrors predicate application, in the sense that, in the light of Frege, $x \in y$ means that (1) $y = \{x \mid \phi(x)\}$ for some concept *φ*, and (2) *φ* truly applies to $x$. (For historical details on Russell’s discovery of the paradox, see Moore 1995)[^moore-1995].

### 2.3 Russell’s paradox involving propositions and truth: the emergence of type theory

Russell’s *Principles of Mathematics* (1903) contains extended discussions of Russell’s and Burali-Forti’s paradoxes in various forms in the sections 78, 84–85, 101, 301. Russell’s paradox is adapted to show that a propositional function *φ* cannot be a logical subject (i.e., as separated from its argument; it is not *saturated* in Frege’s terms); otherwise, *φ* would apply to itself, $\neg \phi(\phi)$ would be a propositional function and it would be possible to reproduce the inconsistency.

In ch. 10, section 102, Russell also gives a form of Cantor’s theorem, which captures the logical essence of diagonalization (this version is by now folklore): no binary relation can parameterize all unary predicates over a given domain $U$ (i.e., no binary relation $R$ exists such that for all unary predicates $P$ over $U$, there is an object $a$ in $U$ for which one has: for all $x$ in $U, R(a, x) \leftrightarrow P(x))$.

In sum, Russell’s contradiction shows the critical status of apparently safe logical principles: either one has to give up the assumption that “any propositional function containing only one variable is equivalent to asserting membership for a class defined by the propositional function” (i.e., the comprehension principle); or one has to reject the idea that “every class can be taken as one term” (pp. 102–103).

In Russell’s hands the paradox applies to predicates, classes, and propositional functions and leads to a new picture of the logico-mathematical universe, which is outlined in a first exposition of the doctrine of types: to each propositional function *φ* is associated a *range of significance*, i.e., a class of objects to which the given *φ* applies in order to produce a proposition; moreover, precisely the ranges of significance form types. However, there are objects that are not ranges of significance; these are just atoms (i.e., *urelemente* or individuals) and they form the lowest type. The next type consists of classes or ranges of individuals; then one has classes of classes of objects of the lowest type, and so on (see also the entry on type theory)..

New difficulties still arise if one accepts that propositions form a type (as they are the only objects of which it can be meaningfully asserted that they are true or false). First of all, there are obviously at least as many propositions as objects (just consider the map associating with $x$ the proposition expressed by $(x = x)$; p. 527). On the other hand, if it is possible to form types of propositions, there are more types of propositions than propositions, by Cantor’s argument. Then we can inject types of propositions into propositions by means of the notion of *logical product*. Let $m$ be a class of propositions and let $\Pi m$ be the proposition “every proposition of $m$ is true” (regarded as a possibly infinitary conjunction); then, if $m$ and $n$ are different classes, the propositions $\Pi m$ and $\Pi n$ are different, i.e., the map associating to $m$ its product $\Pi m$ is injective. Therefore, if we consider the class

$$ \{p \mid \exists m(\Pi m = p \amp p \not\in m)\} = R, $$

we have, by injectivity, a contradiction.

Of course, if one were to adopt the extensional point of view, and hence identify equivalent propositions, the contradiction above could not be derived. Russell, however, sticks to an intensional point of view, stressing that equivalent propositions often can be quite different. So one is apparently forced to reject the assumption that propositions form *one type*, and hence to require that they ought to have *various types*, while logical products ought to have propositions of only one type as factors.

This was eventually the basis of the ramified theory of types, but in 1903 Russell still regarded the suggestion as harsh and artificial. As the footnote on p. 527 shows, he believed that the set of all propositions is a counterexample to Cantor’s theorem.

### 2.4 The mathematicians and the contradictions: Hilbert and Zermelo

Zermelo independently discovered Russell’s paradox in Göttingen (as witnessed by Hilbert and Husserl) in the following form: a set $M$ that comprises as elements all of its subsets is inconsistent. Indeed, consider the set $M_0$ of all elements of $M$ which are not elements of themselves (e.g., the empty set is in $M_0)$. This set is a subset of $M$ and hence by assumption on $M, M_0 \in M$. If $M_0 \in M_0$, then $M_0$ is not a member of itself. Hence $M_0 \not\in M_0$ and since $M_0 \in M, M_0 \in M_0$: contradiction.

In addition, Hilbert had noticed in unpublished work (see Kahle and Peckhaus 2002)[^kahle-2002] that additional contradictions of a mathematical nature can arise. The first one derives from assuming that there is a well-defined set $C$ which satisfies the following closure conditions: (i) the set $N$ of natural numbers is an element of $C$; (ii) $X^X \in C$, whenever $X \in C$ (where $X^X$ is the set of all functions from $X$ to $X)$; (iii) $\cup X \in C$, whenever $X \subseteq C$. Then by (iii), $\cup C = U \in C$ and finally $F = U^U \in C$. But by definition of union, $F \subseteq U$; hence there would exist a map of $U$ onto $F$ and a contradiction could be derived by diagonalization.

Furthermore, as is witnessed by Hilbert’s unpublished *Sommer Vorlesung* 1905 (see Kahle 2004)[^kahle-2004], Hilbert discovered a remarkable functional version of Russell’s paradox, later to become popular in the context of combinatory logic, lambda calculus and recursion theory. The argument is based on *functional self-application* and hence *direct self-reference*.

The contradiction is obtained by assuming that the universe includes everything, i.e., variables range over both objects and functions, and that there are at least two distinct objects. Then one introduces a new operation (universal application in our sense): $xy$ is the result of applying $x$ to $y$. Given two distinct objects 0 and 1, and on the assumption that the universe is closed under arbitrary definition by cases, there exists an object $f$ such that $fx = 0$, if $xx \ne 0$, and $fx = 1$, if $xx = 0$. Then one chooses $x = f$ (as $x$ ranges over everything) and easily derives a contradiction.

The results of the Hilbert school were not published because contradictions and paradoxes were regarded as symptoms of growth and as temporary difficulties. The diagnosis was that traditional logic is insufficient and the theory of concept-formation needs to be sharpened. Any concept $C$ is given in a network of concepts (letter of Hilbert to Frege, Dec. 27, 1899; see Frege 1976, pp. 79–80)[^frege-1976], and this network is determined by the axioms. Only the consistency of the axioms that define the concept guarantees the legitimacy of $C$. In a nutshell: paradoxes tell us that we must develop a metamathematical analysis of the notions of proof and of the axiomatic method; their importance is methodological as well as epistemological.

### 2.5 Around 1905: difficulties arising from definability and the continuum

As the reactions of the mathematical world made clear, the paradoxes were crucially involved around 1905 when basic problems of set theory were worked on. Indeed, the new contradictions not only affected the conception of set and logical concepts, they also came to include the notion of *definability* and its relation with a fundamental issue: the structure of the mathematical continuum and in particular whether the continuum can be well-ordered and whether Cantor’s Continuum Hypothesis (CH) holds.

At the Heidelberg Congress in 1904, Julius König tried to refute Cantor’s continuum hypothesis. Due to a mistake discovered by Zermelo, his paper was immediately withdrawn, but the subsequent year, König produced a new argument.

Consider the reals which are *definable in finitely many words*. They form a countable sequence: $E_0, \ldots, E_n,\ldots$. Since the continuum is uncountable, there exist reals not occurring in the given enumeration. Assuming that the continuum is well-ordered, there exists “the least real $E$ which is not in the sequence $\{E_n \mid n \in \Omega \}$”; this real is not in the sequence, but the very expression “the least real $E$ which is not in the sequence” *defines $E$ with finitely many words*; so $E$ occurs somewhere in the sequence: contradiction!

König also observed that the argument extends to the second number class and a similar paradox could be obtained by considering the collection $\mathbf{FOD}$ of finitely definable countable ordinals. In this case, taking inspiration from Cantor, König’s solution is that Cantor’s second number class is not a set in a proper sense (a completed totality). To define a set, according to König, one should provide not only a rule for defining its elements, but also a means for distinguishing them.

A contradiction related to König’s had been published slightly earlier by Jules Richard, a mathematician of a Lyceé in Dijon. Using an enumeration of all permutations with repetitions of the twenty-six letters of the French alphabet, Richard noticed that the set $E$ of reals that can be defined by finitely many French words is denumerable and hence one can assume to have an enumeration $u_1, u_2,\ldots$ of all those numbers. But then one can define the following real $N$: the integer part of $N$ is 0, while its $n$th decimal digit of $N$ is $p+1$ if $u_n$ has the $n$th decimal digit $p$ different from both 8 and 9; otherwise, the $n$th decimal digit of $N$ is 1. By construction, $N$ will not occur in $u_1, u_2,\ldots$. On the other hand, if we consider that $N$ is defined by means of a finite collection of letters, this must occur in $u_1, u_2,\ldots$.

Contrary to König, Richard did not rely upon the well-ordering of the continuum, and the proposed solution is interesting for the foundational debate to come. He pointed out that the definition of the number $N$ refers to the totality of definable reals, to which $N$ itself belong; but no object should be definable in terms of a collection containing it. So it appears that the definition is viciously circular, and that makes the definition illusory. This idea soon became the basis of Poincaré’s solution, and eventually also Russell’s (see below 3.1, the issue of impredicatively defined collections).

So, why definability? The motivation was made clear for instance by Bernstein’s “Die Theorie der reellen Zahlen” (1905a), where Cantor’s continuum hypothesis was claimed to be settled in the positive. He criticized the so called “Dirichlet notion” of arbitrary function and stated that it is possible to give a foundation to the continuum using only computable reals, i.e., reals possessing an explicit “formation law” (“*Bildungsgesetz*”).

According to him, this is not a restriction since—he claims—there are nondenumerably many computable reals in his sense. He also states that it is possible to display the new computable continuum in a hierarchy (i.e., a $\subset$-increasing sequence) $\{B_{\alpha} \mid \alpha \lt \aleph_1\}$ of subsets of $N^N$, which is defined in such a way that each $B_{\alpha}$ is at most of cardinality $\aleph_1$ and hence that the cardinality of the union of the sequence is at most $\aleph_1$. The idea is to start with a basic domain $B_0 \subset N^N$ of simple functions (e.g., those having finitely many values), then to define a new domain $B_1$ which extends $B_0$ with operations that are defined from elements of $B_0$, and so on.

Though his claims are not justified, in the light of Gödel’s later work on constructibility, one might say that Bernstein’s basic intuition was sound: the continuum problem can be settled, if one has an appropriately general notion of definability (or computability, constructibility) and by iterating it along the ordinals.

This question was ultimately connected with the problem of understanding the atomistic continuum. The arithmetized conception—in the sense of Dedekind or Cantor, where real numbers are identified with suitable sets of rationals—shifted the attention towards *arbitrary infinite sequences of natural numbers*. But this notion was not so easy to accept. According to Bernstein (Bernstein 1905a, p. 449)[^bernstein-1905a], an infinite sequence (or an infinite set) must be given by a genuine rule. But *what is a rule*? Since one must be liberal (in order not to have just special classes of reals, if one is too restrictive), one is naturally driven to think of arbitrary finitely described laws, shifting the attention towards *the syntax of the rules*. However, unless one considers ordinary language, no such syntax is available and this engenders indeterminacy (this is Peano’s diagnosis, see below Peano 1902–1906)[^peano-1906].

The need for a specification of infinite sets is crucial in the discussion of the related well-ordering problem. It also affects the related issue of the classification of discontinuous functions and analytically representable functions of real variables, tackled by the French semi-intuitionists Borel, Baire and Lebesgue. At the same time, they held the view that a mathematical entity (like an infinite set or a function) exists only insofar as it is “nameable by a finite number of words”, against the platonistic views of Hadamard and Zermelo (see Borel et al. 1905)[^borel-1905].

## 3. Paradoxes, predicativism and the doctrine of types: 1905–1913

In the light of the foundational debate, the following years were rich in seminal work: new paradoxes were discovered (Berry, Grelling-Nelson), an old paradox—the Liar—showed up again, a comprehensive view of the contradictions of logic and mathematics was masterfully outlined in the opening section of Russell’s 1908 paper and the preceding Russell 1906a, while a conceptual distinction between two kinds of paradoxes was set forth in Peano’s paper of 1906. Also, the basic ideas of predicativity emerged in the discussion between Poincaré, the leading mathematician of the time, and Russell. Even more important for the history of mathematical logic, fundamental technical advances for solving the paradoxes and shaping the foundations of logic and mathematics were made: Russell’s theory of (ramified) types and Zermelo’s axiomatization of set theory.

### 3.1 Poincaré and Russell on contradictions

Russell’s and Poincaré’s ideas for solving paradoxes are to be found in a number of papers published in the period 1905–1912:

1. the long essay “Les mathématiques et la logique”, in the *Revue* *de Métaphysique et de Morale* (Poincaré 1905, 1906a)[^poincaré-1905][^poincaré-1906a], wherein Poincaré strongly criticizes axiomatic and logicist foundations;
2. Russell’s “On some difficulties in the theory of transfinite numbers and order types” (read in 1905, published in 1907);
3. Poincaré’s counter-attack (Poincaré 1906b)[^poincaré-1906b], the subsequent papers by Russell in the *Revue* (Russell 1906)[^russell-1906] and the *American Journal of Mathematics* (Russell 1908)[^russell-1908], and Poincaré’s last articles (1909a, 1910, 1912).

Poincaré (1906b)[^poincaré-1906b] took the contradictions as grounds to defend an intuitionistic, Kantian point of view. According to him, number-theoretic induction and the axiom of choice constitute independent intuitions, truly synthetic a priori judgements. He then argues against Russell’s logical definition of natural numbers as those numbers which belong *to all recurrent classes* (those classes which contain 0 and are closed under successor). His objection is that the definition is not admissible since it refers essentially to a totality to which the class to be defined belongs—the definition is *impredicative*—and hence it is to be regarded as *circular.* But, according to Poincaré, *mathematical objects do not exist without a proper definition*, and a proper definition must be *predicative*, i.e., it must avoid *vicious circles*; Poincaré thus somewhat extended Richard’s diagnosis.

Poincaré’s views evolved over the years and in the debate with Russell. In the later period, he advanced a novel approach to predicativity, which, though informally sketched, is suggestive of later developments in definability and proof theory (see Feferman 1964, Heinzmann 1985)[^feferman-1964]. He no longer insisted on the vicious circularity of the definition involved in the contradictions; instead, he held the view that *a predicative classification is characterized by invariance*, i.e., that it cannot be affected by the introduction of new elements; by contrast, impredicative notions are subject to constant modification whenever new elements are introduced.

In the light of contemporary logic, Poincaré is hinting at some form of *absoluteness or invariance under extension* (that will be made precise by Kreisel 1960 via model theory and recursion theory)[^kreisel-1960]: his ideas will inspire the non-ramified approach to the foundations of predicative analysis.

In his last contribution to *Acta Mathematica* (1909) and in his fifth Göttingen lecture (1910), he also gave a restatement of Richard’s paradox, as a refinement of Cantor’s theorem, in the form: “there is no definable enumeration of definable reals”.

While mathematicians and Poincaré himself focused on the problems raised by the contradictions insofar as they involved the foundations of specific mathematical notions (the continuum, the natural numbers, the theory of cardinal and ordinal numbers), Russell directly attacked the *comprehension principle*, that is, the assumption that certain propositional functions determine a class (see also 2.3 above). The paradoxes prove that a propositional function may be well-defined for every argument, and yet the collection of the values for which it is defined need not be a class. So *the crucial problem becomes logical*: to give a criterion for selecting those propositional functions which give rise to classes (understood as well-defined objects).

Under the influence of Poincaré, Russell (1906, p. 634) accepted *the vicious circle principle*, for which he used a formulation in the terminology and adopting the notions of formal logic as formulated by Peano:

> Whatever comprises an apparent variable should not be one among the possible values of that variable.

In logical terms, we are not allowed to quantify over a given class $X$ when defining an element of $X$ itself (see also the entry on definitions).

Of course, the vicious circle principle is not itself a theory, but a condition any adequate theory has to satisfy. Russell (1906, 1907)[^russell-1907][^russell-1906] tentatively proposed three alternative approaches: the zigzag theory, the theory of limitation of size, and the no-classes theory. The zigzag theory attempts to capture the idea that the right functions ought to be ‘simple’, while according to the second view, ‘predicative’ would be characterized by a certain limitation of the size of classes which can be predicatively defined (e.g., the collection of all ordinals $\mathbf{ON}$ is too large). In the no-classes theory, classes are not independent entities and anything said about them is to be regarded as an abbreviation of a statement about their members and the propositional functions defining them. This is not far from Poincaré’s idea that mathematical objects should be specified in finitely many words. However, Russell developed his own technical devices—such as the ‘substitution method’ (Landini 1998), and the contextual elimination of definite descriptions (see the entry Russell) – in order to implement his ideas.

In contrast to Poincaré, Russell 1906 did not consider the actual infinite as an essential component of the foundational malaise, and he stressed that contradictions arise even if the infinite is not involved. This is clearly shown by the Liar paradox in the form ‘I am lying’. As far as we know, it is exactly at this point in time that the (probably) most cited semantical puzzle in the history of logic regains a conspicuous position in logical analysis.

In his analysis of the Liar paradox, Russell assumed that there exists a true entity—the proposition—that is presupposed by a genuine statement (e.g., when I say that Socrates is mortal, there is a fact corresponding to my assertion and it is this fact that is called ‘proposition’). The same holds if the statement is false, but not in the case where the statement itself contains quantified variables.

The paradox is then solved by construing the Liar as ‘there is a proposition that I state and that is false’; hence the statement contains *a quantification (hence an apparent variable) over the collection of all propositions*, and it is not a proposition in a proper sense (Russell 1906, 642–644)[^russell-1906]. So the conclusion is that the Liar is false because it does not state a proposition.

Similar considerations apply to *the paradox suggested by Berry*, which is briefly stated in Russell 1906 for the first time in published form, and has the merit of not going beyond the domain of finite numbers.

Consider the natural numbers that are definable by means of less than 18 syllables: this set is non-empty and finite. So there exist numbers which are not definable using less than 18 syllables. Consider the least such number: clearly, by definition, it is not definable with less than 18 syllables.

On the other hand such a number is definable with less than 18 syllables, since it is uniquely determined by the expression “the least number not definable with less than 18 syllables”, which itself has less than 18 syllables.

For the sake of historical accuracy, we should remark that Beppo Levi, who made an articulated contribution to the debate on the axiom of choice in the first two decades of the 1900s, outlined an antinomy which is essentially a variant of Berry’s paradox in the context of discussing Richard’s paradox (see Levi 1908, and also Lolli 2007 and Bruni 2013 for further comments about Levi’s approach to paradoxes)[^levi-1908][^bruni-2013][^lolli-2007].

### 3.2 Mathematical logic as based on the theory of types

The Russellian theory of types is widely known and investigated in the literature (see the entries on type theory and Bertrand Russell): it is of current interest and has descendants in logic and its applications. It was first developed by Russell in the fundamental memoir *Mathematical Logic as based on the theory of types* of 1908.

The doctrine of types is based upon the observation that universal quantification—understood as full generality, i.e., when $x$ ranges ‘over the whole universe’—does not make sense: when we state that $\forall x\phi(x)$ is true, we only claim the function $\phi(x)$ has the value ‘true’ for all arguments $x$ for which *it is meaningful*. The essential point is that each propositional function has a range of significance, i.e., *a type*, and *quantification is legitimate only over types*. Formally speaking, each variable must have a preassigned type. The paradoxes (or reflexive fallacies) prove that certain collections, such as the totality of all propositions, of all classes and so on, cannot be types. So we can quantify over the collection of men, but we cannot properly state ‘all propositions of the form $p\vee \neg p$ are true’. Therefore, the logical entities divide into types, and, in particular, *every propositional function must have a higher type than its arguments*. Moreover, in the light of the vicious circle principle, the notion of *order* must also be introduced. No object can be defined by quantifying over a totality which contains the object itself as element; hence the order of every propositional function must be greater than the order of propositional functions over which it quantifies.

The main idea is clarified in Russell 1908 (pp. 163–164) by considering how propositions can be arranged into a suitable “ramified” hierarchy, according to their order and so as to satisfy the vicious circle principle. First of all, there are elementary propositions, i.e., those containing no bound variables at all, while the lowest type consists of *individuals.* Individuals are entities without logical structure and can be regarded as the subjects of elementary propositions. The second logical type embraces the *first order propositions*, i.e., those whose quantifiers (if any) range only over individuals. Quantification over first order propositions gives rise to a new type, consisting exactly of *second order propositions*. In general, the $(n + 1)$th logical type comprises propositions of order $n$, which contain quantification only up to the $(n - 1)$th order.

Since a propositional function can be obtained from a proposition ‘by treating one or more of its constituents as variables’, the hierarchy of types and orders is naturally lifted to propositional functions, and it makes sense to speak of *order of a function*, its order being roughly the order of the value (i.e., a proposition) which the function assumes when it is applied to an argument for which it makes sense. So, for instance, a function which applies to individuals and takes first-order propositions as values is first-order.

Following the doctrine of types, we must replace ‘all propositions’ by ‘all propositions of order $n$’ for a given $n$. Hence the Liar sentence becomes “it is not true of all propositions $p$ of order $n$, that if I affirm $p, p$ is true”, which is a proposition of order $n + 1$. Then the Liar is simply false rather than contradictory; and this solves the paradox. Similar arguments solve the other paradoxes.

In this theory, *predicative functions* of one argument, i.e., those having as order the successor of the order of their argument, play a crucial role. For instance, a predicative function of an individual variable must have order 1 (in current terminology, it is elementarily definable and quantifies *only* over individuals). The *axiom of reducibility* (AR) states that *every propositional function is equivalent, for all its values, to a predicative function of the same variables.* So, for instance, we might have a definition of a property $P(n)$ of natural numbers (regarded as individuals) which quantifies over, say, second-order propositions. But AR implies that there exists a function $P^* (n)$ which is satisfied by exactly the same numbers as $P(n)$ and is predicative, i.e., it involves quantification *only* on numbers.

Thus, according to the axiom of reducibility, statements about arbitrary functions can be replaced by statements about predicative functions; and predicative functions play the role of classes, i.e., canonical representatives of arbitrary complex concepts (e.g., among the possible properties of different order which have the same extension as $P(n)$, $P^*(n)$ canonically represents the class of numbers satisfying $P(n))$.

Besides the axiom of infinity, AR is an essential tool for reconstructing classical mathematics, but it is a strong existential principle, apparently in conflict with the philosophical idea that logical and mathematical entities are to be constructively generated according to the vicious circle principle. Nonetheless, it was adopted in the (first edition of the) monumental *Principia Mathematica*, written in collaboration with A.N. Whitehead and published in 1910 (vol. 1), 1912 (vol. 2) and 1913 (vol. 3).

Interestingly, the basic idea underlying Russell’s ramified hierarchy of types is a crucial ingredient in Gödel’s later consistency proof of the continuum hypothesis via its inner model $L$ of constructible sets. Also, as already observed in Gödel (1944), a form of AR becomes true in $L$ in the sense that, roughly, an *arbitrary* propositional function of natural numbers is extensionally equivalent to some function of order *α*, for some countable ordinal *α* (see the entry Kurt Gödel). Other important applications of ramified hierarchies have been given since the late fifties in different fields (from recursion theory to proof theory; see the entry on type theory).

### 3.3 Completing the picture

There is a sizeable literature on paradoxes already in the early years of the 20ᵗʰ century, which is not at all exhausted by the previous discussion. Refinements and variations of foundational and logical interest are to be found in the works of several authors, including prominent mathematicians, among them Peano, Borel, Schönflies, Brouwer, and Weyl. Some of the more stimulating and original proposals are surveyed in the rest of this section.

#### 3.3.1 Peano, Schönflies, Brouwer, and Borel

Peano’s criticism (in *Additione a Super Theorema de Cantor-Bernstein*) of Richard’s paradox is mainly known because it points out that *“Richard’s example pertains to linguistics, not to mathematics”* and this statement opens up the distinction between set-theoretic or mathematical antinomies and semantical antinomies: the weak point in Richard’s definition is that to some extent it is symbolic and formal, but it also makes use of the natural language (“*lingua commune*”); this contains ideas that are quite familiar but nevertheless are not sharply defined and are ambiguous (Peano 1906, p. 357–358)[^peano-1906]. For instance, there is no precise criterion for deciding whether a given expression of the natural language represents a rule uniquely defining a number.

In spite of that, Peano elaborated a formal solution. He tried to get rid of vagueness and reference to $E$, the set of finitely definable reals in the unit interval, by fixing an explicit “Gödel-numbering”: given a natural number $n$, write $n$ in base $B$, for sufficiently large $B$ (so as to include the number of alphabet letters plus punctuation marks). Then each number is assigned a finite string of symbols in the natural language, and in certain cases the string will define a number, $\Val(n) =$ “the decimal number which is determined by the expression encoded by $n$ and interpreted according to the rules of the natural language”. Now, in order to get the paradox, one has to prove that there exists a unique number $N$ in (0, 1), satisfying the condition given by Richard (see 2.5 above), but this condition, and hence $N$ itself, depends on $\Val$, which is possibly obscure and cannot be defined exactly according to the rules of mathematics (p. 352, p. 358). The conclusion is that no such a real can exist and Richard’s definition is defective in the same way that “the greatest prime number” is.

Schönflies and Brouwer, by contrast, reacted to the paradoxes while strongly opposing axiomatic and formal methods.

Schönflies (1906)[^schönflies-1906] stuck to a contentual, genetic conception of sets. According to him, sets are generated and, once formed, are conceptually invariant. When a new set is built up, it is added to those that have been used in forming it, without altering their pre-existent structure. So self-membership does not make sense, the universal set does not exist and Russell’s paradox disappears. His view can be seen as hinting at a sort of iterative conception of sets. For Schönflies, the contradictions arise in logic, as opposed to mathematics, and are due to the scholastic nature of logic. He regarded logic as having an unhealthy influence (“*unheilvollen Einflüss*”) on mathematics (“*Für den Cantorismus, aber gegen den Russellismus*” is the final motto of Schönflies 1911).

Brouwer’s approach to paradoxes was also based on a contentual conception of mathematics. It can be found in the dissertation of 1907, chapter III (cf. also van Dalen 1999, pp. 105). As to Russell’s contradiction, Brouwer noticed that the usual logical principles only hold for words with mathematical content, not for linguistic systems, like those of Peano or Russell. For instance, in order to decide whether a class falls under a propositional function, the class has to be a completed totality. The contradictions show that there are propositional functions which define complementary (disjoint) classes and yet do not satisfy the tertium non datur. Similar ideas can be found in the philosophical paper of 1908, “On the unreliability of tertium non datur” (see van Dalen 1999).

A positive by-product of Richard’s paradox in Brouwer’s work (1907, p. 149) is the notion of *denumerably unfinished set*, i.e., a set in which we can determine only denumerable subsets of elements, but where these denumerable subsets do not exhaust the given set, so that one can immediately produce new elements of the set from any given denumerable such subset. Typical examples of denumerably unfinished sets are the totality of countable ordinals, the points of the continuum, and in particular, as could be shown using Richard’s paradox, the set of all definable points of the continuum (1907, p. 150). Brouwer considers Burali-Forti’s contradiction not as a mathematical paradox, since it concerns a logical structure (the collection of all ordinals), which is not a well-defined mathematical object and has no proper mathematical content. Mathematically speaking, the contradiction can be avoided by denying that the largest well-ordered type has a successor order type (p. 153; this is analogous to Bernstein 1905b)[^bernstein-1905b].

Among the French mathematicians, the semi-intuitionist Borel (1908)[^borel-1908] introduced the distinction between *effectively enumerable* sets and *denumerable* ones. The Richard paradox is then solved by observing that Richard’s set $E$ is certainly denumerable, because one can only determine at most a denumerable set of reals by finite means. Yet $E$ is not effectively enumerable, i.e., one cannot produce with finitely many words a procedure for assigning unambiguously a rank (i.e., a position) to each element of the set. In order to make the enumeration of $E$ effective, one ought to have solved all the mathematical problems which one could possibly state, because there are expressions which become definitions of a real only modulo a proof or solution of a certain problem. Borel has in mind a particular example: consider the expression “the unique transcendental number whose decimal expansion is obtained from that of *π* by replacing everywhere 7 with 8, and 8 with 7”. Of course, this is a good definition only if we have shown that the number is not algebraic (see Borel 1908. p. 446)[^borel-1908].

Borel, like Poincaré, adheres to a point of view—definability in finitely many words—which is an extension of the algebraic, Kroneckerian point of view: only objects constructible in finitely many steps are proper mathematical objects. However, unlike Poincaré, he disregards the problem of predicative definitions: for him all paradoxes of set theory derive from viewing the proposition that every denumerable set is effectively enumerable (“*Tout ensemble dénombrable est effectivement énumérable*”) as evident, which is false.

#### 3.3.2 Hessenberg, Grelling, Zermelo and Weyl

On the side of mathematical foundations, three chapters of Gerhard Hessenberg’s *Bericht* (1906) on the fundamentals of set theory are devoted to foundational questions. They contain interesting ideas about the philosophy of mathematics, which unfortunately cannot be discussed in detail here. For instance, Hessenberg underlines the distinction between set theoretic definitions which give criteria for *effectively* deciding membership in a given set, and definitions which don’t. Concerning Kronecker’s constructive criticism of the arithmetized continuum, he holds that, although each irrational number determines an infinite fraction and each infinite fraction possesses a formation rule (“Bildungsgesetz”), it is not true that such a rule is given by *explicit finite means.* For otherwise, we could derive (a form of) *the paradox of finite denotation*, i.e., were formation laws to coincide with definable ones, they would be at most denumerable and hence the reals would be denumerable, against Cantor’s theorem.

In dealing with set theoretic contradictions, Hessenberg distinguishes the ‘ultrafinite’ (paragraphs 96–99) from the ‘transfinite’: this latter notion is an exclusive attribute of sets. By contrast, the collections involved in the paradoxes (such as the Russell set, the set of all sets, of all things, and of all ordinal numbers) are ultrafinite.

As to the proposed solutions of the paradoxes, Hessenberg was inspired by a Kantian idea. Just as in the natural sciences antinomies arise if Nature is conceived as a closed whole, similarly the collection $\mathbf{ON}$ and the set of all sets cannot be conceived as completed totalities. Hence the distinction ‘ultrafinite’/‘transfinite’ is apparently in accord with a theoretical approach which is close to Russell’s limitation of size doctrine.

Close to the same philosophical inspiration, the influential paper of Grelling and Nelson (1908) provides an attempt to unify paradoxes and to isolate their underlying structure. The philosopher Leonard Nelson was a prominent figure in the Göttingen of the early twentieth century, who had Hilbert’s strong support (see Peckhaus 1990). The paper is part of a project to develop a philosophically minded “kritische Mathematik”. It contains a new paradox (credited to Grelling) with a semantical flavor (see also the entry self-reference):

> To each word there corresponds a concept, that the very word designates, and which applies to it or does not apply; in the first case, we call the word *autological*, else *heterological*. Now the word ‘heterological’ itself is autological or heterological. Assuming that the word is autological, the concept that it designates applies, hence ‘heterological’ is heterological. But if the word is heterological, the designated concept does not apply, so ‘heterological’ is not heterological.

Zermelo’s axiomatization of set theory (1908; for more details see entries on set theory, the early development of set theory, alternative axiomatic set theories) supplied a sensible tool for blocking contradictions. The main ideas of the axiomatization can be summarized as follows: (i) naïve comprehension is restricted to a separation axiom, i.e., to a principle granting the existence of enough subsets of an already given set of objects (numbers, points, functions on a given space); ‘enough subsets’ here refers to all the subsets specifiable by means of *definite conditions* involving the primitive notions (set equality and membership) and satisfying the laws of classical logic; (ii) there are axioms ensuring that the basic operations of forming singleton, union, pairing, and power set are well defined and that there exist at least an infinite set and the empty set; (iii) extensionality is assumed: two sets are equal if and only if they have the same elements; (iv) an axiom of choice is postulated, which allows selecting a choice set out of any family of disjoint non-empty sets.

It is immediate to see that Burali-Forti’s antinomy cannot be derived in Zermelo’s system, since the collection of all order types does not exist as a set, and Russell’s paradox simply becomes the theorem that there does not exist a universal set.

However, one could raise at least two objections against the theory on different grounds. First of all, Zermelo’s approach is actually *highly impredicative* and impredicativity was regarded as indispensable by him (else one would be forced to reject standard mathematics, e.g., Zermelo believed this was the case even with the Cauchy-Weierstrass proof of the fundamental theorem of algebra). But impredicativity makes the construction of a model or of an interpretation more difficult and less evident. The second point is that Zermelo believed that the paradox of finite denotation (mentioned by Hessenberg) and Richard’s are blocked in set theory, as the separation axiom ought to yield clear criteria for defining sets. But this is not the case, because Zermelo’s notion of definite property (*definite Eigenschaft*) is given informally and is ultimately vague.

The latter issue was taken up in Weyl’s “Habilitation” lecture (1910), where he addressed the general question: when is a relation explicitly definable from a set of given primitive concepts in mathematics? First of all, he considers, as a concrete case study, the problem of characterizing the explicitly definable concepts of elementary plane geometry: these can be inductively generated by means of five basic definition principles from two suitably chosen primitive concepts (e.g., the identity between points =, and the ternary relation $E(a, b, c)$, ‘the distance of point $a$ from point $b$ is the same as the distance of point $a$ from point $c$’).

The five definition principles correspond to a *finite axiomatization of the elementary comprehension principle*, and they imply the existence of exactly those sets (relations), which are definable by formulas in the elementary language comprising two predicate symbols for $=, E$. More explicitly, one requires closure under the logical operations of negation, conjunction, existential quantification and suitable combinatorial operations of permutation and expansion.

In the light of the geometric example, Weyl attacks the concept “defined by means of finitely many words” as not precise, and long before Fraenkel and Skolem, he succeeds in making the separation principle precise: he simply replaces Zermelo’s informal concept of definite property with the notion of ‘relation explicitly definable from extensional equality and membership by means of the basic elementary logical principles’ (we should simply say: first-order definable).

According to Weyl, Richard’s paradox teaches us the following distinction: on the one hand, we are able to characterize only denumerably many subsets of a given set by means of explicit definitions; but, on the other hand, new objects and (possibly uncountable) sets can be introduced by applying the remaining set theoretic operations, like power set or union.

Weyl addressed the problem of generating the admissible properties over a given domain a few years later in *Das Kontinuum* (1918). As in 1910, the set of sets of natural numbers that are definable via admissible operations (to which now also a form of *iteration* is added) is denumerable. By Cantor’s argument there is no relation which parametrizes all subsets of natural numbers (Weyl 1918, section 5)[^weyl-1918]. Weyl apparently followed a relativistic attitude, according to which the extension of the universe of sets and their properties depend on the operations which are accepted to construct sets (see also the entry Hermann Weyl).

It should be stressed that Weyl’s attitude towards Grelling’s antinomy is utterly negative: he considers it pure Scholasticism (Weyl 1918, section 1)[^weyl-1918]: there is no way, according to him, of assigning a meaning to ‘heterological’ and one should ultimately resolve these problems by appealing to philosophy.

It is interesting to observe that, in the light of recent developments, Weyl’s negative verdict ought to be weakened (see section 6).

## 4. Logical developments and paradoxes until 1930

In the period until 1930, the problem of paradoxes led naturally to and was subsumed under the investigation of logical calculi (its final by-product being the Hilbert-Ackermann textbook of 1928**)[^hilbert-1928].** This in turn opened the way to the simplification of type theory, to important generalizations of the notion of set, and to an almost final axiomatic elaboration of set theory (along the Zermelian route, but also following the new path opened up by Johann von Neumann). The basic logical tool is essentially axiomatic formal analysis.

### 4.1 Set Theory and paradoxes: circular sets and other matters

Do circular objects exist in set theory? Zermelo’s view of sets as axiomatized in 1908 did not in itself exclude the possibility of self-membership. The problem was raised anew by Mirimanoff (1917a, 1917b, 1920; see also the entry Zermelo’s axiomatization of set theory). Once circular sets are allowed, *a strengthening of extensional equality by means of a suitable isomorphism relation* (bisimulation, in current terminology) is needed which essentially corresponds to the isomorphism of the trees picturing the given sets. Russell’s argument then suggests a distinction between sets *of first kind*, which are not isomorphic with any of their own elements, and sets *of second kind* which are indeed isomorphic with at least one of their elements. In the light of this distinction, *Russell’s contradiction shows that the collection R of sets of first kind does not exist as a set.* Indeed, a set of second kind always contains a set of second kind; hence a set of sets of first kind must be of first kind. If $R$ were a set, it should be of first kind; but then it could not contain all sets of first kind. Mirimanoff 1917a then introduced the fundamental distinction between *ordinary* (well-founded) and *extraordinary* (non-well-founded) sets: a set $X$ is ordinary if every $\in$-descending chain in $X$ is finite; it is extraordinary, otherwise (there exist infinite $\in$-descending chains). It follows that all sets of the second kind are extraordinary, but the converse is not true (for instance, consider the set $E=\{e_1, E_1\}$, where $E_1 = \{e_1,e_2, E_2 \}$, $E_2 =\{e_1, e_2, e_3, E_3\}$, etc.).

For the history of paradoxes, it is important to emphasize that Mirimanoff 1917a gave a generalization of the Burali-Forti antinomy, *the paradox of grounded sets*. This paradox actually proves that the collection $\mathbf{W}\mathbf{F}$ of ordinary sets (on a given set of atoms) is not itself a set. Indeed, let $\mathbf{W}\mathbf{F}$ be the set of grounded (= ordinary = wellfounded) sets; then $\mathbf{W}\mathbf{F}$ itself is grounded, for were $\mathbf{W}\mathbf{F} \ni x_0 \ni x_1 \ni x_2\ldots$, then $x_0$ would be an ungrounded member of $\mathbf{W}\mathbf{F}$, which is absurd. Hence $\mathbf{W}\mathbf{F} \in \mathbf{W}\mathbf{F}$, so $\mathbf{W}\mathbf{F}$ is ungrounded, contradiction (the same paradox will also appear in Shen-Yuting 1953)[^shen-yuting-1953].

Mirimanoff’s work is also important for the foundations of set theory. He introduced the notion of ordinal rank for ordinary sets and he noticed that ordinary sets can be arranged in a cumulative hierarchy, indexed by their ranks. However, the existence of a cumulative structure of ordinary sets is not considered as a ground for excluding extraordinary sets. Mirimanoff (pp. 212–213) explicitly points to the use of extraordinary sets for modelling *mirror-like situations*. He mentions the case of a book $B$ whose covering is decorated with a picture $J$ representing two children glancing at the same book, i.e. to the picture $J1$ of $B$. In $J_1$ one could perceive again the two children and the picture $J_{11}$ of the book in perspective. Now $J$ can be regarded as a set including as elements the two children $e_1$ and $e_2$, and the picture $J_1$ of $J$, which in turn decomposes into the pictures $e_{11}, e_{22}$ of $e_1$ and $e_2$, and the picture $J_{11}$ of $J_1$, and so on ad infinitum, Now $J$ is isomorphic to one of its elements, i.e. $J_1: J$ can be considered as a set of second kind and hence extraordinary. This non-mathematical example is suggestive of later developments, i.e., the theory of non-well founded sets and its recent applications to semantics. A set $E$ of second kind is also assimilated to an impredicative collection in the sense of Poincaré (Mirimanoff 1920, p. 34)[^mirimanoff-1920] because of its circularity: indeed, $E$ is given by a condition $E=(y, z,\ldots ,a, b, c,\ldots)$, where $y, z,\ldots$ depend on $E$.

On the other hand, in Mirimanoff’s 1917a there is a remarkable use of Burali-Forti’s paradox which suggests a necessary condition for set-hood in terms of size, viz., if a collection is in bijection with the set of all ordinals, then it does not exist as a set. In Mirimanoff 1917a,b, one can also find the idea of von Neumann ordinal (von Neumann 1923, 1925)[^neumann-1925] and a form of the replacement axiom is present.

Von Neumann’s system of 1925 deals with an alternative axiomatic foundation of set theory. There are two sorts of objects: objects of type II (functions, corresponding to classes) and objects of type I (arguments), linked by the application operation of a function to its arguments. The two domains partly overlap and there are objects of type I–II, corresponding to sets (as functions which can also be arguments). The fundamental axiom IV-2 then states that an object $a$ is a proper class (i.e., it is not type I–II) if and only if the totality of its members can be mapped onto the totality of all arguments. The Burali-Forti antinomy shows that the class $\mathbf{ON}$ of all ordinals is not a set, which implies with axiom IV-2 that there is an application of $\mathbf{ON}$ onto the universe of all sets, and hence that *the universe of sets is well-ordered*. Conceptually, the system settles the problem of making Cantor’s distinction between inconsistent and consistent precise and applicable (against Hilbert’s early criticism); it also shows that global choice becomes a theorem on a suitable view of sets. Though circular objects cannot live in von Neumann’s hierarchical model of set theory, they can be found in the investigations of other mathematicians and logicians, e.g., Finsler. According to Finsler, paradoxes hinge upon circular notions, but circularity does not necessarily lead to contradictions. In particular, Finsler regards Cantor’s notion of set as intrinsically circular: sets depend on sets or on general things depending also on sets and *the associated dependence graph* can drive us back in a circle. For the contemporary reader, it is worth mentioning that an original intuition of Finsler 1926b is the *use of graph theory for representing circular structures*. So arrows are used for interpreting membership, and it is not difficult to imagine a set that has itself as unique element and more complicated circular situations (for more on Finsler’s set theory see Holmes 1996 in Other Internet Resources). Finsler 1926 applies Richard’s paradox in order to produce metamathematical results, in particular ‘formally undecidable propositions’. However, Finsler’s arguments are not conclusive and cannot be considered a proper anticipation of the Gödel incompleteness theorems (on the limit of his ideas, see the discussion in van Heijenoort, 438–440); but they show that an attentive reading of the paradox might have unexpected applications.

### 4.2 Type-theoretic developments and the paradoxes

Concerning the subsequent developments in connection with logic, the process of streamlining the tools of logic steadily continued in Göttingen through the work of Hilbert and his school. This is especially clear from his unpublished lecture notes (e.g., those of Winter-Semester course 1917–1918 *Prinzipien der Mathematik*), which are in many respects close to the textbook of Hilbert-Ackermann of 1928 and which contain formulations of first and second order logic, together with ramified type theory and the axiom of reducibility. Paradoxes are derived by allowing a suitable form of unrestricted comprehension; the problematic assumption is located in the admissibility of *predicates and propositions as objects*, i.e., formally in the expressions $X(Y), P(P)$. Variants of the traditional Liar and of the Berry antinomy are introduced. Interestingly, Hilbert sticks essentially to type theory (he does not lecture upon Zermelo’s system); he defines the ramified theory of types with the axiom of reducibility, proving that certain parts of mathematics can be carried out in the system (on Russell’s influence, see Mancosu 2003)[^mancosu-2003].

That type theory and Russell’s work had a central place not only in Hilbert’s Göttingen is further attested to by the work of Chwistek and Ramsey, who attempted a revision of *Principia Mathematica* (PM) from opposite stand-points. Both authors rejected ramified type theory (RTT, in short) and the axiom of reducibility. Their work can be considered a typical outcome of the process that was to yield streamlined versions of logical formalisms. Insofar as paradoxes are concerned, the main problem is to show that RTT is not required for solving the paradoxes.

The solution proposed by Chwistek was prompted by a constructivistic/predicativistic conception. His position in 1921 was that *Principia Mathematica* were not enough to avoid Richard’s classical antinomy. On the other hand, Chwistek proposed a version of the Liar that can be reconstructed in the simple theory of types without the axiom of reducibility, once we are allowed to quantify over all propositions. On his side, Chwistek adhered to a kind of nominalistic position, and tried to develop a theory of constructive types for the foundations of analysis (his attempt of founding mathematics without the axiom of reducibility was called “heroic” in the introduction to the second edition of the *Principia Mathematica*, 1925, see Linsky 2004)[^linsky-2004].

Ramsey 1926 introduced the by-now standard distinction between *logical and epistemological contradictions* (but see already Peano 1906, and section 3.3.1 of this entry)[^peano-1906]. While logical contradictions involve mathematical or logical terms, like class, number, and hence show that our logic or mathematics is problematic, semantical contradictions involve, besides purely logical terms, notions like “thought”, “language”, “symbolism”, which, according to Ramsey, are empirical (not formal) terms. Hence these contradictions are due to faulty ideas about thought or language and they properly belong to “epistemology”.

According to Ramsey, the antinomies of the first group (such as Russell’s, or Burali-Forti’s) can be avoided by referring to a universe of mathematical objects which is structured into types of individuals, functions of individuals, functions of functions of individuals, etc. Quantification over arbitrary types is legitimate and hence types are closed under impredicative comprehension, which is considered necessary for mathematics. Types are intrinsic to logical and mathematical objects and the logical paradoxes are exactly those which require type distinctions to be solved (e.g., self-membership is blocked for objects in the type-theoretic hierarchy). In order to solve the semantical antinomies (e.g., the Liar, Berry’s), Ramsey proposes to distinguish several notions of meaning. In light of later developments, it is interesting to note that for him *semantics is not a viable universal notion*: in particular, it is impossible to obtain “an all-inclusive relation of meaning for propositional functions. Whatever one we take there is still a way of constructing a symbol to mean in a way not included in our relation. The meanings of meaning form an illegitimate totality” (Ramsey 1926, p. 372)[^ramsey-1926]. This yields the clue to the solution of Grelling’s paradox (see 3.3.2). Let $R$ be the meaning relation linking an adjective $f$ to the corresponding propositional function denoted by $F$ (so that $f R F$ holds). In the definition of “heterological” we do use the relation $R: x$ is heterological iff there exists $F$ such that $F$ does not apply to $x$ and $x R F$. Now, there exists a propositional function, say $H$, which is the meaning of the adjective “heterological”. Ramsey’s point is that this sense of meaning cannot be the same as that given by $R$ and this blocks the contradiction, when we apply $H$ to “heterological” (ibid.,p. 370). So one needs a new meaning relation depending on the given fixed $R$. These ideas foreshadow those of Tarski. (For an analysis of semantical antinomies in a ramified context, compare also the later contribution of Church 1976, also reconsidered and criticized in Martino 2001.)[^church-1976][^martino-2001].

## 5. Paradoxes: between metamathematics and type-free foundations (1930–1945)

With the work of Gödel and Tarski, paradoxical arguments were reshaped into fixed point results, while the semantic conception of truth, the formalization of semantics and the arithmetization of syntax yielded firm grounds for systematic metamathematical investigations. In addition, an effort was made to elaborate new grand logics as a reaction to the logic of *Principia Mathematica.* Conceptually, the notions of (self-applicable) function-in-intension/operation and property/ predicate were accepted as primitive, and the very mechanism of definition/combination of concepts was studied. This line of thought gave impulse to the elaboration of syntactical methods within combinatory logic and to the rise of recursion theory. The diagnosis of the paradoxes was further enriched by a subtler analysis of purely logical features of paradoxical reasoning: this is especially true for negation and the crucial role of contraction and duplication properties built into the laws of standard implication. Three valued logic was applied to naïve comprehension.

### 5.1 Paradoxes and diagonalization

The heuristic role of paradoxes is witnessed by Gödel himself, when he intuitively and explicitly relates his construction of formally undecidable sentences to epistemological paradoxes (“the analogy with the Richard antinomy leaps to the eye”, Gödel 1931, van Heijenoort 1967, p. 599)[^gödel-1931][^heijenoort-1967]. However, self-referential constructions attained an adequate degree of mathematical rigor and became genuine mathematical tools only when non trivial number-theoretic techniques were put to work (see the entry recursive functions), for instance in the analysis of syntactical substitution and in providing arithmetical models of formal provability (the crucial role of substitution for producing contradictions was already noticed by Russell, although he did not publish this; see Pelham and Urquhart 1994)[^pelham-1994]. Conceptually, it is clear from Gödelian constructions that self-reference by itself is innocuous if it is understood in the *indirect sense*: one can have formulas $\phi(x)$, expressing properties of their own “name” $\ulcorner \phi \urcorner$, but no dangerous circularity arises.

Gödel’s construction was soon given a general form, as a general diagonalization lemma, which refers to arbitrary definable properties. This is to be found in Carnap 1934b, p. 91, Carnap 1934a, p. 270, and in Rosser 1939, p. 57, Lemma 1:

> For every formula $\psi(v)$ with only $v$ free, there exists a sentence *φ* such that
>
> $$ \phi \leftrightarrow \psi(\ulcorner \phi \urcorner) $$
>
> *is provable* (see also the entry on Gödel’s incompleteness theorems).

As a matter of fact the lemma has become the standard tool for producing self-referential statements and for *transforming the semantical paradoxes into indefinability and (formal) undecidability results* (see the entry on self-reference). The algebra underlying the Gödelian constructions will be grasped only much later during the 1970’s. It is also important to stress that a few years later (1938) an analog of the diagonalization lemma (the so-called second recursion theorem) was discovered by Kleene and was soon to become a basic tool in the foundations of recursion theory and computability theory.

### 5.2 Paradoxes and the foundations of semantics

It is evident from the work done in the twenties surveyed above that the problem of finding a formal solution to the semantical paradoxes, such as the Liar and the Richard paradox, remained essentially open. Type-theoretic solutions had not been pursued to the extent of providing a systematic formal analysis of semantical notions (like truth or definability). But why would this problem be worth studying from a logical and mathematical point of view? As a matter of fact, semantical notions—in particular the notion of definability—were more or less explicitly used in certain parts of set theory (descriptive set theory) and in more “set theoretically inclined” parts of function theory, which were cultivated by Polish mathematics in the twenties. At the same time, the project of a formal methodology and of a scientific semantics was developed by prominent Polish philosophers and logicians working in Lvov (now Lviv) and Warsaw (Lesniewski, Łukasiewicz, Chwistek; see Wolenski 1995 and the entries on Lesniewski, on Łukasiewicz and on the Lvov-Warsaw school)[^wolenski-1995]. For instance, Chwistek attempted an elementary semantics on the ground of a nominalistic foundational program, where sets are identified with propositional functions, extensionality is rejected and the fundamental notion of semantics is the substitution relation “$H$ is the result of the substitution of $G$ for $F$ in $E$” (Chwistek 1933, p. 374)[^chwistek-1933]. In this stimulating environment, Tarski developed his fundamental analysis of semantical paradoxes, first dating back to 1929 and 1930, reported by Łukasiewicz to the Polish Society of Sciences in Warsaw in 1931 and then detailed in the long memoir of 1935 (see the entries on Tarski and on Tarski’s truth definition).

First of all, the analysis of the Liar paradox starts out by specifying a formal requirement to be met in the semantical investigation of truth, i.e. “a materially adequate (*sachlich zutreffende*) definition” of the term “true sentence ” (*wahre Aussage*). This amounts to the celebrated schema (T), which can be roughly stated in simplified form as:

$$\tag{T} x \text{ is a true sentence if and only if } p. $$

where $p$ stands for a sentence and $x$ is a name of $p$ (the idea being in accord to the classical correspondence intuition). The result that Tarski draws from the Liar is that there cannot be any interpreted language which is free from contradictions, obeys the classical laws of logic, and meets the requirements (I)–(III), where

1. the language has names available for all of its sentences;
2. any expression obtained from (T) by substituting $p$ with an arbitrary sentence of the language and $x$ with a corresponding name of $p$ is accepted as true in the language;
3. there exist self-referential sentences, i.e., it is legitimate that a sentence comprises its own name as constituent (so that we can legitimately stipulate that the name $c$ denotes a sentence $\alpha(\ldots c\ldots))$.

Given these essential obstacles, Tarski provides a *structural definition* of the basic semantical notions, i.e., one that relies only on the logical form of an expression and the fact that expressions are recursively defined. But this route is only viable for a language which is structurally described, e.g., a formalized language. For such languages, which are usually closed under quantification and contain formulas with free variables, Tarski elaborates an appropriate *notion of satisfaction*, which allows him to introduce the notions of *definability, denotation, truth, logical consequence.* It is then possible to give a precise version and a proof of the adequacy condition (T) in a meta-science, whose principles comprise: (i) general logical axioms, (ii) special axioms that depend upon the object theory we consider, and (iii) axioms for dealing with the fundamental properties of the structural notions, i.e., *principles of proof and definition by induction*. Given this semantical machinery, Tarski can solve in the negative the problem of the existence of (a formal counterpart of) *a universal language*, i.e., one where it is possible to define an adequate notion of truth for the same language. Although the theory of simple types, (where the type 0 is the type of individuals; the type $n+1$ is the collection of all classes of type $n$ objects) with the axiom of infinity and extensionality is apparently a good candidate as a general metatheory, it is shown that whichever definition we choose in the theory of types for the term “true”, then it is possible to deduce in the same theory the negation of some instance of the adequacy schema (T). In the proof of this theorem, Tarski applies arithmetization and diagonalization, hence following the Gödelian pattern. On the positive side, the concept of truth can be adequately defined for any formalized language L in a language (the so-called metalanguage), provided it is of higher order than L. Also, Tarski’s semantics makes precise Gödel’s remark (1931, footnote 48) that “the true reason of the incompleteness is that the formation of ever higher types can be continued into the transfinite[…], while in any formal system at most denumerably many of them are available”. Tarskian semantical notions play the role of the higher types hinted at by Gödel. To sum up, the outcome of Tarski’s work is that the semantical notions are eliminated in favor of the (extensional) notions of type or set, and a theoretical explanation of semantical paradoxes is finally achieved.

### 5.3 “The inconsistency of certain formal logics”

In the twenties and in the early thirties, the orthodox view of logic among mathematical logicians was more or less type- or set theoretic. However, there was an effort to develop new grand logics as substitutes for the logic of *Principia Mathematica*. These frameworks arose both as attempts to recover the simplicity of the type-free approach, as derived from the so-called naive comprehension principle, as well as in order to satisfy metamathematical needs, such as the clarification of fundamental concepts underlying the notions of “formal system,” “formalism,” “rule,” etc. In particular, Church and Curry proposed theories which (i) assume as primitive the notions of self-applicable function-in-intension (operation), and (ii) stress the very mechanism of definition/combination of concepts. If one looks closely at the development of these systems, one can see *that paradoxical constructions have become essential tools for defining objects and proving non-trivial logical mathematical facts.* Following ideas of Schönfinkel and aiming at a mathematical analysis of the substitution process, Curry’s 1930 thesis introduced a formal language based on basic general operators, the so-called *combinators* $B$ (composition), $C$ (permutation), $W$ (duplication), $K$ (cancellation), $Q$ (equality), and logical constants like the universal quantifier and implication. Expressions are then inductively generated by application from constants; intuitively, a term $M$ stands for a function, and the applicative term $MN$ (juxtaposition plays the role of application and parentheses are associated to the left) denotes the value of the term obtained by replacing the first variable of $M$ with $N$. Self-application $MM$ is admissible and this feature tells us that *the objects of combinatory logic cannot be simply interpreted as set-theoretic functions*. The formal system consists of standard equations on combinators (e.g, $Bxyz=x(yz), Wxy=xyy$, or $Cxyz=xzy)$, rules for equality and the logical constants; its main goal is to derive equalities $X=Y$ and to make assertions of the form $\vdash X (= X$ is provable). Combinatory logic is a theory which analyzes the modes of combinations of formal objects, substitution, and the notions of proposition and propositional function (see the entry on combinatory logic for a proper introduction to variants of the formalism and an overview of the properties of related calculi). For Curry, the root of the paradoxes is found in assuming that *combinations of concepts are always propositions*. The notion of proposition becomes a *theoretical concept*, which is decided by the theory. Types are not assigned to the expressions of the formal system at the outset, but are instead inferred by means of the system itself, which has a dual nature: it can derive identities, but also truths. In particular, if $\vdash MN$ is derived, this can be read as “$N$ is of type $M$” or “$N$ is an element of $M$”. These ideas foreshadow fundamental developments such as the so-called *formulas-as types interpretation* (see Howard 1968).

Church’s formalism—originally introduced in Church 1932, 1933 as a set of postulates for the foundation of formal logic—includes conversion (i.e., computational) rules, which allow the replacement of terms with intensionally equivalent ones, and rules for asserting certain terms as “true”. The syntax yields a general notation system for functions, based on an applicative language, where there is one basic category of terms (well-formed formulas in his terminology). Some terms are formally provable (or assertable) and are classified as true. Terms are inductively defined from a set of basic constants and variables by means of application and the characteristic *lambda abstraction operator*: if $M$ is a term containing the variable $x, \lambda x.M$ is a term, naming the function defined by $M$. The basic constants designate logical operations: (a kind of restricted) formal implication; existential quantifier, conjunction, negation, description operation, and generalized abstraction (i.e., if $F$ is formal logical equivalence, $A(F, M)$ is “what $M$ has in common with any $N$ formally equivalent to $M$”). It turns out that Church’s logic can interpret naive class theory and hence the system is suspiciously strong and expressive (strength and expressivity are inherited by the formalism which was devised out of Church’s: see the entry on the lambda calculus). Church’s hope was that contradictions could be avoided by ensuring the possibility that a propositional function be *undefined* for some argument.

However, the theories of Curry and Church were almost immediately shown inconsistent in 1934, by Kleene and Rosser, who (essentially) proved a version of the Richard paradox (both systems can *provably enumerate* their own provably total definable number theoretic functions). The result was triggered by Church himself in 1934, when he used the Richard paradox to prove a kind of incompleteness theorem (with respect to statements asserting the totality of number theoretic functions).

The reason for the inconsistencies was eventually clarified by Curry’s 1941 essay. There he distinguishes two basic completeness notions: a system $S$ is *deductively complete*, if, whenever it derives a proposition $B$ from the hypothesis $A$, then it also derives the implication $A \rightarrow B$ (deduction theorem or introduction rule for implication); $S$ is *combinatorially complete* (Curry 1941, p. 455.)[^curry-1941] if, whenever $M$ is a term of the system possibly containing an indeterminate $x$, there exists a term (Church’s $\lambda x.M)$ naming the function of $x$ defined by $M$. Curry then remarks that the paradox of Kleene-Rosser arises because Church’s and Curry’s systems satisfy both kinds of completeness, thus showing that *the two properties are incompatible*. In the more technical part of the paper, Curry carefully axiomatizes the main ingredients exploited by Kleene and Rosser and carries out a lot of non-trivial work both on the logical side and the mathematical side (e.g, to develop a portion of recursive arithmetic, to define the existence of an enumerator, i.e., a term $T$ such that, if $a$ is the Gödel number of a closed term $M$ and $Z_a$ is the term formally representing $a$, then $TZ_a =M$ is provable in $S$, etc.). Curry’s proof of the inconsistencies of combinatory systems is unsatisfactory because it heavily uses a detour through number theory and Gödelization, which, as a matter of fact, is unnecessary as Curry himself soon discovered and presented in a paper with the same title as the one by Kleene and Rosser, “in deference to the original discoverers of the contradiction” (Curry 1942)[^curry-1942]. The main result in it is the following theorem (Curry’s paradox, see the entry Curry’s Paradox):

1. assume that we have a combinatorially complete system, i.e., essentially a system of combinatory logic which contains the standard properties of equality and the basic axioms ensuring the definability of Church’s lambda with the corresponding axioms defining $B, C, I, W$;
2. assume also that the system contains an implication operator $\supset$ satisfying, for arbitrary terms $M, N$ $$\begin{align*} & \vdash M \supset M \\ & \vdash M \supset( M\supset N) \Rightarrow \vdash M \supset N \\ & \vdash M \text{ and } \vdash M\supset N\Rightarrow \vdash N. \\ & \text{Then } S \vdash M, \text{ for every term } M. \end{align*}$$

For the proof, it is enough to find, for any given term B, a term A such that $A=A\supset B$. Curry notes that a twofold construction is possible. By direct self-reference, we can choose: $A = HH$, where $H=\lambda Y (N(YY))$ and $N = \lambda X (X\supset B)$. On the other hand, one can apply indirect self-reference and exploit the machinery of Curry 1941 and Kleene-Rosser: using an enumerator $T$, one sets $U = \lambda X (TXX \supset B)$ and $A=UZ_u$, being $u$ the Gödel number of $U$. Curry suggests that these two routes are akin, respectively, to Russell’s paradox and to the Liar. It is interesting to note that the two ways correspond to by-now standard tools, the so-called *first fixed point theorem* and *second fixed point theorem* of combinatory logic and lambda calculus (Barendregt 1984, p. 131 and p. 143; see also the distinction between the first recursion theorem and the second recursion theorem of classical recursion theory, in this SEP, entry recursive functions)[^barendregt-1984].

Curry’s analysis of the solutions to the paradox would lead us into the realm of the theory of functionality, the history of combinatory logic and proof theory. Here it is enough to recall that according to him, a remedy would be to formulate within the system the very notion of proposition, and a way to avoid the contradictions would lead to a hierarchy of canonical propositions (or to a theory of levels of implication, already adumbrated by Church). Related ideas have been developed since the seventies by Scott 1975, Aczel 1980, Flagg and Myhill 1987, and others.

### 5.4 Criticizing standard implication and negation

In the 1930s, an alternative route to solve the antinomies emerged. This approach exploits the duplication (contraction) combinator $W$ which satisfies $Wfx=fxx$; if $N$ represents negation and $Babc=a(bc)$, then $W(BN)(W(BN))$ is a fixed point of negation, and it is a functional analogue of the Russell class. On the logical level, assigning a type to $W$ leads to the essential inference applied in the derivation of Curry’s paradox, i.e., the contraction rule $A\rightarrow(A\rightarrow B) \Rightarrow(A\rightarrow B)$. The role of contraction was noticed by Fitch 1936, who observed that, in order to derive the Russell paradox one considers a function of two variables, then one diagonalizes and regards such an object as a new unary propositional function. But this step only works if $W$ is accepted. Fitch then proposed a “non-contractive” logic, but his paper did not go beyond a brief sketch of a fragment of classical logic with predicates. One has to wait until the mid eighties to see contraction-free logics used systematically in proof theory and in theoretical computer science (see the entry linear logic).

Fitch 1942 proposed a new approach to the problem of finding consistent combinatory logic systems, which were progressively expanded and refined over many years (until 1980). Fitch’s method to avoid paradoxes consists of *the construction of suitable syntactical models, endowed with self-referential notions of class, membership and truth.* Truth and membership are inductively generated by iterating rules that correspond to natural logical closure conditions and can be formalized by means of *positive* (i.e. negation- and implication-free) clauses. This fact implies that the generation process is cumulative and becomes saturated at a certain point, thus yielding consistent non-trivial interpretations for truth and membership. Mathematically, a collection of positive clauses always gives rise to an operator, say $G$, mapping sets of expressions into sets of expressions and preserving the inclusion relation (i.e., monotone); the saturated sets then correspond to fixed points of the monotone operator $G$ (i.e., to sets $X$ satisfying $G(X)=X)$, which exist according to a classical theorem about complete lattices (see Birkhoff 1967)[^birkhoff-1967].

In the early 1940s, Fitch explored a purely positive (negationless) combinatory system $K$ with the explicit aim of defining a sort of *universal formal system*, where *every system of logic* could be represented. Later he was able to strengthen his approach to include forms of negation and implication, insofar as he provided *a simultaneous generation of truth and falsehood*, and this actually amounts to conceive truth as a *partial predicate*. Fitch’s approach is radically intensional: classes are always classes of expressions $M$ in some language (say, of the basic logic) and they are identified with attributes, while membership is essentially reduced to truth in the sense of $K$. Thus, that $M\in T$ holds, essentially means that $M$ truly falls under the property specified (or expressed) by $T$ (see also the entry on combinatory logic). Logical systems, along similar lines, were also proposed and proved consistent via proof theoretic methods by Schütte in the early fifties (see Schütte 1960 for a comprehensive treatment)[^schütte-1960].

To a certain extent, the ideas of Fitch can be regarded as introducing the view that the basic predicates of truth and membership have to be *partial* or, if you like, *three-valued*. Bochvar (1937)[^bochvar-1937] outlines a proposal based on the introduction of a three-valued logic, where, besides the standard truth values T (truth) and F (false), there exists a third value N, to be interpreted as “meaningless”. His logical analysis leads to the conclusion that the paradoxes involve meaningless statements. A characteristic feature of Bochvar’s formalism is that it distinguishes two types of connectives, roughly corresponding to two different modes of assertion. A statement $A$ in itself assumes exactly one among the prescribed values (true, false or meaningless); but the *internal* three-valued logical operations are also equipped with *external* logical operations, which correspond to statements on the metalevel and allow the use of classical logic in dealing with non-classical statements. Formally, he described three valued truth tables for the main propositional internal connectives & (and), $\sim$ (negation), $\vee$ (or), $\rightarrow$ (implication), $\leftrightarrow$ (logical equivalence). The truth values of $\sim A, A \amp B$, etc., coincide with their classical values if $A, B$ assume classical values; they are meaningless (assume value N) if one among $A, B$ has value N (strictness). No formula built up with the standard connectives can be valid (or a tautology, i.e., is true under all possible assignments), as $A \rightarrow A$ has value N, if $A$ is meaningless. But there are connectives allowing the formation of *metatheorical statements* such as $\vdash A, \neg A, \downarrow A$, to be read as “$A$ is true”, “$A$ is false”, “A is meaningless” (in the given order). The value of $\vdash A (\neg A)$ is true if $A$ is true (false), false (true) otherwise. Bochvar describes a version of the extended type-free logical calculus of Hilbert-Ackermann (1928), and, in order to dispose of the paradoxes, he restricts substitution and hence the comprehension schema of the form

$\exists F\forall x(F(x) \leftrightarrow \phi)$, where *φ* is any formula in which $F$ is not free and which may or may not have $x$ free.

to conditions *φ* with only *internal* logical operations. Apparently, Bochvar’s solution is not simply a *gap solution*, where the logic is weakened; instead, he formalizes the distinction between object *level* and *metalevel* in the logic itself. This makes his theory quite expressive (e.g., it can handle the very notion of “non-sensical”, “meaningless”).

### 5.5 Non-terminating processes, cycles and typical ambiguity

Behmann’s paper 1931 (presented in 1929) locates the source of the paradoxes in the definitional machinery. The paper begins with an analysis of Russell’s contradiction in the form of predicate application. There he observes that, once the Russell predicate $F$ is defined by the stipulation

$$ F(\phi) =_{df} \neg \phi(\phi), $$

it must be possible to eliminate $F$ from any argument involving it. But, if we try to replace $F$ by its definiens, we obtain $F(F) \equiv \neg F(F)$, and we are trapped in an infinite regress, as there is no $F$-free expression that could replace $F(F)$. So the contradiction is ascribed to an error in the theory of definitions, namely to the use of definitions that give rise to an infinite chain of substitutions, without converging to a result. Behmann’s technical proposal consists in a reformed logic without types but with an added operator ! which, when given a predicate *χ*, singles out exactly those arguments $x$ to which *χ* meaningfully applies. For instance, the syllogism Barbara, usually stated in the form

$$ (\forall x)(A(x) \rightarrow B(x)) \amp(\forall x)(B(x) \rightarrow C(x)) \rightarrow(\forall x)(A(x) \rightarrow C(x)), $$

is corrected to

$$\begin{align} (\forall x)(A(x) \rightarrow B(x)&) \amp (\forall x)(B(x) \rightarrow C(x)) \\ &\rightarrow (\forall x)(C(x))! \rightarrow (A(x) \rightarrow C(x))), \end{align}$$

where the range of the final quantifier is restricted to those $x$ for which it does make sense. Behmann did not develop a systematic theory until much later and it is unclear how to interpret his special operator $!$. Nevertheless, his work has inspired work by Aczel and Feferman (1980).

Lewis and Langford (1932) are led to conclusions which are not dissimilar to those of Behmann. According to them, the paradoxes show that certain expressions *do not express propositions*. They adopt the notation $p : \alpha$ to mean that $p$ is a name whose meaning is the proposition *α* (so $p$ and “*α*” denote the same entity and can replace each other); typically the Liar amounts to “$p: p$ is false”, but we can also imagine more complex self-referential situations, for instance:

$$\begin{align*} \tag{\(p_1\)} &p_2 \text{ is false}; \\ \tag{\(p_2\)} &p_1 \text{ is false}. \end{align*}$$

In this case, there is no contradiction, but we become entangled in a vicious regress (p. 440), and hence *no proposition* arises. In general, one can create arbitrary complicated cycles and check that they can lead either to contradictions or to infinite regress; but in either case, the expression fails to converge to a definite proposition.

Even after the logics developed by Russell, Zermelo and Tarski had created the theoretical means to get rid of difficulties involved in the notions of class, set, truth, definability, the paradoxes have remained alive. This probably is due to a persistent interest in alternative formal paradigms, to the controversial features and axioms of *Principia Mathematica*, and to the problematic place that self-reference occupies in mathematical logic. In this context, it is worth mentioning Quine’s paper of 1937 on the system NF (see the entry Quine’s New Foundations), which takes inspiration from the Russellian notion of *typical ambiguity*, that is, from the systematic device of suppressing the order indices of propositional functions and their arguments, leaving them to be restored at will, when needed, according to the discipline of type theory (see 3.2 above). The idea is to restrict naive comprehension to those instances that are *stratified*, where in general a formula *φ* is *stratified* iff it is possible to assign a natural number (type in short) to each term occurrence in such a way that the resulting formula is well-formed in the sense of type theory, e.g., if $t \in$ s is a subformula of *φ*, the type of $s$ is one greater than the type of $t$, etc.. Clearly, stratification blocks set formation when formulas of the form $x\in x, \neg x\in x$ are present. Moreover, in NF the universal set exists. The consistency problem for NF is still open (though partial results are known concerning fragments with bounds on stratification or restriction to extensionality). Remarkably, NF refutes the axiom of choice by a classical theorem of Specker. Again, a classical result of Specker establishes the existence of a model of NF in a suitable version of simple type theory with a formal counterpart of typical ambiguity. Paradoxes are not that far from NF. In 1942 Rosser (and independently Lyndon) published a form of Burali-Forti’s antinomy in a seemingly natural extension (named ML) of the system NF, obtained by adding “ultimate classes”. ML was defined to avoid certain weaknesses of NF (e.g., with respect to number theoretic induction). Once more, the Lyndon-Rosser result brought about the unexpected presence of a paradox in set theory and the foundations of mathematical logic.

## 6. A glance at present-day investigations

### 6.1 From paradoxes to theorems

As noticed many years ago by Kreisel and quite aptly recalled by Dean 2020, p. 541, the right question to deal with is not how *to get rid of paradoxes* or to solve them: instead, the *fruitful* problem is *to get something out of them*. Indeed, paradoxes can be converted into plain undecidability/undefinability theorems, and this is the consequence of a systematic methodology: with the work of Gödel and Tarski, paradoxical arguments are reshaped into fixed point results, while the semantic conception of truth gives rise *to a formalization of semantics itself*, yielding firm grounds for systematic metamathematical investigations, as can be seen from several early contributions by a number of logicians, e.g. Kreisel 1950, Wang 1955. For instance, arithmetizing semantics yields a refinement of the completeness theorem, the so-called *arithmetized completeness theorem* ART: every recursive consistent theory has a model in which the function symbols are replaced by primitive recursive functions and the predicate symbols are replaced by predicates which are definable *with just 2 quantifiers* in a version of formal number theory (cf. Hilbert and Bernays 1939, p. 293 and Feferman 1960)[^feferman-1960]. By adding an arithmetic sentence Con(S) expressing the consistency of a *set* theory S as a new axiom to elementary number theory, one can prove in the resulting system *arithmetic translations* of all theorems of S. A by-product of this metamathematical formalization is a *de facto* unification of set theoretic and semantic theoretic paradoxes, in the sense that paradoxes of either sort become tools for proving incompleteness and undecidability. Typically, a given paradoxical notion is formalized as a predicate in a language of a theory interpreting (at least a fragment of) number theory Z; one then applies diagonalization, self-reference, etc., in order to get statements which correspond to number theoretic sentences that becomes undecidable or unprovable given a consistency assumption.

### 6.2 Foundational frameworks and paradoxes

Philosophical motivations are strongly influential in contemporary logical investigation of paradoxes and hence it is natural to wonder what is surviving of the initial Fregean theory of concepts, as based upon an inconsistent principle of abstraction and the logicistic outlook. Well, the answer is that a non-trivial legacy is still alive: this is especially clear from the Neo-Fregean approach based on Hume’s principle and variations thereof. Consistent subsystems of Frege’s Grundgesetze have been isolated and are currently studied: see Burgess 2005, also for a comprehensive reference list to preceding work by Boolos, Wright and Hale, Heck, Wehmeier, Ferreira, Antonelli and May (see the essays contained in Reck and Cook 2016, and also the entry logicism and neologicism)[^reck-2016]. In addition, work in the Neo-Fregean tradition has shown that the inconsistency of the principle of extensional abstraction (Basic Law V) in Grundgesetze is only an instance of a more general result on the inconsistency in second order logic (extended with a symbol for a function f from concepts to objects) of any abstraction principles that satisfy a condition called “part-whole”: if A is strictly included in B then f(A)≠f(B) (see Mancosu and Siskind 2019).

On the other hand, once we set apart the ideological inspiration of logicism, we might believe that the development of logic and set theory in the 20th century has fully sterilized paradoxes, and that contradictions in logical systems are phenomena of the years of foundational crisis only. But this is not true: paradoxes have been discovered in logical systems related to computer science. For instance, half a century ago, Girard showed that a constructive theory of types, due to Per Martin-Löf 1971, and based on the Curry-Howard correspondence, is inconsistent with the existence of a type of all types; the contradiction follows by means of a type-theoretic reconstruction of an argument related to the Burali-Forti antinomy and the Mirimanoff paradox of grounded sets. Later, Coquand 1986 proved that certain extensions of the calculus C of constructions are inconsistent. Very roughly, C is a higher order impredicative type theory, extending Girard’s system F, a powerful second-order typed lambda calculus with abstraction on types which is suitable for representing proofs of impredicative intuitionistic second-order logic. Coquand 1994 offered a new paradox affecting type theory, which refines Reynold’s result that there is no classical set-theoretic model of polymorphism (read: Girard’s system F, see the entries type theory, set theory: constructive and intuitionistic ZF). On the other side, a general type-free development of the theory of constructions as a foundation for constructive provability in logic and mathematics was originally proposed by Kreisel and Goodman, but it turned out to be affected by an antinomy, which has been recently reconsidered by Dean and Kurokawa 2016.

On the borderline between foundational issues and applications in computer science, arguments with typical paradoxical flavor occur in the investigation of Feferman’s *explicit mathematics* (EM), a theory of (self-applicable) operations and non-extensional classifications. For instance, the existence of a strong power type construction leads to inconsistency in the so-called “theories of types and names”, a development of EM introduced by Jäger 1997 (see the Other Internet Resources section for a link to a comprehensive bibliography on EM from 1975–2013; and for more recent results connected with EM, see Hayashi 2025)[^hayashi-2025]. Paradoxical arguments are also useful for assessing the role of universes and *refuting non-extensionality* in EM, in presence of forms of *uniform* naïve comprehension (see Cantini and Minari 1999)[^cantini-1999]. Indeed, the role of uniformity is essential in previous investigations. Concerning naïve comprehension, it is known since the seventies (Malitz 1976)[^malitz-1976] and the eighties (Weydert 1988, Forti and Hinnion 1989)[^forti-1989][^weydert-1988] that there exist nice topological models of *extensionality* and *non-uniform* naïve comprehension restricted to *generalized positivity conditions*. This has led to the study of so-called *hyperuniverses*. Additional consistency/inconsistency results about the relationship between extensionality and uniform vs. non-uniform comprehension principles can be found, e.g., in Hinnion and Libert 2003, Libert and Esser 2005. In a similar direction, recent theoretical proposals combine anew ideas from combinatory logic and lambda calculus with “inductive” reinterpretations of naïve comprehension and unrestricted truth schema, along a path already opened by Fitch in the late forties (see Scott 1975, Flagg and Myhill 1987, Aczel 1980, and Feferman 1984)[^aczel-1980][^feferman-1984][^flagg-1987][^scott-1975]. Beginning with 1992, there was an attempt, due to K. Grue, to resurrect Church’s lambda calculus as a foundation of mathematics. Grue 2002 presents a very strong extension of lambda calculus, the so-called *map theory*, in which standard axiomatic set theory becomes interpretable, and which can be used to shed light on the difference between Russell’s and Burali-Forti’s paradoxes.

### 6.3 Circularity and self-reference

Since Mirimanoff, Finsler and others, logicians have studied universes of set theory where circular sets exist. However, it is only since the early Eighties that a genuine mathematics of non-well-founded sets (see | set theory: non-wellfounded) is being developed. Using the axiom AFA of anti-foundation, direct self-reference is allowed in set theory, and there exist plenty of sets solving general self-referential equations (AFA was introduced by Forti and Honsell in 1983; for systematic development and history, see Aczel 1988)[^aczel-1988][^forti-1983]. In particular, non-wellfounded sets are applied to the analysis of the paradoxes, to the semantics of natural languages and to theoretical computer science (see Barwise and Etchemendy 1984, Barwise and Moss 1996)[^barwise-1984][^barwise-1996].

Concerning the issue whether self-reference can be avoided in deriving paradoxes, and hence whether there are genuine contradictions arising from ungroundedness, a positive answer has been given by the semantical paradox of Yablo 1993: there are infinitely many agents , etc., each one claiming the same sentence: “at least one agent following me is lying”; but this yields a contradiction – see also the entries on self-reference and liar paradox. The issue this construction raises, namely whether circularity and self-reference are necessary and sufficient conditions to the appearance of paradoxes, has been further considered in Yablo 2006 (see Cook 2014 for a comprehensive study on this matter, and Halbach and Zhang 2017 for a proof without diagonal lemma)[^cook-2014][^halbach-2017]. Moreover, the connection between the incompleteness phenomena and paradoxes has been extended up to include Yablo’s paradox, as a special case of Liar-type paradoxes (Kurahashi 2014, Kikuchi and Kurahashi 2016)[^kikuchi-2016][^kurahashi-2014].

The analysis of self-reference and diagonalization has motivated the application of algebraic and topological techniques: consider Scott’s models for extensional lambda calculus (Scott 1972)[^scott-1972] and their subsequent categorical understanding. On the other hand, category theory has been used for new approaches to paradoxes since Lawvere 1969. A mathematical approach to the general issue of “self-reference vs. unfoundedness” can be found in Bernardi 2001, 2009. Besides Yablo’s paradox and a game theoretic version of Mirimanoff’s paradox, several classical results (existence of a non-r.e. set, Cantor’s theorems on the nondenumerability of the reals) can be transformed into existence theorems for suitable unfounded chains (and formally, unfounded chains are regarded as generalized fixed points).

### 6.4 From paradoxes to incompleteness

In standard metamathematics, an important role for a thorough understanding of the second incompleteness theorem is played by *Löb’s theorem* (Löb 1955)[^löb-1955]. The proof of the theorem is related to *Curry’s paradox* (see this entry, and Curry’s Paradox) and to an informal argument due to Geach 1955. Furthermore, Löb’s theorem is essential for defining mathematical structures, which are adequate for providing versions of self-reference and incompleteness (see the so-called *Magari algebras* and the modal analysis of formal provability, Boolos 1993)[^boolos-1993]. In the same direction, there are applications of *Berry’s paradox*. For instance, in 1966 Vopenka proved the second incompleteness theorem for the Bernays-Gödel theory of sets and classes using a form of the same paradox. Boolos 1989 exploits a Berry-type argument to prove incompleteness in the form “*there is no algorithm whose output contains all true statements of arithmetic and no false ones*” without appealing to diagonalization. The Berry paradox has been related to the incompleteness phenomena also because of work (going back to the sixties and the seventies) in the so-called Kolmogorov complexity and *algorithmic information theory*. In particular, Chaitin has shown in a number of papers how to exploit randomness to prove certain limitations of formal systems (see Chaitin 1995)[^chaitin-1995]. In connection with Chaitin’s results, Kritchman and Raz 2011 gives a proof of the second incompleteness theorem, which is based on an argument resembling the *surprise-test paradox* (see epistemic paradoxes). In turn, this paradox can be explicitly related to Solovay’s completeness theorem of *provability logic* (see Montagna 1994)[^montagna-1994], and more recently Egré 2005, De Voos, Kooj and Verbrugge 2018 applied provability logic to solving *the Knower’s paradox*. It is worth recalling that – again on the side of epistemic logic – self-reference is applicable in order to prove *incompleteness in belief models*. Brandenburger and Keisler (2006) identified a paradox of self-reference in beliefs in games, which yields a *game-theoretic impossibility* theorem akin to Russell’s Paradox. An informal version of the paradox is that the following configuration of beliefs is impossible: Ann believes that Bob assumes that Ann believes that Bob’s assumption is wrong. This is formalized to show that any belief model of a certain kind must have a ’hole’. An interpretation of the result is that “if the analyst’s tools are available to the players in a game, *then there are statements that the players can think about but cannot assume*.” Also, the mere fact of paradoxes like this one, with a distinct logical “flavour”, but arising out of treatments involving epistemic notions, is notable, as it can be regarded as an indication for a direction of work that, hinging upon the many examples already available in the literature, is likely to expand and become systematic in the future thanks to the application of formal methods (see also this entry, §6.5 on this). Although not directly connected with the incompleteness phenomenon, there are indeed several accounts of antinomies affecting what appear to be sets of apparently legitimate, natural postulates involving certain epistemic notions. Let Leitgeb 2021 work as an ultimate example of sources of this sort, presenting a solution to the lottery paradox (see Kyburg 1961 and epistemic paradoxes)[^kyburg-1961] that affects principles relating categorical belief to graded belief (see also Douven 2021 that contains the former source)[^douven-2021].

### 6.5 On the foundations of semantics, again

In the final quarter of the last century a host of logical papers arise from the discussion of the foundations of semantics, with a number of proposals which generalize or modify Tarski’s semantical conception of truth. Tarski notwithstanding, since 1975 the hierarchical approach has been somewhat superseded by new ideas that have rendered the ideal of logical and semantical closure in many respect accessible (especially by means of the fixed point methods used by Kripke 1975 and Martin-Woodruff; see Martin 1984)[^kripke-1975][^martin-1984]. We also mention the approach stemming from Herzberger, Gupta and Belnap 1993 (see the entry revision theory of truth), that has connections with non-elementary parts of definability theory, set theory and higher recursion theory (Welch 2001, 2009, 2011, 2019)[^welch-2001][^welch-2009][^welch-2011][^welch-2019]. This has led to the general axiomatic study of *revision-theoretic definitions* and theories of *circular definitions* (see Bruni 2009, 2013b, 2015, 2019)[^bruni-2009][^bruni-2013b][^bruni-2015][^bruni-2019]. In Standefer 2015 a connection is established between Solovay type theorem and circular definitions of revision theory and a particular modal logic RT (revision theory): a completeness theorem for this logic, analogous to Solovay’s completeness theorem for GL, is proven. The modal logic in question is built upon an operator that is naturally connected with revision-theoretic construction (hence, the name), as explained in Gupta and Standefer 2017. The proof theory of this system is studied in Standefer 2018.

Recent advances on revision theory, have contributed to prove the fertility of the approach (in a direction related to the last part of §6.4 of this entry): Gupta 2011 presents an application to the concept of strategic rationality in a certain type of finite games that is connected to a common way of understanding rational choice in strategic contexts. Although developed independently, Gupta’s stance is reminiscent of previous work by H. Gaifman about rationality being affected by paradoxes resembling the truth theoretic paradoxes like the liar paradox (see Gaifman 1999)[^gaifman-1999]. An extension of this approach to the class of all finite games is presented in Bruni and Sillari 2018. The notable aspect of Gupta’s application is that it makes use of only the finite part of revision theory (i.e., it does not need the transfinite iteration of this construction), and it gets rid of the rule for dealing with stages corresponding to limit ordinals. This limit rule, which is essential to address the concept of truth, turned out to be the most critical aspect of the revision-theoretic approach to circular concepts from both the complexity, and the conceptual point of view (see Campbell-Moore 2019 for a recent, new approach to the topic)[^campbell-moore-2019][^campbell-moore-2019-2].

The wealth and variety of semantical tools has triggered a sort of experimenting with a number of *mixed* proposals. Refinements of revision theory and generalizations thereof can be found in Rivello 2019a e 2019b where a new approach to a formal theory of truth is developed, which implements features of Kripke’s fixed point theory with the Herzberger-Gupta revision theory. An analogous combination, studied from a more proof-theoretic angle, was considered in Standefer 2017. Similarly, combinations of the possible worlds semantics for the necessity predicate with Kripke’s supervaluational partial models for the truth predicate are also studied by Nicolai 2018 (see also Dopico and Hayashi 2024 [Other Internet Resources] for a recent attempt of completing the picture of axiomatic theories of supervualational truth, which builds over Cantini 1990)[^cantini-1990].

Field (2003, 2008)[^field-2003][^field-2008] has proposed influential solutions of the semantical paradoxes which combine Kripkean and revision theoretic techniques. According to him, the present solutions to the paradoxes are not satisfactory because of the following points: (i) the lack of a decent conditional (and biconditional); (ii) the failure of (some instances of) the T-schema, $\rmA \leftrightarrow \rmT(\ulcorner \rmA\urcorner)$; (iii) the failure of intersubstitutivity between A and T(⌈A⌉); (iv) the impossibility of providing an internal analysis of the defectiveness of the paradoxical sentences. Field (2008)[^field-2008] has consequently developed a theory of truth with *a non-classical conditional operator*, which allows to express a notion of *determinate truth* and to state that the Liar is not determinately true. Analysis of Field’s construction requires sophisticated *set-theoretic and recursion theoretic developments* (see Welch 2008, 2009, 2011)[^welch-2008][^welch-2009][^welch-2011]. Moreover, the possibility of logically enriching Kripke’s theory of truth with *novel conditionals* has opened up new routes: e.g. Rossi (2016)[^rossi-2016] provides an interesting method of incorporating a conditional conforming to Łukasiewicz three-valued logic in a fixed-point construction for truth. In the same direction, a considerable attention has been directed in recent literature to the so called *revenge problem*: typical solutions, say, of the Liar paradox, rely on notions that, if expressible in the object language, give rise to new versions of the paradox. So, the solution is only an illusion. The revenge problem can be instantiated by the so-called Strengthened Liar: informally, once we have a model which makes *the Liar sentence L* itself neither true nor false, and we can express this very fact, L is after all not true. But this is the claim made by L, and hence L is true. So the paradox seems to show up again (for more details, see the entry liar paradox and the collection of essays contained in Beall 2007)[^beall-2007].

“Indexical” solutions of the Liar have been developed in several contributions, e.g., by Burge, Gaifman, Simmons. The idea is that the Liar paradox does not involve sentences, but *specific occurrences of sentences*, i.e., sentence tokens (this idea is to be found already in scholastic solutions). For the sake of historical accuracy, let us mention that in 1913 Lesniewski, later Tarski’s dissertation advisor, had already advanced an indexical nominalistically inspired solution of the Liar in his paper *A Critique of the Logical Principle of the Excluded Middle* (see Betti 2004)[^betti-2004].

Besides the model-theoretic side, *axiomatic investigations of truth* and related paradoxes have become increasingly important since the seminal papers of Friedman and Sheard 1987, Feferman 1991. Since the year 2000, this research thread has been intensively studied with various aims, from *proof-theoretic analysis* to philosophical discussion of *minimalism* (for a survey of the varieties of truth theoretic systems and appropriate references, see the entry on axiomatic theories of truth and the recent monographs of Halbach 2011, Horsten 2011; see also the papers Feferman 2008, Fujimoto 2010, Leigh and Rathjen 2010)[^feferman-2008][^fujimoto-2010][^halbach-2011][^horsten-2011][^leigh-2010].

Last but not least, the axiomatic study of epistemic notions has greatly benefited from application of techniques used for proving incompleteness and indefinability results since the early sixties: they have yielded negative results (Kaplan and Montague 1960, Montague 1963, Thomason 1980)[^kaplan-1960][^montague-1963][^thomason-1980] and established an interesting link with the surprise test paradox. The situation may have also been changed by the study of possible world semantics for modal notions, conceived as *predicates* in Halbach, Leitgeb and Welch 2003. However this is open to debate and experimentation: for instance it is argued in Halbach and Welch 2009 that the predicate approach to necessity is a viable route—insofar as the expressive power is considered—provided one resorts to languages that involve both a *truth predicate* and the *necessity operator*.

### 6.6 Staying non-classical

A number of solutions have been proposed, which rely on the use of paraconsistent logics (Priest) or substructural logics (see the entry logic: paraconsistent, as well as the entry substructural logics and Mares and Paoli 2014)[^mares-2014].

The investigation of semantical and set-theoretic paradoxes in infinite-valued logic—which was pioneered by Mow Shaw-Kwei 1954 and Skolem in 1957—has received a new impulse by contributions by Hajek, Shepherdson and Paris 2000, and Hajek 2005, 2010 (see Fisher, Halbach, Kriener and Stern 2015 for a critical discussion about the interplay between the axiomatic and the semantic approach to truth). Typically, in these papers basic results from *mathematical analysis* are applied (e.g. Brouwer’s fixed point theorem). It is worth mentioning that Leitgeb 2008 has given a consistency proof for a *probabilistic theory of truth* with unrestricted T-schema by making use of the Hahn-Banach Theorem. A follow-up of the latter source that connects with researches related to the revision theory (see §6.5), is Campbell-Moore, Horsten and Leitgeb 2019.

Theories of naive truth—as based on the unrestricted biconditional and on a logic without contraction—are to be found in the literature, e.g see Cantini 2002, Zardini 2011, Bacon 2013, Standefer 2016. Ripley 2012, instead, presents an alternative approach based on a non-transitive logical system (see also Cobreros et al. 2012, as well as Cobreros et al. 2015, which attempts at extending the approach to the paradoxes of vagueness)[^cobreros-2012].

Grišin 1981 proved that the system based upon the paradoxical principle *par excellence*—the uniform naïve comprehension schema—and (some form of) non-contractive logic enjoys cut elimination, and hence is consistent. On the other hand, the consistency of the system is ruined by extensionality and this could be counted as an additional paradox! Of course ‘uniform’ here means that a variable-binding abstraction operator {*x* | φ(*x*,*a*)} for naming the set defined by φ, depending on a list of given parameters *a*, is available. Interestingly, it has been shown that closely related systems have unexpected applications to the characterization of complexity classes (Girard 1998, Terui 2004)[^girard-1998][^terui-2004]; on the other hand, the system is *computationally complete* (it can interpret combinatory logic, Cantini 2003)[^cantini-2003].

The choice of a non-classical base logic is often not deprived of consequences, as far as the user-friendly character of a theory is concerned. A recent trend in the literature (building on Halbach and Nicolai 2018)[^halbach-2018][^nicolai-2018] is the attempt of comparing classical vs. non-classical theories (where applicable, like axiomatizations of Kripke fixed-point semantics) to determine the cost related to the one choice vs. the other (see also Castaldo 2023a, 2023b and also Castaldo 2024, which tries to argue in favor of classical theories via recapture)[^castaldo-2023a][^castaldo-2023b][^castaldo-2024].

Finally, since the character of classical (Tarskian) truth is its infinitary nature, one could well classify as non-classical the investigation from Sato and Walker 2023, which tries to clarify the relationship between truth and finitism by answering the question: Does it make sense to investigate a version of “finitist axiomatic truth”?

### 6.7 Towards a “geometric” approach

Besides tools from algebra and analysis, logical investigations about paradoxes have recently applied graph theory (see Cook 2004, Rabern, Rabern and Macauley 2013, Beringer and Schindler 2017, Hsiung 2017)[^beringer-2017][^cook-2004][^hsiung-2017][^rabern-2013]: a basic idea is the attempt to grasp in geometric terms *the patterns of paradox*, *their structural features*. For instance, one can assign a *reference graph* (rfg) to sentences of the language of arithmetic with truth via Leitgeb’s notion of dependence (Leitgeb 2005)[^leitgeb-2005]. It is further conjectured that a solution to the characterization problem for dangerous rfgs amounts to the claim that *basically the Liar- and the Yablo graph are the only paradoxical rfgs*. This route is independently developed in Rossi 2019 by exploring the wide range of semantic behaviours displayed by paradoxical sentences, and providing a unified theory of truth and paradox (see also Bruni and Rossi 2023, which, by extending these means, provide a unification of Liar-like and soritical-like paradoxes)[^bruni-2023]. The result is a theory of truth that yields a threefold classification of paradoxical sentences (liar-like sentences, truth-teller-like sentences, and revenge sentences), and proposes a way of interpreting all three kinds, as well as paradox-free sentences, within a single model, where the basic tool is a notion of “semantic graph”. In Hsiung 2020, instead, Leitgeb’s approach is combined with the one of Beringer and Schindler 2017 to study a type of paradoxes of finitary characteristic, which is defined in terms of Leitgeb’s dependence relation itself.

Notably, graph theory does not seem to be the only way by means of which a uniform treatment of paradoxes (in the form of a theory of “paradoxicality”), is tried to be achieved (see, e.g., Castaldo 2021)[^castaldo-2021].

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

### Primary Sources: 1897–1945

### Recent Sources

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=paradoxes-contemporary-logic). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/paradoxes-contemporary-logic/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=paradoxes-contemporary-logic&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/paradoxes-contemporary-logic/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

- Dopico, P. and Hayashi, D., 2024, “[Axiomatic theories of supervaluational truth: completing the picture](http://arxiv.org/abs/2410.12471)”, manuscript at arXiv.org.
- [Bibliography of Explicit Mathematics (1975–2013)](https://home.inf.unibe.ch/~til/em_bibliography/), Logic and Theory Group (LTG) at the Institute of Computer Science, University of Bern.

## Related Entries

Curry’s paradox | epistemic paradoxes | Fitch’s paradox of knowability | Frege, Gottlob | Frege, Gottlob: theorem and foundations for arithmetic | liar paradox | logic: linear | logic: paraconsistent | logic: substructural | Quine, Willard Van Orman: New Foundations | recursive functions | Russell, Bertrand | Russell’s paradox | set theory | set theory: alternative axiomatic theories | set theory: constructive and intuitionistic ZF | set theory: early development | set theory: non-wellfounded | set theory: Zermelo’s axiomatization of | Sorites paradox | Tarski, Alfred: truth definitions | truth | truth: axiomatic theories of | type theory | vagueness | Zeno of Elea | Zeno of Elea: Zeno’s paradoxes

### Acknowledgments

For this edition of the entry, the authors were supported by the Italian Ministry of Education, University and Research through the PRIN 2017 program “The Manifest Image and the Scientific Image” prot. 2017ZNWW7F_004.

[^behmann-1931]: Behmann., H., 1931, “Zu den Widersprüchen der Logik und der Mengenlehre”, *Jahresbericht der Deutschen Mathematiker-Vereinigung*, 40: 37–48.

[^bernstein-1905a]: Bernstein, F., 1905a, “Die Theorie der reellen Zahlen”, *Jahresbericht der Deutschen Mathematiker-Vereinigung*, 14: 447–449.

[^bernstein-1905b]: –––, 1905b. “Über die Reihe der transfiniten Ordnungszahlen”, *Mathematische Annalen*, 60: 187–193.

[^bernstein-1905c]: –––, 1905c, “Zum Kontinuumproblem”, *Mathematische Annalen*, 60: 463–464.

[^bochvar-1937]: Bochvar, D. A., 1937, “On a three-valued logical calculus and its applications to the analysis of the paradoxes of the classical extended functional calculus”, in *History and Philosophy of Logic*, 2: 87–112, 1981; this is an English translation, by M. Bergmann, of the Russian original, which appeared in *Mathematicheski Sbornik*, 4 (46): 287–308.

[^borel-1908]: Borel, E., 1908, “Les paradoxes de la théorie des ensembles”, *Annales scientifique de l’École Normale Supérieure*, 25: 443–448; reprinted in E. Borel, *Leçons sur la théorie des functions*, Paris: Gauthier Villars, 2ⁿᵈ edition, 1914, 162–166.

[^borel-1905]: Borel, E., Baire, R., Hadamard, J., Lebesgue, H., 1905, “Cinq lettres sur la théorie des ensembles”, *Bulletin de la Société Mathématique de* *France*, 33: 261–273.

[^brouwer-1907]: Brouwer, L.E.J., 1907, “Over die Grondslagen der Wiskunde”, Dissertation, Amsterdam; English translation in L.E.J.Brouwer, *Collected Works I*, Amsterdam: North Holland, 1975.

[^burali-forti-1897]: Burali-Forti C., 1897, “Una questione sui numeri transfiniti”. *Rendiconti del Circolo Matematico di Palermo*, 11: 260, 154–164; English translation in van Heijenoort 1967, 104–111.

[^cantor-1962]: Cantor, G., *Gesammelte Abhandlungen mathematischen und philosophischen Inhalts*, E. Zermelo (ed.), Berlin–Hildesheim: Olms, 1962.

[^cantor-1991]: –––, *Briefe*, in H. Meschkowski and W. Nilson (eds.), Berlin–Hildesheim: Olms, 1991.

[^carnap-1934a]: Carnap, R., 1934a, “Die Antinomien und die Unvollständigkeit der Mathematik”, *Monatshefte für Mathematik und Physik*, 41: 263–284.

[^carnap-1934b]: –––, 1934b, *Die logische Syntax der Sprache*, Berlin: Springer.

[^church-1932]: Church, A., 1932, “A set of postulates for the foundation of logic” (1ˢᵗ paper), *Annals of Mathematics*, 33: 346–366.

[^church-1933]: –––, 1933, “A set of postulates for the foundation of logic” (2ⁿᵈ paper), *Annals of Mathematics*, 34: 839–864.

[^church-1934]: –––, 1934, “The Richard paradox”, *American Mathematical Monthly*, 41: 356–361

[^chwistek-1921]: Chwistek, L., 1921, “Antinomje logiki formalnej”, *Przegląd Filozoficzny*, 24: 164–171; English translation by Z. Jordan: “Antinomies of formal logic”, in S. McCall (ed.), *Polish Logic 1920–1939*, Oxford: Clarendon Press, 1967, 338–345.

[^chwistek-1922]: –––, 1922, “Über die Antinomien der Prinzipien der Mathematik”, *Mathematische Zeitschrift*, 14: 236–243.

[^chwistek-1933]: –––, 1933, “Die nominalistische Grundlegung der Mathematik”, *Erkenntnis*, 3: 367–388.

[^curry-1930]: Curry, H.B., 1930, “Grundlagen der kombinatorischen Logik”, *American Journal of Mathematics*, 52: 509–536.

[^curry-1941]: –––, 1941, “The paradox of Kleene and Rosser”, *Transactions of the American Mathematical Society*, 41: 454–516.

[^curry-1942]: –––, 1942, “The inconsistency of certain formal logics”, *Journal of Symbolic Logic*, 7: 115–117.

[^finsler-1925]: Finsler, P., 1925, “Gibt es Widersprüche in der Mathematik?”, *Jahresbericht der Deutschen Mathematiker-Vereinigung*, 34: 143–155.

[^finsler-1926a]: –––, 1926a, “Formale Beweise und die Unentscheidbarkeit”, *Mathematische Zeitschrift*, 25: 676–682.

[^finsler-1926b]: –––, 1926b, “Über die Grundlagen der Mengenlehre”, *Mathematische Zeitschrift*, 25: 683–713.

[^fitch-1936]: Fitch, F.B., 1936, “A system of formal logic without an analogue to Curry W-operator”, *Journal of Symbolic Logic*, 1: 92–100..

[^fitch-1942]: –––, 1942, “A basic logic”, *Journal of Symbolic Logic*, 7: 105–114.

[^frege-1903]: Frege, G., 1903, *Grundgesetze der Arithmetik. Begriffschriftlich Abgeleitet* (Volume 2), Jena; reprinted, Hildesheim: Olms, 1962.

[^frege-1976]: –––, 1976, *Wissenschaftslicher Briefswechsel*, Hamburg: F. Meiner.

[^frege-1984]: –––, 1984, *Nachgelassene Schriften*, Hamburg: F. Meiner.

[^gödel-1931]: Gödel, K., 1931, “Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I ”, *Monatshefte für Mathematik und Physik*, 38: 173–198.

[^grelling-1908]: Grelling, K. and Nelson, L., 1908, “Bemerkungen zu den Paradoxien von Russell und Burali-Forti ”, *Abhandlungen der Fries’chen Schule*, 2: 301–334.

[^hessenberg-1906]: Hessenberg, G., 1906, *Grundbegriffe der Mengenlehre*, Göttingen: Vandenhoek und Ruprecht; also in *Abhandlungen der Fries’chen Schule*, Neue Reihe, 1: 479–706, 1906.

[^hilbert-1928]: Hilbert, D. and W. Ackermann, 1928, *Grundzüge der theoretischen Logik*, Berlin-Heidelberg: Springer.

[^hilbert-1934]: Hilbert, D. and P. Bernays, 1934/1939, *Grundlagen der Mathematik* (Volumes 1–II), Berlin, Springer (Volume I: 1934, Volume II: 1939.

[^hilbert-1904]: Hilbert, D., 1904, “Über die Grundlagen der Logik und der Arithmetik”, *Verhandlungen des Dritten Internationalen-Mathematiker Kongresses*, Leipzig: Teubner, 174–185; English trans. in van Heijenoort 1967, 129–138.

[^hilbert-1918]: Hilbert, D., 1918, *Prinzipien der Mathematik*, Vorlesung von D. Hilbert, Mathematisches Institut der Georg-August Universität Göttingen.

[^kleene-1935]: Kleene, S.C. and Rosser, J.B., 1935, “The inconsistency of certain formal logics”, *Annals of Mathematics*, 36: 630–637

[^könig-1905]: König, J., 1905, “Über die Grundlagen der Mengenlehre und das Kontinuumsproblem”, *Mathematische Annalen*, 61: 156–160.

[^levi-1902]: Levi, B., 1902, “Intorno alla teoria degli aggregati”, *Reale Istituto Lombardo di Scienze e Lettere, Rendiconti* (2nd Series), 35: 863–868

[^levi-1908]: –––, 1908, “Antinomie logiche?”, *Annali di Matematica* (Third Series), tomo 15: 188–216.

[^lewis-1932]: Lewis, C. I. and C.H. Langford, 1932, *Symbolic Logic*, New York: The Century Co.; Reprinted New York: Dover, 1952.

[^mirimanoff-1917a]: Mirimanoff, D., 1917a, “Les antinomies de Russell et de Burali-Forti et le problème fondamentale de la théorie des ensembles”, *L’Enseignement Mathématique*, 19: 37–52.

[^mirimanoff-1917b]: –––, 1917b, “Remarques sur la théorie des ensembles et les antinomies cantoriennes I ”, *L’Enseignement Mathématique*, 19: 209–217.

[^mirimanoff-1920]: –––, 1920, “Remarques sur la théorie des ensembles et les antinomies cantoriennes II ”, *L’Enseignement Mathématique*, 21: 29–52.

[^peano-1906]: Peano, G., 1906, *Additione, Revista de Matematica*, 8: 143–157; in G. Peano, *Opere Scelte* (Volume I), Roma: Cremonese, 1957, 344–358.

[^poincaré-1905]: Poincaré, H., 1905, “Les mathématiques et la logique”, *Revue de Métaphysique et de Morale*, 13: 815–835.

[^poincaré-1906a]: –––, 1906a, “Les mathématiques et la logique”, *Revue de Métaphysique et de Morale*, 14: 17–34

[^poincaré-1906b]: –––, 1906b, “Les mathématiques et la logique”, *Revue de Métaphysique et de Morale*, 14: 294–317.

[^poincaré-1909a]: –––, 1909a, “La logique de l’infini”, *Revue de Métaphysique et de Morale*, 7: 461–482

[^poincaré-1909b]: –––, 1909b, “Réflexions sur les deux notes precedents”, *Acta Mathematica*, 32: 195–200.

[^poincaré-1910]: –––, 1910, “Über transfiniten Zahlen”, in *Sechs Vorträge über ausgewählte Gegenstände der reinen Mathematik und Physik*, Leipzig-Berlin: Teubner, 43–48.

[^poincaré-1912]: –––, 1912, “La logique de l’infini”, *Scientia*, 12: 1–11.

[^quine-1937]: Quine, W.V.O., 1937, “New foundations for mathematical logic”, *American Mathematical Monthly*, 44: 70–80

[^ramsey-1926]: Ramsey, F.P., 1926, “The foundations of mathematics”, *Proceedings of the London Mathematical Society* (Series 2), 25: 338–384.

[^ramsey-1931]: –––, 1931, *The Foundations of Mathematics and Other Logical Essays*, London: Routledge and Kegan Paul.

[^richard-1905]: Richard, J., 1905, “Les principes des mathématique et le problème des ensembles”, *Revue Générale des Sciences Pures et Appliquées*, 16: 541; also in *Acta Mathematica*, 30: 295–296, 1906; English transl. in van Heijenoort 1967, 142–144.

[^rosser-1939]: Rosser, J.B., 1939, “An informal exposition of proofs of Gödel’s and Church’s theorem”, *Journal of Symbolic Logic*, 4: 53–60.

[^russell-1903]: Russell, B., 1903, *The Principles of Mathematics* (Volume 1), Cambridge: Cambridge University Press.

[^russell-1907]: –––, 1907, “On some difficulties in the theory of transfinite numbers and order types”, *Proceedings of the London Mathematical Society* (2nd series), 4: 29–53

[^russell-1906]: –––, 1906, “Les paradoxes de la logique”, *Revue de Métaphysique et de Morale*, 14: 627–650

[^russell-1908]: –––, 1908, “Mathematical Logic as Based on the Theory of Types”, *American Journal of Mathematics*, 30: 222–262; reprinted in B. Russell, *Logic and Knowledge*, London: Allen and Unwin, 1956, 59–102; reprinted in van Heijenoort 1967, 152–182.

[^schönflies-1906]: Schönflies, A., 1906, “Über die logischen Paradoxien der Mengenlehre”, *Jahresbericht der Deutschen Mathematiker-Vereinigung*, 15: 19–25.

[^tarski-1931]: Tarski, A., 1931, “Sur les ensembles définissables de nombres réels I”, *Fundamenta Mathematicae*, 17: 210–239.

[^tarski-1933]: –––, 1933, “The concept of truth in the languages of the deductive sciences” (Polish), *Prace Towarzystwa Naukowego Warszawskiego, Wydzial III Nauk Matematyczno-Fizyczych* 34, Warsaw; reprinted in Zygmunt, J. (ed.), *Alfred Tarski, Pisma Logiczno-Filozoficzne, 1 Prawda*, Warsaw: Wydawnictwo Naukowe PWN, 1995, 13–172.

[^tarski-1935]: –––, 1935, “Der Wahrheitsbegriff in der formalisierten Sprachen”, *Studia Philosophica*, 1: 261–405; this is an extended German translation of Tarski 1933; English translation in A. Tarski, *Logic, Semantics, Metamathematics*, 2nd edition, Indianapolis: Hackett, 1983, 152–278)

[^heijenoort-1967]: van Heijenoort, J., 1967, *From Frege to Gödel. A source book in mathematical logic 1879–1931*, Cambridge, Mass.: Harvard University Press.

[^neumann-1925]: von Neumann, J., 1925, “Eine Axiomatisierung der Mengenlehre”, *Journal für die reine und angewandte Mathematik*, 154: 219–240; corrections in Volume 155 (1926), p. 128).

[^weyl-1910]: Weyl, H., 1910, “Über die Definitionen der mathematischen Grundbegriffe”, *Mathematisch-naturwissenschaftliche Blätter*, 7: 93–95; 109–113.

[^weyl-1918]: –––, 1918, *Das Kontinuum*, Leipzig: Veit; English Translation, New York: Dover 1994.

[^whitehead-1910]: Whitehead, A.N. and Russell, B., 1910, 1912, 1913, *Principia Mathematica* (3 volumes), Cambridge: Cambridge University Press; second edition, 1925 (volume 1), 1927 (volumes 2, 3).

[^whitehead-1911]: –––, 1911, “Über die Stellung der Definition in der Axiomatik”, *Jahresbericht der Deutschen Mathematiker-Vereinigung*, 20: 222–255.

[^zermelo-1908]: Zermelo, E., 1908, “Untersuchungen über die Grundlagen der Mengenlehre I”, *Mathematische Annalen*, 65: 261–281.

[^zygmunt-1995]: Zygmunt, J. (ed.), 1995, *Alfred Tarski, Pisma Logiczno-Filozoficzne, 1 Prawda*, Warsaw: Wydawnictwo Naukowe PWN.

[^this-nd]: This list contains (i) items cited in the final section; (ii) items related to developments of paradoxes after the Second World War; (iii) critical historical papers.

[^aczel-1980]: Aczel, P., 1980, “Frege structures and the notion of proposition, truth and set”, *The Kleene Symposium*, J. Barwise et al. (eds.), Amsterdam: North-Holland, 31–59.

[^aczel-1988]: –––, 1988, “Non-Well-Founded Sets”, Stanford: CSLI.

[^anderson-2001]: Anderson, C.A. and Zelëny, M. (eds.), 2001, *Logic, Meaning and Computation*, Dordrecht: Kluwer.

[^bacon-2013]: Bacon, A., 2013, “Curry’s paradox and omega inconsistency” *Studia Logica*, 101: 1–9.

[^barendregt-1984]: Barendregt, H., 1984, *The Lambda Calculus. Its Syntax and Semantics* (Studies in Logic and the Foundations of Mathematics, vol. 103), Amsterdam: Elsevier.

[^barwise-1984]: Barwise, J. and Etchemendy, J., 1984. *The Liar*, New York: Oxford University Press.

[^barwise-1996]: Barwise J. and Moss, L., 1996, *Vicious Circles. On the Mathematics of Non-Wellfounded Phenomena*, Stanford: CSLI, 1996.

[^beall-2003]: Beall, JC (ed.), 2003, *Liars and Heaps*, Oxford: Clarendon Press.

[^beall-2007]: –––, 2007, *Revenge of the Liar. New Essays on the Paradox*, New York: Oxford University Press.

[^beringer-2017]: Beringer, T. and Schindler, T., 2017, “A graph-theoretic analysis of the semantic paradoxes”, *Bull. Symb. Log.*, 23: 442–492.

[^bernardi-2001]: Bernardi, C., 2001, “Fixed points and unfounded chains”, *Annals of Pure and Applied Logic*, 109: 163–178.

[^bernardi-2009]: –––, 2009, “A topological approach to Yablo’s paradox”, *Notre Dame Journal of Formal Logic*, 50: 331–338.

[^betti-2004]: Betti, A., 2004, “Lesniewski’s early Liar, Tarski and natural language”, *Annals of pure and applied logic*, 127: 267–287

[^birkhoff-1967]: Birkhoff, G., 1967, *Lattice Theory*, Providence, RI: American Mathematical Society, 3ʳᵈ edition.

[^boolos-1989]: Boolos, G., 1989, “A new proof of the Gödel incompleteness theorem”, *Notices of the American Mathematical Society*, 36: 388–390

[^boolos-1993]: –––, 1993, *The logic of provability*, Cambridge: Cambridge University Press.

[^brandenburger-2006]: Brandenburger, A. and Keisler, H. J., 2006, “An impossibility theorem on beliefs in games”, *Studia Logica*, 84: 211–240.

[^bruni-2009]: Bruni, R., 2009 “A note on theories for quasi-inductive definitions”, *Review of Symbolic Logic*, 2: 684–699.

[^bruni-2013]: –––, 2013, “Beppo Levi’s analysis of the paradoxes”, *Logica Universalis*, 7: 211–231.

[^bruni-2013b]: –––, 2013b, “Analytic calculi for circular concepts by finite revision”, *Studia Logica*, 101: 915–932.

[^bruni-2015]: –––, 2015, “Some remarks on the finite theory of revision” , in D. Achourioti et al. (eds), *Unifying the philosophy of truth* (Logic, Epistemology, and the Unity of Science: Volume 36), Dordrecht: Springer, pp. 169–187.

[^bruni-2019]: –––, 2019, “Addressing Circular Definitions via Systems of Proofs”, in: S. Centrone et al. (eds.), *Mathesis Universalis. Computability and Proof*, Springer Verlag, pp. 75–100.

[^bruni-2023]: Bruni, R. and Rossi, L., 2023, “Truth meets vagueness. Unifying the semantic and the soritical paradoxes”, *Journal of Philosophical Logic*, 52(6): 1637–1671.

[^bruni-2018]: Bruni, R. and Sillari, G., 2018, “A rational way of playing: revision theory for strategic interaction”, *Journal of Philosophical Logic*, 47: 419–448.

[^bueno-2014]: Bueno, O., Menzel, C., and Zalta, E.N., 2014, “Worlds and Propositions Set Free”, *Erkenntnis*, 79: 797–820.

[^burgess-2011]: Burgess, A.G. and Burgess, J.P., 2011, *Truth*, Princeton: Princeton University Press.

[^burgess-2005]: Burgess, J., 2005, *Fixing Frege*, Princeton: Princeton University Press.

[^campbell-moore-2019]: Campbell-Moore, C., 2019, “Limits in the Revision Theory: More Than Just Definite Verdicts”, *Journal of Philosophical Logic*, 48: 11–35.

[^campbell-moore-2019-2]: Campbell-Moore C., Horsten, L. and Leitgeb, H., 2019, “Probability for the Revision Theory of Truth”, *Journal of Philosophical Logic*, 48: 87–112.

[^cantini-1999]: Cantini, A. and Minari, P., 1999, “Uniform inseparability in explicit mathematics”, *The Journal of Symbolic Logic*, 64: 313–326.

[^cantini-1990]: Cantini, A., 1990, “A theory of formal truth arithmetically equivalent to ID₁”, *Journal of Symbolic Logic*, 55: 244–59.

[^cantini-2002]: –––, 2002, “Partial truth”, in L. Horsten and V. Halbach (eds.), *Principles of Truth*, Frankfurt: Hansel-Hohenhausen, 183–202.

[^cantini-2003]: –––, 2003, “The undecidability of Grišin’s set theory”, *Studia Logica*, 74: 345–368.

[^cantini-2004]: –––, 2004, “On a Russellian paradox about propositions and truth”, in G. Link 2004, 259–284.

[^castaldo-2021]: Castaldo, L., 2021, “Fixed-point models for paradoxical predicates”, *Australasian Journal of Logic*, 18(7): 688–723.

[^castaldo-2023a]: –––, 2023a, “On the costs of classical logic”, *Erkenntnis*, 88: 1157–1188.

[^castaldo-2023b]: –––, 2023b, “Notes on models of (partial) Kripke–Feferman truth”, *Studia Logica*, 111: 83–111.

[^castaldo-2024]: –––, 2024, “Saving logic from paradox via nonclassical recapture”, *Philosophical Studies*, 181: 1547–1563.

[^chaitin-1995]: Chaitin, G., 1995, “The Berry paradox”, *Complexity*, 1: 26–30.

[^church-1976]: Church, A., 1976,“A Comparison of Russell’s Resolution of the Semantical Antinomies with that of Tarski ”, *Journal of Symbolic Logic*, 41: 747–760.

[^cobreros-2012]: Cobreros, P., Egré, P., Ripley, D. and van Rooij, R., 2012, “Tolerant, classical, strict”, *Journal of Philosophical Logic*, 41: 347–85.

[^cobreros-nd]: –––, “Vagueness, truth and permissive consequence”, in K. Fujimoto, J. Martínez Fernández, H. Galinon, T. Achourioti (eds.), *Unifying the Philosophy of Truth*, Springer Verlag, 409–430.

[^cook-2004]: Cook, R.T., 2004, “Patterns of Paradox”, *Journal of Symbolic Logic*, 69: 767–774.

[^cook-2014]: –––, 2014, *The Yablo paradox*, New York: Oxford University Press.

[^coquand-1986]: Coquand, T., 1986, “An analysis of Girard’s paradox,” *Proceedings of the IEEE Symposium on Logic in Computer Science*, pp. 227–236.

[^coquand-1994]: –––, 1994, “A new paradox in type theory,” in D. Prawitz, B. Skyrms, D. Westerstahl (eds.), *Logic, Methodology and Philosophy of Science IX*, Studies in Logic and the Foundations of Mathematics, vol. 134, Amsterdam: North-Holland, 555–570.

[^dean-2020]: Dean, W., 2020, “Incompleteness via Paradox”, *Review of Symbolic Logic*, 13(3): 541–592.

[^dean-2016]: Dean, W. and Kurokawa, H., 2016, “Kreisel’s Theory of Constructions, the Kreisel-Goodman Paradox, and the Second Clause”, in T. Piecha and P. Schroeder-Heister (eds.), *Advances in Proof-Theoretic Semantics* (Trends in Logic, Volume 43), Springer International Publishing, 27–63.

[^de-2018]: De Vos, M., Kooi, B. and Verbrugge, R., 2018, “Provability Logic meets the knower paradox”, in: G. Bezhanishvilii (eds.), *Advances in Modal Logic 2018*, Rijksuniversiteit Groningen, pp. 31–35.

[^douven-2021]: Douven I. (ed.), 2021, *Lotteries, Knowledge, and Rational Belief: Essays On the Lottery Paradox*, Cambridge: Cambridge University Press.

[^eberhard-2015]: Eberhard, S. and Strahm, T., 2015, “Unfolding Feasible Arithmetic and Weak Truth”, in T. Achourioti, H. Galinon, J.M. Fernandez, K. Fujimoto (eds.), *Unifying the Philosophy of Truth*, Dordrecht: Springer, 153–167.

[^égré-2005]: Égré, P., 2005, “The Knower Paradox in the Light of Provability Interpretations of Modal Logic”, *Journal of Logic, Language, and Information*, 14: 13–48.

[^enayat-2015]: Enayat, A. and Visser, A., 2015, “New constructions of satisfaction classes”, in T. Achourioti, H. Galinon, J.M. Fernandez, K. Fujimoto (eds.), *Unifying the Philosophy of Truth*, Dordrecht: Springer International Publishing, 321–335.

[^feferman-1960]: Feferman, S., 1960, “Arithmetization of metamathematics in a general setting”, *Fundamenta mathematicae*, 49: 35–92.

[^feferman-1964]: –––, 1964, “Systems of predicative analysis I”, *Journal of Symbolic Logic*, 29: 1–30.

[^feferman-1979]: –––, 1979, “Constructive theories of functions and classes”, in M. Boffa and D. van Dalen (eds.), *Logic Colloquium ‘78*, Amsterdam: North Holland, 159–224.

[^feferman-1984]: –––, 1984,“Towards Useful Type-free Theories. I.” *Journal of Symbolic Logic*, 49: 75–111.

[^feferman-1991]: –––, 1991,“Reflecting on Incompleteness”, *Journal of Symbolic Logic*, 56: 1–49.

[^feferman-2008]: –––, 2008,“Axioms for Determinatess and Truth”, *Review of Symbolic Logic*, 1: 204–217.

[^field-2003]: Field, H., 2003, “A revenge-immune solution to the semantic paradoxes.”, *Journal of Philosophical Logic*, 32: 139–177.

[^field-2008]: –––, 2008, *Saving Truth from Paradox*, New York: Oxford University Press.

[^fischer-2015]: Fischer, M., Halbach, V., Kriener, J., Stern J., 2015, “Axiomatizing semantic theories of truth?”, *The Review of Symbolic Logic*, 8(2): 257–278.

[^flagg-1987]: Flagg, R. and Myhill, J., 1987, “Implications and analysis in classical Frege structures”. *Annals of Pure and Applied Logic*, 34: 33–85.

[^forti-1983]: Forti, M. and Honsell, F., 1983, “Set theory with free construction principles”, *Annali della Scuola Normale Superiore di Pisa*, Classe di Scienze, Serie IV, 10: 493–522.

[^forti-1989]: Forti, M. and Hinnion, R., 1989, “The consistency problem for positive comprehension principles”, *Journal of Symbolic Logic*, 54: 1401–1418.

[^friedman-1987]: Friedman, H. and Sheard, M., 1987, “An Axiomatic Approach to Self-Referential Truth”, *Annals of Pure and Applied Logic*, 33: 1–21.

[^fujimoto-2010]: Fujimoto, K, 2010, “Relative truth and definability of axiomatic truth theories”, *Bulletin of Symbolic Logic*, 16: 33: 305–344.

[^fujimoto-2011]: –––, 2011, “Autonomous progression and transfinite iteration of self-applicable truth”, *Journal of Symbolic Logic*, 76: 914–945.

[^fujimoto-2012]: –––, 2012, “Classes and truths in set theory”, *Annals of Pure and Applied Logic*, 163: 1484–1523.

[^gaifman-1988]: Gaifman, H., 1988. “Operational pointer semantics: Solution to self-referential puzzles I ”, in M. Vardi (ed.), *Proceedings of the Second Conference on Theoretical Aspects of Reasoning about Knowledge*, San Francisco: Morgan Kaufmann, 43–59.

[^gaifman-1999]: –––, 1999, “Self-Reference and the Acyclity of Rational Choice”, *Annals of Pure and Applied Logic*, 96: 117–140.

[^garciadiego-1992]: Garciadiego, A., 1992, *Bertrand Russell and the Origins of Set-theoretic “Paradoxes”*, Basel: Birkhäuser.

[^geach-1955]: Geach, P., 1955, “On Insolubilia”, *Analysis*, 15: 71–72.

[^girard-1998]: Girard, J. Y., 1998, “Light linear logic”, *Information and Computation*, 143: 175–204.

[^grišin-1981]: Grišin, V.N., 1981, “Predicate and set theoretic calculi based on logic without contraction rules” (Russian), *Izvestiya Akademii Nauk SSSR* (Seriya Matematicheskaya), 45(1): 47–68; English translation in *Mathematics of the USSR – Izvestia*., 1982, 18(1): 41–59.

[^grue-2002]: Grue, K., 2002, “Lambda calculus as a foundation of mathematics,”, in C.A. Anderson and M. Zelëny (eds.), *Logic, Meaning and Computation: Essays in Memory of Alonzo Church*, Dordrecht: Kluwer, 287–311.

[^gupta-2011]: Gupta, A., 2011, “On circular concepts” in *Truth, Meaning and Experience*, Oxford: Oxford University Press, 95–134.

[^gupta-1993]: Gupta, A. and Belnap, N., 1993, *The Revision Theory of Truth*, Cambridge, MA: MIT Press.

[^gupta-2017]: Gupta, A. and Standefer, S., 2017, “Conditionals in Theories of Truth”, *Journal of Philosophical Logic*, 46: 27–63.

[^hajek-2005]: Hajek, P., 2005 , “On the arithmetic in the Cantor-Łukasiewicz set theory”, *Archive for Mathematical Logic*, 44: 763–782.

[^hajek-2010]: –––, 2010, “On White’s expansion of Łukasiewicz logic”, *Journal of Logic and Computation.*, 20, 389–397.

[^hajek-2000]: Hajek, P., Paris, J. and Shepherdson, J., 2000 ,“The liar paradox and fuzzy logic”, *Journal of Symbolic Logic*, 65: 339–346.

[^halbach-2011]: Halbach, V., 2011, *Axiomatic Theories of Truth*, Cambridge: Cambridge University Press.

[^halbach-2003]: Halbach, V., Leitgeb, H. and Welch, P., 2003, “Possible world semantics for modal notions conceived as predicates”, *Journal of Philosophical Logic*, 32: 179–223.

[^halbach-2009]: Halbach, V. and Welch, P., 2009, “Necessities and necessary truths: a prolegomenon to the use of modal notions in the analysis of the intensional notions”, *Mind*, 118: 71–100.

[^halbach-2018]: Halbach, V. and Nicolai, C., 2018, “On the costs of non-classical logic”, *Journal of Philosophical Logic*, 47: 227–257.

[^halbach-2017]: Halbach, V. and Zhang, S., 2017, “Yablo without Gödel”, *Analysis*, 77: 53–59.

[^hayashi-2025]: Hayashi, D., 2025, “Theories of Frege structure equivalent to Feferman’s system T₀”, *Annals of Pure and Applied Logic*, 176(1): 1–36, 2025.

[^hinnion-2003]: Hinnion, R. and Libert, T., 2003, “Positive abstraction and extensionality”, *Journal of Symbolic Logic*, 68: 828–836.

[^holmes-2001]: Holmes, M.R., 2001,“Tarski’s Theorem and NFU, ” in Anderson et al., 2001, 469–478.

[^horsten-2011]: Horsten, L., 2011, *The Tarskian Turn. Deflationism and Axiomatic Truth*, Cambridge, MA: The MIT.

[^horsten-nd]: Horsten, L. and Leigh, G., “Truth is simple”, *Mind*, 126: 195–232.

[^hsiung-2017]: Hsiung, M., 2017, “Boolean paradoxes and revision periods”, *Studia Logica*, 105: 881–914.

[^hsiung-2020]: –––, 2020, “What paradoxes depend on”, *Synthese*, 197: 887–913.

[^irvine-2009]: Irvine, A., 2009, “Bertrand Russell’s Logic, ”in D.M. Gabbay and J. Wood (eds.), *Handbook of the History of Logic* (Volume 5: Logic from Russell to Church), Amsterdam: Elsevier and North-Holland, 1–28.

[^jäger-1997]: Jäger, G., 1997, “Power types in explicit mathematics”, *Journal of Symbolic Logic*, 62: 1142–1146.

[^kahle-2004]: Kahle, R., 2004, “David Hilbert über Paradoxien”, Preprint Number 06–17, Departamento de Matemática, Universidade de Coimbra, 2006, 1–42.

[^kahle-2002]: Kahle, R. and Peckhaus, V., 2002, “Hilbert’s paradox”, *Historia Mathematica*, 29: 127–155.

[^kaplan-1960]: Kaplan, D. and Montague, R., 1960, “A paradox regained”, *Notre Dame Journal of Formal Logic*, 1: 79–90.

[^kikuchi-1994]: Kikuchi, M., 1994, “ A note on Boolos’ proof of the incompleteness theorem”, *Mathematical Logic Quarterly*, 40: 528–532.

[^kikuchi-2016]: Kikuchi, M. and Kurahashi, T., 2016, “Liar-type paradoxes and the incompleteness phenomena”, *Journal of Philosophical Logic*, 45: 381–398.

[^klement-2010]: Klement, K., 2010, “Russell, His Paradoxes, and Cantor’s Theorem: Part I”, *Philosophy Compass*, 5: 16–28.

[^kreisel-1950]: Kreisel, G., 1950, “Note on arithmetic models for consistent arithmetic formulae of the predicate calculus”, *Fundamenta Mathematicae*, 37: 265–285.

[^kreisel-1960]: –––, 1960, “La prédicativité”, *Bulletin de la Société Mathématique de France*, 88: 371–391.

[^kripke-1975]: Kripke, S., 1975, “Outline of a Theory of Truth”, *Journal of Philosophy*, 72: 690–716.

[^kritchman-2011]: Kritchman, S. and Raz, R., 2011, “ The surprise examination paradox and the second incompleteness theorem”, *Notices of the American Mathematical Society*, 57: 1454–1458.

[^kurahashi-2014]: Kurahashi, T., 2014, “Rosser-type undecidable sentences and Yablo’s paradox”, *Journal of Philosophical Logic*, 43: 999–1017.

[^kyburg-1961]: Kyburg, H., 1961, *Probability and the Logic of Rational Belief*, Middletown: Wesleyan University Press.

[^lawvere-1969]: Lawvere, F.W., 1969, “Diagonal arguments and Cartesian closed categories”, in P. Hilton (ed.), *Category Theory, Homology Theory and their Applications*, II (Volume 92: Lecture Notes in Mathematics), Berlin-Heidelberg, Springer, 134–145.

[^leigh-2013]: Leigh, G., 2013, “A proof-theoretic account of classical principles of truth”, *Annals of Pure and Applied Logic*, 164: 1009–1024.

[^leigh-2015a]: –––, 2015a, “Some Weak Theories of Truth”, in T. Achourioti, H. Galinon, J.M. Fernandez, K. Fujimoto (eds.), *Unifying the Philosophy of Truth*, Dordrecht: Springer International Publishing, 281–292.

[^leigh-2015b]: –––, 2015b, “Conservativity for theories of compositional truth via cut elimination”, *Journal of Symbolic Logic*, 80: 845–865.

[^leigh-2010]: Leigh, G. and Rathjen, M., 2010, “An ordinal analysis for theories of self-referential truth”, *Archive for Mathematical Logic*, 49: 213–247.

[^leigh-2012]: –––, 2012, “The Friedman-Sheard programme in intuitionistic logic”, *Journal of Symbolic Logic*, 77: 777–806.

[^leitgeb-2005]: Leitgeb, H., 2005, “What truth depends on”, *Journal of Philosophical Logic*, 34 (2), 155–192.

[^leitgeb-2007]: –––, , 2007, “ What theories of truth should be like (but cannot be)”, *Blackwell Philosophy Compass*, 2: 276–290.

[^leitgeb-2008]: –––, 2008, “ On the probabilistic convention T”, *Review of Symbolic Logic*, 1: 218–224.

[^leitgeb-2021]: –––, 2021, “Stability and the lottery paradox”, in Douven 2021, 147–170.

[^libert-2005]: Libert, T. and Esser, O., 2005, “On topological set theory”, *Mathematical Logic Quarterly*, 51: 263–273.

[^link-2004]: Link, G. (ed.), 2004, *One Hundred Years of Russell’s Paradox*, Berlin: De Gruyter.

[^linsky-2004]: Linsky, B., 2004, “Leon Chwistek on the no-classes theory”, *History and Philosophy of Logic*, 25: 53–71.

[^löb-1955]: Löb, M.H., 1955, “Solution of a problem of Leon Henkin”, *The Journal of Symbolic Logic*, 20: 115–118.

[^lolli-2007]: Lolli, G, 2007, “A Berry-type paradox” in C.S. Calude (ed.), *Randomness and Complexity. From Leibniz to Chaitin*, Singapore: World Scientific publishing, 155–160.

[^malitz-1976]: Malitz, R.J., 1976, *Set Theory in which the axiom of foundation fails*, Ph.D. thesis, Philosophy Department, University of California, Los Angeles.

[^mancosu-2003]: Mancosu, P., 2003, “The Russellian Influence on Hilbert and his School”, *Synthèse*, 137: 59–101.

[^mancosu-2019b]: Mancosu, P., Siskind, B., 2019b, “Neologicist Foundation: Inconsistent abstraction principles and part-whole”, in G.M. Mras, P. Weingartner, and B. Ritter (eds.), *Philosophy of Logic and Mathematics: Proceedings of the 41st International Wittgenstein Symposium*, Berlin: De Gruyter, pp. 215–248.

[^mancosu-2004]: Mancosu, P., Zach, R. and Badesa, C., 2004, “The Development of Mathematical Logic from Russell to Tarski: 1900–1935”, in L. Haaparanta (ed.), *The History of Modern Logic*, Oxford: Oxford University Press, pp. 1–187.

[^mares-2014]: Mares, E. and Paoli, F., 2014, “Logical consequence and the paradoxes”, *Journal of Philosophical Logic*, 43: 439–469.

[^martin-1984]: Martin, R.L., 1984, *Recent Essays on Truth and the Liar Paradox*, Oxford: Oxford University Press, 1984.

[^martin-löf-1971]: Martin-Löf, P., 1971, *A Theory of Types*, Technical Report 71–3, University of Stockholm.

[^martin-löf-1998]: –––, 1998, “An intuitionistic theory of types,” in G. Sambin and J.A. Smith (eds.), *Twenty-five years of constructive type theory*, Oxford: Oxford University Press, 127–172.

[^martino-2001]: Martino, E., 2001,“, Russellian type theories and semantical paradoxes,”, in Anderson et al., 2001, pp. 491 –506.

[^mcgee-1991]: McGee, V., 1991, *Truth, Vagueness, and Paradox: An Essay on the Logic of Truth*, Indianapolis and Cambridge: Hackett Publishing.

[^meadows-2015]: Meadows, T., 2015, “Infinitary Tableau for Semantic Truth”, *Review of Symbolic Logic*, 8: 217–235.

[^moh-1954]: Moh Shaw-Kwei, 1954, “Logical Paradoxes for Many-Valued Systems”, *Journal of Symbolic Logic*, 19: 37–39.

[^montagna-1994]: Montagna, F., 1994, “Paradoxes and Incompleteness theorems: the Solovay theorem” (in Italian), *Epistemologia della Matematica. 1992–93 Seminars*, CNR, Rome, pp. 85–95.

[^montague-1963]: Montague, R., 1963, “Syntactical treatment of modality, with corollaries on reflection principles and finite axiomatizability”, *Acta Philosophica Fennica*, 16: 153–167.

[^moore-1995]: Moore, G.H., 1995, “The origin of Russell’s paradox: Russell, Couturat and the antinomy of infinite number”, in J. Hintikka (ed.), *From Dedekind to Gödel. Essays on the development of the foundation of mathematics*, Dordrecht: Kluwer, 215–239.

[^moore-1981]: Moore, G.H. and Garciadiego, A., 1981, “Burali-Forti’s paradox: a reappraisal of its origins”, *Historia Mathematica*, 8: 319–350.

[^murzi-2015]: Murzi, J. and Carrara, M., (eds.), 2015, “Paradox and Logical Revision”, *Topoi*, 34: 1–131.

[^myhill-1950]: Myhill, J., 1950, “A system which can define its own truth”, *Fundamenta Mathematicae*, 37: 190–92.

[^nicolai-2018]: Nicolai, C. 2018, “Necessary truths and supervaluations”, in Ciro de Florio and Alessandro Giordani (eds.), *From arithmetic to metaphysics* (Philosophical Analysis: 73), Berlin: De Gruyter, 309–329.

[^pelham-1994]: Pelham, J. and Urquhart, A., 1994, “Russellian propositions”, in D. Prawitz, B. Skyrms, and D. Westerstahl (eds.), *Logic, Methodology and Philosophy of Science IX*, Amsterdam: Elsevier, 307–326.

[^rabern-2013]: Rabern, L., Rabern, B., and Macauley, M., 2013, “Dangerous reference graphs and semantic paradoxes”, *Journal of Philosophical logic*, 42: 727–765.

[^reck-2016]: Reck, E.H. and Cook, R.T, 2016, “Special Issue: Reconsidering Frege’s Conception of Number”, *Philosophia Mathematica*, 24: 1–116.

[^reinhardt-1986]: Reinhardt, W.N., 1986, “Some Remarks on Extending and Interpreting Theories with a Partial Predicate for Truth”, *Journal of Philosophical Logic*, 15: 219–51.

[^ripley-2012]: Ripley, D., 2012, “Conservatively extending classical logic with transparent truth”, *Review of Symbolic Logic*, 5: 354–378.

[^rivello-2019a]: Rivello, E., 2019a, “Revision without revision sequences: circular definitions”, *Journal of Philosophical Logic*, 48: 57–85.

[^rivello-2019b]: –––, 2019b, “Revision without revision sequences: self-referential truth”, *Journal of Philosophical Logic*, 48: 523–551.

[^rossi-2016]: Rossi, L., 2016, “Adding a conditional to Kripke’s theory of truth”, *Journal of Philosophical Logic*, 45: 485–529.

[^rossi-2019]: –––, 2019, “A unified theory of truth and paradox.”, *Review of Symbolic Logic*, 12: 209–254.

[^sato-2023]: Sato, K. and Walker, J., 2023, “Finitist axiomatic truth”, *The Journal of Symbolic Logic*, 88(1): 22–73.

[^schindler-2016]: Schindler, T. and Beringer, T., 2016, “Reference graphs and semantic paradox”, in A. Arazim, and M. Dancak (eds.), *Logica Yearbook 2015*, London: College Publications, 1–15.

[^schütte-1960]: Schütte, K., 1960, *Beweistheorie*, Berlin-Heidelberg: Springer.

[^scott-1975]: Scott, D., 1975, “Combinators and classes”, in C. Böhm (ed.), *λ*-*calculus and computer science* (Lecture Notes in Computer Science: 37), Berlin: Springer, 1–26.

[^scott-1972]: –––, 1972, “Continuous lattices”, in W. Lawvere (ed.), *Toposes, Algebraic Geometry and Logic* (Lecture Notes in Mathematics: 274), Berlin-Heidelberg: Springer, 97–136.

[^sheard-1994]: Sheard, M., 1994, “A Guide to truth Predicates in the Modern Era”, *Journal of Symbolic Logic*, 59: 1032–54.

[^shen-yuting-1953]: Shen-Yuting, 1953, “The paradox of the class of all grounded sets”, *The Journal of Symbolic Logic*, 18: 114.

[^simmons-1993]: Simmons, K., 1993. *Universality and the Liar*, New York: Cambridge University Press.

[^specker-1962]: Specker, E., 1962, “Typical ambiguity”, in E. Nagel, P. Suppes, and A. Tarski (eds.), *Logic, Methodology and Philosophy of Science*, Stanford: Stanford University Press, pp. 116–123.

[^standefer-2015]: Standefer, S,, 2015, “Solovay-type theorems for circular definitions”, *Review of Symbolic Logic*, 8: 467–487.

[^standefer-2016]: –––, 2016, Contraction and revision, *Australasian Journal of Logic*, 13: 58–77.

[^standefer-2017]: –––, 2017, “Non-Classical Circular Definitions”, *Australasian Journal of Logic*, 14: 147–180.

[^standefer-2018]: –––, 2018, “Proof Theory for Functional Modal Logic”, *Studia Logica*, 106: 49–84.

[^terui-2004]: Terui, K., 2004, “Light Affine Set Theory: a naïve set theory of polynomial time”, *Studia Logica*, 77: 9–40.

[^thomason-1980]: Thomason, R., 1980, “A note of syntactical treatments of modality”, *Synthèse*, 44: 391–395.

[^visser-1989]: Visser, A., 1989, “Semantics and the liar paradox,” *Handbook of Philosophical Logic* (Volume IV), Dordrecht: Kluwer, 617–706.

[^wang-1955]: Wang, H., 1955, “Undecidable sentences generated by semantic paradoxes”, *Journal of Symbolic logic*, 20, 31–43.

[^welch-2001]: Welch, P., 2001, “On Gupta-Belnap revision theories of truth, Kripkean fixed points and the next stable”, *Bulletin of Symbolic Logic*, 7: 345–360.

[^welch-2008]: –––, 2008, “Ultimate truth *vis-a-vis*, Stable Truth ”, *Review of Symbolic Logic*, 1: 126–142.

[^welch-2009]: –––, 2009, “Games for truth”, *Bulletin of Symbolic Logic*, 15: 410–427.

[^welch-2011]: –––, 2011, “Weak systems of determinacy and arithmetical quasi-inductive definitions”, *Journal of Symbolic Logic*, 76: 418–436.

[^welch-2014]: –––, 2014, “Some observations on truth hierarchies”, *Review of Symbolic Logic*, 7: 1–30.

[^welch-2019]: –––, 2019, Rethinking Revision, *Journal of Philosophical Logic*, 48: 137–154.

[^weydert-1988]: Weydert, E., 1988, *How to approximate the naive comprehension scheme inside classical logic*, Dissertation, Rheinische Friedrich-Wilhelms-Universität, Bonn; published in Bonner Mathematische Schriften, 194, Universität Bonn, Mathematisches Institut, Bonn, 1989.

[^wolenski-1995]: Wolenski, J., 1995, “On Tarski’s background”, in J. Hintikka (ed.), *From Dedekind to Gödel*, *Essays on the development of the foundation of mathematics*, Dordrecht: Kluwer, 331–341.

[^yablo-1993]: Yablo, Stephen, 1993, “Paradox without self-reference,” *Analysis*, 53: 251–252.

[^yablo-2006]: –––, 2006, “Circularity and Paradox”, in T. Bolander, V.F. Hendricks, and S.A. Pedersen (eds.), *Self-Reference*, Stanford: Center for the Study of Language and Information Publications, 165–184.

[^zardini-2011]: Zardini, E., 2011, “Truth without contra(di)ction”, *Review of Symbolic Logic*, 4: 498–535.
