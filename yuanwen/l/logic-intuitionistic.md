# Intuitionistic Logic
**First published Wed Sep 1, 1999; substantive revision Fri Dec 16, 2022**

*Moschovakis, Joan*

Intuitionistic logic encompasses the general principles of logical reasoning which have been abstracted by logicians from intuitionistic mathematics, as developed by L. E. J. Brouwer beginning in his [1907] and [1908]. Because these principles also hold for Russian recursive mathematics and the constructive analysis of E. Bishop and his followers, intuitionistic logic may be considered the logical basis of constructive mathematics. Although intuitionistic analysis conflicts with classical analysis, intuitionistic Heyting arithmetic is a subsystem of classical Peano arithmetic. It follows that intuitionistic propositional logic is a proper subsystem of classical propositional logic, and pure intuitionistic predicate logic is a proper subsystem of pure classical predicate logic.

Philosophically, intuitionism differs from logicism by treating logic as a part of mathematics rather than as the foundation of mathematics; from finitism by allowing constructive reasoning about potentially uncountable structures (e.g., monotone bar induction on the tree of potentially infinite sequences of natural numbers); and from Platonism by viewing mathematical objects as mental constructs with no independent ideal existence. Hilbert’s formalist program, to justify classical mathematics by reducing it to a formal system whose consistency should be established by finitistic (hence constructive) means, was the most powerful contemporary rival to Brouwer’s developing intuitionism. In his 1912 essay *Intuitionism and Formalism* Brouwer correctly predicted that any attempt to prove the consistency of complete induction on the natural numbers would lead to a vicious circle.

Brouwer rejected formalism *per se* but admitted the potential usefulness of formulating general logical principles expressing intuitionistically correct constructions, such as *modus ponens*. Formal systems for intuitionistic propositional and predicate logic and arithmetic were fully developed by Heyting [1930], Gentzen [1935] and Kleene [1952]. Gödel [1933] proved the equiconsistency of intuitionistic and classical theories. Beth [1956] and Kripke [1965] provided semantics with respect to which intuitionistic logic is correct and complete, although the completeness proofs for intuitionistic predicate logic require some classical reasoning.

## 1. Rejection of *Tertium Non Datur*

Intuitionistic logic can be succinctly described as classical logic without the Aristotelian law of excluded middle:

$$ \tag{LEM} A \vee \neg A $$

or the classical law of double negation elimination:

$$ \tag{DNE} \neg \neg A \rightarrow A $$

but with the law of contradiction:

$$ (A \rightarrow B) \rightarrow ((A \rightarrow \neg B) \rightarrow \neg A) $$

and *ex falso sequitur quodlibet*:

$$ \neg A \rightarrow (A \rightarrow B). $$

Brouwer [1908] observed that LEM was abstracted from finite situations, then extended without justification to statements about infinite collections. For example, let $x, y$ range over the natural numbers $0, 1, 2, \ldots$ and let $B(y)$ abbreviate $(\primepred(y) \oldand \primepred(y+2)),$ where $\primepred(y)$ expresses “$y$ is a prime number.” Then $\forall y (B(y) \vee \neg B(y))$ holds intuitionistically as well as classically, because in order to determine whether or not a natural number is prime we need only check whether or not it has a divisor strictly between itself and 1.

But if $A(x)$ abbreviates $\exists y(y\gt x \oldand B(y)),$ then in order to assert $\forall x (A(x) \vee \neg A(x))$ intuitionistically we would need an *effective* (cf. the Church-Turing thesis) method to determine whether or not there is a pair of twin primes larger than an arbitrary natural number $x,$ and so far no such method is known. An obvious *semi-effective* method is to list the prime number pairs using a refinement of Eratosthenes’ sieve (generating the natural numbers one by one and striking out every number $y$ which fails to satisfy $B(y)$), and if there is a pair of twin primes larger than $x$ this method will eventually find the first one. However, $\forall x A(x)$ expresses the Twin Primes Conjecture, which has not yet been proved or disproved, so in the present state of our knowledge we can assert neither $\forall x (A(x) \vee \neg A(x))$ nor $\forall x A(x) \vee \neg \forall x A(x).$

One may object that these examples depend on the fact that the Twin Primes Conjecture has not yet been settled. A number of Brouwer’s original “counterexamples” depended on problems (such as Fermat’s Last Theorem) which have since been solved. But to Brouwer the general LEM was equivalent to the *a priori* assumption that *every* mathematical problem has a solution—an assumption he rejected, anticipating Gödel’s incompleteness theorem by a quarter of a century.

The rejection of LEM has far-reaching consequences. On the one hand:

- Intuitionistically, *reductio ad absurdum* only proves *negative* statements, since $\neg \neg A \rightarrow A$ does not hold in general. (If it did, LEM would follow by *modus ponens* from the intuitionistically provable $\neg \neg(A \vee \neg A).$)
- Intuitionistic propositional logic does not have a finite truth-table interpretation. There are infinitely many distinct axiomatic systems between intuitionistic and classical logic.
- Not every propositional formula has an intuitionistically equivalent disjunctive or conjunctive normal form, built from prime formulas and their negations using only $\vee$ and $\oldand.$
- Not every predicate formula has an intuitionistically equivalent prenex normal form, with all the quantifiers at the front.
- While $\forall x \neg \neg(A(x) \vee \neg A(x))$ is a theorem of intuitionistic predicate logic, $\neg \neg \forall x(A(x) \vee \neg A(x))$ is not; so $\neg \forall x(A(x) \vee \neg A(x))$ is consistent with intuitionistic predicate logic.

On the other hand:

- Every intuitionistic proof of a closed statement of the form $A \vee B$ can be effectively transformed into an intuitionistic proof of $A$ or an intuitionistic proof of $B,$ and similarly for closed existential statements.
- Intuitionistic propositional logic is effectively decidable, in the sense that a finite constructive process applies uniformly to every propositional formula, either producing an intuitionistic proof of the formula or demonstrating that no such proof can exist.
- The negative fragment of intuitionistic logic (without $\vee$ or $\exists$) contains a faithful translation of classical logic, and similarly for intuitionistic and classical arithmetic.
- Intuitionistic arithmetic can consistently be extended by axioms which contradict classical arithmetic, enabling the formal study of recursive mathematics.
- Brouwer’s controversial intuitionistic analysis, which conflicts with LEM, can be formalized and shown consistent relative to a classically *and* intuitionistically correct subtheory.

## 2. Intuitionistic First-Order Predicate Logic

Formalized intuitionistic logic is naturally motivated by the informal Brouwer-Heyting-Kolmogorov explanation of intuitionistic truth, outlined in the entries on intuitionism in the philosophy of mathematics and the development of intuitionistic logic. The constructive independence of the logical operations $\oldand, \vee , \rightarrow , \neg , \forall , \exists$ contrasts with the classical situation, where e.g., $A \vee B$ is equivalent to $\neg(\neg A \oldand \neg B),$ and $\exists xA(x)$ is equivalent to $\neg \forall x \neg A(x).$ From the B-H-K viewpoint, a sentence of the form $A \vee B$ asserts that either a proof of $A,$ or a proof of $B,$ has been constructed; while $\neg(\neg A \oldand \neg B)$ asserts that an algorithm has been constructed which would effectively convert any pair of constructions proving $\neg A$ and $\neg B$ respectively, into a proof of a known contradiction.

### 2.1 The formal systems $\mathbf{H–IPC}$ and $\mathbf{H–IQC}$

Following is a Hilbert-style formalism $\mathbf{H–IQC}$ from Kleene [1952] (cf. Troelstra and van Dalen [1988]) for intuitionistic first-order predicate logic. The language $L$ of $\mathbf{H–IQC}$ has predicate letters $P, Q(.), \ldots$ of all arities and individual variables $x, y, z, \ldots$ (with or without subscripts $1, 2, \ldots$), as well as symbols $\oldand, \vee , \rightarrow , \neg , \forall , \exists$ for the logical connectives and quantifiers, and parentheses (, ). The *atomic* (or *prime*) *formulas* of $L$ are expressions such as $P, Q(x), R(x, y, x)$ where $P, Q({.}), R({.}{.}{.})$ are $0$-ary, $1$-ary and $3$-ary predicate letters respectively; that is, the result of filling each blank in a predicate letter by an individual variable symbol is a prime formula. The *(well-formed) formulas* of $L$ are defined inductively as follows:

- Each atomic formula is a *formula*.
- If $A$ and $B$ are *formulas*, so are $(A \oldand B), (A \vee B), (A \rightarrow B)$ and $\neg A.$
- If $A$ is a *formula* and $x$ is a variable, then $\forall xA$ and $\exists xA$ are *formulas*.

In general, we use $A, B, C$ as metavariables for well-formed formulas and $x, y, z$ as metavariables for individual variables. Anticipating applications (for example to intuitionistic arithmetic) we use $s, t$ as metavariables for *terms*; in the case of pure predicate logic, terms are simply individual variables. An occurrence of a variable $x$ in a formula $A$ is *bound* if it is within the scope of a quantifier $\forall x$ or $\exists x,$ otherwise *free*. Intuitionistically as classically, $(A \leftrightarrow B)$ abbreviates $((A \rightarrow B) \oldand (B \rightarrow A)),$ and parentheses will be omitted when this causes no confusion.

There are three rules of inference:

*Modus Ponens* From $A$ and $A \rightarrow B,$ conclude $B.$

*$\forall$-Introduction* From $C \rightarrow A(x),$ where $x$ is a variable which does not occur free in $C,$ conclude $C \rightarrow \forall x A(x).$

*$\exists$-Elimination* From $A(x) \rightarrow C,$ where $x$ is a variable which does not occur free in $C,$ conclude $\exists x A(x) \rightarrow C.$

The axioms are all formulas of the following forms, where in the last two schemas the subformula $A(t)$ is the result of substituting an occurrence of the term $t$ for every free occurrence of $x$ in $A(x),$ and no variable free in $t$ becomes bound in $A(t)$ as a result of the substitution.

$$\begin{array}{l} A \rightarrow(B \rightarrow A) \\ (A \rightarrow B) \rightarrow ((A \rightarrow (B \rightarrow C)) \rightarrow(A \rightarrow C)) \\ A \rightarrow(B \rightarrow (A \oldand B)) \\ (A \oldand B) \rightarrow A \\ (A \oldand B) \rightarrow B \\ A \rightarrow (A \vee B) \\ B \rightarrow (A \vee B) \\ (A \rightarrow C) \rightarrow ((B \rightarrow C) \rightarrow((A \vee B) \rightarrow C)) \\ (A \rightarrow B) \rightarrow ((A \rightarrow \neg B) \rightarrow \neg A) \\ \neg A \rightarrow(A \rightarrow B) \\ \forall xA(x) \rightarrow A(t) \\ A(t) \rightarrow \exists xA(x) \end{array}$$

A *proof* is any finite sequence of formulas, each of which is an axiom or an immediate consequence, by a rule of inference, of (one or two) preceding formulas of the sequence. Any proof is said to *prove* its last formula, which is called a *theorem* or *provable formula* of first-order intuitionistic predicate logic. A *derivation of* a formula $E$ *from* a collection $F$ of *assumptions* is any sequence of formulas, each of which belongs to $F$ or is an axiom or an immediate consequence, by a rule of inference, of preceding formulas of the sequence, such that $E$ is the last formula of the sequence. If such a derivation exists, we say $E$ is *derivable from* $F.$

Intuitionistic propositional logic $\mathbf{H–IPC}$ is the subsystem of $\mathbf{H–IQC}$ which results when the language is restricted to formulas built from proposition letters $P, Q, R,\ldots$ using the propositional connectives $\oldand, \vee , \rightarrow$ and $\neg,$ and only the propositional postulates are used. Thus the last two rules of inference and the last two axiom schemas are absent from the propositional subsystem.

If, in the given list of axiom schemas for intuitionistic propositional or first-order predicate logic, the law expressing *ex falso sequitur quodlibet*:

$$\neg A \rightarrow (A \rightarrow B)$$

is replaced by the classical law of double negation elimination DNE:

$$\neg \neg A \rightarrow A$$

(or, equivalently, if the intuitionistic law of negation introduction:

$$ (A \rightarrow B) \rightarrow ((A \rightarrow \neg B) \rightarrow \neg A) $$

is replaced by LEM), a formal system $\mathbf{H–CPC}$ for classical propositional logic or $\mathbf{H–CQC}$ for classical predicate logic results. Since *ex falso* and the law of contradiction are classical theorems, intuitionistic logic is contained in classical logic. In a sense, classical logic is also contained in intuitionistic logic; see Section 4.1 below.

It is important to note that while LEM and DNE are equivalent as *schemas* over $\mathbf{H–IPC},$ the *implication*

$$ (\neg \neg A \rightarrow A) \rightarrow (A \vee \neg A) $$

is not a theorem schema of $\mathbf{H–IPC}.$ For theories $\mathbf{T}$ based on intuitionistic logic, if $E$ is an arbitrary formula of $L(\mathbf{T})$ then by definition:

$E$ is *decidable in* $\mathbf{T}$ if and only if $\mathbf{T}$ proves $E \vee \neg E.$

$E$ is *stable in* $\mathbf{T}$ if and only if $\mathbf{T}$ proves $\neg \neg E \rightarrow E.$

$E$ is *testable in* $\mathbf{T}$ if and only if $\mathbf{T}$ proves $\neg E \vee \neg \neg E.$

Decidability implies stability, but not conversely. The conjunction of stability and testability is equivalent to decidability. Brouwer himself proved that “absurdity of absurdity of absurdity is equivalent to absurdity” (Brouwer [1923C]), so every formula of the form $\neg A$ is stable; but in $\mathbf{H–IPC}$ and $\mathbf{H–IQC}$ prime formulas and their negations are undecidable, as shown in Section 5.1 below.

### 2.2 Alternative formalisms, and the deduction theorem

The Hilbert-style system $\mathbf{H–IQC}$ is useful for metamathematical investigations of intuitionistic logic, but its forced linearization of deductions and its preference for axioms over rules make it an awkward instrument for establishing derivability. A natural deduction system $\mathbf{N–IQC}$ for intuitionistic predicate logic results from the deductive system $\mathbf{D},$ presented in Section 3 of the entry on classical logic in this Encyclopedia, by omitting the symbol and rules for identity, and replacing the classical rule (DNE) of double negation elimination by the intuitionistic negation elimination rule expressing *ex falso*:

**(INE)**

If $F$ entails $A$ and $F$ entails $\neg A,$ then $F$ entails $B.$

The keys to proving that $\mathbf{H–IQC}$ is equivalent to $\mathbf{N–IQC}$ are *modus ponens* and its converse, the:

**Deduction Theorem** If $B$ is derivable from $A$ and possibly other formulas $F,$ with all variables free in $A$ held constant in the derivation (that is, without using the second or third rule of inference on any variable $x$ occurring free in $A,$ unless the assumption $A$ does not occur in the derivation before the inference in question), then $A \rightarrow B$ is derivable from $F.$

This fundamental result, roughly expressing the rule $(\rightarrow I)$ of $\mathbf{I},$ can be proved for $\mathbf{H–IQC}$ by induction on the definition of a derivation. The other rules of $\mathbf{I}$ hold for $\mathbf{H–IQC}$ essentially by *modus ponens*, which corresponds to $(\rightarrow E)$ in $\mathbf{N–IQC};$ and all the axioms of $\mathbf{H–IQC}$ are provable in $\mathbf{N–IQC}.$

To illustrate the usefulness of the Deduction Theorem, consider the (apparently trivial) theorem schema $(A \rightarrow A).$ A correct proof in $\mathbf{H–IPC}$ takes five lines:

1. $A \rightarrow (A \rightarrow A)$
2. $(A \rightarrow (A \rightarrow A)) \rightarrow ((A \rightarrow ((A \rightarrow A) \rightarrow A)) \rightarrow (A \rightarrow A))$
3. $(A \rightarrow ((A \rightarrow A) \rightarrow A)) \rightarrow(A \rightarrow A)$
4. $A \rightarrow((A \rightarrow A) \rightarrow A)$
5. $A \rightarrow A$

where 1, 2 and 4 are axioms and 3, 5 come from earlier lines by *modus ponens*. However, $A$ is derivable from $A$ (as assumption) in one obvious step, so the Deduction Theorem allows us to conclude that a proof of $A \rightarrow A$ exists. (In fact, the formal proof of $A \rightarrow A$ just presented is part of the constructive proof of the Deduction Theorem!)

It is important to note that, in the definition of a derivation from assumptions in $\mathbf{H–IQC},$ the assumption formulas are treated as if all their free variables were universally quantified, so that $\forall x A(x)$ is derivable from the hypothesis $A(x).$ However, the variable $x$ will be *varied* (not held constant) in that derivation, by use of the rule of $\forall$-introduction; and so the Deduction Theorem cannot be used to conclude (falsely) that $A(x) \rightarrow \forall x A(x)$ (and hence, by $\exists$-elimination, $\exists x A(x) \rightarrow \forall x A(x))$ are provable in $\mathbf{H–IQC}.$ As an example of a correct use of the Deduction Theorem for predicate logic, consider the implication $\exists x A(x) \rightarrow \neg \forall x\neg A(x).$ To show this is provable in $\mathbf{H–IQC},$ we first derive $\neg \forall x\neg A(x)$ from $A(x)$ with all free variables held constant:

1. $\forall x\neg A(x) \rightarrow \neg A(x)$
2. $A(x) \rightarrow (\forall x\neg A(x) \rightarrow A(x))$
3. $A(x)$ (assumption)
4. $\forall x\neg A(x) \rightarrow A(x)$
5. $(\forall x\neg A(x) \rightarrow A(x)) \rightarrow ((\forall x\neg A(x) \rightarrow \neg A(x)) \rightarrow \neg \forall x\neg A(x))$
6. $(\forall x\neg A(x) \rightarrow \neg A(x)) \rightarrow \neg \forall x\neg A(x)$
7. $\neg \forall x\neg A(x)$

Here 1, 2 and 5 are axioms; 4 comes from 2 and 3 by *modus ponens*; and 6 and 7 come from earlier lines by *modus ponens*; so no variables have been varied. The Deduction Theorem tells us there is a proof $P$ in $\mathbf{H–IQC}$ of $A(x) \rightarrow \neg \forall$x$\neg A(x),$ and one application of $\exists$-*elimination* converts $P$ into a proof of $\exists x A(x) \rightarrow \neg \forall x\neg A(x).$ The converse is not provable in $\mathbf{H–IQC},$ as shown in Section 5.1 below.

Other important alternatives to $\mathbf{H–IQC}$ and $\mathbf{N–IQC}$ are the various sequent calculi for intuitionistic propositional and predicate logic. The first such calculus was defined by Gentzen [1934–5], cf. Kleene [1952]. Sequent systems, which prove exactly the same formulas as $\mathbf{H–IQC}$ and $\mathbf{N–IQC},$ keep track explicitly of all assumptions and conclusions at each step of a proof, replacing *modus ponens* (which eliminates an intermediate formula) by a *cut rule* (which can be shown to be an admissible rule (cf. Section 4.2) for the subsystem remaining when it is omitted).

When the details of the formalism are not important, from now on we follow Troelstra and van Dalen [1988] in letting “$\mathbf{IQC}$” or “$\mathbf{IPC}$” refer to any formal system for intuitionistic predicate or propositional logic respectively, and similarly “$\mathbf{CQC}$” and “$\mathbf{CPC}$” for classical predicate and propositional logic.

Both $\mathbf{IPC}$ and $\mathbf{IQC}$ satisfy *interpolation theorems*, e.g.: If $A$ and $B$ are propositional formulas having at least one proposition letter in common, and if $A \rightarrow B$ is provable in $\mathbf{IPC},$ then there is a formula $C,$ containing only proposition letters which occur in both $A$ and $B,$ such that both $A \rightarrow C$ and $C \rightarrow B$ are provable. These topics are treated in Kleene [1952] and Troelstra and Schwichtenberg [2000].

While identity can of course be added to intuitionistic logic, for applications (e.g., to arithmetic) the equality symbol is generally treated as a distinguished predicate constant satisfying the axioms for an equivalence relation (reflexivity, symmetry and transitivity) and additional nonlogical axioms (e.g., the primitive recursive definitions of addition and multiplication). Identity is decidable, intuitionistically as well as classically, but intuitionistic extensional equality is not always decidable; see the discussion of Brouwer’s continuity axioms in Section 3 of the entry on intuitionism in the philosophy of mathematics.

## 3. Intuitionistic Number Theory (Heyting Arithmetic) $\mathbf{HA}$

Intuitionistic (Heyting) arithmetic $\mathbf{HA}$ and classical (Peano) arithmetic $\mathbf{PA}$ share the same first-order language and the same non-logical axioms; only the logic is different. In addition to the logical connectives, quantifiers and parentheses and the individual variables $x, y, z,\ldots$ (also used as metavariables), the language $L(\mathbf{HA})$ of arithmetic has a binary predicate symbol $=,$ individual constant $0,$ unary function constant $S,$ and finitely or countably infinitely many additional constants for primitive recursive functions including addition and multiplication; the precise choice is a matter of taste and convenience. *Terms* are built from variables and $0$ using the function constants; in particular, each natural number $n$ is expressed in the language by the *numeral* $\mathbf{n}$ obtained by applying $S$ $n$ times to $0$ (e.g., $S(S(0))$ is the numeral for $2$). *Prime formulas* are of the form $(s = t)$ where $s, t$ are terms, and *compound formulas* are obtained from these as usual.

The logical axioms and rules of $\mathbf{HA}$ are those of first-order intuitionistic predicate logic $\mathbf{IQC}.$ The nonlogical axioms include the reflexive, symmetric and transitive properties of $=$: $$ \forall x (x = x),$$ $$ \forall x \forall y (x = y \rightarrow y = x),$$ $$ \forall x \forall y \forall z ((x = y \oldand y = z) \rightarrow x = z);$$ the axiom characterizing $0$ as the least natural number:

$$ \forall x\neg(S(x) = 0),$$

the axiom characterizing $S$ as a one-to-one function:

$$ \forall x\forall y(S(x) = S(y) \rightarrow x = y),$$

the extensional equality axiom for $S$:

$$\forall x\forall y (x = y \rightarrow S(x) = S(y));$$

the primitive recursive defining equations for each function constant, in particular for addition: $$ \forall x (x + 0 = x),$$ $$ \forall x \forall y (x + S(y) = S(x + y));$$ and multiplication: $$ \forall x (x \cdot 0 = 0),$$ $$ \forall x \forall y (x \cdot S(y) = (x \cdot y) + x);$$ and the (universal closure of the) schema of mathematical induction, for arbitrary formulas $A(x)$:

$$ ( A(0) \oldand \forall x (A(x) \rightarrow A(S(x))) ) \rightarrow \forall x A(x).$$

Extensional equality axioms for all function constants are derivable by mathematical induction from the equality axiom for $S$ and the primitive recursive function axioms.

The natural order relation $x \lt y$ can be defined in $\mathbf{HA}$ by $\exists z(S(z) + x = y),$ or by the quantifier-free formula $S(x) \dotminus y = 0$ if the symbol and primitive recursive defining equations for predecessor : $$ Pd(0) = 0,$$ $$ \forall x (Pd(S(x)) = x)$$ and cutoff subtraction : $$ \forall x (x \dotminus 0 = x),$$ $$ \forall x \forall y (x \dotminus S(y) = Pd(x \dotminus y))$$ are present in the formalism. $\mathbf{HA}$ proves the comparative law

$$\forall x \forall y (x \lt y \vee x = y \vee y \lt x)$$

and an intuitionistic form of the least number principle, for arbitrary formulas $A(x)$:

$$\begin{aligned} \forall x[&\forall y (y \lt x \rightarrow (A(y) \vee \neg A(y))) \rightarrow \\ &(\exists y ((y \lt x \oldand A(y)) \oldand \forall z(z \lt y \rightarrow \neg A(z)))\ \vee \\ &\forall y(y \lt x \rightarrow \neg A(y)))]. \end{aligned}$$

The hypothesis is needed because not all arithmetical formulas are decidable in $\mathbf{HA}.$ However, $\forall x\forall y(x = y \vee \neg(x = y))$ can be proved directly by mathematical induction, and so:

- Prime formulas (and hence all *quantifier-free* formulas) are decidable and stable in $\mathbf{HA}.$

If $A(x)$ is decidable in $\mathbf{HA},$ then by induction on $x$ so are $\forall y (y \lt x \rightarrow A(y))$ and $\exists y (y \lt x \oldand A(y)).$ Hence:

- Formulas in which all quantifiers are *bounded* are decidable and stable in $\mathbf{HA}.$

The collection $\Delta_0$ of arithmetical formulas in which all quantifiers are bounded is the lowest level of a classical arithmetical hierarchy based on the pattern of alternations of quantifiers in a prenex formula. In $\mathbf{HA}$ not every formula has a prenex form, but Burr [2004] discovered a simple intuitionistic arithmetical hierarchy corresponding level by level to the classical. For the purposes of the next two definitions only, $\forall x$ denotes a block of finitely many universal number quantifiers, and similarly $\exists x$ denotes a block of finitely many existential number quantifiers. With these conventions, Burr’s classes $\Phi_n$ and $\Psi_n$ are defined by:

- $\Phi_0 = \Psi_0 = \Delta_0,$
- $\Phi_1$ is the class of all formulas of the form $\forall x A(x)$ where $A(x)$ is in $\Psi_0.$ For $n \ge 2,$ $\Phi_n$ is the class of all formulas of the form $\forall x [A(x) \rightarrow \exists y B(x,y)]$ where $A(x)$ is in $\Phi_{n-1}$ and $B(x,y)$ is in $\Phi_{n-2},$
- $\Psi_1$ is the class of all formulas of the form $\exists x A(x)$ where $A(x)$ is in $\Phi_0.$ For $n \ge 2,$ $\Psi_n$ is the class of all formulas of the form $A \rightarrow B$ where $A$ is in $\Phi_n$ and $B$ is in $\Phi_{n-1}.$

The corresponding classical prenex classes are defined more simply:

- $\Pi_0 = \Sigma_0 = \Delta_0,$
- $\Pi_{n +1}$ is the class of all formulas of the form $\forall x A(x)$ where $A(x)$ is in $\Sigma_n,$
- $\Sigma_{n +1}$ is the class of all formulas of the form $\exists x A(x)$ where $A(x)$ is in $\Pi_n.$

Peano arithmetic $\mathbf{PA}$ comes from Heyting arithmetic $\mathbf{HA}$ by adding LEM or $\neg \neg A \rightarrow A$ to the list of logical axioms, i.e., by using classical instead of intuitionistic logic. The following results hold even in the fragments of $\mathbf{HA}$ and $\mathbf{PA}$ with the induction schema restricted to $\Delta_0$ formulas.

> **Burr’s Theorem:**
>
> - Every arithmetical formula is provably equivalent in $\mathbf{HA}$ to a formula in one of the classes $\Phi_n.$
> - Every formula in $\Phi_n$ is provably equivalent in $\mathbf{PA}$ to a formula in $\Pi_n,$ and conversely.
> - Every formula in $\Psi_n$ is provably equivalent in $\mathbf{PA}$ to a formula in $\Sigma_n,$ and conversely.

$\mathbf{HA}$ and $\mathbf{PA}$ are proof-theoretically equivalent, as will be shown in Section 4. Each is capable of (numeralwise) expressing its own proof predicate. By Gödel’s famous Incompleteness Theorem, if $\mathbf{HA}$ is consistent then neither $\mathbf{HA}$ nor $\mathbf{PA}$ can prove its own consistency.

## 4. Basic Proof Theory

### 4.1 Translating classical into intuitionistic logic

A fundamental fact about intuitionistic logic is that it has the same consistency strength as classical logic. For propositional logic this was first proved by Glivenko [1929]:

**Glivenko’s Theorem** An arbitrary propositional formula $A$ is classically provable, if and only if $\neg \neg A$ is intuitionistically provable.

Glivenko’s Theorem does not extend to predicate logic, although an arbitrary predicate formula $A$ is classically provable if and only if $\neg \neg A$ is provable in intuitionistic predicate logic plus the “double negation shift” schema.

$$ \tag{DNS} \forall x\neg \neg B(x) \rightarrow \neg \neg \forall x B(x) $$

The more sophisticated **negative translation** of classical into intuitionistic theories, due independently to Gödel and Gentzen, associates with each formula $A$ of the language $L$ another formula $g(A)$ (with no $\vee$ or $\exists),$ such that:

1. Classical predicate logic proves $A \leftrightarrow g(A).$
2. Intuitionistic predicate logic proves $g(A) \leftrightarrow \neg \neg g(A).$
3. If classical predicate logic proves $A,$ then intuitionistic predicate logic proves $g(A).$

The proofs are straightforward from the following inductive definition of $g(A)$ (using Gentzen’s direct translation of implication, rather than Gödel’s in terms of $\neg$ and $\oldand$):

$$\begin{align*} g(P) &\text{ is } \neg \neg P, \text{ if } P \text{ is prime}.\\ g(A \oldand B) &\text{ is } g(A) \oldand g(B). \\ g(A \vee B) &\text{ is } \neg(\neg g(A) \oldand \neg g(B)). \\ g(A \rightarrow B) &\text{ is } g(A) \rightarrow g(B). \\ g(\neg A) &\text{ is } \neg g(A). \\ g(\forall xA(x)) &\text{ is }\forall x g(A(x)). \\ g(\exists xA(x)) &\text{ is } \neg \forall x\neg g(A(x)). \end{align*}$$

For each formula $A,$ $g(A)$ is provable intuitionistically if and only if $A$ is provable classically. In particular, if $B \oldand \neg B$ were classically provable for some formula $B,$ then $g(B) \oldand \neg g(B)$ (which is $g(B \oldand \neg B))$ would in turn be provable intuitionistically. Hence:

1. Classical and intuitionistic predicate logic are equiconsistent.

The negative translation of classical into intuitionistic number theory is even simpler, since prime formulas of intuitionistic arithmetic are stable. Thus $g(s=t)$ can be taken to be $s=t,$ and the other clauses are unchanged. The negative translation of each instance of the schema of mathematical induction is an instance of the same schema, and the other nonlogical axioms of arithmetic are their own negative translations, so:

- (I), (II), (III) and (IV) hold also for number theory.

Gödel [1933e] interpreted these results as showing that intuitionistic logic and arithmetic are *richer* than classical logic and arithmetic, because the intuitionistic theory distinguishes formulas which are classically equivalent, and has the same consistency strength as the classical theory. In particular, Gödel’s incompleteness theorems apply to $\mathbf{HA}$ as well as to $\mathbf{PA}.$

Direct attempts to extend the negative interpretation to analysis fail because the negative translation of the countable axiom of choice is not a theorem of intuitionistic analysis. However, it is consistent with intuitionistic analysis, including Brouwer’s controversial continuity principle, by the functional version of Kleene’s recursive realizability (cf. Section 6.3 below). It follows that intuitionistic mathematics, which can only be expressed by using all the standard logical connectives and quantifiers, is consistent with a faithful translation of classical mathematics avoiding $\vee$ and $\exists.$

This is important because Brouwer’s intuitionistic analysis is inconsistent with LEM. However, if $A$ is any *negative* formula (without $\vee$ or $\exists$) then $\neg \neg A \rightarrow A$ is provable using intuitionistic logic. A reconciliation of intuitionistic and classical analysis along these lines, inspired by Troelstra [1977] and Kripke[2019], is suggested in Moschovakis [2017].

### 4.2 Admissible rules of intuitionistic logic and arithmetic

Gödel [1932] observed that intuitionistic propositional logic has the **disjunction property**:

**(DP)**

If $A \vee B$ is a theorem, then $A$ is a theorem or $B$ is a theorem.

Gentzen [1935] established the disjunction property for closed formulas of intuitionistic predicate logic. From this it follows that if intuitionistic logic is consistent, then $P \vee \neg P$ is not a theorem if $P$ is an atomic formula. Kleene [1945, 1952] proved that intuitionistic first-order number theory also has the related (cf. Friedman [1975]) **existence property**:

**(EP)**

If $\exists x A(x)$ is a closed theorem, then for some closed term $t,$ $A(t)$ is a theorem.

The disjunction and existence properties are special cases of a general phenomenon peculiar to nonclassical theories. The *admissible rules* of a theory are the rules under which the theory is closed. For example, Harrop [1960] observed that the rule:

- If $\neg A \rightarrow (B \vee C)$ is a theorem, so is $(\neg A \rightarrow B) \vee(\neg A \rightarrow C)$

is admissible for intuitionistic propositional logic $\mathbf{IPC}$ because if $A,$ $B$ and $C$ are any formulas such that $\neg A \rightarrow(B \vee C)$ is provable in $\mathbf{IPC},$ then $(\neg A \rightarrow B) \vee (\neg A \rightarrow C)$ is provable in $\mathbf{IPC}.$ Harrop’s rule is not *derivable* in $\mathbf{IPC}$ because the formula

$$(\neg A \rightarrow(B \vee C)) \rightarrow ((\neg A \rightarrow B) \vee (\neg A \rightarrow C))$$

is not intuitionistically provable. Another important example of an admissible nonderivable rule of $\mathbf{IPC}$ is Mints’s rule:

- If $(A \rightarrow B) \rightarrow (A \vee C)$ is a theorem, so is $((A \rightarrow B) \rightarrow A) \vee ((A \rightarrow B) \rightarrow C).$

The two-valued truth table interpretation of classical propositional logic $\mathbf{CPC}$ gives rise to a simple proof that every admissible rule of $\mathbf{CPC}$ is derivable: otherwise, some assignment to $A,$ $B,$ etc. would make the hypothesis true and the conclusion false, and by substituting e.g. $P \rightarrow P$ for the letters assigned “true” and $P \oldand \neg P$ for those assigned “false” one would have a provable hypothesis and unprovable conclusion. The fact that the intuitionistic situation is more interesting leads to many natural questions, some of which have recently been answered.

By generalizing Mints’s Rule, Visser and de Jongh identified a recursively enumerable sequence of successively stronger admissible rules (“Visser’s rules”) which, they conjectured, formed a *basis* for the admissible rules of $\mathbf{IPC}$ in the sense that every admissible rule is derivable from the disjunction property and one of the rules of the sequence. Building on work of Ghilardi [1999], Iemhoff [2001] succeeded in proving their conjecture. Rybakov [1997] proved that the collection of all admissible rules of $\mathbf{IPC}$ is decidable but has no finite basis. Visser [2002] showed that his rules are also the admissible propositional rules of $\mathbf{HA},$ and of $\mathbf{HA}$ extended by Markov’s Principle MP (defined in Section 5.2 below). More recently, Jerabek [2008] found an independent basis for the admissible rules of $\mathbf{IPC},$ with the property that no rule in the basis derives another.

Much less is known about the admissible rules of intuitionistic predicate logic. Pure $\mathbf{IQC},$ without individual or predicate constants, has the following remarkable admissible rule for $A(x)$ with no variables free but $x$:

- If $\exists x A(x)$ is a theorem, so is $\forall x A(x).$

Not every admissible predicate rule of $\mathbf{IQC}$ is admissible for all formal systems based on $\mathbf{IQC};$ for example, $\mathbf{HA}$ evidently violates the rule just stated. Visser proved in [1999] that the property of being an admissible predicate rule of $\mathbf{HA}$ is $\Pi_2$ complete, and in [2002] that $\mathbf{HA}$ $+$ MP has the same predicate admissible rules as $\mathbf{HA}.$ Plisko [1992] proved that the *predicate logic* of $\mathbf{HA}$ $+$ MP (the set of sentences in the language of $\mathbf{IQC}$ all of whose uniform substitution instances in the language of arithmetic are provable in $\mathbf{HA}$ $+$ MP) is $\Pi_2$ complete; Visser [2006] extended this result to some constructively interesting consistent extensions of $\mathbf{HA}$ which are not contained in $\mathbf{PA}.$

While they have not been completely classified, the admissible rules of intuitionistic predicate logic are known to include **Markov’s Rule** for decidable predicates:

- If $\forall x(A(x) \vee \neg A(x)) \oldand \neg \forall x\neg A(x)$ is a theorem, so is $\exists x A(x).$

And the following **Independence-of-Premise Rule** (where $y$ is assumed not to occur free in $A(x))$:

- If $\forall x(A(x) \vee \neg A(x)) \oldand (\forall x A(x) \rightarrow \exists y B(y))$ is a theorem, so is $\exists y (\forall x A(x) \rightarrow B(y)).$

Both rules are also admissible for $\mathbf{HA}.$ The corresponding implications (MP and IP respectively), which are not provable intuitionistically, are verified by Gödel’s “Dialectica” interpretation of $\mathbf{HA}$ (cf. Section 6.3 below). So is the implication (CT) corresponding to one of the most interesting admissible rules of Heyting arithmetic, let us call it the **Church-Kleene Rule**:

- If $\forall x \exists y A(x, y)$ is a closed theorem of $\mathbf{HA}$ then there is a number $n$ such that, provably in $\mathbf{HA},$ the partial recursive function with Gödel number $n$ is total and maps each $x$ to a $y$ satisfying $A(x, y)$ (and moreover $A(\mathbf{x},\mathbf{y})$ is provable, where $\mathbf{x}$ is the numeral for the natural number $x$ and $\mathbf{y}$ is the numeral for $y).$

Combining Markov’s Rule with the negative translation gives the result that classical and intuitionistic arithmetic prove the same formulas of the form $\forall x \exists y A(x, y)$ where $A(x, y)$ is quantifier-free. In general, if $A(x, y)$ is provably decidable in $\mathbf{HA}$ and if $\forall x \exists y A(x, y)$ is a closed theorem of *classical* arithmetic $\mathbf{PA},$ the conclusion of the Church-Kleene Rule holds even in *intuitionistic* arithmetic. For if $\mathbf{HA}$ proves $\forall x \forall y (A(x,y) \vee \neg A(x,y))$ then by the Church-Kleene Rule the characteristic function of $A(x,y)$ has a Gödel number $m,$ provably in $\mathbf{HA};$ so $\mathbf{HA}$ proves $\forall x \exists y A(x,y) \leftrightarrow \forall x \exists y \exists z B(\mathbf{m},x,y,z)$ where $B$ is quantifier-free, and the adjacent existential quantifiers can be contracted in $\mathbf{HA}.$ It follows that $\mathbf{HA}$ and $\mathbf{PA}$ have the same provably recursive functions.

Here is a proof that the rule “If $\forall x (A \vee B(x))$ is a theorem, so is $A \vee \forall x B(x)$” (where $x$ is not free in $A)$ is *not* admissible for $\mathbf{HA},$ if $\mathbf{HA}$ is consistent. Gödel numbering provides a quantifier-free formula $G(x)$ which (numeralwise) expresses the predicate “$x$ is the code of a proof in $\mathbf{HA}$ of $(0 = 1).$” By intuitionistic logic with the decidability of quantifier-free arithmetical formulas, $\mathbf{HA}$ proves $\forall x(\exists y G(y) \vee \neg G(x)).$ However, if $\mathbf{HA}$ proved $\exists yG(y) \vee \forall x\neg G(x)$ then by the disjunction property, $\mathbf{HA}$ must prove either $\exists yG(y)$ or $\forall x\neg G(x).$ The first case is impossible, by the existence property with the consistency assumption and the fact that $\mathbf{HA}$ proves all true quantifier-free sentences. But the second case is also impossible, by Gödel’s second incompleteness theorem, since $\forall x\neg G(x)$ expresses the consistency of $\mathbf{HA}.$

## 5. Basic Semantics

The most direct way to show that a formula (or schema) $F$ is *provable in* a formal system $\mathbf{S}$ is to construct a proof of $F$ in $\mathbf{S}.$ But if a formula (or some substitution instance of a schema) happens *not* to be provable in $\mathbf{S},$ how can that fact be known? Our failure to find a proof may suggest unprovability, but is not in general decisive unless the proof search is a canonical one in Gentzen’s system for intuitionistic propositional logic. Usually what is needed is an *interpretation* with respect to which $\mathbf{S}$ is *sound*, in the sense that every provable formula is *valid* under the interpretation. Then to show $F$ *unprovable* in $\mathbf{S}$ it suffices to show that $F$ is *invalid* under the interpretation, typically by constructing a *countermodel* to $F.$

If a system $\mathbf{S}$ is *complete* for an interpretation, in the sense that every formula which is valid under the interpretation is provable in $\mathbf{S},$ then an indirect way to show that a formula (or schema) is provable in $\mathbf{S}$ is to establish its validity under the interpretation. Completeness does not always accompany soundness; for instance, Heyting arithmetic is sound but incomplete for the realizability interpretation described in Section 5.2 below.

Intuitionistic systems have inspired a variety of interpretations, including Beth’s tableaux, Rasiowa and Sikorski’s topological models, Heyting algebras, formulas-as-types, Kleene’s recursive realizabilities, the Kleene and Aczel slashes, and models based on sheafs and topoi. Of all these interpretations Kripke’s [1965] possible-world semantics, with respect to which intuitionistic predicate logic is sound and complete, most resembles classical model theory. Recursive realizability interpretations, on the other hand, attempt to effectively implement the B-H-K explanation of intuitionistic truth.

### 5.1 Kripke and Beth semantics for intuitionistic logic

A *Kripke structure* $\mathbf{K}$ for $L$ consists of a partially ordered set $K$ of *nodes* and a *domain function D* assigning to each node $k$ in $K$ an inhabited set $D(k),$ such that if $k \le k',$ then $D(k) \subseteq D(k').$ In addition $\mathbf{K}$ has a *forcing* relation determined as follows.

For each node $k$ let $L(k)$ be the language extending $L$ by new constants for all the elements of $D(k).$ To each node $k$ and each $0$-ary predicate letter (each proposition letter) $P,$ either assign $f(P, k) =$ *true* or leave $f(P, k)$ undefined, consistent with the requirement that if $k \le k'$ and $f(P, k) =$ *true* then $f(P, k') =$ *true* also. Say that:

$k$ $\Vdash$ $P$ if and only if $f(P, k) =$ *true*.

To each node $k$ and each $(n+1)$-ary predicate letter $Q(\ldots),$ assign a (possibly empty) set $T(Q, k)$ of $(n+1)$-tuples of elements of $D(k)$ in such a way that if $k \le k'$ then $T(Q, k) \subseteq T(Q, k').$ Say that:

$k$ $\Vdash$ $Q(d_0 ,\ldots, d_n)$ if and only if $(d_0 ,\ldots ,d_n) \in T(Q, k).$

Now define $k$ $\Vdash$ $E$ (which may be read “ $k$ *forces* $E$ ”) for compound sentences $E$ of $L(k)$ inductively as follows:

| $k$ $\Vdash$ $(A \oldand B)$ | if $k$ $\Vdash$ $A$ and $k$ $\Vdash$ $B.$ |
| --- | --- |
| $k$ $\Vdash$ $(A \vee B)$ | if $k$ $\Vdash$ $A$ or $k$ $\Vdash$ $B.$ |
| $k$ $\Vdash$ $(A \rightarrow B)$ | if, for every $k' \ge k,$ if $k'$ $\Vdash$ $A$ then $k'$ $\Vdash$ $B.$ |
| $k$ $\Vdash$ $\neg A$ | if for no $k' \ge k$ does $k'$ $\Vdash$ $A.$ |
| $k$ $\Vdash$ $\forall x A(x)$ | if for every $k' \ge k$ and every $d \in D(k'),$ $k'$ $\Vdash$ $A(d).$ |
| $k$ $\Vdash$ $\exists x A(x)$ | if for some $d \in D(k),$ $k$ $\Vdash$ $A(d).$ |

Any such forcing relation is *consistent*:

For no sentence $A$ and no $k$ is it the case that both $k$ $\Vdash$ $A$ and $k$ $\Vdash$ $\neg A.$

and *monotone*:

If $k \le k'$ and $k$ $\Vdash$ $A$ then $k'$ $\Vdash$ $A.$

**Kripke’s Soundness and Completeness Theorems** establish that a sentence of $L$ is provable in intuitionistic predicate logic if and only if it is forced by every node of every Kripke structure. Thus to show that $\neg \forall x \neg P(x) \rightarrow \exists x P(x)$ is intuitionistically unprovable, it is enough to consider a Kripke structure with $K = \{k, k'\},$ $k \lt k',$ $D(k) = D(k') = \{0\},$ $T(P, k)$ empty but $T(P, k') = \{0\}.$ And to show the converse is intuitionistically provable (without actually exhibiting a proof), one only needs the consistency and monotonicity properties of arbitrary Kripke models, with the definition of $\Vdash.$

Kripke models for languages with equality may interpret $=$ at each node by an arbitrary equivalence relation, subject to monotonicity. For applications to intuitionistic arithmetic, *normal* models (those in which equality is interpreted by identity at each node) suffice because equality of natural numbers is decidable.

Propositional Kripke semantics is particularly simple, since an arbitrary propositional formula is intuitionistically provable if and only if it is forced by the root of every Kripke model whose *frame* (the set $K$ of nodes together with their partial ordering) is a finite tree with a least element (the *root*). For example, the Kripke model with $K = \{k, k', k''\}, k \lt k'$ and $k \lt k'',$ and with $P$ true only at $k',$ shows that both $P \vee \neg P$ and $\neg P \vee \neg \neg P$ are unprovable in $\mathbf{IPC}.$

Each terminal node or *leaf* of a Kripke model is a classical model, because a leaf forces every formula or its negation. Only those proposition letters which occur in a formula $E,$ and only those nodes $k'$ such that $k\le k',$ are relevant to deciding whether or not $k$ forces $E.$ Such considerations allow us to associate effectively with each formula $E$ of $L(\mathbf{IPC})$ a finite class of finite Kripke structures which will include a countermodel to $E$ if one exists. Since the class of all theorems of $\mathbf{IPC}$ is recursively enumerable, we conclude that:

$\mathbf{IPC}$ is effectively decidable. There is a recursive procedure which determines, for each propositional formula $E,$ whether or not $E$ is a theorem of $\mathbf{IPC},$ concluding with either a proof of $E$ or a (finite) Kripke countermodel.

The decidability of $\mathbf{IPC}$ was first obtained by Gentzen in 1935. The undecidability of $\mathbf{IQC}$ follows from the undecidability of $\mathbf{CQC}$ by the negative interpretation.

Familiar non-intuitionistic logical schemata correspond to structural properties of Kripke models, for example:

- DNS holds in every Kripke model with finite frame.
- $(A \rightarrow B) \vee (B \rightarrow A)$ holds in every Kripke model with linearly ordered frame. Conversely, every propositional formula which is not derivable in $\mathbf{IPC} + (A \rightarrow B) \vee (B \rightarrow A)$ has a Kripke countermodel with linearly ordered frame (cf. Section 6.1 below).
- If $x$ is not free in $A$ then $\forall x (A \vee B(x)) \rightarrow (A \vee \forall x B(x))$ holds in every Kripke model $\mathbf{K}$ with constant domain (so that $D(k) = D(k')$ for all $k, k'$ in $K).$ The same is true for MP.

**Beth’s semantic tableaux**, inspired by Brouwer’s notion of *spread*, predated Kripke’s semantics; [Troelstra and van Ulsen](https://festschriften.illc.uva.nl/j50/contribs/troelstra/) give an authoritative account of the history. For a modern version of Beth semantics which facilitates comparison with Kripke semantics, a *Beth structure* is a Kripke structure in which the partially ordered set $K$ is a rooted tree with $k_0$ as the root, and the forcing conditions in a *Beth model* are the same as those in a Kripke model with two exceptions. The forcing conditions for $(A \vee B)$ and $\exists x A(x)$ in a Beth model are as follows, where a *branch* of $K$ is a maximal linearly ordered subset $k_0 \le k_1 \le k_2 \le ...$ of $K.$

| $k$ $\Vdash$ $(A \vee B)$ | if every branch of $K$ passing through $k$ contains a node $k' \ge k$ such that $k'$ $\Vdash$ $A$ or $k'$ $\Vdash$ $B.$ |
| --- | --- |
| $k$ $\Vdash$ $\exists x A(x)$ | if every branch of $K$ passing through $k$ contains a node $k' \ge k$ such that $k'$ $\Vdash$ $A(d)$ for some $d \in D(k').$ |

To use a temporal analogy, a Beth model allows a decision between two alternatives, or the production of a witness to an existential statement, to be postponed until more information and possibly more individuals are available. A Kripke model demands an immediate decision between two alternatives, or the immediate choice of a witness to an existential statement from the current domain of individuals.

Kripke models and Beth models are powerful tools for establishing properties of intuitionistic formal systems; cf. Troelstra and van Dalen [1988], Smorynski [1973], de Jongh and Smorynski [1976], Ghilardi [1999] and Iemhoff [2001], [2005]. However, there is no purely intuitionistic proof that every sentence which is valid in all Kripke and Beth models is provable in $\mathbf{IQC}.$ Following an observation by Gödel, Kreisel [1958] verified that the completeness of intuitionistic predicate logic for Beth semantics is equivalent to Markov’s Principle MP, which Brouwer rejected.

Moreover, Dyson and Kreisel [1961] showed that if $\mathbf{IQC}$ is *weakly* complete for Beth semantics (that is, if no unprovable sentence holds in every Beth model) then the following consequence of MP holds : $$ \tag{GDK} \forall \alpha_{B(\alpha)} \neg \neg \exists x R(\alpha, x) \rightarrow \neg \neg \forall \alpha_{B(\alpha)} \exists x R(\alpha, x),$$ where $x$ ranges over all natural numbers, *α* ranges over all infinite sequences of natural numbers, $B(\alpha)$ abbreviates $\forall x (\alpha(x) \leq 1),$ and $R$ expresses a primitive recursive relation of *α* and $x.$ Conversely, GDK entails the weak completeness of $\mathbf{IQC}.$ This interesting principle, considered as a schema with $R$ required to be quantifier-free, would justify the negative interpretation of a form of Brouwer’s Fan Theorem. It is weaker than MP but unprovable in current systems of intuitionistic analysis. Kreisel [1962] suggested that GDK may eventually be provable on the basis of as yet undiscovered properties of intuitionistic mathematics.

By modifying the definition of a Kripke model to allow “exploding nodes” which force every sentence, Veldman [1976] and de Swart [1976] independently found completeness proofs using only intuitionistic logic. However, Veldman questioned whether Kripke models with exploding nodes were intuitionistically meaningful mathematical objects.

### 5.2 Realizability semantics for Heyting arithmetic

One way to implement the B-H-K explanation of intuitionistic truth for arithmetic is to associate with each sentence $E$ of $\mathbf{HA}$ some collection of numerical codes for algorithms which could establish the constructive truth of $E.$ Following Kleene [1945], a number $e$ *realizes* a sentence $E$ of the language of arithmetic by induction on the logical form of $E$:

| $e$ realizes $r = t$ | if $r = t$ is true. |
| --- | --- |
| $e$ realizes $A \oldand B$ | if $e$ codes a pair $(f,g)$ such that $f$ realizes $A$ and $g$ realizes $B.$ |
| $e$ realizes $A \vee B$ | if $e$ codes a pair $(f,g)$ such that if $f = 0$ then $g$ realizes $A,$ and if $f \gt 0$ then $g$ realizes $B.$ |
| $e$ realizes $A\rightarrow B$ | if, whenever $f$ realizes $A,$ then the $e$th partial recursive function is defined at $f$ and its value realizes $B.$ |
| $e$ realizes $\neg A$ | if no $f$ realizes $A.$ |
| $e$ realizes $\forall x A(x)$ | if, for every $n,$ the $e$th partial recursive function is defined at $n$ and its value realizes $A(\mathbf{n}).$ |
| $e$ realizes $\exists x A(x)$ | if $e$ codes a pair $(n,g)$ and $g$ realizes $A(\mathbf{n}).$ |

An arbitrary formula is realizable if some number realizes its universal closure. Observe that not both $A$ and $\neg A$ are realizable, for any formula $A.$ The fundamental result is:

**Nelson’s Theorem** [1947] If $A$ is derivable in $\mathbf{HA}$ from realizable formulas $F,$ then $A$ is realizable.

Some nonintuitionistic principles can be shown to be realizable. For example, *Markov’s Principle* (for decidable formulas) can be expressed by the schema

**(MP)**

$\forall x (A(x) \vee \neg A(x)) \oldand \neg \forall x \neg A(x) \rightarrow \exists x A(x).$

Although unprovable in $\mathbf{HA},$ MP is realizable by an argument which uses Markov’s Principle informally. But realizability is a fundamentally nonclassical interpretation. In $\mathbf{HA}$ it is possible to express an axiom of recursive choice CT (for “Church’s Thesis”), which contradicts LEM but is (constructively) realizable. Hence by Nelson’s Theorem, $\mathbf{HA}$ $+$ MP $+$ CT is consistent.

Kleene used a variant of number-realizability to prove $\mathbf{HA}$ satisfies the Church-Kleene Rule; the same argument works for $\mathbf{HA}$ with MP or CT, and for $\mathbf{HA}$ $+$ MP $+$ CT. In Kleene and Vesley [1965] and Kleene [1969], functions replace numbers as realizing objects, establishing the consistency of formalized intuitionistic analysis and its closure under a second-order version of the Church-Kleene Rule.

Nelson’s Theorem establishes the unprovability in $\mathbf{IQC}$ of some theorems of classical predicate logic. If, to each $n$-place predicate letter $P(\ldots ),$ a formula $f(P)$ of $L(\mathbf{HA})$ with $n$ free variables is assigned, and if the formula $f(A)$ of $L(\mathbf{HA})$ comes from the formula $A$ of $L$ by replacing each prime formula $P(x_1, \ldots, x_n)$ by $f(P)(x_1 ,\ldots ,x_n),$ then $f(A)$ is called an *arithmetical substitution instance* of $A.$ As an example, if a formula of $L(\mathbf{HA})$ expressing “$y$ is the code of a sentence and $x$ codes a proof in $\mathbf{HA}$ of the sentence with code $y$” is assigned to $P(x,y),$ then (assuming $\mathbf{HA}$ is consistent) the resulting arithmetical substitution instance of $\forall y (\exists x P(x, y) \vee \neg \exists x P(x, y))$ is unrealizable and hence unprovable in $\mathbf{HA},$ and so is its double negation. It follows that $\neg \neg \forall y (\exists x P(x, y) \vee \neg \exists x P(x, y))$ is not provable in $\mathbf{IQC}.$

De Jongh [1970] combined realizability with Kripke modeling to show that intuitionistic propositional logic $\mathbf{IPC}$ and a fragment of $\mathbf{IQC}$ are *arithmetically complete* for $\mathbf{HA}.$ A uniform assignment of simple existential formulas to predicate letters suffices to prove:

**De Jongh’s Theorem (for IPC) [1970]** If a propositional formula $A$ of the language $L$ is not provable in $\mathbf{IPC},$ then some arithmetical substitution instance of $A$ is not provable in $\mathbf{HA}.$

The proof of this version of de Jongh’s Theorem does not need realizability; cf. Smorynski [1973]. As an example, Rosser’s form of Gödel’s Incompleteness Theorem provides a sentence $C$ of $L(\mathbf{HA})$ such that $\mathbf{PA}$ proves neither $C$ nor $\neg C,$ so by the disjunction property $\mathbf{HA}$ cannot prove $(C \vee \neg C).$ But de Jongh’s semantical proof also established that every intuitionistically unprovable predicate formula of a restricted kind has an arithmetical substitution instance which is unprovable in $\mathbf{HA}.$ Using a syntactic method, Daniel Leivant [1979] extended de Jongh’s Theorem to all intuitionistically unprovable predicate formulas, proving that $\mathbf{IQC}$ is arithmetically complete for $\bf{HA}.$ See van Oosten [1991] for a historical exposition and a simpler proof of the full theorem, using abstract realizability with Beth models instead of Kripke models.

Without claiming that number-realizability coincides with intuitionistic arithmetical truth, Nelson observed that for each formula $A$ of $L(\mathbf{HA})$ the predicate “$y$ realizes $A$” can be expressed in $\mathbf{HA}$ by another formula (abbreviated “$y \realizesrel A$”), and the schema $A \leftrightarrow \exists y (y \realizesrel A)$ is consistent with $\mathbf{HA}.$ Troelstra [1973] showed that $(A \leftrightarrow \exists y (y \realizesrel A))$ is *equivalent* over $\mathbf{HA}$ to “extended Church’s Thesis” ECT, a stronger version of CT enabling recursive choice under assumptions which are “almost negative” (containing no $\vee,$ and with $\exists x$ only applied to prime formulas). While $\mathbf{HA}$ is sound but not complete for Kleene’s number-realizability, the next theorem shows that $\mathbf{HA}$ + ECT is both sound and complete for this interpretation.

> **Troelstra’s Characterization Theorem (for number-realizability over $\mathbf{HA}$) [1973]**
> If $A$ is a closed formula of the language $L(\mathbf{HA}),$ then:
>
> 1. $\mathbf{HA}$ + ECT $\vdash$ $(A \leftrightarrow \exists y (y \realizesrel A)).$
> 2. $\mathbf{HA}$ + ECT $\vdash$ $A$ if and only if $\mathbf{HA}$ $\vdash$ $\exists y (y \realizesrel A).$

In $\mathbf{HA}$ $+$ MP $+$ ECT, which Troelstra considers to be a formalization of Russian recursive mathematics (cf. section 3.2 of the entry on constructive mathematics), every formula of the form $(y \realizesrel A)$ has an equivalent “classical” prenex form $A'(y)$ consisting of a quantifier-free subformula preceded by alternating “classical” quantifiers of the forms $\neg \neg \exists x $ and $\forall z \neg \neg ,$ and so $\exists y A'(y)$ is a kind of prenex form of $A.$

## 6. Additional Topics and Further Reading

### 6.1 Subintuitionistic and Intermediate Logics

At present there are several other entries in this encyclopedia treating intuitionistic logic in various contexts, but a general treatment of weaker and stronger propositional and predicate logics appears to be lacking. Many such logics have been identified and studied. Here are a few examples.

A *subintuitionistic propositional logic* can be obtained from $\mathbf{IPC}$ by restricting the language, or weakening the logic, or both. An extreme example of the first is $\mathbf{RN},$ intuitionistic logic with a single propositional variable $P,$ which is named after its discoverers Rieger and Nishimura [1960]. $\mathbf{RN}$ is characterized by the *Rieger-Nishimura lattice* of infinitely many nonequivalent formulas $F_n$ such that every formula whose only propositional variable is $P$ is equivalent by intuitionistic logic to some $F_n.$ Nishimura’s version is

$$\begin{align*} F_{\infty} &= P \rightarrow P. \\ F_0 &= P \oldand \neg P. \\ F_1 &= P. \\ F_2 &= \neg P.\\ F_{2 n + 3} &= F_{2 n + 1} \vee F_{ 2n + 2}. \\ F_{2 n + 4} &= F_{2 n + 3} \rightarrow F_{2 n + 1}. \end{align*}$$

In $\mathbf{RN}$ neither $F_{2 n + 1}$ nor $F_{2 n + 2}$ implies the other; but $F_{2 n}$ implies $F_{2 n + 1},$ and $F_{2 n + 1}$ implies each of $F_{2 n + 3}$ and $F_{2 n + 4}.$

Fragments of $\mathbf{IPC}$ missing one or more logical connectives restrict the language and incidentally the logic, since the intuitionistic connectives $\oldand,$ $\vee,$ $\rightarrow,$ $\neg$ are logically independent over $\mathbf{IPC}.$ Rose [1953] proved that the *implicationless fragment* (without $\rightarrow$) is complete with respect to realizability, in the sense that if every arithmetical substitution instance of a propositional formula $E$ without $\rightarrow$ is (number)-realizable then $E$ is a theorem of $\mathbf{IPC}.$ This result contrasts with:

**Rose’s Theorem** [1953] $\mathbf{IPC}$ is incomplete with respect to realizability.

Let $F$ be the propositional formula $$ ( ( \neg \neg D \rightarrow D) \rightarrow ( \neg \neg D \vee \neg D ) ) \rightarrow ( \neg \neg D \vee \neg D) $$ where $D$ is $(\neg P \vee \neg Q)$ and $P,$ $Q$ are prime. Every arithmetical substitution instance of $F$ is realizable (using classical logic), but $F$ is not provable in $\mathbf{IPC}.$

It follows that $\mathbf{IPC}$ is arithmetically incomplete for $\mathbf{HA}$ $+$ ECT (cf. Section 5.2).

*Minimal logic* $\mathbf{ML}$ comes from intuitionistic logic by deleting *ex falso*. Kolmogorov [1925] showed that this fragment already contains a negative interpretation of classical logic retaining both quantifiers, cf. Leivant [1985]. Minimal logic does prove the special case $\neg A \rightarrow (A \rightarrow \neg B)$ of *ex falso* for negations. Colacito, de Jongh and Vardas [2017] study various *subminimal logics*, each weaker than $\mathbf{ML}.$

Tennant [2017] has proposed a radical intuitionistic *Core Logic* $\mathbf{CL}$ in which the Deduction Theorem is sacrificed along with *ex falso*. Unsatisfiable assumptions entail only falsity; thus $\neg A \vdash (A \rightarrow B)$ but $\neg A, A \not\vdash B$ (unless $B$ is $\bot$). All core proofs are in normal form; in a core deduction all assumptions are *relevant*.

Griss contested Brouwer’s use of negation, objecting to both the law of contradiction and *ex falso*. It is worth noting that negation is not really needed for intuitionistic mathematics since $0 = 1$ is a known contradiction so $\neg A$ can be defined by $A \rightarrow 0 = 1.$ Then *ex falso* can be stated as $0 = 1 \rightarrow A,$ and the law of contradiction is provable from the remaining axioms of $\mathbf{H}.$

An *intermediate propositional logic* is any consistent collection of propositional formulas containing all the axioms of $\mathbf{IPC}$ and closed under *modus ponens* and substitution of arbitrary formulas for proposition letters. Each intermediate propositional logic is contained in $\mathbf{CPC}.$ Some particular intermediate propositional logics, characterized by adding one or more classically correct but intuitionistically unprovable axiom schemas to $\mathbf{IPC},$ have been studied extensively.

One of the simplest intermediate propositional logics is the Gödel-Dummett logic $\mathbf{LC},$ obtained by adding to $\mathbf{IPC}$ the schema $(A \rightarrow B) \vee (B \rightarrow A)$ which is valid on all and only those Kripke frames in which the partial order of the nodes is linear. Gödel [1932] used an infinite sequence of successively stronger intermediate logics to show that $\mathbf{IPC}$ has no finite truth-table interpretation. For each positive integer $n,$ let $\mathbf{G_n}$ be $\mathbf{LC}$ plus the schema $(A_1 \rightarrow A_2) \vee \ldots \vee (A_1 \oldand \ldots \oldand A_n \rightarrow A_{n + 1}).$ Then $\mathbf{G_n}$ is valid on all and only those linearly ordered Kripke frames with no more than $n$ nodes.

The Jankov logic $\mathbf{KC},$ which adds to $\mathbf{IPC}$ the principle of *testability* $\neg A \vee \neg \neg A,$ obviously does not have the disjunction property. The Kreisel-Putnam logic $\mathbf{KP},$ obtained by adding to $\mathbf{IPC}$ the schema $(\neg A \rightarrow (B \vee C)) \rightarrow((\neg A \rightarrow B) \vee (\neg A \rightarrow C)),$ has the disjunction property but does not satisfy all the Visser rules. The intermediate logic obtained by adding the schema

$$((\neg \neg D \rightarrow D) \rightarrow(D \vee \neg D)) \rightarrow (\neg \neg D \vee \neg D),$$

corresponding to Rose’s counterexample, to $\mathbf{IPC}$ also has the disjunction property. Iemhoff [2005] proved that $\mathbf{IPC}$ is the only intermediate propositional logic with the disjunction property which is closed under all the Visser rules. Iemhoff and Metcalfe [2009] developed a formal calculus for generalized admissibility for $\mathbf{IPC}$ and some intermediate logics. Goudsmit [2015] is a thorough study of the admissible rules of intermediate logics, with a comprehensive bibliography.

An intermediate propositional logic $\mathbf{L}$ is said to have the *finite frame property* if there is a class of finite frames on which the Kripke-valid formulas are exactly the theorems of $\mathbf{L}.$ Many intermediate logics, including $\mathbf{LC}$ and $\mathbf{KP},$ have this property. Jankov [1968] used an infinite sequence of finite rooted Kripke frames to prove that there are continuum many intermediate logics. De Jongh, Verbrugge and Visser [2009] proved that every intermediate logic $\mathbf{L}$ with the finite frame property is the *propositional logic* of $\mathbf{HA(L)},$ that is, the class of all formulas in the language of $\mathbf{IPC}$ all of whose arithmetical substitution instances are provable in the logical extension of $\mathbf{HA}$ by $\mathbf{L}.$

An intermediate propositional logic $\mathbf{L}$ is *structurally complete* if every rule which is admissible for $\mathbf{L}$ is derivable in $\mathbf{L},$ and *hereditarily structurally complete* if every intermediate logic extending $\mathbf{L}$ is also structurally complete. Every intermediate logic $\mathbf{L}$ has a *structural completion* $\mathbf{\overline{L}},$ obtained by adjoining all its admissible rules. $\mathbf{LC}$ and $\mathbf{G_n}$ are hereditarily structurally complete. While $\mathbf{IPC},$ $\mathbf{RN}$ and $\mathbf{KC}$ are not structurally complete, their structural completions are hereditarily structurally complete. For these results and more, see Citkin [2016, Other Internet Resources].

Some *intermediate predicate logics*, extending $\mathbf{IQC}$ and closed under substitution, are $\mathbf{IQC}$ $+$ DNS (Section 4.1), $\mathbf{IQC}$ $+$ MP (cf. Section 5.2), $\mathbf{IQC}$ $+$ MP $+$ IP (cf. Section 4.2), and the *intuitionistic logic of constant domains* $\mathbf{CD}$ obtained by adding to $\mathbf{IQC}$ the schema $\forall x (A \vee B(x)) \rightarrow (A \vee \forall x B(x))$ for all formulas $A,$ $B(x)$ with $x$ not occurring free in $A.$ Mints, Olkhovikov and Urquhart [2013] showed that $\mathbf{CD}$ does not have the interpolation property, refuting earlier published proofs by other authors.

### 6.2 Basic Intuitionistic Modal Logic

This section offers only a glimpse of intuitionistic modal logic. Any classical modal logic has an intuitionistic companion defined by replacing the underlying classical propositional or predicate logic by the corresponding intuitionistic propositional or predicate logic. Simpson [1994] and Plotkin and Stirling [1986] provide a general framework for intuitionistic modal logics which is adaptable to a multitude of uses.

The basic intuitionistic modal propositional logic $\mathbf{iK}$ has as axioms:

- all propositional axioms of intuitionistic logic in the modal language with logical connectives $\wedge, \vee, \rightarrow, \leftrightarrow, \neg,$ logical constants $\top$ and $\bot,$ and a unary operator $\Box$ (necessity), and
- all substitution instances of Kripke’s distributive schema $\Box(A \rightarrow B) \rightarrow (\Box A \rightarrow \Box B);$

and as rules of inference all substitution instances of:

- modus ponens: from $A$ and $(A \rightarrow B),$ infer $B,$ and
- necessitation: from $A$ infer $\Box A.$

$\mathbf{iL}$ adds to $\mathbf{iK}$ the Löb axiom schema $\Box (\Box A \rightarrow A) \rightarrow \Box A.$

$\mathbf{iK4}$ adds to $\mathbf{iL}$ the transitive axiom schema $\Box A \rightarrow \Box \Box A.$

The unary operator $\lozenge$ (possibility), classically equivalent to $\neg \Box \neg$, increases the expressiveness of the intuitionistic modal language. Simpson argues that the correct intuitionistic analogue of the classical modal logic $\mathbf{K}$ is Plotkin and Stirling’s $\mathbf{IK}$, which treats $\lozenge$ as an additional primitive and adds to $\mathbf{iK}$ the schemas:

- $\Box (A \rightarrow B) \rightarrow (\lozenge A \rightarrow \lozenge B).$
- $\neg \lozenge \bot.$
- $\lozenge (A \vee B) \rightarrow (\lozenge A \vee \lozenge B).$
- $(\lozenge A \rightarrow \Box B) \rightarrow \Box (A \rightarrow B).$

### 6.3 Advanced topics

Brouwer’s influence on Gödel was significant, although Gödel never became an intuitionist. Gödel’s [1933f] translation of intuitionistic propositional logic into the modal logic $\mathbf{S4}$ is described in Section 2.5 of the entry on Gödel and in Troelstra’s introductory note to the translation of [1933f] in Volume I of Gödel’s Collected Works. See also Mints [2012]. Kripke models for modal logic predated those for intuitionistic logic.

Alternatives to Kripke and Beth semantics for intuitionistic propositional and predicate logic include the topological interpretation of Stone [1937], Tarski [1938] and Mostowski [1948] (cf. Rasiowa and Sikorski [1963], Rasiowa [1974]), which was extended to intuitionistic analysis by Scott [1968] and Krol [1978]. M. Hyland [1982] defined the effective topos *Eff* and proved that its logic is intuitionistic. For a very informative discussion of semantics for intuitionistic logic and mathematics by W. Ruitenberg, and an interesting new perspective by G. Bezhanishvili and W. Holliday, see Other Internet Resources (below).

One alternative to realizability semantics for intuitionistic arithmetic is Gödel’s [1958] “Dialectica” interpretation, which associates with each formula $B$ of $L(\mathbf{HA})$ a quantifier-free formula $B_D$ in the language of intuitionistic arithmetic of all finite types. The *“Dialectica” interpretation* of $B,$ call it $B^D,$ is $\exists Y\forall x B_D (Y, x).$ If $B$ is a closed theorem of $\mathbf{HA},$ then $B_D (F, x)$ is provable for some term $F$ in Gödel’s theory $\mathbf{T}$ of “primitive recursive” functionals of higher type. The translation from $B$ to $B^D$ requires the axiom of choice (at all finite types), MP and IP, so is not strictly constructive; however, the number-theoretic functions expressible by terms $F$ of $\mathbf{T}$ are precisely the provably recursive functions of $\mathbf{HA}$ (and of $\mathbf{PA}).$ The interpretation was extended to analysis by Spector [1962]; cf. Howard [1973]. Clear expositions, and additional references, are to be found in Troelstra’s introduction to the English translation in Gödel [1990] of the original *Dialectica* article, in Avigad and Feferman [1998], and in Ferreira [2008].

While $\mathbf{HA}$ is a proper part of classical arithmetic, the intuitionistic attitude toward mathematical objects results in a theory of real numbers (cf. sections 3.4–3.7 of the entry on intuitionism in the philosophy of mathematics) diverging from the classical. Kleene’s function-realizability interpretation, developed to prove the consistency of his formalization $\mathbf{FIM}$ of the intuitionistic theory of sequences (“intuitionistic analysis”), changes the interpretation of arithmetical formulas; for example, $\neg \neg \forall x (A(x) \vee \neg A(x))$ is function-realizable for every arithmetical formula $A(x).$ In the language of analysis, Markov’s Principle and the negative translation of the countable axiom of choice are among the many non-intuitionistic principles which are function-realizable (by classical arguments) and hence consistent with $\mathbf{FIM};$ cf. Kleene [1965], Vesley [1972] and Moschovakis [2003].

Concrete and abstract realizability semantics for a wide variety of formal systems have been developed and studied by logicians and computer scientists; cf. Troelstra [1998] and van Oosten [2002] and [2008]. Variations of the basic notions are especially useful for establishing relative consistency and relative independence of the nonlogical axioms in theories based on intuitionistic logic; some examples are Moschovakis [1971], Lifschitz [1979], and the realizability notions for constructive and intuitionistic set theories developed by Rathjen [2006, 2012] and Chen [2012]. Early abstract realizability notions include the *slashes* of Kleene [1962, 1963] and Aczel [1968], and Läuchli [1970]. Kohlenbach, Avigad and others have developed realizability interpretations for parts of classical mathematics.

Artemov’s justification logic is an alternative interpretation of the B-H-K explanation of the intuitionistic connectives and quantifiers, with (idealized) proofs playing the part of realizing objects. See also Artemov and Iemhoff [2007].

Another line of research in intuitionistic logic concerns Brouwer’s controversial “creating subject counterexamples” to principles of classical analysis (such as Markov’s Principle) which could not be refuted on the basis of the theory $\mathbf{FIM}$ of Kleene and Vesley [1965]. By weakening Kleene’s strong form of Brouwer’s principle of continuous choice, and adding an axiom he called *Kripke’s Schema* (KP), Myhill [1967] formalized Brouwer’s creating subject arguments in the language of intuitionistic analysis. Krol [1978] and Scowcroft gave topological consistency proofs for intuitionistic analysis with Kripke’s Schema and weak continuity. Kripke himself preferred *Weak Kripke’s Schema* (WKP), which still conflicts with strong continuous choice. Kripke [2019] and Brauer, Linnebo and Shapiro [2022] recently provided an attractive modal interpretation of Brouwer’s theory of the creating subject.

Vesley [1970] found an alternative principle (*Vesley’s Schema* VS) which can consistently be added to $\mathbf{FIM}$ and implies all the counterexamples for which Brouwer required a creating subject. Troelstra’s *generalized continuous* choice (GC), which characterizes Kleene’s function-realizability just as his ECT characterizes number-realizability, and Vesley’s VS express two incompatible possible extensions of intuitionistic analysis, with different mathematical properties.

Constructive mathematicians, following Bishop, traditionally assume intuitionistic logic and work with strong definitions of concepts. For example, they equate “there is at most one number $n$ such that $P(n)$” with “if $n$ and $m$ are distinct numbers then not $P(n)$ or not $P(m),$” rather than the more natural “if $n$ and $m$ are numbers such that $P(n)$ and $P(m)$ then $n = m$”. Shulman [2022] suggests that an “affine” logic of proof and refutation, with additional connectives and an antithesis translation into intuitionistic logic, would be more useful for constructive mathematics.

### 6.4 Recommended reading

The entry on L. E. J. Brouwer discusses Brouwer’s philosophy and mathematics, with a chronology of his life and a selected list of publications including translations and secondary sources. The best way to learn more is to read some of the original papers. English translations of Brouwer’s doctoral dissertation and other papers which originally appeared in Dutch, along with a number of articles in German, can be found in *L. E. J. Brouwer: Collected Works* [1975], edited by Heyting. Benacerraf and Putnam’s essential source book contains Brouwer [1912] (in English translation), Brouwer [1949] and Dummett [1975]. Mancosu’s [1998] provides English translations of many fundamental articles by Brouwer, Heyting, Glivenko and Kolmogorov, with illuminating introductory material by W. van Stigt whose [1990] is another valuable resource.

A delightful, accessible and authoritative introduction to intuitionistic mathematics and logic is Wim Veldman’s [2021]. The third edition [1971] of Heyting’s classic [1956] is an attractive introduction to intuitionistic philosophy, logic and mathematical practice. As part of the formidable project of editing and publishing Brouwer’s *Nachlass*, van Dalen [1981] provides a comprehensive view of Brouwer’s own intuitionistic philosophy. The English translation, in van Heijenoort [1969], of Brouwer’s [1927] (with a fine introduction by Parsons) is still an indispensable reference for Brouwer’s theory of the continuum. Veldman [1990] and [2005] are authentic modern examples of traditional intuitionistic mathematical practice. Troelstra [1991] places intuitionistic logic in its historical context as the common foundation of constructive mathematics in the twentieth century. Bezhanishvili and de Jongh [2005, Other Internet Resources] includes recent developments in intuitionistic logic.

Kleene and Vesley’s [1965] gives a careful axiomatic treatment of intuitionistic analysis, a proof of its consistency relative to a classically correct subtheory, and an extended application to Brouwer’s theory of real number generators. Kleene’s [1969] formalizes the theory of partial recursive functionals, enabling precise formalizations of the function-realizability interpretation used in [1965] and of a related q-realizability interpretation which gives the Church-Kleene Rule for intuitionistic analysis.

Troelstra’s [1973], Beeson’s [1985] and Troelstra and van Dalen’s [1988] (with [corrections](https://www.math.ucla.edu/%7Ejoan/ourTvDcorr030818.pdf)) stand out as the most comprehensive studies of intuitionistic and semi-intuitionistic formal theories, using both constructive and classical methods, with useful bibliographies. Troelstra and Schwichtenberg [2000] presents the proof theory of classical, intuitionistic and minimal logic in parallel, focusing on sequent systems. Troelstra’s [1998] presents formulas-as-types and (Kleene and Aczel) slash interpretations for propositional and predicate logic, as well as abstract and concrete realizabilities for a multitude of applications. Martin-Löf’s constructive theory of types [1984] (cf. Section 3.4 of the entry on constructive mathematics) provides another general framework within which intuitionistic reasoning continues to develop.

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=logic-intuitionistic). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/logic-intuitionistic/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=logic-intuitionistic&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/logic-intuitionistic/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

- Bezhanishvili, G. and Holliday, W., 2018, “[A semantic hierarchy for intuitionistic logic](https://escholarship.org/uc/item/2vp2x4rx),” manuscript, UC Berkeley Faculty Publications.
- Bezhanishvili, N. and de Jongh, D. H. J., 2005, [*Intuitionistic Logic*](http://www.cs.le.ac.uk/people/nb118/Publications/ESSLLI'05.pdf), Lecture notes presented at ESSLLI, Edinburgh.
- Brouwer, [Excerpts from Brouwer’s Cambridge lectures.](http://www.marxists.org/reference/subject/philosophy/works/ne/brouwer.htm)
- Citkin, A., 2016, “[Hereditarily structurally complete superintuitionistic deductive systems](https://arxiv.org/pdf/1611.04809.pdf),” manuscript at arXiv.org.
- de Paiva, Valeria, 2015, [Intuitionistic modal logic: 15 years later](https://logic.berkeley.edu/colloquium/dePaivaSlides.pdf).
- Troelstra, A. S., 2018, [Corrections to some publications](https://eprints.illc.uva.nl/id/eprint/1650).
- Troelstra, A. S., and van Ulsen, P., [The discovery of E. W. Beth’s semantics for intuitionistic logic](https://festschriften.illc.uva.nl/j50/contribs/troelstra/).
- [Realizability Bibliography](https://cs.au.dk/~birke/realizability/index.html), maintained by Lars Birkedal.
- [van Oosten 2000, and other preprints related to realizability,](http://www.math.uu.nl/people/jvoosten/realizability.html) maintained by Jaap van Oosten.

## Related Entries

Brouwer, Luitzen Egbertus Jan | Gödel, Kurt | logic, history of: intuitionistic logic | logic: classical | logic: modal | logic: provability | logicism and neologicism | mathematics, philosophy of | mathematics, philosophy of: formalism | mathematics, philosophy of: intuitionism | mathematics, philosophy of: Platonism | mathematics: constructive | proof theory: development of | set theory: constructive and intuitionistic ZF

### Acknowledgments

I would like to thank Wim Veldman especially for his recent open-access article “Intuitionism: An Inspiration?”, which is a gift to curious students, mathematically inclined philosophers and philosophically inclined mathematicians. Veldman is a practicing intuitionistic mathematician whose mentor was M. de Jongh, one of Brouwer’s students. *Intuitionism: An Introduction* was written more than half a century ago by another of Brouwer’s students, A. Heyting, for a similar audience. The similarity of titles is appropriate.

Over the years, many readers and a few wise and conscientious referees have offered corrections and improvements to this entry. I am still grateful to Edward Horton (for pointing out that replacing *ex falso* by the LEM in the axioms for $\mathbf{IPC}$ does not yield all of $\mathbf{CPC},$ and for providing the correct substitutions) and to all the other readers who have corrected errors in earlier editions. I thank Mark van Atten, Robert Thomas, Victor Pambuccian, Michael Beeson, Mariusz Stopa and Antonino Drago for bringing new and old work to my attention since the last revision. Questions from students are always appreciated; this time, Miles Shi’s question led to an improvement in Section 5. As always, I thank Ed Zalta for his patience and attention to detail, and for the very existence of this comprehensive open-access encyclopedia.

[^aczel-1968]: Aczel, P., 1968, “Saturated intuitionistic theories,” in H.A. Schmidt, K. Schütte, and H.-J. Thiele (eds.), *Contributions to Mathematical Logic*, Amsterdam: North-Holland: 1–11.

[^artemov-2007]: Artemov, S. and Iemhoff, R., 2007, “The basic intuitionistic logic of proofs,” *Journal of Symbol Logic*, 72: 439–451.

[^avigad-1998]: Avigad, J. and Feferman, S., 1998, “Gödel’s functional (”Dialectica“) interpretation,” Chapter V of Buss (ed.) 1998: 337–405.

[^bar-hillel-1965]: Bar-Hillel, Y. (ed.), 1965, *Logic, Methodology and Philosophy of Science*, Amsterdam: North Holland.

[^beeson-1985]: Beeson, M. J., 1985, *Foundations of Constructive Mathematics*, Berlin: Springer.

[^benacerraf-1983]: Benacerraf, P. and Hilary Putnam (eds.), 1983, *Philosophy of Mathematics: Selected Readings*, 2nd Edition, Cambridge: Cambridge University Press.

[^beth-1956]: Beth, E. W., 1956, “Semantic construction of intuitionistic logic,” *Koninklijke Nederlandse Akad. von Wettenscappen*, 19(11): 357–388.

[^brauer-2022]: Brauer, E., 2022, “The modal logic of potential infinity: convergent versus branching possibilities,” *Erkenntnis* 87:2161–2179.

[^brauer-2022-2]: Brauer, E., Linnebo O. and Shapiro, S., 2022, “Divergent potentialism: a modal analysis with an application to choice sequences,” *Philosophia Mathematica* 30(2): 143–172.

[^brouwer-1907]: Brouwer, L. E. J., 1907, “On the Foundations of Mathematics,” Thesis, Amsterdam; English translation in Heyting (ed.) 1975: 11–101.

[^brouwer-1908]: –––, 1908, “The Unreliability of the Logical Principles,” English translation in Heyting (ed.) 1975: 107–111.

[^brouwer-1912]: –––, 1912, “Intuitionism and Formalism,” English translation by A. Dresden, *Bulletin of the American Mathematical Society*, 20 (1913): 81–96, reprinted in Benacerraf and Putnam (eds.) 1983: 77–89; also reprinted in Heyting (ed.) 1975: 123–138.

[^brouwer-1923]: –––, 1923 [1954], “On the significance of the principle of excluded middle in mathematics, especially in function theory,” “Addenda and corrigenda,” and “Further addenda and corrigenda,” English translation in van Heijenoort (ed.) 1967: 334–345.

[^brouwer-1923c]: –––, 1923C, “Intuitionistische Zerlegung mathematischer Grundbegriffe,” *Jahresbericht der Deutschen Mathematiker-Vereinigung*, 33 (1925): 251–256; reprinted in Heyting (ed.) 1975, 275–280.

[^brouwer-1927]: –––, 1927, “Intuitionistic reflections on formalism,” originally published in 1927, English translation in van Heijenoort (ed.) 1967: 490–492.

[^brouwer-1948]: –––, 1948, “Consciousness, philosophy and mathematics,” originally published (1948), reprinted in Benacerraf and Putnam (eds.) 1983: 90–96.

[^burr-2004]: Burr, W., 2004, “The intuitionistic arithmetical hierarchy,” in J. van Eijck, V. van Oostrom and A. Visser (eds.), *Logic Colloquium ’99* (Lecture Notes in Logic 17), Wellesley, MA: ASL and A. K. Peters, 51–59.

[^buss-1998]: Buss, S. (ed.), 1998, *Handbook of Proof Theory*, Amsterdam and New York: Elsevier.

[^chen-2012]: Chen, R-M. and Rathjen, M., 2012, “Lifschitz realizability for intuitionistic Zermelo-Fraenkel set theory,” *Archive for Mathematical Logic*, 51: 789–818.

[^colacito-2017]: Colacito, A., de Jongh, D. and Vargas, A., 2017, “Subminimal Negation”, *Soft Computing*, 21: 165–164.

[^crossley-1965]: Crossley, J., and M. A. E. Dummett (eds.), 1965, *Formal Systems and Recursive Functions*, Amsterdam: North-Holland Publishing.

[^dalen-1981]: van Dalen, D. (ed.), 1981, *Brouwer’s Cambridge Lectures on Intuitionism*, Cambridge: Cambridge University Press.

[^dummett-1975]: Dummett, M., 1975, “The philosophical basis of intuitionistic logic,” originally published (1975), reprinted in Benacerraf and Putnam (eds.) 1983: 97–129.

[^dyson-1961]: Dyson, V. and Kreisel, G., 1961, *Analysis of Beth’s semantic construction of intuitionistic logic*, Technical Report No. 3, Stanford: Applied Mathematics and Statistics Laboratory, Stanford University.

[^ewald-1986]: Ewald, W. B., 1986, “Intuitionistic tense and modal logic,” *Journal of Symbolic Logic* 51(1): 166–179.

[^ferreira-2008]: Ferreira, F., 2008, “A most artistic package of a jumble of ideas,” *Dialectica*, 62: 205–222.

[^fitting-1987]: Fitting, M., 1987, “Resolution for intuitionistic logic”, *Proceedings of the Second International Symposium on Methodologies for Intelligent Systems*, December 1987: 400–407.

[^friedman-1975]: Friedman, H., 1975, “The disjunction property implies the numerical existence property,” *Proceedings of the National Academy of Science*, 72: 2877–2878.

[^gentzen-1934]: Gentzen, G., 1934–5, “Untersuchungen Über das logische Schliessen,” *Mathematische Zeitschrift*, 39: 176–210, 405–431.

[^ghilardi-1999]: Ghilardi, S., 1999, “Unification in intuitionistic logic,” *Journal of Symbolic Logic*, 64: 859–880.

[^glivenko-1929]: Glivenko, V., 1929, “Sur quelques points de la logique de M. Brouwer,” *Académie Royale de Belgique, Bulletins de la classe des sciences*, 5 (15): 183–188.

[^gödel-1932]: Gödel, K., 1932, “Zum intuitionistischen Aussagenkalkül,” *Anzeiger der Akademie der Wissenschaften in Wien*, 69: 65–66. Reproduced and translated with an introductory note by A. S. Troelstra in Gödel 1986: 222–225.

[^gödel-1933e]: –––, 1933e, “Zur intuitionistischen Arithmetik und Zahlentheorie,” *Ergebnisse eines mathematischen Kolloquiums*, 4: 34–38.

[^gödel-1986]: –––, 1933f, “Eine Interpretation des intuitionistischen Aussagenkalküls,” reproduced and translated with an introductory note by A. S. Troelstra in Gödel 1986: 296–304.

[^gödel-1958]: –––, 1958, “Über eine bisher noch nicht benützte Erweiterung des finiten Standpunktes,” *Dialectica*, 12: 280–287. Reproduced with an English translation in Gödel 1990: 241–251.

[^gödel-1986-2]: –––, 1986, *Collected Works*, Vol. I, S. Feferman *et al*. (eds.), Oxford: Oxford University Press.

[^gödel-1990]: –––, 1990, *Collected Works*, Vol. II, S. Feferman *et al*. (eds.), Oxford: Oxford University Press.

[^goudsmit-2015]: Goudsmit, J. P., 2015, *Intuitionistic Rules: Admissible Rules of Intermediate Logics*, Ph.D. dissertation, University of Utrecht.

[^harrop-1960]: Harrop R., 1960, “Concerning formulas of the types $A \rightarrow B \vee C, A \rightarrow (Ex)B(x)$ in intuitionistic formal systems,” *Journal of Symbolic Logic*, 25: 27–32.

[^heijenoort-1967]: van Heijenoort, J. (ed.), 1967, *From Frege to Gödel: A Source Book In Mathematical Logic 1879–1931*, Cambridge, MA: Harvard University Press.

[^heyting-1930]: Heyting, A., 1930, “Die formalen Regeln der intuitionistischen Logik,” in three parts, *Sitzungsberichte der preussischen Akademie der Wissenschaften*: 42–71, 158–169. English translation of Part I in Mancosu 1998: 311–327.

[^heyting-1956]: –––, 1956, *Intuitionism: An Introduction*, Amsterdam: North-Holland Publishing, 3rd revised edition, 1971.

[^heyting-1975]: Heyting, A. (ed.), 1975, *L. E. J. Brouwer: Collected Works* (Volume 1: *Philosophy and Foundations of Mathematics*), Amsterdam and New York: Elsevier.

[^howard-1973]: Howard, W. A., 1973, “Hereditarily majorizable functionals of finite type,” in Troelstra (ed.) 1973: 454–461.

[^hyland-1982]: Hyland, J. M. E., 1982, “The effective topos,” in Troelstra and van Dalen (ed.) 1982: 165–216.

[^iemhoff-2001]: Iemhoff, R., 2001, “On the admissible rules of intuitionistic propositional logic,” *Journal of Symbolic Logic*, 66: 281–294.

[^iemhoff-2005]: –––, 2005, “Intermediate logics and Visser’s rules,” *Notre Dame Journal of Formal Logic*, 46: 65–81.

[^iemhoff-2009]: Iemhoff, R. and Metcalfe, G., 2009, “Proof theory for admissible rules,” *Annals of Pure and Applied Logic*, 159: 171–186.

[^jankov-1968]: Jankov, V. A., 1968, “The construction of a sequence of strongly independent superintuitionistic propositional calculii,” *Soviet Math. Doklady*, 9: 801–807.

[^jerabek-2008]: Jerabek, E., 2008, “Independent bases of admissible rules,” *Logic Journal of the IGPL*, 16: 249–267.

[^jongh-1970]: de Jongh, D. H. J., 1970, “The maximality of the intuitionistic propositional calculus with respect to Heyting’s Arithmetic,” *Journal of Symbolic Logic*, 6: 606.

[^jongh-1976]: de Jongh, D. H. J., and Smorynski, C., 1976, “Kripke models and the intuitionistic theory of species,” *Annals of Mathematical Logic*, 9: 157–186.

[^jongh-2011]: de Jongh, D., Verbrugge, R. and Visser, A., 2011, “Intermediate logics and the de Jongh property,” *Archive for Mathematical Logic*, 50: 197–213.

[^kino-1970]: Kino, A., Myhill, J. and Vesley, R. E. (eds.), 1970, *Intuitionism and Proof Theory: Proceedings of the summer conference at Buffalo, NY, 1968*, Amsterdam: North-Holland.

[^kleene-1945]: Kleene, S. C., 1945, “On the interpretation of intuitionistic number theory,” *Journal of Symbolic Logic*, 10: 109–124.

[^kleene-1952]: –––, 1952, *Introduction to Metamathematics*, Princeton: Van Nostrand.

[^kleene-1962]: –––, 1962, “Disjunction and existence under implication in elementary intuitionistic formalisms,” *Journal of Symbolic Logic*, 27: 11–18.

[^kleene-1963]: –––, 1963, “An addendum,” *Journal of Symbolic Logic*, 28: 154–156.

[^kleene-1965]: –––, 1965, “Classical extensions of intuitionistic mathematics,” in Bar-Hillel (ed.) 1965: 31–44.

[^kleene-1969]: –––, 1969, *Formalized Recursive Functionals and Formalized Realizability*, Memoirs of the American Mathematical Society 89.

[^kleene-1965-2]: Kleene, S. C. and Vesley, R. E., 1965, *The Foundations of Intuitionistic Mathematics, Especially in Relation to Recursive Functions*, Amsterdam: North-Holland.

[^kreisel-1958]: Kreisel, G., 1958, “Elementary completeness properties of intuitionistic logic with a note on negations of prenex formulas,” *Journal of Symbolic Logic*, 23: 317–330.

[^kreisel-1962]: –––, 1962, “On weak completeness of intuitionistic predicate logic,” *Journal of Symbolic Logic*, 27: 139–158.

[^kripke-1965]: Kripke, S. A., 1965, “Semantical analysis of intuitionistic logic,” in J. Crossley and M. A. E. Dummett (eds.) 1965: 92–130.

[^kripke-2019]: –––, 2019, “Free choice sequences: A temporal interpretation compatible with acceptance of classical mathematics,” *Indag.Math.*, 30: 492–499.

[^krol-1978]: Krol, M., 1978, “A topological model of intuitionistic analysis with Kripke’s Schema,” *Zeitschrift für Math. Logik und Grundlagen der Math.*, 24: 427–436.

[^leivant-1979]: Leivant, D., 1979, “Maximality of Intuitionistic Logic,” Mathematical Centre Tracts 73, Mathematisch Centrum, Amsterdam.

[^leivant-1985]: –––, 1985, “Syntactic translations and provably recursive functions,” *Journal of Symbolic Logic*, 50: 682–688.

[^läuchli-1970]: Läuchli, H., 1970, “An abstract notion of realizability for which intuitionistic predicate calculus is complete,” in A. Kino et al. (eds.) 1965: 227–234.

[^lifschitz-1979]: Lifschitz, V., 1979, “CT$_0$ is stronger than CT$_0$!,” *Proceedings of the American Mathematical Society*, 73(1): 101–106.

[^mancosu-1998]: Mancosu, P., 1998, *From Brouwer to Hilbert: The Debate on the Foundations of Mathematics in the 1920s*, New York and Oxford: Oxford University Press.

[^martin-löf-1984]: Martin-Löf, P., 1984, *Intuitionistic Type Theory*, Notes by Giovanni Sambin of a series of lectures given in Padua, June 1980, Napoli: Bibliopolis.

[^mints-2012]: Mints, G., 2012, “The Gödel–Tarski translations of intuitionistic propositional formulas,” in *Correct Reasoning* (Lecture Notes in Computer Science 7265), E. Erdem et al. (eds.), Dordrecht: Springer-Verlag: 487–491.

[^mints-2013]: Mints, G., Olkhovikov, G. and Urquhart, A., 2013, “Failure of interpolation in the intuitionistic logic of constant domains,” *Journal of Symbolic Logic* 78(3): 937–950.

[^moschovakis-1971]: Moschovakis, J. R., 1971, “Can there be no nonrecursive functions?,” *Journal of Symbolic Logic*, 36: 309–315.

[^moschovakis-2003]: –––, 2003, “Classical and constructive hierarchies in extended intuitionistic analysis,” *Journal of Symbolic Logic*, 68: 1015–1043.

[^moschovakis-2009]: –––, 2009, “The logic of Brouwer and Heyting,” in *Logic from Russell to Church* (*Handbook of the History of Logic*, Volume 5), J. Woods and D. Gabbay (eds.), Amsterdam: Elsevier: 77–125.

[^moschovakis-2017]: –––, 2017, “Intuitionistic analysis at the end of time,” *Bulletin of Symbolic Logic*, 23: 279–295.

[^myhill-1967]: Myhill, J., 1967, “Notes toward an axiomatization of intuitionistic analysis,” *Logique et Analyse* 9: 280–297.

[^nelson-1947]: Nelson, D., 1947, “Recursive functions and intuitionistic number theory,” *Transactions of the American Mathematical Society*, 61: 307–368.

[^nishimura-1960]: Nishimura, I., 1960, “On formulas of one variable in intuitionistic propositional calculus,” *Journal of Symbolic Logic*, 25: 327–331.

[^oosten-1991]: van Oosten, J., 1991, “A semantical proof of de Jongh’s theorem,” *Archives for Mathematical Logic*, 31: 105–114.

[^oosten-2002]: –––, 2002, “Realizability: a historical essay,” *Mathematical Structures in Computer Science*, 12: 239–263.

[^oosten-2008]: –––, 2008, *Realizability: An Introduction to its Categorical Side*, Amsterdam: Elsevier.

[^plisko-1992]: Plisko, V. E., 1992, “On arithmetic complexity of certain constructive logics,” *Mathematical Notes*, (1993): 701–709. Translated from *Matematicheskie Zametki*, 52 (1992): 94–104.

[^plotkin-1986]: Plotkin, G. and Stirling, C., 1986, “A framework for intuitionistic modal logic,” in *TARK ’86: Proceedings of the 1986 conference on theoretical aspects of reasoning about knowledge*, J. Halpern (ed.), Morgan Kaufmann Publishers, Los Altos 1986: 399–406. Abstract in *Journal of Symbolic Logic* 53(2): 669.

[^rasiowa-1974]: Rasiowa, H., 1974, *Algebraic Approach to Non-Classical Logics*, Amsterdam: North-Holland.

[^rasiowa-1963]: Rasiowa, H. and Sikorski, R., 1963, *The Mathematics of Metamathematics*, Warsaw: Panstwowe Wydawnictwo Naukowe.

[^rathjen-2006]: Rathjen, M., 2006, “Realizability for constructive Zermelo-Fraenkel set theory,” in *Logic Colloquium 2003* (Lecture Notes in Logic 24), J. Väänänen et al. (eds.), A. K. Peters 2006: 282–314.

[^rathjen-2012]: –––, 2012, “From the weak to the strong existence property,” *Annals of Pure and Applied Logic*, 163: 1400–1418.

[^rose-1953]: Rose, G. F., 1953, “Propositional calculus and realizability,” *Transactions of the American Mathematical Society*, 75: 1–19.

[^ruitenberg-1991]: Ruitenberg, W., 1991, “The unintended interpretations of intuitionistic logic”, in: T. Drucker (ed.), *Perspectives on the History of Mathematical Logic*, Birkhauser 1991: 134–160.

[^rybakov-1997]: Rybakov, V., 1997, *Admissibility of Logical Inference Rules*, Amsterdam: Elsevier.

[^scott-1968]: Scott, D., 1968, “Extending the topological interpretation to intuitionistic analysis,” *Compositio Mathematica*, 20: 194–210.

[^shulman-2022]: Shulman, M., 2022, “Affine logic for constructive mathematics”, *Bulletin of Symbolic Logic*, 28: 327–386.

[^simpson-1994]: Simpson, A. K., 1994, *The proof theory and semantics of intuitionistic modal logic*, Doctoral dissertation, University of Edinburgh.

[^smorynski-1973]: Smorynski, C. A., 1973, “Applications of Kripke models,” in Troelstra (ed.) 1973: 324–391.

[^spector-1962]: Spector, C., 1962, “Provably recursive functionals of analysis: a consistency proof of analysis by an extension of principles formulated in current intuitionistic mathematics,” *Recursive Function Theory: Proceedings of Symposia in Pure Mathematics*, Volume 5, J. C. E. Dekker (ed.), Providence, RI: American Mathematical Society, 1–27.

[^stigt-1990]: van Stigt, W. P., 1990, *Brouwer’s Intuitionism*, Amsterdam: North-Holland.

[^stone-1937]: Stone, M. H., 1937, “Topological representation of distributive lattices and Brouwerian logics”, *Casopis Pest. Mat. Fys.*, 67: 1–25.

[^swart-1976]: Swart, H. C. M. de, 1976, “Another intuitionistic completeness proof,” *Journal of Symbolic Logic* 41: 644–662.

[^tarski-1938]: Tarski, A., 1938, “Der Aussagenkalkül und die Topologie”, *Fundamenta Mathematicae*, 31: 103–134.

[^tennant-2017]: Tennant, N., 2017, *Core Logic*, Oxford University Press, Oxford.

[^troelstra-1977]: Troelstra, A. S., 1977, *Choice Sequences: A Chapter of Intuitionistic Mathematics*, Oxford Logic Guides, Clarendon Press, Oxford.

[^troelstra-1991]: –––, 1991, “History of constructivism in the twentieth century,” ITLI Prepublication Series ML–1991–05, Amsterdam. Final version in *Set Theory, Arithmetic and Foundations of Mathematics* (Lecture Notes in Logic 36), J. Kenney and R. Kossak (eds.), Association for Symbolic Logic, Ithaca, NY, 2011: 150–179.

[^troelstra-1998]: –––, 1998, “Realizability,” Chapter VI of Buss (ed.), 1998: 407–473.

[^troelstra-1958]: –––, Introductory note to 1958 and 1972, in Gödel, 1990: 217–241.

[^troelstra-1973]: Troelstra, A. S. (ed.), 1973, *Metamathematical Investigation of Intuitionistic Arithmetic and Analysis* (Lecture Notes in Mathematics 344), Berlin: Springer-Verlag. Corrections and additions available from the editor.

[^troelstra-2000]: Troelstra, A. S. and Schwichtenberg, H., 2000, *Basic Proof Theory* (Cambridge Tracts in Theoretical Computer Science: Volume 43), 2nd edition, Cambridge: Cambridge University Press.

[^troelstra-1988]: Troelstra, A. S. and van Dalen, D., 1988, *Constructivism in Mathematics: An Introduction*, 2 volumes, Amsterdam: North-Holland Publishing. [See also the *Corrections*, in Other Internet Resources.]

[^troelstra-1982]: Troelstra, A. S. and van Dalen, D. (eds.), 1982, *The L. E. J. Brouwer Centenary Symposium*, Amsterdam: North-Holland Publishing.

[^veldman-1976]: Veldman, W., 1976, “An intuitionistic completeness theorem for intuitionistic predicate logic,” *Journal of Symbolic Logic*, 41: 159–166.

[^veldman-1990]: –––, 1990, “A survey of intuitionistic descriptive set theory,” in P. P. Petkov (ed.), *Mathematical Logic, Proceedings of the Heyting Conference*, New York and London: Plenum Press, 155–174.

[^veldman-2005]: –––, 2005, “Two simple sets that are not positively Borel,” *Annals of Pure and Applied Logic*, 135: 151–209.

[^veldman-2021]: –––, 2021, “Intuitionism: An inspiration?,” *Jahresbericht der Deutscher Mathematiker-Vereinigung*, 123: 221–284.

[^vesley-1972]: Vesley, R. E., 1972, “Choice sequences and Markov’s principle,” *Compositio Mathematica*, 24: 33–53.

[^vesley-1970]: –––, 1970, “A palatable substitute for Kripke’s Schema,” in A. Kino et al. (eds.) 1970: 197ff.

[^visser-1999]: Visser, A., 1999, “Rules and arithmetics,” *Notre Dame Journal of Formal Logic*, 40: 116–140.

[^visser-2002]: –––, 2002, “Substitutions of $\Sigma^{0}_1$ sentences: explorations between intuitionistic propositional logic and intuitionistic arithmetic,” *Annals of Pure and Applied Logic*, 114: 227–271.

[^visser-2006]: –––, 2006, “Predicate logics of constructive arithmetical theories,” *Journal of Symbolic Logic*, 72: 1311–1326.
