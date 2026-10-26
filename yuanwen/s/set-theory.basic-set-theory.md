# set-theory — basic-set-theory（supplement）

> （《set-theory》词条补充材料，源：plato.stanford.edu/entries/set-theory/basic-set-theory.html）

Set Theory > Basic Set Theory (Stanford Encyclopedia of Philosophy)

Stanford Encyclopedia of Philosophy

Menu

- Browse
- Table of Contents
- What's New
- [Random Entry](https://plato.stanford.edu/cgi-bin/encyclopedia/random)
- Chronological
- Archives
- About
- Editorial Information
- About the SEP
- Editorial Board
- How to Cite the SEP
- Special Characters
- Advanced Tools
- Contact
- Support SEP
- Support the SEP
- PDFs for SEP Friends
- Make a Donation
- SEPIA for Libraries

Entry Navigation

- Back to Entry
- Entry Contents
- Entry Bibliography
- Academic Tools
- [Friends PDF Preview ](https://leibniz.stanford.edu/friends/preview/set-theory/)
- [Author and Citation Info ](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=set-theory)
- Back to Top

#### Supplement to Set Theory

## Basic Set Theory

Sets are well-determined collections that are completely characterized by their elements. Thus, two sets are equal if and only if they have exactly the same elements. The basic relation in set theory is that of elementhood, or membership. We write $a\in A$ to indicate that the object $a$ is an *element*, or a *member*, of the set $A$. We also say that $a$ *belongs to* $A$. Thus, a set $A$ is equal to a set $B$ if and only if for every $a$, $a\in
A$ if and only if $a\in B$. In particular, there is only one set with no elements at all. This set is called, naturally, the *empty set*, and is represented by the symbol ${\varnothing}$.

We say that $A$ is a *subset* of $B$, written $A\subseteq
B$, if every element of $A$ is an element of $B$. Thus, $A=B$ if and only if $A\subseteq B$ and $B\subseteq A$. Notice that ${\varnothing}\subseteq A$, for every set $A$.

Given sets $A$ and $B$, one can perform some basic operations with them yielding the following sets:

- The set $A\cup B$, called the *union* of $A$ and $B$, whose elements are the elements of $A$ and the elements of $B$.
- The set $A\cap B$, called the *intersection* of $A$ and $B$, whose elements are the elements common to $A$ and $B$.
- The set $A-B$, called the *difference* of $A$ and $B$, whose elements are those elements of $A$ that are not members of $B$.

It is routine to check that those operations satisfy the following properties:

- Associativity:
- $A \cup (B\cup C)=(A\cup B)\cup C$
- $A \cap (B\cap C)=(A\cap B)\cap C$
- Commutativity:
- $A \cup B=B\cup A$
- $A \cap B=B\cap A$
- Distributivity:
- $A \cup (B\cap C)=(A\cup B)\cap (A\cup C)$
- $A \cap (B\cup C)=(A\cap B)\cup (A\cap C)$
- Idempotency:
- $A \cup A=A$
- $A \cap A=A$
- 
- $A \cup {\varnothing}=A$
- $A\cap {\varnothing}={\varnothing}$
- $A - A={\varnothing}$
- If $A\subseteq B$, then
- $A\cup B=A\cup (B-A)=B$
- $A \cap B=A$

Given an object $a$ we can form the set that has $a$ as its only element. This set is denoted by $\{ a \}$. More generally, given $a,b,c,\ldots$, we can form the set having $a,b,c,\ldots$ as its elements, which we denote by $\{ a,b,c, \ldots\}$. Of course, we can actually write down all the elements of the set when there are not too many of them. In the case of infinite sets this is clearly not possible.

If $a=b$, then $\{ a,b\}=\{ a\}$. Also, for any $a$ and $b$, the pair $\{ a,b\}$ is the same as the pair $\{ b,a\}$. So, if we wish to take into account the order in which the two elements of a pair are given, we need to find another way of representing the pair. Thus, we define the *ordered pair* $(a,b)$ as the set $\{ \{
a\},\{ a,b\}\}$. One can easily check that two ordered pairs $(a,b)$ and $(c,d)$ are equal if and only if $a=c$ and $b=d$. The order is now important, for if $a\ne b$, then $(a,b)\ne
(b,a)$.

The *Cartesian product* $A\times B$ of two sets, $A$ and $B$, is defined as the set of all ordered pairs $(a,b)$ such that $a\in A$ and $b\in B$.

Having defined ordered pairs, one can now define *ordered triples* $(a,b,c)$ as $(a,(b,c))$, or in general *ordered $n$-tuples* $(a_1,\ldots ,a_n)$ as $(a_1, (a_2,\ldots
,a_n))$.

The Cartesian product $A_1 \times \ldots \times A_n$, of the sets $A_1,\ldots , A_n$ is the set of all $n$-tuples $(a_1,\ldots
,a_n)$ such that $a_i \in A_i$, for every $1\leq i\leq n$. In particular, for $n\geq 2$, the $n$-times Cartesian product of a set $A$, denoted by $A^n$, is the set of all $n$-tuples of elements of $A$.

- 1. Relations
- 2. Functions
- 3. Sets and formulas
- 4. Ordinals
- 5. Countable and uncountable sets
- 5.1 Cardinals
- Further Readings

### 1. Relations

A *binary relation* on a set $A$ is a set of ordered pairs of elements of $A$, that is, a subset of $A\times A$. In general, an *$n$-ary relation* on $A$ is a subset of $A^n$.

A binary relation $R$ on a set $A$ is called *reflexive* if $(a,a)\in R$ for every $a\in A$. It is called *symmetric* if $(b,a)\in R$ whenever $(a,b)\in R$. And it is called *transitive* if $(a,c)\in R$ whenever $(a,b)\in R$ and $(b,c)\in R$. A relation that is reflexive, symmetric, and transitive is called an *equivalence relation*. The identity relation on any set $A$ is the paradigmatic example of an equivalence relation. Another example is the relation on the set of all finite sets of natural numbers consisting of all the pairs $(a,b)$ such that $a$ and $b$ have the same number of elements.

If $R$ is an equivalence relation on a set $A$, and $(a,b)\in
R$, then we say that that $a$ and $b$ are *$R$-equivalent*. For every $a\in A$, the *equivalence class* of $a$, usually denoted by $[a]_R$, is the set of all elements of $A$ that are $R$-equivalent to $a$. The set of all $R$-equivalence classes is called the *quotient set* and is denoted by $A/R$. One can easily check that $A/R$ is a *partition* of $A$, that is, no element of $A/R$ is empty, any two elements of $A/R$ are disjoint, and every $a\in A$ belongs to (exactly) one element of $A/R$, namely the class $[a]_R$.

If $R$ is a binary relation, then one usually writes $aRb$ instead of $(a,b)\in R$.

A binary relation $R$ on a set $A$ is called *antisymmetric* if $a=b$ whenever $aRb$ and $bRa$. A relation $R$ on a set $A$ that is reflexive, antisymmetric, and transitive, is called a (reflexive) *partial order*. If we remove from $R$ all pairs $(a,a)$, for every $a\in A$, then we get a *strict* partial order. The $\subseteq$ relation on any set of sets is an example of a partial order. A partial order on a given set $A$ is usually represented by the symbol $\leq$, and the corresponding strict partial ordering by $<$. A partial order $\leq$ on a set $A$ with the additional property that either $a\leq b$ or $b\leq a$, for all elements $a$ and $b$ of $A$, is called a *total order*, or a *linear order*. The usual orderings of the set $\mathbb{N}$ of natural numbers, the set $\mathbb{Z}$ of the integers, the set $\mathbb{Q}$ of the rational numbers, or the set $\mathbb{R}$ of real numbers, are linear orders.

Notice that if $\leq$ is a linear order on a set $A$, and $B\subseteq A$, then $\leq \cap \, B^2$ is also a linear order on $B$. If $\leq$ is a linear order on a set $A$, then we say that $a\in A$ is the $\leq$-least element of $A$ if there is no $b\in A$ distinct from $a$ such that $b\leq a$. The number $0$ is the least element of $\mathbb{N}$, but $\mathbb{Z}$ has no least element.

A linear order $\leq$ on a set $A$ is a *well-order* if every non-empty subset of $A$ has a $\leq$-least element. Equivalently, if there is no infinite strictly descending sequence $$\ldots < a_2< a_1< a_0$$ of elements of $A$. Thus, the usual ordering of $\mathbb{N}$ is a well-order. But the usual order on $\mathbb{Z}$ is not, because it has no least element.

### 2. Functions

A ($1$-ary) *function* on a set $A$ is a binary relation $F$ on $A$ such that for every $a\in A$ there is exactly one pair $(a,b)\in F$. The element $b$ is called the *value* of $F$ on $a$, and is denoted by $F(a)$. And the set $A$ is called the *domain* of $F$. The notation $F:A\to B$ indicates that $F$ is a function with domain $A$ and values in the set $B$. For $n\geq 2$, an *$n$-ary function* on $A$ is a function $F:A^n\to B$, for some $B$.

A function $F:A\to B$ is *one-to-one* if for all elements $a$ and $b$ of $A$, if $a\ne b$, then $F(a)\ne F(b)$. And is *onto* if for every $b\in B$ there is some $a\in A$ such that $F(a)=b$. Finally, $F$ is *bijective* if it is one-to-one and onto. Thus, a bijection $F:A\to B$ establishes a one-to-one correspondence between the elements of $A$ and those of $B$, and $A$ is *bijectable* with $B$ if there is such a bijection. The *identity function* on a set $A$, denoted by $Id:A\to A$, and which consists of all the pairs $(a,a)$, with $a\in A$, is trivially a bijection.

Given functions $F:A\to B$ and $G:B\to C$, the *composition of $F$ and $G$*, written $G\circ F$, is the function $G\circ
F:A\to C$ whose elements are all pairs $(a,G(F(a)))$, where $a\in
A$. If $F$ and $G$ are bijections, then so is $G\circ F$.

### 3. Sets and formulas

The formal *language of set theory* is the first-order language whose only non-logical symbol is the binary relation symbol $\in$.

Given any formula $\varphi(x,y_1,\ldots ,y_n)$ of the language of set theory, and sets $A,B_1,\ldots ,B_n$, one can form the set of all those elements of $A$ that satisfy the formula $\varphi(x,B_1,\ldots ,B_n)$. This set is denoted by $\{ a\in A:
\varphi(a,B_1,\ldots ,B_n)\}$. The following are some examples

- ${\varnothing}=\{ a\in A: \neg a= a\}$
- $A=\{ a\in A: a=a\}$
- $A-B=\{ a\in A: \neg a \in B\}$.
- $A\cap B=\{ a\in A: a\in B\}$.

And if $B$ and $C$ are subsets of $A$, then

- $B\cup C=\{ a\in A: a\in B \vee a\in C\}$.

Given a subset $C\subseteq A\times B$, the *projection* of $C$ (on the first coordinate) is the set

> $\{ a\in A: \exists b\in B ((a,b)\in C)\}$.

It is not the case, however, that given any formula $\varphi(x,y_1,\ldots ,y_n)$, and sets $B_1,\ldots ,B_n$, one can form the set of all those sets that satisfy the formula $\varphi(x,B_1,\ldots ,B_n)$. For let $\varphi(x)$ be the formula $\neg x \in x$. If $A$ were the set of all sets that satisfy the formula, then $A\in A$ if and only if $\neg A \in A$. A contradiction! This contradiction is known as *Russell’s paradox*, after Bertrand Russell, who discovered it in 1901 (see the entry on Russell’s paradox).

### 4. Ordinals

The first ordinal number is ${\varnothing}$. Given an ordinal $\alpha$, the next bigger ordinal, called the (immediate) *successor* of $\alpha$, is the set $\alpha \cup \{ \alpha
\}$. Thus, the successor of $\alpha$ is just the set $\alpha$ together with one more element, namely, $\alpha$ itself. The *finite ordinal numbers* are those obtained by starting with ${\varnothing}$ and repeatedly taking the successor.

In set theory the *natural numbers* are defined as the finite ordinals. Thus,

- $0= {\varnothing}$
- $1= {\varnothing}\cup \{ {\varnothing}\}=\{
{\varnothing}\}$
- $2= \{ {\varnothing}\} \cup \{\{{\varnothing}\}\}=\{ {\varnothing},
\{ {\varnothing}\}\}$
- $3= \{ {\varnothing}, \{ {\varnothing}\}\}\cup \{ \{ {\varnothing},
\{ {\varnothing}\}\}\} =\{ {\varnothing}, \{ {\varnothing}\}, \{
{\varnothing}, \{ {\varnothing}\}\}\}$
- $\vdots$

Notice that $1=\{ 0\}$, $2=\{ 0,1\}$, $3=\{ 0,1,2\}$, and in general we have $n=\{ 0,1,2,\ldots ,n-1\}$. So, every natural number $n$ is just the set of its predecessors.

A set $A$ is *finite* if there is a one-to-one correspondence between some natural number $n$ and the elements of $A$, i.e., a bijection $F:n\to A$, in which case we say that $A$ has $n$ elements. A set is *infinite* if it is not finite.

The set of all finite ordinals is denoted by the Greek letter omega ($\omega$). Thus, $\omega$ is just the set $\mathbb{N}$ of natural numbers. $\omega$ is also an ordinal, the first infinite ordinal. Notice that $\omega$ is not the successor of any ordinal, and so it is called a *limit ordinal*. Once we have $\omega$ we can continue generating more ordinals by taking its successor $\omega \cup \{ \omega \}$, then its successor $(\omega \cup
\{\omega\}) \cup \{\omega \cup \{\omega \}\}$, and so on. All ordinal numbers greater than $0$ are produced in this way, namely, either by taking the successor of the last produced ordinal, or, if there is no such last ordinal, by taking the set of all the ordinals produced so far, as in the case of $\omega$ which yields a new limit ordinal. Note, however, that one cannot take the set of *all* ordinals, for then this set would be a new limit ordinal, which is impossible, since we already had them all.

As with finite ordinals, every infinite ordinal is just the set of its predecessors. One consequence of this is that the $\in$ relation is a strict well-order on any set of ordinals. Thus, for any ordinals $\alpha$ and $\beta$ we define $\alpha <\beta$ if and only if $\alpha \in \beta$. Then the associated reflexive well-order is defined as $\alpha \leq \beta$ if and only if $\alpha <\beta$ or $\alpha =\beta$. Let us now observe that $\alpha \subseteq
\beta$ if and only if $\alpha \leq \beta$.

### 5. Countable and uncountable sets

If $A$ is a finite set, there is a bijection $F:n\to A$ between a natural number $n$ and $A$. Any such bijection gives a *counting* of the elements of $A$, namely, $F(0)$ is the first element of $A$, $F(1)$ is the second, and so on. Thus, all finite sets are countable. An infinite set $A$ is called *countable* if there is a bijection $F:\omega \to A$ between the set of natural numbers and $A$. The set $\mathbb{N}$ of natural numbers is (trivially) countable. If $A$ is an infinite subset of $\omega$, then $A$ is also countable: for let $F:\omega
\to A$ be such that $F(n)$ is the least element of $A$ that is not in the set $\{ F(m)\in A: m< n\}$. Then $F$ is a bijection.

Every infinite subset of a countable set is also countable: for suppose $F:\omega \to A$ is a bijection and $B\subseteq A$ is infinite. Then the set $\{ n\in \omega: F(n)\in B\}$ is an infinite subset of $\omega$, hence countable, and so there is a bijection $G:\omega \to \{ n\in \omega : F(n)\in B\}$. Then the composition function $F\circ G:\omega \to B$ is a bijection.

The union of a countable set and a finite set is also countable. For given sets $A$ and $B$, which without loss of generality we may assume they are disjoint, and given bijections $F:\omega \to A$ and $G:n\to B$, for some $n<\omega$, let $H:\omega \to A\cup B$ be the bijection given by: $H(m)=G(m)$, for every $m<n$, and $H(m)=F(m-n)$, for every $n\leq m$.

Moreover, the union of two countable sets is also countable: since we have already shown that the union of a countable set and a finite set is also countable, it is enough to see that the union of two disjoint countable sets is also countable. So, suppose $A$ and $B$ are countable sets and $F:\omega \to A$ and $G:\omega \to B$ are bijections, then the function $H:\omega \to A\cup B$ consisting of all pairs $(2n,F(n))$, plus all pairs $(2n+1, G(n))$ is a bijection.

Thus, the set $\mathbb{Z}$, being the union of two countable sets, namely $$\mathbb{N}\cup \{ -1,-2,-3,-4,\ldots \}$$ is also countable.

The Cartesian product of two infinite countable sets is also countable. For suppose $F:\omega \to A$ and $G:\omega \to B$ are bijections. Then, using the fact that the function $J:\omega \times
\omega \to \omega$ given by $J((m,n))= 2^m(2n+1)-1$ is a bijection, one has that the function $H:\omega \to A\times B$ given by $H(2^m(2n+1)-1)=(F(m),G(n))$ is also a bijection.

Since any rational number is given by a pair of integers, i.e., a quotient $\frac{m}{n}$, where $m,n\in \mathbb{Z}$ and $n\ne 0$, the set $\mathbb{Q}$ of rational numbers is also countable.

However, Georg Cantor discovered that the set $\mathbb{R}$ of real numbers is not countable. For suppose, aiming for a contradiction, that $F:\omega \to \mathbb{R}$ is a bijection. Let $a_0=F(0)$. Choose the least $k$ such that $a_0<F(k)$ and put $b_0=F(k)$. Given $a_n$ and $b_n$, choose the least $l$ such that $a_n<F(l)<b_n$, and put $a_{n+1}=F(l)$. And choose the least $m$ such that $a_{n+1}<F(m)<b_n$, and put $b_{n+1}=F(m)$. Thus, we have $a_0<a_1<a_2<\cdots$ $\cdots
<b_2<b_1<b_0$. Now let $a$ be the limit of the $a_n$. Then $a$ is a real number different from $F(n)$, all $n$, which is impossible because $F$ is a bijection.

The existence of uncountable sets follows from a much more general fact, also discovered by Cantor. Namely, given any set $A$, the set of all its subsets, called the *power set* of $A$, and denoted by $\mathcal{P}(A)$, is not bijectable with $A$: for suppose that $F:A\to \mathcal{P}(A)$ is a bijection. Then the subset $\{ a\in A: \neg a \in F(a)\}$ of $A$ is the value $F(a)$ of some $a\in A$. But then $a\in F(a)$ if and only if $\neg a \in
F(a)$. Hence, if $A$ is any infinite set, then $\mathcal{P}(A)$ is uncountable.

There are also uncountable ordinals. The set of all finite and countable ordinals is also an ordinal, called $\omega_1$, and is the first uncountable ordinal. Similarly, the set of all ordinals that are bijectable with some ordinal less than or equal to $\omega_1$ is also an ordinal, called $\omega_2$, and is not bijectable with $\omega_1$, and so on.

#### 5.1 Cardinals

The *cardinality*, or size, of a finite set $A$ is the unique natural number $n$ such that there is a bijection $F:n\to A$.

In the case of infinite sets, their cardinality is given, not by a natural number, but by an infinite ordinal. However, in contrast with the finite sets, an infinite set $A$ is bijectable with many different ordinal numbers. For example, the set $\mathbb{N}$ is bijectable with $\omega$, but also with it successor $\omega \cup
\{\omega\}$: by assigning $0$ to $\omega$ and $n+1$ to $n$, for all $n\in \omega$, we obtain a bijection between $\omega \cup
\{\omega \}$ and $\omega$. But since the ordinals are well-ordered, we may define the cardinality of an infinite set as the least ordinal that is bijectable with it.

In particular, the cardinality of an ordinal number $\alpha$ is the least ordinal $\kappa$ that is bijectable with it. Notice that $\kappa$ is not bijectable with any smaller ordinal, for otherwise so would be $\alpha$. The ordinal numbers that are not bijectable with any smaller ordinal are called *cardinal numbers*. Thus, all natural numbers are cardinals, and so are $\omega$, $\omega_1$, $\omega_2$, and so on. In general, given any cardinal $\kappa$, the set of all ordinals that are bijectable with some ordinal $\leq \kappa$ is also a cardinal; it is the smallest cardinal bigger than $\kappa$.

The infinite cardinals are represented by the letter aleph ($\aleph$) of the Hebrew alphabet. Thus, the smallest infinite cardinal is $\omega =\aleph_0$, the next one is $\omega_1=\aleph_1$, which is the first uncountable cardinal, then comes $\omega_2=\aleph_2$, etc.

The cardinality of any set $A$, denoted by $|A|$, is the unique cardinal number that is bijectable with $A$. We saw already that $|\mathbb{R}|$ is uncountable, hence greater than $\aleph_0$, but it is not known what cardinal number it is. The conjecture that $|\mathbb{R}|=\aleph_1$, formulated by Cantor in 1878, is the famous *Continuum Hypothesis*.

### Further Readings

- Devlin, K., 1979, *Fundamentals of Contemporary Set Theory*, Undergraduate Texts in Mathematics, Springer, Second edition 1993, The Joy of Sets: Fundamentals of Contemporary Set Theory. Undergraduate Texts in Mathematics, New York: Springer.
- Enderton, H.B., 1977, *Elements of Set Theory*, New York: Academic Press.
- Jech, T. and K. Hrbaček, 1978 [1999], *Introduction to set theory*, New York: Marcel Dekker, 3rd edition 1999.

Copyright © 2023 by Joan Bagaria <*joan.bagaria@icrea.cat*>

Open access to the SEP is made possible by a world-wide funding initiative. The Encyclopedia Now Needs Your Support Please Read How You Can Help Keep the Encyclopedia Free

#### Browse

- Table of Contents
- What's New
- [Random Entry](https://plato.stanford.edu/cgi-bin/encyclopedia/random)
- Chronological
- Archives

#### About

- Editorial Information
- About the SEP
- Editorial Board
- How to Cite the SEP
- Special Characters
- Advanced Tools
- Accessibility
- Contact

#### Support SEP

- Support the SEP
- PDFs for SEP Friends
- Make a Donation
- SEPIA for Libraries

#### Mirror Sites

View this site from another server:

[ USA (Main Site) Philosophy, Stanford University ](https://plato.stanford.edu/)

- Info about mirror sites

The Stanford Encyclopedia of Philosophy is copyright © 2023 by [The Metaphysics Research Lab](https://mally.stanford.edu/), Department of Philosophy, Stanford University

Library of Congress Catalog Data: ISSN 1095-5054
