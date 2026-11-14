# The Epsilon Calculus
**First published Fri May 3, 2002; substantive revision Thu Jul 18, 2024**

*Avigad, Jeremy, Zach, Richard*

The epsilon calculus is a logical formalism developed by David Hilbert in the service of his program in the foundations of mathematics. The epsilon operator is a term-forming operator which replaces quantifiers in ordinary predicate logic. Specifically, in the calculus, a term $\varepsilon x A$ denotes some $x$ satisfying $A(x)$, if there is one. In Hilbert’s Program, the epsilon terms play the role of ideal elements; the aim of Hilbert’s finitistic consistency proofs is to give a procedure which removes such terms from a formal proof. The procedures by which this is to be carried out are based on Hilbert’s epsilon substitution method. The epsilon calculus, however, has applications in other contexts as well. The first general application of the epsilon calculus was in Hilbert’s epsilon theorems, which in turn provide the basis for the first correct proof of Herbrand’s theorem. Variants of the epsilon operator have been applied in linguistics, computer science, and in the philosophy of language, mathematics, and science.

## 1. Overview

By the turn of the century David Hilbert and Henri Poincaré were recognized as the two most important mathematicians of their generation. Hilbert’s range of mathematical interests was broad, and included an interest in the foundations of mathematics: his *Foundations of Geometry* was published in 1899, and of the list of questions posed to the International Congress of Mathematicians in 1900, three addressed distinctly foundational issues.

Following the publication of Russell’s paradox, Hilbert presented an address to the Third International Congress of Mathematicians in 1904, where, for the first time, he sketched his plan to provide a rigorous foundation for mathematics via syntactic consistency proofs. But he did not return to the subject in earnest until 1917, when he began a series of lectures on the foundations of mathematics with the assistance of Paul Bernays. Although Hilbert was impressed by the work of Russell and Whitehead in their *Principia Mathematica*, he became convinced that the logicist attempt to reduce mathematics to logic could not succeed, due in particular to the non-logical character of their axiom of reducibility. At the same time, he judged the intuitionistic rejection of the law of the excluded middle as unacceptable to mathematics. Therefore, in order to counter concerns raised by the discovery of the logical and set-theoretic paradoxes, a new approach was needed to justify modern mathematical methods.

By the summer of 1920, Hilbert had formulated such an approach. First, modern mathematical methods were to be represented in formal deductive systems. Second, these formal systems were to be proved syntactically consistent, not by exhibiting a model or reducing their consistency to another system, but by a direct metamathematical argument of an explicit, “finitary” character. The approach became known as Hilbert’s program. The epsilon calculus was to provide the first component of this program, while his epsilon substitution method was to provide the second.

The epsilon calculus is, in its most basic form, an extension of first-order predicate logic with an “epsilon operation” that picks out, for any true existential formula, a witness to the existential quantifier. The extension is conservative in the sense that it does not add any new first-order consequences. But, conversely, quantifiers can be defined in terms of the epsilons, so first-order logic can be understood in terms of quantifier-free reasoning involving the epsilon operation. It is this latter feature that makes the calculus convenient for the purpose of proving consistency. Suitable extensions of the epsilon calculus make it possible to embed stronger, quantificational theories of numbers and sets in quantifier-free calculi. Hilbert expected that it would be possible to demonstrate the consistency of such extensions.

## 2. The Epsilon Calculus

In his Hamburg lecture in 1921 (1922), Hilbert first presented the idea of using such an operation to deal with the principle of the excluded middle in a formal system for arithmetic. These ideas were developed into the epsilon calculus and the epsilon substitution method in a series of lecture courses between 1921 and 1923, and in Hilbert’s (1923)[^hilbert-1923]. The final presentation of the epsilon-calculus can be found in Wilhelm Ackermann’s dissertation (1924).

This section will describe a version of the calculus corresponding to first-order logic, while extensions to first- and second-order arithmetic will be described below.

Let $L$ be a first-order language, which is to say, a list of constant, function, and relation symbols with specified arities. The set of epsilon terms and the set of formulae of $L$ are defined inductively, simultaneously, as follows:

- Each constant of $L$ is a term.
- Each variable is a term.
- If $s$ and $t$ are terms, then $s = t$ is a formula.
- If $s_1, \ldots, s_k$ are terms and $F$ is a $k$-ary function symbol of $L, F(s_1, \ldots, s_k)$ is a term.
- If $s_1, \ldots, s_k$ are terms and $R$ is a $k$-ary relation symbol of $L, R(s_1, \ldots, s_k)$ is a formula.
- If $A$ and $B$ are formulae, so are $(A \wedge B)$, $(A \vee B)$, $(A \rightarrow B)$, and $\neg A$.
- If $A$ is a formula and $x$ is a variable, $\varepsilon x A$ is a term.

Parentheses may be dropped when there is no ambiguity. Substitution and the notions of free and bound variable, are defined in the usual way; in particular, the variable $x$ becomes bound in the term $\varepsilon x A$. The intended interpretation is that $\varepsilon x A$ denotes *some* $x$ satisfying $A$, if there is one. Thus, the epsilon terms are governed by the following axiom (Hilbert’s “transfinite axiom”): $$ A(x) \rightarrow A(\varepsilon x A) $$ In addition, the epsilon calculus includes a complete set of axioms governing the classical propositional connectives, and axioms governing the equality symbol. The only rules of the calculus are the following:

- Modus ponens
- Substitution: from $A(x)$, conclude $A(t)$, for any term $t.$

Earlier forms of the epsilon calculus (such as that presented in Hilbert 1923)[^hilbert-1923] use a dual form of the epsilon operator, in which $\varepsilon x A$ returns a value *falsifying* $A(x)$. The version above was used in Ackermann’s dissertation (1924), and has become standard.

Note that the calculus just described is quantifier-free. Quantifiers can be *defined* as follows: $$ \begin{align} \exists x A(x) &\equiv A(\varepsilon x A) \\ \forall x A(x) &\equiv A(\varepsilon x (\neg A)) \end{align} $$ The usual quantifier axioms and rules can be derived from these, so the definitions above serve to embed first-order logic in the epsilon calculus. The converse is, however, not true: not every formula in the epsilon calculus is the image of an ordinary quantified formula under this embedding. Hence, the epsilon calculus is more expressive than the predicate calculus, simply because epsilon terms can be combined in more complex ways than quantifiers.

It is worth noting that epsilon terms are nondeterministic. For example, in a language with constant symbols $a$ and $b$, $\varepsilon x (x = a \vee x = b)$ is either $a$ or $b$, but the calculus leaves it entirely open as to which is the case. One can add to the calculus a schema of *extensionality*, $$ \forall x (A(x) \leftrightarrow B(x)) \rightarrow \varepsilon x A = \varepsilon x B $$ which asserts that the epsilon operator assigns the same witness to equivalent formulae $A$ and $B$. For many applications, however, this additional schema is not necessary.

## 3. The Epsilon Theorems

The second volume of Hilbert and Bernays’ *Grundlagen der Mathematik* (1939) provides an account of results on the epsilon-calculus that had been proved by that time. This includes a discussion of the first and second epsilon theorems with applications to first-order logic, the epsilon substitution method for arithmetic with open induction, and a development of analysis (that is, second-order arithmetic) with the epsilon calculus.

The first and second epsilon theorems are as follows:

**First epsilon theorem:** Suppose $\Gamma \cup \{A\}$ is a set of quantifier-free formulae not involving the epsilon symbol. If $A$ is derivable from $\Gamma$ in the epsilon calculus, then $A$ is derivable from $\Gamma$ in quantifier-free predicate logic.

**Second epsilon theorem:** Suppose $\Gamma \cup \{A\}$ is a set of formulae not involving the epsilon symbol. If $A$ is derivable from $\Gamma$ in the epsilon calculus, then $A$ is derivable from $\Gamma$ in predicate logic.

In the first epsilon theorem, “quantifier-free predicate logic” is intended to include the substitution rule above, so quantifier-free axioms behave like their universal closures. Since the epsilon calculus includes first-order logic, the first epsilon theorem implies that any detour through first-order predicate logic used to derive a quantifier-free theorem from quantifier-free axioms can ultimately be avoided. The second epsilon theorem shows that any detour through the epsilon calculus used to derive a theorem in the language of the predicate calculus from axioms in the language of the predicate calculus can also be avoided.

More generally, the first epsilon theorem establishes that quantifiers and epsilons can always be eliminated from a proof of a quantifier-free formula from other quantifier-free formulae. This is of particular importance for Hilbert’s program, since the epsilons play the role of ideal elements in mathematics. If quantifier-free formulae correspond to the “real” part of the mathematical theory, the first epsilon-theorem shows that ideal elements can be eliminated from proofs of real statements, provided the axioms are also real statements.

This idea is made precise in a certain general consistency theorem which Hilbert and Bernays derive from the first epsilon-theorem, which says the following: Let $F$ be any formal system which results from the predicate calculus by addition of constant, function, and predicate symbols plus true axioms which are quantifier- and epsilon-free, and suppose the truth of atomic formulae in the new language is decidable. Then $F$ is consistent in the strong sense that every derivable quantifier- and epsilon-free formula is true. Hilbert and Bernays use this theorem to give a finitary consistency proof of elementary geometry (1939, Sec 1.4).

The difficulty for giving consistency proofs for arithmetic and analysis consists in extending this result to cases where the axioms also contain ideal elements, i.e., epsilon terms.

*Further reading.* The original sources on the epsilon-calculus and the epsilon theorems (Ackermann 1924, Hilbert & Bernays 1939)[^ackermann-1924][^hilbert-1939] remain available only in German. Leisenring 1969 is a relatively modern book-length introduction to the epsilon calculus in English. The first and second epsilon theorem are described in detail in Zach 2017. Moser & Zach 2006 give a detailed analysis for the case without equality, and Miyamoto & Moser 2024 for the case with equality. The original proofs are given for axiomatic presentations of the epsilon-calculus. Maehara 1955 was the first to consider sequent calculus with epsilon terms. He showed how to prove the second epsilon theorem using cut elimination, and then strengthened the theorem to include the schema of extensionality (Maehara 1957)[^maehara-1957]. Baaz et al. 2018 give an improved version of the first epsilon theorem. Corrections to errors in the literature (including Leisenring’s book) can be found in Flannagan 1975; Ferrari 1987; and Yasuhara 1982. A variation of the epsilon calculus based on Skolem functions, and therefore compatible with first-order logic, is discussed in Davis & Fechter 1991.

## 4. Herbrand’s Theorem

Hilbert and Bernays used the methods of the epsilon calculus to establish theorems about first order logic that make no reference to the epsilon calculus itself. One such example is *Herbrand’s theorem* (Herbrand 1930; see Buss 1995, Girard 1982, and section 2.5 of Buss 1998)[^buss-1995][^buss-1998][^girard-1982][^herbrand-1930]. This is often formulated as the statement that if an existential formula $$ \exists x_1 \ldots \exists x_k A(x_1, \ldots, x_k) $$ is derivable in first-order predicate logic (without equality), where $A$ is quantifier-free, then there are sequences of terms $t_{1}^1, \ldots, t_{k}^1, \ldots, t_{1}^n, \ldots, t_k ^n$, such that $$ A(t_{1}^1, \ldots, t_k ^1) \vee \ldots \vee A(t_{1}^n, \ldots, t_k^n) $$ is a tautology. If one is dealing with first-order logic *with* equality, one has to replace “tautology” by “tautological consequence of substitution instances of the equality axioms”; we will use the term “quasi-tautology” to describe such a formula.

The version of Herbrand’s theorem just described follows immediately from the *Extended First Epsilon Theorem* of Hilbert and Bernays. Using methods associated with the proof of the second epsilon theorem, however, Hilbert and Bernays derived a stronger result that, like Herbrand’s original formulation, provides more information. To understand the two parts of the theorem below, it helps to consider a particular example. Let $A$ be the formula

$$ \exists x_1 \forall x_2 \exists x_3 \forall x_4 B(x_1, x_2, x_3, x_4) $$ where $B$ is quantifier-free. The negation of $A$ is equivalent to $$ \forall x_1 \exists x_2 \forall x_3 \exists x_4 \neg B(x_1, x_2, x _3, x_4). $$ By Skolemizing, i.e., using function symbols to witness the existential quantifiers, we obtain $$ \exists f_2, f_4 \forall x_1, x_3 \neg B(x_1, f_2 (x_1), x_3, f_4 (x_1, x_3)). $$ Taking the negation of this, we see that the original formula is “equivalent” to $$ \forall f_2, f_4 \exists x_1, x_3 B(x_1, f_2 (x_1), x_3, f_4 (x_1, x_3)). $$

The first clause of the theorem below, in this particular instance, says that the formula $A$ above is derivable in first-order logic if and only if there is a sequence of terms $t_{1}^1, t_{3}^1, \ldots, t_{1}^n, t_{3}^n$ in the expanded language with $f_2$ and $f_4$ such that $$ B(t_{1}^1, f_2 (t_{1}^1), t_{3}^1, f_4 (t_{1}^1,t_{3}^1)) \vee \ldots \vee B(t_{1}^n, f_2 (t_{1}^n), t_{3}^n, f_4 (t_{1}^n,t_{3}^n)) $$ is a quasi-tautology.

The second clause of the theorem below, in this particular instance, says that the formula $A$ above is derivable in first-order logic if and only if there are sequences of variables $x_{2}^1, x_{4}^1, \ldots, x_2^n, x_4 ^n$ and terms $s_{1}^1, s_{3}^1, \ldots, s_1^n, s_3 ^n$ in the *original language* such that $$ B(s_{1}^1, x_{2}^1, s_{3}^1, x_4 ^1 ) \vee \ldots \vee B(s_1^n, x_2^n, s_3^n, x_4^n ) $$ is a quasi-tautology, and such that $A$ is derivable from this formula using only the quantifier and idempotency rules described below.

More generally, suppose $A$ is any prenex formula, of the form $$ \mathbf{Q}_1 x_1 \ldots \mathbf{Q}_n x_n B(x_1, \ldots, x_n), $$ where $B$ is quantifier-free. Then $B$ is said to be the *matrix* of $A$, and an *instance of* $B$ is obtained by substituting terms in the language of $B$ for some of its variables. The *Herbrand normal form* $A^H$ of $A$ is obtained by

- deleting each universal quantifier, and
- replacing each universally quantified variable $x_i$ by $f_i (x_{i}^1,\ldots, x_{i}^{k(i)})$, where $x_{i}^1,\ldots, x_{i}^{k(i)}$ are the variables corresponding to the existential quantifiers preceding $\mathbf{Q}_i$ in $A$ (in order), and $f_i$ is a new function symbol designated for this role.

When we refer to an *instance* of the matrix of $A^H$, we mean a formula that is obtained by substituting terms in the expanded language in the matrix of $A^H$. We can now state Hilbert and Bernays’s formulation of

**Herbrand’s theorem.** (1) A prenex formula $A$ is derivable in the predicate calculus if and only if there is a disjunction of instances of the matrix of $A^H$ which is a quasi-tautology.

(2) A prenex formula $A$ is derivable in the predicate calculus if and only if there is a disjunction $\bigvee_j B_j$ of instances of the matrix of $A$, such that $\bigvee_j B_j$ is a quasi-tautology, and $A$ is derivable from $\bigvee_j B_j$ using the following rules:

- from $C_1 \vee \ldots \vee C_i (t) \vee \ldots \vee C_m$ conclude $C_1 \vee \ldots \vee \exists x C_i (x) \vee \ldots \vee C_m$ and
- from $C_1 \vee \ldots \vee C_i (x) \vee \ldots \vee C_m$ conclude $C_1 \vee \ldots \vee \forall xC_i (x) \vee \ldots \vee C_m$ (if $x$ not in $C_j$ for $j \ne i)$,

as well as the idempotence of $\vee$ (from $C \vee C \vee D$ conclude $C \vee D)$.

Herbrand’s theorem can also be obtained by using cut elimination, via Gentzen’s “midsequent theorem.” However, the proof using the second epsilon theorem has the distinction of being the first complete and correct proof of Herbrand’s theorem. Moreover, and this is seldom recognized, whereas the proof based on cut-elimination provides a bound on the length of the Herbrand disjunction only as a function of the cut rank and complexity of the cut formulas in the proof, the length obtained from the proof based on the epsilon calculus provides a bound as a function of the number of applications of the transfinite axiom, and the rank and degree of the epsilon-terms occurring therein. In other words, the length of the Herbrand disjunction depends only on the quantificational complexity of the substitutions involved, and, e.g., not at all on the propositional structure or the length of the proof.

The version of Herbrand’s theorem stated at the beginning of this section is essentially the special case of (2) in which the formula $A$ is existential. In light of this special case, (1) is equivalent to the assertion that a formula $A$ is derivable in first-order predicate logic if and only if $A^H$ is. The forward direction of this equivalence is much easier to prove; in fact, for any formula $A, A \rightarrow A^H$ is derivable in predicate logic. Proving the reverse direction involves eliminating the additional function symbols in $A^H$, and is much more difficult, especially in the presence of equality. It is here that epsilon methods play a central role.

Given a prenex formula, the *Skolem normal form* $A^S$ is defined dually to $A^H$, i.e., by replacing existentially quantified variables by witnessing functions. If $\Gamma$ is a set of prenex sentences, let $\Gamma^S$ denote the set of their Skolem normal forms. Using the deduction theorem and Herbrand’s theorem, it is not hard to show that the following are pairwise equivalent: $$ \begin{align} \Gamma &\text{ proves } A \\ \Gamma &\text{ proves } A^H \\ \Gamma^S &\text{ proves }A \\ \Gamma^S &\text{ proves } A^H \end{align} $$

A striking application of Herbrand’s theorem and related methods is found in Luckhardt’s (1989)[^luckhardt-1989] analysis of Roth’s theorem. For a discussion of useful extensions of Herbrand’s methods, see Sieg 1991. A model-theoretic version of this is discussed in Avigad 2002a.

## 5. The Epsilon Substitution Method and Arithmetic

As noted above, historically, the primary interest in the epsilon calculus was as a means to obtaining consistency proofs. Hilbert’s lectures from 1917–1918 already note that one can easily prove the consistency of propositional logic, by taking propositional variables and formulae to range over truth values 0 and 1, and interpreting the logical connectives as the corresponding arithmetic operations. Similarly, one can prove the consistency of predicate logic (or the pure epsilon calculus), by specializing to interpretations where the universe of discourse has a single element. These considerations suggest the following more general program for proving consistency:

- Extend the epsilon calculus in such a way as to represent larger portions of mathematics.
- Show, using finitary methods, that each proof in the extended system has a consistent interpretation.

For example, consider the language of arithmetic, with symbols for $0$, $1$, $+$, $\times$, $\lt$. Along with quantifier-free axioms defining the basic symbols, one can specify that the epsilon terms $\varepsilon x A(x)$ picks out the least value satisfying $A$, if there is one, with the following axiom: $$ \tag{*} A(x) \rightarrow A(\varepsilon x A(x)) \wedge \varepsilon x A(x) \le x $$ The result is a system that is strong enough to interpret first-order (Peano) arithmetic. Alternatively, one can take the epsilon symbol to satisfy the following axiom: $$ A(y) \rightarrow A(\varepsilon x A(x)) \wedge \varepsilon x A(x) \ne y + 1. $$

In other words, if there is any witness $y$ satisfying $A(y)$, the epsilon term returns a value whose predecessor does not have the same property. Clearly the epsilon term described by (*) satisfies the alternative axiom; conversely, one can check that given $A$, a value of $\varepsilon x (\exists z \le x A(x))$ satisfying the alternative axiom can be used to interpret $\varepsilon x A(x)$ in (*). One can further fix the meaning of the epsilon term with the axiom $$ \varepsilon x A(x) \ne 0 \rightarrow A(\varepsilon x A(x)) $$ which requires that if there is no witness to $A$, the epsilon term return 0. For the discussion below, however, it is most convenient to focus on (*) alone.

Suppose we wish to show that the system above is consistent; in other words, we wish to show that there is no proof of the formula $0 = 1$. By pushing all substitutions to the axioms and replacing free variables by the constant 0, it suffices to show that there is no propositional proof of $0 = 1$ from a finite set of closed instances of the axioms. For that, it suffices to show that, given any finite set of closed instances of axioms, one can assign numerical values to terms in such a way that all the axioms are true under the interpretation. Since the arithmetical operations $+$ and $\times$ can be interpreted in the usual way, the only difficulty lies in finding appropriate values to assign to the epsilon terms.

Hilbert’s *epsilon substitution method* can be described, roughly, as follows:

- Given a finite set of axioms, start by interpreting all epsilon terms as 0.
- Find an instance of the axiom (*) above that is false under the interpretation. This can only happen if one has a term t such that $A(t)$ is true in the interpretation, but either $A(\varepsilon x A(x))$ is false or the value of $t$ is smaller than the value of $\varepsilon x A(x)$.
- “Repair” the assignment by assigning to $\varepsilon x A(x)$ the value of $t$, and repeat the process.

A finitary consistency proof is obtained once it is shown in a finitarily acceptable manner that this process of successive “repairs” terminates. If it does, all critical formulas are true formulas without epsilon-terms.

This basic idea (the “Hilbertsche Ansatz”) was set out first by Hilbert in his 1922 talk (1923), and elaborated in lectures in 1922–23. The examples given there, however, only deal with proofs in which all instances of the transfinite axiom correspond to a single epsilon term $\varepsilon x A(x)$. The challenge was to extend the approach to more than one epsilon term, to nested epsilon terms, and ultimately to second-order epsilons (in order to obtain a consistency proof not just of arithmetic, but of analysis).

The difficulty in dealing with nested epsilon terms can be described as follows. Suppose one of the axioms in the proof is the transfinite axiom $$ B(y) \rightarrow B(\varepsilon y B(y)) $$ $\varepsilon y B(y)$ may, of course, occur in other formulae in the proof, in particular in other transfinite axioms, e.g., $$ A(x, \varepsilon y B(y)) \rightarrow A(\varepsilon x A(x, \varepsilon y B(y)), \varepsilon y B(y)) $$ So first, it seems necessary to find a correct interpretation for $\varepsilon y B(y)$ before we attempt to find one for $\varepsilon x A(x, \varepsilon y B(y))$. However, there are more complicated patterns in which epsilon terms may occur in a proof. An instance of the axiom, which plays a role in determining the correct interpretation for $\varepsilon y B(y)$ might be $$ B(\varepsilon x A(x, \varepsilon y B(y))) \rightarrow B(\varepsilon y B(y)) $$ If $B$(0) is false, then in the first round of the procedure $\varepsilon y B(y)$ will be interpreted by 0. A subsequent change of the interpretation of $\varepsilon x A(x, 0)$ from 0 to, say, $n$, will result in an interpretation of this instance as $B(n) \rightarrow B$(0) which will be false if $B(n)$ is true. So the interpretation of $\varepsilon y B(y)$ will have to be corrected to $n$, which, in turn, might result in the interpretation of $\varepsilon x A(x, \varepsilon y B(y))$ to no longer be a true formula.

This is just a sketch of the difficulties involved in extending Hilbert’s idea to the general case. Ackermann (1924)[^ackermann-1924] provided such a generalization using a procedure which “backtracks” whenever a new interpretation at a given stage results in the need to correct an interpretation already found at a previous stage.

Ackermann’s procedure applied to a system of second-order arithmetic, in which, however, second order terms were restricted so as to exclude cross-binding of second-order epsilons. This amounts, roughly, to a restriction to arithmetic comprehension as the set-forming principle available (see the discussion at the end of this section). Further difficulties with second-order epsilon terms surfaced, and it quickly became apparent that the proof as it stood was fallacious. However, no one in Hilbert’s school realized the extent of the difficulty until 1930, when Gödel announced his incompleteness results. Until then, it was believed that the proof (at least with some modifications introduced by Ackermann, some of which involved ideas from von Neumann’s (1927)[^neumann-1927] version of the epsilon substitution method) would go through at least for the first-order part. Hilbert and Bernays (1939) suggest that the methods used only provides a consistency proof for first-order arithmetic with open induction. In 1936, Gerhard Gentzen succeeded in giving a proof of the consistency of first-order arithmetic in a formulation based on predicate logic without the epsilon symbol. This proof uses transfinite induction up to $\varepsilon_0$. Ackermann (1940)[^ackermann-1940] was later able to adapt Gentzen’s ideas to give a correct consistency proof of first-order arithmetic using the epsilon-substitution method.

Even though Ackermann’s attempts at a consistency proof for second-order arithmetic were unsuccessful, they provided a clearer understanding of the use of second-order epsilon terms in the formalization of mathematics. Ackermann used second-order epsilon terms $\varepsilon f\ A(f)$, where $f$ is a function variable. In analogy with the first-order case, $\varepsilon f\ A(f)$ is a function for which $A(f)$ is true, e.g., $\varepsilon f (x + f(x) = 2x)$ is the identity function $f(x) = x$. Again in analogy with the first-order case, one can use second-order epsilons to interpret second-order quantifiers. In particular, for any second-order formula $A(x)$ one can find a term $t(x)$ such that $$ A(x) \leftrightarrow t(x) = 1 $$ is derivable in the calculus (the formula $A$ may have other free variables, in which case these appear in the term $t$ as well). One can then use this fact to interpret *comprehension* principles. In a language with function symbols, these take the form $$ \exists f \forall x (A(x) \leftrightarrow f(x) = 1) $$ for an arbitrary formula $A(x)$. Comprehension is more commonly expressed in terms of set variables, in which case it takes the form $$ \exists Y \forall x (A(x) \leftrightarrow x \in Y), $$ asserting that every second order formula, with parameters, defines a set.

*Analysis*, or *second-order arithmetic*, is the extension of first-order arithmetic with the comprehension schema for arbitrary second-order formulae. The theory is *impredicative* in that it allows one to define sets of natural numbers using quantifiers that range over the entire universe of sets, including, implicitly, the set being defined. One can obtain *predicative* fragments of this theory by restricting the type of formulae allowed in the comprehension axiom. For example, the restriction discussed in connection with Ackermann above corresponds to the *arithmetic comprehension schema*, in which formulae do not involve second-order quantifiers. There are various ways of obtaining stronger fragments of analysis that are nonetheless predicatively justified. For example, one obtains *ramified analysis* by associating an ordinal rank to set variables; roughly, in the definition of a set of a given rank, quantifiers range only over sets of lower rank, i.e., those whose definitions are logically prior.

*Further Reading*. Hilbert’s and Ackermann’s early proofs are discussed in Zach 2003; 2004. Von Neumann’s proof is the topic of Bellotti 2016. Ackermann’s 1940 proof is discussed in Hilbert & Bernays 1970, and Wang 1963. A modern presentation is given by Moser 2006. An early application of epsilon substitution is the no-counterexample interpretation (Kreisel 1951)[^kreisel-1951].

## 6. More Recent Developments

In this section we discuss the development of the epsilon-substitution method for obtaining consistency results for strong systems; these results are of a mathematical nature. We cannot, unfortunately, discuss the details of the proofs here but would like to indicate that the epsilon-substitution method did not die with Hilbert’s program, and that a significant amount of current research is carried out in epsilon-formalisms.

Gentzen’s consistency proofs for arithmetic launched a field of research known as *ordinal analysis*, and the program of measuring the strength of mathematical theories using ordinal notations is still pursued today. This is particularly relevant to the *extended Hilbert’s program*, where the goal is to justify classical mathematics relative to constructive, or quasi-constructive, systems. Gentzen’s methods of cut-elimination (and extensions to infinitary logic developed by Paul Lorentzen, Petr Novikov, and Kurt Schütte) have, in large part, supplanted epsilon substitution methods in these pursuits. But epsilon calculus methods provide an alternative approach, and there is still active research on ways to extend Hilbert-Ackermann methods to stronger theories. The general pattern remains the same:

1. Embed the theory under investigation in an appropriate epsilon calculus.
2. Describe a process for updating assignments to the epsilon terms.
3. Show that the procedure is normalizing, i.e., given any set of terms, there is a sequence of updates that results in an assignment that satisfies the axioms.

Since the last step guarantees the consistency of the original theory, from a foundational point of view one is interested in the methods used to prove normalization. For example, one obtains an *ordinal analysis* by assigning ordinal notations to steps in the procedure, in such a way that the value of a notation decreases with each step.

In the 1960’s, Tait (1960, 1965, 2010)[^tait-1960][^tait-1965][^tait-2010] extended Ackermann’s methods to obtain an ordinal analysis of extensions of arithmetic with principles of transfinite induction. More streamlined and modern versions of this approach can be found in Mints 2001 and Avigad 2002b. More recently, Mints, Tupailo, and Buchholz have considered stronger, yet still predicatively justifiable, fragments of analysis, including theories of arithmetic comprehension and a $\Delta^{1}_1$-comprehension rule (Mints, Tupailo & Buchholz 1996; Mints & Tupailo 1999; see also Mints 2016)[^mints-1996][^mints-1999][^mints-1996-2]. Arai 2002 has extended the epsilon substitution method to theories that allow one to iterate arithmetic comprehension along primitive recursive well orderings. In particular, his work yields ordinal analyses for predicative fragments of analysis involving transfinite hierarchies and transfinite induction.

Some first steps have been taken in using the epsilon substitution method in the analysis of *impredicative* theories (see Arai 2003, 2006 and Mints 2015)[^arai-2003][^arai-2006][^mints-2015].

A variation on step 3 above involves showing that the normalization procedure is not sensitive to the choice of updates, which is to say, *any* sequence of updates terminates. This is called *strong normalization.* Mints 1996 has shown that many of the procedures considered have this stronger property.

In addition to the traditional, foundational branch of proof theory, today there is a good deal of interest in *structural proof theory*, a branch of the subject that focuses on logical deductive calculi and their properties. This research is closely linked with issues relevant to computer science, having to do with automated deduction, functional programming, and computer aided verification. Here, too, Gentzen-style methods tend to dominate (see again the entry on proof theory). But the epsilon calculus can also provide valuable insights; cf. for example Aguilera & Baaz 2019, or the discussion of Herbrand’s theorem above.

Aside from the investigations of the epsilon calculus in proof theory, two applications should be mentioned. One is the use of epsilon notation in Bourbaki’s *Theorie des ensembles* (1958). The second, of perhaps greater current interest, is the use of the epsilon-operator in the theorem-proving systems [HOL](https://www.cl.cam.ac.uk/Research/HVG/HOL/) and [Isabelle](https://www.cl.cam.ac.uk/Research/HVG/Isabelle/), where the expressive power of epsilon-terms yields significant practical advantages.

## 7. Epsilon Operators in Linguistics, Philosophy, and Non-classical Logics

Reading the epsilon operator as an indefinite choice operator (“an $x$ such that $A(x)$”) suggests that it might be a useful tool in the analysis of indefinite and definite noun phrases in formal semantics. The epsilon notation has in fact been so used, and this application has proved useful in particular in dealing with anaphoric reference.

Consider the familiar example

1. Every farmer who owns a donkey beats it.

The generally accepted analysis of this sentence is given by the universal sentence

1. $\forall x \forall y (\mathrm{Farmer}(x) \wedge \mathrm{Donkey}(y) \wedge \mathrm{Owns}(x, y)) \rightarrow \mathrm{Beats}(x, y))$

The drawback is that “a donkey” suggest an existential quantifier, and thus the analysis should, somehow, parallel in form the analysis of sentence 3 given by 4:

1. Every farmer who owns a donkey is happy,
2. $\forall x (\mathrm{Farmer}(x) \wedge \exists y (\mathrm{Donkey}(y) \wedge \mathrm{Owns}(x, y)) \rightarrow \mathrm{Happy}(x))$,

but the closest possible formalization,

1. $\forall x ((\mathrm{Farmer}(x) \wedge \exists y (\mathrm{Donkey}(y) \wedge \mathrm{Owns}(x, y)) \rightarrow \mathrm{Beats}(x, y))$

contains a free occurrence of $y$. Evans 1980 suggests that since pronouns are referring expressions, they should be analyzed as definite descriptions; and if the pronoun occurs in the consequent of a conditional, the descriptive conditions are determined by the antecedent. This leads to the following E-type analysis of (1): $$ \begin{align*} & &\forall x ((\mathrm{Farmer}(x) \wedge \exists y (\mathrm{Donkey}(y) \wedge \mathrm{Owns}(x, y)) \rightarrow\\ & &(\mathrm{Beats}(x, \iota y (\mathrm{Donkey}(y) \wedge \mathrm{Owns}(x, y))) \end{align*} $$ Here, $\iota x$ is the definite description operator, so $\iota y (\mathrm{Donkey}(y) \wedge \mathrm{Owns}(x, y))$ is “the donkey owned by $x$;”. The trouble with this is that on the standard analysis, the definite description carries a uniqueness condition, and so (5) will be false if there is a farmer who owns more than one donkey. A way out of this is to introduce a new operator, whe (whoever, whatever) which works as a generalized quantifier (Neale, 1990)[^neale-1990]:

$$ \begin{align*} & &\forall x ((\mathrm{Farmer}(x) \wedge \exists y (\mathrm{Donkey}(y) \wedge \mathrm{Owns}(x, y)) \rightarrow\\ & & (\mathrm{Beats}(x, \mathrm{whe}\, y (\mathrm{Donkey}(y) \wedge \mathrm{Owns}(x, y))) \end{align*} $$

As pointed out by von Heusinger (1994)[^heusinger-1994], this suggests that Neale is committed to pronouns being ambiguous between definite descriptions $(\iota$-expressions) and whe-expressions. Heusinger suggests instead to use epsilon operators indexed by choice functions (which depend on the context). According to this approach, the analysis of (1) is

> For every choice function $i$: $$\begin{align*} & &\forall x ((\mathrm{Farmer}(x) \wedge \mathrm{Owns}(x, \varepsilon_i y \mathrm{Donkey} (y)) \rightarrow \\ & &\mathrm{Beats} (x, \varepsilon_{a^*}y \mathrm{Donkey} (y)) \end{align*} $$

Here $a^*$ is a choice function which depends on $i$ and the antecedent of the conditional: If $i$ is a choice function which selects $\varepsilon_i y \mathrm{Donkey}(y)$ from the set of all donkeys, then $\varepsilon_{a^*}y \mathrm{Donkey} (y)$ selects from the set of donkeys owned by $x$.

This approach to dealing with pronouns using epsilon operators indexed by choice functions enable von Heusinger to deal with a wide variety of circumstances (see Egli & von Heusinger 1995; von Heusinger 2000)[^egli-1995][^heusinger-2000][^heusinger-2000-2].

Applications of the epsilon-operator in formal semantics, and choice functions in general, have received significant interest from linguists. Von Heusinger & Egli 2000a list, among others, the following: representations of questions (Reinhart 1992)[^reinhart-1992], specific indefinites (Reinhart 1992; 1997; Winter 1997)[^reinhart-1992][^winter-1997], E-type pronouns (Hintikka & Kulas 1985; Slater 1986; Chierchia 1992, Egli & von Heusinger 1995)[^chierchia-1992][^egli-1995][^hintikka-1985][^slater-1986] and definite noun phrases (von Heusinger 1997, 2004)[^heusinger-1997][^heusinger-2004][^heusinger-2004-2]. Gratzl & Schiemer 2017 provide a comparison between Russell’s and Hilbert’s approaches to dealing with indefinites.

For discussion of the issues and applications of the epsilon operator in linguistics and philosophy of language, see B. H. Slater’s article on epsilon calculi (cited in the Other Internet Resources section below), and the collections von Heusinger & Egli 2000 and von Heusinger & Kempson 2004.

Another application of epsilon calculus is as a general logic for reasoning about arbitrary objects. Meyer Viol 1995a provides a comparison of the epsilon calculus with Fine’s 1985 theory of arbitrary objects. Indeed, the connection is not hard to see. Given the equivalence $\forall x A(x) \equiv$ A$(\varepsilon x (\neg A))$, the term $\varepsilon x (\neg A)$ is an arbitrary object in the sense that it is an object of which $A$ is true iff $A$ is true generally. The connection between $\varepsilon$-terms and Fine’s arbitrary object theory is exploited for philosophical purposes by Bonatti 2022 (abstraction in mathematics), Genco et al 2021 (grounding), and Sandu 2020 (indefinites).)

In his 1961, Carnap proposed to use the $\varepsilon$-operator to reconstruct the theoretical part of scientific theories (a proposal similar to Ramseyfication; see the entry on theoretical terms in science and [Supplement E to the entry on Carnap](https://plato.stanford.edu/entries/carnap/reconstruct-sci-theories.html#TheoTermSentLogiStruTheo)). This proposal is discussed by Schiemer & Gratzl 2016. Leitgeb 2023 considers an $\varepsilon$-version of Ramsey sentences in the context of a semantics of indeterminacy.

Meyer Viol’s papers 1995a, 1995b contain further proof- and model-theoretic studies of the epsilon calculus; specifically intuitionistic epsilon calculi. Here, the epsilon theorems no longer hold, i.e., introduction of epsilon terms produces non-conservative extensions of intuitionistic logic. Other investigations of epsilon operators in intuitionistic logic can be found in Shirai 1971, Bell 1993a, 1993b, DeVidi 1995, and Baaz & Zach 2022. For epsilon-operators in many-valued logics, see Mostowski 1963, for modal epsilon calculus, Fitting 1975.

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=epsilon-calculus). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/epsilon-calculus/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=epsilon-calculus&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/epsilon-calculus/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

- [Epsilon Calculi](http://www.utm.edu/research/iep/e/ep-calc.htm) by B. Hartley Slater (Internet Encyclopedia of Philosophy).

Please contact the authors with further suggestions.

## Related Entries

anaphora | finitism | Hilbert, David | Hilbert, David: program in the foundations of mathematics | logic: classical | mathematics, philosophy of | proof theory | quantifiers and quantification | theoretical terms in science

[^aguilera-2019]: Aguilera, J.P., and M. Baaz, 2019, ‘Unsound inferences make proofs shorter’. *Journal of Symbolic Logic*, 84: 102–122.

[^ackermann-1924]: Ackermann, W., 1924, ‘Begründung des ’’tertium non datur’’ mittels der Hilbertschen Theorie der Widerspruchsfreiheit’, *Mathematische Annalen*, 93: 1–36.

[^ackermann-1937]: –––, 1937–38, ‘Mengentheoretische Begründung der Logik’, *Mathematische Annalen*, 115: 1–22.

[^ackermann-1940]: –––, 1940, ‘Zur Widerspruchsfreiheit der Zahlentheorie’, *Mathematische Annalen*, 117: 162–194.

[^arai-2002]: Arai, T., 2002, ‘Epsilon substitution method for theories of jump hierarchies’, *Archive for Mathematical Logic*, 2: 123–153.

[^arai-2003]: –––, 2003, ‘Epsilon substitution method for ID$_1 (\Pi^{0}_1 \vee \Sigma^{0}_1)$’, *Annals of Pure and Applied Logic*, 121: 163–208.

[^arai-2006]: –––, 2006, ‘Epsilon substitution method for $\Pi^{0}_2$-FIX. *Journal of Symbolic Logic*, 71: 1155–1188

[^avigad-2002a]: Avigad, J., 2002a, ‘Saturated models of universal theories’, *Annals of Pure and Applied Logic*, 118: 219–234.

[^avigad-2002b]: –––, 2002b, ‘Update procedures and the 1-consistency of arithmetic’, *Mathematical Logic Quarterly*, 48: 3–13.

[^baaz-2018]: Baaz, M., A. Leitsch, and A. Lolic, 2018, ‘A sequent-calculus based formulation of the extended first epsilon theorem’, in: Artemov, S., Nerode, A. (eds.), *Logical Foundations of Computer Science*, Berlin: Springer, 55–71.

[^baaz-2022]: Baaz, M., and R. Zach, 2022, ‘Epsilon theorems in intermediate logics’, *The Journal of Symbolic Logic*, 87(2): 682–720.

[^bell-1993a]: Bell, J. L., 1993a. ‘Hilbert’s epsilon-operator and classical logic’, *Journal of Philosophical Logic*, 22: 1–18.

[^bell-1993b]: –––, 1993b. ‘Hilbert’s epsilon operator in intuitionistic type theories’, *Mathematical Logic Quarterly*, 39: 323–337.

[^bellotti-2016]: Bellotti, L., 2016, ‘Von Neumann’s consistency proof’, *Review of Symbolic Logic*, 9: 429–455.

[^bonatti-2022]: Bonatti, N., 2022, ‘A reassessment of cantorian abstraction based on the ε-operator’, *Synthese*, 200(5): 396.

[^bourbaki-1958]: Bourbaki, N., 1958, *Theorie des ensembles*, Paris: Hermann.

[^buss-1995]: Buss, S., 1995, ‘On Herbrand’s theorem’, *Logic and Computational Complexity* (Lecture Notes in Computer Science 960), Berlin: Springer, 195–209.

[^buss-1998]: ––– 1998, ‘Introduction to proof theory’, in: Buss (ed.), *The Handbook of Proof Theory*, Amsterdam: North-Holland, 1–78.

[^chierchia-1992]: Chierchia, G., 1992, ‘Anaphora and dynamic logic’. *Linguistics and Philosophy*, 15: 111–183.

[^davis-1991]: Davis, M., and R. Fechter, 1991, ‘A free variable version of the first-order predicate calculus’, *Journal of Logic and Computation*, 1: 431–451.

[^devidi-1995]: DeVidi, D., 1995, ‘Intuitionistic $\varepsilon$- and $\tau$-calculi’, *Mathematical Logic Quarterly*, 41: 523–546.

[^egli-1995]: Egli, U., and K. von Heusinger, 1995, ‘The epsilon operator and E-type pronouns’, in U. Egli *et al*. (eds.), *Lexical Knowledge in the Organization of Language*, Amsterdam: Benjamins, 121–141 (Current Issues in Linguistic Theory 114).

[^evans-1980]: Evans, G., 1980, ‘Pronouns’, *Linguistic Inquiry*, 11: 337–362.

[^ewald-1996]: Ewald, W. B. (ed.), 1996, *From Kant to Hilbert. A Source Book in the Foundations of Mathematics*, Vol. 2, Oxford: Oxford University Press.

[^ferrari-1987]: Ferrari, P. L., 1987, ‘A note on a proof of Hilbert’s second $\varepsilon$-theorem’, *Journal of Symbolic Logic*, 52: 214–215.

[^fine-1985]: Fine, K., 1985, *Reasoning with Arbitrary Objects*, Oxford: Blackwell.

[^fitting-1975]: Fitting, M., 1975, ‘A modal logic epsilon-calculus’, *Notre Dame Journal of Formal Logic*, 16: 1–16.

[^flannagan-1975]: Flannagan, T. B., 1975, ‘On an extension of Hilbert’s second $\varepsilon$-theorem’, *Journal of Symbolic Logic*, 40: 393–397.

[^genco-2021]: Genco, F. A., F. Poggiolesi, and L. Rossi, 2021, ‘Grounding, quantifiers, and paradoxes’, *Journal of Philosophical Logic*, 50(6): 1417–1448.

[^girard-1982]: Girard, J.-Y., 1982, ‘Herbrand’s theorem and proof theory’, *Proceedings of the Herbrand Symposium*, Amsterdam: North-Holland, 29-38.

[^gratzl-2017]: Gratzl, N., and G. Schiemer, 2017, ‘Two types of indefinites: Hilbert & Russell’, *IfCoLog Journal of Logics and Their Applications*, 4(2): 333–348.

[^herbrand-1930]: Herbrand, J., 1930, *Recherches sur la thèorie de la dèmonstration*, *Dissertation*, University of Paris. English translation in Herbrand 1971, pp. 44–202.

[^herbrand-1971]: –––, 1971, *Logical Writings*, W. Goldfarb (ed.), Cambridge, Mass.: Harvard University Press.

[^hilbert-1922]: Hilbert, D., 1922, ‘Neubegründung der Mathematik: Erste Mitteilung’, *Abhandlungen aus dem Seminar der Hamburgischen Universität*, 1: 157–177, English translation in Mancosu, 1998, 198–214 and Ewald, 1996, 1115–1134.

[^hilbert-1923]: –––, 1923, ‘Die logischen Grundlagen der Mathematik’, *Mathematische Annalen*, 88: 151–165; English translation in Ewald, 1996, 1134–1148.

[^hilbert-1934]: Hilbert, D., and P. Bernays, 1934, *Grundlagen der Mathematik* (Volume 1), Berlin: Springer.

[^hilbert-1939]: –––, 1939, *Grundlagen der Mathematik* (Volume 2), Berlin: Springer.

[^hilbert-1970]: –––, 1970, ‘Grundlagen der Mathematik’ (Volume 2), 2nd, edition, Berlin: Springer, Supplement V.

[^hintikka-1985]: Hintikka, J., and J. Kulas, 1985, *Anaphora and Definite Descriptions: Two Applications of Game-Theoretical Semantics*, Dordrecht: Reidel.

[^kempson-2001]: Kempson, R., W. Meyer Viol, and D. Gabbay, 2001, *Dynamic Syntax: The Flow of Language Understanding*, Oxford: Blackwell.

[^kreisel-1951]: Kreisel, G, 1951, ‘On the interpretation of non-finitist proofs – part I’, *Journal of Symbolic Logic*, 16: 241–267.

[^leisenring-1969]: Leisenring, A. C., 1969, *Mathematical Logic and Hilbert’s Epsilon-Symbol*, London: Macdonald.

[^leitgeb-2023]: Leitgeb, H., 2023, ‘Ramsification and semantic indeterminacy’, *The Review of Symbolic Logic*, 16(3): 900–950.

[^luckhardt-1989]: Luckhardt, H., 1989, ‘Herbrand-Analysen zweier Beweise des Satzes von Roth: Polynomiale Anzahlschranken’, *Journal of Symbolic Logic*, 54: 234–263.

[^maehara-1955]: Maehara, S., 1955, ‘The predicate calculus with $\varepsilon$-symbol’, *Journal of the Mathematical Society of Japan*, 7: 323–344.

[^maehara-1957]: –––, 1957, ‘Equality axiom on Hilbert’s $\varepsilon$-symbol’, *Journal of the Faculty of Science*, University of Tokyo, Section 1, 7: 419–435.

[^mancosu-1998]: Mancosu, P. (ed.), 1998, *From Brouwer to Hilbert. The Debate on the Foundations of Mathematics in the 1920s*, Oxford: Oxford University Press.

[^meyer-1995a]: Meyer Viol, W. P. M., 1995a, *Instantial Logic. An Investigation into Reasoning with Instances*, Ph.D. thesis, University of Utrecht. ILLC Dissertation Series 1995–11.

[^meyer-1995b]: –––, 1995b. ‘A proof-theoretic treatment of assignments’, *Bulletin of the IGPL*, 3: 223–243.

[^mints-1994]: Mints, G., 1994, ‘Gentzen-type systems and Hilbert’s epsilon substitution method. I’, *Logic, Methodology and Philosophy of Science, IX* (Uppsala, 1991), Amsterdam: North-Holland, 91-122.

[^mints-1996]: –––, 1996, ‘Strong termination for the epsilon substitution method’, *Journal of Symbolic Logic*, 61: 1193–1205.

[^mints-2001]: –––, 2001, ‘The epsilon substitution method and continuity’, in W. Sieg *et al*. (eds.), *Reflections on the Foundations of Mathematics: Essays in Honor of Solomon Feferman*, Lecture Notes in Logic 15, Association for Symbolic Logic.

[^mints-2008]: –––, 2008, ‘Cut Elimination for a simple formulation of epsilon calculus’, *Annals of Pure and Applied Logic*,152 (1–3): 148–160.

[^mints-2013]: –––, 2013, ‘Epsilon substitution for first- and second-order predicate logic’, *Annals of Pure and Applied Logic*, 164: 733–739.

[^mints-2015]: –––, 2015, ‘Non-deterministic epsilon substitution method for PA and ID$_1$’, in: Kahle, R., Rathjen, M. (Eds.), *Gentzen’s Centenary: The Quest for Consistency*, Berlin: Springer, pp. 479–500.

[^mints-1999]: Mints, G., and S. Tupailo, 1999, ‘Epsilon-substitution method for the ramified language and $\Delta^{1}_1$-comprehension rule’, in A. Cantini *et al*. (eds.), *Logic and Foundations of Mathematics* (Florence, 1995), Dordrecht: Kluwer, 107–130.

[^mints-1996-2]: Mints, G., S. Tupailo, and W. Buchholz, 1996, ‘Epsilon substitution method for elementary analysis’, *Archive for Mathematical Logic*, 35: 103–130.

[^miyamoto-2024]: Miyamoto, K., and G. Moser, 2024, ‘Herbrand complexity and the epsilon calculus with equality’, *Archive for Mathematical Logic*, 63(1): 89–118.

[^moser-2006]: Moser, G., 2006, ‘Ackermann’s substitution method (remixed)’, *Annals of Pure and Applied Logic*, 142(1–3): 1–18.

[^moser-2006-2]: Moser, G., and R. Zach, 2006, ‘The epsilon calculus and Herbrand complexity’, *Studia Logica*, 82(1): 133–155.

[^mostowski-1963]: Mostowski, A., 1963, ‘The Hilbert epsilon function in many-valued logics’, *Acta Philosophica Fennica*, 16: 169–188.

[^neale-1990]: Neale, S., 1990, *Descriptions*, Cambridge, MA: MIT Press.

[^reinhart-1992]: Reinhart, T., 1992, ‘Wh-in-situ: An apparent paradox’, in P. Dekker and M. Stokhof (eds.). *Proceedings of the Eighth Amsterdam Colloquium*, December 17–20, 1991, ILLC, University of Amsterdam, 483–491.

[^reinhart-1997]: –––, 1997, ‘Quantifier scope: How labor is divided between QR and choice functions’. *Linguistics and Philosophy*, 20: 335–397.

[^sandu-2020]: Sandu, G., 2020, ‘Indefinites, Skolem functions, and arbitrary objects’, in M. Dumitru (ed.), *Metaphysics, Meaning, and Modality: Themes from Kit Fine*, Oxford: Oxford University Press, 98–112.

[^schiemer-2016]: Schiemer, G., and N. Gratzl, 2016, ‘The epsilon-reconstruction of theories and scientific structuralism’, *Erkenntnis*, 81(2): 407–432.

[^shirai-1971]: Shirai, K., 1971, ‘Intuitionistic predicate calculus with $\varepsilon$-symbol’, *Annals of the Japan Association for Philosophy of Science*, 4: 49–67.

[^sieg-1991]: Sieg, W., 1991, ‘Herbrand analyses’, *Archive for Mathematical Logic*, 30: 409–441.

[^slater-1986]: Slater, B. H., 1986, ‘E-type pronouns and $\varepsilon$-terms’, *Canadian Journal of Philosophy*, 16: 27–38.

[^slater-1988]: –––, 1988, ‘Hilbertian reference’, *Noûs*, 22: 283–97.

[^slater-1994]: –––, 1994, ‘The epsilon calculus’ problematic’, *Philosophical Papers*, 23: 217–42.

[^slater-2000]: –––, 2000, ‘Quantifier/variable-binding’, *Linguistics and Philosophy*, 23: 309–21.

[^tait-1960]: Tait, W. W., 1960, ‘The substitution method.’ *Journal of Symbolic Logic*, 30: 175–192.

[^tait-1965]: –––, 1965, ‘Functionals defined by transfinite recursion,’ *Journal of Symbolic Logic*, 30: 155–174.

[^tait-2010]: –––, 2010, ‘The substitution method revisited.’ in: S. Feferman and W. Sieg (eds.), *Proofs, Categories and Computations: Essays in Honor of Grigori Mints*, London: College Publications, pp. 131–14.

[^heusinger-1994]: von Heusinger, K., 1994, Review of Neale (1990). *Linguistics*, 32: 378–385.

[^heusinger-1997]: –––, 1997, ‘Definite descriptions and choice functions’, in S. Akama (ed.). *Logic, Language and Computation*, Dordrecht: Kluwer, 61–91.

[^heusinger-2000]: –––, 2000, ‘The Reference of Indefinites’, in von Heusinger and Egli, (2000), 265–284.

[^heusinger-2004]: –––, 2004, ‘Choice functions and the anaphoric semantics of definite NPs’, *Research in Language and Computation*, 2: 309–329.

[^heusinger-2000-2]: von Heusinger, K., and U. Egli (eds.), 2000, *Reference and Anaphoric Relations*, Dordrecht: Kluwer.

[^heusinger-2000a]: –––, 2000a. ‘Introduction: Reference and the Semantics of Anaphora’, in von Heusinger and Egli (2000), 1–13.

[^heusinger-2004-2]: von Heusinger, K., and R. Kempson (eds.), 2004, *Choice Functions in Semantics*, Special Issue of *Research on Language and Computation*, 2(3).

[^neumann-1927]: von Neumann, J., 1927, ‘Zur Hilbertschen Beweistheorie’, *Mathematische Zeitschrift*, 26: 1–46.

[^wang-1963]: Wang, H., 1963, *A Survey of Mathematical Logic*, Peking: Science Press.

[^winter-1997]: Winter, Y., 1997, ‘Choice functions and the scopal semantics of indefinites’. *Linguistics and Philosophy*, 20: 399–467.

[^yasuhara-1982]: Yasuhara, M., 1982, ‘Cut elimination in $\varepsilon$-calculi’, *Zeitschrift für mathematische Logik und Grundlagen der Mathematik*, 28: 311–316.

[^zach-2003]: Zach, R., 2003, ‘The practice of finitism. Epsilon calculus and consistency proofs in Hilbert’s Program’, *Synthese*, 137: 211–259.

[^zach-2004]: –––, 2004, ‘Hilbert’s “*Verunglückter Beweis*”, the first epsilon theorem, and consistency proofs’. *History and Philosophy of Logic*, 25: 79–94.

[^zach-2017]: –––, 2017, ‘Semantics and proof theory of the epsilon calculus’, in: Ghosh, S., Prasad, S. (Eds.), *Logic and Its Applications. ICLA 2017*, LNCS. Springer, Berlin, Heidelberg, pp. 27–47.
