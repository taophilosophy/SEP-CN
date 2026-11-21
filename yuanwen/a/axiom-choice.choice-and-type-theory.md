# axiom-choice — choice-and-type-theory（supplement）

> （《axiom-choice》词条补充材料，源：plato.stanford.edu/entries/axiom-choice/choice-and-type-theory.html）

#### Supplement to The Axiom of Choice

## The Axiom of Choice in Type Theory

In conclusion, we examine the role of the Axiom of Choice in type theory. The type theory we consider here is the *constructive dependent type theory* (**CDTT**) introduced[^note-sup1] by Per Martin-Löf (1975, 1982, 1984) . This theory is both predicative (so that in particular it lacks a type of propositions), and based on intuitionistic logic[^note-sup2]. Also, as its name indicates, it contains *dependent* types, wherein types can depend on, or “vary over” other types. Type symbols may accordingly take the form $\bB(x)$, with $x$ a variable of a given type $\bA: \bB(x)$ is then a type dependent on or varying over the type $\bA$. It is through the presence of dependent types that *AC* becomes expressible in **CDTT**.

**CDTT** embodies the so-called *propositions-as- types* doctrine, the central thesis of which is that each proposition is to be *identified* with the type, set, or assemblage of its proofs[^note-sup3]. As a result, such proof types, or sets of proofs, have to be accounted the *only* types, or sets. Strikingly, then, in the propositions-as-types doctrine, a type, or set, simply *is* the type, or set, of proofs of a proposition, and, reciprocally, a proposition *is* just the type, or set, of its proofs.

It turns out that **ACL**, the “logical” form of the axiom of choice, is not merely formulable in **CDTT**, *but actually derivable* in it. To see this, we need to outline the correspondence between logical operators and operations on types in **CDTT** obtained by implementing the “propositions-as-types” doctrine. This is most simply done by sketching Tait’s [1994] exposition of the idea in set-theoretic terms. To begin with, consider two propositions/types/sets $\bA$ and $\bB$. What should be required of a proof $f$ of, for example, the implication $\bA \brightarrow \bB$? Just that, given any proof $x$ of $\bA$, $f$ should yield a proof of $\bB$, that is, $f$ should be a function from $\bA$ to $\bB$. In other words, the proposition $\bA \brightarrow \bB$ is just the type of functions from $\bA$ to $\bB$:

$$ \bA \brightarrow \bB = \bB^{\bA} $$

Similarly, all that should be required of a proof $c$ of the conjunction $\bA \wedge \bB$ is that it should yield proofs $x$ and $y$ of $\bA$ and $\bB$, respectively. From this point of view $\bA \wedge \bB$ is accordingly just the type $\bA \times \bB$ of all pairs $(x, y)$, with $x$ of type $\bA$ (we write this as $x: \bA$) and $y: \bB$.

A proof of the disjunction $\bA \vee \bB$ is either a proof of $\bA$ or a proof of $\bB$ together with the information as to which of $\bA$ or $\bB$ it is a proof. That is, if we introduce the type **2** with the two distinct elements 0 and 1, a proof of $\bA \vee \bB$ may be identified as a pair $(c, n)$ in which either $c$ is a proof of $\bA$ and $n$ is 0, or $c$ is a proof of $\bB$ and $n$ is 1. This means that $\bA \vee \bB$ should be construed as the disjoint union $\bA + \bB$ of $\bA$ and $\bB$.

The true proposition $\top$ may be identified with the one element type $\bOne = \{0\}: 0$ thus counts as the unique proof of $\top$. The false proposition $\bot$ is taken to be a proposition which lacks a proof altogether: accordingly $\bot$ is identified with the empty set $\varnothing$. The negation $\neg\bA$ of a proposition $\bA$ is defined as $\bA \rightarrow \bot$, which therefore becomes identified with the set $\varnothing^A$.

A proposition $A$ is deemed to be true if it (i.e, the associated type $\bA$) has an element, that is, if there is a function $\bOne \brightarrow \bA.$ Accordingly the *law of excluded middle* for a proposition $A$ becomes the assertion that there is a function $\bOne \rightarrow A + \varnothing^A$.

In order to deal with the quantifiers we require operations defined on families of types, that is, types $\bPhi(x)$ depending on objects $x$ of some type $\bA$. By analogy with the case $\bA \brightarrow \bB$, a proof $f$ of the proposition $\forall x:\bA \bPhi(x)$, that is, an object of type $\forall x:\bA \bPhi(x)$, should associate with each $x:\bA$ a proof of $\bPhi(x)$. So $f$ is just a function with domain $A$ such that, for each $x:\bA$, $fx$ is of type $\bPhi(x)$. That is, $\forall x:\bA \bPhi(x)$ is the *product* $\Pi x:\bA \bPhi(x)$ of the $\bPhi(x)$’s. We use the *λ*-notation in writing $f$ as $\lambda xfx$.

A proof of the proposition $\exists x:\bA \bPhi(x)$, that is, an object of type $\exists x:\bA \bPhi(x)$, should determine an object $x:\bA$ and a proof $y$ of $\bPhi(x)$, and *vice-versa*. So a proof of this proposition is just a pair $(x,y)$ with $x:\bA$ and $y:\bPhi(x)$. Therefore $\exists x:\bA \bPhi(x)$ is the *disjoint union*, or *coproduct* $Cx:\bA \bPhi(x)$ of the $\bPhi(x)$’s.

To translate all this into the language of **CDTT**[^note-sup4], one uses the following concordance:

| **Logical Operation** | **Set-Theoretic Operation** | **Type-Theoretic Operation** |
| --- | --- | --- |
| $\wedge$ | $\times$ | $\times$ |
| $\vee$ | $+$ | two-term dependent sum |
| $\rightarrow$ | set exponentiation | type exponentiation |
| $\forall x$ | cartesian product $\prod_{i \in I}$ | dependent product $\prod x:\bA$ |
| $\exists x$ | coproduct or disjoint union $C_{i \in I}$ | dependent sum $Cx:\bA$ |

In **CDTT** the logical version **ACL** of *AC* takes the form of the proposition

**ACLT** $ \forall x:\bA\ \exists y:\bB\bPhi(x,y) \rightarrow \exists f:\bB^{\bA}\ \forall x:\bA\bPhi(x,fx). $

Now **ACLT** is *provable* in **CDTT**, as the following argument shows. To begin with, again following Tait, we introduce the functions *σ*, *π*, $\pi^{\prime}$ of types $\forall x:\bA(\bPhi(x) \rightarrow \exists x:\bA \bPhi(x)), \exists x:\bA\bPhi(x) \rightarrow \bA$, and $\forall y: (\exists x\bPhi(x)).\bPhi(\pi(y))$ as follows. If $b:\bA$ and $c: \bPhi(b)$, then $\sigma bc$ is $(b, c)$. If $d:\exists x:\bA \bPhi(x)$, then $d$ is of the form $(b, c)$ and in that case $\pi(d) = b$ and $\pi^{\prime}(d) = c$. These yield the equations

$$\begin{align} \pi(\sigma bc) &= b \\ \pi^{\prime}(\sigma bc) &= c \\ \sigma(\pi d)(\pi^{\prime} d) &= d. \end{align}$$

Now let $u$ be a proof of the antecedent $\forall x:\bA\exists y:\bB \bPhi(x, y))$ of **ACLT.** Then, for any $x: \bA,\pi(ux)$ is of type $\bB$ and $\pi^{\prime}(ux)$ is a proof of $\bPhi(x, \pi ux)$. So $s(u) = \lambda x \pi(ux)$ is of type $\bB^{\bA}$ and $t(u) = \lambda x\pi^{\prime}(ux)$ is a proof of $\forall x:\bA \bPhi(x,s(u)x)$. Accordingly $\lambda u\sigma s(u)t(u)$ is a proof of $\forall x:\bA\ \exists y:\bB \bPhi(x, y)) \rightarrow \exists x:\bB^{\bA}\ \forall x:\bA\bPhi(x, fx))$, so that **ACLT** is derivable in **CDTT**.

Put informally, what this shows is that in **CDTT** the consequent of **ACLT** means *nothing more than its antecedent*. Indeed, in many versions of constructive mathematics the assertability of an alternation of quantifiers $\forall x\exists yR(x,y)$ means *precisely* that one is given a function $f$ for which $R(x,fx)$ holds for all $x$.

We note that in ordinary set theory the argument establishes the *isomorphism* of the sets $\prod x:\bA Cy:\bB\bPhi(x, y))$ and $Cf:\bB^{\bA} \prod x:\bA \bPhi(x,fx))$, but *not* the validity of the usual axiom of choice. This is because in set theory **AC** is not represented by this isomorphism, but rather by the equality—the set-theoretic distributive law[^note-sup5] obtained by replacing $\prod$ by $\cap$ and $C$ by $\cup$, namely

$$ \bigcap_{x \in A} \bigcup_{y\in B} \Phi(x,y) = \bigcup_{f \in B^A} \bigcap_{x \in A} \Phi(x,fx) $$

While in **CDTT** *AC* is provable, and so *a fortiori* has no “untoward” logical consequences, in intuitionistic set theory this is far from being the case, for, as we have noted, in the latter *AC* implies the law of excluded middle. In other words, *AC* interpreted à la propositions-as-types is tautologous[^note-sup6], yet construed set-theoretically it is anything but, since so construed its affirmation yields classical logic. This prompts the question: what modification needs to be made to the propositions-as-types doctrine so as to yield the set-theoretic interpretation of *AC*? An illuminating answer has been given by Maietti (2005) through the use of so-called *monotypes* (or mono-objects), that is, (dependent) types containing at most one entity or having at most one proof. In set theory, mono-objects are *singletons*, that is, sets containing at most one element[^note-sup7].

Maietti’s modification of the propositions-as-types doctrine to bring it into line with the set-theoretic interpretation of formulas is, in essence, to take propositions (or formulas) to correspond to *mono*-objects, that is, singletons, rather than to *arbitrary* sets. Let us call this the *propositions-as-monotypes* interpretation.

Now, finally, let us reconsider *AC* under the propositions-as-monotypes interpretation within set theory**.** It will be convenient to rephrase *AC* as the assertion

$$ \tag{*} {\forall i \inn I}\ {\exists j \inn J}\ M_{ij} \leftrightarrow {\exists f \inn J^I}\ {\forall i \inn I}\ M_{if(i)} $$

where $\langle M_{ij}: i \in I, j \in J\rangle$ is any doubly indexed family of propositions (or sets). In the “propositions as types” interpretation, (\*) corresponds, as we know, to the existence of an isomorphism between $\prod_{i \in I}C_{j \in J} M_{ij}$ and $C_{f \in J^I} \prod_{i \in I} M_{if(i)}$. On the other hand, *AC* interpreted set-theoretically can be presented in the form of the distributive law

$$ \tag{**} \bigcap_{i \in I} \bigcup_{j \in J} M_{ij} = \bigcup_{f \in J^I} \bigcap_{i \in I} M_{if(i)}. $$

In the propositions-as-types interpretation, the universal quantifier $\forall i \in I$ corresponds to the product $prod_{i \in I}$ and the existential quantifier $\exists i \in I$ to the coproduct $C_{i \in I}$. Now in the propositions-as-monotypes interpretation, wherein formulas correspond to singletons, $\forall i \in I$ continues to correspond to $prod_{i \in I}$, since the product of singletons is still a singleton. But the interpretation of $\exists i \in I$ is *changed*. In fact, the interpretation of $\exists i \in I\ M_{i}$ (with each $M_i$ a singleton) now becomes $[C_{i \in I}$], where for each set $X, [X] = \{u: u = 0 \wedge \exists x. x \in X\}$ is the *canonical singleton* associated with $X$. Thinking of $X$ as a set, the singleton $[X]$ reflects the nonemptiness of $X$ in that $X$ has an element if and only if $[X]$ has 0 as its unique element. Thinking of $X$ as a proposition, the proposition $[X]$ reflects the provability of $X$ in that $X$ has a proof if and only if the proposition $[X]$ has 0 as its unique proof.

It follows that, under the propositions-as-monotypes interpretation, the proposition ${\forall i \inn I}\ {\exists j \inn J}\ M_{ij}$ is interpreted as the singleton

$$ \tag{1} \prod_{i \in I}[C_{j\in J} M_{ij}] $$

and the proposition ${\exists f \inn J^I}\ {\forall i \inn I}\ M_{if(i)}$ as the singleton

$$ \tag{2} [C_{f \in J^I} \prod_{i \in I} M_{if(i)}] $$

Under the propositions-as-monotypes interpretation *AC* would be construed as asserting the existence of an isomorphism between (1) and (2).

Now it is readily seen that to give an element of (1) amounts to no more than affirming that, for every $i\in I$, $\cup_{j\in J} M_{ij}$ is nonempty. But to give an element of (2) amounts to specifying maps $f\in J^I$ and $g$ with domain $I$ such that ${\forall i\inn I}\ g(i)\in M_{if(i)}$. It follows that to assert the existence of an isomorphism between (1) and (2), that is, to assert *AC* under the propositions-as-monotypes interpretation, is tantamount to asserting *AC* in the form (\*\*), which in turn yields **ACL** and so the Law of Excluded Middle. This is in sharp contrast with *AC* under the propositions-as-types interpretation, where, as we have seen, its assertion is automatically correct and so has no nonconstructive consequences.
