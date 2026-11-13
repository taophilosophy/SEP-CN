# Second-order and Higher-order Logic
**First published Thu Aug 1, 2019; substantive revision Sat Aug 31, 2024**

*Väänänen, Jouko*

Second-order logic has a subtle role in the philosophy of mathematics. It is stronger than first order logic in that it incorporates “for all properties” into the syntax, while first order logic can only say “for all elements”. At the same time it is arguably weaker than set theory in that its quantifiers range over one limited domain at a time, while set theory has the universalist approach in that its quantifiers range over all possible domains. This stronger-than-first-order-logic/weaker-than-set-theory duality is the source of lively debate, not least because set theory is usually construed as based on first order logic. How can second-order logic be at the same time stronger and weaker? To make the situation even more complex, it was suggested early on that in order that the strength of second-order logic can be exploited to its full extent and in order that “for all properties” can be given an exact interpretation, a first order set-theoretical background has to be assumed. This seemed to undermine the claimed strength of second-order logic as well as its role as the primary foundation of mathematics. It also seemed to attach second-order logic to aspects of set theory which second-order logic might have wanted to bypass: the higher infinite, the independence results, and the difficulties in finding new convincing axioms. Setting aside philosophical questions, it is undeniable and manifested by a continued stream of interesting results, that second-order logic is part and parcel of a logician’s toolbox.

## 1. Introduction

Second-order logic[^note-1] was introduced by Frege in his Begriffsschrift (1879) who also coined the term “second order” (“*zweiter Ordnung*”) in (1884: §53). It was widely used in logic until the 1930s, when set theory started to take over as a foundation of mathematics. It is difficult to say exactly why this happened, but set theory has certain simplicity in being based on one single binary predicate $x\in y$, compared to second- and higher-order logics, including type theory. Discussion among philosophers of the merits of second-order logic especially in comparison to set theory continues to this day (Shapiro 1991)[^shapiro-1991]. Meanwhile second-order logic has become a standard tool of computer science logic, finite model theory in particular. Central questions of theoretical computer science, such as the P = NP? question, can be seen as questions about second-order logic in the finite context.

Ultimately second-order logic is just another formal language. It can be given the standard treatment making syntax, semantics and proof theory exact by working in a mathematical metatheory which we choose to be set theory. It would be possible to use second-order logic itself as metatheory, but it would be more complicated, simply because second-order logic is less developed than set theory.

The distinction between first order logic and second-order logic is easiest to understand in elementary mathematics. Let us consider number theory. The objects of our study are the natural numbers 0, 1, 2,… and their arithmetic. With first order logic we can formulate statements about number theory by using atomic expressions $x = y,$ $x+y = z$ and $x\times y = z$ combined with the propositional operations $\land,$ $\neg,$ $\lor,$ $\to$ and the quantifiers $\forall x$ and $\exists x$. Here the variables *x*, *y*, *z*,… are thought to range over the natural numbers. With second-order logic we can express more: we have variables *x*, *y*, *z*,… as in first order logic for numbers. In addition we have variables *X*, *Y*, *Z*,… for properties of numbers and relations between numbers as well as quantifiers $\forall X$ and $\exists X$ for these variables. We have the atomic expressions of first order logic and also new atomic expressions of the form $X(y_1,\ldots, y_n)$.

An interesting and much studied question arises: what properties of natural numbers can be expressed in first order logic and what can be expressed in second-order logic? The question is equally interesting if “expressed” is replaced by “proved”, once a suitable proof system is given in both cases. We can replace natural numbers by some other mathematical context, for example real numbers, complex numbers, and so on.

With just the constant $0$ and the unary function $n \mapsto n^+$ (where $n^+$ means $n+1$) we can express in second-order logic the *Induction Axiom*

$$\tag{1}\label{ind} \forall X\left(\left[X(0) \land \forall y\left(X(y) \to X(y^+)\right)\right] \to \forall y\,X(y)\right), $$

of natural numbers. This, together with the axioms $\forall x\,\neg(x^+=0)$ and $\forall x\,\forall y(x^+=y^+\to x=y)$ characterizes the natural numbers with their successor operation up to isomorphism. In first order logic any theory which has a countably infinite model has also an uncountable model (by the Upward Löwenheim Skolem Theorem). Hence (\ref{ind}) cannot be expressed in first order logic. Another typical second-order expression is the *Completeness Axiom* of the linear order $\le$ of the real numbers:

$$\tag{2}\label{comp} \begin{align} &\forall X\left(\left[\exists y\,X(y) \land \exists z\,\forall y(X(y) \to y \le z)\right]\right. \to\\ &\qquad\left.\exists z\,\forall y\left(\exists u\left(X(u) \land y \le u\right) \lor z \le y\right)\right), \end{align}$$

This, together with the axioms of ordered fields characterizes the ordered field of real numbers up to isomorphism. In first order logic any countable theory which has an infinite model has also a countable model (by the Downward Löwenheim Skolem Theorem). Hence, again, (\ref{comp}) cannot be expressed in first order logic.

To early logicians it seemed natural to use second-order logic on a par with first order logic, as if there were not much difference. This included Russell, Löwenheim, Hilbert, and Zermelo. Essentially only Skolem emphasized the difference (see Moore 1988 for the emergence of first order logic)[^moore-1988]. In 1929 Gödel proved his Completeness Theorem and the next year his Incompleteness Theorem. It became gradually obvious that second-order logic is very different from first order logic. One of the first indicators was the incompleteness phenomenon. Gödel showed that any effective axiomatization of number theory is incomplete. On the other hand, there was a simple finite categorical—hence complete (§10)—axiomatization of the structure $(\oN,$ $+,$ $\times)$ in second-order logic (see also the discussion related to (\ref{ind})). This showed that there cannot be such a complete axiomatization of second-order logic as there was for first order logic. What became known in the case of first order logic as Gödel’s Completeness Theorem simply cannot hold for second-order logic.

The situation changed somewhat when Henkin proved the Completeness Theorem for second-order logic with respect to so-called general models (§9). Now it became possible to use second-order logic in the same way as first order logic, if only one keeps in mind that the semantics is based on general models. The ability of second-order logic to characterize mathematical structures up to isomorphism does not extend to general models (except in the form of internal categoricity—see §10). Any second-order theory, in a countable vocabulary, with an infinite general model has general models of *all* infinite cardinalities, and therefore cannot be categorical in the context of general models. We shall discuss general models and the related Henkin models in §9.

## 2. The Syntax of Second-Order Logic

A *vocabulary* in second-order logic is just as a vocabulary in first order logic, that is, a set *L* of *relation*, *function* and *constant* symbols. Each relation and function symbol has an *arity*, which is a positive natural number.

Second-order logic has several kinds of *variables*. It has *individual* *variables* denoted by lower case letters $x, y, z, \ldots$ possibly with subscripts. It has *property* and *relation* *variables* denoted by upper case letters $X,Y,Z,\ldots$ possibly with subscripts. Finally, it has *function variables* denoted by upper case letters $F, G, H, \ldots$ possibly with subscripts. Sometimes function variables are omitted as, after all, functions are special kinds of relations. Each relation and function variable has an arity, which is a positive natural number. We identify property variables with 1-ary relation variables.

It is noteworthy that although we have property variables we do not have variables for properties of properties. Such variables would be part of the formalism of third order logic, see §12.

The *terms* of second-order logic are defined recursively as follows: Constant symbols and individual variables are terms. If $t_1,\ldots,t_n$ are terms, *U* is an *n*-ary function symbol and *F* is an *n*-ary function variable, then $U(t_1,\ldots,t_n)$ and $F(t_1,\ldots,t_n)$ are terms. Note that terms denote individuals, not relations or properties. Thus *X* alone is not a term but *x* is.

The *atomic formulas* of second-order logic are defined from terms as follows: If *t* and $t'$ are terms, then $t = t'$ is an atomic formula. If *R* is an *n*-ary relation symbol and $t_1,\ldots,t_n$ are terms, then $R(t_1,\ldots,t_n)$ is an atomic formula. If *X* is an *n*-ary relation variable, then also $X(t_1,\ldots,t_n)$ is an atomic formula. The intuitive meaning of $X(t_1,\ldots,t_n)$ is that the elements $t_1,\ldots, t_n$ are in the relation *X* or are *predicated* by *X*. We do not allow atomic formulas of the form $X = Y$, although they would have an obvious meaning. We achieve the same effect by using quantifiers.

**Definition 1** The *formulas* of second-order logic are defined as follows: Atomic formulas are formulas. If $\phi$ and $\psi$ are formulas, then $\neg\phi$, $\phi\land \psi$, $\phi\lor \psi$, $\phi \to \psi$ and $\phi \leftrightarrow \psi$ are formulas. If $\phi$ is a formula, *x* an individual variable, *X* a relation variable and *F* a function variable, then $\exists x\phi$, $\forall x\phi$, $\exists X\phi$, $\forall X\phi, \exists F\phi$ and $\forall F\phi$ are formulas.

It is interesting to note that in second order logic we can actually *define* the identity $t=t'$ as $\forall X(X(t)\leftrightarrow X(t'))$ and prove the familiar axioms of identity from properties of the implication.

An important special case is *monadic second-order logic* where no function variables are allowed and the relation variables are required to be monadic (a.k.a. unary), i.e., of arity one.

We did not take $X=Y$ as an atomic formula (although we could have) but having introduced the quantifiers we can use

$$\tag{3}\label{XY} \forall x_1\ldots \forall x_n(X(x_1,\ldots,x_n)\leftrightarrow Y(x_1,\ldots,x_n)) $$

as a substitute for $X=Y$. The advantage of taking $X=Y$ as a basic atomic formula would be that using (\ref{XY}) brings along extra quantifiers. Sometimes it is interesting to minimize the number of quantifiers in a formula. Also, (\ref{XY}) gives the identity $X=Y$ an *extensional* flavour in contrast to a possibly different *intensional* construal.

The concepts of a *free* and *bound* *occurrence* of a variable in a formula are defined in the usual way. A formula is called a *sentence* if it has no free variables. The concept of a term being *free* *for* a variable in a formula is defined as in first order logic.

## 3. The Semantics of Second-Order Logic

In order to define the semantics of second-order logic we have to agree what our *metalanguage* is. This fact has nothing to do with second-order logic but is rather a general feature of semantics (Tarski 1933 [1956])[^tarski-1933]. The most commonly used metalanguage for second-order logic is *set theory*. We thus give a set-theoretical interpretation of second-order logic, interpreting “properties” as sets in a domain which itself is a set. This is the most common choice and brings out the main features of second-order logic. We cannot interpret *all* properties by sets, e.g. the property of being identical to oneself. But if the domain that the individual variables range over is taken to be a set, then we can meaningfully interpret properties of individuals in that domain as sets. If we want to interpret second-order logic in a domain which is too large to be a set, we can use the set-theoretical concept of a class (see entry on set theory for more on classes).

We use the same concept of an *L*-structure (or equivalently, an *L*-model) as in first order logic. That is, an *L*-*structure* $\mm$ has a *domain* *M*, which is any non-empty set, an *interpretation* $c^\mm \in M$ of any constant symbol *c* of *L*, an interpretation $R^\mm \subseteq M^n$ of any *n*-ary relation symbol *R* of *L*, as well as an interpretation $H^\mm : M^n \to M$ of any *n*-ary function symbol *H* of *L*. In principle, the domain could be a class but we disregard this possibility here. For a discussion on the set/class distinction in this context, we refer to Shapiro (1991, p. 16).

**Convention:** Whenever we use upper case Fraktur letters, such as $\mm,\mn$ etc, to name a structure, we use the upper case Italic versions of those letters, such as $M,N$ etc, to name the domain of the structure.

Given an *L*-structure $\mm$, an *assignment* is a function *s* from variables to the domain *M* of $\mm$ such that: if *x* is an individual variable, then $s(x) \in M$; if *X* is relation variable of arity *n*, then $s(X) \subseteq M^n$; if *F* is function variable of arity *n*, then $s(F) : M^n \to M$. We use $s(P/X)$ to denote the assignment which is otherwise as *s* except that the value at *X* has been changed to *P*. Similarly $s(a/x)$ and $s(f/F)$.

Note that $0$-ary relation variables are essentially propositions. Their interpretations under an assignment are the truth values (true, false). $0$-ary function variables are essentially individual variables as an assignment maps a $0$-ary function symbol simply to an element of $M$. A $0$-ary relation symbol or variable is at the same time an atomic formula and a non-logical symbol. We disregards in the current presentation this potential notational confusion.

The value $t^\mm\langle s\rangle$ of a term *t* in a model $\mm$ under the interpretation *s* is defined as in first order logic.

The concept $\mm\models\phi$ of the *truth* of the sentence $\phi$ in $\mm$ can now be defined by first defining the auxiliary concept $\mm\models_s\phi$ of the assignment $s$ *satisfying* $\phi$ in $\mm$ (see entry on Tarski’s truth definitions for more details):

**Definition 2 (Tarski’s Truth Definition)** The truth definition for second-order logic extends the respective truth definition for first order logic by the clauses:

1. $\mm \models_s X(t_1,\ldots,t_n)$ iff $(t^\mm_1 \langle s\rangle,\ldots,t^\mm_n \langle s\rangle) \in s(X)$, if $X$ is $n$-ary.
2. $\mm\models_s \exists X\,\phi$ iff $\mm\models_{s(P/X)} \phi$ for some $P \subseteq M^n$, if $X$ is $n$-ary.
3. $\mm\models_s \exists F\,\phi$ iff $\mm\models_{s(f/F)} \phi$ for some $f:M^n \to M$, if $F$ is $n$-ary.

and similarly for the universal quantifiers. For a sentence $\phi$ we define $\mm\models\phi$ to mean $\mm\models_s\phi$ for all (equivalently some) *s*, and then say $\phi$ is *true* in $\mm$.

In clause 1 of the above definition we follow the common practice of giving a set-theoretical interpretation to the predication $X(t_1,\ldots,t_n)$. Having interpreted *X* as a subset of $M^n$, we interpret predication $X(t_1,\ldots,t_n)$ as membership $(t^\mm_1 \langle s\rangle,\ldots,t^\mm_n \langle s\rangle) \in s(X)$. In clause 2 we interpret quantification over properties and relations as quantification over subsets of the cartesian product $M^n$. Respectively, in clause 3 we interpret quantification over functions as quantification over sets that are functions $M^n\to M$ in the set-theoretical sense.

Now that the semantics of second-order logic is defined we can define what it means for a formula $\phi$ to be *valid* and for two formulas $\phi$ and $\psi$ to be *logically equivalent*. As in logic in general, we say that $\phi$ is (logically) valid if $\mm\models_s\phi$ holds for all $\mm$ and all *s*. Likewise, we define $\phi$ and $\psi$ to be logically equivalent, $\phi\equiv\psi$, if $\phi\leftrightarrow\psi$ is valid. Two models $\mm$ and $\mn$ are said to be *second-order equivalent*, in symbols $\mm\equiv_{L^2}\mn$ if for all sentences $\phi$ we have $\mm\models\phi\iff\mn\models\psi$.

The truth definition involves the concepts “for some $P \subseteq M^n$” and “for some $f:M^n \to M$”. Since we assume set theory as our metalanguage, we can interpret these in the sense of set theory. Thus we interpret “for some $P \subseteq M^n$” as “for some *set* $P \subseteq M^n$” and “for some $f:M^n\to M$” as “for some *set* which is a function $f:M^n\to M$”.

For infinite *M* the collection of subsets of $M^n$ and the set of functions $M^n\to M$ are famously complex. Currently set theory (ZFC) cannot even decide how *many* subsets of an infinite set there are. The situation is quite different with first order logic. The respective concept “for some $a \in M$” is unproblematic, relatively speaking. Of course, depending on what *M* is, “for some $a \in M$” can be quite problematic too. To reflect the difficulties involved with finding a $P \subseteq M^n$ or an $f:M^n \to M$ we sometimes say we “guess” a $P \subseteq M^n$ or an $f:M^n \to M$.

When we use set theory as the metatheory for the semantics of *first order* logic, the reliance on the metatheory is of a lower degree than when we use set theory as the metatheory for the semantics of *second order* logic. The central concept, which explains the difference, is that of *absoluteness*. For details, see §6.

### 3.1 The Ehrenfeucht-Fraïssé game of second-order logic

The *Ehrenfeucht-Fraïssé game* is a game-theoretic tool for investigating to what extent two models are similar (see entry on logic and games for a general introduction to Ehrenfeucht-Fraïssé games). Two isomorphic models would be very similar but normally we are interested in similarity of models that are not isomorphic. The Ehrenfeucht-Fraïssé game of second-order logic characterizes $\ma\equiv_{L^2}\mn$, i.e. the proposition that exactly the same second-order sentences are true in $\ma$ and $\mb$, just as the Ehrenfeucht-Fraïssé game of first order logic characterizes the first order elementary equivalence $\ma\equiv\mn$. See the entry on first-order model theory for more on elementary equivalence.

For simplicity we disallow function and constant symbols as well as function variables in this section. Suppose $\ma$ and $\mb$ are two models of the same finite relational vocabulary. In the game which we denote by $G^2_n(\ma,\mb)$ two players I and II pick one at a time subsets (or elements) of *A* or subsets (or elements) of *B*. During round *i* of the game player I can pick a relation $A_i$ on *A* (or an element $a_i$ of *A*) and then player II has to pick a relation $B_i$ on *B* of the same arity as $A_i$ (or an element $b_i$ of on *B*) and vice versa: Player I can instead pick a relation $B_i$ on *B* (or an element $b_i$ of *B*) and then II picks a relation $A_i$ on *A* of the same arity as $B_i$ (or an element $a_i$) of *A*. After *n* rounds the pairs of played elements $(a_i,b_i)$ form a binary relation *R* on $A\times B$. If this relation is a partial isomorphism of the structures $\ma$ and $\mb$ expanded by the played relations $A_i$ and $B_i$, i.e., it preserves atomic formulas and their negations, we say that II has won. The models $\ma$ and $\mb$ satisfy the same second-order sentences if and only if for each $n\in \oN$ Player II has a winning strategy in $G^2_n(\ma,\mb)$. A model class (i.e. a class of models of a fixed vocabulary, closed under isomorphisms) *K* is definable in second-order logic if and only if there is an *n* such that if $\ma\in K$ and Player II has a winning strategy in the $G^2_n(\ma,\mb)$, then $\mb\in K$.

The first order version $G^1_n(\ma,\mb)$, where players play only individual elements, i.e., no relations are played, is very useful in working with first order logic. Unfortunately the game $G^2_n(\ma,\mb)$ is much more complex. It is very difficult to invent winning strategies for Player II except in the trivial case when $\ma\cong\mb$. If Player I plays a binary relation *R* on *A*, Player II should be able to play a binary relation $R'$ on *B* such that whatever challenges Player I makes in the rest of the game, even involving new binary relations, the relations *R* and $R'$ look similar. If $V=L$, then countable second-order equivalent models (with a finite vocabulary) are actually isomorphic (Ajtai 1979)[^ajtai-1979]. For details, see §10. Thus consistently in countable models there is no other winning strategy for Player II than an isomorphism. Perhaps this explains why the game is not as useful in second-order logic as it is in first order logic. However, if we restrict to monadic second-order logic, which in terms of the Ehrenfeucht-Fraïssé game means restricting the game to *unary* predicates, the situation changes. A unary predicate just divides the model into two parts. If Player I divides *A* into two parts, Player II should find a similar division in *B*. This is more reasonable and there actually are useful strategies for Player II. For examples in the finite context see §16.

## 4. Properties of Second-Order Formulas

Many syntactic operations that we are used to in first order logic work equally well in second-order logic. One such is the operation of *relativization*, in which we want to limit what a formula expresses to a fixed part of the universe. For example, we may consider models where a certain unary predicate *U* is used for the set of natural numbers. Then we relativize our axioms of arithmetic to the predicate *U*. Some other part of the model may be used for the power set of the set of natural numbers. Then we relativize our axioms of power set (see §5.3) to that part, and so on.

If $\mm$ is a structure and $A\subseteq M$, then $\mm^{A}$ is obtained by restricting the relations $R^\mm$ and functions $F^\mm$ to *A*. This does not always result in a structure but if it does, it is called the *relativization* of $\mm$ to *A*. Suppose $\phi=\phi(x_1,\ldots,x_n,X_1,\ldots,X_m,F_1,\ldots,F_k)$ is a second-order formula and *U* is a unary relation variable. There is a second-order formula $\phi^{U}$, the relativization of $\phi$ to *U*, such that for all $\mm$ for which $\mm^{U^\mm}$ is a structure:

$$\mm\models\phi^{U}\iff \mm^{U^\mm}\models\phi. $$

Intuitively, $\phi^{U}$ says about $U^\mm$ what $\phi$ says about *M*. To obtain $\phi^{U}$ from $\phi$ one restricts all the first order quantifiers to elements of *U* and second-order quantifiers to subsets, relations and functions on *U*.

Hierarchies based on quantifier structure are a useful method to compare the definability of concepts in different systems. In first order logic it was observed very early on that formulas can be brought into a logically equivalent *Prenex Normal Form* in which all quantifiers occur in the beginning of the formula. This is possible also in second-order logic and the proof is essentially the same. Moreover, using the equivalence (which is reminiscent of a principle of set theory called Axiom of Choice, to which we return in Section 5.4., since in the below formula the relation $Y$ in a sense chooses one $X$ for each $x$ and puts them together into one relation $Y$ – see entry on Axiom of Choice for more on the topic.)

$$\forall x\,\exists X\,\phi\equiv \exists Y\,\forall x\,\phi', $$

where the arity of *Y* is one higher than the arity of *X*, and $\phi'$ is obtained from $\phi$ by replacing everywhere $X(t_1,\ldots,t_n)$ by $Y(x,t_1,\ldots,t_n)$, one can bring every second-order logic formula to a logically equivalent normal form

$$\tag{4}\label{qqq} Q_1X_1\ldots Q_nX_n\phi, $$

where each $Q_i$ is either $\exists$ or $\forall$ and $\phi$ is first order. That is, all second order quantifiers of the formula are in the front.

*Table 1:*

| Notation | The $Q_i$ in (\ref{qqq}) are: |
| --- | --- |
| $\Sigma^1_1$ | All existential |
| $\Pi^1_1$ | All universal |
| $\Sigma^1_2$ | First existential, then universal |
| $\Pi^1_2$ | First universal, then existential |
| $\vdots$ | $\vdots$ |

| Notation | The formula is logically equivalent to: |
| --- | --- |
| $\Delta^1_1$ | Both $\Sigma^1_1$ and $\Pi^1_1$ formulas |
| $\Delta^1_2$ | Both $\Sigma^1_2$ and $\Pi^1_2$ formulas |
| $\vdots$ | $\vdots$ |

Table 1: The hierarchy of second-order formulas.

By restricting what kind of quantifiers the sequence $Q_1X_1\ldots Q_nX_n$ of the Prenex Normal Form (\ref{qqq}) can contain we obtain the classes of $\Sigma^1_n$-, $\Pi^1_n$- and $\Delta^1_n$-formulas, as indicated in Table 1. For example, the second-order formulas (1) and (2) are $\Pi^1_1$-formulas.

We have considered above only quantifiers that bind relation variables but the situation is exactly the same if we had bound function variables.

These classes of formulas have some obvious closure properties: They are all closed, up to logical equivalence, under $\land , \lor$, and first order quantifiers. Moreover, the hierarchy is proper in the sense that for all $n\ge 1$

$$\tag{5}\label{kurat} \Sigma^1_n \nsubseteq \Pi^1_n\text{ and } \Pi^1_n \nsubseteq \Sigma^1_n, $$

which can be proved with a diagonalisation argument. The classes $\Delta^1_n$ are closed under $\land , \lor, \neg$ and first order quantifiers. By Craig’s Interpolation Theorem, $\Delta^1_1$-formulas are logically equivalent to first order formulas [^note-2].

There is a sense in which $\Pi^1_1$, or equivalently $\Sigma^1_1$, already has the full power of second-order logic, although the above hierarchy result (\ref{kurat}) shows that this cannot literally be true. To see this, i.e., to see what the reduction of second-order logic to its $\Pi^1_1$-part means, let *L* be a vocabulary, *E* a binary and *U* a unary relation symbol, both not in *L*. Let $\theta$ be the second-order $\Pi^1_1$-formula

$$\tag{6}\label{ex6} \forall X(\phi_1\land\phi_2\land\phi_3), $$

where

$$\begin{align} \phi_1&\text{ is }\quad \forall x\,\forall y(\forall z(E(z,x)\leftrightarrow E(z,y))\to x=y)\\ \phi_2&\text{ is }\quad \forall x\,\forall y(E(x,y)\to (U(x)\land\neg U(y)))\\ \phi_3&\text{ is }\quad \forall x (X(x)\to U(x))\to\exists y\,\forall z(X(z)\leftrightarrow E(z,y)). \end{align} $$

It is easy to see[^note-3] that models of $\theta$ are, up to isomorphism, models $\mm$ where $M=U^\mm\cup\P(U^\mm)$, $U^\mm\cap\P(U^\mm)=\emptyset$ and for all $a,b\in M$, $E^\mm(a,b)\leftrightarrow a\in b$. In such a model monadic second-order formulas $\phi$ over $U^\mm$ can be reduced to first order formulas $\phi^*$ over *M*. This reduction, due to Hintikka (1955) and further developed by Montague (1963), shows that $\Pi^1_1$-formulas alone are enough to express any second-order property with extra predicates. The idea can be extended to third and higher order logic, and also to non-monadic second-order logic.

As a consequence, checking the validity of a second-order sentence $\phi$ can be recursively reduced to checking the validity of the $\Sigma^1_1$-sentence $\theta\to\phi^*$. Likewise checking whether a second-order sentence $\phi$ has a model of cardinality $\kappa$ can be reduced to asking whether the $\Pi^1_1$-sentence $\theta\land\phi^*$ has a model of cardinality $2^\kappa$. This means that the Löwenheim number[^note-4] and the Hanf number[^note-5] of the entire second-order logic are the same as those of the fragment $\Pi^1_1$.

Summing up, upon first inspection the levels $\Sigma^1_n$ and $\Pi^1_n$ of the hierarchy of second-order formulas grow strictly in expressive power as *n* increases, but a more careful analysis reveals that already the first level $\Sigma^1_1\cup \Pi^1_1$ has the power of all the levels $\Sigma^1_n, \Pi^1_n$ even if the power is somewhat implicit and needs to be brought to light.

In set theory there is the *Levy-hierarchy* of $\Sigma_n$- and $\Pi_n$-formulas (Lévy 1965)[^lévy-1965]. Formulas where all quantifiers are bounded, i.e., of the form $\forall x\in y$ or of the form $\exists x\in y$ for some *x* and *y*, are called $\Sigma_0$ or equivalently $\Pi_0$. Formulas of the form $\forall x\,\phi$, where $\phi$ is $\Sigma_n$, are called $\Pi_{n+1}$. Formulas of the form $\exists x\,\phi$, where $\phi$ is $\Pi_n$, are called $\Sigma_{n+1}$. This is a strict hierarchy roughly for the same reason why the hierarchy of second-order $\Sigma^1_n$- and $\Pi^1_n$-formulas is strict. But there is no known method to reduce the truth of an arbitrary formula to the truth of a formula on the $\Sigma_1\cup\Pi_1$ level. In fact, if the decision problem, Löwenheim-Skolem number and Hanf number are suitably defined for $\Sigma_n\cup \Pi_n$-formulas of set theory, the decision problem gets more and more complicated, and the numbers obtained get bigger and bigger as *n* increases (see Theorem 4; Väänänen 1979)[^väänänen-1979].

The hierarchy $\Sigma_n^1\cup \Pi_n^1$ inside second-order logic and the hierarchy $\Sigma_n\cup\Pi_n$ in set theory, are further compared to each other in §7.

## 5. The Infamous Power of Second-Order Logic

### 5.1 Putting distance between second- and first-order logic

Second-order logic has some remarkable qualities which we will now uncover in detail. Above we characterized the structure of the natural numbers by means of (\ref{ind}). This application of second-order logic is perhaps the most famous and most important. We now reformulate this in a slightly more general form in order to get more power out of it. Suppose *U* is a unary relation variable (“the set of natural numbers”), *G* a unary function variable (“the successor function”), and *z* an individual variable (“the zero”). Let $\theta_{\textrm{PA}}(U,G,z)$ be the sentence

$$\tag{7} \begin{align} &U(z)\land{}\\ &\forall x(U(x)\to(U(G(x))\land\neg G(x)=z))\land{}\\ &\forall x\,\forall y((U(x)\land U(y)\land G(x)=G(y))\to x=y)\land{}\\ &\forall X([X(z) \land \forall x((U(x)\land X(x)) \to X(G(x)))] \to {}\\ &\forall x(U(x)\to X(x))), \end{align} $$

Then $(N,A,g,a)\models\theta_{\textrm{PA}}(U,G,z)$ if and only if $(N,A,g,a)$ is isomorphic to a structure $(M,\oN,s,0)$ where $\oN\subseteq M$ and $s(n)=n+1$. Thus we have used second-order logic to say that the *U*-part of any model of $\theta_{\textrm{PA}}(U,G,z)$, together with the function *G* and the individual *z* are isomorphic to the natural numbers $\oN$ with their successor function and zero. There are many ways to see that no first order sentence can have this property. For example, by the Compactness Theorem such a sentence would have also a *non-standard* model where some element is different from each in the sequence *z*, $G(z)$, $G(G(z))$, $G(G(G(z)))$, $\ldots$. Such a model cannot be isomorphic to the natural numbers $\oN$ with their successor function and zero. Hereupon we may conclude that the Compactness Theorem does not hold for second-order logic in the form that it holds for first order logic.

In models of $\theta_{\textrm{PA}}(U,G,z)$ the formula $\theta_+(U,G,z,H)$

$$\left\{\begin{array}{l} \forall x(U(x)\to H(x,z)=x)\land\\ \forall x\,\forall y(U(x)\to (U(y)\to H(x,G(y))=G(H(x,y))))\\ \end{array}\right. $$

and the formula $\theta_\times(U,G,z,H,J)$

$$\left\{\begin{array}{l} \forall x(U(x)\to J(x,z)=z)\land\\ \forall x\,\forall y(U(x)\to (U(y)\to J(x,G(y))=H(J(x,y),x)))\\ \end{array}\right. $$

define unique functions $m+n=H(m,n)$ and $m\cdot n=J(m,n)$. A first order sentence $\phi(+,\cdot,0)$ of arithmetic is true in $(\oN,+,\cdot,0)$ if and only if

$$\begin{align} &\forall U\, \forall G\, \forall z\, \forall H\, \forall J \\ &\ \left(\left( \theta_{\textrm{PA}} (U,G,z) \land \theta_+(U,G,z,H) \land \theta_\times(U,G,z,H,J) \right) \to (\phi(H,J,z))^{U}\right) \end{align} $$

is valid. We know that truth of first order sentences in $(\oN,+,\cdot,0)$ is undecidable, and even non-arithmetical by results of Gödel (1931 [1986: 144–195]) and Tarski (1933 [1956]). This shows that second-order logic is not completely axiomatizable by effective means, or decidable even in the empty vocabulary. That is, there is no decidable second-order theory with an infinite model. This is in sharp contrast to first order logic where the following theories are decidable: first order logic with empty vocabulary, first order logic with monadic predicates, dense linear order, Pressburger arithmetic (first order theory of $(\oN,+,0)$), real closed fields (first order theory of $(\oR,+,\cdot,0,1)$), theory of algebraically closed fields, and the first order theory of $(\oC,+,\cdot,0,1)$. In second-order logic none of the respective second-order theories are decidable. However, if we restrict second-order logic to *monadic* second-order logic, we obtain many important decidable theories (see §8).

### 5.2 The collapse of the Completeness Theorem

The Completeness Theorem is one of the cornerstones of our understanding of first order logic. Also many extensions of first order logic have a Completeness Theorem, most notably the extension of first order logic by the generalized quantifier “There are uncountably many” and the infinitary language $L_{\omega_1\omega}$. We shall now see that there is no hope of a Completeness Theorem for second-order logic. Later in §9.1 we shall modify the semantics so that a Completeness Theorem can be proved.

Behind the failure of the Completeness Theorem is the fact that second-order logic is—almost by definition—able to say that a set is the power set of another set. What this means is the following: Let *L* be a vocabulary. Let *E* be a binary and *U* a unary relation symbol, both not in *L*. Let $\theta_{\textrm{Pow}}(U,E)$ be the second-order formula (\ref{ex6}). Let us consider the conjunction

$$\tag{8}\label{papow} \theta_{\textrm{PA}}(U,G,z)\land\theta_{\textrm{Pow}}(U,E). $$

Models of this formula are, up to isomorphism, of the form $(M,\in,N,g,a)$, where $\P(N)=M$, $N\cap\P(N)=\emptyset$ and $N$ is countably infinite. Thus the models are necessarily uncountable. This shows that second-order logic, unlike first order logic, has sentences with models but only uncountable ones. Thus the Downward Löwenheim-Skolem Theorem fails for second-order logic, as we already noted above. Combining (\ref{papow}) with the observations in §5.1 yields the following result (by validity we mean the set of Gödel numbers of valid formulas):

**Theorem 3 (Hintikka 1955; Montague 1963)[^hintikka-1955][^montague-1963]** Validity in second-order logic is not second-order definable over $(\oN,+,\cdot,0)$.

In consequence, validity in second-order logic is not $\Sigma^1_n$ for any *n*. Since building power sets in the style of $\theta_{\textrm{Pow}}(U,E)$ can be iterated, we can see that validity in second-order logic is not $\Sigma^m_n$ for any *m* and *n*. We extend this result further below in Theorem 6.

### 5.3 “Set theory in sheep’s clothing”

Second-order logic hides in its semantics some of the most difficult problems of set theory. In the words of Resnik (1988: 75):

> In Philosophy of Logic [Quine 1970][^quine-1970], W. V. Quine summed up a popular opinion among mathematical logicians by referring to second-order logic as “set theory in sheep’s clothing”.

Let us see where this opinion might come from. First we observe that a very simple, indeed a very basic, second-order formula can say that two sets have the same cardinality: Suppose *P* and *R* are unary relation variables. Let $\theta_{\le}(P,R)$ be the formula

$$ \exists F\left(\forall x\,\forall y\left( (F(x)=F(y)\to x=y) \land(P(x)\to R(F(x)) \right)\right). $$

Now $\mm\models_s\theta_\le(P,R)$ if and only if $|s(P)|\le |s(R)|$. Let $\theta_{\textrm{EQ}}(P,R)$ be the formula $\theta_{{\le}}(P,R)\land \theta_{{\le}}(R,P)$. Now $\mm\models_s\theta_{\textrm{EQ}}(P,R)$ if and only if $|s(P)|=|s(R)|$. Let $\theta'_{\textrm{EC}}(R)$ be

$$ \exists F \forall x\,\forall y((F(x)=F(y)\to x=y)\land R(F(x))). $$

Now $\mm\models_s\theta'_{\textrm{EC}}(R)$ if and only if the sets *M* and $s(R)$ have the same cardinality. We will use these formulas to launch an attack on the Continuum Hypothesis, the notorious problem of set theory, proved independent of ZFC by Cohen in 1963 (Cohen 1966)[^cohen-1966].

Let $\theta_{\textrm{CH}}$ be the sentence

$$\tag{9}\begin{align} &\exists E\,\exists U\,\exists G\,\exists z \\ &\ \left( \theta_{\textrm{Pow}}(E,U) \land\theta_{\textrm{PA}}(U,G,z) \land \forall Y(\theta'_{\textrm{EC}}(Y)\lor\theta_{\le}(Y,U)) \right). \end{align}$$

Now $\theta_{\textrm{CH}}$, which is a sentence of the empty vocabulary, has a model if and only if the Continuum Hypothesis CH holds. Similarly, there is a sentence $\theta_{\neg \textrm{CH}}$, which has a model if and only if the Continuum Hypothesis CH does not hold. This shows that the dependence of the semantics of second-order logic on the metatheoretic set theory is so deep that even questions that ZFC cannot solve can determine the truth or falsity of a sentence in a model.

The curious quality of second-order logic is that the truth of a sentence such as $\theta_{\textrm{CH}}$ in a big enough model of the empty vocabulary is equivalent to the truth of the Continuum Hypothesis in the set-theoretical universe. By the same technique almost any set-theoretical statement can be turned into a sentence of second-order logic, the truth of which in a big enough model of the empty vocabulary is equivalent to the truth of the statement in the set-theoretical universe. Somehow second-order logic manages to read the background set theory correctly. Does this mean that second-order logic is set theory in “sheep’s clothing”?

### 5.4 Does second-order logic depend on the Axiom of Choice?

The Axiom of Choice (AC) is a philosophical puzzle in the foundations of mathematics. Roughly speaking, this axiom, that originally emerged in set theory, says that if we have a set $A$ of non-empty disjoint sets, then we can form a new set $B$ which contains exactly one element from each set in $A$. What can be seen as a problem is the fact that when $A$ is infinite, forming the set $B$ seems to require making an infinite number of choices. See entry on Axiom of Choice for a thorough definition and discussion. On the one hand the Axiom of Choice seems magic, for example when it implies that the wildest sets have a well-ordering. On the other hand it seems innocuous, for example when it implies that the Cartesian product of a family of non-empty sets is non-empty. The Axiom of Choice is typically used to construct odd “paradoxical” sets, such as a non-Lebesgue measurable set of real numbers, a well-ordering of the real numbers, a paradoxical decomposition of the sphere (see entry on set theory), and so on. Such sets are usually in one sense or another undefinable. For example, a non-Lebesgue measurable set of real numbers *has* to be undefinable in second-order logic over $(\oN,+,\cdot)$, if there are sufficiently large cardinals (see the entry on large cardinals and determinacy).

The puzzling Axiom of Choice arises also in the middle of second-order logic: Let $\theta$ be the sentence

$$ \forall X(\forall x\,\exists y\,X(x,y)\to\exists F\,\forall x\,X(x,F(x))). $$

Then $\oR\models\theta$ essentially says that if a binary relation $X$ relates to each $x\in\oR$ a non-empty set $\{y\in\oR : X(x,y)\}$, then there is a function $F$ which chooses for each $x\in\oR$ some $y=F(x)$ such that $X(x,y)$. In set theory this is one of many equivalent ways of saying that the Axiom of Choice holds for (continuum size) families of subsets of $\oR$. The basic tenet of second-order logic is that “all” properties of elements of a fixed domain exist and we can quantify over them. In set-theoretical terms this means that all subsets, definable or not, of a set of any cardinality exist and we can quantify over them. In this spirit the Axiom of Choice seems innocent and is usually accepted in the literature of second-order logic.

By Cohen’s results (1966) there are *N* and $N'$ satisfying the axioms of ZF (without the Axiom of Choice) such that “$\oN\models\theta$” holds in *N* but does not hold in $N'$. This is a further demonstration of the dependence of the semantics of second-order logic on the metatheory.

## 6. Non-Absoluteness of Truth in Second-Order Logic

Absoluteness is one of the most important concepts of logic. It was used already in 1939 by Gödel in his analysis of the hierarchy of constructible sets (1939 [1990: 46]) towards proving the consistency of the Continuum Hypothesis. It is briefly mentioned by Gödel three years earlier in connection with the notion of computability (1936 [1986: 397]).

Intuitively speaking, a concept is absolute if its meaning is independent of the formalism used, or in other words, if its meaning in the formal sense is the same as its meaning in the “real world”. This may sound very vague and inexact. However, absoluteness has a perfectly exact technical definition in set theory.

Recall that a set *a* is called *transitive* if every element of an element of *a* is an element of *a*. A transitive model is a model $(M,\in)$ such that *M* is transitive. By the Mostowski Collapsing Lemma (Mostowski 1949)[^mostowski-1949] every well-founded model $(M,E)$ of the Axiom of Extensionality is isomorphic to a unique transitive model. A basic property of transitive models $(M,\in)$ is that if $a,b\in M$, then $M\models a\subseteq b$ if and only if $a\subseteq b$. (If all elements of *a* that are in *M* are in *b* then all elements of *a* are in *b*, as by transitivity of *M*, elements of *a* are necessarily elements of *M*.) We could express this by saying that the formula $x\subseteq y$ is absolute in transitive models. More generally, we say that a formula $\phi(x_1,\ldots,x_n)$ of the first order language of set theory is *absolute* relative to ZFC if there is a finite $T\subseteq \ZFC$ such that for all transitive models $(M,\in)$ of *T* and all $a_1,\ldots,a_n\in M$ we have

$$\phi(a_1,\ldots,a_n)\text{ if and only if }(M,\in)\models\phi(a_1,\ldots,a_n). $$

This definition of absoluteness is equivalent to the following more syntactic condition (Feferman & Kreisel 1966)[^feferman-1966]: there are a $\Sigma_1$-formula $\exists y\,\psi(y,x_1,\ldots,x_n)$ and a $\Pi_1$-formula $\forall y\,\theta(y,x_1,\ldots,x_n)$ such that

$$\ZFC\vdash\forall x_1\ldots\forall x_n(\phi(x_1,\ldots,x_n)\leftrightarrow \exists y\,\psi(y,x_1,\ldots,x_n)) $$

and

$$\ZFC\vdash\forall x_1\ldots\forall x_n(\phi(x_1,\ldots,x_n)\leftrightarrow \forall y\,\theta(y,x_1,\ldots,x_n)). $$

In such a case we say that $\phi(x_1,\ldots,x_n)$ is $\Delta_1^{\text{ZFC}}$.

For first order logic it can be proved that “$\mm\models_s\phi$” is an absolute property of $\mm$, *s* and $\phi$ relative to ZFC. In fact, this is true even if ZFC is replaced by the weaker Kripke-Platek set theory KP (see Barwise 1972a)[^barwise-1972a]. The usual Tarski Truth Definition of first order logic can be written in $\Delta_1^{\text{ZFC}}$ form. For second-order logic the propositions “$\phi$ is a second-order formula”, “$\mm$ is an *L*-structure” and “*s* is an assignment” are all absolute relative to ZFC as well, but “$\mm\models_s\phi$” is not, as we shall now see. This is a crucial property of second-order logic. One may consider it a weakness, if one thinks of absoluteness as a desirable property, or a strength, if one takes non-absoluteness as a sign of expressive power. Whether a weakness or not, it is an important feature of second-order logic and a dominating topic in discussions about it. Second-order logic is, however, not the only non-absolute logic. For example, $L(Q_1)$ (see the entry on generalized quantifiers) and $L_{\omega_1\omega_1}$ (see then entry on infinitary languages) are non-absolute, while $L(Q_0)$ and $L_{\omega_1\omega}$ are absolute. The reason why $L(Q_0)$ is absolute is essentially that the property of a set being infinite is absolute in transitive models of ZFC. Although the set of sentences of $L_{\omega_1\omega}$ may vary from one transitive model of ZFC to another, the truth of a sentence of $L_{\omega_1\omega}$ in a model is absolute in transitive models of ZFC essentially because the truth has a simple inductive definition which only refers to subformulas of the sentence and elements of the model.

Recall the definition of the sentence $\theta_{\textrm{EC}}(P,R)$ in §5.3, which says that the interpretations of the predicates *P* and *R* have the same cardinality. Cardinality is not an absolute property. Two sets (even two ordinals) can be of different cardinality in one transitive model of ZFC and of the same cardinality in a transitive extension. It is easy to see that “$\mm\models_s\theta_{\textrm{EC}}(P,R)$” is not absolute relative to ZFC. Essentially, the reason is that two sets have the same cardinality if there is a bijection between them. In a small transitive set it may happen that the sets are there but the bijection manifesting their equicardinality is not. The bijection may be one obtained by the method of forcing. Or the lack of the bijection may be the result of applying the Downward Löwenheim-Skolem Theorem[^note-6].

A more serious case of non-absoluteness is the sentence $\theta_{\textrm{CH}}$ of §5.3. The sentence $\theta_{\textrm{CH}}$ of the empty vocabulary has a model if and only if the Continuum Hypothesis is true. If $T\subseteq \ZFC$ is finite, then there are countable transitive models $M\subseteq M'$ such that one, say *M*, satisfies CH and the other, in this case $M'$, does not (by Cohen 1966)[^cohen-1966]. In *M* the sentence $\theta_{\textrm{CH}}$ has a model $\ma$, that is, $M\models \textrm{“}\ma\models\theta_{\textrm{CH}}\textrm{”}$. In $M'$ the same sentence has no models, in particular $M'\not\models \textrm{“}\ma\models\theta_{\textrm{CH}}\textrm{”}$. The situation is similar if the Continuum Hypothesis is replaced by the Axiom of Choice (see §5.4). Thus the property of a model satisfying a second-order sentence is not absolute relative to ZFC. Even the property of a second-order sentence *having* a model is not absolute relative to ZFC, because in *M* the sentence $\theta_{\textrm{CH}}$ has a model but in $M'$ not. For first order logic the property of a sentence of having a model is co-r.e. and therefore arithmetical. Arithmetical properties are always absolute relative to ZFC.

The CH and the AC are central questions of set theory and subjects of continuing debate. While the AC is mostly accepted as an axiom, and is part of the ZFC axiom system, the CH is widely considered an open problem. There are even suggestions (e.g., Feferman 1999)[^feferman-1999] that it cannot be solved by any axiom system with the kind of general acceptance that ZFC has. The formalist position in the foundations of mathematics goes further and maintains that the question, what the truth value of CH is, is meaningless. Both CH and its negation are consistent with ZFC, assuming ZFC itself is consistent. According to the formalist position the status of CH has been solved with this. The semantics of second-order logic depending on these hard questions of set theory puts second-order logic into the same “basket” with set theory. Criticism of set theory becomes criticism of second-order logic and vice versa.

Another indication of the dependence of second-order logic on set theory as the metatheory is the result of Barwise to the effect that the existence of the Hanf number of second-order logic is not provable in set theory without a highly complex use of the Replacement Axiom (for details, see Barwise 1972b)[^barwise-1972b].

## 7. Model Theory of Second-Order Logic

Let us start by noting that there are some trivial consequences of second-order logic being able to quantify over relations. For example, the Craig Interpolation Theorem holds for second-order logic for trivial reasons: If the finite relational vocabulary of $\phi$ is *L*, the finite relational vocabulary of $\phi'$ is $L'$ and $\models\phi\to\phi',$ then there is $\theta$ such that $\models\phi\to\theta\text{ and } \models\theta\to\phi'$ and the vocabulary of $\theta$ is $L\cap L'$, because we can let $\theta$ be the sentence $\exists X_1\ldots\exists X_n\,\phi$, where $L\setminus L'=\{X_1,\ldots, X_n\}$. We can additionally demand that every predicate symbol occurring positively in $\theta$ occurs positively in $\phi$ and $\psi$, and every predicate symbol occurring negatively in $\theta$ occurs negatively in $\phi$ and $\psi$ (the *Lyndon Interpolation Theorem* [Lyndon 1959])[^lyndon-1959]. In the same way the Beth Definability Theorem holds for trivial reasons, also some preservation results[^note-7] have a trivial proof. For a negative result, see Craig 1965.

However, second-order logic does not have a model theory in the same sense as first order logic does. There is no Compactness Theorem to produce non-standard models. One reason why first order logic has such a rich model theory is that first order logic is relatively weak. Countable first order theories that have infinite models have models of all infinite cardinalities. This is a consequence of a weakness of first order logic: its sentences cannot limit the size of the model unless the size is finite. In model theory this weakness is turned to a strength: the structure of models of first order theories can be analyzed in interesting ways. See the entry on model theory for examples of this.

Second-order theories can typically have just one model up to isomorphism. Thus if we investigate the class of models of a second-order sentence, the class may very well consist of just one model, up to isomorphism. With just one model one cannot really develop a model theory. One ends up investigating the one and only model and there are no compelling reasons to use logic in the study of it. If the one and only model is an algebraic structure, one should use algebra to study it. If it is an ordered structure, one should use the general theory of ordered structures to study it, and so on. It is unlikely that being second-order characterizable (see §7.1) tells much about the structure. It reveals more about second-order logic in general. For example, being able to characterize the structure of natural numbers means that the Compactness Theorem and the Completeness Theorem fail. Being able to characterize the ordered field of real numbers means that both the Downward and the Upward Löwenheim-Skolem Theorems fail. It is from this perspective—to understand second-order logic itself—that it is interesting to know exactly which structures are second-order characterizable up to isomorphism.

Let us finally compare the two hierarchies, the model theoretic hierarchy $\Sigma_n^1\cup\Pi_n^1$ inside second-order logic and the Levy hierarchy $\Sigma_n\cup\Pi_n$ in set theory.

**Theorem 4**

1. The set of Gödel numbers of valid second-order sentences is the complete $\Pi_2$-set of natural numbers. (Tharp 1973)[^tharp-1973]
2. The Löwenheim-Skolem number of second-order logic is the supremum of all $\Pi_2$-definable ordinals. (Krawczyk & Marek 1977)[^krawczyk-1977]
3. The Hanf number of second-order logic is the supremum of all $\Sigma_2$-definable ordinals. (Krawczyk & Marek 1977)[^krawczyk-1977]
4. Every model class which is definable in second-order logic is $\Delta_2$-definable in set theory. (Väänänen 1979)[^väänänen-1979]

In the light of the above theorem second-order logic sits firmly on the $\Sigma_2\cup\Pi_2$-level of set theoretic definability. This is a reason to consider second-order logic *weaker* than first order set theory. This sounds paradoxical. How can second-order logic, with all the power and non-first order properties it has, be weaker than first order logic based set theory, when first order logic cannot even express finiteness, countability, uncountability, and so on? Nevertheless the message of Theorem 4 is undeniable. Perhaps this would not be so puzzling if we thought of set theory as a very high order logic over the singleton of the empty set. After all, set theory permits endless iterations of the power set operation, while second-order logic permits only one iteration.

We start below with a subsection on models that can be characterized in second-order logic by one sentence up to isomorphism. Another approach to the model theory of second-order logic is to focus on models with *large cardinal* (inaccessible, measurable, supercompact cardinals) properties. This is the topic of §7.2. Finally, in §7.3 we consider the possibility of allowing the so-called general models introduced in §9.1. In this case second-order logic becomes very much like first order logic. However, general models are mostly interesting when they are so-called Henkin models, i.e., they satisfy the so-called Comprehension Axioms. In Henkin models second-order logic satisfies the Compactness Theorem and other principles familiar from first order model theory but no general structure- or classification theory exists yet, perhaps because the Comprehension Axioms bring in a lot of complicated structure into the models.

### 7.1 Second-order characterizable structures

A structure $\ma$ is *second-order characterizable* if there is a second-order sentence $\theta_\ma$ such that $\mb\models\theta_\ma\iff\mb\cong\ma$ for all structures $\mb$ of the same vocabulary as $\ma$.

**Example 5:** The following structures are second-order characterizable:

1. Natural numbers: $(\oN,+,\cdot)$.
2. Real numbers: $(\oR,+,\cdot,0,1)$.
3. Complex numbers: $(\oC,+,\cdot,0,1)$.
4. The first uncountable ordinal $(\omega_1,<)$.
5. The level $(V_\kappa,\in)$ of the cumulative hierarchy, where $\kappa$ is the first strongly inaccessible cardinal $>\omega$.
6. The well-order $(\kappa,<)$ of the first weakly compact cardinal $>\omega$.

Are *all* structures second-order characterizable? There are only countably many second-order sentences, hence only countably many (up to isomorphism) second-order characterizable structures. Therefore there are lots of structures of every infinite cardinality which are not second-order characterizable. However, it is not easy to give examples. One example is $(\kappa,<)$, where $\kappa$ is the first measurable cardinal ($>\omega$). See §7.2 for an explanation. Another example is $(\oN,<,A)$, where *A* is the set of Gödel numbers of valid second-order sentences in the vocabulary of one binary relation. For an explanation, see §7.2. One may ask whether there is an example which arises from mathematical practice outside of mathematical logic. What about $(\oR,+,\times,<,A)$, where *A* is a Hamel basis (a basis for the vector space where the reals are the vectors, rationals are the scalars and vector addition is the usual addition of reals)? It is consistent, relative to the consistency of ZF that no such structure $(\oR,+,\times,<,A)$ is second-order characterizable (Hyttinen, Kangas, & Väänänen 2013).

A special property of second-order characterizable structures is that their reducts are also second-order characterizable, because we can use existential second-order quantifiers to “guess” the missing relations and functions. Therefore it is interesting to find characterizable structures that have as many (but only finitely many) relations and functions as possible. We can endow $\oN$ with any finite number of recursive functions $f_1,\ldots, f_n $ and relations $R_1,\ldots, R_m$ obtaining the structure $(\oN,f_1,\ldots, f_n,R_1,\ldots, R_m)$ and this is second-order characterizable. We can endow $\oR$ with any familiar analytic functions such as trigonometric functions or any other functions given by a convergent power series the coefficients of which are given by a recursive function, and the result is second-order characterizable.

It is easy to see that the second-order theory of a second-order characterizable structure $\ma$ is Turing-reducible to the second-order theory of any bigger second-order characterizable structure $\mb$, as for all second-order $\phi$:

$$\ma\models\phi\iff\mb\models\exists P(\theta_\ma^{P}\land\phi^{P}). $$

The bigger the characterizable structure is, the more complex is the second-order theory. That there is no largest characterizable structure can be seen as follows: If $\ma$ is second-order characterizable, then so is the reduct of $\ma$ to the empty vocabulary[^note-8], that is, the cardinality $|A|$ of $\ma$ is characterizable. Such cardinal numbers were studied by Garland (1974). For example, if $\kappa$ is characterizable, then so are $\kappa^+$ and $2^\kappa$.

If $\phi$ is a second-order sentence, we define

$$\Mod(\phi)=\{\mm: \mm\models\phi\}. $$

If $\phi$ characterizes a model $\ma$, then $\Mod(\phi)$ is just the class of models isomorphic to $\ma$. If we look at $\Mod(\phi)$ from the perspective of set theory, we know it is $\Delta_2$ (Theorem 4). On the other hand, the set of Gödel numbers of valid second-order sentences is $\Pi_2$-complete (Theorem 4), hence not $\Sigma_2$ and in particular, not $\Delta_2$. This contemplation leads us to the following extension of Theorem 3 above:

**Theorem 6 (Väänänen 2012)[^väänänen-2012]** Second-order validity is not second-order definable on any second-order characterizable structure.

This raises the question, how can we understand second-order validity from the second-order perspective? In view of the above theorem we cannot understand second-order validity as something that can be expressed in second-order logic on some structure which itself can be characterized in second-order logic. The reference to set theory seems inevitable in understanding second-order validity. Let us discuss what this might mean from the point of view of structuralism. Parsons defines structuralism as follows:

> By the “structuralist view” of mathematical objects, I mean the view that reference to mathematical objects is always in the context of some background structure, and that the objects involved have no more to them than can be expressed in terms of the basic relations of the structure. (Parsons 1990: 303)[^parsons-1990]

Structuralism in this sense (for other kinds of structuralism, see, e.g., Hellman 2001)[^hellman-2001] seems to fit well into the second-order logic framework. Contrary to set theory, second-order logic always assumes an underlying (limited) structure which is supposed to reflect one particular aspect of mathematics such as the semi-ring of natural numbers, the ordered field of real numbers, the field of complex numbers, the well-ordered structure $(\omega_1,<)$, and so on. Ideally, these underlying structures are second-order characterizable. This leads to a problem with universal truths such as validity, but also with less complex ones such as the statement that every linear order has a completion, or that every field has an algebraic closure. Such universal truths are not about any particular structure.

### 7.2 Second-order logic and large cardinals

We refer to the SEP entries independence and large cardinals and large cardinals and determinacy for the definition of concepts related to large cardinals.

The following early result on the connection between model theory of second-order logic and large cardinals is a model for other more delicate results. It is a kind of Downward Löwenheim-Skolem Theorem for second-order logic. It says that if a second-order sentence has a model of the cardinality of a measurable cardinal, then it has a smaller submodel:

**Theorem 7 (Scott 1961)[^scott-1961]** Suppose $\kappa$ is a measurable cardinal. If $\phi$ is a second-order sentence and $\phi$ has a model $\mm$ of cardinality $\kappa$, then for every $X\subseteq M$ of cardinality $<\kappa$ there is $\mn\subseteq\mm$ such that $X\subseteq N$, $|N| < \kappa$, and $\mn\models\phi$. [^note-9]

A particular consequence is that the first measurable cardinal cannot be second-order characterizable as a model of the empty vocabulary (a fact that was referred to above in §7.1). Theorem 7 resembles remarkably the Downward Löwenheim-Skolem Theorem of first order logic. The only difference is that one has to start with a big model, a model of the size of a measurable cardinal. Smaller cardinals need not work. For example, if $\lambda$ is the least weakly compact cardinal $>\omega$, then there is a sentence $\phi$ which has $\lambda$ (with the empty vocabulary) as a model but no smaller models. The sentence[^note-10] $\phi$ says that $\lambda$ is inaccessible ($>\omega$) and that every $\lambda$-tree (a tree of height $\lambda$ with all levels of size $<\lambda$) has a branch of length $\lambda$.

If we want to obtain a Downward Löwenheim-Skolem Theorem which works for any structure, not only for structures of a measurable cardinality, we have to look at even bigger cardinals: The *LST-number* of second-order logic is defined to be the least (if any exist) $\kappa$ such that if $\ma$ is any structure and $\phi$ is a second-order sentence true in $\ma$, then there is a substructure $\mb$ of $\ma$ of cardinality $<\kappa$ which also satisfies $\phi.$

**Theorem 8 (Magidor 1971)[^magidor-1971]** The LST-number of second-order logic exists if and only if there are supercompact cardinals $>\omega$ and then it is the smallest of them.

Second-order logic is said to satisfy strong *$\kappa$-compactness* if every second-order theory, every subset of size $<\kappa$ of which has a model, has itself a model.

**Theorem 9 (Magidor 1971)[^magidor-1971]** The least $\kappa$ such that second-order logic satisfies the strong $\kappa$-compactness is the least extendible cardinal.

### 7.3 The model theory of general and Henkin models

The situation changes completely if we adopt so-called general models (§9.1). With general models second-order logic has similar model theoretic properties as first order logic, as it can simply be thought of as many sorted first order logic (see §9.1 and Manzano 1996)[^manzano-1996]. By and large, results of many-sorted first order logic translate immediately to second-order logic.

## 8. Decidability Results

The second-order theory of even the empty vocabulary is undecidable, as we noted in §5.1. In contrast, *monadic* second-order logic gives rise to many important decidability results. Let us first observe that (not only in the empty vocabulary but also) in a monadic vocabulary, i.e., one consisting of monadic predicates only, monadic second-order logic is certainly decidable as proved already in 1915 by Löwenheim (1915) in one of the earliest papers on the mathematical aspects of formal logic. Löwenheim’s result can be proved easily by quantifier elimination, or alternatively by the more recent method of Ehrenfeucht-Fraïssé-games (see §3). However, monadic *third* (and higher) order logic in monadic vocabulary, with quantifiers over not only subsets and also over sets of subsets of the domain, is undecidable (Tharp 1973)[^tharp-1973]. We now focus on vocabularies which are not merely monadic.

Compared to a monadic vocabulary, the other extreme can be described as follows: Let *P* be a ternary predicate (a “pairing function”) on a non-empty set *S*. Suppose that for every $x,y\in S$ there is $z\in S$ with $(x, y, z) \in P$ and for every $z\in S$ there is at most one pair $(x, y)$ with $(x, y, z) \in P$. Then the true (full) second-order theory of *S* is interpretable in the monadic theory of $(S, P)$ (Gurevich 1985)[^gurevich-1985]. In other words, in a context where a pairing function is present, as in set theory and number theory, no special advantage arises from limiting second-order logic to its monadic fragment.

The next step from a vocabulary consisting of only monadic predicates is a vocabulary with exactly one unary function. To describe some highly non-trivial results in this case we introduce the following concept, which has independent interest: The *spectrum* of a first or second-order sentence is the set of cardinalities of its finite models. Spectra were introduced by Scholz, see Durand, Jones, Makowsky, and More (2012) for a history. A spectrum is of course always recursive. In fact, a set of natural numbers is a spectrum of a first order sentence iff it is in NEXPTIME, that is, recognizable by a nondeterministic Turing machine in exponential time (Jones & Selman 1974)[^jones-1974]. In the case of sentences with just one unary function symbol there is a surprising characterization. Let us call a set *S* of natural numbers *eventually periodic* if there are natural numbers *N* and *p* with $p > 0$ such that for every *n* with $n > N$, we have $n \in S$ iff $n +p \in S$.

**Theorem 10 (Durand, Fagin, & Loescher 1998; Shelah 2004)[^shelah-2004]** Suppose the vocabulary has just one unary function. Then a set of natural numbers is the spectrum of a monadic second-order sentence if and only if it is the spectrum of a first order sentence if and only if it is eventually periodic.

In graphs monadic second-order logic can still express most interesting properties. For example, the *connectivity* of the graph (here *E* is the edge relation) can be expressed by the sentence

$$\forall X((\exists x\,X(x)\land\forall x\forall y((X(x)\land xEy)\to X(y)))\to\forall x\,X(x)) $$

and the *3-colorability* of the graph by the sentence

$$\begin{align} &\exists X\,\exists Y\,\exists Z ( \forall x( X(x) \lor Y(x) \lor Z(x) )\land{}\\ &\quad\forall x\,\forall y (( (X(x)\land X(y)) \lor(Y(x)\land Y(y)) \lor(Z(x)\land Z(y)) )\to{}\\ &\quad\neg xEy)) \end{align}$$

There is a wealth of decidability results of monadic second-order logic on linear orders, trees and graphs.

**Theorem 11 (Büchi 1962; Elgot 1961; Rabin 1968)[^büchi-1962][^elgot-1961][^rabin-1968]** The monadic second-order theory of $(\oN,s)$, i.e., the successor function on $\oN$ and of the full infinite binary tree, i.e., two successor functions on $\oN$, are both decidable.

The proof goes via a reduction to automata. An *automaton* is a restricted form of a Turing machine. In an automaton the machine never writes on the tape, so the tape just contains the input (Rabin & Scott 1959)[^rabin-1959]. However, the computation may be infinite. The input is considered *accepted* in the case of an infinite computation if an accepting state is reached infinitely many times. (There are also more complicated criteria of acceptance). With monadic second-order logic we can guess an accepting computation of the automaton. It is possible but more difficult to show that an automaton can check the truth of a monadic second-order sentence. The monadic second-order theory of ordinals $(\alpha,<)$ have been studied extensively from the point of view of decidability. For example, the monadic second-order theory of all countable ordinals, the theory of $\omega_1$, and the theory of all ordinals $<\omega_2$ are decidable (Büchi 1973)[^büchi-1973], but ZFC cannot decide whether the monadic second-order theory of $\omega_2$ is decidable (Gurevich, Magidor, & Shelah 1983).

## 9. Axioms of Second-Order Logic

Recall our convention: Whenever we use upper case Fraktur letters, such as $\ma,\mb,\mm,\mn$ etc, to name a structure, we use the upper case Italic versions of those letters, such as $A,B,M,N$ etc, to name the domain of the structure.

The deductive system of second-order logic, presented first explicitly in Hilbert-Ackermann (Hilbert & Ackermann 1938)[^hilbert-1938], is based on the obvious extension of axioms and rules of first order logic together with the *Comprehension Axiom Schema*, defined as follows: Suppose $\phi(x_1,\ldots,x_n)$ is a second-order formula with $x_1,\ldots, x_n$ among its free individual variables and the second-order variable *R* is *not* free in $\phi$. Then the following formula is an instance of the Comprehension Axiom Schema:

$$\tag{10}\label{CA} \exists R\,\forall x_1\ldots x_n(\phi(x_1,\ldots, x_n)\leftrightarrow R(x_1,\ldots, x_n)). $$

There is a similar schema for second-order formulas that define a function but we omit it here.

An example of a very simple second-order inference in number theory would be

$$ \frac{\dfrac{2+5<9}{\exists R\ R(2+5,9)}}{\exists F\,\exists R\ R(F(2,5),9)} $$

A priori (\ref{CA}) might appear very strong as it stipulates the existence of a relation. However, such an *R* seems reasonable to accept because it is definable:

$$R=\{(a_1\ldots a_n) \in M^n: \mm\models \phi(a_1,\ldots, a_n)\}. $$

Our Comprehension Axiom Schema is *impredicative* in the sense that the bound *n*-ary relation variables which may potentially occur in the formula $\phi(a_1,\ldots, a_n)$ have *R* in their range. In this sense second-order logic is utterly impredicative. The Comprehension Axiom Schema has weaker forms that are less impredicative. In the *Arithmetic Comprehension* Schema we assume $\phi(a_1,\ldots, a_n)$ is first order. In the $\Pi^1_1$-Comprehension Schema we assume $\phi(a_1,\ldots, a_n)$ is $\Pi^1_1$. In mathematical practice these two weaker principles usually suffice, see Simpson (1999 [2009]) and §14.

Hilbert-Ackermann (1938) added to the proof system of second-order logic also two different schemas that they call *Axioms of Choice*. We are used to thinking of the Axiom of Choice as a set-theoretical principle. But second-order logic has the same situation with choice principles as set theory. It makes perfect sense in second-order logic to ask whether there is a well-order of the domain. The existence of such a well-order does in general not follow from the Comprehension Schema because the well-order may be---and is likely to be---undefinable. So the only way to get a well-order of, say, the real numbers, in second-order logic is to assume some form of second-order Axiom of Choice. The first choice principle is

$$\tag{AC} \begin{align} &\forall x_1\ldots x_m\exists x_{m+1}\, R(x_1,\ldots, x_{m+1}) \rightarrow {}\\ &\ \exists F\,\forall x_1\ldots\forall x_m\, R(x_1,\ldots, x_m, F(x_1\ldots x_m)) \end{align}$$

and the second is

$$\tag{AC$'$} \forall x_1\ldots x_m\exists F\,\varphi\rightarrow\exists F'\,\forall x_1\ldots x_m\varphi', $$

where the formula $\varphi'$ is obtained from the formula $\varphi$ by replacing everywhere $F(t_1,\ldots, t_k)$ by $F'(t_1\ldots t_k,x_1,\ldots, x_m)$.

The first Axiom of Choice (AC) says intuitively that if a set

$$\{a_{n+1}\in M : \mm\models R(a_1,\ldots,a_n, a_{n+1})\} $$

is non-empty, then there is a function which picks an element $a_{n+1}$ from the set, using the parameters $a_1,\ldots,a_{n}$ as arguments. The second Axiom of Choice (AC′) is a kind of second-order choice: We have for all $a_1,\ldots,a_n$ a function *F* with the property $\phi$, so in fact *F* depends on $a_1,\ldots, a_n$ and should be denoted $F_{a_1\ldots a_n}$. What (AC′) says now is that we can collect the functions $F_{a_1\ldots a_n}$ together to form just one function $F'$ of higher arity such that

$$F'(a_1,\ldots,a_{n+1})=F_{a_1\ldots a_n}(a_{n+1}). $$

Although $F'$ appears to be definable, this is not the case, as the mapping

$$(a_1,\ldots,a_n)\mapsto F_{a_1\ldots a_n} $$

may be highly undefinable.

Naturally, we may also want to assume the *Well-ordering Principle* which states that there is a binary relation which is a total order on the individuals and satisfies the condition that every non-empty set of individuals has a least element in the order. It is easy to see that this principle implies (AC′). In ZFC there are hundreds of equivalent formulations of the Axiom of Choice or weaker versions of it. Most of the formulations that are equivalent in ZFC are non-equivalent in second-order logic. This is because set theory allows free movement between sets and their power sets, but second-order logic does not[^note-11]. To obtain similar equivalence proofs as in set theory, one would have to move between second-order logic and third order logic, see Gaßner (1994) and Siskind, Mancosu & Shapiro (2023).

### 9.1 General models and Henkin models

The concept of “general model” was introduced by Henkin (1950) in order to obtain a Completeness Theorem for second-order logic. General models are not the intended models of the axioms in the sense that bound relation and function variables do not range in these models over *all* relations and functions, only over a collection of them. The generally accepted attitude towards them is that they are not what one wants but they are necessary for obtaining a smooth theory. They are like irrational numbers in calculus: it would be ideal if all lengths that we encounter in calculus (or geometry) were commensurable, but that is not how things turned out. Some lengths are incommensurable, and we end up accepting irrational numbers in order to have a smooth general theory of lengths and their proportions. General models can be also compared to transitive models of set theory. One transitive model may say one thing is true, another says just the opposite is true. But together the transitive models help us understand the axioms of set theory. The current methods in the metamathematical investigation of the axioms of set theory, namely inner models and forcing extensions, all use transitive models of set theory in an essential way. Similarly general models of second-order logic help us investigate metamathematical properties of second-order logic and its axioms.

**Definition 12** A *general model* is a pair $(\mm,\G)$, where $\mm$ is a usual *L*-structure and $\G$ is a set of subsets, relations (of any arity) and functions (of any arity) on *M*. In monadic second-order logic $\G$ is assumed to contain unary predicates only.

We can define the concept

$$(\mm,\G)\models_s\phi $$

for second-order $\phi$ by induction on $\phi$ by stipulating

$$ \begin{align} (\mm,\G)\models_s\exists X\,\phi & \iff (\mm,\G)\models_{s(P/X)} \phi\text{ for some $P\in \G$}.\\ (\mm,\G)\models_s\exists F\,\phi &\iff (\mm,\G)\models_{s(f/X)} \phi\text{ for some $f\in \G$}. \end{align} $$

The difference to the original truth definition of second-order logic is thus that the interpretations of the second-order variables cannot be quite arbitrary, they have to be found in $\G$. The smaller the $\G$ is, the weaker the logic. On the other hand, if $\G^\star$ is the set of *all* relations and functions on *M*, then the truth definition for the general model $(\mm,\G^\star)$ is the same as the original truth definition. We call such general models *full* and indeed identify $(\mm,\G^\star)$ with $\mm$. The other extreme is that $\G=\emptyset$. Then we are back in first order logic. To distinguish second-order logic with general models from the original second-order logic, we call the latter *full*.

**Definition 13** A general model which satisfies all the axioms of second-order logic, including the Comprehension Axiom Schema and the Axioms of Choice, is called a Henkin model.

Note that there is *no* sentence of second-order logic which says that the model is full. That is, there is no second-order $\phi$ such that for all general models $(\mm,\G)$ it holds that

$$ (\mm,\G)\models\phi\iff (\mm,\G) \text{ is full.} $$

If we attempt to use $\forall X\,\exists Y\,\forall x(X(x)\leftrightarrow Y(x))$ as such a $\phi$, we just obtain the result that $\phi$ is always true and says that the general model $(\mm,\G)$ is “full” in its *own* sense of “full”, not in the sense of the metatheory.

A natural attempt to get a Henkin model $(\mm,\G)$ would be to let $\G$ consist of *first order* definable relations and functions on $\mm$. However, in this way we get only Arithmetic Comprehension, not the full Comprehension Axiom.

An easy way to obtain a Henkin model $(\mm,\G)$ is to take a transitive model *N* of ZFC such that $\mm\in N$ and let $\G$ consist of all relations and functions on *M* that are elements of *N*. It follows from $N\models ZFC$ that $(\mm,\G)$ is a Henkin model.

Truth in a general model, namely the proposition “$(\mm,\G)\models_s\phi$” is absolute relative to ZFC, contrary to the truth definition of (full) second-order logic. In this respect second-order logic with general models resembles first order logic. As we will see, it resembles first order logic in many other respects, too.

Second-order logic with general models can be thought of in terms of *many sorted logic*. Many sorted logic is first order logic with several different *sorts* of variables. Respectively, relations and functions may be between elements of different sorts. Here “sort” just means that variables of different “sorts” are kept apart by giving them different names. Otherwise the variables are just ordinary first order variables. Structures $\mm$ of many-sorted logic have a separate domain $M_s$ for each sort *s*. We may think of second-order logic as many sorted logic in which the individual variables are of a sort $\si$, for each *n* the *n*-ary relation variables are of a sort $\sr$, and the *n*-ary function variables of a sort $s_n^{\rm fu}$. In addition there is an $n+1$-ary relation symbol $\sA$ between *n*-tuples of individuals and *n*-ary relation variables indicating which *n*-tuples are in a relation and which are not. Finally there is an $n+1$-ary function symbol $\sF$ between *n*-tuples of individual, individuals, and *n*-ary function variables indicating what value a function variable gives to each *n*-tuple. There are obvious first order axioms which guarantee that the many sorted logic just described faithfully mirrors second-order logic with general models. [^note-12]

For more on the reduction of second-order logic to many-sorted logic, we refer to Manzano (1996). For example, the proof theory of second-order logic can be understood via the translation to many sorted logic. For more on the proof theory of second-order logic, see Buss (1998). There is a translation of many sorted logic further to single sorted first order logic due essentially to Herbrand (1930), see also Wang (1952) and Schmidt (1951). This can be used to obtain many of the basic properties of first order logic first for many sorted logic and then further for second-order logic with general models.

The most important application of general models is the Completeness Theorem:

**Theorem 14 (Henkin 1950)[^henkin-1950]** A second-order sentence follows from the axioms if and only if it is true in all Henkin models. [^note-13]

Respectively, we obtain the Compactness Theorem[^note-14] as well as the downward and the upward versions of the Löwenheim-Skolem Theorem.[^note-15]

One way to think about Henkin models is that they fill the gaps left by full models, just as irrational numbers fill the gaps left by rational numbers. They are needed in order to obtain a smooth theory of second-order logic. They manifest “paradoxical” phenomena that we do not see among full models. For example we obtain non-standard models of number theory, countable models of the axioms of real numbers, etc. The categorical sentences characterizing mathematical structures among full models now suddenly have also other “models”, namely Henkin models, and they come in all infinite cardinalities.

If $\phi$ is a second-order sentence we define

$$\tag{11}\label{henkin} \textit{Mod}_H(\phi)=\{(\mm,\G) : (\mm,\G)\models\phi\} $$

Obviously, $\Mod(\phi)\subseteq \textit{Mod}_H(\phi)$. If $\phi$ characterizes $\mm$ up to isomorphism, then $\mm\in \Mod(\phi) $. In all non-trivial cases[^note-16] $\textit{Mod}_H(\phi)\ne \{\mm\}$. For $\mm\in\Mod(\phi)$ we can think of $(\mm,\G)\in\textit{Mod}_H(\phi)$ as “approximations” of $\mm$. One of the approximations is the “real” $\mm$, i.e. $(\mm,\G^*)$, but by means of deductions in second-order logic we cannot tell which. Because of the inherent weakness of formal systems, going back to Skolem and Gödel, infinite structures are shrouded by Henkin models and cannot be gotten perfectly into focus by deductive means.

The *Fraenkel-Mostowski method* is a construction of Henkin models which was first used in set theory to obtain models where Axiom of Choice fails, and later used in second-order logic to obtain similar models before the method of forcing emerged. The method goes as follows: Suppose $\ma$ is a structure and *H* is a group of automorphisms of $\ma$. A subset *B* of $A^n$ is called *symmetric* if there is a finite set $E\subseteq A$, called a *support* of *B*, such that for all $\pi\in H$ which fix *E* pointwise[^note-17],

$$\forall x_1\ldots\forall x_n((x_1,\ldots, x_n)\in B\to (\pi(x_1),\ldots, \pi(x_n))\in B). $$

The respective condition for a function $f:A^n\to A$ is

$$\begin{align} &\forall x_1\ldots\forall x_n ((x_1,\ldots ,x_n) \in B \to f(\pi(x_1), \ldots ,\pi(x_n)) \in B \land {}\\ &\qquad f(\pi(x_1),\ldots ,\pi(x_n)) = \pi (f (x_1,\ldots ,x_n))) \end{align}$$

Let $\G$ be the set of symmetric relations and functions on *A*. The pair $(\ma,\G)$ is always a Henkin model.

Among the early applications of the Fraenkel-Mostowski method were the result of Mostowski (1938) that one cannot prove from the Comprehension Axiom Schema alone the equivalence of certain two different definitions of finiteness and of Lindenbaum and Mostowski (1938) that Zermelo’s axioms for set theory are not enough to prove the Axiom of Choice, or even just that every infinite set is the disjoint union of two infinite sets.

The *Fraenkel model* arises if *H* is the group of all permutations of an infinite set *A*. In the Fraenkel model the set *A* is infinite but Dedekind-finite (i.e., *A* has no one-one function into a proper subset) and cannot be well-ordered, not even linearly ordered. Moreover, the set *A* is not the disjoint union of two infinite sets. There is no choice function for two element subsets of *A*.

The *Mostowski model* arises if $A=\oQ$ and *H* is the group of automorphisms of $(\oQ,<)$. In the Mostowski model the set *A* can be linearly ordered but not well-ordered. The Axiom of Choice holds for (sets of) non-empty finite sets.

For more on Fraenkel-Mostowski models as Henkin models for second-order logic, see Gaßner (1994).

### 9.2 Axioms of infinity

Recall our convention: Whenever we use upper case Fraktur letters, such as $\ma,\mb,\mm,\mn$ etc, to name a structure, we use the upper case Italic versions of those letters, such as $A,B,M,N$ etc, to name the domain of the structure.

The axioms of second-order logic are trivially true in a (full) model with just one element. This raises the question how to guarantee that there are more than one element in the domain. Of course, we can add, for every *n*, an axiom which says that there are more than *n* elements. There are various ways to say in second-order logic with *one* axiom that there are *infinitely* many individuals. These are equivalent in full models but may be non-equivalent in Henkin models. Some are equivalent if the Axiom of Choice is assumed. Let us call a second-order sentence $\phi$ of the empty vocabulary an *Axiom of Infinity* if

$$\ma\models\phi\text{ if and only if $A$ is infinite}. $$

An axiom of infinity can say in second-order logic that a proper subset of the domain has the same cardinality as the entire domain (i.e., that the domain is not Dedekind-finite), or that there is a partial order without a maximal element, or that there is a set with a unary function and a constant which constitute a structure isomorphic to $(\oN,s,0)$, or that the domain is the union of two disjoint sets which have the same cardinality as the domain, and so on. As is the case in set theory without the Axiom of Choice, the different formulations of infiniteness need not be equivalent. In second-order logic the situation is even more diffuse because of the variety of different formulations of the Axiom of Choice. We refer to Asser (1981) for a discussion of the different variants and to Hasenjaeger (1961) for a proof that the various non-equivalent forms of Axioms of Infinity form in a sense a dense set. For a survey of different concepts of finiteness, see de la Cruz (2002).

## 10. Categoricity

A theory in second (or first) order logic is said to be *categorical* if any two of its models are isomorphic. A single sentence (which has a model) is categorical if and only if it characterizes some model up to isomorphism (see §7.1). A nice property of a categorical theory $\Gamma$ is (semantic) *completeness*: Any sentence $\phi$ in the language in which the theory is written is decided by $\Gamma$ in the following sense. Either every model of $\Gamma$ satisfies $\phi$ or every model of $\Gamma$ satisfies $\neg\phi$. In other words, either $\phi$ or $\neg\phi$ is a (semantic) logical consequence of $\Gamma$. The reason is very simple: $\Gamma$ has, up to isomorphism, only one model *M*. Since isomorphism preserves truth in second-order logic, $\phi$ or $\neg\phi$ is a (semantic) logical consequence of $\Gamma$ according to whether $\phi$ is true in *M* or false in *M*.

If $\phi$ is a second-order sentence we defined above $\Mod(\phi)$ as the class $\{\mm : \mm\models\phi\}$. If $\phi$ characterizes $\mm$ up to isomorphism, then, up to isomorphism,

$$\Mod(\phi)=\{\mm\}. $$

The project of axiomatizing mathematical structures with second-order sentences was so successful in the first quarter of the twentieth century that Carnap even proposed, inspired by Fraenkel (1919 [1928]), see Awodey and Reck 2002 for more on this, that *every* mathematical structure is determined, up to isomorphism, by its second-order theory. There are trivial cardinality reasons why this could not possibly hold for all models of size $2^\omega$ and larger. There are simply not enough second-order theories in comparison with the number of non-isomorphic models. However, the proposal of Carnap is trivially true for finite models, and not entirely unreasonable for countable models. In fact Ajtai (1979) showed that it is consistent with ZFC, provided ZFC itself is consistent, that any two countable structures in a finite vocabulary that satisfy the same second-order sentences are isomorphic. Ajtai showed that it is also consistent with ZFC, provided ZFC itself is consistent, that there are two countable structures in a finite vocabulary that satisfy the same second-order sentences without being isomorphic. Thus Carnap’s conjecture (for countable models) is independent of ZFC.

Solovay has made a posting in FOM (2006 [Other Internet Resources]) in which he shows that the related statement that every complete second-order sentence is categorical, is independent of ZFC. Saarinen, Väänänen and Woodin (2024 [Other Internet Resources]) show that large cardinals, at least up to a supercomapct cardinals, cannot decide whether every complete second-order sentence is categorical,

There is a strong form of categoricity which holds for Henkin structures in important cases and agrees with the usual concept of categoricity in the case of full Henkin models. It builds on the remarkable ability of second-order logic to express its own categoricity. The isomorphism $(M,R)\cong(M',R')$ of two structures $(M,R)$ and $(M',R')$, where the predicates *R* and $R'$ are, say, binary, can be expressed in second-order logic as follows, letting $\ma=(A,M,M',R,R')$, where *A* is any set containing $M\cup M'$, $M=U^\ma$, $M'={U'}^\ma$, $R=P^\ma$ and $R'=P'^\ma$. Now

$$(M,R)\cong(M',R')\iff\ma\models\isom(U,P,U',P'), $$

where $\isom(U,P,U',P')$ is the sentence

$$ \begin{align} &\exists F[ \forall x(U(x)\to U'(F(x))) \land {}\\ &\quad \forall x\,\exists y ( U'(x)\to ( U(y)\land x=F(y) ) ) \land {}\\ &\quad\forall x\,\forall y( ( U(x) \land U(y)) \to {}\\ &\quad[ (F(x)=F(y)\to x=y) \land {}\\ &\quad(P(x,y)\leftrightarrow P'(F(x),F(y))) ] ) ]. \end{align} $$

This suggests that the categoricity of a sentence $\theta(P)$ with a binary predicate symbol *P* can be redefined equivalently,[^note-18] letting $\categ(\theta(P))$ be the sentence

$$\forall P\,\forall P'\,\forall U\,\forall U'\left(\left(\theta(P)^{U}\land\theta(P')^{U'}\right)\to\isom(U,P,U',P')\right), $$

as

$$\tag{12}\label{redef} \models\categ(\theta(P)). $$

In fact, this is how Tarski defines categoricity in Tarski (1956), (page 387). This leads us to define:

**Definition 15** We say that $\theta(P)$ is *internally categorical* if

$$\tag{13}\label{internal} \vdash\categ(\theta(P)). $$

Internal categoricity could also be called *provable categoricity*. The phrase ‘internal categoricity’ was introduced in the context of arithmetic in Walmsley (2002). It was advocated more generally in Väänänen (2012), with more details in Väänänen and Wang (2015). We refer to Button and Walsh (2016) as well as Maddy and Väänänen (2023) for a recent discussion on this concept.

Note that (\ref{internal}) is stronger than (\ref{redef}) because provable sentences are certainly valid. Owing to the Completeness Theorem we can rewrite (\ref{internal}) as

$$\tag{14}\label{internals} (\ma,\G)\models\categ(\theta(P))\text{ for all Henkin models $(\ma,\G)$}. $$

Thus internal categoricity means categoricity not only for ordinary models, i.e., full Henkin models, but categoricity inside an arbitrary Henkin model. Note that categoricity is a meta-theoretical concept as it refers to the semantics of second-order logic. In $\categ(\theta(P))$ the categoricity of $\theta(P)$ is written in the language of second-order logic. That is, the categoricity, despite being a meta-theoretical concept, is written in the object language. It can be asked, whether this leads us to a different concept? Be that as it may, when the meaning of $\categ(\theta(P))$ is uncovered by considering its semantics in the meta-theory, the meaning is the same as the meaning we give to the categoricity of $\theta(P)$. In the concept of internal categoricity we take advantage of this situation by switching from semantical meaning to proof-theoretic meaning: We insist that $\categ(\theta(P))$ is (not only valid but even) provable. Proof-theory requires less meta-theory than semantics. We can investigate provability of second-order sentences even in number theory by using numbers to code sentences and proofs, as Gödel did in his proof of the Incompleteness Theorem. Of course, the Completeness Theorem brings us back to the semantics.

To verify the categoricity of a second-order sentence one has to go through infinite structures in a way which essentially calls for set theory. The situation with internal categoricity is different. To verify the internal categoricity of a second-order sentence one just has to produce a proof. So there is a dramatic difference. And still internal categoricity is stronger than categoricity. So it would be foolish to establish categoricity if one could establish even internal categoricity. Fortunately, the classical examples of categorical sentences are all internally categorical:

**Theorem 16 (Väänänen & Wang 2015)[^väänänen-2015]** The received second-order sentences characterizing the structures $(\oN,<)$ and $(\oR,<,+,\cdot,0,1)$ are internally categorical.

The concept of internal categoricity provides a bridge between full semantics and Henkin semantics. It works in the same way in both cases and shows that the full semantics is a limit case of Henkin semantics but does not have a monopoly when it comes to categoricity.

## 11. Logics Between First and Second Order

First order logic and second-order logic are in a sense two opposite extremes. There are many logics between them i.e., logics that extend properly first order logic, and are properly contained in second-order logic. One example is the extension of first order logic by the generalized quantifier known as the Henkin quantifier:

$$\left( \begin{array}{cc} \forall x&\exists y\\ \forall u&\exists v \end{array}\right)\phi(x,y,u,v,z_1,\ldots,z_n) $$

which has the meaning

$$\exists f\,\exists g\,\forall x\,\forall u\,\phi(x,f(x),u,g(u),z_1,\ldots,z_n). $$

The extension $L(H)$ of first order logic by the Henkin quantifier is almost the same as second-order logic: they have the same $\Delta$-extension (Krynicki & Lachlan 1979)[^krynicki-1979].[^note-19]

The equicardinality or Härtig quantifier

$$Ixy\,\phi(x,z_1,\ldots,z_n)\psi(x,z_1,\ldots,z_n) $$

has the meaning “there are as many elements *x* satisfying $\phi(x,z_1,\ldots,z_n)$ as there are elements *y* satisfying $\psi(y,z_1,\ldots,z_n)$”, i.e.,

$$ \begin{align} &\exists f[\forall x (\phi(x,z_1,\ldots,z_n)\leftrightarrow\psi(f(x),z_1,\ldots,z_n)) \land {}\\ &\quad\forall x\,\forall y((\phi(x,z_1,\ldots,z_n)\land \phi(y,z_1,\ldots,z_n)\land f(x)=f(y))\to x=y) \land {}\\ &\quad\forall y\,\exists x(\psi(y,z_1,\ldots,z_n)\to (\phi(x,z_1,\ldots,z_n)\land f(x)=y)) ] \end{align} $$

The extension $L(I)$ of first order logic by the Härtig quantifier is weaker[^note-20] than second-order logic as its Löwenheim number can be $<2^\omega$, but if $V=L$, then it is $\Delta$-equivalent with second-order logic (Väänänen 1980, Väänänen and Welch 2023)[^väänänen-1980][^väänänen-2023]. For more on $L(I)$, see Herre, Krynicki, Pinus and Väänänen (1991) as well as Magidor and Väänänen (2011).

Here are some other generalized quantifiers that are clearly second-order definable:

$$ \begin{align} Q_0x\,\phi(x,z_1,\ldots,z_n)& \iff\exists X( |X|\ge\aleph_0 \land \forall x\in X\phi(x,z_1,\ldots,z_n) )\\ Q_1x\,\phi(x,z_1,\ldots,z_n)&\iff\exists X( |X|\ge\aleph_1 \land{} \forall x\in X\phi(x,z_1,\ldots,z_n) )\\ Q^{MM}_1xy\,\phi(x,y,z_1,\ldots,z_n)&\iff\exists X( |X|\ge\aleph_1 \land{} \forall x,y\in X\phi(x,y,z_1,\ldots,z_n) )\\ Q^{cof}_\omega xy\,\phi(x,y,z_1,\ldots,z_n)&\iff \{(x,y):\phi(x,y,z_1,\ldots,z_n)\} \\ & \qquad\qquad\text{ is a linear order of cofinality } \omega \end{align} $$

In *weak second-order logic* we have no function variables and the relation variables range over finite relations only. The resulting logic is in many ways similar to the extension of first order logic by the generalized quantifier $Q_0$. Another way to limit the power of second-order logic is the following: Suppose $\psi$ is a first order formula with an *n*-ary relation variable *X* and no non-logical symbols. For infinite *A*, we define $\ma\models_s Q_{\psi}X\phi$ if and only if there is a relation $P\subseteq M^n$ such that $\ma\models_{s(P/X)}\phi\land\psi$. The quantifier $Q_{\psi}$ allows second-order quantification over relations that satisfies $\psi$. If $\psi$ is $\forall x(x=x)$ we obtain the usual second-order quantifier which we denote $Q_{II}$. If moreover $ n=1$ we obtain the monadic second-order quantifier which we denote $Q_{mon}$. If $n=1$ and $\psi$ says that *X* is a singleton, we obtain the usual first order quantifier which we now denote $Q_I$. Finally, if $\psi$ says *X* is the graph of a permutation of the model, we denote this quantifier by $Q_{1-1}$. Rather surprisingly, it turns out that with the right concept of interpretability the quantifiers $Q_I,Q_{mon},Q_{1-1}$ and $Q_{II}$ are, up to biinterpretability, the *only* second-order quantifiers of the form $Q_{\psi}$ (Shelah 1973)[^shelah-1973].

## 12. Higher Order Logic vis-à-vis Type Theory

There are many ways to further extend second-order logic. The most obvious is third, fourth, and so on order logic. The general principle, already recognized by Tarski (1933 [1956]), is that in higher order logic one can formalize the semantics—define truth—of lower order logic. Therefore one certainly gains expressive power by using higher order logic. Let us take number theory as an example. With first order logic we can express properties such as “*n* is a prime number” and propositions such as “there are infinitely many prime numbers”, Fermat’s Last Theorem and Goldbach’s Conjecture. First order properties of natural numbers fall into a natural hierarchy called the *arithmetical hierarchy* the levels of which are denoted $\Sigma^0_n$ and $\Pi^0_n$. With second-order logic we can talk about properties of sets of natural numbers, or in other words, properties of real numbers. In particular, we can define the rationals. A continuous function on the real numbers is determined by its values on rationals. Also, an open set is determined by which rational points it contains. Using these observations we can talk about continuous functions and open sets of reals. Basic facts in calculus, such as Bolzano’s Theorem stating that “If a continuous function has values of opposite sign inside an interval, then it has a root in that interval” are expressible in second-order logic over the structure $(\oN,+,\cdot)$ of natural numbers. Second-order properties of natural numbers fall into a natural hierarchy called the *analytical hierarchy* and its levels are denoted $\Sigma^1_n$ and $\Pi^1_n$. With third order logic we can talk about *sets* of real numbers. We can write the Continuum Hypothesis in third order logic and ask the hard question, whether the model $(\oN,+,\cdot)$ satisfies this sentence. Third order properties of natural numbers have again a natural hierarchy and its levels are denoted $\Sigma^2_n$ and $\Pi^2_n$.

It is obvious that if we keep a base model, such as $(\oN,+,\cdot)$ fixed, and move to higher and higher order logic, we can express more and more complicated concepts and propositions. However, *third* order logic over

$$\mn_1=(\oN,+,\cdot) $$

is nothing more than *second* order logic over

$$\mn_2=(\P(\oN),E,\oN,+,\cdot), $$

where $E\subseteq \oN\times\P(\oN)$ is the relation $nEr\iff n\in r$, which again is nothing more than *first* order logic over

$$\mn_3=(\P(\P(\oN))),E',\P(\oN),E,\oN,+,\cdot), $$

where $E'\subseteq \P(\oN)\times\P(\P(\oN)$ is the relation $rE'X\iff r\in X$. Moreover, second-order logic over $\mn_1$ is nothing more than first order logic over $\mn_2$. When this line of thought is taken to its limit we can see that first order logic over the cumulative hierarchy of sets covers higher order logic over any individual level $V_\alpha$ of the hierarchy. In a sense, first order logic over the cumulative hierarchy of sets is a very very high order logic over $\mn_1$.

There is a marked similarity in the way $\mn_2$ arises from $\mn_1$ and in the way $\mn_3$ arises from $\mn_2$. In both cases we simply add a power set construction on top of what the model already has. Second-order logic alone is very good with power sets as we saw in §5.3. A consequence of this is that all the higher order logics (of any finite order and up to a point also of infinite order) from second-order on have Turing-equivalent decision problems and the same Hanf- and Löwenheim numbers (see §4). Thus, even though higher than second-order logics are strictly speaking stronger than second-order logic no difference can be seen by the usual criteria of strength of expressive power.

*Type theory* is a systematic approach to higher order logics. Variables are assigned types, just as in second-order logic we have variables for individual type, relation type and function type. In a higher order logic it would make sense to have variables for relations between objects of any lower types as well as functions mapping objects of lower type to objects of lower type. In set theory objects have a rank. Elements of a set have a lower rank than the set itself. However, the difference between set-theoretical rank and typing in type theory is that in set theory the rank can be computed when the set is known while in type theory the type of an object can be seen from the type of the variable that the object is the value of. In a sense type theory imposes from the syntax a type for each object considered while in set theory a set has a rank given by the semantics. Arguably set theory gained dominance over type theory after the 1930s because of its simpler syntax and semantics. On the other hand type theory is used in computer science, especially in the theory of programming languages (see SEP entry on type theory).

## 13. Foundations of Mathematics

Mathematics can be based on set theory. This means that mathematical objects are construed as sets and their properties are derived from the axioms of set theory. The intuitive informal picture behind set theory is that there is a cumulative hierarchy $V_\alpha$ ($\alpha$ an ordinal) of sets and the axioms are intended to describe the basic properties of such sets. This kind of set theoretical foundation of mathematics has become widely accepted among working mathematicians. We refer to the SEP entry on set theory for more details. Alternatives to set theory are at least category theory, constructive mathematics, and second-order logic.

If one tries to follow as a logician the language mathematicians use in their research, one cannot help seeing that they use second-order concepts very freely. For example, the Induction Axiom is without doubt used by mathematicians in the second-order form depicted in (\ref{ind}). In their natural language mathematicians do not hesitate to use higher order concepts, and indeed do not always even (need to) know the difference.

Second-order logic as a foundation for mathematics focuses on mathematical structures rather than mathematical “objects”, as set theory does. In principle every structure has its own “foundation” based on the special features of the structure. The role of second-order logic is to provide a common framework for this. The intuitive informal picture behind second-order logic on a structure is that there is a domain *A* of individuals and then separate domains for all *n*-ary relations for all $n\in\oN$ and for all *n*-ary functions for all $n\in\oN$, associated with *A*. In comparison to the informal picture of set theory, we have only the domains of subsets, relations and functions, not iterations such as sets of sets, sets of sets of sets and so on, as in set theory. Therefore the intuitive picture behind second-order logic is simpler than the picture behind set theory. In particular, there is no transfinite iteration over all ordinals. Most structures $\ma$ used in mathematics have a second-order characterization $\theta_\ma$, see §10. Proving (second order) properties $\phi$ of such structures means deriving $\phi$ from $\theta_\ma$. Opinions differ as to whether this derivation should be a syntactic (formal) derivation using some (incomplete) axiom system of second-order logic or whether it should be a semantic derivation (of the form “Every model of the assumptions is a model of the conclusion”). For a working mathematician there is not much difference and probably a semantic derivation is usually favored.

Suppose a mathematician wants to convince someone about the truth of Bolzano’s Theorem “If a continuous function on the reals has negative values as well as positive values inside an interval, then it has a root in that interval”. They would start with the ordered field of real numbers. It would be (thought to be) clear what this means because the second-order axiomatization of the field is categorical. Then they would take an arbitrary continuous function *f* on this field such that it has values of opposite sign inside a fixed interval $(a,b)$. It would be clear what this means because second-order logic has variables for functions. Let $c,d\in (a,b)$ such that $f(c)<0$ and $f(d)>0$. Without loss of generality, $c<d$. Let $X=\{e\in(a,b) : f(e)<0\}$. Since we have relation variables for subsets of the domain, we can think of *X* simply as a value of such a relation variable. It is obvious that *X* exists, but a priori we could have imposed contradictory conditions on *X* (e.g., $X=\{e : e\notin X\}$) and then we should not be able to claim that it exists. However, in this case the Comprehension Axiom Schema implies that *X* exists. Clearly, $X\ne\emptyset$ and *X* is bounded from above by *d*. One of the second-order axioms characterizing the field of real numbers is that every non-empty set which is bounded from above has a supremum. Thus we can let *z* to be the supremum of *X*. Now it follows from basic properties of continuous functions that $f(z)=0$.

It would be difficult to tell in the above proof whether it was a syntactical derivation from the axioms or a semantic argument. On the surface it looks like a semantic argument. But every step can be derived from the axioms, so it could be considered a shorthand version of a syntactic derivation.

Syntactic derivations in second-order logic based on the Comprehension Axiom Schema and Axioms of Choice are very much like syntactic derivations in set theory. In neither case would a working mathematicians write all the details of the argument but would resort to shorthand notation. In both cases—second-order logic and set theory—we can interpret the proofs as shorthand versions of syntactic formal proofs or as semantic proofs. First order logic satisfies the Completeness Theorem with the help of which semantic proofs can be turned into syntactic formal proofs. Since the Completeness Theorem uses the concept of a first order structure, sentences proved from the axioms are true in all models of the axioms, both countable models and non-standard models. Are they true in the intuitive model of cumulative hierarchy of sets? By the Reflection Theorem such sentences are true in the class of all sets, but since the intuitive model is informal, we cannot *prove* that the class of all sets is the same as the intuitive model.

On the other hand, in order for the Completeness Theorem to be applicable, a semantic argument has to be such that it works whatever model of set theory we are using. This means that a semantic argument in set theory should not use properties of individual models of set theory unless they are universal first order properties of all models of ZFC. In practice this means that if a property such as $CH$, $\Diamond$, $2^{\aleph_0}=\aleph_2$, and so on, is used, it is mentioned separately as an assumption. Non-first order properties of models cannot be used at all, or else the Completeness Theorem cannot be used. Still, sometimes non-first order properties *are* used. For example, we may have an argument that every *countable* model of ZFC satisfies $\phi$. But then, by the Downward Löwenheim-Skolem Theorem, *every* model of ZFC satisfies $\phi$. Thus we have been able to eliminate the non-first order assumption of the countability of the model.

Second-order logic satisfies the Completeness Theorem if Henkin models are used. Thus semantic arguments in second-order logic can be turned into syntactic formal proofs, but as with set theory the semantic argument has to be valid in *all* Henkin models, not only in all of the *full* Henkin models. Thus, as in set theory, the semantic argument cannot use properties of the Henkin models that are not shared by all Henkin models, In particular, fullness (see §9.1) cannot be assumed because in general models it is not a second-order property. What happens to categoricity when fullness is abandoned? We still have internal categoricity, so we can use categoricity in proofs as long as we make sure we work inside one model. One certain way to make sure of this is that we base everything on the axioms, the Comprehension Axiom Schema and the Axioms of Choice.

When second-order logic is used as a foundation for mathematics, a situation may emerge in which third order logic is needed. For example, a *topology* is usually defined as a family of sets and is therefore a third order object. It would be well in the spirit of second-order logic to simply include third (or higher) order logic when needed. Naturally, the Comprehension Axiom Schema and the Axioms of Choice have to be then assumed for third order quantifiers.

We have devoted a fair amount of space in this entry to the power of second-order logic to characterize structures (see §7.1). Putting it briefly, if a structure has mathematical interest, it is second-order characterizable. Structures constructed by means of the Axiom of Choice may escape being second-order characterizable. But, what is the power of second-order logic to demonstrate the *existence* of structures? The axioms, including the Comprehension Axioms and the Axioms of Choice, can be satisfied in a one element domain. So we cannot *prove* from the axioms that there are any structures of size $>1$. This undermines Quine’s characterization of second-order logic as “set theory in sheep’s clothing” (1970, section heading in chapter 5), meant probably to suggest that the ontological commitments of second-order logic are on the same level as those of set theory.

Perhaps the philosophy of second-order logic is that if a structure can be characterized, it exists, echoing Hilbert’s formalist philosophy. However, even in that sense we need to know that the characterizing sentence $\theta_\ma$ is consistent. A trivial approach is to observe that $\ma$ itself certainly satisfies $\theta_\ma$, but this clearly begs the question. Still, this is how Hilbert argues for the consistency of his axioms for the real numbers (1900). If $\ma=(\oN,+,\cdot)$, an Axiom of Infinity saying that that a proper subset of the domain has the same cardinality as the entire domain, is what is needed, as was shown by Dedekind. In combination with the Comprehension Axiom Schema the existence of $\ma$ follows. For $(\oR,+,\cdot,0,1)$ this is not enough, we need a stronger Axiom of Infinity, for example the existence of a dense order which satisfies the Completeness Axiom: Every bounded non-empty set has a supremum. It seems inevitable that when we move from a structure to a bigger structure we need to make a largeness assumption. Such assumptions are called Large Domain Assumptions in Väänänen (2012). In set theory this aspect is taken care of at the outset by assuming the Power Set Axiom and the Replacement Axioms which together make sure that there are large enough sets. In second-order logic we have to assume new and new Large Domain Assumptions, as we move along. This can be seen as a drawback, having to make new assumptions all the time. On the other hand it can be seen as an asset, not having to make too ambitious assumptions before they are really needed.

## 14. Second-Order Arithmetic

Owing to the central role that real numbers play in mathematics, the second-order theory of natural numbers, known as *second-order arithmetic* (Simpson 1999 [2009])[^simpson-1999], and denoted $Z_2$, is an important foundational theory. It is stronger than (first order) Peano arithmetic but weaker than set theory. It has variables for individuals thought of as natural numbers as well as variables for sets of natural numbers thought of as real numbers. In addition there are $+$ and $\times$ for arithmetic operations on the individuals. As axioms $Z_2$ has some rather obvious axioms about $+$ and $\times$, the Induction Axiom (\ref{ind}), and the axioms of second-order logic, including the Comprehension Principles (\ref{CA}). A surprising amount of mathematics can be derived in $Z_2$. We refer to Simpson (1999 [2009]) for details. In a sense, $Z_2$ is a great success story for second-order logic.

*Reverse mathematics* uses $Z_2$ to isolate the exact axioms on which well-known theorems from mathematics rely. In a textbook such theorems are proved perhaps in an informal set theory, but how much set theory is actually needed in each case? For example, we may ask what is the weakest set of axioms from which the Bolzano-Weierstrass Theorem[^note-21] can be proved? How much set theory, comprehension, choice, induction, etc is needed? Since $Z_2$ is a natural and sufficient environment for many mathematical theorems, it is an appropriate framework for answering questions raised by the reverse mathematics program. The main (but not the only) distinctions that are made in reverse mathematics concern the amount of the Comprehension Principle that is needed in proving this or that mathematical result. In particular, the role of Arithmetic and $\Pi^1_1$-Comprehension Principles is clarified. The basic theory of real numbers can be developed on the basis of Arithmetic Comprehension only, but proofs relying on the notion of a countable ordinal require the $\Pi^1_1$-Comprehension Principle. Again, we refer to Simpson (1999 [2009]) for details.

## 15. Second-Order Set Theory

We have up to now treated set theory (ZFC) as a first order theory. However, when Zermelo (1930) introduced the axioms which constitute the modern ZFC axiom system, he formulated the axioms in second-order logic. In particular, his *Separation Axiom* is

$$\forall x\,\forall X\,\exists y\,\forall z(z\in Y\leftrightarrow (z\in x\land X(z))) $$

and the *Replacement Axiom* is

$$\forall x\,\forall F\,\exists y\,\forall z(z\in y\leftrightarrow\exists u(u\in x\land z=F(u))). $$

Second-order ZFC, $\ZFC^2$, is simply the received first order ZFC with the Separation Schema replaced by the above single Separation Axiom, and the Replacement Schema replaced by the above single Replacement Axiom. Accordingly, $\ZFC^2$ is a finite axiom system. Zermelo proved that the models of $\ZFC^2$ are, up to isomorphism, of the form $(V_\kappa,\in)$, where $\kappa$ is (strongly) inaccessible $>\omega$.

Kreisel (1967) has pointed out that second-order set theory in a sense decides the CH, i.e., decides whether it is true or not, even if we do not know which way the decision goes. More exactly $\ZFC^2\models CH$ or $\ZFC^2\models \neg CH$, because $CH$ is true if and only if $V_\kappa\models CH$ for inaccessible $\kappa$, i.e., if and only if $\ZFC^2\models CH$. Of course we can express CH in first order set theory, too, so the situation is not really different from first order set theory. Many set theorists think that the concept of set is definitive enough to decide eventually also CH even if ZFC does not decide it. Likewise, we may argue that the concept of second-order semantics is definitive enough to decide CH even if the current axioms of second-order logic cannot do it.

The question arises, why do we not use second-order set theory $\ZFC^2$ as the metatheory of second-order logic, as recommended in Shapiro (1991). In fact we could use it. However, the question might rise, what is the semantics of our metatheory? In principle such questions can lead to an infinite regress. By using first order set theory as the metatheory, the question about the semantics of the metatheory would simply be the question about the semantics of first order logic. We have pointed out in §6 that semantics of first order logic is absolute relative to ZFC. This gives some assurance that we need not continue asking, what the metatheory is.

## 16. Finite Model Theory

The rise of mathematical logic in the first half of the twentieth century was interwoven with different approaches to understanding the infinite structures of the natural and the real numbers. With the emergence of computer science in the second half of the twentieth century logic went through a process of rebirth. The concepts of a computation and of a database both emphasized the need to understand not so much the finite/infinite distinction as the new measures of degrees of finiteness. For example, the question whether a problem can be decided in polynomial time arose to challenge the well-developed theory of what can be decided in finite time. The analogy between finite relational structures and databases led to the emergence of *finite model theory*. For a good review we refer to Fagin (1993).

In the context of finite models second-order logic does not suffer from the same philosophical problems as in the context of infinite models. It is just one language among many others. One of the early successes was the result of Fagin (1974) to the effect that classes of models definable in existential second-order logic, i.e., in the $\Sigma^1_1$-fragment, are exactly those that are NP, i.e., that can be recognized by a non-deterministic Turing machine running in time which is polynomial in the size of the encoding of the model as a binary sequence. The question whether NP is closed under complements is notoriously open. From the point of view of second-order logic this is surprising because on all models, finite or infinite, $\Sigma^1_1$ is of course not closed under complements. For example, the class of infinite models (in the empty vocabulary) is $\Sigma^1_1$ but not $\Pi^1_1$. Also, the class of well-orders is $\Pi^1_1$ but not $\Sigma^1_1$. Therefore the following early result about second-order logic on finite models was remarkable. Here $\mon\Sigma^1_1$ refers to $\Sigma^1_1$ in monadic second-order logic, similarly $\mon\Pi^1_1$.

**Theorem 17 (Fagin 1975)[^fagin-1975]** Connectivity of graphs is not definable in $\mon\Sigma^1_1$. Hence $\mon\Sigma^1_1\ne\mon\Pi^1_1$.

This has subsequently been extended to graphs with certain other structure present, see Fagin, Stockmeyer, and Vardi (1995). The proofs use the Ehrenfeucht-Fraïssé games (see §3.1) and their elaborations.

Let $\Sigma^1_{1,m}$ denote the class of $\Sigma^1_1$-formulas $\exists X_1\ldots\exists X_k\phi$, where the bound second-order variables $X_i$ are at most *m*-ary and $\phi$ is first order. Similarly $\Pi^1_{1,m}$ and $\Delta^1_{1,m}$.

**Theorem 18 (Ajtai 1983)[^ajtai-1983]** The property of a finite structure $(A,R)$, where *R* is $n+1$-ary, of $|R|$ being even, is $\Delta^1_{1,n+1}$ but not $\Sigma^1_{1,n}$ or $\Pi^1_{1,n}$.

This highly non-trivial theorem is one of the corner stones of the study of second-order logic on finite structures. We do not know whether $\Delta^1_1$ is different from $\Sigma^1_1$ on finite structures, but the above theorem gives an arity-based hierarchy result inside $\Delta^1_1$.

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=logic-higher-order). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/logic-higher-order/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=logic-higher-order&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/logic-higher-order/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

- Solovay, Robert M., 2006, “[An example of an axiomatizable second order theory that is complete but non-categorical?](http://cs.nyu.edu/pipermail/fom/2006-May/010561.html)”, Foundations of Mathematics mailing list, 16 May 2006.
- Enderton, Herbert B., “Second-order and Higher-Order Logic”, *Stanford Encyclopedia of Philosophy* (Summer 2019 Edition), Edward N. Zalta (ed.), URL = <[https://plato.stanford.edu/archives/sum2019/entries/logic-higher-order/](https://plato.stanford.edu/archives/sum2019/entries/logic-higher-order/)>. [This was the previous entry on this topic in the *Stanford Encyclopedia of Philosophy* — see the [version history](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=logic-higher-order).]
- Saarinen, Tapio, Jouko Väänänen, and Hugh Woodin, 2024, “[On the categoricity of complete second order theories](https://arxiv.org/abs/2405.03428)”, manuscript at arXiv.org.

## Related Entries

category theory | computability and complexity | mathematics: constructive | plural quantification | set theory | set theory: independence and large cardinals | set theory: large cardinals and determinacy | type theory

## Notes（原文脚注）

[^note-1]: Classical sources for second-order logic are Hilbert & Ackermann (1938) and Church (1956).

[^note-2]: Suppose a formula $\phi$ is logically equivalent to both $\exists X_1\ldots \exists X_n\,\phi_1$ and $\forall Y_1\ldots \forall Y_m\phi_2,$ where $\phi_1$ and $\phi_2$ are first order. W.l.o.g.

$$\{X_1,\ldots, X_n\}\cap\{Y_1,\ldots, Y_m\}=\emptyset.$$

Now $\models\phi_1\to\phi_2$. By the Craig Interpolation Theorem there is a first order $\theta$ such that $\models\phi_1\to\theta$, $\models\theta\to\phi_2$, and the symbols $X_1,$…, $X_n,$ $Y_1,$…, $Y_m$ do not occur in $\theta$. Hence $\phi$ is logically equivalent with $\theta$.

[^note-3]: Here *E* is a kind of membership relation. Indeed, the formula $\phi_1$ resembles the Axiom of Extensionality of ZFC set theory. Formula $\phi_2$ says that if $E(x,y)$ is read as “*x* is an element of *y*", then the “element" *x* must be an element of *U*. We can easily build a model $\mm$ of $\phi_1\land\phi_2$ as follows. Let *A* be a set such that $A\cap\P(A)=\emptyset$. Here $\P(A)$ denotes the power set of *A*. Note that $A\cap\P(A)=\emptyset$ is always the case if, for example, *A* is a set of singletons $\{a_i\}$, where each $a_i$ has cardinality 2. We let $M=A\cup \P(A)$. As the interpretation of the unary relation variable *U* we choose *A*. Finally, as the interpretation of the binary relation variable *E* we choose the real membership relation, that is,

$$E^\mm=\{(a,b)\in A\times \P(A) : a\in b\}.$$

The last conjunct $\phi_3$ says that if *X* is a subset of *U*, then there is some *y* such that exactly those elements *z* of *U* that satisfy $E(z,y)$ are the ones that are in *X*. In a sense *y* “codes” the set *X*. In our example model $\mm$ we would choose $y=X$ because *M* has all the subsets of *A* as elements. In other models we may not be able to choose $y=X$ because *X* is not an element of the model, just a subset of *U*, coded by *y*. In (6) the variable *X* is universally quantified. The effect of this is that *every* subset of *U* is coded by some element of the model. Thus the above $\mm$ satisfies $\theta$. On the other hand, suppose $\mn$ is an arbitrary model of $\theta$. Let us take a set *A* such that $|A|=|U^\mn|$. We can assume $A\cap\P(A)=\emptyset$, as above. Let $M=A\cup\P(A)$. By letting $U^\mm=A$ and

$$E^\mm=\{(a,b)\in A\times \P(A) : a\in b\}$$

we obtain a model $\mm$ (of $\theta$). Let $\pi:U^\mn\to A$ be a bijection. If $b\in N$, let $\pi(b)=\{a\in A:E^\mn(a,b)\}$. Now $\pi:\mn\cong\mm$.

[^note-4]: The smallest cardinal $\kappa$ such that if a second-order sentence has a model at all, it has a model of cardinality $\le\kappa$.

[^note-5]: The smallest cardinal $\kappa$ such that if a second-order sentence has a model of cardinality $\ge\kappa$, it has arbitrarily large models.

[^note-6]: Let $T\subseteq \ZFC$ be finite. Let *L* be Gödel’s model of constructible sets. Let $\delta$ be an ordinal such that $L\models {}$ “$\delta$ is uncountable”. Let $\lambda>\delta$ be a cardinal such that $(L_\lambda,\in)\models T$. Such $\lambda$ exist, because *T* is finite (by the Reflection Theorem, see, e.g., Kunen 1980)[^kunen-1980]. Let $(N,E)\prec (L_{\lambda},\in)$ be countable with $\delta\in N$, by the Löwenheim-Skolem Theorem of first order logic. By Mostowski’s Collapsing Lemma (see e.g. Kunen 1980)[^kunen-1980], there is a transitive $(N',\in)$ and $\pi:(N,E)\cong (N',\in)$. Let $\eta=\pi(\delta)$. Let $\mm\in N'$ be a structure for the empty vocabulary such that $M=\eta$. Let *s* be an assignment such that $s\in N'$, $s(P)=\eta$ and $s(R)=\omega$. Then $(N',\in)$ is a countable transitive model of *T* with an element $\eta$ such that $(N',\in)\models “\eta\mbox{ is uncountable}”,$ hence $(N',\in)\not\models“\mm\models_s\theta_{\textrm{EC}}(P,R)”,$ that is, if second-order logic is construed inside the transitive model $N'$ of the finite part *T* of ZFC, then in the sense of $N'$ the assignment *s* does not satisfy $\theta_{\textrm{EC}}(P,R)$ in $\mm$, but still $\mm\models_s\theta_{\textrm{EC}}(P,R)$, because $\eta$ is a countable ordinal.

[^note-7]: Here is an example: Suppose $\phi$ is preserved under extensions of the *n*-ary predicate symbol *R*, i.e., if $\mm\models\phi$ and $\mm'$ is the result of extending the predicate *R* in $\mm$, then $\mm'\models\phi$. Then $\phi$ is logically equivalent with a second-order sentence $\psi$ in which *R* occurs only positively. The proof is trivial: Let $\phi'$ be the result of replacing $R(t_1,\ldots, t_n)$ everywhere in $\phi$ by $X(t_1,\ldots, t_n)$. Let $\psi$ be the sentence

$$\exists X(\forall x_1\ldots\forall x_n(X(x_1,\ldots, x_n)\to R(x_1,\ldots, x_n))\land\phi').$$

[^note-8]: Suppose $\phi$ characterizes $\ma$ up to isomorphism. Suppose the constant, predicate and function symbols of $\phi$ are $c_1,\ldots, c_n,R_1,\ldots, R_m, F_1,\ldots, F_k$. Let us replace in $\phi$ constant symbols by individual variables, predicate symbols by relation variables and function symbols by function variables obtaining $\phi'$. Let $\phi^*$ be the sentence

$$\exists x_1\ldots \exists x_n\,\exists X_1\ldots\exists X_m\,\exists F_1\ldots F_k\phi'. $$

Note that $\phi^*$ is a sentence of the empty vocabulary. If a structure (*B*) of the empty vocabulary satisfies $\phi^*$, the structure can be expanded to a model $\mb$ of $\phi$. Then $\mb\cong\ma$, whence $|B|=|A|$. Conversely, if *B* is a set such that there is a bijection $\pi:A\to B$, then $\pi$ can be used to copy the structure of $\ma$ onto (*B*) resulting in a structure $\mb$. By construction, $\mb\cong\ma$, whence $\mb\models\phi$. Clearly now $(B)\models\phi^*$. We have shown that $\phi^*$ characterizes the cardinal $|A|$ (i.e., the structure of cardinality $|A|$ of the empty vocabulary) up to isomorphism.

[^note-9]: W.l.o.g. $M=\kappa$. Since $\kappa$ is measurable, there is an elementary embedding $j:V\to N$ with *N* transitive and ${}^\kappa N\subseteq N$. Thus $\mm\in N$. On the other hand $N\models “j(\mm)\models\phi”$. Also $N\models “\mm\models\phi”$. Clearly $\mm\subseteq j(\mm)$. Thus in *N* the model $j(\mm)$ has a submodel which contains *X*, is of size $<j(\kappa)$ and is a model of $\phi$. Since *j* is elementary, $\mm$ has a submodel of size $<\kappa$ which contains *X* and is a model of $\phi$.

[^note-10]: A cardinal $\kappa$ is weakly compact if it is strongly inaccessible and every $\kappa$-tree, i.e., tree of height $\kappa$ in which the levels have cardinality $<\kappa$ has a branch of length $\kappa$. We can express weak compactness of $\kappa$ with a second-order sentence $\phi$. Since $\lambda$ is weakly compact, $(\lambda)\models\phi$. There cannot be a smaller model of $\phi$, because $\lambda$ is the smallest weakly compact cardinal.

[^note-11]: If a set-theoretical proof involves a set *A*, we can without hesitation also consider the power set $\P(A)$ and even the double power set $\P(\P(A))$. In second-order logic the situation is different. If we have a set *A* of individuals, we can talk about its subsets but we cannot collect them together into the power set $\P(A)$. We can do it in third order logic, but then we cannot form $\P(\P(A))$.

[^note-12]: Mirroring means here the existence of translations in both directions. We shall now define these translations. To simplify notation, let us assume that the individual variables of second-order logic are $x_1,$ $x_2,$…, the constant symbols are $c_1,$ $c_2,$…, the *n*-ary relation variables are $X^n_1,$ $X^n_2,$…, and the *n*-ary function variables are $F^n_1,$ $F^n_2,$…. Respectively, let the variables of our many-sorted logic be as follows:

The variables of sort $\si$ are $v_1,v_2,\ldots$, the *n*-ary relation variables are $w^n_1,w^n_2,\ldots$, and the *n*-ary function variables are $u^n_1,u^n_2,\ldots$.

Let $\Gamma$ consist of the following first order sentences:

$$ \begin{align} &\exists v_1(v_1=c_n), \\ &\forall w^n_m\forall w^n_k(\forall v_1\ldots\forall v_n(\sA(x_1,\ldots, x_n,w^n_m)\leftrightarrow \sA(x_1,\ldots, x_n,w^n_k))\\ &\qquad\to w^n_m=w^n_k), \\ &\forall u^n_m\forall u^n_k(\forall v_1\ldots\forall v_n(\sF(x_1,\ldots, x_n,u^n_m)=\sF(x_1,\ldots, x_n,u^n_k))\\ &\qquad\to u^n_m=u^n_k) \\ \end{align} $$

for $n,m,k\in\oN$. We define a translation $\phi\mapsto\phi^*$ from second-order logic to many-sorted logic as follows:

- $x_n^*$ is $ v_n$, $c^*_n=c_n$,
- $F^n_m(t_1,\ldots, t_n)^*$ is $ \sF(t^*_1,\ldots, t^*_n,u^n_m)$,
- $X^n_m(t_1,\ldots, t_n)^*$ is $ \sA(t^*_1,\ldots, t^*_n,w^n_m)$,
- $(t_1=t_2)^*$ is $ t^*_1=t^*_2$,
- $R(t_1,\ldots, t_n)^*$ is $ R(t^*_1,\ldots, t^*_n)$,
- $(\neg\phi)^*$ is $ \neg\phi^*$,
- $(\phi\land\psi)^*$ is $ \phi^*\land\psi^*$,

similarly for $(\phi\lor\psi)^*$, $(\phi\to\psi)^*$, and $(\phi\leftrightarrow\psi)^*$,

- $(\exists x_n\,\phi)^*$ is $ \exists v_n\,\phi^*$,
- $(\exists X^n_m\,\phi)^*$ is $ \exists w^n_m\,\phi^*$,
- $(\exists F^n_m\,\phi)^*$ is $ \exists u^n_m\,\phi^*$,

similarly for $(\forall x_n\,\phi)^*$, $(\forall X^n_m\,\phi)^*$, and $(\forall F^n_m\,\phi)^*$.

A model $\mm$ of $\Gamma$ gives rise to a general model $(\mm^{\textrm{ms}}, \G^{\textrm{ms}})$ with $M_{s^{\textrm{ind}}}$ as the domain and $\G^{\textrm{ms}}$ consisting for each $n\in\oN$ of the relations

$$\{(a_1,\ldots,a_n) \in M_{s^{\text{ind}}}^n: \mm\models \sA(a_1,\ldots,a_n,b)\},$$

where $b\in M_{s^{\textrm{rel}}_n}$, and of the functions $f: M_{\si}^n\to M_{\si}$ such that

$$f(a_1,\ldots,a_n)= \sF(a_1,\ldots,a_n,b),$$

where $b\in M_{\sr}$. Conversely, every general model is of the form $(\mm^{\text{ms}},\G^{\text{ms}})$ for some many sorted model $\mm$ of $\Gamma$. Now for all second-order sentences $\phi$ and all models $\mm$ of $\Gamma$ we have

$$(\mm^{\textrm{ms}},\G^{\textrm{ms}})\models\phi\iff \mm\models\phi^*.$$

Similarly to $\phi\mapsto\phi^*$ there is also a translation from the many-sorted logic into second-order logic.

[^note-13]: The proof is just as the proof given by Henkin for the Completeness Theorem of first order logic. Suppose we have a countable theory which is consistent in the sense that no contradiction can be derived. We add new constant symbols as witnesses for existential formulas $\exists x\,\phi$, new predicate symbols as witnesses for existential formulas $\exists X\,\phi$, and new function symbols as witnesses for existential formulas $\exists F\,\phi$. Then we extend to a maximal consistent theory. From this we can form a general model by using the new constants as the building blocks of the domain of individuals to get a model $\mm$, the new predicate an function symbols as the building blocks of the $\G$. Naturally, not *all* sets of individual end in $\G$, only those that the construction yields as necessary witnesses. An alternative to this proof is a translation of second-order logic to many sorted logic. Then one can use the Completeness Theorem of many sorted logic.

[^note-14]: Every set of second-order sentences, every finite subset of which has a Henkin model, has itself a Henkin model.

[^note-15]: If a second-order sentence has a Henkin model $(\mm,\G)$ with *M* infinite, it has Henkin models $(\mm,\G)$ with *M* any infinite cardinal.

[^note-16]: By the upward Löwenheim-Skolem Theorem, if *M* is infinite, $\textit{Mod}_H(\phi)$ has Henkin models of all infinite cardinalities.

[^note-17]: I.e., $\pi(x)=x$ for all $x\in E$.

[^note-18]: To prove the equivalence, let us first assume $\theta(P)$ is categorical and $\mm$ is an arbitrary model. We show $\mm\models\categ(\theta(P))$. For this, consider values $R=s(P)$ and $R'=s(P')$ of the variables *P* and $P'$ in $\mm$. Let $A=s(U)$ and $A'=s(U')$ be values of the variables *U* and $U'$ in $\mm$. Assume

$$\mm\models_s\theta(P)^{(U)}\land\theta(P')^{(U')}.$$

Let $\ma$ have *A* as the domain and $R\cap (A\times A)$ as the interpretation of *P*. Let $\ma'$ have $A'$ as the domain and $R'\cap (A'\times A')$ as the interpretation of *P*. Now $\ma\models\theta(P)$ and $\ma'\models\theta(P)$. By categoricity there is an isomorphism $\pi:\ma\cong\ma'$. By letting $s(F)=\pi$ we see that

$$\mm\models_s\isom(U,P,U',P').$$

For the converse, suppose $\models\categ(\theta(P))$. Let $\ma$ and $\ma'$ be two arbitrary models of $\theta(P)$. We define a model $\mm$ of the empty vocabulary by letting $M=A\cup A'$. By assumption,

$$\mm\models\categ(\theta(P)).$$

Let

$$ s(U)=A, s(U')=A', s(P)=P^\ma, s(P')=P^{\ma'}. $$

Since

$$\mm\models\categ(\theta(P)),$$

we have

$$\mm\models_s\isom(U,P,U',P').$$

Thus there is $f:M\to M$ such that $f\restriction A$ demonstrates the isomorphism $\ma\cong\ma'$.

[^note-19]: The $\Delta$-extension of a logic $\mathcal{L}$ is the smallest extension of $\mathcal{L}$ to a logic $\mathcal{L'}$ in which every model class, i.e., class of models of a fixed vocabulary which is closed under isomorphisms, which is, and the complement of which is, a class of (possibly many-sorted) reducts of an $\mathcal{L}$-definable model class, i.e., a class of all models of a sentence of $\mathcal{L}$, is definable. Such an $\mathcal{L'}$ is denote $\Delta(\mathcal{L})$. It can be shown that the $\Delta$-operation preserves many properties of logics, see Makowsky, Shelah, and Stavi (1976).

[^note-20]: The Löwenheim number of second-order logic is obviously $>2^\omega$, i.e., there is a sentence $\phi $ of second-order logic that has models but none of size $\le 2^\omega$. If the Löwenheim number of a sublogic of second-order logic is $<2^\omega$, then there cannot be any sentence of the sublogic equivalent to $\phi$, and in this sense the sublogic is weaker than second-order logic.

[^note-21]: This theorem states that every bounded sequence of real numbers contains a convergent subsequence.

[^ajtai-1979]: Ajtai, M., 1979, “Isomorphism and Higher Order Equivalence”, *Annals of Mathematical Logic*, 16(3): 181–203. doi:10.1016/0003-4843(79)90001-9

[^ajtai-1983]: –––, 1983, “$\Sigma_1^1$-Formulae on Finite Structures”, *Annals of Pure and Applied Logic*, 24(1): 1–48. doi:10.1016/0168-0072(83)90038-6

[^asser-1981]: Asser, Günter, 1981, *Einführung in Die Mathematische Logik: Teil Ill: Prädikatenlogik Höherer Stufe*, Thun: Verlag Harri Deutsch.

[^awodey-2002]: Awodey, Steve and Erich H. Reck, 2002, “Completeness and categoricity. I. Nineteenth-century axiomatics to twentieth-century metalogic”, *History and Philosophy of Logic*, 23(1): 1–30.

[^barwise-1972a]: Barwise, K. Jon, 1972a, “Absolute Logics and $L_{\infty \omega }$”, *Annals of Mathematical Logic*, 4(3): 309–340. doi:10.1016/0003-4843(72)90002-2

[^barwise-1972b]: –––, 1972b, “The Hanf Number of Second Order Logic”, *Journal of Symbolic Logic*, 37(3): 588–594. doi:10.2307/2272748

[^büchi-1962]: Büchi, J. Richard, 1962, “On a Decision Method in Restricted Second Order Arithmetic”, in *Logic, Methodology and Philosophy of Science: Proceedings of the 1960 International Congress*, Ernest Nagel, Patrick Suppes, and Alfred Tarski (eds.), Stanford, CA: Stanford University Press, 1–11.

[^büchi-1973]: –––, 1973, “The Monadic Second Order Theory of $\omega _{i}$”, in *Decidable Theories II: The Monadic Second Order Theory of All Countable Ordinals*, by J. Richard Büchi and Dirk Siefkes, edited by G. H. Müller and D. Siefkes, (Lecture Notes in Mathematics 328), Berlin, Heidelberg: Springer Berlin Heidelberg, 1–127. doi:10.1007/BFb0082721

[^buss-1998]: Buss, Samuel R. (ed.), 1998, *Handbook of Proof Theory*, (Studies in Logic and the Foundations of Mathematics 137), New York: Elsevier.

[^button-2016]: Button, Tim and Sean Walsh, 2016, “Structure and Categoricity: Determinacy of Reference and Truth Value in the Philosophy of Mathematics”, *Philosophia Mathematica*, 24(3): 283–307. doi:10.1093/philmat/nkw007

[^carnap-1927]: Carnap, Rudolf, 1927/1930 [2000]. *Untersuchungen zur allgemeinen Axiomatik*, edited and with a foreword by Thomas Bonk and Jesus Mosterin, Darmstadt: Wissenschaftliche Buchgesellschaft.

[^church-1956]: Church, Alonzo, 1956, *Introduction to Mathematical Logic, volume 1*, Revised and enlarged edition, (Princeton Mathematical Series 17), Princeton, NJ: Princeton University Press.

[^cohen-1966]: Cohen, Paul J., 1966, *Set Theory and the Continuum Hypothesis*, New York-Amsterdam: W. A. Benjamin.

[^craig-1965]: Craig, William, 1965, “Satisfaction for $n$-th order languages defined in $n$-th order languages”, *Journal of Symbolic Logic*, 30: 13–25.

[^cruz-2002]: de la Cruz, Omar, 2002, “Finiteness and Choice”, *Fundamenta Mathematicae*, 173(1): 57–76. doi:10.4064/fm173-1-4

[^durand-1998]: Durand, Arnaud, Ronald Fagin, and Bernd Loescher, 1998, “Spectra with Only Unary Function Symbols”, in *Computer Science Logic*, Mogens Nielsen and Wolfgang Thomas (eds.), (Lecture Notes in Computer Science 1414), Berlin, Heidelberg: Springer Berlin Heidelberg, 189–202. doi:10.1007/BFb0028015

[^durand-2012]: Durand, Arnaud, Neil D. Jones, Johann A. Makowsky, and Malika More, 2012, “Fifty Years of the Spectrum Problem: Survey and New Results”, *The Bulletin of Symbolic Logic*, 18(4): 505–553. doi:10.2178/bsl.1804020

[^elgot-1961]: Elgot, Calvin C., 1961, “Decision Problems of Finite Automata Design and Related Arithmetics”, *Transactions of the American Mathematical Society*, 98(1): 21–21. doi:10.1090/S0002-9947-1961-0139530-9

[^fagin-1974]: Fagin, Ronald, 1974, “Generalized First-Order Spectra and Polynomial-Time Recognizable Sets”, in *Complexity of Computation*, Richard M. Karp (ed.), (SIAM-AMS Proceedings 7), Providence, RI: American Mathematical Society, 43–73.

[^fagin-1975]: –––, 1975, “Monadic Generalized Spectra”, *Zeitschrift für mathematische Logik und Grundlagen der Mathematik*, 21(1): 89–96. doi:10.1002/malq.19750210112

[^fagin-1993]: –––, 1993, “Finite-Model Theory—a Personal Perspective”, *Theoretical Computer Science*, 116(1): 3–31. doi:10.1016/0304-3975(93)90218-I

[^fagin-1995]: Fagin, Ronald, Larry J. Stockmeyer, and Moshe Y. Vardi, 1995, “On Monadic NP vs Monadic Co-NP”, *Information and Computation*, 120(1): 78–92. doi:10.1006/inco.1995.1100

[^feferman-1999]: Feferman, Solomon, 1999, “Does Mathematics Need New Axioms?”, *The American Mathematical Monthly*, 106(2): 99–111. doi:10.1080/00029890.1999.12005017

[^feferman-1966]: Feferman, Solomon and Georg Kreisel, 1966, “Persistent and Invariant Formulas Relative to Theories of Higher Order”, *Bulletin of the American Mathematical Society*, 72(3): 480–486. doi:10.1090/S0002-9904-1966-11507-0

[^fraenkel-1919]: Fraenkel, Abraham, 1919 [1928], *Einleitung in die Mengenlehre* (Die Grundlehren der mathematischen Wissenschaften in Einseldarstellungen: Volume 9), Berlin: Springer, 3rd edition, 1928.

[^frege-1879]: Frege, Gottlob, 1879, *Begriffsschrift: Eine Der Arithmetischen Nachgebildete Formelsprache Des Reinen Denkens*, Halle.

[^frege-1884]: –––, 1884, *Die Grundlagen Der Arithmetik*, Breslau: Verlage Wilhelm Koebner.

[^garland-1974]: Garland, Stephen J., 1974, “Second-Order Cardinal Characterizability”, in *Axiomatic Set Theory, Part 2*, T. J. Jech (ed.), (Proceedings of Symposia in Pure Mathematics, 13.2), Providence, RI: American Math Society, 127–146. [[Garland 1974 available online](http://people.csail.mit.edu/garland/publications/Reprints/1974-Second_Order_Cardinal_Characterizability.pdf)]

[^gaßner-1994]: Gaßner, Christine, 1994, “The Axiom of Choice in Second-Order Predicate Logic”, *Mathematical Logic Quarterly*, 40(4): 533–546. doi:10.1002/malq.19940400410

[^gödel-1931]: Gödel, Kurt, 1931 [1986], “Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I”, *Monatshefte für Mathematik und Physik*, 38(1): 173–198. Reprinted and translated as “On Formally Undecidable Propositions of *Principia Mathematica* and Related Systems” in Gödel 1986: 144–195. doi:10.1007/BF01700692

[^gödel-1936]: –––, 1936 [1986], “Über Die Länge von Beweisen”, *Ergebnisse Eirtes Mathematischen Kolloquiums*, 7: 23–24. Reprinted and translated as “On the Length of Proofs” in Gödel 1986: 396–399.

[^gödel-1939]: –––, 1939 [1990], “Consistency-Proof for the Generalized Continuum-Hypothesis”, *Proceedings of the National Academy of Sciences*, 25(4): 220–224. Reprinted in Gödel 1990: 28–32. doi:10.1073/pnas.25.4.220

[^gödel-1986]: –––, 1986, *Collected Works, Volume 1: Publications 1929-1936*, Solomon Feferman (ed.), New York: Oxford University Press.

[^gödel-1990]: –––, 1990, *Collected Works, Volume 2: Publications 1938-1974*, Solomon Feferman (ed.), New York: Oxford University Press.

[^gurevich-1985]: Gurevich, Yuri, 1985, “Monadic Second-Order Theories”, in *Model-Theoretic Logics*, Jon Barwise and Sol Feferman (eds.) (Perspectives in Logic), New York: Springer-Verlag, 479–506. doi:10.1017/9781316717158.019

[^gurevich-1983]: Gurevich, Yuri, Menachem Magidor, and Saharon Shelah, 1983, “The Monadic Theory of $\omega_2$”, *Journal of Symbolic Logic*, 48(2): 387–398. doi:10.2307/2273556

[^herre-1991]: Herre, Heinrich, Michał Krynicki, Alexandr Pinus, and Jouko Väänänen, 1991, “The Härtig-quantifier. A survey”, *Journal of Symbolic Logic*, 56(4): 1153–1183.

[^hasenjaeger-1961]: Hasenjaeger, Gisbert, 1961, “Unabhängigkeitsbeweise in Mengenlehre Und Stufenlogik Der Modelle.”, *Jahresbericht Der Deutschen Mathematiker-Vereinigung*, 63: 141–162.

[^hellman-2001]: Hellman, Geoffrey, 2001, “Three Varieties of Mathematical Structuralism†”, *Philosophia Mathematica*, 9(2): 184–211. doi:10.1093/philmat/9.2.184

[^henkin-1950]: Henkin, Leon, 1950, “Completeness in the Theory of Types”, *Journal of Symbolic Logic*, 15(2): 81–91. doi:10.2307/2266967

[^herbrand-1930]: Herbrand, Jacques, 1930, *Recherches sur la théorie de la démonstration*, (Thèses de l’entre-deux-guerres 110), L’Université de Paris. [[Herbrand 1930 available online](http://eudml.org/doc/192791)]

[^hilbert-1900]: Hilbert, David, 1900, “Über Den Zahlbegriff.”, *Jahresbericht Der Deutschen Mathematiker-Vereinigung*, 8: 180–183.

[^hilbert-1928]: Hilbert, David and William Ackermann, 1928, *Grundzüge Der Theoretischen Logik*, (Grundlehren Der Mathematischen Wissenschaften in Einzeldarstellungen Mit Besonderer Berücksichtigung Der Anwendungsgebiete 27), Berlin: J. Springer.

[^hilbert-1938]: –––, 1938, *Grundzüge Der Theoretischen Logik*, second edition, Berlin: Springer. doi:10.1007/978-3-662-41928-1

[^hintikka-1955]: Hintikka, K. Jaakko J., 1955, “Reductions in the Theory of Types”, *Acta Philosophica Fennica*, 8: 57–115.

[^hyttinen-2013]: Hyttinen, Tapani, Kaisa Kangas, and Jouko Väänänen, 2013, “On Second-Order Characterizability”, *Logic Journal of IGPL*, 21(5): 767–787. doi:10.1093/jigpal/jzs047

[^jones-1974]: Jones, Neil D. and Alan L. Selman, 1974, “Turing Machines and the Spectra of First-Order Formulas”, *Journal of Symbolic Logic*, 39(1): 139–150. doi:10.2307/2272354

[^krawczyk-1977]: Krawczyk, A. and W. Marek, 1977, “On the Rules of Proof Generated by Hierarchies”, in *Set Theory and Hierarchy Theory V*, Alistair Lachlan, Marian Srebrny, and Andrzej Zarach (eds.) (Lecture Notes in Mathematics 619), Berlin: Springer Berlin Heidelberg, 227–239. doi:10.1007/BFb0067654

[^kreisel-1967]: Kreisel, Georg, 1967, “Informal Rigour and Completeness Proofs”, in *Problems in the Philosophy of Mathematics*, Imre Lakatos (ed.), (Studies in Logic and the Foundations of Mathematics 47), Amsterdam: North-Holland, 138–186. doi:10.1016/S0049-237X(08)71525-8

[^krynicki-1979]: Krynicki, Michał and Alistair H. Lachlan, 1979, “On the Semantics of the Henkin Quantifier”, *Journal of Symbolic Logic*, 44(2): 184–200. doi:10.2307/2273726

[^kunen-1980]: Kunen, Kenneth (ed.), 1980, *Set Theory: An Introduction to Independence Proofs*, (Studies in Logic and the Foundations of Mathematics 102), Amsterdam: North-Holland.

[^lévy-1965]: Lévy, Azriel, 1965, *A Hierarchy of Formulas in Set Theory*, (Memoirs of the American Mathematical Society 57), Providence, RI: American Mathematical Society.

[^lindenbaum-1938]: Lindenbaum, Adolf and Andrzej Mostowski, 1938, “Über Die Unabhängigkeit Des Auswahlaxioms Und Einiger Seiner Folgerungen”, *Sprawozdania z Posiedzeń Towarzystwa Naukowego Warszawskiego, Wydział III Nauk Matematyczno-Fizycznych (Comptes-Rendus Des Séances de La Société Des Sciences et Des Lettres de Varsovie,Classe III)*, 31: 27–32.

[^löwenheim-1915]: Löwenheim, Leopold, 1915, “Über Möglichkeiten im Relativkalkül”, *Mathematische Annalen*, 76(4): 447–470. doi:10.1007/BF01458217

[^lyndon-1959]: Lyndon, Roger C., 1959, “An Interpolation Theorem in the Predicate Calculus.”, *Pacific Journal of Mathematics*, 9(1): 129–142.

[^maddy-2023]: Maddy, Penelope and Jouko Väänänen, 2023, *Philosophical Uses of Categoricity Arguments* (Elements in the Philosophy of Mathematics), Cambridge: Cambridge University Press. doi:10.1017/9781009432894

[^magidor-1971]: Magidor, Menachem, 1971, “On the Role of Supercompact and Extendible Cardinals in Logic”, *Israel Journal of Mathematics*, 10(2): 147–157. doi:10.1007/BF02771565

[^magidor-2011]: Magidor, Menachem and Jouko Väänänen, 2011, “On L¨wenheim-Skolem-Tarski numbers for extensions of first order logic”, *Journal of Mathematical Logic*, 11(1): 87-113. doi:10.1142/S0219061311001018

[^makowsky-1976]: Makowsky, J.A., Saharon Shelah, and Jonathan Stavi, 1976, “Δ-Logics and Generalized Quantifiers”, *Annals of Mathematical Logic*, 10(2): 155–192. doi:10.1016/0003-4843(76)90021-8

[^manzano-1996]: Manzano, María, 1996, *Extensions of First Order Logic*, (Cambridge Tracts in Theoretical Computer Science 19), Cambridge: Cambridge University Press.

[^montague-1963]: Montague, Richard, 1963, “Reductions of Higher-Order Logic”, in *The Theory of Models: Proceedings of the 1963 International Symposium at Berkeley*, J.W. Addison, Leon Henkin, and Alfred Tarski (eds.), Amsterdam: North-Holland, 251–264. doi:10.1016/B978-0-7204-2233-7.50030-7

[^moore-1988]: Moore, Gregory H., 1988, “The Emergence of First-Order Logic”, in *History and Philosophy of Modern Mathematics*, (Minnesota Studies in the Philosophy of Science 11), Minneapolis, MN: University of Minnesota Press, 95–135.

[^mostowski-1938]: Mostowski, Andrzej, 1938, “O niezależności definicji skończoności w systemie logiki” (“On the independence of definitions of finiteness in a system of logic”), *Dodatek do Rocznika Towarzystwa. Matematycznego*, XI: 1–54; English translation in Mostowski 1979.

[^mostowski-1949]: Mostowski, Andrzej, 1949, “An Undecidable Arithmetical Statement”, *Fundamenta Mathematicae*, 36(1): 143–164.

[^mostowski-1979]: Mostowski, Andrzej, 1979, *Foundational Studies. Selected works* (Volume II), Studies in Logic and the Foundations of Mathematics: Volume 93, Amsterdam-New York: North-Holland Publishing Co.; PWN-Polish Scientific Publishers, Warsaw, 1979, edited by Kazimierz Kuratowski, Wiktor Marek, Leszek Pacholski, Helena Rasiowa, Czesław Ryll-Nardzewski and Paweł Zbierski.

[^parsons-1990]: Parsons, Charles, 1990, “The Structuralist View of Mathematical Objects”, *Synthese*, 84(3): 303–346. doi:10.1007/BF00485186

[^quine-1970]: Quine, W. V. O., 1970, *Philosophy of Logic*, Cambridge, MA: Harvard University Press.

[^rabin-1968]: Rabin, Michael O., 1968, “Decidability of Second-Order Theories and Automata on Infinite Trees”, *Bulletin of the American Mathematical Society*, 74(5): 1025–1030. doi:10.1090/S0002-9904-1968-12122-6

[^rabin-1959]: Rabin, Michael O. and Dana Scott, 1959, “Finite Automata and Their Decision Problems”, *IBM Journal of Research and Development*, 3(2): 114–125. doi:10.1147/rd.32.0114

[^resnik-1988]: Resnik, Michael D., 1988, “Second-Order Logic Still Wild”, *The Journal of Philosophy*, 85(2): 75–87. doi:10.2307/2026993

[^schmidt-1951]: Schmidt, Arnold, 1951, “Die Zulässigkeit der Behandlung mehrsortiger Theorien mittels der üblichen einsortigen Prädikatenlogik”, *Mathematische Annalen*, 123(1): 187–200. doi:10.1007/BF02054948

[^scott-1961]: Scott, Dana, 1961, “Measurable Cardinals and Constructible Sets”, *Bulletin de l’Académie Polonaise des Sciences, Série des sciences mathématiques, astronomiques et physiques*, 9: 521–524.

[^shapiro-1991]: Shapiro, Stewart, 1991, *Foundations without Foundationalism: A Case for Second-Order Logic*, New York: Oxford University Press. doi:10.1093/0198250290.001.0001

[^shelah-1973]: Shelah, Saharon, 1973, “There Are Just Four Second-Order Quantifiers”, *Israel Journal of Mathematics*, 15(3): 282–300. doi:10.1007/BF02787572

[^shelah-2004]: –––, 2004, “Spectra of Monadic Second Order Sentences”, *Scientiae Mathematicae Japonicae*, (Special issue on set theory and algebraic model theory), 59(2): 351–355. [[Shelah 2004 available online](http://www.jams.or.jp/scm/contents/Vol-9-6/9-52.pdf)]

[^simpson-1999]: Simpson, Stephen G., 1999 [2009], *Subsystems of Second Order Arithmetic*, second edition, (Perspectives in Logic), Cambridge: Cambridge University Press. first edition in 1999, New York: Springer. doi:10.1017/CBO9780511581007

[^siskind-2023]: Siskind, Benjamin, Paolo Mancosu and Stewart Shapiro, 2023, “A note on choice principles in second-order logic” *Review of Symbolic Logic*, 16(2): 339–350. doi:10.1017/S1755020320000301

[^tarski-1933]: Tarski, Alfred, 1933 [1956], *Pojęcie Prawdy w Językach Nauk Dedukcyjnych* (*Le concept de vérité dans les langages formalisés*), (Prace Towarzystwa Naukowego Warszawskiego, Wydział III Nauk Matematyczno-fizycznych/Travaux de la Société des Sciences et des Lettres de Varsovie, Classe III Sciences Mathématiques et Physiques, 34), Warsaw. German translation see Tarski 1936. English translation as “The Concept of Truth in Formalized Languages” in Tarski 1956: chapter 8: 152–278.

[^tarski-1936]: –––, 1936 [1956], “Der Wahrheitsbegriff in Den Formalisierten Sprachen”, *Studia Philosophica*, 1: 261–405. Translated as “The Concept of Truth in Formalized Languages” in Tarski 1956: chapter 8.

[^tarski-1956]: –––, 1956, *Logic, Semantics, Metamathematics; Papers from 1923 to 1938*, J. H. Woodger (trans.), Oxford: Clarendon Press.

[^tharp-1973]: Tharp, Leslie H., 1973, “The Characterization of Monadic Logic”, *Journal of Symbolic Logic*, 38(3): 481–488. doi:10.2307/2273046

[^väänänen-1979]: Väänänen, Jouko, 1979, “Abstract Logic and Set Theory. I. Definability”, in *Logic Colloquium ’78: Proceedings of the Colloquium Held in Mons*, Maurice Boffa, Dirk van Dalen, and Kenneth Mcaloon (eds.), (Studies in Logic and the Foundations of Mathematics 97), Amsterdam: Elsevier, 391–421. doi:10.1016/S0049-237X(08)71637-9

[^väänänen-1980]: –––, 1980, “Boolean Valued Models and Generalized Quantifiers”, *Annals of Mathematical Logic*, 18(3): 193–225. doi:10.1016/0003-4843(80)90005-4

[^väänänen-2012]: –––, 2012, “Second Order Logic or Set Theory?”, *The Bulletin of Symbolic Logic*, 18(1): 91–121. doi:10.2178/bsl/1327328440

[^väänänen-2015]: Väänänen, Jouko and Tong Wang, 2015, “Internal Categoricity in Arithmetic and Set Theory”, *Notre Dame Journal of Formal Logic*, 56(1): 121–134. doi:10.1215/00294527-2835038

[^väänänen-2023]: Väänänen, Jouko and Philip Welch, 2023, “When cardinals determine the power set: inner models and Härtig quantifier logic”, *Mathematical Logic Quarterly*, 69(4): 460–471. doi:10.1002/malq.202200030

[^walmsley-2002]: Walmsley, James, 2002, “Categoricity and Indefinite Extensibility”, *Proceedings of the Aristotelian Society*, 102(1): 239–257. doi:10.1111/j.0066-7372.2003.00052.x

[^wang-1952]: Wang, Hao, 1952, “Logic of Many-Sorted Theories”, *Journal of Symbolic Logic*, 17(2): 105–116. doi:10.2307/2266241

[^zermelo-1930]: Zermelo, Ernst, 1930, “Über Grenzzahlen und Mengenbereiche: Neue Untersuchungen über die Grundlagen der Mengenlehre”, *Fundamenta Mathematicæ*, 16: 29–47.
