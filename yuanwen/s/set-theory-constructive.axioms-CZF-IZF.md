# set-theory-constructive — axioms-CZF-IZF（supplement）

> （《set-theory-constructive》词条补充材料，源：plato.stanford.edu/entries/set-theory-constructive/axioms-CZF-IZF.html）

#### Supplement to Set Theory: Constructive and Intuitionistic ZF

## Axioms of CZF and IZF

The theories Constructive Zermelo-Fraenkel (CZF) and Intuitionistic Zermelo-Fraenkel (IZF) are formulated on the basis of intuitionistic first order logic, $\mathbf{IQC}$ (see the entry on Intuitionistic Logic). As they are usually formulated, they include among the logical axioms the equality axioms, which state that equality, =, is reflexive and that equal terms can be substituted for one another in any formula. The language of CZF and IZF is the same as that of classical ZF, thus it has only the binary predicate symbol $\in$ (membership) as non-logical symbol. We recall that as we work in intuitionistic logic, all the binary connectives and the quantifiers $(\wedge , \vee , \rightarrow , \exists , \forall)$ are taken as primitive (none is defined in terms of any of the others). As is usual, we define negation by means of implication and the constant $\bot$ (absurdity): $\neg \phi$ abbreviates $\phi \rightarrow \bot$. We also write $\phi \leftrightarrow \psi$ for $\phi \rightarrow \psi \wedge \psi \rightarrow \phi$. We write $\forall X\in Y$ and $\exists X\in Y$ for $\forall X(X\in Y \rightarrow \ldots$) and $\exists X(X\in Y \wedge \ldots$), respectively.

In the following we first introduce all the axioms, with names, and then we define the two systems CZF and IZF. We also recall some choice principles which are compatible with constructive and intuitionistic ZF, and finally give two examples of very simple proofs in CZF. For the sake of readabiliy, we use lower and upper case letters to denote sets.

This document is organised as follows:

- Set-theoretic Axioms
- Choice Principles
- Two Examples

### Set-theoretic Axioms

**1. Extensionality:** $\forall x\forall y[\forall z(z\in x \leftrightarrow z\in y) \rightarrow x=y].$

Extensionality enables us to identify sets which might be defined in different ways but happen to have the same elements. This is the axiom which enables us to use the article *the* after the application of any of the other axioms. Consider, for example, the next axiom (Pair): given two sets $X$ and $Y$, the axiom ensures the existence of $a$ set whose elements equal either $X$ or $Y$. Extensionality ensures furthermore that there is only one such a set, *the* unordered pair of $X$ and $Y$. This set is usually informally written as: $\{X, Y\}$.

**2. Pair:** $\forall x\forall y\exists z\forall w(w\in z \leftrightarrow w=x \vee w=y)$.

As particular case of application of pair, given a set $X$ we can form the singleton set $\{X\}$, which is the pair $\{X,X\}$.

**3. Union:** $\forall x\exists y\forall z[z\in y \leftrightarrow \exists w(w\in x \wedge z\in w)].$

Given a set $X$, union allows us to form a set $Y$ whose elements are elements of elements of $X$. By combining union and pair one can form the usual (binary) union of two sets.

**4. Empty set:** $\exists x\forall$y $\neg(y \in x)$.

By extensionality the empty set is unique; we denote it by the symbol $\varnothing$.

**5. Infinity:** $\exists x[\varnothing \in x \wedge \forall y(y\in x \rightarrow suc(y)\in x)]$.

Here for set $X$, $suc(X)$ (the successor of $X)$ is defined as $X\cup \{X\}$. For any set $X$, $suc(X)$ exists by union and pair (and is unique by extensionality).

**6. Separation schema:** $\forall a\exists x\forall y(y\in x \leftrightarrow y\in a \wedge \phi(y))$,   where $x$ is not free in $\phi(y)$.

Given a set $A$, separation allows one to form a new set, all of whose elements are elements of $A$ and also satisfy a condition described by a formula $\phi$. This set is informally written as: $\{Y\in A : \phi(Y)\}$.

**$6'$. Restricted separation schema:** This is the same as separation but holds for *bounded* formulas $\phi(y)$ only. A formula is *bounded* if all its quantifiers are bounded; *i.e.*, they occur only in one of the forms $\forall X\in Y$ or $\exists X\in Y$. Bounded formulas are also called restricted or $\Delta_0$-formulas. Accordingly, bounded separation is also called *restricted separation* or *$\Delta_0$ separation*.

In *bounded* separation we require that if quantifiers occur in $\phi$, they do so only in bounded contexts. By so doing, we ensure that quantification acts on “previously” constructed sets only. We thus avoid impredicative contexts in which one quantifies on the whole universe of sets, also including the set under construction (see the section on Predicativity in constructive set theory of the main article).

**7. Collection schema:** $\forall a[\forall x\in a \exists y \phi(x,y) \rightarrow \exists b\forall x\in a \exists y\in b \phi(x,y)],$  for all formulas $\phi(x,y)$ where $b$ is not free in $\phi(x,y)$.

Collection states that if for each element $X$ of a given set $A$ we can find a set $Y$ such that a relation holds of $X$ and $Y$, then we can find a set $B$ which collects “some” of these $Y$s. That is, $B$ is such that for each element $X$ of $A$ there is a $Y$ in $B$ such that the relation holds of $X$ and $Y$.

**$7'$. Replacement:** $\forall a[\forall x\in a \exists !y \phi(x,y) \rightarrow \exists b\forall x\in a \exists y\in b \phi(x,y)],$   for all formulas $\phi(x,y)$ where $b$ is not free in $\phi(x,y)$.

Note that the antecedent of replacement is a strengthening of the antecedent of collection, as it states that for each $X$ in $A$ there is *exactly one* $Y$ such that $\phi(X,Y)$ holds. Replacement can be seen as stating that if the domain of a function is a set, than its range is also a set.

**$7''$. Strong collection schema:** $\forall a[\forall x\in a \exists y \phi(x,y) \rightarrow $ $\exists b(\forall x\in a \exists y\in b \phi(x,y) \wedge \forall y\in b \exists x\in a \phi(x,y))],$   for all formulas $\phi(x,y)$ where $b$ is not free in $\phi(x,y)$.

This is a strengthened form of collection which is introduced in systems with bounded separation.

**8. Powerset:** $\forall x\exists y\forall z[z\in y \leftrightarrow \forall w(w\in z \rightarrow w\in x)].$

Powerset allows us to form a set of all subsets of a given set $X$.

**$8'$. Subset collection schema:** $\forall a\forall b\exists c\forall u[\forall x\in a \exists y\in b \phi(x, y, u) \rightarrow$ $ \exists d\in c(\forall x\in a \exists y\in d \phi(x, y, u) \wedge \forall y \in d \exists x \in a \phi(x, y, u))],$   for all formulas $\phi(x,y,u)$ where $c$ is not free in $\phi(x,y,u)$.

In CZF, the subset collection schema takes the place of the powerset axiom. As the subset collection schema is particularly intricate, we can clarify its meaning by introducing the axiom of **fullness**, which is equivalent to subset collection on the basis of CZF minus subset collection (Aczel 1978). First some terminology. The notion of relation between two sets $A$ and $B$ is defined in CZF as usual: a relation is a set of ordered pairs, the first component of which is an element of $A$ and the second component of which is an element of $B$. The notion of ordered pair is also standard (see example 2 below). We say that a relation $R$ between $A$ and $B$ is *total* if for each element $X$ in $A$ there is an element $Y$ in $B$ such that $R$ holds of $X$ and $Y$. Given sets $A$ and $B$, we say that a set $C$ is *full in* $A$ *and* $B$ if

1. every element of $C$ is a total relation, and
2. for each total relation $R$ between $A$ and $B$, there is a total relation $S$ in $C$ such that $S$ is a subset of $R$.

The axiom of **fullness** states:

$\forall A\forall B\exists C [C \text{ is full in } A \text{ and } B].$

Compared with powerset, fullness can be seen as focusing on total relations, that is, on particular kinds of subsets of the Cartesian product of two sets, rather than on arbitrary subsets of a given set. Given two sets $A$ and $B$, fullness may be read as stating the existence of a set containing an “approximation” of each total relation between $A$ and $B$. Note that fullness does not state the existence of a set of *all* total relations between two sets, as this would be the same as postulating powerset in the context of CZF minus subset collection (Aczel and Rathjen 2001, Ch. 3). In addition, it does not say that each relation can be “thinned down” to a function, as this would amount to postulating the axiom of choice.

**9. $\in$-Induction:** $\forall a(\forall y\in a \phi(y) \rightarrow \phi(a)) \rightarrow \forall a \phi(a)$,   for every formula $\phi(a)$.

Set induction allows us to induct on the membership relation. It states the following: suppose that for an arbitrary set $A$, whenever a property $\phi$ holds of all elements of $A$ then it propagates to $A$ itself; then we can conclude that the property $\phi$ holds of any set $A$.

This schema replaces ZF’s axiom of foundation whose usual formulation, as we have explained in the main document, is incompatible with set theories based on intuitionistic logic (for the argument see the supplementary document [Set theoretic principles incompatible with intuitionistic logic](set-theory-constructive.incompatible-set-axs.md).)

We also note here that foundation is called Regularity in the article Zermelo Fraenkel set theory in this Encyclopedia. Either terminology can be found in the literature. Here we prefer to use the name *foundation* because in the context of CZF regularity usually refers to a different notion, originating from the classical notion of regular cardinal.

We can now define the theories in question:

$\mathbf{CZF}$: Principles $1, 2, 3, 4, 5, 6', 7'', 8', 9$.

The system IZF extends CZF by allowing unrestricted separation and powerset.

$\mathbf{IZF}$: Principles 1, 2, 3, 4, 5, 6, 7, 8, 9.

Note that IZF has often been formulated with the natural numbers as urelements (see Friedman 1973a, Beeson 1985). A well-known variant of IZF, called IZF$_{Rep}$, is obtained by replacing 7 by $7'$.

The following theorem holds:

CZF + EM = IZF + EM = IZR$_{Rep}$ + EM = ZF,

where EM denotes the principle of the excluded middle (for CZF see Aczel 1978).

Remark: In CZF only the bounded separation schema introduces a restriction on the complexity of the formulas occurring in it, while all the other schemata allow for arbitrary formulas. Note, in particular, that the schemata of collection are unrestricted. This is due to the fact that even the unrestricted schemata are validated by Aczel’s interpretation of constructive set theory in Martin-Löf type theory. It is interesting to note that their interpretation makes essential use of the validity in type theory of the axiom of choice (see the discussion on constructive choice principles in the main article). To avoid making use of the type-theoretic axiom of choice Aczel and Gambino (2002) have proposed a refinement of Aczel’s original interpretation of constructive set theory in type theory by introducing a variant of type theory known as logic-enriched type theory.

We also note that on the basis of CZF minus subset collection, subset collection clearly implies Myhill’s exponentiation axiom, which states that the collection of all functions from a set $A$ to a set $B$ is a set. Also, powerset clearly implies subset collection. These implications, however, cannot be reverted. The fact that subset collection is not as strong as powerset is a consequence of the fact that the proof-theoretic strength of CZF minus subset collection plus powerset exceeds by far that of CZF (Aczel and Rathjen 2001, Rathjen 2012b). That exponentiation does not imply fullness in intuitionistic contexts has been proved by Lubarsky (2005).

### Choice Principles

We here recall the principles of **Countable** and **Dependent Choice**.

Let $\omega$ denote the set of natural numbers (which exists by the infinity axiom). Countable Choice, **AC$_0$**, is the following principle (for any $\psi)$:

$\forall x \in \omega \exists y \in v \psi(x,y) \rightarrow (\exists f: \omega \rightarrow v) \forall x \in \omega \psi(x,f(x))$,

where $f: \omega \rightarrow v$ is an abbreviation for a formal statement expressing the fact that $f$ is a function with domain $\omega$ and range contained in $v$.

Dependent choice, $\mathbf{DC}$, is the following statement (for any $\psi)$:

if $\forall x \in a \exists y \in a \psi(x,y)$ and $b_0 \in a$, then there is $f: \omega \rightarrow a$ such that $f$(0) $= b_0$ and $\forall n \in \omega \psi(f(n), f(n+1))$.

We should also like to mention a consequence of Replacement often called the axiom of **unique choice** (it has also been termed the axiom of **non-choice** in (Myhill 1975) for obvious reasons). This is the statement: if for each element $X$ of $A$ there is *exactly one* $Y$ such that a property holds, than we can find a function $F$ with domain $A$ which assigns to each element $X$ of $A$ an element $F(X)$ such the given property holds. That is:

$\forall x \in A\, \exists ! y\, \psi(x,y) \rightarrow$ $\exists f (\text{Function}(f)\wedge \text{Domain}(f)= A \wedge \forall x \in A \psi(x,f(x)))$,

This principle is clearly valid in the set theories presented above, in which Replacement holds.

See also the discussion on choice principles in the main document: Constructive and intuitionistic ZF; there another constructive choice principle, the presentation axiom, is recalled.

### Two Examples

In a constructive context we sometimes need to be more careful than usual with the proofs of even simple facts. To illustrate this, we now give two simple examples. The first one exemplifies how intuitionistic logic can be used in set theory. The second example illustrates how one can avoid unnecessary impredicative reasoning (thus the proof is not specifically intuitionistic).

1. *Ordered pairs* In the first example we show that if two ordered pairs are equal, then their first and second coordinates are equal, respectively. The notion of ordered pair can be defined in the same way as in classical set theory, that is $(A,B)$ is $\{\{A\}, \{A,B\}\}$. The present proof differs from the one in the supplement Basic set theory to the entry on set theory, because that one argues by cases, depending on whether or not $A = B$. To avoid making use of the principle of excluded middle we can instead argue as follows. Assume that $(A,B) = (C,D)$, that is, $\{\{A\}, \{A,B\}\} = \{\{C\}, \{C,D\}\}$. We want to prove that $A = C$ and $B = D$. As $\{A\}$ is an element of the left-hand side it is also an element of the right-hand side and so either $\{A\} = \{C\}$ or $\{A\} = \{C, D\}$. In either case $A = C$. As $\{A, B\}$ is an element of the left-hand side it is also an element of the right-hand side and so either $\{A,B\} = \{C\}$ or $\{A,B\} = \{C,D\}$. In either case $B = C$ or $B = D$. If $B = C$ then $A = B = C$ so that $\{C\} = \{C,D\}$ giving $C = D$ and hence $B = D$. So in either case $B = D$.
2. *Cartesian products* Given sets $A$ and $B$ we now want to form the cartesian product of $A$ and $B$. This is the set, denoted $A \times B$, of all ordered pairs of the from $(X,Y)$, with $X$ element of $A$ and $Y$ element of $B$. The present proof should be compared with standard ones which use powerset. Fix $X$ in $A$ and observe that for every $Y$ in $B$ there is $Z$ such that $Z = (X,Y)$. By extensionality this set is unique. Apply now replacement to obtain a set $C$ of those pairs of the form $(X,Y)$ for $Y$ in $B$, *i.e.* $C = \{(X,Y) : Y \in B\}$. As for every $X$ in $A$ we can find such a $C$ (and it is unique), we can apply replacement again and then union to get a set $D$ as required. That is, $D$ is such that for every $X$ in $A$ and $Y$ in $B$ there is $W$ in $D$ such that $W = (X,Y)$.

For more detailed presentations of IZF and CZF the reader may wish to consult (Beeson 1985; Troelstra and van Dalen 1988; Aczel and Rathjen 2001; 2010).

Bibliographic information for this supplementary document is in the Bibliography for this entry.
