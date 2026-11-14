# The Algebra of Logic Tradition
**First published Mon Mar 2, 2009; substantive revision Fri Feb 12, 2021**

*Burris, Stanley, Legris, Javier*

The *algebra of logic*, as an *explicit* algebraic system showing the underlying mathematical structure of logic, was introduced by George Boole (1815–1864) in his book *The Mathematical Analysis of Logic* (1847). It is therefore to be distinguished from the more general approach of *algebraic logic*. The methodology initiated by Boole was successfully continued in the 19ᵗʰ century in the work of William Stanley Jevons (1835–1882), Charles Sanders Peirce (1839–1914), Ernst Schröder (1841–1902), among many others, thereby establishing a tradition in (mathematical) logic. From Boole’s first book until the influence after WWI of the monumental work *Principia Mathematica* (1910–1913) by Alfred North Whitehead (1861–1947) and Bertrand Russell (1872–1970), versions of the algebra of logic were the most developed form of mathematical logic above all as presented in Schröder’s three volumes *Vorlesungen über die Algebra der Logik* (1890–1905). Furthermore, this tradition motivated the investigations of Leopold Löwenheim (1878–1957) that eventually gave rise to model theory. In addition, in 1941, Alfred Tarski (1901–1983) in his paper “On the calculus of relations” returned to Peirce’s relation algebra as presented in Schröder’s *Algebra der Logik*. The tradition of the algebra of logic played a key role in the notion of *Logic as Calculus* as opposed to the notion of *Logic as Universal Language*. Beyond Tarski’s algebra of relations, the influence of the algebraic tradition in logic can be found in other mathematical theories, such as category theory. However this influence lies outside the scope of this entry, which is divided into 10 sections.

## 1. Introduction

Boole’s *The Mathematical Analysis of Logic* presents many interesting logic novelties: It was the beginning of nineteenth-century mathematization of logic and provided an *algorithmic* alternative (via a slight modification of ordinary algebra) to the *catalog* approach used in traditional logic (even if reduction procedures were developed in the latter). Instead of a list of valid forms of argument, the validity of arguments were determined on the basis of general principles and rules. Furthermore, it provided an effective method for proving logical laws on the basis of a system of postulates. As Boole wrote later, it was a proper “science of reasoning”, and not a “mnemonic art” like traditional Syllogistics (Boole 1997: 136)[^boole-1997]. Three-quarters of the way through this book, after finishing his discussion of syllogistic logic, Boole started to develop the general tools that would be used in his *Laws of Thought* (1854) to greatly extend traditional logic by permitting an argument to have many premises and to involve many classes. To handle the infinitely many possible logical arguments of this expanded logic, he presented theorems that provided key tools for an algorithmic analysis (a catalog was no longer feasible).

Boole’s ideas were conceived independently of earlier anticipations, like those developed by G.W. Leibniz. They emerged from the particular contexts of English mathematics (see Peckhaus 2009)[^peckhaus-2009]. According to Víctor Sánchez Valencia, the tradition that originated with Boole came to be known as the *algebra of logic* since the publication in 1879 of *Principles of the Algebra of Logic* by Alexander MacFarlane (see Sánchez Valencia 2004: 389)[^sánchez-2004]. MacFarlane considered “the analytical method of reasoning about Quality proposed by Boole” as an algebra (see MacFarlane 1879: 3).

This approach differs from what is usually called *algebraic logic*; though there is some overlap, the historical development of the two areas are different. Algebraic logic is understood as:

> *a style* [of logic] *in which concepts and relations are* expressed by mathematical symbols [$\ldots$] so that mathematical techniques can be applied. Here mathematics shall mean mostly algebra, i.e., the part of mathematics concerned with finitary operations on some set. (Hailperin 2004: 323)[^hailperin-2004]

Algebraic logic can be already found in the work of Leibniz, Jacob Bernoulli and other modern thinkers, and it undoubtedly constitutes an important antecedent of Boole’s approach. In a broader perspective, both are part of the tradition of *symbolic knowledge* in the formal sciences, as first conceived by Leibniz (see Esquisabel 2012)[^esquisabel-2012]. This idea of algebraic logic was continued to some extent in the French Enlightenment in the work of Condillac and Condorcet (see Grattan-Guinness 2000: 14 ff.)[^grattan-guinness-2000]

Boole’s methodology for dealing with logical problems can be described as follows:

1. Translate the logical data into suitable equations;
2. Apply algebraic techniques to solve these equations;
3. Translate this solution, if possible, back into the original language.

In other words, symbolic formulation of logical problems and solution of logical equations constitutes Boole’s method (see Sánchez Valencia 2004: 389)[^sánchez-2004].

Later, in his *Pure Logic* from 1864, Jevons changed Boole’s partial operation of union of disjoint sets to the modern unrestricted union and eliminated Boole’s questionable use of uninterpretable terms (see Jevons 1890)[^jevons-1890]. Peirce (1880)[^peirce-1880] eliminated explicitly the Aristotelian derivation of particular statements from universal statements by giving the modern meaning for “All $A$ is $B$”. In addition, he extended the algebra of logic for classes to the algebra of logic for binary relations and introduced general sums and products to handle quantification. Ernst Schröder, taking inspiration from previous work by Hermann (1809–1877) and Robert Grassmann (1815–1901) and using the framework developed by Peirce, developed and systematized the 19ᵗʰ Century achievements in the algebra of logic in his three-volume work *Vorlesungen über die Algebra der Logik* (1890–1910).

The contributions of Gottlob Frege (1848–1925) to logic from the period 1879–1903, based on an *axiomatic* approach to logic, had very little influence at the time (and the same can be said of the *diagrammatic* systems of C.S. Peirce developed at the turn of the century). Whitehead and Russell rejected the algebra of logic approach, with its predominantly equational formulations and algebraic symbolism, in favor of an approach strongly inspired by the axiomatic system of Frege, and using the notation developed by Giuseppe Peano, namely to use logical connectives, relation symbols and quantifiers.

During the first two decades of the twentieth century, the algebra of logic was further developed in the works of Platon Sergeevich Poretzsky (1846–1907), Louis Couturat (1868–1914), Leopold Löwenheim (1878–1957), and Heinrich Behmann (1891–1970) (see Styazhkin 1969)[^styazhkin-1969]. In particular, elimination theorems in the algebra of logic influenced decision procedures for fragments of first-order and second-order logic (see Mancosu, Zach, Badesa 2009)[^mancosu-2009].

After WWI David Hilbert (1862–1943), who had at first adopted the algebraic approach, picked up on the approach of *Principia*, and the algebra of logic fell out of favor. However, in 1941, Tarski treated relation algebras as an equationally defined class. Such a class has many models besides the *collection of all binary relations on a given universe* that was considered in the 1800s, just as there are many Boolean algebras besides the *power set Boolean algebras* studied in the 1800s. In the years 1948–1952 Tarski, along with his students Chin and Thompson, created cylindric algebras as an algebraic logic companion to first-order logic, and in 1956 Paul Halmos (1916–2006) introduced polyadic algebras for the same purpose. As Halmos (1956 b, c and d) noted, these new algebraic logics tended to focus on studying the extent to which they captured first-order logic and on their universal algebraic aspects such as axiomatizations and structure theorems, but offered little insight into the nature of the first-order logic which inspired their creation.

## 2. 1847—The Beginnings of the Modern Versions of the Algebra of Logic

In late 1847, Boole and Augustus De Morgan (1806–1871) each published a book on logic—Boole’s *Mathematical Analysis of Logic* (1847) and De Morgan’s *Formal Logic* (1847). De Morgan’s approach was to dissect every aspect of traditional deductive logic (usually called ‘Aristotelian logic’) into its minutest components, to consider ways to generalize these components, and then, in some cases, undertake to build a logical system using these components. Unfortunately, he was never able to incorporate his best ideas into a significant system. His omission of a symbol for equality made it impossible to develop an equational algebra of logic. It seems that synthesis was not De Morgan’s strong suit.

De Morgan’s book of 1847 was part of a revival in logic studies that originated at the beginning of 19th Century with Joseph Diez Gergonne (1771–1859) in France, and Bernhard Bolzano (1781–1848) in Bohemia, among others. George Bentham and William Hamilton in the United Kingdom were also part of this revival and their studies focused on the nature of variations of the categorical sentences in traditional syllogistic, including what was called “quantification of the predicate”; for example, “All $A$ are some $B$” or “Some $A$ are all $B$”. It was thought that this problem required an extension of the syllogistic logic of Aristotle and that some form of symbolic method was needed both to handle such statements and provide a classification of their different types (see Heinemann 2015 chapters 2 and 3)[^heinemann-2015].

Boole approached logic from a completely different perspective, namely how to cast Aristotelian logic in the garb of symbolical algebra. Using symbolical algebra was a theme with which he was well-acquainted from his work in differential equations, and from the various papers of his young friend and mentor Duncan Farquharson Gregory (1813–1844), who made attempts to cast other subjects such as geometry into the language of symbolical algebra. Since the application of symbolical algebra to differential equations had proceeded through the introduction of differential operators, it must have been natural for Boole to look for operators that applied in the area of Aristotelian logic. He readily came up with the idea of using “selection” operators, for example, a selection operator for the color red would select the red members from a class. In his 1854 book, Boole realized that it was simpler to omit selection operators and work directly with classes. (However he kept the selection operators to justify his claim that his laws of logic were not ultimately based on observations concerning the use of language, but were actually deeply rooted in the processes of the human mind.) From now on in this article, when discussing Boole’s 1847 book, the selection operators have been replaced with the simpler direct formulation using classes.

Since symbolical algebra was just the syntactic side of ordinary algebra, Boole needed ways to interpret the usual operations and constants of algebra to create his algebra of logic for classes. Multiplication was interpreted as intersection, leading to his one new law, the idempotent law $XX = X$ for multiplication, rediscovering a logical law already formulated by Leibniz. Addition was defined as union, provided one was dealing with *disjoint* classes; and subtraction as class difference, provided one was subtracting a subclass from a class. In other cases, the addition and subtraction operations were simply undefined, or as Boole wrote, *uninterpretable*. The usual laws of arithmetic told Boole that 1 must be the universe and $1 - X$ must be the complement of $X$.

The next step in Boole’s system was to translate the four kinds of categorical propositions into equations, for example “All $X$ is $Y$” becomes $X = XY$, and “Some $X$ is $Y$” becomes $V = XY$, where $V$ is a new symbol. To eliminate the middle term in a syllogism Boole borrowed an elimination theorem from ordinary algebra, but it was too weak for his algebra of logic. This would be remedied in his 1854 book. Boole found that he could not always derive the desired conclusions with the above translation of particular propositions (i.e., those with existential import), so he added the variants $X = VY$, $Y = VX$, and $VX = VY$ (see the entry on Boole).

The symbolic algebra of the 1800s included much more than just the algebra of polynomials, and Boole experimented to see which results and tools might apply to the algebra of logic. For example, he proved one of his results by using an infinite series expansion. His fascination with the possibilities of ordinary algebra led him to consider questions such as: What would logic be like if the idempotent law were replaced by the law $X^3 = X$? His successors, especially Jevons, would soon narrow the operations on classes to the ones that we use today, namely union, intersection and complement.

As mentioned earlier, three-quarters of the way through his brief book of 1847, after finishing derivations of the traditional Aristotelian syllogisms in his system, Boole announced that his algebra of logic was capable of far more general applications. Then he proceeded to add general theorems on developing (expanding) terms, providing interpretations of equations, and using long division to express one class in an equation in terms of the other classes (with side conditions added).

Boole’s theorems, completed and perfected in 1854, gave algorithms for analyzing infinitely many argument forms. This opened a new and fruitful perspective, deviating from the traditional approach to logic, where for centuries scholars had struggled to come up with clever mnemonics to memorize a very small catalog of valid conversions and syllogisms and their various interrelations.

De Morgan’s *Formal Logic* did not gain significant recognition, primarily because it was a large collection of small facts without a significant synthesis. Boole’s *The Mathematical Analysis of Logic* had powerful methods that caught the attention of a few scholars such as De Morgan and Arthur Cayley (1821–1895); but immediately there were serious questions about the workings of Boole’s algebra of logic: Just how closely was it tied to ordinary algebra? How could Boole justify the procedures of his algebra of logic? In retrospect it seems quite certain that Boole did not know why his system worked. His claim, following Gregory, that in order to justify using ordinary algebra it was enough to check the commutative law $XY = YX$ for multiplication and the distributive law $X(Y + Z) = XY + XZ$, is clearly false. Nonetheless it is also likely that he had checked his results in a sufficient number of cases to give substance to his belief that his system was correct.

## 3. 1854—Boole’s Final Presentation of his Algebra of Logic

In his second book, *The Laws of Thought*, Boole not only applied algebraic methods to traditional logic but also attempted some reforms to logic. He started by augmenting the laws of his 1847 algebra of logic (without explicitly saying that his previous list of three axioms was inadequate), and made some comments on the rule of inference (performing the same operation on both sides of an equation). But then he casually stated that the foundation of his system actually rested on a single (new) principle, namely it sufficed to check an argument by seeing if it was correct when the class symbols took on only the values 0 and 1, and the operations were the usual arithmetical operations. Let us call this *Boole’s Rule of 0 and 1*. No meaningful justification was given for Boole’s adoption of this new foundation, it was not given a special name, and the scant references to it in the rest of the book were usually rather clumsily stated. For a modern analysis of this Rule of 0 and 1 see Burris & Sankappanavar 2013.

The development of the algebra of logic in the *Laws of Thought* proceeded much as in his 1847 book, with minor changes to his translation scheme, and with the selection operators replaced by classes. There is a new and very important theorem (correcting the one he had used in 1847), the Elimination Theorem, which says the following: given an equation $F(x,y, z, \ldots) = 0$ in the class symbols $x, y, z$, etc., the most general conclusion that follows from eliminating certain of the class symbols is obtained by (1) substituting 0s and 1s into $F(x, y, z, \ldots)$ for the symbols to be eliminated, in all possible ways, then (2) multiplying these various substitution instances together and setting the product equal to 0. Thus eliminating $y$ and $z$ from $F(x, y, z) = 0$ gives $F(x, 0, 0)F(x, 0, 1)F(x, 1, 0)F(x, 1, 1) = 0$. This theorem also played an important role in Boole’s interpretation of Aristotle’s syllogistic.

From an algebra of logic point of view, the 1854 treatment at times seems less elegant than that in the 1847 book, but it gives a much richer insight into how Boole thinks about the foundations for his algebra of logic. The final chapter on logic, Chapter XV, was an attempt to give a uniform proof of the Aristotelian conversions and syllogisms. (It is curious that prior to Chapter XV Boole did not present any examples of arguments involving particular propositions.) The details of Chapter XV are quite involved, mainly because of the increase in size of expressions when the Elimination and Development Theorems are applied. Boole simply left most of the work to the reader. Later commentators would gloss over this chapter, and no one seems to have worked through its details.

Aside from the Rule of 0 and 1 and the Elimination Theorem, the 1854 presentation is mainly interesting for Boole’s attempts to justify his algebra of logic. He argued that in symbolical algebra it was quite acceptable to carry out equational deductions with partial operations, just as one would when the operations were total, as long as the terms in the premises and the conclusion were interpretable. He said this was the way ordinary algebra worked with the uninterpretable $\sqrt{-1}$, the square root of −1. (The geometric interpretation of complex numbers was recognized early on by Wessel, Argand, and Gauss, but it was only with the publications of Gauss and Hamilton in the 1830s that doubts about the acceptability of complex numbers in the larger mathematical community were overcome. It is curious that in 1854 Boole regarded $\sqrt{-1}$ as uninterpretable.)

There were a number of concerns regarding Boole’s approach to the algebra of logic:

1. Was there a meaningful tie between his algebra of logic and the algebra of numbers, or was it just an accident that they were so similar?
2. Could one handle particular propositions in an algebraic logic that focused on equations?
3. Was it really acceptable to work with uninterpretable terms in equational derivations?
4. Was Boole using “Aristotelian” semantics (the semantics presupposed in traditional logic, where the extension of a term is nonempty)?

## 4. Jevons: An Algebra of Logic Based on Total Operations

Jevons, who had studied with De Morgan, was the first to offer an alternative to Boole’s system. In 1863 he wrote to Boole that surely Boole’s operation of addition should be replaced by the more natural ‘inclusive or’ (or ‘union’), leading to the law $X + X = X$. Boole completely rejected this suggestion (it would have destroyed his system based on ordinary algebra) and broke off the correspondence. Jevons published his system in his 1864 book, *Pure Logic* (reprinted in Jevons 1890)[^jevons-1890]. By ‘pure’ he meant that he was casting off any dependence on the algebra of numbers—instead of classes, which are associated with quantity, he would use predicates, which are associated with quality, and his laws would be derived directly from the (total) fundamental operations of inclusive disjunction and conjunction. But he kept Boole’s use of equations as the fundamental form of statements in his algebra of logic.

By adopting De Morgan’s convention of using upper-case/lower-case letters for complements, Jevons’ system was not suited to provide equational axioms for modern Boolean algebra. However, he refined his system of axioms and rules of inference until the result was essentially the modern system of Boolean algebra for *ground terms*, that is, terms where the class symbols are to be thought of as constants, not as variables.

It must be noticed that modern equational logic deals with *universally quantified* equations (which would have been called *laws* in the 1800s). In the 19ᵗʰ century algebra of logic one could translate “All $X$ is $Y$” as the equation $X = XY$. This is *not* to be viewed as the universally quantified expression $(\forall X)(\forall Y)(X = XY)$. $X$ and $Y$ are to be treated as constants (or schematic letters). Terms that only have constants (no variables) are called *ground* terms.

By carrying out this analysis in the special setting of an algebra of predicates (or equivalently, in an algebra of classes) Jevons played an important role in the development of modern equational logic. As mentioned earlier, Boole gave inadequate sets of equational axioms for his system, originally starting with the two laws due to Gregory plus his idempotent law; these were accompanied by De Morgan’s inference rule that one could carry out the same operation (Boole’s fundamental operations in his algebra of logic were addition, subtraction and multiplication) on equals and obtain equals. Boole then switched to the simple and powerful (but unexplained) Rule of 0 and 1.

Having replaced Boole’s fundamental operations with total operations, Jevons proceeded, over a period of many years, to work on the axioms and rules for his system. Some elements of equational logic that we now take for granted required a considerable number of years for Jevons to resolve:

*The Reflexive Law* ($A=A$). In 1864 Jevons listed this as a postulate (1890, p. 11) and then in §24 he referred to $A = A$ as a “useless Identical proposition”. In his 1869 paper on substitution it became the “Law of Identity”. In the *Principles of Science* (1874) it was one of the three “Fundamental Laws of Thought”.

*The Symmetric Law* ($B = A$ follows from $A = B$). In 1864 Jevons wrote “$A = B$ and $B = A$ are the same statement”. This is a position he would maintain. In 1874 he wrote

> I shall consider the two forms $A = B$ and $B = A$ to express exactly the same identity written differently.

For a final form of his algebra of logic we turn to the laws which he had scattered over 40 pages in *Principles of Science* (1874), having replaced his earlier use of + by $\ORjev$, evidently to move further away from any appearance of a connection with the algebra of numbers:

Laws of Combination

$$ \begin{align} A &= AA = AAA = \& c & \mbox{Law of Simplicity (p. 33)}\\ AB &= BA & \mbox{A Law of Commutativeness (p. 35)}\\ A \ORjev A & = A &\mbox{Law of Unity (p. 72)}\\ A \ORjev B &= B \ORjev A &\mbox{A Law of Commutativeness (p. 72)}\\ A(B \ORjev C) &= AB \ORjev AC & \mbox{(no name given) (p. 76)}\\ \end{align} $$

Laws of Thought

$$ \begin{align} A &= A & \mbox{Law of Identity (p. 74)}\\ Aa &= o & \mbox{Law of Contradiction (p. 74)}\\ A &= AB \ORjev Ab & \mbox{Law of Duality (p. 74)}\\ \end{align} $$

For his single rule of inference Jevons chose his principle of substitution—in modern terms this was essentially a combination of ground replacement and transitivity. He showed how to derive transitivity of equality from this; he could have derived symmetry as well but did not. The associative law was missing—it was implicit in the lack of parentheses in his expressions.

It was only in his *Studies in Deductive Logic* (1880) that Jevons mentioned McColl’s use of an accent to indicate negation. After noting that McColl’s accent allowed one to take the negation of complex bracketed terms he went on to say that, for the most part, he found the notation of De Morgan, the notation that he had always used, to be the more elegant.

## 5. Peirce: Basing the Algebra of Logic on Subsumption

Peirce started his research into the algebra of logic in the late 1860s. In his paper “On an Improvement in Boole’s calculus of Logic” (Peirce 1867)[^peirce-1867], he arrived independently at the same conclusion that Jevons had reached earlier, that one needed to replace Boole’s partial operation of addition with the total operation of union (see CP 3.3.6). In his important 1880 paper, “On the Algebra of Logic”, Peirce quietly broke with the traditional extensional semantics and introduced a usual assumption of modern semantics: the extension of a concept, understood as a class, could be empty (as well as the universe), and stated the truth values of the categorical propositions that we use today. For example, he said the proposition “All $A$ is $B$” is true if $A$ and $B$ are both the empty class. Conversion by Limitation, that is, the argument “All $A$ is $B$” therefore “Some $B$ is $A$”, was no longer a valid inference. Peirce said nothing about the reasons for and merits of his departure from the traditional semantic assumption of existence.

Peirce also broke with Boole’s and Jevons’ use of equality as the fundamental primitive, using instead the relation of “subsumption” interpretable in different ways (subclass relation, implication, etc.). He stated the partial order properties of subsumption and then proceeded to define the operations of + and × as least upper bounds and greatest lower bounds—he implicitly assumed such bounds existed—and listed the key equational properties of the algebras with two binary operations that we now call lattices. Then he claimed that the distributive law followed, but said the proof was too tedious to include. The fruitfulness of this perspective is evident in his seminal paper from 1885. There Peirce introduced a system for propositional logic based on five axioms for implication (represented by the sign ‘$-\kern-.4em<$’), including what is now called Peirce’s law. It certainly made the algebra of logic more elegant.

## 6. De Morgan and Peirce: Relations and Quantifiers in the Algebra of Logic

De Morgan wrote a series of six papers called “On the Syllogism” in the years 1846 to 1863 (reprinted in De Morgan 1966)[^de-1966]. In his efforts to generalize the syllogism, De Morgan replaced the copula “is” with a general binary relation in the second paper of the series dating from 1850. By allowing different binary relations in the two premises of a syllogism, he was led to introduce the composition of the two binary relations to express the conclusion of the syllogism. In this pursuit of generalized syllogisms he introduced various other operations on binary relations, including the converse operation, and he developed a fragment of a calculus for these operations. His main paper on this subject was the fourth in the series, called “On the syllogism, No. IV, and on the logic of relations” published in 1859 (see De Morgan 1966)[^de-1966].

Following De Morgan’s paper, Peirce, in his paper “Description of a Notation for the Logic of Relatives, resulting from an Amplification of the Conceptions of Boole’s Calculus of Logic” from 1870, lifted Boole’s work to the setting of binary relations—with binary relations one had, in addition to union, intersection and complement, the natural operations of composition and converse. A binary relation was characterized as a set of ordered pairs (see 3.328). He worked on this new calculus between 1870 and 1883. Like De Morgan, Peirce also considered a number of other natural operations on relations. Peirce’s main paper on the subject was “On the Algebra of Logic” (1880). By employing unrestricted unions, denoted by Σ, and unrestricted intersections, denoted by Π, Peirce thus introduced quantifiers into his algebra of logic.

In a paper from 1882, “Brief Description of the Algebra of Relatives”, reprinted in De Morgan 1966, he used these quantifiers to define operations on relations by means of operations on certain kind of coefficients. De Morgan gets credit for introducing the concept of relation, but Peirce is considered the true creator of the theory of relations (see, e.g., Tarski 1941: 73)[^tarski-1941]. However, Peirce did not develop this theory. As Calixto Badesa wrote, “the calculus of relatives was never to Peirce’s liking” (Badesa 2004: 32)[^badesa-2004]. He considered it too complicated because of the combination of class operations with relational ones. Instead, he preferred from 1885 onwards to develop a “general algebra” including quantifiers but no operation on relations. In this way, he arrived at an elementary and informal presentation of what is now called first-order logic (see Badesa 2004, *loc. cit*.)[^badesa-2004].

## 7. Schröder’s systematization of the algebra of logic

The German mathematician Ernst Schröder played a key role in the tradition of the algebra of logic. A good example was his challenge to Peirce to provide a proof of the distributive law, as one of the key equational properties of the algebras with two binary operations. Peirce (1885)[^peirce-1885] admitted that he could not provide a proof. Years later Huntington (1904: 300–301)[^huntington-1904] described part of the content of a letter he had received from Peirce in December 1903 that claimed to provide the missing proof—evidently Peirce had stumbled across the long lost pages after the death of Schröder in 1902. Peirce explained to Huntington that he had originally assumed Schröder’s challenge was well-founded and that this apparent shortcoming of his paper “was to be added to the list of blunders, due to the grippe, with which that paper abounds, …”. Actually Peirce’s proof did not correct the error since the distributive law does not hold in lattices in general; instead his proof brought in the operation of complementation—he used the axiom

> if $a$ is not contained in the complement of $b$ then $a$ and $b$ have a common lower bound.

On the basis of his previous algebraic work, Schröder wrote an encyclopedic three volume work at the end of the 19ᵗʰ century called *Vorlesungen über die Algebra der Logik* (1890–1905), built on the subsumption framework with the modern semantics of classes as presented by Peirce. This work was the result of his research in algebra and revealed different influences. Schröder aimed at a general algebraic theory with applications in many mathematical fields, where the algebra of logic was at the core. As Geraldine Brady pointed out, it offers the first exposition of abstract lattice theory, the first exposition of Dedekind’s theory of chains after Dedekind, the most comprehensive development of the calculus of relations, and a treatment of the foundations of mathematics on the basis of the relation calculus (see Brady 2000: 143 f.)[^brady-2000]

The first volume concerned the equational logic of classes, the main result being Boole’s Elimination Theorem of 1854. Three rather complicated counter-examples to Peirce’s claim of distributivity appeared in an appendix to Vol. I, one of which involved nine-hundred and ninety identities for quasigroups. On the basis of this volume, Dedekind (1897)[^dedekind-1897] composed an elegant modern abstract presentation of lattices (which he called *Dualgruppen*); in this paper he presented a five-element counter-example to Peirce’s claim of the distributive law.

Volume II augments the algebra of logic for classes developed in Volume I so that it can handle existential statements. First, using modern semantics, Schröder proved that one cannot use equations to express “Some $X$ is $Y$”. However, he noted that one can easily express it with a negated equation, namely $XY \ne 0$. Volume II, a study of the calculus of classes using both equations and negated equations, attempted to cover the same topics covered in Vol. I, in particular there was considerable effort devoted to finding an Elimination Theorem. After dealing with several special cases, Schröder recommended this topic as an important research area—the quest for an Elimination Theorem would be known as the Elimination Problem.

Inspired mainly by Peirce’s work, Schröder examined the algebra of logic for binary relations in Vol. III of his *Vorlesungen über die Algebra der Logik*. As Tarski once noted, Peirce’s work was continued and extended in a very thorough and systematic way by Schröder. One item of particular fascination for him was this: given an equation $E(x, y, z, \ldots) = 0$ in this algebra, find the general solution for one of the relation symbols, say for $x$, in terms of the other relation symbols. He managed, given a particular solution $x = x0$, to find a remarkable term $S(t, y, z, \ldots)$ with the following properties: (1) $x = S(t, y, z, \ldots)$ yields a solution to $E = 0$ for any choice of relation $t$, and (2) every solution $x$ of $E = 0$ can be obtained in this manner by choosing a suitable $t$. Peirce was not impressed by Schröder’s preoccupation with the problem of solving equations, and pointed out that Schröder’s parametric solution was a bit of a hoax—the expressive power of the algebra of logic for relations was so strong that by evaluating the term $S(t, y, z, \ldots)$ one essentially carried out the steps to check if $E(t, y, z, \ldots) = 0$; if the answer was yes then $S(t, y, z, \ldots)$ returned the value $t$, otherwise it would return the value $x0$.

Summing up, Schröder constructed an algebraic version of modern predicate logic and also a theory of relations. He applied it to different fields (e.g., Cantor’s set theory), and he considered his algebraic notation as a general or universal language (*pasigraphy*, see Peckhaus 2004 and Legris 2012)[^legris-2012][^peckhaus-2004]. It is to be noted that Löwenheim in 1940 still thought it was as reasonable as set theory. According to him, Schröder’s idea of solving a relational equation was a precursor of Skolem functions, and Schröder inspired Löwenheim’s formulation and proof of the famous theorem that every “arithmetical” sentence with an infinite model has a countable model. Schröder’s calculus of relations was the basis for the doctoral dissertation of Norbert Wiener (1894–1964) in Harvard (Wiener 1913)[^wiener-1913]. According to Brady, Wiener gave the first axiomatic treatment of the calculus of relations, preceding Tarski’s axiomatization by more than twenty years (see Brady 2000: 165)[^brady-2000].

## 8. Huntington: Axiomatic Investigations of the Algebra of Logic

At the turn of the 19ᵗʰ Century, David Hilbert (1862–1943) presented, in his *Grundlagen der Geometrie*, Euclidean geometry as an axiomatic subject that did not depend on diagrams for its proofs (Hilbert 1899)[^hilbert-1899]. This led to a wave of interest in studying axiom systems in mathematics; in particular one wanted to know if the axioms were independent, and which primitives led to the most elegant systems. Edward Vermilye Huntington (1874–1952) was one of the first to examine this issue for the algebra of logic. He gave three axiomatizations of the algebra of logic, showed each set of axioms was independent, and that they were equivalent (see Huntington 1904)[^huntington-1904]. In 1933 he returned to this topic with three new sets of axioms, one of which contained the following three equations (1933: 280):

$$ \begin{align} a + b &= b + a \\ (a + b) + c &= a + (b + c) \\ (a' + b')' + (a' + b)' &= a. \end{align} $$

Shortly after this, Herbert Robbins (1915–2001) conjectured that the third equation could be replaced by the slightly simpler

$$ [(a + b)' + (a + b')']' = a. $$

Neither Huntington nor Robbins could prove this, and later it withstood the efforts of many others, including even Tarski and his talented school at Berkeley. Building on partial results of Winker, the automated theorem prover EQP, designed by William McCune of the Argonne National Laboratory, found a proof of the Robbins Conjecture in 1996. This accomplishment was popularized in Kolata 2010.

According to Huntington (1933: 278)[^huntington-1933], the term “Boolean algebra” was introduced by Henry M. Sheffer (1882–1964) in the paper where he showed that one could give a five-equation axiomatization of Boolean algebra using the single fundamental operation of joint exclusion, now known as the Sheffer stroke (see Sheffer 1913)[^sheffer-1913]. Whitehead and Russell claimed in the preface to the second edition of *Principia* that the Sheffer stroke was the greatest advance in logic since the publication of *Principia*. (Hilbert and Ackermann (1928), by contrast, stated that the Sheffer stroke was just a curiosity.) Neither realized that decades earlier Schröder had discovered that the dual of the Sheffer stroke was also such an operation—Schröder’s symbol for his operation was that of a double-edged sword.

In the 1930s Garrett Birkhoff (1911–1996) established the fundamental results of equational logic, namely (1) equational classes of algebras are precisely the classes closed under homomorphisms, subalgebras and direct products, and (2) equational logic is based on five rules: reflexivity, symmetry, transitivity, replacement, and substitution. In the 1940s, Tarski joined in this development of equational logic; the subject progressed rapidly from the 1950s till the present time.

## 9. Stone: Models for the Algebra of Logic

Traditional logic studied certain simple relationships between classes, namely *being a subclass of* and *having a nonempty intersection with*. However, once one adopted an axiomatic approach, the topic of possible models besides the obvious ones surfaced. Beltrami introduced models of non-Euclidean geometry in the late 1860s. In the 1890s Schröder and Dedekind constructed models of the axioms of lattice theory to show that the distributive law did not follow. But when it came to the algebra of classes, Schröder considered only the standard models, namely each was the collection of all subclasses of a given class.

The study of general models of the axioms of Boolean algebra did not get underway until the late 1920s; it was soon brought to a very high level in the work of Marshall Harvey Stone (1903–1989) (see his papers 1936, 1937). He was interested in the structure of rings of linear operators and realized that the central idempotents, that is, the operators $E$ that commuted with all other operators in the ring under multiplication (that is, $EL = LE$ for all $L$ in the ring) and which were idempotent under multiplication ($EE = E$) played an important role. In a natural way, the central idempotents formed a Boolean algebra.

Pursuing this direction of research led Stone to ask about the structure of an arbitrary Boolean algebra, a question that he answered by proving that *every Boolean algebra is isomorphic to a Boolean algebra of sets*. In his work on Boolean algebras he noticed a certain analogy between kernels of homomorphisms and the ideals studied in ring theory—this led him to give the name “ideal” to such kernels. Not long after this he discovered a translation between Boolean algebras and Boolean rings; under this translation the ideals of a Boolean algebra corresponded precisely to the ideals of the associated Boolean ring. His next major contribution was to establish a correspondence between Boolean algebras and certain topological spaces now called Boolean spaces (or Stone spaces). This correspondence would later prove to be a valuable tool in the construction of exotic Boolean algebras. These results of Stone are still a paradigm for developments in the algebra of logic.

Inspired by the rather brief treatment of first-order statements about relations in Vol. III of the *Algebra der Logik*, Löwenheim (1915)[^löwenheim-1915] showed that if such a statement could be satisfied in an infinite domain then it could be satisfied in a denumerable domain. In 1920 Thoralf Skolem (1887–1963) simplified Löwenheim’s proof by introducing Skolem normal forms, and in 1928 Skolem replaced his use of normal forms with a simpler idea, namely to use what are now called Skolem functions. He used these functions to convert first-order sentences into universal sentences, that is to say, into sentences in prenex form with all quantifiers being universal ($\forall$).

## 10. Skolem: Quantifier Elimination and Decidability

Skolem was strongly influenced by Schröder’s *Algebra der Logik*, starting with his PhD Thesis. Later he took a particular interest in the quest for an Elimination Theorem in the calculus of classes. In his 1919 paper he established some results for lattices, in particular, he showed that one could decide the validity of universal Horn sentences (i.e., universal sentences with a matrix that is a disjunction of negated and unnegated atoms, with at most one positive atom) by a procedure that we now recognize to be a polynomial time algorithm. This algorithm was based on finding a least fixed point of a finite partial lattice under production rules derived from universal Horn sentences. Although this result, which is equivalent to the uniform word problem for lattices, was in the same paper as Skolem’s famous contribution to Löwenheim’s Theorem, it was forgotten until a chance rediscovery in the early 1990s. (Whitman (1941)[^whitman-1941] gave a different solution to the more limited equational decision problem for lattices; it became widely known as the solution to the word problem in lattices.)

Skolem (1920)[^skolem-1920] gave an elegant solution to the Elimination Problem posed by Schröder for the calculus of classes by showing that if one added predicates to express “has at least $n$ elements”, for each $n = 1, 2, \ldots$, then there was a simple (but often lengthy) procedure to convert a first-order formula about classes into a quantifier-free formula. In particular this showed that the first-order theory of the calculus of classes was decidable. This quantifier-elimination result was used by Mostowski (1952)[^mostowski-1952] to analyze first-order properties of direct powers and direct sums of single structures, and then by Feferman and Vaught (1959) to do the same for general direct sums and direct products of structures.

The elimination of quantifiers became a main method in mathematical logic to prove decidability, and proving decidability was stated as the main problem of mathematical logic in Hilbert and Ackermann (1928)—this goal was dropped in subsequent editions because of the famous undecidability result of Church and Turing.

## 11. Tarski and the Revival of Algebraic Logic

Model theory can be regarded as the product of Hilbert’s methodology of metamathematics and the algebra of logic tradition, represented specifically by the results due to Löwenheim and Skolem. But it was Tarski who gave the discipline its classical foundation. Model theory is the study of the relations between a formal language and its interpretation in “realizations” (that is, a domain for the variables of the language together with an interpretation for its primitive signs). If the interpretation happens to make a sentence of the language state something true, then the interpretation is a *model* of the sentence (see the entry on model theory). Models consist basically of algebraic structures, and model theory became an autonomous mathematical discipline with its roots not only in the algebra of logic but in abstract algebra (see Sinaceur 1999)[^sinaceur-1999].

Apart from model theory, Tarski revived the algebra of relations in his 1941 paper “On the Calculus of Relations”. First he outlined a formal logic based on allowing quantification over both elements and relations, and then he turned to a more detailed study of the quantifier-free formulas of this system that involved only relation variables. After presenting a list of axioms that obviously held in the algebra of relations as presented in Schröder’s third volume he proved that these axioms allowed one to reduce quantifier-free relation formulas to equations. Thus his calculus of relations became the study of a certain equational theory which he noted had the same relation to the study of all binary relations on sets as the equational theory of Boolean algebra had to the study of all subsets of sets. This led to questions paralleling those already posed and resolved for Boolean algebras, for example, was every model of his axioms for relation algebras isomorphic to an algebra of relations on a set? One question had been answered by Arwin Korselt (1864–1947), namely there were first-order sentences in the theory of binary relations that were not equivalent to an equation in the calculus of relations—thus the calculus of relations definitely had a weaker expressive power than the first-order theory of relations. Actually the expressive power of relation algebra is exactly equivalent to first-order logic with just three variables. However, if in relation algebras (the calculus of relations) one wants to formalize a set theory which has something such as the pair axiom, then one can reduce many variables to three variables, and so it is possible to express any first-order statement of such a theory by an equation. Monk proved that, unlike the calculus of classes, there is no finite equational basis for the calculus of binary relations (see Monk 1964)[^monk-1964]. Tarski and Givant (1987) showed that the equational logic of relation algebras is so expressive that one can carry out first-order set theory in it.

Furthermore, cylindric algebras, essentially Boolean algebras equipped with unary cylindric operations $C_x$ which are intended to capture the existential quantifiers ($\exists x$), were introduced in the years 1948–1952 by Tarski, working with his students Louise Chin and Frederick Thompson (see Henkin & Tarski 1961)[^henkin-1961], to create an algebra of logic that captured the expressive power of the first-order theory of binary relations. Polyadic algebra is another approach to an algebra of logic for first-order logic—it was created by Halmos (1956c)[^halmos-1956c]. The focus of work in these systems was again to see to what extent one could parallel the famous results of Stone for Boolean algebra from the 1930s.

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

### Primary Sources

### Secondary Sources

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=algebra-logic-tradition). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/algebra-logic-tradition/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=algebra-logic-tradition&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/algebra-logic-tradition/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

[Please contact the author with suggestions.]

## Related Entries

algebra | Boole, George | Leibniz, Gottfried Wilhelm: influence on 19th century logic | model theory | model theory: first-order

[^boole-1847]: Boole, G., 1847, *The Mathematical Analysis of Logic, Being an Essay Towards a Calculus of Deductive Reasoning*, Cambridge: Macmillan, Barclay, & Macmillan; reprinted Oxford: Basil Blackwell, 1951.

[^boole-1854]: –––, 1854, *An Investigation of The Laws of Thought on Which are Founded the Mathematical Theories of Logic and Probabilities*, London: Macmillan; reprint by Dover 1958.

[^boole-1997]: –––, 1997. *Selected Manuscripts on Logic and its Philosophy*, Ivor Grattan-Guinness and Gérard Bornet (eds.), Basel, Boston, Berlin, Birkhäuser: Springer.

[^couturat-1905]: Couturat, Louis, 1905, *L’Algèbre de la Logique*, Paris: Gauthier-Villars; 2ⁿᵈ edition, Paris: Blanchard 1980.

[^dedekind-1897]: Dedekind, R., 1897, “Über Zerlegungen von Zahlen durch ihre grössten gemeinsamen Teiler”, reprinted in *Gesammelte mathematische Werke* (1930–1932), 2: 103–147.

[^dedekind-1930]: –––, 1930–1932, *Gesammelte mathematische Werke*, Robert Fricke, Emmy Noether, Öystein Ore (eds.), Braunschweig: Friedr. Vieweg & Sohn.

[^de-1847]: De Morgan, A., 1847, *Formal Logic: or, the Calculus of Inference, Necessary and Probable*, London: Taylor and Walton; reprinted London: The Open Court Company 1926.

[^de-1966]: –––, 1966, *On the Syllogism and Other Logical Writings*, a posthumous collection of De Morgan’s papers on logic, edited by Peter Heath, New Haven: Yale University Press.

[^feferman-1959]: Feferman, S. and R.L. Vaught, 1959, “The first order properties of products of algebraic systems”, *Fundamenta Mathematica*, 47: 57–103.

[^frege-1879]: Frege, F., 1879, *Begriffsschrift: eine der arithmetischen nachgebildete Formelsprache des reinen Denkens*, Halle a. S.: Louis Nebert.

[^frege-1884]: –––, 1884, *Die Grundlagen der Arithmetik:eine logisch-mathematische Untersuchung über den Begriff der Zahl*, Breslau: W. Koebner.

[^frege-1893]: –––, 1893/1903, *Grundgesetze der Arithmetik, begriffsschriftlich abgeleitet*, 2 vols, Jena: Verlag Hermann Pohle.

[^halmos-1956a]: Halmos, P.R., 1956a, “Algebraic logic. I. Monadic Boolean algebras”, *Compositio Mathematica*, 12: 217–249.

[^halmos-1956b]: –––, 1956b, “The basic concepts of algebraic logic”, *American Mathematical Monthly*, 63: 363–387.

[^halmos-1956c]: –––, 1956c, “Algebraic logic. II. Homogeneous locally finite polyadic Boolean algebras of infinite degree”, *Fundamenta Mathematica*, 43: 255–325.

[^halmos-1956d]: –––, 1956d, “Algebraic logic. III. Predicates, terms, and operations in polyadic algebras”, *Transactions of the American Mathematical Society*, 83: 430–470.

[^halmos-1957]: –––, 1957, “Algebraic logic. IV. Equality in polyadic algebras”, *Transactions of the American Mathematical Society*, 86: 1–27.

[^halmos-1962]: –––, 1962, *Algebraic logic*, New York: Chelsea Publishing Co.

[^henkin-1974]: Henkin, L. and J.D. Monk, 1974, “Cylindric algebras and related structures”, in L. Henkin et al. (eds.), *Proceedings of the Tarski Symposium*, Proceedings of Symposia in Pure Mathematics, vol. XXV, Providence, RI: American Mathematical Society, pp. 105–121.

[^henkin-1961]: Henkin, L. and A. Tarski, 1961, “Cylindric algebras”, in *Lattice Theory, Proceedings of Symposia in Pure Mathematics 2*, R. P. Dilworth (ed.), Providence, RI: American Mathematical Society, pp. 83–113.

[^hilbert-1899]: Hilbert, D., 1899, *The Foundations of Geometry*; reprinted Chicago: Open Court 1980, 2ⁿᵈ edition.

[^hilbert-1928]: Hilbert, D. and W. Ackermann, 1928, *Grundzüge der theoretischen Logik*, Berlin: Springer.

[^huntington-1904]: Huntington, E.V., 1904, “Sets of independent postulates for the algebra of logic”, *Transactions of the American Mathematical Society*, 5: 288–309.

[^huntington-1933]: –––, 1933, “New sets of independent postulates for the algebra of logic, with special reference to Whitehead and Russell’s Principia Mathematica”, *Transactions of the American Mathematical Society*, 35(1): 274–304.

[^jevons-1869]: Jevons, W.S., 1869, *The Substitution of Similars, the True Principle of Reasoning, Derived from a Modification of Aristotle’s Dictum*, London: Macmillan and Co.

[^jevons-1870]: –––, 1870, *Elementary Lessons in Logic, Deductive and Inductive*, London: Macmillan & Co.; reprinted 1957.

[^jevons-1874]: –––, 1874, *The Principles of Science, A Treatise on Logic and the Scientific Method*, London and New York: Macmillan and Co.; reprinted 1892.

[^jevons-1880]: –––, 1880, *Studies in Deductive Logic. A Manual for Students*, London and New York: Macmillan and Co.

[^jevons-1883]: –––, 1883, *The Elements of Logic*, New York and Chicago: Sheldon & Co.

[^jevons-1890]: –––, 1890, *Pure Logic and Other Minor Works*, Robert Adamson and Harriet A. Jevons (eds), New York: Lennox Hill Pub. & Dist. Co.; reprinted 1971.

[^jónsson-1951]: Jónsson, B. and A. Tarski, 1951, “Boolean Algebras with Operators. Part I”, *American Journal of Mathematics*, 73(4): 891–939.

[^kolata-1996]: Kolata, G., 1996, “Computer Math Proof Shows Reasoning Power”, *The New York Times*, December 10 (Technology Section, Cybertimes Column). [[Available Online](http://www.nytimes.com/library/cyber/week/1210math.html)]

[^löwenheim-1915]: Löwenheim, L., 1915, “Über möglichkeiten im Relativkalül”, *Mathematische Annalen*, 76(4): 447–470.

[^löwenheim-1940]: –––, 1940, “Einkleidung der Mathematik in Schröderschen Relativkalkul”, *Journal of Symbolic Logic*, 5: 1–17.

[^macfarlane-1879]: Macfarlane, A., 1879, *Principles of the Algebra of Logic. With Examples*, Edinburgh: David Douglas.

[^monk-1964]: Monk, J. D., 1964, “On Representable Relation Algebras”, *The Michigan Mathematical Journal*, 11: 207–210.

[^mostowski-1952]: Mostowski, A., 1952, “On direct products of theories”, *Journal of Symbolic Logic*, 17: 1–31.

[^peirce-1867]: Peirce, C.S., 1867, “On an Improvement in Boole’s Calculus of Logic”, *Proceedings of the American Academy of Arts and Sciences*, 7: 250–261; reprinted in Peirce 1933 [CP], vol. III, pp. 1–19.

[^peirce-1870]: Peirce, C.S., 1870, “Description of a notation for the logic of relatives, resulting from an amplification of the conceptions of Boole’s calculus of logic”, *Memoirs of the American Academy*, 9: 317–378; reprinted in *Collected Papers* 1933: Volume III, 27–98.

[^peirce-1880]: –––, 1880, “On the algebra of logic. Chapter I: Syllogistic. Chapter II: The logic of non-relative terms. Chapter III: The logic of relatives”, *American Journal of Mathematics*, 3: 15–57; reprinted in *Collected Papers* 1933: Volume III, 104–157.

[^peirce-1885]: –––, 1885, “On the Algebra of Logic: A Contribution to the Philosophy of Notation”, *American Journal of Mathematics* 7(2): 180–202; reprinted in *Collected Papers* 1933: Volume III, 359–403.

[^peirce-1933]: –––, 1933 [CP], *Collected Papers*, Charles Hartshorne and Paul Weiss (eds.), Cambridge: Harvard University Press.

[^schröder-1890]: Schröder, E., 1890–1910, *Algebra der Logik, Vols. I–III*; reprint Chelsea 1966.

[^sheffer-1913]: Sheffer, H.M., 1913, “A set of five independent postulates for Boolean algebras, with application to logical constants”, *Transactions of the American Mathematical Society*, 14(4): 481–488.

[^skolem-1919]: Skolem, T., 1919, “Untersuchungen über die Axiome des Klassenkalküls und Über Produktations- und Summationsprobleme, welche gewisse Klassen von Aussagen betreffen”, *Videnskapsselskapets skrifter, I. Matematisk-naturvidenskabelig*, klasse 3; reprinted in Skolem 1970: 66–101.

[^skolem-1920]: –––, 1920, “Logisch-kombinatorische Untersuchungen über die Erfülbarkeit oder Beweisbarkeit mathematischer Sätze nebst einem Theoreme über dichte Menge”, *Videnskapsselskapets skrifter, I. Matematisk-naturvidenskabelig*, klasse 6: 1–36.

[^skolem-1922]: –––, 1922, “Einige Bemerkungen zur axiomatischen Begrundung der Mengenlehre”, *Matematikerkongressen i Helsingfors den 4–7 Juli 1922, Den femte skandinaviska matematikerkongressen, Redogörelse*, Helsinki: Akademiska Bokhandeln; reprinted in Skolem 1970: 189–206.

[^skolem-1928]: –––, 1928, “Über die mathematische Logik”, *Norsk Mathematisk Tidsskrift*, 10: 125–142; in van Heijenoort 1967: 508–524.

[^skolem-1970]: –––, 1970, *Selected Works in Logic*, Oslo: Universitetsforlaget.

[^stone-1936]: Stone, M.H., 1936, “The theory of representations for Boolean algebras”, *Transactions of the American Mathematical Society*, 40(1): 37–111.

[^stone-1937]: –––, 1937, “Applications of the theory of Boolean rings to general topology”, *Transactions of the American Mathematical Society*, 41(3): 375–481.

[^tarski-1941]: Tarski, A., 1941, “On the calculus of relations”, *The Journal of Symbolic Logic*, 6(3): 73–89

[^tarski-1987]: Tarski, A. and S. Givant, 1987, *Set Theory Without Variables*, (Series: Colloquium Publications, Volume 1), Providence: American Mathematical Society.

[^whitehead-1910]: Whitehead, A.N., and B. Russell, 1910–1913, *Principia Mathematica I–III*, Cambridge: Cambridge University Press.

[^whitman-1941]: Whitman, P.M., 1941, “Free lattices”, *Annals of Mathematics*, second series, 42(1): 325–330.

[^wiener-1913]: Wiener, N., 1913, *A Comparison between the treatment of the algebra of relatives by Schroeder and that by Whitehead and Russell*, Ph.D. thesis, Harvard University (Norbert Wiener Papers. MC 22. Institute Archives and Special Collections, MIT Libraries, Cambridge, Massachusetts).

[^badesa-2004]: Badesa, Calixto, 2004, *The Birth of Model Theory. Löwenheim Theorem in the Frame of the Theory of Relations*, Princeton & Oxford: Princeton University Press.

[^brady-2000]: Brady, Geraldine, 2000, *From Peirce to Skolem*, Amsterdam et al.: North-Holland.

[^burris-2013]: Burris. Stanley & H.P. Sankappanavar, 2013, “The Horn Theory of Boole’s Partial Algebras”, *The Bulletin of Symbolic Logic*, 19(1): 97–105.

[^esquisabel-2012]: Esquisabel, Oscar M., 2012, “Representing and Abstracting. An Analysis of Leibniz’s Concept of Symbolic Knowledge”, in Abel Lassalle Casanave (ed.), *Symbolic Knowledge from Leibniz to Husserl*, London: College Publications, pp. 1–49.

[^gabbay-2004]: Gabbay, Dov. M. & John Woods (eds.), 2004, *Handbook of the History of Logic. Volume 3, The Rise of Modern Logic: From Leibniz to Frege*, Amsterdam et al.: Elsevier North Holland.

[^grattan-guinness-1991]: Grattan-Guinness, Ivor, 1991, “The Correspondence between George Boole and Stanley Jevons, 1863–1864”, *History and Philosophy of Logic*, 12(1): 15–35

[^grattan-guinness-2000]: –––, 2000, *The Search for Mathematical Roots,1870–1940. Logic, Set Theories and the Foundations of Mathematics from Cantor trough Russell to Gödel*, Princeton & Oxford: Princeton University Press.

[^hailperin-2004]: Hailperin, Theodore, 2004, “Algebraical Logic 1685–1900”, in Gabbay & Woods 2004: 323–388.

[^haaparanta-2009]: Haaparanta, Leila (ed.), 2009, *The Development of Modern Logic*, New York and Oxford: Oxford University Press.

[^heinemann-2015]: Heinemann, Anna-Sophie, 2015, *Quantifikation des Prädikats und numerisch definiter Syllogismus*, Münster: Mentis 2015.

[^legris-2012]: Legris, Javier, 2012, “Universale Sprache und Grundlagen der Mathematik bei Ernst Schröder”, in G. von Löffladt (ed.), *Mathematik – Logik – Philosophie. Ideen und ihre historischen Wechselwirkungen*, Frankfurt a. M.: Harri Deutsch, pp. 255–269.

[^mancosu-2009]: Mancosu, Paolo, Richard Zach, and Calixto Badesa, 2009, “The Development of Mathematical Logic from Russell to Tarski: 1900–1935”, in Haaparanta 2009: 318–471

[^peckhaus-1997]: Peckhaus, Volker, 1997, *Logik, Mathesis universalis und allgemeine Wissenschaft*, Berlin: Akademie Verlag.

[^peckhaus-2004]: –––, 2004, “Schröder’s Logic”, in Gabbay & Woods 2004: pp. 557–609.

[^peckhaus-2009]: –––, 2009, “The Mathematical Origins of Nineteenth-Century Algebra of Logic”, in Haaparanta 2009: 159–195.

[^sánchez-2004]: Sánchez Valencia, Victor, 2004, “The Algebra of Logic”, in Gabbay & Woods 2004: pp. 389–544.

[^sinaceur-1999]: Sinaceur, Hourya, 1999, *Corps et Modèles. Essai sur l’histoire de l’algèbre réelle*, 2ⁿᵈ ed., Paris: Vrin.

[^styazhkin-1969]: Styazhkin, N. I., 1969, *History of Mathematical Logic from Leibniz to Peano*, Cambridge, MA: MIT Press.

[^van-1967]: Van Heijenoort, Jean, 1967, “Logic as Calculus and Logic as Language”, *Synthese*, 17: 324–330
