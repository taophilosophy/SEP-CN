# Type Theory
**First published Wed Feb 8, 2006; substantive revision Tue Sep 6, 2022**

*Coquand, Thierry*

The topic of type theory is fundamental both in logic and computer science. We limit ourselves here to sketch some aspects that are important in logic. For the importance of types in computer science, we refer the reader for instance to Reynolds 1983 and 1985.

## 1. Paradoxes and Russell’s Type Theories

The theory of types was introduced by Russell in order to cope with some contradictions he found in his account of set theory and was introduced in “Appendix B: The Doctrine of Types” of Russell 1903. This contradiction was obtained by analysing a theorem of Cantor that no mapping

$$ F:X \rightarrow \Pow(X) $$

(where $\Pow(X)$ is the class of subclasses of a class $X)$ can be surjective; that is, $F$ cannot be such that every member $b$ of $\Pow(X)$ is equal to $F(a)$ for some element $a$ of $X$. This can be phrased “intuitively” as the fact that there are more subsets of $X$ than elements of $X$. The proof of this fact is so simple and basic that it is worthwhile giving it here. Consider the following subset of $X$:

$$ A = \{ x \in X \mid x \not\in F(x)\}. $$

This subset cannot be in the range of $F$. For if $A = F(a)$, for some $a$, then

$$\begin{align} a \in F(a) &\text{ iff } a \in A \\ &\text{ iff } a \not\in F(a) \end{align}$$

which is a contradiction.

Some remarks are in order. First, the proof does not use the law of excluded middle and is thus valid intuitionistically. Second, the method that is used, called *diagonalisation* was already present in the work of du Bois-Reymond for building real functions growing faster than any function in a given sequence of functions.

Russell analysed what happens if we apply this theorem to the case where A is the class of all classes, admitting that there is such a class. He was then lead to consider the special class of classes that do not belong to themselves

$$\tag{*} R = \{ w \mid w \not\in w \}. $$

We then have

$$ R \in R \text{ iff } R \not\in R. $$

It seems indeed that Cantor was already aware of the fact that the class of all sets cannot be considered itself to be a set.

Russell communicated this problem to Frege, and his letter, together with Frege’s answer appear in van Heijenoort 1967. It is important to realise that the formulation (*) does not apply as it is to Frege’s system. As Frege himself wrote in his reply to Russell, the expression “a predicate is predicated of itself” is not exact. Frege had a distinction between *predicates* (concepts) and *objects*. A (first-order) predicate applies to an object but it cannot have a predicate as argument. The exact formulation of the paradox in Frege’s system uses the notion of the *extension* of a predicate $P$, which we designate as $\varepsilon P$. The extension of a predicate is itself an object. The important axiom V is:

$$\tag{Axiom V} \varepsilon P = \varepsilon Q \equiv \forall x [P(x) \equiv Q(x)] $$

This axiom asserts that the extension of $P$ is identical to the extension of $Q$ if and only if $P$ and $Q$ are materially equivalent. We can then translate Russell’s paradox (*) in Frege’s system by defining the predicate

$$ R(x) \text{ iff } \exists P[x = \varepsilon P \wedge \neg P(x)] $$

It can then been checked, using Axiom V in a crucial way, that

$$ R(\varepsilon R) \equiv \neg R(\varepsilon R) $$

and we have a contradiction as well. (Notice that for defining the predicate $R$, we have used an *impredicative* existential quantification on predicates. It can be shown that the *predicative* version of Frege’s system is consistent (see Heck 1996 and for further refinements Ferreira 2002)[^ferreira-2002][^heck-1996].

It is clear from this account that an idea of types was already present in Frege’s work: there we find a distinction between objects, predicates (or concepts), predicates of predicates, etc. (This point is stressed in Quine 1940.)[^quine-1940] This hierarchy is called the “extensional hierarchy” by Russell (1959), and its necessity was recognised by Russell as a consequence of his paradox.

## 2. Simple Type Theory and the $\lambda$-Calculus

As we saw above, the distinction: objects, predicates, predicate of predicates, etc., seems enough to block Russell’s paradox (and this was recognised by Chwistek and Ramsey). We first describe the type structure as it is in *Principia* and later in this section we present the elegant formulation due to Church 1940 based on $\lambda$-calculus. The types can be defined as

1. $i$ is the type of individuals
2. $(\,)$ is the type of propositions
3. if $A_1 ,\ldots ,A_n$ are types then $(A_1 ,\ldots ,A_n)$ is the type of $n$-ary relations over objects of respective types $A_1 ,\ldots ,A_n$

For instance, the type of binary relations over individuals is $(i, i)$, the type of binary connectives is $((\,),(\,))$, the type of quantifiers over individuals is $((i))$.

For forming propositions we use this type structure: thus $R(a_1 ,\ldots ,a_n)$ is a proposition if $R$ is of type $(A_1 ,\ldots ,A_n)$ and $a_i$ is of type $A_i$ for $i = 1,\ldots ,n$. This restriction makes it impossible to form a proposition of the form $P(P)$: the type of $P$ should be of the form $(A)$, and $P$ can only be applied to arguments of type $A$, and thus cannot be applied to itself since $A$ is not the same as $(A)$.

However simple type theory is not predicative: we can define an object $Q(x, y)$ of type $(i, i)$ by

$$ \forall P[P(x) \supset P(y)] $$

Assume that we have two individuals $a$ and $b$ such that $Q(a, b)$ holds. We can define $P(x)$ to be $Q(x, a)$. It is then clear that $P(a)$ holds, since it is $Q(a, a)$. Hence $P(b)$ holds as well. We have proved, in an impredicative way, that $Q(a, b)$ implies $Q(b, a)$.

Alternative simpler formulations, which retain only the notion of classes, classes of classes, etc., were formulated by Gödel and Tarski. Actually this simpler version was used by Gödel in his 1931 paper on formally undecidable propositions. The discovery of the undecidable propositions may have been motivated by a heuristic argument that it is unlikely that one can extend the completeness theorem of first-order logic to type theory (see the end of his Lecture at Königsberg 1930 in Gödel Collected Work, Volume III, Awodey and Carus 2001 and Goldfarb 2005)[^awodey-2001][^goldfarb-2005]. Tarski had a version of the definability theorem expressed in type theory (see Hodges 2008)[^hodges-2008]. See Schiemer and Reck 2013.

We have objects of type 0, for individuals, objects of type 1, for classes of individuals, objects of type 2, for classes of classes of individuals, and so on. Functions of two or more arguments, like relations, need not be included among primitive objects since one can define relations to be classes of ordered pairs, and ordered pairs to be classes of classes. For example, the ordered pair of individuals *a, b* can be defined to be $\{\{a\},\{a,b\}\}$ where $\{x,y\}$ denotes the class whose sole elements are $x$ and $y$. (Wiener 1914 had suggested a similar reduction of relations to classes.)[^wiener-1914] In this system, all propositions have the form $a(b)$, where $a$ is a sign of type $n+1$ and $b$ a sign of type $n$. Thus this system is built on the concept of an arbitrary class or subset of objects of a given domain and on the fact that the collection of *all subsets* of the given domain can form a new domain of the next type. Starting from a given domain of individuals, this process is then iterated. As emphasised for instance in Scott 1993, in set theory this process of forming subsets is iterated into the *transfinite*.

In these versions of type theory, as in set theory, functions are not primitive objects, but are represented as functional relations. The addition function for instance is represented as a ternary relation by an object of type $(i,i,i)$. An elegant formulation of the simple type theory which extends it by introducing functions as primitive objects was given by Church in 1940. It uses the $\lambda$-calculus notation (Barendregt 1997)[^barendregt-1997]. Since such a formulation is important in computer science, for the connection with category theory, and for Martin-Löf type theory, we describe it in some detail. In this formulation, predicates are seen as a special kind of functions (propositional functions), an idea that goes back to Frege (see for instance Quine 1940)[^quine-1940]. Furthermore, the notion of function is seen as more primitive than the notion of predicates and relations, and a function is not defined anymore as a special kind of relation. (Oppenheimer and Zalta 2011 presents some arguments against such a primitive representation of functions.)[^oppenheimer-2011] The types of this system are defined inductively as follows

1. there are two basic types $i$ (the type of individuals) and $o$ (the type of propositions)
2. if $A, B$ are types then $A \rightarrow B$, the type of functions from $A$ to $B$, is a type

We can form in this way the types:

| $i\rightarrow o$ | (type of predicates) |
| --- | --- |
| $(i\rightarrow o) \rightarrow o$ | (type of predicates of predicates) |

which correspond to the types $(i)$ and $((i))$ but also the new types

| $i\rightarrow i$ | (type of functions) |
| --- | --- |
| $(i\rightarrow i) \rightarrow i$ | (type of functionals) |

It is convenient to write

$$ A_1 ,\ldots ,A_n \rightarrow B $$

for

$$ A_1 \rightarrow(A_2 \rightarrow \ldots \rightarrow(A_n \rightarrow B)) $$

In this way

$$ A_1 ,\ldots ,A_n \rightarrow o $$

corresponds to the type $(A_1 ,\ldots ,A_n)$.

First-order logic considers only types of the form

| $i,\ldots ,i \rightarrow i$ | (type of function symbols), | and |
| --- | --- | --- |
| $i,\ldots ,i \rightarrow o$ | (type of predicate, relation symbols) |   |

Notice that

$$ A \rightarrow B \rightarrow C $$

stands for

$$ A \rightarrow(B\rightarrow C) $$

(association to the right).

For the terms of this logic, we shall not follow Church’s account but a slight variation of it, due to Curry (who had similar ideas before Church’s paper appeared) and which is presented in detail in R. Hindley’s book on type theory. Like Church, we use $\lambda$-calculus, which provides a general notation for functions

$$ M ::= x \mid M M \mid \lambda x.M $$

Here we have used the so-called BNF notation, very convenient in computing science. This gives a syntactic specification of the $\lambda$-terms which, when expanded, means:

- every variable is a function symbol;
- every juxtaposition of two function symbols is a function symbol;
- every $\lambda x.M$ is a function symbol;
- there are no other function symbols.

The notation for function application $M N$ is a little different than the mathematical notation, which would be $M(N)$. In general,

$$ M_1 M_2 M_3 $$

stands for

$$ (M_1 M_2) M_3 $$

(association to the left). The term $\lambda x.M$ represents the function which to $N$ associates $M[x:=N$]. This notation is so convenient that one wonders why it is not widely used in mathematics. The main equation of $\lambda$-calculus is then $(\beta$-conversion)

$$ (\lambda x.M) N = M[x:=N] $$

which expresses the meaning of $\lambda x.M$ as a function. We have used $M[x:=N$] as a notation for the value of the expression that results when $N$ is substituted for the variable $x$ in the matrix $M$. One usually sees this equation as a rewrite rule $(\beta$-reduction)

$$ (\lambda x.M) N \rightarrow M[x:=N] $$

In *untyped* lambda calculus, it may be that such rewriting does not terminate. The canonical example is given by the term $\Delta = \lambda x.x x$ and the application

$$ \Delta \Delta \rightarrow \Delta \Delta $$

(Notice the similarity with Russell’s paradox.) The idea of Curry is then to look at types as predicates over lambda terms, writing $M:A$ to express that $M$ satisfies the predicate/type $A$. The meaning of

$$ N:A\rightarrow B $$

is then

$$ \forall M, \text{ if } M:A \text{ then } N M:B $$

which justifies the following rules

$$ \frac{N:A\rightarrow B M:A}{N M:B} $$ $$ \frac{M:B [x:A]}{\lambda x.M:A \rightarrow B} $$

In general one works with judgements of the form

$$ x_1 :A_1,...,x_n :A_n \vdash M:A $$

where $x_1,..., x_n$ are distinct variables, and $M$ is a term having all free variables among $x_1,..., x_n$. In order to be able to get Church’s system, one adds some constants in order to form propositions. Typically

| not: | $o\rightarrow o$ |
| --- | --- |
| imply: | $o\rightarrow o\rightarrow o$ |
| and: | $o\rightarrow o\rightarrow o$ |
| forall: | $(A\rightarrow o) \rightarrow o$ |

The term

$$ \lambda x. \neg(x x) $$

represents the predicate of predicates that do not apply to themselves. This term does not have a type however, that is, it is not possible to find $A$ such that

$$ \lambda x. \neg(x x) : (A\rightarrow o) \rightarrow o $$

which is the formal expression of the fact that Russell’s paradox cannot be expressed. Leibniz equality

$$ Q: i \rightarrow i \rightarrow o $$

will be defined as

$$ Q = \lambda x . \lambda y. \forall(\lambda P.\imply(P x) (P y)) $$

One usually writes $\forall x[M$] instead of $\forall(\lambda x.M)$, and the definition of $Q$ can then be rewritten as

$$ Q = \lambda x.\lambda y.\forall P[\imply (P x) (P y)] $$

This example again illustrates that we can formulate impredicative definitions in simple type theory.

The use of $\lambda$-terms and $\beta$-reduction is most convenient for representing the complex substitution rules that are needed in simple type theory. For instance, if we want to substitute the predicate $\lambda x.Q a x$ for $P$ in the proposition

$$ \imply (P a) (P b) $$

we get

$$ \imply ((\lambda x.Q a x) a) ((\lambda x.Q a x) b) $$

and, using $\beta$-reduction,

$$ \imply (Q a a) (Q a b) $$

In summary, simple type theory forbids self-application but not the circularity present in impredicative definitions.

The $\lambda$-calculus formalism also allows for a clearer analysis of Russell’s paradox. We can see it as the definition of the predicate

$$ R x = \neg(x x) $$

If we think of $\beta$-reduction as the process of unfolding a definition, we see that there is a problem already with understanding the definition of R R

$$ R R \rightarrow \neg(R R) \rightarrow \neg(\neg(R R)) \rightarrow \ldots $$

In some sense, we have a non-wellfounded definition, which is as problematic as a contradiction (a proposition equivalent to its negation). One important theorem, the normalisation theorem, says that this cannot happen with simple types: if we have $M:A$ then $M$ is normalisable in a strong way (any sequence of reductions starting from $M$ terminates).

For more information on this topic, we refer to the entry on Church’s simple type theory.

## 3. Ramified Hierarchy and Impredicative Principles

Russell introduced another hierarchy, that was not motivated by any formal paradoxes expressed in a formal system, but rather by the fear of “circularity” and by informal paradoxes similar to the paradox of the liar. If a man says “I am lying”, then we have a situation reminiscent of Russell’s paradox: a proposition which is equivalent to its own negation. Another informal such paradoxical situation is obtained if we define an integer to be the “least integer not definable in less than 100 words”. In order to avoid such informal paradoxes, Russell thought it necessary to introduce another kind of hierarchy, the so-called “ramified hierarchy”. The need for such a hierarchy is hinted in Appendix B of Russell 1903. Interestingly this is connected there to the question of the identity of equivalent propositions and of the logical product of a class of propositions. A thorough discussion can be found in Chapter 10 of Russell 1959. Since this notion of ramified hierarchy has been extremely influential in logic and especially proof theory, we describe it in some details.

In order to further motivate this hierarchy, here is one example due to Russell. If we say

Napoleon was Corsican.

we do not refer in this sentence to any assemblage of properties. The property “to be Corsican” is said to be *predicative*. If we say on the other hand

Napoleon had all the qualities of a great general

we are referring to a totality of qualities. The property “to have all qualities of a great general” is said to be *impredicative*.

Another example, also coming from Russell, shows how impredicative properties can potentially lead to problems reminiscent of the liar paradox. Suppose that we suggest the definition

A typical Englishman is one who possesses all the properties possessed by a majority of Englishmen.

It is clear that most Englishmen do not possess *all* the properties that most Englishmen possess. Therefore, a typical Englishman, according to this definition, should be untypical. The problem, according to Russell, is that the word “typical” has been defined by a reference to all properties and has been treated as itself a property. (It is remarkable that similar problems arise when defining the notion of *random* numbers, cf. Martin-Löf “Notes on constructive mathematics” (1970).) Russell introduced the *ramified hierarchy* in order to deal with the apparent circularity of such impredicative definitions. One should make a distinction between the *first-order* properties, like being Corsican, that do not refer to the totality of properties, and consider that the *second-order* properties refer only to the totality of *first-order properties*. One can then introduce third-order properties, that can refer to the totality of second-order property, and so on. This clearly eliminates all circularities connected to impredicative definitions.

At about the same time, Poincaré carried out a similar analysis. He stressed the importance of “predicative” classifications, and of not defining elements of a class using a quantification over this class (Poincaré 1909)[^poincaré-1909]. Poincaré used the following example. Assume that we have a collection with elements 0, 1 and an operation + satisfying

$$\begin{align} x+0 &= 0 \\ x+(y+1) &= (x+y)+1 \end{align}$$

Let us say that a property is *inductive* if it holds of 0 and holds for $x+1$ if it holds for $x$.

An impredicative, and potentially “dangerous”, definition would be to define an element to be a *number* if it satisfies *all* inductive properties. It is then easy to show that this property “to be a number” is itself inductive. Indeed, 0 is a number since it satisfies all inductive properties, and if $x$ satisfies all inductive properties then so does $x+1$. Similarly it is easy to show that $x+y$ is a number if $x,y$ are numbers. Indeed the property $Q(z)$ that $x+z$ is a number is inductive: $Q$(0) holds since $x+0=x$ and if $x+z$ is a number then so is $x+(z+1) = (x+z)+1$. This whole argument however is circular since the property “to be a number” is not predicative and should be treated with suspicion.

Instead, one should introduce a ramified hierarchy of properties and numbers. At the beginning, one has only *first-order* inductive properties, which do not refer in their definitions to a totality of properties, and one defines the numbers of order 1 to be the elements satisfying all first-order inductive properties. One can next consider the second-order inductive properties, that can refer to the collection of first-order properties, and the numbers of order 2, that are the elements satisfying the inductive properties of order 2. One can then similarly consider numbers of order 3, and so on. Poincaré emphasizes the fact that a number of order 2 is *a fortiori* a number of order 1, and more generally, a number of order $n+1$ is *a fortiori* a number of order $n$. We have thus a sequence of more and more restricted properties: inductive properties of order 1, 2, … and a sequence of more and more restricted collections of objects: numbers of order 1, 2, … Also, the property “to be a number of order $n$” is itself an inductive property of order $n+1$.

It does not seem possible to prove that $x+y$ is a number of order $n$ if $x,y$ are numbers of order $n$. On the other hand, it is possible to show that if $x$ is a number of order $n+1$, and $y$ a number of order $n+1$ then $x+y$ is a number of order $n$. Indeed, the property $P(z)$ that “$x+z$ is a number of order $n$” is an inductive property of order $n+1: P$(0) holds since $x+0 = x$ is a number of order $n+1$, and hence of order $n$, and if $P(z)$ holds, that is if $x+z$ is a number of order $n$, then so is $x+(z+1) = (x+z)+1$, and so $P(z+1)$ holds. Since $y$ is a number of order $n+1$, and $P(z)$ is an inductive property of order $n+1, P(y)$ holds and so $x+y$ is a number of order $n$. This example illustrates well the complexities introduced by the ramified hierarchy.

The complexities are further amplified if one, like Russell as for Frege, defines even basic objects like natural numbers as classes of classes. For instance the number 2 is defined as the class of all classes of individuals having exactly two elements. We again obtain natural numbers of different orders in the ramified hierarchy. Besides Russell himself, and despite all these complications, Chwistek tried to develop arithmetic in a ramified way, and the interest of such an analysis was stressed by Skolem. See Burgess and Hazen 1998 for a recent development.

Another mathematical example, often given, of an impredicative definition is the definition of least upper bound of a bounded class of real numbers. If we identify a real with the set of rationals that are less than this real, we see that this least upper bound can be defined as the union of all elements in this class. Let us identify subsets of the rationals as predicates. For example, for rational numbers $q, P(q)$ holds iff $q$ is a member of the subset identified as $P$. Now, we define the predicate $L_C$ (a subset of the rationals) to be the least upper bound of class $C$ as:

$$ \forall q[L_C (q) \leftrightarrow \exists P[C(P) \wedge P(q)]] $$

which is impredicative: we have defined a predicate $L$ by an existential quantification over all predicates. In the ramified hierarchy, if $C$ is a class of first-order classes of rationals, then $L$ will be a second-order class of rationals. One obtains then not *one* notion or real numbers, but real numbers of different orders 1, 2, … The least upper bound of a collection of reals of order 1 will then be at least of order 2 in general.

As we saw earlier, yet another example of an impredicative definition is given by Leibniz’ definition of equality. For Leibniz, the predicate “is equal to $a$” is true for $b$ iff $b$ satisfies all the predicates satisfied by $a$.

How should one deal with the complications introduced by the ramified hierarchy? Russell showed, in the introduction to the second edition to *Principia Mathematica*, that these complications can be avoided in some cases. He even thought, in Appendix B of the second edition of *Principia Mathematica*, that the ramified hierarchy of natural numbers of order 1,2,… collapses at order 5 for defining the reflexive transitive closure of a relation. However, Gödel later found a problem in his argument, and indeed, it was shown by Myhill 1974 that this hierarchy actually *does not* collapse at any finite level. A similar problem, discussed by Russell in the introduction to the second edition to *Principia Mathematica* arises in the proof of Cantor’s theorem that there cannot be any injective functions from the collection of all predicates to the collection of all objects (the version of Russell’s paradox in Frege’s system that we presented in the introduction). Can this be done in a ramified hierarchy? Russell doubted that this could be done within a ramified hierarchy of predicates and this was indeed confirmed indeed later (see Chwistek 1926, Fitch 1939 and Heck 1996)[^chwistek-1926][^heck-1996].

Because of these problems, Russell and Whitehead introduced in the first edition of *Principia Mathematica* the following *reducibility axiom*: the hierarchy of predicates, first-order, second-order, etc., collapses at level 1. This means that for any predicate of any order, there is a predicate of the first-order level which is equivalent to it. In the case of equality for instance, we postulate a first-order relation “$a=b$” which is equivalent to “$a$ satisfies all properties that $b$ satisfies”. The motivation for this axiom was purely pragmatic. Without it, all basic mathematical notions, like real or natural numbers are stratified into different orders. Also, despite the apparent circularity of impredicative definitions, the axiom of reducibility does not seem to lead to inconsistencies.

As noticed however first by Chwistek, and later by Ramsey, in the presence of the axiom of reducibility, there is actually no point in introducing the ramified hierarchy at all! It is much simpler to accept impredicative definitions from the start. The simple “extensional” hierarchy of individuals, classes, classes of classes, … is then enough. We get in this way the simpler systems formalised in Gödel 1931 or Church 1940 that were presented above.

The axiom of reducibility draws attention to the problematic status of impredicative definitions. To quote Weyl 1946, the axiom of reducibility “is a bold, an almost fantastic axiom; there is little justification for it in the real world in which we live, and none at all in the evidence on which our mind bases its constructions”! So far, no contradictions have been found using the reducibility axiom. However, as we shall see below, proof-theoretic investigations confirm the extreme strength of such a principle.

The idea of the ramified hierarchy has been extremely important in mathematical logic. Russell considered only the finite iteration of the hierarchy: first-order, second-order, etc., but from the beginning, the possibility of extending the ramification transfinitely was considered. Poincaré (1909) mentions the work of Koenig in this direction. For the example above of numbers of different order, he also defines a number to be inductive of order $\omega$ if it is inductive of all finite orders. He then points out that *x+y* is inductive of order $\omega$ if both $x$ and $y$ are. This shows that the introduction of transfinite orders can in some case play the role of the axiom of reducibility. Such transfinite extension of the ramified hierarchy was analysed further by Gödel who noticed the key fact that the following form of the reducibility axiom is actually *provable*: when one extends the ramified hierarchy of properties over the natural numbers into the transfinite this hierarchy collapses at level $\omega_1$, the least uncountable ordinal (Gödel 1995, and Prawitz 1970)[^gödel-1995][^prawitz-1970]. Furthermore, while at all levels $\lt \omega_1$, the collection of predicates is countable, the collection of predicates at level $\omega_1$ is of cardinality $\omega_1$. This fact was a strong motivation behind Gödel’s model of constructible sets. In this model the collection of all subsets of the set of natural numbers (represented by predicates) is of cardinality $\omega_1$ and is similar to the ramified hierarchy. This model satisfies in this way the Continuum Hypothesis, and gives a relative consistency proof of this axiom. (The motivation of Gödel was originally only to build a model where the collection of all subsets of natural numbers is well-ordered.)

The ramified hierarchy has been also the source of much work in proof theory. After the discovery by Gentzen that the consistency of Arithmetic could be proved by transfinite induction (over decidable predicates) along the ordinal $\varepsilon_0$, the natural question was to find the corresponding ordinal for the different levels of the ramified hierarchy. Schütte (1960) found that for the first level of the ramified hierarchy, that is if we extend arithmetic by quantifying only over first-order properties, we get a system of ordinal strength $\varepsilon_{\varepsilon_0}$. For the second level we get the ordinal strength $\varepsilon_{\varepsilon_{ \varepsilon_0}}$, etc. We recall that $\varepsilon_{\alpha}$ denotes the $\alpha$-th $\varepsilon$-ordinal number, an $\varepsilon$-ordinal number being an ordinal $\beta$ such that $\omega^{\beta} = \beta$, see Schütte (1960).

Gödel stressed the fact that his approach to the problem of the continuum hypothesis was not constructive, since it needs the uncountable ordinal $\omega_1$, and it was natural to study the ramified hierarchy along constructive ordinals. After preliminary works of Lorenzen and Wang, Schütte analysed what happens if we proceed in the following more constructive way. Since arithmetic has for ordinal strength $\varepsilon_0$ we consider first the iteration of the ramified hierarchy up to $\varepsilon_0$. Schütte computed the ordinal strength of the resulting system and found an ordinal strength $u(1)\gt \varepsilon_0$. We iterate then ramified hierarchy up to this ordinal $u(1)$ and get a system of ordinal strength $u(2)\gt u(1)$, etc. Each $u(k)$ can be computed in terms of the so-called Veblen hierarchy: $u(k+1)$ is $\phi_{u(k)}(0)$. The limit of this process gives an ordinal called $\Gamma_0$: if we iterate the ramified hierarchy up to the ordinal $\Gamma_0$ we get a system of ordinal strength $\Gamma_0$. Such an ordinal was obtained independently about the same time by S. Feferman. It has been claimed that $\Gamma_0$ plays for predicative systems a role similar to $\varepsilon_0$ for Arithmetic. Recent proof-theoretical works however are concerned with systems having bigger proof-theoretical ordinals that can be considered predicative (see for instance Palmgren 1995).

Besides these proof theoretic investigations related to the ramified hierarchy, much work has been devoted in proof theory to analysing the consistency of the axiom of reducibility, or, equivalently, the consistency of impredicative definitions. Following Gentzen’s analysis of the cut-elimination property in the sequent calculus, Takeuti found an elegant sequent formulation of simple type theory (without ramification) and made the bold conjecture that cut-elimination should hold for this system. This conjecture seemed at first extremely dubious given the circularity of impredicative quantification, which is well reflected in this formalism. The rule for quantifications is indeed

$$ \frac{\Gamma \vdash \forall X[A(X)]}{\Gamma \vdash A[X:=T]} $$

where $T$ is *any* term predicate, which may itself involve a quantification over all predicates. Thus the formula $A[X:=T]$ may be itself much more complex than the formula $A(X)$.

One early result is that cut-elimination for Takeuti’s impredicative system implies in a finitary way the consistency of second-order Arithmetic. (One shows that this implies the consistency of a suitable form of infinity axiom, see Andrews 2002.)[^andrews-2002] Following work by Schütte (1960b), it was later shown by W. Tait and D. Prawitz that indeed the cut-elimination property holds (the proof of this has to use a stronger proof theoretic principle, as it should be according to the incompleteness theorem.)

What is important here is that these studies have revealed the extreme power of impredicative quantification or, equivalently, the extreme power of the axiom of reducibility. This confirms in some way the intuitions of Poincaré and Russell. The proof-theoretic strength of second-order Arithmetic is way above all ramified extensions of Arithmetic considered by Schütte. On the other hand, despite the circularity of impredicative definitions, which is made so explicit in Takeuti’s calculus, no paradoxes have been found yet in second-order Arithmetic.

Another research direction in proof theory has been to understand how much of impredicative quantification can be explained from principles that are available in intuitionistic mathematics. The strongest such principles are strong forms of inductive definitions. With such principles, one can explain a limited form of an impredicative quantification, called $\Pi_{1}^1$-comprehension, where one uses only one level of impredicative quantification over predicates. Interestingly, almost all known uses of impredicative quantifications: Leibniz equality, least upper bound, etc., can be done with $\Pi_{1}^1$-comprehension. This reduction of $\Pi_{1}^1$-comprehension was first achieved by Takeuti in a quite indirect way, and was later simplified by Buchholz and Schütte using the so-called $\Omega$-rule. It can be seen as a constructive explanation of some restricted, but nontrivial, uses of impredicative definitions.

## 4. Type Theory/Set Theory

Type theory can be used as a foundation for mathematics, and indeed, it was presented as such by Russell in his 1908 paper, which appeared the same year as Zermelo’s paper, presenting set theory as a foundation for mathematics.

It is clear intuitively how we can explain type theory in set theory: a type is simply interpreted as a set, and function types $A \rightarrow B$ can be explained using the set theoretic notion of function (as a functional relation, i.e. a set of pairs of elements). The type $A \rightarrow o$ corresponds to the powerset operation.

The other direction is more interesting. How can we explain the notion of sets in terms of types? There is an elegant solution, due to A. Miquel, which complements previous works by P. Aczel (1978) and which has also the advantage of explaining non necessarily well-founded sets a la Finsler. One simply interprets a *set* as a *pointed graph* (where the arrow in the graph represents the membership relation). This is very conveniently represented in type theory, a pointed graph being simply given by a type A and a pair of elements

$$ a:A, R:A \rightarrow A \rightarrow o $$

We can then define in type theory when two such sets $A, a, R$ and $B, b, S$ are equal: this is the case iff there is a bisimulation $T$ between $A$ and $B$ such that $Tab$ holds. A bisimulation is a relation

$$ T:A\rightarrow B\rightarrow o $$

such that whenever $Txy$ and $Rxu$ hold, there exists $v$ such that $Tuv$ and $Syv$ hold, and whenever $Txy$ and $Ryv$ hold, there exists $u$ such that $Tuv$ and $Rxu$ hold. We can then define the membership relation: the set represented $B, b, S$ is a member of the set represented by $A, a, R$ iff there exists $a_1$ such that $Ra_1a$ and $A, a_1, R$ and $B, b, S$ are bisimilar.

It can then be checked that all the usual axioms of set theory extensionality, power set, union, comprehension over bounded formulae (and even antifoundation, so that the membership relation does not need to be well-founded) hold in this simple model. (A bounded formula is a formula where all quantifications are of the form $\forall x \in a\ldots$ or $\exists x \in a\ldots$). In this way it can been shown that Church’s simple type theory is equiconsistent with the bounded version of Zermelo’s set theory.

## 5. Type Theory/Category Theory

There are deep connections between type theory and category theory. We limit ourselves to presenting two applications of type theory to category theory: the constructions of the free cartesian closed category and of the free topos (see the entry on category theory for an explanation of “cartesian closed” and “topos”).

For building the free cartesian closed category, we extend simple type theory with the type 1 (unit type) and the product type $A \times B$, for $A, B$ types. The terms are extended by adding pairing operations and projections and a special element of type 1. As in Lambek and Scott 1986, one can then define a notion of *typed conversions* between terms, and show that this relation is decidable. One can then show (Lambek and Scott 1986)[^lambek-1986] that the category with types as objects and as morphisms from $A$ to $B$ the set of closed terms of type $A \rightarrow B$ (with conversion as equality) is the free cartesian closed category. This can be used to show that equality between arrows in this category is decidable.

The theory of types of Church can also be used to build the free topos. For this we take as objects pairs $A,E$ with $A$ type and $E$ a partial equivalence relation, that is a closed term $E:A \rightarrow A \rightarrow o$ which is symmetric and transitive. We take as morphisms between $A, E$ and $B, F$ the relations $R:A\rightarrow B\rightarrow o$ that are *functional* that is such that for any $a:A$ satisfying $E a a$ there exists one, and only one (modulo $F)$ element $b$ of $B$ such that $F b b$ and $R a b$. For the subobject classifier we take the pair $o, E$ with $E:o\rightarrow o\rightarrow o$ defined as

$$ E M N = \text{ and } (\imply\, M N) (\imply\,N M) $$

One can then show that this category forms a topos, indeed the free topos.

It should be noted that the type theory in Lambek and Scott 1986 uses a variation of type theory, introduced by Henkin and refined by P. Andrews (2002) which is to have an extensional equality as the only logical connective, i.e. a polymorphic constant

$$ \text{eq} : A \rightarrow A \rightarrow o $$

and to define all logical connectives from this connective and constants $T, F : o$. For instance, one defines

$$ \forall P =_{df} \text{eq} (\lambda x.T) P $$

The equality at type $o$ is logical equivalence.

One advantage of the intensional formulation is that it allows for a direct notation of proofs based on $\lambda$-calculus (Martin-Löf 1971 and Coquand 1986)[^coquand-1986][^martin-löf-1971].

## 6. Extensions of Type System, Polymorphism, Paradoxes

We have seen the analogy between the operation A $\rightarrow$ A $\rightarrow$ o on types and the powerset operation on sets. In set theory, the powerset operation can be iterated transfinitely along the cumulative hierarchy. It is then natural to look for analogous transfinite versions of type theory.

One such extension of Church’s simple type theory is obtained by adding universes (Martin-Löf 1970)[^martin-löf-1970]. Adding a universe is a *reflection* process: we add a type $U$ whose objects are the types considered so far. For Church’s simple type theory we will have

$$ o:U, i:U \text{ and } A\rightarrow B:U \text{ if } A:U, B:U $$

and, furthermore, $A$ is a type if $A:U$. We can then consider types such as

$$ (A:U) \rightarrow A \rightarrow A $$

and functions such as

$$ \text{id} = \lambda A.\lambda x.x : (A:U) \rightarrow A \rightarrow A $$

The function id takes as argument a “small” type $A:U$ and an element $x$ of type $A$, and outputs an element of type $A$. More generally if $T(A)$ is a type under the assumption $A:U$, one can form the dependent type

$$ (A:U) \rightarrow T(A) $$

That $M$ is of this type means that $M A:T(A)$ whenever $A:U$. We get in this way extensions of type theory whose strength is similar to the one of Zermelo’s set theory (Miquel 2001)[^miquel-2001]. More powerful form of universes are considered in (Palmgren 1998)[^palmgren-1998]. Miquel (2003) presents a version of type theory of strength equivalent to the one of Zermelo-Fraenkel.

One very strong form of universe is obtained by adding the axiom $U:U$. This was suggested by P. Martin-Löf in 1970. J.Y. Girard showed that the resulting type theory is inconsistent as a logical system (Girard 1972)[^girard-1972]. Though it seems at first that one could directly reproduce Russell’s paradox using a set of all sets, such a direct paradox is actually not possible due to the difference between sets and types. Indeed the derivation of a contradiction in such a system is subtle and has been rather indirect (though, as noticed in Miquel 2001, it can now be reduced to Russell’s paradox by representing sets as pointed graphs)[^miquel-2001]. J.Y. Girard first obtained his paradox for a weaker system. This paradox was refined later (Coquand 1994 and Hurkens 1995)[^coquand-1994][^hurkens-1995]. (The notion of pure type system, introduced in Barendregt 1992, is convenient for getting a sharp formulation of these paradoxes.)[^barendregt-1992] Instead of the axiom $U:U$ one assumes only

$$ (A:U) \rightarrow T(A) : U $$

if $T(A) : U [A:U]$. Notice the circularity, indeed of the same kind as the one that is rejected by the ramified hierarchy: we define an element of type $U$ by quantifying over all elements of $U$. For instance the type

$$ (A:U) \rightarrow A \rightarrow A:U $$

will be the type of the polymorphic identity function. Despite this circularity, J.Y. Girard was able to show normalisation for type systems with this form of polymorphism. However, the extension of Church’s simple type theory with polymorphism is inconsistent as a logical system, i.e. all propositions (terms of type o) are provable.

J.Y. Girard’s motivation for considering a type system with polymorphism was to extend Gödel’s Dialectica (Gödel 1958)[^gödel-1958] interpretation to second-order arithmetic. He proved normalisation using the reducibility method, that had been introduced by Tait (1967) while analysing Gödel 1958. It is quite remarkable that the circularity inherent in impredicativity does not result in non-normalisable terms. (Girard’s argument was then used to show that cut-elimination terminates in Takeuti’s sequent calculus presented above.) A similar system was introduced independently by J. Reynolds (1974) while analysing the notion of polymorphism in computer science.

Martin-Löf’s introduction of a type of all types comes from the identification of the concept of propositions and types, suggested by the work of Curry and Howard. It is worth recalling here his three motivating points:

1. Russell’s definition of types as ranges of significance of propositional functions
2. the fact that one needs to quantify over all propositions (impredicativity of simple type theory)
3. identification of proposition and types

Given (1) and (2) we should have a type of propositions (as in simple type theory), and given (3) this should also be the type of all types. Girard’s paradox shows that one cannot have (1),(2) and (3) simultaneously. Martin-Löf’s choice was to take away (2), restricting type theory to be predicative (and, indeed, the notion of universe appeared first in type theory as a predicative version of the type of all types). The alternative choice of taking away (3) is discussed in Coquand 1986.

## 7. Univalent Foundations

The connections between type theory, set theory and category theory gets a new light through the work on Univalent Foundations (Voevodsky 2015)[^voevodsky-2015] and the *Axiom of Univalence*. This involves in an essential way the extension of type theory described in the previous section, in particular dependent types, the view of propositions as types, and the notion of universe of types. These development are also relevant for discussing the notion of structure, the importance of which was for instance emphasized in Russell 1959.

Martin-Löf 1975 [1973] introduced a new basic type $\mathbf{Id}_A (a,b)$, if $a$ and $b$ are in the type $A$, which can be thought as the type of equality proofs of the element $a$ and $b$. An important feature of this new type is that it can be iterated, so that we can consider the type $\mathbf{Id}_{\mathbf{Id}_A (a,b)}(p,q)$ if $p$ and $q$ are of type $\mathbf{Id}_A (a,b)$. If we think of a type as a special kind of set, it is natural to conjecture that such a type of equality proofs is always inhabited for any two equality proofs $p$ and $q$. Indeed, intuitively, there seems to be at most an equality proof between two elements $a$ and $b$. Surprisingly, Hofmann and Streicher 1996 designed a model of dependent type theory where this is not valid, that is a model where they can be different proofs that two elements are equal. In this model, a type is interpreted by a *groupoid* and the type $\mathbf{Id}_A (a,b)$ by the set of isomorphisms between $a$ and $b$, set which may have more than one element. The existence of this model has the consequence that it cannot be proved in general in type theory that an equality type has at most one element. This groupoid interpretation has been generalized in the following way, which gives an intuitive interpretation of the identity type. A *type* is interpreted by a *topological space*, up to homotopy, and a type $\mathbf{Id}_A (a,b)$ is interpreted by the type of *paths* connecting $a$ and $b$. (See Awodey et al. 2013 and [HoTT 2013, Other Internet Resources].)[^awodey-2013]

Voevodsky 2015 introduced the following stratification of types. (This stratification was motivated in part by this interpretation of a type as a topological space, but can be understood directly without reference to this interpretation.) We say that a type $A$ is a *proposition* if we have $\mathbf{Id}_A (a,b)$ for any element $a$ and $b$ of $A$ (this means that the type $A$ has at most one element). We say that a type $A$ is a *set* if the type $\mathbf{Id}_A (a,b)$ is a proposition for any element $a$ and $b$ of $A$. We say that a type $A$ is a *groupoid* if the type $\mathbf{Id}_A (a,b)$ is a set for any element $a$ and $b$ of $A$. The justification of this terminology is that it can be shown, only using the rules of type theory, that any such type can indeed be seen as a groupoid in the usual categorical sense, where the objects are the elements of this type, the set of morphisms between $a$ and $b$ being represented by the *set* $\mathbf{Id}_A (a,b)$. The composition is the proof of transitivity of equality, and the identity morphism is the proof of reflexivity of equality. The fact that each morphism has an inverse corresponds to the fact that identity is a symmetric relation. This stratification can then be extended and we can define when a type is a 2-groupoid, 3-groupoid and so on. In this view, *type theory* appears as a vast generalization of *set theory*, since a set is a particular kind of type.

Voevodsky 2015 introduces also a notion of *equivalence* between types, notion which generalizes in an uniform way the notions of *logical equivalence* between propositions, *bijection* between sets, *categorical equivalence* between groupoids, and so on. We say that a map $f:A\rightarrow B$ is an equivalence if, for any element $b$ in $B$ the type of pairs $a,p$ where $p$ is of type $\mathbf{Id}_B (f a,b)$, is a proposition and is inhabited. This expresses in a strong way that an element in $B$ is the image of exactly one element in $A$, and if $A$ and $B$ are sets, we recover the usual notion of bijection between sets. (In general if $f:A\rightarrow B$ is an equivalence, then we have a map $B\rightarrow A$, which can be thought of as the inverse of $f$.) It can be shown for instance that the identity map is always an equivalence. Let $\text{Equiv}(A,B)$ be the type of pairs $f,p$ where $f:A\rightarrow B$ and $p$ is a proof that $f$ is an equivalence. Using the fact that the identity map is an equivalence we have an element of $\text{Equiv}(A,A)$ for any type $A$. This implies that we have a map

$$ \mathbf{Id}_U (A,B)\rightarrow \text{Equiv}(A,B) $$

and the *Axiom of Univalence* states that this map is an equivalence. In particular, we have the implication

$$ \text{Equiv}(A,B)\rightarrow \mathbf{Id}_U (A,B) $$

and so if there is an equivalence between two small types then these types are equal.

This Axiom can be seen as a strong form of the extensionality principle. It indeed generalizes the Axiom of *propositional extensionality* mentioned by Church 1940, which states that two logically equivalent propositions are equal. Surprisingly, it also implies the Axiom of *function extensionality*, Axiom 10 in Church 1940, which states that two pointwise equal functions are equal (Voevodsky 2015)[^voevodsky-2015]. It also directly implies that two isomorphic sets are equal, that two categorically equivalent groupoids are equal, and so one.

This can be used to give a formulation of the notion of *transport of structures* (Bourbaki 1957) along equivalences. For instance, let $M A$ be the type of monoid structures on the set $A$: this is the type of tuples $m, e, p$ where $m$ is a binary operation on $A$ and $e$ an element of $A$ and $p$ a proof that these elements satisfy the usual monoid laws. The rule of substitution of equal by equal takes the form

$$ \mathbf{Id}_U (A,B)\rightarrow M A\rightarrow M B $$

If there is a bijection between $A$ and $B$ they are equal by the Axiom of Univalence, and we can use this implication to transport any monoid structure of $A$ in a monoid structure of $B$.

Both Russell 1919 and Russell 1959 stress the importance of the notion of structure. For instance, in Chapter VI of Russell 1919, it is noticed that two similar relations essentially have the same properties, and hence have the same “structure”. (The notion of “similarity” of relations was introduced in Russell 1901.)[^russell-1901] We can also use this framework to refine Russell’s discussions on the notion of structure. For instance, let **Monoid** be the type of pairs $A,p$ where $p$ is an element of $M A$. Two such pairs $A,p$ and $B,q$ are isomorphic if there exists a bijection $f$ from $A$ to $B$ such that $q$ is equal to the transport of structure of $p$ along $f$. A consequence of the Axiom of Univalence is that two isomorphic elements of the type **Monoid** are equal, and hence shares the same properties. Notice that such a general transport of properties is *not* possible when structures are formulated in a set theoretic framework. Indeed, in a set theoretic framework, it is possible to formulate properties using the membership relations, for instance the property that the carrier set of the structure contains the natural number $0$, property that is not preserved in general by isomorphisms. Intuitively, the set theoretical description of a structure is not abstract enough since we can talk about the way this structure is built up. This difference between set theory and type theory is yet another illustration of the characterization by J.Reynolds 1983 of a type structure as a “syntactical discipline for enforcing level of abstraction”.

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=type-theory). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/type-theory/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=type-theory&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](http://philpapers.org/sep/type-theory/) at [PhilPapers](http://philpapers.org/), with links to its database. |

## Other Internet Resources

- Kubota, K., 2018, “[Foundations of Mathematics. Genealogy and Overview](http://www.owlofminerva.net/files/fom.pdf),” manuscript, draft of March 27, 2018.
- [HoTT 2013], [*Homotopy Type Theory: Univalent Foundations of Mathematics*](http://homotopytypetheory.org/book/), Institute for Advanced Study.

## Related Entries

Russell, Bertrand | category theory | Frege, Gottlob | Frege, Gottlob: theorem and foundations for arithmetic | logic: paraconsistent | mathematics: inconsistent | peano | *Principia Mathematica* | type theory: Church’s type theory | type theory: intuitionistic

[^aczel-1978]: Aczel, P., 1978, “The type theoretic interpretation of constructive set theory”, *Logic Colloquium ’77*, Amsterdam: North-Holland, 55–66.

[^andrews-2002]: Andrews, P., 2002, *An introduction to mathematical logic and type theory: to truth through proof* (Applied Logic Series: Volume 27), Dordrecht: Kluwer Academic Publishers, second edition.

[^awodey-2001]: Awodey, S. and Carus, A.W., 2001, “Carnap, completeness and categoricity: the Gabelbarkeitssatz of 1928”, *Erkenntnis*, 54: 145–171.

[^awodey-2013]: ––– and Pelayo, A., Warren, M. 2013, “The Axiom of Univalence in Homotopy Type Theory”, *Notices of the American Mathematical Society*, 60(9): 1157–1164.

[^barendregt-1997]: Barendregt, H., 1997, “The impact of the lambda calculus in logic and computer science”, *Bulletin of Symbolic Logic*, 3(2): 181–215.

[^barendregt-1992]: –––, 1992, *Lambda calculi with types. Handbook of logic in computer science*, Volume 2, Oxford, New York: Oxford University Press, 117–309.

[^bell-2012]: Bell, J.L., 2012, “Types, Sets and Categories”, in Akihiro Kanamory *Handbook of the History of Logic. Volume 6: Sets and Extensions in the Twentieth Century*, Amsterdam: North Holland.

[^bourbaki-1958]: Bourbaki, N., 1958, *Théorie des Ensembles*, 3rd edition, Paris: Hermann.

[^bruijn-1980]: de Bruijn, N. G., 1980, “A survey of the project AUTOMATH”, in *To H. B. Curry: essays on combinatory logic, lambda calculus and formalism*, London-New York: Academic Press, 579–606.

[^burgess-1998]: Burgess J. P. and Hazen A. P., 1998, “Predicative Logic and Formal Arithmetic Source,” *Notre Dame J. Formal Logic*, 39(1): 1–17.

[^buchholz-1988]: Buchholz, W. and K. Schütte, 1988, *Proof theory of impredicative subsystems of analysis* (Studies in Proof Theory: Monograph 2), Naples: Bibliopolis.

[^church-1940]: Church, A., 1940, “A formulation of the simple theory of types,” *Journal of Symbolic Logic*, 5: 56–68

[^church-1984]: –––, 1984, “Russell’s theory of identity of propositions,” *Philosophia Naturalis*, 21: 513–522

[^chwistek-1926]: Chwistek, L., 1926, “Ueber die Hypothesen der Mengelehre,” *Mathematische Zeitschrift*, 25: 439–473

[^chwistek-1948]: –––, 1948, *The Limits of Science: Outline of Logic and of the Methodology of the Exact Sciences*, London: Routledge and Kegan Paul.

[^coquand-1986]: Coquand, T., 1986, “An analysis of Girard’s paradox,” *Proceedings of the IEEE Symposium on Logic in Computer Science*, 227–236.

[^coquand-1994]: –––, 1994, “A new paradox in type theory,” *Stud. Logic Found. Math.* (Volume 134), Amsterdam: North-Holland, 555–570.

[^bois-reymond-1875]: du Bois-Reymond, P., 1875, “Ueber asymptotische Werthe, infintaere Appproximationen und infitaere Aufloesung von Gleichungen,” *Mathematische Annalen*, 8: 363–414.

[^feferman-1964]: Feferman, S., 1964, “Systems of predicative analysis,” *Journal of Symbolic Logic*, 29: 1–30.

[^ferreira-2002]: Ferreira, F. and Wehmeier, K., 2002, “On the consistency of the Delta-1-1-CA fragment of Frege’s Grundgesetze,” *Journal of Philosophic Logic*, 31: 301–311.

[^fitch-1964]: Fitch, F. B., 1964, “The hypothesis that infinite classes are similar,” *Journal of Symbolic Logic*, 4: 159–162.

[^girard-1972]: Girard, J.Y., 1972, *Interpretation fonctionelle et eleimination des coupures dans l’arithmetique d’ordre superieure*, These d’Etat, Université Paris 7.

[^goldfarb-2005]: Goldfarb, Warren, 2005. “On Godel’s way in: The influence of Rudolf Carnap.” *Bulletin of Symbolic Logic* 11(2): 185–193.

[^gödel-1995]: Gödel, K., 1995, *Collected Works Volume III, Unpublished Essays and Lectures*, Oxford: Oxford University Press, 1995.

[^gödel-1931]: –––, 1931, “Über formal untentscheidbare Sätze der Principia Mathematica und verwandter Systeme I,” *Monatshefte fü Mathematik und Physik*, 38: 173–198.

[^gödel-1944]: –––, 1944, “Russell’s mathematical logic,” in *The philosophy of Bertrand Russell*, P. A. Schilpp (ed.), Evanston: Northwestern University Press, 123–153.

[^gödel-1958]: –––, 1958, “Über eine bisher noch nicht benützte Erweiterung des finiten Standpunktes,”, *Dialectica*, 12: 280–287.

[^heck-1996]: Heck, R., Jr., 1996, “The consistency of predicative fragments of Frege’s Grundgesetze der Arithmetik,” *History and Philosophy of Logic*, 17(4): 209–220.

[^heijenoort-1967]: van Heijenoort, 1967, *From Frege to Gödel. A source book in mathematical logic 1879–1931*, Cambridge, MA: Harvard University Press.

[^hindley-1997]: Hindley, R., 1997, *Basic Simple Type Theory*, Cambridge: Cambridge University Press.

[^hodges-2008]: Hodges, W., 2008, “Tarski on Padoa’s Method: a test case for understanding logicians of other traditions”, in *Logic, Navya-Nyāya and Applications: Homage to Bimal Krishna Matilal*, Mihir K. Chakraborti et al. (eds.), London: College Publications, pp. 155–169

[^hofmann-1996]: Hofmann, M. and Streicher, Th. 1996, “The Groupoid interpretation of Type Theory,” in *Twenty-five years of constructive type theory* (Oxford Logic Guides: Volume 36), Oxford, New York: Oxford University Press, 83–111.

[^howard-1980]: Howard, W. A., 1980, “The formulae-as-types notion of construction,” in *To H. B. Curry: essays on combinatory logic, lambda calculus and formalism*, London, New York: Academic Press, 480–490.

[^hurkens-1995]: Hurkens, A. J. C., 1995, “A simplification of Girard’s paradox. Typed lambda calculi and applications,” in *Lecture Notes in Computer Science* (Volume 902), Berlin: Springer: 266–278.

[^lambek-1980]: Lambek, J., 1980. “From $\lambda$-calculus to Cartesian Closed Categories” in *To H.B. Curry: Essays on Combinatory Logic, $\lambda$-calculus and Formalism*, J. Seldin and J. Hindley (eds.), London, New York: Academic Press. pp. 375–402.

[^lambek-1986]: Lambek, J. and Scott, P. J., 1986, *Introduction to higher order categorical logic* (Cambridge Studies in Advanced Mathematics: Volume 7), Cambridge: Cambridge University Press; reprinted 1988.

[^lawvere-2003]: Lawvere, F. W. and Rosebrugh, R., 2003, *Sets for mathematics*, Cambridge: Cambridge University Press.

[^martin-löf-1970]: Martin-Löf, P., 1970, *Notes on constructive mathematics*, Stockholm: Almqvist & Wiksell.

[^martin-löf-1971]: –––, 1971, *A Theory of Types*, Technical Report 71–3, Stockholm: Stockholm University.

[^martin-löf-1998]: –––, 1998, “An intuitionistic theory of types,” in *Twenty-five years of constructive type theory* (Oxford Logic Guides: Volume 36), Oxford, New York: Oxford University Press, 127–172.

[^martin-löf-1975]: –––, 1975 [1973], “An intuitionistic theory of types: Predicative Part,” in *Logic Colloquium ’73* (Proceedings of the Logic Colloquium, Bristol 1973) (Studies in Logic and the Foundations of Mathematics: Volume 80), H.E. Rose and J.C. Shepherdson (eds.), Amsterdam: North-Holland, 73–118.

[^myhill-1974]: Myhill, J., 1974, “The Undefinability of the Set of Natural Numbers in the Ramified Principia”, in *Bertrand Russell’s Philosophy*, G. Nakhnikian (ed.), London: Duckworth, 19–27.

[^miquel-2001]: Miquel, A., 2001, *Le Calcul des Constructions implicite: syntaxe et sémantique*, Thèse de doctorat, Université Paris 7.

[^miquel-2003]: –––, 2003, “A strongly normalising Curry-Howard correspondence for IZF set theory,” in *Computer science Logic* (Lecture Notes in Computer Science, 2803), Berlin: Springer: 441–454.

[^oppenheimer-2011]: Oppenheimer, P. and E. Zalta, 2011, “Relations Versus Functions at the Foundations of Logic: Type-Theoretic Considerations”, *Journal of Logic and Computation*, 21: 351–374.

[^palmgren-1998]: Palmgren, Erik, 1998, “On universes in type theory,” in *Twenty-five years of Constructive Type Theory* (Oxford Logic Guides: Volume 36), Oxford, New York: Oxford University Press, 191–204.

[^poincaré-1909]: Poincaré, 1909, “H. La logique de l’infini” *Revue de metaphysique et de morale*, 17: 461–482.

[^prawitz-1967]: Prawitz, D., 1967, “Completeness and Hauptsatz for second order logic”, *Theoria*, 33: 246–258.

[^prawitz-1970]: –––, 1970, “On the proof theory of mathematical analysis,” in *Logic and value* (Essays dedicated to Thorild Dahlquist on his fiftieth birthday), Filosofiska Studier (Filosof. Föreningen och Filosof. Inst.), No. 9, Uppsala: Uppsala University, 169–180.

[^quine-1940]: Quine, W., 1940, “Review of Church ‘A formulation of the simple theory of types’,” *Journal of Symbolic Logic*, 5: 114.

[^ramsey-1926]: Ramsey, F.P., 1926, “The foundations of mathematics,” *Proceedings of the London Mathematical Society*, s2–25 (1), 338–384.

[^russell-1901]: Russell, B., 1901, “Sur la logique des relations avec des applications a la théorie des séries”, *Revue de Mathématique*, 7: 115–136, 137–148.

[^russell-1903]: –––, 1903, *The Principles of Mathematics*, Cambridge: Cambridge University Press.

[^russell-1908]: –––, 1908, “Mathematical logic as based on the theory of types,” *American Journal of Mathematics*, 30: 222–262.

[^russell-1919]: –––, 1919, *Introduction to Mathematical Philosophy*, London: George Allen and Unwin.

[^russell-1959]: –––, 1959, *My philosophical development*, London, New York: Routledge.

[^russell-1910]: Russell, B. and Whitehead, A., 1910, 1912, 1913, *Principia Mathematica* (3 volumes), Cambridge: Cambidge University Press.

[^reynolds-1974]: Reynolds, J., 1974, “Towards a theory of type structure,” in *Programming Symposium* (Lecture Notes in Computer Science: Volume 19), Berlin: Springer, 408–425.

[^reynolds-1983]: –––, 1983, “Types, Abstraction and Parametric Polymorphism,” *Proceedings of the IFIP 9th World Computer Congress*, Paris, 513–523.

[^reynolds-1984]: –––, 1984, “Polymorphism is not set-theoretic. Semantics of data types,” *Lecture Notes in Computer Science* (Volume 173), Berlin: Springer, 145–156.

[^reynolds-1985]: –––, 1985, “Three approaches to type structure. Mathematical foundations of software development,” in *Lecture Notes in Computer Science* (Volume 185), Berlin: Springer, 97–138.

[^schiemer-2013]: Schiemer, G. and Reck, E.H., 2013, “Logic in the 1930s: Type Theory and Model Theory,” *The Bulletin of Symbolic Logic*, 19(4): 433–472.

[^schütte-1960]: Schütte, K., 1960, *Beweistheorie*, Berlin: Springer-Verlag.

[^schütte-1960b]: –––, 1960b, “Syntactical and Semantical Properties of Simple Type Theory,” *Journal of Symbolic Logic*, 25: 305–326.

[^scott-1993]: Scott, D., 1993 “A type-theoretic alternative to ISWIM, CUCH, OWHY,” *Theoretical Computer Science*, 121: 411–440.

[^skolem-1970]: Skolem, T., 1970, *Selected works in logic*, Jens Erik Fenstad (ed.), Oslo: Universitetsforlaget.

[^tait-1967]: Tait, W. W., 1967, “Intensional interpretations of functionals of finite type,” *Journal of Symbolic Logic*, 32 (2): 198–212.

[^takeuti-1955]: Takeuti, G., 1955 “On the fundamental conjecture of GLC: I”, *Journal of the Mathematical Society of Japan*, 7: 249–275.

[^takeuti-1967]: –––, 1967, “Consistency proofs of subsystems of classical analysis,” *The Annals of Mathematics* (Second Series), 86 (2): 299–348.

[^tarski-1931]: Tarski, A., 1931, “Sur les ensembles definissables de nombres reels I,” *Fundamenta Mathematicae*, 17: 210–239.

[^urquhart-2003]: Urquhart, A., 2003, “The Theory of Types,” in *The Cambridge Companion to Bertrand Russell*, Nicholas Griffin (ed.), Cambridge: Cambridge University Press.

[^voevodsky-2015]: Voevodsky, V., 2015, “An experimental library of formalized mathematics based on univalent foundations,” *Mathematical Structures in Computer Science*, 25: 1278–1294, [available online](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/0E37CCB09CC1B7BA0AAE3F6A34F9727C/S0960129514000577a.pdf/an_experimental_library_of_formalized_mathematics_based_on_the_univalent_foundations.pdf).

[^wiener-1914]: Wiener, N., 1914, “A simplification of the logic of relations,” *Proceedings of the Cambridge Philosophical Society*, 17: 387–390.

[^weyl-1946]: Weyl, H., 1946, “Mathematics and Logic,” *American Mathematical Monthly*, 53: 2–13.

[^zermelo-1908]: Zermelo, E., 1908, “Untersuchungen über die Grundlagen der Mengenlehre I,” *Mathematische Annalen*, 65: 261–281.
