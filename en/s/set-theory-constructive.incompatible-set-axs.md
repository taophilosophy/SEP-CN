# set-theory-constructive — incompatible-set-axs（supplement）

> （《set-theory-constructive》词条补充材料，源：plato.stanford.edu/entries/set-theory-constructive/incompatible-set-axs.html）

#### Supplement to Set Theory: Constructive and Intuitionistic ZF

## Set-theoretic Principles Incompatible with Intuitionistic Logic

In this supplementary document we show how two well-known set-theoretic principles, foundation and choice, are incompatible with Zermelo-Fraenkel set theories based on intuitionistic logic: the assumption of either of these principles implies constructively unacceptable instances of the principle of the excluded middle (EM). (See also the discussion on these principles in the main document: Constructive and intuitionistic ZF.) We also briefly discuss another principle (linearity of ordinals) that gives rise to exlcuded middle. For the sake of readabiliy, we use lower and upper case letters to denote sets.

- Foundation implies instances of EM
- The axiom of choice implies instances of EM
- Constructive ordinals

### Foundation implies instances of EM

The axiom of foundation (or regularity) states that every inhabited (non-empty) set has an $\in$-minimal element. Formally:

$\forall x[\exists y \in x \rightarrow \exists y(y \in x \wedge \forall z(z \in y \rightarrow \neg(z \in x)))$].

Here we show that constructively unacceptable instances of the excluded middle can be derived from foundation on the basis of some very elementary set-theoretic assumptions. As a consequence, foundation, as usually formulated, can not be part of a ZF set theory based on intuitionistic logic. The following argument can be carried out on the basis of a subsystem of [CZF](set-theory-constructive.axioms-CZF-IZF.md) including extensionality, bounded separation, emptyset, and the axiom of pair. In such a system we can form the set $\{0,1\}$ of the von Neumann natural numbers 0 and 1, where 0 is the empty set and 1 is the singleton containing the empty set only.

Let *ψ* be an arbitrary bounded formula and assume foundation. By bounded separation, let

$A := \{y \in \{0,1\}: y = 1 \vee(y = 0 \wedge \psi)\}.$

We can now easily derive the excluded middle for *ψ*. As $1 \in A$, the set $A$ is inhabited. By foundation there exists a minimal element $Y \in A$, that is, a $Y \in A$ such that for all $Z \in Y, Z$ does not belong to $A$. Since $Y$ is an element of $A$, we have either $Y = 1$ or $Y = 0 \wedge \psi$.

- If $Y = 1$, then $0 \in Y$. Thus $\neg(0 \in A)$ because $Y$ is the $\in$-minimal of $A$. Hence, by the definition of $A, \neg(0 = 0 \wedge \psi)$. Thus $\neg \psi$.
- If instead $Y = 0 \wedge \psi$, then clearly *ψ*.

In either case, we have $\psi \vee \neg \psi$.

This argument shows that in a basic constructive set theory, we can prove excluded middle for bounded sentences if we assume foundation. In systems with full (i.e. unbounded) separation, as [IZF](set-theory-constructive.axioms-CZF-IZF.md), the same argument can be used to show that the full principle of excluded middle, EM, is derivable from foundation.

### The axiom of choice implies instances of EM

Here we show that the axiom of choice (AC) implies constructively unacceptable instances of the excluded middle within a basic constructive set theory (Zermelo-Fraenkel style). Therefore we can not assume AC in any reasonable ZF set theory based on intuitionistic logic. The following argument can be carried out, for example, on the basis of a subtheory of CZF that includes extensionality, pair, union, empty set, infinity, bounded separation, replacement and bounded induction on the natural numbers. Such a system essentially coincides with Aczel and Rathjen’s Elementary Constructive Set Theory, ECST, in (Aczel and Rathjen 2010). There the authors show that ECST is already sufficient to carry out a number of basic set-theoretic constructions. It is however a very weak theory, as it can not prove the existence of the addition function on the natural numbers (Rathjen 2008). Note that extensionality and separation play an essential role in the following proof.

By AC we denote the principle:

$\forall u\forall v[(\forall x \in u)(\exists y \in v) \psi(x,y) \rightarrow$ $\exists f: u \rightarrow v)(\forall x \in u) \psi(x,f(x))],$

where “$F: U \rightarrow V$” stands for a formula expressing the fact that $F$ is a set theoretic function with domain $U$ and range included in $V$. The notions of set theoretic function, domain and range can be formalised in a standard way in constructive set theory (see, *e.g.*, Aczel and Rathjen 2001).

Let *φ* be a bounded formula and define the following sets (by bounded separation):

- $A {:}= \{n \in \{0,1\} : n = 0 \vee(n = 1 \wedge \phi)\},$
- $B {:}= \{n \in \{0,1\} : n = 1 \vee(n = 0 \wedge \phi)\}.$

We note that $(\forall z \in \{A,B\})(\exists n \in \{0,1\})(n \in z)$.

By AC, there is a choice function $F: \{A,B\} \rightarrow \{0,1\}$, with $F(A) \in A$ and $F(B) \in B$. Here we need to use a crucial fact about the natural numbers. As the values of $F$ are natural numbers we can prove (by a bounded form of induction on the natural numbers) that either $F(A) = F(B)$ or $F(A) \ne F(B)$. Now we argue as follows.

- If $F(A) = F(B)$, then *φ*, so $\phi \vee \neg \phi$.
- If $F(A) \ne F(B)$, then we show $\neg \phi$. Suppose for a contradiction that *φ* holds. Then *by extensionality* $A = B$ so that $F(A) = F(B)$, contradicting the assumption. We thus have proved that the assumption of *φ* yields a contradiction, so that $\neg \phi$. Thus $\phi \vee \neg \phi$.

In either case, we have proved $\phi \vee \neg \phi$.

Also in this case, the same argument can be used to show that EM follows from AC in a system with full separation instead of bounded separation.

We recall that even if the full axiom of choice is not compatible with constructive and intuitionistic set theories, some consequences of AC, like countable choice, can be added to constructive and intuitionistic ZF (see the main document, section on Constructive Choice Principles).

### Constructive ordinals

Arguments analogous to those just presented can be used to show that standard classical properties of the ordinals, such as the linearity of their order, imply instances of EM.

There are various classically equivalent definitions of ordinal number. In a constructive context, ordinals are usually defined as hereditarily transitive sets (following Powell 1975). A set is *transitive* if its elements are subsets of it. That is, $U$ is transitive if $\forall X \in U (X \subseteq U)$, that is, $\forall X \in U \forall Z \in X (Z \in U)$. An ordinal is then defined as a transitive set all of whose elements are also transitive. The order on the ordinals is given by the membership relation. Linearity of an ordinal *α* is the property: $\forall \beta \in \alpha \forall \gamma \in \alpha(\beta \in \gamma \vee \beta = \gamma \vee \gamma \in \beta)$. It is an easy exercise to prove (using arguments analogous to those above) that assuming linearity for all ordinals yields instances of the excluded middle.

This example shows that in constructive set theory the notion of ordinal does not play the same central role as in classical set theory. However, ordinals supply us with a ranking of the universe and we can still define many of the familiar set-theoretic operations by transfinite recursion on ordinals (see Aczel and Rathjen 2001, Section 4.2). This is fine as long as the definitions by transfinite recursion do not make case distinctions such as in the classical ordinal cases of successor and limit.

Bibliographic information for this supplementary document is in the Bibliography for this entry.
