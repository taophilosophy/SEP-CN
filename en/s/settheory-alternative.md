# Alternative Axiomatic Set Theories
**First published Tue May 30, 2006; substantive revision Tue Sep 21, 2021**

*Holmes, M. Randall*

By “alternative set theories” we mean systems of set theory differing significantly from the dominant *ZF* (Zermelo-Frankel set theory) and its close relatives (though we will review these systems in the article). Among the systems we will review are typed theories of sets, Zermelo set theory and its variations, New Foundations and related systems, positive set theories, and constructive set theories. An interest in the range of alternative set theories does not presuppose an interest in replacing the dominant set theory with one of the alternatives; acquainting ourselves with foundations of mathematics formulated in terms of an alternative system can be instructive as showing us what any set theory (including the usual one) is supposed to do for us. The study of alternative set theories can dispel a facile identification of “set theory” with “Zermelo-Fraenkel set theory”; they are not the same thing.

## 1. Why Set Theory?

Why do we do set theory in the first place? The most immediately familiar objects of mathematics which might seem to be sets are geometric figures: but the view that these are best understood as sets of points is a modern view. Classical Greeks, while certainly aware of the formal possibility of viewing geometric figures as sets of points, rejected this view because of their insistence on rejecting the actual infinite. Even an early modern thinker like Spinoza could comment that it is obvious that a line is not a collection of points (whereas for us it may be hard to see what else it could be; *Ethics*, I.15, scholium IV, 96).

Cantor’s set theory (which we will not address directly here as it was not formalized) arose out of an analysis of complicated subcollections of the real line defined using tools of what we would now call topology (Cantor 1872)[^cantor-1872]. A better advertisement for the usefulness of set theory for foundations of mathematics (or at least one easier to understand for the layman) is Dedekind’s definition of real numbers using “cuts” in the rational numbers (Dedekind 1872)[^dedekind-1872] and the definition of the natural numbers as sets due to Frege and Russell (Frege 1884)[^frege-1884].

Most of us agree on what the theories of natural numbers, real numbers, and Euclidean space ought to look like (though constructivist mathematicians will have differences with classical mathematics even here). There was at least initially less agreement as to what a theory of sets ought to look like (or even whether there ought to be a theory of sets). The confidence of at least some mathematicians in their understanding of this subject (or in its coherence as a subject at all) was shaken by the discovery of paradoxes in “naive” set theory around the beginning of the twentieth century. A number of alternative approaches were considered then and later, but a single theory, the Zermelo-Fraenkel theory with the Axiom of Choice (*ZFC*) dominates the field in practice. One of the strengths of the Zermelo-Fraenkel set theory is that it comes with an image of what the world of set theory is (just as most of us have a common notion of what the natural numbers, the real numbers, and Euclidean space are like): this image is what is called the “cumulative hierarchy” of sets.

### 1.1 The Dedekind construction of the reals

In the nineteenth century, analysis (the theory of the real numbers) needed to be put on a firm logical footing. Dedekind’s definition of the reals (Dedekind 1872)[^dedekind-1872] was a tool for this purpose.

Suppose that the rational numbers are understood (this is of course a major assumption, but certainly the rationals are more easily understood than the reals).

Dedekind proposed that the real numbers could be uniquely correlated with *cuts* in the rationals, where a cut was determined by a pair of sets $(L, R)$ with the following properties: $L$ and $R$ are sets of rationals. $L$ and $R$ are both nonempty and every element of $L$ is less than every element of $R$ (so the two sets are disjoint). $L$ has no greatest element. The union of $L$ and $R$ contains all rationals.

If we understand the theory of the reals prior to the cuts, we can say that each cut is of the form $L = (-\infty , r) \cap \mathbf{Q}, R = [r, \infty) \cap \mathbf{Q}$, where $\mathbf{Q}$ is the set of all rationals and $r$ is a unique real number uniquely determining and uniquely determined by the cut. It is obvious that each real number $r$ uniquely determines a cut in this way (but we need to show that there are no other cuts). Given an arbitrary cut $(L, R)$, we propose that $r$ will be the least upper bound of $L$. The Least Upper Bound Axiom of the usual theory of the reals tells us that $L$ has a least upper bound $(L$ is nonempty and any element of $R$ (which is also nonempty) is an upper bound of $L$, so $L$ has a least upper bound). Because $L$ has no greatest element, its least upper bound $r$ cannot belong to $L$. Any rational number less than $r$ is easily shown to belong to $L$ and any rational number greater than or equal to $r$ is easily shown to belong to $R$, so we see that the cut we chose arbitrarily (and so any cut) is of the form $L = (-\infty , r) \cap \mathbf{Q}, R = [r, \infty) \cap \mathbf{Q}$.

A bolder move (given a theory of the rationals but no prior theory of the reals) is to *define* the real numbers as cuts. Notice that this requires us to have not only a theory of the rational numbers (not difficult to develop) but also a theory of sets of rational numbers: if we are to understand a real number to be identified with a cut in the rational numbers, where a cut is a pair of sets of rational numbers, we do need to understand what a set of rational numbers is. If we are to demonstrate the existence of particular real numbers, we need to have some idea what sets of rational numbers there are.

An example: when we have defined the rationals, and then defined the reals as the collection of Dedekind cuts, how do we define the square root of 2? It is reasonably straightforward to show that $(\{x \in \mathbf{Q} \mid x \lt 0 \vee x^2 \lt 2\}, \{x \in \mathbf{Q} \mid x \gt 0 \amp x^2 \ge 2\})$ is a cut and (once we define arithmetic operations) that it is the positive square root of two. When we formulate this definition, we appear to presuppose that any property of rational numbers determines a set containing just those rational numbers that have that property.

### 1.2 The Frege-Russell definition of the natural numbers

Frege (1884)[^frege-1884] and Russell (1903)[^russell-1903] suggested that the simpler concept “natural number” also admits analysis in terms of sets. The simplest application of natural numbers is to count finite sets. We are all familiar with finite collections with 1, 2, 3, … elements. Additional sophistication may acquaint us with the empty set with 0 elements.

Now consider the number 3. It is associated with a particular property of finite sets: having three elements. With that property it may be argued that we may naturally associate an object, the collection of all sets with three elements. It seems reasonable to identify this set as the number 3. This definition might seem circular (3 is the set of all sets with 3 elements?) but can actually be put on a firm, non-circular footing.

Define 0 as the set whose only element is the empty set. Let $A$ be any set; define $A + 1$ as the collection of all sets $a \cup \{x\}$ where $a \in A$ and $x \not\in a$ (all sets obtained by adding a new element to an element of $A)$. Then $0 + 1$ is clearly the set we want to understand as $1, 1 + 1$ is the set we want to understand as $2, 2 + 1$ is the set we want to understand as 3, and so forth.

We can go further and define the set $\mathbf{N}$ of natural numbers. 0 is a natural number and if $A$ is a natural number, so is $A + 1$. If a set $S$ contains 0 and is closed under successor, it will contain all natural numbers (this is one form of the principle of mathematical induction). Define $\mathbf{N}$ as the intersection of all sets $I$ which contain 0 and contain $A + 1$ whenever $A$ is in $I$ and $A + 1$ exists. One might doubt that there is any inductive set, but consider the set $V$ of all $x$ such that $x = x$ (the universe). There is a formal possibility that $V$ itself is finite, in which case there would be a last natural number $\{V\}$; one usually assumes an Axiom of Infinity to rule out such possibilities.

## 2. Naive Set Theory

In the previous section, we took a completely intuitive approach to our applications of set theory. We assumed that the reader would go along with certain ideas of what sets are like.

What are the identity conditions on sets? It seems entirely in accord with common sense to stipulate that a set is precisely determined by its elements: two sets $A$ and $B$ are the same if for every $x$, either $x \in A$ and $x \in B$ or $x \not\in A$ and $x \not\in B$:

$$ A = B \leftrightarrow \forall x(x \in A \leftrightarrow x \in B) $$

This is called the *axiom of extensionality*.

It also seems reasonable to suppose that there are things which are not sets, but which are capable of being members of sets (such objects are often called *atoms* or *urelements*). These objects will have no elements (like the empty set) but will be distinct from one another and from the empty set. This suggests the alternative weaker axiom of extensionality (perhaps actually closer to common sense),

$$ [\textrm{set}(A) \amp \textrm{set}(B) \amp \forall x(x \in A \leftrightarrow x \in B)] \rightarrow A = B $$

with an accompanying axiom of sethood

$$ x \in A \rightarrow \textrm{ set}(A) $$

What sets are there? The simplest collections are given by enumeration (the set {*Tom*, *Dick*, *Harry*} of men I see over there, or (more abstractly) the set $\{-2, 2\}$ of square roots of 4. But even for finite sets it is often more convenient to give a defining property for elements of the set: consider the set of all grandmothers who have a legal address in Boise, Idaho; this is a finite collection but it is inconvenient to list its members. The general idea is that for any property $P$, there is a set of all objects with property $P$. This can be formalized as follows: For any formula $P(x)$, there is a set $A$ (the variable $A$ should not be free in $P(x))$ such that

$$ \forall x(x \in A \leftrightarrow P(x)). $$

This is called the *axiom of comprehension*. If we have weak extensionality and a sethood predicate, we might want to say

$$ \exists A(\textrm{set}(A) \amp \forall x(x \in A \leftrightarrow P(x))) $$

The theory with these two axioms of extensionality and comprehension (usually without sethood predicates) is called *naive set theory*.

It is clear that comprehension allows the definition of finite sets: our set of men {*Tom*, *Dick*, *Harry*} can also be written $\{x \mid {}$ $x = \textit{Tom}$ ${}\lor{}$ $x = \textit{Dick}$ ${}\lor{}$ $x = \textit{Harry}\}$. It also appears to allow for the definition of *infinite* sets, such as the set $(\{x \in \mathbf{Q} \mid x \lt 0 \lor x^2 \lt 2\}$ mentioned above in our definition of the square root of 2.

Unfortunately, naive set theory is inconsistent. Russell gave the most convincing proof of this, although his was not the first paradox to be discovered: let $P(x)$ be the property $x \not\in x$. By the axiom of comprehension, there is a set $R$ such that for any $x, x \in R$ iff $x \not\in x$. But it follows immediately that $R \in R$ iff $R \not\in R$, which is a contradiction.

It must be noted that our formalization of naive set theory is an anachronism. Cantor did not fully formalize his set theory, so it cannot be determined whether his system falls afoul of the paradoxes (he did not think so, and there are some who agree with him now). Frege formalized his system more explicitly, but his system was not precisely a set theory in the modern sense: the most that can be said is that his system is inconsistent, for basically the reason given here, and a full account of the differences between Frege’s system and our “naive set theory” is beside the point (though historically certainly interesting).

### 2.1 The other paradoxes of naive set theory

Two other paradoxes of naive set theory are usually mentioned, the paradox of Burali-Forti (1897)[^burali-forti-1897]—which has historical precedence—and the paradox of Cantor. To review these other paradoxes is a convenient way to review as well what the early set theorists were up to, so we will do it. Our formal presentation of these paradoxes is anachronistic; we are interested in their mathematical content, but not necessarily in the exact way that they were originally presented.

Cantor in his theory of sets was concerned with defining notions of infinite cardinal number and infinite ordinal number. Consideration of the largest ordinal number gave rise to the Burali-Forti paradox, and consideration of the largest cardinal number gave rise to the Cantor paradox.

Infinite ordinals can be presented in naive set theory as isomorphism classes of well-orderings (a well-ordering is a linear order $\le$ with the property that any nonempty subset of its domain has a $\le$-least element). We use reflexive, antisymmetric, transitive relations $\le$ as our linear orders rather than the associated irreflexive, asymmetric, transitive relations $\lt$, because this allows us to distinguish between the ordinal numbers 0 and 1 (Russell and Whitehead took the latter approach and were unable to define an ordinal number 1 in their *Principia Mathematica*).

There is a natural order on ordinal numbers (induced by the fact that of any two well-orderings, at least one will be isomorphic to an initial segment of the other) and it is straightforward to show that it is a well-ordering. Since it is a well-ordering, it belongs to an isomorphism class (an ordinal number!) $\Omega$.

It is also straightforward to show that the order type of the natural order on the ordinals restricted to the ordinals less than *α* is *α*: the order on $\{0, 1, 2\}$ is of order type 3, the order on the finite ordinals $\{0, 1, 2, \ldots \}$ is the first infinite ordinal *ω*, and so forth.

But then the order type of the ordinals $\lt \Omega$ is $\Omega$ itself, which means that the order type of *all* the ordinals (including $\Omega)$ is “greater”—but $\Omega$ was defined as the order type of all the ordinals and should not be greater than itself!

This paradox was presented first (Cantor was aware of it) and Cantor did not think that it invalidated his system.

Cantor defined two sets as having the same cardinal number if there was a bijection between them. This is of course simply common sense in the finite realm; his originality lay in extending it to the infinite realm and refusing to shy from the apparently paradoxical results. In the infinite realm, cardinal and ordinal number are not isomorphic notions as they are in the finite realm: a well-ordering of order type *ω* (say, the usual order on the natural numbers) and a well-ordering of order type $\omega + \omega$ (say, the order on the natural numbers which puts all odd numbers before all even numbers and puts the sets of odd and even numbers in their usual order) represent different ordinal numbers but their fields (being the same set!) are certainly of the same size. Such “paradoxes” as the apparent equinumerousness of the natural numbers and the perfect squares (noted by Galileo) and the one-to-one correspondence between the points on concentric circles of different radii, noted since the Middle Ages, were viewed as matter-of-fact evidence for equinumerousness of particular infinite sets by Cantor.

Novel with Cantor was the demonstration (1872) that there are infinite sets of different sizes according to this criterion. Cantor’s paradox, for which an original reference is difficult to find, is an immediate corollary of this result. If $A$ is a set, define the *power set* of $A$ as the set of all subsets of $A: \wp(A) = \{B \mid \forall x(x \in B \rightarrow x \in A)\}$. Cantor proved that there can be no bijection between $A$ and $\wp(A)$ for any set $A$. Suppose that $f$ is a bijection from $A$ to $\wp(A)$. Define $C$ as $\{a \in A \mid a \not\in f(a)\}$. Because $f$ is a bijection there must be $c$ such that $f(c) = C$. Now we notice that $c \in C \leftrightarrow c \not\in f (c) = C$, which is a contradiction.

Cantor’s theorem just proved shows that for any set $A$, there is a set $\wp(A)$ which is larger. Cantor’s paradox arises if we try to apply Cantor’s theorem to the set of all sets (or to the universal set, if we suppose (with common sense) that not all objects are sets). If $V$ is the universal set, then $\wp(V)$, the power set of the universal set (the set of all sets) must have larger cardinality than $V$. But clearly no set can be larger in cardinality than the set which contains everything!

Cantor’s response to both of these paradoxes was telling (and can be formalized in *ZFC* or in the related systems which admit proper classes, as we will see below). He essentially reinvoked the classical objections to infinite sets on a higher level. Both the largest cardinal and the largest ordinal arise from considering the very largest collections (such as the universe $V)$. Cantor drew a distinction between legitimate mathematical infinities such as the countable infinity of the natural numbers (with its associated cardinal number $\aleph_0$ and many ordinal numbers $\omega , \omega + 1, \ldots ,\omega + \omega ,\ldots)$, the larger infinity of the continuum, and further infinities derived from these, which he called *transfinite*, and what he called the Absolute Infinite, the infinity of the collection containing everything and of such related notions as the largest cardinal and the largest ordinal. In this he followed St. Augustine (*De Civitate Dei*) who argued in late classical times that the infinite collection of natural numbers certainly existed as an actual infinity because God was aware of each and every natural number, but because God’s knowledge encompassed all the natural numbers their totality was somehow finite in His sight. The fact that his defense of set theory against the Burali-Forti and Cantor paradoxes was subsequently successfully formalized in *ZFC* and the related class systems leads some to believe that Cantor’s own set theory was not implicated in the paradoxes.

## 3. Typed Theories

An early response to the paradoxes of set theory (by Russell, who discovered one of them) was the development of type theory (see the appendix to Russell’s *The Principles of Mathematics* (1903) or Whitehead & Russell’s *Principia Mathematica* (1910–1913).

The simplest theory of this kind, which we call TST (Théorie Simple des Types, from the French, following Forster and others) is obtained as follows. We admit sorts of object indexed by the natural numbers (this is purely a typographical convenience; no actual reference to natural numbers is involved). Type 0 is inhabited by “individuals” with no specified structure. Type 1 is inhabited by sets of type 0 objects, and in general type $n + 1$ is inhabited by sets of type $n$ objects.

The type system is enforced by the grammar of the language. Atomic sentences are equations or membership statements, and they are only well-formed if they take one of the forms $x^{n} = y^{n}$ or $x^{n} \in y^{n+1}$.

The axioms of extensionality of *TST* take the form

$$ A^{n+1} = B^{n+1} \leftrightarrow \forall x^n (x^n \in A^{n+1} \leftrightarrow x^n \in B^{n+1}); $$

there is a separate axiom for each $n$.

The axioms of comprehension of *TST* take the form (for any choice of a type $n$, a formula *φ*, and a variable $A^{n+1}$ not free in $\phi)$

$$ \exists A^{n+1}\forall x^n (x^n \in A^{n+1} \leftrightarrow \phi) $$

It is interesting to observe that the axioms of *TST* are precisely analogous to those of naive set theory.

This is not the original type theory of Russell. Leaving aside Russell’s use of “propositional functions” instead of classes and relations, the system of *Principia Mathematica* (Whitehead & Russell 1910–1913)[^whitehead-1910], hereinafter *PM*, fails to be a set theory because it has separate types for relations (propositional functions of arity $\gt 1)$. It was not until Norbert Wiener observed in 1914 that it was possible to define the ordered pair as a set (his definition of $\lt x, y \gt$ was not the current $\{\{x\},\{x, y\}\}$, due to Kuratowski (1921)[^kuratowski-1921], but $\{\{\{x\}, \varnothing \},\{\{y\}\}\})$ that it became clear that it is possible to code relation types into set types. Russell frequently said in English that relations could be understood as sets of pairs (or longer tuples) but he had no implementation of this idea (in fact, he defined ordered pairs as relations in *PM* rather than the now usual reverse!) For a discussion of the history of this simplified type theory, see Wang 1970.

Further, Russell was worried about circularity in definitions of sets (which he believed to be the cause of the paradoxes) to the extent that he did not permit a set of a given type to be defined by a condition which involved quantification over the same type or a higher type. This *predicativity* restriction weakens the mathematical power of set theory to an extreme degree.

In Russell’s system, the restriction is implemented by characterizing a type not only by the type of its elements but by an additional integer parameter called its “order”. For any object with elements, the order of its type is higher than the order of the type of its elements. Further, the comprehension axiom is restricted so that the condition defining a set of a type of order $n$ can contain parameters only of types with order $\le n$ and quantifiers only over types with order $\lt n$. Russell’s system is further complicated by the fact that it is not a theory of sets, as we noted above, because it also contains relation types (this makes a full account of it here inappropriate). Even if we restrict to types of sets, a simple linear hierarchy of types is not possible if types have order, because each type has “power set” types of each order higher than its own.

We present a typed theory of sets with predicativity restrictions (we have seen this in work of Marcel Crabbé, but it may be older). In this system, the types do not have orders, but Russell’s ramified type theory with orders (complete with relation types) can be interpreted in it (a technical result of which we do not give an account here).

The syntax of predicative *TST* is the same as that of the original system. The axioms of extensionality are also the same. The axioms of comprehension of predicative *TST* take the form (for any choice of a type $n$, a formula *φ*, and a variable $A^{n+1}$ not free in *φ*, satisfying the restriction that no parameter of type $n + 2$ or greater appears in *φ*, nor does any quantifier over type $n + 1$ or higher appear in $\phi)$

$$ \exists A^{n+1}\forall x^n (x^n \in A^{n+1} \leftrightarrow \phi) $$

Predicative mathematics does not permit unrestricted mathematical induction: In impredicative type theory, we can define 0 and the “successor” $A^+$ of a set just as we did above in naive set theory (in a given type $n)$ then define the set of natural numbers:

$$ \begin{aligned} \mathbf{N}^{n+1} = \{m^n \mid\forall A^{n+1}[[0^n \in A^{n+1} \amp \forall B^n (B^n \in A^{n+1} \rightarrow (B^+)^n \in A^{n+1})] \\ \rightarrow m^n \in A^{n+1}] \} \end{aligned} $$

Russell would object that the set $\mathbf{N}^{n+1}$ is being “defined” in terms of facts about *all* sets $A^{n+1}$: something is a type $n + 1$ natural number just in case it belongs to all type $n + 1$ inductive sets. But one of the type $n + 1$ sets in terms of which it is being “defined” is $\mathbf{N}^{n+1}$ itself. (Independently of predicativist scruples, one does need an Axiom of Infinity to ensure that all natural numbers exist; this is frequently added to *TST*, as is the Axiom of Choice).

For similar reasons, predicative mathematics does not permit the Least Upper Bound Axiom of analysis (the proof of this axiom in a set theoretical implementation of the reals as Dedekind cuts fails for the same kind of reason).

Russell solved these problems in *PM* by adopting an Axiom of Reducibility which in effect eliminated the predicativity restrictions, but in later comments on *PM* he advocated abandoning this axiom.

Most mathematicians are not predicativists; in our opinion the best answer to predicativist objections is to deny that comprehension axioms can properly be construed as definitions (though we admit that we seem to find ourselves frequently speaking loosely of *φ* as the condition which “defines” $\{x \mid \phi \})$.

It should be noted that it is possible to do a significant amount of mathematics while obeying predicativist scruples. The set of natural numbers cannot be defined in the predicative version of *TST*, but the set of singletons of natural numbers can be defined and can be used to prove some instances of induction (enough to do quite a bit of elementary mathematics). Similarly, a version of the Dedekind construction of the real numbers can be carried out, in which many important instances of the least upper bound axiom will be provable.

Type theories are still in use, mostly in theoretical computer science, but these are type theories of *functions*, with complexity similar to or greater than the complexity of the system of *PM*, and fortunately outside the scope of this study.

## 4. Zermelo Set Theory and Its Refinements

In this section we discuss the development of the usual set theory *ZFC*. It did not spring up full-grown like Athena from the head of Zeus!

### 4.1 Zermelo set theory

The original theory *Z* of Zermelo (1908)[^zermelo-1908] had the following axioms:

**Extensionality:** Sets with the same elements are equal. (The original version appears to permit non-sets (atoms) which all have no elements, much as in my discussion above under naive set theory).

**Pairing:** For any objects $a$ and $b$, there is a set $\{a, b\} = \{x \mid x = a \lor x = b\}$. (the original axiom also provided the empty set and singleton sets).

**Union:** For any set $A$, there is a set $\cup A = \{x \mid \exists y(x \in y \amp y \in A)\}$. The union of $A$ contains all the elements of elements of $A$.

**Power Set:** For any set $A$, there is a set $\wp(A) = \{x \mid \forall y(y \in x \rightarrow y \in A)\}$. The power set of $A$ is the set of all subsets of $A$.

**Infinity:** There is an infinite set. Zermelo’s original formulation asserted the existence of a set containing $\varnothing$ and closed under the singleton operation: $\{\varnothing ,\{\varnothing \},\{\{\varnothing \}\}, \ldots \}$. It is now more usual to assert the existence of a set which contains $\varnothing$ and is closed under the von Neumann successor operation $x \mapsto x \cup \{x\}$. (Neither of these axioms implies the other in the presence of the other axioms, though they yield theories with the same mathematical strength).

**Separation:** For any property $P(x)$ of objects and any set $A$, there is a set $\{x \in A \mid P(x)\}$ which contains all the elements of $A$ with the property $P$.

**Choice:** For every set $C$ of pairwise disjoint nonempty sets, there is a set whose intersection with each element of $C$ has exactly one element.

We note that we do not need an axiom asserting the existence of $\varnothing$ (which is frequently included in axiom lists as it was in Zermelo’s original axiom set): the existence of any object (guaranteed by logic unless we use a free logic) along with separation will do the trick, and even if we use a free logic the set provided by Infinity will serve (the axiom of Infinity can be reframed to say that there is a set which contains all sets with no elements (without presupposing that there are any) and is closed under the desired successor operation).

Every axiom of Zermelo set theory except Choice is an axiom of naive set theory. Zermelo chose enough axioms so that the mathematical applications of set theory could be carried out and restricted the axioms sufficiently that the paradoxes could not apparently be derived.

The most general comprehension axiom of *Z* is the axiom of Separation. If we try to replicate the Russell paradox by constructing the set $R' = \{x \in A \mid x \not\in x\}$, we discover that $R' \in R' \leftrightarrow R' \in A \amp R' \not\in R'$, from which we deduce $R' \not\in A$. For any set $A$, we can construct a set which does not belong to it. Another way to put this is that *Z* proves that there is no universal set: if we had the universal set $V$, we would have naive comprehension, because we could define $\{x \mid P(x)\}$ as $\{x \in V \mid P(x)\}$ for any property $P(x)$, including the fatal $x \not\in x$.

In order to apply the axiom of separation, we need to have some sets $A$ from which to carve out subsets using properties. The other axioms allow the construction of a lot of sets (all sets needed for classical mathematics outside of set theory, though not all of the sets that even Cantor had constructed with apparent safety).

The elimination of the universal set seems to arouse resistance in some quarters (many of the alternative set theories recover it, and the theories with sets and classes recover at least a universe of all sets). On the other hand, the elimination of the universal set seems to go along with Cantor’s idea that the problem with the paradoxes was that they involved Absolutely Infinite collections—purported “sets” that are too large.

### 4.2 From Zermelo set theory to *ZFC*

Zermelo set theory came to be modified in certain ways.

The formulation of the axiom of separation was made explicit: “for each formula *φ* of the first-order language with equality and membership, $\{x \in A \mid \phi \}$ exists”. Zermelo’s original formulation referred more vaguely to properties in general (and Zermelo himself seems to have objected to the modern formulation as too restrictive).

The non-sets are usually abandoned (so the formulation of Extensionality is stronger) though *ZFA* (Zermelo-Fraenkel set theory with atoms) was used in the first independence proofs for the Axiom of Choice.

The axiom scheme of Replacement was added by Fraenkel to make it possible to construct larger sets (even $\aleph_{\omega}$ cannot be proved to exist in Zermelo set theory). The basic idea is that any collection the same size as a set is a set, which can be logically formulated as follows: if $\phi(x,y)$ is a functional formula [this means $\forall x\forall y\forall z[(\phi(x,y) \amp \phi(x,z)) \rightarrow y = z$] and $A$ is a set then there is a set $\{y \mid \exists x \in A(\phi(x,y))\}$.

The axiom scheme of Foundation was added to support a definite conception of what the universe of sets is like. The idea of the cumulative hierarchy of sets is that we construct sets in a sequence of stages indexed by the ordinals: at stage 0, the empty set is constructed; at stage $\alpha + 1$, all subsets of the set of stage *α* sets are constructed; at a limit stage *λ*, the union of all stages with index less than *λ* is constructed. Replacement is important for the implementation of this idea, as *Z* only permits one to construct sets belonging to the stages $V_n$ and $V_{\omega +n}$ for $n$ a natural number (we use the notation $V_{\alpha}$ for the collection of all sets constructed at stage $\alpha)$. The intention of the Foundation Axiom is to assert that every set belongs to some $V_{\alpha}$ ; the commonest formulation is the mysterious assertion that for any nonempty set $A$, there is an element $x$ of $A$ such that $x$ is disjoint from $A$. To see that this is at least implied by Foundation, consider that there must be a smallest *α* such that $A$ meets $V_{\alpha}$, and any $x$ in this $V_{\alpha}$ will have elements (if any) only of smaller rank and so not in $A$.

Zermelo set theory has difficulties with the cumulative hierarchy. The usual form of the Zermelo axioms (or Zermelo’s original form) does not prove the existence of $V_{\alpha}$ as a set unless *α* is finite. If the Axiom of Infinity is reformulated to assert the existence of $V_{\omega}$, then the ranks proved to exist as sets by Zermelo set theory are exactly those which appear in the natural model $V_{\omega +\omega}$ of this theory. Also, Zermelo set theory does not prove the existence of transitive closures of sets, which makes it difficult to assign ranks to sets in general. Zermelo set theory plus the assertion that every set belongs to a rank $V_{\alpha}$ which is a set implies Foundation, the existence of expected ranks $V_{\alpha}$ (not the existence of such ranks for all ordinals *α* but the existence of such a rank containing each set which can be shown to exist), and the existence of transitive closures, and can be interpreted in Zermelo set theory without additional assumptions.

A reader who wants to examine models of Zermelo set theory which exhibit pathological properties in this regard can consult Mathias (2001b)[^mathias-2001b].

The Axiom of Choice is an object of suspicion to some mathematicians because it is not constructive. It has become customary to indicate when a proof in set theory uses Choice, although most mathematicians accept it as an axiom. The Axiom of Replacement is sometimes replaced with the Axiom of Collection, which asserts, for any formula $\phi(x,y)$:

$$ \forall x \in A\exists y(\phi(x,y)) \rightarrow \exists C\forall x \in A\exists y \in C(\phi(x,y)) $$

Note that *φ* here does not need to be functional; if for every $x \in A$, there are some *y'*s such that $\phi(x, y)$, there is a set such that for every $x \in A$, there is $y$ *in that set* such that $\phi(x, y)$. One way to build this set is to take, for each $x \in A$, all the $y$s of minimal rank such that $\phi(x, y)$ and put them in $C$. In the presence of all other axioms of *ZFC*, Replacement and Collection are equivalent; when the axiomatics is perturbed (or when the logic is perturbed, as in intuitionistic set theory) the difference becomes important. The Axiom of Foundation is equivalent to $\in$-Induction here but not in other contexts: $\in$-Induction is the assertion that for any formula *φ*:

$$ \forall x((\forall y \in x(\phi(y)) \rightarrow \phi(x)) \rightarrow \forall x\phi(x) $$

i.e., anything which is true of any set if it is true of all its elements is true of every set without exception.

### 4.3 Critique of Zermelo set theory

A common criticism of Zermelo set theory is that it is an *ad hoc* selection of axioms chosen to avoid paradox, and we have no reason to believe that it actually achieves this end. We believe such objections to be unfounded, for two reasons. The first is that the theory of types (which is the result of a principled single modification of naive set theory) is easily shown to be precisely equivalent in consistency strength and expressive power to *Z* with the restriction that all quantifiers in the formulas *φ* in instances of separation must be bounded in a set; this casts doubt on the idea that the choice of axioms in *Z* is particularly arbitrary. The fact that the von Neumann-Gödel-Bernays class theory (discussed below) turns out to be a conservative extension of *ZFC* suggests that full *ZFC* is a precise formulation of Cantor’s ideas about the Absolute Infinite (and so not arbitrary). Further, the introduction of the Foundation Axiom identifies the set theories of this class as the theories of a particular class of structures (the well-founded sets) of which the Zermelo axioms certainly seem to hold (whether Replacement holds so evidently is another matter).

These theories are frequently extended with large cardinal axioms (the existence of inaccessible cardinals, Mahlo cardinals, weakly compact cardinals, measurable cardinals and so forth). These do not to us signal a new kind of set theory, but represent answers to the question as to how large the universe of Zermelo-style set theory is.

The choice of Zermelo set theory (leaving aside whether one goes on to *ZFC*) rules out the use of equivalence classes of equinumerous sets as cardinals (and so the use of the Frege natural numbers) or the use of equivalence classes of well-orderings as ordinals. There is no difficulty with the use of the Dedekind cut formulation of the reals (once the rationals have been introduced). Instead of the equivalence class formulations of cardinal and ordinal numbers, the *von Neumann ordinals* are used: a von Neumann ordinal is a transitive set (all of its elements are among its subsets) which is well-ordered by membership. The order type of a well-ordering is the von Neumann ordinal of the same length (the axiom of Replacement is needed to prove that every set well-ordering has an order type; this can fail to be true in Zermelo set theory, where the von Neumann ordinal $\omega + \omega$ cannot be proven to exist but there are certainly well-orderings of this and longer order types). The cardinal number $|A|$ is defined as the smallest order type of a well-ordering of $A$ (this requires Choice to work; without choice, we can use Foundation to define the cardinal of a set $A$ as the set of all sets equinumerous with $A$ and belonging to the first $V_{\alpha}$ containing sets equinumerous with $A)$. This is one respect in which Cantor’s ideas do not agree with the modern conception; he appears to have thought that he could define at least cardinal numbers as equivalence classes (or at least that is one way to interpret what he says), although such equivalence classes would of course be Absolutely Infinite.

### 4.4 Weak variations and theories with hypersets

Some weaker subsystems of *ZFC* are used. Zermelo set theory, the system *Z* described above, is still studied. The further restriction of the axiom of separation to formulas in which all quantifiers are bounded in sets $(\Delta_0$ separation) yields “bounded Zermelo set theory” or “Mac Lane set theory”, so called because it has been advocated as a foundation for mathematics by Saunders Mac Lane (1986). It is interesting to observe that Mac Lane set theory is precisely equivalent in consistency strength and expressive power to *TST* with the Axiom of Infinity. *Z* is strictly stronger than Mac Lane set theory; the former theory proves the consistency of the latter. See Mathias 2001a for an extensive discussion.

The set theory *KPU* (Kripke-Platek set theory with urelements, for which see Barwise 1975)[^barwise-1975] is of interest for technical reasons in model theory. The axioms of *KPU* are the weak Extensionality which allows urelements, Pairing, Union, $\Delta_0$ separation, $\Delta_0$ collection, and $\in$-induction for arbitrary formulas. Note the absence of Power Set. The technical advantage of *KPU* is that all of its constructions are “absolute” in a suitable sense. This makes the theory suitable for the development of an extension of recursion theory to sets.

The dominance of *ZFC* is nowhere more evident than in the great enthusiasm and sense of a new departure found in reactions to the very slight variation of this kind of set theory embodied in versions of *ZFC* without the foundation axiom. It should be noted that the Foundation Axiom was not part of the original system!

We describe two theories out of a range of possible theories of *hypersets* (Zermelo-Frankel set theory without foundation). A source for theories of this kind is Aczel 1988.

In the following paragraphs, we will use the term “graph” for a relation, and “extensional graph” for a relation $R$ satisfying

$$ (\forall y,z \in \textit{field}(R)[\forall x(xRy \equiv xRz) \rightarrow y = z]. $$

A decoration of a graph $G$ is a function $f$ with the property that $f(x) = \{f(y) \mid yGx\}$ for all $x$ in the field of $G$. In *ZFC*, all well-founded relations have unique decorations, and non-well-founded relations have no decorations. Aczel proposed his Anti-Foundation Axiom: *every set graph has a unique decoration*. Maurice Boffa considered a stronger axiom: every partial, injective decoration of an extensional set graph $G$ whose domain contains the $G$-preimages of all its elements can be extended to an injective decoration of all of $G$.

The Aczel system is distinct from the Boffa system in having fewer ill-founded objects. For example, the Aczel theory proves that there is just one object which is its own sole element, while the Boffa theory provides a proper class of such objects. The Aczel system has been especially popular, and we ourselves witnessed a great deal of enthusiasm for this subversion of the cumulative hierarchy. We are doubtless not the only ones to point this out, but we did notice and point out to others that at least the Aczel theory has a perfectly obvious analogue of the cumulative hierarchy. If $A_{\alpha}$ is a rank, the successor rank $A_{\alpha +1}$ will consist of all those sets which can be associated with graphs $G$ with a selected point $t$ with all elements of the field of $G$ taken from $A_{\alpha}$. The zero and limit ranks are constructed just as in *ZFC*. Every set belongs to an $A_{\alpha}$ for *α* less than or equal to the cardinality of its transitive closure. (It seems harder to impose rank on the world of the Boffa theory, though it can be done: the proper class of self-singletons is an obvious difficulty, to begin with!).

It is true (and has been the object of applications in computer science) that it is useful to admit reflexive structures for some purposes. The kind of reflexivity permitted by Aczel’s theory has been useful for some such applications. However, such structures are modelled in well-founded set theory (using relations other than membership) with hardly more difficulty, and the reflexivity admitted by Aczel’s theory (or even by a more liberal theory like that of Boffa) doesn’t come near the kind of non-well-foundedness found in genuinely alternative set theories, especially those with universal set. These theories are close variants of the usual theory *ZFC*, caused by perturbing the last axiom to be added to this system historically (although, to be fair, the Axiom of Foundation is the one which arguably defines the unique structure which the usual set theory is about; the anti-foundation axioms thus invite us to contemplate different, even if closely related, universal structures).

## 5. Theories with Classes

### 5.1 Class theory over *ZFC*

Even those mathematicians who accepted the Zermelo-style set theories as the standard (most of them!) often found themselves wanting to talk about “all sets”, or “all ordinals”, or similar concepts.

Von Neumann (who actually formulated a theory of functions, not sets), Gödel, and Bernays developed closely related systems which admit, in addition to the sets found in *ZFC*, general collections of these sets. (In Hallett 1984, it is argued that the system of von Neumann was the first system in which the Axiom of Replacement was implemented correctly [there were technical problems with Fraenkel’s formulation], so it may actually be the first implementation of *ZFC*.)[^hallett-1984]

We present a theory of this kind. Its objects are *classes*. Among the classes we identify those which are elements as sets.

**Axiom of extensionality:** Classes with the same elements are the same.

**Definition:** A class $x$ is a *set* just in case there is a class $y$ such that $x \in y$. A class which is not a set is said to be a proper class.

**Axiom of class comprehension:** For any formula $\phi(x)$ which involves quantification only over all sets (not over all classes), there is a class $\{x \mid \phi(x)\}$ which contains exactly those *sets* $x$ for which $\phi(x)$ is true.

The axiom scheme of class comprehension with quantification only over sets admits a finite axiomatization (a finite selection of formulas *φ* (most with parameters) suffices) and was historically first presented in this way. It is an immediate consequence of class comprehension that the Russell class $\{x \mid x \not\in x\}$ cannot be a set (so there is at least one proper class).

**Axiom of limitation of size:** A class $C$ is proper if and only if there is a class bijection between $C$ and the universe.

This elegant axiom is essentially due to von Neumann. A class bijection is a class of ordered pairs; there might be pathology here if we did not have enough pairs as sets, but other axioms do provide for their existence. It is interesting to observe that this axiom implies Replacement (a class which is the same size as a set cannot be the same size as the universe) and, surprisingly, implies Choice (the von Neumann ordinals make up a proper class essentially by the Burali-Forti paradox, so the universe must be the same size as the class of ordinals, and the class bijection between the universe and the ordinals allows us to define a global well-ordering of the universe, whose existence immediately implies Choice).

Although Class Comprehension and Limitation of Size appear to tell us exactly what classes there are and what sets there are, more axioms are required to make our universe large enough. These can be taken to be the axioms of *Z* (other than extensionality and choice, which are not needed): the sethood of pairs of sets, unions of sets, power sets of sets, and the existence of an infinite set are enough to give us the world of *ZFC*. Foundation is usually added. The resulting theory is a conservative extension of *ZFC*: it proves all the theorems of *ZFC* about sets, and it does not prove any theorem about sets which is not provable in *ZFC*. For those with qualms about choice (or about global choice), Limitation of Size can be restricted to merely assert that the image of a set under a class function is a set.

We have two comments about this. First, the mental furniture of set theorists does seem to include proper classes, though usually it is important to them that all talk of proper classes can be explained away (the proper classes are in some sense “virtual”). Second, this theory (especially the version with the strong axiom of Limitation of Size) seems to capture the intuition of Cantor about the Absolute Infinite.

A stronger theory with classes, but still essentially a version of standard set theory, is the Kelley-Morse set theory in which Class Comprehension is strengthened to allow quantification over all classes in the formulas defining classes. Kelley-Morse set theory is not finitely axiomatizable, and it is stronger than *ZFC* in the sense that it allows a proof of the consistency of *ZFC*.

### 5.2 Ackermann set theory

The next theory we present was actually embedded in the set theoretical proposals of Paul Finsler, which were (taken as a whole) incoherent (see the notes on Finsler set theory available in the Other Internet Resources). Ackermann later (and apparently independently) presented it again. It is to all appearances a different theory from the standard one (it is our first genuine “alternative set theory”) but it turns out to be essentially the same theory as *ZF* (and choice can be added to make it essentially the same as *ZFC*).

Ackermann set theory is a theory of *classes* in which some classes are *sets*, but there is no simple definition of which classes are sets (in fact, the whole power of the theory is that the notion of set is indefinable!)

All objects are classes. The primitive notions are equality, membership and sethood. The axioms are

**Axiom of extensionality:** Classes with the same elements are equal.

**Axiom of class comprehension:** For any formula *φ*, there is a class $\{x \in V \mid \phi(x)\}$ whose elements are exactly the sets $x$ such that $\phi(x) (V$ here denotes the class of all sets). [But note that it is not the case here that all elements of classes are sets].

**Axiom of elements:** Any element of a set is a set.

**Axiom of subsets:** Any subset of a set is a set.

**Axiom of set comprehension:** For any formula $\phi (x)$ which does not mention the sethood predicate and in which all free variables other than $x$ denote sets, and which further has the property that $\phi(x)$ is only true of sets $x$, the class $\{x \mid \phi \}$ (which exists by Class Comprehension since all suitable $x$ are sets) is a set.

One can conveniently add axioms of Foundation and Choice to this system.

To see the point (mainly, to understand what Set Comprehension says) it is a good idea to go through some derivations.

The formula $x = a \lor x = b$ (where $a$ and $b$ are sets) does not mention sethood, has only the sets $a$ and $b$ as parameters, and is true only of sets. Thus it defines a set, and Pairing is true for sets.

The formula $\exists y(x \in y \amp y \in a)$, where $a$ is a set, does not mention sethood, has only the set $a$ as a parameter, and is true only of sets by the Axiom of Elements (any witness $y$ belongs to the set $a$, so $y$ is a set, and $x$ belongs to the set $y$, so $x$ is a set). Thus Union is true for sets.

The formula $\forall y(y \in x \rightarrow y \in a)$, where $a$ is a set, does not mention sethood, has only the set $a$ as a parameter, and is true only of sets by the Axiom of Subsets. Thus Power Set is true for sets.

The big surprise is that this system proves Infinity. The formula $x \ne x$ clearly defines a set, the empty set $\varnothing$. Consider the formula

$$ \forall I\left[\varnothing \in I \amp \forall y(y \in I \rightarrow y\cup \{y\} \in I) \rightarrow x \in I\right] $$

This formula does not mention sethood and has no parameters (or just the set parameter $\varnothing)$. The class $V$ of all sets has $\varnothing$ as a member and contains $y \cup \{y\}$ if it contains $y$ by Pairing and Union for sets (already shown). Thus any $x$ satisfying this formula is a set, whence the extension of the formula is a set (clearly the usual set of von Neumann natural numbers). So Infinity is true in the sets of Ackermann set theory.

It is possible (but harder) to prove Replacement as well in the realm of well-founded sets (which can be the entire universe of sets if Foundation for classes is added as an axiom). It is demonstrable that the theorems of Ackermann set theory about well-founded sets are exactly the theorems of *ZF* (Lévy 1959; Reinhardt 1970)[^lévy-1959][^reinhardt-1970].

We attempt to motivate this theory (in terms of the cumulative hierarchy). Think of classes as collections which merely exist potentially. The sets are those classes which actually get constructed. Extensionality for classes seems unproblematic. All collections of the actual sets could have been constructed by constructing one more stage of the cumulative hierarchy: this justifies class comprehension. Elements of actual sets are actual sets; subcollections of actual sets are actual sets; these do not seem problematic. Finally, we assert that any collection of classes which is defined without reference to the realm of actual sets, which is defined in terms of specific objects which are actual, and which turns out only to contain actual elements is actual. When one gets one’s mind around this last assertion, it can seem reasonable. A particular thing to note about such a definition is that it is “absolute”: the collection of all actual sets is a proper class and not itself an actual set, because we are not committed to stopping the construction of actual sets at any particular point; but the elements of a collection satisfying the conditions of set comprehension do not depend on how many potential collections we make actual (this is why the actuality predicate is not allowed to appear in the “defining” formula).

It may be a minority opinion, but we believe (after some contemplation) that the Ackermann axioms have their own distinctive philosophical motivation which deserves consideration, particularly since it turns out to yield basically the same theory as *ZF* from an apparently quite different starting point.

Ackermann set theory actually proves that there are classes which have non-set classes as elements; the difference between sets and classes provably cannot be as in von Neumann-Gödel-Bernays class theory. A quick proof of this concerns ordinals. There is a proper class von Neumann ordinal $\Omega$, the class of all set von Neumann ordinals. We can prove the existence of $\Omega + 1$ using set comprehension: if $\Omega$ were the last ordinal, then “$x$ is a von Neumann ordinal with a successor” would be a predicate not mentioning sethood, with no parameters (so all parameters sets), and true only of sets. But this would make the class of all set ordinals a set, and the class of all set ordinals is $\Omega$ itself, which would lead to the Burali-Forti paradox. So $\Omega + 1$ must exist, and is a proper class with the proper class $\Omega$ as an element.

There is a meta-theorem of *ZF* called the Reflection Principle which asserts that any first-order assertion which is true of the universe $V$ is also true of some set. This means that for any particular proof in *ZF*, there is a set $M$ which might as well be the universe (because any proof uses only finitely many axioms). A suitable such set $M$ can be construed as the universe of sets and the actual universe $V$ can be construed as the universe of classes. The set $M$ has the closure properties asserted in Elements and Subsets if it is a limit rank; it can be chosen to have as many of the closure properties asserted in Set Comprehension (translated into terms of $M)$ as a proof in Ackermann set theory requires. This machinery is what is used to show that Ackermann set theory proves nothing about sets that *ZF* cannot prove: one translates a proof in Ackermann set theory into a proof in *ZFC* using the Reflection Principle.

## 6. New Foundations and Related Systems

### 6.1 The definition of *NF*

We have alluded already to the fact that the simple typed theory of sets *TST* can be shown to be equivalent to an untyped theory (Mac Lane set theory, aka bounded Zermelo set theory). We briefly indicate how to do this: choose any map $f$ in the model which is an injection with domain the set of singletons of type 0 objects and range included in type 1 (the identity on singletons of type 0 objects is an example). Identify each type 0 object $x^0$ with the type 1 object $f (\{x^0\})$; then introduce exactly those identifications between objects of different types which are required by extensionality: every type 0 object is identified with a type 1 object, and an easy meta-induction shows that every type $n$ object is identified with some type $n + 1$ object. The resulting structure will satisfy all the axioms of Zermelo set theory except Separation, and will satisfy all instances of Separation in which each quantifier is bounded in a set (this boundedness comes in because each instance of Comprehension in *TST* has each quantifier bounded in a type, which becomes a bounding set for that quantifier in the interpretation of Mac Lane set theory). It will satisfy Infinity and Choice if the original model of *TST* satisfies these axioms. The simplest map $f$ is just the identity on singletons of type 0 objects, which will have the effect of identifying each type 0 object with its own singleton (a failure of foundation). It can be arranged for the structure to satisfy Foundation: for example, if Choice holds type 0 can be well-ordered and each element of type 0 identified with the corresponding segment in the well-ordering, so that type 0 becomes a von Neumann ordinal. (A structure of this kind will never model Replacement, as there will be a countable sequence of cardinals [the cardinalities of the types] which is definable and cofinal below the cardinality of the universe.) See Mathias 2001a for a full account.

Quine’s set theory New Foundations (abbreviated *NF*, proposed in 1937 in his paper “New Foundations for Mathematical Logic”), is also based on a procedure for identifying the objects in successive types in order to obtain an untyped theory. However, in the case of *NF* and related theories, the idea is to identify the entirety of type $n + 1$ with type $n$; the type hierarchy is to be collapsed completely. An obvious difficulty with this is that Cantor’s theorem suggests that type $n + 1$ (being the “power set” of type $n)$ should be intrinsically larger than type $n$ (and in some senses this is demonstrably true).

We first outline the reason that Quine believed that it might be possible to collapse the type hierarchy. We recall from above:

> We admit sorts of object indexed by the natural numbers (this is purely a typographical convenience; no actual reference to natural numbers is involved). Type 0 is inhabited by “individuals” with no specified structure. Type 1 is inhabited by sets of type 0 objects, and in general type $n + 1$ is inhabited by sets of type $n$ objects.

The type system is enforced by the grammar of the language. Atomic sentences are equations or membership statements, and they are only well-formed if they take one of the forms $x^{n} = y^{n}$ or $x^{n} \in y^{n+1}$.

The axioms of extensionality of *TST* take the form

$$ A^{n+1} = B^{n+1} \leftrightarrow \forall x^n (x^n \in A^{n+1} \leftrightarrow x^n \in B^{n+1}); $$

there is a separate axiom for each $n$.

The axioms of comprehension of *TST* take the form (for any choice of a type $n$, a formula *φ*, and a variable $A^{n+1}$ not free in $\phi)$

$$ \exists A^{n+1}\forall x^n (x^n \in A^{n+1} \leftrightarrow \phi) $$

It is interesting to observe that the axioms of *TST* are precisely analogous to those of naive set theory.

For any formula *φ*, define $\phi^+$ as the formula obtained by raising every type index on a variable in *φ* by one. Quine observes that any proof of *φ* can be converted into a proof of $\phi^+$ by raising all type indices in the original proof. Further, every object $\{x^n \mid \phi \}^{n+1}$ that the theory permits us to define has a precise analogue $\{x^{n+1} \mid \phi^{+}\}^{n+2}$ in the next higher type; this can be iterated to produce “copies” of any defined object in each higher type.

For example, the Frege definition of the natural numbers works in *TST*. The number $3^2$ can be defined as the (type 2) set of all (type 1) sets with three (type 0) elements. The number $3^3$ can be defined as the (type 3) set of all (type 2) sets with three (type 1) elements. The number $3^{27}$ can be defined as the (type 27) set of all (type 26) sets with three (type 25) elements. And so forth. Our logic does not even permit us to say that these are a sequence of distinct objects; we cannot ask the question as to whether they are equal or not.

Quine suggested, in effect, that we tentatively suppose that $\phi \equiv \phi^+$ for all *φ* ; it is not just the case that if we can prove *φ*, we can prove $\phi^+$, but that the truth values of these sentences are the same. It then becomes strongly tempting to identify $\{x^n \mid \phi \}^{n+1}$ with $\{x^{n+1} \mid \phi^{+}\}^{n+2}$, since anything we can say about these two objects is the same (and our new assumption implies that we will assign the same truth values to corresponding assertions about these two objects).

The theory *NF* which we obtain can be described briefly (but deceptively) as being the first-order untyped theory with equality and membership having the same axioms as *TST* but without the distinctions of type. If this is not read very carefully, it may be seen as implying that we have adopted the comprehension axioms of naive set theory,

$$ \exists A\forall x(x \in A \leftrightarrow \phi) $$

for each formula *φ*. But we have not. We have only adopted those axioms for formulas *φ* which can be obtained from formulas of *TST* by dropping distinctions of type between the variables (without introducing any identifications between variables of different types). For example, there is no way that $x \not\in x$ can be obtained by dropping distinctions of type from a formula of *TST*, without identifying two variables of different type. Formulas of the untyped language of set theory in which it is possible to assign a type to each variable (the same type wherever it occurs) in such a way as to get a formula of *TST* are said to be *stratified*. The axioms of *NF* are strong extensionality (no non-sets) and stratified comprehension.

Though the set $\{x \mid x \not\in x\}$ is not provided by stratified comprehension, some other sets which are not found in any variant of Zermelo set theory are provided. For example, $x = x$ is a stratified formula, and the universal set $V = \{x \mid x = x\}$ is provided by an instance of comprehension. Moreover, $V \in V$ is true.

All mathematical constructions which can be carried out in *TST* can be carried out in *NF*. For example, the Frege natural numbers can be constructed, and so can the set $\mathbf{N}$ of Frege natural numbers. For example, the Frege natural number 1, the set of *all* one-element sets, is provided by *NF*.

### 6.2 The consistency problem for *NF*; the known consistent subsystems

No contradictions are known to follow from *NF*, but some uncomfortable consequences do follow. The Axiom of Choice is known to fail in *NF*: Specker (1953)[^specker-1953] proved that the universe cannot be well-ordered. (Since the universe cannot be well-ordered, it follows that the “Axiom” of Infinity is a theorem of *NF*: if the universe were finite, it could be well-ordered.) This might be thought to be what one would expect on adopting such a dangerous comprehension scheme, but this turns out not to be the problem. The problem is with extensionality.

Jensen (1968)[^jensen-1968] showed that *NFU* (New Foundations with urelements), the version of New Foundations in which extensionality is weakened to allow many non-sets (as described above under naive set theory) is consistent, is consistent with Infinity and Choice, and is also consistent with the negation of Infinity (which of course implies Choice). *NFU*, which has the full stratified comprehension axiom of *NF* with all its frighteningly big sets, is weaker in consistency strength than Peano arithmetic; *NFU* + Infinity + Choice is of the same strength as *TST* with Infinity and Choice or Mac Lane set theory.

Some other fragments of *NF*, obtained by weakening comprehension rather than extensionality, are known to be consistent. *NF*₃, the version of *NF* in which one accepts only those instances of the axiom of comprehension which can be typed using three types, was shown to be consistent by Grishin (1969)[^grishin-1969].

*NFP* (predicative *NF*), the version of *NF* in which one accepts only instances of the axiom of comprehension which can be typed so as to be instances of comprehension of predicative *TST* (described above under type theories) was shown to be consistent by Marcel Crabbé (1982)[^crabbé-1982]. He also demonstrated the consistency of the theory *NFI* in which one allows all instances of stratified comprehension in which no variable appears of type higher than that assigned to the set being defined (bound variables of the same type as that of the set being defined are permitted, which allows some impredicativity). One would like to read the name *NFI* as “impredicative *NF*” but one cannot, as it is more impredicative than *NFP*, not more impredicative than *NF* itself.

*NF*₃+Infinity has the same strength as second-order arithmetic. So does *NFI* (which has just enough impredicativity to define the natural numbers, and not enough for the Least Upper Bound Axiom). *NFP* is equivalent to a weaker fragment of arithmetic, but does (unlike *NFU*) prove Infinity: this is the only application of the Specker proof of the negation of the Axiom of Choice to a provably consistent theory. Either Union is true (in which case we readily get all of *NF* and Specker’s proof of Infinity goes through) or Union is not true, in which case we note that all finite sets have unions, so there must be an infinite set. *NF*₃ has considerable interest for a surprising reason: it turns out that *all* infinite models of *TST*₃ (simple type theory with three types) satisfy the ambiguity schema $\phi \equiv \phi^+$ (of course this only makes sense for formulas with one or two types) and this turns out to be enough to show that for any infinite model of *TST*₃ there is a model of *NF*₃ with the same theory. *NF*₄ is the same theory as *NF* (Grishin 1969)[^grishin-1969], and we have no idea how to get a model of *TST*₄ to satisfy ambiguity.

Very recently, Sergei Tupailo (2010)[^tupailo-2010] has proved the consistency of *NFSI*, the fragment of *NF* consisting of extensionality and those instances of Comprehension ($\{x \in A \mid \phi \}$ exists) which are stratified and in which the variable $x$ is assigned the lowest type. Tupailo’s proof is highly technical, but Marcel Crabbé pointed out that a structure for the language of set theory in which the sets are exactly the finite and cofinite collections satisfies this theory (so it is very weak). It should be noted that Tupailo’s model of *NFSI* satisfies additional propositions of interest not satisfied by the very simple model of Crabbé, such as the existence of each Frege natural number. It is of some interest whether this new fragment represents an independent way of getting a consistent fragment of *NF*. Note that *NFU*+*NFSI* is *NF* because *NFSI* has strong extensionality. Also, *NFP*+*NFSI* is *NF* because *NFSI* includes Union. The relationship of *NFSI* to *NF*$_3$ has been clarified by Marcel Crabbé in 2016. Tupailo’s theory is shown not to be a fragment of Grishin’s, and thus represents a fourth known method of getting consistent fragments.

### 6.3 Mathematics in *NFU* + Infinity + Choice

Of these set theories, only *NFU* with Infinity, Choice and possibly further strong axioms of infinity (of which more anon) is really mathematically serviceable. We examine the construction of models of this theory and the way mathematics works inside this theory. A source for this development is Holmes 1998. Rosser 1973 develops the foundations of mathematics in *NF*: it can adapted to *NFU* fairly easily).

A model of *NFU* can be constructed as follows. Well-known results of model theory allow the construction of a nonstandard model of *ZFC* (actually, a model of Mac Lane set theory suffices) with an external automorphism $j$ which moves a rank $V_{\alpha}$. We stipulate without loss of generality that $j(\alpha) \lt \alpha$. The universe of our model of *NFU* will be $V_{\alpha}$ and the membership relation will be defined as

$$ x \in_{NFU} y \equiv_{def} j(x) \in y \amp y \in V_{j(\alpha)+1} $$

(where $\in$ is the membership relation of the nonstandard model). The proof that this is a model of *NFU* is not long, but it is involved enough that we refer the reader elsewhere. The basic idea is that the automorphism allows us to code the (apparent) power set $V_{\alpha +1}$ of our universe $V_{\alpha}$ into the “smaller” $V_{j(\alpha)+1}$ which is included in our universe; the left over objects in $V_{\alpha} - V_{j(\alpha)+1}$ become urelements. Note that $V_{\alpha} - V_{j(\alpha)+1}$ is most of the domain of the model of *NFU* in a quite strong sense: almost all of the universe is made up of urelements (note that each $V_{\beta +1}$ is the power set of $V_{\beta}$, and so is strictly larger in size, and not one but many stages intervene between $V_{j(\alpha)+1}$ (the collection of “sets”) and $V_{\alpha}$ (the “universe”)). This construction is related to the construction used by Jensen, but is apparently first described explicitly in Boffa 1988.

In any model of *NFU*, a structure which looks just like one of these models can be constructed in the isomorphism classes of well-founded extensional relations. The theory of isomorphism classes of well-founded extensional relations with a top element looks like the theory of (an initial segment of) the usual cumulative hierarchy, because every set in Zermelo-style set theory is uniquely determined by the isomorphism type of the restriction of the membership relation to its transitive closure. The surprise is that we not only see a structure which looks like an initial segment of the cumulative hierarchy: we also see an external endomorphism of this structure which moves a rank (and therefore cannot be a set), in terms of which we can replicate the model construction above and get an interpretation of *NFU* of this kind inside *NFU*! The endomorphism is induced by the map $T$ which sends the isomorphism type of a relation $R$ to the isomorphism type of $R^{\iota} = \{ \langle \{x\}, \{y\}\rangle \mid xRy\}$. There is no reason to believe that $T$ is a function: it sends any relation $R$ to a relation $R^{\iota}$ which is one type higher in terms of *TST*. It is demonstrable that $T$ on the isomorphism types of well-founded extensional relations is not a set function (we will not show this here, but our discussion of the Burali-Forti paradox below should give a good idea of the reasons for this). See Holmes (1998)[^holmes-1998] for the full discussion.

This suggests that the underlying world view of *NFU*, in spite of the presence of the universal set, Frege natural numbers, and other large objects, may not be that different from the world view of Zermelo-style set theory; we build models of *NFU* in a certain way in Zermelo-style set theory, and *NFU* itself reflects this kind of construction internally. A further, surprising result (Holmes 2012)[^holmes-2012] is that in models of *NFU* constructed from a nonstandard $V_{\alpha}$ with automorphism as above, the membership relation on the nonstandard $V_{\alpha}$ is first-order definable (in a very elaborate way) in terms of the relation $\in_{NFU}$; this is very surprising, since it seems superficially as if all information about the extensions of the urelements has been discarded in this construction. But this turns out not to be the case (and this means that the urelements, which seem to have no internal information, nonetheless have a great deal of structure in these models).

Models of *NFU* can have a “finite” (but externally infinite) universe if the ordinal *α* in the construction is a nonstandard natural number. If *α* is infinite, the model of *NFU* will satisfy Infinity. If the Axiom of Choice holds in the model of Zermelo-style set theory, it will hold in the model of *NFU*.

Now we look at the mathematical universe according to *NFU*, rather than looking at models of *NFU* from the outside.

The Frege construction of the natural numbers works perfectly in *NFU*. If Infinity holds, there will be no last natural number and we can define the usual set $\mathbf{N}$ of natural numbers just as we did above.

Any of the usual ordered pair constructions works in *NFU*. The usual Kuratowski pair is inconvenient in *NF* or in *NFU*, because the pair is two types higher than its projections in terms of *TST*. This means that functions and relations are three types higher than the elements of their domains and ranges. There is a type-level pair defined by Quine (1945; type-level because it is the same type as its projections) which is definable in *NF* and also on $V_{\alpha}$ for any infinite ordinal *α*; this pair can be defined and used in *NF* and the fact that it is definable on infinite $V_{\alpha}$ means that it can be assumed in *NFU*+Infinity that there is a type-level ordered pair (the existence of such a pair also follows from Infinity and Choice together). This would make the type displacement between functions and relations and elements of their domains and ranges just one, the same as the displacement between the types of sets and their elements. We will assume that ordered pairs are of the same type as their projections in the sequel, but we will not present the rather complicated definition of the Quine pair.

Once pairs are defined, the definition of relations and functions proceeds exactly as in the usual set theory. The definitions of integers and rational numbers present no problem, and the Dedekind construction of the reals can be carried out as usual. We will focus here on developing the solutions to the paradoxes of Cantor and Burali-Forti in *NFU*, which give a good picture of the odd character of this set theory, and also set things up nicely for a brief discussion of natural strong axioms of infinity for *NFU*. It is important to realize as we read the ways in which *NFU* evades the paradoxes that this evasion is successful: *NFU* is known to be consistent if the usual set theory is consistent, and close examination of the models of *NFU* shows exactly why these apparent dodges work.

Two sets are said to be of the same cardinality just in case there is a bijection between them. This is standard. But we then proceed to define $|A|$ (the cardinality of a set $A)$ as the set of all sets which are the same size as $A$, realizing the definition intended by Frege and Russell, and apparently intended by Cantor as well. Notice that $|A|$ is one type higher than $A$. The Frege natural numbers are the same objects as the finite cardinal numbers.

The Cantor theorem of the usual set theory asserts that $|A| \lt |\wp(A)|$. This is clearly not true in *NFU*, since | $V|$ is the cardinality of the universe and $|\wp(V)|$ is the cardinality of the set of sets, and in fact $|V| \gt \gt |\wp(V)|$ in all known models of *NFU* (there are many intervening cardinals in all such models). But $|A| \lt |\wp(A)|$ does not make sense in *TST*: it is ill-typed. The correct theorem in *TST*, which is inherited by *NFU*, is $|\wp_1 (A)| \lt |\wp(A)|$, where $\wp_1 (A)$ is the set of one-element subsets of $A$, which is at the same type as the power set of $A$. So we have $|\wp_1 (V)| \lt |\wp(V)|$: there are more sets than there are singleton sets. The apparent bijection $x \mapsto \{x\}$ between $\wp_1 (V)$ and $V$ cannot be a set (and there is no reason to expect it to be a set, since it has an unstratified definition).

A set which satisfies $|A| = |\wp_1 (A)|$ is called a *cantorian* set, since it satisfies the usual form of Cantor’s theorem. A set $A$ which satisfies the stronger condition that the restriction of the singleton map to $A$ is a set is said to be *strongly cantorian* (s.c.). Strongly cantorian sets are important because it is not necessary to assign a relative type to a variable known to be restricted to a strongly cantorian set, as it is possible to use the restriction of the singleton map and its inverse to freely adjust the type of any such variable for purposes of stratification. The strongly cantorian sets are can be thought of as analogues of the *small* sets of the usual set theory.

Ordinal numbers are defined as equivalence classes of well-orderings under similarity. There is a natural order on ordinal numbers, and in *NFU* as in the usual set theory it turns out to be a well-ordering—and, as in naive set theory, a set! Since the natural order on the ordinal numbers is a set, it has an order type $\Omega$ which is itself one of the ordinal numbers. Now in the usual set theory we prove that the order type of the restriction of the natural order on the ordinals to the ordinals less than *α* is the ordinal *α* itself; however, this is an ill-typed statement in *TST*, where, assuming a type level ordered pair, the second occurrence of *α* is two types higher than the first (it would be four types higher if the Kuratowski ordered pair were used). Since the ordinals are isomorphism types of relations, we can define the operation $T$ on them as above.

> The order type of the restriction of the natural order on the ordinals to the ordinals less than *α* is the ordinal $T^2 (\alpha)$

is an assertion which makes sense in *TST* and is in fact true in *TST* and so in *NFU*. We thus find that the order type of the restriction of the natural order on the ordinals to the ordinals less than $\Omega$ is $T^2 (\Omega)$, whence we find that $T^2 (\Omega)$ (as the order type of a proper initial segment of the ordinals) is strictly less than $\Omega$ (which is the order type of *all* the ordinals). Once again, the fact that the singleton map is not a function eliminates the “intuitively obvious” similarity between these orders. This also shows that $T$ is not a function. $T$ is an order endomorphism of the ordinals, though, whence we have $\Omega \gt T^2 (\Omega) \gt T^4 (\Omega)\ldots$, which may be vaguely disturbing, though this “sequence” is not a set. A perhaps useful comment is that in the models of *NFU* described above, the action of $T$ on ordinals exactly parallels the action of $j$ on order types of well-orderings $(j$ does not send *NFU* ordinals to ordinals, exactly, so this needs to be phrased carefully): the “descending sequence” already has an analogue in the sequence $\alpha \gt j(\alpha) \gt j^2 (\alpha)\ldots$ in the original nonstandard model. Some have asserted that this phenomenon (that the ordinals in any model of *NFU* are not externally well-ordered) can be phrased as “*NFU* has no standard model”. We reserve judgement on this—we do note that the theorem “the ordinals in any (set!) model of *NFU* are not well-ordered” is a theorem of *NFU* itself; note that *NFU* does not see the universe as a model of *NFU* (even though it is a set) because the membership relation is not a set relation (if it were, the singleton map certainly would be).

*NFU* + Infinity + Choice is a relatively weak theory: like Zermelo set theory it does not prove even that $\aleph_{\omega}$ exists. As is the case with Zermelo set theory, natural extensions of this theory make it much stronger. We give just one example. The Axiom of Cantorian Sets is the deceptively simple statement (to which there are no evident counterexamples) that “every cantorian set is strongly cantorian”. *NFU* + Infinity + Choice + Cantorian Sets is a considerably stronger theory than *NFU* + Infinity + Choice: in its theory of isomorphism types of well-founded extensional relations with top element, the cantorian types with the obvious “membership” relation satisfy the axioms of *ZFC* + “there is an $n$-Mahlo cardinal” for each concrete $n$. There is no mathematical need for the devious interpretation: this theory proves the existence of $n$-Mahlo cardinals and supports all mathematical constructions at that level of consistency strength in its own terms without any need to refer to the theory of well-founded extensional relations. More elaborate statements about such properties as “cantorian” and “strongly cantorian” (applied to order types as well as cardinality) yield even stronger axioms of infinity.

Our basic claim about *NFU* + Infinity + Choice (and its extensions) is that it is a mathematically serviceable alternative set theory with its own intrinsic motivation (although we have used Zermelo style set theory to prove its consistency here, the entire development can be carried out in terms of *TST* alone: one can use *TST* as meta-theory, show in *TST* that consistency of *TST* implies consistency of *NFU*, and use this result to amend one’s meta-theory to *NFU*, thus abandoning the distinctions between types). We do not claim that it is better than *ZFC*, but we do claim that it is adequate, and that it is important to know that adequate alternatives exist; we do claim that it is useful to know that there are different ways to found mathematics, as we have encountered the absurd assertion that “mathematics is whatever is formalized in *ZFC*”.

### 6.4 Critique of *NFU*

Like Zermelo set theory, *NFU* has advantages and disadvantages. An advantage, which corresponds to one of the few clear disadvantages of Zermelo set theory, is that it is possible to define natural numbers, cardinal numbers, and ordinal numbers in the natural way intended by Frege, Russell, and Whitehead.

Many but not all of the purported disadvantages of *NFU* as a working foundation for mathematics reduce to complaints by mathematicians used to working in *ZFC* that “this is not what we are used to”. The fact that there are fewer singletons than objects (in spite of an obvious external one to one correspondence) takes getting used to. In otherwise familiar constructions, one sometimes has to make technical use of the singleton map or $T$ operations to adjust types to get stratification. This author can testify that it is perfectly possible to develop good intuition for *NFU* and work effectively with stratified comprehension; part of this but not all of it is a good familiarity with how things are done in *TST*, as one also has to develop a feel for how to use principles that subvert stratification.

As Sol Feferman has pointed out, one place where the treatments in *NFU* (at least those given so far) are clearly quite involved are situations in which one needs to work with indexed families of objects. The proof of König’s Lemma of set theory in Holmes 1998 is a good example of how complicated this kind of thing can get in *NFU*. We have a notion that the use of sets of “Quine atoms” (self-singletons) as index sets (necessarily for s.c. sets) might relieve this difficulty, but we haven’t proved this in practice, and problems would remain for the noncantorian situation.

The fact that “*NFU* has no standard models” (the ordinals are not well-ordered in any set model of *NFU*) is a criticism of *NFU* which has merit. We observe, though, that there are other set theories in which nonstandard objects are deliberately provided (we will review some of these below), and some of the applications of those set theories to “nonstandard analysis” might be duplicated in suitable versions of *NFU*. We also observe that strong principles which minimize the nonstandard behavior of the ordinals turn out to give surprisingly strong axioms of infinity in *NFU*; the nonstandard structure of the ordinals allows insight into phenomena associated with large cardinals.

Some have thought that the fact that *NFU* combines a universal set and other big structures with mathematical fluency in treating these structures might make it a suitable medium for category theory. Although we have some inclination to be partial to this class of set theories, we note that there are strong counterarguments to this view. It is true that there are big categories, such as the category of all sets (as objects) and functions (as the morphisms between them), the category of all topological spaces and homeomorphism, and even the category of all categories and functors. However, the category of all sets and functions, for example, while it is a set, is not “cartesian closed” (a technical property which this category is expected to have): see McLarty 1992. Moreover, if one restricts to the s.c. sets and functions, one obtains a cartesian closed category, which is much more closely analogous to the category of all sets and functions over *ZFC*—and shares with it the disadvantage of being a proper class! Contemplation of the models only confirms the impression that the correct analogue of the proper class category of sets and functions in *ZFC* is the proper class category of s.c. sets and functions in *NFU*! There may be some applications for the big set categories in *NFU*, but they are not likely to prove to be as useful as some have optimistically suggested. See Feferman 2006 for an extensive discussion.

An important point is that there is a relativity of viewpoint here: the *NFU* world can be understood to be a nonstandard initial segment of the world of *ZFC* (which could be arranged to include its entire standard part!) with an automorphism and the *ZFC* world (or an initial segment of it) can be interpreted in *NFU* as the theory of isomorphism classes of well-founded extensional relations with top (often restricted to its strongly cantorian part); these two theories are mutually interpretable, so the corresponding views of the world admit mutual translation.

*ZFC* might be viewed as motivated by a generalization of the theory of sets in extension (as generalizations of the notion of finite set, replacing the finite with the transfinite and the rejected infinite with the rejected Absolute Infinite of Cantor) while the motivation of *NFU* can be seen as a correction of the theory of sets as intensions (that is, as determined by predicates) which led to the disaster of naive set theory. Nino Cocchiarella (1985)[^cocchiarella-1985] has noted that Frege’s theory of concepts could be saved if one could motivate a restriction to stratified concepts (the abandonment of strong extensionality is merely a return to common sense). But the impression of a fundamental contrast should be tempered by the observation that the two theories nonetheless seem to be looking at the same universe in different ways!

## 7. Positive Set Theories

### 7.1 Topological motivation of positive set theory

We will not attempt an exhaustive survey of positive set theory; our aim here is to motivate and exhibit the axioms of the strongest system of this kind familiar to us, which is the third of the systems of classical set theory which we regard as genuinely mathematically serviceable (the other two being *ZFC* and suitable strong extensions of *NFU* + Infinity + Choice).

A *positive formula* is a formula which belongs to the smallest class of formulas containing a false statement $\bot$, all atomic membership and equality formulas and closed under the formation of conjunctions, disjunctions, universal and existential quantifications. A *generalized positive formula* is obtained if we allow *bounded* universal and existential quantifications (the additional strength comes from allowing $(\forall x \in A \mid \phi) \equiv \forall x(x \in A \rightarrow \phi)$; bounded existential quantification is positive in any case).

Positive comprehension is motivated superficially by an attack on one of the elements of Russell’s paradox (the negation): a positive set theory will be expected to support the axiom of extensionality (as usual) and the axiom of *(generalized) positive comprehension*: for any (generalized) positive formula $\phi , \{x \mid \phi \}$ exists.

We mention that we are aware that positive comprehension with the additional generalization of positive formulas allowing one to include set abstracts $\{x \mid \phi \}$ (with *φ* generalized positive) in generalized positive formulas is consistent, but turns out not to be consistent with extensionality. We are not very familiar with this theory, so have no additional comments to make about it; do notice that the translations of formulas with set abstracts in them into first order logic without abstracts are definitely not positive in our more restricted sense, and so one may expect some kind of trouble!

The motivation for the kinds of positive set theory we are familiar with is *topological*. We are to understand the sets as closed sets under some topology. Finite unions and intersections of closed sets are closed; this supports the inclusion of $\{x \mid \phi \lor \psi \}$ and $\{x \mid \phi \amp \psi \}$ as sets if $\{x \mid \phi \}$ and $\{x \mid \psi \}$ are sets. Arbitrary intersections of closed sets are closed: this supports our adoption of even bounded universal quantification (if each $\{x \mid \phi(y)\}$ is a set, then $\{x \mid \forall y\phi(y)\}$ is the intersection of all of these sets, and so should be closed, and $\{x \in A \mid \forall y\phi(y)\}$ is also an intersection of closed sets and so should be closed. The motivation for permitting $\{x \mid \exists y\phi(y)\}$ when each $\{x \mid \phi(y)\}$ exists is more subtle, since infinite unions do not as a rule preserve closedness: the idea is that the set of pairs $(x, y)$ such that $\phi(x, y)$ is closed, and the topology is such that the projection of a closed set is closed. Compactness of the topology suffices. Moreover, we now need to be aware that formulas with several parameters need to be considered in terms of a product topology.

An additional very powerful principle should be expected to hold in a topological model: for any class $C$ whatsoever (any collection of sets), the intersection of all sets which include $C$ as a subclass should be a set. Every class has a set closure.

We attempt the construction of a model of such a topological theory. To bring out an analogy with Mac Lane set theory and *NF*, we initially present a model built by collapsing *TST* in yet another manner.

The model of *TST* that we use contains one type 0 object $u$. Note that this means that each type is finite. Objects of each type are construed as better and better approximations to the untyped objects of the final set theory. $u$ approximates any set. The type $n + 1$ approximant to any set $A$ is intended to be the set of type $n$ approximants of the elements of $A$.

This means that we should be able to specify when a type $n + 2$ set $A^{n+2}$ refines a type $n + 1$ set $A^{n+1}$: each (type $n + 1)$ element of $A^{n+2}$ should refine a (type $n)$ element of $A^{n+1}$, and each element of $A^{n+1}$ should be refined by one or more elements of $A^{n+2}$. Along with the information that the type 0 object $u$ refines both of the elements of type 1, this gives a complete recursive definition of the notion of refinement of a type $n$ set by a type $n + 1$ set. Each type $n + 1$ set refines a unique type $n$ set but may be refined by many type $n + 2$ sets. (The “hereditarily finite” sets without $u$ in their transitive closure are refined by just one precisely analogous set at the next higher level.) Define a general relation $x \sim y$ on all elements of the model of set theory as holding when $x = y$ (if they are of the same type) or if there is a chain of refinements leading from the one of $x, y$ of lower type to the one of higher type.

The objects of our first model of positive set theory are sequences $s_n$ with each $s_n$ a type $n$ set and with $s_{n+1}$ refining $s_n$ for each $n$. We say that $s \in t$ when $s_{n} \in t_{n+1}$ for all $n$. It is straightforward to establish that if $s_{n} \in t_{n+1}$ or $s_{n} = t_{n}$ is false, then $s_k \in t_{k+1}$ or (respectively) $s_k = t_k$ is false for all $k \gt n$. More generally, if $s_m \sim t_n$ is false, then $s_{m+k} \sim t_{n+k}$ is false for all $k \ge 0$.

Formulas in the language of the typed theory with $\in$ and $\sim$ have a monotonicity property: if *φ* is a generalized positive formula and one of its typed versions is false, then any version of the same formula obtained by raising types and refining the values of free variables in the formula will continue to be false. It is not hard to see why this will fail to work if negation is allowed.

It is also not too hard to show that if all typed versions of a generalized positive formula *φ* in the language of the intended model (with sequences $s$ appearing as values of free variables replaced by their values at the appropriate types) are true, then the original formula *φ* is true in the intended model. The one difficulty comes in with existential quantification: the fact that one has a witness to $(\exists x.\phi(x))$ in each typed version does not immediately give a sequence witnessing this in the intended model. The tree property of *ω* helps here: only finitely many approximants to sets exist at each level, so one can at each level choose an approximant refinements of which are used at infinitely many higher levels as witnesses to $(\exists x.\phi(x))$, then restrict attention to refinements of that approximant; in this way one gets not an arbitrary sequence of witnesses at various types but a “convergent” sequence (an element of the intended model).

One then shows that any generalized positive formula $\phi(x)$ has an extension $\{x \mid \phi(x)\}$ by considering the sets of witnesses to $\phi(x)$ in each type $n$; these sets themselves can be used to construct a convergent sequence (with the proviso that some apparent elements found at any given stage may need to be discarded; one defines $s_{n+1}$ as the set of those type $n$ approximants which not only witness $\phi(x)$ at the current type $n$ but have refinements which witness $\phi(x)$ at each subsequent type. The sequence of sets $s$ obtained will be an element of the intended model and have the intended extension.

Finally, for any class of sequences (elements of the intended model) $C$, there is a smallest *set* which contains all elements of $C$: let $c_{n+1}$ be the set of terms $s_n$ of sequences $s$ belonging to $C$ at each type $n$ to construct a sequence $c$ which will have the desired property.

This theory can be made stronger by indicating how to pass to transfinite typed approximations. The type $\alpha + 1$ approximation to a set will always be the set of type *α* approximations; if *λ* is a limit ordinal, the type *λ* approximation will be the sequence $\{s_{\beta} \}_{\beta \lt \lambda}$ of approximants to the set at earlier levels (so our “intended model” above is the set of type *ω* approximations in a larger model).

Everything above will work at any limit stage except the treatment of the existential quantifier. The existential quantifier argument will work if the ordinal stage at which the model is being constructed is a weakly compact cardinal. This is a moderately strong large cardinal property (for an uncountable cardinal): it implies, for example, the existence of proper classes of inaccessibles and of $n$-Mahlo cardinals for each $n$.

So for each weakly compact cardinal *κ* (including $\kappa = \omega)$ the approximants of level *κ* in the transfinite type theory just outlined make up a model of set theory with extensionality, generalized positive comprehension, and the closure property. We will refer to this model as the “*κ*-hyperuniverse”.

### 7.2 The system *GPK*$^{+}_{\infty}$ of Olivier Esser

We now present an axiomatic theory which has the *κ*-hyperuniverses with $\kappa \gt \omega$ as (some of its) models. This is a first-order theory with equality and membership as primitive relations. This system is called *GPK*$^{+}_{\infty}$ and is described in Esser 1999.

**Extensionality:** Sets with the same elements are the same.

**Generalized Positive Comprehension:** For any generalized positive formula $\phi , \{x \mid \phi \}$ exists. (Notice that since we view the false formula $\bot$ as positive we need no special axiom asserting the existence of the empty set).

**Closure:** For any formula $\phi(x)$, there is a set $C$ such that $x \in C \equiv [\forall y\forall z(\phi(z) \rightarrow z \in y) \rightarrow x \in y$]; $C$ is the intersection of all sets which include all objects which satisfy $\phi : C$ is called the closure of the class $\{x \mid \phi(x)\}$.

**Infinity:** The closure of the von Neumann ordinals is not an element of itself. (This excludes the *ω*-hyperuniverse, in which the closure of the class of von Neumann ordinals has itself as an additional member).

As one might expect, some of the basic concepts of this set theory are topological (sets being the closed classes of the topology on the universe).

This set theory interprets *ZF*. This is shown by demonstrating first that the discrete sets (and more particularly the (closed) sets of isolated points in the topology) satisfy an analogue of Replacement (a definable function (defined by a formula which need not be positive) with a discrete domain is a set), and so an analogue of separation, then by showing that well-founded sets are isolated in the topology and the class of well-founded sets is closed under the constructions of *ZF*.

Not only *ZF* but also Kelley-Morse class theory can be interpreted; any definable class of well-founded sets has a closure whose well-founded members will be exactly the desired members (it will as a rule have other, non-well-founded members). Quantification over these “classes” defines sets just as easily as quantification over mere sets in this context; so we get an impredicative class theory. Further, one can prove internally to this theory that the “proper class ordinal” in the interpreted $KM$ has the tree property, and so is in effect a weakly compact cardinal; this shows that this theory has considerable consistency strength (for example, its version of *ZF* proves that there is a proper class of inaccessible cardinals, a proper class of $n$-Mahlos for each $n$, and so forth): the use of large cardinals in the outlined model construction above was essential.

The Axiom of Choice in any global form is inconsistent with this theory, but it is consistent for all well-founded sets to be well-orderable (in fact, this will be true in the models described above if the construction is carried out in an environment in which Choice is true). This is sufficient for the usual mathematical applications.

Since *ZF* is entirely immersed in this theory, it is clearly serviceable for the usual classical applications. The Frege natural numbers are not definable in this theory (except for 0 and 1); it is better to work with the finite von Neumann ordinals. The ability to prove strong results about large cardinals using the properties of the proper class ordinal suggests that the superstructure of large sets can be used for mathematical purposes as well. Familiarity with techniques of topology of *κ*-compact spaces would be useful for understanding what can be done with the big sets in this theory.

With the negation of the Axiom of Infinity, we get the theory of the *ω*-hyperuniverse, which is equiconsistent with second-order arithmetic, and so actually has a fair amount of mathematical strength. In this theory, the class of natural numbers (considered as finite ordinals) is not closed and acquires an extra element “at infinity” (which happens to be the closure of the class of natural numbers itself). Individual real numbers can be coded (using the usual Dedekind construction, actually) but the theory of sets of real numbers will begin to look quite different.

### 7.3 Critique of positive set theory

One obvious criticism is that this theory is *extremely* strong, compared with the other systems given here. This could be a good thing or a bad thing, depending on one’s attitude. If one is worried about the consistency of a weakly compact, the level of consistency strength here is certainly a problem (though the theory of the *ω*-hyperuniverse will stay around in any case). On the other hand, the fact that the topological motivation for set theory seems to work and yields a higher level of consistency strength than one might expect (“weakly compact” infinity following from merely uncountable infinity) might be taken as evidence that these are very powerful ideas.

The mathematical constructions that are readily accessible to this author are simply carried over from *ZF* or *ZFC*; the well-founded sets are considered within the world of positive set theory, and we find that they have exactly the properties we expect them to have from the usual viewpoint. It is rather nice that we get (fuzzier) objects in our set theory suitable to represent all of the usual proper classes; it is less clear what we can do with the other large objects than it is in *NFU*. A topologist might find this system quite interesting; in any event, topological expertise seems required to evaluate what can be done with the extra machinery in this system.

We briefly review the paradoxes: the Russell paradox doesn’t work because $x \not\in x$ is not a positive formula; notice that $\{x \mid x \in x\}$ exists! The Cantor paradox does not work because the proof of the Cantor theorem relies on an instance of comprehension which is not positive. $\wp(V)$ does exist and is equal to $V$. The ordinals are defined by a non-positive condition, and do not make up a set, but it is interesting to note that the closure $\mathbf{CL}(On)$ of the class $On$ of ordinals is equal to $On \cup \{\mathbf{CL}(On)\}$; the closure has itself as its only unexpected element.

## 8. Logically and Philosophically Motivated Variations

In the preceding set theories, the properties of the usual objects of mathematics accord closely with their properties as “intuitively” understood by most mathematicians (or lay people). (Strictly speaking, this is not quite true in *NFU* + Infinity without the additional assumption of Rosser’s Axiom of Counting, but the latter axiom (“$\mathbf{N}$ is strongly cantorian”) is almost always assumed in practice).

In the first two classes of system discussed in this section, logical considerations lead to the construction of theories in which “familiar” parts of the world look quite different. Constructive mathematicians do not see the same continuum that we do, and if they are willing to venture into the higher reaches of set theory, they find a different world there, too. The proponents of nonstandard analysis also find it useful to look at a different continuum (and even different natural numbers) though they do see the usual continuum and natural numbers embedded therein.

It is not entirely clear that the final item discussed in this section, the multiverse view of set theory proposed by Joel Hamkins, should be described as a view of the world of set theory at all: it proposes that we should consider that there are multiple different concepts of set each of which describes its own universe (and loosely we might speak of the complex of universes as a “multiverse”), but at bottom it is being questioned whether there is properly a single world of set theory at all. But the tentative list of proposed axioms he gives for relationships between universes have some of the flavor of an alternative set theory.

### 8.1 Constructive set theory

There are a number of attempts at constructive (intuitionistic) theories of types and set theories. We will describe a few systems here, quite briefly as we are not expert in constructive mathematics.

An intuitionistic typed theory of sets is readily obtained by simply adopting the intuitionistic versions of the axioms of *TST* as axioms. An Axiom of Infinity would be wanted to ensure that an interpretation of Heyting arithmetic could be embedded in the theory; it might be simplest to provide type 0 with the primitives of Heyting arithmetic (just as the earliest versions of *TST* had the primitives of classical arithmetic provided for type 0). We believe that this would give a quite comfortable environment for doing constructive mathematics.

Daniel Dzierzgowski has gone so far as to study an intuitionistic version of *NF* constructed in the same way; all that we can usefully report here is that it is not clear that the resulting theory *INF* is as strong as *NF* (in particular, it is unclear whether *INF* interprets Heyting Arithmetic, because Specker’s proof of Infinity in *NF* does not seem to go through in any useful way) but the consistency problem for *INF* remains open in spite of the apparent weakness of the theory.

A more ambitious theory is *IZF* (intuitionistic *ZF*). An interesting feature of the development of *IZF* is that one must be very careful in one’s choice of axioms: some formulations of the axioms of set theory have (constructively deducible) consequences which are not considered constructively valid (such as Excluded Middle), while other (classically equivalent) formulations of the axioms appear not to have such consequences: the latter forms, obviously to be preferred for a constructive development of set theory, often are not the most familiar ones in the classical context.

A set of axioms which seems to yield a nontrivial system of constructive mathematics is the following:

**Extensionality:** in the usual *ZF* form.

**Pairing, Union, Power Set, Infinity:** in the usual *ZF* form.

**Collection:** We are not sure why this is often preferred in constructive set theory, as it seems to us less constructive than replacement? But we have heard it said that Replacement is constructively quite weak.

**$\in$-Induction:** The induction on membership form is preferred for a highly practical reason: more usual formulations of Foundation immediately imply the Axiom of Excluded Middle!

See Friedman 1973 and Other Internet Resources for further information about *IZF*.

As is often the case in constructive mathematics generally, very simple notions of classical set theory (such as the notion of an ordinal) require careful reformulation to obtain the appropriate definition for the constructive environment (and the formulations often appear more complicated than familiar ones to the classical eye). Being inexpert, we will not involve ourselves further in this. It is worth noting that *IZF*, like many but not all constructive systems, admits a double negation interpretation of the corresponding classical theory *ZF*; we might think of *IZF* as a weakened version of *ZF* from the classical standpoint, but in its own terms it is the theory of a larger, more complex realm in which a copy of the classical universe of set theory is embedded.

The theories we have described so far are criticized by some constructive mathematicians for allowing an unrestricted power set operation. A weaker system *CZF* (constructive *ZF* has been proposed which does not have this operation (and which has the same level of strength as the weak set theory *KPU* without Power Set described earlier).

*CZF* omits Power Set. It replaces Foundation with $\in$-Induction for the same reasons as above. The axioms of Extensionality, Pairing, and Union are as in ordinary set theory. The axiom of Separation is restricted to bounded $(\Delta_0)$ formulas as in Mac Lane set theory or *KPU*.

The Collection axiom is replaced by two weaker axioms.

The Strong Collection axiom scheme asserts that if for every $x \in A$ there is $y$ such that $\phi (x, y)$, then there is a set $B$ such that for every $x \in A$ there is $y \in B$ such that $\phi(x, y)$ (as in the usual scheme) but also for every $y \in B$ there is $x \in A$ such that $\phi(x, y)$ ($B$ doesn’t contain any redundant elements). The additional restriction is useful because of the weaker form of the Separation Axiom.

The Subset Collection scheme can be regarded as containing a very weak form of Power Set. It asserts, for each formula $\phi(x, y, z)$ that for every $A$ and $B$, there is a set $C$ such that for each $z$ such that $\forall x \in A\exists y \in B[\phi(x, y, z)$] there is $R_z \in C$ such that for every $x \in A$ there is $y \in R_z$ such that $\phi(x, y, z)$ *and* for every $y \in R_z$ there is $x \in A$ such that $\phi(x, y, z)$ (this is the same restriction as in the Strong Collection axiom; notice that not only are images under the relation constructed, but the images are further collected into a set).

The Subset Collection scheme is powerful enough to allow the construction of the set of all functions from a set $A$ to a set $B$ as a set (which suggests that the classical version of this theory is as strong as *ZF*, since the existence of the set of functions from $A$ to $\{0, 1\}$ is classically as strong as the existence of the power set of $A$, and strong collection should allow the proof of strong separation in a classical environment).

This theory is known to be at the same level of consistency strength as the classical set theory *KPU*. It admits an interpretation in Martin-Löf constructive type theory (as *IZF* does not).

See Aczel (1978, 1982, 1986)[^aczel-1978][^aczel-1982][^aczel-1986] for further information about this theory.

### 8.2 Set theory for nonstandard analysis

Nonstandard analysis originated with Abraham Robinson (1966)[^robinson-1966], who noticed that the use of nonstandard models of the continuum would allow one to make sense of the infinitesimal numbers of Leibniz, and so obtain an elegant formulation of the calculus with fewer alternations of quantifiers.

Later exponents of nonstandard analysis observed that the constant reference to the model theory made the exposition less elementary than it could be; they had the idea of working in a set theory which was inherently “nonstandard”.

We present a system of this kind, a version of the set theory *IST* (Internal Set Theory) of Nelson (1977)[^nelson-1977]. The primitives of the theory are equality, membership, and a primitive notion of *standardness*. The axioms follow.

**Extensionality, Pairing, Union, Power Set, Foundation, Choice:** As in our presentation of *ZFC* above.

**Separation, Replacement:** As in our presentation of *ZFC* above, except that the standardness predicate cannot appear in the formula *φ*.

**Definition:** For any formula *φ*, the formula *φ*ˢᵗ is obtained by replacing each quantifier over the universe with a quantifier over all standard objects (and each quantifier bounded in a set with a quantifier restricted to the standard elements of that set).

**Idealization:** There is a finite set which contains all standard sets.

**Transfer:** For each formula $\phi(x)$ not mentioning the standardness predicate and containing no parameters (free variables other than $x)$ except standard sets, $\forall x\phi(x) \equiv \forall x$(*standard*$(x) \rightarrow \phi(x))$.

**Standardization:** For any formula $\phi(x)$ and standard set $A$, there is a standard set $B$ whose standard elements are exactly the standard elements $x$ of $A$ satisfying $\phi(x)$.

Our form of Idealization is simpler than the usual version but has the same effect.

Transfer immediately implies that any uniquely definable object (defined without reference to standardness) is in fact a standard object. So the empty set is standard, *ω* is standard, and so forth. But it is not the case that all elements of standard objects are standard. For consider the cardinality of a finite set containing all standard objects; this is clearly greater that any standard natural number (usual element of $\omega)$ yet it is equally clearly an element of *ω*. It turns out to be provable that every set all of whose elements are standard is a standard finite set.

Relative consistency of this theory with the usual set theory *ZFC* is established via familiar results of model theory. Working in this theory makes it possible to use the techniques of nonstandard analysis in a “elementary” way, without ever appealing explicitly to the properties of nonstandard models.

### 8.3 The multiverse view of set theory

We examine the theory of the set theoretic multiverse proposed by Joel David Hamkins, whose purpose is to address philosophical questions about independence questions in standard set theory, but which when spelled out formally has some of the flavor of an alternative set theory. A set theoretic Platonist might say about the Continuum Hypothesis (*CH*) that, since there is “of course” a single universe of sets, *CH* is either true or false in that world, but that we cannot determine which of *CH* and $\neg$*CH* actually holds. Hamkins proposes as an alternative (taking the same realist standpoint as the classical Platonist, it must be noted) that there are many distinct concepts of set, which we may suppose for the moment all satisfy the usual axioms of *ZFC*, each concept determining its own universe of sets, and in some of these universes *CH* holds and in some it does not hold. He says further, provocatively, that in his view *CH* is a solved problem, because we have an excellent understanding of the conditions under which *CH* holds in $a$ universe of sets (note the article used) and the conditions in which it does not hold, and even more provocatively, he argues that an “ideal” solution to the *CH* problem in which a generally accepted axiom arises which causes most mathematicians to conclude that *CH* is “self-evidently” true or false (deciding the question in the usual sense) is now actually impossible, because set theorists are now very conversant with universes in which both alternatives hold, and understand very well that neither alternative is “self-evidently” true (the force of his argument is really that the complementary conclusion that one of the alternatives is self-evidently false is now impossible to draw, because we are too well acquainted with actual “worlds” in which each alternative holds to believe that either is absurd).

We could write an entire essay on questions raised in our summary in the previous paragraph, but Hamkins has already done this in Hamkins 2012. Our aim here is to summarize the tentative axioms that Hamkins presents for the multiverse conception. This is not really a formal set of axioms, but it does have some of the qualities of an axiomatization of an alternative set theory. We note that the list of axioms presented here unavoidably presupposes more knowledge of advanced set theory than other parts of this article.

**Realizability Principle:** For any universe $V$, if $W$ is a model of set theory and definable or interpreted in $V$, then $W$ is a universe.

One thing to note here is that Hamkins is open to the idea that some universes may be models of theories other than *ZFC* (weaker theories such as Zermelo set theory or Peano arithmetic, or even different theories such as *ZFA* or *NF/NFU*). But it appears to be difficult philosophically to articulate exact boundaries for what counts as a “concept of set theory” which would define a universe. And this is fine, because there is no notion of “the multiverse” of universes as a completed totality here at all—this would amount to smuggling in the single Platonic universe again through the back door! Some of the axioms which follow do presume that the universes discussed are models of *ZFC* or very similar theories.

**Forcing Extension Principle:** For any universe $V$ and any forcing notion $P$ in $V$, there is a forcing extension $V[G]$, where $G \subset P$ is $V$-generic.

This asserts that our forcing extensions are concretely real worlds. Hamkins discusses the metaphysical difficulties of the status of forcing extensions at length in Hamkins 2012.

**Reflection Axiom:** For every universe $V$, there is a much taller universe $W$ with an ordinal *θ* for which $V$ is elementarily equivalent to (or isomorphic to) $W_{\theta}$, a level of the cumulative hierarchy in $W$.

We quote Hamkins:

> the principle asserts that no universe is correct about the height of the ordinals, and every universe looks like an initial segment of a much taller universe having the same truths. (2012: 438)

Here we are presuming that the universes we are talking about are models of *ZFC* or a *ZFC*-like theory.

**Countability Principle:** Every universe $V$ is countable from the perspective of another, better universe $W$.

This definitely has the flavor of an alternative set theory axiom! The model theoretic motivation is obvious: this amounts to taking Skolem’s paradox seriously. Hamkins notes that the Forcing Extension principle above already implies this, but it is clear in any case that his list of tentative axioms is intended to be neither independent nor complete.

**Well-foundedness Mirage:** Every universe $V$ is ill-founded from the perspective of another, better universe.

Hamkins says that this may be the most provocative of all his axioms. He states that he intends this to imply that even our notion of natural numbers is defective in any universe: the collection of natural numbers as defined in any universe is seen to contain nonstandard elements from the standpoint of a further universe.

**Reverse Embedding Axiom:** For every universe $V$ and every embedding $j : V \rightarrow M$ in $V$, there is a universe $W$ and embedding $h: W \rightarrow V$ such that $j$ is the iterate of $h$.

We merely quote this astonishing assertion, which says that for any elementary embedding of a universe $V$ into a model $M$ included in $V$, our understanding of this embedding locally to $V$ itself is seriously incomplete.

**Absorption into L:** Every universe $V$ is a countable transitive model in another universe $W$ satisfying $V = L$.

We are used to thinking of the constructible universe $L$ as a “restricted” universe. Here Hamkins turns this inside out (he discusses at length why this is a reasonable way to think in the paper Hamkins 2012)[^hamkins-2012].

We leave it to the reader who is interested to pursue this further.

## 9. Small Set Theories

It is commonly noted that set theory produces far more superstructure than is needed to support classical mathematics. In this section, we describe two miniature theories which purport to provide enough foundations without nearly as much superstructure. Our “pocket set theory” (motivated by a suggestion of Rudy Rucker) is just small; Vopenka’s alternative set theory is also “nonstandard” in its approach.

### 9.1 Pocket set theory

This theory is a proposal of ours, which elaborates on a suggestion of Rudy Rucker. We (and many others) have observed that of all the orders of infinity in Cantor’s paradise, only two actually occur in classical mathematical practice outside set theory: these are $\aleph_0$ and $c$, the infinity of the natural numbers and the infinity of the continuum. Pocket set theory is a theory motivated by the idea that these are the only infinities (Vopenka’s alternative set theory also has this property, by the way).

The objects of pocket set theory are classes. A class is said to be a set iff it is an element (as in the usual class theories over *ZFC*).

The ordered pair is defined using the usual Kuratowski definition, but without assuming that there are any ordered pairs. The notions of relation, function, bijection and equinumerousness are defined as usual (still without any assumptions as to the existence of any ordered pairs). An infinite set is defined as a set which is equinumerous with one of its proper subsets. A proper class is defined as a class which is not a set.

The axioms of pocket set theory are

**Extensionality:** Classes with the same elements are equal.

**Class Comprehension:** For any formula *φ*, there is a class $\{x \mid \phi(x)\}$ which contains all sets $x$ such that $\phi(x)$. (note that this is the class comprehension axiom of Kelley-Morse set theory, without any restrictions on quantifiers in $\phi)$.

**Infinite Sets:** There is an infinite set; all infinite sets are the same size.

**Proper Classes:** All proper classes are the same size, and any class the same size as a proper class is proper.

We cannot resist proving the main results (because the proofs are funny).

**Empty Set:** If the empty set were a proper class, then all proper classes would be empty. In particular, the Russell class would be empty. Let $I$ be an infinite set. $\{I\}$ would be a set, because it is not empty, and $\{I,\{I\}\}$ would be a set (again because it is not empty). But $\{I,\{I\}\}$ belongs to the Russell class (as a set with two elements, it cannot be either the Dedekind infinite $I$ or the singleton $\{I\}$. So $\varnothing$ is a set.

**Singleton:** If any singleton $\{x\}$ is a proper class, then all singletons are proper classes, and the Russell class is a singleton. $\{I, \varnothing \}$ is a set (both elements are sets, and the class is not a singleton) which cannot be a member of itself, and so is in the Russell class. But so is $\varnothing$ in the Russell class; so the Russell class is not a singleton, and all singletons are sets.

**Unordered Pair:** The Russell class is not a pair, because it has distinct elements $\varnothing , \{\varnothing \}, \{\{\varnothing \}\}$.

**Relations:** All Kuratowski ordered pairs exist, so all definable relations are realized as set relations.

Cantor’s theorem (no set is the same size as the class of its subsets) and the Schröder-Bernstein theorem (if there are injections from each of two classes into the other, there is a bijection between them) have their standard proofs.

The Russell class can be shown to be the same size as the universe using Schröder-Bernstein: the injection from $R$ into $V$ is obvious, and $V$ can be embedded into $R$ using the map $x \mapsto \{\{x\}, \varnothing \}$ (clearly no set $\{\{x\}, \varnothing \}$ belongs to itself). So a class is proper iff it is the same size as the universe (limitation of size).

Define the von Neumann ordinals as classes which are strictly well-ordered by membership. Each finite ordinal can be proved to be a set (because it is smaller than its successor and is a subclass of the Russell class). The class of all ordinals is not a set (but is the last ordinal), for the usual reasons, and so is the same size as the universe, and so the universe can be well-ordered.

There is an infinite ordinal, because there is an ordinal which can be placed in one-to-one correspondence with one’s favorite infinite set $I$. Since there is an infinite ordinal, every finite ordinal is a set and the first infinite ordinal *ω* is a set. It follows that all infinite sets are countably infinite.

The power set of an infinite set $I$ is not the same size as $I$ by Cantor’s theorem, is certainly infinite, and so cannot be a set, and so must be the same size as the universe. It follows by usual considerations that the universe is the same size as $\wp(\omega)$ or as $\mathbf{R}$ (the set of real numbers, defined in any of the usual ways), and its “cardinal” is $c$. Further, the first uncountable ordinal $\omega_1$ is the cardinality of the universe, so the Continuum Hypothesis holds.

It is well-known that coding tricks allow one to do classical mathematics without ever going above cardinality $c$: for example, the class of *all* functions from the reals to the reals, is too large to be even a proper class here, but the class of *continuous* functions is of cardinality $c$. An individual continuous function $f$ might seem to be a proper class, but it can be coded as a hereditarily countable set by (for example) letting the countable set of pairs of rationals $\langle p, q\rangle$ such that $p \lt f(q)$ code the function $f$. In fact, it is claimed that most of classical mathematics can be carried out using just natural numbers and sets of natural numbers (second-order arithmetic) or in even weaker systems, so pocket set theory (having the strength of *third* order arithmetic) can be thought to be rather generous.

We do remark that it is not necessarily the case that the hypothetical advocate of pocket set theory thinks that the universe is small; he or she might instead think that the continuum is very large…

### 9.2 Vopenka’s alternative set theory

Petr Vopenka has presented the following *alternative set theory* (1979).

The theory has sets and classes. The following axioms hold of sets.

**Extensionality:** Sets with the same elements are the same.

**Empty set:** $\varnothing$ exists.

**Successor:** For any sets $x$ and $y, x \cup \{y\}$ exists.

**Induction:** Every formula *φ* expressed in the language of sets only (all parameters are sets and all quantifiers are restricted to sets) and true of $\varnothing$ and true of $x \cup \{y\}$ if it is true of $x$ is true of all sets.

**Regularity:** Every set has an element disjoint from it.

The theory of sets appears to be the theory of $V_{\omega}$ (the hereditarily finite sets) in the usual set theory!

We now pass to consideration of classes.

**Existence of classes:** If $\phi(x)$ is any formula, then the class $\phi(x)$ of all sets $x$ such that $\phi(x)$ exists. (The set $x$ is identified with the class of elements of $x$.) Note that Kuratowski pairs of sets are sets, and so we can define (class) relations and functions on the universe of sets much as usual.

**Extensionality for classes:** Classes with the same elements are equal.

**Definition:** A *semiset* is a subclass of a set. A *proper class* is a class which is not a set. A *proper semiset* is a subclass of a set which is not a set.

**Axiom of proper semisets:** There is a proper semiset.

A proper semiset is a signal that the set which contains it is nonstandard (recall that all sets *seem* to be hereditarily finite!)

**Definition:** A set is *finite* iff all of its subclasses are sets.

A finite set has standard size (the use of “finite” here could be confusing: all *sets* are nonstandard finite here, after all).

**Definition:** An ordering of type *ω* is a class well-ordering which is infinite and all of whose initial segments are finite. A class is countable if it has an ordering of type *ω*.

An ordering of type *ω* has the same length as the *standard* natural numbers. We can prove that there is such an ordering: consider the order on the finite (i.e., standard finite) von Neumann ordinals. There must be infinite von Neumann ordinals because there is a set theoretically definable bijection between the von Neumann ordinals and the whole universe of sets: any proper semiset can be converted to a proper semiset of a set of von Neumann ordinals.

**Prolongation axiom:** Each countable function $F$ can be extended to a set function.

The Prolongation Axiom has a role similar to that of the Idealization Axiom in the “nonstandard” set theory *IST* above, though the analogy between the alternative set theory and *IST* is far from perfect.

Vopenka considers representations of superclasses of classes using relations on sets. A class relation $R$ on a class $A$ is said to code the superclass of inverse images of elements of $A$ under $R$. A class relation $R$ on a class $A$ is said to extensionally code this superclass if distinct elements of $A$ have distinct preimages. He “tidies up” the theory of such codings by adopting the

**Axiom of extensional coding:** Every collection of classes which is codable is extensionally codable.

It is worth noting that this can be phrased in a way which makes no reference to superclasses: for any class relation $R$, there is a class relation $R'$ such that for any $x$ there is $x'$ with preimage under $R'$ equal to the preimage of $x$ under $R$, and distinct elements of the field of $R'$ have distinct preimages.

His notion of coding is more general: we can further code collections of classes by taking a pair $\langle K, R\rangle$ where $K$ is a subclass of the field of $R$; clearly any collection of classes codable in this way can be extensionally coded by using the axiom in the form we give.

The final axiom is

**Axiom of cardinalities:** If two classes are uncountable, they are the same size.

This implies (as in pocket set theory) that there are two infinite cardinalities, which can be thought of as $\aleph_0$ and $c$, though in this context their behavior is less familiar than it is in pocket set theory. For example, the set of all natural numbers (as Vopenka defines it) is of cardinality $c$, while there is an initial segment of the natural numbers (the finite natural numbers) which has the expected cardinality *ω*.

One gets the axiom of choice from the axioms of cardinalities and extensional codings; the details are technical. One might think that this would go as in pocket set theory: the order type of all the ordinals is not a set and so has the same cardinality as the universe. But this doesn’t work here, because the “ordinals” in the obvious sense are all nonstandard finite ordinals, which, from a class standpoint, are not well-ordered at all. However, there is a devious way to code an uncountable well-ordering using the axiom of extensional coding, and since its domain is uncountable it must be the same size as the universe.

This is a rather difficult theory. A model of the alternative set theory in the usual set theory is a nonstandard model of $V_{\omega}$ of size $\omega_1$ in which every countable external function extends to a function in the model. It might be best to suppose that this model is constructed inside $L$ (the constructible universe) so that the axiom of cardinalities will be satisfied. The axiom of extensional coding follows from Choice in the ambient set theory.

The constructions of the natural numbers and the real numbers with which we started go much as usual, except that we get two kinds of natural numbers (the finite von Neumann ordinals in the set universe (nonstandard), and the *finite* von Neumann set ordinals (standard)). The classical reals can be defined as Dedekind cuts in the standard rationals; these are not sets, but any real can then be approximated by a nonstandard rational. One can proceed to do analysis with some (but not quite all) of the tools of the usual nonstandard analysis.

## 10. Double Extension Set Theory: A Curiosity

A recent proposal of Andrzej Kisielewicz (1998)[^kisielewicz-1998] is that the paradoxes of set theory might be evaded by having two different membership relations $\in$ and *ε*, with each membership relation used to define extensions for the other.

We present the axiomatics. The primitive notions of this theory are equality $(=)$ and the two flavors $\in$ and *ε* of membership. A formula *φ* is *uniform* if it does not mention *ε*. If *φ* is a uniform formula, $\phi^*$ is the corresponding formula with $\in$ replaced by *ε* throughout. A set $A$ is *regular* iff it has the same extension with respect to both membership relations: $x \in A \equiv x \varepsilon A$.

The comprehension axiom asserts that for any uniform formula $\phi(x)$ in which all parameters (free variables other than $x$) are regular, there is an object $A$, for which we use the notation $\{x \mid \phi(x)\}$, such that $\forall x ((x \in A \equiv \phi^*) \amp (x \varepsilon A \equiv \phi))$.

The extensionality axiom asserts that for any $A$ and $B$, $\forall x(x \in A \equiv x \varepsilon B) \rightarrow A = B$. Notice that any object to which this axiom applies is regular.

Finally, a special axiom asserts that any set one of whose extensions is included in a regular set is itself regular.

This theory can be shown to interpret *ZF* in the realm of *hereditarily regular sets*. Formally, the proof has the same structure as the proof for Ackermann set theory. It is unclear whether this theory is actually consistent; natural ways to strengthen it (including the first version proposed by Kisielewicz) turn out to be inconsistent. It is also extremely hard to think about!

An example of the curious properties of this theory is that the ordinals under one membership relation are exactly the regular ordinals while under the other they are longer; this means that the apparent symmetry between the two membership relations breaks!

## 11. Conclusion

We have presented a wide range of theories here. The theories motivated by essentially different views of the realm of mathematics (the constructive theories and the theories which support nonstandard analysis) we set to one side. Similarly, the theories motivated by the desire to keep the universe small can be set to one side. The alternative classical set theories which support a fluent development of mathematics seem to be *ZFC* or its variants with classes (including Ackermann), *NFU* + Infinity + Choice with suitable strong infinity axioms (to get s.c. sets to behave nicely), and the positive set theory of Esser. Any of these is adequate for the purpose, in our opinion, including the one currently in use. There is no compelling reason for mathematicians to use a different foundation than *ZFC*; but there is a good reason for mathematicians who have occasion to think about foundations to be aware that there are alternatives; otherwise there is a danger that accidental features of the dominant system of set theory will be mistaken for essential features of any foundation of mathematics. For example, it is frequently said that the universal set (an extension which is actually trivially easy to obtain in a weak set theory) is an inconsistent totality; the actual situation is merely that one cannot have a universal set while assuming Zermelo’s axiom of separation.

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=settheory-alternative). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/settheory-alternative/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=settheory-alternative&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/settheory-alternative/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

- Aczel, Peter and Michael Rathjen, 2001, “[Notes on Constructive Set Theory](https://web.archive.org/web/20110725092152/http://www.ml.kva.se/preprints/archive/2000-2001/2000-2001-40.pdf)”, Technical Report No. 40, 2000/2001, Institut Mittag-Leffler, The Royal Swedish Academy of Sciences.
- Holmes, Randall, 2021, [Review of D. Booth and R. Ziegler (eds.), *Finsler Set Theory: Platonism and Circularity*](https://randall-holmes.github.io/Drafts/finslerreview.pdf) (PDF), manuscript, 19 September 2021.
- Holmes, Randall and Sky Wilshaw, 2025, “[New Foundations is Consistent](https://arxiv.org/pdf/1503.01406)”, a claimed proof of the consistency of New Foundations, at arXiv.org.
- “[New Foundations is consistent A digitisation of Randall Holmes’ proof](https://leanprover-community.github.io/con-nf/)”, the landing page for a formalization in Lean of the central construction of the claimed consistency proof.

## Related Entries

Brouwer, Luitzen Egbertus Jan | choice, axiom of | continuity and infinitesimals | Frege, Gottlob | Frege, Gottlob: theorem and foundations for arithmetic | logic: intuitionistic | mathematics: constructive | *Principia Mathematica* | Quine, Willard Van Orman: New Foundations | Russell’s paradox | set theory | type theory

[^aczel-1978]: Aczel, Peter, 1978, “The Type Theoretic Interpretation of Constructive Set Theory”, in A. MacIntyre, L. Pacholski, J. Paris (eds.), *Logic Colloquium ‘77*, (Studies in Logic and the Foundations of Mathematics, 96), Amsterdam: North-Holland, pp. 55–66. doi:10.1016/S0049-237X(08)71989-X

[^aczel-1982]: –––, 1982, “The Type Theoretic Interpretation of Constructive Set Theory: Choice Principles”, in A.S. Troelstra and D. van Dalen (eds.), *The L.E.J. Brouwer Centenary Symposium*, (Studies in Logic and the Foundations of Mathematics, 110), Amsterdam: North-Holland, pp. 1–40. doi:10.1016/S0049-237X(09)70120-X

[^aczel-1986]: –––, 1986, “The Type Theoretic Interpretation of Constructive Set Theory: Inductive Definitions”, in Ruth Barcan Marcus, Georg J.W.Dorn, and Paul Weingartner (eds.), *Logic, Methodology, and Philosophy of Science VII*, (Studies in Logic and the Foundations of Mathematics, 114), Amsterdam: North-Holland, pp. 17–49. doi:10.1016/S0049-237X(09)70683-4

[^aczel-1988]: –––, 1988, *Non-Well-Founded Sets* (CSLI Lecture Notes, 14), Stanford: CSLI Publications.

[^st-nd]: St. Augustine, *De Civitate Dei*, Book 12, chapter 18.

[^barwise-1975]: Barwise, Jon, 1975, *Admissible Sets and Structures: An Approach to Definability Theory*, (Perspectives in Mathematical Logic, 7), Berlin: Springer-Verlag.

[^boffa-1988]: Boffa, M., 1988, “ZFJ and the Consistency Problem for NF”, *Jahrbuch der Kurt Gödel Gesellschaft*, Vienna, pp. 102–106

[^burali-forti-1897]: Burali-Forti, C., 1897, “Una questione sui numeri transfiniti”, *Rendiconti del Circolo matematico di Palermo*, 11(1): 154–164. A correction appears in “Sulle classi ben ordinate”, *Rendiconti del Circolo matematico di Palermo*, 11(1): 260. It is not clear that Burali-Forti ever correctly understood his paradox. doi:10.1007/BF03015911 and doi:10.1007/BF03015919

[^cantor-1872]: Cantor, Georg, 1872, “Über die Ausdehnung eines Satzes aus der Theorie der trigonometrischen Reihen”, *Mathematischen Annalen*, 5: 123–32.

[^cantor-1891]: –––, 1891, “Über eine elementare Frage der Mannigfaltigkeitslehre”, *Jahresbericht der deutschen Mathematiker-Vereiningung*, 1: 75–8.

[^cocchiarella-1985]: Cocchiarella, Nino B., 1985, “Frege’s Double-Correlation Thesis and Quine’s Set Theories NF and ML”, *Journal of Philosophical Logic*, 14(1): 1–39. doi:10.1007/BF00542647

[^crabbé-1982]: Crabbé, Marcel, 1982, “On the Consistency of an Impredicative Subsystem of Quine’s *NF*”, *Journal of Symbolic Logic*, 47(1): 131–36. doi:10.2307/2273386

[^crabbé-2016]: –––, 2016, “*NFSI* is not included in *NF*₃”, *Journal of Symbolic Logic*, 81(3): 948–950. doi:10.1017/jsl.2015.29

[^dedekind-1872]: Dedekind, Richard, 1872, *Stetigkeit und irrationale Zahlen*, Brannschweig: Friedrich Vieweg und Sohn (second edition, 1892).

[^esser-1999]: Esser, Olivier, 1999, “On the Consistency of a Positive Theory”, *Mathematical Logic Quarterly*, 45(1): 105–116. doi:10.1002/malq.19990450110

[^feferman-2006]: Feferman, Sol, 2006, “Enriched Stratified Systems for the Foundations of Category Theory” in Giandomenico Sica (ed.), *What is Category Theory?*, Milan: Polimetrica. [[Feferman 2006 preprint available online (PDF)](https://web.archive.org/web/20171211043750/http://math.stanford.edu/%7Efeferman/papers/ess.pdf)]

[^frege-1884]: Frege, Gottlob, 1884, *Die Grundlagen der Arithmetik*, English translation by J.L. Austin, *The Foundations of Arithmetic*, Oxford: Blackwell, 1974.

[^friedman-1973]: Friedman, Harvey, 1973, “Some Applications of Kleene’s Methods for Intuitionistic Systems”, in A.R.D. Mathias and H. Rogers (eds.), *Cambridge Summer School in Mathematical Logic*, (Lecture Notes in Mathematics, 337), Berlin: Springer-Verlag, pp. 113–170. doi:10.1007/BFb0066773

[^grishin-1969]: Grishin, V.N., 1969, “Consistency of a Fragment of Quine’s *NF* System”, *Soviet Mathematics Doklady*, 10: 1387–1390.

[^hallett-1984]: Hallett, Michael, 1984, *Cantorian Set Theory and Limitation of Size*, Oxford: Clarendon, pp. 280–286.

[^hamkins-2012]: Hamkins, Joel David, 2012, “The Set-Theoretic Multiverse”, *Review of Symbolic Logic*, 5(3): 416–449. doi:10.1017/S1755020311000359

[^holmes-1998]: Holmes, M. Randall, 1998, *Elementary Set Theory with a Universal Set*, (Cahiers du Centre de logique, 10), Louvain-la-Neuve: Academia. (See chapter 20 for the discussion of well-founded extensional relation types.) [[Holmes 1998 revised and corrected version available online (PDF)](https://randall-holmes.github.io/head.pdf)]

[^holmes-2012]: –––, 2012, “The Usual Model Construction for *NFU* Preserves Information”, *Notre Dame Journal of Formal Logic*, 53(4): 571–580. doi:10.1215/00294527-1722764

[^jensen-1968]: Jensen, Ronald Bjorn, 1968, “On the Consistency of a Slight (?) Modification of Quine’s ‘New Foundations’”, *Synthese*, 19(1): 250–63. doi:10.1007/BF00568059

[^kisielewicz-1998]: Kisielewicz, Andrzej, 1998, “A Very Strong Set Theory?”, *Studia Logica*, 61(2): 171–178. doi:10.1023/A:1005048329677

[^kuratowski-1921]: Kuratowski, Casimir [Kazimierz], 1921, “Sur la notion de l’ordre dans la Théorie des Ensembles”, *Fundamenta Mathematicae*, 2(1): 161–171. [[Kuratowski 1921 available online](http://eudml.org/doc/212966)]

[^lévy-1959]: Lévy, Azriel, 1959, “On Ackermann’s Set Theory”, *Journal of Symbolic Logic*, 24(2): 154–166. doi:10.2307/2964757

[^mac-1986]: Mac Lane, Saunders, 1986, *Mathematics, Form and Function*, Berlin: Springer-Verlag.

[^mathias-2001a]: Mathias, A.R.D., 2001a, “The Strength of Mac Lane Set Theory”, *Annals of Pure and Applied Logic*, 110(1–3): 107–234. doi:10.1016/S0168-0072(00)00031-2

[^mathias-2001b]: –––, 2001b, “Slim Models of Zermelo Set Theory”, *The Journal of Symbolic Logic*, 66(2): 487–496. doi:10.2307/2695026

[^mclarty-1992]: McLarty, Colin, 1992, “Failure of Cartesian Closedness in *NF*”, *Journal of Symbolic Logic*, 57(2): 555–6. doi:10.2307/2275291

[^nelson-1977]: Nelson, Edward, 1977, “Internal Set Theory, a New Approach to Nonstandard Analysis”, *Bulletin of the American Mathematical Society*, 83(6): 1165–1198. doi:10.1090/S0002-9904-1977-14398-X

[^quine-1937]: Quine, W.V.O., 1937, “New Foundations for Mathematical Logic”, *American Mathematical Monthly*, 44(2): 70–80. doi:10.2307/2300564

[^quine-1945]: –––, 1945, “On Ordered Pairs”, *Journal of Symbolic Logic*, 10(3): 95–96. doi:10.2307/2267028

[^reinhardt-1970]: Reinhardt, William N., 1970, “Ackermann’s Set Theory Equals ZF”, *Annals of Mathematical Logic*, 2(2): 189–249. doi:10.1016/0003-4843(70)90011-2

[^robinson-1966]: Robinson, Abraham, 1966, *Non-standard Analysis*, Amsterdam: North-Holland.

[^rosser-1973]: Rosser, J. Barkley, 1973, *Logic for Mathematicians*, second edition, New York: Chelsea.

[^russell-1903]: Russell, Bertrand, 1903, *The Principles of Mathematics*, London: George Allen and Unwin.

[^specker-1953]: Specker, Ernst P., 1953, “The Axiom of Choice in Quine’s ‘New Foundations for Mathematical Logic’”, *Proceedings of the National Academy of Sciences of the United States of America*, 39(9): 972–5. [[Specker 1953 available online](http://www.pnas.org/content/39/9/972)]

[^spinoza-1677]: Spinoza, Benedict de, 1677, *Ethics*, reprinted and translated in *A Spinoza Reader: the “Ethics” and Other Works*, Edwin Curley (ed. and trans.), Princeton: Princeton University Press, 1994.

[^tupailo-2010]: Tupailo, Sergei, 2010, “Consistency of Strictly Impredicative **NF** and a Little More …”, *Journal of Symbolic Logic*, 75(4): 1326–1338. doi:10.2178/jsl/1286198149

[^vopěnka-1979]: Vopěnka, Petr, 1979, *Mathematics in the Alternative Set Theory*, Leipzig: Teubner-Verlag.

[^wang-1970]: Wang, Hao, 1970, *Logic, Computers, and Sets*, New York: Chelsea, p. 406.

[^whitehead-1910]: Whitehead, Alfred North and Bertrand Russell, [*PM*] 1910–1913, *Principia Mathematica*, 3 volumes, Cambridge: Cambridge University Press.

[^wiener-1914]: Wiener, Norbert, 1914, “A Simplification of the Logic of Relations”, *Proceedings of the Cambridge Philosophical Society*, 17: 387–390.

[^zermelo-1908]: Zermelo, Ernst, 1908, “Untersuchen über die Grundlagen der Mengenlehre I”, *Mathematische Annalen*, 65: 261–281.
