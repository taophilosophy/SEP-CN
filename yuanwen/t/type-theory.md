# Type Theory
**First published Wed Feb 8, 2006; substantive revision Fri Nov 20, 2026**

*Coquand, Thierry*

First published Wed Feb 8, 2006; substantive revision Tue Sep 6, 2022

The topic of type theory is fundamental both in logic and computer science. We limit ourselves here to sketch some aspects that are important in logic. For the importance of types in computer science, we refer the reader for instance to Reynolds 1983 and 1985.

## 1. Paradoxes and Russell’s Type Theories

The theory of types was introduced by Russell in order to cope with some contradictions he found in his account of set theory and was introduced in “Appendix B: The Doctrine of Types” of Russell 1903. This contradiction was obtained by analysing a theorem of Cantor that no mapping $$F : X \to \mathrm{Pow}(X)$$ (where $\mathrm{Pow}(X)$ is the class of subclasses of a class $X$) can be surjective; that is, $F$ cannot be such that every member $b$ of $\mathrm{Pow}(X)$ is equal to $F(a)$ for some element $a$ of $X$. This can be phrased “intuitively” as the fact that there are more subsets of $X$ than elements of $X$. The proof of this fact is so simple and basic that it is worthwhile giving it here. Consider the following subset of $X$: $$A = \{x \in X \mid x \notin F(x)\}.$$ This subset cannot be in the range of $F$. For if $A = F(a)$, for some $a$, then $$\begin{align*} a \in F(a) &\text{ iff } a \in A\\ &\text{ iff } a \notin F(a) \end{align*}$$ which is a contradiction.

Some remarks are in order. First, the proof does not use the law of excluded middle and is thus valid intuitionistically. Second, the method that is used, called *diagonalisation* was already present in the work of du Bois-Reymond for building real functions growing faster than any function in a given sequence of functions.

Russell analysed what happens if we apply this theorem to the case where $X$ is the class of all classes, admitting that there is such a class. He was then led to consider the special class of classes that do not belong to themselves $$(*)\qquad R = \{w \mid w \notin w\}.$$ We then have $$R \in R \text{ iff } R \notin R.$$ It seems indeed that Cantor was already aware of the fact that the class of all sets cannot be considered itself to be a set.

Russell communicated this problem to Frege, and his letter, together with Frege’s answer appear in van Heijenoort 1967. It is important to realise that the formulation $(*)$ does not apply as it is to Frege’s system. As Frege himself wrote in his reply to Russell, the expression “a predicate is predicated of itself” is not exact. Frege had a distinction between predicates (concepts) and objects. A (first-order) predicate applies to an object but it cannot have a predicate as argument. The exact formulation of the paradox in Frege’s system uses the notion of the *extension* of a predicate $P$, which we designate as $\varepsilon P$. The extension of a predicate is itself an object. The important axiom V is: $$\text{(Axiom V)}\qquad \varepsilon P = \varepsilon Q \equiv \forall x[P(x) \equiv Q(x)]$$ This axiom asserts that the extension of $P$ is identical to the extension of $Q$ if and only if $P$ and $Q$ are materially equivalent. We can then translate Russell’s paradox $(*)$ in Frege’s system by defining the predicate $$R(x) \text{ iff } \exists P[x = \varepsilon P \wedge \neg P(x)]$$ It can then be checked, using Axiom V in a crucial way, that $$R(\varepsilon R) \equiv \neg R(\varepsilon R)$$ and we have a contradiction as well. (Notice that for defining the predicate $R$, we have used an impredicative existential quantification on predicates. It can be shown that the predicative version of Frege’s system is consistent (see Heck 1996 and for further refinements Ferreira and Wehmeier 2002)[^ferreira-2002][^heck-1996].)

It is clear from this account that an idea of types was already present in Frege’s work: there we find a distinction between objects, predicates (or concepts), predicates of predicates, etc. (This point is stressed in Quine 1940.)[^quine-1940] This hierarchy is called the “extensional hierarchy” by Russell (1959)[^russell-1959], and its necessity was recognised by Russell as a consequence of his paradox. (For a survey of Russell’s theories of types, see Urquhart 2003.)[^urquhart-2003]

## 2. Simple Type Theory and the *λ*-Calculus

As we saw above, the distinction: objects, predicates, predicate of predicates, etc., seems enough to block Russell’s paradox (and this was recognised by Chwistek and Ramsey). We first describe the type structure as it is in *Principia* and later in this section we present the elegant formulation due to Church 1940 based on *λ*-calculus. The types can be defined as

1. $i$ is the type of individuals
2. $(\,)$ is the type of propositions
3. if $A_1,\dots,A_n$ are types then $(A_1,\dots,A_n)$ is the type of $n$-ary relations over objects of respective types $A_1,\dots,A_n$

For instance, the type of binary relations over individuals is $(i,i)$, the type of binary connectives is $((\,),(\,))$, the type of quantifiers over individuals is $((i))$.

For forming propositions we use this type structure: thus $R(a_1,\dots,a_n)$ is a proposition if $R$ is of type $(A_1,\dots,A_n)$ and $a_i$ is of type $A_i$ for $i=1,\dots,n$. This restriction makes it impossible to form a proposition of the form $P(P)$: the type of $P$ should be of the form $(A)$, and $P$ can only be applied to arguments of type $A$, and thus cannot be applied to itself since $A$ is not the same as $(A)$.

However simple type theory is not predicative: we can define an object $Q(x,y)$ of type $(i,i)$ by $$\forall P[P(x) \supset P(y)]$$ Assume that we have two individuals $a$ and $b$ such that $Q(a,b)$ holds. We can define $P(x)$ to be $Q(x,a)$. It is then clear that $P(a)$ holds, since it is $Q(a,a)$. Hence $P(b)$ holds as well. We have proved, in an impredicative way, that $Q(a,b)$ implies $Q(b,a)$.

Alternative simpler formulations, which retain only the notion of classes, classes of classes, etc., were formulated by Gödel and Tarski. Actually this simpler version was used by Gödel in his 1931 paper on formally undecidable propositions. The discovery of the undecidable propositions may have been motivated by a heuristic argument that it is unlikely that one can extend the completeness theorem of first-order logic to type theory (see the end of his Lecture at Königsberg 1930 in Gödel Collected Work, Volume III, Awodey and Carus 2001 and Goldfarb 2005)[^awodey-2001][^goldfarb-2005]. Tarski had a version of the definability theorem expressed in type theory (Tarski 1931; see Hodges 2008)[^hodges-2008][^tarski-1931]. See Schiemer and Reck 2013.

We have objects of type 0, for individuals, objects of type 1, for classes of individuals, objects of type 2, for classes of classes of individuals, and so on. Functions of two or more arguments, like relations, need not be included among primitive objects since one can define relations to be classes of ordered pairs, and ordered pairs to be classes of classes. For example, the ordered pair of individuals $a, b$ can be defined to be $\{\{a\},\{a,b\}\}$ where $\{x,y\}$ denotes the class whose sole elements are $x$ and $y$. (Wiener 1914 had suggested a similar reduction of relations to classes.)[^wiener-1914] In this system, all propositions have the form $a(b)$, where $a$ is a sign of type $n+1$ and $b$ a sign of type $n$. Thus this system is built on the concept of an arbitrary class or subset of objects of a given domain and on the fact that the collection of all subsets of the given domain can form a new domain of the next type. Starting from a given domain of individuals, this process is then iterated. As emphasised for instance in Scott 1993, in set theory this process of forming subsets is iterated into the transfinite.

In these versions of type theory, as in set theory, functions are not primitive objects, but are represented as functional relations. The addition function for instance is represented as a ternary relation by an object of type $(i,i,i)$. An elegant formulation of the simple type theory which extends it by introducing functions as primitive objects was given by Church in 1940. It uses the *λ*-calculus notation (Barendregt 1997)[^barendregt-1997]. Since such a formulation is important in computer science, for the connection with category theory, and for Martin-Löf type theory, we describe it in some detail. In this formulation, predicates are seen as a special kind of functions (propositional functions), an idea that goes back to Frege (see for instance Quine 1940)[^quine-1940]. Furthermore, the notion of function is seen as more primitive than the notion of predicates and relations, and a function is not defined anymore as a special kind of relation. (Oppenheimer and Zalta 2011 presents some arguments against such a primitive representation of functions.)[^oppenheimer-2011] The types of this system are defined inductively as follows

1. there are two basic types $i$ (the type of individuals) and $o$ (the type of propositions)
2. if $A, B$ are types then $A \to B$, the type of functions from $A$ to $B$, is a type

We can form in this way the types: $$\begin{align*} & i \to o && \text{(type of predicates)}\\ & (i \to o) \to o && \text{(type of predicates of predicates)} \end{align*}$$ which correspond to the types $(i)$ and $((i))$ but also the new types $$\begin{align*} & i \to i && \text{(type of functions)}\\ & (i \to i) \to i && \text{(type of functionals)} \end{align*}$$ It is convenient to write $$A_1,\dots,A_n \to B$$ for $$A_1 \to (A_2 \to \dots \to (A_n \to B))$$ In this way $$A_1,\dots,A_n \to o$$ corresponds to the type $(A_1,\dots,A_n)$.

First-order logic considers only types of the form $$\begin{align*} &i,\dots,i \to i \quad\text{(type of function symbols)},\qquad\text{and} \\ &i,\dots,i \to o \quad\text{(type of predicate, relation symbols)} \end{align*}$$ Notice that $$A \to B \to C$$ stands for $$A \to (B \to C)$$ (association to the right).

For the terms of this logic, we shall not follow Church’s account but a slight variation of it, due to Curry (who had similar ideas before Church’s paper appeared) and which is presented in detail in R. Hindley’s book on type theory. Like Church, we use *λ*-calculus, which provides a general notation for functions $$M ::= x \mid M\,M \mid \lambda x.\,M$$ Here we have used the so-called BNF notation, very convenient in computing science. This gives a syntactic specification of the *λ*-terms which, when expanded, means:

- every variable is a function symbol;
- every juxtaposition of two function symbols is a function symbol;
- every $\lambda x.\,M$ is a function symbol;
- there are no other function symbols.

The notation for function application $M\,N$ is a little different than the mathematical notation, which would be $M(N)$. In general, $$M_1\,M_2\,M_3$$ stands for $$(M_1\,M_2)\,M_3$$ (association to the left). The term $\lambda x.\,M$ represents the function which to $N$ associates $M[x:=N]$. This notation is so convenient that one wonders why it is not widely used in mathematics. The main equation of *λ*-calculus is then (*β*-conversion) $$(\lambda x.\,M)\,N = M[x:=N]$$ which expresses the meaning of $\lambda x.\,M$ as a function. We have used $M[x:=N]$ as a notation for the value of the expression that results when $N$ is substituted for the variable $x$ in the matrix $M$. One usually sees this equation as a rewrite rule (*β*-reduction) $$(\lambda x.\,M)\,N \to M[x:=N]$$ In untyped lambda calculus, it may be that such rewriting does not terminate. The canonical example is given by the term $\Delta = \lambda x.\,x\,x$ and the application $$\Delta\,\Delta \to \Delta\,\Delta$$ (Notice the similarity with Russell’s paradox.) The idea of Curry is then to look at types as predicates over lambda terms, writing $M : A$ to express that $M$ satisfies the predicate/type $A$. The meaning of $$N : A \to B$$ is then $$\forall M,\ \text{if } M : A \text{ then } N\,M : B$$ which justifies the following rules $$\dfrac{N : A \to B \qquad M : A}{N\,M : B} \qquad\qquad \dfrac{M : B\ [x:A]}{\lambda x.\,M : A \to B}$$ In general one works with judgements of the form $$x_1 : A_1, \dots, x_n : A_n \vdash M : A$$ where $x_1,\dots,x_n$ are distinct variables, and $M$ is a term having all free variables among $x_1,\dots,x_n$. In order to be able to get Church’s system, one adds some constants in order to form propositions. Typically $$\begin{align*} \mathsf{not}&: o \to o\\ \mathsf{imply}&: o \to o \to o\\ \mathsf{and}&: o \to o \to o\\ \mathsf{forall}&: (A \to o) \to o \end{align*}$$ The term $$\lambda x.\,\neg(x\,x)$$ represents the predicate of predicates that do not apply to themselves. This term does not have a type however, that is, it is not possible to find $A$ such that $$\lambda x.\,\neg(x\,x) : (A \to o) \to o$$ which is the formal expression of the fact that Russell’s paradox cannot be expressed. Leibniz equality $$Q : i \to i \to o$$ will be defined as $$Q = \lambda x.\,\lambda y.\,\forall(\lambda P.\,\mathsf{imply}(P\,x)(P\,y))$$ One usually writes $\forall x[M]$ instead of $\forall(\lambda x.\,M)$, and the definition of $Q$ can then be rewritten as $$Q = \lambda x.\,\lambda y.\,\forall P[\mathsf{imply}(P\,x)(P\,y)]$$ This example again illustrates that we can formulate impredicative definitions in simple type theory.

The use of *λ*-terms and *β*-reduction is most convenient for representing the complex substitution rules that are needed in simple type theory. For instance, if we want to substitute the predicate $\lambda x.\,Q\,a\,x$ for $P$ in the proposition $$\mathsf{imply}(P\,a)(P\,b)$$ we get $$\mathsf{imply}((\lambda x.\,Q\,a\,x)\,a)((\lambda x.\,Q\,a\,x)\,b)$$ and, using *β*-reduction, $$\mathsf{imply}(Q\,a\,a)(Q\,a\,b)$$ In summary, simple type theory forbids self-application but not the circularity present in impredicative definitions.

The *λ*-calculus formalism also allows for a clearer analysis of Russell’s paradox. We can see it as the definition of the predicate $$R\,x = \neg(x\,x)$$ If we think of *β*-reduction as the process of unfolding a definition, we see that there is a problem already with understanding the definition of $R\,R$ $$R\,R \to \neg(R\,R) \to \neg(\neg(R\,R)) \to \dots$$ In some sense, we have a non-wellfounded definition, which is as problematic as a contradiction (a proposition equivalent to its negation). One important theorem, the normalisation theorem, says that this cannot happen with simple types: if we have $M : A$ then $M$ is normalisable in a strong way (any sequence of reductions starting from $M$ terminates).

For more information on this topic, we refer to the entry on Church’s simple type theory.

## 3. Ramified Hierarchy and Impredicative Principles

Russell introduced another hierarchy, that was not motivated by any formal paradoxes expressed in a formal system, but rather by the fear of “circularity” and by informal paradoxes similar to the paradox of the liar. If a man says “I am lying”, then we have a situation reminiscent of Russell’s paradox: a proposition which is equivalent to its own negation. Another informal such paradoxical situation is obtained if we define an integer to be the “least integer not definable in less than 100 words”. In order to avoid such informal paradoxes, Russell thought it necessary to introduce another kind of hierarchy, the so-called “ramified hierarchy”. The need for such a hierarchy is hinted in Appendix B of Russell 1903. Interestingly this is connected there to the question of the identity of equivalent propositions and of the logical product of a class of propositions (see Church 1984)[^church-1984]. A thorough discussion can be found in Chapter 10 of Russell 1959. Since this notion of ramified hierarchy has been extremely influential in logic and especially proof theory, we describe it in some details.

In order to further motivate this hierarchy, here is one example due to Russell. If we say

> Napoleon was Corsican.

we do not refer in this sentence to any assemblage of properties. The property “to be Corsican” is said to be *predicative*. If we say on the other hand

> Napoleon had all the qualities of a great general

we are referring to a totality of qualities. The property “to have all qualities of a great general” is said to be *impredicative*.

Another example, also coming from Russell, shows how impredicative properties can potentially lead to problems reminiscent of the liar paradox. Suppose that we suggest the definition

> A typical Englishman is one who possesses all the properties possessed by a majority of Englishmen.

It is clear that most Englishmen do not possess all the properties that most Englishmen possess. Therefore, a typical Englishman, according to this definition, should be untypical. The problem, according to Russell, is that the word “typical” has been defined by a reference to all properties and has been treated as itself a property. (It is remarkable that similar problems arise when defining the notion of random numbers, cf. Martin-Löf “Notes on constructive mathematics” (1970).) Russell introduced the ramified hierarchy in order to deal with the apparent circularity of such impredicative definitions. One should make a distinction between the *first-order* properties, like being Corsican, that do not refer to the totality of properties, and consider that the *second-order* properties refer only to the totality of first-order properties. One can then introduce third-order properties, that can refer to the totality of second-order property, and so on. This clearly eliminates all circularities connected to impredicative definitions.

At about the same time, Poincaré carried out a similar analysis. He stressed the importance of “predicative” classifications, and of not defining elements of a class using a quantification over this class (Poincaré 1909)[^poincaré-1909]. Poincaré used the following example. Assume that we have a collection with elements $0, 1$ and an operation $+$ satisfying $$\begin{align*} x + 0 &= x\\ x + (y + 1) &= (x + y) + 1 \end{align*}$$ Let us say that a property is *inductive* if it holds of $0$ and holds for $x+1$ if it holds for $x$.

An impredicative, and potentially “dangerous”, definition would be to define an element to be a *number* if it satisfies all inductive properties. It is then easy to show that this property “to be a number” is itself inductive. Indeed, $0$ is a number since it satisfies all inductive properties, and if $x$ satisfies all inductive properties then so does $x+1$. Similarly it is easy to show that $x+y$ is a number if $x, y$ are numbers. Indeed the property $Q(z)$ that $x+z$ is a number is inductive: $Q(0)$ holds since $x+0=x$ and if $x+z$ is a number then so is $x+(z+1) = (x+z)+1$. This whole argument however is circular since the property “to be a number” is not predicative and should be treated with suspicion.

Instead, one should introduce a ramified hierarchy of properties and numbers. At the beginning, one has only first-order inductive properties, which do not refer in their definitions to a totality of properties, and one defines the numbers of order 1 to be the elements satisfying all first-order inductive properties. One can next consider the second-order inductive properties, that can refer to the collection of first-order properties, and the numbers of order 2, that are the elements satisfying the inductive properties of order 2. One can then similarly consider numbers of order 3, and so on. Poincaré emphasizes the fact that a number of order 2 is *a fortiori* a number of order 1, and more generally, a number of order $n+1$ is *a fortiori* a number of order $n$. We have thus a sequence of more and more restricted properties: inductive properties of order $1, 2, \dots$ and a sequence of more and more restricted collections of objects: numbers of order $1, 2, \dots$ Also, the property “to be a number of order $n$” is itself an inductive property of order $n+1$.

It does not seem possible to prove that $x+y$ is a number of order $n$ if $x, y$ are numbers of order $n$. On the other hand, it is possible to show that if $x$ is a number of order $n+1$, and $y$ a number of order $n+1$ then $x+y$ is a number of order $n$. Indeed, the property $P(z)$ that “$x+z$ is a number of order $n$” is an inductive property of order $n+1$: $P(0)$ holds since $x+0=x$ is a number of order $n+1$, and hence of order $n$, and if $P(z)$ holds, that is if $x+z$ is a number of order $n$, then so is $x+(z+1) = (x+z)+1$, and so $P(z+1)$ holds. Since $y$ is a number of order $n+1$, and $P(z)$ is an inductive property of order $n+1$, $P(y)$ holds and so $x+y$ is a number of order $n$. This example illustrates well the complexities introduced by the ramified hierarchy.

The complexities are further amplified if one, like Russell as for Frege, defines even basic objects like natural numbers as classes of classes. For instance the number 2 is defined as the class of all classes of individuals having exactly two elements. We again obtain natural numbers of different orders in the ramified hierarchy. Besides Russell himself, and despite all these complications, Chwistek tried to develop arithmetic in a ramified way (see Chwistek 1948)[^chwistek-1948], and the interest of such an analysis was stressed by Skolem (see Skolem 1970)[^skolem-1970]. See Burgess and Hazen 1998 for a recent development. Weyl, in *Das Kontinuum* (Weyl 1918)[^weyl-1918], developed a substantial part of analysis on a predicative basis, without the axiom of reducibility, by restricting himself in effect to the first level of the ramified hierarchy.

Another mathematical example, often given, of an impredicative definition is the definition of least upper bound of a bounded class of real numbers. If we identify a real with the set of rationals that are less than this real, we see that this least upper bound can be defined as the union of all elements in this class. Let us identify subsets of the rationals as predicates. For example, for rational numbers $q$, $P(q)$ holds iff $q$ is a member of the subset identified as $P$. Now, we define the predicate $L_C$ (a subset of the rationals) to be the least upper bound of class $C$ as: $$\forall q[L_C(q) \leftrightarrow \exists P[C(P) \wedge P(q)]]$$ which is impredicative: we have defined a predicate $L$ by an existential quantification over all predicates. In the ramified hierarchy, if $C$ is a class of first-order classes of rationals, then $L$ will be a second-order class of rationals. One obtains then not one notion or real numbers, but real numbers of different orders $1, 2, \dots$ The least upper bound of a collection of reals of order 1 will then be at least of order 2 in general.

As we saw earlier, yet another example of an impredicative definition is given by Leibniz’ definition of equality. For Leibniz, the predicate “is equal to $a$” is true for $b$ iff $b$ satisfies all the predicates satisfied by $a$.

How should one deal with the complications introduced by the ramified hierarchy? Russell showed, in the introduction to the second edition to *Principia Mathematica*, that these complications can be avoided in some cases. He even thought, in Appendix B of the second edition of *Principia Mathematica*, that the ramified hierarchy of natural numbers of order $1,2,\dots$ collapses at order 5 for defining the reflexive transitive closure of a relation. However, Gödel later found a problem in his argument (Gödel 1944)[^gödel-1944], and indeed, it was shown by Myhill 1974 that this hierarchy actually does not collapse at any finite level. A similar problem, discussed by Russell in the introduction to the second edition to *Principia Mathematica* arises in the proof of Cantor’s theorem that there cannot be any injective functions from the collection of all predicates to the collection of all objects (the version of Russell’s paradox in Frege’s system that we presented in the introduction). Can this be done in a ramified hierarchy? Russell doubted that this could be done within a ramified hierarchy of predicates and this was indeed later confirmed (see Chwistek 1926, Fitch 1939 and Heck 1996)[^chwistek-1926][^fitch-1939][^heck-1996].

Because of these problems, Russell and Whitehead introduced in the first edition of *Principia Mathematica* the following *reducibility* axiom: the hierarchy of predicates, first-order, second-order, etc., collapses at level 1. This means that for any predicate of any order, there is a predicate of the first-order level which is equivalent to it. In the case of equality for instance, we postulate a first-order relation “$a = b$” which is equivalent to “$a$ satisfies all properties that $b$ satisfies”. The motivation for this axiom was purely pragmatic. Without it, all basic mathematical notions, like real or natural numbers are stratified into different orders. Also, despite the apparent circularity of impredicative definitions, the axiom of reducibility does not seem to lead to inconsistencies.

As noticed however first by Chwistek, and later by Ramsey, in the presence of the axiom of reducibility, there is actually no point in introducing the ramified hierarchy at all! It is much simpler to accept impredicative definitions from the start. The simple “extensional” hierarchy of individuals, classes, classes of classes, … is then enough. We get in this way the simpler systems formalised in Gödel 1931 or Church 1940 that were presented above.

The axiom of reducibility draws attention to the problematic status of impredicative definitions. To quote Weyl 1946, the axiom of reducibility “is a bold, an almost fantastic axiom; there is little justification for it in the real world in which we live, and none at all in the evidence on which our mind bases its constructions”! So far, no contradictions have been found using the reducibility axiom. However, as we shall see below, proof-theoretic investigations confirm the extreme strength of such a principle.

The idea of the ramified hierarchy has been extremely important in mathematical logic. Russell considered only the finite iteration of the hierarchy: first-order, second-order, etc., but from the beginning, the possibility of extending the ramification transfinitely was considered. Poincaré (1909)[^poincaré-1909] mentions the work of Koenig in this direction. For the example above of numbers of different order, he also defines a number to be inductive of order *ω* if it is inductive of all finite orders. He then points out that $x+y$ is inductive of order *ω* if both $x$ and $y$ are. This shows that the introduction of transfinite orders can in some case play the role of the axiom of reducibility. Such transfinite extension of the ramified hierarchy was analysed further by Gödel, who noticed the key fact that the following form of the reducibility axiom is actually provable. Gödel’s hierarchy of constructible sets is defined by $$L_0 = \emptyset,\qquad L_{\alpha+1} = \mathrm{Def}(L_\alpha),\qquad L_\lambda = \bigcup_{\alpha<\lambda} L_\alpha \quad(\lambda \text{ limit}),$$ where $\mathrm{Def}(L_\alpha)$ is the collection of subsets of $L_\alpha$ definable over $(L_\alpha,\in)$ with parameters. It can be seen as the ramified hierarchy continued into the transfinite, a definition at level $\alpha+1$ being allowed to quantify over all objects of level *α*, of whatever type, and not only over properties of natural numbers; this is how Gödel himself presents it (Gödel \*1940a, p. 178, where he speaks of “an axiom of reducibility for transfinite orders”)[^gödel-1940a]. Gödel’s “fundamental theorem”, which he describes as “the corrected core of the so-called Russellian axiom of reducibility” (Gödel \*1939b, p. 143)[^gödel-1939b], states that, in $L$, every set of natural numbers appears at some level $<\omega_1$. Since every level below $\omega_1$ is countable, the hierarchy stops producing new sets of natural numbers at $\omega_1$, the least uncountable ordinal, and the collection of all of them has cardinality $\aleph_1$ (both lectures are in Gödel [CW3]; see also Prawitz 1970)[^prawitz-1970]. Seen from outside $L$, this closure point is $\omega_1^L$, which may be countable (for instance if $0^\#$ exists), in which case the constructible sets of natural numbers form a countable collection. If, on the other hand, definitions may only quantify over previously defined properties *of natural numbers*, one obtains the ramified analytical hierarchy, which stops producing new sets of natural numbers already at a countable ordinal $\beta_0$ (Cohen, Putnam, Gandy; see Boyd, Hensel and Putnam 1969)[^boyd-1969].

Gödel’s observation was a strong motivation behind his model of constructible sets. In this model the collection of all subsets of the set of natural numbers (represented by predicates) is of cardinality $\aleph_1$ and is similar to the ramified hierarchy. This model satisfies in this way the Continuum Hypothesis, and gives a relative consistency proof of this axiom. (The motivation of Gödel was originally only to build a model where the collection of all subsets of natural numbers is well-ordered.)

The ramified hierarchy has been also the source of much work in proof theory. After the discovery by Gentzen that the consistency of Arithmetic could be proved by transfinite induction (over decidable predicates) along the ordinal $\varepsilon_0$, the natural question was to find the corresponding ordinal for the different levels of the ramified hierarchy. Schütte (1960)[^schütte-1960] found that for the first level of the ramified hierarchy, that is if we extend arithmetic by quantifying only over first-order properties, we get a system of ordinal strength $\varepsilon_{\varepsilon_0}$. For the second level we get the ordinal strength $\varepsilon_{\varepsilon_{\varepsilon_0}}$, etc. We recall that $\varepsilon_\alpha$ denotes the *α*-th *ε*-ordinal number, an *ε*-ordinal number being an ordinal *β* such that $\omega^\beta = \beta$, see Schütte (1960)[^schütte-1960].

Gödel stressed the fact that his approach to the problem of the continuum hypothesis was not constructive, since it needs the uncountable ordinal $\omega_1$, and it was natural to study the ramified hierarchy along constructive ordinals. After preliminary works of Lorenzen (1955)[^lorenzen-1955] and Wang (1954)[^wang-1954], Schütte analysed what happens if we proceed in the following more constructive way. Since arithmetic has for ordinal strength $\varepsilon_0$ we consider first the iteration of the ramified hierarchy up to $\varepsilon_0$. Schütte computed the ordinal strength of the resulting system and found an ordinal strength $u(1) > \varepsilon_0$. We iterate then ramified hierarchy up to this ordinal $u(1)$ and get a system of ordinal strength $u(2) > u(1)$, etc. Each $u(k)$ can be computed in terms of the so-called Veblen hierarchy: $u(k+1)$ is $\varphi_{u(k)}(0)$. The limit of this process gives an ordinal called $\Gamma_0$: if we iterate the ramified hierarchy up to the ordinal $\Gamma_0$ we get a system of ordinal strength $\Gamma_0$. Such an ordinal was obtained independently about the same time by S. Feferman (1964)[^feferman-1964]. It has been claimed that $\Gamma_0$ plays for predicative systems a role similar to $\varepsilon_0$ for Arithmetic. Recent proof-theoretical works however are concerned with systems having bigger proof-theoretical ordinals that can be considered predicative in an extended sense. This is the programme of *metapredicativity* (Strahm 1999; Jäger, Kahle and Studer 2001; Jäger and Strahm 2001; see Jäger 2005 for an overview)[^jäger-2005][^jäger-2001][^jäger-2001-2][^strahm-1999], which studies systems whose proof-theoretic ordinals lie beyond $\Gamma_0$ but which can still be analysed with the methods of predicative proof theory. There is a partial parallel with the work on universes in type theory (Palmgren 1998)[^palmgren-1998]. Universe constructions without well-founded trees ($W$-types), such as superuniverses and Palmgren’s higher universe operators, have metapredicative strength beyond $\Gamma_0$. In Martin-Löf type theory, with *Π*, $\Sigma$, natural numbers and the full elimination rules, adding $W$-types of infinitely branching trees, such as the type of Brouwer ordinals, or a Mahlo universe (Setzer 2000)[^setzer-2000] leads beyond this region. The Bachmann–Howard ordinal is then already a lower bound, and the ordinal analysis requires impredicative methods (collapsing functions); see Setzer 1993, where the proof-theoretic ordinal of Martin-Löf type theory with $W$-types and one universe is computed. “Impredicative” is meant here in this sense, which concerns the methods of analysis, as distinct from merely exceeding $\Gamma_0$ (Jäger 2005)[^jäger-2005]. In particular, the “metapredicative Mahlo” of Jäger and Strahm is much weaker than Setzer’s Mahlo universe. Martin-Löf type theory with a hierarchy of universes but without $W$-types has proof-theoretic ordinal $\Gamma_0$ (Feferman 1982)[^feferman-1982]. Martin-Löf’s notion of predicativity (see Section 6), however, is based on the meaning explanation of the rules rather than on proof-theoretic strength. It accepts $W$-types, and thus lies beyond predicativity in the sense of Feferman and Schütte.

Besides these proof theoretic investigations related to the ramified hierarchy, much work has been devoted in proof theory to analysing the consistency of the axiom of reducibility, or, equivalently, the consistency of impredicative definitions. Following Gentzen’s analysis of the cut-elimination property in the sequent calculus, Takeuti (1955)[^takeuti-1955] found an elegant sequent formulation of simple type theory (without ramification) and made the bold conjecture that cut-elimination should hold for this system. This conjecture seemed at first extremely dubious given the circularity of impredicative quantification, which is well reflected in this formalism. The left rule for the second-order quantifier is indeed $$\dfrac{A[X:=T],\ \Gamma \vdash \Delta}{\forall X[A(X)],\ \Gamma \vdash \Delta}$$ where $T$ is any term predicate, which may itself involve a quantification over all predicates. Thus the formula $A[X:=T]$ may be itself much more complex than the formula $A(X)$.

One early result is that cut-elimination for Takeuti’s impredicative system implies in a finitary way the consistency of second-order Arithmetic. (One shows that this implies the consistency of a suitable form of infinity axiom, see Andrews 2002.)[^andrews-2002] Following work by Schütte (1960b)[^schütte-1960b], it was later shown by W. Tait (1966)[^tait-1966] for second-order logic (see also Prawitz 1967)[^prawitz-1967], and by M. Takahashi (1967)[^takahashi-1967] and D. Prawitz (1968)[^prawitz-1968] for full simple type theory, that indeed the cut-elimination property holds. These proofs are semantic and non-constructive: they show that every provable sequent has a cut-free proof, not that a given cut-elimination procedure terminates. They have to use a stronger proof theoretic principle, as it should be according to the incompleteness theorem. The termination of cut-elimination was obtained only later, as a consequence of Girard’s normalisation theorem (see Section 6).

What is important here is that these studies have revealed the extreme power of impredicative quantification or, equivalently, the extreme power of the axiom of reducibility. This confirms in some way the intuitions of Poincaré and Russell. The proof-theoretic strength of second-order Arithmetic is way above all ramified extensions of Arithmetic considered by Schütte. On the other hand, despite the circularity of impredicative definitions, which is made so explicit in Takeuti’s calculus, no paradoxes have been found yet in second-order Arithmetic.

Another research direction in proof theory has been to understand how much of impredicative quantification can be explained from principles that are available in intuitionistic mathematics. The strongest such principles are strong forms of inductive definitions. With such principles, one can explain a limited form of an impredicative quantification, called $\Pi^1_1$-comprehension, where one uses only one level of impredicative quantification over predicates. Interestingly, most impredicative definitions that occur in ordinary mathematics, such as Leibniz equality or the least upper bound of a bounded set of reals, can be justified using $\Pi^1_1$-comprehension. In fact many of them, including these two, need only arithmetical comprehension, as the program of reverse mathematics (Friedman 1975, Simpson 2009)[^friedman-1975][^simpson-2009] has shown in detail. A typical use of $\Pi^1_1$-comprehension is the Cantor–Bendixson theorem (it is in fact equivalent to $\Pi^1_1$-comprehension in reverse mathematics), whose analysis by an inductive definition goes back to Lorenzen (1955)[^lorenzen-1955] and Kreisel (1959)[^kreisel-1959] (see Coquand, Lombardi and Neuwirth 2026)[^coquand-2026]. The reduction of $\Pi^1_1$-comprehension to inductive definitions was first achieved by Takeuti (1967)[^takeuti-1967] in a quite indirect way, and was later simplified by Buchholz and Schütte using the so-called $\Omega$-rule (Buchholz and Schütte 1988)[^buchholz-1988]. It was also reduced to intuitionistic theories of finitely iterated inductive definitions (Buchholz, Feferman, Pohlers and Sieg 1981)[^buchholz-1981]; this is where the connection with well-founded trees ($W$-types) and Martin-Löf type theory lies. These results can be seen as a constructive explanation of some restricted, but nontrivial, uses of impredicative definitions.

## 4. Type Theory / Set Theory

Type theory can be used as a foundation for mathematics, and indeed, it was presented as such by Russell in his 1908 paper, which appeared the same year as Zermelo’s paper, presenting set theory as a foundation for mathematics.

It is clear intuitively how we can explain type theory in set theory: a type is simply interpreted as a set, and function types $A \to B$ can be explained using the set theoretic notion of function (as a functional relation, i.e., a set of pairs of elements). The type $A \to o$ corresponds to the powerset operation.

The other direction is more interesting. How can we explain the notion of sets in terms of types? There is an elegant solution, due to A. Miquel (2001)[^miquel-2001], which complements previous works by P. Aczel (1978)[^aczel-1978] and which has also the advantage of explaining non necessarily well-founded sets à la Finsler. One simply interprets a set as a pointed graph (where the arrow in the graph represents the membership relation), an idea that goes back to Aczel’s work on non-well-founded sets (Aczel 1988)[^aczel-1988]. This is very conveniently represented in type theory, a pointed graph being simply given by a type $A$ and a pair of elements $$a : A,\qquad R : A \to A \to o$$ We can then define in type theory when two such sets $A, a, R$ and $B, b, S$ are equal: this is the case iff there is a bisimulation $T$ between $A$ and $B$ such that $T\,a\,b$ holds. A bisimulation is a relation $$T : A \to B \to o$$ such that whenever $T\,x\,y$ and $R\,x\,u$ hold, there exists $v$ such that $T\,u\,v$ and $S\,y\,v$ hold, and whenever $T\,x\,y$ and $R\,y\,v$ hold, there exists $u$ such that $T\,u\,v$ and $R\,x\,u$ hold. We can then define the membership relation: the set represented $B, b, S$ is a member of the set represented by $A, a, R$ iff there exists $a_1$ such that $R\,a_1\,a$ and $A, a_1, R$ and $B, b, S$ are bisimilar.

It can then be checked that all the usual axioms of set theory extensionality, power set, union, comprehension over bounded formulae (and even antifoundation, so that the membership relation does not need to be well-founded) hold in this simple model. (A bounded formula is a formula where all quantifications are of the form $\forall x \in a\dots$ or $\exists x \in a\dots$). In this way it can be shown that Church’s simple type theory, with an axiom of infinity, is equiconsistent with the bounded version of Zermelo’s set theory (see Mathias 2001, where this set theory is called Mac Lane set theory)[^mathias-2001].

## 5. Type Theory / Category Theory

There are deep connections between type theory and category theory. We limit ourselves to presenting two applications of type theory to category theory: the constructions of the free cartesian closed category and of the free Boolean topos (see the entry on category theory for an explanation of “cartesian closed” and “topos”).

For building the free cartesian closed category, we extend simple type theory with the type 1 (unit type) and the product type $A \times B$, for $A, B$ types. The terms are extended by adding pairing operations and projections and a special element of type 1. As in Lambek and Scott 1986, one can then define a notion of typed conversions between terms, and show that this relation is decidable. One can then show (Lambek 1980, Lambek and Scott 1986)[^lambek-1980][^lambek-1986] that the category with types as objects and as morphisms from $A$ to $B$ the set of closed terms of type $A \to B$ (with conversion as equality) is the free cartesian closed category. This can be used to show that equality between arrows in this category is decidable.

The theory of types of Church can also be used to build a free topos. Since Church’s type theory is classical, what one obtains is the free *Boolean* topos; the free topos of Lambek and Scott 1986 is obtained by the same construction from an intuitionistic higher-order type theory. For this we take as objects pairs $A, E$ with $A$ a type and $E$ a partial equivalence relation, that is a closed term $E : A \to A \to o$ which is symmetric and transitive. We take as morphisms between $A, E$ and $B, F$ the relations $R : A \to B \to o$ that respect $E$ and $F$ (if $R\,a\,b$ holds then so do $E\,a\,a$ and $F\,b\,b$, and if moreover $E\,a\,a'$ and $F\,b\,b'$ then $R\,a'\,b'$ holds) and that are functional, that is such that for any $a : A$ satisfying $E\,a\,a$ there exists one, and only one (modulo $F$) element $b$ of $B$ such that $F\,b\,b$ and $R\,a\,b$; two such relations are identified when they are provably equivalent. For the subobject classifier we take the pair $o, E$ with $E : o \to o \to o$ defined as $$E\,M\,N = \mathsf{and}\,(\mathsf{imply}\,M\,N)(\mathsf{imply}\,N\,M)$$ One can then show that this category forms a topos, indeed the free Boolean topos.

It should be noted that the type theory in Lambek and Scott 1986 uses a variation of type theory, introduced by Henkin and refined by P. Andrews (2002)[^andrews-2002] which is to have an extensional equality as the only logical connective, i.e., a polymorphic constant $$\mathsf{eq}: A \to A \to o$$ and to define all logical connectives from this connective and constants $T, F : o$. For instance, one defines $$\forall P =_{df} \mathsf{eq}\,(\lambda x.\,T)\,P$$ The equality at type $o$ is logical equivalence.

One advantage of the intensional formulation is that it allows for a direct notation of proofs based on *λ*-calculus (Martin-Löf 1971 and Coquand 1986)[^coquand-1986][^martin-löf-1971]. For further connections between types, sets and categories, see Bell 2012 and Lawvere and Rosebrugh 2003.

## 6. Extensions of Type System, Polymorphism, Paradoxes

We have seen the analogy between the operation $A \to A \to o$ on types and the powerset operation on sets. In set theory, the powerset operation can be iterated transfinitely along the cumulative hierarchy. It is then natural to look for analogous transfinite versions of type theory.

One such extension of Church’s simple type theory is obtained by adding *universes* (Martin-Löf 1975 [1973], 1998)[^martin-löf-1975]. Adding a universe is a reflection process: we add a type $U$ whose objects are the types considered so far. For Church’s simple type theory we will have $$o : U,\quad i : U\quad\text{and}\quad A \to B : U \text{ if } A : U,\ B : U$$ and, furthermore, $A$ is a type if $A : U$. We can then consider types such as $$(A : U) \to A \to A$$ and functions such as $$\mathit{id} = \lambda A.\,\lambda x.\,x : (A : U) \to A \to A$$ The function $\mathit{id}$ takes as argument a “small” type $A : U$ and an element $x$ of type $A$, and outputs an element of type $A$. More generally if $T(A)$ is a type under the assumption $A : U$, one can form the dependent type $$(A : U) \to T(A)$$ That $M$ is of this type means that $M\,A : T(A)$ whenever $A : U$. We get in this way extensions of type theory whose strength is similar to the one of Zermelo’s set theory (Miquel 2001)[^miquel-2001]. More powerful form of universes are considered in (Palmgren 1998)[^palmgren-1998]. Miquel (2003)[^miquel-2003] presents a version of type theory of strength equivalent to the one of Zermelo–Fraenkel.

One very strong form of universe is obtained by adding the axiom $U : U$. This was suggested by P. Martin-Löf in 1971 (Martin-Löf 1971)[^martin-löf-1971]. J.Y. Girard showed that the resulting type theory is inconsistent as a logical system (Girard 1972)[^girard-1972]. Though it seems at first that one could directly reproduce Russell’s paradox using a set of all sets, such a direct paradox is actually not possible due to the difference between sets and types. Indeed the derivation of a contradiction in such a system is subtle and has been rather indirect (though, as noticed in Miquel 2001, it can now be reduced to Russell’s paradox by representing sets as pointed graphs)[^miquel-2001]. J.Y. Girard first obtained his paradox for a weaker system, System U$^-$. This paradox was refined later (Coquand 1994 and Hurkens 1995)[^coquand-1994][^hurkens-1995]. (The notion of pure type system, introduced in Barendregt 1992, is convenient for getting a sharp formulation of these paradoxes.)[^barendregt-1992] Instead of the axiom $U : U$ one assumes only $$(A : U) \to T(A) : U$$ if $T(A) : U\ [A : U]$. Notice the circularity, indeed of the same kind as the one that is rejected by the ramified hierarchy: we define an element of type $U$ by quantifying over all elements of $U$. For instance the type $$(A : U) \to A \to A : U$$ will be the type of the polymorphic identity function. Despite this circularity, J.Y. Girard was able to show normalisation for type systems with this form of polymorphism, such as his System F and its higher-order extension F$_\omega$; these systems are thus consistent. By contrast, if one adds this form of polymorphism to Church’s simple type theory at the level of types, allowing types defined by quantification over all types (Girard’s System U$^-$), the resulting system is inconsistent as a logical system, i.e., all propositions (terms of type $o$) are provable.

J.Y. Girard’s motivation for considering a type system with polymorphism was to extend Gödel’s *Dialectica* (Gödel 1958)[^gödel-1958] interpretation to second-order arithmetic. He proved normalisation using the reducibility method, that had been introduced by Tait (1967)[^tait-1967] while analysing Gödel 1958. It is quite remarkable that the circularity inherent in impredicativity does not result in non-normalisable terms. (Girard’s argument was then used to show that cut-elimination terminates in Takeuti’s sequent calculus presented above.) A similar system was introduced independently by J. Reynolds (1974)[^reynolds-1974] while analysing the notion of polymorphism in computer science (see also Reynolds 1984, which shows that polymorphism is not set-theoretic)[^reynolds-1984].

Martin-Löf’s introduction of a type of all types comes from the identification of the concept of propositions and types, suggested by the work of Curry and Howard (Howard 1980)[^howard-1980]. It is worth recalling here his three motivating points:

1. Russell’s definition of types as ranges of significance of propositional functions
2. the fact that one needs to quantify over all propositions (impredicativity of simple type theory)
3. identification of proposition and types

Given (1) and (2) we should have a type of propositions (as in simple type theory), and given (3) this should also be the type of all types. Girard’s paradox shows that one cannot have (1), (2) and (3) simultaneously. Martin-Löf’s choice was to take away (2), restricting type theory to be predicative (and, indeed, the notion of universe appeared first in type theory as a predicative version of the type of all types). The alternative choice of taking away (3) is discussed in Coquand 1986.

Type theory is also the basis of proof assistants, starting with N.G. de Bruijn’s Automath project (de Bruijn 1980)[^bruijn-1980], where the identification of propositions and types was found independently. Many current proof assistants are based on dependent type theories of the kind described in this section, which explains much of the present importance of type theory.

## 7. Univalent Foundations

The connections between type theory, set theory and category theory get a new light through the work on Univalent Foundations and the Axiom of Univalence, introduced by V. Voevodsky around 2009–2010 (see Voevodsky 2015 and [HoTT 2013, Other Internet Resources])[^voevodsky-2015]. This involves in an essential way the extension of type theory described in the previous section, in particular dependent types, the view of propositions as types, and the notion of universe of types. These developments are also relevant for discussing the notion of structure, the importance of which was for instance emphasized in Russell 1959.

Martin-Löf 1975 [1973] introduced a new basic type $\mathrm{Id}_A(a,b)$, if $a$ and $b$ are in the type $A$, which can be thought as the type of equality proofs of the element $a$ and $b$. An important feature of this new type is that it can be iterated, so that we can consider the type $\mathrm{Id}_{\mathrm{Id}_A(a,b)}(p,q)$ if $p$ and $q$ are of type $\mathrm{Id}_A(a,b)$. If we think of a type as a special kind of set, it is natural to conjecture that such a type of equality proofs is always inhabited for any two equality proofs $p$ and $q$. Indeed, intuitively, there seems to be at most one equality proof between two elements $a$ and $b$. Surprisingly, Hofmann and Streicher (1994, 1998) designed a model of dependent type theory where this is not valid, that is a model where there can be different proofs that two elements are equal. In this model, a type is interpreted by a groupoid and the type $\mathrm{Id}_A(a,b)$ by the set of isomorphisms between $a$ and $b$, set which may have more than one element. The existence of this model has the consequence that it cannot be proved in general in type theory that an equality type has at most one element.

This groupoid interpretation has been generalized in the following way, which gives an intuitive interpretation of the identity type. A type is interpreted by a topological space, up to homotopy, and a type $\mathrm{Id}_A(a,b)$ is interpreted by the type of paths connecting $a$ and $b$. (See Awodey et al. 2013 and [HoTT 2013, Other Internet Resources].)[^awodey-2013] The first homotopy-theoretic models of identity types were given by Awodey and Warren (2009). Voevodsky built a model of type theory with univalent universes in simplicial sets (Kapulkin and Lumsdaine 2021)[^kapulkin-2021], and cubical models (Cohen, Coquand, Huber and Mörtberg 2018)[^cohen-2018] give the Axiom of Univalence a computational content. The homotopical point of view also led to *higher inductive types*, which allow one to define types, such as the circle, by generators both for elements and for equality proofs (see [HoTT 2013] and Lumsdaine and Shulman 2020)[^lumsdaine-2020].

Voevodsky 2015 introduced the following stratification of types. (This stratification was motivated in part by this interpretation of a type as a topological space, but can be understood directly without reference to this interpretation.) We say that a type $A$ is a *proposition* if we have $\mathrm{Id}_A(a,b)$ for any element $a$ and $b$ of $A$ (this means that the type $A$ has at most one element). We say that a type $A$ is a *set* if the type $\mathrm{Id}_A(a,b)$ is a proposition for any element $a$ and $b$ of $A$. We say that a type $A$ is a *groupoid* if the type $\mathrm{Id}_A(a,b)$ is a set for any element $a$ and $b$ of $A$. The justification of this terminology is that it can be shown, only using the rules of type theory, that any such type can indeed be seen as a groupoid in the usual categorical sense, where the objects are the elements of this type, the set of morphisms between $a$ and $b$ being represented by the set $\mathrm{Id}_A(a,b)$. The composition is the proof of transitivity of equality, and the identity morphism is the proof of reflexivity of equality. The fact that each morphism has an inverse corresponds to the fact that identity is a symmetric relation. This stratification can then be extended and we can define when a type is a 2-groupoid, 3-groupoid and so on. In this view, type theory appears as a vast generalization of set theory, since a set is a particular kind of type.

Voevodsky 2015 introduces also a notion of *equivalence* between types, notion which generalizes in a uniform way the notions of logical equivalence between propositions, bijection between sets, categorical equivalence between groupoids, and so on. We say that a map $f : A \to B$ is an equivalence if, for any element $b$ in $B$ the type of pairs $a, p$ where $p$ is of type $\mathrm{Id}_B(f\,a, b)$, is a proposition and is inhabited. This expresses in a strong way that an element in $B$ is the image of exactly one element in $A$, and if $A$ and $B$ are sets, we recover the usual notion of bijection between sets. (In general if $f : A \to B$ is an equivalence, then we have a map $B \to A$, which can be thought of as the inverse of $f$.) It can be shown for instance that the identity map is always an equivalence. Let $\mathrm{Equiv}(A,B)$ be the type of pairs $f, p$ where $f : A \to B$ and $p$ is a proof that $f$ is an equivalence. Using the fact that the identity map is an equivalence we have an element of $\mathrm{Equiv}(A,A)$ for any type $A$. This implies that we have a map $$\mathrm{Id}_U(A,B) \to \mathrm{Equiv}(A,B)$$ and the Axiom of Univalence states that this map is an equivalence. In particular, we have the implication $$\mathrm{Equiv}(A,B) \to \mathrm{Id}_U(A,B)$$ and so if there is an equivalence between two small types then these types are equal.

This Axiom can be seen as a strong form of the extensionality principle. It indeed generalizes the Axiom of propositional extensionality mentioned by Church 1940, which states that two logically equivalent propositions are equal. Surprisingly, it also implies the Axiom of function extensionality, Axiom 10 in Church 1940, which states that two pointwise equal functions are equal (Voevodsky 2015)[^voevodsky-2015]. It also directly implies that two isomorphic sets are equal, that two categorically equivalent groupoids are equal, and so on.

This can be used to give a formulation of the notion of transport of structures (Bourbaki 1958)[^bourbaki-1958] along equivalences. For instance, let $M\,A$ be the type of monoid structures on the set $A$: this is the type of tuples $m, e, p$ where $m$ is a binary operation on $A$ and $e$ an element of $A$ and $p$ a proof that these elements satisfy the usual monoid laws. The rule of substitution of equal by equal takes the form $$\mathrm{Id}_U(A,B) \to M\,A \to M\,B$$ If there is a bijection between $A$ and $B$ they are equal by the Axiom of Univalence, and we can use this implication to transport any monoid structure of $A$ in a monoid structure of $B$.

Both Russell 1919 and Russell 1959 stress the importance of the notion of structure. For instance, in Chapter VI of Russell 1919, it is noticed that two similar relations essentially have the same properties, and hence have the same “structure”. (The notion of “similarity” of relations was introduced in Russell 1901.)[^russell-1901] We can also use this framework to refine Russell’s discussions on the notion of structure. For instance, let $\mathit{Monoid}$ be the type of pairs $A, p$ where $p$ is an element of $M\,A$. Two such pairs $A, p$ and $B, q$ are isomorphic if there exists a bijection $f$ from $A$ to $B$ such that $q$ is equal to the transport of structure of $p$ along $f$. A consequence of the Axiom of Univalence is that two isomorphic elements of the type $\mathit{Monoid}$ are equal, and hence share the same properties. Notice that such a general transport of properties is not possible when structures are formulated in a set theoretic framework. Indeed, in a set theoretic framework, it is possible to formulate properties using the membership relations, for instance the property that the carrier set of the structure contains the natural number 0, property that is not preserved in general by isomorphisms. Intuitively, the set theoretical description of a structure is not abstract enough since we can talk about the way this structure is built up. This difference between set theory and type theory is yet another illustration of the characterization by J. Reynolds 1983 of a type structure as a “syntactical discipline for enforcing level of abstraction”.

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=type-theory). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/type-theory/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=type-theory&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/type-theory/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

- Kubota, K., 2018, “[Foundations of Mathematics. Genealogy and Overview](https://www.owlofminerva.net/files/fom.pdf)”, manuscript, draft of March 27, 2018.
- [HoTT 2013], [*Homotopy Type Theory: Univalent Foundations of Mathematics*](https://homotopytypetheory.org/book/), Institute for Advanced Study.

## Related Entries

Russell, Bertrand | category theory | Frege, Gottlob | Frege, Gottlob: theorem and foundations for arithmetic | logic: paraconsistent | mathematics: inconsistent | *Principia Mathematica* | type theory: Church’s type theory | type theory: intuitionistic

[^aczel-1978]: Aczel, P., 1978, “The type theoretic interpretation of constructive set theory”, *Logic Colloquium ’77*, Amsterdam: North-Holland, 55–66.

[^aczel-1988]: –––, 1988, *Non-well-founded sets* (CSLI Lecture Notes: Volume 14), Stanford: CSLI Publications.

[^andrews-2002]: Andrews, P., 2002, *An introduction to mathematical logic and type theory: to truth through proof* (Applied Logic Series: Volume 27), Dordrecht: Kluwer Academic Publishers, second edition.

[^awodey-2001]: Awodey, S. and A.W. Carus, 2001, “Carnap, completeness and categoricity: the Gabelbarkeitssatz of 1928”, *Erkenntnis*, 54: 145–171.

[^awodey-2013]: Awodey, S., Á. Pelayo, and M. Warren, 2013, “Voevodsky’s Univalence Axiom in Homotopy Type Theory”, *Notices of the American Mathematical Society*, 60(9): 1157–1164.

[^awodey-2009]: Awodey, S., and M. Warren, 2009, “Homotopy theoretic models of identity types”, *Mathematical Proceedings of the Cambridge Philosophical Society*, 146(1): 45–55.

[^barendregt-1997]: Barendregt, H., 1997, “The impact of the lambda calculus in logic and computer science”, *Bulletin of Symbolic Logic*, 3(2): 181–215.

[^barendregt-1992]: –––, 1992, *Lambda calculi with types* (Handbook of Logic in Computer Science: Volume 2), Oxford, New York: Oxford University Press, 117–309.

[^bell-2012]: Bell, J.L., 2012, “Types, Sets and Categories”, in Akihiro Kanamori (ed.), *Handbook of the History of Logic. Volume 6: Sets and Extensions in the Twentieth Century*, Amsterdam: North Holland.

[^bourbaki-1958]: Bourbaki, N., 1958, *Théorie des Ensembles*, 3rd edition, Paris: Hermann.

[^boyd-1969]: Boyd, R., G. Hensel, and H. Putnam, 1969, “A recursion-theoretic characterization of the ramified analytical hierarchy”, *Transactions of the American Mathematical Society*, 141: 37–62.

[^bruijn-1980]: de Bruijn, N. G., 1980, “A survey of the project AUTOMATH”, in *To H. B. Curry: essays on combinatory logic, lambda calculus and formalism*, London-New York: Academic Press, 579–606.

[^burgess-1998]: Burgess J. P., and A. P. Hazen, 1998, “Predicative Logic and Formal Arithmetic”, *Notre Dame J. Formal Logic*, 39(1): 1–17.

[^buchholz-1988]: Buchholz, W., and K. Schütte, 1988, *Proof theory of impredicative subsystems of analysis* (Studies in Proof Theory: Monograph 2), Naples: Bibliopolis.

[^buchholz-1981]: Buchholz, W., S. Feferman, W. Pohlers, and W. Sieg, 1981, *Iterated Inductive Definitions and Subsystems of Analysis: Recent Proof-Theoretical Studies* (Lecture Notes in Mathematics: Volume 897), Berlin: Springer.

[^church-1940]: Church, A., 1940, “A formulation of the simple theory of types”, *Journal of Symbolic Logic*, 5: 56–68

[^church-1984]: –––, 1984, “Russell’s theory of identity of propositions”, *Philosophia Naturalis*, 21: 513–522

[^chwistek-1926]: Chwistek, L., 1926, “Ueber die Hypothesen der Mengenlehre”, *Mathematische Zeitschrift*, 25: 439–473

[^chwistek-1948]: –––, 1948, *The Limits of Science: Outline of Logic and of the Methodology of the Exact Sciences*, London: Routledge and Kegan Paul.

[^cohen-2018]: Cohen, C., T. Coquand, S. Huber, and A. Mörtberg, 2018, “Cubical type theory: a constructive interpretation of the univalence axiom”, in *21st International Conference on Types for Proofs and Programs (TYPES 2015)* (Leibniz International Proceedings in Informatics: Volume 69), T. Uustalu (ed.), , Dagstuhl: Schloss Dagstuhl–Leibniz-Zentrum für Informatik, 5:1–5:34.

[^coquand-1986]: Coquand, T., 1986, “An analysis of Girard’s paradox”, *Proceedings of the IEEE Symposium on Logic in Computer Science*, 227–236.

[^coquand-1994]: –––, 1994, “A new paradox in type theory”, *Studies in the Logical Foundations of Mathematics* (Volume 134), Amsterdam: North-Holland, 555–570.

[^coquand-2026]: Coquand, T., H. Lombardi, and S. Neuwirth, 2026, “In 1955, Paul Lorenzen clears the sky in foundations of mathematics for Hermann Weyl”, in *Pillars of Enduring Strength: Learning from Hermann Weyl*, L. Crosilla, Ø. Linnebo and M. Rathjen (eds.), Oxford: Oxford University Press. [[Coquand et al. 2026 preprint available online](https://arxiv.org/abs/2411.16469)]

[^bois-reymond-1875]: du Bois-Reymond, P., 1875, “Ueber asymptotische Werthe, infinitäre Approximationen und infinitäre Auflösung von Gleichungen”, *Mathematische Annalen*, 8: 363–414.

[^feferman-1964]: Feferman, S., 1964, “Systems of predicative analysis”, *Journal of Symbolic Logic*, 29: 1–30.

[^feferman-1982]: –––, 1982, “Iterated inductive fixed-point theories: application to Hancock’s conjecture”, in *The Patras Logic Symposion*, G. Metakides (ed.), Amsterdam: North-Holland, 171–196.

[^ferreira-2002]: Ferreira, F. and K. Wehmeier, 2002, “On the consistency of the Delta-1-1-CA fragment of Frege’s Grundgesetze”, *Journal of Philosophic Logic*, 31: 301–311.

[^fitch-1939]: Fitch, F. B., 1939, “The hypothesis that infinite classes are similar”, *Journal of Symbolic Logic*, 4: 159–162.

[^friedman-1975]: Friedman, H., 1975, “Some systems of second order arithmetic and their use”, in *Proceedings of the International Congress of Mathematicians (Vancouver 1974)* (Volume 1), Ralph James (ed.), Vancouver: Canadian Mathematical Congress, 235–242.

[^girard-1972]: Girard, J.Y., 1972, *Interprétation fonctionnelle et élimination des coupures de l’arithmétique d’ordre supérieur*, Thèse d’État, Université Paris 7.

[^goldfarb-2005]: Goldfarb, Warren, 2005. “On Gödel’s way in: The influence of Rudolf Carnap.” *Bulletin of Symbolic Logic* 11(2): 185–193.

[^gödel-1995]: Gödel, K., [CW3], *Collected Works* (Volume III: Unpublished Essays and Lectures), S. Feferman, et al. (eds.) Oxford: Oxford University Press, 1995.

[^gödel-1931]: –––, 1931, “Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I”, *Monatshefte für Mathematik und Physik*, 38: 173–198.

[^gödel-1939b]: –––, \*1939b, Lecture at Göttingen [Vortrag Göttingen], in Gödel [CW3].

[^gödel-1940a]: –––, \*1940a, Lecture on the consistency of the continuum hypothesis [Brown University, 1940], in Gödel [CW3].

[^gödel-1944]: –––, 1944, “Russell’s mathematical logic”, in *The philosophy of Bertrand Russell*, P. A. Schilpp (ed.), Evanston: Northwestern University Press, 123–153.

[^gödel-1958]: –––, 1958, “Über eine bisher noch nicht benützte Erweiterung des finiten Standpunktes”, *Dialectica*, 12: 280–287.

[^heck-1996]: Heck, R., Jr., 1996, “The consistency of predicative fragments of Frege’s Grundgesetze der Arithmetik”, *History and Philosophy of Logic*, 17(4): 209–220.

[^heijenoort-1967]: van Heijenoort, 1967, *From Frege to Gödel. A source book in mathematical logic 1879–1931*, Cambridge, MA: Harvard University Press.

[^hindley-1997]: Hindley, R., 1997, *Basic Simple Type Theory*, Cambridge: Cambridge University Press.

[^hodges-2008]: Hodges, W., 2008, “Tarski on Padoa’s Method: a test case for understanding logicians of other traditions”, in *Logic, Navya-Nyāya and Applications: Homage to Bimal Krishna Matilal*, Mihir K. Chakraborti et al. (eds.), London: College Publications, pp. 155–169

[^hofmann-1994]: Hofmann, M. and Th. Streicher, 1994, “The groupoid model refutes uniqueness of identity proofs”, *Proceedings of the Ninth Annual IEEE Symposium on Logic in Computer Science*, Los Alamitos: IEEE Computer Society Press, 208–212.

[^hofmann-1998]: ––– , 1998, “The Groupoid interpretation of Type Theory”, in *Twenty-five years of constructive type theory* (Oxford Logic Guides: Volume 36), Oxford, New York: Oxford University Press, 83–111.

[^howard-1980]: Howard, W. A., 1980, “The formulae-as-types notion of construction”, in *To H. B. Curry: essays on combinatory logic, lambda calculus and formalism*, London, New York: Academic Press, 480–490.

[^hurkens-1995]: Hurkens, A. J. C., 1995, “A simplification of Girard’s paradox. Typed lambda calculi and applications”, in *Lecture Notes in Computer Science* (Volume 902), Berlin: Springer: 266–278.

[^jäger-2005]: Jäger, G., 2005, “Metapredicative and explicit Mahlo: a proof-theoretic perspective”, in *Logic Colloquium 2000* (Lecture Notes in Logic: Volume 19), Association for Symbolic Logic, 272–293.

[^jäger-2001]: Jäger, G., R. Kahle, and T. Studer, 2001, “Universes in explicit mathematics”, *Annals of Pure and Applied Logic*, 109: 141–162.

[^jäger-2001-2]: Jäger, G., and T. Strahm, 2001, “Upper bounds for metapredicative Mahlo in explicit mathematics and admissible set theory”, *Journal of Symbolic Logic*, 66: 935–958.

[^kapulkin-2021]: Kapulkin, C., and P. L. Lumsdaine, 2021, “The simplicial model of univalent foundations (after Voevodsky)”, *Journal of the European Mathematical Society*, 23(6): 2071–2126.

[^kreisel-1959]: Kreisel, G., 1959, “Analysis of the Cantor–Bendixson theorem by means of the analytic hierarchy”, *Bulletin de l’Académie Polonaise des Sciences*, 7: 621–626.

[^lambek-1980]: Lambek, J., 1980. “From *λ*-calculus to Cartesian Closed Categories” in *To H.B. Curry: Essays on Combinatory Logic, \(\lambda\)-calculus and Formalism*, J. Seldin and J. Hindley (eds.), London, New York: Academic Press, pp. 375–402.

[^lambek-1986]: Lambek, J., and P. J. Scott, 1986, *Introduction to higher order categorical logic* (Cambridge Studies in Advanced Mathematics: Volume 7), Cambridge: Cambridge University Press; reprinted 1988.

[^lawvere-2003]: Lawvere, F. W. and R. Rosebrugh, 2003, *Sets for mathematics*, Cambridge: Cambridge University Press.

[^lorenzen-1955]: Lorenzen, P., 1955, *Einführung in die operative Logik und Mathematik*, Berlin: Springer.

[^lumsdaine-2020]: Lumsdaine, P. L., and M. Shulman, 2020, “Semantics of higher inductive types”, *Mathematical Proceedings of the Cambridge Philosophical Society*, 169(1): 159–208.

[^martin-löf-1970]: Martin-Löf, P., 1970, *Notes on constructive mathematics*, Stockholm: Almqvist & Wiksell.

[^martin-löf-1971]: –––, 1971, *A Theory of Types*, Technical Report 71–3, Stockholm: Stockholm University.

[^martin-löf-1998]: –––, 1998, “An intuitionistic theory of types”, in *Twenty-five years of constructive type theory* (Oxford Logic Guides: Volume 36), Oxford, New York: Oxford University Press, 127–172.

[^martin-löf-1975]: –––, 1975 [1973], “An intuitionistic theory of types: Predicative Part”, in *Logic Colloquium ’73* (Proceedings of the Logic Colloquium, Bristol 1973) (Studies in Logic and the Foundations of Mathematics: Volume 80), H.E. Rose and J.C. Shepherdson (eds.), Amsterdam: North-Holland, 73–118.

[^mathias-2001]: Mathias, A. R. D., 2001, “The strength of Mac Lane set theory”, *Annals of Pure and Applied Logic*, 110: 107–234.

[^myhill-1974]: Myhill, J., 1974, “The Undefinability of the Set of Natural Numbers in the Ramified Principia”, in *Bertrand Russell’s Philosophy*, G. Nakhnikian (ed.), London: Duckworth, 19–27.

[^miquel-2001]: Miquel, A., 2001, *Le Calcul des Constructions implicite: syntaxe et sémantique*, Thèse de doctorat, Université Paris 7.

[^miquel-2003]: –––, 2003, “A strongly normalising Curry-Howard correspondence for IZF set theory”, in *Computer science Logic* (Lecture Notes in Computer Science, 2803), Berlin: Springer: 441–454.

[^oppenheimer-2011]: Oppenheimer, P., and E. Zalta, 2011, “Relations Versus Functions at the Foundations of Logic: Type-Theoretic Considerations”, *Journal of Logic and Computation*, 21: 351–374.

[^palmgren-1998]: Palmgren, Erik, 1998, “On universes in type theory”, in *Twenty-five years of Constructive Type Theory* (Oxford Logic Guides: Volume 36), Oxford, New York: Oxford University Press, 191–204.

[^poincaré-1909]: Poincaré, H., 1909, “La logique de l’infini”, *Revue de métaphysique et de morale*, 17: 461–482.

[^prawitz-1967]: Prawitz, D., 1967, “Completeness and Hauptsatz for second order logic”, *Theoria*, 33: 246–258.

[^prawitz-1968]: –––, 1968, “Hauptsatz for higher order logic”, *Journal of Symbolic Logic*, 33: 452–457.

[^prawitz-1970]: –––, 1970, “On the proof theory of mathematical analysis”, in *Logic and value (Essays dedicated to Thorild Dahlquist on his fiftieth birthday)*, Filosofiska Studier (Filosof. Föreningen och Filosof. Inst.), No. 9, Uppsala: Uppsala University, 169–180.

[^quine-1940]: Quine, W., 1940, “Review of Church ‘A formulation of the simple theory of types’”, *Journal of Symbolic Logic*, 5: 114.

[^ramsey-1926]: Ramsey, F.P., 1926, “The foundations of mathematics”, *Proceedings of the London Mathematical Society*, s2–25 (1), 338–384.

[^russell-1901]: Russell, B., 1901, “Sur la logique des relations avec des applications a la théorie des séries”, *Revue de Mathématique*, 7: 115–136, 137–148.

[^russell-1903]: –––, 1903, *The Principles of Mathematics*, Cambridge: Cambridge University Press.

[^russell-1908]: –––, 1908, “Mathematical logic as based on the theory of types”, *American Journal of Mathematics*, 30: 222–262.

[^russell-1919]: –––, 1919, *Introduction to Mathematical Philosophy*, London: George Allen and Unwin.

[^russell-1959]: –––, 1959, *My philosophical development*, London, New York: Routledge.

[^russell-1910]: Russell, B., and A. Whitehead, 1910, 1912, 1913, *Principia Mathematica* (3 volumes), Cambridge: Cambridge University Press.

[^reynolds-1974]: Reynolds, J., 1974, “Towards a theory of type structure”, in *Programming Symposium* (Lecture Notes in Computer Science: Volume 19), Berlin: Springer, 408–425.

[^reynolds-1983]: –––, 1983, “Types, Abstraction and Parametric Polymorphism”, *Proceedings of the IFIP 9th World Computer Congress*, Paris, 513–523.

[^reynolds-1984]: –––, 1984, “Polymorphism is not set-theoretic. Semantics of data types”, *Lecture Notes in Computer Science* (Volume 173), Berlin: Springer, 145–156.

[^reynolds-1985]: –––, 1985, “Three approaches to type structure. Mathematical foundations of software development”, in *Lecture Notes in Computer Science* (Volume 185), Berlin: Springer, 97–138.

[^schiemer-2013]: Schiemer, G. and E.H. Reck, 2013, “Logic in the 1930s: Type Theory and Model Theory”, *The Bulletin of Symbolic Logic*, 19(4): 433–472.

[^schütte-1960]: Schütte, K., 1960, *Beweistheorie*, Berlin: Springer-Verlag.

[^schütte-1960b]: –––, 1960b, “Syntactical and Semantical Properties of Simple Type Theory”, *Journal of Symbolic Logic*, 25: 305–326.

[^setzer-1993]: Setzer, A., 1993, *Proof theoretical strength of Martin-Löf Type Theory with W-type and one universe*, Ph.D. thesis, Ludwig-Maximilians-Universität München.

[^setzer-2000]: –––, 2000, “Extending Martin-Löf type theory by one Mahlo-universe”, *Archive for Mathematical Logic*, 39: 155–181.

[^simpson-2009]: Simpson, S. G., 2009, *Subsystems of Second Order Arithmetic*, second edition, Cambridge: Cambridge University Press.

[^scott-1993]: Scott, D., 1993 “A type-theoretic alternative to ISWIM, CUCH, OWHY”, *Theoretical Computer Science*, 121: 411–440.

[^skolem-1970]: Skolem, T., 1970, *Selected works in logic*, Jens Erik Fenstad (ed.), Oslo: Universitetsforlaget.

[^strahm-1999]: Strahm, T., 1999, “First steps into metapredicativity in explicit mathematics”, in *Sets and Proofs*, S. B. Cooper and J. K. Truss (eds.), Cambridge: Cambridge University Press, 383–402.

[^tait-1966]: Tait, W. W., 1966, “A nonconstructive proof of Gentzen’s Hauptsatz for second order predicate logic”, *Bulletin of the American Mathematical Society*, 72: 980–983.

[^tait-1967]: –––, 1967, “Intensional interpretations of functionals of finite type”, *Journal of Symbolic Logic*, 32 (2): 198–212.

[^takahashi-1967]: Takahashi, M., 1967, “A proof of cut-elimination theorem in simple type theory”, *Journal of the Mathematical Society of Japan*, 19: 399–410.

[^takeuti-1955]: Takeuti, G., 1955 “On the fundamental conjecture of GLC: I”, *Journal of the Mathematical Society of Japan*, 7: 249–275.

[^takeuti-1967]: –––, 1967, “Consistency proofs of subsystems of classical analysis”, *The Annals of Mathematics* (Second Series), 86 (2): 299–348.

[^tarski-1931]: Tarski, A., 1931, “Sur les ensembles definissables de nombres reels I”, *Fundamenta Mathematicae*, 17: 210–239.

[^urquhart-2003]: Urquhart, A., 2003, “The Theory of Types”, in *The Cambridge Companion to Bertrand Russell*, Nicholas Griffin (ed.), Cambridge: Cambridge University Press.

[^voevodsky-2015]: Voevodsky, V., 2015, “An experimental library of formalized mathematics based on univalent foundations”, *Mathematical Structures in Computer Science*, 25: 1278–1294.

[^wang-1954]: Wang, H., 1954, “The formalization of mathematics”, *Journal of Symbolic Logic*, 19: 241–266.

[^wiener-1914]: Wiener, N., 1914, “A simplification of the logic of relations”, *Proceedings of the Cambridge Philosophical Society*, 17: 387–390.

[^weyl-1946]: Weyl, H., 1946, “Mathematics and Logic”, *American Mathematical Monthly*, 53: 2–13.

[^weyl-1918]: –––, 1918, *Das Kontinuum. Kritische Untersuchungen über die Grundlagen der Analysis*, Leipzig: Veit.

[^zermelo-1908]: Zermelo, E., 1908, “Untersuchungen über die Grundlagen der Mengenlehre I”, *Mathematische Annalen*, 65: 261–281.
