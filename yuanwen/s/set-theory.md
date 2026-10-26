# Set Theory
**First published Wed Oct 8, 2014; substantive revision Tue Jan 31, 2023**

*Bagaria, Joan*

## 1. The origins

Set theory, as a separate mathematical discipline, begins in the work of Georg Cantor. One might say that set theory was born in late 1873, when he made the amazing discovery that the linear continuum, that is, the real line, is not countable, meaning that its points cannot be counted using the natural numbers. So, even though the set of natural numbers and the set of real numbers are both infinite, there are more real numbers than there are natural numbers, which opened the door to the investigation of the different sizes of infinity. See the entry on the early development of set theory for a discussion of the origin of set-theoretic ideas and their use by different mathematicians and philosophers before and around Cantor’s time.

According to Cantor, two sets \(A\) and \(B\) have the same size, or *cardinality*, if they are bijectable, i.e., the elements of \(A\) can be put in a one-to-one correspondence with the elements of \(B\). Thus, the set \(\mathbb{N}\) of natural numbers and the set \(\mathbb{R}\) of real numbers have different cardinalities. In 1878 Cantor formulated the famous *Continuum Hypothesis* (CH), which asserts that every infinite set of real numbers is either countable, i.e., it has the same cardinality as \(\mathbb{N}\), or has the same cardinality as \(\mathbb{R}\). In other words, there are only two possible sizes of infinite sets of real numbers. The CH is the most famous problem of set theory. Cantor himself devoted much effort to it, and so did many other leading mathematicians of the first half of the twentieth century, such as Hilbert, who listed the CH as the first problem in his celebrated list of 10 (later expanded to 23 in the published version) unsolved mathematical problems presented in 1900 at the Second International Congress of Mathematicians, in Paris. The attempts to prove the CH led to major discoveries in set theory, such as the theory of constructible sets, and the forcing technique, which showed that the CH can neither be proved nor disproved from the usual axioms of set theory. To this day, the CH remains open.

Early on, some inconsistencies, or paradoxes, arose from a naive use of the notion of set; in particular, from the deceivingly natural assumption that every property determines a set, namely the set of objects that have the property. One example is *Russell’s Paradox*, also known to Zermelo:

> consider the property of sets of not being members of themselves. If the property determines a set, call it \(A\), then \(A\) is a member of itself if and only if \(A\) is not a member of itself.

Thus, some collections, like the collection of all sets, the collection of all ordinals numbers, or the collection of all cardinal numbers, are not sets. Such collections are called *proper classes*.

In order to avoid the paradoxes and put it on a firm footing, set theory had to be axiomatized. The first axiomatization was due to Zermelo (1908) and it came as a result of the need to spell out the basic set-theoretic principles underlying his proof of Cantor’s Well-Ordering Principle. Zermelo’s axiomatization avoids Russell’s Paradox by means of the Separation axiom, which is formulated as quantifying over properties of sets, and thus it is a second-order statement. Further work by Skolem and Fraenkel led to the formalization of the Separation axiom in terms of formulas of first-order, instead of the informal notion of property, as well as to the introduction of the axiom of Replacement, which is also formulated as an axiom schema for first-order formulas (see next section). The axiom of Replacement is needed for a proper development of the theory of transfinite ordinals and cardinals, using transfinite recursion (see Section 3). It is also needed to prove the existence of such simple sets as the set of hereditarily finite sets, i.e., those finite sets whose elements are finite, the elements of which are also finite, and so on; or to prove basic set-theoretic facts such as that every set is contained in a transitive set, i.e., a set that contains all elements of its elements (see Mathias 2001 for the weaknesses of Zermelo set theory)[^mathias-2001]. A further addition, by von Neumann, of the axiom of Foundation, led to the standard axiom system of set theory, known as the Zermelo-Fraenkel axioms plus the Axiom of Choice, or ZFC.

Other axiomatizations of set theory, such as those of von Neumann-Bernays-Gödel (NBG), or Morse-Kelley (MK), allow also for a formal treatment of proper classes.

## 2. The axioms of set theory

ZFC is an axiom system formulated in first-order logic with equality and with only one binary relation symbol \(\in\) for membership. Thus, we write \(A\in B\) to express that \(A\) is a member of the set \(B\). See the

[Supplement on Basic Set Theory](set-theory.basic-set-theory.md)

for further details. See also the

[Supplement on Zermelo-Fraenkel Set Theory](set-theory.ZF.md)

for a formalized version of the axioms and further comments. We state below the axioms of ZFC informally.

### 2.1 The axioms of ZFC

- *Extensionality*: If two sets \(A\) and \(B\) have the same elements, then they are equal.
- *Null Set*: There exists a set, denoted by \({\varnothing}\) and called the *empty set*, which has no elements.
- *Pair*: Given any sets \(A\) and \(B\), there exists a set, denoted by \(\{ A,B\}\), which contains \(A\) and \(B\) as its only elements. In particular, there exists the set \(\{ A\}\) which has \(A\) as its only element.
- *Power Set*: For every set \(A\) there exists a set, denoted by \(\mathcal{P}(A)\) and called the *power set* of \(A\), whose elements are all the subsets of \(A\).
- *Union*: For every set \(A\), there exists a set, denoted by \(\bigcup A\) and called the *union* of \(A\), whose elements are all the elements of the elements of \(A\).
- *Infinity:* There exists an infinite set. In particular, there exists a set \(Z\) that contains \({\varnothing}\) and such that if \(A\in Z\), then \(\bigcup\{ A, \{ A\}\}\in Z\).
- *Separation*: For every set \(A\) and every given property, there is a set containing exactly the elements of \(A\) that have that property. A *property* is given by a formula \(\varphi\) of the first-order language of set theory. Thus, Separation is not a single axiom but an axiom schema, that is, an infinite list of axioms, one for each formula \(\varphi\).
- *Replacement*: For every given *definable function* with domain a set \(A\), there is a set whose elements are all the values of the function. Replacement is also an axiom schema, as definable functions are given by formulas.
- *Foundation*: Every non-empty set \(A\) contains an \(\in\)-minimal element, that is, an element such that no element of \(A\) belongs to it.

These are the axioms of Zermelo-Fraenkel set theory, or ZF. The axioms of Null Set and Pair follow from the other ZF axioms, so they may be omitted. Also, Replacement implies Separation.

Finally, there is the Axiom of Choice (AC):

- *Choice:* For every set \(A\) of pairwise-disjoint non-empty sets, there exists a set that contains exactly one element from each set in \(A\).

The AC was, for a long time, a controversial axiom. On the one hand, it is very useful and of wide use in mathematics. On the other hand, it has rather unintuitive consequences, such as the Banach-Tarski Paradox, which says that the unit ball can be partitioned into finitely-many pieces, which can then be rearranged to form two unit balls. The objections to the axiom arise from the fact that it asserts the existence of sets that cannot be explicitly defined. But Gödel’s 1938 proof of its consistency, relative to the consistency of ZF, dispelled any suspicions left about it.

The Axiom of Choice is equivalent, modulo ZF, to the *Well-ordering Principle*, which asserts that every set can be well-ordered, i.e., it can be linearly ordered so that every non-empty subset has a minimal element.

Although not formally necessary, besides the symbol \(\in\) one normally uses for convenience other auxiliary defined symbols. For example, \(A\subseteq B\) expresses that \(A\) is a *subset* of \(B\), i.e., every member of \(A\) is a member of \(B\). Other symbols are used to denote sets obtained by performing basic operations, such as \(A\cup B\), which denotes the *union* of \(A\) and \(B\), i.e., the set whose elements are those of \(A\) and \(B\); or \(A\cap
B\), which denotes the *intersection* of \(A\) and \(B\), i.e., the set whose elements are those common to \(A\) and \(B\). The *ordered pair* \((A,B)\) is defined as the set \(\{ \{ A\},\{
A,B\}\}\). Thus, two ordered pairs \((A,B)\) and \((C,D)\) are equal if and only if \(A=C\) and \(B=D\). And the *Cartesian product* \(A\times B\) is defined as the set of all ordered pairs \((C,D)\) such that \(C\in A\) and \(D\in B\). Given any formula \(\varphi(x,y_1,\ldots ,y_n)\), and sets \(A,B_1,\ldots ,B_n\), by the axiom of Separation one can form the set of all those elements of \(A\) that satisfy the formula \(\varphi(x,B_1,\ldots ,B_n)\). This set is denoted by \(\{ a\in A: \varphi(a,B_1,\ldots ,B_n)\}\). In ZF one can easily prove that all these sets exist. See the [Supplement on Basic Set Theory](set-theory.basic-set-theory.md) for further discussion.

## 3. The theory of transfinite ordinals and cardinals

In ZFC one can develop the Cantorian theory of transfinite (i.e., infinite) ordinal and cardinal numbers. Following the definition given by Von Neumann in the early 1920s, the ordinal numbers, or *ordinals*, for short, are obtained by starting with the empty set and performing two operations: taking the immediate successor, and passing to the limit. Thus, the first ordinal number is \({\varnothing}\). Given an ordinal \(\alpha\), its *immediate successor*, denoted by \(\alpha +1\), is the set \(\alpha \cup \{
\alpha \}\). And given a non-empty set \(X\) of ordinals such that for every \(\alpha \in X\) the successor \(\alpha +1\) is also in \(X\), one obtains the *limit ordinal* \(\bigcup X\). One shows that every ordinal is (strictly) well-ordered by \(\in\), i.e., it is linearly ordered by \(\in\) and there is no infinite \(\in\)-descending sequence. Also, every well-ordered set is isomorphic to a unique ordinal, called its *order-type*.

Note that every ordinal is the set of its predecessors. However, the class \(ON\) of all ordinals is not a set. Otherwise, \(ON\) would be an ordinal greater than all the ordinals, which is impossible. The first infinite ordinal, which is the set of all finite ordinals, is denoted by the Greek letter omega (\(\omega\)). In ZFC, one identifies the finite ordinals with the natural numbers. Thus, \({\varnothing}=0\), \(\{ {\varnothing}\}=1\), \(\{ {\varnothing}, \{
{\varnothing}\}\}=2\), etc., hence \(\omega\) is just the set \(\mathbb{N}\) of natural numbers.

One can extend the operations of addition and multiplication of natural numbers to all the ordinals. For example, the ordinal \(\alpha
+\beta\) is the order-type of the well-ordering obtained by concatenating a well-ordered set of order-type \(\alpha\) and a well-ordered set of order-type \(\beta\). The sequence of ordinals, well-ordered by \(\in\), starts as follows

> 0, 1, 2,…, \(n\),…, \(\omega\), \(\omega+1\), \(\omega+2\),…, \(\omega +\omega\),…, \(\omega \cdot
n\), …, \(\omega \cdot \omega\),…, \(\omega^n\), …, \(\omega^\omega\), …

The ordinals satisfy the principle of *transfinite induction*: suppose that \(C\) is a class of ordinals such that whenever \(C\) contains all ordinals \(\beta\) smaller than some ordinal \(\alpha\), then \(\alpha\) is also in \(C\). Then the class \(C\) contains all ordinals. Using transfinite induction one can prove in ZFC (and one needs the axiom of Replacement) the important principle of *transfinite recursion*, which says that, given any definable class-function \(G\) (namely a definable operation that takes any set \(x\) to a set \(G(x)\)), one can define a class-function \(F\) with domain the class \(ON\) of ordinals, such that \(F(\alpha)\) is the value of the function \(G\) applied to the function \(F\) restricted to \(\alpha\). One uses transfinite recursion, for example, in order to define properly the arithmetical operations of addition, product, and exponentiation on the ordinals.

Recall that an infinite set is *countable* if it is bijectable, i.e., it can be put into a one-to-one correspondence, with \(\omega\). All the ordinals displayed above are either finite or countable. But the set of all finite and countable ordinals is also an ordinal, called \(\omega_1\), and is not countable. Similarly, the set of all ordinals that are bijectable with some ordinal less than or equal to \(\omega_1\) is also an ordinal, called \(\omega_2\), and is not bijectable with \(\omega_1\), and so on.

### 3.1 Cardinals

A *cardinal* is an ordinal that is not bijectable with any smaller ordinal. Thus, every finite ordinal is a cardinal, and \(\omega\), \(\omega_1\), \(\omega_2\), etc. are also cardinals. The infinite cardinals are represented by the letter aleph (\(\aleph\)) of the Hebrew alphabet, and their sequence is indexed by the ordinals. It starts like this

> \(\aleph_0\), \(\aleph_1\), \(\aleph_2\), …, \(\aleph_\omega\), \(\aleph_{\omega +1}\), …, \(\aleph_{\omega +\omega}\), …, \(\aleph_{\omega^2}\), …, \(\aleph_{\omega^\omega}\), …, \(\aleph_{\omega_1}\), …, \(\aleph_{\omega_2}\), …

Thus, \(\omega=\aleph_0\), \(\omega_1=\aleph_1\), \(\omega_2=\aleph_2\), etc. For every cardinal there is a bigger one, and the limit of an increasing sequence of cardinals is also a cardinal. Thus, the class of all cardinals is not a set, but a proper class.

An infinite cardinal \(\kappa\) is called *regular* if it is not the union of less than \(\kappa\) smaller cardinals. Thus, \(\aleph_0\) is regular, and so are all infinite successor cardinals, such as \(\aleph_1\). Non-regular infinite cardinals are called *singular*. The first singular cardinal is \(\aleph_\omega\), as it is the union of countably-many smaller cardinals, namely \(\aleph_\omega =\bigcup \{\aleph_n : n&lt;\omega\} \).

The *cofinality* of a cardinal \(\kappa\), denoted by \(cf(\kappa)\) is the smallest cardinal \(\lambda\) such that \(\kappa\) is the union of \(\lambda\)-many smaller ordinals. Thus, \(cf(\aleph_\omega)=\aleph_0\).

By the AC (in the form of the Well-Ordering Principle), every set \(A\) can be well-ordered, hence it is bijectable with a unique cardinal, called the *cardinality* of \(A\). Given two cardinals \(\kappa\) and \(\lambda\), the sum \(\kappa +\lambda\) is defined as the cardinality of the set consisting of the union of any two disjoint sets, one of cardinality \(\kappa\) and one of cardinality \(\lambda\). And the product \(\kappa \cdot \lambda\) is defined as the cardinality of the Cartesian product \(\kappa \times
\lambda\). The operations of sum and product of infinite cardinals are trivial, for if \(\kappa\) and \(\lambda\) are infinite cardinals, then \(\kappa +\lambda =\kappa \cdot \lambda = maximum \{ \kappa
,\lambda\}\).

In contrast, cardinal exponentiation is highly non-trivial, for even the value of the simplest non-trivial infinite exponential, namely \(2^{\aleph_0}\), is not known and cannot be determined in ZFC (see below). The cardinal \(\kappa^\lambda\) is defined as the cardinality of the Cartesian product of \(\lambda\) copies of \(\kappa\); equivalently, as the cardinality of the set of all functions from \(\lambda\) into \(\kappa\). König’s theorem asserts that \(\kappa^{cf(\kappa)}&gt;\kappa\), which implies that the cofinality of the cardinal \(2^{\aleph_0}\), whatever that cardinal is, must be uncountable. But this is essentially all that ZFC can prove about the value of the exponential \(2^{\aleph_0}\).

In the case of exponentiation of singular cardinals, ZFC has a lot more to say. In 1989, Shelah proved the remarkable result that if \(\aleph_\omega\) is a strong limit, that is, \(2^{\aleph_n}&lt;\aleph_\omega\), for every \(n&lt;\omega\), then \(2^{\aleph_\omega}&lt;\aleph_{\omega_4}\) (see Shelah (1994)). The technique developed by Shelah to prove this and similar theorems, in ZFC, is called *pcf theory* (for *possible cofinalities*), and has found many applications in other areas of mathematics.

## 4. The universe \(V\) of all sets

*A posteriori*, the ZF axioms other than Extensionality—which needs no justification because it just states a defining property of sets—may be justified by their use in building the *cumulative hierarchy of sets*. Namely, in ZF we define using transfinite recursion the class-function that assigns to each ordinal \(\alpha\) the set \(V_\alpha\), given as follows:

- \(V_0={\varnothing}\)
- \(V_{\alpha +1}=\mathcal{P}(V_\alpha)\)
- \(V_\alpha =\bigcup \{ V_\beta : \beta &lt;\alpha \}\), whenever \(\alpha\) is a limit ordinal.

The Power Set axiom is used to obtain \(V_{\alpha +1}\) from \(V_\alpha\). Replacement and Union allow one to form \(V_\alpha\) for \(\alpha\) a limit ordinal. Indeed, consider the function that assigns to each \(\beta &lt;\alpha\) the set \(V_\beta\). By Replacement, the collection of all the \(V_\beta\), for \(\beta &lt;\alpha\), is a set, hence the Union axiom applied to that set yields \(V_\alpha\). The axiom of Infinity is needed to prove the existence of \(\omega\) and hence of the transfinite sequence of ordinals. Finally, the axiom of Foundation is equivalent, assuming the other axioms, to the statement that every set belongs to some \(V_\alpha\), for some ordinal \(\alpha\). Thus, ZF proves that the set theoretic universe, denoted by \(V\), is the union of all the \(V_\alpha\), \(\alpha\) an ordinal.

The proper class \(V\), together with the \(\in\) relation, satisfies all the ZFC axioms, and is thus a model of ZFC. It is the intended model of ZFC, and one may think of ZFC as providing a description of \(V\), a description however that is highly incomplete, as we shall see below.

One important property of \(V\) is the so-called *Reflection Principle*. Namely, for each formula \(\varphi(x_1,\ldots ,x_n)\), ZFC proves that there exists some \(V_\alpha\) that reflects it, that is, for every \(a_1,\ldots,a_n\in V_\alpha\),

> \(\varphi(a_1,\ldots ,a_n)\) holds in \(V\) if and only if \(\varphi(a_1,\ldots,a_n)\) holds in \(V_\alpha\).

Thus, \(V\) cannot be characterized by any sentence, as any sentence that is true in \(V\) must be also true in some initial segment \(V_\alpha\). In particular, ZFC is not finitely axiomatizable, for otherwise ZFC would prove that, for unboundedly many ordinals \(\alpha\), \(V_\alpha\) is a model of ZFC, contradicting Gödel’s second incompleteness theorem (see Section 5.2).

The Reflection Principle encapsulates the essence of ZF set theory, for as shown by Levy (1960), the axioms of Extensionality, Separation, and Foundation, together with the Reflection Principle, formulated as the axiom schema asserting that each formula is reflected by some set that contains all elements and all subsets of its elements (note that the \(V_\alpha\) are like this), is equivalent to ZF.

## 5. Set theory as the foundation of mathematics

Every mathematical object may be viewed as a set. For example, the natural numbers are identified with the finite ordinals, so \(\mathbb{N}=\omega\). The set of integers \(\mathbb{Z}\) may be defined as the set of equivalence classes of pairs of natural numbers under the equivalence relation \((n, m)\equiv (n',m')\) if and only if \(n+m'=m+n'\). By identifying every natural number \(n\) with the equivalence class of the pair \((n,0)\), one may extend naturally the operations of sum and product of natural numbers to \(\mathbb{Z}\) (see Enderton (1977) for details, and Levy (1979) for a different construction). Further, one may define the rationals \(\mathbb{Q}\) as the set of equivalence classes of pairs \((n,m)\) of integers, where \(m\ne 0\), under the equivalence relation \((n,m)\equiv (n',m')\) if and only if \(n\cdot m'=m\cdot n'\). Again, the operations \(+\) and \(\cdot\) on \(\mathbb{Z}\) may be extended naturally to \(\mathbb{Q}\). Moreover, the ordering \(\leq_{\mathbb{Q}}\) on the rationals is given by: \(r \leq_{\mathbb{Q}} s\) if and only if there exists \(t\in \mathbb{Q}\) such that \(s=r+t\). The real numbers may be defined as Dedekind cuts of \(\mathbb{Q}\), namely, a real number is given by a pair \((A,B)\) of non-empty disjoint sets such that \(A\cup B=\mathbb{Q}\), \(A\) has no greatest element, and \(a
\lt_{\mathbb{Q}} b\) for every \(a\in A\) and \(b\in B\). One can then extend again the operations of \(+\) and \(\cdot\) on \(\mathbb{Q}\), as well as the ordering \(\leq_{\mathbb{Q}}\), to the set of real numbers \(\mathbb{R}\).

Let us emphasize that it is not claimed that, e.g., real numbers *are* Dedekind cuts of rationals, as they could also be defined using Cauchy sequences, or in other different ways. What is important, from a foundational point of view, is that the set-theoretic version of \(\mathbb{R}\), together with the usual algebraic operations, satisfies the categorical axioms that the real numbers satisfy, namely those of a complete ordered field. The metaphysical question of what the real numbers really are is irrelevant here.

Algebraic structures can also be viewed as sets, as any \(n\)-ary relation on the elements of a set \(A\) can be viewed as a set of ordered \(n\)-tuples \((a_1,\ldots ,a_n)\) of elements of \(A\). And any \(n\)-ary function \(f\) on \(A\), with values on some set \(B\), can be seen as the set of ordered \(n+1\)-tuples \(((a_1,\ldots
,a_n),b)\) such that \(b\) is the value of \(f\) on \((a_1,\ldots
,a_m)\). Thus, for example, a *group* is just a triple \((A, +,
0)\), where \(A\) is a non-empty set, \(+\) is a binary function on \(A\) that is associative, \(0\) is an element of \(A\) such that \(a+0=0+a=a\), for all \(a\in A\), and for every \(a\in A\) there is an element of \(A\), denoted by \(-a\), such that \(a+(-a)=(-a)+a=0\). Also, a *topological space* is just a set \(X\) together with a topology \(\tau\) on it, i.e., \(\tau\) is a subset of \(\mathcal{P}(X)\) containing \(X\) and \({\varnothing}\), and closed under arbitrary unions and finite intersections. Any mathematical object whatsoever can always be viewed as a set, or a proper class. The properties of the object can then be expressed in the language of set theory. Any mathematical statement can be formalized into the language of set theory, and any mathematical theorem can be derived, using the calculus of first-order logic, from the axioms of ZFC, or from some extension of ZFC. It is in this sense that set theory provides a foundation for mathematics.

The foundational role of set theory for mathematics, while significant, is by no means the only justification for its study. The ideas and techniques developed within set theory, such as infinite combinatorics, forcing, or the theory of large cardinals, have turned it into a deep and fascinating mathematical theory, worthy of study by itself, and with important applications to practically all areas of mathematics.

### 5.1 Metamathematics

The remarkable fact that virtually all of mathematics can be formalized within ZFC, makes possible a mathematical study of mathematics itself. Thus, any questions about the existence of some mathematical object, or the provability of a conjecture or hypothesis can be given a mathematically precise formulation. This makes *metamathematics* possible, namely the mathematical study of mathematics itself. So, the question about the provability or unprovability of any given mathematical statement becomes a sensible mathematical question. When faced with an open mathematical problem or conjecture, it makes sense to ask for its provability or unprovability in the ZFC formal system. Unfortunately, the answer may be neither, because ZFC, if consistent, is incomplete.

### 5.2 The incompleteness phenomenon

Gödel’s completeness theorem for first-order logic implies that ZFC is *consistent*—i.e., no contradiction can be derived from it—if and only if it has a model. A *model* of ZFC is a pair \((M,E)\), where \(M\) is a non-empty set and \(E\) is a binary relation on \(M\) such that all the axioms of ZFC are true when interpreted in \((M,E)\), i.e., when the variables that appear in the axioms range over elements of \(M\), and \(\in\) is interpreted as \(E\). Thus, if \(\varphi\) is a sentence of the language of set theory and one can find a model of ZFC in which \(\varphi\) holds, then its negation \(\neg \varphi\) cannot be proved in ZFC. Hence, if one can find a model of \(\varphi\) and also a model of \(\neg
\varphi\), then \(\varphi\) is neither provable nor disprovable in ZFC, in which case we say that \(\varphi\) is *undecidable* in, or *independent* of, ZFC.

In 1931, Gödel announced his striking incompleteness theorems, which assert that any reasonable formal system for mathematics is necessarily incomplete. In particular, if ZFC is consistent, then there are propositions in the language of set theory that are undecidable in ZFC. Moreover, Gödel’s second incompleteness theorem implies that the formal (arithmetical) statement \(CON(ZFC)\), which asserts that ZFC is consistent, while true, cannot be proved in ZFC. And neither can its negation. Thus, \(CON(ZFC)\) is undecidable in ZFC.

If ZFC is consistent, then it cannot prove the existence of a model of ZFC, for otherwise ZFC would prove its own consistency. Thus, a proof of consistency or of undecidability of a given sentence \(\varphi\) is always a *relative consistency* proof. That is, one assumes that ZFC is consistent, hence it has a model, and then one constructs another model of ZFC where the sentence \(\varphi\) is true. We shall see several examples in the next sections.

## 6. The set theory of the continuum

From Cantor and until about 1940, set theory developed mostly around the study of the continuum, that is, the real line \(\mathbb{R}\). The main topic was the study of the so-called regularity properties, as well as other structural properties, of simply-definable sets of real numbers, an area of mathematics that is known as *Descriptive Set Theory*.

### 6.1 Descriptive Set Theory

Descriptive Set Theory is the study of the properties and structure of definable sets of real numbers and, more generally, of definable subsets of \(\mathbb{R}^n\) and other *Polish spaces* (i.e., topological spaces that are homeomorphic to a separable complete metric space), such as the *Baire space* \(\mathcal{N}\) of all functions \(f:\mathbb{N} \to \mathbb{N}\), the space of complex numbers, Hilbert space, and separable Banach spaces. The simplest sets of real numbers are the basic open sets (i.e., the open intervals with rational endpoints), and their complements. The sets that are obtained in a countable number of steps by starting from the basic open sets and applying the operations of taking the complement and forming a countable union of previously obtained sets are the *Borel sets*. All Borel sets are *regular*, that is, they enjoy all the classical *regularity properties*. One example of a regularity property is the *Lebesgue measurability*: a set of reals is Lebesgue measurable if it differs from a Borel set by a null set, namely, a set that can be covered by sets of basic open intervals of arbitrarily-small total length. Thus, trivially, every Borel set is Lebesgue measurable, but sets more complicated than the Borel ones may not be. Other classical regularity properties are the *Baire property* (a set of reals has the Baire property if it differs from an open set by a meager set, namely, a set that is a countable union of sets that are not dense in any interval), and the *perfect set property* (a set of reals has the perfect set property if it is either countable or contains a perfect set, namely, a nonempty closed set with no isolated points). In ZFC one can prove that there exist non-regular sets of reals, but the AC is necessary for this (Solovay 1970)[^solovay-1970].

The *analytic sets*, also called \(\mathbf{\Sigma}^1_1\), are the continuous images of Borel sets. And the *co-analytic*, or \(\mathbf{\Pi}^1_1\), sets are the complements of analytic sets.

Starting from the analytic (or the co-analytic) sets and applying the operations of projection (from the product space \(\mathbb{R}\times
\mathcal{N}\) to \(\mathbb{R}\)) and complementation, one obtains the *projective sets*. The projective sets form a hierarchy of increasing complexity. For example, if \(A\subseteq \mathbb{R}\times
\mathcal{N}\) is co-analytic, then the projection \(\{ x\in
\mathbb{R}: \exists y\in \mathcal{N}((x,y)\in A)\}\) is a projective set in the next level of complexity above the co-analytic sets. Those sets are called \(\mathbf{\Sigma}^1_2\), and their complements are called \(\mathbf{\Pi}^1_2\).

The projective sets come up very naturally in mathematical practice, for it turns out that a set \(A\) of reals is projective if and only if it is definable in the structure

\[\mathcal{R}=(\mathbb{R}, +,\cdot ,\mathbb{Z}).\]

That is, there is a first-order formula \(\varphi ( x, y_1,\ldots,
y_n)\) in the language for the structure such that for some \(r_1,\ldots ,r_n\in \mathbb{R}\),

\[A=\{ x\in \mathbb{R}: \mathcal{R}\models \varphi(x,r_1,\ldots
,r_n)\}.\]

ZFC proves that every analytic set, and therefore every co-analytic set, is Lebesgue measurable and has the Baire property. It also proves that every analytic set has the perfect set property. But the perfect set property for co-analytic sets implies that the first uncountable cardinal, \(\aleph_1\), is a large cardinal in the constructible universe \(L\) (see Section 7), namely a so-called inaccessible cardinal (see Section 10), which implies that one cannot prove in ZFC that every co-analytic set has the perfect set property.

The theory of projective sets of complexity greater than co-analytic is completely undetermined by ZFC. For example, in \(L\) there is a \(\mathbf{\Sigma}^1_2\) set that is not Lebesgue measurable and does not have the Baire property, whereas if Martin’s axiom holds (see Section 11), every such set has those regularity properties. There is, however, an axiom, called the axiom of Projective Determinacy, or PD, that is consistent with ZFC, modulo the consistency of some large cardinals (in fact, it follows from the existence of some large cardinals), and implies that all projective sets are regular. Moreover, PD settles essentially all questions about the projective sets. See the entry on large cardinals and determinacy for further details.

### 6.2 Determinacy

A regularity property of sets that subsumes all other classical regularity properties is that of being *determined*. For simplicity, we shall work with the Baire space \(\mathcal{N}\). Recall that the elements of \(\mathcal{N}\) are functions \(f:\mathbb{N} \to
\mathbb{N}\), that is, sequences of natural numbers of length \(\omega\). The space \(\mathcal{N}\) is topologically equivalent (i.e., homeomorphic) to the set of irrational points of \(\mathbb{R}\). So, since we are interested in the regularity properties of subsets of \(\mathbb{R}\), and since countable sets, such as the set of rationals, are negligible in terms of those properties, we may as well work with \(\mathcal{N}\), instead of \(\mathbb{R}\).

Given \(A\subseteq \mathcal{N}\), the *game* associated to \(A\), denoted by \({\mathcal G}_A\), has two players, I and II, who play alternatively \(n_i\in \mathbb{N}\): I plays \(n_0\), then II plays \(n_1\), then I plays \(n_2\), and so on. So, at stage \(2k\), player I plays \(n_{2k}\) and at stage \(2k+1\), player II plays \(n_{2k+1} \). We may visualize a run of the game as follows:

| \(\mathbf{I}\) | \(n_0\) |   | \(n_2\) |   | \(n_4\) |   | \(\cdots\) |   | \(n_{2k}\) |   | \(\cdots\) |   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| \(\mathbf{II}\) |   | \(n_1\) |   | \(n_3\) |   | \(\cdots\) |   | \(\cdots\) |   | \(n_{2k+1}\) |   | \(\cdots\) |

After infinitely many moves, the two players produce an infinite sequence \(n_0, n_1,n_2,\ldots\) of natural numbers. Player I wins the game if the sequence belongs to \(A\). Otherwise, player II wins.

The game \({\mathcal{G}}_A\) is *determined* if there is a winning strategy for one of the players. A *winning strategy* for one of the players, say for player II, is a function \(\sigma\) from the set of finite sequences of natural numbers into \(\mathbb{N}\), such that if the player plays according to this function, i.e., she plays \(\sigma (n_0,\ldots ,n_{2k})\) at the \(k\)-th turn, she will always win the game, no matter what the other player does.

We say that a subset \(A\) of \(\mathcal{N}\) is *determined* if and only if the game \({\mathcal{G}}_A\) is determined.

One can prove in ZFC—and the use of the AC is necessary—that there are non-determined sets. Thus, the *Axiom of Determinacy* (AD), which asserts that all subsets of \(\mathcal{N}\) are determined, is incompatible with the AC. But Donald Martin proved, in ZFC, that every Borel set is determined. Further, he showed that if there exists a large cardinal called measurable (see Section 10), then even the analytic sets are determined. The axiom of *Projective Determinacy* (PD) asserts that every projective set is determined. It turns out that PD implies that all projective sets of reals are regular, and Woodin has shown that, in a certain sense, PD settles essentially all questions about the projective sets. Moreover, PD seems to be necessary for this. Another axiom, \(AD^{L(\Bbb R )}\), asserts that the AD holds in \(L(\Bbb R)\), which is the least transitive class that contains all the ordinals and all the real numbers, and satisfies the ZF axioms (see Section 7). So, \(AD^{L(\Bbb R )}\) implies that every set of reals that belongs to \(L(\Bbb R)\) is regular. Also, since \(L(\Bbb R)\) contains all projective sets, \(AD^{L(\Bbb R )}\) implies PD.

### 6.3 The Continuum Hypothesis

The Continuum Hypothesis (CH), formulated by Cantor in 1878, asserts that every infinite set of real numbers has cardinality either \(\aleph_0\) or the same cardinality as \(\mathbb{R}\). Thus, the CH is equivalent to \(2^{\aleph_0}=\aleph_1\).

Cantor proved in 1883 that closed sets of real numbers have the perfect set property, from which it follows that every uncountable closed set of real numbers has the same cardinality as \(\mathbb{R}\). Thus, the CH holds for closed sets. More than thirty years later, Pavel Aleksandrov extended the result to all Borel sets, and then Mikhail Suslin to all analytic sets. Thus, all analytic sets satisfy the CH. However, the efforts to prove that co-analytic sets satisfy the CH would not succeed, as this is not provable in ZFC.

In 1938 Gödel proved the consistency of the CH with ZFC. Assuming that ZF is consistent, he built a model of ZFC, known as the *constructible universe*, in which the CH holds. Thus, the proof shows that if ZF is consistent, then so is ZF together with the AC and the CH. Hence, assuming ZF is consistent, the AC cannot be disproved in ZF and the CH cannot be disproved in ZFC.

See the entry on the continuum hypothesis for the current status of the problem.

## 7. Gödel’s constructible universe

Gödel’s constructible universe, denoted by \(L\), is defined by transfinite recursion on the ordinals, similarly as \(V\), but at successor steps, instead of taking the power set of \(V_\alpha\) to obtain \(V_{\alpha +1}\), one only takes the set of those subsets of \(L_\alpha\) that are definable in \(L_\alpha\), using elements of \(L_\alpha\) as parameters. Thus, letting \(\mathcal{P}^{Def}(X)\) to denote the set of all the subsets of \(X\) that are definable in the structure \((X,\in )\) by a formula of the language of set theory, using elements of \(X\) as parameters of the definition, we let

- \(L_0={\varnothing}\)
- \(L_{\alpha +1}=\mathcal{P}^{Def}(L_\alpha)\)
- \(L_\lambda =\bigcup \{L_\alpha :\alpha &lt;\lambda\}\), whenever \(\lambda\) is a limit ordinal.

Then \(L\) is the union of all the \(L_\alpha\), for \(\alpha\) an ordinal.

Gödel showed that \(L\) satisfies all the ZFC axioms, and also the CH. In fact, it satisfies the *Generalized Continuum Hypothesis* (GCH), namely \(2^{\aleph_\alpha}=\aleph_{\alpha
+1}\), for every ordinal \(\alpha\).

The statement \(V=L\), called the *axiom of constructibility*, asserts that every set belongs to \(L\). It holds in \(L\), hence it is consistent with ZFC, and implies both the AC and the GCH.

The proper class \(L\), together with the \(\in\) relation restricted to \(L\), is an *inner model* of ZFC, that is, a *transitive* (i.e., it contains all elements of its elements) class that contains all ordinals and satisfies all the ZFC axioms. It is in fact the smallest inner model of ZFC, as any other inner model contains it.

More generally, given any set \(A\), one can build the smallest transitive model of ZF that contains \(A\) and all the ordinals in a similar manner as \(L\), but now starting with the transitive closure of \(\{A \}\), i.e., the smallest transitive set that contains \(A\), instead of \({\varnothing}\). The resulting model, \(L(A)\), need not be however a model of the AC. One very important such model is \(L(\mathbb{R})\), the smallest transitive model of ZF that contains all the ordinals and all the real numbers.

The theory of constructible sets owes much to the work of Ronald Jensen. He developed the so-called *fine structure* theory of \(L\) and isolated some combinatorial principles, such as the diamond (\(\diamondsuit\)) and square (\(\Box\)), which can be used to carry out complicated constructions of uncountable mathematical objects. Fine structure theory plays also an important role in the analysis of bigger \(L\)-like models, such as \(L(\mathbb{R})\) or the inner models for large cardinals (see Section 10.1).

## 8. Forcing

In 1963, twenty-five years after Gödel’s proof of the consistency of the CH and the AC, relative to the consistency of ZF, Paul Cohen (1966) proved the consistency of the negation of the CH, and also of the negation of the AC, relative to the consistency of ZF. Thus, if ZF is consistent, then the CH is undecidable in ZFC, and the AC is undecidable in ZF. To achieve this, Cohen devised a new and extremely powerful technique, called *forcing*, for expanding countable transitive models of ZF, or of ZFC.

Since the axiom \(V=L\) implies the AC and the CH, any model of the negation of the AC or the CH must violate \(V=L\). So, let’s illustrate the idea of forcing in the case of building a model for the negation of \(V=L\). We start with a transitive model \(M\) of ZFC, which we may assume, without loss of generality, to be a model of \(V=L\). To violate \(V=L\) we need to expand \(M\) by adding a new set \(r\) so that, in the expanded model, \(r\) will be non-constructible. Since all hereditarily-finite sets are constructible, we aim to add an infinite set of natural numbers. The first problem we face is that \(M\) may contain already all subsets of \(\omega\). Fortunately, by the Löwenheim-Skolem theorem for first-order logic, \(M\) has an elementary submodel which is isomorphic to a countable transitive model \(N\). So, since we are only interested in the statements that hold in \(M\), and not in \(M\) itself, we may as well work with \(N\) instead of \(M\), and so we may assume that \(M\) itself is countable. Then, since \(\mathcal{P}(\omega)\) is uncountable, there are plenty of subsets of \(\omega\) that do not belong to \(M\). But, unfortunately, we cannot just pick any infinite subset \(r\) of \(\omega\) that does not belong to \(M\) and add it to \(M\). The reason is that \(r\) may encode a lot of information, so that when added to \(M\), \(M\) is no longer a model of ZF, or it is still a model of \(V=L\). To avoid this, one needs to pick \(r\) with great care. The idea is to pick \(r\) *generic* over \(M\), meaning that \(r\) is built from its finite approximations in such a way that it does not have any property that is definable in \(M\) and can be avoided. For example, by viewing \(r\) as an infinite sequence of natural numbers in the increasing order, the property of \(r\) containing only finitely-many even numbers can be avoided, because given any finite approximation to \(r\)—i.e., any finite increasing sequence of natural numbers—one can always extend it by adding more even numbers, so that at the end of the construction \(r\) will contain infinitely-many even numbers; while the property of containing the number 7 cannot be avoided, because when a finite approximation to \(r\) contains the number 7, then it stays there no matter how the construction of \(r\) proceeds. Since \(M\) is countable, there are such generic \(r\). Then the expanded model \(M[r]\), which includes \(M\) and contains the new set \(r\), is called a *generic extension* of \(M\). Since we assumed \(M\) is a transitive model of \(V=L\), the model \(M[r]\) is just \(L_\alpha (r)\), where \(\alpha\) is the supremum of the ordinals of \(M\). Then one can show, using the *forcing* relation between finite approximations to \(r\) and formulas in the language of set theory expanded with so-called *names* for sets in the generic extension, that \(M[r]\) is a model of ZFC and \(r\) is not constructible in \(M[r]\), hence the axiom of constructibility \(V=L\) fails.

In general, a forcing extension of a model \(M\) is obtained by adding to \(M\) a generic subset \(G\) of some partially ordered set \(\mathbb{P}\) that belongs to \(M\). In the above example, \(\mathbb{P}\) would be the set of all finite increasing sequences of natural numbers, seen as finite approximations to the infinite sequence \(r\), ordered by \(\subseteq\); and \(G\) would be the set of all finite initial segments of \(r\).

In the case of the consistency proof of the negation of the CH, one starts from a model \(M\) of ZFC, as before, and adds \(\aleph_2\) new subsets of \(\omega\), so that in the generic extension the CH fails. In this case one needs to use an appropriate partial ordering \(\mathbb{P}\) so that the \(\aleph_2\) of \(M\) is not *collapsed*, i.e., it is the same as the \(\aleph_2\) of the generic extension, and thus the generic extension \(M[G]\) will satisfy the sentence that says that there are \(\aleph_2\) real numbers.

### 8.1 Other applications of forcing

Besides the CH, many other mathematical conjectures and problems about the continuum, and other infinite mathematical objects, have been shown undecidable in ZFC using the forcing technique.

One important example is *Suslin’s Hypothesis* (SH). Cantor had shown that every linearly ordered set \(S\) without endpoints that is dense (i.e., between any two different elements of \(S\) there is another one), complete (i.e., every subset of \(S\) that is bounded above has a supremum), and with a countable dense subset is isomorphic to the real line. Suslin conjectured that this is still true if one relaxes the requirement of containing a countable dense subset to being *ccc*, i.e., every collection of pairwise-disjoint intervals is countable. In the early 1970s, Thomas Jech produced a consistent counterexample using forcing, and Ronald Jensen showed that a counterexample exists in \(L\). About the same time, Robert Solovay and Stanley Tennenbaum (1971) developed and used for the first time the iterated forcing technique to produce a model where the SH holds, thus showing its independence from ZFC. In order to make sure that the SH holds in the generic extension, one needs to destroy all counterexamples, but by destroying one particular counterexample one may inadvertently create new ones, and so one needs to force again and again; in fact one needs to go on for at least \(\omega_2\)-many steps. This is why a forcing iteration is needed.

Among other famous mathematical problems that have been shown undecidable in ZFC thanks to the forcing technique, especially using iterated forcing and sometimes combined with large cardinals, we may mention the Measure Problem and the Borel Conjecture in measure theory, Kaplansky’s Conjecture on Banach algebras, and Whitehead’s Problem in group theory.

## 9. The search for new axioms

As a result of 60 years of development of the forcing technique, and its applications to many open problems in mathematics, there are now literally hundreds of problems and questions, in practically all areas of mathematics, that have been shown independent of ZFC. These include almost all important questions about the structure of uncountable sets. One might say that the undecidability phenomenon is pervasive, to the point that the investigation of the uncountable has been rendered nearly impossible in ZFC alone (see however Shelah (1994) for remarkable exceptions).

This prompts the question about the truth-value of the statements that are undecided by ZFC. Should one be content with them being undecidable? Does it make sense at all to ask for their truth-value? There are several possible reactions to this. One is the skeptic’s position: the statements that are undecidable in ZFC have no definite answer; and they may even be inherently vague. Another, the common one among mathematicians, is Gödel’s position: the undecidability only shows that the ZFC system is too weak to answer those questions, and therefore one should search for new axioms that once added to ZFC would answer them. The search for new axioms has been known as *Gödel’s Program*. See Hauser (2006) for a thorough philosophical discussion of the Program, and also the entry on large cardinals and determinacy for philosophical considerations on the justification of new axioms for set theory.

A central theme of set theory is thus the search and classification of new axioms. These fall currently into two main types: the axioms of large cardinals and the forcing axioms.

## 10. Large cardinals

One cannot prove in ZFC that there exists a regular limit cardinal \(\kappa\), for if \(\kappa\) is such a cardinal, then \(L_\kappa\) is a model of ZFC, and so ZFC would prove its own consistency, contradicting Gödel’s second incompleteness theorem. Thus, the existence of a regular limit cardinal must be postulated as a new axiom. Such a cardinal is called *weakly inaccessible*. If, in addition \(\kappa\) is a strong limit, i.e., \(2^\lambda &lt;\kappa\), for every cardinal \(\lambda &lt;\kappa\), then \(\kappa\) is called *strongly inaccessible*. A cardinal \(\kappa\) is strongly inaccessible if and only if it is regular and \(V_\kappa \) is a model of ZFC. If the GCH holds, then every weakly inaccessible cardinal is strongly inaccessible.

Large cardinals are uncountable cardinals satisfying some properties that make them very large, and whose existence cannot be proved in ZFC. The first weakly inaccessible cardinal is just the smallest of all large cardinals. Beyond inaccessible cardinals there is a rich and complex variety of large cardinals, which form a linear hierarchy in terms of consistency strength, and in many cases also in terms of outright implication. See the entry on independence and large cardinals for more details.

To formulate the next stronger large-cardinal notion, let us say that a subset \(C\) of an infinite cardinal \(\kappa\) is *closed* if every limit of elements of \(C\) which is less than \(\kappa\) is also in \(C\); and is *unbounded* if for every \(\alpha
&lt;\kappa\) there exists \(\beta\in C\) greater than \(\alpha\). For example, the set of limit ordinals less than \(\kappa\) is closed and unbounded. Also, a subset \(S\) of \(\kappa\) is called *stationary* if it intersects every closed unbounded subset of \(\kappa\). If \(\kappa\) is regular and uncountable, then the set of all ordinals less than \(\kappa\) of cofinality \(\omega\) is an example of a stationary set. A regular cardinal \(\kappa\) is called *Mahlo* if the set of strongly inaccessible cardinals smaller than \(\kappa\) is stationary. Thus, the first Mahlo cardinal is much larger than the first strongly inaccessible cardinal, as there are \(\kappa\)-many strongly inaccessible cardinals smaller than \(\kappa\).

Much stronger large cardinal notions arise from considering strong reflection properties. Recall that the Reflection Principle (Section 4), which is provable in ZFC, asserts that every *true* sentence (i.e., every sentence that holds in \(V\)) is true in some \(V_\alpha\). A strengthening of this principle to second-order sentences yields some large cardinals. For example, \(\kappa\) is strongly inaccessible if and only if every \(\Sigma^1_1\) sentence (i.e., existential second-order sentence in the language of set theory, with one additional predicate symbol) true in any structure of the form \((V_\kappa ,\in, A)\), where \(A\subseteq V_\kappa\), is true in some \((V_\alpha ,\in ,A\cap V_\alpha)\), with \(\alpha
&lt;\kappa\). The same type of reflection, but now for \(\Pi^1_1\) sentences (i.e., universal second-order sentences), yields a much stronger large cardinal property of \(\kappa\), called *weak compactness*. Every weakly compact cardinal \(\kappa\) is Mahlo, and the set of Mahlo cardinals smaller than \(\kappa\) is stationary. By allowing reflection for more complex second-order, or even higher-order, sentences one obtains large cardinal notions stronger than weak compactness.

The most famous large cardinals, called *measurable*, were discovered by Stanisław Ulam in 1930 as a result of his solution to the Measure Problem. A (two-valued) *measure*, or *ultrafilter*, on a cardinal \(\kappa\) is a subset \(U\) of \(\mathcal{P}(\kappa)\) that has the following properties: (i) the intersection of any two elements of \(U\) is in \(U\); (ii) if \(X\in
U\) and \(Y\) is a subset of \(\kappa\) such that \(X\subseteq Y\), then \(Y\in U\); and (iii) for every \(X\subseteq\kappa\), either \(X\in U\) or \(\kappa -X\in U\), but not both. A measure \(U\) is called *\(\kappa\)-complete* if every intersection of less than \(\kappa\) elements of \(U\) is also in \(U\). And a measure is called *non-principal* if there is no \(\alpha &lt;\kappa\) that belongs to all elements of \(U\). A cardinal \(\kappa\) is called *measurable* if there exists a measure on \(\kappa\) that is \(\kappa\)-complete and non-principal.

Measurable cardinals can be characterized by elementary embeddings of the universe \(V\) into some transitive class \(M\). That such an embedding \(j:V\to M\) is *elementary* means that \(j\) preserves truth, i.e., for every formula \(\varphi (x_1,\ldots ,x_n)\) of the language of set theory, and every \(a_1,\ldots ,a_n\), the sentence \(\varphi (a_1,\ldots ,a_n)\) holds in \(V\) if and only if \(\varphi (j(a_1),\ldots ,j(a_n))\) holds in \(M\). It turns out that a cardinal \(\kappa\) is measurable if and only if there exists an elementary embedding \(j:V\to M\), with \(M\) transitive, so that \(\kappa\) is the first ordinal moved by \(j\), i.e., the first ordinal such that \(j(\kappa)\ne \kappa\). We say that \(\kappa\) is the *critical point* of \(j\), and write \(crit(j)=\kappa\). The embedding \(j\) is definable from a \(\kappa\)-complete non-principal measure on \(\kappa\), using the so-called *ultrapower* construction. Conversely, if \(j:V\to M\) is an elementary embedding, with \(M\) transitive and \(\kappa=crit(j)\), then the set \(U=\{ X\subseteq \kappa:\kappa\in j(X)\}\) is a \(\kappa\)-complete non-principal ultrafilter on \(\kappa\). A measure \(U\) obtained in this way from \(j\) is called *normal*.

Every measurable cardinal \(\kappa\) is weakly compact, and there are many weakly compact cardinals smaller than \(\kappa\). In fact, below \(\kappa\) there are many cardinals that are *totally indescribable*, i.e., they reflect all sentences, of any complexity, and in any higher-order language.

If \(\kappa\) is measurable and \(j:V\to M\) is given by the ultrapower construction, then \(V_\kappa \subseteq M\), and every sequence of length less than or equal to \(\kappa\) of elements of \(M\) belongs to \(M\). Thus, \(M\) is quite similar to \(V\), but it cannot be \(V\) itself. Indeed, a famous theorem of Kenneth Kunen shows that there cannot be any elementary embedding \(j:V\to V\), other than the trivial one, i.e., the identity. All known proofs of this result use the Axiom of Choice, and it is an outstanding important question if the axiom is necessary. Kunen’s Theorem opens the door to formulating large cardinal notions stronger than measurability by requiring that \(M\) is closer to \(V\).

For example, \(\kappa\) is called *strong* if for every ordinal \(\alpha\) there exists an elementary embedding \(j:V\to M\), for some \(M\) transitive, such that \(\kappa =crit(j)\) and \(V_\alpha
\subseteq M\).

Another important, and much stronger large cardinal notion is supercompactness. A cardinal \(\kappa\) is *supercompact* if for every \(\alpha\) there exists an elementary embedding \(j:V\to
M\), with \(M\) transitive and critical point \(\kappa\), so that \(j(\kappa)&gt;\alpha\) and every sequence of elements of \(M\) of length \(\alpha\) belongs to \(M\).

Woodin cardinals fall between strong and supercompact. Every supercompact cardinal is Woodin, and if \(\delta\) is Woodin, then \(V_\delta\) is a model of ZFC in which there is a proper class of strong cardinals. Thus, while a Woodin cardinal \(\delta\) need not be itself very strong—the first one is not even weakly compact—it implies the existence of many large cardinals in \(V_\delta\).

Beyond supercompact cardinals we find the *extendible* cardinals, the *huge*, the *super huge*, etc.

Kunen’s theorem about the non-existence of a non-trivial elementary embedding \(j:V\to V\) actually shows that there cannot be an elementary embedding \(j:V_{\lambda +2}\to V_{\lambda +2}\) different from the identity, for any \(\lambda\).

The strongest large cardinal notions not known to be inconsistent, modulo ZFC, are the following:

- There exists an elementary embedding \(j:V_{\lambda +1}\to V_{\lambda
+1}\) different from the identity.
- There exists an elementary embedding \(j:L(V_{\lambda +1})\to
L(V_{\lambda +1})\) different from the identity.

Large cardinals form a linear hierarchy of increasing consistency strength. In fact they are the stepping stones of the interpretability hierarchy of mathematical theories. See the entry on independence and large cardinals for more details. Typically, given any sentence \(\varphi\) of the language of set theory, exactly one the following three possibilities holds about the theory ZFC plus \(\varphi\):

- ZFC plus \(\varphi\) is inconsistent.
- ZFC plus \(\varphi\) is equiconsistent with ZFC (i.e., ZFC is consistent if and only if so is ZFC plus \(\varphi\)).
- ZFC plus \(\varphi\) is equiconsistent with ZFC plus the existence of some large cardinal.

Thus, large cardinals can be used to prove that a given sentence \(\varphi\) does not imply another sentence \(\psi\), modulo ZFC, by showing that ZFC plus \(\psi\) implies the consistency of some large cardinal, whereas ZFC plus \(\varphi\) is consistent assuming the existence of a smaller large cardinal, or just assuming the consistency of ZFC. In other words, \(\psi\) has higher consistency strength than \(\varphi\), modulo ZFC. Then, by Gödel’s second incompleteness theorem, ZFC plus \(\varphi\) cannot prove \(\psi\), assuming ZFC plus \(\varphi\) is consistent.

As we already pointed out, one cannot prove in ZFC that large cardinals exist. But everything indicates that their existence not only cannot be disproved, but in fact the assumption of their existence is a very reasonable axiom of set theory. For one thing, there is a lot of evidence for their consistency, especially for those large cardinals for which it is possible to construct a canonical inner model.

### 10.1 Inner models of large cardinals

An *inner model* of ZFC is a transitive proper class that contains all the ordinals and satisfies all ZFC axioms. Thus, \(L\) is the smallest inner model, while \(V\) is the largest. Some large cardinals, such as inaccessible, Mahlo, or weakly-compact, may exist in \(L\). That is, if \(\kappa\) has one of these large cardinal properties, then it also has the property in \(L\). But some large cardinals cannot exist in \(L\). Indeed, Scott (1961) showed that if there exists a measurable cardinal \(\kappa\), then \(V\ne L\). It is important to notice that \(\kappa\) does belong to \(L\), since \(L\) contains all ordinals, but it is not measurable in \(L\) because a \(\kappa\)-complete non-principal measure on \(\kappa\) cannot exist there.

If \(\kappa\) is a measurable cardinal, then one can construct an \(L\)-like model in which \(\kappa\) is measurable by taking a \(\kappa\)-complete non-principal and normal measure \(U\) on \(\kappa\), and proceeding as in the definition of \(L\), but now using \(U\) as an additional predicate. The resulting model, called \(L[U]\), is an inner model of ZFC in which \(\kappa\) is measurable, and in fact \(\kappa\) is the only measurable cardinal. The model is canonical, in the sense that any other normal measure witnessing the measurability of \(\kappa\) would yield the same model, and has many of the properties of \(L\). For instance, it has a projective well ordering of the reals, and it satisfies the GCH.

Building similar \(L\)-like models for stronger large cardinals, such as strong, or Woodin, is much harder. Those models are of the form \(L[E]\), where \(E\) is a sequence of *extenders*, each extender being a coherent system of measures, that encode the relevant elementary embeddings.

The largest \(L\)-like inner models for large cardinals that have been obtained so far can contain Woodin cardinals that are limits of Woodin cardinals (Neeman 2002)[^neeman-2002]. However, building an \(L\)-like model for a supercompact cardinal is still a challenge. The supercompact barrier seems to be the crucial one, for Woodin has shown that for a natural kind of inner model for a supercompact cardinal \(\kappa\), which he calls a *weak extender model for the supercompactness of \( \kappa
\)*, all stronger large cardinals greater than \(\kappa\) that may exist in \(V\), such as extendible, huge, etc. would also exist in the model.

### 10.2 Consequences of large cardinals

The existence of large cardinals has dramatic consequences, even for simply-definable small sets, like the projective sets of real numbers. For example, Solovay (1970) proved, assuming that there exists a measurable cardinal, that all \(\mathbf{\Sigma}^1_2\) sets of reals are Lebesgue measurable and have the Baire property, which cannot be proved in ZFC alone. And Shelah and Woodin (1990) showed that the existence of a proper class of Woodin cardinals implies that the theory of \(L(\mathbb{R})\), even with real numbers as parameters, cannot be changed by forcing, which implies that all sets of real numbers that belong to \(L(\mathbb{R})\) are regular. Further, under a weaker large-cardinal hypothesis, namely the existence of infinitely many Woodin cardinals, Martin and Steel (1989) proved that every projective set of real numbers is determined, i.e., the axiom of PD holds, hence all projective sets are regular. Moreover, Woodin showed that the existence of infinitely many Woodin cardinals, plus a measurable cardinal above all of them, implies that every set of reals in \(L(\mathbb{R})\) is determined, i.e., the axiom \(AD^{L(\mathbb{R})}\) holds, hence all sets of real numbers that belong to \(L(\mathbb{R})\), and therefore all projective sets, are regular. He also showed that Woodin cardinals provide the optimal large cardinal assumptions by proving that the following two statements:

1. There are infinitely many Woodin cardinals.
2. \(AD^{L({\Bbb R})}\).

are equiconsistent, i.e., ZFC plus 1 is consistent if and only if ZFC plus 2 is consistent. See the entry on large cardinals and determinacy for more details and related results.

Another area in which large cardinals play an important role is the exponentiation of singular cardinals. The so-called *Singular Cardinal Hypothesis* (SCH) completely determines the behavior of the exponentiation for singular cardinals, modulo the exponentiation for regular cardinals. The SCH follows from the GCH, and so it holds in \(L\). A consequence of the SCH is that if \(2^{\aleph_n}&lt;\aleph_\omega\), for all finite \(n\), then \(2^{\aleph_{\omega}}=\aleph_{\omega +1}\). Thus, if the GCH holds for cardinals smaller than \(\aleph_\omega\), then it also holds at \(\aleph_\omega\). The SCH holds above the first supercompact cardinal (Solovay). But Magidor (1977) showed that, remarkably, assuming the existence of large cardinals it is possible to build a model of ZFC where the GCH first fails at \(\aleph_\omega\), hence the SCH fails. Large cardinals stronger than measurable are actually needed for this. In contrast, however, ZFC alone suffices to prove that if the SCH holds for all cardinals smaller than \(\aleph_{\omega_1}\), then it also holds for \(\aleph_{\omega_1}\). Moreover, if the SCH holds for all singular cardinals of countable cofinality, then it holds for all singular cardinals (Silver).

## 11. Forcing axioms

Forcing axioms are axioms of set theory that assert that certain existential statements are absolute between the universe \(V\) of all sets and its (ideal) forcing extensions, i.e., some existential statements that hold in some forcing extensions of \(V\) are already true in \(V\). The first forcing axiom was formulated by Donald Martin in the wake of the Solovay-Tennenbaum proof of the consistency of Suslin’s Hypothesis, and is now known as *Martin’s Axiom* (MA). Before we state it, let us say that a *partial ordering* is a non-empty set \(P\) together with a binary relation \(\leq\) on \(P\) that is reflexive and transitive. Two elements, \(p\) and \(q\), of \(P\) are called *compatible* if there exists \(r\in P\) such that \(r\leq p\) and \(r\leq q\). An *antichain* of \(P\) is a subset of \(P\) whose elements are pairwise-incompatible. A partial ordering \(P\) is called *ccc* if every antichain of \(P\) is countable. A non-empty subset \(G\) of \(P\) is called a *filter* if (i) every two elements of \(G\) are compatible, and (ii) if \(p\in G\) and \(p\leq q\), then also \(q\in G\). Finally, a subset \(D\) of \(P\) is called *dense* if for every \(p\in P\) there is \(q\in D\) such that \(q\leq p\).

MA asserts the following:

> For every ccc partial ordering \(P\) and every set \(\{ D_\alpha
:\alpha &lt;\kappa \}\), where \(\kappa \lt 2^{\aleph_0}\), of dense subsets of \(P\), there exists a filter \(G\subseteq P\) that is *generic* for the set, i.e., \(G\cap D_\alpha \ne
{\varnothing}\), for all \(\alpha &lt;\kappa\).

Since MA follows easily from the CH, MA is only of interest if the CH fails. Martin and Solovay (1970) proved that MA plus the negation of the CH is consistent with ZFC, using iterated forcing with the ccc property. At first sight, MA may not look like an axiom, namely an obvious, or at least reasonable, assertion about sets, but rather like a technical statement about ccc partial orderings. It does look more natural, however, when expressed in topological terms, for it is simply a generalization of the well-known Baire Category Theorem, which asserts that in every compact Hausdorff topological space the intersection of countably-many dense open sets is non-empty. Indeed, MA is equivalent to:

> In every compact Hausdorff ccc topological space, the intersection of less than \(2^{\aleph_0}\)-many dense open sets is non-empty.

MA has many different equivalent formulations and has been used very successfully to settle a large number of open problems in other areas of mathematics. For example, MA plus the negation of the CH implies Suslin’s Hypothesis and that every \(\mathbf{\Sigma}^1_2\) set of reals is Lebesgue measurable and has the Baire property. It also implies that \(2^{\aleph_0}\) is a regular cardinal, but it does not decide what cardinal it is. See Fremlin (1984) for many more consequences of MA and other equivalent formulations. In spite of this, the status of MA as an axiom of set theory is still unclear. Perhaps the most natural formulation of MA, from a foundational point of view, is in terms of *generic absoluteness*. Namely, MA is equivalent to the following:

> For every ccc partial ordering \(P\), if an existential statement, containing subsets of some cardinal less than \(2^{\aleph_0}\) as parameters, holds in an (ideal) generic extension of \(V\) obtained by forcing with \(P\), then the statement is true, i.e., it holds in \(V\). In other words, if a set having a property that depends only on bounded subsets of \( 2^{\aleph_0}\) exists in some (ideal) generic extension of \(V\) obtained by forcing with a ccc partial ordering, then a set with that property already exists in \(V\).

The notion of ideal generic extension of \(V\) can be made precise in terms of so-called Boolean-valued models, which provide an alternative version of forcing.

Much stronger forcing axioms than MA (for \(\omega_1\)) were introduced in the 1980s, such as J. Baumgartner’s *Proper Forcing Axiom* (PFA), and the stronger *Martin’s Maximum* (MM) of Foreman, Magidor, and Shelah (1988). Both the PFA and MM are consistent relative to the existence of a supercompact cardinal. The PFA asserts the same as MA, but for partial orderings that have a property weaker than the ccc, called *properness*, introduced by Shelah. And MM asserts the same for the wider class of partial orderings that, when forcing with them, do not destroy stationary subsets of \(\omega_1\).

Strong forcing axioms, such as the PFA and MM imply that all projective sets of reals are determined (PD), and have many other strong consequences in infinite combinatorics. Notably, they imply that the cardinality of the continuum is \(\aleph_2\).

A different forcing axiom is Woodin’s Axiom \((\ast)\), which resulted from his analysis of \(\mathbb{P}_{{\rm max}}\) forcing extensions over models of AD. Even though a stronger form of MM known as \({\rm MM}^{++}\) and Axiom \((\ast)\) have similar and very rich consequences, both their motivation and their formulation are very different, to the point that they were seen as competing axioms. Their connection was far from being clear, until Asperó and Schindler (2021) showed that, in the presence of large cardinals, Axiom \((\ast)\) is equivalent to a bounded form of \({\rm MM}^{++}\), and therefore to a natural generic absoluteness principle.

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=set-theory). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/set-theory/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=set-theory&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/set-theory/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

## Related Entries

[^asperó-2021]: Asperó, D. and Schindler, R. D., 2021, “Martin’s Maximum\(^{++}\) implies Woodin’s Axiom \((\ast)\)”, *Annals of Mathematics*, 193(3): 793–835.

[^bagaria-2008]: Bagaria, J., 2008, “Set Theory”, in *The Princeton Companion to Mathematics*, edited by Timothy Gowers; June Barrow-Green and Imre Leader, associate editors. Princeton: Princeton University Press.

[^cohen-1966]: Cohen, P.J., 1966, *Set Theory and the Continuum Hypothesis*, New York: W. A. Benjamin, Inc.

[^enderton-1977]: Enderton, H.B., 1977, *Elements of Set Theory*, New York: Academic Press.

[^ferreirós-2007]: Ferreirós, J., 2007, *Labyrinth of Thought: A History of Set Theory and its Role in Modern Mathematics*, Second revised edition, Basel: Birkhäuser.

[^foreman-1988]: Foreman, M., Magidor, M., and Shelah, S., 1988, “Martin’s maximum, saturated ideals and non-regular ultrafilters”, Part I, *Annals of Mathematics*, 127: 1–47.

[^fremlin-1984]: Fremlin, D.H., 1984, “Consequences of Martin’s Axiom”, *Cambridge tracts in Mathematics* #84. Cambridge: Cambridge University Press.

[^gödel-1931]: Gödel, K., 1931, “Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I,” *Monatshefte für Mathematik Physik*, 38: 173–198. English translation in Gödel 1986, 144–195.

[^gödel-1938]: –––, 1938, “The consistency of the axiom of choice and of the generalized continuum hypothesis”, *Proceedings of the National Academy of Sciences, U.S.A.* 24: 556–557.

[^gödel-1986]: –––, 1986, *Collected Works I. Publications 1929–1936*, S. Feferman et al. (eds.), Oxford: Oxford University Press.

[^hauser-2006]: Hauser, K., 2006, “Gödel’s program revisited, Part I: The turn to phenomenology”, *Bulletin of Symbolic Logic*, 12(4): 529–590.

[^jech-2003]: Jech, T., 2003, *Set theory*, 3d Edition, New York: Springer.

[^jensen-1972]: Jensen, R.B., 1972, “The fine structure of the constructible hierarchy”, *Annals of Mathematical Logic*, 4(3): 229–308.

[^kanamori-2003]: Kanamori, A., 2003, *The Higher Infinite*, Second Edition. *Springer Monographs in Mathematics*, New York: Springer.

[^kechris-1995]: Kechris, A.S., 1995, *Classical Descriptive Set Theory*, *Graduate Texts in Mathematics*, New York: Springer Verlag.

[^kunen-1980]: Kunen, K., 1980, *Set Theory, An Introduction to Independence Proofs*, Amsterdam: North-Holland.

[^levy-1960]: Levy, A., 1960, “Axiom schemata of strong infinity in axiomatic set theory”, *Pacific Journal of Mathematics*, 10: 223–238.

[^levy-1979]: –––, 1979, *Basic Set Theory*, New York: Springer.

[^magidor-1977]: Magidor, M., 1977, “On the singular cardinals problem, II”, *Annals of Mathematics*, 106: 514–547.

[^martin-1970]: Martin, D.A. and R. Solovay, 1970, “Internal Cohen Extensions”, *Annals of Mathematical Logic*, 2: 143–178.

[^martin-1989]: Martin, D.A. and J.R. Steel, 1989, “A proof of projective determinacy”, *Journal of the American Mathematical Society*, 2(1): 71–125.

[^mathias-2001]: Mathias, A.R.D., 2001, “Slim models of Zermelo Set Theory”, *Journal of Symbolic Logic*, 66: 487–496.

[^neeman-2002]: Neeman, I., 2002, “Inner models in the region of a Woodin limit of Woodin cardinals”, *Annals of Pure and Applied Logic*, 116: 67–155.

[^scott-1961]: Scott, D., 1961, “Measurable cardinals and constructible sets”, *Bulletin de l’Académie Polonaise des Sciences. Série des Sciences Mathématiques, Astronomiques et Physiques*, 9: 521–524.

[^shelah-1994]: Shelah, S., 1994, “Cardinal Arithmetic”, *Oxford Logic Guides*, 29, New York: The Clarendon Press, Oxford University Press.

[^shelah-1998]: –––, 1998, *Proper and improper forcing*, 2nd Edition, New York: Springer-Verlag.

[^shelah-1990]: Shelah, S. and W.H. Woodin, 1990, “Large cardinals imply that every reasonably definable set of reals is Lebesgue measurable”, *Israel Journal of Mathematics*, 70(3): 381–394.

[^solovay-1970]: Solovay, R., 1970, “A model of set theory in which every set of reals is Lebesgue measurable”, *Annals of Mathematics*, 92: 1–56.

[^solovay-1971]: Solovay, R. and S. Tennenbaum, 1971, “Iterated Cohen extensions and Souslin’s problem”, *Annals of Mathematics (2)*, 94: 201–245.

[^todorcevic-1989]: Todorcevic, S., 1989, “Partition Problems in Topology”, *Contemporary Mathematics*, Volume 84. American Mathematical Society.

[^ulam-1930]: Ulam, S., 1930, ‘Zur Masstheorie in der allgemeinen Mengenlehre’, *Fundamenta Mathematicae*, 16: 140–150.

[^woodin-1999]: Woodin, W.H., 1999, *The Axiom of Determinacy, Forcing Axioms, and the Nonstationary Ideal*, *De Gruyter Series in Logic and Its Applications* 1, Berlin-New York: Walter de Gruyter.

[^woodin-2001]: –––, 2001, “The Continuum Hypothesis, Part I”, *Notices of the AMS*, 48(6): 567–576, and “The Continuum Hypothesis, Part II”, *Notices of the AMS* 48(7): 681–690.

[^zeman-2001]: Zeman, M., 2001, *Inner Models and Large Cardinals*, *De Gruyter Series in Logic and Its Applications* 5, Berlin-New York: Walter de Gruyter.

[^zermelo-1908]: Zermelo, E., 1908, “Untersuchungen über die Grundlagen der Mengenlehre, I”, *Mathematische Annalen* 65: 261–281. Reprinted in Zermelo 2010: 189–228, with a facing-page English translation, and an Introduction by Ulrich Felgner (2010). English translation also in van Heijenoort 1967: 201–215.

[^jech-2014]: Jech, Thomas, “Set Theory”, *The Stanford Encyclopedia of Philosophy* (Fall 2014 Edition), Edward N. Zalta (ed.), URL = <[https://plato.stanford.edu/archives/fall2014/entries/set-theory/](https://plato.stanford.edu/archives/fall2014/entries/set-theory/)>. [This was the previous entry on set theory in the *Stanford Encyclopedia of Philosophy* — see the [version history](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=set-theory).]
